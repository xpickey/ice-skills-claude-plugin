# Anti-AI Wording Cross-Check — Handoff Template (Preset 1)

ส่ง template นี้ให้ Codex ผ่าน `ask-codex.sh --new` เพื่อให้ Codex ตรวจภาษา AI **แบบ independent** (Claude ตรวจด้วย `thesis-ai-det-col` patterns เอง → Codex ตรวจซ้ำด้วย template นี้ → รวมผล 2 model). patterns สรุปจาก `thesis-ai-det-col` skill (corpus-grounded).

## วิธีใช้ (Claude)
1. Claude ตรวจ text ด้วย `thesis-ai-det-col` ก่อน (Skill tool) → ได้ findings ชุด A
2. `ask-codex.sh --new "<TEMPLATE ข้างล่าง + text>"` → Codex ได้ findings ชุด B
3. **รวมผล:** จุดที่ทั้งคู่เจอ = confident · จุดที่เจอฝ่ายเดียว = ตรวจซ้ำ (อาจ false-positive หรือ pattern ที่อีกฝ่ายพลาด)
4. สรุปให้ผู้ใช้ ระบุว่าอะไรมาจาก Claude/Codex/ทั้งคู่

## HANDOFF TEMPLATE (copy ส่ง Codex)

```
TASK: ตรวจข้อความไทย/อังกฤษนี้ว่ามีกลิ่น AI เขียนไหม ตาม checklist ข้างล่าง รายงานเป็น list สั้น

STEP 1 — ระบุ register: Academic / Business / General

STEP 2 — CORE checks (ทุก register):
- Burstiness: ประโยคยาวเท่ากันหมด (16-22 คำ ติดกัน 3+ ประโยค ไม่มีประโยคสั้น 5-12 คำคั่น) → flag
- Opening: ทุกประโยค/ย่อหน้าขึ้นต้นแบบเดียว (โครงเดิมซ้ำใน 5 ประโยค) → flag
- Nested clause: ซึ่ง/ที่/อัน ซ้อนเกิน 2 ชั้น → flag
- Transition: นอกจากนี้/Furthermore/Moreover เกิน 3 ครั้ง/500 คำ → flag
- Section-closing: ปิดหัวข้อแบบพิธีกรรมซ้ำ "ดังจะกล่าวในหัวข้อถัดไป" → flag
- Personal voice: ไร้ชื่อ/วันที่/ตัวเลขเฉพาะ (เลขกลม ๆ ตลอด) → flag

STEP 3 — ถ้า Academic: Class A (เจอครั้งเดียว = fail): "เป็นที่ทราบกันดีว่า"/"สังเคราะห์ได้ว่า"/"อย่างก้าวกระโดด"/"ยิ่งไปกว่านั้น". + citation cluster ≥4 ติดกัน. + reporting-verb overclaim (งานทัศนะ+"พบว่า" / สำรวจ+"พิสูจน์ว่า" โดยไม่ทดสอบสมมติฐาน)

STEP 4 — ถ้า Business: 
- Watchlist (flag เฉพาะลอย ไม่มี anchor): synergy/seamless/robust/เพิ่มประสิทธิภาพ/ครบวงจร/ไร้รอยต่อ
- Calque/ลิเก (แก้เป็น fact หรือตัด): "ส่งมอบคุณค่า"→ระบุผลลัพธ์ · "ใช้ประโยชน์จากความเชี่ยวชาญ"→ระบุประสบการณ์ · "ความลึกของทีม"→ระบุ cert/ปี
- Orphan data: ตัวเลข/metric ต้องมีที่มาตอนกล่าวครั้งแรก (ไม่งั้น flag ว่าลอย)
- Boilerplate opener: "เอกสารนี้นำเสนอ..." → flag

STEP 5 — ถ้าไทย (ทุก register):
- Translationese: "การ"+กริยา เกิน 2/ประโยค · passive ไทย · "ความ"+คุณศัพท์ ซ้อน → flag
- Particle leak: ครับ/ค่ะ/คะ/นะ ท้ายประโยคทางการ → flag (แต่ไม่ใช่หางคำประสม เช่น ครอบครัว/พรรณนา/เลขา)

GUARD (ห้าม flag — คนใช้จริง):
- ขับเคลื่อน / ยกระดับ / บูรณาการ / นอกจากนี้(≤3/500w) / อย่างมีประสิทธิภาพ = OK
- ลิเก OK ถ้าผูก fact: "ส่งมอบ[ผลลัพธ์เจาะจง]" ผ่าน, "ส่งมอบคุณค่า" (ลอย) ไม่ผ่าน
- end-to-end/ครบวงจร OK ถ้าผูก noun+ขอบเขต
- ห้ามแปลงศัพท์ไทยที่วงการใช้จริง (กระทบยอด, ศัพท์ราชการบัญญัติ) เป็นทับศัพท์

OUTPUT:
- register: [Academic/Business/General]
- findings: [มิติ | ตำแหน่ง/คำ | ทำไมเป็น AI-tell | ฉบับแก้]
- severity: [🔴 fail ทันที / 🟠 หลายจุด / 🟡 จุดเดียว]
- AI likelihood: [%]

ข้อความที่ต้องตรวจ:
<<<TEXT>>>
```

## หมายเหตุ
- template นี้ "บีบ" จาก 292K-word corpus — Codex จึงพูดภาษาเดียวกับ skill (register-aware, anchor-driven, มี guard กัน false-positive)
- patterns ที่ Codex มักพลาด (calque C1-C12, transliteration TL1-3, particle boundary): skill เก็บละเอียดกว่า → ใช้ Claude เป็นหลักตรงนี้, Codex เสริม surface-level (ลิเก/buzzword/burstiness)
- source: `thesis-ai-det-col` references 01/05a/06/11 + Wording Discipline W1-W7
