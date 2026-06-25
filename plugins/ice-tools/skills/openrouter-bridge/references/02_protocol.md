# Bridge Protocol — handoff, turn-taking, persona-review (openrouter-bridge)

## Roles
- **Claude** = หลัก/ออกแบบ + คุม loop
- **OpenRouter model (เลือกได้)** = peer reviewer / second-opinion / ผู้สวมบท

โครงเดียวกับ claude-codex-bridge — ต่างที่ stateless (helper เก็บ history) + เลือก model.

## Turn shape: PROPOSE → CRITIQUE → REFINE
1. **PROPOSE** (`--new --model X`) — เสนอ + handoff fields + เลือก model ตามงาน
2. **CRITIQUE** (model) — แย้ง/เสริม/หา concern
3. **REFINE** (`--resume`) — ปรับ + ถามต่อ (model เดิม จำ history) → วน
4. หยุด: converge หรือ LOOP CAP ~5 (history resend = token โต) → Claude สรุป + attribution (ระบุว่ามาจาก model ไหน)

## Handoff fields (ต่อ turn)
- **objective** — เป้าหมายรอบนี้
- **context** — บริบทครบ (model ไม่เห็นไฟล์ ต้อง dump ให้ครบใน prompt)
- **work_done** — Claude ทำ/ตัดสินใจอะไรแล้ว
- **next_request** — อยากให้ model ทำอะไร (สำคัญสุด)

## ⭐ Persona Review pattern (KTC use-case)
ให้ model **สวมบทผู้มีอำนาจตัดสินใจ** อ่าน deck/proposal หา concern แบบไม่ใจอ่อน — ดีกว่าให้คนในทีมที่อยากให้ดีลผ่านอ่านเอง.

**วิธี:**
1. dump context ครบ (deck text + บริบทดีล + ราคา) — model ไม่เห็นไฟล์
2. กำหนด persona ชัด + business style + จุดยืน:
   - **CFO** — เน้น value to business, ROI, จ่ายแพงต้องคุ้ม, type business style CFO
   - **CIO** — คนทำงานจริง รู้ว่าไม่ควรจ่ายแพงถ้าไม่มีเหตุผลพอ, technical buyer
   - **CTO/Procurement** — feasibility, risk, vendor lock-in
3. สั่ง: "อ่านแบบนักวิจารณ์ที่ไม่ใจอ่อน — ซื้อไหม? concern ตรงไหน? ไม่โอเคตรงไหน? ไม่ซื้อเพราะอะไร?"
4. **เลือก model ต่างต่อ persona** ได้ (CFO→model วิเคราะห์ธุรกิจเก่ง · CIO→model technical) — แต่ละ persona = `--new` thread แยก (fresh lens)
5. เอา concern กลับมา → ทีม (ท่านเทพ/อริส/แจนนี่) + Claude ช่วยตอบ + ปรับ deck

**ตัวอย่าง prompt skeleton:**
```
act as CFO ของ [บริษัท] — business style CFO เน้น value to business, จ่ายแพงต้องมีเหตุผล.
context ครบ: [deck text + ดีล + ราคา].
อ่านแล้วบอก: ซื้อไหม? concern ตรงไหน? ไม่ซื้อเพราะอะไร? อะไรยังไม่ convince?
ตอบแบบ CFO จริง ไม่ใจอ่อน.
```

## Transcript (audit)
helper append ทุก turn ลง `$BRIDGE_DIR/transcript.md` (role + model + timestamp + content) — ตรวจย้อน/สรุปได้

## ส่ง context ใหญ่ (deck/doc)
model ไม่เห็นไฟล์ → dump text เข้า prompt. deck ยาว → ใส่ใน prompt ตรง ๆ (helper รับ prompt เป็น arg เดียว — ใช้ heredoc/ไฟล์ใน Bash ฝั่ง Claude แล้วส่ง). cost: prompt ใหญ่ + history resend = แพง → persona review มัก 1-2 turn/persona พอ
