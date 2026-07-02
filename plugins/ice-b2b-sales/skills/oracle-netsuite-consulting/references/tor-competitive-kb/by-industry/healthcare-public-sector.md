# TOR Competitive KB — healthcare-public-sector — NetSuite Weakness & Counter

---
last_verified: "2026-06-29"
source: "TOR Requirement Bank + Gap Pack v2"
confidence_note: >
  ชุดข้อมูลต้นทางเป็น "ร่าง TOR เชิงแข่งขัน" ที่ออกแบบให้ NetSuite ตอบได้เพียง Partial/No และ Oracle Fusion
  ตอบ Fully (ระบุไว้ชัดใน README ของต้นฉบับ) จึงไม่ใช่การวิเคราะห์ความต้องการที่เป็นกลาง. KB ฉบับนี้เก็บทั้ง
  (ก) จุดที่ NetSuite สู้ไม่ได้จริง และ (ข) มุมมองถ่วงดุลของ iCE — first-party add-on (NSPB / NetSuite Account
  Reconciliation / NSAW), certified SuiteApp, custom หรือข้อโต้แย้ง over-spec/ล็อกสเปก. ระดับ Confidence ของแต่ละ
  record อิงว่ามี KB/เอกสารทางการรองรับหรือไม่ (verbatim ในหัวข้อ "หลักฐาน / Citation"). รายการที่ติดป้าย
  [ต้อง verify] ต้องยืนยันกับ environment จริง/ผู้ขายก่อนตัดสินใจ. This KB is a COUNTER kit used when iCE SELLS
  or DEFENDS NetSuite against a Fusion-biased TOR — not a concession sheet.
ams_review: "yearly — re-verify product positions"
generalization_note: >
  ต้นฉบับอ้างถึงองค์กรเฉพาะราย — KB ฉบับนี้ generalize เป็นรูปแบบอุตสาหกรรม healthcare / blood-bank service /
  biologics (serum-vaccine) production under GMP / non-profit foundation / public-sector ที่อยู่ภายใต้การตรวจของ
  สำนักงานการตรวจเงินแผ่นดิน (สตง.). ไม่มีการระบุชื่อหน่วยงานใด ๆ ในเอกสาร.
---

> **วิธีอ่าน / How to use** — แต่ละ record มี (1) จุดที่ NetSuite สู้ไม่ได้ (Gap) ตามต้นฉบับ, (2) Counter /
> Mitigation ที่ iCE ใช้ป้องกัน, (3) Procurement caveat เมื่อการล็อกสเปกมีความเสี่ยงถูก สตง./ผู้ยื่นรายอื่น
> ท้วงติง, (4) Confidence และ (5) Citation แบบ verbatim. สำหรับกลุ่ม healthcare-public-sector จุดอ่อน "จริงและ
> ปิดยาก" มีเพียงไม่กี่ข้อ (data residency/sovereignty, GMP electronic batch record, preventive-SoD/CCM, e-Tax
> Invoice XML); ที่เหลือส่วนใหญ่ปิดได้ด้วย first-party add-on/SuiteApp หรือเป็น over-spec ของงานสาธารณกุศล/นิติ
> บุคคลเดียวในไทย.

---

## F-EPM-01 — Driver-based planning & budgeting (xP&A)

**Capability (TH):** การวางแผน/งบประมาณแบบ driver-based
**Capability (EN):** Driver-based planning & budgeting
**Domain:** EPM · **iCE severity:** ต่ำ

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** ERP แกนของ NetSuite ไม่มี predictive/multi-scenario planning ในตัว; NSPB
เป็น OEM ตัดทอนของ Oracle PBCS และปัจจุบันมีเฉพาะโมดูล Financials — ยังไม่มีโมดูล Workforce/Capital สำเร็จรูป
(Oracle Help ระบุชัด "A Workforce module is not currently available"). Oracle EPM Cloud (EPBCS) มี planning
ครบทุกมิติในตัว.

**Counter / Mitigation:** ข้ออ้าง "ไม่มี predictive/scenario" ไม่จริง — NetSuite Planning and Budgeting (NSPB)
เป็น **first-party add-on** ที่สร้างบนเอนจิน Oracle PBCS/Hyperion เดียวกับ Oracle EPM Cloud รองรับ driver-based,
what-if/multi-scenario, Predictive Planning และ rolling forecast พร้อม sync GL อัตโนมัติ. สำหรับ healthcare/
public-sector ที่มี รพ./ศูนย์บริการโลหิต/หน่วยผลิตชีววัตถุ การวาง headcount/capex ทำผ่าน driver-based ใน NSPB
Financials ได้ ไม่จำเป็นต้องมีโมดูล Workforce/Capital สำเร็จรูป + predictive multi-scenario ระดับ enterprise
ซึ่งเป็น over-spec. ข้อจำกัดจริง = NSPB เป็นลิขสิทธิ์แยก (ต้องตั้งงบ) ไม่ใช่ "ขาด core".

**Procurement caveat:** การบังคับ "native driver-based platform … without any external tool" ในเชิงเทคนิคก็ยัง
คลุมด้วย NSPB ได้ (เป็นแอปในตระกูล NetSuite) แต่ถ้อยคำ "ในตัว/ไม่มีเครื่องมือภายนอกใด ๆ" มีลักษณะบีบให้เข้าหา
suite เดียว — ควรเขียนแบบ outcome-based (วางงบ driver-based + scenario ได้) เพื่อลดความเสี่ยงล็อกสเปก.

**Confidence:** high

**หลักฐาน / Citation:**
- [WEB:docs.oracle.com] NetSuite Planning and Budgeting — 'Planning and Budgeting currently supports only the Financials module. A Workforce module is not currently available.' (article_8124016549 — ตรวจแล้วมีจริง/ยังอัปเดต)
- [WEB:docs.oracle.com] NetSuite Planning and Budgeting Financials Overview — driver-based/trend-based/direct-input accounts, what-if scenarios, Predictive Planning (article_7160253896 — ตรวจแล้วมีจริง)
- [WEB:netsuite.com] What is NetSuite Planning and Budgeting — scenario plans / what-if / driver-based, built on Oracle EPM (financial-planning.shtml)
- [KB] Netsuite-Statistical Accounting / Netsuite-General Accounting (~0.6) — base NetSuite มีเพียง GL budget + statistical allocation; KB ไม่มีเอกสาร NSPB เฉพาะ บ่งชี้ว่า xP&A เต็มต้องใช้ add-on

---

## F-EPM-04 — Multidimensional profitability & activity-based costing

**Capability (TH):** การวิเคราะห์กำไร/ต้นทุนหลายมิติ
**Capability (EN):** Multidimensional profitability & costing
**Domain:** EPM · **iCE severity:** ต่ำ

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** NetSuite core ไม่มี ABC engine วิเคราะห์กำไร/ต้นทุนหลายมิติเต็มรูปแบบ —
ABC/profitability หลายมิติระดับ Oracle PCMCS ต้องซื้อโมดูล add-on แยก.

**Counter / Mitigation:** ข้ออ้าง "ไม่มี engine" เกินจริง. Native มี Allocation Schedules (ทั้ง Fixed และ Dynamic)
ปันส่วนข้าม account/department/class/location/custom segment ถ่วงน้ำหนักด้วย Statistical Accounts ซึ่ง NetSuite
Help ระบุเองว่า "useful in advanced costing such as Activity Based Costing and Usage Based Costing" บวก Custom
Segments หลายมิติและ Project Profitability. ABC engine เต็มรูปมีโมดูล **first-party NetSuite Profitability &
Cost Management (NSPCM)** ใน NetSuite EPM (แพลตฟอร์มเดียวกับ Oracle PCMCS/Hyperion). สำหรับงานการกุศล/สาธารณะ
การปันส่วนต้นทุนทางอ้อมเข้าโปรแกรม/กองทุน/cost center ทำได้ด้วย native allocation เพียงพอ — ABC engine ระดับ
PCMCS แบบ native ในตัวเป็น over-spec.

**Procurement caveat:** การบังคับ "native multidimensional ABC engine" ใน TOR ผูกสเปกเข้าหา PCMCS-class product —
ควรระบุผลลัพธ์ (ปันส่วนต้นทุนเข้าโปรแกรม/กองทุนได้) แทน.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-General Accounting (0.59) — Allocation Schedules ปันส่วนข้าม account/department/class/location/custom segment
- [KB] Netsuite-Statistical Accounting (0.60) — Dynamic Allocation ถ่วงน้ำหนักด้วย Statistical Account
- [KB] Netsuite-Projects (0.50) — Project Profitability / Job Costing
- [WEB:docs.oracle.com] NetSuite Help — Working with Allocation Schedules Weighted by the Balance of a Statistical Account (chapter_3866895958): ระบุชัด 'useful in advanced costing such as Activity Based Costing and Usage Based Costing' — verified
- [WEB:netsuite.com] NetSuite Profitability and Cost Management (EPM add-on) — ABC/driver-based allocation, profitability หลายมิติ (product page verified, ขายคู่กับ NetSuite ERP เท่านั้น)
- [WEB:oracle.com] Oracle PCMCS — Profitability & Cost Management (สาย EPM/Hyperion เดียวกับ NSPCM, อ้างเป็น lineage)

---

## F-SCM-01 — Demand/supply planning & S&OP

**Capability (TH):** Demand & Supply Planning + S&OP
**Capability (EN):** Demand/supply planning & S&OP
**Domain:** SCM · **iCE severity:** ต่ำ

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** NetSuite มี Demand Planning/Supply Planning/DRP ในตัว (ภายใต้ Advanced
Inventory) พร้อมพยากรณ์เชิงสถิติ 4 วิธี (Linear Regression/Moving Average/Seasonal Average/Sales Forecast) แต่
เป็นวิธีพื้นฐาน ไม่มี demand sensing/ML และไม่มี S&OP (Sales & Operations Planning) ระดับองค์กรแบบ Oracle SCP
Cloud — S&OP enterprise คือ gap จริง.

**Counter / Mitigation:** คะแนน "1 (ต้อง add-on/custom)" เหมารวมเกินไป: งานวางแผนอุปสงค์/อุปทานพื้นฐาน NetSuite
ทำได้ **native** ในตัว. สำหรับ blood-bank service / biologics ที่ต้องพยากรณ์ความต้องการเลือด/เซรุ่ม native
demand planning พอใช้ตามสเกล (เลือดอายุสั้นอาจต้องปรับแต่งวิธีพยากรณ์/custom) ส่วน S&OP เต็มรูปแบบเชื่อมแผนขาย-
ผลิต-การเงินเกินความจำเป็นขององค์กรสาธารณกุศล.

**Procurement caveat:** S&OP/IBP เป็นครึ่งเดียวของข้อกำหนดและเป็นส่วนที่ over-spec — การมัดรวมกับ demand planning
พื้นฐานแล้วให้ Mandatory เป็นเทคนิคล็อกสเปก; แยกสองส่วนออกจากกัน.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-Inventory Management (0.69) — Demand Planning เป็นฟีเจอร์ในตัว + Distribution Resource Planning + projection methods
- [KB] NSIMG (0.66) — Demand Plans/Supply Plans, Seasonal Average method, Supply Allocation หลาย location
- [WEB:docs.oracle.com] NetSuite Applications Suite — Calculating Item Demand (4 วิธีพยากรณ์เชิงสถิติ native, /ns-online-help/section_N2290234.html)

---

## F-MFG-01 — Process / mixed-mode manufacturing (recipe, batch genealogy, GMP)

**Capability (TH):** Process / Mixed-mode Manufacturing
**Capability (EN):** Process / mixed-mode manufacturing
**Domain:** Manufacturing · **iCE severity:** สูง

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** ฐานมาตรฐานทำได้แค่ light discrete; งาน process manufacturing (สูตร/recipe,
batch genealogy, co-product) ต้องซื้อโมดูลเสริม NetSuite Advanced Manufacturing; lot/expiry เป็น native แต่ FEFO
มาเป็น SuiteApp ที่ต้องติดตั้ง. **ที่ขาดจริงและปิดยากคือ process mfg ระดับ GMP/ชีววัตถุเข้ม (electronic batch
record เชิง regulatory, potency)** ซึ่งไม่มีในตัว.

**Counter / Mitigation:** NetSuite Advanced Manufacturing (โมดูลเสริม) มี Recipe/Formulation Management (ระดับ
Manufacturing Workbench) และ co-product/by-product ในตัว; lot/batch + วันหมดอายุ + traceability เป็น native
(co-product สื่อตรงกับการแยกส่วนประกอบโลหิต: เลือดรวม→เม็ดเลือดแดง/พลาสมา/เกล็ดเลือด). สำหรับ GMP electronic
batch record + potency ของหน่วยผลิตเซรุ่ม/วัคซีน ต้องเสริม **custom SuiteScript หรือ SuiteApp นอก (blendAPPS/
BatchMaster)** — เป็นงานวางแผนปิด gap ก่อน go-live ไม่ใช่ blocker เชิงเทคนิคทั้งก้อน. งาน lot/expiry/co-product
พื้นฐานของ blood-bank service ยังเพียงพอ; process mfg อุตสาหกรรมเต็มรูปเกี่ยวน้อย.

**Procurement caveat:** ระบุ requirement เฉพาะสิ่งที่ใช้จริง (GMP batch record + lot/expiry/traceability) แทน
"mixed-mode manufacturing เต็มรูป" ที่ดึงเข้าหา SAP PP-PI/Oracle Manufacturing Cloud โดยไม่มี use case ครบ.

**Confidence:** medium (ต้นฉบับระบุ [ความเชื่อมั่น: กลาง])

**หลักฐาน / Citation:**
- [KB] Netsuite-Advanced Manufacturing User Guide (Setting up an Assembly CoProduct 0.62)
- [KB] NSIMG/Inventory Management (FEFO Lot Allocations SuiteApp 0.69)
- [WEB:docs.oracle.com] Lot Numbered Items / Lot and Serial Number Trace
- [WEB:suiteapp.com] blendAPPS Formula & Recipe Management (ยืนยันว่า process/recipe ลึกมักใช้ SuiteApp นอก)

---

## F-WMS-01 — Directed warehouse operations (WMS)

**Capability (TH):** Warehouse Management แบบ directed operations
**Capability (EN):** Directed warehouse operations
**Domain:** SCM · **iCE severity:** กลาง

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** NetSuite WMS เป็น SuiteApp ที่ต้องซื้อ license แยก (ไม่รวมในฐาน ERP) และวาง
ตำแหน่งสำหรับปริมาณงานต่ำ-กลาง; ที่อ่อนกว่า Oracle WMS Cloud/SAP EWM จริงคือ slotting optimization และ labor
management เชิงวิศวกรรม (engineered standards/yard/automation).

**Counter / Mitigation:** ข้ออ้าง "ไม่มี wave ขั้นสูง" คลาดเคลื่อน — directed put-away, wave/zone release, RF
barcode, cycle count เป็น **native ของ WMS SuiteApp (first-party)**. สำหรับ blood-bank/biologics งาน directed
put-away คุมอุณหภูมิ, RF/barcode, lot/expiry ตรงกับศูนย์บริการโลหิต/หน่วยผลิตชีววัตถุ; ต้องตั้งงบซื้อ WMS
SuiteApp. slotting/labor ระดับ DC พาณิชย์แทบไม่มี use case (over-spec).

**Procurement caveat:** เขียน requirement ให้ครอบ directed put-away/wave/RF/lot-expiry (ที่ใช้จริง) มากกว่า
"labor management/slotting engineered standards" ที่เอียงเข้าหา tier-1 WMS.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] WMS4-WMS Outbound Fulfillment (0.65) — Create a Wave/Template/Location
- [KB] WMS Advanced Setup (0.60) — Pick zones, Picking/Replenishment/Staging Strategies
- [WEB:netsuite.com] NetSuite WMS product page — mobile RF barcode, putaway/picking strategies, wave release
- [WEB:houseblend.io] NetSuite WMS Setup, Mobile RF & Wave Picking — zone picking, directed putaway, task/labor KPIs

---

## F-PRC-02 — Supplier qualification / SRM portal

**Capability (TH):** Supplier Qualification / SRM Portal
**Capability (EN):** Supplier management portal
**Domain:** Procurement · **iCE severity:** กลาง

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** ส่วน supplier qualification/onboarding (แบบสอบถาม/ขึ้นทะเบียนผู้ขาย) อ่อนจริง
ต้องใช้ SuiteApp พาร์ทเนอร์หรือ custom; vendor performance predictive score ผูกกับ Supply Chain Control Tower
(โมดูลเสริม) และ quality rejection ต้องใช้โมดูล Quality Management — ไม่ใช่ scorecard 4 KPI สำเร็จรูป.

**Counter / Mitigation:** "ไม่มี performance ครบ" เกินจริง — building block ของ vendor performance มี native/
คอนฟิกได้: portlet On-Time Delivery Performance / Vendor Return Amount เป็น native และทำ scorecard ได้จาก
**custom KPI/saved search**. ส่วน qualification/onboarding ปิดด้วย **certified SuiteApp (เช่น Gatekeeper)**.
สำหรับ biologics ที่ต้อง supplier qualification เชิง GMP เป็นจุดที่ NetSuite อ่อนจริง — ต้องวางแผน SuiteApp/
custom ก่อน go-live (ไม่ใช่จุดปัดตก).

**Procurement caveat:** GMP supplier qualification เกี่ยวข้องสูงและควรอยู่ใน TOR แต่ระบุเป็น outcome (คัดกรอง/
ประเมินผู้ขายเชิงระบบได้) แทนการบังคับ "SRM portal ครบวงจร native" ที่เอียงเข้าหา Oracle Supplier Qualification.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-Purchasing and Receiving (0.53) — On-Time Delivery Performance / Vendor Return Amount portlet (native)
- [KB] Netsuite-Inventory Management / NSIMG (~0.49) — Supply Chain Control Tower: Vendor Predicted Days Late/Early (predictive, โมดูลเสริม)
- [WEB:docs.oracle.com] NetSuite Applications Suite — Vendor Delivery Performance Scores (ผ่าน Supply Chain Control Tower)
- [WEB:docs.oracle.com] NetSuite Applications Suite — Creating a KPI Scorecard / Using a Custom KPI in a KPI Scorecard (vendor scorecard สร้างจาก custom KPI/saved search)
- [WEB:suiteapp.com] Gatekeeper — vendor scorecard/qualification เป็น SuiteApp พาร์ทเนอร์

---

## F-PRJ-01 — Capital project costing / grants

**Capability (TH):** Capital Project Costing / Grants
**Capability (EN):** Capital project costing
**Domain:** Project · **iCE severity:** กลาง

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** ฟังก์ชันที่ใช้จริงทำได้แต่กระจายอยู่บน SuiteApp/โมดูลเสริมหลายชั้น — Job
Costing/Project Budgeting ต้องให้ account rep เปิดให้; CWIP/CIP พักต้นทุนใน GL แล้วตั้งสินทรัพย์ผ่าน Fixed
Assets Management (FAM = SuiteApp) แบบ manual; workflow CIP buildup คล่องตัวมักพึ่ง third-party (Netgain
NetAsset); grants/fund ใช้ NFP Financials (managed SuiteApp) แต่รายงานสำเร็จรูปอิง US-FASB ต้องปรับเข้ามาตรฐาน
ไทย. ที่อ่อนกว่า Oracle Project Costing Cloud จริงคือ deep multi-level WBS/EPC.

**Counter / Mitigation:** เรต Partial ต่ำกว่าความจริง — แกนที่ healthcare/public-sector ใช้ (grants/fund/
capitalization) NetSuite ทำได้จริงผ่าน **first-party SuiteApp (NFP Financials + FAM)**. grants/fund + capital
project (สร้าง รพ./ครุภัณฑ์การแพทย์) เกี่ยวข้องสูง — วางแผนติดตั้ง SuiteApp + ปรับรายงานให้เข้ามาตรฐานไทย. deep
WBS/EPC แทบไม่เกี่ยว = over-spec.

**Procurement caveat:** ระบุ requirement เป็น grant/fund accounting + capitalization (CIP) + auto-post GL แทน
"enterprise deep-WBS PPM" ที่เอียงเข้าหา Oracle PPM/Primavera.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-Projects (0.61) — Job Costing/Project Budgeting โพสต์เข้า GL (ต้องให้ account rep เปิด)
- [KB] Netsuite-Non-Profit SuiteApps (0.66) — NFP Financials: Grant/Fund/Revenue Restriction
- [KB] Netsuite-Fixed Assets Management (0.53) — asset type 'project' (CIP) ตั้งสินทรัพย์เมื่อปิดโครงการ
- [WEB:netsuite.com] NetSuite Nonprofit — Fund Accounting & Grant Management (NFP Financials SuiteApp)
- [WEB:community.oracle.com] FAM — Tracking Construction in Progress (CIP) in Fixed Asset Management
- [WEB:netgain.tech] NetSuite Fixed Asset Roll Forward & CIP (NetAsset = third-party add-on)

---

## F-QM-01 — Quality management (inspection / NCR / CAPA)

**Capability (TH):** Quality Management (QM / CAPA)
**Capability (EN):** Quality management
**Domain:** Quality · **iCE severity:** สูง

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** CAPA เต็มรูป (root cause 5-Why/Fishbone/8D → corrective action →
effectiveness verification) และ pharma GxP validation/electronic batch record ไม่มีแบบ out-of-the-box — ต้อง
config บน SuiteFlow เองหรือซื้อ QMS SuiteApp เฉพาะ (Intellect QMS/QT9).

**Counter / Mitigation:** ข้ออ้าง "ไม่มี" เกินจริง — ฐาน **NetSuite Quality Management SuiteApp (native, ฟรี)**
ครอบคลุม inspection plan, inspection queue และจัดการ non-conformance (NCR) ผ่าน SuiteFlow พร้อม lot/serial
traceability ใช้ได้จริงในสเกลปัจจุบันของ blood-bank/biologics. ที่ขาดคือ CAPA เต็มรูป + GMP validation เชิงลึก
ซึ่งปิดด้วย config/SuiteApp เสริม — เป็นงานวางแผนก่อน go-live เพราะหน่วยผลิตเซรุ่ม/วัคซีนและศูนย์บริการโลหิตต้องมี
inspection/NCR + lot/expiry traceability ตามมาตรฐาน GMP/ISO 13485.

**Procurement caveat:** ระบุความสามารถ inspection/NCR/lot-traceability + CAPA workflow เป็น outcome; หลีกเลี่ยง
ถ้อยคำ "validated GxP QMS native" ที่มีเพียง SAP QM ตอบได้เต็ม = ล็อกสเปก.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-Quality User Guide (0.56)
- [KB] NSIMG (0.57) — non-conformance ทำผ่าน SuiteFlow
- [WEB:brokenrubik.com] NetSuite Quality Management Guide (partner blog) — ระบุชัดว่าไม่ใช่ QMS ทดแทนงาน validation ยา
- [WEB:docs.oracle.com] NetSuite Quality Inspection Queue

---

## NF-ARC-02 — Deployment options & data residency / sovereignty

**Capability (TH):** ทางเลือกการติดตั้ง / data residency
**Capability (EN):** Deployment & data residency options
**Domain:** Technical · **iCE severity:** สูง

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** NetSuite เป็น multi-tenant SaaS ล้วน ไม่มีทางเลือก on-prem/private/
Cloud@Customer และ **ไม่มี data center ในไทย** อีกทั้งยังไม่รองรับ Oracle EU Sovereign Cloud (เลือกได้เพียง data
center ภูมิภาค เช่น EU) — **เป็นช่องว่างที่ปิดด้วย SuiteApp/custom ไม่ได้เลย**. Oracle มีเส้นทาง in-country/
sovereign (AIS Cloud/Oracle Alloy ในไทย, EU Sovereign Cloud).

**Counter / Mitigation:** จุดอ่อนนี้ "จริงและปิดยาก" — iCE ไม่กลบ. แต่บริบทถ่วงดุล: on-prem/private เป็น
over-spec เมื่อองค์กรเลือกแนวทาง SaaS และ **PDPA ไทยไม่บังคับเก็บข้อมูลในประเทศ** (เป็นประเด็นนโยบาย sovereignty
ระดับบอร์ด ไม่ใช่ข้อบังคับกฎหมาย). สำหรับข้อมูลสุขภาพผู้ป่วย/ผู้บริจาค ควรยกเป็นการตัดสินใจ/ยอมรับความเสี่ยงระดับ
บอร์ดก่อน go-live. (Fusion SaaS public มาตรฐานก็ไม่มี region ในไทยเช่นกัน — ต่างกันที่ Oracle มีเส้นทาง sovereign
ให้เลือก).

**Procurement caveat:** **สูง** — หากเขียน TOR บังคับ "in-country data residency / Cloud@Customer" จะตัด NetSuite
ออกด้วยเงื่อนไขที่ PDPA ไม่ได้บังคับ และเอียงเข้าหา Oracle OCI/Alloy โดยตรง; ควรกำหนดเป็นนโยบายความเสี่ยง +
เกณฑ์ certification (ISO 27001/SOC/PCI) แทนการล็อก physical region. [ต้อง verify สถานะ Oracle EU Sovereign Cloud]

**Confidence:** medium (ต้นฉบับระบุ [ความเชื่อมั่น: กลาง]; มีจุด [ต้อง verify])

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

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** NetSuite ไม่มี engine Segregation of Duties (SoD) อัตโนมัติและ continuous
controls monitoring สำเร็จรูปแบบ native — ต้องเสริมด้วย SuiteApp ของพาร์ทเนอร์ (Fastpath Assure, Netwrix
Strongpoint, SafePaaS). Oracle Advanced Access Controls (Risk Management Cloud) เหนือกว่าชัดเจน.

**Counter / Mitigation:** ถ้อยคำ "ไม่มี access governance ระดับ audit" ลดทอนของจริง — ในตัวมี role-based security
ละเอียด, เครื่องมือตรวจสิทธิ์ (Use Searches to Audit Roles, Show Role Permission Differences), Login Audit
Trail, 2FA/SSO และผ่าน SOC 1/2, ISO 27001 จริง. ปิด gap SoD ด้วย **certified SuiteApp ต้นทุนบริหารจัดการได้**.
สำหรับ public-sector/healthcare ที่อยู่ใต้การตรวจของ สตง. SoD/access governance ครอบการรับบริจาคและจัดซื้อจัดจ้าง
— ควรวางแผนจัดหา SuiteApp certified ปิด gap ก่อน go-live; GRC engine อัตโนมัติเทียบ Oracle เป็นส่วนเกินของ
องค์กรประเทศเดียว.

**Procurement caveat:** ระบุ requirement เป็น "ตรวจ/บังคับ SoD ได้ผ่าน controls + audit trail" (ยอมรับ certified
add-on) แทน "automated SoD engine native" ที่มีเพียง Oracle/SAP ตอบเต็ม.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-Managing Users & Roles (0.6678) — Use Searches to Audit Roles + Login Audit Trail
- [KB] Netsuite-Managing Users & Roles (0.6544) — periodic access review/terminated-user revocation
- [WEB:oracle.com] Oracle Advanced Access Controls Cloud Service datasheet — automated SoD + continuous monitoring + ruleset สำเร็จรูปจำนวนมาก
- [WEB:suiteapp.com] Fastpath Assure for NetSuite — SoD analysis by user/role/permission (ruleset 125+ conflicts)
- [WEB:mysuite.tech] Segregation of Duties in NetSuite: where native tools stop

---

## GP-FUNC-01 — Process manufacturing (formula, batch, co/by-products)

**Capability (TH):** การผลิตแบบกระบวนการ (สูตร/ล็อต/ co-by product)
**Capability (EN):** Process manufacturing (formula, batch, co/by-products)
**Domain:** Manufacturing · **iCE severity:** สูง

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** NetSuite=1★ vs Oracle Fusion=4★ vs SAP S/4HANA=5★ (Gap Severity: Critical;
Fusion เด่นสุด). NetSuite ขาดความลึกของ process manufacturing แบบ SAP PP-PI/Oracle — การคุมสูตรเชิง GMP เข้ม
เช่น potency และ genealogy ของชีววัตถุ ต้องเสริม SuiteApp ภายนอกหรือ custom.

**Counter / Mitigation:** การให้ 1★ + "ไม่มี process mfg แท้ ต้องพึ่ง SuiteApp" ต่ำกว่าความจริง — native มี
recipe/formula (ระดับ workbench) + co-/by-product และ lot/batch (FEFO ผ่าน **first-party SuiteApp**). กระทบสูง
เฉพาะหน่วยผลิตเซรุ่ม-วัคซีน (light pharma/GMP) ที่ต้องคุม potency/genealogy ตามมาตรฐาน GMP — วางแผนเสริม
SuiteApp/custom (blendAPPS Formula & Recipe) ปิด gap ก่อน go-live; ศูนย์บริการโลหิตและหน่วยอื่นใช้ lot/batch
native ได้พอ. (ข้อนี้ซ้ำ F-MFG-01 — ใช้ counter เดียวกัน).

**Procurement caveat:** เขียนเฉพาะ GMP batch record + lot/expiry/co-product ที่ใช้จริง; หลีกเลี่ยง "full process
mfg" ที่ดึงเข้าหา SAP PP-PI.

**Confidence:** medium (ต้นฉบับระบุ [ความเชื่อมั่น: กลาง])

**หลักฐาน / Citation:**
- [KB] Netsuite-Advanced Manufacturing User Guide (Assembly CoProduct 0.62)
- [KB] Netsuite-Manufacturing (BOM/routing/Advanced Manufacturing 0.60)
- [WEB:netsuite.com] Lot Tracking native (FEFO ผ่าน SuiteApp)
- [WEB:suiteapp.com] blendAPPS Formula & Recipe Management

---

## GP-FUNC-04 — Demand planning & statistical forecasting

**Capability (TH):** วางแผนอุปสงค์ / พยากรณ์
**Capability (EN):** Demand planning & statistical forecasting
**Domain:** SCM · **iCE severity:** ต่ำ

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** NetSuite=1★ vs Oracle Fusion=5★ vs SAP S/4HANA=4★ (Gap Severity: Critical;
Fusion เด่นสุด ✔✔). NetSuite Demand Planning เป็นวิธีพื้นฐาน ไม่มี demand sensing/ML และ collaboration แบบ
Oracle SCM Demand Management.

**Counter / Mitigation:** การจัด 1★ "จำกัดมาก" ต่ำกว่าจริง — Demand Planning เป็นฟีเจอร์ **ในตัว** พร้อมพยากรณ์
เชิงสถิติ 4 วิธี (Linear Regression/Moving Average/Seasonal Average/Sales Forecast). พยากรณ์ความต้องการเลือด/
วัคซีน/เซรุ่มใช้วิธีสถิติ native ครอบคลุมได้ ไม่ต้องถึง demand forecasting ระดับ tier-1 (การลดเหลือ 1 ดาวสะท้อน
การตั้งสเปกเทียบ tier-1 มากกว่าความต้องการจริง).

**Procurement caveat:** ระบุ "statistical demand forecasting" เป็น outcome; อย่าผูกกับ "demand sensing/ML" ที่
เป็นจุดเด่นเฉพาะ Oracle.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-Inventory Management (0.69) — Demand Planning วิเคราะห์ stock demand จาก historical
- [KB] NSIMG (0.66) — Demand Plans/Supply Plans, Seasonal Average method
- [WEB:docs.oracle.com] NetSuite Applications Suite — Calculating Item Demand (Linear Regression/Moving Average/Seasonal Average/Sales Forecast)

---

## GP-FUNC-06 — Warehouse management (WMS) — wave/zone, RF, 3PL

**Capability (TH):** คลังสินค้าขั้นสูง (WMS, wave/zone, RF)
**Capability (EN):** Warehouse Mgmt (WMS) — wave/zone, RF, 3PL
**Domain:** SCM · **iCE severity:** กลาง

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** NetSuite=2★ vs Oracle Fusion=4★ vs SAP S/4HANA=5★ (Gap Severity: High).
NetSuite WMS เป็น first-party SuiteApp ที่ต้องซื้อ license แยก; native เหมาะปริมาณต่ำ-กลาง — 3PL billing เชิงลึก,
slotting optimization, yard management ต้องเสริม SuiteApp พาร์ทเนอร์ (RF-SMART/Infios).

**Counter / Mitigation:** rating 2/"add-on ตื้น" ลดทอนเกินจริง — wave/zone picking, RF/barcode, directed
put-away เป็น **native ของ WMS SuiteApp (first-party)**; multi-location/multi-warehouse เป็น native ของ ERP
ฐาน. เหมาะกับคลังหลายแห่งของ blood-bank service/biologics ที่ต้องคุม lot/expiry/RF; 3PL/yard mgmt แทบไม่เกี่ยว.
ต้นทุน license WMS เป็นรายการที่ต้องวางแผน. (ข้อนี้ซ้ำ F-WMS-01 / TOR-SCM-02).

**Procurement caveat:** เขียนครอบ directed ops + lot/expiry (ที่ใช้) มากกว่า "3PL billing/slotting engineered" ที่
เอียง tier-1 WMS.

**Confidence:** medium (ต้นฉบับระบุ [ความเชื่อมั่น: กลาง])

**หลักฐาน / Citation:**
- [KB] WMS4-WMS Outbound Fulfillment (0.65) — wave; WMS Advanced Setup (0.60) — zones/strategies
- [WEB:netsuite.com] NetSuite WMS product page — RF, putaway/picking strategies, cycle count
- [WEB:brokenrubik.com] Best WMS for NetSuite 2026: Native vs RF-SMART/Infios — native WMS มี wave/zone/directed ops แต่วางตำแหน่งปริมาณต่ำ-กลาง, 3rd-party ลึกกว่าด้าน labor/slotting

---

## GP-FUNC-10 — Supplier lifecycle & performance management (SLM)

**Capability (TH):** บริหารวงจรชีวิต & ผลงานซัพพลายเออร์
**Capability (EN):** Supplier lifecycle & performance management (SLM)
**Domain:** Procurement · **iCE severity:** กลาง

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** NetSuite=1★ vs Oracle Fusion=4★ vs SAP S/4HANA=5★ (Gap Severity: High).
NetSuite ไม่มี supplier scorecard 4 KPI สำเร็จรูปแบบ native; KPI คุณภาพ (quality rejection) ต้องใช้โมดูล Quality
Management และ supplier qualification/SLM lifecycle เชิงลึกต้องใช้ SuiteApp/custom.

**Counter / Mitigation:** ข้ออ้าง "ไม่มี scorecard เลย" คลาดเคลื่อน — On-Time Delivery Performance เป็น native
portlet, predictive vendor scores ผ่าน Supply Chain Control Tower (โมดูลเสริม) บวก KPI Scorecard จาก custom
KPI/saved search. Qualification เชิงลึกปิดด้วย **certified SuiteApp (Gatekeeper)**. กระทบหน่วยผลิตเซรุ่ม-วัคซีน
(GMP) ที่ต้องคัดกรอง/ประเมินคุณภาพซัพพลายเออร์เชิงระบบ — ปิด gap ได้ด้วย SuiteApp/custom ต้นทุนบริหารจัดการได้.
(สอดคล้อง F-PRC-02).

**Procurement caveat:** ระบุเป็น outcome (ประเมิน/คัดกรองผู้ขายเชิงระบบ); ยอมรับ certified add-on แทน "SLM
lifecycle native ครบวงจร".

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-Purchasing and Receiving (0.53) — On-Time Delivery Performance / Vendor Return Amount (native portlet)
- [KB] Netsuite-Vendors (0.53) — vendor records (พื้นฐาน, ไม่มี qualification workflow)
- [WEB:docs.oracle.com] NetSuite Applications Suite — Vendor Delivery Performance Scores (ผ่าน Supply Chain Control Tower)
- [WEB:docs.oracle.com] NetSuite Applications Suite — Creating a KPI Scorecard / Using a Custom KPI (vendor scorecard = custom KPI/saved search)
- [WEB:suiteapp.com] Gatekeeper — balanced scorecard/qualification เป็น SuiteApp

---

## GP-FUNC-11 — Contract lifecycle management (CLM)

**Capability (TH):** บริหารสัญญา (CLM)
**Capability (EN):** Contract Lifecycle Management (CLM)
**Domain:** Procurement · **iCE severity:** สูง

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** NetSuite=1★ vs Oracle Fusion=4★ vs SAP S/4HANA=4★ (Gap Severity: Med).
NetSuite ไม่มีโมดูล CLM เฉพาะในตัว — "Managing Contracts" native เป็นสัญญาฝั่งขาย/ต่ออายุเท่านั้น ไม่มี clause
library, authoring, redline หรือ obligation management; ฝั่งจัดซื้อมีเพียง Purchase Contract + เก็บไฟล์ใน File
Cabinet.

**Counter / Mitigation:** ความต้องการจริงของ public-sector/healthcare (คลังสัญญา + แจ้งเตือนต่ออายุ + audit
trail) ทำได้ด้วย **native + certified SuiteApp ราคาประหยัด (Gatekeeper, Conga/Malbek)** — ไม่ใช่ blocker. งาน
จัดซื้อ/สัญญาทุนสนับสนุนอยู่ใต้การตรวจ สตง. จึงต้องมี CLM พร้อมใช้ตั้งแต่ go-live → วางแผน/จัดงบเปิด SuiteApp
ล่วงหน้า. CLM ระดับ enterprise (AI redline/clause library เต็มรูป) เป็น over-spec (gap_severity 'Med' สมเหตุผล).

**Procurement caveat:** ระบุ outcome (จัดเก็บ/ต่ออายุ/ตรวจสอบสัญญาได้) และยอมรับ SuiteApp; อย่าบังคับ "AI
clause-library CLM native" ที่ตัด NetSuite.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-Software Vertical Contract Renewals (0.66) + Netsuite-Sales Orders and Cash Sales (0.63) — เป็น contract ฝั่งขาย/ต่ออายุเท่านั้น
- [WEB:docs.oracle.com] NetSuite Applications Suite — Managing Contracts (จำกัดที่ sales renewal lifecycle; ไม่มี clause library/authoring/obligation)
- [WEB:suiteapp.com] Gatekeeper Contract Management & Vendor Portal — CLM สำหรับ NetSuite เป็น SuiteApp พาร์ทเนอร์ (ยืนยันมีจริง)

---

## GP-FUNC-13 — Enterprise planning & budgeting (EPM / xP&A)

**Capability (TH):** วางแผนงบ/พยากรณ์องค์กร (EPM / xP&A)
**Capability (EN):** Enterprise Planning & Budgeting (EPM / xP&A)
**Domain:** EPM · **iCE severity:** ต่ำ

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** NetSuite=2★ vs Oracle Fusion=5★ vs SAP S/4HANA=4★ (Gap Severity: Critical;
Fusion เด่นสุด ✔✔). NSPB เป็นโมดูลเสริมลิขสิทธิ์แยกและเป็นรุ่น productized (Financials) ปรับแต่งได้จำกัดกว่า
Oracle EPBCS เต็ม — ไม่มีโมดูล Workforce/Capital สำเร็จรูป และไม่มี FCCS/ARCS/PCMCS ในชุด.

**Counter / Mitigation:** การให้ 2/5 และตี "Critical gap" สูงเกินจริง — **NSPB (first-party) ใช้เอนจิน PBCS/
Hyperion เดียวกับ Oracle EPM Cloud** จึงทำ xP&A core (driver-based, scenario, predictive, rolling forecast) ได้
ในตัว. ความต่างคือความกว้างของ pre-built modules ไม่ใช่ core capability ที่ขาดหาย. งบประมาณของสำนักงบประมาณ
องค์กรการกุศลใช้ NSPB Financials + NSAW เพียงพอ; ความกว้างระดับ Hyperion เต็มสูบเป็น over-spec. (สอดคล้อง
F-EPM-01 / GP-STANDOUT-01 / TOR-FIN-01).

**Procurement caveat:** อย่าบังคับ "workforce/capital planning สำเร็จรูป native + full Hyperion suite" ที่เอียง
เข้าหา Oracle EPM Cloud.

**Confidence:** high

**หลักฐาน / Citation:**
- [WEB:docs.oracle.com] NetSuite Planning and Budgeting Financials Overview — driver-based, what-if scenarios, Predictive Planning (article_7160253896 — ตรวจแล้วมีจริง)
- [WEB:docs.oracle.com] NetSuite Planning and Budgeting — รองรับเฉพาะโมดูล Financials, ไม่มี Workforce module (article_8124016549 — ตรวจแล้วมีจริง)
- [WEB:netsuite.com] What is NetSuite Planning and Budgeting — built on Oracle EPM Cloud engine, scenario/what-if (financial-planning.shtml)
- [KB] Netsuite-Statistical Accounting / Netsuite-General Accounting (~0.6) — base NetSuite มีเพียง budget/statistical allocation พื้นฐาน

---

## GP-FUNC-15 — Advanced cost accounting (multi-method costing)

**Capability (TH):** ต้นทุนขั้นสูง (actual/standard หลายวิธี)
**Capability (EN):** Advanced cost accounting (multi-method costing)
**Domain:** Finance · **iCE severity:** ต่ำ

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** NetSuite=2★ vs Oracle Fusion=4★ vs SAP S/4HANA=5★ (Gap Severity: High).
NetSuite ไม่มี actual costing หลาย valuation/หลายสกุลเชิงลึกแบบ SAP Material Ledger (CO/ML); วิธีต้นทุนตั้งครั้ง
เดียวที่ item record เปลี่ยนไม่ได้หลังบันทึก, Multi-Book ตั้ง standard cost ต่างกันรายบัญชีได้แต่ไม่ใช่คนละวิธี
ต้นทุนต่อบัญชี.

**Counter / Mitigation:** เรตติ้ง "costing จำกัดวิธี" ประเมินต่ำเกิน — NetSuite มี **7 วิธีต้นทุน native**
(Average/FIFO/LIFO/Standard/Group Average/Lot-Numbered/Specific + Landed Cost). Standard/Average + **Lot-Numbered
costing** ตรงกับการคิดต้นทุนรายล็อตของผลิตภัณฑ์โลหิต/เซรุ่ม/วัคซีน (batch) ครอบคลุมได้; ความลึก Material Ledger
(actual costing หลาย valuation/transfer pricing) เป็นของจริงแต่ over-spec สำหรับงานสาธารณกุศล.

**Procurement caveat:** ระบุวิธีต้นทุนที่ใช้จริง (standard/average/lot) แทน "multi-valuation actual costing" ที่
มีเพียง SAP ML ตอบเต็ม.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] NSIRM (0.657) — Costing Methods: Average/FIFO/LIFO/Standard/Group Average/Lot/Specific
- [KB] Netsuite-Item Record Management (0.62) — Group Average, Standard Costing, Cost Category, Landed Cost
- [KB] Netsuite-Multi-Book Accounting + Item Record Mgmt (0.55) — ตั้ง standard cost ต่างกันรายบัญชี (per-book amount)
- [WEB:docs.oracle.com] NetSuite Applications Suite — Costing Methods (section_N2191818) — verified ครบ 7 วิธี
- [WEB:docs.oracle.com] NetSuite Help — Revaluation and Multi-Book Accounting: แต่ละ book มี standard cost ของตัวเองตามสกุลเงิน (per-book cost ไม่ใช่ per-book method) — verified
- [WEB:netsuite.com] Beyond FIFO & LIFO: Inventory Costing Methods (+ Group Average/Lot/Specific) — verified

---

## GP-FUNC-16 — Statutory localization, tax engine & e-invoicing (e-Tax Invoice TH)

**Capability (TH):** Tax engine & localization ตามกฎหมายแต่ละประเทศ
**Capability (EN):** Statutory localization, tax engine & e-invoicing
**Domain:** Finance · **iCE severity:** สูง

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** NetSuite=2★ vs Oracle Fusion=4★ vs SAP S/4HANA=5★ (Gap Severity: Critical;
Fusion เด่นสุด). **ไม่มีมาตรฐาน e-Tax Invoice ไทยแบบ native** — Electronic Invoicing SuiteApp เป็นเพียงกรอบออก
XML/JSON ต้องทำ template เอง/ใช้พาร์ทเนอร์เพื่อส่งกรมสรรพากร; ความกว้างประเทศน้อยกว่า SAP/Oracle.

**Counter / Mitigation:** การให้ 2★ ประเมินต่ำไปสำหรับ scope ไทย — **SuiteTax + SEA Localization + International
Tax Reports** รองรับ VAT/ภ.พ.30/ใบกำกับภาษี-เครดิตโน้ตตามรูปแบบกรมสรรพากรครบสำหรับไทย. ช่องว่างจริงแคบเหลือเพียง
**e-Tax Invoice XML ส่งกรมสรรพากร** (ต้อง custom/partner) ไม่ใช่ "ทำภาษีไม่ได้" และไม่ใช่เรื่องจำนวนประเทศ.
กระทบทุกหน่วยที่ออกเอกสารภาษี (รพ./จัดซื้อ/รับบริจาคที่มีภาษี) — e-Tax Invoice & e-Receipt เป็นข้อบังคับตาม
กฎหมายไทย ต้องวางแผน custom/partner ปิด gap ก่อน go-live.

**Procurement caveat:** ระบุ e-Tax Invoice/e-Receipt (TH) + VAT/ภ.พ.30 เป็น outcome; อย่าบังคับ "statutory
localization ทุกประเทศ native" ที่เอียงเข้าหา breadth ของ Oracle/SAP.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-Country Specific Features (0.7242, SuiteTax Reports/VAT)
- [WEB:docs.oracle.com] Thailand Tax Invoice & Credit Memo Templates (SEA Localization, P.P.30)
- [WEB:docs.oracle.com] Electronic Invoicing Overview (กรอบ XML/JSON ไม่มี native มาตรฐานไทย)

---

## GP-FUNC-18 — Core HR & multi-country global payroll

**Capability (TH):** Core HR + Global Payroll หลายประเทศ
**Capability (EN):** Core HR & multi-country global payroll
**Domain:** HCM · **iCE severity:** กลาง

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** NetSuite=1★ vs Oracle Fusion=5★ vs SAP S/4HANA=5★ (Gap Severity: Critical).
Payroll เนทีฟมีเฉพาะสหรัฐ (SuitePeople U.S. Payroll) — **ไม่มีเงินเดือนไทย/หลายประเทศในตัว** ต้องใช้ SuiteApp
พาร์ตเนอร์ (มีค่าใช้จ่าย+งาน implement) หรือเชื่อมระบบเงินเดือนไทยภายนอก.

**Counter / Mitigation:** เรต 1★/Critical ต่ำเกินจริง — เหมาว่า "ไม่มี global payroll = HCM ทั้งก้อนใช้ไม่ได้"
ทั้งที่ **Core HR เป็นโมดูล native ใช้งานจริง** (ทะเบียนพนักงาน/org chart, Time-Off, ค่าตอบแทน/สวัสดิการ).
เงินเดือนไทยทำได้ผ่าน SuiteApp/ระบบภายนอก (เช่น NuSmart International Payroll) — ไม่ใช่ "ทำไม่ได้". เกณฑ์ "global/
หลายประเทศ" ไม่เกี่ยวเพราะจ่ายเงินเดือนในไทยประเทศเดียว = over-spec; ต้องวางสถาปัตยกรรม payroll ไทยแบบต่อเชื่อม
ตั้งแต่ต้น. ยังต้องตรวจว่า SuiteApp พาร์ตเนอร์ครอบคลุมภาษี/ประกันสังคมไทยจริงหรือไม่ [ต้อง verify].

**Procurement caveat:** แยกเกณฑ์ "Core HR" (ผ่าน native) ออกจาก "multi-country global payroll" (ไม่เกี่ยว) —
การมัดรวมแล้วให้ Mandatory เป็นล็อกสเปกเอียงเข้า Oracle/SAP.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-Employee Management — Core HR/Time-Off/Compensation (0.7159)
- [WEB:docs.oracle.com] NetSuite Applications Suite - SuitePeople U.S. Payroll (native payroll = US-only)
- [WEB:suiteapp.com] International Payroll Extension for SuitePeople / NuSmart International Payroll and HCM (third-party SuiteApp; ครอบคลุมไทยจริงหรือไม่ [ต้อง verify])

---

## GP-FUNC-19 — Talent: performance, learning, recruiting

**Capability (TH):** Talent / Performance / Learning / Recruiting
**Capability (EN):** Talent: performance, learning, recruiting
**Domain:** HCM · **iCE severity:** ต่ำ

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** NetSuite=1★ vs Oracle Fusion=5★ vs SAP S/4HANA=5★ (Gap Severity: Critical).
Recruiting มีเพียงพื้นฐาน (Job Requisition + Recruiting Reports) ไม่ใช่ ATS เต็มรูป; ไม่มี Learning/LMS เนทีฟ และ
ไม่มี succession planning — ต้องต่อระบบเฉพาะทางภายนอก (Greenhouse/Lever) ผ่าน API.

**Counter / Mitigation:** "แทบไม่มี talent suite" เกินจริง — **SuitePeople Performance Management เป็นเนทีฟ**
(goals/reviews/check-in/Kudos) บน data model เดียวกับ Core HR. งาน performance/learning พื้นฐานของบุคลากร รพ.
ใช้ของเนทีฟได้; talent suite ครบวงจร (ATS/LMS/succession) แทบไม่มี use case จริงสำหรับองค์กรการกุศล/การศึกษา —
เลือกต่อเชื่อมเฉพาะที่จำเป็น. (สอดคล้อง TOR-HCM-02).

**Procurement caveat:** ระบุ performance (ที่ใช้) เป็น outcome; อย่าบังคับ "end-to-end talent บน data model
เดียว" ที่ออกแบบมาตี SuccessFactors และเอียงเข้า Oracle HCM.

**Confidence:** high

**หลักฐาน / Citation:**
- [WEB:netsuite.com] SuitePeople Performance Management (product page)
- [KB] Netsuite-Administrator Guide — Performance Management (SuitePeople HR), Kudos (0.5788)
- [KB] Netsuite-Employee Management — Recruiting Reports bundle/Job Requisition (0.4987; เป็นแค่ recruiting พื้นฐาน ไม่ใช่ ATS)

---

## GP-FUNC-20 — Time & labor / workforce management at scale (shift scheduling)

**Capability (TH):** Time & Labor / Workforce Mgmt ขนาดใหญ่
**Capability (EN):** Time & labor / workforce management at scale
**Domain:** HCM · **iCE severity:** กลาง

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** NetSuite=2★ vs Oracle Fusion=4★ vs SAP S/4HANA=4★ (Gap Severity: High).
WFM เป็นโมดูลซื้อแยก และชุดกฎ wage/labor-compliance เป็นพรีเซ็ตอิงกฎหมายแรงงานสหรัฐ ผูกแน่นกับ U.S. Payroll —
องค์กรไทยต้องตั้งกฎ OT/แรงงานไทยเอง และยังไม่ลึกเท่า UKG/SAP สำหรับโมเดลแรงงาน/สหภาพซับซ้อนมาก.

**Counter / Mitigation:** ข้อกล่าวอ้าง "time tracking พื้นฐาน" ล้าสมัย — **SuitePeople Workforce Management (WFM,
เปิดตัว 2023 R1)** ทำจัดตารางกะ + labor forecasting, time & attendance (clock in/out มือถือ/แท็บเล็ต, geo-tag/
ไบโอเมตริก), wage rules engine และสลับกะ ปิด gap shift scheduling/T&A ที่อ้างว่าไม่มีไปแล้ว. เกี่ยวกับการจัดเวร
พยาบาล รพ. พอควร — ใช้ WFM ได้แต่ต้อง config กฎแรงงานไทยเพิ่ม; การจัดเวรเชิงลึกมักใช้ระบบ T&A/HIS เฉพาะทางต่อ
เชื่อมอยู่แล้ว.

**Procurement caveat:** ระบุ shift scheduling/T&A ที่ใช้จริง; ยอมรับ config กฎไทย + ต่อเชื่อม T&A/HIS แทนการ
บังคับ "workforce mgmt at scale native" ที่เอียง tier-1.

**Confidence:** medium (ต้นฉบับระบุ [ความเชื่อมั่น: กลาง])

**หลักฐาน / Citation:**
- [WEB:docs.oracle.com] NetSuite Applications Suite - SuitePeople Workforce Management Overview (native shift scheduling/T&A/wage rules)
- [WEB:netsuite.com] SuitePeople Workforce Management (product/datasheet; เปิดตัว 2023 Release 1)

---

## GP-FUNC-21 — Enterprise PPM, project costing & grants

**Capability (TH):** PPM ระดับองค์กร / ต้นทุนโครงการ / ทุนวิจัย
**Capability (EN):** Enterprise PPM, project costing & grants
**Domain:** Project · **iCE severity:** กลาง

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** NetSuite=3★ vs Oracle Fusion=5★ vs SAP S/4HANA=4★ (Gap Severity: High;
Fusion เด่นสุด ✔✔). ที่ด้อยกว่าจริงคือ enterprise PPM/project costing สเกลใหญ่และตารางงานระดับ Primavera (Oracle
PPM Cloud tier-1).

**Counter / Mitigation:** ความต้องการจริงอยู่ในระดับที่ **NetSuite + Nonprofit edition รองรับครบ** — Project
Management โพสต์ต้นทุนเข้า GL พร้อม budget vs actual และทำทุนวิจัย/grants ผ่าน **NFP Financials (first-party
SuiteApp: Grant Management & Fund Accounting)**. ต้องตั้งงบ NFP Financials SuiteApp + ปรับรายงานสำเร็จรูป US-FASB
เข้ามาตรฐานไทย ซึ่งเป็นงานจริงต่อภารกิจรับบริจาค/กองทุน; ส่วน PPM/Primavera tier-1 เป็น over-spec. (สอดคล้อง
F-PRJ-01 / TOR-PPM-01).

**Procurement caveat:** ระบุ project costing/grants/fund + auto-post GL เป็น outcome; อย่าบังคับ "enterprise PPM
tier-1/Primavera-grade" ที่ตัด NetSuite.

**Confidence:** medium (ต้นฉบับระบุ [ความเชื่อมั่น: กลาง])

**หลักฐาน / Citation:**
- [KB] Netsuite-Projects (0.61) — native project costing/job costing/budgeting
- [KB] Netsuite-Non-Profit SuiteApps (0.66) — Grant Management & Fund Accounting
- [WEB:netsuite.com] NetSuite Nonprofit ERP — Grant Management & Fund Accounting
- [WEB:docs.oracle.com/netsuite] Non-Profit Financial Management (NetSuite Help)

---

## GP-FUNC-23 — Enterprise asset management & maintenance (EAM)

**Capability (TH):** บริหารสินทรัพย์/ซ่อมบำรุงองค์กร (EAM)
**Capability (EN):** Enterprise Asset Management & maintenance (EAM)
**Domain:** Asset · **iCE severity:** กลาง

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** NetSuite=1★ vs Oracle Fusion=4★ vs SAP S/4HANA=5★ (Gap Severity: High).
Base FAM (SuiteApp) ทำได้แค่เสื่อมราคา/ตีราคาใหม่/จำหน่าย + เก็บ maintenance schedule/insurance แต่ไม่มี work
order; EAM โรงงานหนัก (linear asset/reliability) ยังเป็นจุดแข็ง SAP PM.

**Counter / Mitigation:** เรต 1 ดาวต่ำกว่าความจริง — งานซ่อมบำรุง work order/preventive maintenance ตามเวลา/
meter-based ทำได้ผ่าน **NetSuite Field Service Management (first-party หลัง Oracle ซื้อ Next Technik ต.ค. 2023)**
ให้ work order, PM (meter-based: ชั่วโมง/ไมล์/รอบ → สร้างงานอัตโนมัติ), asset hierarchy/sub-asset และ
maintenance history — เป็นโมดูลซื้อแยก. PM ครุภัณฑ์การแพทย์/แล็บ/cold-chain เกี่ยวพอควร — เพิ่มโมดูล FSM หรือใช้
biomedical CMMS เฉพาะทางต่อเชื่อม; EAM โรงงานหนักเป็น over-spec.

**Procurement caveat:** ระบุ PM/work order/meter-based ที่ใช้จริง; อย่าบังคับ "predictive/condition-based EAM
เต็มรูป" ที่เอียงเข้า SAP PM.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-Fixed Assets Management (0.60) — depreciation + maintenance schedule/insurance, ไม่มี work order
- [WEB:netsuite.com] NetSuite Field Service Management — work orders, automated preventive maintenance, asset hierarchy
- [WEB:netsuite.com] FSM datasheet — usage/meter-based maintenance (hours/mileage/cycles) auto-generates jobs
- [WEB:oracle.com] Oracle acquires Next Technik — FSM กลายเป็น first-party (2023)

---

## GP-FUNC-25 — Field service management (FSM)

**Capability (TH):** บริการภาคสนาม (Field Service)
**Capability (EN):** Field Service Management (FSM)
**Domain:** Service · **iCE severity:** ต่ำ

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** NetSuite=1★ vs Oracle Fusion=4★ vs SAP S/4HANA=4★ (Gap Severity: Med).
NetSuite FSM เป็น add-on ที่ต้องซื้อแยกและมีค่าใช้จ่าย.

**Counter / Mitigation:** การให้ 1★/มองว่าเป็น third-party ล้วน **ล้าสมัย** — ปัจจุบัน **NetSuite Field Service
Management เป็น first-party** (เดิม NextService/Next Technik ที่ Oracle เข้าซื้อปี 2023) มี schedule board ลาก-
วาง, dispatch ตาม skill/location, mobile app, asset/warranty, preventive maintenance, ผูก inventory ตรง.
สำหรับ healthcare มีเพียง use case ชายขอบ (ซ่อมครุภัณฑ์การแพทย์/หน่วยรับบริจาคเคลื่อนที่) ซึ่งใช้ EAM/maintenance
ก็พอ — การบรรจุใน TOR เป็น over-spec.

**Procurement caveat:** FSM เชิงพาณิชย์ไม่ใช่กระบวนการหลักของ healthcare/public-sector — อย่าบังคับใน TOR (over-
spec/ล็อกสเปก).

**Confidence:** medium (ต้นฉบับระบุ [ความเชื่อมั่น: กลาง]; มีจุด [ต้อง verify])

**หลักฐาน / Citation:**
- [WEB:netsuite.com] NetSuite Field Service Management — Scheduling and Dispatch
- [WEB] Oracle เข้าซื้อ Next Technik (NextService) ก.ย. 2023 — ยืนยันสถานะ first-party
- [KB] ไม่พบเอกสาร FSM โดยตรง (top ~0.45 = NSIMG) [ต้อง verify จากเว็บทางการ]

---

## GP-FUNC-26 — Quality management (QMS), inspection plans

**Capability (TH):** ระบบคุณภาพ (QMS) / แผนตรวจสอบ
**Capability (EN):** Quality Management (QMS), inspection plans
**Domain:** Quality · **iCE severity:** สูง

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** NetSuite=1★ vs Oracle Fusion=4★ vs SAP S/4HANA=5★ (Gap Severity: High).
CAPA เต็มรูปต้อง config บน SuiteFlow หรือซื้อ QMS SuiteApp เพิ่ม และไม่ใช่ระบบ validated GxP เต็มรูปแบบอย่าง
SAP QM — ความลึกระดับ regulated pharma ยังเป็นช่องว่างจริง.

**Counter / Mitigation:** เรตติ้ง 1★ ทำให้เข้าใจผิดว่า NetSuite แทบไม่มีระบบคุณภาพ — **Quality Management
SuiteApp (เนทีฟ)** มี inspection plan + non-conformance ผ่าน SuiteFlow + lot/serial traceability ใช้ได้จริง
(ตามจริงราว 3★) ช่วยรองรับแนวทาง ISO 13485 ได้บางส่วน. กระทบสูงต่อการผลิตชีววัตถุ (เซรุ่ม/วัคซีน) และงานศูนย์
บริการโลหิตที่ต้องมีระบบคุณภาพ/แผนตรวจสอบตามมาตรฐาน GMP/ISO 13485 — วางแผนปิด gap CAPA/validation ก่อน go-live.
(ซ้ำ F-QM-01).

**Procurement caveat:** ระบุ inspection/NCR/traceability + CAPA workflow เป็น outcome; หลีกเลี่ยง "validated GxP
QMS native" ที่มีเพียง SAP QM ตอบเต็ม.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-Quality User Guide (0.56)
- [KB] NSIMG (0.57) — non-conformance ทำผ่าน SuiteFlow
- [WEB:brokenrubik.com] NetSuite Quality Management Guide (partner blog)
- [WEB:docs.oracle.com] NetSuite Quality Inspection Queue

---

## GP-FUNC-27 — Governance, Risk & Compliance (GRC) / SoD

**Capability (TH):** กำกับ ความเสี่ยง การควบคุม / SoD
**Capability (EN):** Governance, Risk & Compliance (GRC) / SoD
**Domain:** GRC · **iCE severity:** สูง

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** NetSuite=2★ vs Oracle Fusion=5★ vs SAP S/4HANA=5★ (Gap Severity: High).
NetSuite มีเครื่องมือ native แค่บริหาร role/permission + audit trail + approval workflow + ตรวจสิทธิ์ (saved
search/role audit) — **ไม่มี engine automated SoD/continuous controls monitoring แบบเนทีฟ** อย่าง Oracle Risk
Mgmt Cloud หรือ SAP GRC Access Control.

**Counter / Mitigation:** เรตติ้ง 2★ (Partial) สมเหตุผล; ถ้อยคำ "SoD/role review พื้นฐาน" ลดทอน — NetSuite มี
เครื่องมือ audit role + audit trail native และ **ecosystem SoD ที่ certified เต็มที่ (Fastpath Assure, Netwrix
Strongpoint, SafePaaS)**. องค์กรอยู่ใต้การตรวจของ สตง. การควบคุมการแบ่งแยกหน้าที่ (SoD) เป็นข้อกำหนดธรรมาภิบาล/
ตรวจสอบ — วางแผนติดตั้ง SuiteApp SoD ที่ certified และออกแบบ controls ก่อน go-live; continuous controls
monitoring ระดับ enterprise เต็มรูปเป็นส่วนเสริมที่เลือกได้. (สอดคล้อง NF-SEC-01 / GP-TECH-11 / TOR-TECH-05).

**Procurement caveat:** ระบุ "ตรวจ/บังคับ SoD ได้ (ยอมรับ certified add-on)" แทน "automated SoD/CCM native" ที่มี
เพียง Oracle/SAP ตอบเต็ม.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-Managing Users & Roles (0.695/0.6678) — role permissions + audit role searches
- [WEB:netsuite.com] What is NetSuite Governance, Risk & Compliance? — GRC = native controls + partner SuiteApp (ไม่ใช่ SoD engine native)
- [WEB:oracle.com] Oracle Risk Management Cloud — automated SoD + continuous monitoring
- [WEB:netwrix.com] NetSuite Segregation of Duties (Strongpoint) — alert on SoD conflicts
- [WEB:suiteapp.com] Fastpath Assure for NetSuite

---

## GP-TECH-08 — Data residency, sovereignty & region count

**Capability (TH):** ถิ่นที่อยู่ข้อมูล / sovereign / จำนวน region
**Capability (EN):** Data residency, sovereignty & region count
**Domain:** Technical · **iCE severity:** สูง

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** NetSuite=2★ vs Oracle Fusion=5★ vs SAP S/4HANA=4★ (Gap Severity: High;
Fusion เด่นสุด ✔✔). NetSuite ให้ data residency ผ่าน data center หลายภูมิภาค (EU/NA/APAC) แต่ **ไม่มี DC ใน
ประเทศไทยและไม่รองรับ EU Sovereign Cloud** ขณะที่ Oracle มีเส้นทาง sovereign/in-country (EU Sovereign Cloud, AIS
Cloud/Oracle Alloy ไทย) — จุดต่างนี้ไม่สมมาตร.

**Counter / Mitigation:** จุดอ่อนจริงและปิดยาก (iCE ไม่กลบ). บริบทถ่วงดุล: **PDPA ไม่บังคับ localization** และ
ข้อมูลไทยของ public SaaS ทั้งสองเจ้าอยู่ต่างประเทศคล้ายกัน (Oracle Fusion SaaS public มาตรฐานก็ไม่มี region ใน
ไทย) — ต่างกันที่ Oracle มีเส้นทาง sovereign ให้เลือก. ข้อมูลสุขภาพ/ผู้บริจาคทำให้ sovereignty มีน้ำหนักเชิง
นโยบาย/การตรวจสอบ — ควรเคลียร์ทางเลือก data center ในประเทศ/sovereign ก่อน go-live. (สอดคล้อง NF-ARC-02 /
GP-STANDOUT-09 / TOR-TECH-04).

**Procurement caveat:** **สูง** — การบังคับ in-country/sovereign region ใน TOR เอียงเข้าหา OCI/Alloy โดยตรงและใช้
เงื่อนไขที่ PDPA ไม่ได้บังคับ; กำหนดเป็นนโยบายความเสี่ยง + certification แทน. [ต้อง verify]

**Confidence:** medium (ต้นฉบับระบุ [ความเชื่อมั่น: กลาง]; มีจุด [ต้อง verify])

**หลักฐาน / Citation:**
- [WEB:netsuite.com] NetSuite Data Center datasheet — EU DCs (Amsterdam/Frankfurt/London/Newport), no Thai DC
- [WEB:sota.io] NetSuite not on Oracle EU Sovereign Cloud (Q1 2026) [ต้อง verify]
- [WEB:bakermckenzie.com] Thailand cross-border data transfer — no localization mandate
- [WEB:oracle.com] AIS Cloud / Oracle Alloy Thailand (2024)

---

## GP-TECH-12 — Industry-specific cloud solutions depth

**Capability (TH):** โซลูชันเฉพาะอุตสาหกรรม
**Capability (EN):** Industry-specific cloud solutions depth
**Domain:** Technical · **iCE severity:** สูง

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** NetSuite=2★ vs Oracle Fusion=4★ vs SAP S/4HANA=5★ (Gap Severity: High).
การผลิตชีววัตถุ (เซรุ่ม/วัคซีน) ระดับ GMP เต็มรูปไม่ครบในตัว — electronic batch record/GMP เชิงลึกต้องประเมิน fit
และอาจต้องเสริมโซลูชัน ISV เฉพาะ.

**Counter / Mitigation:** คำกล่าว NetSuite "อ่อน vertical" **กลับด้าน** สำหรับ healthcare/non-profit — vertical ที่
เกี่ยวจริงที่สุดคือ nonprofit/กองทุน-ทุนสนับสนุน ซึ่ง NetSuite แข็งและเป็น **native-grade (NFP Financials
SuiteApp: Revenue Restriction Management, Grant Management, Pledge & Donation, รายงาน Net Assets/FASB)** และมี
lot-numbered + วันหมดอายุ + FEFO + Quality Management SuiteApp เป็นพื้นฐาน traceability. อุตสาหกรรมที่ต้นฉบับยกมา
(oil&gas, utilities, auto) ไม่เกี่ยวเลย. กระทบเฉพาะหน่วยผลิตชีววัตถุ GMP ที่ต้องประเมินและปิด gap GMP ก่อน
go-live.

**Procurement caveat:** อย่าให้ TOR ตัด NetSuite ด้วย "industry depth" ที่วัดจาก vertical นอกภารกิจ (oil&gas/
utilities) — vertical ที่เกี่ยวจริง (nonprofit) NetSuite แข็ง.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-Non-Profit SuiteApps — NFP Financials/Revenue Restriction/Grant (0.63)
- [KB] NSIMG — FEFO Lot Allocations/expiry (0.658)
- [KB] Netsuite-Item Record Management — lot numbered + expiration labels (0.682)

---

## GP-STANDOUT-01 — Fusion standout: Enterprise Planning & Budgeting (EPM / xP&A)

**Capability (TH):** วางแผนงบ-พยากรณ์องค์กร (EPM / xP&A)
**Capability (EN):** Enterprise Planning & Budgeting (EPM / xP&A) — Fusion standout
**Domain:** EPM · **iCE severity:** ต่ำ

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** การวางแผนงบ-พยากรณ์ขั้นสูงของ NetSuite ต้องซื้อ NSPB เป็น add-on แยก และความ
ลึกด้าน driver-based, multi-scenario, financial close/consolidation รวมศูนย์ ยังไม่เทียบชั้น Oracle EPM Cloud
(สาย Hyperion) ที่ยกเป็น Fusion standout Rank 1.

**Counter / Mitigation:** EPM/xP&A ระดับ Hyperion เป็นจุดแข็ง Oracle จริง แต่ **"เกินความจำเป็น"** ของงานสาธารณ
กุศล — งบประมาณของหน่วยงานสาธารณกุศลใช้ **NSPB (first-party, เอนจิน Oracle EPM เดียวกัน) + NSAW เพียงพอ**. การ
ตั้งสเปก driver-based/multi-scenario เต็มรูปทั้งองค์กรเป็น over-spec ที่ดันค่า license + implementation ขึ้นมาก
โดยไม่มี use case จริงรองรับ. (สอดคล้อง F-EPM-01 / GP-FUNC-13 / TOR-FIN-01).

**Procurement caveat:** อย่าตั้ง EPM เต็มรูปทั้งองค์กรเป็น Mandatory — เป็นการดันสเปก/TCO เข้าหา Oracle EPM Cloud.

**Confidence:** low (ต้นฉบับไม่มีบล็อกหลักฐาน KB/เว็บสำหรับ standout item นี้)

**หลักฐาน / Citation:**
- ไม่มี citation KB/เว็บเฉพาะใน record ต้นฉบับ (standout summary) — อ้างอิงประกอบใช้ citation ของ F-EPM-01 / GP-FUNC-13 / TOR-FIN-01 (NSPB built on Oracle EPM Cloud engine)

---

## GP-STANDOUT-03 — Fusion standout: Unified HCM on a single data model

**Capability (TH):** HCM แบบรวมศูนย์ data model เดียว
**Capability (EN):** Unified HCM on a single data model — Fusion standout
**Domain:** HCM · **iCE severity:** กลาง

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** SuitePeople เป็น HCM แบบ light — ขาดความลึกด้าน talent/workforce และไม่มี
payroll ไทยในตัว ต้องต่อเชื่อมพันธมิตร payroll ไทยภายนอก ต่างจาก Oracle HCM Cloud (Gartner Leader) ที่อยู่บน
data model เดียวกับ Finance (Fusion standout Rank 3).

**Counter / Mitigation:** HCM/Global Payroll หลายประเทศ **"ไม่เกี่ยว"** — payroll อยู่ในไทยประเทศเดียว และงาน HR/
เงินเดือนมักใช้ระบบเฉพาะของไทย/ราชการอยู่แล้ว; **SuitePeople (Core HR + Performance native) + พันธมิตร payroll
ไทย** ครอบคลุมได้. งานที่เหลือคือวางการเชื่อมต่อระบบ payroll ไทย/พันธมิตรให้กลืนกับ SuitePeople ซึ่งบริหารจัดการ
ได้. (สอดคล้อง GP-FUNC-18 / TOR-HCM-01).

**Procurement caveat:** อย่าบังคับ "unified HCM + global payroll บน data model เดียว" ที่เอียงเข้า Oracle HCM
Cloud — แยก Core HR (ผ่าน) ออกจาก global payroll (ไม่เกี่ยว).

**Confidence:** low (ต้นฉบับไม่มีบล็อกหลักฐาน KB/เว็บสำหรับ standout item นี้)

**หลักฐาน / Citation:**
- ไม่มี citation KB/เว็บเฉพาะใน record ต้นฉบับ (standout summary) — อ้างอิงประกอบใช้ citation ของ GP-FUNC-18 / TOR-HCM-01 (SuitePeople Core HR native; U.S.-only native payroll; Thai payroll via partner SuiteApp [ต้อง verify])

---

## GP-STANDOUT-06 — Fusion standout: Demand planning & SCM Cloud breadth

**Capability (TH):** วางแผนอุปสงค์ / SCM Cloud
**Capability (EN):** Demand planning & SCM Cloud breadth — Fusion standout
**Domain:** SCM · **iCE severity:** ต่ำ

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** ฟังก์ชัน Demand Planning ของ NetSuite ตื้นกว่า Oracle SCM Cloud (พยากรณ์เชิง
สถิติพื้นฐาน ไม่มี demand sensing/ML และไม่มี S&OP) ที่ยกเป็น Fusion standout Rank 6.

**Counter / Mitigation:** Demand planning/SCM Cloud **เกี่ยวข้องต่ำ** — ไม่ใช่ผู้ผลิต/กระจายสินค้าเชิงพาณิชย์
ขนาดใหญ่. งานคลังโลหิต/เวชภัณฑ์ใช้ **inventory + reorder point + lot/expiry ของ NetSuite (native)** ได้; งาน
พยากรณ์ความต้องการเลือด/เวชภัณฑ์/เซรุ่มมี use case จริงแต่ native demand planning ครอบคลุมได้. demand/supply
planning เต็มรูป (demand sensing/ML/S&OP) เป็น over-spec. (สอดคล้อง F-SCM-01 / GP-FUNC-04).

**Procurement caveat:** อย่าบังคับ "SCM Cloud breadth + demand sensing" ที่เอียงเข้า Oracle SCM Cloud.

**Confidence:** low (ต้นฉบับไม่มีบล็อกหลักฐาน KB/เว็บสำหรับ standout item นี้)

**หลักฐาน / Citation:**
- ไม่มี citation KB/เว็บเฉพาะใน record ต้นฉบับ (standout summary) — อ้างอิงประกอบใช้ citation ของ F-SCM-01 / GP-FUNC-04 (native statistical demand planning, 4 methods)

---

## GP-STANDOUT-09 — Fusion standout: Broad public + sovereign cloud regions

**Capability (TH):** region/sovereign cloud หลากหลาย
**Capability (EN):** Broad public + sovereign cloud regions — Fusion standout
**Domain:** Technical · **iCE severity:** สูง

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** ตัวเลือก data center ของ NetSuite จำกัดและไม่มี government/sovereign region
ในไทย ต่างจาก OCI ที่มี public + government + sovereign regions มากกว่า — ข้อได้เปรียบ Fusion/OCI ที่ legitimate
(Fusion standout Rank 9).

**Counter / Mitigation:** ข้อนี้ **"อาจสำคัญจริง" (ไม่ปัดทิ้ง)** — หากมีข้อกำหนด data residency ในไทยสำหรับข้อมูล
สุขภาพ/ผู้บริจาคโลหิตภายใต้ PDPA (ศูนย์บริการโลหิตแห่งชาติ) เรื่อง region/sovereign cloud อาจเป็น blocker. iCE
counter = ตรวจตัวเลือก data center ในประเทศของทั้งสองค่ายและวางแผนปิด gap ก่อน go-live (แนวทางกลาง, ไม่ปัดทิ้ง).
(สอดคล้อง NF-ARC-02 / GP-TECH-08 / TOR-TECH-04).

**Procurement caveat:** **สูง** — หากเงื่อนไข in-country/sovereign เป็น Mandatory NetSuite เสียเปรียบเชิงสถาปัตย
กรรม; ต้อง verify roadmap และชั่งกับข้อเท็จจริงว่า PDPA ไม่บังคับ localization. [ต้อง verify]

**Confidence:** low (ต้นฉบับไม่มีบล็อกหลักฐาน KB/เว็บเฉพาะสำหรับ standout item นี้; มีจุด [ต้อง verify])

**หลักฐาน / Citation:**
- ไม่มี citation KB/เว็บเฉพาะใน record ต้นฉบับ (standout summary) — อ้างอิงประกอบใช้ citation ของ GP-TECH-08 / NF-ARC-02 (no Thai DC, no EU Sovereign Cloud; Oracle AIS Cloud/Alloy Thailand) [ต้อง verify]

---

## TOR-FIN-01 — TOR: Enterprise planning & budgeting (xP&A) on ERP platform

**Capability (TH):** เครื่องมือวางแผนงบประมาณและพยากรณ์ระดับองค์กร (xP&A) บนแพลตฟอร์มเดียวกับ ERP
**Capability (EN):** Native Enterprise Planning & Budgeting (xP&A) on the same platform as the ERP
**Domain:** EPM · **iCE severity:** ต่ำ · **Priority:** Mandatory · **NetSuite ตอบได้?:** Partial

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** NSPB ยังไม่มีโมดูล Workforce/Capital planning สำเร็จรูป (Oracle Help ระบุ
รองรับเฉพาะโมดูล Financials) และเป็นแอป/ลิขสิทธิ์แยกจาก ERP — การวางแผนกำลังคน/งบลงทุนต้องสร้างเป็น driver model
เอง ไม่ใช่ template พร้อมใช้.

**Counter / Mitigation:** xP&A core (driver-based, multi-scenario, rolling forecast, predictive) ทำได้
**first-party บนเอนจิน Oracle EPM เดียวกัน** (sync GL อัตโนมัติ). การวางแผนกำลังคน/งบลงทุนทำได้ผ่าน driver-based
ใน NSPB Financials แต่ NSPB เป็นต้นทุน add-on แยกจาก ERP ที่ต้องตั้งงบ; โมดูล Workforce/Capital สำเร็จรูปเป็น
over-spec. "Partial" สมเหตุผลเฉพาะส่วน add-on/pre-built module ไม่ใช่เพราะขาด core. (สอดคล้อง F-EPM-01 /
GP-FUNC-13 / GP-STANDOUT-01).

**Procurement caveat:** ถ้อยคำ "native xP&A บนแพลตฟอร์มเดียวกับ ERP + workforce/capital ในตัว" เอียงเข้าหา Oracle
EPM Cloud — ระบุ outcome (วางงบ driver-based/scenario/rolling ได้) แทน.

**Confidence:** high

**หลักฐาน / Citation:**
- [WEB:docs.oracle.com] NetSuite Planning and Budgeting — 'supports only the Financials module. A Workforce module is not currently available.' (article_8124016549 — ตรวจแล้วมีจริง)
- [WEB:docs.oracle.com] NetSuite Planning and Budgeting Financials Overview — driver-based/trend-based/direct-input, what-if, Predictive Planning (article_7160253896 — ตรวจแล้วมีจริง)
- [WEB:netsuite.com] What is NetSuite Planning and Budgeting — produce scenario plans, multiple what-if, driver-based (financial-planning.shtml)
- [KB] Netsuite-Sales Force Automation (~0.6) — base NetSuite มีเพียง sales forecasting/GL budget; xP&A เต็มต้องใช้ NSPB add-on

---

## TOR-FIN-03 — TOR: Statutory tax / e-invoicing (e-Tax Invoice TH)

**Capability (TH):** localization และ statutory/tax compliance ในตัว + e-invoicing/e-tax ทุกประเทศ โดยไม่พึ่ง third-party
**Capability (EN):** Built-in localization & statutory/tax compliance incl. country-specific e-invoicing/e-tax, without third-party add-ons
**Domain:** Finance · **iCE severity:** สูง · **Priority:** Mandatory · **NetSuite ตอบได้?:** No (ต้นฉบับ)

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** **e-Tax Invoice/e-Receipt แบบ XML ส่งกรมสรรพากรยังไม่มี native** —
Electronic Invoicing เป็นกรอบเปล่า ต้องทำ custom template หรือใช้ partner SuiteApp; ความกว้างประเทศน้อยกว่า SAP/
Oracle.

**Counter / Mitigation:** การตอบ "No" **เกินจริง** — statutory ไทยพื้นฐาน (VAT/ภ.พ.30, ใบกำกับภาษี/เครดิตโน้ต)
รองรับผ่าน **SEA Localization + International Tax Reports ซึ่งเป็น free managed bundle ของ NetSuite เอง (ไม่ใช่
third-party)**. จุดอ่อนจริงเหลือเฉพาะ e-Tax Invoice XML → ความจริงคือ Partial ไม่ใช่ No. e-Tax Invoice/e-Receipt
เป็นข้อกำหนดไทยที่ต้องส่งกรมสรรพากร ต้องวางแผนปิด gap (custom/partner) ก่อนใช้งานจริง; เงื่อนไข "ทุกประเทศ" ไม่
เกี่ยวเพราะดำเนินงานในไทยประเทศเดียว. (สอดคล้อง GP-FUNC-16).

**Procurement caveat:** ถ้อยคำ "ทุกประเทศ + e-tax native โดยไม่พึ่ง add-on" คือการล็อกสเปก (SuiteApp ที่ใช้เป็น
ของ NetSuite เอง ไม่ใช่ third-party ตามที่อ้าง) — ระบุ e-Tax Invoice (TH) เป็น outcome.

**Confidence:** high

**หลักฐาน / Citation:**
- [WEB:docs.oracle.com] Southeast Asia Localization (free managed first-party bundle)
- [WEB:docs.oracle.com] Thailand Invoicing Features / Electronic Invoicing Overview (กรอบ ไม่มี native ไทย)
- [KB] Netsuite-Country Specific Features (0.7209)

---

## TOR-SCM-02 — TOR: Warehouse management (WMS) directed operations

**Capability (TH):** WMS รองรับ wave/zone/batch picking, directed put-away, RF/barcode, หลายคลัง/3PL
**Capability (EN):** Advanced WMS: wave/zone/batch picking, directed put-away, RF/barcode, multi-warehouse/3PL
**Domain:** SCM · **iCE severity:** กลาง · **Priority:** Important · **NetSuite ตอบได้?:** Partial

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** WMS เป็น SuiteApp ที่ต้องซื้อลิขสิทธิ์แยก และ native WMS วางตำแหน่งปริมาณ
ต่ำ-กลาง — 3PL billing เชิงลึกและ slotting optimization ระดับ enterprise (SAP EWM) อ่อนกว่า; งานคลังสูง/ซับซ้อน
มักเสริม RF-SMART.

**Counter / Mitigation:** "Partial/add-on ตื้น" ประเมินต่ำกว่าจริง — wave/zone/batch picking, directed put-away,
RF/barcode, multi-warehouse เป็น **ฟีเจอร์ในตัวของ WMS SuiteApp (first-party)**. กระทบบางหน่วย (ศูนย์บริการโลหิต/
หน่วยผลิตชีววัตถุ ที่ต้อง lot/expiry, RF, directed put-away คุมอุณหภูมิ) แต่ปริมาณไม่สูงมาก native WMS น่าจะพอ;
3PL billing/slotting อยู่นอกภารกิจ. (สอดคล้อง F-WMS-01 / GP-FUNC-06). [ต้อง verify ปริมาณจริง]

**Procurement caveat:** เขียนครอบ directed ops + lot/expiry (ที่ใช้จริง) แทน "3PL billing/slotting engineered"
ที่เอียง tier-1 WMS.

**Confidence:** medium (ต้นฉบับระบุ [ความเชื่อมั่น: กลาง])

**หลักฐาน / Citation:**
- [KB] WMS4-WMS Outbound Fulfillment (0.65) — wave; WMS Advanced Setup (0.60) — zone/batch/RF strategies
- [WEB:netsuite.com] NetSuite WMS product page — directed putaway, RF barcode, multi-location
- [WEB:houseblend.io] NetSuite WMS Optimization: Slotting & Picking — มี slotting/picking strategies (ลึกน้อยกว่ามาตรฐาน enterprise)

---

## TOR-MFG-01 — TOR: Process / mixed-mode manufacturing

**Capability (TH):** process/formula manufacturing: recipe/BOM, lot, co-/by-products, finite scheduling (APS)
**Capability (EN):** Process/formula manufacturing incl. recipes/BOM, lot/batch, co-/by-products, finite-capacity scheduling (APS)
**Domain:** Manufacturing · **iCE severity:** สูง · **Priority:** Mandatory · **NetSuite ตอบได้?:** No (ต้นฉบับ)

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** **ไม่มี GMP/regulated electronic batch record + potency management แบบพร้อม
ใช้** ต้อง custom หรือ SuiteApp ภายนอก (blendAPPS Formula & Recipe สำหรับ process mfg เชิงลึก).

**Counter / Mitigation:** TOR มัดรวม process/formula + lot/batch + co-/by-product + finite scheduling (APS) เป็น
Mandatory ข้อเดียวแล้วตัด NetSuite="No" — เป็นเทคนิคบีบ. ความจริง: **Advanced Manufacturing ครอบคลุม recipe/
formula (ระดับ workbench), co-/by-product และ finite scheduling** และฐานระบบมี lot/batch native (FEFO เป็น
first-party SuiteApp) → ตอบได้อย่างน้อย Partial. ส่วนที่ขาดจริงคือ GMP batch record ที่หน่วยผลิตเซรุ่ม-วัคซีนต้อง
ใช้ (ต้องเสริม SuiteApp/custom ก่อน go-live); APS เต็มรูปเป็น over-spec. (สอดคล้อง F-MFG-01 / GP-FUNC-01).

**Procurement caveat:** การมัดหลายความสามารถ tier-1 เข้าเป็นข้อบังคับเดียวคือล็อกสเปก — แยก GMP batch record/lot
(ที่ใช้) ออกจาก APS/full process mfg (over-spec). [ต้อง verify]

**Confidence:** medium (ต้นฉบับระบุ [ความเชื่อมั่น: กลาง])

**หลักฐาน / Citation:**
- [KB] Netsuite-Advanced Manufacturing User Guide (CoProduct 0.62 + Finite Scheduling 0.70)
- [KB] NSIMG/Inventory Management (Lot Numbered / FEFO SuiteApp 0.69)
- [WEB:docs.oracle.com] Lot Numbered Items / Finite Scheduling
- [WEB:suiteapp.com] blendAPPS Formula & Recipe Management (process mfg ลึกใช้ SuiteApp นอก)

---

## TOR-HCM-01 — TOR: Core HR & payroll

**Capability (TH):** Core HR และ Global Payroll หลายประเทศในตัว: org management, absence, benefits, statutory payroll
**Capability (EN):** Native Core HR & multi-country Global Payroll: org management, absence, benefits, statutory payroll per country
**Domain:** HCM · **iCE severity:** กลาง · **Priority:** Mandatory · **NetSuite ตอบได้?:** No (ต้นฉบับ)

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** **ไม่มี global payroll หลายประเทศและไม่มี payroll ไทยแบบ native** (มีเฉพาะ
SuitePeople U.S. Payroll) — การจ่ายเงินเดือนตามกฎหมายแรงงานไทยต้องต่อเชื่อม SuiteApp พาร์ทเนอร์ (NuSmart
International Payroll, ความครอบคลุมไทยยัง [ต้อง verify]) หรือระบบภายนอก.

**Counter / Mitigation:** การตอบ "No" ทั้งข้อไม่ถูกต้องนัก — **Core HR, org management, absence (Time-Off),
benefits/compensation มีในตัว (native)**. Payroll ไทยเป็นงานที่ใช้จริงและต้องวางสถาปัตยกรรมต่อเชื่อมกับระบบเงิน
เดือนภายนอก; multi-country payroll เป็น over-spec เพราะดำเนินงานในไทยประเทศเดียว. (หมายเหตุ misattribution จาก
ต้นฉบับ: 'Jcurve Thai Localization' เป็น localization ภาษี ไม่ใช่ payroll). (สอดคล้อง GP-FUNC-18 / GP-STANDOUT-03).

**Procurement caveat:** แยกเกณฑ์ Core HR (ผ่าน native) ออกจาก global payroll (ไม่เกี่ยว) — การผูกผลทั้งข้อไว้กับ
"multi-country global payroll" คือล็อกสเปกเอียงเข้า Oracle/SAP.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-Employee Management — SuitePeople Core HR/Time-Off/Compensation (0.7159)
- [WEB:docs.oracle.com] SuitePeople U.S. Payroll (native = US-only)
- [WEB:suiteapp.com] NuSmart International Payroll and HCM (third-party payroll; Thai coverage [ต้อง verify])
- [แก้ misattribution] 'Jcurve Thai Localization for NetSuite' เป็น localization ภาษี (VAT/WHT/master data) ไม่ใช่ payroll — ตัดออกจากหลักฐานเงินเดือนไทย

---

## TOR-HCM-02 — TOR: Talent management (performance/learning/recruiting)

**Capability (TH):** ชุด Talent ครบวงจร: recruiting, performance, learning, succession บน data model เดียวกับ Core HR
**Capability (EN):** End-to-end Talent suite — recruiting, performance, learning, succession — on the same data model as Core HR
**Domain:** HCM · **iCE severity:** ต่ำ · **Priority:** Important · **NetSuite ตอบได้?:** No (ต้นฉบับ)

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** **learning/LMS และ succession planning ไม่มี native และ recruiting/ATS มี
เพียงพื้นฐาน** — ต้องใช้ third-party ต่อเชื่อม.

**Counter / Mitigation:** "No" เกินจริง — **Performance Management มีแบบ native บน data model เดียวกับ Core HR**
(NetSuite ผ่านเกณฑ์ 'data model เดียว' สำหรับ performance ด้วยซ้ำ; เกณฑ์นี้ออกแบบมาตี SuccessFactors ที่เป็นหลาย
คลาวด์). performance (และ Core HR) ที่ใช้จริงรองรับ native; ชุด talent ครบวงจร (ATS/LMS/succession) ค่อนข้าง
over-spec สำหรับองค์กรการกุศล/การศึกษา — เลือกต่อเชื่อมเฉพาะโมดูลที่จำเป็น. (สอดคล้อง GP-FUNC-19).

**Procurement caveat:** อย่าบังคับ "end-to-end talent บน data model เดียว" ที่เอียงเข้า Oracle HCM — ระบุ
performance (ที่ใช้) เป็น outcome.

**Confidence:** high

**หลักฐาน / Citation:**
- [WEB:netsuite.com] SuitePeople Performance Management (product page)
- [KB] Netsuite-Administrator Guide — Performance Management (SuitePeople HR), Kudos (0.5788)

---

## TOR-PPM-01 — TOR: Enterprise PPM, project costing & grants

**Capability (TH):** Enterprise PPM: project costing, budget vs actual, capitalization, grants, auto-post เข้า GL
**Capability (EN):** Enterprise PPM with project costing, budget vs actual, capitalization, grants, auto-posting to GL
**Domain:** Project · **iCE severity:** กลาง · **Priority:** Important · **NetSuite ตอบได้?:** Partial

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** ไม่มี Enterprise PPM ระดับ deep WBS/EPC-grade เป็น native; Job Costing/
Project Budgeting ต้องให้ account rep เปิด, capitalization CIP→สินทรัพย์มักพึ่ง third-party (NetAsset) เพราะ base
FAM เป็น manual, grants/fund ต้องซื้อ SuiteApp NFP Financials (รายงานสำเร็จรูปอิง US-FASB ต้องปรับเป็นไทยเอง).

**Counter / Mitigation:** ติด Partial เพราะ deep WBS/EPC-grade เท่านั้น — **ฟังก์ชันหลักของ TOR (project costing,
budget vs actual, auto-post เข้า GL, capitalization ผ่าน FAM, grants/fund ผ่าน NFP Financials) NetSuite ทำได้
จริงผ่าน first-party SuiteApp**. grants/fund + capitalization ครุภัณฑ์โครงการเกี่ยวข้องจริง — ต้องตั้งงบ SuiteApp
+ ปรับรายงานให้เข้ามาตรฐานไทย; PPM tier-1 เต็มรูปเป็น over-spec. (สอดคล้อง F-PRJ-01 / GP-FUNC-21).

**Procurement caveat:** ระบุ project costing/grants/fund + auto-post GL เป็น outcome; อย่าบังคับ "deep-WBS
enterprise PPM" ที่เอียงเข้า Oracle PPM Cloud/Primavera.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-Projects (0.61) — native project costing/job costing/budgeting
- [KB] Netsuite-Non-Profit SuiteApps (0.66) — NFP Financials Grant/Fund
- [WEB:netsuite.com] NetSuite Nonprofit — Fund Accounting & Grant Management (NFP Financials)
- [WEB:community.oracle.com] FAM CIP — capitalize project costs to fixed asset
- [WEB:netgain.tech] CIP buildup via NetAsset (third-party add-on)

---

## TOR-EAM-01 — TOR: Enterprise asset management & maintenance

**Capability (TH):** EAM: work order, preventive/predictive maintenance, meter reading, ประวัติการบำรุงรักษา
**Capability (EN):** EAM with work orders, preventive/predictive maintenance, meter readings, maintenance history
**Domain:** Asset · **iCE severity:** กลาง · **Priority:** Important · **NetSuite ตอบได้?:** No (ต้นฉบับ)

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** base FAM ทำได้แค่ค่าเสื่อม ไม่มี work order; และ FSM เอียงไป field service ไม่
ใช่ predictive/condition-based EAM เต็มรูป (งานโรงงานหนัก/linear asset ยังเป็นของ SAP PM).

**Counter / Mitigation:** การให้ "No" เกินจริง — **NetSuite Field Service Management (first-party หลังซื้อ Next
Technik 2023)** ให้ work order, preventive maintenance ตามเวลา/usage, asset hierarchy และ maintenance history;
meter/usage-based (ชั่วโมง/ไมล์/รอบ) สร้าง work order อัตโนมัติได้ → ควรเป็น Partial ไม่ใช่ No. งาน PM ครุภัณฑ์/
อุปกรณ์ cold-chain ของศูนย์บริการโลหิตเกี่ยวข้องจริง ปิดได้ด้วย FSM ที่ต้องลงทุนเพิ่ม; full plant EAM/predictive
เป็น over-spec. (ต้นฉบับตัดคำ 'predictive' ออก — ยืนยันได้แค่ preventive + usage-based). (สอดคล้อง GP-FUNC-23).

**Procurement caveat:** ระบุ work order/PM/meter-based/history ที่ใช้จริง; อย่าบังคับ "predictive/condition-based
EAM เต็มรูป" ที่เอียงเข้า SAP PM.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-Fixed Assets Management (0.60) — base FAM = depreciation + maintenance schedule, ไม่มี work order
- [WEB:netsuite.com] NetSuite Field Service Management — work orders, automated preventive maintenance, asset hierarchy
- [WEB:netsuite.com] FSM datasheet — usage/meter-based maintenance auto-generates work orders
- [WEB:oracle.com] Oracle acquires Next Technik — FSM กลายเป็น first-party (2023)

---

## TOR-TECH-04 — TOR: Deployment / data residency options

**Capability (TH):** ระบุทางเลือกการติดตั้ง (public/private/sovereign/in-country) และตำแหน่ง data center ตามข้อกำหนด residency
**Capability (EN):** State deployment options (public/private/sovereign/in-country) and data-center locations meeting residency requirements
**Domain:** Technical · **iCE severity:** สูง · **Priority:** Mandatory · **NetSuite ตอบได้?:** Partial

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** จุดอ่อนจริงและปิดไม่ได้เชิงสถาปัตยกรรม — NetSuite เป็น **public multi-tenant
SaaS เท่านั้น: ไม่มี data center ในไทย ไม่มี private/sovereign region และไม่อยู่บน EU Sovereign Cloud**; ต่างจาก
gap อื่นในชุดนี้ที่ปิดด้วย SuiteApp ข้อนี้เพิ่ม in-country/sovereign region ให้ NetSuite ไม่ได้.

**Counter / Mitigation:** การตี "region จำกัด → Partial" ประเมินต่ำกว่าจริงเพราะข้อกำหนดเพียง **"ระบุทางเลือก"**
ซึ่ง NetSuite ทำได้ (ระบุได้ว่าเป็น public multi-tenant บน data center EU/NA/APAC มี data residency เชิงภูมิภาค).
in-country ไทยไม่ใช่ข้อบังคับ PDPA; Fusion SaaS public มาตรฐานก็ไม่มี region ในไทยเช่นกัน — ต่างกันที่ Oracle มี
เส้นทาง in-country (AIS Cloud/Oracle Alloy). แตะข้อมูลสุขภาพ/ผู้บริจาคโลหิตซึ่งเป็น data class อ่อนไหวสูง — หาก
องค์กรกำหนด in-country/sovereign เป็นเงื่อนไข NetSuite เสียเปรียบและต้องเคลียร์ก่อน go-live. (สอดคล้อง NF-ARC-02
/ GP-TECH-08 / GP-STANDOUT-09).

**Procurement caveat:** **สูง** — TOR ขอเพียง "ระบุทางเลือก" (NetSuite ตอบได้) แต่หากยกระดับเป็นบังคับ in-country/
sovereign region จะเอียงเข้าหา OCI/Alloy โดยตรง; PDPA ไม่บังคับ localization. [ต้อง verify in-country/sovereign
roadmap]

**Confidence:** medium (ต้นฉบับระบุ [ความเชื่อมั่น: กลาง]; มีจุด [ต้อง verify])

**หลักฐาน / Citation:**
- [WEB:netsuite.com] NetSuite Data Center datasheet — multi-region, no Thai DC
- [WEB:sota.io] NetSuite not on Oracle EU Sovereign Cloud (Q1 2026) [ต้อง verify]
- [WEB:oracle.com] Public Cloud Regions; AIS Cloud/Oracle Alloy Thailand
- [WEB:securiti.ai] Thailand PDPA — no localization mandate

---

## TOR-TECH-05 — TOR: GRC / automated SoD controls

**Capability (TH):** ควบคุมสิทธิ์ละเอียด + ตรวจ SoD อัตโนมัติ + continuous controls monitoring ในตัว
**Capability (EN):** Fine-grained access control with automated SoD checks and built-in continuous controls monitoring
**Domain:** Technical · **iCE severity:** สูง · **Priority:** Important · **NetSuite ตอบได้?:** Partial

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** **ไม่มี automated SoD เชิง preventive (block self-approval แบบ ruleset) และไม่
มี continuous controls monitoring เป็น native** — ต้องใช้ certified SuiteApp (Fastpath Assure, Netwrix
Strongpoint, Greenlight Approvals) ปิดส่วน preventive.

**Counter / Mitigation:** NetSuite มี **fine-grained access control + SoD แบบ detective (saved search/role audit
ตรวจ creator=approver) ในตัว**; ส่วน preventive ปิดด้วย **certified SuiteApp (market-standard)**. เกี่ยวข้องสูง
เพราะ SoD อยู่ใต้การตรวจของ สตง. โดยตรง — ต้องวางแผนจัดหา SuiteApp ปิด preventive SoD และออกแบบ control matrix ให้
พร้อมก่อน go-live เพื่อผ่านการตรวจ; CCM แบบ native เต็มรูปเป็นฟีเจอร์ระดับองค์กรข้ามชาติที่ over-spec สำหรับ NGO
ไทย. (สอดคล้อง NF-SEC-01 / GP-FUNC-27 / GP-TECH-11).

**Procurement caveat:** "continuous controls monitoring ในตัว" เป็น over-spec ที่มีเพียง Oracle/SAP ตอบเต็ม —
ระบุ SoD (detective + preventive ผ่าน certified add-on) เป็น outcome แทน.

**Confidence:** high

**หลักฐาน / Citation:**
- [WEB:mysuite.tech] NetSuite SoD: detective vs preventive (native ไม่ block self-approval แบบ ruleset)
- [WEB:oracle.com] Oracle Risk Management Cloud — built-in continuous controls monitoring
- [WEB:suiteapp.com] Greenlight Approvals / Fastpath Assure — preventive self-approval blocking + automated SoD
- [KB] Netsuite-Managing Users & Roles (0.6544) — access review/audit guidance (manual)

---

*จบ KB — 42 records · vertical: healthcare-public-sector · product angle: NetSuite (weakness + counter/defend). ทุก record เก็บทั้ง gap และ counter ตามหลัก BALANCED ของ iCE second-opinion; ไม่มีการระบุชื่อหน่วยงานใด ๆ.*
