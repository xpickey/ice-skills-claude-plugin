#!/usr/bin/env bash
# make_font_kit.sh — สร้างชุดฟอนต์แนบไปกับ deliverable ให้ลูกค้าติดตั้ง
# V01R01 | 2026.08.04 | ผูกกับ skill ice-doc-builder §3.0-A FALLBACK
#
# ทำไมต้องมี (คำสั่ง user 2026.08.04):
#   ปัญหา "ลูกค้าไม่มีฟอนต์เรา" เคยแก้ด้วยการ **ยอมลดคุณภาพ** ไปใช้ fallback ที่ลูกค้ามี
#   (Tahoma = เก่า · Sukhumvit Set = โทนไม่ทางการ) — ทั้งคู่ user ปฏิเสธ
#   ทางที่ถูกกว่า: **ส่งฟอนต์ให้ลูกค้าเลย** เพราะ IBM Plex Sans Thai Looped เป็น SIL OFL
#   + fsType 0x0000 (Installable) = แจกจ่ายได้ถูกกฎหมาย 100% · ครบ 7 น้ำหนัก = 0.8 MB
#   ⛔ Leelawadee / Tahoma / TH Sarabun New แจกไม่ได้ (proprietary) — ได้แค่หวังว่าลูกค้ามี
#
# Usage:
#   bash make_font_kit.sh <outdir> [ชื่อ family]     # default = IBM Plex Sans Thai Looped
set -uo pipefail

OUT="${1:?usage: make_font_kit.sh <outdir> [font family]}"
FAM="${2:-IBM Plex Sans Thai Looped}"
KIT="$OUT/_Fonts"

# ── ยืนยันว่า family นี้ "แจกได้" จริงก่อนทำอะไร (อ่านจากตัวไฟล์ ไม่ใช่จากความจำ)
CHECK=$(ICE_BUILD=pipeline python3 - "$FAM" <<'PY'
import sys, os
sys.path.insert(0, os.path.expanduser("~/.claude/agents/_lib"))
from font_policy import DISTRIBUTABLE
fam = sys.argv[1]
print("OK" if fam in DISTRIBUTABLE else "NO")
PY
)
if [ "$CHECK" != "OK" ]; then
  echo "⛔ '$FAM' ไม่อยู่ในรายการที่แจกจ่ายได้ (font_policy.DISTRIBUTABLE)" >&2
  echo "   ฟอนต์ proprietary (Leelawadee/Tahoma/TH Sarabun New) แจกให้ลูกค้าไม่ได้ตามลิขสิทธิ์" >&2
  exit 2
fi

mkdir -p "$KIT"
n=0
ICE_BUILD=pipeline python3 - "$FAM" "$KIT" <<'PY'
import sys, os, glob, shutil
from fontTools.ttLib import TTFont
fam, kit = sys.argv[1], sys.argv[2]
for r in ["/Library/Fonts", os.path.expanduser("~/Library/Fonts"),
          "/System/Library/Fonts/Supplemental"]:
    for p in glob.glob(f"{r}/*.ttf") + glob.glob(f"{r}/*.otf"):
        try:
            f = TTFont(p, fontNumber=0, lazy=True)
            name = f["name"].getDebugName(1) or ""
            # เอาทุกน้ำหนักของตระกูลนี้ (น้ำหนักนอก RIBBI เป็น family แยก เช่น "... SemiBold")
            if name.startswith(fam):
                fs = f["OS/2"].fsType
                if fs & 0x0002:          # Restricted = ห้าม embed/แจก
                    print(f"  ⛔ ข้าม {os.path.basename(p)} (fsType Restricted)")
                    continue
                shutil.copy2(p, kit)
                print(f"  ✓ {os.path.basename(p)}")
        except Exception:
            pass
PY
n=$(ls "$KIT" 2>/dev/null | grep -c '\.\(ttf\|otf\)$' || echo 0)
[ "$n" -eq 0 ] && { echo "❌ ไม่พบไฟล์ฟอนต์ของ '$FAM' บนเครื่องนี้" >&2; exit 3; }

cat > "$KIT/อ่านก่อนติดตั้ง-README.txt" <<EOF
ชุดฟอนต์สำหรับเปิดเอกสารชุดนี้ให้ตรงตามต้นฉบับ
================================================
ฟอนต์: $FAM  ($n ไฟล์)

ทำไมต้องติดตั้ง
---------------
ไฟล์ Excel ไม่รองรับการฝังฟอนต์ (ข้อจำกัดของ Microsoft Excel เอง ทุกแพลตฟอร์ม)
หากเครื่องของท่านไม่มีฟอนต์นี้ โปรแกรมจะเลือกฟอนต์อื่นแทนโดยอัตโนมัติ
ทำให้ความกว้างคอลัมน์ ความสูงแถว และตำแหน่งวรรณยุกต์คลาดเคลื่อนจากต้นฉบับ

วิธีติดตั้ง
-----------
Windows : เลือกไฟล์ทั้งหมด > คลิกขวา > Install for all users
macOS   : เลือกไฟล์ทั้งหมด > ดับเบิลคลิก > Install Font

ลิขสิทธิ์
---------
ฟอนต์ชุดนี้เผยแพร่ภายใต้ SIL Open Font License 1.1 (https://scripts.sil.org/OFL)
ติดตั้งและใช้งานได้โดยไม่มีค่าใช้จ่าย ทั้งงานส่วนตัวและงานเชิงพาณิชย์

หมายเหตุ
--------
หากไม่สะดวกติดตั้ง สามารถใช้ไฟล์ PDF ที่แนบมาในชุดเดียวกันแทนได้
ไฟล์ PDF ฝังฟอนต์มาครบแล้ว จึงแสดงผลตรงต้นฉบับทุกเครื่องโดยไม่ต้องติดตั้งอะไร
EOF

echo ""
echo "✅ สร้างชุดฟอนต์แล้ว: $KIT"
echo "   $n ไฟล์ · $(du -sh "$KIT" | cut -f1) · +README ภาษาไทย"
echo "   → แนบไปพร้อม .xlsx/.docx ที่ส่งลูกค้า (คู่กับ PDF companion)"
