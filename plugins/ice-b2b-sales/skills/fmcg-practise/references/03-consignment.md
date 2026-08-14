# 03 — Consignment (ฝากขาย)

> **Load this when:** goods sit at a counterparty's site but the brand still owns them · the words
> ฝากขาย, consignment, counter, sale-out recognition, or "we only get paid when it sells" appear ·
> a department-store counter, an event stand, or a merchandiser network is in scope.
> **Do not load this for:** outright sale into the same retailer → **02 Modern Trade** · what the
> retailer deducts from the payment → **10 Trade Spend and Net GP**.
> **Source basis:** the apparel implementation, where both models were designed, built and
> documented at flow level. This is the strongest-evidenced material in the whole skill.

## 1. Use cases — what this channel actually is

Consignment is goods placed with someone who will sell them, where **ownership stays with the brand
until the sale to the end shopper happens**. The counterparty holds stock it has not bought.

The recognisable situations: a department-store counter staffed by the brand's own merchandiser · a
specialty retailer that will carry the range but will not take the inventory risk · a distributor
trialling a new line · a pop-up or event stand · and the mirror case, where the brand itself holds
someone else's goods to sell.

### The finding that matters most: consignment is two designs, not one

Both were built in the reference implementation, in parallel, for different customer groups. **The
difference is the tax point, not the commercial arrangement** — and it is the single most valuable
distinction in this skill.

| | **True consignment (ฝากขายแท้)** | **Pseudo consignment (ฝากขายเทียม)** |
|---|---|---|
| Tax invoice issued | **when the goods sell** | **when the goods are delivered** |
| Goods move out as | a **transfer request** | a **sales order** |
| Stock relieved | at the sale-out feed | at fulfilment |
| Revenue recognised | at sale-out | at delivery |
| Second inventory book | not required | **required** — a shadow position holds the goods still at the counterparty |
| Invoicing pattern | periodic, **grouped** | one invoice at delivery |
| Custom development | moderate | **substantial** |

**Both existed for the same brand at the same time.** Which one applies is a commercial and tax
decision made per customer group, not a system preference.

**The same split was repeated for event and pop-up stock** (file **09**), which confirms it as a
reusable pattern rather than a one-off arrangement.

### Consignment-in — the mirror case

The brand may also **hold goods belonging to someone else** and sell them (รับฝากขาย). The reference
implementation carried this as its own sub-flow within traditional trade, and the warehouse topology
carries a separate location group for it. Consignment therefore runs in **both directions** in the
same design, and the two must not share a location.

### The three defining facts

- **Tax point:** sale-out for the true model; delivery for the pseudo model.
- **Debtor:** the retailer or counterparty, in both models.
- **Unsold stock owner:** the brand, in both models — which is precisely why neither can be treated
  as an ordinary sale.

## 2. Process — the flow

### True consignment — invoice when it sells

```
STOCK OUT
  buyer raises a TRANSFER REQUEST to the consignment location
  → approver signs off
  → system notifies the warehouse; goods delivered
  → merchandiser at the counter inspects and SCANS RECEIPT on the front-line system
  → stock auto-transfers into Location = Consignment
  ⓘ no revenue, no invoice — stock has moved, ownership has not

SALE
  merchandiser records sales on the front-line system through the day
  → sale-out data flows to the ERP; ONE SALES ORDER PER LOCATION PER DAY is created in batch
  → auto order fulfilment
  → accounting raises the AR invoice ON A CYCLE, GROUPED
  → billing → receipt
```

### Pseudo consignment — invoice when it is delivered

```
STOCK OUT
  the transfer is executed AS A SALES ORDER, not a transfer request
  → approval → auto order fulfilment
  → STOCK RELIEVED at fulfilment
  → a program auto-books a receipt of the same quantity into a consignment location
    IN A SECOND BOOK
  → accounting issues the invoice / tax invoice immediately

SALE
  merchandiser records the sale
  → ERP auto-relieves stock FROM THE SECOND BOOK, carrying a reference to the
    consignment invoice
  → billing → customer payment applied against the invoice already issued
```

**Read the pseudo model carefully.** The financial books already show a sale. The shadow book exists
solely so the business can still see what is physically standing at the counterparty. Keeping the
two in step is a custom program, and reconciling them is a period-close task.

### The daily batching decision

Sale-out arrives as many small consumer transactions and must land in the ERP as revenue. The
reference implementation collapsed them into **one sales order per location per day**. That is the
right default, but it needs two things decided before the first month-end: **the cut-off time**, and
**what happens to a late-arriving transaction** after the day has been posted.

## 3. Functions the system must provide

| # | Function | Why it is needed | Typically standard or custom |
|---|---|---|---|
| 1 | A **consignment location group** distinct from sellable warehouse stock | consigned goods are owned but not available to other channels | standard master data |
| 2 | A **separate consignment-in location group** | goods owned by someone else must never mix with own stock | standard master data |
| 3 | **Transfer request with approval** to move stock to a consignment location (true model) | moves stock without creating revenue | standard |
| 4 | **Receipt confirmation from the front line** that completes the transfer | the counter, not the warehouse, confirms arrival | integration |
| 5 | **Sale-out feed** from the front-line system into the ERP | this is the revenue event in the true model | integration, usually custom |
| 6 | **Daily batching of sale-out into one order per location**, with cut-off and late-arrival handling | keeps volume manageable without losing traceability | custom |
| 7 | **Grouped periodic invoicing** with source references surviving on every line | the counterparty expects one invoice per cycle, but disputes are line-level | standard invoicing, careful design |
| 8 | **Dual-book inventory** — real book relieved at delivery, shadow book holding the consigned position (pseudo model) | the only way to invoice at delivery and still see the goods | **substantial custom development** |
| 9 | **Synchronisation program** keeping the two books in step, with a reconciliation report | the books drift silently otherwise | custom |
| 10 | **Reference to the consignment invoice** carried on the shadow-book relief | without it, nothing ties the sale back to the invoice already raised | custom |
| 11 | **Periodic physical count at the counterparty's site**, with a variance and shrinkage route | the brand's stock is where the brand's staff are not | process plus standard count function |
| 12 | **Stock availability query back to the front-line system** | the counter needs to know what it can promise | integration |
| 13 | Returns from consignment stock — back to own warehouse, not into the retailer's return path | the goods were never the retailer's | standard, needs its own location |
| 14 | Reporting that shows **consigned stock separately from sellable stock** | otherwise available-to-promise is overstated across every other channel | standard reporting on a correct location design |

Functions 8, 9 and 10 are where the pseudo model earns its cost. **Do not quote the pseudo model as
configuration in any product.**

## 4. Integration touchpoints

| Touchpoint | Direction | Mode | What it carries |
|---|---|---|---|
| Consignment receipt scan | front-line system → ERP | asynchronous | confirmation that goods arrived at the counter |
| Sale-out feed | front-line system → ERP | asynchronous, daily batch | sale lines by location and item |
| Consignment stock adjustment | front-line system → ERP | real-time | the shadow-book relief in the pseudo model, with the invoice reference |
| Stock availability query | front-line system ← ERP | synchronous | on-hand at the consignment location |
| Warehouse release and confirmation | ERP ↔ warehouse | asynchronous | the physical delivery to the counter |
| Order creation from batched sale-out | ERP internal | scheduled | one order per location per day |

Inbound adjustments derive their **accounting dimensions from the sale channel carried on the
message** rather than from an operator's choice — the same pattern used at the point of sale. It is
how a business with many channels keeps its ledger analysable without asking counter staff to
understand accounting.

## 5. Challenges, gaps and improvement areas

| What commonly goes wrong | What the reference implementation did | What a better design looks like |
|---|---|---|
| **"Consignment" scoped as one requirement** | built both models separately, correctly | establish the tax point per customer group in discovery, before estimating. The two differ by an order of magnitude in effort |
| **Pseudo model sold as configuration** | delivered as custom programs plus a shadow book | price the dual-book mechanics, the synchronisation program, the reconciliation report and a support runbook as explicit line items |
| **The two books drift and nobody notices** | a synchronisation program kept them aligned | add a **reconciliation report to the period-close checklist**, not just the program. A program that fails silently is worse than no program |
| **Stock at the counterparty is counted rarely or never** | periodic count with variance handling | agree count frequency and who performs it **during discovery** — the counters are staffed by people who may not work for the client, and this is the single largest source of unexplained loss in this channel |
| **Consigned stock leaks into available-to-promise** | separate location groups | verify that every channel's availability logic excludes consignment locations — this is easy to get wrong and expensive to discover |
| **Late sale-out after the period closed** | daily batching with a cut-off | decide the late-arrival rule before the first close; it will happen in month one |
| **Consignment-in mixed with own stock** | its own location group | never share a location; ownership differs and so does the balance sheet treatment |
| **Sale-out assumed to arrive over EDI** | delivered through the merchandiser device | sale-out is **not** in the standard EDI document set (file **02**) — design it as its own path |

## 6. Discovery questions

1. Which customer groups hold your stock without having bought it? ⚑ *changes the estimate materially*
2. For each — **when must you issue the tax invoice: when you deliver, or when it sells?** ⚑ *this is the question that separates the two models*
3. How does sale-out reach you today, from each counterparty, and how often?
4. Who physically counts the stock at those sites, how often, and what happens when the count disagrees? ⚑
5. Do you also hold anyone else's goods on consignment?
6. When goods come back from a counter, where do they go — your warehouse, or the retailer's return process?
7. Do your other channels currently see consigned stock as available to sell?
8. What is your cut-off for a day's sale-out, and what do you do with a transaction that arrives after the period closed?
9. Do you run events or pop-ups with the same arrangement? *(same pattern, shorter fuse — file 09)*

## Related files

- **00** channel map and the classification method
- **02** modern trade — where consignment sits alongside outright sale on the same account
- **09** event and pop-up stock — the same two models on a shorter timescale
- **11** inventory and costing — the location topology that makes this possible
- **17** Thailand compliance — the tax-point question behind the two models
- **19** the full discovery bank
