# Higgsfield CLI — Command Reference (สำหรับ Claude Code path)

> ใช้เมื่ออยู่ **Claude Code** (มี Bash) — เรียก higgsfield CLI ผ่าน Bash tool แทน MCP.
> CLI v0.2.1 (brew) · alias: `higgsfield` = `higgs` = `hf` · auth login แล้ว.
> command ทั้งหมดด้านล่าง verify จาก `higgsfield --help` จริง (2026.06.14).

## Top-level commands
| command | ทำอะไร |
|---|---|
| `higgsfield account` | credit + transactions (`account status` · `account transactions`) |
| `higgsfield auth` | login / logout / token |
| `higgsfield generate` | create / cost / get / list / wait jobs |
| `higgsfield model` | list / get models |
| `higgsfield marketing-studio` | Marketing Studio assets |
| `higgsfield product-photoshoot` | brand-quality image (mode-specific prompt enhance) |
| `higgsfield soul-id` | train / manage Soul refs |
| `higgsfield upload` | upload media inputs |
| `higgsfield workflow` | list / inspect workflows |
| `higgsfield workspace` | select billing workspace |
| `higgsfield marketplace-cards` | marketplace product cards |

## Core workflow (CLI path)

### 1. Pre-flight
```bash
hf account status          # ดู credit + plan ก่อนเริ่ม
hf model list --image      # หรือ --video — ดู model ที่ใช้ได้
hf model get nano_banana_2 # ดู params/defaults ของ model
```

### 2. Preflight cost (งานแพง — ทำก่อนเสมอ)
```bash
hf generate cost <model> --prompt "..."    # ประเมิน credit ก่อนสั่งจริง
```

### 3. Upload media (ถ้ามี ref)
```bash
hf upload <file>           # คืน upload_id → ใช้กับ --image
```

### 4. Generate
```bash
# image
hf generate create nano_banana_2 --prompt "cinematic product photo" --image ./photo.png
# video (async — ใช้ --wait poll ในตัว)
hf generate create <video_model> --prompt "..." --wait --wait-timeout 20m --wait-interval 5s
```
- `<job_set_type>` = model id (จาก `model list`)
- `--prompt "..."` · `--image <file|upload_id>` · param อื่นดู `model get`
- `--json` = raw JSON output (ดู job_id/result url ตรง)

### 5. Poll async job (ถ้าไม่ใช้ --wait)
```bash
hf generate wait <job_id>         # poll จนเสร็จ
hf generate get <job_id>          # ดูสถานะ/ผล 1 job
hf generate list                  # ประวัติ jobs
```

## Specialized

### Marketing Studio (DTC ad)
```bash
hf marketing-studio --help        # ดู subcommands (product/brand/preset)
```

### Soul ID (character คงหน้า)
```bash
hf soul-id --help                 # train / list / manage
# train: ใช้ 5-20 รูป — ถามผู้ใช้ก่อน (เสียเครดิต + ~10 นาที)
```

### Product Photoshoot
```bash
hf product-photoshoot --help
```

## CLI ↔ MCP mapping (path เทียบเท่า)
| งาน | CLI (Claude Code) | MCP (Claude อื่น) |
|---|---|---|
| สร้างภาพ | `hf generate create <img_model> --prompt` | `generate_image` |
| สร้างวิดีโอ | `hf generate create <vid_model> --prompt --wait` | `generate_video` |
| preflight cost | `hf generate cost <model>` | `get_cost: true` |
| ดู model | `hf model list / get` | `models_explore` |
| credit | `hf account status` | `balance` |
| upload | `hf upload <file>` | `media_upload` / `media_import_url` |
| poll job | `hf generate wait <id>` | poll job status |
| Marketing Studio | `hf marketing-studio` | `show_marketing_studio` |
| Soul ID | `hf soul-id` | `show_characters(action=train)` |

## หลักเดียวกับ MCP path
- **preflight cost ก่อนงานแพง** (`hf generate cost`) — credit-based, 208 credit starter พอจำกัด
- **ถาม Soul ID train ก่อน** (5-20 รูป + เครดิต)
- **ห้าม fabricate model/param** — `hf model get` ดูจริง
- async (video) ใช้ `--wait` หรือ `generate wait <id>`
- credit หมด → `hf account` แล้ว top-up (หรือ `show_plans_and_credits` ถ้าอยู่ MCP)

## ตรวจ environment ก่อนเลือก path
- **มี Bash tool** = Claude Code → ใช้ CLI (ไฟล์นี้)
- **ไม่มี Bash** = Claude Desktop/Web/Cowork → ใช้ MCP (`references/mcp-functions.md`)
- Nano Banana = MCP เสมอ (ไม่มี CLI)
