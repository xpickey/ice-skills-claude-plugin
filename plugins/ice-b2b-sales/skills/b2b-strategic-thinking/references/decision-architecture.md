# Decision Architecture

Strategy is the act of choosing. This reference codifies how to structure a decision so the choice is **defensible, reversible-when-needed, and clear about what would change it.**

Use this whenever the model is asked to "recommend," "decide," "pick," "go/no-go," or "what should we do."

---

## The four-part decision package

Every decision recommendation should arrive in this shape:

1. **The choice** — what is being chosen, between what options
2. **The recommendation** — which option, with confidence level
3. **The reasoning** — criteria, weights, evidence, trade-offs
4. **The reversibility plan** — what would change the answer, what to monitor, when to revisit

Skipping #4 is the most common failure. A recommendation without a reversibility plan is a guess in disguise.

---

## The decision tree

```
Question
  ├─ Frame the choice (what is in / out of scope)
  ├─ Inventory options (MECE — including "do nothing")
  ├─ Define criteria (with weights, tied to strategy)
  ├─ Score options against criteria
  ├─ Identify trade-offs (what each option costs)
  ├─ Recommend with confidence
  └─ Define monitoring (what would change the answer)
```

---

## Framing the choice

A poorly framed choice is unsalvageable downstream. Watch for:

- **False binaries.** "Build vs. buy" often hides "build, buy, partner, defer, or commission a feasibility study."
- **Smuggled-in conclusions.** "Should we go with Vendor A or Vendor B?" smuggles in the assumption that the choice is between A and B. Re-frame: "What is the best path to capability X?"
- **Wrong altitude.** A board-level question framed as a project decision (or vice versa) wastes the decision.
- **Missing "do nothing."** Always include the status-quo option, even if it's clearly worse — it forces the cost-of-inaction calculation.

---

## Defining criteria

Criteria should be:
- **Tied to strategy.** Each criterion answers "why does this matter to our objective?"
- **MECE.** No overlaps; no important dimension missing.
- **Weighted.** Equal weighting is rarely true and often hides the real decision driver.
- **Testable.** "Strategic fit" is not a criterion; "extends our existing OneStream relationship" is.

**Default criteria starter list for B2B software decisions:**
- Business value (quantified)
- Technical fit (capability coverage, architecture alignment)
- Implementation risk (effort, change burden)
- Cost (TCO over 3-5 years; cash timing)
- Vendor strength (financial, roadmap, ecosystem)
- Strategic optionality (does this open or close future moves?)
- Local context (Thai/APAC delivery, language, references)
- Compliance / regulatory fit (PDPA, e-GP, audit defensibility)

Adjust based on the specific decision. Make weights explicit; don't bury them.

---

## Scoring discipline

For each option × criterion:
- Use a **clear scale** (1-5 or 1-10), defined upfront ("5 = best in class; 1 = unacceptable").
- Pair each score with **one-sentence evidence**, not just a number.
- Mark scores as **verified, asserted (vendor-claimed), or assumed**.
- Run a **sensitivity check**: if the top weighted criterion's weight changes by ±20%, does the answer flip? If yes, that's the real conversation.

---

## Surfacing trade-offs

A clean recommendation that hides trade-offs is dishonest. For the recommended option, name:
- **What you're giving up** (the close-second option's strengths)
- **What risks you're accepting** (and the mitigation)
- **Who pays for this choice** (which stakeholder or function bears the cost of change)
- **What you're betting on** (the assumption that, if wrong, breaks the choice)

This is what makes a recommendation *executive-grade*. It signals you've actually thought about it.

---

## Confidence calibration

State confidence in plain language and tie it to evidence quality:

| Confidence | Means | Trigger |
|---|---|---|
| **High** | The evidence supports this decisively; we'd defend it under hostile scrutiny | Multiple independent data sources align; key assumptions are facts |
| **Medium** | The balance of evidence supports this; reasonable people could disagree | Some inference involved; one or two key assumptions |
| **Low** | We have a tentative direction but real uncertainty | Heavy reliance on inference; data is thin or stale |

**If confidence is Low**, the recommendation should usually be a **bounded next move** (paid pilot, scoping engagement, parallel feasibility) rather than a full commitment.

---

## The reversibility plan

Define before delivery:

1. **What metrics would prove the choice right?** (Leading indicators, not lagging.)
2. **What metrics would suggest it's wrong?** (Tripwires.)
3. **Who owns monitoring, and at what cadence?**
4. **What is the cost of reversing, by quarter elapsed?**
5. **At what checkpoint is the next decision triggered?**

Strategic decisions are rarely irreversible. They are usually expensive to reverse — and that expense should be **named**, not hidden.

---

## Decision frames by situation

### Vendor down-select (e.g., Oracle vs. SAP vs. NetSuite)
Use a weighted decision matrix. Force at least one criterion that explicitly addresses **lock-in / exit cost**. Score against the customer's actual capability roadmap, not a generic feature checklist.

### Build vs. Buy vs. Partner
Use Wardley Mapping (`references/frameworks-library.md`) to expose what is *commodity* (buy/SaaS) vs. *differentiating* (build/custom). The answer is usually "buy the commodity, build the differentiation, partner the in-between."

### Pursue vs. Pass on a deal
Use a 2x2 of "winnability × strategic value." Force a "do nothing" comparison. Be willing to recommend "pass" — false positives in pursuit are the largest hidden cost in sales.

### Sequencing initiatives in a roadmap
Use a 2x2 of "value × effort" with a third dimension (color/size) for **dependency**. Sequence by dependency-respecting impact.

### Go-to-market segment choice
Use Three Horizons + value pool sizing. Force a kill criterion per H2/H3 bet.

### Pricing / commercial structure
Use Value Engineering Logic Tree to anchor price to value, then test against customer's budget reality and competitor's posture. Surface "what we're betting on" explicitly.

---

## Calibration to Thai/APAC + Government

A few decision-architecture moves that matter:

- **Government decisions are committee decisions.** Frame the recommendation as it will be experienced by the steering committee — emphasize defensibility, audit-readiness, and policy alignment over cleverness.
- **Family-business decisions are owner decisions.** Frame in cash and legacy terms; respect the founder's bunkhun toward incumbent partners; never recommend a path that humiliates an existing vendor.
- **Patience is a feature, not a bug.** A Thai mid-enterprise buyer's "let me think about it for a month" is not a stall — it's relationship-building. The reversibility plan should respect that timeline rather than push artificial urgency.
- **Face-saving alternatives.** When recommending "pass" or "delay," provide a face-saving narrative the customer can use internally.

See `references/thai-apac-calibration.md` for deeper guidance.

---

## Anti-patterns

| Anti-pattern | Symptom | Fix |
|---|---|---|
| **Analysis paralysis** | A 40-criterion matrix with no weights | Force top-5 weighted criteria |
| **Beauty contest** | All vendors score 4-5 on everything | Re-anchor scoring to customer-specific outcomes |
| **Single-option pitch** | "Recommendation: do X" with no compared alternatives | Include rejected options and why |
| **Buried trade-off** | Recommendation reads like a free lunch | Name what's given up explicitly |
| **No reversibility plan** | Decision packaged as final | Add monitoring and tripwire metrics |
| **Confidence theater** | "We strongly recommend…" with weak evidence | Calibrate honestly; recommend a smaller bet if uncertain |
