# Thailand & APAC Localization

Use these guardrails whenever the client is Thai, the audience is bilingual, or the deal touches Thai regulation and procurement. This file overrides global-default assumptions where they conflict with Thai market practice.

## Language Strategy

The skill auto-detects the target language from prompt cues, client name, and audience signals. Defaults:

- **Mixed stakeholders** (typical Thai enterprise / government) → parallel bilingual Thai + English
- **Pure Thai audience** (local SME, government working level) → Thai first, English glossary for technical terms
- **Pure English audience** (HQ abroad, expatriate leadership) → English first
- **Executive bilingual** (C-suite in Thai-English comfort) → English with selective Thai for culturally-loaded terms

### Thai business register
- Use formal Thai (ภาษาทางการ) for written deliverables and C-suite
- Use polite particles (ครับ / ค่ะ) in spoken workshop facilitation but not in written formal reports
- Avoid literal English-to-Thai translation; adapt metaphors (e.g., "blue ocean" often stays in English; "low-hanging fruit" translates to "ผลไม้ที่เก็บได้ง่าย" but may sound stilted — prefer "quick win" or "ชัยชนะเล็กๆ ที่ทำได้เร็ว")
- Keep vendor product names in English (Oracle Fusion, SAP S/4HANA) — do not translate

## Cultural Sensitivity

### Hierarchy (ระบบอาวุโส)
- Respect seniority in workshop facilitation — senior attendees speak first unless explicitly structured otherwise
- Do not put junior attendees on the spot in front of seniors
- Use silent ideation (post-its, written Crazy 8s) to equalize voice — this is the single most important technique for Thai workshops

### Kreng jai (เกรงใจ)
- Reluctance to disagree openly, especially with seniors or guests
- Symptom: "yes" answers that mean "I heard you" not "I agree"
- Counter-measure: ask "what would have to be true for this to NOT work?" instead of "do you agree?"
- Use anonymous written input for controversial topics

### Face-saving (รักษาหน้า)
- Never publicly correct a senior's factual error — offer the correction privately or reframe
- Celebrate contributions by name in group; critique only in private
- In pre-mortems, frame failures as "the strategy failed" not "person X's idea failed"

### Consensus-building (ฉันทามติ)
- Thai organizations often decide by consensus more than by vote
- Do not force dot-voting as the decision method; use it to reveal clustering, then discuss
- Allow for post-workshop consultation (ปรึกษากลับ) before final commitment — build this into the agenda

### Relationship-first (ความสัมพันธ์)
- Thai enterprise buying is relationship-driven; workshops build trust as much as content
- Include relationship-building time (refreshments, informal conversation) — do not treat this as wasted time
- Senior sponsorship matters more than analytical rigor for initial momentum

## Regulatory Landscape

### PDPA (Personal Data Protection Act B.E. 2562 / 2019)
Applies to processing of personal data in Thailand. Key requirements:
- Lawful basis for processing (consent, contract, legal obligation, vital interest, legitimate interest, public task)
- Data subject rights (access, rectification, erasure, portability, objection)
- Data Protection Officer (DPO) appointment for certain entities
- Breach notification within 72 hours
- Cross-border transfer restrictions (requires adequate protection)
- ROPA (Record of Processing Activities) maintenance
- Penalties up to ฿5M + imprisonment

Implication for workshops: when ideating customer-facing AI, journey maps that involve personal data, or cross-border cloud, always flag PDPA compliance as a design constraint.

### Cloud Security Standard 2567 (2024)
Mandatory for government agencies and Critical Information Infrastructure (CII). Specifies:
- Data localization requirements for specific data classes
- Encryption standards
- Security controls mapped to ISO 27001 / NIST
- Incident response and reporting

Implication: Oracle / SAP / MSFT / AWS / Azure / GCP deployments for Thai public sector must map to Cloud Standard 2567. Use the `legal-it-thailand-cloud` skill for detail.

### Cybersecurity Act B.E. 2562
Governs CII cybersecurity. Applies to government, energy, finance, healthcare, transport, telecom, ICT sectors.

### Public Procurement Act B.E. 2560
Governs all government procurement. Key concepts: e-bidding, e-market, specific methods (selection, specific procurement), TOR, Middle Price, committees, appeal process.

Implication: proposals for government must be structured to meet e-GP process; envisioning workshops with government clients should produce TOR-ready requirements.

### BoT, SEC, OIC regulations
For financial services: Bank of Thailand (BoT), Securities and Exchange Commission (SEC), Office of Insurance Commission (OIC). Core regulations: IFRS 9 expected credit loss, Basel III/IV, IT Risk Guidelines, AML/CFT.

## Market Structure

### Thailand 4.0 / Digital Government
National policy framing. Use as a Why-Now driver when selling to public sector and state enterprises.

### BOI (Board of Investment)
Tax incentives for priority sectors. Relevant for manufacturing clients planning digital transformation with capex.

### EEC (Eastern Economic Corridor)
Three-province (Chonburi, Rayong, Chachoengsao) special economic zone. Smart city, digital, advanced manufacturing focus. Use as a geographic play for manufacturing and logistics deals.

### Partner ecosystem
- Oracle: Thai partners tiered (Cloud Elite, Cloud Select, Cloud Standard)
- SAP: Platinum / Gold / Silver partner tiers
- MSFT: Solutions Partner designations (Business Applications, Data & AI, etc.)
- Salesforce: Consulting Partner ranks
- Government: selected via e-GP or specific authorization

Local SI landscape is concentrated; name-recognition matters for senior stakeholder comfort.

### Fiscal cycles
- Private: calendar year (Jan–Dec) or Thai fiscal (varies)
- Government: Thai fiscal year October–September
- Budget approval: November–December typical for next-year commitments
- Implication: deal pacing must respect these cycles

## Thai-Specific Workshop Design Adjustments

- Open with relationship time (15 min for senior stakeholders; skip only if rapport already exists)
- Use silent + written ideation for at least 30% of ideation time
- Alternate small-group breakouts (safer for junior voices) and plenary (for decision-making)
- Build in "take away for consultation" time — do not force final decisions in the room unless the sponsor has pre-authorized
- Use Thai language for emotional / experiential parts (empathy, journey), English for technical / analytical parts (frameworks, value case)
- Respect seniority in seating and speaking order; deviate only with the sponsor's explicit agreement

## Thai-Specific Value-Case Language

When building the "Why Invest / Why Now / Why Us" narrative for Thai audiences:

- **Why Invest** — emphasize risk reduction and audit defensibility alongside revenue (Thai CFOs are often more conservative than Western counterparts)
- **Why Now** — tie to concrete Thai drivers: regulatory deadline, fiscal year, BOI eligibility window, competitive move, political change
- **Why Us** — emphasize local presence, Thai-speaking team, government relationships, past projects with Thai references, PDPA / Cloud Standard compliance

## Common Missteps to Avoid

- Using US-centric examples (Tesla, Amazon) as primary references — prefer Thai examples (SCB, PTT, CPF, True, Central, SCG) when available
- Applying global pricing benchmarks without local adjustment (Thai SaaS pricing typically lower than US/EU)
- Assuming English as default — ask first
- Forcing direct confrontation in workshops (use silent / anonymous methods)
- Skipping hierarchy acknowledgment (always address senior stakeholders first in introductions)
- Ignoring the fiscal-cycle dependency of government deals
