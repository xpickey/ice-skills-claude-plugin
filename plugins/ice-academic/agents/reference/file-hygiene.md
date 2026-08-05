# FILE HYGIENE — กฎที่เก็บไฟล์ชั่วคราว/ไฟล์ทำงานของทั้ง fleet (SSOT)

> **Version:** V01R02 | **Date:** 2026.08.06 | คำสั่ง user (design โดย user เอง)
> **ใช้กับ:** ทุก agent + L0 session · ไฟล์ temp, ไฟล์ทดสอบ, render PDF/PNG, ภาพ crop ตรวจงาน,
> ไฟล์ทดลอง, ไฟล์ระหว่างทางทุกอย่างที่ไม่ใช่ deliverable จริง

## กฎหลัก 3 ข้อ (design โดย user 2026.08.06)

**① ที่เก็บ temp เดียวต่อ sub-project — `<sub-project>/20-Output/_temp/`**
ทุก agent เก็บไฟล์ temp/ทดสอบ**ที่เดียวกัน** ใต้ sub-project ที่กำลังทำงาน:
```
ตัวอย่าง: ทำงานที่  Projects/Viriyah/26-VFIN-New-ERP/
ที่เก็บ temp  =  Projects/Viriyah/26-VFIN-New-ERP/20-Output/_temp/
```
- ใช้ `_temp/` ใต้ `20-Output` (ไม่วางไฟล์ temp ลอยใน `20-Output` ตรง ๆ) — กันปนกับไฟล์ส่งมอบจริง
  ที่อาจอยู่ใน `20-Output` เดียวกัน · แยกชนิดได้ด้วยโฟลเดอร์ย่อย เช่น `_temp/qa/` (หลักฐานตรวจของอริส)
- sub-project ไม่มีโฟลเดอร์ `20-Output` → สร้างได้เลย (`20-Output/_temp/`)
- งานที่ไม่ผูกโปรเจกต์ใด ๆ → session scratchpad ที่ระบบให้มา (`/private/tmp/claude-…/scratchpad`)

**② ไฟล์ output จริง = ตำแหน่งที่ user/spec ระบุเท่านั้น — ไม่แน่ใจ = ถามก่อนทำงานต่อ**
deliverable จริง (ไฟล์ V##R## ที่จะส่ง/ใช้จริง) ไปที่ตำแหน่งที่ถูกสั่งไว้เท่านั้น
· ไม่มีคำสั่งชัดเจนว่าเก็บที่ไหน = **หยุดถาม user ก่อนทำงานต่อ** ห้ามเดา ห้ามเลือกเอง

**③ 🔴 ห้ามสร้างไฟล์/โฟลเดอร์นอกโปรเจกต์เด็ดขาด**
โดยเฉพาะใต้ `~/Documents` และ `~/Documents/Claude` (root) — เคสจริง 2026.08.05:
`~/Documents/_qa_aris_vfin/` (11 MB) + `qa_s6_*.pptx` กระจายใต้ ~/Documents · **user เจอ ไม่ใช่ระบบ**

## กฎประกอบ

- **spec / build script รายโปรเจกต์** = เอกสารประกอบงานที่ต้องตรวจย้อนได้ (อ้างใน QA-log)
  → เก็บที่ `_build/` ข้าง artifact ตามธรรมเนียม DOC-PIPELINE เดิม — ไม่ใช่ temp ไม่ต้องย้าย
- **PowerPoint AppleScript** (sandbox เขียน /private/tmp ไม่ได้) → staging `~/Documents/.ice-staging/`
  แล้ว**ย้ายเข้า `20-Output/_temp/` ทันทีในคำสั่งเดียวกัน** (`osascript … && mv …`) — ห้ามทิ้งค้าง
- **จบงานเก็บกวาด:** หลักฐาน QA ที่อ้างใน QA-log เก็บไว้ใน `_temp/qa/` ได้ · ไฟล์ทดลองอื่นลบ
  · ก่อนปิด DELIVERY REPORT ให้ `ls` ยืนยันว่าไม่มีไฟล์หลงนอก `_temp/` และนอกโปรเจกต์

## ที่มา

คำสั่ง user 2026.08.06 (2 รอบ): รอบแรกพบไฟล์ QA ของงาน VFIN กระจายใต้ ~/Documents —
สาเหตุราก: Renderer Ladder เดิมสั่ง "save ใต้ ~/Documents แล้วย้าย" (ทำครึ่งแรก ลืมครึ่งหลัง)
+ ทั้ง 8 agent ไม่มีกติกาที่เก็บไฟล์ temp เลย (0/8) · รอบสอง user ออกแบบเอง: ที่เก็บเดียวต่อ
sub-project = `20-Output/_temp/` · output จริงตามตำแหน่งที่ระบุ · ไม่แน่ใจ = ถามก่อนทำต่อ
· หลักการบ้านเดียว: กฎอยู่ไฟล์นี้ไฟล์เดียว — agent ถือ pointer ห้าม copy เนื้อไปแปะ
