# 04 — Van sales and direct store delivery (ขายบนรถ / รถเร่)

> **Load this when:** the prospect's own vehicles carry stock and sell from it · the words "รถเร่",
> "van sales", "direct store delivery", "DSD", "เคลียร์ของเคลียร์เงิน" or "พนักงานขายหน่วยรถ" appear ·
> reps collect cash at the shop · the customer base is thousands of small independent outlets that no
> central ordering system reaches.
> **Do not load this for:** ordinary outright selling to dealers and independent shops where the goods
> are delivered from a warehouse against an order taken earlier → that is **01 Traditional trade**.
> Van sales is a delivery-and-settlement model layered on top of that customer base, not a different
> customer base.
> **Source basis:** one reference implementation — a Thai food and beverage manufacturer and
> distributor, from its functional specification for logistics, warehouse management and van sales.
> **Treat the van detail as design intent, not as verified running practice:** the five van screens in
> that specification passed screen-level writing but never passed second-pass quality assurance, and
> their internal cross-references disagree with one another. The process narrative is consistent; it
> has been through neither review nor an observed live operation. Material tagged **[general practice
> knowledge]** is added here and comes from neither reference implementation.

## 1. Use cases — what this channel actually is

Van sales is **direct store delivery to traditional trade**: a rep drives a loaded vehicle along a
published route, sells from what is on the van, hands the goods over on the spot, takes the money or
extends credit against the outlet's limit, and settles both stock and cash at the end of the shift.
The action on the rep's screen in the reference design is literally *deliver and collect* — one
event, one visit.

The three defining facts, which are what separate this from every other channel:

- **Tax point** — the sale happens at the point of sale on the vehicle, so the document is due there.
  **How that document is actually issued is the open question of this chapter — see §5 and question 1.**
- **Who the debtor is** — the outlet, where credit is extended; otherwise nobody, because the money is
  collected in the same visit.
- **Who owns unsold stock** — the brand. Stock on the van is the brand's inventory sitting outside the
  distribution centre in one person's custody overnight. The reference design calls it **off-DC
  stock** and gives it its own audit regime.

**The recognisable situation.** A manufacturer sells through organised retail centrally, and separately
reaches several thousand small independent shops that will never place an order through a portal. Those
shops buy in small quantities, often several times a week, frequently in cash, and expect the goods to
arrive on the same visit the order is placed. A van fleet is the only economic way to serve them.

**The structural requirement that comes with it.** In the reference design the van lane must be kept
**structurally separate from the modern trade lane** — not run as a variant of it — enforced downstream
as a hard block: van receivable may not be merged with modern trade receivable. Modern trade receivable
is dominated by deductions and disputes (file **10**); van receivable is dominated by small balances
against many small shops with a limit each. Merging them destroys both collections and dispute handling.

### Two route models — the source covers only one

| Model | Thai | What happens | In the source? |
|---|---|---|---|
| **Cash van / sell from stock** | ขายสด บนรถ | stock, money and document settle in a single visit; assortment is capped by what fits on the vehicle | **yes — this is the whole of the reference design** |
| **Pre-sales, deliver later** | รับออร์เดอร์ก่อน ส่งทีหลัง | an order call captures the order, a later delivery call fulfils it | **not described anywhere** |

The nearest thing the source has to pre-sales is the **standing order** (ลูกค้าประจำ), used as one of
two demand inputs when sizing the morning load, alongside the outlet-level forecast. A standing order
sizes the load; it is not an order captured on a previous visit and fulfilled on a later one.

**[general practice knowledge]** The commercial difference matters at scoping. A cash van settles
everything in one touch but is limited to what the vehicle carries. Pre-sales raises effective
assortment and lets the load be built against real orders, but costs a second visit and loosens
settlement discipline, because the money, the goods and the document no longer arrive together. **A
customer running both needs two route calendars, two stock-ownership rules and two revenue-recognition
points.** Establish which one — or both — before estimating. See question 2.

## 2. Process — the flow

```
MORNING, AT THE DISTRIBUTION CENTRE
  load calculated per route from forecast + standing orders → proposed quantity per SKU
  → stock drawn under first-expired-first-out, lot and expiry validated
     · scanning a later-expiry lot while an earlier one remains → REJECTED, operator redirected
     · already-expired lot → HARD BLOCK, no role may override
  → load validated against vehicle weight, cube, pallet count and temperature zone
  → CONFIRM LOAD-OUT: load locks · VAN INVENTORY created (on-van = loaded) · load-out sheet prints

ON ROUTE — offline-first, not offline-tolerant
  visit outlets in the published stop sequence
  → order captured on the mobile device, van stock decremented in real time
     · quantity ordered above quantity on van → hard stop
     · outlet balance + order value above limit, or overdue ageing breached → BLOCKED
       (manager waiver possible, reason code logged, the driver may never self-approve)
  → payment taken — cash · mobile transfer · card · cheque — or credit extended
  → STOP CANNOT CLOSE until signature, condition photograph, note, arrival and departure
    timestamps, GPS and delivered quantity are all captured; evidence LOCKS on sync
  → orders queue as pending-sync and auto-sync on reconnect
     · van stock no longer matches on sync → CONFLICT-HOLD, supervisor only
  → [conditional] actual sell-in diverges from forecast beyond tolerance → rep raises a
    recalibration → manager approves → inventory adjustment created, DC notified for the next
    round, actual sell-in returned to demand planning

END OF SHIFT — two closes on one record set
  MONEY:  opening float + collections by method − change given = expected closing cash
          compared against counted cash · variance reason-coded
          electronic collections are pulled from the gateway and cannot be typed
  STOCK:  loaded − sold + returned = expected on van
          compared against counted on van, per SKU AND PER LOT
  → maker (driver) submits → checker (supervisor or cashier) verifies → finance posts
  → POSTING TO THE LEDGER IS DELAYED ONE TO TWO DAYS BY DESIGN
  → posted reconciliation is immutable; a correction is a new adjustment, never an edit
```

**Three details in that close carry most of the control value.** The posting delay is not an
operational inefficiency but a designed window for duplicate and fraud detection before entries become
immutable — say so when a client asks why the van cannot post same-day. Electronic collections are
pulled from the gateway and cannot be typed, so only cash and cheque are counted by hand, which is what
stops fabricated cash. And the equation names **change given** as a subtraction, the line most often
missing from a home-grown settlement sheet, whose absence makes every close look short by the float.

**Where FEFO touches the van.** Two points only — the load-out draw, and the restock of a saleable
return. The wider shelf-life control layer (receipt, put-away, near-expiry alerting, quarantine,
disposition routes) belongs to file **11** and is not repeated here.

## 3. Functions the system must provide

| # | Function | Why it is needed | Typically standard or custom |
|---|---|---|---|
| 1 | **Van inventory as its own record**, keyed by vehicle + SKU + **lot**, carrying on-van, sold and returned quantities | stock in one person's custody overnight is not a warehouse bin and cannot be audited like one | usually custom, or a specialised add-on |
| 2 | Load calculation per route from **forecast plus standing orders** | the load is the single biggest determinant of a productive day | custom or planning-module function |
| 3 | **FEFO enforcement at load-out** — later-expiry lot rejected with redirection to the correct bin; expired lot hard-blocked | food safety; the block must not be waivable by any role | standard in WMS-grade products, custom elsewhere |
| 4 | Load validated against **vehicle weight, cube, pallet count and temperature zone** | a load that does not fit is discovered at the dock, not on the road | custom |
| 5 | **Offline-first order capture** with a pending-sync queue and full function without a signal | connectivity cannot be assumed on a route | specialised mobile product |
| 6 | **Conflict-hold state** when a sync finds van stock no longer matches, clearable only by a supervisor | the tell that dead zones and concurrent adjustment are real, not occasional lag | part of the mobile product |
| 7 | Real-time decrement of van stock with a **hard stop above quantity on van** | prevents selling units that are not on the vehicle | part of the mobile product |
| 8 | **Credit check at order capture**, not at invoicing — balance plus order value against limit, and overdue ageing | by invoicing time the goods are already in the shop | standard check, custom placement |
| 9 | Manager waiver with **mandatory reason code, logged, no self-approval by the driver** | the single most abusable point in the channel | standard workflow, deliberate design |
| 10 | **Proof of delivery as a completion gate** — signature, condition photograph, note, arrival and departure timestamps, GPS, delivered quantity — **locked on sync** | a stop that closes without evidence cannot be defended later, and evidence that stays editable is not evidence | specialised mobile product |
| 11 | **Geofenced check-in** against the published route, with supervisor override | counters claimed visits that never happened | part of the mobile product |
| 12 | **Cash reconciliation** on the explicit equation, including change given | the arithmetic every home-grown sheet gets wrong | custom |
| 13 | **Electronic collections pulled from the gateway, read-only** to the person closing | prevents fabricated cash | integration build |
| 14 | **Stock reconciliation per SKU and per lot** at shift close | a variance must be attributable to a lot, not merely to a SKU | custom |
| 15 | **Segregation of duties enforced as blocking rules** — maker ≠ checker, checker ≠ poster | the whole control model rests on this | standard, must be configured deliberately |
| 16 | **Parameterised variance thresholds** — cash variance blocks posting; off-DC variance opens an investigation | the mechanism is designable; the numbers are the client's | custom |
| 17 | **Driver-level variance history** held as a standing attribute on the driver master | a pattern across shifts is the real signal, not any single shift | custom |
| 18 | **Rolling off-DC stock audit** of vehicles on a short cycle, separate from the warehouse cycle count | surprise counting is what makes custody real | custom |
| 19 | **Deliberate delay of the ledger posting**, then immutability | the fraud-detection window | configuration plus discipline |
| 20 | **Route optimisation** from outlet coordinates, operating hours, visit frequency, vehicle capacity and driver shift limit | a manual route plan does not survive a growing outlet base | specialised engine, usually a separate product |
| 21 | **Local travel-time adjustment** — congestion and flood season | a plan built on free-flow travel times fails from the first day | configuration inside the routing engine |
| 22 | **Publishing a route freezes the on-time baseline and arms the geofence** | on-time measurement needs a baseline nobody can move afterwards | custom |
| 23 | **Outlet identity governed by pinned GPS and tax registration number** — free-text address rejected, duplicate registration blocked | a fragmented customer base fills with duplicates and fictitious outlets otherwise | custom |
| 24 | Separation between **whoever pins the outlet and whoever sets its credit limit** | stops one pair of hands creating a fictitious outlet complete with a credit line | standard workflow, deliberate design |
| 25 | **Return capture on the van**, classified by reason, feeding the shift-close stock equation | a return changes the expected count that night | custom |
| 26 | **Return rate monitored per outlet and per driver** against a threshold | a high return rate is a behaviour signal about the route, not only a stock movement | reporting, custom |
| 27 | Van receivable held **separately from modern trade receivable**, enforced | merging them destroys both collections and dispute handling | configuration, enforced as a hard block |

Rows 1, 5, 12, 14, 18, 20 and 23 are where the effort concentrates, and rows 5, 6, 10 and 11 usually
mean a specialised field-sales product rather than the core ERP. The last column describes mainstream
capability in this category, not any one product's behaviour; verify against what is on the table.

## 4. Integration touchpoints

| Touchpoint | Direction | Mode | What it carries |
|---|---|---|---|
| Forecast and standing orders | planning → load calculation | batch, daily | expected demand per SKU per route |
| Load-out confirmation | load-out → van inventory | synchronous | vehicle, SKU, lot, expiry, quantity |
| Product, price and scheme catalogue | ERP → mobile device | batch, with offline cache | sellable SKUs, current price, running schemes |
| Outlet master and credit position | ERP → mobile device | batch, refreshed per shift | outlet, limit remaining, overdue flag |
| Order and delivery capture | mobile device → ERP | **asynchronous, queued offline** | order lines, payment method, evidence pack, GPS |
| Payment gateway collections | gateway → reconciliation | asynchronous, read-only into the close | electronic collection totals per shift |
| Actual sell-in and variance | van → planning | batch, daily | what actually sold, against what was forecast |
| Returns brought back | van → warehouse receipt | asynchronous | quantity, lot, reason |
| Shift close posting | reconciliation → ledger | batch, **deliberately delayed** | cash, variance, stock adjustment, by legal entity |
| Route plan and geofence | routing engine → mobile device | batch, on publish | stop sequence, expected arrival, geofence |

**The connection that is absent from the source, and worth naming:** there is no third-party logistics
provider, no carrier integration and no outsourced warehouse anywhere in this design. The fleet is
owned, with vehicle and driver masters carrying capacity profiles and shift limits. Wherever a prospect
uses a third party for any part of the van operation, that is unmapped ground — see question 9.

## 5. Challenges, gaps and improvement areas

| What commonly goes wrong | What the reference implementation did | What a better design looks like |
|---|---|---|
| **How the tax document is issued on the van is undefined** | the specification covers the evidence pack in full, states that tax sits at invoice level, and **says nothing about where the van's invoice number comes from, how the sequence is controlled per vehicle, or how a sale made offline receives a compliant document**. The electronic tax document reference appears only on the modern trade screen | **unknown from this source, and it must not be guessed.** It is the first question a Thai client asks. Establish the answer with the client and their tax advisor before any estimate — see question 1 and file **17** |
| **Cash and stock leaking off the vehicle** | named outright as the purpose of the shift-close design — close the cash and stock leak before entries reach the ledger | treat the van as a small warehouse with weak physical security and one accountable person: lot-level counting, a rolling surprise audit, and a variance history held against the person |
| **Driver and outlet collusion** — a quantity reported sold materially above what the shop received | modelled as a designed-for scenario, countered by delivered quantity captured at the stop with signature and photograph, then matched at close | keep the evidence at the stop, not at the close; a variance discovered at close with no stop-level evidence cannot be resolved |
| **Fabricated cash** | electronic collections pulled from the gateway and made read-only; only cash and cheque are counted and keyed | the same rule everywhere a person keys a number a machine already knows |
| **Duplicate and same-day fraudulent postings** | ledger posting deliberately delayed, then made immutable, with corrections as new adjustments | keep the delay in the design and explain it as a control; clients read it as slowness unless told |
| **Reps claiming visits they did not make** | geofenced check-in with supervisor override | pair the geofence with the published route so the baseline and the fence come from one act |
| **Evidence edited after the fact** | proof of delivery locked on sync | lock on sync rather than on approval — the gap between the two is where edits happen |
| **The van empties mid-route in a promotional week** | mid-route recalibration: rep raises, manager approves, adjustment created, DC notified, actual sell-in returned to planning | good as far as it goes; the deeper fix is the forecast, and it only improves if actuals return to planning — file **13** |
| **Zero-sales visits are invisible** | proof of delivery records completed, partial and failed with reason codes for outlet closed, refused and damaged — which captures a **failed delivery**. **There is no concept of a productive-call rate, a strike rate, or a visit where the shop was open and no order was placed** | for a van operation the productive-call rate is a primary performance measure. Design the zero-sales visit as a first-class record from the start — see question 7 |
| **Travel time treated as a constant** | congestion and flood season carried as explicit adjustment factors in the routing engine | keep them as configuration, not as a fudge in the stop count |
| **A fragmented outlet base fills with duplicates** | identity by pinned GPS and tax registration number, duplicate registration blocked outright, near-duplicate location warned, creation separated from credit granting | adopt this whole; it is the cheapest control in the chapter |
| **Van receivable merged into modern trade receivable** | enforced as a hard block | keep them apart from the first design, not after the first collections cycle fails |
| **Returns brought back and forgotten**, and a physical return assumed to be the same event as a financial credit | quantity returned is a field on van inventory and part of the shift-close equation, while the credit note to the outlet is a separate flag with its own amount; classification and disposition happen downstream at the DC | keep the halves distinct — the van owns what came back and how it changes tonight's count, the credit is its own decision, and disposition of the stock belongs to file **11** |
| **Every threshold in this chapter** | all of them are declared illustrative by the source's own authors — geofence radius, cash variance limit, van stock variance, driver variance, return-rate trigger, forecast divergence tolerance | **the mechanism is designed; the numbers are placeholders.** Ask the client. Never quote a figure |

## 6. Discovery questions

1. **When a rep sells at the shop, what document does the shopkeeper receive, and where does its number
   come from?** Is it printed on the vehicle, taken from a pre-numbered book, or raised afterwards at
   the depot — and what happens when the sale is made with no signal? ⚑ *changes the estimate
   materially, and this practice has no reference answer for it*
2. Do your reps sell from the van, take orders for later delivery, or both? ⚑ *both means two route
   calendars and two revenue-recognition points*
3. How is the morning load decided today, who decides it, and what happens when a shop wants more than
   the van is carrying?
4. How does a rep know an outlet is over its limit or overdue — at the shop, or afterwards? ⚑
5. Walk me through the end of a shift. Who counts the stock, who counts the cash, who checks them, and
   who posts them? ⚑ *this one question exposes the whole control model*
6. How soon after the shift do the numbers reach your accounts, and is that deliberate?
7. How do you know whether a rep called on a shop and made no sale? ⚑ *usually absent, and it is the
   channel's primary performance measure*
8. Do you count stock on the vehicles unannounced, and how often?
9. Is any part of the operation run by a third party — the vehicles, the drivers, the depot? ⚑ *the
   reference design assumes an owned fleet throughout*
10. Do your goods carry an expiry date, and does a rep ever bring expired stock back? *(opens file 11)*
11. When a shop returns goods to the rep, does the money always go back too, or sometimes only the
    goods?
12. How are routes planned today, and how often does the plan survive contact with the traffic?
13. How is a new shop opened as a customer, and who sets its credit limit? ⚑
14. Is van credit collected by the same people who chase your retail customers? *(if yes, expect the
    collections process to be carrying two incompatible jobs — see file 10)*

## Related files

- **00** channel map and the classification method
- **01** traditional trade — the same customer base served through a warehouse rather than a van
- **10** trade spend and Net GP — the deduction domain that van receivable must stay clear of
- **11** inventory, locations and costing — bin and lot discipline, shelf-life control, FEFO across the
  estate, returns disposition
- **13** demand planning — where actual sell-in returns and improves the next load
- **16** the application estate — where a field-sales product and a routing engine sit alongside the ERP
- **17** Thailand compliance — tax documents, electronic tax documents, and the unanswered question above
- **19** the full discovery bank
