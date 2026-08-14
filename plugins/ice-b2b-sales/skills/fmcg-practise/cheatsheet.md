# Cheatsheet — decision rules for FMCG / fashion multi-channel solution design

> One page to keep beside you in a discovery meeting or a solution workshop.
> This file holds **judgement**, not definitions. For terms see `glossary.md`;
> for repeatable mechanisms see `patterns.md`.

## The three questions that define a channel

Ask these of every customer group. Two groups that differ on **any** of the three need separate
treatment, however similar the commercial deal looks.

| # | Question | Why it decides the design |
|---|---|---|
| 1 | **When must the tax invoice be issued?** | sets the revenue and VAT point, which sets the document chain |
| 2 | **Who actually owes you the money?** | sets the receivable sub-ledger and the reconciliation work |
| 3 | **After delivery, whose balance sheet carries the stock?** | sets whether you need a consignment location, a shadow book, or neither |

## Consignment — the decision tree

```
Goods sit at someone else's site and the sale happens later
│
├─ Tax invoice on SALE-OUT  →  TRUE consignment (ฝากขายแท้)
│   • move with a Transfer Request; no revenue at delivery
│   • stock sits in a consignment location, still yours
│   • daily batch sale-out feed creates the sales order
│   • invoice on a cycle, GROUPED
│   • cost driver: periodic counts + feed reliability
│
└─ Tax invoice on DELIVERY  →  PSEUDO consignment (ฝากขายเทียม)
    • move as a SALES ORDER; stock relieved and revenue booked now
    • a SHADOW BOOK holds the position still physically at the retailer
    • sale-out feed only relieves the shadow book
    • cost driver: dual-book sync program + reconciliation report
    ⚠ this is custom development in any ERP — never quote it as configuration
```

**If both models are in scope, that is two designs, not one design with a flag.**

## Online — who is the debtor?

| Sub-model | Debtor | Order opens | Invoice trigger | Reconciliation pain |
|---|---|---|---|---|
| Website prepaid | consumer | **pending** | after payment verified + fulfilment | low |
| Website cash on delivery | **courier** | **approved** | at despatch, collected on courier remittance | medium |
| Marketplace | **platform** | approved | on platform delivery confirmation | **high — net settlement, many-to-one** |
| Chat / social | consumer | pending | after payment evidence verified | low, but manual |

**Rule:** if the answer to "who pays you" changes, the AR design changes. Do not let "e-commerce"
be one line in a scope document.

## Modern trade versus consignment — the disambiguator

> After you deliver, if the goods do not sell, **who carries them on their balance sheet?**
> Retailer → modern trade outright. You → consignment.

Everything else (both involve a mall, both need sale-out data, both have deductions) is noise.

## EDI expectation setting

| What the customer says | What to assume | What to budget |
|---|---|---|
| "The retailer has EDI" | EDI covers the **purchase order** and little else | file/template import path + sale-out reconciliation report |
| "We want full EDI" | prove it retailer by retailer before committing | discovery task per retailer group, before the estimate is fixed |

Promising EDI parity in a proposal and finding the retailer's limits during build is a schedule
risk that lands on the implementer, not the customer.

## Costing — how to advise

| If the customer... | Then... |
|---|---|
| wants stock value **per shop or per location** and uses moving average at subsidiary level | say plainly that per-location valuation will not be accurate; it is a design decision with a reporting consequence, not a checkbox |
| has stable manufacturing cost and a real cost-accounting function | standard cost with variance analysis is the better fit |
| needs lot traceability or has genuine seasonal ageing | first-in-first-out, accepting the transactional overhead |
| decorates or subcontracts goods | ask **who determines the transformed cost — the system or a person?** If a person, put a cost-verification report in the month-end checklist |
| sells seasonal apparel | ageing and fast/slow/dead-stock reporting is **in scope**, not standard — this is where their margin goes |

## Transformation — change the item code or not?

| Change the item code when | Keep the item code when |
|---|---|
| the output is independently sellable | the decoration is one-off and customer-specific |
| it needs its own demand history and price | it will never be sold to anyone else |
| it appears in a catalogue | you would otherwise create hundreds of dead codes |
| **cost:** item-master proliferation, needs an owner | **cost:** added value must be carried elsewhere; stock cannot distinguish decorated from plain |

## Location design — the generating test

> For every place a unit can be, ask: **do I own it?** and **can I sell it this month?**
> Two different answers = two different location groups.

The eight groups this produces: trading · transformation · consignment-out · consignment-in ·
returns · work-in-process/in-transit · loaned · damaged.

Bins inside a location separate by **material status** (good / damaged / claim), because one
location holds several conditions at once.

## Pricing and promotion — the rule

> **The front end owns the decision. The ERP owns the record.**

| The client says | Your response |
|---|---|
| "discounts are decided in our sales app / on the platform / at the till" | fine — that is the right place. **Does the discount come back to the ERP on the transaction?** |
| "the ERP just gets the net price" | that is the gap. Net-only means you can report revenue but never explain it — no discount analysis, no campaign effectiveness, no channel margin |
| "we can work the discount out from the base price" | you recover the **amount**, not the **type** or the **funder**. Stopgap, not design |
| "the platform funded that promotion" | then it is **not brand cost** — book it separately, or online margin is understated and the channel looks worse than it is |

**Must land on the ERP sales line, every channel:** gross price · discount amount and percentage ·
discount/promotion **type** · campaign **code** · net price · **who funded it**.

## Marketplace settlement — the three-way match

```
ERP revenue  ──match by order──  platform settlement report  ──match by cycle──  bank receipt
(invoices from confirmed         (per-order gross, each                          (one net receipt)
 deliveries)                      deduction, net payable)
```

Three questions the design must answer: **did they pay for everything you shipped · were the
deductions correct · does the net equal the money that arrived.**

Build: platform order reference on every document · a settlement record per cycle per platform ·
deductions posted **by type** not one bucket · brand-funded separated from platform-funded ·
many-to-one cash application · aged variance report with an owner · a tolerance and write-off route.

**Match on the order, not the period** — returns settle on a different cycle from the sale.

**The discovery question:** *"How do you know today that the platform paid you for everything you
shipped, and that its deductions were correct?"* The answer is almost always a spreadsheet and a
person — and that person will sponsor this part of the project.

## Where to put the boundary between ERP and front end

> **Does it change a balance or a stock position?**
> Yes → the ERP is the record. No → the front end owns it, and only the outcome crosses.

## Integration defaults

| Situation | Default |
|---|---|
| a human is waiting for the answer | **synchronous** — credit check, stock check, order creation, stock request |
| everything else | **asynchronous** |
| master data going outward | **batch** — product, price list |
| transactions coming inward | **real time** |
| more than one marketplace | **one gateway**, not one integration per platform |
| front-line system posting to the ledger | derive account / department / class from the **sale channel**, never from operator choice |
| any estate above ~10 interfaces | one **enumerated error contract** shared across all of them |

## Estimating signals — what makes a consumer-goods ERP deal bigger than it looks

**This skill gives you line items, not effort figures.** It carries no verified man-day data, and
inventing ranges would be worse than omitting them. Take the *what to price separately* from here
and the *how much* from your own delivery estimating model.

### Relative weight — which lines are the large ones

Ordered by **design complexity and custom-development content**, heaviest first — not by measured
effort, because this skill carries no verified man-day data. Use it to decide where to spend
estimating attention, not as a substitute for estimating.

| Weight | Line item | Why it sits here |
|---|---|---|
| **Heaviest** | **Pseudo-consignment dual-book synchronisation** | custom program + reconciliation report + support runbook, and it is never configuration |
| | **The integration estate as a whole** (~25 touchpoints) | the happy path is quick; error contract, retry, duplicate protection and reconciliation are the work |
| | **Promotion and discount mechanics** | priced as configuration, delivered as development, almost every time |
| | **Data migration of open balances** | open orders, consignment stock at retailers, in-transit stock, open deductions, returns in flight |
| **Heavy** | **Statutory document formats** | each preprinted variant is a report customisation, and they are non-negotiable |
| | **Marketplace gateway** (build or buy) | one-off, then cheap per platform — but the first one is real |
| | **Item master and variant handling** | style × colour × size, plus barcode and external-reference cross-mapping |
| | **Transformation / outside processing** | own master data, own location, own cost mechanism |
| **Moderate** | **Per-location inventory valuation or stock-value ceilings** | custom, and often discovered late |
| | **Ageing, movement-class and dead-stock reporting** | custom in the reference implementation, not standard |
| | **Treasury** — bank reconciliation, cheque handling, withholding-tax payment splitting | a workstream, not a payables add-on |
| | **Budget commitment/obligation/actual reporting and carry-forward** | both were gaps |
| **Lighter, but never zero** | additional channels beyond the first two of a given type · additional point-of-sale or 3PL instances · reason-code and reference-data setup | each is small; the count is what bites |

Treat each of these as an explicit line item, not a rounding allowance:

- Both consignment models in scope → dual-book sync **plus** reconciliation **plus** a support runbook
- More than two marketplaces, or an intent to add more → gateway build or buy decision
- Cash on delivery at volume → courier receivable and remittance reconciliation
- Per-location or per-shop stock valuation → costing-grain decision with reporting consequences
- Decoration or personalisation as routine → transformation module, outside location, cost mechanism
- Statutory preprinted document formats → each variant is a report customisation
- Electronic tax filing through a service provider → a file interface plus its failure handling
- Tiered pricing or discount approval expected **inside** the ERP → not free if the ERP holds base price only
- Milestone or progress billing on projects → not present in a standard order-to-cash design
- Several point-of-sale products or several 3PLs → multiply the interface count, not the effort per interface
- Channel count discovered during design → the reference implementation went from ~6 assumed to 15 actual

## Tells — recognise the situation fast

| If you hear... | You are probably looking at... |
|---|---|
| "we sell into the mall" | two different channels being conflated — ask the ownership question |
| "the stock report never matches" | consignment or store counts without a count discipline |
| "finance rekeys it into a spreadsheet at month end" | a missing reconciliation, usually settlement or sale-out |
| "we just add a line for the printing" | transformation being handled outside the item master |
| "the platform pays us net" | many-to-one cash application that nobody has designed |
| "sales decide the discount" | pricing governance living outside the ERP |
| "every store request becomes its own delivery" | fulfilment consolidation missing |
| "we'll do EDI with them" | a purchase-order-only interface being described as EDI |

## Questions that earn credibility in the first meeting

1. When your goods sit on a retailer's shelf, when must you issue the tax invoice — on delivery, or when the shopper buys?
2. For each channel: who pays you, and when do you consider the sale complete?
3. Does anyone rely on stock value per shop?
4. When you decorate a blank, does it become a new product code?
5. What stops two channels selling the same unit?
6. Who can release a customer who is over their credit limit, and where is that decision recorded?
7. How do you decide when to mark down?

Asking any of these before quoting separates a consultant from a vendor.
