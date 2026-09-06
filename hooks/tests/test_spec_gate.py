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
    # ขอบเขตของด่าน (V01R02 · 2026.09.06): ทุกไฟล์ผลลัพธ์ในโฟลเดอร์งาน ไม่ใช่เฉพาะไฟล์กำหนดเนื้อหา
    import sys as _s
    _s.path.insert(0, os.path.dirname(HERE))
    import ice_route_lib as lib
    sid = "specscope"
    st = lib.merge_routes_into_state(lib.load_state(sid), [r for r in lib.load_table() if r["id"] == "deck-customer"])
    lib.save_state(sid, st)

    def scope(name, path, expect):
        p = subprocess.run([sys.executable, GATE], input=json.dumps({"session_id": sid, "tool_name": "Write", "tool_input": {"file_path": path, "content": "x"}}), capture_output=True, text=True)
        got = "deny" in p.stdout
        ok = got == expect
        print(("  ✓ " if ok else "  ✗ ") + name + ("" if ok else f"  (deny={got} expected={expect})"))
        return 0 if ok else 1

    bad += scope("ร่างในโฟลเดอร์ผลงาน โหลดไม่ครบ → ปฏิเสธ", "/Users/x/Documents/Claude/Projects/A/11-A/20 - Output/outline.md", True)
    bad += scope("บันทึกในเขตคลังสมองของงาน โหลดไม่ครบ → ปฏิเสธ", "/Users/x/Documents/Claude/Projects/A/11-A/90-Brain/approach.md", True)
    bad += scope("ไฟล์นอกโฟลเดอร์ผลงาน → ผ่าน", "/tmp/scratch/notes.md", False)
    bad += scope("ไฟล์ระบบของทีม → ผ่าน", "/Users/x/.claude/hooks/a.md", False)

    # ด่านจากเนื้อหา (2026.09.06): เรื่องที่เพิ่งรู้ตอนอ่านเอกสารต้นทาง ต้องโหลดกติกาก่อนเขียน
    sid2 = "contentroute"
    st2 = lib.merge_routes_into_state(lib.load_state(sid2), [r for r in lib.load_table() if r["id"] == "deck-customer"])
    for s in ("ice-doc-builder", "b2b-slide-designer", "ice-writing-register"):
        lib.record_skill(st2, s)
    for rp in st2["read_first"]:
        lib.record_read(st2, lib.expand(rp))
    lib.save_state(sid2, st2)

    def content(name, body, expect):
        p = subprocess.run([sys.executable, GATE], input=json.dumps({"session_id": sid2, "tool_name": "Write", "tool_input": {"file_path": PATH, "content": body}}), capture_output=True, text=True)
        got = "deny" in p.stdout
        ok = got == expect
        print(("  ✓ " if ok else "  ✗ ") + name + ("" if ok else f"  (deny={got} expected={expect})"))
        return 0 if ok else 1

    bad += content("เนื้อหาอยู่ในเรื่องที่โหลดครบแล้ว → ผ่าน", PAGE.format(n=1, t="ปก", a="ปิดงบเร็วขึ้น", k="x", e=""), False)
    bad += content("เนื้อหาเผยว่าเป็นงานราชการ e-GP → ปฏิเสธให้โหลดก่อน", PAGE.format(n=1, t="ตอบข้อกำหนด", a="ตอบ TOR ของการประปาส่วนภูมิภาค ระบบ e-GP", k="x", e=""), True)
    bad += content("เนื้อหาเผยว่าใช้ NetSuite → ปฏิเสธให้โหลดก่อน", PAGE.format(n=1, t="ทางออก", a="ใช้ NetSuite SuiteScript ทำ workflow", k="x", e=""), True)
    try:
        os.remove(lib.state_path(sid2))
    except OSError:
        pass
    try:
        os.remove(lib.state_path(sid))
    except OSError:
        pass
    print("\nผล: " + ("ผ่านทั้งหมด" if bad == 0 else f"ไม่ผ่าน {bad} ข้อ"))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
