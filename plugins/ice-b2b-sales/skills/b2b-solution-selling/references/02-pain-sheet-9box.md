# Reference 02 — Pain Sheet, Pain Chain & 9-Box Vision Processing Model

**Use when:** Converting vague complaints into critical, quantified pain. Co-creating the buyer's vision so they own it. Preparing to write a proposal, business case, or executive presentation.

This reference covers two of the most powerful Bosworth/Eades Solution Selling tools.

---

## A. The Pain Sheet (one row per admitted pain)

A Pain Sheet is the working document that captures every admitted business pain in the buyer's organisation. Every row must be defensible to the buyer.

| Field | Definition | Bad example | Good example |
|---|---|---|---|
| **Pain (in buyer's words)** | What the buyer actually said, not what you wish they said | "Our system is old" | "Our month-end close has slipped from 12 to 18 business days over the last three quarters" — Khun Somchai, Group Controller, 14 Apr 2026 |
| **Reason / Root Cause** | Why this pain exists | "Bad software" | "GL is fragmented across 4 entities; intercompany matching is manual in Excel; 3-day reconciliation gate before consolidation can start" |
| **Quantified Impact** | The cost of this pain in metrics the buyer cares about — THB, days, FTE, % margin, audit findings, customer churn | "It costs a lot of time" | "11 extra business days × 5 finance FTE × THB 150K monthly fully-loaded = THB 8.25M/year direct cost. Plus 2 audit findings on segregation of duties = THB 1.5M remediation cost. Plus deferred treasury decisions = ~THB 4M working capital opportunity." |
| **Pain Owner** | Which role personally feels this pain in their performance review | "Finance team" | "CFO (audit committee exposure), Group Controller (team turnover), Treasurer (working capital miss)" |
| **Pain Status** | Latent / Admitted / Critical | — | Critical — board has put it on the Q3 agenda |
| **Capability Required** | What capability (NOT product feature) would relieve this pain | "Oracle Cloud Financials" | "Real-time intercompany matching at line level; automated reversal entries; sub-ledger reconciliation dashboards available to controller before period close" |

Rule: **No Capability is filled in until Reason and Quantified Impact are admitted by the buyer.** Otherwise you are selling features, not solving pain.

## B. The Pain Chain (how pain cascades up the org)

A Pain Sheet entry only matters if you can show how it cascades from the operator level up to the Economic Buyer. Map every critical pain on this chain:

```
USER LEVEL pain (operator)
    ↓ causes
SUPERVISOR / MANAGER pain (functional owner)
    ↓ causes
DIRECTOR / VP pain (P&L or function owner)
    ↓ causes
C-SUITE pain (Economic Buyer)
    ↓ causes
BOARD / SHAREHOLDER pain (governance, regulator, market)
```

**Worked example — manual intercompany matching:**

| Level | Owner | Pain |
|---|---|---|
| User | GL accountant | Works 60-hour weeks last 5 days of every month |
| Manager | Group Controller | Cannot publish close on day 7; team turnover up 30% YoY |
| Director | CFO | Audit committee flagged segregation-of-duties gap two quarters running |
| C-suite | CEO | Bank covenant reports filed late twice; lender raised pricing 25 bps |
| Board | Audit Committee Chair | Considering replacing Big Four auditor at premium fee due to control concerns |

When you can articulate the chain, the seller controls the conversation with **anyone** in the buying centre — because each person hears their own pain in your story.

## C. The 9-Box Vision Processing Model

Once a Critical Pain is admitted, the seller's job is to help the buyer **build a vision** of how to solve it — in the buyer's own words. The buyer who builds the vision owns it; the buyer who is told the vision resists it.

The 9-Box is a question matrix. Three rows × three columns:

|  | **Reasons** (why this pain exists) | **Impact** (what this pain causes) | **Capabilities** (what would solve it) |
|---|---|---|---|
| **OPEN** | "What is causing this close delay?" | "What does this delay cost the team / business?" | "If you could change one thing about the close process, what would it be?" |
| **CONTROL** | "So if I'm hearing you right, the root cause is the manual intercompany match, plus the FX translation step. Is that the order of magnitude?" | "So that 11-day slippage costs roughly THB 13M a year fully loaded — does that match your view?" | "If the system could auto-match intercompany at line level and trigger reversal entries automatically, would that close the gap?" |
| **CONFIRM** | "Let's lock that. Root cause is intercompany + FX + control gap. Agreed?" | "Agreed cost: THB 13M/year direct + audit risk + treasury opportunity. We'll quantify treasury together next week. OK?" | "Agreed capability requirements: real-time IC matching at line level, auto-reversal, sub-ledger dashboards available to Controller pre-close. Anything else?" |

### The discipline

- **OPEN** — buyer talks 80%, seller listens; collect raw material
- **CONTROL** — seller summarises, paraphrases, narrows; tests the buyer's thinking
- **CONFIRM** — get explicit agreement in writing (email recap or shared doc); now you can quote it back

The seller never says "Oracle does X" inside this matrix. The buyer says "I need a system that does X." That is the entire point.

## D. From Vision to Capability Statement

After the 9-Box, the seller produces a **Capability Statement** — a list of *what the system must do*, expressed as buyer outcomes, NOT product modules:

**Bad (feature list):**
- Oracle Cloud Financials
- Intercompany Module
- Account Reconciliation Cloud Service

**Good (capability statement, in buyer's voice):**
- "Match intercompany transactions automatically at line level so my GL team can stop the manual Excel reconciliation"
- "Generate reversal entries automatically and post them on the next-period open"
- "Give my Controller a real-time sub-ledger reconciliation dashboard accessible before the close window opens, not after"
- "Cut my month-end close from 18 days to 7 days by Q2 next year"

The Capability Statement is the bridge from Pain Sheet → Business Case → SOW → Customer Success Criteria. Every downstream artefact references it.

## E. Output-format guidance

When the user asks for a Pain Sheet, deliver:

1. A table with one row per admitted pain (use the schema in section A)
2. A Pain Chain diagram for the 1–2 most critical pains (use the markdown chain in section B)
3. A 9-Box matrix populated with **suggested questions** for each cell — this is the seller's call plan for the next meeting
4. A draft Capability Statement (4–8 bullets, in buyer's voice, NOT product language)
5. A "what to confirm in writing" checklist — the things the seller must get the buyer to acknowledge by email after the next meeting

Then offer the next component: "Want me to take this Pain Sheet and build the MEDDPICC scorecard, or convert the Capability Statement into a CFO-grade business case?"

## F. Common failure modes

- **Pain stops at "we want to be more efficient".** Push for THB / days / FTE quantification or it is not a pain, it is a wish.
- **Single-source pain.** Only the GL accountant has admitted it; the CFO has not. The deal is single-threaded — see `05-stakeholder-mobilizer.md`.
- **Capability statement contains product names.** Re-write it in the buyer's voice. If you cannot, you have not done the 9-Box properly.
- **No compelling event.** Pain is real but the buyer is not under pressure to act this quarter. Keep the deal warm but do not forecast it — see `03-meddpicc-scorecard.md`.
