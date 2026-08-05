---
name: ice-doc-builder
description: "iCE Document Build Craft — ความรู้ build .pptx/.docx/.xlsx/PDF/HTML ระดับ specialist (Build Discipline D1-D4 tri-slot Thai+EN font, 18 PPTX lessons, Method B font-embed, Strict Validator, SAVE-FIRST, VALIDATION BUDGET, renderer ladder) ที่ย้ายมาจาก deliverable-gen-agent เพื่อให้ทุก persona โหลดใช้ได้ (L0/กัปตัน/คิม/สมนึก build เองใน DOC-PIPELINE V3 · เจนนี่-shell ใช้ตอน background build). ถือ contract ของ marker ICE_BUILD=pipeline (PreToolUse hook). Triggers (TH): build deck, สร้าง slide, สร้างเอกสาร, ทำ proposal เป็นไฟล์, สร้าง .pptx, ทำ .docx, ทำ .xlsx, ทำ ROI excel, dashboard, font ไทย, font เพี้ยน, แก้ font, embed font, ไฟล์เปิดไม่ได้, Repair dialog. Triggers (EN): build deck, generate slides, build document, create pptx/docx/xlsx, ROI workbook, dashboard, font embed, Thai font, corrupted file, ICE_BUILD."
---

> **Skill:** ice-doc-builder | **Version:** V01R12 | **Date:** 2026.08.06
> **V01R12 (2026.08.06 · คำสั่ง user):** ⭐ FILE HYGIENE — §0.1 ข้อ 6 + แก้ต้นตอใน §7 ②: "save ใต้ ~/Documents แล้วย้าย" → staging `~/Documents/.ice-staging/` + ย้ายเข้า `_build/_qa/` ในคำสั่งเดียวกัน (ขยะ `_qa_aris_vfin/` 11 MB + `qa_s6_*.pptx` ใต้ ~/Documents — user เจอ ไม่ใช่ระบบ) · SSOT ทั้ง fleet = `reference/file-hygiene.md`
> **V01R11 (2026.08.05 · คำสั่ง user — เคส VFIN):** +**§3.0 ⑤ TEMPLATE-BASE BUILD** — งานต่อยอด template/เด็คเดิมใช้ฟอนต์ตามนโยบายปัจจุบันเป็นค่าเริ่มต้น **ห้ามสืบทอดฟอนต์ template อัตโนมัติ** · ฟอนต์ template เฉพาะ user สั่งชัดเจน (font_override_reason + QA-log) · agent ห้ามออก --allow-font ให้ตัวเองด้วยเหตุผลความสม่ำเสมอ · PLAN-CARD ต้องแจ้ง mixed-font ชั่วคราว · ③ APPROVED SET จำกัดขอบเขตเหลืองานเริ่มจากศูนย์ · `font_policy` V01R08 · อริส +D7.6d
> **V01R10 (2026.08.05 · QA + คำสั่ง user):** +**§0.1 ข้อ 0 ASK-FIRST** (คำถามค้าง = ห้ามเริ่ม build · เอกสารพร้อมคำถามแนบท้าย = ผิด protocol) · **แก้ §3.0-A แถวสไลด์แน่น:** ฟอนต์ = `Leelawadee` ตัวธรรมดา (เดิมเขียน Leelawadee UI ไม่ตรงกับโค้ดและคำสั่ง user) + เกณฑ์อัตโนมัติ + 🔴 ยกเว้น rail=govt (ฟอนต์บังคับ TOR ชนะกฎความแน่น) · อ้างอิงเดิม V01R09 | **Date:** 2026.08.04
> **V01R09 (2026.08.04) — ⭐ ตารางตัดสินใจฟอนต์ถาวร (§3.0-A):** เกณฑ์ 5 ข้อเรียงตาม "อำนาจตัดสิน" (ฝังได้ไหม → สิทธิ์ → น้ำหนัก → GAP → ยอดวรรณยุกต์) + ตารางงาน×ฟอนต์ · **กฎใหม่ (user): PPTX สไลด์แน่นต้องบีบบรรทัด → `Leelawadee UI` แทนฟอนต์ราง** (ยอดวรรณยุกต์ 0.743 vs 0.924 → ไม่ชนเมื่อบีบ · PPTX ฝังได้จึงไม่ต้องห่วงเครื่องผู้รับ) · **fallback เปลี่ยนเป็นลำดับ** `Leelawadee UI → Sukhumvit Set → Tahoma` (user: "Tahoma ไม่ค่อยสวย") · +บันทึกความจริงว่า **ไม่มีฟอนต์ไทยสวยตัวไหนมีทั้ง Win+Mac** → ทางแก้จริงคือ PDF companion ไม่ใช่หา fallback สวย · `font_policy` V01R03 (`fallbacks` เป็น list + `rail_fallbacks()`)
> **V01R08 (2026.08.04) — ตัวเลือกฟอนต์ (คำสั่ง user):** +**Leelawadee / Leelawadee UI / UI Semilight** เป็นตัวเลือกที่อนุมัติ (ผ่าน V4 ไม่ต้อง `--allow-font` · auditor แจ้ง ℹ เตือน GAP ทุกครั้ง) · ⛔ **ถอด Sarabun ออกจากตัวเลือก (V5 ใหม่)** — คนละตัวกับ TH Sarabun New/TH SarabunPSK ที่ยังใช้ได้ · **default ยังเป็น IBM Plex Sans Thai Looped** เพราะวัดแล้ว GAP ไทย-ละติน 18.9% ชนะ Leelawadee 27.3% (เกณฑ์ตัดสินตามคำสั่ง user "GAP ดีกว่าเอาตัวนั้น") · `font_policy` V01R02 (+APPROVED_ALT +RETIRED) · `build_xlsx` V02R04 (เลิกมีสำเนากฎ → เรียก `check_fonts` จาก SSOT)
> **V01R07 (2026.08.04) — ⭐ ONE POLICY, ONE AUDITOR, ALL FORMATS:** นโยบายฟอนต์ย้ายเป็น SSOT `_lib/font_policy.py` (RAILS+BLACKLIST+check_fonts) · **§0.1 ข้อ 4 ยกเป็นกติกาบังคับ: build script ทุกตัว `from font_policy import RAILS` — ห้าม hard-code ชื่อฟอนต์** · **จุดตรวจเดียว `_lib/audit_fonts.py`** ครอบ xlsx/pptx/docx/html/pdf · build_pptx/docx/dashboard/deck/html แก้ให้อ่านจากรางแล้ว (build_pptx เดิม **ไม่เคย set ฟอนต์เลยสักบรรทัด** · build_docx ไม่มี `w:cs` · dashboard เป็น CSS ละตินล้วน) · เอกสารกำกับที่เคยขัดกันเอง (`05-typography` V02R01 · `sales-pipeline-report` V01R04 · `gantt-timeline` V01R02) ลดเหลือ pointer
> **V01R06 (2026.08.04) — ⭐ V4 RAIL CONFORMANCE:** +**§6 V4** ตรวจว่าฟอนต์ **ตรงรางที่นโยบายกำหนด** ไม่ใช่แค่ "resolve ได้ + ไม่ blacklist" (V1/V2 ตอบคนละคำถามกับนโยบาย → Sarabun ลอดทั้งคู่) · เคสจริง `PWA TCO-Breakdown V01R22` build 2026.08.04 ยังเป็น Sarabun แล้ว validator ขึ้น PASS — **user จับได้ ไม่ใช่ระบบ** · ต้นเหตุ: build script เขียนมือ hard-code `FONT` เอง → bypass ตาราง RAILS · +**E4 แก้ false positive** (fail เฉพาะ merge **และ** ไม่ตั้ง row height — พิสูจน์ด้วย differential test ว่าไฟล์ที่ builder เราสร้างสดก็ FAIL) · `build_xlsx.py` **V02R02**
> **V01R05 (2026.08.01) — RENDERER SHIM GUARD:** +**§7 กฎข้อ 0** `soffice` ใน PATH = shim ของ codex runtime ที่แทนฟอนต์ทั้งไฟล์เงียบ ๆ → ใช้ `_lib/render_pdf.sh` เสมอ + POST-RENDER FONT VERIFY
> **V01R04 (2026.07.31)**
> **V01R04 (2026.07.31) — THAI WORD BREAKING (คำสั่ง user):** +**§3.5** ตัดบรรทัดไม่ผ่ากลางคำ ด้วย **PyThaiNLP** (`newmm` — `longest` ห้ามใช้ มัน lowercase อังกฤษ) · **3 ชั้น**: T1 lang-tag `th-TH` (ไม่แตะข้อความ · docx/pptx) → T2 QA-only ทำนายจุดผ่ากลางคำแล้วขยายคอลัมน์แทน (⭐ default ของ xlsx) → T3 ZWSP (ทางสุดท้าย · **แลกกับ Ctrl+F หาไม่เจอ**) · tool: `_lib/thai_wordbreak.py` · เคสจริง: PWA TOR Matrix เสี่ยง **47/261 เซลล์**
> **V01R03 (2026.07.31) — FONT POLICY 2 ราง + Excel discipline + validator ใหม่ (LOCKED โดย user):** +**§3.0 FONT POLICY** (เอกชน = `IBM Plex Sans Thai Looped` ไทย=อังกฤษไม่บวก pt · ราชการ = `TH Sarabun New` 16pt · BLACKLIST 8 ตระกูลพร้อมเหตุผล · single-family-first) · +**§3.2 XLSX เขียนใหม่ E1-E6** (Excel ฝัง font ไม่ได้→PDF companion · row height = pt×1.45×บรรทัด+6 · vertical=center · ห้าม merge ในแถวไทย+wrap · ห้าม shrink-to-fit · ตั้ง default font ก่อนคำนวณ width) · +**§3.1 W1-W3** (ascii+hAnsi+cs ตัวเดียวกันเพราะสเปก MS ขัดกันเอง · bCs/iCs บังคับ · ห้าม lineRule=exact) · +**§6 V1-V3 validator** (⭐V1 font-name resolution ดักชื่อฟอนต์ที่ไม่มีจริง · V2 blacklist · V3 สระอำ integrity) · **แก้ D3** เลิกใช้ "+1-2pt" และ "line-height 1.8+" ที่**ตรวจแล้วไม่มีต้นทางจริง** → ใช้สูตร cap-height ratio ที่วัดเอง · **แก้ D1** single-family แทน paired
> **ฐานหลักฐาน V01R03:** PDF สาธารณะ 45 ฉบับ (`pdffonts`+span) · วัด metric ฟอนต์จริง 9 ตระกูล · user ทดสอบสายตา · เคสจริง PWA TOR Matrix · เอกสารเต็ม → `Output/iCE_Thai-Latin_Font-Policy_PROPOSAL_V01R01_2026.07.31.md`
> **V01R02 (2026.07.18):** ดูด้านล่าง
> **V01R02 (2026.07.18):** +§2B DOCX/XLSX CORRUPTION LESSONS + RECOVERY LADDER (จ่ายราคาจริง VFIN V02R02 docx: Word Repair→error 3 รอบ — Word-strict vs LO-lenient · settings order CT_Settings · hand-rolled odttf = Word ปฏิเสธ · rels self-closing · false-green MCP/AppleScript · LO round-trip rescue) + แก้ §3.1 EMBED ("Word ทำได้เหมือน pptx" = ผิด — GUI-embed หรือ PDF companion เท่านั้น)
> **กำเนิด:** DOC-PIPELINE V3 — สกัดจาก deliverable-gen-agent V02R08 §4/§5/E4 **คำต่อคำ** (ความรู้ที่แลกด้วยความเจ็บจริง) + เพิ่ม §3 FONT DISCIPLINE ข้ามฟอร์แมต (DOCX/XLSX/PDF — คำสั่ง user 2026.07.17: "Word font ไม่สม่ำเสมอ เอาบทเรียน PPTX มาใช้กับ PDF/Word/Excel")
> **ผู้ใช้ skill นี้:** L0 (adopt กัปตัน/คิม/สมนึก) build เองใน pipeline · deliverable-gen-agent (เจนนี่-shell) ตอน background build · ทุกกรณี **QA โดยอริสยังบังคับ — skill นี้ไม่ใช่ใบผ่าน QA**

---

# §0 CONTRACT — ใครใช้ ใช้เมื่อไหร่ marker อะไร

## 0.1 เงื่อนไขก่อน build (ครบทุกข้อจึงเริ่ม)
0. **⭐ ASK-FIRST ผ่านแล้ว (V01R10 · คำสั่ง user 2026.08.05)** — ทุกข้อสงสัยที่ source ไม่ตอบ
   (ผู้อ่าน/โครง/ความยาว/ตัวเลขที่ขาด/สิ่งห้ามใส่/ภาษา+ราง) ถูกถาม user เป็นชุดเดียวและ**ได้คำตอบแล้ว**
   — มีคำถามค้าง = ห้ามเริ่ม build · เจอกำกวมใหม่ระหว่าง build = หยุดถามทันที ห้ามเดา ·
   🔴 เอกสารส่งมอบพร้อม "คำถามปรับปรุง" แนบท้าย = ทำผิดข้อนี้ (นิยามเต็ม: กัปตัน S1 / สมนึก T1)
1. **Spec อยู่บนดิสก์แล้ว** — content spec + design spec save เป็นไฟล์ก่อนเสมอ (D-P1/D-P2 ของ DOC-PIPELINE) · build อ่านจาก spec ไม่อ่านจากความจำใน context (spec-on-disk = build ใหญ่แค่ไหน context ก็ไม่บวม)
2. **ประกาศโหมดใน PLAN-CARD แล้ว** (work_mode: lite|full) + คิว ④ อริส QA ไว้แล้ว
3. **เขียน build script ลงดิสก์** (ไม่ heredoc ยาวใน context) → รันด้วย marker
4. ⭐⭐ **ฟอนต์มาจาก SSOT เท่านั้น — ห้าม hard-code ชื่อฟอนต์ในโค้ดเด็ดขาด** (V01R07 · กติกาบังคับ)
   ```python
   import sys; sys.path.insert(0, os.path.expanduser("~/.claude/agents/_lib"))
   from font_policy import RAILS
   FONT = RAILS[rail]["font"]          # rail = "private" | "govt"
   ```
   ใช้กับ **ทุก** build script รวมที่เขียนมือรายโปรเจกต์ · `font_policy.py` = บ้านเดียวของ RAILS/BLACKLIST
   > **ทำไมถึงเป็นกฎบังคับ (เคสจริง 2026.08.04):** นโยบาย 2 รางถูก LOCK ตั้งแต่ 2026.07.31 แต่
   > `PWA TCO-Breakdown V01R22` ที่ build วันที่ 08.04 ยังออกมาเป็น Sarabun **และ validator ขึ้น PASS**
   > เพราะ build script เขียนมือตั้ง `FONT = "Sarabun"` เองเป็นค่าคงที่ ไม่เคยแตะตาราง RAILS เลย
   > สำรวจแล้วพบว่า build script **5 ใน 6 ตัว** ทำแบบเดียวกัน = นโยบายบังคับใช้ได้แค่ฟอร์แมตเดียว
   > **user เป็นคนจับได้ ไม่ใช่ระบบ**
5. **จบ build ต้องรัน `audit_fonts.py` ก่อนคิว ④ เสมอ** (§6) — build_* ของเราเรียกให้อัตโนมัติแล้ว
6. **⭐ FILE HYGIENE (V01R12 · คำสั่ง user 2026.08.06):** ไฟล์ทำงานทุกชนิด (spec/script/render/crop)
   → `<โฟลเดอร์งาน>/_build/` · หลักฐานตรวจ → `_build/_qa/` · 🔴 ห้ามสร้างไฟล์ใหม่ตรง ๆ ใต้ ~/Documents
   หรือ ~/Documents/Claude root เด็ดขาด · ไม่แน่ใจ = ถาม user · จบงาน `ls` ยืนยันไม่มีไฟล์หลง
   — SSOT: `reference/file-hygiene.md`

## 0.2 MARKER SEMANTICS (ผูก PreToolUse hook `ice-prebuild-guard.sh`)
| Marker | ใคร | ความหมาย |
|---|---|---|
| `ICE_BUILD=pipeline ` | L0 (persona กัปตัน/คิม/สมนึก) | build ถูกกฎใน DOC-PIPELINE V3 — ยืนยันว่า 0.1 ครบ + โหลด skill นี้แล้ว |
| `ICE_BUILDER=jenny ` | เจนนี่-shell เท่านั้น | background build ตาม DISK-IS-TRUTH · **USER-INVOKED ONLY: เจนนี่ทำงานเฉพาะเมื่อ User สั่ง/เรียกชื่อตรง** (L1 เสนอได้ ห้าม dispatch เอง) |
| `ICE_SMARTFIX=1 ` | L1 | Smart Fix ≤5 จุด บน base ที่ VALID |
| `ICE_INLINE_APPROVED=1 ` | ตาม FAILURE PROTOCOL | user อนุมัติ exception แล้ว |
- ทุกคำสั่ง Bash ที่รัน python สร้าง/แตะ .pptx/.docx/.xlsx ต้องขึ้นต้นด้วย marker ที่ตรงบทบาท — ไม่มี marker = hook deny (by design)
- marker ไม่ใช่ของแจก: ห้ามใส่ให้ context อื่นที่ไม่ได้โหลด skill นี้

## 0.3 SAVE-FIRST · NO SELF-RENDER (จากเจนนี่ V02R08 — คงหลักเดิม)
- **Build → SAVE V##R## ลงดิสก์ทันที → self-check เชิงโครงสร้างเท่านั้น → ส่งเข้า ④** — self-check = zip CRC · จำนวน slide/หน้า/sheet · embed flags · collision/overflow คำนวณจาก XML geometry (**ไม่ render ภาพ**)
- **ห้าม render preview เพื่อเช็คงานตัวเอง** — การดูภาพจริงเป็นหน้าที่ ④ อริส (EVIDENCE FRESHNESS — render สดอยู่แล้ว) · render ซ้ำ = จ่าย token ×2
- ข้อยกเว้น: CB Progressive per-unit preview หรือ user สั่ง preview ชัดเจน → ใช้ Renderer Ladder (§7)
- กฎเหล็ก: **tool รายงานสำเร็จ ≠ ไฟล์เกิดจริง — `ls -la` ยืนยัน output ทุก save/export**

## 0.4 D-P3/D-P5 ROLE RULES (จาก DOC-PIPELINE)
- **D-P3 BUILD:** build ตาม spec **ห้ามแก้เนื้อหาเอง** — เจอปัญหา content → หยุด flag (content เป็นของ ①②)
- **D-P5 FIX:** แก้**เฉพาะ**ตาม consolidated fix list ที่ L1 FINAL รายข้อแล้ว → SAVE R+1 → ④ delta re-QA เสมอ
- **D7 HARD BLOCK (font/layout customer-facing):** L0 ห้ามตัดสิน WON'T-FIX เองฝ่ายเดียว — ต้อง user sign-off
- fail แบบเดิม 2 ครั้ง → หยุด รายงาน diagnostic — **ห้าม debug spiral** (บทเรียน TQR 155 calls)

---

# §1 🎨 BUILD DISCIPLINE D1-D4 (แก้ Font "Serious" — Global BP + 4 projects + TQR · คงคำต่อคำ)

> หลักฐาน 3 แหล่ง: Microsoft Learn (Thai x-height < ก-height = Latin cap-height) · Google/Adobe (CJK +1px, line +0.1em) · 4 projects จริง (BAAC "set latin+ea+cs explicit" · EXIM "16,548 Tahoma runs เพราะไม่มี cs=, 5 font spellings" · Banpu "Thai 0.5-1pt smaller, width 1.15-1.20×")

## D1 — TRI-SLOT FONT BINDING (latin + ea + cs) ⭐⭐⭐ แก้ TH+EN ไม่จับคู่ + tofu
```
ทุก text run set 3 slots ใน <a:rPr> → PowerPoint เลือก font ต่อ glyph เอง
(ไม่ต้อง split run = กัน empty <a:t> corruption ตาม TQR §13):
  <a:latin typeface="Open Sans"/>   ← EN/Latin glyphs
  <a:ea    typeface="Open Sans"/>   ← East-Asian (กัน fallback)
  <a:cs    typeface="Sarabun"/>     ← Complex Script = THAI ⭐
+ theme1.xml majorFont/minorFont ต้อง set <a:cs> + <a:ea> ด้วย (ไม่ปล่อยว่าง — python-pptx default ว่าง)

⭐ V01R03 — SINGLE-FAMILY FIRST: ใช้ฟอนต์ตัวเดียวใส่ทั้ง latin/ea/cs (ดู §3.0 FONT POLICY)
  เพราะฟอนต์ที่เลือกมีละตินออกแบบคู่มาในตัว → ไม่ต้องจับคู่ ไม่ต้องชดเชยขนาด
  จับคู่ 2 ตระกูลเมื่อจำเป็นเท่านั้น (เช่น ลูกค้าบังคับ Latin brand font) → ต้องชดเชยตาม D3
```

## D2 — FONT NORMALIZATION MAP แก้ font chaos (font_test.pptx มี 13 fonts ปน!)
```
ก่อน save → enumerate fonts ที่ใช้จริง → rewrite variant → spec:
  "TH SarabunPSK"/"TH Sarabun PSK"/"THSarabunPSK" → "Sarabun"
  "Calibri"(render ไทย)/"Tahoma"(ไม่ตั้งใจ)/"Browallia" → paired spec
→ collapse ทุก font นอก approved set → report before/after count (EXIM 27→12 เคยทำมือ → auto)
```

## D3 — OPTICAL SIZE (⭐ เขียนใหม่ V01R03 — เลิกท่องอัตราส่วน ใช้ cap-height ที่วัดได้)

> **ทำไมต้องรื้อ:** กฎเดิม "TH +1-2pt (Google/MS ยืนยัน)" และ "line-height TH 1.8+" — ตรวจสอบย้อนแล้ว **ไม่มีต้นทางจริง** (เอกสาร Google Fonts ที่ถูกอ้างไม่พูดถึงไทยเลย) · กฎเดียวที่ตีพิมพ์จริงคือ **Material Design: ไทย +1px มีเพดาน + line-height +0.1em + เลี่ยง Bold** ซึ่งเป็น offset คงที่ ไม่ใช่อัตราส่วน

```
⭐ กฎตัดสินขนาด (ใช้ cap-height ratio แทนการเดา):
  ① ฟอนต์เดียวครอบ 2 ภาษา (นโยบายหลัก §3.0) → TH sz = EN sz  ห้ามบวก
     (วัดแล้ว: IBM Plex Sans Thai Looped / Sarabun cap ≈ 0.700 em = ละตินในตัวเดียวกัน)
  ② จับคู่ 2 ตระกูล → ชดเชยด้วยสูตร:  TH_pt = EN_pt × (cap_ละติน ÷ cap_ไทย)
     ค่าที่วัดจากไฟล์จริงบนเครื่องนี้ (em):
       Sarabun 0.700 · IBM Plex Sans Thai (+Looped) 0.698 · Anuphan 0.698
       Tahoma 0.727 · Noto Sans Thai 0.714 · Kanit 0.644 · TH Sarabun New/PSK 0.476
       (ละติน: Open Sans 0.714 · Raleway 0.710 · Arial 0.716 · Helvetica 0.717)
     → TH Sarabun New คู่ละติน 11pt = 11 × (0.714÷0.476) ≈ 16pt ✅ ตรงธรรมเนียมราชการพอดี
  ③ ไม่มีค่าวัด → ใช้ Material Design: TH = EN +1pt (หยุดบวกเมื่อ ≥ ขนาดหัวข้อ)
• TH-only object: body ≥18pt · heading ≥24pt (ห้าม TH <16pt customer-facing)
• ⭐ LINE HEIGHT ไม่ใช้เลขลอย — คำนวณจาก winAscent ของฟอนต์นั้นจริง (ดู §3.0 ตาราง)
  rule of thumb ที่ทดสอบแล้ว: row/line = pt × 1.45 ต่อบรรทัด (ไม่ใช่ 1.8)
• ⭐ Bold ไทย: Material Design แนะนำ**เลี่ยง Bold** (native speakers: หนาเกิน) →
  ใช้ SemiBold/Medium แทนถ้าฟอนต์มี (IBM Plex Looped มี Medium/SemiBold ครบ)
• Thai width budget = 1.15-1.20× Latin (คำนวณ box width)
```

## D4 — NO-OVERLAP + FONT-EMBED + STRICT VALIDATOR แก้ object ทับ + font หาย
```
STRICT VALIDATOR (mandatory ก่อนส่งเข้า ④):
  ✓ CHAR-GUARD (Lesson #18) ⭐: scan U+2192 (→) + ญาติ (⟶/➜/➔) ในทุก text run → PowerPoint reject ทั้งไฟล์
      → auto-replace ด้วย ▸ (build_pptx.py ทำตอน build · validator ตรวจซ้ำ safety net) · LibreOffice มองไม่เห็น
  ✓ Collision: คำนวณ bbox ทุก shape → overlap > threshold → flag + auto-fix
  ✓ Overflow: text ยาว vs box (TH 1.15-1.20×) → normAutofit fontScale floor ≥80%
  ✓ Bleed: object เลย slide 12.19m×6.858m → move in
  ✓ TH-wrap: TH sub-header wrap ลง teal underline → widen textbox (TQR G4)
  ✓ FONT-EMBED ⭐⭐⭐ (KD V01R01 2026.06.03 — verified ใน REAL PowerPoint โดย User):
      ⛔ METHOD A (LibreOffice EmbedFonts) = ใช้ไม่ได้จริง — พิสูจน์แล้ว ห้ามใช้:
        soffice --convert-to pptx:...EmbedFonts → unzip พบ 0 fntdata (ไม่ embed เลย)
        + เขียน sldSz type="screen4x3" ทับ → ทำลาย 16:9 (LibreOffice embed ได้เฉพาะ .odp)
      ✅ METHOD B (PRIMARY) = _lib/embed_fonts_pptx.py — ทำ 5 เงื่อนไขครบอัตโนมัติ:
        python3 ~/.claude/agents/_lib/embed_fonts_pptx.py IN.pptx OUT.pptx \
          --font "Open Sans:regular=/path/OpenSans-Regular.ttf,bold=...Bold.ttf" \
          --font "Sarabun:regular=/path/Sarabun-Regular.ttf,bold=...Bold.ttf"
        5 เงื่อนไข (ขาดข้อใด = Repair dialog หรือ font หาย):
          1. embeddedFontLst วาง AFTER notesSz (ECMA-376 — LibreOffice ผ่อนปรน แต่ PowerPoint reject)
          2. ⭐ fontTools round-trip normalize ทุก font (TTFont(src).save(dst)) —
             แก้ "Install Embedded Fonts: General Failure" · แม้ STATIC font ก็ต้อง normalize
             (Bug#2: Sarabun static + fsType Installable + name สะอาด ก็ยัง fail ถ้าไม่ normalize)
          3. content-type = application/x-fontdata (ไม่ใช่ x-font-ttf/obfuscated)
          4. embedTrueTypeFonts="1" + saveSubsetFonts="0" (ฝัง full ไม่ใช่ subset — python-pptx default "1" = mismatch)
          5. static font (Variable → instancer) + fsType ≠ 0x0002 Restricted (Restricted = ห้าม embed ตามลิขสิทธิ์)
      ✅ METHOD C (FALLBACK ปลอดภัยเสมอ) = PDF companion — PDF ฝัง font ในตัว 100% (ส่งคู่ .pptx)
      LICENSE: Raleway/OpenSans/Kanit/Sarabun/IBMPlex = SIL OFL (embed ถูกกฎหมาย) · ตรวจ fsType ก่อนเสมอ
      EMBED เมื่อ: customer-facing=MANDATORY · internal=optional · PDF=ไม่ต้อง
  ✓ Corruption: empty <a:t>==0 · run-less <a:p> missing endParaRPr==0 · sldSz NO type attr
  ✓ FONT-EMBED VALIDATE ⭐: python3 ~/.claude/agents/_lib/validate_pptx_fonts.py OUT.pptx → ต้อง PASS
      (ตรวจ CT_Presentation order + content-type x-fontdata + embedTrueTypeFonts=1 + fntdata มีจริง)
      + typeface ใน embeddedFontLst ตรงกับ name-table family (nameID 1) + match a:cs ใน run (D1)
  ✓ Package: unzip -t (CRC) · [Content_Types] complete · rId integrity · docProps company="iCE Consulting Co., Ltd."
  → OPEN IN REAL POWERPOINT = บังคับ (qlmanage/LibreOffice = false-green — มองไม่เห็น corruption/16:9/General-Failure/U+2192)
      ⛔ LibreOffice render ผ่าน ≠ validation pass — ใช้ preview เร็ว ๆ ได้ แต่ "สวยใน LibreOffice" อาจเป็นไฟล์เสียในเครื่องลูกค้า (KT Food S4: → หลุดเพราะ LibreOffice ปล่อยผ่าน)
      ⚠️ font "General Failure" (อาการ B) = AppleScript/qlmanage มองไม่เห็น → คนเปิด PowerPoint ดู dialog

🚧 BUILD NOTE: embed customer-facing = Method B เสมอ · ห้ามใช้ LibreOffice EmbedFonts
(พิสูจน์แล้วไม่ embed + พัง 16:9) · embed ไม่ผ่าน/font Restricted → fallback PDF companion (Method C)
```

---

# §2 — 18 PPTX Lessons (คงคำต่อคำ — แลกด้วยความเจ็บจริงจาก TQR §6.7)
```
✓ corruption-safe: endParaRPr ครบ + ไม่มี empty <a:t> (str.replace ที่ทำ run ว่าง)
✓ 16:9: strip sldSz type='screen4x3' (python-pptx default 4:3 — qlmanage มองไม่เห็น)
✓ embeddedFontLst AFTER notesSz (ECMA-376 order — บั๊ก V03R01-R04) → canonical = D4 cond.1
✓ font-scale-by-context: scale เฉพาะ body 9.5-13pt · skip ≤9.4 fine-print + ≥13.5 heading
✓ text()=run-per-line vs para_runs()=inline runs
✓ static font weights + fontTools round-trip normalize ⭐ (Variable→instancer; แม้ static ไม่ normalize ก็ "General Failure") → canonical = D4 cond.2
✓ no raster-of-text (โดยเฉพาะไทย — กัน Reisurance/Steeeing corruption)
✓ merge: deep-copy slide XML + re-relate image parts · page-renumber: defer to merge
✓ _noshadow() default ทุก shape · translucent: manual alpha injection
✓ preset-swap in place ต้องล้าง avLst ⭐ — gd ของ preset เดิม (เช่น adj ของ roundRect ค้างบน ellipse หลังเปลี่ยน prstGeom) ทำให้ PowerPoint สั่ง Repair ทั้งที่ qlmanage/LibreOffice/Keynote เปิดผ่าน → เปลี่ยน prstGeom ต้องเคลียร์ <a:avLst> เดิมเสมอ
✓ U+2192 (→) ใน text ⭐ — PowerPoint for Mac ปฏิเสธทั้งไฟล์ (Repair) ทันทีที่เจอ "→" (+ญาติ ⟶/➜/➔) · LibreOffice/qlmanage ปล่อยผ่าน (false-green) → แทนด้วย ▸ (U+25B8) · _lib/build_pptx.py auto-replace · debug ด้วย binary-search แยกหน้าทีละหน้า (ไม่ใช่อ่าน spec)
```

---

# §2B ⭐ DOCX/XLSX CORRUPTION LESSONS + RECOVERY LADDER (V01R02 ใหม่ — จ่ายราคาจริง VFIN V02R02 docx คืน 2026.07.17: Repair → "error trying to open" 3 รอบ)

> คู่แฝดของ §2 ฝั่ง Word/Excel — คำสั่ง user: "เอาบทเรียนแก้ error ของ PPTX มาใช้กับ Word/Excel ด้วย"

## 2B.1 DOCX Corruption Lessons (ทุกข้อ = เกิดจริง ยืนยันจริง)
```
✓ ⭐⭐⭐ WORD-STRICT vs LO-LENIENT (กฎแม่ของทุกข้อ): LibreOffice เปิด/convert ผ่าน + zip OK + XML
  parse ผ่าน + render สวย 11/11 หน้า ≠ Word เปิดได้ — Word ตรวจ schema ลึกกว่าทุกเครื่องมือบน host
  → "LibreOffice ผ่าน" ใช้เป็น preview เท่านั้น ห้ามเซ็นรับรอง G6
✓ ⭐⭐⭐ settings.xml ELEMENT ORDER (CT_Settings sequence): แทรก element ผิดตำแหน่ง = Repair ทั้งไฟล์
  ลำดับที่ต้องจำ: zoom → embedTrueTypeFonts → embedSystemFonts → saveSubsetFonts → proofState →
  defaultTabStop → … → savePreviewPicture → … → updateFields → compat → rsids
  (ห้าม append หัว/ท้าย <w:settings> มั่ว — python-docx ไม่มี ordered-insert ให้ settings)
✓ ⭐⭐⭐ HAND-ROLLED odttf EMBED ใน DOCX = Word ปฏิเสธ ("unreadable content" → "error trying to open")
  แม้ทำครบตามตำรา ECMA (obfuscate XOR reversed-GUID + fontKey + fontTable embeds + rels + Content-Types):
  Word ก็ไม่รับของที่ประกอบมือ → DOCX EMBED มี 2 ทางเท่านั้น:
  (ก) ตั้ง flag แล้วให้ WORD GUI เขียน font parts เอง (user: Word > Preferences > Save > Embed fonts > Save)
  (ข) Method C: PDF companion (pdffonts ทุกแถว emb=yes) — ปลอดภัยเสมอ ⭐ default
  (= คู่แฝดของ ⛔ Method A LibreOffice-EmbedFonts ฝั่ง pptx — "ทางลัด embed ที่ไม่ใช่ engine จริง = พัง")
✓ ⭐ RELS SELF-CLOSING PITFALL: word/_rels/*.rels ที่ว่าง = `<Relationships/>` (self-closing)
  → โค้ด `.replace('</Relationships>', …)` ล้มเงียบ ได้ rels ว่าง → r:id ลอย = ฟีเจอร์ตายเงียบ
  (เคสจริง: embed ตาย odttf กลายเป็น dead weight 1.4MB) → handle ทั้งสองรูปเสมอ + post-gate: ทุก r:id resolve
✓ ⭐ FALSE-GREEN ตรวจ Repair: Word MCP open_document รายงาน "opened successfully" + AppleScript open
  ไม่ error — ทั้งที่ Word GUI จริงขึ้น Repair dialog → การยืนยัน no-Repair มีทางเดียว: USER เปิด Word GUI เอง
✓ duplicate attribute จาก string-injection: เช็ค xmlns บน root ต้องเช็คเฉพาะ root tag จริง
  (`split('>')[0]` เช็คผิดตำแหน่ง → เติม xmlns ซ้ำ → "duplicate attribute" → LO ก็ load ไม่ได้)
✓ List Number style = ชุดเลขเดียวทั้งเอกสาร (นับต่อข้าม section: §7 ขึ้น 12-21) → runbook/เอกสารที่เลขตายตัว
  ใช้เลข literal + hanging indent แทน · ✓ docProps creator default "python-docx" → overwrite = iCE เสมอ
✓ อาการ "error trying to open / check file permissions" หลังวน Repair: ล้าง ~$lock + xattr quarantine +
  Cmd-Q Word (stale process) ก่อน retest ทุกครั้ง — ไม่งั้น dialog เดิมโผล่ซ้ำแม้ไฟล์ดีแล้ว
```

## 2B.2 ⭐ DOCX RECOVERY LADDER (ไฟล์โดน Word ปฏิเสธ — เรียงจากถูกไปแพง)
```
① ล้างสิ่งแวดล้อม: ~$lock + xattr -c + Cmd-Q Word → user เปิดใหม่ (อาการ permission มักจบตรงนี้)
② ตรวจ XML ทุก part ด้วย parseString + เทียบ element order (§2B.1) → แก้เฉพาะจุด (surgical)
③ ⭐ LO ROUND-TRIP (พิสูจน์แล้ว 2026.07.17 · ⚠ V01R05: ต้องใช้ **absolute path** ไม่ใช่ soffice จาก PATH — §7 กฎข้อ 0):
   /Applications/LibreOffice.app/Contents/MacOS/soffice --convert-to "docx:MS Word 2007 XML"
   → LO writer เขียนไฟล์ใหม่ทั้งใบแบบ Word-compatible · TOC field/PAGE field/ตาราง/สี/font รอดครบ
   → ใช้เมื่อหา culprit ไม่เจอ/เวลาบีบ — แลกกับ style detail เล็กน้อย · เก็บไฟล์เดิมเป็น forensic เสมอ
④ Word GUI "Open and Repair" / Text Recovery (ปลายทางสุดท้าย — ให้ user กด)
+ ทุกขั้น: PDF companion ส่งได้ทันทีระหว่างซ่อม (content เดียวกัน 100%)
```

## 2B.3 XLSX Corruption Lessons (pointer — บทเรียนเดิมที่พิสูจน์แล้ว)
```
✓ "Removed Records: Formula" repair: openpyxl เขียน formula → Excel repair ทั้งไฟล์
  → freeze source formulas เป็น values + ห้าม cell text ขึ้นต้น "=" + ตรวจ 0 <f>-ไม่มี-<v> ก่อนส่ง
  (สูตร LIVE ที่ตั้งใจใส่ → ตาม §4.1: cached <v> + fullCalcOnLoad + omit calcChain)
✓ external-link flatten · ~$lock/.DS_Store strip ก่อน zip (§4.1 เดิม)
```

---

# §3 ⭐ FONT DISCIPLINE ข้ามฟอร์แมต — DOCX / XLSX / PDF (V01R01 ใหม่ — คำสั่ง user 2026.07.17: "Word font ไม่สม่ำเสมอ")

> หลักการเดียวกับ D1-D4 แต่ XML คนละตระกูล — สาเหตุ Word font เพี้ยน 90% = python-docx ปล่อย default (Calibri) รั่วบน run ที่ไม่ได้ set slot ไทย

## 3.0-A ⭐⭐⭐ ตารางตัดสินใจ — "งานนี้ใช้ฟอนต์อะไร" (V01R09 · 2026.08.04)

> ก่อนหน้านี้เกณฑ์อยู่ในหัวคน → เลือกไม่เหมือนกันทุกครั้ง · ตารางนี้คือคำตอบเดียวที่ตรวจย้อนได้

### ขั้นที่ 1 — ถามเรียงตามนี้ (ข้อบนตัดสินก่อน ข้อล่างเป็นแค่รสนิยม)

| # | คำถาม | ทำไมอยู่ลำดับนี้ |
|---|---|---|
| **①** | **ฟอร์แมตนี้ฝังฟอนต์ได้ไหม** | ฝังได้ → เครื่องปลายทาง**ไม่สำคัญเลย** เลือกตามสวยได้เต็มที่ · ฝังไม่ได้ → ต้องคิดถึงเครื่องผู้รับก่อน |
| **②** | **สิทธิ์ใช้งานอนุญาตไหม** | OFL = ฝัง/แจก/host ได้หมด · Microsoft proprietary = ฝังในเอกสารได้ แต่ **host เป็น webfont ไม่ได้** |
| **③** | **มีน้ำหนักที่ต้องใช้ครบไหม** | ไม่มี Bold จริง → Word/PPT **ปลอมหนาให้** (รีดตัวอักษร) = หัวข้อเละ · **ชดเชยไม่ได้** |
| ④ | GAP ไทย-ละติน | ชดเชยได้ด้วยการเพิ่ม pt ให้ไทย |
| ⑤ | ยอดวรรณยุกต์ | ชดเชยได้ด้วยความสูงแถว/line-height |

### ขั้นที่ 2 — เปิดตารางตามงาน

| งาน | ฝังได้? | ⭐ ฟอนต์ | เหตุผล |
|---|---|---|---|
| **PPTX ทั่วไป** | ✅ Method B | `IBM Plex Sans Thai Looped` | GAP ดีสุด 18.9% + น้ำหนักครบ 7 ตัว |
| **⭐ PPTX สไลด์แน่น/ต้องบีบบรรทัด** | ✅ | **`Leelawadee`** (ตัวธรรมดา — user เลือก 2026.08.05 · ไม่ใช่ตัว UI) | ยอดวรรณยุกต์ **0.737** vs IBM Plex 0.924 → บีบ line-height แล้ว**ไม่ชน** · ฝังได้จึงไม่ต้องห่วงเครื่องผู้รับ · **`build_pptx.py` สลับให้อัตโนมัติทั้งเด็ค**เมื่อสไลด์ใดเข้าเกณฑ์ (>400 ตัวอักษร / >8 บรรทัด / ตาราง >40 ช่อง) · ปิด/บังคับด้วย `spec["dense"]: false/true` · 🔴 **ยกเว้นงานราชการ (rail=govt): ฟอนต์บังคับของ TOR ชนะกฎความแน่นเสมอ** — ไม่สลับอัตโนมัติ ต้องประกาศ `dense: true` เอง |
| **DOCX** | ⚠️ มือไม่ได้ | `IBM Plex Sans Thai Looped` + **PDF companion** | ฝังด้วยมือ = Word ปฏิเสธ (§2B.1) |
| **XLSX ทั่วไป** | ❌ **ฝังไม่ได้** | `IBM Plex Sans Thai Looped` + **PDF companion บังคับ** | PDF คือฉบับที่ลูกค้า "เห็น" · xlsx คือฉบับให้แก้ต่อ |
| **XLSX ที่รู้ว่าผู้รับ Windows** | ❌ | `Leelawadee UI` | มากับ Windows ทุกเครื่อง → ไม่ substitute |
| **HTML / webfont** | webfont | `IBM Plex Sans Thai Looped` | **OFL host ได้** · ⛔ Leelawadee เป็น MS proprietary **host ไม่ได้** |
| **PDF** | ✅ เสมอ | ตามต้นทาง | ฝัง 100% |
| ราชการ / TOR / e-GP | — | `TH Sarabun New` 16pt | รางราชการ · **TOR ระบุฟอนต์ = TOR ชนะ** |
| วิชาการ มจร./วารสาร | — | `TH SarabunPSK` | ข้อบังคับมหาวิทยาลัย **ชนะนโยบายเรา** |

### ⭐ ปัญหา "ลูกค้าไม่มีฟอนต์เรา" — แก้ตามลำดับนี้ ไม่ใช่ยอมลดคุณภาพไปใช้ fallback

**ขั้น 0 — ฝังฟอนต์ก่อนเสมอ (ทดสอบจริง 2026.08.04 ไม่ใช่อ้างเอกสาร)**

| ฟอร์แมต | ฝังได้ไหม | วิธี | หลักฐาน |
|---|---|---|---|
| **PPTX** | ✅ **ได้** | `_lib/embed_fonts_pptx.py` (Method B) | ทดสอบ: `ppt/fonts/font1-2.fntdata` 239 KB · `embedTrueTypeFonts="1"` ✅ · `validate_pptx_fonts.py` PASS |
| **DOCX** | ⚠️ สคริปต์ไม่ได้ | (ก) Word GUI: Preferences > Save > Embed fonts (ข) PDF companion | ประกอบ odttf เองครบตำรา → **Word ปฏิเสธทั้งไฟล์** (VFIN V02R02 §2B.1) |
| **XLSX** | ❌ **ไม่ได้เลย** | — | Microsoft รองรับ embed เฉพาะ Word/PowerPoint |
| PDF | ✅ เสมอ | — | ตรวจ `pdffonts` ทุกแถว emb=yes |

⇒ **PPTX/PDF จบตั้งแต่ขั้นนี้** — ฝังแล้วเครื่องปลายทางไม่เกี่ยวเลย ใช้ฟอนต์ที่สวยที่สุดได้เต็มที่

**ขั้น 1 — เหลือแค่ XLSX (+DOCX ที่ไม่ได้ฝัง) → ส่งฟอนต์ให้ลูกค้าติดตั้ง**

```bash
bash ~/.claude/agents/_lib/make_font_kit.sh "<โฟลเดอร์ deliverable>"
```
สร้าง `_Fonts/` = ไฟล์ฟอนต์ครบทุกน้ำหนัก + README ภาษาไทย (เหตุผล/วิธีติดตั้ง/ลิขสิทธิ์)

| | ลูกค้ามีอยู่แล้ว | **เราส่งให้ได้ไหม** |
|---|---|---|
| **IBM Plex Sans Thai Looped** | ❌ | ✅ **ได้** — SIL OFL · fsType 0x0000 · 7 น้ำหนัก = **0.8 MB** |
| Leelawadee / Tahoma / TH Sarabun New | ✅/บางส่วน | ⛔ **ไม่ได้** — proprietary (ได้แค่หวังว่าลูกค้ามี) |

> ⭐ **นี่คือจุดที่พลิกข้อโต้แย้ง "Leelawadee หาง่ายกว่า"** — ข้อโต้แย้งนั้นตั้งอยู่บนสมมติฐานว่า
> เราใช้ได้แค่ฟอนต์ที่ลูกค้ามีอยู่แล้ว · แต่ฟอนต์ราง **แจกได้ถูกกฎหมาย 0.8 MB** จึงไม่ต้องยอมลดคุณภาพ

**ขั้น 2 — PDF companion (บังคับสำหรับ .xlsx/.docx ที่ส่งลูกค้า · §3.2 E1)**
PDF ฝังฟอนต์ 100% → สิ่งที่ลูกค้า **เห็น** ถูกเสมอ แม้ไม่ติดตั้งอะไรเลย

**ขั้น 3 — fallback (ทางสุดท้ายจริง ๆ)**
```
fallbacks = ["Leelawadee UI"]     ← เหลือตัวเดียว
```
🔴 **ตัดออกแล้วทั้งคู่ (คำสั่ง user 2026.08.04):**
- ~~Tahoma~~ — ออกแบบปี 1994 · ไทย+อังกฤษด้วยกันไม่สวยจริง
- ~~Sukhumvit Set~~ — GAP ดีสุด 15.7% ก็จริง แต่เป็นฟอนต์ UI ของ Apple **โทนมนเป็นกันเอง ไม่ใช่โทนเอกสารทางการของเอกชน** + มีเฉพาะ macOS

> **ความจริงที่ต้องยอมรับ: ไม่มีฟอนต์ไทยที่ทั้งสวย ทั้งทางการ ทั้งมีบน Windows และ macOS**
> Tahoma เคยถูกใช้เพราะเป็น**ตัวเดียวที่ครอบ 2 OS** ไม่ใช่เพราะสวย
> ⇒ อย่าเสียเวลาหา fallback ที่ดีกว่า — **ไต่ขั้น 0-2 ให้ fallback ไม่ถูกใช้เลย**

---

## 3.0 ⭐⭐⭐ FONT POLICY — 2 ราง (V01R03 · LOCKED โดย user 2026.07.31)

> **ฐานหลักฐาน:** PDF สาธารณะ 45 ฉบับส่องด้วย `pdffonts`+span analysis (บริษัทไทย 30 · Big Four 15) · วัด metric จากไฟล์ฟอนต์จริง 9 ตระกูล · user ทดสอบสายตาเองในไฟล์ `ThaiFontTest_Excel_V01R01` · เอกสารเต็ม → `Output/iCE_Thai-Latin_Font-Policy_PROPOSAL_V01R01_2026.07.31.md`

### รางที่ 1 — งานเอกชน (proposal · deck · workbook · business case · demo)
```
ฟอนต์หลัก : IBM Plex Sans Thai Looped      ← ชื่อ family ที่ถูกต้อง (มี Looped ต่อท้าย)
ขนาด      : ไทย = อังกฤษ  ห้ามบวก pt      (cap 0.698 em · ละตินอยู่ในตัวเดียวกัน)
น้ำหนัก    : Thin/ExtraLight/Light/Regular/Medium/SemiBold/Bold — เลี่ยง Bold ใช้ SemiBold แทน
สำรอง     : Tahoma (ติดมากับ Win+Mac ทั้งคู่ — ใช้เมื่อคุมเครื่องปลายทางไม่ได้)
หลักฐาน   : user ทดสอบผ่าน · ปตท. ใช้จริงใน 56-1 One Report · SIL OFL = embed ถูกกฎหมาย
            ยอดวรรณยุกต์ 0.864 em เทียบกล่อง 1.239 → เหลือที่ว่าง 0.375 em (สบายที่สุดในกลุ่ม)
```

### รางที่ 2 — งานราชการ / TOR / e-GP / รัฐวิสาหกิจ
```
ฟอนต์หลัก : TH Sarabun New                 ← ไม่ใช่ PSK · ⛔ ห้าม IT๙ เด็ดขาด
ขนาด      : 16pt  (= ละติน 11-12pt · วัดได้ 0.714÷0.476 = ×1.47 → ตรงธรรมเนียมพอดี)
⚠ ระวัง    : ที่ว่างหัวเหลือแค่ 0.008 em (ยอด ้ 0.836 vs กล่อง 0.844)
            → ต้องตั้ง row height / line spacing เผื่อเสมอ ห้ามใช้ค่า default
ข้อกฎหมาย : มติ ครม. 2553 + นร 0106/ว 2019 ผูกพัน**ส่วนราชการ** ไม่ผูกพันผู้ขาย
            → อ่าน TOR ก่อนเสมอ · TOR ระบุฟอนต์ = ทำตาม TOR (override นโยบายนี้)
เหตุผลคุณภาพ: ชั้นข้อความไม่พัง — สระอำ รอด 100% (ต่างจาก Angsana/Cordia/Browallia ที่สูญ 100%)
หลักฐาน   : PwC ทำเป็นทางการ self-host 4 น้ำหนักใน rebrand design system
```

### ⭐ ตัวเลือกที่อนุมัติเพิ่ม (V01R08 · 2026.08.04 — เลือกใช้ได้ ไม่ต้อง `--allow-font`)

```
Leelawadee · Leelawadee UI · Leelawadee UI Semilight   (ไทย+อังกฤษในตัวเดียว)
  ⭐ จุดแข็ง : ยอดวรรณยุกต์เตี้ยที่สุดในกลุ่ม (~0.74 em) = ปลอดภัยสุดเมื่อความสูงแถว/บรรทัดถูกบีบ
              + ติดมากับ Windows ทุกเครื่อง · fsType 0x0008 = embed ได้ถูกลิขสิทธิ์
  ⚠ ข้อแลก  : GAP ไทย-ละติน 27.3% (กว้างสุดในกลุ่ม) → ไทยปนอังกฤษบรรทัดเดียวจะเห็นไทยเล็กกว่า
              ถ้าเลือกใช้ ต้องเพิ่ม pt ให้ไทย · งานทั่วไปใช้ฟอนต์รางดีกว่า
  ที่ตั้ง    : /Library/Fonts/leelawad.ttf (ตัวธรรมดา) · Leelawui.ttf (ตัว UI)
```

**ตารางวัดจริงบนเครื่องนี้ — ก/H = ความสูง ก เทียบ cap H *ในฟอนต์เดียวกัน*** (ยิ่งใกล้ 1.000 ยิ่งไม่ต้องชดเชย):

| family | ก/H | ยอดไม้โท | GAP ไทยเล็กกว่าละติน |
|---|---|---|---|
| **IBM Plex Sans Thai Looped** | **0.811** | 0.924 | **18.9%** ← ราง private |
| IBM Plex Sans Thai | 0.799 | 0.866 | 20.1% |
| Noto Sans Thai | 0.782 | 0.840 | 21.8% |
| Tahoma | 0.769 | 0.805 | 23.1% ← fallback |
| Leelawadee / Leelawadee UI | 0.727 | 0.737 / 0.743 | 27.3% ← ตัวเลือกอนุมัติ |
| ~~Sarabun~~ | 0.837 | **0.957** | 16.3% ← **ถอดออก** |

> **ทำไม Sarabun GAP ดีที่สุดแต่ถูกถอด:** ตัวเลข ก/H ไม่ใช่เกณฑ์เดียว — Sarabun ยอดวรรณยุกต์
> **0.957 em สูงสุดในกลุ่ม** และขอที่ว่างแนวตั้ง 1.286 em มากสุด → เป็นตัวที่โดนบีบและชนหนักที่สุด
> เมื่อพื้นที่แนวตั้งไม่พอ ซึ่งคืออาการที่ผู้ใช้ทดสอบสายตาเองแล้วไม่ผ่าน (คำสั่งถอด 2026.08.04)

### ⛔ ถอดออกจากตัวเลือก (V5 — ไม่ใช่ blacklist แต่ห้ามเลือกใช้ในงานใหม่)
```
Sarabun (+ ทุกน้ำหนัก Light/Medium/SemiBold/ExtraBold/Thin/ExtraLight)
  เหตุผล: ยอดวรรณยุกต์ 0.957 em สูงสุด + ขอที่ว่าง 1.286 em มากสุด → โดนบีบหนักสุด
  ⚠ คนละตัวกับ  'TH Sarabun New'  (รางราชการ — ใช้ได้ปกติ)
              และ 'TH SarabunPSK' (ข้อบังคับ มจร./วารสาร — ใช้ได้ปกติ)
  ไฟล์เก่าที่ใช้อยู่ = rebuild ตอนมี revision ถัดไป (ไม่ต้องไล่แก้ย้อนหลังทั้งหมด)
```

### ⛔ BLACKLIST — ห้ามใช้ (พร้อมเหตุผลที่ตรวจสอบแล้ว)
```
TH Sarabun IT๙          — แปลงเลขอารบิก 1234 → เลขไทย ๑๒๓๔ เงียบ ๆ (หายนะในเอกสารราคา) ·
                          ประกาศชื่อตัวเองว่า "TH SarabunPSK" ใน name record → สลับกันเงียบ ·
                          ความกว้างตัวเลข +24% → ตารางเพี้ยน
                          ⚠ กปภ./สตง./กรมเจรจาฯ ใช้ฟอนต์นี้ใน TOR — ถ้าเจอ ต้องแจ้ง user ก่อน
Angsana New / AngsanaUPC \
Cordia New / CordiaUPC    } — ทำลาย สระอำ (ำ) ในชั้นข้อความ 100% → copy-paste/ค้นหา/index พัง
Browallia New / UPC      /    (วัดจริง: KPMG 0/81 · Deloitte 0/15 · EY 0/18 รอด) · UPC ยังไม่มีบน macOS
EucrosiaUPC / JasmineUPC — ตระกูลเดียวกัน + ไม่ได้ติดตั้งบนเครื่องนี้
Calibri / Aptos / Arial  — ไม่มี glyph ไทยเลย (Aptos ประกาศ script tag แค่ Cyrl/Grek/Latn) →
                          ทุกตัวอักษรไทยตกไป fallback ที่ไม่ชดเชยขนาด = ต้นเหตุ "ไทยเล็กกว่าอังกฤษ"
Microsoft Sans Serif     — ไม่มี Bold จริง + ที่ว่างวรรณยุกต์ = 0 (worst-case ink = กล่องพอดีเป๊ะ)
Sarabun (Google)         — ไม่ใช่ blacklist แต่ user ปฏิเสธจากการทดสอบสายตา:
                          ยอดวรรณยุกต์ 0.957 em สูงสุดในกลุ่ม + ขอที่ว่าง 1.286 em มากสุด
                          → โดนบีบหนักที่สุดเมื่อพื้นที่แนวตั้งไม่พอ · ใช้ได้เมื่อคุม row height ได้เต็มที่
⚠ ชื่อชนกัน: "Sarabun" ≠ "TH Sarabun New" — คนละฟอนต์ ขนาดต่าง 47% (cap 0.700 vs 0.476)
            ระบุผิดตัว = เอกสารเพี้ยนทั้งฉบับ
```

### กติกาข้ามฟอร์แมต
```
① SINGLE-FAMILY FIRST — ใส่ฟอนต์ตัวเดียวทุก slot (latin/ea/cs หรือ ascii/hAnsi/eastAsia/cs)
   หลักฐาน: บริษัทไทย 30 ฉบับ **ไม่มีฉบับไหนจงใจจับคู่ 2 ตระกูลสำหรับเนื้อความ**
② จับคู่ 2 ตระกูลเมื่อลูกค้าบังคับ Latin brand font เท่านั้น → ชดเชยขนาดตาม D3 สูตร cap-ratio
   (Big Four ทำแบบนี้ทุกราย ตั้งไทยใหญ่กว่า 1.18-1.77× — เพราะไม่มีฟอนต์ไทยของแบรนด์ตัวเอง)
③ APPROVED SET เดียวทั้งชุดเอกสาร (deck+docx+xlsx ของงานเดียวต้องตรงกัน — ลูกค้าเห็นเป็นชุด)
   ⚠ V01R11: กติกานี้คุม**งานที่เริ่มจากศูนย์** — งานต่อยอด template เดิม ดูข้อ ⑤ (นโยบายชนะความสม่ำเสมอ)
⑤ 🔴 TEMPLATE-BASE BUILD (คำสั่ง user 2026.08.05 · เคส VFIN MA-AMS-CR): งานที่สร้าง**ต่อยอด
   template/เด็คเดิม** (รวมแทรกสไลด์ใหม่ · edit บน valid base) → **ใช้ฟอนต์ตามนโยบายปัจจุบัน
   (ราง/ตัวเลือกอนุมัติ) เป็นค่าเริ่มต้น — ห้ามสืบทอดฟอนต์ของ template โดยอัตโนมัติ**
   · ฟอนต์ template ใช้ได้**เฉพาะ user สั่งชัดเจน** ("ใช้ font ตาม template") → บันทึก
     `font_override_reason: "user สั่งใช้ font ตาม template"` ใน spec + จดใน QA-log
   · agent **ห้ามออก --allow-font ให้ตัวเอง**ด้วยเหตุผลความสม่ำเสมอของเด็คเดิม
   · หน้าที่ตอน PLAN-CARD: แจ้ง user ว่าสไลด์ใหม่จะฟอนต์ต่างจากของเดิมในเด็คเดียวกัน (mixed-font
     ชั่วคราว) จนกว่าเด็คจะ migrate ทั้งใบ — user เลือกรับ หรือสั่ง "ใช้ font ตาม template" ตรงนั้น
   · ที่มา: เคส VFIN 2026.08.05 — สไลด์ใหม่บนเด็ค Compile คง Sarabun (ฟอนต์ที่ถอดออกแล้ว)
     โดยอ้างความสม่ำเสมอของ template ทั้งที่ user ไม่ได้สั่งเรื่องฟอนต์ → user พลิกค่าเริ่มต้น
④ ชื่อ family ต้องเป็นชื่อจริงจาก name table — ห้ามเติม subfamily ต่อท้าย
   ❌ "IBM Plex Sans Thai Regular"  ✅ "IBM Plex Sans Thai Looped"
   (เคสจริง 2026.07.31: ไฟล์ PWA TOR Matrix ใส่ชื่อผิด → Excel substitute เงียบ → ฟอนต์ปน 3 ตัว)
```

## 3.1 DOCX — TRI-SLOT ฉบับ WordprocessingML (คู่แฝด D1)
```
ทุก run set <w:rFonts> ครบ 4 attributes (คู่แฝดของ latin/ea/cs):
  <w:rFonts w:ascii="Open Sans" w:hAnsi="Open Sans"     ← EN/Latin
            w:eastAsia="Open Sans" w:cs="Sarabun"/>      ← EA + THAI ⭐
+ ขนาดมี 2 slot แยก (คู่แฝด D3): <w:sz> = Latin (half-points) · <w:szCs> = Thai ⭐
  → TH +1-2pt ทำผ่าน szCs (เช่น sz=22 → szCs=26 คือ 11pt/13pt)
+ styles.xml ต้อง set ที่ราก ไม่ไล่แก้ราย run:
  - docDefaults/rPrDefault → rFonts ครบ 4 + sz/szCs
  - Normal + Heading1-3 + Table styles → rFonts ครบ 4 ทุก style ที่ใช้
  - run ที่ไม่มี direct formatting จะ inherit ถูกต้องเอง = สม่ำเสมอทั้งไฟล์
⭐ W1-W3 (V01R03 — จากสเปกจริง):
W1 set w:ascii + w:hAnsi + w:cs **เป็นฟอนต์ตัวเดียวกัน** (นโยบาย single-family §3.0)
   เหตุผล: สเปก Microsoft 2 ฉบับ**ขัดกันเอง**ว่าไทยใช้ slot ไหน — ECMA-376 บอก cs (จำแนกตาม
   Unicode range) แต่ MS-OI29500 ซึ่งบันทึก algorithm จริงของ Word **ไม่มี Thai ในตาราง**
   และสั่งว่า "range ที่ไม่อยู่ในตารางให้ใช้ hAnsi" → ตั้งเหมือนกันหมด = คำถามนี้ไร้ความหมาย
   ⚠ w:cs ไม่ตั้ง → Word ถอยไป Times New Roman (ไม่มีไทย) → substitute เงียบเป็น Angsana/Cordia
W2 ⭐ w:bCs + w:iCs ทุกครั้งที่มี w:b / w:i
   เหตุผล: w:b และ w:i **ไม่มีผลกับ complex script** → นี่คือสาเหตุ "หัวข้อไทยไม่หนา แต่อังกฤษหนา"
W3 🔴 ห้าม lineRule="exact" ในย่อหน้าที่มีไทย
   ECMA ST_LineSpacingRule: exact = สูงเท่าที่กำหนดเป๊ะ "ถ้าเนื้อหาใหญ่เกิน จะถูกตัด"
   → วรรณยุกต์ตายก่อนเพื่อน · ใช้ "auto"/multiple แทน
+ ⚠ ลบ w:cstheme / w:asciiTheme / w:hAnsiTheme / w:eastAsiaTheme ออกจาก styles.xml และทุก run
   (theme attribute ที่ระดับ style จะ override docDefaults ของเรา)

NORMALIZATION (D2 ใช้ตรง ๆ): enumerate ทุก w:rFonts ทั้ง document.xml+styles.xml
  → collapse variant/นอก approved set → report before/after
VALIDATOR DOCX เพิ่ม: ✓ ทุก run มี cs font ที่เป็น Thai-capable
  ✓ ไม่มี "Calibri"/"Cambria" เหลือ (python-docx default leak)
  ✓ szCs ≥ sz ทุกจุดที่มีข้อความไทย ✓ styles.xml rPrDefault ครบ 4 slots
EMBED ⚠ (แก้ V01R02 — พิสูจน์แล้วว่า "ทำได้เหมือน pptx" = ผิด): DOCX ห้ามฝัง font parts (odttf) ด้วยมือ
  — Word ปฏิเสธทั้งไฟล์ (เคสจริง VFIN V02R02 §2B.1) · flag settings ต้องวางถูกลำดับ CT_Settings (§2B.1) ·
  ทางที่ใช้ได้จริง: (ก) user ให้ Word GUI embed เอง (Preferences>Save) หรือ (ข) PDF companion (Method C) ⭐ default
```

## 3.2 XLSX — ⭐ เขียนใหม่ V01R03 (E1-E6 · จากหลักฐาน Microsoft + เคสจริง PWA TOR Matrix)

> **ทำไม Excel ยากที่สุดใน 3 ฟอร์แมต:** (ก) เซลล์มีฟอนต์ได้**ชื่อเดียว** ไม่มี slot ไทยแยกเหมือน pptx/docx — ยืนยันจาก MS-XLSX + `openpyxl.styles.fonts.Font.__elements__` ไม่มี cs/ea/latin (ข) **ฝังฟอนต์ไม่ได้เลย** (ค) ไม่มีสูตรทางการแปลง pt → ความสูงแถว (Microsoft บอกขึ้นกับแอปตาม ISO 29500 §18.3.1.73)

```
พื้นฐาน:
  • เซลล์ที่มีไทย (แม้ปนนิดเดียว) → ฟอนต์ Thai-capable ตาม §3.0 · ห้ามหวังพึ่ง fallback
  • ทำผ่าน NamedStyle (header/body/number/thai-note) — ห้าม set ราย cell แบบ ad-hoc
  • theme1.xml minorFont/majorFont ตั้งเป็น approved set (กัน Calibri/Aptos โผล่ในกราฟ/element ใหม่)
  • ⚠ tri-slot (latin/ea/cs) มีอยู่ใน .xlsx จริง แต่**เฉพาะ DrawingML** (กราฟ/shape/text box)
    — ใช้กับ "ค่าในเซลล์" ไม่ได้ · เอา discipline จาก pptx มาใช้ตรง ๆ = ทำงานเงียบ ๆ แต่ไม่มีผล

E1 ⛔ EXCEL ฝังฟอนต์ไม่ได้ทุกแพลตฟอร์ม (Microsoft รองรับ embed เฉพาะ Word/PowerPoint)
    → .xlsx ที่ส่งลูกค้า มี 2 ทางเท่านั้น:
      (ก) ใช้ฟอนต์ที่ลูกค้ามีแน่ (Tahoma) หรือ
      (ข) ⭐ แนบ PDF companion เสมอ (PDF ฝัง font 100% — ตรวจด้วย §3.3)
    → ไฟล์ภายใน/ไฟล์ทำงาน = ใช้ฟอนต์ตามนโยบายได้เต็มที่

E2 ⭐ ROW HEIGHT ตั้งชัดเจน ห้ามพึ่ง AutoFit
    สูตรที่ทดสอบแล้ว:  height = pt × 1.45 × จำนวนบรรทัด + 6
    เหตุผล: ไทยซ้อน mark ได้ 4 ชั้นบน + 2 ชั้นล่าง (Microsoft Thai shaping spec) ขณะละตินซ้อน 1 ชั้น
    → AutoFit คำนวณจากบรรทัดละติน = ที่ว่างไม่พอโดยโครงสร้าง
    ⚠ TH Sarabun New 16pt (ที่ว่างหัวเหลือ 0.008 em) → เผื่อมากกว่านี้ ทดสอบก่อนส่ง

E3 ⭐ vertical = "center" ทุกเซลล์ที่มีไทย
    เหตุผล: ค่าเริ่มต้นของ Excel = bottom → ยึดกล่องข้อความที่พื้นเซลล์ แล้วตัดส่วนเกิน**ด้านบน**
    ซึ่งคือที่อยู่ของวรรณยุกต์พอดี

E4 🔴 ห้าม merge cell ในแถวที่มีไทย + wrap
    Microsoft ยืนยัน: AutoFit ความสูงแถว **ถูกปิดใช้งาน** ในแถว/คอลัมน์ที่มี merged cell
    และ Wrap Text ก็ไม่ขยายแถวที่ merge → แถวโดนตัดโดยการออกแบบ
    ทางเลือกแทน merge: "Center Across Selection" (จัดกลางข้ามคอลัมน์โดยไม่ merge จริง)

E5 🔴 ห้ามใช้ "Shrink to fit" กับเซลล์ไทย
    มันย่อขนาดฟอนต์ → วรรณยุกต์เล็กลงอีก = แย่ที่สุดในบรรดา 4 วิธีที่ Microsoft เสนอ

E6 ตั้ง default font ของ workbook **ก่อน** คำนวณความกว้างคอลัมน์
    เหตุผล: ความกว้างคอลัมน์วัดเป็น "จำนวนตัวอักษรของ default font" (default 8.43)
    → เปลี่ยน default ทีหลัง = ทุกคอลัมน์ขยับเงียบ ๆ

VALIDATOR XLSX (→ §6 V1-V3):
  ✓ V1 ทุกชื่อฟอนต์ resolve ได้จริง  ✓ V2 ไม่มีตัวใน blacklist  ✓ ไม่มี Calibri/Aptos leak
  ✓ เซลล์ไทยทุกเซลล์ได้ฟอนต์ Thai-capable  ✓ เซลล์ไทย+wrap ทุกแถวมี row height ตั้งชัดเจน
  ✓ ไม่มี merged cell ในแถวที่มีไทย+wrap  ✓ ไม่มี shrink_to_fit บนเซลล์ไทย
```

## 3.3 PDF — EMBED-VERIFY เสมอ (ปลายทางของทุกฟอร์แมต)
```
PDF ที่ generate จาก pptx/docx (renderer ladder §7) หรือสร้างตรง:
  • ทุก font ต้อง EMBED ในไฟล์ — ตรวจด้วย: pdffonts OUT.pdf → คอลัมน์ emb = yes ทุกแถว
    (มี "no" = เครื่องปลายทางจะ substitute → layout/สระไทยพัง)
  • สร้าง PDF ตรง (reportlab/weasyprint): ลงทะเบียน TTF ทั้งคู่ Latin+Thai + fallback chain ชัดเจน
  • ห้ามมี font ชื่อ generic (Helvetica/Times) เหลือในงานไทย — สัญญาณ substitution
VALIDATOR PDF: ✓ pdffonts ทุกแถว emb=yes ✓ เปิดดู 1 หน้า sample สระ/วรรณยุกต์ไม่ลอย
```

## 3.5 ⭐ THAI WORD BREAKING — ตัดบรรทัดไม่ผ่ากลางคำ (V01R04 ใหม่ · คำสั่ง user 2026.07.31)

> **ปัญหา:** ไทยไม่มีช่องว่างระหว่างคำ → Office ตัดบรรทัดกลางคำเป็นประจำ (`ระบบบัญ` / `ชีแยกประเภท`, `ภาคผนว` / `ก`) · เคสจริง: ไฟล์ PWA TOR Matrix มี **47 จาก 261 เซลล์ไทย** เสี่ยงตัดกลางคำ
> **เครื่องมือ:** `~/.claude/agents/_lib/thai_wordbreak.py` (PyThaiNLP 5.3.4 · engine **`newmm`** เท่านั้น — `longest` แปลงอังกฤษเป็นตัวพิมพ์เล็กทิ้ง SAP→sap)

```
⭐ 3 ชั้น — ใช้ชั้นบนก่อนเสมอ เพราะชั้นล่างแลกด้วยการแก้ข้อความ

T1 LANG-TAG (ดีที่สุด — ไม่แตะข้อความเลย)
   ตั้ง language ให้ engine ของ Office ตัดคำเอง (มี dictionary ไทยในตัว):
     DOCX : <w:lang w:bidi="th-TH"/> ใน rPr ของ run ที่มีไทย
     PPTX : <a:rPr lang="th-TH" …> บน run ที่มีไทย (python-pptx: run.font.language_id)
     XLSX : ❌ ไม่มี — cell ไม่มี slot ภาษา (ต้องใช้ T2/T3)
   ✅ Ctrl+F ยังหาเจอ · copy-paste สะอาด · ไม่มีอักขระซ่อน

T2 QA-ONLY (ตรวจอย่างเดียว ไม่แก้ — ⭐ ค่าเริ่มต้นของ .xlsx)
   ใช้ PyThaiNLP ทำนายว่าที่ความกว้างนี้ บรรทัดจะผ่ากลางคำตรงไหน → **แก้ด้วยการขยายคอลัมน์
   หรือปรับข้อความ** ไม่ใช่แก้ตัวอักษร
     python3 _lib/thai_wordbreak.py --audit FILE.xlsx [--col C] [--width 45]
     python3 _lib/thai_wordbreak.py --check "ข้อความ" --width 30
   ⚠ การวัดความกว้างต้องไม่นับสระบน/ล่าง+วรรณยุกต์ (combining mark กินความกว้าง 0)
     — helper คำนวณให้แล้วใน display_width()

T3 ZWSP INJECTION (ทางสุดท้าย — แลกด้วยราคาที่ต้องรู้ตัว)
   แทรก U+200B ที่ขอบคำ → บังคับจุดตัดบรรทัด
     python3 _lib/thai_wordbreak.py --zwsp "ข้อความ"   /  --strip เพื่อถอดคืน
   🔴 **ราคา: Ctrl+F หาคำที่คร่อม ZWSP ไม่เจอ** (ค้น "ระบบบัญชี" ในข้อความที่มี ZWSP คั่น = ไม่เจอ)
      + copy-paste ติดอักขระซ่อนไปด้วย
   ใช้เมื่อ: (ก) .xlsx cell ที่ T1 ใช้ไม่ได้ **และ** ขยายคอลัมน์ไม่ได้แล้ว
            (ข) layout สำคัญกว่า search (เช่น หัวตารางสั้น ๆ ที่ต้องสวย)
   ❌ ห้ามใช้กับ: เนื้อความยาวที่ลูกค้าจะ copy ไปใช้ต่อ · เอกสาร TOR/e-GP ที่ถูก index
```

**กติกาบังคับ:** ทุก build ที่มีไทย+wrap → **รัน T2 audit ก่อนส่งเข้า ④** · เจอเสี่ยง → แก้ตามลำดับ ① ขยายคอลัมน์ ② ปรับข้อความ ③ ZWSP (ต้องบอก user ว่าแลกอะไร)

## 3.4 กติการ่วมทุกฟอร์แมต
- **APPROVED SET เดียวทั้งเอกสารชุดเดียวกัน** (deck+docx+xlsx ของงานเดียวต้อง family ตรงกัน — ลูกค้าเห็นเป็นชุด)
- Normalization report before/after ทุก build · ภาษาไฟล์ถามก่อนตาม H6

---

# §4 — Other Build Lessons + Build-vs-Edit + γ1/γ3 (คงคำต่อคำ)

## 4.1 Other Build Lessons (4 projects)
```
xlsx: LIVE formula (=NPV(rate,CF1:CF10)/=IRR + cached <v> + fullCalcOnLoad) · no external-link (flatten) ·
      omit calcChain (Excel rebuild) · Thai via sharedStrings · freeze header + data-validation dropdowns
Ordered section manifest: section#/divider/footer/filename จาก 1 list (กัน section drift)
Image hygiene: downsample ≤150dpi (กัน deck 45-58MB) · strip ~$lock + .DS_Store ก่อน zip
docProps: overwrite creator=iCE (กัน "Steve Canny" python-pptx default leak)
```

## 4.2 Build-vs-Edit Guard + Pipelines + γ1/γ3 + CLOSED-LOOP
```
RULE (numeric): NEW deck OR >5 slides change → BUILD from spec (full pipeline)
                ≤5 slides edit บน VALID base → EDIT via python-pptx API (รักษา structure)
                (rebuild-from-source = re-introduce corruption → ห้าม edit แบบ rebuild)
BUILD PIPELINE: Pre-Flight → build per-section (18 lessons + D1-D4) → merge+page+font-embed → STRICT VALIDATOR → ส่ง ④
EDIT PIPELINE:  open VALID base (PowerPoint-Repaired ถ้ามี) → python-pptx API edit → re-verify corruption → ส่ง ④

⭐ γ1 SELF-TEST (ด่านศูนย์): Strict Validator = Collision + Overflow (Y-budget 16:9 6.858m H)
  → เจอทับ/ล้น → แก้จบในตัว (QA/User ไม่ควรเจอ overflow/collision)
⭐ γ3 CANONICAL: derived slide (value/summary/timeline อ้างตัวเลข) → ใช้ตัวเลขจาก key_facts canonical เดียว
⭐ CLOSED-LOOP: หลังแก้ ระบุ "แก้ issue ไหนบ้าง" (id + สิ่งที่ทำ) → tick [FIXED] ใน QA-log
```

## 4.3 Reusable Layout Patterns (`~/.claude/agents/_lib/patterns/`)
```
_lib/patterns/gantt-timeline.md — Project Timeline/Gantt (สกัดจาก EPM deck จริง ผ่านงาน+User อนุมัติ)
งานตรง pattern ที่มี → อ่าน spec ใน _lib/patterns/ ก่อน → คงรูปแบบที่ผ่านงานจริง
```

---

# §5 📋 DOCUMENT-TYPE → SKILL ROUTING MATRIX (อ่านก่อน build ทุกครั้ง — คงคำต่อคำ)

| ประเภทเอกสาร | Default format | Design skill (โหลด) | Build engine | ภาษา default |
|---|---|---|---|---|
| **Proposal / ข้อเสนอ** | .docx หรือ deck | b2b-slide-designer + b2b-presentation-creator | pptx/docx | ถาม (H6) มัก Bilingual |
| **Pitch deck / นำเสนอลูกค้า** | .pptx (หรือ html demo) | slide-designer + presentation-creator + pre-flight-deck | `_lib/build_pptx.py` หรือ HTML | Bilingual |
| **Board paper / Executive briefing** | .pptx | slide-designer (Cobalt/iCE-Propose) + design-principles | `_lib/build_pptx.py` (embed) | ตามผู้บริหาร |
| **SoW** | .docx | presentation-creator (เนื้อ) + docx | `_lib/build_docx.py` | ตาม contract |
| **Business case / ROI narrative** | .docx + .xlsx | presentation-creator + design-principles | docx + xlsx | Bilingual |
| **ROI / TCO workbook** | .xlsx | (table discipline) | `_lib/build_xlsx.py` | ตัวเลข EN, label ตามผู้อ่าน |
| **TOR / RFP response (ราชการ/e-GP)** | .docx + .pptx | slide-designer (iCE-CI) + advisor-govt-gfmis (เนื้อ) | docx/pptx (TH SarabunPSK→Sarabun, embed) | **TH** (ราชการ) |
| **QBR / EBR deck** | .pptx | slide-designer (Whiteboard/Cobalt) + sales-pipeline-report | `_lib/build_pptx.py` | ตามลูกค้า |
| **Dashboard / analytics** | HTML (interactive) | sales-pipeline-report | pandas/matplotlib → HTML | Bilingual |
| **Demo / microsite / แชร์ลิงก์** | **HTML deck** | presentation-creator (ref 13) + slide-designer §5.6 | `scripts/build_html.py` | ตาม audience |
| **แปลง .pptx เดิม → web** | HTML | presentation-creator (ref 13 §4) | `scripts/extract-pptx.py` → build_html | คงของเดิม |
| **บทความวิชาการ (persona=สมนึก)** | .docx | academic skill ตามวารสาร (AGJ/soc-sci/phd-mcu/jpspa/phd-buddhist) | `_lib/build_docx.py` | TH academic |

**กฎเสริม (ทุกแถว):** Font ทุก customer-facing → slide-designer §5.5.1 single-source → D1-D4 (pptx) / §3.1 (docx) / §3.2 (xlsx) · design-principles.md (20 rules) = format-agnostic · ภาษาไฟล์ถามก่อน (H6 เว้น 3 ข้อยกเว้น) · ไม่แน่ใจ format/ประเภท → ถาม · AI imagery → higgsfield (หลัก) / gemini (fallback) — preflight cost ก่อน · **build tools = `~/.claude/agents/_lib/build_*.py` (SSOT — อยู่ที่เดิม)**

---

# §6 ⭐ VALIDATION BUDGET (Hard Rule กัน validation loop กิน token — เคสจริง Viriyah 2026.07.14 transcript 1.48MB)

1. **SINGLE-PASS:** validator ครบชุดตาม format/tier รัน **1 ครั้งเดียว** → PASS ทุกข้อ = **จบ ส่งเข้า ④ ทันที** — ห้าม re-run/re-render/re-parse "เพื่อความชัวร์"
2. **FAIL → แก้ → re-check เฉพาะข้อที่ fail (delta)** · cap 2 รอบ → ยัง fail = หยุด รายงาน diagnostic ไม่ฝืนวน
3. **SCALE-TO-SIZE:** artifact เล็ก (xlsx ≤~30 แถว · deck ≤5 slides · docx ≤3 หน้า) = ตรวจโครงสร้าง+ค่าพอ ไม่ render ภาพทุกหน้า
4. **TOKEN DISCIPLINE:** parse/ตรวจด้วย script ที่คืนผลเป็น**ตัวเลข/counts** — ห้าม dump raw XML เข้า context (transcript บวม = ทำผิดข้อนี้)
- **PPTX:** γ1 Strict Validator (§1 D4 ทุก ✓) · **XLSX:** formula-integrity + §3.2 E1-E6 · **DOCX:** §3.1 W1-W3 + academic → citation-verbatim · **HTML:** เปิด browser/screenshot จริง · **PDF:** pdffonts emb=yes
- ทุก format: validator report เป็น**ตัวเลขจริง** ("collision 0 · overflow 0 · fonts 4/4 embedded") — ห้ามรายงาน "ผ่านแล้ว" ลอย ๆ

## ⭐ V1-V3 FONT VALIDATORS (V01R03 ใหม่ — บังคับทุก build ที่มีไทย · รันก่อนส่งเข้า ④)

> **ทำไมเพิ่ง"มี":** 2026.07.31 พบไฟล์ `PWA_ERP_TOR_System-Module-User-Matrix_V01R04` ระบุฟอนต์ `IBM Plex Sans Thai Regular` ซึ่ง**ไม่มี family ชื่อนี้อยู่จริง** → Excel ทิ้งแล้ว substitute เงียบ → ฟอนต์ปน 3 ตัวในไฟล์เดียว → user เห็นเป็น "วรรณยุกต์เพี้ยน ขนาดไม่เท่ากัน" · **ระบบเดิมไม่มีตัวตรวจใดจับได้เลย**

```
V1 ⭐⭐⭐ FONT-NAME RESOLUTION (สำคัญสุด — ตัวที่จะดักบั๊กข้างบน)
   ทุกชื่อฟอนต์ในไฟล์ต้อง match family name จริงจาก name table (nameID 1) ของฟอนต์ที่ติดตั้ง
   แบบ **exact string** — ไม่ใช่ substring ไม่ใช่ fuzzy
   วิธีตรวจ: enumerate ฟอนต์ที่ติดตั้ง → fontTools อ่าน getDebugName(1) → เทียบ set
   ❌ FAIL ทันทีถ้าเจอชื่อที่ resolve ไม่ได้ — ห้ามปล่อยผ่านด้วยเหตุผลว่า "น่าจะได้"
   กับดักที่พบบ่อย: เติม subfamily ต่อท้าย ("... Regular"/"... Bold") · สะกดต่าง · เว้นวรรคเกิน
   หมายเหตุ: น้ำหนักนอก RIBBI เป็น **family แยก** (เช่น "IBM Plex Sans Thai Looped SemiBold"
   เป็นคนละ family กับ "IBM Plex Sans Thai Looped") → ต้องระบุให้ตรงกับที่ติดตั้งจริง

V2 BLACKLIST REJECT — reject ทันทีถ้าพบใน artifact ที่มีไทย:
   TH Sarabun IT๙ · Angsana* · Cordia* · Browallia* · Eucrosia* · Jasmine* ·
   Microsoft Sans Serif · และ Calibri/Aptos/Arial บนเซลล์/run ที่มีอักขระไทย
   (เหตุผลรายตัว → §3.0 BLACKLIST)

## ⭐⭐ จุดตรวจเดียว ทุกฟอร์แมต — `audit_fonts.py` (V01R07 · 2026.08.04)

```bash
python3 ~/.claude/agents/_lib/audit_fonts.py [--rail private|govt] [--allow-font NAME]... FILE...
```
| ฟอร์แมต | ตรวจอะไร |
|---|---|
| `.xlsx` | delegate `build_xlsx.audit()` → V1/V2/V4 + E2-E5 + T2 word-break |
| `.pptx` | ฟอนต์บน run ที่มีไทยจริง (`a:cs`/`a:latin`) + **D1: run ไทยที่ไม่มี `<a:cs>`** |
| `.docx` | `w:cs`/`w:ascii` + **W1: run ไทยไม่มี `w:cs` และ docDefaults ก็ไม่ได้ตั้ง** (inherit = ผ่าน) |
| `.html` | ชื่อแรกของทุก `font-family` stack |
| `.pdf` | ทุกแถว `emb=yes` + ไม่มี fallback Linux/LO + **พบฟอนต์ของรางจริง** (V1 ข้าม — ชื่อถูก subset) |

**หลักที่ยึด:** ตรวจเฉพาะฟอนต์ที่ **ถูกใช้กับข้อความไทยจริง** ไม่ใช่ที่ประกาศใน theme table
(sweep แรกของเคสนี้นับ Cordia/Angsana จาก theme ได้ 540 ไฟล์ = false positive ล้วน)
`--allow-font` ใช้กับ: TOR บังคับ · ข้อบังคับวารสาร/มหาวิทยาลัย · ไฟล์ที่ลูกค้าส่งมา (ไม่ใช่ของเราสร้าง)

---

V4 ⭐⭐ RAIL CONFORMANCE (V01R06 · 2026.08.04 — ด่านที่ "หายไป" จนเกิดเคสจริง)
   ฟอนต์ต้องเป็นตัวที่ **ราง** กำหนดใน §3.0 (หรือ fallback ของรางนั้น) — ไม่ใช่แค่ "มีจริง + ไม่ blacklist"
     python3 _lib/build_xlsx.py [--rail private|govt] [--allow-font "ชื่อ"]... --audit FILE
   🔴 **ทำไมต้องมี** — V1/V2 ตอบคนละคำถามกับนโยบาย:
       V1 ถาม "ชื่อนี้ resolve ไหม"   → Sarabun resolve ✅
       V2 ถาม "อยู่ blacklist ไหม"    → §3.0 เขียนเองว่า Sarabun **ไม่ใช่** blacklist ✅
       → ฟอนต์ที่ **ถูกต้องทางเทคนิคแต่ผิดนโยบาย** ลอดทั้งสองด่านโดยไม่มีใครทัก
   เคสจริง 2026.08.04: `PWA_ERP-HCM_TCO-Breakdown-3Y_V01R22` build วันเดียวกับที่นโยบายบังคับใช้อยู่แล้ว
   ยังออกมาเป็น Sarabun และ validator ขึ้น **✅ PASS** — user เป็นคนจับได้ ไม่ใช่ระบบ
   **ต้นเหตุที่แท้จริง (สำคัญกว่าตัวด่าน):** นโยบายอยู่ใน RAILS ซึ่งถูกเรียกเฉพาะ `build_xlsx.py build()`
   ที่อ่าน spec.json — แต่ deliverable ส่วนใหญ่สร้างด้วย **build script เขียนมือ** ที่ตั้ง `FONT = "..."`
   เองเป็นค่าคงที่แล้วสั่ง openpyxl ตรง ๆ → **bypass ตาราง RAILS ทั้งตาราง**
   ⇒ กติกาใหม่: build script เขียนมือทุกตัวต้อง `from build_xlsx import RAILS` แล้วอ่านฟอนต์จากราง
      ห้าม hard-code ชื่อฟอนต์ · และต้องรัน `--audit` ก่อนส่งเข้า ④ ทุกครั้ง
   `--allow-font` ใช้เมื่อ: TOR บังคับฟอนต์ · ไฟล์ที่ลูกค้าส่งมา (ไม่ใช่ของเราสร้าง)

V3 สระอำ INTEGRITY (เฉพาะ output ที่เป็น PDF หรือจะถูก copy-paste)
   export PDF → สกัดข้อความ → นับ U+0E33 (ำ) กับคู่ประกอบ U+0E4D+U+0E32 (ํา)
   ✓ ผ่าน: เจอ ำ หรือ ํา ครบตามจำนวนในต้นฉบับ
   ❌ FAIL: หายกลายเป็นช่องว่าง = ฟอนต์ตระกูล UPC (แก้ไม่ได้ ต้องเปลี่ยนฟอนต์)
   หลักฐานที่มาของกฎ: KPMG 0/81 · Deloitte 0/15 · EY 0/18 รอด vs TH Sarabun New 409/409 รอด
```

---

# §7 🖨️ RENDERER LADDER (host นี้ — พิสูจน์จริง VFIN 2026.07.17 · ใช้เมื่อถูกสั่ง preview เท่านั้น)

```
🔴🔴 กฎข้อ 0 (V01R05 — บทเรียน Akara 2026.08.01): ⛔ ห้ามเรียก `soffice` เปล่า ๆ จาก PATH เด็ดขาด

   บนเครื่องนี้ `which soffice` → /opt/homebrew/bin/soffice → **shim ของ codex runtime**
   ("[soffice-headless V01R01] runtime=~/.cache/codex-runtimes/.../override/soffice")
   shim **มองไม่เห็น /Library/Fonts → แทนฟอนต์ทั้งไฟล์ แล้วรายงานว่าสำเร็จ** (ไม่มี error)

   หลักฐาน differential test (ไฟล์เดียวกัน render 2 ทาง):
     shim → NotoSans · FrankRuhlHofshi (ฟอนต์ฮีบรู!) · LinuxLibertineG   — IBM Plex 0 ตัว
     จริง → IBMPlexSansThaiLooped-Regular/Bold                            ✅
   ผลกระทบที่แพงที่สุด: **QA render ด้วย shim → รายงานตัวอักษรล้น/เพี้ยนเป็นชุด = false positive
   ทั้งหมด** → ทีมไล่แก้ layout ที่ไม่ได้พัง (เสียเวลาทั้งรอบ)

⭐ ใช้ helper เสมอ — มันหา binary ตัวจริงให้ + ตรวจฟอนต์หลัง render ให้ในตัว:
   bash ~/.claude/agents/_lib/render_pdf.sh <file> [outdir] --expect "IBMPlexSansThaiLooped"
   bash ~/.claude/agents/_lib/render_pdf.sh --which     # ดูว่าเครื่องนี้จะใช้ตัวไหน

① LibreOffice **absolute path** + fresh profile (helper ทำให้แล้ว · ถ้าทำมือ):
   /Applications/LibreOffice.app/Contents/MacOS/soffice --headless \
     -env:UserInstallation=file:///tmp/lo-run --convert-to pdf --outdir . "ไฟล์.pptx"
   (ไม่ใส่ fresh profile = พิมพ์ "convert..." แต่ไม่เขียนไฟล์เงียบ ๆ)
   วิธียืนยันว่าได้ตัวจริง: `--version` ต้องขึ้นต้น "LibreOffice " — shim จะขึ้นอย่างอื่น
② PowerPoint AppleScript save-as-PDF (fidelity สูงสุด): dest ต้องเป็น POSIX file (string เฉย ๆ = "done" แต่ไม่เขียน) ·
   sandbox เขียน /private/tmp ไม่ได้ → 🔴 V01R12: ใช้ staging `~/Documents/.ice-staging/` เท่านั้น
   แล้ว**ย้ายเข้า `<โฟลเดอร์งาน>/_build/_qa/` ทันทีในคำสั่งเดียวกัน** (`osascript … && mv … && rmdir`)
   — ข้อความเดิม "save ใต้ ~/Documents แล้วย้าย" คือต้นตอขยะ `_qa_aris_vfin/` + `qa_s6_*.pptx`
   ที่ user เจอใต้ ~/Documents (2026.08.05): agent ทำครึ่งแรก ลืมครึ่งหลัง → กติกาเต็ม `reference/file-hygiene.md`
③ PowerPoint MCP = เช็ค "เปิดได้/ไม่ขึ้น Repair" เท่านั้น (export_pdf = false success ห้ามใช้ render)
④ ไม่มีทางไหนได้ = NOT-VERIFIABLE-ON-HOST บอกตรง ๆ — ห้ามหลุดไป loop สอบสวน

⭐⭐ POST-RENDER FONT VERIFY (บังคับทุกครั้งที่ render — ด่านที่จับ renderer regression ทุกชนิด):
   pdffonts OUT.pdf → ✓ ทุกแถว emb=yes  ✓ **เจอฟอนต์ที่เราตั้งจริง**
   🔴 เจอ LinuxLibertine / FrankRuhl / DejaVu / Liberation = สัญญาณว่า renderer มองไม่เห็นฟอนต์ระบบ
      → หยุด ตรวจ `render_pdf.sh --which` ก่อนสรุปว่าไฟล์พัง
   หลักการ: **ผลตรวจที่ได้จาก renderer ผิดตัว = หลักฐานปลอม** — เช็ค renderer ก่อนโทษไฟล์เสมอ

แล้ว pdftoppm -r 100..130 เป็น PNG รายหน้า · กฎเหล็ก: ls ยืนยันไฟล์เกิดจริงทุกขั้น
```

---

# §8 ⭐ CODEX/OPENROUTER OPTION (คงตามคำสั่ง user — advisor/QA/idea ทางเลือก)

- ผู้ build (L0/persona ใด ๆ) ใช้ Codex/OpenRouter เป็น**ที่ปรึกษาทางเลือก**ได้ตาม codex_scope ที่ user เปิด: review โค้ด build ก่อนรันงานใหญ่ · ภาษาใน artifact ก่อนส่ง ④ · ไอเดีย design
- **กติกาเหล็ก: ผู้ตรวจภายนอกว่าผ่าน ≠ ข้าม Strict Validator/γ1 — ของตัวเองรันเสมอ (เสริม ไม่แทน)** · QA จริงยังเป็นอริส
- L0 เรียกเองใน loop หลัก = เสถียร (แก้ pattern เดิม "subagent หลุดตอนกำลังเรียก advisor") · **เจนนี่-shell ตั้ง `codex_scope: none` เสมอ** (บทเรียน Viriyah team-memory)
- Contract = skill `claude-codex-bridge` / `openrouter-bridge` (ONE-HOME)

---

*Skill: ice-doc-builder **V01R01** | 2026.07.17 | สกัดจาก deliverable-gen-agent V02R08 (§4→§1-2·4 · §5→§5 · E4→§0.3+§6) คำต่อคำ + ใหม่: §3 FONT ข้ามฟอร์แมต docx/xlsx/pdf + §0 CONTRACT ICE_BUILD=pipeline + §7 Renderer Ladder + §8 Codex Option*
*ใช้โดย: L0 (กัปตัน/คิม/สมนึก personas) · deliverable-gen-agent shell · QA โดยอริสบังคับทุกกรณี (Producer≠Checker)*
