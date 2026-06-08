# Use Case Playbook — 8 Scenarios

แต่ละ Use Case ระบุ: Audience, Model, Aspect Ratio, Resolution, Prompt Pattern, Output Naming, Pairing Skill

---

## Category A: B2B / Pre-sales (3 Use Cases)

### UC-01: Hero Image สำหรับ Slide Proposal

**Audience:** Executive / Decision Maker
**Use:** Section Cover, Chapter Opener ใน Proposal Deck

**Specs:**
- Model: `nb2`
- Aspect Ratio: `16:9`
- Resolution: `4k`
- Prompt Pattern: B-01 (Slide Hero) + Industry variant B-04
- Output: `/path/to/proposal/slides/section-N_hero_V##R##.png`
- Pairing: + `b2b-presentation-creator` (ส่ง Image Spec ต่อ)

**Workflow:**
1. ระบุ Section Topic (e.g., "Digital Transformation Roadmap")
2. ระบุ Industry Context (e.g., Public Sector, Financial Services)
3. เลือก Industry palette จาก B-04
4. Compose Prompt ตาม B-01 + Industry variant
5. Generate + ส่ง Path ให้ slide builder

---

### UC-02: Product Shot สำหรับ Catalog / Spec Sheet

**Audience:** Customer / End User
**Use:** Product Page, Spec Sheet, Brochure

**Specs:**
- Model: `nb2` (`pro` ถ้า High-fidelity Print)
- Aspect Ratio: `1:1` (Square Catalog) หรือ `3:4` (Vertical Spec Sheet)
- Resolution: `4k`
- Prompt Pattern: P-02 (White BG) หรือ P-03 (Lifestyle)
- Output: `/path/to/products/[sku]_[angle]_V##R##.png`
- Pairing: + `b2b-presentation-creator`, + `oracle-netsuite-consulting` (ดึง SKU Info)

**Workflow:**
1. ขอ Product Description (Material, Color, Finish, Dimension)
2. ขอ Context (White BG / Lifestyle / In-use)
3. เลือก Aspect ตาม Layout ปลายทาง
4. Generate ภาพหลัก + 2-3 angles
5. Save ด้วย Naming Convention `[sku]_[angle]_V##R##`

---

### UC-03: Concept Mockup สำหรับ Customer Workshop

**Audience:** Workshop Participants / Stakeholders
**Use:** Design Sprint, Strategy Workshop, Ideation Session

**Specs:**
- Model: `flash` (เร็ว ทำหลายภาพ) หรือ `nb2` (Quality)
- Aspect Ratio: `4:3` หรือ `16:9`
- Resolution: `2k` (ไม่จำเป็นต้อง 4K สำหรับ Mood Reference)
- Prompt Pattern: D-06 (Concept Sketch) หรือ B-02 (Workshop Mockup)
- Output: `/path/to/workshop/[date]/concept_[N]_V##R##.png`
- Pairing: + `b2b-design-thinking`

**Workflow:**
1. ระบุ Workshop Topic + Key Concept
2. Generate 3-5 ภาพในสไตล์เดียวกันแต่ Concept ต่างกัน
3. ใช้เป็น Stimulus สำหรับ Ideation
4. หลัง Workshop เก็บใน Workshop Archive

---

## Category B: Marketing (3 Use Cases)

### UC-04: Social Media Asset (FB / IG / LinkedIn / X)

**Audience:** Public, Followers
**Use:** Daily Post, Campaign, Announcement

**Specs:**
| Platform | Aspect | Resolution |
|---|---|---|
| Instagram Feed | `1:1` | `2k` |
| Instagram Story/Reel | `9:16` | `2k` |
| Facebook Post | `1:1` หรือ `16:9` | `2k` |
| LinkedIn Post | `1.91:1` (close to `16:9`) | `2k` |
| X/Twitter | `16:9` | `2k` |
| YouTube Thumbnail | `16:9` | `2k` |

- Model: `nb2`
- Prompt Pattern: M-02, M-03, M-04 ตาม Platform
- Output: `/path/to/social/[campaign]/[platform]_[date]_V##R##.png`
- Pairing: + `marketing:content-creation` (Caption + Hashtag)

**Workflow:**
1. ระบุ Campaign + Key Message
2. ระบุ Platform (อาจหลาย Platform = หลาย Aspect)
3. ระบุ Brand Voice/Tone
4. Generate ตาม Aspect ของแต่ละ Platform
5. ส่งต่อให้ Content writer ใส่ Caption

---

### UC-05: Campaign Banner / Website Hero

**Audience:** Website Visitor, Campaign Target
**Use:** Landing Page Hero, Email Header, Web Banner

**Specs:**
- Model: `nb2`
- Aspect Ratio: `21:9` (Cinematic Hero) หรือ `16:9` (Standard)
- Resolution: `4k`
- Prompt Pattern: M-01 (Hero Banner)
- Output: `/path/to/web/[page]/hero_V##R##.png`
- Pairing: + `brand-guidelines`

**Workflow:**
1. ระบุ Page Topic + Conversion Goal
2. ระบุ Brand Color Palette (จาก brand-guidelines)
3. ระบุ Headline ที่จะ Overlay (เพื่อให้ Composition มี Space)
4. Generate + ส่ง Designer ใส่ Headline

---

### UC-06: Brand-aligned Illustration Series

**Audience:** Brand-aware Users
**Use:** Blog Post, Newsletter, Internal Comm

**Specs:**
- Model: `nb2`
- Aspect Ratio: `16:9` (Article Header) หรือ `1:1` (Inline)
- Resolution: `2k`
- Prompt Pattern: D-08 (Infographic) + Brand Style Constraint
- Output: `/path/to/blog/[topic]/illust_[N]_V##R##.png`
- Pairing: + `brand-guidelines`, + Internal Comms Skills

**Workflow:**
1. ขอ Brand Style Guide (Color, Style Keyword, Mood)
2. Compose Series Prompt with Consistent Style
3. Generate 5-10 ภาพในสไตล์เดียว
4. QA: ทุกภาพต้องดู "เป็นพี่น้องกัน"

---

## Category C: Internal / Productivity (2 Use Cases)

### UC-07: Mood Board / Reference Library

**Audience:** Internal Designer / Workshop Facilitator
**Use:** Pre-design Inspiration, Style Reference

**Specs:**
- Model: `flash` (Volume) หรือ `nb2` (Quality Selection)
- Aspect Ratio: หลากหลาย (เลือกตามภาพต้นแบบ)
- Resolution: `1k` หรือ `2k`
- Prompt Pattern: B-06 (Mood Board Item)
- Output: `/path/to/moodboard/[project]/[mood]_[N]_V##R##.png`
- Pairing: + `b2b-design-thinking`

**Workflow:**
1. ระบุ Project + Mood Keywords (3-5 คำ)
2. Generate 10-20 ภาพในมู้ดต่างๆ
3. Save เป็น Collection
4. ใช้เป็น Reference ไม่ใช่ Final

---

### UC-08: Iterative Edit Loop

**Audience:** Designer / Marketer ผู้ Refine ภาพหลายรอบ
**Use:** Refine ภาพเดิมหลายรอบ (Background, Style, Element)

**Specs:**
- Model: `nb2` (Default) หรือ `pro` (Complex Edit)
- Resolution: ตาม Original
- Mode: `edit`
- Prompt Pattern: Iterative Edit + ระบุ Preserve/Change ชัด
- Output: `/path/to/edits/[base]_v1.png`, `_v2.png`, `_v3.png`
- Naming: เพิ่ม `_v[N]` ทุกครั้งที่แก้

**Workflow:**
1. รับ Original Image Path
2. ขอ Specific Change (อะไรเปลี่ยน, อะไรรักษา)
3. ใช้ Iterative Edit Template
4. Generate → ดูผล → Iterate ถ้าจำเป็น
5. หลังพอใจ ลบ Intermediate versions

**Iteration Tips:**
- รอบ 1: เปลี่ยน Major (Background, Subject)
- รอบ 2: เปลี่ยน Color/Style
- รอบ 3+: Fine-tune Detail
- ห้ามแก้ทุกอย่างพร้อมกัน — รอบละ Change

---

## Output Naming Convention

ใช้ Convention นี้ทุก Use Case เพื่อให้หา/Track ง่าย:

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

| ผู้ใช้บอก | Use Case | Model | Aspect | Resolution |
|---|---|---|---|---|
| "Slide hero" | UC-01 | nb2 | 16:9 | 4k |
| "Product photo" | UC-02 | nb2/pro | 1:1 or 3:4 | 4k |
| "Workshop concept" | UC-03 | flash/nb2 | 4:3 or 16:9 | 2k |
| "Instagram post" | UC-04 | nb2 | 1:1 | 2k |
| "Web hero banner" | UC-05 | nb2 | 21:9 or 16:9 | 4k |
| "Blog illustration" | UC-06 | nb2 | 16:9 | 2k |
| "Mood board" | UC-07 | flash | varies | 1k |
| "แก้ภาพเดิม" | UC-08 | nb2/pro | match original | match original |
