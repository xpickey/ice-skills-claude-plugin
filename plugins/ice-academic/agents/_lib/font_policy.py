#!/usr/bin/env python3
"""
font_policy.py — SSOT ของนโยบายฟอนต์ไทย+ละติน (skill ice-doc-builder §3.0)
V01R01 | 2026.08.04

ทำไมต้องแยกไฟล์นี้ออกมา (บทเรียน 2026.08.04):
  นโยบายเคยอยู่ใน build_xlsx.py ตัวเดียว → build script ฟอร์แมตอื่น (pptx/docx/dashboard/html)
  และ build script เขียนมือรายโปรเจกต์ **hard-code ชื่อฟอนต์เอง** แล้ว bypass นโยบายทั้งตาราง
  ผลจริง: PWA TCO-Breakdown V01R22 build วันที่นโยบายบังคับใช้อยู่แล้ว ยังออกมาเป็น Sarabun
  และ validator ขึ้น ✅ PASS — **user เป็นคนจับได้ ไม่ใช่ระบบ**

⭐ กติกา: build script ทุกตัว (รวมที่เขียนมือรายโปรเจกต์) ต้อง
     from font_policy import RAILS
     FONT = RAILS[rail]["font"]
   ห้าม hard-code ชื่อฟอนต์เป็น string literal เด็ดขาด
"""
import os, re, glob

# ─────────────────────────────────────────────────────────────────────────────
# §3.0 FONT POLICY — 2 ราง (LOCKED โดย user 2026.07.31)
# ─────────────────────────────────────────────────────────────────────────────
RAILS = {
    # เอกชน: ไทย=อังกฤษ ไม่บวก pt (cap 0.698 em — ละตินอยู่ในตัวเดียวกัน)
    "private": {"font": "IBM Plex Sans Thai Looped", "size": 11, "fallback": "Tahoma"},
    # ราชการ/TOR/e-GP: 16pt = ละติน 11-12pt (วัดได้ ×1.47)
    "govt":    {"font": "TH Sarabun New",            "size": 16, "fallback": "Tahoma"},
}

# ⚠ ข้อยกเว้นที่ถูกต้อง — "ผู้บังคับภายนอก" ชนะนโยบายเราเสมอ ห้ามไป "แก้" ให้ตรงราง:
#   • TOR / e-GP ระบุฟอนต์ไว้            → ทำตาม TOR
#   • ข้อบังคับวารสาร/มหาวิทยาลัย        → เช่น มจร. บังคับ TH SarabunPSK ตลอดเล่ม
#   • ไฟล์ที่ลูกค้า/ผู้ขายส่งมา            → ไม่ใช่ของเราสร้าง ไม่อยู่ใต้นโยบายเรา
EXTERNAL_MANDATE_NOTE = ("TOR/e-GP · ข้อบังคับวารสาร-มหาวิทยาลัย · ไฟล์ที่รับมาจากภายนอก "
                         "= อยู่นอกนโยบายนี้ ใช้ --allow-font")

# §3.0 BLACKLIST — เหตุผลรายตัวอยู่ใน skill ice-doc-builder §3.0
BLACKLIST_PATTERNS = [
    (r"^TH Sarabun ?IT", "แปลงเลขอารบิก→เลขไทยเงียบ ๆ + ชื่อชนกับ PSK + digit width +24%"),
    (r"^Angsana",   "ทำลาย สระอำ ในชั้นข้อความ 100% (copy-paste/ค้นหา/index พัง)"),
    (r"^Cordia",    "ทำลาย สระอำ 100% · ไม่มีบน macOS"),
    (r"^Browallia", "ทำลาย สระอำ 100% · ไม่มีบน macOS"),
    (r"^Eucrosia",  "ตระกูล UPC เดียวกัน"),
    (r"^Jasmine",   "ตระกูล UPC เดียวกัน · ไม่ได้ติดตั้ง"),
    (r"^Microsoft Sans Serif", "ไม่มี Bold จริง + ที่ว่างวรรณยุกต์ = 0"),
]
LATIN_ONLY = {"Calibri", "Aptos", "Arial", "Cambria", "Times New Roman", "Helvetica"}

THAI_RE = re.compile(r"[฀-๿]")


def has_thai(v) -> bool:
    return isinstance(v, str) and bool(THAI_RE.search(v))


def installed_families() -> set:
    """V1 — family name จริงจาก name table (nameID 1) ของฟอนต์ที่ติดตั้งบนเครื่องนี้"""
    fams = set()
    try:
        from fontTools.ttLib import TTFont
    except ImportError:
        return fams          # ไม่มี fontTools → V1 ข้าม (ต้องรายงานว่า "ข้าม" ไม่ใช่ "ผ่าน")
    roots = ["/System/Library/Fonts", "/System/Library/Fonts/Supplemental",
             "/Library/Fonts", os.path.expanduser("~/Library/Fonts")]
    for root in roots:
        for ext in ("ttf", "otf", "ttc"):
            for p in glob.glob(f"{root}/**/*.{ext}", recursive=True):
                try:
                    n = TTFont(p, fontNumber=0, lazy=True)["name"].getDebugName(1)
                    if n:
                        fams.add(n)
                except Exception:
                    pass
    return fams


def blacklist_hit(name: str):
    for pat, reason in BLACKLIST_PATTERNS:
        if re.match(pat, name or "", re.I):
            return reason
    return None


def check_fonts(fonts, rail: str = "private", allow_fonts=None, fams=None) -> dict:
    """V1 + V2 + V4 รวมจุดเดียว — ใช้ได้กับทุกฟอร์แมต (xlsx/pptx/docx/html)

    fonts = ชื่อฟอนต์ที่ "ถูกใช้กับข้อความไทยจริง" (ไม่ใช่ที่ประกาศไว้ใน theme table)
    คืน dict: unresolvable / blacklisted / off_rail / fails / v1_skipped
    """
    allow_fonts = set(allow_fonts or ())
    if rail not in RAILS:
        raise ValueError(f"rail ต้องเป็น {'|'.join(RAILS)} (ได้: {rail})")
    if fams is None:
        fams = installed_families()
    fonts = {f for f in fonts if f}

    rep = {"fonts_used": sorted(fonts), "rail": rail,
           "unresolvable": [], "blacklisted": [], "off_rail": [],
           "v1_skipped": not bool(fams)}

    for n in sorted(fonts):
        why = blacklist_hit(n)
        if why:
            rep["blacklisted"].append((n, why))
        if fams and n not in fams and n not in LATIN_ONLY:
            rep["unresolvable"].append(n)

    ok = {RAILS[rail]["font"], RAILS[rail]["fallback"]} | allow_fonts
    rep["off_rail"] = sorted({n for n in fonts if n not in LATIN_ONLY} - ok)

    fails = []
    if rep["unresolvable"]:
        fails.append(f"V1 FONT-NAME ไม่ resolve: {rep['unresolvable']}")
    if rep["blacklisted"]:
        fails.append(f"V2 BLACKLIST: {[n for n, _ in rep['blacklisted']]}")
    if rep["off_rail"]:
        fails.append(f"V4 ผิดราง '{rail}' (ต้องเป็น '{RAILS[rail]['font']}' หรือ fallback "
                     f"'{RAILS[rail]['fallback']}'): {rep['off_rail']} → {EXTERNAL_MANDATE_NOTE}")
    rep["fails"] = fails
    return rep
