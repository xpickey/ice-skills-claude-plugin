---
name: copy-page-md
description: "Copy Page MD — เก็บหน้าเว็บ/เอกสาร online เป็น clean Markdown ลงดิสก์พร้อม provenance frontmatter (source URL + fetch date) ทุกชิ้น สำหรับงานเก็บวัตถุดิบของเสี่ยวป้อ (retrieval-scout) และทุก persona ที่ต้อง save หน้าเว็บเป็น MD. หลักการจาก MD-This-Page (MIT — readability-extract เนื้อหลัก ตัด nav/ads) แต่ implement ด้วยเครื่องมือในระบบ ไม่ clone โค้ดภายนอกมารัน. Triggers (TH): เก็บหน้าเว็บ, แปลงเว็บเป็น MD, save หน้านี้, ดูดเว็บ, เก็บบทความ, copy page. Triggers (EN): copy page md, save page as markdown, web to markdown, fetch page, archive page."
---

> **Skill:** copy-page-md | **Version:** V01R01 | **Date:** 2026.07.18
> **ที่มา:** vet จาก `Ademking/MD-This-Page` (MIT) 2026.07.18 — ยืมหลักการ (Defuddle readability-extract → MD + metadata) เขียนใหม่ด้วยเครื่องมือในระบบ (supply-chain safe)

# กติกาเหล็ก
1. **A1/H2 GATE:** เข้า internet ได้เฉพาะเมื่อ user อนุญาตในงานนั้น (brief ระบุ `internet_permission: granted-by-user`) — ไม่มี = ทำได้เฉพาะไฟล์ local
2. **PROVENANCE บังคับทุกไฟล์** (กัน hallucination H3): ทุก MD ที่เก็บต้องมี frontmatter ตาม template ล่าง — ไฟล์ไม่มี provenance = ใช้อ้างอิงไม่ได้
3. **เก็บ ไม่ตีความ:** สกัด/ทำความสะอาด/จัดโครงได้ แต่ห้ามสรุปความเห็น ห้ามตัดสิน (การตีความเป็นของเทพ/L1)
4. **ls ยืนยันไฟล์เกิดจริงทุกครั้ง** + เขียน `_gather-result.md` สรุปรายการที่เก็บ (DISK-IS-TRUTH)

# METHOD LADDER (เลือกบนลงล่าง)
```
① WebFetch — แปลงหน้าเป็น markdown ในตัว · เหมาะหน้า static/บทความ · prompt สั่ง
   "return the full main content as clean markdown, keep headings/tables/links,
    drop nav/ads/footer" (= หลัก Defuddle)
② Browser pane (mcp__Claude_Browser__get_page_text / read_page) — หน้า JS-heavy /
   ต้อง login / ต้อง interact ก่อน · แปลงเป็น MD เอง (คงโครง heading/ตาราง)
③ Apify actor (rag-web-browser หรือ site-specific actor) — งาน scale หลายหน้า /
   เว็บกัน bot / ต้องการ structured data · เลือก actor ที่ rating สูง
④ ไฟล์ local (docx/pdf/html ในเครื่อง) — อ่านตรง + แปลงเป็น MD (ไม่ต้องขอ internet)
ทุกทาง: ห้าม bypass CAPTCHA · เจอ paywall/login ที่ไม่มีสิทธิ์ = หยุดรายงาน ไม่หาทางอ้อม
```

# OUTPUT TEMPLATE (ทุกไฟล์)
```markdown
---
source_url: "<URL เต็ม หรือ path ไฟล์ local>"
fetched: "YYYY.MM.DD HH:MM"
fetched_by: "retrieval-scout (เสี่ยวป้อ) | <persona>"
method: "webfetch | browser | apify:<actor> | local"
title: "<ตามหน้าจริง>"
author: "<ถ้ามี — ห้ามเดา>"
published: "<ถ้ามี — ห้ามเดา>"
status: "complete | partial(<เหตุผล>)"
---
<เนื้อหา Markdown สะอาด: คง heading/ตาราง/ลิงก์/code block · ตัด nav/โฆษณา/footer/cookie>
```
- ชื่อไฟล์: `<topic-slug>_<YYYY.MM.DD>.md` · ปลายทาง default: `[project]/00 - Context/_retrieved/` (หรือตาม brief)
- หลายหน้า → 1 ไฟล์/หน้า + `_gather-result.md` รวมรายการ (url · ไฟล์ · status · ขนาด)

*Skill: copy-page-md **V01R01** | 2026.07.18 | ใช้โดย: retrieval-scout-agent (หลัก) + ทุก persona · แรงบันดาลใจ: Ademking/MD-This-Page (MIT)*
