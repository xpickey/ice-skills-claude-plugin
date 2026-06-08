# iCE-Propose Template — Designer Brief (Proposal-Optimized iCE Variant)

> **Version:** V01R01 | **Date:** 2026-05-15
> **Concept:** "Premium Enterprise Advisor with a Soft Edge" — Confident, Calm, Technical-Premium
> **Source of Truth:** Distilled from 6 real iCE Consulting deliverables + iCE Corporate Identity Guideline (Dec 2021)
> **Relationship to iCE-CI:** iCE-Propose เป็น Variant ของ iCE-CI ที่ปรับให้เหมาะกับงาน Proposal, Solution Architecture, Project Roadmap, และ TOR-Compliance เป็นการเฉพาะ

---

## 1. Theme Concept

iCE-Propose คือ Template ที่ปรับ Visual Language ของ iCE-CI ให้เหมาะกับ **งานเสนอขายและงานนำเสนอโครงการระดับองค์กร** เป็นการเฉพาะ โดยเน้น 3 จุดที่ต่างจาก iCE-CI มาตรฐาน:

1. **3D Glass-Metallic Infographic** — ใช้ icon แบบไอโซเมตริก 3 มิติ สไตล์กระจก-โลหะ แทน outline icon 2 มิติ
2. **Bilingual EN-first Hierarchy** — ภาษาอังกฤษเป็นหัวเรื่องหลักเสมอ ภาษาไทยเป็นรอง
3. **4 Signature Layout Patterns** — Two-Column Split, Horizontal Tech Flow, 3×2 Phase Grid, Timeline+Swimlane (สกัดจากผลงาน iCE จริง)

อารมณ์ของ Template: Premium, Confident, Calm, Technical, Trustworthy — มืออาชีพระดับสากล แต่ไม่แข็งกระด้าง

> **เมื่อไรควรใช้ iCE-Propose แทน iCE-CI:**
> - งาน Proposal / RFP / TOR Response ที่ต้องการ visual impact สูงกว่า CI มาตรฐาน
> - Solution Architecture / Integration Diagram ที่ต้องใช้ 3D infographic
> - Project Roadmap / Master Schedule + RACI ที่ต้องการ swimlane bar
> - Methodology Slide / Governance Slide ที่ต้องการ pyramid hierarchy
> - งานที่ต้องนำเสนอผู้บริหารระดับ C-Suite หรือ Board

> **เมื่อไรควรใช้ iCE-CI แทน iCE-Propose:**
> - เอกสารทางการที่ต้องการความเรียบและความเป็น Official สูงสุด
> - Press Release, Annual Report, Letter Head, Memo
> - งานที่ต้อง print ขาวดำเป็นหลัก (3D infographic จะหายไป)

---

## 2. Color System (ขยายจาก iCE-CI + Verified Pairing จากภาพจริง)

### 2.1 Primary Palette (อ้างอิงจากคู่มือ CI — เหมือน iCE-CI)

| Role | Hex | ชื่อทางการ |
| :--- | :--- | :--- |
| Main Color | `#1E66A4` | น้ำเงิน iCE |
| Secondary Color | `#41A8B5` | ฟ้า iCE |
| Pure White | `#FFFFFF` | ขาว |
| Dark Gray (แทนสีดำ) | `#595959` | เทาเข้ม |

### 2.2 Suggested Background Gradient

| Direction | Stops | ใช้ใน |
| :--- | :--- | :--- |
| Diagonal 135° (default) | `#1E66A4` → `#41A8B5` | Cover, Section Divider, Closing |
| Linear Horizontal 90° | `#1E66A4` → `#41A8B5` | Top Banner ของ Phase Grid |

### 2.3 Tints & Shades (ขยายเพิ่มเพื่อใช้งานจริง — เหมือน iCE-CI)

| Token | Hex | การใช้งานใน iCE-Propose |
| :--- | :--- | :--- |
| iCE Blue 95 | `#194F7A` | Hover State, Heading เน้น, Label บน 3D Block |
| iCE Blue 80 | `#2B7AC0` | Body Heading รอง, iCE Bar (Gantt) |
| iCE Blue 50 | `#7AA8CC` | Background Card อ่อน, Icon Mid-tone, Pyramid Mid Layer |
| iCE Blue 30 | `#A8C7E0` | Border, Divider, Phase Card Outline |
| iCE Blue 10 | `#E5EEF5` | Background Highlight อ่อน, Tech Diagram Panel |
| iCE Cyan 50 | `#7BC9D2` | Tint รอง Chart, Pyramid Top Layer |
| iCE Cyan 10 | `#DAEEF1` | Background Secondary |
| Cool Gray Light | `#F4F6F8` | Section Background |
| Mid Gray | `#9CA3AF` | Caption, Customer Bar (Gantt) |

### 2.4 Semantic Colors (ใช้เฉพาะกรณีจำเป็น)

| สถานะ | Hex | ใช้เมื่อ |
| :--- | :--- | :--- |
| Success | `#16A34A` | Sign-off ผ่าน, Milestone สำเร็จ |
| Warning | `#D97706` | Risk Medium, Attention Required |
| Error | `#DC2626` | Risk High, Blocker |
| Info | `#41A8B5` | Default Note (ใช้ iCE Secondary) |

### 2.5 Verified Color Pairings (สกัดจากผลงาน iCE จริง 6 ชิ้น)

คู่สีที่ผู้ออกแบบใช้ซ้ำในผลงานหลายชิ้น — ใช้ได้ทันทีไม่ต้องคิดใหม่:

| Pair Name | สีคู่ | พบในภาพ |
| :--- | :--- | :--- |
| Header Gradient | `#1E66A4` → `#41A8B5` (diagonal หรือ horizontal) | ทุกภาพ |
| 3D Block Tri-tone | Top `#7BC9D2` + Mid `#41A8B5` + Base `#1E66A4` | Pyramid + Diamond Markers |
| Card on Light BG | White card + `#F4F6F8` BG + `#A8C7E0` border | Phase Cards |
| Gantt Bar Coding | `#1E66A4` iCE / `#9CA3AF` Customer / `#41A8B5` Joint | Master Schedule |
| Tech Diagram Frame | `#E5EEF5` panel + `#1E66A4` outline + Cool Gray content | Solution Architecture |
| Toolset Tile | White top + `#1E66A4` หรือ `#41A8B5` bottom strip | Toolset Gallery |

---

## 3. Typography Hierarchy (เหมือน iCE-CI + Bilingual Rule เพิ่ม)

### 3.1 Font Stack (ตามคู่มือ CI)

| Language | Headline | Body A | Body B |
| :--- | :--- | :--- | :--- |
| English | Raleway ExtraBold | Raleway | Open Sans Light |
| Thai | Kanit Bold | Kanit Light | Sarabun Regular |

### 3.2 Type Scale (PPTX 16:9 — ปรับจาก iCE-CI ให้ลึกขึ้นสำหรับงาน Proposal)

| Level | EN (pt) | TH (pt) | Color | Weight |
| :--- | :--- | :--- | :--- | :--- |
| H1 Title (EN-first) | 36-44 | 32-40 | `#1E2937` (เกือบดำ) | ExtraBold/Bold |
| H1 Sub (TH-second) | 22-26 | 22-26 | `#595959` | Regular |
| H2 Section | 22-26 | 20-24 | `#1E66A4` | Bold |
| H3 Item | 18-20 | 16-18 | `#1E2937` | Bold |
| Body | 12-14 | 12-14 | `#595959` | Regular |
| Caption | 9-10 | 9-10 | `#9CA3AF` | Regular |

### 3.3 Bilingual EN-first Hierarchy Rule (กฎเฉพาะของ iCE-Propose)

ในผลงาน iCE จริงทุกชิ้น — ภาษาอังกฤษเป็นหัวเรื่องหลักเสมอ ขนาดใหญ่กว่า หนากว่า เข้มกว่า ภาษาไทยเป็นรองอยู่ใต้ ขนาดเล็กกว่า เบากว่า สีอ่อนกว่า

```
[ENGLISH HEADLINE — Bold, Dark, Large]
[Thai sub-headline — Regular, Gray, Smaller]
```

ห้ามสลับลำดับ ห้ามใช้ขนาดเท่ากัน ห้ามใช้สีเดียวกัน — กฎนี้ไม่มีข้อยกเว้นใน iCE-Propose

---

## 4. Grid System (เหมือน iCE-CI)

### 4.1 PPTX 16:9 (1280 × 720 px)

- Margin: 48 px ทุกด้าน (5-7% ของ width)
- Column: 12
- Gutter: 24 px
- Header Height: 80 px
- Footer Height: 32 px (เส้น iCE Secondary บางๆ)
- Whitespace Target: 35-45% ของพื้นที่ทั้งหมด (สูงกว่า template อื่น)

### 4.2 Logo Placement (ปรับจาก iCE-CI สำหรับงาน Proposal)

| Position | ใช้เมื่อ |
| :--- | :--- |
| มุมซ้ายบน | Cover Slide, Intro Page |
| มุมขวาบน | Content Slide ทั่วไป (ที่พบบ่อยที่สุดในผลงานจริง) |
| มุมซ้ายล่าง | Footer Mode (เมื่อมี page number ขวาล่าง) |

**กฎ:** มุมเดียวต่อหน้า — ไม่ใส่ logo สองมุมในหน้าเดียวกัน

---

## 5. Spacing / Padding Scale (เหมือน iCE-CI)

| Token | Value |
| :--- | :--- |
| xxs | 4 px |
| xs | 8 px |
| sm | 16 px |
| md | 24 px |
| lg | 32 px |
| xl | 48 px |
| 2xl | 64 px |

---

## 6. Image & 3D Infographic Treatment (จุดต่างหลักจาก iCE-CI)

### 6.1 3D Icon System (ลายเซ็นของ iCE-Propose)

iCE-Propose ใช้ **3D Isometric Icons** แทน outline icon ของ iCE-CI

| Attribute | Specification |
| :--- | :--- |
| Style | Isometric 3D, มุมเอียง 15-25° |
| Material | Glass + Metallic mix, soft reflection |
| Color Range | Monochromatic blue-cyan (`#7AA8CC` ถึง `#41A8B5`) |
| Highlight | สีอ่อนกว่า ฝั่งแสงด้านบน-ซ้าย |
| Shadow | Soft drop shadow ใต้ icon, opacity 15-25% |
| Background | วางบน platform/base disc สีโทนเดียวกัน |
| Size Consistency | ใช้ size เดียวกันใน gallery — ห้ามผสมใหญ่-เล็ก |

### 6.2 3D Block / Diamond Marker

ใช้สำหรับ **Milestone หรือ Phase Boundary**:

| Attribute | Specification |
| :--- | :--- |
| รูปทรง | Cube/Diamond ไอโซเมตริก |
| สี | เริ่ม `#1E66A4` ที่ phase แรก → ค่อยๆ ไล่ไป `#41A8B5` ที่ phase หลัง |
| ขนาด | ใหญ่กว่า icon ทั่วไป 1.5-2 เท่า |
| ตำแหน่ง | ลอยอยู่เหนือ timeline หรือคั่นระหว่าง phase |
| Label | วางบน (เช่น "Project Charter", "Go-Live") สี `#1E2937` |

### 6.3 3D Pyramid / Tier Structure

ใช้สำหรับนำเสนอ **Hierarchy หรือ Governance Tier**:

| Attribute | Specification |
| :--- | :--- |
| จำนวนชั้น | สูงสุด 3 ชั้น (ห้ามเกิน 4) |
| ชั้นบนสุด | Cube เล็ก สี `#41A8B5` + glow effect บน |
| ชั้นกลาง | Slab กลาง สี `#7AA8CC` โปร่งใสเล็กน้อย |
| ชั้นล่าง | Slab ใหญ่ สี `#1E66A4` เป็นฐาน |
| เส้นเชื่อม | เส้นโค้งบาง สี `#7AA8CC` จากแต่ละชั้น → label ทางขวา |

### 6.4 Photographic Image (เมื่อใช้)

- โทนภาพ: Professional, Clean, Modern (เหมือน iCE-CI)
- รูปทรง: สี่เหลี่ยมขอบมน 8 px
- Filter: Blue Cast เล็กน้อย
- Overlay: iCE Main Blue Opacity 30%

---

## 7. Iconography Style (ต่างจาก iCE-CI ตรงนี้)

| Attribute | iCE-CI | iCE-Propose |
| :--- | :--- | :--- |
| Default Style | 2D Outline 2 px | 3D Isometric Glass-Metallic |
| Color | `#1E66A4` / `#41A8B5` | Monochromatic blue-cyan range |
| Size | 24 / 32 / 48 px | 48 / 64 / 96 px (ใหญ่กว่าเพราะมี depth) |
| Use When | งาน formal, print, memo | งาน proposal, executive deck |

**สำรอง 2D Outline icon** สำหรับใช้ใน body text หรือ inline element — ไม่ใช่ทุกที่ต้องเป็น 3D

---

## 8. Connector & Flow Lines (เฉพาะสำหรับ Tech Diagram)

| Type | Spec | ใช้เมื่อ |
| :--- | :--- | :--- |
| Solid Arrow | 2 px stroke `#41A8B5` ปลายลูกศรเล็ก | Data flow ปกติ |
| Glowing Pipe | Gradient tube + animated arrow inside | Secure connection (VPN, MPLS) |
| Dotted Line | 1.5 px dashed `#A8C7E0` | Optional/Conditional link |
| Curve Hint | Bezier curve อ่อน ๆ ซ้ายไปขวา | Hierarchical link (pyramid → label) |
| Bidirectional | คู่ลูกศรซ้าย-ขวาในท่อ | Bi-directional integration |

---

## 9. Animation & Transition (เหมือน iCE-CI)

- Slide Transition: Fade 0.4s
- Object Animation: Fade-In 0.3s
- 3D Object Reveal: Scale + Fade 0.5s (เฉพาะ icon 3D)
- หลีกเลี่ยง: Bounce, Spin, Comic Animation

---

## 10. Accessibility Notes (เหมือน iCE-CI)

| ประเด็น | มาตรฐาน |
| :--- | :--- |
| Contrast (Dark Gray บนขาว) | 12.6:1 (AAA) |
| Contrast (ขาวบน iCE Main Blue) | 7.2:1 (AAA) |
| Body Font Size | ≥ 12 pt (PPTX 16:9), ≥ 11 pt (Word) |
| Print Test | ผ่านการพิมพ์ขาว-ดำ — แต่ 3D infographic จะหายไป |

---

## 11. 4 Signature Layout Patterns (สกัดจากผลงาน iCE จริง)

นี่คือจุดต่างที่ใหญ่ที่สุดจาก iCE-CI — iCE-Propose มี **4 Signature Patterns** ที่พบในผลงาน iCE จริงทุกชิ้น แทนที่จะมี 15 Layout แบบ template อื่น เพราะ Patterns เหล่านี้ครอบคลุม 80% ของ slide ใน Proposal ทั่วไป

### Pattern A — Two-Column Split (สำหรับ Methodology / Governance)

**ใช้เมื่อ:** อธิบาย Principle คู่กับ Structure ในหน้าเดียวกัน

```
+--------------------------------+--------------------------------+
| Core Principles (45%)          | Visualization (55%)            |
| - 3D icon + Item 1             | [3D Pyramid / 3D Diagram]      |
|   + bullet description         | + Tier labels ขวา              |
| - 3D icon + Item 2             |                                |
|   + bullet description         |                                |
| - 3D icon + Item 3             |                                |
|   + bullet description         |                                |
+--------------------------------+--------------------------------+
| Toolset Gallery (4-5 cells, full width, equal size)             |
+-----------------------------------------------------------------+
```

**Specs:**
- Title: Bilingual EN-first บนสุด (Section 3.3)
- Left Column: 3D Icon `#7AA8CC`→`#41A8B5` + H3 + Body
- Right Column: 3D Pyramid 3-Tier ตาม Section 6.3
- Toolset Tile: White top + `#1E66A4` strip ล่าง
- Logo: มุมขวาบน

### Pattern B — Horizontal Tech Flow (สำหรับ Solution Architecture)

**ใช้เมื่อ:** อธิบาย Integration, Data Flow, System Architecture

```
                                +----------+
                                | Identity |
                                | Provider |
                                +----+-----+
                                     |
+----------+    +----------+    +----v-----+    +----------+
| Source   | -> | Transport| -> | Dest.    | -> | Outputs  |
| Systems  |    | (VPN)    |    | Cloud    |    | (Reports)|
| (icons)  |    | (lock)   |    | (cloud)  |    | (panels) |
+----------+    +----------+    +----------+    +----------+
```

**Specs:**
- Title: Bilingual EN-first
- Zone 1: Card `#E5EEF5` + 3D icons ของ source systems
- Zone 2: Glowing Pipe gradient + Lock icon (3D)
- Zone 3: 3D Cloud + Cube ภายใน
- Zone 4: Output Stack Box (2 ชั้น) — Outbound Reports + Datasets
- Connector: Solid arrow `#41A8B5` ระหว่าง zone

### Pattern C — 3×2 Phase Grid (สำหรับ Roadmap / Process)

**ใช้เมื่อ:** Phase-based Roadmap 4-6 ระยะ, Method Steps

```
+--------------------------------------------------------+
| Top Banner: Solid #41A8B5 + Title ขาว                  |
+--------------------------------------------------------+
+----------+ +----------+ +----------+
| PHASE 1  | | PHASE 2  | | PHASE 3  |
| ✓ Item   | | ✓ Item   | | ✓ Item   |
| ✓ Item   | | ✓ Item   | | ✓ Item   |
| ✓ Item   | | ✓ Item   | | ✓ Item   |
+----------+ +----------+ +----------+
+----------+ +----------+ +----------+
| PHASE 4  | | PHASE 5  | | PHASE 6  |
| ✓ Item   | | ✓ Item   | | ✓ Item   |
+----------+ +----------+ +----------+
```

**Specs:**
- Top Banner: Solid `#41A8B5` พร้อม Title สีขาว + Subtitle ไทย
- Card: White fill, 8px radius, border `#A8C7E0` 1 px, left accent bar `#41A8B5` 4 px
- Header Card: Bold UPPERCASE ภาษาอังกฤษ + ภาษาไทยกำกับใต้
- Bullets: Check icon `#41A8B5` (ห้ามใช้จุดดำ)
- Logo: มุมขวาบน

### Pattern D — Timeline + Swimlane (สำหรับ Master Schedule + RACI)

**ใช้เมื่อ:** Master Schedule + Roles/Responsibilities + RACI ร่วมกัน

```
Milestones:   ◆ Charter  ◆ Design SO  ◆ SIT SO  ◆ Go-Live  ◆ Warranty End
              (3D Diamond — gradient #1E66A4 → #41A8B5 ตาม phase)

Project Mgmt:  ████ iCE   ████████ Joint    ░░░░░░░░ Customer
Implementation:           ████ iCE   ░░░░░░░░ Customer   ████ Joint
Data Migration:           ████ iCE   ░░░░░░░░ Customer
Testing:                       ████ iCE   ████ Joint   ░░░░░░░░ Customer
Support & Training:                              ████ iCE   ████████ Joint

Timeline:     Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec
              Phase 1 | Phase 2 | Phase 3 | Phase 4 | Phase 5 | Phase 6
              (3D Diamond markers ระหว่าง phase brackets)

+--------------------------------------------------------+
| Legend: ▓ iCE Consulting  ░ Customer  ▒ Joint          |
+--------------------------------------------------------+
```

**Specs:**
- Top Milestones: 3D Diamond markers (Section 6.2) + label สีดำ
- Swim-lane labels: ซ้ายมือ Bold `#1E2937`
- Bars: iCE `#1E66A4` / Customer `#9CA3AF` / Joint `#41A8B5`
- Bottom Axis: Month labels + Phase brackets
- Legend Box: White card + border `#A8C7E0` + color chip ซ้ายของแต่ละ entry
- Logo: มุมขวาบน

### Quick Decision Matrix

| โจทย์ Slide | Pattern | ตัวอย่างจริง |
| :--- | :--- | :--- |
| Methodology + Governance | A | Implementation & Governance Methodology |
| Solution Architecture | B | ERP Cloud Architecture, TOR Compliance |
| Phase-based Roadmap | C | Project Implementation Roadmap |
| Master Schedule + RACI | D | Detailed Master Project Schedule |
| Single concept + 3-5 items | A ดัดแปลง | — |
| Comparison 2-3 columns | A ดัดแปลง equal columns | — |
| Process step-by-step | C ดัดแปลง 1 แถวยาว | — |

---

## 12. Composition Rules

### 12.1 Reading Path (ลำดับสายตา)

อ่านจากผลงาน iCE จริงพบลำดับเดียวกันทุกชิ้น:

1. Title Block บนสุด (EN bold → TH light)
2. Section Headers สี iCE Blue
3. Visual Element (3D icon / diagram) เป็น Focal Point
4. Body Content สี Dark Gray
5. Caption / Footnote สี Mid Gray ล่างสุด
6. Logo + Page Number มุมเดียว

### 12.2 Whitespace Discipline

iCE-Propose มี whitespace ratio สูงกว่า template อื่น — 35-45% ของหน้า เพื่อให้ executive อ่านได้สบายตา ห้ามอัด content แน่นเกินไป

---

## 13. Anti-Patterns — สิ่งที่ห้ามทำใน iCE-Propose

อ่านจากผลงาน iCE จริง 6 ชิ้น — สิ่งต่อไปนี้ **ไม่เคยปรากฏ**:

| ห้าม | เหตุผล |
| :--- | :--- |
| ใช้สีนอก palette (ม่วง ส้ม ชมพู) | ทำลาย brand recognition |
| ผสม flat icon กับ 3D icon ในหน้าเดียว | คนละ visual language |
| Shadow แรงเกินไป หรือ heavy gradient | ดูเป็น "AI-generated stock" |
| Title ไทยใหญ่กว่า EN | ผิด bilingual hierarchy |
| Bullet จุดดำ | ใช้ check icon `#41A8B5` |
| Navy เต็มหน้า ใน content slide | iCE ใช้ white/light gray |
| Emoji ในเนื้อหา | ใช้ 3D icon family เท่านั้น |
| Font นอก stack | ผิดมาตรฐาน CI |
| Logo สองมุมในหน้าเดียว | duplicate brand mark |
| Icon ใน gallery สลับใหญ่-เล็ก | ทำลาย rhythm |

---

## 14. Application Notes

### 14.1 PowerPoint
- Master Slide กำหนด Theme Color: iCE Main / iCE Secondary / Cool Gray / White
- Theme Font: Heading = Kanit Bold + Raleway ExtraBold, Body = Sarabun + Open Sans Light
- Asset Library: 3D icon set แยกต่างหากจาก 2D icon ของ iCE-CI
- บันทึก `.potx` เป็น Template มาตรฐาน iCE-Propose

### 14.2 Word (ใช้เฉพาะ Proposal Document)
- ใช้ iCE-CI Word template เป็นฐาน
- เพิ่ม 3D icon เฉพาะหน้า Executive Summary และ Methodology
- หน้าอื่นใช้ outline icon ปกติเพื่อความเรียบ

### 14.3 ห้ามทำ (เพิ่มจาก iCE-CI)
- ห้ามใช้ 3D icon เกินขนาด 30% ของ slide area (รก)
- ห้ามใช้ Pattern C 3×2 Grid กับเนื้อหาที่มีเพียง 2-3 ระยะ (เลือก Pattern A แทน)
- ห้ามใช้ Pattern D Timeline กับ project ที่สั้นกว่า 6 เดือน (ใช้ Pattern C แทน)

---

## 15. Cross-Reference: เลือก Template ไหนระหว่าง iCE-CI กับ iCE-Propose

| สถานการณ์ | Recommend |
| :--- | :--- |
| Proposal / RFP / TOR Response (visual impact สูง) | **iCE-Propose** |
| Solution Architecture / Integration Diagram | **iCE-Propose** |
| Project Roadmap + RACI | **iCE-Propose** |
| Methodology / Governance Slide | **iCE-Propose** |
| Executive Briefing / Board Paper | **iCE-Propose** |
| Press Release / Annual Report | **iCE-CI** |
| Letter Head / Memo / Email Template | **iCE-CI** |
| Internal Working Document | **iCE-CI** |
| งานที่ต้อง print ขาว-ดำเป็นหลัก | **iCE-CI** |
| Customer-facing Brochure | **iCE-CI** หรือ **iCE-Propose** (ตาม mood) |

---

**Source:** Distilled from 6 real iCE Consulting deliverables:
1. Implementation & Governance Methodology (Pattern A)
2. Solution Architecture (ERP Cloud Finance) (Pattern B)
3. Project Implementation Roadmap (Pattern C)
4. Detailed Master Project Schedule (Pattern D)
5. Solution Architecture TOR Compliance v1 (Pattern B variant)
6. Solution Architecture TOR Compliance v2 (Pattern B variant)

**End of iCE-Propose Designer Brief — V01R01**
