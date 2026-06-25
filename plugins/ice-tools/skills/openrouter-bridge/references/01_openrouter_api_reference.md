# OpenRouter API Reference (verified) — for openrouter-bridge

OpenRouter = OpenAI-compatible gateway สู่ model ทุกค่าย ผ่าน API key เดียว. verified จาก docs จริง (quickstart) 2026.06.

## Endpoint + headers
- chat: `POST https://openrouter.ai/api/v1/chat/completions`
- models: `GET https://openrouter.ai/api/v1/models`
- headers **required:** `Authorization: Bearer $OPENROUTER_API_KEY` · `Content-Type: application/json`
- headers **optional (attribution บน dashboard):** `HTTP-Referer: <site>` · `X-Title: <app name>` — helper ใส่ให้แล้ว (track usage ได้)

## Request body
```json
{ "model": "anthropic/claude-sonnet-4",
  "messages": [ {"role":"user","content":"..."}, {"role":"assistant","content":"..."} ],
  "stream": false }
```
- model id format = `provider/model` (เช่น `openai/gpt-5.1`, `deepseek/deepseek-r1`)
- **stateless** — ไม่มี session ฝั่ง server → ต้องส่ง `messages[]` ทั้งหมดทุกครั้ง (helper เก็บใน messages.json)
- `stream` = ไม่ใช้ (manual turn เอา reply เต็ม)

## Response + error
- สำเร็จ: `.choices[0].message.content` = คำตอบ (jq extract)
- error: JSON `{"error":{"message":..,"code":..}}` — **อาจมาพร้อม HTTP 200** → helper เช็ก `.error` เสมอ ไม่พึ่งแค่ HTTP code
- helper exit codes: 2=usage · 4=no-key · 5=API error · 6=empty reply · 7=ต้องเลือก model (picker)

## Alias → model id (ใน helper)
| alias | id | เหมาะกับ |
|---|---|---|
| `r1` | deepseek/deepseek-r1 | reasoning หนัก, ถกเชิงลึก |
| `sonnet` | anthropic/claude-sonnet-4 | allround เขียน/วิเคราะห์ |
| `opus` | anthropic/claude-opus-4 | งานยากสุด |
| `gpt` | openai/gpt-5.1 | second opinion ต่างค่าย |
| `gemini` | google/gemini-2.5-pro | context ยาว/เอกสารใหญ่ |
| `flash` | google/gemini-2.5-flash | เร็ว/ถูก ร่าง-สรุป |
| `llama` | meta-llama/llama-3.3-70b-instruct | open model |
> alias = best-guess id ปัจจุบัน — **verify live ด้วย `--models`** (ราคา+id เปลี่ยนได้). ถ้า id ตาย → ส่ง full id ตรง ๆ ได้เลย (resolve_model คืนค่าเดิมถ้าไม่ใช่ alias).

## Cost note (สำคัญ — ต่างจาก Codex)
stateless → ส่ง history ทั้งหมดทุก turn → **token โตเชิงเส้นทุกรอบ** (turn 5 ส่ง 5 turns). เทียบ Codex (server จำเอง ส่งแค่ prompt ใหม่). ⇒ **LOOP CAP ~5 turn สำคัญกว่า** + เลือก model ถูกลงสำหรับงานยาว ๆ (flash) / model แพงเฉพาะรอบสำคัญ.

## Key handling (security)
helper อ่าน key จาก env `OPENROUTER_API_KEY` หรือ source บรรทัดเดียวจาก `~/.hermes/.env` — **ไม่ hardcode, ไม่ echo key, ไม่ commit**. ถ้าไม่มี → exit 4 พร้อมวิธีตั้ง.
