# 15 — Finance: ledger, dimensions and the retail estate register

> **Load this when:** the general ledger, chart of accounts, dimensions, channel profitability, period
> close, consolidation, or fixed assets for a retail estate are in scope · someone asks "what is our
> margin by channel" · the prospect trades between more than one legal entity · the asset register is
> full of shop fit-outs rather than factory machines.
> **Do not load this for:** forecasting and planning → file **13** · stock valuation and costing → file
> **11** · purchasing, payables and budget control → file **14** · Thai tax and electronic tax documents
> → file **17** · investment-promotion segregation of the ledger → file **18**.
> **Source basis:** the apparel reference implementation's ledger and fixed-asset design, read together
> with its issue and gap register. Where the design left something unresolved, this file says so — an
> honest gap is more useful in a discovery conversation than an invented remedy.

## 1. What the ledger is actually being asked to answer

A brand selling through wholesale, modern trade, its own shops, marketplaces and export **does not have
a revenue number — it has five, with structurally different cost to serve.** The ledger has to answer
*which channel earned this, and what did it cost to earn it*, without anyone rekeying a spreadsheet.

That is a harder question than it sounds, because the cost to serve is spread across places the ledger
does not naturally see: the retailer's deductions (file **10**), the platform's commission (file **06**),
the cost of running a van (file **04**), the depreciation of a counter that a merchandiser stands behind.
The dimension design is what makes those costs land in the same bucket as the revenue they belong to.

## 2. The rule that matters most

> **Put the channel in the dimensions, never in the account code.**

A chart of accounts (ผังบัญชี) that encodes channel, branch and product family inside a long composite
number ages badly: every new marketplace or pop-up becomes a chart change, and the chart is
unmaintainable within two seasons. The durable pattern is **a short chart of accounts crossed with
independent dimensions** — legal entity, location or site, department or channel, class or brand line,
and a free segment for campaign or collection. A new channel then costs **one master record, not a chart
revision**.

### Separate the two things both called "the channel"

| | Where it lives | What it decides |
|---|---|---|
| **Channel classification** | a segment on the **customer master** | the commercial and tax treatment of that customer — tax point, pricing basis, credit terms, which channel process applies |
| **Channel reporting dimension** | **one** ledger dimension | how revenue, cost of sales and cost to serve are grouped for reporting |

They are not the same field and must not be maintained twice. **The classification is the source; the
ledger dimension is derived from it.**

### The failure this prevents, stated precisely

The reference implementation has all the **containers** — legal entity, location, profit and cost centre,
and a named dimension concept — but **never writes down the mapping rule**. Channel identity therefore
ends up living in three places at once: the **location code prefix**, because locations are created from
the sales-channel side; the **department and class**, each derived independently by the point-of-sale and
consignment interfaces from the sale channel on the inbound message; and a **segment of the customer
number**.

That is enough to produce a channel report, and not enough to guarantee that two reports agree. To be
precise about which of the three is at fault: the customer-number segment is legitimate — it *is* the
channel classification, and the customer master is its right home. The defect is the **absence of a
single declared ledger owner**. Nothing said which dimension the reporting channel lives in, so the
location prefix and the interface-derived department and class each became an independent, unreconciled
answer to the same question.

**What to force in a comparable engagement, before build starts:**

1. **Name the owning ledger dimension explicitly.** Which one depends on the estate's shape — *department
   or class* is the usual answer for a brand with many channels selling from shared sites; *location* is
   defensible only where a location serves exactly one channel and always will.
2. **Derive it from the customer master's channel classification** through one governed mapping table —
   not by each interface making its own decision.
3. **Every inbound integration populates it the same way**, from that same table. The mechanism the
   reference used (interfaces deriving account, department and class from the sale channel on the inbound
   message) is correct; what was missing was one authority defining the mapping.
4. **The mapping table is governed master data** with change control and a named owner, not a lookup
   someone maintains on the side.
5. **Location coding may echo the channel for readability but must never be the source of truth.** The
   moment one location serves two channels — a shop that also fulfils online orders — a location-derived
   channel becomes wrong, silently.

Raise this in solution design. It is cheap to fix before build and expensive afterwards, because every
interface and every historical transaction has to be revisited.

## 3. Close, consolidation and the control layer

**What the reference did well, and is worth reusing as a design:**

- **Sequenced module close (การปิดงวด) with a manager-only ledger lock.** Purchasing, inventory, payables,
  fixed assets and receivables each hold their own period and close in order before the ledger period
  itself closes. Reopening a closed period is possible but permission-gated, with the stated caution that
  a reopened period may alter reported figures and require re-approval.
- **Reconciliation (การกระทบยอด) written as a loop, not a checklist.** A mismatch sends the accountant back
  to find the cause; the reconciliation then restarts. Every subledger reconciles to the ledger from
  standard reporting — payables ageing and tax, inventory valuation and ageing, receivables ageing and tax,
  the asset register and its movement history, and the trial balance.
- **Native consolidation** with an elimination entity, elimination-enabled accounts, dedicated intercompany
  customer and vendor records, and system-generated elimination entries at close — which matters as soon as
  a brand trades between manufacturing, distribution and retail companies. Year end sweeps revenue and
  expense to retained earnings automatically.
- **Employee advance clearing (เงินทดรองจ่าย) covering all three settlement outcomes**, including the
  under-spend case where the employee transfers the balance back **before** the clearing entry exists, so
  the receipt reaches bank reconciliation. Most blueprints omit that third case.
- **Segregation on every master change** — requester, approver and accounting maintainer are three distinct
  roles on chart of accounts, location and profit or cost centre alike.
- **Automating the location master feed from the sales-channel system**, while keeping accounting in the
  loop to set the entity and description. Where counters open and close within a season, manual branch-code
  requests are the bottleneck — but an automated feed *without* an approval gate turns a dimension set into
  noise. That compromise is the right one.

**A scoping rule worth carrying:** across the whole reference document set, **journal postings appeared in
only two places.** These were process-flow documents, not accounting specifications. **Treat a process flow
with no journal entries as an incomplete blueprint**, and price the accounting mapping as its own workshop.
A controller cannot review flows whose postings they cannot see.

## 4. Fixed assets as a retail estate register

For a consumer brand the fixed-asset register is **mostly a retail estate register**. The large-value items
are not factory machines. They are shop fit-outs, in-mall counters and shelving, lighting and signage,
point-of-sale terminals and tablets, display units, and fixtures sitting inside a retailer's floor space
that the brand still owns. Notably, the reference design **never names any of these as an asset class and
states no policy for them** — everything below applies by construction rather than by statement. Four
consequences follow.

**1 — Every asset carries the site, and it must be the same site the profit and loss uses.** When a counter
closes and its fit-out moves to another mall, **depreciation (ค่าเสื่อมราคา) has to follow on the day it
happens**, or the closing store carries a charge for an asset it no longer holds and channel profitability
is wrong at exactly the moment someone is deciding whether to keep the site. The reference handles this
well — **transfer (การโอนย้ายสินทรัพย์) with depreciation split by days held on each side, plus
receiving-party confirmation** before the asset accountant processes it. That is stronger than most
blueprints and worth quoting as a target design.

**2 — Useful life should follow the lease, not the fixture.** Fit-out in a leased mall is economically a
leasehold improvement: its life is the shorter of physical life and remaining lease or concession term, and
it needs writing off when the site closes early rather than being carried live. **Nothing in the reference
links an asset to a lease term or a site-closure event**, and disposal is a manual request — so for a brand
opening and closing counters seasonally, the write-off lags the closure by quarters. Raise it as a design
requirement, not a report.

**3 — Counting an estate spread across other people's shops is the hard part.** Code-scan counting
(การตรวจนับสินทรัพย์) is the right answer and the reference shape is sound — printed list, scan, review,
route differences to recount, adjustment, transfer or disposal — but **the scan itself was a gap**: build,
not configuration. **The test question to raise:** can the merchandiser already visiting the store scan
assets on the same device used for stock counting and sale-out capture? **If asset counting needs a separate
visit by a separate team, it will not happen annually in practice.**

**4 — Low-value, high-volume fixtures need a policy before they need a system.** A brand can own tens of
thousands of small display units. Registering each is unmanageable; registering them as one asset per
rollout makes disposal untraceable. The usual resolution is a **capitalisation threshold plus grouped
registration**, with an asset-split capability when part of a batch retires. The reference has the split
mechanism; **the threshold policy was never defined.** Policy first, then mechanism.

**Two further points.** Confirm the **two-book design** — accounting basis and tax basis — early, because
Thai tax and accounting depreciation diverge on exactly the fit-out and equipment categories a retailer
holds most of. And settle explicitly an unresolved sequencing conflict: the business wanted to **sell an
asset first and retire it afterwards by interface**, while the standard flow makes disposal
(การตัดจำหน่าย) generate the invoice. **The two orders produce different points of revenue recognition and
different reconciliation work.** It is a design decision, not a defect — but it must be decided, not
drifted into.

## 5. Functions the system must provide

| # | Function | Why it is needed | Typically standard or custom |
|---|---|---|---|
| 1 | Chart of accounts, location and profit/cost centre masters under a **request → approve → maintain** cycle with three distinct roles | dimension values are the reporting spine; uncontrolled creation destroys comparability | standard |
| 2 | **One governed channel mapping table**, customer classification → ledger dimension | the single defect described in §2 | custom master, governance-dependent |
| 3 | **Location master created and updated by interface** from the sales-channel system, with accounting retaining the approval step | seasonal counters make manual branch-code requests the bottleneck | integration build |
| 4 | Every inbound integration **populating the channel dimension from that one table** | otherwise each interface answers the question differently | integration design |
| 5 | Inactive master values suppressed from transaction screens | stops dead dimensions reappearing on new documents | standard |
| 6 | Manual journal **singly or by bulk upload**, with all-or-nothing file validation | month-end volume is upload-driven; a partial load is worse than none | standard |
| 7 | **Selective approval inside an uploaded batch**, and adding documents to an open batch | one bad line should not reject a whole batch | standard |
| 8 | Journals touching receivable and payable control accounts **forcing selection of a customer or supplier** | protects subledger-to-ledger agreement | usually custom |
| 9 | Petty cash (เงินสดย่อย) and employee advance (เงินทดรองจ่าย) raised, approved and cleared **in the system**, covering all three settlement outcomes | the under-spend case, where cash returns before the clearing entry, is the one usually missed | standard, with custom forms |
| 10 | **Subledger-to-ledger reconciliation reporting** across payables, receivables, inventory and assets | the close depends on it, and it must be a loop | standard |
| 11 | **Per-module period close in sequence**, ledger lock reserved to the accounting manager, reopen permission-gated | prevents back-posting into a reported period | standard |
| 12 | **Consolidation** — elimination entity, elimination-enabled accounts, intercompany customer and vendor records, generated elimination entries | multi-entity brands consolidate every period, not annually | standard |
| 13 | **Year-end sweep** of revenue and expense to retained earnings | routine, but must be verified as generated rather than keyed | standard |
| 14 | **Channel and campaign profitability reporting** — margin by channel, by collection, and cost to serve | the first report the commercial director asks for | reporting build |
| 15 | **Drill-back from a ledger balance to the source transaction** chain | in a high-volume multi-channel business this is where month-end investigation time goes | often a gap — verify |
| 16 | Asset classification carrying the **account mapping**, with capitalisation proposed automatically from the purchasing chain | keeps posting rules in one place instead of on each asset | standard |
| 17 | **Direct registration and bulk import** of assets, outside the purchasing chain | opening balances, group transfers, count adjustments, self-constructed assets | standard, needs a verification control |
| 18 | **Transfer with depreciation split by days held**, plus receiving-party confirmation | the counter-moves-mall case, and the control that makes it auditable | standard |
| 19 | **Disposal as write-off or as sale**, revaluation, asset split, and suspend/restart of depreciation | a retail estate churns; all four events are routine | standard |
| 20 | **Two asset books** — accounting basis and tax basis | Thai tax and accounting lives diverge on retail fixtures | standard |
| 21 | **Scan-based physical count** with differences routed to recount, adjust, transfer or dispose | an estate inside other people's shops cannot be counted from a desk | usually custom |
| 22 | **Asset period close as the posting event to the ledger**, blocked while registrations are outstanding | stops orphan capitalisations sitting outside the accounts | standard |

## 6. Challenges, gaps and improvement areas

| What commonly goes wrong | What the reference implementation did | What a better design looks like |
|---|---|---|
| **Channel identity in three places at once** | location prefix, interface-derived department and class, and a customer-number segment — all unreconciled | declare one owning ledger dimension, derive it from the customer classification through one governed table, and make every interface use it |
| **Channel encoded in the account code** | avoided in structure — the containers exist | keep the chart short and the dimensions independent, so a new channel is one master record |
| **Channel and campaign profitability absent** | the report inventory was wholly control-oriented — no margin by channel, by collection, or cost-to-serve view | design the commercial reporting set alongside the control set, not after go-live |
| **Drill-back to source transactions** | recorded as unresolved | test it in the demo with a real chain: journal ← payment ← invoice ← goods receipt ← order ← requisition |
| **Prepaid amortisation** | recorded as unresolved | seasonal marketing prepayments and mall deposits are standing features of retail — scope it in |
| **Elimination by shareholding proportion, and minority interest** | recorded as unresolved | bites the moment a joint-venture retail entity exists; confirm the group structure before quoting |
| **Exchange-rate maintenance** | manual; an automated central-bank rate feed was raised as a gap | cheap to build, and it removes a recurring monthly keying error |
| **Statutory disbursement voucher (ใบสำคัญจ่าย)** | recorded as a gap across vendor prepayment and both petty-cash flows | count the Thai statutory forms during discovery and price them as line items — see file **17** |
| **Process flows with no journal entries** | postings appeared in only two places across the whole document set | treat that as an incomplete blueprint and run an accounting-mapping workshop |
| **Retail fixtures never defined as an asset class** | no policy for fit-out, counters, point-of-sale hardware or in-mall shelving | set the capitalisation threshold and the grouped-registration policy before configuring anything |
| **Fit-out life not linked to the lease** | no link between an asset, a lease term or a site closure | write-off must be triggered by the closure event, not discovered a quarter later |
| **Asset counting designed as its own expedition** | scan capability was a build item | put the count on the device the merchandiser already carries, or accept it will not happen |
| **Sell-then-retire against dispose-then-invoice** | an unresolved conflict between the business preference and the standard flow | decide it explicitly: the two orders differ in revenue recognition point and reconciliation effort |

**Scoping signals — raise the estimate when you see:** channel or campaign profitability expected as
standard reporting · more than one legal entity, especially with intercompany trading or a joint venture ·
drill-back from the ledger to source transactions as a stated requirement · a retail estate with counters
opening and closing within the year · asset counting across sites the brand does not control · two-book
accounting and tax depreciation · statutory Thai forms that the standard output does not produce.

## 7. Discovery questions

1. When your commercial director asks for margin by channel, where does that number come from today? ⚑
2. Which single field in your system tells you the channel — and does every system agree on it? ⚑
   *(if the answer names more than one field, you have found the §2 defect)*
3. Who is allowed to create a customer, and who sets its channel classification?
4. How long does it take to trace a ledger balance back to the transaction that caused it?
5. How many legal entities are there, do they trade with each other, and is any of them a joint venture? ⚑
6. What closes first at period end, and who is allowed to reopen a closed period?
7. What are your biggest assets — and how many of them sit inside someone else's store? ⚑
8. When a counter closes, how quickly does the fit-out get written off?
9. Is there a capitalisation threshold for small fixtures, and how are batches of them registered?
10. When do you count fixed assets, who does it, and on what device?
11. Do you keep separate accounting and tax depreciation?
12. When you sell an asset, does the sale come first or the retirement? ⚑

## Related files

- **10** trade spend and Net GP — the deductions that decide whether channel margin is real
- **11** inventory, locations and costing — the backbone the ledger receives postings from
- **12** transformation and production — the other source of cost postings
- **13** demand planning — the plan these dimensions eventually report against
- **14** procurement and budget control — which feeds the same dimensions from the buy side
- **16** the application estate — where every inbound message populates these dimensions
- **17** Thailand compliance — electronic tax documents. **Tax depreciation is not covered there**
  and is an open question for the client's adviser
- **18** investment promotion — where the ledger must additionally segregate promoted business
- **19** the full discovery bank
