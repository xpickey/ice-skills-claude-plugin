# Doc QA-Log — Template กลางต่อเอกสาร (ONE-HOME)

> **Version: V01R02 | 2026.07.14** (+`mode` ใน Process Compliance — รองรับ MODE GATE/PROVENANCE LOCK)
> **V01R01 | 2026.07.13** — QA-log บังคับของทุกงาน DOC-PIPELINE V2: **ไม่มี QA-log = งานไม่จบ**
> **ที่มา:** ยกรูปแบบที่พิสูจน์แล้วจากงานจริง (EuroFood Planning Deck 2026.07.13 — ตัวอย่างที่เดิน pipeline ถูกต้องครบ) · ใช้โดย: กัปตัน V03R04 (§9) · คิม V02R03 (K6) · สมนึก V02R03 (T6) · เจนนี่ V02R03 (D-P5 fixed_issues) · อริส V02R02 (D-P4)

## LOCATION + OWNER

```
LOCATION: {project}/00 - Context/[ชื่อเอกสาร]_QA-log.md   (1 ไฟล์/artifact — ทุก version/รอบลงไฟล์เดิม ไม่แตกไฟล์ใหม่)
OWNER:    L1 (กัปตัน/คิม/สมนึก) เขียน · ⑤ คืน detected_issues (read-only) · ④ คืน fixed_issues
CREATE:   ตอนเริ่ม D-P3 BUILD ครั้งแรกของ artifact นั้น
```

## TEMPLATE

```markdown
# QA Log — [ชื่อเอกสาร]
## บันทึกการตรวจคุณภาพต่อเอกสาร (ต่อเนื่องทุกรอบ — ไม่ใส่ version ในชื่อไฟล์)

Artifact: <ชื่อ + ชนิด> · Deal/Project: <ชื่อ>
Producer: <L1 (V3 default) | jenny-shell (user เรียกตรง)> · Checker: อริส (qa-master) · Coordinator: <L1> · **builder = L1|jenny-shell**

---

## Round — V##R## (YYYY.MM.DD) — <หัวข้อรอบ เช่น "build แรก" / "แก้ 5 จุดหลัง QA">
Producer <ใคร> · Checker <ใคร + tier: FAST/FULL/DELTA> (+ Codex Mode B ถ้าใช้) · **verdict = PASS/BLOCK/WARN · counts: critical=X major=Y minor=Z**

**Process (Compliance line):** **mode=<SOLO|PANEL|LITE|FULL>** · อ่าน=<ใคร> · approach=<ใคร> · build=<ใคร> · QA=<ใคร> · final-decide=<L1> · exceptions=<ไม่มี | [EXCEPTION] อ้าง team-memory>

**Render evidence (EVIDENCE FRESHNESS — บังคับเมื่อมี visual QA):**
`<คำสั่ง render เช่น soffice --headless --convert-to pdf ... && pdftoppm -png -r 100 ...>` · dpi=<N> · rendered=<YYYY.MM.DD HH:MM> · จากไฟล์ V##R## ปัจจุบัน ✓

**Findings + คำตัดสิน L1 (รายข้อ):**
1. [BLOCK|SHOULD|NOTE] <อาการ + ตำแหน่ง slide/หน้า> → **[FIX → แก้: ใคร] / [WON'T-FIX + เหตุผล]**
2. ...

**Validator (④):** font_embed n/n · collision 0 · overflow 0 · <format-specific> · real PowerPoint เปิดไม่ Repair ✓

**เหลือ/ค้าง:** <รอ user ตัดสิน / spot-check ตา user / ไม่มี>
```

## กติกา

1. **1 รอบ QA = 1 หมวด Round** — append ต่อท้าย ไม่ลบรอบเก่า (ประวัติ = หลักฐาน audit)
2. **ทุก finding ต้องมีคำตัดสินของ L1** (FIX/WON'T-FIX+เหตุผล) — finding ค้างไม่มีคำตัดสิน = รอบยังไม่จบ
3. **Render evidence บังคับ** เมื่อรอบนั้นมี visual/layout QA — ไม่มีบรรทัด render = verdict มิติ visual ใช้ไม่ได้ (กัน Akara-case: ตรวจจาก PNG เก่า)
4. **Process Compliance บรรทัดเดียวต่อรอบ** — ใคร audit ย้อนหลังอ่านบรรทัดนี้รู้ทันทีว่างานเดิน pipeline หรือหลุด
5. **⭐ `mode` = หลักฐาน PROVENANCE LOCK (V01R02):** artifact ที่มีแต่ round ที่ mode=SOLO/PANEL/LITE และยังไม่เคยมี round FULL → **ยังส่งลูกค้าไม่ได้** (RATCHET) — บรรทัดนี้คือที่ที่ L1/User ตรวจได้ว่าผ่านด่านหรือยัง
6. QA-log ละเอียดราย artifact · `_team-memory.md` เก็บเฉพาะภาพรวม/บทเรียนที่ทีมต้องรู้ — ไม่ซ้ำหน้าที่กัน

*Version V01R02 (2026.07.14 — +mode) · คู่กับ DOC-PIPELINE V2 + MODE GATE (ไฟล์กัปตัน §5) + FAILURE PROTOCOL (§6) + team-memory [EXCEPTION] (V01R03)*

## บทความวิชาการชิ้นที่ 9 — การจัดชั้นแรงงานใหม่ในยุคปัญญาประดิษฐ์ (2026.08.11)
- **artifact:** `Academic/บทความวิชาการที่ 9/การจัดชั้นแรงงานใหม่ยุคปัญญาประดิษฐ์_V01R10_2026.08.11.docx`
- **ปลายทาง:** วารสารสหวิทยาการนวัตกรรมปริทรรศน์ (JIDIR) · builder = L0 adopt สมนึก · QA = อริส 7 รอบ
- **verdict สุดท้าย:** WARN-PASS — critical 0 · major 0 · ดุลพินิจผู้เขียน 4
- **ตัวเลขปิดงาน:** Word 14 หน้าทั้งฉบับ / เนื้อความ 12 หน้า (เกณฑ์ ≤15 และ ≤12) · 7,098 คำ · อ้างอิง 30 รายการ ไทย 21 (70%) · สองทิศทางครบ 30/30 · ตัวเอน 30/30 · D5 14/15 · TH SarabunPSK ตระกูลเดียว ฝังครบ · `<w:cs/>` 199 · cantSplit 10 · ภาพ 400 dpi
- **บทเรียนที่ต้องจำ:**
  1. **นับหน้าเชื่อได้เฉพาะ Microsoft Word** — LibreOffice ต่ำกว่าคงที่ 2 หน้าตลอด 3 รอบ (13 vs 15) เพราะตัดบรรทัดไทยคนละกลไก
  2. **ธาตุ `<w:cs/>` ≠ คุณลักษณะ `w:cs` ของ rFonts** — ตั้งแต่ชื่อฟอนต์อย่างเดียวไม่พอ ต้องประกาศว่าข้อความเป็นอักษรเชิงซ้อนด้วย มิฉะนั้น Word ตัดคำไทยไม่ได้ + jc=thaiDistribute จะยืดตัวอักษรจนอ่านไม่ได้ (เจอ 0/200 ครั้งแรก แก้เป็น 199 → หน้าลดจาก 16 เหลือ 14 ทันที)
  3. **ภาพประกอบต้องออกแบบบนขนาดพิมพ์จริง** — ออกแบบบน 10 นิ้วแล้ววางที่ 6.2 นิ้ว = ตัวอักษรเหลือ 62% (13pt → 8pt)
  4. **เรนเดอร์ภาพที่ได้ทั้งอักษรไทยถูกและกราฟิกสมัยใหม่ = headless Chrome --print-to-pdf** (LibreOffice จัดไทยถูกแต่ไม่รองรับ flexbox/gradient · PIL ทำกราฟิกได้แต่สระลอย)
  5. **`cantSplit` แก้แถวถูกผ่า แต่สร้างช่องว่างท้ายหน้า** — เคส นี้ 150.9 จุด ≈ ส่วนล้นพอดี ทางแก้ที่ถูกคือย่อข้อความในช่องตาราง (คืนพื้นที่สองทางพร้อมกัน) ไม่ใช่ตัดเนื้อความอย่างเดียว
  6. **การขึ้นบรรทัดบังคับ (`<br>`) ไม่กันการตัดซ้ำชั้นสอง** — แต่ละท่อนต้องสั้นพออยู่ในหนึ่งบรรทัดจริง มิฉะนั้นระบบตัดซ้ำและอาจผ่ากลางคำ
  7. **ผู้ตรวจรายงานผิดได้ ต้องมีหลักฐานตรวจสอบเอง** — อริสรายงานว่าฟอนต์ในภาพไม่ใช่ TH SarabunPSK ผู้เขียนตรวจ pdffonts แล้วพบว่าเป็น จึงส่งกลับ อริสตรวจซ้ำแล้วถอนข้อนั้น · และอริสเองพบว่ารายงานรอบ 5 ของตัวเองเรื่องตารางที่ 1 คลาดเคลื่อน แล้วแก้ในรอบ 7
  8. **ผู้ตรวจไม่ปิดข้อเท็จจริงภายนอก** — ISS-005 อริสยืนยันว่า "หลักฐานของผู้เรียก มิใช่ของผู้ตรวจ" ผู้เขียนไปเปิดเว็บจริงแล้วพบว่าชื่อระบบที่ใช้ผิด (ระบบเตือนภัยด้านแรงงาน ไม่ใช่ ระบบพยากรณ์และเตือนภัยฯ)
