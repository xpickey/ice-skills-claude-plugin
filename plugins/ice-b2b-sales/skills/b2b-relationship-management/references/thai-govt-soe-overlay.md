# Thai Government & State Enterprise (SOE) Overlay — Reference

Selling and managing relationships in Thai government and รัฐวิสาหกิจ (state enterprises) is a distinct discipline. The buying motion, decision rights, regulatory environment, and relationship norms differ from commercial enterprise in ways that make commercial-only playbooks not just suboptimal but actively counterproductive.

This overlay sits on top of the general Thai cultural overlay (`thai-cultural-overlay.md`) and the broader skill framework.

## Customer Universe

Typical Thai government / SOE customers for enterprise software:

**Central government**:
- Ministries (กระทรวง) and their departments (กรม)
- Office of the Prime Minister and Cabinet-affiliated agencies
- Comptroller-General's Department (กรมบัญชีกลาง) — owner of GFMIS
- Revenue Department (กรมสรรพากร), Customs Department (กรมศุลกากร)

**Local government**:
- Provincial Administrative Organizations (องค์การบริหารส่วนจังหวัด — อบจ.)
- Municipal governments (เทศบาล)
- Sub-district administrations (อบต.)
- Bangkok Metropolitan Administration (BMA / กทม.)

**State enterprises (รัฐวิสาหกิจ)**:
- Energy: PTT, EGAT, MEA, PEA, Bangchak
- Telecom: NT (CAT + TOT merged)
- Transport: AOT, SRT, Thai Airways (in restructuring), MRT, BTS
- Finance: GH Bank, GSB, BAAC, EXIM Bank, IBT
- Other: TOT, Thailand Post, Thai PBS

**Universities**: state and autonomous universities under the Ministry of Higher Education

**Independent agencies**: BoT (Bank of Thailand), SEC, OIC

## Procurement Framework — The Non-Negotiable Layer

Every government / SOE engagement is shaped by the procurement law:

- **พรบ.การจัดซื้อจัดจ้างและการบริหารพัสดุภาครัฐ พ.ศ. 2560** — the Procurement Act
- **ระเบียบกระทรวงการคลังว่าด้วยการจัดซื้อจัดจ้างและการบริหารพัสดุภาครัฐ พ.ศ. 2560** — the implementing regulations
- **ระบบ e-GP** — mandatory electronic procurement platform
- **GFMIS** — government financial management information system; budget execution, payments, accounting

Procurement methods relevant to enterprise software:
- **e-bidding** (ประกวดราคาอิเล็กทรอนิกส์) — most large IT procurements
- **วิธีคัดเลือก** (selective method) — limited competition with named qualified vendors
- **วิธีเฉพาะเจาะจง** (specific method) — single-source under defined conditions
- **e-market** — for low-value, off-the-shelf items (rarely applicable to enterprise software)

For deep procurement framework guidance, route to the `govt-egp-gfmis` and `advisor-govt-gfmis` skills which contain the full legal and operational reference.

## Relationship Lifecycle (Government-Specific)

### Pre-RFP Period — Where the Real Work Happens
The relationship is built **before** the procurement opens. Once the TOR is published, formal communication is restricted; influence is limited to what was already established.

- Build relationships with the technical owners and the policy owners — they shape the TOR
- Provide white papers, demos, and technical briefings during the pre-procurement period
- Help shape the requirements through legitimate education (not by writing the TOR — which is a compliance risk)
- Reference the customer's 5-year plan, ministerial policy, or SOE corporate plan in our positioning

### TOR (Terms of Reference) Phase
- Read the TOR forensically — every clause was put there by someone for a reason
- Identify clauses that may favor specific vendors and assess implications
- Submit clarification questions formally and on schedule (note: questions are public to all bidders)
- Decide bid / no-bid based on TOR alignment, price ceiling, and incumbent dynamics

### Bid Submission
- Compliance is binary — a single missing document disqualifies; build redundant review
- Pricing is regulated — must include the "price ceiling" methodology
- Local-presence requirements — Thailand-incorporated entity, local support team, local data residency where required
- Technology-transfer commitments — training, knowledge transfer, after-sales support are typically scored

### Award and Contract
- Contract negotiation is constrained — most terms are pre-set in the TOR
- Performance bonds, warranty bonds, retention amounts are standard
- Penalty clauses (ค่าปรับ) for delay are typically THB 1,000–10,000 per day or % of contract value
- Government contracts typically include training, technology transfer, and after-sales as mandatory triad — design delivery accordingly

### Implementation
- สตง. (Office of the Auditor General) audit exposure throughout
- Internal audit (หน่วยตรวจสอบภายใน) reviews regularly
- Steering committee structures with formal minutes
- Acceptance is procedural and document-heavy — เอกสารตรวจรับ for every milestone

### AMS / Maintenance / Renewal
- Annual or multi-year AMS contracts; renewal often requires re-bid under e-GP
- Pricing uplifts politically sensitive — heavy documentation required
- Local AMS partner usually mandatory; even global vendors operate via local channel for AMS
- Performance scorecards reviewed annually for renewal decisions

## Stakeholder Map — Government Specifics

Beyond the standard buying-committee taxonomy (`stakeholder-power-mapping.md`), government / SOE accounts have additional stakeholder categories:

### Within the Customer
- **ผู้บริหารระดับสูง** — Permanent Secretary (ปลัดกระทรวง), Director-General (อธิบดี), Governor (ผู้ว่าฯ), CEO of SOE
- **ปลัดรอง / รองอธิบดี** — Deputies; often the real operational authority
- **ผู้อำนวยการ (กอง / สำนัก / ฝ่าย)** — Director-level operational owners
- **คณะกรรมการจัดซื้อจัดจ้าง** — Procurement committee; members rotate; composition often defined by regulation
- **คณะกรรมการตรวจรับ** — Acceptance committee
- **CIO / ผู้บริหารเทคโนโลยีสารสนเทศ** — Increasingly important; direct equivalent of commercial CIO
- **DPO / เจ้าหน้าที่คุ้มครองข้อมูล** — PDPA-mandated; gatekeepers on data-handling

### External / Ecosystem
- **กระทรวงดิจิทัล (DES)** — Sets digital policy and oversees several agencies
- **สำนักงาน ก.พ.ร.** — Government bureaucratic reform office; influences procurement standards
- **สตง. (Auditor General)** — Audit exposure; not a contact but a constraint
- **ป.ป.ช. (NACC)** — Anti-corruption commission; constraint
- **ผู้ตรวจการแผ่นดิน** — Ombudsman; constraint
- **Cabinet (ครม.)** — For mega-projects above threshold; political-level approval
- **SEPO** — State Enterprise Policy Office; oversees SOE governance

### Influencers
- **Big Four consultants** — Often advising the customer on technology strategy, RFP design, vendor evaluation
- **Academic advisors** — Universities consulted for technical evaluations
- **Industry associations** — TMA, TBA, FTI for SOE policy work
- **Media** — Coverage of major IT projects can shape political risk

## Cultural Calibration — Government Layer

In addition to the general Thai cultural overlay:

- **Hierarchy is more rigid** — protocol matters; titles are used; military ranks (where applicable) are observed
- **Documentation is currency** — verbal agreements have limited weight; everything material must be in writing
- **Slow is normal** — government cycles are deliberately slower than commercial; impatience reads as disrespect for due process
- **Continuity across political cycles** — civil service continuity insulates from political change, but mega-project momentum can shift with Cabinet changes
- **Consensus over individual decision** — committees are not theatre; they are how decisions actually get made
- **Corruption sensitivity is high** — anti-bribery vigilance must be visible; even appearance issues damage reputation
- **National-interest framing** — positioning as supporting Thailand's digital sovereignty, citizen service, regulatory mission lands well

## Legal and Regulatory Constraints (Beyond Procurement)

- **PDPA (พรบ.คุ้มครองข้อมูลส่วนบุคคล)** — Mandatory; government accounts often have heightened requirements
- **Cybersecurity Act (พรบ.การรักษาความมั่นคงปลอดภัยไซเบอร์)** — Critical Information Infrastructure (CII) designation triggers additional requirements
- **Cloud Security Standard 2567 (กมช.)** — For government cloud services; relevant when proposing cloud-based ERP / EPM
- **Data residency** — Thai government data often must remain in Thailand; cloud architecture must comply
- **Local-presence and Thai-language requirements** — User interfaces, documentation, support must be Thai-capable

For deep legal coverage, route to the `legal-it-thailand-cloud` skill.

## Operational Patterns

### TOR-Stage Engagement
- Provide capability briefings, not requirement specifications
- Refer to public materials (annual reports, 5-year plans, SET filings for SOE) when positioning
- Partner with academic / consulting / association ecosystems where helpful
- Maintain visibility across multiple agencies — Thai civil servants rotate; an officer in Ministry A this year may be in Ministry B next year

### Bid Strategy
- Compliance score is everything — partial compliance is non-compliance
- Price competitive but defensible — too low is suspicious, too high is uncompetitive
- Differentiation through implementation, not just product
- Highlight Thai-presence, Thai-team, Thai-success-stories prominently
- For mega-projects: prepare for committee presentations with multiple senior committee members

### Implementation Posture
- Over-document everything; assume สตง. will eventually review
- Maintain formal change-control discipline; verbal scope changes are toxic
- Steering committee discipline — formal agendas, minutes, action items
- Cultural sensitivity — implementation team is the face of the relationship for years
- Plan for staffing continuity — government accounts notice and remember team rotation

### Long-Term Position
- Government and SOE customers value long-term partners over best-quarter pricing
- Successful 5-year+ relationships compound — incumbency advantage on AMS, expansion modules, adjacent agencies
- Reference value is high — a successful government deployment opens doors across the public sector
- Failed government deployments are publicly visible (สตง. reports, news) and damage prospects across all government accounts

## Common Failure Modes (Government-Specific)

- **Treating government like commercial** — applying commercial sales velocity, discount tactics, or transactional patterns to a relationship-and-procedure environment
- **Ignoring TOR clauses** — assuming the technical evaluation will overlook compliance gaps
- **Single-point relationship** — relying on one official; civil service rotation will end the relationship
- **Late entry** — engaging only when the RFP is published; the decision was already shaped pre-RFP
- **Compliance shortcuts** — "we'll fix it later" approaches to PDPA, cybersecurity, data residency invite audit findings
- **Local-presence theatre** — claiming local capability without real Thai team / infrastructure; discovered fast
- **Quarterly pressure tactics** — pushing government cycles to fit our quarterly forecast; reads as disrespect
- **Forgetting the after-sales triad** — under-investing in training, technology transfer, and AMS commitments that the TOR explicitly required

## Cross-Skill Routing

For deep dives, route to specialist skills already available:
- **`govt-egp-gfmis`** — full procurement law, e-GP, GFMIS, COA reference
- **`advisor-govt-gfmis`** — integrated FM / budget / procurement / ERP advisory
- **`smart-pao-platform`** — local government (อบจ.) platform-specific guidance
- **`legal-it-thailand-cloud`** — PDPA, Cloud Security Standard, Cybersecurity Act for IT vendors
- **`b2b-enterprise-sale-strategy`** — government segment of the segment-specific sales playbooks

This relationship-management skill assumes those references; do not duplicate their content here.

## Output

For government accounts, every standard artifact (account plan, stakeholder map, QBR, etc.) is produced with this overlay applied. There is no separate government template; instead, the standard templates are filled with the government-aware content described above.
