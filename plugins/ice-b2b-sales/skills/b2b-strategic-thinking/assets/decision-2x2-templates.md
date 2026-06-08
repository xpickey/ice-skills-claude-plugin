# Decision 2x2 & Matrix Templates

Reach for these when the strategic move is to **force a comparison and recommend**. Each template includes a default usage pattern, the axes/criteria, the trap to avoid, and an example.

For deeper guidance, see `references/decision-architecture.md`.

---

## Template A — Effort × Impact (prioritization)

**Use when:** Sequencing initiatives, triaging a backlog, deciding what to do this quarter.

**Axes:**
- X: Effort (Low → High)
- Y: Impact (Low → High)

**Quadrants:**
- Upper right (high impact, high effort) — **Strategic bets** — sequence carefully
- Upper left (high impact, low effort) — **Quick wins** — do first
- Lower left (low impact, low effort) — **Fill-ins** — do if resources permit
- Lower right (low impact, high effort) — **Avoid** — say no

**Trap:** Everything ends up "high impact." Force ranking — there can only be one #1.

**Example output:**

| Initiative | Effort | Impact | Quadrant | Recommendation |
|---|---|---|---|---|
| ERP module 1 launch | High | High | Strategic bet | Q1-Q2 |
| Reporting consolidation | Low | High | Quick win | Q1 |
| Custom RPA bots | High | Low | Avoid | Defer |
| Self-service portal | Low | Med | Fill-in | Q3 |

---

## Template B — Winnability × Strategic Value (deal pursuit)

**Use when:** Deciding which deals in the pipeline to invest in, which to deprioritize, which to walk away from.

**Axes:**
- X: Winnability (Low → High) — based on Champion strength, MEDDPICC completeness, competitive position
- Y: Strategic value (Low → High) — revenue, logo value, vertical credibility, expansion potential

**Quadrants:**
- Upper right — **Pursue hard** — full team, executive sponsor, custom assets
- Upper left (high value, low winnability) — **Strategic shaping** — invest selectively in a multi-quarter play; don't burn cash this quarter
- Lower left — **Pass** — say no; redirect resources
- Lower right (low value, high winnability) — **Transactional** — execute lean

**Trap:** Reluctance to populate the "Pass" quadrant. Empty pass-quadrant means false-positive pursuit costs are about to bleed the team.

---

## Template C — Decision Matrix (vendor / option down-select)

**Use when:** Comparing 3+ vendors, build/buy/partner, technology platform choice.

**Format:**

| Criterion | Weight | Option A score | Option B score | Option C score |
|---|---|---|---|---|
| Business value (quantified) | 25% | | | |
| Technical fit (capability coverage) | 20% | | | |
| Implementation risk | 15% | | | |
| TCO (3-5 yr) | 15% | | | |
| Vendor strength (financial, roadmap) | 10% | | | |
| Local context (Thai/APAC delivery) | 10% | | | |
| Compliance / regulatory fit | 5% | | | |
| **Weighted total** | 100% | | | |

**Scoring scale:** 1-5 (5 = best in class; 1 = unacceptable). Pair each score with one-sentence evidence; mark scores as Verified / Asserted / Assumed.

**Sensitivity check:** If the highest-weighted criterion's weight changes by ±20%, does the ranking flip? If yes, surface that as the real conversation.

**Trap:** Beauty contest where every option scores 4-5 on everything. Re-anchor scoring to **customer-specific outcomes**, not generic feature lists.

---

## Template D — Build × Buy × Partner (capability sourcing)

**Use when:** Deciding how to source a new capability — internally develop, license/SaaS, or partner.

**Frame:** Place the capability on the Wardley Mapping evolution axis (genesis → custom → product → commodity). The placement drives the answer:

| Capability stage | Usually right answer | Why |
|---|---|---|
| Genesis (novel, undefined) | Build (or partner with R&D-heavy vendor) | No mature product exists |
| Custom (domain-specific) | Build (if differentiating) or partner (if not) | Custom adds capability tailored to advantage |
| Product (multiple vendors) | Buy / SaaS | Vendor competition → good economics |
| Commodity (utility) | Buy on price / SLAs | Differentiation lives elsewhere |

**Trap:** Building what's commodity (proud-to-build syndrome) or buying what's differentiating (proud-to-outsource syndrome). Both quietly destroy strategic position.

---

## Template E — Now / Next / Later (roadmap framing)

**Use when:** Communicating a portfolio or product roadmap to stakeholders without committing to dates that will move.

**Format:**

| Now (next 90 days) | Next (90 days - 12 months) | Later (12+ months) |
|---|---|---|
| Initiative A | Initiative D | Initiative G |
| Initiative B | Initiative E | Initiative H |
| Initiative C | Initiative F | |

**Annotation:** For each, mark dependency, owner, and success metric.

**Trap:** "Later" becomes a graveyard. Add a kill criterion for each Later initiative — what would have to be true to promote it to Next; what would kill it.

---

## Template F — Risk Heatmap (likelihood × impact)

**Use when:** Communicating risk register to a steering committee or executive sponsor.

**Axes:**
- X: Likelihood (Rare → Almost certain)
- Y: Impact (Insignificant → Catastrophic)

**Color coding:** Upper right = red (active mitigation required); diagonal middle = amber (monitor); lower left = green (accept).

**Format:** Table with risk, likelihood (1-5), impact (1-5), score (LxI), mitigation, owner.

| Risk | Likelihood | Impact | Score | Mitigation | Owner |
|---|---|---|---|---|---|
| | | | | | |

**Trap:** All risks rated medium. Force the upper-right quadrant to have at least one item, and force the discussion of which ones to accept rather than mitigate.

---

## Template G — Three Horizons (portfolio strategy)

**Use when:** Helping a customer or executive sequence current-business defense vs. future-bet investment.

**Format:**

| | H1 — Defend & Extend | H2 — Build the Next Engine | H3 — Create Optionality |
|---|---|---|---|
| Time horizon | 0-2 years | 2-4 years | 4+ years |
| Investment | 60-70% | 20-30% | 5-10% |
| Metrics | Margin, retention | Pipeline, adoption | Learning, optionality |
| Risk tolerance | Low | Medium | High |
| Kill criterion | n/a | Defined | Defined |

**Trap:** H3 becomes a wishlist. Each H3 bet needs a falsifiable hypothesis and a kill criterion.

---

## Selection guide

| Situation | Template |
|---|---|
| Sequencing work | A — Effort × Impact |
| Pipeline triage | B — Winnability × Strategic Value |
| Vendor / option down-select | C — Decision Matrix |
| Capability sourcing | D — Build × Buy × Partner |
| Roadmap communication | E — Now / Next / Later |
| Risk communication | F — Risk Heatmap |
| Portfolio sequencing | G — Three Horizons |

When in doubt: the **smallest framework that exposes the trade-off** wins. A clean MECE list often beats a fancy 2x2.
