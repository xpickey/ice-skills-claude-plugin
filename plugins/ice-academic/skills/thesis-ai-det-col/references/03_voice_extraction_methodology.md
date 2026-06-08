# Voice/Writing Profile Extraction Methodology

## When to Read This

อ่านไฟล์นี้เมื่อทำ Mode 2 (EXTRACT) — สกัด Voice Profile จากโฟลเดอร์อ้างอิงของผู้ใช้ หรือเลือก Sub-Profile จาก KM-TH-THESIS-DOC

---

## 1. Why Voice Profile Matters

ทำงานบนพื้นฐาน **Stylometry** — ศาสตร์ที่ใช้สถิติเชิงภาษาวิเคราะห์สไตล์การเขียน เป้าหมาย: ทำให้ฉบับ humanize ไม่เพียง "ผ่าน detector" แต่ "ตรงเสียงผู้เขียน" ด้วย

---

## 2. The 5-Level Source Hierarchy (กฎเหล็ก: ห้ามเดา ห้ามมั่ว)

ไล่ตามลำดับนี้ ห้ามข้ามขั้น:

### 🥇 Level 1 — User-Specified Folder (priority สูงสุด)

**เงื่อนไข:** ผู้ใช้ระบุ folder/ไฟล์เฉพาะ

**วิธีดำเนินการ:**
1. อ่านเอกสารทุกชิ้นในแหล่งที่ระบุ
2. ใช้ pdftotext หรือ text extraction
3. สกัด 6+1 Dimensions (Section 4)
4. รวมผลเป็น Voice Profile ใหม่

### 🥈 Level 2 — This Skill's Reference (KM-TH-THESIS-DOC)

**เงื่อนไข:** ผู้ใช้ไม่ระบุแหล่ง — งานเป็นวิชาการไทย

**วิธีดำเนินการ:**
- โหลด `voice_profiles/KM-TH-THESIS-DOC_V02R01.md`
- ใช้ Decision Tree (Section 12 ของ KM-TH-THESIS-DOC) เลือก 1 ใน 7 Sub-Profiles

### 🥉 Level 3 — Active Skill's Knowledge Base

(ใน skill อื่นที่อาจมี Voice Profile ฝัง — ไม่ใช่กรณีของเรา)

### 4️⃣ Level 4 — Pre-defined Library

KM-TH-THESIS-DOC มี 7 Sub-Profiles ครบ:
- VP-A1, VP-A2, VP-B1, VP-B2, VP-C1, VP-C2, VP-C3

### 5️⃣ Level 5 — ASK USER (ห้ามเดา)

**เงื่อนไข:** ทุก Level 1-4 ไม่มีข้อมูล

**ต้องถามผู้ใช้:**
> "ผมไม่พบ Voice/Writing Profile ในแหล่งที่กำหนด ครับ
> เพื่อให้การ humanize ตรงเสียงผู้เขียน กรุณาระบุ:
> (a) โฟลเดอร์/ไฟล์อ้างอิงที่ผมจะสกัด Voice ได้
> (b) เลือก Pre-defined Voice Profile (VP-A1 ถึง VP-C3)
> (c) ให้ผมเขียน 3 ตัวอย่างต่างกัน เพื่อให้ท่านเลือก
> (d) ดำเนินการต่อโดยใช้ Default Profile (จะระบุข้อจำกัดในผลลัพธ์)"

---

## 3. Reference Corpus Requirements

### 3.1 Minimum (Standard Mode)

- อย่างน้อย **3 เอกสาร** ของผู้เขียนเดียวกัน
- รวมความยาวไม่ต่ำกว่า **15,000 คำ**

### 3.2 Intensive Mode (สำหรับงานวิชาการระดับสูง)

- อย่างน้อย **5 เอกสาร** ของผู้เขียนเดียวกัน
- รวมความยาวไม่ต่ำกว่า **30,000 คำ**
- ครอบคลุมช่วงเวลาอย่างน้อย **2 ปี**

**เหตุผล:** งานวิจัย stylometry แสดงว่าสไตล์ผู้เขียนสามารถระบุได้ใน 5,000 คำขึ้นไป ความเสถียรเพิ่มขึ้นชัดเมื่อมี ≥ 30,000 คำ

---

## 4. The 6+1 Dimensions

ไม่ว่าใช้แหล่งใด ต้องสกัดให้ครบทั้ง 6 มิติ + เพิ่ม Dimension 7 ในกรณี Intensive Mode

### 📐 Dimension 1: Sentence-Level Patterns

**สิ่งที่ต้องสกัด:**
- ความยาวประโยคเฉลี่ย (Mean จำนวนคำ)
- การกระจายตัว (Distribution: short/medium/long ใน %)
- ค่า Standard Deviation (SD)
- ประเภทประโยคที่ใช้บ่อย (บอกเล่า/เงื่อนไข/เปรียบเทียบ/เหตุและผล)
- ตำแหน่งของประธานและกริยา
- การใช้ประโยคซ้อน vs ประโยคเดี่ยว

**Output:**
```
- Mean: 19.4 words
- Distribution: Short(5-12) 22% / Medium(13-24) 51% / Long(25+) 27%
- SD: 7.8
- Frequent types: Comparative 38%, Causal 29%, Conditional 20%
- S-V position: Subject-first 65%, Adverbial-first 20%, Quote/Question 15%
- Complex: 60% / Simple: 40%
```

### 📚 Dimension 2: Vocabulary Signature

**สิ่งที่ต้องสกัด:**
- ศัพท์เทคนิคที่ใช้บ่อย (พร้อมความถี่)
- คำเชื่อมที่ปรากฏบ่อย
- คำกริยาที่นิยมใช้ในการวิเคราะห์
- คำคุณศัพท์เชิงวิชาการ
- **คำที่ผู้เขียนหลีกเลี่ยง** (สำคัญ — สำหรับ Pass 2)

### 🏗️ Dimension 3: Paragraph Architecture

- ความยาวย่อหน้าเฉลี่ย
- รูปแบบการเปิดย่อหน้า (Topic Sentence/Question/Quote/Statistic)
- รูปแบบการปิดย่อหน้า
- การจัดเรียงเหตุผล (Inductive/Deductive/Mixed)

### ⚔️ Dimension 4: Argumentation Style

- วิธีนำเสนอ Claim (assertive/hedged)
- วิธียก Evidence (จำนวน citations ต่อ claim)
- วิธีวิเคราะห์ (เปรียบเทียบ/สังเคราะห์/วิพากษ์)
- วิธีจัดการ Counterargument
- น้ำหนัก Theory vs Empirical

### 📑 Dimension 5: Citation & Reference Style

- ความถี่ของ in-text citation (ต่อ 100 คำ)
- ตำแหน่งที่นิยมวาง citation (end/mid/opening)
- รูปแบบการกล่าวถึงผู้แต่ง (Author-prominent vs Information-prominent)
- การใช้ Direct Quote vs Paraphrase
- รูปแบบ citation (APA, Chicago, Vancouver, เชิงอรรถ)

### 🇹🇭 Dimension 6: Cultural & Contextual Markers

- การอ้างบริบทไทย (กฎหมาย/หน่วยงาน/นโยบาย)
- การใช้คำศัพท์ทางพระพุทธศาสนา (ถ้ามี)
- การยกตัวอย่างกรณีศึกษา (Thailand/ASEAN/International ratio)
- น้ำเสียงทางวัฒนธรรม (Formal/Semi-formal/Informal)

### 🎓 Dimension 7 (Intensive Academic Only): Disciplinary Conventions

- Hedging norms ของสาขา (laden/sparse)
- การใช้ first-person (ผู้วิจัย/I/We)
- Reading philosophy (positivist/interpretive/critical)
- Methodology language
- Theoretical framing
- Citation density expected by journal

---

## 5. Calibration & Memory Creation

### 5.1 Standard Calibration

หลังสกัด Voice Profile:
1. **Calibration Review** — แสดง Profile ให้ผู้ใช้ดู
2. **Test on Sample** — ให้ Claude เขียน sample paragraph 50-80 คำ ตาม Profile
3. **User Feedback** — ผู้ใช้ยืนยันหรือปรับ
4. **Iteration** — ปรับ Profile จนตรง

### 5.2 Intensive Calibration (Academic)

1. Claude เขียน 3 sample paragraphs ที่ topic ต่างกัน
2. ผู้ใช้ blind test — เลือก paragraph ที่เหมือนเสียงตน
3. ถ้า ≥ 2 จาก 3 paragraphs ผู้ใช้ระบุว่าเหมือน → Profile pass
4. ถ้าไม่ → กลับไปสกัดใหม่ พร้อมระบุประเด็นที่คลาดเคลื่อน

### 5.3 Memory Storage

บันทึกใน:
- Profile ID: VP-[YYYYMMDD]-[XXX]
- ตำแหน่ง: `voice_profiles/[user-defined-name].md`
- Memory Index Entry — บันทึกการใช้งานครั้งนี้

---

## 6. Voice Profile Output Template

ใช้ template ใน `../templates/voice_profile.md`

---

## 7. KM-TH-THESIS-DOC Decision Tree

ถ้าผู้ใช้ไม่ระบุแหล่งและงานเป็นวิชาการไทย ใช้ตัดสินใจ:

```
START → เป็นงาน มจร? (ดุษฎีนิพนธ์/วิทยานิพนธ์)
         │
        ┌┴┐
       Yes No
        │  │
       ┌┴┐ │
   Buddhist เป็นแกน?
    Yes No  │
     │  │   │
    A2 A1   เป็น Research (มีสถิติ x̄, SD)?
                │
              ┌┬┴┬─┐
              │  │ │
            Academic Research
                 │       │
              วารสาร?    สาขา?
              ┌┴┐    ┌──┼──┐
              AGJ Other บัญชี จัดซื้อ รัฐ/Edu
              B1 B2   C1   C2   C3
```
