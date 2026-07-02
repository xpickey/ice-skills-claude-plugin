# TOR Competitive KB — logistics — Oracle Fusion Standout & TOR Weaponization

---
last_verified: "2026-06-29"
source: "TOR Requirement Bank + Gap Pack v2"
confidence_note: "แต่ละ record ระบุ Confidence (high/medium/low) ตามว่ามี KB/เว็บทางการยืนยันหรือไม่ — ห้ามยกระดับความเชื่อมั่นเกินหลักฐานที่มี. หลาย gap เป็น 'ช่องว่างตามสเปก' ที่ปิดได้ด้วย NetSuite first-party add-on (NSPB, NSAR, NSAW, WMS SuiteApp) หรือเป็น over-spec — ให้เก็บทั้งฝั่งรุกและ counter-view ของ iCE ไว้เสมอ. This file is written from the Oracle Fusion SELL angle; the iCE second-opinion caveats are preserved to keep procurement fair and สตง.-defensible."
ams_review: "yearly — re-verify product positions"
---

## บริบทของ vertical นี้ / How to use this file

หมวด **logistics** ในที่นี้ครอบคลุมงานคลังสินค้า (WMS), การขนส่ง (TMS) และการวางแผนอุปสงค์/อุปทาน (demand & supply planning) — ทั้งในบริบทของผู้ให้บริการโลจิสติกส์/กระจายสินค้าเชิงพาณิชย์ และในบริบทของ **healthcare / blood-bank / non-profit foundation / public-sector** ที่มีคลัง cold-chain สำหรับโลหิต เวชภัณฑ์ เซรุ่ม และวัคซีน. เมื่อ iCE ขาย Oracle Fusion เอกสารนี้ให้ (ก) จุดที่ Fusion ชนะจริง (Standout), (ข) ถ้อยคำ TOR ที่ควรบรรจุเพื่อให้คู่แข่ง NetSuite ตอบได้เพียง Partial/No, และ (ค) **iCE caveat** เตือนความเสี่ยง over-spec / ล็อกสเปกที่อาจถูกท้วงติงโดย สตง. หรือผู้ยื่นรายอื่น.

**คำเตือนหลัก (จาก second_opinion):** เอกสารต้นทางเป็น "ชุดร่าง TOR เชิงแข่งขัน" ที่ออกแบบให้ NetSuite ตอบได้แค่ Partial/No — ไม่ใช่การวิเคราะห์ความต้องการที่เป็นกลาง. หลายข้อในหมวดโลจิสติกส์ (TMS เต็มรูป, S&OP/IBP, slotting/labor management ระดับ DC พาณิชย์) เป็น over-spec สำหรับองค์กรที่ไม่ใช่ผู้ผลิต/กระจายสินค้าเชิงพาณิชย์ขนาดใหญ่. ก่อนบรรจุลง TOR จริง ควรเขียน requirement แบบ **outcome-based** ตามภารกิจจริง ไม่ผูกกับฟีเจอร์เฉพาะผลิตภัณฑ์ เพื่อลดความเสี่ยงถูกท้วงติงเรื่องความเป็นธรรม.

---

## F-SCM-01 — Demand/supply planning & S&OP

- **Capability (TH):** การวางแผนความต้องการและอุปทาน (demand & supply planning) พร้อม S&OP
- **Capability (EN):** Demand/supply planning & S&OP
- **Domain:** SCM (Supply Chain Planning) · **iCE severity:** ต่ำ

**Oracle Fusion advantage (Standout):**
Oracle SCM Planning Cloud เป็น tier-1 planning platform — มีการพยากรณ์เชิงสถิติขั้นสูง, demand sensing/ML และกระบวนการ S&OP/IBP ที่เชื่อมแผนขาย-ผลิต-การเงินเข้าด้วยกันแบบ consensus ในตัว. เทียบกับ NetSuite ที่มี Demand Planning/Supply Planning/DRP ในตัว (ภายใต้ Advanced Inventory) แต่ใช้วิธีพยากรณ์พื้นฐานเพียง 4 วิธี (Linear Regression, Moving Average, Seasonal Average, Sales Forecast) และ **ไม่มี S&OP (Sales & Operations Planning) ระดับองค์กร** — จุดนี้เป็น gap จริงที่ Fusion เหนือกว่า. สำหรับผู้ให้บริการโลจิสติกส์/กระจายสินค้าที่ต้องรัน consensus planning ข้ามหน่วยงาน ความกว้างและการกลืนกับ Finance ของ Oracle SCM Cloud เป็นข้อได้เปรียบชัดเจน.

**TOR wording to weaponize (ภาษาไทย):**
"ระบบต้องมีแพลตฟอร์มวางแผนความต้องการและอุปทาน (demand & supply planning) พร้อมการพยากรณ์เชิงสถิติ (statistical forecasting) และกระบวนการ S&OP ในตัว"

**TOR wording (English):**
"The solution must provide a native demand & supply planning platform with statistical forecasting and S&OP."

**iCE caveat (over-spec / procurement-fairness):**
คะแนน "1 — ต้อง add-on/custom" ในต้นทางเหมารวมเกินจริง: งานวางแผนอุปสงค์/อุปทานพื้นฐาน NetSuite ทำได้ในตัว (ยืนยันจากเว็บทางการ) — gap จริงคือ S&OP enterprise ซึ่งเป็นเพียงครึ่งเดียวของข้อกำหนด. สำหรับคลังโลหิต/เวชภัณฑ์ (blood-bank/healthcare) native demand planning พอใช้ตามสเกล (เลือดอายุสั้นอาจต้องปรับแต่งวิธีพยากรณ์) ส่วน S&OP เต็มรูปแบบเกินความจำเป็น (over-spec). การบรรจุ "S&OP ในตัว" แบบ Mandatory จึงมีลักษณะล็อกสเปกไปทาง Oracle — ให้ระวังหากผู้ซื้อไม่ได้เป็นผู้ผลิต/กระจายสินค้าเชิงพาณิชย์ขนาดใหญ่.

**Confidence:** high
**หลักฐาน / Citation:**
- [KB] Netsuite-Inventory Management (0.69) — Demand Planning เป็นฟีเจอร์ในตัว + Distribution Resource Planning + projection methods
- [KB] NSIMG (0.66) — Demand Plans/Supply Plans, Seasonal Average method, Supply Allocation หลาย location
- [WEB:docs.oracle.com] NetSuite Applications Suite — Calculating Item Demand (4 วิธีพยากรณ์เชิงสถิติ native, /ns-online-help/section_N2290234.html)
- [ความเชื่อมั่น: สูง]

---

## F-WMS-01 — Directed warehouse operations (WMS)

- **Capability (TH):** Warehouse Management แบบสั่งการอัตโนมัติ (directed operations)
- **Capability (EN):** Directed warehouse operations
- **Domain:** SCM (Warehouse & Logistics) · **iCE severity:** กลาง

**Oracle Fusion advantage (Standout):**
Oracle WMS Cloud เป็น tier-1 WMS — รองรับ directed put-away/picking, wave management, และ **warehouse labor management + slotting optimization เชิงวิศวกรรม** (engineered standards, yard, automation) ในระดับ DC พาณิชย์ที่ NetSuite WMS ยังบางกว่า. NetSuite WMS เป็น SuiteApp ที่ต้องซื้อ license แยก (ไม่รวมใน ERP ฐาน) — มี directed put-away, wave/zone release, RF/barcode และ cycle count ในตัว แต่วางตำแหน่งสำหรับปริมาณงานต่ำ-กลาง. สำหรับผู้ให้บริการโลจิสติกส์/3PL ที่มี throughput สูง การจัดคลื่นงานและบริหารแรงงานคลังระดับ tier-1 ของ Oracle เป็นจุดแยกที่ชัดเจน.

**TOR wording to weaponize (ภาษาไทย):**
"ระบบต้องมีการบริหารคลังสินค้าแบบสั่งการอัตโนมัติ (directed operations): directed put-away/picking, การจัดคลื่นงาน (wave) และการบริหารแรงงานคลัง (labor management)"

**TOR wording (English):**
"The solution must provide warehouse management with directed operations: directed put-away/picking, wave management and warehouse labor management."

**iCE caveat (over-spec / procurement-fairness):**
ข้อความต้นทาง "ไม่มี wave ขั้นสูง" **คลาดเคลื่อน** — wave/zone/directed put-away เป็นฟีเจอร์ในตัวของ NetSuite WMS (ยืนยันจาก netsuite.com). ที่อ่อนกว่าจริงเหลือเพียง slotting optimization และ labor management ระดับ tier-1 ซึ่งเป็น over-spec สำหรับคลัง cold-chain ของ healthcare/blood-bank ที่ปริมาณงานไม่สูงถึงระดับ DC พาณิชย์. directed put-away คุมอุณหภูมิ, RF/barcode, lot/expiry ตรงกับงานคลังโลหิต/เซรุ่มจริง (NetSuite ทำได้) — จุดขายที่ควรใช้คือ labor management ของ high-volume 3PL ไม่ใช่การอ้างว่า NetSuite ทำ directed operations ไม่ได้. ข้อควรระวัง: WMS เป็น SuiteApp ที่ต้องซื้อเพิ่มทั้งสองผลิตภัณฑ์ — ให้ชั่ง TCO ตามจริง.

**Confidence:** high
**หลักฐาน / Citation:**
- [KB] WMS4-WMS Outbound Fulfillment (0.65) — Create a Wave/Template/Location
- [KB] WMS Advanced Setup (0.60) — Pick zones, Picking/Replenishment/Staging Strategies
- [WEB:netsuite.com] NetSuite WMS product page — mobile RF barcode, putaway/picking strategies, wave release
- [WEB:houseblend.io] NetSuite WMS Setup, Mobile RF & Wave Picking — zone picking, directed putaway, task/labor KPIs
- [ความเชื่อมั่น: สูง]

---

## F-WMS-02 — Transportation management (TMS)

- **Capability (TH):** การบริหารการขนส่ง (Transportation Management, TMS)
- **Capability (EN):** Transportation management
- **Domain:** SCM (Warehouse & Logistics) · **iCE severity:** แทบไม่มีผล

**Oracle Fusion advantage (Standout):**
Oracle OTM (Oracle Transportation Management) เป็น full TMS — มี carrier rating, route optimization และ freight settlement ในตัวสำหรับผู้ส่งสินค้า/ผู้ให้บริการขนส่งข้ามชาติ. NetSuite **ไม่มี TMS เต็มรูปแบบ native** — มีเพียง shipping integration (FedEx/UPS/USPS real-time rate + label); TMS เต็มรูปต้องเสริมด้วย SuiteApp (SuiteFleet, FreightPOP, Pacejet). สำหรับบริษัทโลจิสติกส์เชิงพาณิชย์ที่การบริหารค่าระวางและการจัดเส้นทางเป็นแกนหลักของธุรกิจ Oracle OTM เป็นข้อได้เปรียบที่ชัดเจนที่สุดในหมวดนี้.

**TOR wording to weaponize (ภาษาไทย):**
"ระบบต้องมีการบริหารการขนส่ง (transportation management): การคิดค่าขนส่ง (carrier rating), การจัดเส้นทาง (route optimization) และการบริหารค่าระวาง (freight settlement)"

**TOR wording (English):**
"The solution must provide transportation management: carrier rating, route optimization and freight settlement."

**iCE caveat (over-spec / procurement-fairness):**
ข้ออ้าง "ไม่มี TMS native" ถูกต้อง แต่การให้คะแนน 0/"ทำไม่ได้เลย" ในต้นทาง **แรงเกินไป** เพราะ shipping integration เป็น native และ SuiteApp เติม TMS ได้ครบ. TMS ระดับ Oracle OTM ออกแบบให้ผู้ส่งสินค้าข้ามชาติ — สำหรับ non-profit/healthcare ที่กระจายโลหิต/เซรุ่มในประเทศด้วยรถ/ผู้ส่งของตนเอง อาจได้ประโยชน์เล็กน้อยจาก last-mile route/dispatch (เช่น SuiteFleet SuiteApp) แต่ไม่ต้องใช้ TMS พาณิชย์ (carrier rating/freight settlement) ระดับ enterprise. การบรรจุ TMS เต็มรูปใน TOR สำหรับองค์กรที่ไม่ทำขนส่งเชิงพาณิชย์เป็นแกนหลัก = over-spec / ล็อกสเปกชัดเจน — ควรใช้เฉพาะเมื่อผู้ซื้อเป็นผู้ให้บริการโลจิสติกส์จริง.

**Confidence:** high
**หลักฐาน / Citation:**
- [KB] Netsuite-Shipping Guide (0.59) — carrier label integration เท่านั้น ไม่มี TMS native (theme tms top score 0.59)
- [WEB:netsuite.com] What Is a Transportation Management System (article)
- [WEB:suitefleet.com] NetSuite Route Optimization / TMS SuiteApp (Azdan) — route optimization/dispatch เสริมภายนอกแบบ SuiteApp
- [ความเชื่อมั่น: สูง]

---

## GP-FUNC-04 — Demand planning & statistical forecasting

- **Capability (TH):** วางแผนอุปสงค์ / พยากรณ์เชิงสถิติ
- **Capability (EN):** Demand planning & statistical forecasting
- **Domain:** SCM (Supply Chain) · **iCE severity:** ต่ำ

**Oracle Fusion advantage (Standout):**
ในการเทียบ 3 ทาง (NetSuite 1★ / Oracle Fusion 5★★★★★ / SAP S/4HANA 4★★★★) Oracle Fusion **เด่นสุด (✔✔)** ในหมวดนี้ — Oracle SCM Demand Management เป็นจุดแข็งที่นำหน้าทั้ง NetSuite และ SAP: มี demand sensing, ML-based forecasting และ collaboration ในตัว. NetSuite Demand Planning เป็นฟีเจอร์ในตัวและมีพยากรณ์เชิงสถิติ 4 วิธี (Linear Regression/Moving Average/Seasonal Average/Sales Forecast) แต่เป็นวิธีพื้นฐาน — ไม่มี demand sensing/ML. สำหรับผู้กระจายสินค้าที่ความแม่นยำของ forecast กระทบต้นทุนสต็อกโดยตรง ความลึกของ Oracle เป็นจุดแยกที่วัดผลได้.

**TOR wording to weaponize (ภาษาไทย):**
"ระบบต้องมีการวางแผนอุปสงค์ (demand planning) พร้อมการพยากรณ์เชิงสถิติขั้นสูง รองรับ demand sensing/ML และการทำงานร่วม (collaboration) ในตัว โดยไม่ต้องใช้เครื่องมือภายนอก"
(สังเคราะห์จาก differentiator ในต้นทาง: "NetSuite Demand Planning จำกัดมาก; Oracle SCM Demand Mgmt เป็นจุดแข็งที่นำหน้าทั้งคู่")

**TOR wording (English):**
"The solution must provide demand planning with advanced statistical forecasting, native demand sensing/ML and collaboration, without external tools."
(Synthesized from the source differentiator note; the source Gap Pack provides the 3-way rating, not a verbatim TOR sentence for this row — see TOR-SCM-01/F-SCM-01 for the exact weaponized wording.)

**iCE caveat (over-spec / procurement-fairness):**
การจัด NetSuite ที่ 1★ "จำกัดมาก" **ต่ำกว่าความจริง** — ความสามารถพยากรณ์อุปสงค์เชิงสถิติมีในตัว (ยืนยันจากเว็บทางการ) และเพียงพอกับสเกลองค์กรกุศล/สาธารณะ. การลดเหลือ 1★ สะท้อนการตั้งสเปกเทียบ tier-1 มากกว่าความต้องการจริง. สำหรับ blood-bank/healthcare การพยากรณ์ความต้องการเลือด/วัคซีน/เซรุ่มมีประโยชน์จริง แต่ native ของ NetSuite (วิธีพื้นฐาน) ครอบคลุมได้ ไม่ต้องถึง demand forecasting ระดับ tier-1 — ระวังการล็อกสเปกด้วย demand sensing/ML หากผู้ซื้อไม่ใช่ผู้กระจายสินค้าเชิงพาณิชย์.

**Confidence:** high
**หลักฐาน / Citation:**
- [KB] Netsuite-Inventory Management (0.69) — Demand Planning วิเคราะห์ stock demand จาก historical
- [KB] NSIMG (0.66) — Demand Plans/Supply Plans, Seasonal Average method
- [WEB:docs.oracle.com] NetSuite Applications Suite — Calculating Item Demand (Linear Regression/Moving Average/Seasonal Average/Sales Forecast)
- [ความเชื่อมั่น: สูง]

---

## GP-FUNC-06 — Warehouse management (WMS) — wave/zone, RF, 3PL

- **Capability (TH):** คลังสินค้าขั้นสูง (WMS, wave/zone, RF, 3PL)
- **Capability (EN):** Warehouse Mgmt (WMS) — wave/zone, RF, 3PL
- **Domain:** SCM (Supply Chain) · **iCE severity:** กลาง

**Oracle Fusion advantage (Standout):**
ในการเทียบ 3 ทาง (NetSuite 2★★ / Oracle Fusion 4★★★★ / SAP S/4HANA 5★★★★★) Oracle Fusion **เด่นสุด (✔)** เหนือ NetSuite — Oracle WMS Cloud แข็งแรงในด้าน 3PL billing เชิงลึก, slotting optimization และ yard management ที่ NetSuite WMS (first-party SuiteApp, ซื้อ license แยก) ยังบางกว่า. (หมายเหตุ: SAP EWM ลึกสุดในสามค่าย แต่เมื่อ iCE ขาย Fusion จุดขายคือ Oracle WMS Cloud รวมในชุดเดียวกับ ERP/Finance และเหนือ NetSuite ในงาน high-volume/3PL.) สำหรับผู้ให้บริการโลจิสติกส์/3PL ที่ต้องออกบิลค่าบริการคลังตามกิจกรรม ความลึกของ Oracle เป็นจุดแยกที่ชัด.

**TOR wording to weaponize (ภาษาไทย):**
"ระบบต้องมีการจัดการคลังสินค้าขั้นสูง (WMS) รองรับ wave/zone/batch picking, directed put-away, การทำงานผ่าน RF/barcode, การบริหารหลายคลัง และการเรียกเก็บค่าบริการคลังแบบ 3PL (3PL billing) พร้อม slotting optimization ในตัว"
(สังเคราะห์จาก differentiator: "NetSuite WMS เป็น add-on ตื้น; SAP EWM ลึกสุด, Oracle WMS Cloud แข็งแรง" — จุดที่อ่อนจริงของ NetSuite = 3PL billing + slotting; ดู TOR-SCM-02 สำหรับถ้อยคำ TOR ที่ระบุไว้ตรง ๆ)

**TOR wording (English):**
"The solution must provide advanced Warehouse Management (WMS) supporting wave/zone/batch picking, directed put-away, RF/barcode operations, multi-warehouse management, and native 3PL billing with slotting optimization."
(Synthesized; the exact TOR-spec sentence for WMS is captured verbatim under TOR-SCM-02 below.)

**iCE caveat (over-spec / procurement-fairness):**
rating 2★/"add-on ตื้น" ในต้นทาง **ลดทอนเกินจริง** — ความสามารถหลักของ requirement (wave/zone/RF/directed put-away) NetSuite WMS ทำได้ในตัว (คำว่า "ตื้น" ไม่ถูก แม้ "add-on" จะจริงบางส่วนเพราะเป็น SuiteApp ที่ซื้อเพิ่ม และเหมาะปริมาณต่ำ-กลาง). ที่ Oracle WMS Cloud/SAP EWM ลึกกว่าจริงคือ 3PL billing และ slotting optimization — สำหรับคลังหลายแห่งของ blood-bank/healthcare (lot, expiry, RF) 3PL/yard management แทบไม่เกี่ยว. การบรรจุ 3PL billing/slotting ระดับ enterprise ลง TOR ขององค์กรที่ไม่ใช่ 3PL = over-spec; ควรใช้เฉพาะเมื่อผู้ซื้อดำเนินธุรกิจคลังให้บริการบุคคลภายนอกจริง. ต้นทุน license WMS เป็นรายการที่ต้องวางแผน TCO ทั้งสองผลิตภัณฑ์.

**Confidence:** medium
**หลักฐาน / Citation:**
- [KB] WMS4-WMS Outbound Fulfillment (0.65) — wave; WMS Advanced Setup (0.60) — zones/strategies
- [WEB:netsuite.com] NetSuite WMS product page — RF, putaway/picking strategies, cycle count
- [WEB:brokenrubik.com] Best WMS for NetSuite 2026: Native vs RF-SMART/Infios — native WMS มี wave/zone/directed ops แต่วางตำแหน่งปริมาณต่ำ-กลาง, 3rd-party ลึกกว่าด้าน labor/slotting
- [ความเชื่อมั่น: กลาง]

---

## GP-FUNC-07 — Transportation management (TMS)

- **Capability (TH):** การขนส่ง (TMS) / โลจิสติกส์
- **Capability (EN):** Transportation Management (TMS)
- **Domain:** SCM (Supply Chain) · **iCE severity:** แทบไม่มีผล

**Oracle Fusion advantage (Standout):**
ในการเทียบ 3 ทาง (NetSuite 0 / Oracle Fusion 4★★★★ / SAP S/4HANA 5★★★★★) Oracle Fusion **เด่นสุด (✔)** เหนือ NetSuite ในหมวด TMS — NetSuite ไม่มี TMS native (ต้องต่อ 3rd party) ขณะที่ Oracle มี TMS ในชุด SCM Cloud. สำหรับบริษัทโลจิสติกส์/กระจายสินค้าที่ต้องการ carrier rating, route optimization และ freight settlement บนแพลตฟอร์มเดียวกับ ERP, Oracle เป็นข้อได้เปรียบ (แม้ SAP GTS/TMS จะลึกสุดในสามค่าย แต่จุดขายของ Fusion คือความกลืนกับ Finance).

**TOR wording to weaponize (ภาษาไทย):**
"ระบบต้องมีการบริหารการขนส่ง (TMS) แบบ native บนแพลตฟอร์มเดียวกับ ERP รองรับ carrier rating, route optimization และ freight settlement โดยไม่ต้องต่อระบบภายนอก"
(สังเคราะห์จาก differentiator: "NetSuite ไม่มี TMS native; ต้องต่อ 3rd party" — ดู F-WMS-02 สำหรับถ้อยคำ TOR ที่ระบุไว้ตรง ๆ)

**TOR wording (English):**
"The solution must provide native Transportation Management (TMS) on the same platform as the ERP — carrier rating, route optimization and freight settlement — without third-party connectors."
(Synthesized; the exact weaponized TMS sentence is captured verbatim under F-WMS-02 above.)

**iCE caveat (over-spec / procurement-fairness):**
ข้ออ้างถูกในเชิงเทคนิค (NetSuite ไม่มี TMS native จริง) แต่ TMS (carrier rating/route optimization/freight settlement) เป็นความสามารถของบริษัทโลจิสติกส์/ผู้ส่งออกข้ามชาติ. การบังคับใส่ใน TOR สำหรับ non-profit/healthcare/public-sector ในประเทศ = **over-spec / ล็อกสเปก** ชัดเจน — งานกระจายในประเทศใช้ shipping integration + last-mile dispatch SuiteApp ก็เพียงพอ. ให้ใช้ถ้อยคำนี้เฉพาะเมื่อผู้ซื้อบริหารขนส่งเชิงพาณิชย์ระดับองค์กรเป็นกระบวนการหลักจริง มิฉะนั้นเสี่ยงถูกท้วงติงเรื่องความเป็นธรรม.

**Confidence:** high
**หลักฐาน / Citation:**
- [KB] Netsuite-Shipping Guide (0.59) — theme tms มีแต่ shipping label integration ไม่มี TMS native
- [WEB:netsuite.com] NetSuite Logistics ERP / TMS article — TMS เป็น integration/partner ไม่ใช่โมดูล native
- [WEB:suitefleet.com] Top 20 Transportation Management Systems 2026 — ทั้งหมดเป็น SuiteApp/partner
- [ความเชื่อมั่น: สูง]

---

## GP-STANDOUT-06 — Fusion standout: Demand planning & SCM Cloud breadth

- **Capability (TH):** วางแผนอุปสงค์ / SCM Cloud (จุดเด่น Oracle Fusion)
- **Capability (EN):** Fusion standout — Demand planning & SCM Cloud breadth
- **Domain:** SCM · **iCE severity:** ต่ำ

**Oracle Fusion advantage (Standout):**
นี่คือ **จุดเด่นที่ Oracle Fusion ชนะโดยตรง** (Rank 6 ในชุด Fusion Standout): Oracle SCM Cloud (Demand/Supply/Inventory) กว้างและรวมอยู่ในชุดเดียวกับ ERP — ครบกว่าและกลืนกับ Finance. เทียบกับ NetSuite ที่ Demand Planning ตื้นกว่า และเทียบกับ SAP ที่ IBP ดีแต่แยก license/landscape ต่างหาก. จุดขายเชิงกลยุทธ์ของ Fusion ในหมวดโลจิสติกส์คือ "one suite" — วางแผนอุปสงค์-อุปทาน-สินค้าคงคลังบนแพลตฟอร์มเดียวที่กลืนกับบัญชี/การเงิน ลดการ integrate ข้ามระบบ.

**TOR wording to weaponize (ภาษาไทย):**
"ระบบต้องมีชุดบริหารซัพพลายเชน (SCM: demand/supply/inventory planning) ที่รวมอยู่บนแพลตฟอร์มเดียวกับ ERP/Finance โดยไม่ต้องมี landscape หรือ license แยกสำหรับการวางแผน"
(สังเคราะห์จาก standout note: "Oracle SCM Cloud กว้างและรวมในชุดเดียวกับ ERP — ครบกว่าและกลืนกับ Finance"; ชุด Fusion Standout เป็น differentiator ไม่ใช่ TOR spec สำเร็จรูป)

**TOR wording (English):**
"The solution must provide a unified Supply Chain suite (demand/supply/inventory planning) on the same platform as the ERP/Finance, with no separate planning landscape or license."
(Synthesized from the standout differentiator; this row is a Fusion-standout entry, not a verbatim TOR-spec sentence.)

**iCE caveat (over-spec / procurement-fairness):**
Demand planning/SCM Cloud **เกี่ยวข้องต่ำ** กับองค์กรที่ไม่ใช่ผู้ผลิต/กระจายสินค้าเชิงพาณิชย์ขนาดใหญ่. งานคลังโลหิต/เวชภัณฑ์ของ blood-bank/healthcare ใช้ inventory + reorder point + lot/expiry ของ NetSuite ได้ครอบคลุม. จุดอ่อนจริงของ NetSuite คือ Demand Planning ตื้นกว่า Oracle SCM Cloud (พยากรณ์เชิงสถิติพื้นฐาน ไม่มี demand sensing/ML และไม่มี S&OP) — แต่สำหรับภารกิจ non-profit/public-sector ผลกระทบต่ำ. การใช้ "unified SCM suite / no separate license" เป็น TOR mandatory สำหรับองค์กรที่ inventory + reorder point เพียงพอ = over-spec — ให้เก็บเป็นจุดขายเชิง value (one suite, กลืนกับ Finance) มากกว่าเป็นบาร์คัดออก.

**Confidence:** medium
**หลักฐาน / Citation:**
- แหล่งต้นทาง (Gap Pack — Oracle Fusion Standout, Rank 6): differentiator "Oracle SCM Cloud (Demand/Supply/Inventory) กว้างและรวมในชุดเดียวกับ ERP — ครบกว่าและกลืนกับ Finance"; vs NetSuite = "NetSuite Demand Planning ตื้น"; vs SAP = "SAP IBP ดีแต่แยก license/landscape"
- iCE second-opinion: จุดอ่อน NetSuite จริง = Demand Planning ตื้นกว่า Oracle SCM Cloud (ไม่มี demand sensing/ML, ไม่มี S&OP) — ผลต่อ non-profit/healthcare ต่ำ
- (หมายเหตุ: record ชุด Standout นี้ไม่มี KB/เว็บทางการอ้างอิงเฉพาะ — ให้ cross-check กับ GP-FUNC-04/F-SCM-01 ที่มี citation ตรงเรื่อง demand planning)

---

## TOR-SCM-02 — TOR: Warehouse management (WMS) directed operations

- **Capability (TH):** การจัดการคลังสินค้าขั้นสูง (WMS) — ถ้อยคำ TOR สำเร็จรูป
- **Capability (EN):** Advanced Warehouse Management (WMS) — TOR-spec sentence
- **Domain:** SCM (Supply Chain / WMS) · **iCE severity:** กลาง

**Oracle Fusion advantage (Standout):**
นี่คือ **ถ้อยคำ TOR spec ที่ร่างไว้ตรง ๆ** สำหรับหมวด WMS (NetSuite ตอบได้เพียง "Partial"). Differentiator ในต้นทาง: "NetSuite WMS เป็น add-on ตื้น; SAP EWM/Oracle WMS Cloud ลึกกว่า (✔)". Oracle WMS Cloud รองรับ wave/zone/batch picking, directed put-away, RF/barcode และ multi-warehouse/3PL ในระดับ tier-1 ที่ลึกกว่า NetSuite WMS SuiteApp — โดยเฉพาะ 3PL billing เชิงลึกและ slotting optimization. เมื่อขาย Fusion, ให้บรรจุถ้อยคำนี้เพื่อดัน NetSuite ลงเหลือ Partial บนมิติ 3PL/slotting.

**TOR wording to weaponize (ภาษาไทย):**
"ระบบต้องมีการจัดการคลังสินค้าขั้นสูง (WMS) รองรับ wave/zone/batch picking, directed put-away, การทำงานผ่าน RF/barcode และการบริหารหลายคลัง/3PL"

**TOR wording (English):**
"The solution shall provide advanced Warehouse Management (WMS) supporting wave/zone/batch picking, directed put-away, RF/barcode operations, and multi-warehouse/3PL management."

**iCE caveat (over-spec / procurement-fairness):**
การให้ "Partial" ในต้นทาง **ประเมินต่ำกว่าความจริง** สำหรับ requirement ที่ระบุ (wave/zone/batch picking, directed put-away, RF/barcode, multi-warehouse — ทั้งหมดเป็นฟีเจอร์ในตัวของ NetSuite WMS SuiteApp). "Partial" มีมูลบางส่วนเพราะ native WMS วางตำแหน่งปริมาณต่ำ-กลาง และ 3PL billing/slotting optimization ระดับ SAP EWM ยังอ่อนกว่า. สำหรับคลัง cold-chain ของ blood-bank/vaccine-serum production facility ในบริบท healthcare/non-profit (หลายคลัง, lot/expiry, RF, directed put-away คุมอุณหภูมิ) native WMS น่าจะพอ ส่วน 3PL billing แทบไม่เกี่ยว (อยู่นอกภารกิจ). **[ต้อง verify]** ระดับ throughput จริงกับ environment ก่อนสรุป. ระวังการใช้คำว่า "3PL" ใน TOR ถ้าผู้ซื้อไม่ได้ให้บริการคลังแก่บุคคลภายนอก — เข้าข่ายล็อกสเปก.

**Confidence:** medium
**หลักฐาน / Citation:**
- [KB] WMS4-WMS Outbound Fulfillment (0.65) — wave; WMS Advanced Setup (0.60) — zone/batch/RF strategies
- [WEB:netsuite.com] NetSuite WMS product page — directed putaway, RF barcode, multi-location
- [WEB:houseblend.io] NetSuite WMS Optimization: Slotting & Picking — มี slotting/picking strategies (ลึกน้อยกว่ามาตรฐาน enterprise)
- [ความเชื่อมั่น: กลาง]

---

## สรุปเชิงกลยุทธ์ (logistics) / Strategic summary

| record | capability | severity (iCE) | Fusion จุดขายหลัก | over-spec risk |
|---|---|---|---|---|
| F-SCM-01 | Demand/supply planning & S&OP | ต่ำ | S&OP/IBP enterprise | สูง (S&OP = over-spec ถ้าไม่ใช่ผู้ผลิต/กระจายสินค้าใหญ่) |
| F-WMS-01 | Directed warehouse ops (WMS) | กลาง | labor mgmt + slotting tier-1 | กลาง (slotting/labor = over-spec สำหรับคลัง cold-chain เล็ก) |
| F-WMS-02 | Transportation mgmt (TMS) | แทบไม่มีผล | Oracle OTM full TMS | สูงมาก (TMS พาณิชย์ = over-spec สำหรับกระจายในประเทศ) |
| GP-FUNC-04 | Demand planning & forecasting | ต่ำ | demand sensing/ML | สูง (tier-1 forecast = over-spec) |
| GP-FUNC-06 | WMS (wave/zone, RF, 3PL) | กลาง | 3PL billing + slotting | กลาง-สูง (3PL billing = over-spec ถ้าไม่ใช่ 3PL) |
| GP-FUNC-07 | Transportation mgmt (TMS) | แทบไม่มีผล | native TMS in-suite | สูงมาก (over-spec) |
| GP-STANDOUT-06 | SCM Cloud breadth (Fusion standout) | ต่ำ | unified one-suite SCM | สูง (unified SCM mandatory = over-spec) |
| TOR-SCM-02 | WMS directed ops (TOR spec) | กลาง | 3PL/slotting depth | กลาง (คำว่า "3PL" = ล็อกสเปกถ้าไม่ให้บริการคลังภายนอก) |

**ข้อเสนอเชิงจัดซื้อจัดจ้าง (จาก second_opinion):** ในหมวดโลจิสติกส์ จุดที่ Oracle Fusion ชนะจริงและ "ควรพิจารณา" คือความลึกของ WMS (3PL billing/slotting) และ demand planning ระดับ tier-1 — แต่ส่วนใหญ่ (TMS เต็มรูป, S&OP/IBP, slotting/labor ระดับ DC พาณิชย์) เกี่ยวข้องกับผู้ผลิต/กระจายสินค้าเชิงพาณิชย์ขนาดใหญ่ ไม่ใช่ non-profit/healthcare/public-sector. เพื่อความเป็นธรรมและลดความเสี่ยงถูกท้วงติง (สตง./ผู้ยื่นรายอื่น) ควรเขียน requirement แบบ **outcome-based** ตามภารกิจจริง (เช่น "รองรับคลัง cold-chain หลายแห่งพร้อม lot/expiry และ RF") ไม่ผูกกับฟีเจอร์เฉพาะผลิตภัณฑ์ (เช่น "3PL billing native"). ทุกข้อที่ติดป้าย [ต้อง verify] ควรยืนยันกับ environment จริง/ผู้ขายก่อนตัดสินใจ.
