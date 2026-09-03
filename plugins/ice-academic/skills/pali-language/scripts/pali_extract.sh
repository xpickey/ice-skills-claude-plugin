#!/usr/bin/env bash
# pali_extract.sh — สกัดเอกสารบาลี (PDF/docx/…) เป็น Markdown 2 แหล่ง (text-layer + OCR) แล้วตรวจ
# ใช้: bash pali_extract.sh <FILE> <OUTDIR>
# ต้องมี: ~/.claude/agents/_lib/doc_to_md.sh (skill ice-doc-reader) · pdftoppm (poppler) สำหรับ OCR
# ผลลัพธ์: <OUTDIR>/<name>.md (text layer) · <OUTDIR>/<name>-ocr.md (OCR) · รายงาน pali_check
# skill: pali-language V01R01 · 2026.09.03 · local-only ไม่ส่งไฟล์ออกนอกเครื่อง
set -uo pipefail
HELPER="$HOME/.claude/agents/_lib/doc_to_md.sh"
HERE="$(cd "$(dirname "$0")" && pwd)"
FILE="${1:?ใส่ path ไฟล์ต้นทาง}"; OUT="${2:?ใส่โฟลเดอร์ผลลัพธ์}"
[ -x "$HELPER" ] || [ -f "$HELPER" ] || { echo "✗ ไม่พบ helper ice-doc-reader: $HELPER"; exit 4; }
mkdir -p "$OUT"
name="$(basename "${FILE%.*}")"

echo "═══ [1/3] text layer → $OUT/$name.md ═══"
bash "$HELPER" "$FILE" -o "$OUT/$name.md"; t_exit=$?
echo "   exit=$t_exit $([ $t_exit -eq 3 ] && echo '(ไทยเสีย — ปกติสำหรับ PDF บาลีที่ฟอนต์พัง · โรมัน/พินทุยังใช้ได้)')"

echo "═══ [2/3] OCR ทุกหน้า → $OUT/$name-ocr.md (~1.8 วิ/หน้า) ═══"
bash "$HELPER" "$FILE" --ocr-all -o "$OUT/$name-ocr.md"; o_exit=$?
echo "   exit=$o_exit"

echo "═══ [3/3] ตรวจเฉพาะบาลี ═══"
bash "$HERE/pali_check.sh" "$OUT/$name.md" "$OUT/$name-ocr.md"

echo
echo "provenance ที่ต้องบันทึกเมื่อประกอบไฟล์สุดท้าย:"
echo "  source: $FILE · extracted: $(date +%Y-%m-%d) · method: dual-source · thai_check: text=$t_exit ocr=$o_exit"
