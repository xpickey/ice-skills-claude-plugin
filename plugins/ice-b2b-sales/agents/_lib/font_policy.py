#!/usr/bin/env python3
"""
font_policy.py — SSOT ของนโยบายฟอนต์ไทย+ละติน (skill ice-doc-builder §3.0)
V01R02 | 2026.08.04

V01R02 (คำสั่ง user):
  +APPROVED_ALT — ตัวเลือกที่อนุมัติเพิ่ม เลือกใช้ได้โดยไม่ต้อง --allow-font:
     Leelawadee / Leelawadee UI / Leelawadee UI Semilight
  +RETIRED      — Sarabun ถอดออกจากตัวเลือก (V5) · ⚠ คนละตัวกับ TH Sarabun New / TH SarabunPSK
  default ยังเป็น IBM Plex Sans Thai Looped เพราะวัดแล้ว GAP ไทย-ละตินน้อยกว่า (18.9% vs 27.3%)

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

# ─────────────────────────────────────────────────────────────────────────────
# ⭐ V01R02 (2026.08.04) — ตัวเลือกที่อนุมัติเพิ่ม + ตัวที่ถอดออก
#
# วัดจริงบนเครื่องนี้ (ก/H = ความสูงตัว ก เทียบ cap H **ในฟอนต์เดียวกัน**
# → ยิ่งใกล้ 1.000 ยิ่งไม่ต้องชดเชยขนาดเมื่อไทยปนอังกฤษในกล่องเดียว):
#
#   family                      ก/H     ยอดไม้โท   GAP ไทยเล็กกว่าละติน
#   IBM Plex Sans Thai Looped   0.811     0.924     18.9%   ← ดีสุด = default (ราง private)
#   IBM Plex Sans Thai          0.799     0.866     20.1%
#   Noto Sans Thai              0.782     0.840     21.8%
#   Tahoma                      0.769     0.805     23.1%   ← fallback
#   Leelawadee                  0.727     0.737     27.3%   ← ตัวเลือกอนุมัติ
#   Leelawadee UI               0.727     0.743     27.3%   ← สัดส่วนเท่าตัวธรรมดาเป๊ะ
#   Sarabun                     0.837     0.957     16.3%   ← ถอดออก (ดูด้านล่าง)
#
# ⭐ การตัดสิน default (คำสั่ง user 2026.08.04 "GAP ดีกว่าเอาตัวนั้น"):
#   IBM Plex Sans Thai Looped (18.9%) ชนะ Leelawadee (27.3%) → คงเป็นฟอนต์รางเอกชนเหมือนเดิม
# ─────────────────────────────────────────────────────────────────────────────

# ตัวเลือกที่อนุมัติแล้ว — เลือกใช้ได้โดยไม่ต้อง --allow-font (แต่ default ยังเป็นฟอนต์ราง)
_LEELA_NOTE = (
    "ไทย+อังกฤษในตัวเดียว · ⭐ จุดแข็ง: ยอดวรรณยุกต์เตี้ยที่สุดในกลุ่ม (~0.74 em) "
    "= ปลอดภัยสุดเมื่อความสูงแถว/บรรทัดถูกบีบ · ติดมากับ Windows ทุกเครื่อง "
    "(fsType 0x0008 = embed ได้ถูกลิขสิทธิ์) "
    "· ⚠ แลกด้วย GAP 27.3% (ไทยเล็กกว่าละตินมากสุดในกลุ่ม) → ถ้าไทยปนอังกฤษในบรรทัดเดียว "
    "ต้องเพิ่ม pt ให้ไทย ไม่งั้นไทยจะดูเล็ก — งานทั่วไปใช้ฟอนต์รางดีกว่า"
)
APPROVED_ALT = {
    "Leelawadee":              _LEELA_NOTE,
    "Leelawadee UI":           _LEELA_NOTE + " · รุ่น UI (hinting สำหรับหน้าจอ)",
    "Leelawadee UI Semilight": "น้ำหนักบางของ Leelawadee UI — metric เดียวกันทุกค่า",
}

# ⛔ ถอดออกจากตัวเลือก (คำสั่ง user 2026.08.04) — ไม่ใช่ blacklist (ไม่ได้ทำลายชั้นข้อความ)
#    แต่ห้ามเลือกใช้ในงานใหม่ · ไฟล์เก่าที่ใช้อยู่ = rebuild ตอนมี revision ถัดไป
RETIRED = {
    "Sarabun": ("user ถอดออก 2026.08.04 — ยอดวรรณยุกต์ 0.957 em สูงสุดในกลุ่ม "
                "+ ขอที่ว่างแนวตั้ง 1.286 em มากสุด → โดนบีบ/ชนหนักที่สุดเมื่อพื้นที่ไม่พอ "
                "(ผู้ใช้ทดสอบสายตาเองแล้วไม่ผ่าน) · ⚠ คนละตัวกับ 'TH Sarabun New' (รางราชการ) "
                "และ 'TH SarabunPSK' (ข้อบังคับ มจร.) — สองตัวนั้นยังใช้ได้ตามปกติ"),
    "Sarabun Light": "ตระกูลเดียวกับ Sarabun ที่ถอดออก",
    "Sarabun Medium": "ตระกูลเดียวกับ Sarabun ที่ถอดออก",
    "Sarabun SemiBold": "ตระกูลเดียวกับ Sarabun ที่ถอดออก",
    "Sarabun ExtraBold": "ตระกูลเดียวกับ Sarabun ที่ถอดออก",
    "Sarabun Thin": "ตระกูลเดียวกับ Sarabun ที่ถอดออก",
    "Sarabun ExtraLight": "ตระกูลเดียวกับ Sarabun ที่ถอดออก",
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

    # V01R02: ตัวเลือกที่อนุมัติแล้ว (APPROVED_ALT) ผ่านได้โดยไม่ต้อง --allow-font
    ok = ({RAILS[rail]["font"], RAILS[rail]["fallback"]}
          | set(APPROVED_ALT) | allow_fonts)
    cand = {n for n in fonts if n not in LATIN_ONLY}
    rep["off_rail"] = sorted(cand - ok)
    # แยก "ถอดออกจากตัวเลือก" ออกจาก off-rail ทั่วไป — ผู้อ่านต้องรู้ว่าทำไมถึงห้าม
    rep["retired"] = sorted((cand & set(RETIRED)) - allow_fonts)
    rep["off_rail"] = [n for n in rep["off_rail"] if n not in rep["retired"]]
    # ใช้ตัวเลือกอนุมัติ แต่ไม่ใช่ฟอนต์ราง → แจ้งเตือน ไม่ fail
    rep["alt_used"] = sorted((cand & set(APPROVED_ALT)) - {RAILS[rail]["font"]})

    fails = []
    if rep["unresolvable"]:
        fails.append(f"V1 FONT-NAME ไม่ resolve: {rep['unresolvable']}")
    if rep["blacklisted"]:
        fails.append(f"V2 BLACKLIST: {[n for n, _ in rep['blacklisted']]}")
    if rep["retired"]:
        for n in rep["retired"]:
            fails.append(f"V5 ฟอนต์ที่ถอดออกจากตัวเลือกแล้ว: '{n}' — {RETIRED[n]}")
    if rep["off_rail"]:
        alt = ", ".join(f"'{a}'" for a in sorted(APPROVED_ALT))
        fails.append(f"V4 ผิดราง '{rail}' (ต้องเป็น '{RAILS[rail]['font']}' · fallback "
                     f"'{RAILS[rail]['fallback']}' · ตัวเลือกอนุมัติ {alt}): "
                     f"{rep['off_rail']} → {EXTERNAL_MANDATE_NOTE}")
    rep["fails"] = fails
    return rep
