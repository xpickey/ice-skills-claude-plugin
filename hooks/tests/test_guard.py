#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ชุดทดสอบ ice-prebuild-guard.sh (V03R02) — รัน: python3 hooks/tests/test_guard.py
ครอบ: อ่านอย่างเดียวผ่าน · build โดยไม่มี marker ถูกปฏิเสธ · ด่าน D ปฏิเสธเมื่อ session ยังไม่โหลด skill
· ผ่านเมื่อโหลดครบ · session ที่ไม่มีเส้นทางไม่ถูกด่าน D แตะ · งานแก้ไฟล์ระบบผ่าน"""
import json
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
HOOKS = os.path.dirname(HERE)
sys.path.insert(0, HOOKS)
import ice_route_lib as lib  # noqa: E402

GUARD = os.path.join(HOOKS, "ice-prebuild-guard.sh")
TMP = tempfile.mkdtemp(prefix="guardtest-")
DOCX_NEW = os.path.join(TMP, "Deck_V01R01_2026.09.05.docx")


def run(cmd, sid="none"):
    p = subprocess.run(["bash", GUARD], input=json.dumps({"session_id": sid, "tool_input": {"command": cmd}}), capture_output=True, text=True)
    return "deny" in p.stdout, p.stdout


def case(name, cmd, sid, expect_deny, must_contain=None):
    denied, out = run(cmd, sid)
    ok = denied == expect_deny and (must_contain is None or not denied or must_contain in out)
    print(("  ✓ " if ok else "  ✗ ") + name + ("" if ok else f"  (deny={denied} expected={expect_deny}) {out[:160]}"))
    return 0 if ok else 1


def main():
    bad = 0
    sid = "guardtest-" + os.path.basename(TMP)
    # session ที่มีเส้นทาง deck แต่ยังไม่โหลดอะไร
    st = lib.load_state(sid)
    st = lib.merge_routes_into_state(st, [r for r in lib.load_table() if r["id"] == "doc-customer"])
    lib.save_state(sid, st)
    build_ok_markers = f"ICE_BUILD=pipeline ICE_BASE=NEW python3 build_deck.py --out '{DOCX_NEW}'"

    bad += case("อ่านอย่างเดียวผ่าน", "python3 -c 'from docx import Document; print(Document(\"a.docx\").paragraphs)'", sid, False)
    bad += case("บันทึกภาพ .png จากไฟล์ชื่อ .pptx → ผ่าน (ไม่ใช่การเขียนเอกสาร)", "python3 - <<'PY'\nsheet.save('_review/contact-sheet.png')  # จาก Deck_V01R05.pptx\nPY", "none", False)
    bad += case("python-pptx เขียนไฟล์เอกสารจริงโดยไม่มี marker → ปฏิเสธ", "python3 -c \"from pptx import Presentation; p=Presentation(); p.save('/tmp/a.pptx')\"", "none", True)
    bad += case("build ไม่มี marker → ปฏิเสธ (ตรรกะเดิม)", "python3 build_deck.py", "none", True)
    bad += case("build ผ่านสคริปต์ใน _lib โดยไม่มี marker → ปฏิเสธ (บทเรียน Pass 6)", "cd /tmp/x && python3 ~/.claude/agents/_lib/build_pptx.py _build/spec.json Deck_V01R01.pptx", "none", True)
    bad += case("แก้ไฟล์ระบบใน _lib ด้วย sed → ผ่าน", "sed -i '' 's/a/b/' ~/.claude/agents/_lib/build_pptx.py", "none", False)
    bad += case("heredoc แก้ hook → ผ่าน", "python3 - <<'EOF'\nopen('/Users/x/.claude/hooks/a.py','w').write('x')\nEOF", "none", False)
    bad += case("สร้างแม่แบบลงคลัง assets ด้วย heredoc → ผ่าน (ยกเว้นเฉพาะปลายทางในคลัง)", "python3 - <<'EOF'\nprs.save('/Users/x/.claude/skills/b2b-slide-designer/assets/masters/M.pptx')\nEOF", "none", False)
    bad += case("ด่าน D: session ยังไม่โหลด skill → ปฏิเสธ", build_ok_markers, sid, True, "ยังโหลด skill")
    for name in ("ice-doc-builder", "ice-writing-register"):
        lib.record_skill(st, name)
    for p in st["read_first"]:
        lib.record_read(st, lib.expand(p))
    lib.save_state(sid, st)
    bad += case("ด่าน D: โหลดครบ → ผ่าน", build_ok_markers, sid, False)
    bad += case("session ไม่มีเส้นทาง → ด่าน D ไม่แตะ", build_ok_markers, "no-route-session", False)
    bad += case("คำสั่งที่เพียงเอ่ยคำว่า pptx และ .save( แต่ไม่ได้เขียนเอกสารจริง → ผ่าน (V03R05)", "python3 ~/.claude/agents/_lib/patch.py pptx .save(", sid, False)
    bad += case("สคริปต์ build ใน _lib ที่เขียนเอกสารจริงโดยไม่มี marker → ปฏิเสธ (V03R03)", "python3 ~/.claude/agents/_lib/build_pptx.py spec.json out.pptx", sid, True)
    # V03R06 — การดูแลตัวสคริปต์สร้างเอกสารเอง ต้องไม่ถูกปิดกั้น (ชื่อสคริปต์ปรากฏในคำสั่ง แต่ไม่ได้สั่งให้ทำงาน)
    bad += case("ตรวจไวยากรณ์สคริปต์สร้างสไลด์ → ผ่าน (V03R06)", "python3 -m py_compile plugins/ice-b2b-sales/_lib/build_pptx.py", sid, False)
    bad += case("แก้สคริปต์สร้างสไลด์แล้วตรวจไวยากรณ์ → ผ่าน (V03R06)", "cd /r && perl -0pi -e 's/a/b/g' plugins/ice-b2b-sales/_lib/build_pptx.py && python3 -m py_compile plugins/ice-b2b-sales/_lib/build_pptx.py", sid, False)
    bad += case("ค้นบรรทัดในสคริปต์สร้างสไลด์ → ผ่าน (V03R06)", "grep -n '_tpl_slide' plugins/ice-b2b-sales/_lib/build_pptx.py", sid, False)
    try:
        os.remove(lib.state_path(sid))
    except OSError:
        pass
    print("\nผล: " + ("ผ่านทั้งหมด" if bad == 0 else f"ไม่ผ่าน {bad} ข้อ"))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
