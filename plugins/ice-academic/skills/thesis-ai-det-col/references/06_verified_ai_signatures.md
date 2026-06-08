# Verified AI Signatures — Real Thai Academic Corpus + Wikipedia Patterns

## When to Read This

อ่านเมื่อทำ Layer 1 (Vocabulary Footprints Check) ของ Mode 1 หรือ Pass 2 Step 1 ของ Mode 3 — ต้องการรายการคำที่ verified ว่าเป็น AI signature จริง

**Sources of Truth:**
1. การวิเคราะห์ corpus 101 ไฟล์งานวิจัยไทย (~292,000 คำ) ใน `voice_profiles/KM-TH-THESIS-DOC_V02R01.md`
2. [Wikipedia:Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) — รายละเอียด 24 patterns ใน `07_wikipedia_24_patterns.md`

---

## 1. 🔴 Confirmed AI Signatures (ปรากฏ ≤ 5 ครั้งใน 292K คำ) — CLASS A

**คำเหล่านี้คือ AI signature จริง — Pass 2 ต้องลบออก:**

**การวัด (V03):** Section 1 + 1.5 + 1.6 = **Class A — Zero-Tolerance**: ตรวจแบบ per-instance พบ ≥ 1 ครั้ง = Fail Check 1b ทันที พร้อมบันทึกตำแหน่ง **ห้ามใช้เกณฑ์ density กับ Class A** — เกณฑ์ density (Section 5) ใช้กับ Class B (Section 2 🟡 + Section 4 English) เท่านั้น

| คำ | จำนวนครั้งใน 292K | คำแทนที่ |
|---|---|---|
| เป็นที่ทราบกันดีว่า | 0 | ลบทิ้ง / ระบุข้อเท็จจริงโดยตรง |
| นับเป็นสิ่งสำคัญ | 0 | ลบทิ้ง / ระบุประเด็น |
| ในแง่หนึ่ง | 0 | ระบุแง่ไหน |
| อาจถือได้ว่า | 0 | "ถือว่า" |
| ดังที่กล่าวไว้ข้างต้น | 0 | "ดังนั้น" / ลบ |
| อย่างพิถีพิถัน | 0 | "อย่างละเอียด" |
| ยิ่งไปกว่านั้น | 1 | "นอกจากนั้น" / ลบ |
| อาจกล่าวได้ว่า | 1 | ลบ / ระบุโดยตรง |
| ในเวลาเดียวกัน | 1 | "ในขณะเดียวกัน" |
| ในท้ายที่สุด | 1 | "ท้ายที่สุด" |
| กล่าวโดยสรุป | 2 | "สรุปว่า" |
| ปฏิเสธไม่ได้ว่า | 3 | ลบ |

---

## 1.5 Field-Discovered Signatures (Living List) ⭐ V03

Corpus 292K แช่แข็ง ณ V05R01 — pattern ใหม่ที่หลุดรอดจากงานจริงให้ลงทะเบียนที่นี่ **ถือเป็น Class A ทันที** เมื่อพบซ้ำใน ≥ 2 เอกสารอิสระจึงเลื่อนขึ้น Section 1 ถาวร

| คำ/สูตร | พบเมื่อ | บริบทที่พบ | สถานะ | คำแทนที่ |
|---|---|---|---|---|
| ทั้งหมดนี้สังเคราะห์ได้ว่า | 2026-06 | เปิดย่อหน้าสรุปบทความวิชาการ (~3 จุดในงานเดียว — บทความจริงในชุดอ้างอิงของผู้ใช้แทบไม่ใช้) | Class A | "สรุปว่า" / เปิดย่อหน้าด้วยข้อค้นพบตรง |
| สามารถสังเคราะห์ได้ว่า | 2026-06 | เดียวกัน | Class A | เดียวกัน |

**ขั้นตอนเพิ่มรายการ:** (1) ระบุ pattern + ตำแหน่งที่พบ (2) เทียบกับ corpus อ้างอิงถ้าเข้าถึงได้ (3) ลงตารางพร้อมวันที่/บริบท (4) พบซ้ำในเอกสารอิสระที่ 2 → เลื่อนขึ้น Section 1

## 1.6 Promotional Intensifiers & Artifacts — CLASS A (Zero-Tolerance) ⭐ V03

คำเร่งน้ำหนักเชิงโปรโมต **ครั้งเดียวก็ส่งกลิ่น** — บทเรียนจริง: "อย่างก้าวกระโดด" โผล่ครั้งเดียวจึงผ่านเกณฑ์ density แต่ reviewer จับได้ทันที ห้ามประเมินกลุ่มนี้แบบ density

| คำ | คำแทนที่ |
|---|---|
| อย่างก้าวกระโดด | ระบุขนาดจริง: "เพิ่มขึ้น 3 เท่าภายใน 2 ปี" |
| พลิกโฉม | ระบุสิ่งที่เปลี่ยนจริง |
| ปฏิวัติวงการ | ระบุการเปลี่ยนแปลงเฉพาะ |
| อย่างที่ไม่เคยมีมาก่อน / อย่างที่ไม่เคยปรากฏมาก่อน | ตัด / เทียบกับฐานปีจริง |
| อย่างมหาศาล | ระบุขนาด/ตัวเลขจริง |
| ก้าวสำคัญสู่อนาคต / เปิดศักราชใหม่ | ตัด (ดู `07` Pattern 24) |
| งดงามตระการตา / เลื่องชื่อ / ตั้งอยู่ใจกลาง | ตัด (ดู `07` Pattern 4) |

Chatbot artifacts และ sycophantic tone (`09_filler_replacement_table.md` Sections 5-7) ถือเป็น Class A ด้วย

---

## 2. 🟡 Moderate Use (5–30 ครั้ง — ใช้ได้แต่ระวัง density) — CLASS B

| คำ | จำนวนครั้ง | บริบทที่ใช้ |
|---|---|---|
| อย่างลึกซึ้ง | 7 | บทอภิปราย Profile A |
| อย่างเป็นรูปธรรม | 10 | นโยบาย Profile A/B |
| ในยุคที่ | 16 | บทนำ Profile B/C |
| ในขณะเดียวกัน | 16 | คำเชื่อม |
| ในยุคปัจจุบัน | 24 | บทนำ Profile B/C |
| โดยสรุป | 17 | สรุป |

---

## 3. 🟢 Common in Real Thai (> 30 ครั้ง — ใช้ได้)

**สำคัญ:** คำเหล่านี้ที่ AI Detector ภาษาอังกฤษมักจัดเป็น AI signature **ไม่ใช่ AI signature ในภาษาไทย** เพราะนักวิจัยไทยจริงใช้แพร่หลาย

| คำ | จำนวนครั้ง | จำนวนไฟล์ | Verdict |
|---|---|---|---|
| ขับเคลื่อน | 272 | 62 | ✅ ใช้แพร่หลาย |
| ยกระดับ | 133 | 43 | ✅ ใช้ได้ |
| อย่างยั่งยืน | 68 | 32 | ✅ ใช้ได้ (ระบุระยะเวลาเฉพาะดีกว่า) |
| อย่างมีประสิทธิภาพ | 195 | 55 | ✅ ใช้แพร่หลาย |
| อย่างเป็นระบบ | 59 | 33 | ✅ ใช้ได้ |
| หลากหลาย | 179 | 55 | ✅ ใช้ได้ |
| อย่างต่อเนื่อง | 148 | — | ✅ ใช้แพร่หลาย |
| อย่างมีนัยสำคัญ | 119 | 36 | ✅ ใช้ — โดยเฉพาะ Profile C ที่มีสถิติ |
| อย่างชัดเจน | 35 | 25 | ✅ ใช้ |
| อย่างเหมาะสม | 53 | — | ✅ ใช้ |
| บูรณาการ | 432 | 59 | ✅ ใช้แพร่หลายมาก |
| นอกจากนี้ | 156 | 69 | ✅ ใช้ได้ (≤ 3 ครั้ง/500 คำ) |
| อย่างไรก็ตาม | 56 | 26 | ✅ ใช้ได้ |
| ดังนั้น | 239 | 82 | ✅ ใช้แพร่หลายมาก |
| เนื่องจาก | 290 | 79 | ✅ ใช้แพร่หลายมาก |
| ทั้งนี้ | 122 | 60 | ✅ ใช้แพร่หลาย |
| ในศตวรรษที่ | 41 | — | ✅ ใช้ใน Profile B/C (บทนำ) |

---

## 4. English Tier 1 Vocabulary (สำหรับ Pass 2 Step 1.1-1.4)

ในส่วนที่เป็นภาษาอังกฤษของเอกสาร bilingual:

### 4.1 Verbs

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

### 4.2 Adjectives

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

### 4.3 Nouns

| AI ใช้ | คำแทนที่ |
|---|---|
| landscape | field / area |
| realm | area / domain |
| tapestry | mix / combination |
| symphony | combination |
| testament | proof / evidence |
| synergy | cooperation |
| paradigm | model / framework |

### 4.4 Phrases

| AI ใช้ | วลีแทนที่ |
|---|---|
| "It's important to note that..." | ตัดทิ้ง |
| "In today's fast-paced world..." | ระบุปี / ตัดทิ้ง |
| "In the realm of..." | "In [field]..." |
| "Delving into the intricacies of..." | "Examining..." |
| "A testament to..." | "Proves..." |
| "Embark on a journey..." | "Begin..." |
| "Plays a crucial role in..." | "Drives..." |

---

## 5. Pass 2 Density Targets (ใช้กับ Class B เท่านั้น — Class A วัดแบบ per-instance)

| ระดับเอกสาร | จำนวน Tier 1 ที่ยอมรับ |
|---|---|
| งานวิชาการระดับวารสารนานาชาติ | ≤ 2 ครั้ง / 1,000 คำ |
| งานวิชาการระดับวารสารไทย (TCI) | ≤ 4 ครั้ง / 1,000 คำ |
| Business proposal / Executive | ≤ 3 ครั้ง / 1,000 คำ |
| งานราชการ | ≤ 2 ครั้ง / 1,000 คำ |
| Marketing content | ≤ 5 ครั้ง / 1,000 คำ |

---

## 6. Lesson Learned

> **Updated Understanding (V05R01):** คำว่า "ขับเคลื่อน" และ "ยกระดับ" ที่ AI Detector ภาษาอังกฤษมักจัดเป็น AI signature (drive, elevate) **ไม่ใช่ AI signature ในภาษาไทย** เพราะนักวิจัยไทยจริง ๆ ใช้แพร่หลาย — "ขับเคลื่อน" ปรากฏ 272 ครั้งใน 62 ไฟล์, "ยกระดับ" 133 ครั้งใน 43 ไฟล์
>
> **AI signature จริงในภาษาไทยวิชาการ** คือคำในตาราง Section 1 ข้างต้น

---

## 7. Cross-Reference: Wikipedia 24-Pattern Mapping

สำหรับ patterns ที่ Wikipedia ครอบคลุมแต่ไม่อยู่ในตารางเฉพาะภาษาไทยข้างต้น ให้อ่าน `07_wikipedia_24_patterns.md`:

| Wikipedia Pattern # | ครอบคลุมใน file นี้แล้ว? |
|---|---|
| 1. Inflated symbolism | ❌ ดู `07_wikipedia_24_patterns.md` Section "Pattern 1" |
| 2. Notability name-dropping | ❌ ดู `07_*` Section "Pattern 2" |
| 3. Superficial -ing analyses | ❌ ดู `07_*` Section "Pattern 3" |
| 4. Promotional language | ❌ ดู `07_*` Section "Pattern 4" |
| 5. Vague attributions | ✅ บางส่วนใน Section 1-2 ของ file นี้ |
| 6. Formulaic Challenges | ❌ ดู `07_*` Section "Pattern 6" |
| 7. AI vocabulary | ✅ ครบใน Section 1-3 |
| 8. Copula avoidance | ❌ ดู `07_*` Section "Pattern 8" |
| 9. Negative parallelisms | ❌ ดู `07_*` Section "Pattern 9" |
| 10. Rule of three | ✅ ใน `01_three_layer_detection.md` Layer 2 Check 5 |
| 11. Synonym cycling | ❌ ดู `07_*` Section "Pattern 11" |
| 12. False ranges | ❌ ดู `07_*` Section "Pattern 12" |
| 13. Em dash overuse | ✅ ใน `02_two_pass_protocol.md` Advanced C |
| 14. Boldface overuse | ❌ ดู `07_*` Section "Pattern 14" |
| 15. Inline-header lists | ❌ ดู `07_*` Section "Pattern 15" |
| 16. Title Case headings | ❌ ดู `07_*` Section "Pattern 16" |
| 17. Emoji decoration | ❌ ดู `07_*` Section "Pattern 17" |
| 18. Curly quotes | ❌ ดู `07_*` Section "Pattern 18" |
| 19. Chatbot artifacts | ❌ ดู `07_*` Section "Pattern 19" + `09_filler_replacement_table.md` Section 7 |
| 20. Knowledge-cutoff disclaimers | ❌ ดู `09_filler_replacement_table.md` Section 6 |
| 21. Sycophantic tone | ❌ ดู `09_filler_replacement_table.md` Section 5 |
| 22. Filler phrases | ❌ ดู `09_filler_replacement_table.md` Sections 1-2 |
| 23. Excessive hedging | ✅ บางส่วนใน Section 1; เพิ่มใน `09_*` Section 3 |
| 24. Generic conclusions | ❌ ดู `09_filler_replacement_table.md` Section 4 |

**Translation:** เมื่อข้อความเป็นภาษาอังกฤษหรือ Bilingual, ใช้ `07_wikipedia_24_patterns.md` คู่กันกับ file นี้
