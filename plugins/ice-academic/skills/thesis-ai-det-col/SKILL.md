---
name: thesis-ai-det-col
description: Thai AI detection, humanization, Voice/Writing Profile extraction, and full-document pre-submission audit — register-agnostic across Academic, Business, and General writing (TH+EN). Use to detect whether text was AI-written, humanize it to authentic human voice, extract a writing profile from a folder of references, or audit a document before submission. Triggers on "ตรวจ AI", "ทำให้ดูเป็นมนุษย์เขียน", "humanize", "ลด AI score", "Turnitin", "GPTZero", "แก้ข้อความ AI", "สกัด writing style", "ดุษฎีนิพนธ์ มจร", "บทความวิชาการ TCI", "บทความวิจัย", "ตรวจ proposal", "ตรวจข้อเสนอ", "ตรวจ citation", "ตรวจ format ก่อนส่ง", "review เอกสาร", "audit บทความ" — and Thai dissertations, MCU theses, AGJ/TCI articles, iCE business proposals, general writing (email/blog/report), or a folder of documents to learn the style. Use even when the user doesn't say "AI". Self-contained and portable — runs on both Claude Code and Claude on web. ONLY reads, detects, rewrites, audits — does NOT produce formatted documents.
---

# THESIS-AI-DET-COL — Thai AI Detection & Correction Skill

ทักษะตรวจจับและแก้ไขเนื้อหา AI สำหรับงานเขียนภาษาไทย+อังกฤษ — register-agnostic ครอบคลุม 3 ประเภทเนื้อหาเท่าเทียมกัน (🟩 Academic / 🟧 Business / 🟪 General) — Detection, Correction (Two-Pass), Voice Profile Extraction, Full-Document Audit.

**Version: V06R01 | 2026.06.13** — Major rewrite: **Shared Core (register-agnostic) + 3 Branches เท่าเทียม**. 🟦 CORE = กลไกที่ไม่มี academic default ฝังอยู่ · 🟩/🟧/🟪 = 3 branch สมมาตร (column เท่ากัน) ไม่มีตัวใดเกาะตัวอื่น. เพิ่ม **Register Gate เป็น Tier-1 entry** (ขึ้นก่อนทุกอย่าง — ห้ามเดา Academic) · ตาราง 3-branch สมมาตร · 2-tier tree (register-gate → sub-profile) · de-dup (corpus / anti-halluc / two-pass / density → SSOT 1 ที่ + pointer) · TQ rebalance (TQ1-2 → CORE universal · TQ3-9 → 🟩 academic) · Mode 6 worked example ครบ 3 register. (V05: Shared Core + 3 Branches เริ่มต้น — ดู changelog)

> **Corpus Provenance (SSOT):** corpus จริง = งานวิชาการไทย **101 ไฟล์ / ~292K คำ** + เอกสารธุรกิจ iCE **13 proposals**. ตัวเลขนี้อ้างได้ที่เดียวบรรทัดนี้ — ส่วนอื่นชี้กลับมาที่นี่.
> **⚠ Corpus asymmetry note:** 292K academic vs 13 iCE = **data-availability ไม่ใช่ priority ranking**. branch ที่มี corpus หนากว่า "ไม่ได้" สำคัญกว่า — ทั้ง 3 branch เท่าเทียมในการตัดสินใจ; ความหนาของหลักฐานต่างกันเพราะข้อมูลที่หาได้ต่างกันเท่านั้น.

---

## 0. TIER-1 ENTRY — REGISTER GATE (ต้องผ่านก่อนทุกอย่าง) ⭐ V06

**ก่อนทำงานทุกครั้ง คำถามแรกคือ "งานนี้ register ไหน?"** — ไม่ใช่ "Mode ไหน". ไม่มี default-bias ฝังในกลไก.

```
งานนี้ register ไหน?
   🟩 Academic   ดุษฎีนิพนธ์ / บทความ / วิจัย / วิชาการ
   🟧 Business   proposal / SoW / investment / solution / manday
   🟪 General    email / blog / report / บันทึก / งานทั่วไป
ห้ามเดา Academic อัตโนมัติ · คาบเกี่ยว/ไม่ชัด = ASK (ห้ามเดา)
```

- **กฎ Tier-1:** ระบุ register ก่อน → จึงเลือก Mode → จึงโหลดไฟล์. register เป็นแกนเลือก corpus / voice profile / register-specific check.
- **ASK rule:** เอกสารคาบเกี่ยว (เช่น business case ที่มีส่วนวิชาการ) หรือไม่มีสัญญาณชัด → ถามผู้ใช้ก่อน ห้ามเดา.
- **2-Tier tree:** Tier-1 = register-gate (3 branch) → Tier-2 = sub-profile ในแต่ละ branch (ดู §2.5).

---

## 1. SCOPE (ขอบเขต)

**ทักษะนี้ทำ:**
- ตรวจจับว่าข้อความเขียนโดย AI หรือไม่ (3-Layer Detection — register-agnostic)
- แก้ไขข้อความ AI ให้อ่านเหมือนมนุษย์เขียนและตรงเสียงผู้เขียน (Two-Pass Method)
- สกัด Voice/Writing Profile จากโฟลเดอร์เอกสารอ้างอิง (6+1 Dimensions)
- อ่านสรุปและให้ feedback คุณภาพข้อความ
- ตรวจเอกสารวิชาการไทย "ทั้งฉบับ" ก่อนส่ง ผ่าน Thai Academic Audit Engine (`references/10_academic_audit_engine.md`) — 🟩 academic branch

**ทักษะนี้ไม่ทำ:**
- ไม่สร้างเอกสารรูปแบบสำเร็จ (PPTX/DOCX/PDF/Excel) — ส่งต่อ skill อื่น (`docx`/`pptx`/deliverable-gen)
- ไม่จัดทำแผนภูมิ/visualization
- ไม่เขียนใหม่ทั้งฉบับจากศูนย์ — เน้นแก้ ไม่เน้น generate (ดู §14)

**Output ขึ้นกับ Prompt:** ผู้ใช้ระบุรูปแบบที่ต้องการแต่ละครั้ง — ทักษะนี้เน้นเนื้อหา ไม่กำหนด format.

---

## 2. ARCHITECTURE — SHARED CORE + 3 BRANCHES เท่าเทียม ⭐ V06

โครงสร้าง = **🟦 CORE (register-agnostic — กลไกที่ไม่มี academic default) + 3 branch เท่าเทียม** ไม่มีตัวใด "แทรก" หรือ "เกาะ" ตัวอื่น. แก้ CORE ที่เดียว ใช้ครบ 3.

### 2.1 SHARED CORE — กลไก register-agnostic (แก้ที่เดียว ใช้ครบ 3) 🟦

CORE ไม่มี academic default — เป็นกลไก AI-tell สากลที่ทุก register ใช้ร่วมกัน.

| Core component | ไฟล์ (SSOT) | ทำอะไร (สากลทุก register ไม่ผูก academic) |
|---|---|---|
| **3-Layer universal-check** | `01` | burstiness · sentence-opening · paragraph-symmetry · transition-density · bullet-thinking · template-proximity · nested-clause · paragraph-length (universal checks ที่ไม่ผูก register) |
| **Thai structure universal** | `01` + `05` §1.3 | TQ1-TQ2 (nested-clause ≤2 ชั้น · sentence-opening ไม่ซ้ำใน 5 ประโยค) — โครงสร้างไทยที่ทุก register ใช้ (ดู §4) |
| **EN AI-vocab + cadence** | `06` §4 + `07` (24 patterns) | delve/leverage/robust/seamless ฯลฯ — AI-tell ภาษาอังกฤษสากล |
| **Two-Pass method** | `02` | Rhythm→Vocabulary (กลไกแก้ ไม่ผูก register) — separation canonical อยู่ที่นี่ (ดู §7) |
| **Voice-Extract** | `03` | 6+1 Dimensions (สกัด profile register ไหนก็ได้) |
| **Correction techniques** | `04` | Catalog 18 techniques + Anti-Patterns 8 |
| **Filler/chatbot artifacts** | `09` | filler phrases สากล |
| **Soul** | `08` | เติมเสียงมนุษย์ (ทุก register หลัง de-AI — ดู §10 worked example 3 register) |
| **Anti-Hallucination H3** | canonical §12 | ห้ามกุชื่อ/ตัวเลข/citation — ทุก branch (รายละเอียดเดียวที่ §12) |
| **Wording W1-W7** | §2.3 | positive-default · no-unexplained-tech · anti-ลิเก · no-abbrev · no-marketing-leak · de-bureaucratize · particle-leak |

### 2.2 3-BRANCH SYMMETRIC TABLE — สมมาตร (column เท่ากันทุก branch) 🟩🟧🟪

ทั้ง 3 branch มีโครงเดียวกัน 4 column — academic **ไม่หนากว่า** general. ความต่างคือเนื้อ ไม่ใช่สิทธิ์.

| | 🟩 Academic | 🟧 Business | 🟪 General |
|---|---|---|---|
| **Engine** | `05` thai-academic + `06` Class A/B + `10` audit | `11` B-Check (TB1-8/EB1-9 cadence) + Watchlist + Anchor | Core ล้วน + register adjust |
| **Checks** | +3 academic-check (Citation · Reporting-Verb · Acronym) + TQ3-9 | §6 Anti-ลิเก (L1-8/P1-9+GUARD) + Lexical-fingerprint + Section-density | watchlist สากล + register-fit |
| **Voice Profile** | `KM-TH-THESIS-DOC` (7 sub) | `KM-TH-BIZ-DOC` (8 sub) | core baseline + register tune (⚠ ไม่มี dedicated corpus — ดู limitation §2.5) |
| **Soul-calibration** | "ผู้วิจัย" voice · acknowledge complexity · counterargument อิงงานจริง | "เรา/ทีมที่ปรึกษา" voice · value-prose พอเหมาะ · org-marker lock | conversational voice · ชัดเจน-สอน · ไม่ลิเก ไม่ทางการเกิน |

> **⚠ ทั้ง 3 branch อยู่ใน skill นี้ — ห้าม route ออก (circular guard):** qa-master Dimension 5 (Anti-AI) โหลด skill นี้โดยตรง → ถ้าแยก branch ใด ๆ ออกไป skill อื่น qa-master จะโหลดกลับ = **วนวงกลม**. AI-detection ทั้ง 3 register ต้องอยู่ที่ skill นี้ที่เดียว.

### 2.3 WORDING DISCIPLINE LAYER (Core — ทุก branch) 🟦
- **W1 Positive-default** — positive เป็นค่าตั้งต้น · negative เฉพาะระบุชัด/วิจารณ์ limitation จริง
- **W2 No-unexplained-technical** — technical/acronym ที่ไม่อธิบาย → flag · เนื้อหาเทคนิคลึกอธิบายได้ แต่ต้องมีคำอธิบายเชิงผู้ใช้ · readability-load (ประโยคยาว×ซับซ้อน) → `11` §4.6
- **W3 Anti-ลิเก/over-ornate + calque** — บรรณสโวหาร/คำหรูเกิน + translationese วลีศัพท์ธุรกิจแปลตรง → flag · catalog เต็ม (L1-L8 ไทย / P1-P9 อังกฤษ + GUARD §6 · C1-C12 calque + V1-V4 over-ornate verb §6.5) → ดู `11` §6+§6.5 (cut→anchor-swap: แลกคำหรู/calque เป็น fact/กลไก มิฉะนั้นตัด · โครงประโยคแปล → `05a` §1)
- **W4 No-abbreviation-without-context** — คำย่อนิยามก่อน
- **W5 Marketing-leakage** — emoji/slang/hook/CTA/clickbait → flag (ไม่เหมาะทั้ง 3 branch)
- **W6 De-bureaucratize/transliteration** — TH-coinage technical ทึบกว่า EN-loanword → flag · คง EN/ไทย(English) ครั้งแรกแล้วทับศัพท์ (decision pivot vs calque W3 — แกน = recognizability ผู้อ่านเป้าหมาย) → ดู `11` §6.6 · gloss-once `05a` §8
- **W7 Politeness-particle leak** — คำลงท้ายสุภาพ (ครับ/ค่ะ/คะ/นะคะ) ในเอกสารทางการ → flag · ผ่าน Boundary Guard ก่อน (segment+line-break-join+clause-final+exclusion) → ดู `11` §6.8 · CORE `05a` §Particle Boundary Guard

> **Register note:** W1-W7 เป็น core (ทุก branch) แต่ "ความเข้ม" ต่างกันตาม Soul-calibration ใน §2.2 — Academic: วิจารณ์เฉพาะ limitation · Business: positive-default + technical อธิบายหลายระดับ · General: conversational ชัดเจน.

### 2.4 L1 WRITE-CLEAN CARD — เขียนสะอาดตั้งแต่แรก (prevention)

`12_write_clean_card.md` = สารสกัด top AI-tells (core A + 3 register B + guard C) แบบสั้น สำหรับใช้ตอน **เขียน** (ไม่ใช่ตอน detect). ออกแบบให้ **ทุก agent ในระบบฝัง/อ้าง** → เลี่ยง AI-cadence ตั้งแต่ร่างแรก ไม่ต้องวน detect→fix (ประหยัด token). 2 ชั้นเสริมกัน: **L1 card = prevention (ทุก agent ตอนเขียน)** · **skill เต็ม = detection/correction (qa-master D5 ตอน QA จริงจัง)**.

### 2.5 2-TIER TREE — register-gate → sub-profile (Tier-2 ในแต่ละ branch)

หลังผ่าน Tier-1 Register Gate (§0) → เข้า Tier-2 เลือก sub-profile ในแต่ละ branch:

- **🟩 Academic Tier-2:** มจร? → Buddhist แกน? → A2:A1 · ไม่ใช่ มจร → Research(สถิติ)/Academic → วารสาร/สาขา → B1/B2/C1/C2/C3 (7 sub — ดู §11)
- **🟧 Business Tier-2:** section-matrix 8 sub (Proposal/Narrative · Investment/Commercial · Solution-Response · Manday/Service · Cover-Letter · FSD/Spec · SoW/Technical · Gap-Analysis — ดู §11)
- **🟪 General Tier-2:** blog / email / report
  > **⚠ Limitation:** General **ยังไม่มี dedicated corpus** (ไม่มี 101-file/13-proposal เทียบเท่า). Tier-2 จึงใช้ core baseline + register tune; ถ้าผู้ใช้มีโฟลเดอร์ตัวอย่าง → Mode 2 EXTRACT สกัด profile เฉพาะก่อนแก้ (แนะนำ). ระบุ limitation นี้ใน report เมื่อทำงาน General โดยไม่มี corpus.

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
1. **ห้าม fabricate** — ห้ามสร้างชื่อ/ตัวเลข/citation/วันที่ ที่ไม่มีจริง (รายละเอียด §12)
2. **ห้ามทำ Pass 1 + Pass 2 พร้อมกัน** — แก้ rhythm ก่อน vocabulary เสมอ (Two-Pass separation canonical §7)
3. **Voice Profile ต้องมาจาก Level 1–5 Hierarchy** — ไม่มีต้องถาม
4. **Verified AI Signature เท่านั้น** — ใช้ corpus จริง (Corpus Provenance ด้านบน) · งาน EN/Bilingual ดู `07` (24 patterns)
5. **Register Gate ก่อนเสมอ** (§0) — เลือก engine/profile/wording ตาม register · ห้ามเดา Academic
6. **Avoiding AI patterns is only half the job** — ลบ AI ไม่พอ ต้องเติมเสียงมนุษย์ (Mode 6, `08`)
7. **Mandatory Load Manifest** (§4) — โหลดไฟล์ครบก่อนรัน
8. **Full-Coverage Scan** — ตรวจทุกย่อหน้า 100% ห้ามสุ่ม · check ระยะใกล้ใช้ sliding window · รายงาน Scan Coverage

---

## 4. MANDATORY LOAD MANIFEST (บังคับโหลดก่อนเริ่ม)

ไฟล์ใน manifest **บังคับโหลด** ก่อนรัน workflow + บันทึกใน "Files Loaded" ของ report ทุกครั้ง. โครง = **CORE (โหลดทุก branch) + BRANCH-specific (โหลดเฉพาะ branch ที่ผ่าน Register Gate §0)**.

**CORE — โหลดทุกครั้งทุก branch (register-agnostic):**

| Mode | Core files |
|---|---|
| 1 DETECT | `01` (3-Layer) + `06` §4 (EN vocab) + `05a` (ถ้าข้อความไทย — core Thai mechanics register-neutral) |
| 2 EXTRACT | `03` |
| 3 CORRECT | `02` + `04` + `09` + `05a` (ถ้าข้อความไทย) |
| 4 FULL CYCLE | Mode 1 + Mode 3 core |
| 5 SUMMARIZE | none (quick read) |
| 6 ADD SOUL | `08` |

**BRANCH-specific — โหลดเพิ่มตาม branch (เลือก 1):**

| Branch | DETECT (Mode 1) เพิ่ม | CORRECT (Mode 3) เพิ่ม | Profile |
|---|---|---|---|
| 🟩 Academic | `05a` (core) + `05` (academic) + `06` §1-3 (Class A/B) | `05a` + `05` | `KM-TH-THESIS-DOC` |
| 🟧 Business | `11` (B-Check TB/EB + §6) | `11` | `KM-TH-BIZ-DOC` |
| 🟪 General | (core พอ) + watchlist สากล | (core พอ) | core baseline + register tune |
| **+ EN/Bilingual ทุก branch** | + `07` (24 patterns) | + `07` | — |

### Thai Structural Quick-List — TQ rebalance ⭐ V06

โครงสร้างไทยแยก 2 ระดับ: **TQ1-TQ2 = 🟦 CORE (universal ทุก register)** · **TQ3-TQ9 = 🟩 ACADEMIC**.

**🟦 CORE (universal Thai structure — ทุก register):**

| # | กฎ | อ้างอิง |
|---|---|---|
| TQ1 | อนุประโยคซ้อน "ซึ่ง/ที่/อัน" ≤ 2 ชั้น/ประโยค | `05` §1.3 |
| TQ2 | โครงเปิดประโยคเดียวกันห้ามซ้ำใน 5 ประโยค/ย่อหน้า | `01` Check 6 |

**🟩 ACADEMIC (อ้าง `05` thai-academic):**

| # | กฎ | อ้างอิง |
|---|---|---|
| TQ3 | สูตรประโยคสำเร็จรูปต้องรื้อทั้งโครง ไม่ใช่ถอดคำ | `05` §7 |
| TQ4 | Forward signpost ≤ 1 ครั้ง/เอกสาร | `05` §9 |
| TQ5 | Acronym นิยามเต็มครั้งแรกครั้งเดียว | `05` §8 |
| TQ6 | คำ Class A Zero-Tolerance (อย่างก้าวกระโดด ฯลฯ) เจอครั้งเดียวต้องแก้ | `06` §1.6 |
| TQ7 | ย่อหน้าสรุปห้ามเปิดด้วยสูตรสังเคราะห์ | `06` §1.5 |
| TQ8 | ระวัง "การ/ความ" ซ้อน + passive แบบภาษาแปล | `05` §1 |
| TQ9 | กริยารายงานตรงชนิดแหล่ง (งานทัศนะห้าม "พบว่า/พิสูจน์ว่า") | `05` §10 |

> **🟧 Business / 🟪 General quick-list (สมมาตร):** Business → ดู `11` B-Check (TB1-8 TH cadence / EB1-9 EN cadence) + §6 Anti-ลิเก. General → watchlist สากล (`06`§4 + `09`) + register-fit (conversational ชัดเจน).

### ⚠ Corpus-Correct Rule (กันลบคำที่คนใช้จริง) — ใช้ทั้ง 3 branch

- **Class A Zero-Tolerance** (เจอครั้งเดียวแก้): Academic = ยิ่งไปกว่านั้น/ในท้ายที่สุด/ทั้งหมดนี้สังเคราะห์ได้ว่า/อย่างก้าวกระโดด/พลิกโฉม(ใน body)/เป็นที่ทราบกันดีว่า (`06`). Business = ดู `11` (cadence tell B1-B4)
- **Common-in-Real-Thai (🟢 ใช้ได้ density ≤3/500)**: Academic = นอกจากนี้ (156×)/อย่างมีประสิทธิภาพ (195×). Business = ตอบโจทย์/รองรับ/พลิกโฉม(ใน vision) (ดู `11` §3)
- **ห้าม blanket-ban** คำที่ปรากฏใน corpus จริง · คำใหม่ที่สงสัย → Field-Discovered Living List (`06` §1.5) พร้อมวันที่
- **§6.6 ห้ามแปลงศัพท์ไทยใช้จริง** (กระทบยอด/ศัพท์ราชการบัญญัติ/Class A) → keep-Thai · flag เฉพาะ TH-coinage *ทึบกว่า* EN ต่อผู้อ่านเป้าหมาย
- **§6.8 ห้าม flag หางคำในคำประสม/ข้าม line-break** → ผ่าน Particle Boundary Guard (segment-not-substring + line-break-join + clause-final-only + compound-noun-exclusion) ก่อนเสมอ
- **Pass 2 density (5-register)** = SSOT ที่ `06` §5 (นานาชาติ≤2 / TCI≤4 / Business≤3 / ราชการ≤2 / Marketing≤5 ต่อ 1,000 คำ — ใช้กับ Class B เท่านั้น). ที่นี่ชี้ไป ไม่ทำซ้ำ.

---

## 5. MODE 1: DETECT

1. **อ่านข้อความ** — ระบุภาษา ความยาว + **Register Gate (§0)** → เลือก branch: 🟩 Academic / 🟧 Business / 🟪 General (ไม่ชัด = ถาม · ห้ามเดา Academic)
2. **โหลด Core + Branch files (§4)** แล้วรัน **Scan Discipline** (`01` §1.5) — แตกย่อหน้าใส่หมายเลข ตรวจทุกย่อหน้า 100%
3. **🟦 CORE — รัน universal-check (ทุก branch เหมือนกัน)** — ดู `01`:
   - **Layer 1:** Density (Class B) + Zero-Tolerance (Class A — hard gate, Check 1b)
   - **Layer 2 (7 universal):** Burstiness, Sentence Opening, Paragraph Symmetry, Transition Density, Bullet-thinking, Template Proximity, Nested Clause
   - **Layer 3 (universal ส่วน):** Paragraph Length, Personal Voice Markers, Section-Closing Ritual
   - **Thai structure universal:** TQ1-TQ2 (§4)
   - **EN/Bilingual:** EN AI-vocab + EB cadence (`06` §4 + `07`)
4. **🟩🟧🟪 BRANCH — รัน register-specific check (ตาม branch ที่ผ่าน Gate):**
   - **🟩 Academic** — +3 academic-check (Citation Distribution · Reporting-Verb Alignment · Acronym Re-Expansion จาก Layer 3) + Class A/B (`06` §1-3) + TQ3-9
   - **🟧 Business** — B-Check (`11` §5): Cadence TB1-TB8 · Watchlist · Register whitelist (กัน over-correction) · Anchor + Section density · §6 Anti-ลิเก
   - **🟪 General** — watchlist สากล + register-fit (conversational ชัดเจน ไม่ลิเก ไม่ทางการเกิน) · ระบุ limitation ถ้าไม่มี corpus (§2.5)
5. **🟦 CORE — Wording Discipline Layer (§2.3)** — รันคู่: W1-W7 (ความเข้มตาม branch)
6. **Output Detection Report** (`templates/detection_report.md`) — ระบุ Branch + Files Loaded + Scan Coverage 100%

**Pass gate:** ≥13/15 checks ผ่าน · **Check 1b (Class A Zero-Tolerance) = hard-gate** (เจอ ≥1 = Fail ทันที ไม่ว่าคะแนนรวมเท่าใด).

**สถิติที่คำนวณ:** Mean sentence length · SD (≥5) · Tier 1 density/1000 (Class B) · Transition density/500 · Personal Voice Markers count

---

## 6. MODE 2: EXTRACT (สกัด Voice Profile)

1. อ่านโฟลเดอร์อ้างอิง — ดู `03` (5-Level Source Hierarchy)
2. สกัด **6+1 Dimensions** (D1 Sentence Architecture · D2 Vocabulary · D3 Tone/Register · D4 Rhetorical · D5 Structure · D6 Bilingual · D7 Personal/Org Markers) — Profile ID `VP-[YYYYMMDD]-[XXX]`
3. คำนวณ aggregate statistics จาก corpus จริง
4. Output: Voice Profile + Calibration Samples + Profile ID

**หากไม่มีแหล่งอ้างอิง** → เลือกจาก Library (Academic: `KM-TH-THESIS-DOC` · Business: `KM-TH-BIZ-DOC`) หรือถาม (Level 5 = ASK เสมอ). 🟪 General ไม่มี library — ถ้ามีโฟลเดอร์ผู้ใช้ ให้ EXTRACT ก่อน (§2.5).

---

## 7. MODE 3: CORRECT (Two-Pass)

**Two-Pass separation = canonical ที่นี่ (§7).** ส่วนอื่นที่อ้าง "ห้ามรัน Pass 1+2 พร้อมกัน" ชี้กลับมาที่นี่.

**Pre-conditions:** ข้อความ input · Voice Profile (ตาม register) · User-provided facts (Personal Anchors) · Target AI score

### Pass 1: Rhythm Correction
1. ระบุย่อหน้าเสี่ยง (>3/5 ประโยคยาว 16-22 คำ)
2. Burstiness Injection: ตัด 2 ประโยคสั้น (8-12 คำ), ขยาย 1 ยาว (25-35 คำ)
3. Diversify Sentence Opening (5 รูปแบบ) + Proximity Guard
4. Adjust Paragraph Architecture (short/medium/long mix)
5. Verify SD ≥ 5 · **30% shrink gate** (ห้ามตัดเนื้อหาเกิน 30% โดยไม่แจ้ง)

### Pass 2: Vocabulary Correction
1. Search & Replace 9 หมวด (EN Verbs/Adjectives/Nouns/Phrases + Thai openers/modifiers/connectives/hedging + Class A)
2. **Replace by Voice Profile** — D2 Vocabulary Signature ของ profile ที่เลือก (academic ใช้ `KM-TH-THESIS-DOC` · business ใช้ `KM-TH-BIZ-DOC`)
3. ระวัง Symptom Substitution (ห้ามเปลี่ยน AI เป็น AI อีกคำ)
4. เพิ่ม Specificity (Anchor rule สำหรับ business — ดู `11` §4)
5. Template-Level Replace — รื้อโครงสูตร (`05` §7)
6. Reporting-Verb Alignment (`05` §10) — 🟩 Academic
7. **คง Lexical Fingerprint** — 🟧 Business: ห้าม normalize "Advance Modules"/"operation excellency" ถ้า quote ต้นทาง (`11`)
8. **Org-marker lock** — 🟧 Business: "28 ปี / first Oracle Partner / vision / ค่านิยม" ใช้ได้เฉพาะมีในแหล่งจริง ห้าม inject (รายละเอียด §12)

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
        Voice Match Scoring (D1-D6+D7, ≥75% gate) → [Final]
```
ใช้ `Prompt FC1: Full 8-Step Cycle` ใน `templates/correction_prompts.md`

---

## 9. MODE 5: SUMMARIZE

Quick read + feedback (ไม่รัน 3-Layer ครบ): คุณภาพ AI signature โดยรวม · จุดเด่น/จุดอ่อน · ความสอดคล้อง Voice Profile · ข้อแนะนำ

---

## 10. MODE 6: ADD SOUL

**ใช้เมื่อ:** ผ่าน detector แล้วแต่ "อ่านเหมือน AI" / เย็นชา / ไม่มีตัวตน · prose ตีความ = soul-demand สูงสุด

**ขั้นตอน:** อ่าน `08` → รัน Soul Check **7 คำถาม** → เลือก Technique **S1-S6** (S1 Have Opinions / S2 Vary Rhythm / S3 Acknowledge Complexity / S4 Use voice-marker / S5 Let Some Mess In / S6 Be Specific) → ปรับตาม Voice Profile + Soul-calibration ของ branch (§2.2).

**กฎเหล็ก 4:** (1) ห้ามเติม fake personality · (2) ห้าม fabricate emotions · (3) counterargument อิงงานจริง · (4) ใช้ user-provided facts เท่านั้น.

### Worked example — S4 voice-marker ครบ 3 register (สมมาตร)

S4 ("ใช้สรรพนาม/ตัวตน") ไม่ใช่ academic-only — ปรับ voice-marker ตาม register:

| Register | voice-marker | ตัวอย่าง soul-injection |
|---|---|---|
| 🟩 Academic | "ผู้วิจัย" | "ผู้วิจัยเห็นว่าข้อค้นพบนี้ยังมีข้อจำกัด เพราะกลุ่มตัวอย่างจำกัดเฉพาะ…" (มีจุดยืน + acknowledge limitation จริง) |
| 🟧 Business | "เรา / ทีมที่ปรึกษา" | "จากประสบการณ์ของทีมที่ปรึกษาในงานลักษณะนี้ เราพบว่าขั้นตอน migration มักติดที่…" (อิงประสบการณ์จริงของทีม ห้ามกุ) |
| 🟪 General | conversational (ฉัน/ผม/เรา ตามบริบท) | "ผมลองวิธีนี้แล้วได้ผลกับงานจริง — แต่ต้องระวังจุดที่…" (น้ำเสียงคุยกับผู้อ่าน ชัดเจน ไม่ทางการเกิน) |

> ทั้ง 3 ต้องอิง **user-provided facts เท่านั้น** — soul มาจาก fact จริง ไม่ใช่ personality ปลอม (กฎเหล็ก §10).

---

## 11. VOICE PROFILE LIBRARIES

### 🟩 Academic — `voice_profiles/KM-TH-THESIS-DOC_V02R01.md` (7 sub-profiles)
VP-A1 MCU PA Dissertation · A2 MCU Buddhist Integration · B1 AGJ Article · B2 General TCI · C1 Accounting Research · C2 Procurement Research · C3 Public-Sector/Education
**Tier-2 Decision Tree:** มจร? → Buddhist แกน? A2:A1 · ไม่ใช่ มจร → Research(สถิติ)/Academic → วารสาร/สาขา → B1/B2/C1/C2/C3
**AGJ calibration (worked sample):** AGJ readability 5.72 · มจร human-baseline ~60% · x̄ 4.13 SD 0.32 (ดู `10` audit engine)

### 🟧 Business — `voice_profiles/KM-TH-BIZ-DOC_V01R02.md` (8 sub-profiles, corpus-grounded 13 iCE proposals)
Proposal/Narrative · Investment/Commercial · Solution-Response · Manday/Service-Model · Cover-Letter/Transmittal · FSD/Spec · SoW/Technical · Gap-Analysis/Review
**กฎทอง:** register ต่าง section ไม่เท่ากัน — Investment section = value-prose ≈ 0 (ห้าม buzzword) · AI-tell โผล่ใน narrative มากกว่า investment

### 🟪 General — ไม่มี dedicated library (ดู limitation §2.5)
ใช้ core baseline + register tune · ถ้าผู้ใช้มีโฟลเดอร์ตัวอย่าง → Mode 2 EXTRACT สกัดก่อนแก้.

**ถ้าไม่มี sub-profile เหมาะ** → Mode 2 EXTRACT สกัดใหม่จากโฟลเดอร์ผู้ใช้

---

## 12. ANTI-HALLUCINATION SAFEGUARDS (canonical — ทุก Mode) 🟦

**H3 Anti-Hallucination = canonical ที่นี่ที่เดียว.** ส่วนอื่นที่อ้าง "ห้าม fabricate" ชี้กลับมาที่ §12.

- **Mandatory User Fact Input** ก่อน Correction (ตัวเลข/ชื่อ/วันที่ จากผู้ใช้)
- **Mandatory Voice Profile** ก่อน Pass 2
- **Flag Missing Data** เป็น `[NEEDS USER INPUT: ...]`
- **No Citation Generation** — ใช้เฉพาะที่ผู้ใช้ให้ (Citation Guard — 🟩 academic ดู `10` audit)
- **Pass Separation** — ไม่รัน Pass 1+2 พร้อมกัน (กลไก canonical §7)
- **No Voice Profile Fabrication** — Level 5 = ASK
- **Business org-marker lock** — "28 ปี / first Oracle Partner / vision / ค่านิยม" ใช้ได้เฉพาะมีในแหล่งจริงของเอกสารนั้น ห้าม inject อัตโนมัติ
- **Lexical fingerprint preserve** — ห้าม normalize quote ต้นทาง (เช่น "operation excellency") ถ้าเป็นคำของผู้เขียนจริง

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
- **🟩 Academic full-document audit:** ใช้ `10` TAAE 7-Phase (Step 0 Resolve Standard → … → Citation Guard → Final Gate) — shared กับ qa-master.

---

## 15. REFERENCE FILES

> หมายเลข reference (01–12) = **contract** — sections อื่นใน skill นี้ hard-link ด้วยเลขนี้ (`04`/`06`/`07`/`11` โดยเฉพาะ). **ห้ามเปลี่ยนเลข reference.**

| ไฟล์ | เมื่อใช้ |
|---|---|
| `01_three_layer_detection.md` | Mode 1 — methodology + 15 checks (Check 1a/1b + 1-13) + Scan Discipline |
| `02_two_pass_protocol.md` | Mode 3 — Pass 1+2 + Advanced (Two-Pass canonical คู่ §7) |
| `03_voice_extraction_methodology.md` | Mode 2 — 6+1 Dimensions + 5-Level Hierarchy |
| `04_correction_techniques.md` | Catalog 18 Techniques (T1-18) + Anti-Patterns 8 |
| `05a_thai_core_mechanics.md` | 🟦 CORE Mode 1+3 (ไทย register-neutral) — Translationese, Detector-tells, Formulaic Templates, Acronym, Section-Closing, Reporting-Verb mechanism (โหลดทุก branch) |
| `05_thai_academic_patterns.md` | 🟩 Mode 1+3 (ไทย academic เฉพาะ) — ผู้วิจัย/APA · MCU 5 บท/พระไตรปิฎก/มจร 60% · TCI สถิติ (คู่กับ `05a`) |
| `06_verified_ai_signatures.md` | คำ verified AI signature (Corpus Provenance) — Class A/B + §5 density (5-register SSOT) |
| `07_wikipedia_24_patterns.md` | 24 patterns (English/Bilingual) + Severity Triage |
| `08_personality_and_soul.md` | Mode 6 — Soul Technique S1-S6 + 7Q + กฎเหล็ก 4 |
| `09_filler_replacement_table.md` | filler phrases + chatbot artifacts (Pass 2) |
| `10_academic_audit_engine.md` | 🟩 TAAE — ตรวจเอกสารวิชาการทั้งฉบับ 7-Phase (shared กับ qa-master) — Step 0 + Citation Guard + Final Gate |
| `11_business_ai_patterns.md` | 🟧 Business branch — AI-tell + register (Corpus Provenance: 13 iCE) · TB1-8/EB1-9 cadence + §6 Anti-ลิเก + §6.5 Translationese/Calque (C1-12/V1-4) |
| `12_write_clean_card.md` ⭐ | **L1 Write-Clean Card** — สารสกัด top AI-tells (core A + 3 register B + guard C) สำหรับ "เขียนสะอาดตั้งแต่แรก" · ให้ทุก agent ฝัง/อ้าง (prevention) — คู่กับ skill เต็ม (detection) |

> **Note:** `00_MAIN_KB` ถูก archive แล้ว (`archive/00_MAIN_KB_V05R01_DEPRECATED.md`) — ไม่อยู่ใน lazy-load path. `05` ถูก split แล้ว (V06): 🟦 `05a_thai_core_mechanics.md` (core mechanics ภาษาไทย register-neutral — โหลดทุก branch) + 🟩 `05_thai_academic_patterns.md` (academic เฉพาะ). Government Thai ย้ายไป 🟧 `11`.

**Voice profiles:** `KM-TH-THESIS-DOC` (🟩 academic) · `KM-TH-BIZ-DOC` (🟧 business) · 🟪 General = core baseline (ไม่มี library)

---

## 16. WORKFLOW SUMMARY

```
ผู้ใช้พิมพ์ prompt
  → ⭐ Register Gate (§0): "register ไหน?" 🟩 Academic / 🟧 Business / 🟪 General (ไม่ชัด=ถาม · ห้ามเดา Academic)
  → เลือก Mode (1-6)
  → ถามคำถามจำเป็น (Voice source, facts, target score)
  → โหลด CORE + BRANCH files ตาม Manifest (§4)
  → รัน CORE universal-check (register-agnostic) → BRANCH register-specific check
  → ส่ง output ตาม format ที่ prompt กำหนด (ระบุ branch ใน report)
  → เสนอ next step
```

---

## CHANGELOG

- **V06R01 (2026.06.13)** — Major rewrite: **Register-agnostic CORE + 3 Branches เท่าเทียม**. (1) **Register Gate = Tier-1 entry (§0)** ขึ้นก่อนทุกอย่าง — "register ไหน?" ก่อน "Mode ไหน" · ห้ามเดา Academic · ไม่ชัด=ASK. (2) **3-branch symmetric table (§2.2)** — column เท่ากันทุก branch (Engine · Checks · Voice Profile · Soul-calibration); academic ไม่หนากว่า general. (3) **2-Tier tree (§2.5)** — Tier-1 register-gate → Tier-2 sub-profile (academic 7 / business 8 / general blog-email-report พร้อม limitation note ว่าไม่มี dedicated corpus). (4) **de-dup → SSOT+pointer**: Corpus Provenance (292K/13 iCE) รวมเหลือ 1 บรรทัด (เดิมซ้ำ 4 จุด) · Anti-Halluc H3 canonical §12 เท่านั้น · Two-Pass separation canonical §7 · density 5-register → pointer ไป `06`§5. (5) **TQ rebalance** — TQ1-2 → 🟦 CORE (universal Thai structure) · TQ3-9 → 🟩 academic · เพิ่ม business/general quick-list pointer (สมมาตร). (6) **Mode 6 worked example** ครบ 3 register — S4 voice-marker: academic "ผู้วิจัย" / business "เรา/ทีมที่ปรึกษา" / general conversational (ไม่ใช่ academic-only). (7) **corpus asymmetry note** — 292K academic vs 13 iCE = data-availability ไม่ใช่ priority ranking. (8) §15 ลบ `00_MAIN_KB` (archived) + note `05a` ถ้า ref-phase split. CORE ระบุชัด "register-agnostic ไม่มี academic default". MUST-KEEP numbers + qa-master D5 circular guard คงครบ.
- **V05R01 (2026.06.13)** — Major restructure: **Shared Core + 3 Branches**. แยก "กลไก AI-tell สากล" = 🟦 CORE (12 universal-check, `06`§4 EN vocab + `07`, two-pass `02`, voice-extract `03`, techniques `04`, filler `09`, soul `08`, wording W1-W5, anti-halluc H3) ออกจาก "register เฉพาะทาง" = 3 branch (🟩 Academic: `05`+`06`§1-3+TQ1-9+`10`+3 academic-check · 🟧 Business: `11` B-Check TB/EB+§6+Anchor+fingerprint · 🟪 General: core+register-tune). Manifest แยก Core + Branch-specific. เตรียมรองรับ L1 Write-Clean Card.
- **V04R02 (2026.06.13)** — ขยาย Business corpus 6→13 iCE proposals. `KM-TH-BIZ-DOC` V01R02: 8 sub-profiles + register ยืนยัน + Reframe/Citation-to-source. `11_business_ai_patterns` V01R02: +TB1-TB8 +EB1-EB9 +ANTI-ลิเก Catalog (L1-L8/P1-P9 + GUARD) +watchlist. Scope clarify: voice profile เก็บ "ลายเซ็นภาษา" ไม่ใช่ "ค่าตัวเลของค์กร".
- **V04R01 (2026.06.12)** — Major: เพิ่ม Business Engine ในตัว (Content-Type Gate 3 ประเภท + `KM-TH-BIZ-DOC` + `11_business_ai_patterns.md`). Restructure ลำดับเป็นเส้นตรง.
- **V03R02 (2026.06.12)** — Content-Type Gate + Wording Discipline + Corpus-Correct Rule + fix 7 defects.
- **V03R01 (2026.06.07)** — 15 จุดตรวจ + Zero-Tolerance Class + Field-Discovered Living List + Mandatory Load Manifest + Full-Coverage Scan.
- **V02 (2026.06)** — Mode 6 ADD SOUL + 24 Wikipedia patterns + 18 Correction Techniques.

*Corpus Provenance: งานวิจัยไทย 101 ไฟล์ (~292K คำ) + เอกสารธุรกิจ iCE 13 proposals — ดู references `06` (academic) / `11` (business). asymmetry = data-availability ไม่ใช่ priority.*
