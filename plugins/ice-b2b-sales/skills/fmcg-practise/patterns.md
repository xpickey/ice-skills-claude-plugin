# Patterns — reusable mechanisms from the reference implementations

> Each entry is a mechanism you can lift into a new design. `When to use` · `How` ·
> `Trade-offs`. For decision rules see `cheatsheet.md`; for definitions see `glossary.md`.
> Where a mechanism has a home file, it is named in bold — **02** modern trade · **03** consignment ·
> **04** van sales · **06** online · **10** trade spend · **11** inventory · **17** Thailand.

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

**When to use** — always, and especially where the warehouse is outside the building or run by a
third party.
**How** — the ERP issues the fulfilment instruction, but stock is relieved and cost of sales posted
only on the **confirmation** coming back. Confirmation takes three forms across the channels, and
they are the same pattern rather than three exceptions: the warehouse's fulfilment confirmation, the
**van settlement** at end of shift (**04**), and the **daily store posting** from point of sale.
**Trade-offs** — the stock ledger is only as timely as its confirmations; a silent integration
failure stalls both stock and cost. Needs a monitored confirmation backlog per confirming source,
not one queue for all of them.

## Van settlement as the stock-relief event

**When to use** — any channel where the selling person carries the stock: van sales, direct store
delivery, a merchandiser working from a held quantity (**04**).
**How** — stock loaded onto the vehicle becomes **van inventory** in its own right, keyed by vehicle,
item and lot. Sales during the route decrement that van inventory in real time on the mobile device,
but **the stock ledger is not relieved at the moment of sale** — it is relieved at the end-of-shift
settlement, where money and stock close together on one record set: opening float plus collections
by method less change given against counted cash, and loaded less sold plus returned against counted
on van, per item **and per lot**. Maker, checker and poster are three different people, and the
posted reconciliation is immutable — a correction is a new adjustment, never an edit.
**Trade-offs** — the ledger lags the physical sale by up to a shift, and clients ask why the van
cannot post same-day. That lag is the control, not a defect: it is the window in which duplicates
and fabricated cash are caught before entries become immutable, so present it as designed. The costs
are a van-inventory record most products do not have natively, a settlement screen, and the
segregation-of-duty rules to enforce it. Two things are commonly left out and both break the close —
**change given** as a subtraction in the cash equation, and lot-level rather than item-level stock
variance.

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

## Funder-split pass-through test for any middle layer

**When to use** — any time an OMS, marketplace aggregator or fulfilment-provider platform sits
between the sales channels and the ERP.
**How** — before committing to the layer, trace one promoted order end to end and confirm the ERP
still receives: discount amount and type, **who funded it**, the campaign code, and the platform's
settlement identifiers. Then trace one settled order and confirm the deduction lines survive.
**Trade-offs** — none if it passes. If it fails, the single clean feed silently destroys funder
attribution (invariant 9) and the three-way match — and the failure is invisible until finance
asks why online margin looks wrong.

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

## Rebate component decomposition

**When to use** — any trade agreement with a retailer that is more than a flat discount.
**How** — decompose the agreement into independently calculable components (fixed per unit, flat
percentage, tiered, growth, gross-profit guarantee), each carrying **five attributes**: **basis**
(sell-in or sell-through) · **scope on the product axis** (whole turnover, basket, item) · **scope on
the customer axis** (group, banner, store cluster — the axis most home-grown designs omit) ·
**mechanic** (retroactive, incremental **or prospective** — three values, not two) · and
**settlement** (on-invoice, off-invoice, net-bill, credit note or unilateral deduction — largely the
retailer's choice rather than the brand's). Accrue per component.
**Trade-offs** — more master data and more configuration than a single agreed amount. Justified
because a lump sum cannot be accrued correctly, cannot be matched to a deduction, and cannot tell
you which part of the deal earned its money. **Two of the three mechanic values** carry accounting consequences rather
than only arithmetic: **retroactive** creates a catch-up charge the moment a tier is crossed, which a
flat design gets materially wrong; **prospective** is a customer option that may be deferred rather
than accrued — a different accounting model, not a different rate. And modelling only the product
axis makes a group-level and a banner-level rebate on the same item impossible to apply without
double-counting — see the next pattern. Full treatment in file **10**, stage 2.

## Rebate hierarchy cascade without double-counting

**When to use** — any retailer relationship where agreements are struck at more than one level: a
group deal and a banner deal, a category deal and an item deal, or any combination of the two
(**10**).
**How** — model scope on **two axes**, customer hierarchy and product hierarchy, and let an agreement
attach at **any node** of either. Entitlement then cascades downward: a transaction inherits every
agreement whose node sits above it on both axes. The hard part is the arithmetic, not the
inheritance — a group-level rebate and a banner-level rebate on the same item must **both** apply and
**must not** double-count. Resolve it by evaluating each agreement against its own base and
composing the results under an explicit rule per component, rather than summing rates or applying
them in sequence to a shrinking base. Every accrual line must carry the node it was earned at, or a
deduction can never be matched back to the agreement that justified it.
**Trade-offs** — the hardest single piece of a trade-spend build, and custom in most products. A
single product-axis scope is cheaper and cannot express the situation at all; adding the customer
axis later means reworking the accrual history. The compensations are that the same node reference
makes deduction matching tractable and turns "which part of the deal earned its money" into a query
rather than an investigation.

## Versioned agreement as dispute evidence

**When to use** — any brand selling through organised retail, and in Thailand specifically wherever
retailer charges are in scope (**10**, **17**).
**How** — hold the trade agreement as a **versioned, effective-dated, amendment-tracked** record, not
as a current state that gets edited. The design test is a question: *given a deduction dated some
time in the past, can the system reconstruct the agreement exactly as it stood on that date?* If it
cannot, the claim cannot be defended, because the evidence used to dispute is the approved agreement
or promotion **as it stood on the deduction date** — not as it stands today. Carry the version
reference on every accrual, claim and dispute submission.
**Trade-offs** — versioning is more to build and more to govern than a maintained current record,
and users will ask why they cannot simply correct a rate. Two independent arguments carry it, and
together they are stronger than either alone. The first is commercial: dispute defence, where late
or unreconstructable evidence is the main reason claims are lost. The second is Thai compliance —
published competition guidance on retailer charges to suppliers **requires a prior written
agreement**, which turns the agreement record into a compliance artefact rather than good practice.
Position the system as the **evidence layer** and stop there: whether a specific charge is lawful is
the client's legal counsel's call, and file **17** is written to be handed over rather than answered.

## Two document types for a trade rebate

**When to use** — settling trade spend by credit document in Thailand (**10**, **17**).
**How** — treat the tax credit note and the **commercial credit note carrying no VAT** as two
distinct objects with **separate numbering series**, separate templates and separate tax
determination, and make the document type an outcome of the settlement's character rather than a
user's choice at the moment of issue. The relevant distinction is between a discount given at the
moment of sale and a benefit earned on a condition and settled later; Thai guidance points to the
first as a credit-note event and away from the second.
**Trade-offs** — two document families to build, number and reconcile, against a design that routes
everything through one. The one-document design is not simpler in the end: it produces VAT that does
not reconcile to the periodic return, and unpicking it after a year of postings is worse than
building both. Note the boundary — this pattern gives you the **structure**; whether a particular
rebate structure qualifies for a tax credit note is a question for the client's tax adviser, and the
question list is in file **17**.

## Deduction single front door

**When to use** — any brand selling through organised retail.
**How** — normalise every short-payment into one claim structure at the moment of arrival,
whatever the channel (remittance advice, retailer portal, bank statement), mapping each retailer's
own reason codes to an internal set through a maintained table. Then match with a confidence score
and a **per-retailer** tolerance, block double-dips, and support splitting one deducted amount
across many invoices or promotions.
**Trade-offs** — an intake and mapping layer to build and maintain. Without it the three arrival
channels remain three separate problems and nobody can state total deductions for a period. The
match rate becomes the operational metric: unmatched is leakage.

## Dispute window registry

**When to use** — wherever retailers operate supplier portals with time-limited dispute windows.
**How** — register each retailer's portal with its window length, accepted dispute codes, required
document formats and escalation contact. Count down to expiry, warn ahead of it, and **gate
submission on evidence completeness**. Capture proof of delivery within a day of despatch rather
than when a dispute opens.
**Trade-offs** — master data that must be maintained as retailers change their rules. Cheap
relative to the loss it prevents: a missed window is unrecoverable, and late evidence is the main
reason disputes fail.

## Contribution-margin waterfall with separated fulfilment penalties

**When to use** — whenever the client asks which retailer or which promotion actually makes money.
**How** — report gross revenue → cost of sales → CM1 → trade deductions → CM2 → fulfilment cost →
CM3, sliced by retailer and programme, drillable to item. Show Net GP margin **and** trade-spend
ratio together. Keep delivery-performance penalties in fulfilment cost, shown as their own line —
not inside trade deductions. **That placement is a management-reporting judgement to settle with the
accounting-policy owner before build; their tax and accounting classification is a separate question
that research could not settle — see file 17.** Freeze and version the snapshot at period close.
**Trade-offs** — depends on a clean channel dimension and on accruals being right, so it cannot be
delivered first. Placing penalties in the trade bucket is the common shortcut and it distorts the
trade-spend ratio, hiding an operational problem inside a commercial number.
