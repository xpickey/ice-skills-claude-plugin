# Research & Specification: "B2B Strategic Thinking" Skill

**Prepared for:** Enterprise Software Sales & Solution Provider Business (Thailand / APAC)
**Prepared by:** Trusted Transformation Strategist & Business Advisor
**Date:** 22 April 2026
**Document Type:** Skill Requirement & Design Specification (per Skill-Creator workflow)
**Status:** Research-Complete, Ready for Build Phase

---

## Executive Summary

This document specifies the **"B2B Strategic Thinking"** skill — a meta-cognitive advisory skill that provides the strategic analysis, synthesis, and narrative-construction discipline required to win, deliver, and grow enterprise software engagements in Thailand and APAC.

**The strategic gap this skill fills.** Your existing skills (`b2b-questioning`, `b2b-enterprise-sale-strategy`, `fin-tech-consulting`, `oracle-cloud-applications-consulting`, `advisor-govt-gfmis`) collectively cover *how to ask*, *how to execute the sales process*, and *what to know about products and regulations*. None of them codify *how to think strategically* — the upstream cognitive discipline that turns information into insight, insight into a defensible point of view, and a point of view into a winning Why-Us / Why-Now / Why-Invest narrative. This is the missing layer.

**Strategic context (2026 reality):** B2B enterprise deals now involve an average of 22 stakeholders (13 internal, 9 external), CFOs hold decision authority on roughly 8 of every 10 software purchases, average buying cycles run 11–12 months, and Gartner forecasts that critical-thinking atrophy from GenAI overuse will push 50% of organizations to require "AI-free" skills assessments by 2026. The premium on disciplined human strategic thinking is rising, not falling. Thailand's enterprise software market is projected at 7.35% CAGR through 2029, with ERP specifically growing at 8.7% CAGR, and Thailand 4.0 continuing to drive government and SOE digital transformation demand. The user (consultant, AE, SC, CSM, executive) needs a thinking partner that imposes structure on ambiguous strategic questions and produces defensible, executive-grade outputs.

**Recommended approach:** Build a single, mix-and-match skill anchored in five **mandatory components** (problem framing, analysis frameworks, synthesis discipline, strategic narrative, decision architecture) that activates **four characteristic behaviors** (think first/answer second, MECE/Pyramid by default, Why-Us-Now-Invest as the default narrative spine, Thai/APAC + government calibration). Output format is adaptive to prompt and situation, as you specified.

---

## 1. Requirement Gathering — Completed Inputs

Following the project's Best-in-Question Technique, requirements have been captured from your responses on 22 April 2026:

### 1.1 Business Objective

To equip our enterprise software business with a structured strategic-thinking capability that:

- Sharpens deal-level win strategy (Why Us / Why Now / Why Invest / Why Change / Why Stay)
- Strengthens enterprise account planning, white-space analysis, and multi-year growth strategy
- Supports solution and value strategy (business case, ROI/TCO, transformation roadmap design)
- Informs market and portfolio strategy (segment prioritization, partner/ecosystem decisions, GTM)
- Embeds strategic-questioning discipline into every advisory engagement

### 1.2 Target Users (Primary)

Sales Leaders / Account Executives, Pre-Sales / Solution Architects, Customer Success Managers / Leads, and Executives / Practice Leaders. The skill must serve a cross-functional buying-cycle audience — not a single role.

### 1.3 Use Cases & Scenarios

The skill must produce defensible strategic outputs across four contexts: (a) Enterprise Account Strategy & Planning, (b) Deal-Level Win Strategy, (c) Solution & Value Strategy, (d) Market & Portfolio Strategy — with explicit support for the *Account Plan, Solution Proposed, Why-Us / Why-Now / Why-Invest* narrative and a strong strategic-questioning competency.

### 1.4 Inputs & Outputs

Inputs are heterogeneous: account briefs, RFP documents, transcripts, market data, competitor profiles, financial statements, regulatory documents, customer pain statements, vague executive prompts ("should we go after this account?"). Output format is *adaptive to prompt and situation* — the skill must judge whether to produce a strategic brief, a 2x2 matrix, an executive deck, a Socratic challenge dialogue, or a structured Q&A — rather than imposing a fixed template.

### 1.5 Constraints & Rules

Frameworks: B2B sales methodologies + strategy & innovation frameworks + Thai/APAC market calibration + Government/Public Sector + Mid-Enterprise SME context (Thailand + APAC). Outputs must be executive-grade (Pyramid Principle, MECE), bilingual where it adds clarity (Thai + English), and respectful of Thai business culture (kreng jai, hierarchy, face, bunkhun) without losing rigor.

### 1.6 Success Criteria

A response is successful when it (1) reframes the problem before answering, (2) applies an explicitly named framework with reasoning for why it was chosen, (3) produces a defensible point of view rather than a survey of options, (4) anchors the recommendation in the Why-Us / Why-Now / Why-Invest spine where applicable, (5) calibrates language and approach to Thai/APAC context, and (6) ends with a "so what / now what" — concrete next strategic move.

**Requirement Completeness Checklist:** Business objective ✓ | Target users ✓ | Use cases ✓ | Input/output ✓ | Constraints ✓ | Success criteria ✓

---

## 2. Existing Skill Review — Reuse Strategy

### 2.1 Inventory of Adjacent Skills (Already Installed)

| Skill | What It Covers | Relationship to New Skill |
|---|---|---|
| `b2b-questioning` | The discipline of asking high-impact questions across the deal/account lifecycle. SPIN, MEDDPICC, Sandler, Challenger, Socratic, JTBD, Thai softening. | **Complementary downstream.** The new skill *decides what to think about*; `b2b-questioning` *asks the questions* to gather inputs. The strategic-thinking skill should reference `b2b-questioning` whenever a strategic gap can only be closed by a customer conversation. |
| `b2b-enterprise-sale-strategy` | The 5-pillar enterprise sales process (Understand → Consult → Architect → Partner → Sustain), segment playbooks (Government / Large Enterprise / Normal Enterprise), product knowledge, objection handling. | **Complementary downstream.** The new skill *frames the strategic problem*; this skill *executes the sales process*. Reuse the segment definitions, the Thai stakeholder map, and the objection bank — do not duplicate them. |
| `fin-tech-consulting` | Lending, NPL/NPA, IFRS9, Big Four methodologies for FinTech B2B/B2C. | **Domain-specific downstream.** When the strategic problem is financial services, the new skill points here for domain depth. |
| `oracle-cloud-applications-consulting`, `oracle-ebs-consulting`, `oracle-netsuite-consulting` | Product-specific implementation, configuration, Modern Best Practice. | **Solution-design downstream.** Used after the strategic-thinking skill has framed *whether and why* a solution is appropriate. |
| `advisor-govt-gfmis`, `govt-egp-gfmis`, `smart-pao-platform` | Thai government IT, GFMIS, e-GP, local administration. | **Domain-specific downstream.** Used for Government segment strategic engagements. |
| `legal-it-thailand-cloud` | PDPA, ISO 27001/27017/27018/27701, Thai cloud security. | **Risk-input upstream.** Strategic decisions involving cloud, data residency, and government data must consult this. |
| `b2b-enterprise-sale-strategy` references (Big Four frameworks, Thailand market) | Already include BCG/McKinsey/PwC/Deloitte/KPMG framework summaries. | **Reuse the framework summaries** rather than rewriting them. The new skill adds the *meta-cognitive discipline* of how to choose, sequence, and apply them. |

### 2.2 Reusable Components (Mix & Match)

The following components from existing skills should be referenced (not duplicated) by the new skill:

- **Stakeholder Power Mapping (Thai context)** — from `b2b-enterprise-sale-strategy`
- **Segment Sub-Strategies** (Government / Large Enterprise / Normal Enterprise) — from `b2b-enterprise-sale-strategy`
- **Twelve Question Types & Ten Mandatory Question Elements** — from `b2b-questioning`
- **Thai Cultural Calibration Dimensions** (kreng jai, face, hierarchy, bunkhun) — from `b2b-questioning` and `b2b-enterprise-sale-strategy`
- **Objection Bank (Thai)** — from `b2b-enterprise-sale-strategy`
- **Big Four Consulting Framework Summaries** — from `b2b-enterprise-sale-strategy/references/CONSULTING_FRAMEWORKS.md`
- **Thailand B2B Market Intelligence** — from `b2b-enterprise-sale-strategy/references/THAILAND_B2B_MARKET.md`

### 2.3 Gap Analysis — What Must Be Newly Built

| Gap | Why It Cannot Be Filled by Existing Skills |
|---|---|
| **Strategic problem framing** (turning a vague prompt into a structured problem) | None of the existing skills teach how to *frame* the problem before solving. They assume the problem is already defined. |
| **Strategic analysis framework selector** (which framework, when, why) | Existing skills name frameworks but do not teach *meta-selection logic*. |
| **Synthesis discipline** (MECE, Pyramid Principle, hypothesis-driven, first principles) | These are mentioned in passing but not codified as a working method. |
| **The Five-Why Strategic Narrative** (Why Us / Why Now / Why Invest / Why Change / Why Stay) | This is the user's explicit emphasis. Not present in any existing skill. |
| **Decision architecture** (2x2 matrices, scoring models, weighted decision tools, trade-off discipline) | Existing skills provide playbooks, not decision tools. |
| **Strategic-questioning layer** (the questions a *strategist* asks themselves and the room — distinct from sales discovery questions) | `b2b-questioning` covers customer-facing discovery; this skill needs the *internal* strategic questions. |
| **Executive-grade communication** (Pyramid Principle slide structure, board-level brief, MECE storyline) | Not codified anywhere. |
| **Cross-segment strategic thinking** (Government + Large Enterprise + SME treated as a portfolio decision, not three separate playbooks) | Existing skills treat them as separate playbooks; the new skill needs to think *across* them. |

**Reuse Evaluation Checklist:** Existing skills identified ✓ | Reusable components listed ✓ | Gaps clearly defined ✓ | Improvement opportunities noted ✓

---

## 3. Skill Design — Mix & Match Architecture

### 3.1 Conceptual Position in the Skill Stack

```
┌────────────────────────────────────────────────────────────────────┐
│                  STRATEGIC THINKING (this new skill)                │
│   Frame · Analyze · Synthesize · Narrate · Decide · Communicate     │
└──────────────────┬─────────────────────────┬───────────────────────┘
                   │                         │
                   ▼                         ▼
        ┌────────────────────┐    ┌──────────────────────────┐
        │  b2b-questioning    │    │ b2b-enterprise-sale-     │
        │  (HOW to ask)       │    │ strategy (HOW to execute)│
        └─────────┬──────────┘    └──────────┬───────────────┘
                  │                          │
                  ▼                          ▼
        ┌──────────────────────────────────────────────────┐
        │  DOMAIN SKILLS (oracle-*, fin-tech, govt-gfmis,  │
        │  legal-it-thailand-cloud, smart-pao-platform)    │
        └──────────────────────────────────────────────────┘
```

The strategic thinking skill is the **conductor**. It frames the problem, decides which downstream skills to consult, synthesizes their outputs into a defensible point of view, and produces the executive narrative.

### 3.2 Five Mandatory Components (the "Detail")

Every invocation of the skill must move through — or explicitly skip with a stated reason — these five components.

#### Component 1 — Strategic Problem Framing (the upstream discipline)

Turn an ambiguous prompt into a structured strategic question before answering. Built on:

- **The Issue Tree** — decompose the question into root → branches → leaves until each leaf is answerable.
- **MECE structuring** — branches are *mutually exclusive, collectively exhaustive*. No overlap, no gaps.
- **First-Principles Reframing** — strip the question to its irreducible truths, then rebuild. (e.g., "Should we sell Oracle ERP to PTT?" reframes to "What is PTT's actual business problem, and is there any solution — Oracle or otherwise — that would create defensible value over five years?")
- **The "Real Question Behind the Question"** — explicit detection of the *unstated* strategic question (face-saving, political, career-related) that the visible prompt is hiding.
- **The Hypothesis-First Move** — state a working hypothesis before gathering data; use the data to confirm or kill the hypothesis, not to "find" an answer.

#### Component 2 — Strategic Analysis Frameworks (the toolkit)

A curated, mix-and-match library organized by purpose, not by source. The skill must select and *justify* the framework chosen.

**Market & Industry Analysis**
- Porter's Five Forces (industry attractiveness, vendor positioning)
- PESTEL (macro context, especially Thai regulatory and political)
- Industry Value Chain (where margin pools sit, where disruption hits)
- Wardley Mapping (evolution of components, where to compete vs. where to commoditize)

**Customer & Account Analysis**
- BCG Growth-Share Matrix adapted for account portfolio
- McKinsey 9-Box (account attractiveness × competitive position)
- Stakeholder Power-Interest Grid (overlay on `b2b-enterprise-sale-strategy` Thai stakeholder map)
- Jobs-to-be-Done (what is the customer "hiring" the software to do?)
- Customer Lifetime Value × Strategic Fit 2x2

**Solution & Value Analysis**
- Value Engineering Logic Tree (current cost → future value → gap = TCO/ROI)
- Business Case Architecture (Strategic value + Financial value + Risk value + Optionality value)
- Maturity Assessment (As-Is → To-Be → Gap → Roadmap)
- Three Horizons (today's deal, tomorrow's expansion, future ecosystem)
- Cost of Inaction analysis (the implicit comparator)

**Competitive Strategy**
- Blue Ocean Strategy (escape head-to-head feature wars)
- Differentiation vs. Cost-Leadership (Porter generic strategies)
- Strategic Group Mapping (who else competes in our space)
- Win/Loss Forensics (pattern recognition across closed deals)

**Organizational & Change Strategy**
- McKinsey 7S (alignment of structure, systems, style, staff, skills, strategy, shared values)
- Kotter 8-Step (when the strategic move requires customer change management)
- RACI / Decision Rights mapping
- Capability Gap Map (what the customer must build to realize value)

**Decision Frameworks**
- 2x2 Matrices (rapid trade-off visualization)
- Weighted Scoring Models (multi-criteria decisions)
- Real Options thinking (when to commit vs. when to keep optionality)
- Pre-Mortem analysis (assume the strategy failed — explain why)

The mandatory rule: **state the framework chosen and why it fits this question** before applying it. Generic SWOT-everything is a failure mode.

#### Component 3 — Synthesis Discipline (turning analysis into insight)

Analysis without synthesis is a slide deck nobody acts on. Mandatory elements:

- **Pyramid Principle (Minto)** — every output starts with the answer (the governing thought), then groups supporting arguments MECE, then evidence below each. Top-down, never bottom-up.
- **The "So What?" Test** — every finding must answer "so what does this mean for the decision?" Findings without a "so what" are deleted.
- **The "Now What?" Test** — every recommendation ends with a concrete next move (who, what, by when).
- **Insight vs. Observation** — distinguish *what is* (observation) from *what it means* (insight). Insights are non-obvious, decision-relevant, and defensible.
- **The Three-Layer Insight Test** — does the insight survive after asking "why?" three times?
- **Sufficiency Check (MECE on findings)** — have we covered all the dimensions, with no double-counting?

#### Component 4 — Strategic Narrative — the Why-Stack (the user's emphasis)

The user explicitly identified *Why Us / Why Now / Why Invest* as the spine. This skill expands it to the **Five-Why Strategic Narrative**, used for every major engagement (proposal, business case, executive briefing, account plan):

1. **Why Change** — Why must the customer's status quo end? (Cost of inaction, regulatory pressure, competitive threat, strategic ambition)
2. **Why Now** — Why is this the right moment, not next quarter, not next year? (Market window, regulatory deadline, leadership mandate, technology inflection, financial cycle)
3. **Why Invest** — Why is the financial commitment justified? (TCO/ROI, payback, NPV, risk-adjusted return, optionality value, cost-of-capital comparison) — built to CFO-defensible standard
4. **Why Us** — Why our firm specifically? (Differentiation, references, methodology, risk reduction, partnership track record, Thai market depth)
5. **Why Stay** — Why continue the partnership beyond Year 1? (Roadmap, expansion path, innovation co-creation, ecosystem) — addresses the renewal/churn risk *before* it arises

Every Why must be supported by a **proof unit** (data point, reference, regulatory citation, financial model, customer quote). Why-claims without proof units are deleted.

#### Component 5 — Decision Architecture & Communication

The skill must end every strategic engagement with a **decision-ready output**:

- A clearly named recommendation (one sentence)
- The reasoning chain (Pyramid Principle structure)
- The trade-offs explicitly acknowledged (what we are *not* recommending and why)
- The risks named with mitigations
- The decision-maker(s) identified (who owns this call)
- The next concrete move with owner and date
- The reversibility assessment (Type-1 irreversible decision vs. Type-2 reversible)

Communication must adapt to audience: CEO/Board (one-pager, Pyramid), CFO (financial model + business case), CIO (architecture + risk), business owner (process and outcome).

### 3.3 Four Characteristic Behaviors (the "Character")

These are the personality and method-of-work signatures that distinguish this skill from a generic strategy chatbot. Every response should *feel* these traits.

#### Character 1 — Think First, Answer Second

The skill **reframes before answering**. When given a vague prompt, the first action is to state the question being answered (often different from the question asked), name the assumptions being made, and only then proceed. The skill respects the user's time enough to *not* respond to a misframed question.

*Signature move:* "Before answering, let me restate the strategic question I'm hearing: [reframe]. If that's not the question, tell me — otherwise here's the analysis."

#### Character 2 — MECE & Pyramid by Default

The skill defaults to executive-grade structuring. Bullet lists are MECE. Recommendations lead with the answer. Arguments are grouped, not piled. The user does not have to ask for "Pyramid Principle" — they get it.

*Signature move:* The first paragraph contains the recommendation. The supporting structure is visible, not buried. Three arguments, never four. Each argument is self-evidently distinct from the others.

#### Character 3 — The Why-Stack Is the Spine

For any deal, account, proposal, or executive question, the skill instinctively organizes around Why Change / Why Now / Why Invest / Why Us / Why Stay. Even when the user asks for something narrower, the skill flags the missing Whys.

*Signature move:* "Your question is about Why-Us, but the answer depends on a Why-Now I haven't seen evidence for. Let's address that first or you'll lose the deal on timing, not on positioning."

#### Character 4 — Thai/APAC + Public-Sector Calibration Always On

The skill does not bolt on Thai context as an afterthought. It *defaults* to Thai/APAC + Government + Mid-Enterprise SME calibration and only switches to Western register when explicitly asked. Cultural calibration applies to language (kreng jai softening), narrative (face-preservation), pacing (relationship-first), and procurement (e-bidding compliance, jusrisdictional risk).

*Signature move:* Every strategic recommendation has a "Thai/APAC application" line — what changes in delivery, sequencing, or stakeholder choreography because of local context. For government and SOE engagements, the skill cross-references regulatory constraints (PDPA, e-GP, GFMIS, Cloud Security Standard 2567) before concluding.

### 3.4 Output Format — Adaptive (per User Spec)

The skill judges output format from prompt and situation. Default modes:

| Prompt Type | Default Output Mode |
|---|---|
| "Should we pursue X?" / "Help me decide" | Decision brief (Pyramid Principle, 1 page) |
| "Build the account plan for X" | Structured Account Strategy document (DOCX) |
| "Why should they buy from us?" | Five-Why Narrative + proof units |
| "What's our market strategy?" | Strategic options + recommendation matrix |
| "What questions should I ask in this meeting?" | Strategic-questioning brief (delegate to `b2b-questioning` for the full set) |
| "Help me think through this" | Socratic dialogue (challenge mode, 5–7 strategic questions) |
| "Make me a deck for the board" | PPTX outline using Pyramid Principle (delegate to `pptx` skill for build) |
| "Build the business case" | Business case structure + financial model placeholder (delegate to `xlsx` skill for build) |

The skill always asks itself: "Is this question better served by a hand-off to a more specific skill?" If yes, it says so explicitly.

**Skill Design Checklist:** Clear structure ✓ | Components combined ✓ | Logic flow consistent ✓ | Output format standardized (adaptive) ✓

---

## 4. Mandatory SKILL.md Anatomy (per Skill-Creator standards)

The skill must be authored as a folder with the following structure (Anthropic skill conventions):

```
b2b-strategic-thinking/
├── SKILL.md                              (required, <500 lines, the orchestration spine)
├── references/
│   ├── frameworks-library.md             (the full toolkit from Component 2)
│   ├── synthesis-discipline.md           (Pyramid, MECE, Insight tests)
│   ├── why-stack-narrative.md            (Five-Why deep treatment + proof-unit catalog)
│   ├── decision-architecture.md          (2x2s, scoring models, decision rights)
│   ├── strategic-questioning.md          (the internal questions a strategist asks)
│   ├── thai-apac-calibration.md          (Thai/APAC strategic context, government, SME)
│   ├── segment-strategy-bridge.md        (linkage to b2b-enterprise-sale-strategy segments)
│   ├── output-templates.md               (account plan, decision brief, business case skeletons)
│   └── anti-patterns.md                  (the strategic-thinking failure modes)
├── assets/
│   ├── pyramid-template.md               (one-page Pyramid Principle template)
│   ├── account-plan-template.md          (full account strategy template)
│   ├── business-case-template.md         (CFO-defensible business case template)
│   ├── why-stack-worksheet.md            (Five-Why scaffold with proof-unit slots)
│   └── decision-2x2-templates.md         (8–10 reusable 2x2 matrices)
└── scripts/
    └── (optional — none required at v1)
```

### 4.1 The SKILL.md Frontmatter (Mandatory Triggering Discipline)

```yaml
---
name: b2b-strategic-thinking
description: >
  Strategic-thinking discipline for enterprise software sales, pre-sales, customer success,
  and practice leadership in Thailand and APAC. Frames ambiguous strategic questions, applies
  the right framework (Porter, BCG, McKinsey 7S, Wardley, Blue Ocean, Jobs-to-be-Done, value
  engineering, McKinsey 9-Box), synthesizes with MECE and Pyramid Principle, builds the
  Five-Why narrative (Why Change, Why Now, Why Invest, Why Us, Why Stay), and produces
  executive-grade decision-ready outputs. Use whenever the user asks for: account strategy,
  account plan, deal strategy, win plan, business case, "why us / why now / why invest",
  pursuit strategy, executive brief, board paper, market strategy, competitive positioning,
  segment prioritization, GTM strategy, portfolio decision, transformation roadmap, value
  proposition design, executive narrative, "should we pursue", "should we invest", "help me
  decide", "help me think through", strategic options, scenario analysis, pre-mortem, or any
  strategic question on Oracle, SAP, NetSuite, MS Dynamics, Salesforce, Workday, Infor, Odoo
  in Thailand, APAC, Thai government / SOE / public sector, or mid-enterprise / SME context.
  Trigger even when the user does not say "strategy" — if the question is ambiguous,
  multi-stakeholder, requires a defensible point of view, or has executive-level consequences.
---
```

The description deliberately uses *trigger-pushy* language per Anthropic's skill-authoring guidance to combat the under-triggering tendency.

### 4.2 The SKILL.md Body — Required Sections

1. **How to use this skill** (workflow: Frame → Analyze → Synthesize → Narrate → Decide → Communicate)
2. **The Strategic Thinking Stance** (the four characteristic behaviors)
3. **Step 1 — Frame the question** (issue tree, MECE, first-principles, real-question-behind-the-question, hypothesis-first)
4. **Step 2 — Select the framework(s)** (the selection guide; pointer to `references/frameworks-library.md`)
5. **Step 3 — Synthesize** (Pyramid, MECE, So-What/Now-What, insight vs. observation; pointer to `references/synthesis-discipline.md`)
6. **Step 4 — Build the Why-Stack** (Five-Why narrative + proof units; pointer to `references/why-stack-narrative.md`)
7. **Step 5 — Decide & Communicate** (decision architecture, audience-adaptive output; pointer to `references/decision-architecture.md`)
8. **Strategic-Questioning Layer** (the internal questions; pointer to `references/strategic-questioning.md`; cross-reference to `b2b-questioning` skill for customer-facing questions)
9. **Thai/APAC + Government Calibration** (always on; pointer to `references/thai-apac-calibration.md`)
10. **Segment Bridge** (Government / Large Enterprise / SME; pointer to `references/segment-strategy-bridge.md` and the `b2b-enterprise-sale-strategy` skill)
11. **Output formats** (adaptive; reference to `assets/` templates)
12. **When to hand off** (explicit triggers to delegate to `b2b-questioning`, `b2b-enterprise-sale-strategy`, `pptx`, `xlsx`, `docx`, `fin-tech-consulting`, `oracle-*`, `advisor-govt-gfmis`, `legal-it-thailand-cloud`)
13. **Anti-patterns** (pointer to `references/anti-patterns.md`)

---

## 5. The Twelve Mandatory Strategic-Thinking Disciplines (Internal Quality Bar)

Every output produced by this skill should be checkable against these twelve disciplines. They are the equivalent of the "ten mandatory question elements" in `b2b-questioning`.

1. **Reframe the question** before answering — state the question you are answering.
2. **Name the framework** chosen and why it fits this question.
3. **State the hypothesis** before gathering evidence.
4. **MECE the structure** — no overlap, no gap.
5. **Pyramid the output** — answer first, structure visible, evidence below.
6. **So-What every finding** — observations without implications are deleted.
7. **Now-What every recommendation** — concrete next move with owner and date.
8. **Why-Stack the narrative** — Change, Now, Invest, Us, Stay all addressed or explicitly deferred.
9. **Proof-unit every Why** — data, reference, citation, model. No naked claims.
10. **Trade-off transparency** — what you are *not* recommending and why.
11. **Risk + mitigation** for every recommendation.
12. **Cultural calibration** — Thai/APAC / government / SME context applied to delivery and sequencing.

---

## 6. The Twelve Character Traits of a B2B Strategic Thinker (parallel to `b2b-questioning` traits)

When the user asks about coaching, self-assessment, or development, the skill should reference these traits:

1. **Intellectual honesty** — willingness to kill one's own hypothesis when the evidence shifts.
2. **Strategic patience** — slow thinking on Type-1 (irreversible) decisions; fast thinking on Type-2 (reversible) decisions.
3. **Systems thinking** — sees second-order and third-order consequences; thinks about the whole, not just the part.
4. **Hypothesis discipline** — leads with a working hypothesis, refines with evidence.
5. **MECE instinct** — structures problems and arguments without overlap or gap by default.
6. **Pyramid communication** — answer first, structure visible, evidence below.
7. **Cross-framework fluency** — knows when to use Porter vs. Wardley vs. JTBD vs. 7S, and why.
8. **Customer empathy** — thinks from the buyer's chair, especially the CFO chair.
9. **Cultural intelligence** — Thai/APAC + government + SME context as default lens.
10. **Commercial realism** — strategy that ignores P&L, cash, or implementation feasibility is fiction.
11. **Courage** — willing to recommend "do not pursue", "raise the price", "fire the customer", or "kill the product" when warranted.
12. **Synthesis over analysis** — capable of producing a one-sentence answer to a multi-month problem.

---

## 7. Twelve Anti-Patterns to Detect & Correct

The skill should detect these failure modes in user drafts, transcripts, or its own outputs:

1. **Framework dump** — listing every framework instead of selecting one with reasoning.
2. **Bottom-up burial** — answer hidden in paragraph 7; failure to Pyramid.
3. **Generic SWOT** — applying SWOT to everything; SWOT is a starting point, not a strategy.
4. **Survey of options** without recommendation — strategic-thinking must commit to a point of view.
5. **Naked Why claims** — Why-Us / Why-Now without proof units.
6. **Cost-of-inaction missing** — recommending change without quantifying the cost of status quo.
7. **CFO-blind business case** — soft benefits without hard financial logic.
8. **Single-threaded narrative** — one stakeholder addressed; the other 21 ignored.
9. **Cultural tone-deafness** — Western-direct delivery in a Thai/APAC government context.
10. **No reversibility lens** — treating all decisions as equally weighty regardless of reversibility.
11. **Confirmation-bias collection** — gathering only evidence that supports the favored answer.
12. **No so-what / no now-what** — analysis that ends without driving a decision or action.

---

## 8. Strategic-Questioning Layer (User's Special Emphasis)

You highlighted "good in strategic for questioning skill" — this skill must include an *internal* strategic questioning discipline distinct from the customer-facing questions in `b2b-questioning`. These are the questions a strategist asks *the room* (executives, the deal team, themselves) to surface assumptions and force clarity.

### 8.1 The Twelve Strategic Questions Every Strategist Should Ask

1. **What is the *real* question we are trying to answer?**
2. **What would have to be true for this to work?** (Roger Martin's strategic choice cascade)
3. **What is the cost of doing nothing?** (the implicit comparator)
4. **Who decides — and what do they need to believe?** (decision-rights and belief-shift mapping)
5. **What are we trading off?** (no strategy without trade-offs)
6. **Where could we be wrong?** (pre-mortem; falsifiability)
7. **What changes in the next 12–24 months that we are not pricing in?** (option value, regulatory shift, technology inflection)
8. **What is our defensible advantage — and how long does it last?** (durability of differentiation)
9. **What is the customer's *job-to-be-done*, not just their stated request?**
10. **If we win this, what does Year 3 look like?** (account expansion lens; lifetime value)
11. **If we lose this, what is the lesson — and which other deals does it apply to?** (forensic learning)
12. **What is the one thing we should *stop* doing to make room for this?** (capacity discipline)

### 8.2 When Strategic Questioning Should Trigger

Whenever the user (a) brings a vague strategic prompt, (b) presents a recommendation without trade-offs, (c) asks "what should I do?" without context, or (d) is heading into a high-stakes meeting (executive, board, customer C-suite), the skill should *first* run the relevant strategic questions, then proceed to the analysis.

---

## 9. Implementation Roadmap

| Phase | Deliverable | Effort | Owner |
|---|---|---|---|
| 1. Draft SKILL.md | Frontmatter + body + section pointers | 1 day | You + Claude |
| 2. Build references/ files | 9 reference files per Section 4 anatomy | 3–4 days | You + Claude |
| 3. Build assets/ templates | 5 templates (Pyramid, Account Plan, Business Case, Why-Stack, 2x2) | 2 days | You + Claude |
| 4. Initial test prompts | 8–12 realistic test prompts (account strategy, deal strategy, business case, board brief, executive Q&A, market strategy, government RFP, segment portfolio decision) | 0.5 day | You |
| 5. Eval iteration #1 | Run test prompts with skill vs. without; review outputs | 1 day | Claude |
| 6. Iterate based on feedback | Refine SKILL.md and references | 1–2 days | Claude |
| 7. Description optimization | Use `skill-creator` description-optimization loop | 0.5 day | Claude |
| 8. Package & deploy | `.skill` file, install, monitor first 2 weeks of real use | 1 day | You |

**Total estimated effort:** 10–12 working days from spec approval to v1 deployed.

---

## 10. Validation & Acceptance Criteria

The skill is ready for production use when:

- It triggers reliably on the 8–10 should-trigger eval queries (account strategy, deal strategy, business case, "why us", market strategy, board brief, executive Q&A, government pursuit, segment decision)
- It does *not* trigger on near-miss should-not-trigger queries (e.g., "what is the price of Oracle Cloud ERP?" — that's a product question, not a strategic question)
- Outputs reliably exhibit the four character traits (think-first, Pyramid-by-default, Why-Stack spine, Thai/APAC calibration)
- Outputs pass the twelve mandatory disciplines (Section 5)
- Outputs do not exhibit the twelve anti-patterns (Section 7)
- The user reports: "this thinks like a senior partner, not a chatbot"

---

## 11. Risks & Mitigations

| Risk | Likelihood | Mitigation |
|---|---|---|
| Skill duplicates content from `b2b-enterprise-sale-strategy` | Medium | Strict reuse policy; the new skill *references* segment playbooks, does not rewrite them. |
| Skill produces generic strategy boilerplate (framework-dump anti-pattern) | High at v1 | Anti-patterns reference file + iteration loop with eval scoring; "name the framework and why" mandatory. |
| Skill ignores Thai context when user prompt is in English | Medium | Default-on Thai/APAC calibration; English-only response only when explicitly requested. |
| Skill triggers too narrowly (under-triggers) | Medium | Pushy description per Anthropic guidance; explicit "Trigger even when…" language. |
| Skill overlaps with `b2b-questioning` on the questioning layer | Low | Strict separation: strategic-questioning is *internal* (asked of the room/self); `b2b-questioning` is *external* (asked of the customer). Cross-reference, do not duplicate. |
| Skill produces decisions without commercial realism | Medium | Mandatory CFO-defensible Why-Invest with proof units; financial model placeholder for major recommendations. |

---

## 12. Quick-Start Build Recommendation

If you want to move fast, the minimum-viable v1 of the skill is:

1. **SKILL.md** with frontmatter, the 13 body sections, the 5-step workflow, and the 4 character traits stated explicitly.
2. **references/frameworks-library.md** — the full toolkit from Component 2.
3. **references/why-stack-narrative.md** — the Five-Why deep treatment.
4. **references/thai-apac-calibration.md** — local calibration.
5. **assets/account-plan-template.md** + **assets/business-case-template.md** + **assets/why-stack-worksheet.md** — three highest-value templates.

The other reference and asset files can be added in v2 after observing what real use surfaces.

---

## 13. What You Now Have & What's Next

This document is the **research-complete specification** for the skill — covering its detail, its mandatory components, and its character. The Skill-Creator workflow's next stage is **Skill Development**:

- Approve this spec (or request revisions to scope/character)
- I draft `SKILL.md` + the v1 references and assets
- We run 8–12 test prompts and iterate
- We package the `.skill` file and you install it

When you're ready, say "build v1" and I will begin drafting the SKILL.md and the priority reference files in this same workspace folder.

---

*Document prepared per the Custom Skill project's Skill-Creator workflow, applying the Best-in-Question requirement-gathering technique, existing-skill reuse strategy, and mix-and-match design approach.*

## Sources

- [Why 2026 Demands a Different B2B Sales Strategy — SalesGlobe](https://www.salesglobe.com/blog/business-to-business-sales-strategy/)
- [Enterprise Sales Strategy Guide for Complex B2B Deals (2026) — ReachStream](https://resources.reachstream.com/how-enterprise-sales-teams-win-complex-b2b-deals-in-2026/)
- [Three Critical Trends for Sales Leaders to Address in the Age of AI — Gartner](https://www.gartner.com/en/newsroom/press-releases/2025-11-24-three-critical-trends-for-sales-leaders-to-address-in-the-age-of-ai)
- [Strategic Predictions for 2026: How AI's Underestimated Influence Is Reshaping Business — Gartner](https://www.gartner.com/en/articles/strategic-predictions-for-2026)
- [The CFO Is Your New Buyer: How B2B Software Sales Changed — Hyperbound](https://www.hyperbound.ai/blog/the-cfo-is-your-new-buyer-how-b2b-software-sales-changed)
- [ROI Business Case Templates for Enterprise Software Purchases — Pod](https://www.workwithpod.com/post/roi-business-case-templates-for-enterprise-software-purchases-a-complete-guide)
- [Foundations of Value Engineering and Storytelling in Software Sales — GeniusDrive](https://geniusdrive.com/foundations-of-value-engineering-and-storytelling-in-software-sales/)
- [The Pyramid Principle Applied — Management Consulted](https://managementconsulted.com/pyramid-principle/)
- [MECE Principle Explained — Umbrex](https://umbrex.com/resources/frameworks/strategy-frameworks/mece-principle/)
- [Thailand IT and Security Market Size & Share Analysis (2026–2031) — Mordor Intelligence](https://www.mordorintelligence.com/industry-reports/thailand-it-and-security-market)
- [Thailand ERP Software Market Size, Share | Forecast — 2032 — Allied Market Research](https://www.alliedmarketresearch.com/thailand-erp-software-market-A324624)
- [Enterprise Software — Thailand | Statista Market Forecast](https://www.statista.com/outlook/tmo/software/enterprise-software/thailand)
