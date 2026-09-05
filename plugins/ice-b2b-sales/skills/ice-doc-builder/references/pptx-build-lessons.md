# บทเรียนการสร้างไฟล์นำเสนอ — 18 PPTX Lessons · STRICT VALIDATOR และการฝังฟอนต์ (D4 ฉบับเต็ม) · Build-vs-Edit · แม่แบบเลย์เอาต์

> **Version:** V01R01 | **Date:** 2026.09.05 | ส่วนหนึ่งของสกิล `ice-doc-builder` — เนื้อหาย้ายมาจาก `SKILL.md` V01R23 (§2 · §1 D4 ฉบับเต็ม · §4.1-4.3) ตามเดิมทุกตัวอักษร (คำสั่ง Pass 2.6: ลดขนาดไฟล์หลักโดยกลไกไม่หาย)
> **ไฟล์นี้ใช้ทำอะไร:** เก็บบทเรียนที่แลกด้วยความเจ็บจริงของไฟล์ .pptx และรายละเอียดเชิงเทคนิคของด่านตรวจโครงสร้าง — ไฟล์หลักเหลือสาระสำคัญและชี้มาที่นี่
> **ใช้เมื่อไหร่:** ตอนเขียนหรือแก้ build script ของไฟล์นำเสนอ · ตอน PowerPoint ขึ้น Repair · ตอนฝังฟอนต์ไม่ผ่าน · ตอนต้องตัดสินว่า build ใหม่หรือแก้เฉพาะจุด
> **path ในไฟล์นี้:** `_lib/` หมายถึง `~/.claude/agents/_lib/` · หัวข้อที่ขึ้นต้นด้วย § หมายถึงหัวข้อของ `SKILL.md` ของสกิลนี้ · รหัสทีม ⑤ อริส = `qa-master-agent` ผู้ตรวจคุณภาพอิสระ · เลขวงกลมในบันได (① ② ③) เป็นลำดับขั้น ไม่ใช่รหัสทีม

## ส่วนที่ 1 — §2 18 PPTX Lessons (คงคำต่อคำ — แลกด้วยความเจ็บจริงจาก TQR §6.7)

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

## ส่วนที่ 2 — §1 D4 STRICT VALIDATOR + FONT-EMBED ฉบับเต็ม (5 เงื่อนไขของ Method B)

```
STRICT VALIDATOR (บังคับก่อนส่งเข้า ⑤ อริส):
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
  → OPEN IN REAL POWERPOINT = บังคับ — **ผู้ทำคือ ⑤ อริส ในรอบตรวจ ไม่ใช่ผู้ build**
      (ผู้ build ทำได้แค่ self-check เชิงโครงสร้างตาม §0.3) · อริสเปิดแล้วยังไม่แน่ใจว่ามี Repair dialog
      หรือไม่ → ขอ user เปิดยืนยัน เหมือนกรณี DOCX ใน §2B.1 (qlmanage/LibreOffice = false-green — มองไม่เห็น corruption/16:9/General-Failure/U+2192)
      ⛔ LibreOffice render ผ่าน ≠ validation pass — ใช้ preview เร็ว ๆ ได้ แต่ "สวยใน LibreOffice" อาจเป็นไฟล์เสียในเครื่องลูกค้า (KT Food S4: → หลุดเพราะ LibreOffice ปล่อยผ่าน)
      ⚠️ font "General Failure" (อาการ B) = AppleScript/qlmanage มองไม่เห็น → คนเปิด PowerPoint ดู dialog

🚧 BUILD NOTE: embed customer-facing = Method B เสมอ · ห้ามใช้ LibreOffice EmbedFonts
(พิสูจน์แล้วไม่ embed + พัง 16:9) · embed ไม่ผ่าน/font Restricted → fallback PDF companion (Method C)
```

## ส่วนที่ 3 — §4.1 Other Build Lessons (4 projects)

```
xlsx: LIVE formula (=NPV(rate,CF1:CF10)/=IRR + cached <v> + fullCalcOnLoad) · no external-link (flatten) ·
      omit calcChain (Excel rebuild) · Thai via sharedStrings · freeze header + data-validation dropdowns
Ordered section manifest: section#/divider/footer/filename จาก 1 list (กัน section drift)
Image hygiene: downsample ≤150dpi (กัน deck 45-58MB) · strip ~$lock + .DS_Store ก่อน zip
docProps: overwrite creator=iCE (กัน "Steve Canny" python-pptx default leak)
```

## ส่วนที่ 4 — §4.2 Build-vs-Edit Guard + Pipelines + γ1/γ3 + CLOSED-LOOP

```
RULE (numeric): NEW deck OR >5 slides change → BUILD from spec (full pipeline)
                ≤5 slides edit บน VALID base → EDIT via python-pptx API (รักษา structure)
                (rebuild-from-source = re-introduce corruption → ห้าม edit แบบ rebuild)
BUILD PIPELINE: Pre-Flight → build per-section (18 lessons + D1-D4) → merge+page+font-embed → STRICT VALIDATOR → ส่ง ⑤ อริส
EDIT PIPELINE:  open VALID base (PowerPoint-Repaired ถ้ามี) → python-pptx API edit → re-verify corruption → ส่ง ⑤ อริส

⭐ γ1 SELF-TEST (ด่านศูนย์): Strict Validator = Collision + Overflow (Y-budget 16:9 6.858m H)
  → เจอทับ/ล้น → แก้จบในตัว (QA/User ไม่ควรเจอ overflow/collision)
⭐ γ3 CANONICAL: derived slide (value/summary/timeline อ้างตัวเลข) → ใช้ตัวเลขจาก key_facts canonical เดียว
⭐ CLOSED-LOOP: หลังแก้ ระบุ "แก้ issue ไหนบ้าง" (id + สิ่งที่ทำ) → tick [FIXED] ใน QA-log
```

## ส่วนที่ 5 — §4.3 Reusable Layout Patterns

```
_lib/patterns/gantt-timeline.md — Project Timeline/Gantt (สกัดจาก EPM deck จริง ผ่านงาน+User อนุมัติ)
งานตรง pattern ที่มี → อ่าน spec ใน _lib/patterns/ ก่อน → คงรูปแบบที่ผ่านงานจริง
```
