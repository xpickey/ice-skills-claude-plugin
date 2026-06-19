#!/usr/bin/env bash
# desktop-force-update.sh — Force-update Claude Desktop skills จาก GIT (marketplace repo)
#
# ใช้เมื่อ: ต้องการให้ Claude Desktop ได้ skill เวอร์ชันล่าสุดจาก GitHub
#          (เช่น มีคนอื่น push งานมา — เหมือน f215d34) โดยไม่ต้องผ่าน Claude Code reinstall
#
# ทำอะไร: (1) git pull marketplace repo ให้ล่าสุด  (2) force-copy ทุก skill ของ ice-academic
#          ลง Desktop snapshot (source = git ไม่ใช่ ~/.claude/skills master)
#
# ใช้: ./desktop-force-update.sh                  (ทุก skill ใน ice-academic)
#      ./desktop-force-update.sh jpspa-academic-article phd-mcu-pa-dissertation   (เจาะจง)
#      SKIP_PULL=1 ./desktop-force-update.sh      (ข้าม git pull — ใช้ของที่ pull ไว้แล้ว)
#
# ปลอดภัย: exclude .bak/_staging/.DS_Store/cruft · verify ในตัว · ไม่ commit/ไม่ push
# created 2026.06.19
set -euo pipefail

REPO="$HOME/.claude/plugins/marketplaces/ice-skills"
MP="$REPO/plugins/ice-academic/skills"
DT_ROOT="$HOME/Library/Application Support/Claude/local-agent-mode-sessions/skills-plugin"
EXCLUDES=( --exclude='*.bak*' --exclude='.DS_Store' --exclude='_staging' --exclude='_staging/' --exclude='{references,assets,examples}' )

echo "════════════════════════════════════════════"
echo " Claude Desktop ← Git Force-Update — $(date '+%Y-%m-%d %H:%M')"
echo "════════════════════════════════════════════"

# ─── 1) PULL git ให้ล่าสุด (source of truth) ──────────────
if [ "${SKIP_PULL:-0}" = "1" ]; then
  echo "[1/3] git pull — ข้าม (SKIP_PULL=1)"
else
  echo "[1/3] git pull --rebase (ดึง skill ล่าสุดจาก GitHub)"
  if ! git -C "$REPO" pull --rebase origin main 2>&1 | tail -4; then
    echo "  ✗ git pull ล้มเหลว (อาจมี conflict/uncommitted) — แก้ก่อน แล้วรันใหม่ หรือใช้ SKIP_PULL=1"
    exit 1
  fi
fi
echo "  → marketplace อยู่ที่ commit: $(git -C "$REPO" rev-parse --short HEAD)"

# ─── 2) หา Desktop skills dir แบบ dynamic (กัน UUID เปลี่ยน) ─
DT_SKILLS="$(find "$DT_ROOT" -maxdepth 3 -type d -name skills 2>/dev/null \
  | while read -r d; do printf '%s\t%s\n' "$(stat -f %m "$d")" "$d"; done \
  | sort -rn | head -1 | cut -f2-)"
if [ -z "$DT_SKILLS" ] || [ ! -d "$DT_SKILLS" ]; then
  echo "[2/3] ✗ ไม่พบ Claude Desktop skills dir — Desktop ติดตั้งแล้วหรือยัง? (เปิด Desktop 1 ครั้งให้สร้าง snapshot)"
  exit 1
fi

# skill list: args หรือ ทุก dir ใน marketplace ice-academic
if [ "$#" -gt 0 ]; then SKILLS=("$@")
else SKILLS=(); for d in "$MP"/*/; do SKILLS+=("$(basename "$d")"); done
fi

# ─── 3) FORCE COPY git → Desktop ─────────────────────────
echo ""
echo "[2/3] Force-copy → Desktop"
echo "  target: $DT_SKILLS"
for s in "${SKILLS[@]}"; do
  [ -d "$MP/$s" ] || { echo "  ✗ ไม่พบใน git: $s — ข้าม"; continue; }
  rsync -a --delete "${EXCLUDES[@]}" "$MP/$s/" "$DT_SKILLS/$s/"
  echo "  ✓ $s"
done

# ─── VERIFY ──────────────────────────────────────────────
echo ""
echo "[3/3] Verify (git ↔ Desktop ตรงกัน)"
ok=1
for s in "${SKILLS[@]}"; do
  [ -d "$MP/$s" ] || continue
  d=$(diff -rq "$MP/$s" "$DT_SKILLS/$s" 2>/dev/null | grep -vE '\.bak|_staging|\.DS_Store|\{references' || true)
  [ -z "$d" ] && echo "  ✓ $s" || { echo "  ✗ $s ต่าง:"; echo "$d"; ok=0; }
done

echo ""
echo "════════════════════════════════════════════"
[ "$ok" = 1 ] && echo " ✅ Desktop force-update เสร็จ จาก git $(git -C "$REPO" rev-parse --short HEAD)"
echo " ⟳ restart Claude Desktop เพื่อโหลด skill ใหม่"
echo "════════════════════════════════════════════"
