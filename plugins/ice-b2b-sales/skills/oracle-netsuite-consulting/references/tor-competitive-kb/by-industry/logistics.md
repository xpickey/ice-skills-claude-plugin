# TOR Competitive KB — logistics — NetSuite Weakness & Counter

---
last_verified: "2026-06-29"
source: "TOR Requirement Bank + Gap Pack v2"
confidence_note: "Records inherit the confidence tag from each source record ([ความเชื่อมั่น: สูง/กลาง]). All product positions are mid-2026 standard positioning; items marked [ต้อง verify] must be confirmed against a live environment/vendor before a bid commitment. Source data is a COMPETITIVE TOR draft deliberately biased so NetSuite scores Partial/No and Oracle Fusion scores Fully — this KB preserves both the gap AND the iCE counter-view for balanced use."
ams_review: "yearly — re-verify product positions"
---

> **วิธีใช้ / How to use.** ไฟล์นี้ใช้เมื่อ iCE **ขาย NetSuite** หรือ **ตั้งรับ (defend)** จาก TOR ที่เอียงไปทาง Oracle Fusion ในกลุ่มงานโลจิสติกส์ (คลังสินค้า/กระจายสินค้า/ขนส่ง/วางแผนอุปสงค์). แต่ละหัวข้อให้ทั้ง (1) จุดที่ NetSuite เสียเปรียบจริง และ (2) แนวตั้งรับ — ปิดด้วย first-party add-on, certified SuiteApp, custom หรือข้อโต้แย้ง "over-spec".
>
> **บริบทลูกค้า (generalized).** แหล่งข้อมูลอ้างองค์กรลักษณะ **healthcare / blood-bank / non-profit foundation / public-sector** (นิติบุคคลเดียวในไทย งานสาธารณกุศล มีคลังหลายแห่งประเภท cold-chain สำหรับโลหิต/เวชภัณฑ์/ชีววัตถุ) — ใช้ pattern นี้แทนชื่อลูกค้าเสมอ. โลจิสติกส์ของกลุ่มนี้เป็น **การกระจายในประเทศ ปริมาณต่ำ-กลาง คุมอุณหภูมิ/lot/expiry** ไม่ใช่ DC พาณิชย์ปริมาณสูงหรือขนส่งข้ามชาติ — จุดนี้คือแกนของข้อโต้แย้ง over-spec ส่วนใหญ่ในไฟล์นี้.
>
> **Procurement note (สตง.).** การเขียน requirement ให้ผูกกับฟีเจอร์เฉพาะผลิตภัณฑ์ (เช่น "ระบุจำนวนประเทศ native", "TMS/GTM/S&OP native ในตัว") เป็นการล็อกสเปกที่เสี่ยงถูกท้วงติงจากสำนักงานการตรวจเงินแผ่นดิน (สตง.) และผู้ยื่นรายอื่น — ควรเขียนแบบ **outcome-based** ตามภารกิจจริง.

---

## F-SCM-01 — Demand & Supply Planning + S&OP

**Capability (TH):** การวางแผนความต้องการ/อุปทาน และกระบวนการ S&OP
**Capability (EN):** Demand/supply planning & S&OP

**Domain + iCE severity:** SCM · **ต่ำ (Low)**

**จุดที่ NetSuite สู้ไม่ได้ (Gap):**
ตามข้อความ TOR ต้นทาง NetSuite Demand Planning ถูกจัดว่า "พื้นฐานมาก — ไม่มี statistical forecasting/S&OP ระดับองค์กร" และให้คะแนน NetSuite = 1 (ต้อง add-on/custom) ขณะที่ Oracle SCM Planning Cloud เป็น tier-1 planning platform. TOR แนะนำสเปกให้ต้องมี "แพลตฟอร์มวางแผนความต้องการและอุปทานพร้อม statistical forecasting และกระบวนการ S&OP ในตัว (native)".

**Counter / Mitigation:**
ข้ออ้าง "ไม่มี statistical forecasting" **ไม่จริง**. NetSuite มี Demand Planning, Supply Planning และ Distribution Resource Planning (DRP) เป็นฟีเจอร์ในตัว (เปิดใช้ภายใต้ Advanced Inventory) พร้อมพยากรณ์เชิงสถิติ 4 วิธี — Linear Regression, Moving Average, Seasonal Average และ Sales Forecast. คะแนน 1 ("ต้อง add-on/custom") จึงเหมารวมเกินไป เพราะงานวางแผนอุปสงค์/อุปทานพื้นฐาน NetSuite ทำได้ในตัว.

**Gap จริงที่เหลือ** คือ demand sensing/ML และ **S&OP (Sales & Operations Planning) ระดับองค์กร** แบบ Oracle SCP Cloud ซึ่ง NetSuite ไม่มีในตัว — แต่นั่นเป็นเพียงครึ่งเดียวของข้อกำหนด ไม่ใช่ทั้งหมด. สำหรับ pattern healthcare/blood-bank (ศูนย์บริการโลหิต/ผลิตเซรุ่ม) การพยากรณ์ความต้องการเลือด/เซรุ่มด้วย native demand planning เพียงพอตามสเกล (สินค้าอายุสั้นเช่นโลหิตอาจต้องปรับแต่งวิธีพยากรณ์/custom). **Over-spec rebuttal:** S&OP เต็มรูปเป็นกระบวนการ consensus ของผู้ผลิต/กระจายสินค้าเชิงพาณิชย์ขนาดใหญ่ — เกินความจำเป็นขององค์กรสาธารณกุศลนิติบุคคลเดียว.

**Procurement caveat:**
การบังคับ "S&OP native ในตัว" ลง TOR แบบ Mandatory คือการเอียงสเปกไปทาง Oracle/SAP — เสี่ยงข้อท้วงติง สตง. ควรเขียนเป็นผลลัพธ์ (พยากรณ์ความต้องการ + เติมเต็มสต็อกตามรอบ) แทนการระบุโมดูล S&OP.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-Inventory Management (0.69) — Demand Planning เป็นฟีเจอร์ในตัว + Distribution Resource Planning + projection methods
- [KB] NSIMG (0.66) — Demand Plans/Supply Plans, Seasonal Average method, Supply Allocation หลาย location
- [WEB:docs.oracle.com] NetSuite Applications Suite — Calculating Item Demand (4 วิธีพยากรณ์เชิงสถิติ native, /ns-online-help/section_N2290234.html)

---

## F-WMS-01 — Directed Warehouse Operations (WMS)

**Capability (TH):** การบริหารคลังสินค้าแบบสั่งการอัตโนมัติ (directed operations)
**Capability (EN):** Directed warehouse operations

**Domain + iCE severity:** SCM · **กลาง (Medium)**

**จุดที่ NetSuite สู้ไม่ได้ (Gap):**
TOR ระบุว่า NetSuite WMS เป็น "mid-tier — ไม่มี slotting/labor management/wave ขั้นสูง" ให้คะแนน NetSuite = 2 (ได้บางส่วน) ขณะที่ Oracle WMS Cloud เป็น tier-1 (directed put-away/picking, wave, labor management). สเปกที่แนะนำบังคับให้มี directed put-away/picking, wave management และ warehouse labor management.

**Counter / Mitigation:**
การระบุว่า "ไม่มี wave ขั้นสูง" **คลาดเคลื่อน**. NetSuite WMS เป็น **first-party SuiteApp ที่ NetSuite พัฒนาเอง** (ต้องซื้อ license แยก ไม่รวมใน ERP ฐาน) และมี directed put-away, wave release, zone/RF barcode, cycle count และ task/wave management พร้อม KPI พื้นฐานในตัวจริง (ยืนยันจาก netsuite.com). ฟีเจอร์หลักของ requirement (wave/zone/directed put-away/RF) จึงทำได้ในตัวของ WMS SuiteApp.

**ที่อ่อนกว่าจริง** คือ **slotting optimization** และ **labor management เชิงวิศวกรรม** (engineered standards/yard/automation) ที่บางกว่า Oracle WMS Cloud/SAP EWM. สำหรับ pattern healthcare/blood-bank: directed put-away คุมอุณหภูมิ + RF/barcode + lot/expiry ตรงกับงานคลัง cold-chain (ศูนย์บริการโลหิต/สถานผลิตชีววัตถุ) — ปิดด้วย NetSuite WMS SuiteApp ได้. **Over-spec rebuttal:** slotting/labor management ระดับ DC พาณิชย์แทบไม่มี use case ในองค์กรกระจายปริมาณต่ำ-กลาง; งานปริมาณสูง/ซับซ้อนจริงเสริมด้วย SuiteApp พาร์ทเนอร์ (RF-SMART/Infios) ได้.

**Procurement caveat:**
ต้องตั้งงบซื้อ WMS SuiteApp เป็นรายการแยก (ไม่รวมในฐาน ERP) — ควรระบุเป็นต้นทุนที่วางแผนได้ ไม่ใช่ข้ออ่อนเชิงฟังก์ชัน. หลีกเลี่ยงการเขียนสเปกล็อก "labor management เชิงวิศวกรรม native" ซึ่งเป็น over-spec และเอียงไปทาง tier-1.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] WMS4-WMS Outbound Fulfillment (0.65) — Create a Wave/Template/Location
- [KB] WMS Advanced Setup (0.60) — Pick zones, Picking/Replenishment/Staging Strategies
- [WEB:netsuite.com] NetSuite WMS product page — mobile RF barcode, putaway/picking strategies, wave release
- [WEB:houseblend.io] NetSuite WMS Setup, Mobile RF & Wave Picking — zone picking, directed putaway, task/labor KPIs

---

## F-WMS-02 — Transportation Management (TMS)

**Capability (TH):** การบริหารการขนส่ง (คิดค่าขนส่ง/จัดเส้นทาง/ค่าระวาง)
**Capability (EN):** Transportation management

**Domain + iCE severity:** SCM · **แทบไม่มีผล (Negligible)**

**จุดที่ NetSuite สู้ไม่ได้ (Gap):**
TOR ให้คะแนน NetSuite = 0 ("ทำไม่ได้เลย") ระบุว่า NetSuite "ไม่มี TMS ในตัว (มีแค่ shipping integration)" ขณะที่ Oracle OTM เป็น full TMS (carrier rating, route optimization, freight settlement). สเปกแนะนำบังคับ carrier rating + route optimization + freight settlement.

**Counter / Mitigation:**
ข้ออ้าง "ไม่มี TMS native" **ถูกต้องตามข้อเท็จจริง** — NetSuite ไม่มี native carrier rating engine, route optimization หรือ freight settlement มีเพียง shipping integration (FedEx/UPS/USPS real-time rate + label). แต่การให้คะแนน 0 ("ทำไม่ได้เลย") **แรงเกินไป** เพราะ shipping integration เป็น native และ TMS เต็มรูปเติมได้ครบผ่าน **certified SuiteApp** (SuiteFleet, FreightPOP, Pacejet).

**Over-spec rebuttal:** TMS ระดับ Oracle OTM ออกแบบสำหรับผู้ส่งสินค้า/ผู้ส่งออกข้ามชาติเชิงพาณิชย์ ไม่ใช่ภารกิจกระจายโลหิต/เซรุ่มในประเทศ. สำหรับ pattern healthcare/non-profit: การกระจายในประเทศด้วยรถ/ผู้ส่งของตนเองอาจได้ประโยชน์เล็กน้อยจาก last-mile route/dispatch (เช่น SuiteFleet SuiteApp) แต่ไม่ต้องใช้ TMS พาณิชย์ (carrier rating/freight settlement) ระดับ enterprise.

**Procurement caveat:**
การใส่ full-TMS native เป็น requirement สำหรับองค์กรสาธารณกุศลในประเทศ = over-spec/ล็อกสเปกไปทาง Oracle — เสี่ยงข้อท้วงติง สตง. ควรเขียนเป็นผลลัพธ์ (คำนวณค่าจัดส่ง + จัดเส้นทางกระจายในประเทศ) ที่ตอบได้ด้วย native shipping + SuiteApp.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-Shipping Guide (0.59) — carrier label integration เท่านั้น ไม่มี TMS native (theme tms top score 0.59)
- [WEB:netsuite.com] What Is a Transportation Management System (article)
- [WEB:suitefleet.com] NetSuite Route Optimization / TMS SuiteApp (Azdan) — route optimization/dispatch เสริมภายนอกแบบ SuiteApp

---

## GP-FUNC-04 — Demand Planning & Statistical Forecasting

**Capability (TH):** วางแผนอุปสงค์ / พยากรณ์เชิงสถิติ
**Capability (EN):** Demand planning & statistical forecasting

**Domain + iCE severity:** SCM · **ต่ำ (Low)**

**จุดที่ NetSuite สู้ไม่ได้ (Gap):**
Gap Pack (3-way) ให้ NetSuite = 1★, Oracle Fusion = 5★★★★★, SAP S/4HANA = 4★★★★, Gap Severity = Critical, Fusion เด่นสุด. หมายเหตุ: "NetSuite Demand Planning จำกัดมาก; Oracle SCM Demand Mgmt เป็นจุดแข็งที่นำหน้าทั้งคู่".

**Counter / Mitigation:**
การจัด 1★ "จำกัดมาก" **ต่ำกว่าจริง**. NetSuite Demand Planning เป็นฟีเจอร์ในตัวและมีพยากรณ์เชิงสถิติ 4 วิธี (Linear Regression / Moving Average / Seasonal Average / Sales Forecast) วิเคราะห์ stock demand จาก historical. การลดเหลือ 1★ สะท้อนการตั้งสเปกเทียบ tier-1 มากกว่าความต้องการจริง.

**Gap จริงที่เหลือ:** เป็นวิธีพื้นฐาน — ไม่มี demand sensing/ML และ collaboration แบบ Oracle SCM Demand Management. **Over-spec rebuttal:** ความสามารถพยากรณ์อุปสงค์เชิงสถิติมีในตัวและเพียงพอกับสเกลองค์กรกุศล; สำหรับ pattern blood-bank/healthcare การพยากรณ์ความต้องการเลือด/วัคซีน/เซรุ่มใช้วิธีสถิติ native ครอบคลุมได้ ไม่ต้องถึง demand forecasting ระดับ tier-1.

**Procurement caveat:**
การตั้ง Gap Severity = Critical และล็อกสเปก tier-1 demand forecasting/ML native เป็นการเอียงไปทาง Oracle SCM Cloud — ควรทบทวนให้เป็น outcome-based ตามปริมาณและอายุสินค้าจริง.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-Inventory Management (0.69) — Demand Planning วิเคราะห์ stock demand จาก historical
- [KB] NSIMG (0.66) — Demand Plans/Supply Plans, Seasonal Average method
- [WEB:docs.oracle.com] NetSuite Applications Suite — Calculating Item Demand (Linear Regression/Moving Average/Seasonal Average/Sales Forecast)

---

## GP-FUNC-06 — Warehouse Management (WMS) — wave/zone, RF, 3PL

**Capability (TH):** คลังสินค้าขั้นสูง (WMS, wave/zone, RF)
**Capability (EN):** Warehouse Mgmt (WMS) — wave/zone, RF, 3PL

**Domain + iCE severity:** SCM · **กลาง (Medium)**

**จุดที่ NetSuite สู้ไม่ได้ (Gap):**
Gap Pack ให้ NetSuite = 2★★, Oracle Fusion = 4★★★★, SAP S/4HANA = 5★★★★★, Gap Severity = High, Fusion เด่นสุด. หมายเหตุ: "NetSuite WMS เป็น add-on ตื้น; SAP EWM ลึกสุด, Oracle WMS Cloud แข็งแรง".

**Counter / Mitigation:**
rating 2/"add-on ตื้น" **ลดทอนเกินจริง**. NetSuite WMS เป็น **first-party SuiteApp** (ต้องซื้อ license แยก) รองรับ wave/zone picking, RF/barcode, directed put-away ในตัว ส่วน multi-location/multi-warehouse เป็น native ของ ERP ฐาน — ความสามารถหลักของ requirement ทำได้ในตัว. คำว่า "add-on" ถูกบางส่วน (เป็น SuiteApp ที่ซื้อเพิ่ม) แต่ "ตื้น" ไม่ถูก.

**ที่ SAP EWM/Oracle WMS Cloud ลึกกว่าจริง** คือ **3PL billing เชิงลึก, slotting optimization และ yard management** — งานปริมาณสูง/ซับซ้อนมักเสริมด้วย SuiteApp พาร์ทเนอร์ (RF-SMART/Infios). **Over-spec rebuttal:** สำหรับ pattern blood-bank/healthcare (คลังหลายแห่ง, lot/expiry, RF, cold-chain) NetSuite WMS เหมาะกับปริมาณต่ำ-กลางและครอบคลุมได้; 3PL/yard management แทบไม่เกี่ยวกับภารกิจ.

**Procurement caveat:**
ต้นทุน license WMS SuiteApp เป็นรายการที่ต้องวางแผน (ระบุใน TCO). หลีกเลี่ยงการล็อกสเปก "3PL billing / slotting optimization native" ซึ่งเกินภารกิจและเอียงไปทาง SAP EWM/Oracle.

**Confidence:** medium

**หลักฐาน / Citation:**
- [KB] WMS4-WMS Outbound Fulfillment (0.65) — wave; WMS Advanced Setup (0.60) — zones/strategies
- [WEB:netsuite.com] NetSuite WMS product page — RF, putaway/picking strategies, cycle count
- [WEB:brokenrubik.com] Best WMS for NetSuite 2026: Native vs RF-SMART/Infios — native WMS มี wave/zone/directed ops แต่วางตำแหน่งปริมาณต่ำ-กลาง, 3rd-party ลึกกว่าด้าน labor/slotting

---

## GP-FUNC-07 — Transportation Management (TMS) / Logistics

**Capability (TH):** การขนส่ง (TMS) / โลจิสติกส์
**Capability (EN):** Transportation Management (TMS)

**Domain + iCE severity:** SCM · **แทบไม่มีผล (Negligible)**

**จุดที่ NetSuite สู้ไม่ได้ (Gap):**
Gap Pack ให้ NetSuite = 0 (–), Oracle Fusion = 4★★★★, SAP S/4HANA = 5★★★★★, Gap Severity = High, Fusion เด่นสุด. หมายเหตุ: "NetSuite ไม่มี TMS native; ต้องต่อ 3rd party".

**Counter / Mitigation:**
ข้ออ้าง **ถูกในเชิงเทคนิค** — NetSuite ไม่มี TMS native มีแค่ shipping label integration; TMS เต็มรูปต้องต่อ SuiteApp/3rd party. แนวตั้งรับคือปิดด้วย **certified SuiteApp/partner** (ผลสำรวจ Top 20 TMS สำหรับ NetSuite ล้วนเป็น SuiteApp/partner) — carrier rating/route optimization/freight settlement เติมได้ครบผ่านพันธมิตร.

**Over-spec rebuttal:** TMS (carrier rating/route optimization/freight settlement) เป็นความสามารถของบริษัทโลจิสติกส์/ผู้ส่งออกข้ามชาติ — ตัวข้อความ Gap Pack เองยอมรับว่า SAP GTS/OTM เป็นมาตรฐานองค์กรข้ามชาติ. สำหรับ pattern non-profit/public-sector ในประเทศ ไม่มีการบริหารขนส่งเชิงพาณิชย์ระดับองค์กรเป็นกระบวนการหลัก งานกระจายในประเทศใช้ shipping integration + last-mile dispatch SuiteApp ก็เพียงพอ.

**Procurement caveat:**
การบังคับ TMS native ใน TOR สำหรับองค์กรสาธารณกุศลในประเทศ = over-spec/ล็อกสเปกชัดเจน — เสี่ยงข้อท้วงติง สตง. ควรเขียนเป็นผลลัพธ์การกระจายในประเทศ ไม่ผูกกับ TMS engine ใน ERP.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-Shipping Guide (0.59) — theme tms มีแต่ shipping label integration ไม่มี TMS native
- [WEB:netsuite.com] NetSuite Logistics ERP / TMS article — TMS เป็น integration/partner ไม่ใช่โมดูล native
- [WEB:suitefleet.com] Top 20 Transportation Management Systems 2026 — ทั้งหมดเป็น SuiteApp/partner

---

## GP-STANDOUT-06 — Fusion Standout: Demand Planning & SCM Cloud Breadth

**Capability (TH):** วางแผนอุปสงค์ / ความกว้างของ SCM Cloud
**Capability (EN):** Fusion standout: Demand planning & SCM Cloud breadth

**Domain + iCE severity:** SCM · **ต่ำ (Low)**

**จุดที่ NetSuite สู้ไม่ได้ (Gap):**
Gap Pack จัดเป็นจุดเด่น (standout) ของ Oracle Fusion อันดับ 6. เทียบ NetSuite: "NetSuite Demand Planning ตื้น"; เทียบ SAP: "SAP IBP ดีแต่แยก license/landscape". เหตุผลที่ Fusion เด่นสุด: Oracle SCM Cloud (Demand/Supply/Inventory) กว้างและรวมในชุดเดียวกับ ERP — ครบกว่าและกลืนกับ Finance.

**Counter / Mitigation:**
จุดอ่อนจริง: ฟังก์ชัน Demand Planning ของ NetSuite ตื้นกว่า Oracle SCM Cloud (พยากรณ์เชิงสถิติพื้นฐาน ไม่มี demand sensing/ML และไม่มี S&OP). **แนวตั้งรับ:** ปิดงานจริงด้วย native inventory + reorder point + lot/expiry + Demand Planning 4 วิธี ซึ่งครอบคลุมงานคลังโลหิต/เวชภัณฑ์ตามสเกล.

**Over-spec rebuttal:** ความเกี่ยวข้องต่ำ — pattern blood-bank/healthcare/non-profit ไม่ใช่ผู้ผลิต/กระจายสินค้าเชิงพาณิชย์ขนาดใหญ่. งานพยากรณ์ความต้องการเลือด/เวชภัณฑ์/เซรุ่มมี use case จริง แต่ใช้ native demand planning + reorder point + lot/expiry ครอบคลุมได้; demand/supply planning เต็มรูป (demand sensing/ML/S&OP) เป็น over-spec.

**Procurement caveat:**
"ความกว้าง/ครบชุด SCM Cloud" เป็นจุดขายเชิงสถาปัตยกรรมของ Oracle — ไม่ควรแปลงเป็น requirement เชิงบังคับ (breadth requirement) เพราะสร้างข้อได้เปรียบเทียมและเสี่ยงล็อกสเปก.

**Confidence:** medium
*(หมายเหตุ: บันทึก standout นี้มี KB/web citation เชิงผลิตภัณฑ์ในตัวอย่างจำกัด — ข้อสรุปเชิงเปรียบเทียบอิงตำแหน่งผลิตภัณฑ์มาตรฐาน จึงกำหนดความเชื่อมั่นระดับ medium)*

**หลักฐาน / Citation:**
- (ไม่มี KB/web citation เฉพาะรายการในบันทึก standout ต้นทาง — ข้อโต้แย้ง native demand planning อ้างอิงหลักฐานร่วมใน GP-FUNC-04: NetSuite Demand Planning 4 วิธีสถิติ native + reorder point + lot/expiry)

---

## TOR-SCM-02 — TOR Spec: Advanced Warehouse Management (WMS) Directed Operations

**Capability (TH):** ข้อกำหนด TOR — คลังสินค้าขั้นสูง (WMS) แบบสั่งการ
**Capability (EN):** TOR: Warehouse management (WMS) directed operations

**Domain + iCE severity:** SCM · **กลาง (Medium)**

**จุดที่ NetSuite สู้ไม่ได้ (Gap):**
ข้อกำหนด TOR (Type: Functional, Priority: Important): "ระบบต้องมีการจัดการคลังสินค้าขั้นสูง (WMS) รองรับ wave/zone/batch picking, directed put-away, การทำงานผ่าน RF/barcode และการบริหารหลายคลัง/3PL". NetSuite ตอบได้ = Partial. Differentiator note: "NetSuite WMS เป็น add-on ตื้น; SAP EWM/Oracle WMS Cloud ลึกกว่า".

**Counter / Mitigation:**
การให้ "Partial" **ประเมินต่ำกว่าความจริง** สำหรับ requirement ที่ระบุ — wave/zone/batch picking, directed put-away, RF/barcode และ multi-warehouse ทั้งหมดเป็นฟีเจอร์ในตัวของ **NetSuite WMS SuiteApp** (first-party, ซื้อ license แยก). อย่างไรก็ตาม "Partial" มีมูลบางส่วน เพราะ native WMS วางตำแหน่งปริมาณต่ำ-กลาง และงานสูง/ซับซ้อนมักเสริม RF-SMART.

**ที่อ่อนกว่าจริง** คือ **3PL billing เชิงลึก และ slotting optimization ระดับ SAP EWM**. **Over-spec rebuttal:** สำหรับคลัง cold-chain ของ pattern blood-bank/healthcare (ปริมาณไม่สูงมาก, หลายคลัง, lot/expiry, RF, directed put-away คุมอุณหภูมิ) native WMS น่าจะเพียงพอ ส่วน 3PL billing อยู่นอกภารกิจ.

**Procurement caveat:**
Priority "Important" กับข้อความ "add-on ตื้น" ประเมิน NetSuite ต่ำกว่าจริง — ควรระบุ requirement เป็นผลลัพธ์ (directed put-away คุมอุณหภูมิ + RF + lot/expiry หลายคลัง) แทนการล็อกสเปก 3PL/slotting ระดับ enterprise ที่เอียงไปทาง SAP EWM. ต้นทุน license WMS SuiteApp ต้องระบุใน TCO. *(หมายเหตุต้นทาง: [ต้อง verify] กับ environment จริงก่อนตัดสิน)*

**Confidence:** medium

**หลักฐาน / Citation:**
- [KB] WMS4-WMS Outbound Fulfillment (0.65) — wave; WMS Advanced Setup (0.60) — zone/batch/RF strategies
- [WEB:netsuite.com] NetSuite WMS product page — directed putaway, RF barcode, multi-location
- [WEB:houseblend.io] NetSuite WMS Optimization: Slotting & Picking — มี slotting/picking strategies (ลึกน้อยกว่ามาตรฐาน enterprise)

---

*KB generated for skill `oracle-netsuite-consulting` · product angle: NetSuite Weakness & Counter · industry: logistics · source: TOR Requirement Bank + Gap Pack v2 · last_verified 2026-06-29 · balanced per iCE Second Opinion (client name generalized to healthcare/blood-bank/non-profit/public-sector patterns).*
