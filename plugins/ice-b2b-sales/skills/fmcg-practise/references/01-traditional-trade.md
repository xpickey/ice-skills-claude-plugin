# 01 — Traditional Trade (ขายขาดผ่านร้านค้า)

> **Load this when:** the prospect sells outright to dealers, distributors, sub-distributors or
> independent shops · you hear "ตัวแทนจำหน่าย", "ร้านค้า", "ขายสด / เครดิต", "วงเงินเครดิต" or
> "เงินมัดจำ" · the invoice is raised when the goods ship, and the shop owns them from that moment.
> **Do not load this for:** organised retail on a trading agreement, where the money comes back short
> → **02** · goods the brand still owns after delivery → **03** · an organisation buying for its own
> use or for a project → **07** · a buyer outside the country → **08**.
> **Source basis:** the apparel reference implementation documents this channel end to end —
> order-to-cash, credit, deposit, and four sourcing models across two payment terms. Credit override,
> tiered discount and the return process are **documented absences** in that source, and are marked
> as such rather than filled in.

## 1. Use cases — what this channel actually is

The brand sells goods outright to someone whose business is reselling them. Ownership, risk and the
money all move at delivery. It is the simplest channel to account for and the hardest one to get paid
by, which is why almost all of its design is about credit rather than revenue. The recognisable
situations: provincial dealers each serving a cluster of small shops; a distributor buying in bulk
and reselling down a second tier; a single outlet ordering from a representative who visits. One
brand usually runs all three at once, on one design.

**The three defining facts, and they are the least ambiguous of any channel:** the **tax invoice is
issued on shipment** · the **debtor is the dealer** · **unsold stock belongs to the dealer** once
delivered. No consignment location, no shadow book, no sale-out feed. What replaces that difficulty
is credit exposure spread across many small counterparties.

### The finding that shapes the whole design

> **Channel differentiation belongs in customer coding and tax-point rules. Process differentiation
> belongs in payment terms and sourcing model.**

In the reference implementation the design documents for traditional trade and for project sales are,
at process level, **identical** — same requirement rows, same integration list, same step sequences,
only the flow numbering changed. Not sloppiness: one process per channel would instead have produced
a dozen near-identical designs to maintain. Worth saying when a customer insists each channel is
unique.

Channel identity is carried in a **customer-master segment** — in the reference, a six-segment
customer number: record type, geography, channel group, a category whose meaning depends on that
group (sales region for trade, tax-point model for consignment, marketplace for online), a separator
and a running number. It drives reporting and tax-point treatment; **it does not change the
transaction path.** Standard auto-numbering carries one prefix only, so this shape is a customisation.

### The three axes that actually change behaviour

| Axis | Variants | What changes in the system |
|---|---|---|
| **Payment term** | cash (ขายสด) · credit (เครดิต) | cash inserts a human release gate — payment evidence uploaded by sales, notification to finance, finance approval of goods release, and the order opening **pending** instead of approved. Credit relies on the automated credit and overdue check instead |
| **Sourcing model** | stocked collection product · made to order · transformation with a new item code · transformation with the same item code | stocked goods flow straight to fulfilment. Made to order raises a requisition and purchase order and receives into a supplier-linked location. Transformation ships own stock out to a subcontractor against a production request — file **12** |
| **Deposit** | present · absent (เงินมัดจำ) | with a deposit: a receipt posts to an undeposited-funds account, VAT is charged and a tax invoice issued **on the deposit**, and the final invoice is netted against it. Without: one invoice at fulfilment |

The four sourcing models and two payment terms are the cross-channel matrix defined in file **00**.

## 2. Process — the flow

### The spine — credit sale of stocked goods

```
front office: representative confirms the sale, quotation accepted
  → stock check · credit-limit check · overdue-invoice check   (all before the order can exist)
  → sales order created in the ERP + stock reserved (การจองสินค้า)   status = APPROVED
  → release to the warehouse
  → warehouse picks                                            status = PICKED
  → warehouse confirms packed and hands to the carrier         status = PACKED
  → STOCK RELIEVED, cost of sales posted
  → invoice / tax invoice raised — only from a fulfilment in shipped status
  → invoice file passed to the warehouse operator so the paperwork travels with the goods
  → delivery → billing note (ใบวางบิล) on term → receipt (ใบเสร็จรับเงิน) → cash applied
```

**Two control points to name in any design review.** Stock is relieved **on the warehouse's
confirmation**, not on the ERP's instruction — the physical event drives the accounting event. And
**the invoice may only be raised from a fulfilment in shipped status**, the single rule that stops
every wholesale channel from billing goods that never left.

### Where the variants diverge

Branches against the spine above; the mechanics behind each are the third column of the axes table.

```
[cash]      opens PENDING → payment evidence uploaded → accounting notified → accounting
              approves the goods release → APPROVED → rejoin the spine
[deposit]   accounting notified at order creation → deposit receipt to undeposited funds →
              confirmed against the bank, VAT charged, TAX INVOICE ISSUED ON THE DEPOSIT →
              final invoice netted against it (หักเงินมัดจำ)   ← a two-tax-document sale
[made to order]   SO raises a purchase requisition into the normal purchasing chain; goods
              received into a SUPPLIER-LINKED LOCATION and fulfilled from there
[transformation]  own stock transferred out to the subcontractor's location, production or
              purchase request raised for the decoration work  → file 12
```

On a credit order nothing stands between order entry and picking except the automated credit and
overdue check — which is why it has to be trustworthy. The requisition-to-payment side of made to
order is procurement's, not this file's. Both made-to-order paths carry two stated limitations in the
reference: the order line is a **dummy item** until the real item exists, and **production status is
updated by hand**, with no feed back from the maker — design intent with a known weakness.

### Returns and credit notes

Two paths, to be separated in the first design pass rather than the last. **Credit note with goods
return** — recorded against the original sales document, approved by authority level, sent to the
warehouse, physically received, stock booked back, credit memo raised, refund if money must go back.
**Credit note only** — a price or allowance correction with no goods movement. In the reference's
earliest channel documents the credit-note *process* was not designed at channel level at all: the
requirement was only to **see** credit-note data and print the statutory form. The full return flow
arrived later, as a separate process area.

## 3. Functions the system must provide

| # | Function | Why it is needed | Typically standard or custom |
|---|---|---|---|
| 1 | Customer creation from the front office with a **two-stage approval** — accounting, then an authorised approver — and registration documents attached to the request | a new dealer is a credit exposure, not a name; the papers are what the approver reviews | standard master data; approval chain and attachment usually custom |
| 2 | **Structured customer number** carrying record type, geography, channel group and category | channel reporting and tax-point treatment hang off this code | custom — standard auto-numbering carries one prefix |
| 3 | **Customer record split into a sales-editable zone and a finance-controlled zone** (credit limit, term, bill-to, grade) | ship-to and contact changes should not queue behind finance | configuration plus custom approval routing |
| 4 | **Credit-limit and overdue check at order creation**, with a credit-remaining view — customer, credit remaining, overdue yes or no — shown to whoever enters the order | prevents shipping into a blocked account, and lets the representative know before promising | standard check, plus integration to surface it in the front end |
| 5 | **Credit-hold release against a single order**, with reason code, authority tier and audit trail | see section 5 — the alternative is a permanently raised credit limit | usually custom; frequently missing entirely |
| 6 | Stock reservation at order creation | stops another channel taking the same units | standard |
| 7 | **Cash-sale release gate** — payment evidence uploaded, finance approves release, order moves from pending to approved | the only human gate on the cash path | standard approval plus custom evidence capture |
| 8 | **Deposit handling** — automatic receipt, VAT on the deposit, its own tax invoice, netting against the final invoice | a two-tax-document sale, commonly done by hand | standard receipt; VAT-on-deposit and netting usually custom |
| 9 | **Invoice only from a fulfilment in shipped status** | stops billing goods that never left | standard control, worth stating explicitly |
| 10 | Statutory Thai **preprinted forms** — invoice/tax invoice, receipt/tax invoice, billing note, credit note | four separate layouts in the reference, all custom | custom report development |
| 11 | Automatic transfer of the invoice file to the warehouse operator | the document must travel with the goods | custom interface |
| 12 | **Automatic requisition from the sales order** for made-to-order lines | otherwise someone rekeys every made-to-order line into purchasing | custom in most products |
| 13 | **Production status on the sales order**, manual or interfaced | the representative is asked "where is my order" every day | standard field; the feed behind it is the hard part |
| 14 | Returns in two forms — **with goods return** and **credit note only** | allowances must not be forced through a goods-receipt path | standard, needs deliberate design |
| 15 | **Discount and promotion write-back** onto the sales line | the front end decides the discount; without the write-back there is no margin analysis | integration design — see section 5 |

Rows 2, 5, 8, 10 and 12 are where the effort concentrates. The core chain — order, reservation, credit
check, fulfilment, stock relief, costing, invoicing — is broadly standard in a mainstream ERP.

## 4. Integration touchpoints

| Touchpoint | Direction | Mode | What it carries |
|---|---|---|---|
| Customer creation, and approval or amendment result back | front office ↔ ERP | asynchronous | customer, addresses, contacts, finance-controlled fields |
| Stock availability check | front office → ERP | synchronous | on-hand and available by location |
| Credit and overdue check | front office → ERP | **synchronous** — a human is waiting | credit remaining, overdue flag |
| Sales order creation and reservation | front office → ERP | **synchronous** | order header and lines, **with price detail and discount breakdown** |
| Order and production status back | ERP → front office | asynchronous | status tracking through to shipped |
| Product and price list master | ERP → front office | batch | item, group, unit of measure, base price |
| Picking instruction out, packed confirmation back | ERP ↔ warehouse operator | asynchronous | fulfilment instruction; packed confirmation and quantities |
| Invoice document to the warehouse operator | ERP → warehouse operator | file transfer | tax invoice travelling with the goods |
| Electronic tax document | ERP → tax service | batch | signed invoice and credit note — file **17** |

**Rule of thumb:** synchronous only where a human is waiting for the answer — stock, credit, order
and reservation. Everything else asynchronous, with a visible status so nobody is left guessing.

## 5. Challenges, gaps and improvement areas

| What commonly goes wrong | What the reference implementation did | What a better design looks like |
|---|---|---|
| **A separate process designed per channel** | recognised early that traditional trade and project sales are one process family | differentiate in customer coding and tax point; keep one order-to-cash design and vary payment term and sourcing model |
| **No credit-override path** | **not documented at all** — the only human release gate designed was the cash goods-release approval | design a hold release as a **transaction, not a master-data change** — pattern below |
| **Tiered, volume or trade discount** | **not present in the source design** — no discount matrix, ladder or approval threshold | if the prospect expects laddered pricing inside the ERP, that is a scope item, not an assumption |
| **Discount invisible in the ERP** | the ERP held a base price only; discounting lived in the channel front ends | keep that architecture — it is correct — but require the write-back below |
| **Returns designed late** | the earliest channel documents required only that credit-note data be *visible* and the statutory form print | put both return paths in the first design pass; they are where trade allowances and damaged goods land |
| **Made-to-order status by hand** | dummy item plus manual status update on the sales order, stated as a known limitation | ask whether the maker can feed status back before promising order visibility to the sales team |
| **Structured customer code underestimated** | recorded as a customisation, because standard auto-numbering carries one prefix | count the segments during discovery and price the numbering programme as a line item |

### The credit-hold release pattern to propose where none exists

Every wholesale business has exceptions — a strategic dealer at limit on the last day of the quarter,
a customer whose payment is confirmed but not cleared. With no designed override path, staff invent
one outside the system and the control stops meaning anything. **A credit-hold release should be a
recorded transaction, not a changed master record**, because the alternative always ends the same way:
someone raises the limit to let one order through, and nobody lowers it again.

| Element | What good looks like |
|---|---|
| **Mechanism** | a hold-release action against **the specific order**, leaving the customer's credit limit untouched |
| **Authority** | tiered by exposure value, with the tiers set by finance rather than by sales |
| **Reason** | a mandatory reason code from a maintained list — payment in transit, strategic account, order under negotiation — never free text |
| **Expiry** | the release applies to that order only and lapses when it ships |
| **Visibility** | a released-on-override report finance reviews on a cycle, showing who released what and why |
| **Master-data change** | a genuine limit increase stays a separate, finance-controlled amendment with its own approval — never the answer to one blocked order |

Proposing this costs nothing and lands well: the finance director has almost always seen the
alternative.

### The pricing write-back — the requirement that is not optional

The ERP holding a base price while each channel decides its own discount is a **sound design and
should be defended, not apologised for**: the front end is where the deal context lives, and forcing
all of it into the ERP produces a promotion engine nobody can maintain. **The front end owns the
decision; the ERP owns the record — a channel that cannot write back is a channel you cannot
analyse.** What must land on the ERP transaction line:

| Field | Why it is needed |
|---|---|
| **Gross or list price** | the baseline the discount is measured against |
| **Discount amount** and **discount percentage** | the value actually given away |
| **Discount or promotion type** | trade discount · campaign · member price · staff price · platform-funded · brand-funded — different economics, and they must not share one bucket |
| **Promotion or campaign code** | so a campaign can be evaluated across every channel that ran it |
| **Net price and net line value** | what was actually invoiced |
| **Who funded it** — brand, retailer or platform | a platform-funded discount is not a cost to the brand; netting the two together destroys the margin number |

Three consequences, better stated than discovered. Discount governance sits **outside** the ERP's
approval framework, so the authority matrix has to be built in each front end and will not look the
same in all of them. The **campaign code becomes reference data shared across systems and needs one
owner** — the same governance problem as the channel dimension in file **15**, and the same answer.
And agreed terms and billed amounts still live in two places: the write-back makes them *comparable*,
not *one record*, so a periodic report comparing agreement against grant is worth building. Where a
front end cannot send the breakdown, deriving discount from base price and net line value recovers
the amount but not the type or funder, which is the part that matters.

## 6. Discovery questions

1. Do you sell to dealers on credit, cash, or both — and who releases the goods when payment is not
   yet cleared? ⚑ *changes the estimate materially*
2. What happens today when a dealer is at their credit limit and wants to order — who says yes, and
   where is that decision recorded? ⚑
3. Who maintains credit limits and payment terms, and what approval does a change need?
4. Do you take deposits, and how is the tax invoice on the deposit handled and netted off the final
   invoice? ⚑
5. Of your dealer orders, what proportion is sold from stock, made to order, or decorated to order?
   ⚑ *this is the sourcing-model mix, and it drives the build*
6. Where are prices held, and where are discounts decided and approved? Does the ERP see the
   breakdown, or only the net amount? ⚑
7. Do you operate laddered or volume-based dealer pricing, and do you expect the ERP to enforce it?
8. How does your customer code work — what does each part mean, and which fields must sales be able
   to change without waiting for finance?
9. When goods come back from a dealer, what happens — and how often is it a price correction rather
   than a physical return? How many statutory preprinted formats must you produce?
10. How does a representative find out where an order is, while the goods are still being made?

## Related files

- **00** channel map, classification method, and the four-by-two sourcing and payment matrix
- **02** modern trade — the organised-retail sibling · **03** consignment — where the brand still owns
  the goods
- **07** project and corporate · **08** export — the same spine, different buyer and border
- **11** inventory, locations and costing · **12** transformation and decoration — the sourcing models
  that leave the warehouse tail
- **15** finance, ledger and assets — where the campaign code and channel dimension are governed
- **17** Thailand compliance — electronic tax documents. **The VAT treatment of deposits is not
  covered there** and is an open question for the client's adviser ·
  **19** the full discovery bank
