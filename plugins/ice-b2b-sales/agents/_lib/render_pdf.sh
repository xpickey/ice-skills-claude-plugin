#!/usr/bin/env bash
# render_pdf.sh — render office → PDF ด้วย LibreOffice "ตัวจริง" + ตรวจฟอนต์ที่ฝังจริง
# V01R01 | 2026.08.01 | ผูกกับ skill ice-doc-builder §7 RENDERER LADDER + อริส E4 EVIDENCE FRESHNESS
#
# ทำไมต้องมี: `soffice` ใน PATH บนเครื่องนี้ = **shim ของ codex runtime** ไม่ใช่ LibreOffice
#   → มองไม่เห็น /Library/Fonts → แทนฟอนต์ทั้งไฟล์เงียบ ๆ **แล้วรายงานว่าสำเร็จ**
#   หลักฐาน differential test 2026.08.01 (ไฟล์เดียวกัน):
#     shim  → NotoSans · FrankRuhlHofshi(ฮีบรู!) · LinuxLibertineG   — IBM Plex 0 ตัว
#     จริง  → IBMPlexSansThaiLooped-Regular/Bold                      ✅
#   ผลกระทบ: QA render ด้วย shim → รายงานตัวอักษรล้น/เพี้ยนเป็นชุด = **false positive ทั้งหมด**
#
# Usage:
#   render_pdf.sh <file.pptx|docx|xlsx> [outdir] [--expect "IBMPlexSansThaiLooped"]
#   render_pdf.sh --which          # บอกว่าเครื่องนี้จะใช้ binary ตัวไหน
set -uo pipefail

# ── หา LibreOffice ตัวจริง — ⛔ ห้ามใช้ `soffice` จาก PATH ────────────────────
find_real_lo() {
  local cands=(
    "/Applications/LibreOffice.app/Contents/MacOS/soffice"
    "/opt/homebrew/Caskroom/libreoffice"/*/LibreOffice.app/Contents/MacOS/soffice
    "$HOME/Applications/LibreOffice.app/Contents/MacOS/soffice"
    "/usr/lib/libreoffice/program/soffice"
  )
  for c in "${cands[@]}"; do
    [ -x "$c" ] || continue
    # ตัวจริงต้องรายงานชื่อขึ้นต้น "LibreOffice " — shim จะรายงานอย่างอื่น
    if "$c" --version 2>/dev/null | head -1 | grep -q "^LibreOffice "; then
      echo "$c"; return 0
    fi
  done
  return 1
}

if [ "${1:-}" = "--which" ]; then
  echo "PATH soffice : $(command -v soffice || echo '(ไม่มี)')"
  [ -n "$(command -v soffice)" ] && echo "  → version   : $(soffice --version 2>&1 | head -1)"
  if LO=$(find_real_lo); then
    echo "LibreOffice จริง: $LO"
    echo "  → version   : $("$LO" --version 2>&1 | head -1)"
  else
    echo "❌ ไม่พบ LibreOffice ตัวจริง — ติดตั้งก่อน หรือใช้ Renderer Ladder ขั้น ② (PowerPoint AppleScript)"
  fi
  exit 0
fi

SRC="${1:?usage: render_pdf.sh <file> [outdir] [--expect FONT]}"
# กัน silent failure (เคสจริง 2026.08.09: เรียกด้วย --output_dir <path> → สคริปต์สร้างโฟลเดอร์ชื่อ "--output_dir" จริง ๆ
# แล้วทิ้ง path ที่ตั้งใจไว้เงียบ ๆ) — outdir เป็น positional ตัวที่ 2 เท่านั้น flag เดียวที่รับคือ --expect
case "$SRC" in -*) echo "❌ argument แรกต้องเป็น path ไฟล์ ไม่ใช่ flag: $SRC" >&2
  echo "   usage: render_pdf.sh <file> [outdir] [--expect FONT]" >&2; exit 2;; esac
OUT="${2:-$(dirname "$SRC")}"
case "$OUT" in --expect) OUT="$(dirname "$SRC")";;   # เรียกแบบ render_pdf.sh file --expect FONT = ไม่ได้ระบุ outdir
  -*) echo "❌ outdir เป็น positional ตัวที่ 2 — ไม่รับ flag ชื่อ '$OUT' (สคริปต์นี้ไม่มี --output_dir/--outdir)" >&2
  echo "   ✅ ถูก: render_pdf.sh ไฟล์.docx \"<โฟลเดอร์ปลายทาง>\" --expect FONT" >&2; exit 2;; esac
EXPECT=""
for ((i=1; i<=$#; i++)); do
  [ "${!i}" = "--expect" ] && { j=$((i+1)); EXPECT="${!j:-}"; }
done
[ -f "$SRC" ] || { echo "❌ ไม่พบไฟล์: $SRC" >&2; exit 2; }

LO=$(find_real_lo) || {
  echo "❌ ไม่พบ LibreOffice ตัวจริง (PATH soffice = shim ใช้ไม่ได้)" >&2
  echo "   → ไปขั้น ② ของ Renderer Ladder: PowerPoint AppleScript save-as-PDF" >&2
  exit 3
}

# profile สดทุกครั้ง — ไม่ใส่ = LibreOffice พิมพ์ 'convert...' แต่ไม่เขียนไฟล์เงียบ ๆ
PROFILE="/tmp/lo-run-$$"
mkdir -p "$OUT"
echo "→ ใช้: $LO"
"$LO" --headless -env:UserInstallation="file://$PROFILE" \
      --convert-to pdf --outdir "$OUT" "$SRC" >/dev/null 2>&1
rc=$?
rm -rf "$PROFILE"

PDF="$OUT/$(basename "${SRC%.*}").pdf"
# กฎเหล็ก: tool รายงานสำเร็จ ≠ ไฟล์เกิดจริง
[ -f "$PDF" ] || { echo "❌ render ไม่ได้ไฟล์ (rc=$rc): $PDF" >&2; exit 4; }
echo "✅ ได้ไฟล์: $PDF ($(wc -c <"$PDF" | tr -d ' ') bytes)"

# ── ⭐ POST-RENDER FONT VERIFY — ด่านที่จับ renderer regression ทุกชนิด ──────
command -v pdffonts >/dev/null || { echo "⚠ ไม่มี pdffonts — ข้ามการตรวจฟอนต์ (ไม่ใช่ 'ผ่าน')"; exit 0; }
echo "── ฟอนต์ที่ฝังจริงใน PDF ──"
pdffonts "$PDF"
NOEMB=$(pdffonts "$PDF" | awk 'NR>2 && $(NF-3)=="no" {print $1}' | head -5)
[ -n "$NOEMB" ] && { echo "❌ มีฟอนต์ที่ไม่ได้ฝัง: $NOEMB" >&2; exit 5; }

# สัญญาณ substitution ที่เจอจริงจาก shim — เจอเมื่อไหร่แปลว่า renderer มองไม่เห็นฟอนต์ระบบ
SUBS=$(pdffonts "$PDF" | grep -iE "LinuxLibertine|FrankRuhl|DejaVu|Liberation" | head -3)
if [ -n "$SUBS" ]; then
  echo "🔴 พบฟอนต์ fallback ของ Linux/LibreOffice — แปลว่า renderer มองไม่เห็นฟอนต์ที่เราตั้ง:" >&2
  echo "$SUBS" >&2
  echo "   ตรวจว่ากำลังใช้ shim อยู่หรือไม่: render_pdf.sh --which" >&2
  exit 6
fi

if [ -n "$EXPECT" ]; then
  if pdffonts "$PDF" | grep -qi "$EXPECT"; then
    echo "✅ ยืนยันพบฟอนต์ที่คาดไว้: $EXPECT"
  else
    echo "❌ ไม่พบฟอนต์ที่คาดไว้ '$EXPECT' ใน PDF — ถูกแทนที่แล้ว" >&2
    exit 7
  fi
fi
