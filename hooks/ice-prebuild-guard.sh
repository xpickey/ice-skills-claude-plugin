#!/usr/bin/env bash
# iCE PRE-BUILD GUARD (V03R02 | 2026.09.05) — DOC-PIPELINE V3 enforcement: "L0 BUILDS, ARIS CHECKS"
# block เฉพาะ "การสร้าง/แก้" office artifact (.pptx/.docx/.xlsx) — การอ่าน/inspect ผ่านเสมอ
#
# V03R02 (2026.09.05): + ด่าน D SKILLS-LOADED — ตรวจสภาพ session (hooks/ice_route_lib.py check) ว่าโหลด skill ตามตารางเส้นทางแล้ว
# V03R01b: ด่านใหม่ทำงานเฉพาะคำสั่งที่เขียนไฟล์เอกสารจริง และยกเว้นงานแก้ไฟล์ระบบของทีมเอง
# V03R01a: ที่อยู่ไฟล์ที่ยังไม่ถูกแทนค่าตัวแปร shell = ข้ามการตรวจความสด ไม่ปฏิเสธผิด (พบตอนทดสอบ)
# V03R01 (2026.08.26 — คำสั่ง user จากบทเรียนงาน OCC): เพิ่ม 3 ด่านหลัง marker
#   ด่าน A BASE-FRESHNESS  : ICE_BUILD=pipeline ต้องประกาศ ICE_BASE=<path> หรือ ICE_BASE=NEW
#                            และฐานที่ประกาศต้องเป็นรุ่นสูงสุดบนดิสก์ (กัน rebuild จากฐานเก่า)
#   ด่าน B USER-EDIT       : ถ้าไฟล์ฐานถูกแก้หลัง build ล่าสุด (checksum ไม่ตรง .last-built.json)
#                            → ต้องอ่าน+ซึมซับการแก้ แล้วประกาศ ICE_ABSORBED=1
#   ด่าน C DESIGN-BRIEFED  : งาน .pptx ต้องมี ICE_DESIGN=briefed (เอกสาร marker อยู่ที่
#                            b2b-slide-designer §4.11.1 = tripwire บังคับเปิด design craft)
#   เหตุผล: งานจริง 4 session ติดกัน สกิลออกแบบถูกโหลด 0 ครั้ง · OCC rebuild จากฐาน V42 ทั้งที่
#   ดิสก์อยู่ R57 ทำให้การแก้ด้วยมือของ user หาย · เอกสารหนึ่งชิ้นสะสมถึง 61 รุ่น
# V02R01: DOC-PIPELINE V3 — L0 build เองถูกกฎด้วย marker ICE_BUILD=pipeline (เอกสาร marker อยู่ใน
#   skill ice-doc-builder เท่านั้น = tripwire บังคับโหลด craft ก่อน build) · เจนนี่เหลือบท background
#   builder (ICE_BUILDER=jenny) · deny message ชี้ไป skill แทนชี้ไปเจนนี่
# V01R03: + ICE_SMARTFIX=1 (Smart Fix ≤5 slides บน valid base — rules/deliverable.md §1.6)
# V01R02 fix: ตรวจ WRITE indicators เท่านั้น (.save( หรือ build script) — read-only ผ่านเสมอ
#   (เคสจริง Viriyah 2026.07.14: unzip/list sheets โดน block → L0 ต้องอ้อม guard)
# ปิดการทำงาน: ลบ block PreToolUse ใน ~/.claude/settings.json
set -u

IN="$(cat)"
CMD="$(jq -r '.tool_input.command // empty' <<<"$IN" 2>/dev/null)"
SID="$(jq -r '.session_id // empty' <<<"$IN" 2>/dev/null)"
[[ -z "$CMD" ]] && exit 0

deny() {  # $1 = เหตุผล (ภาษา business ตาม language-register — ห้ามใช้รหัสภายในกับ user)
  jq -nc --arg r "$1" '{hookSpecificOutput:{hookEventName:"PreToolUse",permissionDecision:"deny",permissionDecisionReason:$r}}'
  exit 0
}

# ── marker ทางเลี่ยงที่อนุมัติไว้: ผ่านทันที (คงพฤติกรรมเดิม V02R01) ──
case "$CMD" in
  *ICE_BUILDER=jenny*|*ICE_SMARTFIX=1*|*ICE_INLINE_APPROVED=1*) exit 0 ;;
esac

# ── ตัวชี้วัดว่าคำสั่งนี้ "เขียนไฟล์เอกสารจริง" (ไม่ใช่แค่กล่าวถึงชื่อเครื่องหมายในข้อความ) ──
# เหตุผล: คำสั่งที่เพียงเขียนเอกสารอธิบายเครื่องหมาย ค้นหาคำ หรือแก้ไฟล์กติกาของทีม ไม่ควรถูกปิดกั้น
#         (บทเรียนเดียวกับเคส Viriyah 2026.07.14 ที่การเปิดอ่านไฟล์เคยถูกปิดกั้นผิด)
writes_office_file() {
  grep -qE '(^|[[:space:];&|(])python3?([[:space:]]|$)' <<<"$CMD" || return 1
  grep -qiE '(build_[a-z0-9_]*\.py|[a-z0-9_]*_build[a-z0-9_]*\.py)' <<<"$CMD" && return 0
  grep -qiE '(pptx|docx|xlsx|openpyxl)' <<<"$CMD" && grep -q '\.save(' <<<"$CMD" && return 0
  return 1
}

# ── งานแก้ไฟล์ระบบของทีมเอง (ใต้ ~/.claude) ไม่ใช่งานผลิตเอกสารส่งลูกค้า — ไม่เข้าด่านนี้ ──
# เหตุผล: ไฟล์กติกาและสคริปต์ของทีมมักมีข้อความอธิบายชื่อเครื่องหมายและชนิดไฟล์เอกสารอยู่ในตัว
#         ถ้าไม่ยกเว้น ด่านจะปิดกั้นการดูแลระบบของตัวเองจนแก้อะไรไม่ได้
edits_system_files() {
  grep -qE '(\.claude/(hooks|agents|skills|plugins)|_lib/)' <<<"$CMD"
}

# ── เส้น pipeline: เข้าด่าน A/B/C เฉพาะคำสั่งที่เขียนไฟล์เอกสารจริง ──
if [[ "$CMD" == *ICE_BUILD=pipeline* ]] && writes_office_file && ! edits_system_files; then

  # ด่าน C — งานไฟล์นำเสนอต้องผ่านการตั้งโจทย์ออกแบบก่อน
  if grep -qiE '\.pptx|pptx-builder|python-pptx|from pptx' <<<"$CMD" && [[ "$CMD" != *ICE_DESIGN=briefed* ]]; then
    deny "งานไฟล์นำเสนอต้องผ่านการตั้งโจทย์ออกแบบก่อนลงมือสร้าง: เปิดสกิล b2b-slide-designer หัวข้อ 4.11 DESIGN BRIEF ตอบชุดคำถามตั้งโจทย์ เขียนผลลง design spec แล้วจึงเติมคำว่า ICE_DESIGN=briefed ไว้ในคำสั่งนี้ (รายละเอียดของเครื่องหมายนี้อยู่ที่หัวข้อ 4.11.1 ของสกิลนั้น) เหตุผล: งานที่ข้ามขั้นตั้งโจทย์ออกแบบทำให้ต้องกลับมาแก้เรื่องสีและเลย์เอาต์อีกหลายรอบ"
  fi

  # ด่าน A — ต้องประกาศฐานที่ใช้สร้างงานรุ่นนี้
  if [[ "$CMD" != *ICE_BASE=* ]]; then
    deny "ก่อนสร้างหรือแก้ไฟล์ผลงาน ต้องอ่านไฟล์รุ่นล่าสุดจากโฟลเดอร์จริงก่อน แล้วประกาศว่าใช้ไฟล์ใดเป็นฐานด้วย ICE_BASE=<ที่อยู่ไฟล์รุ่นนั้น> หรือ ICE_BASE=NEW เมื่อสร้างงานชิ้นนี้เป็นครั้งแรก เหตุผล: user แก้ไขไฟล์ผลงานด้วยตนเองเป็นเรื่องปกติ การสร้างงานต่อจากความจำหรือจากสคริปต์เดิมทำให้การแก้ไขเหล่านั้นหายไป"
  fi

  BASE="$(sed -nE 's/.*ICE_BASE=("([^"]*)"|([^ ]*)).*/\2\3/p' <<<"$CMD" | head -1)"

  # ที่อยู่ไฟล์ที่ยังมีตัวแปรของ shell อยู่ (เช่น $DIR หรือ $(...)) จะถูกแทนค่าตอนคำสั่งทำงานจริง
  # ด่านนี้เห็นคำสั่งก่อนการแทนค่า จึงตรวจความสดของฐานไม่ได้ — ปล่อยผ่านโดยไม่เดา
  # (ยังบังคับให้ประกาศฐานอยู่ เพราะการประกาศคือสิ่งที่ทำให้ผู้สร้างต้องไปอ่านไฟล์จริงก่อน)
  case "$BASE" in *'$'*|*'`'*) exit 0 ;; esac

  if [[ -n "$BASE" && "$BASE" != "NEW" ]]; then
    BASE="${BASE/#\~/$HOME}"
    [[ -f "$BASE" ]] || deny "ไฟล์ฐานที่ประกาศไว้ไม่มีอยู่จริงในระบบ: $BASE — ตรวจที่อยู่ไฟล์อีกครั้งด้วยการดูรายการไฟล์ในโฟลเดอร์เป้าหมาย แล้วประกาศฐานให้ตรงกับไฟล์รุ่นล่าสุดที่มีอยู่"

    DIR="$(cd "$(dirname "$BASE")" && pwd)"; FN="$(basename "$BASE")"
    # แยก stem (ชื่อก่อนรหัสรุ่น) + รหัสรุ่น V##R##
    if [[ "$FN" =~ ^(.*)_?[Vv]([0-9]+)[Rr]([0-9]+) ]]; then
      STEM="${BASH_REMATCH[1]}"; BV=$((10#${BASH_REMATCH[2]})); BR=$((10#${BASH_REMATCH[3]}))
      BASE_KEY=$((BV*10000+BR)); NEWEST_KEY=$BASE_KEY; NEWEST_FN="$FN"
      # สแกนเฉพาะโฟลเดอร์เดียวกัน (ไม่รวม _archive ซึ่งเป็นที่เก็บรุ่นเก่าโดยเจตนา)
      while IFS= read -r g; do
        gb="$(basename "$g")"
        [[ "$gb" =~ [Vv]([0-9]+)[Rr]([0-9]+) ]] || continue
        k=$((10#${BASH_REMATCH[1]}*10000+10#${BASH_REMATCH[2]}))
        if (( k > NEWEST_KEY )); then NEWEST_KEY=$k; NEWEST_FN="$gb"; fi
      done < <(find "$DIR" -maxdepth 1 -type f -name "${STEM}*" 2>/dev/null)

      if (( NEWEST_KEY > BASE_KEY )); then
        deny "ฐานที่ประกาศไม่ใช่รุ่นล่าสุดของงานชิ้นนี้ — ประกาศไว้ว่า $FN แต่ในโฟลเดอร์เดียวกันมี $NEWEST_FN ซึ่งใหม่กว่า ให้เปิดอ่านรุ่นที่ใหม่กว่านั้นก่อน ตรวจว่ามีจุดใดที่ user แก้ไขไว้ ปรับไฟล์กำหนดเนื้อหาให้ตรงกับไฟล์จริง แล้วจึงประกาศฐานใหม่ให้ถูกต้อง"
      fi
    fi

    # ด่าน B — ไฟล์ฐานถูกแก้หลัง build ล่าสุดหรือไม่
    LAST="$DIR/_build/.last-built.json"; [[ -f "$LAST" ]] || LAST="$DIR/.last-built.json"
    if [[ -f "$LAST" && "$CMD" != *ICE_ABSORBED=1* ]]; then
      REC="$(jq -r --arg f "$FN" '.[$f] // empty' "$LAST" 2>/dev/null)"
      if [[ -n "$REC" ]]; then
        NOW="$(shasum -a 256 "$BASE" 2>/dev/null | awk '{print $1}')"
        if [[ -n "$NOW" && "$NOW" != "$REC" ]]; then
          deny "ไฟล์ $FN ถูกแก้ไขหลังจากที่ระบบสร้างครั้งล่าสุด แสดงว่า user แก้ไขด้วยตนเอง ให้เปิดอ่านไฟล์นี้ก่อน เทียบหาทุกจุดที่ถูกแก้ ปรับไฟล์กำหนดเนื้อหาให้ตรงกับไฟล์จริง แล้วเติมคำว่า ICE_ABSORBED=1 ไว้ในคำสั่งเพื่อยืนยันว่ารับการแก้ไขเหล่านั้นเข้ามาแล้ว จึงจะสร้างงานต่อได้"
        fi
      fi
    fi
  fi
  # ── ด่าน D SKILLS-LOADED (V03R02 · 2026.09.05): ตารางเส้นทาง skill ระบุว่างานนี้ต้องโหลด skill อะไรก่อน ──
  # สภาพ session ถูกจดโดย hooks/ice-skill-record.py ทุกครั้งที่ model โหลด skill หรือเปิดไฟล์
  # เหตุผล: log ส.ค.–ก.ย. 2026 พบว่า 47 จาก 56 session ที่สร้างเอกสารไม่เคยโหลด skill ออกแบบเลย
  if [[ -n "$SID" && -f "$HOME/.claude/hooks/ice_route_lib.py" ]]; then
    MISSING="$(python3 "$HOME/.claude/hooks/ice_route_lib.py" check "$SID" 2>/dev/null)" || RC=$? ; RC="${RC:-0}"
    if [[ "$RC" -eq 3 ]]; then
      deny "ยังสร้างไฟล์ไม่ได้ เพราะยังโหลด skill ที่ตารางเส้นทางกำหนดไว้สำหรับงานประเภทนี้ไม่ครบ — $MISSING — ให้โหลด skill ด้วย Skill tool และเปิดอ่านไฟล์ที่ระบุก่อน แล้วรันคำสั่งนี้อีกครั้ง (ตารางอยู่ที่ ~/.claude/hooks/skill-routing.yaml)"
    fi
  fi
  exit 0
fi

# ── ไม่มี marker ใด ๆ: ตรวจว่าเป็นคำสั่งเขียนไฟล์ office หรือไม่ (ตรรกะเดิม V01R02/V02R01) ──
grep -qE '(^|[[:space:];&|(])python3?([[:space:]]|$)' <<<"$CMD" || exit 0

is_build_script=0; is_office_write=0
grep -qiE '(build_[a-z0-9_]*\.py|[a-z0-9_]*_build[a-z0-9_]*\.py)' <<<"$CMD" && is_build_script=1
if grep -qiE '(pptx|docx|xlsx|openpyxl)' <<<"$CMD" && grep -q '\.save(' <<<"$CMD"; then is_office_write=1; fi
[[ $is_build_script -eq 0 && $is_office_write -eq 0 ]] && exit 0
edits_system_files && exit 0   # งานดูแลไฟล์ระบบของทีมเอง ไม่ใช่การผลิตเอกสาร

deny "คำสั่งนี้กำลังสร้างหรือแก้ไฟล์เอกสาร แต่ยังไม่ได้ผ่านขั้นตอนที่กำหนดไว้ ให้ทำสามอย่างนี้ก่อน: หนึ่ง เปิดสกิล ice-doc-builder ซึ่งเก็บวิธีสร้างเอกสารและรายการเครื่องหมายที่ต้องใช้ · สอง บันทึกไฟล์กำหนดเนื้อหาและไฟล์กำหนดรูปแบบลงดิสก์ · สาม จัดคิวให้ผู้ตรวจคุณภาพตรวจงานชิ้นนี้ไว้แล้ว จากนั้นจึงรันคำสั่งพร้อมเครื่องหมายที่ตรงกับบทบาทของท่าน หมายเหตุ: การเปิดอ่านหรือตรวจสอบไฟล์ไม่ถูกปิดกั้น และห้ามเลี่ยงด่านนี้ด้วยการซ่อนชื่อไฟล์"
