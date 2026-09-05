#!/usr/bin/env bash
# render_pdf.sh — render office → PDF ด้วย LibreOffice "ตัวจริง" + ตรวจฟอนต์ที่ฝังจริง
# V01R02 | 2026.08.30 | ผูกกับ skill ice-doc-builder §7 RENDERER LADDER + อริส E4 EVIDENCE FRESHNESS
#
# V01R02 — เพิ่มด่าน "ฟอนต์แปลกปน" (--allow / --strict-fonts):
#   เดิมสคริปต์ถามคำถามเดียวว่า "ฟอนต์ที่คาดไว้มีอยู่ไหม" จึงมองไม่เห็นฟอนต์ตัวที่ *เกินมา*
#   เคสจริง CP Axtra 2026.08.30: อักขระ ★ (U+2605) 3 จุดในไฟล์ ลากฟอนต์ HiraginoSans-W3 เข้า PDF
#   ขณะที่ audit_fonts รายงาน fonts=1 PASS และ --expect ก็ผ่าน → เครื่องที่ไม่มี Hiragino จะได้ผลต่างออกไป
#   บทเรียน: ฟอนต์ที่ "เกินมา" อันตรายพอกับฟอนต์ที่ "ขาดไป" เพราะแปลว่ามีอักขระที่ฟอนต์รางไม่มี glyph
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
#                                          [--allow "Font A,Font B"] [--strict-fonts]
#   render_pdf.sh --which          # บอกว่าเครื่องนี้จะใช้ binary ตัวไหน
#   --allow        : ชื่อฟอนต์ (คั่นด้วยจุลภาค) ที่ยอมให้มีนอกเหนือจาก --expect เช่นฟอนต์สัญลักษณ์ที่ตั้งใจใช้
#   --strict-fonts : ให้ "ฟอนต์แปลกปน" เป็นความล้มเหลว (exit 8) แทนคำเตือน — ใช้กับงานส่งลูกค้า
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
# outdir เป็น positional ตัวที่ 2 · ถ้าตัวที่ 2 ขึ้นต้นด้วย -- แปลว่าไม่ได้ระบุ outdir (ใช้โฟลเดอร์ของไฟล์ต้นทาง)
#   V01R02: เดิมยอมเฉพาะ --expect ทำให้ `render_pdf.sh ไฟล์ --strict-fonts --expect X` ถูกปฏิเสธผิด ๆ
case "${2:-}" in
  ""|--*) OUT="$(dirname "$SRC")";;
  *)      OUT="$2";;
esac
EXPECT=""; ALLOW=""; STRICT_FONTS=0
for ((i=1; i<=$#; i++)); do
  [ "${!i}" = "--expect" ] && { j=$((i+1)); EXPECT="${!j:-}"; }
  [ "${!i}" = "--allow" ]  && { j=$((i+1)); ALLOW="${!j:-}"; }
  [ "${!i}" = "--strict-fonts" ] && STRICT_FONTS=1
done
[ -f "$SRC" ] || { echo "❌ ไม่พบไฟล์: $SRC" >&2; exit 2; }

LO=$(find_real_lo) || {
  echo "❌ ไม่พบ LibreOffice ตัวจริง (PATH soffice = shim ใช้ไม่ได้)" >&2
  echo "   → ไปขั้น ② ของ Renderer Ladder: PowerPoint AppleScript save-as-PDF" >&2
  exit 3
}

# profile สดทุกครั้ง — ไม่ใส่ = LibreOffice พิมพ์ 'convert...' แต่ไม่เขียนไฟล์เงียบ ๆ
PROFILE="/tmp/lo-run-$$"
STAGE="/tmp/lo-stage-$$"
mkdir -p "$OUT" "$STAGE"
echo "→ ใช้: $LO"
# V01R02: render ลงโฟลเดอร์ชั่วคราวก่อนแล้วค่อยย้าย — ถ้า render ล้มแล้วปลายทางมี PDF ชื่อเดียวกัน
#   จากรอบก่อนอยู่ ระบบจะไปตรวจฟอนต์จากหลักฐานเก่าโดยไม่รู้ตัว (ชนกฎ EVIDENCE FRESHNESS ของผู้ตรวจ)
"$LO" --headless -env:UserInstallation="file://$PROFILE" \
      --convert-to pdf --outdir "$STAGE" "$SRC" >/dev/null 2>&1
rc=$?
rm -rf "$PROFILE"

STAGED="$STAGE/$(basename "${SRC%.*}").pdf"
PDF="$OUT/$(basename "${SRC%.*}").pdf"
# กฎเหล็ก: tool รายงานสำเร็จ ≠ ไฟล์เกิดจริง
[ -f "$STAGED" ] || { rm -rf "$STAGE"; echo "❌ render ไม่ได้ไฟล์ (rc=$rc) — ไฟล์เดิมที่ปลายทาง (ถ้ามี) ไม่ถูกแตะ" >&2; exit 4; }
mv -f "$STAGED" "$PDF"; rm -rf "$STAGE"
echo "✅ ได้ไฟล์: $PDF ($(wc -c <"$PDF" | tr -d ' ') bytes)"

# ── ⭐ POST-RENDER FONT VERIFY — ด่านที่จับ renderer regression ทุกชนิด ──────
command -v pdffonts >/dev/null || { echo "⚠ ไม่มี pdffonts — ข้ามการตรวจฟอนต์ (ไม่ใช่ 'ผ่าน')"; exit 0; }
# V01R02: อ่านครั้งเดียวแล้วเช็กสถานะ — เดิมเรียกซ้ำหลายครั้งและไม่เคยเช็ก ทำให้ PDF ที่เสียจนอ่านไม่ได้
#   หลุดเป็น "ผ่าน" ได้เมื่อไม่ได้ระบุ --expect
FONTS_RAW=$(pdffonts "$PDF" 2>/dev/null); pf_rc=$?
if [ $pf_rc -ne 0 ] || [ -z "$FONTS_RAW" ]; then
  echo "❌ pdffonts อ่าน PDF ไม่ได้ (rc=$pf_rc) — ไฟล์อาจเสีย ถือว่าไม่ผ่าน" >&2; exit 5
fi
echo "── ฟอนต์ที่ฝังจริงใน PDF ──"
echo "$FONTS_RAW"

NOEMB=$(echo "$FONTS_RAW" | awk 'NR>2 && $(NF-3)=="no" {print $1}' | head -5)
[ -n "$NOEMB" ] && { echo "❌ มีฟอนต์ที่ไม่ได้ฝัง: $NOEMB" >&2; exit 5; }

# สัญญาณ substitution ที่เจอจริงจาก shim — เจอเมื่อไหร่แปลว่า renderer มองไม่เห็นฟอนต์ระบบ
SUBS=$(echo "$FONTS_RAW" | grep -iE "LinuxLibertine|FrankRuhl|DejaVu|Liberation" | head -3)
if [ -n "$SUBS" ]; then
  echo "🔴 พบฟอนต์ fallback ของ Linux/LibreOffice — แปลว่า renderer มองไม่เห็นฟอนต์ที่เราตั้ง:" >&2
  echo "$SUBS" >&2
  echo "   ตรวจว่ากำลังใช้ shim อยู่หรือไม่: render_pdf.sh --which" >&2
  exit 6
fi

# ── การเทียบชื่อฟอนต์ ───────────────────────────────────────────────────────
# V01R02: ตัดช่องว่างและแปลงเป็นตัวพิมพ์เล็กทั้งสองฝั่งก่อนเทียบ เพราะ pdffonts คืนชื่อแบบไม่มีช่องว่าง
#   ("IBMPlexSansThaiLooped-Bold") ขณะที่ผู้เรียกอาจส่งชื่อตระกูลที่มีช่องว่าง ("IBM Plex Sans Thai Looped")
#   และเทียบแบบข้อความตรง (grep -F) เพื่อไม่ให้ชื่อฟอนต์ถูกตีความเป็น regex
norm() { echo "$1" | tr -d ' ' | tr '[:upper:]' '[:lower:]'; }
# ชื่อฟอนต์ที่ฝังจริง ตัด subset prefix 6 ตัวหน้าออก · ข้าม [none] ที่ pdffonts ใช้กับฟอนต์ไร้ชื่อ
FONT_NAMES=$(echo "$FONTS_RAW" | awk 'NR>2 && NF>0 {print $1}' | sed 's/^[A-Z]\{6\}+//' | grep -v '^\[none\]$' | sort -u)

if [ -n "$EXPECT" ]; then
  NE=$(norm "$EXPECT"); found=0
  while read -r f; do
    [ -z "$f" ] && continue
    case "$(norm "$f")" in *"$NE"*) found=1; break;; esac
  done <<< "$FONT_NAMES"
  if [ "$found" = "1" ]; then
    echo "✅ ยืนยันพบฟอนต์ที่คาดไว้: $EXPECT"
  else
    echo "❌ ไม่พบฟอนต์ที่คาดไว้ '$EXPECT' ใน PDF — ถูกแทนที่แล้ว" >&2
    exit 7
  fi
fi

# ── ⭐ ด่านฟอนต์แปลกปน — ตอบคำถามที่ --expect ตอบไม่ได้: "มีฟอนต์อื่นเกินมาไหม" ──
if [ -z "$EXPECT" ]; then
  echo "ℹ ไม่ได้ระบุ --expect จึงข้ามการตรวจฟอนต์แปลกปน (ข้าม ≠ ผ่าน)"
  exit 0
fi
EXTRA=""
NE=$(norm "$EXPECT")
while read -r f; do
  [ -z "$f" ] && continue
  nf=$(norm "$f")
  case "$nf" in *"$NE"*) continue;; esac
  hit=0
  if [ -n "$ALLOW" ]; then
    IFS=',' read -r -a _allow_arr <<< "$ALLOW"
    for a in "${_allow_arr[@]}"; do
      na=$(norm "$a"); [ -z "$na" ] && continue
      case "$nf" in *"$na"*) hit=1; break;; esac
    done
  fi
  [ "$hit" = "0" ] && EXTRA="${EXTRA}${f}
"
done <<< "$FONT_NAMES"
EXTRA=$(echo "$EXTRA" | sed '/^$/d')

if [ -n "$EXTRA" ]; then
  echo "🔴 พบฟอนต์นอกรายการที่คาดไว้ในไฟล์นี้:" >&2
  echo "$EXTRA" | sed 's/^/     /' >&2
  echo "   แปลว่ามีอักขระบางตัวที่ฟอนต์หลักไม่มี glyph → ระบบไปหยิบฟอนต์อื่นมาแทนให้เงียบ ๆ" >&2
  echo "   เครื่องที่ไม่มีฟอนต์ตัวนั้นจะแสดงผลต่างออกไป (เคสจริง: ★ U+2605 ลาก HiraginoSans เข้ามา)" >&2
  echo "   ทางแก้: หาอักขระต้นเหตุแล้วเปลี่ยนเป็นตัวที่ฟอนต์รางมี · ถ้าตั้งใจใช้ ให้ประกาศ --allow \"ชื่อฟอนต์\"" >&2
  if [ "$STRICT_FONTS" = "1" ]; then exit 8; fi
  # V01R02: ทางคำเตือนต้องจบด้วย 0 — เดิมคำสั่งสุดท้ายของสคริปต์เป็นการทดสอบเงื่อนไขที่เป็นเท็จ
  #   ทำให้ทั้งสคริปต์คืนสถานะ 1 ผู้เรียก (ผู้ตรวจคุณภาพ) แยกไม่ออกจาก error จริง
  exit 0
fi
echo "✅ ไม่มีฟอนต์แปลกปน (เทียบกับ --expect${ALLOW:+ + --allow})"
exit 0
