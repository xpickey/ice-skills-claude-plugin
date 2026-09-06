#!/usr/bin/env bash
# iCE POST-BUILD RECORD (V01R04 | 2026.09.05) — ทำงานหลังคำสั่งสร้างเอกสารสำเร็จ
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
# V01R04 (2026.09.06 — ซ้อมจริง Pass 6): คำสั่งที่ขึ้นต้นด้วย `cd <โฟลเดอร์> &&` สร้างไฟล์นอก cwd ของ session
# ทำให้ find ใต้ cwd ไม่เจอไฟล์ และตัวบันทึกกับตัวตรวจอัตโนมัติไม่ทำงานเงียบ ๆ → อ่านโฟลเดอร์จาก cd ก่อน
CDDIR="$(sed -nE 's/^[[:space:]]*cd[[:space:]]+"?([^"&;|]+)"?[[:space:]]*&&.*/\1/p' <<<"$CMD" | head -1)"
CDDIR="${CDDIR/#\~/$HOME}"; CDDIR="${CDDIR%"${CDDIR##*[![:space:]]}"}"; [[ -n "$CDDIR" && -d "$CDDIR" ]] && CWD="$CDDIR"   # ตัดช่องว่างท้ายที่ sed จับติดมา
FILES="$(find "$CWD" -maxdepth 3 -type f \( -name '*.pptx' -o -name '*.docx' -o -name '*.xlsx' \) \
         -not -path '*/_archive/*' -not -path '*/_temp/*' -newermt '-2 minutes' 2>/dev/null | head -5)"
# ไฟล์ผลลัพธ์ที่ระบุเป็น path เต็มในคำสั่ง (อยู่นอก cwd ก็เจอ)
for tok in $(grep -oE '(/|~/)[^[:space:]"'"'"']+\.(pptx|docx|xlsx)' <<<"$CMD"); do tok="${tok/#\~/$HOME}"; [[ -f "$tok" ]] && FILES="$FILES"$'\n'"$tok"; done
FILES="$(printf '%s\n' "$FILES" | awk 'NF && !seen[$0]++')"
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
first="$(ls -t $(printf '%s\n' "$FILES" | tr '\n' ' ') 2>/dev/null | head -1)"   # ไฟล์ที่แตะล่าสุด = ผลลัพธ์ของคำสั่งนี้
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

WRAP="$HOME/.claude/agents/_lib/thai_wordbreak.py"
if [[ -f "$WRAP" && ( "$first" == *.pptx || "$first" == *.docx || "$first" == *.xlsx ) ]]; then
  wr="$(run_limited 60 python3 "$WRAP" --audit "$first" 2>&1 | head -4 | tr '\n' ' ')"
  [[ -n "$wr" ]] && MSG="$MSG · ผลตรวจการตัดบรรทัดกลางคำภาษาไทย: $wr"
fi

# ข้อความรอเติมที่หลุดขึ้นหน้างาน (บทเรียนซ้อมจริง 2026.09.06: ผู้ตรวจพบ "รอค่าฐานจากลูกค้า" บนสไลด์สามใบ
# ทั้งที่รอบก่อนแจ้งว่าแก้แล้ว — เครื่องหาได้เองด้วยคำสั่งเดียว จึงไม่ควรปล่อยให้เป็นงานของคนตรวจ)
if [[ "$first" == *.pptx || "$first" == *.docx ]]; then
  ph="$(run_limited 30 python3 - "$first" <<'PY' 2>/dev/null
import re,sys
p=sys.argv[1]; t=[]
try:
    if p.endswith(".pptx"):
        from pptx import Presentation
        t=[sh.text_frame.text for s in Presentation(p).slides for sh in s.shapes if getattr(sh,"has_text_frame",False)]
    else:
        from docx import Document
        d=Document(p); t=[x.text for x in d.paragraphs]+[c.text for tb in d.tables for r in tb.rows for c in r.cells]
except Exception:
    sys.exit(0)
pat=re.compile(r"\[(?:รอ|NEED FROM USER|TBD|XXX|TODO)[^\]]*\]|รอค่า[ก-๙]*|รอตัวเลข[ก-๙]*|ตัวอย่างข้อความ|\bTBD\b|\bXXX\b",re.I)
hits=sorted({m.group(0) for x in t for m in pat.finditer(x or "")})
if hits: print("พบข้อความรอเติมบนหน้างาน %d แบบ: %s — ต้องเติมค่าจริงหรือย้ายไปบันทึกผู้บรรยายก่อนส่งตรวจ"%(len(hits),", ".join(hits[:5])))
PY
)"
  [[ -n "$ph" ]] && MSG="$MSG · ⚠ $ph"
fi

STYLE="$HOME/.claude/agents/_lib/thai_style_check.py"
if [[ -f "$STYLE" && ( "$first" == *.pptx || "$first" == *.docx ) ]]; then
  sty="$(run_limited 60 python3 "$STYLE" "$first" 2>&1 | tail -6 | tr '\n' ' ')"
  [[ -n "$sty" ]] && MSG="$MSG · ผลตรวจภาษาแปลและสำนวน AI อัตโนมัติ (ต้องไม่มีข้อต้องแก้ก่อนส่งผู้ตรวจคุณภาพ): $sty"
fi

# บันทึกผลตรวจอัตโนมัติของไฟล์ล่าสุดลง .last-built.json (ช่อง _audits) ให้ด่านส่งผู้ตรวจคุณภาพอ่านได้
if [[ -n "$first" ]]; then
  fd="$(dirname "$first")"; fstore="$fd/_build"; [[ -d "$fstore" ]] || fstore="$fd"
  python3 - "$fstore/.last-built.json" "$(basename "$first")" "${out:-}" "${lay:-}" "${sty:-}" <<'PY' 2>/dev/null
import json,sys,os,re
rec,name,fonts,layout,style=sys.argv[1:6]
d={}
if os.path.exists(rec):
    try: d=json.load(open(rec))
    except Exception: d={}
def v(txt,fail_pat,warn_pat=None):
    if not txt: return "NA"
    if re.search(fail_pat,txt): return "FAIL"
    if warn_pat and re.search(warn_pat,txt): return "WARN"
    return "PASS"
d.setdefault("_audits",{})[name]={"fonts":v(fonts,r"❌|FAIL"),"layout":v(layout,r"ผล: FAIL",r"ผล: WARN"),"style":v(style,r"ต้องแก้ [1-9]")}
os.makedirs(os.path.dirname(rec),exist_ok=True); json.dump(d,open(rec,"w"),ensure_ascii=False,indent=1)
PY
fi

[[ -z "$MSG" ]] && exit 0
jq -nc --arg c "หลังสร้างไฟล์: ${MSG# · } · ขั้นถัดไปตามลำดับงาน คือทำภาพรวมทุกหน้าส่งให้ผู้ใช้กวาดตา แล้วจึงส่งให้ผู้ตรวจคุณภาพ" \
  '{hookSpecificOutput:{hookEventName:"PostToolUse",additionalContext:$c}}'
exit 0
