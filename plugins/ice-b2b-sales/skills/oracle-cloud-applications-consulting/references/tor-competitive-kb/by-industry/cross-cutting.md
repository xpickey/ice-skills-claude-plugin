# TOR Competitive KB — cross-cutting — Oracle Fusion Standout & TOR Weaponization

---
last_verified: "2026-06-29"
source: "TOR Requirement Bank + Gap Pack v2"
confidence_note: "Confidence per record reflects whether an official KB/vendor citation exists in the source. Records with verified docs.oracle.com / netsuite.com / analyst citations are marked high; records resting partly on '[ต้อง verify]' flags or partner-blog corroboration are medium. This file is derived from a competitive TOR draft biased toward Oracle Fusion; every record therefore preserves the iCE balanced second-opinion so the same KB is safe to use whether iCE sells Fusion or defends NetSuite. NEVER invent gaps, model names, figures, or citations beyond what the source records contain."
ams_review: "yearly — re-verify product positions"
usage: "This file is used when iCE SELLS Oracle Fusion. For each capability it states where Fusion genuinely wins and the exact TOR wording (TH+EN) that makes a competing NetSuite bid score Partial/No. Read the iCE caveat before lifting any clause verbatim into a live TOR — locking a spec to one product's feature is a procurement-fairness (สตง.) risk."
scope: "cross-cutting = capabilities that apply across industries (EPM, ledgers, platform/extensibility, integration, MDM, analytics, embedded AI, architecture, data residency, GRC/SoD, accreditations). Industry-specific manufacturing/SCM/HCM records live in their own vertical files."
---

## How to read each record

- **Oracle Fusion advantage (Standout)** — the genuine, defensible reason Fusion wins on this capability.
- **TOR wording (TH / EN)** — the exact suggested spec that pushes a NetSuite bid toward Partial/No. Lift with care.
- **iCE caveat** — the balanced counter-view: where NetSuite closes the gap with a first-party add-on (NSPB = Oracle PBCS engine, NetSuite Account Reconciliation / NSAR = Oracle Fusion EPM, NSAW = Oracle ADW+OAC), where the spec is over-spec/not-applicable, and where over-tight wording is a สตง. procurement-risk. Use it to keep the TOR defensible and to know what a smart NetSuite competitor will say back.
- **Confidence** — high | medium | low, driven by citation strength in the source record.
- **หลักฐาน / Citation** — copied verbatim from the record. Not invented.

Client identity is generalized throughout to healthcare / blood-bank / biologics (serum-vaccine) / non-profit-foundation / public-sector patterns. No client name appears in this file.

---

## F-EPM-01 — Driver-based planning & budgeting (xP&A)

**Capability (TH):** การวางแผน/งบประมาณแบบ driver-based
**Capability (EN):** Driver-based planning & budgeting
**Domain:** EPM · **iCE severity:** ต่ำ

**Oracle Fusion advantage (Standout):** Oracle EPM Cloud (EPBCS) เป็นผู้นำตลาด (สาย Hyperion/PBCS) มีการวางแผนครบทุกมิติในตัว — workforce, capital และ project planning สำเร็จรูป พร้อม statistical forecasting และ what-if/predictive multi-scenario บนแพลตฟอร์มเดียว โดยไม่ต้องประกอบโมดูลเสริม. Oracle EPM Cloud is best-in-class enterprise planning with pre-built Workforce/Capital/Project modules and native predictive/multi-scenario modelling on one platform.

**TOR wording to weaponize (ภาษาไทย):** ระบบต้องมีแพลตฟอร์มการวางแผนและงบประมาณแบบ driver-based ในตัว (native) ที่รองรับ workforce, capital และ project planning พร้อมการพยากรณ์เชิงสถิติและการจำลองสถานการณ์ (predictive / what-if) โดยไม่ต้องใช้เครื่องมือภายนอก

**TOR wording (English):** The solution must provide a native driver-based planning and budgeting platform supporting workforce, capital and project planning with built-in statistical forecasting and what-if scenario modelling, without any external tool.

**iCE caveat:** จุดที่ทำให้ NetSuite ได้แค่ Partial คือ NSPB เป็น add-on ลิขสิทธิ์แยกและ "ยังไม่มีโมดูล Workforce/Capital สำเร็จรูป" (Oracle Help ระบุชัด) — ไม่ใช่เพราะ "ขาด predictive/scenario" ตามที่ร่างเดิมอ้าง เพราะ NSPB สร้างบนเอนจิน Oracle PBCS/Hyperion เดียวกันและทำ driver-based/what-if/predictive/rolling forecast + sync GL ได้จริง. การบังคับ "โมดูล Workforce/Capital สำเร็จรูป + predictive multi-scenario ระดับ enterprise" ในบริบทองค์กรสาธารณกุศลนิติบุคคลเดียวเป็น over-spec — headcount/capex วางผ่าน driver-based ใน NSPB Financials ได้. เขียนสเปกแบบ outcome-based เพื่อเลี่ยงข้อครหาล็อกสเปก.

**Confidence:** high

**หลักฐาน / Citation:**
- [WEB:docs.oracle.com] NetSuite Planning and Budgeting — 'Planning and Budgeting currently supports only the Financials module. A Workforce module is not currently available.' (article_8124016549 — ตรวจแล้วมีจริง/ยังอัปเดต)
- [WEB:docs.oracle.com] NetSuite Planning and Budgeting Financials Overview — driver-based/trend-based/direct-input accounts, what-if scenarios, Predictive Planning (article_7160253896 — ตรวจแล้วมีจริง)
- [WEB:netsuite.com] What is NetSuite Planning and Budgeting — scenario plans / what-if / driver-based, built on Oracle EPM (financial-planning.shtml)
- [KB] Netsuite-Statistical Accounting / Netsuite-General Accounting (~0.6) — base NetSuite มีเพียง GL budget + statistical allocation; KB ไม่มีเอกสาร NSPB เฉพาะ บ่งชี้ว่า xP&A เต็มต้องใช้ add-on

---

## F-EPM-02 — Advanced financial consolidation (multi-tier ownership, equity method)

**Capability (TH):** การรวมงบการเงิน (consolidation) ขั้นสูง
**Capability (EN):** Advanced financial consolidation
**Domain:** EPM · **iCE severity:** แทบไม่มีผล

**Oracle Fusion advantage (Standout):** Oracle FCCS รองรับโครงสร้างการถือหุ้นหลายชั้น (multi-tier ownership %), equity-method / equity pickup, การลงบัญชี NCI อัตโนมัติ, step acquisition และให้รายงานทั้งมุมมอง statutory และ management. ในกลุ่มข้ามชาติที่มี JV/บริษัทร่วมและถือหุ้นบางส่วนจำนวนมาก FCCS เหนือกว่าชัดเจนเพราะ NetSuite ไม่ลงบัญชี NCI/equity method ให้อัตโนมัติ.

**TOR wording to weaponize (ภาษาไทย):** ระบบต้องรองรับการรวมงบการเงินที่มีโครงสร้างการถือหุ้นหลายชั้น (multi-tier ownership %), การบันทึกแบบ equity method, การตัดรายการระหว่างกัน (intercompany elimination) อัตโนมัติ และให้รายงานได้ทั้งมุมมอง statutory และ management

**TOR wording (English):** The solution must support financial consolidation with multi-tier ownership %, equity-method accounting, automated intercompany eliminations, and both statutory and management reporting views.

**iCE caveat:** NetSuite OneWorld ทำ consolidation หลายชั้น + intercompany auto-elimination + CTA ได้ และมีฟิลด์ Ownership% — จึงไม่ใช่ "ไม่มี ownership%". สิ่งที่ขาดจริงคือการลงบัญชี/ปรับ NCI อัตโนมัติ, equity method, step acquisition, fair-value NCI (ต้องใช้ SuiteApp เช่น Eide Bailly NCI Module หรือปรับมือ). สำหรับองค์กรนิติบุคคลเดียวในประเทศที่ไม่มีโครงสร้างถือหุ้นหลายชั้น/JV ความสามารถระดับ FCCS แทบไม่ได้ใช้ = over-spec.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-General Accounting (consolidation, 0.59) — Intercompany Auto Elimination + consolidated exchange rates
- [KB] Netsuite-NetSuite OneWorld Guide (consolidation, 0.60) — subsidiary เป็นนิติบุคคล/nexus/base currency
- [WEB:timdietrich.me] NetSuite Intercompany Transactions & Eliminations — multi-tier hierarchy, auto elimination, CTA, Ownership% พร้อมข้อจำกัด equity method/complex NCI
- [WEB:suiteapp.com] Eide Bailly NCI Module for Partially-Owned Subsidiaries — ยืนยันว่า NetSuite ไม่ลงบัญชี NCI ถือหุ้นบางส่วนอัตโนมัติ ต้องใช้ SuiteApp

---

## F-EPM-03 — Automated reconciliation & close orchestration

**Capability (TH):** การกระทบยอดบัญชีอัตโนมัติ + close orchestration
**Capability (EN):** Automated reconciliation & close
**Domain:** EPM · **iCE severity:** กลาง

**Oracle Fusion advantage (Standout):** Oracle ARCS ทำ account reconciliation + transaction matching + close-task orchestration ในตัวบนแพลตฟอร์ม EPM เดียว — จับคู่รายการอัตโนมัติ, เทมเพลตกระทบยอดหลายประเภท และ audit trail สำหรับการปิดบัญชีที่ตรวจสอบได้.

**TOR wording to weaponize (ภาษาไทย):** ระบบต้องมีความสามารถกระทบยอดบัญชี (account reconciliation) แบบอัตโนมัติ พร้อมการจับคู่รายการ (transaction matching) และการบริหารงานปิดบัญชี (financial close orchestration) ในตัว

**TOR wording (English):** The solution must provide automated account reconciliation with transaction matching and financial close-task orchestration natively.

**iCE caveat:** ช่องว่างเดิมถูกปิดแล้วด้วย NetSuite Account Reconciliation (NSAR, ออกปี 2023 สร้างบน Oracle Fusion EPM — transaction matching ระดับล้านรายการ, สูงสุด ~5 ล้านแถว CSV) แต่ NSAR เป็นโมดูล add-on ลิขสิทธิ์แยก ถ้าไม่ซื้อจะเหลือแค่ period-close checklist + bank rec ตามที่ TOR อ้าง. สำหรับนิติบุคคลเดียว transaction matching อัตโนมัติระดับล้านรายการเป็น nice-to-have; ควรพิจารณา TCO ของ NSAR เทียบ Oracle ARCS ที่ก็คิดค่าโมดูลแยกเช่นกัน.

**Confidence:** high

**หลักฐาน / Citation:**
- [WEB:prnewswire.com] NetSuite Account Reconciliation announced 2023-06-14 — built on Oracle Fusion EPM, transaction matching engine + reconciliation/close management
- [WEB:oracle.com] NSAR What's New 2023 — transaction matching export สูงสุด 5,000,000 แถว CSV
- [KB] Netsuite-General Accounting (reconciliation_close, 0.62) — Period Close Checklist
- [KB] NETSUITE_FOR_CONSULTANTS (reconciliation_close, 0.63) — Period Close / period lockdown

---

## F-FIN-01 — Multi-GAAP / secondary ledgers

**Capability (TH):** Multi-GAAP / secondary ledgers
**Capability (EN):** Multi-GAAP / secondary ledgers
**Domain:** Finance · **iCE severity:** ต่ำ

**Oracle Fusion advantage (Standout):** Oracle รองรับ primary ledger + multiple secondary/reporting ledgers หลายชุด พร้อม mapping อัตโนมัติ — ยืดหยุ่นกว่าและไม่ชนเพดานจำนวนสมุดสำหรับองค์กรที่ต้องการ reporting ledgers จำนวนมาก.

**TOR wording to weaponize (ภาษาไทย):** ระบบต้องรองรับ multi-GAAP ด้วยบัญชีแยกประเภทหลัก (primary) และบัญชีแยกประเภทรอง/เพื่อการรายงาน (secondary/reporting ledgers) หลายชุด พร้อมการ mapping อัตโนมัติ

**TOR wording (English):** The solution must support multi-GAAP via a primary ledger and multiple secondary/reporting ledgers with automated mapping.

**iCE caveat:** NetSuite Full Multi-Book Accounting รองรับสมุดหลัก 1 + สมุดรองสูงสุด 4 (รวม 5 สมุด active) ต่างมาตรฐาน (US GAAP/IFRS/tax/management) พร้อม COA mapping และปรับค่าเงินรายสมุด — ตรงกับ "primary + secondary + auto mapping". ข้อจำกัดจริงคือเพดาน 4 สมุดรอง และต้องเปิดผ่าน OneWorld + NetSuite PS. องค์กรที่ต้องการสมุดหลัก (statutory ไทย) + 1 สมุด IFRS/บริหาร อยู่ในเพดานสบาย ๆ → over-spec ถ้าบังคับ "หลายชุด".

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-Multi-Book Accounting (multibook_secondary, 0.71) — Full/Adjustment-Only secondary books, OneWorld only, multiple sets of records จาก transaction เดียว
- [WEB:docs.oracle.com] Planning for Multi-Book Accounting — สูงสุด 4 secondary books (รวม 5 active books), ต่าง COA/currency/accounting rules
- [WEB:netsuite.com] Multi-Book Accounting — COA mapping rules ต่อมาตรฐาน

---

## F-FIN-02 — Breadth of statutory localizations (multi-country tax)

**Capability (TH):** ความกว้างของ localization ตามกฎหมายหลายประเทศ
**Capability (EN):** Breadth of statutory localizations
**Domain:** Finance · **iCE severity:** แทบไม่มีผล

**Oracle Fusion advantage (Standout):** Oracle มี global tax engine + localization ตามกฎหมายแบบ pre-certified ครอบคลุมจำนวนประเทศมากกว่า — ข้อได้เปรียบจริงสำหรับองค์กรที่ดำเนินงานหลายประเทศ.

**TOR wording to weaponize (ภาษาไทย):** ระบบต้องมี global tax engine และชุด localization ตามกฎหมาย (statutory) แบบ pre-certified ครอบคลุมหลายประเทศ ผู้เสนอราคาต้องระบุจำนวนประเทศที่รองรับแบบ native

**TOR wording (English):** The solution must provide a global tax engine and pre-certified statutory localizations across multiple countries; the bidder must state the number of natively supported countries.

**iCE caveat:** การบังคับ "ระบุจำนวนประเทศที่รองรับ native" คือการล็อกสเปกที่ไม่สะท้อนความต้องการจริงขององค์กรที่อยู่ประเทศเดียว. NetSuite มี SuiteTax + Country Localization/International Tax Reports ~50+ ประเทศ (รวมไทยครบผ่าน Southeast Asia Localization — ใบกำกับภาษี/ภ.พ.30). Oracle ชนะเฉพาะประเทศอื่นที่องค์กรไม่ได้ใช้ → severity แทบไม่มีผล.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-Country Specific Features (0.7295)
- [WEB:docs.oracle.com] List of Country-Specific/SuiteTax Localization Features
- [WEB:suitecertified.com] NetSuite Country Localizations 50+ (secondary — corroborated)

---

## NF-PLT-01 — Extensibility without governance caps

**Capability (TH):** การต่อยอดโดยไม่มีข้อจำกัด governance
**Capability (EN):** Extensibility without governance caps
**Domain:** Technical · **iCE severity:** แทบไม่มีผล

**Oracle Fusion advantage (Standout):** Oracle OCI/VBCS/APEX เป็น general-purpose PaaS ที่ต่อยอดได้ทั้ง low-code + pro-code สำหรับสร้างแอปแยกอิสระ โดยไม่มี per-transaction governance-unit/script-unit/row cap แบบ SuiteCloud.

**TOR wording to weaponize (ภาษาไทย):** ระบบต้องมีแพลตฟอร์มการต่อยอด (extensibility) ทั้งแบบ low-code และ pro-code โดยไม่มีข้อจำกัดด้าน governance unit, script-unit หรือ row-limit ต่อ transaction

**TOR wording (English):** The solution must provide both low-code and pro-code extensibility without per-transaction governance unit, script-unit or row limits.

**iCE caveat:** ข้อความ "ต่อยอดไม่ได้" เกินจริง — NetSuite มี low-code (SuiteFlow/SuiteBuilder) + pro-code (SuiteScript 2.x), Map/Reduce รีเซ็ต governance ทุก invocation และ SuiteCloud Plus เพิ่ม concurrency. เงื่อนไข "ไม่มี governance cap ใด ๆ ต่อ transaction" เป็น over-spec เพราะทุกแพลตฟอร์มคลาวด์ multi-tenant รวม Oracle ก็มี resource limit ของตัวเอง. ปริมาณงานระดับองค์กรกลางแทบไม่ชน cap.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-SuiteScript Developer Guide (0.665) — usage/governance units
- [KB] Netsuite-SuiteScript 2.0 (0.601) — Map/Reduce map phase 10,000 / function 1,000 units, governance reset ต่อ invocation (Hard Limits on Function Invocations)
- [WEB:docs.oracle.com] NetSuite Applications Suite — Concurrency Governance Limits Based on Service Tiers and SuiteCloud Plus Licenses
- [WEB:houseblend.io] NetSuite Map/Reduce Guide — governance reset ต่อ job, processor pool แยกจาก API concurrency [ต้อง verify]

---

## NF-PLT-02 — Mature ALM & dev/test/prod environments

**Capability (TH):** ALM: dev/test/prod + on-demand refresh
**Capability (EN):** Mature ALM & environments
**Domain:** Technical · **iCE severity:** ต่ำ

**Oracle Fusion advantage (Standout):** Oracle มี dev/test/prod landscape + transport/CI-CD + on-demand environment refresh แบบเต็มรูป (ระดับ SAP-style transport) ครอบทุก config.

**TOR wording to weaponize (ภาษาไทย):** ระบบต้องมีการบริหารวงจรพัฒนาแอปพลิเคชัน (ALM) ที่สมบูรณ์: แยกสภาพแวดล้อม dev/test/prod พร้อม transport/CI-CD และการรีเฟรชสภาพแวดล้อมแบบ on-demand

**TOR wording (English):** The solution must provide mature ALM: separate dev/test/prod environments with transport/CI-CD and on-demand environment refresh.

**iCE caveat:** NetSuite มี ALM ใช้งานจริง — sandbox แยก dev/test/prod, SDF เป็น transport (customization-as-XML), SuiteCloud CLI ต่อ CI/CD (GitLab/Jenkins/GitHub Actions). จุดอ่อนจริงคือ SDF ไม่ครอบทุก customization/config (บาง PDF layout/setting ต้องตามมือ) และ sandbox refresh ไม่ instant มีรอบจำกัด. ข้อกำหนด on-demand refresh + full transport เป็น over-spec สำหรับองค์กรประเทศเดียว.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-SuiteCloud Development Framework (0.671) — SDF เป็น deployment/transport (customization-as-XML)
- [KB] Netsuite-SuiteCloud SDK Overview (0.654) — SuiteCloud CLI (Java/Node) สำหรับ SDLC/automation
- [WEB:docs.oracle.com] NetSuite Applications Suite — Limitations for Custom Transaction Forms / Customizations Supported by SDF (SDF ไม่ครอบทุก customization)
- [WEB:netsuite.com] How NetSuite Powers DevOps Pipelines with SuiteCloud Platform Developer Tools — SuiteCloud CLI ครอบ SDLC
- [WEB:salto.io] Introduction to CI/CD for SuiteScript — pipeline GitLab/Jenkins/GitHub Actions

---

## NF-INT-01 — Native enterprise iPaaS

**Capability (TH):** Native enterprise iPaaS
**Capability (EN):** Native enterprise iPaaS
**Domain:** Technical · **iCE severity:** ต่ำ

**Oracle Fusion advantage (Standout):** Oracle Integration Cloud (OIC) เป็น iPaaS พร้อม prebuilt adapters และ visual orchestration ที่วางอยู่ในตระกูล Oracle เดียวกัน.

**TOR wording to weaponize (ภาษาไทย):** ระบบต้องมีแพลตฟอร์มการเชื่อมต่อระดับองค์กร (enterprise iPaaS) ในตัว พร้อม adapter สำเร็จรูป โดยไม่บังคับให้ใช้ middleware ภายนอก

**TOR wording (English):** The solution must provide a native enterprise iPaaS with prebuilt adapters, without mandating external middleware.

**iCE caveat:** ข้อกล่าวอ้าง "ต้องพึ่ง 3rd-party iPaaS" เกินจริง — NetSuite ต่อ API ได้เอง (SuiteTalk REST/SOAP, RESTlets, SuiteScript, SuiteAnalytics Connect ODBC/JDBC) ขาดเพียง visual orchestration แบบลากวางในตัว. สำคัญ: OIC ของ Oracle ก็เป็นไลเซนส์แยกคิดตามปริมาณ message (~$2–10k/เดือน) — ทั้งสองค่ายต้องมีชั้น iPaaS แยกเมื่องานหนักจริง การบังคับ "iPaaS ในตัว" จึงเป็นเกณฑ์ที่ตัด NetSuite ด้วยมาตรฐานที่ Oracle เองก็ไม่ผ่านแบบ native = over-spec.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-SuiteCloud Platform Introduction (0.686)
- [KB] Netsuite-SuiteTalk REST Web Services (0.685)
- [WEB:houseblend.io] Celigo vs Boomi: NetSuite iPaaS Comparison (ยืนยันมีจริง)
- [WEB:erpresearch.com] Oracle ERP Fusion Cloud Pricing — OIC เป็นไลเซนส์แยก คิดตาม message (ยืนยันมีจริง)

---

## NF-INT-02 — Native MDM / data governance

**Capability (TH):** Master Data Management (MDM)
**Capability (EN):** Native MDM / data governance
**Domain:** Technical · **iCE severity:** แทบไม่มีผล

**Oracle Fusion advantage (Standout):** Oracle มี MDM (Customer/Product/Supplier Hub) และ data governance เชิงลึกสำหรับสภาพแวดล้อมหลายระบบต้นทาง/หลายอินสแตนซ์.

**TOR wording to weaponize (ภาษาไทย):** ระบบต้องมีการบริหารข้อมูลหลัก (master data management) และการกำกับดูแลข้อมูล (data governance) ในตัว

**TOR wording (English):** The solution must provide native master data management (MDM) and data governance.

**iCE caveat:** คะแนน 0 "ทำไม่ได้เลย" เกินจริง — NetSuite มี Duplicate Record Detection & Record Merge (EntityDeduplicationTask), always-on audit trail บน master data, field-level/role-based security และ GRC ที่รวมใน platform license แล้ว. ที่ขาดจริงคือ MDM hub หลายโดเมนเฉพาะทาง. และ Oracle MDM เองก็เป็นโมดูล/ไลเซนส์แยก ไม่ใช่ของแถมใน Fusion. องค์กรที่ใช้ ERP อินสแตนซ์เดียว NetSuite เป็น single source of truth อยู่แล้ว → MDM hub เป็น over-spec.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] NetSuite Basics — Duplicate Record Detection & Merge (0.65)
- [KB] Netsuite-SuiteScript 2.0 API Reference — EntityDeduplicationTask (0.682)
- [WEB:netsuite.com] Governance, Risk & Compliance — audit trail บน master data + field-level security (รวมใน platform license, ยืนยันแล้ว)
- [WEB:oracle.com] Oracle MDM = Customer/Product/Supplier Hub (โมดูลแยก)

---

## NF-ANL-01 — Enterprise embedded analytics (in-memory)

**Capability (TH):** Embedded analytics ระดับองค์กร
**Capability (EN):** Enterprise embedded analytics
**Domain:** Technical · **iCE severity:** ต่ำ

**Oracle Fusion advantage (Standout):** Oracle OTBI + OAC + Autonomous DB วิเคราะห์ in-memory บนข้อมูลปริมาณมากในตัว — enterprise embedded + self-service analytics บนสแตกเดียวกัน.

**TOR wording to weaponize (ภาษาไทย):** ระบบต้องมีการวิเคราะห์ข้อมูลแบบฝังในตัว (embedded) และแบบ self-service บนข้อมูลปริมาณระดับองค์กร (in-memory) โดยไม่ต้องซื้อ data warehouse แยกต่างหาก

**TOR wording (English):** The solution must provide embedded and self-service analytics on enterprise-scale data (in-memory) without requiring a separately licensed data warehouse.

**iCE caveat:** เกณฑ์ "ไม่ต้องซื้อ DW แยก" ตัด NetSuite ด้วยมาตรฐานที่ Oracle เองก็ไม่ผ่าน — งานวิเคราะห์หนักของ NetSuite ใช้ NSAW ซึ่งสร้างบน Oracle ADW + OAC (สแตกเดียวกับที่ Oracle ยกเป็นจุดเด่น) และ Oracle ก็ขาย OAC/Autonomous DW แยกเช่นกัน. native SuiteAnalytics (Workbook + Saved Search + Dashboard/KPI) เป็น self-service real-time อยู่แล้ว เพียงพอกับ dashboard เชิงปฏิบัติการ/กองทุน-บริจาค → in-memory ระดับองค์กรเป็น over-spec.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-SuiteAnalytics Workbook (0.63)
- [WEB:netsuite.com] NetSuite Analytics Data Warehouse — built on Oracle ADW + OAC
- [WEB:katoomi.com] NetSuite Analytics Warehouse: A Technical Overview (ADW columnar + OAC)

---

## NF-ANL-02 — Embedded generative AI / ML across suite

**Capability (TH):** Embedded Generative AI / ML
**Capability (EN):** Embedded GenAI across suite
**Domain:** Technical · **iCE severity:** ต่ำ

**Oracle Fusion advantage (Standout):** Oracle ฝัง AI/GenAI ทั่ว Fusion (finance/SCM/HCM) กว้างและสุกกว่า พร้อม anomaly detection/ML forecasting ในหลายโมดูลบน data model เดียว.

**TOR wording to weaponize (ภาษาไทย):** ระบบต้องมี generative AI / machine learning ฝังในตัว ครอบคลุมงาน finance, supply chain และ HCM

**TOR wording (English):** The solution must provide embedded generative AI / machine learning across finance, supply chain and HCM.

**iCE caveat:** ภาพ "AI ของ NetSuite ใหม่และเบา" ล้าสมัย — ตั้งแต่ 2024.1 NetSuite ฝัง Text Enhance (OCI GenAI) + Bill Capture/Document AI ทั่ว finance/HR/SCM และ 2025.1 เพิ่ม SuiteAnalytics Assistant. ที่ต้องซื้อแยกคือ anomaly detection + ML forecasting (Intelligent Performance Management) ในโมดูล NetSuite EPM. Oracle ยังกว้าง/สุกกว่าจริง แต่การล็อกสเปกจาก roadmap วันนี้เสี่ยงเลือกจากแผนมากกว่าของจริง.

**Confidence:** high

**หลักฐาน / Citation:**
- [WEB:netsuite.com] New NetSuite Features Build AI into Everyday Processes
- [WEB:cio.com] NetSuite adds more Text Enhance gen AI capabilities
- [WEB:netsuite.com] GenAI powers new assistant, automated insights in NetSuite 2025.1

---

## NF-ARC-01 — Tier-1 transaction throughput / no governance cap

**Capability (TH):** Tier-1 transaction throughput
**Capability (EN):** Tier-1 throughput, no governance cap
**Domain:** Technical · **iCE severity:** แทบไม่มีผล

**Oracle Fusion advantage (Standout):** Oracle Fusion + Autonomous DB รองรับ throughput ระดับ tier-1 สำหรับปริมาณธุรกรรมองค์กรขนาดใหญ่มาก.

**TOR wording to weaponize (ภาษาไทย):** ระบบต้องพิสูจน์ได้ว่ารองรับปริมาณธุรกรรมระดับองค์กรขนาดใหญ่ (tier-1) โดยไม่มีการจำกัด (throttling) หรือ governance cap ผู้เสนอราคาต้องระบุ throughput (ล้านรายการ/วัน)

**TOR wording (English):** The solution must demonstrate proven tier-1 enterprise transaction throughput without throttling or governance caps; the bidder must state throughput (million transactions/day).

**iCE caveat:** NetSuite มี governance limit จริง (Map/Reduce ~10,000 units/exec; search 1,000 แถวผ่าน getRange / 4,000 ผ่าน .each()) แต่เป็นเพดาน "ต่อสคริปต์/ต่อหน้า" ไม่ใช่เพดานปริมาณธุรกรรมธุรกิจ — งานปริมาณมากใช้ Map/Reduce + runPaged() แบ่งหน้าได้ และตั้งแต่ ก.พ. 2025 NetSuite รันบน Oracle Autonomous Database/OCI กว่า 12 region. โหลดระดับองค์กรกลาง (blood-bank/รพ./บริจาค/จัดซื้อ) ไม่ถึงล้านรายการ/วัน → ข้อกำหนดนี้เป็น over-spec/ล็อกสเปก.

**Confidence:** high

**หลักฐาน / Citation:**
- [WEB:docs.oracle.com] NetSuite Help — Search getRange/.each() limits (1,000/4,000)
- [WEB:prnewswire.com] NetSuite Migrates to Oracle Autonomous Database (Feb 2025; 'over a dozen regions')
- [KB] Netsuite-SuiteScript 2.0 API Reference — runPaged()/governance (0.577)

---

## NF-ARC-02 — Deployment options & data residency / sovereignty

**Capability (TH):** ทางเลือกการติดตั้ง / data residency
**Capability (EN):** Deployment & data residency options
**Domain:** Technical · **iCE severity:** สูง

**Oracle Fusion advantage (Standout):** Oracle มีเส้นทาง in-country/sovereign (Oracle Alloy / AIS Cloud ในไทย, EU Sovereign Cloud) + Cloud@Customer + regional DC + private options ที่ NetSuite ไม่มี — เป็น gap ที่ปิดด้วย SuiteApp/custom ไม่ได้เลย. นี่คือหนึ่งใน "ประเด็นควรพิจารณาจริง" ตาม second-opinion.

**TOR wording to weaponize (ภาษาไทย):** ระบบต้องมีทางเลือกการติดตั้งที่ยืดหยุ่น รวมถึงตัวเลือกเก็บข้อมูลภายในประเทศ (data residency) หรือแบบ dedicated / Cloud@Customer

**TOR wording (English):** The solution must offer flexible deployment options including in-country data residency or a dedicated / Cloud@Customer option.

**iCE caveat:** ข้อจำกัด NetSuite ถูกต้อง (multi-tenant SaaS ล้วน ไม่มี on-prem/private/Cloud@Customer, ไม่มี DC ในไทย, ยังไม่รองรับ Oracle EU Sovereign Cloud) — แต่พึงระบุว่า Oracle Fusion SaaS แบบ public มาตรฐานก็ไม่มี region ในไทยเช่นกัน; ข้อได้เปรียบ Oracle คือ "เส้นทาง" sovereign/in-country (Alloy/AIS/EU Sovereign) ไม่ใช่ public SaaS ปกติ. on-prem/private เป็น over-spec เมื่อองค์กรเลือก SaaS และ PDPA ไทยไม่บังคับเก็บข้อมูลในประเทศ. สำหรับข้อมูลสุขภาพ/ผู้บริจาค (blood-bank/รพ.) sovereignty เป็นประเด็นนโยบายบอร์ดที่มีน้ำหนักจริง — legitimate ที่จะใส่ แต่ควรกรอบเป็น "ระบุทางเลือก" มากกว่าบังคับ Cloud@Customer เพื่อลดข้อครหาล็อกสเปก. [ต้อง verify สถานะ Oracle EU Sovereign Cloud / in-country roadmap]

**Confidence:** medium

**หลักฐาน / Citation:**
- [WEB:netsuite.com] What is NetSuite ERP (multi-tenant SaaS, no on-prem)
- [WEB:sota.io] NetSuite NOT available on Oracle EU Sovereign Cloud as of Q1 2026 [ต้อง verify]
- [WEB:oracle.com] AIS Cloud / Oracle Alloy — in-country Thai cloud (2024)
- [KB] NSTWP — multi-tenant shared service (0.541)

---

## NF-SEC-01 — Automated SoD & access governance

**Capability (TH):** Automated Segregation of Duties (SoD)
**Capability (EN):** Automated SoD & access governance
**Domain:** Technical · **iCE severity:** สูง

**Oracle Fusion advantage (Standout):** Oracle Risk Management Cloud (Advanced Access Controls) ทำ automated SoD + continuous controls monitoring + ruleset สำเร็จรูปจำนวนมาก + access governance ในตัว — เหนือกว่าชัดเจน. เป็น "ประเด็นควรพิจารณาจริง" เพราะอยู่ภายใต้การตรวจของ สตง.

**TOR wording to weaponize (ภาษาไทย):** ระบบต้องแสดงการตรวจจับ SoD และการควบคุมเชิงป้องกัน (preventive controls) แบบอัตโนมัติ พร้อมการกำกับดูแลสิทธิ์เข้าถึง (access governance) — ไม่ว่าจะโดย native หรือผ่าน certified add-on

**TOR wording (English):** The solution must demonstrate automated SoD detection and preventive controls with access governance — natively or via a certified add-on.

**iCE caveat:** gap "engine SoD อัตโนมัติ native" มีจริง — แต่ข้อความ "ไม่มี access governance ระดับ audit" ลดทอนของจริง: NetSuite มี role-based security ละเอียด, เครื่องมือตรวจสิทธิ์ (Use Searches to Audit Roles, Show Role Permission Differences), Login Audit Trail, 2FA/SSO และผ่าน SOC 1/2, ISO 27001. ปิด gap ด้วย SuiteApp certified ต้นทุนไม่สูง (Fastpath Assure, Netwrix Strongpoint, SafePaaS). continuous controls monitoring ระดับ enterprise เกินความจำเป็นของ NGO ประเทศเดียว — วางแผน SuiteApp SoD ก่อน go-live เพื่อผ่าน สตง. สำคัญเรื่องความสมมาตร: คำตอบ SoD/CCM ของ Oracle เอง (Advanced Access Controls / Risk Management Cloud) ก็เป็น add-on ที่ต้องซื้อไลเซนส์แยก — ไม่ใช่ของที่มากับ base Fusion — เช่นเดียวกับที่ OIC/MDM/NSAW เป็นไลเซนส์แยกทั้งสองค่าย ดังนั้นการเขียน "native, ไม่พึ่งบุคคลที่สาม" จึงล็อกสเปกเข้ากับโมดูล Oracle ที่ต้องจ่ายเงินเพิ่มพอ ๆ กับที่ตัด NetSuite+Fastpath ออก. So a "native, no third-party" clause spec-locks to a paid Oracle module just as much as it excludes NetSuite+Fastpath — write it outcome-based instead.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-Managing Users & Roles (0.6678) — Use Searches to Audit Roles + Login Audit Trail
- [KB] Netsuite-Managing Users & Roles (0.6544) — periodic access review/terminated-user revocation
- [WEB:oracle.com] Oracle Advanced Access Controls Cloud Service datasheet — automated SoD + continuous monitoring + ruleset สำเร็จรูปจำนวนมาก
- [WEB:suiteapp.com] Fastpath Assure for NetSuite — SoD analysis by user/role/permission (ruleset 125+ conflicts)
- [WEB:mysuite.tech] Segregation of Duties in NetSuite: where native tools stop

---

## NF-SEC-02 — Industry / government accreditations

**Capability (TH):** Industry / Government Accreditations
**Capability (EN):** Industry/government accreditations
**Domain:** Technical · **iCE severity:** แทบไม่มีผล

**Oracle Fusion advantage (Standout):** Oracle มี industry solutions + accreditation ภาครัฐ/regulated ที่กว้างกว่า (FedRAMP/IL/sovereign) จาก OCI.

**TOR wording to weaponize (ภาษาไทย):** ผู้เสนอราคาต้องแสดงรายการการรับรอง (accreditation) ด้านอุตสาหกรรมและภาครัฐ/หน่วยงานกำกับ ที่เกี่ยวข้องกับธุรกิจของหน่วยงาน

**TOR wording (English):** The bidder must provide a list of relevant industry and government/regulatory accreditations applicable to the organization's business.

**iCE caveat:** Oracle NetSuite ถือใบรับรองสากลครบ: SOC 1/SOC 2 Type II, ISO 27001/27018/42001, PCI DSS Level 1 + PCI SSF. accreditation ภาครัฐที่ Oracle กว้างกว่า (FedRAMP/IL) เป็นการรับรองของรัฐบาล/กลาโหมสหรัฐฯ ไม่ใช่ข้อกำหนดของหน่วยงานไทย — การบังคับ "accreditation ภาครัฐกว้าง" จึงเป็น over-spec ที่เอียงเข้าหา Oracle. ใบรับรองที่เกี่ยวจริง (ISO 27001, SOC, PCI สำหรับรับบริจาคบัตรเครดิต) NetSuite มีครบ.

**Confidence:** high

**หลักฐาน / Citation:**
- [WEB:netsuite.com] NetSuite Application and Operational Security — SOC 1/2, ISO 27001/27018/42001, PCI DSS, PCI SSF
- [WEB:houseblend.io] NetSuite Audit Readiness: SOC 1, SOC 2 & ISO 27001 Guide
- [WEB:stratusgreen.com] NetSuite PCI Compliance — Level 1 Service Provider

---

## GP-FUNC-12 — Group consolidation & multi-GAAP at scale

**Capability (TH):** งบรวมกลุ่มหลายมาตรฐานบัญชี ขนาดใหญ่
**Capability (EN):** Group consolidation & multi-GAAP at scale
**Domain:** Finance · **iCE severity:** แทบไม่มีผล
*(NetSuite 3★ · Oracle Fusion 5★ · SAP S/4HANA 4★ · Gap Severity: High · Fusion เด่นสุด ✔✔)*

**Oracle Fusion advantage (Standout):** Oracle FCCS (Hyperion) นำหน้าทั้ง NetSuite และ SAP เรื่อง consolidation ซับซ้อน "ขนาดใหญ่/หลาย GAAP/NCI-equity method" — สำหรับกลุ่มบริษัทใหญ่หลายสิบนิติบุคคลข้ามประเทศที่ถือหุ้นบางส่วน ข้อได้เปรียบ NCI/equity method มีจริงและสำคัญ.

**TOR wording to weaponize (ภาษาไทย):** ระบบต้องรองรับการจัดทำงบการเงินรวมของกลุ่มกิจการที่มีหลายนิติบุคคลข้ามประเทศ หลายมาตรฐานบัญชี (multi-GAAP) พร้อม equity method / NCI และการรวมงบระดับ enterprise scale

**TOR wording (English):** The solution must support group consolidation across many cross-border entities and multiple accounting standards (multi-GAAP) at enterprise scale, including equity method / NCI accounting.

**iCE caveat:** การเปรียบเทียบนี้ค่อนข้างสมดุลอยู่แล้ว (NetSuite ได้ 3/5) — OneWorld + Multi-Book เพียงพอระดับ mid-market และทำ consolidation พื้นฐาน + multi-GAAP ได้ในตัว. "group consolidation & multi-GAAP at scale" เกินความจำเป็นของนิติบุคคลเดียวในไทย = over-spec ในบริบทองค์กรสาธารณกุศล ไม่มี use case จริง.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-Multi-Book Accounting (multibook_secondary, 0.71) — secondary books multi-GAAP
- [KB] Netsuite-General Accounting (consolidation, 0.59) — Intercompany Auto Elimination + consolidated exchange rates
- [WEB:timdietrich.me] NetSuite Intercompany Transactions & Eliminations — OneWorld เพียงพอ mid-market แต่จำกัดในเคสซับซ้อน (equity method, complex NCI)

---

## GP-FUNC-13 — Enterprise planning & budgeting (EPM / xP&A)

**Capability (TH):** วางแผนงบ/พยากรณ์องค์กร (EPM / xP&A)
**Capability (EN):** Enterprise Planning & Budgeting (EPM / xP&A)
**Domain:** EPM · **iCE severity:** ต่ำ
*(NetSuite 2★ · Oracle Fusion 5★ · SAP S/4HANA 4★ · Gap Severity: Critical · Fusion เด่นสุด ✔✔)*

**Oracle Fusion advantage (Standout):** Oracle EPM Cloud = best-in-class (Hyperion) — มี FCCS/ARCS/PCMCS และโมดูล Workforce/Capital สำเร็จรูปในชุดเดียว; ความกว้างของ suite และระดับ customization (EPBCS เต็ม) เหนือ NSPB (รุ่น Financials productized).

**TOR wording to weaponize (ภาษาไทย):** ระบบต้องมีชุดบริหารผลการดำเนินงานองค์กร (EPM) ครบวงจรในตระกูลเดียวกัน ครอบคลุม planning/budgeting (driver-based, multi-scenario), consolidation, account reconciliation และ profitability/cost management พร้อมโมดูล Workforce และ Capital planning สำเร็จรูป

**TOR wording (English):** The solution must provide a complete EPM suite in one product family covering planning/budgeting (driver-based, multi-scenario), consolidation, account reconciliation and profitability/cost management, with pre-built Workforce and Capital planning modules.

**iCE caveat:** การให้ 2/5 และตี "Critical gap" สูงเกินจริง — NSPB ใช้เอนจิน PBCS/Hyperion เดียวกับ Oracle EPM Cloud จึงทำ xP&A core (driver-based, scenario, predictive, rolling forecast) ได้ในตัว. ช่องว่างจริงคือ "ความกว้างของ suite" (FCCS/ARCS/PCMCS + Workforce/Capital สำเร็จรูป) ไม่ใช่ core capability ที่ขาด. xP&A ระดับ Hyperion เต็มสูบเกินสิ่งที่สำนักงบประมาณองค์กรการกุศลใช้จริง = over-spec.

**Confidence:** high

**หลักฐาน / Citation:**
- [WEB:docs.oracle.com] NetSuite Planning and Budgeting Financials Overview — driver-based, what-if scenarios, Predictive Planning (article_7160253896 — ตรวจแล้วมีจริง)
- [WEB:docs.oracle.com] NetSuite Planning and Budgeting — รองรับเฉพาะโมดูล Financials, ไม่มี Workforce module (article_8124016549 — ตรวจแล้วมีจริง)
- [WEB:netsuite.com] What is NetSuite Planning and Budgeting — built on Oracle EPM Cloud engine, scenario/what-if (financial-planning.shtml)
- [KB] Netsuite-Statistical Accounting / Netsuite-General Accounting (~0.6) — base NetSuite มีเพียง budget/statistical allocation พื้นฐาน

---

## GP-FUNC-16 — Statutory localization, tax engine & e-invoicing (e-Tax Invoice TH)

**Capability (TH):** Tax engine & localization ตามกฎหมายแต่ละประเทศ
**Capability (EN):** Statutory localization, tax engine & e-invoicing
**Domain:** Finance · **iCE severity:** สูง
*(NetSuite 2★ · Oracle Fusion 4★ · SAP S/4HANA 5★ · Gap Severity: Critical · Fusion เด่นสุด ✔)*

**Oracle Fusion advantage (Standout):** Oracle (และ SAP) มี localization/e-invoice ครอบคลุมประเทศมากที่สุด พร้อม tax engine + e-invoicing ตามข้อกำหนดของแต่ละประเทศในตัว.

**TOR wording to weaponize (ภาษาไทย):** ระบบต้องมี statutory localization และ tax engine ในตัว พร้อมรองรับ e-Tax Invoice / e-Receipt ตามมาตรฐานกรมสรรพากรไทย (รูปแบบ XML ที่ส่งกรมสรรพากรได้) โดยไม่ต้องพัฒนา custom template หรือพึ่ง add-on ภายนอก

**TOR wording (English):** The solution must provide built-in statutory localization and a tax engine, including Thai e-Tax Invoice / e-Receipt (Revenue-Department-compliant XML submission) natively, without custom templates or external add-ons.

**iCE caveat:** SuiteTax + SEA Localization รองรับ VAT/ภ.พ.30/ใบกำกับภาษี-เครดิตโน้ตตามรูปแบบกรมสรรพากรครบสำหรับไทย — การให้ 2★ ประเมินต่ำไปสำหรับ scope ไทย. ช่องว่างจริงและ legitimate คือ e-Tax Invoice/e-Receipt แบบ XML ส่งกรมสรรพากร (Electronic Invoicing SuiteApp เป็นเพียงกรอบ ต้องทำ template เอง/ใช้ partner) — เป็นข้อบังคับตามกฎหมายไทย ต้องวางแผนปิด gap ก่อน go-live. ส่วน "ความกว้างหลายประเทศ" ไม่เกี่ยว. ระวัง: เขียนสเปกให้ "รองรับ e-Tax Invoice ไทย" ได้ (legitimate) แต่ "โดยไม่ต้อง add-on ใด ๆ" อาจล็อกสเปกเพราะฝั่ง Oracle ก็มักต้อง localization pack/partner เช่นกัน.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-Country Specific Features (0.7242, SuiteTax Reports/VAT)
- [WEB:docs.oracle.com] Thailand Tax Invoice & Credit Memo Templates (SEA Localization, P.P.30)
- [WEB:docs.oracle.com] Electronic Invoicing Overview (กรอบ XML/JSON ไม่มี native มาตรฐานไทย)

---

## GP-FUNC-27 — Governance, Risk & Compliance (GRC) / SoD

**Capability (TH):** กำกับ ความเสี่ยง การควบคุม / SoD
**Capability (EN):** Governance, Risk & Compliance (GRC) / SoD
**Domain:** GRC · **iCE severity:** สูง
*(NetSuite 2★ · Oracle Fusion 5★ · SAP S/4HANA 5★ · Gap Severity: High · Fusion เด่นสุด ✔)*

**Oracle Fusion advantage (Standout):** Oracle Risk Management Cloud (และ SAP GRC Access Control) มี automated SoD + continuous controls monitoring เป็น engine native — เหนือกว่าเครื่องมือ role/permission + audit ของ NetSuite.

**TOR wording to weaponize (ภาษาไทย):** ระบบต้องแสดง Segregation of Duties แบบอัตโนมัติ (ruleset สำเร็จรูป), continuous controls monitoring และ preventive control (บล็อกการอนุมัติที่ขัด SoD) — ไม่ว่าจะโดย native GRC engine หรือผ่าน certified add-on

**TOR wording (English):** The solution must demonstrate automated Segregation of Duties (pre-built rulesets), continuous controls monitoring and preventive controls (blocking SoD-violating approvals) — natively or via a certified add-on.

**iCE caveat:** เรตติ้ง 2★ (Partial) สมเหตุผล และ gap automated SoD/CCM เทียบ Oracle/SAP มีจริง — แต่ "SoD/role review พื้นฐาน" ลดทอน: NetSuite มี audit role + audit trail native และ ecosystem SoD certified เต็มที่ (Fastpath Assure, Netwrix Strongpoint, SafePaaS). SoD เกี่ยวข้องเพราะองค์กรอยู่ใต้การตรวจของ สตง. — ต้องวางแผนติดตั้ง SuiteApp SoD ก่อน go-live. continuous controls monitoring ระดับ enterprise เต็มรูปเป็นส่วนเสริมที่เลือกได้ (over-spec). สำคัญเรื่องความสมมาตร: คำตอบ SoD/CCM ของ Oracle เอง (Advanced Access Controls / Risk Management Cloud) ก็เป็น add-on ที่ต้องซื้อไลเซนส์แยก — ไม่ใช่ native-in-base Fusion — เช่นเดียวกับที่ KB นี้เปิดเผยเรื่อง OIC/MDM/NSAW ว่าเป็นไลเซนส์แยกทั้งสองค่าย ดังนั้น "native GRC engine โดยไม่ต้องพึ่ง SuiteApp" จึงล็อกสเปกเข้ากับโมดูล Oracle ที่ต้องจ่ายเงินเพิ่มพอ ๆ กับที่ตัด NetSuite+Fastpath ออก — เขียนแบบ outcome-based เพื่อลดความเสี่ยง สตง.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-Managing Users & Roles (0.695/0.6678) — role permissions + audit role searches
- [WEB:netsuite.com] What is NetSuite Governance, Risk & Compliance? — GRC = native controls + partner SuiteApp (ไม่ใช่ SoD engine native)
- [WEB:oracle.com] Oracle Risk Management Cloud — automated SoD + continuous monitoring
- [WEB:netwrix.com] NetSuite Segregation of Duties (Strongpoint) — alert on SoD conflicts
- [WEB:suiteapp.com] Fastpath Assure for NetSuite

---

## GP-TECH-01 — In-memory DB & real-time embedded analytics

**Capability (TH):** ฐานข้อมูลในหน่วยความจำ / วิเคราะห์เรียลไทม์
**Capability (EN):** In-memory DB & real-time embedded analytics
**Domain:** Technical · **iCE severity:** แทบไม่มีผล
*(NetSuite 2★ · Oracle Fusion 4★ · SAP S/4HANA 5★ · Gap Severity: High · Fusion เด่นสุด ✔)*

**Oracle Fusion advantage (Standout):** Oracle มี in-memory columnar analytics ผ่าน OAC + Autonomous DW; SAP HANA columnar in-memory เป็นจุดแข็งสูงสุดของ tier-1.

**TOR wording to weaponize (ภาษาไทย):** ระบบต้องมีสถาปัตยกรรมวิเคราะห์แบบ in-memory columnar สำหรับข้อมูลปริมาณมหาศาลในตัว รองรับ real-time embedded analytics บนฐานข้อมูลประสิทธิภาพสูง

**TOR wording (English):** The solution must provide in-memory columnar analytics architecture for very large data volumes natively, supporting real-time embedded analytics on a high-performance database.

**iCE caveat:** ข้อความ "NetSuite ไม่มี analytics layer แบบ real-time" ไม่ถูกต้อง — NetSuite รันบนฐานข้อมูลเดียว โพสต์ธุรกรรม real-time และ SuiteAnalytics/Saved Search/Dashboard อ่านข้อมูลสดทันทีเป็นจุดแข็ง native. ที่ขาดคือ engine in-memory columnar แบบ HANA (เปิดผ่าน NSAW = Oracle ADW ซึ่งเป็นโมดูลเสริม). in-memory tier-1 เป็น over-spec สำหรับมูลนิธิ ไม่มี use case จริง.

**Confidence:** high

**หลักฐาน / Citation:**
- [WEB:netsuite.com] SuiteAnalytics — built-in real-time reporting/searches/dashboards
- [WEB:theblueflamelabs.com] SuiteAnalytics Workbook real-time on live transactional data
- [KB] Netsuite-SuiteAnalytics Workbook (0.63)

---

## GP-TECH-02 — Very high transaction volume & concurrency

**Capability (TH):** ปริมาณธุรกรรม/ผู้ใช้พร้อมกันสูงมาก
**Capability (EN):** Very high transaction volume & concurrency
**Domain:** Technical · **iCE severity:** แทบไม่มีผล
*(NetSuite 2★ · Oracle Fusion 5★ · SAP S/4HANA 5★ · Gap Severity: Critical · Fusion เด่นสุด ✔)*

**Oracle Fusion advantage (Standout):** Oracle/SAP สเกลองค์กรใหญ่กว่าในปริมาณธุรกรรม/concurrency ระดับ tier-1 โดยไม่ต้องออกแบบ pagination/batch หลบ governance unit.

**TOR wording to weaponize (ภาษาไทย):** ระบบต้องรองรับปริมาณธุรกรรมและจำนวนผู้ใช้พร้อมกันระดับสูงมาก โดย SuiteScript unit / concurrency / search row-limit ต้องไม่เป็นข้อจำกัดต่อ batch posting หรือ integration ปริมาณมาก

**TOR wording (English):** The solution must support very high transaction volumes and concurrent users, with no SuiteScript-unit / concurrency / search row-limit constraining bulk posting or high-volume integration.

**iCE caveat:** หลักฐานที่อ้าง (search 1,000/4,000 แถว) เป็นเพดานต่อหน้า/ต่อสคริปต์ ไม่ใช่เพดานข้อมูล — เกิน 5,000 ผลลัพธ์ใช้ Query.runPaged()/saved search แบ่งหน้า (วนได้หมื่น-แสนแถว) และเพิ่ม concurrency ด้วย SuiteCloud Plus. governance ออกแบบเพื่อความเป็นธรรม multi-tenant ไม่ได้จำกัด throughput ธุรกิจ. ปริมาณ/concurrency ระดับองค์กรกลางไม่ถึงระดับชน limit → over-spec.

**Confidence:** high

**หลักฐาน / Citation:**
- [WEB:docs.oracle.com] NetSuite Help — Search Result Limits
- [KB] Netsuite-SuiteScript 2.0 — runPaged() required when >5,000 results (0.573)
- [WEB:anchorgroup.tech] Paginating large result sets via runPaged()

---

## GP-TECH-03 — Customization & extensibility platform depth (PaaS)

**Capability (TH):** แพลตฟอร์มปรับแต่ง/ต่อยอด (PaaS)
**Capability (EN):** Customization & extensibility platform depth
**Domain:** Technical · **iCE severity:** ต่ำ
*(NetSuite 3★ · Oracle Fusion 4★ · SAP S/4HANA 5★ · Gap Severity: High)*

**Oracle Fusion advantage (Standout):** SAP BTP/RAP และ Oracle (OIC/VBCS/APEX) เป็น enterprise PaaS เต็มรูปสำหรับสร้างแอปแยกอิสระ — ลึกกว่า SuiteCloud ที่ยังมี governance cap.

**TOR wording to weaponize (ภาษาไทย):** ระบบต้องมาพร้อมแพลตฟอร์ม PaaS ระดับองค์กร (general-purpose) สำหรับสร้างแอปพลิเคชันแยกอิสระบนคลาวด์เดียวกัน ทั้งแบบ low-code และ pro-code โดยไม่มี governance cap ต่อสคริปต์

**TOR wording (English):** The solution must include an enterprise general-purpose PaaS for building standalone applications on the same cloud, both low-code and pro-code, without per-script governance caps.

**iCE caveat:** เรตติ้ง 3★ พอรับได้ แต่กรอบ "สู้ไม่ได้เพราะ governance cap" เกินจริง — SuiteCloud (custom record, SuiteScript 2.x, SuiteFlow, Suitelet, RESTlet, SDF) ต่อยอดได้จริง เพียงไม่ใช่ general-purpose PaaS สำหรับสร้างแอปแยกอิสระแบบ APEX/BTP. governance เป็น guardrail ของ multi-tenant ไม่ใช่กำแพง. องค์กรระดับนี้ไม่จำเป็นต้องมี enterprise PaaS เต็มรูป → over-spec ถ้าบังคับ "สร้างแอปแยกอิสระ".

**Confidence:** medium

**หลักฐาน / Citation:**
- [KB] Netsuite-SuiteScript Developer Guide (0.665) — SuiteScript governance units
- [KB] Netsuite-SuiteCloud Development Framework (0.671) — แพลตฟอร์มต่อยอด/transport
- [KB] Netsuite-SuiteCloud Platform Introduction (0.671) — ขอบเขต SuiteCloud (SuiteScript/SuiteBuilder/SuiteFlow/SuiteBundler)
- [WEB:netsuite.com] How NetSuite Powers DevOps Pipelines with SuiteCloud Platform Developer Tools — ความกว้างของ SuiteCloud platform

---

## GP-TECH-04 — Embedded AI/ML & GenAI across processes

**Capability (TH):** AI/GenAI ฝังในกระบวนการธุรกิจ
**Capability (EN):** Embedded AI/ML & GenAI across processes
**Domain:** Technical · **iCE severity:** ต่ำ
*(NetSuite 2★ · Oracle Fusion 5★ · SAP S/4HANA 4★ · Gap Severity: High · Fusion เด่นสุด ✔✔)*

**Oracle Fusion advantage (Standout):** Oracle ฝัง AI ทั่ว Fusion + GenAI (กว้างและรวมศูนย์บน data model เดียว) ปล่อยเร็วและกว้างกว่า SAP Joule.

**TOR wording to weaponize (ภาษาไทย):** ระบบต้องมี AI/GenAI ฝังในกระบวนการธุรกิจครบทั้ง intelligent assistant, anomaly detection, ML forecasting และ document IDR ในตัว (base) โดยไม่ต้องซื้อโมดูลวิเคราะห์/EPM เพิ่ม

**TOR wording (English):** The solution must embed AI/GenAI across processes — intelligent assistant, anomaly detection, ML forecasting and document IDR — in the base product, without buying an add-on analytics/EPM module.

**iCE caveat:** ภาพ "NetSuite เพิ่งเริ่มทำ AI" ล้าสมัย — native AI ครอบหลายกระบวนการแล้ว (Text Enhance/OCI GenAI, Bill Capture/Document AI ตั้งแต่ 2024.1, SuiteAnalytics Assistant 2025.1). ที่ต้องซื้อแยกคือ anomaly detection + ML forecasting (Intelligent Performance Management ในโมดูล EPM, ~$10k–25k/ปี). ช่องว่างกับ Oracle เป็นเรื่องความกว้าง/วุฒิภาวะ + ต้นทุน add-on ไม่ใช่ "ไม่มี". การผูก "anomaly/forecasting ต้องอยู่ใน base" = ล็อกสเปกเพราะฝั่ง Oracle ก็แยก EPM.

**Confidence:** high

**หลักฐาน / Citation:**
- [WEB:netsuite.com] How NetSuite uses AI
- [WEB:houseblend.io] NetSuite AI/EPM — Exception Management + IPM (anomaly/forecast)
- [WEB:gurussolutions.com] NetSuite AI in 2026 — capabilities and features

---

## GP-TECH-05 — Enterprise BI & self-service analytics

**Capability (TH):** BI/Self-service analytics ระดับองค์กร
**Capability (EN):** Enterprise BI & self-service analytics
**Domain:** Technical · **iCE severity:** ต่ำ
*(NetSuite 2★ · Oracle Fusion 5★ · SAP S/4HANA 5★ · Gap Severity: High · Fusion เด่นสุด ✔)*

**Oracle Fusion advantage (Standout):** Oracle Analytics Cloud + Autonomous DW (และ SAP Analytics Cloud) แข็งกว่าด้าน enterprise BI/วิเคราะห์ข้ามแหล่งข้อมูล.

**TOR wording to weaponize (ภาษาไทย):** ระบบต้องมี enterprise BI และ self-service analytics ในตัว รองรับการวิเคราะห์ข้ามแหล่งข้อมูลบน data warehouse ระดับองค์กร โดยไม่ต้องซื้อ warehouse แยก

**TOR wording (English):** The solution must provide enterprise BI and self-service analytics natively, supporting cross-source analysis on an enterprise data warehouse, without a separately licensed warehouse.

**iCE caveat:** การเทียบ add-on พรีเมียมของ Oracle (OAC+ADW) กับ native ของ NetSuite ไม่เป็นธรรม — enterprise BI ของ NetSuite คือ NSAW ซึ่งก็สร้างบน OAC + Autonomous DW เดียวกัน (ต้องซื้อเพิ่มเหมือนกัน). self-service BI (SuiteAnalytics Workbook drag-drop/pivot/chart + Dashboard/KPI บนข้อมูลสด) มี native อยู่แล้ว. native + Nonprofit dashboard เพียงพอ → OAC/HANA ระดับองค์กรเกินความจำเป็น = over-spec.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-SuiteAnalytics Workbook (0.63); NetSuite Basics (0.60)
- [WEB:netsuite.com] SuiteAnalytics business intelligence — self-service
- [WEB:katoomi.com] NSAW technical overview — built on OAC + Autonomous DW

---

## GP-TECH-06 — Native iPaaS / integration platform

**Capability (TH):** แพลตฟอร์มเชื่อมต่อ (iPaaS) ในตัว
**Capability (EN):** Native iPaaS / integration platform
**Domain:** Technical · **iCE severity:** ต่ำ
*(NetSuite 3★ · Oracle Fusion 5★ · SAP S/4HANA 5★ · Gap Severity: Med · Fusion เด่นสุด ✔)*

**Oracle Fusion advantage (Standout):** Oracle OIC & SAP Integration Suite เป็น iPaaS ระดับองค์กรที่มี orchestration ในตระกูลเดียวกัน.

**TOR wording to weaponize (ภาษาไทย):** ระบบต้องมี iPaaS orchestration engine ในตัว (visual orchestration, mapping, prebuilt adapters) โดยไม่ต้องพึ่งเครื่องมือ integration ของบุคคลที่สาม

**TOR wording (English):** The solution must include a native iPaaS orchestration engine (visual orchestration, mapping, prebuilt adapters), without relying on third-party integration tools.

**iCE caveat:** เรตติ้ง 3★ สะท้อนว่า NetSuite ไม่ได้อ่อน — SuiteTalk REST/SOAP + RESTlet + SuiteScript เป็นช่องทาง integration มาตรฐานที่ใช้จริง (throttle ยกได้ด้วย SuiteCloud Plus). สิ่งที่ขาดคือ iPaaS orchestration ในตัวเท่านั้น ซึ่ง Oracle OIC/SAP Integration Suite ก็เป็น add-on แยกไลเซนส์เช่นกัน — การเทียบว่า "Oracle/SAP มีในตัว" ไม่แฟร์. ปริมาณเชื่อมต่อระดับกลางใช้ API ในตัวได้ ไม่ใช่จุดตัดสิน.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-SuiteTalk REST Web Services (0.685)
- [KB] Netsuite-SuiteCloud Platform Introduction (0.686)
- [WEB:erpresearch.com] OIC เป็นไลเซนส์แยกจาก Fusion ERP (ยืนยันมีจริง)
- [WEB:houseblend.io] NetSuite iPaaS Comparison (Celigo/Boomi/Workato/MuleSoft)

---

## GP-TECH-07 — Deployment options (public/private/on-prem)

**Capability (TH):** ทางเลือกติดตั้ง (cloud/private/on-prem)
**Capability (EN):** Deployment options (public/private/on-prem)
**Domain:** Technical · **iCE severity:** แทบไม่มีผล
*(NetSuite 1★ · Oracle Fusion 4★ · SAP S/4HANA 5★ · Gap Severity: High · Fusion เด่นสุด ✔)*

**Oracle Fusion advantage (Standout):** Oracle มี region/sovereign หลากหลาย; SAP มี private/on-prem (RISE/S4 on-prem). NetSuite เป็น public multi-tenant อย่างเดียว.

**TOR wording to weaponize (ภาษาไทย):** ระบบต้องมีทางเลือกการติดตั้งหลากหลาย (public cloud / private cloud / on-premise) เพื่อรองรับข้อกำหนดด้านความมั่นคงและการกำกับดูแลของหน่วยงาน

**TOR wording (English):** The solution must offer multiple deployment options (public cloud / private cloud / on-premise) to meet the organization's security and governance requirements.

**iCE caveat:** จริงที่ NetSuite เป็น public multi-tenant อย่างเดียว ไม่มี private/on-prem (ต่างจาก SAP RISE/S4 on-prem) — แต่ทุกอย่าง fully-managed บน OCI/Oracle Autonomous Database. การบังคับ on-prem/private ใน RFP คลาวด์เป็นการล็อกสเปกเพื่อกัน SaaS-only vendor; เมื่อองค์กรเลือก SaaS แล้ว deployment model เหล่านี้จะไม่ถูกใช้จริง → over-spec.

**Confidence:** medium

**หลักฐาน / Citation:**
- [WEB:netsuite.com] Why Multi-tenancy in the Cloud Matters (cloud-only, no on-prem)
- [WEB:netsuite.com] What is NetSuite ERP

---

## GP-TECH-08 — Data residency, sovereignty & region count

**Capability (TH):** ถิ่นที่อยู่ข้อมูล / sovereign / จำนวน region
**Capability (EN):** Data residency, sovereignty & region count
**Domain:** Technical · **iCE severity:** สูง
*(NetSuite 2★ · Oracle Fusion 5★ · SAP S/4HANA 4★ · Gap Severity: High · Fusion เด่นสุด ✔✔)*

**Oracle Fusion advantage (Standout):** Oracle มี public+gov+sovereign regions มากสุด เหมาะ TOR ภาครัฐ + เส้นทาง in-country (EU Sovereign Cloud, AIS Cloud/Oracle Alloy ไทย) ที่ NetSuite ยังไม่มี — จุดต่างที่ไม่สมมาตร.

**TOR wording to weaponize (ภาษาไทย):** ผู้เสนอราคาต้องระบุตัวเลือก data residency / sovereign region และจำนวน region ที่รองรับ รวมถึงเส้นทาง in-country สำหรับข้อมูลที่มีความอ่อนไหวสูง (ข้อมูลสุขภาพ/ผู้บริจาค)

**TOR wording (English):** The bidder must state data residency / sovereign region options and the number of supported regions, including an in-country path for highly sensitive data (health / donor data).

**iCE caveat:** NetSuite ให้ data residency ผ่าน DC หลายภูมิภาค (EU/NA/APAC) — ไม่ใช่ "ไม่มี residency". จุดต่างจริงคือไม่มี DC ในไทยและไม่รองรับ EU Sovereign Cloud; แต่ Oracle Fusion SaaS แบบ public มาตรฐานก็ไม่มี region ในไทยเช่นกัน — ข้อได้เปรียบ Oracle คือ "เส้นทาง" sovereign/in-country. PDPA ไม่บังคับ localization → เป็นประเด็นเชิงนโยบายบอร์ด. legitimate ที่จะให้น้ำหนักสำหรับข้อมูลสุขภาพ/ผู้บริจาค แต่ควรกรอบเป็น "ระบุทางเลือก + verify" ไม่ใช่บังคับ in-country เพื่อลดข้อครหา. [ต้อง verify]

**Confidence:** medium

**หลักฐาน / Citation:**
- [WEB:netsuite.com] NetSuite Data Center datasheet — EU DCs (Amsterdam/Frankfurt/London/Newport), no Thai DC
- [WEB:sota.io] NetSuite not on Oracle EU Sovereign Cloud (Q1 2026) [ต้อง verify]
- [WEB:bakermckenzie.com] Thailand cross-border data transfer — no localization mandate
- [WEB:oracle.com] AIS Cloud / Oracle Alloy Thailand (2024)

---

## GP-TECH-09 — Guaranteed performance SLA at peak

**Capability (TH):** SLA/การันตี throughput บน multi-tenant
**Capability (EN):** Guaranteed performance SLA at peak
**Domain:** Technical · **iCE severity:** แทบไม่มีผล
*(NetSuite 2★ · Oracle Fusion 4★ · SAP S/4HANA 5★ · Gap Severity: Med)*

**Oracle Fusion advantage (Standout):** Oracle/SAP วางตำแหน่งการันตี performance ช่วง peak ได้แน่นกว่า (SAP private/HANA dedicated).

**TOR wording to weaponize (ภาษาไทย):** ผู้เสนอราคาต้องระบุ SLA การันตีประสิทธิภาพ (response time/throughput) ในช่วง peak load บนสภาพแวดล้อมที่ไม่แชร์ทรัพยากร (dedicated/isolated)

**TOR wording (English):** The bidder must state a guaranteed performance SLA (response time/throughput) at peak load on a non-shared (dedicated/isolated) environment.

**iCE caveat:** ความแปรปรวน performance ช่วง peak บน shared multi-tenant เป็นลักษณะของ SaaS ทั่วไป — Oracle Fusion SaaS ก็ multi-tenant เหมือนกัน. NetSuite มี uptime SLA + Application Performance Management (APM SuiteApp ฟรี) ให้ตรวจ/จูน. การตัด NetSuite ที่ "peak SLA" ทั้งที่ Fusion ก็ shared เป็นการเทียบไม่สมมาตร; การบังคับ dedicated/isolated ล็อกสเปกไปหา SAP private. โหลด peak (รับบริจาค/ปิดบัญชี) ไม่สูงพอเป็นความเสี่ยง → over-spec.

**Confidence:** medium

**หลักฐาน / Citation:**
- [WEB:netsuite.com] Why Multi-tenancy in the Cloud Matters
- [KB] Netsuite-Application Performance Management Guide (0.564)

---

## GP-TECH-10 — Languages, country & statutory coverage

**Capability (TH):** จำนวนภาษา/ประเทศ/statutory ที่รองรับ
**Capability (EN):** Languages, country & statutory coverage
**Domain:** Technical · **iCE severity:** แทบไม่มีผล
*(NetSuite 2★ · Oracle Fusion 4★ · SAP S/4HANA 5★ · Gap Severity: High · Fusion เด่นสุด ✔)*

**Oracle Fusion advantage (Standout):** SAP ครอบคลุมประเทศมากสุด, Oracle รองลงมา — สำคัญสำหรับองค์กรข้ามชาติ. NetSuite รองรับน้อยกว่าทั้งคู่.

**TOR wording to weaponize (ภาษาไทย):** ระบบต้องรองรับจำนวนภาษา ประเทศ และชุด statutory compliance จำนวนมาก ผู้เสนอราคาต้องระบุจำนวนประเทศ/ภาษาที่รองรับแบบ pre-certified

**TOR wording (English):** The solution must support a large number of languages, countries and statutory-compliance packs; the bidder must state the number of pre-certified supported countries/languages.

**iCE caveat:** NetSuite รองรับจำนวนประเทศน้อยกว่า SAP จริง แต่ localization ไทยครบผ่าน Southeast Asia Localization + SuiteTax (ภาษาไทย, VAT ภ.พ.30, ใบกำกับภาษี/Branch ID, ภาษีหัก ณ ที่จ่าย ภ.ง.ด.). ตัวข้อความเองระบุว่า "สำคัญสำหรับองค์กรข้ามชาติ" — องค์กรประเทศเดียว (payroll ไทยอย่างเดียว) จึงเป็น over-spec ที่ชัดเจน.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-Country Specific Features — Thailand Tax Codes/VAT ภ.พ.30 (0.619)
- [KB] Netsuite-Country Specific Features — Southeast Asia Localization SuiteApp/Thailand Invoicing (0.606)

---

## GP-TECH-11 — Fine-grained access & automated SoD controls

**Capability (TH):** ควบคุมสิทธิ์ละเอียด / SoD อัตโนมัติ
**Capability (EN):** Fine-grained access & automated SoD controls
**Domain:** Technical · **iCE severity:** สูง
*(NetSuite 2★ · Oracle Fusion 5★ · SAP S/4HANA 5★ · Gap Severity: High · Fusion เด่นสุด ✔)*

**Oracle Fusion advantage (Standout):** Oracle Risk Mgmt & SAP GRC มี automated SoD/continuous controls แบบ preventive ในตัว ที่ NetSuite ไม่มี native.

**TOR wording to weaponize (ภาษาไทย):** ระบบต้องแสดงการควบคุมสิทธิ์แบบละเอียดพร้อม automated SoD controls (ruleset) และ continuous controls monitoring แบบ preventive — ไม่ว่าจะโดย native หรือผ่าน certified add-on

**TOR wording (English):** The solution must demonstrate fine-grained access control with automated SoD controls (rulesets) and preventive continuous controls monitoring — natively or via a certified add-on.

**iCE caveat:** gap automated SoD/CCM แบบ preventive มีจริง — แต่ "NetSuite role-based พื้นฐาน" มองข้ามว่า NetSuite คุมสิทธิ์ละเอียด (636+ permission ต่อ record/feature), Login Audit Trail, 2FA/TBA และ audit ได้ (detective). fine-grained access จำเป็นและ NetSuite ทำได้ดี; automated continuous SoD (preventive) ปิดด้วย add-on certified (Fastpath/Strongpoint/SafePaaS). CCM ระดับ enterprise เกินความจำเป็นของสเกล NGO. สำคัญเรื่องความสมมาตร: คำตอบ SoD/CCM ของ Oracle เอง (Advanced Access Controls / Risk Management Cloud) ก็เป็น add-on ที่ต้องซื้อไลเซนส์แยก — ไม่ใช่ native-in-base Fusion — เหมือนที่ OIC/MDM/NSAW เป็นไลเซนส์แยกทั้งสองค่าย ดังนั้นการเขียน "native, ไม่ต้อง add-on" จึงล็อกสเปกเข้ากับโมดูล Oracle ที่ต้องจ่ายเงินเพิ่มพอ ๆ กับที่ตัด NetSuite+Fastpath ออก — เขียนแบบ outcome-based เพื่อลดความเสี่ยง สตง.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-Managing Users & Roles (0.6691) — granular permission structure (636+ permissions)
- [KB] Netsuite-Authentication Guide — 2FA / token-based auth; Netsuite-Administrator Guide (0.6642) — password policy + SoD monitoring example (PO created by AP)
- [WEB:oracle.com] Oracle Advanced Access Controls — continuous SoD monitoring
- [WEB:mysuite.tech] NetSuite SoD native vs add-on boundary (detective not preventive)

---

## GP-TECH-12 — Industry-specific cloud solutions depth

**Capability (TH):** โซลูชันเฉพาะอุตสาหกรรม
**Capability (EN):** Industry-specific cloud solutions depth
**Domain:** Technical · **iCE severity:** สูง
*(NetSuite 2★ · Oracle Fusion 4★ · SAP S/4HANA 5★ · Gap Severity: High · Fusion เด่นสุด ✔)*

**Oracle Fusion advantage (Standout):** SAP มี industry solutions ลึกสุด (oil&gas, utilities, auto, pharma); Oracle รองลงมา. Fusion เหนือ NetSuite ในความลึก vertical ของอุตสาหกรรม regulated เช่น biologics/pharma GMP.

**TOR wording to weaponize (ภาษาไทย):** ระบบต้องมีโซลูชันเฉพาะอุตสาหกรรมเชิงลึก (industry cloud) ที่รองรับกระบวนการผลิตชีววัตถุ/ยาระดับ GMP (electronic batch record, potency, genealogy) แบบ validated ในตัว

**TOR wording (English):** The solution must provide deep industry-specific cloud solutions supporting GMP biologics/pharma processes (electronic batch record, potency, genealogy) as a validated capability natively.

**iCE caveat:** อุตสาหกรรมที่ร่างยกมา (oil&gas, utilities, auto) ไม่เกี่ยวกับองค์กรสาธารณกุศลเลย; และ vertical ที่เกี่ยวจริง (nonprofit/fund-grant) NetSuite แข็งและเป็น native-grade — NFP Financials SuiteApp (Revenue Restriction, Grant Management, Pledge & Donation, Net Assets/FASB), lot-numbered + expiry + FEFO + Quality Management SuiteApp. ช่องว่าง legitimate เฉพาะ "การผลิตชีววัตถุ GMP เต็มรูป (electronic batch record ลึก)" ที่ต้องประเมิน fit/เสริม ISV สำหรับหน่วยผลิตเซรุ่ม-วัคซีน — ไม่ใช่ทั้งองค์กร. อย่าเหมาว่า NetSuite "อ่อน vertical".

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-Non-Profit SuiteApps — NFP Financials/Revenue Restriction/Grant (0.63)
- [KB] NSIMG — FEFO Lot Allocations/expiry (0.658)
- [KB] Netsuite-Item Record Management — lot numbered + expiration labels (0.682)

---

## GP-TECH-13 — Upgrade control & release management

**Capability (TH):** ควบคุมการอัปเกรด / รอบ release
**Capability (EN):** Upgrade control & release management
**Domain:** Technical · **iCE severity:** ต่ำ
*(NetSuite 3★ · Oracle Fusion 4★ · SAP S/4HANA 4★ · Gap Severity: Med)*

**Oracle Fusion advantage (Standout):** SAP private/on-prem คุมรอบ upgrade เองได้มากกว่า. (หมายเหตุ: Fusion บังคับอัปเดตรายไตรมาส 4 ครั้ง/ปี ข้ามไม่ได้เช่นกัน — ข้อได้เปรียบ "คุมรอบ" ที่แท้จริงอยู่ที่ SAP private มากกว่า Fusion.)

**TOR wording to weaponize (ภาษาไทย):** ระบบต้องให้ผู้ใช้ควบคุมรอบเวลาการอัปเกรด (upgrade scheduling/deferral) และมีสภาพแวดล้อมทดสอบรีลีสล่วงหน้าตลอดเวลา

**TOR wording (English):** The solution must allow the customer to control upgrade timing (scheduling/deferral) and provide an always-available release-preview environment.

**iCE caveat:** NetSuite บังคับ upgrade 2 ครั้ง/ปี ข้ามไม่ได้จริง และมี Release Preview เฉพาะช่วง preview window — แต่การให้ Fusion เหนือกว่าทำให้เข้าใจผิด เพราะ Fusion บังคับอัปเดตถี่กว่า (รายไตรมาส). สำหรับองค์กรการกุศล forced upgrade ของ SaaS เป็นข้อดี (ทันสมัยเสมอ ไม่มีต้นทุน/โปรเจกต์อัปเกรด) ภาระจริงเหลือเพียง regression test ตามรอบ. ข้อได้เปรียบ "คุมรอบ" ที่แท้จริงเป็นของ SAP private ไม่ใช่ Fusion — ใช้ weaponize ข้อนี้ต่อ NetSuite ต้องระวังย้อนเข้าตัว Fusion.

**Confidence:** high

**หลักฐาน / Citation:**
- [WEB:terillium.com] NetSuite Upgrade Schedule — 2 major releases/ปี ข้ามไม่ได้
- [WEB:docs.oracle.com] NetSuite Release Preview — สภาพแวดล้อมทดสอบรีลีสใหม่ เปิดเฉพาะช่วง preview window (ไม่ใช่ sandbox ฟรีทั่วไป)
- [WEB:blogs.oracle.com] fusioninsider Quarterly updates made easy — Fusion อัปเดตรายไตรมาส บังคับ
- [WEB:community.oracle.com] Skipping quarterly release cycles of ERP cloud — ยืนยัน opt out/ข้ามรอบไม่ได้

---

## GP-TECH-14 — Native master data management & governance

**Capability (TH):** บริหารข้อมูลหลักในตัว (MDM/governance)
**Capability (EN):** Native Master Data Management & governance
**Domain:** Technical · **iCE severity:** แทบไม่มีผล
*(NetSuite 2★ · Oracle Fusion 4★ · SAP S/4HANA 5★ · Gap Severity: High · Fusion เด่นสุด ✔)*

**Oracle Fusion advantage (Standout):** SAP MDG มี MDM ในตัว; Oracle มี governance ผ่าน Product/Customer Hub — สำหรับ federation ข้ามหลายระบบต้นทาง/หลายอินสแตนซ์.

**TOR wording to weaponize (ภาษาไทย):** ระบบต้องมี MDM hub หลายโดเมนแบบ federation ในตัว รองรับ data stewardship และการควบคุมคุณภาพข้อมูลข้ามระบบต้นทางหลายระบบ

**TOR wording (English):** The solution must provide a native multi-domain MDM hub with federation, supporting data stewardship and cross-source data-quality controls.

**iCE caveat:** ถูกต้องที่ NetSuite ไม่มี MDM hub แท้แบบ multi-domain/federation — มีเพียง Duplicate Detection, Record Merge และ audit trail บน master data (ข้อจำกัดเชิงเทคนิคจริง). แต่ MDM federation มีค่าเมื่อมีหลายระบบต้นทาง/หลายอินสแตนซ์; องค์กรที่ใช้ ERP เดียวเป็นแกน ข้อมูลหลักอยู่ใน NetSuite อยู่แล้ว และ Oracle เองก็ทำผ่าน Product/Customer Hub โมดูลแยก ไม่ใช่ in-the-box → over-spec.

**Confidence:** medium

**หลักฐาน / Citation:**
- [KB] NetSuite Basics — Duplicate Record Detection & Merge (0.65)
- [WEB:netsuite.com] Governance, Risk & Compliance — audit trail บน master data (ยืนยันมีจริง)
- [WEB:oracle.com] Oracle Product Hub / Customer Hub (โมดูล MDM แยก)

---

## GP-TECH-15 — API governance limits (concurrency / row caps)

**Capability (TH):** ข้อจำกัด API (concurrency/row limit)
**Capability (EN):** API governance limits (concurrency / row caps)
**Domain:** Technical · **iCE severity:** แทบไม่มีผล
*(NetSuite 1★ · Oracle Fusion 4★ · SAP S/4HANA 5★ · Gap Severity: High · Fusion เด่นสุด ✔)*

**Oracle Fusion advantage (Standout):** Oracle/SAP รองรับ integration ปริมาณสูงโดยไม่ชน concurrency/row cap แบบ SuiteTalk.

**TOR wording to weaponize (ภาษาไทย):** ระบบต้องรองรับ integration ปริมาณสูงโดยไม่มีข้อจำกัด API concurrency หรือ row cap ต่อการเรียก และต้องระบุเพดาน concurrency ที่การันตี

**TOR wording (English):** The solution must support high-volume integration without API concurrency or per-call row caps, and must state the guaranteed concurrency ceiling.

**iCE caveat:** ข้อจำกัดมีจริงและตรงเอกสาร (concurrency base 5 shared / 15 Tier 1 / 20 Tier 2-Ultimate, +10 ต่อ SuiteCloud Plus; saved search SOAP 1,000 แถว/หน้า) — แต่เรตติ้ง 1★/"เพดานจริงของ integration ปริมาณสูง" เกินจริงสำหรับสเกลองค์กรกลาง: เพดานยกได้ด้วย SuiteCloud Plus และ REST/SuiteQL/RESTlet ไม่ติด cap 1,000 แถวแบบ saved search. ปริมาณจริงไม่ถึงระดับ governance เป็นคอขวด → over-spec.

**Confidence:** medium

**หลักฐาน / Citation:**
- [KB] Netsuite-SuiteTalk SOAP Web Services Platform Guide — Governance Overview (0.766)
- [KB] NSTWP — Concurrency / Search Page Size 1,000 (0.62)
- [WEB:docs.oracle.com] NetSuite Help — Concurrency Governance Limits Based on Service Tiers & SuiteCloud Plus (ยืนยันตัวเลขตรง)
- [WEB:katoomi.com] NetSuite Integration Concurrency Limits 2025 (ยืนยันมีจริง)

---

## GP-STANDOUT-01 — Fusion standout: Enterprise Planning & Budgeting (EPM / xP&A)

**Capability (TH):** วางแผนงบ-พยากรณ์องค์กร (EPM / xP&A)
**Capability (EN):** Enterprise Planning & Budgeting (EPM / xP&A)
**Domain:** EPM · **iCE severity:** ต่ำ · *(Type: Functional · Rank 1)*

**Oracle Fusion advantage (Standout):** Oracle EPM Cloud (สาย Hyperion) เป็น best-in-class — driver-based, multi-scenario, financial close/consolidation รวมศูนย์บนแพลตฟอร์มเดียว นำหน้าทั้ง NetSuite (NSPB จำกัด) และ SAP (ใช้ SAC/BPC แยกชั้น).

**TOR wording to weaponize (ภาษาไทย):** ระบบต้องมี EPM/xP&A ที่ทำ driver-based/multi-scenario planning + financial close/consolidation รวมศูนย์บนแพลตฟอร์มเดียวกับ ERP (ดู TOR-FIN-01 สำหรับข้อความบังคับเต็ม)

**TOR wording (English):** The solution must provide EPM/xP&A with driver-based/multi-scenario planning plus consolidated financial close on the same platform as the ERP (see TOR-FIN-01 for the full mandatory clause).

**iCE caveat:** EPM/xP&A ระดับ Hyperion เป็นจุดแข็ง Oracle จริง แต่ "เกินความจำเป็น" — งบประมาณ/พยากรณ์ของมูลนิธิ/หน่วยงานสาธารณกุศลใช้ NSPB + NSAW เพียงพอ. การตั้งสเปก driver-based/multi-scenario ทั้งองค์กรดันค่า license + implementation ขึ้นมากโดยไม่มี use case จริงรองรับ = over-spec.

**Confidence:** low

**หลักฐาน / Citation:** ไม่มี KB/web citation ในระเบียนนี้ (standout summary) — ยืนยัน positioning ผ่าน F-EPM-01, GP-FUNC-13, TOR-FIN-01 ที่มี citation ครบ.

---

## GP-STANDOUT-02 — Fusion standout: Embedded AI/ML & GenAI across the suite

**Capability (TH):** AI/GenAI ฝังทั่วทั้งชุดแอป
**Capability (EN):** Embedded AI/ML & GenAI across the suite
**Domain:** Technical · **iCE severity:** ต่ำ · *(Type: Technical · Rank 2)*

**Oracle Fusion advantage (Standout):** Oracle ฝัง AI/GenAI ใน Fusion ทุกโมดูลบน data model เดียว ปล่อยเร็วและกว้างกว่า rollout ของ SAP (Joule ตามมา).

**TOR wording to weaponize (ภาษาไทย):** ระบบต้องมี AI/GenAI ฝังข้ามทุกโมดูลบน data model เดียว รวม anomaly detection และ ML forecasting ในตัว (ดู TOR-TECH-03 / GP-TECH-04 สำหรับข้อความบังคับเต็ม)

**TOR wording (English):** The solution must embed AI/GenAI across all modules on a single data model, including native anomaly detection and ML forecasting (see TOR-TECH-03 / GP-TECH-04 for the full clause).

**iCE caveat:** AI/GenAI ฝังในชุดแอปเป็น "nice to have" ไม่ใช่ตัวตัดสิน และทั้งสองค่ายพัฒนาเร็วทุกไตรมาส — การล็อกสเปกวันนี้เสี่ยงเลือกจาก roadmap มากกว่าของจริง. NetSuite ก็เพิ่ม AI ต่อเนื่อง (Text Enhance, Bill Capture, anomaly ใน Analytics Warehouse) จุดต่างเหลือเรื่องความกว้าง/วุฒิภาวะ + ต้นทุน EPM add-on.

**Confidence:** low

**หลักฐาน / Citation:** ไม่มี KB/web citation ในระเบียนนี้ (standout summary) — citation อยู่ใน GP-TECH-04, NF-ANL-02, TOR-TECH-03.

---

## GP-STANDOUT-04 — Fusion standout: One unified cloud on a single data model

**Capability (TH):** ชุดคลาวด์เดียว data model เดียว
**Capability (EN):** One unified cloud on a single data model
**Domain:** Technical · **iCE severity:** แทบไม่มีผล · *(Type: Technical · Rank 4)*

**Oracle Fusion advantage (Standout):** Fusion (ERP+SCM+HCM+EPM+CX) ออกแบบเป็นชุดเดียวตั้งแต่ต้น — ลด integration ภายในเทียบ landscape ผสมของ SAP (Ariba/SuccessFactors/Concur ที่ซื้อมา).

**TOR wording to weaponize (ภาษาไทย):** ระบบต้องเป็นชุดคลาวด์เดียวบน data model เดียว (unified suite) ครอบคลุม ERP/SCM/HCM/EPM ลด integration ภายในระหว่างโมดูล

**TOR wording (English):** The solution must be one unified cloud suite on a single data model covering ERP/SCM/HCM/EPM, minimizing internal cross-module integration.

**iCE caveat:** ข้อนี้ย้อนแย้ง — "ชุดคลาวด์เดียว data model เดียว" คือจุดแข็งดั้งเดิมของ NetSuite (born-in-cloud, unified suite) เองตั้งแต่ต้น. NetSuite ตอบเกณฑ์ unified data model ได้เต็มเช่นเดียวกับ Fusion — การยกเป็นข้อได้เปรียบเฉพาะ Fusion จึงไม่สร้างความต่าง และไม่ใช่ช่องว่างที่แท้จริง. หลีกเลี่ยงการใช้ข้อนี้ weaponize (มันย้อนเข้าตัว). จุดอ่อนที่แท้คือ "ความกว้าง/ลึกของโมดูล" ซึ่งประเมินแยกในข้ออื่น.

**Confidence:** low

**หลักฐาน / Citation:** ไม่มี KB/web citation ในระเบียนนี้ (standout summary; iCE ระบุว่าเป็นข้อย้อนแย้ง).

---

## GP-STANDOUT-05 — Fusion standout: Embedded analytics + Autonomous Data Warehouse

**Capability (TH):** Analytics + Autonomous Data Warehouse
**Capability (EN):** Embedded analytics + Autonomous Data Warehouse
**Domain:** Technical · **iCE severity:** ต่ำ · *(Type: Technical · Rank 5)*

**Oracle Fusion advantage (Standout):** OAC + Autonomous DW (self-driving, self-securing) ให้ analytics ระดับองค์กรในตัว ลดงาน DBA.

**TOR wording to weaponize (ภาษาไทย):** ระบบต้องมี embedded analytics + enterprise data warehouse ที่บริหารจัดการตนเอง (autonomous, self-tuning/securing) ในตระกูลเดียวกัน (ดู TOR-TECH-02 / NF-ANL-01)

**TOR wording (English):** The solution must provide embedded analytics + a self-managing (autonomous) enterprise data warehouse in the same product family (see TOR-TECH-02 / NF-ANL-01).

**iCE caveat:** NSAW ของ NetSuite สร้างบน Oracle Autonomous Data Warehouse เดียวกัน ให้ self-service analytics + prebuilt content — ความต้องการ BI ขององค์กรสาธารณกุศลไม่ถึงระดับที่ต้องตั้งสเปก enterprise warehouse แยก. เกณฑ์นี้เทียบ add-on ของทั้งสองค่าย (NSAW = OAC+ADW) → ไม่สร้างความต่างที่ตัดสิน.

**Confidence:** low

**หลักฐาน / Citation:** ไม่มี KB/web citation ในระเบียนนี้ (standout summary) — citation อยู่ใน NF-ANL-01, GP-TECH-05, TOR-TECH-02.

---

## GP-STANDOUT-08 — Fusion standout: Autonomous Database foundation

**Capability (TH):** Autonomous Database ใต้ระบบ
**Capability (EN):** Autonomous Database foundation
**Domain:** Technical · **iCE severity:** แทบไม่มีผล · *(Type: Non-Functional · Rank 8)*

**Oracle Fusion advantage (Standout):** Oracle Autonomous DB จูน/แพตช์/กันภัยอัตโนมัติ ลด TCO ด้าน infra/DBA — เป็นเกณฑ์ที่ TOR ด้าน NFR ให้คะแนนได้.

**TOR wording to weaponize (ภาษาไทย):** ระบบต้องวางอยู่บนฐานข้อมูลที่บริหารจัดการตนเอง (auto-tuning/patching/scaling/securing) เพื่อลดภาระ DBA และ TCO ด้านโครงสร้างพื้นฐาน (ดู TOR-TECH-08)

**TOR wording (English):** The solution must run on a self-managing database (auto-tuning/patching/scaling/securing) to reduce DBA effort and infrastructure TCO (see TOR-TECH-08).

**iCE caveat:** Autonomous Database เป็นข้อได้เปรียบ infra/TCO ของ Oracle จริง แต่ "มองไม่เห็น" จากมุมผู้ใช้ปลายทาง — และล้าสมัยในฐานะ differentiator: NetSuite ย้ายไปรันบน Oracle Autonomous Database เดียวกัน (ประกาศ ก.พ. 2025) และเป็น SaaS ที่ Oracle ดูแล infra ให้ทั้งหมดอยู่แล้ว (ผู้ใช้ไม่ต้องมี DBA). ตั้งเป็น NFR ได้แต่ไม่กระทบงานจริง — ระวังย้อนเข้าตัว.

**Confidence:** low

**หลักฐาน / Citation:** ไม่มี KB/web citation ในระเบียนนี้ (standout summary) — citation ยืนยัน (NetSuite บน Autonomous DB) อยู่ใน TOR-TECH-08.

---

## GP-STANDOUT-09 — Fusion standout: Broad public + sovereign cloud regions

**Capability (TH):** region/sovereign cloud หลากหลาย
**Capability (EN):** Broad public + sovereign cloud regions
**Domain:** Technical · **iCE severity:** สูง · *(Type: Non-Functional · Rank 9)*

**Oracle Fusion advantage (Standout):** OCI มี public+government+sovereign regions มากสุด เหมาะ TOR ภาครัฐ/ข้อมูลในประเทศ — เป็นข้อได้เปรียบ Fusion/OCI ที่ legitimate เมื่อมีข้อกำหนด data residency ในไทย (ข้อมูลสุขภาพ/ผู้บริจาคโลหิต).

**TOR wording to weaponize (ภาษาไทย):** ผู้เสนอราคาต้องรองรับ public + government + sovereign cloud regions หลากหลาย พร้อมเส้นทาง in-country/sovereign สำหรับข้อมูลอ่อนไหว (ดู TOR-TECH-04 / GP-TECH-08 / NF-ARC-02)

**TOR wording (English):** The bidder must support broad public + government + sovereign cloud regions, with an in-country/sovereign path for sensitive data (see TOR-TECH-04 / GP-TECH-08 / NF-ARC-02).

**iCE caveat:** ตัวเลือก data center ของ NetSuite จำกัดและไม่มี government/sovereign region ในไทย ต่างจาก OCI — ข้อได้เปรียบ legitimate. แต่ถ่วงดุล: Oracle Fusion SaaS แบบ public มาตรฐานก็ไม่มี region ในไทยเช่นกัน (ข้อได้เปรียบคือ "เส้นทาง" Alloy/AIS/EU Sovereign) และ PDPA ไทยไม่บังคับ data localization. แนะนำ verify ตัวเลือก data center ในประเทศของทั้งสองค่ายก่อนตัดสิน — ไม่ใช่ปัดทิ้ง และไม่ใช่บังคับเป็น blocker โดยไม่ตรวจ. [ต้อง verify]

**Confidence:** low

**หลักฐาน / Citation:** ไม่มี KB/web citation ในระเบียนนี้ (standout summary) — citation รองรับ (Alloy/AIS, EU Sovereign, no Thai DC) อยู่ใน GP-TECH-08, NF-ARC-02, TOR-TECH-04.

---

## GP-STANDOUT-10 — Fusion standout: Continuous quarterly innovation, low-disruption

**Capability (TH):** นวัตกรรมต่อเนื่องไม่ disrupt
**Capability (EN):** Continuous quarterly innovation, low-disruption
**Domain:** Technical · **iCE severity:** ต่ำ · *(Type: Non-Functional · Rank 10)*

**Oracle Fusion advantage (Standout):** Fusion ปล่อยฟีเจอร์รายไตรมาสแบบ opt-in ไม่ rip-and-replace — granularity ละเอียดกว่ารอบ 2 ครั้ง/ปีของ NetSuite; ลดความเสี่ยงและต้นทุนวงจรชีวิต.

**TOR wording to weaponize (ภาษาไทย):** ระบบต้องปล่อยนวัตกรรมต่อเนื่องแบบ opt-in granularity ละเอียด (เช่น รายไตรมาส) โดยไม่ rip-and-replace

**TOR wording (English):** The solution must deliver continuous innovation with fine-grained opt-in cadence (e.g., quarterly) without rip-and-replace.

**iCE caveat:** ข้ออ้างอ่อน — NetSuite ก็เป็นคลาวด์ปล่อย 2 release/ปีแบบ opt-in + SuiteApp ecosystem; ทั้งคู่เป็น continuous cloud. การยกเป็นจุดเด่นเฉพาะ Fusion ไม่สมเหตุผล. ภาระจริงเหลือเพียง regression test ตามรอบปีละ 2 ครั้ง (บริหารจัดการได้) — ใช้ weaponize ข้อนี้ได้เพียงเรื่อง cadence granularity ไม่ใช่ "NetSuite disrupt".

**Confidence:** low

**หลักฐาน / Citation:** ไม่มี KB/web citation ในระเบียนนี้ (standout summary) — citation รอบ upgrade อยู่ใน GP-TECH-13.

---

## TOR-FIN-01 — TOR: Enterprise planning & budgeting (xP&A) on ERP platform

**Capability (TH):** เครื่องมือวางแผนงบประมาณและพยากรณ์ระดับองค์กร (xP&A) บนแพลตฟอร์มเดียวกับ ERP
**Capability (EN):** Enterprise Planning & Budgeting (xP&A) on the ERP platform
**Domain:** EPM · **iCE severity:** ต่ำ · *(Priority: Mandatory · NetSuite: Partial)*

**Oracle Fusion advantage (Standout):** Oracle EPM Cloud = leader; ทำ driver-based, multi-scenario, rolling forecast และ workforce/capital planning สำเร็จรูปบนแพลตฟอร์มเดียวกับ ERP. SAP ต้องใช้ SAC/BPC แยก.

**TOR wording to weaponize (ภาษาไทย):** ระบบต้องมีเครื่องมือวางแผนงบประมาณและพยากรณ์ระดับองค์กร (Enterprise Planning & Budgeting / xP&A) บนแพลตฟอร์มเดียวกับ ERP รองรับ driver-based planning, การจำลองหลายสถานการณ์ (multi-scenario), rolling forecast และการวางแผนกำลังคน/งบลงทุนในตัว

**TOR wording (English):** The solution shall provide a native Enterprise Planning & Budgeting (xP&A) capability on the same platform as the ERP, supporting driver-based planning, multi-scenario modeling, rolling forecasts, and built-in workforce & capital planning.

**iCE caveat:** เรต Partial สมเหตุผลเฉพาะส่วน "workforce & capital planning สำเร็จรูปในตัว" (Oracle Help ระบุ NSPB มีเฉพาะโมดูล Financials ยังไม่มี Workforce module) และ NSPB เป็นแอป/ลิขสิทธิ์แยกจาก ERP — ไม่ใช่เพราะขาด core. NSPB ตอบ driver-based/multi-scenario/rolling/predictive ได้บนเอนจิน Oracle EPM เดียวกัน. การบังคับ "โมดูล workforce/capital สำเร็จรูป + predictive multi-scenario ระดับ enterprise" = over-spec/ล็อกสเปกเอียงไป Oracle — วาง headcount/capex ผ่าน driver-based ใน NSPB Financials ได้.

**Confidence:** high

**หลักฐาน / Citation:**
- [WEB:docs.oracle.com] NetSuite Planning and Budgeting — 'supports only the Financials module. A Workforce module is not currently available.' (article_8124016549 — ตรวจแล้วมีจริง)
- [WEB:docs.oracle.com] NetSuite Planning and Budgeting Financials Overview — driver-based/trend-based/direct-input, what-if, Predictive Planning (article_7160253896 — ตรวจแล้วมีจริง)
- [WEB:netsuite.com] What is NetSuite Planning and Budgeting — produce scenario plans, multiple what-if, driver-based (financial-planning.shtml)
- [KB] Netsuite-Sales Force Automation (~0.6) — base NetSuite มีเพียง sales forecasting/GL budget; xP&A เต็มต้องใช้ NSPB add-on

---

## TOR-FIN-03 — TOR: Statutory tax / e-invoicing (e-Tax Invoice TH)

**Capability (TH):** localization และ statutory/tax compliance ในตัวสำหรับทุกประเทศ รวม e-invoicing/e-tax
**Capability (EN):** Built-in localization & statutory/tax compliance for every country, incl. e-invoicing/e-tax
**Domain:** Finance · **iCE severity:** สูง · *(Priority: Mandatory · NetSuite: No)*

**Oracle Fusion advantage (Standout):** SuiteTax ครอบคลุมประเทศน้อยกว่า; SAP/Oracle ครอบคลุม localization + e-invoice กว้างสุด. Fusion ตอบ "ทุกประเทศ + e-tax native" ได้กว้างกว่า.

**TOR wording to weaponize (ภาษาไทย):** ระบบต้องมี localization และ statutory/tax compliance ในตัวสำหรับทุกประเทศที่องค์กรดำเนินงาน รวมถึง e-invoicing/e-tax ตามข้อกำหนดของแต่ละประเทศ โดยไม่ต้องพึ่ง third-party add-on

**TOR wording (English):** The solution shall provide built-in localization and statutory/tax compliance for every country of operation, including country-specific e-invoicing/e-tax, without reliance on third-party add-ons.

**iCE caveat:** การตอบ "No" เกินจริงสำหรับ scope ไทย — NetSuite รองรับ statutory ไทยผ่าน SEA Localization + International Tax Reports (free managed bundle ของ NetSuite เอง ไม่ใช่ third-party) ครอบ VAT/ภ.พ.30 + ใบกำกับภาษี/เครดิตโน้ตตามกรมสรรพากร. จุดอ่อนจริงและ legitimate เหลือเฉพาะ e-Tax Invoice/e-Receipt แบบ XML ส่งกรมสรรพากร (Electronic Invoicing เป็นกรอบเปล่า ต้อง custom/partner) — เป็นข้อบังคับกฎหมายไทย ต้องปิด gap ก่อน go-live. เงื่อนไข "ทุกประเทศ + โดยไม่พึ่ง add-on" คือการล็อกสเปก (องค์กรอยู่ไทยประเทศเดียว และ SuiteApp ที่ใช้เป็นของ NetSuite เอง) → ความจริงคือ Partial ไม่ใช่ No.

**Confidence:** high

**หลักฐาน / Citation:**
- [WEB:docs.oracle.com] Southeast Asia Localization (free managed first-party bundle)
- [WEB:docs.oracle.com] Thailand Invoicing Features / Electronic Invoicing Overview (กรอบ ไม่มี native ไทย)
- [KB] Netsuite-Country Specific Features (0.7209)

---

## TOR-TECH-01 — TOR: Tier-1 scalability / transaction throughput

**Capability (TH):** รองรับปริมาณธุรกรรม/ผู้ใช้พร้อมกันสูงระดับองค์กร โดยไม่มี governance limit
**Capability (EN):** Enterprise-scale transaction volume/concurrency without governance limits
**Domain:** Technical · **iCE severity:** แทบไม่มีผล · *(Priority: Mandatory · NetSuite: Partial)*

**Oracle Fusion advantage (Standout):** SAP/Oracle สเกลกว่าในปริมาณธุรกรรม/concurrency ระดับ tier-1 โดยไม่ติด SuiteScript governance + search row caps.

**TOR wording to weaponize (ภาษาไทย):** ระบบต้องรองรับปริมาณธุรกรรมและผู้ใช้พร้อมกันสูงระดับองค์กร โดยไม่มีเพดานจำกัด (governance limit) ที่กระทบ batch posting, integration หรือ reporting ปริมาณมาก พร้อมระบุตัวเลข throughput/concurrency ที่การันตี

**TOR wording (English):** The solution shall support enterprise-scale transaction volumes and concurrent users without governance limits that constrain bulk posting, integration, or high-volume reporting, and shall state guaranteed throughput/concurrency figures.

**iCE caveat:** NetSuite มี governance/concurrency cap และ search page size สูงสุด 1,000 จริง และไม่ออกการันตี throughput เป็นตัวเลข SLA — แต่รองรับงานปริมาณมากด้วย Map/Reduce (processor queue แยก ไม่นับรวม web-services concurrency), SuiteCloud Plus (+10 ต่อ license) และ CSV import. "Partial = สเกลไม่ได้" เกินจริง; ปริมาณธุรกรรมระดับองค์กรกลางไม่ถึง tier-1 (ล้านรายการ/วัน) → ข้อกำหนด "ไม่มี cap + การันตี throughput" เป็น over-spec ที่ไม่ผูกมัดงานจริง.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-SuiteTalk SOAP Web Services Platform Guide (0.718) — แต่ละ SuiteCloud Plus license เพิ่ม concurrent web services +10
- [KB] NSTWP (0.516) — pageSize preference (search page size, สูงสุด 1,000)
- [WEB:docs.oracle.com] Concurrency Governance Limits Based on Service Tiers and SuiteCloud Plus Licenses
- [WEB:houseblend.io] NetSuite Map/Reduce Guide — processor pool แยก ไม่นับ API concurrency, chunk งานปริมาณมากได้ [ต้อง verify]

---

## TOR-TECH-02 — TOR: Enterprise analytics / in-memory BI

**Capability (TH):** การวิเคราะห์เรียลไทม์ฝังในตัว + self-service BI + enterprise DW ที่บริหารจัดการเอง
**Capability (EN):** Embedded real-time analytics + self-service BI + self-managing enterprise DW
**Domain:** Technical · **iCE severity:** ต่ำ · *(Priority: Important · NetSuite: Partial)*

**Oracle Fusion advantage (Standout):** SAP HANA in-memory เด่น real-time; Oracle OAC + Autonomous DW เด่นด้าน self-managing enterprise data warehouse.

**TOR wording to weaponize (ภาษาไทย):** ระบบต้องมีการวิเคราะห์ข้อมูลแบบเรียลไทม์ฝังในตัว (embedded real-time analytics) บนข้อมูลธุรกรรมสด พร้อม self-service BI และ data warehouse ระดับองค์กรที่บริหารจัดการเอง

**TOR wording (English):** The solution shall provide embedded real-time analytics on live transactional data, with self-service BI and a self-managing enterprise data warehouse.

**iCE caveat:** 2 ใน 3 ข้อ (real-time analytics บนธุรกรรมสด + self-service BI) เป็นจุดแข็ง native ของ NetSuite (SuiteAnalytics Workbook/Saved Search/Dashboard); ข้อ "self-managing enterprise DW" ตอบด้วย NSAW บน Oracle Autonomous Database (auto-tune/patch/scale) แต่เป็น add-on เสียเงินแยก. Partial เกิดจากผูกข้อกำหนด DW พรีเมียมเข้ามา ทั้งที่ Oracle ก็ต้องใช้ OAC/ADW แยกเช่นกัน — enterprise DW จัดการตนเองเป็น over-spec ที่แทบไม่มี use case.

**Confidence:** high

**หลักฐาน / Citation:**
- [WEB:netsuite.com] SuiteAnalytics — built-in real-time, no warehouse needed
- [WEB:houseblend.io] NSAW on Oracle Autonomous Data Warehouse (self-managing)
- [KB] Netsuite-SuiteAnalytics Workbook (0.63)

---

## TOR-TECH-03 — TOR: Embedded AI / GenAI across processes

**Capability (TH):** AI/GenAI ฝังในกระบวนการธุรกิจหลัก (assistant, anomaly, forecasting, document IDR)
**Capability (EN):** AI/GenAI embedded across core processes
**Domain:** Technical · **iCE severity:** ต่ำ · *(Priority: Important · NetSuite: No)*

**Oracle Fusion advantage (Standout):** Oracle ฝัง AI กว้างทั่ว Fusion (intelligent assistant, anomaly detection, forecasting, document IDR) บน data model เดียว; SAP Joule ตามมา.

**TOR wording to weaponize (ภาษาไทย):** ระบบต้องมีความสามารถ AI/GenAI ฝังในกระบวนการธุรกิจหลัก (เช่น ผู้ช่วยอัจฉริยะ, anomaly detection, การพยากรณ์, document IDR) โดยไม่ต้องต่อระบบภายนอก

**TOR wording (English):** The solution shall embed AI/GenAI within core business processes (e.g., intelligent assistants, anomaly detection, forecasting, document IDR) without external bolt-ons.

**iCE caveat:** เรต "No/ทำไม่ได้เลย" แรงเกินจริง — 2 ใน 4 ความสามารถมี native จริง: intelligent assistant (SuiteAnalytics Assistant + Text Enhance, 2024.1–2025.1) และ document IDR (Bill Capture/Document AI). ที่ต้องซื้อแยกคือ anomaly detection + forecasting (Intelligent Performance Management ในโมดูล EPM, ~$10k–25k/ปี). ช่องว่างกับ Oracle เป็นเรื่องความกว้าง/วุฒิภาวะ + ต้นทุน add-on ไม่ใช่ "ไม่มี" → ความจริงใกล้ Partial. Document IDR ช่วยงาน AP/จัดซื้อ/รับบริจาคได้ทันที.

**Confidence:** high

**หลักฐาน / Citation:**
- [WEB:netsuite.com] NetSuite 2024.1 — Text Enhance, Bill Capture
- [WEB:netsuite.com] GenAI assistant 2025.1 (SuiteAnalytics Assistant)
- [WEB:netsuite.com] NetSuite EPM — Intelligent Performance Management (add-on)
- [WEB:docs.oracle.com] NetSuite Features That Use AI

---

## TOR-TECH-04 — TOR: Deployment / data residency options

**Capability (TH):** ระบุทางเลือกการติดตั้ง (public/private/sovereign) + ตำแหน่ง data center
**Capability (EN):** State deployment options (public/private/sovereign) + data-center locations
**Domain:** Technical · **iCE severity:** สูง · *(Priority: Mandatory · NetSuite: Partial)*

**Oracle Fusion advantage (Standout):** NetSuite = public multi-tenant, region จำกัด → Partial; Oracle OCI sovereign/gov regions เด่น; SAP private ผ่าน RISE. Fusion/OCI ตอบเส้นทาง in-country/sovereign ที่ NetSuite ไม่มี.

**TOR wording to weaponize (ภาษาไทย):** ผู้เสนอราคาต้องระบุทางเลือกการติดตั้ง (public cloud, private cloud, sovereign/in-country region) และตำแหน่ง data center ที่รองรับข้อกำหนดถิ่นที่อยู่ของข้อมูล (data residency) ของหน่วยงาน

**TOR wording (English):** The bidder shall state available deployment options (public, private, sovereign/in-country region) and data-center locations meeting the organization's data-residency requirements.

**iCE caveat:** จุดอ่อน NetSuite จริงและปิดไม่ได้เชิงสถาปัตยกรรม (public multi-tenant SaaS เท่านั้น, ไม่มี DC ในไทย/private/sovereign, ไม่อยู่บน EU Sovereign Cloud) — ต่างจาก gap อื่นในชุดนี้ที่ปิดด้วย SuiteApp. Oracle มีเส้นทาง in-country (Alloy/AIS) ที่ NetSuite ยังไม่มี. ถ่วงดุล: TOR ขอเพียง "ระบุทางเลือก" ซึ่ง NetSuite ตอบได้, Fusion SaaS public มาตรฐานก็ไม่มี region ในไทย, และ PDPA ไม่บังคับ localization. สำหรับข้อมูลสุขภาพ/ผู้บริจาคของ blood-bank/รพ. sovereignty มีน้ำหนักจริง — เคลียร์ประเด็นก่อน go-live แต่กรอบเป็น "ระบุทางเลือก + verify" ไม่ใช่บังคับ in-country เพื่อลดข้อครหาล็อกสเปก. [ต้อง verify in-country/sovereign roadmap]

**Confidence:** medium

**หลักฐาน / Citation:**
- [WEB:netsuite.com] NetSuite Data Center datasheet — multi-region, no Thai DC
- [WEB:sota.io] NetSuite not on Oracle EU Sovereign Cloud (Q1 2026) [ต้อง verify]
- [WEB:oracle.com] Public Cloud Regions; AIS Cloud/Oracle Alloy Thailand
- [WEB:securiti.ai] Thailand PDPA — no localization mandate

---

## TOR-TECH-05 — TOR: GRC / automated SoD controls

**Capability (TH):** ควบคุมสิทธิ์ละเอียด + automated SoD + continuous controls monitoring ในตัว
**Capability (EN):** Fine-grained access + automated SoD + built-in continuous controls monitoring
**Domain:** Technical · **iCE severity:** สูง · *(Priority: Important · NetSuite: Partial)*

**Oracle Fusion advantage (Standout):** Oracle Risk Mgmt Cloud & SAP GRC มี automated SoD + continuous controls monitoring (preventive) ในตัว ที่ NetSuite ไม่มี native.

**TOR wording to weaponize (ภาษาไทย):** ระบบต้องมีการควบคุมสิทธิ์การเข้าถึงแบบละเอียด พร้อมการตรวจสอบการแบ่งแยกหน้าที่ (Segregation of Duties) อัตโนมัติ และ continuous controls monitoring ในตัว

**TOR wording (English):** The solution shall provide fine-grained access control with automated Segregation of Duties (SoD) checks and built-in continuous controls monitoring.

**iCE caveat:** ช่องว่าง native จริงคือ "continuous controls monitoring ในตัว" + automated SoD เชิง preventive (block self-approval แบบ ruleset) — Oracle/SAP เหนือกว่า. แต่ NetSuite ทำ fine-grained access control ได้ในตัว และทำ SoD แบบ detective ได้ (saved search/role audit ตรวจ creator=approver). SoD เกี่ยวข้องสูงเพราะอยู่ใต้การตรวจ สตง. โดยตรง — ต้องจัดหา certified SuiteApp (Fastpath Assure/Netwrix Strongpoint/Greenlight Approvals) ปิด preventive + ออกแบบ control matrix ก่อน go-live. CCM แบบ native เต็มรูปเป็น over-spec สำหรับ NGO ไทย; การบังคับ "ในตัว" = ล็อกสเปก.

**Confidence:** high

**หลักฐาน / Citation:**
- [WEB:mysuite.tech] NetSuite SoD: detective vs preventive (native ไม่ block self-approval แบบ ruleset)
- [WEB:oracle.com] Oracle Risk Management Cloud — built-in continuous controls monitoring
- [WEB:suiteapp.com] Greenlight Approvals / Fastpath Assure — preventive self-approval blocking + automated SoD
- [KB] Netsuite-Managing Users & Roles (0.6544) — access review/audit guidance (manual)

---

## TOR-TECH-06 — TOR: Native iPaaS / integration platform

**Capability (TH):** แพลตฟอร์มเชื่อมต่อ (iPaaS) ในตัว + API management + event-driven + throughput ไม่ติดเพดาน API
**Capability (EN):** Native iPaaS + API management + event-driven + throughput without API limits
**Domain:** Technical · **iCE severity:** ต่ำ · *(Priority: Important · NetSuite: Partial)*

**Oracle Fusion advantage (Standout):** Oracle OIC & SAP Integration Suite เป็น iPaaS เต็มรูป (prebuilt adapters, API management, event-driven orchestration) ในตระกูลเดียวกัน.

**TOR wording to weaponize (ภาษาไทย):** ระบบต้องมาพร้อมแพลตฟอร์มเชื่อมต่อ (iPaaS) ในตัว รองรับ pre-built adapters, API management, event-driven integration และ throughput ระดับองค์กรโดยไม่ติดเพดาน API

**TOR wording (English):** The solution shall include a native iPaaS supporting pre-built adapters, API management, event-driven integration, and enterprise throughput without restrictive API limits.

**iCE caveat:** NetSuite ให้ REST/SOAP/RESTlets + SuiteScript + event hooks (User Event/Scheduled/Map-Reduce) ทำ event-driven integration ได้ และมี pre-built connectors ผ่าน SuiteApp แต่ไม่มี iPaaS + API management รวมในแพ็กเกจเดียว และมี concurrency governance. ข้อกำหนดที่มัด "iPaaS ในตัว + ไม่มีเพดาน API" ถูกออกแบบให้ NetSuite ตอบได้แค่ Partial — แต่ Oracle OIC ก็เป็นไลเซนส์แยกคิดตาม message ไม่ฟรีในตัว ERP → over-spec/ล็อกสเปก. งาน integration จริง (HIS/ธนาคารเลือด/ธนาคาร) ใช้ API ในตัวได้ตามสเกล.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-SuiteCloud Platform Introduction (0.647)
- [KB] Netsuite-SuiteTalk REST Web Services (0.685)
- [WEB:erpresearch.com] OIC เป็นไลเซนส์แยกจาก Fusion ERP คิดตาม message (ยืนยันมีจริง)
- [WEB:docs.oracle.com] NetSuite Help — Concurrency Governance Limits

---

## TOR-TECH-07 — TOR: Native master data management (MDM)

**Capability (TH):** MDM + data governance ในตัว รองรับ data stewardship, data-quality, federation ข้ามโดเมน
**Capability (EN):** Native MDM + data governance with stewardship, data-quality, cross-domain federation
**Domain:** Technical · **iCE severity:** แทบไม่มีผล · *(Priority: Important · NetSuite: No)*

**Oracle Fusion advantage (Standout):** NetSuite ไม่มี MDM แท้ → No; SAP MDG มีในตัว, Oracle governance ผ่าน hub. Fusion ตอบ cross-domain federation ได้กว้างกว่า.

**TOR wording to weaponize (ภาษาไทย):** ระบบต้องมีการบริหารข้อมูลหลัก (Master Data Management) และ data governance ในตัว รองรับ data stewardship, การควบคุมคุณภาพข้อมูล และ federation ข้ามโดเมน

**TOR wording (English):** The solution shall provide native Master Data Management and data governance, supporting data stewardship, data-quality controls, and cross-domain federation.

**iCE caveat:** การตี "No (ทำไม่ได้เลย)" เกินจริง — NetSuite ทำ data stewardship/data-quality ระดับใช้งานได้ (Duplicate Detection, Record Merge/EntityDeduplicationTask, audit trail, role/field-level security) เพียงไม่มี cross-domain federation MDM hub. federation ข้ามโดเมนเป็นความต้องการของ enterprise หลายระบบ และ Oracle เองก็ทำผ่าน Product/Customer Hub โมดูลแยก ไม่ใช่ in-the-box → ข้อกำหนดนี้ล็อกสเปก. องค์กรที่ใช้ ERP เดียวไม่มี use case federation.

**Confidence:** medium

**หลักฐาน / Citation:**
- [KB] NetSuite Basics — Duplicate Record Detection (0.65)
- [KB] Netsuite-SuiteScript 2.0 API Reference — EntityDeduplicationTask (0.682)
- [WEB:oracle.com] Oracle MDM = Customer/Product/Supplier Hub (โมดูลแยก)
- [WEB:netsuite.com] Governance, Risk & Compliance — audit trail/field-level security (รวมใน platform license, ยืนยันแล้ว)

---

## TOR-TECH-08 — TOR: Architecture / infrastructure foundation

**Capability (TH):** สถาปัตยกรรมฐานข้อมูล + การดูแลอัตโนมัติ (auto-tuning/patching/scaling/security) ลด DBA/TCO
**Capability (EN):** Database architecture + autonomous operations (auto-tuning/patching/scaling/security)
**Domain:** Technical · **iCE severity:** แทบไม่มีผล · *(Priority: Optional · NetSuite: Partial)*

**Oracle Fusion advantage (Standout):** Oracle Autonomous Database เป็นจุดเด่นเฉพาะ (self-tuning/patching/scaling/securing); SAP HANA ต้องจูน. TOR อาจตั้งเป็น NFR ให้คะแนน.

**TOR wording to weaponize (ภาษาไทย):** ผู้เสนอราคาต้องอธิบายสถาปัตยกรรมฐานข้อมูลและการดูแลอัตโนมัติ (auto-tuning, auto-patching, auto-scaling, auto-security) ที่ช่วยลดภาระงาน DBA และ TCO ด้านโครงสร้างพื้นฐาน

**TOR wording (English):** The bidder shall describe the database architecture and autonomous operations (auto-tuning, auto-patching, auto-scaling, auto-security) that reduce DBA effort and infrastructure TCO.

**iCE caveat:** จุดอ่อนแทบไม่มี และ differentiator ล้าสมัย — NetSuite ย้ายไปรันบน Oracle Autonomous Database เดียวกัน (ประกาศ SuiteConnect ก.พ. 2025) จึงได้ auto-tuning/zero-downtime patching/auto-scaling/auto-security ในตัว และในฐานะ SaaS เต็มรูปลูกค้าไม่ต้องมี DBA. ข้อกำหนดนี้ priority Optional ยิ่งไม่ใช่ตัวตัดสิน — การอ้าง "Autonomous DB เป็นของ Oracle เจ้าเดียว / NetSuite เป็น black-box" ย้อนเข้าตัวได้ ระวังใช้ weaponize.

**Confidence:** high

**หลักฐาน / Citation:**
- [WEB:prnewswire.com] NetSuite Migrates to Oracle Autonomous Database (Feb 2025)
- [WEB:accountingtoday.com] NetSuite migrates suite to AI self-maintaining database
- [WEB:oracle.com] Autonomous Database features (auto-tune/patch/scale/secure)

---

## Cross-cutting weaponization playbook (iCE selling Fusion)

Ranked by how defensibly a spec pushes a NetSuite bid to Partial/No **without** creating สตง. procurement-fairness exposure:

1. **Strongest & legitimate (architectural gaps NetSuite cannot close with a SuiteApp)** — NF-ARC-02 / GP-TECH-08 / TOR-TECH-04 (in-country / sovereign data residency for health & donor data) and GP-TECH-07 (private/on-prem). Fusion/OCI genuinely wins; frame as "state your in-country/sovereign path" and require verification, not as a bare Cloud@Customer mandate. iCE severity สูง.
2. **Strong on genuine native gaps (closeable only by paid add-on)** — NF-SEC-01 / GP-FUNC-27 / GP-TECH-11 / TOR-TECH-05 (automated + preventive SoD / continuous controls monitoring), GP-FUNC-16 / TOR-FIN-03 (Thai e-Tax Invoice XML). Fusion has it natively; NetSuite needs a certified SuiteApp or custom. Legitimate under สตง. audit context — but avoid "without any add-on" wording, which locks the spec.
3. **Use with caution (over-spec / not-applicable for a single-country non-profit)** — EPM breadth (F-EPM-01/03, GP-FUNC-13, TOR-FIN-01, GP-STANDOUT-01), consolidation at scale (F-EPM-02, GP-FUNC-12), multi-country localization breadth (F-FIN-02, GP-TECH-10), tier-1 throughput (NF-ARC-01, GP-TECH-02, TOR-TECH-01), in-memory BI / enterprise DW (NF-ANL-01, GP-TECH-01/05, TOR-TECH-02), native iPaaS (NF-INT-01, GP-TECH-06, TOR-TECH-06), MDM hub (NF-INT-02, GP-TECH-14, TOR-TECH-07). These score NetSuite Partial/No but the capability has little or no real use case here — mandating them reads as spec-locking.
4. **Weak / boomerang — do NOT weaponize** — GP-STANDOUT-04 (unified single data model: NetSuite's own historic strength), GP-STANDOUT-08 / TOR-TECH-08 (Autonomous DB: NetSuite now runs on the same Oracle Autonomous Database since Feb 2025), GP-STANDOUT-10 / GP-TECH-13 (continuous/quarterly innovation: Fusion actually forces quarterly upgrades; the real upgrade-control advantage belongs to SAP private), NF-ANL-02 / GP-TECH-04 / GP-STANDOUT-02 (embedded AI: gap is breadth/maturity + add-on cost, not absence). These claims rest on outdated or self-contradicting premises and hand a sharp NetSuite competitor an easy rebuttal.

**Standing rule (second_opinion.txt):** write requirements outcome-based against the organization's real mission, not bound to one product's specific feature. This is both more defensible against สตง./competitor challenge and harder for a NetSuite bid to rebut on fairness grounds. Every add-on gap cited above should be weighed on TCO — Oracle Fusion licenses NSPB-equivalents (EPBCS, ARCS, PCMCS, OAC+ADW, OIC, Risk Management Cloud, MDM Hub) as separate modules too.
