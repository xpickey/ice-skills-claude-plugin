# 06 — Online and Marketplace (ช่องทางออนไลน์)

> **Load this when:** the brand sells through its own website, a regional marketplace, social or
> chat channels · the words marketplace, Shopee, Lazada, TikTok, cash on delivery, platform
> settlement, or "our online team" appear · online returns or overselling are a stated problem.
> **Do not load this for:** the brand's physical shops → **05 Owned Store** · what a *retailer*
> deducts → **10 Trade Spend and Net GP**.
> **Source basis:** the apparel implementation, where all four sub-models were designed and built.
> Settlement reconciliation design is reinforced by the food and beverage case's deduction work and
> by public practitioner sources.

## 1. Use cases — what this channel actually is

Online is not one channel. It is **at least four sub-models with different debtors, different
billing triggers and different reconciliation problems**. Treating them as one is the most common
online scoping error.

| Sub-model | Order origin | Order opens as | Billing trigger | **Who owes the money** |
|---|---|---|---|---|
| **Own website — prepaid** | brand storefront → API | **pending** | finance verifies receipt, then releases; invoice after fulfilment | the consumer |
| **Own website — cash on delivery** | brand storefront → API | **approved**, released immediately | invoice raised as cash on delivery | **the courier**, until it remits |
| **Marketplace** | platform → the brand's **API gateway** → API | **approved** | the gateway returns delivery confirmation; the ERP maps it to the shipment and **auto-creates the invoice** | **the platform**, on its settlement cycle |
| **Social / chat commerce** | conversation → sales confirms stock and attaches payment evidence → CRM | **pending** until finance verifies | as the wholesale chain | the consumer, evidence-based |

The recognisable situations: a fashion brand running its own storefront alongside three
marketplaces and a chat-based sales team · a food brand whose marketplace volume spikes on
double-digit campaign days · any consumer brand where the finance team reconciles platform payments
in a spreadsheet.

**Two decisions to carry into every prospect conversation:**

1. **Who is the debtor** — consumer, courier, or platform. Each produces a different receivable
   sub-ledger and a different reconciliation problem, and the client rarely states this unprompted.
2. **A brand-owned API gateway sits between the marketplaces and the ERP.** The ERP integrates once
   with the gateway; the gateway absorbs each platform's dialect. Without it, every new marketplace
   is a new ERP integration.

### Tax invoice on request — a standing decision node

Every online flow in the reference implementation carries an explicit branch: **does the customer
want a tax invoice?** Consumers request them selectively, so customer tax details are captured only
on that branch. This shapes the receivable design in every consumer-facing channel and is easy to
miss in scoping. Full context in file **17**.

## 2. Process — the flow

### Own website, prepaid

```
order placed on the storefront
  → customer tax details captured only if a tax invoice is requested
  → API creates the sales order and reserves stock, status PENDING
  → finance verifies the payment and approves release
  → API releases to the warehouse → fulfilment → confirmation
  → STOCK RELIEVED
  → AR invoice raised
  → receipt
```

### Own website, cash on delivery

Same until order creation, but the order opens **approved** and releases immediately. The invoice is
raised as a cash-on-delivery receivable and **collected from the courier**, not from the shopper.

### Marketplace

```
order on the platform
  → the brand's API GATEWAY receives it
  → gateway calls the ERP: create sales order + reserve, status APPROVED
  → release to warehouse → fulfilment → confirmation → STOCK RELIEVED
  → gateway returns DELIVERY CONFIRMATION
  → ERP maps confirmation to the shipment and AUTO-CREATES the AR invoice
  → billing collects from the PLATFORM on its settlement cycle
```

### Platform settlement — the three-way match

The step most often left as "a report to build later", and the one that keeps a finance team in a
spreadsheet forever if it is.

```
      ERP revenue                 Platform settlement report            Bank
 (invoices from confirmed      (per-order gross, each deduction,     (one net receipt
  deliveries)                   net payable)                          per cycle)
        │                                │                                 │
        └────── match by ORDER ──────────┴────── match by CYCLE total ──────┘
```

Three questions the design must answer:

1. **Did the platform pay for everything you shipped?** Missing orders mean revenue never
   recognised; extra ones mean revenue recognised for something cancelled.
2. **Were the deductions correct?** Commission at the agreed rate, shipping subsidy on the right
   orders, penalties explained.
3. **Does the platform's net equal the money that arrived?** A gap is either timing or error, and
   the two must be distinguishable.

**Match on the order, not the period** — returns and cancellations settle on a different cycle from
the original sale, so an order can appear as revenue in one period and as a deduction two periods
later.

### API and import mechanics — verified against the platforms' own interfaces (Thailand, 2026)

**Shopee Open API v2.** Orders come from `get_order_list` → `get_order_detail`. Settlement is per-order
via `get_escrow_detail`, whose published formula is the reconciliation spec in one line:
`escrow_amount = total_amount + voucher + credit_card_promotion + seller_rebate + coin − commission_fee
− credit_card_transaction_fee − cross_border_tax − service_fee − buyer_shopee_kredit −
seller_coin_cash_back + final_shipping_fee − seller_return_refund_amount`. Two design consequences:
the escrow value **moves until the order completes**, so pull it only after completion; and vouchers
arrive **already split seller-funded versus platform-funded**, so a design that merges them is
discarding a distinction the platform itself maintains (invariant 12).

**Lazada Open Platform.** Orders via `/orders/get` + `/order/items/get`. Settlement via the finance
group: `/finance/payout/status/get` for the payout cycles and `/finance/transaction/details/get` for
the line-level deductions. Access is app key/secret plus a **per-store token that expires** — token
refresh is part of the integration design, not an afterthought.

**Spreadsheet-import interim** (brands typically run a file-based bridge before the API build; the
platform order export carries 70+ columns of which a mapping usually selects 10-15). Five transforms
recur in every implementation and belong in the fit-gap as their own line items:
1. **Extract VAT from both item price and freight** before import when the ERP prices exclusive.
2. **Explode pack SKUs** — listing variants encoded as `<baseSKU>-<n>ea` must become base SKU × n
   with the unit price divided back, or stock relief is wrong by the pack factor.
3. **One one-time customer account per platform** — buyers are not created as customers; the
   platform is the debtor (consistent with the sub-model table above).
4. **Line-level unique reference** for idempotent re-import — one order carries many SKU lines, so
   order number alone cannot be the duplicate key.
5. **Carry the buyer's tax-invoice request fields** (requested flag, tax ID, contact number) —
   they are the trigger for per-order e-Tax issuance (file 17).
Pull only orders in **delivered** status, and design the pull window around the platform's
post-delivery return period: a return filed after import must produce a credit note, not a silent
mismatch at settlement.

### The other platforms are not more of the same — three integration classes (Thailand, 2026)

Scoping error to prevent: a prospect says "we sell on Shopee, Lazada, TikTok, LINE and Facebook"
and the estimate multiplies one connector by five. The five fall into **three classes with
different reconciliation designs**, and the third has no settlement report at all.

| Class | Platforms | Order capture | Money flow | Reconciliation |
|---|---|---|---|---|
| **Full marketplace** | Shopee · Lazada · **TikTok Shop** | Order API | platform collects, deducts, pays on cycle | **three-way match** (above) |
| **Platform storefront, seller collects** | **LINE SHOPPING** (public Open API since 2023: orders, products, stock) | Order API | payment via the seller's own gateway or transfer — no escrow cycle | **two-way**: order ↔ payment received |
| **Chat commerce** | **Facebook / Instagram** (no native checkout in Thailand) · LINE OA chat | conversation → order entered by admin or an order-capture tool; often routed through an OMS aggregator | seller collects: transfer slip, gateway link, or cash on delivery | **two-way**, and the harder half is order *capture*: chat orders that never enter a system are unreconcilable by definition |

Design consequences worth pricing separately:
- **TikTok Shop reconciles like Shopee** — its Finance API exposes statements and per-order
  transactions, settles after delivery plus the return window, and adds a deduction type the other
  two do not have at the same scale: **creator/affiliate commission**, which must land in trade
  spend (file 10) attributed to the campaign, not lumped into platform fees.
- **LINE looks like a marketplace but settles like a website** — use the order API, skip the
  escrow design, and match receipts against the seller's own payment gateway.
- **Chat commerce needs the manual-verify sub-model** (the fourth debtor pattern in this file):
  the consumer is the debtor, an admin confirms payment before release, and the integration
  question is which tool captures the chat order — because a brand with real chat volume runs an
  OMS aggregator in front of the ERP, which then becomes one integration, not three.
- A prospect on all five platforms therefore needs **two connector designs plus one capture
  decision**, not five connectors — say so in the estimate and the architecture page (file 16).

### The capture decision has three answers — and one may already be made (Thailand, 2026)

Where do marketplace orders enter the estate before the ERP? Three options, priced differently:

| Option | What it is | When it wins | The fit-gap test |
|---|---|---|---|
| **Direct connectors** | ERP (or middleware) integrates each platform's API | few platforms · brand wants full line-level data ownership | full control, most build |
| **Independent OMS aggregator** | a commercial OMS (in the Thai market, ZORT is the reference case — public API v4, connects Shopee, Lazada, TikTok Shop, LINE SHOPPING and web stores) holds the platform connections; the ERP integrates **once** to the OMS | many platforms · chat commerce in the mix · the OMS's stock-sync prevents overselling across channels | **does the OMS pass through the funder-split promotion fields and the settlement identifiers?** If it flattens them, invariant 9 and the three-way match break behind a clean-looking single feed |
| **Fulfilment platform** | a fulfilment provider's own OMS/WMS, bundled with the warehouse service (Sokochan-class: the OMS is free when goods sit in their warehouse) | the brand **already outsources fulfilment** — the platform connections and the stock truth may already live there | same pass-through test, plus an exit question: the order history lives in the provider's system, so switching 3PL means migrating the sales-channel hub too |

If the prospect already uses an outsourced-fulfilment provider, ask **which system currently talks
to the marketplaces** before designing anything — the capture decision may already be made, and the
ERP's job reduces to one inbound feed plus the settlement match. The dependency cuts both ways:
cheapest integration, deepest lock-in.

## 3. Functions the system must provide

| # | Function | Why it is needed | Typically standard or custom |
|---|---|---|---|
| 1 | **API gateway** absorbing each marketplace's dialect | the ERP integrates once instead of once per platform | custom build or bought middleware |
| 2 | Order creation with **reservation at the moment of order** | prevents another channel taking the same unit | standard |
| 3 | **Status-differentiated order creation** — pending for prepaid, approved for cash on delivery and marketplace | the release gate differs by sub-model | configuration |
| 4 | **Payment-verified release gate** for prepaid orders | goods must not leave before money is confirmed | standard approval |
| 5 | **Tax-invoice-on-request branch** capturing customer tax details conditionally | consumers request selectively; capturing always is wasteful and capturing never is non-compliant | configuration plus storefront design |
| 6 | **Delivery-confirmation-driven invoicing** for marketplace | the platform's confirmation is the billing trigger, not the despatch | integration plus automation |
| 7 | **Courier clearing account** per carrier for cash on delivery | the courier is the debtor in transit | standard account design, deliberate |
| 8 | Clearing a cash-on-delivery shipment that was **returned rather than collected**, with no cash receipt | happens routinely in fashion and consumer goods | often missed; needs explicit design |
| 9 | **Settlement record per cycle per platform**, holding the platform's own gross, deductions and net | the counterparty's claim, held before matching, is what makes reconciliation possible | custom |
| 10 | **Deductions posted by type** — commission, payment fee, shipping subsidy, platform-funded promotion, penalty | each is a different cost with a different owner and negotiation | standard accounts, custom mapping |
| 11 | **Brand-funded separated from platform-funded** discount | a platform-funded discount is not a brand cost; netting them understates online margin | integration design — see function 14 |
| 12 | **Many-to-one cash application** — one receipt clearing many invoices net of many deductions | the settlement covers many orders | standard in mature products, verify |
| 13 | **Aged variance report with an owner**, plus a tolerance and write-off route | small residuals occur every cycle; unaged ones accumulate forever | custom reporting |
| 14 | **Promotion write-back** — realised price, discount amount and type, campaign code, funder, on the sales line | the platform decides the discount; the ERP must record it or campaign margin cannot be analysed | integration design |
| 15 | **Platform order reference carried on every document** — order, fulfilment, invoice, cash application | without a shared key, nothing above works | configuration |
| 16 | **Availability logic that prevents overselling** across channels | one stock pool serving several channels is where this channel breaks | see file **11** |
| 17 | Returns at consumer-return rates, back into a **returns location** with a disposition decision | online return volume is materially higher than wholesale | standard, capacity-dependent |

Functions 1, 8, 9, 11 and 13 are where online scope is normally underestimated.

## 4. Integration touchpoints

| Touchpoint | Direction | Mode | What it carries |
|---|---|---|---|
| Order creation and reservation | storefront / gateway / CRM → ERP | synchronous | order with **price detail and discount breakdown**, not just a net amount |
| Payment confirmation | payment gateway webhook → ERP | asynchronous | payment status against the order |
| Release to warehouse | ERP → warehouse | asynchronous | fulfilment instruction |
| Fulfilment confirmation | warehouse → ERP | asynchronous | picked, packed, shipped |
| Delivery confirmation | marketplace → gateway → ERP | asynchronous | the billing trigger for marketplace orders |
| Settlement report | platform → ERP | batch, per cycle | per-order gross, deductions by type, net payable |
| Stock availability | ERP → storefront and gateway | scheduled or event-driven | what may be sold |
| Product and price master | ERP → storefront and gateway | batch | item, description, base price |
| Return and refund | platform / storefront → ERP | asynchronous | return authorisation, receipt, credit note |

## 5. Challenges, gaps and improvement areas

| What commonly goes wrong | What the reference implementation did | What a better design looks like |
|---|---|---|
| **Online treated as one channel** | designed four sub-models separately | classify by debtor and billing trigger before estimating |
| **Settlement reconciliation deferred to "a report later"** | the gateway carried the order reference through every document, which made reconciliation possible | design the three-way match as a solution: settlement record, deductions by type, many-to-one application, aged variance with an owner |
| **Platform-funded discounts booked as brand cost** | — | separate the funder on the transaction line; otherwise online margin is understated and channel investment decisions are distorted |
| **Overselling when one pool serves many channels** | separate locations and reservation at order creation | decide explicitly between a live single pool and channel allocation — file **11** |
| **Cash on delivery modelled as a consumer receivable** | courier route designed | clearing account per carrier, and a route to clear a returned shipment with no cash receipt |
| **Return rates sized from wholesale experience** | returns designed with a returns location | ask for the client's own return rate by channel. **No defensible published figure exists for apparel e-commerce returns** — do not quote one |
| **One integration per marketplace** | the API gateway | the gateway pays for itself from the second platform onward; below two, a direct integration or bought middleware is cheaper |
| **Platform changes its report format silently** | — | build the settlement import to **fail loudly** rather than mis-map a column quietly |
| **Customer service left out of scope** | a separate training track was needed post-go-live for the impact of online sales on case handling | include the service desk's view of order status and returns in scope from the start |

## 6. Discovery questions

1. Which online routes do you sell through today — own site, which marketplaces, chat, and roughly what mix? ⚑
2. For each — **who actually pays you: the shopper, the courier, or the platform?** ⚑
3. How do you know today that a platform paid you for everything you shipped, and that its deductions were correct? ⚑ *(the answer is usually a spreadsheet and a person — that person will sponsor this work)*
4. Do your platform reports separate commission, payment fees, shipping subsidy and campaign funding, or arrive as one net figure?
5. When the platform funds a promotion, can you tell that apart from one you funded? ⚑
6. What proportion of online orders come back, and where does that stock go?
7. What stops the same unit being sold twice across two channels today?
8. Who decides the price and the promotion for each online route — and does the ERP see the breakdown or only the net? ⚑
9. For cash on delivery: how do you clear a shipment the customer refused?
10. Does your customer service team see order and return status, and where do they see it?

## Related files

- **00** channel map and the classification method
- **05** owned store — the other consumer-facing channel
- **10** trade spend and Net GP — the same deduction discipline, applied to retailers
- **11** inventory and costing — overselling, allocation, returns disposition
- **16** the application estate, including where the gateway sits
- **17** Thailand compliance — platform reporting to the tax authority, withholding on platform fees
- **19** the full discovery bank
