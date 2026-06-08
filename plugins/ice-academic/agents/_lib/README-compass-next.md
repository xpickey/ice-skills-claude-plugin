# _lib — Build Helper Modules (deliverable-gen-agent)

> **Owner:** deliverable-gen-agent (④) — เรียกใช้เป็น module (ไม่ใช่ sub-agent)
> **Purpose:** helper สำหรับ build .docx/.pptx/.xlsx ที่ฝัง 16 PPTX lessons + Build Discipline D1-D4
> **Status:** scaffold — implement จริงตอน build deck แรก (สกัดจาก TQR ice_deck_builder.py + ปรับตาม Build Discipline)

---

## Modules

```
_lib/
├── build_pptx.py    ← PPTX builder (16 lessons + D1-D4 tri-slot font + Strict Validator)
├── build_docx.py    ← DOCX builder (tri-slot font + bilingual)
├── build_xlsx.py    ← XLSX builder (live formula =NPV/IRR + no external-link)
└── font_utils.py    ← tri-slot binding (latin+ea+cs) + normalization map + optical size + embed (3 methods)
```

---

## build_pptx.py — MUST embed (จาก TQR §6.7 + Build Discipline)

```python
# CORE FUNCTIONS:
def new_deck():
    """16:9 deck — strip sldSz type='screen4x3' (ไม่งั้น render 4:3 overflow — qlmanage มองไม่เห็น)"""

def text(s, x, y, w, h, runs, ...):
    """แต่ละ run-tuple = SEPARATE LINE"""

def para_runs(s, x, y, w, h, run_lines, ...):
    """inline runs ON ONE LINE (EN+TH inline)"""

# D1 TRI-SLOT FONT (ทุก run):
def set_run_font(run, latin, cs, ea=None, sz_latin=None, sz_cs=None):
    """set <a:latin> + <a:ea> + <a:cs> → PowerPoint เลือก font ต่อ glyph
       cs=Thai font (Sarabun/Kanit) · sz_cs = sz_latin + 1-2pt (D3 optical)"""

# STRICT VALIDATOR (D4 — ก่อน return):
def validate_deck(path):
    """
    ✓ empty <a:t> == 0
    ✓ run-less <a:p> missing endParaRPr == 0
    ✓ sldSz NO type attr (16:9)
    ✓ no printerSettings
    ✓ collision: bbox overlap check
    ✓ overflow: text vs box (TH 1.15-1.20x)
    ✓ font: ทุก Thai run มี cs= · font count ≤ approved set
    ✓ embed: embedTrueTypeFonts (customer-facing)
    → return report + OPEN IN REAL POWERPOINT (qlmanage false-green)
    """

# FONT-EMBED (3 methods):
def embed_fonts(path, method="A"):
    """
    A (primary): soffice --headless --convert-to pptx:"Impress MS PowerPoint 2007 XML:EmbedFonts"
    B (fallback): manual inject ppt/fonts/*.fntdata + embeddedFontLst AFTER notesSz
    C (hybrid): python-pptx embedTrueTypeFonts=1
    PREREQ: static weights (Variable → fonttools instancer)
    """

# helpers: rect/oval/grad/node/chevron/gbar/icon — _noshadow() default · merge + page-renumber (defer)
```

---

## font_utils.py — D1/D2/D3

```python
PAIRED_FONTS = {
    "heading": {"en": "Raleway", "en_weight": "ExtraBold", "th": "Kanit", "th_weight": "Bold"},
    "body":    {"en": "Open Sans", "th": "Sarabun"},
    "alt":     {"en": "Inter", "th": "IBM Plex Sans Thai"},
    "govt":    {"th": "TH Sarabun New"},
}

# D2 NORMALIZATION MAP:
FONT_NORMALIZE = {
    "TH SarabunPSK": "Sarabun", "TH Sarabun PSK": "Sarabun", "THSarabunPSK": "Sarabun",
    "Tahoma": None,   # → paired spec (ถ้าไม่ตั้งใจ)
    "Calibri": None,  # ถ้า render ไทย → Sarabun
}

def normalize_fonts(deck):
    """enumerate fonts → rewrite variant → spec → report before/after count"""

# D3 OPTICAL:
TH_SIZE_DELTA = 1.5  # TH > EN +1-2pt
TH_MIN_BODY = 18; TH_MIN_HEADING = 24  # TH-only customer-facing
TH_WIDTH_FACTOR = 1.175  # 1.15-1.20x Latin
```

---

## build_xlsx.py — live formula (Banpu/EXIM lesson)

```python
def write_roi_model(...):
    """
    LIVE formula (ไม่ hardcode): =NPV(rate, CF1:CF10), =IRR(...), =SUM, payback
    anchored to named-range driver block (capex, discount_rate, cashflow)
    + cached <v> + fullCalcOnLoad (numbers แสดงก่อน Excel recalc)
    NO external links (flatten) · omit calcChain (Excel rebuild) · Thai via sharedStrings
    freeze header + data-validation dropdowns
    """
```

---

## 🚧 BUILD NOTE
- scaffold นี้ = spec/signature · implement จริงตอน build deck แรก (สกัดจาก TQR ice_deck_builder.py 273 lines + per-section scripts)
- font-embed Method A: ทดสอบ layout-shift ก่อน (LibreOffice อาจขยับ) → baseline

---

*_lib README | deliverable-gen-agent | 2026.06.01 | Implementation Backlog B1*
