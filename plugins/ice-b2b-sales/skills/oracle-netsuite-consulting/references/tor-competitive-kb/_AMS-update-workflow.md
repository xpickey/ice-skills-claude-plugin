# AMS Yearly Update Workflow — TOR Competitive KB
# ขั้นตอนทบทวนประจำปี — คลังความรู้ TOR เชิงแข่งขัน (สำหรับทีม AMS ของ iCE)

---
kb: "tor-competitive-kb"
purpose: "keep NetSuite-vs-Fusion product positions current; append new TOR gaps; retire closed gaps"
cadence: "yearly (recommended: after each major NetSuite release wave / annually before peak bid season)"
owner: "iCE AMS + Pre-sales / Bid Desk"
audience: "iCE staff only — internal (see _ACCESS.md)"
---

> **ทำไมต้องทบทวนทุกปี.** ตำแหน่งผลิตภัณฑ์เปลี่ยนเร็ว — NetSuite ออกฟีเจอร์ใหม่ทุกไตรมาส และ SuiteApp/first-party
> add-on ปิด gap เดิมเรื่อย ๆ (เช่น NetSuite Account Reconciliation ปิด gap "ไม่มี transaction matching" ในปี 2023).
> เรคคอร์ดที่ไม่ทบทวนจะกลายเป็นข้อมูลเก่าและทำให้ iCE **ยอมรับ gap ที่ปิดไปแล้ว** หรือ **เสนอ counter ที่ล้าสมัย** ในดีลจริง.

---

## 0. ก่อนเริ่ม / Preconditions
- อ่าน `_ACCESS.md` — งานนี้แตะ competitive intelligence ภายใน.
- ยึด anti-hallucination: **ห้ามเพิ่ม gap/ตัวเลข/ชื่อรุ่น/citation ที่ไม่มีหลักฐาน**. ทุกการเปลี่ยนตำแหน่งผลิตภัณฑ์
  ต้องมี citation (Oracle/NetSuite Help, release notes, suiteapp.com, หรือ analyst).
- ยึด client-anonymization: ห้ามเขียนชื่อลูกค้าจริง — ใช้รูปแบบอุตสาหกรรม (healthcare / blood-bank / non-profit /
  public-sector) เท่านั้น.
- ทำงานทีละ vertical file; commit/สรุปการเปลี่ยนแปลงต่อไฟล์.

---

## 1. Re-verify each record's product position / ตรวจตำแหน่งผลิตภัณฑ์รายเรคคอร์ด
สำหรับทุกเรคคอร์ดในไฟล์ vertical:
1. เปิด **Gap** + **Counter** แล้วถามว่า *ยังจริงไหมกับรุ่นปัจจุบัน?* เทียบกับ:
   - NetSuite release notes ปีล่าสุด (ฟีเจอร์ใหม่ที่อาจย้าย gap → native)
   - Oracle/NetSuite Help (docs.oracle.com/…/netsuite) — ยืนยันข้อความที่ยกมา (เช่น "A Workforce module is not
     currently available") ยัง valid หรือถูกยกเลิก
   - suiteapp.com — SuiteApp ที่อ้างยังมี/ยัง certified หรือเปลี่ยนชื่อ/เจ้าของ
   - แหล่ง analyst (ถ้ามี)
2. ปรับ **severity** ถ้าจำเป็น (เช่น first-party ทำให้ native → ลด `สูง`→`กลาง`/`ต่ำ`). อธิบายเหตุผลในเรคคอร์ด.
3. ตรวจ tag `[ต้อง verify]` — ยืนยันแล้วให้ถอด tag หรือคงไว้พร้อมโน้ตว่าเหตุใดยังต้อง verify.

## 2. Update last_verified + confidence / ปรับวันที่ตรวจ + ความเชื่อมั่น
- อัปเดต `last_verified` ใน **frontmatter ของไฟล์** เป็นวันที่ทบทวน (รูปแบบ `YYYY-MM-DD`).
- ปรับ **Confidence** รายเรคคอร์ด: `high` = ยืนยันด้วย official docs/KB มี score · `medium` = documented บางส่วน/ขึ้นกับ
  ตำแหน่งผลิตภัณฑ์ที่ควร verify กับ environment จริง · `low` = ไม่มี citation แข็งในแหล่ง.
- ถ้าเรคคอร์ดไม่มี citation เลย → confidence ต้องไม่เกิน `low` (anti-hallucination).

## 3. Append new records / เพิ่มเรคคอร์ดใหม่
- เมื่อพบ gap ใหม่จาก TOR/ดีลจริง หรือ 3-way gap ใหม่ → เพิ่มใต้ **vertical ที่ถูกต้อง** (และซ้ำใน `cross-cutting.md`
  ถ้าเป็น platform/technical/standout ที่มีน้ำหนักหลาย vertical).
- ตั้ง **ID ใหม่** ต่อจากซีรีส์เดิมให้ไม่ชน (`F-*`/`NF-*` = TOR bank · `GP-FUNC/TECH/STANDOUT-*` = gap pack · `TOR-*` =
  TOR spec). ID เดียวกันที่ปรากฏหลาย vertical ต้องมี severity/เนื้อหาตรงกันทุกไฟล์.
- ถ้าเป็น vertical ที่ **ยังไม่มีไฟล์** (ปัจจุบัน: `telco`, `retail-distribution`, `hospitality`) → สร้างไฟล์ใหม่
  `by-industry/<vertical>.md` โดยคัดลอก frontmatter + how-to-use header จากไฟล์ที่มีอยู่ แล้วเริ่มเรคคอร์ดแรก.
- หลังเพิ่ม → อัปเดต **index table + total_records + verticals_covered** ใน `README.md`.

## 4. Flag closed gaps / ทำเครื่องหมาย gap ที่ถูกปิดแล้ว
- **อย่าลบเรคคอร์ด** — เก็บไว้เป็นประวัติและกันการอ้าง gap เดิมซ้ำ.
- เมื่อผลิตภัณฑ์ปิด gap แล้ว → ใส่ป้าย `**gap closed YYYY**` ที่หัวเรคคอร์ด + โน้ตสั้นว่าปิดด้วยฟีเจอร์/รุ่นใด +
  citation, แล้วลด severity ตามจริง. ตัวอย่างเดิมที่ควรใช้เป็นแบบ: F-EPM-03 (close orchestration) ถูกปิดโดย
  **NetSuite Account Reconciliation ออกปี 2023 บน Oracle Fusion EPM** — คงเรคคอร์ดไว้แต่เปลี่ยนกรอบจาก "ทำไม่ได้" เป็น
  "ปิดด้วย add-on (มีค่าลิขสิทธิ์)".
- ถ้า gap ปิดจน severity เหลือ `แทบไม่มีผล` → คงไว้พร้อมป้าย closed เพื่อเตือนทีมว่า **อย่าใส่ข้อนี้ใน TOR อีก**
  (กลายเป็น spec-lock ที่ปิดไปแล้ว).

## 5. Consistency & sign-off / ปิดงาน
- ตรวจว่า severity/เนื้อหาของ ID เดียวกันตรงกันข้าม vertical files (ID ปรากฏหลายไฟล์).
- ตรวจ client-anonymization ทั้งไฟล์ (ห้ามมีชื่อลูกค้าจริง).
- อัปเดต `README.md` index (records, severity breakdown, total, verticals_covered) ให้ตรงกับไฟล์จริง.
- บันทึกผู้ทบทวน + วันที่ในสรุปการเปลี่ยนแปลง (changelog ท้ายไฟล์ vertical หรือ commit note).

---

## Template — เรคคอร์ดใหม่ / New record template
คัดลอกบล็อกนี้ไปวางใต้ vertical ที่ถูกต้อง แล้วเติมค่า. รักษาลำดับฟิลด์ให้เหมือนเรคคอร์ดเดิมทุกไฟล์.

```markdown
## <ID> — <Capability TH> / <Capability EN>

- **Capability (TH):** <ความสามารถ ภาษาไทย + ขอบเขตย่อ>
- **Capability (EN):** <capability in English + short scope>
- **Domain:** <EPM|Finance|SCM|Manufacturing|Procurement|Project|Asset|HCM|Quality|GRC|ESG|Order Mgmt|Service|Technical>
  · **iCE severity:** <สูง (High) | กลาง (Medium) | ต่ำ (Low) | แทบไม่มีผล (Negligible)>

**จุดที่ NetSuite สู้ไม่ได้ (Gap):**
<มุมที่ TOR เชิงแข่งขันกล่าวอ้าง — ระบุสิ่งที่ NetSuite ขาดจริง แยกจากข้ออ้างที่เกินจริง>

**Counter / Mitigation:**
- **Rebuttal to overclaim:** <ข้ออ้างใดเกินจริง + ข้อเท็จจริงที่ถูกต้อง>
- **First-party / SuiteApp path:** <NSPB / NSAR / NSAW / NSPCM / SuiteApp certified — ปิด gap อย่างไร, add-on แยกลิขสิทธิ์ไหม>
- **Over-spec rebuttal (<vertical> context):** <เมื่อใดเป็น over-spec สำหรับองค์กรลักษณะนี้>

**Procurement caveat:**
<ทำไมการล็อกสเปกข้อนี้เสี่ยงถูกท้วง (สตง./ผู้ยื่นรายอื่น); แนะ outcome-based wording แทน>

**Confidence:** <high | medium | low>   <!-- low ถ้าไม่มี citation แข็ง -->

**หลักฐาน / Citation:**
- [KB] <doc> (<theme>, <score>) — <สาระ>
- [WEB:docs.oracle.com] <หัวข้อ Help + ข้อความยกมา> (<article id> — ตรวจแล้ว/ต้อง verify)
- [WEB:suiteapp.com] <SuiteApp> — <ยืนยันอะไร>

<!-- ถ้า gap ถูกปิดแล้ว ให้ใส่ป้ายที่หัวเรคคอร์ด: **gap closed YYYY** + ปิดด้วยฟีเจอร์/รุ่น + citation -->

---
```

**หมายเหตุ severity mapping (สงวนจากต้นฉบับ):**
`สูง` = จุดอ่อนจริง กระทบภารกิจหลัก ต้องปิดก่อน go-live ·
`กลาง` = จริง กระทบบางหน่วย ปิดด้วย SuiteApp/custom ต้นทุนจัดการได้ ·
`ต่ำ` = เล็กน้อย native/workaround พอ ·
`แทบไม่มีผล` = ช่องว่างตามสเปกแต่แทบไม่มี use case (over-spec / spec-lock — เตือนอย่าใส่ TOR).

---

## Backlog — improvements deferred from 2026-06-29 team review / รายการปรับปรุงที่เลื่อนไว้

รายการเหล่านี้ผ่านการ review แล้วว่า **ไม่ block การใช้งาน** (should/nice-to-have) — ทำในรอบ AMS ถัดไป:

- **[SHOULD] SoD/duplicate-record canonical pointer** — `cross-cutting.md` เก็บ SoD เป็นหลายเรคคอร์ดใกล้เคียง (NF-SEC-01 / GP-FUNC-27 / GP-TECH-11) และ F-WMS-01/GP-FUNC-06, F-MFG-01/GP-FUNC-01 ก็ซ้ำ. เพิ่มบรรทัด "CANONICAL: weaponize จาก <ID หลัก>; ตัวอื่น = cross-cut view" ที่หัวแต่ละคลัสเตอร์ กันเผลอ paste 2 เวอร์ชันที่ caveat ต่างกันลงบิดเดียว.
- **[NICE] energy-utilities.md** — ตรวจชื่อ/สะกด vendor ที่ถูกซื้อ (Next Technik vs product NextService) + วันที่ acquisition กับ oracle.com ก่อนใช้ในดีลจริง (claim อิง [WEB] นอก 3 source-of-truth files).
- **[NICE] education / healthcare HCM records** — เพิ่ม note ว่า SuitePeople Performance native + LMS/succession gap มาจาก NetSuite KB ไม่ใช่ gap_pack (ครอบเฉพาะ 27 Finance/SCM). รอบ AMS ให้ re-verify HCM กับ NetSuite Help โดยตรง.
- **[NICE] per-record "safe-to-lift" flag** — เพิ่มป้าย HONEST-KNOCKOUT vs CREDIBILITY-DIFFERENTIATOR-DO-NOT-LOCK ต่อเรคคอร์ด กัน junior rep อ่าน severity ต่ำแล้ว lock spec ผิด.
