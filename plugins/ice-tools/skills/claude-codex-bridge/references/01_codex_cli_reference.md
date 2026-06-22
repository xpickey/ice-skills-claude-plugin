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
