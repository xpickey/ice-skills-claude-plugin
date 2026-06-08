---
name: ice-netsuite-thailand-advisory
description: Use when scoping, designing, proposing, or delivering an Oracle NetSuite engagement for a Thai or APAC organisation. Wraps Oracle's SuiteCloud Agent Skills with Thailand-specific localization (THB, TFRS, VAT/WHT, e-Tax Invoice, BOI, Pillar Two), Thai OneWorld topology decisions, and iCE Consulting's advisory voice for pre-sales, business case, and RFP/TOR response work. Triggers on NetSuite + Thailand, NetSuite Thai subsidiary, NetSuite OneWorld Thailand, e-Tax Thailand NetSuite, BOI NetSuite, TFRS NetSuite, ปรึกษา NetSuite, ติดตั้ง NetSuite, ระบบบัญชี NetSuite ไทย, ภาษีไทย NetSuite, TOR NetSuite ภาครัฐ, RFP NetSuite, business case NetSuite, ROI NetSuite Thailand. Designed to compose with netsuite-ai-connector-instructions, netsuite-owasp-secure-coding, netsuite-sdf-project-documentation, netsuite-sdf-roles-and-permissions, netsuite-suitescript-records-reference, netsuite-suitescript-upgrade, and netsuite-uif-spa-reference.
license: Proprietary — iCE Consulting
metadata:
  author: Pichai / iCE Consulting
  version: V01R01
  date: 2026.05.23
  base_spec: agentskills.io
  composes_with: oracle/netsuite-suitecloud-sdk
---

# iCE NetSuite Thailand Advisory Skill

Version: V01R01 | Date: 2026.05.23

## Purpose

Oracle's seven SuiteCloud Agent Skills cover the technical surface of NetSuite — SDF, SuiteScript, UIF SPA, secure coding, AI Connector, records reference, role permissions. They are excellent. They are also globally generic. This skill adds the layer that Thai and APAC engagements actually need:

- Local statutory and tax context the Oracle skills do not encode.
- A bilingual Thai-English deliverable voice that customers, ministries, and state enterprises here expect.
- The pre-sales and proposal framing iCE Consulting uses when positioning NetSuite against alternatives, defending price, and shaping a business case the CFO and the steering committee will both sign.

The skill is opinionated. It should be — that is what makes it useful next to the neutral Oracle baselines.

## When to invoke

Invoke this skill before you reach for the Oracle skills if the engagement has any of the following signals:

1. Customer is incorporated in Thailand, or has a Thai subsidiary inside a OneWorld topology.
2. Deliverable will be reviewed in Thai, or in mixed Thai-English.
3. Procurement runs under พรบ. การจัดซื้อจัดจ้างฯ 2560 or via e-GP.
4. BOI-promoted activities are in scope, or the customer holds BOI privileges that affect chart-of-accounts mapping.
5. Pillar Two (GloBE) reporting applies to the customer's group for FY 2025 onwards.
6. RFP, TOR, business case, or board paper is the target output, not just a working document.

When the work is purely technical — a SuiteScript bug, a UIF component, an SDF deployment — go straight to the Oracle skill that fits. This skill is the advisory wrapper, not a substitute.

## Composition pattern

Think of this skill as the orchestrator that loads context, then hands the engineering job to the Oracle skills.

```
1. ice-netsuite-thailand-advisory          ← engagement framing, Thai context, deliverable voice
   ├── netsuite-ai-connector-instructions   ← when AI Connector is part of the design
   ├── netsuite-sdf-project-documentation   ← when generating SDF docs/runbooks
   ├── netsuite-sdf-roles-and-permissions   ← when designing customrole XML
   ├── netsuite-suitescript-records-reference ← when writing or reviewing SuiteScript
   ├── netsuite-suitescript-upgrade         ← when migrating 1.0 → 2.1
   ├── netsuite-uif-spa-reference           ← when building UIF SPA components
   └── netsuite-owasp-secure-coding         ← always, on any code-bearing deliverable
```

Invocation example in a prompt:

```
Use $ice-netsuite-thailand-advisory to scope a NetSuite OneWorld implementation
for <customer>, a Thai manufacturing group with one BOI-promoted subsidiary
and two non-promoted subsidiaries. Output: business case section for the
board paper, in Thai with English glossary, V01R01.
```

The skill will frame the engagement (THB primary, BOI separation strategy, Pillar Two readiness, TFRS-to-NetSuite COA mapping) and then defer to `netsuite-sdf-project-documentation` for the runbook section if the prompt asks for one.

---

## SECTION 1 — Thailand statutory and tax context

Use these as design inputs, not as final regulatory advice. Verify with the customer's tax advisor and the latest Revenue Department announcements before commitment.

### 1.1 Currency and reporting

- Primary currency for any Thai subsidiary in OneWorld is THB.
- Group reporting commonly runs USD or the parent's home currency; configure consolidated currency at the parent subsidiary level with monthly FX revaluation.
- TFRS (Thai Financial Reporting Standards) is broadly converged with IFRS, but disclosure timing and lease accounting carve-outs apply for SMEs under TFRS for NPAEs. Confirm whether the customer reports under TFRS or TFRS for NPAEs before mapping the chart of accounts.

### 1.2 Indirect tax — VAT

- Standard VAT rate is 7 percent in Thailand (verified at time of writing; treat as a parameter and read the customer's tax setup, do not hardcode).
- Input VAT and output VAT are separately tracked. NetSuite's tax engine handles this through tax codes — configure separate codes for input, output, and zero-rated transactions.
- VAT registration threshold and timing matters for subsidiaries with growing local revenue — flag it during scoping so the customer's tax advisor confirms.

### 1.3 Withholding tax

- WHT rates vary by transaction type. Services to corporations are commonly withheld at 3 percent; rent at 5 percent; transportation at 1 percent — confirm against the customer's specific transaction profile and current PND/แบบ filings.
- NetSuite supports WHT through a combination of tax codes and a deduction at payment time. Decide early whether WHT will be recorded at invoice or at payment — the Thai tax point typically aligns with payment.
- PND 1, PND 3, PND 53 reporting needs the WHT-by-vendor extract. Design the report or saved search early; it is not in the standard NetSuite SuiteApp set.

### 1.4 e-Tax Invoice and e-Receipt

- The Revenue Department's e-Tax framework (e-Tax Invoice and e-Receipt) is the direction of travel for Thai indirect tax reporting. NetSuite does not natively issue Thai e-Tax documents to the RD's specification.
- Two pragmatic paths: (a) a localization SuiteApp from a Thai partner that handles XML formatting and RD submission, or (b) middleware integration to a certified e-Tax service provider. Both have trade-offs on cost, deployment time, and audit trail.
- Note for proposal framing: explicitly call out the e-Tax handling approach in the scoping section — leaving it ambiguous is a common dispute trigger during UAT.

### 1.5 BOI privileges

- BOI-promoted activities often require segregated cost and revenue tracking from non-promoted activities within the same legal entity. This drives one of three NetSuite design choices:
  1. Separate subsidiary per promotion (clean, but doubles master-data effort).
  2. Single subsidiary with classification/department/location dimension for BOI versus non-BOI.
  3. Multi-book accounting with secondary book for BOI reporting.
- Recommendation depends on volume of BOI transactions and audit complexity. State the choice and the rationale in the business case — auditors and BOI inspectors will ask.

### 1.6 Pillar Two (GloBE)

- Thailand has adopted the GloBE rules. Groups with consolidated revenue above the threshold (EUR 750 million in two of the last four years) face top-up tax obligations.
- For NetSuite, the design implication is data — effective tax rate per jurisdiction, covered taxes, GloBE income. Oracle's EPM TRCS handles the calculation; NetSuite needs to provide the underlying source data with sufficient granularity.
- If the customer is in scope, flag this in the business case as a finance-modernization driver — Pillar Two readiness is a board-level concern, not an IT detail.

### 1.7 Government and state enterprise context

- For ministries, state enterprises (รัฐวิสาหกิจ), and local government bodies (อบจ./เทศบาล), NetSuite is rarely the system of record for the statutory side — that role belongs to New GFMIS Thai. NetSuite tends to play a supporting role for operational accounting, project costing, or subsidiary entities.
- e-GP, TOR templates, and procurement law (พรบ. 2560) apply. The proposal must address license model, data residency (OCI Singapore vs other regions), source code escrow expectations, and exit clauses.

---

## SECTION 2 — Thai OneWorld topology

The single most common scoping mistake on Thai NetSuite engagements is treating the topology as an afterthought. Decide it early, document it in the business case, and lock it before SuiteSuccess kickoff.

### 2.1 Subsidiary structure decision tree

Ask three questions in order:

1. **Are there multiple legal entities in Thailand?** If yes — one subsidiary per legal entity. NetSuite enforces this for Thai statutory reporting.
2. **Does any entity hold BOI privileges?** If yes — decide BOI separation strategy (see 1.5). The choice affects subsidiary count.
3. **Will the group consolidate at a regional or global parent?** If yes — define the parent subsidiary topology so that elimination journals and FX revaluation post correctly.

### 2.2 Master data localization

For each Thai subsidiary configure:

- Base currency THB.
- Address format Thai-postal (Thai language enabled at company level if customer wants Thai-language documents).
- Tax registration number (เลขประจำตัวผู้เสียภาษี).
- Branch code per Thai VAT filing requirements.
- Default tax codes for input VAT, output VAT, WHT rates by type.
- Chart of accounts aligned with TFRS account structure — many Thai customers have inherited a numeric-coded COA from their previous accounting system, and forcing them onto NetSuite's default is a change-management hit they will resist.

### 2.3 Multi-language considerations

If Thai-language outputs are required (invoices, purchase orders, statutory reports):

- Enable Multi-Language at the company level.
- Decide which forms and PDF layouts need Thai translation — usually invoices, credit memos, purchase orders, and statutory financial reports.
- Font handling matters. Sarabun or TH Sarabun New are the de facto standards for Thai government and corporate documents. Custom PDF templates must embed the font; do not rely on default Helvetica fallback.

---

## SECTION 3 — iCE Consulting advisory voice

This section governs how deliverables are written, not what they contain.

### 3.1 The Five Why narrative

Every customer-facing deliverable — business case, board paper, executive briefing, proposal — should explicitly answer five questions in this order:

1. **Why Change?** What is wrong with the status quo? Quantify the pain. The CFO must believe doing nothing is more expensive than doing this project.
2. **Why Now?** What changed in the last 12 to 24 months that makes the case urgent? Regulatory (Pillar Two, e-Tax), commercial (M&A activity, IPO timing), or operational (system end-of-life, finance team turnover).
3. **Why Invest in NetSuite specifically?** What does NetSuite do that the alternatives (SAP S/4HANA, Microsoft Dynamics 365, local ERPs, status quo) do not? Be honest — sometimes the answer is "less, but faster, at a lower TCO."
4. **Why Us?** What does the implementation partner bring that the customer cannot do themselves and that other partners cannot do as well? Reference architecture, Thai localization depth, public sector experience, an existing relationship with a champion.
5. **Why Stay?** After go-live, why will the customer continue paying maintenance and not switch in five years? Roadmap alignment, ecosystem, AMS quality, talent availability.

Never skip a question. If you cannot answer "Why Us?" without sounding generic, the answer is not yet ready.

### 3.2 Multiple options with trade-offs

For any non-trivial recommendation, present at least three options. The customer's decision-makers should never feel cornered into a single path.

Template:

```
Option A — <name>
  Approach:    <one paragraph>
  Effort:      <ballpark person-months / weeks>
  Cost:        <ballpark THB or USD, or stated range>
  Risk:        <what could go wrong>
  When to choose: <if the customer values X above Y, this is the option>

Option B — <name>
  ...

Option C — Status quo / do nothing
  Always include this. It clarifies what the customer is paying to avoid.
```

### 3.3 ROI framing

Three numbers, every time:

- **Hard savings** — headcount avoided, license costs eliminated, audit hours reduced. Defensible to the CFO.
- **Soft benefits** — cycle time reduction, error rate reduction, employee experience. Defensible to the COO, harder to put on the P&L.
- **Strategic value** — Pillar Two readiness, M&A integration capability, future-state architecture alignment. Defensible to the board.

State each separately. Do not blend them into a single benefit number — sophisticated buyers will discount the whole thing if you do.

### 3.4 Risk transparency

List the top three risks in plain language. For each, state the mitigation. Customers respect partners who name risks early — and become suspicious of partners who do not.

```
Risk 1 — <plain language>
  Likelihood:  Low / Medium / High
  Impact:      Low / Medium / High
  Mitigation:  <what we will do to reduce likelihood or impact>
  Owner:       <iCE / Customer / Joint>
```

### 3.5 Tone

The tone is consultative-advisory, not sales-pitch. Three discipline rules:

1. **No name-dropping.** Do not write "based on Big Four best practices" or "applying MEDDPICC qualification" in deliverables. The customer is paying for your judgement, not for citations.
2. **No filler.** Cut "it is important to note," "in today's fast-paced world," "we live in an era where." Get to the point.
3. **First person where it fits.** "We recommend Option B" lands harder than "It is recommended that Option B be selected." Use "เราเสนอ..." in Thai.

### 3.6 Bilingual handling

Default to the customer's working language. If unknown, ask. For mixed audiences:

- **Full bilingual** — Thai and English in parallel sections or columns. Heavy to maintain. Use only for top-level deliverables (executive summary, board paper).
- **Thai primary with English glossary** — body in Thai, key terms cross-referenced to English on first use. Best for ministerial or rajakarn deliverables.
- **English primary with Thai key-term annotation** — body in English, Thai term in parentheses for statutory items (e.g., เลขประจำตัวผู้เสียภาษี). Best for multinational customers with Thai subsidiary.

Never auto-translate without review. NetSuite-specific terminology in Thai is not yet standardized — pick a glossary at project start and stick to it.

---

## SECTION 4 — Deliverable templates

### 4.1 Business case skeleton

```
1. Executive Summary               (1 page)
2. Why Change / Now / Invest / Us / Stay   (per 3.1)
3. Scope and Out-of-Scope          (use 2.1 decision tree)
4. Solution Options                (3+ options per 3.2)
5. Recommended Option              (with rationale)
6. Financial Case                  (3-number ROI per 3.3)
7. Implementation Approach         (SuiteSuccess vs custom, phasing)
8. Risks and Mitigations           (top 3-5 per 3.4)
9. Governance and Decision Asks    (what we need from the steering committee)
10. Appendices                     (technical detail, Thai statutory mapping)
```

### 4.2 RFP/TOR response skeleton

```
1. Executive Summary
2. Understanding of Requirements   (mirror the TOR back, show comprehension)
3. Solution Architecture           (NetSuite core + localization SuiteApps + integrations)
4. Implementation Methodology      (SuiteSuccess phases, milestones, deliverables)
5. Team and Roles                  (named team if possible)
6. Thai Localization Coverage      (Section 1 + Section 2 of this skill)
7. Risk Management
8. Pricing                         (license + implementation + post-go-live AMS)
9. Compliance Annexes              (PDPA, ISO 27001, data residency, source code escrow)
10. Commercial Terms               (payment schedule, change request process, SLA)
```

### 4.3 Pre-sales discovery checklist

When kicking off discovery with a Thai prospect, work through these in the first one or two sessions:

- Entity structure — how many Thai legal entities, how many regional, who consolidates where.
- BOI promotions — current and planned.
- Tax registration — VAT, WHT, e-Tax status.
- Current systems — accounting, payroll, HR, CRM, e-commerce.
- Pain points — top three, in the customer's own words. Write them down verbatim.
- Trigger event — what made the customer pick up the phone now.
- Decision criteria — what the customer says they will use to choose.
- Decision process — who decides, who influences, who can veto.
- Budget — confirmed, indicative, or aspirational.
- Timeline — go-live ambition, regulatory or commercial drivers behind it.

The output of this is not a document — it is a confidence call on whether to invest pre-sales effort. If three or more of the above are blank after two sessions, the deal is not yet qualified.

---

## SECTION 5 — Handoff protocol to Oracle skills

When this skill has framed the engagement and the work shifts to engineering, invoke the Oracle skills explicitly. Pattern:

```
The advisory framing above is fixed. For the technical sections, invoke:

  $netsuite-sdf-project-documentation to produce the deployment runbook for
    the SDF project at <path>. Apply the bilingual handling rule from Section 3.6.

  $netsuite-sdf-roles-and-permissions to draft customrole XML for the
    Thai AP team. Reference the BOI separation strategy chosen in Section 1.5.

  $netsuite-owasp-secure-coding to audit any RESTlets or external integration
    endpoints exposed for e-Tax submission or middleware.
```

Always close the handoff with a verification ask: "After the Oracle skill produces its output, confirm it does not contradict the Thai context in Sections 1-4 of this skill."

---

## SECTION 6 — Known limitations

This skill encodes context that is current as of May 2026. The following items drift faster than the rest and must be checked before any customer-facing commitment:

- VAT rate (currently 7 percent, has been raised in draft legislation more than once).
- WHT rates and PND filing forms.
- e-Tax Invoice technical specification revisions.
- BOI promotion categories and conditions.
- Pillar Two implementation timeline and Thai DMTT (Domestic Minimum Top-up Tax) rate.
- NetSuite release-specific features — SuiteAgents, AI Connector, NSAW are evolving quarterly.

Treat numbers and references in this skill as design inputs. The customer's tax advisor and the latest NetSuite release notes are the authoritative sources.

---

## SECTION 7 — Skill maintenance

- Version increments on substantive content change (V01R01 → V02R01).
- Sub-release increments on minor edits (V01R01 → V01R02).
- Quarterly review against Thai Revenue Department announcements and NetSuite release notes.
- When Oracle's underlying skills update, re-check Section 5 handoff patterns for compatibility.

End of skill.
