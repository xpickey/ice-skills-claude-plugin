#!/usr/bin/env python3
"""build_template_meta.py — สกัด metadata จาก 71 framework .pptx → templates-cache-meta.json
metadata = slide-count + shape summary + framework + size (เล็ก, เข้า git, portable ข้ามเครื่อง).
binary .pptx ไม่เข้า git (cache-on-demand) — metadata นี้ทำให้ย้ายเครื่องยังรู้ว่า template มีอะไร.

Usage: python build_template_meta.py [catalog-templates-ready.md]
"""
import json, os, re, sys, zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
SD = os.path.dirname(HERE)
CATALOG = sys.argv[1] if len(sys.argv) > 1 else os.path.join(SD, "references", "catalog-templates-ready.md")

def pptx_meta(path):
    """slide-count + shape-type summary + size — ไม่เก็บ binary"""
    try:
        with zipfile.ZipFile(path) as z:
            slides = [n for n in z.namelist() if re.match(r'ppt/slides/slide\d+\.xml$', n)]
            # นับ shape คร่าว ๆ จาก slide แรก (โครงสร้าง)
            shapes = 0
            if slides:
                xml = z.read(slides[0]).decode('utf-8', 'ignore')
                shapes = xml.count('<p:sp>') + xml.count('<p:pic>') + xml.count('<p:graphicFrame>')
        return {"slides": len(slides), "shapes_slide1": shapes,
                "size_kb": os.path.getsize(path) // 1024, "openable": True}
    except Exception as e:
        return {"openable": False, "error": str(e)[:60]}

def main():
    meta = {"_note": "metadata cache (portable, in git) — binary .pptx is cache-on-demand (gitignored). "
                     "ย้ายเครื่อง: metadata บอกว่า template มีกี่ slide/หน้าตาไง → build จาก inspiration ถ้า binary หาย.",
            "_generated_from": os.path.basename(CATALOG), "templates": {}}
    if not os.path.exists(CATALOG):
        print(f"catalog not found: {CATALOG}"); return
    txt = open(CATALOG, encoding='utf-8').read()
    # parse rows: | **Name** | slides | `path` | pdf |
    for m in re.finditer(r'\|\s*\*\*([^*]+)\*\*\s*\|\s*(\d+)\s*\|\s*`([^`]+)`', txt):
        name, slides_str, path = m.group(1).strip(), m.group(2), m.group(3).strip()
        info = {"framework": name, "src_path": path, "catalog_slides": int(slides_str)}
        if os.path.exists(path):
            info.update(pptx_meta(path))
        else:
            info["openable"] = False; info["error"] = "src not found on this machine"
        meta["templates"][name] = info
    out = os.path.join(SD, "references", "templates-cache-meta.json")
    json.dump(meta, open(out, 'w'), indent=2, ensure_ascii=False)
    ok = sum(1 for v in meta["templates"].values() if v.get("openable"))
    print(f"✅ {out}")
    print(f"   {len(meta['templates'])} templates · {ok} openable on this machine")

if __name__ == "__main__":
    main()
