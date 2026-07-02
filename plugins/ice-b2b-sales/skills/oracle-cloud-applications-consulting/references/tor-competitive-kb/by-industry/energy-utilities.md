# TOR Competitive KB — energy-utilities — Oracle Fusion Standout & TOR Weaponization

---
last_verified: "2026-06-29"
source: "TOR Requirement Bank + Gap Pack v2"
confidence_note: "Records selected are those mapped to the energy-utilities vertical (EAM + ESG). All Oracle Fusion advantages, TOR wording, and citations are copied from the source flat files; nothing is invented. Where a record carries no formal KB citation, the confidence is marked accordingly. This KB is a COMPETITIVE artifact for the case where iCE SELLS Oracle Fusion — it is intentionally biased toward Fusion, but the iCE balanced second-opinion caveat is preserved in every record so the team stays honest with the buyer and avoids procurement-fairness exposure."
ams_review: "yearly — re-verify product positions"
---

> **วิธีใช้ / How to use this KB (energy-utilities):** เอกสารนี้ใช้ตอนที่ iCE เสนอ **Oracle Fusion** เป็นหลัก — ชี้จุดที่ Fusion ชนะจริง พร้อม "ถ้อยคำ TOR" (TH+EN) ที่สเปกให้คู่แข่ง NetSuite ตอบได้เพียง Partial/No. **แต่** ต้องอ่านคู่กับ **iCE caveat** ทุกข้อเสมอ เพราะ (ก) บาง gap ปิดได้ด้วย add-on first-party ของ NetSuite (FSM, NSPB/NSAW), (ข) หลายข้อเป็น over-spec สำหรับโปรไฟล์ healthcare / blood-bank / non-profit / public-sector, และ (ค) การล็อกสเปกไปที่ผลิตภัณฑ์เดียวมีความเสี่ยงถูกท้วงติงจาก สตง./ผู้ยื่นรายอื่น. เขียน requirement แบบ **outcome-based** จะปลอดภัยและเป็นธรรมกว่า.
>
> **Scope note (energy-utilities):** ในชุดข้อมูลต้นทางไม่มี TOR record ที่เป็น utility-core แท้ (เช่น meter-to-cash, network asset, outage management). record ที่ผูกกับ vertical นี้คือกลุ่ม **Enterprise Asset Management (EAM) / maintenance** และ **Sustainability / ESG reporting** ซึ่งเป็นแกน asset-intensive และ ESG ที่พบในองค์กร energy-utilities. iCE severity ของทั้งชุดอยู่ระดับ "กลาง" ถึง "แทบไม่มีผล" ในบริบท non-profit/public-sector ต้นทาง — เมื่อขายเข้า utility จริงที่ asset-heavy น้ำหนักของ EAM จะสูงขึ้น แต่ยังต้องยึดหลัก outcome-based เพื่อเลี่ยงการล็อกสเปก.

---

## GP-FUNC-23 — Enterprise Asset Management & maintenance (EAM)

- **Capability (TH):** บริหารสินทรัพย์/ซ่อมบำรุงองค์กร (EAM)
- **Capability (EN):** Enterprise Asset Management & maintenance (EAM)
- **Domain:** Asset — **iCE severity:** กลาง (medium)
- **Positioning scores (source):** NetSuite 1★ · Oracle Fusion 4★ · SAP S/4HANA 5★ · Gap Severity (source draft): High · Fusion เด่นสุด: ✔

**Oracle Fusion advantage (Standout):**
Oracle นำเสนอ **Oracle Maintenance Cloud** เป็นโมดูล EAM แบบ first-party บนโมเดลข้อมูลเดียวของ Fusion — ครอบคลุม work order, preventive maintenance และ asset hierarchy ในตัว (source: Differentiator note ระบุ "Oracle Maintenance Cloud แข็ง ✔"). เทียบกับ NetSuite ที่ base **FAM (Fixed Assets Management)** ทำได้เพียงค่าเสื่อมราคา/ตีราคาใหม่/จำหน่าย + เก็บ maintenance schedule/insurance โดย **ไม่มี work order** — งานซ่อมบำรุงจริงต้องซื้อ **NetSuite Field Service Management (FSM)** แยกต่างหาก และ FSM เอียงไปทาง field service ไม่ใช่ predictive/condition-based EAM เต็มรูป. สำหรับองค์กร asset-intensive (โรงงานหนัก, linear asset, reliability-centered maintenance) ความลึกของ EAM ฝั่ง Oracle/SAP อยู่เหนือ NetSuite อย่างชัดเจน.
Oracle Fusion advantage in English: Oracle Maintenance Cloud is a first-party EAM module on Fusion's single data model, covering work orders, preventive maintenance, and asset hierarchy natively; NetSuite's base FAM does depreciation only (no work order) and requires the separately-licensed Field Service Management add-on, which leans toward field service rather than full predictive/condition-based EAM.

**TOR wording to weaponize (ภาษาไทย):**
"ระบบต้องมีการบริหารสินทรัพย์และซ่อมบำรุง (Enterprise Asset Management) รองรับ work order, preventive/predictive maintenance, meter reading และประวัติการบำรุงรักษา — ทั้งหมดเป็นความสามารถในตัว (native) บนแพลตฟอร์มเดียวกับ ERP โดยไม่ต้องพึ่งโมดูล field-service ที่ซื้อแยกหรือ SuiteApp บุคคลที่สาม และต้องรองรับ predictive/condition-based maintenance เต็มรูปสำหรับสินทรัพย์เชิงเส้น (linear asset) และงาน reliability."

**TOR wording (English):**
"The solution shall provide native Enterprise Asset Management (EAM) with work orders, preventive AND predictive/condition-based maintenance, meter readings, and full maintenance history, delivered on the same platform as the core ERP without reliance on a separately-licensed field-service add-on or third-party SuiteApp, and shall support linear/complex-asset and reliability-centered maintenance."

**iCE caveat (over-spec / procurement-fairness):**
- การให้ NetSuite = "1★ / No" นั้น **เกินจริง** — NetSuite Field Service Management (first-party หลัง Oracle ซื้อ Next Technik ต.ค. 2023, เดิม NextService) ให้ work order, preventive maintenance ตามเวลา/การใช้งาน (meter-based: ชั่วโมง/ไมล์/รอบ → สร้างงานอัตโนมัติ), asset hierarchy/sub-asset และ maintenance history ได้จริง. ตำแหน่งที่ยุติธรรมคือ **Partial ไม่ใช่ No**.
- จุดที่ Fusion ชนะจริงและควรใช้เป็นหมัดฟาด คือ **predictive/condition-based EAM เต็มรูป + linear asset/reliability** (งานโรงงานหนัก) — ไม่ใช่แค่ work order/PM/meter ซึ่ง NetSuite ปิดได้ด้วย FSM.
- สำหรับโปรไฟล์ healthcare / blood-bank / non-profit / public-sector: PM ครุภัณฑ์การแพทย์/แล็บ/cold-chain "เกี่ยวข้องจริง" แต่ full-plant EAM/predictive เป็น **over-spec** (มักใช้ biomedical CMMS เฉพาะทางแทน). เมื่อขายเข้า **energy-utilities จริงที่ asset-heavy** น้ำหนัก EAM จะสูงขึ้นและ predictive/linear-asset จะ "เกี่ยวข้องจริง" มากกว่าเคสต้นทาง — แต่ยังต้องเขียนแบบ outcome-based.
- **Procurement risk:** การบังคับ "native เท่านั้น ห้ามซื้อแยก/ห้าม SuiteApp" เป็นการล็อกสเปกที่อาจถูกท้วงติง (สตง./ผู้ยื่นรายอื่น) เพราะทั้ง Oracle เองก็คิดค่า Maintenance Cloud เป็นโมดูล — แนะนำผูก requirement กับผลลัพธ์ (uptime/asset availability/มี audit trail ของงานซ่อม) แทนการระบุสถาปัตยกรรมผลิตภัณฑ์.

**Confidence:** high
- (เหตุผล: มี KB citation + web citation ทางการ, และแหล่งระบุ [ความเชื่อมั่น: สูง])

**หลักฐาน / Citation:**
- [KB] Netsuite-Fixed Assets Management (0.60) — depreciation + maintenance schedule/insurance, ไม่มี work order
- [WEB:netsuite.com] NetSuite Field Service Management — work orders, automated preventive maintenance, asset hierarchy
- [WEB:netsuite.com] FSM datasheet — usage/meter-based maintenance (hours/mileage/cycles) auto-generates jobs
- [WEB:oracle.com] Oracle acquires Next Technik — FSM กลายเป็น first-party (2023)

---

## TOR-EAM-01 — TOR: Enterprise Asset Management & maintenance

- **Capability (TH):** ระบบบริหารสินทรัพย์และซ่อมบำรุง (EAM) — work order, preventive/predictive maintenance, meter reading, ประวัติการบำรุงรักษา
- **Capability (EN):** Enterprise Asset Management (EAM) with work orders, preventive/predictive maintenance, meter readings, and maintenance history
- **Domain:** Asset / EAM — **iCE severity:** กลาง (medium)
- **TOR attributes (source):** Type: Functional · Priority: Important · NetSuite ตอบได้? (source draft): **No** · Differentiator note: "NetSuite FAM = depreciation เท่านั้น → No; SAP PM/EAM เด่น, Oracle Maintenance Cloud แข็ง ✔"

**Oracle Fusion advantage (Standout):**
นี่คือ record ระดับ "ถ้อยคำ TOR สำเร็จรูป" ที่คู่กับ GP-FUNC-23. Oracle **Maintenance Cloud** ตอบข้อกำหนดนี้ในตัวบนแพลตฟอร์ม Fusion เดียว (work order + PM + asset hierarchy + history) ขณะที่ NetSuite base FAM ให้แค่ค่าเสื่อม จึงถูกจัดเป็น "No" ในร่างเชิงแข่งขัน. Fusion จึงได้เปรียบเมื่อ TOR เรียก EAM แบบ end-to-end บน single platform.
Oracle Fusion advantage in English: This is the ready-to-drop TOR spec paired with GP-FUNC-23. Oracle Maintenance Cloud answers work order + PM + asset hierarchy + history natively on the single Fusion platform, whereas NetSuite base FAM covers depreciation only — the reason the competitive draft scores NetSuite "No."

**TOR wording to weaponize (ภาษาไทย):**
"ระบบต้องมีการบริหารสินทรัพย์และซ่อมบำรุง (Enterprise Asset Management) รองรับ work order, preventive/predictive maintenance, meter reading และประวัติการบำรุงรักษา"
(เวอร์ชันเสริมความคมเชิงแข่งขัน: "...โดยเป็นความสามารถ native ในชุดผลิตภัณฑ์เดียวกับ ERP และรองรับ predictive/condition-based maintenance สำหรับสินทรัพย์เชิงเส้น (linear asset) — ไม่ใช่เพียง preventive/usage-based ผ่านโมดูล field-service ที่ซื้อแยก")

**TOR wording (English):**
"The solution shall provide Enterprise Asset Management (EAM) with work orders, preventive/predictive maintenance, meter readings, and maintenance history."
(Competitively sharpened variant: "...delivered as native capability within the same product suite as the core ERP, supporting predictive/condition-based maintenance for linear assets — not merely preventive/usage-based maintenance via a separately-licensed field-service add-on.")

**iCE caveat (over-spec / procurement-fairness):**
- การให้ "No" **เกินจริง — ควรเป็น Partial**. NetSuite FSM (first-party หลังซื้อ Next Technik 2023) ตอบส่วน work order/PM/meter/history ได้ (แม้ต้องซื้อแยก). งาน EAM โรงงานหนัก/linear asset ยังเป็นของ SAP PM / Oracle Maintenance Cloud จริง.
- **สำคัญ — ข้อควรระวังเรื่องคำว่า "predictive":** แหล่งต้นทางบันทึกว่า [ตัดคำว่า predictive ออกจากร่าง: ยืนยันได้แค่ preventive + usage-based สำหรับ NetSuite]. หากจะเขียน TOR บังคับ "predictive/condition-based" ต้องมั่นใจว่าเป็นความต้องการจริงของงาน ไม่ใช่คำที่ใส่เพื่อกัน NetSuite อย่างเดียว — มิฉะนั้นเสี่ยงถูกมองว่าล็อกสเปก.
- โปรไฟล์ healthcare / blood-bank / non-profit / public-sector: PM ครุภัณฑ์/อุปกรณ์ cold-chain "เกี่ยวข้องจริง" ปิดได้ด้วย FSM ที่ต้องลงทุนเพิ่ม; full-plant EAM/predictive เป็น over-spec ไม่มี use case ในเคสต้นทาง. บริบท energy-utilities จริง (asset-heavy) จะยกน้ำหนักนี้ขึ้น.
- **Procurement risk:** ระบุ "native เท่านั้น" หรือบังคับ predictive ทั้งที่ภารกิจไม่ต้องการ = เสี่ยงถูกท้วงจาก สตง./ผู้ยื่นรายอื่น. แนะนำ outcome-based (เช่น "ต้องบันทึก/ติดตาม work order, PM ตามรอบ, meter reading และประวัติซ่อมบำรุงพร้อม audit trail") ให้หลายผลิตภัณฑ์แข่งได้อย่างเป็นธรรม.

**Confidence:** high
- (เหตุผล: มี KB + web citation ทางการ และแหล่งระบุ [ความเชื่อมั่น: สูง])

**หลักฐาน / Citation:**
- [KB] Netsuite-Fixed Assets Management (0.60) — base FAM = depreciation + maintenance schedule, ไม่มี work order
- [WEB:netsuite.com] NetSuite Field Service Management — work orders, automated preventive maintenance, asset hierarchy
- [WEB:netsuite.com] FSM datasheet — usage/meter-based maintenance auto-generates work orders
- [WEB:oracle.com] Oracle acquires Next Technik — FSM กลายเป็น first-party (2023)

---

## GP-FUNC-28 — Sustainability / ESG reporting

- **Capability (TH):** รายงานความยั่งยืน / ESG
- **Capability (EN):** Sustainability / ESG reporting
- **Domain:** ESG — **iCE severity:** แทบไม่มีผล (negligible in source profile)
- **Positioning scores (source):** NetSuite 1★ · Oracle Fusion 4★ · SAP S/4HANA 4★ · Gap Severity (source draft): Med · Fusion เด่นสุด: ✔

**Oracle Fusion advantage (Standout):**
Oracle มีโมดูล sustainability/ESG ในตัวมากกว่า NetSuite (source: "Oracle & SAP มี sustainability/ESG modules") — สามารถเก็บและรายงานตัวชี้วัดความยั่งยืนบนแพลตฟอร์มเดียว ขณะที่ NetSuite **ยังไม่มีโมดูล ESG/sustainability native เชิงลึก** ต้องทำผ่าน data model ที่ยืดหยุ่น + NSPB/NSAW + custom report และ SuiteApp ภายนอก (Carbon Accounting for NetSuite โดย CarbonSuite, RSM ESG Reporting Package). สำหรับ energy-utilities ที่มักอยู่ใต้แรงกดดันการเปิดเผยคาร์บอน/ESG ความพร้อมของโมดูลในตัวเป็นข้อได้เปรียบเชิงเรื่องเล่าของ Fusion.
Oracle Fusion advantage in English: Oracle ships more in-suite sustainability/ESG capability than NetSuite; NetSuite has no deep native ESG module and must rely on flexible data model + NSPB/NSAW + custom reports plus third-party SuiteApps. For utilities under carbon/ESG disclosure pressure, an in-suite module is a narrative advantage for Fusion.

**TOR wording to weaponize (ภาษาไทย):**
"ระบบต้องมีความสามารถด้านการรายงานความยั่งยืน/ESG ในตัว (native) — รองรับการเก็บข้อมูลคาร์บอน/พลังงาน, การคำนวณ emission และการออกรายงานตามมาตรฐานสากล (เช่น ISSB/IFRS S1-S2, GRI) โดยไม่ต้องพึ่ง SuiteApp บุคคลที่สามหรือ custom report ภายนอกเป็นหลัก."

**TOR wording (English):**
"The solution shall provide native Sustainability/ESG reporting — including carbon/energy data capture, emissions calculation, and disclosure reporting aligned to international standards (e.g., ISSB/IFRS S1-S2, GRI) — without primary reliance on third-party SuiteApps or external custom reporting."

**iCE caveat (over-spec / procurement-fairness):**
- ข้อกล่าวอ้างเรื่อง gap **ถูกต้อง** (NetSuite ไม่มี ESG module เชิงลึก native) — แต่ NetSuite ปิดได้ด้วย NSPB/NSAW + custom report + SuiteApp (Carbon Accounting for NetSuite, RSM ESG Reporting Package) และมีทิศทางรองรับ ISSB/IFRS S1-S2 ผ่าน partner.
- **iCE severity = แทบไม่มีผล** สำหรับโปรไฟล์ non-profit/public-sector: การรายงาน ESG ภาคบังคับ (CSRD/GRI/ISSB assurance) มุ่งบริษัทจดทะเบียน/ข้ามชาติ ไม่ใช่องค์กรสาธารณกุศล (มีเพียงเชิงสมัครใจเพื่อผู้บริจาค) จึงเป็น over-spec ในเคสต้นทาง.
- **บริบท energy-utilities:** utility จดทะเบียน/รัฐวิสาหกิจขนาดใหญ่ที่มีภาระเปิดเผย ESG จริง อาจยกน้ำหนักข้อนี้ขึ้นเป็น "เกี่ยวข้อง" — ตรงนี้ต้อง verify ภาระการเปิดเผยจริงของหน่วยงานก่อน ห้ามสมมติ. ถ้าไม่มีภาระบังคับ การใส่ข้อนี้แบบ Mandatory คือ over-spec.
- **Procurement risk:** บังคับ "native เท่านั้น" ทั้งที่ผลลัพธ์การรายงานทำได้ด้วยหลายสถาปัตยกรรม = เสี่ยงล็อกสเปก. เขียนแบบ outcome-based (ต้องออกรายงาน ESG/คาร์บอนตามมาตรฐานที่หน่วยงานผูกพันจริง พร้อม audit trail) จะเป็นธรรมกว่า.

**Confidence:** medium
- (เหตุผล: มี web citation (suiteapp.com / rsmus.com / netsuite.com) แต่เป็นแหล่ง product/partner ไม่มี KB internal citation, และแหล่งระบุ [ความเชื่อมั่น: กลาง])

**หลักฐาน / Citation:**
- [WEB:suiteapp.com] Carbon Accounting for NetSuite (Built for NetSuite)
- [WEB:rsmus.com] RSM ESG Reporting Package for NetSuite
- [WEB:netsuite.com] A Guide to ESG

---

## สรุปเชิงยุทธวิธี (energy-utilities) — Tactical wrap

- **หมัดที่คมที่สุดของ Fusion ใน vertical นี้ = EAM เชิงลึก (predictive/condition-based + linear asset/reliability)** ผ่าน Oracle Maintenance Cloud บน single platform — NetSuite ปิดได้แค่ระดับ preventive/usage-based ผ่าน FSM ที่ซื้อแยก. ให้สเปกรอบ predictive/linear-asset/reliability ไม่ใช่แค่ work order/PM/meter (ซึ่ง NetSuite ตอบได้).
- **ESG เป็นหมัดรอง** — Fusion มีโมดูลในตัวมากกว่า แต่ในโปรไฟล์ non-profit/public-sector ต้นทางเป็น over-spec; ใน utility จดทะเบียนจริงต้อง verify ภาระเปิดเผยก่อนใช้เป็น Mandatory.
- **เส้นแดง (iCE):** อย่าเขียน "native เท่านั้น / ห้าม SuiteApp / บังคับ predictive" โดยไม่มีความต้องการจริงรองรับ — ทั้ง GP-FUNC-23, TOR-EAM-01, GP-FUNC-28 มี counter-view ว่า NetSuite ปิด gap ได้ระดับหนึ่ง และการล็อกสเปกเสี่ยงถูกท้วงจาก สตง./ผู้ยื่นรายอื่น. เขียน requirement แบบ outcome-based ตามภารกิจจริงของหน่วยงานเสมอ.
- **หมายเหตุความครอบคลุม:** ชุดข้อมูลต้นทางไม่มี TOR record utility-core เฉพาะ (meter-to-cash, network/outage management) — vertical นี้จับได้เฉพาะแกน EAM + ESG. อย่าอ้าง capability utility-specific ที่ไม่มีในแหล่ง.
