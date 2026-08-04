#!/usr/bin/env python3
"""
audit_fonts.py — จุดตรวจฟอนต์ **จุดเดียว** ครอบทุกฟอร์แมต (xlsx/pptx/docx/html/pdf)
V01R01 | 2026.08.04 | ผูกกับ skill ice-doc-builder §3.0 FONT POLICY + §6 V1-V4

ทำไมต้องมีตัวเดียว (บทเรียน 2026.08.04 — เคส PWA TCO-Breakdown V01R22):
  เดิมมีตัวตรวจฟอนต์เฉพาะ .xlsx · ฟอร์แมตอื่นไม่มีเลย · แต่ละ build script ถือนโยบายของตัวเอง
  → นโยบายที่ LOCKED ไว้บังคับใช้ได้แค่ฟอร์แมตเดียว · user เป็นคนจับได้ ไม่ใช่ระบบ

⭐ หลักที่ยึด: **ตรวจเฉพาะฟอนต์ที่ถูกใช้กับข้อความไทยจริง**
  ไม่ใช่ที่ประกาศไว้ใน theme table — เพราะไฟล์ Office ไทยแทบทุกไฟล์พก Cordia/Angsana
  มาใน theme โดยไม่ได้ใช้ (sweep แรกของเคสนี้นับได้ 540 ไฟล์ = false positive ล้วน)

Usage:
    python3 audit_fonts.py [--rail private|govt] [--allow-font NAME]... FILE [FILE...]
    python3 audit_fonts.py --rail govt "(ร่าง_TOR).docx"
exit code: 0 = ผ่านทุกไฟล์ · 1 = มีไฟล์ FAIL · 2 = usage ผิด
"""
import sys, os, re, zipfile, subprocess

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from font_policy import RAILS, LATIN_ONLY, THAI_RE, check_fonts, installed_families

MAX_SHOW = 5          # §6 VALIDATION BUDGET — รายงาน counts + ตัวอย่าง ≤5 ห้าม dump XML
# ฟอนต์ fallback ของ Linux/LibreOffice = สัญญาณว่า renderer มองไม่เห็นฟอนต์ระบบ (render_pdf.sh)
PDF_FALLBACK_RE = re.compile(r"LinuxLibertine|FrankRuhl|DejaVu|Liberation", re.I)


def _thai_runs(xml: str, run_tag: str, text_tag: str):
    """คืน run ที่มีอักขระไทยจริง (ไม่ใช่ทุก run) — หัวใจของการไม่นับ theme table"""
    for r in re.findall(rf"<{run_tag}[ >].*?</{run_tag}>", xml, re.S):
        txt = "".join(re.findall(rf"<{text_tag}[^>]*>(.*?)</{text_tag}>", r, re.S))
        if THAI_RE.search(txt):
            yield r


# ── ตัวเก็บฟอนต์รายฟอร์แมต — คืน (fonts:set, extra_fails:list) ────────────────
def collect_pptx(path):
    fonts, nocs = set(), 0
    with zipfile.ZipFile(path) as z:
        for n in z.namelist():
            if not re.match(r"ppt/slides/slide\d+\.xml$", n):
                continue
            xml = z.read(n).decode("utf-8", "ignore")
            for r in _thai_runs(xml, "a:r", "a:t"):
                cs = re.findall(r'<a:cs typeface="([^"]+)"', r)
                fonts.update(cs)
                fonts.update(re.findall(r'<a:latin typeface="([^"]+)"', r))
                if not cs:
                    nocs += 1        # D1 — run ไทยไม่มี a:cs → PowerPoint เลือกฟอนต์เอง
    extra = ([f"D1 run ไทยที่ไม่ได้ตั้ง <a:cs> = {nocs} run "
              f"(PowerPoint จะเลือกฟอนต์เอง → ไทยเล็ก/ผิดตระกูล)"] if nocs else [])
    return fonts, extra


def collect_docx(path):
    fonts, nocs, inherited = set(), 0, None
    with zipfile.ZipFile(path) as z:
        names = z.namelist()
        # ⭐ ต้องอ่าน docDefaults ก่อนเสมอ — run ที่ไม่มี direct formatting **inherit** จากราก
        #   (ice-doc-builder §3.1: "run ที่ไม่มี direct formatting จะ inherit ถูกต้องเอง")
        #   ถ้าไม่เช็คตรงนี้ = ฟ้อง no-cs ทุก run ของไฟล์ที่ตั้งฟอนต์ถูกต้องที่ราก = false positive
        if "word/styles.xml" in names:
            sx = z.read("word/styles.xml").decode("utf-8", "ignore")
            m = re.search(r"<w:docDefaults>.*?</w:docDefaults>", sx, re.S)
            if m:
                cs = re.search(r'<w:rFonts[^>]*w:cs="([^"]+)"', m.group(0))
                if cs:
                    inherited = cs.group(1)
                    fonts.add(inherited)
            for st in re.findall(r"<w:style[ >].*?</w:style>", sx, re.S):
                fonts.update(re.findall(r'<w:rFonts[^>]*w:cs="([^"]+)"', st))
        if "word/document.xml" in names:
            xml = z.read("word/document.xml").decode("utf-8", "ignore")
            for r in _thai_runs(xml, "w:r", "w:t"):
                cs = re.findall(r'w:cs="([^"]+)"', r)
                fonts.update(cs)
                fonts.update(re.findall(r'w:ascii="([^"]+)"', r))
                if not cs:
                    nocs += 1
    # W1 เป็นข้อบกพร่องจริง **ก็ต่อเมื่อ** ราก (docDefaults) ไม่ได้ตั้ง w:cs ไว้ให้ inherit
    if nocs and not inherited:
        extra = [f"W1 run ไทย {nocs} run ไม่มี w:cs **และ docDefaults ก็ไม่ได้ตั้งไว้** → "
                 f"Word ถอยไป Times New Roman → substitute เป็น Angsana/Cordia เงียบ ๆ"]
    else:
        extra = []
        if nocs:
            print(f"   ℹ {nocs} run ไทยไม่มี w:cs ตรง ๆ แต่ inherit จาก docDefaults "
                  f"('{inherited}') — ถูกกฎตาม §3.1")
    return fonts, extra


def collect_html(path):
    txt = open(path, encoding="utf-8", errors="ignore").read()
    fonts = set()
    # ⚠ ค่าของ font-family ขึ้นต้นด้วย quote ได้ ("'IBM Plex...', 'Tahoma', ...")
    #   → char class ห้ามตัด quote ออก ไม่งั้น match ได้สตริงว่างทุกครั้ง
    for stack in re.findall(r"font-family\s*:\s*([^;}]+)", txt, re.I):
        for tok in stack.split(","):
            tok = tok.strip().strip("'\"")
            # ข้าม generic/keyword ของ CSS — ไม่ใช่ชื่อ family จริง
            if tok and not tok.startswith(("var(", "-apple-", "--")) and \
               tok.lower() not in ("sans-serif", "serif", "monospace", "system-ui",
                                   "inherit", "initial", "ui-sans-serif", "cursive"):
                fonts.add(tok)
                break                # เอาชื่อแรกของ stack = ตัวที่จะถูกใช้จริง
    return fonts, []


# PDF base-14 ที่ viewer มีในตัวเสมอ — ไม่ใช่ "ฟอนต์ที่เราเลือก" จึงไม่เอาเข้า V1/V4
PDF_BASE14 = {"symbol", "zapfdingbats"}
_STYLE_SUFFIX = re.compile(
    r"[-,](?:Regular|Bold|Italic|Oblique|BoldItalic|BoldOblique|Light|Medium|SemiBold"
    r"|DemiBold|Thin|Black|Heavy|ExtraLight|ExtraBold|Book|Roman|MT|PS|Condensed)+$", re.I)


def _squash(s):
    return re.sub(r"[^a-z0-9]", "", (s or "").lower())


def _pdf_family(raw, fams):
    """PDF ตัดช่องว่างในชื่อฟอนต์ทิ้ง ('TH SarabunPSK' → 'TH-SarabunPSK')
    → exact-match ใช้ไม่ได้ ต้องเทียบแบบ squash แล้ว map กลับเป็นชื่อ family จริง"""
    n = re.sub(r"^[A-Z]{6}\+", "", raw)          # subset prefix ABCDEF+
    n = _STYLE_SUFFIX.sub("", n)
    sq = _squash(n)
    for f in fams:                                # map กลับเป็นชื่อจริงถ้าเจอ
        if _squash(f) == sq:
            return f
    return n                                      # ไม่เจอ → คืนชื่อดิบ ให้ V1 ฟ้องตามจริง


def collect_pdf(path, fams=None):
    try:
        out = subprocess.run(["pdffonts", path], capture_output=True, text=True, timeout=60).stdout
    except FileNotFoundError:
        return set(), ["⚠ ไม่มี pdffonts — ข้ามการตรวจ (ไม่ใช่ 'ผ่าน')"]
    fams = fams if fams is not None else installed_families()
    fonts, fails, noemb = set(), [], []
    lines = out.splitlines()
    if len(lines) < 2:
        return fonts, fails
    # ⚠ pdffonts เป็นตารางความกว้างคงที่ และ **ชื่อฟอนต์มีช่องว่างได้** ('TH SarabunPSK')
    #   → ห้ามใช้ line.split() (เคยทำให้ 'TH SarabunPSK' เหลือ 'TH')
    #   บรรทัดที่ 2 เป็นแถวขีด --- ใช้บอกความกว้างแต่ละคอลัมน์
    widths, pos = [], 0
    for seg in lines[1].split(" "):
        widths.append((pos, pos + len(seg)))
        pos += len(seg) + 1
    if len(widths) < 4:
        return fonts, fails
    name_c, emb_c = widths[0], widths[3]
    for line in lines[2:]:
        # ⚠ pdffonts จัดคอลัมน์ตาม **ไบต์** ไม่ใช่ตัวอักษร — ชื่อไทย (๙ = 3 ไบต์ UTF-8)
        #   ทำให้ slice ด้วย index ตัวอักษรกินคอลัมน์ถัดไป ('TH SarabunIT๙  C')
        b = line.encode("utf-8")
        raw = b[name_c[0]:name_c[1]].decode("utf-8", "ignore").strip()
        if not raw:
            continue
        fam = _pdf_family(raw, fams)
        if _squash(fam) not in PDF_BASE14:
            fonts.add(fam)
        if b[emb_c[0]:emb_c[1]].decode("utf-8", "ignore").strip() == "no":
            noemb.append(raw)
    if noemb:
        fails.append(f"PDF มีฟอนต์ที่ไม่ได้ฝัง {len(noemb)} ตัว: {noemb[:MAX_SHOW]}")
    hit = [f for f in fonts if PDF_FALLBACK_RE.search(f)]
    if hit:
        fails.append(f"🔴 พบฟอนต์ fallback ของ Linux/LibreOffice {hit} — renderer มองไม่เห็นฟอนต์ระบบ "
                     f"→ ตรวจ `render_pdf.sh --which` ก่อนสรุปว่าไฟล์พัง (ผลจาก renderer ผิดตัว = หลักฐานปลอม)")
    return fonts, fails


COLLECTORS = {".pptx": collect_pptx, ".docx": collect_docx,
              ".html": collect_html, ".htm": collect_html, ".pdf": collect_pdf}


def audit_file(path, rail="private", allow=None, fams=None) -> bool:
    """คืน True = ผ่าน"""
    ext = os.path.splitext(path)[1].lower()
    print(f"\n━━ {os.path.basename(path)}  [rail={rail}]")
    if not os.path.exists(path):
        print("   ❌ ไม่พบไฟล์"); return False

    if ext == ".xlsx":
        # xlsx มีตัวตรวจเต็ม (E2-E5 + T2 word-break) อยู่แล้ว — delegate ไม่ทำซ้ำ
        import build_xlsx
        rep = build_xlsx.audit(path, strict=False, rail=rail, allow_fonts=allow)
        return not rep["fails"]

    if ext not in COLLECTORS:
        print(f"   ⚠ ไม่รองรับนามสกุล {ext} — ข้าม (ไม่ใช่ 'ผ่าน')"); return True

    try:
        # PDF ต้องใช้รายชื่อฟอนต์ที่ติดตั้งเพื่อ map ชื่อที่ถูกตัดช่องว่างกลับเป็น family จริง
        fonts, extra = (collect_pdf(path, fams) if ext == ".pdf" else COLLECTORS[ext](path))
    except Exception as e:
        print(f"   ❌ อ่านไฟล์ไม่ได้: {e}"); return False

    if not fonts and not extra:
        print("   ℹ ไม่พบข้อความไทยที่ตั้งฟอนต์ไว้ — ไม่มีอะไรให้ตรวจ"); return True

    if ext == ".pdf":
        # ⭐ PDF ใช้เกณฑ์ต่างจากฟอร์แมตต้นทาง — เพราะ pdffonts ไม่บอกว่าฟอนต์ไหนอยู่บนข้อความไทย
        #   renderer ฝังฟอนต์ UI/สัญลักษณ์ของตัวเอง (Hiragino/LucidaGrande/ZapfDingbats) ตามปกติ
        #   → ถาม "ฟอนต์ของรางอยู่ในไฟล์จริงไหม" แทน "มีฟอนต์อื่นปนไหม" · V1 ข้าม (ชื่อถูก subset/ตัดช่องว่าง)
        want = RAILS[rail]["font"]
        ok_present = any(_squash(want) == _squash(f) or _squash(f) in
                         {_squash(a) for a in (allow or ())} or
                         _squash(RAILS[rail]["fallback"]) == _squash(f) for f in fonts)
        print(f"   fonts ที่ฝังใน PDF: {', '.join(sorted(fonts)) or '(none)'}")
        fails = list(extra)
        for n in sorted(fonts):
            from font_policy import blacklist_hit
            why = blacklist_hit(n)
            if why:
                fails.append(f"V2 BLACKLIST ใน PDF: '{n}' — {why}")
        if not ok_present:
            fails.append(f"V4 ไม่พบฟอนต์ของราง '{rail}' ('{want}') ใน PDF เลย → ถูก substitute ไปแล้ว")
        if fails:
            print("   ❌ FAIL:")
            for f in fails[:MAX_SHOW]:
                print("      -", f)
            if len(fails) > MAX_SHOW:
                print(f"      … อีก {len(fails)-MAX_SHOW} รายการ")
            return False
        print(f"   ✅ PASS — ฝังครบ · ไม่มี blacklist · พบฟอนต์ของราง '{rail}'")
        return True

    rep = check_fonts(fonts, rail=rail, allow_fonts=allow, fams=fams)
    print(f"   fonts (บนข้อความไทย): {', '.join(rep['fonts_used']) or '(none)'}"
          + ("   ⚠ V1 SKIPPED (ไม่มี fontTools)" if rep["v1_skipped"] else ""))
    fails = rep["fails"] + extra
    if fails:
        print("   ❌ FAIL:")
        for f in fails:
            print("      -", f)
        return False
    print(f"   ✅ PASS — V1 resolve ครบ · V2 ไม่มี blacklist · V4 ตรงราง '{rail}'")
    return True


if __name__ == "__main__":
    argv, rail, allow = sys.argv[1:], "private", set()
    while len(argv) >= 2 and argv[0] in ("--rail", "--allow-font"):
        if argv[0] == "--rail":
            rail = argv[1]
            if rail not in RAILS:
                sys.exit(f"--rail ต้องเป็น {'|'.join(RAILS)} (ได้: {rail})")
        else:
            allow.add(argv[1])
        argv = argv[2:]
    if not argv:
        print(__doc__.split("Usage:")[1].strip(), file=sys.stderr); sys.exit(2)
    # อาร์กิวเมนต์ที่ขึ้นต้นด้วย -- แต่ไม่รู้จัก = พิมพ์ผิด/quote ผิด — ห้ามเข้าใจเป็นชื่อไฟล์เงียบ ๆ
    # (เจอจริงตอนทดสอบ: zsh ไม่ word-split ตัวแปร → ส่ง "--rail govt" มาเป็นอาร์กิวเมนต์เดียว
    #  แล้วถูกนับเป็นไฟล์ → รายงาน FAIL ที่ไม่ใช่ความผิดของไฟล์)
    bad = [a for a in argv if a.startswith("--")]
    if bad:
        sys.exit(f"❌ อาร์กิวเมนต์ไม่รู้จัก (หรือ quote ผิด): {bad}\n"
                 f"   ใช้: audit_fonts.py [--rail private|govt] [--allow-font NAME]... FILE...")

    shared = installed_families()      # enumerate ฟอนต์ครั้งเดียว ใช้ร่วมทุกไฟล์ (แพง)
    ok = all([audit_file(p, rail, allow, shared) for p in argv])
    print(f"\n{'✅ ผ่านทั้งหมด' if ok else '❌ มีไฟล์ที่ไม่ผ่าน'} ({len(argv)} ไฟล์ · rail={rail})")
    sys.exit(0 if ok else 1)
