# 11 — Inventory, locations and costing (คลังสินค้า ตำแหน่งเก็บ และต้นทุน)

> **Load this when:** warehouse and location structure, bins, lots, expiry, third-party logistics,
> fulfilment, costing method, stock valuation, counting, ageing or dead stock are in scope · or when
> a prospect says their stock figure is never right.
> **Do not load this for:** how a channel *sells* → **00**-**09** · what the retailer deducts when
> short-dated stock is rejected → **10** · how movements post to the ledger → **15** · the warehouse
> and point-of-sale interfaces themselves → **16**.
> **Source basis:** two implementations strong in opposite halves. The apparel case supplies location
> topology, the moving-average costing decision and the analytics; the food and beverage case supplies
> bin-and-lot discipline, directed put-away, wave picking and the entire shelf-life layer, which
> apparel has no equivalent of. Where they differ it is a difference of category, not a contradiction.
> Every figure in both is declared illustrative by its own authors, so this file carries no values.

## 1. Location topology — eight functional groups, not two

The instinct is to model warehouses and shops. The apparel reference controls locations by **eight
functional groups**, each existing because stock in it behaves differently in the accounts:

| # | Location group | Thai | Owned by the brand? | Sellable now? |
|---|---|---|---|---|
| 1 | Trading stock | คลังซื้อขาย | yes | yes |
| 2 | Transformation / decoration | คลังแปรสภาพ | yes | not yet |
| 3 | Consignment-out | คลังฝากขาย | **yes** — sitting at a partner | yes, by the partner |
| 4 | Consignment-in | คลังรับฝากขาย | **no** — someone else's goods | yes, on their behalf |
| 5 | Returns holding | คลังรับคืน | yes | not until assessed |
| 6 | Work in process / in transit | คลังระหว่างทำ | yes | no |
| 7 | Loaned goods | คลังยืมสินค้า | yes — samples, sponsorship, event loan | no |
| 8 | Damaged / scrap | คลังของเสีย | yes | no |

**The test that generates this list:** for every place a unit can physically be, ask *do I own it* and
*can I sell it this month*. Two different answers mean two different location groups.

**Grain.** The structure is **subsidiary → location → bin**, bins inside one location separated **by
material status** (good, damaged, customer-claim), because one site holds several conditions at once
and netting them overstates availability. The food case goes finer wherever goods perish or volume is
high: **stock at bin-and-lot grain, never warehouse grain**, each balance carrying **four quantity
states — on hand, reserved, committed, available** — available computed live and never negative, bins
carrying a velocity class and a temperature zone (ambient, chilled, frozen) with capacity in weight and
cube. Warehouse-grain inventory is what produces overselling and short picking.

**The location master is governed, not self-service.** Opening a location in the apparel reference
requires the department and customer codes from Accounting, then documentation to Supply Chain, with
automating that flow from the sales side recorded as a gap. Keep the control and automate the paperwork
— location codes carry accounting dimensions, and an ungoverned list becomes unreportable within a year.

## 2. The process set, and the disciplines inside it

| Group | Processes |
|---|---|
| Manage master | manage location · manage location bin |
| Manage receipt | goods receipt |
| Manage transfer | store↔store · warehouse→store · store→warehouse · bin transfer · inventory transfer · transfer order raised by Supply Chain |
| Manage order fulfilment | fulfilment for sales — automatic · fulfilment for sales — manual |
| Inventory adjustment | adjust inventory, increase and decrease |
| Inventory count | via the in-house programme · via standard ERP · via point of sale |
| Inventory replenishment | replenish location by transfer order |

**Transfers always pass through in-transit** — one movement in on approval, a second out on receipt, so
nothing is invisible or double-counted and the gap between them is a measurable lead time.

Three execution disciplines from the food case sit under those processes wherever throughput or
perishability warrants them. **Put-away is directed** on four ranked criteria — zone compatibility
(mandatory, never operator-overridable), velocity class, remaining capacity and first-expired-first-out
— so newer stock never buries an earlier-expiring lot, a full bin proposing an overflow bin in a
compatible zone or else a supervisor override with a logged reason. **Picking is wave-based, driven by
the receiving window rather than readiness** — waves group orders sharing a delivery window, sized to
truck and driver capacity, released **backwards from the customer's cutoff** less lead time, with a zone
lock against collision and a short pick flowing into the in-full measure.
**Allocation is scored and reservation all-or-nothing** — lots chosen on a configurable weighted score
of expiry priority, delivery urgency and proximity, with insufficient availability at commit rejecting
the whole reservation. Every outbound step is scan-validated (bin, item and lot at pick, case at pack,
vehicle before ship), after which the shipment record is immutable.

## 3. Fulfilment and third-party logistics

Where an external provider runs the physical warehouse, the ERP stays the system of record:

```
ERP creates Order Fulfilment (from a SALES ORDER or a TRANSFER ORDER) → provider releases, picks, packs
  → provider confirms back → status progresses to packed / shipped → STOCK RELIEVED, cost of sales
  posted → ship status passed onward to the store or front-end system waiting for it
```

**The same fulfilment mechanism serves sales and transfers** — selling to a customer and replenishing a
shop are one instruction with a different destination, and separating them doubles the integration for
no benefit. **Stock relief happens on the warehouse's confirmation, not the ERP's instruction**, which
keeps the ledger honest when the warehouse is outside the building. **Cross-dock bypasses the
availability pool entirely** — matched inbound goes straight to pack and load without a bin holding it,
a mid-receipt shortage re-computing the outbound allocation. One asymmetry to check early: the food case
runs an owned fleet and warehouse with no external provider or carrier integration at all, while the
apparel case is built around one. Neither is the default.

## 4. Costing — the method and the per-location trap

**Method in the apparel reference: moving average. The decision left open: moving average by subsidiary
or by location?** The concern recorded in that design's own words — with valuation held at subsidiary
level, the **inventory value report by location shows an incorrect cost and amount, while the report by
subsidiary is correct.** The mechanism, worth walking a controller through live:

| Step | What happens | Effect |
|---|---|---|
| 1 | Goods received at the warehouse at the opening cost | subsidiary average equals the opening cost |
| 2 | Units transferred out to a shop | the shop receives them carrying the opening cost |
| 3 | A later receipt arrives at a **different** cost | the subsidiary average moves to a blend of the two |
| 4 | The shop sells its units | they leave **at the blended average, not the cost they arrived with** |

The subsidiary total stays right throughout; the per-location picture does not. If the controller wants
stock value per shop, say plainly that this is a **design decision with a reporting consequence, not a
configuration checkbox** — raising it in discovery earns credibility, discovering it in user acceptance
testing costs a re-design in the least forgiving phase. A **related control the same business asked
for** was quantity and value per location held against a total cost ceiling, locking transfers-in and
receipts when exceeded unless approved; it shipped as a custom programme spanning goods receipt, return,
transfer in, adjustment increase, count increase and cost adjustment increase. Treat any "control stock
value at site level" requirement as bespoke development.

| Method | Fits when | Watch out for |
|---|---|---|
| **Moving average** | many items, frequent receipts at varying cost, no need to trace lots | per-location valuation as above; cost changes ripple retroactively through open positions |
| **Standard cost with variances** | stable manufacturing cost base, variance analysis wanted, a real cost-accounting function | needs disciplined periodic cost rolls and an owner for the variances |
| **First in, first out** | traceability matters, or goods are perishable or seasonal with genuine ageing | more transactional overhead; layer maintenance grows with volume |

Note the category difference: for **fashion and seasonal apparel** the pressure is markdown — a unit
goes **out of season** rather than bad — while for **food** it is expiry, a control problem before it is
a valuation one. Either way, stock needs a defensible way to be written down as it ages.

## 5. Shelf life, FEFO and disposition

This layer has no counterpart in the apparel case and is the strongest contribution of the food and
beverage source. It is a **food-safety control enforced by the system**, not a workflow step.

**FEFO is enforced at four separate points, not once:** at **receipt**, where remaining shelf life is
measured against a per-item threshold — below it an override path needing supervisor approval with a
reason, and already expired on arrival triggering quarantine and a disposition decision rather than
entry to available stock · at **put-away**, where burying an earlier-expiring lot behind a later one is
blocked · at **pick and van load-out**, where scanning a later-expiring lot while an earlier remains is
rejected and the operator **redirected to the correct bin**, an expired lot hard-blocked · at **return
restock**, where a saleable return re-enters under FEFO with lot and expiry or the line cannot close.

**Expired and near-expiry are two different controls with two different powers.** Near-expiry raises a
warning a supervisor may override with a logged reason, multi-stage on per-item thresholds. **Expired is
a hard block no role can override** — the lot is set to blocked-pick automatically, removing it from
allocation, picking and van loading at once.

**Five disposition routes**, each with its own mandatory fields and approval level: return to supplier
(the return authorisation reference) · discounted release (a named customer restriction) · donation (a
named recipient) · destruction (manager authorisation, photographic evidence, a write-off posting) ·
repack (target item, lot, new expiry). All five need a photograph, a named authoriser, a reason and a
timestamp, and partial disposition of a lot is supported, leaving the balance in its prior state.

**Returns are classified twice** — by reason (unsold, damaged, expired, near-expiry) and by condition
after inspection (saleable, scrap, recall) — the condition setting the exit: saleable restocked under
FEFO, scrap or expired needing approval and evidence before the loss is booked, recall blocking restock
and opening lot traceability. A credit note is a separate flag with its own amount, because a physical
return and a financial credit are not the same event. And short-dated stock accepted inbound becomes a
customer rejection and then a deduction, so **shelf life at receipt is an input to 10**, not only to the
warehouse.

## 6. Counting, analytics and availability

**Three count mechanisms coexist** in the apparel case because three populations count — warehouse
staff, store staff, the merchandiser network. The food case shows the discipline underneath: **cycle
counting replaces the annual full count**, scheduled by velocity class into low-activity windows so
counts do not collide with running waves; counting is **blind**, the system quantity hidden to remove
bias; accuracy is measured against a per-class tolerance band, investigation opens only on a breach, and
while open **the lot or bin is held**. Counter, adjustment creator and approver are three people.

**Two analytics were built as customisations** in the apparel reference, both category-defining for a
seasonal brand: an **inventory ageing report** by age band, and a **fast-moving, slow-moving and
dead-stock report** by movement class. **Do not assume these are standard** — a buying team that cannot
see ageing and movement class cannot mark down on time. Raise sell-through, weeks of supply, stock turn
and the share of stock older than a season as questions, never as figures.

**Omni-channel stock — one pool or allocated?** A **single pool with live availability** gives the
highest accuracy at the highest integration load and is exposed to latency at peak trading; **allocation
by location or channel buffer** is simpler and resilient, at the cost of reserved stock that may not
sell. The apparel reference allocates **by location**, checking stock plus reserves at order creation.
Either way, make it an explicit decision with a named owner and agree what happens on an oversell.

## 7. Functions the system must provide (effort concentrates in 2, 5, 6, 8, 9, 12, 13 and 14)

| # | Function | Why it is needed | Typically standard or custom |
|---|---|---|---|
| 1 | Location groups distinguishing **owned versus not owned** and **sellable versus not sellable**, over three levels **subsidiary → location → bin** with bins carrying material status | availability is otherwise unanswerable; consigned and subcontracted stock is mis-stated, and one site holds good, damaged and claim stock at once | standard master data, custom grouping attribute |
| 2 | **Bin-and-lot grain with four quantity states** — on hand, reserved, committed, available | warehouse-grain stock is what causes overselling and short picking | standard in warehouse-grade products, custom elsewhere |
| 3 | Governed location master with accounting dimensions attached | ungoverned location codes make the ledger unreportable | standard, plus workflow |
| 4 | **In-transit as a mandatory leg** of every inter-site transfer | nothing invisible, nothing double-counted, lead time measurable | standard |
| 5 | **Directed put-away** on ranked criteria, zone rules not operator-overridable | prevents FEFO burial and temperature breaches | warehouse module or custom |
| 6 | **Wave picking released backwards from the receiving cutoff** with a zone lock, and **weighted lot allocation with atomic reservation** | missing the customer's window is a deduction, not an inconvenience; partial over-commitment is how one lot gets promised twice | specialist capability |
| 7 | One fulfilment mechanism serving **both sales orders and transfer orders**, with stock relieved on the warehouse's confirmation | halves the integration, and keeps the ledger honest when the warehouse is outside the building | standard, needs deliberate design |
| 8 | **FEFO enforced at receipt, put-away, pick and return restock** | one enforcement point is evaded by the other three | specialist or custom |
| 9 | **Expired as an unoverridable block, near-expiry as an approvable warning** | two different powers that must not be built as one rule | custom in most estates |
| 10 | **Disposition routes with mandatory evidence** and a write-off posting, fed by **returns classified by reason and by condition** | the loss must be authorised and attributable, and restock, scrap and recall are three different obligations | part custom |
| 11 | Costing method with the **valuation grain decided explicitly** | per-location value is a design decision, not a checkbox | standard method, custom reporting |
| 12 | Stock **value or quantity ceiling per location** with approval to exceed | asked for routinely; not a configuration option | custom |
| 13 | **Blind cycle counting** by velocity class with tolerance-gated investigation and a hold while open, alongside **several counting mechanisms for several populations** | an unsettled count must not feed the next wave, and warehouse, store and field staff will not adopt one tool | specialist or custom |
| 14 | **Ageing and movement-class reporting** | markdown timing depends on it entirely | custom in both references |
| 15 | An explicit **omni-channel availability rule** — single pool or allocated | otherwise it is decided by accident, one interface at a time | design decision |


## 8. Challenges, gaps and improvement areas

| What commonly goes wrong | What the reference implementations did | What a better design looks like |
|---|---|---|
| **Locations modelled as physical sites only**, so transformed and consigned stock drops out of view | eight functional groups driven by ownership and sellability, each still owned and still counted | run the two-question test on every place a unit can be, before any master data is built, and never let "not sellable" be represented by absence from the system |
| **Stock held at warehouse grain** | the food case holds bin-and-lot with four quantity states; the apparel case rarely goes below location | hold the grain the category needs — lot grain is not optional where goods expire |
| **Per-location valuation assumed free, and FEFO treated as a picking preference** | valuation grain recorded as an open decision with a known reporting defect; FEFO enforced at four points with expired unoverridable | decide the valuation grain at design time and say what that grain cannot report; build FEFO as a control with a stated power at each point, and decide who may override which |
| **Ageing and dead stock assumed standard, and counting designed for one population** | both reports were customisations; three count mechanisms coexist deliberately | price ageing and movement class as line items — they are where seasonal margin is lost — and match the counting tool to who counts, behind one adjustment path |
| **External logistics assumed either way, and oversell handled by hope** | one case is built around a provider and the other has none; allocation by location with a check at order creation | ask who runs the warehouse, because it changes the estate and the stock-relief design; and make the availability rule explicit before go-live |

## 9. Discovery questions

1. Where can a unit of your stock physically be, and in each place — **do you own it, and can you sell it?** ⚑ *changes the estimate materially*
2. Who runs your warehouse — you or a third party? Whose system is the record of stock? ⚑
3. Do your goods carry a lot number and an expiry date, and when short-dated stock is rejected by a customer, where does that loss land today? ⚑
4. If a lot is near expiry, who may release it — and once it has passed expiry, is anyone allowed to? *(the answer to the second half should be nobody)*
5. What costing method do you use, and **does anyone rely on stock value per site?** ⚑
6. How do you decide when to mark down, on what data — and who counts, how often, with what tool?
7. What stops two channels selling the same unit? When goods come back, who decides whether they are saleable, and what share never returns to sellable stock?
8. **Do you import any raw material duty-free under an investment-promotion certificate?** ⚑ — if yes, the location and valuation design changes before it is fixed, not after. See the section below and file **18**

## Duty-exempt stock under an investment-promotion certificate

> Triggered by discovery question 8 above.

If the client holds a promotion certificate covering imported raw material, **the duty status is a
property of the stock, not a report filter**. Duty-exempt and duty-paid material of the same item
**may not share one valuation layer** — commingling has to be impossible, not merely visible. The
quantity held is also capped against an approved maximum, and consumption is tested against an
approved formula; breaching either raises a **back-duty (จ่ายอากรย้อนหลัง)** exposure that belongs in
the accounts before filing, not after an audit.

This changes the location and valuation design set out above, so establish it **before** fixing the
topology. Full treatment in file **18**.

## Related files

- **03** consignment — the consignment location groups and the dual-book question · **04** van sales —
  stock in one person's custody overnight, and FEFO at load-out
- **05** owned store and point of sale — store replenishment, in-transit and store counts · **10** trade
  spend and Net GP — where a short-dated rejection becomes a deduction
- **12** make and transform — the outside-processing location and how its cost is set · **14** procure
  to pay — the quarantine, claim and supplier-return bins, and landed cost at receipt
- **15** accounting and assets — how movements post to the ledger · **16** the application estate — the
  warehouse and point-of-sale touchpoints
- **18** BOI and incentives — duty-exempt stock segregation in the valuation layer
- **19** the full discovery bank
