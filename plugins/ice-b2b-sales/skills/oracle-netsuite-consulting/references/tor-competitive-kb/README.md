# TOR Competitive KB — NetSuite Weakness & Counter (iCE Internal)
# คลังความรู้ TOR เชิงแข่งขัน — จุดอ่อน NetSuite และแนวตอบโต้ (สำหรับ iCE ภายในเท่านั้น)

---
kb: "tor-competitive-kb"
owner: "iCE Consulting — Pre-sales / Bid Desk"
audience: "iCE staff only (internal competitive intelligence)"
last_verified: "2026-06-29"
source: "TOR Requirement Bank + 3-way Gap Pack (NetSuite vs Oracle Fusion vs SAP S/4HANA) v2"
ams_review: "yearly — see _AMS-update-workflow.md"
access: "INTERNAL — see _ACCESS.md before any customer-facing reuse"
verticals_covered: 9        # of the 11 iCE verticals (telco, retail-distribution, hospitality not yet populated)
total_records: 171          # record-views across files; underlying unique requirements = 101 ids (many appear in >1 vertical)
---

> **อ่านก่อนใช้ / Read first.** เอกสารชุดนี้เป็น **competitive intelligence ภายในของ iCE** ที่วิเคราะห์ตำแหน่ง
> ผลิตภัณฑ์ NetSuite เทียบ Oracle Fusion (และ SAP S/4HANA บางส่วน) ในบริบทการร่าง/ตอบ TOR. **ห้ามคัดลอกเนื้อหา
> ดิบ (จุดอ่อนคู่แข่ง / คำวิจารณ์ผลิตภัณฑ์) ลงเอกสารที่ลูกค้าเห็นโดยตรง** — ใช้ได้เฉพาะ *ถ้อยคำ TOR ที่แปลงเป็น
> กลาง อิงผลลัพธ์แล้ว* เท่านั้น (ดู `_ACCESS.md`). This is **iCE-internal** material; the customer sees only the
> derived, neutral, outcome-based TOR wording — never the competitor-weakness analysis itself.

---

## 1. What this KB is / KB นี้คืออะไร

**EN.** A structured, per-vertical knowledge base of every place a Fusion-biased TOR frames **NetSuite as
weak against Oracle Fusion** — together with the **honest iCE counter-view** for each. The underlying dataset
is a *competitive TOR draft* that was deliberately built so NetSuite scores Partial/No and Oracle Fusion scores
Fully. This KB re-processes that draft into a form iCE can actually use on both sides of a deal:

- **Sell-side (iCE sells NetSuite).** When iCE is the NetSuite bidder, each record shows the honest gap, the
  first-party or SuiteApp mitigation path, and whether the requirement is over-spec — so iCE can respond
  truthfully without conceding a false "No".
- **Shape-side (iCE shapes a TOR toward Oracle/NetSuite fit).** Each record carries suggested TOR wording, but
  every record also carries the **procurement-fairness caveat**: locking a spec to one product's feature invites a
  สตง. / competing-bidder challenge. Outcome-based wording is the safe path.

**TH.** คลังความรู้แยกตามอุตสาหกรรม (per-vertical) ที่รวบรวมทุกจุดที่ TOR (ซึ่งเอนเอียงไปทาง Oracle Fusion) กล่าวว่า
**NetSuite สู้ Oracle Fusion ไม่ได้** — พร้อม **ความเห็นตั้งรับที่ซื่อตรงของ iCE** ทุกข้อ. ชุดข้อมูลต้นทางเป็น "ร่าง TOR
เชิงแข่งขัน" ที่ออกแบบให้ NetSuite ตอบได้แค่ Partial/No และ Oracle Fusion ตอบ Fully จึง **ไม่ใช่การวิเคราะห์ความต้องการ
ที่เป็นกลาง** — KB นี้แปลงมันให้ iCE ใช้ได้จริงทั้งสองด้าน (ขาย NetSuite และ shape TOR).

### หลักการสมดุล (Balanced — non-negotiable)
ทุกเรคคอร์ดเก็บ **ทั้ง gap และ counter** เสมอ. iCE counter-view สรุปได้ 3 แกน:
1. **ปิดได้ด้วย NetSuite first-party add-on** — NSPB (= เอนจิน Oracle PBCS/Hyperion), NetSuite Account Reconciliation
   (= Oracle Fusion EPM), NSAW (= Oracle ADW + Analytics Cloud), NSPCM (= สาย Oracle PCMCS) — หลายเกณฑ์ตัด NetSuite
   ด้วยมาตรฐานที่ Oracle Fusion เองก็ต้องซื้อโมดูลแยกเหมือนกัน.
2. **Over-spec / ไม่มี use case จริง** — ความสามารถระดับโรงงาน/ข้ามชาติ (process mfg เต็มรูป, APS, S&OP/IBP, global
   payroll หลายประเทศ, TMS, global trade, MDM, EAM) ส่วนใหญ่ไม่เกี่ยวกับองค์กรนิติบุคคลเดียวในไทย / องค์กรสาธารณกุศล /
   หน่วยงานภาครัฐ.
3. **Procurement risk** — การล็อกสเปกกับฟีเจอร์เฉพาะผลิตภัณฑ์เดียวเสี่ยงถูกท้วง (สตง. / ผู้ยื่นรายอื่น) — เขียน
   requirement แบบ outcome-based ตามภารกิจจริง.

### หมายเหตุการปกปิดชื่อลูกค้า (client anonymization)
ต้นฉบับอ้างถึงลูกค้าเฉพาะราย — ในทุกไฟล์ KB ได้ **generalize เป็นรูปแบบอุตสาหกรรม** แล้ว (healthcare / blood-bank /
non-profit foundation / public-sector). **ห้ามเขียนชื่อลูกค้าจริงกลับเข้าไปในไฟล์ KB ใด ๆ.**

---

## 2. How it's organized / โครงสร้าง

```
references/tor-competitive-kb/
├── README.md                 ← ไฟล์นี้ (ภาพรวม + index + how-to-query)
├── _ACCESS.md                ← กติกาการเข้าถึง + procurement-fairness (อ่านก่อน reuse)
├── _AMS-update-workflow.md   ← workflow ทบทวนประจำปี + template เรคคอร์ดใหม่
└── by-industry/              ← 9 ไฟล์ ตาม iCE vertical (1 vertical = 1 ไฟล์)
    ├── bfsi-fintech.md
    ├── cross-cutting.md
    ├── education.md
    ├── energy-utilities.md
    ├── healthcare-public-sector.md
    ├── logistics.md
    ├── manufacturing.md
    ├── public-sector-govt.md
    └── trading-services.md
```

**Taxonomy = 11 iCE verticals.** `by-industry/` เก็บ 1 ไฟล์ต่อ vertical. หนึ่ง requirement อาจปรากฏในหลาย vertical
(เช่น GRC/SoD, data residency เป็น cross-cutting) — จึงเก็บซ้ำในไฟล์ที่เกี่ยวข้อง เพื่อให้ **เปิดไฟล์เดียวจบต่อ 1 ดีล**.
ด้วยเหตุนี้ยอดรวม record-view (171) จึงมากกว่าจำนวน requirement จริง (101 ids ไม่ซ้ำ).

**Record anatomy (แต่ละเรคคอร์ด).** `## <ID> — <capability TH/EN>` → Capability (TH/EN) · Domain · **iCE severity** →
**Gap** (มุมที่ TOR เชิงแข่งขันกล่าวอ้าง) → **Counter / Mitigation** (first-party / SuiteApp / over-spec rebuttal) →
**Procurement caveat** → **Confidence** → **Citation** (KB score / Oracle-NetSuite Help / suiteapp.com / analyst).
`ID` prefix บอกแหล่ง: `F-*`/`NF-*` = TOR Requirement Bank · `GP-FUNC/TECH/STANDOUT-*` = 3-way Gap Pack · `TOR-*` = Gap-Pack TOR spec.

**iCE severity (สงวนจากต้นฉบับ, 4 ระดับ).**
`สูง` = จุดอ่อนจริง กระทบภารกิจหลัก ต้องปิด gap ก่อน go-live ·
`กลาง` = จุดอ่อนจริง กระทบบางหน่วย ปิดได้ด้วย SuiteApp/custom ต้นทุนจัดการได้ ·
`ต่ำ` = จุดอ่อนเล็กน้อย NetSuite native/workaround ครอบคลุมงานจริง ·
`แทบไม่มีผล` = ช่องว่างตามสเปกแต่แทบไม่มี use case (over-spec / spec-lock).

---

## 3. Index of by-industry files / สารบัญไฟล์ (verified 2026-06-29)

จำนวนเรคคอร์ดและ severity ด้านล่างนับจริงจากไฟล์ (join กับ mapping — ตรวจแล้วครบ ไม่มี id ตกหล่น).

| Vertical file | Records | Severity breakdown (สูง / กลาง / ต่ำ / แทบไม่มีผล) | Top severities & notes |
|---|---:|---|---|
| `by-industry/healthcare-public-sector.md` | **42** | 16 / 14 / 12 / 0 | **สูงสุด (16 สูง)** — process/GMP mfg, QMS, data residency, SoD, EAM, PPM/grants. ไฟล์แกนกลางของ dataset. |
| `by-industry/cross-cutting.md` | **55** | 11 / 5 / 20 / 19 | ไฟล์ใหญ่สุด — platform/technical + Fusion "standout" ทั้งชุด. severity เอียงไป ต่ำ/แทบไม่มีผล (ส่วนใหญ่ over-spec/coverable). |
| `by-industry/public-sector-govt.md` | **19** | 11 / 2 / 4 / 2 | เข้มข้น **11 สูง** — GRC/SoD, data residency/sovereignty, statutory tax/e-invoicing, PPM/grants, sourcing. |
| `by-industry/manufacturing.md` | **16** | 5 / 2 / 6 / 3 | process/mixed-mode mfg + QMS = สูง; APS/ETO = แทบไม่มีผล (over-spec นอกงานผลิตซับซ้อน). |
| `by-industry/trading-services.md` | **14** | 1 / 2 / 4 / 7 | severity อ่อนสุด — 7 แทบไม่มีผล (TMS/global trade/CPQ over-spec); sourcing/SLM/CLM คือแกนจริง. |
| `by-industry/bfsi-fintech.md` | **12** | 4 / 3 / 1 / 4 | 4 สูง = GRC/SoD + controls ในบริบทกำกับ/ตรวจ (สตง.); consolidation/treasury มัก over-spec สำหรับนิติบุคคลเดียว. |
| `by-industry/logistics.md` | **8** | 0 / 3 / 3 / 2 | WMS directed ops = กลาง; TMS/global trade = แทบไม่มีผล. ไม่มีเรคคอร์ด สูง. |
| `by-industry/energy-utilities.md` | **3** | 0 / 2 / 0 / 1 | EAM/maintenance = กลาง; ESG = แทบไม่มีผล. ชุดเล็ก. |
| `by-industry/education.md` | **2** | 0 / 0 / 2 / 0 | Talent/learning (2 มุมของ capability เดียว) severity ต่ำ ทั้งคู่. ชุดเล็กสุด. |
| **รวม / Total** | **171** | 48 / 45 / 62 / 58 | 9 ไฟล์ · unique requirement 101 ids |

**Verticals ที่ยังไม่มีไฟล์ (3 จาก 11):** `telco`, `retail-distribution`, `hospitality` — ไม่มี requirement ใน dataset
ต้นทางที่ map มาที่ vertical เหล่านี้ จึงยังไม่สร้างไฟล์. เมื่อมี TOR ของ vertical เหล่านี้เข้ามา ให้สร้างไฟล์ใหม่ตาม
`_AMS-update-workflow.md`.

---

## 4. How to query / วิธีใช้งานจริงในงาน TOR หรือ Proposal

**กฎทอง: เปิด "ไฟล์ vertical ของดีล" + `cross-cutting.md` เสมอ.** เรคคอร์ด platform/technical (SoD, data residency,
iPaaS, analytics, AI, MDM, throughput) อยู่ใน `cross-cutting.md` และมีน้ำหนักในเกือบทุกดีล.

| ถ้างานคือ… | เปิดไฟล์ |
|---|---|
| TOR/proposal โรงพยาบาล / ศูนย์โลหิต / มูลนิธิ / องค์กรสาธารณกุศล | `by-industry/healthcare-public-sector.md` + `cross-cutting.md` |
| TOR หน่วยงานราชการ / รัฐวิสาหกิจ (e-GP, สตง.) | `by-industry/public-sector-govt.md` + `cross-cutting.md` |
| ธนาคาร / ประกัน / FinTech (บริบทกำกับ + ตรวจสอบ) | `by-industry/bfsi-fintech.md` + `cross-cutting.md` |
| ผู้ผลิต (โดยเฉพาะ process/GMP/mixed-mode) | `by-industry/manufacturing.md` + `cross-cutting.md` |
| เทรดดิ้ง / จัดจำหน่าย / บริการ (sourcing/CLM) | `by-industry/trading-services.md` + `cross-cutting.md` |
| โลจิสติกส์ / คลังสินค้า / กระจายสินค้า | `by-industry/logistics.md` + `cross-cutting.md` |
| พลังงาน / สาธารณูปโภค (EAM/ESG) | `by-industry/energy-utilities.md` + `cross-cutting.md` |
| การศึกษา / สถาบัน (talent/learning) | `by-industry/education.md` + `cross-cutting.md` |
| ล้วน ๆ เชิงเทคนิค/แพลตฟอร์ม (architecture, security, AI) | `cross-cutting.md` |
| telco / retail-distribution / hospitality | ยังไม่มีไฟล์ → ใช้ `cross-cutting.md` + vertical ใกล้เคียง แล้วสร้างไฟล์ใหม่ (ดู AMS workflow) |

**Workflow ต่อ 1 requirement:**
1. **อ่าน iCE severity ก่อน.** `แทบไม่มีผล`/`ต่ำ` → มัก over-spec: อย่ายอมรับเป็น "No", ชี้ counter/first-party path.
   `สูง`/`กลาง` → gap จริง: วางแผนปิดด้วย add-on/SuiteApp/custom และตั้งงบ TCO.
2. **ใช้ Gap + Counter ประกอบคำตอบ** — sell-side: ตอบตรงด้วย counter + mitigation. shape-side: ใช้ suggested wording
   *เฉพาะหลังแปลงเป็น outcome-based* ตาม `_ACCESS.md`.
3. **เช็ก Confidence + Citation.** ข้อ `[ต้อง verify]` หรือ confidence ต่ำ ต้องยืนยันกับ environment จริง/ผู้ขายก่อนใช้ในดีล.
4. **บังคับ procurement caveat.** ก่อนเสนอ wording ที่ล็อกฟีเจอร์ ให้ทวนว่าองค์กรมี use case จริงหรือไม่ — ถ้าไม่มี
   = spec-lock เสี่ยงถูกท้วง.

**เชื่อมกับ agent/skill:** ใช้ร่วมกับ skill `competitor-objection-bank` (แนวตอบโต้ข้อโต้แย้ง) และ agent **เทพ**
(solution-knowledge, fit-gap) / **ยอดนักขาย** (sales-process, TOR). KB นี้ = แหล่งข้อเท็จจริง; agent = ผู้เรียบเรียง.

**🔗 KB คู่ (มุมตรงข้าม — requirement ID เดียวกัน):** ไฟล์นี้คือ **มุม NetSuite (จุดอ่อน + counter/ป้องกัน)**. สำหรับ
**มุม Oracle Fusion (จุดแข็ง + weaponize TOR wording)** ของ requirement ID เดียวกัน (F-EPM-01, GP-FUNC-27 ฯลฯ ใช้ ID ร่วมกันทั้งสอง KB)
→ เปิด `oracle-cloud-applications-consulting/references/tor-competitive-kb/by-industry/<vertical>.md`. ดึง **attack + defense ของ ID เดียวในทีเดียว**:
Fusion-side = วิธี spec ให้ NetSuite ตก · NetSuite-side (ไฟล์นี้) = วิธีตอบโต้/ปิด gap. เลือกใช้ตามว่ากำลังขาย product ตัวไหน.

---

## 5. Provenance & limits / ที่มาและข้อจำกัด
- **ที่มา:** TOR Requirement Bank (27 ข้อ NetSuite vs Oracle Fusion) + 3-way Gap Pack (functional / technical /
  Fusion standout / TOR spec: NetSuite vs Oracle Fusion vs SAP S/4HANA). ตรวจกับ NetSuite KB (Qdrant),
  Oracle/NetSuite Help, suiteapp.com, และแหล่งนักวิเคราะห์.
- **จุดเวลา:** ตำแหน่งผลิตภัณฑ์เป็นค่ากลางปี 2026 — ทบทวนประจำปี (`_AMS-update-workflow.md`).
- **Anti-hallucination:** ห้ามเพิ่ม gap/ตัวเลข/ชื่อรุ่น/citation ที่ไม่มีในแหล่ง. เรคคอร์ดที่ไม่มี citation → confidence
  ต้องสะท้อนตามจริง.
