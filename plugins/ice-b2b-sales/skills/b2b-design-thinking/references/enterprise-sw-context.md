# Enterprise Software Context — Five Domain Pillars

The skill must be fluent across these five pillars. Use the vendor-specific installed skills for deep configuration detail; this file ensures the DT/ST layer speaks the right language.

## Pillar 1 — Oracle Stack

**Products:** Oracle Fusion Cloud (ERP, EPM, SCM, HCM, CX), E-Business Suite (EBS R12), NetSuite, Oracle Cloud Infrastructure (OCI), APEX, Visual Builder Cloud Service (VBCS), Analytics Cloud.

**Typical deal shape:**
- Fusion ERP: mid-market to large, 6–18 month cycle, often multi-pillar
- EBS: installed base upgrade or re-platform to Fusion / S/4 / NetSuite
- NetSuite: upper SME and mid-market, faster cycles (3–9 months)
- OCI: infrastructure play, often bundled with app migration

**Implementation methodology:** Oracle Unified Method (OUM), True Cloud Method (Fusion), Oracle AIM (legacy EBS).

**Key workshop hooks:**
- Pain: EBS aging, customizations unsupported, cloud mandate
- Why Now: license renewal, regulatory change (IFRS, PDPA), M&A integration
- Why Us (if Oracle partner): certified competencies, local support, industry IP

**Extension platforms:** APEX for low-code on DB, VBCS for Fusion extensions, Oracle Integration Cloud (OIC).

**Installed skills to delegate to:**
- `oracle-cloud-applications-consulting` — Fusion depth
- `oracle-ebs-consulting` — EBS depth + upgrade paths
- `oracle-netsuite-consulting` — NetSuite + SuiteSuccess

## Pillar 2 — SAP Stack

**Products:** S/4HANA (on-prem / Private Cloud / Public Cloud), RISE with SAP, GROW with SAP, SAP Business Technology Platform (BTP), SAP Business One (B1), SuccessFactors, Ariba, Concur, Joule (GenAI copilot).

**Typical deal shape:**
- S/4HANA RISE: large enterprise, 12–24 month cycle, mandatory ECC sunset driver (2027)
- BTP: platform extension play, often post-core implementation
- Business One: SME, faster cycle, local partner heavy

**Implementation methodology:** SAP Activate (Agile-based), five phases: Discover / Prepare / Explore / Realize / Deploy / Run.

**Key workshop hooks:**
- Pain: ECC sunset 2027, customizations in ECC blocking upgrade
- Why Now: cloud mandate, regulatory (Thai e-Tax, e-GP integration), AI / Joule opportunity
- Why Us: SAP certified partner tier, local Thai SME expertise, vertical accelerators

**Extension platforms:** BTP (iPaaS, low-code via AppGyver, Data & AI services), ABAP on BTP for custom logic.

**Style note:** SAP pre-sales typically uses the **AppHaus method** — design-thinking-informed envisioning. Adopt its structure for SAP workshops.

## Pillar 3 — Other Commercial

**Products:**
- Microsoft Dynamics 365 (F&O, Business Central, CE/CRM) + Power Platform (Power Apps, Power Automate, Power BI, Copilot Studio, Dataverse)
- Salesforce (Sales, Service, Marketing, Commerce, Data Cloud, Einstein, Agentforce, Platform)
- Infor (CloudSuite Industry, Financials, M3)
- Odoo (open-source ERP, strong in Thai SME)
- Workday (HCM, Financials — large enterprise)

**Typical deal shape:**
- MSFT D365 + Power Platform: often bundled with M365 / Azure; strong low-code extension story
- Salesforce: CRM-led, expanding into platform and data cloud; partner ecosystem critical
- Infor: vertical-industry focus (manufacturing, distribution, fashion)
- Odoo: cost-sensitive, local partner delivery, customization heavy
- Workday: HR-first, then financials for large enterprise

**Extension platforms:** Power Platform (MSFT), Salesforce Platform / Lightning / Apex, Odoo Studio, Workday Extend.

**Key distinguishing themes:**
- **MSFT story:** productivity + AI (Copilot everywhere) + low-code democratization
- **Salesforce story:** single source of truth + Einstein/Agentforce + partner apps
- **Infor story:** industry CloudSuites (pre-built vertical solutions)
- **Odoo story:** all-in-one at lower TCO, open-source flexibility
- **Workday story:** unified HR + finance, strong for large complex organizations

## Pillar 4 — Thai Public Sector

**Products:**
- GFMIS (Government Fiscal Management Information System) — national budget, procurement, accounting
- e-GP (Electronic Government Procurement) — mandatory procurement portal
- SMART PAO — Provincial Administrative Organization platform
- Local government ERP (Municipal and Sub-district administrations)
- e-LAAS — local administrative accounting

**Regulatory/context frame:**
- Public Procurement Act B.E. 2560 (2017) — procurement rules
- Thai Fiscal Discipline Act
- Cloud Security Standard 2567 — mandatory for government CII
- PDPA compliance
- Digital Government Development Plan / Thailand 4.0 / Digital Government Development Agency (DGA)

**Typical deal shape:**
- Government procurement via e-GP (e-bidding, e-market, specific methods)
- Fiscal year (Oct–Sep) drives budget cycles
- TOR (Terms of Reference) and Middle Price analysis mandatory
- Approval hierarchy: user unit → procurement committee → treasurer → head of agency
- Implementation often multi-year, with annual appropriations

**Key workshop hooks:**
- Pain: legacy system aging, audit findings from OAG (Office of the Auditor General), policy mandate (Thailand 4.0)
- Why Now: budget cycle alignment, regulatory mandate deadline, political administration priorities
- Why Us: local track record, government certifications, bilingual Thai/English delivery, PDPA and Cloud Standard 2567 compliance

**Installed skills to delegate to:**
- `advisor-govt-gfmis` — GFMIS depth
- `govt-egp-gfmis` — procurement legal and technical detail
- `smart-pao-platform` — PAO platform specifics
- `legal-it-thailand-cloud` — PDPA + Cybersecurity Act + Cloud Standard 2567

## Pillar 5 — AI & Custom Extensions

This pillar sits **on top** of the other four. Every enterprise software platform now has AI and extension capabilities — the ideation dimension is growing faster than any other.

### 5a. AI Use-Case Ideation on Top of ERP/CRM
Patterns to ideate:
- **GenAI copilots** — summarization, drafting, Q&A over enterprise data (Oracle AI Agents, SAP Joule, MSFT Copilot, Salesforce Einstein/Agentforce)
- **Agentic AI workflows** — multi-step task execution (e.g., invoice exception handling, expense policy validation, supplier onboarding)
- **Predictive analytics** — demand forecasting, payment behavior, churn, stock-out, collection
- **Document intelligence** — OCR + extraction (invoices, contracts, purchase orders, tax forms)
- **Conversational interfaces** — employee HR self-service, citizen service bots, procurement intake
- **Anomaly detection** — fraud, expense abuse, journal entry anomalies, cybersecurity

### 5b. Custom App Extensions on PaaS / Low-Code
Match the base platform:
- **Oracle Fusion** → Oracle Integration Cloud (OIC) + VBCS for extensions; APEX for DB-adjacent apps
- **SAP S/4HANA** → BTP (Build Process Automation, Build Apps, ABAP on BTP)
- **MSFT D365** → Power Platform (Power Apps + Power Automate + Dataverse + Copilot Studio)
- **Salesforce** → Salesforce Platform + Lightning + Apex + Flow
- **NetSuite** → SuiteScript + SuiteFlow + SuiteCloud Platform
- **Workday** → Workday Extend

### 5c. Integration & Data Product Ideation
- iPaaS patterns (Oracle OIC, SAP Integration Suite, MSFT Azure Integration, MuleSoft)
- Data products for analytics and AI: Snowflake, Databricks, Oracle Autonomous DB, SAP Datasphere
- Real-time event streaming (Kafka, Confluent, Azure Event Hub)
- Master Data Management (MDM) plays

### 5d. Industry Vertical AI Plays for Thailand
- **Public sector:** tax fraud detection, procurement anomaly, citizen service chatbot, e-GP bid analytics
- **Banking & Financial Services:** NPL/NPA prediction, IFRS9 ECL, KYC/AML, credit decisioning, robo-advisor
- **Manufacturing:** predictive maintenance, quality vision, OEE analytics, demand sensing
- **Retail & CPG:** dynamic pricing, assortment, customer lifetime value, recommendation
- **Healthcare:** claims automation, clinical documentation copilot, patient flow

## Cross-Pillar Patterns

Regardless of vendor, enterprise software deals share these patterns:

- **Value case structure:** revenue uplift + cost takeout + risk reduction + strategic option value
- **Stakeholder map:** Economic Buyer (CFO/CEO), Technical Buyer (CIO/CTO), User Champion (LOB leader), Coach (internal sponsor), Influencer (security, procurement, legal)
- **Objection set:** cost, timing, risk, fit, vendor lock-in, people-change capacity
- **Proof points needed:** ROI case, reference customers, PoC, security & compliance, local support

Use these patterns as the backbone for any workshop, with vendor-specific detail layered in from the installed skills.
