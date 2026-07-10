# Codex CLI Reference (verified) — for claude-codex-bridge

Codex CLI **v0.137.0**, login = OAuth ("Logged in using ChatGPT"), model `gpt-5.5`, provider `openai`, base URL `chatgpt.com/backend-api/codex` (default when ChatGPT-login). Auth stored in `~/.codex/auth.json` (tokens, no API key). ทั้งหมดนี้ verified จากเครื่องจริง 2026.06.22.

## Two subcommands, DIFFERENT flag sets ⚠️
นี่คือ gotcha หลัก — `exec` กับ `exec resume` รับ flag ไม่เหมือนกัน:

| flag | `codex exec` | `codex exec resume` |
|---|---|---|
| `-s, --sandbox` | ✅ | ❌ (inherits from session) |
| `-C, --cd` | ✅ | ❌ (inherits) |
| `--skip-git-repo-check` | ✅ | ✅ |
| `--json` | ✅ | ✅ |
| `-o, --output-last-message` | ✅ | ✅ |
| `-m, --model` | ✅ | ✅ |
| `--ephemeral` | ✅ | ✅ |
| `-a, --ask-for-approval` | ❌ **ไม่มี** | ❌ **ไม่มี** |

→ ถ้าใส่ `-s` หรือ `-C` กับ `resume` = `error: unexpected argument '-s' found` (exit 2).
→ ไม่มี `-a` ที่ subcommand ไหนเลย — **approval คุมผ่าน sandbox mode เท่านั้น**.

## ⭐ Probe 2026.07.10 (codex-cli 0.137.0 — ข้อเท็จจริงเพิ่มที่ตารางบนยังไม่มี)

| flag/ความสามารถ | `codex exec` | `codex exec resume` | ใช้ทำอะไรใน bridge |
|---|---|---|---|
| `--output-schema <FILE>` | ✅ | ✅ | **บังคับคำตอบเป็น JSON ตาม schema** → helper V02R01 รับ `--schema <file>` ส่งต่อ (ใช้กับ `references/verdict.schema.json` ตาม ref 05 Review Contract) |
| `resume [SESSION_ID]` positional | — | ✅ รับ **UUID หรือ thread name** · มี `--last` (ล่าสุด) + `--all` (ปิด cwd filter) | multi-session native — helper V02R01 เก็บ id ต่อชื่อ session |
| `-c key=value` config override · `-p profile` | ✅ | ✅ (-c) | ยังไม่ใช้ default — จดไว้ |
| `codex exec review` subcommand | ✅ (review ทั้ง git repo) | — | ไม่ใช้ในงานเอกสารธุรกิจ |

**กติกาบำรุงรักษา:** helper V02R01 มี runtime feature-detection สำหรับ `--output-schema` (เช็คจาก `--help` จริงก่อนใช้ — CLI อัปเดตแล้ว flag หาย = เตือน+ทำต่อแบบไม่มี schema ไม่พังเงียบ) · ใครแก้ helper ครั้งหน้า: **probe `codex --version` + `--help` ก่อนเสมอ** แล้วอัปเดตหมวดนี้พร้อมประทับวันที่

## Output (เอา text สะอาด)
- `--output-last-message <FILE>` → เขียน **เฉพาะคำตอบสุดท้าย** ของ Codex (ไม่มี banner/ERROR/token) → `cat <FILE>`
- `--json` → JSONL บน stdout, event สำคัญ:
  - `{"type":"thread.started","thread_id":"019e..."}` ← **session id สำหรับ resume**
  - `{"type":"item.completed","item":{"type":"agent_message","text":"..."}}` ← คำตอบ
  - `{"type":"turn.completed","usage":{"input_tokens":...}}` ← token (สังเกต input_tokens โตขึ้นทุก turn = context สะสม = resume จำจริง)
- **stderr** = noise (skill load error, MCP `rmcp` transport error, githubcopilot auth) → แยกลง err.log, อย่าปนคำตอบ

## Session continuity
- session ถูก persist อัตโนมัติที่ `~/.codex/sessions/YYYY/MM/DD/rollout-*.jsonl`
- resume ด้วย `codex exec resume <UUID>` หรือ `--last`
- พิสูจน์แล้ว: 3-turn conversation, session id เดียวตลอด, Codex อ้างถึงสิ่งที่ตั้งชื่อใน turn ก่อนได้

## Sandbox modes
- `read-only` (default ของ helper) — Codex อ่าน/วิเคราะห์ได้ แก้ไฟล์ไม่ได้ → ปลอดภัยสำหรับถก/review
- `workspace-write` — แก้ไฟล์ใน workspace ได้ → **ถามผู้ใช้ก่อนใช้** (set `BRIDGE_SANDBOX=workspace-write`)
- `danger-full-access` / `--dangerously-bypass-approvals-and-sandbox` — อย่าใช้นอกจากผู้ใช้ยืนยันชัด

## Trust-directory note
`codex exec` นอก git repo ต้องใส่ `--skip-git-repo-check` ไม่งั้น "Not inside a trusted directory" (exit 2).

## Invocation templates (ที่ helper ใช้)
```bash
# new thread
codex exec --json -o LAST --skip-git-repo-check -s read-only -C "$DIR" "<prompt>" >EVENTS 2>err.log
# resume (NO -s, NO -C)
codex exec resume "<SID>" --json -o LAST --skip-git-repo-check "<prompt>" >EVENTS 2>err.log
```

## ⭐ Probe 2026.07.10 (บ่าย — codex-cli 0.144.1 หลัง brew upgrade จาก 0.137.0)
- `--output-schema` ✅ ยังอยู่ทั้ง `exec` และ `exec resume` · `resume` ยังไม่รับ `-s`/`-C` ตามเดิม
- **Models ในบัญชี (จาก models_cache.json):** gpt-5.4 · gpt-5.4-mini · **gpt-5.5** · **gpt-5.6-luna** · **gpt-5.6-terra** · codex-auto-review — ⚠️ 5.6 ใช้ได้เฉพาะ CLI ≥0.144 (0.137 โดน API 400 "requires newer version")
- config default = `gpt-5.6-terra` (backup pre-terra มี) · helper V02R02 `--model` สลับต่อ call — ทดสอบจริง terra/luna/5.5 + resume memory ผ่านครบ
