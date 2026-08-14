# 05 — Online: website, marketplace and chat commerce

> Load this when the brand's own storefront, marketplaces, social/chat selling, payment
> gateways, cash on delivery, or platform settlement are in scope.

## Online is not one channel — it is at least four

The reference implementation splits the online customer group into four sub-models, and each one
has a **different debtor, a different order status on creation, and a different billing trigger**.
Treating them as one "e-commerce" requirement is how online scope explodes mid-project.

| Sub-model | Order origin | Status on creation | Who owes the money | Invoice raised when |
|---|---|---|---|---|
| **Brand website — prepaid** (bank transfer, card, payment gateway) | storefront → API | **Pending** | the consumer | after Finance verifies receipt and releases; invoice after fulfilment |
| **Brand website — cash on delivery** | storefront → API | **Approved**, released immediately | **the courier** | at despatch, collected from the courier on remittance |
| **Marketplace** (Shopee, Lazada, TikTok and similar) | marketplace → **the brand's API gateway** → API | **Approved** | **the platform** | on delivery confirmation from the platform, matched to the shipment, invoice raised automatically |
| **Chat / social commerce** (messaging apps, social direct messages, telephone) | conversation → sales confirms stock and attaches payment evidence → CRM | **Pending** until Finance verifies | the consumer | as per the wholesale chain |

### Why the status difference matters

A **prepaid website order opens pending** because the money must be confirmed before goods leave
— the risk is releasing stock against a fake transfer slip. A **cash-on-delivery order opens
approved** because there is nothing to verify yet — the risk moves to the collection end, where
the courier now owes the money. Getting this backwards either strands paid orders in a queue or
ships unpaid goods.

## The API gateway pattern — the most reusable design decision here

In the reference implementation, marketplace orders do **not** integrate to the ERP directly.
The brand runs its **own API gateway** between the marketplaces and the ERP:

```
Shopee ─┐
Lazada ─┼─→  brand API gateway  ─→  ERP (one integration)
TikTok ─┘                          ← delivery confirmation, stock
```

The gateway also sends **delivery-confirmation events** back, which the ERP maps to the shipment
to trigger the AR invoice automatically.

**Why this matters commercially.** Without a gateway, every new marketplace is a new ERP
integration — new specification, new test cycle, new support surface, and a new thing that breaks
when the platform changes its API. With a gateway, the ERP integrates once and the gateway absorbs
each platform's dialect. For a brand that expects to add marketplaces over time, the gateway pays
for itself on the second platform.

**The alternative** — a commercial multi-channel order-management platform sitting in the same
position — is a genuine build-versus-buy decision. Buy reaches a first marketplace faster. Build
wins when the brand runs its own storefront *plus* several marketplaces *plus* a physical estate,
because channel-specific business rules then have somewhere sensible to live. Make this decision
in solution design; discovering it in build is expensive.

Whichever is chosen, the same object set has to be mapped across the boundary: **item master,
pricing and promotion, stock and inventory location, order, allocation, picking, fulfilment,
shipment matching, invoice, payment receipt.**

## Tax invoice on request — a standing decision node

Every online flow in the reference implementation carries an explicit decision: **does the customer
want a tax invoice (ขอใบกำกับภาษีหรือไม่)?** Only on the "yes" branch does the system capture the
customer's tax details and raise a named invoice.

This is a Thai-market reality that materially shapes the AR design. Consumers request tax invoices
selectively, so the receivable sub-ledger splits between named customers and an aggregate. Any
consumer-facing prospect in Thailand needs this branch, and it is routinely missed in scoping
because it looks like a form field rather than a design decision.

## Platform settlement reconciliation — design it, do not discover it

The marketplace model creates a receivable **from the platform**, not from the shopper. The platform
then remits **net** of its commission, transaction fees, subsidised shipping, platform-funded
campaign contributions, penalties and adjustments — on its own cycle, covering many orders at once.

**This is the single most-underestimated piece of online scope**, and it is a solution to be
designed, not a report to be added later. Without it, finance reconciles a spreadsheet against a
bank statement every cycle, forever.

### The three-way match

```
        ERP revenue                Platform settlement report              Bank
   (invoices raised from      (per-order gross, fees, subsidies,      (one net receipt
    confirmed deliveries)       adjustments, net payable)              per cycle)
          │                              │                                  │
          └──────── match by order ──────┴───── match by cycle total ───────┘
```

Three questions the design must answer:

1. **Does every order the platform is paying for exist in the ERP as revenue?** Missing orders mean
   revenue never recognised. Extra orders mean revenue recognised for something cancelled.
2. **Do the deductions the platform applied agree with what was expected?** Commission at the agreed
   rate, shipping subsidy on the right orders, penalties explained.
3. **Does the net figure the platform says it paid equal the money that arrived?** A gap here is
   either a timing difference or an error, and the two must be distinguishable.

### What to build

| Element | Design |
|---|---|
| **Platform order reference on every document** | carried from order → fulfilment → invoice → cash application. Without a shared key nothing below works |
| **A settlement record per cycle per platform** | holding the platform's own totals — gross, each deduction type, net — as the counterparty's claim, before matching |
| **Fee and deduction posting by type, not one bucket** | commission, payment fee, shipping subsidy, platform-funded promotion, penalty. Each is a different expense with a different owner and a different negotiation |
| **Brand-funded versus platform-funded separated** | a platform-funded discount is not a cost to the brand. Netting them together makes online margin look worse than it is and is the most common analytical error in this channel |
| **Many-to-one cash application** | one receipt clears many invoices net of many deductions — the receipt design must support this natively rather than by manual journal |
| **A variance report with an owner and an ageing** | unmatched orders, unexplained deductions and timing differences, each aged. What is not aged is not chased |
| **A defined tolerance and write-off route** | small residuals will exist every cycle. Decide who may clear them and up to what value, or they accumulate |

### Where it breaks

- **Returns and cancellations settle on a different cycle from the original sale**, so an order can
  appear as revenue in one period and as a deduction two periods later. Match on the order, not the
  period.
- **The platform changes its report format** without notice. Build the import to fail loudly rather
  than silently mis-map a column.
- **Promotion contributions arrive as a lump sum** rather than per order, and cannot be attributed
  back without the campaign code — which is the same write-back requirement described in file **02**.
- **Cross-border or multi-entity selling** puts the settlement in a different currency or a different
  legal entity from the revenue.

**Say this in discovery:** *"How do you know today that the platform paid you for everything you
shipped, and that its deductions were correct?"* The answer is almost always a spreadsheet and a
person, and that person is usually the one who will sponsor this part of the project.

## Returns — the online-specific pressure

Apparel and fashion carry materially higher return rates than most consumer categories, because
fit cannot be judged before purchase. The reference implementation's return design supports this
through two paths and an approval gate:

1. Sales or customer service records the return **referencing the original sales document**.
2. An approver signs off by authority level.
3. On approval a return record is created in the ERP automatically.
4. The return order is sent to the third-party warehouse.
5. The warehouse books the physical receipt; stock is received automatically.
6. Accounting creates the credit memo.
7. If money must go back, Finance processes the refund.

Plus the **credit-note-only** path for price corrections with no goods movement.

Two things to design deliberately for online returns:
- **The returned unit's condition drives where it lands** — resaleable stock, refurbishment, or
  write-off. Sending everything back to sellable stock overstates availability.
- **The refund route depends on the original payment route** — card reversal, transfer, platform
  wallet, or courier remittance adjustment. These are not interchangeable.

The reference implementation also captured an explicit downstream effect: **the customer service
process had to be revised because online selling changed the case mix.** Online generates case
volume — where is my order, wrong size, refund status — that a wholesale business never had.
Budget for the service process, not just the order process.

## Overselling — the cross-channel risk

The same physical unit is visible to the storefront, several marketplaces, the stores and the
wholesale team simultaneously. Two broad strategies exist:

- **Real-time availability sync** — one stock pool, every channel checks live. Highest accuracy,
  highest integration load, and exposed to latency at peak.
- **Channel allocation or buffer** — a quantity is set aside per channel, or a safety buffer is
  withheld from online. Simpler and resilient, at the cost of unsold reserved stock.

The reference implementation checks stock at order creation and reserves against the sales order,
with allocation possible **by location** — effectively a location-driven allocation model. Whichever
approach a prospect takes, make it an explicit decision with a named owner, and agree what happens
when an oversell does occur, because at some volume it will.

## Scoping signals

Raise the estimate when you see:
- More than two marketplaces, or an intention to add more
- Cash on delivery at meaningful volume — it adds a courier receivable and a remittance reconciliation
- A brand storefront **plus** marketplaces **plus** physical stores sharing one stock pool
- Chat/social selling that must produce proper tax documents
- Return rates typical of fashion, with refunds across multiple payment routes

## Discovery questions

1. Which online channels do you sell through today, and which do you plan to add in the next year?
2. For each: who pays you, and when do you consider the sale complete?
3. Do you have anything sitting between the marketplaces and your back office today?
4. How do you reconcile a platform's remittance against your orders?
5. What proportion of online customers ask for a tax invoice?
6. When goods come back, how do you decide whether they can be sold again?
7. What stops the same unit being sold twice across two channels today?

## Related files

- **01** the channel map
- **06** owned store — the other consumer-facing channel
- **07** the stock pool that all channels draw from
- **11** the gateway and order integration touchpoints
- **12** online gaps versus common practice
