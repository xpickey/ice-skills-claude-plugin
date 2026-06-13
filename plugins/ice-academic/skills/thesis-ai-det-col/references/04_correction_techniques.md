# 18 Correction Techniques Catalog — 🟦 CORE + 3 Branches (🟩/🟧/🟪)

## When to Read This

Reference catalog ของ 18 เทคนิคการแก้ไขเฉพาะรายตัว — ใช้คู่กับ Two-Pass Protocol (`02_two_pass_protocol.md`) เมื่อต้องการตัวอย่าง before/after และการ map กับ Layer/Pass

**Architecture:** catalog นี้เป็น 🟦 **CORE** — กลไกการแก้ register-agnostic (ไม่มี academic default). แต่ละ technique tag ว่าเป็น **กลไก** register ไหน:

- 🟦 **CORE** — กลไกที่ทำงานได้ทุก register (academic = business = general เท่าเทียม)
- 🟩 **Academic** / 🟧 **Business** / 🟪 **General** — กลไกที่ผูกกับ register นั้นโดยธรรมชาติ (3 branch เท่าเทียม ไม่มีตัวใดเกาะตัวอื่น)

ตัวอย่าง before/after ของแต่ละ technique ก็ tag register ของ **ตัวอย่าง** แยกต่างหาก (technique เป็น 🟦 CORE ได้ แม้ตัวอย่างจะเป็น 🟧 หรือ 🟪) — เพื่อไม่ให้ผู้อ่านเข้าใจผิดว่าเทคนิคนั้นใช้ได้เฉพาะ register เดียว

**Version note:** เพิ่ม 6 เทคนิคจาก Wikipedia Signs of AI Writing (T13-18) — ครอบคลุม patterns ที่ V01 catalog ขาดไป. รายละเอียด 24 Wikipedia patterns + Severity Triage อยู่ใน `07_wikipedia_24_patterns.md`

---

## Table of Techniques

Column **Reg.** = register ของ **กลไก** (🟦 = ทุก register). Pass/Layer map เป็น contract — ห้ามเปลี่ยน

| # | Technique | Reg. | Pass / Layer | Example |
|---|---|---|---|---|
| 1 | Personal Anchor Injection | 🟦 | Pass 2 / Layer 3 Check 8 | ใส่ชื่อจริง ตัวเลขจริง |
| 2 | Burstiness Injection | 🟦 | Pass 1.2 / Layer 2 Check 1 | สลับยาว-สั้น |
| 3 | Sentence Opening Diversification | 🟦 | Pass 1.3 / Layer 2 Check 2 | 5 รูปแบบ |
| 4 | Tier 1 Vocabulary Detoxification | 🟦 | Pass 2.1 / Layer 1 | ลบคำ Tier 1 |
| 5 | List Asymmetry | 🟦 | Pass 1.4 / Layer 2 Check 5 | 3 ข้อ → 2/4/5 |
| 6 | Voice Particularization | 🟦 | Pass 2.2 / Layer 3 Check 8 | ตาม Voice Profile |
| 7 | Counterargument Insertion | 🟩 | Layer 3 Check 8 + Adv C | เพิ่มข้อโต้แย้ง |
| 8 | Citation Specification | 🟩 | Pass 2.4 / Layer 3 Check 7 | ระบุ DOI/หน้า |
| 9 | Idiom and Register Shift | 🟦 | Pass 2.2 + Thai-Specific | ปรับสำนวน |
| 10 | Asymmetric Information Density | 🟦 | Pass 1.4 / Layer 3 Check 6 | ย่อหน้าหนัก/เบา |
| 11 | Question Embedding | 🟦 | Pass 1.3 / Layer 2 Check 2 | คำถามวาทศิลป์ 1/500 คำ |
| 12 | Cultural and Temporal Specificity | 🟦 | Pass 2.4 + Adv B | ระบุปี เหตุการณ์ |
| 13 | Inflated Symbolism Removal | 🟦 | Pass 2 + Wikipedia Pattern 1 | ลบประโยคขยายความสำคัญ |
| 14 | Superficial -ing Analysis Removal | 🟦 | Pass 2 + Wikipedia Pattern 3 | ลบ -ing phrase ไร้สาระ |
| 15 | Negative Parallelism Removal | 🟦 | Pass 2 + Wikipedia Pattern 9 | "not just X, it's Y" → ตรง |
| 16 | Copula Restoration | 🟦 | Pass 2 + Wikipedia Pattern 8 | "serves as" → "is" |
| 17 | Chatbot Artifact Removal | 🟦 | Pass 2 + Wikipedia Pattern 19-21 | ลบ preamble/CTA |
| 18 | Soul Injection | 🟩 | จาก `08_personality_and_soul.md` | เติมเสียงผู้เขียน |

---

## Detailed Examples

### Technique 1: Personal Anchor Injection — 🟦 CORE

**Method:** เพิ่มชื่อจริง วันที่จริง สถานที่จริง ตัวเลขจริง หรือเรื่องเล่าส่วนตัว

> กลไกนี้ใช้ได้ทุก register — academic ผูกกับ field/site/dataset จริง, business ผูกกับลูกค้า/man-day/module จริง, general ผูกกับเหตุการณ์/วันที่จริง. ตัวอย่างด้านล่างเป็น 🟧 **Business**

*Before:* "Companies that invest in digital transformation typically see significant improvements in operational efficiency."

*After (🟧 Business):* "When Bangchak Corporation rolled out Oracle Cloud ERP in Q2 2024, monthly close time fell from 11 working days to 4."

### Technique 2: Burstiness Injection — 🟦 CORE

**Method:** สลับประโยคยาว (25+ คำ) กับประโยคสั้น (3-7 คำ)

*Before:* "The implementation of artificial intelligence in customer service has produced measurable improvements in response time, customer satisfaction, and overall operational efficiency, leading to higher retention rates and increased revenue."

*After (🟧 Business):* "AI changed our customer service. Response time fell from 14 minutes to 90 seconds, and CSAT climbed eight points in a single quarter. But the real win was retention: customers who once churned at 22% annually now leave at 9%."

### Technique 3: Sentence Opening Diversification — 🟦 CORE

**Method:** สลับ 5 รูปแบบ (Adverb / Subordinate / Question / Quote / Prepositional)

### Technique 4: Tier 1 Vocabulary Detoxification — 🟦 CORE

**Method:** ใช้รายการใน `06_verified_ai_signatures.md` แทนคำ Tier 1

### Technique 5: List Asymmetry — 🟦 CORE

**Method:** เปลี่ยนรายการ 3 ข้อสมมาตรเป็น 2, 4, หรือ 5 ข้อ ที่ความยาวต่างกัน

### Technique 6: Voice Particularization — 🟦 CORE

**Method:** เลือกคำตาม Voice Profile (Dimension 2 — Vocabulary Signature)

### Technique 7: Counterargument Insertion — 🟩 Academic

**Method:** แทรกย่อหน้าที่ยอมรับข้อจำกัด (กลไก scholarly — ผูกกับ academic register)

> ตัวอย่างด้านล่างเป็น 🟧 **Business** (procurement decision) — แสดงว่ากลไกนี้ย้ายไป business ได้ แต่ home register คือ academic

*Example (🟧 Business):* "There is a counterview worth taking seriously: that organizations adopting AI procurement tools too early end up locked into vendor architectures before the market has matured. We acknowledge the risk, but argue that the cost of waiting another 18 months exceeds the cost of switching."

### Technique 8: Citation Specification — 🟩 Academic

**Method:** ระบุ author/year/page

*Before:* "Research has shown that organizational change initiatives fail at high rates."

*After (🟩 Academic):* "Beer and Nohria's 2000 Harvard Business Review study put the failure rate of organizational change programs at 70%."

### Technique 9: Idiom and Register Shift — 🟦 CORE

**Method:** ใช้สำนวนตาม Voice Profile — เลี่ยงคำตลาดในงานวิชาการ, เลี่ยงสำนวนวิชาการในงาน business (กลไกปรับ register ใช้ได้ทุกทาง)

### Technique 10: Asymmetric Information Density — 🟦 CORE

**Method:** ย่อหน้าหนึ่งลึก ย่อหน้าถัดไปสั้นเป็นข้อสังเกต

### Technique 11: Question Embedding — 🟦 CORE

**Method:** แทรกคำถามวาทศิลป์ 1 ครั้งต่อ 500 คำ (ไม่เกิน)

### Technique 12: Cultural and Temporal Specificity — 🟦 CORE

**Method:** ระบุช่วงเวลา ฤดูกาล เหตุการณ์ปัจจุบัน บริบทวัฒนธรรม

---

## Wikipedia-Derived Techniques (T13-18)

> T13-18 มาจาก Wikipedia Signs of AI Writing — กลไกลบ AI-tell ที่ทำงานได้ทุก register (🟦 CORE). ตัวอย่างหลายตัวเป็นเนื้อหา encyclopedic ซึ่ง tag เป็น 🟪 **General** เพื่อบอกว่าตัวอย่างมาจาก register ใด — ไม่ได้แปลว่าเทคนิคใช้ได้เฉพาะ general

### Technique 13: Inflated Symbolism Removal — 🟦 CORE (Wikipedia Pattern 1)

**Method:** ลบประโยคที่ "ขยายความสำคัญ" โดยไม่เพิ่มข้อมูลจริง

> ตัวอย่างด้านล่างเป็น 🟪 **General** (เนื้อหา encyclopedic)

*Before (🟪 General):* "การก่อตั้งสถาบันสถิติแห่งคาตาโลเนียในปี 1989 เป็นจุดเปลี่ยนสำคัญในวิวัฒนาการสถิติภูมิภาคของสเปน สะท้อนการเคลื่อนไหวที่กว้างขวางในการกระจายอำนาจ"

*After (🟪 General):* "สถาบันสถิติแห่งคาตาโลเนียก่อตั้งในปี 1989 เพื่อเก็บและเผยแพร่สถิติภูมิภาค แยกจากสำนักสถิติแห่งชาติของสเปน"

### Technique 14: Superficial -ing Analysis Removal — 🟦 CORE (Wikipedia Pattern 3)

**Method:** ลบ "-ing phrases" ที่ตามท้ายประโยคแบบไม่เพิ่มสาระ

> ตัวอย่างด้านล่างเป็น 🟪 **General** (เนื้อหา encyclopedic)

*Before (🟪 General):* "The temple uses blue, green, and gold, symbolizing Texas bluebonnets, the Gulf of Mexico, and Texan landscapes, reflecting the community's connection to the land."

*After (🟪 General):* "The temple uses blue, green, and gold colors. The architect chose these to reference local bluebonnets and the Gulf coast."

**Thai version (🟪 General):**
*Before:* "วัดใช้สีน้ำเงิน เขียว และทอง สะท้อนถึงธรรมชาติของท้องถิ่น ส่งเสริมให้เกิดความผูกพันกับชุมชน นำไปสู่การอนุรักษ์อย่างยั่งยืน"
*After:* "วัดใช้สีน้ำเงิน เขียว และทอง สถาปนิกระบุว่าเลือกเพราะตรงกับสีดอกบลูบอนเน็ตประจำท้องถิ่น"

### Technique 15: Negative Parallelism Removal — 🟦 CORE (Wikipedia Pattern 9)

**Method:** เปลี่ยน "It's not just X, it's Y" เป็นประโยคตรง

> ตัวอย่างด้านล่างเป็น 🟪 **General** (เนื้อหาทั่วไป)

*Before (🟪 General):* "It's not merely a song, it's a statement."
*After (🟪 General):* "The song carries a political message."

*Before (🟪 General, Thai):* "ไม่เพียงแค่นโยบาย แต่เป็นการเปลี่ยนแปลงทางความคิด"
*After (🟪 General, Thai):* "นโยบายนี้สะท้อนการเปลี่ยนแปลงทางความคิดของผู้กำหนดนโยบาย"

### Technique 16: Copula Restoration — 🟦 CORE (Wikipedia Pattern 8)

**Method:** เปลี่ยน "serves as / stands as / boasts" กลับเป็น "is / has"

> ตัวอย่างด้านล่างเป็น 🟪 **General** (เนื้อหา encyclopedic)

*Before (🟪 General):* "Gallery 825 serves as LAAA's exhibition space and boasts over 3,000 square feet."
*After (🟪 General):* "Gallery 825 is LAAA's exhibition space, totaling 3,000 square feet."

*Before (🟪 General, Thai):* "องค์กรนี้เป็นเครื่องหมายแห่งความก้าวหน้าของวงการ"
*After (🟪 General, Thai):* "องค์กรนี้เป็นองค์กรชั้นนำของวงการ"

### Technique 17: Chatbot Artifact Removal — 🟦 CORE (Wikipedia Pattern 19-21)

**Method:** ลบทุกอย่างที่บ่งบอกว่ามาจาก chatbot conversation — รายละเอียดใน `09_filler_replacement_table.md` Section 5-7

> Section 5-7 ใน `09` เป็น contract (hard-link) — ห้ามเปลี่ยนเลข. ตัวอย่างด้านล่างเป็น 🟪 **General**

*Before (🟪 General):* "Here is an overview of the French Revolution. I hope this helps! Let me know if you'd like me to expand."
*After (🟪 General):* "The French Revolution began in 1789 when financial crisis and food shortages led to widespread unrest."

### Technique 18: Soul Injection — 🟩 Academic (จาก `08_personality_and_soul.md`)

**Method:** เติมเสียงผู้เขียน — ความเห็น, การยอมรับความซับซ้อน, การใช้ "ผู้วิจัย" ตรง ๆ, การยอมรับข้อจำกัด

> home register = academic (ผูกกับเสียง "ผู้วิจัย" + peer reviewer). ดูรายละเอียด 6 sub-techniques (S1-S6) ใน `08_personality_and_soul.md`

**Trigger:** ใช้เมื่อข้อความผ่าน Pass 1+2 แล้วแต่ "อ่านยังไม่มีตัวตน" หรือ peer reviewer feedback ว่า "ฟังเหมือน AI"

---

## Anti-Patterns to Avoid (🟦 CORE — ทุก register)

**Don't:**
- จงใจสะกดผิด — Turnitin 2026 จับได้
- แทนคำด้วย thesaurus แบบสุ่ม (Symptom Substitution)
- ใช้ humanizer tool อัตโนมัติ
- เพิ่ม filler เพื่อหลอก burstiness
- รัน Pass 1 และ Pass 2 พร้อมกัน
- เขียนโดยไม่อ้าง Voice Profile
- **เติม fake personality ด้วย Soul Injection** — ห้ามคิดความเห็นที่ผู้เขียนไม่ได้คิด
- **เติม fake counterargument** — ห้ามสร้าง "บางคนแย้งว่า..." ลอย ๆ

---

## CHANGELOG
- **V06R01 (2026.06.13)** — RE-LABEL เป็น 🟦 CORE catalog (register-agnostic, ไม่มี academic default). Tag ทั้ง 18 technique: 🟦 CORE = T1-6, T9-17 (กลไก register-agnostic) · 🟩 Academic = T7 (counterargument), T8 (citation), T18 (soul) · ไม่มี technique ใดเป็น 🟧/🟪 home แต่ tag **ตัวอย่าง** แยก — ย้ายตัวอย่าง business (T1/T2/T7) เป็น 🟧, ตัวอย่าง encyclopedic (T13-17) เป็น 🟪. เพิ่ม Reg. column ใน Table of Techniques + เติม T13-18 ครบในตาราง (เดิมมีแต่ T1-12). คง 18 names + Anti-Patterns 8 + Pass/Layer map (contract — ไม่เปลี่ยน) + `09` Section 5-7 hard-link (ไม่เปลี่ยนเลข) ครบ.
