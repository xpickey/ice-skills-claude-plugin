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

## Van sales — the first question is the document on the vehicle

> A rep sells from a loaded vehicle, hands the goods over and takes the money in one visit. The tax
> point is therefore **on the vehicle, at the stop** — which raises a question the source material
> does not answer and you must not answer for the client.

**Ask before anything else:** *"When your rep sells at the shop, what document does the customer
walk away with — and where does its number come from?"*

| What you need to establish | Why it decides the design |
|---|---|
| Is a tax invoice or a receipt issued **at the stop**, or raised later at the office? | one is a mobile printing and numbering problem, the other is a settlement-time posting problem |
| **Where does the running number come from** — a book held on the van, a range allocated to the vehicle, or the ERP on sync? | number-range control per vehicle is a build; a shared range across an offline fleet is a duplicate waiting to happen |
| What happens to the number when the device is offline all day? | this is where offline-first designs break |

**Three rules that hold once the document question is settled:**

- **Van stock is relieved at settlement, not at the sale.** The mobile device decrements van
  inventory live; the ledger moves at the end-of-shift close. Say so before a client assumes
  same-day posting, and present the posting delay as the fraud-detection window it is.
- **Van receivable must not be merged with modern-trade receivable.** Modern trade is dominated by
  deductions and disputes; van is many small balances against many small shops with a limit each.
  Merging them destroys both collections and dispute handling.
- **Establish the route model before estimating** — cash van (sell from stock, settle in one visit)
  or pre-sales (order on one call, deliver on another). A client running **both** needs two route
  calendars, two stock-ownership rules and two revenue-recognition points.

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

## The trade agreement is evidence, not paperwork — two reasons, same requirement

> **Keep the agreement versioned and amendment-tracked, and be able to reproduce the version that was
> in force on any given date.**

| Why it matters | Where it comes from |
|---|---|
| **Dispute defence** — the approved promotion or agreement *as it stood on the deduction date* is what you argue with. A system that cannot reproduce that version cannot defend the claim | file **10**, stage 5 |
| **Thai compliance** — competition guidance on retailer charges requires a **written agreement made in advance**, and treats a charge beyond what the contract states as unfair. The system is how the supplier evidences that | file **17**, section 1 |

Two independent reasons landing on one design decision. That is a stronger argument than "the auditor
will like it", and it is the line to use when a client pushes back on the cost of versioning.

## Trade spend — the three questions that win the meeting

1. *"When a retailer short-pays you, how long before you know why — and what share do you never explain?"*
2. *"Do you know your margin **after** back-margin, by retailer? Can you show me by item?"*
3. *"When you cross a volume tier that re-rates retrospectively, how does that reach your accounts?"*

**The line that lands:** a brand can win the listing, hit the volume target, and still lose money on
that retailer — and gross-margin reporting will not reveal it until the year is over.

### Rebate component — five attributes, not one type

| Attribute | Options | Why it changes the build |
|---|---|---|
| Basis | sell-**in** / sell-**through** | sell-through needs a point-of-sale feed from the retailer |
| Scope — **product** axis | whole turnover / basket / item | what qualifies |
| Scope — **customer** axis | group / banner / store cluster | **the axis home-grown designs omit** — and the reason group and banner deals double-count |
| Mechanic | **retroactive** / incremental / **prospective** | three values, not two — see below |
| Settlement | on-invoice / off-invoice / net-bill / credit note / **unilateral deduction** | different tax treatment, and largely **the retailer's choice, not the brand's** |

### Rebate mechanic — three values, and the third is a different accounting model

| Mechanic | What happens commercially | What it means for the design |
|---|---|---|
| **Retroactive** | crossing a tier re-rates everything from the start of the period | a catch-up charge at the moment of crossing, not a rounding difference. Accounted as **variable consideration** — estimated and constrained |
| **Incremental** | the new rate applies only above the threshold | the straightforward case, and the one most designs assume is the only one |
| **Prospective** | the benefit earned now applies to **future** purchases | published guidance treats it as a **customer option**, potentially deferred rather than accrued. **Not a different rate — a different model** |

**The discovery question that finds the third one:** *"Are any of your rebates earned now but applied
to future purchases?"* Almost nobody volunteers this, and a design built on two mechanics cannot
absorb it later without reworking the accrual history.

**And estimation is a decision, not a default.** Where the outcome is not yet known, the choice
between an **expected-value** and a **most-likely-amount** approach is made per contract, the
estimate is constrained so revenue is not recognised where a significant reversal is likely, and it
is reassessed at each reporting date. Accruing at the current rate and truing up periodically
satisfies the arithmetic but not the requirement. **Confirm any standard or paragraph citation with
the client's auditor before it goes in a document — this skill does not assert them.**

### Net GP waterfall — and the two placement rules

```
Gross revenue − COGS = CM1 − trade deductions = CM2 − fulfilment cost = CM3 (Net GP)
```
- Show **Net GP margin % and trade-spend ratio together**. Either alone misleads.
- **Delivery-performance penalties sit in fulfilment cost, not in trade deductions** — a
  management-reporting judgement to settle with the accounting-policy owner before build; their tax
  and accounting classification is a separate, unsettled question (file 17). They are your
  operational failure, not commercial investment. Mixing them distorts the trade-spend ratio.
- **Freeze and version the snapshot at close**, or late debit memos silently restate a closed period.

### Deduction handling — the four non-negotiables

single front door for all three arrival channels · confidence score + **per-retailer** tolerance ·
**double-dip block** (same entitlement settled twice — by credit note *and* by deduction) · split
allocation both ways. **Unmatched = leakage; the match rate is the metric.**

### Dispute — the loss that is entirely avoidable

Register each retailer's **submission window, accepted codes, required formats**. Count down, warn
before expiry, **gate submission on evidence completeness**. Capture proof of delivery **within a
day of despatch**, not when the dispute starts. Missing the window is a permanent loss.

### Settling a Thai rebate — the assumption that is probably wrong

> Most designs assume a volume rebate is settled by issuing a tax credit note (ใบลดหนี้). Thai
> guidance points the other way, and the consequence is structural rather than cosmetic.

The reasoning to carry in your head: a **conditional** discount is not a discount given at the time
of sale, so it sits inside the VAT base at the time of sale — and the events that permit a tax
credit note are a closed list. A rebate earned on cumulative volume is therefore likely **not a
credit-note event at all**, leaving a **commercial credit note carrying no VAT**.

| Design consequence | What to do about it |
|---|---|
| **Two document types are needed**, not one | tax credit note for qualifying events, commercial credit note without VAT for conditional rebates — **separate numbering series**, separate templates |
| Discount **at the moment of sale** behaves differently from a rebate **settled later** | this is the on-invoice versus off-invoice distinction, and in Thailand the gap is a tax-character gap, not a timing one |
| Routing all trade spend through tax credit notes | produces VAT that does not reconcile to the periodic return — and a year of postings to unpick |

**How to say it, and where to stop.** Raise it as a design question with a known shape: *"Which of
your rebate structures can be settled by tax credit note, and which need a commercial credit note?
That is a question for your tax adviser, and we will build for both answers."* **Never rule on a
specific structure.** The question list is in file **17**; handing it over is itself a credibility
signal, because most competitors assume instead.

### Which reporting framework the client uses changes the scope

> Ask this **before** sizing the trade-spend accrual work. It can move the estimate materially in
> either direction, and it is invisible if you do not ask.

| If the client reports under... | Then the accrual scope... |
|---|---|
| the **full standard** (the Thai equivalent of the international revenue standard is a direct translation, with no local modification on consideration payable to a customer) | includes **estimation method, constraint and reassessment at each reporting date** — the machinery in the mechanic table above |
| the framework for **entities without public accountability** (กิจการที่ไม่มีส่วนได้เสียสาธารณะ) | is materially lighter — that framework measures revenue net of trade and volume discounts only and carries **no variable-consideration concept**, which the professional body itself identifies as a point of difference |

**The question:** *"Which financial reporting framework do you report under — and is that expected to
change?"* A group planning to move up, or one with a subsidiary on each, is scoping for both.

## "We already have EDI" — decide which of three things they mean

| They mean | Tell | ERP scope |
|---|---|---|
| **Portal-only** | someone opens a supplier portal and re-keys into the ERP | zero integration built — **and the pain they hired you for is still there** |
| **Bureau-integrated** | the ERP exchanges with one EDI service provider who fans out to every retailer | **one** interface + per-retailer configuration ← usually the right proposal |
| **Direct to retailer** | the ERP connects to each chain separately | **one interface per retailer**, forever, plus maintenance |

**The question that separates them:** *"Does that exchange touch your ERP, or does someone key it in
from a screen?"*

Thai market reality: bureau Web EDI covering the major chains exists and supports **six document
types** — purchase order · invoice · advance ship notice · credit note request · remittance advice ·
return to vendor. **Coverage is per retailer and per document, not one yes or no.** Never quote
"Thai modern trade is purchase-order-only" as a fact — verify per account.

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
| | **Rebate hierarchy cascade across both axes without double-counting** | the hardest single piece of a trade-spend build, and custom in most products |
| | **The integration estate as a whole** (~25 touchpoints) | the happy path is quick; error contract, retry, duplicate protection and reconciliation are the work |
| | **Van sales — van inventory, offline-first capture and the settlement close** | a van-inventory record most products lack natively, a specialised mobile product, and a settlement screen with segregation of duties |
| | **Promotion and discount mechanics** | priced as configuration, delivered as development, almost every time |
| | **Data migration of open balances** | open orders, consignment stock at retailers, in-transit stock, open deductions, returns in flight |
| **Heavy** | **Statutory document formats** | each preprinted variant is a report customisation, and they are non-negotiable |
| | **Marketplace gateway** (build or buy) | one-off, then cheap per platform — but the first one is real |
| | **Item master and variant handling** | style × colour × size, plus barcode and external-reference cross-mapping |
| | **Transformation / outside processing** | own master data, own location, own cost mechanism |
| **Heavy** | **Investment-promotion segregation**, where the client is promoted | valuation-layer segregation of duty-exempt stock, document-level tagging before posting, and governed common-cost allocation |
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
| "we'll do EDI with them" | a portal someone re-keys from, being described as EDI |

## Questions that earn credibility in the first meeting

1. When your goods sit on a retailer's shelf, when must you issue the tax invoice — on delivery, or when the shopper buys?
2. For each channel: who pays you, and when do you consider the sale complete?
3. Does anyone rely on stock value per shop?
4. When you decorate a blank, does it become a new product code?
5. What stops two channels selling the same unit?
6. Who can release a customer who is over their credit limit, and where is that decision recorded?
7. How do you decide when to mark down?

Asking any of these before quoting separates a consultant from a vendor.
