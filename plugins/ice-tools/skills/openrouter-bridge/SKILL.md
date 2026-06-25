---
name: openrouter-bridge
description: "Use when the user wants a second opinion / debate / review / idea-extraction from a model OTHER than Claude or Codex — picking ANY model via OpenRouter (GPT, Gemini, Llama, DeepSeek-R1, Claude, etc. through one API). Claude drives a manual turn-by-turn conversation by calling a curl helper; OpenRouter is stateless so the helper keeps conversation history locally and resends it each turn. Pick a model with --model <alias|id> (gpt/sonnet/gemini/r1/flash) or omit to get a 5-model picker. Triggers on ถาม OpenRouter, ปรึกษาหลายโมเดล, เลือก model, second opinion, รีวิวด้วยโมเดลอื่น, ถก solution หลายโมเดล, persona review, สกัด idea, ask another model, multi-model consult. NOT for one-shot when Codex/Claude suffices, and NOT an MCP server. Requires OPENROUTER_API_KEY in ~/.hermes/.env."
trigger: /openrouter-bridge
---

# Claude ↔ OpenRouter Bridge (multi-model consultant)

**Version: V01R01 | 2026.06.25** — manual-turn conversation bridge ให้ Claude ปรึกษา/ถก/รีวิว/สกัด idea กับ **model ใดก็ได้บน OpenRouter** (GPT/Gemini/Llama/DeepSeek-R1/Claude ฯลฯ ผ่าน API เดียว). Claude คุม loop. OpenRouter **stateless** → helper เก็บ history เอง (messages.json) ส่งซ้ำทุกรอบ.

> พี่น้องของ `claude-codex-bridge` — โครงเดียวกัน (--new/--resume, presets, transcript) ต่างที่ **เลือก model ได้** + คิดเงินตาม model (Codex = gpt-5.5 ตายตัว, ฟรี, มี memory ในตัว).

## When to use
- อยากได้ **second opinion จาก model ที่ต่างจาก Claude/Codex** (เช่น DeepSeek-R1 reasoning, Gemini context ยาว)
- **เลือก model ตามงาน** — reasoning หนัก→r1 · เขียนรอบด้าน→sonnet · ต่างค่าย→gpt · เอกสารใหญ่→gemini · เร็ว/ถูก→flash
- **persona review** (สวมบท CFO/CIO/CTO อ่าน deck หา concern — แบบ KTC) โดยเลือก model ต่างต่อ persona
- ถก/รีวิว/สกัด idea หลายรอบ (model จำ thread ผ่าน history-resend)

**ไม่ใช้เมื่อ:** Codex/Claude พอแล้ว (ฟรีกว่า) · ถามครั้งเดียวไม่ต่อ · ไม่อยากจ่าย token (history โตทุก turn)

## Prerequisite (ครั้งเดียว)
- สร้าง key: https://openrouter.ai/keys
- ใส่ใน `~/.hermes/.env` (uncomment): `OPENROUTER_API_KEY=sk-or-...` (หรือ `export`)
- ถ้าไม่มี key → helper พิมพ์วิธีตั้งแล้ว exit 4 (ชัดเจน ไม่เดา)
- ต้องมี `curl` + `jq` (verified พร้อม)

## How Claude drives it
```bash
SK=~/.claude/skills/openrouter-bridge/scripts
"$SK/ask-openrouter.sh" --models                       # ดู model + ราคา
"$SK/ask-openrouter.sh" --new --model r1 "<prompt>"    # เริ่ม (เลือก model)
"$SK/ask-openrouter.sh" --resume "<prompt>"            # คุยต่อ (จำ history, model เดิม)
"$SK/ask-openrouter.sh" --new "<prompt>"               # ไม่ใส่ model → ขึ้น 5-model picker (exit 7)
```
ผล = คำตอบสะอาด (jq เอา .choices[0].message.content) · history ที่ `$BRIDGE_DIR/messages.json` · audit ที่ `transcript.md`

**Model UX:** `--model <alias|id>` · alias: gpt/sonnet/opus/gemini/flash/r1/llama → full id · **ไม่ระบุ → 5-model picker** (exit 7) ให้ Claude เสนอผู้ใช้/เลือกตามงาน (ไม่ default เงียบ) · env `OPENROUTER_MODEL` ตั้ง default ถาวรได้

**Loop:** PROPOSE → CRITIQUE → REFINE · **LOOP CAP ~5 turn** (สำคัญกว่า Codex — history resend = token โตทุกรอบ) → เกินถามผู้ใช้ก่อน

## Codex หรือ OpenRouter — เลือกอันไหน
| | claude-codex-bridge | openrouter-bridge |
|---|---|---|
| model | gpt-5.5 ตายตัว | **เลือกได้ทุกตัว** |
| memory | มีในตัว (resume) | helper เก็บ history (resend) |
| cost | ฟรี (OAuth) | จ่ายตาม model |
| เหมาะเมื่อ | งานทั่วไป, ฟรี, ต้อง memory | ต้อง model เฉพาะ (reasoning/ถูก/persona ต่าง) |

## References
- `references/01_openrouter_api_reference.md` — endpoint/headers/body/models/error + alias table + cost note
- `references/02_protocol.md` — handoff + turn-taking + **persona-review pattern (KTC CFO/CIO)**
- `references/03_presets.md` — 5 presets (anti-AI / deliverable review / code review / design debate / **persona review**)

## CHANGELOG
- **V01R01 (2026.06.25)** — initial. curl+jq helper (--new/--resume/--models/--pick), stateless history-resend (messages.json), --model+alias+5-model-picker (no silent default), error-guard (.error inspect), transcript audit, key from ~/.hermes/.env. Mirror ของ claude-codex-bridge. +persona-review preset (KTC use-case).
