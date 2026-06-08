# Orchestration Playbook
**Version:** V02R02 | **Date:** 2026.05.22 | **Companion to:** `../SKILL.md`

# Section 0 — How to Read

This playbook is lookup, not reading. Each Worked Example (WE) is a Rapid-Workflow recipe
calibrated for 30–60 minute production. Each Quick Reference Card (QRC) is a one-page
job-aid for a specific recurring pre-sales task.

Each WE follows the same shape:
- **When to invoke** — one line.
- **Prerequisite Input** — what must be on the table before you start (Customer Profile
  is the universal first item).
- **Skill chain** — exact order, no flexibility.
- **Rapid recipe** — 4–8 steps of what to write, in 30–60 minutes.
- **Critical pitfalls** — what kills the deliverable if done wrong.
- **Output template hint** — 3–5 lines of structure to start from.

When a WE references an artifact pattern from real iCE work, the customer is anonymised
as `[CUSTOMER]`, `[ORG]`, `[BANK]`, `[VENDOR-A]`. Financial figures are `[VALUE]`. Dates
are `[DATE]`. Where details are inferred from folder/filename rather than file contents,
they carry an `[ASSUMED: ...]` flag.

# Section 1 — Worked Examples

## WE-00 Customer Profile Method (Pre-Step Zero)

**When to invoke:** Always, the first time you engage a customer in this session. Skip
only if the user uploads a Customer Profile artifact and points to it.

**Prerequisite Input:**
- Customer legal name and short brand name
- Industry segment (use Industry × Product table in `sub-skill-index.md` Section 3)
- Either: existing customer file shared by the user, OR public information access

**Skill chain:** `strategic-thinking → questioning → (optional product skill)`

**Rapid recipe (45 min):**

1. **Open with positioning** (5 min) — legal entity, founding year, headquarters, brand
   tagline, strategic concept. One paragraph. This is the anchor for everything else.

2. **Map business segments as planning units** (10 min) — list 4 to 8 segments as a
   table. Each segment is a planning unit for downstream EPM, business case, and demo
   work. Do not skip this even if the customer looks single-segment; segments emerge.

3. **Strategic roadmap, two horizons** (10 min) — Domestic + International (or Onshore
   + Cross-segment). Use 1–3-year horizons. Themes only, not initiatives.

4. **Five strategic-themes lenses** (10 min) — Portfolio choice, Customer-segment shift,
   Digital / Innovation agenda, Operating-model change, Risk and macro drivers. One
   short paragraph each.

5. **Risk and scenario drivers** (5 min) — name the 4–6 risks that move forecasts
   materially. These become scenario inputs for any business case.

6. **EPM-ready input checklist** (5 min) — what data must be collected: revenue by
   segment, customer mix, channel mix, asset footprint, digital KPIs, financial levers,
   external drivers. This is the lift-off pad for downstream WE-02 and WE-06.

**Critical pitfalls:**
- Writing as a corporate brochure instead of an advisor's input list. Every section
  must end with "what this tells us for planning."
- Inventing financial figures or growth rates. If a number is not from a real source,
  flag `[VALUE TBD]` or `[ASSUMED]`.
- Skipping the segment table because the customer "obviously" has one product line —
  segments always emerge by channel, region, or customer cohort.

**Output template hint:**
```
1. Company overview (for EPM baseline)
2. Current business model and core segments  [TABLE: Segment / Activities / Notes]
3. Strategic roadmap and expansion themes    [Domestic / International]
4. Key strategic themes (for advisor analysis)
5. Major challenges (for risk and scenario planning)
6. Ready-to-use input list (EPM-ready checklist)
```

Source pattern: based on iCE Customer Profile for `[CUSTOMER: Large Travel-Retail Group]`,
2026.05 — six-section structure with purpose-tagged sub-sections.

---

## WE-01 RFP/TOR Response (Oracle Fusion + รัฐวิสาหกิจ)

**When to invoke:** The customer is a รัฐวิสาหกิจ or government ministry, has published
a TOR with clause-numbered requirements, and asks for a Technical Proposal in response.

**Prerequisite Input:**
- Customer Profile (WE-00 output)
- TOR document with all annexes
- Confirmed budget envelope or pricing constraint from the TOR
- iCE's go/no-go decision (run QRC-09 if not done)

**Skill chain:** `strategic-thinking → solution-selling → oracle-cloud-applications-consulting → govt-egp-gfmis → presentation-creator`

**Rapid recipe (60 min for the structural skeleton; fill across additional sessions):**

1. **Section 1 — Executive Summary & Understanding (10 min)**: four sub-sections —
   Executive Summary, Understanding the Organisation, Understanding Project Objectives,
   Budget Envelope. Tone: confident, organisation-specific, not generic.

2. **Section 2 — Project Management (5 min)**: workplan, methodology, risk management,
   team structure, communication cadence. Five sub-sections. Use the iCE 5-phase
   delivery shape (Planning → Analysis → Design → Build → Transition → Go-Live).

3. **Section 3 — Technical (10 min)**: system architecture, integration, security,
   data migration from legacy, technical deliverable list. Five sub-sections.

4. **Section 4 — Warranty (5 min)**: 1-year warranty scope, helpdesk SLA, monthly/
   quarterly monitoring, vulnerability management. Five sub-sections.

5. **Section 5 — Post-Warranty Cost (5 min)**: yearly subscription, maintenance MD
   bucket, man-day rate sheet, headcount cost.

6. **Section 6 — License Rights (5 min)**: full-user / view-only / admin counts, cloud
   environment ownership, 5-year scaling.

7. **Section 7 — Process & Deliverables (15 min)**: this is the heavy section.
   Sub-sections 7.1 through 7.20 covering Project Charter, Kick-off, Requirements,
   Design, Build, SIT, UAT, Training, Data Migration, Go-Live, Reporting, Integration
   (Inbound + Outbound), Reports (Financial + Management + Budget + Reconciliation),
   Deliverable List (9 categories of documents).

8. **Section 8 — Compliance Matrix (5 min skeleton, fill across sessions)**: every TOR
   clause 4.3.x mapped to one of Fully Comply (FC) / Partial Comply (PC) / Custom Comply
   (CC) / Workaround (WA). This is the section the customer scores.

**Critical pitfalls:**
- Confusing organisation-specific Section 1 with generic vendor introduction. Section 1
  is about THEM; iCE introduction comes in an appendix or covering letter.
- Section 7 padding. Every sub-section must add specific commitment, not abstract
  methodology language.
- Compliance Matrix written in narrative paragraphs. It must be a table with TOR clause
  ID, FC/PC/CC/WA marker, and a 1–2 line evidence column.
- Pricing presented before scope is locked. The Compliance Matrix locks scope; pricing
  in Section 5/6 must trace to it line by line.

**Output template hint:**
```
ส่วนที่ 1 บทสรุปผู้บริหาร & ความเข้าใจ        (1.1–1.4)
ส่วนที่ 2 ข้อเสนอด้านการบริหารโครงการ          (2.1–2.5)
ส่วนที่ 3 ข้อเสนอด้านเทคนิค                    (3.1–3.5)
ส่วนที่ 4 ข้อเสนอด้านการรับประกันคุณภาพ        (4.1–4.5)
ส่วนที่ 5 ค่าใช้จ่ายหลังสิ้นสุดระยะรับประกัน    (5.1–5.4)
ส่วนที่ 6 สิทธิ์การใช้งานระบบ                  (6.1–6.6)
ส่วนที่ 7 กระบวนการดำเนินงาน & ขอบเขต         (7.1–7.20 + sub-bullets)
ส่วนที่ 8 ข้อกำหนดทั่วไปและ Compliance Matrix  (8.1.1–8.1.x for each TOR clause)
```

Source pattern: `[BANK: รัฐวิสาหกิจ Export-Import]` Technical Proposal V01R05, 2026.05
— 8-section structure with full TOR Compliance Matrix in Section 8.

---

## WE-02 Business Case + ROI (Oracle NetSuite + Trading)

**When to invoke:** Customer is asking for a written investment justification — either
to support an internal CFO/CEO sign-off, or as part of a multi-vendor evaluation. The
financial model travels with the prose case.

**Prerequisite Input:**
- Customer Profile (WE-00)
- Current-state pain quantification (or `[ASSUMED]` with named drivers)
- Target capability scope (modules in play)
- Time horizon (3-year vs 5-year)
- Discount rate / hurdle rate for NPV (ask if not provided)

**Skill chain:** `strategic-thinking → solution-selling → oracle-netsuite-consulting → (optional why-thinking)`

**Rapid recipe (50 min):**

1. **Executive summary** (5 min) — three lines: what we propose, what it delivers,
   what it costs. Headline NPV and payback period only.

2. **Project at a glance** (5 min) — single table: customer entity, legal entities in
   scope, user count breakdown (named vs non-named), module set, indicative timeline,
   investment band. Mirror the language of the customer's procurement form.

3. **Current state vs target state** (10 min) — two columns. Current is pain anchored
   in real quotes or process gaps. Target is the post-implementation capability.
   Do not list features; list outcomes.

4. **Benefit lines, 3 to 5 (15 min)** — each one quantified. Typical benefit lines for
   a Trading customer: faster close (manday savings), inventory accuracy (carrying
   cost reduction), pricing discipline (margin uplift), audit readiness (compliance
   cost avoidance), revenue uplift from analytics. Each line: assumption → calculation
   → annual value → caveat.

5. **Cost lines, 5-year (10 min)** — Y1 = Implementation + License + Hardware (if any);
   Y2–Y5 = License Renewal + Maintenance + Optional Capacity Adds. Show as a single
   table; do NOT bury costs in narrative.

6. **NPV / Payback / Sensitivity (5 min)** — one-page math. Always show two sensitivity
   scenarios: pessimistic (50% of benefit realised) and optimistic (120% with one
   bonus benefit). Customer CFOs trust ranges, not single numbers.

**Critical pitfalls:**
- Benefits framed in feature language ("real-time consolidation") rather than outcome
  language ("3 days closing instead of 9"). Always express benefit in time, money, or
  risk reduction.
- Missing the negative case. Without a downside scenario, the business case reads as
  vendor pitch, not advisor work.
- Costs in body prose, benefits in tables. Always invert that — costs in tables (audit
  trail), benefits in prose with table backup (story leads, math supports).

**Output template hint:**
```
1. Executive Summary
2. Project at a Glance      [TABLE: Customer / Entities / Users / Modules / Timeline / Investment]
3. Current State vs Target State  [TWO COLUMNS]
4. Benefit Lines            [TABLE: Driver / Assumption / Annual Value / Caveat]
5. 5-Year Cost              [TABLE: Year / Implementation / License / Maintenance / Total]
6. NPV / Payback / Sensitivity   [Base + Pessimistic + Optimistic]
```

Source patterns:
- `[CUSTOMER: Telco-Services Group]` NetSuite EPM Budget Investment V02R01, 2026.05
  — seven-project investment table with phase-based payment-term schedule.
- `[CUSTOMER: Telecom-Holding Conglomerate]` ERP/EPM Master Agreement + Work Order +
  Tax Subscription Services Agreement, 2026.05 — three-document commercial package
  pattern (Master Agreement frames legal terms, Work Order frames scope and price per
  engagement, Tax Subscription Services Agreement frames recurring subscription
  separately). When the customer's procurement model is a parent-MSA-with-child-WOs
  shape, this three-document split is mandatory; do not collapse into a single
  proposal. Use Master Agreement as the precedent reference for legal terms, and
  separate the recurring SaaS subscription into its own agreement to keep the budget
  lines clean.

---

## WE-03 Demo Design (Oracle Fusion + Large Enterprise)

**When to invoke:** A discovery is complete; the customer asks to see how the proposed
solution actually behaves. The deliverable is a deck plus a live (or recorded) demo
script.

**Prerequisite Input:**
- Customer Profile (WE-00)
- Top 3 to 5 customer pain points (from discovery), prioritised
- Source-of-truth system map (where does customer data live today)
- Available demo environment access (or screenshots/walkthroughs from sandbox)

**Skill chain:** `strategic-thinking → oracle-cloud-applications-consulting → presentation-creator`

**Rapid recipe (50 min):**

1. **Solution Architecture cover (5 min)** — one slide that names the proposed
   platform, the customer's source-of-truth system, the integration backbone, and the
   "end-to-end" framing line. The cover sets the entire viewing frame.

2. **Two-to-three "Prebuilt" module deep-dives (15 min)** — pick the modules that
   matter to the customer's top pains, not the modules iCE happens to know best. Each
   module gets one slide with: capability headline, three input methods or use cases,
   and how it connects to the next module. Show the **deep-dive shape**, not feature
   parade.

3. **One "Custom" model for customer-specific lever (15 min)** — every Large Enterprise
   has one driver that the prebuilt model doesn't fit. Build that as a Custom slide:
   the driver tree, the calculation logic, the input forms.

4. **Three to five UX slides walking through the user experience (10 min)** — Web
   Form, Smart View / Excel, Dashboard, Mobile, Approvals. These are the slides that
   make the demo memorable. Use real screenshots where available.

5. **Integration backbone slide (5 min)** — Data Objects table: source → target →
   frequency → mode (real-time / daily / on-demand). Eight rows is the sweet spot —
   fewer feels under-engineered, more overwhelms.

**Critical pitfalls:**
- Generic Oracle marketing slides inserted between custom slides. They break the
  thread and signal "we couldn't think of anything specific."
- Custom model presented without a Driver Tree visualisation. Customers absorb the
  Tree in 10 seconds; the prose takes them 90.
- Integration treated as appendix. Put it in the main flow — it is the technical
  bridge to engineering buy-in.

**Output template hint:**
```
Slide 01 — Cover / Solution Architecture        (end-to-end framing)
Slide 02 — Architecture Deep Dive               (Platform + Source-of-Truth + Integration backbone)
Slide 03–04 — Prebuilt Module Deep Dives        (per priority pain)
Slide 05 — Custom Model Driver Tree
Slide 06 — Custom Model UX (Web Form)
Slide 07–10 — UX walkthrough (Excel, Dashboard, etc.)
Slide 11 — Integration Data Objects table
```

Source pattern: `[CUSTOMER: Large Travel-Retail Group]` iCE EPM Presentation V02R01,
2026.05 — 14-slide deck with EPBCS Core + Custom BPS Layer + SAP integration backbone.

---

## WE-04 Demo Design (Oracle NetSuite + Manufacturing)

**When to invoke:** Customer is a multi-entity manufacturer (or industrial-services
group with manufacturing-like cost behaviour) and asks for a NetSuite demo or
investment overview that maps to multiple project workstreams rather than a single ERP
go-live.

**Prerequisite Input:**
- Customer Profile (WE-00)
- Legal entity count and consolidation requirement (single GL ledger? multi-GAAP?)
- Project-cost behaviour (job costing? cost-of-production? project-based?)
- Bank account count and payment workflow type (Host-to-Host? batch?)

**Skill chain:** `strategic-thinking → oracle-netsuite-consulting → presentation-creator`

**Rapid recipe (50 min):**

1. **Investment Summary cover (5 min)** — single slide stating: total program scope =
   N implementation projects, framing both as one program. List the N projects.

2. **Approach and methodology (5 min)** — show the iCE delivery shape (planning →
   analysis → design → build → transition → go-live → warranty), explicit that the
   shape applies to every project.

3. **Project deep-dives, one slide per project (25 min)** — for each of the N projects,
   build one slide containing: project title (bilingual), one-line outcome statement,
   "Current Pain Points" (3–5 bullet points anchored in customer language), and
   "Target Capability" (3–5 bullet points anchored in NetSuite delivery). Common
   projects in a manufacturer context: financial consolidation & close, inter-company
   reconciliation, corporate FP&A, project-cost planning, cash flow planning, bank
   reconciliation, open-item / accrual clearing.

4. **Investment summary table (5 min)** — every project as a row, columns: project
   name (Thai/English), time frame, investment band, project type (Mandatory /
   Optional). Subtotals by project type.

5. **Payment terms and Why iCE (10 min)** — milestone-based payment schedule (e.g.
   20% at Project Initiation, then drawdowns at phase gates). Why-Us slide is 4–6
   anchored points (certifications, deal references, team continuity, support model).

**Critical pitfalls:**
- One mega-project slide for everything. NetSuite-on-Manufacturing usually fragments
  into 5–8 sub-projects; collapsing them into one hides scope and creates pricing
  ambiguity.
- "Pain Points" written by you instead of the customer. Always anchor in real
  discovery quotes; if not available, flag `[ASSUMED]`.
- Why iCE at the start instead of the end. The customer should ask "why these guys?"
  after seeing the solution, not before.

**Output template hint:**
```
Slide 01 — Investment Summary cover (N projects)
Slide 02 — Approach & Methodology (shared shape)
Slide 03–N — Project cards (Pain Points + Target Capability)
Slide N+1 — Investment Summary Table
Slide N+2 — Payment Terms Timeline
Slide N+3 — Why iCE (4–6 anchors)
Slide N+4 — Thank You / Contact
```

Source pattern: `[CUSTOMER: Telecom-Services Group]` NetSuite EPM Budget Investment
V02R01, 2026.05 — 14-slide deck covering 7 implementation projects.

---

## WE-05 Demo Design (Oracle NetSuite + FMCG / Trading)

**When to invoke:** Customer is in F&B, FMCG, Sports apparel, consumer goods retail,
or wholesale distribution, and asks for a NetSuite proposal — typically with a heavy
inventory, B2B+B2C channel mix, or franchise/partner network angle.

**Prerequisite Input:**
- Customer Profile (WE-00)
- Channel mix (B2B vs B2C, online vs retail, distributor vs direct)
- Product master complexity (SKU count, variant model, multi-language)
- Existing system + pain (Excel-bound? legacy POS? mismatched ledgers?)

**Skill chain:** `strategic-thinking → solution-selling → oracle-netsuite-consulting → presentation-creator`

**Rapid recipe (45 min):**

1. **Investment Proposal cover and Why iCE early-mention (5 min)** — for FMCG/Trading
   buyers, surface credibility upfront (named industry references, deal references)
   because the buying lens skews retail-pragmatic, not enterprise-strategic.

2. **Proposed solution architecture (10 min)** — show NetSuite as the backbone with
   adjacent: e-commerce platform, payment gateway, communication (Email/SMS/OTP), POS
   /retail, and warehouse/3PL. The architecture slide is more important here than for
   pure-finance demos because of the channel breadth.

3. **Scope: in vs out (5 min)** — clear table. FMCG customers often want to start
   wide, scope it down to a Phase-1 footprint that retires the worst pain first.
   Recommended Phase-1: GL + AP + AR + Inventory + Item Master + Basic Sales Order +
   Purchase Order.

4. **License × User × Module mapping (5 min)** — show named-user vs non-named-user
   split. FMCG/Trading usually has many transactional users (operation) and few named
   approvers — leveraging non-named licence economics is the deal-defining lever.

5. **Project assumptions and RACI (5 min)** — one slide of assumptions (the things
   that must be true for the price to hold) and one short RACI naming who-does-what
   between iCE, customer IT, and the operating BU.

6. **5-phase methodology, indicative timeline, investment summary (10 min)** —
   condense the standard delivery shape into one timeline slide and one investment
   slide. Include both Mandatory and Optional add-ons (NetSuite localisation,
   e-commerce integration, BI add-on).

7. **CR-pattern reference for post-Go-Live (5 min)** — `[INSERT IF CUSTOMER IS
   EVALUATING LONG-TERM]` — show a single sample CR (Change Request) line item to
   demonstrate the post-implementation operating model: severity, impact analysis,
   manday breakdown.

**Critical pitfalls:**
- Treating FMCG like Finance. The buying committee includes COO and CDO, not just
  CFO; demo must show inventory, channel, customer master — not just GL.
- Skipping the channel architecture. For these customers, channel topology IS the
  business model.
- Pricing only Mandatory items. Always include 1–2 Optional add-ons so the buyer can
  trade trade-up vs. wait — single-price proposals lose negotiating room.

**Output template hint:**
```
Slide 01 — Cover / Project at a Glance
Slide 02 — To-Be Architecture (NetSuite + Channel + Payment + Comm)
Slide 03 — Project Scope (Legal Entity / Module / User counts)
Slide 04 — Implementation Approach (Single-instance, single-ledger)
Slide 05 — License × User Mapping
Slide 06 — Project Assumptions
Slide 07 — In-Scope vs Out-of-Scope table
Slide 08 — Methodology (5-phase)
Slide 09 — Timeline
Slide 10 — RACI Matrix
Slide 11 — Project Team Structure
Slide 12 — Investment Summary (Mandatory + Optional)
Slide 13 — Payment Terms
Slide 14 — Sample CR pattern (post-Go-Live)
```

Source patterns (four real FMCG/Retail anchors, pick the closest to the deal in front of you):

- `[CUSTOMER: Sports Apparel Group]` C-Suite Proposal DEMO v2.0, 2024.06 — 85-slide
  Salesforce-CRM + NetSuite-ERP integration deck. Pattern: front-of-deck "New Modern
  Sales Method & Process" framing; Salesforce Opportunity → Cost Estimation → Quote
  → Sales Order tracked from ERP; integration carries channels (Phone / Facebook
  Messenger / Email / Line OA / Online Payment / 3rd-party). Reach for this when
  the deal includes CRM-ERP integration, not pure ERP.

- `[CUSTOMER: Integrated Poultry Group]` NetSuite Proposal V01R05, 2026.01 — 146-slide
  gold-standard NetSuite-FMCG deck. Patterns: iCE company profile + Why iCE + named
  industry references (three peer companies in the same vertical, anonymised); seven
  NetSuite core modules mapped to Sales / SCM / Finance / Manufacturing business
  functions; SuiteCloud platform layered for customisation; AI-in-the-Suite section
  (NetSuite Advisor, SuiteAnswers Virtual Assistant, Supply Chain Control Tower);
  Customer 360 (with Asia-availability caveat). Use when customer is a vertically-
  integrated FMCG manufacturer (farm-to-fork, factory-to-shelf) and named industry
  references in the same vertical close the credibility gap.

- `[CUSTOMER: Health Foods Corporation]` Propose Solution rev0.2, 2025.02 — 90-slide
  multi-channel FMCG deck. Pattern: deep iCE Group structure intro (parent group,
  resource counts, regional offices, technology partners), then High Level Solution
  with **all channels in one architecture diagram**: CRM + ERP + Mobile POS + Modern
  Trade EDI + Owned Store + E-Commerce + Pipeline Mgt + Traditional Trade Dealer.
  Reach for this when the customer's channel topology is the deal-defining complexity.

- `[CUSTOMER: Health Foods Corporation, IIG-channel version]` Propose Solution
  1st-to-proposal, 2024.11 — 25-slide compact variant. Pattern: anchored in real
  Design Thinking Workshop output (customer team-identified pain points), structured
  as CRM/PRM Engagement Platform with a 3-Release plan across M1–M11 and explicit
  Crawl-Walk-Run approach across Process / People / Technology / Governance / Data.
  Use this anchor when the customer has already done a design workshop with iCE; the
  proposal continues that conversation rather than starting from scratch.

For the long-term operating model post-Go-Live, pair the chosen anchor with
`[CUSTOMER: F&B / Restaurant Group]` NetSuite CR template, 2026.04 — single CR form
covering severity, impact analysis, and manday breakdown across Solution Design /
Dev / Testing / Deployment.

---

## WE-06 Board Paper (Cross-product + Large Enterprise)

**When to invoke:** The customer's board, executive committee, or steering committee
needs a written briefing on a transformation decision. Audience is non-technical;
the deliverable must read in 5–10 minutes and survive being printed and circulated.

**Prerequisite Input:**
- Customer Profile (WE-00)
- The decision the board is being asked to make (vendor selection? phase 2 approval?
  budget release?)
- Confirmed audience composition (CEO + CFO + COO + IT? full board?)
- Time budget for reading (5 min, 10 min, 30 min — calibrate length accordingly)

**Skill chain:** `strategic-thinking → why-thinking → presentation-creator` (.pptx) OR no
presentation-creator if .docx

**Rapid recipe (60 min):**

1. **Decision frame, top of page (5 min)** — single statement of what the board is
   approving. Not the project description; the specific decision. "Approve a 5-year,
   `[VALUE]` investment in `[PLATFORM]` to consolidate `[N]` legal entities and retire
   `[LEGACY]`."

2. **Why Change (10 min)** — three to five forcing functions. Each one names a
   specific risk or opportunity that is degrading without action. Not generic ("market
   is changing") but specific ("post-pandemic group-tour share dropped from 60% to
   30%, requiring a different revenue model").

3. **Why Now (5 min)** — what changes if the board defers six months. Cost of delay
   in real money or real risk. Two paragraphs.

4. **Why This Path (10 min)** — three options compared in a single table: do nothing,
   minimum viable, recommended scope. Each gets: cost, risk, time-to-value, downside.
   The recommended row carries the most detail.

5. **Why Us (5 min)** — short. Three anchors: relevant precedent, team continuity,
   support shape. Do not over-sell; the board already knows iCE if it is on the
   shortlist.

6. **Risk and mitigation (10 min)** — top 5 risks with mitigation owner named. Risk
   types worth surfacing for board audience: adoption risk, integration risk, vendor
   risk, data quality risk, regulatory risk.

7. **Decision and next steps (5 min)** — what is being approved today, what triggers,
   and what the next gate is. One paragraph.

8. **Appendix (10 min)** — financial detail, technical detail, comparable references.
   Board audience reads top half; appendix exists for the readers who want detail.

**Critical pitfalls:**
- Decision frame buried on page 3. The opener IS the ask; everything else explains it.
- Three options with two visibly-wrong fillers. The board sees through that. Make
  options genuinely different in shape (scope, vendor, sequencing), not just price
  variants of the same plan.
- "Why Us" written as iCE pitch. Reframe as "why this combination" — capability +
  reference + team is what the board is buying.
- Risk register with no owner. A risk without an owner is a wish, not a mitigation.

**Output template hint:**
```
Page 1 — Decision Frame + Recommendation (one paragraph)
Page 2 — Why Change (3–5 forcing functions)
Page 3 — Why Now (cost of delay)
Page 4 — Three Options Compared (table + recommended row detail)
Page 5 — Why Us / Why This Combination
Page 6 — Top Risks + Mitigation Owners
Page 7 — Decision & Next Steps
Page 8+ — Appendix (Financial detail, Technical detail, References)
```

Source pattern: `[CUSTOMER: Multi-country Mining/Energy Group]` Technical Discussion
v2.3.1, 2026.05 — 39-slide format using topic-numbered structure (5 topics) and Q&A
appendix referencing TOR question IDs. Adapt the topic-numbered structure when the
audience is technical-executive; simplify to 5–8 pages for pure-board audience.

---

## WE-07 FinTech Pursuit (Bank + IFRS9 / Lending / NPL)

**When to invoke:** Customer is a Bank, NBFI, Insurance, or Securities firm asking for
help on Lending Origination, NPL/NPA management, IFRS9 / TFRS9 implementation, or
Credit Risk transformation. Regulatory posture matters more than product breadth.

**Prerequisite Input:**
- Customer Profile (WE-00) with regulator named (BoT? SEC? OIC?)
- Current IFRS9 / TFRS9 maturity level
- Existing core system and what fragment of the lending value chain it covers
- Pain centre (origination latency? NPL recovery? credit-decision quality? regulatory
  reporting?)

**Skill chain:** `strategic-thinking → solution-selling → fin-tech-consulting → (Oracle product skill if Oracle-platform) → presentation-creator`

**Rapid recipe (60 min):**

1. **Regulatory frame (10 min)** — open with the regulator and the specific rule that
   forces the project. IFRS9 staging? TFRS9 ECL model? BoT Section X reporting? The
   regulator-named opener is what makes Bank buyers commit; without it, the proposal
   reads as IT modernisation.

2. **Lending value-chain map (10 min)** — one slide / one page showing where the
   pain sits in the value chain: Onboard → Underwrite → Disburse → Service →
   Recover → Charge-off. Highlight the 2–3 stages targeted; out-of-scope is explicit.

3. **IFRS9 / TFRS9 staging logic (15 min, if applicable)** — the technical core. Show
   Stage 1 / Stage 2 / Stage 3 transition rules, PD / LGD / EAD components, forward-
   looking macro overlay, and the ECL calculation flow. Bank CFOs and risk officers
   need to see this; without it, they cannot sign off.

4. **NPL / NPA workflow (10 min, if applicable)** — collection cohorts (early
   delinquency vs deep recovery), workflow automation, call-script integration,
   restructuring scenarios, write-off triggers. Show the volume math — NPL workflow
   pays for itself only above a minimum recovery uplift.

5. **Regulatory reporting auto-generation (5 min)** — list the reports that must come
   out of the system: BOT, SEC, OIC, TFRS9, IFRS9, internal capital adequacy. The bank
   CIO buys on automation here.

6. **Architecture and data model (10 min)** — high-level: core-banking → credit engine
   → risk warehouse → IFRS9 calculator → reporting. Specific to Oracle if Oracle is
   the proposed stack; otherwise vendor-agnostic.

**Critical pitfalls:**
- IT-led pitch with finance treated as a downstream user. Banks buy this from the
  finance and risk seats; lead with finance/risk, IT is enabler.
- Mixing IFRS9 and TFRS9 vocabulary inconsistently. The Thai bank audience needs Thai
  terms (มาตรฐาน TFRS9, การจัดชั้น, ECL, การจัดการ NPL) alongside English.
- Missing the regulator-frequency mismatch. Some reports are monthly, some quarterly,
  some daily for capital adequacy. The customer must see that the system handles all
  three cadences without manual reconciliation.

**Output template hint:**
```
Section 1 — Regulatory Frame (regulator + rule + deadline)
Section 2 — Lending Value-Chain Map (in-scope vs out-of-scope)
Section 3 — IFRS9/TFRS9 Staging + ECL Logic
Section 4 — NPL/NPA Workflow (cohorts + automation + scenarios)
Section 5 — Regulatory Reporting Suite (BOT/SEC/OIC + internal)
Section 6 — Architecture & Data Model
Section 7 — Investment + Phased Roadmap
```

Source patterns (three real Government-Bank anchors):

- `[BANK: รัฐวิสาหกิจ Export-Import Bank]` Technical Proposal V01R05, 2026.05 —
  8-section structure with Compliance Matrix Section 8 covering TOR 4.3.1 through
  4.3.16+. Best anchor for the **prose body** of a Bank Technical Proposal — Section 1
  (understanding the bank), Section 7 (process and deliverables), Section 8 (clause-
  by-clause comply).

- `[BANK: รัฐวิสาหกิจ Agricultural Cooperatives Bank]` ERP Demo Applications V02R01,
  2025.07 — 137-slide Oracle EBS Bank demo. Patterns to lift: opens with **Finance
  Modernization for Banking Reference Architecture** showing all banking source
  systems (Loans, Cards, Trading Systems, Corporate Deposits, Cash Management,
  Collection, FX & Money Market, Payments) feeding into a unified Financial / Cost
  / Planning core; Oracle FSI Reference Table (Thai Bank A, Thai Bank B with
  Yes/Yes across FCCS / EPBCS / PCMCS); Compliance posture stated upfront (PCI DSS
  Type II, SOX); End-to-End Budget Control Process Flow (Plan → GL → Project →
  Approval); Budgeting Workflow (Executive ↔ Budget Coordinator with explicit
  Request and Approval steps). Use this anchor when the bank is asking for a demo
  rather than a proposal, and when Budget / EPM is the central topic.

- `[BANK: รัฐวิสาหกิจ Agricultural Cooperatives Bank]` ERP Digital Transformation
  Roadmap, 2026.04 — 32-slide three-topic Roadmap deck. Three-topic structure:
  (1) แนวทางการพัฒนาระบบ (system-development approach) — Oracle Tech Stack,
  Solution Architecture, EBS, Finance Analytics, One-UI, Personalize Workbench,
  Event-Driven Integration, Process Orchestration, REST APIs, Cyber Security aligned
  with กมช. (National Cybersecurity Committee) and PDPA; (2) ความเสี่ยงที่อาจเกิดขึ้น
  (risks and mitigation) — risk register with categories (บุคลากร / Vendor / Schedule
  / Quality / Technology) and named owner per row; (3) ประมาณการมูลค่าการลงทุน 5 ปี
  (5-year investment estimation) — with DC Site + DR Site Network Diagrams (Cisco
  UCS C240 M8 × 2 reference). Reach for this anchor when the deliverable is
  Roadmap-style (multi-year, board-facing) rather than Proposal-style.

For IFRS9 / TFRS9 staging specifics, the materialised artifact base does not yet
include a published staging-logic deck; continue to flag IFRS9 stage transitions, PD
/ LGD / EAD components, and ECL calculation flow as `[ASSUMED: TFRS9 staging logic
common to Thai BoT-regulated banks]` until a customer-specific IFRS9 artifact is
shared.

---

## WE-08 Government e-Bidding (Ministry + e-GP + GFMIS)

**When to invoke:** Customer is a government ministry, รัฐวิสาหกิจ, or state savings/
agricultural bank, and the procurement is running through e-GP under พรบ.จัดซื้อจัดจ้าง
2560. The deliverable is a formal e-Bidding submission with TOR Comply, ราคากลาง
acknowledgement, and หลักประกัน management.

**Prerequisite Input:**
- Customer Profile (WE-00) with confirmed regulator framework (พรบ. 2560 vs. agency-
  specific rules)
- Full TOR with all annexes and clause numbering
- ราคากลาง and any pre-bid clarifications already issued
- Confirmed iCE bidding eligibility (no debarment, no conflict)

**Skill chain:** `strategic-thinking → solution-selling → oracle-cloud-applications-consulting → govt-egp-gfmis → advisor-govt-gfmis (if budget/treasury) → presentation-creator`

**Rapid recipe (60 min for skeleton; multi-session for full submission):**

1. **e-GP submission cover sheet (5 min)** — bidder identity, project name, TOR
   reference number, bid validity period, หลักประกัน type (Bank Guarantee vs. Cash
   Deposit), bid amount within ราคากลาง.

2. **TOR Comply structure decision (5 min)** — for รัฐวิสาหกิจ deals, the response is
   usually broken into Functional Lots + Lot-4 (non-functional). Decide upfront which
   Lot model the customer is using. Common: Lot#1 = Finance core, Lot#2 = SCM core,
   Lot#3 = HCM + Future capabilities (AI/ESG/GRC), Lot#4 = Application List + TCO
   Template + Data Volume + Software License + Interface + Customization.

3. **Per-Lot Business Capability workbooks (20 min for skeleton)** — for each Lot, one
   workbook with module-level FC / PC / CC / WA assessment. Module abbreviations
   commonly used: LSD (Sales/Distribution), PCM (Cost/Procurement), SRM (Supplier),
   LPM (Plant/Maintenance/Manufacturing), FAR (Fixed Assets), FGL (GL), AIS (AP/AR),
   HRC/HOM/HPA (HR Core / Org / Payroll). Each workbook is several hundred rows; build
   the skeleton, fill across additional sessions with module SMEs.

4. **Lot-4 non-functional set (15 min)** — Application Landscape List, Data Volume
   Template, TCO Template, Software License Sheet, Interface Detail Sheet,
   Customization Information Sheet. Lot-4 is what kills proposals when missed; never
   skip it.

5. **RFI Response presentation slide deck (10 min, if RFI not RFP)** — for the
   "early-stage" government bid where a Capability Overview is requested rather than
   a full Technical Proposal. Structure: Executive Summary headline (e.g. "275
   requirements assessed, 78% Fully Comply"), Understanding the Mission, Solution
   Architecture, Compliance Distribution (FC/PC/CC/WA), Why Oracle (or relevant
   platform), Implementation Roadmap, 5-Year Cost Estimation, Strategic Value.

6. **Compliance language calibration (5 min)** — government-formal Thai is mandatory.
   "ระบบรองรับ" not "ระบบมีฟีเจอร์"; "ผู้เสนอราคาให้บริการ" not "เราให้บริการ"; "ตามเอกสาร
   ประกวดราคา" not "ตามที่เสนอ". The QA file's Government-Formal typography pair must
   be used.

**Critical pitfalls:**
- Skipping ราคากลาง check. If the bid exceeds ราคากลาง without justification, the bid
  is non-responsive — automatic disqualification.
- Submitting a Technical Proposal when the procurement is e-bidding under พรบ. 2560
  Method 2 (Selection). Method 2 has stricter format requirements; check the procurement
  method first.
- Compliance Matrix in narrative paragraphs. Government procurement reviewers score
  cell-by-cell; a table is mandatory.
- Lot-4 forgotten. Functional capability without Application Landscape, TCO, and
  License sheets gets the bid down-marked even when functional comply is 100%.
- Bid security (หลักประกันการเสนอราคา) not attached or wrong format. Verify the TOR's
  required form: Bank Guarantee from an approved bank, Cash, or Insurance Bond.

**Output template hint:**
```
File 01 — e-GP Cover Sheet + ราคากลาง Acknowledgement
File 02 — Technical Proposal (8 sections, per WE-01)
File 03 — Compliance Matrix (TOR clause × FC/PC/CC/WA)
File 04+ — Per-Lot Business Capability Workbooks (Lot#1 / Lot#2 / Lot#3 / etc.)
File NN — Lot-4 Workbooks (Application List, TCO, Data Volume, License, Interface, Customization)
File NN+1 — Bid Security Document (Bank Guarantee or equivalent)
File NN+2 — Reference Customer Template
File NN+3 — RFI Response Presentation (if RFI stage)
```

Source patterns (six real Government / SOE anchors, pick by procurement stage):

- `[SOE: Multi-country Energy SOE]` ERP TOR Comply Lot#1–Lot#4, 2024 — multi-Lot,
  multi-workbook submission framework. Module abbreviations (LSD / PCM / SRM / LPM /
  FAR / FGL / AIS / HRC / HOM / HPA) define the Lot-level Business Capability sheets
  inside each Lot workbook. Use when the customer's TOR is structured as multiple
  functional Lots plus a Lot-4 non-functional bundle.

- `[QUASI-GOVT: Pharmaceutical Manufacturing Institute]` RFI Response V01R04, 2026.05
  — 20-slide bilingual deck with FC/PC/CC categorisation. Headline-metric framing
  ("275 requirements assessed, 78% Fully Comply") shifts the reader to the comply
  distribution in 10 seconds, before any solution-architecture detail. Use when the
  customer is at the RFI stage and a capability overview is requested rather than a
  full Technical Proposal.

- `[SOE: Export-Import Bank]` Technical Proposal V01R05, 2026.05 — 8-section
  TOR-Comply structure with Section 8 Compliance Matrix. Best anchor for the **prose
  body** of a SOE Bank Technical Proposal.

- `[SOE: Agricultural Cooperatives Bank]` ERP Demo Applications V02R01, 2025.07 —
  137-slide Oracle EBS Bank demo. Reach for this when the SOE Bank deal calls for a
  demo (not a proposal): Finance Modernization for Banking Reference Architecture,
  Oracle FSI Reference Table (Thai Bank A/B comply summary), PCI DSS Type II + SOX
  upfront, End-to-End Budget Control Process Flow, Budgeting Workflow with Executive
  ↔ Budget Coordinator interaction explicit.

- `[SOE: Agricultural Cooperatives Bank]` ERP Digital Transformation Roadmap, 2026.04
  — 32-slide three-topic Roadmap deck. Pattern: (1) แนวทางการพัฒนาระบบ — Oracle
  Tech Stack, Solution Architecture, EBS, Finance Analytics, One-UI, Personalize
  Workbench, Event-Driven Integration, Process Orchestration, REST APIs, Cyber
  Security aligned with กมช. + PDPA; (2) ความเสี่ยงและการลด — risk register with
  category and named owner; (3) ประมาณการ 5 ปี — investment estimation with DC + DR
  Network Diagrams. Use this when the customer wants a Roadmap rather than a Comply
  document — distinct shape, distinct audience (CIO Office, not Procurement).

- `[SOE: Government Savings Bank]` Hyperion Draft TOR v1.3, 2023 + ERP Business
  Requirements FIS / HRIS / Non-Functional, 2026.04 — RFI-stage workbook bundle plus
  TOR draft. Three key patterns:

  (a) **TOR document structure for SOE-Bank Hyperion / EPM**: บทนิยาม / qualifications
      / Document Sets 1+2 / Price-Performance scoring (NOT lowest-price) / 4-งวด
      payment milestones / 7 ภาคผนวก (System Spec / Cloud Infrastructure / Deliverables
      / Training / Personnel Qualification / Price-Performance Scoring / Maintenance).
      Use when the procurement runs under a SOE Bank's own procurement rules rather
      than central พรบ. 2560.

  (b) **Business Requirements workbook structure**: FIS workbook has 6 module sheets
      (AP / AM / Budget / GL / Mgmt Acct / Branch Support); HRIS workbook has 9
      process-group sheets (Org Structure / Recruit-Transfer / Employee Data /
      Learning / Performance / Rewards / Time-Leave / Labour Relations / Separation).
      Each row carries Process Group → Main Process → Sub-Process → Business
      Requirement Title → Description → System → Responsible Dept. This is the
      **row-level Compliance Matrix format** for SOE Banks — denser than the central-
      government Lot model.

  (c) **Third-party-consultant-facilitated NFR pattern**: the Non-Functional
      Requirement workbook is framed by an external advisor — visible because the
      workbook carries two consultant-named columns ("Client Feedback Classification"
      + "Clarification") alongside the vendor's Comply Y/N column. Recognise the
      pattern: an external advisory firm has run requirements gathering and approval
      cycles before the bid opens; the bidder must respond inside the consultant's
      structure. Do not re-shape the workbook; complete the Comply column row by row
      and let the consultant's clarification column carry the requirement-specific
      interpretation. The advisor's name (visible in the workbook header) is a
      procurement-process fact, not a vendor reference — handle it accordingly when
      writing the responding proposal.

# Section 2 — Quick Reference Cards

## QRC-01 Competitor Battle Card

**When to invoke:** A specific competitor (Vendor-A) is in the deal; sales needs a
one-page card to handle objections and reframe the win.

**Skill chain:** `strategic-thinking → product-skill → why-thinking`

**Critical thinking checklist:**
- Who is Vendor-A's natural champion in this customer? Why?
- What are Vendor-A's two strongest claims that the customer will repeat back?
- For each Vendor-A claim — true / partially true / false?
- What is iCE's two-line counter-frame (not denial, reframe)?
- What is the one customer-specific proof point that swings the deal?
- What is the trap to avoid? (e.g. arguing on Vendor-A's terms)

**Output template hint:**
```
1. Vendor-A claim → iCE reframe (3 rows max)
2. Customer-specific proof point (1 line, named)
3. The trap to avoid (1 line)
```

---

## QRC-02 Win Theme / Win Plan

**When to invoke:** Active pursuit with named decision-makers; need a written
articulation of the few themes that will carry the deal.

**Skill chain:** `strategic-thinking → why-thinking → solution-selling`

**Critical thinking checklist:**
- Three win themes max — more dilutes the message.
- Each theme answers: Why Change (their problem), Why Us (our differentiator), Why
  Now (the forcing function).
- For each theme — is there a champion who will repeat it? If no, the theme dies.
- Are the themes anchored in something the customer has said, or are they vendor wish?
- What is the disqualifier — what would invalidate each theme?

**Output template hint:**
```
Theme 1: <one-line statement>
   Why Change · Why Us · Why Now · Champion · Disqualifier
Theme 2: ...
Theme 3: ...
```

---

## QRC-03 Reference Customer / Case Study

**When to invoke:** Customer asks "do you have someone like us who has done this?" —
short answer must be a credible specific example, not a logo wall.

**Skill chain:** `strategic-thinking → product-skill`

**Critical thinking checklist:**
- Industry adjacency: same industry > adjacent industry > size match > geography.
- Use case adjacency: same module set > similar module set > overall ERP.
- Verifiable detail: named customer requires customer consent; otherwise anonymise.
- Three points only: who they were, what changed, what they got. Resist longer.

**Output template hint:**
```
Customer (anonymised if no consent)
Before — what they had
What changed — module + timeline + scope
Outcome — measured benefit, with caveats
```

---

## QRC-04 Negotiation Playbook (Deal-Level Strategy Sheet)

**When to invoke:** Final-round pricing or scope negotiation, often with procurement
present.

**Skill chain:** `solution-selling → relationship-management`

**Deep reference:** This is the strategy-sheet form. For the full tactical playbook —
Position vs Interest excavation, BATNA/ZOPA computation, Logrolling catalogue,
Conditional-Offer templates, Tricks-Defense protocols, and walk-away discipline — read
`b2b-solution-selling/references/10-negotiation-playbook.md` (Component 10). Pair this
strategy sheet with that playbook for any high-stakes deal.

**For the in-room tactical card** (4-step objection handling, conditional-offer one-liner,
trick defuses) use **QRC-11 — Negotiation In-Room Field Card (Bilingual)** below.

**Critical thinking checklist:**
- What is our walk-away (must hold)? What is our give-away (can flex)?
- What is the customer's procurement constraint (budget cycle? ราคากลาง? subscription
  policy?)
- What are the trades worth? Faster timeline costs us money but saves them risk —
  what is that worth to them?
- Who is in the room? Procurement + business owner + IT — each has different levers.
- What is the post-deal lever? Renewal upside, expansion in 12 months, AMS attach.

**Output template hint:**
```
Walk-away: <number / scope item>
Give-away: <which line items can flex>
Trade matrix: <flex item × concession value>
Room map: <who decides which lever>
Post-deal upside: <12-month expansion theme>
```

---

## QRC-05 Sales Forecast / Pipeline Health

**When to invoke:** Pipeline review with named deals at named stages; need a quick
read of forecast confidence.

**Skill chain:** `strategic-thinking → relationship-management`

**Critical thinking checklist:**
- For each deal — confirmed-close vs likely-close vs at-risk.
- For each deal — is there a champion? An economic buyer named? A documented decision
  criterion? Paper-process understood?
- For each deal — what is the single most likely reason it slips one quarter?
- What is the pipeline cover ratio (3x of target? 2x? Below 2x = stress).
- What deals are stalled (no movement in 30 days)? Stalled deals need a different
  intervention than slow deals.

**Output template hint:**
```
Deal × Stage × Confidence (3-band) × Champion present? × Slip-risk
Pipeline cover ratio
Stalled-deal list (with reason hypothesis)
```

---

## QRC-06 Partner / Channel Strategy

**When to invoke:** Considering a partner or channel motion — implementation partner,
local reseller, ISV, hyperscaler co-sell.

**Skill chain:** `strategic-thinking → design-thinking`

**Critical thinking checklist:**
- What does the partner own that iCE doesn't (and vice versa)?
- Where does the partner economics squeeze ours — and is that worth the volume?
- Customer-facing single throat to choke or shared accountability?
- Conflict cases: what if partner refers a deal to a different ISV?
- Renewal / expansion split — who owns it in year 2?

**Output template hint:**
```
Partner Type · What they bring · What we keep · Economics · Conflict policy · Year-2 ownership
```

---

## QRC-07 Industry Trend Briefing

**When to invoke:** Sales or marketing asks for a quick read on what's moving in a
specific industry segment — to inform messaging, account planning, or content.

**Skill chain:** `strategic-thinking → product-skill`

**Critical thinking checklist:**
- Three macro trends moving the industry — sourced, not invented.
- For each trend — implication for technology adoption in 12–24 months.
- Where does the platform iCE sells fit each trend? Where does it miss?
- Which sub-segment is most affected? (helps target accounts)
- What is the disqualifying counter-trend? (helps avoid blind spots)

**Output template hint:**
```
Trend 1 — driver · implication · iCE relevance · counter-trend
Trend 2 — ...
Trend 3 — ...
```

---

## QRC-08 Customer Health Score / Churn Risk

**When to invoke:** Customer Success or AMS team reviewing an existing account;
need a quick read on whether the customer is at risk of churn or expansion.

**Skill chain:** `relationship-management → questioning`

**Critical thinking checklist:**
- Health signals — usage (active users, transaction volume), SLA breaches, support
  ticket trend, executive sponsorship strength, satisfaction signals.
- Risk signals — competitor mention, leadership change, M&A in customer org, payment
  delay, public negative posture.
- Expansion signals — new use case mentioned, expansion brief asked, parallel
  business unit interest.
- Engagement cadence — last exec touch, last QBR, last functional review.
- What's the single intervention this month?

**Output template hint:**
```
Health: Green / Yellow / Red (with 2-line reasoning)
Top risk signal · Top expansion signal · Engagement cadence
Single intervention recommended this month
```

---

## QRC-09 Bid / No-Bid Decision

**When to invoke:** TOR received; before investing pursuit effort, decide go/no-go.

**Skill chain:** `strategic-thinking → solution-selling`

**Critical thinking checklist (7 disqualifying conditions — 5 or more = No Bid):**
1. Eligibility — is iCE actually qualified? (size, registration, prior project
   threshold)
2. Capability fit — is the proposed platform a real fit, or a stretch?
3. Champion presence — is there a named internal advocate?
4. Decision criteria — are they visible, or hidden?
5. Competition — how many incumbents have advantage in this TOR?
6. Economics — does the price band cover iCE delivery cost + margin?
7. Timeline — can iCE actually deliver on the stated timeline?

**Output template hint:**
```
Bid / No-Bid: <decision>
Disqualifying condition count: <N>/7
Top three risks if Bid: <list>
Top one trigger that would flip the decision: <condition>
```

---

## QRC-10 Voice of Customer / NPS

**When to invoke:** Quarterly or post-implementation; need to translate raw customer
feedback into actionable themes for product, support, and account team.

**Skill chain:** `questioning → relationship-management`

**Critical thinking checklist:**
- Are the responses self-selected (motivated detractors over-represent)?
- Three themes that drive promoter behaviour — name them.
- Three themes that drive detractor behaviour — name them.
- Is there one process change that would flip 5+ detractors to passives?
- What is the regrettable-loss list this quarter (customers who churned despite
  intervention)?

**Output template hint:**
```
NPS score (with confidence note on sample size)
Top promoter theme (3 lines) · Top detractor theme (3 lines)
Single process change recommended this quarter
Regrettable losses list (with root cause)
```

## QRC-11 Negotiation In-Room Field Card (Bilingual)

**When to invoke:** You are about to walk into a final-pricing meeting, a BAFO round, an
objection-heavy call, or any conversation where the customer is pushing back on price,
scope, or terms — and you need a one-page card you can review in the lift on the way up.

**เมื่อใช้:** ใช้ก่อนเข้าประชุมเจรจาราคารอบสุดท้าย รอบ BAFO หรือสถานการณ์ที่ลูกค้า
กดดันเรื่องราคา / scope / เงื่อนไข — เปิดอ่านในลิฟต์ก่อนขึ้นห้องประชุม

**Deep reference / อ้างอิงเต็ม:** `b2b-solution-selling/references/10-negotiation-playbook.md`
(Component 10). This card is the field-summary; the playbook is the deep manual.

**Skill chain:** `solution-selling (Component 10) → why-thinking → (relationship-management)`

---

### 1. Before You Walk In — เตรียมก่อนเข้าห้อง

| EN | TH |
|---|---|
| Write down our BATNA in one sentence. | เขียน BATNA ของเราเป็นประโยคเดียว |
| Write down our Walk-Away Point on paper, keep in jacket. Do not show. | เขียน Walk-Away Point บนกระดาษ พกในแจ็คเก็ต ห้ามให้เห็น |
| Calibrate the anchor: 15–25 % above the number we expect to land on, with a 2-line story. | ตั้ง Anchor ที่ 15–25 % สูงกว่าตัวเลขที่คาดว่าจะจบ พร้อมเหตุผล 2 ประโยค |
| Have 3 tradeable variables in your pocket (not just price). | มี 3 ตัวแปรที่แลกได้ในกระเป๋า (ไม่ใช่แค่ราคา) |
| Confirm: is the Economic Buyer in the room, or only a recommender? | ยืนยัน: Economic Buyer อยู่ในห้องหรือเป็นแค่ผู้แนะนำ? |

---

### 2. The 4-Step Objection Protocol — โปรโตคอลตอบข้อโต้แย้ง 4 ขั้น

Use this **every time** the customer raises an objection — including "your price is too
high." Never respond to the first thing they say.

ใช้ **ทุกครั้ง** ที่ลูกค้ายกข้อโต้แย้ง — รวมถึง "ราคาแพงเกินไป" ห้ามตอบสิ่งแรก
ที่เขาพูดทันที

| # | Step | EN script | TH script |
|---|---|---|---|
| 1 | **Listen + capture** | (Pause two beats. Write down what they said, verbatim.) | (เว้นจังหวะสองวินาที จดสิ่งที่เขาพูดตรง ๆ) |
| 2 | **Lock the scope** | "Beyond this point, is there anything else keeping you from moving forward today?" | "นอกจากประเด็นนี้แล้ว ยังมีเรื่องอื่นอีกไหมที่ทำให้คุณยังไม่ตัดสินใจครับ?" |
| 3 | **Prioritise** | "Of these, which one is most important to resolve first?" | "ในบรรดาเรื่องเหล่านี้ เรื่องไหนสำคัญที่สุดที่ต้องแก้ก่อนครับ?" |
| 4 | **Solve the right one** | Match tool to objection (see table below) | จับคู่เครื่องมือกับประเภทข้อโต้แย้ง (ดูตารางด้านล่าง) |

**Match the tool to the objection / จับคู่เครื่องมือ:**

| Objection type / ประเภทข้อโต้แย้ง | Use / ใช้ |
|---|---|
| ROI is not real / ROI ไม่จริง | Logos — recompute, show comparable customer outcome |
| Budget is fixed / งบจำกัด | Variable Shift — payment terms, phasing, scope tier |
| Timeline is impossible / Timeline ไม่ทัน | Scenario — realistic plan + contingency, named owners |
| Cannot trust delivery / ไม่มั่นใจในทีม | Social Proof — named reference, escorted site visit |
| Relationship risk / กลัวเสียความสัมพันธ์ | Personal commitment — exec sponsor named in writing |

---

### 3. The Conditional Offer — กฎเหล็กการแลกเปลี่ยน

> **EN:** "If you [thing valuable to us], then I can [thing valuable to you]."
>
> **TH:** "หากคุณ [สิ่งที่มีค่าต่อเรา] ผมถึงจะ [สิ่งที่มีค่าต่อคุณ] ได้ครับ"

**No concession travels alone. Ever.**
**ทุกการให้ต้องมีการขอแลกเสมอ ห้ามให้ฟรี**

**Common trades / สิ่งที่ขอแลกได้บ่อย:**
faster payment terms · multi-year commitment · reference customer rights · case-study
publication rights · steering-committee cadence written into SOW · earlier Phase-2
commitment letter · joint marketing material · executive QBR access.

---

### 4. Tricks-Defense Cheat Sheet — รับมือเล่ห์เหลี่ยม

| Trick | Symptom | Defuse (EN) | Defuse (TH) |
|---|---|---|---|
| **Good Cop / Bad Cop** | One person hardballs, another "rescues" with a still-bad offer | "I appreciate the flexibility. Let me restate the full package." | "ขอบคุณที่ยืดหยุ่นครับ ผมขออนุญาตทบทวน package ทั้งหมดอีกครั้ง" |
| **The Nibble** | Small extras requested *after* the deal seems agreed | Run every late ask through Conditional Offer above | ใช้ Conditional Offer กับทุกการขอเพิ่มหลังตกลงแล้ว |
| **Higher Authority** | "Board / CFO needs to approve" appears late | Ask upfront: "Who needs to be in the room for us to agree today?" Reserve negotiating room for the higher-authority meeting | ถามก่อน: "ต้องมีใครในห้องเพื่อตัดสินใจวันนี้?" เก็บพื้นที่ต่อรองสำหรับห้องผู้บริหาร |
| **Take It or Leave It** | Ultimatum with fast deadline | Ask one question that the ultimatum cannot answer; if refused, return to BATNA gracefully and leave | ถามคำถาม 1 ข้อที่คำขาดตอบไม่ได้ ถ้าปฏิเสธ ให้ถอยกลับไปยัง BATNA อย่างสุภาพและเดินออก |

---

### 5. Walk-Away Test — เช็คก่อนเซ็น

Before saying yes to any final offer, run silently in your head:

ก่อนตอบ "ตกลง" ในข้อเสนอสุดท้าย ถามตัวเองเงียบ ๆ:

| EN | TH |
|---|---|
| Is this deal better than our BATNA? | ข้อตกลงนี้ดีกว่า BATNA ของเราหรือไม่? |
| Did we trade for every concession we gave? | เราขอแลกทุกครั้งที่เราให้หรือไม่? |
| Will the Champion be able to defend this internally without us in the room? | Champion จะปกป้องข้อตกลงนี้ภายในองค์กรลูกค้าได้โดยไม่มีเราในห้องหรือไม่? |
| Have we summarised the package back and got "yes, that captures it" in writing? | เราสรุป package กลับและได้ "ใช่ ครบแล้ว" เป็นลายลักษณ์อักษรหรือยัง? |
| If we walk away today, can we live with that outcome? | ถ้าเราเดินออกวันนี้ เรารับผลที่ตามมาได้ไหม? |

**If three or more answers are "no" — pause the deal. Do not close to a sub-BATNA deal
because the quarter is closing.**

**หากตอบ "ไม่ใช่" ตั้งแต่ 3 ข้อขึ้นไป — หยุดปิดดีล ห้ามเซ็นข้อตกลงที่แย่กว่า BATNA
เพียงเพราะใกล้สิ้นไตรมาส**

---

### 6. The 24-Hour Written Summary — สรุปเป็นลายลักษณ์อักษรภายใน 24 ชม.

Within 24 hours of verbal agreement, send a written-summary email that restates the
package and the next step. Copy the Economic Buyer if possible. This is not a contract;
it is the document that survives the next re-org on their side and the next selective
memory on either.

ภายใน 24 ชั่วโมงหลังตกลงด้วยวาจา ส่งอีเมลสรุป package และ Next Step โดยสำเนาถึง
Economic Buyer หากเป็นไปได้ นี่ไม่ใช่สัญญา — แต่คือเอกสารที่จะอยู่รอดผ่านการ
ปรับโครงสร้างองค์กรลูกค้าและความจำที่เลือกของทั้งสองฝ่าย

---

**End of QRC-11. For deep tactics, return to Component 10 in `b2b-solution-selling`.**
**จบ QRC-11 สำหรับเทคนิคเชิงลึก กลับไปอ่าน Component 10 ใน `b2b-solution-selling`**

---

# Section 3 — Anti-Patterns

These are the recurring failure modes that show up across all eight WEs. Watch for
them before saving.

| Anti-Pattern | Symptom | Fix |
|---|---|---|
| Vendor monologue | Slides 1–5 are about iCE, not about the customer | Move iCE introduction to back of deck or covering letter |
| Feature parade | Demo slides list product features, not customer outcomes | Reframe every feature as "this addresses customer's pain X" |
| Generic compliance | Compliance Matrix says "FC" for every clause without evidence | Pair every FC marker with a 1–2 line evidence column |
| Synthetic discovery | "Pain Points" sound like vendor pitch, not customer language | Anchor in real discovery quotes or flag `[ASSUMED]` |
| Methodology theatre | Body uses a named methodology or framework brand instead of plain prose | Translate the concept into business language; never let the brand name reach the reader |
| Symmetric three-options | Three options where two are visibly straw men | Make options genuinely different in shape (scope, vendor, sequencing) |
| Risk wishes | Risk register without owners | Every risk gets a named owner; otherwise it is a wish |
| Optional erasure | Single mandatory price with no optional add-ons | Always include 1–2 optional add-ons for negotiating room |

# Section 4 — Quality Gates

Before saving any deliverable produced via this playbook, run these gates in order:

| Gate | What it checks | Pass condition |
|---|---|---|
| 1. Anti-AI sweep | Step 9 vocabulary from Protocol V6.0 | No "leverage / robust / comprehensive / seamless"; no "เป็นที่ทราบกันดีว่า / ปฏิเสธไม่ได้ว่า" |
| 2. Burstiness check | Sentence-length variety, opening variety | SD of sentence length ≥ 5; ≥ 5 different opening forms in main paragraphs |
| 3. Name-drop scan | Body must contain zero firm names, zero methodology brands | Zero hits on the H9 list |
| 4. Anti-hallucination | Every number / name / date traces to a real source | All inferred items flagged `[ASSUMED]` or `[VALUE TBD]` |
| 5. Typography & Bilingual QA | Font pairing, x-height balance, spacing | Run `typography-bilingual-qa.md` checklist |
| 6. Pre-Save Confirmation | Filename, version stamp, location confirmed with user | User confirms before save |

End of Orchestration Playbook.
