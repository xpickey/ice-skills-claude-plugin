#!/usr/bin/env python3
"""
doc_to_md.py — แปลงเอกสารเป็น Markdown ในเครื่อง 100% + ตรวจความสมบูรณ์ภาษาไทย
V01R03 | 2026.08.07 | ผูกกับ skill ice-doc-reader
  V01R02 +OCR ในเครื่อง (macOS Vision · --ocr) + CMap suspect ลดเป็น flag (แก้ false positive)
  V01R03 (รีวิว) ฟอร์แมตไม่รองรับ/ไฟล์ว่าง/ไฟล์เสีย = exit 2 พร้อมข้อความชัด — เดิม .txt ได้
         ผลว่างเปล่าพร้อม exit 0 = ข้อมูลหายเงียบชนิดเดียวกับที่เครื่องมือนี้ตั้งใจกัน
  exit: 0=สะอาด(หรือไฟล์ text อ่านตรงได้) · 1=ไม่พบไฟล์ · 2=อ่านไม่ได้/ว่าง/ไม่รองรับ ·
        3=ข้อความไทยเสียหาย · 4=ไม่พบ venv

ทำไมต้องมี: การ "อ่านเอกสาร" ของ fleet เคยเป็นเรื่องเดา — แต่ละ agent ใช้เครื่องมือคนละตัว
(python-docx อ่านได้แต่ย่อหน้า · pdftotext ทำสระอำแตก · ฟอร์แมตแปลก ๆ อ่านไม่ได้เลย)
และ **ไม่มีใครตรวจว่าข้อความไทยรอดครบไหม** → ข้อมูลหายเงียบ ๆ ก่อนถึงคลังความรู้ด้วยซ้ำ

3 ขั้นที่ทำให้อัตโนมัติ:
  ① คัดกรอง (PDF เท่านั้น · pdf-inspector) — หน้าไหนเป็นภาพ อ่านข้อความไม่ได้ → เตือนก่อนแปลง
  ② แปลง (anydoc) — 16 นามสกุล → GitHub-Flavored Markdown
  ③ ตรวจไทย (ของเราเอง) — สระอำ/วรรณยุกต์รอดครบไหม · CMap พังไหม

⛔ ทุกขั้นรันในเครื่อง ไม่มี API ไม่มี cloud — เอกสารลูกค้า สัญญา งบการเงิน ไม่ออกจากเครื่อง

Usage:
    python3 doc_to_md.py FILE [-o OUT.md] [--ocr] [--inspect-only] [--quiet]
        --ocr = OCR หน้าที่เป็นภาพด้วย macOS Vision (ในเครื่อง · ต้องสั่งเอง)
    python3 doc_to_md.py --scan DIR          # กวาด PDF ทั้งโฟลเดอร์ ดูว่าอ่านได้ครบไหม

Interpreter: ต้องใช้ venv ของ fleet — เรียกผ่าน doc_to_md.sh หรือ
    ~/.claude/agents/_lib/.venv-doc/bin/python doc_to_md.py …
"""
import sys, os, re, glob, time, json

THAI_RE = re.compile(r"[฀-๿]")
SARA_AM_BROKEN = "ํา"          # นิคหิต + สระอา = สระอำที่แตก — สัญญาณชัดเจน ไม่กำกวม
FLOATING_TONE = re.compile(r"[ \t][่-๋]")   # วรรณยุกต์ตามหลังช่องว่าง = ผิดเสมอ

# ⚠ V01R02 (QA 2026.08.06): CMap garble ตรวจได้เฉพาะ PDF และเป็นแค่ "น่าสงสัย" ไม่ใช่ "พัง"
#   สัญญาณจริงคือวรรณยุกต์ถูกแทนด้วยตัวเลข/สัญลักษณ์ (ท่า→ท1า · จ้าง→จ@าง)
#   แต่ pattern ไทย+ตัวเลข+ไทย เป็นภาษาไทยปกติ (ย้อนหลัง4ปี · ข้อ5ก) → แยกด้วย regex ไม่ได้ 100%
#   ⇒ ① รันเฉพาะ .pdf (docx/pptx/xlsx ไม่มี CMap — เอากฎ PDF ไปใช้ผิดที่)
#      ② ตัดกรณีที่ตัวเลขคั่นแล้วอ่านได้ปกติ (ตามด้วยหน่วย/ลักษณนาม)
#      ③ รายงานเป็น "น่าสงสัย ให้คนดู" ไม่นับเป็น fail — เพราะอาจเป็นคำพิมพ์ผิดในต้นฉบับ
#         (พิสูจน์แล้ว: 'จำนว0น' มีอยู่ในไฟล์ TOR ต้นฉบับจริง = ผู้เขียนพิมพ์ผิดเอง)
CMAP_SUSPECT = re.compile(r"[ก-ฮ][0-9@#$%^&*](?=[ก-ฮ])")
_UNIT_AFTER = re.compile(r"^[0-9]+\s*(ปี|เดือน|วัน|ครั้ง|ชั่วโมง|นาที|ราย|คน|แห่ง|ข้อ|ชั้น|ระดับ)")


def check_thai(md: str, is_pdf: bool = False) -> dict:
    """ตรวจความสมบูรณ์ของข้อความไทย — ตัวนี้ขาดไม่ได้ ไม่มีใน anydoc/pdf-inspector

    hard fail (ชัดเจน): สระอำแตก · วรรณยุกต์ลอย
    soft flag (ให้คนดู): CMap suspect เฉพาะ PDF — อาจเป็นคำพิมพ์ผิดในต้นฉบับ
    """
    thai = len(THAI_RE.findall(md))
    broken_am = md.count(SARA_AM_BROKEN)
    floating = len(FLOATING_TONE.findall(md))

    suspects = []
    if is_pdf:
        for m in CMAP_SUSPECT.finditer(md):
            tail = md[m.start() + 1:m.start() + 12]
            if _UNIT_AFTER.match(tail):      # 'ย้อนหลัง4ปี' = ปกติ ไม่ใช่ความเสียหาย
                continue
            suspects.append(md[m.start():m.end() + 1])

    return {
        "thai_chars": thai,
        "sara_am_ok": md.count("ำ"),
        "sara_am_broken": broken_am,
        "floating_tone": floating,
        "cmap_suspect": len(suspects),
        "suspect_samples": suspects[:5],
        "clean": broken_am == 0 and floating == 0,   # suspect ไม่ทำให้ fail
    }


def inspect_pdf(path: str) -> dict:
    """① คัดกรอง PDF — หน้าไหนเป็นภาพ อ่านข้อความไม่ได้"""
    try:
        import pdf_inspector
    except ImportError:
        return {"available": False}
    try:
        c = pdf_inspector.classify_pdf(path)
    except Exception as e:
        # V01R03: PDF เสีย/ไม่ใช่ PDF จริง — บอกสั้น ๆ ไม่พ่น traceback
        return {"available": False, "corrupt": f"{type(e).__name__}: {str(e)[:120]}"}
    ocr = list(c.pages_needing_ocr or [])
    return {
        "available": True,
        "pdf_type": str(c.pdf_type),
        "page_count": c.page_count,
        "pages_needing_ocr": ocr,
        "readable_pages": c.page_count - len(ocr),
    }


def ocr_pdf_pages(path: str, pages: list, dpi: int = 200) -> dict:
    """③ OCR ในเครื่องด้วย macOS Vision — ยังไม่ออกนอกเครื่อง (คำสั่ง user 2026.08.06)

    ใช้เมื่อ pdf-inspector บอกว่าหน้าไหนเป็นภาพ · รองรับไทยตั้งแต่ macOS Sonoma
    วัดจริง: 1.75 วินาที/หน้า · สระอำแตก 0 · วรรณยุกต์ลอย 0
    """
    import subprocess, tempfile, glob as _g
    try:
        import Vision, Quartz
        from Foundation import NSURL
    except ImportError:
        return {"available": False,
                "hint": "ติดตั้ง: ~/.claude/agents/_lib/.venv-doc/bin/pip install "
                        "pyobjc-framework-Vision pyobjc-framework-Quartz"}
    if not shutil_which("pdftoppm"):
        return {"available": False, "hint": "ต้องมี pdftoppm (poppler) — brew install poppler"}

    out = {}
    with tempfile.TemporaryDirectory() as td:
        for pg in pages:
            n = pg + 1                                   # pdf-inspector = 0-indexed · pdftoppm = 1-indexed
            subprocess.run(["pdftoppm", "-png", "-r", str(dpi), "-f", str(n), "-l", str(n),
                            path, f"{td}/p"], capture_output=True)
            pngs = _g.glob(f"{td}/p-*.png")
            if not pngs:
                out[pg] = ""; continue
            src = Quartz.CGImageSourceCreateWithURL(NSURL.fileURLWithPath_(pngs[0]), None)
            img = Quartz.CGImageSourceCreateImageAtIndex(src, 0, None)
            req = Vision.VNRecognizeTextRequest.alloc().init()
            req.setRecognitionLevel_(Vision.VNRequestTextRecognitionLevelAccurate)
            req.setRecognitionLanguages_(["th-TH", "en-US"])
            req.setUsesLanguageCorrection_(True)
            h = Vision.VNImageRequestHandler.alloc().initWithCGImage_options_(img, None)
            h.performRequests_error_([req], None)
            out[pg] = "\n".join(o.topCandidates_(1)[0].string() for o in (req.results() or []))
            for f in pngs: os.remove(f)
    return {"available": True, "pages": out,
            "chars": sum(len(v) for v in out.values())}


def shutil_which(cmd):
    import shutil
    return shutil.which(cmd)


def convert(path: str, quiet=False, do_ocr=False) -> tuple:
    """② แปลง + ③ ตรวจไทย (+④ OCR ในเครื่องเมื่อสั่ง) · คืน (markdown, report)"""
    import anydoc
    rep = {"file": os.path.basename(path), "size_mb": round(os.path.getsize(path) / 1e6, 2)}

    if path.lower().endswith(".pdf"):
        ins = inspect_pdf(path)
        rep["inspect"] = ins
        if ins.get("available") and ins["pages_needing_ocr"]:
            n = len(ins["pages_needing_ocr"])
            rep["warning"] = (f"🔴 {n} จาก {ins['page_count']} หน้าเป็นภาพ — อ่านข้อความไม่ได้ "
                              f"(ต้อง OCR แยก) · Markdown ที่ได้จะขาดเนื้อหาส่วนนี้")

    t = time.time()
    md = ""
    try:
        if path.lower().endswith(".pdf"):
            md = anydoc.to_markdown_bytes(open(path, "rb").read(), "pdf")
        else:
            md = anydoc.to_markdown(path)
    except Exception as e:
        # PDF ที่เป็นภาพล้วน anydoc โยน UnsupportedError — ไม่ใช่ความผิดพลาด
        # แต่เป็นข้อเท็จจริงที่ต้องบอก user แล้วเดินต่อด้วย OCR (ถ้าสั่ง)
        if "OCR is required" in str(e) or "no extractable text" in str(e):
            rep["no_text_layer"] = True
            rep["warning"] = (f"🔴 PDF นี้ไม่มีชั้นข้อความเลย (เป็นภาพทั้งไฟล์) — anydoc อ่านไม่ได้")
        else:
            rep["error"] = f"{type(e).__name__}: {e}"
            rep["ms"] = round((time.time() - t) * 1000)
            rep["chars"] = 0
            rep["thai"] = check_thai("", is_pdf=False)
            return "", rep
    rep["ms"] = round((time.time() - t) * 1000)
    rep["chars"] = len(md)
    # ④ OCR ในเครื่อง — ทำเมื่อ user สั่ง --ocr เท่านั้น (ไม่ทำเอง · ใช้เวลา ~1.8 วิ/หน้า)
    ins = rep.get("inspect") or {}
    ocr_targets = ins.get("pages_needing_ocr") or (
        list(range(ins.get("page_count", 0))) if rep.get("no_text_layer") else [])
    if do_ocr and ocr_targets:
        o = ocr_pdf_pages(path, ocr_targets)
        rep["ocr"] = {k: v for k, v in o.items() if k != "pages"}
        if o.get("available"):
            parts = [md, "\n\n---\n\n## เนื้อหาจากหน้าที่เป็นภาพ (OCR ในเครื่อง · macOS Vision)\n"]
            for pg, txt in sorted(o["pages"].items()):
                parts.append(f"\n### หน้า {pg+1}\n\n{txt}\n")
            md = "".join(parts)
            rep["ocr"]["note"] = f"เติมเนื้อหา {len(o['pages'])} หน้า ({o['chars']:,} ตัวอักษร)"

    rep["chars"] = len(md)
    rep["thai"] = check_thai(md, is_pdf=path.lower().endswith(".pdf"))
    return md, rep


def print_report(rep: dict):
    ins = rep.get("inspect") or {}
    th = rep["thai"]
    print(f"  {rep['file']}  ({rep['size_mb']} MB · {rep['ms']} ms · {rep['chars']:,} ตัวอักษร)")
    if ins.get("available"):
        print(f"    ชนิด PDF : {ins['pdf_type']} · {ins['page_count']} หน้า "
              f"(อ่านข้อความได้ {ins['readable_pages']} หน้า)")
    if rep.get("warning"):
        print(f"    {rep['warning']}")
        if not rep.get("ocr"):
            print(f"    → ทางเลือก: ① ขอไฟล์ต้นฉบับที่เป็นข้อความจากผู้ส่ง (ดีที่สุด ไม่มีความเสี่ยง)")
            print(f"                ② OCR ในเครื่อง: เติม --ocr (macOS Vision · ~1.8 วิ/หน้า · ไฟล์ไม่ออกนอกเครื่อง)")
            print(f"                ③ ถ้ายังไม่ได้ผล → ขออนุญาต user ก่อนส่งให้บริการภายนอกช่วยอ่าน")
    if rep.get("ocr"):
        o = rep["ocr"]
        print(f"    OCR ในเครื่อง: {o.get('note') or o.get('hint') or 'ไม่สำเร็จ'}")
    if th["thai_chars"]:
        status = "✅ สะอาด" if th["clean"] else "🔴 พบความเสียหาย"
        print(f"    ข้อความไทย: {th['thai_chars']:,} อักขระ · สระอำ {th['sara_am_ok']:,} → {status}")
        if not th["clean"]:
            if th["sara_am_broken"]:
                print(f"      · สระอำแตก {th['sara_am_broken']} จุด (ค้นหา/copy จะพลาด)")
            if th["floating_tone"]:
                print(f"      · วรรณยุกต์ลอย {th['floating_tone']} จุด")

        if th.get("cmap_suspect"):
            print(f"    ⚠ น่าสงสัย {th['cmap_suspect']} จุด เช่น {th['suspect_samples'][:3]} — "
                  f"อาจเป็นวรรณยุกต์เพี้ยนจาก CMap ของ PDF **หรือคำพิมพ์ผิดในต้นฉบับ** "
                  f"→ เปิดดูจุดนั้นก่อนใช้อ้างอิง (ไม่นับเป็นความเสียหาย)")
    else:
        print(f"    (ไม่มีข้อความไทย)")


def scan_dir(d: str):
    """กวาด PDF ทั้งโฟลเดอร์ — ดูว่ามีไฟล์ไหนอ่านไม่ครบ ก่อนดูดเข้าคลัง"""
    pdfs = sorted(glob.glob(os.path.join(d, "**", "*.pdf"), recursive=True))
    print(f"  กวาด {len(pdfs)} ไฟล์ PDF ใน {d}\n")
    t = time.time(); bad = []
    types = {}
    for f in pdfs:
        try:
            ins = inspect_pdf(f)
            types[ins["pdf_type"]] = types.get(ins["pdf_type"], 0) + 1
            if ins["pages_needing_ocr"]:
                bad.append((os.path.basename(f), len(ins["pages_needing_ocr"]), ins["page_count"]))
        except Exception as e:
            types["error"] = types.get("error", 0) + 1
    print(f"  เสร็จใน {time.time()-t:.2f} วินาที")
    for k, v in sorted(types.items(), key=lambda x: -x[1]):
        print(f"    {k:<14} {v} ไฟล์")
    if bad:
        tot = sum(b[1] for b in bad)
        print(f"\n  🔴 อ่านข้อความไม่ได้ {len(bad)} ไฟล์ · รวม {tot} หน้า — ดูดเข้าคลังจะได้ข้อมูลไม่ครบ")
        for n, o, p in sorted(bad, key=lambda x: -x[1])[:10]:
            print(f"     {o:>4}/{p:<5} หน้า  {n[:60]}")
    else:
        print(f"\n  ✅ ทุกไฟล์อ่านข้อความได้ครบ")


if __name__ == "__main__":
    a = sys.argv[1:]
    if not a:
        print(__doc__.split("Usage:")[1].strip(), file=sys.stderr); sys.exit(2)

    if a[0] == "--scan":
        if len(a) < 2: sys.exit("ใช้: --scan DIR")
        scan_dir(a[1]); sys.exit(0)

    path = a[0]
    if not os.path.isfile(path):
        sys.exit(f"❌ ไม่พบไฟล์: {path}")

    # ⭐ V01R03 (รีวิว 2026.08.07): ตรวจฟอร์แมตก่อน — เดิมไฟล์ .txt/.md ได้ผลว่างเปล่า
    #   พร้อม exit 0 = ข้อมูลหายเงียบ ชนิดเดียวกับที่เครื่องมือนี้ตั้งใจกัน
    if os.path.getsize(path) == 0:
        print(f"❌ ไฟล์ว่างเปล่า (0 byte): {path} — แจ้ง user ขอไฟล์ใหม่", file=sys.stderr)
        sys.exit(2)
    TEXT_ALREADY = {".txt", ".md", ".markdown", ".json", ".yaml", ".yml", ".xml", ".html", ".htm", ".log"}
    ext = os.path.splitext(path)[1].lower()
    if ext in TEXT_ALREADY:
        print(f"ℹ {os.path.basename(path)} เป็นไฟล์ข้อความอยู่แล้ว — อ่านตรงได้เลย ไม่ต้องแปลง")
        sys.exit(0)
    import anydoc as _ad
    if ext != ".pdf" and _ad.format_from_path(path) is None:
        print(f"❌ ฟอร์แมต '{ext}' ไม่รองรับ (anydoc รองรับ 16 นามสกุล office/rtf/epub/csv/pdf) — "
              f"ห้ามเดาเนื้อหา แจ้ง user เลือกทางอื่น", file=sys.stderr)
        sys.exit(2)

    quiet = "--quiet" in a
    if "--inspect-only" in a:
        ins = inspect_pdf(path)
        print(json.dumps(ins, ensure_ascii=False, indent=2)); sys.exit(0)

    try:
        md, rep = convert(path, quiet, do_ocr="--ocr" in a)
    except Exception as e:
        print(f"❌ อ่านไฟล์ไม่ได้: {type(e).__name__}: {str(e)[:150]}", file=sys.stderr)
        print(f"   → แจ้ง user · ทางเลือก: ขอไฟล์ใหม่จากผู้ส่ง / ตรวจว่าไฟล์เสียหรือไม่ใช่ฟอร์แมตจริง",
              file=sys.stderr)
        sys.exit(2)
    if rep.get("error"):
        print(f"❌ อ่านไฟล์ไม่ได้: {rep['error'][:150]}", file=sys.stderr); sys.exit(2)
    if rep["chars"] == 0 and not rep.get("no_text_layer"):
        print(f"❌ แปลงแล้วได้เนื้อหาว่างเปล่า — ไฟล์อาจเสียหรือไม่มีข้อความ · แจ้ง user ห้ามใช้ต่อเงียบ ๆ",
              file=sys.stderr)
        sys.exit(2)
    out = None
    if "-o" in a:
        out = a[a.index("-o") + 1]
    elif not quiet:
        out = os.path.splitext(path)[0] + ".md"

    if out:
        open(out, "w", encoding="utf-8").write(md)
        if not quiet:
            print_report(rep)
            print(f"    → {out}")
    else:
        print(md)

    # exit≠0 เมื่อข้อความไทยเสียหาย — ให้ script ที่เรียกจับได้
    sys.exit(0 if rep["thai"]["clean"] else 3)
