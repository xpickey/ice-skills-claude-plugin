# Three-Layer Detection Methodology — Core Engine (🟦 CORE) + 3 Academic Checks (🟩)

**V04R01** · 2026.06.13 · 🟦 CORE engine (register-agnostic) + 🟩 Academic checks · Shared Core + 3 Branches (🟩 Academic / 🟧 Business / 🟪 General เท่าเทียม) · *[จัดทำใน SKILL V06 architecture pass]*

## When to Read This

อ่านไฟล์นี้เมื่อทำขั้นตอน DETECT หรือ FULL CYCLE (ขั้นตอนแรก) ของ register ใดก็ตาม — ต้องการรายละเอียดของ 3 Layers และ 15 จุดตรวจ เพื่อรัน self-check ครบถ้วน

🟦 **CORE — กลไกตรวจจับ register-agnostic.** 12 จาก 15 จุดตรวจเป็น **universal engine** ที่ใช้ได้กับทุก register — 🟩 Academic / 🟧 Business / 🟪 General เรียกกลไกเดียวกัน ต่างกันแค่ "ตารางคำ/ความหนาแน่น/baseline" ที่แต่ละ branch หยิบมาเสียบ (ดู Check 1a/1b). ไม่มี academic default ฝังในกลไก — มีเพียง **3 จุดตรวจที่ผูกกับ register วิชาการโดยเฉพาะ** (Check 9 / Check 12 / Check 13) ติด marker 🟩 ชัดเจน branch อื่นข้ามได้

**Version history:** V03R01 (2026.06.07) เพิ่ม Check 1b/6/7/11/12/13 + Scan Discipline. V04R01 (2026.06.13) RE-LABEL core vs academic ตามสถาปัตยกรรม Shared Core + 3 Branches — เนื้อหากลไก/เกณฑ์/บทเรียนคงเดิม verbatim

---

## 1. Overview

ระบบตรวจจับ AI ในปี 2569 (Turnitin, GPTZero, Originality.ai, Copyleaks) ทำงานบนสามมิติร่วมกัน — Statistical, Linguistic, Structural — เราสะท้อนเป็น 3 Layers:

| Layer | What it Checks | Number of Checks | ชนิด |
|---|---|---|---|
| Layer 1 | AI Vocabulary Footprints | 2 (1a Density + 1b Zero-Tolerance) | 🟦 CORE engine (content ป้อนต่อ branch) |
| Layer 2 | Statistical & Sentence Patterns | 7 (Check 1–7) | 🟦 CORE (universal ทั้งหมด) |
| Layer 3 | Structural & Discourse Patterns | 6 (Check 8–13) | 🟦 CORE ×3 (8/10/11) + 🟩 Academic ×3 (9/12/13) |

**รวม 15 จุดตรวจ** — เกณฑ์ผ่าน: ≥ 13/15 **และ** Check 1b (Zero-Tolerance) ต้องผ่านเสมอ — 1b ไม่ผ่าน = Fail ทั้งฉบับทันที ไม่ว่าคะแนนรวมเป็นเท่าใด

### 1.1 🟦 CORE vs 🟩 Academic — Check Inventory (RE-LABEL)

| ชนิด | จำนวน | จุดตรวจ |
|---|---|---|
| 🟦 **CORE (universal engine)** | **12** | Check 1a Density · Check 1b Zero-Tolerance · Check 1 Burstiness · Check 2 Opening Variability · Check 3 Paragraph Symmetry · Check 4 Transition Density · Check 5 Bullet-Point Thinking · Check 6 Template Proximity · Check 7 Nested Clause Depth · Check 8 Paragraph Length · Check 10 Personal Voice · Check 11 Section-Closing Ritual |
| 🟩 **Academic (register-specific)** | **3** | Check 9 Citation Distribution · Check 12 Acronym Re-Expansion (5-บท exception) · Check 13 Reporting-Verb Alignment |

> **กฎ branch:** branch 🟧 Business / 🟪 General รัน 12 CORE checks เสมอ; 3 academic checks (9/12/13) **ข้ามได้** เว้นแต่งานนั้นมีการอ้างอิงวิชาการ. การข้าม 3 academic checks → เกณฑ์ผ่านปรับเป็น ≥ 11/12 (Check 1b ยังเป็น hard-gate). branch 🟩 Academic รันครบ 15.
>
> **Check 1a/1b เป็น CORE engine แต่ content ป้อนต่อ branch:** กลไกวัด (per-instance Zero-Tolerance / density) อยู่ที่ `06_verified_ai_signatures.md` §0 (register-agnostic). word-list ที่ป้อนเข้ากลไก: 🟩 = Thai-count (`06` §1–3) · 🟧 = `11_business_ai_patterns.md` (TB/EB cadence + watchlist) · 🟪 = watchlist สากล. **กลไกเดียว เนื้อหาต่างกันตาม branch.**

---

## 1.5 Scan Discipline Protocol (🟦 CORE — บังคับก่อนรันทุก Layer) ⭐ V03

บทเรียนจากจุดหลุดจริง: pattern ซ้ำสองครั้งติดในย่อหน้าเดียวรอดการตรวจ เพราะผู้ตรวจนับความถี่รวมทั้งฉบับแล้วสรุปว่า density ต่ำ — **ความถี่รวมต่ำไม่ได้แปลว่าปลอดภัย**

1. **แตกเอกสารเป็นย่อหน้า** ใส่หมายเลขกำกับ [P1]…[Pn] ก่อนเริ่มตรวจ
2. **ไล่ตรวจทีละย่อหน้า ทุกย่อหน้า ทุกบรรทัด** — ห้ามสุ่มตรวจ ห้ามอ่านข้าม ห้ามตัดสินจากภาพรวม
3. **Check เชิงระยะใกล้ (Check 6, 11) ใช้ sliding window** — เลื่อนทีละประโยค ดูหน้าต่าง 5 ประโยค ไม่ใช่นับความถี่รวมแล้วหารเฉลี่ย
4. **คำ Class A (Check 1b): บันทึกตำแหน่งทุก hit** (ย่อหน้า/ประโยค) — 1 hit = Fail
5. **จบเอกสารทำ document-level sweep อีกหนึ่งรอบ** — Check 11 (Closing Ritual) ทุก branch; Check 9 (Citation), Check 12 (Acronym), Check 13 (Reporting Verbs — ไล่ทุกจุดอ้างอิงเทียบชนิดแหล่ง) เฉพาะ branch 🟩 หรืองานที่มีการอ้างอิง — ต้องมองข้ามหัวข้อ จึงตรวจได้เฉพาะการ sweep ทั้งฉบับ
6. **รายงาน Scan Coverage** = จำนวนย่อหน้าที่ตรวจ / ย่อหน้าทั้งหมด — ต้องเท่ากับ 100% มิฉะนั้นรายงานถือว่าไม่สมบูรณ์ ห้าม output

---

## 2. LAYER 1 — AI Vocabulary Footprints Check (🟦 CORE engine — 2 Checks)

### 2.1 Methodology

เปรียบเทียบ vocabulary ในข้อความกับ **word-list ของ branch ที่กำลังตรวจ** ผ่านกลไกวัด register-agnostic ใน `06_verified_ai_signatures.md` §0 (3-Class machinery) โดยแยกเป็น 2 จุดตรวจที่วัดคนละแบบ:

| จุดตรวจ | กลไกวัด (🟦 CORE) | content ป้อนต่อ branch |
|---|---|---|
| **Check 1a — Density (Class B)** | ความหนาแน่นต่อ 1,000 คำ เทียบเป้าหมาย §5 (ดู §2.2) | 🟩 `06` §2 + §4 EN Tier 1 · 🟧 `11` watchlist · 🟪 watchlist สากล |
| **Check 1b — Zero-Tolerance (Class A)** ⭐ V03 | per-instance: พบ ≥ 1 ครั้ง = Fail ทันที (HARD GATE) | 🟩 `06` §1+§1.5+§1.6 · 🟧 `11` Class A · 🟪 watchlist Class A |

**Check 1b ห้ามใช้เกณฑ์ density เด็ดขาด** — บทเรียนจากจุดหลุดจริง: "อย่างก้าวกระโดด" ปรากฏครั้งเดียวจึงผ่านเกณฑ์ density แต่คำเร่งน้ำหนักเชิงโปรโมตครั้งเดียวก็ส่งกลิ่น — ทุก hit ต้องบันทึกตำแหน่ง (ย่อหน้า/ประโยค)

### 2.2 Check 1a Pass Criteria (Class B — Density) → SSOT pointer

> **เกณฑ์ density 5-register = SSOT ที่ `06_verified_ai_signatures.md` §5** (Pass 2 Density Targets — ใช้กับ Class B เท่านั้น). ไฟล์นี้ไม่ทำซ้ำตาราง — สรุปย่อเพื่อ orient:
>
> นานาชาติ ≤ 2 · TCI ≤ 4 · Business/Executive ≤ 3 · ราชการ ≤ 2 · Marketing ≤ 5 (ครั้ง Tier 1 / 1,000 คำ). ค่าทางการอ่านจาก `06` §5 เสมอ — แก้ที่เดียว.

### 2.3 ⚠️ สำคัญ — content ป้อนสำหรับ branch 🟩 Academic (ภาษาไทย)

> หมายเหตุ: ส่วนนี้เป็น **content ของ branch 🟩** (corpus วิชาการไทย 101 ไฟล์ / 292K คำ + iCE 13 ไฟล์) ไม่ใช่ universal default — branch 🟧/🟪 ใช้ word-list ของตน. รายการเต็มอยู่ที่ `06_verified_ai_signatures.md` §1–3.

**คำที่เคยจัดเป็น Tier 1 ใน English context แต่ใช้ได้ในภาษาไทย (Green — corpus-confirmed):**
- "ขับเคลื่อน" (272 ครั้งใน corpus 62 ไฟล์) — ✅ ใช้ได้
- "ยกระดับ" (133/43) — ✅ ใช้ได้
- "อย่างยั่งยืน" (68/32) — ✅ ใช้ได้
- "อย่างมีประสิทธิภาพ" (195/55) — ✅ ใช้ได้
- "บูรณาการ" (432/59) — ✅ ใช้แพร่หลาย
- "นอกจากนี้" (156/69) — ✅ ใช้ได้ (คุม density)

**คำที่เป็น AI signature จริงในภาษาไทย — Class A** (ปรากฏ ≤ 5 ครั้ง / 292K):
- "เป็นที่ทราบกันดีว่า" (0)
- "นับเป็นสิ่งสำคัญ" (0)
- "ในแง่หนึ่ง" (0)
- "อาจถือได้ว่า" (0)
- "อย่างพิถีพิถัน" (0)
- "ยิ่งไปกว่านั้น" (1)
- "ปฏิเสธไม่ได้ว่า" (3)

ดูรายการเต็มใน `06_verified_ai_signatures.md`

---

## 3. LAYER 2 — Statistical & Sentence Pattern Check (🟦 CORE — 7 Checks, universal ทั้งหมด)

> Layer 2 ทั้ง 7 จุดตรวจเป็น 🟦 CORE — รันทุก register ทุก branch.

### Check 1: Burstiness — Sentence Length Variability 🟦

**วิธีตรวจ:**
1. นับจำนวนคำของแต่ละประโยค
2. ตรวจ 5 ประโยคติดต่อกัน — หากมีมากกว่า 3 ประโยคยาว 16-22 คำ → **เสี่ยงสูง**
3. คำนวณ Standard Deviation (SD)

**เกณฑ์ผ่าน:**
- SD ≥ 5
- มีประโยคสั้น (5-12 คำ) ≥ 1 ต่อย่อหน้า
- มีประโยคยาว (25-35+ คำ) ≥ 1 ต่อย่อหน้า

### Check 2: Sentence Opening Variability 🟦

**❌ AI Pattern:** ทุกประโยคเริ่มด้วยประธาน + กริยา

**✅ Human Pattern:** สลับ 5 รูปแบบ:
- Adverb: "ในปี 2567 องค์กร..."
- Subordinate Clause: "เมื่อพิจารณาจาก..."
- Question: "อะไรเป็นปัจจัยสำคัญ?"
- Quote: "นักวิชาการชี้ว่า '...'"
- Prepositional: "ภายใต้กฎหมายฉบับใหม่..."

**เกณฑ์ผ่าน:** ใน 10 ประโยคติดต่อกัน อย่างน้อย 3 ประโยคต้องไม่ใช่ประธาน-กริยา

### Check 3: Paragraph Symmetry 🟦

**เกณฑ์ผ่าน:** ในเอกสาร 1,500 คำ มีย่อหน้าอย่างน้อย 3 ขนาด (สั้น/กลาง/ยาว)

### Check 4: Transition Phrase Density 🟦

**เกณฑ์ผ่าน:** ≤ 3 คำเชื่อม (นอกจากนี้/อีกทั้ง/Furthermore/Moreover) ต่อ 500 คำ

### Check 5: Bullet-Point Thinking in Prose 🟦

**❌ AI Pattern:** "มี 3 ประการ ได้แก่... ปัจจัยที่หนึ่ง... ปัจจัยที่สอง..."

**✅ Human Pattern:** เขียนเป็นความเรียงต่อเนื่อง

### Check 6: Template Proximity — โครงประโยคซ้ำในระยะใกล้ 🟦 ⭐ V03

**วิธีตรวจ (sliding window — ห้ามนับความถี่รวมทั้งฉบับ):**
1. สกัด "โครงเปิด" ของทุกประโยค (โครงสร้าง 3-4 คำแรก เช่น "เมื่อพิจารณา…ผ่าน…จะพบว่า")
2. เลื่อนหน้าต่าง 5 ประโยคทีละประโยค เทียบโครงภายในหน้าต่าง

**เกณฑ์ผ่าน:**
- โครงเปิดเดียวกันไม่ซ้ำภายใน 5 ประโยคติดกัน และไม่ซ้ำภายในย่อหน้าเดียวกัน
- โครงประโยคเต็มรูป (template) เดียวกันใช้ ≤ 1 ครั้งต่อหัวข้อ
- รูปแบบเปิดทั้ง 5 ชนิด (Adverb/Subordinate/Question/Quote/Prepositional): ชนิดละ ≤ 2 ครั้งต่อ 10 ประโยคติดกัน

**⚠️ กับดักที่เกิดจริง:** การแก้ Check 2 ด้วยการเติม Subordinate opener ถี่ ๆ ทำให้ "เมื่อพิจารณา…ผ่านกรอบ…จะพบว่า" โผล่สองครั้งติดในย่อหน้าเดียว — Check 2 ผ่าน (เพราะไม่ใช่ประธาน-กริยา) แต่ Check 6 ต้องจับ เพราะ detector และ reviewer มองเห็นการซ้ำระยะใกล้ ไม่ได้มองความถี่รวม

### Check 7: Nested Clause Depth — อนุประโยคซ้อน 🟦 ⭐ V03

**วิธีตรวจ:** ทุกประโยค นับชั้นการซ้อนของ "ซึ่ง / ที่ / อัน / โดยที่" (translationese — ตัวอย่างการแก้ใน `05_thai_academic_patterns.md` §1.3)

**เกณฑ์ผ่าน:** ≤ 2 ชั้นต่อประโยค — ประโยคที่ซ้อนเกิน ("ซึ่ง…ที่…ใน…") ให้แตกเป็น 2 ประโยคหรือยุบอนุประโยค

---

## 4. LAYER 3 — Structural & Discourse Pattern Check (6 Checks — 🟦 CORE ×3 + 🟩 Academic ×3)

> Layer 3 ผสม: Check 8/10/11 = 🟦 CORE (universal) · Check 9/12/13 = 🟩 Academic (register-specific — branch 🟧/🟪 ข้ามได้เว้นมีการอ้างอิง).

### Check 8: Paragraph Length Variability 🟦

**เกณฑ์ผ่าน:** ความยาวย่อหน้าในช่วง 3-12 ประโยค โดย:
- ย่อหน้าสั้น (2-3 ประโยค) ≥ 20%
- ย่อหน้ายาว (7+ ประโยค) ≥ 20%

### Check 9: Citation Distribution 🟩 Academic

**❌ AI Pattern:** Cluster citations ที่จุดเดียวกัน "(Smith, 2020; Jones, 2021; Brown, 2022; Lee, 2023; Wang, 2024)"

**เกณฑ์ผ่าน:** ไม่มี citation cluster ที่มี ≥ 4 citations ติดกัน — ยกเว้นใน literature review

> 🟩 **ผูก register วิชาการ:** จุดตรวจนี้สมเหตุสมผลเฉพาะงานที่มีระบบอ้างอิง — branch 🟧 Business / 🟪 General ข้ามได้เว้นแต่งานนั้นมี citation จริง.

### Check 10: Personal Voice Markers 🟦

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

### Check 11: Section-Closing Ritual Uniformity 🟦 ⭐ V03

**วิธีตรวจ (document-level sweep):** เก็บประโยคปิดของทุกหัวข้อมาเรียงเทียบกัน

**เกณฑ์ผ่าน:**
- Forward signpost ("…ในหัวข้อถัดไป" / "ดังจะได้กล่าวต่อไป") ≤ 1 ครั้งต่อเอกสาร
- ไม่มีสองหัวข้อติดกันที่ปิดด้วยสูตรเดียวกัน
- การปิดหัวข้อทั้งเอกสารมีอย่างน้อย 3 แบบ (ทางเลือกการปิดดู `05_thai_academic_patterns.md` §9)

**หลักคิด:** สัญญาณ AI อยู่ที่ "ทุกหัวข้อปิดด้วยพิธีกรรมเดียวกัน" ไม่ใช่จำนวนครั้ง — signpost 3 ครั้งจาก 3 หัวข้อ = Fail แม้ density จะดูรับได้ **ห้ามใช้ดุลยพินิจแบบ density กับ check นี้** (บทเรียนจริง: เคยตัดสินใจคงไว้ 2 จุดเพราะคิดว่า density รับได้ — ผลคือหลุด)

### Check 12: Acronym Re-Expansion 🟩 Academic ⭐ V03

**วิธีตรวจ (document-level sweep):** หาทุกคู่ "ชื่อเต็ม (ตัวย่อ)" เช่น "กรอบคน-กระบวนการ-เทคโนโลยี (PPT)" แล้วนับการปรากฏซ้ำของชื่อเต็ม+วงเล็บเดิมหลังการนิยามครั้งแรก

**เกณฑ์ผ่าน:** นิยามเต็มรูปครั้งแรกครั้งเดียว — การเอ่ยครั้งถัดไปใช้ตัวย่อล้วน ("กรอบ PPT")
**ข้อยกเว้น:** ดุษฎีนิพนธ์โครงสร้าง 5 บท อนุญาต re-define ครั้งแรกของแต่ละบท

**นิสัย LLM:** นิยามอักษรย่อเต็มยศใหม่ทุกครั้งที่เอ่ยถึง — คนเขียนจริงนิยามครั้งเดียวแล้วใช้ตัวย่อตลอด (รายละเอียด `05_thai_academic_patterns.md` §8)

> 🟩 **ผูก register วิชาการ:** ข้อยกเว้น 5-บท ใช้กับดุษฎีนิพนธ์ — branch 🟧/🟪 ตรวจ acronym hygiene ทั่วไปได้แต่ไม่มี 5-บท exception.

### Check 13: Reporting Verb–Evidence Alignment 🟩 Academic ⭐ V03

**วิธีตรวจ (document-level sweep):** ไล่ทุกจุดอ้างอิง/การรายงานแหล่ง ระบุชนิดแหล่ง (ทัศนะ / เชิงประจักษ์ / หลายแหล่งสอบทาน) แล้วเทียบกริยารายงานกับตาราง `05_thai_academic_patterns.md` §10

**เกณฑ์ผ่าน:**
- งานทัศนะ/บทความวิชาการ ไม่ใช้ "ยืนยันว่า / พิสูจน์ว่า / พบว่า" (ใช้ เสนอว่า, ชี้ว่า, มองว่า, วิเคราะห์ว่า)
- งานเชิงประจักษ์ ไม่ใช้ "พิสูจน์ว่า" เว้นแต่มีการทดสอบสมมติฐานจริง (ใช้ พบว่า, รายงานว่า, แสดงให้เห็นว่า)
- "ยืนยันในทิศทางเดียวกันว่า" สงวนไว้สำหรับหลายแหล่งที่ให้ผลตรงกัน

**นิสัย LLM:** ใช้ "พบว่า" เหมารวมทุกแหล่ง — กริยาแรงเกินหลักฐาน = overclaim ที่ reviewer จับและเข้าข่าย fabrication ระดับ claim

> 🟩 **ผูก register วิชาการ:** จุดตรวจนี้ตรวจ reporting-verb ของการอ้างอิงแหล่ง — branch 🟧/🟪 ข้ามได้เว้นแต่งานนั้นรายงานแหล่งอ้างอิงเชิงวิชาการ.

---

## 5. Detection Report Template

ใช้ template ใน `../templates/detection_report.md` เมื่อ output ผลตรวจ — รายงานต้องระบุ branch ที่ตรวจ (🟩/🟧/🟪) และจำนวน academic checks ที่รัน/ข้าม

---

## 6. Score Interpretation

**การนับสถานะรวม:** ผ่าน X/15 จุดตรวจ — เกณฑ์ผ่าน ≥ 13/15 **และ** Check 1b ต้องผ่าน (1b Fail = Fail ทั้งฉบับ ไม่ว่าคะแนนอื่นเป็นเท่าใด)

> **branch 🟧/🟪 ที่ข้าม 3 academic checks (9/12/13):** เกณฑ์ผ่านปรับเป็น ≥ 11/12 (Check 1b ยังเป็น hard-gate). รายงานต้องระบุชัดว่ารัน 12 CORE checks ไม่ใช่ 15.

| AI Score | Action |
|---|---|
| 0-20% | Pass — ส่งงานได้ |
| 21-40% | Light revision (Pass 1 อย่างเดียวก็พอ) |
| 41-60% | Substantial rewrite (Pass 1 + Pass 2) |
| 61-80% | Section-by-section humanization (Two-Pass + Advanced) |
| 81-100% | Full rewrite |

---

## CHANGELOG

- **V04R01 (2026.06.13)** — RE-LABEL core engine vs academic checks (Shared Core + 3 Branches เท่าเทียม, ไม่มี academic default). (1) **§1.1 NEW Check Inventory** — แยก 🟦 CORE 12 จุด (1a/1b + Check 1–8/10/11) vs 🟩 Academic 3 จุด (Check 9 Citation / Check 12 Acronym 5-บท / Check 13 Reporting-Verb); branch 🟧/🟪 รัน 12 CORE, ข้าม 3 academic ได้เว้นมีการอ้างอิง. (2) **Check 1a/1b = CORE engine แต่ content ป้อนต่อ branch** — กลไกวัด register-agnostic ที่ `06` §0; word-list 🟩 Thai-count / 🟧 `11` / 🟪 watchlist. (3) **density table → pointer `06` §5** (ไม่ทำซ้ำ — สรุปย่อ 5-register เพื่อ orient เท่านั้น). (4) marker 🟦/🟩 ติดทุก Check inline + §2.3 re-scope เป็น "content ของ branch 🟩" (ไม่ใช่ universal). (5) Score §6 เพิ่มเกณฑ์ ≥ 11/12 สำหรับ branch ที่ข้าม academic checks. **คงเดิม verbatim:** 15-check + Scan Discipline 6 ข้อ + Pass ≥ 13/15 + Check 1b hard-gate + เกณฑ์ทุก check + บทเรียนจุดหลุดจริง + Green counts (272/62, 133/43, 195/55, 432/59, 156/69 ฯลฯ) + Class A counts (เป็นที่ทราบกันดีว่า=0 … ปฏิเสธไม่ได้ว่า=3). ห้าม fabricate.
- **V03R01 (2026.06.07)** — เพิ่ม Check 1b Zero-Tolerance, Check 6 Template Proximity, Check 7 Nested Clause Depth, Check 11 Section-Closing Ritual, Check 12 Acronym Re-Expansion, Check 13 Reporting Verb Alignment และ Scan Discipline Protocol (ยกระดับจากบทเรียนจุดหลุดจริง)
