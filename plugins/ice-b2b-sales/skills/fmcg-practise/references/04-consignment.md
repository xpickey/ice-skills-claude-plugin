# 04 — Consignment (ฝากขาย): the two models and what they cost you

> Load this when consignment, ฝากขาย, sale-out recognition, or department-store counters
> are in scope. This is the highest-risk channel to get wrong and the one most often
> under-scoped in a proposal.

## The core insight

**"Consignment" is never one requirement.** In the reference implementation two consignment
models run side by side, and what separates them is not the commercial deal — it is **when the
tax invoice must be issued**. Everything else follows from that one answer.

| | **True consignment** (ฝากขายแท้) | **Pseudo consignment** (ฝากขายเทียม) |
|---|---|---|
| Tax invoice issued | **when the goods are sold** to the end consumer | **when the goods are delivered** to the retailer |
| Document that moves the stock out | Transfer Request (ใบขอโอน) | **Sales Order** |
| Stock relieved from the main book | no — it moves to a consignment location | **yes, at fulfilment** |
| Where the consigned stock sits | consignment location in the same book | a **second book / separate subsidiary** holding the same quantity |
| Revenue recognised | on sale-out | at delivery |
| Receivable created | on periodic grouped invoice | at delivery |
| What the sale-out feed does | creates the sales order and the invoice | only relieves stock from the shadow book |

Ask the discovery question in exactly this form: **"When your goods sit on a retailer's shelf,
at what moment do you have to issue the tax invoice — when you deliver, or when the shopper
buys?"** The answer determines the entire design. In Thailand this is a tax-position question,
not a preference; confirm it with the customer's tax adviser rather than deciding it in a
workshop.

---

## Model 1 — True consignment: invoice on sale-out

### Step A — moving the goods out (no revenue, no invoice)

1. The buyer or merchandising team raises a **Transfer Request** to the consignment location and approves it.
2. An approver with the appropriate authority signs off.
3. The system notifies the warehouse automatically to prepare the goods.
4. The goods are delivered — routed through the third-party warehouse integration if a 3PL runs the physical operation.
5. The merchandiser at the retailer inspects the delivery and **scans receipt on the in-house or store system**.
6. On that confirmation the system **transfers stock into the consignment location**. Ownership has not changed; only the location has.

### Step B — recording the sale (revenue happens here)

1. The merchandiser records sales on the in-house/store system as they happen.
2. Sale-out data flows to the ERP and **one sales order is created per day, in batch** — not one per transaction.
3. Order fulfilment is created automatically against that daily sales order.
4. Accounting raises the **AR invoice on a billing cycle, grouped** across the period rather than per sales order.
5. Billing and collection follow the retailer's terms.

Stock availability is checked back to the front-line system through a stock-check integration so
the merchandiser sees what is really on the counter.

### What this model demands
- A **daily batch sale-out feed**, with a defined cut-off and a defined failure path.
- **Grouped/cycle invoicing** — the AR document does not map one-to-one to a sales order.
- **Periodic physical counts** at every consignment location, because the brand still owns the stock it cannot see.

---

## Model 2 — Pseudo consignment: invoice on delivery

### Step A — moving the goods out (revenue happens here)

1. The buyer raises the movement **as a Sales Order**, not a transfer request, and approves it.
2. Order fulfilment is created and the warehouse ships.
3. **Stock is relieved at fulfilment** — cost of goods sold posts now.
4. A program **automatically books a goods receipt into a consignment location in a second book**, for exactly the quantity relieved. This shadow position is what lets the brand still see what is physically on the retailer's shelf even though the accounts have already sold it.
5. Accounting issues the invoice and tax invoice immediately, on the statutory preprinted form.

### Step B — recording the sale (no revenue; stock housekeeping only)

1. The merchandiser records the sale on the in-house system.
2. The ERP **relieves stock from the consignment location in the shadow book**, carrying a reference back to the consignment invoice.
3. Billing and customer payment are applied against the invoice that was already issued at delivery.

### What this model demands
- A **dual-book inventory design**: the real book relieved at delivery, a shadow book holding the consigned position.
- A **custom program** to keep the two books in step — this is not standard behaviour in any ERP.
- A **reference field linking the shadow movement back to the original consignment invoice**, otherwise reconciliation is impossible.
- Discipline about what the shadow book is *not*: it must never feed financial reporting.

---

## Consignment-in — the mirror case

The same reference model also handles **goods the brand receives on consignment from someone
else** (รับฝากขาย), sold through its own channels. The inventory topology therefore carries two
distinct consignment location groups:

- **คลังฝากขาย** — consignment-out: owned by the brand, sitting at a partner
- **คลังรับฝากขาย** — consignment-in: sitting at the brand, owned by a partner

Any prospect that both places goods with retailers and carries other brands needs both, and they
must never be netted together in a stock-value report.

## Event and pop-up stock — the same pattern, shorter fuse

The reference implementation applies the **identical true/pseudo split to retail event and
pop-up stock**. That confirms the pattern generalises: whenever goods move to a site the brand
does not control, with the sale happening later, the tax-point question returns. Events add
urgency because the cycle is days rather than months and the count happens under time pressure
at tear-down.

---

## Where consignment goes wrong

| Failure | Why it happens | What to design for |
|---|---|---|
| Stock on the shelf does not match the system | sale-out feed missed a day; returns and transfers between counters unrecorded; shrinkage | scheduled counts per location, a visible feed-health check, and an accepted variance-write-off route |
| Revenue recognised in the wrong period | sale-out feed arrives after month-end cut-off | define the cut-off and the late-arrival treatment **before** go-live, not at first close |
| The shadow book drifts from the real book (pseudo model) | the sync program failed silently, or someone posted a manual adjustment in one book only | reconciliation report between the two books, run as part of period close |
| Invoicing disputes with the retailer | grouped cycle invoices cannot be traced back to individual sale-out lines | keep the sale-out reference on every line through to the invoice |
| Counter returns handled as sales reversals | the return never physically comes back to the brand's warehouse | treat counter returns as a movement within the consignment location, distinct from a goods return to the warehouse |

## Scoping signals — what makes consignment expensive

Raise the estimate when you see any of these:
- **Both models in scope** — two tax points means two designs, not one design with a flag.
- **A shadow book is required** — dual-book synchronisation is custom development plus a reconciliation report plus a support runbook.
- **Many consignment locations** — count effort and feed-failure surface scale with location count, not with revenue.
- **The retailer's system is the source of sale-out** — you inherit their file format, their timing and their outages.
- **Consignment-in as well as consignment-out** — separate location groups, separate valuation treatment, separate reporting.

## Discovery questions

1. When goods sit on a retailer's shelf, when must you issue the tax invoice — on delivery or on sale?
2. How does sale-out data reach you today — a file, a portal, a merchandiser app, or a spreadsheet by email?
3. How often do you physically count consigned stock, and who does it?
4. When a shopper returns an item at the counter, what happens to your stock record?
5. Do you also hold anyone else's goods on consignment?
6. Do you invoice per delivery, or on a cycle? If a cycle, does the retailer expect line-level detail?

## Related files

- **01** the channel map and where consignment sits among the others
- **03** modern trade — the outright-sale sibling that is often confused with consignment
- **07** the consignment location groups inside the wider inventory topology
- **11** the integration touchpoints that carry sale-out and stock adjustment
- **12** consignment gaps versus common practice
