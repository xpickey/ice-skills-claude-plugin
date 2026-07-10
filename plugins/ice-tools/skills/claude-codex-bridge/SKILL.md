---
name: claude-codex-bridge
description: "Use when the user wants Claude to consult, debate, or pair with OpenAI Codex (gpt-5.5) on a problem — design discussion, code review, second opinion, or hand-off-to-write-then-review. Claude drives a manual turn-by-turn conversation by calling the local Codex CLI via a helper script; Codex keeps its own session memory across turns (codex exec resume), so it remembers the thread. Triggers on ถาม Codex, ปรึกษา Codex, ให้ Codex review, ถก solution กับ Codex, คุยกับ Codex, second opinion, Codex bridge, agent bridge, ส่งให้ Codex เขียน. NOT for one-shot questions to Codex with no follow-up (just call codex exec directly), and NOT a Codex MCP server."
trigger: /codex-bridge
---

# Claude ↔ Codex Bridge

**Version: V02R02 | 2026.07.10** — manual-turn conversation bridge. Claude talks to OpenAI **Codex** (default model จาก `~/.codex/config.toml` — ปัจจุบัน **gpt-5.6-terra** · สลับต่อ call ได้ด้วย `--model`) through the local `codex` CLI, one turn at a time, with Claude driving the loop. Codex keeps its own session memory across turns via `codex exec resume` (verified end-to-end).
**V02R02 เพิ่ม:** ⭐ `--model` passthrough (สลับ 5.5 ↔ terra ↔ luna ต่องานโดยไม่แก้ config — feature-detected · ทดสอบจริงครบ 3 model + resume memory บน CLI 0.144.1) · re-probe 0.144.1: `--output-schema` ยังอยู่ทั้ง exec/resume · resume ยังไม่รับ -s/-C ตามเดิม
**V02R01:** Modes A-E · Review Contract (ref 05 + `verdict.schema.json`) · multi-session (`--session`) · Authorization Matrix + `codex_scope` · Degradation Ladder. **V01R02:** 4 presets + fleet binding.

> ทักษะนี้ทำให้ Claude "ปรึกษา/ถก/ตรวจ/จับคู่งาน" กับ Codex ได้จริง — Claude เป็นหลัก/ออกแบบ, Codex เป็น peer reviewer / second detector / ผู้ช่วยเขียน. ต่างจาก MCP ตรงที่ Codex **จำบทสนทนาของตัวเอง** ข้าม turn ได้.

## Modes A-E (แคตตาล็อก — agent เสนอ mode ที่เหมาะได้ หรือ user ระบุเอง)

| Mode | ชื่อ | เมื่อไร | กติกา |
|---|---|---|---|
| **A** | Consult/Debate | ถกไอเดีย/design หลายรอบ | protocol เดิม (PROPOSE→CRITIQUE→REFINE · ref 02) — เบา ไม่แบก contract |
| **B** | Review Contract | ตรวจงานจริงจัง (deliverable/โค้ด/เอกสาร) | **ref 05 บังคับ**: counts + convergence + `--schema references/verdict.schema.json` |
| **C** | Co-writer | ให้ Codex เขียน/แก้ไฟล์จริง แล้ว Claude ตรวจ | ต้อง `BRIDGE_SANDBOX=workspace-write` → **ถาม user ก่อนเสมอ** |
| **D** | Shard Review | งานใหญ่ ตรวจขนาน 2-3 มุม (fact/risk/completeness) | `--session shard-*` แยกวง → รวมผลตัดซ้ำเก็บ severity สูง (ref 02 §Shard) |
| **E** | Second Detector | ตรวจซ้ำอิสระ (anti-AI/QA) | Preset 1 (ref 03) + ผลต้อง map เข้า format ของผู้เรียก (เช่น detected_issues ของ qa-master) |

## When to use
- ผู้ใช้อยากได้ **second opinion** จาก Codex ต่อ design / โค้ด / แนวทาง (Mode A)
- **ตรวจงานแบบวัดผลได้** ก่อนส่งจริง (Mode B/D) — จบด้วยตัวเลข ไม่ใช่ความรู้สึก
- **ถก solution** ไปกลับหลายรอบ (Claude เสนอ → Codex แย้ง → Claude ปรับ)
- **ส่งงานให้ Codex ช่วยเขียน** แล้วเอากลับมา review ต่อ (Mode C — ยืนยันก่อน)
- ต้องการให้ Codex **จำ context** ของรอบก่อน (ไม่ใช่ถามครั้งเดียวจบ)

**ไม่ใช้เมื่อ:** ถาม Codex ครั้งเดียวไม่ต่อ (เรียก `codex exec "..."` ตรง ๆ พอ) · งานที่ Claude ทำเองได้เร็วกว่า · ต้องการ Codex เป็น MCP tool (คนละ pattern)

## Prerequisite (เช็กครั้งเดียว)
- `codex login status` ต้องขึ้น **"Logged in using ChatGPT"** (OAuth — ไม่ใช่ API key)
- `codex --version` ≥ 0.137.0 (probe ล่าสุด 2026.07.10 — ดู ref 01 §Probe)
- ยังไม่ login → บอกผู้ใช้รัน `codex login` ใน terminal — assistant ทำแทนไม่ได้ → ระหว่างนั้นใช้ **Degradation Ladder** (ล่าง)

## How Claude drives the loop (manual turn)

Helper: `scripts/ask-codex.sh` (V02R01). Claude เรียกผ่าน Bash:

```bash
SKILL=~/.claude/skills/claude-codex-bridge
# วงเดียวแบบเดิม (back-compat V01)
"$SKILL/scripts/ask-codex.sh" --new "<prompt รอบแรก>"
"$SKILL/scripts/ask-codex.sh" --resume "<prompt รอบถัดไป>"       # Codex จำ thread
# ⭐ หลายวง (ต่อ opportunity / ต่อสายตรวจ)
"$SKILL/scripts/ask-codex.sh" --session tqr-deal --new "..."
"$SKILL/scripts/ask-codex.sh" --session tqr-deal --resume "..."
"$SKILL/scripts/ask-codex.sh" --list-sessions
# ⭐ Review Mode (Mode B/D/E) — บังคับ verdict JSON ด้วยกลไก
"$SKILL/scripts/ask-codex.sh" --session review-x --schema "$SKILL/references/verdict.schema.json" --new "<submit ตาม ref 05 §7>"
# ⭐ สลับ model ต่องาน (V02R02) — ไม่แก้ config · default = config.toml (ตอนนี้ gpt-5.6-terra)
"$SKILL/scripts/ask-codex.sh" --session x --model gpt-5.6-luna --new "..."   # หรือ gpt-5.5 / gpt-5.4-mini
```

ผลลัพธ์ = คำตอบสะอาดของ Codex บน stdout + transcript audit ที่ `$BRIDGE_DIR[/sessions/<name>]/transcript.md` · `--new` ทับวงเดิม → helper เตือน + เก็บ id เก่าไว้ `.prev`

**Loop ที่ Claude ทำเอง (Mode A):**
1. `--new` ส่งโจทย์ + handoff fields (ref 02)
2. อ่านคำตอบ → ตัดสินใจ: เห็นด้วย/แย้ง/ขอขยาย
3. `--resume` turn ถัดไป → วนจนได้ข้อสรุป → สรุปให้ผู้ใช้ + attribution
4. **LOOP CAP ~5 turn** → เกินแล้วไม่ converge → หยุด ถามผู้ใช้

**Loop แบบตรวจงาน (Mode B/D/E):** ใช้ REVIEW turn shape ใน ref 02 + กติกาเต็มใน **ref 05**:
- ทุก verdict จบด้วย counts · **ผ่าน = critical=0 & high≤2** (default — งาน final เข้มขึ้นได้)
- **หยุดเมื่อ critical ไม่ลด 2 รอบติด** (stagnation — เลขเดียวกับ Circuit Breaker ของ fleet)
- "แก้แล้ว" ต้อง verify กับไฟล์จริงก่อนนับ FIXED · ของเข้าไม่ครบ → Codex ตอบ REVIEW_BLOCKED
- `ACCEPTED_RISK` = **user อนุมัติได้คนเดียว** — AI ห้ามยอมรับความเสี่ยงแทน

## Handoff message protocol (แต่ละ turn ควรมี)
4 fields (ref 02): **objective** (เป้าหมาย/นิยามเสร็จ) · **context_delta** (อะไรเปลี่ยน) · **work_done** · **next_request** (สำคัญสุด — กัน Codex เดาเอง)
turn-shape: **PROPOSE → CRITIQUE → REFINE** (Mode A) · **SUBMIT → VERDICT → FIX → RE-VERDICT** (Mode B — ref 02)

## Sandbox & safety
- default = `-s read-only` (Codex อ่านได้ ไม่แก้ไฟล์) — ปลอดภัยสำหรับถก/ตรวจ
- **ให้ Codex แก้ไฟล์จริง** (Mode C) = `BRIDGE_SANDBOX=workspace-write` → **ถามผู้ใช้ยืนยันก่อน**
- helper ไม่ push git / ไม่ deploy — เป็นแค่ตัวคุย

## ⭐ Degradation Ladder (Codex ใช้ไม่ได้ — ไม่จบแค่ "ไปรัน codex login")
```
Codex CLI ไม่พร้อม → (1) เสนอ OpenRouter (skill openrouter-bridge — ต้องมี OPENROUTER_API_KEY · จ่ายตาม model)
                   → (2) ผู้ตรวจ model เดียวกันตาม contract เดิม + แจ้งตรง ๆ ว่าคุณภาพต่ำกว่า cross-model
ทุกชั้นระบุใน attribution ว่าใช้ชั้นไหน (ref 05 §10)
```

## Presets (เลือกตาม use-case — ใช้ได้ทุก Mode ที่ตรง)
| # | Preset | เมื่อไร | template |
|---|---|---|---|
| 1 ⭐ | **Anti-AI cross-check** | ตรวจภาษา AI ไทย/อังกฤษ — Claude ตรวจด้วย `thesis-ai-det-col` → Codex ตรวจซ้ำ independent → รวม 2 model (Mode E) | ref 03 (เต็ม) |
| 2 | **Sales/academic deliverable** | review proposal/บทความก่อนส่ง (Mode B) | ref 04 |
| 3 | **Code review** | Claude เขียน → Codex หา bug/security (Mode B) | ref 04 |
| 4 | **Design/architecture debate** | ถก design ไปกลับ (Mode A) | ref 04 |

## ⭐ Authorization Matrix (ONE-HOME — ใครเรียก Codex/OpenRouter ได้เมื่อไร · กำหนดโดย user 2026.07.10)

| Agent | รู้จัก | เปิดใช้เมื่อ | เสนอ mode เองได้? |
|---|---|---|---|
| codex-bridge-agent (สะพานโคเด็กซ์) | ทุก Mode (คือ orchestrator) | user สั่ง | ✅ เสนอ mode หรือรับ mode ที่ user ระบุ |
| iCE-Compass-Next (กัปตัน) | ทุก Mode | **user สั่ง** (หรือเสนอแล้ว user OK) | ✅ |
| kim-assistant (เลขาคิม) | ทุก Mode | **user สั่ง** (หรือเสนอแล้ว user OK) | ✅ |
| thesis-ai-det-col (สมนึก/ผู้ทรง) | ทุก Mode + second detector วิชาการ | **user ระบุมาเท่านั้น** | ✅ เสนอได้ แต่รอ user ยืนยัน |
| solution-knowledge (เทพ) | ทุก Mode (เด่น refuter A/B) | **user สั่ง** ผ่าน L1 | ✅ |
| deliverable-gen (เจนนี่) | เฉพาะ Mode B/C — reviewer งาน build สำคัญ | **ตัดสินใจเองได้เมื่อ `codex_scope ∈ {available, instructed}`** จาก L1 — นอกนั้นห้าม | ⚠️ ในกรอบ scope |
| qa-master (อริส) | เฉพาะ Mode E/B — second detector ตอน QA | **ตัดสินใจเองได้เมื่อ `codex_scope ∈ {available, instructed}`** — นอกนั้นห้าม | ⚠️ ในกรอบ scope |

**`codex_scope` (field ในซองคำสั่ง L1→L2):** `none` = default L2 ห้ามเรียก · `available` = user เปิดใช้ในงานนี้แล้ว → เจนนี่/อริสตัดสินใจเองตามบทบาท · `instructed` = L1 สั่งชัด + ระบุ `codex_mode` · L2 รายงาน `codex_turns` กลับใน envelope เสมอ
**Gatekeeper อนุมัติการใช้ = กัปตัน/คิม/ผู้ทรง เท่านั้น** · manual + propose — ไม่ auto (กัน token บาน) · **OpenRouter อยู่ใต้ Matrix + contract เดียวกันทุกประการ** (เลือก Codex XOR OpenRouter ตามเนื้อหา/persona — ไม่ยิงพร้อมกัน)

## References
- `references/01_codex_cli_reference.md` — flag/output/quirk verified (รวม §Probe 2026.07.10: --output-schema, resume positional id)
- `references/02_protocol.md` — handoff/transcript + PROPOSE→CRITIQUE→REFINE + ⭐ REVIEW turn shape + ⭐ Shard pattern
- `references/03_antiAI_handoff.md` — Preset 1 เต็ม (anti-AI + GUARD)
- `references/04_presets.md` — Preset 2-4 + fleet binding pattern
- ⭐ `references/05_review_contract.md` — Review Contract เต็ม (counts/convergence/stagnation/disposition/entry-validation/FIXED-verify/Context Repairs/fallback ladders)
- ⭐ `references/verdict.schema.json` — JSON Schema สำหรับ `--schema` (บังคับ verdict format ด้วยกลไก)

## CHANGELOG
- **V02R02 (2026.07.10)** — +`--model` passthrough ใน helper (สลับ model ต่อ call: gpt-5.5/gpt-5.6-terra/gpt-5.6-luna — feature-detected ต่อ command path เหมือน --schema) · config default → gpt-5.6-terra (backup: config.toml.bak.2026.07.10-pre-terra) · re-probe CLI 0.144.1 (brew upgrade จาก 0.137.0 — เดิม 5.6 ใช้ไม่ได้ API ตอบ "requires newer version"): --output-schema คงอยู่ทั้ง exec/resume · ทดสอบจริง 4 ข้อผ่าน (terra default/luna/5.5/resume memory)
- **V02R01 (2026.07.10)** — +Modes A-E · +Review Contract (ref 05 + verdict.schema.json — M1-M8 business-adapted จาก ai-auto-work) · +helper V02R01 (--session multi-thread/--list-sessions/--schema passthrough + runtime feature-detection + overwrite guard + session log) · +Authorization Matrix + codex_scope (ONE-HOME — คำสั่ง user) · +Degradation Ladder · ref 01 +Probe 2026.07.10 · ref 02 +REVIEW shape + Shard pattern. Backward-compatible: ไม่ใส่ --session = พฤติกรรม V01 เดิม.
- **V01R02 (2026.06.22)** — +4 presets (ref 03 anti-AI เต็ม + ref 04 deliverable/code/design) + fleet binding pattern (gatekeeper-gated). Anti-AI use-case validated จริง.
- **V01R01 (2026.06.22)** — initial. manual-turn bridge: helper ask-codex.sh (--new/--resume), session continuity via codex exec resume, clean output via --output-last-message, transcript audit log. Prototype verified 3-turn with memory intact.
