#!/usr/bin/env bash
# ============================================================
# Nanobanana MCP — API Key Rotation Script
# Bundled in: nanobanana-connection skill
# Version: V01R01 | Date: 2026.05.25
#
# Purpose:
#   เปลี่ยน Gemini API Key พร้อมกันใน:
#     - Claude Desktop / Cowork (claude_desktop_config.json)
#     - Claude Code CLI (~/.claude.json via `claude mcp`)
#
# Usage:
#   bash scripts/rotate_api_key.sh
#   หรือ
#   chmod +x scripts/rotate_api_key.sh && ./scripts/rotate_api_key.sh
#
# Environment Overrides (optional):
#   TARGET_DIR=/path/to/nanobanana-mcp
#   IMAGE_OUTPUT_DIR=/path/to/images
# ============================================================

set -e

# ----- Defaults (override via env if needed) -----
TARGET_DIR="${TARGET_DIR:-/Users/xpickey/Documents/Claude/Custom Skill/nanobanana-mcp}"
DESKTOP_CONFIG="$HOME/Library/Application Support/Claude/claude_desktop_config.json"
IMAGE_OUTPUT_DIR="${IMAGE_OUTPUT_DIR:-$TARGET_DIR/images}"

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${GREEN}=== Nanobanana API Key Rotation ===${NC}"
echo ""

# ----- เตือนเรื่อง Key เก่า -----
echo -e "${RED}⚠️  ก่อนเริ่ม: หาก Key เก่ารั่ว/Compromise${NC}"
echo "    เปิด https://aistudio.google.com/apikey"
echo "    หา Key เก่า → กด 3 จุด → Delete API Key"
echo "    จากนั้นสร้าง Key ใหม่ → Copy ไว้"
echo ""
read -p "พร้อมแล้วกด Enter เพื่อต่อ (Ctrl+C เพื่อยกเลิก)..."
echo ""

# ----- รับ Key ใหม่ -----
echo -e "${YELLOW}วาง Gemini API Key ใหม่ (ขึ้นต้น AIza...):${NC}"
read -r -s NEW_KEY
echo ""

if [[ -z "$NEW_KEY" ]]; then
  echo -e "${RED}❌ ไม่มี Key — หยุด${NC}"
  exit 1
fi

if [[ ! "$NEW_KEY" =~ ^AIza ]]; then
  echo -e "${YELLOW}⚠️  Key ไม่ขึ้นต้น AIza — ตรวจให้แน่ใจ${NC}"
  read -p "ยืนยันจะใช้ Key นี้? (y/N) " confirm
  [[ "$confirm" != "y" ]] && exit 1
fi
echo -e "${GREEN}✓ ได้รับ Key ใหม่${NC}"
echo ""

# ----- (Optional) ทดสอบ Key ก่อน Update Config -----
echo -e "${YELLOW}🔍 ทดสอบ Key ก่อนใช้งานจริง (ใช้เวลา <3 วินาที)...${NC}"
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" \
  "https://generativelanguage.googleapis.com/v1beta/models?key=$NEW_KEY" \
  -H "Content-Type: application/json" --max-time 10 || echo "000")

case "$HTTP_CODE" in
  200)
    echo -e "${GREEN}✓ Key ใช้งานได้${NC}"
    ;;
  401|403)
    echo -e "${RED}❌ Key ไม่ Valid (HTTP $HTTP_CODE) — กรุณาตรวจสอบที่ AI Studio${NC}"
    exit 1
    ;;
  000)
    echo -e "${YELLOW}⚠️  ทดสอบ Network ไม่ได้ — จะทำต่อโดยไม่ทดสอบ${NC}"
    ;;
  *)
    echo -e "${YELLOW}⚠️  ได้ HTTP $HTTP_CODE — อาจมีปัญหา แต่จะทำต่อ${NC}"
    ;;
esac
echo ""

# ----- หา Full Path ของ uv -----
UV_PATH=""
for c in "$HOME/.local/bin/uv" "/opt/homebrew/bin/uv" "/usr/local/bin/uv" "$(which uv 2>/dev/null)"; do
  if [[ -x "$c" ]]; then UV_PATH="$c"; break; fi
done

if [[ -z "$UV_PATH" ]]; then
  echo -e "${RED}❌ หา uv ไม่เจอ — ติดตั้งก่อน:${NC}"
  echo "   curl -LsSf https://astral.sh/uv/install.sh | sh"
  exit 1
fi
echo -e "${GREEN}✓ uv path: $UV_PATH${NC}"
echo ""

# ----- [1/2] Update Claude Desktop / Cowork -----
echo -e "${YELLOW}[1/2] อัปเดต Claude Desktop / Cowork Config...${NC}"

if [[ -f "$DESKTOP_CONFIG" ]]; then
  # Backup
  BACKUP="${DESKTOP_CONFIG}.backup.$(date +%Y%m%d_%H%M%S)"
  cp "$DESKTOP_CONFIG" "$BACKUP"
  echo "  สำรอง Config เดิม → $BACKUP"

  # Update via Python (handles JSON parsing properly)
  TARGET_DIR_ESC="$TARGET_DIR" \
  IMAGE_OUTPUT_DIR_ESC="$IMAGE_OUTPUT_DIR" \
  UV_PATH_ESC="$UV_PATH" \
  NEW_KEY_ESC="$NEW_KEY" \
  HOME_ESC="$HOME" \
  DESKTOP_CONFIG_ESC="$DESKTOP_CONFIG" \
  python3 <<'PYEOF'
import json, os, sys

p = os.environ['DESKTOP_CONFIG_ESC']
target_dir = os.environ['TARGET_DIR_ESC']
image_dir = os.environ['IMAGE_OUTPUT_DIR_ESC']
uv_path = os.environ['UV_PATH_ESC']
new_key = os.environ['NEW_KEY_ESC']
home = os.environ['HOME_ESC']

try:
    with open(p) as f:
        cfg = json.load(f)
except (json.JSONDecodeError, FileNotFoundError):
    cfg = {}

cfg.setdefault('mcpServers', {})

if 'nanobanana' not in cfg['mcpServers']:
    cfg['mcpServers']['nanobanana'] = {
        "command": uv_path,
        "args": ["run", "--directory", target_dir,
                 "python", "-m", "nanobanana_mcp_server.server"],
        "env": {
            "IMAGE_OUTPUT_DIR": image_dir,
            "NANOBANANA_MODEL": "auto",
            "PATH": f"{home}/.local/bin:/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin"
        }
    }
    print("  สร้าง nanobanana entry ใหม่")
else:
    print("  พบ nanobanana entry เดิม")

cfg['mcpServers']['nanobanana'].setdefault('env', {})
cfg['mcpServers']['nanobanana']['env']['GEMINI_API_KEY'] = new_key

with open(p, 'w') as f:
    json.dump(cfg, f, indent=2)
print("  ✓ อัปเดต API Key สำเร็จ")
PYEOF
  echo -e "${GREEN}✓ Desktop / Cowork: เสร็จ${NC}"
else
  echo -e "${YELLOW}⚠️  ไม่พบ Config — สร้างใหม่${NC}"
  mkdir -p "$(dirname "$DESKTOP_CONFIG")"
  cat > "$DESKTOP_CONFIG" <<EOF
{
  "mcpServers": {
    "nanobanana": {
      "command": "$UV_PATH",
      "args": ["run", "--directory", "$TARGET_DIR",
               "python", "-m", "nanobanana_mcp_server.server"],
      "env": {
        "GEMINI_API_KEY": "$NEW_KEY",
        "IMAGE_OUTPUT_DIR": "$IMAGE_OUTPUT_DIR",
        "NANOBANANA_MODEL": "auto",
        "PATH": "$HOME/.local/bin:/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin"
      }
    }
  }
}
EOF
  echo -e "${GREEN}✓ สร้าง Config ใหม่${NC}"
fi
echo ""

# ----- [2/2] Update Claude Code CLI -----
echo -e "${YELLOW}[2/2] อัปเดต Claude Code CLI...${NC}"
if command -v claude &> /dev/null; then
  claude mcp remove nanobanana --scope user 2>/dev/null && \
    echo "  ลบ Entry เดิมแล้ว" || echo "  ไม่มี Entry เดิม (ปกติ ถ้าเพิ่มครั้งแรก)"

  claude mcp add nanobanana --scope user \
    --env "GEMINI_API_KEY=$NEW_KEY" \
    --env "IMAGE_OUTPUT_DIR=$IMAGE_OUTPUT_DIR" \
    --env "NANOBANANA_MODEL=auto" \
    -- "$UV_PATH" run --directory "$TARGET_DIR" python -m nanobanana_mcp_server.server

  echo -e "${GREEN}✓ Code CLI: เสร็จ${NC}"
else
  echo -e "${YELLOW}⚠️  ไม่พบ claude command — ข้าม Code CLI${NC}"
  echo "    หากต้องการ Setup ภายหลัง รัน:"
  echo "    claude mcp add nanobanana --scope user \\"
  echo "      --env GEMINI_API_KEY=<key> \\"
  echo "      --env IMAGE_OUTPUT_DIR=$IMAGE_OUTPUT_DIR \\"
  echo "      -- $UV_PATH run --directory \"$TARGET_DIR\" \\"
  echo "         python -m nanobanana_mcp_server.server"
fi
echo ""

# ----- สรุป -----
echo -e "${GREEN}=== ✅ Rotation เสร็จสมบูรณ์ ===${NC}"
echo ""
echo "ขั้นต่อไป (สำคัญ):"
echo "  1. Cmd+Q ปิด Claude Desktop / Cowork สนิท → เปิดใหม่"
echo "  2. ออกจาก Claude Code Session (Ctrl+D) → เปิดใหม่ → /mcp ตรวจ"
echo "  3. ลองพรอมต์ทดสอบ:"
echo "     'ใช้ nanobanana ทำภาพ logo มินิมอล สีน้ำเงิน 1:1'"
echo ""
if [[ -f "$BACKUP" ]]; then
  echo -e "${YELLOW}⚠️  Backup เก่าอยู่ที่: $BACKUP${NC}"
  echo "    ลบทิ้งได้เมื่อยืนยันว่า Config ใหม่ใช้งานได้"
fi
