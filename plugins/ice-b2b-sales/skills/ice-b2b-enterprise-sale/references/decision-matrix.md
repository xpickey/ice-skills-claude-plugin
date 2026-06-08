# Decision Matrix
**Version:** V02R02 | **Date:** 2026.05.22 | **Companion to:** `../SKILL.md`

# Section 0 — How to Use

Open this file only when the four routing questions in SKILL.md Section 3 do not return
a confident answer in under a minute. Do not pre-read it. Each section below is a single
lookup that ends with a chain assignment.

The matrix is **Deliverable-First**. Asking "what product is this?" before "what artifact
am I producing?" puts you on the wrong path roughly half the time — the same product
needs very different chains for a TOR Response vs. a Board Paper vs. an Existing Customer
CR.

Reading order under pressure:

1. Decide deliverable type (Section 2) — this is 80% of the routing
2. Layer in product (Section 4) — narrows the product-specific skill
3. Layer in domain (Section 5) — adds GFMIS / e-GP / PDPA / PAO if applicable
4. Apply stop rules (Section 6) — confirm you are not chaining beyond five skills

Skip Section 3 (Role × Stage) unless the request explicitly mentions a stage. It is a
secondary lens, not the primary one.

# Section 1 — Master Decision Tree

```
                    ┌─────────────────────────┐
                    │  What is the request?   │
                    └────────────┬────────────┘
                                 │
       ┌─────────────────────────┼─────────────────────────┐
       │                         │                         │
   ▼ Fast Path                ▼ Pre-sales              ▼ Strategic
   (single artifact,          (RFP, Proposal,         (Account plan,
    internal, reversible)      Demo, Business case)    Win plan, QBR)
       │                         │                         │
       ▼                         ▼                         ▼
   Single skill              Hot Path (4.1)             Standard (4.2)
   (questioning OR           strategic→solution-        strategic→why→
    relationship)            selling→product→           relationship→
                             domain→pptx                product
       │                         │                         │
       └───────┬─────────────────┴─────────────┬───────────┘
               │                               │
               ▼                               ▼
       Typography QA gate              Anti-AI / Anti-Name-Drop
       (if .docx/.pptx/.pdf)           gate (always)
                                              │
                                              ▼
                                       Pre-Save + V##R##
```

Two principles govern this tree:

- **Down the funnel, never sideways.** Once a chain is chosen, do not swap skills
  mid-draft; finish, then revise.
- **Pre-sales heavy is the default.** When in doubt, treat the request as Pre-sales Hot
  Path because that is ~70 % of real-world workload — the Strategic and Fast paths are
  the exceptions, not the rule.

# Section 2 — Deliverable-First Matrix (PRIMARY)

Look up the deliverable in column 1, take the chain from column 3, and confirm the
typography behaviour in column 4. Industry overlay is in column 5 — leave blank when
not applicable.

## 2.1 Pre-sales Pursuit Deliverables

| # | Deliverable | Chain (in order) | Output Format | Industry Lens |
|---|---|---|---|---|
| D-01 | RFP/RFI Response | strategic-thinking → solution-selling → product → domain → presentation-creator | .pptx OR .docx | Industry compliance language |
| D-02 | TOR Response (รัฐวิสาหกิจ) | strategic-thinking → solution-selling → govt-egp-gfmis → product → presentation-creator | .docx + .pptx + compliance matrix .xlsx | TOR clause × FC/PC/CC mapping |
| D-03 | Technical Proposal | strategic-thinking → solution-selling → product → presentation-creator | .docx (sections 1–8) | Industry-specific terms in section 1 |
| D-04 | Commercial Proposal | solution-selling → product → presentation-creator | .docx (pricing + payment + ToS) | Industry-typical payment terms |
| D-05 | Business Case / ROI | strategic-thinking → solution-selling → product | .docx + .xlsx 5-year model | Industry KPIs in benefit lines |
| D-06 | Demo Design / Solution Architecture | strategic-thinking → product → presentation-creator | .pptx | Industry-specific data flow |
| D-07 | Board Paper / Executive Briefing | strategic-thinking → why-thinking → presentation-creator | .pptx OR .docx | Industry-typical risk framing |
| D-08 | RFI Response (informational) | solution-selling → product → presentation-creator | .pptx | Headline-metric framing |
| D-21 | Negotiation Brief / Price Defense Sheet | solution-selling → why-thinking → (relationship-management) | .docx 1–2 pages OR inline | Industry-typical price/scope sensitivities |
| D-22 | BAFO (Best & Final Offer) Strategy Sheet | solution-selling → strategic-thinking → why-thinking | .docx 1 page | Industry buyer-power lens |

## 2.2 Strategic & Account Deliverables

| # | Deliverable | Chain (in order) | Output Format | Industry Lens |
|---|---|---|---|---|
| D-09 | Account Plan / Win Plan | strategic-thinking → why-thinking → relationship-management → product | .docx OR .pptx | Industry buying-cycle calibration |
| D-10 | Competitive Battle Card | strategic-thinking → product → why-thinking | .pptx 1-pager | Industry-specific competitor map |
| D-11 | Discovery Prep (multi-question set) | questioning → product | .docx 1-pager | Industry-specific pain themes |
| D-12 | Stakeholder / Power Map | relationship-management → strategic-thinking | .pptx OR .xlsx | Industry-typical buying committee |
| D-13 | Win/Loss Debrief | strategic-thinking → why-thinking → relationship-management | .docx | Industry pattern flagging |

## 2.3 Customer-success & Existing-customer Deliverables

| # | Deliverable | Chain (in order) | Output Format | Industry Lens |
|---|---|---|---|---|
| D-14 | QBR / EBR | relationship-management → strategic-thinking → presentation-creator | .pptx | Industry KPI alignment |
| D-15 | Renewal / Expansion Pitch | relationship-management → why-thinking → solution-selling | .pptx | Industry growth lever |
| D-16 | Customer Change Request (CR) | solution-selling → product | .docx (form-style) | Industry workflow context |
| D-17 | Customer Health Score | relationship-management → questioning | .xlsx OR .pptx | Industry churn indicators |

## 2.4 Communication & Light-weight Deliverables

| # | Deliverable | Chain (in order) | Output Format | Industry Lens |
|---|---|---|---|---|
| D-18 | Sales Follow-up Email | questioning OR relationship-management (single) | Inline OR .docx | Tone-only |
| D-19 | Meeting / Call Notes Summary | questioning (single) | Inline OR .docx | Tone-only |
| D-20 | Internal Sitrep | strategic-thinking (single) | Inline OR .docx | None |

## 2.5 Customer Profile (Pre-Step Zero)

| # | Deliverable | Chain (in order) | Output Format | Industry Lens |
|---|---|---|---|---|
| D-00 | Customer Profile | strategic-thinking → questioning + (optional) industry-specific reading | .docx 1–2 pages | **Heavy** — profile is the industry lens for every downstream deliverable |

D-00 is the prerequisite for D-01 through D-17 whenever the customer is new to you in
this engagement. See `orchestration-playbook.md` WE-00 for the method.

# Section 3 — Role × Stage Matrix (Secondary)

Use this lens only if the user request explicitly mentions a role or stage that does
not map cleanly to a deliverable type. Otherwise, Section 2 is more accurate.

## 3.1 Role Lens

| Role | Primary Skills | Secondary | When to Reach |
|---|---|---|---|
| Sales / Account Director | strategic-thinking, why-thinking, relationship-management | questioning, solution-selling | Account planning, deal pursuit, exec engagement |
| Pre-sales / Sales Engineer | solution-selling, product skill, presentation-creator | questioning, strategic-thinking | Discovery, demo design, proposal, RFP/TOR |
| Customer Success / AMS Lead | relationship-management, product skill | questioning, why-thinking | QBR, renewal, escalation, CR |
| Practice Lead / Pursuit Owner | strategic-thinking, why-thinking, solution-selling | All Tier-A | Bid/no-bid, win plan, business case, board paper |
| Marketing / Channel | strategic-thinking, why-thinking | design-thinking | Battle card, campaign, partner pitch |

## 3.2 Stage Lens (Pursuit Stage → Skill emphasis)

| Stage | Heavy Skills | Light Skills | Typical Deliverable |
|---|---|---|---|
| Prospect / Identify | strategic-thinking, why-thinking | questioning | Industry brief, target list |
| Qualify | solution-selling, questioning | strategic-thinking | Qualification scorecard, pain sheet |
| Engage / Discover | questioning, design-thinking | solution-selling | Discovery script, workshop deck |
| Solution / Propose | solution-selling, product, presentation-creator | strategic-thinking | Technical + Commercial Proposal |
| Negotiate / Close | solution-selling, why-thinking | relationship-management | Negotiation playbook, final pricing |
| Implement Handover | (out of scope) | (out of scope) | — handover briefing only |
| Renew / Expand | relationship-management, why-thinking | solution-selling | QBR, expansion pitch, CR |

# Section 4 — Product Routing

Once the deliverable is fixed, the product determines which product-specific Tier-A or
Tier-B skill is added to the chain.

| Product Cue in Request | Skill to Add | Where to Add in Chain |
|---|---|---|
| "Fusion", "Oracle Cloud ERP/EPM/SCM/HCM", "OCI", "Pillar Two", "TRCS", "FCCS", "ARCS", "EPBCS", "Redwood" | `oracle-cloud-applications-consulting` | After strategic-thinking, before presentation-creator |
| "EBS", "R12.x", "ADOP", "Cloud Manager", "EBS-to-OCI", "Hybrid Oracle ERP" | `oracle-ebs-consulting` | Same position as above |
| "NetSuite", "SuiteSuccess", "SuiteAgents", "NSAW", "OneWorld", "MyInvois" | `oracle-netsuite-consulting` | Same position |
| "Lending", "Loan Origination", "NPL/NPA", "IFRS9/TFRS9", "Digital Banking", "Payment", "Credit Risk" | `fin-tech-consulting` | After solution-selling — drives business-case lens |
| Cross-product / vendor-agnostic / pure consulting | (no product skill) | Use only Tier-A skills |

**Conflict rule.** If the request names two products (e.g. "compare NetSuite vs Fusion"),
add BOTH product skills, with the one being recommended placed first. Cap the chain at
five skills total — drop the lowest-priority Tier-B if needed.

# Section 5 — Domain Overlay Triggers

These overlays are mandatory when triggered. They are not optional flavour; they change
the entire artifact structure.

| Trigger Words | Domain Skill | Chain Position |
|---|---|---|
| "GFMIS", "New GFMIS Thai", "FM", "e-LAAS", "บัญชีเกณฑ์คงค้าง", "Vendor Master 1000–8000", "BAHTNET/SMART", "Bank Reconciliation ภาครัฐ", "Internal Audit GFMIS" | `advisor-govt-gfmis` | After Product, before presentation-creator |
| "e-GP", "พรบ.จัดซื้อจัดจ้าง 2560", "e-bidding", "e-market", "TOR Response", "Compliance Matrix", "ราคากลาง", "หลักประกัน", "ค่าปรับ", "การอุทธรณ์" | `govt-egp-gfmis` | After Product, before presentation-creator |
| "อบจ.", "เทศบาล", "อปท.", "SMART PAO", "e-Saraban", "เบี้ยผู้สูงอายุ", "กองทุนสุขภาพตำบล" | `smart-pao-platform` | After Product, before presentation-creator |
| "PDPA", "ISO 27001", "ISO 27017/27018/27701", "Cloud Security 2567", "DPA", "ROPA", "Cross-border transfer", "Sensitive data" | `legal-it-thailand-cloud` | Layered with Product — affects security & compliance sections |

**Compound triggers.** If the deal is รัฐวิสาหกิจ AND uses Oracle Cloud, the chain is:
`strategic-thinking → solution-selling → oracle-cloud-applications-consulting →
govt-egp-gfmis → presentation-creator`. The domain skill follows the product skill so
that compliance language is layered onto a real solution, not floated abstractly.

When PDPA appears alongside any other domain, it is layered, not chained — it
contributes specific clauses, not a separate document structure.

# Section 6 — Stop Rules

Use these to prevent over-chaining or runaway scope. If a stop rule fires, fix the
chain before drafting.

## 6.1 Hard Caps

| Cap | Limit | If exceeded |
|---|---|---|
| Maximum skills in one chain | 5 | Drop the lowest-priority Tier-B; split the deliverable if it still doesn't fit |
| Maximum Tier-A skills in one chain | 4 | Re-read the request — likely over-scoped |
| Maximum deliverables produced in one session | 2 | Stop after the second; sequence the rest |
| Maximum reference-file deep-reads in one session | 1 | The references are lookup, not study material |

## 6.2 Pivot Triggers

| Signal | Reaction |
|---|---|
| User mentions a Tier-C skill (relationship-management) but no Existing-customer context | Treat as Tier-B; do not pivot the whole chain |
| User mentions a methodology brand name | Translate silently into the underlying concept; do not echo the name in output |
| User mentions an industry not in the Industry × Product table | Treat as adjacent industry (closest fit) and flag `[ASSUMED: industry adjacency]` |
| User uploads a Customer Profile artifact | Skip WE-00; jump to the chain for the actual deliverable |
| User asks for "just the answer, no chain explanation" | Run chain silently; deliver only the artifact |

## 6.3 Bid / No-Bid Stop

For RFP and TOR responses, before chaining any pursuit work, run a quick bid/no-bid
sanity check (see `orchestration-playbook.md` QRC-09). If five or more of the seven
disqualifying conditions fire, recommend No-Bid and stop. Do not produce a Technical
Proposal for a deal that the qualification flags would have killed.

## 6.4 Anti-Hallucination Stop

If the request requires specific customer financial figures, contract values, or
stakeholder names that are not in any uploaded artifact or in the user's chat, stop
and ask. Do not generate `[CUSTOMER X grew 23 % last year]` from inference.

# Section 7 — Worked Routing Examples

Three short examples to anchor the table. Each takes the request as-is and shows the
chain it produces.

## Example A

> "ทำ technical proposal ตอบ TOR ของรัฐวิสาหกิจ ใช้ Oracle Cloud ERP — ผู้ตัดสินคือ CFO"

- Deliverable: D-02 TOR Response (รัฐวิสาหกิจ)
- Product: Oracle Fusion Cloud → `oracle-cloud-applications-consulting`
- Domain: TOR / e-GP → `govt-egp-gfmis`
- Audience: CFO → emphasis on 5-year cost model and risk allocation

**Chain:** `strategic-thinking → solution-selling → oracle-cloud-applications-consulting
→ govt-egp-gfmis → presentation-creator`. Output: .docx (8 sections) + .pptx executive
summary + .xlsx compliance matrix. Typography QA: Government-Formal pair.

## Example B

> "ลูกค้า NetSuite รายเก่า ขอ CR เพิ่ม column ในหน้า PO และ Vendor — กระทบ schedule ไหม?"

- Deliverable: D-16 Customer Change Request
- Product: NetSuite → `oracle-netsuite-consulting`
- Domain: none
- Industry: Existing customer — F&B/Retail

**Chain:** `solution-selling → oracle-netsuite-consulting`. Output: .docx CR form
(severity, impact, manday breakdown, approval block). Typography QA: Corporate-Clean.

## Example C

> "ทำ pitch deck 1 page สำหรับ CEO บอกว่าทำไมต้องเลือกเรา"

- Deliverable: D-10 Competitive Battle Card (variant: single-page exec pitch)
- Product: not specified — use cross-product framing unless user adds detail
- Domain: none

**Chain:** `strategic-thinking → why-thinking → presentation-creator`. Output: 1-slide
.pptx. Typography QA: Corporate-Modern. Tone: punchy, headline-led.

End of Decision Matrix.
