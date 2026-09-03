#!/usr/bin/env bash
# pali_check.sh — ตรวจความเสียหายเฉพาะข้อความบาลีใน Markdown ที่สกัดจากเอกสาร
# ใช้: bash ~/.claude/skills/pali-language/scripts/pali_check.sh <text-layer.md> [<ocr.md>]
# ตรวจ P1-P7 ตาม references/09-document-ingestion.md §4 · ไม่แก้ไฟล์ · ไม่ส่งอะไรออกนอกเครื่อง
# exit 0 = ไม่พบ 🔴 ในไฟล์ใด · exit 3 = พบ 🔴 อย่างน้อย 1 ข้อ (ส่วนนั้นห้ามใช้โดยไม่ประกอบ dual-source) · exit 1 = ไม่พบไฟล์
# ใช้ python3 ของระบบสำหรับ regex Unicode (grep ช่วงอักษรไทยบน macOS ไม่เสถียรตาม locale)
# skill: pali-language V01R03 · 2026.09.04 — R03 แก้ตาม QA อริส delta PALI-012/013: pointer → 09 §2.3 · P5 ใช้อัตราส่วน short > tbl×20 · regex PUA เขียนเป็น \uXXXX · R02 แก้ตาม QA อริส PALI-001/002/005: P1 ใช้อัตราส่วนแทนตัวเลขดิบ · +P5 ตารางแตก · +P7 Private Use/พินทุกำพร้า · คืน exit code จริง
set -uo pipefail
export LC_ALL=en_US.UTF-8 2>/dev/null || true
RC=0

check_one() {
  local f="$1" label="$2"
  [ -f "$f" ] || { echo "  ✗ ไม่พบไฟล์: $f"; return 1; }
  python3 - "$f" "$label" <<'PY'
import re, sys, os
f, label = sys.argv[1], sys.argv[2]
t = open(f, encoding="utf-8", errors="replace").read()
thai   = len(re.findall(r"[฀-๿]", t))
amm    = t.count("ำ")            # ำ
pinthu = t.count("ฺ")            # ฺ
nikkh  = t.count("ํ")            # ํ
diacr  = len(re.findall(r"[āīūṅñṭḍṇḷṃṁ]", t))
lines  = t.splitlines()
tbl    = sum(1 for l in lines if l.lstrip().startswith("|"))
short  = sum(1 for l in lines if 0 < len(l.strip()) <= 12 and not l.lstrip().startswith(("|", "#", "-", "*", "`")))
C = "กขคฆจฉชฌฏฐฑฒตถทธปผพภ"
p1_raw = len(re.findall(rf"[{C}ยรลวสห]ุ[{C}]", t))   # สระอุ + พยัญชนะ — นับทั้งของถูก (พุทฺธ ทุติยา) และของเสีย (ปุตุต ตสุส)
p1_bad = p1_raw >= 20 and p1_raw > pinthu                  # สระอุแบบนี้มากกว่าพินทุ = OCR เปลี่ยน ฺ→ุ เป็นระบบ (วัดจริง: OCR ตำรา 696:179 · OCR สไลด์3 136:73 · text layer ตำรา 457:1,922)
p2 = len(re.findall(r"(?<![฀-๿])[ก-ฮ]{1,3}ฺ?[ก-ฮ]?์(?![฀-๿])", t))
p3 = len([m for m in re.findall(r"[A-Za-z]+[฀-๿!0-9]+[A-Za-z]*|[A-Za-z]*[฀-๿!0-9]+[A-Za-z]+", t) if not m.isdigit()])
pua    = len(re.findall(r"[\uf700-\uf8ff]", t))            # อักขระเขต Private Use ที่ฟอนต์ไทยใช้แทน glyph สำรอง
orphan = len(re.findall(r"(?<![ก-ฮ])ฺ", t))          # พินทุที่ไม่มีพยัญชนะไทยนำหน้า (พยัญชนะกลายเป็น PUA ไปแล้ว)
red = []
print(f"── {label}: {os.path.basename(f)}")
print(f"   ไทย {thai:,} อักขระ · สระอำ {amm} · พินทุ ฺ {pinthu} · นิคหิต ํ {nikkh} · IAST diacritics {diacr} · บรรทัดตาราง {tbl}")
if p1_bad:
    red.append("P1"); print(f"   🔴 P1 พินทุ→สระอุ: สระอุ+พยัญชนะ {p1_raw} จุด มากกว่าพินทุ {pinthu} — OCR เปลี่ยน ฺ เป็น ุ ทั้งไฟล์ (ปุตุต/ตสุส) ห้ามใช้เป็นแหล่งคำบาลี")
else:
    print(f"   ✓ P1 พินทุ {pinthu} ≥ สระอุ+พยัญชนะ {p1_raw} (ตัวเลขหลังนับคำถูกอย่าง พุทฺธ/ทุติยา ด้วย — ใช้เทียบอัตราส่วนเท่านั้น)")
print(f"   {'⚠ P2 นิคหิต→การันต์ (อห์/มย์) พบ '+str(p2)+' จุด' if p2 else '✓ P2 ไม่พบนิคหิตกลายเป็นการันต์'}")
print(f"   {'⚠ P3 โรมันปนอักษรไทย/ตัวเลข พบ '+str(p3)+' จุด — IAST เพี้ยน' if p3 else '✓ P3 โรมันสะอาด'}")
print(f"   {'⚠ P4 ไม่มี IAST diacritics เลย — ถ้าเอกสารมีโรมัน แปลว่าหาย' if (diacr == 0 and thai > 0) else '✓ P4 IAST '+str(diacr)}")
if short >= 50 and short > tbl * 20:   # อัตราส่วน: บรรทัดสั้นมากกว่าบรรทัดตาราง 20 เท่า (วัดจริง: OCR ตำรา 2,445:1 · text layer มีตารางจริงจึงไม่ติด)
    print(f"   ⚠ P5 บรรทัดสั้น ≤12 อักขระ {short} บรรทัด เทียบบรรทัดตาราง {tbl} — ตารางแตกเป็นบรรทัดเดี่ยว (OCR) ใช้ตารางจากอีกแหล่ง")
else:
    print(f"   ✓ P5 ตาราง {tbl} บรรทัด · บรรทัดสั้น {short}")
if thai >= 1000 and amm == 0:
    red.append("P6"); print("   🔴 P6 ไทย ≥1,000 แต่สระอำ = 0 — text layer พัง (ใช้ OCR สำหรับร้อยแก้ว)")
else:
    print(f"   ✓ P6 สระอำ {amm}")
if pua or orphan:
    red.append("P7"); print(f"   🔴 P7 อักขระ Private Use (U+F700-F8FF) {pua} ตัว · พินทุกำพร้า {orphan} จุด — ฟอนต์ใช้ glyph สำรองแทน ญ/ฐ ก่อนพินทุ และสระ/วรรณยุกต์ (ดู 09 §2.3 วิธีคืนอักขระ · scripts/pali_restore_pua.py)")
else:
    print("   ✓ P7 ไม่พบอักขระ Private Use / พินทุกำพร้า")
sys.exit(3 if red else 0)
PY
  [ $? -eq 3 ] && RC=3
  return 0
}

echo "═══ pali_check — ตรวจความเสียหายเฉพาะบาลี (P1-P7) ═══"
check_one "${1:?ใส่ไฟล์ text-layer.md}" "TEXT-LAYER" || exit 1
if [ -n "${2:-}" ]; then
  check_one "$2" "OCR" || exit 1
  echo
  echo "═══ คำแนะนำ (dual-source) ═══"
  echo "   คำบาลี/ตาราง/โรมัน IAST  → ใช้ TEXT-LAYER ($(basename "$1")) — ถ้า P7 ขึ้น ให้คืนอักขระตาม 09 §2.3 ก่อน"
  echo "   คำอธิบายไทยร้อยแก้ว       → ใช้ OCR ($(basename "$2"))"
  echo "   คำที่สองแหล่งขัดกัน       → เทียบรูปโรมัน/paradigm ก่อน · ตัดสินไม่ได้ = flag [?] ห้ามเดา"
fi
echo
if [ "$RC" -eq 3 ]; then
  echo "ผล: 🔴 พบความเสียหายที่ต้องประกอบ dual-source / คืนอักขระก่อนใช้ (exit 3)"
else
  echo "ผล: ✓ ไม่พบ 🔴 (exit 0) — ไฟล์ที่ประกอบเสร็จควรได้ผลนี้"
fi
exit "$RC"
