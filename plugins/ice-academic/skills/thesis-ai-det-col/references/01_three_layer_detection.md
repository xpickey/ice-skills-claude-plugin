# Three-Layer Detection Methodology

## When to Read This

อ่านไฟล์นี้เมื่อทำ Mode 1 (DETECT) หรือ Mode 4 (FULL CYCLE) ขั้นตอนแรก — ต้องการรายละเอียดของ 3 Layers และ 15 จุดตรวจ เพื่อรัน self-check ครบถ้วน

**Version: V03R01 (2026.06.07)** — เพิ่ม Check 1b Zero-Tolerance, Check 6 Template Proximity, Check 7 Nested Clause Depth, Check 11 Section-Closing Ritual, Check 12 Acronym Re-Expansion, Check 13 Reporting Verb Alignment และ Scan Discipline Protocol (ยกระดับจากบทเรียนจุดหลุดจริง)

---

## 1. Overview

ระบบตรวจจับ AI ในปี 2569 (Turnitin, GPTZero, Originality.ai, Copyleaks) ทำงานบนสามมิติร่วมกัน — Statistical, Linguistic, Structural — เราสะท้อนเป็น 3 Layers:

| Layer | What it Checks | Number of Checks |
|---|---|---|
| Layer 1 | AI Vocabulary Footprints | 2 (1a Density + 1b Zero-Tolerance) |
| Layer 2 | Statistical & Sentence Patterns | 7 |
| Layer 3 | Structural & Discourse Patterns | 6 |

**รวม 15 จุดตรวจ** — เกณฑ์ผ่าน: ≥ 13/15 **และ** Check 1b (Zero-Tolerance) ต้องผ่านเสมอ — 1b ไม่ผ่าน = Fail ทั้งฉบับทันที ไม่ว่าคะแนนรวมเป็นเท่าใด

---

## 1.5 Scan Discipline Protocol (บังคับก่อนรันทุก Layer) ⭐ V03

บทเรียนจากจุดหลุดจริง: pattern ซ้ำสองครั้งติดในย่อหน้าเดียวรอดการตรวจ เพราะผู้ตรวจนับความถี่รวมทั้งฉบับแล้วสรุปว่า density ต่ำ — **ความถี่รวมต่ำไม่ได้แปลว่าปลอดภัย**

1. **แตกเอกสารเป็นย่อหน้า** ใส่หมายเลขกำกับ [P1]…[Pn] ก่อนเริ่มตรวจ
2. **ไล่ตรวจทีละย่อหน้า ทุกย่อหน้า ทุกบรรทัด** — ห้ามสุ่มตรวจ ห้ามอ่านข้าม ห้ามตัดสินจากภาพรวม
3. **Check เชิงระยะใกล้ (Check 6, 11) ใช้ sliding window** — เลื่อนทีละประโยค ดูหน้าต่าง 5 ประโยค ไม่ใช่นับความถี่รวมแล้วหารเฉลี่ย
4. **คำ Class A (Check 1b): บันทึกตำแหน่งทุก hit** (ย่อหน้า/ประโยค) — 1 hit = Fail
5. **จบเอกสารทำ document-level sweep อีกหนึ่งรอบ** — Check 11 (Closing Ritual), Check 12 (Acronym), Check 9 (Citation), Check 13 (Reporting Verbs — ไล่ทุกจุดอ้างอิงเทียบชนิดแหล่ง) ต้องมองข้ามหัวข้อ จึงตรวจได้เฉพาะการ sweep ทั้งฉบับ
6. **รายงาน Scan Coverage** = จำนวนย่อหน้าที่ตรวจ / ย่อหน้าทั้งหมด — ต้องเท่ากับ 100% มิฉะนั้นรายงานถือว่าไม่สมบูรณ์ ห้าม output

---

## 2. LAYER 1 — AI Vocabulary Footprints Check (2 Checks)

### 2.1 Methodology

เปรียบเทียบ vocabulary ในข้อความกับ **Verified AI Signature List** (`06_verified_ai_signatures.md`) โดยแยกเป็น 2 จุดตรวจที่วัดคนละแบบ:

| จุดตรวจ | รายการอ้างอิง | วิธีวัด |
|---|---|---|
| **Check 1a — Density (Class B)** | 06 Section 2 (🟡 Moderate) + Section 4 (English Tier 1) | ความหนาแน่นต่อ 1,000 คำ ตามตาราง 2.2 |
| **Check 1b — Zero-Tolerance (Class A)** ⭐ V03 | 06 Section 1 (Confirmed) + 1.5 (Field-Discovered) + 1.6 (Promotional/Artifacts) | per-instance: พบ ≥ 1 ครั้ง = Fail ทันที (HARD GATE) |

**Check 1b ห้ามใช้เกณฑ์ density เด็ดขาด** — บทเรียนจากจุดหลุดจริง: "อย่างก้าวกระโดด" ปรากฏครั้งเดียวจึงผ่านเกณฑ์ density แต่คำเร่งน้ำหนักเชิงโปรโมตครั้งเดียวก็ส่งกลิ่น — ทุก hit ต้องบันทึกตำแหน่ง (ย่อหน้า/ประโยค)

### 2.2 Check 1a Pass Criteria (Class B — Density)

| ระดับเอกสาร | จำนวน Tier 1 ที่ยอมรับ |
|---|---|
| งานวิชาการระดับวารสารนานาชาติ | ≤ 2 ครั้ง / 1,000 คำ |
| งานวิชาการระดับวารสารไทย (TCI) | ≤ 4 ครั้ง / 1,000 คำ |
| Business proposal / Executive | ≤ 3 ครั้ง / 1,000 คำ |
| งานราชการ | ≤ 2 ครั้ง / 1,000 คำ |
| Marketing content | ≤ 5 ครั้ง / 1,000 คำ |

### 2.3 ⚠️ สำคัญ — สำหรับภาษาไทย

**คำที่เคยจัดเป็น Tier 1 ใน English context แต่ใช้ได้ในภาษาไทย:**
- "ขับเคลื่อน" (272 ครั้งใน corpus 62 ไฟล์) — ✅ ใช้ได้
- "ยกระดับ" (133/43) — ✅ ใช้ได้
- "อย่างยั่งยืน" (68/32) — ✅ ใช้ได้
- "อย่างมีประสิทธิภาพ" (195/55) — ✅ ใช้ได้
- "บูรณาการ" (432/59) — ✅ ใช้แพร่หลาย

**คำที่เป็น AI signature จริงในภาษาไทย** (ปรากฏ ≤ 5 ครั้ง / 292K):
- "เป็นที่ทราบกันดีว่า" (0)
- "นับเป็นสิ่งสำคัญ" (0)
- "ในแง่หนึ่ง" (0)
- "อาจถือได้ว่า" (0)
- "อย่างพิถีพิถัน" (0)
- "ยิ่งไปกว่านั้น" (1)
- "ปฏิเสธไม่ได้ว่า" (3)

ดูรายการเต็มใน `06_verified_ai_signatures.md`

---

## 3. LAYER 2 — Statistical & Sentence Pattern Check (7 Checks)

### Check 1: Burstiness — Sentence Length Variability

**วิธีตรวจ:**
1. นับจำนวนคำของแต่ละประโยค
2. ตรวจ 5 ประโยคติดต่อกัน — หากมีมากกว่า 3 ประโยคยาว 16-22 คำ → **เสี่ยงสูง**
3. คำนวณ Standard Deviation (SD)

**เกณฑ์ผ่าน:**
- SD ≥ 5
- มีประโยคสั้น (5-12 คำ) ≥ 1 ต่อย่อหน้า
- มีประโยคยาว (25-35+ คำ) ≥ 1 ต่อย่อหน้า

### Check 2: Sentence Opening Variability

**❌ AI Pattern:** ทุกประโยคเริ่มด้วยประธาน + กริยา

**✅ Human Pattern:** สลับ 5 รูปแบบ:
- Adverb: "ในปี 2567 องค์กร..."
- Subordinate Clause: "เมื่อพิจารณาจาก..."
- Question: "อะไรเป็นปัจจัยสำคัญ?"
- Quote: "นักวิชาการชี้ว่า '...'"
- Prepositional: "ภายใต้กฎหมายฉบับใหม่..."

**เกณฑ์ผ่าน:** ใน 10 ประโยคติดต่อกัน อย่างน้อย 3 ประโยคต้องไม่ใช่ประธาน-กริยา

### Check 3: Paragraph Symmetry

**เกณฑ์ผ่าน:** ในเอกสาร 1,500 คำ มีย่อหน้าอย่างน้อย 3 ขนาด (สั้น/กลาง/ยาว)

### Check 4: Transition Phrase Density

**เกณฑ์ผ่าน:** ≤ 3 คำเชื่อม (นอกจากนี้/อีกทั้ง/Furthermore/Moreover) ต่อ 500 คำ

### Check 5: Bullet-Point Thinking in Prose

**❌ AI Pattern:** "มี 3 ประการ ได้แก่... ปัจจัยที่หนึ่ง... ปัจจัยที่สอง..."

**✅ Human Pattern:** เขียนเป็นความเรียงต่อเนื่อง

### Check 6: Template Proximity — โครงประโยคซ้ำในระยะใกล้ ⭐ V03

**วิธีตรวจ (sliding window — ห้ามนับความถี่รวมทั้งฉบับ):**
1. สกัด "โครงเปิด" ของทุกประโยค (โครงสร้าง 3-4 คำแรก เช่น "เมื่อพิจารณา…ผ่าน…จะพบว่า")
2. เลื่อนหน้าต่าง 5 ประโยคทีละประโยค เทียบโครงภายในหน้าต่าง

**เกณฑ์ผ่าน:**
- โครงเปิดเดียวกันไม่ซ้ำภายใน 5 ประโยคติดกัน และไม่ซ้ำภายในย่อหน้าเดียวกัน
- โครงประโยคเต็มรูป (template) เดียวกันใช้ ≤ 1 ครั้งต่อหัวข้อ
- รูปแบบเปิดทั้ง 5 ชนิด (Adverb/Subordinate/Question/Quote/Prepositional): ชนิดละ ≤ 2 ครั้งต่อ 10 ประโยคติดกัน

**⚠️ กับดักที่เกิดจริง:** การแก้ Check 2 ด้วยการเติม Subordinate opener ถี่ ๆ ทำให้ "เมื่อพิจารณา…ผ่านกรอบ…จะพบว่า" โผล่สองครั้งติดในย่อหน้าเดียว — Check 2 ผ่าน (เพราะไม่ใช่ประธาน-กริยา) แต่ Check 6 ต้องจับ เพราะ detector และ reviewer มองเห็นการซ้ำระยะใกล้ ไม่ได้มองความถี่รวม

### Check 7: Nested Clause Depth — อนุประโยคซ้อน ⭐ V03

**วิธีตรวจ:** ทุกประโยค นับชั้นการซ้อนของ "ซึ่ง / ที่ / อัน / โดยที่" (translationese — ตัวอย่างการแก้ใน `05_thai_academic_patterns.md` §1.3)

**เกณฑ์ผ่าน:** ≤ 2 ชั้นต่อประโยค — ประโยคที่ซ้อนเกิน ("ซึ่ง…ที่…ใน…") ให้แตกเป็น 2 ประโยคหรือยุบอนุประโยค

---

## 4. LAYER 3 — Structural & Discourse Pattern Check (6 Checks)

### Check 8: Paragraph Length Variability

**เกณฑ์ผ่าน:** ความยาวย่อหน้าในช่วง 3-12 ประโยค โดย:
- ย่อหน้าสั้น (2-3 ประโยค) ≥ 20%
- ย่อหน้ายาว (7+ ประโยค) ≥ 20%

### Check 9: Citation Distribution

**❌ AI Pattern:** Cluster citations ที่จุดเดียวกัน "(Smith, 2020; Jones, 2021; Brown, 2022; Lee, 2023; Wang, 2024)"

**เกณฑ์ผ่าน:** ไม่มี citation cluster ที่มี ≥ 4 citations ติดกัน — ยกเว้นใน literature review

### Check 10: Personal Voice Markers

**Markers ที่บ่งชี้เสียงผู้เขียน:**
- ชื่อเฉพาะ (บริษัท บุคคล สถาบัน)
- ตัวเลขเฉพาะ (31.7% ไม่ใช่ "30%")
- วันที่เฉพาะ (ไตรมาส 2 ปี 2567)
- เรื่องเล่า/ประสบการณ์
- ข้อสังเกตเชิงบริบท
- Counterargument
- Legal/Regulatory anchors (มาตรา/ระเบียบ)

**เกณฑ์ผ่าน:**
- เอกสาร < 1,000 คำ: ≥ 5 markers
- 1,000-3,000 คำ: ≥ 12 markers
- > 3,000 คำ: ≥ 1 marker ต่อ 200 คำ

### Check 11: Section-Closing Ritual Uniformity ⭐ V03

**วิธีตรวจ (document-level sweep):** เก็บประโยคปิดของทุกหัวข้อมาเรียงเทียบกัน

**เกณฑ์ผ่าน:**
- Forward signpost ("…ในหัวข้อถัดไป" / "ดังจะได้กล่าวต่อไป") ≤ 1 ครั้งต่อเอกสาร
- ไม่มีสองหัวข้อติดกันที่ปิดด้วยสูตรเดียวกัน
- การปิดหัวข้อทั้งเอกสารมีอย่างน้อย 3 แบบ (ทางเลือกการปิดดู `05_thai_academic_patterns.md` §9)

**หลักคิด:** สัญญาณ AI อยู่ที่ "ทุกหัวข้อปิดด้วยพิธีกรรมเดียวกัน" ไม่ใช่จำนวนครั้ง — signpost 3 ครั้งจาก 3 หัวข้อ = Fail แม้ density จะดูรับได้ **ห้ามใช้ดุลยพินิจแบบ density กับ check นี้** (บทเรียนจริง: เคยตัดสินใจคงไว้ 2 จุดเพราะคิดว่า density รับได้ — ผลคือหลุด)

### Check 12: Acronym Re-Expansion ⭐ V03

**วิธีตรวจ (document-level sweep):** หาทุกคู่ "ชื่อเต็ม (ตัวย่อ)" เช่น "กรอบคน-กระบวนการ-เทคโนโลยี (PPT)" แล้วนับการปรากฏซ้ำของชื่อเต็ม+วงเล็บเดิมหลังการนิยามครั้งแรก

**เกณฑ์ผ่าน:** นิยามเต็มรูปครั้งแรกครั้งเดียว — การเอ่ยครั้งถัดไปใช้ตัวย่อล้วน ("กรอบ PPT")
**ข้อยกเว้น:** ดุษฎีนิพนธ์โครงสร้าง 5 บท อนุญาต re-define ครั้งแรกของแต่ละบท

**นิสัย LLM:** นิยามอักษรย่อเต็มยศใหม่ทุกครั้งที่เอ่ยถึง — คนเขียนจริงนิยามครั้งเดียวแล้วใช้ตัวย่อตลอด (รายละเอียด `05_thai_academic_patterns.md` §8)

### Check 13: Reporting Verb–Evidence Alignment ⭐ V03

**วิธีตรวจ (document-level sweep):** ไล่ทุกจุดอ้างอิง/การรายงานแหล่ง ระบุชนิดแหล่ง (ทัศนะ / เชิงประจักษ์ / หลายแหล่งสอบทาน) แล้วเทียบกริยารายงานกับตาราง `05_thai_academic_patterns.md` §10

**เกณฑ์ผ่าน:**
- งานทัศนะ/บทความวิชาการ ไม่ใช้ "ยืนยันว่า / พิสูจน์ว่า / พบว่า" (ใช้ เสนอว่า, ชี้ว่า, มองว่า, วิเคราะห์ว่า)
- งานเชิงประจักษ์ ไม่ใช้ "พิสูจน์ว่า" เว้นแต่มีการทดสอบสมมติฐานจริง (ใช้ พบว่า, รายงานว่า, แสดงให้เห็นว่า)
- "ยืนยันในทิศทางเดียวกันว่า" สงวนไว้สำหรับหลายแหล่งที่ให้ผลตรงกัน

**นิสัย LLM:** ใช้ "พบว่า" เหมารวมทุกแหล่ง — กริยาแรงเกินหลักฐาน = overclaim ที่ reviewer จับและเข้าข่าย fabrication ระดับ claim

---

## 5. Detection Report Template

ใช้ template ใน `../templates/detection_report.md` เมื่อ output ผลตรวจ

---

## 6. Score Interpretation

**การนับสถานะรวม:** ผ่าน X/15 จุดตรวจ — เกณฑ์ผ่าน ≥ 13/15 **และ** Check 1b ต้องผ่าน (1b Fail = Fail ทั้งฉบับ ไม่ว่าคะแนนอื่นเป็นเท่าใด)

| AI Score | Action |
|---|---|
| 0-20% | Pass — ส่งงานได้ |
| 21-40% | Light revision (Pass 1 อย่างเดียวก็พอ) |
| 41-60% | Substantial rewrite (Pass 1 + Pass 2) |
| 61-80% | Section-by-section humanization (Two-Pass + Advanced) |
| 81-100% | Full rewrite |
