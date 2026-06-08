# Value Realization Tracking — Reference

In enterprise software, the gap between *value sold* and *value realized* is the single biggest determinant of renewal, expansion, and reference. McKinsey's research on Net Revenue Retention shows companies that systematically track and prove customer value achieve ~7 percentage points higher NRR than peers — a structural advantage that compounds.

The discipline is not just "are they happy" — it is *did the business outcomes promised in the sale actually happen, and can we prove it with numbers the CFO would accept*.

## The Three Failure Modes Value Tracking Prevents

1. **Sold value, never proved** — the business case in the deal disappears after signature; renewal becomes a price negotiation instead of an outcome conversation
2. **Proved value, never communicated** — the value happened but the customer doesn't know or doesn't agree it was us; champions cannot defend the renewal
3. **Communicated value, never updated** — the original case is stale; the customer has new pains and we are still talking about old wins

A working value-realization practice closes all three gaps.

## The Value Realization Loop

```
Define (pre-sale) → Baseline (at signature) → Track (continuous) →
Prove (quarterly via QBR) → Communicate (executive via EBR) → Refresh (annually)
```

### 1. Define — Pre-Sale Business Case

Every enterprise deal must close with a documented, quantified business case agreed by both sides. The case has three components:

- **Outcomes**: what business result will improve (e.g., DSO reduced from 65 to 45 days; close cycle from 12 to 5 days; procurement cycle time -30%; audit findings -50%)
- **Impact**: the quantified financial or operational effect (THB / USD value, hours saved, % improvement) — with the math
- **Mechanism**: how our solution causes that result — the causal chain, not correlation

The Economic Buyer must sign the business case. If they will not, that is itself a deal-stage signal — the value is not yet credible to the people who will be measured on it.

### 2. Baseline — At Signature / Go-Live

Capture the *current state* numbers at go-live. Without a baseline, future improvement is unprovable.

- Current process metrics (cycle times, headcount, error rates, costs)
- Current system landscape (what we are replacing or augmenting)
- Current pain points in the customer's own words
- Sign-off from the Economic Buyer that this is an accurate baseline

Common failure: skipping the baseline because go-live is busy. Six months later, no one remembers what "before" looked like, and value claims become opinions.

### 3. Track — Continuous

Instrument the value metrics. Make them visible to both sides on an agreed cadence.

- Identify 3–5 leading indicators (adoption, utilization, key workflow execution rate)
- Identify 3–5 lagging outcome indicators (DSO, close cycle, audit findings, cost per transaction)
- Build a simple dashboard — the customer should be able to see it any time
- Validate the data with the customer's own systems where possible (do not unilaterally claim numbers)

For Oracle / SAP / NetSuite implementations, instrument value tracking inside the platform where possible — pulling from the same GL / sub-ledger / OTC / P2P data the customer already trusts.

### 4. Prove — Quarterly via QBR

Every QBR includes a Value Scorecard segment. Standard structure:

| Outcome | Baseline | Target | Current | Status | Mechanism |
|---|---|---|---|---|---|
| DSO | 65 days | 45 days | 48 days | Green (-26% vs. baseline, on track) | AR automation + dunning workflows |
| Month-end close | 12 days | 5 days | 7 days | Yellow (still working through reconciliations) | Auto-reconciliation in GL |
| Procurement cycle | 21 days | 14 days | 16 days | Green | e-PO + auto-approval routing |

Rules of engagement:
- Show the bad numbers along with the good — credibility is built by transparency on misses
- Attribute honestly — if the result happened for reasons other than us, say so
- For misses: name the root cause and the recovery action

### 5. Communicate — Executive via EBR

The QBR is for the operational layer. The EBR is where value goes upstairs.

- Cumulative value to date (THB / USD), with mechanism breakdown
- Year-over-year trend
- Comparison against the original business case
- Forecast of value still to come from upcoming initiatives
- Joint statement: customer executive + our executive co-attest to the value (powerful for both sides)

For Thai government / SOE: present value in formats acceptable to สตง. and internal audit — sourced, calculated, and traceable.

### 6. Refresh — Annually

Business changes. Last year's outcomes may no longer be the right ones. Refresh annually:

- Revisit the business case — what is still relevant, what is stale
- Add new outcomes that have emerged (new modules deployed, new processes in scope)
- Retire outcomes that are now baked-in and no longer actively tracked
- Re-baseline where the customer's business has materially changed

## Value Realization → Renewal & Expansion

Value realization is the single best predictor of renewal price-power and expansion velocity.

- **Strong value realization** → renewal at or above list, expansion conversations initiated by the customer
- **Weak value realization** → price pressure at renewal, expansion blocked until we "earn it back"
- **No value realization data** → renewal becomes a generic procurement event; we are interchangeable with any vendor

See `renewal-expansion-motion.md` for how value realization data plugs into the renewal motion.

## Common Failure Modes

- **Set and forget** — business case agreed pre-sale, never revisited → renewal happens without it
- **Numbers without narrative** — a dashboard with no story; the customer cannot use it to defend the spend internally
- **Our numbers, not theirs** — claiming value the customer does not validate → kills credibility on first dispute
- **Hiding the misses** — reporting only green; one discovered miss erodes trust on all the greens
- **Optimism inflation** — using "$X opportunity" when we mean "$X if everything goes right" — be specific about confidence

## Cultural Calibration

- For Thai Economic Buyers and CFOs: numbers presented with the math behind them; conservative claims preferred over bold ones; documentation matters as much as the headline
- For Thai government: value framing should align with public-purpose outcomes (efficiency, transparency, citizen service, audit-readiness) in addition to direct savings
- Avoid Western "ROI sell" theatrics — Thai buyers respond better to steady, well-documented evidence than to flashy claims

## Output Format

The value scorecard is part of QBR / EBR templates. There is also a standalone `assets/account-health-scorecard.md` that incorporates value realization as one of its components. For complex multi-year programs, build a dedicated `value-realization-plan.md` per account.
