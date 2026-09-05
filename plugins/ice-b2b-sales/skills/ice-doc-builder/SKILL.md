---
name: ice-doc-builder
description: "iCE Document Build Craft — ความรู้ build .pptx/.docx/.xlsx/PDF/HTML ระดับ specialist (Build Discipline D1-D4 tri-slot Thai+EN font, 18 PPTX lessons, Method B font-embed, Strict Validator, SAVE-FIRST, VALIDATION BUDGET, renderer ladder) ที่ย้ายมาจาก deliverable-gen-agent เพื่อให้ทุก persona โหลดใช้ได้ (L0/กัปตัน/คิม/สมนึก build เองใน DOC-PIPELINE V3 · เจนนี่-shell ใช้ตอน background build). ถือ contract ของ marker ICE_BUILD=pipeline (PreToolUse hook). Triggers (TH): build deck, สร้าง slide, สร้างเอกสาร, ทำ proposal เป็นไฟล์, สร้าง .pptx, ทำ .docx, ทำ .xlsx, ทำ ROI excel, dashboard, font ไทย, font เพี้ยน, แก้ font, embed font, ไฟล์เปิดไม่ได้, Repair dialog. Triggers (EN): build deck, generate slides, build document, create pptx/docx/xlsx, ROI workbook, dashboard, font embed, Thai font, corrupted file, ICE_BUILD."
---

> **Skill:** ice-doc-builder | **Version:** V01R23 | **Date:** 2026.09.01
> **V01R20 (2026.08.31 · คำสั่ง user — หลักฐานจากงาน OCC Minutes of Meeting):** 🔴 **เพิ่มกฎ W4 และ W5 ใน §3.1 ซึ่งเป็นวินัย "ตาราง" ของไฟล์ Word ที่ขาดหายมาตลอด** — เดิม §3.1 มีแต่ W1-W3 ซึ่งว่าด้วยฟอนต์ล้วน ขณะที่ §3.2 ฝั่ง Excel มีวินัยตารางครบตั้งแต่ E2 ถึง E5 ช่องว่างนี้ทำให้ **เอกสาร Word ทุกฉบับที่ทีมเคยสร้างมา ตั้งความกว้างคอลัมน์ไว้แล้วไม่มีผลเลยแม้แต่ตารางเดียว**
> · **W4** ทุกตารางตั้งแต่สองคอลัมน์ขึ้นไปต้องตั้ง `w:tblLayout` เป็น fixed พร้อมเขียน `w:tblGrid` ใหม่และตั้ง `w:tcW` ในรอบเดียว ไม่งั้นตัวจัดหน้าเฉลี่ยทุกคอลัมน์เท่ากัน (เคสจริง: ตั้ง 1.4/5.0/7.0/3.0 ซม. ได้ 4.2 ซม. เท่ากันทุกคอลัมน์)
> · **W5** แถวเนื้อหาต้องตั้ง `w:cantSplit` ไม่งั้นแถวขาดกลางไปโผล่หน้าถัดไป (เคสจริงพบ 8 จุดใน 2 ไฟล์ แก้แล้วเหลือ 0 จุด)
> · **`audit_fonts.py` ตรวจสองข้อนี้ให้แล้วสำหรับ .docx และรายงานทั้งคู่เป็นความล้มเหลวเท่ากัน** เพราะคำถามที่ด่านตรวจตอบคือ "กฎถูกปฏิบัติตามหรือไม่" ซึ่งดูจากตัวไฟล์ได้แน่นอนทั้งสองข้อ ส่วนคำถามว่า "เกิดความเสียหายจริงหรือยัง" ตอบได้จากการ render เท่านั้น และ**ความไม่แน่นอนของคำถามหลัง ห้ามนำมาลดระดับการตรวจของคำถามแรก** (ขยายความเต็มอยู่ในกล่องท้าย VALIDATOR DOCX ของ §3.1 ซึ่งเป็นบ้านของเรื่องนี้)
> · **การทดสอบก่อนรับงาน:** ทดสอบเทียบสองทางกับไฟล์จริงก่อนแก้และหลังแก้ (ก่อนแก้ฟ้อง 4 ตารางและ 33 แถว หลังแก้ผ่านสะอาด) · ยืนยันว่าผลตรวจเดิมของ .xlsx .pptx .docx ไม่เปลี่ยน · grep-gate กลไกและกฎ 61 รายการไม่หายแม้ข้อเดียว · **ผ่าน Cold-Reader Test สามรอบ** โดยผู้อ่านที่ไม่มีบริบทตอบถูกทุกข้อทุกรอบ
> · **สิ่งที่ผู้อ่านทั้งสามรอบจับได้แล้วแก้ไปในรุ่นนี้ด้วย (ทั้งหมดอยู่ใน §3.1):** ① ตัวอย่างโค้ดจับคู่ฟอนต์สองตระกูลซึ่งขัดกับ W1 ที่อยู่ใต้มันเอง และไม่มีคำเตือนห้ามลอกแบบที่ §1 D1 มี ② คำแนะนำ "TH +1-2pt ผ่าน szCs" ค้างจากก่อนนโยบาย single-family ③ W5 บอกว่าคำตอบมาจาก render แต่ไม่ได้บอกว่าใครเป็นคน render ④ ข้อบังคับ PDF companion ของ .docx ประกาศอยู่ที่ §3.0-A แต่ E1 ที่ถูกอ้างถึงเขียนถึง .xlsx อย่างเดียว ⑤ เหตุผลที่เคยลดระดับ W5 เป็นข้อสังเกตนั้นผิดตรรกะ จึงเปลี่ยนเป็นความล้มเหลวเท่ากับ W4 ⑥ ด่าน `szCs ≥ sz` หลวมกว่านโยบาย เพราะปล่อยไฟล์ที่บวกขนาดให้ไทยทั้งที่ใช้ฟอนต์ตัวเดียวผ่านไปได้ ⑦ ตารางจุดตรวจใน §6 แถว `.docx` ยังไม่ครอบ W4-W5 ⑧ จำนวนข้อยกเว้นของกฎห้าม render เอง เขียนไม่ตรงกับ §0.3 ⑨ ตารางจุดตรวจใน §6 แถว `.docx` ไม่ได้ระบุด่านฟอนต์ V1/V2/V4 ทั้งที่แถว `.xlsx` ระบุครบ และไม่เคยมีที่ใดบอกว่า W2 W3 กับเกณฑ์ `szCs` ไม่มีด่านอัตโนมัติ ทำให้ผู้ที่พึ่งเครื่องมืออย่างเดียวพลาดสามข้อนี้เงียบ ๆ
> **หมายเหตุประวัติรุ่น:** รายการด้านล่างเรียงจากใหม่ไปเก่า · **ไม่มีบันทึกของ V01R15 · V01R16 · V01R18** (ไม่ได้ถูกเขียนไว้ตั้งแต่ต้น ไม่ใช่ถูกลบ) — ถ้าต้องสืบว่ารุ่นเหล่านั้นเปลี่ยนอะไร ให้ดูประวัติไฟล์ในระบบเก็บรุ่นแทน
> **V01R19 (2026.08.30 · คำสั่ง user — หลักฐานจากงาน CP Axtra Requirement Baseline):** 🔴 **แก้ §3.2 E2 จาก "ตรวจว่าตั้งความสูงด้วยสูตรหรือไม่" เป็น "ตรวจว่าความสูงพอกับข้อความจริงหรือไม่"** — ค่าเริ่มต้นเปลี่ยนเป็น auto-height · ตั้งเองเฉพาะแถว merge/banner ด้วย floor pt×1.72 (เดิม 1.45) · หลักฐาน ⑤ อริสตรวจ 3 รอบด้วย render จริง: ×1.45 เฉือน 83/112 แถว · ×1.72 เฉือน 52/140 · auto 0/140 — รากปัญหาคือการเดาจำนวนบรรทัดหลัง wrap ไม่ใช่ตัวคูณ · `build_xlsx.py` **V02R03** (builder ปล่อย auto เป็นค่าเริ่มต้น · audit เลิก fail แถว auto · fail เฉพาะแถวที่ตั้งเองแล้วไม่พอแม้แต่บรรทัดเดียว และ**ประกาศตรง ๆ ว่าตรวจการเฉือนจาก wrap ไม่ได้** — ลองสร้างตัวประมาณแล้วพลาดทั้งสองทาง เกินจริง 2 เท่าและต่ำกว่าจริง 7 เท่า จึงเลิกเดาแทนที่จะปล่อยให้ validator โกหก) · +**เครื่องมือใหม่ `_lib/xlsx_rowheight_probe.py`** — ตอบคำถาม "ข้อความถูกเฉือนไหม" ด้วยการให้ LibreOffice คำนวณ auto-height แล้วเทียบกับค่าที่ตั้งไว้ (แม่นกว่าการประมาณจากจำนวนอักขระมาก) · **แก้ค่าพื้นของด่านสถิต จาก pt×1.72+6 เป็น pt×1.35** หลังวัดพบว่าค่าเดิมสูงกว่าความสูงหนึ่งบรรทัดจริงทุกฟอนต์ที่ทดสอบ จึงจะฟ้องแถวที่ปกติดี · **ตรวจความถูกต้องเนื้อหาโดยทีม (เทพ + Codex) แล้วแก้ตาม:** พื้นของด่านสถิตเปลี่ยนเป็น **อ่าน metric ของฟอนต์จริงตอนรัน** (hhea) แทนค่าคงที่ — เพราะ 1.72 วัดจาก IBM Plex ตัวเดียวแล้วเกินจริงเกือบ 40% บน TH Sarabun New · ทดสอบข้อเสนอให้ใช้ usWinAscent+Descent แล้ว **ฟ้องผิด 3 ใน 6 เคส** จึงใช้ hhea ซึ่งอยู่ใต้ค่าจริงทุกเคส · +นับบรรทัดจาก `\n` ที่รู้แน่ · ตัดการอ้าง "Microsoft บอก ISO 29500 §18.3.1.73" ที่ยืนยันไม่ได้ · **ยืนยัน auto-height กับ Microsoft Excel ตัวจริง** (21.0 / 84.0 pt เทียบ LibreOffice 20.1 / 76.1) · แก้บั๊ก `render_pdf.sh` 5 ข้อที่ Codex จับได้ — เด่นสุดคือ **ทางคำเตือนคืน exit 1** ทำให้ผู้ตรวจแยกไม่ออกจาก error จริง · +**`render_pdf.sh` V01R02 ด่านฟอนต์แปลกปน** `--allow` + `--strict-fonts` (เคสจริง: อักขระ ★ ลาก HiraginoSans-W3 เข้า PDF ขณะ audit_fonts ขึ้น fonts=1 PASS และ --expect ก็ผ่าน เพราะทั้งคู่ตรวจแค่ "ฟอนต์ที่คาดไว้มีไหม" ไม่ได้ตรวจ "มีฟอนต์อื่นปนไหม") · **บทเรียนแม่ของรุ่นนี้:** เครื่องมือตรวจรายงานผ่านขณะของจริงพัง 3 ครั้งในเอกสารเดียว เพราะ validator อ่านค่าที่ประกาศไว้ในไฟล์ ไม่ได้อ่านผลที่ render ออกมา → กฎที่เขียนใหม่ต้องผูกกับผลลัพธ์ที่วัดได้เสมอ
> **V01R17 (2026.08.15) — TABLE WIDTH = ระบบสมการ (เคสจริง TQR WO R05→R10 วน 5 รอบ):** 🔴 **ห้ามแก้ความกว้างคอลัมน์ทีละคอลัมน์** — ความกว้างรวมของตารางคงที่ การขยายคอลัมน์หนึ่งโดยหักจากอีกคอลัมน์คือการย้ายรอยตัดไปโผล่ที่ใหม่ (Approach → Requirement → หัว No. — เสียไป 4 รุ่น) · **วิธีที่ถูก ทำครั้งเดียวก่อนแตะอะไร:** วัด**ความกว้างขั้นต่ำของทุกคอลัมน์พร้อมกัน** = ค่าที่มากกว่าระหว่าง (ก) คำ/token ที่ตัดไม่ได้ที่กว้างสุดในเนื้อเซลล์ กับ (ข) **หัวตารางตัวหนา** (ตัวหนากว้างกว่าเนื้อ — `No.` หนา 624 twips ขณะเลข `74` แค่ 262) บวกขอบเซลล์ ~216 twips → รวมทุกคอลัมน์เทียบความกว้างที่มี → **พอ = ตั้งครบทุกคอลัมน์ใน build เดียว จบ** · **ไม่พอ = ปัญหาเนื้อหา ไม่ใช่ปัญหาความกว้าง** (token ยาวเพราะไม่มีช่องว่างหลัง `/` ฯลฯ) → เสนอ user แก้ที่ข้อความ ห้ามวนเกลี่ยความกว้างต่อ · วัดจากไฟล์ฟอนต์จริง ไม่กะด้วยตา
> **V01R14 (2026.08.08 · FLEET READABILITY V3 Phase 2):** +**§0.0 ตารางนิยาม** (รหัสทีม · เลขวงกลมที่เป็นลำดับขั้น · rail/RAILS · SSOT · tri-slot · Method A/B/C · false-green · γ1/γ3 · staging) · 🔴 **แก้รหัสผู้ตรวจให้ตรงทั้ง fleet: ④ → ⑤ อริส ทุกจุด** (เดิมไฟล์นี้ใช้ ④ หมายถึงอริส ซึ่งชนกับ ④ เจนนี่ในไฟล์ agent — รหัสเดียวหมายถึงคนละคน) · **ไม่แตะเนื้อบทเรียนคงคำต่อคำ** (§1 D1-D4 · §2 · §2B · §3-§7)
> **V01R13 (2026.08.07 · คำสั่ง user):** ⭐ iCE SUPER TEMPLATE — §0.1 ข้อ 7 + `references/ice-super-template.md` (แม่แบบ deck เรียกโดยชื่อ: ลายเส้นทอง 10 อุตสาหกรรม + Higgsfield สูตรยิงครั้งเดียว + archetype 6 หน้า) — จบการพิมพ์ชุดคำสั่งเดิมซ้ำทุก deck
> **V01R12 (2026.08.06 · คำสั่ง user):** ⭐ FILE HYGIENE — §0.1 ข้อ 6 + แก้ต้นตอใน §7 ②: "save ใต้ ~/Documents แล้วย้าย" → staging `~/Documents/.ice-staging/` + ย้ายเข้า `_build/_qa/` ในคำสั่งเดียวกัน (ขยะ `_qa_aris_vfin/` 11 MB + `qa_s6_*.pptx` ใต้ ~/Documents — user เจอ ไม่ใช่ระบบ) · SSOT ทั้ง fleet = `reference/file-hygiene.md`
> **V01R11 (2026.08.05 · คำสั่ง user — เคส VFIN):** +**§3.0 ⑤ TEMPLATE-BASE BUILD** — งานต่อยอด template/เด็คเดิมใช้ฟอนต์ตามนโยบายปัจจุบันเป็นค่าเริ่มต้น **ห้ามสืบทอดฟอนต์ template อัตโนมัติ** · ฟอนต์ template เฉพาะ user สั่งชัดเจน (font_override_reason + QA-log) · agent ห้ามออก --allow-font ให้ตัวเองด้วยเหตุผลความสม่ำเสมอ · PLAN-CARD ต้องแจ้ง mixed-font ชั่วคราว · ③ APPROVED SET จำกัดขอบเขตเหลืองานเริ่มจากศูนย์ · `font_policy` V01R08 · อริส +D7.6d
> **V01R10 (2026.08.05 · QA + คำสั่ง user):** +**§0.1 ข้อ 0 ASK-FIRST** (คำถามค้าง = ห้ามเริ่ม build · เอกสารพร้อมคำถามแนบท้าย = ผิด protocol) · **แก้ §3.0-A แถวสไลด์แน่น:** ฟอนต์ = `Leelawadee` ตัวธรรมดา (เดิมเขียน Leelawadee UI ไม่ตรงกับโค้ดและคำสั่ง user) + เกณฑ์อัตโนมัติ + 🔴 ยกเว้น rail=govt (ฟอนต์บังคับ TOR ชนะกฎความแน่น) · อ้างอิงเดิม V01R09 | **Date:** 2026.08.04
> **V01R09 (2026.08.04) — ⭐ ตารางตัดสินใจฟอนต์ถาวร (§3.0-A):** เกณฑ์ 5 ข้อเรียงตาม "อำนาจตัดสิน" (ฝังได้ไหม → สิทธิ์ → น้ำหนัก → GAP → ยอดวรรณยุกต์) + ตารางงาน×ฟอนต์ · **กฎใหม่ (user): PPTX สไลด์แน่นต้องบีบบรรทัด → `Leelawadee UI` แทนฟอนต์ราง** (ยอดวรรณยุกต์ 0.743 vs 0.924 → ไม่ชนเมื่อบีบ · PPTX ฝังได้จึงไม่ต้องห่วงเครื่องผู้รับ) · **fallback เปลี่ยนเป็นลำดับ** `Leelawadee UI → Sukhumvit Set → Tahoma` (user: "Tahoma ไม่ค่อยสวย") · +บันทึกความจริงว่า **ไม่มีฟอนต์ไทยสวยตัวไหนมีทั้ง Win+Mac** → ทางแก้จริงคือ PDF companion ไม่ใช่หา fallback สวย · `font_policy` V01R03 (`fallbacks` เป็น list + `rail_fallbacks()`)
> **V01R08 (2026.08.04) — ตัวเลือกฟอนต์ (คำสั่ง user):** +**Leelawadee / Leelawadee UI / UI Semilight** เป็นตัวเลือกที่อนุมัติ (ผ่าน V4 ไม่ต้อง `--allow-font` · auditor แจ้ง ℹ เตือน GAP ทุกครั้ง) · ⛔ **ถอด Sarabun ออกจากตัวเลือก (V5 ใหม่)** — คนละตัวกับ TH Sarabun New/TH SarabunPSK ที่ยังใช้ได้ · **default ยังเป็น IBM Plex Sans Thai Looped** เพราะวัดแล้ว GAP ไทย-ละติน 18.9% ชนะ Leelawadee 27.3% (เกณฑ์ตัดสินตามคำสั่ง user "GAP ดีกว่าเอาตัวนั้น") · `font_policy` V01R02 (+APPROVED_ALT +RETIRED) · `build_xlsx` V02R04 (เลิกมีสำเนากฎ → เรียก `check_fonts` จาก SSOT)
> **V01R07 (2026.08.04) — ⭐ ONE POLICY, ONE AUDITOR, ALL FORMATS:** นโยบายฟอนต์ย้ายเป็น SSOT `_lib/font_policy.py` (RAILS+BLACKLIST+check_fonts) · **§0.1 ข้อ 4 ยกเป็นกติกาบังคับ: build script ทุกตัว `from font_policy import RAILS` — ห้าม hard-code ชื่อฟอนต์** · **จุดตรวจเดียว `_lib/audit_fonts.py`** ครอบ xlsx/pptx/docx/html/pdf · build_pptx/docx/dashboard/deck/html แก้ให้อ่านจากรางแล้ว (build_pptx เดิม **ไม่เคย set ฟอนต์เลยสักบรรทัด** · build_docx ไม่มี `w:cs` · dashboard เป็น CSS ละตินล้วน) · เอกสารกำกับที่เคยขัดกันเอง (`05-typography` V02R01 · `sales-pipeline-report` V01R04 · `gantt-timeline` V01R02) ลดเหลือ pointer
> **V01R06 (2026.08.04) — ⭐ V4 RAIL CONFORMANCE:** +**§6 V4** ตรวจว่าฟอนต์ **ตรงรางที่นโยบายกำหนด** ไม่ใช่แค่ "resolve ได้ + ไม่ blacklist" (V1/V2 ตอบคนละคำถามกับนโยบาย → Sarabun ลอดทั้งคู่) · เคสจริง `PWA TCO-Breakdown V01R22` build 2026.08.04 ยังเป็น Sarabun แล้ว validator ขึ้น PASS — **user จับได้ ไม่ใช่ระบบ** · ต้นเหตุ: build script เขียนมือ hard-code `FONT` เอง → bypass ตาราง RAILS · +**E4 แก้ false positive** (fail เฉพาะ merge **และ** ไม่ตั้ง row height — พิสูจน์ด้วย differential test ว่าไฟล์ที่ builder เราสร้างสดก็ FAIL) · `build_xlsx.py` **V02R02**
> **V01R05 (2026.08.01) — RENDERER SHIM GUARD:** +**§7 กฎข้อ 0** `soffice` ใน PATH = shim ของ codex runtime ที่แทนฟอนต์ทั้งไฟล์เงียบ ๆ → ใช้ `_lib/render_pdf.sh` เสมอ + POST-RENDER FONT VERIFY
> **V01R04 (2026.07.31) — THAI WORD BREAKING (คำสั่ง user):** +**§3.5** ตัดบรรทัดไม่ผ่ากลางคำ ด้วย **PyThaiNLP** (`newmm` — `longest` ห้ามใช้ มัน lowercase อังกฤษ) · **3 ชั้น**: T1 lang-tag `th-TH` (ไม่แตะข้อความ · docx/pptx) → T2 QA-only ทำนายจุดผ่ากลางคำแล้วขยายคอลัมน์แทน (⭐ default ของ xlsx) → T3 ZWSP (ทางสุดท้าย · **แลกกับ Ctrl+F หาไม่เจอ**) · tool: `_lib/thai_wordbreak.py` · เคสจริง: PWA TOR Matrix เสี่ยง **47/261 เซลล์**
> **V01R03 (2026.07.31) — FONT POLICY 2 ราง + Excel discipline + validator ใหม่ (LOCKED โดย user):** +**§3.0 FONT POLICY** (เอกชน = `IBM Plex Sans Thai Looped` ไทย=อังกฤษไม่บวก pt · ราชการ = `TH Sarabun New` 16pt · BLACKLIST 8 ตระกูลพร้อมเหตุผล · single-family-first) · +**§3.2 XLSX เขียนใหม่ E1-E6** (Excel ฝัง font ไม่ได้→PDF companion · row height = pt×1.45×บรรทัด+6 **[ยกเลิกแล้วโดย V01R19 — ห้ามหยิบไปใช้ ดู §3.2 E2]** · vertical=center · ห้าม merge ในแถวไทย+wrap · ห้าม shrink-to-fit · ตั้ง default font ก่อนคำนวณ width) · +**§3.1 W1-W3** (ascii+hAnsi+cs ตัวเดียวกันเพราะสเปก MS ขัดกันเอง · bCs/iCs บังคับ · ห้าม lineRule=exact) · +**§6 V1-V3 validator** (⭐V1 font-name resolution ดักชื่อฟอนต์ที่ไม่มีจริง · V2 blacklist · V3 สระอำ integrity) · **แก้ D3** เลิกใช้ "+1-2pt" และ "line-height 1.8+" ที่**ตรวจแล้วไม่มีต้นทางจริง** → ใช้สูตร cap-height ratio ที่วัดเอง · **แก้ D1** single-family แทน paired
> **ฐานหลักฐาน V01R03:** PDF สาธารณะ 45 ฉบับ (`pdffonts`+span) · วัด metric ฟอนต์จริง 9 ตระกูล · user ทดสอบสายตา · เคสจริง PWA TOR Matrix · เอกสารเต็ม → `Output/iCE_Thai-Latin_Font-Policy_PROPOSAL_V01R01_2026.07.31.md`
> **V01R02 (2026.07.18):** +§2B DOCX/XLSX CORRUPTION LESSONS + RECOVERY LADDER (จ่ายราคาจริง VFIN V02R02 docx: Word Repair→error 3 รอบ — Word-strict vs LO-lenient · settings order CT_Settings · hand-rolled odttf = Word ปฏิเสธ · rels self-closing · false-green MCP/AppleScript · LO round-trip rescue) + แก้ §3.1 EMBED ("Word ทำได้เหมือน pptx" = ผิด — GUI-embed หรือ PDF companion เท่านั้น)
> **กำเนิด:** DOC-PIPELINE V3 — สกัดจาก deliverable-gen-agent V02R08 §4/§5/E4 **คำต่อคำ** (ความรู้ที่แลกด้วยความเจ็บจริง) + เพิ่ม §3 FONT DISCIPLINE ข้ามฟอร์แมต (DOCX/XLSX/PDF — คำสั่ง user 2026.07.17: "Word font ไม่สม่ำเสมอ เอาบทเรียน PPTX มาใช้กับ PDF/Word/Excel")
> **ผู้ใช้ skill นี้:** L0 (adopt กัปตัน/คิม/สมนึก) build เองใน pipeline · deliverable-gen-agent (เจนนี่-shell) ตอน background build · ทุกกรณี **QA โดยอริสยังบังคับ — skill นี้ไม่ใช่ใบผ่าน QA**

---

# §0 CONTRACT — ใครใช้ ใช้เมื่อไหร่ marker อะไร

## 0.0 ⭐ ตารางนิยาม — รหัสและศัพท์ทุกตัวที่ไฟล์นี้ใช้ (อ่านก่อนใช้งานครั้งแรก)

> วิธีเขียนไฟล์ระบบที่ skill นี้ยึด: `~/.claude/agents/reference/fleet-writing-standard.md`

| รหัส / ศัพท์ | ความหมาย |
|---|---|
| **② ก้อง · ③ เทพ · ④ เจนนี่ · ⑤ อริส · ⑥ เสี่ยวป้อ · ⑦ โมโม่** | รหัสทีม (เลขวงกลมที่ยืนเดี่ยวหน้าชื่อคน): ② `sales-process-agent` เขียนเนื้อหาฝั่งงานขาย · ③ `solution-knowledge-agent` ให้คำตอบด้าน product/industry · ④ `deliverable-gen-agent` ผู้สร้างไฟล์เบื้องหลัง **ทำงานเฉพาะเมื่อ user เรียกชื่อตรง** · ⑤ `qa-master-agent` ผู้ตรวจคุณภาพอิสระ — **ปลายทางบังคับของทุก build** · ⑥ `retrieval-scout-agent` เก็บวัตถุดิบ · ⑦ `demo-builder-agent` สร้าง demo/prototype app |
| **เลขวงกลมในบันได/ตาราง (① ② ③ ④ ⑤)** | **เป็นลำดับขั้นตอนเท่านั้น ไม่ใช่รหัสทีม** — เช่น "① ล้างสิ่งแวดล้อม → ② ตรวจ XML" ใน RECOVERY LADDER · แยกได้จากบริบท: รหัสทีมจะมีชื่อคนตามหลังเสมอ (⑤ อริส) |
| **L0 / L1** | L0 = main loop ของ session ที่คุยกับ user โดยตรงและรับบทเป็น persona (กัปตัน/คิม/สมนึก) · L1 = agent ระดับบนที่เป็นเจ้าของงานชิ้นนั้น — ใน DOC-PIPELINE V3 ทั้งสองคือ "ผู้ build" |
| **DOC-PIPELINE V3 · D-P0 ถึง D-P5** | กระบวนการทำเอกสารของ fleet: D-P0 เก็บวัตถุดิบ · D-P1 อ่าน source · D-P2 เขียน spec · D-P3 build · D-P4 ⑤ ตรวจ · D-P5 แก้แล้วให้ ⑤ ตรวจส่วนต่าง — นิยามเต็มอยู่ไฟล์กัปตัน §5 |
| **spec (content spec / design spec)** | ไฟล์ที่ระบุ "เนื้อหาอะไร" และ "หน้าตาอย่างไร" ซึ่งต้อง save ลงดิสก์ก่อน build เสมอ (spec-on-disk) |
| **marker** | คำนำหน้าคำสั่ง Bash ที่บอก hook `ice-prebuild-guard.sh` ว่า build นี้มาจากเส้นทางที่ถูกกฎ — รายการครบใน §0.2 |
| **rail (ราง) / RAILS** | "ราง" = ชุดฟอนต์ตามประเภทงาน มี 2 ราง: `private` งานเอกชน · `govt` งานราชการ/TOR · `RAILS` = ตารางในไฟล์ `~/.claude/agents/_lib/font_policy.py` ซึ่งเป็นแหล่งเดียวของชื่อฟอนต์ (SSOT) |
| **SSOT (Single Source of Truth)** | แหล่งข้อมูลจริงเพียงแห่งเดียวที่ทุกคนต้องอ้างถึง — ห้ามคัดลอกค่าไปเก็บซ้ำที่อื่น เพราะสำเนาจะเก่าโดยไม่มีใครรู้ |
| **tri-slot (D1)** | การกำหนดชื่อฟอนต์ครบ 3 ช่องในหนึ่ง text run — latin (อังกฤษ) · ea (เอเชียตะวันออก) · cs (complex script = ภาษาไทย) — เพื่อให้โปรแกรมเลือกฟอนต์ถูกต่อตัวอักษร |
| **Method A / B / C (ฝังฟอนต์ PPTX)** | A = ใช้ LibreOffice EmbedFonts (**พิสูจน์แล้วว่าใช้ไม่ได้ ห้ามใช้**) · B = `_lib/embed_fonts_pptx.py` (วิธีหลัก) · C = ส่ง PDF companion คู่ไปด้วย (ทางสำรองที่ปลอดภัยเสมอ) |
| **PDF companion** | ไฟล์ PDF ที่ export จาก artifact เดียวกันแล้วส่งคู่กันไป — ใช้เมื่อฟอร์แมตนั้นฝังฟอนต์ไม่ได้ (xlsx/docx) เพราะ PDF ฝังฟอนต์ครบ 100% · **🔴 ต้องถามผู้ใช้ก่อนทำทุกครั้ง ห้ามทำเอง — กติกาเต็มที่ §0.1 ข้อ 9** |
| **false-green** | เครื่องมือรายงานว่า "ผ่าน" ทั้งที่ของจริงเสีย — เช่น LibreOffice เปิดไฟล์ได้แต่ PowerPoint สั่ง Repair · เจอ false-green = ต้องยืนยันด้วยโปรแกรมจริง |
| **CB (Composed Build)** | วิธี build งานใหญ่โดยแบ่งเป็นหน่วยย่อยแล้วประกอบ — ใช้เมื่อเอกสารยาวเกินกว่าจะ build รวดเดียว |
| **γ1 / γ3 (แกมมา 1 / แกมมา 3)** | ชื่อชุด self-test ที่ผู้ build ต้องทำเองก่อนส่ง ⑤ (นิยามเดียว อยู่ §4.2): **γ1** = ตรวจว่าไม่มีวัตถุทับกันและไม่มีข้อความล้นกรอบ — ผู้ตรวจไม่ควรต้องเจอสองอาการนี้ · **γ3 CANONICAL** = ทุกหน้าที่อ้างตัวเลขต้องดึงจากชุดข้อเท็จจริงชุดเดียวกัน ตัวเลขห้ามขัดกันข้ามหน้า |
| **staging** | โฟลเดอร์พักไฟล์ชั่วคราวระหว่างสร้าง (`~/Documents/.ice-staging/`) ซึ่งต้องย้ายเข้าที่เก็บจริงในคำสั่งเดียวกัน ไม่ทิ้งค้าง |
| **ตระกูลรหัสกฎ (D · W · E · T · V · γ)** | รหัสนำหน้าเลขที่ใช้เรียกกฎแต่ละข้อในไฟล์นี้ แยกตามเรื่องที่กฎนั้นคุม: **D1-D4** วินัยการสร้างไฟล์นำเสนอ (§1) · **W1-W5** วินัยของไฟล์ Word โดย W1 ถึง W3 เป็นเรื่องฟอนต์ และ W4 ถึง W5 เป็นเรื่องตาราง (§3.1) · **E1-E6** วินัยของไฟล์ Excel (§3.2) · **T1-T3** ชั้นวิธีจัดการการตัดคำไทย (§3.5) · **V1-V4** ด่านตรวจฟอนต์ (§6) · **γ1 และ γ3** ชุดทดสอบที่ผู้สร้างต้องทำเองก่อนส่งผู้ตรวจ (§4.2) |
| **H3 (กฎเหล็ก)** | กฎของ CLAUDE.md เครื่อง PART 3 ข้อ 3: ห้ามกุข้อมูลที่ไม่มีจริง (ตัวเลข ชื่อ วันที่ ข้อมูลทางเทคนิค) — ไม่แน่ใจให้ถาม |

## 0.1 เงื่อนไขก่อน build (ข้อ 0-4, 6 และ 8 ต้องครบจึงเริ่ม · ข้อ 5 ทำหลัง build เสร็จ · ข้อ 7 ใช้เมื่อ user เอ่ยชื่อ template · ข้อ 9 ใช้เมื่อจะทำไฟล์ประกอบ)

> **⭐ ลำดับงานเมื่อ "แก้ artifact ที่มีอยู่แล้ว" (สถานการณ์ที่พบบ่อยที่สุด — อ่านกล่องนี้ก่อนลงมือ):**
> 1. **อ่านไฟล์จริงก่อนถาม** — `ls` หารุ่นสูงสุดบนดิสก์ + เปิดอ่านเนื้อหา (ข้อ 1b) เพราะต้องเห็นของจริงก่อนจึงจะรู้ว่าควรถามอะไร
> 2. **หา diff แล้วปรับ spec ให้ตรงไฟล์** (ข้อ 1b) — จุดที่ต่างจาก spec คือสิ่งที่ user แก้เอง ต้องรักษาไว้
> 3. **ถามสิ่งที่ยังค้างเป็นชุดเดียว** (ข้อ 0 ASK-FIRST) — ถามหลังเห็นไฟล์จริง คำถามจะตรงกว่าและน้อยกว่า
> 4. **เลือกวิธีแก้:** ไม่เปลี่ยนโครง → แก้เฉพาะจุดบนไฟล์จริง (ข้อ 1c) · เปลี่ยนโครง → สร้างใหม่จาก spec
> 5. **เขียนสคริปต์ลงดิสก์ (ข้อ 3) เสมอทั้งสองวิธี** แล้วรันด้วยเครื่องหมายที่ตรงบทบาท: แก้เฉพาะจุดไม่เกินห้าจุดบนไฟล์ที่สมบูรณ์ใช้ `ICE_SMARTFIX=1` · นอกนั้นใช้ `ICE_BUILD=pipeline` พร้อม `ICE_BASE=` (งานนำเสนอเพิ่ม `ICE_DESIGN=briefed`)
> 6. **บันทึกรุ่นใหม่พร้อมย้ายรุ่นก่อนหน้าเข้า `_archive/` ในคำสั่งเดียวกัน** แล้วส่งผู้ตรวจคุณภาพ
0. **⭐ ASK-FIRST ผ่านแล้ว (V01R10 · คำสั่ง user 2026.08.05)** — ทุกข้อสงสัยที่ source ไม่ตอบ
   (ผู้อ่าน/โครง/ความยาว/ตัวเลขที่ขาด/สิ่งห้ามใส่/ภาษา+ราง) ถูกถาม user เป็นชุดเดียวและ**ได้คำตอบแล้ว**
   — มีคำถามค้าง = ห้ามเริ่ม build · เจอกำกวมใหม่ระหว่าง build = หยุดถามทันที ห้ามเดา ·
   🔴 เอกสารส่งมอบพร้อม "คำถามปรับปรุง" แนบท้าย = ทำผิดข้อนี้ (นิยามเต็ม: กัปตัน S1 / สมนึก T1)
1. **Spec อยู่บนดิสก์แล้ว** — content spec + design spec save เป็นไฟล์ก่อนเสมอ (D-P1/D-P2 ของ DOC-PIPELINE) · build อ่านจาก spec ไม่อ่านจากความจำใน context (spec-on-disk = build ใหญ่แค่ไหน context ก็ไม่บวม) · **content spec ต้องเขียนตามกติกาภาษากลาง `~/.claude/agents/reference/language-register.md` — โหลดกติกานั้นก่อนลงมือเขียน spec เสมอ ไม่ใช่รอให้อริสจับตอนตรวจ D8** เพราะการแก้ถ้อยคำหลัง build เสร็จหมายถึงต้อง build ใหม่ทั้งรอบ (เคสจริงสิงหาคม 2026: user ต้องสอนเรื่องภาษาซ้ำห้าครั้งใน session เดียว)

1b. **⭐⭐ DISK-IS-TRUTH BASE — ไฟล์บนดิสก์คือความจริง ไม่ใช่ spec และไม่ใช่ความจำ (V01R18 · คำสั่ง user 2026.08.26)**
   **user แก้ไขไฟล์ผลงานด้วยตัวเองเป็นเรื่องปกติหลัง build เสร็จ** เพราะ user เป็นผู้เข้าใจเรื่องราวและสิ่งที่จะเสนอลูกค้า งานนี้จึงเป็นการทำงานร่วมกันระหว่างคนกับ agent ก่อนแก้หรือ build ซ้ำ artifact ที่มีอยู่แล้ว **ต้องทำสามขั้นนี้ตามลำดับเสมอ**
   1. `ls` โฟลเดอร์เป้าหมายหา**รุ่นสูงสุดที่อยู่บนดิสก์จริง** แล้วเปิดอ่านเนื้อหาไฟล์รุ่นนั้น (ไฟล์ office ให้แตกอ่านเนื้อหาจริง ไม่ใช่ดูแค่ชื่อไฟล์)
   2. เทียบเนื้อหาที่อ่านได้กับ spec หรือรุ่นที่ตัวเองเคยสร้าง เพื่อหาจุดที่ user แก้ไข แล้ว**ปรับ spec ให้ตรงกับไฟล์จริงก่อน** (spec ตามไฟล์ ไม่ใช่ไฟล์ตาม spec)
   3. จึงเริ่มงาน และประกาศฐานในคำสั่ง build ด้วย `ICE_BASE=<path รุ่นที่ใช้เป็นฐาน>` หรือ `ICE_BASE=NEW` เมื่อสร้างครั้งแรก
   ❌ ผิด: นำ build script เดิมมารันสร้างรุ่นถัดไปโดยไม่เปิดไฟล์ปัจจุบัน — การแก้ด้วยมือของ user หายทั้งหมด (เคสจริง OCC: rebuild จากฐาน V42 ทั้งที่ดิสก์อยู่ที่ R57 เนื้อหาถดถอย user ต้องย้ำให้อ่านไฟล์ซ้ำหลายรอบ)
   ✅ ถูก: เปิดไฟล์รุ่นล่าสุดอ่าน พบว่า user แก้หัวข้อหน้าห้าและตัวเลขหน้าเก้า จึงบันทึกทั้งสองจุดเข้า spec แล้วจึงสร้างรุ่นใหม่ที่คงการแก้นั้นไว้
   > ตัวตรวจก่อนสร้างไฟล์เทียบลายนิ้วมือไฟล์กับรุ่นที่ build ล่าสุดให้เองด้วย ถ้าพบว่าไฟล์ถูกแก้หลัง build ล่าสุดจะปฏิเสธคำสั่งจนกว่าจะอ่านและซึมซับการแก้แล้วประกาศ `ICE_ABSORBED=1` (ดู §0.2)

1c. **⭐ EDIT-IN-PLACE FIRST — แก้บนไฟล์จริงก่อน สร้างใหม่ทั้งไฟล์เมื่อจำเป็นเท่านั้น (V01R18)**
   งานแก้ที่**ไม่เปลี่ยนโครงสร้างเอกสาร** (แก้ถ้อยคำ ตัวเลข สี ตำแหน่ง ขนาดตัวอักษร) ให้**แก้เฉพาะจุดบนไฟล์รุ่นล่าสุดผ่าน API ของไลบรารีเอกสาร** เป็นค่าเริ่มต้น เพราะวิธีนี้รักษาการแก้ไขของ user ทุกจุดไว้เองโดยอัตโนมัติ และใช้ทรัพยากรน้อยกว่าการสร้างใหม่ทั้งไฟล์มาก
   สร้างใหม่ทั้งไฟล์จาก spec เมื่อ**เปลี่ยนโครงสร้าง**เท่านั้น เช่น เพิ่มหรือลดจำนวนหน้า เปลี่ยนลำดับเนื้อหา หรือเปลี่ยนแม่แบบ
   ❌ ผิด: แก้ข้อความสองบรรทัดแล้ว build ใหม่ทั้งเล่มขนาดสี่สิบเมกะไบต์ (เคสจริง OCC: หนึ่งเอกสารสะสมหกสิบเอ็ดรุ่นด้วยวิธีนี้)
   ✅ ถูก: เปิดไฟล์รุ่นล่าสุด แก้ข้อความสองจุดที่ต้องแก้ บันทึกเป็นรุ่นถัดไป
2. **ประกาศโหมดใน PLAN-CARD แล้ว** (work_mode: lite|full) + คิว ⑤ อริส (qa-master) ให้ตรวจไว้แล้ว
2b. **ตัวแปลภาษาที่ใช้ = `python3` ของระบบ** ซึ่งเป็นที่อยู่ของไลบรารีสร้างเอกสารทั้งสามตัว — **ห้ามใช้ python ของ `_lib/.venv-doc`** เพราะ venv นั้นแยกไว้สำหรับเครื่องมือ*อ่าน*เอกสารคนละชุดกัน · **ไม่ต้องจำรายชื่อไลบรารีหรือชื่อ path — ถามเครื่องมือเอาว่าตอนนี้ของจริงเป็นอย่างไร:** `python3 ~/.claude/agents/_lib/env_check.py build` (ตอบครบว่าใช้ตัวไหน มีอะไรแล้ว ขาดอะไร พร้อมคำสั่งติดตั้ง) · เจอข้อความว่าไม่พบไลบรารีเมื่อไร ให้รันคำสั่งนี้ก่อนสรุปเสมอ
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
5. **จบ build ต้องผ่าน `audit_fonts.py` ก่อนคิว ⑤ อริส เสมอ** (§6) — **ผ่าน ไม่ใช่ต้องรันเอง:**
   build_* ของเราเรียกให้อัตโนมัติในตัวแล้ว ถ้าใช้มันสร้างงานก็ถือว่าครบ **ห้ามรันซ้ำ** (§6 ข้อ 1 SINGLE-PASS)
   ต้องรันเองเมื่อ: เขียน build script เอง · แก้ไฟล์ด้วยมือหลัง build · หรือได้ไฟล์มาจากที่อื่น
6. **⭐ FILE HYGIENE (V01R12 · design โดย user 2026.08.06):** ไฟล์ temp/ทดสอบ/render ทุกชนิด →
   **ที่เก็บเดียวของ sub-project: `<sub-project>/20-Output/_temp/`** (หลักฐานตรวจ → `_temp/qa/`)
   · spec/build script ยังอยู่ `_build/` ข้าง artifact (เอกสารประกอบงาน ไม่ใช่ temp)
   · ไฟล์ output จริง → ตำแหน่งที่ user/spec ระบุเท่านั้น — **ไม่แน่ใจ = ถามก่อนทำงานต่อ**
   · 🔴 ห้ามสร้างไฟล์นอกโปรเจกต์ (โดยเฉพาะใต้ ~/Documents) — SSOT: `reference/file-hygiene.md`
7. **⭐ iCE SUPER TEMPLATE (V01R13 · คำสั่ง user 2026.08.07 — จบการพิมพ์สั่งซ้ำ ≥5 session):**
   **user เอ่ยชื่อ "iCE Super Template" → ดึง `references/ice-super-template.md` มาใช้ทั้งชุดทันที**
   · สั่ง deck ทั่วไปโดยไม่เอ่ยชื่อ = ห้ามเหมาใช้เอง — ถาม CI/รายละเอียด/template ตาม ASK-FIRST ปกติ
   — archetype 6 หน้า (ปกเข้มไล่เฉด+ลายเส้นทองคล้ำตามอุตสาหกรรม · TOC ·
   divider · detail พื้นขาวลายจาง · process=infographic+Color telling/Block/Shading · closing) +
   สูตร background Higgsfield ยิงครั้งเดียว/deck + motif 10 อุตสาหกรรม + ฟอนต์ตามโหมดภาษา (RAILS) +
   ASK-FIRST ชุดสั้น 4 ข้อ (อุตสาหกรรม/ภาษา/ผู้ชม/โครง) · user ระบุ template อื่น/แบรนด์ลูกค้า = ตามนั้นแทน
   · สี/type scale/grid = authority เดิมที่ `b2b-slide-designer/references/template_ice_propose.md` (ห้าม fork)

8. **⭐⭐ DESIGN LOADOUT — งานออกแบบต้องเปิดสกิลออกแบบก่อนเขียน design spec (V01R18 · คำสั่ง user 2026.08.26)**
   งานที่ผลลัพธ์เป็น**ไฟล์นำเสนอ ข้อเสนอ หรือเอกสารที่ส่งถึงลูกค้า** ต้องโหลด `b2b-slide-designer` และ `b2b-presentation-creator` **ก่อนเขียน design spec เสมอ** (เส้นทางเลือกใช้ต่อฟอร์แมตอยู่ที่ MASTER MATRIX §5)
   งานที่ต้อง**วาด infographic หรือ icon** ไม่ว่าฟอร์แมตใด ต้องโหลด `b2b-slide-designer` หัวข้อ 4.11 DESIGN BRIEF ก่อนลงมือ **ข้ามไม่ได้ไม่ว่างานจะเล็กแค่ไหน** แล้วประกาศ `ICE_DESIGN=briefed` ในคำสั่ง build
   งานที่ต้อง**วาดแผนภาพเชิงโครงสร้าง (diagram) หรือผังกระบวนการ (flow)** — เช่น สถาปัตยกรรมระบบ ผังกระบวนการทำงาน swimlane sequence ผังฐานข้อมูล ผังองค์กร quadrant กรอบแนวคิดวิจัย หรือการวาดใหม่จากไฟล์ `.drawio`/`.mmd` ที่ลูกค้าส่งมา — **ต้องโหลด skill `diagram-design` ก่อนเขียน design spec เสมอ** เพราะ skill นั้นถือกติกาการเลือกชนิดแผนภาพ งบความซับซ้อน และกฎเส้นเชื่อมที่กันงานออกมาดูเป็นงาน AI สำเร็จรูป **ตารางตัดสินว่ากรณีไหนใช้และกรณีไหนไม่ใช้ อยู่ที่ §5.1 "ตารางกรณีใช้ `diagram-design`" ซึ่งเป็นบ้านเดียวของกติกานี้** — ที่นี่บอกเพียงว่าต้องโหลดก่อนเขียน spec
   **เรื่องเครื่องหมาย `ICE_DESIGN=briefed` ให้ถือตามนี้ (ตอบข้อสงสัยที่เกิดจริงตอนทดสอบผู้อ่านเย็น 2026.09.01):** เครื่องหมายนี้ยืนยันว่าทำ DESIGN BRIEF ตาม `b2b-slide-designer` หัวข้อ 4.11 แล้ว จึง **ผูกกับฟอร์แมตผลลัพธ์ ไม่ได้ผูกกับว่าใช้ skill ไหนวาด** · งานที่ผลลัพธ์เป็นไฟล์นำเสนอ เอกสาร หรือภาพที่ส่งถึงลูกค้า **ต้องประกาศเสมอแม้ภาพในนั้นจะวาดด้วย `diagram-design`** เพราะทั้งไฟล์ยังต้องผ่าน DESIGN BRIEF · **ข้อยกเว้นเดียว** คืองานที่ส่งมอบเป็นไฟล์แผนภาพเดี่ยว ๆ (ไฟล์ HTML หรือภาพที่ออกจาก `diagram-design` โดยไม่ได้ประกอบเป็นเอกสาร) ซึ่งไม่ต้องประกาศ เพราะไม่มีเอกสารให้ brief — **การทำ brief ของ `diagram-design` ไม่นับแทน DESIGN BRIEF 4.11 และในทางกลับกันก็ไม่นับแทนกัน เพราะคนละเรื่องกัน: 4.11 ตั้งโจทย์ว่าเอกสารทั้งฉบับจะสื่ออะไร ส่วน `diagram-design` ตัดสินว่าภาพหนึ่งภาพเป็นชนิดใดและตัดอะไรออก**
   ❌ ผิด: เขียน design spec ว่า "ใส่ผังสถาปัตยกรรมระบบหนึ่งภาพ" แล้วส่งให้ builder ไปวาดเอาเองโดยไม่เปิด `diagram-design` (ได้กล่องเท่ากันหมด ลูกศรทแยง เงาใต้กล่อง — ผิดกฎ skill นั้นทั้งสามข้อ)
   ✅ ถูก: โหลด `diagram-design` → เลือกชนิดจากตาราง 39 ชนิด → ยืนยันชนิดและสิ่งที่จะตัดออกกับผู้ใช้ → เขียน spec ที่ระบุชนิดแผนภาพและจำนวนกล่องสูงสุด → จึงส่งต่อให้ build
   **ขอบเขตการบังคับให้ชัด:** ตัวตรวจก่อนสร้างไฟล์**ปฏิเสธอัตโนมัติเฉพาะงานไฟล์นำเสนอ** (`.pptx`) เพราะเป็นกรณีที่ตรวจด้วยเครื่องได้แน่นอน ส่วนงาน infographic ที่ออกเป็นเอกสาร ภาพ หรือหน้าเว็บ ตัวตรวจจับไม่ได้ **ผู้สร้างต้องถือกติกานี้เอง** และประกาศเครื่องหมายเช่นกัน — การที่เครื่องจับไม่ได้ไม่ได้แปลว่าได้รับยกเว้น (เอกสารเครื่องหมายนี้อยู่ที่ `b2b-slide-designer` หัวข้อ 4.11.1 ซึ่งเป็นบ้านเดียวของมัน)
   > **ทำไมเป็นเงื่อนไขบังคับ:** การตรวจงานจริงสี่ครั้งติดกันในเดือนสิงหาคม 2026 พบว่าสกิลออกแบบทั้งสองตัวถูกเปิดอ่าน**ศูนย์ครั้ง** ทั้งที่มีกฎสั่งไว้แล้วในไฟล์ของกัปตัน เพราะ session ที่ไม่ได้สวมบทกัปตันไม่มีทางเห็นกฎนั้น ผลคือ user รายงานว่างานที่ได้ "สีไม่สวย เหมือนไม่ได้ใช้แม่แบบ" กฎจึงถูกย้ายมาอยู่ที่นี่ซึ่งเป็นไฟล์ที่ทุก build ต้องเปิด

9. **🔴🔴 ไฟล์ PDF ประกอบ ต้องถามก่อนทำทุกครั้ง ห้ามทำเอง (V01R22 · คำสั่ง user 2026.09.01 — หลักฐานจากงาน CK)**
   ไฟล์ Excel และ Word ฝังฟอนต์ไม่ได้ กติกาเดิมจึงให้ทำไฟล์ PDF ส่งคู่ไปด้วย เพื่อประกันว่าเครื่องผู้รับเห็นแบบอักษรถูกต้อง **แต่ห้ามลงมือทำเองโดยอัตโนมัติ** ให้ถามผู้ใช้ก่อน พร้อมวางทางเลือกทั้งสองทางบนโต๊ะให้ครบ

   **คำถามที่ต้องถาม:** "ไฟล์นี้เป็นไฟล์ตาราง (หรือไฟล์เอกสาร) ซึ่งฝังแบบอักษรไม่ได้ ถ้าเปิดบนเครื่องที่ไม่มีแบบอักษรชุดเดียวกัน หน้าตาจะเพี้ยน มีสองทางเลือก ทางที่หนึ่ง ทำไฟล์ PDF ส่งคู่ไปด้วย แลกกับรอบตรวจที่เพิ่มขึ้นและปัญหารอยตัดกลางคำไทยในไฟล์แปลงซึ่งแก้ไม่ได้ ทางที่สอง ส่งไฟล์แบบอักษรให้ผู้รับติดตั้ง ซึ่งแทบไม่มีต้นทุน ท่านเลือกทางไหน"

   **ยกเว้นไม่ต้องถาม** เมื่อผู้ใช้สั่งให้ทำไฟล์ PDF ตรง ๆ หรือเคยตอบไว้แล้วในรอบงานเดียวกันว่าต้องการ

   > **ทำไมเป็นเงื่อนไขบังคับ:** งานลูกค้าเดือนกันยายน 2026 ระบบทำไฟล์ PDF เอง 32 ครั้งโดยผู้ใช้ไม่เคยสั่งแม้แต่ครั้งเดียว และปัญหาที่กินรอบตรวจมากที่สุดตลอดสามวัน คือรอยตัดกลางคำไทยซึ่งโตจาก 63 จุดเป็น 128 จุดโดยไม่เคยแก้ได้ **ปัญหานั้นเกิดจากไฟล์ PDF ล้วน ๆ ไม่กระทบไฟล์ตารางที่ผู้ใช้สั่ง** ถ้าไม่ทำไฟล์ประกอบตั้งแต่แรก ปัญหาทั้งชุดก็ไม่เกิด — บทเรียนคือ **การทำตามกติกาโดยไม่บอกผู้ใช้ว่ามันมีราคา คือความผิดพลาดเอง**

## 0.2 MARKER SEMANTICS (ผูก PreToolUse hook `ice-prebuild-guard.sh`)
| Marker | ใคร | ความหมาย |
|---|---|---|
| `ICE_BUILD=pipeline ` | L0 (persona กัปตัน/คิม/สมนึก) | build ถูกกฎใน DOC-PIPELINE V3 — ยืนยันว่า 0.1 ครบ + โหลด skill นี้แล้ว |
| `ICE_BUILDER=jenny ` | เจนนี่-shell เท่านั้น | background build ตาม DISK-IS-TRUTH · **USER-INVOKED ONLY: เจนนี่ทำงานเฉพาะเมื่อ User สั่ง/เรียกชื่อตรง** (L1 เสนอได้ ห้าม dispatch เอง) |
| `ICE_SMARTFIX=1 ` | L1 | Smart Fix ≤5 จุด บน base ที่ VALID · **นิยาม "จุด"** = การแก้หนึ่งที่ที่แยกกันได้ — pptx นับเป็นสไลด์ · xlsx นับเป็นเซลล์หรือช่วงเซลล์ที่ติดกัน · docx นับเป็นย่อหน้า/ตาราง · เกิน 5 = build ใหม่ |
| `ICE_INLINE_APPROVED=1 ` | ตาม FAILURE PROTOCOL | user อนุมัติ exception แล้ว |
| `ICE_BASE=<path>` หรือ `ICE_BASE=NEW` ⭐ | ทุกคนที่ build | **ประกาศฐานที่ใช้สร้างงานรุ่นนี้** — `<path>` คือไฟล์รุ่นที่อ่านมาเป็นฐาน หรือ `NEW` เมื่อสร้าง artifact ครั้งแรก · ตัวตรวจจะปฏิเสธเมื่อฐานที่ประกาศไม่ใช่รุ่นล่าสุดบนดิสก์ (กันการสร้างงานทับการแก้ของ user — เงื่อนไข 0.1 ข้อ 1b) |
| `ICE_DESIGN=briefed` ⭐ | ผู้สร้างไฟล์นำเสนอและงาน infographic | ยืนยันว่าทำ DESIGN BRIEF ตาม `b2b-slide-designer` หัวข้อ 4.11 แล้ว — **เอกสารของเครื่องหมายนี้อยู่ที่หัวข้อ 4.11.1 ของสกิลนั้นซึ่งเป็นบ้านเดียว** (เงื่อนไข 0.1 ข้อ 8) |
| `ICE_ABSORBED=1` ⭐ | ผู้ที่ build ต่อจากไฟล์ที่ user แก้เอง | ยืนยันว่าอ่านไฟล์ที่ user แก้ หา diff ครบทุกจุด และปรับ spec ให้ตรงไฟล์แล้ว — ใช้เมื่อตัวตรวจแจ้งว่าไฟล์ถูกแก้หลัง build ล่าสุด (เงื่อนไข 0.1 ข้อ 1b) |
- ทุกคำสั่ง Bash ที่รัน python สร้าง/แตะ .pptx/.docx/.xlsx ต้องขึ้นต้นด้วย marker ที่ตรงบทบาท — ไม่มี marker = hook deny (by design)
- marker ไม่ใช่ของแจก: ห้ามใส่ให้ context อื่นที่ไม่ได้โหลด skill นี้

## 0.3 SAVE-FIRST · NO SELF-RENDER (จากเจนนี่ V02R08 — คงหลักเดิม)
- **Build → SAVE V##R## ลงดิสก์ทันที → self-check เชิงโครงสร้างเท่านั้น → ส่งเข้า ⑤ อริส** — self-check = zip CRC · จำนวน slide/หน้า/sheet · embed flags · collision/overflow คำนวณจาก XML geometry (**ไม่ render ภาพ**)
- **ห้าม render preview เพื่อเช็คงานตัวเอง** — การดูภาพจริงเป็นหน้าที่ ⑤ อริส (EVIDENCE FRESHNESS — render สดอยู่แล้ว) · render ซ้ำ = จ่าย token ×2
- ข้อยกเว้น: CB Progressive per-unit preview หรือ user สั่ง preview ชัดเจน → ใช้ Renderer Ladder (§7)
- กฎเหล็ก: **tool รายงานสำเร็จ ≠ ไฟล์เกิดจริง — `ls -la` ยืนยัน output ทุก save/export**

## 0.4 D-P3/D-P5 ROLE RULES (จาก DOC-PIPELINE)
- **D-P3 BUILD:** build ตาม spec **ห้ามแก้เนื้อหาเอง** — เจอปัญหา content → หยุด flag (content เป็นของผู้เขียนเนื้อหา — L1 ผู้คุมงาน หรือ ② ก้อง / ③ เทพ ตามชนิดเนื้อหา)
- **D-P5 FIX:** แก้**เฉพาะ**ตาม consolidated fix list ที่ L1 FINAL รายข้อแล้ว → SAVE R+1 → ⑤ อริส delta re-QA เสมอ
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
  ⚠️ ชื่อฟอนต์ในตัวอย่างข้างบนคงไว้คำต่อคำตามบทเรียนเดิม (Sarabun ถูกถอดจากตัวเลือกแล้วใน §3.0)
     — เวลาเขียนโค้ดจริงห้ามคัดลอกชื่อฟอนต์จากตัวอย่าง ให้ดึงจาก font_policy.RAILS เสมอ (§0.1 ข้อ 4)
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
  ⚠ ค่านี้ใช้กับ line-height ของกล่องข้อความ (pptx/docx) เท่านั้น — **ความสูงแถวของ .xlsx ใช้คนละค่า**
    เพราะต้องเดาจำนวนบรรทัดหลัง wrap ด้วย ดู §3.2 E2 (ค่าเริ่มต้น = auto-height · floor เมื่อตั้งเอง = 1.72)
• ⭐ Bold ไทย: Material Design แนะนำ**เลี่ยง Bold** (native speakers: หนาเกิน) →
  ใช้ SemiBold/Medium แทนถ้าฟอนต์มี (IBM Plex Looped มี Medium/SemiBold ครบ)
• Thai width budget = 1.15-1.20× Latin (คำนวณ box width)
```

## D4 — NO-OVERLAP + FONT-EMBED + STRICT VALIDATOR แก้ object ทับ + font หาย
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
สำรอง     : Leelawadee UI ตัวเดียวเท่านั้น — ⛔ Tahoma ถูกตัดออกแล้ว (คำสั่ง user 2026.08.04 · §3.0-A ขั้น 3)
            fallback คือทางสุดท้ายจริง ๆ ให้ไต่ขั้น 0-2 จนไม่ต้องใช้
หลักฐาน   : user ทดสอบผ่าน · ปตท. ใช้จริงใน 56-1 One Report · SIL OFL = embed ถูกกฎหมาย
            ยอดวรรณยุกต์ 0.864 em เทียบกล่อง 1.239 → เหลือที่ว่าง 0.375 em (สบายที่สุดในกลุ่ม)
```

### รางที่ 2 — งานราชการ / TOR / e-GP / รัฐวิสาหกิจ
```
ฟอนต์หลัก : TH Sarabun New                 ← ไม่ใช่ PSK · ⛔ ห้าม IT๙ เด็ดขาด
ขนาด      : 16pt  (= ละติน 11-12pt · วัดได้ 0.714÷0.476 = ×1.47 → ตรงธรรมเนียมพอดี)
⚠ ระวัง    : ที่ว่างหัวเหลือแค่ 0.008 em (ยอด ้ 0.836 vs กล่อง 0.844)
            → **line spacing** (pptx/docx) ต้องตั้งเผื่อเสมอ ห้ามใช้ค่า default
            → **row height ของ .xlsx ไม่ใช่กรณีเดียวกัน** — ตาม §3.2 E2 (V01R19) ค่าเริ่มต้นคือปล่อย
              auto-height เพราะการเดาจำนวนบรรทัดพลาดบ่อยกว่าที่ auto จะเผื่อไม่พอ · ฟอนต์นี้เสี่ยงกว่าตัวอื่น
              จึงบังคับให้ยืนยันด้วย render จริงก่อนส่งเสมอ (E2 ชั้น ②) — เมื่อขัดกัน **§3.2 E2 ชนะ**
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
| ~~Tahoma~~ | 0.769 | 0.805 | 23.1% ← **ตัดออกแล้ว** (คงตัวเลขไว้เป็นข้อมูลเปรียบเทียบ) |
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
   🔴 ข้อยกเว้นเดียว: การสลับฟอนต์อัตโนมัติของสไลด์แน่น (§3.0-A) ชนะกฎข้อนี้ เพราะ "อ่านออกไหม"
   สำคัญกว่า "เหมือนกันทั้งชุด" — เมื่อเกิดขึ้นต้องแจ้ง mixed-font ใน PLAN-CARD และบันทึกเหตุผลใน QA-log
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
   · 🔴 **การยกหน้าจาก deck ต้นแบบ (copy-page build) ก็อยู่ใต้กฎข้อนี้ทั้งหมด และเพิ่มสองข้อบังคับ
     (คำสั่ง user 2026.08.16 · เคส OCC):**
     (ก) **copy หน้าเสร็จ ต้องแปลงฟอนต์ทุก run ของหน้านั้นเป็นฟอนต์รางทันทีก่อน save** — ตั้งครบ
         ทั้งสามช่องตามวินัย D1 (`<a:latin>` + `<a:ea>` + `<a:cs>`) เพราะหน้าที่ยกมาแบกฟอนต์ของ
         ต้นแบบมาเต็มตัว (เคสจริง: ต้นแบบ FMCG หนึ่งหน้าถือ Open Sans + Noto Sans Thai + Tahoma +
         Arimo พร้อมกัน — ไม่มีตัวไหนอยู่บนราง)
     (ข) **ห้ามใช้เหตุผล "เนื้อหาเป็นอังกฤษล้วน" เพื่อยกเว้นการตั้งฟอนต์ตามราง** ด้วยสองเหตุผล:
         หนึ่ง รางบังคับทั้งเอกสารไม่ใช่เฉพาะตัวอักษรไทย (SINGLE-FAMILY FIRST — ฟอนต์รางตัวเดียว
         ใส่ทุก slot ทั้งเล่ม) · สอง คำว่า "อังกฤษล้วน" เป็นข้อเท็จจริงที่ต้อง**พิสูจน์ด้วยการสแกน
         อักษรไทยในไฟล์ต้นแบบจริง** (`grep` ช่วง ก-๛ ใน XML ของหน้านั้น) ไม่ใช่สมมติจากการดูผ่าน ๆ
         — เคสจริง 2026.08.16: แผนงานประกาศว่า "deck นี้ EN ล้วนจึงไม่ชน" ทั้งที่ต้นแบบหน้านั้น
         มีข้อความไทยอยู่จริง 76 จุดบนฟอนต์นอกราง — สมมติฐานที่ไม่ได้ตรวจหนึ่งบรรทัด เกือบพา
         ฟอนต์ผิดทั้งชุดผ่านเข้างาน
④ ชื่อ family ต้องเป็นชื่อจริงจาก name table — ห้ามเติม subfamily ต่อท้าย
   ❌ "IBM Plex Sans Thai Regular"  ✅ "IBM Plex Sans Thai Looped"
   (เคสจริง 2026.07.31: ไฟล์ PWA TOR Matrix ใส่ชื่อผิด → Excel substitute เงียบ → ฟอนต์ปน 3 ตัว)
```

## 3.1 DOCX — วินัยฟอนต์ (W1-W3) และวินัยตาราง (W4-W5) ฉบับ WordprocessingML
```
ทุก run set <w:rFonts> ครบ 4 attributes (คู่แฝดของ latin/ea/cs):
  <w:rFonts w:ascii="Open Sans" w:hAnsi="Open Sans"     ← EN/Latin
            w:eastAsia="Open Sans" w:cs="Sarabun"/>      ← EA + THAI ⭐
  ⚠️ ชื่อฟอนต์ในตัวอย่างข้างบนคงไว้คำต่อคำตามบทเรียนเดิม และตัวอย่างนี้เป็นการ**จับคู่สองตระกูล**
     ซึ่ง W1 ข้างล่างห้ามในงานปกติ ส่วน Sarabun ก็ถูกถอดจากตัวเลือกไปแล้ว (§3.0) — เวลาเขียนโค้ดจริง
     **ห้ามคัดลอกชื่อฟอนต์จากตัวอย่างนี้** ให้ดึงจาก font_policy.RAILS แล้วใส่ฟอนต์ตัวเดียวกันครบ
     ทั้งสี่ช่องตาม W1 (คำเตือนเดียวกับที่ §1 D1 มีอยู่แล้ว — ย้ำที่นี่เพราะผู้อ่านที่เปิดเฉพาะ §3.1
     จะไม่เห็นคำเตือนของ D1)
+ ขนาดมี 2 slot แยก (คู่แฝด D3): <w:sz> = Latin (half-points) · <w:szCs> = Thai ⭐
  → 🔴 **นโยบายปัจจุบันใช้ฟอนต์ตัวเดียวครอบสองภาษา (§3.0 SINGLE-FAMILY FIRST) กรณีนั้น
    szCs ต้องเท่ากับ sz ห้ามบวกขนาดให้ไทย** ตาม D3 ข้อ ①
  → การบวกขนาดผ่าน szCs ใช้ได้เฉพาะเมื่อ**จับคู่สองตระกูล**เพราะลูกค้าบังคับฟอนต์ละตินของแบรนด์
    และต้องคำนวณด้วยสูตร cap-ratio ของ D3 ข้อ ② ไม่ใช่บวกลอย ๆ (ตัวอย่างค่าที่ได้ sz=22 → szCs=26
    คือ 11pt กับ 13pt) — ข้อความเดิมที่เขียนว่า "TH +1-2pt" เป็นของก่อนนโยบาย single-family
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

⭐⭐ W4-W5 วินัยตาราง (V01R20 — เพิ่มเพราะช่องว่างนี้ทำให้เอกสาร Word ทุกฉบับที่เคยสร้างมามีอาการเดียวกัน)
ศัพท์ XML ที่สองข้อนี้ใช้ นิยามไว้ก่อนถึงจุดใช้งาน: `w:tbl` = ตารางหนึ่งตาราง · `w:tblPr` = กล่อง
  คุณสมบัติของตารางนั้น · `w:tblGrid` และ `w:gridCol` = โครงคอลัมน์ที่บอกความกว้างรายคอลัมน์ ·
  `w:tcW` = ความกว้างที่ตั้งไว้รายช่อง · `w:tblLayout` = วิธีที่ตัวจัดหน้าใช้ตัดสินความกว้างคอลัมน์ ·
  `w:trPr` = กล่องคุณสมบัติของแถว · `w:cantSplit` = คำสั่งห้ามแถวขาดกลางเมื่อชนขอบหน้า ·
  `w:tblHeader` = คำสั่งให้แถวหัวตารางซ้ำเมื่อขึ้นหน้าใหม่ (คนละเรื่องกับ w:cantSplit และทำงานถูก
  อยู่แล้ว ไม่ต้องแก้) · autofit = โหมดที่ตัวจัดหน้าคำนวณความกว้างคอลัมน์เอง ซึ่งเป็นค่าเริ่มต้นของ Word

W4 🔴 ทุกตารางตั้งแต่ 2 คอลัมน์ขึ้นไป ผู้ build ต้องตั้ง <w:tblLayout w:type="fixed"/> ใน w:tblPr
   พร้อมเขียน w:tblGrid ใหม่ให้ครบทุกคอลัมน์ และตั้ง w:tcW ทุกช่อง — ทำสามอย่างนี้ในรอบเดียว
   ตอนสร้างตาราง
   เหตุผล: ไม่ตั้ง = ตัวจัดหน้าใช้โหมด autofit แล้ว **เฉลี่ยทุกคอลัมน์เท่ากัน โดยทิ้งความกว้าง
   ที่เราตั้งไว้ทั้งหมด** · การตั้ง w:tcW รายช่องอย่างเดียวไม่ช่วย เพราะค่านั้นถูกทิ้งไปพร้อมกัน
   เคสจริง (งาน OCC Minutes of Meeting V01R01 · 2026.08.31 · ผู้ตรวจวัดจาก PDF ที่ render สด):
   ตั้งไว้ 1.4/5.0/7.0/3.0 ซม. แต่ออกมา 4.2 ซม. เท่ากันทุกคอลัมน์ → คอลัมน์ "ลำดับ" ที่มีเลข
   หลักเดียวได้พื้นที่เท่ากับคอลัมน์ข้อความยาว 144 อักขระ ซึ่งห่อบรรทัดจนแถวสูงผิดสัดส่วนทั้งตาราง
   ❌ ผิด: ตั้ง `cell.width` ของ python-docx ให้ครบทุกช่องแล้วถือว่าจบ — ค่าถูกทิ้งทั้งหมด
   ✅ ถูก: ตั้ง w:tblLayout เป็น fixed → ลบ w:tblGrid เดิมแล้วเขียนใหม่ตามค่าจริง → ตั้ง w:tcW ทุกช่อง
      (โค้ดที่พิสูจน์แล้วว่าใช้ได้คือฟังก์ชัน `fix_layout()` ใน build script ของงาน OCC)
   🔴 อ่านคู่กับกติกา TABLE WIDTH ของ V01R17 ที่หัวไฟล์: เมื่อความกว้างไม่พอ **ห้ามไล่แก้ทีละ
   คอลัมน์** เพราะการขยายคอลัมน์หนึ่งโดยหักจากอีกคอลัมน์คือการย้ายรอยตัดไปโผล่ที่ใหม่ ให้วัด
   ความกว้างขั้นต่ำของทุกคอลัมน์พร้อมกันแล้วตั้งใหม่ครั้งเดียว · ผลรวมความกว้างทุกคอลัมน์ต้อง
   ไม่เกินความกว้างกรอบพิมพ์ ซึ่งเท่ากับความกว้างกระดาษลบขอบซ้ายลบขอบขวา

W5 ⭐ แถวเนื้อหาทุกแถว ผู้ build ต้องตั้ง <w:cantSplit/> ใน w:trPr ตอนสร้างตาราง ยกเว้นแถว
   หัวตารางที่ใช้ w:tblHeader อยู่แล้ว
   เหตุผล: ไม่ตั้ง = แถวที่ยาวและบังเอิญไปตกขอบหน้าจะถูกหั่นครึ่ง ข้อความส่วนหลังไปโผล่ใต้หัวตาราง
   ของหน้าถัดไป เหลือช่องว่างเปล่าข้าง ๆ ผู้อ่านเห็นเป็นตารางพัง
   เคสจริงชุดเดียวกัน: พบ 8 จุดใน 2 ไฟล์ ตั้ง w:cantSplit แล้วเหลือ 0 จุด
   ❌ ผิด: ปล่อยแถวตามค่าเริ่มต้น แล้วรอดูว่าหน้าไหนจะพัง
   ✅ ถูก: ตั้ง w:cantSplit ทุกแถวเนื้อหาตั้งแต่ตอนสร้าง (ฟังก์ชัน `no_split()` ในงานเดียวกัน)
   ⚠ ข้อแลกเปลี่ยนที่ต้องรู้ล่วงหน้า: แถวที่สูงเกินหนึ่งหน้ากระดาษจะถูกดันไปทั้งแถว ทิ้งช่องว่าง
   ท้ายหน้าก่อน → มีแถวสูงขนาดนั้นให้แก้ที่เนื้อหาโดยแยกเป็นหลายแถว **ห้ามถอด w:cantSplit ออก**

VALIDATOR DOCX เพิ่ม: ✓ ทุก run มี cs font ที่เป็น Thai-capable
  ✓ ไม่มี "Calibri"/"Cambria" เหลือ (python-docx default leak)
  ✓ szCs เทียบ sz ให้ตรงนโยบายที่ใช้จริง — **ฟอนต์ตัวเดียวครอบสองภาษา (ค่าเริ่มต้น) ต้อง szCs = sz
    เท่านั้น** · szCs > sz ถูกต้องเฉพาะงานที่จับคู่สองตระกูลตาม D3 ข้อ ② และต้องบันทึกเหตุผลไว้
    ⚠️ เกณฑ์เดิมที่เขียนว่า "szCs ≥ sz" หลวมเกินไป เพราะปล่อยให้ไฟล์ที่บวกขนาดให้ไทยทั้งที่ใช้ฟอนต์
    ตัวเดียวผ่านด่านไปได้ ทั้งที่ผิดนโยบาย — ช่องเดียวกับที่ V01R06 เจอกับ V4 RAIL CONFORMANCE
  ✓ styles.xml rPrDefault ครบ 4 slots
  ✓ W4 ทุกตารางตั้งแต่ 2 คอลัมน์ขึ้นไปมี w:tblLayout เป็น fixed ✓ W5 แถวเนื้อหามี w:cantSplit
  🔴 **แยกให้ชัดว่าข้อไหนมีด่านอัตโนมัติ และข้อไหนไม่มี** — เพราะ "เครื่องมือขึ้นผ่าน" ไม่ได้แปลว่า
    ครบทุกข้อในรายการข้างบน:
      **มีด่านตรวจให้:** W1 · W4 · W5 · และด่านฟอนต์ V1/V2/V4
      **ไม่มีด่านตรวจ ผู้ build ต้องถือเอง:** W2 (`bCs`/`iCs` คู่กับ `b`/`i`) · W3 (ห้าม `lineRule="exact"`
        ในย่อหน้าที่มีไทย) · เกณฑ์ `szCs` เทียบ `sz` · การไม่มี Calibri/Cambria หลงเหลือ ·
        `styles.xml` rPrDefault ครบสี่ช่อง
    หลักเดียวกับข้อ 8 ของ §0.1: **การที่เครื่องจับไม่ได้ ไม่ได้แปลว่าได้รับยกเว้น**
  วิธีตรวจ W1 W4 W5 — ข้อเท็จจริงอยู่ในเครื่องมือ ไม่ใช่ในข้อความนี้ (มาตรฐานการเขียนไฟล์ระบบ ข้อ 7):
    คำสั่ง:  python3 ~/.claude/agents/_lib/audit_fonts.py --rail <private|govt> FILE.docx
    จะได้:   ผลฟอนต์ V1/V2/V4 · **FAIL W4** พร้อมเลขตารางและจำนวนคอลัมน์ของตารางที่ยังไม่ fixed ·
             **FAIL W5** พร้อมจำนวนแถวเนื้อหาที่ยังไม่ได้ตั้ง w:cantSplit
    ไม่ผ่าน: แก้ตาม W4 และ W5 ข้างบน แล้วรันคำสั่งเดิมซ้ำจนได้ PASS
  🔴 แยกสองคำถามนี้ให้ขาดจากกัน ห้ามเอามาปนกัน:
    ① **"กฎถูกปฏิบัติตามหรือไม่"** — ตอบได้แน่นอนจากตัวไฟล์ทั้ง W4 และ W5 เพราะเป็นการดูว่ามีหรือ
       ไม่มีคำสั่งนั้นเขียนอยู่ · ด่านตรวจตอบคำถามนี้ ทั้งสองข้อจึงเป็น **ความล้มเหลว** เท่ากัน
    ② **"เกิดความเสียหายขึ้นจริงหรือยัง"** — เช่นแถวนั้นขาดกลางหน้าจริงไหม คอลัมน์เบียดจนอ่านไม่ออก
       ไหม · **ด่านตรวจตอบไม่ได้** เพราะขึ้นกับการแบ่งหน้าและการวัดผลบนหน้ากระดาษจริง คำตอบมาจาก
       การ render เท่านั้น (§7)
    ⚠️ ความไม่แน่นอนของคำถาม ② **ห้ามนำมาลดระดับการตรวจของคำถาม ①** — กฎที่บังคับไว้แล้วว่าต้องทำ
    ถ้าไม่ทำก็คือไม่ทำ ไม่ต้องรอดูว่าโชคดีไม่พังหรือเปล่า (บทเรียนแม่ของ V01R19 บอกว่าห้ามให้ตัวตรวจ
    อ้างสิ่งที่มันรู้ไม่ได้ — ไม่ได้บอกให้ปล่อยสิ่งที่มันรู้ได้ผ่านไป)
  **ใครเป็นคน render:** ⑤ อริส ในรอบตรวจ **ไม่ใช่ผู้ build** (§0.3 NO SELF-RENDER และ §1 D4) —
    หน้าที่ของผู้ build จบลงที่รันคำสั่งตรวจข้างบนให้ผ่าน แล้วส่งไฟล์เข้า ⑤ · ยกเว้นสองกรณีตาม §0.3
    คือ CB Progressive per-unit preview และกรณีที่ user สั่ง preview เองอย่างชัดเจน
EMBED ⚠ (แก้ V01R02 — พิสูจน์แล้วว่า "ทำได้เหมือน pptx" = ผิด): DOCX ห้ามฝัง font parts (odttf) ด้วยมือ
  — Word ปฏิเสธทั้งไฟล์ (เคสจริง VFIN V02R02 §2B.1) · flag settings ต้องวางถูกลำดับ CT_Settings (§2B.1) ·
  ทางที่ใช้ได้จริง: (ก) user ให้ Word GUI embed เอง (Preferences>Save) หรือ (ข) PDF companion (Method C) ⭐ default
  🔴 **.docx ที่ส่งลูกค้า = แนบ PDF companion เสมอ ไม่ใช่ทางเลือก** ด้วยเหตุผลเดียวกับ .xlsx ใน §3.2 E1
  คือฝังฟอนต์ด้วยสคริปต์ไม่ได้ ไฟล์ .docx จึงเป็นฉบับให้แก้ต่อ ส่วน PDF คือฉบับที่ลูกค้าเห็นแล้วถูกเสมอ
  (ข้อบังคับนี้ประกาศไว้แล้วที่ §3.0-A ขั้น 2 ซึ่งครอบทั้งสองฟอร์แมต — เขียนซ้ำที่นี่เพราะ E1 ที่ถูกอ้าง
  ถึงเขียนถึง .xlsx อย่างเดียว ผู้อ่านที่ตามไปอ่าน E1 จึงไม่พบข้อบังคับฝั่ง .docx) · ประโยชน์พ่วง:
  PDF ปิดความเสี่ยงเรื่องการตัดคำไทยของ Word บนเครื่องผู้รับที่เราควบคุมไม่ได้ไปพร้อมกัน
```

## 3.2 XLSX — ⭐ เขียนใหม่ V01R03 (E1-E6 · จากหลักฐาน Microsoft + เคสจริง PWA TOR Matrix)

> **ทำไม Excel ยากที่สุดใน 3 ฟอร์แมต:** (ก) เซลล์มีฟอนต์ได้**ชื่อเดียว** ไม่มี slot ไทยแยกเหมือน pptx/docx — ยืนยันจาก MS-XLSX + `openpyxl.styles.fonts.Font.__elements__` ไม่มี cs/ea/latin (ข) **ฝังฟอนต์ไม่ได้เลย** (ค) ตัว `ht` มีหน่วยเป็น point ตามสเปก แต่**ไม่มีสูตรทางการว่าฟอนต์ขนาดหนึ่งต้องใช้แถวสูงเท่าไร** — สูตรใน ECMA-376 กับใน MS-OI29500 ให้ค่าไม่ตรงกันและคำนวณจริงแล้วไม่ตรงทั้งคู่ (ยืนยันโดยผู้พัฒนา library OOXML) ⇒ ความสูงที่พอดีต้องได้จากการ render เท่านั้น

```
พื้นฐาน:
  • เซลล์ที่มีไทย (แม้ปนนิดเดียว) → ฟอนต์ Thai-capable ตาม §3.0 · ห้ามหวังพึ่ง fallback
  • ทำผ่าน NamedStyle (header/body/number/thai-note) — ห้าม set ราย cell แบบ ad-hoc
  • theme1.xml minorFont/majorFont ตั้งเป็น approved set (กัน Calibri/Aptos โผล่ในกราฟ/element ใหม่)
  • ⚠ tri-slot (latin/ea/cs) มีอยู่ใน .xlsx จริง แต่**เฉพาะ DrawingML** (กราฟ/shape/text box)
    — ใช้กับ "ค่าในเซลล์" ไม่ได้ · เอา discipline จาก pptx มาใช้ตรง ๆ = ทำงานเงียบ ๆ แต่ไม่มีผล

E1 ⛔ EXCEL ฝังฟอนต์ไม่ได้ทุกแพลตฟอร์ม (Microsoft รองรับ embed เฉพาะ Word/PowerPoint)
    → **.xlsx ที่ส่งลูกค้า: แนบ PDF companion เสมอ ไม่ใช่ทางเลือก** (PDF ฝังฟอนต์ 100% — ตรวจด้วย §3.3)
      เพราะฟอนต์ในรางทั้งสอง (IBM Plex Sans Thai Looped · TH Sarabun New) เป็น proprietary
      ส่งไฟล์ฟอนต์ให้ลูกค้าติดตั้งไม่ได้ → ไฟล์ .xlsx เป็นฉบับให้แก้ต่อ · PDF เป็นฉบับที่ลูกค้าเห็น
    → ถ้าจำเป็นต้องพึ่งฟอนต์ที่เครื่องลูกค้ามีอยู่แล้ว ให้เลือกตาม §3.0-A ขั้น 3 (ผู้รับ Windows = `Leelawadee UI`)
      ⛔ **ห้ามใช้ Tahoma** — ถูกตัดออกจากนโยบายแล้วตามคำสั่ง user 2026.08.04 (ข้อความเดิมของ E1 ที่แนะนำ
      Tahoma เป็นข้อความค้างจากก่อนนโยบายเปลี่ยน · เก็บบันทึกไว้ที่ §3.0-A)
    → ไฟล์ภายใน/ไฟล์ทำงาน = ใช้ฟอนต์ตามนโยบายได้เต็มที่ ไม่ต้องแนบ PDF

E2 ⭐ ความสูงแถวต้องพอกับข้อความจริง — ตัดสินที่ผลลัพธ์ ไม่ใช่ที่วิธีตั้งค่า
    กฎ: ห้ามมีแถวใดที่ข้อความถูกเฉือน จะได้ความสูงมาด้วยวิธีใดก็ได้ ขอให้ผลถูก
    ค่าเริ่มต้น = ⭐ **ไม่ตั้งความสูง ปล่อยให้โปรแกรมคำนวณเอง (auto-height)**
      เหตุผล: การตั้งเองต้องเดา "จำนวนบรรทัดหลัง wrap" ซึ่งขึ้นกับความกว้างคอลัมน์ ฟอนต์ และการตัดคำไทย
      พร้อมกันทั้งสามอย่าง — การเดานี้เองคือสิ่งที่พลาด ไม่ใช่ตัวคูณ
    หลักฐานที่เปลี่ยนกฎข้อนี้ (CP Axtra Requirement Baseline 2026.08.30 · ⑤ อริสตรวจ 3 รอบด้วย render จริง):
      สูตร ×1.45 → เฉือน 83/112 แถว · สูตร ×1.72 → เฉือน 52/140 แถว · auto-height → เฉือน 0/140 แถว
      เคสร้ายที่สุดคือแถวที่ขาดเพียง 1-6 pt: สระบนและวรรณยุกต์หายทั้งบรรทัด ผู้อ่านอ่านผิดโดยไม่มีช่องว่างให้สังเกต
      (แถวที่ขาดมาก ๆ ยังเห็นว่าตัว ส่วนแถวที่ขาดนิดเดียวกลับอันตรายกว่า)
    หมายเหตุแก้ความเข้าใจเดิม: กฎเก่าให้เหตุผลว่า "AutoFit คำนวณจากบรรทัดละติน จึงเผื่อที่ไม่พอโดยโครงสร้าง"
      — วัดจริงกับฟอนต์ตามราง §3.0 แล้วพบว่า AutoFit เผื่อพอ ที่ไม่พอคือการเดาจำนวนบรรทัดของเราเอง
      ห้ามย้อนกลับไปบังคับตั้งความสูงเองด้วยเหตุผลข้อนั้นอีก
    ตั้งความสูงเองได้ใน 3 กรณีนี้เท่านั้น:
      (ก) แถวที่มี merged cell **และไม่มีข้อความไทยที่ wrap** — AutoFit ถูกปิดใช้งานที่นั่น ไม่ตั้ง = ไม่มีอะไรกู้
          🔴 ถ้าแถว merge นั้นมีไทย + wrap ห้ามใช้ทางนี้ เพราะ **E4 ห้าม merge แบบนั้นตั้งแต่ต้น**
             ให้เปลี่ยนไปใช้ "Center Across Selection" ตามที่ E4 เสนอ แล้วแถวนั้นจะกลับไปใช้ auto ได้ตามปกติ
             (กรณี banner ไทยจึงไม่เข้าข้อ (ก) — เข้าข้อ (ข) เมื่อดีไซน์บังคับความสูง หรือไม่ต้องตั้งเลย)
      (ข) แถว banner หรือหัวเรื่องที่ดีไซน์กำหนดความสูงคงที่
      (ค) งานที่ต้องการให้แบ่งหน้าตรงกันเป๊ะทุกเครื่อง (ดูข้อแลกเปลี่ยนย่อหน้าถัดไป)
      เมื่อตั้งเอง ใช้ floor = pt × 1.72 × บรรทัด + 6 · ทุกค่าเป็น point และเขียนลงไฟล์เป็น point ตรง ๆ
      (คุณสมบัติความสูงแถวของ openpyxl รับหน่วย point) · 1.72 คือค่าที่วัดจากงานจริง — 1.45 ของเดิมต่ำเกินไป
      · "+6" คือระยะเผื่อขอบบน-ล่างของเซลล์
      ✅ **ยืนยันกับ Excel ตัวจริงแล้ว (2026.08.30)** — ข้อกังวลว่า "auto-height อาจเป็นพฤติกรรมของ LibreOffice
        เท่านั้น" ไม่เป็นจริง: เปิดไฟล์ใน Microsoft Excel แล้วอ่านความสูงที่มันคำนวณ ได้ **แถวสั้น 21.0 pt ·
        แถวข้อความยาวที่ wrap 84.0 pt** (LibreOffice ให้ 20.1 และ 76.1 — Excel เผื่อมากกว่าราว 10%)
        ⇒ ไฟล์ที่ผ่านการวัดด้วย LibreOffice จะปลอดภัยใน Excel ด้วย
        กลไก: แถวที่ไม่ได้ตั้งความสูงจะไม่มีแอตทริบิวต์ `customHeight="1"` ซึ่งเป็นธงสั่ง "ห้าม auto-fit"
        — ไม่มีธงนี้ โปรแกรมจึงคำนวณเองทุกตัว (ตรวจได้ด้วย
        `unzip -p FILE.xlsx xl/worksheets/sheet1.xml | grep -o 'customHeight="1"' | wc -l`)
      ⭐ **การขึ้นบรรทัดใหม่ในเซลล์ (\n) นับได้แน่นอน ไม่ใช่การพยากรณ์** — ตัวตรวจคูณพื้นด้วยจำนวนบรรทัดที่ขึ้นใหม่จริง
        และ builder ตั้งความสูงให้แถวหลายบรรทัดอัตโนมัติ · เดิมแถวที่บรรจุ 3 บรรทัดแต่ตั้งความสูงเท่าบรรทัดเดียวลอดด่านไปได้
      📏 ความสูง **หนึ่งบรรทัด** ที่วัดจริงด้วย LibreOffice (2026.08.30 · วิธีวัด = ล้างความสูงแล้วให้ LO คำนวณ
        ตามขั้นตอนของ `xlsx_rowheight_probe.py` — ใช้เทียบว่าค่าที่ตั้งสมเหตุสมผลไหม):
        IBM Plex Sans Thai Looped 9pt = 15.0 · 11pt = 20.1 · 14pt = 24.6 · 16pt = 26.9
        TH Sarabun New 11pt = 16.4 · 16pt = 22.4   (หน่วย point ทั้งหมด)
      ⚠ **"บรรทัด" ในสูตรนี้เอามาจากไหน** — คำถามนี้สำคัญเพราะ E2 เพิ่งบอกเองว่าการเดาจำนวนบรรทัดคือรากปัญหา
        คำตอบ: **ห้ามเดา** ทั้ง 3 กรณีข้างบนเป็นกรณีที่จำนวนบรรทัด**รู้ล่วงหน้าอยู่แล้ว** — (ก) และ (ข) เป็นแถว
        ที่เราออกแบบเองว่าให้สูงกี่บรรทัด ส่วน (ค) ให้ปล่อย auto สร้างไฟล์รอบแรก render ดูว่าจริง ๆ กี่บรรทัด
        แล้วค่อยตรึงค่านั้นลงไป · ถ้าตอบไม่ได้ว่าแถวนั้นกี่บรรทัด แปลว่าแถวนั้นไม่ควรตั้งเอง ให้ปล่อย auto
    ⚠ ข้อแลกเปลี่ยนที่ทำให้เกิดกรณี (ค): ไฟล์ที่ไม่มีความสูงตายตัวจะ**แบ่งหน้าไม่เหมือนกันเป๊ะทุกเครื่อง**
      เพราะความสูงจริงขึ้นกับ Excel/LibreOffice ของเครื่องนั้น → ถ้าต้องการหน้าตรงกันทุกเครื่อง
      ให้ตั้งเองด้วย floor ข้างบน แล้วพิสูจน์ด้วยการ render ตามข้อ ② ด้านล่าง
    ⚠ TH Sarabun New 16pt (ที่ว่างหัวเหลือ 0.008 em) เสี่ยงกว่าฟอนต์อื่น — ต้องดู render ก่อนส่งเสมอ
    วิธีตรวจ 2 ชั้น:
      ① สถิต — `python3 ~/.claude/agents/_lib/audit_fonts.py --rail <ราง> FILE.xlsx`
         จะได้: จำนวนแถวที่ปล่อย auto และจำนวนแถวที่ตั้งความสูงเอง · และ **FAIL E2** เมื่อพบแถวที่ตั้งเอง
                แล้วสั้นผิดปกติจนไม่พอแม้แต่บรรทัดเดียว พร้อมตำแหน่งเซลล์และค่าพื้น
                **พื้นคำนวณจากไฟล์ฟอนต์จริงตอนรัน** (hhea: ascender − descender + lineGap ÷ unitsPerEm × pt)
                ไม่ใช่ค่าคงที่ เพราะค่าที่ถูกของฟอนต์หนึ่งผิดสำหรับอีกฟอนต์ — IBM Plex Sans Thai Looped = 1.650
                · TH Sarabun New = 1.331 ต่างกัน 24% · อ่าน metric ไม่ได้จึงถอยไปใช้ค่าคงที่ 1.35 ซึ่งต่ำกว่าทุกฟอนต์ที่วัด
                (เคยตั้งพื้นเป็น pt × 1.72 + 6 ซึ่ง **ผิด** — 1.72 วัดจาก IBM Plex ตัวเดียวแล้วเอาไปใช้ข้ามฟอนต์
                 เกินจริงเกือบ 40% บน TH Sarabun New และ "+6" นับ padding ซ้ำกับที่ ink box รวมไว้แล้ว)
         ถ้า FAIL: ขยายแถวนั้นให้ถึงค่าที่บอก หรือเปลี่ยนมาปล่อย auto แล้วรันคำสั่งเดิมซ้ำจนผ่าน
         🔴 สิ่งที่ด่านนี้ **บอกไม่ได้** และห้ามเข้าใจผิด: มันไม่รู้ว่าข้อความถูกเฉือนหรือไม่เมื่อ wrap หลายบรรทัด
            เพราะการพยากรณ์การตัดบรรทัดภาษาไทยจากข้อมูลสถิตพลาดทั้งสองทาง — วัดกับไฟล์จริงเทียบผล render
            (CP Axtra 2026.08.30 · ของจริงเฉือน 52 แถว): นับอักขระดิบ → ฟ้อง 105 แถว (เกินจริงราวสองเท่า)
            · ตัดสระ/วรรณยุกต์ที่กว้าง 0 แล้วใช้อัตราส่วนที่วัดจากไฟล์ฟอนต์จริง (ไทย ÷ '0' = 1.058)
              → ฟ้อง 7 แถว (ต่ำกว่าจริงมาก)
            สาเหตุ: หน่วยความกว้างคอลัมน์ของ Excel ไม่ใช่จำนวนตัวอักษร และ LibreOffice ตัดบรรทัดไทย
            ด้วยพจนานุกรม ไม่ใช่ตามจำนวนอักขระ
            ⇒ **ข้อ ② เป็นด่านเดียวที่ตอบเรื่องการเฉือนได้** · validator เขียวไม่ใช่หลักฐานว่าข้อความครบ
      ② ผลจริง (บังคับสำหรับงานส่งลูกค้า ทุกขนาด — ข้อนี้ชนะข้อยกเว้น SCALE-TO-SIZE ใน §6 ข้อ 3
         ที่ให้ข้ามการ render สำหรับไฟล์เล็ก เพราะการเฉือนข้อความไม่ขึ้นกับจำนวนแถว)
         **②ก ตรวจความสูงแถวด้วยเครื่องมือ (ทำก่อน เพราะให้คำตอบเป็นตัวเลขรายแถว):**
         `python3 ~/.claude/agents/_lib/xlsx_rowheight_probe.py FILE.xlsx`
         วิธีทำงาน: คัดลอกไฟล์ → ล้างความสูงแถวทิ้ง → ให้ LibreOffice ตัวจริงคำนวณ auto-height ใหม่
           → เทียบกับความสูงที่ไฟล์ตั้งไว้ · ต่ำกว่า = ข้อความถูกเฉือนจริง
         จะได้: รายชื่อแถวที่ไม่พอ พร้อมค่าที่ตั้งไว้และค่าที่ต้องการ (exit 3 เมื่อพบ · exit 0 เมื่อผ่าน)
         ถ้าพบ: ปล่อยแถวนั้นเป็น auto-height (แนะนำ) หรือขยายให้ถึงค่าที่ระบุ แล้วรันซ้ำจนได้ exit 0
         ⚠ ผู้ตัดสินคือ LibreOffice ไม่ใช่ Excel — ค่าอาจต่างจาก Excel เล็กน้อย แต่เป็นหลักฐานที่วัดได้จริง
           และแม่นกว่าการประมาณจากจำนวนอักขระอย่างเทียบไม่ติด (เคสจริง: ประมาณได้ 105 หรือ 7 · probe ได้ 43
           เทียบกับที่ผู้ตรวจนับจากภาพ 52 — คนละชุดแถวที่วัด แต่อยู่ในระดับเดียวกัน)
         **②ข ดูภาพจริง (ทำหลัง เพื่อจับสิ่งที่ตัวเลขไม่บอก เช่นวรรณยุกต์ชนขอบ):**
         `bash ~/.claude/agents/_lib/render_pdf.sh FILE.xlsx OUTDIR --expect "<ชื่อฟอนต์>" --strict-fonts`
         ⚠ "<ชื่อฟอนต์>" ต้องเป็นชื่อที่ปรากฏใน PDF ไม่ใช่ชื่อที่เราตั้งในไฟล์ (เช่น `IBM Plex Sans Thai Looped`
           ปรากฏเป็น `IBMPlexSansThaiLooped`) — ยังไม่รู้ชื่อ ให้ render เปล่าหนึ่งครั้งแล้วอ่านจากตาราง
           ที่ helper พิมพ์ออกมา จากนั้นค่อยรันซ้ำพร้อม --expect (การรันสองรอบนี้เป็นข้อยกเว้นที่ยอมรับได้)
         จะได้: PDF ที่ render ด้วย LibreOffice ตัวจริง + รายการฟอนต์ที่ฝัง + ด่านฟอนต์แปลกปน (ดู §7)
         ถ้ายังเฉือน: เปิดแถวที่ข้อความยาวสุดดู ถ้าสระบน/วรรณยุกต์หาย ให้กลับไปแก้แล้ว render ซ้ำ
         (ดูภาพจริงรายหน้า: `pdftoppm -r 130 -png OUT.pdf หน้า` แล้วเปิดดูแถวที่ยาวที่สุด)
    ❌ ผิด: ตั้ง `ws.row_dimensions[r].height = pt × 1.45 × (เดาว่า 2 บรรทัด)` ทุกแถว แล้วถือว่าจบเพราะ validator เขียว
    ✅ ถูก: ปล่อย auto สำหรับแถวข้อความยาว · ตั้งเองเฉพาะแถว merge/banner ด้วย floor 1.72 · แล้วยืนยันด้วย render จริง

E3 ⭐ vertical = "center" ทุกเซลล์ที่มีไทย
    เหตุผล 2 ชั้น — (ก) **มีเอกสารยืนยัน:** ค่าเริ่มต้นของ Excel คือ bottom
    (ข) **เป็นผลสืบเนื่องเชิงกลไก ไม่ใช่ข้อความของ Microsoft:** เมื่อยึดกล่องข้อความที่พื้นเซลล์
    ส่วนที่เกินจะถูกตัดด้านบน ซึ่งคือที่อยู่ของวรรณยุกต์ — **ยืนยันด้วยหลักฐานของเราเอง** จาก QA
    งาน CP Axtra ที่บันทึกอาการตรงกันว่า "สระบนและวรรณยุกต์หายทั้งบรรทัด" 

E4 🔴 ห้าม merge cell ในแถวที่มีไทย + wrap
    Microsoft ยืนยัน: AutoFit ความสูงแถว **ถูกปิดใช้งาน** ในแถว/คอลัมน์ที่มี merged cell
    และ Wrap Text ก็ไม่ขยายแถวที่ merge → แถวโดนตัดโดยการออกแบบ
    ทางเลือกแทน merge: "Center Across Selection" (จัดกลางข้ามคอลัมน์โดยไม่ merge จริง)

E5 🔴 ห้ามใช้ "Shrink to fit" กับเซลล์ไทย
    มันย่อขนาดฟอนต์ → วรรณยุกต์เล็กลงอีก = แย่ที่สุดในบรรดา 4 วิธีที่ Microsoft เสนอ

E6 ตั้ง default font ของ workbook **ก่อน** คำนวณความกว้างคอลัมน์
    เหตุผล: หนึ่งหน่วยความกว้างคอลัมน์ = ความกว้างของอักขระ **"0" (ศูนย์) ในฟอนต์ของ Normal style**
    บวก padding เป็นพิกเซล (default 8.43) — คือ "จำนวนตัวอักษรของฟอนต์เริ่มต้น"
    **ไม่ใช่จำนวนตัวอักษรของข้อความที่เราพิมพ์** (จุดนี้เป็นเหตุผลหนึ่งที่ประมาณจำนวนบรรทัดจากความยาวข้อความไม่ได้)
    → เปลี่ยน default ทีหลัง = ทุกคอลัมน์ขยับเงียบ ๆ

VALIDATOR XLSX (→ §6 V1-V3):
  ✓ V1 ทุกชื่อฟอนต์ resolve ได้จริง  ✓ V2 ไม่มีตัวใน blacklist  ✓ ไม่มี Calibri/Aptos leak
  ✓ เซลล์ไทยทุกเซลล์ได้ฟอนต์ Thai-capable
  ✓ E2 ไม่มีแถวที่ตั้งความสูงเองแล้วต่ำกว่าพื้นหนึ่งบรรทัด (pt × 1.72 + 6) · แถวที่ปล่อย auto = ผ่าน
    ⚠ ด่านนี้ **ไม่ได้ตรวจ**การเฉือนจาก wrap — เรื่องนั้นตอบได้จาก render เท่านั้น (E2 ชั้น ②)
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

**กติกาบังคับ (แยกตามฟอร์แมต):** `.xlsx` → **รัน T2 audit ก่อนส่งเข้า ⑤ อริส เสมอ** เพราะข้อความถูกบีบอยู่ในความกว้างคอลัมน์ที่ตายตัว · `.pptx` และ `.docx` → ใช้ **T1 lang-tag `th-TH`** บนทุก run ที่มีข้อความไทยก็เพียงพอ (โปรแกรมตัดคำให้เอง) แล้วให้ ⑤ ตรวจด้วยตาในรอบ render · เจอเสี่ยง → แก้ตามลำดับ ① ขยายคอลัมน์ ② ปรับข้อความ ③ ZWSP (ต้องบอก user ว่าแลกอะไร)

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
BUILD PIPELINE: Pre-Flight → build per-section (18 lessons + D1-D4) → merge+page+font-embed → STRICT VALIDATOR → ส่ง ⑤ อริส
EDIT PIPELINE:  open VALID base (PowerPoint-Repaired ถ้ามี) → python-pptx API edit → re-verify corruption → ส่ง ⑤ อริส

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
| **Pitch deck / นำเสนอลูกค้า** | .pptx (หรือ html demo) | slide-designer (รวมด่านตรวจก่อนสร้าง deck ไว้ที่หัวข้อ 4.4 แล้ว) + presentation-creator | `_lib/build_pptx.py` หรือ HTML | Bilingual |
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
| **แผนภาพ (diagram) / ผังกระบวนการ (flow)** ⭐ | HTML+SVG ในตัวเอง (แปลงเป็น .png/.svg ได้เมื่อสั่ง) | **`diagram-design`** (39 ชนิด) | skill เขียนไฟล์ HTML เอง — ไม่ใช้ `_lib/build_*.py` | ตามผู้อ่าน |

**กฎเสริม (ทุกแถว):** Font ทุก customer-facing → slide-designer §5.5.1 single-source → D1-D4 (pptx) / §3.1 (docx) / §3.2 (xlsx) · design-principles.md (20 rules) = format-agnostic · ภาษาไฟล์ถามก่อน (H6 เว้น 3 ข้อยกเว้น) · ไม่แน่ใจ format/ประเภท → ถาม · AI imagery → higgsfield (หลัก) / gemini (fallback) — preflight cost ก่อน · **build tools = `~/.claude/agents/_lib/build_*.py` (SSOT — อยู่ที่เดิม)**

---

## 5.1 ⭐ ตารางกรณีใช้ `diagram-design` — บ้านเดียวของกติกานี้ (V01R21 · คำสั่ง user 2026.09.01)

**`diagram-design` คืออะไร:** skill ในกลุ่ม `ice-tools` ที่ถือความรู้การออกแบบแผนภาพ 39 ชนิด ผลลัพธ์เป็นไฟล์ HTML ที่มีภาพ SVG อยู่ในตัวเองไฟล์เดียว (แปลงเป็น .png หรือ .svg ได้เมื่อผู้ใช้สั่งเท่านั้น) ตัว skill ถือกฎสามชั้นที่ทำให้ภาพไม่ออกมาเป็นงาน AI สำเร็จรูป ได้แก่ การเลือกชนิดแผนภาพให้ตรงเรื่อง งบความซับซ้อน (จำกัดจำนวนกล่องและลูกศรต่อภาพ) และกฎเส้นเชื่อมหกข้อ (เส้นหักมุมฉากเท่านั้น ห้ามเส้นทแยง ห้ามเส้นทับกัน) นอกจากนี้ยังอ่านไฟล์ `.drawio` และ Mermaid (`.mmd`) เข้ามาวาดใหม่ได้ **โหลดก่อนเขียน design spec เสมอตามเงื่อนไข §0.1 ข้อ 8**

### ✅ กรณีที่ต้องใช้ `diagram-design`

| กลุ่มกรณี | ตัวอย่างงานจริงของทีม |
|---|---|
| **สถาปัตยกรรมและระบบ** | ผังสถาปัตยกรรมโซลูชัน · ผังระบบปัจจุบันเทียบระบบปลายทาง (As-Is / To-Be) · ผังการติดตั้ง · ผังการเชื่อมต่อระหว่างระบบ · ผังความสัมพันธ์ฐานข้อมูล (ER / DB schema) · ผังการพึ่งพากันของส่วนประกอบ |
| **กระบวนการและการไหล** | ผังกระบวนการธุรกิจ · flowchart · swimlane (แบ่งเลนตามผู้รับผิดชอบ) · ผังการไหลของข้อมูล · sequence diagram · state machine · เส้นทางประสบการณ์ผู้ใช้ (user journey) |
| **โครงสร้างและลำดับชั้น** | ผังองค์กร · ผังต้นไม้ · ผังชั้น (layer stack) · ผังกล่องซ้อน · kanban |
| **ภาพเชิงวิเคราะห์สำหรับผู้บริหาร** | quadrant สองแกน · radar / spider · Venn · พีระมิด / funnel · timeline และ roadmap · Gantt แบบไฟล์เดี่ยว · loop / flywheel · Wardley map · fishbone |
| **งานวิชาการ (persona = สมนึก)** | กรอบแนวคิดการวิจัย · ผังขั้นตอนการวิจัย · ผังก้างปลาหาสาเหตุ |
| **วาดใหม่จากไฟล์ที่ได้รับ** | ลูกค้าหรือทีมส่งไฟล์ `.drawio` หรือ Mermaid `.mmd` มา แล้วต้องการฉบับที่นำเสนอได้ — skill มีตัวสกัดเนื้อหาในตัวและ **วาดใหม่ ไม่ใช่แปลงไฟล์ตรง ๆ** (สิ่งที่ต้องถามก่อนวาด อยู่ใต้ตารางนี้) |

### ❌ กรณีที่ไม่ใช่ของ skill นี้ — ให้ไปเส้นทางเดิม

| กรณี | ไปที่ | เหตุผลที่แยก |
|---|---|---|
| ภาพประกอบเชิงศิลป์หรือไอคอนในสไลด์ ที่ไม่ได้สื่อโครงสร้างหรือลำดับ | `b2b-slide-designer` หัวข้อ 4.11 แล้วประกาศ `ICE_DESIGN=briefed` (กติกาเดิม §0.1 ข้อ 8) | คนละงาน: อันนั้นคือการตกแต่งให้สไลด์สวย อันนี้คือการอธิบายว่าสิ่งของเชื่อมกันอย่างไร |
| ภาพถ่าย ภาพวาด หรือภาพเปิดเรื่องที่สร้างด้วยปัญญาประดิษฐ์ | higgsfield (หลัก) หรือ gemini (สำรอง) ตามกฎเสริมข้างบน | เป็นการสร้างภาพ ไม่ใช่การวางผัง |
| Gantt ที่ต้องฝังเป็นวัตถุในไฟล์ `.pptx` ตามแม่แบบที่ผ่านงานจริงแล้ว | `~/.claude/agents/_lib/patterns/gantt-timeline.md` (ดู §4.3) | แม่แบบนั้นผ่านงานจริงและผู้ใช้อนุมัติแล้ว ใช้ `diagram-design` เฉพาะเมื่อต้องการ Gantt เป็นไฟล์เดี่ยวหรือหน้าเว็บ |
| วิเคราะห์ codebase หรือกองเอกสารเพื่อทำแผนที่ความรู้ | skill `graphify` (อยู่ `ice-tools` เหมือนกัน) | `graphify` **วิเคราะห์**ของที่มีอยู่แล้วสร้างกราฟอัตโนมัติ · `diagram-design` **ออกแบบ**ภาพเพื่อสื่อสารสิ่งที่คนตัดสินใจแล้ว |
| แผนภาพแบบ Mermaid ที่ต้องคงเป็นข้อความในเอกสารสำหรับนักพัฒนา | `netsuite-sdf-project-documentation` (มีแม่แบบ Mermaid อยู่แล้ว) | เอกสารนักพัฒนาต้องการ diff ได้ใน git — ต้องคงเป็นข้อความ ไม่ใช่ไฟล์ HTML |
| ข้อมูลที่จัดเป็นรายการหรือตารางเปรียบเทียบได้อยู่แล้ว | ใช้ตารางในเอกสาร | ตัว skill เองก็ห้ามวาด (หัวข้อ "When to Use" ของ skill) — แผนภาพต้องทำให้เข้าใจมากกว่าข้อความ ไม่ใช่แค่ดูแพงขึ้น |

> **จุดที่พลาดบ่อยและวิธีตัดสิน:** ถ้าภาพนั้น**มีของหลายชิ้นที่เชื่อมกันหรือเรียงลำดับกัน** = แผนภาพ ใช้ `diagram-design` · ถ้าเป็น**ภาพเดี่ยวเพื่อความสวยงามหรือสื่ออารมณ์** = ภาพประกอบ ไปเส้นทางเดิม
> **เส้นแบ่งกับแถวสุดท้ายของตาราง ❌ (ข้อมูลที่จัดเป็นตารางได้):** ตารางเหมาะกับ**การเทียบค่าของสิ่งของที่ไม่ได้เชื่อมกัน** เช่น เทียบราคาสามแพ็กเกจ · แผนภาพเหมาะกับ**ความสัมพันธ์หรือลำดับ** เช่น ข้อมูลไหลจากระบบไหนไปไหน ใครส่งต่อให้ใคร — เกณฑ์คือ **ถ้าลบเส้นเชื่อมออกแล้วความหมายหายไป ให้วาดเป็นแผนภาพ ถ้าลบแล้วยังอ่านรู้เรื่อง ให้ใช้ตาราง**
>
> **เมื่อรับไฟล์ `.drawio` หรือ `.mmd` จากลูกค้ามาวาดใหม่ ต้องถามผู้ใช้สามข้อก่อนลงมือ** เพราะไฟล์ต้นทางมักมีของเกินจำเป็นและ skill จะตัดให้ตามงบความซับซ้อน: (1) ต้องคงผังการวางเดิมไว้หรือจัดใหม่ได้ (2) ตัดกล่องที่ไม่จำเป็นออกได้หรือไม่ หรือทุกกล่องมีความหมายทางสัญญา (3) ผู้อ่านปลายทางเป็นใคร (วิศวกร ผสม หรือผู้บริหาร) เพราะระดับรายละเอียดต่างกัน · **การประกาศ `ICE_BASE` ในกรณีนี้ให้ใช้ `ICE_BASE=NEW`** เพราะเครื่องหมายนั้นหมายถึงรุ่นก่อนหน้าของงานที่**ทีมเราสร้างเอง** (ดู §0.2) ไฟล์ที่ลูกค้าส่งมาเป็นวัตถุดิบ ไม่ใช่รุ่นก่อนหน้าของงานเรา — ยกเว้นเคยวาดฉบับของเราไปแล้วและกำลังแก้ฉบับนั้น จึงชี้ `ICE_BASE` ไปที่ไฟล์ของเรารุ่นล่าสุด
> **ผลลัพธ์ที่ได้เป็นไฟล์ HTML** — เมื่อต้องนำไปวางในไฟล์ `.pptx` หรือ `.docx` ให้สั่ง skill แปลงเป็นภาพก่อน (`.png` หรือ `.svg`) แล้วจึงแทรกตามเส้นทางรูปภาพปกติของฟอร์แมตนั้น
> **การแปลงเป็น `.png` ต้องมีเครื่องมือเสริมในเครื่อง** ซึ่งเปลี่ยนได้เองโดยไม่มีใครมาแก้ไฟล์นี้ตาม จึงห้ามเชื่อข้อความนี้แทนการตรวจจริง — ให้ตรวจด้วยคำสั่ง `python3 ~/.claude/skills/diagram-design/scripts/self_check.py <ไฟล์ที่สร้าง>` ซึ่งจะบอกว่าไฟล์ผ่านกฎของ skill หรือไม่ **ถ้าคำสั่งไม่ผ่านหรือหาไฟล์ไม่พบ ให้ส่งมอบเป็นไฟล์ HTML ตามเดิมแล้วแจ้งผู้ใช้ อย่าติดตั้งเครื่องมือเพิ่มเอง**

---

# §6 ⭐ VALIDATION BUDGET (Hard Rule กัน validation loop กิน token — เคสจริง Viriyah 2026.07.14 transcript 1.48MB)

1. **SINGLE-PASS:** validator ครบชุดตาม format/tier รัน **1 ครั้งเดียว** → PASS ทุกข้อ = **จบ ส่งเข้า ⑤ อริส ทันที** — ห้าม re-run/re-render/re-parse "เพื่อความชัวร์"
2. **FAIL → แก้ → re-check เฉพาะข้อที่ fail (delta)** · cap 2 รอบ → ยัง fail = หยุด รายงาน diagnostic ไม่ฝืนวน
3. **SCALE-TO-SIZE:** artifact เล็ก (xlsx ≤~30 แถว · deck ≤5 slides · docx ≤3 หน้า) = ตรวจโครงสร้าง+ค่าพอ ไม่ render ภาพทุกหน้า
   ⚠ **ข้อยกเว้น: .xlsx ที่ส่งลูกค้าต้อง render ทุกขนาด** ตาม §3.2 E2 ชั้น ② เพราะการเฉือนข้อความไม่ขึ้นกับจำนวนแถว
4. **TOKEN DISCIPLINE:** parse/ตรวจด้วย script ที่คืนผลเป็น**ตัวเลข/counts** — ห้าม dump raw XML เข้า context (transcript บวม = ทำผิดข้อนี้)
- **PPTX:** γ1 Strict Validator (§1 D4 ทุก ✓) · **XLSX:** formula-integrity + §3.2 E1-E6 · **DOCX:** §3.1 W1-W5 (ฟอนต์ W1-W3 · ตาราง W4-W5) + academic → citation-verbatim · **HTML:** เปิด browser/screenshot จริง · **PDF:** pdffonts emb=yes (ตาราง §6 ตรวจได้แค่ emb + รายชื่อ fallback ที่รู้จัก — ด่าน "ไม่มีฟอนต์อื่นเกินมา" อยู่ที่ `render_pdf.sh --expect` ดู §7)
- ทุก format: validator report เป็น**ตัวเลขจริง** ("collision 0 · overflow 0 · fonts 4/4 embedded") — ห้ามรายงาน "ผ่านแล้ว" ลอย ๆ

## ⭐ FONT VALIDATORS V1-V4 (หมายเหตุลำดับ: V3 พิมพ์อยู่ต่อจาก V4 ในหัวข้อถัดไป — อ่านให้ครบทั้งสี่ตัว) (V01R03 ใหม่ — บังคับทุก build ที่มีไทย · รันก่อนส่งเข้า ⑤ อริส)

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

> **ใช้ตัวไหน:** ใช้ `audit_fonts.py` เสมอ — มันเป็นประตูเดียวที่ครอบทุกฟอร์แมต และสำหรับ .xlsx มันเรียก `build_xlsx.audit()` ให้เองอยู่แล้ว · `build_xlsx.py --audit` มีไว้สำหรับเรียกจากโค้ดหรือ debug เฉพาะ .xlsx เท่านั้น

```bash
python3 ~/.claude/agents/_lib/audit_fonts.py [--rail private|govt] [--allow-font NAME]... FILE...
```
| ฟอร์แมต | ตรวจอะไร |
|---|---|
| `.xlsx` | delegate `build_xlsx.audit()` → V1/V2/V4 + E2-E5 + T2 word-break |
| `.pptx` | ฟอนต์บน run ที่มีไทยจริง (`a:cs`/`a:latin`) + **D1: run ไทยที่ไม่มี `<a:cs>`** |
| `.docx` | V1/V2/V4 บน `w:cs`/`w:ascii` + **W1: run ไทยไม่มี `w:cs` และ docDefaults ก็ไม่ได้ตั้ง** (inherit = ผ่าน) · **W4: ตารางตั้งแต่ 2 คอลัมน์ขึ้นไปไม่มี `w:tblLayout` เป็น fixed** · **W5: แถวเนื้อหาไม่มี `w:cantSplit`** — W4 กับ W5 เป็นความล้มเหลวทั้งคู่ รายละเอียดที่ §3.1 · ⚠️ **W2 W3 และเกณฑ์ `szCs` ไม่มีด่านอัตโนมัติ ผู้ build ต้องถือเอง** |
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
   ⇒ กติกาใหม่: build script เขียนมือทุกตัวต้อง `from font_policy import RAILS` แล้วอ่านฟอนต์จากราง
      ห้าม hard-code ชื่อฟอนต์ · และต้องรัน `--audit` ก่อนส่งเข้า ⑤ อริส ทุกครั้ง
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
   ⭐ **งานส่งลูกค้าทุกฟอร์แมต (.xlsx/.pptx/.docx) ต้องใส่ `--strict-fonts` เสมอ** เพื่อให้ "ฟอนต์แปลกปน"
     เป็นความล้มเหลว (exit 8) ไม่ใช่แค่คำเตือน — เหตุผลเดียวกันทุกฟอร์แมต คือเครื่องผู้รับที่ไม่มีฟอนต์
     ตัวที่ปนเข้ามาจะแสดงผลต่างออกไป · ถ้ามีฟอนต์ตัวที่สองที่ตั้งใจใช้จริง (เช่นฟอนต์สัญลักษณ์)
     ให้ประกาศไว้ด้วย `--allow "ชื่อฟอนต์"`
   รหัสจบของ helper: 0 = ผ่าน (รวมกรณีเตือนเรื่องฟอนต์ปนแบบไม่ strict) · 2 = เรียกใช้ผิด/ไม่พบไฟล์ ·
     3 = ไม่พบ LibreOffice ตัวจริง · 4 = render ไม่ได้ไฟล์ · 5 = ฟอนต์ไม่ฝัง หรืออ่าน PDF ไม่ได้ ·
     6 = เจอฟอนต์ fallback ของ Linux/LO (renderer ผิดตัว) · 7 = ไม่พบฟอนต์ที่คาดไว้ · 8 = ฟอนต์ปนแบบ strict

① LibreOffice **absolute path** + fresh profile (helper ทำให้แล้ว · ถ้าทำมือ):
   /Applications/LibreOffice.app/Contents/MacOS/soffice --headless \
     -env:UserInstallation=file:///tmp/lo-run --convert-to pdf --outdir . "ไฟล์.pptx"
   (ไม่ใส่ fresh profile = พิมพ์ "convert..." แต่ไม่เขียนไฟล์เงียบ ๆ)
   วิธียืนยันว่าได้ตัวจริง: `--version` ต้องขึ้นต้น "LibreOffice " — shim จะขึ้นอย่างอื่น
② PowerPoint AppleScript save-as-PDF (fidelity สูงสุด): dest ต้องเป็น POSIX file (string เฉย ๆ = "done" แต่ไม่เขียน) ·
   sandbox เขียน /private/tmp ไม่ได้ → 🔴 V01R12: ใช้ staging `~/Documents/.ice-staging/` เท่านั้น
   แล้ว**ย้ายเข้า `<sub-project>/20-Output/_temp/` ทันทีในคำสั่งเดียวกัน** (`osascript … && mv … && rmdir`)
   — ข้อความเดิม "save ใต้ ~/Documents แล้วย้าย" คือต้นตอขยะ `_qa_aris_vfin/` + `qa_s6_*.pptx`
   ที่ user เจอใต้ ~/Documents (2026.08.05): agent ทำครึ่งแรก ลืมครึ่งหลัง → กติกาเต็ม `reference/file-hygiene.md`
③ PowerPoint MCP = เช็ค "เปิดได้/ไม่ขึ้น Repair" เท่านั้น (export_pdf = false success ห้ามใช้ render)
④ ไม่มีทางไหนได้ = NOT-VERIFIABLE-ON-HOST บอกตรง ๆ — ห้ามหลุดไป loop สอบสวน

⭐⭐ POST-RENDER FONT VERIFY (บังคับทุกครั้งที่ render — ด่านที่จับ renderer regression ทุกชนิด):
   pdffonts OUT.pdf → ✓ ทุกแถว emb=yes  ✓ **เจอฟอนต์ที่เราตั้งจริง**  ✓ ⭐ **ไม่มีฟอนต์ตัวอื่นเกินมา**
   🔴 เจอ LinuxLibertine / FrankRuhl / DejaVu / Liberation = สัญญาณว่า renderer มองไม่เห็นฟอนต์ระบบ
      → หยุด ตรวจ `render_pdf.sh --which` ก่อนสรุปว่าไฟล์พัง
   🔴 ⭐ V01R19 — เจอฟอนต์ที่**ไม่ได้อยู่ในรายการที่คาดไว้**
      **ลำดับเหตุการณ์ (อ่านให้ตรงกัน):** ก่อนหน้านี้ helper ตรวจแค่ "ฟอนต์ที่คาดไว้มีไหม" เคสด้านล่างจึงลอดผ่าน
      → ตั้งแต่ `render_pdf.sh` **V01R02** helper ตรวจ "มีฟอนต์อื่นเกินมาไหม" ให้ด้วยทันทีที่ระบุ `--expect`
      พฤติกรรมปัจจุบัน: `--expect` เดี่ยว ๆ = **รายงานเป็นคำเตือนแต่ยัง exit 0** · เติม `--strict-fonts`
      จึงกลายเป็นความล้มเหลว exit 8 · ไม่ระบุ `--expect` เลย = ไม่ได้ตรวจข้อนี้ (helper จะพิมพ์บอกว่าข้าม)
      การเทียบชื่อ: จับแบบ **ข้อความบางส่วน ไม่แยกตัวพิมพ์ใหญ่เล็ก และรับค่าเดียว** — ใส่ชื่อตระกูลก็พอ
      น้ำหนักทุกตัวของตระกูลนั้น (Regular/Bold/…) ผ่านด้วยกันเพราะใช้ชื่อตระกูลร่วมกัน
      เคสที่ทำให้เกิดกฎข้อนี้:
      แปลว่ามีอักขระบางตัวที่ฟอนต์รางไม่มี glyph → ระบบหยิบฟอนต์อื่นมาแทนเงียบ ๆ
      เครื่องที่ไม่มีฟอนต์ตัวนั้นจะแสดงผลต่างออกไป — **ฟอนต์ที่เกินมาอันตรายพอกับฟอนต์ที่ขาดไป**
      เคสจริง CP Axtra 2026.08.30: อักขระ ★ (U+2605) 3 จุด ลาก HiraginoSans-W3 เข้า PDF ขณะที่
      `audit_fonts` รายงาน fonts=1 PASS และ `--expect` ก็ผ่าน เพราะทั้งคู่ตรวจแค่ "ฟอนต์ที่คาดไว้มีไหม"
      → ทางแก้ ขั้นที่ 1 หาอักขระต้นเหตุ (อย่าเดา) — คำสั่งนี้ไล่ทุกข้อความในไฟล์แล้วพิมพ์อักขระที่อยู่นอก
        ช่วงไทย/ละติน/เครื่องหมายพื้นฐาน ซึ่งเป็นกลุ่มที่ฟอนต์รางมักไม่มี glyph:
        `python3 -c "import sys,re;from openpyxl import load_workbook as L;w=L(sys.argv[1]);print(sorted({c for s in w for r in s.iter_rows() for x in r if isinstance(x.value,str) for c in x.value if not re.match(r'[\u0E00-\u0E7F\u0020-\u007E\u00A0-\u00FF]',c)}))" FILE.xlsx`
        ⚠ คำสั่งนี้คืน "รายชื่อผู้ต้องสงสัย" ไม่ใช่คำตัดสิน — อักขระอย่าง — → ≥ ฟอนต์รางมี glyph อยู่แล้ว
          ให้เทียบกับชื่อฟอนต์ที่ `pdffonts` รายงานว่าเกินมา แล้วไล่ทีละตัวว่าตัวไหนเป็นต้นเหตุจริง
        ขั้นที่ 2 เปลี่ยนเป็นตัวที่ฟอนต์รางมี หรือใช้คำแทน (เครือญาติของ CHAR-GUARD §1 D4 ที่ทำกับ → U+2192)
        อักขระที่เคยทำพังจริงในทีมนี้: **★ U+2605** (ลาก HiraginoSans) และ **→ U+2192** (PowerPoint ปฏิเสธไฟล์)
        ถ้าตั้งใจใช้ ให้ประกาศด้วย `--allow "ชื่อฟอนต์"` — ห้ามปล่อยผ่านเงียบ ๆ
   หลักการ: **ผลตรวจที่ได้จาก renderer ผิดตัว = หลักฐานปลอม** — เช็ค renderer ก่อนโทษไฟล์เสมอ

แล้ว pdftoppm -r 100..130 เป็น PNG รายหน้า · กฎเหล็ก: ls ยืนยันไฟล์เกิดจริงทุกขั้น
```

---

# §8 ⭐ CODEX/OPENROUTER OPTION (คงตามคำสั่ง user — advisor/QA/idea ทางเลือก)

- ผู้ build (L0/persona ใด ๆ) ใช้ Codex/OpenRouter เป็น**ที่ปรึกษาทางเลือก**ได้ตาม codex_scope ที่ user เปิด: review โค้ด build ก่อนรันงานใหญ่ · ภาษาใน artifact ก่อนส่ง ⑤ อริส · ไอเดีย design
- **กติกาเหล็ก: ผู้ตรวจภายนอกว่าผ่าน ≠ ข้าม Strict Validator/γ1 — ของตัวเองรันเสมอ (เสริม ไม่แทน)** · QA จริงยังเป็นอริส
- L0 เรียกเองใน loop หลัก = เสถียร (แก้ pattern เดิม "subagent หลุดตอนกำลังเรียก advisor") · **เจนนี่-shell ตั้ง `codex_scope: none` เสมอ** (บทเรียน Viriyah team-memory)
- Contract = skill `claude-codex-bridge` / `openrouter-bridge` (ONE-HOME)

---

*Skill: ice-doc-builder **V01R20** | 2026.08.31 | สกัดจาก deliverable-gen-agent V02R08 (§4→§1-2·4 · §5→§5 · E4→§0.3+§6) คำต่อคำ + ใหม่: §3 FONT ข้ามฟอร์แมต docx/xlsx/pdf + §0 CONTRACT ICE_BUILD=pipeline + §7 Renderer Ladder + §8 Codex Option*
*ใช้โดย: L0 (กัปตัน/คิม/สมนึก personas) · deliverable-gen-agent shell · QA โดยอริสบังคับทุกกรณี (Producer≠Checker)*
