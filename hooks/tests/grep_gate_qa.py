#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""grep-gate ปลายทางของ Pass 3 (qa-master-agent) — grep_gate_qa.py (V01R01 · 2026.09.05)

อ่านตารางใน qa-master-agent.inventory.md แล้วตรวจทุกแถว:
  คง                → ทุกคำสำคัญต้องพบใน qa-master-agent.proposed.md
  ย้ายไป <path>      → ทุกคำสำคัญต้องพบในไฟล์ปลายทาง
  ลบ — บ้าน <path>   → ทุกคำสำคัญต้องพบในไฟล์บ้านที่ระบุ (ยืนยันว่าบ้านนั้นมีเรื่องนี้จริง จึงลบจากไฟล์ agent ได้)
วิธีใช้: python3 hooks/tests/grep_gate_qa.py [inventory.md] [proposed.md]
ผล: รายงานผ่าน/ตกรายแถว · exit 0 = ผ่านทุกแถว · exit 2 = มีแถวตก
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
AG = os.path.join(REPO, "plugins", "ice-b2b-sales", "agents")
INV = sys.argv[1] if len(sys.argv) > 1 else os.path.join(AG, "qa-master-agent.inventory.md")
PROP = sys.argv[2] if len(sys.argv) > 2 else os.path.join(AG, "qa-master-agent.proposed.md")

_cache = {}


def read(path):
    path = os.path.expanduser(path)
    if path not in _cache:
        _cache[path] = open(path, encoding="utf-8").read() if os.path.exists(path) else None
    return _cache[path]


def main():
    rows = []
    for line in open(INV, encoding="utf-8"):
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        # คำสำคัญคั่นด้วย \| (escaped pipe) — คืนค่าให้เป็น | ก่อนแยก
        if len(cells) < 4 or not cells[0].isdigit():
            continue
        rows.append(cells)
    # การ split ข้างบนตัดที่ \| ด้วย — อ่านใหม่แบบระวัง escape
    rows = []
    for line in open(INV, encoding="utf-8"):
        if not line.startswith("|"):
            continue
        parts = re.split(r"(?<!\\)\|", line.strip().strip("|"))
        cells = [c.strip().replace("\\|", "|") for c in parts]
        if len(cells) < 4 or not cells[0].isdigit():
            continue
        rows.append(cells)

    fails, passes = [], 0
    for num, rule, dest, kw in rows:
        keys = [k.strip() for k in kw.split(" | ") if k.strip()]
        if dest.startswith("คง"):
            target = PROP
        elif dest.startswith("ย้ายไป"):
            target = dest.replace("ย้ายไป", "", 1).strip()
        elif dest.startswith("ลบ"):
            m = re.search(r"บ้าน\s+(\S+)", dest)
            target = m.group(1) if m else ""
        else:
            fails.append((num, rule[:50], f"ช่องปลายทางอ่านไม่ออก: {dest}"))
            continue
        text = read(target)
        if text is None:
            fails.append((num, rule[:50], f"ไม่พบไฟล์ปลายทาง {target}"))
            continue
        missing = [k for k in keys if k not in text]
        if missing:
            fails.append((num, rule[:50], f"{os.path.basename(target)} ไม่มีคำ: {missing}"))
        else:
            passes += 1

    print(f"== grep-gate qa-master · แถวทั้งหมด {len(rows)} · ผ่าน {passes} · ตก {len(fails)} ==")
    for num, rule, why in fails:
        print(f"  ✗ #{num} {rule}… → {why}")
    print("  ผล: " + ("ผ่านทุกแถว" if not fails else f"ตก {len(fails)} แถว"))
    sys.exit(0 if not fails else 2)


if __name__ == "__main__":
    main()
