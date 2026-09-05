#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ด่านรับไฟล์ระบบที่เสนอมา (SKILL.proposed.md / agent .proposed.md) — check_proposed.py (V01R01 · 2026.09.05)
ตรวจเกณฑ์ที่วัดได้ด้วยเครื่องก่อนส่งให้ผู้อ่านที่ไม่มีบริบทมาก่อน (Cold-Reader Test):
  บรรทัด ≤ เพดานที่ให้ · เครื่องหมายเน้น (🔴 ⭐ ⚠ MUST NEVER ALWAYS) ≤ 5 · description ≤ 300 ตัวอักษร ขึ้นต้นด้วยกรณีใช้
  ไม่มีประวัติรุ่นในเนื้อ (บรรทัดที่ขึ้นต้นด้วย V##R## นอกหัวไฟล์) · pointer ทุกตัวชี้ไฟล์ที่มีจริง · ไม่มีคำแปลตรง/สำนวน AI (thai_style_check)
วิธีใช้: python3 hooks/tests/check_proposed.py <ไฟล์> --max-lines 350
"""
import argparse
import os
import re
import subprocess
import sys

EMPH = re.compile(r"🔴|⭐|⚠|\bMUST\b|\bNEVER\b|\bALWAYS\b")  # ห้าม/บังคับ เป็นกริยาปกติของกฎ ไม่นับเป็นการเน้น
STYLE = os.path.expanduser("~/.claude/agents/_lib/thai_style_check.py")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file")
    ap.add_argument("--max-lines", type=int, default=350)
    ap.add_argument("--max-emph", type=int, default=5)
    a = ap.parse_args()
    t = open(a.file, encoding="utf-8").read()
    lines = t.split("\n")
    bad = []
    n = len(lines)
    if n > a.max_lines:
        bad.append(f"บรรทัด {n} เกินเพดาน {a.max_lines}")
    fm_end = t.find("\n---", 4) if t.startswith("---") else 0
    body = t[fm_end + 4:] if fm_end else t
    emph = len(EMPH.findall(body))
    if emph > a.max_emph:
        bad.append(f"เครื่องหมายเน้น {emph} จุด เกิน {a.max_emph}")
    m = re.search(r"^description:\s*(.*?)(?=^\w+:|^---)", t, re.S | re.M)
    desc = m.group(1).strip() if m else ""
    if len(desc) > 300:
        bad.append(f"description {len(desc)} ตัวอักษร เกิน 300")
    if desc and not re.match(r"^[\"'|>]?\s*(ใช้เมื่อ|Use when|ใช้ทุกครั้ง)", desc):
        bad.append("description ไม่ได้ขึ้นต้นด้วยกรณีใช้ (ใช้เมื่อ… / Use when…)")
    hist = [i + 1 for i, l in enumerate(lines[8:], start=8) if re.match(r"^\s*[-*>]?\s*\**V\d\dR\d\d", l)]
    if hist:
        bad.append(f"มีบรรทัดประวัติรุ่นในเนื้อ {len(hist)} บรรทัด (เช่นบรรทัด {hist[:3]})")
    base = os.path.dirname(os.path.abspath(a.file))
    dangling = []
    for p in set(re.findall(r"`((?:~/\.claude|references|\.\./|/Users/)[^`\s]+)`", t)):
        q = p.rstrip(".,;:)")
        cands = [os.path.expanduser(q), os.path.join(base, q), os.path.join(base, "..", q)]
        if not any(os.path.exists(c) for c in cands) and "<" not in q:
            dangling.append(q)
    if dangling:
        bad.append("pointer ชี้ไฟล์ที่ไม่มีจริง: " + ", ".join(dangling[:6]))
    style = ""
    if os.path.exists(STYLE):
        p = subprocess.run([sys.executable, STYLE, a.file, "--register", "general"], capture_output=True, text=True)
        blocks = [l for l in p.stdout.split("\n") if "[ต้องแก้]" in l]
        if blocks:
            bad.append("ภาษาแปล/สำนวน AI ต้องแก้ " + str(len(blocks)) + " จุด: " + " | ".join(b.strip()[:70] for b in blocks[:3]))
        style = p.stdout.strip().split("\n")[-1] if p.stdout.strip() else ""
    print(f"== {os.path.basename(a.file)} · {n} บรรทัด · เน้น {emph} · description {len(desc)} ตัวอักษร ==")
    for b in bad:
        print("  ✗ " + b)
    if style:
        print("  " + style)
    print("  ผล: " + ("ผ่านด่านเครื่อง" if not bad else f"ไม่ผ่าน {len(bad)} ข้อ"))
    sys.exit(2 if bad else 0)


if __name__ == "__main__":
    main()
