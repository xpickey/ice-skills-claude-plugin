# Bridge Presets — handoff templates ต่อ use-case

แต่ละ preset = handoff template + agent ที่ผูก. Claude เลือก preset ตามงาน แล้วส่งให้ Codex ผ่าน `ask-codex.sh`.

| # | Preset | Claude ทำ | Codex (peer) ทำ | Fleet agent ที่ผูก |
|---|---|---|---|---|
| 1 | **Anti-AI cross-check** | ตรวจด้วย thesis-ai-det-col | ตรวจซ้ำ independent (ref 03) | ผู้ทรง, qa-master(D5), แจนนี่, กัปตัน |
| 2 | **Sales/academic deliverable** | ร่าง proposal/บทความ | review คุณภาพ/ช่องโหว่ | กัปตัน, ผู้ทรง, qa-master, แจนนี่ |
| 3 | **Code review** | เขียน/แก้โค้ด | หา bug/security/edge | กัปตัน, แจนนี่ |
| 4 | **Design/architecture debate** | เสนอ design | แย้ง/เสริม/trade-off | กัปตัน, ผู้ทรง, qa-master, แจนนี่, จารโป้ง |

> Preset 1 มี template เต็มที่ `references/03_antiAI_handoff.md`. Preset 2-4 ใช้ template ล่างนี้.

## Preset 2 — Sales/Academic Deliverable Review
```
TASK: review deliverable นี้ในฐานะ peer reviewer. โจทย์: หาช่องโหว่ที่ทำให้ลูกค้า/กรรมการไม่เชื่อ/ไม่ผ่าน
objective: <เป้าหมายเอกสาร เช่น proposal ERP / บทความ TCI>
review_focus: <logic / completeness / claim ที่ไม่มีหลักฐาน / โครงสร้าง / ภาษา>
next_request: ชี้จุดอ่อน เรียงตามความรุนแรง + เสนอวิธีแก้ 1 บรรทัด/จุด
context: <constraint เช่น TOR ข้อไหน, มาตรฐานวารสารอะไร>

deliverable:
<<<CONTENT>>>
```
ผูก: **กัปตัน** (sales proposal) / **ผู้ทรง** (academic) ส่งมาผ่าน Claude · **qa-master** ใช้เป็น D10 cross-check · **แจนนี่** หลัง build เสร็จ

## Preset 3 — Code Review (phud.me style)
```
TASK: review โค้ด/diff นี้ หา bug, security, edge case, ที่ Claude อาจมองข้าม
objective: <โค้ดทำอะไร>
review_focus: correctness / security / error-handling / performance / readability
next_request: ชี้ปัญหาเป็น file:line + severity + fix สั้น. ถ้าไม่มีปัญหา บอกชัด
context: <ภาษา/framework/constraint>

code:
<<<CODE or git diff>>>
```
ผูก: **กัปตัน** (technical proposal) / **แจนนี่** (build script/automation). sandbox read-only พอ; ให้ Codex แก้ไฟล์เอง = workspace-write (ถามผู้ใช้ก่อน)

## Preset 4 — Design / Architecture Debate
```
TASK: ถก design นี้กับฉัน (Claude). คุณคือ peer ที่ท้าทายสมมติฐาน
objective: <ปัญหาที่กำลังออกแบบ>
proposed: <design ที่ Claude เสนอ + เหตุผล>
next_request: แย้งจุดที่เปราะ / เสนอทางเลือก / ชี้ trade-off ที่ Claude มองข้าม. อย่าเห็นด้วยถ้าไม่จริง
context: <constraint, scale, ทีม, เวลา>
```
ผูก: **กัปตัน** (deal strategy) / **ผู้ทรง** (research design) / **จารโป้ง** (solution/fit-gap architecture) / **qa-master** (เกณฑ์คุณภาพ) / **แจนนี่** (build feasibility). turn-shape: PROPOSE→CRITIQUE→REFINE วนจน converge (LOOP CAP 5)

## Fleet binding pattern (high-stakes escalation)
agent **ไม่เรียก Codex ทุกครั้ง** — เรียกเมื่อ:
- งานสำคัญ/disputed + ผู้ใช้สั่ง หรือ Claude เสนอแล้วผู้ใช้ OK
- confidence ต่ำ / มีผลผูกพัน commercial-legal-academic
gatekeeper = กัปตัน/Kim/ผู้ทรง (ไม่ใช่ทุก L2 เรียกเอง = กัน recursion + token บาน)
