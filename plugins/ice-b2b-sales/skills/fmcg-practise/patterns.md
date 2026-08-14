# Patterns — reusable mechanisms from the reference implementation

> Each entry is a mechanism you can lift into a new design. `When to use` · `How` ·
> `Trade-offs`. For decision rules see `cheatsheet.md`; for definitions see `glossary.md`.

## Channel-coded customer master

**When to use** — the business has many customer groups whose commercial treatment differs but
whose process is broadly the same.
**How** — carry the sale channel as a segment on the customer master. Reporting, tax-point rules
and accounting dimensions derive from it. Write the process once and let the customer code drive
the variation.
**Trade-offs** — depends on disciplined customer coding; a miscoded customer reports and taxes
wrongly. Needs a governed customer-creation process to be safe.

## Dual-book consignment

**When to use** — the tax invoice must be issued on delivery, but the goods are physically still
at the retailer and must remain visible.
**How** — move the goods on a sales order; relieve stock and book revenue at fulfilment; a program
simultaneously books a receipt of the same quantity into a consignment location in a **second
book**. The sale-out feed later relieves only the second book, carrying a reference back to the
consignment invoice.
**Trade-offs** — custom development in any ERP, plus a reconciliation report between the two books
in the period-close checklist, plus a support runbook. The shadow book must never feed financial
reporting. Do not quote this as configuration.

## Daily batch sale-out to one order

**When to use** — a consignment or merchandiser channel generating many small consumer
transactions that must land in the ERP as revenue.
**How** — the front-line system records transactions all day; a scheduled feed creates **one sales
order per location per day**; fulfilment and invoicing follow on a cycle, grouped.
**Trade-offs** — needs a defined cut-off and a defined late-arrival treatment before the first
month-end. Loses per-transaction traceability unless the sale-out reference is carried on each
line, which it should be.

## Grouped cycle invoicing

**When to use** — a counterparty expects one invoice covering a period rather than one per
delivery or per sale.
**How** — accumulate fulfilments over the cycle; raise a grouped AR invoice; keep the source
reference on every line.
**Trade-offs** — dispute resolution is only possible if the line-level references survive the
grouping. Without them the customer's queries cannot be answered.

## Invoice-only-from-shipped

**When to use** — always, in any channel where goods move.
**How** — make fulfilment status "shipped" a precondition for raising the AR invoice.
**Trade-offs** — blocks the legitimate case of billing before despatch (some project and deposit
arrangements), which therefore needs a deliberate exception route rather than an accidental one.

## Physical-event-drives-accounting-event

**When to use** — the warehouse is outside the building, or run by a third party.
**How** — the ERP issues the fulfilment instruction, but stock is relieved and cost of sales posted
only on the warehouse's **confirmation** coming back.
**Trade-offs** — the stock ledger is only as timely as the warehouse's confirmations; a silent
integration failure stalls both stock and cost. Needs a monitored confirmation backlog.

## One fulfilment mechanism for sales and transfers

**When to use** — the same warehouse serves customer despatch and internal replenishment.
**How** — generate the same warehouse instruction from either a sales order or a transfer order;
the warehouse does not need to know which.
**Trade-offs** — none material; designing them separately doubles integration for no benefit. The
one caveat is that priority rules must distinguish a customer despatch from a store replenishment.

## In-transit two-step transfer

**When to use** — any movement between sites that is not instantaneous.
**How** — on despatch, transfer into an in-transit location; on receipt, transfer from in-transit
to the destination.
**Trade-offs** — two transactions instead of one, in exchange for stock never being invisible or
double-counted, and a measurable delivery gap.

## Sale-channel-driven account mapping

**When to use** — front-line systems (point of sale, merchandiser apps, warehouse devices) post
transactions that must hit the right accounting dimensions.
**How** — the inbound message carries the sale channel; the ERP derives the account, department and
class from it. Operators never choose an account.
**Trade-offs** — the mapping table becomes critical master data with its own change control. Worth
it: it is the only way a fifteen-channel ledger stays analysable.

## Tax-invoice-on-request split posting

**When to use** — any consumer-facing channel in Thailand.
**How** — branch on whether the customer requested a tax invoice. Requested → capture tax details
and raise a **named invoice**; not requested → aggregate into **one summary customer** invoice.
Split receipts by payment type in both branches.
**Trade-offs** — two AR populations to reconcile, but the alternative is either an unusable
receivable ledger or a compliance failure.

## Brand-owned API gateway for marketplaces

**When to use** — two or more marketplaces, or an intention to add more.
**How** — the gateway speaks each platform's dialect; the ERP integrates once with the gateway.
Delivery confirmations flow back through the gateway and trigger the AR invoice automatically.
**Trade-offs** — an extra component to build, host and support, in exchange for making the second
and every subsequent marketplace cheap. Below two platforms the arithmetic favours a direct
integration or a bought platform.

## Synchronous only when a human waits

**When to use** — deciding the mode of every integration in the estate.
**How** — credit check, stock check, order creation and stock request are synchronous. Everything
else is asynchronous.
**Trade-offs** — asynchronous flows need status visibility so users are not left guessing; budget
for the status surface, not just the interface.

## Promotion write-back

**When to use** — always, in any estate where discounting is decided in a channel front end rather
than in the ERP. That is most consumer-goods estates, and the architecture is correct.
**How** — the front end decides the discount; the order interface writes the realised pricing back
onto the ERP sales line: gross price, discount amount and percentage, discount or promotion **type**,
promotion or campaign **code**, net price, and **who funded it** (brand, retailer or platform).
Sales analysis then works identically in every channel — gross sales less discount equals net sales,
with discount type and campaign as reportable dimensions.
**Trade-offs** — order interfaces must carry price detail rather than a final amount, which is more
to build and more to test. Promotion and campaign codes become shared reference data needing one
owner. Where a front end genuinely cannot send the breakdown, derive the amount from the base price —
but accept that derivation recovers the value and loses the type and the funder, which is the part
that matters. The alternative is revenue nobody can explain.

## Three-way platform settlement reconciliation

**When to use** — any marketplace channel, from the first platform onward.
**How** — match ERP revenue (invoices from confirmed deliveries) against the platform's settlement
report (per-order gross, each deduction, net payable) against the bank receipt. Hold a **settlement
record per cycle per platform** carrying the counterparty's own totals before matching. Post
deductions **by type** — commission, payment fee, shipping subsidy, platform-funded promotion,
penalty — never in one bucket. Separate **brand-funded from platform-funded**. Apply cash
**many-to-one**. Age the variances and give them an owner, with a defined tolerance and write-off
route for the residuals that occur every cycle.
**Trade-offs** — a real build, not a report. Justified because the alternative is a permanent manual
reconciliation and an understated online margin: booking platform-funded discounts as brand cost
makes the channel look less profitable than it is, which distorts channel investment decisions.
Match on the **order**, not the period, because returns and cancellations settle on a different cycle
from the original sale.

## Master data outward in batch, transactions inward in real time

**When to use** — an ERP feeding channel front ends.
**How** — product and price lists go out as scheduled files; orders and confirmations come in as
real-time calls.
**Trade-offs** — front ends can be up to one batch cycle stale on price. Acceptable for wholesale;
decide deliberately for consumer channels where a wrong price is visible to the shopper.

## One enumerated error contract

**When to use** — any estate above roughly ten interfaces.
**How** — every integration returns the same error classes — required field missing, wrong data
type, field width mismatch, value not defined in the ERP, stock not available — each with a code
and a defined resend path.
**Trade-offs** — slightly more work per interface at build; turns support into one runbook instead
of one per interface. Strongly worth proposing deliberately.

## Two return paths

**When to use** — always.
**How** — separate **credit note with goods return** (approval → return order to the warehouse →
physical receipt → credit memo → refund if due) from **credit note only** (price or allowance
correction, no goods movement).
**Trade-offs** — none; forcing allowances through a goods-receipt path creates phantom stock. The
work is in defining the approval authority for each path.

## Function-based location grouping

**When to use** — any business where stock sits in more than one kind of place.
**How** — generate the location list by asking, for every place a unit can be: **do I own it** and
**can I sell it this month**. Two different answers mean two groups. Separate bins within a
location by material status.
**Trade-offs** — a longer location list and a governed creation process, in exchange for being able
to answer "how much of my stock is actually sellable".

## Governed location and customer master creation

**When to use** — where master records carry accounting dimensions.
**How** — the requester obtains the accounting codes first, submits documentation, and a controlling
function opens the record. Numbering follows a defined structure.
**Trade-offs** — slower to open a new site or customer; the alternative is an unreportable ledger
within a year. Automate the paperwork, keep the control.

## Cost-verification report for manual cost setting

**When to use** — wherever a person, not the system, determines a cost — most commonly
subcontracted transformation.
**How** — a scheduled report listing transformation jobs whose cost adjustments have not been
completed, run as part of period close.
**Trade-offs** — a compensating control, not a fix. The real improvement is moving routine cases
onto a work order with a bill of materials so cost rolls automatically; keep manual adjustment for
exceptions.

## Three counting mechanisms for three populations

**When to use** — a business with a warehouse, stores and a merchandiser network.
**How** — provide a warehouse count tool, a finance-driven cycle count, and a point-of-sale count,
all posting to the same stock ledger.
**Trade-offs** — three things to build and support. Forcing one mechanism on all three populations
is a common cause of adoption failure, so this is usually the cheaper path.
