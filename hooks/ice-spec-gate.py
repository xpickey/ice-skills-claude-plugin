#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ขั้นตรวจสอบก่อนเขียนไฟล์กำหนดเนื้อหา — hook PreToolUse สำหรับ Write และ Edit (V01R01 · 2026.09.05)

"การคิด" ของทีมมีผลลัพธ์เป็นไฟล์ spec เสมอ (content-spec · design-spec · demo-spec · plan card)
ด่านนี้ปฏิเสธการเขียนไฟล์ spec ถ้า session ยังไม่ได้โหลด skill ที่ตารางเส้นทางกำหนดเป็น required
หรือยังไม่ได้เปิดไฟล์ read_first — คือบังคับลำดับ "โหลดก่อน คิดทีหลัง" ที่ตัวไฟล์ ไม่ใช่ที่ความจำ
ไฟล์อื่นทั้งหมดผ่านเสมอ · session ที่ไม่มีเส้นทางบังคับผ่านเสมอ
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.realpath(__file__))))
import ice_route_lib as lib  # noqa: E402

SPEC_PATTERN = re.compile(r"(_build/[^/]*spec[^/]*\.md$|content-spec|design-spec|demo-spec|plan-card|CONTENT-SPEC|DESIGN-SPEC|DEMO-SPEC)", re.I)


def deny(reason):
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": "deny", "permissionDecisionReason": reason}}, ensure_ascii=False))
    return 0


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return 0
    inp = payload.get("tool_input") or {}
    path = inp.get("file_path") or ""
    if not path or not SPEC_PATTERN.search(path):
        return 0
    if "/.claude/" in path or "iCE-Skills-Marketplace" in path:
        return 0  # ไฟล์ระบบของทีมเอง ไม่ใช่ spec ของงานลูกค้า
    session_id = payload.get("session_id") or "unknown"
    st = lib.load_state(session_id)
    if not st.get("required") and not st.get("read_first"):
        return 0
    ms, mr = lib.missing_required(st)
    if not ms and not mr:
        return 0
    parts = []
    if ms:
        parts.append("โหลด skill เหล่านี้ด้วย Skill tool ก่อน: " + ", ".join(ms))
    if mr:
        parts.append("เปิดอ่านไฟล์เหล่านี้ก่อน: " + ", ".join(mr))
    return deny("ยังเขียนไฟล์กำหนดเนื้อหาไม่ได้ เพราะยังโหลด skill ที่ประเภทงานนี้ต้องใช้ไม่ครบ — " + " · ".join(parts) + " — เหตุผล: งานสิงหาคม–กันยายน 2026 ที่คิดก่อนโหลด skill ต้องกลับมาแก้ภาษา สี และเลย์เอาต์ซ้ำหลายสิบรอบ")


if __name__ == "__main__":
    sys.exit(main())
