# NOTICE — iCE B2B Combo Skill

สกิลนี้ (`ice-b2b-combo`) รวมและเรียบเรียงใหม่จากชุดความรู้งานขาย/พรีเซลล์ B2B Enterprise Software ของ
iCE Consulting พร้อมเทคนิคการทำงานที่สกัดมาจากแนวปฏิบัติภายใน และนโยบายการจัดการ context จากโครงการโอเพนซอร์ส.
เนื้อหา **เขียนใหม่ทั้งหมด** (ไม่คัดลอกโครงสร้าง/ถ้อยคำเดิม) และทำให้ portable (ไม่ผูกกับเครื่องมือ/agent เฉพาะเครื่อง).

---

## 1. ฐานความรู้งานขาย (เรียบเรียงใหม่จาก 17 สกิลภายใน)

reference ในสกิลนี้สังเคราะห์ใหม่จากชุดสกิลงานขายของ iCE Consulting:

**Method (วิธีขาย/วิธีคิด):** enterprise-sale-strategy · solution-selling · strategic-thinking ·
design-thinking · why-thinking · questioning · relationship-management

**Product (ความรู้ผลิตภัณฑ์):** Oracle Cloud Applications · Oracle EBS · NetSuite · NetSuite Thailand advisory

**Domain (overlay ไทย/vertical):** FinTech/Lending/IFRS9 · GFMIS ภาครัฐ · e-GP จัดซื้อจัดจ้าง · Thai e-Tax compliance

**QA:** pre-flight deck checklist

> เนื้อหาถูก dedup — แนวคิดที่ใช้ร่วม (qualification scorecard, why-stack, กรอบคิด, Thai calibration) รวมไว้ที่
> `references/_shared/` ที่เดียว.

---

## 2. เทคนิคการทำงาน (สกัดจากแนวปฏิบัติภายใน — ไม่ระบุชื่อ)

4 "หมวก" ใน `references/_capabilities/` สกัดวิธีทำงานจากบทบาทภายในของ iCE:
- **ROUTE** — Context-Lock, mode selection, routing, validation gates, anti-loop, positive wording
- **KNOW** — FACT/PATTERN/ASSUMPTION gate, primary-lock, confidence scoring, retrieval discipline
- **BUILD-SPEC** — font discipline, build lessons, build-vs-edit, preview-first (ออก spec ไม่ build เอง)
- **CHECK** — 9-dimension QA, speed-tier, detector-not-decider

---

## 3. Context Discipline — adapted from claude-tmux-compact

`references/context-discipline.md` ปรับนโยบายการจัดการ context มาจาก:

**claude-tmux-compact** — https://github.com/nutoanan/claude-tmux-compact · License: **MIT**

ดึงเฉพาะ **นโยบาย** (Worth-It check: SAFE/PAYOFF/NO-THRASH · keep-pointers-not-payloads ·
classify TERMINUS/CONTINUATION/GREY-ZONE) — **ไม่ได้นำกลไก tmux/shell hooks มาใช้** (อันนั้นผูกกับ runtime เฉพาะ).
เนื้อหา rewrite เป็นวินัยทั่วไปที่ใช้ได้ทุกสภาพแวดล้อม.

```
MIT License — Copyright (c) claude-tmux-compact contributors
Permission is hereby granted, free of charge, to any person obtaining a copy of this software
and associated documentation files (the "Software"), to deal in the Software without restriction…
(ดูฉบับเต็มที่ repository ต้นทาง)
```

---

## 4. Portability

สกิลนี้ออกแบบให้ **ใช้ได้ทุกเครื่อง/ทุกสภาพแวดล้อม**:
- ไม่อ้างชื่อ agent ภายในของ fleet · ไม่ผูก MCP/tool เฉพาะเครื่อง · ไม่มี absolute path.
- งานสร้างเอกสาร = **ออก spec** ให้เครื่องมือใด ๆ ทำตาม ไม่รัน build เอง.
- การค้น web ใช้เครื่องมือที่มีในสภาพแวดล้อมนั้น (tool-agnostic).

---

*iCE B2B Combo — สังเคราะห์จากชุดความรู้ภายใน + แนวปฏิบัติการทำงาน + Context Discipline (MIT). เขียนใหม่ทั้งหมด.*

---

## CHANGELOG

- **R2 (2026.08.23)** — sync กับ fleet ที่ขยับหลังสร้างรอบแรก (25 มิ.ย.):
  1. **แก้กติกาฟอนต์ตามนโยบาย 2026.07.31** (พิสูจน์ด้วย PDF จริง 45 ฉบับ): ค่าเริ่มต้น = single-family
     ไทย=อังกฤษขนาดเท่ากัน **ยกเลิก "+1-2pt"** · เอกชน = IBM Plex Sans Thai Looped · ราชการ = TH Sarabun New
     (แทน PSK) · จับคู่ 2 ตระกูลเฉพาะเมื่อลูกค้าบังคับ brand font (`_capabilities/build-spec.md`).
  2. **เพิ่ม Pitch-Belief** (5 บทเรียน — ลูกค้าซื้อความเชื่อ) ใน `method/why-thinking.md` §7 +
     **Reality anchor สองเสียง DREAM+REALITY ทุกชั้น WHY** ใน `_shared/why-stack.md`.
  3. **เพิ่ม `product/tor-competitive.md`** — playbook ตั้งสเปก/ตอบ TOR แบบ dual-angle (Fusion⇄NetSuite)
     กลั่นจาก TOR Competitive KB ภายใน (171 record-views · 2026-06-29) พร้อมกติกาถ่วงดุล/fairness ครบ.
- **R1 (2026.06.25)** — สร้างครั้งแรกจาก 17 สกิลภายใน + 4 capabilities + context discipline.
