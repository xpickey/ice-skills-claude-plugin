# TOR Competitive KB — cross-cutting — NetSuite Weakness & Counter

---
last_verified: "2026-06-29"
source: "TOR Requirement Bank + Gap Pack v2"
confidence_note: "This KB is a DEFENSIVE / SELL-SIDE brief for iCE when positioning or defending Oracle NetSuite against a Fusion-biased TOR. The underlying source is a competitive TOR draft engineered so NetSuite scores Partial/No and Oracle Fusion scores Fully; it is NOT a neutral requirements analysis. Every record therefore carries BOTH the raw gap AND the balanced iCE counter (first-party add-on coverage, certified SuiteApp, custom, or over-spec/procurement-risk rebuttal). Confidence per record reflects whether an official KB/web citation exists in the source; records with no hard citation are marked medium/low. Product positions are mid-2026 and must be re-verified against a live environment / the vendor before commitment."
ams_review: "yearly — re-verify product positions"
---

> **How to use this file.** These are cross-cutting capabilities that recur in almost every enterprise TOR regardless of industry (EPM, consolidation, tax, HCM, platform, integration, analytics, AI, architecture, security/GRC). For every requirement the source biases toward Oracle Fusion, iCE holds a balanced counter-view: many "gaps" are (a) coverable by NetSuite first-party add-ons that run on the same Oracle engine — NSPB (= Oracle PBCS/Hyperion), NetSuite Account Reconciliation / NSAR (= Oracle Fusion EPM), NSAW (= Oracle ADW + Analytics Cloud), NSPCM (= Oracle PCMCS); or (b) coverable by certified SuiteApps / custom SuiteScript; or (c) genuine over-spec that a single-country, single-entity public-sector / non-profit / healthcare organisation has no use case for. Where a TOR locks a spec to one product's native feature, note the **procurement risk** — under สตง. (State Audit Office) scrutiny, spec-locking to a single vendor is legally challengeable and should be reframed as outcome-based.

> **แนวทางใช้ไฟล์นี้.** นี่คือความสามารถ "ข้ามอุตสาหกรรม" (cross-cutting) ที่ปรากฏในเกือบทุก TOR ระดับองค์กร ไม่ว่าอุตสาหกรรมใด (EPM, งบรวม, ภาษี, HCM, แพลตฟอร์ม, การเชื่อมต่อ, analytics, AI, สถาปัตยกรรม, ความปลอดภัย/GRC). ทุกข้อกำหนดในแหล่งข้อมูลเอียงเข้าหา Oracle Fusion — iCE ถือมุมมองถ่วงดุลว่าหลายช่องว่างเป็น (ก) ปิดได้ด้วย add-on first-party ของ NetSuite ที่รันบนเอนจิน Oracle เดียวกัน — NSPB (= Oracle PBCS/Hyperion), NetSuite Account Reconciliation / NSAR (= Oracle Fusion EPM), NSAW (= Oracle ADW + Analytics Cloud), NSPCM (= Oracle PCMCS); (ข) ปิดได้ด้วย SuiteApp certified / custom; หรือ (ค) เป็น over-spec ที่องค์กรประเทศเดียว/นิติบุคคลเดียว/ภาครัฐ-สาธารณกุศล ไม่มี use case จริง. กรณี TOR ล็อกสเปกเข้าฟีเจอร์ native ของผลิตภัณฑ์เดียว ให้ระบุ **ความเสี่ยงด้านจัดซื้อ** — ภายใต้การตรวจของ สตง. การล็อกสเปกเข้าผู้ขายรายเดียวถูกท้วงติงได้ ควรเขียนใหม่แบบอิงผลลัพธ์ (outcome-based).

---

## F-EPM-01 — Driver-based planning & budgeting (xP&A)

- **Capability (TH):** การวางแผน/งบประมาณแบบ driver-based
- **Capability (EN):** Driver-based planning & budgeting
- **Domain:** EPM · **iCE severity:** ต่ำ

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** ERP แกนของ NetSuite ไม่มี predictive/multi-scenario planning ในตัว. NSPB เป็น OEM ตัดทอนของ Oracle PBCS ที่เป็น add-on ลิขสิทธิ์แยก และปัจจุบันมีเฉพาะโมดูล Financials — ยังไม่มีโมดูล Workforce/Capital สำเร็จรูป (Oracle Help ระบุชัด "A Workforce module is not currently available"). Oracle EPM Cloud (EPBCS) มี planning ครบทุกมิติในตัว.

**Counter / Mitigation:** ข้อกล่าวอ้าง "ไม่มี predictive/scenario" ไม่จริง — NetSuite ทำ driver-based, what-if/multi-scenario, Predictive Planning และ rolling forecast ได้จริงผ่าน **NetSuite Planning and Budgeting (NSPB)** ซึ่งสร้างบนเอนจิน Oracle PBCS/Hyperion เดียวกับ Oracle EPM Cloud พร้อม sync GL อัตโนมัติ (first-party add-on). เหตุที่ควรได้แค่ Partial คือ NSPB เป็น add-on ลิขสิทธิ์แยกและยังไม่มีโมดูล Workforce/Capital สำเร็จรูป — ไม่ใช่เพราะ "ขาด predictive/scenario". สำหรับองค์กรที่มี headcount/capex จริง (โรงพยาบาล/ศูนย์บริการโลหิต/หน่วยผลิตชีววัตถุ) วาง headcount/capex ผ่าน driver-based ใน NSPB Financials ได้ ไม่จำเป็นต้องมีโมดูล Workforce/Capital สำเร็จรูป + predictive multi-scenario ระดับ enterprise ซึ่งเป็น over-spec.

**Procurement caveat:** การบังคับ "native driver-based + workforce/capital สำเร็จรูป + predictive โดยไม่ใช้เครื่องมือภายนอก" ลง TOR เอียงเข้าหา Oracle EPBCS โดยตรง — ควรเขียนเป็น outcome (วางงบ/พยากรณ์แบบ driver-based ได้) เพื่อลดความเสี่ยงถูกท้วง.

**Confidence:** high

**หลักฐาน / Citation:**
- [WEB:docs.oracle.com] NetSuite Planning and Budgeting — 'Planning and Budgeting currently supports only the Financials module. A Workforce module is not currently available.' (article_8124016549 — ตรวจแล้วมีจริง/ยังอัปเดต)
- [WEB:docs.oracle.com] NetSuite Planning and Budgeting Financials Overview — driver-based/trend-based/direct-input accounts, what-if scenarios, Predictive Planning (article_7160253896 — ตรวจแล้วมีจริง)
- [WEB:netsuite.com] What is NetSuite Planning and Budgeting — scenario plans / what-if / driver-based, built on Oracle EPM (financial-planning.shtml)
- [KB] Netsuite-Statistical Accounting / Netsuite-General Accounting (~0.6) — base NetSuite มีเพียง GL budget + statistical allocation; KB ไม่มีเอกสาร NSPB เฉพาะ บ่งชี้ว่า xP&A เต็มต้องใช้ add-on

---

## F-EPM-02 — Advanced financial consolidation (multi-tier ownership, equity method)

- **Capability (TH):** การรวมงบการเงิน (consolidation) ขั้นสูง
- **Capability (EN):** Advanced financial consolidation
- **Domain:** EPM · **iCE severity:** แทบไม่มีผล

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** OneWorld consolidation รองรับระดับ mid-market — ไม่ลงบัญชี/ปรับ NCI (ส่วนได้เสียที่ไม่มีอำนาจควบคุม) อัตโนมัติ และไม่รองรับ equity method / step acquisition / fair-value NCI ในตัว. Oracle FCCS รองรับโครงสร้างถือหุ้นหลายชั้น, equity pickup, statutory+management views.

**Counter / Mitigation:** NetSuite OneWorld ทำ consolidation หลายชั้น (multi-tier subsidiary hierarchy), ตัดรายการระหว่างกันอัตโนมัติ (Intercompany Auto Elimination) และแปลงค่าเงิน/CTA ได้ในตัว พร้อมฟิลด์ Ownership% — จึงไม่ใช่ทั้ง "ไม่มี ownership%" (ผิด) และไม่ใช่ "ครบในตัว" (เกิน). เคสถือหุ้นบางส่วน/JV/equity method ต้องใช้ SuiteApp (เช่น Eide Bailly NCI Module) หรือปรับมือ. ในกลุ่มข้ามชาติที่มี JV/บริษัทร่วมจำนวนมาก Oracle FCCS เหนือกว่าชัดเจน — แต่สำหรับนิติบุคคลเดียวในประเทศ ไม่มีโครงสร้างถือหุ้นหลายชั้นที่ต้องใช้ NCI/equity method → ความสามารถระดับ FCCS แทบไม่ได้ใช้.

**Procurement caveat:** บังคับ multi-tier ownership%/equity-method ลง TOR สำหรับองค์กรนิติบุคคลเดียว = over-spec/ล็อกสเปก.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-General Accounting (consolidation, 0.59) — Intercompany Auto Elimination + consolidated exchange rates
- [KB] Netsuite-NetSuite OneWorld Guide (consolidation, 0.60) — subsidiary เป็นนิติบุคคล/nexus/base currency
- [WEB:timdietrich.me] NetSuite Intercompany Transactions & Eliminations — multi-tier hierarchy, auto elimination, CTA, Ownership% พร้อมข้อจำกัด equity method/complex NCI
- [WEB:suiteapp.com] Eide Bailly NCI Module for Partially-Owned Subsidiaries — ยืนยันว่า NetSuite ไม่ลงบัญชี NCI ถือหุ้นบางส่วนอัตโนมัติ ต้องใช้ SuiteApp

---

## F-EPM-03 — Automated reconciliation & close orchestration

- **Capability (TH):** การกระทบยอดบัญชีอัตโนมัติ + close orchestration
- **Capability (EN):** Automated reconciliation & close
- **Domain:** EPM · **iCE severity:** กลาง

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** ฐาน ERP ของ NetSuite มีเพียง period-close checklist + bank reconciliation — ไม่มี transaction matching อัตโนมัติและ close orchestration ขั้นสูงในตัว. Oracle ARCS ทำ account reconciliation + transaction matching + close-task orchestration ในตัว.

**Counter / Mitigation:** ช่องว่างเดิมถูกปิดแล้วด้วย **NetSuite Account Reconciliation (NSAR)** ออกปี 2023 สร้างบน Oracle Fusion EPM — มี transaction matching engine จับคู่ได้ระดับล้านรายการ (สูงสุด ~5 ล้านแถว CSV), เทมเพลตกระทบยอดหลายประเภท (AP/AR/bank/prepaid/accrual/FA/intercompany), audit trail และ close management (first-party add-on ลิขสิทธิ์แยก). ถ้าไม่ซื้อ NSAR ก็เหลือแค่ period-close checklist + bank rec ตามที่ TOR อ้าง. สำหรับนิติบุคคลเดียว การกระทบยอด/ปิดงบเกี่ยวกับทุกหน่วยการเงิน จึงควรพิจารณางบ NSAR แต่ matching อัตโนมัติระดับล้านรายการเป็น nice-to-have เพราะปริมาณจริงไม่สูงถึงระดับนั้น.

**Procurement caveat:** ควรระบุว่าเป็นความสามารถ EPM ที่ทั้ง NetSuite (NSAR) และ Oracle (ARCS) ต่างคิดค่าโมดูลแยก — การตัด NetSuite ด้วยเกณฑ์ "native ในตัว" ไม่สมมาตร.

**Confidence:** high

**หลักฐาน / Citation:**
- [WEB:prnewswire.com] NetSuite Account Reconciliation announced 2023-06-14 — built on Oracle Fusion EPM, transaction matching engine + reconciliation/close management
- [WEB:oracle.com] NSAR What's New 2023 — transaction matching export สูงสุด 5,000,000 แถว CSV
- [KB] Netsuite-General Accounting (reconciliation_close, 0.62) — Period Close Checklist
- [KB] NETSUITE_FOR_CONSULTANTS (reconciliation_close, 0.63) — Period Close / period lockdown

---

## F-FIN-01 — Multi-GAAP / secondary ledgers

- **Capability (TH):** Multi-GAAP / secondary ledgers
- **Capability (EN):** Multi-GAAP / secondary ledgers
- **Domain:** Finance · **iCE severity:** ต่ำ

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** NetSuite Full Multi-Book Accounting รองรับสมุดหลัก 1 + สมุดรองสูงสุด 4 (รวม 5 สมุด active) และต้องเปิดผ่าน OneWorld + NetSuite Professional Services เท่านั้น — ยืดหยุ่นน้อยกว่า reporting/secondary ledgers ของ Oracle ที่รองรับได้มากกว่า องค์กรที่ต้องการสมุดจำนวนมากจะชนเพดาน.

**Counter / Mitigation:** Full Multi-Book Accounting แต่ละชุดต่างมาตรฐานได้ (US GAAP/IFRS/tax/management) พร้อมกฎ mapping ผังบัญชีและปรับค่าเงินรายสมุดในตัว → ตรงกับ "primary + secondary ledgers + auto mapping" ที่ TOR ขอ (native, ไม่ต้อง third-party). องค์กรที่ต้องการสมุดหลัก (statutory ไทย) + 1 สมุด IFRS/บริหาร อยู่ในเพดาน 4 สมุดรองอย่างสบาย — gap เพดาน 4 สมุดจึงแทบไม่กระทบ.

**Procurement caveat:** ระบุจำนวนสมุดที่จำเป็นจริง (โดยทั่วไป 2-3) แทนการเปิด requirement แบบไม่จำกัด เพื่อไม่ให้กลายเป็นเกณฑ์ล็อกสเปก.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-Multi-Book Accounting (multibook_secondary, 0.71) — Full/Adjustment-Only secondary books, OneWorld only, multiple sets of records จาก transaction เดียว
- [WEB:docs.oracle.com] Planning for Multi-Book Accounting — สูงสุด 4 secondary books (รวม 5 active books), ต่าง COA/currency/accounting rules
- [WEB:netsuite.com] Multi-Book Accounting — COA mapping rules ต่อมาตรฐาน

---

## F-FIN-02 — Breadth of statutory localizations (multi-country tax)

- **Capability (TH):** ความกว้างของ localization ตามกฎหมายหลายประเทศ
- **Capability (EN):** Breadth of statutory localizations
- **Domain:** Finance · **iCE severity:** แทบไม่มีผล

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** SuiteTax ของ NetSuite รองรับประเทศแบบ pre-certified น้อยกว่า Oracle Fusion จริง (NetSuite ~50+ ประเทศผ่าน Country Localization/International Tax Reports ซึ่งบางส่วนเป็น SuiteApp/managed bundle). Oracle ชนะเรื่องจำนวนประเทศ.

**Counter / Mitigation:** NetSuite มี SuiteTax engine + ชุด Country Localization/International Tax Reports กว่า 50 ประเทศ รวมไทยผ่าน Southeast Asia Localization + International Tax Reports (ซึ่งเป็น SuiteApp ที่ NetSuite เผยแพร่เองแบบ free managed bundle — ไม่ใช่ third-party). สำหรับองค์กรที่อยู่ประเทศเดียว NetSuite รองรับไทยครบ (ใบกำกับภาษี/ภ.พ.30) — ส่วนที่ Oracle เหนือกว่าคือประเทศอื่นที่องค์กรไม่ได้ใช้.

**Procurement caveat:** การให้ผู้เสนอราคา "ระบุจำนวนประเทศที่รองรับ native" คือการล็อกสเปกที่ไม่สะท้อนความต้องการจริงขององค์กรประเทศเดียว.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-Country Specific Features (0.7295)
- [WEB:docs.oracle.com] List of Country-Specific/SuiteTax Localization Features
- [WEB:suitecertified.com] NetSuite Country Localizations 50+ (secondary — corroborated)

---

## NF-PLT-01 — Extensibility without governance caps

- **Capability (TH):** การต่อยอดโดยไม่มีข้อจำกัด governance
- **Capability (EN):** Extensibility without governance caps
- **Domain:** Technical · **iCE severity:** แทบไม่มีผล

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** SuiteCloud มีเพดาน governance unit จริง (Map/Reduce: map phase 10,000 units/job, ต่อ function 1,000 units) — งานประมวลผลปริมาณมากต้องออกแบบแบ่ง chunk และอาจต้องซื้อ SuiteCloud Plus เพื่อเพิ่ม concurrency/processor. Oracle OCI/VBCS/APEX ต่อยอดได้ทั้ง low-code + pro-code โดยไม่มี per-transaction governance cap.

**Counter / Mitigation:** "มี cap" จริง แต่ "ต่อยอดไม่ได้" เกินจริง — Map/Reduce รีเซ็ต governance ทุก invocation และแบ่ง chunk ประมวลผลปริมาณมากได้ บวก SuiteCloud Plus เพิ่ม concurrency/processor และมีทั้ง low-code (SuiteFlow/SuiteBuilder) และ pro-code (SuiteScript 2.x). เงื่อนไข "ไม่มี governance cap ใดๆ ต่อ transaction" เป็น over-spec เพราะทุกแพลตฟอร์มคลาวด์ multi-tenant รวม Oracle ก็มี resource limit ของตัวเอง. ปริมาณงานระดับองค์กรกลาง (single-country operations) แทบไม่ชน governance cap.

**Procurement caveat:** ข้อกำหนด "ไม่มี cap ต่อ transaction" ไม่มี use case จริง และเป็นเกณฑ์ที่ multi-tenant SaaS ทุกเจ้าไม่ผ่านเท่ากัน — เอียงเข้า PaaS ของ Oracle.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-SuiteScript Developer Guide (0.665) — usage/governance units
- [KB] Netsuite-SuiteScript 2.0 (0.601) — Map/Reduce map phase 10,000 / function 1,000 units, governance reset ต่อ invocation (Hard Limits on Function Invocations)
- [WEB:docs.oracle.com] NetSuite Applications Suite — Concurrency Governance Limits Based on Service Tiers and SuiteCloud Plus Licenses
- [WEB:houseblend.io] NetSuite Map/Reduce Guide — governance reset ต่อ job, processor pool แยกจาก API concurrency [ต้อง verify]

---

## NF-PLT-02 — Mature ALM & dev/test/prod environments

- **Capability (TH):** ALM: dev/test/prod + on-demand refresh
- **Capability (EN):** Mature ALM & environments
- **Domain:** Technical · **iCE severity:** ต่ำ

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** SDF (transport แบบ customization-as-XML) ไม่ครอบทุก customization/config เช่น ไฟล์นอก FileCabinet/SuiteScripts, บาง custom PDF layout และบาง setting ต้องตามด้วยมือ; และ sandbox refresh ไม่ instant มีรอบ/ความถี่จำกัด — จึงไม่ใช่ full transport แบบ SAP. Oracle มี dev/test/prod landscape + transport/CI-CD + on-demand environment refresh.

**Counter / Mitigation:** "ควบคุม landscape อ่อน" เกินจริง — NetSuite มี ALM ใช้งานจริง: แยก dev/test/prod ด้วย sandbox, SDF เป็น transport (customization-as-XML) และ SuiteCloud CLI (Node/Java) ต่อ CI/CD (GitLab/Jenkins/GitHub Actions) ได้ toolchain นี้ใช้งานจริงในอุตสาหกรรม. dev/test/prod sandbox + SuiteCloud CLI เพียงพอกับการดูแลระบบขององค์กรประเทศเดียว ส่วน on-demand refresh + full transport ระดับ enterprise เป็น over-spec.

**Procurement caveat:** เขียน requirement เป็น "แยก dev/test/prod + deployment pipeline ที่ตรวจสอบได้" แทนการบังคับ "on-demand refresh + full transport" ซึ่งเอียงเข้า SAP/Oracle.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-SuiteCloud Development Framework (0.671) — SDF เป็น deployment/transport (customization-as-XML)
- [KB] Netsuite-SuiteCloud SDK Overview (0.654) — SuiteCloud CLI (Java/Node) สำหรับ SDLC/automation
- [WEB:docs.oracle.com] NetSuite Applications Suite — Limitations for Custom Transaction Forms / Customizations Supported by SDF (SDF ไม่ครอบทุก customization)
- [WEB:netsuite.com] How NetSuite Powers DevOps Pipelines with SuiteCloud Platform Developer Tools — SuiteCloud CLI ครอบ SDLC
- [WEB:salto.io] Introduction to CI/CD for SuiteScript — pipeline GitLab/Jenkins/GitHub Actions

---

## NF-INT-01 — Native enterprise iPaaS

- **Capability (TH):** Native enterprise iPaaS
- **Capability (EN):** Native enterprise iPaaS
- **Domain:** Technical · **iCE severity:** ต่ำ

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** NetSuite ไม่มีเครื่องมือ iPaaS orchestration แบบลากวาง (visual) ในตัว — งานเชื่อมหลายระบบที่ซับซ้อนต้องเสริม Celigo หรือ Boomi ซึ่งเป็น SuiteApp ของบุคคลที่สาม (มีต้นทุนไลเซนส์เพิ่ม). Oracle Integration Cloud (OIC) เป็น iPaaS ในตัวพร้อม prebuilt adapters.

**Counter / Mitigation:** ข้ออ้าง "ต้องพึ่ง 3rd-party iPaaS" เกินจริง — NetSuite มีช่องทาง integration ในตัวครบ (SuiteTalk REST/SOAP, RESTlets, SuiteScript และ SuiteAnalytics Connect ODBC/JDBC) ต่อ API งานหนักได้เองโดยไม่บังคับ iPaaS. ที่ขาดคือเครื่องมือ orchestration ลากวางในตัวเท่านั้น. สำคัญ: ฝั่ง Oracle เองก็ไม่ให้ iPaaS ฟรีในตัว — OIC เป็นไลเซนส์แยกคิดตามปริมาณ message (~$2-10k/เดือน) ทั้งสองค่ายต้องมีชั้น iPaaS แยกเมื่องานหนักจริงเหมือนกัน. งานเชื่อม HIS/ระบบเฉพาะทาง/ธนาคาร ปิดได้ด้วย API ในตัว + Celigo ต้นทุนพอประมาณ.

**Procurement caveat:** การบังคับ "iPaaS ในตัว" = over-spec ที่ตัด NetSuite ด้วยมาตรฐานที่ Oracle เองก็ต้องซื้อ OIC แยก.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-SuiteCloud Platform Introduction (0.686)
- [KB] Netsuite-SuiteTalk REST Web Services (0.685)
- [WEB:houseblend.io] Celigo vs Boomi: NetSuite iPaaS Comparison (ยืนยันมีจริง)
- [WEB:erpresearch.com] Oracle ERP Fusion Cloud Pricing — OIC เป็นไลเซนส์แยก คิดตาม message (ยืนยันมีจริง)

---

## NF-INT-02 — Native MDM / data governance

- **Capability (TH):** Master Data Management (MDM)
- **Capability (EN):** Native MDM / data governance
- **Domain:** Technical · **iCE severity:** แทบไม่มีผล

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** NetSuite ไม่มี MDM hub แบบหลายโดเมนเฉพาะทาง (Customer/Product/Supplier Hub) ที่ Oracle มี. (TOR ให้คะแนน 0 "ทำไม่ได้เลย" ซึ่งคลาดเคลื่อน.)

**Counter / Mitigation:** คะแนน 0 เกินจริง — NetSuite มี data governance ในตัวจริง: Duplicate Record Detection & Record Merge (EntityDeduplicationTask), always-on audit trail บนการแก้ master data, field-level/role-based security และ GRC ที่รวมใน platform license แล้ว. ที่ขาดคือ MDM hub แบบ multi-domain/federation เท่านั้น. องค์กรที่ใช้ ERP อินสแตนซ์เดียว NetSuite เป็น single source of truth อยู่แล้ว ไม่ต้องมี MDM hub แยก. ฝั่ง Oracle เอง MDM ก็คือ Customer/Product/Supplier Hub ที่เป็นโมดูล/ไลเซนส์แยก ไม่ใช่ของแถมใน Fusion.

**Procurement caveat:** บังคับ MDM hub ในตัวลง TOR = over-spec สำหรับองค์กรอินสแตนซ์เดียว และเป็นเกณฑ์ที่ Oracle เองก็ตอบด้วยโมดูลแยก.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] NetSuite Basics — Duplicate Record Detection & Merge (0.65)
- [KB] Netsuite-SuiteScript 2.0 API Reference — EntityDeduplicationTask (0.682)
- [WEB:netsuite.com] Governance, Risk & Compliance — audit trail บน master data + field-level security (รวมใน platform license, ยืนยันแล้ว)
- [WEB:oracle.com] Oracle MDM = Customer/Product/Supplier Hub (โมดูลแยก)

---

## NF-ANL-01 — Enterprise embedded analytics (in-memory)

- **Capability (TH):** Embedded analytics ระดับองค์กร
- **Capability (EN):** Enterprise embedded analytics
- **Domain:** Technical · **iCE severity:** ต่ำ

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** งานวิเคราะห์ปริมาณมาก/ข้ามระบบต้องซื้อ NetSuite Analytics Warehouse (NSAW) ซึ่งเป็นโมดูลเสริมเสียเงินต่างหาก (SuiteAnalytics ในตัวไม่ใช่ in-memory columnar). Oracle OTBI + OAC + Autonomous DB วิเคราะห์ in-memory บนข้อมูลปริมาณมากในตัว.

**Counter / Mitigation:** SuiteAnalytics (Workbook + Saved Search + Dashboard/KPI) เป็น analytics ฝังในตัวแบบ self-service อ่านธุรกรรมสด real-time บนฐานข้อมูลเดียว ไม่ต้องมี data warehouse แยก (จุดแข็ง native). งานวิเคราะห์หนักใช้ **NSAW** ซึ่งสร้างบน Oracle Autonomous Data Warehouse + Oracle Analytics Cloud — สแตกเดียวกับที่ฝั่ง Oracle ยกเป็นจุดเด่น. เกณฑ์นี้ตัด NetSuite ด้วยมาตรฐานที่ Oracle เองก็ขาย OAC/Autonomous DW แยกเช่นกัน. dashboard เชิงปฏิบัติการ/กองทุน-บริจาค ครอบคลุมด้วย native + Nonprofit SuiteApp — in-memory ระดับองค์กรเป็น over-spec.

**Procurement caveat:** "โดยไม่ต้องซื้อ data warehouse แยก" เป็นเกณฑ์ไม่สมมาตร เพราะ enterprise BI ของทั้งสองค่ายคือ OAC+ADW ที่ต้องซื้อเพิ่ม.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-SuiteAnalytics Workbook (0.63)
- [WEB:netsuite.com] NetSuite Analytics Data Warehouse — built on Oracle ADW + OAC
- [WEB:katoomi.com] NetSuite Analytics Warehouse: A Technical Overview (ADW columnar + OAC)

---

## NF-ANL-02 — Embedded generative AI / ML across suite

- **Capability (TH):** Embedded Generative AI / ML
- **Capability (EN):** Embedded GenAI across suite
- **Domain:** Technical · **iCE severity:** ต่ำ

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** anomaly detection และ ML forecasting (Intelligent Performance Management) ไม่ได้อยู่ใน base — อยู่ในโมดูล NetSuite EPM ที่ต้องซื้อแยก; และความกว้างของ GenAI ที่ฝังข้ามทุกกระบวนการยังน้อยกว่า Oracle Fusion. Oracle AI ฝังทั่ว Fusion (finance/SCM/HCM).

**Counter / Mitigation:** ภาพ "AI ของ NetSuite ใหม่และเบา" ล้าสมัย — ตั้งแต่ 2024.1 NetSuite ฝัง generative AI (Text Enhance ขับด้วย OCI GenAI) ทั่ว finance/HR(SuitePeople)/SCM/sales-support และมี Bill Capture/Document AI เป็น native; ปี 2025.1 เพิ่ม SuiteAnalytics Assistant (ถาม-ตอบภาษาธรรมชาติ). Document AI ใช้คุมความถูกต้อง AP/รับบริจาคได้ทันทีแบบ native; anomaly/forecasting ต้องลงทุน EPM เพิ่ม; GenAI ข้ามทุกโมดูลเป็น nice-to-have. Oracle ยังกว้างและสุกกว่าจริง แต่ไม่ใช่ว่า NetSuite มีแค่ฟีเจอร์เดียว.

**Procurement caveat:** การล็อกสเปกจาก AI roadmap วันนี้เสี่ยงเลือกจากแผนมากกว่าของจริง — ทั้งสองค่ายพัฒนาเร็วทุกไตรมาส.

**Confidence:** high

**หลักฐาน / Citation:**
- [WEB:netsuite.com] New NetSuite Features Build AI into Everyday Processes
- [WEB:cio.com] NetSuite adds more Text Enhance gen AI capabilities
- [WEB:netsuite.com] GenAI powers new assistant, automated insights in NetSuite 2025.1

---

## NF-ARC-01 — Tier-1 transaction throughput / no governance cap

- **Capability (TH):** Tier-1 transaction throughput
- **Capability (EN):** Tier-1 throughput, no governance cap
- **Domain:** Technical · **iCE severity:** แทบไม่มีผล

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** NetSuite มี governance limit จริง (scheduled/Map-Reduce ~10,000 units/exec; search ดึง 1,000 แถวผ่าน getRange และ 4,000 แถวผ่าน .each()) — เป็นเพดานต่อสคริปต์/ต่อหน้า งานปริมาณมากต้องออกแบบด้วย Map/Reduce + runPaged() แบ่งหน้า. Oracle Fusion + Autonomous DB รองรับ throughput ระดับ tier-1.

**Counter / Mitigation:** เพดานเหล่านี้เป็น "ต่อสคริปต์/ต่อหน้า" ไม่ใช่เพดานปริมาณธุรกรรมทางธุรกิจ — การยกตัวเลข row-limit มาพิสูจน์ "สเกลไม่ได้" เป็นการตีความผิด. งานปริมาณมากใช้ Map/Reduce + runPaged() แบ่งหน้าได้ และตั้งแต่ ก.พ. 2025 NetSuite รันบน Oracle Autonomous Database/OCI (กว่า 12 region) รองรับองค์กรขนาดใหญ่. โหลดขององค์กรกลาง (single-country operations) ระดับปานกลาง ไม่ใช่ tier-1 (ล้านรายการ/วัน).

**Procurement caveat:** บังคับ "ล้านรายการ/วัน ไม่มี throttling" = over-spec/ล็อกสเปก สำหรับองค์กรที่ไม่มีปริมาณระดับนั้น.

**Confidence:** high

**หลักฐาน / Citation:**
- [WEB:docs.oracle.com] NetSuite Help — Search getRange/.each() limits (1,000/4,000)
- [WEB:prnewswire.com] NetSuite Migrates to Oracle Autonomous Database (Feb 2025; 'over a dozen regions')
- [KB] Netsuite-SuiteScript 2.0 API Reference — runPaged()/governance (0.577)

---

## NF-ARC-02 — Deployment options & data residency / sovereignty

- **Capability (TH):** ทางเลือกการติดตั้ง / data residency
- **Capability (EN):** Deployment & data residency options
- **Domain:** Technical · **iCE severity:** สูง

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** NetSuite เป็น multi-tenant SaaS ล้วน — ไม่มีทางเลือก on-prem/private/Cloud@Customer และไม่มี data center ในไทย อีกทั้งยังไม่รองรับ Oracle EU Sovereign Cloud (เลือกได้เพียง data center ภูมิภาค เช่น EU). **เป็นช่องว่างที่ปิดด้วย SuiteApp/custom ไม่ได้เลย.** Oracle มีเส้นทาง in-country/sovereign (AIS Cloud/Oracle Alloy ในไทย, EU Sovereign Cloud).

**Counter / Mitigation:** ข้อจำกัดนี้ถูกต้อง (ไม่ใช่กล่าวเกิน) — แต่ NetSuite เลือก data center ภูมิภาคได้ (EU: Amsterdam/Frankfurt/London ฯลฯ) จึงมี data residency เชิงภูมิภาค. on-prem/private เป็น over-spec เมื่อองค์กรเลือกแนวทาง SaaS และ PDPA ไทยไม่บังคับเก็บข้อมูลในประเทศ. **อย่างไรก็ตาม นี่เป็น 1 ในไม่กี่ข้อที่ควรพิจารณาจริง** (ดู second-opinion §C): หากบอร์ดให้น้ำหนัก sovereignty ของข้อมูลสุขภาพ/ผู้บริจาค (บริบท healthcare/blood-bank/public-sector) ต้องยอมรับความเสี่ยงระดับบอร์ดก่อน go-live — Oracle มีเส้นทาง in-country ที่ NetSuite ยังไม่มี.

**Procurement caveat:** เป็นประเด็นนโยบาย sovereignty ไม่ใช่ข้อบังคับกฎหมาย (PDPA ไทยไม่บังคับ data localization) — แต่ต่างจาก gap อื่น ข้อนี้ปิดด้วย add-on ไม่ได้ ควรเคลียร์เป็นการตัดสินใจ/ยอมรับความเสี่ยงระดับบอร์ด. [ต้อง verify สถานะ Oracle EU Sovereign Cloud]

**Confidence:** medium

**หลักฐาน / Citation:**
- [WEB:netsuite.com] What is NetSuite ERP (multi-tenant SaaS, no on-prem)
- [WEB:sota.io] NetSuite NOT available on Oracle EU Sovereign Cloud as of Q1 2026 [ต้อง verify]
- [WEB:oracle.com] AIS Cloud / Oracle Alloy — in-country Thai cloud (2024)
- [KB] NSTWP — multi-tenant shared service (0.541)

---

## NF-SEC-01 — Automated SoD & access governance

- **Capability (TH):** Automated Segregation of Duties (SoD)
- **Capability (EN):** Automated SoD & access governance
- **Domain:** Technical · **iCE severity:** สูง

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** NetSuite ไม่มี engine Segregation of Duties (SoD) อัตโนมัติและ continuous controls monitoring สำเร็จรูปแบบ native — ต้องเสริมด้วย SuiteApp ของพาร์ทเนอร์. Oracle Risk Management Cloud (Advanced Access Controls) ทำ automated SoD + access governance + risk mgmt ในตัว และเหนือกว่าชัดเจน.

**Counter / Mitigation:** ข้อความ "ไม่มี access governance ระดับ audit" ลดทอนของจริง — NetSuite มี role-based security ละเอียด, เครื่องมือตรวจสิทธิ์ในตัว (Use Searches to Audit Roles, Show Role Permission Differences), Login Audit Trail, 2FA/SSO และผ่าน SOC 1/2, ISO 27001 จริง. ปิด gap SoD engine ด้วย **SuiteApp certified ต้นทุนไม่สูง** (Fastpath Assure, Netwrix Strongpoint, SafePaaS). **เป็น 1 ในข้อที่ควรพิจารณาจริง** (second-opinion §C) เพราะ SoD ครอบการรับบริจาค/จัดซื้อจัดจ้างที่อยู่ภายใต้การตรวจของ สตง. — ควรวางแผนจัดหา SuiteApp certified ปิด gap ก่อน go-live. ส่วน GRC engine อัตโนมัติระดับ enterprise เต็มรูปเป็นส่วนเกินของ NGO ประเทศเดียว.

**Procurement caveat:** บังคับ "automated SoD ในตัว native" ล็อกเข้า Oracle Risk Mgmt Cloud — เขียนเป็น outcome (มี SoD control + audit trail ที่ตรวจสอบได้) ที่ NetSuite + certified SuiteApp ตอบได้.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-Managing Users & Roles (0.6678) — Use Searches to Audit Roles + Login Audit Trail
- [KB] Netsuite-Managing Users & Roles (0.6544) — periodic access review/terminated-user revocation
- [WEB:oracle.com] Oracle Advanced Access Controls Cloud Service datasheet — automated SoD + continuous monitoring + ruleset สำเร็จรูปจำนวนมาก
- [WEB:suiteapp.com] Fastpath Assure for NetSuite — SoD analysis by user/role/permission (ruleset 125+ conflicts)
- [WEB:mysuite.tech] Segregation of Duties in NetSuite: where native tools stop

---

## NF-SEC-02 — Industry / government accreditations

- **Capability (TH):** Industry / Government Accreditations
- **Capability (EN):** Industry/government accreditations
- **Domain:** Technical · **iCE severity:** แทบไม่มีผล

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** NetSuite ไม่มี accreditation ภาครัฐแบบ FedRAMP / government-cloud / sovereign region เหมือน Oracle OCI เพราะเป็น multi-tenant SaaS ล้วน. Oracle มี industry solutions + gov/regulated accreditation กว้าง.

**Counter / Mitigation:** Oracle NetSuite ถือใบรับรองสากลครบ: SOC 1/SOC 2 Type II, ISO 27001/27018/42001 และ PCI DSS Level 1 Service Provider + PCI SSF. Oracle มี accreditation ภาครัฐกว้างกว่าจริง แต่เป็นการรับรองของรัฐบาล/กลาโหมสหรัฐฯ ไม่ใช่ข้อกำหนดของหน่วยงานไทย. ใบรับรองที่เกี่ยวข้องจริง (ISO 27001, SOC, PCI สำหรับช่องทางรับบริจาคบัตรเครดิต) NetSuite มีครบ.

**Procurement caveat:** เขียน TOR ให้ต้องมี "accreditation ภาครัฐกว้าง" = over-spec ที่เอียงเข้าหา Oracle — ควรระบุเฉพาะใบรับรองที่เกี่ยวข้องกับธุรกิจจริงของหน่วยงาน.

**Confidence:** high

**หลักฐาน / Citation:**
- [WEB:netsuite.com] NetSuite Application and Operational Security — SOC 1/2, ISO 27001/27018/42001, PCI DSS, PCI SSF
- [WEB:houseblend.io] NetSuite Audit Readiness: SOC 1, SOC 2 & ISO 27001 Guide
- [WEB:stratusgreen.com] NetSuite PCI Compliance — Level 1 Service Provider

---

## GP-FUNC-12 — Group consolidation & multi-GAAP at scale

- **Capability (TH):** งบรวมกลุ่มหลายมาตรฐานบัญชี ขนาดใหญ่
- **Capability (EN):** Group consolidation & multi-GAAP at scale
- **Domain:** Finance · **iCE severity:** แทบไม่มีผล

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** สำหรับกลุ่มบริษัทใหญ่หลายสิบนิติบุคคลข้ามประเทศที่ถือหุ้นบางส่วน Oracle FCCS (Hyperion) เหนือกว่าเรื่อง consolidation ซับซ้อน (NCI/equity method, multi-GAAP at scale). (3-way: NetSuite 3★ · Oracle Fusion 5★ · SAP S/4HANA 4★.)

**Counter / Mitigation:** ข้อเปรียบเทียบนี้ค่อนข้างสมดุลอยู่แล้ว (แหล่งให้ NetSuite 3/5) — OneWorld + Multi-Book ของ NetSuite ทำ consolidation พื้นฐาน + multi-GAAP ได้ในตัว เพียงจำกัดในเคสซับซ้อนมาก (equity method/complex NCI). สำหรับนิติบุคคลเดียวในประเทศ ไม่ต้องทำงบรวมกลุ่มหลายนิติบุคคลข้ามประเทศ ความสามารถระดับ FCCS จึงเป็น over-spec ไม่มี use case จริง.

**Procurement caveat:** "at scale" ในบริบทองค์กรนิติบุคคลเดียว = over-spec ในบริบท TOR.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-Multi-Book Accounting (multibook_secondary, 0.71) — secondary books multi-GAAP
- [KB] Netsuite-General Accounting (consolidation, 0.59) — Intercompany Auto Elimination + consolidated exchange rates
- [WEB:timdietrich.me] NetSuite Intercompany Transactions & Eliminations — OneWorld เพียงพอ mid-market แต่จำกัดในเคสซับซ้อน (equity method, complex NCI)

---

## GP-FUNC-13 — Enterprise planning & budgeting (EPM / xP&A)

- **Capability (TH):** วางแผนงบ/พยากรณ์องค์กร (EPM / xP&A)
- **Capability (EN):** Enterprise Planning & Budgeting (EPM / xP&A)
- **Domain:** EPM · **iCE severity:** ต่ำ

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** NSPB เป็นโมดูลเสริมมีค่า license แยก และเป็นรุ่น productized (Financials) ที่ปรับแต่งได้จำกัดกว่า Oracle EPBCS เต็ม — ไม่มีโมดูล Workforce/Capital สำเร็จรูป และไม่มี FCCS/ARCS/PCMCS ในชุดเหมือน Oracle EPM Cloud. (3-way: NetSuite 2★ · Oracle Fusion 5★ · SAP 4★, แหล่งตี Critical.)

**Counter / Mitigation:** การให้ 2/5 และตี "Critical gap" เกินจริง เพราะ NSPB ใช้เอนจิน PBCS/Hyperion เดียวกับ Oracle EPM Cloud จึงทำ xP&A core (driver-based, scenario, predictive, rolling forecast) ได้ในตัว. ความต่างคือความกว้างของ pre-built modules และระดับ customization ไม่ใช่ core capability ที่ขาดหาย. งบประมาณที่สำนักงบประมาณองค์กรใช้จริงครอบคลุมด้วย NSPB Financials — ความกว้างระดับ Hyperion เต็มสูบเกินความจำเป็น.

**Procurement caveat:** การตี "Critical" และบังคับ Workforce/Capital สำเร็จรูปในตัวเป็นการยกระดับ severity ที่ล็อกเข้า Oracle EPM Cloud.

**Confidence:** high

**หลักฐาน / Citation:**
- [WEB:docs.oracle.com] NetSuite Planning and Budgeting Financials Overview — driver-based, what-if scenarios, Predictive Planning (article_7160253896 — ตรวจแล้วมีจริง)
- [WEB:docs.oracle.com] NetSuite Planning and Budgeting — รองรับเฉพาะโมดูล Financials, ไม่มี Workforce module (article_8124016549 — ตรวจแล้วมีจริง)
- [WEB:netsuite.com] What is NetSuite Planning and Budgeting — built on Oracle EPM Cloud engine, scenario/what-if (financial-planning.shtml)
- [KB] Netsuite-Statistical Accounting / Netsuite-General Accounting (~0.6) — base NetSuite มีเพียง budget/statistical allocation พื้นฐาน

---

## GP-FUNC-16 — Statutory localization, tax engine & e-invoicing (e-Tax Invoice TH)

- **Capability (TH):** Tax engine & localization ตามกฎหมายแต่ละประเทศ
- **Capability (EN):** Statutory localization, tax engine & e-invoicing
- **Domain:** Finance · **iCE severity:** สูง

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** SuiteTax ครอบคลุมประเทศน้อยกว่า SAP/Oracle; และสำคัญกว่า — **ไม่มีมาตรฐาน e-Tax Invoice ไทยแบบ native**: Electronic Invoicing SuiteApp เป็นเพียง "กรอบ" ออก XML/JSON ต้องทำ template เอง/ใช้ partner. (3-way: NetSuite 2★ · Oracle 4★ · SAP 5★, Critical.)

**Counter / Mitigation:** SuiteTax เป็น tax engine จริง + localization ไทย (SEA Localization, International Tax Reports → VAT/ภ.พ.30, ใบกำกับภาษี/เครดิตโน้ตตามรูปแบบกรมสรรพากร) ครบสำหรับไทย — การให้ 2★ ประเมินต่ำไปสำหรับ scope ไทย. ช่องว่างจริงเหลือเฉพาะ **e-Tax Invoice XML ส่งกรมสรรพากร** ที่ต้อง custom/partner ไม่ใช่ "ทำภาษีไม่ได้" และไม่ใช่เรื่องจำนวนประเทศ. **นี่คือ gap severity สูงที่ต้องวางแผนปิดก่อน go-live** — e-Tax Invoice & e-Receipt เป็นข้อบังคับตามกฎหมายไทย กระทบทุกหน่วยที่ออกเอกสารภาษี.

**Procurement caveat:** ส่วนความกว้างหลายประเทศไม่เกี่ยวกับองค์กรประเทศเดียว (over-spec) แต่ e-Tax Invoice ไทยเป็นข้อกำหนดจริงที่ต้องระบุแยกและปิดด้วย custom/partner.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-Country Specific Features (0.7242, SuiteTax Reports/VAT)
- [WEB:docs.oracle.com] Thailand Tax Invoice & Credit Memo Templates (SEA Localization, P.P.30)
- [WEB:docs.oracle.com] Electronic Invoicing Overview (กรอบ XML/JSON ไม่มี native มาตรฐานไทย)

---

## GP-FUNC-18 — Core HR & multi-country global payroll

- **Capability (TH):** Core HR + Global Payroll หลายประเทศ
- **Capability (EN):** Core HR & multi-country global payroll
- **Domain:** HCM · **iCE severity:** กลาง

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** NetSuite SuitePeople payroll เนทีฟมีเฉพาะสหรัฐ (SuitePeople U.S. Payroll) — ไม่มีเงินเดือนไทย/หลายประเทศในตัว ต้องใช้ SuiteApp พาร์ตเนอร์หรือเชื่อมระบบเงินเดือนไทยภายนอก. Oracle HCM & SAP SuccessFactors เป็น tier-1. (3-way: NetSuite 1★ · Oracle 5★ · SAP 5★, Critical.)

**Counter / Mitigation:** เรต 1★/Critical ต่ำเกินจริง — NetSuite SuitePeople มี Core HR เนทีฟจริง (ทะเบียนพนักงาน/org chart, การลา Time-Off, ติดตามค่าตอบแทน-สวัสดิการ, ยืนยัน KB 0.72). ที่ขาดคือ payroll หลายประเทศ/ไทยเนทีฟ ซึ่งทำได้ผ่าน SuiteApp พาร์ตเนอร์ (เช่น NuSmart International Payroll / International Payroll Extension) — ไม่ใช่ "ทำไม่ได้" แต่ก็ไม่ใช่ "เนทีฟฟรี". สำหรับองค์กรที่จ่ายเงินเดือนในไทยประเทศเดียว เกณฑ์ "global/หลายประเทศ" ไม่เกี่ยว (over-spec); ที่ใช้จริงคือ Core HR (เนทีฟ) + เงินเดือนไทย (ต่อเชื่อม) — ต้องวางสถาปัตยกรรม payroll ไทยแบบต่อเชื่อมตั้งแต่ต้น.

**Procurement caveat:** ควรแยกเกณฑ์ "Core HR" (NetSuite ผ่าน native) ออกจาก "global payroll" (ไม่เกี่ยว/over-spec) — การมัดรวมแล้วบังคับ Mandatory เอียงเข้า Oracle/SAP. [ต้อง verify SuiteApp พาร์ตเนอร์ครอบคลุมภาษี/ประกันสังคมไทยจริง]

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-Employee Management — Core HR/Time-Off/Compensation (0.7159)
- [WEB:docs.oracle.com] NetSuite Applications Suite - SuitePeople U.S. Payroll (native payroll = US-only)
- [WEB:suiteapp.com] International Payroll Extension for SuitePeople / NuSmart International Payroll and HCM (third-party SuiteApp; ครอบคลุมไทยจริงหรือไม่ [ต้อง verify])

---

## GP-FUNC-27 — Governance, Risk & Compliance (GRC) / SoD

- **Capability (TH):** กำกับ ความเสี่ยง การควบคุม / SoD
- **Capability (EN):** Governance, Risk & Compliance (GRC) / SoD
- **Domain:** GRC · **iCE severity:** สูง

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** NetSuite มีเครื่องมือ native แค่บริหาร role/permission + audit trail + approval workflow + ตรวจสิทธิ์ (saved search/role audit) — ไม่มี engine automated SoD/continuous controls monitoring แบบเนทีฟอย่าง Oracle Risk Mgmt Cloud หรือ SAP GRC Access Control. (3-way: NetSuite 2★ · Oracle 5★ · SAP 5★, High.)

**Counter / Mitigation:** เรตติ้ง 2★ (Partial) สมเหตุผล และ gap automated SoD/CCM เทียบ Oracle/SAP มีจริง — แต่ถ้อยคำ "SoD/role review พื้นฐาน" ลดทอน: NetSuite มีเครื่องมือ audit role + audit trail native และ ecosystem SoD ที่ certified เต็มที่. ปิด gap ด้วย **SuiteApp** (Fastpath Assure, Netwrix Strongpoint, SafePaaS). **severity สูงเพราะองค์กรอยู่ใต้การตรวจของ สตง.** — SoD เป็นข้อกำหนดด้านธรรมาภิบาล/ตรวจสอบ ต้องวางแผนติดตั้ง SuiteApp SoD ที่ certified และออกแบบ controls ก่อน go-live. ส่วน continuous controls monitoring ระดับ enterprise เต็มรูปเป็นส่วนเสริมที่เลือกได้.

**Procurement caveat:** บังคับ "automated SoD/CCM ในตัว native" ล็อกเข้า Oracle/SAP — เขียนเป็น outcome (มี SoD control ที่ certified + ตรวจสอบได้).

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-Managing Users & Roles (0.695/0.6678) — role permissions + audit role searches
- [WEB:netsuite.com] What is NetSuite Governance, Risk & Compliance? — GRC = native controls + partner SuiteApp (ไม่ใช่ SoD engine native)
- [WEB:oracle.com] Oracle Risk Management Cloud — automated SoD + continuous monitoring
- [WEB:netwrix.com] NetSuite Segregation of Duties (Strongpoint) — alert on SoD conflicts
- [WEB:suiteapp.com] Fastpath Assure for NetSuite

---

## GP-TECH-01 — In-memory DB & real-time embedded analytics

- **Capability (TH):** ฐานข้อมูลในหน่วยความจำ / วิเคราะห์เรียลไทม์
- **Capability (EN):** In-memory DB & real-time embedded analytics
- **Domain:** Technical · **iCE severity:** แทบไม่มีผล

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** NetSuite ไม่มีเครื่องยนต์ฐานข้อมูล in-memory columnar แบบ SAP HANA ในตัว — หากต้องการวิเคราะห์ปริมาณมหาศาลแบบ in-memory ต้องเปิดผ่าน NSAW (Oracle Autonomous DW) ซึ่งเป็นโมดูลเสริมเสียเงิน. (3-way: NetSuite 2★ · Oracle 4★ · SAP 5★, High.)

**Counter / Mitigation:** ข้อกล่าวอ้าง "NetSuite ไม่มี analytics layer แบบ real-time" **ไม่ถูกต้อง** — NetSuite รันบนฐานข้อมูลเดียว โพสต์ธุรกรรม real-time, SuiteAnalytics/Saved Search/Dashboard อ่านข้อมูลสดทันทีโดยไม่ต้อง sync (จุดแข็ง native). HANA in-memory แรงจริงสำหรับวิเคราะห์ปริมาณมหาศาล แต่เป็น over-spec; real-time operational analytics ที่ native ครอบงานรับบริจาค/คลัง/ปฏิบัติการได้ ส่วน in-memory tier-1 ไม่มี use case จริง.

**Procurement caveat:** เหตุผลหลักที่ใช้ตัด NetSuite (ว่าไม่มี real-time analytics) เป็นข้อเท็จจริงที่ผิด — ควร reject เกณฑ์นี้.

**Confidence:** high

**หลักฐาน / Citation:**
- [WEB:netsuite.com] SuiteAnalytics — built-in real-time reporting/searches/dashboards
- [WEB:theblueflamelabs.com] SuiteAnalytics Workbook real-time on live transactional data
- [KB] Netsuite-SuiteAnalytics Workbook (0.63)

---

## GP-TECH-02 — Very high transaction volume & concurrency

- **Capability (TH):** ปริมาณธุรกรรม/ผู้ใช้พร้อมกันสูงมาก
- **Capability (EN):** Very high transaction volume & concurrency
- **Domain:** Technical · **iCE severity:** แทบไม่มีผล

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** NetSuite มี governance limit (SuiteScript units, concurrency, ผลค้นหา 1,000/4,000 แถวต่อครั้ง) — ต้องออกแบบ batch/pagination และอาจซื้อ SuiteCloud Plus เพื่อเพิ่ม concurrency จึงไม่ใช่ throughput แบบ "ไม่มีเพดานเลย" อย่าง SAP/Oracle tier-1. (3-way: NetSuite 2★ · Oracle 5★ · SAP 5★, Critical.)

**Counter / Mitigation:** หลักฐานที่อ้าง (search 1,000/4,000 แถว) เป็นเพดานต่อหน้า/ต่อสคริปต์ ไม่ใช่เพดานข้อมูล — เกิน 5,000 ผลลัพธ์ใช้ Query.runPaged()/saved search แบบแบ่งหน้า (วนได้หลายหมื่น-แสนแถว) และเพิ่ม concurrency ด้วย SuiteCloud Plus. governance ออกแบบเพื่อความเป็นธรรม multi-tenant ไม่ได้จำกัด throughput ธุรกิจ. ปริมาณ/concurrency ขององค์กรกลางไม่ถึงระดับชน limit เหล่านี้.

**Procurement caveat:** การยกตัวเลข row-limit มาเป็นข้อพิสูจน์ "สเกลไม่ได้" เป็นการตีความผิด — สเกลระดับล้านรายการ/วันเป็น over-spec ที่ไม่มี use case.

**Confidence:** high

**หลักฐาน / Citation:**
- [WEB:docs.oracle.com] NetSuite Help — Search Result Limits
- [KB] Netsuite-SuiteScript 2.0 — runPaged() required when >5,000 results (0.573)
- [WEB:anchorgroup.tech] Paginating large result sets via runPaged()

---

## GP-TECH-03 — Customization & extensibility platform depth (PaaS)

- **Capability (TH):** แพลตฟอร์มปรับแต่ง/ต่อยอด (PaaS)
- **Capability (EN):** Customization & extensibility platform depth
- **Domain:** Technical · **iCE severity:** ต่ำ

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** SuiteCloud (custom record, SuiteScript 2.x, SuiteFlow, Suitelet, RESTlet, SDF) ต่อยอดบน NetSuite ได้จริง แต่ไม่ใช่ general-purpose PaaS สำหรับสร้างแอปพลิเคชันแยกอิสระแบบ Oracle APEX/SAP BTP และยังมี governance cap. (3-way: NetSuite 3★ · Oracle 4★ · SAP 5★, High.)

**Counter / Mitigation:** เรตติ้ง 3★ พอรับได้ แต่กรอบ "สู้ไม่ได้เพราะ governance cap" เกินจริง — governance เป็น guardrail ของ multi-tenant ไม่ใช่กำแพง. SuiteCloud เป็นแพลตฟอร์มต่อยอดที่สมบูรณ์พอควร (custom record, SuiteScript 2.x, SuiteFlow, Suitelet สร้าง UI เอง, RESTlet, SDF, SuiteTalk REST/SOAP). ความลึกของ SuiteCloud ครอบคลุมความต้องการ customization ภายในระบบ ERP ได้เพียงพอ — ไม่จำเป็นต้องมี enterprise PaaS เต็มรูปมาสร้างแอปนอกระบบ.

**Procurement caveat:** บังคับ "general-purpose PaaS ในตัว" เอียงเข้า APEX/BTP — over-spec สำหรับ customization ในระบบ ERP.

**Confidence:** medium

**หลักฐาน / Citation:**
- [KB] Netsuite-SuiteScript Developer Guide (0.665) — SuiteScript governance units
- [KB] Netsuite-SuiteCloud Development Framework (0.671) — แพลตฟอร์มต่อยอด/transport
- [KB] Netsuite-SuiteCloud Platform Introduction (0.671) — ขอบเขต SuiteCloud (SuiteScript/SuiteBuilder/SuiteFlow/SuiteBundler)
- [WEB:netsuite.com] How NetSuite Powers DevOps Pipelines with SuiteCloud Platform Developer Tools — ความกว้างของ SuiteCloud platform

---

## GP-TECH-04 — Embedded AI/ML & GenAI across processes

- **Capability (TH):** AI/GenAI ฝังในกระบวนการธุรกิจ
- **Capability (EN):** Embedded AI/ML & GenAI across processes
- **Domain:** Technical · **iCE severity:** ต่ำ

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** AI ขั้นสูงอย่าง anomaly detection และ ML forecasting/variance ไม่ใช่ฟีเจอร์ base — ต้องซื้อโมดูล NetSuite EPM แยก (Intelligent Performance Management ~$10k-25k/ปี) และความกว้างของ GenAI ที่ฝังข้ามทุกกระบวนการยังน้อยกว่า Oracle Fusion. (3-way: NetSuite 2★ · Oracle 5★ · SAP 4★, High.)

**Counter / Mitigation:** ภาพ "NetSuite เพิ่งเริ่มทำ AI" ล้าสมัย — AI พื้นฐานฝัง native แล้ว (Text Enhance/OCI GenAI, Bill Capture/Document AI ตั้งแต่ 2024.1, SuiteAnalytics Assistant 2025.1). Document AI ใช้คุมงาน AP/รับบริจาคได้ทันทีแบบ native; anomaly/forecasting เป็นการลงทุนเสริม (EPM); ความกว้างระดับองค์กรเป็น nice-to-have. ช่องว่างกับ Oracle แคบลงมาก ไม่ใช่ระดับ "เพิ่งเริ่ม".

**Procurement caveat:** การล็อกสเปกจาก AI roadmap วันนี้เสี่ยงเลือกจากแผนมากกว่าของจริง.

**Confidence:** high

**หลักฐาน / Citation:**
- [WEB:netsuite.com] How NetSuite uses AI
- [WEB:houseblend.io] NetSuite AI/EPM — Exception Management + IPM (anomaly/forecast)
- [WEB:gurussolutions.com] NetSuite AI in 2026 — capabilities and features

---

## GP-TECH-05 — Enterprise BI & self-service analytics

- **Capability (TH):** BI/Self-service analytics ระดับองค์กร
- **Capability (EN):** Enterprise BI & self-service analytics
- **Domain:** Technical · **iCE severity:** ต่ำ

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** BI ระดับองค์กร/วิเคราะห์ข้ามแหล่งข้อมูลไม่ใช่ของ native — ต้องเปิดผ่าน NSAW (NetSuite Analytics Warehouse = Oracle Analytics Cloud + Autonomous DW รีแบรนด์) ซึ่งเป็นโมดูลเสริมเสียเงิน. (3-way: NetSuite 2★ · Oracle 5★ · SAP 5★, High.)

**Counter / Mitigation:** self-service BI มี native อยู่แล้ว (SuiteAnalytics Workbook แบบ drag-drop dataset/pivot/chart + Dashboard/KPI บนข้อมูลสด). การเทียบ add-on พรีเมียมของ Oracle (OAC+ADW) กับ native ของ NetSuite ไม่เป็นธรรม — enterprise BI ของ NetSuite ก็คือ OAC+Autonomous DW รีแบรนด์เป็น NSAW (ต้องซื้อเพิ่มเช่นกัน). native SuiteAnalytics + Nonprofit dashboard เพียงพอสำหรับองค์กรสาธารณกุศล; OAC/HANA ระดับองค์กรเกินความจำเป็น.

**Procurement caveat:** เกณฑ์ตัด NetSuite ด้วย enterprise BI ที่ Oracle/SAP เองก็ขายเป็น add-on แยก (NSAW = เครื่องยนต์เดียวกับ OAC+ADW) — ไม่สมมาตร.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-SuiteAnalytics Workbook (0.63); NetSuite Basics (0.60)
- [WEB:netsuite.com] SuiteAnalytics business intelligence — self-service
- [WEB:katoomi.com] NSAW technical overview — built on OAC + Autonomous DW

---

## GP-TECH-06 — Native iPaaS / integration platform

- **Capability (TH):** แพลตฟอร์มเชื่อมต่อ (iPaaS) ในตัว
- **Capability (EN):** Native iPaaS / integration platform
- **Domain:** Technical · **iCE severity:** ต่ำ

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** NetSuite ไม่มี iPaaS orchestration engine ในตัวแบบ Oracle OIC/SAP Integration Suite — งาน orchestration/mapping ที่ซับซ้อนต้องพึ่งเครื่องมือ iPaaS ของพาร์ทเนอร์ (Celigo/Boomi/Workato/MuleSoft). (3-way: NetSuite 3★ · Oracle 5★ · SAP 5★, Med.)

**Counter / Mitigation:** เรตติ้ง 3 ดาวสะท้อนว่า NetSuite ไม่ได้อ่อน — สิ่งที่มีคือช่องทาง integration มาตรฐาน (SuiteTalk REST/SOAP, RESTlet, SuiteScript) ที่มี concurrency throttle (ยกเพดานได้ด้วย SuiteCloud Plus). สิ่งที่ขาดคือ iPaaS orchestration ในตัวเท่านั้น ซึ่ง Oracle OIC/SAP Integration Suite ก็เป็น add-on แยกไลเซนส์เช่นกัน. ปริมาณการเชื่อมต่อระดับกลางใช้ API ในตัวรองรับได้ ไม่ใช่จุดตัดสิน.

**Procurement caveat:** การเทียบว่า "Oracle/SAP มีในตัว" ไม่แฟร์ เพราะ OIC/Integration Suite เป็นไลเซนส์แยก.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-SuiteTalk REST Web Services (0.685)
- [KB] Netsuite-SuiteCloud Platform Introduction (0.686)
- [WEB:erpresearch.com] OIC เป็นไลเซนส์แยกจาก Fusion ERP (ยืนยันมีจริง)
- [WEB:houseblend.io] NetSuite iPaaS Comparison (Celigo/Boomi/Workato/MuleSoft)

---

## GP-TECH-07 — Deployment options (public/private/on-prem)

- **Capability (TH):** ทางเลือกติดตั้ง (cloud/private/on-prem)
- **Capability (EN):** Deployment options (public/private/on-prem)
- **Domain:** Technical · **iCE severity:** แทบไม่มีผล

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** NetSuite เป็น public multi-tenant cloud อย่างเดียว ไม่มีทางเลือก private cloud หรือ on-premise แบบ SAP RISE/S/4HANA on-prem (ทุกอย่างเป็น fully-managed บน OCI/Oracle Autonomous Database). เป็นข้อจำกัดจริงตามสเปก. (3-way: NetSuite 1★ · Oracle 4★ · SAP 5★, High.)

**Counter / Mitigation:** เมื่อองค์กรตัดสินใจมุ่งใช้ SaaS แล้ว ความยืดหยุ่นเรื่อง private/on-prem จะไม่ถูกนำมาใช้จริง. การบังคับ on-prem/private ใน RFP ระบบคลาวด์เป็นการล็อกสเปกเพื่อกัน vendor ที่เป็น SaaS-only มากกว่าจะเป็นความต้องการใช้งานจริง.

**Procurement caveat:** on-prem/private ใน RFP คลาวด์ = ล็อกสเปก — ควร reject หากองค์กรเลือกแนวทาง SaaS.

**Confidence:** medium

**หลักฐาน / Citation:**
- [WEB:netsuite.com] Why Multi-tenancy in the Cloud Matters (cloud-only, no on-prem)
- [WEB:netsuite.com] What is NetSuite ERP

---

## GP-TECH-08 — Data residency, sovereignty & region count

- **Capability (TH):** ถิ่นที่อยู่ข้อมูล / sovereign / จำนวน region
- **Capability (EN):** Data residency, sovereignty & region count
- **Domain:** Technical · **iCE severity:** สูง

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** NetSuite ให้ data residency ผ่าน data center หลายภูมิภาค (EU/NA/APAC) แต่ **ไม่มี DC ในประเทศไทย และไม่รองรับ EU Sovereign Cloud** ขณะที่ Oracle มีเส้นทาง sovereign/in-country (EU Sovereign Cloud, AIS Cloud/Oracle Alloy ไทย) ที่ NetSuite ยังไม่มี — จุดต่างนี้ไม่สมมาตร. (3-way: NetSuite 2★ · Oracle 5★ · SAP 4★, High.)

**Counter / Mitigation:** NetSuite ไม่ได้ "ไม่มี residency" อย่างที่อ้าง — ให้ residency เชิงภูมิภาคได้; จุดต่างจริงคือไม่มี DC ในไทย. PDPA ไม่บังคับ localization และข้อมูลไทยของ public SaaS ทั้งสองเจ้าอยู่ต่างประเทศคล้ายกัน (Oracle Fusion SaaS public มาตรฐานก็ไม่มี region ในไทย) — แต่ไม่สมมาตรเสียทีเดียวเพราะ Oracle มีเส้นทาง sovereign/in-country ที่ NetSuite ยังไม่มี. **severity สูงในบริบท healthcare/blood-bank/public-sector** เพราะข้อมูลสุขภาพ/ผู้บริจาคทำให้ sovereignty มีน้ำหนักเชิงนโยบาย/การตรวจสอบ — ควรเคลียร์ทางเลือก data center ในประเทศ/sovereign ก่อน go-live.

**Procurement caveat:** เป็นน้ำหนักเชิงนโยบาย ไม่ใช่ข้อบังคับ PDPA — แต่ต่างจาก gap อื่น ปิดด้วย SuiteApp ไม่ได้ [ต้อง verify].

**Confidence:** medium

**หลักฐาน / Citation:**
- [WEB:netsuite.com] NetSuite Data Center datasheet — EU DCs (Amsterdam/Frankfurt/London/Newport), no Thai DC
- [WEB:sota.io] NetSuite not on Oracle EU Sovereign Cloud (Q1 2026) [ต้อง verify]
- [WEB:bakermckenzie.com] Thailand cross-border data transfer — no localization mandate
- [WEB:oracle.com] AIS Cloud / Oracle Alloy Thailand (2024)

---

## GP-TECH-09 — Guaranteed performance SLA at peak

- **Capability (TH):** SLA/การันตี throughput บน multi-tenant
- **Capability (EN):** Guaranteed performance SLA at peak
- **Domain:** Technical · **iCE severity:** แทบไม่มีผล

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** NetSuite เป็น shared multi-tenant SaaS จึงไม่มี SLA การันตี throughput ตายตัวช่วง peak — performance อาจแปรปรวนตามทรัพยากรรวม มีให้แค่ uptime SLA และเครื่องมือ APM (Application Performance Management SuiteApp ฟรี) ไว้ตรวจ/จูน. (3-way: NetSuite 2★ · Oracle 4★ · SAP 5★, Med.)

**Counter / Mitigation:** ข้อจำกัดนี้ไม่ใช่ของ NetSuite โดยเฉพาะ — Oracle Fusion SaaS ก็ multi-tenant เช่นกัน การตัด NetSuite ที่ "peak SLA" จึงเป็นการเทียบไม่สมมาตร. ปริมาณงานช่วง peak (รับบริจาค/ปิดบัญชี) ขององค์กรสาธารณกุศลไม่สูงพอจะชนเพดานทรัพยากร.

**Procurement caveat:** เกณฑ์ "การันตี throughput SLA" บน multi-tenant ตัด SaaS ทุกเจ้ารวม Fusion — ไม่สมมาตร.

**Confidence:** medium

**หลักฐาน / Citation:**
- [WEB:netsuite.com] Why Multi-tenancy in the Cloud Matters
- [KB] Netsuite-Application Performance Management Guide (0.564)

---

## GP-TECH-10 — Languages, country & statutory coverage

- **Capability (TH):** จำนวนภาษา/ประเทศ/statutory ที่รองรับ
- **Capability (EN):** Languages, country & statutory coverage
- **Domain:** Technical · **iCE severity:** แทบไม่มีผล

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** NetSuite รองรับจำนวนประเทศ/statutory น้อยกว่า SAP จริง จึงเสียเปรียบหากต้องใช้กับองค์กรข้ามชาติหลายประเทศ. (3-way: NetSuite 2★ · Oracle 4★ · SAP 5★, High.)

**Counter / Mitigation:** localization ไทยครบถ้วนผ่าน Southeast Asia Localization SuiteApp + SuiteTax (ภาษาไทย, VAT ภ.พ.30, ใบกำกับภาษี/Branch ID, ภาษีหัก ณ ที่จ่าย รายงาน ภ.ง.ด.). ความกว้าง statutory หลายประเทศไม่เกี่ยวกับองค์กรที่ดำเนินงานในไทยประเทศเดียว — ตัวข้อความในแหล่งยังระบุเองว่า "สำคัญสำหรับองค์กรข้ามชาติ".

**Procurement caveat:** over-spec ที่ชัดเจนสำหรับ single-country organization.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-Country Specific Features — Thailand Tax Codes/VAT ภ.พ.30 (0.619)
- [KB] Netsuite-Country Specific Features — Southeast Asia Localization SuiteApp/Thailand Invoicing (0.606)

---

## GP-TECH-11 — Fine-grained access & automated SoD controls

- **Capability (TH):** ควบคุมสิทธิ์ละเอียด / SoD อัตโนมัติ
- **Capability (EN):** Fine-grained access & automated SoD controls
- **Domain:** Technical · **iCE severity:** สูง

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** NetSuite ไม่มี "การแยกหน้าที่อัตโนมัติ" (SoD) ระดับ ruleset และ continuous control monitoring แบบ preventive ในตัว — ทำได้เพียง detective (เช่น Login Audit Trail) และต้องเสริมด้วย SuiteApp พาร์ทเนอร์ (Fastpath Assure, Netwrix Strongpoint, SafePaaS). Oracle Risk Mgmt/SAP GRC มีในตัว. (3-way: NetSuite 2★ · Oracle 5★ · SAP 5★, High.)

**Counter / Mitigation:** "NetSuite role-based พื้นฐาน" มองข้ามว่าการคุมสิทธิ์ของ NetSuite ละเอียด (fine-grained permission 636+ ต่อ record/feature) + Login Audit Trail + 2FA/TBA และ audit ได้ — gap SoD อัตโนมัติปิดได้ด้วย add-on. **severity สูงเพราะกระทบงานควบคุมภายในที่อยู่ใต้การตรวจของ สตง.** — ต้องวางแผนจัดซื้อ add-on SoD/GRC และตั้งงบบริหารจัดการก่อน go-live. ส่วน automated continuous SoD ระดับ enterprise เป็นส่วนเสริมที่เกินจำเป็นสำหรับสเกลองค์กรกลาง.

**Procurement caveat:** บังคับ "automated SoD preventive ในตัว" ล็อกเข้า Oracle Advanced Access Controls — เขียนเป็น outcome ที่ NetSuite + certified SuiteApp ตอบได้.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-Managing Users & Roles (0.6691) — granular permission structure (636+ permissions)
- [KB] Netsuite-Authentication Guide — 2FA / token-based auth; Netsuite-Administrator Guide (0.6642) — password policy + SoD monitoring example (PO created by AP)
- [WEB:oracle.com] Oracle Advanced Access Controls — continuous SoD monitoring
- [WEB:mysuite.tech] NetSuite SoD native vs add-on boundary (detective not preventive)

---

## GP-TECH-12 — Industry-specific cloud solutions depth

- **Capability (TH):** โซลูชันเฉพาะอุตสาหกรรม
- **Capability (EN):** Industry-specific cloud solutions depth
- **Domain:** Technical · **iCE severity:** สูง

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** การผลิตชีววัตถุ (เซรุ่ม/วัคซีน) ระดับ GMP เต็มรูปไม่ครบในตัว — electronic batch record/GMP เชิงลึกต้องประเมิน fit และอาจต้องเสริมโซลูชัน ISV เฉพาะ. SAP มี industry solutions ลึกสุด (oil&gas, utilities, auto, pharma). (3-way: NetSuite 2★ · Oracle 4★ · SAP 5★, High.)

**Counter / Mitigation:** **ข้อกล่าวอ้าง "NetSuite อ่อน vertical" กลับด้าน** — vertical ที่เกี่ยวกับองค์กรสาธารณกุศล/non-profit จริง NetSuite แข็งและเป็น native-grade: **NFP Financials SuiteApp** (Revenue Restriction Management, Grant Management, Pledge & Donation, รายงาน Net Assets/FASB) และด้าน blood-bank/biologics มี lot-numbered + วันหมดอายุ + FEFO + Quality Management SuiteApp เป็นพื้นฐาน traceability. อุตสาหกรรมที่แหล่งยกมา (oil&gas, utilities, auto) ไม่เกี่ยวกับองค์กรเลย. gap severity สูงเฉพาะการผลิตชีววัตถุ GMP ของหน่วยผลิตเซรุ่ม/วัคซีน ที่ต้องประเมินและปิด gap ก่อน go-live.

**Procurement caveat:** การสรุปว่า NetSuite "อ่อน vertical" ละเลย nonprofit/fund-grant ที่ NetSuite แข็งและตรงงานที่สุด — เกณฑ์นี้เอียง.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-Non-Profit SuiteApps — NFP Financials/Revenue Restriction/Grant (0.63)
- [KB] NSIMG — FEFO Lot Allocations/expiry (0.658)
- [KB] Netsuite-Item Record Management — lot numbered + expiration labels (0.682)

---

## GP-TECH-13 — Upgrade control & release management

- **Capability (TH):** ควบคุมการอัปเกรด / รอบ release
- **Capability (EN):** Upgrade control & release management
- **Domain:** Technical · **iCE severity:** ต่ำ

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** NetSuite บังคับ upgrade 2 ครั้ง/ปี ข้ามไม่ได้ และคุมเวลา/รอบเองได้น้อย — มีเพียง Release Preview ให้ทดสอบล่วงหน้าเฉพาะช่วง preview window. ต่างจาก SAP private/on-prem ที่คุมรอบเองได้. (3-way: NetSuite 3★ · Oracle 4★ · SAP 4★, Med.)

**Counter / Mitigation:** การให้ Fusion เหนือกว่าทำให้เข้าใจผิด เพราะ **Fusion บังคับอัปเดตถี่กว่า (รายไตรมาส 4 ครั้ง/ปี) opt out/ข้ามไม่ได้เช่นกัน**; มีเพียง SAP private/on-prem ที่คุมรอบเองได้จริง. forced upgrade ของ SaaS เป็นเรื่องปกติ ภาระจริงเหลือเพียง regression test ตามรอบปีละ 2 ครั้งซึ่งบริหารจัดการได้ และอาจเป็นข้อดี (ทันสมัยเสมอ ไม่มีต้นทุน/โปรเจกต์อัปเกรดเอง).

**Procurement caveat:** เกณฑ์ "คุมรอบอัปเกรด" ที่ให้ Fusion เหนือ NetSuite ผิดข้อเท็จจริง (Fusion ถี่กว่า).

**Confidence:** high

**หลักฐาน / Citation:**
- [WEB:terillium.com] NetSuite Upgrade Schedule — 2 major releases/ปี ข้ามไม่ได้
- [WEB:docs.oracle.com] NetSuite Release Preview — สภาพแวดล้อมทดสอบรีลีสใหม่ เปิดเฉพาะช่วง preview window (ไม่ใช่ sandbox ฟรีทั่วไป)
- [WEB:blogs.oracle.com] fusioninsider Quarterly updates made easy — Fusion อัปเดตรายไตรมาส บังคับ
- [WEB:community.oracle.com] Skipping quarterly release cycles of ERP cloud — ยืนยัน opt out/ข้ามรอบไม่ได้

---

## GP-TECH-14 — Native master data management & governance

- **Capability (TH):** บริหารข้อมูลหลักในตัว (MDM/governance)
- **Capability (EN):** Native Master Data Management & governance
- **Domain:** Technical · **iCE severity:** แทบไม่มีผล

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** NetSuite ไม่มี MDM hub แท้แบบ multi-domain/federation (บริหารข้อมูลหลักข้ามหลายระบบต้นทาง) — มีเพียง Duplicate Detection, Record Merge และ audit trail บน master data. เป็นข้อจำกัดเชิงเทคนิคจริง; SAP MDG มีในตัว. (3-way: NetSuite 2★ · Oracle 4★ · SAP 5★, High.)

**Counter / Mitigation:** MDM แบบ federation มีค่าเมื่อมีหลายระบบต้นทาง/หลายอินสแตนซ์ — องค์กรที่ใช้ ERP เดียวเป็นแกน ข้อมูลหลักอยู่ใน NetSuite อยู่แล้ว. Oracle เองก็ทำผ่าน Product Hub/Customer Hub ที่เป็นโมดูลแยก (ไม่ใช่ in-the-box). การลงทุน MDM hub จึงเกินความจำเป็น.

**Procurement caveat:** MDM hub ในตัว = over-spec/ล็อกสเปกสำหรับองค์กรอินสแตนซ์เดียว/ในประเทศเดียว.

**Confidence:** medium

**หลักฐาน / Citation:**
- [KB] NetSuite Basics — Duplicate Record Detection & Merge (0.65)
- [WEB:netsuite.com] Governance, Risk & Compliance — audit trail บน master data (ยืนยันมีจริง)
- [WEB:oracle.com] Oracle Product Hub / Customer Hub (โมดูล MDM แยก)

---

## GP-TECH-15 — API governance limits (concurrency / row caps)

- **Capability (TH):** ข้อจำกัด API (concurrency/row limit)
- **Capability (EN):** API governance limits (concurrency / row caps)
- **Domain:** Technical · **iCE severity:** แทบไม่มีผล

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** NetSuite มีเพดาน governance ของ API จริงและยืนยันตามเอกสาร — SuiteTalk concurrency ฐาน 5 (shared)/15 (Tier 1)/20 (Tier 2-Ultimate) เกินแล้วได้ HTTP 429, และ saved search ผ่าน SOAP สูงสุด 1,000 แถว/หน้า. (3-way: NetSuite 1★ · Oracle 4★ · SAP 5★, High.)

**Counter / Mitigation:** เพดานนี้ยกได้ด้วยการซื้อ SuiteCloud Plus license (+10 concurrency ต่อ license) และหลบ cap 1,000 แถวได้ด้วย REST/SuiteQL/RESTlets (ที่ไม่ติด cap แบบ saved search). ปริมาณธุรกรรมระดับกลางไม่ถึงระดับที่ governance เป็นคอขวด — การให้ 1 ดาวว่าเป็น "เพดานจริงของ integration ปริมาณสูง" เกินจริงสำหรับสเกลองค์กรกลาง.

**Procurement caveat:** เกณฑ์ที่วัด integration ปริมาณสูงมาก = over-spec สำหรับปริมาณจริงระดับกลาง.

**Confidence:** medium

**หลักฐาน / Citation:**
- [KB] Netsuite-SuiteTalk SOAP Web Services Platform Guide — Governance Overview (0.766)
- [KB] NSTWP — Concurrency / Search Page Size 1,000 (0.62)
- [WEB:docs.oracle.com] NetSuite Help — Concurrency Governance Limits Based on Service Tiers & SuiteCloud Plus (ยืนยันตัวเลขตรง)
- [WEB:katoomi.com] NetSuite Integration Concurrency Limits 2025 (ยืนยันมีจริง)

---

## GP-STANDOUT-01 — Fusion standout: Enterprise Planning & Budgeting (EPM / xP&A)

- **Capability (TH):** วางแผนงบ-พยากรณ์องค์กร (EPM / xP&A)
- **Capability (EN):** Enterprise Planning & Budgeting (EPM / xP&A)
- **Domain:** EPM · **iCE severity:** ต่ำ

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** การวางแผนงบ-พยากรณ์ขั้นสูงของ NetSuite ต้องซื้อ NSPB เป็น add-on แยก และความลึกด้าน driver-based, multi-scenario, financial close/consolidation รวมศูนย์ ยังไม่เทียบชั้น Oracle EPM Cloud (สาย Hyperion, best-in-class). (Fusion standout Rank 1.)

**Counter / Mitigation:** EPM/xP&A ระดับ Hyperion เป็นจุดแข็ง Oracle จริง แต่ "เกินความจำเป็น" ขององค์กรสาธารณกุศล — งบประมาณ/พยากรณ์ใช้ **NSPB + NSAW** เพียงพอ. การตั้งสเปก driver-based/multi-scenario ทั้งองค์กร = over-spec ที่ดันค่า license + implementation ขึ้นมาก.

**Procurement caveat:** ตั้งสเปก EPM เต็มรูปทั้งองค์กรเป็น over-spec ที่ดันค่า license/implementation ขึ้นโดยไม่มี use case จริงรองรับ.

**Confidence:** low *(standout item — no KB/web citation in source record)*

**หลักฐาน / Citation:** *(no KB/web citations provided in this standout record; positioning based on iCE second-opinion analysis — NSPB/NSAW cross-referenced in F-EPM-01, GP-FUNC-13)*

---

## GP-STANDOUT-02 — Fusion standout: Embedded AI/ML & GenAI across the suite

- **Capability (TH):** AI/GenAI ฝังทั่วทั้งชุดแอป
- **Capability (EN):** Embedded AI/ML & GenAI across the suite
- **Domain:** Technical · **iCE severity:** ต่ำ

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** AI/GenAI ฝังในตัวของ NetSuite ยังกระจายไม่กว้างและไม่ลึกเท่า Oracle Fusion ที่ฝังข้ามทุกโมดูลบน data model เดียว — anomaly detection/ML forecasting อยู่ในโมดูล EPM ที่ต้องซื้อแยก. (Fusion standout Rank 2.)

**Counter / Mitigation:** AI พื้นฐานฝัง native แล้ว (Text Enhance, Bill Capture/Document AI, SuiteAnalytics Assistant). AI/GenAI ฝังในชุดแอปเป็น "nice to have" ไม่ใช่ตัวตัดสิน และทั้งสองค่ายพัฒนาเร็วทุกไตรมาส. Document AI ใช้คุมงาน AP/รับบริจาคได้ทันทีแบบ native; anomaly/forecasting เป็นการลงทุนเสริม.

**Procurement caveat:** การล็อกสเปกจาก roadmap วันนี้เสี่ยงเลือกจากแผนมากกว่าของจริง.

**Confidence:** low *(standout item — no KB/web citation in source record)*

**หลักฐาน / Citation:** *(no KB/web citations provided in this standout record; native AI positions cross-referenced in NF-ANL-02, GP-TECH-04)*

---

## GP-STANDOUT-03 — Fusion standout: Unified HCM on a single data model

- **Capability (TH):** HCM แบบรวมศูนย์ data model เดียว
- **Capability (EN):** Unified HCM on a single data model
- **Domain:** HCM · **iCE severity:** กลาง

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** SuitePeople ของ NetSuite เป็น HCM แบบ light — ขาดความลึกด้าน talent/workforce และไม่มี payroll ไทยในตัว ต้องต่อเชื่อมพันธมิตร payroll ไทยภายนอก. ต่างจาก Oracle HCM Cloud (Gartner Leader) ที่อยู่บน data model เดียวกับ Finance. (Fusion standout Rank 3.)

**Counter / Mitigation:** HCM/Global Payroll หลายประเทศ "ไม่เกี่ยว" กับองค์กรที่ payroll อยู่ในไทยประเทศเดียว และงาน HR/เงินเดือนมักใช้ระบบเฉพาะของไทย/ราชการอยู่แล้ว — **SuitePeople + พันธมิตร payroll ไทย ครอบคลุมได้**. payroll ไทยไม่ต้องการ global payroll หลายประเทศ แต่ยังต้องวางงานเชื่อมต่อระบบ payroll ไทย/พันธมิตรให้กลืนกับ SuitePeople ซึ่งเป็นงานที่บริหารจัดการได้.

**Procurement caveat:** "global HCM/payroll data model เดียว" over-spec สำหรับ single-country payroll.

**Confidence:** low *(standout item — no KB/web citation in source record)*

**หลักฐาน / Citation:** *(no KB/web citations provided in this standout record; SuitePeople Core HR + Thai-payroll-connect positions cross-referenced in GP-FUNC-18, TOR-HCM-01)*

---

## GP-STANDOUT-04 — Fusion standout: One unified cloud on a single data model

- **Capability (TH):** ชุดคลาวด์เดียว data model เดียว
- **Capability (EN):** One unified cloud on a single data model
- **Domain:** Technical · **iCE severity:** แทบไม่มีผล

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** จุดอ่อนที่แท้คือ "ความกว้าง/ความลึกของโมดูล" (HCM/EPM/SCM) ที่ถูกประเมินแยกในข้ออื่น. (Fusion standout Rank 4 — Fusion อ้าง ERP+SCM+HCM+EPM+CX ออกแบบเป็นชุดเดียว.)

**Counter / Mitigation:** **ข้อนี้ย้อนแย้ง** — "ชุดคลาวด์เดียว data model เดียว" คือจุดแข็งดั้งเดิมของ NetSuite (born-in-cloud, unified suite) ตั้งแต่ต้น การยกเป็นข้อได้เปรียบเฉพาะ Fusion จึงไม่สร้างความต่าง. NetSuite ตอบเกณฑ์ unified data model ได้เต็มเช่นเดียวกับ Fusion — ข้อนี้ไม่ใช่ช่องว่างที่แท้จริง.

**Procurement caveat:** เกณฑ์ "unified single cloud" เป็นจุดแข็ง NetSuite เองมาแต่ต้น — ยกเป็นข้อได้เปรียบ Fusion ไม่มีมูล.

**Confidence:** low *(standout item — no KB/web citation in source record)*

**หลักฐาน / Citation:** *(no KB/web citations provided in this standout record; iCE second-opinion — NetSuite born-in-cloud unified suite)*

---

## GP-STANDOUT-05 — Fusion standout: Embedded analytics + Autonomous Data Warehouse

- **Capability (TH):** Analytics + Autonomous Data Warehouse
- **Capability (EN):** Embedded analytics + Autonomous Data Warehouse
- **Domain:** Technical · **iCE severity:** ต่ำ

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** SuiteAnalytics ในตัว NetSuite มีขอบเขตจำกัด — การได้ analytics ระดับองค์กร + data warehouse ต้องซื้อ NSAW เป็น add-on แยก. (Fusion standout Rank 5: OAC + Autonomous DW.)

**Counter / Mitigation:** **NSAW สร้างบน Oracle Autonomous Data Warehouse ตัวเดียวกับ OAC ที่ Fusion ใช้** และให้ self-service analytics + prebuilt content. ความต้องการ BI ขององค์กรสาธารณกุศลยังไม่ถึงระดับที่ต้องตั้งสเปก enterprise warehouse แยกต่างหาก.

**Procurement caveat:** เกณฑ์นี้เทียบ add-on พรีเมียมของ Oracle กับ native ของ NetSuite — แต่ enterprise BI ของทั้งสองค่ายคือ ADW เดียวกัน (NSAW = OAC+ADW).

**Confidence:** low *(standout item — no KB/web citation in source record)*

**หลักฐาน / Citation:** *(no KB/web citations provided in this standout record; NSAW = OAC+ADW positioning cross-referenced in NF-ANL-01, GP-TECH-05)*

---

## GP-STANDOUT-08 — Fusion standout: Autonomous Database foundation

- **Capability (TH):** Autonomous Database ใต้ระบบ
- **Capability (EN):** Autonomous Database foundation
- **Domain:** Technical · **iCE severity:** แทบไม่มีผล

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** ใต้ระบบ NetSuite เป็น multi-tenant ทั่วไป ไม่ได้โฆษณาคุณสมบัติ self-tuning/self-patching/self-securing แบบ Oracle Autonomous Database ที่ Fusion ใช้ ซึ่งเป็นข้อได้เปรียบด้าน infra/TCO ของ Oracle. (Fusion standout Rank 8.)

**Counter / Mitigation:** NetSuite เป็น SaaS ที่ Oracle ดูแล infrastructure/patching/security ให้ทั้งหมดอยู่แล้ว ผู้ใช้ไม่ต้องมี DBA. **ยิ่งไปกว่านั้น NetSuite ย้ายไปรันบน Oracle Autonomous Database (ประกาศ ก.พ. 2025) จึงได้ auto-tune/patch/scale/secure ในตัวเช่นกัน** (ดู TOR-TECH-08). เป็นเกณฑ์ที่ตั้งใน NFR ได้แต่ "มองไม่เห็น" จากมุมงานจริงของผู้ใช้ปลายทาง.

**Procurement caveat:** differentiator นี้ล้าสมัย — NetSuite รันบน Autonomous DB เดียวกัน.

**Confidence:** low *(standout item — no KB/web citation in source record; but corroborated by TOR-TECH-08 citations)*

**หลักฐาน / Citation:** *(no KB/web citations in this standout record; corroborating migration evidence at TOR-TECH-08 — [WEB:prnewswire.com] NetSuite Migrates to Oracle Autonomous Database, Feb 2025)*

---

## GP-STANDOUT-09 — Fusion standout: Broad public + sovereign cloud regions

- **Capability (TH):** region/sovereign cloud หลากหลาย
- **Capability (EN):** Broad public + sovereign cloud regions
- **Domain:** Technical · **iCE severity:** สูง

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** ตัวเลือก data center ของ NetSuite จำกัดและไม่มี government/sovereign region ในไทย ต่างจาก OCI ที่มี public + government + sovereign regions มากกว่า. **ข้อนี้เป็นข้อได้เปรียบ Fusion/OCI ที่ legitimate.** (Fusion standout Rank 9.)

**Counter / Mitigation:** หากมีข้อกำหนด data residency ในไทยสำหรับข้อมูลสุขภาพ/ผู้บริจาคภายใต้ PDPA (บริบท blood-bank/healthcare) เรื่อง region/sovereign cloud **อาจเป็น blocker** — ต้องตรวจตัวเลือก data center ในประเทศของทั้งสองค่ายและวางแผนปิด gap ก่อน go-live **(ไม่ใช่ปัดทิ้ง)**. เป็น 1 ในข้อที่ควรพิจารณาจริง (second-opinion §C) — Oracle มีเส้นทาง in-country/sovereign ที่ NetSuite ยังไม่มี.

**Procurement caveat:** เป็นข้อได้เปรียบ Fusion ที่ชอบธรรม — ไม่ควรปัดทิ้งเป็น over-spec; แต่ PDPA ไทยยังไม่บังคับ localization [ต้อง verify].

**Confidence:** medium *(standout item — no KB/web citation in this record, but corroborated by GP-TECH-08 / NF-ARC-02)*

**หลักฐาน / Citation:** *(no KB/web citations in this standout record; corroborating residency evidence at GP-TECH-08 / NF-ARC-02 — [WEB:oracle.com] AIS Cloud/Oracle Alloy Thailand; [WEB:sota.io] NetSuite not on EU Sovereign Cloud Q1 2026 [ต้อง verify])*

---

## GP-STANDOUT-10 — Fusion standout: Continuous quarterly innovation, low-disruption

- **Capability (TH):** นวัตกรรมต่อเนื่องไม่ disrupt
- **Capability (EN):** Continuous quarterly innovation, low-disruption
- **Domain:** Technical · **iCE severity:** ต่ำ

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** NetSuite บังคับ upgrade 2 รอบ/ปีตามปฏิทิน (ทีม IT ต้อง regression test ตามรอบ) ขณะ Fusion ปล่อยฟีเจอร์รายไตรมาสแบบ opt-in granularity ละเอียดกว่า. (Fusion standout Rank 10.)

**Counter / Mitigation:** ทั้งคู่เป็น continuous cloud ปล่อยแบบ opt-in มี SuiteApp ecosystem และไม่ rip-and-replace — ข้ออ้างว่า "นวัตกรรมรายไตรมาสไม่ disrupt" เป็นจุดเด่นเฉพาะ Fusion จึงอ่อน. ภาระจริงเหลือเพียงการทดสอบ release ตามรอบปีละ 2 ครั้งซึ่งบริหารจัดการได้.

**Procurement caveat:** ยกความถี่ release เป็นข้อได้เปรียบ Fusion ไม่สมเหตุผล — ทั้งคู่เป็น continuous cloud.

**Confidence:** low *(standout item — no KB/web citation in source record)*

**หลักฐาน / Citation:** *(no KB/web citations provided in this standout record; upgrade-cadence facts cross-referenced in GP-TECH-13)*

---

## TOR-FIN-01 — TOR: Enterprise planning & budgeting (xP&A) on ERP platform

- **Capability (TH):** เครื่องมือวางแผนงบประมาณและพยากรณ์ระดับองค์กร (xP&A) บนแพลตฟอร์มเดียวกับ ERP
- **Capability (EN):** Native Enterprise Planning & Budgeting (xP&A) on the same platform as the ERP
- **Domain:** EPM · **iCE severity:** ต่ำ · **TOR verdict:** Partial · Mandatory

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** NSPB ยังไม่มีโมดูล Workforce/Capital planning สำเร็จรูป (Oracle Help ระบุรองรับเฉพาะโมดูล Financials) และเป็นแอป/ลิขสิทธิ์แยกจาก ERP — การวางแผนกำลังคน/งบลงทุนต้องสร้างเป็น driver model เอง ไม่ใช่ template พร้อมใช้.

**Counter / Mitigation:** xP&A core (driver-based, multi-scenario, rolling forecast, predictive) ทำได้ first-party บนเอนจิน Oracle EPM เดียวกัน (sync GL อัตโนมัติ) — "Partial" สมเหตุผลเฉพาะส่วน workforce/capital ไม่ใช่เพราะขาด core. การวางแผนกำลังคน/งบลงทุนทำได้ผ่าน driver-based ใน NSPB Financials.

**Procurement caveat:** บังคับให้มีโมดูล workforce/capital planning สำเร็จรูป + predictive multi-scenario ระดับ enterprise ใน TOR = over-spec/ล็อกสเปกเอียงไป Oracle EPBCS.

**Confidence:** high

**หลักฐาน / Citation:**
- [WEB:docs.oracle.com] NetSuite Planning and Budgeting — 'supports only the Financials module. A Workforce module is not currently available.' (article_8124016549 — ตรวจแล้วมีจริง)
- [WEB:docs.oracle.com] NetSuite Planning and Budgeting Financials Overview — driver-based/trend-based/direct-input, what-if, Predictive Planning (article_7160253896 — ตรวจแล้วมีจริง)
- [WEB:netsuite.com] What is NetSuite Planning and Budgeting — produce scenario plans, multiple what-if, driver-based (financial-planning.shtml)
- [KB] Netsuite-Sales Force Automation (~0.6) — base NetSuite มีเพียง sales forecasting/GL budget; xP&A เต็มต้องใช้ NSPB add-on

---

## TOR-FIN-02 — TOR: Multi-level group consolidation, multi-GAAP, auditable close

- **Capability (TH):** งบการเงินรวมหลายระดับ หลายมาตรฐาน (multi-GAAP/IFRS) + intercompany elimination + currency translation + ปิดงบอัตโนมัติที่ตรวจสอบได้
- **Capability (EN):** Multi-level group consolidation across multiple accounting standards, with intercompany elimination, currency translation, and an auditable automated close
- **Domain:** Finance · **iCE severity:** กลาง · **TOR verdict:** Partial · Mandatory

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** การปิดงบอัตโนมัติที่ตรวจสอบได้ (auditable automated close) ไม่มี native — ต้องเสริมโมดูล NSAR (ซื้อเพิ่ม); และเคสซับซ้อน เช่น NCI/equity method ต้อง SuiteApp หรือปรับด้วยมือ.

**Counter / Mitigation:** งบการเงินรวมหลายระดับ/หลายมาตรฐาน, intercompany auto-elimination และ currency translation ทำได้ native (OneWorld + Multi-Book Accounting) → เข้าข่ายใกล้ Fully มากกว่าจะเป็นแค่ Partial. งบรวมหลายกองทุน/หน่วยงาน + IFRS รองรับได้จริง กระทบเฉพาะต้นทุน NSAR add-on และงานปิดบัญชีส่วนที่ซับซ้อนเกิน mid-market ซึ่งองค์กรนิติบุคคลเดียวมีน้อย.

**Procurement caveat:** ตั้งบาร์ "ซับซ้อนระดับ FCCS/NCI" ให้ NetSuite = Partial มีลักษณะล็อกสเปก เพราะส่วนที่ซับซ้อนนั้นไม่เกี่ยวกับองค์กรนิติบุคคลเดียว.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-General Accounting (consolidation, 0.59) — Intercompany Auto Elimination + consolidated exchange rates (currency translation)
- [KB] Netsuite-Multi-Book Accounting (multibook_secondary, 0.71) — multi-GAAP secondary books
- [WEB:prnewswire.com] NetSuite Account Reconciliation 2023-06-14 — auditable automated close (add-on)
- [WEB:timdietrich.me] NetSuite Intercompany Transactions & Eliminations — multi-tier consolidation, auto elimination, CTA + ข้อจำกัด NCI/equity method

---

## TOR-FIN-03 — TOR: Statutory tax / e-invoicing (e-Tax Invoice TH)

- **Capability (TH):** localization + statutory/tax compliance ในตัวสำหรับทุกประเทศ รวม e-invoicing/e-tax โดยไม่พึ่ง third-party add-on
- **Capability (EN):** Built-in localization and statutory/tax compliance for every country, including country-specific e-invoicing/e-tax, without third-party add-ons
- **Domain:** Finance · **iCE severity:** สูง · **TOR verdict:** No · Mandatory

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** e-Tax Invoice/e-Receipt แบบ XML ส่งกรมสรรพากรยังไม่มี native — Electronic Invoicing เป็นกรอบเปล่า ต้องทำ custom template หรือใช้ partner SuiteApp.

**Counter / Mitigation:** การตอบ "No" เกินจริงสำหรับ scope ไทย — statutory ไทยพื้นฐาน (VAT/ภ.พ.30, ใบกำกับภาษี/เครดิตโน้ต) รองรับผ่าน **SEA Localization + International Tax Reports ซึ่งเป็น free managed bundle ของ NetSuite เอง (ไม่ใช่ third-party ตามที่อ้าง)** → ความจริงคือ Partial ไม่ใช่ No. จุดอ่อนจริงเหลือเฉพาะ e-Tax Invoice XML. **severity สูง** เพราะ e-Tax Invoice & e-Receipt เป็นข้อบังคับตามกฎหมายไทย — ต้องวางแผนปิด gap นี้ (custom/partner) ก่อนใช้งานจริง.

**Procurement caveat:** เงื่อนไข "ทุกประเทศ + e-tax native โดยไม่พึ่ง add-on" = ล็อกสเปก (องค์กรอยู่ไทยประเทศเดียว และ SuiteApp ที่ใช้เป็นของ NetSuite เอง ไม่ใช่ third-party).

**Confidence:** high

**หลักฐาน / Citation:**
- [WEB:docs.oracle.com] Southeast Asia Localization (free managed first-party bundle)
- [WEB:docs.oracle.com] Thailand Invoicing Features / Electronic Invoicing Overview (กรอบ ไม่มี native ไทย)
- [KB] Netsuite-Country Specific Features (0.7209)

---

## TOR-HCM-01 — TOR: Core HR & payroll

- **Capability (TH):** Core HR และ Global Payroll หลายประเทศในตัว (org management, absence, benefits, จ่ายเงินเดือนตามกฎหมายแต่ละประเทศ)
- **Capability (EN):** Native Core HR and multi-country Global Payroll (org management, absence, benefits, statutory payroll per country)
- **Domain:** HCM · **iCE severity:** กลาง · **TOR verdict:** No · Mandatory

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** NetSuite ไม่มี global payroll หลายประเทศและไม่มี payroll ไทยแบบ native (มีเฉพาะ SuitePeople U.S. Payroll) — การจ่ายเงินเดือนตามกฎหมายแรงงานไทยต้องต่อเชื่อม SuiteApp พาร์ทเนอร์ (เช่น NuSmart International Payroll) หรือระบบภายนอก.

**Counter / Mitigation:** การตอบ "No" ทั้งข้อไม่ถูกต้องนัก — **SuitePeople ทำ Core HR, org management, absence (Time-Off), benefits/compensation ในตัวได้ (ยืนยัน KB 0.72)**. ที่ขาดจริงคือ payroll หลายประเทศ/ไทยเนทีฟ. ควรแยกเกณฑ์ "Core HR" (ผ่าน native) ออกจาก "global payroll" (ไม่เกี่ยว). payroll ไทยเป็นงานที่ใช้จริงและต้องวางสถาปัตยกรรมต่อเชื่อมกับระบบเงินเดือนภายนอก.

**Procurement caveat:** ตั้ง Mandatory + No โดยผูกผลทั้งหมดไว้กับ "multi-country global payroll" ที่องค์กรประเทศเดียวไม่ได้ใช้ ทั้งที่ Core HR ที่ใช้จริง NetSuite มีเนทีฟ — เข้าข่ายล็อกสเปกเอียงเข้า Oracle/SAP. [ต้อง verify SuiteApp payroll ไทย]

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-Employee Management — SuitePeople Core HR/Time-Off/Compensation (0.7159)
- [WEB:docs.oracle.com] SuitePeople U.S. Payroll (native = US-only)
- [WEB:suiteapp.com] NuSmart International Payroll and HCM (third-party payroll; Thai coverage [ต้อง verify])
- [แก้ misattribution] 'Jcurve Thai Localization for NetSuite' เป็น localization ภาษี (VAT/WHT/master data) ไม่ใช่ payroll — ตัดออกจากหลักฐานเงินเดือนไทย

---

## TOR-TECH-01 — TOR: Tier-1 scalability / transaction throughput

- **Capability (TH):** รองรับปริมาณธุรกรรม/ผู้ใช้พร้อมกันสูงระดับองค์กรโดยไม่มี governance limit + ระบุ throughput/concurrency ที่การันตี
- **Capability (EN):** Enterprise-scale transaction volumes and concurrency without governance limits + guaranteed throughput/concurrency figures
- **Domain:** Technical · **iCE severity:** แทบไม่มีผล · **TOR verdict:** Partial · Mandatory

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** NetSuite มี governance/concurrency cap และ search page size สูงสุด 1,000 บรรทัดจริง และ **ไม่ออกการันตี throughput เป็นตัวเลข SLA** ตามที่ TOR ขอ — ต้องออกแบบงานปริมาณมากผ่าน Map/Reduce (processor queue แยก) และซื้อ SuiteCloud Plus เพิ่ม concurrent web services.

**Counter / Mitigation:** รองรับงานปริมาณมากด้วย Map/Reduce (processor queue แยก ไม่นับรวม web services concurrency), SuiteCloud Plus (+10 concurrent ต่อ license) และ CSV import — "Partial = สเกลไม่ได้" เกินจริง. ปริมาณธุรกรรมของศูนย์โลหิต/รพ./บริจาค/จัดซื้อไม่ถึงระดับ tier-1 (ล้านรายการ/วัน) ที่ governance cap จะเป็นคอขวด.

**Procurement caveat:** "ไม่มี governance cap + การันตี throughput" เป็น over-spec ที่ในทางปฏิบัติไม่ผูกมัดงานจริง.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-SuiteTalk SOAP Web Services Platform Guide (0.718) — แต่ละ SuiteCloud Plus license เพิ่ม concurrent web services +10
- [KB] NSTWP (0.516) — pageSize preference (search page size, สูงสุด 1,000)
- [WEB:docs.oracle.com] Concurrency Governance Limits Based on Service Tiers and SuiteCloud Plus Licenses
- [WEB:houseblend.io] NetSuite Map/Reduce Guide — processor pool แยก ไม่นับ API concurrency, chunk งานปริมาณมากได้ [ต้อง verify]

---

## TOR-TECH-02 — TOR: Enterprise analytics / in-memory BI

- **Capability (TH):** วิเคราะห์ข้อมูลเรียลไทม์ฝังในตัวบนธุรกรรมสด + self-service BI + data warehouse ระดับองค์กรที่บริหารจัดการเอง
- **Capability (EN):** Embedded real-time analytics on live data, self-service BI, and a self-managing enterprise data warehouse
- **Domain:** Technical · **iCE severity:** ต่ำ · **TOR verdict:** Partial · Important

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** "self-managing enterprise data warehouse" ไม่ native — ต้องซื้อ NSAW (บน Oracle Autonomous Database) เป็น add-on เสียเงินแยก.

**Counter / Mitigation:** 2 ใน 3 ข้อกำหนดเป็นจุดแข็ง native: real-time analytics บนธุรกรรมสด + self-service BI ทำได้ในตัว (SuiteAnalytics Workbook/Saved Search/Dashboard). ข้อ DW จัดการตนเองตอบด้วย **NSAW บน Oracle Autonomous Database (auto-tune/auto-patch/auto-scale)** — แต่ NSAW เป็นโมดูลเสริม (Oracle เองก็ต้องใช้ OAC/ADW แยก). real-time + self-service ครอบคลุมงานมูลนิธิได้ในตัว; enterprise DW จัดการตนเองเป็น over-spec.

**Procurement caveat:** "Partial" เกิดจากผูกข้อกำหนด DW พรีเมียมเข้ามา ทั้งที่ Oracle ก็ต้องใช้ OAC/ADW แยกเช่นกัน.

**Confidence:** high

**หลักฐาน / Citation:**
- [WEB:netsuite.com] SuiteAnalytics — built-in real-time, no warehouse needed
- [WEB:houseblend.io] NSAW on Oracle Autonomous Data Warehouse (self-managing)
- [KB] Netsuite-SuiteAnalytics Workbook (0.63)

---

## TOR-TECH-03 — TOR: Embedded AI / GenAI across processes

- **Capability (TH):** AI/GenAI ฝังในกระบวนการธุรกิจหลัก (ผู้ช่วยอัจฉริยะ, anomaly detection, พยากรณ์, document IDR) โดยไม่ต้องต่อระบบภายนอก
- **Capability (EN):** Embedded AI/GenAI within core processes (intelligent assistants, anomaly detection, forecasting, document IDR) without external bolt-ons
- **Domain:** Technical · **iCE severity:** ต่ำ · **TOR verdict:** No · Important

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** anomaly detection และ forecasting อยู่ใน Intelligent Performance Management ของโมดูล NetSuite EPM ที่ต้องซื้อแยก (~$10k-25k/ปี) ไม่ใช่ base และยังตามหลัง Oracle ด้านความกว้าง/วุฒิภาวะ.

**Counter / Mitigation:** เรต "No/ทำไม่ได้เลย" แรงเกินจริง — **2 ใน 4 ความสามารถมี native จริง**: intelligent assistant (SuiteAnalytics Assistant + Text Enhance, native 2024.1-2025.1) และ document IDR (Bill Capture/Document AI, native). document IDR ช่วยงาน AP/จัดซื้อ/รับบริจาคได้ทันทีโดยไม่เพิ่มต้นทุน; anomaly/forecasting ต้องลงทุน EPM เพิ่ม — ต้องชั่งต้นทุนเทียบประโยชน์. ช่องว่างกับ Oracle เป็นเรื่องความกว้าง/วุฒิภาวะ + ต้นทุน add-on ไม่ใช่ "ไม่มี".

**Procurement caveat:** มัด 4 ความสามารถแล้วตัด "No" เป็นการบีบ NetSuite ให้ตก ทั้งที่ 2 ใน 4 มี native.

**Confidence:** high

**หลักฐาน / Citation:**
- [WEB:netsuite.com] NetSuite 2024.1 — Text Enhance, Bill Capture
- [WEB:netsuite.com] GenAI assistant 2025.1 (SuiteAnalytics Assistant)
- [WEB:netsuite.com] NetSuite EPM — Intelligent Performance Management (add-on)
- [WEB:docs.oracle.com] NetSuite Features That Use AI

---

## TOR-TECH-04 — TOR: Deployment / data residency options

- **Capability (TH):** ระบุทางเลือกการติดตั้ง (public/private/sovereign/in-country) และตำแหน่ง data center ที่รองรับ data residency ของหน่วยงาน
- **Capability (EN):** State deployment options (public/private/sovereign/in-country) and data-center locations meeting data-residency requirements
- **Domain:** Technical · **iCE severity:** สูง · **TOR verdict:** Partial · Mandatory

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** **จุดอ่อนจริงและปิดไม่ได้เชิงสถาปัตยกรรม** — NetSuite เป็น public multi-tenant SaaS เท่านั้น: ไม่มี data center ในไทย, ไม่มี private/sovereign region และไม่อยู่บน EU Sovereign Cloud. ต่างจาก gap อื่นในชุดนี้ที่ปิดได้ด้วย SuiteApp ข้อนี้เพิ่ม in-country/sovereign region ให้ NetSuite ไม่ได้. Oracle มีเส้นทาง in-country (AIS Cloud/Oracle Alloy ไทย).

**Counter / Mitigation:** NetSuite ระบุทางเลือกได้ว่าเป็น public multi-tenant SaaS บน data center หลายภูมิภาค (EU/NA/APAC) มี data residency เชิงภูมิภาค — ข้อกำหนดเพียง "ระบุทางเลือก" ซึ่ง NetSuite ทำได้ และ in-country ไทยไม่ใช่ข้อบังคับ PDPA. Fusion SaaS แบบ public มาตรฐานก็ไม่มี region ในไทยเช่นกัน. **severity สูง** เพราะแตะข้อมูลสุขภาพผู้ป่วย/ผู้บริจาคของบริบท healthcare/blood-bank — หากองค์กรกำหนด in-country/sovereign residency เป็นเงื่อนไข NetSuite จะเสียเปรียบและต้องเคลียร์ก่อน go-live.

**Procurement caveat:** TOR ขอเพียง "ระบุทางเลือก" ซึ่ง NetSuite ตอบได้ — การตี "Partial → region จำกัด" ประเมินต่ำ; แต่หากให้น้ำหนัก sovereignty ต้อง verify roadmap. [ต้อง verify in-country/sovereign roadmap]

**Confidence:** medium

**หลักฐาน / Citation:**
- [WEB:netsuite.com] NetSuite Data Center datasheet — multi-region, no Thai DC
- [WEB:sota.io] NetSuite not on Oracle EU Sovereign Cloud (Q1 2026) [ต้อง verify]
- [WEB:oracle.com] Public Cloud Regions; AIS Cloud/Oracle Alloy Thailand
- [WEB:securiti.ai] Thailand PDPA — no localization mandate

---

## TOR-TECH-05 — TOR: GRC / automated SoD controls

- **Capability (TH):** ควบคุมสิทธิ์การเข้าถึงแบบละเอียด + ตรวจ SoD อัตโนมัติ + continuous controls monitoring ในตัว
- **Capability (EN):** Fine-grained access control with automated SoD checks and built-in continuous controls monitoring
- **Domain:** Technical · **iCE severity:** สูง · **TOR verdict:** Partial · Important

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** NetSuite ไม่มี automated SoD เชิง preventive (block self-approval แบบ ruleset) และไม่มี continuous controls monitoring เป็น native — ต้องใช้ certified SuiteApp (Fastpath Assure, Netwrix Strongpoint, Greenlight Approvals) ปิดส่วน preventive ซึ่งเป็น market-standard.

**Counter / Mitigation:** NetSuite ทำ fine-grained access control ได้ในตัว และทำ SoD แบบ detective ได้ (saved search/role audit เช่นค้น creator=approver). **severity สูงเพราะ SoD อยู่ใต้การตรวจของ สตง. โดยตรง** — ต้องวางแผนจัดหา SuiteApp ปิด preventive SoD และออกแบบ control matrix ให้พร้อมก่อน go-live เพื่อผ่านการตรวจ. ส่วน CCM แบบ native เต็มรูปเป็นฟีเจอร์ระดับองค์กรข้ามชาติที่เป็น over-spec สำหรับ NGO ไทย.

**Procurement caveat:** บังคับ "continuous controls monitoring ในตัว native" = over-spec; SoD ที่องค์กรต้องการจริงทำได้ด้วย native (detective) + certified SuiteApp.

**Confidence:** high

**หลักฐาน / Citation:**
- [WEB:mysuite.tech] NetSuite SoD: detective vs preventive (native ไม่ block self-approval แบบ ruleset)
- [WEB:oracle.com] Oracle Risk Management Cloud — built-in continuous controls monitoring
- [WEB:suiteapp.com] Greenlight Approvals / Fastpath Assure — preventive self-approval blocking + automated SoD
- [KB] Netsuite-Managing Users & Roles (0.6544) — access review/audit guidance (manual)

---

## TOR-TECH-06 — TOR: Native iPaaS / integration platform

- **Capability (TH):** แพลตฟอร์มเชื่อมต่อ (iPaaS) ในตัว รองรับ pre-built adapters, API management, event-driven integration + throughput ระดับองค์กรโดยไม่ติดเพดาน API
- **Capability (EN):** Native iPaaS with pre-built adapters, API management, event-driven integration, and enterprise throughput without restrictive API limits
- **Domain:** Technical · **iCE severity:** ต่ำ · **TOR verdict:** Partial · Important

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** NetSuite ไม่มี iPaaS + API management รวมในแพ็กเกจเดียวแบบ native — มี REST/SOAP/RESTlets + SuiteScript + event hooks (User Event/Scheduled/Map-Reduce) และ pre-built connectors ผ่าน SuiteApp แต่ยังติด concurrency governance.

**Counter / Mitigation:** ทำ event-driven integration ได้ในตัว (event hooks) มี pre-built connectors ผ่าน SuiteApp/Connector. **Oracle OIC ที่อ้างเป็น iPaaS เต็มรูปก็เป็นไลเซนส์แยกคิดตาม message เช่นกัน** — ไม่ฟรีในตัว ERP. งาน integration จริง (HIS/ระบบเฉพาะทาง/ธนาคาร) ใช้ REST/SOAP/RESTlet ในตัวรองรับได้ตามสเกล เสริม iPaaS พาร์ทเนอร์เมื่อจำเป็น.

**Procurement caveat:** มัด "iPaaS ในตัว + ไม่มีเพดาน API" เข้าด้วยกัน = over-spec/ล็อกสเปก เพราะ OIC ก็ไลเซนส์แยก.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-SuiteCloud Platform Introduction (0.647)
- [KB] Netsuite-SuiteTalk REST Web Services (0.685)
- [WEB:erpresearch.com] OIC เป็นไลเซนส์แยกจาก Fusion ERP คิดตาม message (ยืนยันมีจริง)
- [WEB:docs.oracle.com] NetSuite Help — Concurrency Governance Limits

---

## TOR-TECH-07 — TOR: Native master data management (MDM)

- **Capability (TH):** Master Data Management + data governance ในตัว รองรับ data stewardship, การควบคุมคุณภาพข้อมูล และ federation ข้ามโดเมน
- **Capability (EN):** Native MDM and data governance supporting data stewardship, data-quality controls, and cross-domain federation
- **Domain:** Technical · **iCE severity:** แทบไม่มีผล · **TOR verdict:** No · Important

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** NetSuite ไม่มี MDM hub แบบ cross-domain federation เป็น native — มีเครื่องมือ data stewardship/data-quality ระดับใช้งานได้ (Duplicate Detection, Record Merge/EntityDeduplicationTask, audit trail, role/field-level security) แต่ไม่มี federation ข้ามโดเมน.

**Counter / Mitigation:** ตี "No (ทำไม่ได้เลย)" เกินจริง — มีงาน governance/data-quality ในตัว. federation ข้ามโดเมนเป็นความต้องการของ enterprise หลายระบบ และ **Oracle เองก็ทำผ่าน Customer/Product/Supplier Hub โมดูลแยก** ไม่ใช่ in-the-box. องค์กรที่ใช้ ERP เดียวไม่มี use case federation ข้ามหลายระบบ.

**Procurement caveat:** MDM hub ในตัว = over-spec/ล็อกสเปก และเป็นเกณฑ์ที่ Oracle เองก็ตอบด้วยโมดูลแยก.

**Confidence:** medium

**หลักฐาน / Citation:**
- [KB] NetSuite Basics — Duplicate Record Detection (0.65)
- [KB] Netsuite-SuiteScript 2.0 API Reference — EntityDeduplicationTask (0.682)
- [WEB:oracle.com] Oracle MDM = Customer/Product/Supplier Hub (โมดูลแยก)
- [WEB:netsuite.com] Governance, Risk & Compliance — audit trail/field-level security (รวมใน platform license, ยืนยันแล้ว)

---

## TOR-TECH-08 — TOR: Architecture / infrastructure foundation

- **Capability (TH):** อธิบายสถาปัตยกรรมฐานข้อมูลและการดูแลอัตโนมัติ (auto-tuning/patching/scaling/security) ที่ลดภาระ DBA และ TCO
- **Capability (EN):** Describe database architecture and autonomous operations (auto-tuning/patching/scaling/security) reducing DBA effort and infrastructure TCO
- **Domain:** Technical · **iCE severity:** แทบไม่มีผล · **TOR verdict:** Partial · Optional

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** (TOR ตี NetSuite เป็น "black-box multi-tenant" เทียบ Oracle Autonomous Database — แต่ข้อกล่าวอ้างนี้ล้าสมัย.)

**Counter / Mitigation:** **differentiator ล้าสมัย** — NetSuite ย้ายไปรันบน Oracle Autonomous Database (ประกาศ SuiteConnect ก.พ. 2025) จึงได้ auto-tuning / zero-downtime patching / auto-scaling / auto-security ในตัว และในฐานะ SaaS เต็มรูป ลูกค้าไม่ต้องมี DBA — ตรงเป้าหมายข้อกำหนด (ลดภาระ DBA/TCO). อีกทั้ง requirement นี้ priority Optional ยิ่งไม่ใช่ตัวตัดสิน.

**Procurement caveat:** "Autonomous DB เป็นของ Oracle เจ้าเดียว / NetSuite เป็น black-box" ผิดข้อเท็จจริง — NetSuite รันบน Autonomous Database เดียวกัน.

**Confidence:** high

**หลักฐาน / Citation:**
- [WEB:prnewswire.com] NetSuite Migrates to Oracle Autonomous Database (Feb 2025)
- [WEB:accountingtoday.com] NetSuite migrates suite to AI self-maintaining database
- [WEB:oracle.com] Autonomous Database features (auto-tune/patch/scale/secure)

---

*End of cross-cutting KB. All client identities generalised to healthcare / blood-bank / non-profit-foundation / public-sector patterns per iCE anti-name-drop policy. Product positions dated mid-2026 — re-verify yearly (see `ams_review`). Records marked [ต้อง verify] require live-environment / vendor confirmation before commitment.*
