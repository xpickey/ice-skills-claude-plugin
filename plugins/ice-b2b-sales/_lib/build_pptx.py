#!/usr/bin/env python3
"""
build_pptx.py — generic PPTX builder for sales agents.

Usage:
    python3 build_pptx.py spec.json out.pptx
    ICE_TEMPLATE=/path/iCE-Propose_Master.pptx python3 build_pptx.py spec.json out.pptx   (V02R05 โหมดแม่แบบ · V02R06 แก้ ISS-002/006/007/010)

FONT RULE (V02R04 · 2026.08.05) — ⚠ ข้อความเดิมที่ว่า "default = Tahoma ทุกข้อความ"
  **ยกเลิกแล้ว** (โค้ดไม่เคยอ่าน docstring นี้ · ตั้งแต่ V02R01 ฟอนต์มาจาก font_policy.RAILS)
  • ฟอนต์มาจาก **ราง** ที่ infer_rail() เดาจากชนิดเอกสาร (เอกชน/ราชการ)
  • สไลด์แน่น (>400 ตัวอักษร หรือ >8 บรรทัด หรือ ตาราง >40 ช่อง ในสไลด์ใดสไลด์หนึ่ง)
    → สลับทั้งเด็คเป็น 'Leelawadee' (ยอดวรรณยุกต์เตี้ยสุด = ไม่ชนเมื่อบีบบรรทัด)
    ปิด/บังคับด้วย spec["dense"] = false / true
  • spec["font_family"] ระบุเอง = เคารพ ไม่แทรกแซง (แต่ยังผ่านด่านนโยบาย V1/V2/V4/V5)

spec.json schema:
{
  "title": "Deck title",
  "subtitle": "Optional subtitle",
  "author": "Optional",
  "font_family": "Tahoma",   # optional, default = Tahoma (TH+EN balanced)
  "theme": {"primary": "#1F4E79", "accent": "#2E75B6"},   # optional
  "slides": [
    {"layout": "title", "title": "...", "subtitle": "..."},
    {"layout": "section", "title": "Section header"},
    {"layout": "bullets", "title": "...", "bullets": ["...", "..."]},
    {"layout": "two_column", "title": "...", "left": ["..."], "right": ["..."]},
    {"layout": "table", "title": "...", "headers": ["A","B"], "rows": [["x","y"]]},
    {"layout": "kpi", "title": "...", "kpis": [{"label":"ARR","value":"$1.2M","delta":"+18% YoY"}]},
    {"layout": "image", "title": "...", "image_path": "/path/to.png"},
    {"layout": "thanks", "title": "Thank you", "subtitle": "..."}
  ]
}
"""
import sys, os, re, json, math, subprocess
from datetime import datetime
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.oxml.ns import qn
from pptx.oxml import parse_xml
from pptx.oxml.ns import nsdecls


def OxmlElement(tag):
    return parse_xml(f'<{tag} {nsdecls("a")}/>')


# ⭐ นโยบายฟอนต์มาจาก SSOT เดียว — ห้าม hard-code ชื่อฟอนต์ในไฟล์นี้ (V02R02)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from font_policy import (RAILS, resolve_font_policy, infer_rail,
                         measure_slide_density, DENSE_FONT)   # noqa: E402


def hex_to_rgb(h):
    h = h.lstrip("#")
    return RGBColor(int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16))


# ── CHAR GUARD (PPTX Lesson #18) ────────────────────────────────────────────
# U+2192 "→" (และ arrow ญาติ) ทำให้ PowerPoint for Mac ปฏิเสธทั้งไฟล์ (Repair)
# ขณะที่ LibreOffice/qlmanage ปล่อยผ่าน (false-green). แทนด้วย ▸ (U+25B8) ที่
# เปิดได้ทุก engine + สื่อความ flow เดียวกัน. ตรวจซ้ำที่ deck_qa.py (safety net).
CHAR_REPLACEMENTS = {
    "→": "▸",  # → RIGHTWARDS ARROW       → ▸ BLACK RIGHT-POINTING SMALL TRIANGLE
    "⟶": "▸",  # ⟶ LONG RIGHTWARDS ARROW  → ▸
    "➜": "▸",  # ➜ HEAVY ROUND-TIPPED ARROW → ▸
    "➔": "▸",  # ➔ HEAVY WIDE-HEADED ARROW  → ▸
    "➙": "▸",  # ➙ HEAVY RIGHTWARDS ARROW   → ▸
}


def _sanitize_chars(obj, _stats=None):
    """Recursively replace PowerPoint-rejecting chars in any string within spec.
    Returns (sanitized_obj, replacement_count). Logs to stderr — never silent."""
    top = _stats is None
    if _stats is None:
        _stats = {"count": 0}
    if isinstance(obj, str):
        out = obj
        for bad, good in CHAR_REPLACEMENTS.items():
            if bad in out:
                _stats["count"] += out.count(bad)
                out = out.replace(bad, good)
        return (out, _stats["count"]) if top else out
    if isinstance(obj, dict):
        res = {k: _sanitize_chars(v, _stats) for k, v in obj.items()}
        return (res, _stats["count"]) if top else res
    if isinstance(obj, list):
        res = [_sanitize_chars(v, _stats) for v in obj]
        return (res, _stats["count"]) if top else res
    return (obj, _stats["count"]) if top else obj


def add_title_slide(prs, slide, theme):
    layout = prs.slide_layouts[0]
    s = prs.slides.add_slide(layout)
    s.shapes.title.text = slide.get("title", "")
    if len(s.placeholders) > 1:
        s.placeholders[1].text = slide.get("subtitle", "")


def add_section_slide(prs, slide, theme):
    layout = prs.slide_layouts[5]
    s = prs.slides.add_slide(layout)
    s.shapes.title.text = slide.get("title", "")


def add_bullets_slide(prs, slide, theme):
    layout = prs.slide_layouts[1]
    s = prs.slides.add_slide(layout)
    s.shapes.title.text = slide.get("title", "")
    body = s.placeholders[1].text_frame
    body.text = slide["bullets"][0] if slide.get("bullets") else ""
    for b in slide.get("bullets", [])[1:]:
        p = body.add_paragraph()
        p.text = b


def add_two_column(prs, slide, theme):
    layout = prs.slide_layouts[5]
    s = prs.slides.add_slide(layout)
    s.shapes.title.text = slide.get("title", "")
    left_items = slide.get("left", [])
    right_items = slide.get("right", [])
    left = s.shapes.add_textbox(Inches(0.5), Inches(1.5), Inches(4.5), Inches(5)).text_frame
    right = s.shapes.add_textbox(Inches(5.0), Inches(1.5), Inches(4.5), Inches(5)).text_frame
    if left_items:
        left.text = left_items[0]
        for t in left_items[1:]:
            left.add_paragraph().text = t
    if right_items:
        right.text = right_items[0]
        for t in right_items[1:]:
            right.add_paragraph().text = t


def add_table(prs, slide, theme):
    layout = prs.slide_layouts[5]
    s = prs.slides.add_slide(layout)
    s.shapes.title.text = slide.get("title", "")
    headers = slide.get("headers", [])
    rows = slide.get("rows", [])
    if not headers:
        return
    rows_n = len(rows) + 1
    cols_n = len(headers)
    tbl = s.shapes.add_table(rows_n, cols_n, Inches(0.5), Inches(1.5), Inches(9), Inches(0.5 * rows_n)).table
    for j, h in enumerate(headers):
        tbl.cell(0, j).text = str(h)
    for i, row in enumerate(rows, start=1):
        for j, v in enumerate(row):
            tbl.cell(i, j).text = str(v)


def add_kpi(prs, slide, theme):
    layout = prs.slide_layouts[5]
    s = prs.slides.add_slide(layout)
    s.shapes.title.text = slide.get("title", "")
    kpis = slide.get("kpis", [])
    n = max(1, len(kpis))
    box_w = 9 / n
    for i, k in enumerate(kpis):
        left = Inches(0.5 + i * box_w)
        shape = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, Inches(2), Inches(box_w - 0.2), Inches(2.5))
        tf = shape.text_frame
        tf.text = k.get("label", "")
        p = tf.add_paragraph()
        p.text = k.get("value", "")
        p.font.size = Pt(28)
        p.font.bold = True
        if k.get("delta"):
            p2 = tf.add_paragraph()
            p2.text = k["delta"]


def add_image(prs, slide, theme):
    layout = prs.slide_layouts[5]
    s = prs.slides.add_slide(layout)
    s.shapes.title.text = slide.get("title", "")
    if slide.get("image_path"):
        s.shapes.add_picture(slide["image_path"], Inches(0.5), Inches(1.5), Inches(9), Inches(5))


# ── ⭐ D1 TRI-SLOT FONT BINDING (V02R01 — 2026.08.04) ────────────────────────
# บั๊กที่แก้: ไฟล์นี้ **ไม่เคย set ฟอนต์เลยสักบรรทัด** ตลอดอายุการใช้งาน — docstring
# บอก "default Tahoma" และ spec key `font_family` แต่โค้ดไม่เคยอ่านทั้งคู่ (dead doc)
# → output ได้ฟอนต์ default ของ python-pptx (Calibri) ซึ่งไม่มี glyph ไทยเลย
# ทำเป็น post-pass เดินทุก run แทนการแก้ layout function ทั้ง 8 ตัว (ปลอดภัยกว่า)
def _bind_font(tf, font):
    for p in tf.paragraphs:
        for r in p.runs:
            rPr = r._r.get_or_add_rPr()
            for tag in ("a:latin", "a:ea", "a:cs"):          # ครบ 3 slot — D1
                for old in rPr.findall(qn(tag)):
                    rPr.remove(old)
                el = OxmlElement(tag)
                el.set("typeface", font)
                rPr.append(el)


def apply_font(prs, font):
    """เดินทุก shape/table cell ในทุก slide แล้วผูกฟอนต์ครบ 3 slot"""
    n = 0
    for s in prs.slides:
        for sh in s.shapes:
            if sh.has_text_frame:
                _bind_font(sh.text_frame, font); n += 1
            if getattr(sh, "has_table", False) and sh.has_table:
                for row in sh.table.rows:
                    for cell in row.cells:
                        _bind_font(cell.text_frame, font); n += 1
    return n


# ═══════════════════════════════════════════════════════════════════════════════
# ⭐ V02R05 (2026.09.05 · Wave B) — โหมดแม่แบบ: ICE_TEMPLATE=<path ไฟล์ .pptx แม่แบบ>
#   ต้นตอ: builder ทุกตัวสร้าง deck จาก Presentation() เปล่าแล้ววาดทุกอย่างจาก shape primitive
#   (เฉลี่ย 47 shape ต่อหน้า วัตถุทับกัน ฟอนต์ไม่คงที่ หน้าตาไม่เหมือน CI) — โหมดนี้เปิดแม่แบบจริง
#   ที่ฝังฟอนต์/สี/กริดของ iCE ไว้แล้ว (b2b-slide-designer/assets/masters/iCE-Propose_Master.pptx)
#   แล้ว "เติมเนื้อหาลง placeholder" ของ layout ที่เลือกตามชื่อเท่านั้น
#   ⚠ ไม่ตั้งตัวแปรนี้ = พฤติกรรมเดิมทุกอย่าง 100% (โค้ดด้านบนไม่ถูกแตะ)
#
#   ชื่อ layout ใน spec ใช้ได้ทั้งชื่อเดิม (title/section/bullets/two_column/table/kpi/image/thanks)
#   และชื่อของแม่แบบ (cover/divider/action-title-body/two-column/three-card/table/timeline/closing/appendix)
#   คีย์เพิ่มเติมที่โหมดแม่แบบอ่าน (ไม่บังคับ):
#     ระดับ deck : "footer" (ข้อความท้ายหน้า) · "icon_color" (hex ของ icon ที่แปลงจาก SVG)
#     ทุกหน้าเนื้อหา : "icon" = ชื่อไฟล์ mdi-*.svg ในคลัง หรือ path .png/.svg → icon นำหน้าหัวเรื่อง
#     cover  : "kicker" "subtitle" "meta"          · divider : "number" "subtitle"
#     action-title-body : "bullets" + "image_path" หรือ "image_icon" (พื้นที่ภาพด้านขวา)
#     two-column : "left_title" "left" "left_icon" "right_title" "right" "right_icon"
#     three-card : "cards": [{"icon","title","text"|"bullets"}] (หรือแปลงจาก "kpis" ให้อัตโนมัติ)
#     table  : "headers" "rows" "note"              · timeline : "phases": [{"label","text"}] ≤4
#     closing: "subtitle" "contact"                 · appendix : "bullets"
#   bullet ระดับสอง: ข้อความขึ้นต้นด้วยสองช่องว่าง หรือ {"text": "...", "level": 1}
# ═══════════════════════════════════════════════════════════════════════════════
#
#   ⭐ V02R06 (2026.09.06 · แก้ตามผลตรวจของอริสจากการซ้อมจริง Pass 6 — ทั้งหมดทำงานเฉพาะโหมดแม่แบบ):
#     ISS-002 timeline : เส้นแกนและหมุดวาดบนสไลด์ตามจำนวน phases จริง (2–4) และจัดตำแหน่ง placeholder ให้กระจายเต็มความกว้าง
#                        (แม่แบบ V01R02 ถอดหมุดตายตัวออกแล้ว) — ตรวจได้: จำนวนวงกลมบนสไลด์ = จำนวนช่วง
#     ISS-006 icon     : icon ที่ใช้เป็นภาพประกอบ (image_icon / icon การ์ด / icon คอลัมน์) จำกัดขนาดไม่เกิน ICON_MAX_IN นิ้ว
#                        จัดกึ่งกลางพื้นที่ภาพ และแปลง SVG ที่ความละเอียดตามขนาดที่วางจริง (≥ ICON_MIN_DPI) · ภาพทุกชิ้นถูกวัด dpi จริง
#                        แล้วเตือนเมื่อต่ำกว่าเกณฑ์
#     ISS-007 color    : สี icon กำหนดได้รายหน้า — "icon_color" (hex) หรือ "color_set" (ชื่อชุดสีจาก tokens.json ของ iCE Design System:
#                        cool/teal/deep/warm/danger/success หรือ path เช่น "brand.teal" "status.danger") ระดับหน้าชนะระดับ deck
#                        · ห้ามคิดสีเอง: ทุกชื่อชุดแปลงเป็นค่าจาก tokens.json เท่านั้น
#     ISS-010 version  : core_properties (title/subject/author/version/comments) มาจาก spec · รหัสรุ่น V##R## และวันที่ YYYY.MM.DD
#                        อ่านจากชื่อไฟล์ผลลัพธ์แล้วต่อท้าย footer ทุกหน้าเนื้อหา (spec "footer_version": false เพื่อปิด)
# ═══════════════════════════════════════════════════════════════════════════════
ICE_TEMPLATE = os.environ.get("ICE_TEMPLATE") or None
ICON_DIR = os.path.expanduser("~/.claude/skills/b2b-slide-designer/assets/icons")
DS_TOKENS = "/Users/xpickey/Documents/Claude/iCE-Design-System/tokens/tokens.json"   # ต้นทางสีเดียวกับ make_master.py
ICON_MAX_IN = 2.0        # icon ที่ใช้เป็นภาพประกอบ ขยายได้ไม่เกินกี่นิ้ว (ISS-006: 4.55 นิ้ว จาก 512px = 113 dpi หยาบ)
ICON_MIN_DPI = 150       # ความละเอียดจริงขั้นต่ำของภาพทุกชิ้นที่วางบนสไลด์
ICON_RENDER_DPI = 200    # แปลง SVG ที่ความละเอียดนี้ตามขนาดที่วางจริง (ไม่ต่ำกว่า 512px)
SLIDE_W_IN, SAFE_MARGIN_IN = 13.333, 0.6     # กริดของแม่แบบ (make_master.py W_IN · ML/MR)
TIMELINE = {  # ค่ากริดแกนเวลาของแม่แบบ V01R02 (make_master.py TL_*) — แก้ที่โน่นต้องแก้ที่นี่ให้ตรงกัน
    "label_y": 2.70, "label_h": 0.80, "track_y": 3.85, "detail_y": 4.25, "detail_h": 2.25,
    "pin_d": 0.52, "track_pt": 5, "tones": ["navyDeep", "navy", "tealBright", "teal"],
}


def _load_tokens():
    try:
        with open(DS_TOKENS, encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"⚠ อ่าน tokens.json ไม่ได้ ({e}) — ใช้ได้เฉพาะ icon_color แบบ hex", file=sys.stderr)
        return {}


_TOKENS = None


def _token_color(path):
    """คืน hex (ไม่มี #) ของสีจาก tokens.json ตาม path เช่น 'brand.navy' 'status.warning' 'gold.deep' · ไม่พบ = None"""
    global _TOKENS
    if _TOKENS is None:
        _TOKENS = _load_tokens()
    node = _TOKENS.get("color", {})
    for part in path.split("."):
        node = node.get(part) if isinstance(node, dict) else None
        if node is None:
            return None
    val = node.get("value") if isinstance(node, dict) else node
    if isinstance(val, str) and re.fullmatch(r"#?[0-9A-Fa-f]{6}", val):
        return val.lstrip("#").upper()
    return None


# ชื่อชุดสีที่ content-spec ใช้ (color_set) → path ใน tokens.json — ไม่มีค่าสีเขียนตรง ๆ ในไฟล์นี้
COLOR_SETS = {
    "cool": "brand.navy", "navy": "brand.navy", "teal": "brand.teal", "deep": "brand.navyDeep",
    "bright": "brand.tealBright", "warm": "status.warning", "amber": "status.warning",
    "danger": "status.danger", "alert": "status.danger", "success": "status.success", "gold": "gold.deep",
}


def _resolve_color(value, where):
    """แปลงค่าที่ spec ให้ (hex / ชื่อชุด / path ใน tokens) เป็น hex · ค่าที่ไม่รู้จัก = หยุดพร้อมบอกตัวเลือก"""
    if value in (None, "", "none", "default"):
        return None
    v = str(value).strip()
    if re.fullmatch(r"#?[0-9A-Fa-f]{6}", v):
        return v.lstrip("#").upper()
    hexcol = _token_color(COLOR_SETS.get(v.lower(), v))
    if hexcol is None:
        sys.exit(f"{where}: ไม่รู้จักชุดสี '{value}' — ใช้ hex, ชื่อชุด ({', '.join(COLOR_SETS)}) "
                 f"หรือ path ใน tokens.json เช่น brand.teal / status.danger")
    return hexcol


def _slide_color(sl, deck):
    """สี icon ของหน้านี้ — ระดับหน้า (icon_color > color_set) ชนะระดับ deck (icon_color > color_set) · ไม่ระบุ = brand.navy"""
    for src, key in ((sl, "icon_color"), (sl, "color_set"), (deck, "icon_color"), (deck, "color_set")):
        c = _resolve_color(src.get(key), f"{key} ของหน้า '{sl.get('title', '')[:30]}'" if src is sl else f"{key} ระดับ deck")
        if c:
            return c
    return _token_color("brand.navy") or "1E66A4"

TEMPLATE_LAYOUT_ALIAS = {
    "title": "cover", "cover": "cover",
    "section": "divider", "divider": "divider",
    "bullets": "action-title-body", "image": "action-title-body", "action-title-body": "action-title-body",
    "two_column": "two-column", "two-column": "two-column",
    "kpi": "three-card", "cards": "three-card", "three-card": "three-card",
    "table": "table",
    "timeline": "timeline",
    "thanks": "closing", "closing": "closing",
    "appendix": "appendix",
}


def _layout_by_name(prs, name):
    for lay in prs.slide_layouts:
        if lay.name == name:
            return lay
    avail = ", ".join(l.name for l in prs.slide_layouts)
    sys.exit(f"แม่แบบไม่มี layout ชื่อ '{name}' (มี: {avail})")


def _remove_all_slides(prs):
    """ลบสไลด์ตัวอย่างที่ติดมากับแม่แบบ — เหลือแต่ master/layout"""
    sldIdLst = prs.slides._sldIdLst
    for sldId in list(sldIdLst):
        prs.part.drop_rel(sldId.rId)
        sldIdLst.remove(sldId)


def _ph(slide, idx):
    for shp in slide.placeholders:
        if shp.placeholder_format.idx == idx:
            return shp
    return None


def _set_text(ph, items):
    """เติมข้อความลง placeholder · str = ย่อหน้าเดียว · list = หลายย่อหน้า (bullet ตาม layout)"""
    if ph is None or items in (None, "", []):
        return False
    if isinstance(items, str):
        items = [items]
    tf = ph.text_frame
    first = True
    for it in items:
        level = 0
        if isinstance(it, dict):
            level, it = int(it.get("level", 0)), str(it.get("text", ""))
        elif it.startswith("  "):
            level, it = 1, it.strip()
        p = tf.paragraphs[0] if first else tf.add_paragraph()
        p.text = it
        p.level = level
        first = False
    return True


def _icon_px(size_in):
    """ความละเอียดที่จะแปลง SVG: ตามขนาดที่วางจริง × ICON_RENDER_DPI ปัดขึ้นเป็นขั้น 64px และไม่ต่ำกว่า 512px"""
    if not size_in:
        return 512
    return max(512, int(math.ceil(size_in * ICON_RENDER_DPI / 64.0)) * 64)


def _icon_png(src, color, out_dir, size_in=None):
    """คืน path PNG ของ icon · รับชื่อ mdi-xxx / ไฟล์ .svg / ไฟล์ .png · size_in = ขนาดที่จะวางจริง (นิ้ว) กำหนดความละเอียด
    SVG → PNG ใช้ qlmanage ของ macOS (ไม่ต้องติดตั้งอะไร) · ย้อมสีด้วยการแทน currentColor ก่อนแปลง"""
    if not src:
        return None
    if src.lower().endswith(".png") and os.path.isfile(src):
        return src
    name = os.path.basename(src)
    if not name.endswith(".svg"):
        name += ".svg"
    if not name.startswith("mdi-") and not os.path.isfile(src):
        name = "mdi-" + name
    svg_path = src if os.path.isfile(src) else os.path.join(ICON_DIR, name)
    if not os.path.isfile(svg_path):
        sys.exit(f"ไม่พบ icon: {src} (ค้นใน {ICON_DIR} — ดูรายชื่อที่ INDEX.md)")
    icon_dir = os.path.join(out_dir, "_icons")
    os.makedirs(icon_dir, exist_ok=True)
    hexcol = (color or _token_color("brand.navy") or "1E66A4").lstrip("#").upper()
    px = _icon_px(size_in)
    stem = os.path.splitext(os.path.basename(svg_path))[0]
    png = os.path.join(icon_dir, f"{stem}-{hexcol}.png" if px == 512 else f"{stem}-{hexcol}-{px}px.png")
    if os.path.isfile(png):
        return png
    tinted = os.path.join(icon_dir, f"{stem}-{hexcol}.svg")
    with open(svg_path, encoding="utf-8") as f:
        svg = f.read().replace("currentColor", f"#{hexcol}")
    with open(tinted, "w", encoding="utf-8") as f:
        f.write(svg)
    r = subprocess.run(["qlmanage", "-t", "-s", str(px), "-o", icon_dir, tinted],
                       capture_output=True, text=True)
    made = tinted + ".png"
    if not os.path.isfile(made):
        sys.exit(f"แปลง SVG เป็น PNG ไม่สำเร็จ ({r.stderr.strip()[:200]}) — ดูวิธีทางเลือกใน "
                 f"{ICON_DIR}/INDEX.md หัวข้อ 'การแปลง SVG เป็น PNG'")
    os.remove(tinted)
    # qlmanage คืนภาพพื้นขาวทึบ → คำนวณความโปร่งใสจากความเข้มของพิกเซล แล้วระบายสีที่ต้องการ
    # (icon ของคลังเป็นสีเดียวบนพื้นขาว จึงใช้ช่องสีต่ำสุดเป็นตัวบอกว่าพิกเซลนั้นเป็นเนื้อ icon แค่ไหน)
    try:
        from PIL import Image
        rr, gg, bb = int(hexcol[0:2], 16), int(hexcol[2:4], 16), int(hexcol[4:6], 16)
        floor = min(rr, gg, bb)
        with Image.open(made) as im:
            im = im.convert("RGBA")
            px = im.load()
            w, h = im.size
            for yy in range(h):
                for xx in range(w):
                    r, g, b, _ = px[xx, yy]
                    a = 255 - min(r, g, b)
                    a = int(round(a * 255 / max(1, 255 - floor)))
                    px[xx, yy] = (rr, gg, bb, max(0, min(255, a)))
            im.save(png)
        os.remove(made)
    except Exception as e:                      # ไม่มี PIL → ใช้ภาพพื้นขาวไปก่อน (แจ้งเสมอ)
        print(f"⚠ icon {stem}: ทำพื้นโปร่งใสไม่ได้ ({e}) — ใช้ภาพพื้นขาว", file=sys.stderr)
        os.replace(made, png)
    return png


_DPI_WARNINGS = []


def _fill_pic(slide, ph, path, max_in=None):
    """วางภาพให้พอดีในกรอบ placeholder แบบไม่ตัดขอบ (contain) จัดกึ่งกลาง แล้วถอด placeholder ออก
    max_in = เพดานขนาด (นิ้ว) สำหรับ icon ที่ใช้เป็นภาพประกอบ (ISS-006) · วัด dpi จริงของทุกภาพ ต่ำกว่าเกณฑ์ = เตือน"""
    if ph is None or not path:
        return False
    try:
        from PIL import Image
        with Image.open(path) as im:
            iw, ih = im.size
    except Exception:
        iw, ih = 1, 1
    bx, by, bw, bh = ph.left, ph.top, ph.width, ph.height
    cap_w = min(bw, Inches(max_in)) if max_in else bw
    cap_h = min(bh, Inches(max_in)) if max_in else bh
    scale = min(cap_w / iw, cap_h / ih)
    w, h = int(iw * scale), int(ih * scale)
    x, y = bx + (bw - w) // 2, by + (bh - h) // 2
    slide.shapes.add_picture(path, x, y, w, h)
    ph._element.getparent().remove(ph._element)
    dpi = iw / (w / 914400.0) if w else 0
    if dpi < ICON_MIN_DPI:
        _DPI_WARNINGS.append(f"{os.path.basename(path)} วางกว้าง {w / 914400:.2f} นิ้ว จาก {iw}px = {dpi:.0f} dpi "
                             f"(เกณฑ์ ≥{ICON_MIN_DPI})")
    return True


def _icon_into(slide, ph, src, color, out_dir, max_in=None):
    """แปลง icon ที่ความละเอียดตามขนาดที่จะวางจริง แล้ววางลง placeholder (ขนาดจริง = เล็กสุดของกรอบกับ max_in)"""
    if ph is None or not src:
        return False
    size_in = min(ph.width, ph.height) / 914400.0
    if max_in:
        size_in = min(size_in, max_in)
    return _fill_pic(slide, ph, _icon_png(src, color, out_dir, size_in=size_in), max_in=max_in)


def _clone_footer(slide, layout, footer_text):
    """ยก footer (idx 11) และเลขหน้า (idx 12) จาก layout ลงสไลด์ — python-pptx ไม่ clone ให้เอง
    (PowerPoint แสดงสองอย่างนี้เฉพาะเมื่อสไลด์มี placeholder ของตัวเอง)"""
    import copy as _copy
    spTree = slide.shapes._spTree
    for shp in layout.placeholders:
        idx = shp.placeholder_format.idx
        if idx not in (11, 12):
            continue
        el = _copy.deepcopy(shp._element)
        spTree.append(el)
    for shp in slide.placeholders:
        if shp.placeholder_format.idx == 11 and footer_text:
            shp.text_frame.paragraphs[0].text = footer_text


def _prune_empty(slide):
    """ถอด placeholder ที่ไม่ได้เติม (กันข้อความ 'Click to add' และกล่องว่างค้างในไฟล์)"""
    for shp in list(slide.placeholders):
        pf = shp.placeholder_format
        if pf.idx in (11, 12):
            continue
        if shp.has_text_frame and shp.text_frame.text.strip():
            continue
        if not shp.has_text_frame and getattr(shp, "has_table", False) and shp.has_table:
            continue
        shp._element.getparent().remove(shp._element)


def _title_icon(slide, spec_slide, deck, out_dir):
    icon = spec_slide.get("icon")
    if icon:
        _icon_into(slide, _ph(slide, 10), icon, _slide_color(spec_slide, deck), out_dir)


DARK_LAYOUTS = {"cover", "divider", "closing"}

# ความเข้มของภาพพื้นหลัง (ร้อยละ) — ผลตรวจคุณภาพ 2026.09.06 พบว่าลายที่ความเข้มเต็มวิ่งผ่านหลังข้อความ
# ในคอลัมน์ขวาและแถบส่วนท้ายหน้า เพราะกริดเนื้อหาของแม่แบบกินความกว้างถึง 12.6 จาก 13.33 นิ้ว
# ทางแก้ที่ไม่ต้องหดพื้นที่เนื้อหาของทุก deck คือทำให้ลายเป็นลายน้ำจาง ๆ แทนการย้ายข้อความ
# หน้าพื้นเข้มจางน้อยกว่าเพราะตัวอักษรขาวบนพื้นเข้มมีความต่างสีสูงอยู่แล้ว · ปรับรายเล่มได้ด้วย
# ช่อง background_opacity_dark และ background_opacity_light ในไฟล์กำหนดเนื้อหา
BG_OPACITY_DARK = 75
BG_OPACITY_LIGHT = 40


def _fade_picture(pic, percent):
    """ทำให้ภาพโปร่งลงตามร้อยละที่กำหนด (100 = ทึบเต็ม) โดยเติม alphaModFix ให้กับ blip ของภาพ"""
    try:
        pct = max(1, min(100, int(percent)))
    except (TypeError, ValueError):
        pct = 100
    if pct >= 100:
        return
    blip = pic._element.blipFill.find(qn("a:blip"))
    if blip is None:
        return
    fx = blip.makeelement(qn("a:alphaModFix"), {"amt": str(pct * 1000)})
    blip.append(fx)


def _check_background_origin(spec, out_path):
    """เตือนเมื่อภาพพื้นหลังไม่ได้สร้างขึ้นสำหรับเอกสารชิ้นนี้
    กติกาของ user 2026.09.06: พื้นหลังต้องสร้างใหม่ทุกครั้งตามหัวเรื่องของเอกสาร ห้ามหยิบของงานอื่นมาใช้ซ้ำ
    การนับว่า "มีภาพพื้นหลัง" อย่างเดียวยังบังคับได้แค่ครึ่งเดียว เพราะไฟล์ที่ยืมมาจากเล่มอื่นก็นับผ่าน
    จึงตรวจเพิ่มว่าไฟล์อยู่ในคลังภาพของงานชิ้นนี้เอง (_build/assets/bg/ ข้างไฟล์ผลงาน) หรือไม่"""
    home = os.path.join(os.path.dirname(os.path.abspath(out_path)), "_build", "assets", "bg")
    declared = [(k, spec.get(k)) for k in ("background_dark", "background_light") if spec.get(k)]
    if not declared:
        print("⚠ ยังไม่ได้ประกาศภาพพื้นหลังของเล่มนี้ (ช่อง background_dark และ background_light) — "
              "ทุก deck ต้องมีพื้นหลังลายเส้นทองที่สร้างใหม่ตามหัวเรื่องของเอกสาร "
              "สูตรอยู่ที่ ice-super-template หัวข้อ 4", file=sys.stderr)
        return
    home_real = os.path.realpath(home)
    for key, path in declared:
        parent = os.path.dirname(os.path.realpath(os.path.expanduser(path)))
        if parent != home_real:
            print(f"⚠ ภาพพื้นหลังช่อง {key} ไม่ได้อยู่ในคลังภาพของงานชิ้นนี้ ({home}) — "
                  f"ถ้าเป็นไฟล์ที่ยืมมาจากเอกสารเรื่องอื่น ให้สร้างใหม่ตามหัวเรื่องของเล่มนี้ก่อน", file=sys.stderr)


def _apply_background(prs, slide, layout_name, deck):
    """วางภาพพื้นหลังของ deck นี้ทับพื้นไล่เฉดของแม่แบบ แล้วดันไปหลังสุด
    (คำสั่ง user 2026.09.06: ลายเส้นทองต้องสร้างใหม่ทุกครั้งตามหัวเรื่องของเอกสาร ไม่ใช่ไฟล์ตายตัว —
     กติกาเต็มอยู่ที่ ice-doc-builder/references/ice-super-template.md §3 ลายตามอุตสาหกรรม และ §4 สูตรสร้าง)
    ช่องใน spec: background_dark ใช้กับหน้าปก คั่น ปิด · background_light ใช้กับหน้าเนื้อหา
    ไม่ใส่ = ใช้พื้นไล่เฉดของแม่แบบตามเดิม"""
    key = "background_dark" if layout_name in DARK_LAYOUTS else "background_light"
    path = deck.get(key)
    if not path:
        return
    path = os.path.expanduser(path)
    if not os.path.isfile(path):
        print(f"⚠ ไม่พบไฟล์พื้นหลัง {key}: {path} — ใช้พื้นไล่เฉดของแม่แบบแทน", file=sys.stderr)
        return
    pic = slide.shapes.add_picture(path, 0, 0, width=prs.slide_width, height=prs.slide_height)
    tree = slide.shapes._spTree
    tree.remove(pic._element)
    tree.insert(2, pic._element)      # หลังสุด ก่อนทุก placeholder
    pic._element.nvPicPr.cNvPr.set("name", "Deck Background")
    _fade_picture(pic, deck.get("background_opacity_dark" if layout_name in DARK_LAYOUTS
                               else "background_opacity_light",
                               BG_OPACITY_DARK if layout_name in DARK_LAYOUTS else BG_OPACITY_LIGHT))


def _tpl_slide(prs, name, deck=None):
    layout = _layout_by_name(prs, TEMPLATE_LAYOUT_ALIAS.get(name, name))
    slide = prs.slides.add_slide(layout)
    if deck is not None:
        _apply_background(prs, slide, TEMPLATE_LAYOUT_ALIAS.get(name, name), deck)
    return slide, layout


def tpl_cover(prs, sl, deck, out_dir):
    s, lay = _tpl_slide(prs, "cover", deck)
    s.shapes.title.text = sl.get("title", deck.get("title", ""))
    _set_text(_ph(s, 1), sl.get("kicker", deck.get("kicker")))
    _set_text(_ph(s, 2), sl.get("subtitle", deck.get("subtitle")))
    _set_text(_ph(s, 3), sl.get("meta"))
    return s, lay


def tpl_divider(prs, sl, deck, out_dir):
    s, lay = _tpl_slide(prs, "divider", deck)
    s.shapes.title.text = sl.get("title", "")
    _set_text(_ph(s, 1), sl.get("number"))
    _set_text(_ph(s, 2), sl.get("subtitle"))
    return s, lay


def tpl_action_title_body(prs, sl, deck, out_dir):
    s, lay = _tpl_slide(prs, "action-title-body", deck)
    s.shapes.title.text = sl.get("title", "")
    _set_text(_ph(s, 1), sl.get("bullets"))
    if sl.get("image_path"):
        _fill_pic(s, _ph(s, 2), sl["image_path"])
    elif sl.get("image_icon"):
        # ISS-006: icon เป็นภาพประกอบ ไม่ขยายเต็มกรอบ 4.7 นิ้ว — จำกัด ICON_MAX_IN และวางกึ่งกลางพื้นที่ภาพ
        _icon_into(s, _ph(s, 2), sl["image_icon"], _slide_color(sl, deck), out_dir, max_in=ICON_MAX_IN)
    _title_icon(s, sl, deck, out_dir)
    return s, lay


def tpl_two_column(prs, sl, deck, out_dir):
    s, lay = _tpl_slide(prs, "two-column", deck)
    s.shapes.title.text = sl.get("title", "")
    _set_text(_ph(s, 1), sl.get("left_title"))
    _set_text(_ph(s, 2), sl.get("left"))
    _set_text(_ph(s, 3), sl.get("right_title"))
    _set_text(_ph(s, 4), sl.get("right"))
    for idx, key in ((5, "left_icon"), (6, "right_icon")):
        if sl.get(key):
            _icon_into(s, _ph(s, idx), sl[key], _slide_color(sl, deck), out_dir)
    _title_icon(s, sl, deck, out_dir)
    return s, lay


def tpl_three_card(prs, sl, deck, out_dir):
    s, lay = _tpl_slide(prs, "three-card", deck)
    s.shapes.title.text = sl.get("title", "")
    cards = sl.get("cards")
    if not cards and sl.get("kpis"):
        cards = [{"title": k.get("value", ""), "text": [k.get("label", ""), k.get("delta", "")]}
                 for k in sl["kpis"]]
    for i, c in enumerate((cards or [])[:3]):
        base = i * 3
        if c.get("icon"):
            _icon_into(s, _ph(s, base + 1), c["icon"], _slide_color(sl, deck), out_dir)
        _set_text(_ph(s, base + 2), c.get("title"))
        body = c.get("bullets") or c.get("text")
        if isinstance(body, list):
            body = [t for t in body if t]
        _set_text(_ph(s, base + 3), body)
    _title_icon(s, sl, deck, out_dir)
    return s, lay


def tpl_table(prs, sl, deck, out_dir):
    s, lay = _tpl_slide(prs, "table", deck)
    s.shapes.title.text = sl.get("title", "")
    headers, rows = sl.get("headers", []), sl.get("rows", [])
    ph = _ph(s, 1)
    if headers and ph is not None:
        gf = ph.insert_table(len(rows) + 1, len(headers))
        tbl = gf.table
        sz = Pt(16) if len(rows) <= 6 else Pt(14)
        for j, h in enumerate(headers):
            tbl.cell(0, j).text = str(h)
        for i, row in enumerate(rows, start=1):
            for j, v in enumerate(row):
                tbl.cell(i, j).text = str(v)
        for r in tbl.rows:
            r.height = Inches(0.45)
            for c in r.cells:
                for p in c.text_frame.paragraphs:
                    for run in p.runs:
                        run.font.size = sz
    _set_text(_ph(s, 2), sl.get("note"))
    _title_icon(s, sl, deck, out_dir)
    return s, lay


def _timeline_track_and_pins(slide, n, centers_in, pin_font):
    """วาดเส้นแกน (ไล่เฉด brand) ยาวพอดีจากหมุดแรกถึงหมุดสุดท้าย + หมุดเลข 1..n บนสไลด์ (ISS-002)
    สีทั้งหมดจาก tokens.json ตามคีย์ใน TIMELINE['tones'] · ฟอนต์ตัวเลขในหมุด = ฟอนต์รางที่ผู้เรียกส่งมา"""
    T = TIMELINE
    ty, d = T["track_y"], T["pin_d"]
    g0, g1 = _token_color("brand.navy"), _token_color("brand.teal")
    x1, x2 = centers_in[0] - 0.3, centers_in[-1] + 0.3
    spTree = slide.shapes._spTree
    A = 'xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" ' \
        'xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main"'
    E = lambda v: int(round(v * 914400))
    track = parse_xml(
        f'<p:cxnSp {A}><p:nvCxnSpPr><p:cNvPr id="0" name="Timeline Track"/><p:cNvCxnSpPr/><p:nvPr/></p:nvCxnSpPr>'
        f'<p:spPr><a:xfrm><a:off x="{E(x1)}" y="{E(ty)}"/><a:ext cx="{E(x2 - x1)}" cy="0"/></a:xfrm>'
        f'<a:prstGeom prst="line"><a:avLst/></a:prstGeom>'
        f'<a:ln w="{int(T["track_pt"] * 12700)}" cap="rnd"><a:gradFill rotWithShape="1"><a:gsLst>'
        f'<a:gs pos="0"><a:srgbClr val="{g0}"/></a:gs><a:gs pos="100000"><a:srgbClr val="{g1}"/></a:gs>'
        f'</a:gsLst><a:lin ang="0" scaled="0"/></a:gradFill><a:round/></a:ln></p:spPr></p:cxnSp>')
    spTree.append(track)
    tones = T["tones"]
    white = _token_color("brand.white") or "FFFFFF"
    for i, cx in enumerate(centers_in):
        tone = _token_color("brand." + tones[int(round(i * (len(tones) - 1) / max(1, n - 1)))])   # กระจายเฉดเข้ม→อ่อนตามจำนวนช่วง
        pin = parse_xml(
            f'<p:sp {A}><p:nvSpPr><p:cNvPr id="0" name="Milestone {i + 1}"/><p:cNvSpPr/><p:nvPr/></p:nvSpPr>'
            f'<p:spPr><a:xfrm><a:off x="{E(cx - d / 2)}" y="{E(ty - d / 2)}"/><a:ext cx="{E(d)}" cy="{E(d)}"/></a:xfrm>'
            f'<a:prstGeom prst="ellipse"><a:avLst/></a:prstGeom><a:solidFill><a:srgbClr val="{tone}"/></a:solidFill>'
            f'<a:ln w="19050"><a:solidFill><a:srgbClr val="{white}"/></a:solidFill></a:ln></p:spPr>'
            f'<p:txBody><a:bodyPr wrap="square" lIns="0" tIns="0" rIns="0" bIns="0" anchor="ctr" rtlCol="0"/><a:lstStyle/>'
            f'<a:p><a:pPr algn="ctr"/><a:r><a:rPr lang="en-US" sz="1400" b="1" dirty="0"><a:solidFill><a:srgbClr val="{white}"/></a:solidFill>'
            f'<a:latin typeface="{pin_font}"/><a:ea typeface="{pin_font}"/><a:cs typeface="{pin_font}"/></a:rPr>'
            f'<a:t>{i + 1}</a:t></a:r></a:p></p:txBody></p:sp>')
        spTree.append(pin)
    # id ของรูปทรงต้องไม่ซ้ำในสไลด์ — ให้ python-pptx จ่ายให้ใหม่
    used = max((int(el.get("id")) for el in spTree.iter() if el.tag.endswith("}cNvPr") and el.get("id", "0").isdigit()), default=1)
    for el in spTree.iter():
        if el.tag.endswith("}cNvPr") and el.get("id") == "0":
            used += 1
            el.set("id", str(used))


def tpl_timeline(prs, sl, deck, out_dir):
    s, lay = _tpl_slide(prs, "timeline", deck)
    s.shapes.title.text = sl.get("title", "")
    phases = (sl.get("phases") or [])[:4]
    n = len(phases)
    if n < 2:
        sys.exit(f"timeline '{sl.get('title', '')[:30]}': ต้องมี phases อย่างน้อย 2 ช่วง (ได้ {n})")
    # ISS-002: กระจาย placeholder ป้าย/รายละเอียดเต็มความกว้างตามจำนวนช่วงจริง แล้ววาดเส้นแกน+หมุดให้พอดี
    cw = SLIDE_W_IN - 2 * SAFE_MARGIN_IN
    seg = cw / n
    centers = [SAFE_MARGIN_IN + (i + 0.5) * seg for i in range(n)]
    T = TIMELINE
    for i, ph_ in enumerate(phases):
        for idx, key, y, h in ((i + 1, "label", T["label_y"], T["label_h"]), (i + 5, "text", T["detail_y"], T["detail_h"])):
            p = _ph(s, idx)
            if p is None:
                continue
            p.left, p.top = Inches(centers[i] - seg / 2 + 0.1), Inches(y)
            p.width, p.height = Inches(seg - 0.2), Inches(h)
            _set_text(p, ph_.get(key))
    rail_font = RAILS[deck.get("_rail", "private")]["font"]
    _timeline_track_and_pins(s, n, centers, rail_font)
    _title_icon(s, sl, deck, out_dir)
    return s, lay


def tpl_closing(prs, sl, deck, out_dir):
    s, lay = _tpl_slide(prs, "closing", deck)
    s.shapes.title.text = sl.get("title", "ขอบคุณ")
    _set_text(_ph(s, 1), sl.get("subtitle"))
    _set_text(_ph(s, 2), sl.get("contact"))
    return s, lay


def tpl_appendix(prs, sl, deck, out_dir):
    s, lay = _tpl_slide(prs, "appendix", deck)
    s.shapes.title.text = sl.get("title", "")
    _set_text(_ph(s, 1), sl.get("bullets"))
    _title_icon(s, sl, deck, out_dir)
    return s, lay


TEMPLATE_LAYOUTS = {
    "cover": tpl_cover, "divider": tpl_divider, "action-title-body": tpl_action_title_body,
    "two-column": tpl_two_column, "three-card": tpl_three_card, "table": tpl_table,
    "timeline": tpl_timeline, "closing": tpl_closing, "appendix": tpl_appendix,
}


def _version_stamp(out_path):
    """อ่านรหัสรุ่น V##R## และวันที่ YYYY.MM.DD จากชื่อไฟล์ผลลัพธ์ (กติกา PART 6: [Name]_V##R##_YYYY.MM.DD.ext) · ไม่พบ = None"""
    base = os.path.basename(out_path)
    ver = re.search(r"V\d{2,}R\d{2,}", base)
    date = re.search(r"\d{4}\.\d{2}\.\d{2}", base)
    return (ver.group(0) if ver else None), (date.group(0) if date else None)


def _fix_app_properties(out_path, spec, n_slides, title):
    """ข้อมูลกำกับส่วนขยาย (docProps/app.xml) ยังเป็นของแม่แบบเสมอ เพราะ python-pptx ไม่แตะไฟล์นี้
    ผลคือจำนวนสไลด์เป็น 0 และชื่อโปรแกรมเป็นของเครื่องที่ทำแม่แบบ ทำให้ระบบจัดเก็บเอกสารอ่านค่าผิด
    (พบจากผลตรวจของผู้ตรวจคุณภาพ 2026.09.06 · ตัวตรวจ validate_pptx_structure.py จับข้อนี้แล้ว)"""
    import re as _re
    import shutil as _sh
    import zipfile as _zip
    tmp = out_path + ".tmp"
    try:
        with _zip.ZipFile(out_path) as zin, _zip.ZipFile(tmp, "w", _zip.ZIP_DEFLATED) as zout:
            for item in zin.infolist():
                data = zin.read(item.filename)
                if item.filename == "docProps/app.xml":
                    xml = data.decode("utf-8")
                    xml = _re.sub(r"<Slides>\d*</Slides>", f"<Slides>{n_slides}</Slides>", xml)
                    xml = _re.sub(r"<TitlesOfParts>.*?</TitlesOfParts>", "", xml, flags=_re.S)
                    xml = _re.sub(r"<HeadingPairs>.*?</HeadingPairs>", "", xml, flags=_re.S)
                    if "<Company>" in xml:
                        xml = _re.sub(r"<Company>.*?</Company>", f"<Company>{spec.get('author', 'iCE Consulting')}</Company>", xml, flags=_re.S)
                    if "<TitleOfParts>" not in xml and "<Application>" in xml:
                        xml = _re.sub(r"<Application>.*?</Application>", "<Application>iCE build_pptx.py</Application>", xml, flags=_re.S)
                    data = xml.encode("utf-8")
                zout.writestr(item, data)
        _sh.move(tmp, out_path)
    except Exception as e:                      # ไฟล์ยังใช้ได้ ถ้าขั้นนี้ล้ม จึงไม่หยุดงาน
        print(f"⚠ เขียนข้อมูลกำกับส่วนขยายไม่สำเร็จ ({e}) — ไฟล์ยังใช้ได้ แต่ตัวตรวจจะรายงานข้อนี้")
        if os.path.exists(tmp):
            os.remove(tmp)


def _set_core_properties(prs, spec, out_path, template_path):
    """ISS-010: Document Properties ต้องเป็นของ deck ไม่ใช่ของแม่แบบ"""
    ver, date = _version_stamp(out_path)
    cp = prs.core_properties
    cp.title = spec.get("title", "") or os.path.splitext(os.path.basename(out_path))[0]
    cp.subject = spec.get("subject") or spec.get("subtitle", "") or ""
    cp.author = spec.get("author", "") or "iCE Consulting"
    cp.last_modified_by = cp.author
    cp.keywords = spec.get("keywords", "") or ""
    cp.category = spec.get("category", "") or ""
    cp.version = ver or ""
    cp.comments = (f"{ver or ''} {date or ''}".strip() + f" · สร้างจาก spec ด้วย build_pptx.py บนแม่แบบ "
                   f"{os.path.basename(template_path)}").strip(" ·")
    now = datetime.now()
    cp.created = cp.modified = cp.last_printed = now
    cp.revision = 1
    return ver, date


def build_with_template(prs, spec, out_path):
    """โหมดแม่แบบ — เติม placeholder ตามชื่อ layout · คืนจำนวนสไลด์"""
    out_dir = os.path.dirname(os.path.abspath(out_path))
    _remove_all_slides(prs)
    footer = spec.get("footer", "iCE Consulting · เอกสารลับ")
    # ISS-010: รหัสรุ่น + วันที่ ในแถบท้ายหน้าทุกหน้าเนื้อหา (อ่านจากชื่อไฟล์ผลลัพธ์ · ปิดด้วย "footer_version": false)
    ver, date = _version_stamp(out_path)
    if spec.get("footer_version", True):
        if ver:
            footer = f"{footer} · {ver}" + (f" · {date}" if date else "")
        else:
            print(f"⚠ ชื่อไฟล์ผลลัพธ์ไม่มีรหัสรุ่น V##R## ({os.path.basename(out_path)}) — footer จึงไม่มีรหัสรุ่น (กฎ H9)",
                  file=sys.stderr)
    for sl in spec["slides"]:
        name = TEMPLATE_LAYOUT_ALIAS.get(sl.get("layout", "bullets"), sl.get("layout"))
        fn = TEMPLATE_LAYOUTS.get(name)
        if fn is None:
            sys.exit(f"layout '{sl.get('layout')}' ไม่มีในแม่แบบ (ใช้ได้: {', '.join(TEMPLATE_LAYOUTS)})")
        s, lay = fn(prs, sl, spec, out_dir)
        _prune_empty(s)
        _clone_footer(s, lay, footer)
    if _DPI_WARNINGS:
        print(f"⚠ ภาพความละเอียดต่ำกว่า {ICON_MIN_DPI} dpi {len(_DPI_WARNINGS)} ชิ้น:", file=sys.stderr)
        for w in _DPI_WARNINGS[:MAX_DPI_SHOW]:
            print(f"   - {w}", file=sys.stderr)
    else:
        print(f"🖼 ภาพทุกชิ้นความละเอียดจริง ≥{ICON_MIN_DPI} dpi")
    return len(prs.slides)


MAX_DPI_SHOW = 10


LAYOUTS = {
    "title": add_title_slide,
    "section": add_section_slide,
    "bullets": add_bullets_slide,
    "two_column": add_two_column,
    "table": add_table,
    "kpi": add_kpi,
    "image": add_image,
    "thanks": add_title_slide,
}


def build(spec_path, out_path):
    with open(spec_path) as f:
        spec = json.load(f)
    # CHAR GUARD (Lesson #18): auto-replace PowerPoint-rejecting chars (→ ▸) before build
    spec, _n = _sanitize_chars(spec)
    if _n:
        print(f"CHAR-GUARD: replaced {_n} arrow char(s) (U+2192/etc → ▸) — would have caused PowerPoint Repair", file=sys.stderr)
    if ICE_TEMPLATE:
        # ⭐ V02R05 โหมดแม่แบบ — ขนาดสไลด์/ฟอนต์ theme/สี/โลโก้/footer มาจากไฟล์แม่แบบทั้งหมด
        if not os.path.isfile(ICE_TEMPLATE):
            sys.exit(f"ICE_TEMPLATE ชี้ไปไฟล์ที่ไม่มีอยู่จริง: {ICE_TEMPLATE}")
        prs = Presentation(ICE_TEMPLATE)
        print(f"🧩 แม่แบบ: {ICE_TEMPLATE} · layout: {', '.join(l.name for l in prs.slide_layouts)}")
    else:
        prs = Presentation()
        prs.slide_width = Inches(10)
        prs.slide_height = Inches(7.5)
    _check_background_origin(spec, out_path)
    theme = spec.get("theme", {})
    if not spec.get("slides"):
        spec["slides"] = [{"layout": "title", "title": spec.get("title", "Untitled"), "subtitle": spec.get("subtitle", "")}]
    elif spec["slides"][0].get("layout") not in ("title", "cover"):
        spec["slides"].insert(0, {"layout": "title", "title": spec.get("title", "Untitled"), "subtitle": spec.get("subtitle", "")})
    # ⭐ D1 — ฟอนต์มาจากราง (§3.0) · spec override ได้เมื่อลูกค้า/แบรนด์บังคับ
    rail, _why = infer_rail(spec, out_path)
    print(f"📄 ราง: {rail}  ({_why})")
    if rail not in RAILS:
        sys.exit(f"rail ต้องเป็น {'|'.join(RAILS)} (ได้: {rail})")
    font = spec.get("font_family") or RAILS[rail]["font"]

    if ICE_TEMPLATE:
        spec["_rail"] = rail                      # ให้รูปทรงที่ builder วาดเอง (หมุด timeline) ใช้ฟอนต์รางเดียวกัน
        build_with_template(prs, spec, out_path)
        _set_core_properties(prs, spec, out_path, ICE_TEMPLATE)     # ISS-010
    else:
        for slide in spec["slides"]:
            layout = slide.get("layout", "bullets")
            LAYOUTS.get(layout, add_bullets_slide)(prs, slide, theme)

    # ⭐ V02R03 (คำสั่ง user 2026.08.05) — สไลด์แน่น/ต้องบีบบรรทัด → DENSE_FONT ทั้งเด็ค
    #   เหตุผลเชิงตัวเลข: ยอดวรรณยุกต์ Leelawadee 0.737 em vs ฟอนต์ราง 0.924 em
    #   → เมื่อบีบ line-height ตัวที่ยอดสูงกว่าชนก่อน · PPTX ฝังฟอนต์ได้จึงไม่ห่วงเครื่องผู้รับ
    #   ปิดได้ด้วย spec["dense"] = false · บังคับเปิดด้วย spec["dense"] = true
    if not spec.get("font_family"):          # ผู้ใช้ระบุฟอนต์เองแล้ว = เคารพ ไม่แทรกแซง
        _forced = spec.get("dense")
        _dense, _dwhy = measure_slide_density(spec.get("slides", []))
        if _forced is True:
            _dense, _dwhy = True, "spec ระบุ dense=true"
        elif _forced is False:
            _dense, _dwhy = False, "spec ระบุ dense=false — ไม่สลับ"
        # ⚠ V02R04 (QA 2026.08.05): งานราชการ — ฟอนต์บังคับของ TOR ชนะกฎความแน่นเสมอ
        #   เจอจาก QA จริง: เด็ค TOR ที่แน่นถูกสลับทิ้งจาก TH Sarabun New → Leelawadee เงียบ ๆ
        #   auto-switch จึงทำเฉพาะราง private · ราง govt ต้องประกาศ dense=true เองเท่านั้น (มีร่องรอย)
        if _dense and rail != "private" and _forced is not True:
            print(f"🎚 สไลด์แน่น ({_dwhy}) แต่เป็นงานราชการ — คงฟอนต์ '{font}' ตามข้อบังคับ · "
                  f"บีบพื้นที่ด้วย line spacing/ลดเนื้อหาแทน · ยืนยันจะสลับจริง → ใส่ \"dense\": true")
            _dense = False
        if _dense and font != DENSE_FONT:
            print(f"🎚 สไลด์แน่น → เปลี่ยนทั้งเด็คเป็น '{DENSE_FONT}': {_dwhy}")
            print(f"   (ยอดวรรณยุกต์ 0.737 em เทียบ '{font}' 0.924 em = ไม่ชนเมื่อบีบบรรทัด"
                  f" · แลกกับไทยเล็กกว่าละตินมากขึ้น · ปิดด้วย \"dense\": false)")
            font = DENSE_FONT
        elif not _dense:
            print(f"🎚 ความแน่น: {_dwhy} → ใช้ฟอนต์ราง")

    # ⭐ V02R02: ด่านนโยบายก่อนสร้างไฟล์ — ผิดนโยบาย = แก้ให้เป็นฟอนต์ราง + แจ้ง (ไม่ fail)
    font, _notices, _ = resolve_font_policy(font, rail, spec)
    for _n in _notices:
        print(_n)
    n = apply_font(prs, font)
    prs.save(out_path)
    _fix_app_properties(out_path, spec, len(prs.slides), spec.get("title", ""))
    print(f"OK: wrote {out_path} with {len(prs.slides)} slides · "
          f"font='{font}' (rail={rail}) ผูกครบ 3 slot ใน {n} text frame")

    # post-build gate — จุดตรวจเดียวกับทุกฟอร์แมต
    subprocess.run([sys.executable, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                                 "audit_fonts.py"), "--rail", rail,
                    *(["--allow-font", font] if spec.get("font_family") else []), out_path])


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("usage: build_pptx.py spec.json out.pptx", file=sys.stderr)
        sys.exit(2)
    build(sys.argv[1], sys.argv[2])
