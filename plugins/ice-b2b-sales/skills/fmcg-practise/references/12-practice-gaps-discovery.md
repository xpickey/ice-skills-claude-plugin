# 12 — Practice, gaps and discovery: what goes wrong and what to ask

> Load this when scoping, estimating, running discovery, writing the risk section of a proposal,
> or answering "what usually goes wrong with these projects".
> This is the file that turns the rest of the skill into a sales advantage.

## How to read this file

Each section states **the industry benchmark** (what good looks like), then **what the reference
implementation actually did**, then **the gap and the improvement path**. The benchmark positions
are drawn from published practice and standard accounting treatment; the reference observations are
factual records of one completed implementation.

**Two disciplines when using this in customer-facing work:**
- A recorded **gap** is a fact about that design, not a product limitation. Present it as an
  improvement opportunity, never as a shipped capability.
- Where a figure is not independently verifiable, argue qualitatively. **A mis-attributed statistic
  in a proposal is a bigger risk than no statistic.**

---

## 1. Consignment

**Benchmark.** Good practice separates two events that weak designs merge: **the VAT tax point** and
**the revenue recognition point**. Under standard revenue accounting, revenue on consigned goods is
recognised when control passes to the end customer — not on delivery to the consignee. A brand
running consignment should be able to state, per retailer relationship, which tax treatment applies,
and the system should issue the tax invoice on the corresponding trigger rather than on one
hard-coded event.

**Thailand-specific — treat as a discussion frame, not tax advice.** Thai VAT law provides for an
agency-for-sale arrangement under which the tax point on consigned goods can be deferred until the
agent sells to the end customer, subject to conditions on the contract — including that **both
principal and agent are VAT-registered**, that the contract is notified to the authority within a
short window, that the original is retained for several years, and that separate goods accounting
is kept. **Without a qualifying contract, the tax point falls at delivery**, meaning the brand funds
the VAT before the cash arrives and carries the working-capital cost of stock sitting on someone
else's shelf.

A pattern reported in the Thai market for businesses without a qualifying contract is to issue the
tax invoice on delivery and then credit-note monthly against the retailer's actual sales report and
re-invoice. Describe that as observed market practice, not as a recommended method.

> **Always confirm the tax position with the client's tax adviser before stating it in a
> customer-facing document.** The value you add in discovery is *raising the question early*, not
> answering it for them.

**What the reference implementation did.** Ran **both** models in parallel — "true" consignment with
the tax invoice on sale-out, and "pseudo" consignment with the tax invoice on delivery plus a shadow
book. That is the right answer for a brand with mixed retailer contracts, and it is expensive:
two designs, a custom synchronisation program, and a reconciliation obligation.

**Gaps and improvement areas.**
- **Reconciliation is the recurring failure point**, not the initial build. Sale-out feeds miss days;
  counter-to-counter transfers and counter returns go unrecorded; shrinkage accumulates. Design the
  count cadence, the feed-health check and the accepted variance-write-off route **before** go-live.
- **The month-end cut-off for late-arriving sale-out data is routinely undefined.** Define it in
  design, not at first close.
- **Grouped cycle invoices become undisputable** if line-level sale-out references are lost in the
  grouping. Carry the reference through.

---

## 2. Modern trade

**Benchmark.** Good practice treats **sell-out capture and deduction control as core capabilities,
not reports**. Sale-in is the revenue event in outright trade; sale-out drives replenishment,
promotion measurement and planning. Deductions need a control set that distinguishes an agreed trade
term from a disputed claim, with an ageing and a resolution owner.

**What the reference implementation did.** Built sale-out reconciliation against invoices with
variance reporting, and delivered a purpose-built modern-trade order-entry screen. Recorded EDI for
replenishment and sales as a **gap** — the counterparty supported EDI for the purchase order only —
and shipped file/template import instead.

**Gaps and improvement areas.**
- **EDI expectation management is the recurring commercial risk.** Per-retailer EDI capability in
  Thailand is not publicly documented in any authoritative source we could retrieve. **Ask the client,
  retailer by retailer, before fixing the estimate.** Assume purchase-order-only until proven
  otherwise.
- **Trade terms lived partly outside the ERP** because the ERP held only a base price and discounting
  happened in front-end systems. **That architecture is not the gap — the missing write-back is.**
  Defend the design (the front end owns the deal context) and make the requirement explicit: every
  channel writes its realised discount back onto the ERP sales line, with amount, type and funder.
  Without it there is no channel or campaign margin analysis in any system. Field set in file **02**.
  What remains after the write-back is narrower and legitimate: a periodic report comparing agreed
  terms against terms actually granted.
- **Deduction handling was not designed as a control set.** Without one, the receivable ageing becomes
  noise within two quarters. The improvement is a deduction register with reason codes, an owner and
  an ageing — modest to build, high in operational value.

---

## 3. Online and marketplace

**Benchmark.** Standard practice is **one gross revenue stream per marketplace with the platform's
fees recognised as expense**, where the brand is the principal in the transaction — and a settlement
reconciliation that works many-to-one from the platform's net remittance back to individual orders.
Whether revenue is gross or net turns on whether the brand or the platform controls the goods before
transfer; this is a judgement to make with the client's auditor.

**What the reference implementation did.** Built a **brand-owned API gateway** so the ERP integrates
once and each marketplace's dialect is absorbed by the gateway; mapped delivery confirmation to the
shipment to raise the invoice automatically; handled cash on delivery with the courier as debtor; and
carried an explicit tax-invoice-on-request branch in every consumer flow.

**Gaps and improvement areas.**
- **Settlement reconciliation must be designed as a solution, not added as a report.** It is a
  three-way match — ERP revenue against the platform's settlement report against the money that
  arrived — and it needs a settlement record per cycle, deductions posted by type rather than in one
  bucket, brand-funded separated from platform-funded, many-to-one cash application, and an aged
  variance report with an owner. Full design in file **05**. Where this is left as "we will build a
  report later", finance reconciles a spreadsheet against a bank statement every cycle indefinitely,
  and online margin is understated because platform-funded discounts are booked as brand cost.
- **Returns in fashion e-commerce run materially higher than in most categories.** Published all-retail
  and all-online return rates exist; an apparel-specific rate could not be verified from a primary
  source, so argue this qualitatively. Design consequences that do hold: the returned unit's condition
  must route it to resaleable, refurbishment or write-off, and the refund route must follow the
  original payment route.
- **The customer-service impact of going online is systematically under-scoped.** The reference
  implementation had to revise its service-case process because online created case types a wholesale
  business never had. Budget for the service process, not only the order process.
- **Overselling** needs an explicit decision — live single pool versus channel allocation — with a
  named owner and an agreed answer for what happens when an oversell occurs. At volume, one will.

---

## 4. Inventory and costing

**Benchmark.** Standard practice **fixes the valuation grain and the cost formula in solution design**,
and states plainly what per-location reporting will and will not show. For seasonal goods the control
set is: ageing bands measured from receipt or season start · movement classification recalculated on a
cadence · **markdown as a planned event monitored against plan**, not an emergency at season end ·
write-down to net realisable value when cost exceeds expected selling price less costs to sell, which
for aged fashion stock is recurring rather than exceptional.

**What the reference implementation did.** Moving average, with **the subsidiary-versus-location
valuation grain left as an open decision**, and the per-location report inaccuracy recorded openly in
the design. Built inventory ageing and fast/slow/dead-stock reporting as **customisations**. Built a
custom stock-value ceiling control per location.

**Gaps and improvement areas.**
- **The valuation-grain trap is the single highest-value costing point in pre-sales.** Goods received
  at one cost and transferred at that cost; a later receipt at a different cost moves the average; the
  receiving location now carries a value matching neither. This is not a rounding difference. Raise it
  in discovery — it costs a change request and a difficult conversation if it surfaces in user
  acceptance testing.
- **Ageing and dead-stock reporting get scoped as "reports we will add later"**, and are then the reason
  finance distrusts the system in year one. For seasonal apparel they belong in core scope.
- Useful measures to discuss — sell-through by collection, weeks of supply, stock turn, gross margin
  return on inventory investment, proportion of stock older than one season. Discuss the measures; do
  not quote benchmark ranges you cannot source.

---

## 5. Omni-channel inventory

**Benchmark.** Standard practice is **one available-to-promise number consumed by every channel**,
with allocation applied as policy on top rather than as separate stock pools. Reservation rules,
ship-from-store eligibility and third-party warehouse synchronisation all resolve against that single
number.

**What the reference implementation did.** Allocation by **location**, stock checked and reserved at
order creation, one fulfilment mechanism serving both sales orders and transfer orders, in-transit
locations on every inter-site move, and three separate counting mechanisms for three counting
populations.

**Gaps and improvement areas.**
- **Store requests could not be grouped into one fulfilment** — real warehouse overhead for a chain
  doing many small replenishments. Consolidation is a legitimate phase-two improvement.
- **Routine store replenishment sat in a manual approval queue** even where Supply Chain review added
  nothing. A rules-based auto-release for routine replenishment is a throughput gain worth proposing.
- **Stock relief depends on the warehouse's confirmation returning.** A silent integration failure
  stalls both stock and cost of sales. A monitored confirmation backlog is a cheap, high-value control.

---

## 6. Transformation and make-to-order

**Benchmark.** Where goods are subcontracted for conversion, good practice computes the finished cost
from a bill of materials plus the subcontract service, with variance visible between expected and
actual.

**What the reference implementation did.** Set the transformed cost through **two manual inventory
adjustments** — issuing material and goods out of the outside location, and receiving finished goods
back at a cost Cost Accounting determines — with a **verify-cost report** as the compensating control.

**Gaps and improvement areas.**
- **Transformed-goods margin is only as good as the cost accountant's discipline and timing.** There is
  no automatic variance, so drift is invisible until someone looks.
- **The process does not scale linearly.** Twice the jobs is roughly twice the manual cost work, and
  month-end close waits on it.
- **The improvement path:** move routine cases onto a work order with a bill of materials and a
  subcontract operation so cost rolls automatically, keeping manual adjustment for exceptions. This is
  a credible phase-two story and a real differentiator — provided it is offered as an improvement, not
  implied as present.
- **Automatic purchase-requisition creation from a sales order** was a recorded gap requiring a custom
  interface. Prospects routinely assume this link is standard.

---

## 7. Procurement, payables and budget

**Benchmark.** Best practice for over-budget behaviour is not "block everything" — it is **warn at
requisition, block at purchase order, allow at invoice with a recorded override**. Budget reporting
needs three states: **commitment, obligation, actual**.

**What the reference implementation did.** Checked budget at requisition, purchase order, receipt,
invoice, credit note and journal — committing the budget when the buyer commits rather than when the
invoice lands. Disabled direct purchase-order entry so requisition approval is binding. Split goods
receipt into three flows including converted goods. Built a claim and quality-control quarantine
topology.

**Gaps and improvement areas.**
- **Three-state budget reporting (commitment / obligation / actual) was a gap.** It is the
  most-requested budget report in any product-buying business — assume it in scope.
- **Multi-year carry-forward was a gap.** Store fit-outs, campaigns and product development straddle
  year-end; this touches the fiscal calendar and the project dimension, not only the report.
- **Over-budget behaviour was never resolved** — the documents state an error is shown but not whether
  it is a hard stop or overridable, and **budget transfer between units or projects does not exist at
  all**. Ask all three directly.
- **Invoice matching tolerance was undefined**, with no exception route for partial or over-receipt.
  In a business that routinely receives short, this surfaces first in user acceptance testing.
- **The requisition-to-order price ceiling was pending**, which makes requisition approval advisory
  rather than binding.
- **Treasury was the thinnest area** — bank reconciliation, cheque clearing, the cheque register and
  withholding-tax payment splitting all at "pending solution". In Thailand these are month-end
  blockers. Scope treasury as its own workstream.
- **Process documentation arrived without journal postings.** Treat a process flow with no journal
  entries as an incomplete blueprint and price the accounting mapping as its own workshop.

---

## 8. What actually delays these programmes

**On published evidence — and why this skill gives you no statistics to quote.** Independent,
retrievable figures on enterprise-software project outcomes are far scarcer than the volume of
writing about them suggests. Duration, failure-rate and cause-breakdown figures circulate widely in
secondary listings, almost always without a retrievable primary source behind them.

**So make every risk argument in this section qualitatively.** The mechanisms below are well
evidenced by the reference implementation and by ordinary practice; the percentages that usually
accompany them are not. A mis-attributed statistic in a proposal is a larger risk than no statistic —
it is the one thing a sceptical chief financial officer will check, and the only thing they need to
find wrong to discount everything else you said.

If a client asks for benchmark numbers, the honest and stronger answer is: *"I can tell you what
goes wrong and in what order — and I would rather show you your own numbers than someone else's."*
Then use the discovery set at the end of this file.

### The eight under-estimated areas, in the order they bite

| # | Area | Why it is under-estimated |
|---|---|---|
| 1 | **Channel count as a multiplier** | scope is sized by module, but each channel adds its own order intake, price basis, debtor, promotion mechanic, return path and reconciliation. Ten channels is not one process ten times — it is ten variants, each with a different owner |
| 2 | **Integration count and error handling** | the happy path is quick; the error contract, retry behaviour, duplicate protection and reconciliation report are where the effort is |
| 3 | **Item master and variant explosion** | style × colour × size. Barcode, marketplace listing, retailer article number and internal code rarely agree, and cross-reference maintenance is an ongoing operating cost, not a migration task |
| 4 | **Data migration, especially open balances** | item and customer master is the visible part; open orders, consignment stock at retailers, in-transit stock, open deductions and returns in flight decide whether go-live is calm |
| 5 | **Promotion mechanics** | priced as configuration, delivered as development. Multi-buy, bundle, staff and member pricing, channel-specific and platform-funded promotions rarely map to one native mechanism |
| 6 | **Tax and document rules** | tax invoice on request, branch designation on the document, consignment tax point, electronic tax submission. Each is small; collectively a workstream, and legally non-negotiable |
| 7 | **Reconciliation reporting** | marketplace settlement, consignment counts, store daily takings, third-party warehouse stock. These decide whether finance trusts the system, and they are specified last |
| 8 | **Cutover across channels that cannot stop** | stores trade, marketplaces trade, retailers keep sending orders. A multi-channel cutover has no quiet weekend |

### Migration and cutover — the two under-specified areas, in more detail

These are named in the table above and deserve more than a row, because they are where a
multi-channel programme is most often surprised.

**Migration: master data is the visible part, open balances are the risky part.**

| Layer | What it is | Why it bites |
|---|---|---|
| **Master** | customers, vendors, items, prices, locations, bills of materials | visible, planned, and usually done adequately. Item variant handling (style × colour × size) plus external cross-references — barcode, marketplace listing, retailer article number — is bigger than it looks |
| **Balances** | stock on hand by location and bin, general ledger opening balances, receivables and payables ageing | standard, and rarely the problem |
| **Open positions — the real risk** | open sales orders and reservations · **consignment stock sitting at retailers** · stock in transit between sites · goods with subcontractors · open purchase orders and goods received not invoiced · **open retailer deductions and disputes** · returns in flight · unapplied receipts | each is a partly-completed process, so it must arrive in the new system *mid-flight* and then complete correctly. This is what decides whether go-live is calm |

The practical rule: **for every process in scope, ask what a half-finished instance of it looks like,
and how it will arrive.** A consignment position that migrates as plain stock, or an open deduction
that migrates as a clean receivable, produces a reconciliation problem in the first month that
nobody can unwind.

**Cutover: a multi-channel business has no quiet weekend.**

Shops trade, marketplaces trade, and retailers keep sending purchase orders. Points to settle in the
plan rather than in the week itself:

- **Which channels can be paused and for how long** — usually the wholesale order desk can, the
  shops and marketplaces cannot.
- **The order-cutoff rule per channel** — the last order taken in the old system, and where the first
  new one is taken. Marketplace orders arrive automatically and will not respect a cutoff, so the
  gateway or the import needs a switch.
- **Stock-count timing against trading hours** — counting a shop that is open is counting a moving
  target.
- **Consignment positions**, which need a count at the counterparty's site inside the cutover window,
  coordinated with people who do not work for the client.
- **Whether channels go live together or in waves.** Waves reduce risk per event but require the two
  systems to share a stock position for the duration — which is its own integration and its own
  reconciliation. Decide deliberately; do not let it emerge.

**A defensible phasing shape** where a wave approach is chosen: core finance and inventory with the
largest single channel first, because that proves the backbone · then the remaining wholesale
channels, which reuse the same spine · then the consumer channels (stores, online), which carry the
most volume and the least tolerance for disruption · then the reporting and analytics layer, once
there is real data to report on. State it as a shape to be validated, not a template.

### The pattern behind the pattern

Most delay traces to one root: **the operating model was decided during the build rather than before
it.** Who owns price per channel · who is accountable for consignment shrinkage · whether a store is
credited for an order shipped from the warehouse · which system holds the authoritative on-hand.
These are business decisions. When they arrive as system questions during build, each costs a client
decision cycle — which is exactly what a plan cannot absorb.

**Discovery that surfaces these as decisions with owners and dates is the most effective schedule
protection available, and it is the part of pre-sales a competitor pitching on licence price cannot
copy.**

---

## The discovery question set

### Opening three — ask of every channel
1. When must the tax invoice be issued?
2. Who actually owes you the money?
3. After delivery, whose balance sheet carries the stock?

### The operating-model test
> For each channel, can the client name — **today, without a workshop** — the owner of price, the
> debtor, the return path, and the authoritative stock position?

Every "we'd have to check" is a decision that will otherwise land in the build phase. Log it with an
owner and a date.

### By area

**Channels** — Which customer groups do you sell to? Which sell the same product? What stops two
channels selling the same unit?

**Consignment** — When goods sit on a retailer's shelf, when must you issue the tax invoice? How does
sale-out reach you? How often do you count, and who does it? When a shopper returns at the counter,
what happens to your stock record? Do you also hold anyone else's goods?

**Modern trade** — After delivery, who owns the stock? How does the purchase order reach you, per
retailer? Which trade terms are settled by credit note and which by deduction? When a retailer
short-pays, how do you decide today whether it is valid?

**Online** — Which platforms today, which next year? For each, who pays you? What sits between the
marketplaces and your back office? How do you reconcile a platform's remittance? What proportion of
customers ask for a tax invoice? When goods come back, how do you decide whether they can be sold
again?

**Stores** — How many, and are any inside a department store's system? How do stores request
replenishment, and who approves it? Who authorises a refund at the counter? How often do stores count?

**Inventory and costing** — Where can a unit be, and in each place do you own it and can you sell it?
Who runs your warehouse? Does anyone rely on stock value per site? How do you decide when to mark
down?

**Transformation** — What proportion of orders involve decoration or personalisation? Does a decorated
blank become a new product code? Who does the work? While goods are with a subcontractor, how do you
know what is there and what it is worth? How is the cost determined — calculated, or set by an
accountant?

**Procurement and budget** — Can a buyer raise a purchase order without an approved requisition? When
you receive short, what happens to the invoice match? At what point is budget consumed? If someone is
over budget, does the system stop them or warn them, and who can override? Does unspent budget carry
forward?

**Credit** — Who can release a customer over their credit limit, up to what value, and where is that
decision recorded?

---

## Open topics this skill does not yet cover

Recorded honestly so nothing here is presented as more complete than it is:

- Per-retailer electronic-data-interchange capability in Thailand — no authoritative public source
  was retrievable; ask the client.
- Apparel-specific return rates — widely quoted, not verifiable from a primary source.
- Thai electronic tax invoice interaction with consignment and marketplace sales — not yet researched.
- Deduction validity and dispute-resolution benchmark ranges — published without external citation;
  not usable as industry standard.

## Related files

- **01-08** the channel and operations detail behind each gap above
- **09-11** the back-office modules and the architecture
- `cheatsheet.md` for the decision rules in meeting-ready form
