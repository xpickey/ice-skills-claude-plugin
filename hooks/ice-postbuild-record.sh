#!/usr/bin/env bash
# iCE POST-BUILD RECORD (V01R03 | 2026.09.05) — ทำงานหลังคำสั่งสร้างเอกสารสำเร็จ
# หน้าที่: 1) บันทึกลายนิ้วมือไฟล์ที่เพิ่งสร้าง เพื่อให้ด่านก่อนสร้าง (ice-prebuild-guard V03R01)
#             รู้ได้ว่าไฟล์ถูก user แก้ไขเองในภายหลังหรือไม่
#          2) เรียกตัวตรวจฟอนต์ให้อัตโนมัติ แล้วส่งผลกลับให้ผู้ทำงานเห็นทันที
# ผลลัพธ์: คืน additionalContext ให้ผู้ทำงานอ่าน (ไม่ปิดกั้นคำสั่งที่ทำไปแล้ว)
# ที่มา: บทเรียนงาน OCC 2026.08 — การตรวจฟอนต์และการทำภาพรวมถูกเขียนเป็นกฎให้จำ แต่ถูกข้ามบ่อย
set -u
IN="$(cat)"
CMD="$(jq -r '.tool_input.command // empty' <<<"$IN" 2>/dev/null)"
[[ -z "$CMD" ]] && exit 0
[[ "$CMD" == *ICE_BUILD=pipeline* || "$CMD" == *ICE_BUILDER=jenny* || "$CMD" == *ICE_SMARTFIX=1* ]] || exit 0

# หาไฟล์เอกสารที่ถูกแตะล่าสุดภายใน 2 นาที จากโฟลเดอร์ที่คำสั่งทำงาน
CWD="$(jq -r '.cwd // empty' <<<"$IN" 2>/dev/null)"; [[ -d "${CWD:-}" ]] || CWD="$PWD"
FILES="$(find "$CWD" -maxdepth 3 -type f \( -name '*.pptx' -o -name '*.docx' -o -name '*.xlsx' \) \
         -not -path '*/_archive/*' -not -path '*/_temp/*' -newermt '-2 minutes' 2>/dev/null | head -5)"
[[ -z "$FILES" ]] && exit 0

MSG=""
while IFS= read -r f; do
  [[ -f "$f" ]] || continue
  d="$(dirname "$f")"; b="$(basename "$f")"
  store="$d/_build"; [[ -d "$store" ]] || store="$d"
  rec="$store/.last-built.json"
  h="$(shasum -a 256 "$f" | awk '{print $1}')"
  python3 - "$rec" "$b" "$h" <<'PY' 2>/dev/null
import json,sys,os
rec,name,h=sys.argv[1],sys.argv[2],sys.argv[3]
d={}
if os.path.exists(rec):
    try: d=json.load(open(rec))
    except Exception: d={}
d[name]=h
os.makedirs(os.path.dirname(rec),exist_ok=True)
json.dump(d,open(rec,"w"),ensure_ascii=False,indent=1)
PY
  MSG="$MSG · บันทึกลายนิ้วมือของ $b แล้ว (ใช้ตรวจว่ามีการแก้ไขด้วยมือในภายหลังหรือไม่)"
done <<< "$FILES"

# เรียกตัวตรวจอัตโนมัติ ถ้ามีเครื่องมืออยู่
# V01R02 (2026.09.05): macOS ไม่มีคำสั่ง timeout — บรรทัดเดิม "timeout 60 python3 …" จึงล้มเงียบทุกครั้ง
#   ทำให้การตรวจฟอนต์อัตโนมัติไม่เคยทำงานจริงตั้งแต่ 2026.08.26 · แก้เป็นตัวห่อที่ใช้ได้ทั้งสองระบบ
#   + เพิ่มตัวตรวจเลย์เอาต์ (audit_layout.py) สำหรับไฟล์นำเสนอ ตามแนวทางการทำสไลด์ 6 ข้อ
run_limited() {  # $1 = วินาที · ที่เหลือ = คำสั่ง
  local secs="$1"; shift
  if command -v gtimeout >/dev/null 2>&1; then gtimeout "$secs" "$@"; else "$@"; fi
}
first="$(head -1 <<<"$FILES")"
AUDIT="$HOME/.claude/agents/_lib/audit_fonts.py"
if [[ -f "$AUDIT" ]]; then
  out="$(run_limited 60 python3 "$AUDIT" "$first" 2>&1 | tail -3 | tr '\n' ' ')"
  [[ -n "$out" ]] && MSG="$MSG · ผลตรวจฟอนต์อัตโนมัติ: $out"
fi
LAYOUT="$HOME/.claude/agents/_lib/audit_layout.py"
if [[ -f "$LAYOUT" && "$first" == *.pptx ]]; then
  lay="$(run_limited 60 python3 "$LAYOUT" "$first" 2>&1 | tail -12 | tr '\n' ' ')"
  [[ -n "$lay" ]] && MSG="$MSG · ผลตรวจเลย์เอาต์อัตโนมัติ (ต้องเป็น PASS ก่อนส่งผู้ตรวจคุณภาพ): $lay"
fi

STYLE="$HOME/.claude/agents/_lib/thai_style_check.py"
if [[ -f "$STYLE" && ( "$first" == *.pptx || "$first" == *.docx ) ]]; then
  sty="$(run_limited 60 python3 "$STYLE" "$first" 2>&1 | tail -6 | tr '\n' ' ')"
  [[ -n "$sty" ]] && MSG="$MSG · ผลตรวจภาษาแปลและสำนวน AI อัตโนมัติ (ต้องไม่มีข้อต้องแก้ก่อนส่งผู้ตรวจคุณภาพ): $sty"
fi

[[ -z "$MSG" ]] && exit 0
jq -nc --arg c "หลังสร้างไฟล์: ${MSG# · } · ขั้นถัดไปตามลำดับงาน คือทำภาพรวมทุกหน้าส่งให้ผู้ใช้กวาดตา แล้วจึงส่งให้ผู้ตรวจคุณภาพ" \
  '{hookSpecificOutput:{hookEventName:"PostToolUse",additionalContext:$c}}'
exit 0
