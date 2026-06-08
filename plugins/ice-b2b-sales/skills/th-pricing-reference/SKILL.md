---
name: th-pricing-reference
description: Thailand-market pricing reference for enterprise software (Oracle Cloud / EBS / NetSuite, SAP RISE/GROW/B1, MS Dynamics 365 F&O/BC, Workday, Salesforce). Provides list-price anchors in USD, typical Thai-market discount bands, contracting nuances, BYOL / Customer 2 Cloud / Universal Credits levers, and budget benchmarks for sizing deals. Use when building proposals, ROI/TCO models, discount-justification memos, deal-desk approvals, or competitor comparisons in the Thai enterprise market. Bilingual EN + TH business wording.
---

# TH Pricing Reference — Enterprise Software (Thailand Market)

## Operating principles

1. **List prices are anchors, not truth.** Thai-market discount bands are deeper than US/EMEA in mid-market and SOE deals; shallower for tier-1 enterprise/regulated.
2. **Always quote in USD with Baht reference.** Vendors price in USD; Thai customers budget in Baht. Provide both.
3. **TCO over 3 years** is the right denominator. License is 30-50% of TCO; the rest is implementation, integration, infra, change management, support.
4. **BYOL economics is the #1 lever for Oracle DB customers** moving to OCI — frame this early.
5. **Multi-year commit + scope expansion** unlock the deepest discounts; one-shot price haggling is the worst negotiation play.

---

## Oracle Cloud SaaS (Fusion ERP / EPM / SCM / HCM / CX)

### List-price anchors (USD/user/month — current generation)

| Module | Metric | List | TH typical net |
|---|---|---|---|
| **Financials Cloud (ERP)** | Hosted Named User | $175 | $115–140 (20–35% off) |
| **Procurement Cloud** | Employee | $40 | $26–32 |
| **Project Financials** | Hosted Named User | $200 | $130–160 |
| **EPM Standard (Planning)** | Hosted Named User | $250 | $160–200 |
| **EPM Enterprise (full suite)** | Hosted Named User | $500 | $325–400 |
| **FCC (Consolidation)** | Hosted Named User | $200 | $130–160 |
| **ARCS (Account Recon)** | Hosted Named User | $80 | $52–64 |
| **SCM Cloud** | Hosted Named User | $300 | $195–240 |
| **HCM Foundation** | Employee | $15 | $10–12 |
| **HCM Talent** | Employee | $7 | $5–6 |
| **OTBI / FAW** | Per-user/mo | $80 | $52–64 (often bundled) |

### Discount levers (additive — stack carefully)
- **3-year commit:** +5–10%
- **5-year commit:** +10–15%
- **Multi-pillar bundle (ERP + EPM + HCM):** +5–8%
- **Reference customer agreement** (logo + case study + peer reference): +3–5%
- **Greenfield / new-logo strategic:** +5–10%
- **Q4 strategic / fiscal-year close (Oracle FY = Jun 1):** +5–10% — May/June is optimal close window
- **Counter-displace SAP/Workday with documented compete:** +5–10%

### Contracting nuances (Thailand)
- **Master Cloud Services Agreement (MCSA)** — Oracle's standard cloud contract, signed in Singapore or USA jurisdiction by default; large Thai deals can negotiate Thai law/jurisdiction
- **Thai language addendum** — possible for SOE / govt customers
- **Order forms in Baht** — possible but rare; FX risk usually with customer
- **PDPA addendum** — standard for Thai customers; review data-residency clause
- **Test environment** — 1 included; additional ~$1,000–3,000/mo per env
- **Sandbox** — typically included; verify edition (Standard vs Premium)

---

## Oracle EBS (perpetual, install base)

| Item | Metric | List | Discount band |
|---|---|---|---|
| EBS Application User | Per user perpetual | $4,595 | 30–60% (volume-tiered) |
| Annual Support (SULS) | 22% of license | varies | flat (rarely discounted) |
| **Customer 2 Cloud (C2C)** credit | License-equivalent value applied to Cloud | up to ~50% | Oracle's primary EBS-to-Fusion lever |

**Key levers:**
- C2C unlocks cloud subscription using existing on-prem license value — major TCO improvement
- Support Rewards: 25% earned on OCI consumption applies against on-prem support invoice
- ULA → audit → cloud is a common 3-step path for big EBS install base

---

## Oracle NetSuite

### Pricing model (per company, not per user — different from Fusion)
| Component | Typical TH cost |
|---|---|
| **NetSuite ERP (base)** — Limited / Standard / Premium / Enterprise / Ultimate | $999 / $1,999 / $2,999 / $3,999 / $5,999 USD/mo (entry) |
| **OneWorld (multi-sub)** | +$1,999 USD/mo (entry) |
| **User license (Full)** | $99–129 USD/user/mo |
| **User license (Employee/Limited)** | $49 USD/user/mo |
| **Industry SuiteApp** (e.g. WMS, Manufacturing) | $499–2,999 USD/mo |
| **NetSuite Premium Support** | 8–10% uplift |

### TH-typical SuiteSuccess deal
- Mid-market wholesale/distribution, ~30 users, OneWorld 3-sub, 100 days deploy
- License: ~$80K–120K USD/yr
- Implementation: ~$150K–250K USD one-time
- TCO Year-1: ~$250K–400K USD
- **Discount band: 15–30% off list, 3-year commit standard**

---

## SAP RISE / S/4HANA Cloud Private Edition

### FUE (Full Use Equivalent) — the SAP unit
- 1 FUE ≈ 1 Professional / 5 Functional / 30 Productivity users
- TH list ~$100–140 USD/FUE/month for S/4HANA Cloud Private (RISE bundle including hosting)
- **Discount band: 25–45% off list** for new logos; deeper for displacement

### RISE bundle includes
- S/4HANA Cloud Private Edition
- BTP credits (~10–15% of FUE value)
- SAP Business Network starter pack (Ariba)
- SAP Cloud ALM
- Hosting on Azure / AWS / GCP / SAP infra (managed)
- One sandbox

### TH-typical RISE deal
- Mid-large mfg/retail, 200-500 FUE
- License: $300K–800K USD/yr
- SI implementation: 1.5x–2.5x license year-1
- **3-year commit standard**, 10–15% additional discount

---

## SAP GROW with SAP (S/4HANA Cloud Public Edition)

- TH list ~$60–90 USD/FUE/month — lower entry than RISE
- **Discount band: 15–25%** (shallower — multi-tenant)
- 3-year commit; quarterly auto-release

---

## SAP Business One

- **Channel-only** — TH partner sets margin
- Professional User: ~$3,213 USD perpetual list (B1 on HANA, less on SQL)
- Limited User: ~$1,666 USD perpetual list
- Maintenance: 18% annually
- **Cloud (partner-hosted):** ~$80–130 USD/user/mo
- **TH partner discount:** 30–50% from SAP, partner adds 20–35% margin → end-customer 0–20% vs list

---

## Microsoft Dynamics 365 F&O

| App | List USD/user/mo | TH typical |
|---|---|---|
| D365 Finance | $210 | $150–180 |
| D365 SCM | $210 | $150–180 |
| D365 Commerce | $210 + commerce-scale-unit | varies |
| D365 Project Operations | $135 | $95–115 |
| Attach license (2nd, 3rd app) | $30 | $20–25 |
| Activity / Team Member | $8 | $5–7 |

- 3-year EA discount: +10–15%
- M365 + Azure attach: +5–10% (consolidated MS spend)

---

## Microsoft Dynamics 365 Business Central

| Edition | List USD/user/mo | TH typical |
|---|---|---|
| Essentials | $70 | $45–60 |
| Premium | $100 | $65–85 |
| Team Member | $8 | $5–7 |

- TH partner-channel deals; CSP-led, partner adds services margin
- Annual commit standard

---

## Workday

- Pricing **opaque** — no public list
- TH typical: $80–150 USD/employee/year for HCM
- Workday Financials adds ~$200/employee/year
- Discount lever: Adaptive Planning bundle, multi-year, large EE count
- **Discount band: 20–35%** typical; deeper for tier-1 strategic logos

---

## Salesforce

| Cloud | List USD/user/mo | TH typical |
|---|---|---|
| Sales Cloud — Professional | $80 | $55–70 |
| Sales Cloud — Enterprise | $165 | $115–140 |
| Sales Cloud — Unlimited | $330 | $230–280 |
| Service Cloud — Enterprise | $165 | $115–140 |
| Marketing Cloud — Engagement | starts $1,250/mo | varies |
| Data Cloud (CDP) | usage-based | varies |

- **Discount band: 15–35%** depending on commitment
- 3-year deal + multi-cloud bundle: +10–15%
- Q4 (Salesforce FY = Feb 1): January is the best close window

---

## Implementation cost ratios (rule of thumb — 3-year TCO modeling)

| Product | Impl : License (Year 1) |
|---|---|
| Oracle Fusion ERP | 1.5–2.5x |
| Oracle EBS upgrade | 2–3x (Brownfield), 4–6x (Greenfield) |
| NetSuite SuiteSuccess | 1.5–2x |
| SAP RISE Greenfield | 2.5–4x |
| SAP RISE Brownfield | 1.5–2.5x |
| GROW with SAP | 1–1.5x |
| SAP B1 | 0.5–1.5x (channel-led) |
| D365 F&O | 2–3x |
| D365 BC | 1–2x |

---

## Thai-market pricing levers — playbook summary

| Lever | When to pull | Typical $ impact |
|---|---|---|
| **Multi-year commit (3y → 5y)** | First, always | 10–20% discount |
| **Multi-pillar bundle** | If multiple modules in scope | 5–10% |
| **BYOL to OCI** (Oracle DB customers) | Hybrid / cloud move | Up to 50% off public-cloud DB list |
| **Oracle Support Rewards** | Existing on-prem Oracle DB | 25% of OCI consumption applied to on-prem support |
| **Customer 2 Cloud (Oracle)** | EBS-to-Fusion | License credit applied to subscription |
| **Reference / case study** | New-logo strategic | 3–5% |
| **Q-end / FY-end timing** | When customer can commit | 5–10% |
| **Greenfield / displacement** | Counter-position SAP/Oracle/MS | 5–10% |
| **Govt / SOE volume** | TH public sector pursuit | RFP-driven; budget-constrained |

---

## Anti-patterns (don't do these in TH market)

1. ❌ **List-price quote without discount frame** — TH expects negotiation; signals weakness
2. ❌ **Year-1 only quote** — customer compares to partner who quoted Year 1 only; you lose Year 2-3 margin
3. ❌ **Discount without trade** — see negotiation-agent's trade ladder
4. ❌ **Bundling at end of cycle** — lock scope first, then price
5. ❌ **Foreign jurisdiction insistence** — large TH deals expect Thai law/jurisdiction option
6. ❌ **Ignoring PDPA / data-residency** — Thai customers will ask
7. ❌ **No bilingual quote** — TH C-level wants TH summary alongside USD detail

---

## Output usage

When invoked by another agent, return:
- Specific module/SKU pricing for the deal in scope
- Recommended discount band based on profile (logo type, commit, scope)
- Trade levers to deploy
- Implementation cost band for TCO model
- Anti-pattern flags if customer ask is unrealistic
- Cross-references to `negotiation-agent` (for trade execution) and `competitor-objection-bank` (for compete-justified discount)
