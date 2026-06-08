# Evaluation Evidence — Iteration 1

This folder contains the empirical evidence that this skill works.
It was generated using the Anthropic skill-creator evaluation
framework (3 realistic test cases, with-skill vs no-skill baseline,
graded against 23 explicit assertions by an independent grader).

## Files

| File | What it is |
|---|---|
| `iteration-1-benchmark.md` | Quantitative summary: pass rate, time, tokens (with vs without skill) |
| `iteration-1-benchmark.json` | Same data, machine-readable, with per-eval and per-assertion breakdowns |
| `iteration-1-eval-viewer.html` | Interactive review viewer — open in browser to read every with-skill and baseline output side-by-side, see which assertions passed, and leave feedback |

## Headline numbers (iteration 1)

| Metric | With skill | Without skill | Delta |
|---|---|---|---|
| Pass rate | 100% (23/23) | 33% (8/23) | **+67 pts** |
| Time | 307s avg | 152s avg | +155s |
| Tokens | 111k avg | 82k avg | +29k |

## The three test cases

1. **thai-conglomerate-cfo-discovery-prep** — Oracle Cloud Financials + EPM to a Thai listed THB 18bn food-processing conglomerate. Tests SPIN sequencing weighted to Implication, Challenger reframe, Thai cultural calibration (kreng-jai, face, family-principal shadow buying centre), competitive positioning vs SAP S/4HANA RISE and NetSuite. (7/7 with skill, 1/7 baseline.)
2. **stuck-deal-meddpicc-diagnosis** — Stuck THB 45M Oracle EPM deal at a Thai SET-listed retail group. Tests numeric MEDDPICC scoring (8 elements, traffic-light), Champion-vs-Coach test, seller-DNA derailer detection (Happy Ears, Alligator Arms, Single-threaded), kill criteria, "this week" actions. (7/7 with skill, 2/7 baseline.)
3. **signed-deal-handover-pack** — NetSuite implementation at a Thai mid-market manufacturer (THB 12M TCV, BOI e-tax compelling event). Tests all 10 mandatory handover artefacts (Win Brief, SOW Alignment Memo, EB-signable numerical Success Criteria, Open Commitments Log, Risk Register, Stakeholder Map carryover, etc.) plus the discipline that they exist BEFORE signature, plus AD post-signature continuity. (9/9 with skill, 5/9 baseline.)

## Why this matters

The baseline is what a smart Claude session produces *without* this skill — it is not "stupid". The 67-point delta is the value the skill adds on top of generic sales advice: explicit Thai cultural protocol, named methodologies executed end-to-end, numeric scoring over qualitative guessing, sell-through-deliver discipline, and seller-self-diagnosis using the DNA rubric.
