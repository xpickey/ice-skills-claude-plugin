# 13 — Demand planning (การวางแผนอุปสงค์)

> **Load this when:** the prospect forecasts, plans production or replenishment, runs promotions that
> must be planned before they are settled, sells goods carrying an expiry date, or asks how retailer
> sell-through data becomes a number the factory can act on · the words forecast accuracy, safety stock,
> MRP, FEFO, shelf life, cannibalization, consensus or sell-through appear.
> **Do not load this for:** what a promotion finally costs — accrual, deduction, rebate, Net GP → file
> **10** · lots, locations and costing → **11** · production and bills of materials → **12** ·
> purchasing and budget → **14**.
> **Source basis:** a Thai food and beverage manufacturer's demand-planning specification, twelve
> screens deep and far richer on this subject than the apparel reference case, which contributes the
> seasonal-collection material where the two differ. Where the source states a rule but gives no
> formula, this file says so rather than inventing one.

## Read this first — "sell-through" here means demand, not revenue

Throughout this file, **sell-through (ยอดขายออก) is a demand signal** — what the shopper
actually bought, as distinct from what the retailer ordered. Nothing here says anything about when
revenue is recognised; the accounting sense of the same word, where sale-out *is* the revenue event in
consignment, belongs to file **03**, with the channel view in **02**. One retailer feed usually serves
both purposes, which is exactly why the senses get conflated. When a client says "we handle sale-out",
the useful reply is *"for revenue recognition, or for forecasting?"* File **00** carries the two-sense
table this paragraph is bound to.

## 1. The spine

```
History (sell-through and sell-in feeds)
  → statistical baseline by SKU, banner and location
  → layers applied: promotional uplift · seasonality · shelf-life constraint
  → consensus, override, version lock
  → net unconsumed forecast → factory MRP · safety stock → replenishment
  → accuracy and bias measured → back into method and override review
```

What makes it work is a **weekly rolling cycle tied to the retailer order window**: last week's
point-of-sale data lands early in the week, the baseline refreshes, the horizon rolls forward, the near
horizon locks, and supply planning has the rest of the week to react before delivery day. A plan
refreshed monthly cannot serve a channel that orders weekly.

Two structural facts shape everything below. **The forecasting grain is SKU × banner × channel format ×
location × period** — banner and channel format sit *inside* the key, because the same SKU behaves
differently in a convenience chain and a hypermarket. And **base demand and promotional demand are held
as separate quantities summing to the gross**, enforced at save; a system storing only the total can
never tell trend from campaign.

## 2. Baseline and hierarchy

History is decomposed into **base, seasonal, trend and promotional components** over a configurable
lookback per SKU, store and banner. Below a minimum of clean history the system should refuse to fit
statistically and route the item to the new-product path — a forecast fitted on too little history looks
authoritative and is not. Three disciplines carry the weight: SKUs are **auto-classified into a
demand-pattern class** so an intermittent item is not smoothed like a fast mover, and moving off the
automatic method needs a written reason; **each outlier is dispositioned** — exclude, treat as an event
curve, or keep — before the version can be submitted, so panic buying and viral spikes never enter the
trend; and **confidence is computed, never keyed**.

The **hierarchy** runs SKU → brand → banner → channel format → distribution centre or route → region →
national across day, week, month and annual buckets, reconciling top-down, bottom-up and middle-out with
detail always summing to aggregate as a blocking rule. **Roll-forward** advances the horizon
automatically; near buckets freeze behind a **planning fence** and change only by formal override, while
far buckets absorb new actuals. What makes a head-office promotion executable is **banner-to-store
disaggregation** — volume agreed centrally is spread to stores using uplift, a store-size index and
trailing velocity share, and the store sum must reconcile back to the banner total or the run is blocked.

**Version governance** carries four layers — statistical baseline → promotion-adjusted → consensus →
final committed and locked for supply — with immutable history, so a correction is a new version, not an
edit. Every override records type, original quantity, override quantity, justification and computed
magnitude; **approval escalates by magnitude tier**; and every override **expires and auto-reverts unless
re-confirmed**, because a temporary adjustment left alone becomes permanent bias inside the production
plan. Makers may not approve or lock their own work.

## 3. Promotions — uplift, cannibalization, and the master shared with trade spend

A promotion carries a demand-side object distinct from its commercial terms: an **uplift factor and curve
shape** keyed by promotion type, banner, channel and season; a **pull-forward window** and a
**post-promotion dip window**; a **cannibalization set** of other SKUs with cross-elasticity values; and
an **external signal** field for competitor or category movement. Cross-elasticity is normally negative —
a positive value means a complementary product and must be confirmed — and a promoted SKU may never sit
in its own cannibalization set. Overlapping promotions on the same SKU and banner window are **simulated
combined, never separately**.

**True-up closes the loop.** At promotion close the actual sell-through quantity is captured, variance against
the planned promotional quantity computed, and that variance exposed as an interface to trade-spend
accrual and rebate return-on-investment. The demand side references and trues up; it never settles.
Whoever creates the linkage may not approve the variance going to accrual, a variance beyond tolerance
requires validation before release, and editing a linkage after lock must **flag every dependent forecast
for refresh** rather than silently recalculate.

> **The rule that must survive into the design: one promotion, one master record, two consumers.** The
> promotion master belongs to the trade-spend domain (file **10**); planning binds to it through a single
> shared promotion identifier and has no create-or-edit action of its own.

If the two domains hold **separate promotion records**, the failure is specific and expensive. The
sell-through quantity used to accrue the scanback or rebate liability and the sell-through quantity used
to forecast then come from different definitions of the same campaign — different date windows, different
SKU lists, different store scope. Finance accrues against one number while planning produces to another,
the true-up variance cannot be reconciled to the deduction the retailer actually takes, and neither side
can prove which is right. **Verify at discovery whether the promotion calendar and the forecast reference
the same record; two spreadsheets that are supposed to match is a finding, not a detail.**

## 4. Sell-in against sell-through

| Signal | Thai | What it is | How it misleads |
|---|---|---|---|
| **Sell-in** | ยอดขายเข้า | the order or withdrawal signal — the distributor's order to the factory, the retailer's order to the distributor | inflated when the channel builds its own stock; a spike may be replenishment, not demand |
| **Sell-through** | ยอดขายออก | actual point-of-sale consumption at the retailer | the true signal, but it arrives late and incomplete |

**Derive primary demand from verified sell-through, not from sell-in**, so the plan does not chase order
spikes that are only channel filling. The derivation is a trailing average on sell-through with
promotional pull-forward periods excluded; where every period in the lookback carries a promotion flag
the clean average cannot be computed, and the run must warn rather than produce a number.

**The divergence exception is the valuable part.** High sell-in against low sell-through flags
**channel-stuffing and obsolescence risk**, routing the row to a review queue and blocking until
dispositioned from a closed list — accept the stock build · reduce the next purchase order · redistribute
· return to supplier · markdown — each with written justification. Accepting a stock build on a
near-expiry item raises an extra write-off warning, and the reviewer who dispositions may not approve.

Two engineering details decide whether this works. **Feed lag is designed for, not assumed away**: a
per-banner latency and service level are held as data, alignment is lag-aware, and beyond the service
level derivation is deferred rather than run on stale data, or the plan oscillates. And **join integrity
is absolute**: every point-of-sale row resolves through a SKU-to-retailer article-code cross-reference
master with validity windows, and unresolvable rows are **quarantined, not guessed** — deduction matching
in file **10** joins on that same master, so it is one master governed once.

Modern trade and van sales are **structurally different demand flows** that must not be reconciled with
each other's logic: modern trade is point-of-sale driven, while van sales and traditional trade have no
point-of-sale feed at all and are inferred from delivery and order history. Separate models, separate
service levels — files **04** and **01**.

## 5. Shelf life as a planning dimension (FEFO และอายุสินค้า)

This dimension does not exist in a fashion practice. Apparel has dead stock; food has dead stock **with a
date on it**, which turns a slow-moving problem into a write-off with a deadline.

For each production lot the system estimates a **consumption date** from forecast plus lead time, compares
it against expiry, and raises a **near-expiry flag** when remaining shelf life falls short of the lead
time to the next demand window or below a configured threshold. Three outputs follow: the per-lot flag, a
**lot-aging report** that triggers action, and a **consumption schedule** by distribution centre, store
and SKU handed to the warehouse to drive FEFO bin allocation and cross-dock sequencing — worth saying out
loud in a design review, because **bin allocation is then driven by a plan, not decided on the warehouse
floor**. An action is mandatory before a flagged lot can be saved — route to a high-velocity outlet, mark
down, return to supplier, or quarantine. Return and quarantine need quality approval, and **a markdown
must be tied to a promotion so it can be trued up and reach trade spend**, or the margin loss disappears
from Net GP. Expired lots and lots on quality hold are barred from allocation outright.

Two rules carry commercial weight. **Minimum remaining shelf life at receipt is a policy owned here and
enforced at goods receipt** — a short-dated lot is blocked or escalated — and the rule is per customer and
per retailer, so it is a discovery question, never an assumption. And **FEFO outranks fair share**: where
fair-share allocation would spread an ageing lot evenly, FEFO leads and pushes it to high-velocity outlets
first, fair share second. A system treating fair share as sovereign will age stock in slow stores.

## 6. From forecast to supply — MRP, capacity, safety stock

The handoff to the factory is the **net unconsumed forecast** — gross less the sales orders that have
already consumed it, floored at zero — by SKU, location and period, exploded against the bill of materials
with lead-time offsets. Consumed exceeding gross raises a supply exception rather than a negative number.
MRP may only be fed from a locked version, and rows missing a required dimension are quarantined first.

**Capacity is checked in the same pass** against line capacity, any drying or curing time and minimum batch
size: demand above capacity raises a bottleneck warning with the shortfall, and demand that does not divide
into the minimum batch warns about over-production. **Low, base and high scenarios** size pre-festival
ramp-up, with a **post-festival drawdown trigger** stepping down safety stock and the production ramp after
the peak — explicitly to prevent the overstock and write-off short-shelf-life goods suffer once a festival
passes.

**Safety stock is a governed policy, not an assumed buffer**: held per SKU by location or channel, driven by
demand variability, lead-time variability, average demand and lead time against a service-level target,
**differentiated by channel** with seasonal modulation, and escalated for approval where a target exceeds
the channel norm. New SKUs fall back to a percent-of-forecast rule until history is sufficient, and observed
stockout rates are compared back against what the service level implied, so the policy is corrected rather
than trusted.

> **Honesty flag — confirm, do not assume.** The source states the reorder-point relationship (average
> demand over the lead time, plus safety stock) and nothing more. **The safety-stock formula itself, the
> service-level-to-Z-score table, the statistical methods behind the pattern classes, the uplift curve
> mathematics and the cannibalization model are specified nowhere.** Treat all five as customer decisions to
> confirm with the planning team. Every numeric threshold in the source — divergence, near-expiry days,
> minimum shelf life at receipt, accuracy and bias tolerances, override escalation tiers, service-level band
> — is marked illustrative by its own authors and must never be quoted as a benchmark.

## 7. Measuring it — forecast accuracy (WMAPE / MAPE / bias)

Three metrics with three jobs, at SKU × banner × period grain: **WMAPE** is volume-weighted and is the
headline portfolio measure; **MAPE** suits high-velocity items and is switched off for intermittent ones;
**bias** detects systematic over- or under-forecasting, and is the one that quietly costs money. Four points
separate a real accuracy loop from a report. **Baseline and promotional periods are measured separately**
with their own tolerances, so a promotional miss triggers review of the uplift assumption rather than of the
baseline method. **Zero and low-demand periods are safeguarded** — excluded, or a floor applied — so a
near-zero denominator cannot distort the headline. **Two feedback loops run**: accuracy below tolerance
opens a forecast review and can re-fit the method or pattern class, while persistent one-directional bias
triggers **override validation**, examining the override that caused it beside the statistical original and
the actual. And **segregation of duties holds** — whoever acknowledges an accuracy alert is not whoever
raised the review or authored the override.

## 8. New products, supersession and seasonality

**No history is the normal case, not the exception** — for a food brand at launch, for a fashion brand every
season. A new SKU borrows from reference SKUs matched on attributes (category, price, form, size, channel),
all mandatory before seeding and with no self-reference. Launch runs an **S-curve ramp** across trial,
adoption and maturity, re-fitted weekly against actual sell-through, with deliberately conservative initial
stock and a **shortened replenishment cadence** while the ramp is unproven; **supersession** transfers demand
history to the successor SKU so the forecast line stays continuous. The retailer article code must exist
*before* seeding, or point-of-sale and deduction matching both fail. The apparel practice states the same
idea in its own vocabulary — **plan at the level that has history, size at the level that does not**:
forecast volume at collection or category level, then break it to SKU by size curve and colour mix using
sell-through ratios observed at the same point in prior seasons. That breakdown is where an apparel forecast
either works or fills the warehouse with the wrong sizes.

**Seasonality is a maintained master, not a curve someone drew.** For Thailand that means moving-date
festivals — Chinese New Year, Songkran, Loy Krathong, the year-end gift season, back-to-school — each with
lead days, a build-up shape and a **post-festival cliff window**, maintained a year or more ahead, with
prior-year actuals able to override the configured impact. Critically, **a driver marked regional must carry
a region scope**, because a national curve masks local timing and produces a plan that is early in one
region and late in another.

## 9. Functions the system must provide

| # | Function | Why it is needed | Typically standard or custom |
|---|---|---|---|
| 1 | Baseline with **base / seasonal / trend / promotional decomposition** | promotional volume left in the trend corrupts every future period | standard engine, custom decomposition rules |
| 2 | **Demand-pattern classification** with reasoned method override, and **mandatory outlier disposition** before submit | one method fits no whole catalogue, and spikes otherwise enter the trend silently | usually custom |
| 3 | Reconcilable **hierarchy** with detail summing to aggregate, plus **roll-forward behind a planning fence** | the aggregate and the detail must be the same plan, and the committed horizon must not drift | standard in a planning tool, custom in an ERP alone |
| 4 | **Banner-to-store disaggregation** reconciling back to the banner total | head-office promotions have to reach the right shops | custom |
| 5 | **Promotion linkage** — uplift curve, pull-forward, post-promotion dip, cannibalization set | the demand-side assumption of a campaign, held as data | custom |
| 6 | **One shared promotion master** with trade spend, bound by a single identifier | two records mean accrual and forecast disagree — see §3 | integration design plus a governance decision |
| 7 | **Promotion true-up** at close, variance exposed to accrual | closes the loop between what was planned and what sold | custom |
| 8 | **Sell-in / sell-through reconciliation** with divergence flag and closed disposition list | detects channel stuffing before it becomes write-off | custom |
| 9 | **Lag-aware point-of-sale ingestion**, joined through an **article-code cross-reference master** with validity windows and quarantine | stale feeds cause whiplash, and one join failure breaks point-of-sale *and* deduction matching | integration build plus custom governance |
| 10 | **Shelf-life demand and lot aging** — consumption date against expiry, mandatory action set | food dead stock has a deadline | custom |
| 11 | **Minimum remaining shelf life at receipt**, and a **FEFO consumption schedule** that outranks fair share | the retailer's rule applied at the earliest controllable point; allocation follows the plan, not the floor | custom, per retailer |
| 12 | **Forecast consumption netting** floored at zero, feeding a **capacity and scenario check** — line, batch, curing, low/base/high | the only quantity MRP should see, and a plan the factory cannot make is not a plan | standard in manufacturing suites |
| 13 | **Safety stock policy** per SKU and channel, service-level differentiated | one buffer rule over-serves some channels and starves others | standard calculation, custom governance |
| 14 | **Accuracy and bias measurement**, baseline and promotional measured apart | without it nobody knows whether the plan is improving | standard reporting, custom split |
| 15 | **Version governance** — four layers, immutable history, expiring overrides, consensus lock | stale overrides otherwise sit permanently inside MRP | custom |
| 16 | **New-product seeding and supersession** with attribute-matched references and an S-curve ramp | most launches have no history at all | custom |
| 17 | **Seasonality calendar** with regional scope and post-festival cliff | moving festival dates cannot be a fixed monthly index | custom master |

Functions 4, 6, 8, 10, 11 and 15 are where the effort concentrates, and 6 is where the deal usually breaks
during implementation.

## 10. Challenges, gaps and improvement areas

| What commonly goes wrong | What the reference implementations did | What a better design looks like |
|---|---|---|
| **Planning off the order signal** | the food specification names the distortion outright — the distributor builds its own stock and the factory chases it | derive primary demand from verified sell-through, keeping sell-in as the reconciliation counterpart |
| **Channel stuffing found at write-off** | divergence flag, review queue, closed disposition list | make the flag blocking, and tie an accepted stock build on a short-dated item to the shelf-life warning |
| **Retailer feed lag ignored** | latency and per-banner service level held as data, derivation deferred beyond it | never compute on stale data — defer and say so, rather than publishing a plan that oscillates |
| **Promotion and forecast in separate masters** | one shared promotion identifier, planning referencing only | one master, one identifier, two consumers — and check it at discovery, because two spreadsheets is the common as-is |
| **Overrides that never expire** | expiry with auto-revert unless re-confirmed, approval escalating by magnitude | treat an override as temporary by construction, not by intention |
| **Shelf life treated as a warehouse concern** | owned in planning — consumption date, lot aging, action set, receipt gate | plan against expiry, and let the plan drive FEFO allocation; a markdown outside the promotion structure never reaches Net GP in file **10** |
| **No path from plan to production** | the apparel design connected planning to purchasing and transfers but **not to work orders, bills of materials or routing** — a broken link for a brand that makes or subcontracts | insist on the MRP handoff explicitly; see file **12** |
| **One forecasting method for the whole catalogue** | a single moving average over a short history window | continuity lines, seasonal collections and campaign items behave differently — per-plan method selection is the enabler |
| **Reorder point mistaken for a plan** | reorder-point replenishment with automatic transfer requests | reactive replenishment refills what already sold; a finite seasonal buy needs initial allocation and in-season rebalancing |
| **Retailers that supply no data at all** | at least one banner submits manually on its own cycle | build consensus to accommodate per-retailer cadence rather than assuming a feed |
| **Thresholds quoted to a client as benchmarks** | every threshold in the source is marked illustrative by its authors | no defensible market figure exists for accuracy, divergence or shelf-life rules — ask, never quote |

## 11. Discovery questions

1. What do you forecast today, and at what level — item, category, brand, or the whole account? ⚑
2. Does your forecast start from what retailers ordered, or from what shoppers actually bought? ⚑
3. Which retailers give you point-of-sale data, how often, and how many days behind is it? ⚑
4. When a retailer's order jumps, how do you tell a real uplift from the channel building stock?
5. Where does a promotion live before it is settled — and is that the same record finance accrues against?
   ⚑ *(the file 10 seam; two records is the finding)*
6. After a campaign ends, who compares what you planned to sell with what sold, and what happens to the
   difference?
7. For products with an expiry date, what remaining shelf life must a lot have when it reaches the
   retailer's dock — and does that rule differ by retailer? ⚑
8. How do you decide today which lot ships to which store?
9. Does your plan feed production, or only purchasing? ⚑
10. How is safety stock set — one rule for everything, or per channel? When did anyone last check it
    against actual stockouts?
11. How do you forecast a product that has never been sold?
12. How do you handle festivals whose dates move, and does the timing differ by region?
13. Do you measure forecast accuracy, and is promotional error measured apart from baseline error?
14. Who may override the forecast, and what happens to that override three months later? ⚑

## Related files

- **00** the channel map, and the two-sense table for sale-out and sell-through
- **02** modern trade — where the sale-out feed comes from, in its accounting sense
- **03** consignment — the accounting meaning of sale-out, kept deliberately separate from this file
- **04** van sales — the demand flow with no point-of-sale signal at all
- **10** trade spend and Net GP — the shared promotion master, accrual and true-up counterpart
- **11** inventory, locations and costing — lots, expiry dates, and the stock the plan commits
- **12** transformation and production — what the MRP handoff actually drives
- **16** the application estate — where planning sits and what feeds it
- **19** the full discovery bank
