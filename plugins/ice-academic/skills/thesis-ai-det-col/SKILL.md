---
name: thesis-ai-det-col
description: Thai AI detection, humanization, Voice/Writing Profile extraction, and full-document pre-submission audit — for Academic, Business, and General writing (TH+EN). Use to detect whether text was AI-written, humanize it to authentic human voice, extract a writing profile from a folder of references, or audit a document before submission. Triggers on "ตรวจ AI", "ทำให้ดูเป็นมนุษย์เขียน", "humanize", "ลด AI score", "Turnitin", "GPTZero", "แก้ข้อความ AI", "สกัด writing style", "ดุษฎีนิพนธ์ มจร", "บทความวิชาการ TCI", "บทความวิจัย", "ตรวจ proposal", "ตรวจข้อเสนอ", "ตรวจ citation", "ตรวจ format ก่อนส่ง", "review เอกสาร", "audit บทความ" — and Thai dissertations, MCU theses, AGJ/TCI articles, iCE business proposals, or a folder of documents to learn the style. Use even when the user doesn't say "AI". Self-contained and portable — runs on both Claude Code and Claude on web. ONLY reads, detects, rewrites, audits — does NOT produce formatted documents.
---

# THESIS-AI-DET-COL — Thai AI Detection & Correction Skill

ทักษะตรวจจับและแก้ไขเนื้อหา AI สำหรับงานเขียนภาษาไทย+อังกฤษ ครอบคลุม 3 ประเภทเนื้อหา (Academic / Business / General) — Detection, Correction (Two-Pass Method), Voice Profile Extraction, และ Full-Document Audit. ตั้งบน corpus จริง: งานวิชาการไทย 101 ไฟล์ (292K คำ) + เอกสารธุรกิจ iCE 13 ไฟล์.

**Version: V05R01 | 2026.06.13** — Major: restructure เป็น **Shared Core + 3 Branches เท่าเทียม** (§2). กลไกสากล (12 universal-check, EN AI-vocab, two-pass, soul, wording, anti-halluc) = 🟦 CORE แก้ที่เดียว · register-specific (🟩 Academic / 🟧 Business / 🟪 General) แยก 3 branch ไม่มีตัวใดแทรก/เกาะ. ปิด gap General (เดิมเกาะ academic → มี branch จริง). Manifest แยก Core + Branch-specific. (V04R02: Business corpus 6→13 + ref 11 TB/EB + ANTI-ลิเก — ดู changelog)

---

## 1. SCOPE (ขอบเขต)

**ทักษะนี้ทำ:**
- ตรวจจับว่าข้อความเขียนโดย AI หรือไม่ (3-Layer Detection)
- แก้ไขข้อความ AI ให้อ่านเหมือนมนุษย์เขียนและตรงเสียงผู้เขียน (Two-Pass Method)
- สกัด Voice/Writing Profile จากโฟลเดอร์เอกสารอ้างอิง (6+1 Dimensions)
- อ่านสรุปและให้ feedback คุณภาพข้อความ
- ตรวจเอกสารวิชาการไทย "ทั้งฉบับ" ก่อนส่ง ผ่าน Thai Academic Audit Engine (`references/10_academic_audit_engine.md`)

**ทักษะนี้ไม่ทำ:**
- ไม่สร้างเอกสารรูปแบบสำเร็จ (PPTX/DOCX/PDF/Excel) — ส่งต่อ skill อื่น (`docx`/`pptx`/deliverable-gen)
- ไม่จัดทำแผนภูมิ/visualization
- ไม่เขียนใหม่ทั้งฉบับจากศูนย์ — เน้นแก้ ไม่เน้น generate (ดู §14)

**Output ขึ้นกับ Prompt:** ผู้ใช้ระบุรูปแบบที่ต้องการแต่ละครั้ง — ทักษะนี้เน้นเนื้อหา ไม่กำหนด format.

---

## 2. ARCHITECTURE — SHARED CORE + 3 BRANCHES ⭐ V05

โครงสร้าง **Shared Core + 3 Branches** — สิ่งที่เป็นกลไกสากล (AI-tell ที่ทุกงานใช้ร่วมกัน) อยู่ **CORE แก้ที่เดียว** · สิ่งที่ผูก register เฉพาะ (academic/business/general) แยก **3 branch เท่าเทียมกัน** ไม่มีตัวใด "แทรก" หรือ "เกาะ" ตัวอื่น.

### 2.1 CONTENT-TYPE GATE (เช็คประเภทเนื้อหาก่อนเสมอ)

**ก่อนทำงานทุกครั้ง — ระบุประเภทเอกสารก่อน** เพื่อเลือก branch (corpus / voice profile / register-specific check ต่างกัน). ไม่มี default-bias — เลือกตามเอกสารจริง; ถ้าคาบเกี่ยว/ไม่ชัด = ถาม (ห้ามเดาเป็น Academic อัตโนมัติ).

| Branch | เอกสารแบบไหน | Branch-specific Engine | Voice Profile |
|---|---|---|---|
| 🟩 **Academic** | ดุษฎีนิพนธ์/บทความ/วิจัย/วิชาการ | `05` thai-academic-patterns + `06` Class A/B + 3 academic-check (Citation/Reporting-Verb/Acronym) + TQ1-9 + `10` audit | `KM-TH-THESIS-DOC` (7 sub) |
| 🟧 **Business** | proposal/SoW/investment/solution/manday | `11` B-Check (TB/EB cadence) + Watchlist + Anchor rule + §6 Anti-ลิเก (L1-L8/P1-P9) + Lexical-fingerprint | `KM-TH-BIZ-DOC` (8 sub) |
| 🟪 **General** | งานทั่วไป (email/บทความทั่วไป/บันทึก) | Core ล้วน + register adjust (เสียงที่ปรึกษา-สอน) + watchlist สากล | academic baseline + register tune |

> **⚠ ทั้ง 3 branch อยู่ใน skill นี้ — ไม่ route ออก:** qa-master D5 Anti-AI โหลด skill นี้โดยตรง → ถ้าแยก branch ออกไป skill อื่น qa-master จะโหลดกลับ = วนวงกลม. AI-detection ทั้ง 3 register อยู่ที่ skill นี้ที่เดียว.

### 2.2 SHARED CORE — กลไกที่ทุก branch ใช้ร่วม (แก้ที่เดียว ใช้ครบ 3) 🟦

| Core component | ไฟล์ | ทำอะไร (สากลทุก register) |
|---|---|---|
| **3-Layer 12 universal-check** | `01` | burstiness · sentence-opening · paragraph-symmetry · transition-density · bullet-thinking · template-proximity · nested-clause · paragraph-length (12/15 check ที่ไม่ผูก register) |
| **EN AI-vocab + cadence** | `06` §4 + `07` (24 patterns) | delve/leverage/robust/seamless ฯลฯ + EB cadence — AI-tell ภาษาอังกฤษสากล |
| **Two-Pass method** | `02` | Rhythm→Vocabulary (กลไกแก้ ไม่ผูก register) |
| **Voice-Extract** | `03` | 6+1 Dimensions (สกัด profile แบบไหนก็ได้) |
| **Correction techniques** | `04` | Catalog 18 techniques |
| **Filler/chatbot artifacts** | `09` | filler phrases สากล |
| **Soul** | `08` | เติมเสียงมนุษย์ (ทุก register หลัง de-AI) |
| **Anti-Hallucination H3** | — | ห้ามกุชื่อ/ตัวเลข/citation — ทุก branch |
| **Wording W1-W5** | (ฝังด้านล่าง) | positive-default · no-unexplained-tech · anti-ลิเก · no-abbrev · no-marketing-leak |

### 2.3 WORDING DISCIPLINE LAYER (Core — ทุก branch)
- **W1 Positive-default** — positive เป็นค่าตั้งต้น · negative เฉพาะระบุชัด/วิจารณ์ limitation จริง
- **W2 No-unexplained-technical** — technical/acronym ที่ไม่อธิบาย → flag · เนื้อหาเทคนิคลึกอธิบายได้ แต่ต้องมีคำอธิบายเชิงผู้ใช้
- **W3 Anti-ลิเก/over-ornate** — บรรณสโวหาร/คำหรูเกิน → flag · catalog เต็ม (L1-L8 ไทย / P1-P9 อังกฤษ + GUARD) → ดู `11` §6 (cut→anchor-swap: แลกคำหรูเป็น fact/กลไก มิฉะนั้นตัด)
- **W4 No-abbreviation-without-context** — คำย่อนิยามก่อน
- **W5 Marketing-leakage** — emoji/slang/hook/CTA/clickbait → flag (ไม่เหมาะทั้ง 3 branch)

> **Register note:** W1-W5 เป็น core (ทุก branch) แต่ "ความเข้ม" ต่างกัน — Academic: วิจารณ์เฉพาะ limitation, อธิบายเข้าใจง่าย · Business: positive-default, technical อธิบายหลายระดับ · General: เสียงที่ปรึกษา-สอน ชัดเจน.

### 2.4 L1 WRITE-CLEAN CARD — เขียนสะอาดตั้งแต่แรก (prevention) ⭐ V05

`12_write_clean_card.md` = สารสกัด top AI-tells (core A + 3 register B + guard C) แบบสั้น สำหรับใช้ตอน **เขียน** (ไม่ใช่ตอน detect). ออกแบบให้ **ทุก agent ในระบบฝัง/อ้าง** → เลี่ยง AI-cadence ตั้งแต่ร่างแรก ไม่ต้องวน detect→fix (ประหยัด token). 2 ชั้นเสริมกัน: **L1 card = prevention (ทุก agent ตอนเขียน)** · **skill เต็ม = detection/correction (qa-master D5 ตอน QA จริงจัง)**.

---

## 3. SIX MODES (หกโหมดหลัก)

| Mode | งาน | Output |
|---|---|---|
| **1 DETECT** | ตรวจ AI signature ด้วย 3-Layer Method (15 จุดตรวจ) | Detection Report + Pass/Fail |
| **2 EXTRACT** | สกัด Voice Profile จากโฟลเดอร์อ้างอิง (6+1 Dimensions) | Voice Profile + Profile ID |
| **3 CORRECT** | แก้ไขข้อความด้วย Two-Pass Method (Rhythm → Vocabulary) | Pass 1 + Pass 2 Output + Change Log |
| **4 FULL CYCLE** | Detect → Correct → Soul → Voice Match (≥75%) | Final Output + score progression |
| **5 SUMMARIZE** | อ่านและให้ feedback คุณภาพ (quick read) | Concise critique |
| **6 ADD SOUL** | เติมเสียงมนุษย์เมื่อข้อความผ่าน detector แต่ยัง soulless | Soul-enriched output |

### Mode Selection

| User says (TH) | User says (EN) | Mode |
|---|---|---|
| "ตรวจดูว่าเขียนโดย AI ไหม" | "Check if AI-generated" | **1 DETECT** |
| "อ่านโฟลเดอร์ X สกัด writing profile" | "Extract writing style from folder" | **2 EXTRACT** |
| "แก้ให้เหมือนมนุษย์เขียน" + Voice Profile | "Humanize using profile X" | **3 CORRECT** |
| "ตรวจและแก้ให้ครบ" | "Detect and fix" | **4 FULL CYCLE** |
| "อ่านและสรุปให้หน่อย" | "Read and summarize" | **5 SUMMARIZE** |
| "ผ่าน detector แล้วแต่ยังแข็ง เติม soul" | "Passes detector but soulless" | **6 ADD SOUL** |

**ถ้าไม่ชัด** → ถามผู้ใช้ด้วย 6-option clarification (1 Detect / 2 Extract / 3 Correct / 4 Full Cycle / 5 Summarize / 6 Add Soul).

### กฎเหล็ก (ทุก Mode)
1. **ห้าม fabricate** — ห้ามสร้างชื่อ/ตัวเลข/citation/วันที่ ที่ไม่มีจริง
2. **ห้ามทำ Pass 1 + Pass 2 พร้อมกัน** — แก้ rhythm ก่อน vocabulary เสมอ
3. **Voice Profile ต้องมาจาก Level 1–5 Hierarchy** — ไม่มีต้องถาม
4. **Verified AI Signature เท่านั้น** — ใช้ corpus จริง (academic 292K / business iCE) · งาน EN/Bilingual ดู `07` (24 patterns)
5. **Content-Type Gate ก่อนเสมอ** (§2) — เลือก engine/profile/wording ตามประเภท
6. **Avoiding AI patterns is only half the job** — ลบ AI ไม่พอ ต้องเติมเสียงมนุษย์ (Mode 6, `08`)
7. **Mandatory Load Manifest** (§4) — โหลดไฟล์ครบก่อนรัน
8. **Full-Coverage Scan** — ตรวจทุกย่อหน้า 100% ห้ามสุ่ม · check ระยะใกล้ใช้ sliding window · รายงาน Scan Coverage

---

## 4. MANDATORY LOAD MANIFEST (บังคับโหลดก่อนเริ่ม)

ไฟล์ใน manifest **บังคับโหลด** ก่อนรัน workflow + บันทึกใน "Files Loaded" ของ report ทุกครั้ง. โครงเป็น **CORE (โหลดทุก branch) + BRANCH-specific (โหลดเฉพาะ branch ที่เลือกใน §2.1)**.

**CORE — โหลดทุกครั้งทุก branch:**

| Mode | Core files |
|---|---|
| 1 DETECT | `01` (3-Layer) + `06` §4 (EN vocab) |
| 2 EXTRACT | `03` |
| 3 CORRECT | `02` + `04` + `09` |
| 4 FULL CYCLE | Mode 1 + Mode 3 core |
| 5 SUMMARIZE | none (quick read) |
| 6 ADD SOUL | `08` |

**BRANCH-specific — โหลดเพิ่มตาม branch (เลือก 1):**

| Branch | DETECT (Mode 1) เพิ่ม | CORRECT (Mode 3) เพิ่ม | Profile |
|---|---|---|---|
| 🟩 Academic | `05` + `06` §1-3 (Class A/B) | `05` | `KM-TH-THESIS-DOC` |
| 🟧 Business | `11` (B-Check TB/EB + §6) | `11` | `KM-TH-BIZ-DOC` |
| 🟪 General | (core พอ) + watchlist สากล | (core พอ) | academic baseline + register tune |
| **+ EN/Bilingual ทุก branch** | + `07` (24 patterns) | + `07` | — |

### Thai Structural Quick-List (TQ1–TQ9) — 🟩 ACADEMIC branch (อ้าง `05` thai-academic; General ใช้เฉพาะ TQ1-2 ที่เป็นโครงสร้างสากล)

| # | กฎ | อ้างอิง |
|---|---|---|
| TQ1 | อนุประโยคซ้อน "ซึ่ง/ที่/อัน" ≤ 2 ชั้น/ประโยค | `05` §1.3 |
| TQ2 | โครงเปิดประโยคเดียวกันห้ามซ้ำใน 5 ประโยค/ย่อหน้า | `01` Check 6 |
| TQ3 | สูตรประโยคสำเร็จรูปต้องรื้อทั้งโครง ไม่ใช่ถอดคำ | `05` §7 |
| TQ4 | Forward signpost ≤ 1 ครั้ง/เอกสาร | `05` §9 |
| TQ5 | Acronym นิยามเต็มครั้งแรกครั้งเดียว | `05` §8 |
| TQ6 | คำ Class A Zero-Tolerance (อย่างก้าวกระโดด ฯลฯ) เจอครั้งเดียวต้องแก้ | `06` §1.6 |
| TQ7 | ย่อหน้าสรุปห้ามเปิดด้วยสูตรสังเคราะห์ | `06` §1.5 |
| TQ8 | ระวัง "การ/ความ" ซ้อน + passive แบบภาษาแปล | `05` §1 |
| TQ9 | กริยารายงานตรงชนิดแหล่ง (งานทัศนะห้าม "พบว่า/พิสูจน์ว่า") | `05` §10 |

### ⚠ Corpus-Correct Rule (กันลบคำที่คนใช้จริง) — ใช้ทั้ง Academic + Business

- **Class A Zero-Tolerance** (เจอครั้งเดียวแก้): Academic = ยิ่งไปกว่านั้น/ในท้ายที่สุด/ทั้งหมดนี้สังเคราะห์ได้ว่า/อย่างก้าวกระโดด/พลิกโฉม(ใน body)/เป็นที่ทราบกันดีว่า (`06`). Business = ดู `11` (cadence tell B1-B4)
- **Common-in-Real-Thai (🟢 ใช้ได้ density ≤3/500)**: Academic = นอกจากนี้ (156×)/อย่างมีประสิทธิภาพ (195×). Business = ตอบโจทย์/รองรับ/พลิกโฉม(ใน vision) (ดู `11` §3)
- **ห้าม blanket-ban** คำที่ปรากฏใน corpus จริง · คำใหม่ที่สงสัย → Field-Discovered Living List (`06` §1.5) พร้อมวันที่

---

## 5. MODE 1: DETECT

1. **อ่านข้อความ** — ระบุภาษา ความยาว + **Content-Type Gate (§2.1)** → เลือก branch: 🟩 Academic / 🟧 Business / 🟪 General (ไม่ชัด = ถาม)
2. **โหลด Core + Branch files (§4)** แล้วรัน **Scan Discipline** (`01` §1.5) — แตกย่อหน้าใส่หมายเลข ตรวจทุกย่อหน้า 100%
3. **🟦 CORE — รัน universal-check (ทุก branch เหมือนกัน)** — ดู `01`:
   - **Layer 1:** Density (Class B) + Zero-Tolerance (Class A — hard gate)
   - **Layer 2 (7 universal):** Burstiness, Sentence Opening, Paragraph Symmetry, Transition Density, Bullet-thinking, Template Proximity, Nested Clause
   - **Layer 3 (universal ส่วน):** Paragraph Length, Personal Voice Markers, Section-Closing Ritual
   - **EN/Bilingual:** EN AI-vocab + EB cadence (`06` §4 + `07`)
4. **🟩🟧🟪 BRANCH — รัน register-specific check (ตาม branch ที่เลือก):**
   - **🟩 Academic** — +3 academic-check (Citation Distribution · Reporting-Verb Alignment · Acronym Re-Expansion จาก Layer 3) + Class A/B (`06` §1-3) + TQ1-9
   - **🟧 Business** — B-Check (`11` §5): Cadence TB1-TB8 · Watchlist · Register whitelist (กัน over-correction) · Anchor + Section density · §6 Anti-ลิเก
   - **🟪 General** — watchlist สากล + register-fit (เสียงที่ปรึกษา-สอน ชัดเจน ไม่ลิเก)
5. **🟦 CORE — Wording Discipline Layer (§2.3)** — รันคู่: W1-W5 (ความเข้มตาม branch)
6. **Output Detection Report** (`templates/detection_report.md`) — ระบุ Branch + Files Loaded + Scan Coverage 100%

**สถิติที่คำนวณ:** Mean sentence length · SD (≥5) · Tier 1 density/1000 (Class B) · Transition density/500 · Personal Voice Markers count

---

## 6. MODE 2: EXTRACT (สกัด Voice Profile)

1. อ่านโฟลเดอร์อ้างอิง — ดู `03` (5-Level Source Hierarchy)
2. สกัด **6+1 Dimensions** (D1 Sentence Architecture · D2 Vocabulary · D3 Tone/Register · D4 Rhetorical · D5 Structure · D6 Bilingual · D7 Personal/Org Markers)
3. คำนวณ aggregate statistics จาก corpus จริง
4. Output: Voice Profile + Calibration Samples + Profile ID `VP-[YYYYMMDD]-[XXX]`

**หากไม่มีแหล่งอ้างอิง** → เลือกจาก Library (Academic: `KM-TH-THESIS-DOC` · Business: `KM-TH-BIZ-DOC`) หรือถาม (Level 5 = ASK เสมอ)

---

## 7. MODE 3: CORRECT (Two-Pass)

**Pre-conditions:** ข้อความ input · Voice Profile (ตาม content-type) · User-provided facts (Personal Anchors) · Target AI score

### Pass 1: Rhythm Correction
1. ระบุย่อหน้าเสี่ยง (>3/5 ประโยคยาว 16-22 คำ)
2. Burstiness Injection: ตัด 2 ประโยคสั้น (8-12 คำ), ขยาย 1 ยาว (25-35 คำ)
3. Diversify Sentence Opening (5 รูปแบบ) + Proximity Guard
4. Adjust Paragraph Architecture (short/medium/long mix)
5. Verify SD ≥ 5

### Pass 2: Vocabulary Correction
1. Search & Replace 9 หมวด (EN Verbs/Adjectives/Nouns/Phrases + Thai openers/modifiers/connectives/hedging + Class A)
2. **Replace by Voice Profile** — D2 Vocabulary Signature ของ profile ที่เลือก (academic ใช้ `KM-TH-THESIS-DOC` · business ใช้ `KM-TH-BIZ-DOC`)
3. ระวัง Symptom Substitution (ห้ามเปลี่ยน AI เป็น AI อีกคำ)
4. เพิ่ม Specificity (Anchor rule สำหรับ business — ดู `11` §4)
5. Template-Level Replace — รื้อโครงสูตร (`05` §7)
6. Reporting-Verb Alignment (`05` §10) — Academic
7. **คง Lexical Fingerprint** — Business: ห้าม normalize "Advance Modules"/"operation excellency" ถ้า quote ต้นทาง (`11`)

**Advanced (4 Techniques)** ใช้เสริมเมื่อ score ยังสูง — ดู `02` + Catalog 18 ใน `04`

**Output:** Pass 1 (Rhythm) + Pass 2 (Vocabulary + Voice) + Change Log + `[NEEDS USER INPUT: ...]`

---

## 8. MODE 4: FULL CYCLE

```
[Input] → Mode 1 Detect → ผ่าน? ──Yes→ [Done]
              │ No
              ↓
        Mode 3 Correct (Two-Pass)
              ↓
        Mode 1 Re-Detect ← loop จน AI score < target
              ↓
        Mode 6 Soul step (ถ้า prose ตีความ/soulless)
              ↓
        Voice Match Scoring (D1-D6+D7, ≥75%) → [Final]
```
ใช้ `Prompt FC1: Full 8-Step Cycle` ใน `templates/correction_prompts.md`

---

## 9. MODE 5: SUMMARIZE

Quick read + feedback (ไม่รัน 3-Layer ครบ): คุณภาพ AI signature โดยรวม · จุดเด่น/จุดอ่อน · ความสอดคล้อง Voice Profile · ข้อแนะนำ

---

## 10. MODE 6: ADD SOUL

**ใช้เมื่อ:** ผ่าน detector แล้วแต่ "อ่านเหมือน AI" / เย็นชา / ไม่มีตัวตน · prose ตีความ (discussion/contribution) = soul-demand สูงสุด

**ขั้นตอน:** อ่าน `08` → รัน Soul Check 7 คำถาม → เลือก Technique S1-S6 (Have Opinions / Vary Rhythm / Acknowledge Complexity / Use "ผู้วิจัย" / Let Some Mess In / Be Specific) → ปรับตาม Voice Profile

**กฎเหล็ก:** ห้ามเติม fake personality · ห้าม fabricate emotions · counterargument อิงงานจริง · ใช้ user-provided facts เท่านั้น

---

## 11. VOICE PROFILE LIBRARIES

### Academic — `voice_profiles/KM-TH-THESIS-DOC_V02R01.md` (7 sub-profiles)
VP-A1 MCU PA Dissertation · A2 MCU Buddhist Integration · B1 AGJ Article · B2 General TCI · C1 Accounting Research · C2 Procurement Research · C3 Public-Sector/Education
**Decision Tree:** มจร? → Buddhist แกน? A2:A1 · ไม่ใช่ มจร → Research(สถิติ)/Academic → วารสาร/สาขา → B1/B2/C1/C2/C3

### Business — `voice_profiles/KM-TH-BIZ-DOC_V01R02.md` (8 sub-profiles, corpus-grounded 13 iCE proposals)
Proposal/Narrative · Investment/Commercial · Solution-Response · Manday/Service-Model · Cover-Letter/Transmittal · FSD/Spec · SoW/Technical · Gap-Analysis/Review
**กฎทอง:** register ต่าง section ไม่เท่ากัน — Investment section = value-prose ≈ 0 (ห้าม buzzword) · AI-tell โผล่ใน narrative มากกว่า investment

**ถ้าไม่มี sub-profile เหมาะ** → Mode 2 EXTRACT สกัดใหม่จากโฟลเดอร์ผู้ใช้

---

## 12. ANTI-HALLUCINATION SAFEGUARDS (ทุก Mode)

- **Mandatory User Fact Input** ก่อน Correction (ตัวเลข/ชื่อ/วันที่ จากผู้ใช้)
- **Mandatory Voice Profile** ก่อน Pass 2
- **Flag Missing Data** เป็น `[NEEDS USER INPUT: ...]`
- **No Citation Generation** — ใช้เฉพาะที่ผู้ใช้ให้
- **Pass Separation** — ไม่รัน Pass 1+2 พร้อมกัน
- **No Voice Profile Fabrication** — Level 5 = ASK
- **Business org-marker lock** — "28 ปี / first Oracle Partner / vision / ค่านิยม" ใช้ได้เฉพาะมีในแหล่งจริงของเอกสารนั้น ห้าม inject อัตโนมัติ

---

## 13. OUTPUT FORMAT (ขึ้นกับ Prompt)

Skill ไม่กำหนด format — Prompt เป็นผู้กำหนด:

| ผู้ใช้ขอ | ตอบ |
|---|---|
| "ตอบใน chat" | markdown ใน chat |
| "ใส่ในไฟล์ .md" | สร้าง .md ตามตำแหน่ง |
| "Word / Presentation" | เรียก skill `docx`/`pptx` เพิ่ม (ไม่ทำเอง) |
| TH / EN / Bilingual | ตอบตามที่ระบุ |

---

## 14. กรณีพิเศษ

- **โฟลเดอร์ > 50 PDF:** aggregate analysis ก่อน → อ่านลึกเฉพาะตัวอย่างหลากหลาย (8-10 ฉบับ) → verify pattern
- **ข้อความ < 300 คำ:** AI Detector ไม่แม่นยำ — แจ้งผู้ใช้ · แนะนำ Mode 5
- **ขอ "เขียนใหม่ทั้งหมด":** out-of-scope (เน้นแก้ ไม่ generate) → Mode 2 EXTRACT + ส่งต่อ skill เขียน (academic-article/dissertation)

---

## 15. REFERENCE FILES

| ไฟล์ | เมื่อใช้ |
|---|---|
| `00_MAIN_KB_V05R01.md` | KB หลัก ~30K คำ (perplexity/burstiness/stylometry/watermark/detection theory) — comprehensive task |
| `01_three_layer_detection.md` | Mode 1 — methodology + 15 checks |
| `02_two_pass_protocol.md` | Mode 3 — Pass 1+2 + Advanced |
| `03_voice_extraction_methodology.md` | Mode 2 — 6+1 Dimensions + 5-Level Hierarchy |
| `04_correction_techniques.md` | Catalog 18 Techniques (12 Original + 6 Wikipedia) |
| `05_thai_academic_patterns.md` | Mode 1+3 (ไทย) — Translationese, Templates, Acronym, Reporting-Verb |
| `06_verified_ai_signatures.md` | คำ verified AI signature (corpus 292K) — Class A/B |
| `07_wikipedia_24_patterns.md` | 24 patterns (English/Bilingual) |
| `08_personality_and_soul.md` | Mode 6 — Soul Technique S1-S6 |
| `09_filler_replacement_table.md` | filler phrases + chatbot artifacts (Pass 2) |
| `10_academic_audit_engine.md` | TAAE — ตรวจเอกสารวิชาการทั้งฉบับ 7-Phase (shared กับ qa-master) |
| `11_business_ai_patterns.md` | 🟧 Business branch — AI-tell + register (corpus iCE 13 ไฟล์) · TB/EB cadence + §6 Anti-ลิเก |
| `12_write_clean_card.md` ⭐ | **L1 Write-Clean Card** — สารสกัด top AI-tells (core A + 3 register B + guard C) สำหรับ "เขียนสะอาดตั้งแต่แรก" · ให้ทุก agent ฝัง/อ้าง (prevention) — คู่กับ skill เต็ม (detection) |

**Voice profiles:** `KM-TH-THESIS-DOC` (academic) · `KM-TH-BIZ-DOC` (business)

---

## 16. WORKFLOW SUMMARY

```
ผู้ใช้พิมพ์ prompt
  → Content-Type Gate (§2.1): เลือก branch 🟩 Academic / 🟧 Business / 🟪 General (ไม่ชัด=ถาม)
  → เลือก Mode (1-6)
  → ถามคำถามจำเป็น (Voice source, facts, target score)
  → โหลด CORE + BRANCH files ตาม Manifest (§4)
  → รัน CORE universal-check → BRANCH register-specific check
  → ส่ง output ตาม format ที่ prompt กำหนด (ระบุ branch ใน report)
  → เสนอ next step
```

---

## CHANGELOG

- **V05R01 (2026.06.13)** — Major restructure: **Shared Core + 3 Branches** (§2). แยกชัด "กลไก AI-tell สากล (common แชร์ทุก register)" = 🟦 CORE (12 universal-check, `06`§4 EN vocab + `07`, two-pass `02`, voice-extract `03`, techniques `04`, filler `09`, soul `08`, wording W1-W5, anti-halluc H3 — แก้ที่เดียว ใช้ครบ 3) ออกจาก "register เฉพาะทาง" = 3 branch เท่าเทียม (🟩 Academic: `05`+`06`§1-3+TQ1-9+`10`+3 academic-check · 🟧 Business: `11` B-Check TB/EB+§6+Anchor+fingerprint · 🟪 General: core+register-tune — ปิด gap เดิมที่เกาะ academic). Mode 1 DETECT แยก step CORE→BRANCH. Manifest แยก Core + Branch-specific. ไม่มี content ใหม่ใน reference — เป็นการ reorganize flow ให้ business/general เทียบเท่า academic (ไม่ใช่ augment). เตรียมรองรับ L1 Write-Clean Card (ref ใหม่) ให้ทุก agent ฝัง.
- **V04R02 (2026.06.13)** — ขยาย Business corpus 6→13 iCE proposals (BCG/Exim/KingPower/Forth/KTC/BANPU/TMB ฯลฯ). `KM-TH-BIZ-DOC` V01R02: 8 sub-profiles (+Cover-Letter/FSD/SoW/Gap-Analysis) + register ยืนยัน + Reframe/Citation-to-source patterns. `11_business_ai_patterns` V01R02: +TB1-TB8 (TH cadence) +EB1-EB9 (EN cadence) +ANTI-ลิเก Catalog (L1-L8/P1-P9 + GUARD) +watchlist (best-in-class/zero-risk/Transformation/✓emoji). Scope clarify: voice profile เก็บ "ลายเซ็นภาษา" ไม่ใช่ "ค่าตัวเลของค์กร" (fact-check แยกจาก AI-style detection).
- **V04R01 (2026.06.12)** — Major: เพิ่ม Business Engine ในตัว (Content-Type Gate 3 ประเภท Academic/Business/General + `KM-TH-BIZ-DOC` corpus-grounded + `11_business_ai_patterns.md`). Restructure ลำดับเป็นเส้นตรง. รวม changelog ท้ายไฟล์ · ล้าง remark กระจัดกระจาย.
- **V03R02 (2026.06.12)** — Content-Type Gate + Wording Discipline (เดิม Business route ออก) + Corpus-Correct Rule + fix 7 defects.
- **V03R01 (2026.06.07)** — 15 จุดตรวจ + Zero-Tolerance Class + Field-Discovered Living List + Mandatory Load Manifest + Full-Coverage Scan.
- **V02 (2026.06)** — Mode 6 ADD SOUL + 24 Wikipedia patterns + 18 Correction Techniques.

*Corpus: งานวิจัยไทย 101 ไฟล์ (292K คำ) + เอกสารธุรกิจ iCE 13 ไฟล์ — ดู `references/00_MAIN_KB_V05R01.md`*
