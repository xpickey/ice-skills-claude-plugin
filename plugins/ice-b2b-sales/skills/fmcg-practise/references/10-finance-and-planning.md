# 10 — Finance and planning: ledger, assets, demand

> Load this when the general ledger, dimensions, channel profitability, period close,
> consolidation, fixed assets for a retail estate, or demand planning are in scope.

---

## Part A — General ledger and channel profitability

### The framing

A brand selling through wholesale, modern trade, its own stores, marketplaces and export **does not
have a revenue number — it has five, with structurally different cost to serve.** The ledger has to
answer *which channel earned this, and what did it cost to earn it*, without anyone rekeying a
spreadsheet.

### The rule that matters most

> **Put the channel in the dimensions, never in the account code.**

A chart of accounts that encodes channel, branch and product family inside a long composite number
ages badly: every new marketplace or pop-up becomes a chart change, and the chart is unmaintainable
within two seasons.

The durable pattern is **a short chart of accounts crossed with independent dimensions** — legal
entity, location or site, department or channel, class or brand line, and a free segment for campaign
or collection. A new channel then costs **one master record, not a chart revision**.

### The largest gap in the reference implementation

The reference design has the **containers** — company, location, profit and cost centre, and a named
dimension concept — but **never writes down the mapping rule**. Worse, channel identity ends up living
in **three places at once**:

1. the **location** prefix (locations are created from the sales-channel side)
2. the **department and class**, derived by the point-of-sale and consignment interfaces from the sale channel
3. a **segment of the customer number**

That is enough to produce a channel report, and not enough to guarantee that two reports agree.

**To be precise about which of the three is at fault:** the third is legitimate — the customer-number
segment is the *channel classification*, and the customer master is the right home for it. The defect
is the **absence of a single derived ledger owner**: nothing declared which dimension the reporting
channel lives in, so the location prefix and the interface-derived department and class each became
an independent, unreconciled answer to the same question.

### Separate the two things both called "the channel"

Before deciding which dimension owns channel, separate the two concepts the word covers, because
conflating them is what produced the three-places-at-once problem:

| | Where it lives | What it decides |
|---|---|---|
| **Channel classification** | a segment on the **customer master** | the commercial and tax treatment of that customer — tax point, pricing basis, credit terms, which channel process applies |
| **Channel reporting dimension** | one **ledger dimension** | how revenue, cost of sales and cost to serve are grouped for reporting |

They are not the same field and should not be maintained twice. **The classification is the source;
the ledger dimension is derived from it.**

**What to force in a comparable engagement, before build starts:**

1. **Name the owning ledger dimension explicitly.** Which one it is depends on the estate's shape —
   *department or class* is the usual answer for a brand with many channels selling from shared
   sites, and *location* is defensible only where a location serves exactly one channel and always
   will. Whichever is chosen, write it down as the single owning dimension.
2. **Derive it from the customer master's channel classification**, through one governed mapping
   table — not by each interface making its own decision.
3. **Every inbound integration populates it the same way**, from that same table. In the reference
   implementation the point-of-sale and consignment interfaces each derived department and class
   from the sale channel on the inbound message, which is the right mechanism; what was missing was
   a single authority defining the mapping.
4. **The mapping table is governed master data** with change control and an owner, not a lookup
   someone maintains on the side.
5. **Location coding may echo the channel for readability, but must not be the source of truth.**
   The moment one location serves two channels — a shop that also fulfils online orders — a
   location-derived channel becomes wrong, silently.

Raise this in solution design. It is cheap to fix before build and expensive afterwards, because
every interface and every historical transaction has to be revisited.

### What the reference implementation did well

- **Native consolidation with an elimination company and elimination-enabled accounts** — matters for a
  brand trading between manufacturing, distribution and retail entities, and the intercompany
  treatment was specified at the right level of detail.
- **Sequenced module close with a manager-only ledger lock** — closes modules in order and prevents
  back-posting.
- **Reconciliation written as a loop, not a checklist** — the process returns to the difference until it
  clears.
- **Employee advance clearing covering all three settlement outcomes**, including the cash-returned
  case, which most blueprints omit.
- **Automating the location master feed from the sales-channel system.** Where counters open and close
  within a season, manual branch-code requests are the bottleneck. The right compromise was kept:
  the feed is automated, but accounting stays in the loop to set the company and description — an
  automated feed without an approval gate turns a dimension set into noise.

### What was thin — and worth raising in any comparable deal

| Area | Why it matters for a consumer brand |
|---|---|
| **Drill-back from the ledger to the source transaction** — unresolved | in a high-volume multi-channel business, this is where month-end investigation time goes |
| **Prepaid amortisation** — unresolved | seasonal marketing prepayments and mall deposits are standing features of retail |
| **Elimination by shareholding proportion** — unresolved | bites the moment a joint-venture retail entity exists |
| **Channel and campaign profitability reporting — absent entirely** | the report inventory was wholly control-oriented: no margin by channel, margin by collection, or cost-to-serve view. **This is the first report the commercial director asks for.** |

**A finding to carry as a scoping rule:** across the whole reference document set, **journal postings
appeared in only two places.** These were process-flow documents, not accounting specifications.
**Treat a process flow with no journal entries as an incomplete blueprint**, and price the accounting
mapping as its own workshop. A controller cannot review flows whose postings they cannot see.

---

## Part B — Fixed assets: a retail estate register

### The reframe

For a consumer brand the fixed-asset register is **mostly a retail estate register**. The
large-value items are not factory machines. They are shop fit-outs, in-mall counters and shelving,
lighting and signage, point-of-sale terminals and tablets, display units, and fixtures sitting inside
a retailer's floor space that the brand still owns.

Four consequences follow.

### 1. Every asset carries the site — and it must be the same site the profit and loss uses

When a counter closes and its fit-out moves to another mall, **depreciation has to follow on the day
it happens.** Otherwise the closing store carries a charge for an asset it no longer holds, and
channel profitability is wrong at exactly the moment someone is deciding whether to keep the site.

The reference implementation handles this well: **transfer with depreciation split by days held, plus
receiving-party confirmation.** That is the correct design and stronger than most blueprints.

### 2. Useful life should follow the lease, not the fixture

Fit-out in a leased mall is economically a **leasehold improvement**. Its life is the shorter of
physical life and remaining lease or concession term, and it needs writing off when the site closes
early rather than being carried live.

**Nothing in the reference design links an asset to a lease term or a site-closure event**, and
disposal is a manual request. For a brand opening and closing counters seasonally, the write-off then
lags the closure by quarters. Raise this as a design requirement, not a report.

### 3. Counting an estate spread across other people's shops is the hard part

Barcode or code-scan counting is the right answer, and the reference shape is sound — printed list,
scan, review, route differences to recount, then adjust, transfer or dispose. But **the scan itself
was a gap**: build, not configuration.

**The test question to raise:** can the merchandiser already visiting the store scan assets on the
same device used for stock counting and sale-out capture? **If asset counting needs a separate visit
by a separate team, it will not happen annually in practice.**

### 4. Low-value, high-volume fixtures need a policy before they need a system

A brand can own tens of thousands of small display units. Registering each is unmanageable;
registering them as one asset per rollout makes disposal untraceable.

The usual resolution is a **capitalisation threshold plus grouped registration**, with an asset-split
capability available when part of a batch retires. The reference implementation has the split
mechanism; **the threshold policy was not defined.** Policy first, then mechanism.

### Two further points

- **Confirm the two-book (accounting and tax) depreciation design early.** Thai tax and accounting
  depreciation diverge on exactly the fit-out and equipment categories a retailer holds most of.
- **An unresolved sequencing conflict worth settling explicitly:** the business wanted to sell an asset
  first and retire it afterwards by interface, while the standard flow makes disposal generate the
  invoice. **The two orders produce different points of revenue recognition and different
  reconciliation work.** This is a design decision, not a defect — but it must be decided, not drifted
  into.

---

## Part C — Demand planning for seasonal goods

### Why fashion breaks standard forecasting

Statistical forecasting assumes the item selling next season is the item that sold last season. **A
collection replaces itself.** Most stock-keeping units being planned have **no history at all**, and
the ones that do are about to be discontinued.

### The durable pattern: plan at the level that has history, size at the level that does not

**Two stages:**
1. **Forecast volume at collection or category level**, where last season genuinely informs next season.
2. **Break that volume down to SKU by size curve and colour mix**, using sell-through ratios observed at
   the same point in previous seasons.

The reference implementation gets the first half right and says so explicitly — forecasting is done
for the **collection group** — and uses an **alternate-source item** so a new item can borrow a
predecessor's history. That is the correct mechanism.

**The readable pages never mention the size-and-colour breakdown.** For apparel, that is precisely
where a forecast either works or fills the warehouse with extra-small and no large. Probe it directly.

### One forecasting method should not govern the whole catalogue

The reference implementation uses a **moving average over roughly six months of history, projecting
six to twelve months forward**. That is reasonable for continuity lines and a poor fit for seasonal
peaks, where a history window spanning one season systematically over- or under-states the next. A
seasonal-average method exists for exactly this case, at the cost of forcing monthly intervals.

**The point to raise:** continuity basics, seasonal collections and campaign items behave differently.
**Per-plan method selection** is what makes differentiating them possible.

### A demand plan for a multi-channel brand is really two plans

- **How much to buy or make** — the forecast.
- **Where to place it and when to move it** — the allocation and replenishment plan.

The reference implementation answers the second with **reorder-point replenishment and automatic
transfer requests**, which is right for keeping counters stocked. But reorder point is **reactive** —
it refills what has already sold. For a seasonal collection with a finite buy and a fixed selling
window, initial allocation and in-season rebalancing matter more than reorder point, because there is
no replenishment to be had once the buy is exhausted.

### Two structural gaps in the reference design

- **No path from the demand plan into production.** Planning connects to purchasing (suggested planned
  orders becoming purchase orders) and to inter-site transfers, but **not to work orders, bills of
  materials or routing** — even though those components exist elsewhere in the system. For a brand that
  makes or subcontracts, that is a broken link. See file **08** for where transformation and production
  actually live.
- **Three pages of the source design were unreadable images**, covering plan review and adjustment, plan
  reporting, and order-item management. Those areas are therefore **not documented in this skill** —
  stated here rather than glossed over.

---

## Scoping signals across all three areas

Raise the estimate when you see:
- Channel or campaign profitability expected as standard reporting
- More than one legal entity, especially with intercompany trading or a joint venture
- Drill-back from the ledger to source transactions as a stated requirement
- A retail estate with counters opening and closing within the year
- Asset counting across sites the brand does not control
- Two-book accounting and tax depreciation
- Seasonal collections with no sales history and a size-and-colour breakdown requirement
- Demand planning expected to drive production, not only purchasing

## Discovery questions

1. When your commercial director asks for margin by channel, where does that number come from today?
2. Which single field in your system tells you the channel — and does every system agree on it?
3. How long does it take to trace a ledger balance back to the transaction that caused it?
4. What are your biggest assets — and how many of them sit inside someone else's store?
5. When a counter closes, how quickly does the fit-out get written off?
6. When do you count fixed assets, and who does it?
7. How do you forecast an item that has never been sold before?
8. Does your plan tell you how much to buy, where to send it, or both?

## Related files

- **07** the inventory and costing backbone the ledger receives postings from
- **08** where production and transformation actually live
- **09** procurement and budget, which feed the same dimensions
- **11** the estate that populates these dimensions on every inbound message
- **12** the gaps above, consolidated with industry benchmarks
