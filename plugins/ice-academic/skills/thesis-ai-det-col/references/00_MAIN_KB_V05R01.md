# AI Detection and AI Correction — Comprehensive Knowledge Base

**Document Title (TH):** ฐานความรู้ครอบคลุมเรื่องการตรวจจับและการแก้ไขเนื้อหาที่เขียนโดย AI พร้อม Voice/Writing Profile Extraction
**Version:** V05R01 (Major Update — supersedes V04R01)
**Date:** 2026-04-30
**Author:** Pichai (xpickey@gmail.com)
**Purpose:** Knowledge Base ต้นทางสำหรับสร้าง Custom Skill ด้าน AI Detection & AI Correction พร้อม Voice/Writing Profile Extraction
**Scope:** ครอบคลุม 4 บริบท — Academic, Business/Sales/Proposal, Government, Marketing/Content
**Languages:** Bilingual (Thai + English)

**🆕 Companion Knowledge Base:** [`KM-TH-THESIS-DOC V02R01`](../voice_profiles/KM-TH-THESIS-DOC/KM-TH-THESIS-DOC_V02R01_2026-04-30.md) — Voice Profile Library สำหรับงานวิชาการไทย (สกัดจาก corpus 101 ไฟล์)

**Major Changes from V04R01:**
- ✅ **ผนวก KM-TH-THESIS-DOC V02R01** เป็น Companion Knowledge Base — เพิ่ม Voice Profile Library สำหรับงานวิชาการไทย 7 Sub-Profiles
- ✅ **อัปเดต Section 8.2 (5-Level Source Hierarchy)** — Level 4 ตอนนี้มี Pre-defined Library ที่สกัดจาก corpus 101 ไฟล์
- ✅ **อัปเดต Section 4.1 (Tier 1 Vocabulary)** — แก้ไขความเข้าใจผิด: คำ "ขับเคลื่อน" "ยกระดับ" "อย่างยั่งยืน" **ไม่ใช่ AI signature ในภาษาไทย** (ตรวจพบใน corpus จริงสูงมาก)
- ✅ **เพิ่ม Section 8.6 (Verified AI Signature List)** — รายการคำที่เป็น AI signature จริงใน corpus 292K คำของไทยวิชาการ
- ✅ **อัปเดต Section 17 (Skill Architecture)** — voice_profiles/ folder ตอนนี้มี KM-TH-THESIS-DOC ครบ 7 Sub-Profiles
- ✅ **เพิ่ม Section 8.7 (Thai Academic Sub-Profiles)** — รายชื่อ 7 Sub-Profiles พร้อมขอบเขตการใช้งาน

**Major Changes from V03R01 (carried forward):**
- เพิ่ม Section 7 "8-Step Sequential Thinking Master Workflow"
- เพิ่ม Section 8 "Voice/Writing Profile Extraction Methodology"
- เพิ่ม Section 11 "Voice/Writing Match Scoring & Memory Storage"

---

## TABLE OF CONTENTS / สารบัญ

**Part 1 — Foundations / รากฐาน**
1. Executive Overview / ภาพรวมเชิงบริหาร
2. The Three Dimensions of AI Detection / สามมิติของการตรวจจับ AI

**Part 2 — The Detection Stack / ชุดเครื่องมือตรวจจับ**
3. AI Detection Tools Landscape (2026 Update)
4. The Three-Layer Detection Methodology
5. Thai-Specific Detection Patterns
6. AI Detection Self-Check Report Template

**Part 3 — The Voice & Correction Stack / ชุดสกัดเสียงและแก้ไข** ⭐ MAJOR EXPANSION
7. **The 8-Step Sequential Thinking Master Workflow** ⭐ NEW
8. **Voice/Writing Profile Extraction Methodology (6 Dimensions)** ⭐ NEW
9. AI Correction Protocol — Two-Pass Method
10. AI Correction Techniques Catalog (12 Techniques)
11. **Voice/Writing Match Scoring & Memory Storage** ⭐ NEW

**Part 4 — Application & Quality Assurance / การประยุกต์และประกันคุณภาพ**
12. Use Case Specific Guidance
13. Quality Assurance Checklist

**Part 5 — Governance / การกำกับดูแล**
14. Ethical Framework
15. Common Pitfalls & False Positives

**Part 6 — Operationalization / การปฏิบัติ**
16. Prompt Templates for Detection, Voice Extraction & Correction
17. Skill Design Implications
18. Glossary
19. References & Further Reading

---

# PART 1 — FOUNDATIONS / รากฐาน

## 1. EXECUTIVE OVERVIEW / ภาพรวมเชิงบริหาร

### 1.1 Why This Knowledge Base Matters / เหตุใดเรื่องนี้จึงสำคัญ

**English:**
The widespread adoption of generative AI (ChatGPT, Claude, Gemini, Copilot, and others) has fundamentally changed how knowledge workers, students, marketers, and government officials produce written content. In response, institutions have deployed AI detection systems — Turnitin AI, GPTZero, Originality.ai, Copyleaks, Winston AI, ZeroGPT, Sapling, and others — to flag machine-generated text. As of 2026, detection has matured into a layered discipline: Turnitin's January 2026 update introduced a dedicated detection layer for "humanizer bypass" tools, the EU AI Act takes full effect in August 2026 requiring AI-generated content labeling, and Thailand's draft AI legislation (in public consultation through ETDA) is following the EU's risk-based classification model. The discipline of **AI Detection** (knowing what these tools look for), **Voice/Writing Profile Extraction** (knowing what authentic human writing looks like for a specific author), and **AI Correction** (rewriting AI-generated drafts to read as authentic, human-authored prose that matches the author's true voice) has therefore become an essential professional capability.

**ภาษาไทย:**
การใช้ AI สร้างเนื้อหาอย่างกว้างขวางได้เปลี่ยนวิธีที่บุคลากรความรู้ผลิตงานเขียนอย่างมีนัยสำคัญ องค์กรต่าง ๆ จึงนำระบบตรวจจับ AI มาใช้ ในปี 2569 (2026) การตรวจจับได้พัฒนาเป็นระเบียบวิธีหลายชั้น โดย Turnitin ออกอัปเดตเดือนมกราคม 2569 เพิ่มชั้นตรวจจับ "humanizer bypass" EU AI Act มีผลบังคับใช้ในเดือนสิงหาคม 2569 และร่างกฎหมาย AI ของไทยก็ดำเนินตามแบบ EU **ทักษะที่จำเป็น 3 อย่างคือ การตรวจจับ AI (AI Detection), การสกัดเสียงและสไตล์ผู้เขียน (Voice/Writing Profile Extraction), และการแก้ไขเนื้อหาให้ตรงกับเสียงผู้เขียน (AI Correction)**

### 1.2 Three Disciplines, One Goal / สามทักษะ หนึ่งเป้าหมาย

| มิติ | AI Detection / การตรวจจับ | Voice Profile Extraction / การสกัดเสียง | AI Correction / การแก้ไข |
|---|---|---|---|
| คำถามหลัก | "ข้อความนี้จะถูกตรวจจับว่า AI หรือไม่?" | "เสียงผู้เขียนแท้ ๆ คืออย่างไร?" | "จะเขียนใหม่ให้ตรงเสียงผู้เขียนได้อย่างไร?" |
| ผลลัพธ์ | Risk score, flagged passages | Voice Profile ใน 6 มิติ | ข้อความที่ humanize แล้วและตรงเสียงผู้เขียน |
| ทักษะ | Pattern recognition, สถิติ | Stylometric analysis | Voice matching, rewriting |
| เครื่องมือ | Detector platforms | Reference corpus + 6-dimension extractor | Two-Pass Method + 12 Techniques Catalog |

### 1.3 The Core Principle / หลักการสำคัญ

> **English:** *AI Correction is not deception — it is the process of restoring the author's authentic voice (extracted as a Voice/Writing Profile) to a draft that AI helped generate, ensuring the final work genuinely reflects the author's thinking, judgment, evidence, and stylistic fingerprint.*
>
> **ภาษาไทย:** *การแก้ไขเนื้อหา AI ไม่ใช่การหลอกลวง แต่คือกระบวนการคืนเสียงผู้เขียนที่แท้จริง (สกัดเป็น Voice/Writing Profile) ให้แก่ฉบับร่างที่ AI ช่วยสร้าง เพื่อให้ผลงานสุดท้ายสะท้อนความคิด วิจารณญาณ หลักฐาน และลายนิ้วมือสไตล์ของผู้เขียนอย่างแท้จริง*

This principle elevates the discipline beyond detector evasion. The objective is **Voice Authenticity Restoration**, not surface-level "AI score reduction."

---

## 2. THE THREE DIMENSIONS OF AI DETECTION / สามมิติของการตรวจจับ AI

ระบบตรวจจับ AI ในปี 2569 (2026) ทุกระบบทำงานบนสามมิติหลัก ความเข้าใจมิติทั้งสามคือรากฐานของทั้งการตรวจจับและการแก้ไข

### 2.1 Dimension 1 — Statistical Patterns / มิติเชิงสถิติ

**A. Perplexity / ความซับซ้อนเชิงภาษา**
- Definition: การวัดความคาดเดาได้ของแต่ละคำในข้อความ — AI มักให้ผลลัพธ์ที่มี **low perplexity** (เลือกคำที่น่าจะเป็น) ส่วนมนุษย์มี perplexity สูงกว่า
- Human writing has higher perplexity due to unexpected word choices, idiosyncratic phrasings, and surprising connectives.

**B. Burstiness / ความผันผวนของจังหวะประโยค**
- Definition: การกระจายความยาวและความซับซ้อนของประโยค — มนุษย์สลับประโยคสั้นกับยาว (high burstiness) AI มักผลิตประโยคความยาวใกล้เคียงกัน (low burstiness)

> **2026 Note:** Anthropic's Claude models naturally produce text with higher burstiness than GPT models — Turnitin's January 2026 update improved Claude detection by ~12%.

### 2.2 Dimension 2 — Linguistic Patterns / มิติเชิงภาษา

ตรวจวัดลักษณะเชิงคุณภาพของคำและสำนวน:
- **Vocabulary** — Tier 1 AI words (ดูภาค 4.1)
- **Phrasing** — แม่แบบที่ AI ผลิตซ้ำ
- **Hedging** — สำนวนเลี่ยง
- **Translationese** — ภาษาไทยที่แปลตรงตัวจากอังกฤษ

### 2.3 Dimension 3 — Structural Patterns / มิติเชิงโครงสร้าง

ตรวจวัดสถาปัตยกรรมเอกสาร:
- **Paragraph Architecture** — AI ชอบย่อหน้าความยาวเท่ากัน
- **List Symmetry** — รายการสามข้อสมมาตร
- **Heading Density** — H2/H3 มากเกินจริง
- **Citation Distribution** — Cluster citations
- **Conclusion Recap** — ปิด section ด้วยสรุปซ้ำ

### 2.4 Why All Three Matter Together

การ humanize ที่ได้ผลต้องแก้ทั้งสามมิติ — แต่ **ต้องแก้ทีละมิติ ไม่พร้อมกัน** (เหตุผลในภาค 9.1: Two-Pass Method)

นอกจากสามมิติ Detection ของ "AI vs Human" แล้ว ยังต้องเสริมด้วย **มิติที่สี่ที่ V04R01 เน้น คือ "Voice Match"** — ข้อความไม่เพียงต้อง "ไม่ใช่ AI" แต่ต้อง "เป็นเสียงผู้เขียนแท้ ๆ" ด้วย (รายละเอียดในภาค 7-8 และ 11)

---

# PART 2 — THE DETECTION STACK / ชุดเครื่องมือตรวจจับ

## 3. AI DETECTION TOOLS LANDSCAPE (2026 UPDATE) / ภาพรวมเครื่องมือ

### 3.1 Tools by Primary Use Case / เครื่องมือจำแนกตามบริบท

#### A. For Academic Use / สำหรับงานวิชาการ

**Turnitin AI Writing Detection**
- มาตรฐานของมหาวิทยาลัยและวารสารทั่วโลก คะแนน 0–100% ทำงานควบคู่ plagiarism check
- **2026 Update:** เพิ่ม "AI Bypasser Detection Layer" (มกราคม 2569) ตรวจจับลายนิ้วมือของ humanizer
- **Claimed accuracy:** 98% สำหรับเอกสารที่มี AI content ≥ 20% และ false positive rate < 1% สำหรับงาน ≥ 300 คำ
- **ข้อจำกัด:** ตกลงเหลือ 60–85% เมื่อข้อความผ่านการแก้ด้วยมืออย่างจริงจัง

**Originality.ai** — เน้น content marketing และวารสาร แม่นยำสูงในภาษาอังกฤษ รองรับ 15+ ภาษา

**Copyleaks AI Content Detector** — รองรับ **30+ ภาษา (รวมไทย)** — เหมาะที่สุดสำหรับงานไทยและการตรวจสอบข้ามภาษา

**iThenticate** — สำหรับวารสารระดับนานาชาติและงานวิจัย Pre-publication

#### B. For Business / Marketing / Content

- **GPTZero** — perplexity + burstiness เป็นหลัก, อ้าง 99.3% accuracy
- **Winston AI** — content marketing, API integration, AI image detection
- **ZeroGPT** — ฟรี/freemium, WhatsApp/Telegram bot
- **Sapling AI Detector** — B2B SaaS, รองรับ DeepSeek

#### C. For Government / Legal

- **Turnitin** สำหรับเอกสารราชการที่อิงระเบียบวิชาการ
- **Originality.ai** สำหรับเอกสารนโยบายภาษาอังกฤษ
- **Copyleaks** สำหรับเอกสารราชการไทย

**ระบบกำลังพัฒนาของหน่วยงานราชการ — บริบท 2026:**
- **EU AI Act (สิงหาคม 2569):** บังคับให้ AI-generated content ระบุได้ machine-readable + ฉลากที่ผู้อ่านมองเห็นสำหรับ deepfake และ public-interest text
- **Watermarking:** ผู้พัฒนาโมเดลเริ่มใส่ watermark เชิงสถิติ
- **ประเทศไทย:** ETDA จัดรับฟังความเห็น Draft Principles for AI Legislation พ.ค.–มิ.ย. 2568 ใช้ระบบจำแนกความเสี่ยงแบบ EU

### 3.2 Score Interpretation / การตีความคะแนน

| Score | Meaning | Action |
|---|---|---|
| 0–20% | Low AI signature | ผ่าน — ส่งงานได้ |
| 21–40% | Moderate signal | Pass 1 อย่างเดียวก็พอ |
| 41–60% | Significant AI signal | Pass 1 + Pass 2 ครบ |
| 61–80% | High AI signature | Two-Pass + Advanced Techniques |
| 81–100% | Almost certainly AI | Full rewrite — เริ่มใหม่จาก Step 1 ของ 8-Step (ภาค 7) |

### 3.3 Universal Limitations

- ผลคะแนนเป็นความน่าจะเป็น **ไม่ใช่หลักฐานเด็ดขาด**
- false positive โดยเฉพาะในงานเขียนของผู้ใช้ภาษาอังกฤษเป็นภาษาที่สอง
- ความแม่นยำตกในข้อความสั้น (< 250–300 คำ)
- มี lag ราว 1–3 เดือนหลัง release model ใหม่
- เครื่องมือต่างยี่ห้อให้คะแนนต่างกัน → อ้างอิงเครื่องมือที่สถาบันกำหนด

### 3.4 The Cat-and-Mouse Reality

อัลกอริทึมและโมเดลพัฒนาควบคู่กัน — Turnitin AI Bypasser Detection ทำให้ humanizer tools ที่เคยใช้ได้หมดประสิทธิภาพในทันที **แนวทางที่ยั่งยืนคือการเขียนปรับด้วยมือตาม 8-Step Master Workflow และ Two-Pass Method โดยมี Voice Profile เป็นจุดยึด**

---

## 4. THE THREE-LAYER DETECTION METHODOLOGY / ระเบียบวิธีตรวจจับ 3 ชั้น

### 4.1 LAYER 1 — AI Vocabulary Footprints Check / ชั้นตรวจคำศัพท์

#### 🔴 Tier 1: คำที่ AI Detector จับได้ทันที (ห้ามใช้เด็ดขาด)

#### 4.1.1 English Vocabulary Tier 1

**Verbs:**

| AI ใช้ | คำแทนที่ |
|---|---|
| delve / delve into | examine / look at / study |
| underscore | emphasize / highlight |
| leverage | use / apply |
| utilize | use |
| harness | use / apply |
| streamline | simplify / improve |
| foster | support / build |
| navigate | manage / handle |
| unveil | reveal / show |
| showcase | show / present |
| embark | begin / start |
| embrace | accept / adopt |
| resonate | connect / appeal |
| elevate | raise / improve |

**Adjectives:**

| AI ใช้ | คำแทนที่ |
|---|---|
| pivotal | important / key / central |
| robust | strong / reliable |
| comprehensive | thorough / complete |
| multifaceted | complex / many-sided |
| intricate | complex / detailed |
| seamless | smooth |
| cutting-edge | advanced / new |
| innovative | new / creative |
| meticulous | careful / detailed |
| nuanced | subtle / detailed |
| holistic | whole / overall |
| dynamic | active / changing |
| bespoke | custom / tailored |

**Nouns:**

| AI ใช้ | คำแทนที่ |
|---|---|
| landscape | field / area |
| realm | area / domain |
| tapestry | mix / combination |
| symphony | combination |
| testament | proof / evidence |
| synergy | cooperation |
| paradigm | model / framework |
| framework (overuse) | structure / approach |
| ecosystem (overuse) | environment / network |

**Phrases:**

| AI ใช้ | วลีแทนที่ |
|---|---|
| "It's important to note that..." | ตัดทิ้ง / "Note that..." |
| "It's important to remember that..." | ตัดทิ้ง |
| "In today's fast-paced world..." | ระบุปี / ตัดทิ้ง |
| "In the realm of..." | "In [field]..." |
| "Delving into the intricacies of..." | "Examining..." |
| "Navigating the complexities of..." | "Managing..." |
| "A testament to..." | "Proves..." |
| "Embark on a journey..." | "Begin..." |
| "Stands as a testament to..." | "Proves..." |
| "Plays a crucial role in..." | "Drives..." / "Controls..." |
| "In the ever-evolving landscape of..." | ระบุช่วงเวลา / ตัดทิ้ง |

#### 4.1.2 Thai Vocabulary Tier 1

**คำเปิดประโยคที่ AI ใช้บ่อย:**

| AI ใช้ | วิธีแก้ |
|---|---|
| "ในยุคปัจจุบัน" | "ในปัจจุบัน" / ระบุปี |
| "เป็นที่ทราบกันดีว่า" | ตัดทิ้ง |
| "ปฏิเสธไม่ได้ว่า" | ตัดทิ้ง |
| "นับเป็นสิ่งสำคัญที่..." | ตัดทิ้ง |
| "ดังที่กล่าวมาข้างต้น" | ตัดทิ้ง / "ดังนั้น" |
| "อย่างที่เราทราบกันดี" | ตัดทิ้ง |
| "ในโลกที่..." | ตัดทิ้ง |
| "ท่ามกลางการเปลี่ยนแปลง..." | ระบุการเปลี่ยนแปลงเฉพาะ |
| "ในยุคที่ … กำลังพัฒนาอย่างรวดเร็ว" | ระบุช่วงเวลา / ตัดทิ้ง |
| "ในบริบทดังกล่าว" | "กรณีนี้" |

**คำขยายที่ใช้พร่ำเพรื่อ:**

| AI ใช้ | วิธีแก้ |
|---|---|
| "อย่างมีนัยสำคัญ" | ระบุนัยอะไร / ตัวเลข |
| "อย่างชัดเจน" | แสดงหลักฐานแทน |
| "ครอบคลุม" | ระบุขอบเขตเฉพาะ |
| "หลากหลาย" | ระบุประเภทเฉพาะ |
| "หลายมิติ" | ระบุมิติเฉพาะ |
| "อย่างยั่งยืน" | ระบุระยะเวลา |
| "อย่างเป็นระบบ" | ระบุระบบที่ใช้ |
| "อย่างมีประสิทธิภาพ" | ระบุที่วัดได้ |
| "อันสำคัญยิ่ง" | "สำคัญ" |
| "อย่างลึกซึ้ง" | ระบุประเด็น |
| "อย่างพิถีพิถัน" | "อย่างละเอียด" |
| "อย่างบูรณาการ" | ระบุการบูรณาการเฉพาะ |

**คำเชื่อมที่ AI ใช้ซ้ำ:**

| AI ใช้ | วิธีแก้ |
|---|---|
| "นอกจากนี้" | สลับกับ "อีกประเด็นหนึ่ง" / ตัดทิ้ง |
| "อีกทั้ง" | สลับกับคำอื่น |
| "ยิ่งไปกว่านั้น" | "นอกจากนั้น" / ตัดทิ้ง |
| "ในขณะเดียวกัน" | "พร้อมกันนั้น" |
| "อย่างไรก็ตาม" | "แต่กระนั้น" / "หากแต่" |
| "ดังนั้น" | "จึง" / "เช่นนั้น" |
| "กล่าวโดยสรุป" | "สรุปแล้ว" / ตัดทิ้ง |
| "ในท้ายที่สุด" | "สุดท้าย" / ตัดทิ้ง |

**Hedging ที่ AI ใช้ซ้ำ:**

| AI ใช้ | วิธีแก้ |
|---|---|
| "อาจกล่าวได้ว่า" | ภาษามั่นใจ / ตัดทิ้ง |
| "อาจถือได้ว่า" | "ถือว่า" |
| "อาจพิจารณาได้ว่า" | "พิจารณาว่า" |
| "ในแง่หนึ่ง" | ระบุแง่ไหน |
| "ในบางกรณี" | ระบุกรณีเฉพาะ |
| "เป็นที่น่าสังเกตว่า" | ตัดทิ้ง |

#### 4.1.3 Tier 1 Pass Criteria

| ระดับเอกสาร | จำนวน Tier 1 ที่ยอมรับ |
|---|---|
| งานวิชาการระดับวารสารนานาชาติ | ≤ 2 ครั้ง / 1,000 คำ |
| งานวิชาการระดับวารสารไทย | ≤ 4 ครั้ง / 1,000 คำ |
| Business proposal / Executive | ≤ 3 ครั้ง / 1,000 คำ |
| งานราชการ | ≤ 2 ครั้ง / 1,000 คำ |
| Marketing content | ≤ 5 ครั้ง / 1,000 คำ |

#### 4.1.4 ⚠️ V05R01 CORRECTION — Verified Tier 1 Vocabulary จาก Real Thai Corpus

**สำคัญ:** การวิเคราะห์ corpus 101 ไฟล์งานวิจัยไทย (~292,000 คำ) ใน [`KM-TH-THESIS-DOC V02R01`](../voice_profiles/KM-TH-THESIS-DOC/KM-TH-THESIS-DOC_V02R01_2026-04-30.md) **แก้ไขความเข้าใจผิดเรื่องคำต้องห้ามภาษาไทย** ดังนี้:

**🟢 คำที่เคยจัดเป็น Tier 1 แต่ใช้ได้จริงในไทย (REMOVED จาก Tier 1):**

| คำ | จำนวนครั้งใน corpus 292K | Verdict V05R01 |
|---|---|---|
| ขับเคลื่อน | 272 ครั้ง / 62 ไฟล์ | ✅ ใช้ได้ — ไม่ใช่ AI signature ในไทย |
| ยกระดับ | 133 ครั้ง / 43 ไฟล์ | ✅ ใช้ได้ |
| อย่างยั่งยืน | 68 ครั้ง / 32 ไฟล์ | ✅ ใช้ได้ (ระบุระยะเวลาเฉพาะดีกว่า) |
| อย่างมีประสิทธิภาพ | 195 ครั้ง / 55 ไฟล์ | ✅ ใช้แพร่หลาย |
| อย่างเป็นระบบ | 59 ครั้ง / 33 ไฟล์ | ✅ ใช้ได้ |
| หลากหลาย | 179 ครั้ง / 55 ไฟล์ | ✅ ใช้ได้ |
| บูรณาการ | 432 ครั้ง / 59 ไฟล์ | ✅ ใช้แพร่หลายมาก |

**🔴 คำที่ Verified ว่าเป็น AI Signature จริง (ปรากฏ ≤ 5 ครั้งใน corpus 292K คำ):**

| คำ | จำนวนครั้ง | คำแทนที่ |
|---|---|---|
| **เป็นที่ทราบกันดีว่า** | 0 | ตัดทิ้ง |
| **นับเป็นสิ่งสำคัญ** | 0 | ตัดทิ้ง |
| **ในแง่หนึ่ง** | 0 | ระบุแง่ไหน |
| **อาจถือได้ว่า** | 0 | "ถือว่า" |
| **ดังที่กล่าวไว้ข้างต้น** | 0 | "ดังนั้น" / ตัดทิ้ง |
| **อย่างพิถีพิถัน** | 0 | "อย่างละเอียด" |
| **ยิ่งไปกว่านั้น** | 1 | "นอกจากนั้น" |
| **อาจกล่าวได้ว่า** | 1 | ตัดทิ้ง |
| **ในเวลาเดียวกัน** | 1 | "ในขณะเดียวกัน" |
| **ในท้ายที่สุด** | 1 | "ท้ายที่สุด" |
| **กล่าวโดยสรุป** | 2 | "สรุปว่า" |
| **ปฏิเสธไม่ได้ว่า** | 3 | ตัดทิ้ง |

**กฎใหม่ V05R01:**
- เมื่อทำ Pass 2 (Vocabulary Correction) สำหรับงานเขียนวิชาการไทย ใช้รายการ Verified AI Signature นี้เป็นหลัก
- คำในรายการสีเขียวยังเป็น "ใช้ได้" ตราบเท่าที่ density ไม่เกิน Pass Criteria ในตาราง 4.1.3
- รายละเอียดเพิ่มเติม โดยเฉพาะ Sub-Profile เฉพาะสาขา ดูใน [`KM-TH-THESIS-DOC V02R01`](../voice_profiles/KM-TH-THESIS-DOC/KM-TH-THESIS-DOC_V02R01_2026-04-30.md) Part 4

### 4.2 LAYER 2 — Statistical Pattern Check / ชั้นตรวจสถิติ

ชั้นนี้วัดมิติเชิงปริมาณ มี 5 Check:

#### ✅ Check 1: Burstiness — Sentence Length Variability

**วิธีตรวจ:**
1. นับจำนวนคำของแต่ละประโยค
2. ตรวจ 5 ประโยคติดต่อกัน — หากมีมากกว่า 3 ประโยคที่ยาว 16–22 คำ → **เสี่ยงสูง**
3. คำนวณ SD ของความยาวประโยค

**เกณฑ์ผ่าน:**
- SD ≥ 5
- มีประโยคสั้น (5–12 คำ) ≥ 1 ต่อย่อหน้า
- มีประโยคยาว (25–35+ คำ) ≥ 1 ต่อย่อหน้า

#### ✅ Check 2: Sentence Opening Variability

**❌ AI Pattern:** ทุกประโยคเริ่มด้วยประธาน + กริยา
**✅ Human Pattern:** สลับด้วย adverb / subordinate clause / question / quote / prepositional phrase

**เกณฑ์ผ่าน:** ใน 10 ประโยคติดต่อกัน อย่างน้อย 3 ต้องไม่ใช่ประธาน-กริยา

#### ✅ Check 3: Paragraph Symmetry

**เกณฑ์ผ่าน:** ในเอกสาร 1,500 คำ มีความยาวย่อหน้าอย่างน้อย 3 ขนาด (สั้น/กลาง/ยาว)

#### ✅ Check 4: Transition Phrase Density

**เกณฑ์ผ่าน:** ≤ 3 คำเชื่อมต่อ 500 คำ

#### ✅ Check 5: Bullet-Point Thinking in Prose

**❌ AI Pattern:** "มี 3 ประการ ได้แก่… ปัจจัยที่หนึ่ง… ปัจจัยที่สอง…"
**✅ Human Pattern:** เขียนเป็นความเรียงต่อเนื่อง

### 4.3 LAYER 3 — Structural Pattern Check / ชั้นตรวจโครงสร้าง

#### ✅ Check 6: Paragraph Length Variability

**เกณฑ์ผ่าน:** ความยาวย่อหน้าในช่วง 3–12 ประโยค โดยมีย่อหน้าสั้น (2–3) อย่างน้อย 20% และย่อหน้ายาว (7+) อย่างน้อย 20%

#### ✅ Check 7: Citation Distribution

**เกณฑ์ผ่าน:** ไม่มี citation cluster ที่มี ≥ 4 citations ติดกัน (ยกเว้น literature review)

#### ✅ Check 8: Personal Voice Markers

**เครื่องหมายที่บ่งชี้เสียงผู้เขียน:**
- Specific names / numbers / dates
- Anecdotes
- Contextual asides
- Counterargument
- Legal/Regulatory anchors (เช่น "ตาม พ.ร.บ.การจัดซื้อจัดจ้าง พ.ศ. 2560 มาตรา 8")

**เกณฑ์ผ่าน:**
- < 1,000 คำ: ≥ 5 markers
- 1,000–3,000 คำ: ≥ 12 markers
- > 3,000 คำ: ≥ 1 marker ต่อ 200 คำ

---

## 5. THAI-SPECIFIC DETECTION PATTERNS / ลายนิ้วมือเฉพาะภาษาไทย

### 5.1 ปัญหาที่เกิดจากการแปลตรงตัว (Translationese)

**ก. การใช้ "การ" + คำกริยา มากเกินไป**
- AI: "การดำเนินการเพื่อการพัฒนาการบริการให้เกิดการยอมรับ"
- เขียนใหม่: "พัฒนาบริการให้ลูกค้ายอมรับ"

**ข. การใช้ passive voice ภาษาไทย**
- AI: "ระบบนี้ถูกออกแบบมาเพื่อจะถูกใช้งานโดย…"
- เขียนใหม่: "เราออกแบบระบบนี้สำหรับ…"

**ค. การวาง "ที่" ซ้อนกัน**
- AI: "องค์กรที่มีระบบที่ได้รับการรับรองที่สามารถบริหารจัดการ"
- เขียนใหม่: "องค์กรที่มีระบบรับรองมาตรฐานและบริหารจัดการได้"

**ง. การใช้ "ความ" + คำคุณศัพท์ มากเกินไป**

### 5.2 ปัญหาเฉพาะภาษาทางการของไทย (Government Thai)

- ใช้ "ตาม" แทน "อาศัยอำนาจตาม"
- ละเลยการระบุตำแหน่งและหน่วยงานเต็มยศ
- ใช้ภาษาตลาดในเอกสารทางการ ("เน้น" "ดัน" "ปลดล็อก")
- ขาดการอ้างระเบียบ/ประกาศ/หนังสือสั่งการ

### 5.3 ปัญหาเฉพาะภาษาวิชาการไทย

- ใช้ "เรา" แทน "ผู้วิจัย" / "คณะผู้วิจัย"
- "งานวิจัยพบว่า" แทน APA นาม-ปี
- ขาดศัพท์ราชบัณฑิตยสภา
- คำทับศัพท์ไม่ถูกต้อง

### 5.4 ลักษณะอื่นที่ Detector ภาษาไทยจับได้

- การใช้ em dash (—) แบบภาษาอังกฤษ (ไทยใช้น้อย)
- bold คำหลักทุกย่อหน้า
- เครื่องหมายวรรคตอนแบบฝรั่ง
- การวรรคไม่ตรงธรรมชาติของไทย

---

## 6. AI DETECTION SELF-CHECK REPORT TEMPLATE / แม่แบบรายงานผลตรวจ

```
═══════════════════════════════════════════════════════
🔍 AI DETECTION SELF-CHECK REPORT
═══════════════════════════════════════════════════════
วันที่ตรวจ:        [YYYY-MM-DD HH:MM]
ข้อความที่ตรวจ:    [ชื่อ/Section]
จำนวนคำ:           [X] คำ
ภาษา:              [Thai / English / Bilingual]
บริบท:             [Academic / Business / Government / Marketing]
Voice Profile ID:  [VP-...]   ← เพิ่มใหม่ใน V04R01
เกณฑ์เป้าหมาย:    AI Score < [X]%

─────────────────────────────────────────────────────
LAYER 1: AI VOCABULARY FOOTPRINTS
─────────────────────────────────────────────────────
Tier 1 Words ที่พบ:
- "[คำ]" ปรากฏ X ครั้ง → "[คำใหม่]"

Total Tier 1 Words:    [X]
Density (per 1,000 words): [X.X]
สถานะ Layer 1:         ☐ ผ่าน  ☐ ไม่ผ่าน

─────────────────────────────────────────────────────
LAYER 2: STATISTICAL PATTERNS
─────────────────────────────────────────────────────
Check 1: Burstiness (SD): [X.X]      ☐ ผ่าน  ☐ ไม่ผ่าน
Check 2: Sentence Opening             ☐ ผ่าน  ☐ ไม่ผ่าน
Check 3: Paragraph Symmetry           ☐ ผ่าน  ☐ ไม่ผ่าน
Check 4: Transition Density: [X]      ☐ ผ่าน  ☐ ไม่ผ่าน
Check 5: Bullet-Point Thinking        ☐ ผ่าน  ☐ ไม่ผ่าน

─────────────────────────────────────────────────────
LAYER 3: STRUCTURAL PATTERNS
─────────────────────────────────────────────────────
Check 6: Paragraph Length             ☐ ผ่าน  ☐ ไม่ผ่าน
Check 7: Citation Distribution        ☐ ผ่าน  ☐ ไม่ผ่าน
Check 8: Personal Voice Markers       ☐ ผ่าน  ☐ ไม่ผ่าน

═══════════════════════════════════════════════════════
📊 OVERALL AI DETECTION SCORE
═══════════════════════════════════════════════════════
Layer 1 (Vocabulary):  ☐ ผ่าน  ☐ ไม่ผ่าน
Layer 2 (Statistical): ☐ ผ่าน (X/5 checks)
Layer 3 (Structural):  ☐ ผ่าน (X/3 checks)
คะแนน AI ประมาณ:       [XX]%
สถานะรวม:             ☐ ผ่าน  ☐ ต้องแก้ไข

→ ถ้าไม่ผ่าน: ดำเนินการ Step 6 (AI Correction Two-Pass) ใน 8-Step (ภาค 7)
→ ถ้าผ่าน: ดำเนินการ Step 7 (Voice Match Scoring) (ภาค 11)
═══════════════════════════════════════════════════════
```

---

# PART 3 — THE VOICE & CORRECTION STACK / ชุดสกัดเสียงและแก้ไข

## 7. THE 8-STEP SEQUENTIAL THINKING MASTER WORKFLOW / ขั้นตอนปฏิบัติหลัก 8 ขั้น

### 7.1 Why This Master Workflow / เหตุใดจึงต้องมี Master Workflow

V01–V03 ของฐานความรู้นี้ใช้ "7-Phase Production Workflow" เป็นกระบวนการหลัก แต่ขาดมิติสำคัญหนึ่งคือ **Voice/Writing Profile** — เพราะการ humanize ที่ดีไม่ใช่แค่ "ลด AI score" แต่ต้อง **"ตรงเสียงผู้เขียน"** ด้วย

V04R01 จึงปรับเป็น **8-Step Sequential Thinking Master Workflow** ที่:
1. ทำให้ Voice Profile เป็นแกนของกระบวนการ
2. แบ่งขั้นตอนให้ชัดเจนเชิง Sequential Thinking (เหมาะกับ AI agent)
3. รวม Detection, Correction, และ Voice Matching เข้าเป็นวงจรเดียว
4. มีการบันทึกความจำ (Memory) เพื่อ reuse Voice Profile ในงานครั้งต่อไป

### 7.2 The 8 Steps Overview / ภาพรวม 8 ขั้นตอน

```
ขั้น 1: VOICE SOURCE SELECTION    → กำหนดประเภทงานและแหล่งอ้างอิง
ขั้น 2: VOICE/WRITING PROFILE EXTRACTION  → สกัด Profile ใน 6 มิติ
ขั้น 3: VOICE/WRITING CALIBRATION & MEMORY CREATION  → ปรับเทียบและบันทึก
ขั้น 4: WRITE FIRST DRAFT          → เขียนฉบับร่างโดยอ้าง KB เพื่อหลีก AI
ขั้น 5: AI DETECTION SELF-CHECK    → ตรวจ 3-Layer Self-Check
ขั้น 6: AI CORRECTION (Two-Pass)   → แก้ Rhythm + Vocabulary
ขั้น 7: VOICE/WRITING MATCH SCORING → ให้คะแนนความตรงเสียงผู้เขียน
ขั้น 8: STORAGE & MEMORY            → จัดเก็บผลงาน + ปรับปรุง Profile
```

### 7.3 Step 1 — VOICE SOURCE SELECTION / การเลือกแหล่งเสียง

**วัตถุประสงค์:**
- ระบุว่าผู้ใช้ต้องการเขียนงานประเภทใด
- ระบุแหล่งเอกสาร/ไฟล์ที่จะใช้สกัด Voice Profile

**สามกรณีที่พบ:**

**กรณี A: ผู้ใช้กำลังเริ่มเขียนงานใหม่**
→ ถามผู้ใช้:
- "งานนี้เป็นประเภทใด?" (วิทยานิพนธ์ / บทความวิชาการ / proposal / นโยบาย / blog / ฯลฯ)
- "ผู้เขียนคือใคร?" (ตนเอง / ในนามองค์กร / ในนามคณะผู้วิจัย)
- "มีงานเก่าของผู้เขียนคนนี้ให้ใช้สกัด Voice หรือไม่?"
- "ระบุโฟลเดอร์/ไฟล์อ้างอิงที่ต้องการให้ใช้สกัด Voice"

**กรณี B: ผู้ใช้นำข้อความที่ AI สร้างมาแล้ว ให้แก้**
→ อ่านข้อความก่อน เพื่อระบุ:
- หัวข้อ (subject matter detection)
- บริบท (academic / business / government / marketing)
- ภาษา (Thai / English / Bilingual)
- ความยาวและความซับซ้อน

→ จากนั้นถามผู้ใช้:
- "ต้องการให้สกัด Voice Profile จากแหล่งใด?"
- "หรือใช้ Voice Profile ที่บันทึกไว้แล้ว?" (ดูใน Memory)

**กรณี C: ผู้ใช้โหลดเอกสารอ้างอิงให้แล้ว**
→ Claude ดำเนินการอ่านเอกสารทันที ระบุหัวข้อ, ประเภท, สไตล์เบื้องต้น แล้วเข้าสู่ Step 2

**ผลลัพธ์ของ Step 1:**
```
Source Selection Record:
- Document Type: [ประเภทเอกสาร]
- Author Identity: [ผู้เขียน]
- Reference Sources: [แหล่งสกัด Voice]
- Language: [ภาษา]
- Context: [บริบท]
- Target AI Score: [< X%]
```

### 7.4 Step 2 — VOICE/WRITING PROFILE EXTRACTION / การสกัด Voice Profile

**วัตถุประสงค์:**
- สกัดเสียงและสไตล์ของผู้เขียนใน 6 มิติ (รายละเอียดทั้งหมดในภาค 8)

**ขั้นตอนสรุป:**
1. ใช้ **5-Level Source Hierarchy** (ภาค 8.2) เพื่อหาแหล่ง Voice
2. สกัด **6 Dimensions** (ภาค 8.3): Sentence-Level / Vocabulary / Paragraph / Argumentation / Citation / Cultural
3. ออกผลเป็น **Voice Profile** ตาม Output Template (ภาค 8.5)

**กฎ Anti-Hallucination:**
- ห้าม Claude สร้าง Voice Profile โดยเดา
- หากไม่มีแหล่งข้อมูลในทั้ง 5 Levels → **ต้องถามผู้ใช้ ไม่ใช่เดา**

**ผลลัพธ์ของ Step 2:**
- Voice Profile Document (ตาม template ในภาค 8.5)
- Voice Profile ID: VP-[YYYYMMDD]-[XXX]

### 7.5 Step 3 — VOICE/WRITING CALIBRATION & MEMORY CREATION / การปรับเทียบและบันทึก

**วัตถุประสงค์:**
- ยืนยันความถูกต้องของ Voice Profile กับผู้ใช้
- บันทึกเป็น Memory เพื่อ reuse

**ขั้นตอน:**
1. **Calibration Review** — แสดง Voice Profile ที่สกัดได้ให้ผู้ใช้ดู และให้ผู้ใช้ยืนยันหรือปรับ
2. **Test on Sample** — ให้ Claude เขียน sample paragraph สั้น ๆ (50–80 คำ) ตาม Profile แล้วให้ผู้ใช้ประเมิน
3. **Iteration** — ปรับ Profile ตาม feedback ของผู้ใช้ จนตรง
4. **Memory Storage** — บันทึก Profile ใน:
   - Project memory (สำหรับ project ปัจจุบัน)
   - Skill memory library (สำหรับ reuse ใน skill ครั้งต่อ ๆ ไป)

**ผลลัพธ์ของ Step 3:**
- Calibrated Voice Profile (V01R01 ของ Profile)
- Memory Reference: VP-[YYYYMMDD]-[XXX] บันทึกใน /voice_profiles/ folder

### 7.6 Step 4 — WRITE FIRST DRAFT / เขียนฉบับร่างแรก

**วัตถุประสงค์:**
- เขียนฉบับร่างโดย **อ้าง Knowledge Base ของฐานความรู้นี้** เพื่อหลีกเลี่ยง AI Statement และ AI Writing Style ตั้งแต่แรก

**กฎการเขียน:**
1. หลีกเลี่ยง Tier 1 Vocabulary (ภาค 4.1) ตั้งแต่ต้น
2. เขียนตาม Voice Profile ที่ calibrated แล้ว (Step 3)
3. ใส่ Personal Voice Markers (Layer 3 Check 8) ตั้งแต่ต้น — ไม่ต้องรอแก้ทีหลัง
4. ใช้ Burstiness สูง (SD ≥ 5) ตั้งแต่ต้น
5. สลับ Sentence Opening 5 รูปแบบ
6. ห้ามใช้ "humanizer tool" เลย — เขียนเองด้วยมือหรือ Claude (ภายใต้ guidance นี้)

**กรณีพิเศษ — Working with AI-Generated Draft:**
- ถ้าผู้ใช้นำข้อความที่ AI สร้างมาให้ → ข้ามไป Step 5 ทันที
- ถ้าเขียนใหม่จาก outline → ทำตามกฎข้างต้น

**ผลลัพธ์ของ Step 4:**
- Draft V01R01 พร้อม Voice Profile reference
- Pre-Detection notes (สิ่งที่ผู้เขียนเฝ้าระวัง)

### 7.7 Step 5 — AI DETECTION SELF-CHECK / ตรวจจับตนเอง 3 ชั้น

**วัตถุประสงค์:**
- วัด AI signature ของฉบับร่าง

**ขั้นตอน:**
1. ตรวจ Layer 1 (Vocabulary Footprints) — ภาค 4.1
2. ตรวจ Layer 2 (Statistical Patterns) — ภาค 4.2 (5 Checks)
3. ตรวจ Layer 3 (Structural Patterns) — ภาค 4.3 (3 Checks)
4. กรอก AI Detection Self-Check Report (ภาค 6)
5. (ทางเลือก) นำเข้าระบบจริง — Turnitin / Copyleaks / GPTZero / Originality
6. ใช้เครื่องมือ ≥ 2 ตัว cross-validate ถ้าทำได้

**Decision Gate:**
- ถ้าผ่านเกณฑ์ → ข้ามไป Step 7 (Voice Match Scoring)
- ถ้าไม่ผ่าน → ไป Step 6 (Two-Pass Correction)

**ผลลัพธ์ของ Step 5:**
- AI Detection Report ฉบับสมบูรณ์
- Decision: Pass → Step 7, Fail → Step 6

### 7.8 Step 6 — AI CORRECTION (Two-Pass Method) / การแก้ไขสองรอบ

**วัตถุประสงค์:**
- ดำเนินการ Two-Pass Method ตามภาค 9 อย่างเคร่งครัด

**ขั้นตอนสรุป (รายละเอียดในภาค 9):**

**Pass 1 — Rhythm Correction (5 Steps):**
- Step 1.1: ระบุย่อหน้าเสี่ยง
- Step 1.2: Burstiness Injection
- Step 1.3: Diversify Sentence Openings (5 รูปแบบ)
- Step 1.4: Adjust Paragraph Architecture
- Step 1.5: Verify SD ≥ 5

**Pass 2 — Vocabulary Correction (4 Steps):**
- Step 2.1: Search & Replace 8 หมวด ตามลำดับ
- Step 2.2: Replace by Voice Profile (จาก Step 3)
- Step 2.3: Avoid Symptom Substitution
- Step 2.4: Add Specificity

**Optional — Advanced Techniques (ภาค 9.4):**
- A: Sentence Combining & Splitting
- B: Personal/Cultural Markers
- C: Aside & Qualification
- D: Imperfect Flow

**Optional — 12 Techniques Catalog (ภาค 10):**
ใช้เลือกตามปัญหาที่ระบุ

**กฎเหล็ก:** ห้ามรัน Pass 1 และ Pass 2 พร้อมกัน

**Loop Back:** หลัง Step 6 ให้ย้อนทำ Step 5 (Re-Detection) จนผ่าน

**ผลลัพธ์ของ Step 6:**
- Draft V01R02+ (Humanized — ผ่าน Two-Pass)
- Pass 1 Change Log
- Pass 2 Change Log

### 7.9 Step 7 — VOICE/WRITING MATCH SCORING / การให้คะแนนความตรงเสียง

**วัตถุประสงค์:**
- ตรวจว่าฉบับที่ humanize แล้ว **ตรง Voice Profile** ของผู้เขียนหรือไม่
- ป้องกัน "ผ่าน detector แต่ไม่ใช่เสียงผู้เขียน"

**ขั้นตอนสรุป (รายละเอียดในภาค 11):**
1. วัดทุกมิติของ Voice Profile กับฉบับสุดท้าย
2. ให้คะแนนแต่ละมิติ (0–100%)
3. คำนวณ Overall Match Score
4. Pass / Fail ตามเกณฑ์ (มักใช้ ≥ 75%)

**Decision Gate:**
- Match Score ≥ 75% → ผ่าน → Step 8
- Match Score < 75% → ย้อน Step 6 ปรับใหม่ตาม Voice Profile

**ผลลัพธ์ของ Step 7:**
- Voice Match Scoring Report
- Decision: Pass → Step 8, Fail → Step 6

### 7.10 Step 8 — STORAGE & MEMORY / การจัดเก็บและบันทึก

**วัตถุประสงค์:**
- จัดเก็บผลงานสุดท้าย
- ปรับปรุง Voice Profile Memory (learning loop)

**ขั้นตอน:**
1. **Final Document Storage** — บันทึกฉบับสุดท้ายตามมาตรฐานองค์กร (เช่น 20-Output/ ใน Project Mode)
2. **Voice Profile Update** — ถ้าฉบับสุดท้ายมีลักษณะใหม่ที่ผู้ใช้ยอมรับ ให้ update Voice Profile (V01R02 ของ Profile)
3. **Memory Index** — บันทึก:
   - Document ID, Voice Profile ID, AI Score, Match Score
   - Lessons learned (ปัญหาที่พบ + วิธีแก้)
4. **Disclosure (ถ้าจำเป็น)** — แนบ AI Disclosure ตามภาค 14

**ผลลัพธ์ของ Step 8:**
- Final Document V01R0X พร้อม metadata
- Updated Voice Profile (ถ้ามีการเรียนรู้ใหม่)
- Memory Index Entry

### 7.11 Visual Summary — 8-Step Master Workflow

```
┌─────────────────────────────────────────────────────────────────┐
│         8-STEP SEQUENTIAL THINKING MASTER WORKFLOW              │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Step 1: VOICE SOURCE SELECTION                                 │
│  └─ ถามประเภทงาน + แหล่งอ้างอิง                                │
│           ↓                                                     │
│  Step 2: VOICE/WRITING PROFILE EXTRACTION                       │
│  └─ 5-Level Source Hierarchy → 6 Dimensions → Profile           │
│           ↓                                                     │
│  Step 3: CALIBRATION & MEMORY CREATION                          │
│  └─ Review → Test → Iterate → Save (VP-ID)                      │
│           ↓                                                     │
│  Step 4: WRITE FIRST DRAFT                                      │
│  └─ ตาม Voice Profile + Avoid Tier 1 + KB Guidance              │
│           ↓                                                     │
│  Step 5: AI DETECTION SELF-CHECK ←──────────┐                  │
│  └─ 3-Layer Methodology + Detection Report  │                  │
│           ↓                                  │                  │
│        ผ่าน?                                 │                  │
│       ↙    ↘                                │                  │
│      No    Yes                               │                  │
│       ↓     ↓                                │                  │
│  Step 6:    │                                │                  │
│  TWO-PASS  │                                │                  │
│  CORRECTION│                                │                  │
│  Pass 1 → Pass 2 → Advanced ─────────────────┘                  │
│             ↓                                                   │
│  Step 7: VOICE/WRITING MATCH SCORING ←──────┐                  │
│  └─ 6 Dimensions Match → Overall Score      │                  │
│           ↓                                  │                  │
│        ≥ 75%?                                │                  │
│       ↙    ↘                                │                  │
│      No    Yes                               │                  │
│       ↓     ↓                                │                  │
│   ย้อน Step 6  ──────────────────────────────┘                  │
│              ↓                                                  │
│  Step 8: STORAGE & MEMORY                                       │
│  └─ Save Final + Update Profile + Memory Index                  │
│              ↓                                                  │
│         FINAL OUTPUT                                            │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 8. VOICE/WRITING PROFILE EXTRACTION METHODOLOGY / ระเบียบวิธีสกัด Voice Profile

### 8.1 Why Voice Profile Matters / ทำไม Voice Profile จึงสำคัญ

ภาคนี้สร้างขึ้นบนพื้นฐานวิชาการของ **Stylometry** — ศาสตร์ที่ใช้สถิติเชิงภาษาวิเคราะห์สไตล์การเขียน เป็นที่ยอมรับในงานนิติเวชเชิงภาษา (forensic linguistics) มาตั้งแต่ปี 1851 (Mendenhall) และนำมาใช้ระบุผู้เขียนที่ไม่ทราบชื่อมาตลอด

**หลักการ Stylometric:**
> "Stylometry ignores the content of a piece, focusing on the latent authorial fingerprint — a linguistic signature detectable through patterns of word choice, sentence structure, and stylistic markers — that is present in all writings of an author."

**สำหรับ AI Correction:**
- AI Detector ทำงานบนหลัก Stylometry — ตรวจ "AI fingerprint"
- การ humanize ที่ดี ต้องเปลี่ยนจาก "AI fingerprint" เป็น "ผู้เขียน fingerprint" ของผู้เขียนคนนั้น
- หากไม่มี Voice Profile → ผลลัพธ์เป็น "เสียงทั่วไปของมนุษย์" ที่ลด AI score ได้แต่ไม่ใช่เสียงผู้เขียน

**ใน V04R01 Voice Profile จึงเป็นแกน — ไม่ใช่ส่วนเสริม**

### 8.2 The 5-Level Voice Source Hierarchy / ลำดับความสำคัญของแหล่งเสียง 5 ระดับ

เมื่อต้องสกัด Voice Profile Claude ต้องไล่ตามลำดับนี้ ห้ามข้ามขั้น

#### 🥇 Level 1 (Priority สูงสุด): User-Specified Folder / Reference

**เงื่อนไข:** ผู้ใช้ระบุ folder, ไฟล์, หรือเอกสารอ้างอิงเฉพาะที่จะใช้สกัด Voice

**วิธีดำเนินการ:**
1. อ่านเอกสารทุกชิ้นในแหล่งที่ระบุ
2. สกัด 6 Dimensions (ภาค 8.3)
3. รวมผลเป็น Voice Profile ใหม่สำหรับ prompt/project นี้

**ตัวอย่าง:**
- "ใช้บทความ 5 ฉบับใน /Users/.../my-published-articles/ เป็น reference"
- "สกัดจากวิทยานิพนธ์ปริญญาเอกของผู้เขียนคนนี้"
- "ใช้ proposal ที่ส่งให้ลูกค้า ABC ในปี 2567"

#### 🥈 Level 2 (Default): This MD / This Skill Reference

**เงื่อนไข:** ผู้ใช้ไม่ระบุแหล่ง — ใช้ Voice Profile ที่ฝังในฐานความรู้นี้

**Voice Profile ที่ฝังใน V04R01 KB:**

แม้ KB นี้เน้นวิธีการสกัด มากกว่ามี Pre-defined Voice Profiles ก็ตาม สำหรับ Default ใช้ Voice Profile ดังนี้:

**Default Profile A: Senior Advisor Thai Bilingual**
- Sentence-Level: SD ≥ 5, Mean 18 คำ
- Vocabulary: ภาษาธุรกิจขั้นสูง, ใช้ศัพท์ราชบัณฑิตยสภา
- Paragraph: 4–8 ประโยค, เปิดด้วย topic sentence + evidence
- Argumentation: Comparative + Critical + Counterargument
- Citation: APA นาม-ปี
- Cultural: อ้างกฎหมายไทย + บริบท SE Asia

**Default Profile B: Academic Researcher Thai PhD**
- Sentence-Level: SD ≥ 6, Mean 22 คำ
- Vocabulary: ศัพท์เฉพาะสาขา + ราชบัณฑิตยสภา
- Paragraph: 6–10 ประโยค, theoretical framing
- Argumentation: Inductive + Theory-grounded
- Citation: ทุก claim มี citation
- Cultural: อ้างทฤษฎี + Buddhist insights (ถ้าเหมาะสม)

#### 🥉 Level 3 (Active Skill's Knowledge Base)

**เงื่อนไข:** ใน Custom Skill ที่จะสร้างขึ้น มี knowledge base ของ skill นั้นที่ฝัง Voice Profile

**วิธีดำเนินการ:**
- โหลด Voice Profile จาก /references/voice_profile.md ใน skill ที่ active

#### 4️⃣ Level 4 (Pre-defined Skills Voice Profile Library)

**เงื่อนไข:** Skill มี Voice Profile Library — มี Voice Profile ที่กำหนดไว้สำเร็จรูปสำหรับบริบทมาตรฐาน

**🆕 V05R01 Library — KM-TH-THESIS-DOC (Voice Profile Library สำหรับงานวิชาการไทย):**

ฐานข้อมูล `voice_profiles/KM-TH-THESIS-DOC/` มี **7 Sub-Profiles** ที่สกัดจาก corpus 101 ไฟล์งานวิจัยไทย (~292,000 คำ):

| Profile ID | ชื่อ Profile | ขอบเขตการใช้งาน |
|---|---|---|
| **VP-A1** | MCU PA Dissertation | ดุษฎีนิพนธ์รัฐประศาสนศาสตร์ มจร (ไม่เน้นพุทธบูรณาการเป็นแกน) |
| **VP-A2** | MCU Buddhist Integration | ดุษฎีนิพนธ์ มจร ที่เน้นพุทธบูรณาการเป็นแกนทฤษฎี |
| **VP-B1** | AGJ Article | บทความวิชาการในวารสารบัณฑิตศึกษาวิชาการ (TCI Tier 2) |
| **VP-B2** | General TCI Academic | บทความวิชาการ TCI ทั่วไปที่ไม่ใช่ AGJ |
| **VP-C1** | Accounting Research | บทความวิจัยสาขาบัญชี/บริหารธุรกิจ (มีสถิติ x̄, SD) |
| **VP-C2** | Procurement Research | บทความวิจัยสาขาการจัดซื้อจัดจ้าง / e-GP |
| **VP-C3** | Public Sector/Education Research | บทความวิจัยสาขารัฐประศาสนศาสตร์/การศึกษา |

**คุณสมบัติของ KM-TH-THESIS-DOC:**
- ครอบคลุม 6+1 Dimensions ครบสำหรับทุก Sub-Profile
- มีสถิติเชิงปริมาณจริง (Mean, SD, Distribution) จาก corpus
- มี Real Opening Sentence Library
- มี Buddhist Dhamma Library (ไตรสิกขา, อิทธิบาท ๔, พรหมวิหาร ๔, พละ ๔, สังคหวัตถุ ๔, สาราณียธรรม)
- มี Pali Tipitaka Citation Format
- มี Verified AI Signature List (คำที่ปรากฏ ≤ 5 ครั้งใน corpus 292K คำ)

**Library ที่แนะนำให้สร้างเพิ่มเติม (ใน skill ในอนาคต):**
- `business_b2b_cfo.md` — proposal ระดับ CFO
- `business_sales_proposal.md` — sales pursuit
- `government_thai_official.md` — หนังสือราชการ
- `government_thai_policy.md` — รายงานนโยบาย
- `marketing_thai_b2c.md` — content การตลาด B2C
- `marketing_thought_leadership.md` — thought leadership content

**วิธีดำเนินการเมื่อใช้ KM-TH-THESIS-DOC:**
1. อ่าน [`KM-TH-THESIS-DOC V02R01`](../voice_profiles/KM-TH-THESIS-DOC/KM-TH-THESIS-DOC_V02R01_2026-04-30.md)
2. ตรวจ Decision Tree (Part 3 Section 12 ของ KM-TH-THESIS-DOC) เพื่อเลือก Sub-Profile ที่เหมาะสม
3. ใช้ Sub-Profile นั้นเป็น Voice Profile สำหรับ Pass 2 Vocabulary Correction

#### 5️⃣ Level 5 (Fallback): ASK USER — ห้ามเดา ห้ามมั่ว

**เงื่อนไข:** ทุก Level 1–4 ไม่มีข้อมูล

**กฎเหล็ก:**
- **ห้าม Claude สร้าง Voice Profile ขึ้นมาเอง**
- **ห้ามเดา**
- **ต้องถามผู้ใช้** ด้วยคำถามต่อไปนี้:

```
ผมไม่พบ Voice/Writing Profile ในแหล่งที่กำหนด ครับ
เพื่อให้การ humanize ตรงเสียงผู้เขียน กรุณาระบุข้อใดข้อหนึ่ง:

(a) ระบุโฟลเดอร์/ไฟล์อ้างอิงที่ผมจะสกัด Voice ได้
(b) เลือก Pre-defined Voice Profile จาก Library:
    - [Profile A: Academic Thai PhD]
    - [Profile B: Business B2B CFO]
    - [Profile C: Government Thai Official]
    - [Profile D: Marketing Thought Leadership]
    - [อื่น ๆ ตาม Library]
(c) ให้ผมเขียน 3 ตัวอย่างน้ำเสียงต่างกัน เพื่อให้ท่านเลือก
(d) ดำเนินการต่อโดยใช้ Default Profile ของ KB (ระบุข้อจำกัดในผลลัพธ์)
```

### 8.3 The 6 Dimensions of Voice/Writing Profile / 6 มิติของ Voice Profile

ไม่ว่าจะใช้แหล่งใด (Level 1–4) Claude ต้องสกัดให้ครบทั้ง 6 มิติ

#### 📐 Dimension 1: Sentence-Level Patterns / รูปแบบระดับประโยค

**สิ่งที่ต้องสกัด:**
- ความยาวประโยคเฉลี่ย (Mean number of words)
- การกระจายตัวของความยาวประโยค (Distribution: short / medium / long ในรูปเปอร์เซ็นต์)
- ค่า Standard Deviation (SD) ของความยาวประโยค
- ประเภทประโยคที่ใช้บ่อย (บอกเล่า / เงื่อนไข / เปรียบเทียบ / เหตุและผล)
- ตำแหน่งของประธานและกริยาในประโยค
- การใช้ประโยคซ้อน (complex/compound) vs ประโยคเดี่ยว (simple)

**Output Sample:**
```
Dimension 1 — Sentence-Level Patterns:
- Mean sentence length: 19.4 words
- Distribution: Short (5-12w) 22% / Medium (13-24w) 51% / Long (25+w) 27%
- Standard Deviation: 7.8
- Frequent types: Comparative (38%), Causal (29%), Conditional (20%)
- Subject-Verb position: Subject-first 65%, Adverbial-first 20%, Quote/Question 15%
- Complex vs Simple: Complex 60% / Simple 40%
```

#### 📚 Dimension 2: Vocabulary Signature / ลายเซ็นคำศัพท์

**สิ่งที่ต้องสกัด:**
- ศัพท์เทคนิคที่ใช้ในเอกสารอ้างอิง (พร้อมความถี่)
- คำเชื่อมที่ปรากฏบ่อย (frequency-ranked)
- คำกริยาที่นิยมใช้ในการวิเคราะห์
- คำคุณศัพท์เชิงวิชาการที่ใช้บ่อย
- **คำที่ผู้เขียนหลีกเลี่ยง** (โดยเฉพาะ Tier 1 ที่ผู้เขียนแท้ ๆ ไม่ใช้)

**Output Sample:**
```
Dimension 2 — Vocabulary Signature:
- Domain Terms (high freq): "GFMIS" (24x), "การบริหารงบประมาณ" (18x),
                              "ระบบสารสนเทศภาครัฐ" (15x)
- Connectives: "ดังนั้น" (12x), "เนื่องจาก" (8x), "ในขณะที่" (6x)
                ⚠️ ผู้เขียนไม่ใช้ "นอกจากนี้/อีกทั้ง"
- Analysis verbs: "วิเคราะห์", "สังเคราะห์", "เปรียบเทียบ", "ตีความ"
- Academic adjectives: "เชิงระบบ", "เชิงประจักษ์", "เชิงทฤษฎี"
- AVOIDED: "ขับเคลื่อน", "ยกระดับ", "อย่างยั่งยืน", "อย่างครอบคลุม"
```

#### 🏗️ Dimension 3: Paragraph Architecture / สถาปัตยกรรมย่อหน้า

**สิ่งที่ต้องสกัด:**
- ความยาวย่อหน้าเฉลี่ย (จำนวนประโยค)
- รูปแบบการเปิดย่อหน้า (Topic Sentence / Question / Quote / Statistic / Anecdote)
- รูปแบบการปิดย่อหน้า (Synthesis / Transition / Open Question / Implication)
- การจัดเรียงเหตุผล (Inductive / Deductive / Mixed)

**Output Sample:**
```
Dimension 3 — Paragraph Architecture:
- Mean paragraph: 6.2 sentences
- Opening pattern: Topic Sentence 55%, Question 18%, Quote 12%, Statistic 15%
- Closing pattern: Synthesis 60%, Transition 25%, Open Question 15%
- Reasoning: Inductive 30%, Deductive 45%, Mixed 25%
```

#### ⚔️ Dimension 4: Argumentation Style / สไตล์การโต้แย้ง

**สิ่งที่ต้องสกัด:**
- วิธีนำเสนอ Claim (assertive / hedged / qualified)
- วิธียก Evidence (จำนวน citation ต่อ claim, ประเภท evidence ที่นิยม)
- วิธีวิเคราะห์ (เปรียบเทียบ / สังเคราะห์ / วิพากษ์ / เชิงทฤษฎี / เชิงประจักษ์)
- วิธีจัดการกับ Counterargument (acknowledge / refute / synthesize)
- น้ำหนักระหว่าง Theory vs Empirical Evidence

**Output Sample:**
```
Dimension 4 — Argumentation Style:
- Claim style: Assertive 70% / Hedged 30%
- Evidence per claim: Avg 1.4 citations
- Analysis types: Comparative 35%, Critical 30%, Synthetic 25%, Theoretical 10%
- Counterargument handling: Acknowledge & refute (always include)
- Theory vs Empirical: 40% theory / 60% empirical evidence
```

#### 📑 Dimension 5: Citation & Reference Style / สไตล์การอ้างอิง

**สิ่งที่ต้องสกัด:**
- ความถี่ของ In-text Citation (ต่อ 100 คำ)
- ตำแหน่งที่นิยมวาง Citation (ปลายประโยค / กลางประโยค / เปิดประโยค)
- รูปแบบการกล่าวถึงผู้แต่ง (Author-prominent: "Smith (2023) argues…" vs Information-prominent: "AI detection has matured (Smith, 2023).")
- การใช้ Direct Quote vs Paraphrase
- รูปแบบ citation (APA, Chicago, Vancouver, ฯลฯ)

**Output Sample:**
```
Dimension 5 — Citation & Reference Style:
- Citation density: 3.2 per 100 words
- Position: End-sentence 60%, Mid-sentence 25%, Opening 15%
- Style: Author-prominent 65%, Information-prominent 35%
- Quote vs Paraphrase: Direct quote 15%, Paraphrase 85%
- Format: APA 7th edition (นาม-ปี)
```

#### 🇹🇭 Dimension 6: Cultural & Contextual Markers / เครื่องหมายวัฒนธรรมและบริบท

**สิ่งที่ต้องสกัด:**
- การอ้างอิงบริบทไทย (กฎหมาย / หน่วยงาน / นโยบาย)
- การใช้คำศัพท์ทางพระพุทธศาสนา (ถ้ามี)
- การยกตัวอย่างกรณีศึกษา (international vs domestic mix)
- น้ำเสียงทางวัฒนธรรม (เป็นทางการ / กึ่งทางการ / ไม่เป็นทางการ)
- การใช้สำนวนพื้นเมือง / สำนวนเฉพาะอาชีพ

**Output Sample:**
```
Dimension 6 — Cultural & Contextual Markers:
- Thai context references: กฎหมายไทย 12 จุด, หน่วยงานไทย 8 จุด, นโยบายไทย 5 จุด
- Buddhist references: 0 (academic context นี้ไม่ใช้)
- Case studies: Thailand 65%, ASEAN 20%, International 15%
- Cultural register: Formal academic
- Profession-specific phrases: "อาศัยอำนาจตาม", "ระเบียบกระทรวงการคลัง"
```

### 8.4 Intensive Mode for Academic Writing / โหมดเข้มข้นสำหรับงานวิชาการ

สำหรับงานวิจัย วิทยานิพนธ์ ดุษฎีนิพนธ์ บทความวิชาการ — ที่ความตรง Voice เป็นเรื่องสำคัญสุด — ใช้ **Intensive Mode** ที่เพิ่มขั้นตอนต่อไปนี้

#### 8.4.1 Reference Corpus Requirement (Intensive)

**ขั้นต่ำ:** เอกสารอ้างอิงต้องมี:
- อย่างน้อย **5 เอกสาร** ของผู้เขียนคนเดียวกัน
- รวมความยาวไม่ต่ำกว่า **30,000 คำ**
- ครอบคลุมช่วงเวลาอย่างน้อย **2 ปี** (เพื่อจับการเปลี่ยนแปลงสไตล์ที่อาจมี)

**ทำไม:**
- งานวิจัย stylometry แสดงว่าสไตล์ผู้เขียนสามารถระบุได้ใน 5,000 คำขึ้นไป
- ความเสถียรของการระบุเพิ่มขึ้นชัดเมื่อมี ≥ 30,000 คำ
- ผู้เขียนมีการเปลี่ยนแปลงสไตล์ตามเวลา จึงต้องครอบคลุมหลายช่วง

#### 8.4.2 Disciplinary Voice Profile / Voice Profile เฉพาะสาขา

**Intensive Mode** เพิ่มมิติที่ 7 (เฉพาะ academic):

**Dimension 7 (Academic Add-On): Disciplinary Conventions**
- Hedging norms ของสาขา (laden / sparse)
- Use of first-person in academic prose (ผู้วิจัย / I / We)
- Reading philosophy: positivist / interpretive / critical
- Preferred research methodology language
- Discipline-specific theoretical framing
- Citation density expected by journal

**ตัวอย่าง — Public Administration (รัฐประศาสนศาสตร์):**
```
Dimension 7 — Disciplinary Conventions:
- Hedging: Sparse (เน้นยืนยันด้วย evidence)
- First-person: ใช้ "ผู้วิจัย" หรือเลี่ยงประธาน
- Philosophy: Critical-Pragmatic
- Methodology language: "การวิจัยเชิงคุณภาพ", "การสัมภาษณ์เชิงลึก"
- Theoretical framing: New Public Management, Good Governance
- Citation density: 4-6 per 100 words (TCI Tier 2 standard)
```

#### 8.4.3 Author Evolution Tracking / การติดตามการเปลี่ยนแปลง

**สำหรับผู้เขียนที่เขียนต่อเนื่อง:**
- ระบุ early-career vs mid-career vs current
- บันทึก trajectory of vocabulary expansion
- ระบุ stable signature elements vs evolving ones

#### 8.4.4 Voice Profile Verification (Calibration ขั้นเข้ม)

**Intensive Mode Calibration:**
1. Claude เขียน 3 sample paragraphs ที่ topic ต่างกัน ตาม Profile
2. ผู้ใช้ blind test — เลือก paragraph ที่เหมือนเสียงตน
3. ถ้า ≥ 2 จาก 3 paragraphs ผู้ใช้ระบุว่าเหมือน → Profile pass
4. ถ้าไม่ → กลับไปสกัดใหม่ พร้อมระบุประเด็นที่คลาดเคลื่อน

### 8.5 Voice Profile Output Template / แม่แบบ Voice Profile

```
═══════════════════════════════════════════════════════
👤 VOICE/WRITING PROFILE
═══════════════════════════════════════════════════════
Profile ID:        VP-[YYYYMMDD]-[XXX]
Author/Persona:    [ชื่อผู้เขียน หรือ persona]
Created:           [Date]
Version:           V[##]R[##]
Source Level:      [1 / 2 / 3 / 4 / 5]
Source Documents:  [list of reference documents]
Total Reference:   [X words across Y documents]
Calibration Status: ☐ Pending  ☐ Calibrated  ☐ Verified

─────────────────────────────────────────────────────
📐 DIMENSION 1: SENTENCE-LEVEL PATTERNS
─────────────────────────────────────────────────────
- Mean sentence length: [X] words
- Distribution: Short (5-12w) [X]% / Medium (13-24w) [X]% / Long (25+w) [X]%
- Standard Deviation: [X.X]
- Frequent types: [list with %]
- Subject-Verb position: [list with %]
- Complex vs Simple: [X]% / [X]%

─────────────────────────────────────────────────────
📚 DIMENSION 2: VOCABULARY SIGNATURE
─────────────────────────────────────────────────────
- Domain Terms (high freq): [list with frequency]
- Frequent Connectives: [list]
- Analysis Verbs: [list]
- Academic Adjectives: [list]
- AVOIDED Words: [list — เน้น Tier 1 ที่ผู้เขียนไม่ใช้]

─────────────────────────────────────────────────────
🏗️ DIMENSION 3: PARAGRAPH ARCHITECTURE
─────────────────────────────────────────────────────
- Mean paragraph: [X] sentences
- Opening pattern: [list with %]
- Closing pattern: [list with %]
- Reasoning order: [Inductive / Deductive / Mixed - %]

─────────────────────────────────────────────────────
⚔️ DIMENSION 4: ARGUMENTATION STYLE
─────────────────────────────────────────────────────
- Claim style: [Assertive / Hedged / Qualified - %]
- Evidence per claim: [X citations average]
- Analysis types: [list with %]
- Counterargument handling: [Acknowledge / Refute / Synthesize]
- Theory vs Empirical: [X]% / [X]%

─────────────────────────────────────────────────────
📑 DIMENSION 5: CITATION & REFERENCE STYLE
─────────────────────────────────────────────────────
- Citation density: [X] per 100 words
- Position: [End / Mid / Opening - %]
- Style: [Author-prominent / Information-prominent - %]
- Quote vs Paraphrase: [%] / [%]
- Format: [APA / Chicago / Vancouver / Custom]

─────────────────────────────────────────────────────
🇹🇭 DIMENSION 6: CULTURAL & CONTEXTUAL MARKERS
─────────────────────────────────────────────────────
- Thai context references: [count by type]
- Buddhist references: [Y/N + frequency if any]
- Case studies: Thailand [X]% / ASEAN [X]% / International [X]%
- Cultural register: [Formal / Semi-formal / Informal]
- Profession-specific phrases: [list]

─────────────────────────────────────────────────────
🎓 DIMENSION 7 (ACADEMIC INTENSIVE ONLY)
─────────────────────────────────────────────────────
- Hedging norms: [Laden / Sparse]
- First-person usage: [convention]
- Philosophy: [list]
- Methodology language: [list]
- Theoretical framing: [list]
- Citation density expected: [X] per 100 words

─────────────────────────────────────────────────────
🔄 CALIBRATION SAMPLES
─────────────────────────────────────────────────────
Sample 1 (Topic: [X]):
[ตัวอย่างย่อหน้าที่ Claude เขียนตาม Profile นี้]

Sample 2 (Topic: [Y]):
[ตัวอย่างย่อหน้า]

Sample 3 (Topic: [Z]):
[ตัวอย่างย่อหน้า]

User Verification: ☐ Sample 1 ☐ Sample 2 ☐ Sample 3 (passed)

═══════════════════════════════════════════════════════
📌 NOTES & USAGE GUIDANCE
═══════════════════════════════════════════════════════
[ข้อสังเกตเพิ่มเติม กฎพิเศษ ข้อจำกัดที่ผู้ใช้ระบุ]

═══════════════════════════════════════════════════════
```

### 8.6 Verified AI Signature List — รายการคำที่เป็น AI signature จริง 🆕 V05R01

**Methodology:** วิเคราะห์ corpus 101 ไฟล์งานวิจัยไทย (~292,000 คำ) ที่เก็บไว้ใน `voice_profiles/KM-TH-THESIS-DOC/` ทำให้ได้ **Verified AI Signature List** — คำที่ AI Detector มักจัดว่าเป็น AI pattern แต่ตรวจสอบกับงานเขียนของนักวิจัยไทยจริง ๆ ว่า "ปรากฏหรือไม่"

#### 🔴 Confirmed AI Signatures (ปรากฏ ≤ 5 ครั้งใน corpus 292K คำ)

**คำเหล่านี้คือ AI signature จริง — Pass 2 ต้องลบออกในงานเขียนภาษาไทยทุกประเภท:**

| คำ | จำนวนครั้ง | Action |
|---|---|---|
| เป็นที่ทราบกันดีว่า | 0 | ลบทิ้ง |
| นับเป็นสิ่งสำคัญ | 0 | ลบทิ้ง |
| ในแง่หนึ่ง | 0 | ระบุแง่ไหน |
| อาจถือได้ว่า | 0 | "ถือว่า" |
| ดังที่กล่าวไว้ข้างต้น | 0 | "ดังนั้น" / ลบ |
| อย่างพิถีพิถัน | 0 | "อย่างละเอียด" |
| ยิ่งไปกว่านั้น | 1 | "นอกจากนั้น" |
| อาจกล่าวได้ว่า | 1 | ลบ |
| ในเวลาเดียวกัน | 1 | "ในขณะเดียวกัน" |
| ในท้ายที่สุด | 1 | "ท้ายที่สุด" |
| กล่าวโดยสรุป | 2 | "สรุปว่า" |
| ปฏิเสธไม่ได้ว่า | 3 | ลบ |

#### 🟢 Common in Real Thai — ใช้ได้ (ปรากฏ > 30 ครั้ง)

**คำเหล่านี้ที่เคยจัดเป็น AI Tier 1 แต่ "ใช้แพร่หลายในไทยจริง" — ไม่ใช่ AI signature:**

| คำ | จำนวนครั้ง | จำนวนไฟล์ | ใช้ได้เพราะ |
|---|---|---|---|
| ขับเคลื่อน | 272 | 62 | นักวิจัยไทยใช้แพร่หลาย |
| ยกระดับ | 133 | 43 | ใช้ในงานนโยบาย |
| อย่างมีประสิทธิภาพ | 195 | 55 | ใช้แพร่หลาย |
| บูรณาการ | 432 | 59 | คำหลักในงานพุทธบูรณาการ |
| หลากหลาย | 179 | 55 | ใช้แพร่หลาย |
| อย่างยั่งยืน | 68 | 32 | ใช้บ่อยในเชิงนโยบาย |
| ดังนั้น | 239 | 82 | คำเชื่อมมาตรฐาน |
| เนื่องจาก | 290 | 79 | คำเชื่อมมาตรฐาน |

> **กฎใหม่:** Pass 2 (Vocabulary Correction) ภาษาไทยต้องใช้ Verified AI Signature List นี้แทน Tier 1 list ทั่วไป — รายละเอียดทั้งหมดใน [`KM-TH-THESIS-DOC V02R01`](../voice_profiles/KM-TH-THESIS-DOC/KM-TH-THESIS-DOC_V02R01_2026-04-30.md) Section 3, 14, 15

### 8.7 Thai Academic Sub-Profiles — 7 Sub-Profiles 🆕 V05R01

V05R01 เพิ่ม 7 Sub-Profiles เฉพาะงานเขียนวิชาการไทย ที่สกัดจาก corpus 101 ไฟล์จริง ใน [`KM-TH-THESIS-DOC V02R01`](../voice_profiles/KM-TH-THESIS-DOC/KM-TH-THESIS-DOC_V02R01_2026-04-30.md):

| Sub-Profile | สาขา | Mean Sentence | Citation Style | Buddhist Dhamma |
|---|---|---|---|---|
| **VP-A1** MCU PA Diss. | ดุษฎีนิพนธ์รัฐประศาสนศาสตร์ | 21.4 คำ | เชิงอรรถ | น้อย |
| **VP-A2** MCU Buddhist Diss. | ดุษฎีนิพนธ์พุทธบูรณาการ | 21.4 คำ | เชิงอรรถ + พระไตรปิฎก | มาก (แกนหลัก) |
| **VP-B1** AGJ Article | บทความ AGJ TCI Tier 2 | 23.1 คำ | APA | น้อย-มาก |
| **VP-B2** General TCI Academic | บทความวิชาการ TCI ทั่วไป | 23.1 คำ | APA | น้อย |
| **VP-C1** Accounting Research | วิจัยบัญชี/บริหาร | 23.0 คำ | APA + สถิติ | ไม่มี |
| **VP-C2** Procurement Research | วิจัยจัดซื้อจัดจ้าง | 23.0 คำ | APA + พ.ร.บ. | ไม่มี |
| **VP-C3** Public/Education Research | วิจัยรัฐ/การศึกษา | 23.0 คำ | APA | ไม่มี |

**Decision Tree** สำหรับเลือก Sub-Profile อยู่ใน [`KM-TH-THESIS-DOC V02R01`](../voice_profiles/KM-TH-THESIS-DOC/KM-TH-THESIS-DOC_V02R01_2026-04-30.md) Section 12

---

## 9. AI CORRECTION PROTOCOL — TWO-PASS METHOD / โปรโตคอลแก้ไข AI: วิธีสองรอบ

ภาคนี้คือรายละเอียด Step 6 ของ 8-Step Master Workflow — **โปรโตคอลปฏิบัติสำคัญที่สุด**

### 9.1 PRINCIPLE: Two-Pass Correction Method / หลักการสองรอบ

**Pass 1 — Rhythm Correction:** แก้รูปแบบประโยค (จังหวะ ความยาว การเปิด)
**Pass 2 — Vocabulary Correction:** แก้คำศัพท์ (Tier 1, AI phrases, hedging) **โดยอ้าง Voice Profile**

#### ⚠️ กฎเหล็ก: ห้ามทำพร้อมกันในรอบเดียว

**เหตุผล:**
1. **Cognitive Load:** การแก้สองมิติพร้อมกันทำให้ overwhelm
2. **Verifiability:** การแยก Pass ทำให้วัดผลแต่ละมิติได้
3. **Symptom Substitution Risk:** ทำพร้อมกันมักเปลี่ยนคำ AI เป็นคำ AI อีกคำ
4. **Quality Control:** Pass 1 ต้องตรวจ SD ≥ 5 ก่อน Pass 2 — ถ้าทำพร้อมกันวัดไม่ได้
5. **Voice Profile Alignment:** Pass 2 ต้องอ้าง Voice Profile — ถ้าทำพร้อมกัน Voice หลุด

**ลำดับที่ถูกต้อง:**
```
Draft → Pass 1 (Rhythm) → ตรวจ SD ≥ 5 → Pass 2 (Vocabulary + Voice Profile) → ตรวจ Tier 1 ผ่าน → Done
```

### 9.2 PASS 1: RHYTHM CORRECTION / รอบที่ 1 แก้จังหวะ

#### Step 1.1: ระบุย่อหน้าที่เสี่ยง

อ่านทีละย่อหน้า — หากมีมากกว่า 3 ประโยคยาว 16–22 คำ ใน 5 ประโยคติดต่อกัน → mark

#### Step 1.2: ปรับความยาวประโยค (Burstiness Injection)

**กฎการแก้ (ต่อย่อหน้าที่ mark):**
- ตัด 2 ประโยคให้สั้นลง (8–12 คำ)
- ขยาย 1 ประโยคให้ยาวขึ้น (25–35 คำ) ด้วยรายละเอียดเฉพาะ

**ตัวอย่าง:**

*ก่อน:* "ระบบนี้ช่วยลดต้นทุนการดำเนินงานอย่างมีนัยสำคัญ องค์กรที่นำระบบไปใช้พบผลลัพธ์ที่ดีอย่างต่อเนื่อง ทีมงานสามารถทำงานได้อย่างมีประสิทธิภาพมากขึ้น ผู้บริหารพึงพอใจกับผลที่ได้รับ"
SD ≈ 1.7 ❌

*หลัง:* "ต้นทุนลดลง 23% ในเดือนแรก ที่บริษัท ABC ในไตรมาส 2 ปี 2567 ทีม Finance รายงานว่าพวกเขาปิดบัญชีรายเดือนเร็วขึ้น 4 วันโดยไม่ต้องเพิ่มคนเลย ผู้บริหารยอมรับ"
SD ≈ 14.4 ✅

#### Step 1.3: ปรับการเปิดประโยค (5 รูปแบบ)

1. **Adverb:** "ในปี 2567 องค์กร 245 แห่งได้นำระบบนี้ไปใช้"
2. **Subordinate Clause:** "เมื่อพิจารณาจากข้อมูลย้อนหลัง 5 ปี…"
3. **Question:** "อะไรเป็นปัจจัยสำคัญที่ทำให้สำเร็จ?"
4. **Quote:** "นักวิชาการชี้ว่า 'การปฏิรูปต้องเริ่มจากระบบงบประมาณ'"
5. **Prepositional:** "ภายใต้กฎหมายฉบับใหม่ หน่วยงานต้อง…"

**เกณฑ์ผ่าน:** ใน 10 ประโยคติดต่อกัน อย่างน้อย 3 ต้องเปิดด้วยรูปแบบที่ไม่ใช่ประธาน-กริยา

#### Step 1.4: ปรับ Paragraph Architecture

1. หากมีย่อหน้ายาวเท่ากันมากกว่า 3 ย่อหน้าติดกัน → แตกย่อหน้าหนึ่งให้สั้น 2 ประโยค
2. หากทุกย่อหน้าเปิดด้วย topic sentence → เปลี่ยนหนึ่งย่อหน้าให้เปิดด้วย anecdote
3. ทำให้มีย่อหน้าอย่างน้อย 3 ขนาด (สั้น 2–3 / กลาง 4–6 / ยาว 7+)

#### Step 1.5: ตรวจ Burstiness ใหม่ (Pass 1 Exit Criteria)

- ✅ ทุกย่อหน้ามี SD ≥ 5
- ✅ Sentence Opening Variability ผ่าน
- ✅ Paragraph Length มีอย่างน้อย 3 ขนาด

**หาก Pass 1 ผ่าน → ดำเนินการ Pass 2**

### 9.3 PASS 2: VOCABULARY CORRECTION / รอบที่ 2 แก้คำศัพท์

#### Step 2.1: Search & Replace AI Footprints (8 หมวด ตามลำดับ)

1. Tier 1 English Verbs
2. Tier 1 English Adjectives
3. Tier 1 English Nouns
4. AI Phrase Templates
5. คำเปิดประโยคไทย
6. คำขยายไทยพร่ำเพรื่อ
7. คำเชื่อมไทยซ้ำ
8. Hedging ซ้ำ

#### Step 2.2: Replace ตามตาราง — แต่ใช้ Voice Profile เป็นแนว

**สำคัญที่สุด:**
- อ้างอิง **Voice Profile** ที่ Calibrated แล้วใน Step 3 ของ 8-Step
- **Voice Profile บอกว่าผู้เขียนใช้คำใดเป็นหลัก** (จาก Dimension 2 — Vocabulary Signature)
- คำแทนที่ในตาราง Tier 1 เป็น **กรอบ** ใช้ Voice Profile เลือกคำที่ตรง "สำเนียงสาขา"

**ตัวอย่าง (Tier 1: "leverage"):**

| Voice Profile | คำแทนที่ที่ตรง |
|---|---|
| Academic Thai PhD (PA) | "อาศัย" / "ใช้กลไก" |
| Government Thai Official | "อาศัยอำนาจตาม" |
| Business B2B CFO | "use" / "apply" |
| Marketing Thai B2C | "นำ X มาช่วย" |

#### Step 2.3: ระวัง Symptom Substitution

**❌ ห้าม:** เปลี่ยนคำ AI เป็นคำ AI อีกคำ

| ❌ Wrong | ✅ Right |
|---|---|
| comprehensive → robust | comprehensive → "covers procurement, AP, AR" |
| leverage → utilize | leverage → "use" หรือระบุที่ใช้เฉพาะ |
| ขับเคลื่อน → ผลักดัน | ขับเคลื่อน → "ลดต้นทุน 18% ใน 6 เดือน" |
| อย่างยั่งยืน → อย่างต่อเนื่อง | อย่างยั่งยืน → "ตลอด 5 ปี" |

#### Step 2.4: เพิ่ม Specificity

ทุกคำขยายเชิงนามธรรมที่ลบออก ต้องเปลี่ยนเป็นรายละเอียดเชิงรูปธรรม:

| คำคลุมเครือ | คำเฉพาะเจาะจง |
|---|---|
| "หลายมิติ" | "ในด้านการเงิน บุคลากร และเทคโนโลยี" |
| "หลากหลาย" | "ทั้ง 5 หน่วยงาน — กระทรวงการคลัง กรมบัญชีกลาง สรรพากร ศุลกากร และสำนักงบฯ" |
| "อย่างต่อเนื่อง" | "ตั้งแต่ปี 2562 ถึงปัจจุบัน" |
| "อย่างมีประสิทธิภาพ" | "ลด cycle time จาก 14 วันเหลือ 4 วัน" |
| "comprehensive solution" | "modules covering AP, AR, GL, and FA" |

**Pass 2 Exit Criteria:**
- ✅ Tier 1 word density ผ่านเกณฑ์ภาค 4.1.3
- ✅ ไม่มี Symptom Substitution
- ✅ ทุกคำคลุมเครือถูกแทนด้วยรายละเอียด
- ✅ คำที่เลือกแทนตรงกับ Voice Profile

### 9.4 ADVANCED CORRECTION TECHNIQUES / 4 เทคนิคขั้นสูง

ใช้เสริมหลัง Pass 1+2 ผ่านแล้ว เมื่อ AI score ยังสูง

#### Technique A: Sentence Combining & Splitting

- รวมประโยคสั้น 2 ประโยคเป็นประโยคยาวซับซ้อน
- แยกประโยคยาว 1 ประโยคเป็นประโยคสั้น 2–3 ประโยค

#### Technique B: Insert Personal/Cultural Markers

**สำหรับงานราชการและวิชาการไทย:**
- "ตาม พ.ร.บ.การจัดซื้อจัดจ้าง พ.ศ. 2560 มาตรา 8 (3)…"
- "จากการสำรวจ 245 หน่วยงานในปี 2566 พบว่า 67%…"
- "อ้างถึงหนังสือกระทรวงการคลัง ที่ กค 0405.4/ว.123…"
- "ในไตรมาส 4 ของปีงบประมาณ ก่อนกันเงินเหลื่อมปี…"

**สำหรับงาน Business / Marketing:**
- "เมื่อบริษัท Bangchak Corporation เปิดใช้ระบบ…"
- "CFO บอกในที่ประชุมว่า 'ถ้าไม่ลด close cycle 5 วัน เราไม่ต่อ'"
- "ROI 247% ใน 18 เดือน, payback 7.4 เดือน"

#### Technique C: Aside & Qualification

- แทรกข้อสังเกตหรือข้อจำกัดด้วย em dash
- "ระบบนี้ได้ผลดี — แม้จะมีข้อจำกัดในช่วงแรก — ในที่สุดก็ยอมรับ"

> **ข้อจำกัดภาษาไทย:** Em dash ใช้ไม่เกิน 1 ครั้งต่อ 300 คำ

#### Technique D: Imperfect Flow

- ห้ามใช้ "นอกจากนี้/อีกทั้ง" ทุกย่อหน้า — สูงสุด 1 ครั้งต่อ 1,000 คำ
- ปล่อยให้บางย่อหน้าเริ่มแบบ abrupt
- บางครั้งจบแบบ "ปลายเปิด"

### 9.5 Two-Pass Method Visual Summary

```
┌─────────────────────────────────────────────────────────────────┐
│              AI CORRECTION PROTOCOL — TWO-PASS METHOD            │
│              (ภายใน Step 6 ของ 8-Step Master Workflow)            │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  Draft (after Detection 3-Layer in Step 5)                      │
│  + Voice Profile (from Step 3)                                  │
│         ↓                                                       │
│  ┌────────────────────────────────────────────────┐             │
│  │  PASS 1: RHYTHM CORRECTION (5 Steps)            │             │
│  │  1.1: ระบุย่อหน้าเสี่ยง                          │             │
│  │  1.2: Burstiness Injection                      │             │
│  │  1.3: Diversify Sentence Openings (5 รูปแบบ)    │             │
│  │  1.4: Adjust Paragraph Architecture            │             │
│  │  1.5: Verify SD ≥ 5                            │             │
│  └────────────────────────────────────────────────┘             │
│         ↓ (Pass 1 ผ่าน)                                         │
│  ┌────────────────────────────────────────────────┐             │
│  │  PASS 2: VOCABULARY CORRECTION (4 Steps)         │             │
│  │  2.1: Search & Replace 8 หมวด                    │             │
│  │  2.2: Replace by VOICE PROFILE (จาก Step 3)      │             │
│  │  2.3: Avoid Symptom Substitution                │             │
│  │  2.4: Add Specificity                           │             │
│  └────────────────────────────────────────────────┘             │
│         ↓ (ถ้า AI score ยังสูง)                                │
│  ┌────────────────────────────────────────────────┐             │
│  │  ADVANCED TECHNIQUES (เลือกใช้)                  │             │
│  │  A. Sentence Combining & Splitting              │             │
│  │  B. Personal/Cultural Markers                   │             │
│  │  C. Aside & Qualification                       │             │
│  │  D. Imperfect Flow                              │             │
│  └────────────────────────────────────────────────┘             │
│         ↓                                                       │
│  Re-Detection (return to Step 5)                                │
│         ↓                                                       │
│  Voice Match Scoring (Step 7)                                   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 10. AI CORRECTION TECHNIQUES CATALOG (12 TECHNIQUES) / แค็ตตาล็อกเทคนิค 12 รายการ

ภาคนี้คือ catalog เทคนิครายตัว — อ้างอิงควบคู่กับ Two-Pass Protocol

### Technique 1: Personal Anchor Injection (Pass 2 + Layer 3 Check 8)

เพิ่มชื่อจริง วันที่จริง สถานที่จริง ตัวเลขจริง เรื่องเล่าส่วนตัว

*Before:* "Companies that invest in digital transformation typically see significant improvements in operational efficiency."

*After:* "When Bangchak Corporation rolled out Oracle Cloud ERP in Q2 2024, monthly close time fell from 11 working days to 4."

### Technique 2: Burstiness Injection (Pass 1.2 + Layer 2 Check 1)

สลับประโยคยาว (25+ คำ) กับประโยคสั้น (3–7 คำ)

### Technique 3: Sentence Opening Diversification (Pass 1.3 + Layer 2 Check 2)

สลับเปิดประโยคด้วย 5 รูปแบบ (Adverb / Subordinate / Question / Quote / Prepositional)

### Technique 4: Tier 1 Vocabulary Detoxification (Pass 2.1 + Layer 1)

แทน Tier 1 vocabulary ตามตาราง — ปรับโครงสร้างประโยค ไม่ใช่แทน 1:1

### Technique 5: List Asymmetry (Pass 1.4 + Layer 2 Check 5)

เปลี่ยนรายการ 3 ข้อสมมาตรเป็น 2, 4, หรือ 5 ข้อ ที่ความยาวต่างกัน

### Technique 6: Voice Particularization (Pass 2.2 + Layer 3 Check 8)

เลือกคำตาม Voice Profile (Dimension 2 — Vocabulary Signature)

### Technique 7: Counterargument Insertion (Layer 3 Check 8 + Advanced C)

แทรกการโต้แย้งหรือข้อจำกัด

### Technique 8: Citation Specification (Pass 2.4 + Layer 3 Check 7)

ระบุ citation เฉพาะ ไม่ใช่ "งานวิจัยพบว่า"

### Technique 9: Idiom and Register Shift (Pass 2.2 + Thai-Specific)

ใช้สำนวนเฉพาะอาชีพตาม Voice Profile (Dimension 6)

### Technique 10: Asymmetric Information Density (Pass 1.4 + Layer 3 Check 6)

ย่อหน้าหนึ่งลึก ย่อหน้าถัดไปสั้นเป็นข้อสังเกต

### Technique 11: Question Embedding (Pass 1.3 + Layer 2 Check 2)

แทรกคำถามวาทศิลป์ 1 ครั้งต่อ 500 คำ

### Technique 12: Cultural and Temporal Specificity (Pass 2.4 + Advanced B)

ระบุช่วงเวลา ฤดูกาล เหตุการณ์ปัจจุบัน บริบทวัฒนธรรม

### 10.1 Anti-Patterns to Avoid

- จงใจสะกดผิด — Turnitin 2026 จับได้
- ใส่ typo
- แทนคำด้วย thesaurus แบบสุ่ม (Symptom Substitution)
- ใช้ humanizer tool อัตโนมัติ
- เพิ่ม filler เพื่อหลอก burstiness
- รัน Pass 1 และ Pass 2 พร้อมกัน
- **เขียนโดยไม่อ้าง Voice Profile** ⭐ ใหม่ใน V04R01

---

## 11. VOICE/WRITING MATCH SCORING & MEMORY STORAGE / การให้คะแนนตรงเสียงและบันทึก

ภาคนี้คือรายละเอียด **Step 7 และ Step 8** ของ 8-Step Master Workflow

### 11.1 Why Score the Match / ทำไมต้องให้คะแนน

หลังการ humanize เสร็จ ต้องตอบคำถาม 2 ข้อ:

1. **ผ่าน Detector หรือไม่?** → AI Detection Score (Step 5/6)
2. **ตรงเสียงผู้เขียนหรือไม่?** → Voice Match Score (Step 7) ⭐

**ปัญหาที่ Voice Match ป้องกัน:**
- งานผ่าน detector แต่อ่านแล้วไม่เหมือนเสียงผู้เขียน
- ผู้อ่าน peer ของผู้เขียนสังเกตได้ทันทีว่า "ไม่ใช่สำเนียงของเขา"
- ในงานวิชาการ — committee อาจตั้งคำถามถึงความเป็นเจ้าของงาน

### 11.2 Scoring Methodology per Dimension / วิธีให้คะแนนรายมิติ

วัดแต่ละมิติของ Voice Profile (ภาค 8.3) เทียบกับฉบับสุดท้าย

#### Dimension 1 Score: Sentence-Level Match

**วิธีคำนวณ:**
- เปรียบเทียบ Mean sentence length (target ±15%)
- เปรียบเทียบ SD (target ±20%)
- เปรียบเทียบ Distribution of short/medium/long (target ±10%)

**คะแนน:** 0–100% — ใช้ค่าเฉลี่ยเรขาคณิตของทั้ง 3 ตัวชี้วัด

#### Dimension 2 Score: Vocabulary Match

- ตรวจ Top 30 คำเฉพาะของ Profile ปรากฏในฉบับสุดท้ายกี่ครั้ง
- ตรวจคำที่ Profile ระบุว่า "Avoided" ปรากฏหรือไม่
- คะแนน = (คำที่ตรง / คำที่ควรมี) × 100% − (คำที่ห้ามใช้ × penalty)

#### Dimension 3 Score: Paragraph Architecture Match

- เปรียบเทียบ Mean paragraph length, Opening pattern, Closing pattern
- คะแนน = average match across 3 sub-metrics

#### Dimension 4 Score: Argumentation Match

- ตรวจ Claim style, Evidence per claim, Counterargument handling
- คะแนน = average match

#### Dimension 5 Score: Citation Match

- ตรวจ Citation density, Position, Style
- คะแนน = average match

#### Dimension 6 Score: Cultural & Contextual Match

- ตรวจ Thai context references, Cultural register, Profession-specific phrases
- คะแนน = average match

#### Dimension 7 Score (Academic Intensive Only)

- ตรวจ Hedging norms, First-person, Methodology language
- คะแนน = average match

### 11.3 Overall Match Score Formula / สูตรคะแนนรวม

**Standard Mode (Dimensions 1–6):**
```
Overall Match = (D1 × 0.20) + (D2 × 0.25) + (D3 × 0.15) + (D4 × 0.15)
              + (D5 × 0.10) + (D6 × 0.15)
```

**Intensive Mode (Dimensions 1–7, สำหรับงานวิชาการ):**
```
Overall Match = (D1 × 0.18) + (D2 × 0.22) + (D3 × 0.13) + (D4 × 0.13)
              + (D5 × 0.10) + (D6 × 0.12) + (D7 × 0.12)
```

**น้ำหนัก:** Vocabulary (D2) มีน้ำหนักสูงสุด เพราะเป็นลายนิ้วมือชัดที่สุดของ stylometry

### 11.4 Pass/Fail Threshold / เกณฑ์ผ่าน

| ระดับงาน | เกณฑ์ผ่าน Voice Match |
|---|---|
| งานวิชาการระดับวารสารนานาชาติ | ≥ 85% |
| วิทยานิพนธ์ ดุษฎีนิพนธ์ | ≥ 80% |
| Business proposal ระดับ Executive | ≥ 75% |
| งานราชการ | ≥ 75% |
| Marketing content | ≥ 70% |

**ถ้าไม่ผ่าน:** ย้อน Step 6 ระบุมิติที่ตกเกณฑ์ → แก้เฉพาะส่วนนั้นใน Pass 2 (โดยอ้าง Voice Profile ใหม่)

### 11.5 Voice/Writing Match Scoring Report Template

```
═══════════════════════════════════════════════════════
🎯 VOICE/WRITING MATCH SCORING REPORT
═══════════════════════════════════════════════════════
Document ID:           [Doc-ID]
Voice Profile ID:      VP-[YYYYMMDD]-[XXX]
Date:                  [YYYY-MM-DD]
Mode:                  ☐ Standard  ☐ Intensive (Academic)

─────────────────────────────────────────────────────
DIMENSIONAL SCORES
─────────────────────────────────────────────────────
D1 Sentence-Level:        [XX]%  (target: ≥75%)
D2 Vocabulary:            [XX]%  (target: ≥80%)
D3 Paragraph:             [XX]%  (target: ≥70%)
D4 Argumentation:         [XX]%  (target: ≥70%)
D5 Citation:              [XX]%  (target: ≥75%)
D6 Cultural:              [XX]%  (target: ≥70%)
D7 Disciplinary [Acad]:   [XX]%  (target: ≥80%)

─────────────────────────────────────────────────────
OVERALL MATCH SCORE
─────────────────────────────────────────────────────
Calculated:    [XX.X]%
Threshold:     [≥X]% (per use case)
Status:        ☐ ผ่าน  ☐ ไม่ผ่าน

─────────────────────────────────────────────────────
DIMENSION-LEVEL FINDINGS
─────────────────────────────────────────────────────
Strongest match:   [Dimension X] — [reason]
Weakest match:     [Dimension Y] — [reason]
Recommendations:   [actionable steps to improve weak dimension]

═══════════════════════════════════════════════════════
DECISION
═══════════════════════════════════════════════════════
☐ PASS → ดำเนินการ Step 8 (Storage)
☐ FAIL → ย้อน Step 6, แก้เฉพาะ Dimension [Y] โดยอ้าง Voice Profile
═══════════════════════════════════════════════════════
```

### 11.6 Memory Storage (Step 8 Detail) / การจัดเก็บความจำ

**สิ่งที่ต้องบันทึก:**

1. **Final Document** — ในตำแหน่งที่ผู้ใช้กำหนด (เช่น 20-Output/ ใน Project Mode)
2. **Voice Profile (Updated)** — ถ้ามีการเรียนรู้ใหม่ → V01R02 ของ Profile
3. **Memory Index Entry:**

```
═══════════════════════════════════════════════════════
📂 MEMORY INDEX ENTRY
═══════════════════════════════════════════════════════
Document ID:           [Doc-ID]
Title:                 [ชื่อเอกสาร]
Author/Persona:        [ชื่อ]
Version:               V[##]R[##]
Date:                  [YYYY-MM-DD]
Voice Profile Used:    VP-[YYYYMMDD]-[XXX]
Voice Profile Version: V[##]R[##]

AI Detection Score:    [XX]% (Final)
Voice Match Score:     [XX]% (Final)

Lessons Learned:
- [ปัญหาที่พบในกระบวนการ]
- [วิธีแก้ที่ใช้]
- [ข้อสังเกตสำหรับครั้งต่อไป]

Stored Path:           [path]
═══════════════════════════════════════════════════════
```

4. **Disclosure (ถ้าจำเป็น)** — แนบตามภาค 14

### 11.7 Learning Loop / วงจรการเรียนรู้

แต่ละครั้งที่ใช้งาน Skill นี้ Voice Profile จะปรับปรุงให้แม่นขึ้น:

```
ครั้งที่ 1 → สกัด Profile V01R01 → ใช้แก้งาน → ปรับ Profile V01R02
ครั้งที่ 2 → ใช้ Profile V01R02 → ใช้แก้งาน → ปรับ Profile V01R03
...
ครั้งที่ N → Profile แม่นยำตรงเสียงผู้เขียนสูงสุด (mature profile)
```

---

# PART 4 — APPLICATION & QUALITY ASSURANCE / การประยุกต์และประกันคุณภาพ

## 12. USE CASE SPECIFIC GUIDANCE / แนวปฏิบัติเฉพาะบริบท

### 12.1 Academic Writing / งานเขียนวิชาการ

**Acceptable scores:**
- AI Score: ≤ 5–10% (วารสารนานาชาติ Q1–Q2), ≤ 10–20% (TCI), ≤ 20% (วิทยานิพนธ์ตามสถาบัน)
- Voice Match: ≥ 80% (วิทยานิพนธ์), ≥ 85% (วารสารนานาชาติ)

**Critical practices:**
1. **Intensive Mode Voice Profile** — ใช้ Dimension 7 (Disciplinary Conventions)
2. AI ห้ามใช้ในการตีความข้อมูลและการวิเคราะห์
3. ทุก citation ตรวจสอบ DOI
4. บทคัดย่อเขียนใหม่ด้วยมือ
5. ใช้ "ผู้วิจัย" + APA นาม-ปี + ศัพท์ราชบัณฑิตยสภา
6. ระบุ AI Disclosure ใน Methods/Acknowledgments
7. **Two-Pass Method:** Pass 1 ปรับ rhythm + Pass 2 ใช้ Disciplinary Voice Profile

### 12.2 Business / Sales / Proposal

**Acceptable scores:**
- AI Score: ≤ 20–30%
- Voice Match: ≥ 75%

**Critical practices:**
1. **Voice Profile** — ใช้ "B2B CFO" หรือ "Sales Pursuit" Profile
2. Customer-specific data ทุกย่อหน้า
3. หลีกเลี่ยง generic value proposition
4. ใช้คำที่ลูกค้าใช้
5. Two-Pass Method: Pass 2 ใช้ Voice Profile แบบ executive

### 12.3 Government Documents

**Acceptable scores:**
- AI Score: ≤ 15% (เอกสารทางการ), ≤ 20% (รายงาน)
- Voice Match: ≥ 75%

**Critical practices:**
1. **Voice Profile** — ใช้ "Government Thai Official" Profile (Cultural Dimension 6 หนักมาก)
2. ใช้ภาษาราชการตามระเบียบฯ พ.ศ. 2526
3. ระบุระเบียบและกฎหมายอ้างอิงครบ
4. หลีกเลี่ยงคำตลาด ("ขับเคลื่อน" "ยกระดับ")
5. ตำแหน่งและหน่วยงานเต็มยศ
6. Two-Pass Method + Advanced Technique B (Personal/Cultural Markers)

### 12.4 Marketing / Content / Communication

**Acceptable scores:**
- AI Score: ≤ 20% (blog), ≤ 30% (LinkedIn)
- Voice Match: ≥ 70%

**Critical practices:**
1. **Voice Profile** — ใช้ "Marketing B2C" หรือ "Thought Leadership" Profile
2. Hook 50–100 คำแรกเขียนด้วยมือ
3. First-person voice with concrete experience
4. หลีกเลี่ยง LinkedIn-style AI patterns
5. Two-Pass Method: Pass 1 เน้น Step 1.3 (Sentence Opening)

---

## 13. QUALITY ASSURANCE CHECKLIST / รายการตรวจคุณภาพ

### 13.1 Pre-Submission Checklist (Universal)

```
[ ] ผ่าน 8-Step Master Workflow ครบทุก Step
[ ] Voice Profile สกัดและ Calibrated แล้ว (Step 3)
[ ] AI score อยู่ภายใต้เกณฑ์ของสถาบัน
[ ] ผ่าน 3-Layer Self-Check
[ ] ผ่าน Two-Pass Method (Pass 1 + Pass 2 ไม่ทำพร้อมกัน)
[ ] Voice Match Score ≥ เกณฑ์ของบริบท
[ ] ทุกย่อหน้ามี personal anchor หรือ specific evidence
[ ] ไม่มี Tier 1 vocabulary เกินเกณฑ์
[ ] ทุกการอ้างอิงตรวจสอบแล้ว
[ ] ตัวเลข ชื่อ วันที่ ตรวจสอบแล้ว
[ ] อ่านออกเสียงแล้วฟังดูเป็นมนุษย์ + เป็นเสียงผู้เขียน
[ ] มีอย่างน้อย 1 counterargument
[ ] AI Disclosure ระบุครบ
[ ] Version ระบุชัด (V##R##)
[ ] Memory Index Entry บันทึกแล้ว
```

### 13.2 Academic-Specific QA

```
[ ] ทุก citation ตรวจ DOI/แหล่งจริง
[ ] APA/Chicago/Vancouver ถูกต้อง
[ ] บทคัดย่อเขียนด้วยมือ
[ ] ใช้ "ผู้วิจัย" ไม่ใช่ "เรา"
[ ] ใช้ศัพท์ราชบัณฑิตยสภา
[ ] ระบุ AI ใน Methods/Acknowledgments
[ ] ตรวจ plagiarism ผ่าน Turnitin/iThenticate
[ ] Voice Profile Intensive Mode (Dimension 7) ใช้แล้ว
[ ] Voice Match ≥ 80–85%
```

### 13.3 Business/Sales QA

```
[ ] ข้อมูลเฉพาะลูกค้าทุกย่อหน้า
[ ] Value proposition เป็นตัวเลขผลลัพธ์
[ ] ใช้คำที่ลูกค้าใช้
[ ] CTA เฉพาะเจาะจง
[ ] ผู้อนุมัติทบทวนแล้ว
[ ] Voice Match ≥ 75%
```

### 13.4 Government QA

```
[ ] ระเบียบ/กฎหมายอ้างอิงครบ
[ ] คำขึ้นต้น/ลงท้ายตามระเบียบ
[ ] ราชาศัพท์ถูกต้อง
[ ] ตำแหน่งและหน่วยงานเต็มยศ
[ ] ผ่านการตรวจสอบฝ่ายกฎหมาย
[ ] เตรียมรับมาตรฐาน AI labeling
[ ] Voice Match ≥ 75%
```

### 13.5 Marketing QA

```
[ ] Hook 50–100 คำแรกเขียนด้วยมือ
[ ] First-person voice + concrete example
[ ] SEO keywords natural
[ ] CTA เฉพาะเจาะจง
[ ] Brand voice (Voice Profile) สอดคล้อง
[ ] Voice Match ≥ 70%
```

---

# PART 5 — GOVERNANCE / การกำกับดูแล

## 14. ETHICAL FRAMEWORK / กรอบจริยธรรม

### 14.1 Three Ethical Categories

**A. Acceptable AI Assistance**
- ระดมความคิด สร้าง outline เบื้องต้น
- ขัดเกลาไวยากรณ์และน้ำเสียง
- สรุปงานวิจัยที่ผู้เขียนอ่านแล้ว
- ช่วยแปลและตรวจการแปล
- สร้าง first draft ที่ผู้เขียนแก้ทั้งหมดด้วย Two-Pass Method และตาม Voice Profile

**B. Conditional AI Assistance (ต้องเปิดเผย)**
- AI สร้างเนื้อหาทั้งหมด ผู้เขียนแก้เฉพาะภาษา
- AI วิเคราะห์ข้อมูล
- AI สร้างภาพ/infographic

**C. Unacceptable AI Use**
- AI เขียนวิทยานิพนธ์ทั้งหมดและส่งโดยไม่ระบุ
- AI สร้าง citation ปลอม
- AI สร้างข้อมูลวิจัยปลอม
- AI ในการสอบ
- AI สร้างคำให้สัมภาษณ์ในนามบุคคลที่ไม่ทราบ

### 14.2 Disclosure Templates

**Academic (English):**
> "ChatGPT (GPT-4, OpenAI) was used to assist in language polishing and outline generation. All analytical reasoning, data interpretation, and conclusions were developed by the author(s). A Voice Profile was extracted from the author's prior published work to ensure stylistic consistency. Citations were independently verified."

**Academic (Thai):**
> "ผู้วิจัยใช้ ChatGPT (GPT-4, OpenAI) ในการช่วยขัดเกลาภาษาและจัดทำโครงร่างเบื้องต้น โดยใช้ Voice Profile ที่สกัดจากงานเขียนของผู้วิจัยเองเพื่อรักษาความสม่ำเสมอของสำเนียง การวิเคราะห์ การตีความ และข้อสรุปทั้งหมด ผู้วิจัยเป็นผู้พัฒนาขึ้นเอง การอ้างอิงทุกชิ้นได้ตรวจสอบความถูกต้องอย่างเป็นอิสระ"

### 14.3 Regulatory Context (2026)

- **EU AI Act (สิงหาคม 2569):** AI-generated content ต้อง machine-readable + ฉลากมองเห็นสำหรับ deepfake/public-interest text
- **Thailand Draft AI Act:** ETDA รับฟังความเห็น 2568 — กรอบจำแนกความเสี่ยงแบบ EU
- **เตรียมรับ AI labeling** ในเอกสารสาธารณะ

### 14.4 Red Lines

- ไม่สร้างข้อมูล ตัวเลข citation ปลอม
- ไม่อ้างความเห็นของบุคคลจริงเท็จ
- ไม่ส่งงานผู้อื่นที่ปรับด้วย AI โดยอ้างเป็นของตน
- ไม่ใช้ AI ในบริบทที่กฎหมายห้าม
- **ไม่สกัด Voice Profile จากงานผู้อื่นโดยไม่ได้รับอนุญาต** ⭐ ใหม่ใน V04R01

---

## 15. COMMON PITFALLS & FALSE POSITIVES / ข้อผิดพลาดที่พบบ่อย

### 15.1 False Positive Triggers

1. Non-native English writing
2. Highly formal academic writing
3. Technical or legal writing
4. Corporate boilerplate
5. Translation from another language
6. Thai government documents
7. **Voice Profile ที่สกัดจาก corpus เล็กเกินไป** ⭐ ใหม่

**Mitigation:**
- ใช้เครื่องมือ cross-validate
- เก็บ draft history
- Voice Profile ขั้นต่ำ 5 docs / 30,000 words
- หากถูก flag ผิด ขออุทธรณ์โดยแสดงหลักฐาน 8-Step process

### 15.2 Common Correction Mistakes

1. **Symptom Substitution** (กฎใน Pass 2 Step 3)
2. Adding Typos
3. Over-Humanization
4. Removing All AI Help
5. Trusting Humanizer Tools Blindly
6. Running Pass 1 + Pass 2 Together
7. **เขียนโดยไม่อ้าง Voice Profile** ⭐ ใหม่
8. **Voice Profile สกัดผิดเพราะข้าม Calibration (Step 3)** ⭐ ใหม่

### 15.3 Edge Cases

**Short Texts (<300 words):**
- Detector ไม่แม่น
- Voice Profile ใช้ได้แต่ Match Score มี variance สูง

**Code-Like Content:**
- Detector มัก false positive
- ใช้ภาษามนุษย์ในส่วน explanation

**Translation Workflows:**
- AI แปลมักถูกจับ
- ปรับสำนวนหลังแปลด้วย Two-Pass

**Author with No Prior Work:**
- ไม่มีฐานสกัด Voice Profile
- Fallback: ใช้ Pre-defined Profile (Level 4) + ขอ user calibration อย่างเข้ม

---

# PART 6 — OPERATIONALIZATION / การปฏิบัติ

## 16. PROMPT TEMPLATES FOR DETECTION, VOICE EXTRACTION & CORRECTION / แม่แบบคำสั่ง

### 16.1 Detection Prompts

**Prompt D1: 3-Layer Self-Detection Audit (English/Thai)**
```
Analyze the following text using the 3-Layer Detection Methodology.

LAYER 1 — Vocabulary Footprints: List all Tier 1 words/phrases.
LAYER 2 — Statistical Patterns: 5 Checks (Burstiness, Opening, Symmetry, Transition, Bullet-thinking).
LAYER 3 — Structural Patterns: 3 Checks (Paragraph length, Citation, Voice Markers).

Output as AI Detection Self-Check Report (template in section 6).

Text: <<<TEXT>>>
```

### 16.2 Voice Profile Extraction Prompts ⭐ NEW

**Prompt V1: Voice Profile Extraction (Standard Mode)**
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
Voice Profile Output Template (section 8.5).

Reference documents: <<<DOCS>>>
Author/Persona: <<<NAME>>>
Context: <<<ACADEMIC/BUSINESS/GOVERNMENT/MARKETING>>>

Output:
1. Complete Voice Profile filling all 6 dimensions
2. Profile ID assignment (VP-[YYYYMMDD]-[XXX])
3. 3 Calibration sample paragraphs (different topics) for user verification
```

**Prompt V2: Voice Profile Extraction (Intensive Academic Mode)**
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

**Prompt V3: Voice Profile Calibration**
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

### 16.3 Two-Pass Correction Prompts

**Prompt C-Pass1: Rhythm Correction Only**
```
Apply ONLY Pass 1: Rhythm Correction to the text below.
DO NOT modify vocabulary in this pass.

Step 1.1: Identify at-risk paragraphs
Step 1.2: Burstiness Injection (shorten 2 / expand 1 per paragraph)
Step 1.3: Diversify openings (Adverb / Subordinate / Question / Quote / Prepositional)
Step 1.4: Adjust paragraph architecture
Step 1.5: Verify SD ≥ 5

CONSTRAINTS: Do NOT replace vocabulary. Do NOT invent facts.

Source facts: <<<FACTS>>>
Text: <<<TEXT>>>

Output: Pass 1 text + Burstiness report + Sentence opening report
```

**Prompt C-Pass2: Vocabulary Correction with Voice Profile**
```
Apply ONLY Pass 2: Vocabulary Correction to the text below.
The text passed Pass 1 — DO NOT alter rhythm.

VOICE PROFILE (mandatory): <<<VOICE_PROFILE>>>

Step 2.1: Search & Replace by 8 categories (in order):
  1. English Verbs / 2. English Adjectives / 3. English Nouns
  4. AI Phrases / 5. Thai openers / 6. Thai modifiers
  7. Thai connectives / 8. Hedging
Step 2.2: Choose replacements per VOICE PROFILE Dimension 2
Step 2.3: Avoid Symptom Substitution
Step 2.4: Add Specificity (replace vague modifiers with concrete data)

CONSTRAINTS: Do NOT alter rhythm. Do NOT invent facts.

Source facts: <<<FACTS>>>
Text (Pass 1-corrected): <<<TEXT>>>

Output: Pass 2 text + Vocabulary log + Specificity log
```

### 16.4 Voice Match Scoring Prompt ⭐ NEW

**Prompt M1: Voice Match Scoring**
```
Score the match between the Final Document and the Voice Profile.

Apply the formula in section 11.3:
Standard Mode: D1×0.20 + D2×0.25 + D3×0.15 + D4×0.15 + D5×0.10 + D6×0.15
Intensive: D1×0.18 + D2×0.22 + D3×0.13 + D4×0.13 + D5×0.10 + D6×0.12 + D7×0.12

Voice Profile: <<<PROFILE>>>
Final Document: <<<DOC>>>
Mode: <<<STANDARD/INTENSIVE>>>

Output: Voice/Writing Match Scoring Report (template in section 11.5)
+ specific recommendations to improve the weakest dimension
```

### 16.5 Combined Full-Cycle Prompt ⭐ NEW

**Prompt FC1: Full 8-Step Cycle**
```
Execute the full 8-Step Sequential Thinking Master Workflow.

Inputs:
- Document Type: <<<TYPE>>>
- Author/Persona: <<<NAME>>>
- Reference Documents: <<<DOCS>>>
- Source Material (facts/data): <<<FACTS>>>
- Target AI Score: < <<<X>>>%
- Target Voice Match: ≥ <<<Y>>>%
- Mode: <<<STANDARD/INTENSIVE>>>

Steps (execute in order; do NOT skip):
1. Voice Source Selection — confirm sources
2. Voice Profile Extraction (6-Dim or 7-Dim if Intensive)
3. Calibration & Memory — produce 3 samples for verification
4. Write First Draft — using Voice Profile + KB guidance
5. AI Detection Self-Check — 3-Layer Methodology
6. Two-Pass Correction — Pass 1 then Pass 2 (with Voice Profile)
7. Voice Match Scoring — apply formula, return per-dimension report
8. Storage & Memory — output Memory Index Entry

Output for each step: deliverable + decision (proceed/iterate)
Final output: Final Document + Voice Profile (calibrated) + Reports
```

### 16.6 Specialized Use-Case Prompts

**Prompt C2-Academic (Thai/EN):**
```
Apply Two-Pass Method to academic text targeting [Journal Standard],
using Voice Profile (Intensive Mode with D7).

Voice Profile: ผู้วิจัย Ph.D. สาขา [field], ภาษาไทยวิชาการ, APA นาม-ปี

Pass 1: Rhythm — สลับประโยคยาวอภิปราย กับประโยคสั้นสรุป
Pass 2: Vocabulary —
   - "เรา" → "ผู้วิจัย"
   - "งานวิจัยพบว่า" → "[ชื่อ] ([ปี]) พบว่า…"
   - ตามตาราง Tier 1 + Voice Profile

ห้ามสร้าง citation ปลอม
```

**Prompt C2-Business (Bilingual):**
```
Apply Two-Pass Method to proposal for [Customer] in Thailand,
using Voice Profile "B2B CFO."

Customer facts: <<<DATA>>>

Pass 1: open paragraphs with customer-specific observation
Pass 2: replace generic value props with quantified outcomes
       in customer's language

DO NOT invent customer detail. Flag as [INPUT NEEDED].
```

**Prompt C2-Government (Thai):**
```
ปรับเป็นภาษาราชการตามระเบียบฯ พ.ศ. 2526
ใช้ Two-Pass + Voice Profile "Government Thai Official"

Pass 1: Rhythm — รูปแบบหนังสือราชการ (ด้วย…/ตามที่… → จึงเรียนมาเพื่อ…)
Pass 2: Vocabulary —
   - แทนคำตลาด ("ขับเคลื่อน" "ยกระดับ" "ปลดล็อก")
   - เพิ่ม Personal/Cultural Markers (มาตรา ระเบียบ หนังสือสั่งการ)

ห้ามสร้างเลขที่หนังสือ มาตรา ระเบียบที่ไม่มีจริง
```

**Prompt C2-Marketing:**
```
Apply Two-Pass to marketing copy [Channel]/[Audience],
using Voice Profile "Marketing Thought Leadership"

Pass 1: First 50 words must hook with story/stat/observation
        Sentence opening: alternate question/quote/anecdote
Pass 2:
  - Eliminate Tier 1 AI vocabulary
  - Eliminate "Here's what I learned…", "Let me share a story…"
  - SEO keyword <<<KEYWORD>>>: natural, not stuffed

User's actual experience: <<<INPUT>>>
```

---

## 17. SKILL DESIGN IMPLICATIONS / นัยสำหรับการออกแบบ Custom Skill

### 17.1 Recommended Skill Architecture

**Skill Name:** `ai-detection-correction`

**Description Triggers:** AI detection, AI correction, humanize AI, Two-Pass, Voice Profile, ตรวจ AI, แก้ไข AI, ทำให้ดูเป็นมนุษย์, ลด AI score, สกัดเสียงผู้เขียน, Voice Match, Turnitin, GPTZero, Originality, Copyleaks

**Skill Capabilities (4 Modes):**

**Mode 1 — Detection Only**
- Input: ข้อความ + บริบท
- Output: AI Detection Report
- Prompt: D1

**Mode 2 — Voice Profile Extraction Only** ⭐ NEW
- **Sub-Mode 2A:** Standard (6 Dimensions)
- **Sub-Mode 2B:** Intensive Academic (7 Dimensions)
- Input: Reference documents + author persona
- Output: Calibrated Voice Profile + Memory Entry
- Prompt: V1, V2, V3

**Mode 3 — Correction Only**
- **Sub-Mode 3A:** Pass 1 Only (Rhythm)
- **Sub-Mode 3B:** Pass 2 Only (Vocabulary + Voice Profile)
- **Sub-Mode 3C:** Two-Pass Combined
- Input: ข้อความ + Voice Profile + user facts
- Output: Corrected text + Pass logs + Match score
- Prompt: C-Pass1, C-Pass2, FC1

**Mode 4 — Full 8-Step Cycle**
- Input: All 8-Step inputs
- Output: Complete cycle deliverables + Memory Index Entry
- Prompt: FC1
- Iterates until target met

### 17.2 Required Reference Files

```
ai-detection-correction/
├── SKILL.md                              (main entry point)
├── references/
│   ├── 01_three_dimensions_framework.md  (ภาค 2)
│   ├── 02_tools_landscape_2026.md        (ภาค 3)
│   ├── 03_three_layer_methodology.md     (ภาค 4)
│   ├── 04_tier1_vocabulary_en.md         (ภาค 4.1.1)
│   ├── 05_tier1_vocabulary_th.md         (ภาค 4.1.2)
│   ├── 06_thai_specific_patterns.md      (ภาค 5)
│   ├── 07_8step_master_workflow.md       (ภาค 7) ⭐
│   ├── 08_voice_extraction_methodology.md (ภาค 8) ⭐
│   ├── 09_two_pass_protocol.md           (ภาค 9)
│   ├── 10_correction_catalog.md          (ภาค 10)
│   ├── 11_voice_match_scoring.md         (ภาค 11) ⭐
│   ├── 12_use_case_guidance.md           (ภาค 12)
│   ├── 13_qa_checklists.md               (ภาค 13)
│   ├── 14_ethical_framework.md           (ภาค 14)
│   └── 15_pitfalls.md                    (ภาค 15)
├── templates/
│   ├── detection_report_template.md      (ภาค 6)
│   ├── voice_profile_template.md         (ภาค 8.5) ⭐
│   ├── voice_match_scoring_template.md   (ภาค 11.5) ⭐
│   ├── memory_index_entry_template.md    (ภาค 11.6) ⭐
│   ├── prompt_d1_detection.md
│   ├── prompt_v1_voice_extraction.md     ⭐
│   ├── prompt_v2_voice_intensive.md      ⭐
│   ├── prompt_v3_voice_calibration.md    ⭐
│   ├── prompt_c_pass1_rhythm.md
│   ├── prompt_c_pass2_vocabulary.md
│   ├── prompt_m1_voice_scoring.md        ⭐
│   ├── prompt_fc1_full_cycle.md          ⭐
│   ├── prompt_c2_academic.md
│   ├── prompt_c2_business.md
│   ├── prompt_c2_government.md
│   └── prompt_c2_marketing.md
├── voice_profiles/                        ⭐ Pre-defined Library
│   ├── KM-TH-THESIS-DOC/                 🆕 V05R01 Thai Academic Library
│   │   └── KM-TH-THESIS-DOC_V02R01_2026-04-30.md  (7 Sub-Profiles + 6+1 Dimensions)
│   ├── academic_thai_phd.md              (placeholder — refer to KM-TH-THESIS-DOC VP-A1/A2)
│   ├── academic_international_q1.md      (to be created)
│   ├── business_b2b_cfo.md               (to be created)
│   ├── business_sales_proposal.md        (to be created)
│   ├── government_thai_official.md       (to be created)
│   ├── government_thai_policy.md         (to be created)
│   ├── marketing_thai_b2c.md             (to be created)
│   └── marketing_thought_leadership.md   (to be created)
├── memory/                                ⭐ NEW
│   ├── voice_profiles/                   (extracted profiles by user)
│   ├── document_index.md                 (Memory Index of all docs)
│   └── lessons_learned.md                (cumulative learning)
└── examples/
    ├── before_after_academic.md
    ├── before_after_business.md
    ├── before_after_government.md
    └── before_after_marketing.md
```

### 17.3 Skill Workflow (เมื่อถูกเรียก) — Aligned with 8-Step

1. **Step 1:** ถาม Mode/Sub-Mode + บริบท + Use Case + Language + Target Scores
2. **Step 2:** ถาม Voice Source — ไล่ตาม 5-Level Hierarchy
3. **Step 3:** สกัด Voice Profile (ถ้ายังไม่มี) → Calibrate → Save Memory
4. **Step 4:** ถาม User-provided facts (ป้องกัน hallucination)
5. **Step 5:** Load reference files ที่เกี่ยวข้อง
6. **Step 6:** Apply Prompt template — ตามขั้นตอน 8-Step
7. **Step 7:** Output ผลลัพธ์ + Detection + Voice Match + Memory Entry + Version
8. **Step 8:** เสนอ next step (iterate / save / explain / extract new profile)

### 17.4 Anti-Hallucination Safeguards

- **Mandatory Voice Source Selection** ก่อน extraction
- **Mandatory User Fact Input** ก่อน correction
- **Mandatory Voice Profile** ก่อน Pass 2
- **Calibration Required** ก่อน production (sample test)
- **Flag Missing Data** เป็น `[NEEDS USER INPUT]`
- **No Citation Generation** — ใช้เฉพาะที่ผู้ใช้ให้
- **Pass Separation Enforcement** — ไม่ให้รัน Pass 1+2 พร้อม
- **No Voice Profile Fabrication** — Level 5 = ASK, ห้ามเดา

### 17.5 Skill Boundaries

- ไม่ทำให้ข้อความหลีกเลี่ยง detector ในงานที่จริยธรรมห้าม
- ไม่สร้างข้อมูลปลอม
- ไม่ humanize เพื่อหลอกผู้อ่าน
- ไม่สกัด Voice Profile จากงานผู้อื่นโดยไม่ได้รับอนุญาต
- ไม่รับผิดชอบในกรณีผู้ใช้ใช้ผิดจริยธรรม

---

## 18. GLOSSARY / อภิธานศัพท์

| Term | คำแปล | Definition |
|---|---|---|
| 8-Step Master Workflow | ขั้นตอนหลัก 8 ขั้น | Sequential Thinking workflow ครอบคลุมตั้งแต่ Voice Source ถึง Storage |
| AI Bypasser | เครื่องมือหลบ AI Detection | Software ปรับ AI text — Turnitin 2026 ตรวจจับได้ |
| AI Correction | การแก้ไขเนื้อหา AI | ปรับข้อความ AI ให้อ่านเหมือนมนุษย์ |
| AI Detection | การตรวจจับ AI | ระบุว่าข้อความเขียนโดย AI หรือมนุษย์ |
| AI Score | คะแนน AI | ค่าตัวเลขจาก detector |
| AI Signature / Fingerprint | ลายนิ้วมือ AI | รูปแบบที่บ่งชี้การเขียนโดย AI |
| Burstiness | ความผันผวนของจังหวะ | ความหลากหลายของความยาวประโยค (SD ≥ 5) |
| Calibration | การปรับเทียบ | กระบวนการยืนยัน Voice Profile กับผู้ใช้ผ่าน sample test |
| Detector | เครื่องมือตรวจจับ | Software วัด AI score |
| Dimension (Voice) | มิติ (เสียงผู้เขียน) | 6+1 มิติของ Voice Profile (Sentence/Vocabulary/Paragraph/Argumentation/Citation/Cultural/[Disciplinary]) |
| False Positive | การตรวจผิด (เป็น AI) | งานมนุษย์ที่ถูกจัดเป็น AI ผิดพลาด |
| Hallucinated Citation | การอ้างอิงปลอม | citation ที่ AI สร้างไม่มีอยู่จริง |
| Humanization | การทำให้เป็นมนุษย์ | กระบวนการปรับ AI text ให้เหมือนมนุษย์ |
| Humanizer Tool | เครื่องมือ humanize | Software อัตโนมัติ — Turnitin จับได้ |
| Intensive Mode | โหมดเข้มข้น | Voice Extraction ระดับเข้มสำหรับงานวิชาการ (เพิ่ม D7) |
| Layer | ชั้นตรวจจับ | Layer 1 (Vocabulary), 2 (Statistical), 3 (Structural) |
| Level (Source) | ระดับ (แหล่งเสียง) | 5-Level Voice Source Hierarchy (User-Specified → Default → Skill → Library → Ask) |
| Memory Index | ดัชนีความจำ | บันทึกผลงาน + Voice Profile + lessons learned |
| Pass | รอบการแก้ | Pass 1 (Rhythm), Pass 2 (Vocabulary) — ห้ามทำพร้อมกัน |
| Perplexity | ความซับซ้อนเชิงภาษา | การวัดความคาดเดาได้ของคำ |
| Personal Anchor | จุดยึดส่วนบุคคล | ข้อมูลเฉพาะที่บ่งบอกตัวตนผู้เขียน |
| Personal Voice Marker | เครื่องหมายเสียงผู้เขียน | ชื่อ ตัวเลข วันที่ เรื่องเล่า counterargument มาตรากฎหมาย |
| Stylometry | สถิติเชิงสไตล์ | ศาสตร์วิเคราะห์สไตล์การเขียนเชิงสถิติ |
| Symptom Substitution | การแทน AI ด้วย AI | เปลี่ยนคำ AI เป็นคำ AI อีกคำ — ห้ามใน Pass 2 Step 3 |
| Tier 1 Vocabulary | คำศัพท์ระดับ 1 | คำที่ AI Detector จับได้ทันที |
| Translationese | ภาษาแปลตรงตัว | ภาษาไทยที่อ่านแล้วรู้ว่าแปลจากอังกฤษ |
| Two-Pass Method | วิธีสองรอบ | โปรโตคอลแก้ไขแยก Rhythm กับ Vocabulary |
| Voice Match Score | คะแนนตรงเสียง | คะแนนความตรง Voice Profile (0–100%) |
| Voice Profile / Writing Profile | สไตล์ผู้เขียน | สไตล์เฉพาะของผู้เขียน — สกัดใน 6+1 มิติ |
| Watermarking | การฝังลายเซ็น AI | เทคนิคที่ผู้พัฒนา AI ฝังในผลลัพธ์ — EU AI Act 2026 |
| AI Disclosure | การเปิดเผยการใช้ AI | การระบุการใช้ AI ในเอกสาร |

---

## 19. REFERENCES & FURTHER READING / แหล่งอ้างอิง

### 19.1 Detection Research

- Mitchell, E., et al. (2023). *DetectGPT: Zero-Shot Machine-Generated Text Detection using Probability Curvature.* arXiv:2301.11305
- Sadasivan, V. S., et al. (2023). *Can AI-Generated Text be Reliably Detected?* arXiv:2303.11156
- Krishna, K., et al. (2023). *Paraphrasing Evades Detectors of AI-generated Text.* arXiv:2303.13408
- Liang, W., et al. (2023). *GPT detectors are biased against non-native English writers.* Patterns, Cell Press

### 19.2 Stylometry & Voice Profile Research ⭐ NEW

- Mendenhall, T. C. (1887). *The Characteristic Curves of Composition.* Science.
- Burrows, J. F. (2002). *Delta: A Measure of Stylistic Difference and a Guide to Likely Authorship.* Literary and Linguistic Computing, 17(3).
- Stamatatos, E. (2009). *A Survey of Modern Authorship Attribution Methods.* JASIST, 60(3).
- Hollingsworth, C. D. (2012). *Syntactic Stylometry: Using Sentence Structure for Authorship Attribution.* University of Georgia.
- *Stylometric Analysis and Machine Learning: a winning couple for Authorship Identification.* NOTIONES (2023).
- *Stylometric comparisons of human versus AI-generated creative writing.* Humanities and Social Sciences Communications, Nature (2025).
- *Stylometry and forensic science: A literature review.* PMC, NIH (2024).
- *Authorship Attribution Methods, Challenges, and Future Research Directions: A Comprehensive Survey.* Information (MDPI, 2024).

### 19.3 Tool Documentation (2026)

- Turnitin AI Writing Detection — https://www.turnitin.com/solutions/ai-writing
- Turnitin AI Detector Roadmap 2026 — https://turnitin.app/blog/Turnitin-AI-Detector-Roadmap-Features-Coming-in-2026.html
- Originality.ai — https://originality.ai/
- GPTZero — https://gptzero.me/
- Copyleaks AI Content Detector — https://copyleaks.com/ai-content-detector
- Winston AI — https://gowinston.ai/
- Sapling AI Detector — https://sapling.ai/
- ZeroGPT — https://zerogpt.com/

### 19.4 Style and Voice Guides

- Strunk, W., & White, E. B. (2000). *The Elements of Style* (4th ed.)
- Williams, J. M., & Bizup, J. (2017). *Style: Lessons in Clarity and Grace* (12th ed.)
- ราชบัณฑิตยสภา. (2554). *พจนานุกรม ฉบับราชบัณฑิตยสถาน พ.ศ. 2554.*
- สำนักนายกรัฐมนตรี. *ระเบียบสำนักนายกรัฐมนตรีว่าด้วยงานสารบรรณ พ.ศ. 2526.*

### 19.5 Academic Voice Research ⭐ NEW

- Hyland, K. (2008). *Disciplinary Voices: Interactions in Research Writing.* English Text Construction, 1(1).
- Matsuda, P. K. (2001). *Voice in Japanese Written Discourse: Implications for Second Language Writing.* Journal of Second Language Writing, 10.
- *Authorial Voice in Academic Writing.* INSPIRA Journal.
- *Finding Your Voice as an Academic Writer (and Writing Clearly).* Journal of Social Work Education (2016).

### 19.6 Ethics and Disclosure

- COPE — Position Statement on AI Tools (2023)
- Nature Editorial. (2023). *Tools such as ChatGPT threaten transparent science.*
- ICMJE — Recommendations on AI-Assisted Technologies in Manuscripts

### 19.7 Regulatory References (2026)

- EU AI Act — https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
- Code of Practice on AI-Generated Content — https://digital-strategy.ec.europa.eu/en/policies/code-practice-ai-generated-content
- Thailand ETDA — Draft Principles for AI Legislation (Public Consultation 2568)
- Thailand AI Policy & Regulation Guide 2026 — Lex Nova Partners

### 19.8 Industry-Specific Guidance

- Google Search Central — *E-E-A-T and AI-generated content guidelines* (2024)
- Thai Higher Education Commission — แนวปฏิบัติการใช้ AI ในงานวิจัยและการเขียนวิชาการ (2566)

---

## DOCUMENT METADATA / ข้อมูลกำกับเอกสาร

**File:** `AI_Detection_and_Correction_Knowledge_Base_V05R01_2026-04-30.md`
**Version:** V05R01 (Major Update — supersedes V01R01, V02R01, V03R01, V04R01)
**Date:** 2026-04-30
**Total Sections:** 19 (organized in 6 Parts)
**Word Count (Approximate):** ~30,000 words (Thai+English combined)
**Status:** Comprehensive Knowledge Base with 8-Step Master Workflow + Voice/Writing Profile Extraction + KM-TH-THESIS-DOC integration — Ready for Skill Construction

**Companion Knowledge Base:**
- [`KM-TH-THESIS-DOC V02R01`](../voice_profiles/KM-TH-THESIS-DOC/KM-TH-THESIS-DOC_V02R01_2026-04-30.md) — Voice Profile Library สำหรับงานวิชาการไทย 7 Sub-Profiles (~10,000 คำ) สกัดจาก corpus 101 ไฟล์ (~292,000 คำ)

**Next Step:** ทบทวน V05R01 + KM-TH-THESIS-DOC V02R01 → ถ้าผ่าน → ใช้ skill-creator สร้าง Custom Skill ตามภาค 17

**Change Log:**
- **V01R01 (2026-04-30):** Initial knowledge base, 15 sections, ~6,700 words
- **V02R01 (2026-04-30):** Added 3-Dimension Framework, 3-Layer Detection, Tier 1 Tables, Detection Report Template; 6 Parts; ~17,000 words
- **V03R01 (2026-04-30):** Added Two-Pass Method (Pass 1 Rhythm + Pass 2 Vocabulary), 4 Advanced Techniques; ~22,000 words
- **V04R01 (2026-04-30):** **Major addition** — Voice/Writing Profile Extraction as core methodology:
  - Section 7 (NEW): 8-Step Sequential Thinking Master Workflow
  - Section 8 (NEW): Voice/Writing Profile Extraction Methodology with 5-Level Source Hierarchy + 6+1 Dimensions
  - Section 11 (NEW): Voice/Writing Match Scoring & Memory Storage
  - ~28,000 words
- **V05R01 (2026-04-30):** **Major update** — KM-TH-THESIS-DOC integration:
  - **🆕 Companion KB:** ผนวก [`KM-TH-THESIS-DOC V02R01`](../voice_profiles/KM-TH-THESIS-DOC/KM-TH-THESIS-DOC_V02R01_2026-04-30.md) — Voice Profile Library 7 Sub-Profiles สำหรับงานวิชาการไทย สกัดจาก corpus 101 ไฟล์ ~292,000 คำ
  - **🆕 Section 4.1.4:** Verified Tier 1 Vocabulary จาก Real Thai Corpus — แก้ไขความเข้าใจผิดเรื่องคำ "ขับเคลื่อน" "ยกระดับ" "อย่างยั่งยืน" — ปรากฏใน corpus จริง 272/133/68 ครั้งตามลำดับ จึงไม่ใช่ AI signature ในไทย
  - **🆕 Section 8.6:** Verified AI Signature List — ปรับเป็นรายการคำที่ปรากฏ ≤ 5 ครั้งใน corpus 292K คำของไทยวิชาการจริง (เช่น "เป็นที่ทราบกันดีว่า" 0 ครั้ง, "นับเป็นสิ่งสำคัญ" 0 ครั้ง, "อย่างพิถีพิถัน" 0 ครั้ง, "ปฏิเสธไม่ได้ว่า" 3 ครั้ง)
  - **🆕 Section 8.7:** Thai Academic Sub-Profiles — รายการ 7 Sub-Profiles (VP-A1 ถึง VP-C3) พร้อมขอบเขตการใช้งาน
  - **อัปเดต Section 8.2 Level 4:** Pre-defined Library ตอนนี้มี KM-TH-THESIS-DOC ครบ 7 Sub-Profiles
  - **อัปเดต Section 17.2:** Skill Architecture — voice_profiles/ folder ตอนนี้มี KM-TH-THESIS-DOC integration
  - ~30,000 words

**Voice Profile Library (KM-TH-THESIS-DOC V02R01) — 7 Sub-Profiles:**
| Profile ID | ชื่อ | สาขา/บริบท |
|---|---|---|
| VP-A1 | MCU PA Dissertation | ดุษฎีนิพนธ์รัฐประศาสนศาสตร์ มจร |
| VP-A2 | MCU Buddhist Integration | ดุษฎีนิพนธ์ มจร พุทธบูรณาการ |
| VP-B1 | AGJ Article | บทความวิชาการ AGJ TCI Tier 2 |
| VP-B2 | General TCI Academic | บทความวิชาการ TCI ทั่วไป |
| VP-C1 | Accounting Research | บทความวิจัยบัญชี/บริหาร |
| VP-C2 | Procurement Research | บทความวิจัยจัดซื้อจัดจ้าง |
| VP-C3 | Public Sector/Education Research | บทความวิจัยรัฐประศาสนศาสตร์/การศึกษา |

---

*— End of Knowledge Base Document V05R01 —*
