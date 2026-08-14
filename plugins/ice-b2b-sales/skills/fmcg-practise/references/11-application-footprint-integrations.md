# 11 — The end-to-end application footprint and its integration catalogue

> Load this when the question is architecture: which system owns what, what the estate looks
> like end to end, how many integrations a multi-channel consumer brand needs, and how to
> draw the picture for an executive audience.

## The three-layer model

A consumer-goods brand selling B2B2C needs three layers plus the channel front ends. Presenting
it this way keeps an executive conversation out of the weeds while still being technically honest.

| Layer | What sits there | The one-line rationale |
|---|---|---|
| **Communication tools** | messaging apps, social channels, telephone, chat | reach the consumer where they already are |
| **Sales tools** (front operations) | pipeline management, dealer ordering app, modern-trade ordering app, sale-out capture, mobile order management, e-commerce order and return, export order and cost sheet, quotation, member management, customer data platform, segmentation, marketing automation, customer service | let each channel transact in its own idiom without bending the back office |
| **Core ERP** (back operations) | customer master, order management back end, product and pricing, accounts receivable, inventory management, purchasing, purchase requisition, accounts payable, work order, bill of materials and routing, costing, fixed assets, general ledger, demand planning | one financial and inventory truth |
| **Analytics** | sales analytics, customer analytics, ERP and supply-chain analytics | measure across the whole estate, not per silo |

**Channel front ends feeding the estate:** project sales · traditional trade (dealer) · modern
trade (purchase-order or file ordering) · owned store (point of sale) · e-commerce (own storefront
domestic and global, plus marketplaces) · export.

## The ownership rule that settles most architecture arguments

> **The ERP owns money, stock and master data. The front-end tools own engagement and
> channel-specific data entry.**

When a prospect asks "should this live in the ERP?", the test is: **does it change a balance or a
stock position?** If yes, the ERP is the record and the front end is a data-entry surface. If no —
a campaign, a segment, a conversation, a pipeline stage — it belongs in the front end and only its
outcome crosses the boundary.

Applied to the usual contested items:

| Capability | Owner | What crosses into the ERP |
|---|---|---|
| Loyalty membership and points (B2C and B2B) | member management / customer data platform | the customer record and credit position |
| Segmentation, campaigns, marketing automation | customer data platform / marketing suite | promotion definitions only |
| Pipeline, quotation, opportunity | CRM | the sales order and opportunity status |
| Dealer and modern-trade ordering | channel ordering apps | orders, credit notes, payments |
| Sale-out capture at the retailer | merchandiser device / in-house app | sale-in and sale-out records |
| Point of sale in own stores | POS | daily revenue summary, stock requests, stock adjustments |
| Marketplace and storefront orders | storefront + API gateway | order, credit note, payment, customer registration |
| Order management back end, product and pricing | **ERP** | native |
| Inventory, purchasing, work order, costing | **ERP** | native |
| Receivables, payables, general ledger, fixed assets | **ERP** | native |
| Case management and service | service desk / CRM | case reference against the order |

## The distribution cascade the architecture has to serve

```
Brand / manufacturer
  ├─ 1st tier wholesale → 2nd tier wholesale → retail → consumer
  ├─ Modern trade retail                             → consumer
  ├─ Own branch / store                              → consumer
  ├─ Online (storefront + marketplaces)              → consumer
  └─ Export
```

The same stock-keeping unit reaches the shopper through a two-step wholesale chain, a retail
buyer, the brand's own shop, and a marketplace — **each with a different owner of price, a
different debtor, and a different point at which the brand loses sight of the goods.** That is why
one "sales order" concept is never enough, and it is the clearest way to explain channel
complexity to an executive in one slide.

## The integration catalogue — roughly 25 touchpoints

The reference implementation's register, grouped by purpose. Codes are the reference
implementation's own numbering, kept because they show the shape and scale of a real estate.

### Group 1 — Master data (ERP is the master, front ends consume)

| Ref | Integration | Direction | Mode |
|---|---|---|---|
| INT10 | Product master | ERP → CRM | batch file over secure transfer |
| INT11 | Price list master | ERP → CRM | batch |
| INT01 | Create customer account | CRM → ERP | API, asynchronous |
| INT02 | Update customer account | ERP → CRM | API or batch, asynchronous |

### Group 2 — Pre-order checks (synchronous, because the rep is waiting)

| Ref | Integration | Direction | Mode |
|---|---|---|---|
| INT03 | Check stock | CRM → ERP | API |
| INT06 | Check customer credit | CRM → ERP | API, synchronous |

### Group 3 — Order capture

| Ref | Integration | Direction | Mode |
|---|---|---|---|
| INT04 | Create sales order | CRM → ERP | API, synchronous |
| INT05 | Create reserve order | CRM → ERP | API, synchronous |
| INT07 | Opportunity update | CRM → ERP | API |
| INT08 | Order search | CRM → ERP | API |
| INT09 | Order and reserve detail | CRM → ERP | API |
| INT18 | E-commerce order to sales order | storefront → ERP | API, asynchronous |
| INT23 | File template for modern-trade and online-platform orders | file import → ERP | batch |
| INT22 | Electronic-data-interchange order import | file import → ERP | batch |

### Group 4 — Point of sale

| Ref | Integration | Direction | Mode |
|---|---|---|---|
| INT12 | Daily revenue summary | POS → ERP | API |
| INT13 | Revenue detail for electronic tax filing | POS → ERP | API |
| INT14 | Stock adjustment | POS → ERP | API |
| INT15 | Stock request | POS → ERP | API, synchronous |
| INT16 | Stock response | ERP → POS | API, synchronous |
| INT17 | Sale-out transaction | merchandiser device → ERP | API |

### Group 5 — Warehouse and third-party logistics

| Ref | Integration | Direction | Mode |
|---|---|---|---|
| INT20 | Picking, move and issue instruction | ERP → 3PL | API |
| INT21 | Warehouse transaction confirmation | 3PL → ERP | API |
| INT21.1 | Fulfilment ship status onward to the point of sale | ERP → POS | API |
| INT17.1 | Consignment stock adjustment | in-house system → ERP | API |

### Group 6 — Money and platform

| Ref | Integration | Direction | Mode |
|---|---|---|---|
| INT19 | Payment-gateway result to order status | webhook → ERP | API |
| INT23 (gateway) | API gateway for online platforms | marketplaces → gateway → ERP | API |

Plus the customisation-side interfaces that grew during build — return creation from CRM, return
search, return receipt notification, credit memo from the point of sale, count-stock synchronisation,
tax-invoice file transfer to the electronic-tax service provider.

**The number itself is the message.** A multi-channel consumer brand runs on the order of
**twenty-five integrations, not five.** The register in the reference implementation reached
version nineteen by the end of build — it grew as channels were discovered. Budget for that growth
explicitly rather than being surprised by it.

## Patterns worth reusing from this catalogue

**1. Synchronous only where a human is waiting.** Credit check, stock check, order creation and
stock request are synchronous because someone is standing there. Everything else is asynchronous.
This is a good default for any estate of this shape.

**2. Master data flows outward in batch; transactions flow inward in real time.** Product and price
lists are batch feeds from the ERP; orders and confirmations are real-time calls into it. Cheap,
robust, and easy to explain.

**3. One gateway per channel family, not one integration per platform.** The marketplace gateway
(file 05) is the clearest example. The same logic argues for one warehouse interface serving both
sales fulfilment and stock transfers.

**4. Sale-channel-driven account mapping.** Inbound adjustments carry the sale channel, and the ERP
derives the account, department and class from it. Front-line staff never choose an account, and
the ledger stays analysable.

**5. One enumerated error contract across every integration.** The reference implementation uses the
same five error classes everywhere — required field missing, wrong data type, field width mismatch,
value not defined in the ERP, and stock not available — each with a code and a defined resend path.
Across twenty-five interfaces this turns support into a single runbook instead of twenty-five. It is
a quiet decision with a large operational payoff, and worth proposing deliberately.

## Worked example — sketching the footprint for a live prospect

**The brief you are given in the room:** *a fashion brand selling through two regional marketplaces,
about forty of its own shops, and counters inside three department-store chains. They also do team
kit for corporate customers.*

Work it in this order. It takes about ten minutes and it is the artefact this skill exists to
produce.

### Step 1 — enumerate the channels, and refuse to classify the ambiguous one

| What they said | Channel | Confident? |
|---|---|---|
| two marketplaces | online — marketplace sub-model | yes |
| forty own shops | owned store, point of sale | yes |
| counters in three department-store chains | **modern trade outright OR consignment — cannot tell yet** | **no** |
| team kit for corporate customers | project sales + transformation | yes |
| (not mentioned, always ask) | own website? export? dealers? staff sales? events? | unknown |

**Do not guess the counters.** Ask the ownership question — *after you deliver, if the goods do not
sell, who carries them on their balance sheet?* If the answer is "we do", ask the tax-point question
next, because true versus pseudo consignment is the difference between configuration and the
heaviest custom line in the estimate. Everything else in this sketch is a known shape with a known
answer; **the counters are the unknown that swings the number**, so they get the first question.

### Step 2 — lay the three layers

| Layer | For this prospect |
|---|---|
| **Communication** | messaging and social channels for consumer contact and chat selling, if they do it |
| **Sales tools** | marketplace connectivity → **a brand-owned API gateway** · point of sale across forty shops · sale-out capture at the department-store counters · a quotation and opportunity front end for corporate team kit |
| **Core ERP** | customer master, order management, product and pricing, receivables, inventory, purchasing, work order and bill of materials for team kit, costing, payables, general ledger, fixed assets for the shop estate, demand planning |
| **Analytics** | channel margin, sell-through by collection, ageing and dead stock |

### Step 3 — count the integrations, by group

| Group | For this prospect | Rough count |
|---|---|---|
| Master data | product and price out to the front ends; customer in and out | 3–4 |
| Pre-order checks | stock check, credit check for corporate customers | 2 |
| Order capture | marketplace orders via the gateway; corporate orders from the front end; counter sale-out | 3–4 |
| Point of sale | daily revenue summary, stock request, stock response, stock adjustment, credit memo, ship-status sync | 5–6 |
| Warehouse | fulfilment instruction out, confirmation back — serving both customer despatch and shop replenishment. **Ask whether a third-party provider runs the warehouse; if they run it in-house there is no interface here, and if there are two providers there are two** | 0–3 |
| Money and platform | payment gateway result, platform settlement data, electronic tax invoice submission | 2–3 |
| Returns | return creation, return receipt notification | 2 |

**Roughly twenty touchpoints before anyone has asked for anything unusual** — and one gateway
carrying the marketplaces rather than one integration per platform.

That is a little below the ~25 of the reference estate quoted earlier in this file, and correctly so:
this prospect has fewer channels, one warehouse arrangement and no export or dealer network yet.
Expect it to move toward twenty-five as the unasked channels surface — the count grows during design,
not after it.

### Step 4 — name the three things that will decide the estimate

1. **The counters' tax point** — configuration, or dual-book custom development.
2. **Whether the shops and the marketplaces draw on one stock pool** — and what happens on an
   oversell.
3. **Whether decorated team kit gets its own item code** — item-master strategy, and whether cost is
   calculated or set by a person.

### Step 5 — the sentence to say out loud

> *"You have at least four channels and probably six, around twenty integration points, and one
> question I cannot answer for you yet — whether the department-store counters are outright sales or
> consignment. That single answer moves this estimate more than anything else on the list, so it is
> where I would like to start."*

That sentence is the whole value of this skill in one line: **you have sized the shape, and you have
named the unknown instead of pricing around it.**

## Drawing this for an executive

The picture that lands is three horizontal bands — communication, sales tools, core ERP — with the
channels entering from the left and analytics across the top. Keep integration codes off the
executive version; they belong in the solution-architecture appendix. What the executive needs to
see is that **each channel keeps its own way of working while the money and the stock converge on
one place.**

## Scoping signals

Raise the estimate when you see:
- More than one point-of-sale product, or more than one 3PL
- Marketplaces without a gateway already in place
- A customer data platform or loyalty programme that must exchange customer and credit data
- Electronic tax filing obligations with a third-party service provider
- An existing middleware layer that must be kept

## Discovery questions

1. Draw me your current estate — what system does an order live in, from first contact to cash?
2. Which of these systems are you keeping, and which are in play?
3. Where is your customer master today, and who is allowed to create a customer?
4. Where are prices and promotions decided?
5. What sits between your marketplaces and your back office?
6. Who runs your warehouse, and whose system is the record?

## Related files

- **01** the channel map the architecture has to serve
- **05** the API gateway pattern in detail
- **06** the point-of-sale integration set
- **07** the warehouse and 3PL integration set
- **12** what usually goes wrong in the integration layer
