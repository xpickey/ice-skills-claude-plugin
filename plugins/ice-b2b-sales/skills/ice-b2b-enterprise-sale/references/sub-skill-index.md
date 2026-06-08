# Sub-Skill Index
**Version:** V02R02 | **Date:** 2026.05.22 | **Companion to:** `../SKILL.md`

# Section 0 — How to Use This Index

This index answers three questions that come up mid-chain:

1. **Which skill should I reach for first?** → Section 1 (Tier map A/B/C)
2. **Two skills look the same — which one do I pick?** → Section 2 (Disambiguation)
3. **The customer is in industry X — does that change the chain?** → Section 3 (Industry × Product)

A normal session opens this file for one row, applies, and closes. The index is
calibrated to Pichai's actual workload distribution: 70 % pre-sales heavy, Oracle-centric
(Fusion 30 % + EBS 20 % + NetSuite 20 % = 70 %), and rotating across ten industry
segments. Skills frequency follows that mix, not what looks academically balanced.

Tiers are named, not ranked by quality. Tier-A is "first-call" because the work hits it
every week. Tier-C is "occasional" because the underlying customer scenario is real but
infrequent. Tier-D is empty by design — if a skill is never used, it does not need a
slot in the index; remove it instead.

# Section 1 — Skill Inventory by Tier

## 1.1 Tier A — First-Call Skills (5)

These are the spine of every pre-sales pursuit. Expect to invoke at least one Tier-A
skill in every chain, often two.

### 1.1.1 b2b-questioning

**Reach for it when:** designing discovery questions, building a qualification list,
preparing for a customer call, drafting a follow-up email, or summarising meeting notes.

**Inputs it expects:** customer name (or anonymised handle), meeting purpose, known
pains (if any), audience role.

**Outputs it produces:** a question set ordered by purpose (Situation, Problem,
Implication, Payoff), with paired-question alternatives for kreng-jai dynamics.

**Pairs naturally with:** solution-selling (qualification scoring sequel),
relationship-management (champion identification), product skills (technical follow-up).

**Avoid using it when:** the artifact is a multi-section proposal — questioning is for
verbal/exchange artifacts, not for documents.

---

### 1.1.2 b2b-solution-selling

**Reach for it when:** building a pain sheet, scoring a deal on economic-buyer /
decision-criteria / champion / paper-process axes, writing a business case section,
constructing the value-narrative for a proposal.

**Inputs it expects:** discovery findings (real pains, not generic), stakeholder names
and roles, current-state pain quantification (or `[ASSUMED]` flag).

**Outputs it produces:** pain-to-value chain, qualification scorecard, business-case
prose, win-themes alignment, negotiation playbook with Conditional-Offer templates,
price-defense talk-tracks, BATNA/ZOPA computation, and the 4-step objection-handling
protocol (see `references/10-negotiation-playbook.md` inside that skill).

**Pairs naturally with:** strategic-thinking (frames the deal), product skills (proves
feasibility), why-thinking (sharpens narrative).

**Avoid using it when:** the request is purely informational (RFI-only with no
proposal) — qualification logic adds noise to an info exchange.

---

### 1.1.3 b2b-strategic-thinking

**Reach for it when:** framing a deal that is bigger than a single artifact, deciding
where to play / how to win in a market or segment, building win-plan logic, choosing
positioning against a competitor, writing the Why-Now and Why-Us narrative for an
executive audience.

**Inputs it expects:** the strategic question (not the artifact), context on the
customer's market, hypothesis of what is changing.

**Outputs it produces:** issue tree, prioritised options with trade-offs, recommended
position, narrative skeleton.

**Pairs naturally with:** why-thinking, solution-selling, presentation-creator.

**Avoid using it when:** the task is execution-level only (e.g. format a deck the user
already wrote) — strategy frame is overkill.

---

### 1.1.4 b2b-presentation-creator

**Reach for it when:** the deliverable is a .pptx — proposal deck, pitch, demo deck,
RFI/RFP response slides, board paper slides, QBR/EBR deck, demo script slides.

**Inputs it expects:** deck purpose, audience, narrative arc (from the upstream chain),
brand/theme preference, time-budget.

**Outputs it produces:** slide-by-slide structure, layout patterns, suggested visuals,
typography pairing aligned with the QA file.

**Pairs naturally with:** solution-selling (proposal narrative), product skills
(technical deep-dive slides), strategic-thinking (executive opener).

**Avoid using it when:** the artifact is a .docx, .xlsx, or inline reply — presentation
patterns do not transfer cleanly.

---

### 1.1.5 fin-tech-consulting

**Reach for it when:** the deal touches Lending / Loan Origination, NPL/NPA, IFRS9 /
TFRS9, Digital Banking, Payment Systems, Credit Risk Engines, or any Bank/Securities
/Insurance back-office transformation. Tier-A despite FinTech being only ~10 % of
customer mix — when it hits, it dominates the deal economics.

**Inputs it expects:** Bank/NBFI type, regulatory posture (BoT / SEC / TFRS9 maturity),
existing core system, target capability.

**Outputs it produces:** FinTech-specific business case, regulator-aware architecture,
NPL/NPA process flow, IFRS9 staging logic, capability roadmap.

**Pairs naturally with:** product skills (when an Oracle ERP/EPM is the underlying
platform), strategic-thinking (for transformation framing), solution-selling (for the
business case).

**Avoid using it when:** the customer is not regulated as a financial entity. F&B and
Retail with credit cards do not trigger this skill.

## 1.2 Tier B — Frequent Skills (7)

Layer these onto the spine when the deal context calls for it. Each one has a clear
trigger — do not invoke without it.

### 1.2.1 b2b-design-thinking

**Trigger:** the deliverable is a workshop, an ideation session, or a multi-stakeholder
group discovery (not a 1:1 discovery call).

**Where in the chain:** at the front, before solution-selling, when the work is
genuinely a workshop. Otherwise skip.

---

### 1.2.2 b2b-why-thinking

**Trigger:** the deliverable needs a Why-Change / Why-Now / Why-Invest / Why-Us /
Why-Stay narrative — typically board paper, executive briefing, win plan, renewal pitch.

**Where in the chain:** after strategic-thinking, before presentation-creator. It
sharpens the narrative spine; do not use it as a substitute for strategic-thinking.

---

### 1.2.3 oracle-cloud-applications-consulting

**Trigger:** Oracle Fusion Cloud (ERP/EPM/SCM/HCM), OCI, Redwood UX, Pillar Two TRCS,
AI Agent Studio, FCCS/ARCS/EPBCS, Touchless AP, OIC Gen3.

**Where in the chain:** after solution-selling, before domain-overlay skills.

**Coverage gaps to watch:** quarterly release adoption deadlines (e.g. 26D/27A
Redwood), Pillar Two activation timelines.

---

### 1.2.4 oracle-ebs-consulting

**Trigger:** Oracle EBS R12.2 (latest 12.2.15), ADOP patching, EBS Cloud Manager,
EBS-to-OCI lift-and-shift, EBS modernisation roadmap, Stay/Modernise/Migrate decision.

**Where in the chain:** after solution-selling, before domain-overlay skills.

**Coverage gaps to watch:** Premier Support timeline to 2037 — use this as the
"do-nothing" risk anchor in business cases.

---

### 1.2.5 oracle-netsuite-consulting

**Trigger:** NetSuite ERP, SuiteSuccess methodology, SuiteAgents (2026.1 AI surface),
NSAW, OneWorld topology, Thai localisation (MyInvois, e-Tax, VAT/WHT, Coretax), 
SuiteCloud.

**Where in the chain:** after solution-selling, before domain-overlay skills.

**Coverage gaps to watch:** OneWorld licence sizing per legal entity is the most
common scoping mistake; double-check before publishing pricing.

---

### 1.2.6 advisor-govt-gfmis

**Trigger:** Thai government Finance / Budget / Treasury / FM / e-LAAS / GFMIS
integration / Vendor Master / Run Payment / BAHTNET/SMART / Accrual Accounting / 
Public-sector COA / Year-end Closing.

**Where in the chain:** after product, before presentation-creator.

**Avoid using it when:** the deal is private sector. GFMIS context does not transfer.

---

### 1.2.7 govt-egp-gfmis

**Trigger:** Procurement Law (พรบ. 2560), ระเบียบกระทรวงการคลัง, e-GP, e-bidding,
e-market, TOR Response, Compliance Matrix building, ราคากลาง, หลักประกัน, ค่าปรับ,
การอุทธรณ์, การทิ้งงาน, e-Tax government, สัญญา IT ภาครัฐ.

**Where in the chain:** after product, before presentation-creator. Mandatory for
รัฐวิสาหกิจ and ราชการ TOR responses.

**Avoid using it when:** the customer is private sector or quasi-government with their
own procurement rules — confirm regulator scope before invoking.

## 1.3 Tier C — Occasional Skills (1)

### 1.3.1 b2b-relationship-management

**Trigger:** the deliverable is for an existing customer — QBR / EBR / Renewal /
Expansion / Customer Health / Escalation Recovery / Stakeholder Map for an active
account.

**Where in the chain:** as the lead skill for Existing-customer work (D-14 through
D-17 in the decision matrix).

**Why Tier-C and not Tier-B:** existing-customer work is ~25 % of workload, but when
it does come up, this skill is the spine, not a layer. Treat it as Tier-A inside its
context.

## 1.4 Tier D — Rare or Never (Empty by Design)

No skills in this tier. If usage data shows a skill never gets invoked, the action is
to retire it, not to demote it.

# Section 2 — Disambiguation Table

Four overlap pairs trip up routing. Use this table to decide quickly.

## 2.1 b2b-strategic-thinking ↔ b2b-why-thinking

| Question | strategic-thinking | why-thinking |
|---|---|---|
| What does it do? | Frames the deal; picks the lens (where-to-play, how-to-win, options + trade-offs) | Sharpens the narrative spine — Why-Change / Why-Now / Why-Us / Why-Stay |
| Best use case | Win plan, account strategy, pursuit framing, market/segment positioning | Board paper, executive briefing, win-themes finalisation |
| Output shape | Issue tree, options, recommendation | Five-question narrative, headline statements |
| When both fit | Use strategic-thinking first (frame), then why-thinking (sharpen). Do not invert. |

**Rule of thumb.** If the question is "should we?", reach for strategic-thinking. If
the question is "how do we say it?", reach for why-thinking.

## 2.2 b2b-solution-selling ↔ b2b-questioning

| Question | solution-selling | questioning |
|---|---|---|
| What does it do? | Builds a pain-to-value chain, qualification scoring, business case spine | Designs questions for discovery, calls, follow-ups, prep |
| Best use case | Proposal / Business case / Pursuit qualification | Discovery prep / Follow-up email / Meeting summary |
| Output shape | Pain sheet, scorecard, business-case prose | Question set in purpose order |
| When both fit | If the artifact is a question list → questioning only. If the artifact is a proposal → solution-selling; questioning is internal-only. |

**Rule of thumb.** Questioning helps you find the truth. Solution-selling helps you
convey the value once you've found it. Two different jobs.

## 2.3 b2b-design-thinking ↔ b2b-questioning

| Question | design-thinking | questioning |
|---|---|---|
| What does it do? | Multi-stakeholder workshop facilitation, ideation, journey mapping | 1:1 discovery, call prep, follow-up |
| Best use case | Envisioning workshop, design sprint, "How Might We" session | One conversation at a time |
| Output shape | Workshop agenda, exercises, artefacts | Question set |
| When both fit | Workshop → design-thinking. 1:1 call → questioning. They rarely overlap in practice. |

**Rule of thumb.** If three or more people are in the room, design-thinking. If two,
questioning.

## 2.4 advisor-govt-gfmis ↔ govt-egp-gfmis

| Question | advisor-govt-gfmis | govt-egp-gfmis |
|---|---|---|
| What does it do? | Finance / Budget / Treasury — GFMIS, FM, e-LAAS, Vendor Master, Run Payment, BAHTNET/SMART, Accrual, Year-end | Procurement / Bidding — พรบ. 2560, e-GP, TOR Response, Compliance Matrix, ราคากลาง, หลักประกัน |
| Best use case | Government finance modernisation, GFMIS integration design, public-sector accounting | TOR Response, e-bidding submission, procurement compliance matrix |
| Output shape | Finance/Budget/Treasury design, COA, integration spec | TOR clause-by-clause comply doc, e-GP submission readiness |
| When both fit | A full government deal often needs both — chain procurement first (govt-egp-gfmis for the TOR Response), finance/treasury second (advisor-govt-gfmis for the underlying system design). |

**Rule of thumb.** Procurement = how-we-win-the-bid. GFMIS = how-the-money-flows-after.

# Section 3 — Industry × Product Lookup Table

## 3.1 Industry Coverage Matrix

| Industry Segment | Typical Product Pairing | Domain Overlay | Typical Deliverable |
|---|---|---|---|
| Public Listed / Large Enterprise | Oracle Fusion (EPM-heavy) or EBS | PDPA layered | Technical + Commercial Proposal, Board Paper, Demo Design |
| Mid-market / SME | Oracle NetSuite | PDPA layered | Investment Proposal, Demo Design, Implementation Approach |
| ราชการ (Government Ministry) | Oracle Fusion or EBS | govt-egp-gfmis + advisor-govt-gfmis | TOR Response, e-Bidding, Compliance Matrix |
| รัฐวิสาหกิจ (SOE) | Oracle Fusion or EBS | govt-egp-gfmis + advisor-govt-gfmis (often both) | TOR Response (multi-Lot), Functional Capability Workbooks, Lot-4 (TCO/Interface/Customization) |
| องค์การในกำกับของรัฐ (Quasi-Govt) | Oracle Fusion or NetSuite | govt-egp-gfmis (lite) — depends on procurement framework | RFI Response, Capability Overview, 5-year Cost Estimation |
| อบจ. / เทศบาล / อปท. | SMART PAO platform or NetSuite | smart-pao-platform, advisor-govt-gfmis | TOR Response, อบจ. Application Landscape, Workflow Mapping |
| FinTech / Banking / NBFI | Oracle Fusion (Finance core) + fin-tech-consulting | legal-it-thailand-cloud (PDPA-heavy) | Technical Proposal (Bank-specific TOR), IFRS9 Engine Design, Lending Platform Architecture |
| Healthcare / Pharma | Oracle Fusion or NetSuite | govt-egp-gfmis (if public hospital) | RFI Response with GMP language, FMIS Design, Compliance Assessment |
| Trading / Wholesale / Distribution | Oracle NetSuite (often) or Fusion | PDPA layered | Investment Proposal, Demo Design, Multi-entity Rollout |
| Manufacturing | Oracle Fusion (Cost-heavy) or EBS legacy | PDPA layered | Technical Proposal, Cost-of-Production Model, Plant Maintenance Add-on |

## 3.2 Product-per-Industry Routing Rules

When the customer's industry is mentioned but the product is not, default to:

- **Public Listed + Mid-market + Trading + Manufacturing** → ask the user; Oracle Fusion
  vs. NetSuite is a real decision, not an assumption.
- **ราชการ + รัฐวิสาหกิจ** → default to Oracle Fusion unless the user explicitly says
  EBS. Government deals are increasingly Fusion-centric.
- **อบจ. / เทศบาล / อปท.** → default to SMART PAO platform. Only suggest Oracle Fusion
  if the customer is a large อบจ. with cross-province ambitions.
- **FinTech / Banking** → default to Oracle Fusion + fin-tech-consulting overlay.
- **Healthcare / Pharma** → ask; varies sharply between public hospital, private
  hospital chain, pharma manufacturer, and pharma distributor.

## 3.3 Placeholder Roadmap — Future Skills (Reserved)

These three slots are reserved for future skill creation. They are intentionally not
created in V02R01 because the customer concentration does not yet justify a dedicated
skill. When concentration crosses ~5 deals per year in one segment, promote.

| Reserved Slot | Trigger to Promote | Notes |
|---|---|---|
| `b2b-trading-fmcg` | When Trading / FMCG / Wholesale workload exceeds 5 active deals/year | Today: ~3 deals/year, handled by `oracle-netsuite-consulting` + Tier-A skills |
| `b2b-manufacturing` | When Manufacturing (discrete or process) workload exceeds 5 active deals/year | Today: ~3 deals/year, handled by Oracle Fusion/EBS skill + Tier-A |
| `b2b-healthcare` | When Healthcare (hospital, pharma) workload exceeds 5 active deals/year | Today: ~2 deals/year, handled by product skill + ad-hoc industry framing |

Until promotion, use the Industry × Product matrix above and flag industry-specific
content with `[ASSUMED: industry adjacency]` where the inference is not from a real
customer artifact.

## 3.4 Pure Consulting Branch

When the deal is not bound to a specific product — assessment, strategy, transformation
roadmap, vendor evaluation — drop the product skill and chain Tier-A only:

`strategic-thinking → why-thinking → solution-selling → (presentation-creator if .pptx)`

This is the right shape for: vendor-evaluation report, transformation readiness
assessment, capability maturity model, target operating model design, IT strategy paper.

# Section 4 — Stage × Skill Routing

This section is a one-page cross-reference if you start from a pursuit stage rather
than a deliverable.

| Pursuit Stage | Hot Skills | Optional Add-ons | Typical Artifact |
|---|---|---|---|
| Identify / Prospect | strategic-thinking, why-thinking | questioning | Industry brief, target list |
| Qualify | questioning, solution-selling | strategic-thinking | Qualification scorecard, pain sheet |
| Engage / Discover | questioning, design-thinking | solution-selling | Discovery script, workshop deck |
| Solution | solution-selling, product skill, presentation-creator | strategic-thinking | Technical + Commercial Proposal |
| Negotiate | solution-selling (Component 10), why-thinking | relationship-management | Negotiation Brief (D-21), Price Defense Sheet, final pricing |
| Close | why-thinking, solution-selling | relationship-management | Win plan signed-off, internal handover |
| Implement Handover | (out of scope) | (out of scope) | Handover briefing only |
| Renew / Expand | relationship-management, why-thinking | solution-selling | QBR, expansion pitch, CR |

# Section 5 — Skill Loading Rules

- **Load one Tier-A skill first.** Choose the spine (usually solution-selling or
  strategic-thinking). Layer Tier-B onto the spine — never the other way around.
- **Product skill is loaded second.** It anchors the solution discussion in real
  product capability. Skipping it produces vendor-agnostic content that does not help
  a specific deal.
- **Domain overlay is loaded after product.** This sequence prevents writing compliance
  language before the underlying solution is shaped.
- **Presentation-creator is always last.** It styles the output; it does not shape the
  content.
- **Typography QA runs after presentation-creator, before save.** It is a gate, not a
  skill — see `typography-bilingual-qa.md`.

# Section 6 — Maintenance Notes

- **When a new skill is added to the user's library**, place it into a tier in this file
  before the next chain runs. Default to Tier-B and watch usage for two months.
- **When a skill is renamed**, update all references in this index AND in
  `decision-matrix.md` Section 4 and Section 5. Misnamed routing is the #1 cause of
  silent skill-skipping.
- **When a placeholder slot is promoted** (Section 3.3), update the description in
  `SKILL.md` Section 1 (Triggers) to add the new industry vocabulary.
- **When a domain overlay scope changes** (e.g. new e-GP rule, PDPA amendment), update
  the trigger keywords in `decision-matrix.md` Section 5 — not here. This file lists
  skills, not legal scope.

End of Sub-Skill Index.
