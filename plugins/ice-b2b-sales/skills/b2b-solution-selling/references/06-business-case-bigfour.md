# Reference 06 — Quantified Business Case (ROI / NPV / SCQA / Big Four Frameworks)

**Use when:** The deal needs board-grade financial justification. CFO has asked for a paper. Procurement is pushing back on price. Champion needs ammunition for the steering committee. Internal investment committee needs a defensible IRR.

This reference fuses the financial core (ROI / NPV / IRR / Payback / Sensitivity) with the consulting communication frameworks (SCQA, Pyramid Principle, MECE, Issue Tree) that Big Four (McKinsey, BCG, Deloitte, KPMG, PwC) use to make those numbers persuasive.

---

## A. The four numbers every CFO will check

A business case without these four numbers will not survive a serious finance review.

### 1. ROI (Return on Investment)
```
ROI = (Net Benefit / Total Investment) × 100%
```
- Simple, intuitive — but **time-blind** (year 1 ROI = year 5 ROI in this formula)
- Use as a headline; never as the only metric
- Typical hurdle in Thailand enterprise software: ROI ≥ 150% over 3 years

### 2. NPV (Net Present Value)
```
NPV = Σ [ Cash Flow_t / (1 + r)^t ] for t = 0 to N
```
- Discounts future benefits by the cost of capital (r)
- Standard discount rates: Thai blue-chip 8–10%; mid-market 10–12%; SOE 6–8% (TGB rate); start-up / risky 15–20%
- Decision rule: **NPV > 0 → accept**; NPV > similar projects → prefer

### 3. IRR (Internal Rate of Return)
```
IRR = the discount rate r at which NPV = 0
```
- The "implicit return" of the project
- Decision rule: **IRR > company's cost of capital (WACC)** → accept
- Useful for comparing projects of different sizes

### 4. Payback Period
```
Payback = Years until cumulative Net Cash Flow ≥ 0
```
- Risk-mitigation lens: how long is the company exposed before recovering the investment?
- Thai enterprise software typical hurdle: payback ≤ 24 months for digital transformation, ≤ 36 months for ERP

**Always show all four.** A deal with high NPV but 5-year payback may fail risk review even if NPV-positive.

## B. The benefit categories — quantify each

A defensible business case decomposes benefits into 4–6 clearly named buckets. Each bucket has its own assumption set and sensitivity range.

| Category | Examples | How to quantify |
|---|---|---|
| **Direct cost reduction** | Headcount avoided, license consolidation, infrastructure savings | FTE × fully-loaded cost; THB/year of legacy maintenance avoided |
| **Productivity gain** | Hours saved × FTE × loaded rate | Be conservative — assume only 50–70% of "saved" time is redeployed productively |
| **Revenue uplift** | Faster quote-to-cash, churn reduction, expansion revenue | Hardest to defend — always show low/base/high; use customer-validated data |
| **Working capital release** | DSO reduction, inventory turns, AP optimisation | (Days improved / 365) × Revenue × cost of capital |
| **Risk avoidance** | Audit findings, regulatory penalty, security breach | Probability × magnitude — show the math, do not over-claim |
| **Strategic optionality** | Speed to launch new business, ability to acquire and integrate | Hardest to quantify — narrative + a placeholder THB number |

**Rule:** Every benefit must trace to (a) the Pain Sheet, (b) a metric the EB cares about, and (c) a customer-validated source (their own number, not yours).

## C. The three-scenario sensitivity table (mandatory)

CFOs trust models that admit their fragility. Deliver every business case with three columns:

| Driver | Worst case | Base case | Best case |
|---|---|---|---|
| User adoption rate | 50% | 75% | 90% |
| Headcount avoidance | 5 FTE | 8 FTE | 12 FTE |
| Working capital improvement | 5 days | 10 days | 15 days |
| Maintenance cost saved | THB 30M | THB 50M | THB 70M |
| **Total NPV (3yr, 10% disc.)** | **THB 80M** | **THB 180M** | **THB 320M** |
| **Payback (months)** | **30** | **18** | **12** |
| **IRR** | **22%** | **45%** | **78%** |

**The discipline:**
- Worst case must still be NPV-positive — otherwise the project is too risky
- Base case is the number you commit to in the proposal
- Best case is the upside narrative for the EB

Then **name the three assumptions that move the answer most** (e.g., "user adoption", "headcount avoidance", "go-live date"). These are the assumptions the seller must defend in the business case meeting — and the ones the customer will sandbag in negotiation.

## D. The cost-of-status-quo lens (often more persuasive than ROI)

Many CFOs do not approve projects because of the ROI. They approve them because of the **cost of doing nothing**, which is often invisible until you make it visible.

| Cost-of-status-quo bucket | Example |
|---|---|
| Compounding inefficiency | "Manual close costs THB 13M/year now and will grow ~10% annually as transaction volume grows." |
| Audit / regulatory exposure | "Two years of segregation-of-duties findings; year three triggers Big Four auditor escalation, est. THB 8M premium." |
| Missed opportunities | "Cannot acquire the next entity without 6 months of IT integration; one missed deal pipeline = THB 200M revenue." |
| Talent risk | "Group Controller has resigned twice; replacement market premium is THB 2.5M/year." |
| Customer / market risk | "Competitor launched real-time visibility; we will lose 2 tier-1 retail customers within 18 months without it." |

The status-quo number plus the project investment together = the "do nothing" cost. The CFO compares this to the project NPV. Often the status-quo cost alone justifies the project before a single project benefit is counted.

## E. SCQA — the executive-summary framework

McKinsey's standard frame for any board paper, executive memo, or one-page summary. Mandatory at the top of every business case.

| Element | What it does | Example |
|---|---|---|
| **S — Situation** | What the audience already knows and agrees with | "Our finance close has slipped from 12 to 18 days over 3 quarters, costing ~THB 13M/year and triggering 2 audit findings." |
| **C — Complication** | What changed; the source of tension | "Q3 board has placed Group Controller's tenure under review; Q4 audit committee wants a remediation plan with a deadline." |
| **Q — Question** | The decision the audience must make | "Do we adopt cloud-based finance consolidation now, or remediate in-house over 18 months?" |
| **A — Answer** | The 1-sentence recommendation | "Adopt Oracle Cloud Financials in a 9-month phased programme starting Q1 FY27 — NPV THB 180M, payback 18 months, addresses both audit findings within 12 months." |

The SCQA goes at the top of the deck, the top of the memo, and the top of the email to the EB. Everything below it justifies the *A*.

## F. The Pyramid Principle (Minto) — structuring the rest of the case

Below the SCQA, every supporting argument should be:

- **Top-down**: lead with the answer, then justify
- **MECE**: Mutually Exclusive, Collectively Exhaustive — no overlaps, no gaps
- **Grouped in threes**: humans process 3 grouped arguments easily; 7+ overwhelms

**Example pyramid for "Adopt Oracle Cloud Financials":**

```
ANSWER: Adopt Oracle Cloud Financials in 9-month phased programme

  Argument 1: Resolves the regulatory exposure
    - Closes both audit findings within 12 months (Sub-evidence)
    - Provides automated SoD controls (Sub-evidence)
    - Generates audit-ready trails reducing audit fees by ~15% (Sub-evidence)

  Argument 2: Delivers committed financial outcomes
    - NPV THB 180M base, THB 80M worst (Sub-evidence)
    - Payback 18 months base, 30 worst (Sub-evidence)
    - 4 of 5 Thai listed peers chose this same path (Sub-evidence)

  Argument 3: Manages execution risk
    - Phased: GL/AP first, consolidation phase 2 (Sub-evidence)
    - Big Four implementation partner with 6 Thai references (Sub-evidence)
    - Executive steering with monthly board read-out (Sub-evidence)
```

## G. MECE — the test that separates analyst from manager

Whenever you list anything (drivers, benefits, risks, options), apply MECE:

- **Mutually Exclusive**: no two items overlap (no double-counting benefits)
- **Collectively Exhaustive**: nothing missing the audience could ask about

**MECE test for a benefits list:**
- Direct cost reduction ✓
- Productivity gain ✓ (does not overlap; redeployed time, not avoided cost)
- Working capital ✓
- Risk avoidance ✓
- Revenue uplift ✓
- Strategic optionality ✓

Now ask: "What did I miss?" If the audience can name a benefit not on this list, you have failed Collectively Exhaustive — and your number is wrong.

## H. The 7S / Issue Tree for diagnostic problems

When the customer says "we are not sure what the problem is," use McKinsey's **Issue Tree** (or BCG's **Issue Map**) to decompose:

```
TOP ISSUE: Why is our finance function under-performing?

  Branch 1: People & skills
    - Sub: Talent retention
    - Sub: Training
    - Sub: Org design

  Branch 2: Process & policy
    - Sub: Close process
    - Sub: Reconciliation policy
    - Sub: Approval matrix

  Branch 3: Systems & data
    - Sub: ERP fragmentation
    - Sub: Data quality
    - Sub: Integration / reporting layer
```

Then prioritise branches by impact × ease, and propose to address the top 1–2 with your solution. This positions you as a diagnostic advisor, not a software vendor.

## I. Output-format guidance

When the user asks for a business case, deliver:

1. **A 1-page SCQA executive summary** at the top — Situation, Complication, Question, Answer (single page, no exceptions)
2. **The four headline numbers** prominently: NPV (3yr at 10%), IRR, Payback, ROI
3. **A benefit decomposition table** — by category, with quantification, source, and confidence level (high/medium/low)
4. **A three-scenario sensitivity table** — worst / base / best, with the 3 most-sensitive assumptions named
5. **A cost-of-status-quo section** — what does "do nothing" cost over 3 years
6. **A risk register** — top 5 risks, mitigations, residual risk owner
7. **A MECE-tested options comparison** if relevant (e.g., Oracle vs SAP vs status quo) — same axes, same time horizon, same discount rate
8. **An implementation summary** — phases, costs by phase, who owns what

Then offer the next component: "Want me to convert this into a board paper, or build the Champion enablement pack so your sponsor can defend this in committee?"

## J. Output template (copy and fill)

```
=== EXECUTIVE SUMMARY (SCQA) ===
SITUATION: ...
COMPLICATION: ...
QUESTION: ...
ANSWER: ...

=== HEADLINE NUMBERS ===
3-Year NPV (10% disc.):    THB ___M
IRR:                        ___%
Payback:                    ___ months
3-Year ROI:                 ___%
Discount rate assumption:   ___%

=== BENEFIT DECOMPOSITION ===
Category             | Year 1   | Year 2   | Year 3   | 3-yr Total | Confidence
---------------------|----------|----------|----------|------------|----------
Cost reduction       | THB __M  | THB __M  | THB __M  | THB __M    | High
Productivity gain    | THB __M  | THB __M  | THB __M  | THB __M    | Medium
Working capital      | THB __M  | THB __M  | THB __M  | THB __M    | Medium
Risk avoidance       | THB __M  | THB __M  | THB __M  | THB __M    | Low
Revenue uplift       | THB __M  | THB __M  | THB __M  | THB __M    | Low
TOTAL BENEFITS       | THB __M  | THB __M  | THB __M  | THB __M    |

=== INVESTMENT ===
Software / subscription:    THB __M (Y1) + THB __M/yr ongoing
Implementation services:    THB __M
Internal effort (capitalised): THB __M
Change management:          THB __M
TOTAL 3-YEAR INVESTMENT:    THB __M

=== SENSITIVITY ===
                       | Worst    | Base     | Best
NPV                    | THB __M  | THB __M  | THB __M
Payback (months)       | __       | __       | __
IRR                    | __%      | __%      | __%
TOP 3 SENSITIVITIES (assumptions that move the answer most):
  1. ...
  2. ...
  3. ...

=== COST OF STATUS QUO (3 years) ===
Compounding inefficiency:   THB __M
Audit / regulatory exposure: THB __M
Missed opportunity:         THB __M
Talent / customer / market: THB __M
TOTAL DO-NOTHING COST:      THB __M

=== TOP 5 RISKS ===
Risk | Probability | Impact | Mitigation | Residual Owner
1. ...

=== RECOMMENDATION ===
[1 sentence — repeat the SCQA Answer]
```

## K. Common failure modes

- **NPV with no discount rate stated.** Specify it; CFOs check.
- **No sensitivity.** A point estimate looks naive. Three scenarios with named assumptions look professional.
- **Benefits not in customer's words.** Use their cost categories, not the vendor brochure's.
- **Productivity gain at 100% redeployment.** No CFO believes "saved" time turns into 100% useful work; haircut to 50–70%.
- **Risk avoidance with no probability.** "Avoided audit penalty THB 50M" without "× 30% probability" is fiction.
- **No status-quo number.** The most persuasive piece of the case; never omit.
- **Pyramid violated** — 8 supporting points, no grouping. Force into 3 themes.
- **SCQA missing** — buried lead. Audience reads first 30 seconds; they should see Situation → Answer in that window.
