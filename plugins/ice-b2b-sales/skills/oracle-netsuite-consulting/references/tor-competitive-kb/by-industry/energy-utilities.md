---
last_verified: "2026-06-29"
source: "TOR Requirement Bank + Gap Pack v2"
confidence_note: "แหล่งข้อมูลตั้งต้นเป็นชุดร่าง TOR เชิงแข่งขันที่ออกแบบให้ NetSuite ตอบได้เพียง Partial/No และ Oracle Fusion ตอบ Fully — มิใช่การวิเคราะห์ความต้องการที่เป็นกลาง. KB นี้จึงเก็บทั้ง 'ช่องว่าง (Gap)' และ 'มุมมองโต้แย้ง/แนวทางปิด (Counter/Mitigation)' ควบคู่กัน ระดับ Confidence ของแต่ละข้อยึดจากการมี/ไม่มี KB หรือ citation ทางการในบันทึกต้นทาง. The source is a Fusion-biased competitive TOR draft; every record preserves both the gap and iCE's balanced counter-view."
ams_review: "yearly — re-verify product positions"
---

# TOR Competitive KB — energy-utilities — NetSuite Weakness & Counter

**บริบทการใช้งาน / Usage context:** ใช้ชุดความรู้นี้เมื่อ iCE เสนอขาย NetSuite หรือปกป้อง NetSuite จากร่าง TOR ที่เอียงไปทาง Oracle Fusion ในกลุ่มอุตสาหกรรม **energy-utilities** — โดยเฉพาะเมื่อ TOR ผลักดันสเปกด้านการบริหารสินทรัพย์/ซ่อมบำรุงองค์กร (EAM) และการรายงานความยั่งยืน/ESG. แต่ละหัวข้อระบุจุดที่ NetSuite เสียเปรียบจริง คู่กับแนวทางปิดช่องว่างด้วย first-party add-on / certified SuiteApp / custom หรือข้อโต้แย้งเชิง over-spec ตามระเบียบวิธี Second Opinion ของ iCE.

> **หมายเหตุการอ้างอิงอุตสาหกรรม / Industry generalization:** บันทึกต้นทางอ้างถึงหน่วยงานเฉพาะราย (องค์กรสาธารณกุศล/ธนาคารเลือด/หน่วยผลิตชีววัตถุภาครัฐ). ใน KB นี้ได้ทำให้เป็นรูปแบบทั่วไป (generalized) เป็น healthcare / blood-bank / non-profit foundation / public-sector patterns เพื่อความเป็นกลางและนำไปใช้ซ้ำได้ ไม่ระบุชื่อลูกค้ารายใด. Records here are generalized to healthcare / public-sector / non-profit asset-maintenance and cold-chain equipment patterns — no client name is used.

---

## GP-FUNC-23 — Enterprise Asset Management & maintenance (EAM)

**Capability (TH):** บริหารสินทรัพย์/ซ่อมบำรุงองค์กร (EAM)
**Capability (EN):** Enterprise Asset Management & maintenance (EAM)

**Domain + iCE severity:** Asset · ระดับความรุนแรง (iCE) = **กลาง (medium)**
*Vendor scoring in source: NetSuite 1★ · Oracle Fusion 4★ · SAP S/4HANA 5★ · Gap Severity (source) = High · Fusion เด่นสุด ✔*

**จุดที่ NetSuite สู้ไม่ได้ (Gap):**
Base FAM (Fixed Assets Management — เป็น SuiteApp) ทำได้เฉพาะการคิดค่าเสื่อมราคา/ตีราคาใหม่/จำหน่าย และเก็บ maintenance schedule กับ insurance เท่านั้น — **ไม่มี work order.** สำหรับงานบริหารสินทรัพย์/ซ่อมบำรุงระดับโรงงานหนัก (linear asset, reliability-centered maintenance) SAP PM/EAM ยังลึกที่สุด และ Oracle Maintenance Cloud แข็งแรงกว่า. ร่าง TOR จึงจัด NetSuite ไว้ที่ 1★ พร้อมระบุว่า "FAM = แค่ fixed-asset depreciation; ไม่มี maintenance/work order."

**Counter / Mitigation:**
เรต 1★ ต่ำกว่าความจริง. NetSuite มี **NetSuite Field Service Management (FSM)** ซึ่งเป็นผลิตภัณฑ์ **first-party** หลัง Oracle เข้าซื้อ Next Technik ในเดือน ต.ค. 2023 (เดิมชื่อ NextService) — เพิ่มความสามารถ work order, preventive maintenance ตามเวลา/การใช้งาน (meter-based: ชั่วโมง/ไมล์/รอบ → สร้างงานซ่อมอัตโนมัติ), asset hierarchy/sub-asset และ maintenance history. FSM เป็นโมดูลที่ต้องซื้อแยกและเอียงไปทาง field service. แนวทางปิดช่องว่าง:
- **First-party add-on:** เพิ่มโมดูล NetSuite FSM เพื่อครอบ work order + preventive/usage-based maintenance + asset hierarchy + maintenance history (มีต้นทุน license ต้องวางแผน).
- **Interface option:** สำหรับงานบำรุงรักษาครุภัณฑ์การแพทย์/แล็บ/อุปกรณ์ cold-chain องค์กรกลุ่ม healthcare มักใช้ biomedical CMMS เฉพาะทางแล้วต่อเชื่อมกับ NetSuite.
- **Over-spec rebuttal:** EAM โรงงานหนัก/linear asset/reliability ระดับ SAP PM เป็น over-spec สำหรับองค์กร healthcare/public-sector/non-profit ที่ไม่ได้เดินไลน์อุตสาหกรรมหนัก — ความต้องการจริงคือ PM ครุภัณฑ์และอุปกรณ์ cold-chain ซึ่ง FSM ปิดได้.

**Procurement caveat:**
การเขียน requirement ให้ต้องมี "EAM เต็มรูปแบบระดับโรงงาน (predictive/condition-based, linear asset, reliability)" มีความเสี่ยงเป็นการล็อกสเปกไปทางผลิตภัณฑ์เฉพาะ (SAP PM/Oracle Maintenance Cloud) เกินภารกิจจริงขององค์กรกลุ่มนี้ — ควรเขียนแบบอิงผลลัพธ์ (outcome-based: "รองรับ work order + preventive/usage-based maintenance + maintenance history ของครุภัณฑ์และอุปกรณ์ cold-chain") เพื่อลดความเสี่ยงถูกท้วงติงเรื่องความเป็นธรรมในการจัดซื้อจัดจ้าง (สตง.).

**Confidence:** high — บันทึกต้นทางระบุ [ความเชื่อมั่น: สูง] และมี KB + citation ทางการหลายรายการ.

**หลักฐาน / Citation:**
- [KB] Netsuite-Fixed Assets Management (0.60) — depreciation + maintenance schedule/insurance, ไม่มี work order
- [WEB:netsuite.com] NetSuite Field Service Management — work orders, automated preventive maintenance, asset hierarchy
- [WEB:netsuite.com] FSM datasheet — usage/meter-based maintenance (hours/mileage/cycles) auto-generates jobs
- [WEB:oracle.com] Oracle acquires Next Technik — FSM กลายเป็น first-party (2023)

---

## GP-FUNC-28 — Sustainability / ESG reporting

**Capability (TH):** รายงานความยั่งยืน / ESG
**Capability (EN):** Sustainability / ESG reporting

**Domain + iCE severity:** ESG · ระดับความรุนแรง (iCE) = **แทบไม่มีผล (negligible)**
*Vendor scoring in source: NetSuite 1★ · Oracle Fusion 4★ · SAP S/4HANA 4★ · Gap Severity (source) = Med · Fusion เด่นสุด ✔*

**จุดที่ NetSuite สู้ไม่ได้ (Gap):**
NetSuite ยังไม่มีโมดูล ESG/sustainability แบบเนทีฟเชิงลึก — ข้อกล่าวอ้างเรื่อง gap นี้ถูกต้อง. Oracle และ SAP มีโมดูล sustainability/ESG ในตัวมากกว่า. ร่าง TOR ระบุว่า NetSuite "ยังจำกัด."

**Counter / Mitigation:**
NetSuite ปิดความต้องการรายงาน ESG/ความยั่งยืนได้ผ่านหลายเส้นทางแม้ไม่มีโมดูลเนทีฟเชิงลึก:
- **First-party analytics/planning:** ใช้ data model ที่ยืดหยุ่นของ NetSuite ร่วมกับ **NSPB** (NetSuite Planning & Budgeting) และ **NSAW** (NetSuite Analytics Warehouse) + custom report เพื่อรวบรวมและรายงานตัวชี้วัด.
- **Certified SuiteApp:** ปิด gap การคำนวณคาร์บอน/ESG ด้วย SuiteApp ภายนอก — **Carbon Accounting for NetSuite (Built for NetSuite, โดย CarbonSuite)** และ **RSM ESG Reporting Package for NetSuite**; ทิศทางใหม่รองรับ ISSB/IFRS S1-S2 ผ่าน partner.
- **Over-spec rebuttal:** การรายงาน ESG/ความยั่งยืนภาคบังคับ (CSRD/GRI/ISSB assurance) มุ่งเป้าไปที่บริษัทจดทะเบียน/ข้ามชาติ ไม่ใช่องค์กรสาธารณกุศล/public-sector — สำหรับองค์กรกลุ่มนี้การเปิดเผย ESG มักเป็นเชิงสมัครใจ (เพื่อผู้บริจาค/ผู้มีส่วนได้ส่วนเสีย) จึงเป็น over-spec หากบรรจุเป็นข้อบังคับใน TOR.

**Procurement caveat:**
บันทึกต้นทางชี้ชัดว่าการบรรจุ ESG reporting ภาคบังคับใน TOR = over-spec สำหรับองค์กรที่ไม่อยู่ในขอบเขตการเปิดเผย ESG ภาคบังคับ — การผูกเป็น mandatory requirement มีความเสี่ยงเป็นการตั้งสเปกเทียบระดับ tier-1 เกินภารกิจจริง; หากต้องการรายงานเชิงสมัครใจ ควรเขียนแบบอิงผลลัพธ์ (outcome-based) ไม่ผูกกับโมดูลเนทีฟของผลิตภัณฑ์ใดผลิตภัณฑ์หนึ่ง.

**Confidence:** medium — บันทึกต้นทางระบุ [ความเชื่อมั่น: กลาง]; หลักฐานเป็น citation ทางเว็บ (SuiteApp/vendor) ไม่มี KB score เชิงลึก.

**หลักฐาน / Citation:**
- [WEB:suiteapp.com] Carbon Accounting for NetSuite (Built for NetSuite)
- [WEB:rsmus.com] RSM ESG Reporting Package for NetSuite
- [WEB:netsuite.com] A Guide to ESG

---

## TOR-EAM-01 — TOR: Enterprise asset management & maintenance

**Capability (TH):** ระบบต้องมีการบริหารสินทรัพย์และซ่อมบำรุง (Enterprise Asset Management) รองรับ work order, preventive/predictive maintenance, meter reading และประวัติการบำรุงรักษา
**Capability (EN):** The solution shall provide Enterprise Asset Management (EAM) with work orders, preventive/predictive maintenance, meter readings, and maintenance history.

**Domain + iCE severity:** Asset / EAM (Type: Functional · Priority: Important) · ระดับความรุนแรง (iCE) = **กลาง (medium)**
*Source verdict: NetSuite ตอบได้? = No · Differentiator note: "NetSuite FAM = depreciation เท่านั้น → No; SAP PM/EAM เด่น, Oracle Maintenance Cloud แข็ง ✔"*

**จุดที่ NetSuite สู้ไม่ได้ (Gap):**
base FAM ของ NetSuite ทำได้แค่ค่าเสื่อมราคา — **ไม่มี work order.** ร่าง TOR จึงตัดสินให้ NetSuite ตอบ "No" ต่อข้อกำหนด EAM ที่ต้องการ work order + preventive/predictive maintenance + meter reading + maintenance history โดยชูว่า SAP PM/EAM เด่นและ Oracle Maintenance Cloud แข็งแรง.

**Counter / Mitigation:**
การให้ผล "No" เกินจริง — ควรเป็น **Partial** ไม่ใช่ No:
- **First-party add-on:** เมื่อซื้อโมดูลแยก **NetSuite Field Service Management (FSM, first-party หลังซื้อ Next Technik 2023)** NetSuite จะตอบข้อกำหนด TOR ส่วน work order, preventive maintenance (ตามเวลา/usage), asset hierarchy และ maintenance history ได้; meter/usage-based (ชั่วโมง/ไมล์/รอบ) สร้าง work order อัตโนมัติได้.
- **ข้อจำกัดที่ต้อง honest-flag:** FSM เอียงไปทาง field service และ **ไม่ใช่ predictive/condition-based EAM เต็มรูป** — ยืนยันได้เฉพาะ preventive + usage-based (บันทึกต้นทางตัดคำว่า "predictive" ออกจากร่างโดยเจตนา). งาน EAM โรงงานหนัก/linear asset ยังเป็นของ SAP PM จริง.
- **Over-spec rebuttal:** full plant EAM / predictive maintenance เป็น over-spec สำหรับองค์กร healthcare/public-sector ที่ความต้องการจริงคือ PM ครุภัณฑ์และอุปกรณ์ cold-chain — ซึ่ง FSM (ที่ต้องลงทุนเพิ่ม) ปิดได้.

**Procurement caveat:**
ข้อกำหนดคำว่า "predictive maintenance" ในตัว TOR เป็นจุดที่ควรระวัง — การผูกคำว่า predictive/condition-based EAM เต็มรูปทำให้ NetSuite (และผู้เสนอที่ใช้ FSM) เสียเปรียบทั้งที่งานจริงต้องการเพียง preventive + usage-based. เพื่อความเป็นธรรมและลดความเสี่ยงถูกท้วงติง (สตง./ผู้ยื่นรายอื่น) ควรปรับ requirement ให้อิงผลลัพธ์ตามภารกิจจริง (work order + preventive/usage-based maintenance + meter reading + maintenance history) และเปิดให้ตอบแบบ Partial ที่ปิดด้วยโมดูลเสริมได้ ไม่ล็อกไปที่ predictive/condition-based ของผลิตภัณฑ์เฉพาะราย.

**Confidence:** high — บันทึกต้นทางระบุ [ความเชื่อมั่น: สูง] และมี KB + citation ทางการหลายรายการ.

**หลักฐาน / Citation:**
- [KB] Netsuite-Fixed Assets Management (0.60) — base FAM = depreciation + maintenance schedule, ไม่มี work order
- [WEB:netsuite.com] NetSuite Field Service Management — work orders, automated preventive maintenance, asset hierarchy
- [WEB:netsuite.com] FSM datasheet — usage/meter-based maintenance auto-generates work orders
- [WEB:oracle.com] Oracle acquires Next Technik — FSM กลายเป็น first-party (2023)

---

*KB generated for iCE Consulting competitive-TOR practice · product angle: NetSuite weakness + counter · industry vertical: energy-utilities · 3 records (GP-FUNC-23, GP-FUNC-28, TOR-EAM-01). Client identities generalized to healthcare/public-sector/non-profit patterns per anti-name-drop rule. Preserve both gap and counter — re-verify product positions yearly (AMS).*
