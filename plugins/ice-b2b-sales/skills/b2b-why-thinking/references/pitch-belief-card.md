# Pitch-Belief Card (L1 SSOT) — V01R01

> **Source of truth = ไฟล์นี้.** 4 homes ชี้มาที่นี่ — carry เฉพาะ layer ของตัวเอง (application) **ไม่ restate framework / research / techniques ซ้ำ**. (เหมือน L1 Write-Clean Card pattern) · register-neutral · หนึ่งหน้า.

## CORE THESIS
**Big-Idea × Visual-that-convinces × Technical-Story-that-assures** — คิดมุม Creative + Producer + Production พร้อมกัน.
**Enemy จริง = buyer indecision + committee misalignment** ไม่ใช่ idea อ่อน. หน้าที่ยากสุด = ทำให้ทั้งห้องเชื่อว่า "ฝันสร้างได้จริง และเราคือคนสร้าง".

## THE 5 LESSONS (บทเรียน · research anchor · technique · owning layer)

| # | บทเรียน | research anchor | technique | owning layer |
|---|---|---|---|---|
| **L1** | ลูกค้าซื้อ **ความเชื่อ** ไม่ใช่ไอเดีย | buyer decision-confidence คือตัวชี้ขาด ไม่ใช่คุณภาพ solution — confident buyer ซื้อ/ขยาย **~2.6x** `[source: Gartner 2019 "confident in their decision"]`; sense-making reps ปิด high-quality low-regret deal **~80%** `[source: Gartner sense-making]` | เปลี่ยนโจทย์ pitch จาก "พิสูจน์ solution ดีสุด" → "ทำให้ลูกค้ามั่นใจว่าเลือกถูก + เราส่งได้จริง" | **HOME 1** SELLING STANCE + **HOME 2** PHILOSOPHY |
| **L2** | ความสวย ≠ ความน่าเชื่อถือ (ยิ่งสวยยิ่งต้องมีหลักฐาน) | aesthetic ↑ perceived credibility ใน **~3.4s** (amelioration effect, **p<0.001**) `[source: cognitive-fluency/amelioration study]` — **แต่** ข้อมูล high-quality/แน่นเกิน → buyer down-scope/stall **~153%** `[source: Gartner 2019 information overload]`. polish ชนะเฉพาะเมื่อ **aid comprehension** (processing fluency) ไม่ใช่เพิ่ม density | prune ไม่ pile · ทุก visual เด่นต้องชี้ไปที่หลักฐาน (reference/man-day/architecture) ไม่ใช่ตกแต่งที่ว่าง | **HOME 4** VISUAL CREDIBILITY |
| **L3** | ขาย **อนาคต** ไม่ใช่ deck | vision/reframing pays เฉพาะบาง stage — solution-exploration **~+41%**, requirements-building **~+28%** `[source: buyer-enablement journey research — to confirm exact figures]` ไม่ใช่ทุกสไลด์ | future-state immersion timed ตาม stage · ให้ลูกค้าเห็น To-Be ของตัวเอง (data จริง, day-in-the-life) ไม่ใช่ generic demo | **HOME 3** STRUCTURE |
| **L4** | Storytelling = **2 ภาษา** (ฝัน + จริง) | indecision = **~56%** ของ no-decision (FOMU) `[source: Challenger/JOLT indecision]`; committee misalignment ทำ stall **~40%+**, **~74%** ทีมขัดแย้ง `[source: Challenger Customer]` — de-risk + alignment สำคัญกว่า idea ใหญ่ | vision (Why Change/Now) **ต้องคู่กับ** proof/feasibility (architecture/man-day/ops/migration) ที่ลด perceived risk | **HOME 2** NARRATIVE |
| **L5** | deck = **design piece** (ทุกอย่างมีผล รวมชื่อไฟล์) | aesthetic = competence signal (amelioration) แต่ต้อง aid comprehension `[source: amelioration study]` | zero-defect deck (font/grid/naming/version) = สัญญาณ delivery-quality · sloppy deck = ลูกค้าอ่านว่าโปรเจกต์จะ sloppy | **HOME 4** VISUAL CREDIBILITY |

> **⚠ H3/P5:** ตัวเลขวิจัยทุกตัวมี `[source]`/`[to confirm]` — ห้าม hard-code เลขลอยในงานลูกค้า. ยืนยันจาก deep-research 2026.07.04 (verified 3-0): Gartner (biggest-challenge / confident-decisions / sense-making), Challenger (indecision/JOLT, Challenger Customer), + วิจัยวิชาการ cognitive-fluency/amelioration.

## APPLICATION MAP + ANTI-BLEED (contract — หนึ่ง layer ต่อ home)

| Home | OWNS (layer เดียว) | NOT (ปล่อยให้เพื่อนบ้าน) |
|---|---|---|
| **HOME 1** ยอดนักขาย (sales-process) | **SELLING STANCE** — ตอนเขียน content Solution/Proposal: เรียง belief→narrative→proof · ทุก vision line ผูก de-risk fact | NOT belief *philosophy* (→ `right-why-philosophy.md`) · NOT visual density (HOME 4) · NOT deck order (HOME 3) |
| **HOME 2** b2b-why-thinking | **PHILOSOPHY + NARRATIVE** — belief core + WHY แต่ละข้อพูด 2 เสียง (ฝัน+จริง) | NOT slide order/timing (HOME 3) · NOT 5-lesson thesis (= card นี้) |
| **HOME 3** b2b-presentation-creator | **STRUCTURE** — ลำดับสไลด์ + stage-timing ที่ de-risk (belief↔proof สลับ, future-state placement) | NOT two-voice *copy* (HOME 2) · NOT visual craft ราย object (HOME 4) |
| **HOME 4** เจนนี่ (deliverable-gen) | **VISUAL CREDIBILITY** — อ่านคะแนน 6-Axis เป็น buyer delivery-signal | NOT axis *definitions* (= presentation-creator §0.5.6) · NOT deck structure (HOME 3) · NOT slop *detection* (qa-master D7.S — เจนนี่ *ป้องกัน* pre-emit) |

## CHANGELOG
- **V01R01 (2026.07.04)** — สร้าง SSOT จากบทความ Creative Director (5 บทเรียน Pitch) + deep-research verified. Write-Clean Card pattern (framework อยู่ที่เดียว, 4 homes ชี้มา ไม่ fork). host ที่ b2b-why-thinking (belief center of gravity).
