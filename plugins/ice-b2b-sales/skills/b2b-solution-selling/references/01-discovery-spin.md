# Reference 01 — Discovery & SPIN Question Engine

**Use when:** Preparing for any discovery, advancing, or stakeholder-mapping meeting. Building a question set for any role × any product. Reviewing why a previous call did not advance.

---

## A. Pre-call Hypothesis Builder (McKinsey-style)

Walk into every meeting with a falsifiable hypothesis, not an open-ended fishing trip. Capture these inputs first:

| Field | What good looks like |
|---|---|
| Industry & sub-segment | "Thai food-processing exporter, 3 plants, 20% of revenue from Japan / EU markets" |
| Ownership structure | Family-controlled / SET-listed / MNC subsidiary / Government / SOE — each implies a different decision-rights map |
| Top 3 likely business pains (hypothesis) | Specific, in their language, tied to a metric they would name to their board |
| Likely Economic Buyer | Named individual + their KPI |
| Likely Champion candidates | Named individuals + why they would risk their reputation for this deal |
| Compelling event hypothesis | A deadline that forces a decision — regulatory, system EOL, M&A integration, audit finding, board mandate |
| Competitive landscape | Incumbent + 2 likely alternatives + the status quo |
| Two reframe insights to teach | Industry insights the buyer probably does not know — see `04-challenger-pitch.md` |
| Two desired commitments from the call | What does "advance" look like? Next meeting? Access to EB? Data for business case? |

If any field is "I don't know", that is a discovery question for this meeting — name it explicitly.

## B. SPIN Question Sequence (Neil Rackham, Huthwaite)

The four question types must run in order. Skipping straight to "Need-payoff" before establishing Implication is the most common SPIN failure mode.

### S — Situation (use sparingly, 10–20% of call)
Establish basic facts. Burn as few of these as possible — the buyer resents being asked things you could have researched.
- "How many entities are on your current GL?"
- "What is your current month-end close cycle in business days?"
- "Which version of Oracle EBS are you running, and is it on Premier or Sustaining support?"

### P — Problem (20–30% of call)
Explore difficulties, dissatisfactions, and concerns the buyer has *with their current state*.
- "Where does the close take longer than you would like?"
- "What happens when intercompany balances do not match at month-end?"
- "How confident are you in your forecast for next quarter, on a scale of 1–10?"

### I — Implication (30–40% of call — this is where complex deals are won)
Make the problem feel bigger. Quantify the cascade. Move pain from "annoying" to "critical".
- "If close keeps slipping, what does that do to your covenant reporting deadline?"
- "What is the cost — in audit fees, in restatement risk, in CFO credibility — of finding errors three weeks after close?"
- "If forecast accuracy stays at 60%, what does that force you to do with working capital?"
- "When the audit committee sees these control gaps again, what is the conversation with the board?"

### N — Need-payoff (15–25% of call)
Have the buyer articulate the value of solving the problem. The buyer should be selling to themselves.
- "If you could close in 7 days instead of 18, what would your team do with those 11 days?"
- "If forecast accuracy moved from 60% to 95%, how would that change the way Treasury manages the line of credit?"
- "What would board confidence look like if covenant reports were published 5 days ahead of schedule, every quarter?"

## C. SPIN ratio targets

Rackham's research on 35,000+ calls shows the difference between successful and unsuccessful complex sales:

| Call type | Situation | Problem | Implication + Need-payoff |
|---|---|---|---|
| Failed complex sale | 60–70% | 20–30% | <10% (mostly feature dump) |
| Successful complex sale | 10–20% | 25–35% | 50–60% |

If the user's call plan is heavy on Situation, push back.

## D. Question library by role

For each enterprise software buyer role, lead with these starter questions and then layer SPIN.

### CFO
- What does your audit committee push you on each quarter? (problem)
- When you miss a forecast by more than 5%, what is the board conversation? (implication)
- If we could compress your close from 14 to 7 days, what would that unlock for treasury? (need-payoff)

### Controller / Finance Director
- Walk me through the last close. Where did the team work weekends? (problem)
- What is the cost — in turnover, in errors, in audit findings — of those weekends? (implication)
- If reconciliation were automated, where would your team's time go? (need-payoff)

### CIO / IT Director
- Which legacy systems are out of support or about to be? (situation → problem)
- What is the cost of running Oracle EBS on Sustaining Support? Of recruiting EBS DBAs in Bangkok today? (implication)
- If you could redirect 2 FTE from keep-the-lights-on to value work, what would they build first? (need-payoff)

### COO / Supply Chain Head
- How fast can you re-plan production when a major customer changes their forecast? (problem)
- When that re-plan takes a week instead of a day, what is the customer impact? The inventory impact? (implication)
- If demand-driven planning gave you a 24-hour replan, what would that mean for service levels? (need-payoff)

### Head of Procurement (especially Thai government / SOE)
- What does your Procurement Act 2560 audit look like in this category? (problem)
- When สตง. flags a deviation, what happens to the project owner? (implication)
- If TOR scoring were defensible end-to-end, how much faster would the committee approve? (need-payoff)

## E. Question library by product domain

Use these as starter packs — adapt to the buyer's actual situation.

### Oracle Cloud ERP / SAP S/4HANA / NetSuite (Financials)
- Close cycle, intercompany matching, multi-entity consolidation, FX translation, GL fragmentation, audit control gaps, manual journal volume, forecast accuracy.

### Oracle EPM / SAP Analytics Cloud / Anaplan (EPM / Planning)
- Budgeting cycle length, scenario modelling capability, driver-based forecasting, rolling forecast adoption, board reporting lead time, what-if speed.

### SCM / Supply Chain
- Demand forecast accuracy, on-time-in-full %, inventory turns, days inventory outstanding, supplier collaboration, sales & operations planning cadence.

### HCM / Workforce
- Time-to-hire, payroll error rate, performance review compliance, retention by role, talent pipeline, total cost of workforce.

### Industry / Custom (FinTech / GovTech / Healthcare)
- Sector-specific compliance burden, regulator reporting cycles, customer experience metrics, transaction volumes, fraud / risk indicators.

## F. Anti-patterns to screen out before the call

- **Too many situation questions** — buyer disengages within 15 minutes
- **Premature feature dump** — "Let me show you our solution" before pain is admitted
- **Unearned benefit statement** — "This will save you 50%" before the buyer has agreed there is a problem worth 50% of anything
- **Single-thread call** — only one buyer attends; you have learned nothing about the buying centre
- **No commitment ask** — call ends without a clear next step; deal stalls in pipeline

## G. Call planning template (copy this and fill in)

```
ACCOUNT: [name + entity]
MEETING: [date, attendees, role of each]
HYPOTHESIS: [3 likely pains, in their language]
COMPELLING EVENT HYPOTHESIS: [the deadline that forces a decision]
DESIRED OUTCOMES (commitments to ask for):
  1. [primary]
  2. [fallback]
SPIN PLAN:
  Situation (max 3): ...
  Problem (3–5): ...
  Implication (4–6 — these are the work): ...
  Need-payoff (2–3): ...
TWO REFRAME INSIGHTS TO TEACH:
  1. ...
  2. ...
RISK / DERAILER WATCH:
  - [e.g. "EB will not attend — escalation plan?"]
NEXT-LOGICAL-STEP after this call (component to advance to):
  - [e.g. Pain Sheet, MEDDPICC scorecard, Stakeholder Map]
```

## H. Output-format guidance

When the user asks for a discovery plan or a question set, deliver:

1. The filled-in **Call planning template** above
2. The full **SPIN question sequence** with 8–15 questions total, weighted to Implication
3. Two **reframe insights** in plain language (not jargon)
4. A **commitment ladder** — primary ask + fallback if EB does not show
5. A **note on Thai cultural calibration** if the buyer is Thai — see `08-thailand-context.md`

Then offer the next component: "Want me to score this opportunity on MEDDPICC, or build the Pain Sheet from what you already know?"
