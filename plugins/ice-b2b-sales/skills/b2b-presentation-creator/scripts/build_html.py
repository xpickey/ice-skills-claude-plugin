#!/usr/bin/env python3
# ============================================================
# build_html.py — HTML Presentation Slide builder (skill-owned)
#
# Renders a single self-contained .html deck (zero-dependency,
# fixed 16:9 stage, inline CSS/JS) from an outline JSON.
#
# Stage model, viewport CSS, and JS scaling/nav approach adapted from
# frontend-slides (MIT (c) 2025 Zara Zhang)
# https://github.com/zarazhangrui/frontend-slides
# See references/NOTICE-html-slides.md for full license.
#
# Design principles (60-30-10, WCAG, 8pt grid, ≤4 type sizes ...) follow
# power-design (MIT (c) 2026 Jack Roberts) — see references/design-principles.md
#
# Usage:
#   python build_html.py --outline outline.json \
#       [--css-vars theme-vars.json] [--title "Deck Title"] \
#       --output Deck_Customer_V01R01_2026-06-20.html
#
# outline.json schema (minimal):
#   {
#     "title": "Deck title",
#     "css_vars": { "--accent": "#1E66A4", "--font-display": "Kanit", ... },
#     "slides": [
#       { "title": "...", "subtitle": "...",
#         "bullets": ["...","..."],         # OR
#         "body": "free HTML/text",
#         "image": "assets/x.png",          # optional
#         "notes": "speaker notes",         # optional -> HTML comment
#         "layout": "title|content|section|quote"  # optional, default content
#       }
#     ]
#   }
#
# The deck is bilingual-safe (TH+EN): css_vars feed --font-display / --font-body
# chosen by b2b-slide-designer §5.6 (web-safe fallback stack). This script does
# NOT pick fonts — it consumes the spec the skill hands it.
# ============================================================

import argparse
import html as _html
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
VIEWPORT_CSS = os.path.join(HERE, "..", "assets", "html", "viewport-base.css")

# ---- forbidden-char guard (mirror of PPTX Lesson #18; harmless in HTML but
#      kept for cross-format consistency so copy pasted between PPTX/HTML is safe)
ARROW_MAP = {"→": "▸", "⟶": "▸", "➙": "▸",
             "➔": "▸", "➘": "▸"}


def sanitize(text):
    if not text:
        return ""
    for bad, good in ARROW_MAP.items():
        text = text.replace(bad, good)
    return text


def esc(text):
    return _html.escape(sanitize(str(text)))


def load_viewport_css():
    try:
        with open(VIEWPORT_CSS, encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        sys.stderr.write(f"WARN: viewport-base.css not found at {VIEWPORT_CSS}; "
                         "using inline fallback.\n")
        # minimal fallback so the deck still renders
        return (".deck-stage{position:absolute;left:0;top:0;width:1920px;"
                "height:1080px;transform-origin:0 0;overflow:hidden}"
                ".slide{position:absolute;inset:0;width:1920px;height:1080px;"
                "visibility:hidden;opacity:0}"
                ".slide.active,.slide.visible{visibility:visible;opacity:1;z-index:1}")


# ---- default theme tokens (overridable by outline css_vars) ----
DEFAULT_VARS = {
    "--stage-bg": "#0d1117",
    "--slide-bg": "#ffffff",
    "--text-primary": "#141413",
    "--text-muted": "#6e6b66",
    "--accent": "#1E66A4",          # iCE Blue default
    "--accent-2": "#41A8B5",        # iCE Cyan
    "--font-display": "'Kanit', 'Raleway', system-ui, sans-serif",
    "--font-body": "'Sarabun', 'Open Sans', system-ui, sans-serif",
    # authored at 1920x1080 stage size (power-design rule 8: title >=48px)
    "--title-size": "112px",
    "--subtitle-size": "40px",
    "--body-size": "30px",
    "--slide-padding": "112px",     # ~5% safe-zone (power-design rule 5)
    "--content-gap": "32px",
    "--ease": "cubic-bezier(0.16,1,0.3,1)",
}

# Google Fonts the default tokens rely on (web-safe per slide-designer §5.6)
FONT_LINK = ('<link href="https://fonts.googleapis.com/css2?'
             'family=Kanit:wght@400;600;700&family=Sarabun:wght@300;400;600&'
             'family=Raleway:wght@600;800&family=Open+Sans:wght@400;600&'
             'display=swap" rel="stylesheet">')


def render_vars(css_vars):
    merged = dict(DEFAULT_VARS)
    if css_vars:
        merged.update(css_vars)
    lines = "\n".join(f"  {k}: {v};" for k, v in merged.items())
    return f":root {{\n{lines}\n}}"


BASE_STYLE = """
.slide { padding: var(--slide-padding); box-sizing: border-box;
  font-family: var(--font-body); color: var(--text-primary);
  background: var(--slide-bg); display: flex; flex-direction: column;
  justify-content: center; }
.slide h1 { font-family: var(--font-display); font-size: var(--title-size);
  line-height: 1.08; margin: 0 0 var(--content-gap); font-weight: 700; }
.slide h2 { font-family: var(--font-display); font-size: var(--subtitle-size);
  line-height: 1.2; margin: 0 0 var(--content-gap); font-weight: 600;
  color: var(--accent); }
.slide p, .slide li { font-size: var(--body-size); line-height: 1.5; }
.slide ul { margin: 0; padding-left: 1.2em; }
.slide li { margin-bottom: 16px; }   /* 8pt grid (power-design rule 15) */
.slide .accent-bar { width: 120px; height: 10px; background: var(--accent);
  margin-bottom: 40px; }
.slide.layout-title { align-items: flex-start; }
.slide.layout-title h1 { font-size: calc(var(--title-size) * 1.15); }
.slide.layout-section { background: var(--accent); color: #fff;
  justify-content: center; align-items: flex-start; }
.slide.layout-section h1 { color: #fff; }
.slide.layout-quote { justify-content: center; }
.slide.layout-quote p { font-size: 64px; font-family: var(--font-display);
  font-style: italic; max-width: 1400px; }
.slide .deck-img { max-height: 60%; margin-top: var(--content-gap);
  object-fit: contain; }
.reveal { opacity: 0; transform: translateY(28px);
  transition: opacity .6s var(--ease), transform .6s var(--ease); }
.slide.visible .reveal { opacity: 1; transform: translateY(0); }
.slide.visible .reveal:nth-child(2){transition-delay:.08s}
.slide.visible .reveal:nth-child(3){transition-delay:.16s}
.slide.visible .reveal:nth-child(4){transition-delay:.24s}
.slide.visible .reveal:nth-child(5){transition-delay:.32s}
.deck-controls { color: #fff; font: 14px var(--font-body); opacity:.6 }
"""

JS_CONTROLLER = r"""
<script>
(function(){
  var stage = document.getElementById('deckStage');
  var slides = Array.prototype.slice.call(document.querySelectorAll('.slide'));
  var i = 0;
  function fit(){
    var f = Math.min(window.innerWidth/1920, window.innerHeight/1080);
    var x = (window.innerWidth - 1920*f)/2, y = (window.innerHeight - 1080*f)/2;
    stage.style.transform = 'translate('+x+'px,'+y+'px) scale('+f+')';
  }
  function show(n){
    i = Math.max(0, Math.min(slides.length-1, n));
    slides.forEach(function(s,idx){ s.classList.toggle('visible', idx===i);
      s.classList.toggle('active', idx===i); });
    var c = document.getElementById('deckCounter');
    if(c) c.textContent = (i+1)+' / '+slides.length;
  }
  function next(){ show(i+1); } function prev(){ show(i-1); }
  window.addEventListener('resize', fit);
  document.addEventListener('keydown', function(e){
    if(['ArrowRight','ArrowDown',' ','PageDown'].indexOf(e.key)>-1){e.preventDefault();next();}
    else if(['ArrowLeft','ArrowUp','PageUp'].indexOf(e.key)>-1){e.preventDefault();prev();}
    else if(e.key==='Home'){show(0);} else if(e.key==='End'){show(slides.length-1);}
  });
  // touch
  var sx=0; document.addEventListener('touchstart',function(e){sx=e.touches[0].clientX;});
  document.addEventListener('touchend',function(e){
    var dx=e.changedTouches[0].clientX-sx;
    if(Math.abs(dx)>50){ dx<0?next():prev(); }
  });
  fit(); show(0);
})();
</script>
"""


def slide_html(s):
    layout = s.get("layout", "content")
    parts = [f'<section class="slide layout-{esc(layout)}">']
    if s.get("notes"):
        parts.append(f"<!-- Notes: {esc(s['notes'])} -->")
    if layout in ("content", "title") and s.get("title"):
        parts.append('<div class="accent-bar reveal"></div>')
    if s.get("title"):
        parts.append(f'<h1 class="reveal">{esc(s["title"])}</h1>')
    if s.get("subtitle"):
        parts.append(f'<h2 class="reveal">{esc(s["subtitle"])}</h2>')
    if s.get("bullets"):
        items = "".join(f'<li class="reveal">{esc(b)}</li>' for b in s["bullets"])
        parts.append(f"<ul>{items}</ul>")
    if s.get("body"):
        parts.append(f'<p class="reveal">{esc(s["body"])}</p>')
    if s.get("image"):
        parts.append(f'<img class="deck-img reveal" src="{esc(s["image"])}" alt="">')
    parts.append("</section>")
    return "\n".join(parts)


def build(outline, title_override=None, css_vars_override=None):
    title = title_override or outline.get("title", "Presentation")
    css_vars = dict(outline.get("css_vars", {}))
    if css_vars_override:
        css_vars.update(css_vars_override)
    slides = outline.get("slides", [])
    if not slides:
        raise ValueError("outline has no slides")

    body = "\n".join(slide_html(s) for s in slides)
    doc = f"""<!DOCTYPE html>
<html lang="th">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
{FONT_LINK}
<style>
{render_vars(css_vars)}

/* === viewport-base (fixed 16:9 stage) === */
{load_viewport_css()}

/* === deck base styles === */
{BASE_STYLE}
</style>
</head>
<body>
<div class="deck-viewport">
  <main class="deck-stage" id="deckStage">
{body}
  </main>
</div>
<div class="deck-controls"><span id="deckCounter"></span></div>
{JS_CONTROLLER}
</body>
</html>
"""
    return doc


def main():
    ap = argparse.ArgumentParser(description="Build a single-file HTML deck from an outline.")
    ap.add_argument("--outline", required=True, help="outline JSON path")
    ap.add_argument("--css-vars", help="optional JSON of CSS var overrides")
    ap.add_argument("--title", help="override deck title")
    ap.add_argument("--output", required=True, help="output .html path")
    a = ap.parse_args()

    with open(a.outline, encoding="utf-8") as f:
        outline = json.load(f)
    css_vars = None
    if a.css_vars:
        with open(a.css_vars, encoding="utf-8") as f:
            css_vars = json.load(f)

    doc = build(outline, title_override=a.title, css_vars_override=css_vars)
    with open(a.output, "w", encoding="utf-8") as f:
        f.write(doc)
    n = len(outline.get("slides", []))
    print(f"Built HTML deck: {a.output}  ({n} slides, {len(doc)} bytes)")


if __name__ == "__main__":
    main()
