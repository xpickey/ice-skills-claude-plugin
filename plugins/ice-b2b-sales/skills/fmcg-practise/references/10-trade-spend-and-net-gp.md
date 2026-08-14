# 10 — Trade Spend and Net GP (การบริหารค่าใช้จ่ายช่องทางและกำไรสุทธิรายห้าง)

> **Load this when:** the conversation is about **what the retailer takes back** — listing fees,
> rebates, promotions, scanbacks, deductions, chargebacks, disputes, accruals — or when anyone asks
> which retailer or which promotion is actually profitable.
> **Do not load this for:** how modern trade *sells* → **02** · consignment mechanics → **03** ·
> what a *marketplace platform* deducts → **06**, which uses the same discipline on a different
> counterparty.
> **Source basis:** the food and beverage implementation, whose solution design covers this domain
> across fifteen screens traced to a documented requirement set — the deepest single source in this
> skill. Reinforced by published accounting guidance and practitioner sources for the areas that
> implementation did not reach. **Every figure in both is marked illustrative by its own authors;
> this file therefore carries no numbers.**

## 1. Use cases — why this is the hardest money in consumer goods

A brand invoices a retailer at gross. It never receives gross. Between the invoice and the bank sits
a layer of listing fees, promotional support, volume rebates, growth incentives, compliance
penalties, delivery-performance penalties and unexplained short-payments.

**The defining behaviour: retailers deduct first and explain later — or never.** A retailer does not
invoice for its trade support. It **short-pays** and leaves the supplier to work out why. The money
lost in the gross-to-net gap arrives through three unconnected routes — the remittance advice
attached to the payment, the retailer's supplier portal, and the bank statement where a payment
simply lands smaller than expected.

With no single place to collect them, commercial and receivables teams cannot keep up and reported
margin per retailer stops being true. That is the business case for everything below.

### The three money streams, which are commonly confused

| Stream | What it is | Who initiates |
|---|---|---|
| **Conditional trade spend** | rebates earned by achieving volume, growth or a margin guarantee | earned by performance |
| **Unconditional fees** | listing and slotting, new-store opening, shelf and display space, marketing development funds, free fill | **charged by the retailer regardless of performance** |
| **Penalties** | compliance and delivery-performance charges | **deducted unilaterally by the retailer** |

**These are three different families, not three flavours of one thing.** The rebate component model
in section 2 covers the first. The second is a separate accounting question — a large up-front
payment can be capitalised and amortised or recognised immediately, and that choice follows the
substance of what was received, not company policy. The third is a cost stream that the reference
implementation did not carry at all.

### Who pays attention to this

The commercial controller who cannot explain last quarter's margin · the key-account manager
negotiating next year's terms without knowing what this year cost · the receivables team carrying
unexplained residue · and the finance director who wants Net GP by retailer and has been told it
will take three weeks to produce.

## 2. Process — the eight stages

```
[Master setup]        [Deal setup]         [Operate]          [Reconcile]              [Report]
Retailer/banner  →  Trade agreement  →  Promotion &    →  Deduction intake      →  Net GP waterfall
master              Rebate builder      scanback          Matching engine          Analytics
                    Budget checkbook    Accrual          Dispute + portal
                                        Evidence/POD      Tax treatment
                                                          AR application/suspense
```

Every stage is a place money leaks if it is missing. A scope covering only the first two is scoping
a system that cannot answer the question the finance director asked.

### Stage 1 — Retailer and banner master

The **banner** — an individual chain, as distinct from the group that owns it — is the dimension
every downstream transaction carries. Two requirements are cheap now and expensive to retrofit:
a **parent group above the banner**, so exposure and negotiating position are visible per group; and
**effective-dated re-mapping**, so a banner moving between groups does not silently restate prior
periods.

### Stage 2 — Trade agreement and rebate decomposition

The **trade agreement** is the annual contract as a header with lines — minimum buying quantity,
tier structure, mandatory promotion commitments, shelf obligations, delivery-performance terms,
payment terms. **Versioned and amendment-tracked**, because the agreement as it stood on a given
date is the evidence for the tax and revenue treatment that followed — and, as stage 4 shows, for
disputing a deduction.

**A trade deal is not one lump sum.** Held as one, it cannot be accrued correctly, matched to a
deduction, or evaluated. It decomposes into **rebate components**:

| Component type | Mechanism |
|---|---|
| Fixed per unit | an agreed amount per case or unit sold |
| Flat percentage | a straight percentage of turnover |
| Tiered | rate steps as volume crosses thresholds |
| Growth | earned only on growth against a base period |
| Gross-profit guarantee | the brand underwrites the retailer's margin; shortfall clawed back |

Each component carries independent attributes. **The combination, not the type, is what makes the
calculation:**

| Attribute | Values | Why it matters |
|---|---|---|
| **Basis** | sell-**in** · sell-**through** | sell-through needs a point-of-sale feed from the retailer |
| **Scope — product axis** | whole turnover · basket · item | what qualifies |
| **Scope — customer axis** | group · banner · store cluster | **the axis most home-grown designs omit** |
| **Mechanic** | **retroactive** · **incremental** · **prospective** | three values, not two — see below |
| **Settlement** | on-invoice · off-invoice · net-bill · credit note · **unilateral deduction** | largely **the retailer's choice, not the brand's** |

**Scope is two-dimensional.** Industry practice attaches an agreement at any node of a **customer
hierarchy × product hierarchy** matrix and cascades downward. This is where self-built designs break:
a group-level rebate and a banner-level rebate on the same item must both apply and **must not
double-count**. A single product-axis scope cannot express that.

**The mechanic has three values, and they are not three shades of one idea:**

- **Retroactive** — crossing a tier re-rates everything from the start of the period. Creates a
  catch-up charge the moment the threshold is crossed. Accounting-wise this is **variable
  consideration**, estimated and constrained.
- **Incremental** — the new rate applies only above the threshold.
- **Prospective** — the earned benefit applies to *future* purchases. Published guidance treats this
  as a **customer option**, which may be a material right and therefore deferred rather than
  accrued. **This is a different accounting model, not a different rate.**

Getting the mechanic wrong is not a rounding difference; it puts the amount in the wrong period and
sometimes on the wrong line.

**Estimation is a decision, not a default.** Where the outcome is not yet known, published guidance
requires choosing between an **expected-value** and a **most-likely-amount** approach per contract —
and it is explicit that this is not a free choice. It also requires **constraining** the estimate so
that revenue is not recognised where a significant reversal is likely, and **reassessing at each
reporting date**. A design that simply accrues at the current rate and trues up quarterly satisfies
the arithmetic but not the standard.

> ⚠ Paragraph references in published summaries could not be verified against the standard itself
> during research. **Confirm any citation with the client's auditor before putting it in a
> document.** The structure above is sound; the paragraph numbers are not this skill's to assert.

### Stage 3 — Budget checkbook

Trade spend is controlled on a grid of **retailer × month × programme type**, in three layers:
**Budget → Commit → Available**. Budget is approved; commit is claimed by deals and promotions;
available is what remains. **Accrual is a subset of commit, not an addition** — get that wrong and
every consumption figure double-counts. Over-commitment is blocked at a threshold and released by an
approver whose seniority rises with the amount. Budgets are versioned so a re-forecast does not
erase the plan.

### Stage 4 — Promotion, scanback and proof of performance

A **scanback** pays per unit actually scanned at the till rather than as an up-front lump, and is
modelled separately from a billback.

```
promotion recorded before it starts — period, eligible items, rate per unit, EXPECTED VOLUME
  → accrue against expected volume as contra-revenue
  → retailer's point-of-sale scan report arrives, matched to the promotion → ACTUAL
  → variance against forecast checked against tolerance, flagged before it reaches reported margin
  → redemption tracked forecast-versus-actual → accrual TRUED UP or REVERSED within a defined window
```

**The promotion identifier is a shared key with demand planning** (file **13**). The same promotion
drives a trade-spend accrual and a forecast uplift; if the two systems hold different promotion
records, the sell-through used to settle the scanback will not match the one used to forecast, and
both become unreliable. **One promotion master, consumed twice. One point-of-sale pipeline, serving
both.**

### Stage 5 — Deduction intake, matching and dispute

**Intake — one front door.** Every deduction, whatever route it arrived by, is normalised into one
claim structure: captured, classified, and flagged by document type on arrival. Each retailer's own
reason codes map to an internal set through a maintained table, so downstream logic never learns
each retailer's vocabulary.

**Matching.** Each deduction line is paired against what should support it — an accrual, an
agreement line, a promotion — with four essential behaviours:

| Behaviour | Purpose |
|---|---|
| Confidence score per match | analysts work the doubtful ones, not all of them |
| **Per-retailer** tolerance | variance inside tolerance settles; outside it escalates. Retailers differ in accuracy |
| **Double-dip block** | prevents the same entitlement settling twice — once by credit note and once by deduction |
| Split allocation | one deducted amount across many invoices or promotions, and the reverse |

**Unmatched is leakage.** The match rate is the most useful operational metric in this domain.

**Dispute.** Three things make it work:

1. **Responsibility categorisation** before disputing — supplier, retailer, carrier, or a genuine
   entitlement the supplier had forgotten. Each leads somewhere different. Disputing everything
   damages the relationship; disputing nothing funds the retailer.
2. **A portal registry** holding each retailer's **submission window, accepted codes, required
   document formats and escalation contact**, counting down to expiry and **gating submission on
   evidence completeness**. Windows can be short and differ per retailer. Missing one is a permanent
   loss and the most avoidable in the cycle.
3. **Recovery tracking** — status, ageing, recovery rate and leakage by retailer and programme.

> **The design point that ties stages 2 and 5 together:** *the approved promotion or agreement as it
> stood on the deduction date is the evidence used to dispute.* A system that cannot reconstruct that
> version cannot defend the claim. This is why the trade agreement must be versioned rather than
> simply current — and it is a stronger argument for versioning than "audit likes it".

**Evidence** — proof of delivery, signed transport documents, despatch-notice timestamps, pallet
photographs, delivery time against the agreed window — is captured **within a day of delivery**, not
when a dispute begins. Late or missing evidence is the main reason disputes are lost, and win rates
decline the longer a claim sits.

### Stage 6 — Accrual and true-up

Trade spend is recognised as **contra-revenue** — consideration payable to a customer — at the sales
invoice, once probable and estimable, then reviewed and adjusted so the balance reflects reality
before close. Five events all occur in practice:

| Event | What happens |
|---|---|
| Automatic generation | accrual raised from the invoice and the rate structure |
| Revaluation on tier movement | the retroactive catch-up from stage 2 |
| Reversal | a growth or conditional rebate that will not be achieved is released |
| Termination proration | an item or contract cancelled mid-period is prorated, not left accruing |
| **Variance root-cause** | each difference classified **one-time · structural · controllable** |

That last one turns an accounting routine into management information. "We were out by a lot" is not
useful; "we were out because of a structural rate error on one banner" is.

**Whether a payment reduces revenue or is an expense** turns on whether the brand received a
distinct good or service at fair value in return. Advertising support with evidence of the
advertising may be an expense; a volume rebate is a reduction of revenue. Get the test right rather
than applying one treatment to the whole category.

### Stage 7 — Thai tax treatment

Off-invoice money has a different tax character from a discount on the face of the invoice. Three
lines run in parallel — **withholding tax** on rebates and promotional support · **value added tax
through debit and credit notes**, each with statutory content, timing and a limited validity period
· **electronic tax documents and periodic returns**.

**The base to get right:** the withholding base is the rebate amount **excluding value added tax** —
not the amount after withholding, and not the VAT-inclusive figure. Naming the field carefully
prevents an entire class of error, because the readings sound identical in conversation.

**Four dates, all different, all needed:** invoice date · accrual date · the month the VAT credit
falls in · cash settlement date. A design carrying one date will not reconcile to the periodic
return.

Rates, categories and validity periods are **file 17**, and every one of them is something to confirm
with a tax adviser rather than assert.

### Stage 8 — Receivable application, suspense, and Net GP

A matched, taxed, settled deduction still has to be **applied against the open receivable**.
Deductions apply against **specific open items**, not the customer balance in aggregate; what cannot
be applied goes to a visible, aged **suspense** position with an owner, never a general adjustment;
and suspense write-off has its own approval ladder. Skip this and the ledger fills with unexplained
residue — the condition the project was meant to end.

**Net GP** is reported as a contribution-margin waterfall:

```
  Gross revenue
− Cost of goods sold
= CM1
− Trade deductions accrued
= CM2
− Fulfilment cost
     of which: delivery-performance penalty   ← its own line
= CM3  →  Net GP
```

Sliced by banner and programme, drillable to item, and shown with **two metrics together** — Net GP
margin **and** trade-spend ratio. One without the other misleads: a healthy margin funded by
unsustainable trade spend looks fine on a single number. Alongside it, **promotion return** — spend
percentage against volume-lift percentage — where a ratio below one means the promotion destroyed
value.

Three decisions inside the waterfall:

1. **Delivery-performance penalties belong in fulfilment cost, not trade deductions.** They are the
   brand's operational failure, not commercial investment; mixing them distorts the trade-spend ratio
   and hides the cause. Source documents frequently contradict themselves here — settle it with the
   accounting-policy owner before build.
2. **Freeze and version the snapshot at close.** Late debit memos arrive after close; without a
   frozen snapshot they silently restate a closed period and the figures stop tying to the filed
   return.
3. **Cross-entity consolidation.** Groups sell to the same retailer through several legal entities;
   consolidated Net GP needs the eliminations designed in.

## 3. Functions the system must provide

| # | Function | Why it is needed | Typically standard or custom |
|---|---|---|---|
| 1 | Banner master with parent group and **effective-dated re-mapping** | consolidated exposure; history that survives a re-brand | custom |
| 2 | **Versioned, amendment-tracked trade agreement** header and lines | it is the evidence for tax treatment *and* for disputing deductions | usually custom |
| 3 | **Rebate component builder** — five types × basis × two-axis scope × three mechanics × settlement | a lump sum cannot be accrued, matched or evaluated | custom |
| 4 | **Hierarchy cascade without double-counting** across customer and product axes | group and banner rebates on the same item must both apply, once | custom — the hardest single piece |
| 5 | **Estimation method per contract** (expected value or most likely amount) with a constraint, reassessed each reporting date | required by revenue recognition guidance; quarterly true-up alone does not satisfy it | custom |
| 6 | Unconditional fee handling, with capitalise-and-amortise **or** immediate recognition by substance | listing and space fees are a different family from rebates | standard accounts, deliberate policy |
| 7 | **Budget checkbook** — Budget → Commit → Available, versioned, over-commit blocked | spend control before the money is gone | custom |
| 8 | **Promotion and scanback** with expected volume, point-of-sale matching, variance tolerance, true-up window | scanbacks settle on actual, not plan | custom |
| 9 | **Shared promotion master** with demand planning | one promotion, two consumers; divergence makes both unreliable | integration design |
| 10 | **Deduction intake** normalising three arrival routes, with a retailer code-mapping table | otherwise three separate problems and no period total | custom |
| 11 | **Matching engine** — confidence score, per-retailer tolerance, double-dip block, split allocation | turns raw deductions into explained ones; exposes leakage | custom |
| 12 | **Dispute management with a portal registry** — window countdown, accepted codes, required formats, evidence gate | missed windows are permanent, avoidable losses | custom |
| 13 | **Contemporaneous evidence capture** within a day of delivery, shared with delivery-performance measurement | late evidence loses disputes; measure once, use twice | custom |
| 14 | **Accrual engine** with automatic generation, tier revaluation, reversal, termination proration | five events that all occur in practice | custom |
| 15 | **Variance root-cause classification** — one-time, structural, controllable | makes the variance actionable | custom |
| 16 | Withholding, VAT debit and credit note, and electronic tax document handling with **four separate dates** | reconciliation to the periodic return depends on it | localisation |
| 17 | **Deduction-to-open-item application** with an aged, owned **suspense** position and a write-off ladder | prevents unexplained residue accumulating | standard with deliberate design |
| 18 | **Net GP waterfall** by banner and programme, item-drillable, dual-metric, with **frozen versioned snapshots** | the question the board is actually asking | custom reporting |
| 19 | Cross-entity consolidation with eliminations | groups sell through several entities | standard consolidation, custom mapping |
| 20 | **Approval thresholds in bands** across accrual override, dispute write-off, budget over-commit, suspense write-off, cross-entity elimination | one approver is not governance | configuration |

## 4. Integration touchpoints

| Touchpoint | Direction | Mode | What it carries |
|---|---|---|---|
| Point-of-sale scan report | retailer → ERP | batch, per promotion cycle | scanned units by item and store |
| Sale-out feed | retailer or merchandiser → ERP | batch, daily or weekly | consumption, shared with planning as sell-through |
| Remittance advice | retailer → ERP | batch, per payment | deduction lines with retailer reason codes |
| Retailer portal extract | portal → ERP | batch or manual | deductions and dispute status |
| Bank statement | bank → ERP | batch | the payment that arrived, for the unexplained residue |
| Dispute submission | ERP → retailer portal | often manual | claim plus evidence pack |
| Evidence capture | warehouse and carrier → ERP | event-driven | proof of delivery, timestamps, images |
| Electronic tax documents | ERP → tax service | batch | credit and debit notes, withholding certificates |
| Promotion master | ERP ↔ planning | shared record | one promotion, two consumers |

## 5. Challenges, gaps and improvement areas

| What commonly goes wrong | What the reference implementations did | What a better design looks like |
|---|---|---|
| **Trade spend scoped as "a report"** | the food and beverage design treats it as fifteen screens across six process stages | scope it as its own domain with the twenty functions above |
| **Deduction and dispute lifecycle absent entirely** | **the apparel case had none of it** — the largest single gap between the two references | intake, matching, dispute with portal windows, evidence, recovery tracking |
| **Rebate held as one amount** | decomposed into components | components with basis, two-axis scope, mechanic and settlement |
| **Scope modelled on the product axis only** | product axis only | add the customer-hierarchy axis and solve the double-count |
| **Mechanic modelled as two values** | retroactive and incremental | add **prospective**, and treat it as a different accounting model |
| **Estimation left implicit** | accrue then true up quarterly | choose the estimation approach per contract, constrain it, reassess each reporting date |
| **Unconditional fees treated as rebates** | not carried | separate family; capitalise or expense by substance |
| **Penalties mixed into trade deductions** | source documents contradicted themselves | own line inside fulfilment cost; settle with the policy owner before build |
| **Agreement stored as current, not versioned** | versioned | versioning is what makes disputes defensible, not just auditable |
| **Benchmark figures quoted to clients** | — | **published trade-spend ranges disagree with each other** because the definition of what counts differs. Never present one as the industry standard; ask the client for their own |

## 6. Discovery questions

1. When a retailer short-pays, how long before you know why — and what proportion is never explained? ⚑
2. Do you know your margin **after** everything the retailer takes back, by retailer and by item? ⚑
3. When you cross a volume tier that re-rates retrospectively, how does that reach your accounts? ⚑
4. Are any of your rebates earned now but applied to *future* purchases? ⚑ *(prospective — different accounting)*
5. Do you have rebates agreed at group level and at chain level on the same products? How do you stop them double-counting? ⚑
6. Which fees do you pay regardless of performance — listing, new store, space, marketing funds — and are they inside or outside your trade-spend budget?
7. How do you decide the accrual when you do not yet know which tier you will land in?
8. Where do deductions arrive from — remittance advice, portal, bank statement — and where are they collected?
9. What is each retailer's dispute window, and how do you track it? ⚑
10. When you dispute, can you retrieve the promotion terms **as they stood on the deduction date**? ⚑
11. Who owns unapplied deductions, and how old is the oldest one?
12. Are delivery-performance penalties reported inside trade spend, or separately?

**The observation that lands:** a brand can win the listing, hit the volume target, and still lose
money on that retailer — and gross-margin reporting will not reveal it until the year is over.

## Related files

- **02** modern trade — how the channel sells, and where the deduction begins
- **03** consignment — the other arrangement on the same retailer account
- **06** online — the same reconciliation discipline applied to a platform
- **13** demand planning — the shared promotion master and sell-through data
- **15** the ledger dimensions this reporting depends on
- **17** Thailand — the tax treatment of every item above
- **19** the full discovery bank
