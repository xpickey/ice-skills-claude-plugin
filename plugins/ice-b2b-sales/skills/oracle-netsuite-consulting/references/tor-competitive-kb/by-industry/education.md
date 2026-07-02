# TOR Competitive KB — education — NetSuite Weakness & Counter

---
last_verified: "2026-06-29"
source: "TOR Requirement Bank + Gap Pack v2"
confidence_note: "Records inherit the confidence tag from each source record ([ความเชื่อมั่น: สูง/กลาง]). All product positions are mid-2026 standard positioning; items marked [ต้อง verify] must be confirmed against a live environment/vendor before a bid commitment. Source data is a COMPETITIVE TOR draft deliberately biased so NetSuite scores Partial/No and Oracle Fusion scores Fully — this KB preserves both the gap AND the iCE counter-view for balanced use. บริบท education มาจากมิติบุคลากร/การเรียนรู้ (talent, LMS, performance) ที่ทับกับงานฝึกอบรม/พัฒนาบุคลากรของสถาบันการศึกษาและองค์กรที่มีภารกิจ learning."
ams_review: "yearly — re-verify product positions"
---

> **วิธีใช้ / How to use.** ไฟล์นี้ใช้เมื่อ iCE **ขาย NetSuite** หรือ **ตั้งรับ (defend)** จาก TOR ที่เอียงไปทาง Oracle Fusion ในกลุ่มงานที่แตะมิติ **education / การพัฒนาบุคลากร / การเรียนรู้ (learning & talent)**. แต่ละหัวข้อให้ทั้ง (1) จุดที่ NetSuite เสียเปรียบจริง และ (2) แนวตั้งรับ — ปิดด้วย first-party add-on, certified SuiteApp, custom หรือข้อโต้แย้ง "over-spec".
>
> **บริบทลูกค้า (generalized).** แหล่งข้อมูลอ้างองค์กรลักษณะ **healthcare / blood-bank / non-profit foundation / public-sector** (นิติบุคคลเดียวในไทย งานสาธารณกุศล มี รพ./ศูนย์บริการ/หน่วยผลิตชีววัตถุ และบุคลากรจำนวนมากที่ต้องพัฒนา/อบรม/ประเมินผลงาน) — ใช้ pattern นี้แทนชื่อลูกค้าเสมอ. ในมิติ education/learning ประเด็นสำคัญคือ **การบริหารผลงาน (performance) และการเรียนรู้/อบรม (learning/LMS) ของบุคลากร** ไม่ใช่ระบบบริหารสถาบันการศึกษา (SIS) เชิงพาณิชย์ — จุดนี้คือแกนของข้อโต้แย้ง over-spec ในไฟล์นี้.
>
> **Procurement note (สตง.).** การเขียน requirement ให้ผูกกับสถาปัตยกรรมเฉพาะผลิตภัณฑ์ (เช่น "Talent suite ครบวงจร recruiting/performance/learning/succession บน data model เดียวใน ERP") เป็นการล็อกสเปกที่เสี่ยงถูกท้วงติงจากสำนักงานการตรวจเงินแผ่นดิน (สตง.) และผู้ยื่นรายอื่น — เพราะเกณฑ์ "single data model" ถูกออกแบบมาเพื่อตี suite ที่เป็นหลายคลาวด์ (เช่น SuccessFactors) โดยเฉพาะ. ควรเขียนแบบ **outcome-based** ตามภารกิจจริง (พัฒนา/ประเมิน/อบรมบุคลากร) และเปิดทางให้ต่อเชื่อมระบบเฉพาะทาง (best-of-breed) ได้.

---

## GP-FUNC-19 — Talent: Performance, Learning, Recruiting

**Capability (TH):** ชุดบริหารบุคลากร (Talent) — บริหารผลงาน / การเรียนรู้ / การสรรหา
**Capability (EN):** Talent: performance, learning, recruiting

**Domain + iCE severity:** HCM · **ต่ำ (Low)**

**จุดที่ NetSuite สู้ไม่ได้ (Gap):**
Gap Pack ให้คะแนน NetSuite = 1 ★ (เทียบ Oracle Fusion 5 ★★★★★ และ SAP S/4HANA 5 ★★★★★) จัด Gap Severity = Critical โดยระบุเหตุผลว่า "NetSuite แทบไม่มี talent suite; Oracle HCM (Gartner Leader) & SuccessFactors ครบ". กล่าวคือ ในมุมของ TOR ต้นทาง NetSuite ถูกวางว่าไม่มีชุด talent ครบวงจร (recruiting/performance/learning) เทียบชั้น Oracle HCM หรือ SuccessFactors.

**Counter / Mitigation:**
ข้อความ "แทบไม่มี talent suite" **เกินจริง**. SuitePeople มี **Performance Management เนทีฟ** (goals, reviews, check-in, Kudos) บน data model เดียวกับ Core HR — ยืนยันจาก KB — จึงไม่ใช่ "แทบไม่มี". ส่วน recruiting มีเพียงพื้นฐาน (Job Requisition record + บันเดิล Recruiting Reports) ซึ่ง **ไม่ใช่ ATS เต็มรูป**.

**Gap จริงที่เหลือ** คือ (1) **ไม่มี Learning/LMS เนทีฟ** และ (2) recruiting/ATS เต็มรูปและ succession ยังไม่มีในตัว — ต้องต่อระบบเฉพาะทางภายนอก (เช่น Greenhouse, Lever สำหรับ ATS; หรือ LMS best-of-breed) ผ่าน API. นี่คือแนวที่องค์กรทั่วไปมักเลือกอยู่แล้ว: เลือกระบบ learning/recruiting เฉพาะทางต่อเชื่อม ไม่จำเป็นต้องฝังใน ERP.

**Over-spec rebuttal:** สำหรับ pattern healthcare/public-sector/non-profit งาน performance และ learning พื้นฐานของบุคลากร รพ./หน่วยงานใช้ของเนทีฟ (Performance Management) ได้ ส่วน talent suite ครบวงจร (ATS/LMS/succession ระดับองค์กร) แทบไม่มี use case จริงในองค์กรการกุศล — การบังคับใน TOR จึงเป็น over-spec. ในบริบท **education/learning** โดยเฉพาะ ถ้าเน้น LMS จริงจัง แนวทางที่ถูกต้องทางเทคนิคและทางจัดซื้อคือ **ต่อเชื่อม LMS เฉพาะทาง** (best-of-breed) เข้ากับ Core HR ของ SuitePeople มากกว่าเรียกร้อง LMS ฝังใน ERP.

**Procurement caveat:**
เกณฑ์ "talent suite ครบวงจรบน data model เดียวใน ERP" เป็นการล็อกสเปกไปทาง Oracle HCM — เสี่ยงข้อท้วงติง สตง. ควรเขียนเป็นผลลัพธ์ (ตั้ง/ติดตามเป้าผลงาน + จัดอบรม/บันทึกการเรียนรู้ของบุคลากร) และเปิดให้ใช้สถาปัตยกรรมต่อเชื่อม (integration) กับระบบ learning/recruiting เฉพาะทางได้ ไม่ผูกว่าต้องเป็นโมดูลใน ERP เดียว.

**Confidence:** high

**หลักฐาน / Citation:**
- [WEB:netsuite.com] SuitePeople Performance Management (product page)
- [KB] Netsuite-Administrator Guide — Performance Management (SuitePeople HR), Kudos (0.5788)
- [KB] Netsuite-Employee Management — Recruiting Reports bundle/Job Requisition (0.4987; เป็นแค่ recruiting พื้นฐาน ไม่ใช่ ATS)

---

## TOR-HCM-02 — TOR: Talent Management (Performance / Learning / Recruiting / Succession)

**Capability (TH):** ชุดบริหารบุคลากร (Talent) ครบวงจร: สรรหา (recruiting), บริหารผลงาน (performance), การเรียนรู้ (learning) และการวางแผนสืบทอดตำแหน่ง (succession) บน data model เดียวกับ Core HR
**Capability (EN):** End-to-end Talent suite — recruiting, performance, learning, and succession — on the same data model as Core HR

**Domain + iCE severity:** HCM · **ต่ำ (Low)**

**จุดที่ NetSuite สู้ไม่ได้ (Gap):**
ข้อกำหนด TOR (Type: Functional, Priority: Important) ระบุว่าระบบต้องมี Talent suite ครบวงจร (recruiting/performance/learning/succession) บน data model เดียวกับ Core HR และตัดสิน "NetSuite ตอบได้? = No". Differentiator note ของ TOR ระบุ "Oracle HCM รวมศูนย์ data model เดียว ✔✔ / SuccessFactors เป็นหลายคลาวด์รวม; NetSuite ไม่มี".

**Counter / Mitigation:**
คำตอบ "No" ทั้งข้อ **ไม่ถูกต้องนัก**. SuitePeople มี **Performance Management เนทีฟบน data model เดียวกับ Core HR อยู่แล้ว** — จึงผ่านเกณฑ์ "single data model" สำหรับ performance ด้วยซ้ำ (เกณฑ์ "data model เดียว" นี้แท้จริงออกแบบมาเพื่อตี SuccessFactors ที่เป็นหลายคลาวด์รวม ไม่ใช่ตี NetSuite).

**Gap จริงที่เหลือ** คือ recruiting/ATS มีเพียงพื้นฐาน, **learning/LMS ไม่มีเนทีฟ** และ **succession planning ไม่มีเนทีฟ** — ต้องใช้ third-party ต่อเชื่อม. Performance Management ยังคงเป็น native บน data model เดียวกับ Core HR ตามที่ยืนยันจาก KB.

**Over-spec rebuttal:** งาน performance (และ Core HR) ที่ใช้จริงของ pattern healthcare/public-sector/non-profit รองรับ native ได้ ส่วนชุด talent ครบวงจร (ATS/LMS/succession) ค่อนข้าง over-spec สำหรับองค์กรการกุศล — เลือกต่อเชื่อมเฉพาะโมดูลที่จำเป็นได้. ในมิติ **education/learning** ที่โฟกัส LMS/การพัฒนาบุคลากร แนวทางต่อเชื่อม LMS เฉพาะทางเข้ากับ Core HR ให้ผลลัพธ์ที่ตรงความต้องการมากกว่าและคุ้มค่ากว่าการยัด suite เต็มรูปที่ไม่ได้ใช้.

**Procurement caveat:**
เกณฑ์บังคับ "Talent suite ครบวงจรบน data model เดียว" ถูกวางมาเพื่อตัดผู้เสนอที่ใช้สถาปัตยกรรม best-of-breed/หลายคลาวด์ (รวมถึง SuccessFactors) — เป็นการล็อกสเปกที่เสี่ยงถูกท้วงติงจาก สตง. และผู้ยื่นรายอื่น. ควรเขียน requirement แบบ outcome-based (บริหารผลงาน + จัดการเรียนรู้/อบรม + วางแผนสืบทอดตำแหน่งตามความจำเป็นจริง) และอนุญาตให้ใช้การต่อเชื่อมระบบเฉพาะทางได้ ไม่บังคับว่าต้องเป็นโมดูลเดียวใน data model เดียว.

**Confidence:** high

**หลักฐาน / Citation:**
- [WEB:netsuite.com] SuitePeople Performance Management (product page)
- [KB] Netsuite-Administrator Guide — Performance Management (SuitePeople HR), Kudos (0.5788)

---

## หมายเหตุมุมกว้าง / Cross-record note (education vertical)

ทั้งสองรายการในไฟล์นี้ (GP-FUNC-19 และ TOR-HCM-02) เป็นมุมมองซ้ำของ **capability เดียวกัน** (Talent: performance/learning/recruiting/succession) จากคนละแหล่ง (Gap Pack functional vs TOR spec) และทั้งคู่มี **iCE severity = ต่ำ (Low)** ตรงกัน. ข้อสรุปตั้งรับที่สอดคล้องกันสำหรับมิติ education/learning:

- **จุดที่ยอมรับตรง ๆ (concede):** NetSuite/SuitePeople **ไม่มี LMS เนทีฟ** และ **ไม่มี succession planning เนทีฟ**; recruiting เป็นเพียงพื้นฐาน ไม่ใช่ ATS เต็มรูป.
- **จุดที่ต้องแก้ข้อกล่าวอ้าง (reframe):** **Performance Management เป็น native บน data model เดียวกับ Core HR** — ดังนั้นคะแนน "1★" หรือคำตอบ "No" ทั้งข้อในแหล่งต้นทางเกินจริง.
- **แนวปิด gap (mitigation):** ต่อเชื่อม LMS / ATS เฉพาะทาง (best-of-breed) ผ่าน API เข้ากับ SuitePeople Core HR — เป็นสถาปัตยกรรมที่องค์กรส่วนใหญ่เลือกอยู่แล้ว และเหมาะกับงาน learning/education มากกว่าการฝังทุกอย่างใน ERP.
- **แนวจัดซื้อ (procurement):** ผลักดันให้ requirement เขียนแบบ outcome-based และเปิดทาง integration เพื่อลดความเสี่ยงล็อกสเปก/ข้อท้วงติง สตง.
