# 05 — Owned store and point of sale (ร้านของแบรนด์เอง)

> **Load this when:** the brand runs its own shops, outlet stores or counters inside a department
> store · the words "POS", "หน้าร้าน", "สาขา", "ปิดยอดสิ้นวัน", "ขอใบกำกับภาษี" or "ขอเบิกสินค้าเข้าสาขา"
> appear · a point-of-sale system has to meet the ERP.
> **Do not load this for:** a temporary point of sale that runs for a few days and then ends — an
> event, a pop-up, a roadshow — or for sales to the brand's own staff and complimentary giveaways →
> those ride on the same point-of-sale route but behave differently in the accounts, and they live in
> **09 Event, employee, complimentary and other**.
> **Source basis:** one reference implementation — a Thai apparel and sportswear brand with an owned
> retail estate alongside its wholesale business — from its order-to-cash blueprint, its inventory
> design and its point-of-sale integration specifications. This material was designed, built and run;
> the two limitations recorded in §5 are the design team's own, stated openly.

## 1. Use cases — what this channel actually is

An owned store is the brand selling directly to a consumer from premises the brand controls. The
whole channel turns on one design decision that the reference implementation made deliberately and
that generalises: **the ERP is posted by the day, not by the transaction.**

The three defining facts:

- **Tax point** — on request, otherwise at the daily aggregated posting. Thai consumers ask for a tax
  invoice (ใบกำกับภาษี) selectively, so the channel has two tax points running side by side and the
  design has to carry both. This is §1's most consequential sentence and is expanded below.
- **Who the debtor is** — the consumer, who has already paid. What the receivable actually tracks is
  the shop, until its takings reach the bank.
- **Who owns unsold stock** — the brand, on its own site. There is no consignment question here
  because nobody else's premises are involved.

**The recognisable situations.** A brand runs a handful of flagship shops plus outlet stores clearing
end-of-season goods, a factory shop selling seconds, and a **concession or counter** inside a
department store. All post the same way and share the same replenishment problem; what differs is who
owns the till — and that is the variant which changes the design most. Where the landlord's own point
of sale takes the money, the debtor becomes the department store rather than the consumer, settlement
turns periodic rather than daily, and the arrangement is often a consignment in substance, at which
point the tax-point question of file **03** returns and this file is no longer the right home. Ask
early, and ask per counter rather than per retailer.

### Why the day rather than the transaction

- A store does hundreds of small transactions. The general ledger needs the day, not the line.
- The point-of-sale system is the operational system of record for the shop floor; the ERP is the
  financial system of record. Each keeps the grain it needs, and neither is asked to be the other.
- Day-end is when the shop reconciles its cash anyway, so it is the natural posting boundary.

Real-time posting is right for the things that cannot wait — **stock requests** and **stock
adjustments** — and those are integrated separately and synchronously. The rule that falls out is
worth stating in any solution design: *aggregate the money, but never the stock.*

## 2. Process — the flow

```
DURING THE DAY
  consumer buys at the counter
  → [branch] customer asks for a tax invoice?  yes → capture customer tax data at the till
  → point-of-sale system holds the transaction detail; nothing posts to the ERP yet

AT CLOSE OF DAY — one message, two populations
  point-of-sale sends the daily revenue summary per shop
  → ERP splits it:
       customers who requested a tax invoice → ONE INVOICE EACH, in that customer's name,
         receipts recorded per customer and per payment type
       customers who did not                 → aggregated into ONE SUMMARY CUSTOMER,
         one invoice, receipts grouped by payment type
  → revenue side posted:  Dr AR-Shop / Cr Revenue / Cr Output Tax
  → cost side posted:     Dr Cost of Goods Sold / Cr Inventory
  → receipts accepted, SPLIT BY PAYMENT TYPE — cash · card · transfer · wallet
  → shop sends its daily sales and tax reports to Accounting for the cash reconciliation
  → on settlement:        Dr Bank / Cr AR-Shop

REPLENISHMENT — real time, not day-end
  store raises a stock request → ERP creates a TRANSFER ORDER
  → Supply Chain reviews and approves → despatch
  → transfer into an IN-TRANSIT LOCATION on despatch
  → second transfer from in-transit into the shop on receipt
  → ship-status passed back so the store can book the goods in

RETURN AT THE COUNTER
  shopper returns an item → credit memo raised FROM the point of sale, refund immediate
  → returned unit inspected → sellable stock, or a returns or damaged bin inside the store location
```

**The tax-invoice split is the detail everyone misses.** The daily posting is not one invoice per
shop. It is one invoice per customer who asked, plus one aggregated invoice for everyone who did not.
That single rule is what keeps a consumer retail estate's receivable sub-ledger usable in Thailand.
Design it in from the start; it is expensive to retrofit and it is not a reporting afterthought.

**Why replenishment moves through in-transit.** Stock is never invisible and never double-counted, and
the difference between despatch and receipt becomes a measurable delivery gap rather than an argument.

**Why the counter return bypasses the usual approval chain.** The shopper is standing there and the
refund happens immediately, so no back-office approval can realistically run first. The consequence is
that the store-level credit memo needs a control of its own — who may authorise, up to what value,
against which reason codes — because the normal chain is bypassed by necessity, not by oversight.

## 3. Functions the system must provide

| # | Function | Why it is needed | Typically standard or custom |
|---|---|---|---|
| 1 | **Daily revenue summary per shop** creating the receivable and the revenue posting | the general ledger needs the day, not the transaction | integration build |
| 2 | **Tax-invoice split** — a named invoice per requesting customer, plus one aggregated summary customer for the rest | Thai consumers request tax invoices selectively; without this the sub-ledger is unusable | custom, and easy to miss in scoping |
| 3 | Capture of customer tax data **at the till**, on the request branch only | the data does not exist unless it is asked for at the moment of sale | point-of-sale configuration |
| 4 | **Receipts split by payment type** — cash, card, transfer, wallet | the shop's takings must reconcile to the bank by tender | standard, needs the split on the inbound message |
| 5 | Cost posting alongside revenue at the same daily boundary | otherwise margin by shop is not available | standard |
| 6 | **Stock request from the store, in real time**, creating a transfer order for Supply Chain approval | a shop that cannot ask for stock will phone instead, and the request will not be in the system | integration build |
| 7 | **Stock response** back to the store — what is available and what is coming | prevents the shop asking twice | integration build |
| 8 | **Stock adjustment from the store, in real time** — damage, loss, found stock, count correction | store stock accuracy decays daily, not monthly | integration build |
| 9 | **Ship-status synchronised back to the store** | the shop cannot book goods in against a despatch it cannot see | integration build |
| 10 | **Account, department and class derived from the sale channel** on every inbound message | keeps the ledger analysable without asking shop staff to understand accounting | integration design — adopt this pattern everywhere a front-line system posts |
| 11 | **In-transit location** on every store transfer, with two movements rather than one | stock is never invisible and never double-counted | standard, if location design allows it |
| 12 | **Credit memo raised from the point of sale**, with its own authorisation control and reason codes | the refund happens before any approval chain could run | integration build plus deliberate control design |
| 13 | **Bins separated by material status inside a store location** — good, damaged, customer claim | a returned unit's condition decides whether it is sellable again | standard location design |
| 14 | **Three count mechanisms coexisting** — warehouse programme, finance-driven ERP cycle count, and a store count run by shop staff | three different populations count, and forcing one mechanism on all three is a common cause of adoption failure | standard, but the count design must be explicit |
| 15 | **Consolidation of several store requests into one fulfilment** | see §5 — this was absent in the reference implementation and is real warehouse overhead | custom; assume it is not free |
| 16 | Shop as a **reporting dimension** on every transaction, including adjustments | per-shop margin and per-shop shrinkage are otherwise unavailable | standard, governance-dependent |

Rows 2, 10, 12 and 15 are where the effort and the surprises concentrate. The last column describes
mainstream capability in this category rather than any one product's behaviour; verify it against the
point-of-sale product actually in the estate, because integration-friendliness varies more here than
anywhere else in the channel set.

## 4. Integration touchpoints

| Touchpoint | Direction | Mode | What it carries |
|---|---|---|---|
| Daily revenue summary | point of sale → ERP | asynchronous, once per shop per day | revenue, tax, receipts by payment type, tax-invoice requests |
| Revenue detail for electronic tax documents | point of sale → ERP | asynchronous | transaction-level detail behind the requested invoices |
| Store stock position | point of sale → ERP | asynchronous | on-hand as the shop sees it |
| Stock request | point of sale → ERP | **synchronous** — a person is waiting | shop, item, quantity requested |
| Stock response | ERP → point of sale | **synchronous** | available now, and what is already on its way |
| Stock adjustment | point of sale → ERP | real time | increase or decrease, with the sale channel that drives the account mapping |
| Ship-status synchronisation | ERP → point of sale | real time | fulfilment shipped status, so the shop can receive |
| Credit memo from the counter | point of sale → ERP | real time | return, reason code, refund method |
| Product and price master | ERP → point of sale | batch | items, prices, promotions |

**A standardised error contract across these integrations is worth insisting on** — missing required
field, wrong data type, field-width mismatch, value not defined in the ERP, on-hand not available —
each returning a coded error that the sending system re-validates and resends. Across an estate of
roughly twenty-five integrations this turns support into one runbook instead of twenty. The full
estate view lives in file **16**.

## 5. Challenges, gaps and improvement areas

| What commonly goes wrong | What the reference implementation did | What a better design looks like |
|---|---|---|
| **Every transaction posted to the ERP in real time** | posted a daily summary per shop deliberately, and kept only stock movements real time | keep the split; aggregate the money, never the stock |
| **The tax-invoice-on-request branch treated as a report** | built the split into the daily posting — named invoices plus one aggregated summary customer | design it in at the first blueprint; retrofitting it means re-cutting the receivable sub-ledger |
| **Store requests cannot be grouped into one fulfilment** | recorded openly as a limitation — every store request produced its own fulfilment, which for a chain doing many small replenishments is real warehouse overhead | consolidation of requests into a single fulfilment is a legitimate phase-two capability; price it rather than assume it |
| **Routine replenishment queued behind a manual review it does not need** | every request passed Supply Chain approval; the design noted that routine replenishment could create a fulfilment directly | tier the approval by value or by whether the item is on a standing replenishment plan — leaving everything in a manual queue is a throughput cost a maturing estate should revisit |
| **Store staff asked to choose accounting codes** | account, department and class derived from the sale channel on the inbound message | adopt this wherever a front-line system posts to the ledger |
| **Counter refunds with no control of their own** | credit memo raised from the point of sale, necessarily ahead of any approval chain | give the store-level credit memo an explicit authorisation limit and reason-code set, since it bypasses the normal chain by design |
| **One counting mechanism forced on three populations** | three mechanisms coexisted — warehouse, finance, store | expect all three; a single mechanism is a common cause of adoption failure |
| **Stock value expected per shop without deciding the valuation grain** | moving-average costing, with the grain — by legal entity or by location — recorded as an open decision, and per-location inventory valuation noted as unreliable when the average is held above location level | decide the grain in design, and tell the controller that per-shop stock valuation is a design decision with a report-accuracy consequence rather than a configuration checkbox. Full treatment in file **11** |
| **A concession assumed to behave like an owned shop** | — | where the landlord's till takes the money, the debtor and the tax point both move, and the arrangement may be a consignment in substance — file **03** |

## 6. Discovery questions

1. How many own shops and counters, and are any of them inside a department store's own system? ⚑
   *a concession may not belong in this channel at all*
2. For a counter inside a department store — who takes the money, and when do you get it?
3. What point-of-sale product do the shops run, and can it call an interface? Is it the same product
   across the whole estate? ⚑ *several different products means several integrations*
4. Do you post store sales daily or per transaction today, and what breaks at month end?
5. How many of your shoppers ask for a tax invoice, and how do you capture their details today? ⚑
6. How do you reconcile a shop's takings to the bank — is the day split by payment type?
7. How does a shop ask for stock, who approves it, and how long does that take?
8. Can several shop requests be filled in one delivery today, or does each one become its own?
9. What happens when a shopper returns an item — who authorises the refund, up to what value, and
   where does the returned item go?
10. How often do shops count, who counts, and who reconciles the difference?
11. Does your controller expect stock value per shop? ⚑ *opens the costing-grain conversation in file 11*

## Related files

- **00** channel map and the classification method
- **03** consignment — the model a department-store counter may actually be
- **06** online and marketplace — the other consumer-facing channel, and the shared stock question
- **09** event, employee, complimentary and other — the groups that ride on this same point-of-sale route
- **11** inventory, locations and costing — location groups, in-transit, count mechanisms, the costing grain
- **16** the application estate and its integration catalogue
- **17** Thailand compliance — tax invoices, electronic tax documents, the request branch
- **19** the full discovery bank
