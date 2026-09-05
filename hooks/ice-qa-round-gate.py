#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""เพดานรอบตรวจคุณภาพที่เครื่องนับ — hook PreToolUse สำหรับเครื่องมือ Agent (V01R01 · 2026.09.05)

นับจำนวนครั้งที่ session นี้ส่งงานให้ผู้ตรวจคุณภาพ (qa-master-agent) ต่อไฟล์งานหนึ่งชิ้น
เมื่อจะส่งเป็นรอบที่ 4 ระบบปฏิเสธ และให้ user เป็นผู้ตัดสินว่าจะขยายรอบหรือไม่ — ห้าม agent ยกเว้นตัวเอง
เหตุผล: กติกาเพดาน 3 รอบมีอยู่ในไฟล์อริสมาตลอด แต่เป็นตัวหนังสือ ผลคือ 16 จาก 28 session ในสิงหาคม–กันยายน 2026
เกินเพดาน (สูงสุด 17 รอบ) และมี 9 รอบที่เกิดต่อกันโดย user ไม่ได้พิมพ์อะไรคั่นเลย
การขยายรอบ: user ต้องพิมพ์อนุมัติในแชท แล้ว agent ใส่ข้อความ "ICE_QA_EXTEND=1" ในคำสั่งส่งตรวจครั้งนั้น (ใช้ได้ครั้งละหนึ่งรอบ)
สภาพ session: ~/.claude/state/ice-session/<session_id>.json ช่อง qa_rounds {ชื่อไฟล์: จำนวนรอบ}
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.realpath(__file__))))
import ice_route_lib as lib  # noqa: E402

CAP = 3
ARTIFACT = re.compile(r"([\w\-. ()]+\.(?:pptx|docx|xlsx|pdf|md))", re.I)


def deny(reason):
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": "deny", "permissionDecisionReason": reason}}, ensure_ascii=False))


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return 0
    inp = payload.get("tool_input") or {}
    if "qa-master" not in str(inp.get("subagent_type", "")):
        return 0
    prompt = inp.get("prompt") or ""
    session_id = payload.get("session_id") or "unknown"
    names = ARTIFACT.findall(prompt)
    # ตัดเลขรุ่นออก เพื่อให้ทุกรุ่นของงานชิ้นเดียวกันนับเป็นชิ้นเดียว
    key = re.sub(r"_?V\d\dR\d\d.*$", "", os.path.basename(names[0])) if names else "(ไม่ระบุไฟล์)"
    st = lib.load_state(session_id)
    rounds = st.setdefault("qa_rounds", {})
    n = rounds.get(key, 0)
    if n >= CAP and "ICE_QA_EXTEND=1" not in prompt:
        deny(f"งาน {key} ถูกส่งตรวจคุณภาพครบ {CAP} รอบแล้วใน session นี้ — ครบเพดานที่ทีมตั้งไว้ ห้ามส่งรอบที่ {n + 1} เอง "
             f"ให้สรุปให้ user ฟังว่ารอบที่ผ่านมาแก้อะไรไปแล้ว เหลืออะไร และถามว่าจะขยายรอบตรวจหรือรับงานตามสภาพ "
             f"ถ้า user อนุมัติให้ขยาย ให้ใส่ข้อความ ICE_QA_EXTEND=1 ในคำสั่งส่งตรวจครั้งถัดไป (ใช้ได้ทีละหนึ่งรอบ) "
             f"เหตุผลของเพดาน: งานเดือนกันยายน 2026 ตรวจถึงรอบที่ 17 เพราะแก้ทีละจุดแล้วส่งตรวจซ้ำ")
        return 0
    rounds[key] = n + 1
    lib.save_state(session_id, st)
    return 0


if __name__ == "__main__":
    sys.exit(main())
