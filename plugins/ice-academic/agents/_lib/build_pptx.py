#!/usr/bin/env python3
"""
build_pptx.py — generic PPTX builder for sales agents.

Usage:
    python3 build_pptx.py spec.json out.pptx

FONT RULE (CRITICAL — established 2026-05-24):
  Default font is "Tahoma" for ALL text in mixed TH/EN decks.
  Reason: Tahoma is the only universally-available font with TRUE
  TH+Latin visual parity (cap-height + x-height + stroke-width match)
  in PowerPoint on both Windows and macOS.

  Do NOT use Sarabun (TH) + Calibri (EN) — Thai will look smaller.
  See pptx-builder-agent.md "Font Selection" section for full rationale.

  Override only when spec.json explicitly sets `"font_family": "..."` AND
  caller confirms font embedding is acceptable (+2-5 MB file size).

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
import sys, json
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE


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
    prs = Presentation()
    prs.slide_width = Inches(10)
    prs.slide_height = Inches(7.5)
    theme = spec.get("theme", {})
    if not spec.get("slides"):
        spec["slides"] = [{"layout": "title", "title": spec.get("title", "Untitled"), "subtitle": spec.get("subtitle", "")}]
    elif spec["slides"][0].get("layout") != "title":
        spec["slides"].insert(0, {"layout": "title", "title": spec.get("title", "Untitled"), "subtitle": spec.get("subtitle", "")})
    for slide in spec["slides"]:
        layout = slide.get("layout", "bullets")
        LAYOUTS.get(layout, add_bullets_slide)(prs, slide, theme)
    prs.save(out_path)
    print(f"OK: wrote {out_path} with {len(prs.slides)} slides")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("usage: build_pptx.py spec.json out.pptx", file=sys.stderr)
        sys.exit(2)
    build(sys.argv[1], sys.argv[2])
