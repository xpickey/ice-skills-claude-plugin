#!/usr/bin/env bash
# ============================================================
# Gemini Image MCP (rlabs/gemini-mcp) — API Key Rotation Script
# Bundled in: nanobanana-connection skill
# Version: V02R01 | Date: 2026.06.21
#
# Engine: @rlabs-inc/gemini-mcp (binary local, ไม่ใช่ uv/Vertex)
#   Migrated from nanobanana MCP (uv + Custom Skill path บน iCloud) → rlabs/gemini-mcp.
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
#   GEMINI_BIN=/path/to/gemini-mcp          (default: ~/.hermes/node/bin/gemini-mcp)
#   GEMINI_OUTPUT_DIR=/path/to/images       (default: ~/.local/share/gemini-mcp-images)
#   GEMINI_IMAGE_MODEL=gemini-3-pro-image-preview
# ============================================================

set -e

# ----- Defaults (override via env if needed) -----
GEMINI_BIN="${GEMINI_BIN:-$HOME/.hermes/node/bin/gemini-mcp}"
GEMINI_OUTPUT_DIR="${GEMINI_OUTPUT_DIR:-$HOME/.local/share/gemini-mcp-images}"
GEMINI_IMAGE_MODEL="${GEMINI_IMAGE_MODEL:-gemini-3-pro-image-preview}"
DESKTOP_CONFIG="$HOME/Library/Application Support/Claude/claude_desktop_config.json"
SERVER_NAME="gemini"

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${GREEN}=== Gemini (rlabs/gemini-mcp) API Key Rotation ===${NC}"
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

# ----- ตรวจ binary ของ gemini-mcp -----
if [[ ! -x "$GEMINI_BIN" ]]; then
  echo -e "${RED}❌ หา gemini-mcp binary ไม่เจอที่ $GEMINI_BIN${NC}"
  echo "   ติดตั้งก่อน: npm install -g @rlabs-inc/gemini-mcp"
  echo "   หรือ override ด้วย: GEMINI_BIN=/path/to/gemini-mcp bash $0"
  exit 1
fi
echo -e "${GREEN}✓ gemini-mcp binary: $GEMINI_BIN${NC}"
echo ""

# ----- [1/2] Update Claude Desktop / Cowork -----
echo -e "${YELLOW}[1/2] อัปเดต Claude Desktop / Cowork Config...${NC}"

if [[ -f "$DESKTOP_CONFIG" ]]; then
  # Backup
  BACKUP="${DESKTOP_CONFIG}.backup.$(date +%Y%m%d_%H%M%S)"
  cp "$DESKTOP_CONFIG" "$BACKUP"
  echo "  สำรอง Config เดิม → $BACKUP"

  # Update via Python (handles JSON parsing properly)
  GEMINI_BIN_ESC="$GEMINI_BIN" \
  GEMINI_OUTPUT_DIR_ESC="$GEMINI_OUTPUT_DIR" \
  GEMINI_IMAGE_MODEL_ESC="$GEMINI_IMAGE_MODEL" \
  NEW_KEY_ESC="$NEW_KEY" \
  SERVER_NAME_ESC="$SERVER_NAME" \
  DESKTOP_CONFIG_ESC="$DESKTOP_CONFIG" \
  python3 <<'PYEOF'
import json, os

p = os.environ['DESKTOP_CONFIG_ESC']
gemini_bin = os.environ['GEMINI_BIN_ESC']
output_dir = os.environ['GEMINI_OUTPUT_DIR_ESC']
image_model = os.environ['GEMINI_IMAGE_MODEL_ESC']
new_key = os.environ['NEW_KEY_ESC']
server = os.environ['SERVER_NAME_ESC']

try:
    with open(p) as f:
        cfg = json.load(f)
except (json.JSONDecodeError, FileNotFoundError):
    cfg = {}

cfg.setdefault('mcpServers', {})

if server not in cfg['mcpServers']:
    cfg['mcpServers'][server] = {
        "type": "stdio",
        "command": gemini_bin,
        "args": [],
        "env": {
            "GEMINI_IMAGE_MODEL": image_model,
            "GEMINI_OUTPUT_DIR": output_dir
        }
    }
    print(f"  สร้าง {server} entry ใหม่")
else:
    print(f"  พบ {server} entry เดิม")

cfg['mcpServers'][server].setdefault('env', {})
cfg['mcpServers'][server]['env']['GEMINI_API_KEY'] = new_key

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
    "$SERVER_NAME": {
      "type": "stdio",
      "command": "$GEMINI_BIN",
      "args": [],
      "env": {
        "GEMINI_API_KEY": "$NEW_KEY",
        "GEMINI_IMAGE_MODEL": "$GEMINI_IMAGE_MODEL",
        "GEMINI_OUTPUT_DIR": "$GEMINI_OUTPUT_DIR"
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
  claude mcp remove "$SERVER_NAME" --scope user 2>/dev/null && \
    echo "  ลบ Entry เดิมแล้ว" || echo "  ไม่มี Entry เดิม (ปกติ ถ้าเพิ่มครั้งแรก)"

  claude mcp add "$SERVER_NAME" --scope user \
    --env "GEMINI_API_KEY=$NEW_KEY" \
    --env "GEMINI_IMAGE_MODEL=$GEMINI_IMAGE_MODEL" \
    --env "GEMINI_OUTPUT_DIR=$GEMINI_OUTPUT_DIR" \
    -- "$GEMINI_BIN"

  echo -e "${GREEN}✓ Code CLI: เสร็จ${NC}"
else
  echo -e "${YELLOW}⚠️  ไม่พบ claude command — ข้าม Code CLI${NC}"
  echo "    หากต้องการ Setup ภายหลัง รัน:"
  echo "    claude mcp add $SERVER_NAME --scope user \\"
  echo "      --env GEMINI_API_KEY=<key> \\"
  echo "      --env GEMINI_IMAGE_MODEL=$GEMINI_IMAGE_MODEL \\"
  echo "      --env GEMINI_OUTPUT_DIR=$GEMINI_OUTPUT_DIR \\"
  echo "      -- $GEMINI_BIN"
fi
echo ""

# ----- สรุป -----
echo -e "${GREEN}=== ✅ Rotation เสร็จสมบูรณ์ ===${NC}"
echo ""
echo "ขั้นต่อไป (สำคัญ):"
echo "  1. Cmd+Q ปิด Claude Desktop / Cowork สนิท → เปิดใหม่"
echo "  2. ออกจาก Claude Code Session (Ctrl+D) → เปิดใหม่ → /mcp ตรวจ"
echo "  3. ลองพรอมต์ทดสอบ:"
echo "     'ทำภาพ logo มินิมอล สีน้ำเงิน 1:1' (เรียก gemini-generate-image)"
echo ""
if [[ -n "${BACKUP:-}" && -f "$BACKUP" ]]; then
  echo -e "${YELLOW}⚠️  Backup เก่าอยู่ที่: $BACKUP${NC}"
  echo "    ลบทิ้งได้เมื่อยืนยันว่า Config ใหม่ใช้งานได้"
fi
