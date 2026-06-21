# Use Case Playbook — 8 Scenarios

แต่ละ Use Case ระบุ: Audience, Tool, Style, Aspect Ratio, imageSize, Prompt Pattern, Output Naming, Pairing Skill

> **Engine:** rlabs/gemini-mcp (server name `gemini`) · default image model = Nano Banana Pro (`gemini-3-pro-image-preview`)
> ภาพถูก save อัตโนมัติลง `GEMINI_OUTPUT_DIR` (`~/.local/share/gemini-mcp-images`) — ไม่มี `output_path` param. การตั้งชื่อตาม Convention ด้านล่างทำหลัง generate (move/rename ไฟล์จาก output dir ไปยัง path ปลายทางของงาน)
> **ไม่มี `model_tier` (nb2/pro/flash)** อีกต่อไป — ใช้ `imageSize` (`1K` / `2K` default / `4K`) คุมคุณภาพ/ต้นทุนแทน

---

## Category A: B2B / Pre-sales (3 Use Cases)

### UC-01: Hero Image สำหรับ Slide Proposal

**Audience:** Executive / Decision Maker
**Use:** Section Cover, Chapter Opener ใน Proposal Deck

**Specs:**
- Tool: `gemini-generate-image`
- Style: `photorealistic` (param `style`)
- Aspect Ratio: `16:9`
- imageSize: `4K`
- Prompt Pattern: B-01 (Slide Hero) + Industry variant B-04
- Output Target: `/path/to/proposal/slides/section-N_hero_V##R##.png`
- Pairing: + `b2b-presentation-creator` (ส่ง Image Spec ต่อ)

**Workflow:**
1. ระบุ Section Topic (e.g., "Digital Transformation Roadmap")
2. ระบุ Industry Context (e.g., Public Sector, Financial Services)
3. เลือก Industry palette จาก B-04
4. Compose Prompt ตาม B-01 + Industry variant
5. เรียก `gemini-generate-image(prompt=..., style="photorealistic", aspectRatio="16:9", imageSize="4K")`
6. ย้าย/เปลี่ยนชื่อไฟล์จาก output dir ไป Output Target แล้วส่ง Path ให้ slide builder

**ตัวอย่าง Call:**
```
gemini-generate-image(
  prompt="Wide cinematic establishing shot of a modern enterprise data center, abstract digital transformation theme, clean negative space on the left for headline overlay, deep blue and teal palette, soft volumetric lighting",
  style="photorealistic",
  aspectRatio="16:9",
  imageSize="4K"
)
```

---

### UC-02: Product Shot สำหรับ Catalog / Spec Sheet

**Audience:** Customer / End User
**Use:** Product Page, Spec Sheet, Brochure

**Specs:**
- Tool: `gemini-generate-image`
- Style: `photorealistic`
- Aspect Ratio: `1:1` (Square Catalog) หรือ `3:4` (Vertical Spec Sheet)
- imageSize: `4K` (High-fidelity Print)
- Prompt Pattern: P-02 (White BG) หรือ P-03 (Lifestyle)
- Output Target: `/path/to/products/[sku]_[angle]_V##R##.png`
- Pairing: + `b2b-presentation-creator`, + `oracle-netsuite-consulting` (ดึง SKU Info)

**Workflow:**
1. ขอ Product Description (Material, Color, Finish, Dimension)
2. ขอ Context (White BG / Lifestyle / In-use)
3. เลือก Aspect ตาม Layout ปลายทาง
4. Generate ภาพหลัก + 2-3 angles (เรียก `gemini-generate-image` ซ้ำ — rlabs ไม่มี `n` batch param จึง generate ทีละภาพ ปรับ prompt ระบุมุมกล้องในแต่ละครั้ง)
5. ใช้ `gemini-analyze-image(imagePath=...)` ตรวจว่า material/color ตรง brief ก่อนส่ง
6. ย้ายไฟล์และ Save ด้วย Naming Convention `[sku]_[angle]_V##R##`

---

### UC-03: Concept Mockup สำหรับ Customer Workshop

**Audience:** Workshop Participants / Stakeholders
**Use:** Design Sprint, Strategy Workshop, Ideation Session

**Specs:**
- Tool: `gemini-generate-image`
- Style: `concept art` หรือ `sketch` (param `style`)
- Aspect Ratio: `4:3` หรือ `16:9`
- imageSize: `2K` (ไม่จำเป็นต้อง 4K สำหรับ Mood Reference — ประหยัดต้นทุน)
- Prompt Pattern: D-06 (Concept Sketch) หรือ B-02 (Workshop Mockup)
- Output Target: `/path/to/workshop/[date]/concept_[N]_V##R##.png`
- Pairing: + `b2b-design-thinking`

**Workflow:**
1. ระบุ Workshop Topic + Key Concept
2. Generate 3-5 ภาพในสไตล์เดียวกันแต่ Concept ต่างกัน (คง `style` + `imageSize` เดิม เปลี่ยนเฉพาะเนื้อ prompt เพื่อให้ดูเป็นชุดเดียวกัน)
3. ใช้เป็น Stimulus สำหรับ Ideation
4. หลัง Workshop เก็บใน Workshop Archive

---

## Category B: Marketing (3 Use Cases)

### UC-04: Social Media Asset (FB / IG / LinkedIn / X)

**Audience:** Public, Followers
**Use:** Daily Post, Campaign, Announcement

**Specs:**
| Platform | aspectRatio | imageSize |
|---|---|---|
| Instagram Feed | `1:1` | `2K` |
| Instagram Story/Reel | `9:16` | `2K` |
| Facebook Post | `1:1` หรือ `16:9` | `2K` |
| LinkedIn Post | `16:9` (ใกล้ 1.91:1) | `2K` |
| X/Twitter | `16:9` | `2K` |
| YouTube Thumbnail | `16:9` | `2K` |

- Tool: `gemini-generate-image`
- Style: เลือกตาม brand (เช่น `photorealistic`, `flat illustration`, `3d render`)
- Prompt Pattern: M-02, M-03, M-04 ตาม Platform
- Output Target: `/path/to/social/[campaign]/[platform]_[date]_V##R##.png`
- Pairing: + `marketing:content-creation` (Caption + Hashtag)

**Workflow:**
1. ระบุ Campaign + Key Message
2. ระบุ Platform (อาจหลาย Platform = หลาย `aspectRatio`)
3. ระบุ Brand Voice/Tone → map ไปที่ param `style`
4. Generate ตาม `aspectRatio` ของแต่ละ Platform (เรียกซ้ำต่อ Platform)
5. ส่งต่อให้ Content writer ใส่ Caption

> **Tip:** ถ้าเนื้อหาอิงเหตุการณ์/เทรนด์ปัจจุบัน (เช่น campaign ตามกระแส) เปิด `useGoogleSearch=true` เพื่อ ground ภาพให้สอดคล้องบริบทจริง

---

### UC-05: Campaign Banner / Website Hero

**Audience:** Website Visitor, Campaign Target
**Use:** Landing Page Hero, Email Header, Web Banner

**Specs:**
- Tool: `gemini-generate-image`
- Style: `photorealistic` หรือ `cinematic`
- Aspect Ratio: `21:9` (Cinematic Hero) หรือ `16:9` (Standard)
- imageSize: `4K`
- Prompt Pattern: M-01 (Hero Banner)
- Output Target: `/path/to/web/[page]/hero_V##R##.png`
- Pairing: + `brand-guidelines`

**Workflow:**
1. ระบุ Page Topic + Conversion Goal
2. ระบุ Brand Color Palette (จาก brand-guidelines) — ใส่เป็นคำอธิบายสีใน prompt
3. ระบุ Headline ที่จะ Overlay → สั่งให้ Composition เว้น negative space ใน prompt
4. `gemini-generate-image(prompt=..., style="cinematic", aspectRatio="21:9", imageSize="4K")`
5. ส่ง Designer ใส่ Headline

---

### UC-06: Brand-aligned Illustration Series

**Audience:** Brand-aware Users
**Use:** Blog Post, Newsletter, Internal Comm

**Specs:**
- Tool: `gemini-generate-image`
- Style: ระบุ style เดียวคงที่ตลอดชุด (เช่น `flat illustration`, `watercolor`)
- Aspect Ratio: `16:9` (Article Header) หรือ `1:1` (Inline)
- imageSize: `2K`
- Prompt Pattern: D-08 (Infographic) + Brand Style Constraint
- Output Target: `/path/to/blog/[topic]/illust_[N]_V##R##.png`
- Pairing: + `brand-guidelines`, + Internal Comms Skills

**Workflow:**
1. ขอ Brand Style Guide (Color, Style Keyword, Mood)
2. Compose Series Prompt with Consistent Style (ล็อค param `style` เดียวกันทุกภาพ)
3. Generate 5-10 ภาพในสไตล์เดียว
4. QA: ใช้ `gemini-analyze-image` เทียบทุกภาพให้ดู "เป็นพี่น้องกัน" — ถ้าภาพไหนหลุดสไตล์ regenerate เฉพาะภาพนั้น

---

## Category C: Internal / Productivity (2 Use Cases)

### UC-07: Mood Board / Reference Library

**Audience:** Internal Designer / Workshop Facilitator
**Use:** Pre-design Inspiration, Style Reference

**Specs:**
- Tool: `gemini-generate-image`
- Style: หลากหลาย (ทดลองหลาย style ได้)
- Aspect Ratio: หลากหลาย (เลือกตามภาพต้นแบบ)
- imageSize: `1K` หรือ `2K` (Volume work — ใช้ `1K` เพื่อประหยัดต้นทุนที่สุด)
- Prompt Pattern: B-06 (Mood Board Item)
- Output Target: `/path/to/moodboard/[project]/[mood]_[N]_V##R##.png`
- Pairing: + `b2b-design-thinking`

**Workflow:**
1. ระบุ Project + Mood Keywords (3-5 คำ)
2. Generate 10-20 ภาพในมู้ดต่างๆ ที่ `imageSize="1K"`
3. Save เป็น Collection
4. ใช้เป็น Reference ไม่ใช่ Final

---

### UC-08: Iterative Edit Loop (Session-based)

**Audience:** Designer / Marketer ผู้ Refine ภาพหลายรอบ
**Use:** Refine ภาพหลายรอบ (Background, Style, Element) ภายใน session เดียว

**Specs:**
- Tools: `gemini-start-image-edit` → `gemini-continue-image-edit` → `gemini-end-image-edit`
- Aspect Ratio / imageSize: ตั้งครั้งเดียวที่ `gemini-start-image-edit` (สืบทอดทั้ง session)
- Prompt Pattern: Iterative Edit + ระบุ Preserve/Change ชัดในแต่ละ turn
- Output Target: `/path/to/edits/[base]_v1.png`, `_v2.png`, `_v3.png`
- Naming: เพิ่ม `_v[N]` ทุกครั้งที่แก้

**Workflow (session-based — ต่างจาก one-shot edit เดิม):**
1. เริ่ม session: `gemini-start-image-edit(prompt="<ภาพ base ที่ต้องการ>", aspectRatio=..., imageSize=...)` → ได้ภาพ base + `sessionId`
2. แก้ทีละรอบในระบบเดียวกัน: `gemini-continue-image-edit(sessionId=..., prompt="make the background warmer")` — เรียกซ้ำได้ Gemini จำ context ภาพก่อนหน้าใน session
3. (ถ้าไม่แน่ใจผล) `gemini-analyze-image(imagePath=<ภาพล่าสุด>, query="does the lighting look warm and natural?")` ให้ Claude ดูภาพแล้วสั่งแก้ต่อได้แม่นขึ้น
4. เมื่อพอใจ: `gemini-end-image-edit(sessionId=...)` ปิด session
5. ถ้าลืม sessionId ที่เปิดค้าง: `gemini-list-image-sessions()` ดู session ทั้งหมดที่ยัง active

**Iteration Tips:**
- รอบ 1: เปลี่ยน Major (Background, Subject)
- รอบ 2: เปลี่ยน Color/Style
- รอบ 3+: Fine-tune Detail
- ห้ามแก้ทุกอย่างพร้อมกัน — รอบละ Change (session จะจำผลสะสมให้)
- อย่าลืม `gemini-end-image-edit` เพื่อไม่ให้ session ค้าง

---

## Output Naming Convention

ใช้ Convention นี้ทุก Use Case เพื่อให้หา/Track ง่าย (rename หลัง generate จาก `GEMINI_OUTPUT_DIR`):

```
[purpose]_[descriptor]_V##R##_YYYY.MM.DD.[ext]
```

ตัวอย่าง:
- `hero_oracle-erp-section1_V01R01_2026.05.25.png`
- `logo_abc-consulting_V01R03_2026.05.25.png`
- `product_sku12345_white-bg_V01R01_2026.05.25.png`
- `social_instagram-feed_campaign-q3_V02R01_2026.05.25.png`
- `mockup_dashboard-laptop_V01R01_2026.05.25.png`

**Version Rules:**
- R: Minor Edit (e.g., V01R01 → V01R02)
- V: Major Rewrite (e.g., V01R03 → V02R01)
- เก็บ V01R01 ไว้ตลอด เผื่อย้อนกลับ

---

## Quick Decision Matrix

| ผู้ใช้บอก | Use Case | Tool | style | aspectRatio | imageSize |
|---|---|---|---|---|---|
| "Slide hero" | UC-01 | gemini-generate-image | photorealistic | 16:9 | 4K |
| "Product photo" | UC-02 | gemini-generate-image | photorealistic | 1:1 or 3:4 | 4K |
| "Workshop concept" | UC-03 | gemini-generate-image | concept art | 4:3 or 16:9 | 2K |
| "Instagram post" | UC-04 | gemini-generate-image | brand-dependent | 1:1 | 2K |
| "Web hero banner" | UC-05 | gemini-generate-image | cinematic | 21:9 or 16:9 | 4K |
| "Blog illustration" | UC-06 | gemini-generate-image | flat illustration | 16:9 | 2K |
| "Mood board" | UC-07 | gemini-generate-image | varies | varies | 1K |
| "แก้ภาพเดิม" | UC-08 | gemini-start/continue/end-image-edit | (set at start) | match base | match base |
| "ดูภาพนี้ให้หน่อย / วิเคราะห์ภาพ" | (any) | gemini-analyze-image | — | — | — |

---

## Migration Note (V03R01 · 2026-06-21)

Playbook นี้ย้ายจาก nanobanana MCP มาใช้ **rlabs/gemini-mcp** (`@rlabs-inc/gemini-mcp` v0.8.1) ทั้งหมด. การเปลี่ยนแปลงหลักที่กระทบ Use Cases:

- **เลิกใช้ `model_tier`** (nb2/pro/flash) — คุมคุณภาพ/ต้นทุนผ่าน `imageSize` `1K`/`2K`/`4K` แทน. default ของ engine คือ Nano Banana Pro (`gemini-3-pro-image-preview`) เสมอ
- **Resolution syntax เปลี่ยน:** `4k`/`2k`/`1k` → `4K`/`2K`/`1K` (param ชื่อ `imageSize`, default = `2K`)
- **`style` เป็น param แยก** (ไม่ฝังใน prompt) — เช่น `"photorealistic"`, `"watercolor"`, `"anime"`
- **Edit เปลี่ยนเป็น session-based:** ไม่มี `mode=edit` / `input_image_path` one-shot — ใช้ `gemini-start-image-edit` → `gemini-continue-image-edit` (ซ้ำได้) → `gemini-end-image-edit` แทน (UC-08)
- **ไม่มี `output_path` / `n` (batch):** ภาพ save อัตโนมัติลง `GEMINI_OUTPUT_DIR` ทีละภาพ — generate หลายภาพต้องเรียกซ้ำ
- **Feature ใหม่:** `gemini-analyze-image` (Claude เห็น/วิเคราะห์ภาพได้ → ใช้ QA + iterate แม่นขึ้น), `gemini-generate-video` (Veo), `gemini-list-image-sessions`
