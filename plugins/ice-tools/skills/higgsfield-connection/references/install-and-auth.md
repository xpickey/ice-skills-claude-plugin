# Higgsfield — Install & Auth (CLI + MCP Setup)

> เป้าหมาย: ติดตั้ง Higgsfield CLI → login → ต่อ MCP เข้า Claude (Desktop/Code/Cowork) → restart → verify ว่า tool ปรากฏ. Higgsfield ทำงานแบบ **credit-based** (ไม่ใช่ API key) — auth ผ่าน CLI session (token-based, อายุสั้น re-auth เป็นระยะ).

## Table of Contents
- [Prerequisites](#prerequisites)
- [Install (3 methods)](#install-3-methods)
- [Auth](#auth)
- [MCP Setup per client](#mcp-setup-per-client)
- [Verify Connection](#verify-connection)
- [Re-auth when session expires](#re-auth-when-session-expires)
- [Troubleshooting (quick)](#troubleshooting-quick)

---

## Prerequisites
- บัญชี Higgsfield ที่มี **credit** (ไม่ใช่ API key — ระบบเป็น credit-based) — credit หมดดูหัวข้อ re-auth/recovery + ใช้ `show_plans_and_credits`.
- **Node.js + npm** (สำหรับวิธี npm) — เช็ค: `node -v` / `npm -v`.
- **Homebrew** (สำหรับวิธี brew, macOS/Linux) — เช็ค: `brew --version`.
- Claude client ที่จะต่อ MCP: **Claude Desktop**, **Claude Code**, หรือ **Claude Cowork**.
- สิทธิ์เขียน config ของ client (ดู path ในแต่ละหัวข้อด้านล่าง).

---

## Install (3 methods)
เลือกวิธีใดวิธีหนึ่ง. repo อ้างอิง: `github.com/higgsfield-ai/cli`.

### Method 1 — npm (cross-platform)
```bash
npm i -g @higgsfield/cli
```

### Method 2 — Homebrew (macOS / Linux)
```bash
brew install higgsfield-ai/tap/higgsfield
```

### Method 3 — curl install script
```bash
curl https://raw.githubusercontent.com/higgsfield-ai/cli/main/install.sh | sh
```

ตรวจว่าติดตั้งสำเร็จ:
```bash
higgsfield --version
```
> ถ้า `command not found` — เปิด terminal ใหม่ (reload PATH) หรือเช็คว่า global bin (npm/brew) อยู่ใน `$PATH`.

---

## Auth
login ผ่าน CLI (token-based — เก็บ session token ไว้ในเครื่อง):
```bash
higgsfield auth login
```
- คำสั่งนี้จะเปิด flow ให้ยืนยันตัวตน (ทำตามที่ CLI แจ้งบนหน้าจอ).
- **Session อายุสั้น** — ต้อง re-auth เป็นระยะ (ดู [Re-auth](#re-auth-when-session-expires)).
- ไม่ต้องตั้ง API key — credit ของบัญชีถูกผูกกับ session นี้.

ตรวจสถานะ login (ชื่อ subcommand อาจต่างตามเวอร์ชัน CLI — ดู `higgsfield auth --help`):
```bash
higgsfield auth --help
```

---

## MCP Setup per client
แนวคิดเหมือนกันทุก client: ลงทะเบียน Higgsfield เป็น MCP server แล้ว restart. Higgsfield เป็น MCP server — เมื่อต่อสำเร็จ tool จะมาในรูป `mcp__<UUID>__<tool>` (เช่น `mcp__6473a427-...__generate_image`). **prefix เป็น UUID และต่างตาม session/install** — อย่า hardcode คาดเดา; verify จาก client จริง.

> command/transport ที่แน่นอนของ MCP server — เช็คจาก output ของ CLI (เช่น `higgsfield --help` / `higgsfield mcp --help`) หรือ repo `github.com/higgsfield-ai/cli`. ตัวอย่างด้านล่างใช้รูปแบบ MCP config มาตรฐาน (command + args); ปรับ `command`/`args` ให้ตรงกับที่ CLI ระบุ.

### Claude Code (CLI)
วิธีที่ง่ายสุด — ใช้คำสั่ง `claude mcp add` (ปรับ command ตามที่ Higgsfield CLI ระบุ):
```bash
claude mcp add higgsfield -- higgsfield mcp
```
หรือแก้ config โดยตรง (`~/.claude.json` หรือ project `.mcp.json`):
```json
{
  "mcpServers": {
    "higgsfield": {
      "command": "higgsfield",
      "args": ["mcp"]
    }
  }
}
```
ตรวจ: `claude mcp list` → ควรเห็น `higgsfield` (สถานะ connected).

### Claude Desktop
แก้ไฟล์ `claude_desktop_config.json`:
- **macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

เพิ่ม entry ใต้ `mcpServers`:
```json
{
  "mcpServers": {
    "higgsfield": {
      "command": "higgsfield",
      "args": ["mcp"]
    }
  }
}
```
> Save แล้ว **quit Claude Desktop ให้สุด** (Cmd+Q / ออกจาก tray) แล้วเปิดใหม่ — reload config ตอนเปิดเท่านั้น.

### Claude Cowork
- เปิด MCP / Connectors settings ใน Cowork → Add MCP server.
- ใส่ command เดียวกัน (`higgsfield mcp` หรือ command ที่ CLI ระบุ) แบบ local/stdio server.
- ถ้า Cowork รับ config เป็น JSON — ใช้บล็อก `mcpServers` แบบเดียวกับด้านบน.
- restart / reload Cowork หลังเพิ่ม.

> ทั้ง 3 client: ต้อง `higgsfield auth login` สำเร็จ **ก่อน** (หรือก่อนเรียก tool แรก) — MCP server ใช้ session ที่ CLI เก็บไว้.

---

## Verify Connection
หลัง restart client แล้ว:

1. **เช็ค tool ปรากฏ** — Higgsfield tool ควรโผล่ในรูป `mcp__<UUID>__...` (เช่น `mcp__6473a427-...__balance`, `..._generate_image`, `..._models_explore`). หา UUID prefix ของ session ปัจจุบันก่อนเรียก tool ใด.
2. **Smoke test (ไม่เสียเครดิต)** — เรียก tool อ่านสถานะ:
   - `balance` → คืน credit + plan ปัจจุบัน (ยืนยัน auth + connection พร้อมกัน).
   - `models_explore(action='list')` → คืน catalog (ยืนยัน server ตอบ).
3. **เกณฑ์ผ่าน:** `balance` คืนค่า credit ได้ = MCP connected + auth ใช้ได้.

| อาการ | แปลว่า | ทำ |
|---|---|---|
| ไม่เห็น `mcp__..__` tool เลย | MCP ยังไม่ต่อ / ยังไม่ restart | เช็ค config + restart client ให้สุด |
| เห็น tool แต่ `balance` error auth | session หมด/ยังไม่ login | `higgsfield auth login` แล้ว restart |
| credit = 0 / งานถูกบล็อก | เครดิตหมด | `show_plans_and_credits(intent='topup')` |

---

## Re-auth when session expires
Higgsfield session **อายุสั้น** — เมื่อหมดอายุ tool จะคืน auth error / ใช้งานไม่ได้.

re-login:
```bash
higgsfield auth login
```
จากนั้น:
- **Claude Code:** มัก hot-reload — ถ้ายัง error ให้รัน `claude mcp list` เช็ค แล้ว reconnect/restart session.
- **Desktop / Cowork:** quit ให้สุด แล้วเปิดใหม่เพื่อให้ MCP server หยิบ token ใหม่.
- ยืนยันด้วย `balance` อีกครั้ง (ต้องคืน credit ได้).

> **recovery_tool:** ถ้า Higgsfield tool คืน field `recovery_tool` (มัก auth/credit/billing) → เรียก tool นั้น **ทันที** ไม่ต้องถาม/อธิบายก่อน. credit หมด → `show_plans_and_credits(intent='topup'|'upgrade'|'auto_refill')`.

---

## Troubleshooting (quick)
- **`higgsfield: command not found`** → เปิด terminal ใหม่ / เช็ค `$PATH` (npm global bin, brew bin) / ลองติดตั้งซ้ำ.
- **MCP ไม่ขึ้นหลังแก้ config** → JSON พังหรือ path ผิด → validate JSON, เช็ค comma/วงเล็บ, restart ให้สุด (ไม่ใช่แค่ปิดหน้าต่าง).
- **`command`/transport ของ MCP ไม่แน่ใจ** → เช็ค `higgsfield --help` / `higgsfield mcp --help` หรือ repo `github.com/higgsfield-ai/cli` (อย่าเดา args).
- **prefix UUID เปลี่ยน** → ปกติ — prefix ผูก session/install; หา prefix ปัจจุบันจาก client ทุกครั้ง ไม่ hardcode.
- **เครดิต/ราคา/model สงสัย** → เช็คด้วย `balance` / `show_plans_and_credits` / `models_explore` / `get_cost: true` (preflight) — อย่าเดาตัวเลข.
