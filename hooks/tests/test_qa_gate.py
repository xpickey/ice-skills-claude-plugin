#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ทดสอบ ice-qa-round-gate.py — รอบ 1–3 ผ่าน · รอบ 4 ปฏิเสธ · ICE_QA_EXTEND=1 ผ่านหนึ่งรอบ · ไฟล์คนละชิ้นนับแยก · agent อื่นไม่ถูกแตะ"""
import json
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
HOOKS = os.path.dirname(HERE)
sys.path.insert(0, HOOKS)
import ice_route_lib as lib  # noqa: E402
GATE = os.path.join(HOOKS, "ice-qa-round-gate.py")


def call(sid, agent, prompt):
    p = subprocess.run([sys.executable, GATE], input=json.dumps({"session_id": sid, "tool_name": "Agent", "tool_input": {"subagent_type": agent, "prompt": prompt}}), capture_output=True, text=True)
    return '"deny"' in p.stdout


def main():
    sid = "qatest-" + next(tempfile._get_candidate_names())
    bad = 0
    deck = "ตรวจ /x/Deck_V01R03_2026.09.05.pptx ตาม spec"
    for i in range(1, 4):
        d = call(sid, "qa-master-agent", deck.replace("R03", f"R0{i}"))
        ok = not d; bad += 0 if ok else 1; print(("  ✓ " if ok else "  ✗ ") + f"รอบ {i} ผ่าน")
    d = call(sid, "qa-master-agent", deck.replace("R03", "R04")); ok = d; bad += 0 if ok else 1; print(("  ✓ " if ok else "  ✗ ") + "รอบ 4 ถูกปฏิเสธ")
    d = call(sid, "qa-master-agent", "ICE_QA_EXTEND=1 " + deck.replace("R03", "R04")); ok = not d; bad += 0 if ok else 1; print(("  ✓ " if ok else "  ✗ ") + "user อนุมัติขยาย (ICE_QA_EXTEND=1) ผ่านหนึ่งรอบ")
    d = call(sid, "qa-master-agent", deck.replace("R03", "R05")); ok = d; bad += 0 if ok else 1; print(("  ✓ " if ok else "  ✗ ") + "รอบถัดไปโดยไม่มีอนุมัติ ถูกปฏิเสธอีก")
    d = call(sid, "qa-master-agent", "ตรวจ /x/Workbook_V01R01.xlsx"); ok = not d; bad += 0 if ok else 1; print(("  ✓ " if ok else "  ✗ ") + "ไฟล์คนละชิ้น นับแยก")
    d = call(sid, "solution-knowledge-agent", deck); ok = not d; bad += 0 if ok else 1; print(("  ✓ " if ok else "  ✗ ") + "agent อื่นไม่ถูกแตะ")
    try:
        os.remove(lib.state_path(sid))
    except OSError:
        pass
    print("\nผล: " + ("ผ่านทั้งหมด" if bad == 0 else f"ไม่ผ่าน {bad} ข้อ"))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
