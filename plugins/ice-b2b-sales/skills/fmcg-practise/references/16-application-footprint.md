# 16 — The application footprint and its integration catalogue

> **Load this when:** the question is architecture — which system owns what, what the estate looks like
> end to end, how many integrations a multi-channel consumer brand actually needs, and how to draw the
> picture for an executive audience · a prospect asks "can you show us the landscape" · an estimate needs
> an integration count before the interfaces are specified.
> **Do not load this for:** how any single channel works — files **01**–**09** · what a promotion costs →
> **10** · stock and costing mechanics → **11** · Thai electronic tax documents → **17**.
> **Source basis:** the apparel reference implementation's integration register, which is the only one of
> the two references that carried a complete estate view, extended with the touchpoints the van-sales and
> trade-spend material added. Where a connection is general practice rather than evidenced, it says so.

## 1. The three-layer model

A consumer-goods brand selling B2B2C needs three layers plus the channel front ends. Presented this way,
an executive conversation stays out of the weeds while remaining technically honest.

| Layer | What sits there | The one-line rationale |
|---|---|---|
| **Communication tools** | messaging apps, social channels, telephone, chat | reach the consumer where they already are |
| **Sales tools** (front operations) | pipeline management, dealer ordering app, modern-trade ordering app, **van-sales mobile application and route planning**, sale-out capture, mobile order management, e-commerce order and return, export order and cost sheet, quotation, member management, customer data platform, segmentation, marketing automation, customer service | let each channel transact in its own idiom without bending the back office |
| **Core ERP** (back operations) | customer master, order management back end, product and pricing, accounts receivable, **deduction and dispute management**, inventory management, purchasing, requisition, payables, work order, bill of materials and routing, costing, fixed assets, general ledger, **demand planning** | one financial and inventory truth |
| **Analytics** | sales analytics, customer analytics, ERP and supply-chain analytics, **Net GP by retailer and item** | measure across the whole estate, not per silo |

**Channel front ends feeding the estate:** project and corporate sales · traditional trade (dealer) ·
**van sales / direct store delivery** · modern trade (portal, file or electronic ordering) · owned store
(point of sale) · e-commerce (own storefront domestic and global, plus marketplaces) · export.

## 2. The ownership rule that settles most architecture arguments

> **The ERP owns money, stock and master data. The front-end tools own engagement and channel-specific
> data entry.**

When a prospect asks "should this live in the ERP?", the test is: **does it change a balance or a stock
position?** If yes, the ERP is the record and the front end is a data-entry surface. If no — a campaign,
a segment, a conversation, a pipeline stage — it belongs in the front end, and only its outcome crosses
the boundary.

| Capability | Owner | What crosses into the ERP |
|---|---|---|
| Loyalty membership and points (B2C and B2B) | member management / customer data platform | the customer record and credit position |
| Segmentation, campaigns, marketing automation | customer data platform / marketing suite | promotion definitions only |
| Pipeline, quotation, opportunity | CRM | the sales order and opportunity status |
| Dealer and modern-trade ordering | channel ordering apps | orders, credit notes, payments |
| **Van-sales selling, delivery and collection on the vehicle** | mobile application, offline-capable | orders, deliveries, collections, returns, and the shift-close settlement |
| **Route planning and geofencing** | routing engine | the published route plan only |
| Sale-out capture at the retailer | merchandiser device / in-house app | sale-in and sale-out records |
| Point of sale in own stores | POS | daily revenue summary, stock requests, stock adjustments |
| Marketplace and storefront orders | storefront + API gateway | order, credit note, payment, customer registration |
| **Promotion master** | **trade spend owns the record; planning consumes it** | one identifier, two consumers — never two records (files **10**, **13**) |
| **Deduction, dispute and rebate accrual** | **ERP** — it changes a balance | native |
| **Demand plan** | planning capability, in or beside the ERP | the netted forecast, safety stock and replenishment signals |
| Order management back end, product and pricing | **ERP** | native |
| Inventory, purchasing, work order, costing | **ERP** | native |
| Receivables, payables, general ledger, fixed assets | **ERP** | native |
| Case management and service | service desk / CRM | case reference against the order |

## 3. The distribution cascade the architecture has to serve

```
Brand / manufacturer
  ├─ 1st tier wholesale → 2nd tier wholesale → retail → consumer
  ├─ Van sales / direct store delivery → small retail → consumer
  ├─ Modern trade retail                                → consumer
  ├─ Own branch / store                                 → consumer
  ├─ Online (storefront + marketplaces)                 → consumer
  └─ Export
```

The same stock-keeping unit reaches the shopper through a two-step wholesale chain, a van that both sells
and delivers, a retail buyer, the brand's own shop and a marketplace — **each with a different owner of
price, a different debtor, and a different point at which the brand loses sight of the goods.** That is
why one "sales order" concept is never enough, and it is the clearest way to explain channel complexity
to an executive in one slide.

## 4. The integration catalogue

Grouped by purpose. Groups 1–6 are the apparel reference implementation's own register — the shape and
scale of a real estate. Groups 7–9 are what the later channels add.

| Group | Touchpoint | Direction | Mode |
|---|---|---|---|
| 1 Master data | Product master · price list master | ERP → front ends | batch |
| 1 | Create customer account | CRM → ERP | API, asynchronous |
| 1 | Update customer account | ERP → CRM | API or batch, asynchronous |
| 1 | **SKU-to-retailer article-code cross-reference** | ERP ↔ planning and deduction matching | shared master (files **10**, **13**) |
| 2 Pre-order checks | Check stock | front end → ERP | API |
| 2 | Check customer credit and overdue | front end → ERP | **synchronous** — a person is waiting |
| 3 Order capture | Create sales order · create reserve order | front end → ERP | API, synchronous |
| 3 | Opportunity update · order search · order and reserve detail | CRM ↔ ERP | API |
| 3 | E-commerce order to sales order | storefront → ERP | API, asynchronous |
| 3 | File template for modern-trade and online-platform orders | file import → ERP | batch |
| 3 | Electronic-data-interchange order import | bureau or retailer → ERP | batch |
| 4 Point of sale | Daily revenue summary · revenue detail for electronic tax filing | POS → ERP | API |
| 4 | Stock request · stock response | POS ↔ ERP | **synchronous** |
| 4 | Stock adjustment · credit memo from the counter | POS → ERP | API |
| 4 | Fulfilment ship status onward to the point of sale | ERP → POS | API |
| 4 | Sale-out transaction | merchandiser device → ERP | API |
| 5 Warehouse and 3PL | Picking, move and issue instruction | ERP → 3PL | API |
| 5 | Warehouse transaction confirmation | 3PL → ERP | API |
| 5 | Consignment stock adjustment | in-house system → ERP | API |
| 6 Money and platform | Payment-gateway result to order status | webhook → ERP | API |
| 6 | API gateway for online platforms | marketplaces → gateway → ERP | API |
| 6 | Platform settlement report | platform → ERP | batch, per cycle |
| 6 | Tax-invoice file transfer to the electronic-tax provider | ERP → tax service | batch |
| **7 Field sales and van** *(file 04)* | Product, price and scheme catalogue | ERP → mobile device | batch, with offline cache |
| 7 | Outlet master and credit position | ERP → mobile device | batch, refreshed per shift |
| 7 | Load-out confirmation | load-out → van inventory | synchronous |
| 7 | Order, delivery and collection capture | mobile device → ERP | **asynchronous, queued offline** |
| 7 | Returns brought back to the warehouse | van → warehouse receipt | asynchronous |
| 7 | Electronic collection totals per shift | gateway → reconciliation | asynchronous, read-only into the close |
| 7 | Shift-close posting | reconciliation → ledger | batch, deliberately delayed |
| 7 | Route plan and geofence | routing engine → mobile device | batch, on publish |
| **8 Trade spend** *(file 10)* | Point-of-sale scan report | retailer → ERP | batch, per promotion cycle |
| 8 | Remittance advice with deduction lines and retailer reason codes | retailer → ERP | batch, per payment |
| 8 | Retailer portal extract — deductions and dispute status | portal → ERP | batch or manual |
| 8 | Bank statement, for the unexplained residue | bank → ERP | batch |
| 8 | Dispute submission with evidence pack | ERP → retailer portal | often manual |
| 8 | Evidence capture — proof of delivery, timestamps, images | warehouse and carrier → ERP | event-driven |
| **9 Planning** *(file 13)* | Sell-through ingestion for demand derivation | **the same retailer feed as the sale-out row above** | batch, lag-aware |
| 9 | Promotion master binding | trade spend ↔ planning | **one shared record, not an interface built twice** |
| 9 | Net unconsumed forecast to MRP | planning → production | batch, on version lock |
| 9 | FEFO consumption schedule | planning → warehouse | batch, daily or weekly |

Plus the customisation-side interfaces that grow during build — return creation from the front end, return
search, return receipt notification, credit memo from the point of sale, count-stock synchronisation, and
asset transfer, disposal and count feeds where the retail estate is managed from the sales-channel side
(file **15**).

**The number itself is the message.** The apparel estate ran on the order of **twenty-five integrations,
not five**, and its register reached its nineteenth version by the end of build — it grew as channels were
discovered. Adding a van operation contributes roughly eight more touchpoints and a deduction desk another
six, so **a brand running modern trade, vans and a trade-spend function lands closer to forty than to
twenty-five.** Budget for that growth explicitly rather than being surprised by it. Two of the planning
rows above are deliberately *not* new interfaces, and saying so is worth as much as the count: the
sell-through feed and the promotion master are shared records, and building them twice is the classic
avoidable cost.

## 5. Patterns worth reusing

**1. Synchronous only where a human is waiting.** Credit check, stock check, order creation, stock request
and van load-out are synchronous because someone is standing there. Everything else is asynchronous, with a
visible status so users are not left guessing.

**2. Master data flows outward in batch; transactions flow inward in real time.** Product and price lists
are batch feeds from the ERP; orders and confirmations are real-time calls into it. Cheap, robust, easy to
explain.

**3. One gateway per channel family, not one integration per platform.** The marketplace gateway (file
**06**) is the clearest example; the same logic argues for one warehouse interface serving both sales
fulfilment and stock transfers.

**4. Sale-channel-driven account mapping.** Inbound adjustments carry the sale channel and the ERP derives
account, department and class from it, so front-line staff never choose an account and the ledger stays
analysable. **File 15 adds the condition that makes this safe:** the derivation must come from one governed
mapping table, not from each interface deciding for itself.

**5. One enumerated error contract across every integration** — the same five error classes everywhere
(required field missing, wrong data type, field width mismatch, value not defined in the ERP, stock not
available), each with a code and a defined resend path. Across forty interfaces that turns support into a
single runbook instead of forty: a quiet decision with a large operational payoff, worth proposing
deliberately.

**6. Offline-first wherever connectivity is not guaranteed.** The van channel cannot assume a signal at the
outlet, so capture queues on the device and settles at shift close, with catalogue and credit position
cached rather than called. A design requiring a live call in the field will fail in the field.

**7. Share the record instead of interfacing it.** Where two domains need the same object — promotion
master, article-code cross-reference, sell-through feed — bind them to one record with one identifier. An
interface between two masters is an agreement to disagree on a schedule.

## 6. Worked example — sketching the footprint for a live prospect

**The brief you are given in the room:** *a fashion brand selling through two regional marketplaces, about
forty of its own shops, and counters inside three department-store chains. They also do team kit for
corporate customers.*

Work it in this order. It takes about ten minutes and it is the artefact this skill exists to produce.

### Step 1 — enumerate the channels, and refuse to classify the ambiguous one

| What they said | Channel | Confident? |
|---|---|---|
| two marketplaces | online — marketplace sub-model | yes |
| forty own shops | owned store, point of sale | yes |
| counters in three department-store chains | **modern trade outright OR consignment — cannot tell yet** | **no** |
| team kit for corporate customers | project sales + transformation | yes |
| (not mentioned, always ask) | own website? export? dealers? vans? staff sales? events? | unknown |

**Do not guess the counters.** Ask the ownership question — *after you deliver, if the goods do not sell,
who carries them on their balance sheet?* If the answer is "we do", ask the tax-point question next,
because true versus pseudo consignment is the difference between configuration and the heaviest custom
line in the estimate. Everything else here is a known shape with a known answer; **the counters are the
unknown that swings the number**, so they get the first question.

### Step 2 — lay the three layers

| Layer | For this prospect |
|---|---|
| **Communication** | messaging and social channels for consumer contact and chat selling, if they do it |
| **Sales tools** | marketplace connectivity → **a brand-owned API gateway** · point of sale across forty shops · sale-out capture at the department-store counters · a quotation and opportunity front end for corporate team kit |
| **Core ERP** | customer master, order management, product and pricing, receivables, **deduction management for the department-store accounts**, inventory, purchasing, work order and bill of materials for team kit, costing, payables, general ledger, fixed assets for the shop estate, demand planning |
| **Analytics** | channel margin, **Net GP by retailer**, sell-through by collection, ageing and dead stock |

### Step 3 — count the integrations, by group

| Group | For this prospect | Rough count |
|---|---|---|
| Master data | product and price out to the front ends; customer in and out | 3–4 |
| Pre-order checks | stock check, credit check for corporate customers | 2 |
| Order capture | marketplace orders via the gateway; corporate orders from the front end; counter sale-out | 3–4 |
| Point of sale | daily revenue summary, stock request, stock response, stock adjustment, credit memo, ship-status sync | 5–6 |
| Warehouse | fulfilment instruction out, confirmation back — serving both customer despatch and shop replenishment. **Ask whether a third party runs the warehouse; in-house means no interface here, and two providers mean two** | 0–3 |
| Money and platform | payment gateway result, platform settlement data, electronic tax invoice submission | 2–3 |
| **Trade spend** | remittance advice and portal extract from the department-store chains, dispute submission, evidence capture | **2–4** |
| Returns | return creation, return receipt notification | 2 |
| Field sales | **none — they run no vans.** Ask anyway, because a wholesale ambition adds a whole group | 0 |

**Roughly twenty-two touchpoints before anyone has asked for anything unusual** — and one gateway carrying
the marketplaces rather than one integration per platform. That is below the ~25 of the apparel estate and
well below the ~40 of a brand with vans and a deduction desk, and correctly so: this prospect has fewer
channels, one warehouse arrangement, no vans, and no export or dealer network yet. Expect it to climb as
the unasked channels surface — the count grows during design, not after it.

### Step 4 — name the three things that will decide the estimate

1. **The counters' tax point** — configuration, or dual-book custom development.
2. **Whether the shops and the marketplaces draw on one stock pool** — and what happens on an oversell.
3. **Whether decorated team kit gets its own item code** — item-master strategy, and whether cost is
   calculated or set by a person.

### Step 5 — the sentence to say out loud

> *"You have at least four channels and probably six, around twenty integration points, and one question I
> cannot answer for you yet — whether the department-store counters are outright sales or consignment. That
> single answer moves this estimate more than anything else on the list, so it is where I would like to
> start."*

That sentence is the whole value of this skill in one line: **you have sized the shape, and you have named
the unknown instead of pricing around it.**

## 7. Drawing this for an executive

The picture that lands is three horizontal bands — communication, sales tools, core ERP — with the channels
entering from the left and analytics across the top. Keep integration codes off the executive version; they
belong in the solution-architecture appendix. What the executive needs to see is that **each channel keeps
its own way of working while the money and the stock converge on one place.**

## 8. Challenges, gaps and improvement areas

| What commonly goes wrong | What the reference implementation did | What a better design looks like |
|---|---|---|
| **Integration count sized from the channels the client volunteered** | the register reached its nineteenth version during build as channels surfaced | enumerate the unasked channels in discovery and budget for growth explicitly |
| **One integration per marketplace** | a single brand-owned gateway | one gateway per channel family; platforms plug into it |
| **Shared records rebuilt as interfaces** | the promotion master and sell-through feed are each consumed by two domains | bind to one record with one identifier — see pattern 7 |
| **Error handling designed per interface** | one enumerated error contract across the estate | five error classes, one code set, one resend path, one support runbook |
| **Channel derived independently by each interface** | inbound messages carried the sale channel and each interface mapped it | keep the mechanism, add the single governed mapping table of file **15** |
| **A live call assumed at the point of sale in the field** | the van design queues offline and settles at shift close | offline-first, with the catalogue and credit position cached |
| **Middleware inherited but unexamined** | not evidenced either way in the source | ask what sits between the front ends and the back office today, and who supports it |

**Scoping signals — raise the estimate when you see:** more than one point-of-sale product, or more than
one third-party logistics provider · marketplaces with no gateway already in place · a customer data
platform or loyalty programme that must exchange customer and credit data · electronic tax filing through
a third-party service provider · an existing middleware layer that must be kept · a field-sales fleet, or
an ambition to start one · deductions arriving from more than a handful of retailers.

## 9. Discovery questions

1. Draw me your current estate — what system does an order live in, from first contact to cash? ⚑
2. Which of these systems are you keeping, and which are in play?
3. Where is your customer master today, and who is allowed to create a customer?
4. Where are prices and promotions decided — and does the ERP see the breakdown? ⚑
5. What sits between your marketplaces and your back office?
6. Who runs your warehouse, and whose system is the record? ⚑
7. Do your field staff sell from a vehicle, and does their device work without a signal?
8. Where do retailer deductions arrive, and what system holds them today?
9. Which systems already exchange data automatically, and which are re-keyed by a person? ⚑

## Related files

- **00** the channel map the architecture has to serve
- **04** van sales — the offline-first group, and the shift close
- **06** online and marketplace — the API gateway pattern in detail
- **05** owned store — the point-of-sale integration set
- **10** trade spend and Net GP — the deduction group and the promotion master
- **11** inventory and 3PL — the warehouse integration set
- **13** demand planning — the shared feeds and the MRP handoff
- **15** ledger dimensions — what every inbound message must populate, and how
- **19** what usually goes wrong in the integration layer
