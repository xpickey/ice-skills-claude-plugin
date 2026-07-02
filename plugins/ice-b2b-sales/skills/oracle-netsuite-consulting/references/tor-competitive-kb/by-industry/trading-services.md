# TOR Competitive KB — trading-services — NetSuite Weakness & Counter

---
last_verified: "2026-06-29"
source: "TOR Requirement Bank + Gap Pack v2"
confidence_note: "แหล่งข้อมูลตั้งต้นเป็น 'ชุดร่าง TOR เชิงแข่งขัน' ที่ออกแบบให้ NetSuite ตอบได้แค่ Partial/No และ Oracle Fusion ตอบ Fully — จึงมี bias ไปทาง Oracle. KB นี้เก็บทั้ง Gap (ตามร่าง TOR) และ Counter/Mitigation (มุมมองสมดุลของ iCE) ควบคู่กันเสมอ. ระดับ Confidence ต่อข้อสะท้อนว่ามีหลักฐาน KB/เอกสารทางการอ้างอิงหรือไม่ — ข้อที่ติดป้าย [ต้อง verify] ควรยืนยันกับ environment จริง/ผู้ขายก่อนตัดสินใจ. This KB is used when iCE SELLS or DEFENDS NetSuite against a Fusion-biased TOR."
ams_review: "yearly — re-verify product positions"
---

## บริบทของ vertical นี้ / How to read this file

**trading-services** ครอบคลุมงานจัดซื้อ-จัดหา (procurement/sourcing), การบริหารซัพพลายเออร์และสัญญา, การกระจาย/โลจิสติกส์, การค้าและ localization หลายประเทศ, และการเสนอราคาเชิงพาณิชย์ (CPQ). ในบริบทลูกค้าจริงที่ร่าง TOR ชุดนี้อ้างอิง (องค์กรกลุ่ม healthcare / blood-bank / non-profit foundation / public-sector ที่ดำเนินงานในประเทศเป็นหลัก) ความสามารถ "ระดับข้ามชาติ/เชิงพาณิชย์เต็มรูป" จำนวนมากในหมวดนี้เป็น over-spec — จุดที่ควรพิจารณาจริงมีเพียงไม่กี่ข้อ (โดยเฉพาะ Contract Lifecycle Management และการคัดกรอง/ประเมินซัพพลายเออร์เชิงคุณภาพในงานที่อยู่ใต้การตรวจสอบ). แต่ละหัวข้อด้านล่างแยก **Gap** (จุดที่ NetSuite เสียเปรียบตามร่าง TOR) ออกจาก **Counter / Mitigation** (แนวทางป้องกัน/ปิด gap ด้วย first-party add-on, certified SuiteApp, custom หรือ over-spec rebuttal) และ **Procurement caveat** (ความเสี่ยงเชิงจัดซื้อจัดจ้าง — การล็อกสเปกกับผลิตภัณฑ์เดียวมีความเสี่ยงถูกท้วงติงจาก สตง./ผู้ยื่นรายอื่น).

---

## F-FIN-02 — ความกว้างของ localization ตามกฎหมายหลายประเทศ / Breadth of statutory localizations

- **Capability (TH):** ความกว้างของ localization ตามกฎหมายหลายประเทศ
- **Capability (EN):** Breadth of statutory localizations (multi-country tax)
- **Domain:** Finance / Tax
- **iCE severity:** แทบไม่มีผล (negligible)

**จุดที่ NetSuite สู้ไม่ได้ (Gap):**
NetSuite SuiteTax รองรับประเทศแบบ pre-certified น้อยกว่า Oracle Fusion จริง — หลายประเทศต้องใช้ SuiteApp/partner. Oracle Fusion มี global tax engine + localization หลายประเทศแบบ pre-certified ที่กว้างกว่า. ร่าง TOR ขอให้ผู้เสนอราคา "ระบุจำนวนประเทศที่รองรับแบบ native" ซึ่งเป็นเกณฑ์ที่ Oracle ได้เปรียบโดยตรง.

**Counter / Mitigation:**
NetSuite มี SuiteTax engine + ชุด Country Localization / International Tax Reports กว่า 50 ประเทศ (รวมไทยผ่าน Southeast Asia Localization + International Tax Reports ซึ่งเป็น SuiteApp ที่ NetSuite เผยแพร่เองแบบ free managed bundle). สำหรับองค์กรที่ดำเนินงานในไทยประเทศเดียว NetSuite รองรับไทยครบ (ใบกำกับภาษี / ภ.พ.30 ผ่าน Southeast Asia Localization) — ส่วนที่ Oracle เหนือกว่าคือ "ประเทศอื่นที่องค์กรไม่ได้ใช้". จำนวนประเทศที่ pre-certified น้อยกว่า Oracle จริง แต่ไม่ใช่ use case ของลูกค้าในประเทศ.

**Procurement caveat:**
การตั้งสเปกให้ผู้เสนอราคา "ระบุจำนวนประเทศที่รองรับ native" คือการล็อกสเปกที่ไม่สะท้อนความต้องการจริงขององค์กรที่อยู่ประเทศเดียว — เสี่ยงถูกท้วงติงว่าเป็นเกณฑ์ที่ออกแบบมาเพื่อกีดกัน. ควรเขียน requirement แบบอิงผลลัพธ์ (รองรับ statutory ไทยครบตามที่กรมสรรพากรกำหนด) แทนการนับจำนวนประเทศ.

- **Confidence:** high
- **หลักฐาน / Citation:**
  - [KB] Netsuite-Country Specific Features (0.7295)
  - [WEB:docs.oracle.com] List of Country-Specific/SuiteTax Localization Features
  - [WEB:suitecertified.com] NetSuite Country Localizations 50+ (secondary — corroborated)

---

## F-WMS-02 — การบริหารการขนส่ง (TMS) / Transportation management

- **Capability (TH):** การบริหารการขนส่ง (TMS)
- **Capability (EN):** Transportation management (TMS)
- **Domain:** SCM
- **iCE severity:** แทบไม่มีผล (negligible)

**จุดที่ NetSuite สู้ไม่ได้ (Gap):**
NetSuite ไม่มี TMS เต็มรูปในตัว — ไม่มี native carrier rating engine, route optimization และ freight settlement มีเพียง shipping integration (FedEx/UPS/USPS real-time rate + label). Oracle OTM เป็น full TMS. ร่าง TOR ให้คะแนน NetSuite "0 — ทำไม่ได้เลย".

**Counter / Mitigation:**
Shipping integration เป็น native อยู่แล้ว และ TMS เต็มรูปปิดได้ด้วย certified SuiteApp เช่น SuiteFleet, FreightPOP, Pacejet — ดังนั้นการให้คะแนน 0 "ทำไม่ได้เลย" จึงแรงเกินไป. TMS ระดับ Oracle OTM ออกแบบสำหรับผู้ส่งสินค้าข้ามชาติ ไม่ใช่ภารกิจกระจายสินค้า/เวชภัณฑ์ในประเทศ. งานกระจายในประเทศด้วยรถ/ผู้ส่งของตนเองอาจได้ประโยชน์เล็กน้อยจาก last-mile route/dispatch (SuiteFleet SuiteApp) แต่ไม่ต้องใช้ TMS พาณิชย์ (carrier rating/freight settlement) ระดับ enterprise.

**Procurement caveat:**
การบังคับ TMS full-suite (carrier rating + route optimization + freight settlement) ใน TOR สำหรับองค์กรที่กระจายสินค้าในประเทศเป็นหลัก = over-spec/ล็อกสเปก — เสี่ยงถูกท้วงว่าเป็นเกณฑ์ที่ไม่มี use case จริงรองรับ.

- **Confidence:** high
- **หลักฐาน / Citation:**
  - [KB] Netsuite-Shipping Guide (0.59) — carrier label integration เท่านั้น ไม่มี TMS native (theme tms top score 0.59)
  - [WEB:netsuite.com] What Is a Transportation Management System (article)
  - [WEB:suitefleet.com] NetSuite Route Optimization / TMS SuiteApp (Azdan) — route optimization/dispatch เสริมภายนอกแบบ SuiteApp

---

## F-PRC-01 — การจัดหาเชิงกลยุทธ์ (RFx / e-Auction) / Strategic sourcing

- **Capability (TH):** การจัดหาเชิงกลยุทธ์ (RFx / e-Auction)
- **Capability (EN):** Strategic sourcing (RFx / e-auction)
- **Domain:** Procurement
- **iCE severity:** ต่ำ (low)

**จุดที่ NetSuite สู้ไม่ได้ (Gap):**
ร่าง TOR อ้างว่า NetSuite ไม่มี sourcing engine (RFx/e-auction) ในตัว และให้คะแนน "0 — ทำไม่ได้เลย". Oracle Procurement Cloud (Sourcing) มี RFx + e-auction ครบในชุดเดียว.

**Counter / Mitigation:**
ข้ออ้างนี้คลาดเคลื่อน — NetSuite มี Request for Quote (RFQ) เป็นฟีเจอร์ native (ต้องเปิด feature ก่อนใช้): ตั้งช่วงเสนอราคา, ผู้ขายยื่นราคาหลาย tier/price break ผ่าน Vendor Center, มี Award column เปรียบเทียบ/มอบรางวัล และเมื่อบันทึกระบบ auto-สร้าง Purchase Contract หนึ่งใบต่อผู้ขายที่ได้รับรางวัล (ยืนยันจาก docs.oracle.com). สิ่งที่ไม่มี native จริงคือ **การประมูลย้อนกลับสด (live reverse e-auction) เท่านั้น** — คะแนน 0 จึงผิดข้อเท็จจริง งาน sourcing จริงส่วนใหญ่ (RFQ + เปรียบเทียบ + ออกสัญญา) NetSuite ทำได้ในตัว.

**Procurement caveat:**
การให้คะแนน 0 ทั้งที่ RFQ เป็น native ทำให้เกณฑ์นี้ดูถูกออกแบบมาเพื่อกีดกัน — e-auction เป็นเพียงส่วนเดียว (ไม่ใช่ทั้งหมด) ของ requirement. การล็อกสเปก "e-auction ในตัวเท่านั้น" กับองค์กรที่แทบไม่มี use case ประมูลย้อนกลับ = ความเสี่ยงเชิงจัดซื้อ ควรเขียนแบบ outcome-based (รองรับ RFx + เปรียบเทียบ + ออกสัญญา).

- **Confidence:** high
- **หลักฐาน / Citation:**
  - [WEB:docs.oracle.com] NetSuite Request for Quote (RFQ) — native feature, Vendor Center bid, Award column, auto Purchase Contract per awarded vendor; ที่ไม่มี native = live reverse e-auction เท่านั้น. (อ้างอิงเดิมใน record F-PRC-01)

---

## F-PRC-02 — การคัดกรอง/บริหารผู้ขาย (SRM Portal) / Supplier qualification & management portal

- **Capability (TH):** การคัดกรอง/บริหารผู้ขาย (SRM Portal)
- **Capability (EN):** Supplier qualification / SRM portal
- **Domain:** Procurement
- **iCE severity:** กลาง (medium)

**จุดที่ NetSuite สู้ไม่ได้ (Gap):**
NetSuite vendor portal พื้นฐาน — ไม่มี supplier qualification / onboarding / performance ครบวงจร. Oracle มี Supplier Portal + Supplier Qualification ครบ. ร่าง TOR ให้คะแนน "1 — ต้อง add-on/custom".

**Counter / Mitigation:**
ต้องแยกสองส่วน:
1. **Vendor performance** — มี native บางส่วน: portlet On-Time Delivery Performance / late orders / Vendor Return Amount และ predictive "Vendor Delivery Performance Scores" แต่ตัว predictive ผูกกับ Supply Chain Control Tower (โมดูลเสริมที่ต้องเปิด/มีค่าใช้จ่าย). "Vendor Scorecard" ที่ NetSuite โฆษณาคือ KPI Scorecard ทั่วไปที่สร้างจาก custom KPI/saved search ไม่ใช่ scorecard 4 KPI สำเร็จรูป (quality rejection ต้องใช้โมดูล Quality Management).
2. **Qualification/onboarding** แบบแบบสอบถาม/ขึ้นทะเบียน — อ่อนจริง ต้องใช้ certified SuiteApp (เช่น Gatekeeper) หรือ custom.

สำหรับงานที่ต้องคัดกรอง/ประเมินคุณภาพซัพพลายเออร์อย่างเป็นระบบ (เช่น สายการผลิตชีววัตถุ/light-pharma ภายใต้ GMP) จุดนี้เกี่ยวข้องจริงและ NetSuite อ่อน — แต่ปิด gap ได้ด้วย SuiteApp/custom ต้นทุนบริหารจัดการได้.

**Procurement caveat:**
เกณฑ์ "SRM ครบวงจรในตัว" ที่ผูกกับ Oracle Supplier Qualification โดยตรงมีความเสี่ยงล็อกสเปก — ควรระบุผลลัพธ์ (มีกระบวนการคัดกรอง+ขึ้นทะเบียน+ประเมิน พร้อม audit trail) และเปิดให้ปิดด้วย SuiteApp certified ได้ ไม่ผูกกับโมดูลเฉพาะผลิตภัณฑ์.

- **Confidence:** medium — (no tagged [KB]/[WEB] citation in source record; based on NetSuite product-knowledge prose — verify against docs.oracle.com before live-bid use)
- **หลักฐาน / Citation:**
  - (ตาม record F-PRC-02) native vendor performance portlet (On-Time Delivery / Vendor Return Amount); predictive Vendor Delivery Performance Scores ผ่าน Supply Chain Control Tower; KPI Scorecard = custom KPI/saved search; qualification/onboarding ต้องใช้ SuiteApp (เช่น Gatekeeper) หรือ custom.

---

## GP-FUNC-05 — S&OP / Integrated Business Planning / Sales & Operations Planning (S&OP / IBP)

- **Capability (TH):** S&OP / Integrated Business Planning
- **Capability (EN):** Sales & Operations Planning (S&OP / IBP)
- **Domain:** SCM
- **iCE severity:** แทบไม่มีผล (negligible)

**จุดที่ NetSuite สู้ไม่ได้ (Gap):**
NetSuite ไม่มีโมดูล S&OP/IBP ในตัว — "forecasting" ใน KB เป็น Sales Force Automation (พยากรณ์ pipeline/โอกาสขายแบบ probability-weighted) ไม่ใช่กระบวนการ S&OP เชิงปฏิบัติการ. โมดูล S&OP/IBP แท้คือ Oracle SCP Cloud และ SAP IBP (แยก license). Gap Severity ในร่าง = Critical.

**Counter / Mitigation:**
ข้อเท็จจริงถูกต้องว่า NetSuite ไม่มี S&OP/IBP native — แต่ S&OP/IBP เป็นกระบวนการ consensus เชื่อมแผนขาย-ผลิต-การเงินสำหรับองค์กรผลิต/กระจายสินค้าเชิงพาณิชย์ขนาดใหญ่. สำหรับองค์กรที่ไม่ได้รัน S&OP/IBP แบบบริษัทผลิตข้ามชาติ ความสามารถนี้แทบไม่ได้ใช้ — เป็น over-spec rebuttal ที่ตรงตัว (แม้หน่วยงานที่ผลิตชีววัตถุ/วัคซีนภายในองค์กร ก็ยังไม่ถึงระดับ consensus planning เชิงพาณิชย์).

**Procurement caveat:**
การบรรจุ S&OP/IBP แบบ Mandatory ใน TOR = over-spec/ล็อกสเปกไปทาง Oracle — เสี่ยงถูกท้วงว่าเป็นเกณฑ์ที่ออกแบบให้ NetSuite ตอบไม่ได้ ทั้งที่ไม่มี use case จริง.

- **Confidence:** high
- **หลักฐาน / Citation:**
  - [KB] Netsuite-Sales Force Automation (0.62) — 'forecasting' = sales pipeline/probability-weighted ไม่ใช่ S&OP
  - [KB] netsuite_kb — ค้น 'S&OP/IBP' ไม่พบโมดูลจริง (hit สูงสุด 0.50 นอกเรื่อง) = หลักฐานว่าไม่มี native
  - [WEB:sap.com] SAP Integrated Business Planning — เป็นผลิตภัณฑ์เฉพาะแยกต่างหาก
  - [WEB:netsuite.com] What Is Integrated Business Planning — บทความให้ความรู้ ไม่ใช่โมดูลในผลิตภัณฑ์

---

## GP-FUNC-07 — การขนส่ง (TMS) / โลจิสติกส์ / Transportation Management (TMS)

- **Capability (TH):** การขนส่ง (TMS) / โลจิสติกส์
- **Capability (EN):** Transportation Management (TMS)
- **Domain:** SCM
- **iCE severity:** แทบไม่มีผล (negligible)

**จุดที่ NetSuite สู้ไม่ได้ (Gap):**
NetSuite ไม่มี TMS native — มีแค่ shipping label integration; TMS เต็มรูป (carrier rating, route optimization, freight settlement) ต้องต่อ SuiteApp/3rd party. NetSuite: 0 · Oracle Fusion: 4 · SAP S/4HANA: 5. Gap Severity = High.

**Counter / Mitigation:**
ข้ออ้างถูกในเชิงเทคนิค แต่ TMS (carrier rating/route optimization/freight settlement) เป็นความสามารถของบริษัทโลจิสติกส์/ผู้ส่งออกข้ามชาติ. งานกระจายในประเทศใช้ shipping integration (native) + last-mile dispatch SuiteApp ก็เพียงพอ. สำหรับองค์กรที่ไม่มีการบริหารขนส่งเชิงพาณิชย์ระดับองค์กรเป็นกระบวนการหลัก นี่คือ over-spec.

**Procurement caveat:**
การบังคับใส่ TMS ใน TOR สำหรับองค์กรสาธารณกุศล/ในประเทศ = over-spec/ล็อกสเปก — เสี่ยงถูกท้วงติง ควรเขียนแบบ outcome-based (รองรับการจัดส่ง/ติดตามพัสดุในประเทศ).

- **Confidence:** high
- **หลักฐาน / Citation:**
  - [KB] Netsuite-Shipping Guide (0.59) — theme tms มีแต่ shipping label integration ไม่มี TMS native
  - [WEB:netsuite.com] NetSuite Logistics ERP / TMS article — TMS เป็น integration/partner ไม่ใช่โมดูล native
  - [WEB:suitefleet.com] Top 20 Transportation Management Systems 2026 — ทั้งหมดเป็น SuiteApp/partner

---

## GP-FUNC-08 — การค้าระหว่างประเทศ / พิธีการศุลกากร / Global Trade Management & customs/compliance

- **Capability (TH):** การค้าระหว่างประเทศ / พิธีการศุลกากร
- **Capability (EN):** Global Trade Management & customs/compliance
- **Domain:** SCM
- **iCE severity:** แทบไม่มีผล (negligible)

**จุดที่ NetSuite สู้ไม่ได้ (Gap):**
NetSuite ไม่มีโมดูล Global Trade Management/พิธีการศุลกากรในตัว — เก็บ HS/HTS code เป็น custom field ได้ แต่ไม่มี classification workflow, denied-party screening, customs filing แบบ native. NetSuite: 0 · Oracle Fusion: 4 · SAP S/4HANA: 5 (SAP GTS เป็นมาตรฐานองค์กรข้ามชาติ). Gap Severity = High.

**Counter / Mitigation:**
ข้ออ้างถูก และตัวข้อความเองยอมรับว่า SAP GTS เป็น "มาตรฐานองค์กรข้ามชาติ" — GTM ปิดได้ด้วย certified SuiteApp เช่น Descartes Visual Compliance/DPS, eCustoms. สำหรับองค์กรในประเทศที่ไม่ได้ทำการค้า/ส่งออก-นำเข้าเชิงพาณิชย์ข้ามชาติเป็นแกนหลัก การนำเข้า reagent/เวชภัณฑ์ปริมาณจำกัดใช้ตัวแทน/ศุลกากรภายนอกได้ ไม่ต้องมี GTM engine ใน ERP — over-spec ชัดเจน.

**Procurement caveat:**
การใส่ GTM ใน TOR สำหรับองค์กรในประเทศ = over-spec ที่ชัดเจน — เสี่ยงถูกท้วงว่าเป็นเกณฑ์ล็อกสเปกไปทาง SAP/Oracle โดยไม่มี use case.

- **Confidence:** high
- **หลักฐาน / Citation:**
  - [KB] ไม่พบเอกสาร GTM ใน netsuite_kb (theme gtm top score เพียง 0.52 = Country Specific Features/Tax) → ยืนยันไม่มี GTM native
  - [WEB:netsuite.com] What Is Global Trade Management (article อธิบายแนวคิด ไม่ใช่โมดูลใน NetSuite)
  - [WEB:suiteapp.com] Descartes Denied Party Screening (DPS) — GTM/screening เป็น SuiteApp 3rd-party

---

## GP-FUNC-09 — จัดหาเชิงกลยุทธ์ / e-Sourcing / ประมูล / Strategic sourcing / e-Sourcing / RFx & auctions

- **Capability (TH):** จัดหาเชิงกลยุทธ์ / e-Sourcing / ประมูล
- **Capability (EN):** Strategic sourcing / e-Sourcing / RFx & auctions
- **Domain:** Procurement
- **iCE severity:** ต่ำ (low)

**จุดที่ NetSuite สู้ไม่ได้ (Gap):**
ร่างระบุ "NetSuite จัดซื้อพื้นฐาน; SAP Ariba & Oracle Sourcing Cloud ครบกว่ามาก" และให้ 1★. NetSuite ไม่มี e-auction (ประมูลออนไลน์ย้อนกลับ) และไม่มีเครือข่ายจัดหาแบบ SAP Ariba Network/Oracle Sourcing Cloud. Gap Severity = High.

**Counter / Mitigation:**
เรตติ้ง 1★ ต่ำเกินไป — NetSuite จัดซื้อมากกว่า "พื้นฐาน": RFQ native + Purchase Contracts/Blanket Orders (auto จาก RFQ) + vendor performance (on-time delivery native, scorecard ผ่าน KPI Scorecard/custom KPI, predictive ผ่าน Supply Chain Control Tower เสริม). ขาดเฉพาะ **e-auction และเครือข่ายจัดหาระดับองค์กรข้ามชาติ (Ariba/Oracle Sourcing)** ซึ่งองค์กรการกุศลขนาดนี้ไม่จำเป็น. งานจัดซื้อจริง (ขอใบเสนอราคา/ทำสัญญาซื้อ) รองรับครบในตัว.

**Procurement caveat:**
การให้ 1★ พร้อมป้าย "จัดซื้อพื้นฐาน" ลดทอนความสามารถ native เกินจริง — เสี่ยงถูกท้วงว่าเกณฑ์ e-Sourcing network/e-auction ถูกใส่เพื่อกีดกัน. ควรระบุ outcome (RFx + เปรียบเทียบ + สัญญาซื้อ + เชื่อม e-GP ตามระเบียบพัสดุไทย).

- **Confidence:** high
- **หลักฐาน / Citation:**
  - [KB] Netsuite-Purchasing and Receiving (0.66–0.67) — RFQ / Award / Purchase Contracts & Blanket Orders
  - [WEB:docs.oracle.com] NetSuite Applications Suite — Analyzing and Awarding a Request for Quote (auto Purchase Contract; ไม่มี e-auction)
  - [ต้อง verify][WEB:erpresearch.com] ความเห็นว่า Oracle ERP Cloud เหนือกว่าด้าน procurement แต่ NetSuite ครอบ mid-market — เป็นแหล่งความเห็น/บล็อก ยังไม่ยืนยันแน่ชัด

---

## GP-FUNC-10 — บริหารวงจรชีวิต & ผลงานซัพพลายเออร์ / Supplier lifecycle & performance management (SLM)

- **Capability (TH):** บริหารวงจรชีวิต & ผลงานซัพพลายเออร์
- **Capability (EN):** Supplier lifecycle & performance management (SLM)
- **Domain:** Procurement
- **iCE severity:** กลาง (medium)

**จุดที่ NetSuite สู้ไม่ได้ (Gap):**
ร่างระบุ "NetSuite vendor record เบื้องต้น; ไม่มี scorecard/qualification workflow ลึก" และให้ 1★. Gap Severity = High.

**Counter / Mitigation:**
ข้ออ้าง "ไม่มี scorecard เลย" คลาดเคลื่อน — NetSuite มี On-Time Delivery Performance เป็น native portlet และ predictive vendor scores ผ่าน Supply Chain Control Tower (โมดูลเสริม) บวก KPI Scorecard ที่สร้างจาก custom KPI/saved search. แต่ **ไม่ใช่ scorecard 4 KPI สำเร็จรูป native** (quality rejection ต้องใช้โมดูล Quality Management) และ supplier qualification/SLM lifecycle เชิงลึกยังต้องใช้ certified SuiteApp/custom (เช่น Gatekeeper). สำหรับงานที่ต้องคัดกรอง+ประเมินคุณภาพซัพพลายเออร์อย่างเป็นระบบ (สาย GMP/light-pharma) จุดนี้เกี่ยวข้องสูงและ NetSuite อ่อนจริง — ปิด gap ด้วย SuiteApp/custom ต้นทุนบริหารจัดการได้.

**Procurement caveat:**
การให้ 1★ พร้อมระบุ "ไม่มี scorecard/qualification" มีข้อมูลผิดบางส่วน (vendor performance มี native/คอนฟิกได้) — เกณฑ์ควรระบุผลลัพธ์ (มีการประเมินผลงาน + คัดกรอง + audit trail) และเปิดให้ปิดด้วย SuiteApp certified ไม่ผูกกับ Oracle SLM โดยตรง.

- **Confidence:** high
- **หลักฐาน / Citation:**
  - [KB] Netsuite-Purchasing and Receiving (0.53) — On-Time Delivery Performance / Vendor Return Amount (native portlet)
  - [KB] Netsuite-Vendors (0.53) — vendor records (พื้นฐาน, ไม่มี qualification workflow)
  - [WEB:docs.oracle.com] NetSuite Applications Suite — Vendor Delivery Performance Scores (ผ่าน Supply Chain Control Tower)
  - [WEB:docs.oracle.com] NetSuite Applications Suite — Creating a KPI Scorecard / Using a Custom KPI (vendor scorecard = custom KPI/saved search)
  - [WEB:suiteapp.com] Gatekeeper — balanced scorecard/qualification เป็น SuiteApp

---

## GP-FUNC-11 — บริหารสัญญา (CLM) / Contract Lifecycle Management (CLM)

- **Capability (TH):** บริหารสัญญา (CLM)
- **Capability (EN):** Contract Lifecycle Management (CLM)
- **Domain:** Procurement
- **iCE severity:** สูง (high)

**จุดที่ NetSuite สู้ไม่ได้ (Gap):**
NetSuite **ไม่มีโมดูล CLM ในตัวเลย** — "Managing Contracts" native เป็นสัญญาฝั่งขาย/ต่ออายุเท่านั้น (Software Vertical Contract Renewals) ไม่มี clause library (คลังข้อสัญญา), authoring, redline หรือ obligation management; ฝั่งจัดซื้อมีเพียง Purchase Contract + เก็บไฟล์ใน File Cabinet. NetSuite: 1★ · Oracle Fusion: 4 · SAP S/4HANA: 4. Gap Severity = Med.

**Counter / Mitigation:**
CLM เต็มรูปต้องพึ่ง certified SuiteApp พาร์ทเนอร์ทั้งหมด (เช่น Gatekeeper, Azdan, Conga/Malbek). แต่ความต้องการจริงของลูกค้ากลุ่มนี้ — คลังสัญญา + แจ้งเตือนต่ออายุ + audit trail — ทำได้ด้วย native + SuiteApp ราคาประหยัด ไม่ใช่ blocker. CLM ระดับ enterprise (AI redline/clause library เต็มรูป) ถือว่า over-spec — gap severity "Med" จึงสมเหตุผล. **นี่คือ 1 ใน 3-4 ข้อของ vertical นี้ที่ "ควรพิจารณาจริง"** ไม่ใช่ over-spec ทั้งหมด.

**Procurement caveat:**
งานจัดซื้อ/สัญญาทุนสนับสนุนของหน่วยงานภาครัฐ/กึ่งราชการอยู่ใต้การตรวจ สตง. — ต้องมีคลังสัญญา + แจ้งเตือนต่ออายุ + audit trail พร้อมใช้ตั้งแต่ go-live. ต้องวางแผน/จัดงบเปิดใช้ SuiteApp ล่วงหน้า (ถือเป็นความเสี่ยง implementation ที่บริหารได้ ไม่ใช่การล็อกสเปก — แต่ควรเขียน TOR แบบ outcome-based ไม่ระบุยี่ห้อ CLM).

- **Confidence:** high
- **หลักฐาน / Citation:**
  - [KB] Netsuite-Software Vertical Contract Renewals (0.66) + Netsuite-Sales Orders and Cash Sales (0.63) — เป็น contract ฝั่งขาย/ต่ออายุเท่านั้น
  - [WEB:docs.oracle.com] NetSuite Applications Suite — Managing Contracts (จำกัดที่ sales renewal lifecycle; ไม่มี clause library/authoring/obligation)
  - [WEB:suiteapp.com] Gatekeeper Contract Management & Vendor Portal — CLM สำหรับ NetSuite เป็น SuiteApp พาร์ทเนอร์ (ยืนยันมีจริง)

---

## GP-FUNC-24 — CPQ / กำหนดราคาซับซ้อน / Configure-Price-Quote (CPQ) & complex pricing

- **Capability (TH):** CPQ / กำหนดราคาซับซ้อน
- **Capability (EN):** Configure-Price-Quote (CPQ) & complex pricing
- **Domain:** Order Mgmt
- **iCE severity:** แทบไม่มีผล (negligible)

**จุดที่ NetSuite สู้ไม่ได้ (Gap):**
ร่างระบุ "NetSuite CPQ จำกัด; Oracle CPQ & SAP มี configurator แข็งกว่า" และให้ 2★. NetSuite: 2 · Oracle Fusion: 4 · SAP S/4HANA: 4. Gap Severity = Med.

**Counter / Mitigation:**
NetSuite CPQ เป็นผลิตภัณฑ์ native (ซื้อแยก จากการเข้าซื้อ Verenia) — มี Configurator, Guided Selling, Proposal Generator, Manufacturing Integration เหมาะกับสินค้าที่ต้อง config/มี pricing rules; อ่อนกว่า Oracle CPQ/SAP เฉพาะการกำหนดค่าที่ซับซ้อนระดับสูงมากเท่านั้น. CPQ คือเครื่องมือเสนอราคาสินค้า config ได้เชิงพาณิชย์ — องค์กรที่ไม่มีการขายสินค้าตั้งค่าซับซ้อน/quoting เชิงพาณิชย์แทบไม่มี use case.

**Procurement caveat:**
การบรรจุ CPQ ใน TOR = over-spec/ล็อกสเปกโดยไม่กระทบงานจริง — เสี่ยงถูกท้วงติงว่าเป็นเกณฑ์ที่ไม่มี use case.

- **Confidence:** high
- **หลักฐาน / Citation:**
  - [KB] Netsuite-SuiteCommerce Store Front (0.56) — พบเฉพาะ quote/pricing ไม่มี configurator engine
  - [WEB:netsuite.com] NetSuite CPQ product page
  - [WEB:docs.oracle.com] NetSuite CPQ Overview

---

## GP-TECH-10 — จำนวนภาษา/ประเทศ/statutory ที่รองรับ / Languages, country & statutory coverage

- **Capability (TH):** จำนวนภาษา/ประเทศ/statutory ที่รองรับ
- **Capability (EN):** Languages, country & statutory coverage
- **Domain:** Technical / Localization
- **iCE severity:** แทบไม่มีผล (negligible)

**จุดที่ NetSuite สู้ไม่ได้ (Gap):**
SAP ครอบคลุมประเทศมากสุด; NetSuite รองรับน้อยกว่าทั้ง SAP และ Oracle — "สำคัญมากสำหรับองค์กรข้ามชาติ". NetSuite: 2 · Oracle Fusion: 4 · SAP S/4HANA: 5. Gap Severity = High.

**Counter / Mitigation:**
NetSuite รองรับจำนวนประเทศน้อยกว่า SAP จริง แต่ **localization ไทยครบ** ผ่าน Southeast Asia Localization SuiteApp + SuiteTax — ภาษาไทย, VAT (ภ.พ.30), ใบกำกับภาษี/Branch ID และภาษีหัก ณ ที่จ่าย (รายงาน ภ.ง.ด.). ความกว้าง statutory หลายประเทศไม่เกี่ยวกับองค์กรที่ดำเนินงานในไทยประเทศเดียว (payroll ไทยอย่างเดียว) — ตัวข้อความยังระบุเองว่า "สำคัญสำหรับองค์กรข้ามชาติ".

**Procurement caveat:**
เป็น over-spec ที่ชัดเจนสำหรับองค์กร single-country — การนับจำนวนประเทศเป็นเกณฑ์คัดเลือกเสี่ยงถูกท้วงว่ากีดกัน. ควรระบุ statutory ไทยที่ต้องรองรับ ไม่ใช่จำนวนประเทศทั้งหมด.

- **Confidence:** high
- **หลักฐาน / Citation:**
  - [KB] Netsuite-Country Specific Features — Thailand Tax Codes/VAT ภ.พ.30 (0.619)
  - [KB] Netsuite-Country Specific Features — Southeast Asia Localization SuiteApp/Thailand Invoicing (0.606)

---

## GP-STANDOUT-07 — Fusion standout: Procurement Cloud ครบวงจร / End-to-end Procurement Cloud

- **Capability (TH):** จุดเด่น Fusion — Procurement Cloud ครบวงจร
- **Capability (EN):** Fusion standout: End-to-end Procurement Cloud
- **Domain:** Procurement
- **iCE severity:** ต่ำ (low)

**จุดที่ NetSuite สู้ไม่ได้ (Gap):**
Oracle Fusion วาง Procure-to-Pay + Sourcing + Supplier Mgmt ไว้ในชุดเดียวโดยตรง ไม่ต้องผูก network แยกแบบ Ariba. ร่างระบุ NetSuite ให้งานจัดซื้อระดับพื้นฐาน (P2P) ขาดความครบของ strategic sourcing/e-auction และ supplier management เชิงลึกที่ Oracle Fusion มีในตัว และต้องต่อ e-GP (จัดซื้อจัดจ้างภาครัฐ) ตามระเบียบพัสดุไทยผ่าน integration เอง. Rank 7 ใน Fusion Standout list.

**Counter / Mitigation:**
งานจัดซื้อสาธารณกุศล/กึ่งราชการเน้น **procure-to-pay + เส้นทางอนุมัติ + เชื่อม e-GP** ตามระเบียบพัสดุไทย ซึ่ง NetSuite Procurement + integration ทำได้. ส่วน strategic sourcing/e-auction เต็มรูปเป็น nice-to-have ไม่ใช่ตัวตัดสิน. (ดู F-PRC-01/GP-FUNC-09 — RFQ + auto Purchase Contract เป็น native; ที่ขาดคือ e-auction/network เท่านั้น).

**Procurement caveat:**
การยก "Procurement Cloud ครบวงจรในตัว" เป็นเกณฑ์ตัดสินเสี่ยงล็อกสเปกไปทาง Fusion — ควรเน้นผลลัพธ์ P2P + เชื่อม e-GP ตามระเบียบพัสดุไทย ซึ่งเป็นความต้องการจริงของงานจัดซื้อภาครัฐ/กึ่งราชการ.

- **Confidence:** medium
- **หลักฐาน / Citation:**
  - (ตาม record GP-STANDOUT-07) Oracle Fusion Procure-to-Pay + Sourcing + Supplier Mgmt ในชุดเดียว vs NetSuite P2P + integration e-GP; รายละเอียด RFQ/Purchase Contract native อ้างอิงหลักฐานใน F-PRC-01 / GP-FUNC-09. ไม่มี KB/web citation เฉพาะข้อ standout นี้ในแหล่งตั้งต้น.

---

## TOR-PRC-01 — TOR: การจัดหาเชิงกลยุทธ์ (RFx / e-Auction / scorecard / supplier lifecycle) / Strategic sourcing

- **Capability (TH):** TOR — จัดหาเชิงกลยุทธ์ (RFx, e-auction, supplier scorecard, supplier lifecycle)
- **Capability (EN):** TOR: Strategic sourcing (RFx / e-auction / scorecard / supplier lifecycle)
- **Domain:** Procurement / Sourcing
- **iCE severity:** ต่ำ (low)

**จุดที่ NetSuite สู้ไม่ได้ (Gap):**
ร่าง TOR: "ระบบต้องมีการจัดหาเชิงกลยุทธ์ (strategic sourcing) รองรับ RFx, การประมูลออนไลน์ (e-auction), การประเมินซัพพลายเออร์ (scorecard) และการบริหารวงจรชีวิตซัพพลายเออร์ในตัว." NetSuite ตอบได้ = Partial. Differentiator note: "NetSuite จัดซื้อพื้นฐาน; Oracle Sourcing Cloud อยู่ในชุดเดียว ✔✔ / SAP ใช้ Ariba network แยก."

**Counter / Mitigation:**
TOR รวม RFx + e-auction + supplier scorecard + supplier lifecycle ไว้ในข้อเดียว; NetSuite ทำได้ **~3/4**:
- RFQ + auto Purchase Contract = native (แข็ง)
- vendor scorecard ผ่าน on-time delivery native + KPI Scorecard/custom KPI + Control Tower เสริม (กลาง)
- vendor lifecycle/qualification บางส่วน (อ่อน — ปิดด้วย SuiteApp)
- ขาดเฉพาะ **e-auction**

จึง ns_can = 'Partial' ตรงข้อเท็จจริง แต่ฉลาก "จัดซื้อพื้นฐาน" ลดทอนเกินไป.

**Procurement caveat:**
การรวม 4 ความสามารถไว้ในข้อเดียวโดยมี e-auction เป็นเงื่อนไข "ในตัว" ทำให้ NetSuite ตอบได้แค่ Partial ทั้งที่ 3/4 เป็น native — เสี่ยงถูกท้วงว่าเกณฑ์ถูกออกแบบเพื่อกีดกัน. ควรแยกข้อ (RFx / scorecard / lifecycle เป็น outcome-based; e-auction เป็น optional/nice-to-have) และอนุญาตให้ปิดด้วย SuiteApp certified.

- **Confidence:** medium
- **หลักฐาน / Citation:**
  - (ตาม record TOR-PRC-01) NetSuite RFQ + auto Purchase Contract native; vendor scorecard = on-time delivery native + KPI Scorecard/custom KPI + Supply Chain Control Tower เสริม; vendor lifecycle/qualification บางส่วน; ขาด e-auction. รายละเอียดหลักฐาน RFQ/scorecard อ้างอิงตาม F-PRC-01, F-PRC-02, GP-FUNC-09, GP-FUNC-10. ไม่มี KB/web citation เฉพาะข้อ TOR spec นี้ในแหล่งตั้งต้น.

---

## สรุปเชิงกลยุทธ์สำหรับ vertical นี้ / Strategic wrap-up

จากทั้ง 14 records ของ **trading-services**: จุดที่ "ควรพิจารณาจริง" (ไม่ใช่ over-spec) มีเพียง **GP-FUNC-11 (CLM — สูง)** และ **F-PRC-02 / GP-FUNC-10 (supplier qualification/SLM — กลาง)** โดยเฉพาะเมื่อองค์กรมีสายงานที่อยู่ใต้การตรวจสอบ (สตง.) หรือมีการคัดกรองซัพพลายเออร์เชิงคุณภาพ (GMP/light-pharma). ทั้งสามข้อปิดได้ด้วย certified SuiteApp (Gatekeeper ฯลฯ) + native ต้นทุนบริหารจัดการได้.

ส่วนที่เหลือ (S&OP/IBP, TMS ×2, Global Trade, CPQ, statutory หลายประเทศ) เป็น **over-spec** สำหรับองค์กรที่ดำเนินงานในประเทศเป็นหลัก และงานจัดหา (F-PRC-01 / GP-FUNC-09 / TOR-PRC-01) NetSuite ทำได้ ~3/4 ในตัว (RFQ + auto Purchase Contract native) — ขาดเฉพาะ live e-auction. เมื่อขาย/ป้องกัน NetSuite ให้เน้น: (1) RFQ + Purchase Contract เป็น native จริง คะแนน 0/1★ ในร่าง TOR คลาดเคลื่อน, (2) ความสามารถข้ามชาติ/เชิงพาณิชย์เต็มรูปไม่มี use case, และ (3) การล็อกสเปกกับผลิตภัณฑ์เดียวมีความเสี่ยงเชิงจัดซื้อ — ควรเขียน requirement แบบ outcome-based ตามภารกิจจริง.

---

*KB generated from TOR Requirement Bank + Gap Pack v2 · balanced per iCE second-opinion methodology (2026-06-29) · client identifiers generalized to healthcare / blood-bank / non-profit / public-sector patterns · AMS: re-verify yearly.*
