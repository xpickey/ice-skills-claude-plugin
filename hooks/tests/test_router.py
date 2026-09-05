#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ชุดทดสอบตารางเส้นทาง skill + hook (V01R01 · 2026.09.05)
รัน: python3 hooks/tests/test_router.py   — ต้องผ่านทุกข้อก่อน commit ตารางหรือ hook
ประโยคทดสอบเป็นคำสั่งจริงของ user จาก log สิงหาคม–กันยายน 2026 (ย่อ)"""
import json
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
HOOKS = os.path.dirname(HERE)
sys.path.insert(0, HOOKS)
import ice_route_lib as lib  # noqa: E402

PROJ = "/Users/xpickey/Documents/Claude/Projects/OCC/26-OCC ERP Project"
ACA = "/Users/xpickey/Documents/Claude/Academic/บทความวิชาการที่ 9"

# (ข้อความ, โฟลเดอร์, เส้นทางที่ต้องพบ, เส้นทางที่ต้องไม่พบ)
CASES = [
    ("กัปตันและทีมเอาเข้า iCE super template แล้วสร้างให้มี icon ที่สวยงามแต่ละหน้า มี infographic", PROJ, ["deck-customer"], ["academic-article"]),
    ("ปรับ PPTX นำเสนอในมุมเสนอลูกค้า ไม่ใช้มุมภายใน ให้เห็น benefit", PROJ, ["deck-customer"], []),
    ("ต้องการ one page DISCLAIMER, KEY ASSUMPTIONS แบบไม่ลิเก", PROJ, ["deck-customer", "thai-translation"], []),
    ("ทำเป็น excel Save ที่ 21 - Present", PROJ, ["doc-customer"], ["academic-article"]),
    ("ตอบ TOR ของ บสย. ทำ clarification list", PROJ, ["doc-customer"], []),
    ("จากข้อมูลทั้งหมด ตั้งคำถามสอบถามเพิ่มเพื่อ Qualify เลือก Software", PROJ, ["sales-thinking"], []),
    ("แปลเป็นไทยไม่เข้าเลย ลองแปลแบบคนทำงานด้าน Lab", PROJ, ["thai-translation"], []),
    ("ท่านสมนึกและอริส เช็คการเขียนภาษาไทยในบทความวิชาการ อ้างอิง APA", ACA, ["academic-article"], ["deck-customer"]),
    ("รีวิวบทนำ สะกดผิด", ACA, ["academic-article"], []),          # จับจาก path อย่างเดียว
    ("PPTX mapping SAP to Oracle for King Power ด้วย NetSuite", PROJ, ["deck-customer", "product-netsuite"], []),
    ("อ่าน File นี้ แล้วสรุปการประชุม MOM 27 aug", PROJ, ["doc-customer", "doc-reading"], []),
    ("ทำ demo app dashboard ให้ลูกค้ากดได้", PROJ, ["demo-app"], []),
    ("GFMIS กับ e-GP ต่างกันอย่างไร", PROJ, ["govt-thailand"], []),
    ("สวัสดีครับ วันนี้อากาศดี", "/Users/xpickey/Documents/Claude", [], ["deck-customer", "doc-customer"]),
    ("ทำ Pass 2.3 ตามแผน", "/Users/xpickey/Documents/Claude/Custom Skill/iCE-Skills-Marketplace", ["fleet-maintenance"], ["deck-customer"]),
]


def test_matching():
    routes = lib.load_table()
    ids = {r["id"] for r in routes}
    assert len(ids) == len(routes), "id ซ้ำในตาราง"
    bad = 0
    for prompt, cwd, must, must_not in CASES:
        got = {r["id"] for r in lib.match_routes(prompt, cwd, routes)}
        miss = [m for m in must if m not in got]
        extra = [m for m in must_not if m in got]
        ok = not miss and not extra
        bad += 0 if ok else 1
        print(("  ✓ " if ok else "  ✗ ") + prompt[:48].ljust(50) + " → " + ", ".join(sorted(got)) + ("" if ok else f"   ขาด {miss} เกิน {extra}"))
    return bad


def test_paths_exist():
    routes = lib.load_table()
    bad = 0
    for r in routes:
        for p in (r.get("read_first") or []) + ([r["card"]] if r.get("card") else []):
            if not os.path.exists(lib.expand(p)):
                print("  ✗ ไฟล์ที่ตารางอ้างไม่มีจริง:", r["id"], p); bad += 1
        for s in (r.get("required") or []) + (r.get("recommended") or []):
            if not os.path.exists(lib.expand(f"~/.claude/skills/{s}/SKILL.md")):
                print("  ✗ skill ที่ตารางอ้างไม่มีจริง:", r["id"], s); bad += 1
    return bad


def run_hook(name, payload):
    p = subprocess.run([sys.executable, os.path.join(HOOKS, name)], input=json.dumps(payload), capture_output=True, text=True)
    return p.returncode, p.stdout, p.stderr


def test_hooks_end_to_end():
    sid = "test-" + next(tempfile._get_candidate_names())
    bad = 0
    # 1) router เพิ่มข้อความเข้าบริบทและจดประเภทงาน
    rc, out, err = run_hook("ice-skill-router.py", {"session_id": sid, "cwd": PROJ, "prompt": "ทำ deck นำเสนอ OCC ให้มี infographic"})
    ok = rc == 0 and "deck-customer" in out and "ice-doc-builder" in out and "กฎการออกแบบสไลด์ที่ใช้ทุกครั้ง" in out
    print(("  ✓ " if ok else "  ✗ ") + "router เพิ่มประเภทงาน + กฎสไลด์เข้าบริบท" + ("" if ok else f" rc={rc} err={err[:200]} out={out[:200]}")); bad += 0 if ok else 1
    # 2) spec gate ปฏิเสธเมื่อยังไม่โหลด
    rc, out, err = run_hook("ice-spec-gate.py", {"session_id": sid, "tool_name": "Write", "tool_input": {"file_path": PROJ + "/20-Propose/_build/content-spec.md"}})
    ok = '"deny"' in out
    print(("  ✓ " if ok else "  ✗ ") + "spec gate ปฏิเสธก่อนโหลด" + ("" if ok else f" out={out[:200]}")); bad += 0 if ok else 1
    # 3) จดการโหลด skill และเปิดไฟล์
    for name in ("ice-doc-builder", "ice-b2b-sales:b2b-slide-designer", "ice-writing-register"):
        run_hook("ice-skill-record.py", {"session_id": sid, "tool_name": "Skill", "tool_input": {"skill": name}})
    st = lib.load_state(sid)
    for p in st["read_first"]:
        run_hook("ice-skill-record.py", {"session_id": sid, "tool_name": "Read", "tool_input": {"file_path": lib.expand(p)}})
    # 4) spec gate ผ่านหลังโหลดครบ
    rc, out, err = run_hook("ice-spec-gate.py", {"session_id": sid, "tool_name": "Write", "tool_input": {"file_path": PROJ + "/20-Propose/_build/content-spec.md"}})
    ok = '"deny"' not in out
    print(("  ✓ " if ok else "  ✗ ") + "spec gate ผ่านหลังโหลดครบ" + ("" if ok else f" out={out[:300]}")); bad += 0 if ok else 1
    # 5) check จาก shell
    p = subprocess.run([sys.executable, os.path.join(HOOKS, "ice_route_lib.py"), "check", sid], capture_output=True, text=True)
    ok = p.returncode == 0
    print(("  ✓ " if ok else "  ✗ ") + "check สำหรับ prebuild guard = ครบ" + ("" if ok else f" rc={p.returncode} {p.stdout}")); bad += 0 if ok else 1
    # 6) ไฟล์ที่ไม่ใช่ spec ผ่านเสมอ · session ที่ไม่มีเส้นทางผ่านเสมอ
    rc, out, err = run_hook("ice-spec-gate.py", {"session_id": sid, "tool_name": "Write", "tool_input": {"file_path": PROJ + "/notes.md"}})
    rc2, out2, _ = run_hook("ice-spec-gate.py", {"session_id": "no-route-" + sid, "tool_name": "Write", "tool_input": {"file_path": PROJ + "/_build/content-spec.md"}})
    ok = '"deny"' not in out and '"deny"' not in out2
    print(("  ✓ " if ok else "  ✗ ") + "ไฟล์อื่น/ session ไม่มีเส้นทาง ผ่านเสมอ"); bad += 0 if ok else 1
    # 7) ข้อความไม่ตรงเส้นทางแต่เป็นงาน → บันทึก no-route
    rc, out, err = run_hook("ice-skill-router.py", {"session_id": sid, "cwd": PROJ, "prompt": "ช่วยสร้างตารางเปรียบเทียบผู้ให้บริการคลาวด์สามรายให้หน่อยครับ พร้อมข้อดีข้อเสีย"})
    ok = "ไม่ตรงกับประเภทงาน" in out
    print(("  ✓ " if ok else "  ✗ ") + "no-route → ขอให้ประกาศ + บันทึก"); bad += 0 if ok else 1
    try:
        os.remove(lib.state_path(sid))
    except OSError:
        pass
    return bad


if __name__ == "__main__":
    total = 0
    print("== จับคู่ข้อความกับตาราง =="); total += test_matching()
    print("== ไฟล์และ skill ที่ตารางอ้างถึงมีจริง =="); total += test_paths_exist()
    print("== hook ทำงานครบวงจร =="); total += test_hooks_end_to_end()
    print("\nผล: " + ("ผ่านทั้งหมด" if total == 0 else f"ไม่ผ่าน {total} ข้อ"))
    sys.exit(1 if total else 0)
