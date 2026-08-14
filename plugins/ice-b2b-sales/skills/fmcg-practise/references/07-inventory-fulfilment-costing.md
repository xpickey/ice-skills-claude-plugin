# 07 — Inventory, fulfilment and costing: the backbone every channel shares

> Load this when warehouse structure, stock locations, third-party logistics, fulfilment,
> costing method, stock valuation, or inventory analytics are in scope.
> This is the file that makes multi-channel selling work; every channel file above depends on it.

## Location topology — eight functional groups, not two

The instinct is to model warehouses and shops. The reference implementation controls locations by
**eight functional groups**, and each exists because stock in it behaves differently in the
accounts:

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

**The test that generates this list:** for every place a unit can physically be, ask *do I own it*
and *can I sell it this month*. Two different answers mean two different location groups. A
prospect that models only physical sites cannot answer "how much of my inventory is actually
sellable" — which is the question their controller asks every month.

### Three levels, and bins carry status

The structure is **Subsidiary → Location → Bin**. Bins inside one location are separated **by
material status** — good goods, damaged goods, customer-claim goods. This matters because a store
or a returns location holds units in several conditions at once, and netting them together
overstates availability.

### Location master is governed, not self-service

Creating a location in the reference implementation requires the requester to obtain the
department and customer codes from Accounting first, then submit documentation to Supply Chain,
which opens the location. A gap was recorded for automating the flow of location-master data from
the sales-channel side to Accounting.

**Why the governance exists:** location codes carry accounting dimensions. An ungoverned location
list becomes an unreportable general ledger within a year. Keep the control; automate the paperwork.

## The inventory process set

| Group | Processes |
|---|---|
| Manage master | manage location · manage location bin |
| Manage receipt | goods receipt |
| Manage transfer | store↔store · warehouse→store · store→warehouse · bin transfer · inventory transfer · transfer order raised by Supply Chain |
| Manage order fulfilment | fulfilment for sales — automatic · fulfilment for sales — manual |
| Inventory adjustment | adjust inventory, increase and decrease |
| Inventory count | via the in-house programme · via standard ERP · via point of sale |
| Inventory replenishment | replenish location by transfer order |

**Transfers always pass through in-transit.** On approval the system creates an inventory transfer
into the in-transit location; on receipt a second transfer moves it to the destination. Nothing is
invisible, nothing is double-counted, and the gap between the two movements is a measurable
delivery lead time.

**Three count mechanisms coexist** because three populations count — warehouse staff, store staff
and the merchandiser network. Forcing one mechanism on all three is a common adoption failure.

## Fulfilment and third-party logistics

Where a 3PL runs the physical warehouse, the ERP stays the system of record and the 3PL is driven
by integration:

```
ERP creates Order Fulfilment (from a SALES ORDER or a TRANSFER ORDER)
  → sent to the 3PL to release the goods
  → 3PL picks, packs
  → 3PL confirms back to the ERP → status progresses to packed / shipped
  → stock relieved, cost of sales posted
  → ship status passed onward to the store or front-end system that is waiting for it
```

Two points worth carrying:

- **The same fulfilment mechanism serves sales and transfers.** Selling to a customer and
  replenishing a shop are the same warehouse instruction with a different destination. Designing
  them separately doubles the integration for no benefit.
- **Stock relief happens on the warehouse's confirmation, not on the ERP's instruction.** The
  physical event drives the accounting event. This is what keeps the stock ledger honest when the
  warehouse is outside the building.

## Costing — the decision and the honest gotcha

**Method in the reference implementation: moving average.**

**The open decision recorded in the design: moving average by Subsidiary, or by Location?**

**The recorded concern, in the design's own words:** with valuation held at subsidiary level, the
**inventory value report by Location shows an incorrect cost and amount, while the report by
Subsidiary is correct.**

The worked example is simple and worth reproducing in a discovery conversation:

| Date | Transaction | Qty | Cost | Amount |
|---|---|---|---|---|
| 1 Oct | Goods received at the warehouse | 10 | 10 | 100 |
| 5 Oct | Transferred out to the shop | 10 | 10 | 100 |
| 10 Oct | Goods received at the warehouse | 10 | 12 | 120 |

| Date | Transaction (at the shop) | Qty | Cost | Amount |
|---|---|---|---|---|
| 5 Oct | Transferred in | 10 | 10 | 100 |
| 15 Oct | Picked and sold | 10 | **11** | **110** |

The shop received units at 10, but the second receipt at 12 moved the subsidiary-level average to
11 — so the units leave the shop valued at 11, not the 10 they arrived at. The subsidiary total
stays right; the per-location picture does not.

**What to do with this in pre-sales.** If the customer's controller wants stock value per shop,
say plainly that this is a design decision with a reporting consequence, not a configuration
checkbox. Raising it in discovery earns credibility. Discovering it in user acceptance testing
costs the project a re-design in its least forgiving phase.

### A related control the business asked for

The reference customer asked the system to **control quantity and value per location against a
total cost ceiling**, locking transfers-in and receipts when exceeded unless approval is obtained.
This shipped as a custom programme covering goods receipt, goods return, inventory transfer in,
inventory adjustment increase, inventory count increase and inventory cost adjustment increase.

That is a reasonable ask and a real customisation. Treat any "control stock value at site level"
requirement as bespoke development until proven otherwise.

## Choosing a costing method — practitioner view

| Method | Fits when | Watch out for |
|---|---|---|
| **Moving average** | many SKUs, frequent receipts at varying cost, no need to trace individual lots | per-location valuation accuracy, as above; cost changes ripple retroactively through open positions |
| **Standard cost with variances** | stable manufacturing cost base, variance analysis is wanted, strong cost-accounting function | needs disciplined periodic cost rolls and someone to own the variances |
| **First in, first out** | traceability matters, or the goods are perishable or seasonal with real ageing | more transactional overhead; layer maintenance grows with volume |

For fashion and seasonal apparel specifically, the pressure is markdown rather than spoilage: a
unit does not go bad, it goes **out of season**, and its recoverable value falls on a calendar.
Whatever method is chosen, the customer needs a defensible way to write stock down as it ages.

## Inventory analytics the business actually needed

Two reports were built as customisations in the reference implementation, and both are
category-defining rather than optional for a seasonal consumer brand:

- **Inventory ageing report** — stock by age band
- **SKU fast-moving, slow-moving and dead-stock report** — movement classification

**Do not assume these are standard.** Aged and dead stock is where the margin of a seasonal
apparel business goes. If a prospect's buying team cannot see ageing and movement class, they
cannot markdown on time. Put both in scope explicitly.

Useful measures to raise in discovery, phrased as questions rather than promised numbers:
sell-through rate by collection, weeks of supply, stock turn, gross margin return on inventory
investment, and the proportion of stock older than one season.

## Omni-channel stock — one pool or allocated?

Every channel draws on the same units. Two strategies, both legitimate:

- **Single pool with live availability** — highest accuracy, highest integration load, exposed to
  latency at peak trading.
- **Allocation by location or channel buffer** — simpler and resilient; the cost is reserved stock
  that may not sell.

The reference implementation allocates **by location**, and checks stock plus reserves against the
sales order at creation. Whichever a prospect chooses, make it an explicit decision with a named
owner, and agree in advance what happens when an oversell occurs — because at volume, one will.

## Scoping signals

Raise the estimate when you see:
- Per-location or per-shop inventory valuation as a firm requirement
- A 3PL, especially more than one, or a 3PL with a fixed API you must meet
- Consignment in either direction — it adds location groups and count obligations
- Stock-value ceilings or approval-gated receipts
- Ageing, movement class or markdown reporting expected as standard
- Several counting populations with different tools

## Discovery questions

1. Where can a unit of your stock physically be, and in each place — do you own it, and can you sell it?
2. Who runs your warehouse — you or a third party? Whose system is the record?
3. What costing method do you use today, and does anyone rely on stock value per site?
4. How do you decide when to mark down, and what data do you use?
5. Who counts, how often, and what do you do with the variance?
6. What stops two channels selling the same unit?

## Related files

- **04** consignment locations and the dual-book question
- **06** store replenishment, in-transit and store counts
- **08** transformation stock and how its cost is set
- **10** how inventory posts to the general ledger
- **11** the warehouse and point-of-sale integration touchpoints
- **12** costing and inventory gaps versus common practice
