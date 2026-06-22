<!-- ============================================================
     anti-slop-gates.md — Visual Anti-AI gates for slide design
     Transferable rules adapted from hallmark (MIT © Hallmark contributors / Together AI)
     https://github.com/Nutlope/hallmark — see NOTICE-hallmark.md for license.

     SCOPE: VISUAL slop only (ดีไซน์ที่ "ดูเหมือน AI ทำ"). คนละชั้นกับ:
       • qa-master D5 = anti-AI ภาษา/copy (24 patterns TH+EN) — นี่ไม่แตะภาษา
       • design-principles.md 20 rules = positive "ทำให้ถูก" — นี่คือ negative "ห้ามทำ AI tell"
     คัดเฉพาะ TRANSFERABLE-to-slide — ทิ้ง web-only (hover/scroll/responsive/nav/focus-ring/input-state).
     ============================================================ -->

# Anti-Slop Gates (Visual) — ตรวจก่อนปล่อย Design Spec / ก่อน build

> **หลัก:** AI มี "default look" ที่ทุกคนได้เหมือนกัน (purple gradient, italic header, ทุกอย่างอยู่กลาง,
> icon-card grid, emoji). gate พวกนี้จับ pattern ซ้ำซากนั้น. **ทุกข้อต้องตอบ "ไม่"** — ถ้า "ใช่" = แก้.
> ใช้คู่ design-principles 20 rules (positive) — anti-slop = negative gate (กันสิ่งที่ห้าม).

---

## 🎯 TOP TELLS — 5 ตัวที่จับบ่อยสุด (จำให้ขึ้นใจ)

| # | Tell | ทำไมเป็น AI · แก้ยังไง |
|---|---|---|
| **1** | **Italic header/display** | **#1 AI tell.** header/title ต้อง **roman เสมอ** — เน้นด้วย weight/สี/underline ไม่ใช่ italic. italic ใช้ได้แค่ใน body emphasis (กลางย่อหน้า) |
| **2** | **Purple→blue / cyan→magenta gradient** (โดยเฉพาะ gradient text) | single most-recognised AI look. ห้าม gradient บน text/headline · radial bloom บน bg ได้แต่ ≤20% |
| **3** | **Centered-everything** (title slide: eyebrow+title+lede+CTA แกนกลางเดียว) | auto-fail. กลางได้ ≤2 element · ที่เหลือ break alignment (eyebrow/CTA ชิดขอบ/numeral-anchor) |
| **4** | **Emoji เป็น feature icon** (✨🚀⚡🔥🎯✅) | instant AI tell. ใช้ icon library เดียว (catalog-icons 401 SVG) · ไม่ emoji ใน bullet/value-prop |
| **5** | **Invented metric** ("เร็วขึ้น 10×", "50,000+ ลูกค้า" ที่กุเอง) | อ่านเหมือนโกหก. แทนด้วย "—" + "ยืนยันตัวเลข" หรือ rebuild section · ตัวเลขต้องมาจาก user |

---

## 📋 FULL CHECKLIST (18 transferable gates — group ตามหมวด)

### TYPOGRAPHY
1. **Display font = Inter/Roboto/Open Sans/Poppins/Lato/DM Sans/system default?** → banned (LLM ถูก train มากับพวกนี้). ใช้ font จาก §5.5 whitelist
2. **Italic header/display?** → FAIL (#1 tell — ดูบน). header roman เสมอ
3. **>3 font families ในหน้าเดียว?** → 2+1 rule: display + body + outlier 1 ตัว (wordmark/big-stat). 4th = slop
4. **weight ต่างกัน <300?** (body 400 + heading 600 = "default setting") → ต่างให้ ≥300 (400+700 หรือ 400+200)

### COLOR
5. **purple→blue/cyan→magenta gradient ที่ไหน?** (especially gradient text) → ห้าม (tell #2)
6. **accent >5% ของพื้นที่ slide?** (solid fill/heading สี accent/full-bleed) → accent = emphasis ไม่ใช่ paint. ถอย
7. **pure #000 หรือ #fff เป็น base?** → tint neutral ไป accent hue นิด (paper สว่าง 92-98% · dark 12-18%) — ไม่ flat
8. **neutral/grey ไม่ tint (เทาด้าน ๆ)?** → tint ทุก grey ไป accent hue (warm accent→warm greys) — coherent
9. **สีเดียวทั้งหน้า / ไม่มี accent moment?** → 1 accent ชัด (60-30-10)

### LAYOUT
10. **Centered-everything (title slide)?** → auto-fail (tell #3). break alignment
11. **3-equal-column icon-card grid** (icon บน + heading)? → template default. ใช้ asymmetry/variation
12. **card-in-card** (การ์ดซ้อนการ์ด)? → visual slop
13. **thick colored side-stripe** (เส้นสีหนา 4-6px ซ้าย/ขวา card)? → instant tell
14. **arbitrary spacing** (17px, ค่ามั่ว)? → ใช้ 8pt scale (8/16/24/32/48/64/96) ทุก padding/gap/margin
15. **decorative element ไม่มีเหตุผล** (blob/scanline/badge/numeral ที่ไม่ anchor เนื้อหา)? → decoration ต้อง motivated

### ICON & IMAGERY
16. **mix 2+ icon libraries** (Material + Lucide + Heroicons ปนกัน)? OR **emoji เป็น feature icon**? → 1 library (catalog-icons 401) · ไม่ emoji (tell #4)

### CONTENT HONESTY
17. **invented metric** (ตัวเลขที่ user ไม่ได้ให้ + กุเพื่อ fill stat-layout)? → "—" + "ยืนยันตัวเลข" (tell #5) · stat ไม่เป็น headline เดี่ยว (ต้องมีคำอธิบายคู่)
18. **fake UI mockup วาดเอง** (browser bar + traffic-light dots / phone frame+notch / IDE chrome)? → ใช้ screenshot จริง หรือไม่ใส่ chrome

---

## CONTRAST (ผูก design-principles rule 11 + §5.5 — ไม่ซ้ำ แค่ย้ำ slop-case)
- **black-on-black bug:** text สี ink บน bg สี ink (ลืม flip สี) → ทุก surface สี accent ต้องมี accent-ink (text สีตัด)
- **dark section ink-on-ink:** panel bg เข้ม (L<50%) ต้อง swap text เป็นสีอ่อน + child inherit
- ทุก (color, background) pair ต้องผ่าน WCAG ≥4.5:1 body / ≥3:1 large

---

## วิธีใช้ (prevention — slide-designer)
1. ก่อนออก Design Spec → ไล่ checklist (เน้น 5 top tells)
2. เจอ "ใช่" → แก้ก่อนส่ง presentation-creator
3. customer-facing → เข้มทุกข้อ · internal/draft → เน้น 5 top tells

## วิธีใช้ (detection — qa-master D7.S)
- scan deck ที่ build แล้ว → FLAG gate ที่ละเมิด (ไม่ auto-block) → ส่ง Compass ตัดสิน
- ชัดเจน (gradient text/emoji/italic header) → recommend แก้ · ก้ำกึ่ง → revalidate

---

*Transferable subset (~18 จาก 58 hallmark gates) — ทิ้ง web-only (microinteraction/responsive/nav/input/sticky ~40 gate). adapted 2026.06.20.*
