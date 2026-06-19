#!/usr/bin/env bash
# deploy-skills.sh — sync iCE skills จาก master (~/.claude/skills) ไป 3 ปลายทาง
#   1) Marketplace (Claude Code)   2) Claude Desktop snapshot   3) .zip สำหรับ claude.ai web
#
# ใช้: ./deploy-skills.sh [skill1 skill2 ...]      (ไม่ใส่ชื่อ = ทุก skill ที่ map ไว้ด้านล่าง)
# ปลอดภัย: idempotent, exclude .bak/_staging/.DS_Store/cruft, ไม่ commit/ไม่ push (ผู้ใช้ทำเอง)
#
# maintained by User — created 2026.06.19
set -euo pipefail

# ─── CONFIG ───────────────────────────────────────────────
MASTER="$HOME/.claude/skills"
MP="$HOME/.claude/plugins/marketplaces/ice-skills/plugins/ice-academic/skills"
DT_ROOT="$HOME/Library/Application Support/Claude/local-agent-mode-sessions/skills-plugin"
WEB_OUT="$HOME/Documents/Claude/Output/skills-web-upload-$(date +%Y.%m.%d)"

# skill ที่ deploy (ค่าเริ่มต้น = 5 academic skills; override ได้ด้วย args)
DEFAULT_SKILLS=(
  phd-mcu-pa-dissertation
  agj-academic-article
  soc-sci-academic-article
  jpspa-academic-article
  phd-buddhist-public-admin
)
SKILLS=("${@:-${DEFAULT_SKILLS[@]}}")
[ "$#" -gt 0 ] && SKILLS=("$@") || SKILLS=("${DEFAULT_SKILLS[@]}")

# exclude ชุดเดียว ใช้ทุก rsync/zip
EXCLUDES=( --exclude='*.bak*' --exclude='.DS_Store' --exclude='_staging' --exclude='_staging/' --exclude='{references,assets,examples}' )

# ─── หา Desktop skills dir แบบ dynamic (กัน UUID เปลี่ยนเมื่อ reinstall) ───
# เลือกตัวที่แก้ล่าสุด (mtime) ถ้ามีหลายชุด
DT_SKILLS="$(find "$DT_ROOT" -maxdepth 3 -type d -name skills 2>/dev/null \
  | while read -r d; do printf '%s\t%s\n' "$(stat -f %m "$d")" "$d"; done \
  | sort -rn | head -1 | cut -f2-)"

echo "════════════════════════════════════════════"
echo " iCE Skills Deploy — $(date '+%Y-%m-%d %H:%M')"
echo " Skills: ${SKILLS[*]}"
echo "════════════════════════════════════════════"

# ─── 1) MASTER → MARKETPLACE (Claude Code) ───────────────
echo ""
echo "[1/3] → Marketplace (Claude Code)"
for s in "${SKILLS[@]}"; do
  [ -d "$MASTER/$s" ] || { echo "  ✗ ไม่พบ master: $s — ข้าม"; continue; }
  rsync -a --delete "${EXCLUDES[@]}" "$MASTER/$s/" "$MP/$s/"
  echo "  ✓ $s"
done

# ─── 2) MASTER → CLAUDE DESKTOP snapshot ─────────────────
echo ""
if [ -n "$DT_SKILLS" ] && [ -d "$DT_SKILLS" ]; then
  echo "[2/3] → Claude Desktop ($DT_SKILLS)"
  for s in "${SKILLS[@]}"; do
    [ -d "$MASTER/$s" ] || continue
    rsync -a --delete "${EXCLUDES[@]}" "$MASTER/$s/" "$DT_SKILLS/$s/"
    echo "  ✓ $s"
  done
else
  echo "[2/3] → Claude Desktop: ⚠ ไม่พบ skills dir (Desktop อาจยังไม่ติดตั้ง/เปลี่ยน path) — ข้าม"
fi

# ─── 3) MASTER → .zip สำหรับ claude.ai web ───────────────
echo ""
echo "[3/3] → .zip web upload ($WEB_OUT)"
mkdir -p "$WEB_OUT"
( cd "$MASTER"
  for s in "${SKILLS[@]}"; do
    [ -d "$s" ] || continue
    rm -f "$WEB_OUT/$s.zip"
    zip -rq "$WEB_OUT/$s.zip" "$s" \
      -x "*.bak*" -x "*/_staging/*" -x "*/_staging" -x "*.DS_Store" -x "*{references,assets,examples}*"
    echo "  ✓ $s.zip"
  done
)

# ─── VERIFY + สรุป ───────────────────────────────────────
echo ""
echo "── Verify (master ↔ marketplace ↔ Desktop) ──"
ok=1
for s in "${SKILLS[@]}"; do
  [ -d "$MASTER/$s" ] || continue
  d1=$(diff -rq "$MASTER/$s" "$MP/$s" 2>/dev/null | grep -vE '\.bak|_staging|\.DS_Store|\{references' || true)
  d2=""; [ -n "$DT_SKILLS" ] && d2=$(diff -rq "$MASTER/$s" "$DT_SKILLS/$s" 2>/dev/null | grep -vE '\.bak|_staging|\.DS_Store|\{references' || true)
  if [ -z "$d1" ] && [ -z "$d2" ]; then echo "  ✓ $s"; else echo "  ✗ $s ต่าง:"; echo "$d1$d2"; ok=0; fi
done
# กัน .bak หลุด
leak=$(find "$MP" -name '*.bak*' 2>/dev/null | wc -l | tr -d ' ')
echo "  .bak ใน marketplace: $leak (ควร 0)"

echo ""
echo "════════════════════════════════════════════"
[ "$ok" = 1 ] && echo " ✅ Deploy เสร็จ — Code/Desktop sync + .zip พร้อม"
echo ""
echo " ขั้นถัดไป (ผู้ใช้ทำเอง):"
echo "   • Claude Code  : bump version ใน plugin.json (ถ้ายังไม่ทำ) → git add/commit/push"
echo "   • Claude Desktop: restart app"
echo "   • Claude web   : อัปโหลด .zip ที่ $WEB_OUT ผ่าน Settings → Customize → Skills"
echo "════════════════════════════════════════════"
