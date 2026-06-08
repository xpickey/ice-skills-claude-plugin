# Voice/Writing Profile Extraction Prompt Template

## Prompt V1: Standard Voice Profile Extraction

```
Extract a Voice/Writing Profile from the reference documents below.
Apply the 6-Dimension framework:

D1 Sentence-Level Patterns
D2 Vocabulary Signature
D3 Paragraph Architecture
D4 Argumentation Style
D5 Citation & Reference Style
D6 Cultural & Contextual Markers

For each dimension, output statistics and examples per the
Voice Profile Output Template (templates/voice_profile.md).

Reference documents: <<<DOCS>>>
Author/Persona: <<<NAME>>>
Context: <<<ACADEMIC/BUSINESS/GOVERNMENT/MARKETING>>>

Output:
1. Complete Voice Profile filling all 6 dimensions
2. Profile ID assignment (VP-[YYYYMMDD]-[XXX])
3. 3 Calibration sample paragraphs (different topics) for user verification
```

---

## Prompt V2: Intensive Academic Voice Profile (7 Dimensions)

```
Extract a Voice/Writing Profile in INTENSIVE MODE for academic writing.
Apply the 6-Dimension framework PLUS Dimension 7 (Disciplinary Conventions).

Required reference: ≥ 5 documents, ≥ 30,000 words, span ≥ 2 years.

D7 sub-dimensions:
- Hedging norms
- First-person convention
- Reading philosophy
- Methodology language
- Theoretical framing
- Citation density expected

Output: Complete Voice Profile + 3 calibration samples + author evolution notes.

Reference: <<<DOCS>>>
Discipline: <<<FIELD>>>
Target Journal/Standard: <<<STANDARD>>>
```

---

## Prompt V3: Voice Profile Calibration

```
Show me 3 sample paragraphs (60-100 words each) on different topics,
written in the Voice Profile below. I will blind-test them.

Voice Profile: <<<PROFILE>>>

Topics for samples:
1. <<<TOPIC_1>>>
2. <<<TOPIC_2>>>
3. <<<TOPIC_3>>>

After I provide feedback, refine the profile based on what I selected
as "matching my voice" vs "not matching."
```

---

## Process Steps for Voice Extraction (Mode 2)

### Step 1: Pre-Extraction Q&A (with user)

ถามผู้ใช้:
1. "ระบุโฟลเดอร์/ไฟล์อ้างอิงที่จะสกัด Voice Profile (path เต็ม)"
2. "ผู้เขียนคือใคร? (ตนเอง / ในนามองค์กร / persona เฉพาะ)"
3. "บริบทงานคืออะไร? (Academic / Business / Government / Marketing)"
4. "ต้องการ Standard Mode (6 มิติ) หรือ Intensive Mode (7 มิติ — งานวิชาการ)?"

### Step 2: Read & Process Documents

1. ใช้ `pdftotext -layout` แปลง PDF → text (ถ้าเป็น PDF)
2. นับจำนวนคำรวมและจำนวนเอกสาร
3. ตรวจ corpus minimum:
   - Standard: ≥ 3 docs / 15,000 คำ
   - Intensive: ≥ 5 docs / 30,000 คำ / 2 ปี
4. ถ้าไม่ถึง — แจ้งผู้ใช้และขอเอกสารเพิ่ม

### Step 3: Aggregate Analysis

ใช้ Python หรือ regex เพื่อ:
- คำนวณ Mean, Median, SD ของความยาวประโยค
- นับความถี่ของคำสำคัญ
- ระบุ pattern ของบทคัดย่อ บทนำ บทสรุป
- ตรวจรูปแบบ citation

### Step 4: Deep Reading (Sample)

อ่านเชิงลึก 5-10 ฉบับเป็นตัวแทน:
- บทคัดย่อ
- ย่อหน้าแรกของบทนำ
- ย่อหน้าสรุป
- ตัวอย่างเชิงอรรถ/บรรณานุกรม

### Step 5: Synthesize Profile

กรอกเข้า template `voice_profile.md` ครบทุก Dimension

### Step 6: Calibration

ใช้ Prompt V3 เพื่อทดสอบ Profile กับผู้ใช้

### Step 7: Save & Report

- บันทึก Profile ใน `voice_profiles/[name]_VP-YYYYMMDD-XXX.md`
- แสดงสถิติให้ผู้ใช้: เอกสารที่อ่าน, จำนวนคำ, ผลการสกัด
