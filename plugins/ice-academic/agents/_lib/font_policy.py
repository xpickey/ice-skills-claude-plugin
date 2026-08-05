#!/usr/bin/env python3
"""
font_policy.py — SSOT ของนโยบายฟอนต์ไทย+ละติน (skill ice-doc-builder §3.0)
V01R07 | 2026.08.05
  V01R06 measure_slide_density + DENSE_FONT (PPTX สไลด์แน่น → Leelawadee ทั้งเด็ค)
  V01R07 (QA) ตัด 'กรม'/'สำนักงาน' ออกจาก RAIL_SIGNALS — 'กรม' เป็น substring ของ 'โปรแกรม'
         ทำให้เอกสารเอกชนโดนจัดเป็นราชการ (เจอจาก QA จริง)
  V01R03 fallbacks เป็น list + rail_fallbacks() · V01R04 resolve_font_policy (auto-correct)
  V01R05 infer_rail (เดารางจากชนิดเอกสาร)

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
    "private": {"font": "IBM Plex Sans Thai Looped", "size": 11,
                "fallbacks": ["Leelawadee UI"]},
    # ราชการ/TOR/e-GP: 16pt = ละติน 11-12pt (วัดได้ ×1.47)
    "govt":    {"font": "TH Sarabun New",            "size": 16,
                "fallbacks": ["Leelawadee UI"]},
}

# ⭐ ฟอนต์ที่ **แจกจ่ายให้ลูกค้าได้ถูกกฎหมาย** (SIL OFL · fsType 0x0000 Installable)
#   → นี่คือทางออกจริงของปัญหา "ลูกค้าไม่มีฟอนต์เรา" ที่ดีกว่าการยอมลดคุณภาพไปใช้ fallback
#   IBM Plex Sans Thai Looped ครบ 7 น้ำหนัก = 0.8 MB เท่านั้น · แนบไปกับชุดเอกสารได้เลย
#   ⛔ Leelawadee / Tahoma / TH Sarabun New = **แจกไม่ได้** (proprietary) — ได้แค่หวังว่าลูกค้ามี
DISTRIBUTABLE = {"IBM Plex Sans Thai Looped", "IBM Plex Sans Thai", "Noto Sans Thai"}

# ⭐ V01R03 (2026.08.04 · คำสั่ง user "Tahoma ไม่ค่อยสวย พยายามไม่ใช้")
#   fallback เปลี่ยนจาก string เดี่ยว → **ลำดับ** · ใช้เมื่อ "ฝังฟอนต์ไม่ได้ + คุมเครื่องปลายทางไม่ได้"
#   (= .xlsx เป็นหลัก · .docx ที่ส่งให้แก้ต่อ)
#
#   ความจริงที่ต้องยอมรับ: **ไม่มีฟอนต์ไทย "สวย" ตัวไหนที่มีทั้ง Windows และ macOS**
#     Sukhumvit Set  GAP 15.7% (ดีสุดที่วัดได้) · ยอดไม้โท 0.964 · มากับ macOS   ไม่มีบน Windows
#     Leelawadee UI  GAP 27.3%                  · ยอดไม้โท 0.743 · มากับ Windows ไม่มีบน macOS
#     Tahoma         GAP 23.1%                  · ยอดไม้โท 0.805 · มีทั้งคู่      แต่ออกแบบปี 1994
#   → Tahoma เคยเป็น fallback เพราะเป็น **ตัวเดียวที่ครอบ 2 OS** ไม่ใช่เพราะสวย
#   → ลำดับใหม่วางตามผู้รับจริงของงานนี้ (องค์กรไทย = Windows เป็นหลัก) และดัน Tahoma ไปท้ายสุด
#
#   🔴 ทางแก้ที่ถูกจริงคือ **เลิกพึ่ง fallback**: .xlsx ที่ส่งลูกค้า ให้แนบ PDF companion เสมอ (§3.2 E1)
#      PDF ฝังฟอนต์ 100% → สิ่งที่ลูกค้า "เห็น" ถูกต้องเสมอ ส่วน .xlsx คือฉบับให้แก้ต่อ
#      ซึ่งผู้แก้จะจัดรูปแบบเองอยู่แล้ว → fallback แทบไม่มีผลต่อความสวยที่ลูกค้าเห็น


# ─────────────────────────────────────────────────────────────────────────────
# ⭐ V01R05 (2026.08.04 · คำสั่ง user) — เดาราง "จากชนิดเอกสาร" ไม่ใช่ default ตัวเดียวทุกงาน
#   เดิม: rail = spec.get("rail", "private") → งาน TOR ราชการก็ได้ฟอนต์เอกชนไปเงียบ ๆ
#   ตอนนี้: อ่านสัญญาณจาก path/ชื่อไฟล์/เนื้อ spec → เลือกรางให้ + **ประกาศเสมอว่าเดาจากอะไร**
#   (ประกาศสำคัญพอ ๆ กับการเดาถูก — เดาผิดแล้วเงียบ คือสิ่งที่ทำให้เคส PWA/VFIN หลุดมาตลอด)
# ─────────────────────────────────────────────────────────────────────────────
RAIL_SIGNALS = {
    # ⚠ V01R07 (QA 2026.08.05): คำบ่งชี้ต้องเป็นคำที่ชนกับบริบทเอกชนไม่ได้
    #   ตัดออก: "กรม" (เป็น substring ของ "โปรแกรม" → เอกสารเอกชนที่มีคำว่าโปรแกรมโดนจัดเป็น
    #   ราชการทั้งหมด — เจอจาก QA จริง) · "สำนักงาน" (คำสามัญ — สำนักงานใหญ่/สำนักงานขาย ของเอกชน)
    #   ภาษาไทยไม่มีวรรคคั่นคำ จึงเช็ค word boundary ไม่ได้ → ใช้ได้เฉพาะคำยาวเฉพาะทาง
    "govt": ["tor", "ทีโออาร์", "e-gp", "egp", "ประกวดราคา", "สอบราคา", "จัดซื้อจัดจ้าง",
             "ราชการ", "รัฐวิสาหกิจ", "พัสดุ", "ข้อกำหนดและขอบเขต", "ประกาศเชิญชวน",
             "กระทรวง", "การประปา", "การไฟฟ้า", "เทศบาล", "องค์การบริหารส่วน"],
    "academic": ["วิทยานิพนธ์", "ดุษฎีนิพนธ์", "สารนิพนธ์", "บทความวิชาการ", "บทความวิจัย",
                 "มจร", "วารสาร", "thesis", "dissertation", "journal", "abstract",
                 "บรรณานุกรม", "งานวิจัย"],
}


def infer_rail(spec=None, out_path="", default="private"):
    """เดารางจากชนิดเอกสาร · คืน (rail, reason)

    ลำดับสัญญาณ (บนชนะล่าง):
      ① spec["rail"] ระบุตรง ๆ            ② spec["doc_type"]
      ③ คำในชื่อไฟล์/path ปลายทาง          ④ คำในหัวเรื่อง/ชื่อชีทของ spec
      ⑤ ไม่มีสัญญาณ → default (private) — แต่ยัง**ประกาศ**ว่าใช้ค่าเริ่มต้นเพราะไม่พบสัญญาณ
    """
    spec = spec or {}
    if spec.get("rail") in RAILS:
        return spec["rail"], f"spec ระบุ rail='{spec['rail']}' ตรง ๆ"

    dt = (spec.get("doc_type") or "").lower()
    hay_parts = [os.path.basename(out_path), out_path, dt,
                 str(spec.get("title", "")), str(spec.get("name", ""))]
    for sh in spec.get("sheets", []) or []:
        hay_parts.append(str(sh.get("name", "")))
        hay_parts += [str(h) for h in (sh.get("headers") or [])[:8]]
    hay = " ".join(hay_parts).lower()

    for rail, words in RAIL_SIGNALS.items():
        if rail not in RAILS:
            continue
        hit = [w for w in words if w in hay]
        if hit:
            return rail, f"พบคำบ่งชี้ {hit[:3]} → ราง '{rail}'"

    # academic ไม่ใช่ราง แต่มีข้อบังคับของตัวเอง — เตือนให้ประกาศ override แทนการเดาเอง
    acad = [w for w in RAIL_SIGNALS["academic"] if w in hay]
    if acad:
        return default, (f"⚠ พบคำบ่งชี้งานวิชาการ {acad[:3]} — ข้อบังคับ มจร./วารสาร มักบังคับ "
                         f"'TH SarabunPSK' 16pt ซึ่งอยู่นอกนโยบายราง "
                         f"→ ถ้าใช่ ให้ใส่ \"font\":\"TH SarabunPSK\" + "
                         f"\"font_override_reason\":\"ข้อบังคับวารสาร/มหาวิทยาลัย\" ใน spec")
    return default, f"ไม่พบสัญญาณชนิดเอกสาร → ใช้ค่าเริ่มต้น '{default}'"


# ─────────────────────────────────────────────────────────────────────────────
# ⭐ V01R06 (2026.08.05 · คำสั่ง user) — PPTX สไลด์แน่น → Leelawadee ทั้งเอกสาร
#
#   ทำไม: ยอดวรรณยุกต์ Leelawadee = 0.737 em · IBM Plex Looped = 0.924 em
#   เมื่อสไลด์ต้องบีบบรรทัด (ข้อความเยอะ/กล่องเล็ก/normAutofit ย่อ) ตัวที่ยอดสูงกว่าจะ**ชนก่อน**
#   → เลือกตัวที่ยอดเตี้ยสุดเพื่อซื้อที่ว่างแนวตั้ง แลกกับ GAP ที่กว้างขึ้น (27.3% vs 18.9%)
#   PPTX **ฝังฟอนต์ได้** จึงไม่ต้องห่วงว่าเครื่องผู้รับมี Leelawadee หรือไม่
#
#   ⭐ สลับ **ทั้งเด็ค** ไม่ใช่ทีละสไลด์ — §3.0 ③ APPROVED SET เดียวต่อชุดเอกสาร
#      (สไลด์เดียวในเด็คใช้ฟอนต์ต่าง = ผู้อ่านเห็นความไม่สม่ำเสมอทันที)
# ─────────────────────────────────────────────────────────────────────────────
DENSE_FONT = "Leelawadee"          # ตัวธรรมดา (ผู้ใช้ติดตั้งเอง /Library/Fonts/leelawad.ttf)
DENSE_CHARS_PER_SLIDE = 400        # สไลด์ 16:9 อ่านสบาย ≈ 6 bullet × 60 ตัว ≈ 360
DENSE_LINES_PER_SLIDE = 8          # เกินนี้ต้องย่อ font หรือบีบ line-height
DENSE_TABLE_CELLS = 40             # ตารางคือ layout ที่แน่นที่สุดเสมอ


def measure_slide_density(slides):
    """คืน (is_dense, reason) — วัดจาก spec ก่อน build · ไม่เดา ใช้ตัวเลขจริง"""
    worst = (0, 0, 0, -1)          # chars, lines, cells, slide_index
    for i, sl in enumerate(slides or []):
        texts, lines, cells = [], 0, 0
        for k in ("title", "subtitle"):
            if sl.get(k):
                texts.append(str(sl[k]))
        for k in ("bullets", "left", "right"):
            items = sl.get(k) or []
            texts += [str(x) for x in items]
            lines += len(items)
        if sl.get("headers") or sl.get("rows"):
            hdr = sl.get("headers") or []
            rows = sl.get("rows") or []
            texts += [str(h) for h in hdr]
            for r in rows:
                texts += [str(c) for c in (r or [])]
            cells = len(hdr) + sum(len(r or []) for r in rows)
            lines += len(rows)
        for kp in sl.get("kpis") or []:
            texts += [str(kp.get(x, "")) for x in ("label", "value", "delta")]
            lines += 1
        chars = sum(len(t) for t in texts)
        if (chars, lines, cells) > worst[:3]:
            worst = (chars, lines, cells, i)

    chars, lines, cells, idx = worst
    hits = []
    if chars > DENSE_CHARS_PER_SLIDE:
        hits.append(f"{chars} ตัวอักษร (เกณฑ์ >{DENSE_CHARS_PER_SLIDE})")
    if lines > DENSE_LINES_PER_SLIDE:
        hits.append(f"{lines} บรรทัด (เกณฑ์ >{DENSE_LINES_PER_SLIDE})")
    if cells > DENSE_TABLE_CELLS:
        hits.append(f"ตาราง {cells} ช่อง (เกณฑ์ >{DENSE_TABLE_CELLS})")
    if hits:
        return True, f"สไลด์ที่ {idx + 1} แน่นสุด: " + " · ".join(hits)
    return False, f"สไลด์แน่นสุด = {chars} ตัวอักษร / {lines} บรรทัด — ยังไม่ถึงเกณฑ์บีบ"


def resolve_font_policy(font, rail, spec=None, fams=None):
    """⭐ ด่านนโยบาย **ก่อน build** — เรียกทันทีหลัง resolve ชื่อฟอนต์ ก่อนเขียนไฟล์ใด ๆ

    คืน (font_ที่จะใช้จริง, notices, allow_fonts_สำหรับ audit)

    ปรัชญา (คำสั่ง user 2026.08.04 "ให้ทำงานถูกต้อง ไม่ต้อง fail — เสียเวลาและ token"):
      **แก้ให้อัตโนมัติแล้วแจ้ง ดีกว่าหยุดแล้วให้คนไปแก้ spec**
      เพราะเมื่อฟอนต์ผิดนโยบาย คำตอบที่ถูกมีอยู่ **ตัวเดียวชัดเจน** = ฟอนต์ราง
      การ fail จึงเป็นแค่การผลักงานที่ตัดสินใจได้เองกลับไปให้คน = เสียรอบเปล่า
      ⚠ แต่ **ห้ามแก้เงียบ** — ทุกการเปลี่ยนต้องพิมพ์บอกว่าเปลี่ยนอะไร จากอะไร เพราะอะไร

    บทเรียนที่หล่อกฎนี้ (VFIN NetSuite proposal 2026.08.04):
      spec ระบุ Sarabun → build ผ่าน → self-audit ขึ้น PASS (เพราะถูกยื่นเฉลย allow_fonts={FONT})
      → ไปเจอ FAIL ตอนรัน audit_fonts.py แยกทีหลัง → ย้อนแก้ spec → build ใหม่ = เสีย 1 รอบเต็ม

    override ได้ ต้องประกาศเหตุผล: spec["font_override_reason"] = "TOR ข้อ 5.1 บังคับ"
      (เจตนา: ออกนอกนโยบายได้ แต่ต้องมีร่องรอย ไม่ใช่ค่า default ที่ลืมแก้)
    """
    spec = spec or {}
    notices = []
    allow = set(spec.get("allow_fonts") or ())
    reason = spec.get("font_override_reason")

    if reason:                       # ผู้ใช้ตัดสินใจเองแล้วโดยมีเหตุผล → เคารพ
        allow.add(font)
        notices.append(f"ℹ ใช้ '{font}' นอกนโยบายตามที่ประกาศไว้: {reason}")
        rep = check_fonts({font}, rail=rail, allow_fonts=allow, fams=fams)
        for n, why in rep["blacklisted"]:
            notices.append(f"🔴 เตือน: '{n}' อยู่ใน BLACKLIST — {why} "
                           f"(ยังใช้ต่อตามที่ท่านระบุ แต่ผลกระทบนี้แก้ไม่ได้ด้วยการจัดรูปแบบ)")
        return font, notices, allow

    rep = check_fonts({font}, rail=rail, allow_fonts=allow, fams=fams)
    if not rep["fails"]:
        return font, notices, allow

    # ── ผิดนโยบาย และไม่ได้ประกาศเหตุผล → แก้ให้เป็นฟอนต์ราง แล้วบอกให้ชัด
    target = RAILS[rail]["font"]
    why = []
    if rep["retired"]:
        why.append(f"'{font}' ถูกถอดออกจากตัวเลือกแล้ว ({RETIRED.get(font, '').split('·')[0].strip()})")
    if rep["blacklisted"]:
        why.append(f"'{font}' อยู่ใน BLACKLIST ({rep['blacklisted'][0][1]})")
    if rep["unresolvable"]:
        near = sorted(f for f in (fams or ()) if font.split()[0].lower() in f.lower())[:4]
        why.append(f"ไม่มี family ชื่อ '{font}' ติดตั้งอยู่จริง"
                   + (f" (ใกล้เคียง: {near})" if near else ""))
    if rep["off_rail"] and not why:
        why.append(f"'{font}' ไม่ใช่ฟอนต์ของ rail='{rail}' และไม่อยู่ในตัวเลือกที่อนุมัติ")

    notices.append(f"⚙ เปลี่ยนฟอนต์อัตโนมัติ: '{font}' → '{target}'")
    for w in why:
        notices.append(f"   เหตุผล: {w}")
    notices.append(f"   ทางเลือกอื่นที่อนุมัติ: {sorted(APPROVED_ALT)}")
    notices.append(f"   ถ้าตั้งใจใช้ '{font}' จริง (TOR/วารสาร/แบรนด์ลูกค้า) "
                   f"→ ใส่ \"font_override_reason\" ใน spec แล้ว build ใหม่")
    return target, notices, allow


def rail_fallbacks(rail: str) -> list:
    """คืนลำดับ fallback (ตัวแรก = แนะนำสุด) — รองรับทั้ง key เก่า 'fallback' และใหม่ 'fallbacks'"""
    r = RAILS[rail]
    fb = r.get("fallbacks") or [r.get("fallback")]
    return [f for f in fb if f]


def rail_fallback(rail: str) -> str:
    """ตัวเดียวสำหรับที่ที่ใส่ได้ชื่อเดียว (เซลล์ Excel) — ตัวแรกของลำดับ"""
    return rail_fallbacks(rail)[0]

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
    ok = ({RAILS[rail]["font"], *rail_fallbacks(rail)}
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
                     f"fallback {rail_fallbacks(rail)} · ตัวเลือกอนุมัติ {alt}): "
                     f"{rep['off_rail']} → {EXTERNAL_MANDATE_NOTE}")
    rep["fails"] = fails
    return rep
