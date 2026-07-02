# TOR Competitive KB — trading-services — Oracle Fusion Standout & TOR Weaponization

---
last_verified: "2026-06-29"
source: "TOR Requirement Bank + Gap Pack v2"
confidence_note: "Confidence per record reflects whether an official Oracle/NetSuite KB or web citation backs the position. 'high' = KB + official docs corroborated; 'medium' = KB partial or [ต้อง verify] flag present. All records preserve the iCE balanced second-opinion (NetSuite counter-view) verbatim so the same file can be used defensively when the competitor argues coverage-by-add-on. Client identity generalized to healthcare / blood-bank / non-profit / public-sector patterns per anti-disclosure rule."
ams_review: "yearly — re-verify product positions"
angle: "fusion — STANDOUT + WEAPONIZE (used when iCE SELLS Oracle Fusion)"
industry_vertical: "trading-services"
record_count: 13
severity_distribution: "สูง 1 · กลาง 2 · ต่ำ 4 · แทบไม่มีผล 6"
---

## บทนำ / How to use this file (trading-services angle)

เอกสารนี้คือคลังความรู้เชิงแข่งขันสำหรับสถานการณ์ที่ iCE **ขาย Oracle Fusion** ให้กลุ่มงาน trading & services — โดยเฉพาะสายจัดซื้อจัดหา (procurement/sourcing/contract), การกระจาย-โลจิสติกส์, และการเสนอราคาเชิงพาณิชย์ (order management/CPQ). แต่ละหัวข้อระบุ (1) จุดที่ Oracle Fusion เหนือกว่า NetSuite จริง (Standout), (2) ถ้อยคำ TOR ที่แนะนำให้สเปกเพื่อให้คู่แข่งที่ยื่นด้วย NetSuite ตอบได้เพียง Partial/No, และ (3) คำเตือนของ iCE เพื่อเลี่ยงการเขียนสเปกล็อกผลิตภัณฑ์ (over-spec / procurement-fairness risk) ที่อาจถูกท้วงจากผู้ตรวจสอบหรือผู้ยื่นรายอื่น.

This is a competitive knowledge base for engagements where iCE **sells Oracle Fusion** into trading & services accounts. Each section is deliberately two-sided: it hands the seller the Fusion advantage and the exact spec wording to press, **and** it keeps the iCE counter-view so the team never over-claims and can spot a defensible NetSuite rebuttal in advance. The underlying raw pack was drafted as a competitive TOR biased toward Fusion — treat every "must be native / without any add-on" clause as a potential over-spec flag, not a truth about requirements.

> **iCE governing caveat (จาก second_opinion.txt):** ชุด TOR ต้นฉบับถูกออกแบบให้ NetSuite ตอบได้แค่ Partial/No และ Oracle Fusion ตอบ Fully — จึงไม่ใช่การวิเคราะห์ความต้องการที่เป็นกลาง. ข้อกล่าวอ้างจำนวนมากมองข้าม first-party add-on ของ NetSuite (NSPB, NetSuite Account Reconciliation, NSAW) ที่ใช้เอนจิน Oracle เดียวกัน และหลาย gap เป็น over-spec สำหรับองค์กรที่ดำเนินงานในไทยประเทศเดียว. เพื่อความเป็นธรรมและลดความเสี่ยงถูกท้วงติง (สตง./ผู้ยื่นรายอื่น) ควรเขียน requirement แบบ **outcome-based** ตามภารกิจจริง ไม่ผูกกับฟีเจอร์เฉพาะผลิตภัณฑ์ใดผลิตภัณฑ์หนึ่ง.

---

## GP-FUNC-11 — Contract Lifecycle Management (CLM) / การบริหารสัญญาตลอดวงจรชีวิต

- **Capability (TH):** บริหารสัญญา (CLM)
- **Capability (EN):** Contract Lifecycle Management (CLM)
- **Domain:** Procurement · **iCE severity:** สูง (High)
- **Scoring in raw pack:** NetSuite 1★ · Oracle Fusion 4★★★★ · SAP S/4HANA 4★★★★ · Gap Severity: Med

**Oracle Fusion advantage (Standout):**
Oracle Fusion Procurement มีโมดูล Contract Lifecycle Management ในชุดเดียว: clause library (คลังข้อสัญญา), authoring/redline, obligation management และ audit trail ครบวงจร. NetSuite ไม่มีโมดูล CLM เฉพาะในตัวเลย — native "Managing Contracts" จำกัดที่สัญญาฝั่งขาย/ต่ออายุ (sales renewal lifecycle) และฝั่งจัดซื้อมีเพียง Purchase Contract + เก็บไฟล์ใน File Cabinet. CLM เต็มรูปบน NetSuite ต้องพึ่ง SuiteApp พาร์ทเนอร์ (Gatekeeper, Conga/Malbek) ทั้งหมด. ในงานจัดซื้อ/สัญญาที่อยู่ภายใต้การตรวจสอบ (เช่นภาครัฐ/กึ่งราชการ/สาธารณกุศล) ความสามารถ clause library + obligation + audit trail ในแพลตฟอร์มเดียวเป็นข้อได้เปรียบเชิงกำกับที่ชัดเจนของ Fusion.

**TOR wording to weaponize (ภาษาไทย):**
"ระบบต้องมีการบริหารสัญญาตลอดวงจรชีวิต (Contract Lifecycle Management) ในตัวบนแพลตฟอร์มเดียวกับระบบจัดซื้อ ครอบคลุมคลังข้อสัญญา (clause library), การร่างและปรับแก้ (authoring/redline), การติดตามภาระผูกพัน (obligation management), การแจ้งเตือนต่ออายุ และร่องรอยการตรวจสอบ (audit trail) โดยไม่ต้องพึ่ง add-on ภายนอก"

**TOR wording (English):**
"The solution must provide native Contract Lifecycle Management (CLM) on the same platform as procurement, covering a clause library, contract authoring/redline, obligation management, renewal alerts and full audit trail, without reliance on an external add-on."

**iCE caveat:**
ความต้องการจริงของหน่วยงานสาธารณกุศล/กึ่งราชการ (คลังสัญญา + แจ้งเตือนต่ออายุ + audit trail) สามารถทำได้ด้วย NetSuite native + SuiteApp ราคาประหยัด และไม่ใช่ blocker — จุดอ่อนที่แท้จริงคือ "ต้องซื้อ SuiteApp เพิ่ม" ไม่ใช่ "ทำไม่ได้". การบังคับ CLM ระดับ enterprise แบบ AI redline / clause library เต็มรูป "ในตัวโดยไม่พึ่ง add-on" เป็น over-spec (gap_severity ต้นฉบับให้ระดับ Med เท่านั้น). ถ้าคู่แข่งวางแผนงบ SuiteApp (เช่น Gatekeeper) มาตั้งแต่ต้น เขาปิด requirement นี้ได้ในต้นทุนที่บริหารจัดการได้ — จึงควรระวังการเขียนสเปกที่ดูล็อกผลิตภัณฑ์เกินจำเป็นและอาจถูกท้วง.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-Software Vertical Contract Renewals (0.66) + Netsuite-Sales Orders and Cash Sales (0.63) — เป็น contract ฝั่งขาย/ต่ออายุเท่านั้น
- [WEB:docs.oracle.com] NetSuite Applications Suite — Managing Contracts (จำกัดที่ sales renewal lifecycle; ไม่มี clause library/authoring/obligation)
- [WEB:suiteapp.com] Gatekeeper Contract Management & Vendor Portal — CLM สำหรับ NetSuite เป็น SuiteApp พาร์ทเนอร์ (ยืนยันมีจริง)

---

## F-PRC-02 — Supplier Qualification / SRM Portal / พอร์ทัลบริหารผู้ขาย

- **Capability (TH):** Supplier Qualification / SRM Portal
- **Capability (EN):** Supplier management portal
- **Domain:** Procurement · **iCE severity:** กลาง (Medium)
- **Scoring in raw pack:** NetSuite 1 (ต้อง add-on/custom) · Priority: กลาง

**Oracle Fusion advantage (Standout):**
Oracle Fusion มี Supplier Portal + Supplier Qualification Management ครบวงจร: การคัดกรอง (qualification) ด้วยแบบสอบถาม, การขึ้นทะเบียนผู้ขาย (onboarding) และการประเมินผลงาน (performance) ในตัวบนแพลตฟอร์มเดียว. NetSuite vendor portal พื้นฐานกว่า — ส่วนที่อ่อนจริงคือ qualification/onboarding เชิงแบบสอบถาม/ขึ้นทะเบียน ซึ่งต้องใช้ SuiteApp (เช่น Gatekeeper) หรือ custom; ส่วน vendor performance มี building block native (portlet On-Time Delivery/Vendor Return Amount) แต่ scorecard สำเร็จรูปต้องสร้างเองจาก custom KPI/saved search และ predictive score ผูกกับ Supply Chain Control Tower (โมดูลเสริมมีค่าใช้จ่าย). สำหรับสายจัดซื้อที่ต้องคัดกรองซัพพลายเออร์อย่างเป็นระบบ (โดยเฉพาะงานที่มีมาตรฐานคุณภาพ/GMP) กระบวนการ qualification ในตัวของ Fusion เป็นข้อได้เปรียบ.

**TOR wording to weaponize (ภาษาไทย):**
"ระบบต้องมีพอร์ทัลและกระบวนการบริหารผู้ขาย (supplier management) ครบวงจรในตัว: การคัดกรองคุณสมบัติ (qualification) ด้วยแบบสอบถามที่กำหนดเงื่อนไขได้, การขึ้นทะเบียนผู้ขาย (onboarding) และการประเมินผลงาน (performance/scorecard) แบบมี KPI สำเร็จรูป — โดยไม่ต้องพึ่ง SuiteApp/add-on ภายนอก"

**TOR wording (English):**
"The solution must provide a complete, native supplier management portal and process: configurable supplier qualification questionnaires, supplier onboarding, and performance evaluation with out-of-the-box scorecard KPIs — without reliance on external SuiteApps/add-ons."

**iCE caveat:**
คำว่า "ไม่มี performance ครบ" เกินจริง — building block ของ vendor performance มี native/คอนฟิกได้ (On-Time Delivery portlet). ที่อ่อนจริงคือ qualification/onboarding เชิงแบบสอบถามซึ่งปิดได้ด้วย SuiteApp/custom ต้นทุนบริหารจัดการได้ ไม่ใช่จุดปัดตก. การบังคับ "scorecard KPI สำเร็จรูป native + qualification โดยไม่พึ่ง add-on" มีลักษณะเอียงเข้าหา Fusion — ควรเขียนแบบ outcome-based (ต้องคัดกรอง/ประเมินผู้ขายได้อย่างเป็นระบบ) มากกว่าระบุกลไกในตัวเฉพาะ.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-Purchasing and Receiving (0.53) — On-Time Delivery Performance / Vendor Return Amount portlet (native)
- [KB] Netsuite-Inventory Management / NSIMG (~0.49) — Supply Chain Control Tower: Vendor Predicted Days Late/Early (predictive, โมดูลเสริม)
- [WEB:docs.oracle.com] NetSuite Applications Suite — Vendor Delivery Performance Scores (ผ่าน Supply Chain Control Tower)
- [WEB:docs.oracle.com] NetSuite Applications Suite — Creating a KPI Scorecard / Using a Custom KPI in a KPI Scorecard (vendor scorecard สร้างจาก custom KPI/saved search)
- [WEB:suiteapp.com] Gatekeeper — vendor scorecard/qualification เป็น SuiteApp พาร์ทเนอร์

---

## GP-FUNC-10 — Supplier Lifecycle & Performance Management (SLM) / บริหารวงจรชีวิตและผลงานซัพพลายเออร์

- **Capability (TH):** บริหารวงจรชีวิต & ผลงานซัพพลายเออร์
- **Capability (EN):** Supplier lifecycle & performance management (SLM)
- **Domain:** Procurement · **iCE severity:** กลาง (Medium)
- **Scoring in raw pack:** NetSuite 1★ · Oracle Fusion 4★★★★ · SAP S/4HANA 5★★★★★ · Gap Severity: High

**Oracle Fusion advantage (Standout):**
Oracle Fusion Procurement มี supplier lifecycle management เต็มวงจร (registration → qualification → performance scorecard → offboarding) พร้อม scorecard KPI สำเร็จรูป. NetSuite มี On-Time Delivery Performance เป็น native portlet และ predictive vendor scores ผ่าน Supply Chain Control Tower (โมดูลเสริม) บวก KPI Scorecard ที่สร้างจาก custom KPI/saved search — แต่ไม่ใช่ scorecard 4-KPI สำเร็จรูป native (quality rejection ต้องใช้โมดูล Quality Management) และ supplier qualification/SLM lifecycle เชิงลึกยังต้องใช้ SuiteApp/custom (เช่น Gatekeeper). ในดีลที่ผู้ซื้อให้น้ำหนักการประเมิน-คัดกรองซัพพลายเออร์อย่างเป็นระบบ (คุณภาพ/ส่งมอบ/ความเสี่ยง) ความครบของ SLM ในตัว Fusion เป็นข้อได้เปรียบ.

**TOR wording to weaponize (ภาษาไทย):**
"ระบบต้องรองรับการบริหารวงจรชีวิตซัพพลายเออร์ (Supplier Lifecycle Management) ครบวงจรในตัว รวมถึง supplier scorecard ที่มี KPI สำเร็จรูปหลายด้าน (การส่งมอบตรงเวลา คุณภาพ/อัตราการปฏิเสธ ราคา และความเสี่ยง) โดยไม่ต้องสร้าง KPI เองหรือพึ่งโมดูล/แอปเสริมภายนอก"

**TOR wording (English):**
"The solution must support end-to-end native Supplier Lifecycle Management, including a supplier scorecard with out-of-the-box multi-dimension KPIs (on-time delivery, quality/rejection rate, price and risk), without requiring self-built KPIs or external add-on modules."

**iCE caveat:**
ข้ออ้าง "ไม่มี scorecard เลย" คลาดเคลื่อน — vendor performance มี native/คอนฟิกได้; ช่องว่าง qualification เชิงลึกปิดด้วย SuiteApp/custom ได้และไม่ critical ยกเว้นงานคุณภาพ/GMP ที่เกี่ยวข้องสูง. การกำหนด "scorecard KPI สำเร็จรูปหลายด้าน โดยไม่พึ่ง add-on" ตัด NetSuite ด้วยมาตรฐานที่แม้แต่ฟีเจอร์ native ก็ทำได้บางส่วนแล้ว — ควรระวัง over-spec และตั้งเกณฑ์ตามผลลัพธ์การบริหารซัพพลายเออร์ที่จำเป็นจริง.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-Purchasing and Receiving (0.53) — On-Time Delivery Performance / Vendor Return Amount (native portlet)
- [KB] Netsuite-Vendors (0.53) — vendor records (พื้นฐาน, ไม่มี qualification workflow)
- [WEB:docs.oracle.com] NetSuite Applications Suite — Vendor Delivery Performance Scores (ผ่าน Supply Chain Control Tower)
- [WEB:docs.oracle.com] NetSuite Applications Suite — Creating a KPI Scorecard / Using a Custom KPI (vendor scorecard = custom KPI/saved search)
- [WEB:suiteapp.com] Gatekeeper — balanced scorecard/qualification เป็น SuiteApp

---

## F-PRC-01 — Strategic Sourcing (RFx / e-Auction) / การจัดหาเชิงกลยุทธ์

- **Capability (TH):** Strategic Sourcing (RFx / e-Auction)
- **Capability (EN):** Strategic sourcing
- **Domain:** Procurement · **iCE severity:** ต่ำ (Low)
- **Scoring in raw pack:** NetSuite 0 (ทำไม่ได้เลย) · Priority: สูง

**Oracle Fusion advantage (Standout):**
Oracle Procurement Cloud (Sourcing) มีทั้ง RFx และ e-auction (การประมูลย้อนกลับสด/live reverse auction) ในตัว. NetSuite มี Request for Quote (RFQ) เป็น native (เปิด feature ก่อนใช้) — ตั้งช่วงเสนอราคา, ผู้ขายยื่นราคาหลาย tier/price break ผ่าน Vendor Center, มี Award column เปรียบเทียบและ auto-สร้าง Purchase Contract ต่อผู้ขายที่ได้รับรางวัล — แต่ **ไม่มี live reverse e-auction ในตัว**. จุด standout ที่ป้องกันได้จริงของ Fusion คือ e-auction แบบเรียลไทม์ ไม่ใช่ RFx (ซึ่ง NetSuite ทำได้ native).

**TOR wording to weaponize (ภาษาไทย):**
"ระบบต้องมีการจัดหาเชิงกลยุทธ์ (strategic sourcing) ในตัว ครอบคลุมทั้งการออกเอกสารสอบราคา (RFx) และการประมูลอิเล็กทรอนิกส์แบบย้อนกลับเรียลไทม์ (live reverse e-auction) บนแพลตฟอร์มเดียวกับระบบจัดซื้อ โดยไม่ต้องพึ่งระบบภายนอก"

**TOR wording (English):**
"The solution must provide native strategic sourcing covering both RFx and real-time reverse e-auctions on the same platform as procurement, without external systems."

**iCE caveat:**
การให้ NetSuite = 0 ("ทำไม่ได้เลย") ไม่ถูกต้อง — RFQ + auto Purchase Contract เป็นมาตรฐาน NetSuite อยู่แล้ว; ช่องว่างจริงแคบเหลือเพียง e-auction เรียลไทม์. สำหรับการจัดซื้อใช้เงินรัฐในไทยมักผ่านระบบ **e-GP กลางของกรมบัญชีกลาง** ไม่ใช่ e-auction ในตัว ERP — การบังคับ "e-auction ในตัวระบบ" จึงเป็น over-spec/ล็อกสเปกที่เสี่ยงถูกท้วง โดยเฉพาะหน่วยงานที่ต้องปฏิบัติตามระเบียบพัสดุ. [ต้อง verify ระเบียบพัสดุเฉพาะของหน่วยงาน]

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-Purchasing and Receiving (0.66) — Request for Quotes feature / Vendor RFQ / Awarding a Request for Quote / Purchase Contracts
- [WEB:docs.oracle.com] NetSuite Applications Suite — Analyzing and Awarding a Request for Quote (Award column; auto-creates Purchase Contract per awarded vendor; ไม่มี e-auction)
- [ต้อง verify] จัดซื้อใช้เงินรัฐในไทยมักผ่าน e-GP กลาง ไม่ใช่ e-auction ในตัว ERP; หน่วยงานมีระเบียบพัสดุของตนเอง

---

## GP-FUNC-09 — Strategic Sourcing / e-Sourcing / RFx & Auctions

- **Capability (TH):** จัดหาเชิงกลยุทธ์ / e-Sourcing / ประมูล
- **Capability (EN):** Strategic sourcing / e-Sourcing / RFx & auctions
- **Domain:** Procurement · **iCE severity:** ต่ำ (Low)
- **Scoring in raw pack:** NetSuite 1★ · Oracle Fusion 4★★★★ · SAP S/4HANA 5★★★★★ · Gap Severity: High

**Oracle Fusion advantage (Standout):**
Oracle Sourcing Cloud มีชุด e-Sourcing/RFx และ e-auction ครบ พร้อมเครือข่ายจัดหาระดับองค์กร. NetSuite จัดซื้อมากกว่า "พื้นฐาน" ตามที่ต้นฉบับกล่าว — RFQ native + Purchase Contracts/Blanket Orders (auto จาก RFQ) + vendor performance (on-time delivery native, scorecard ผ่าน KPI Scorecard/custom KPI, predictive ผ่าน Supply Chain Control Tower เสริม) — แต่ที่ขาดจริงคือ e-auction และเครือข่ายจัดหาแบบ SAP Ariba Network/Oracle Sourcing Cloud. Standout ที่ป้องกันได้ของ Fusion คือ sourcing network + e-auction ระดับองค์กรข้ามชาติ.

**TOR wording to weaponize (ภาษาไทย):**
"ระบบต้องมีชุดการจัดหาเชิงกลยุทธ์ (e-Sourcing) ครบวงจรในตัว รวมการประมูลออนไลน์ (e-auction) และการเชื่อมต่อเครือข่ายซัพพลายเออร์ (supplier network) โดยไม่ต้องพึ่งพาระบบเครือข่ายจัดหาภายนอกที่แยกจาก ERP"

**TOR wording (English):**
"The solution must provide a complete native strategic sourcing (e-Sourcing) suite including online e-auctions and a supplier network, without relying on an external sourcing network separate from the ERP."

**iCE caveat:**
เรตติ้ง 1★ ต่ำเกินไปสำหรับฟีเจอร์ที่ native/คอนฟิกได้; ส่วนที่เกินคือ e-auction และ sourcing network ระดับองค์กรข้ามชาติ ซึ่งองค์กรจัดซื้อขนาดกลาง/สาธารณกุศลในประเทศไม่จำเป็น. งานจัดซื้อจริง (ขอใบเสนอราคา/ทำสัญญาซื้อ) รองรับครบใน NetSuite native — การใส่ e-auction + supplier network "ในตัว" ลง TOR แบบ Mandatory มีลักษณะล็อกสเปก ควรตั้งเป็น nice-to-have หรือเขียนแบบ outcome-based.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-Purchasing and Receiving (0.66–0.67) — RFQ / Award / Purchase Contracts & Blanket Orders
- [WEB:docs.oracle.com] NetSuite Applications Suite — Analyzing and Awarding a Request for Quote (auto Purchase Contract; ไม่มี e-auction)
- [ต้อง verify][WEB:erpresearch.com] ความเห็นว่า Oracle ERP Cloud เหนือกว่าด้าน procurement แต่ NetSuite ครอบ mid-market — เป็นแหล่งความเห็น/บล็อก ยังไม่ยืนยันแน่ชัด

---

## GP-STANDOUT-07 — Fusion Standout: End-to-End Procurement Cloud

- **Capability (TH):** Procurement Cloud ครบวงจร
- **Capability (EN):** End-to-end Procurement Cloud
- **Domain:** Procurement · **iCE severity:** ต่ำ (Low)
- **Type:** Functional differentiator · **Rank in standout pack:** 7

**Oracle Fusion advantage (Standout):**
Fusion มี Procure-to-Pay + Sourcing + Supplier Management อยู่ในชุดเดียวกันโดยตรง ไม่ต้องผูก network แยกแบบ SAP Ariba. vs NetSuite: NetSuite ให้งานจัดซื้อระดับพื้นฐาน (P2P) และขาดความครบของ strategic sourcing/e-auction และ supplier management เชิงลึกที่ Oracle Fusion มีในตัว. จุดขายเชิงสถาปัตยกรรมคือ "ครบทั้งวงจรจัดซื้อบนแพลตฟอร์มเดียว" ซึ่งลดจุดเชื่อมและความซับซ้อนในการบริหารซัพพลายเออร์-สัญญา-การประมูลในที่เดียว.

**TOR wording to weaponize (ภาษาไทย):**
"ระบบต้องมีชุดจัดซื้อครบวงจร (end-to-end Procurement) บนแพลตฟอร์มเดียว ครอบคลุม Procure-to-Pay, Strategic Sourcing และ Supplier Management ในตัว โดยไม่ต้องเชื่อมต่อกับเครือข่ายจัดซื้อภายนอกที่แยกออกจากระบบ ERP"

**TOR wording (English):**
"The solution must provide an end-to-end Procurement suite on a single platform, covering Procure-to-Pay, Strategic Sourcing and Supplier Management natively, without integrating to an external procurement network separate from the ERP."

**iCE caveat:**
งานจัดซื้อสาธารณกุศล/กึ่งราชการเน้น **P2P + เส้นทางอนุมัติ + เชื่อม e-GP** ตามระเบียบพัสดุไทย ซึ่ง NetSuite Procurement + integration ทำได้; ส่วน strategic sourcing/e-auction เต็มรูปเป็น nice-to-have ไม่ใช่ตัวตัดสิน (iCE severity: ต่ำ). การเขียนสเปก "ครบวงจรบนแพลตฟอร์มเดียวโดยไม่เชื่อมภายนอก" อาจย้อนแย้งกับข้อเท็จจริงที่งานจัดซื้อภาครัฐไทยต้องเชื่อม e-GP กลางอยู่ดี — จึงควรระวังถ้อยคำที่ล็อกสเปกและตรวจสอบความสอดคล้องกับระเบียบพัสดุก่อน.

**Confidence:** medium

**หลักฐาน / Citation:**
- (Standout differentiator record — ไม่มี KB/official citation เฉพาะแนบมากับ record นี้; อ้างอิงข้ามกับ F-PRC-01/GP-FUNC-09 สำหรับหลักฐาน RFQ/Purchase Contract native ของ NetSuite และการเชื่อม e-GP ตามระเบียบพัสดุไทย)

---

## TOR-PRC-01 — TOR Spec: Strategic Sourcing (RFx / e-Auction / Supplier Scorecard / Lifecycle)

- **Capability (TH):** การจัดหาเชิงกลยุทธ์ (RFx / e-auction / scorecard / supplier lifecycle)
- **Capability (EN):** Strategic sourcing (RFx / e-auction)
- **Domain:** Procurement · **iCE severity:** ต่ำ (Low)
- **TOR classification:** Type Functional · Priority Important · NetSuite ตอบได้: Partial

**Oracle Fusion advantage (Standout):**
ข้อกำหนดรวม RFx + e-auction + supplier scorecard + supplier lifecycle ไว้ในข้อเดียว. Oracle Sourcing Cloud อยู่ในชุดเดียวและตอบได้ครบทั้ง 4 องค์ประกอบ. NetSuite ทำได้ ~3/4: RFQ + auto Purchase Contract เป็น native (แข็ง), vendor scorecard ผ่าน on-time delivery native + KPI Scorecard/custom KPI + Control Tower เสริม (กลาง), vendor lifecycle/qualification บางส่วน (อ่อน) — ขาดเฉพาะ e-auction. การมัดรวม 4 องค์ประกอบในข้อเดียวเป็นเทคนิคที่ทำให้ NetSuite ตกไปที่ Partial เพราะขาดชิ้นเดียว (e-auction) แม้ 3 ส่วนที่เหลือจะทำได้.

**TOR wording to weaponize (ภาษาไทย):**
"ระบบต้องมีการจัดหาเชิงกลยุทธ์ (strategic sourcing) ในตัว รองรับ RFx, การประมูลออนไลน์ (e-auction), การประเมินซัพพลายเออร์ (scorecard) และการบริหารวงจรชีวิตซัพพลายเออร์ ครบทั้งสี่องค์ประกอบบนแพลตฟอร์มเดียว"

**TOR wording (English):**
"The solution shall provide strategic sourcing with RFx, online e-auctions, supplier scorecards, and built-in supplier lifecycle management — all four components on a single platform."

**iCE caveat:**
NetSuite ตอบ Partial เป็นการประเมินที่ยุติธรรม แต่ฉลาก "จัดซื้อพื้นฐาน" ลดทอนความจริงว่า RFQ/Purchase Contract เป็น native และ vendor performance คอนฟิกได้. RFx + supplier scorecard เป็นงานจัดซื้อจริงที่ NetSuite รองรับ native/คอนฟิก; **e-auction ในตัวระบบเป็น over-spec** ที่หน่วยงานในประเทศแทบไม่มี use case จริง (มักผ่าน e-GP กลาง). การมัดรวม 4 องค์ประกอบเพื่อดัน Partial เป็นรูปแบบที่อาจถูกท้วงเรื่องความเป็นธรรม — พิจารณาแยกข้อกำหนดตามผลลัพธ์ที่จำเป็นจริง. [ต้อง verify]

**Confidence:** medium

**หลักฐาน / Citation:**
- [KB] Netsuite-Purchasing and Receiving (0.66) — RFQ/Award/Purchase Contracts
- [WEB:docs.oracle.com] NetSuite Applications Suite — Analyzing and Awarding a Request for Quote (RFx native, auto Purchase Contract, ไม่มี e-auction)
- [WEB:docs.oracle.com] NetSuite Applications Suite — Vendor Delivery Performance Scores (scorecard ผ่าน Supply Chain Control Tower + custom KPI)
- [ความเชื่อมั่น: กลาง — มี [ต้อง verify] flag บน use case e-auction ของหน่วยงาน]

---

## F-FIN-02 — Breadth of Statutory Localizations / ความกว้างของ localization หลายประเทศ

- **Capability (TH):** ความกว้างของ localization ตามกฎหมายหลายประเทศ
- **Capability (EN):** Breadth of statutory localizations
- **Domain:** Finance · **iCE severity:** แทบไม่มีผล (Negligible)
- **Scoring in raw pack:** NetSuite 2 (ได้บางส่วน) · Priority: กลาง

**Oracle Fusion advantage (Standout):**
Oracle Fusion มี global tax engine + ชุด localization ตามกฎหมาย (statutory) แบบ pre-certified ครอบคลุมหลายประเทศมากกว่า NetSuite. NetSuite มี SuiteTax engine + Country Localization/International Tax Reports กว่า 50 ประเทศ (รวมไทยผ่าน Southeast Asia Localization + International Tax Reports ซึ่งเป็น managed bundle ที่ NetSuite เผยแพร่เอง) แต่จำนวนประเทศที่ pre-certified ยังน้อยกว่า Fusion จริง. Standout ที่ป้องกันได้คือ "จำนวนประเทศ" สำหรับกลุ่มการค้า/บริการที่ดำเนินงานข้ามหลายประเทศ.

**TOR wording to weaponize (ภาษาไทย):**
"ระบบต้องมี global tax engine และชุด localization ตามกฎหมาย (statutory) แบบ pre-certified ครอบคลุมหลายประเทศ ผู้เสนอราคาต้องระบุจำนวนประเทศที่รองรับแบบ native"

**TOR wording (English):**
"The solution must provide a global tax engine and pre-certified statutory localizations across multiple countries; the bidder must state the number of natively supported countries."

**iCE caveat:**
การตั้งสเปกให้ผู้เสนอราคา "ระบุจำนวนประเทศที่รองรับ native" คือการล็อกสเปกที่ไม่สะท้อนความต้องการจริงหากหน่วยงานดำเนินงานในไทยประเทศเดียว — NetSuite รองรับไทยครบ (ใบกำกับภาษี/ภ.พ.30 ผ่าน Southeast Asia Localization). ส่วนที่ Oracle ชนะคือประเทศอื่นที่องค์กรไม่ได้ใช้ (iCE severity: แทบไม่มีผล). ใช้ข้อนี้เฉพาะเมื่อผู้ซื้อมีธุรกรรม trading ข้ามหลายประเทศจริงเท่านั้น มิฉะนั้นเป็น over-spec.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-Country Specific Features (0.7295)
- [WEB:docs.oracle.com] List of Country-Specific/SuiteTax Localization Features
- [WEB:suitecertified.com] NetSuite Country Localizations 50+ (secondary — corroborated)

---

## F-WMS-02 — Transportation Management (TMS) / การบริหารการขนส่ง

- **Capability (TH):** Transportation Management (TMS)
- **Capability (EN):** Transportation management
- **Domain:** SCM · **iCE severity:** แทบไม่มีผล (Negligible)
- **Scoring in raw pack:** NetSuite 0 (ทำไม่ได้เลย) · Priority: กลาง

**Oracle Fusion advantage (Standout):**
Oracle Transportation Management (OTM) เป็น full TMS: carrier rating, route optimization และ freight settlement. NetSuite ไม่มี TMS เต็มรูปในตัว — มีเพียง shipping integration (FedEx/UPS/USPS real-time rate + label) เป็น native; TMS เต็มรูปต้องเสริม SuiteApp (SuiteFleet/FreightPOP/Pacejet). Standout ที่ป้องกันได้ของ Fusion คือ carrier rating engine + route optimization + freight settlement ในตัว สำหรับผู้ส่งสินค้า/กระจายสินค้าเชิงพาณิชย์.

**TOR wording to weaponize (ภาษาไทย):**
"ระบบต้องมีการบริหารการขนส่ง (transportation management) ในตัว: การคิดค่าขนส่ง (carrier rating), การจัดเส้นทาง (route optimization) และการบริหารค่าระวาง (freight settlement) โดยไม่ต้องพึ่ง SuiteApp/ระบบภายนอก"

**TOR wording (English):**
"The solution must provide native transportation management: carrier rating, route optimization and freight settlement, without reliance on external SuiteApps."

**iCE caveat:**
ข้ออ้าง "ไม่มี TMS native" ถูกต้อง แต่การให้คะแนน 0 ("ทำไม่ได้เลย") แรงเกินเพราะ shipping integration เป็น native และ SuiteApp เติม TMS ได้ครบ. TMS ระดับ Oracle OTM ออกแบบให้ผู้ส่งสินค้าข้ามชาติ — สำหรับงานกระจายในประเทศด้วยรถ/ผู้ส่งของตนเอง อาจได้ประโยชน์เล็กน้อยจาก last-mile route/dispatch (SuiteFleet) แต่ไม่ต้องใช้ TMS พาณิชย์ระดับ enterprise (over-spec, iCE severity: แทบไม่มีผล). ใช้เฉพาะดีล trading/distribution ที่มีการขนส่งเชิงพาณิชย์เป็นแกนจริง.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-Shipping Guide (0.59) — carrier label integration เท่านั้น ไม่มี TMS native (theme tms top score 0.59)
- [WEB:netsuite.com] What Is a Transportation Management System (article)
- [WEB:suitefleet.com] NetSuite Route Optimization / TMS SuiteApp (Azdan) — route optimization/dispatch เสริมภายนอกแบบ SuiteApp

---

## GP-FUNC-07 — Transportation Management (TMS) / Logistics

- **Capability (TH):** การขนส่ง (TMS) / โลจิสติกส์
- **Capability (EN):** Transportation Management (TMS)
- **Domain:** SCM · **iCE severity:** แทบไม่มีผล (Negligible)
- **Scoring in raw pack:** NetSuite 0 (–) · Oracle Fusion 4★★★★ · SAP S/4HANA 5★★★★★ · Gap Severity: High

**Oracle Fusion advantage (Standout):**
Fusion มี TMS native (OTM) สำหรับงานโลจิสติกส์เชิงพาณิชย์; NetSuite ไม่มี TMS native ต้องต่อ 3rd party/SuiteApp. จุด standout ป้องกันได้คือ carrier rating/route optimization/freight settlement ในตัว — เป็นความสามารถของบริษัทโลจิสติกส์/ผู้ส่งออกข้ามชาติ.

**TOR wording to weaponize (ภาษาไทย):**
"ระบบต้องมีโมดูลบริหารการขนส่งและโลจิสติกส์ (Transportation Management) ในตัว ครอบคลุมการคิดค่าขนส่ง การวางแผนเส้นทาง และการชำระค่าระวาง โดยไม่ต้องต่อระบบบุคคลที่สาม"

**TOR wording (English):**
"The solution must provide a native Transportation Management module covering carrier rating, route planning and freight settlement, without connecting to a third-party system."

**iCE caveat:**
ข้ออ้างถูกในเชิงเทคนิค แต่ TMS (carrier rating/route optimization/freight settlement) เป็นความสามารถของบริษัทโลจิสติกส์/ผู้ส่งออกข้ามชาติ. การบังคับใส่ใน TOR สำหรับองค์กรที่งานหลักไม่ใช่การบริหารขนส่งเชิงพาณิชย์ = over-spec/ล็อกสเปก (iCE severity: แทบไม่มีผล) — งานกระจายในประเทศใช้ shipping integration + last-mile dispatch SuiteApp ก็เพียงพอ. ใช้ข้อนี้เฉพาะกับ trading/logistics account ที่การขนส่งเป็น core process จริง.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-Shipping Guide (0.59) — theme tms มีแต่ shipping label integration ไม่มี TMS native
- [WEB:netsuite.com] NetSuite Logistics ERP / TMS article — TMS เป็น integration/partner ไม่ใช่โมดูล native
- [WEB:suitefleet.com] Top 20 Transportation Management Systems 2026 — ทั้งหมดเป็น SuiteApp/partner

---

## GP-FUNC-08 — Global Trade Management & Customs/Compliance / การค้าระหว่างประเทศ

- **Capability (TH):** การค้าระหว่างประเทศ / พิธีการศุลกากร
- **Capability (EN):** Global Trade Management & customs/compliance
- **Domain:** SCM · **iCE severity:** แทบไม่มีผล (Negligible)
- **Scoring in raw pack:** NetSuite 0 (–) · Oracle Fusion 4★★★★ · SAP S/4HANA 5★★★★★ · Gap Severity: High

**Oracle Fusion advantage (Standout):**
Fusion มี Global Trade Management capabilities สำหรับ classification, denied-party screening และ compliance; NetSuite ไม่มีโมดูล GTM/พิธีการศุลกากรในตัว — เก็บ HS/HTS code เป็น custom field ได้ แต่ไม่มี classification workflow, denied-party screening หรือ customs filing แบบ native (ต้องใช้ SuiteApp เช่น Descartes Visual Compliance/DPS, eCustoms). Standout ป้องกันได้คือ trade classification + screening + customs ในตัว สำหรับผู้ค้า/ส่งออก-นำเข้าเชิงพาณิชย์ข้ามชาติ.

**TOR wording to weaponize (ภาษาไทย):**
"ระบบต้องมีการบริหารการค้าระหว่างประเทศ (Global Trade Management) ในตัว ครอบคลุมการจัดประเภทพิกัดสินค้า (classification), การตรวจสอบรายชื่อต้องห้าม (denied-party screening) และการจัดทำเอกสารพิธีการศุลกากร โดยไม่ต้องพึ่ง SuiteApp/ระบบภายนอก"

**TOR wording (English):**
"The solution must provide native Global Trade Management covering commodity classification, denied-party screening and customs documentation, without reliance on external SuiteApps."

**iCE caveat:**
ข้ออ้างถูก และตัวข้อความยอมรับว่า SAP GTS เป็น "มาตรฐานองค์กรข้ามชาติ" — สำหรับองค์กรในประเทศที่ไม่ได้ทำการค้า/ส่งออก-นำเข้าเชิงพาณิชย์ข้ามชาติเป็นแกนหลัก การใส่ GTM ใน TOR = over-spec ชัดเจน (iCE severity: แทบไม่มีผล). การนำเข้าปริมาณจำกัดใช้ตัวแทน/ศุลกากรภายนอกได้ ไม่ต้องมี GTM engine ใน ERP. ใช้เฉพาะกับผู้ค้า/import-export ที่มีปริมาณธุรกรรมข้ามชาติสูงและต้องคุม trade compliance จริง.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] ไม่พบเอกสาร GTM ใน netsuite_kb (theme gtm top score เพียง 0.52 = Country Specific Features/Tax) → ยืนยันไม่มี GTM native
- [WEB:netsuite.com] What Is Global Trade Management (article อธิบายแนวคิด ไม่ใช่โมดูลใน NetSuite)
- [WEB:suiteapp.com] Descartes Denied Party Screening (DPS) — GTM/screening เป็น SuiteApp 3rd-party

---

## GP-FUNC-24 — Configure-Price-Quote (CPQ) & Complex Pricing / การเสนอราคาสินค้าที่ config ได้

- **Capability (TH):** CPQ / กำหนดราคาซับซ้อน
- **Capability (EN):** Configure-Price-Quote (CPQ) & complex pricing
- **Domain:** Order Management · **iCE severity:** แทบไม่มีผล (Negligible)
- **Scoring in raw pack:** NetSuite 2★★ · Oracle Fusion 4★★★★ · SAP S/4HANA 4★★★★ · Gap Severity: Med

**Oracle Fusion advantage (Standout):**
Oracle CPQ มี configurator ที่แข็งแรงสำหรับสินค้าที่กำหนดค่าซับซ้อนระดับสูงมากและ pricing rules ซับซ้อน. NetSuite CPQ เป็นผลิตภัณฑ์ native (ซื้อแยก จากการเข้าซื้อ Verenia) — มี Configurator, Guided Selling, Proposal Generator, Manufacturing Integration เหมาะกับสินค้าที่ต้อง config/มี pricing rules — อ่อนกว่า Oracle CPQ/SAP เฉพาะการกำหนดค่าที่ซับซ้อนระดับสูงมากเท่านั้น. Standout ป้องกันได้ของ Fusion อยู่ที่ความลึกของ configurator/rules engine สำหรับผู้ค้าที่ขายสินค้า configurable ซับซ้อน.

**TOR wording to weaponize (ภาษาไทย):**
"ระบบต้องมีความสามารถ Configure-Price-Quote (CPQ) ในตัว รองรับการกำหนดค่าสินค้าที่ซับซ้อนหลายชั้น (multi-level configuration), กฎการตั้งราคาขั้นสูง (advanced pricing rules) และ guided selling บนแพลตฟอร์มเดียวกับระบบขาย"

**TOR wording (English):**
"The solution must provide native Configure-Price-Quote (CPQ) supporting multi-level product configuration, advanced pricing rules and guided selling on the same platform as order management."

**iCE caveat:**
CPQ คือเครื่องมือเสนอราคาสินค้าที่ config ได้เชิงพาณิชย์. สำหรับหน่วยงานที่ไม่มีการขายสินค้าตั้งค่าซับซ้อน/quoting เชิงพาณิชย์ การบรรจุใน TOR = over-spec/ล็อกสเปกโดยไม่กระทบงานจริง (iCE severity: แทบไม่มีผล; NetSuite CPQ เองก็เป็น native product ที่ซื้อแยกได้). ใช้ข้อนี้เฉพาะ trading account ที่ขายสินค้า configurable ซับซ้อนจริงและ configurator depth เป็นเกณฑ์ตัดสินได้.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-SuiteCommerce Store Front (0.56) — พบเฉพาะ quote/pricing ไม่มี configurator engine
- [WEB:netsuite.com] NetSuite CPQ product page
- [WEB:docs.oracle.com] NetSuite CPQ Overview

---

## GP-TECH-10 — Languages, Country & Statutory Coverage / จำนวนภาษา-ประเทศ-statutory

- **Capability (TH):** จำนวนภาษา/ประเทศ/statutory ที่รองรับ
- **Capability (EN):** Languages, country & statutory coverage
- **Domain:** Technical (Localization) · **iCE severity:** แทบไม่มีผล (Negligible)
- **Scoring in raw pack:** NetSuite 2★★ · Oracle Fusion 4★★★★ · SAP S/4HANA 5★★★★★ · Gap Severity: High

**Oracle Fusion advantage (Standout):**
Fusion รองรับจำนวนภาษา/ประเทศ/statutory มากกว่า NetSuite — สำคัญมากสำหรับองค์กรข้ามชาติ. NetSuite รองรับจำนวนประเทศน้อยกว่าจริง แต่ localization ไทยครบผ่าน Southeast Asia Localization SuiteApp + SuiteTax (ภาษาไทย, VAT ภ.พ.30, ใบกำกับภาษี/Branch ID และภาษีหัก ณ ที่จ่าย รายงาน ภ.ง.ด.). Standout ป้องกันได้คือ "ความกว้าง multi-country statutory" สำหรับผู้ค้า/บริการที่ดำเนินงานหลายประเทศ.

**TOR wording to weaponize (ภาษาไทย):**
"ระบบต้องรองรับหลายภาษาและ statutory/localization ครอบคลุมทุกประเทศที่องค์กรดำเนินงานแบบ native ผู้เสนอราคาต้องระบุจำนวนภาษาและประเทศที่รองรับ statutory reporting ในตัว"

**TOR wording (English):**
"The solution must provide native multi-language and statutory/localization coverage for every country of operation; the bidder must state the number of languages and countries with built-in statutory reporting."

**iCE caveat:**
ความกว้าง statutory หลายประเทศไม่เกี่ยวกับองค์กรที่ดำเนินงานในไทยประเทศเดียว (payroll ไทยอย่างเดียว) — ตัวข้อความต้นฉบับยังระบุเองว่า "สำคัญสำหรับองค์กรข้ามชาติ". เป็น over-spec ที่ชัดเจน (iCE severity: แทบไม่มีผล) เพราะ localization ไทยครบถ้วนบน NetSuite. ใช้เฉพาะดีล trading/services ที่มีหลายนิติบุคคล/หลายประเทศจริง มิฉะนั้นเสี่ยงถูกท้วงเรื่องความเป็นธรรม.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-Country Specific Features — Thailand Tax Codes/VAT ภ.พ.30 (0.619)
- [KB] Netsuite-Country Specific Features — Southeast Asia Localization SuiteApp/Thailand Invoicing (0.606)

---

## สรุปเชิงกลยุทธ์ / Seller's summary (trading-services)

สำหรับ trading & services การ์ดที่ "ป้องกันได้จริง" และมีน้ำหนักสูงสุดคือกลุ่มจัดซื้อ-สัญญา: **CLM (GP-FUNC-11, สูง)** เป็นจุดเดียวที่ iCE ให้ severity สูง — NetSuite ไม่มีโมดูล CLM ในตัวเลย และงานภายใต้การตรวจสอบต้องการคลังสัญญา + audit trail พร้อมใช้. รองลงมาเป็นกลุ่มกลาง **Supplier Qualification/SRM (F-PRC-02)** และ **SLM (GP-FUNC-10)** ที่ qualification/onboarding ของ NetSuite อ่อนจริง.

การ์ดที่เหลือ (sourcing/e-auction, TMS, GTM, CPQ, multi-country localization) ส่วนใหญ่เป็น **ต่ำ/แทบไม่มีผล** — ใช้ได้เฉพาะเมื่อ account เป็นผู้ค้า/ผู้ส่งออก/โลจิสติกส์ข้ามชาติที่มี use case จริงเท่านั้น. สำหรับหน่วยงานที่ดำเนินงานในประเทศเป็นหลัก (สาธารณกุศล/กึ่งราชการ/บริการในประเทศ) การ์ดเหล่านี้มีความเสี่ยง over-spec สูงและอาจถูกท้วงเรื่องความเป็นธรรมในการจัดซื้อจัดจ้าง (สตง./ผู้ยื่นรายอื่น). แนวปฏิบัติที่ปลอดภัย: เขียน requirement แบบ **outcome-based** ตามภารกิจจริง แล้วใช้จุดแข็ง Fusion (procurement suite ครบวงจร + CLM + supplier lifecycle บนแพลตฟอร์มเดียว) เป็น value narrative แทนการล็อกสเปกที่ฟีเจอร์เฉพาะผลิตภัณฑ์.
