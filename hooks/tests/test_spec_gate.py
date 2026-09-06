#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ชุดทดสอบ ice-spec-gate.py — ด่านเนื้อหา: ตัวเลขบน action_title/key_message ต้องมี evidence เป็นแหล่งจริง
รัน: python3 hooks/tests/test_spec_gate.py
ที่มา: ซ้อมจริง 2026.09.06 — user ทักตัวเลข 80% ที่กุขึ้นเป็นตัวอย่างว่าอวดอ้างเกินจริง"""
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
GATE = os.path.join(os.path.dirname(HERE), "ice-spec-gate.py")
PATH = "/tmp/guardtest/Projects/X/11-X/20 - Output/_build/demo-content-spec.md"


def run(content, sid="none"):
    p = subprocess.run([sys.executable, GATE], input=json.dumps({"session_id": sid, "tool_name": "Write", "tool_input": {"file_path": PATH, "content": content}}), capture_output=True, text=True)
    return "deny" in p.stdout, p.stdout


def case(name, content, expect_deny, must=None):
    denied, out = run(content)
    ok = denied == expect_deny and (must is None or not denied or must in out)
    print(("  ✓ " if ok else "  ✗ ") + name + ("" if ok else f"  (deny={denied} expected={expect_deny}) {out[:160]}"))
    return 0 if ok else 1


PAGE = "## หน้า {n} — {t}\nobjective: x\naction_title: {a}\nkey_message: {k}\nevidence: {e}\nvisual: icon\ntopic_id: t\ncolor_set: none\n"


def main():
    bad = 0
    bad += case("ตัวเลขบนหน้า แต่ evidence เป็นตัวอย่าง → ปฏิเสธ",
                PAGE.format(n=4, t="ผล", a="ลดงานกระทบยอดลง 80 เปอร์เซ็นต์", k="ตัวอย่าง", e="[ตัวอย่าง] ไม่มีตัวเลขจริง"), True, "80 เปอร์เซ็นต์")
    bad += case("ตัวเลขบนหน้า แต่ evidence รอจากลูกค้า → ปฏิเสธ (ห้ามใส่เลขก่อนมีค่าจริง)",
                PAGE.format(n=2, t="ปัญหา", a="ปิดงบล่าช้า 15 วัน", k="x", e="[NEED FROM USER: จำนวนวันจริง]"), True)
    bad += case("ตัวเลขบนหน้า และ evidence เป็นแหล่งจริง → ผ่าน",
                PAGE.format(n=2, t="ปัญหา", a="ปิดงบล่าช้า 15 วัน", k="x", e="รายงานปิดงบ Q2 ของลูกค้า (10 - Input/close-report.xlsx) หน้า 3"), False)
    bad += case("ไม่มีตัวเลขบนหน้า evidence ว่างได้ → ผ่าน",
                PAGE.format(n=6, t="ปิด", a="ขั้นถัดไปคือประชุมยืนยันขอบเขตกับทีมบัญชี", k="x", e=""), False)
    bad += case("ตัวเลขอยู่ใน evidence เอง ไม่ใช่บนหน้า → ผ่าน",
                PAGE.format(n=3, t="ทางออก", a="ใช้ระบบงาน ERP เดียวกันทั้งกลุ่ม", k="ลดงานกระทบยอดด้วยมือ (ตัวเลขรอจากลูกค้า)", e="[NEED FROM USER: ชั่วโมงกระทบยอดต่อเดือน]"), False)
    print("\nผล: " + ("ผ่านทั้งหมด" if bad == 0 else f"ไม่ผ่าน {bad} ข้อ"))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
