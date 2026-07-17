---
name: ice-doc-builder
description: "iCE Document Build Craft — ความรู้ build .pptx/.docx/.xlsx/PDF/HTML ระดับ specialist (Build Discipline D1-D4 tri-slot Thai+EN font, 18 PPTX lessons, Method B font-embed, Strict Validator, SAVE-FIRST, VALIDATION BUDGET, renderer ladder) ที่ย้ายมาจาก deliverable-gen-agent เพื่อให้ทุก persona โหลดใช้ได้ (L0/กัปตัน/คิม/สมนึก build เองใน DOC-PIPELINE V3 · เจนนี่-shell ใช้ตอน background build). ถือ contract ของ marker ICE_BUILD=pipeline (PreToolUse hook). Triggers (TH): build deck, สร้าง slide, สร้างเอกสาร, ทำ proposal เป็นไฟล์, สร้าง .pptx, ทำ .docx, ทำ .xlsx, ทำ ROI excel, dashboard, font ไทย, font เพี้ยน, แก้ font, embed font, ไฟล์เปิดไม่ได้, Repair dialog. Triggers (EN): build deck, generate slides, build document, create pptx/docx/xlsx, ROI workbook, dashboard, font embed, Thai font, corrupted file, ICE_BUILD."
---

> **Skill:** ice-doc-builder | **Version:** V01R02 | **Date:** 2026.07.18
> **V01R02 (2026.07.18):** +§2B DOCX/XLSX CORRUPTION LESSONS + RECOVERY LADDER (จ่ายราคาจริง VFIN V02R02 docx: Word Repair→error 3 รอบ — Word-strict vs LO-lenient · settings order CT_Settings · hand-rolled odttf = Word ปฏิเสธ · rels self-closing · false-green MCP/AppleScript · LO round-trip rescue) + แก้ §3.1 EMBED ("Word ทำได้เหมือน pptx" = ผิด — GUI-embed หรือ PDF companion เท่านั้น)
> **กำเนิด:** DOC-PIPELINE V3 — สกัดจาก deliverable-gen-agent V02R08 §4/§5/E4 **คำต่อคำ** (ความรู้ที่แลกด้วยความเจ็บจริง) + เพิ่ม §3 FONT DISCIPLINE ข้ามฟอร์แมต (DOCX/XLSX/PDF — คำสั่ง user 2026.07.17: "Word font ไม่สม่ำเสมอ เอาบทเรียน PPTX มาใช้กับ PDF/Word/Excel")
> **ผู้ใช้ skill นี้:** L0 (adopt กัปตัน/คิม/สมนึก) build เองใน pipeline · deliverable-gen-agent (เจนนี่-shell) ตอน background build · ทุกกรณี **QA โดยอริสยังบังคับ — skill นี้ไม่ใช่ใบผ่าน QA**

---

# §0 CONTRACT — ใครใช้ ใช้เมื่อไหร่ marker อะไร

## 0.1 เงื่อนไขก่อน build (ครบทุกข้อจึงเริ่ม)
1. **Spec อยู่บนดิสก์แล้ว** — content spec + design spec save เป็นไฟล์ก่อนเสมอ (D-P1/D-P2 ของ DOC-PIPELINE) · build อ่านจาก spec ไม่อ่านจากความจำใน context (spec-on-disk = build ใหญ่แค่ไหน context ก็ไม่บวม)
2. **ประกาศโหมดใน PLAN-CARD แล้ว** (work_mode: lite|full) + คิว ④ อริส QA ไว้แล้ว
3. **เขียน build script ลงดิสก์** (ไม่ heredoc ยาวใน context) → รันด้วย marker

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

PAIRED FONTS (optical-matched, ติดตั้งแล้วในเครื่อง):
  Heading: Raleway ExtraBold ↔ Kanit Bold · Body: Open Sans ↔ Sarabun ·
  Alt: Inter ↔ IBM Plex Sans Thai · Govt: TH Sarabun New
```

## D2 — FONT NORMALIZATION MAP แก้ font chaos (font_test.pptx มี 13 fonts ปน!)
```
ก่อน save → enumerate fonts ที่ใช้จริง → rewrite variant → spec:
  "TH SarabunPSK"/"TH Sarabun PSK"/"THSarabunPSK" → "Sarabun"
  "Calibri"(render ไทย)/"Tahoma"(ไม่ตั้งใจ)/"Browallia" → paired spec
→ collapse ทุก font นอก approved set → report before/after count (EXIM 27→12 เคยทำมือ → auto)
```

## D3 — OPTICAL SIZE + TH-FIRST-CLASS แก้ "ขนาดไม่เท่ากัน" + "TH ใหญ่อ่านง่าย"
```
• TH run sz > EN +1-2pt (Google/MS ยืนยัน) ผ่าน cs sz แยกจาก latin sz
• TH-only object: body ≥18pt · heading ≥24pt (ห้าม TH <16pt customer-facing)
• line-height TH 1.8+ (tonal marks ต้องพื้นที่แนวตั้ง)
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
③ ⭐ LO ROUND-TRIP (พิสูจน์แล้ว 2026.07.17): soffice --convert-to "docx:MS Word 2007 XML"
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
NORMALIZATION (D2 ใช้ตรง ๆ): enumerate ทุก w:rFonts ทั้ง document.xml+styles.xml
  → collapse variant/นอก approved set → report before/after
VALIDATOR DOCX เพิ่ม: ✓ ทุก run มี cs font ที่เป็น Thai-capable
  ✓ ไม่มี "Calibri"/"Cambria" เหลือ (python-docx default leak)
  ✓ szCs ≥ sz ทุกจุดที่มีข้อความไทย ✓ styles.xml rPrDefault ครบ 4 slots
EMBED ⚠ (แก้ V01R02 — พิสูจน์แล้วว่า "ทำได้เหมือน pptx" = ผิด): DOCX ห้ามฝัง font parts (odttf) ด้วยมือ
  — Word ปฏิเสธทั้งไฟล์ (เคสจริง VFIN V02R02 §2B.1) · flag settings ต้องวางถูกลำดับ CT_Settings (§2B.1) ·
  ทางที่ใช้ได้จริง: (ก) user ให้ Word GUI embed เอง (Preferences>Save) หรือ (ข) PDF companion (Method C) ⭐ default
```

## 3.2 XLSX — SINGLE-FAMILY STRATEGY (โมเดล font ต่างจาก pptx/docx)
```
SpreadsheetML ไม่มี per-glyph slots (ไม่มี cs/latin แยก) → กติกา:
  • เซลล์มีไทย (หรือปนไทย) → font เดียวที่ Thai-capable: "Sarabun" (ห้ามหวังพึ่ง fallback)
  • เซลล์ EN/ตัวเลขล้วน → paired Latin ("Open Sans") ได้ — แต่ถ้า sheet ปนไทยมาก ใช้ Sarabun ทั้ง sheet = สม่ำเสมอกว่า
  • ทำผ่าน NAMED STYLES (openpyxl NamedStyle: header/body/number/thai-note) — ห้าม set font ราย cell แบบ ad-hoc
  • theme1.xml minorFont/majorFont set เป็น approved set กัน default Calibri โผล่ในกราฟ/element ใหม่
  • ขนาด: ไทย ≥11pt (แนะนำ 12) — D3 spirit
  • xlsx embed font ไม่ได้ → ส่งลูกค้าที่ต้อง layout เป๊ะ = แนบ PDF companion
VALIDATOR XLSX เพิ่ม: ✓ enumerate fonts ใน styles.xml → ทุกตัวอยู่ใน approved set
  ✓ ไม่มี Calibri (default leak) ✓ cell ไทยไม่ได้ font Latin-only
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
- **PPTX:** γ1 Strict Validator (§1 D4 ทุก ✓) · **XLSX:** formula-integrity + §3.2 · **DOCX:** §3.1 + academic → citation-verbatim · **HTML:** เปิด browser/screenshot จริง · **PDF:** pdffonts emb=yes
- ทุก format: validator report เป็น**ตัวเลขจริง** ("collision 0 · overflow 0 · fonts 4/4 embedded") — ห้ามรายงาน "ผ่านแล้ว" ลอย ๆ

---

# §7 🖨️ RENDERER LADDER (host นี้ — พิสูจน์จริง VFIN 2026.07.17 · ใช้เมื่อถูกสั่ง preview เท่านั้น)

```
① soffice --headless -env:UserInstallation=file:///tmp/lo-profile-fresh --convert-to pdf
   (ไม่ใส่ fresh profile = พิมพ์ "convert..." แต่ไม่เขียนไฟล์เงียบ ๆ)
② PowerPoint AppleScript save-as-PDF (fidelity สูงสุด): dest ต้องเป็น POSIX file (string เฉย ๆ = "done" แต่ไม่เขียน) ·
   sandbox เขียน /private/tmp ไม่ได้ → save ใต้ ~/Documents แล้วย้าย
③ PowerPoint MCP = เช็ค "เปิดได้/ไม่ขึ้น Repair" เท่านั้น (export_pdf = false success ห้ามใช้ render)
④ ไม่มีทางไหนได้ = NOT-VERIFIABLE-ON-HOST บอกตรง ๆ — ห้ามหลุดไป loop สอบสวน
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
