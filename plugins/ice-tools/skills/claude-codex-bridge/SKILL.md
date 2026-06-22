---
name: claude-codex-bridge
description: "Use when the user wants Claude to consult, debate, or pair with OpenAI Codex (gpt-5.5) on a problem — design discussion, code review, second opinion, or hand-off-to-write-then-review. Claude drives a manual turn-by-turn conversation by calling the local Codex CLI via a helper script; Codex keeps its own session memory across turns (codex exec resume), so it remembers the thread. Triggers on ถาม Codex, ปรึกษา Codex, ให้ Codex review, ถก solution กับ Codex, คุยกับ Codex, second opinion, Codex bridge, agent bridge, ส่งให้ Codex เขียน. NOT for one-shot questions to Codex with no follow-up (just call codex exec directly), and NOT a Codex MCP server."
trigger: /codex-bridge
---

# Claude ↔ Codex Bridge

**Version: V01R02 | 2026.06.22** — manual-turn conversation bridge. Claude (this agent) talks to OpenAI **Codex gpt-5.5** through the local `codex` CLI, one turn at a time, with Claude driving the loop and deciding when to continue or stop. Codex keeps its own session memory across turns via `codex exec resume`, so it remembers the thread (verified end-to-end). **V01R02 เพิ่ม 4 presets** (anti-AI cross-check / deliverable review / code review / design debate) + fleet binding.

> ทักษะนี้ทำให้ Claude "ปรึกษา/ถก/จับคู่งาน" กับ Codex ได้จริง — Claude เป็นหลัก/ออกแบบ, Codex เป็น peer reviewer / ผู้ช่วยเขียน. ต่างจาก MCP ตรงที่ Codex **จำบทสนทนาของตัวเอง** ข้าม turn ได้.

## When to use
- ผู้ใช้อยากได้ **second opinion** จาก Codex ต่อ design / โค้ด / แนวทาง
- **ถก solution** ไปกลับหลายรอบ (Claude เสนอ → Codex แย้ง/เสริม → Claude ปรับ)
- **ส่งงานให้ Codex ช่วยเขียน** แล้วเอากลับมา review ต่อ
- ต้องการให้ Codex **จำ context** ของรอบก่อน (ไม่ใช่ถามครั้งเดียวจบ)

**ไม่ใช้เมื่อ:** ถาม Codex ครั้งเดียวไม่ต่อ (เรียก `codex exec "..."` ตรง ๆ พอ) · งานที่ Claude ทำเองได้เร็วกว่า · ต้องการ Codex เป็น MCP tool (คนละ pattern)

## Prerequisite (เช็กครั้งเดียว)
- `codex login status` ต้องขึ้น **"Logged in using ChatGPT"** (OAuth — ไม่ใช่ API key)
- `codex --version` ≥ 0.137.0
- ถ้ายังไม่ login → บอกผู้ใช้รัน `codex login` ใน terminal (เปิด browser authorize) — assistant ทำแทนไม่ได้

## How Claude drives the loop (manual turn)

Helper: `scripts/ask-codex.sh` (อยู่ใน skill นี้). Claude เรียกผ่าน Bash:

```bash
SKILL=~/.claude/skills/claude-codex-bridge
# turn แรก — เริ่ม thread ใหม่
"$SKILL/scripts/ask-codex.sh" --new "<prompt รอบแรก>"
# turn ถัดไป — Codex จำ context (resume session เดิม)
"$SKILL/scripts/ask-codex.sh" --resume "<prompt รอบถัดไป>"
```

ผลลัพธ์ = คำตอบสะอาดของ Codex (ไม่มี banner/error/token) พิมพ์ออก stdout + เก็บ transcript audit ไว้ที่ `$BRIDGE_DIR/transcript.md` (ดู references/02).

**Loop ที่ Claude ทำเอง:**
1. `--new` ส่งโจทย์ + handoff fields (ดู protocol ล่าง)
2. อ่านคำตอบ Codex → ตัดสินใจ: เห็นด้วย/แย้ง/ขอให้ขยาย
3. `--resume` ส่ง turn ถัดไป (Codex จำรอบก่อน)
4. วนจนได้ข้อสรุป → สรุปให้ผู้ใช้ (อ้างว่าอันไหนมาจาก Codex)
5. **LOOP CAP:** ถ้าเกิน ~5 turn ยังไม่ converge → หยุด ถามผู้ใช้ก่อนไปต่อ (กัน token บาน)

## Handoff message protocol (แต่ละ turn ควรมี)
Codex เองแนะนำ 4 field นี้ (ตอน prototype) — ใช้เป็นโครง prompt แต่ละรอบ:
- **objective** — เป้าหมายรอบนี้ / นิยาม "เสร็จ"
- **context_delta** — อะไรเปลี่ยนจากรอบก่อน (resume จำได้อยู่แล้ว แต่ย้ำจุดสำคัญ)
- **work_done** — Claude ทำ/ตัดสินใจอะไรไปแล้ว
- **next_request** — อยากให้ Codex ทำอะไรต่อ (field สำคัญสุด — กัน loop เดาเอง)

turn-shape ที่แนะนำ: **PROPOSE** (Claude เสนอ) → **CRITIQUE** (Codex แย้ง/เสริม) → **REFINE** (Claude ปรับ + ถามต่อ).

## Sandbox & safety
- default ของ helper = `-s read-only` (Codex อ่านได้ ไม่แก้ไฟล์) — ปลอดภัยสำหรับ "ถก/review"
- ถ้าจะ **ให้ Codex แก้ไฟล์จริง** ต้องเปลี่ยนเป็น `workspace-write` — **ถามผู้ใช้ยืนยันก่อน** (ดู references/01 §sandbox)
- helper ไม่ push git / ไม่ deploy — เป็นแค่ตัวคุย

## Presets (เลือกตาม use-case)
| # | Preset | เมื่อไร | template |
|---|---|---|---|
| 1 ⭐ | **Anti-AI cross-check** | ตรวจภาษา AI ไทย/อังกฤษ (ไม่ลิเก/ไม่ calque/ไม่อธิบายยาว) — Claude ตรวจด้วย `thesis-ai-det-col` → Codex ตรวจซ้ำ independent → รวม 2 model | ref 03 (เต็ม) |
| 2 | **Sales/academic deliverable** | review proposal/บทความ/deliverable ก่อนส่ง | ref 04 |
| 3 | **Code review** | Claude เขียน → Codex หา bug/security | ref 04 |
| 4 | **Design/architecture debate** | ถก design ไปกลับ | ref 04 |

**Fleet binding (high-stakes escalation, optional):** กัปตัน/ผู้ทรง/qa-master/แจนนี่/จารโป้ง เรียก Codex cross-check ได้ **เฉพาะงานสำคัญ/disputed + ผู้ใช้สั่งหรือ Claude เสนอแล้วผู้ใช้ OK** — ไม่ auto ทุกครั้ง (กัน token บาน). gatekeeper = กัปตัน/Kim/ผู้ทรง.

## References
- `references/01_codex_cli_reference.md` — flag/output/quirk ของ `codex exec` ที่พิสูจน์แล้ว (รวม gotcha: `-a` ไม่มี, resume รับ flag น้อยกว่า exec)
- `references/02_protocol.md` — รูปแบบ handoff/transcript + turn-taking + ตัวอย่าง session จริง
- `references/03_antiAI_handoff.md` — Preset 1 template เต็ม (anti-AI patterns จาก thesis-ai-det-col + GUARD กัน false-positive)
- `references/04_presets.md` — Preset 2-4 templates + fleet binding pattern

## CHANGELOG
- **V01R02 (2026.06.22)** — +4 presets (ref 03 anti-AI cross-check เต็ม จาก thesis-ai-det-col patterns + GUARD · ref 04 deliverable/code/design templates) + fleet binding pattern (high-stakes escalation, gatekeeper-gated). Anti-AI use-case validated จริง: Codex ตรวจภาษา AI ไทยได้ + เสริมกับ skill (ไม่ซ้ำ).
- **V01R01 (2026.06.22)** — initial. manual-turn bridge: helper `ask-codex.sh` (--new/--resume), session continuity via `codex exec resume`, clean output via `--output-last-message`, transcript audit log. Prototype verified 3-turn conversation with Codex memory intact. Corpus-correct flags (no `-a`; resume ≠ exec flag set) documented in ref 01.
