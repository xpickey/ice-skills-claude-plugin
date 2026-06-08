# Correction Prompt Templates

## Prompt C-Pass1: Rhythm Correction Only

```
Apply ONLY Pass 1: Rhythm Correction to the text below.
DO NOT modify vocabulary in this pass.

Step 1.1: Identify at-risk paragraphs (>3 of 5 sentences are 16-22 words)
Step 1.2: Burstiness Injection
   - Shorten 2 sentences to 8-12 words
   - Expand 1 sentence to 25-35 words with specific details
Step 1.3: Diversify sentence openings using:
   - Adverb / Subordinate Clause / Question / Quote / Prepositional phrase
Step 1.4: Adjust paragraph architecture for length variability
Step 1.5: Verify SD ≥ 5 per paragraph

CONSTRAINTS:
- Do NOT replace any vocabulary in this pass
- Do NOT invent facts, names, numbers
- Mark missing data as [NEEDS USER INPUT: <what>]

Source facts the user has provided: <<<USER_FACTS>>>
Text: <<<TEXT>>>

OUTPUT:
1. Pass 1 rewritten text
2. Burstiness report (SD per paragraph before/after)
3. Sentence opening diversity report
4. [NEEDS USER INPUT] flags
```

---

## Prompt C-Pass2: Vocabulary Correction with Voice Profile

```
Apply ONLY Pass 2: Vocabulary Correction to the text below.
The text has already passed Pass 1 (Rhythm) — DO NOT alter rhythm in this pass.

Voice/Writing Profile to follow: <<<VOICE_PROFILE>>>

Step 2.1: Search & Replace by category (in this order, ใช้ 06_verified_ai_signatures.md):
   1. Tier 1 English Verbs
   2. Tier 1 English Adjectives
   3. Tier 1 English Nouns
   4. AI Phrase Templates
   5. Thai sentence openers (Verified Confirmed AI Signatures)
   6. Thai over-modifiers
   7. Thai connectives
   8. Hedging phrases

Step 2.2: Choose replacements per the Voice Profile (not 1:1 from table)
Step 2.3: Avoid Symptom Substitution (don't replace AI word with another AI word)
Step 2.4: Add Specificity — every vague modifier becomes concrete data

CONSTRAINTS:
- Do NOT alter sentence rhythm or paragraph structure
- Do NOT invent facts, names, numbers
- Mark missing data as [NEEDS USER INPUT]

Source facts: <<<USER_FACTS>>>
Text (already Pass 1-corrected): <<<TEXT>>>

OUTPUT:
1. Pass 2 rewritten text
2. Vocabulary change log (8 categories)
3. Specificity additions log
4. [NEEDS USER INPUT] flags
```

---

## Prompt C-TwoPass: Combined Two-Pass

```
Apply the AI Correction Protocol Two-Pass Method to the text below.
Execute Pass 1 first, then Pass 2 — never simultaneously.

Voice Profile: <<<VOICE_PROFILE>>>
Source facts: <<<USER_FACTS>>>
Text: <<<TEXT>>>

PASS 1 — Rhythm Correction (5 Steps): [perform per Prompt C-Pass1]
→ Output Pass 1 result and Burstiness verification

PASS 2 — Vocabulary Correction (4 Steps): [perform per Prompt C-Pass2]
→ Output Pass 2 result and Vocabulary verification

ADVANCED TECHNIQUES (only if AI score remains high):
A. Sentence Combining & Splitting
B. Personal/Cultural Markers
C. Aside & Qualification (use em dash sparingly in Thai)
D. Imperfect Flow

FINAL OUTPUT:
1. Final corrected text
2. Pass 1 change log
3. Pass 2 change log
4. Advanced techniques applied (if any)
5. [NEEDS USER INPUT] remaining
```

---

## Prompt C2-Academic (Thai/EN)

```
Apply Two-Pass Method to academic text targeting [Journal Standard].

Voice Profile: ผู้วิจัยระดับ [Ph.D./Master] สาขา [field],
ภาษาไทยวิชาการ, [APA นาม-ปี / เชิงอรรถ มจร],
ใช้ศัพท์ราชบัณฑิตยสภา, หลีกเลี่ยงคำตลาด

Pass 1: Rhythm — เน้นการสลับประโยคยาวอภิปราย กับประโยคสั้นสรุปประเด็น
Pass 2: Vocabulary — เปลี่ยนสรรพนาม "เรา" → "ผู้วิจัย"
                    เปลี่ยน "งานวิจัยพบว่า" → "[ชื่อ] ([ปี]) พบว่า…"

ห้ามสร้าง citation ปลอม ทุกการอ้างอิงต้องมาจากแหล่งจริงที่ผู้วิจัยให้
```

---

## Prompt C2-MCU-Buddhist (Thai)

```
Apply Two-Pass Method to MCU dissertation text (Profile A2).

Voice Profile:
- ผู้วิจัยระดับปรัชญาดุษฎีบัณฑิต สาขารัฐประศาสนศาสตร์ มจร
- เลขไทย (๑ ๒ ๓), พุทธศักราช
- "ผู้วิจัย" + "รูปหรือคน"
- เชิงอรรถ + พระไตรปิฎก ฉบับ มจร พ.ศ. ๒๕๓๙
- หลักธรรม: <<<DHAMMA>>> (ระบุ เช่น ไตรสิกขา/อิทธิบาท ๔/พรหมวิหาร ๔)

Pass 1: Rhythm
   - บทคัดย่อ: "การวิจัยนี้มีวัตถุประสงค์ ๑. เพื่อ..."
   - บทที่ ๑: เปิดด้วยกฎหมาย/ประวัติเรื่องที่วิจัย
Pass 2: Vocabulary
   - หลักธรรมต้องใช้ตรงตามคู่มือ มจร
   - ห้ามคำตลาด (ขับเคลื่อน...ใน proposal ก็ใช้ได้แต่ใน MCU ต้องระวัง)

ห้ามสร้างเลขข้อพระไตรปิฎกที่ไม่มีจริง
ห้ามสร้างชื่อผู้แต่งหรือปีพิมพ์ที่ไม่มีจริง
```

---

## Prompt FC1: Full 8-Step Cycle

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
