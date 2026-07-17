---
name: copy-design
description: "Copy Design — สกัด design language ของเว็บไซต์ (สีจริง typography spacing component patterns) ออกมาเป็นไฟล์ DESIGN.md มาตรฐาน (แนวคิด Google Stitch / VoltAgent awesome-design-md) เพื่อใช้ co-brand ลูกค้าใน deck/HTML demo/proposal — ต่อยอด customer-ci-finder จาก 'logo+hex' เป็น design system เต็มใบ. เก็บจากของจริงเท่านั้น ไม่ invent สี/ฟอนต์. Triggers (TH): เก็บ design เว็บ, สกัดสี CI ลูกค้า, ทำ DESIGN.md, copy design, ดึง design language, สี brand ลูกค้า. Triggers (EN): copy design, extract design system, DESIGN.md, brand extraction, design tokens from site."
---

> **Skill:** copy-design | **Version:** V01R01 | **Date:** 2026.07.18
> **ที่มา:** vet จาก `VoltAgent/awesome-design-md` (MIT) 2026.07.18 — ยืมโครง DESIGN.md (73+ ตัวอย่างจริง: Apple/Figma/Airbnb) มาเป็น template · เขียน extractor เองด้วยเครื่องมือในระบบ

# กติกาเหล็ก
1. **A1/H2 GATE:** เข้า internet เฉพาะเมื่อ user อนุญาตในงานนั้น
2. **ของจริงเท่านั้น (H3):** hex/font/spacing ทุกค่าต้องอ่านจากหน้า/CSS จริง (computed style · stylesheet · asset) — **ห้าม invent ค่า** · ค่าที่หาไม่ได้ = เว้นว่าง + ระบุ "not-found" (สอดคล้อง customer-ci-finder: "fetch → extract → ไม่ invent")
3. **PROVENANCE frontmatter บังคับ** (source_url + fetched + method) เหมือน copy-page-md
4. **เก็บ ไม่ตัดสิน:** สกัด design ที่เห็น ไม่วิจารณ์/ไม่เลือกให้ — การตัดสินใช้เป็นของ L1+design skills (b2b-slide-designer)

# วิธีสกัด (Method Ladder)
```
① Browser pane: เปิดหน้า → javascript_tool อ่าน getComputedStyle ของ element ตัวแทน
   (headings h1-h3 · body · buttons · links · cards) + ดึง CSS variables (:root)
   → ได้ hex/font/size/weight/line-height/radius จริง
② WebFetch หน้า + stylesheet หลัก → parse ค่าจาก CSS (fallback เมื่อไม่มี browser)
③ Screenshot (computer screenshot/zoom) → ยืนยันภาพรวม (สีที่ render จริง ≠ CSS เสมอ)
④ อ้างอิงโครงจากคลัง awesome-design-md (MIT) เมื่อเว็บดังมีอยู่แล้ว — cite repo
```

# DESIGN.md TEMPLATE (โครงตาม awesome-design-md — เติมเฉพาะที่เจอจริง)
```markdown
---
version: alpha
name: "<Brand>-design-analysis"
source_url: "<url>" · fetched: "YYYY.MM.DD" · method: "browser|webfetch"
description: "<1 ย่อหน้า: บุคลิก design ที่เห็นจริง — โทน สี จังหวะ ความรู้สึก>"
---
colors:            # hex จริงจากหน้า — primary/on-primary/ink/canvas/surface/accent/semantic
typography:        # ต่อ role (display/heading/body/caption): fontFamily/fontSize/fontWeight/lineHeight/letterSpacing
spacing_radius:    # grid unit · border-radius ที่ใช้ซ้ำ · shadow
components:        # ปุ่ม/card/nav ที่เป็นเอกลักษณ์ (รูปทรง+พฤติกรรม)
rules:             # กติกาที่สังเกตได้ (เช่น "CTA = pill เสมอ" "ไม่ใช้เงา")
not_found: [ ... ] # ค่าที่หาไม่ได้ — ห้ามเดา
```
- ปลายทาง: `[project]/00 - Context/_retrieved/DESIGN_<brand>_<YYYY.MM.DD>.md`
- ผู้ใช้ผล: กัปตัน/คิม (design spec ขั้น D-P2) + b2b-slide-designer (co-brand) + HTML demo (CSS vars)

*Skill: copy-design **V01R01** | 2026.07.18 | ใช้โดย: retrieval-scout-agent (หลัก) + ผู้ build ใน pipeline · แรงบันดาลใจ: VoltAgent/awesome-design-md (MIT) + Google Stitch DESIGN.md*
