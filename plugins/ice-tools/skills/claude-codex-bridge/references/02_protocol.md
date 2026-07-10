# Bridge Protocol — handoff, turn-taking, transcript

## Roles
- **Claude** = หลัก/ออกแบบ + **คุม loop** (ตัดสินใจว่าจะถกต่อ/จบ)
- **Codex (gpt-5.5)** = peer reviewer / ผู้ช่วยเขียน / second opinion

ต่างจาก phud.me agent-bridge (auto-loop ผ่าน fswatch + 2 terminal) — ที่นี่ Claude เรียก `codex exec` ผ่าน Bash ตรง ๆ จึง **ไม่ต้อง fswatch** เหลือแค่ helper เดียว. handoff/feedback กลายเป็น transcript log (audit) แทน IPC channel.

## Turn shape: PROPOSE → CRITIQUE → REFINE
1. **PROPOSE** (Claude `--new`) — เสนอ design/โค้ด/คำถาม พร้อม handoff fields
2. **CRITIQUE** (Codex) — แย้ง/เสริม/ชี้ช่องโหว่
3. **REFINE** (Claude `--resume`) — ปรับตาม feedback + ถามต่อ → วน
4. หยุดเมื่อ converge หรือถึง LOOP CAP (~5 turn) → Claude สรุปให้ผู้ใช้

## Handoff fields (ใส่ใน prompt แต่ละ turn)
Codex เสนอเอง 4 field นี้ตอน prototype (ใช้เป็นโครง):
- **objective** — เป้าหมายรอบนี้ / นิยาม "เสร็จ"
- **context_delta** — อะไรเปลี่ยนจากรอบก่อน
- **work_done** — Claude ทำ/ตัดสินใจอะไรไปแล้ว
- **next_request** — อยากให้ Codex ทำอะไรต่อ (**สำคัญสุด** — กัน Codex เดาเอง)

ไม่ต้องใส่ครบทุก field ทุก turn — turn แรกควรครบ, turn ต่อ ๆ ไป resume จำ context ให้แล้ว เน้น `next_request`.

## Transcript (audit)
helper append ทุก turn ลง `$BRIDGE_DIR/transcript.md`:
```
### CLAUDE → CODEX  (timestamp)  [--new|--resume]
<prompt ที่ Claude ส่ง>

### CODEX → CLAUDE  (timestamp)  [session <id>]
<คำตอบ Codex>
---
```
ใช้ตรวจย้อนบทสนทนา / debug / สรุปให้ผู้ใช้ได้

## ตัวอย่าง session จริง (prototype 2026.06.22)
3-turn ถก "handoff message ควรมี field อะไร":
- **T1** (Claude --new): ถามโจทย์ → Codex เสนอ 4 field (objective/context_delta/work_done/next_request)
- **T2** (Claude --resume): "เลือก field สำคัญสุด" → Codex ตอบ `next_request` + เหตุผล (**อ้างชื่อ field เดิม = จำได้**)
- **T3** (Claude --resume): "สรุป 1 ประโยค" → Codex สรุปครบทั้ง 4 field (**จำทั้ง thread**)
- session id เดียวตลอด, input_tokens โต 24k→47k (context สะสม)

## ⭐ REVIEW turn shape (Mode B/D/E — เพิ่ม V02R01 · ใช้คู่ ref 05 Review Contract)

เมื่อ turn เป็น "การตรวจงาน" (ไม่ใช่ถกไอเดีย) — รูปทรงรอบเปลี่ยนเป็น:
1. **SUBMIT** (Claude `--new` + `--schema references/verdict.schema.json`) — ส่งของครบตาม ref 05 §7: ตัวงานเต็ม + เกณฑ์ + scope/รอบ
2. **VERDICT** (Codex) — JSON ตาม schema: issues (Files/Impact/Minimal fix) + `counts` + `context_repairs`
3. **FIX** (Claude แก้ตามจริง — เปิดไฟล์แก้ ไม่ใช่แค่รับปาก)
4. **RE-VERDICT** (Claude `--resume` + `--schema`) — แนบรายการ issue รอบก่อน → Codex ต้องตอบ fixed_verified/still_present ครบ
5. จบเมื่อ **counts ผ่านเกณฑ์** (critical=0 & high≤2 default) · **หยุดเมื่อ critical ไม่ลด 2 รอบติด** (stagnation — ref 05 §4) · เพดาน ~5 turns
- OpenRouter ไม่มี --output-schema → ใช้ format markdown + trailer `<!-- counts: ... -->` + บันไดสำรอง ref 05 §9

## ⭐ Shard pattern (Mode D — งานใหญ่ ตรวจขนานหลายมุม)

```bash
S=~/.claude/skills/claude-codex-bridge
"$S/scripts/ask-codex.sh" --session shard-fact  --schema "$S/references/verdict.schema.json" --new "ตรวจเฉพาะมุมข้อเท็จจริง/ตัวเลข: <งาน+เกณฑ์>"
"$S/scripts/ask-codex.sh" --session shard-risk  --schema "$S/references/verdict.schema.json" --new "ตรวจเฉพาะมุมความเสี่ยง/compliance: <งาน+เกณฑ์>"
"$S/scripts/ask-codex.sh" --session shard-compl --schema "$S/references/verdict.schema.json" --new "ตรวจเฉพาะความครบถ้วนเทียบ requirement: <งาน+เกณฑ์>"
```
→ Claude รวมผล: ตัดซ้ำ (เรื่องเดียวกันเก็บ severity สูงกว่า) → counts รวม → ตัดสินตามเกณฑ์เดียว · แต่ละ shard resume ต่อได้อิสระ

## ส่งโค้ดให้ Codex review (pattern)
ใส่โค้ด/diff ใน prompt ตรง ๆ (helper รับ prompt เป็น arg). ถ้าโค้ดยาว:
```bash
ask-codex.sh --new "review โค้ดนี้ objective=หาบั๊ก next_request=ชี้ file:line ที่ผิด:
$(cat path/to/file)"
```
หรือถ้าต้องให้ Codex **อ่าน/แก้ไฟล์เอง** → ต้อง `BRIDGE_SANDBOX=workspace-write` + `-C <repo>` (ถามผู้ใช้ก่อน).
