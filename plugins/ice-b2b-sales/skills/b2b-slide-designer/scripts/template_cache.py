#!/usr/bin/env python3
"""template_cache.py — Cache-on-demand + availability check + graceful fallback.

เรียกใช้ template ตัวไหน → ทยอย copy เข้า assets/templates-cache/ (gitignored, local-only).
เช็คว่ายังอยู่ไหม. ถ้าหาย → fallback graceful (ไม่ crash).

Resolution order:
  1. cache (assets/templates-cache/) — มีแล้ว ใช้เลย
  2. src_path (จาก metadata) — ต้นทางบนเครื่องนี้ → copy เข้า cache + ใช้
  3. ไม่มีทั้งคู่ → return fallback dict (build จาก inspiration/MCP + แจ้ง user)

Usage:
  python template_cache.py get "<framework name>"   → resolve + cache + print JSON
  python template_cache.py check                     → health-check ทั้ง 73 หมวด
"""
import json
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SD = os.path.dirname(HERE)
META = os.path.join(SD, "references", "templates-cache-meta.json")
CACHE_DIR = os.path.join(SD, "assets", "templates-cache")


def load_meta():
    if not os.path.exists(META):
        return {}
    return json.load(open(META, encoding="utf-8")).get("templates", {})


def cache_name(fw):
    return "".join(c if c.isalnum() else "_" for c in fw) + ".pptx"


def resolve(fw):
    """cache-first → src → fallback. return {status, path|None, note}"""
    meta = load_meta()
    entry = meta.get(fw)
    cached = os.path.join(CACHE_DIR, cache_name(fw))

    # 1. cache hit
    if os.path.exists(cached):
        return {"status": "cache", "path": cached, "note": "from local cache"}

    # 2. src on this machine → copy into cache (ทยอยเก็บ)
    if entry and entry.get("src_path") and os.path.exists(entry["src_path"]):
        os.makedirs(CACHE_DIR, exist_ok=True)
        try:
            shutil.copy2(entry["src_path"], cached)
            return {"status": "cached-now", "path": cached,
                    "note": f"copied src → cache ({entry.get('slides', '?')} slides)"}
        except Exception as e:
            return {"status": "src-only", "path": entry["src_path"],
                    "note": f"src ok, cache failed: {e}"}

    # 3. fallback — template หาย (graceful, ไม่ crash)
    if entry:
        return {"status": "missing", "path": None,
                "note": (f"template '{fw}' หาย (เคยมี {entry.get('catalog_slides', '?')} slides). "
                         f"→ build จาก catalog-infographics (inspiration) หรือ MCP แทน. "
                         f"ต้นทางเดิม: {entry.get('src_path', '?')}")}
    return {"status": "unknown", "path": None,
            "note": f"ไม่รู้จัก template '{fw}' (ไม่อยู่ใน metadata)"}


def health_check():
    meta = load_meta()
    ok = miss = cached = 0
    missing = []
    for fw, e in meta.items():
        if os.path.exists(os.path.join(CACHE_DIR, cache_name(fw))):
            cached += 1
            ok += 1
        elif e.get("src_path") and os.path.exists(e["src_path"]):
            ok += 1
        else:
            miss += 1
            missing.append(fw)
    print(f"Health check: {len(meta)} templates · {ok} available "
          f"({cached} cached) · {miss} MISSING")
    if missing:
        print("  ⚠️ หาย (ต้นทางไม่พบ + ไม่มี cache):")
        for m in missing[:20]:
            print(f"     - {m}")
        print("  → ย้าย/ลบไฟล์ หรือย้ายเครื่อง? ดู migration guide ใน catalog-templates-ready.md")
    return miss == 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: template_cache.py get '<framework>' | check")
        sys.exit(1)
    if sys.argv[1] == "check":
        sys.exit(0 if health_check() else 1)
    elif sys.argv[1] == "get" and len(sys.argv) > 2:
        print(json.dumps(resolve(sys.argv[2]), ensure_ascii=False, indent=2))
    else:
        print("Usage: template_cache.py get '<framework>' | check")
        sys.exit(1)
