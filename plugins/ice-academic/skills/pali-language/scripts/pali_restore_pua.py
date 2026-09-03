#!/usr/bin/env python3
"""pali_restore_pua.py — คืนอักขระไทยที่ text layer ของ PDF ฝังเป็นรหัสเขต Private Use (U+F700-F71B)

ใช้:  python3 ~/.claude/skills/pali-language/scripts/pali_restore_pua.py <in.md> -o <out.md>
      python3 pali_restore_pua.py <in.md> --report        # ดูสถิติอย่างเดียว ไม่เขียนไฟล์

ที่มา (references/09-document-ingestion.md §2.3): ฟอนต์ไทยเก็บ glyph สำรอง (ญ/ฐ ตัดหางเมื่อมีพินทุ · สระ-วรรณยุกต์
เลื่อนตำแหน่ง) ไว้ในเขต PUA และ PDF บางไฟล์ฝังรหัสนั้นแทนอักขระจริง — ตาราง MAP ด้านล่าง**ได้จากการจับคู่คำ text layer
กับ OCR ของเอกสารเดียวกันแบบตำแหน่งต่อตำแหน่ง** (ตำราอบรมบาลี 2026.09.03: คำที่จับคู่ได้เอกลักษณ์ 1,955 คำ ทุกรหัสใน
ตารางตรง 100% ยกเว้น U+F70F 93%) และรหัสพินทุ/นิคหิตที่ OCR ยืนยันไม่ได้ ตรวจกับ paradigm ในไฟล์ 02/04 แทน
รหัสที่ไม่มีหลักฐานพอ (ตัวอย่าง < 10) **ไม่แปลง** — คงไว้และรายงานให้ตรวจด้วยตา (กฎ R2: ห้ามซ่อมด้วยการเดา)
skill: pali-language V01R03 · 2026.09.04 (R03: pointer → 09 §2.3 ตาม QA อริส PALI-012)
"""
import sys, re, argparse, collections, unicodedata

# รหัส → อักขระ · (จำนวนหลักฐาน, วิธียืนยัน)
MAP = {
    0xF701: ("ิ", "52 คำ · จับคู่ OCR 100%"),
    0xF702: ("ี", "11 คำ · จับคู่ OCR 100%"),
    0xF705: ("่", "10 คำ · จับคู่ OCR 100%"),
    0xF70A: ("่", "1,108 คำ · จับคู่ OCR 100%"),
    0xF70B: ("้", "1,289 คำ · จับคู่ OCR 100%"),
    0xF70E: ("์", "485 คำ · จับคู่ OCR 100% (เช่น คัมภีร์ ลิงค์)"),
    0xF70F: ("ญ", "14 คำ · จับคู่ OCR 93% + paradigm: ปญฺญา วิญฺญาณ ปญฺจมี รญฺญา"),
    0xF710: ("ั", "82 คำ · จับคู่ OCR 100%"),
    0xF712: ("็", "366 คำ · จับคู่ OCR 100%"),
    0xF71A: ("ฺ", "96 จุด · ตรวจกับ paradigm: เสฏฺฐี วฏฺฏ ปฏฺฐาย (02 §5.x/07 §3)"),
    0xF71B: ("ํ", "17 จุด · ตรวจกับ paradigm: เอยฺยุํ อวทตฺถุํ (04 §3.3/3.5)"),
}

def restore(text):
    out, done, left = [], collections.Counter(), collections.Counter()
    for ch in text:
        cp = ord(ch)
        if cp in MAP:
            out.append(MAP[cp][0]); done[cp] += 1
        elif 0xF700 <= cp <= 0xF8FF:
            out.append(ch); left[cp] += 1
        else:
            out.append(ch)
    return unicodedata.normalize("NFC", "".join(out)), done, left

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("infile"); ap.add_argument("-o", "--out"); ap.add_argument("--report", action="store_true")
    a = ap.parse_args()
    t = open(a.infile, encoding="utf-8").read()
    r, done, left = restore(t)
    orphan_before = len(re.findall(r"(?<![ก-ฮ])ฺ", t)); orphan_after = len(re.findall(r"(?<![ก-ฮ])ฺ", r))
    print("═══ pali_restore_pua ═══")
    print(f"   คืนอักขระ {sum(done.values()):,} ตัว จาก {len(done)} รหัส: " + " ".join(f"{hex(k)}→{MAP[k][0]}×{v}" for k, v in sorted(done.items())))
    print(f"   ญฺ: {t.count('ญฺ')} → {r.count('ญฺ')} · พินทุกำพร้า: {orphan_before} → {orphan_after}")
    if left:
        print(f"   ⚠ PUA ที่ไม่มี mapping ยืนยัน คงไว้ {sum(left.values())} ตัว: " + " ".join(f"{hex(k)}×{v}" for k, v in sorted(left.items())) + " — ตรวจด้วยตา/เทียบ OCR แล้วแก้เอง ห้ามเดา")
    if a.report or not a.out:
        return 0
    open(a.out, "w", encoding="utf-8").write(r)
    print(f"   เขียน: {a.out} (NFC)")
    return 0

if __name__ == "__main__":
    sys.exit(main())
