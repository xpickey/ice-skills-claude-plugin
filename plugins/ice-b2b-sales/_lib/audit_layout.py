#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ตัวตรวจเลย์เอาต์สไลด์อัตโนมัติ — audit_layout.py (V01R02 · 2026.09.06)

V01R02 (แก้ตามข้อสังเกตของอริสจากการซ้อมจริง Pass 6):
  + หัวเรื่องล้นกล่อง (เตือน ไม่ใช่ไม่ผ่าน): วัดความกว้างข้อความหัวเรื่องด้วยไฟล์ฟอนต์จริงของราง (font_policy.font_file_for + Pillow)
    เทียบกับความกว้างกล่อง = จำนวนบรรทัดที่ต้องใช้ · ความสูงบรรทัดจาก ascender+descender ของฟอนต์ เทียบความสูงกล่อง = จำนวนบรรทัดที่รับได้
    → ต้องใช้มากกว่ารับได้ = เตือน "หัวเรื่องประมาณ N บรรทัด กล่องรับได้ M" (ตัวตรวจเดิมจับได้เฉพาะกล่องสองกล่องซ้อนกัน ไม่เห็นบรรทัดทับกันในกล่องเดียว)
    ขนาดฟอนต์อ่านจาก run → paragraph → placeholder ของ layout → master ตามลำดับสืบทอด · หาไฟล์ฟอนต์ไม่ได้ = ประมาณด้วย 0.55 em ต่อตัวอักษรและบอกว่าเป็นค่าประมาณ
  + ข้อความในแถบท้ายหน้าและเลขหน้า (placeholder ftr/sldNum/dt) ไม่นับเข้างบคำของหน้า — เป็นส่วนประกอบของแม่แบบ ไม่ใช่เนื้อหาที่ผู้ฟังอ่าน
    (ตั้งแต่ builder ใส่รหัสรุ่น+วันที่ลง footer ทุกหน้า งบคำของทุกหน้าถูกกินไป 2 คำโดยไม่มีเนื้อหาเพิ่ม)

ตรวจไฟล์ .pptx ด้วยเครื่องก่อนส่งให้ผู้ตรวจคุณภาพ (อริส) เพื่อให้รอบตรวจของคนใช้กับเนื้อหาและตรรกะเท่านั้น
กฎที่ตรวจมาจาก "แนวทางการทำสไลด์ของ iCE" (b2b-slide-designer/references/pptx-design-doctrine.md):
  ข้อ 1/5  ข้อความต่อหน้าไม่เกินงบคำของโหมด (เอกสารอ่านเอง 75 คำ · นำเสนอสด 25 คำ) → เกิน = เตือน · เกินมาก = ไม่ผ่าน
  ข้อ 2    หน้าเนื้อหาต้องมีภาพหรือ icon อย่างน้อยหนึ่งชิ้น → ไม่มี = ไม่ผ่าน
  ข้อ 5    วลี "วัตถุประสงค์ของหน้า/สไลด์" หรือ "slide objective" ห้ามปรากฏบนสไลด์ → พบ = ไม่ผ่าน (หัวข้อ "Objective & Scope" ของเอกสารไม่นับ)
  เลย์เอาต์ กล่องข้อความล้นขอบสไลด์ = ไม่ผ่าน · กล่องข้อความสองกล่องซ้อนกัน = ไม่ผ่าน
  จำนวนหน้า เกินเพดานของโหมด (เอกสาร 30 · นำเสนอ 20) = เตือน

วิธีใช้:  python3 ~/.claude/agents/_lib/audit_layout.py FILE.pptx [--mode document|presenter] [--json]
ผลลัพธ์:  ตารางรายหน้า + สรุป · exit 0 = ผ่าน/เตือน · exit 2 = ไม่ผ่าน (มีข้อที่ต้องแก้ก่อนส่งตรวจ)
หมายเหตุ: การนับคำภาษาไทยใช้ค่าประมาณ 4.5 ตัวอักษรต่อคำ · ภาพ = รูปภาพหรือกลุ่มรูปทรงที่ไม่มีข้อความ (icon ที่วาด)
"""
import argparse
import json
import re
import sys

try:
    from pptx import Presentation
    from pptx.enum.shapes import MSO_SHAPE_TYPE
except ImportError:
    print("ต้องติดตั้ง python-pptx ก่อน: pip install python-pptx")
    sys.exit(3)

import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
try:
    from font_policy import RAILS, font_file_for
except Exception:
    RAILS, font_file_for = {"private": {"font": ""}}, lambda fam: None

BUDGET = {"document": (75, 120, 30), "presenter": (25, 40, 20)}   # (warn_words, fail_words, max_slides)
CHROME_PH = {"FOOTER", "SLIDE_NUMBER", "DATE"}          # placeholder ของแม่แบบที่ไม่ใช่เนื้อหา (ชื่อใน PP_PLACEHOLDER)
TITLE_PH = {"TITLE", "CENTER_TITLE"}
THAI_COMBINING = re.compile(r"[ัิ-ฺ็-๎]")   # สระบน-ล่าง/วรรณยุกต์ ไม่กินความกว้าง
_FONT_CACHE = {}


def _ph_type_name(sh):
    try:
        return sh.placeholder_format.type.name if sh.is_placeholder else ""
    except Exception:
        return ""


def _inherited_size_pt(sh, slide):
    """ขนาดฟอนต์ (pt) ของหัวเรื่อง ตามลำดับสืบทอด run → paragraph → placeholder ใน layout → master · ไม่พบ = None"""
    for p in sh.text_frame.paragraphs:
        for r in p.runs:
            if r.font.size:
                return r.font.size.pt
        if p.font.size:
            return p.font.size.pt
    try:
        idx = sh.placeholder_format.idx
        for owner in (slide.slide_layout, slide.slide_layout.slide_master):
            for lp in owner.placeholders:
                if lp.placeholder_format.idx == idx:
                    m = re.search(r'<a:lvl1pPr[^>]*>.*?<a:defRPr[^>]*\bsz="(\d+)"', lp._element.xml, re.S)
                    if m:
                        return int(m.group(1)) / 100.0
        m = re.search(r"<p:titleStyle>.*?<a:defRPr[^>]*\bsz=\"(\d+)\"", slide.slide_layout.slide_master._element.xml, re.S)
        if m:
            return int(m.group(1)) / 100.0
    except Exception:
        pass
    return None


def _font_for(bold, size_pt):
    """คืน (ImageFont, ชื่อไฟล์) ของฟอนต์รางเอกชนที่ขนาดนี้ · ไม่มี Pillow/ไม่พบไฟล์ = (None, None)"""
    key = (bold, size_pt)
    if key in _FONT_CACHE:
        return _FONT_CACHE[key]
    res = (None, None)
    try:
        from PIL import ImageFont
        path = font_file_for(RAILS["private"]["font"])
        if path and bold:
            cand = re.sub(r"-Regular(\.\w+)$", r"-Bold\1", path)
            if os.path.isfile(cand):
                path = cand
        if path:
            res = (ImageFont.truetype(path, int(round(size_pt))), os.path.basename(path))
    except Exception:
        res = (None, None)
    _FONT_CACHE[key] = res
    return res


def title_fit(sh, slide):
    """ประมาณว่าหัวเรื่องต้องใช้กี่บรรทัดและกล่องรับได้กี่บรรทัด · คืน (need, fit, note) หรือ None เมื่อวัดไม่ได้"""
    text = " ".join(sh.text_frame.text.split())
    if not text or not sh.width or not sh.height:
        return None
    size = _inherited_size_pt(sh, slide)
    if not size:
        return None
    bold = any(r.font.bold for p in sh.text_frame.paragraphs for r in p.runs) or True   # หัวเรื่องของแม่แบบเป็นตัวหนา
    box_w = sh.width / 12700.0                  # EMU → pt
    box_h = sh.height / 12700.0
    font, fname = _font_for(bold, size)
    if font is not None:
        width = max(font.getlength(line) for line in text.split("\n")) if "\n" in text else font.getlength(text)
        asc, desc = font.getmetrics()
        line_h = asc + desc
        note = f"วัดจาก {fname} {size:g}pt"
    else:
        width = (len(text) - len(THAI_COMBINING.findall(text))) * size * 0.55
        line_h = size * 1.65
        note = f"ประมาณ 0.55 em/ตัวอักษร ({size:g}pt — ไม่พบไฟล์ฟอนต์)"
    need = max(1, int(-(-width // box_w)))
    fit = max(1, int(box_h // line_h))
    return need, fit, note
THAI = re.compile(r"[฀-๿]+")
LATIN = re.compile(r"[A-Za-z0-9][A-Za-z0-9'’\-./%]*")
OBJECTIVE = re.compile(r"วัตถุประสงค์ของ(หน้า|สไลด์)|objective of (this|the) (slide|page)|(slide|page) objective", re.I)  # หัวข้อ "Objective & Scope" ของเอกสารเป็นเนื้อหาปกติ ไม่นับ


def word_count(text):
    thai = sum(len(m) for m in THAI.findall(text))
    latin = len(LATIN.findall(text))
    return int(round(thai / 4.5)) + latin


def iter_shapes(shapes):
    for sh in shapes:
        if sh.shape_type == MSO_SHAPE_TYPE.GROUP:
            yield sh, True
            for inner, _ in iter_shapes(sh.shapes):
                yield inner, False
        else:
            yield sh, False


def bbox(sh):
    try:
        if sh.left is None or sh.width is None:
            return None
        return (sh.left, sh.top, sh.left + sh.width, sh.top + sh.height)
    except Exception:
        return None


def overlap_ratio(a, b):
    ix = min(a[2], b[2]) - max(a[0], b[0])
    iy = min(a[3], b[3]) - max(a[1], b[1])
    if ix <= 0 or iy <= 0:
        return 0.0
    inter = ix * iy
    small = min((a[2] - a[0]) * (a[3] - a[1]), (b[2] - b[0]) * (b[3] - b[1])) or 1
    return inter / small


def audit_slide(slide, W, H, mode):
    warn_w, fail_w, _ = BUDGET[mode]
    words = 0
    texts = []          # (bbox, text) ของกล่องที่มีข้อความ
    pictures = 0
    drawn = 0           # รูปทรงที่ไม่มีข้อความ (icon/แผนภาพที่วาด) นับเฉพาะที่เล็กกว่า 40% ของหน้า
    overflow = 0
    objective_hit = False
    for sh, is_group in iter_shapes(slide.shapes):
        bb = bbox(sh)
        if bb and not is_group:
            if bb[0] < -0.01 * W or bb[1] < -0.01 * H or bb[2] > 1.01 * W or bb[3] > 1.01 * H:
                overflow += 1
        if sh.shape_type == MSO_SHAPE_TYPE.PICTURE or getattr(sh, "image", None) is not None and sh.shape_type != MSO_SHAPE_TYPE.GROUP:
            pictures += 1
            continue
        has_text = getattr(sh, "has_text_frame", False) and sh.text_frame.text.strip()
        if has_text:
            t = sh.text_frame.text.strip()
            words += word_count(t)
            if OBJECTIVE.search(t):
                objective_hit = True
            if bb:
                texts.append((bb, t[:40]))
        elif bb and not is_group:
            area = (bb[2] - bb[0]) * (bb[3] - bb[1])
            if 0 < area < 0.4 * W * H:
                drawn += 1
    overlaps = []
    for i in range(len(texts)):
        for j in range(i + 1, len(texts)):
            r = overlap_ratio(texts[i][0], texts[j][0])
            if r > 0.3:
                overlaps.append((texts[i][1], texts[j][1], round(r, 2)))
    has_visual = pictures > 0 or drawn >= 3
    # หน้าที่ใช้ layout ปก/คั่น/ปิด/ภาคผนวกของแม่แบบ (ICE_TEMPLATE) มีโลโก้และองค์ประกอบใน layout อยู่แล้ว ตัวตรวจมองไม่เห็นจึงไม่ถือว่า "ไม่มีภาพ"
    try:
        if (slide.slide_layout.name or "").strip().lower() in ("cover", "divider", "closing", "appendix"):
            has_visual = True
    except Exception:
        pass
    is_content = words > 12
    issues = []
    if overflow:
        issues.append(f"ล้นขอบ {overflow} ชิ้น")
    if overlaps:
        issues.append(f"ข้อความซ้อนกัน {len(overlaps)} คู่")
    if is_content and not has_visual:
        issues.append("หน้าเนื้อหาไม่มีภาพหรือ icon")
    if words > fail_w:
        issues.append(f"ข้อความ {words} คำ เกินงบ {warn_w} มาก ต้องแตกเป็น bullet หรือแยกหน้า")
    elif words > warn_w:
        issues.append(f"ข้อความ {words} คำ เกินงบ {warn_w} (เตือน)")
    if objective_hit:
        issues.append("มีคำว่าวัตถุประสงค์ของหน้าบนสไลด์ (ต้องอยู่ใน spec เท่านั้น)")
    fail = bool(overflow or overlaps or (is_content and not has_visual) or words > fail_w or objective_hit)
    return {"words": words, "pictures": pictures, "drawn": drawn, "overflow": overflow, "overlaps": len(overlaps),
            "content": is_content, "visual": has_visual, "issues": issues, "fail": fail}


def icon_style_spread(prs):
    """ความสม่ำเสมอของสไตล์ภาพประกอบ — วัดสัดส่วนพิกเซลที่มีหมึกของภาพเล็กทุกชิ้น (ภาพที่กว้างไม่เกิน 1.2 นิ้ว = icon)
    ภาพแบบเส้นโปร่งกับแบบทึบตันมีสัดส่วนหมึกต่างกันชัด ถ้าค่ากระจายเป็นสองกลุ่มแปลว่าปนสองสไตล์ในเล่มเดียว
    (ข้อเสนอของผู้ตรวจคุณภาพ 2026.09.06 — ก่อนหน้านี้ต้องใช้คนดูทุกครั้ง) · คืน (ค่าต่ำสุด ค่าสูงสุด จำนวนภาพ) หรือ None เมื่อวัดไม่ได้"""
    try:
        import io as _io
        from PIL import Image
    except Exception:
        return None
    ratios = []
    for s in prs.slides:
        for sh in s.shapes:
            if sh.shape_type != MSO_SHAPE_TYPE.PICTURE or not sh.width:
                continue
            if sh.width > int(1.2 * 914400):   # 914400 EMU = 1 นิ้ว
                continue
            try:
                im = Image.open(_io.BytesIO(sh.image.blob)).convert("LA")
                px = list(im.getdata())
                on = [p for p in px if p[1] > 40]          # นับเฉพาะพิกเซลที่ไม่โปร่งใส
                if not on:
                    continue
                ratios.append(sum(1 for p in on if p[0] < 200) / len(px))
            except Exception:
                continue
    return (min(ratios), max(ratios), len(ratios)) if len(ratios) >= 3 else None


def audit(path, mode):
    prs = Presentation(path)
    W, H = prs.slide_width, prs.slide_height
    rows = [audit_slide(s, W, H, mode) for s in prs.slides]
    _, _, max_slides = BUDGET[mode]
    n = len(rows)
    fails = [i + 1 for i, r in enumerate(rows) if r["fail"]]
    warns = [i + 1 for i, r in enumerate(rows) if r["issues"] and not r["fail"]]
    summary = {
        "file": path, "mode": mode, "slides": n,
        "avg_words": round(sum(r["words"] for r in rows) / n, 1) if n else 0,
        "max_words": max((r["words"] for r in rows), default=0),
        "content_without_visual": sum(1 for r in rows if r["content"] and not r["visual"]),
        "overflow_slides": sum(1 for r in rows if r["overflow"]),
        "overlap_slides": sum(1 for r in rows if r["overlaps"]),
        "too_many_slides": n > max_slides,
        "fail_slides": fails, "warn_slides": warns,
        "verdict": "FAIL" if fails else ("WARN" if warns or n > max_slides else "PASS"),
    }
    sp = icon_style_spread(prs)
    if sp:
        lo, hi, cnt = sp
        summary["icon_ink"] = {"min": round(lo, 3), "max": round(hi, 3), "count": cnt, "spread": round(hi - lo, 3)}
        # ช่วงห่างเกิน 0.18 = มีทั้งภาพแบบเส้นโปร่งและแบบทึบตันปนกัน (วัดจากคลัง icon ของทีม: เส้นโปร่งอยู่ราว 0.18–0.28 · ทึบตันอยู่ราว 0.34–0.52)
        if hi - lo > 0.18:
            summary["icon_mixed_style"] = True
            if summary["verdict"] == "PASS":
                summary["verdict"] = "WARN"
    return summary, rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="+")
    ap.add_argument("--mode", choices=list(BUDGET), default="document")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    worst = 0
    for f in a.files:
        s, rows = audit(f, a.mode)
        if a.json:
            print(json.dumps({"summary": s, "slides": rows}, ensure_ascii=False))
        else:
            print(f"== {f} · โหมด {a.mode} · {s['slides']} หน้า · เฉลี่ย {s['avg_words']} คำ/หน้า · สูงสุด {s['max_words']} คำ ==")
            for i, r in enumerate(rows, 1):
                if r["issues"]:
                    print(f"  หน้า {i:2d} [{'ไม่ผ่าน' if r['fail'] else 'เตือน'}] " + " · ".join(r["issues"]))
            if s.get("icon_mixed_style"):
                ii = s["icon_ink"]
                print(f"  [เตือน] ภาพประกอบปนสองสไตล์ในเล่มเดียว — สัดส่วนหมึกของภาพเล็ก {ii['count']} ชิ้นกระจายตั้งแต่ "
                      f"{ii['min']*100:.0f}% ถึง {ii['max']*100:.0f}% (ห่างกัน {ii['spread']*100:.0f} จุด) · แบบเส้นโปร่งกับแบบทึบตันไม่ควรอยู่ในเล่มเดียวกัน ให้เลือกสไตล์เดียว")
            if s["too_many_slides"]:
                print(f"  [เตือน] จำนวนหน้า {s['slides']} เกินเพดานของโหมด {BUDGET[a.mode][2]}")
            print(f"  ผล: {s['verdict']} — ไม่ผ่าน {len(s['fail_slides'])} หน้า · เตือน {len(s['warn_slides'])} หน้า")
        worst = max(worst, 2 if s["verdict"] == "FAIL" else 0)
    sys.exit(worst)


if __name__ == "__main__":
    main()
