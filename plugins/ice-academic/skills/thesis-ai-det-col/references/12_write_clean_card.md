# 12 — WRITE-CLEAN CARD (L1) — เขียนสะอาดตั้งแต่แรก ⭐ V01R01

> **ใช้เมื่อไหร่:** ตอน **เขียน prose** (ไม่ใช่ตอน detect). การ์ดนี้คือ "สารสกัด top AI-tells" ที่ทุก agent ฝัง/อ้างได้ — เพื่อ**เลี่ยง AI-cadence ตั้งแต่ pass แรก** ไม่ต้องวน detect→fix ทีหลัง (ประหยัด token).
>
> **นี่ไม่ใช่ detector** — detector เต็มอยู่ที่ Mode 1 (`01`/`06`/`11`). การ์ดนี้คือ checklist สั้นสำหรับ "ผู้เขียน". เมื่อต้องตรวจจริงจัง/customer-facing → qa-master D5 โหลด skill เต็ม.
>
> **Source of truth = skill นี้** (CORE + 3 branch). การ์ดนี้สกัดมา — ถ้าขัดกัน ยึด `06`/`11` เป็นหลัก.

---

## ส่วน A — 🟦 CORE (ทุก register · ทุก agent · ทุกภาษา)

**A1 — EN AI-vocab ห้ามใช้ (แทนด้วยคำธรรมดา):**
delve→examine · leverage→use · utilize→use · robust→strong/reliable · seamless→smooth · comprehensive→thorough · pivotal→key · foster→support · navigate→manage · showcase→show · underscore→emphasize · streamline→simplify · cutting-edge→advanced · holistic→overall · tapestry/symphony→mix · testament→proof · realm/landscape→area/field

**A2 — EN cadence ห้ามทำ (โครงประโยค):**
- ห้ามขึ้น section ด้วย meta-frame ซ้ำ "The following table/recommendations..." → ขึ้นเนื้อเลย
- ห้ามปิดย่อหน้าด้วย "This demonstrates/builds/underscores [abstract noun]" → ปิดด้วย fact/owner/number
- ห้าม "not just X but Y" ซ้ำ >1 ครั้ง
- ห้าม tri-stack buzzword ("ensures zero-risk migration through comprehensive testing")

**A3 — TH cadence ห้ามทำ:**
- ห้าม triadic-benefit ลอย "ทันสมัย คล่องตัว เพิ่มประสิทธิภาพ" (3 ท่อน generic ไร้ตัวเลข) → ยุบเหลือ benefit วัดได้ 1
- ห้าม superlative-stack 3 ชั้น "ระดับโลก + ผู้นำ + ต่อเนื่องหลายปี" → เหลือ 1-2 + ใส่ปีจริง
- ห้าม translationese: "เป็นที่น่าสังเกตว่า / มีบทบาทสำคัญอย่างยิ่ง / ในโลกปัจจุบันที่ / ไม่เพียงแต่...แต่ยัง"

**A4 — Human-voice ต้องทำ (เขียนให้ไม่ใช่ AI):**
- **Burstiness** — สลับประโยคสั้น (8-12 คำ) กับยาว (25-35) · ห้ามทุกประโยคยาวเท่ากัน
- **Vary opening** — ห้ามขึ้นประโยคโครงเดียวกันซ้ำใน 5 ประโยค
- **Specificity** — ทุก claim ผูก fact/number/mechanism · ถ้าไม่มี = ตัด (ห้ามกุ — H3)

**A5 — Wording (W1-W5):** positive-default · technical อธิบายเชิงผู้ใช้ · ไม่ลิเก · คำย่อนิยามก่อน · ไม่ emoji/CTA/clickbait

---

## ส่วน B — register-specific (เลือกตามงานที่เขียน)

### 🟩 B-Academic (ดุษฎีนิพนธ์/บทความ/วิจัย)
- **Class A zero-tolerance** (เจอครั้งเดียวแก้): ยิ่งไปกว่านั้น · ในท้ายที่สุด · ทั้งหมดนี้สังเคราะห์ได้ว่า · อย่างก้าวกระโดด · พลิกโฉม(ใน body) · เป็นที่ทราบกันดีว่า · ปฏิเสธไม่ได้ว่า
- ห้ามเปิดย่อหน้าสรุปด้วยสูตรสังเคราะห์ · acronym นิยามครั้งเดียว · กริยารายงานตรงชนิดแหล่ง (งานทัศนะห้าม "พบว่า/พิสูจน์ว่า")
- 🟢 ใช้ได้ (อย่าตัดผิด): นอกจากนี้ · อย่างมีประสิทธิภาพ · บูรณาการ · ขับเคลื่อน · ยกระดับ (คำที่นักวิจัยไทยใช้จริง density ≤3/500)

### 🟧 B-Business (proposal/SoW/solution/manday)
- **ห้ามเด็ดขาด** (0 hits ใน corpus iCE จริง): zero-risk · best-in-class · world-class · "Transformation"(งาน technical upgrade) · ✓-emoji checklist
- **Anchor rule** — คำหรูทุกคำแลกเป็น fact/capability/man-day/module จริง มิฉะนั้นตัด (สไตล์ fit% / man-day / module ของ iCE)
- ห้าม feature-dump ใน Exec Summary (ย้าย list เทคนิคลงล่าง · Exec เหลือ 1 ประโยค value)
- 🟢 register iCE ใช้ได้ (อย่าตัดผิด): Leading Practice · Scalability · ตอบโจทย์ · รองรับ · comprehensive+noun เฉพาะ · ชื่อ module จริง (GL/AP/AR) · Single Point of Contact · 90-day validity
- **คง Lexical Fingerprint** — ห้าม normalize คำที่ quote จากต้นทาง
- **B6 Term-Localization (ก่อนแปลศัพท์ technical/product เป็นไทย ตัดสินด้วย TL-A/B/C):**
  - **TL-A คงไทย** — ศัพท์วิชาชีพไทยมาตรฐาน (กระทบยอด, บัญชีแยกประเภท, ค่าเสื่อม ฯลฯ) → คงไทย
  - **TL-B คงอังกฤษ** — เมื่อคำไทย misname product feature จริง → คง EN (เช่น FAH ไม่ใช่ "เครื่องบันทึกบัญชี" ที่สื่อเหมือนเครื่องคีย์ข้อมูล)
  - **TL-C ไทย (EN) ครั้งแรก** — มีศัพท์ไทยใช้ได้แต่ผูก EN ตอนแรก
  - **ห้ามแตะ** 4 fit-labels (Configure/Customization/Integration/Workaround = bilingual by design)
  - **product-feature-misname guard:** verify ชื่อ feature จาก source ก่อนเสมอ — ห้ามเดา · ห้าม overclaim category (RNA = measurement engine ไม่ใช่ "actuarial")
  - *prevention extract ของ §6.6 — detection เต็ม = skill §6.6 B-Check 7/11. TL-A = §6.6 well-known-Thai guard (กระทบยอด) · TL-B misname = มิติใหม่ MG1 (gated) · ทิศตรงข้าม §6.5 (calque) ยังคงอยู่*

### 🟪 B-General (email/บทความทั่วไป/บันทึก)
- เสียงที่ปรึกษา-สอน ชัดเจน ตรงประเด็น · ไม่ลิเก ไม่บรรยายเกิน
- watchlist สากล (A1-A3) พอ · ไม่ต้อง Class A academic / Anchor business เต็มรูป
- positive-default · ผูก fact เมื่ออ้างตัวเลข

---

## ส่วน C — GUARD (กัน over-correction)

- **ห้าม blanket-ban** คำที่อยู่ใน corpus จริง (ดู 🟢 ในแต่ละ branch) — AI-tell = **cadence/density** ไม่ใช่ vocabulary เดี่ยว
- คำที่ "ดูหรู" แต่จำเป็น (register/procurement/domain term) = เก็บไว้
- สงสัยคำใหม่ → flag เป็น Field-Discovered (`06` §1.5) ไม่ใช่ตัดทันที

---

## วิธีใช้ (สำหรับ agent)

1. **ตอนเขียน** — สแกนใจ A1-A5 (core) + B-[register] ของงานที่ทำ → เลี่ยงตั้งแต่ร่างแรก
2. **ไม่แน่ใจว่าหลุดไหม** — ถ้าเป็น customer-facing/ส่งจริง → ส่ง qa-master D5 (โหลด skill เต็ม detect)
3. **การ์ดนี้ = prevention · skill เต็ม = detection/correction** — คนละชั้น เสริมกัน

---

## CHANGELOG
- **V01R02 (2026.06.24)** — +B6 Term-Localization ใต้ B-Business (TL-A keep-Thai / TL-B keep-EN-on-misname / TL-C Thai(EN)-first + product-feature-misname guard + verify-from-source) — prevention extract ของ §6.6/§6.6.1; เคส VFIN. example-light (push enumerated product list ไป Compass brief). cross-ref ชี้ skill เป็น source of truth (anti-drift).
- **V01R01 (2026.06.13)** — สกัดครั้งแรกจาก CORE + 3 branch (V05R01). A=core (EN vocab/cadence + TH cadence + human-voice + wording) · B=register-specific (academic Class A / business anchor+ห้าม zero-risk / general) · C=guard. ออกแบบเป็น L1 ให้ทุก agent ฝัง/อ้าง — "เขียนสะอาดตั้งแต่แรก" แทน detect-fix loop.
