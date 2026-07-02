# TOR Competitive KB — manufacturing — NetSuite Weakness & Counter

---
last_verified: "2026-06-29"
source: "TOR Requirement Bank + Gap Pack v2"
confidence_note: "Records carry per-item confidence (high/medium/low) based on whether an official Oracle/NetSuite Help, suiteapp.com, or vendor citation exists in the source. Where the source marks [ต้อง verify], the position must be re-confirmed against a live environment/vendor before use in a bid. The underlying TOR draft is a COMPETITIVE document biased toward Oracle Fusion; every gap below is paired with iCE's balanced counter-view (first-party add-on coverage, over-spec rebuttal, or procurement-fairness caveat)."
ams_review: "yearly — re-verify product positions"
---

> **How to use this file (iCE selling / defending NetSuite in a manufacturing-flavoured TOR)**
> Client identities in the raw data have been generalized to industry patterns: healthcare / blood-bank / non-profit foundation / public-sector production (e.g. serum-and-vaccine light-pharma production under GMP). The "manufacturing" cut here is a small, regulated, single-entity production profile — NOT a commercial multi-plant, cross-border manufacturer. Read every gap together with its **Counter / Mitigation** and **Procurement caveat**: most "process manufacturing / APS / S&OP / global-trade / heavy-EAM" gaps are over-spec for this profile, and several are already coverable by NetSuite first-party add-ons (Advanced Manufacturing, WMS, FSM, NSPB, NSAR, NSPCM) that run on the same Oracle engine the TOR credits only to Fusion.
>
> **Genuinely-consider items for a regulated production unit** (per iCE second opinion): GMP electronic batch record / potency (F-MFG-01, GP-FUNC-01, TOR-MFG-01) and full CAPA / GxP validation (F-QM-01, GP-FUNC-26) are the real gaps to plan for before go-live. The rest are largely over-spec or first-party-coverable.

---

## F-MFG-01 — Process / Mixed-mode Manufacturing (การผลิตแบบผสมผสาน discrete + process)

**Capability:** การผลิตแบบ mixed-mode (discrete + process) รวมสูตรการผลิต (recipe/formula) และการสืบย้อนกลับล็อต (batch genealogy) / Process / mixed-mode manufacturing (recipe/formula, batch genealogy).
**Domain:** Manufacturing · **iCE severity:** สูง (High)

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** NetSuite ฐานมาตรฐานทำได้แค่ light discrete. งาน process manufacturing (สูตร/recipe, batch genealogy, co-product) ต้องซื้อโมดูลเสริม NetSuite Advanced Manufacturing; lot/expiry เป็น native แต่ FEFO มาเป็น SuiteApp ที่ต้องติดตั้ง. ที่ขาดจริงและปิดยากคือ process mfg ระดับ GMP/ชีววัตถุเข้ม (electronic batch record เชิง regulatory, potency) ซึ่งไม่มีในตัว. Oracle Manufacturing Cloud รองรับ discrete + process + mixed-mode ในตัว.

**Counter / Mitigation:** ข้ออ้าง "อ่อนมาก / ไม่มีเลย" เกินจริง — NetSuite Advanced Manufacturing (first-party add-on) มี Recipe/Formulation Management ระดับ Manufacturing Workbench และ co-product/by-product ในตัว; lot/batch + วันหมดอายุ + traceability เป็น native (FEFO ผ่าน SuiteApp ฟรีของ NetSuite เอง). ปิด gap ที่เหลือ (GMP electronic batch record, potency) ได้ด้วย custom SuiteScript หรือ certified SuiteApp ภายนอก เช่น blendAPPS Formula & Recipe Management หรือ BatchMaster. co-product ยังสื่อตรงกับการแยกส่วนประกอบโลหิต (whole blood → เม็ดเลือดแดง/พลาสมา/เกล็ดเลือด) ซึ่ง native รองรับได้.

**Procurement caveat:** การบังคับ "mixed-mode process mfg + batch genealogy แบบ native ในตัว ไม่ใช้เครื่องมือภายนอก" ลง TOR ทั้งที่ profile จริงคือหน่วยผลิตชีววัตถุขนาดเล็ก = ผลักไปทาง Fusion/SAP โดยไม่จำเป็น. GMP batch record เกี่ยวเฉพาะหน่วยผลิตเซรุ่ม/วัคซีน ไม่ใช่ทุกหน่วย — ควรเขียนแบบ outcome-based (ต้องคุม lot/potency/traceability ได้ตามมาตรฐาน GMP) ไม่ผูกกับ "native engine" ของผลิตภัณฑ์ใด เพื่อลดความเสี่ยงถูก สตง./ผู้ยื่นรายอื่นท้วงว่าล็อกสเปก.

**Confidence:** medium

**หลักฐาน / Citation:**
- [KB] Netsuite-Advanced Manufacturing User Guide (Setting up an Assembly CoProduct 0.62)
- [KB] NSIMG/Inventory Management (FEFO Lot Allocations SuiteApp 0.69)
- [WEB:docs.oracle.com] Lot Numbered Items / Lot and Serial Number Trace
- [WEB:suiteapp.com] blendAPPS Formula & Recipe Management (ยืนยันว่า process/recipe ลึกมักใช้ SuiteApp นอก)

---

## GP-FUNC-01 — Process manufacturing (formula, batch, co/by-products) — 3-way vs Fusion vs SAP

**Capability:** การผลิตแบบกระบวนการ (สูตร/ล็อต/co-by product) / Process manufacturing (formula, batch, co/by-products).
**Domain:** Manufacturing · **iCE severity:** สูง (High)

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** NetSuite=1★ vs Oracle Fusion=4★ vs SAP S/4HANA=5★. ราว TOR: "NetSuite ไม่มี process/formula manufacturing แท้ ต้องพึ่ง SuiteApp; SAP PP/PP-PI ลึกสุดสำหรับเคมี/อาหาร/ยา." การคุมสูตรเชิง GMP เข้ม เช่น potency และ genealogy ของชีววัตถุ ยังเป็นช่องว่างจริงเทียบความลึกของ SAP/Oracle.

**Counter / Mitigation:** ซ้ำประเด็นกับ F-MFG-01 — Advanced Manufacturing มี recipe/formula (ระดับ workbench) + co-/by-product และฐานระบบมี lot/batch native (FEFO ผ่าน SuiteApp ของ NetSuite). การให้ 1★ พร้อมระบุ "ไม่มี process mfg แท้" จึงต่ำกว่าความจริง. gap ที่แท้จริง (formula ระดับ GMP/potency) ปิดด้วย SuiteApp ภายนอก (blendAPPS Formula & Recipe) หรือ custom; ศูนย์บริการโลหิตและหน่วยอื่นใช้ lot/batch native ได้พอ.

**Procurement caveat:** ความลึก SAP PP-PI/Oracle เหนือกว่าเฉพาะการผลิตชีววัตถุที่ regulated (potency/genealogy เข้ม) — เป็นข้อพึงพิจารณาเฉพาะหน่วยผลิตยา/วัคซีน ไม่ใช่ทุกหน่วย. ตั้งเป็น requirement รวมทั้งองค์กร = over-spec.

**Confidence:** medium

**หลักฐาน / Citation:**
- [KB] Netsuite-Advanced Manufacturing User Guide (Assembly CoProduct 0.62)
- [KB] Netsuite-Manufacturing (BOM/routing/Advanced Manufacturing 0.60)
- [WEB:netsuite.com] Lot Tracking native (FEFO ผ่าน SuiteApp)
- [WEB:suiteapp.com] blendAPPS Formula & Recipe Management

---

## TOR-MFG-01 — TOR spec: Process / mixed-mode manufacturing (bundled Mandatory)

**Capability:** ระบบต้องรองรับ process/formula manufacturing (recipe/BOM, lot/batch, co-/by-products) + finite-capacity scheduling (APS) / Process/formula manufacturing incl. recipes/BOM, lot/batch, co-/by-products, finite scheduling.
**Domain:** Manufacturing · **iCE severity:** สูง (High)

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** TOR draft = Mandatory, ตัด NetSuite = "No". Differentiator: "NetSuite ไม่มี process mfg/APS แท้ → No; SAP PP-PI เด่น, Oracle Mfg แข็ง." ที่ขาดจริงคือ GMP/regulated electronic batch record + potency management แบบพร้อมใช้ ต้อง custom หรือ SuiteApp ภายนอก.

**Counter / Mitigation:** TOR มัดรวม process/formula + lot/batch + co-/by-product + finite scheduling เป็น Mandatory ข้อเดียวแล้วตัด "No" — เป็นเทคนิคบีบ NetSuite ให้ตก. ความจริง: Advanced Manufacturing ครอบคลุม recipe/formula (workbench), co-/by-product และ finite scheduling; ฐานระบบมี lot/batch native (FEFO SuiteApp) → NetSuite ตอบได้อย่างน้อย **Partial ไม่ใช่ No**. ปิดส่วน GMP batch record ด้วย blendAPPS/custom.

**Procurement caveat:** การมัดหลายความสามารถ tier-1 (process + APS เต็มรูป) เข้าเป็นข้อบังคับเดียวคือการล็อกสเปก. แยก requirement ตาม outcome จริง: lot/expiry สูง (โลหิต/หน่วยผลิตชีววัตถุ), co-product เกี่ยวการแยกส่วนประกอบโลหิต, GMP batch record เกี่ยวเฉพาะหน่วยผลิตวัคซีน, ส่วน APS เต็มรูป = over-spec. เขียนแยกจะเป็นธรรมและกัน สตง. ท้วง.

**Confidence:** medium (source marks [ต้อง verify] on the summary)

**หลักฐาน / Citation:**
- [KB] Netsuite-Advanced Manufacturing User Guide (CoProduct 0.62 + Finite Scheduling 0.70)
- [KB] NSIMG/Inventory Management (Lot Numbered / FEFO SuiteApp 0.69)
- [WEB:docs.oracle.com] Lot Numbered Items / Finite Scheduling
- [WEB:suiteapp.com] blendAPPS Formula & Recipe Management (process mfg ลึกใช้ SuiteApp นอก)

---

## F-MFG-02 — Advanced Planning & Scheduling (APS / finite scheduling)

**Capability:** การวางแผน/จัดตารางการผลิตแบบ finite/constraint-based (APS) / Finite / constraint-based advanced planning & scheduling.
**Domain:** Manufacturing · **iCE severity:** แทบไม่มีผล (Negligible)

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** TOR อ้าง "NetSuite มีแค่ supply planning พื้นฐาน — ไม่มี finite/constraint-based scheduling." Oracle Production Scheduling ทำ finite capacity scheduling. จุดด้อยจริงที่เหลือ: NetSuite เป็น heuristic ระดับ work center ไม่ใช่ constraint solver หลายข้อจำกัดเต็มรูปแบบ Oracle/SAP.

**Counter / Mitigation:** ข้ออ้าง "ไม่มี finite scheduling" **ไม่ถูกต้อง** — NetSuite Advanced Manufacturing มี finite/capacity scheduling ในตัวจริง (ปล่อย work order เมื่อเครื่องจักร/แรงงานว่าง, คำนวณ capacity ปัจจุบัน+อนาคต) ยืนยันทั้งใน KB และหน้า Help ทางการ "Finite Scheduling". ไม่ต้อง add-on ภายนอก — เป็นส่วนหนึ่งของ Advanced Manufacturing.

**Procurement caveat:** APS แบบ constraint solver เต็มรูป (Oracle Production Scheduling/SAP APS) เป็น over-spec สำหรับหน่วยผลิตสเกลเล็ก — ไม่มี use case จริง. ห้ามใส่ "constraint-based APS ในตัว" เป็น Mandatory เพราะเป็นการล็อกสเปกที่งานจริงไม่ต้องใช้.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-Advanced Manufacturing User Guide (Finite Scheduling 0.70; Scheduling Production 0.67)
- [WEB:docs.oracle.com] NetSuite Applications Suite — Finite Scheduling (ns-online-help/bridgehead_1508338278)

---

## GP-FUNC-02 — Advanced production scheduling (finite capacity, APS) — 3-way

**Capability:** วางแผนการผลิตแบบจำกัดกำลัง (APS/finite scheduling) / Advanced production scheduling (finite capacity, APS).
**Domain:** Manufacturing · **iCE severity:** แทบไม่มีผล (Negligible)

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** NetSuite=1★ vs Fusion=4★ vs SAP=5★. ราว TOR: "NetSuite มีแค่ basic work order; ไม่มี finite scheduling/constraint-based ในตัว." ส่วนที่ยังด้อยจริง: ความสามารถ optimize แบบ constraint-based APS เต็มรูปยังเทียบ Oracle Production Scheduling/SAP ไม่ได้.

**Counter / Mitigation:** ซ้ำกับ F-MFG-02 — NetSuite Advanced Manufacturing มี finite/capacity scheduling ในตัว (ยืนยันด้วย KB + หน้า Help ทางการ, ความเชื่อมั่นสูง). การระบุ "1★ มีแค่ basic work order ไม่มี finite scheduling" **เกินจริง**; finite/capacity scheduling พื้นฐานมี native จริง เพียง optimize ยังด้อยกว่า Oracle/SAP.

**Procurement caveat:** งานผลิตสเกลเล็กไม่มี use case ของ APS เต็มรูป → over-spec ชัดเจน. ตั้งเป็นเกณฑ์ให้คะแนนแบบ tier-1 = ล็อกสเปก.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-Advanced Manufacturing User Guide (Finite Scheduling 0.70; Scheduling Production 0.67)
- [WEB:docs.oracle.com] NetSuite — Finite Scheduling (Help page)

---

## GP-FUNC-03 — Discrete MRP II & shop-floor execution — 3-way

**Capability:** MRP II / shop-floor control เชิงลึก / Discrete MRP II & shop-floor execution.
**Domain:** Manufacturing · **iCE severity:** ต่ำ (Low)

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** NetSuite=2★ vs Fusion=4★ vs SAP=5★. NetSuite (ผ่าน Advanced Manufacturing) มี MRP/supply planning, routing/WIP และ shop-floor control (operation-level reporting, scrap/rework, mobile/tablet) ในตัว **แต่ตื้นกว่า SAP PP/MES** ในงาน discrete ขนาดใหญ่ที่มี shop-floor execution ซับซ้อน. ข้ออ้างเรื่องความตื้นจึงถูกต้องตามข้อเท็จจริง.

**Counter / Mitigation:** ยอมรับ gap แต่วางกรอบให้ถูก: NetSuite Advanced Manufacturing มี MRP II / routing / WIP / shop-floor reporting (scanner/tablet) ครบพอสำหรับ work order + lot ระดับพื้นฐาน. ความลึก MES/PP ของ SAP เหนือกว่าเฉพาะโรงงาน discrete ขนาดใหญ่ — depth ส่วนเกินไม่กระทบผลใช้งานจริงของหน่วยผลิตขนาดเล็ก.

**Procurement caveat:** deep MES = over-spec สำหรับหน่วยที่ไม่ได้เดินไลน์ผลิต discrete ระดับโรงงานใหญ่. หน่วยผลิตชีววัตถุ/ศูนย์โลหิตใช้ work order + lot พื้นฐานก็เพียงพอ.

**Confidence:** medium

**หลักฐาน / Citation:**
- [KB] NSIMG/Inventory Management (supply planning / regenerate supply plan 0.57)
- [KB] Netsuite-Advanced Manufacturing User Guide (Shop Floor: Scanner/Tablet data)
- [WEB:netsuite.com] Advanced Manufacturing datasheet (finite capacity scheduling, batch management, MES)

---

## F-MFG-03 — Project / Engineer-to-Order (ETO) Manufacturing

**Capability:** การผลิตแบบ engineer-to-order (ETO) / project manufacturing ผูกต้นทุนกับ project/WBS / Project / ETO manufacturing.
**Domain:** Manufacturing · **iCE severity:** แทบไม่มีผล (Negligible)

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** NetSuite ผูก work order กับ project ได้ แต่ไม่มี engineer-to-order/EPC project-manufacturing costing เชิงลึกแบบ Oracle Project Manufacturing หรือ SAP PS+PP — ต้อง customize หนักหากจะทำ. จุดอ่อนนี้เป็นจริง (Oracle รองรับในตัว).

**Counter / Mitigation:** ยอมรับว่าเป็นจุดอ่อนจริงในเชิงฟีเจอร์ แต่ไม่มี use case: ETO/EPC คือผลิตตามสั่งออกแบบเฉพาะ (ต่อเรือ/อากาศยาน/รับเหมาก่อสร้าง) ซึ่ง profile หน่วยผลิตชีววัตถุ/สาธารณกุศลไม่มีโมเดลธุรกิจนี้เลย. ไม่ต้องลงทุนปิด gap.

**Procurement caveat:** การบรรจุ ETO/project manufacturing ใน TOR เท่ากับล็อกสเปกที่ไม่ได้ใช้จริง — over-spec ชัดเจน. ควรตัดออกจาก requirement.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-Manufacturing (work order types / project link ~0.60)
- [KB] Netsuite-Projects (create order/link to project 0.61)

---

## F-QM-01 — Quality Management (QM / CAPA)

**Capability:** การบริหารคุณภาพในตัว: inspection plans, non-conformance (NCR), CAPA / Quality management (inspection / NCR / CAPA).
**Domain:** Quality · **iCE severity:** สูง (High)

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** TOR อ้าง "NetSuite QM SuiteApp พื้นฐาน — ไม่มี inspection plans/non-conformance/CAPA เชิงลึก." Oracle Quality Cloud มี inspection, non-conformance, CAPA. ที่ขาดจริง: CAPA เต็มรูป (root cause 5-Why/Fishbone/8D → corrective action → effectiveness verification) และ pharma GxP validation / electronic batch record ไม่มีแบบ out-of-the-box.

**Counter / Mitigation:** ข้ออ้าง "ไม่มี" **เกินจริง** — NetSuite Quality Management SuiteApp (native, ฟรี) ทำ inspection plan, quality inspection queue และจัดการ non-conformance (NCR) ผ่าน SuiteFlow พร้อม lot/serial traceability ใช้งานได้จริงในสเกลหน่วยผลิตชีววัตถุ/ศูนย์โลหิตปัจจุบัน. ปิด gap CAPA เต็มรูป/validation ด้วยการ config บน SuiteFlow เอง หรือซื้อ QMS SuiteApp เฉพาะ (Intellect QMS, QT9). ไม่ควรกลับไปเหมาว่าได้ CAPA/validation ครบในตัว.

**Procurement caveat:** CAPA เต็มรูปและ pharma GxP validation เป็น gap จริงที่ต้องวางแผนปิดก่อน go-live (เกี่ยวข้องสูงกับหน่วยผลิตเซรุ่ม/วัคซีนและงานโลหิต) — เขียน requirement แบบ outcome (ต้องมี inspection/NCR/CAPA + traceability ตามมาตรฐาน GMP/ISO 13485) ไม่ผูก "native ในตัว" เพื่อเปิดทาง config/SuiteApp และกันการล็อกสเปก.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-Quality User Guide (0.56)
- [KB] NSIMG (0.57) — non-conformance ทำผ่าน SuiteFlow
- [WEB:brokenrubik.com] NetSuite Quality Management Guide (partner blog) — ระบุชัดว่าไม่ใช่ QMS ทดแทนงาน validation ยา
- [WEB:docs.oracle.com] NetSuite Quality Inspection Queue

---

## GP-FUNC-26 — Quality Management (QMS), inspection plans — 3-way

**Capability:** ระบบคุณภาพ (QMS) / แผนตรวจสอบ / Quality Management (QMS), inspection plans.
**Domain:** Quality · **iCE severity:** สูง (High)

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** NetSuite=1★ vs Fusion=4★ vs SAP=5★. ราว TOR: "NetSuite Quality Mgmt ตื้น; SAP QM ลึกสุดสำหรับ regulated industry." ที่ขาดจริง: CAPA เต็มรูปต้อง config บน SuiteFlow หรือซื้อ QMS SuiteApp; ไม่ใช่ระบบ validated GxP เต็มรูปแบบ SAP QM — ความลึกระดับ regulated pharma ยังเป็นช่องว่างจริง.

**Counter / Mitigation:** เช่นเดียวกับ F-QM-01 — Quality Management SuiteApp (native) มี inspection plan + non-conformance ผ่าน SuiteFlow + lot/serial traceability ใช้งานได้จริง จึงไม่สมควรได้ 1★ (ตามจริงราว 3★). ช่วยรองรับแนวทาง ISO 13485 ได้บางส่วน. ปิด gap CAPA/validation ด้วย config หรือ QMS SuiteApp เฉพาะ.

**Procurement caveat:** เรตติ้ง 1★ ทำให้เข้าใจผิดว่า NetSuite แทบไม่มีระบบคุณภาพ ทั้งที่มีโมดูล native ใช้ได้จริง — ใช้ข้อนี้โต้ตอนตอบ TOR. ความลึก validated GxP เต็มรูป (SAP QM) เป็น over-spec ยกเว้นการผลิตยา/ชีววัตถุที่ regulated จริง ซึ่งควรเขียน outcome-based.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-Quality User Guide (0.56)
- [KB] NSIMG (0.57) — non-conformance ทำผ่าน SuiteFlow
- [WEB:brokenrubik.com] NetSuite Quality Management Guide (partner blog)
- [WEB:docs.oracle.com] NetSuite Quality Inspection Queue

---

## F-SCM-01 — Demand & Supply Planning + S&OP

**Capability:** วางแผนความต้องการ/อุปทาน + statistical forecasting + S&OP / Demand/supply planning & S&OP.
**Domain:** SCM · **iCE severity:** ต่ำ (Low)

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** TOR อ้าง "NetSuite Demand Planning พื้นฐานมาก — ไม่มี statistical forecasting/S&OP ระดับองค์กร" (ให้คะแนน 1 = ต้อง add-on/custom). Oracle SCM Planning Cloud เป็น tier-1 platform. gap จริง: ไม่มี demand sensing/ML และไม่มี S&OP (Sales & Operations Planning) ระดับองค์กร.

**Counter / Mitigation:** คะแนน 1 เหมารวมเกินไป — NetSuite มี Demand Planning, Supply Planning และ Distribution Resource Planning (DRP) เป็นฟีเจอร์ในตัว (เปิดใช้ภายใต้ Advanced Inventory) พร้อมพยากรณ์เชิงสถิติ 4 วิธี (Linear Regression, Moving Average, Seasonal Average, Sales Forecast). ข้ออ้าง "ไม่มี statistical forecasting" **ไม่จริง**. gap จริงคือ S&OP enterprise ซึ่งเป็นเพียงครึ่งเดียวของข้อกำหนด. การพยากรณ์ความต้องการเลือด/เซรุ่มใช้ native demand planning พอตามสเกล (เลือดอายุสั้นอาจ custom วิธีพยากรณ์).

**Procurement caveat:** S&OP เต็มรูปเกินความจำเป็นของหน่วยผลิต/กระจายชีววัตถุที่ไม่ใช่ผู้ผลิตเชิงพาณิชย์ขนาดใหญ่ — over-spec. เขียน requirement ให้เป็น "พยากรณ์ความต้องการเชิงสถิติ" ไม่ใช่ "S&OP/IBP ในตัว".

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-Inventory Management (0.69) — Demand Planning เป็นฟีเจอร์ในตัว + Distribution Resource Planning + projection methods
- [KB] NSIMG (0.66) — Demand Plans/Supply Plans, Seasonal Average method, Supply Allocation หลาย location
- [WEB:docs.oracle.com] NetSuite Applications Suite — Calculating Item Demand (4 วิธีพยากรณ์เชิงสถิติ native, /ns-online-help/section_N2290234.html)

---

## GP-FUNC-04 — Demand planning & statistical forecasting — 3-way

**Capability:** วางแผนอุปสงค์ / พยากรณ์ / Demand planning & statistical forecasting.
**Domain:** SCM · **iCE severity:** ต่ำ (Low)

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** NetSuite=1★ vs Fusion=5★ vs SAP=4★. ราว TOR: "NetSuite Demand Planning จำกัดมาก; Oracle SCM Demand Mgmt เป็นจุดแข็งที่นำหน้าทั้งคู่." gap จริง: เป็นวิธีพื้นฐาน ไม่มี demand sensing/ML และ collaboration แบบ Oracle SCM Demand Management.

**Counter / Mitigation:** NetSuite Demand Planning เป็นฟีเจอร์ในตัว มีพยากรณ์เชิงสถิติ 4 วิธี (Linear Regression/Moving Average/Seasonal Average/Sales Forecast) — การจัด 1★ "จำกัดมาก" ต่ำกว่าจริง. การพยากรณ์ความต้องการเลือด/วัคซีน/เซรุ่มด้วย native (วิธีพื้นฐาน) ครอบคลุมได้ ไม่ต้องถึง tier-1 demand forecasting.

**Procurement caveat:** การลดเหลือ 1★ สะท้อนการตั้งสเปกเทียบ tier-1 มากกว่าความต้องการจริงขององค์กรกุศล — over-spec.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-Inventory Management (0.69) — Demand Planning วิเคราะห์ stock demand จาก historical
- [KB] NSIMG (0.66) — Demand Plans/Supply Plans, Seasonal Average method
- [WEB:docs.oracle.com] NetSuite Applications Suite — Calculating Item Demand (Linear Regression/Moving Average/Seasonal Average/Sales Forecast)

---

## GP-STANDOUT-06 — Fusion standout: Demand planning & SCM Cloud breadth

**Capability:** วางแผนอุปสงค์ / SCM Cloud (Fusion standout) / Demand planning & SCM Cloud breadth.
**Domain:** SCM · **iCE severity:** ต่ำ (Low)

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** Fusion standout (Rank 6): Oracle SCM Cloud (Demand/Supply/Inventory) กว้างและรวมในชุดเดียวกับ ERP — ครบกว่าและกลืนกับ Finance. จุดอ่อนจริง: ฟังก์ชัน Demand Planning ของ NetSuite ตื้นกว่า Oracle SCM Cloud (พยากรณ์เชิงสถิติพื้นฐาน ไม่มี demand sensing/ML และไม่มี S&OP).

**Counter / Mitigation:** เกี่ยวข้องต่ำกับ profile หน่วยผลิต/กระจายชีววัตถุที่ไม่ใช่ผู้ผลิต/กระจายสินค้าเชิงพาณิชย์ขนาดใหญ่. งานคลังโลหิต/เวชภัณฑ์ใช้ inventory + reorder point + lot/expiry ของ NetSuite ได้ครอบคลุม. NetSuite เองก็เป็น unified suite (born-in-cloud) จึงกลืน SCM กับ Finance ได้เช่นกัน.

**Procurement caveat:** demand/supply planning เต็มรูป (demand sensing/ML/S&OP) เป็น over-spec — ตั้งเป็นเกณฑ์ให้แต้ม Fusion โดยไม่มี use case จริงรองรับ = ล็อกสเปก.

**Confidence:** medium

**หลักฐาน / Citation:**
- [WEB:netsuite.com] NetSuite Demand Planning / Inventory (reorder point, lot/expiry — native) *(อ้างอิงจาก differentiator note; ไม่มี KB citation เฉพาะข้อ standout นี้)*
- Cross-ref: GP-FUNC-04, F-SCM-01 (same capability, KB-backed)

---

## GP-FUNC-15 — Advanced cost accounting (multi-method costing) — 3-way

**Capability:** ต้นทุนขั้นสูง (actual/standard หลายวิธี) / Advanced cost accounting (multi-method costing).
**Domain:** Finance · **iCE severity:** ต่ำ (Low)

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** NetSuite=2★ vs Fusion=4★ vs SAP=5★. ราว TOR: "NetSuite costing จำกัดวิธี; SAP CO/ML (material ledger) ลึกสุด." ข้อจำกัดจริง: วิธีต้นทุนตั้งครั้งเดียวที่ item record และเปลี่ยนไม่ได้หลังบันทึก; Multi-Book ตั้ง standard cost ต่างกันรายบัญชีได้ (per-book amount) แต่ **ไม่ใช่** การตั้งคนละวิธีต้นทุนต่อบัญชี. ที่ขาดจริงคือ actual costing หลาย valuation/หลายสกุลเชิงลึกแบบ SAP Material Ledger (CO/ML).

**Counter / Mitigation:** เรตติ้ง 2★ "costing จำกัดวิธี" ประเมินต่ำเกิน — NetSuite รองรับ 7 วิธีต้นทุน native: Average, FIFO, LIFO, Standard (พร้อม variance + Cost Category + Cost Template), Group Average, Lot-Numbered และ Specific (serialized) รวม Landed Cost. Lot-Numbered costing ตรงกับการคิดต้นทุนรายล็อตของผลิตภัณฑ์โลหิต/เซรุ่ม/เซรุ่มแก้พิษงู. Standard/Average + Lot-Numbered ครอบคลุมงานจริงของหน่วยผลิตชีววัตถุและศูนย์โลหิต.

**Procurement caveat:** actual costing หลาย valuation/transfer pricing ระดับ SAP Material Ledger เป็นของจริงแต่ over-spec สำหรับ profile นี้. ตั้งเป็น requirement บังคับ = ล็อกสเปกไปทาง SAP.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] NSIRM (0.657) — Costing Methods: Average/FIFO/LIFO/Standard/Group Average/Lot/Specific
- [KB] Netsuite-Item Record Management (0.62) — Group Average, Standard Costing, Cost Category, Landed Cost
- [KB] Netsuite-Multi-Book Accounting + Item Record Mgmt (0.55) — ตั้ง standard cost ต่างกันรายบัญชี (per-book amount)

---

## F-EPM-04 — Multidimensional Profitability & Costing (ABC)

**Capability:** การวิเคราะห์กำไร/ต้นทุนหลายมิติ (activity-based costing) / Multidimensional profitability & activity-based costing.
**Domain:** EPM · **iCE severity:** ต่ำ (Low)

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** TOR อ้าง "NetSuite ไม่มี engine วิเคราะห์ profitability/allocation แบบหลายมิติ (activity-based)." Oracle PCMCS ทำ multidimensional profitability & cost allocation. gap จริง: NetSuite core ไม่มี ABC engine วิเคราะห์กำไร/ต้นทุนหลายมิติเต็มรูปแบบ — ABC/profitability หลายมิติระดับ PCMCS ต้องซื้อโมดูล add-on แยก.

**Counter / Mitigation:** ข้ออ้าง "ไม่มี engine" **เกินจริง** — NetSuite core มี native allocation: Allocation Schedules ทั้ง Fixed และ Dynamic ปันส่วนข้าม account/department/class/location/custom segment ถ่วงน้ำหนักด้วย Statistical Accounts ซึ่ง NetSuite Help ระบุเองว่า "useful in advanced costing such as Activity Based Costing and Usage Based Costing" + Custom Segments หลายมิติ + Project Profitability. ABC engine เต็มรูปมีโมดูล NetSuite Profitability & Cost Management (NSPCM) ใน NetSuite EPM (แพลตฟอร์มเดียวกับ Oracle PCMCS/Hyperion) เป็น add-on แยกไลเซนส์ — ปิด gap ได้เมื่อจำเป็น.

**Procurement caveat:** การบังคับ ABC engine ระดับ PCMCS แบบ native ในตัวลง TOR เป็น over-spec — native allocation + statistical accounts + custom segments ปันส่วนต้นทุนทางอ้อมเข้าโปรแกรม/กองทุน/cost center ได้พอสำหรับงานสาธารณกุศล. เขียน outcome-based (ต้องปันส่วนต้นทุนทางอ้อมได้) ไม่ผูก "native engine".

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-General Accounting (0.59) — Allocation Schedules ปันส่วนข้าม account/department/class/location/custom segment
- [KB] Netsuite-Statistical Accounting (0.60) — Dynamic Allocation ถ่วงน้ำหนักด้วย Statistical Account
- [KB] Netsuite-Projects (0.50) — Project Profitability / Job Costing
- [WEB:docs.oracle.com] NetSuite Help — Working with Allocation Schedules Weighted by the Balance of a Statistical Account (chapter_3866895958): ระบุชัด "useful in advanced costing such as Activity Based Costing and Usage Based Costing" — verified
- [WEB:netsuite.com] NetSuite Profitability and Cost Management (EPM add-on) — ABC/driver-based allocation, profitability หลายมิติ (verified, ขายคู่กับ NetSuite ERP)
- [WEB:oracle.com] Oracle PCMCS — Profitability & Cost Management (สาย EPM/Hyperion เดียวกับ NSPCM)

---

## GP-FUNC-23 — Enterprise Asset Management & maintenance (EAM) — 3-way

**Capability:** บริหารสินทรัพย์/ซ่อมบำรุงองค์กร / Enterprise asset management & maintenance (EAM).
**Domain:** Asset · **iCE severity:** กลาง (Medium)

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** NetSuite=1★ vs Fusion=4★ vs SAP=5★. ราว TOR: "NetSuite FAM = แค่ fixed-asset depreciation; ไม่มี maintenance/work order. SAP PM/EAM ลึกสุด." จุดอ่อนจริง: Base FAM (SuiteApp) ทำได้แค่เสื่อมราคา/ตีราคาใหม่/จำหน่าย + เก็บ maintenance schedule/insurance **แต่ไม่มี work order**. EAM โรงงานหนัก (linear asset/reliability) ยังเป็นจุดแข็ง SAP PM.

**Counter / Mitigation:** เรต 1★ ต่ำกว่าความจริง — NetSuite Field Service Management (first-party หลัง Oracle ซื้อ Next Technik ต.ค. 2023, เดิม NextService) เพิ่ม work order, preventive maintenance ตามเวลา/การใช้งาน (meter-based: ชั่วโมง/ไมล์/รอบ → สร้างงานอัตโนมัติ), asset hierarchy/sub-asset และ maintenance history. เป็นโมดูลซื้อแยกและเอียงไปทาง field service. งาน PM ครุภัณฑ์การแพทย์/แล็บ/cold-chain ปิดได้ด้วย FSM หรือเชื่อม biomedical CMMS เฉพาะทาง.

**Procurement caveat:** EAM โรงงานหนัก/predictive-condition-based เต็มรูปเป็น over-spec สำหรับ profile นี้ (รพ.มักใช้ biomedical CMMS เฉพาะทางอยู่แล้ว). ระบุ requirement เป็น work order + PM + maintenance history ตาม outcome, ไม่บังคับ "EAM plant-grade ในตัว".

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-Fixed Assets Management (0.60) — depreciation + maintenance schedule/insurance, ไม่มี work order
- [WEB:netsuite.com] NetSuite Field Service Management — work orders, automated preventive maintenance, asset hierarchy
- [WEB:netsuite.com] FSM datasheet — usage/meter-based maintenance (hours/mileage/cycles) auto-generates jobs
- [WEB:oracle.com] Oracle acquires Next Technik — FSM กลายเป็น first-party (2023)

---

## TOR-EAM-01 — TOR spec: Enterprise Asset Management & maintenance

**Capability:** ระบบต้องมี EAM รองรับ work order, preventive/predictive maintenance, meter reading, maintenance history / EAM with work orders, preventive/predictive maintenance, meter readings, maintenance history.
**Domain:** Asset · **iCE severity:** กลาง (Medium)

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** TOR draft = Important, ตัด NetSuite = "No". Differentiator: "NetSuite FAM = depreciation เท่านั้น → No; SAP PM/EAM เด่น, Oracle Maintenance Cloud แข็ง." จุดอ่อนจริง: base FAM ทำได้แค่ค่าเสื่อม ไม่มี work order; และ FSM เอียงไป field service ไม่ใช่ predictive/condition-based EAM เต็มรูป (งานโรงงานหนัก/linear asset ยังเป็นของ SAP PM).

**Counter / Mitigation:** การให้ "No" **เกินจริง — ควรเป็น Partial**. NetSuite Field Service Management (first-party หลังซื้อ Next Technik 2023) ให้ work order, preventive maintenance (ตามเวลา/usage), asset hierarchy และ maintenance history; meter/usage-based (ชั่วโมง/ไมล์/รอบ) สร้าง work order อัตโนมัติได้ — แต่เป็นโมดูลซื้อแยก. หมายเหตุ: source ตัดคำว่า "predictive" ออกจากร่าง — ยืนยันได้แค่ preventive + usage-based เท่านั้น.

**Procurement caveat:** คำว่า "predictive maintenance" ในตัว TOR เป็นจุดที่ NetSuite ยืนยันได้แค่ preventive/usage-based — ควรท้วงให้แก้ requirement เป็น preventive + meter-based (ซึ่ง FSM ตอบได้) มิฉะนั้น "predictive/condition-based EAM เต็มรูป" คือ over-spec ที่ล็อกไปทาง SAP/Oracle. งาน PM ครุภัณฑ์/cold-chain ปิดด้วย FSM ที่ลงทุนเพิ่มได้.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-Fixed Assets Management (0.60) — base FAM = depreciation + maintenance schedule, ไม่มี work order
- [WEB:netsuite.com] NetSuite Field Service Management — work orders, automated preventive maintenance, asset hierarchy
- [WEB:netsuite.com] FSM datasheet — usage/meter-based maintenance auto-generates work orders
- [WEB:oracle.com] Oracle acquires Next Technik — FSM กลายเป็น first-party (2023)

---

## Summary — severity roll-up (manufacturing cut, 16 records)

| iCE severity | Records |
|---|---|
| **สูง (High)** | F-MFG-01, GP-FUNC-01, TOR-MFG-01, F-QM-01, GP-FUNC-26 |
| **กลาง (Medium)** | GP-FUNC-23, TOR-EAM-01 |
| **ต่ำ (Low)** | GP-FUNC-03, F-SCM-01, GP-FUNC-04, GP-STANDOUT-06, GP-FUNC-15, F-EPM-04 |
| **แทบไม่มีผล (Negligible)** | F-MFG-02, GP-FUNC-02, F-MFG-03 |

**Defense priority for a regulated single-entity production profile:** the only genuinely-plan-before-go-live gaps are **GMP electronic batch record / potency** (F-MFG-01, GP-FUNC-01, TOR-MFG-01) and **full CAPA / GxP validation** (F-QM-01, GP-FUNC-26), both closeable via SuiteApp/custom. Everything at "ต่ำ / แทบไม่มีผล" is either first-party-coverable (Advanced Manufacturing, WMS, FSM, NSPB, NSPCM on the same Oracle engine) or over-spec that iCE should challenge on procurement-fairness grounds (outcome-based wording, not product-locked features — reducing สตง./bidder-challenge risk).

*Source basis: TOR Requirement Bank + Gap Pack v2, cross-checked against iCE balanced second-opinion (2026-06-29). Client identity generalized to healthcare / blood-bank / non-profit / public-sector production patterns per iCE anti-name-drop policy.*
