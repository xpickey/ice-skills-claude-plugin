# Bridge Presets — openrouter-bridge (5 presets)

แต่ละ preset = handoff template + model แนะนำ. Claude เลือก preset + model ตามงาน.

| # | Preset | Claude ทำ | OpenRouter (peer) ทำ | model แนะนำ |
|---|---|---|---|---|
| 1 | **Anti-AI cross-check** | ตรวจด้วย thesis-ai-det-col | ตรวจซ้ำ independent | sonnet / r1 |
| 2 | **Deliverable review** | ร่าง proposal/บทความ | หาช่องโหว่/จุดไม่เชื่อ | sonnet / gpt |
| 3 | **Code review** | เขียน/แก้โค้ด | หา bug/security/edge | r1 / gpt |
| 4 | **Design/architecture debate** | เสนอ design | แย้ง/trade-off | r1 / opus |
| 5 ⭐ | **Persona review (KTC)** | dump deck+context | สวมบท CFO/CIO หา concern | เลือกต่อ persona |

> presets 1-4 = model-agnostic (reuse แนวจาก claude-codex-bridge). preset 5 = เด่นของ OpenRouter (เลือก model ต่อ persona).

## Preset 1 — Anti-AI cross-check
```
TASK: ตรวจข้อความไทย/อังกฤษว่ามีกลิ่น AI เขียนไหม (ลิเก/calque/anchor หาย/burstiness/particle)
รายงาน: register · findings [มิติ|ตำแหน่ง|ทำไม|แก้] · severity · AI likelihood %
GUARD: ห้าม flag ศัพท์วิชาชีพไทยที่ใช้จริง (กระทบยอด/บัญชีแยกประเภท)
ข้อความ: <<<TEXT>>>
```
> รวมผล: Claude(thesis-ai-det-col) + OpenRouter → จุดที่ทั้งคู่เจอ=confident · ฝ่ายเดียว=ตรวจซ้ำ

## Preset 2 — Deliverable Review
```
TASK: review deliverable ในฐานะ peer reviewer — หาช่องโหว่ที่ลูกค้า/กรรมการไม่เชื่อ/ไม่ผ่าน
objective: <เป้าหมายเอกสาร> · review_focus: <logic/completeness/claim ไม่มีหลักฐาน/ภาษา>
next_request: ชี้จุดอ่อนเรียงความรุนแรง + แก้ 1 บรรทัด/จุด
deliverable: <<<CONTENT>>>
```

## Preset 3 — Code Review
```
TASK: review โค้ด/diff หา bug, security, edge case
review_focus: correctness/security/error-handling/performance
next_request: file:line + severity + fix สั้น · ไม่มีปัญหา = บอกชัด
code: <<<CODE>>>
```

## Preset 4 — Design / Architecture Debate
```
TASK: ถก design — คุณคือ peer ที่ท้าทายสมมติฐาน
proposed: <design + เหตุผล> · next_request: แย้งจุดเปราะ/ทางเลือก/trade-off ที่มองข้าม
อย่าเห็นด้วยถ้าไม่จริง
```

## Preset 5 ⭐ — Persona Review (KTC CFO/CIO)
ดูเต็มที่ `references/02_protocol.md` §Persona Review. สรุป:
- 1 persona = 1 `--new` thread (fresh lens) · เลือก model ต่อ persona
- CFO (value to business, จ่ายแพงต้องคุ้ม) · CIO (technical, ไม่จ่ายแพงถ้าไม่มีเหตุผล) · CTO/Procurement (risk/lock-in)
- dump context ครบ (model ไม่เห็นไฟล์) · สั่งอ่านแบบไม่ใจอ่อน: ซื้อไหม? concern? ไม่ซื้อเพราะ?
- เอา concern กลับ → ทีม (ท่านเทพ/อริส/แจนนี่) + Claude ตอบ + ปรับ deck
```
act as [CFO|CIO] ของ [บริษัท] — business style ตาม persona, จุดยืนไม่ใจอ่อน.
context ครบ: <<<deck text + ดีล + ราคา>>>
บอก: ซื้อไหม? concern ตรงไหน? ไม่ซื้อเพราะอะไร? อะไรยังไม่ convince?
```
