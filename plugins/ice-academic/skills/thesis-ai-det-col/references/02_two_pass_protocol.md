# Two-Pass Correction Protocol

**V06R02** · 2026.06.13 · 🟦 CORE (register-agnostic) · Shared Core + 3 Branches (🟩 Academic / 🟧 Business / 🟪 General เท่าเทียม) · *[R02: กู้ em-dash worked example (split orphan) + pointer →11 §7.4]*

## When to Read This

🟦 **CORE — register-agnostic.** ไฟล์นี้คือกลไกแก้ไขสองรอบ (Rhythm + Vocabulary) ที่ใช้ได้กับทุก register — 🟩 Academic / 🟧 Business / 🟪 General เรียกใช้กลไกเดียวกัน ต่างกันแค่ "ตารางคำ/ความหนาแน่น/Voice Profile" ที่แต่ละ branch หยิบมาเสียบ (ดู Step 2.1 / Step 2.2). ไม่มี academic default ฝังในกลไก

อ่านเมื่อทำขั้นตอน CORRECT (แก้ไข) หรือ FULL CYCLE ของ register ใดก็ตาม — ต้องการรายละเอียด Pass 1 (Rhythm) + Pass 2 (Vocabulary) + Advanced Techniques (→ §4 pointer)

---

## 1. กฎเหล็ก: ห้ามทำพร้อมกัน

**Pass 1 — Rhythm Correction:** แก้รูปแบบประโยค (จังหวะ ความยาว การเปิด)
**Pass 2 — Vocabulary Correction:** แก้คำศัพท์โดยอ้าง Voice Profile

### เหตุผลที่ต้องแยก

1. **Cognitive Load:** การแก้สองมิติพร้อมกันทำให้พลาดประเด็น
2. **Verifiability:** การแยก Pass ทำให้วัดผลแต่ละมิติได้
3. **Symptom Substitution Risk:** ทำพร้อมกันมักเปลี่ยนคำ AI เป็นคำ AI อีกคำ
4. **Quality Control:** Pass 1 ต้องตรวจ SD ≥ 5 ก่อน Pass 2
5. **Voice Profile Alignment:** Pass 2 ต้องอ้าง Voice Profile

**ลำดับ:** Draft → Pass 1 → ตรวจ SD ≥ 5 → Pass 2 → ตรวจ Tier 1 → Advanced (ถ้าจำเป็น) → Done

---

## 2. PASS 1: Rhythm Correction (5 Steps)

### Step 1.1: ระบุย่อหน้าที่เสี่ยง

**วิธีการ:**
1. อ่านทีละย่อหน้า
2. นับจำนวนคำของแต่ละประโยค
3. หากมีมากกว่า 3 ประโยคยาว 16-22 คำ ใน 5 ประโยคติดต่อกัน → **mark ย่อหน้านั้น**

### Step 1.2: ปรับความยาวประโยค (Burstiness Injection)

**กฎการแก้ (ต่อย่อหน้าที่ mark):**
- **ตัด 2 ประโยคให้สั้นลง (8-12 คำ)** — เลือกประโยคที่มี filler หรือ adjective เกิน
- **ขยาย 1 ประโยคให้ยาวขึ้น (25-35 คำ)** — ใส่รายละเอียดเฉพาะ ตัวเลข ชื่อ บริบท

**ตัวอย่าง:**

*ก่อน:* "ระบบนี้ช่วยลดต้นทุนการดำเนินงานอย่างมีนัยสำคัญ องค์กรที่นำระบบไปใช้พบผลลัพธ์ที่ดีอย่างต่อเนื่อง ทีมงานสามารถทำงานได้อย่างมีประสิทธิภาพมากขึ้น" — SD ≈ 1.7 ❌

*หลัง:* "ต้นทุนลดลง 23% ในเดือนแรก ที่บริษัท ABC ในไตรมาส 2 ปี 2567 ทีม Finance รายงานว่าพวกเขาปิดบัญชีรายเดือนเร็วขึ้น 4 วันโดยไม่ต้องเพิ่มคนเลย ผู้บริหารยอมรับ" — SD ≈ 14.4 ✅

### Step 1.3: ปรับการเปิดประโยค (5 รูปแบบ)

ใน 10 ประโยคติดต่อกัน ต้องมีอย่างน้อย 3 ประโยคเปิดด้วยรูปแบบที่ไม่ใช่ประธาน-กริยา:

1. **Adverb:** "ในปี 2567 องค์กรทั้งหมด 245 แห่ง..."
2. **Subordinate Clause:** "เมื่อพิจารณาจากข้อมูลย้อนหลัง 5 ปี เราพบว่า..."
3. **Question:** "อะไรเป็นปัจจัยสำคัญที่ทำให้สำเร็จ?"
4. **Quote:** "นักวิชาการชี้ว่า 'การปฏิรูปต้องเริ่มจาก...'"
5. **Prepositional:** "ภายใต้กฎหมายฉบับใหม่ หน่วยงานต้อง..."

**เพดานการซ้ำ (Template Proximity Guard) ⭐ V03 — บังคับคู่กับการ diversify:**
- รูปแบบเปิดชนิดเดียวกัน ≤ 2 ครั้งต่อ 10 ประโยคติดกัน
- Lexical template เดียวกัน (เช่น "เมื่อพิจารณา…จะพบว่า") ≤ 1 ครั้งต่อหัวข้อ — ห้ามซ้ำในย่อหน้าเดียวกันเด็ดขาด
- ⚠️ บทเรียนจริง: การ diversify ด้วย Subordinate opener ถี่เกิน ทำให้ "เมื่อพิจารณา…ผ่านกรอบ…จะพบว่า" ซ้ำสองครั้งติด — diversify หมายถึง "หลายแบบสลับกัน" ไม่ใช่ "แบบเด่นแบบเดียวถี่ขึ้น" (ตรวจซ้ำด้วย Layer 2 Check 6)

### Step 1.4: ปรับ Paragraph Architecture

**กฎ:**
1. ย่อหน้ายาวเท่ากันมากกว่า 3 ย่อหน้าติดกัน → แตกย่อหน้าหนึ่งให้สั้น
2. ทุกย่อหน้าเปิดด้วย topic sentence → เปลี่ยนหนึ่งย่อหน้าให้เปิดด้วย anecdote
3. ทำให้มีย่อหน้าอย่างน้อย 3 ขนาด (สั้น 2-3 / กลาง 4-6 / ยาว 7+)

### Step 1.5: ตรวจ Burstiness ใหม่ (Pass 1 Exit)

- ✅ ทุกย่อหน้ามี SD ≥ 5
- ✅ Sentence Opening Variability ผ่าน
- ✅ Paragraph Length มีอย่างน้อย 3 ขนาด

**หาก Pass 1 ผ่าน → ไปต่อ Pass 2**

---

## 3. PASS 2: Vocabulary Correction (6 Steps)

### Step 2.1: Search & Replace 9 หมวด ตามลำดับ

🟦 **CORE:** ลำดับ 9 หมวดเป็น register-agnostic — แต่ **ตารางคำ/density ที่หยิบมาเสียบในแต่ละหมวดต่างกันตาม branch** (🟩 SSOT = `06_verified_ai_signatures.md` · 🟧 SSOT = `11_business_ai_patterns.md` · 🟪 ใช้คำที่ overlap ทั้งสอง branch — Tier 1 EN + Class A สากล). ทั้ง 3 เท่าเทียม ห้าม default Academic

ตรวจตามลำดับ ห้ามสลับ:

1. Tier 1 English Verbs (delve, leverage, foster, navigate)
2. Tier 1 English Adjectives (comprehensive, robust, seamless)
3. Tier 1 English Nouns (landscape, realm, tapestry)
4. AI Phrase Templates ("It's important to note", "In today's fast-paced")
5. คำเปิดประโยคไทย → ตาราง SSOT ตาม branch (🟩 `06_verified_ai_signatures.md` · 🟧 `11_business_ai_patterns.md`)
6. คำขยายไทยพร่ำเพรื่อ
7. คำเชื่อมไทยซ้ำ
8. Hedging ซ้ำ
9. **Class A Zero-Tolerance** ⭐ V03 → **ดู SSOT (pointer):** 🟩 `06_verified_ai_signatures.md` §1.5-1.6 · 🟧 `11_business_ai_patterns.md` (Anti-ลิเก L1-8 / Class A ฝั่งธุรกิจ). หลักการ register-agnostic: คำเร่งน้ำหนักโปรโมต + สูตรสังเคราะห์ เจอครั้งเดียวต้องลบ/แทน **ห้ามใช้เกณฑ์ density** (density ใช้กับ Class B เท่านั้น). ตัวอย่าง 🟩: "อย่างก้าวกระโดด", "พลิกโฉม", "ทั้งหมดนี้สังเคราะห์ได้ว่า"

### Step 2.2: Replace ตาม Voice Profile

🟦 **CORE (register-agnostic):** กลไกคงเดิมทุก register — ใช้ Voice Profile ที่ Calibrated แล้ว โดย D2 Vocabulary Signature ระบุ "คำที่ผู้เขียนใช้บ่อย" และ "คำที่ผู้เขียนหลีกเลี่ยง" แล้วเลือกคำแทนที่ตามนั้น. ตัวคำแทนที่ขึ้นกับ branch — 🟩/🟧/🟪 เท่าเทียมกัน ไม่มี branch ใดเป็นค่าเริ่มต้น

**ตัวอย่างคำแทนที่ตาม branch (Tier 1: "leverage" / "ขับเคลื่อนด้วย"):**

🟩 **Academic** — เลือก Voice Profile วิชาการ (ดูชุด A1/A2/B1/B2/C1/C2/C3 ใน `03_voice_extraction_methodology.md` + `voice_profiles/`)

| Voice Profile | คำแทนที่ที่ตรง |
|---|---|
| Profile A1/A2 (MCU) | "อาศัย" / "ใช้กลไก" |
| Profile B1 (AGJ) | "ขับเคลื่อน" / "ใช้" |
| Profile C1 (Accounting Research) | "ใช้" / "ประยุกต์ใช้" |

🟧 **Business** — เลือก Voice Profile เชิงธุรกิจ/ข้อเสนอ (ดู `11_business_ai_patterns.md` — ตารางคำ + Voice ฝั่งธุรกิจ)

| บริบท | คำแทนที่ที่ตรง |
|---|---|
| Proposal / Executive (formal) | "ใช้" / "อาศัย" + ระบุผลเชิงตัวเลข |
| Pitch / Marketing | คงพลังได้แต่ผูกกับ proof point จริง — เลี่ยงสูตรลอย |

🟪 **General** — เลือก Voice Profile ทั่วไป (ความเป็นทางการกลาง ๆ — ไม่ผูกศัพท์เฉพาะวิชาการหรือธุรกิจ)

| บริบท | คำแทนที่ที่ตรง |
|---|---|
| Explanatory / Informational | "ใช้" / "ทำให้เกิด" + รายละเอียดเฉพาะ |
| Narrative / Opinion | ตามเสียงผู้เขียนจริง |

> ⚠️ ทั้ง 3 branch เท่าเทียม — เลือกตาม register ของงาน ห้าม default ไป Academic. ถ้ายังไม่มี Voice Profile ของ branch นั้น → calibrate ก่อน (`03_voice_extraction_methodology.md`) ห้ามยืมโปรไฟล์ข้าม register

### Step 2.3: ระวัง Symptom Substitution

**❌ ห้าม:** เปลี่ยนคำ AI เป็นคำ AI อีกคำ

| ❌ Wrong | ✅ Right |
|---|---|
| comprehensive → robust | comprehensive → "ครอบคลุม AP, AR, GL" |
| ขับเคลื่อน → ผลักดัน | ขับเคลื่อน → "ลดต้นทุน 18% ใน 6 เดือน" |
| อย่างยั่งยืน → อย่างต่อเนื่อง | อย่างยั่งยืน → "ตลอด 5 ปีข้างหน้า" |

### Step 2.4: เพิ่ม Specificity

ทุกคำคลุมเครือต้องเปลี่ยนเป็นรายละเอียดเชิงรูปธรรม:

| คลุมเครือ | เฉพาะเจาะจง |
|---|---|
| "หลายมิติ" | "ในด้านการเงิน บุคลากร และเทคโนโลยี" |
| "หลากหลาย" | "ทั้ง 5 หน่วยงาน — กรมบัญชีกลาง..." |
| "อย่างต่อเนื่อง" | "ตั้งแต่ปี 2562 ถึงปัจจุบัน" |
| "อย่างมีประสิทธิภาพ" | "ลด cycle time จาก 14 วัน เหลือ 4 วัน" |

### Step 2.5: Template-Level Replace (รื้อโครง ไม่ใช่ถอดคำ) ⭐ V03

สแกนตาราง **Thai Formulaic Sentence Templates** (`05_thai_academic_patterns.md` §7) — จับทั้งโครงประโยค ไม่ใช่รายคำ

**วิธีแก้ที่ถูก:** รื้อโครงทั้งประโยค — เขียนข้อความตรง ระบุข้อค้นพบ/ช่องว่างวิจัยจริง

**❌ ห้ามแก้เปลือก:** ลบ "อย่างไรก็ตาม" ออกแต่คงโครง "คำถามสำคัญที่ยังไม่ได้รับคำตอบคือ…" ไว้ — template ยังอยู่ detector ยังจับ (บทเรียนจริง: การลดคำรายตัวโดยไม่มองทั้งประโยคคือสาเหตุจุดหลุด)

| ก่อน (template) | หลัง (รื้อโครง) |
|---|---|
| "อย่างไรก็ตาม คำถามสำคัญที่ยังไม่ได้รับคำตอบคือกลไกใดทำให้นโยบายไม่บรรลุผล" | "งานวิจัยที่ทบทวนยังไม่ได้ตอบว่ากลไกใดทำให้นโยบายไม่บรรลุผล — ช่องว่างนี้คือจุดที่บทความนี้เข้าไปตรวจสอบ" |
| "ทั้งหมดนี้สังเคราะห์ได้ว่าการบูรณาการข้อมูลคือเงื่อนไขตั้งต้น" | "การบูรณาการข้อมูลจึงเป็นเงื่อนไขตั้งต้น" / เปิดย่อหน้าด้วยข้อค้นพบเลย |

### Step 2.6: Reporting Verb Alignment (กริยารายงานตรงชนิดแหล่ง) ⭐ V03

🟩 **Branch-conditional (Academic-primary):** บังคับเมื่อมีการอ้างอิงแหล่ง — งานวิชาการเป็นหลัก. 🟧 Business/🟪 General ใช้เมื่ออ้างงานวิจัย/ข้อมูลแหล่งที่สาม; งานที่ไม่มี citation ข้ามได้

ไล่ทุกจุดอ้างอิง เทียบกริยารายงานกับตาราง `05_thai_academic_patterns.md` §10:

- งานทัศนะ/บทความวิชาการ → เสนอว่า, ชี้ว่า, มองว่า, วิเคราะห์ว่า (ห้าม ยืนยันว่า/พิสูจน์ว่า/พบว่า)
- งานเชิงประจักษ์ → พบว่า, รายงานว่า, แสดงให้เห็นว่า (ห้าม พิสูจน์ว่า เว้นแต่ทดสอบสมมติฐานจริง)
- หลายแหล่งให้ผลตรงกัน → ยืนยันในทิศทางเดียวกันว่า, สอดคล้องกัน

กริยาแรงเกินหลักฐาน = overclaim ต้องแก้ทุกจุด — ห้ามยกระดับ claim เพื่อให้ข้อความดูหนักแน่น

**Pass 2 Exit Criteria** (🟦 CORE — Class B density/Class A table หยิบจาก SSOT ของ branch ที่ใช้):
- ✅ Tier 1 word density ผ่านเกณฑ์ (Class B — density ตาม register: 🟩 `06` §5 / 🟧 `11`)
- ✅ ไม่มีคำ Class A Zero-Tolerance หลงเหลือ (สแกนทุกบรรทัด — SSOT: 🟩 `06` §1/1.5/1.6 · 🟧 `11`)
- ✅ ไม่มี Formulaic Template หลงเหลือ — ตรวจทั้งโครง ไม่ใช่แค่คำ
- ✅ ไม่มีโครงเปิดซ้ำภายใน 5 ประโยค/ย่อหน้าเดียวกัน
- ✅ Forward signpost ≤ 1 ครั้ง/เอกสาร และไม่มีหัวข้อติดกันปิดด้วยสูตรเดียวกัน
- ✅ Acronym นิยามเต็มครั้งเดียว หลังจากนั้นใช้ตัวย่อ
- ✅ ทุกประโยคซ้อนอนุประโยค ≤ 2 ชั้น
- ✅ 🟩 กริยารายงานตรงกับชนิดแหล่งทุกจุดอ้างอิง (`05` §10) — branch-conditional (ดู Step 2.6)
- ✅ ไม่มี Symptom Substitution
- ✅ ทุกคำคลุมเครือถูกแทนด้วยรายละเอียด
- ✅ คำที่เลือกตรงกับ Voice Profile (ของ branch ที่ใช้)

---

## 4. ADVANCED CORRECTION TECHNIQUES → ดู SSOT ใน `04`

🟦 **CORE pointer (de-dup):** ใช้เสริมหลัง Pass 1+2 ผ่านแล้ว แต่ AI score ยังสูง. รายละเอียด **Advanced Techniques ทั้งชุด เป็น SSOT ที่ `04_correction_techniques.md`** (18 Techniques T1-T18 + Anti-Patterns 8 + ตัวอย่าง before/after) — ห้าม duplicate ที่นี่

**Map 4 Advanced → 18-Technique Catalog (`04`):**

| Advanced (เดิม) | → `04` Technique | หมายเหตุ register |
|---|---|---|
| A. Sentence Combining & Splitting | T2 Burstiness + T10 Asymmetric Density | register-agnostic |
| B. Personal / Cultural Markers | T1 Personal Anchor + T12 Cultural/Temporal | 🟩 ไทย/ราชการ: พ.ร.บ./หนังสือ ว.; Profile A2: พระไตรปิฎก + "ผู้วิจัย/รูปหรือคน" · 🟧 Business: ชื่อบริษัท/ตัวเลขดีล · 🟪 General: เหตุการณ์/ปีจริง |
| C. Aside & Qualification (em dash) | T7 Counterargument + Adv C | em dash ภาษาไทย ≤ 1 ครั้ง/300 คำ (ทุก register) · ตัวอย่าง: *"ระบบนี้ได้ผลดี — แม้จะมีข้อจำกัดในการใช้งานช่วงแรกที่ผู้ใช้ต้องเรียนรู้ใหม่ — ในที่สุดก็ยอมรับโดยทั่วไป"* |
| D. Imperfect Flow | T18 + Anti-Pattern "filler burstiness" | "นอกจากนี้/อีกทั้ง/ยิ่งไปกว่านั้น" ≤ 1 ครั้ง/1,000 คำ; ปล่อยบางย่อหน้าเริ่ม abrupt / จบปลายเปิด |

> รายละเอียดเต็ม + ตัวอย่าง → `04_correction_techniques.md`. branch-specific marker (🟩/🟧/🟪) เลือกตาม register ของงาน — กลไกแทรกเหมือนกัน ต่างกันแค่ชนิด marker. ตัวอย่าง Personal/Cultural anchor ราชการ → `11` §7.4

---

## 5. Visual Summary

🟦 กลไกเดียวกันทุก register — สิ่งที่เปลี่ยนคือ Voice Profile + ตารางคำ/density ที่หยิบจาก SSOT ของ branch (🟩 `06`/`05` · 🟧 `11` · 🟪 overlap)

```
┌────────────────────────────────────────────────────────┐
│  Draft (after Detection)                                │
│  + Voice Profile ของ branch (🟩 Academic / 🟧 Business   │
│    / 🟪 General — เท่าเทียม, calibrate ก่อนใช้)          │
│         ↓                                                │
│  PASS 1: RHYTHM CORRECTION (5 Steps) — register-agnostic │
│  1.1 ระบุย่อหน้าเสี่ยง                                    │
│  1.2 Burstiness Injection (ตัด 2 / ขยาย 1)              │
│  1.3 Diversify Sentence Openings (5 รูปแบบ)            │
│  1.4 Adjust Paragraph Architecture                      │
│  1.5 Verify SD ≥ 5                                      │
│         ↓                                                │
│  PASS 2: VOCABULARY CORRECTION (6 Steps)                │
│  2.1 Search & Replace 9 หมวด (Class A → SSOT ของ branch) │
│  2.2 Replace by VOICE PROFILE (🟩/🟧/🟪 เท่าเทียม)       │
│  2.3 Avoid Symptom Substitution                         │
│  2.4 Add Specificity                                    │
│  2.5 Template-Level Replace (รื้อโครง)                  │
│  2.6 Reporting Verb Alignment — 🟩 branch-conditional   │
│         ↓                                                │
│  ADVANCED (เลือกใช้ตามจำเป็น) → SSOT `04`                │
│  A→T2/T10 · B→T1/T12 · C→T7 · D→T18  (marker ตาม branch) │
│         ↓                                                │
│  Re-Detection → ผ่าน → Voice Match Scoring              │
└────────────────────────────────────────────────────────┘
```

---

## Changelog

- **V06R01 (2026.06.13)** — RE-LABEL เป็น 🟦 CORE register-agnostic ภายใต้สถาปัตยกรรม Shared Core + 3 Branches เท่าเทียม (🟩 Academic / 🟧 Business / 🟪 General). (1) Trigger (When to Read) → register-neutral ไม่ผูก Mode 3 academic. (2) Step 2.2 Voice table → แยก 3 branch เท่าเทียม + กฎห้าม default Academic / ห้ามยืมโปรไฟล์ข้าม register. (3) §4 Advanced → pointer ไป `04` (SSOT 18 Techniques) + map A-D→T2/T10/T1/T12/T7/T18 (ตัด ~30 บรรทัดซ้ำ). (4) Class A / Class B density → pointer ไป SSOT ตาม branch (🟩 `06` · 🟧 `11`). (5) Step 2.6 Reporting Verb → flag branch-conditional (Academic-primary). คง Pass 1/Pass 2 thresholds (SD≥5, density Class B, Class A zero-tolerance) ครบ.
