# 06 — Owned store and point of sale

> Load this when the brand runs its own shops, counters, outlet stores, staff sales,
> or event points of sale, and the point-of-sale system has to meet the ERP.

## The design principle: the day, not the transaction

An owned-store estate could post every transaction to the ERP in real time. The reference
implementation deliberately does not. It posts **a daily revenue summary per shop**, and it is
right to do so.

Reasons that generalise:
- A store does hundreds of small transactions; the general ledger needs the day, not the line.
- The point-of-sale system is the operational system of record for the shop floor; the ERP is the
  financial system of record. Each keeps the grain it needs.
- Day-end is when the shop reconciles cash anyway, so it is the natural posting boundary.

Real-time posting is appropriate for the things that must not wait — **stock requests** and
**stock adjustments** — and those are integrated separately and synchronously.

## What the daily posting actually does

At close of day the point-of-sale system sends the revenue summary, and the ERP:

1. **Creates the AR invoice per shop**, posting `Dr AR-Shop / Cr Revenue / Cr Output Tax`.
2. Posts the cost side: `Dr Cost of Goods Sold / Cr Inventory`.
3. **Accepts the customer payment**, splitting receipts by **payment type (receipt method)** — cash,
   card, transfer, wallet — so the shop's takings reconcile to the bank by tender type.
4. On settlement, clears `Dr Bank / Cr AR-Shop`.

The shop sends its daily sales report and tax report to Accounting for the cash reconciliation.

### The tax-invoice split — the detail everyone misses

The posting is **not** one invoice per shop. It splits:

- **Customers who requested a tax invoice** → an invoice each, in that customer's name, with
  receipts recorded per customer and per payment type.
- **Customers who did not** → aggregated into **one summary customer**, one invoice, receipts
  grouped by payment type.

This single rule is what keeps a consumer retail estate's receivable sub-ledger usable in
Thailand. Design it in; do not treat it as a reporting afterthought.

## Store stock movements — the four integrations

| Movement | Direction | Mode | What it does |
|---|---|---|---|
| **Stock request** | store → ERP | real-time | store raises a replenishment request; the ERP creates a **Transfer Order**; Supply Chain reviews and approves before despatch |
| **Stock response** | ERP → store | real-time | the ERP answers what is available and what is coming |
| **Stock adjustment** | store → ERP | real-time | inventory adjustment, increase or decrease — damage, loss, found stock, count correction |
| **Ship-status sync** | ERP → store | real-time | passes the fulfilment shipped status through so the store can book the goods in |

Two design points worth carrying:

**1. Account mapping is driven by the sale channel, not chosen by the operator.** On every inbound
adjustment the adjustment account, department and class are **derived from the sale channel** on the
message. This is how a business with many channels keeps its general ledger analysable without
asking shop staff to understand accounting. Adopt this pattern wherever front-line systems post to
the ledger.

**2. Replenishment moves through in-transit.** A transfer from warehouse to shop creates an
inventory transfer into an **in-transit location** on despatch, and a second transfer from
in-transit into the shop on receipt. Stock is never invisible and never double-counted, and the
difference between the two is a measurable delivery gap.

## Credit notes and returns at the counter

A store return needs its own integration — a **credit memo raised from the point-of-sale** — because
the shopper is standing at the counter and the refund happens immediately, before any back-office
approval could realistically run. Two consequences:

- The store-level credit memo needs its own control (who can authorise, up to what value, with what
  reason code) since the usual approval chain is bypassed by necessity.
- The returned unit's condition determines whether it goes back to sellable stock or into a returns
  or damaged location. Bins within a store location are separated by material status precisely for
  this.

## Employee sales and event sales

Two related channels ride on the same point-of-sale route:

- **Employee sales** — priced differently, sometimes payroll-deducted, and needing their own
  reporting for tax and benefit purposes. Same mechanism, different customer group and price basis.
- **Event and pop-up sales** — a temporary point of sale. Where the goods move to the event site
  ahead of selling, the **consignment true/pseudo tax-point question returns** (see file 04),
  because stock is now sitting somewhere the brand does not permanently control.

## Known constraints from the reference implementation

Two limitations were recorded openly in the design, and they are honest examples of what a retail
estate runs into:

- **Store requests cannot be grouped into a single fulfilment.** Every store request produces its
  own fulfilment. For a chain doing many small replenishments this is real warehouse overhead, and
  a consolidation capability is a legitimate improvement area.
- **Replenishment that does not need Supply Chain review could bypass it.** The design notes that a
  branch request could create an order fulfilment directly for routine replenishment. Leaving every
  request in a manual approval queue is a throughput cost that a maturing estate should revisit.

Both are useful in a proposal: they show the practice has been through real operations, and they
give a credible improvement story for phase two.

## Counting stock in a retail estate

Three separate count mechanisms coexist in the reference implementation, because three different
populations count:

1. **Warehouse count** — the in-house programme, high volume, scheduled
2. **Standard ERP count** — finance-driven, for controlled cycle counts
3. **Point-of-sale count** — store staff counting their own floor

Expect all three in any brand with an owned estate. Trying to force one mechanism on all three
populations is a common cause of adoption failure.

## Scoping signals

Raise the estimate when you see:
- Many stores, especially concessions inside department stores where the landlord's rules apply
- A point-of-sale product that is not integration-friendly, or several different ones across the estate
- Store-level stock accuracy expectations without a count discipline to support them
- Employee and complimentary sales that need separate tax and reporting treatment
- Events and pop-ups as a routine part of the calendar

## Discovery questions

1. How many own stores and counters, and are any of them inside a department store's system?
2. What point-of-sale system do the stores run, and can it call an API?
3. Do you post store sales daily or per transaction today, and what breaks at month end?
4. How do stores request replenishment, and who approves it?
5. What happens when a shopper returns an item in store — who authorises the refund?
6. How often do stores count, and who reconciles the difference?
7. Do you sell to staff, and does that need separate reporting?

## Related files

- **01** the channel map
- **04** consignment — the model that also applies to event stock
- **05** online — the other consumer-facing channel and the shared stock question
- **07** the inventory backbone, location groups and count mechanisms
- **11** the point-of-sale integration touchpoints
