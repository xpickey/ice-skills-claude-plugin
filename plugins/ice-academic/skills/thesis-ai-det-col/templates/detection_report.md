═══════════════════════════════════════════════════════
🔍 AI DETECTION SELF-CHECK REPORT (V03 — 15 จุดตรวจ)
═══════════════════════════════════════════════════════
วันที่ตรวจ:        [YYYY-MM-DD HH:MM]
ข้อความที่ตรวจ:    [ชื่อ/Section]
จำนวนคำ:           [X] คำ
ผู้ตรวจ:           [ชื่อ]
ภาษา:              [Thai / English / Bilingual]
บริบท:             [Academic / Business / Government / Marketing]
Voice Profile ID:  [VP-...]
เกณฑ์เป้าหมาย:    AI Score < [X]%

Files Loaded (ตาม Manifest SKILL.md §3.5):
  [ ] 01_three_layer_detection.md
  [ ] 05_thai_academic_patterns.md
  [ ] 06_verified_ai_signatures.md
  [ ] 07_wikipedia_24_patterns.md (เมื่อ EN/Bilingual)
  อื่น ๆ: [...]
⚠️ รายงานที่ Files Loaded ไม่ครบตาม Manifest = ไม่สมบูรณ์

Scan Coverage:     [X] / [Y] ย่อหน้า = [XXX]%  (ต้อง 100% จึง output ได้)

─────────────────────────────────────────────────────
LAYER 1: AI VOCABULARY FOOTPRINTS (2 Checks)
─────────────────────────────────────────────────────
Check 1a: Density (Class B — 06 §2 + §4)
  Tier 1 Words ที่พบ:
  - "[คำ]" ปรากฏ X ครั้ง → "[คำใหม่]"
  - "[คำ]" ปรากฏ X ครั้ง → "[คำใหม่]"
  Total Class B Words:       [X]
  Density (per 1,000 words): [X.X]
  สถานะ:                    ☐ ผ่าน  ☐ ไม่ผ่าน

Check 1b: Zero-Tolerance Scan (Class A — 06 §1 + §1.5 + §1.6) ⚠ HARD GATE
  Hits ที่พบ (พบ ≥ 1 = Fail ทั้งฉบับ):
  - "[คำ]" ที่ [ย่อหน้า P_/ประโยคที่ _] → "[วิธีแก้]"
  Total Class A Hits:        [X]  (ต้อง = 0)
  สถานะ:                    ☐ ผ่าน (0 hits)  ☐ FAIL — หยุดและแก้ทันที

─────────────────────────────────────────────────────
LAYER 2: STATISTICAL & SENTENCE PATTERNS (7 Checks)
─────────────────────────────────────────────────────
Check 1: Burstiness
  - SD ความยาวประโยค:       [X.X]
  - มีประโยคสั้น (5–12 คำ):  ☐ มี ☐ ไม่มี
  - มีประโยคยาว (25–35+):    ☐ มี ☐ ไม่มี
  สถานะ:                    ☐ ผ่าน  ☐ ไม่ผ่าน

Check 2: Sentence Opening Variability
  - จำนวนรูปแบบเปิดประโยคใน 10 ประโยค: [X]
  สถานะ:                    ☐ ผ่าน  ☐ ไม่ผ่าน

Check 3: Paragraph Symmetry
  - ความยาวย่อหน้ามีกี่ขนาด: [X]
  สถานะ:                    ☐ ผ่าน  ☐ ไม่ผ่าน

Check 4: Transition Phrase Density
  - คำเชื่อมต่อ 500 คำ:     [X]
  สถานะ:                    ☐ ผ่าน  ☐ ไม่ผ่าน

Check 5: Bullet-Point Thinking in Prose
  - มีรายการใน prose form:   ☐ มี ☐ ไม่มี
  สถานะ:                    ☐ ผ่าน  ☐ ไม่ผ่าน

Check 6: Template Proximity (sliding window 5 ประโยค) ⭐ V03
  - โครงเปิดซ้ำในหน้าต่าง/ย่อหน้าเดียวกัน:
    - "[โครง]" ที่ [P_/ประโยค _ และ _]
  - Template เต็มรูปซ้ำเกิน 1 ครั้ง/หัวข้อ: ☐ มี ☐ ไม่มี
  - รูปแบบเปิดชนิดเดียวกัน > 2 ครั้ง/10 ประโยค: ☐ มี ☐ ไม่มี
  สถานะ:                    ☐ ผ่าน  ☐ ไม่ผ่าน

Check 7: Nested Clause Depth (ซึ่ง/ที่/อัน ≤ 2 ชั้น) ⭐ V03
  - ประโยคที่ซ้อนเกิน 2 ชั้น: [X] ประโยค
    - [P_/ประโยค _]: "[ข้อความย่อ]"
  สถานะ:                    ☐ ผ่าน  ☐ ไม่ผ่าน

─────────────────────────────────────────────────────
LAYER 3: STRUCTURAL & DISCOURSE PATTERNS (6 Checks)
─────────────────────────────────────────────────────
Check 8: Paragraph Length Variability
  - มี short / medium / long paragraphs: ☐ ครบ ☐ ไม่ครบ
  สถานะ:                    ☐ ผ่าน  ☐ ไม่ผ่าน

Check 9: Citation Distribution
  - มี citation cluster ≥4: ☐ มี ☐ ไม่มี
  สถานะ:                    ☐ ผ่าน  ☐ ไม่ผ่าน

Check 10: Personal Voice Markers
  - จำนวน markers ที่พบ:    [X]
  - เกณฑ์ที่ต้องการ:        [Y]
  สถานะ:                    ☐ ผ่าน  ☐ ไม่ผ่าน

Check 11: Section-Closing Ritual Uniformity ⭐ V03
  - ประโยคปิดของแต่ละหัวข้อ:
    - [หัวข้อ 1]: "[สูตรปิด]"
    - [หัวข้อ 2]: "[สูตรปิด]"
  - Forward signpost ทั้งเอกสาร: [X] ครั้ง (เกณฑ์ ≤ 1)
  - หัวข้อติดกันปิดสูตรเดียวกัน: ☐ มี ☐ ไม่มี
  - จำนวนแบบการปิดทั้งเอกสาร: [X] แบบ (เกณฑ์ ≥ 3)
  สถานะ:                    ☐ ผ่าน  ☐ ไม่ผ่าน
  ⚠ ห้ามใช้ดุลยพินิจแบบ density — วัดที่ความสม่ำเสมอของพิธีกรรม

Check 12: Acronym Re-Expansion ⭐ V03
  - คู่ "ชื่อเต็ม (ย่อ)" ที่พบ: [รายการ]
  - การ re-expand หลังนิยามครั้งแรก: [X] ครั้ง ที่ [ตำแหน่ง]
    (ข้อยกเว้น: ดุษฎีนิพนธ์ 5 บท re-define ต้นบทได้)
  สถานะ:                    ☐ ผ่าน  ☐ ไม่ผ่าน

Check 13: Reporting Verb–Evidence Alignment ⭐ V03
  - จุดอ้างอิงทั้งหมด: [X] จุด
  - กริยาไม่ตรงชนิดแหล่ง (05 §10): [X] จุด
    - [ตำแหน่ง]: "[กริยาที่ใช้]" กับแหล่งชนิด [ทัศนะ/เชิงประจักษ์] → "[กริยาที่ถูก]"
  สถานะ:                    ☐ ผ่าน  ☐ ไม่ผ่าน

═══════════════════════════════════════════════════════
📊 OVERALL AI DETECTION SCORE
═══════════════════════════════════════════════════════
Layer 1 (Vocabulary):  [X]/2  — Check 1b: ☐ ผ่าน ☐ FAIL (hard gate)
Layer 2 (Statistical): [X]/7
Layer 3 (Structural):  [X]/6

รวม:                   [X]/15  (เกณฑ์ผ่าน ≥ 13/15 และ 1b ต้องผ่าน)
คะแนน AI ประมาณการณ์: [XX]%
เกณฑ์ผ่าน:             < [X]%
สถานะรวม:             ☐ ผ่าน  ☐ ต้องแก้ไข
                       (1b Fail = Fail ทั้งฉบับ ไม่ว่าคะแนนรวมเท่าใด)

→ ถ้าไม่ผ่าน: ดำเนินการ Mode 3 (Two-Pass Correction รวม Step 2.5–2.6)
→ ถ้าผ่าน: ดำเนินการ Voice Match Scoring (Mode 4)
═══════════════════════════════════════════════════════
