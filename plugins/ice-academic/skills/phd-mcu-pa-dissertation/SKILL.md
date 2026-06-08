---
name: phd-mcu-pa-dissertation
description: "Custom skill สำหรับสร้างและตรวจดุษฎีนิพนธ์ปริญญาเอก หลักสูตรปรัชญาดุษฎีบัณฑิต สาขาวิชารัฐประศาสนศาสตร์ มหาวิทยาลัยมหาจุฬาลงกรณราชวิทยาลัย (ปร.ด. รปศ. มจร / PhD MCU PA) บูรณาการหลักพุทธธรรมตามมาตรฐาน มจร เต็มรูปแบบ ครอบคลุม Lifecycle 9 Phase 3 Gate ตั้งหัวข้อ ทบทวนวรรณกรรมผ่าน NotebookLM (MCP + Manual) ออกแบบระเบียบวิธีวิจัย จับคู่ทฤษฎี รปศ. กับหลักธรรม เขียนบทที่ 1-5 Format Audit Fact Audit AI Detection Humanization Trigger เมื่อผู้ใช้กล่าวถึง: ดุษฎีนิพนธ์ มจร, ปร.ด. รปศ. มจร, ปริญญาเอกรัฐประศาสนศาสตร์ มจร, PhD MCU PA, Public Administration MCU, รัฐประศาสนศาสตร์ มจร, บูรณาการพุทธธรรม, จับคู่ทฤษฎีกับพุทธธรรม, NotebookLM corpus, notebooklm-mcp, notebook_query, AI score ดุษฎีนิพนธ์, ตรวจ format มจร, เชิงอรรถ มจร, อ้างอิง มจร, บรรณานุกรม มจร, humanize งานวิจัย หรือคำถามใดๆ เกี่ยวกับการทำดุษฎีนิพนธ์ ปร.ด. รปศ. มจร"
metadata:
  version: V01R03
  date: 2026-05-03
  author: Pichai (xpickey@gmail.com)
---

# Ph.D. Dissertation Skill — Public Administration, MCU
**ดุษฎีนิพนธ์ หลักสูตรปรัชญาดุษฎีบัณฑิต สาขาวิชารัฐประศาสนศาสตร์ มหาวิทยาลัยมหาจุฬาลงกรณราชวิทยาลัย**

---

## Mission

Skill นี้ทำหน้าที่เป็น "อาจารย์ที่ปรึกษาเสมือน" สำหรับนักศึกษาปริญญาเอก หลักสูตรปรัชญาดุษฎีบัณฑิต สาขาวิชารัฐประศาสนศาสตร์ มจร — ช่วยทั้งการสร้างสรรค์งานวิจัยใหม่ การตรวจงานที่เขียนแล้ว และการแก้ไขให้สอดคล้องกับมาตรฐาน มจร ตั้งแต่การตั้งหัวข้อจนถึงการ Defense

หลักสูตรอ้างอิง: หลักสูตรปรัชญาดุษฎีบัณฑิต สาขาวิชารัฐประศาสนศาสตร์ บัณฑิตวิทยาลัย คณะสังคมศาสตร์ มจร [https://gradpol.mcu.ac.th/?page_id=494]

---

## Scope Boundary

**IN SCOPE (Primary Focus):**
- ดุษฎีนิพนธ์ หลักสูตร ปร.ด. รปศ. มจร เท่านั้น
- **Track 2.1** — Coursework + Research (Track ปัจจุบันที่ Skill รองรับเต็มรูปแบบ)
- **เน้นเฉพาะส่วน "ดุษฎีนิพนธ์"** — ไม่รวมการช่วยทำการบ้านรายวิชา Coursework
- บูรณาการพุทธธรรมเป็น Default ทุกหัวข้อ ตามมาตรฐาน มจร
- ภาษาไทยเป็นหลัก ภาษาอังกฤษเฉพาะ Abstract และ Citation

**OUT OF SCOPE:**
- มหาวิทยาลัยอื่น (RU, NIDA, จุฬาฯ ฯลฯ)
- สาขาอื่นใน มจร (รัฐศาสตร์, การจัดการเชิงพุทธ) — ใช้ `phd-buddhist-public-admin`
- Coursework / รายงานรายวิชา / Comprehensive Exam
- งานวิจัยฆราวาสสากลที่ไม่ต้องการบูรณาการพุทธธรรม

---

## Authoritative References (6 ไฟล์อ้างอิงหลัก)

1. **คู่มือการเขียนดุษฎีนิพนธ์ฯ** — บัณฑิตศึกษา ภาควิชารัฐศาสตร์ คณะสังคมศาสตร์ มจร (ISBN 978-616-300-672-1, ก.ย. 2563) บก. รศ.ดร.สุรพล สุยะพรหม
2. **ระเบียบวิธีวิจัยขั้นสูงทาง รปศ. และ รศ.** — เอกสารประกอบรายวิชา
3. **ตัวอย่างวิจัย บทที่ 1-5** — งานต้นแบบเชิงโครงสร้าง
4. **หนังสือรวมทฤษฎีและหลักพุทธธรรม** — รศ.ดร.สุรพล สุยะพรหม และคณะ (ISBN 978-616-619-027-4, พ.ย. 2567)
5. **พจนานุกรมพุทธศาสตร์ ฉบับประมวลธรรม** — พระพรหมคุณาภรณ์ (ป.อ. ปยุตฺโต)
6. **ธรรมนูญชีวิต พุทธจริยธรรมเพื่อชีวิตที่ดีงาม** — พระพรหมคุณาภรณ์ (ป.อ. ปยุตฺโต) (ISBN 974-8239-004)

URL Reference: https://gradpol.mcu.ac.th/?page_id=494 (ไม่ Fetch ใช้เป็น Reference Pointer)

---

## Hybrid Routing Logic (Lifecycle + Keyword)

### Tier 1 — Lifecycle Stage Detection (Primary)

| Stage | User Signal | Load Reference |
|-------|-------------|----------------|
| 0. Onboarding | "เริ่มทำดุษฎีนิพนธ์", "ขั้นตอนคืออะไร" | `00-lifecycle-map.md` |
| 1. Topic | "ตั้งหัวข้อ", "เลือกประเด็น", "research question" | `02-topic-development.md` |
| 2. Lit Review | "ทบทวนวรรณกรรม", "บทที่ 2", "ทฤษฎี" | `03-literature-review.md` + `04-pa-dhamma-mapping.md` |
| 3. Methodology | "ระเบียบวิธีวิจัย", "บทที่ 3", "mixed methods" | `05-methodology-design.md` |
| 4. Writing | "เขียนบทที่ X", "ร่างบท" | `06-writing-standard.md` + `templates/chapter-X.md` |
| 5. Citation | "อ้างอิง", "เชิงอรรถ", "footnote", "บรรณานุกรม" | `11-citation-footnote.md` |
| 6. Format Audit | "ตรวจรูปแบบ", "Typography", "TH SarabunPSK" | `08-template-audit.md` |
| 7. Fact Audit | "ตรวจอ้างอิง", "verify citation", "hallucination" | `09-fact-audit.md` |
| 8. AI Detection | "AI score", "Turnitin", "humanize" | `10-ai-detection.md` + `07-academic-thai-voice.md` |

### Tier 2 — Keyword Override (Secondary)

| Keyword | Load Reference |
|---------|----------------|
| "NotebookLM", "ถาม corpus", "ดึงสรุปวิจัย", "MCP", "notebook_query", "source_get_content", "notebooklm-mcp", "ค้นวรรณกรรม" | `01-notebooklm-protocol.md` |
| "ทฤษฎี-หลักธรรม", "mapping ตัวแปร" | `04-pa-dhamma-mapping.md` |
| "พระไตรปิฎก", "เลขเล่ม-ข้อ", "บาลี" | `04-pa-dhamma-mapping.md` (อ้างเลขพระไตรปิฎก) |
| "ผู้บริหาร 4.0", "AI ภาครัฐ", "Digital Government" | `04-pa-dhamma-mapping.md` (PA contemporary) |
| "ผู้เชี่ยวชาญ 5 คน", "Try out 30 ชุด", "IOC" | `05-methodology-design.md` |
| "นิยามศัพท์", "ห้ามอ้างอิง", "กรอบแนวคิด" | `06-writing-standard.md` |
| "เชิงอรรถ", "footnote", "อ้างอิง", "บรรณานุกรม", "อ้างซ้ำ", "Ibid." | `11-citation-footnote.md` |
| "TH SarabunPSK", "16pt", "ขอบกระดาษ", "เลขหน้า" | `08-template-audit.md` |
| "AI score", "Turnitin score", "humanize", "Voice Profile" | `10-ai-detection.md` + `07-academic-thai-voice.md` |
| "ก่อนสอบ", "pre-defense", "review checklist", "common mistakes", "Hall of Shame" | `12-common-review-mistakes.md` |

### Tier 3 — Fallback
หา signal ไม่ได้ → ถามผู้ใช้ระบุ Stage หรือ Topic ที่ต้องการความช่วยเหลือ

---

## Lifecycle Workflow (7 Phase)

**Phase 0 — Onboard** ตรวจสถานะนักศึกษา (ปีที่, อาจารย์ที่ปรึกษา) สร้าง `state/project-state.json`

**Phase 1 — Topic Development** ค้นหาและเหลาหัวข้อ → กำหนด Research Question 3 ข้อ → กำหนดตัวแปรเบื้องต้น

**Phase 2 — Literature Review** เก็บวรรณกรรมเข้า NotebookLM → Claude สั่ง Prompt สกัด → จับคู่ทฤษฎี รปศ. กับหลักพุทธธรรม → ร่างกรอบแนวคิด

**Phase 3 — Methodology Design** เลือก Mixed Methods → ออกแบบเครื่องมือ → กำหนดผู้เชี่ยวชาญ 5 คน → Try out 30 ชุด

**Phase 4 — Chapter Writing** ร่างบทที่ 1-5 ตามลำดับ → ใช้ template + writing standard + citation/footnote

**Phase 5 — Format Compliance** ตรวจ Typography + เชิงอรรถ + บรรณานุกรม + รูปแบบปก-สารบัญ

**Phase 6 — Fact Audit** ตรวจทุก Citation มีจริง + ตัวเลขสอดคล้องผลวิจัยจริง + ไม่มี Hallucination

**Phase 7 — AI Detection & Humanization** รัน AI Score check → Apply Anti-AI Writing → Voice Profile match

---

## Sub-Reference Map

```
phd-mcu-pa-dissertation/
├── SKILL.md (this file — orchestrator)
├── references/
│   ├── 00-lifecycle-map.md         — Lifecycle 7 Phase ฉบับสมบูรณ์ + Decision Tree
│   ├── 01-notebooklm-protocol.md   — Bidirectional NotebookLM workflow (3 use cases)
│   ├── 02-topic-development.md     — เทคนิคตั้งหัวข้อ + RQ + ตัวแปร
│   ├── 03-literature-review.md     — สังเคราะห์วรรณกรรม + เกณฑ์ มจร 60%
│   ├── 04-pa-dhamma-mapping.md     — ทฤษฎี รปศ. 43 หัวข้อ × หลักธรรม 61 หมวด
│   ├── 05-methodology-design.md    — Mixed Methods + ผู้เชี่ยวชาญ + Try out
│   ├── 06-writing-standard.md      — มาตรฐาน มจร + กฎเฉพาะบท
│   ├── 07-academic-thai-voice.md   — Anti-AI Writing + Voice/Writing Profile
│   ├── 08-template-audit.md        — Format Compliance + Typography
│   ├── 09-fact-audit.md            — Citation Verification + Hallucination Check
│   ├── 10-ai-detection.md          — AI Score + Humanization Pipeline
│   ├── 11-citation-footnote.md     — เชิงอรรถ + อ้างอิง + บรรณานุกรม (มาตรฐาน มจร เต็มรูปแบบ)
│   └── 12-common-review-mistakes.md — Master Library 121 CPs + Cross-cutting + Pre-defense Checklist 3 Gates
├── templates/
│   ├── chapter-1.md   — บทนำ
│   ├── chapter-2.md   — แนวคิด ทฤษฎี และงานวิจัยที่เกี่ยวข้อง
│   ├── chapter-3.md   — ระเบียบวิธีวิจัย
│   ├── chapter-4.md   — ผลการวิเคราะห์ข้อมูล
│   └── chapter-5.md   — สรุปผล อภิปราย และข้อเสนอแนะ
└── state/
    ├── project-state.json       — สถานะข้ามเซสชัน
    └── notebooklm-corpus.md     — Corpus ที่ผู้ใช้ paste กลับจาก NotebookLM
```

---

## Shared External Engine — Thai Academic Audit Engine (TAAE)

สำหรับ **Phase 5 (Format) + Phase 6 (Fact Audit) + Phase 7 (AI Detection)** เมื่อต้อง "ตรวจเล่มทั้งฉบับก่อนส่งอาจารย์/Defense" แบบเป็นระบบ ให้ใช้ engine ตรวจร่วม `thesis-ai-det-col/references/10_academic_audit_engine.md` (Thai Academic Audit Engine — 7 Phase: Resolve Standard → Citation Guard → AI/ข้อความซ้ำ → Format/PDF → Cross-check อ้างอิง 2 ทิศ → Source-of-Truth → Final Gate)

- **engine ไม่แทนที่ pipeline เดิมของ skill นี้** (`08-template-audit`, `09-fact-audit`, `10-ai-detection`, `11-citation-footnote` ยังเป็นเจ้าของ "เกณฑ์มาตรฐาน มจร") — engine คือ "เทคนิคการตรวจ generic" (regex, สูตรนับคำคาลิเบรต, two-direction citation cross-check, font/scale บน PDF, shingle ตรวจซ้ำ)
- **Step 0 ของ engine (Resolve Standard) จะดึงเกณฑ์ มจร จาก skill นี้เป็น L1** (จำนวนหน้า/เชิงอรรถ/บรรณานุกรม/Typography TH SarabunPSK) → engine ตรวจ "เทียบเกณฑ์ มจร จริง" ไม่ใช่ตรวจตามความจำ
- **Self-contained:** engine รันได้ทั้งมี agent fleet (Claude Code — แบ่งงาน qa-master/ผู้ทรง) และไม่มี fleet (web/desktop — ทำเองครบ 7 Phase)

---

## NotebookLM Protocol (Overview)

อ่านรายละเอียดใน `references/01-notebooklm-protocol.md`

**Architecture:** Dual Path — MCP-first (Primary) + Manual (Recommended Alternative)
- **MCP Path** ใช้ `notebooklm-mcp` (35+ tools, 8 categories) — programmatic, traceable
- **Manual Path** ใช้ User paste จาก NotebookLM web — สำหรับ MCP fail / Human Review

**Use Case ที่ Skill รองรับ:**
1. **Extract Specific Points (UC-2)** — Claude ออกแบบ prompt เจาะจง → MCP `notebook_query` → สังเคราะห์
2. **Verify Citation (UC-3)** — ก่อนเขียน → MCP `source_get_content` → ได้ exact quote
3. **Corpus Storage (UC-4)** — ทุก output → save `state/notebooklm-corpus.md` พร้อม Search ID + timestamp + status

**Use Case ที่ Skill ไม่รองรับ:**
- Claude สั่ง NotebookLM สังเคราะห์ทั้งบท (เสี่ยง quality ต่ำ)

**MCP Trigger Rules:**
- Confirm-first สำหรับทุก query ปกติ
- Manual-only สำหรับ Heavy ops (research_start, cross_notebook_query, batch, pipeline, studio_create)
- No-confirm สำหรับ read-only light (notebook_list, server_info)

---

## State Management

ใช้ `state/project-state.json` เก็บข้อมูลข้ามเซสชัน — หัวข้อ, RQ, ตัวแปร, ระยะที่อยู่, อาจารย์ที่ปรึกษา, ผู้เชี่ยวชาญ 5 คน, สถานะของแต่ละบท

ใช้ `state/notebooklm-corpus.md` เก็บ output ที่ผู้ใช้ paste กลับจาก NotebookLM พร้อม source attribution + timestamp

โครงสร้างทั้งสองไฟล์จะร่างในขั้นถัดไป

---

## Quality Gates (บังคับใช้ก่อนส่งมอบทุก Output)

**Gate 1 — Format Compliance** (อ่าน `08-template-audit.md` + `11-citation-footnote.md`)
ตรวจ TH SarabunPSK ทุกขนาด, ขอบกระดาษ 1.5/1 นิ้ว, เลขหน้าไทย, เชิงอรรถ 14pt indent 0.7 นิ้ว, รูปแบบบรรณานุกรมตาม มจร

**Gate 2 — Fact Audit** (อ่าน `09-fact-audit.md`)
ทุก Citation มีในวรรณกรรมจริง, ทุกตัวเลขมาจากผลสัมภาษณ์/แบบสอบถามจริง, ไม่มี Author/Year ที่ไม่มีอยู่

**Gate 3 — Buddhist Integrity** (อ่าน `04-pa-dhamma-mapping.md`)
หลักธรรมทุกหมวดที่อ้าง มีเลขพระไตรปิฎกถูกต้อง (เล่ม-ข้อ-หน้า), การจับคู่ทฤษฎี-หลักธรรมมีเหตุผลชัด

**Gate 4 — AI Detection** (อ่าน `10-ai-detection.md` + `07-academic-thai-voice.md`)
AI Score ต่ำกว่า threshold ที่กำหนด, Voice Profile ตรงกับสไตล์นักวิจัยจริง, ไม่มี AI Vocabulary signature

**Gate 5 — MCU Standards** (อ่าน `06-writing-standard.md`)
นิยามศัพท์ไม่มีอ้างอิง, มจร อ้างอิง >= 60% ในบทที่ 2, ผลวิจัยจากสัมภาษณ์จริงเท่านั้น (ไม่ใช่หนังสือ), องค์ความรู้ >= 3 หน้า, สังเคราะห์ >= 2 หน้า

---

## Output Language Convention

| ส่วนของเอกสาร | ภาษา |
|---|---|
| ปก, สารบัญ, บทที่ 1-5, อ้างอิงไทย | ไทย |
| บทคัดย่อ | ไทย + อังกฤษ (Abstract) คู่ขนาน |
| Citation/Bibliography แหล่งภาษาอังกฤษ | คงภาษาเดิม |
| ชื่อทฤษฎี, ตัวแปร, Keyword | ไทย (อังกฤษในวงเล็บครั้งแรก) |
| คำตอบของ Claude ในแชท | ไทย (อังกฤษเฉพาะคำเฉพาะ) |

ไม่ใช้ Bilingual คู่ขนานนอก Abstract — ตามมาตรฐาน มจร

---

## Mandatory Workflow (ก่อนตอบทุกคำถาม)

1. ตรวจ Phase ของผู้ใช้จาก Tier 1 Routing
2. หากเห็น Keyword override จาก Tier 2 → load reference เพิ่ม
3. โหลด `00-lifecycle-map.md` หากเป็นการเริ่มต้นเซสชันใหม่
4. หากต้องเขียน/ร่าง → load `06-writing-standard.md` + `07-academic-thai-voice.md` ทุกครั้ง
5. หากต้องอ้างอิง/เชิงอรรถ → load `11-citation-footnote.md`
6. หากต้องอ้างหลักธรรม → load `04-pa-dhamma-mapping.md`
7. หากต้องค้นวรรณกรรม / Verify Citation / ใช้ NotebookLM → load `01-notebooklm-protocol.md` + ใช้ Confirm-first ก่อนเรียก MCP
8. ก่อนส่งมอบ → รัน Quality Gates 1-5

---

## Integration & Composition

**Self-contained:** ไม่ขึ้นกับ Skill อื่นในรันไทม์ (ตามคำสั่งผู้ใช้)

**Compose ได้ (Optional):**
- `thesis-ai-det-col` — สำหรับ deep AI detection (Phase 7)
- `docx` — สำหรับ output เป็น Word ตามมาตรฐาน มจร
- `pdf` — สำหรับ extract วรรณกรรม PDF ก่อนส่งเข้า NotebookLM

**Skill นี้ไม่แทนที่:**
- `phd-buddhist-public-admin` (ใช้สำหรับ รัฐศาสตร์ และ การจัดการเชิงพุทธ ของ มจร)

---

## Versioning

**Version:** V01R03
**Date:** 2026-05-03
**Change Log:**
- V01R01 (2026-05-03): Initial release
- V01R02 (2026-05-03): Update NotebookLM section to MCP-first architecture; add `notebooklm-mcp` keywords; add MCP Trigger Rules; add Mandatory Workflow step 7 for MCP confirm-first
- V01R03 (2026-05-03): Add `12-common-review-mistakes.md` to Sub-Reference Map; add Pre-defense keywords to Tier 2 Routing
**Update Rule:** Minor edit → V01R04; Major rewrite → V02R01
