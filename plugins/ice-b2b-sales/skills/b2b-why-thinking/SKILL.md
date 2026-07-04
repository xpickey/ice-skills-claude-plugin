---
name: b2b-why-thinking
description: >-
  WHY-integrated thinking for B2B enterprise work. Combines Start-With-Why
  (Golden Circle, belief discovery) with MEDDPICC qualification and the Why
  Change / Why Now / Why Invest / Why Us / Why Stay executive narrative. Use
  when a B2B sales, pre-sales, customer success, advisory, or proposal user
  needs to — discover or sharpen a company or customer WHY, qualify a deal
  with MEDDPICC plus belief overlay, build Why Change/Now/Invest/Us/Stay
  narratives, score Deal Health, or write a WHY-driven pitch, proposal, or
  executive briefing. Triggers on Start With Why, Golden Circle, MEDDPICC,
  Why Invest/Now/Us, Deal health, executive narrative, and Thai phrases
  หา WHY, WHY ที่ใช่, วางกลยุทธ์ดีล, เขียน proposal, เตรียม pitch executive.
  Strong for Oracle, SAP, NetSuite, Microsoft, Salesforce, Workday, Infor
  deals in Thailand, APAC, government, and SOE. Outputs bilingual Thai +
  English by default. Composes with b2b-solution-selling,
  b2b-strategic-thinking, ice-b2b-enterprise-sale.
---

# b2b-why-thinking — WHY-Integrated Thinking for B2B Enterprise

> **"MEDDPICC tells you if the deal is qualified. WHY tells you if the customer will believe you. Why Invest / Now / Us is the bridge that makes both meet — in the executive room."**

This skill combines two companion frameworks into one operating system for B2B advisory work:

- **Finding the Right WHY** — philosophy + discovery (the RIGHT attributes, 5-level WHY Maturity Ladder, 7-Step Questioning Protocol, Clarity Test, Apple case, 10 Commandments).
- **WHY-to-MEDDPICC Bridge** — qualification + narrative (MEDDPICC primer with WHY overlay, Why-Stack, 3-Lens / Burning Platform / 3-Dimensions frameworks, 4 deal archetypes, 65-point integrated scorecard, proposal and presentation structures).

Together they form a four-layer stack:

```
   Philosophy        :  WHY (belief, purpose, challenge to status quo)
        │
        ▼
   Narrative         :  Why Change → Why Now → Why Invest → Why Us → Why Stay
        │
        ▼
   Qualification     :  MEDDPICC + WHY overlay (integrated 65-point scorecard)
        │
        ▼
   Execution         :  Pitch · Proposal · Presentation · Demo · Negotiation · QBR
```

---

## When to use this skill

Trigger on any of these user intents:

1. **"Help me find / sharpen our WHY"** (own company, practice, or a specific offer) — go to the *Discovery Mode*.
2. **"Find the customer's WHY"** for a specific deal — go to the *Discovery Mode* with customer lens.
3. **"Qualify / review this deal"** with MEDDPICC + belief overlay — go to the *Qualification Mode*.
4. **"Build the executive narrative"** (Why Change / Now / Invest / Us / Stay) for a proposal, board paper, or C-suite pitch — go to the *Narrative Mode*.
5. **"Score this deal's health"** or "should we forecast this?" — go to the *Deal Health Mode*.
6. **"Produce a WHY-driven proposal / pitch deck / executive briefing"** — go to the *Authoring Mode*.
7. **"Coach me / my team on a stuck deal"** — diagnose which WHY is weak, then fix.

If the user's intent is ambiguous, start with a 4–6 question interview (see *Interview Protocol* below) before producing output.

---

## Core principles (always keep in mind)

These principles come from the two source frameworks and should shape every output.

1. **WHY is a belief, not a slogan.** It must be *Rooted · Inspiring · Guiding · Honest · Timeless* (R-I-G-H-T). If it fits on a mug without effort, it's probably not the right WHY.
2. **WHY doesn't replace MEDDPICC — it enriches it.** Hard qualification without belief = price war. Belief without qualification = stalled deal.
3. **Every MEDDPICC letter has a WHY question behind it.** Metrics have a purpose, Economic Buyers have a legacy, Champions take political risk for a reason. Surface those reasons.
4. **The biggest competitor is "do nothing".** 60–70% of B2B deals are lost to status-quo, not to named competitors. Why Now is usually the weakest link.
5. **Executives buy in five questions.** Why Change / Why Now / Why Invest / Why Us / Why Stay — in that order, always. **แต่ละข้อต้องตอบด้วย 2 ภาษา — DREAM (vision) + REALITY (proof/feasibility ที่ลด perceived risk)** มิฉะนั้น deal stall ที่ indecision. → `references/pitch-belief-card.md` L4 (SSOT).
6. **WHY is a filter, not a magnet.** Its job is to *repel* prospects who don't share the belief, so LTV and margin compound on the ones who do.
7. **Every red flag = a missing WHY.** Price pressure → Why Invest weak. Deal stall → Why Now weak. Competitive loss → Why Us weak. "Let's revisit next quarter" → all three are weak.
8. **Bilingual by default.** For Thai-market deals and advisory, produce Thai + English side-by-side unless the user asks for one language only.
9. **Do not fabricate customer-specific facts.** If the user hasn't provided them, mark them as `[to confirm in discovery]` — never invent names, numbers, or internal dynamics.

---

## Interview Protocol (use before producing significant output)

Ask 3–6 short, targeted questions depending on the mode. Use multi-select / choice format where possible. Examples:

**Universal (always ask if unknown):**
- Which mode do you want? (Discovery · Qualification · Narrative · Deal Health · Authoring · Coaching)
- Whose WHY are we working on? (Our company / practice · This specific customer · Both — shared belief)
- Which deal / account / offer is this for? (name + rough size + stage)
- Which competitor(s) or alternative(s) are in the room — including "do nothing"?

**Mode-specific add-ons:** see each mode section below.

Produce the output only once you have enough signal. If the user pushes back on the interview, give them the best-guess output but clearly flag assumptions.

---

## Modes of operation

Each mode has a lightweight workflow, the reference file to consult, and the default output format. Always prefer to read the matching reference file before producing the output — the SKILL.md is the map, the references are the territory.

### Mode 1 — Discovery (Finding the Right WHY)

**When:** user wants to find, sharpen, or test a WHY (own or customer's).

**Workflow:**
1. Read `references/right-why-philosophy.md` — the 5-level WHY Maturity Ladder, RIGHT attributes, 7-Step Questioning Protocol, Clarity Test, Apple case, 10 Commandments.
2. Run the 7 steps on the target: Origin Excavation → 5-Whys Drill-Down → Contribution Mapping → Status Quo Challenge → Personal Resonance → Market Differentiation Test → Synthesis.
3. Draft the WHY statement in both Standard ("To X so that Y") and Apple-style ("Everything we do, we believe… we challenge status quo by… we just happen to…") forms.
4. Run the 7-Point Clarity Test and Red Flags checklist. If it fails ≥2 criteria, iterate.
5. Output: filled *WHY Discovery Workbook* (`assets/templates/why-discovery-workbook.md`) + two candidate WHY statements + Clarity scorecard.

**Default output:** Markdown + a filled workbook. Offer a `.docx` upgrade if the user wants an executive document.

---

### Mode 2 — Qualification (WHY-to-MEDDPICC Bridge)

**When:** user is qualifying a specific opportunity, or a deal feels "technically qualified but emotionally thin" (or vice versa).

**Workflow:**
1. Read `references/meddpicc-bridge.md` — MEDDPICC primer, the 8-letter Bridge Map, the 4 deal archetypes, and the 65-point Integrated Scorecard.
2. For each MEDDPICC letter, capture both the factual answer and the WHY question behind it (see Bridge Map).
3. Identify deal archetype: Aligned Believer · Technical Fit · Spiritual Connection · Lost Cause — and prescribe the matching action.
4. Fill the *WHY-to-MEDDPICC Mapping Worksheet* (`assets/templates/why-meddpicc-worksheet.md`).
5. Score on the 65-point Integrated Scorecard and classify: Strong (55–65) / Workable (40–54) / At Risk (25–39) / Dead (<25).
6. Output a concise diagnosis + the top 3 weak letters/WHYs + the next-step action plan.

**Default output:** Filled worksheet + 1-page "Deal Diagnosis" summary.

---

### Mode 3 — Narrative (Why Change / Now / Invest / Us / Stay)

**When:** user is preparing a proposal, board paper, EBR, C-suite pitch, or any executive-grade artifact.

**Workflow:**
1. Read `references/why-stack-narrative.md` — full treatment of Why Change, Why Now, Why Invest (3-Lens), Why Us (3-Dimensions), Why Stay + the pitch-pattern phrasing.
2. For each of the 5 WHYs, build:
   - the headline belief (one sentence),
   - the 3 strongest supporting points,
   - the pitch-pattern paragraph in the executive's language,
   - evidence anchors (reference customers, KPIs, third-party data — with `[to confirm]` markers where user didn't supply).
   - **⭐ emit แต่ละ WHY เป็นคู่ (DREAM | REALITY):** DREAM = pitch-pattern (vision) · REALITY = Reality anchor (proof/feasibility ลด risk) จาก `why-stack-narrative.md`. ขาดเสียงจริง = deal stall. → `pitch-belief-card.md` L4.
3. Stress-test each WHY with its red-flag checklist (e.g. for Why Now: the "Why Not Next Year" test).
4. Assemble the *Executive Bridge Slide* — one page with Why Change / Now / Invest / Us / Stay, success metrics, decision date, sponsor, champion.
5. Output: the full 5-WHY narrative block + the Executive Bridge slide + suggested phrasings in both Thai and English.

**Default output:** Markdown block ready to paste into deck/doc/email. Offer a `.pptx` upgrade if user wants slides.

---

### Mode 4 — Deal Health (Weekly Pipeline Review)

**When:** sales manager or seller is reviewing pipeline, forecasting, or triaging stuck deals.

**Workflow:**
1. Read `references/meddpicc-bridge.md` (Section: Deal Health Scorecard + Red Flag Checklist) and `references/why-stack-narrative.md` (Section: Pulse check questions).
2. For each deal, run the 5-minute drill:
   - 2 min: quick MEDDPICC evidence check (8 letters).
   - 2 min: Why-Stack pulse check (5 questions).
   - 1 min: diagnosis + top action for the week.
3. Classify against the 4 archetypes; flag any "Technical Fit" (price-war risk) and "Spiritual Connection" (no-close risk) deals with specific corrective actions.
4. Output: per-deal scorecard row + an overall pipeline-health readout (how many Aligned Believers vs others, where forecast confidence sits).

**Default output:** Table / scorecard in markdown. Offer `.xlsx` upgrade for larger pipelines.

---

### Mode 5 — Authoring (Proposal / Pitch / Presentation)

**When:** user wants to generate the actual document.

**Workflow:**
1. Read `references/presentation-proposal.md` — the 10-section WHY-Driven Proposal structure, the 60-minute executive presentation flow, the Executive Bridge Slide pattern, and 7 tips for WHY-driven B2B pitches.
2. Gather required inputs: customer name, industry, deal size, EB + Champion + competitor, 2–3 metrics, the shared belief. Flag missing inputs as `[to confirm]`.
3. Draft the artifact in the requested format:
   - **Pitch:** Apple-style Belief → Challenge → How → What → Invitation (≤ 1 page).
   - **Proposal:** 10-section WHY-driven structure with Executive Summary anchored on shared belief.
   - **Presentation:** 60-min flow mapped to MEDDPICC hooks per section.
4. Self-review against principles 1–9 (above) and the Red Flags list. Fix anything that fails.

**Default output:** Markdown draft. Offer `.docx` / `.pptx` / `.pdf` upgrades — chain to the `docx`, `pptx`, or `pdf` skill as needed.

---

### Mode 6 — Coaching (Stuck Deal / Objection Diagnosis)

**When:** user presents a stuck deal or an objection ("budget tight", "let's revisit next quarter", "evaluating vendor X", "IT team needs to review first").

**Workflow:**
1. Map the symptom to the weak WHY using the Red Flag table (see `references/meddpicc-bridge.md`).
2. Produce 3 targeted re-entry actions: (a) one question to ask Champion, (b) one slide/email to send EB, (c) one commercial/methodology move.
3. If the root cause is a missing archetype-level fix, state it plainly — including "disqualify" when that is the honest call.

**Default output:** 1-page diagnosis + 3 re-entry actions.

---

## Orchestration with other skills

This skill is a *thinking layer* — it composes well with these specialist skills. When the user's request stretches beyond the WHY/MEDDPICC/Narrative scope, hand off or chain:

| User need | Chain to |
|---|---|
| Thai B2B enterprise sales playbook (Oracle/SAP etc.) | `b2b-solution-selling`, `ice-b2b-enterprise-sale`, `b2b-enterprise-sale-strategy` |
| Strategic framework (Porter, BCG, Wardley, 7S…) | `b2b-strategic-thinking` |
| Discovery/coaching questions | `b2b-questioning` |
| Account/relationship (QBR, EBR, renewal, expansion) | `b2b-relationship-management` |
| Design-thinking / envisioning workshop | `b2b-design-thinking` |
| Thai government e-GP / GFMIS / SMART PAO specifics | `govt-egp-gfmis`, `advisor-govt-gfmis`, `smart-pao-platform` |
| Oracle ERP / EPM / NetSuite / EBS technical depth | `oracle-cloud-applications-consulting`, `oracle-netsuite-consulting`, `oracle-ebs-consulting` |
| FinTech / IFRS9 / NPL/NPA | `fin-tech-consulting` |
| Pipeline report, call prep, outreach | `sales-pipeline-report`, `sales:call-prep`, `sales:draft-outreach` |
| Word / Excel / PowerPoint / PDF output | `docx`, `xlsx`, `pptx`, `pdf` |

When chaining, pass along the filled templates (workbook, worksheet, scorecard) so the downstream skill has full context.

---

## Output quality bar (self-review before delivering)

Before returning any artifact, check:

- [ ] **Rooted** — every belief statement traces back to a real origin or customer fact (not marketing fluff). Assumptions flagged `[to confirm]`.
- [ ] **Pass the "remove our name" test** — no WHY statement works if a competitor could paste their name in.
- [ ] **All five WHYs addressed** where relevant (Change / Now / Invest / Us / Stay).
- [ ] **MEDDPICC gaps named, not hidden** — weak letters are explicitly called out with an action.
- [ ] **Executive language** — short sentences, one idea per line, no jargon soup.
- [ ] **Bilingual** (Thai + English) if the customer/user is in Thai market.
- [ ] **One artifact, one purpose** — a proposal is not a pitch is not a workbook.
- [ ] **Risks, not just upside** — mentions the cost of inaction and the risk of choosing us.
- [ ] **Two languages present** — every WHY has BOTH a DREAM (vision) and a REALITY anchor (proof/feasibility). Vision alone → stalls on indecision.

If any check fails, iterate before handing back.

---

## Reference files (progressive disclosure)

Do not load everything at once. Read the relevant reference file when the mode calls for it:

- `references/right-why-philosophy.md` — *Finding the Right WHY* in full: R-I-G-H-T attributes, 5-level Maturity Ladder, Anatomy of the Right WHY, 7-Step Questioning Protocol, 7-Point Clarity Test, Red Flags, Apple case study, 10 Commandments, Sales-stage application.
- `references/meddpicc-bridge.md` — MEDDPICC primer, the 8-letter WHY Bridge Map, the 65-point Integrated Scorecard, the 4 deal archetypes (Aligned Believer / Technical Fit / Spiritual Connection / Lost Cause), the Red-Flag-to-WHY diagnosis table.
- `references/why-stack-narrative.md` — Why Change / Why Now / Why Invest (3-Lens) / Why Us (3-Dimensions) / Why Stay with discovery questions, frameworks (Burning Platform matrix, Executive Pitch Patterns), red flags, **+ per-WHY Reality anchors (two-language de-risk)**.
- `references/pitch-belief-card.md` — **⭐ L1 SSOT: Pitch-Belief framework** (5 บทเรียน Pitch + งานวิจัย + application map 4 homes). belief > idea · 2 ภาษา · visual credibility · deck = design piece. skill นี้ owns NARRATIVE layer; homes อื่นชี้มาที่การ์ดนี้.
- `references/presentation-proposal.md` — WHY-Driven 10-section proposal structure, 60-minute executive presentation flow with MEDDPICC hooks, Apple-style B2B pitch template, Executive Bridge Slide pattern, 7 tips for communicating WHY in B2B.
- `references/question-bank.md` — Bilingual (Thai + English) question bank covering Discovery, Qualification, Narrative, Deal Review, and Objection Handling.

## Asset templates (use as-is or adapt)

- `assets/templates/why-discovery-workbook.md` — 10-question workbook (Origin / Belief / Contribution / Impact).
- `assets/templates/why-statement-builder.md` — Standard + Apple-style formulas with blank fields.
- `assets/templates/why-meddpicc-worksheet.md` — full discovery-call worksheet combining 8 MEDDPICC letters + 5-WHY assessment + Deal Health Score + Next Actions.
- `assets/templates/why-invest-canvas.md` — 3-Lens business case canvas (Financial / Strategic / Personal-Organizational).
- `assets/templates/deal-health-scorecard.md` — 65-point integrated scorecard with interpretation bands and archetype mapping.
- `assets/examples/oracle-erp-thai-manufacturing-case.md` — end-to-end walk-through of a 180M-THB Oracle Cloud ERP deal, showing the "before MEDDPICC-only" vs. "after WHY-to-MEDDPICC Bridge" contrast.

---

## Three rules to remember

```
╔════════════════════════════════════════════════════════════╗
║                                                            ║
║  1. WHY ที่ใช่ (Right WHY) = Belief that challenges        ║
║     status quo — Rooted, Inspiring, Guiding, Honest,       ║
║     Timeless.                                              ║
║                                                            ║
║  2. MEDDPICC tells you if the deal is qualified.           ║
║     WHY tells you if the customer will believe you.        ║
║     Why Invest / Now / Us is the bridge that makes         ║
║     both meet — in the executive room.                     ║
║                                                            ║
║  3. Every red flag = a missing WHY. Diagnose the           ║
║     weak WHY before you negotiate the price.               ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝
```

---

## Version History
- **V01R02 (2026.07.04)** — +Two-Language (dream+reality) lens on WHY-stack: per-WHY Reality anchors in `why-stack-narrative.md` (proof/feasibility ลด perceived risk คู่กับ vision) + Core principle 5 extended + Mode 3 emits paired DREAM|REALITY + Output-bar checkbox. **Hosts `references/pitch-belief-card.md` (L1 SSOT)** — Pitch-Belief framework (5 lessons + deep-research) that 4 fleet homes point to. Body-only (frontmatter untouched — note: description is over the ~1024 Web cap, separate fix).
- **V01R01** — initial (Start-With-Why + MEDDPICC + 5-WHY narrative).

> *"You don't sell a solution. You sell a belief — backed by a qualified plan."*
