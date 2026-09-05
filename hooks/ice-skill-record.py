#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""บันทึกรายชื่อ skill ที่ถูกโหลดจริง — hook PostToolUse สำหรับเครื่องมือ Skill และ Read (V01R01 · 2026.09.05)

ทุกครั้งที่ model เรียก Skill tool หรือ Read ไฟล์ จะจดชื่อ skill (หรือ path ไฟล์) ลงสภาพ session
ด่าน Write spec และด่าน build ใช้บันทึกนี้ตัดสินว่า "โหลดแล้วจริง" ไม่ใช่เชื่อคำพูดของ model
ไม่ปิดกั้นอะไร (PostToolUse ปิดกั้นไม่ได้อยู่แล้ว) — ทำงานเงียบ
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.realpath(__file__))))
import ice_route_lib as lib  # noqa: E402


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return 0
    tool = payload.get("tool_name") or ""
    inp = payload.get("tool_input") or {}
    session_id = payload.get("session_id") or "unknown"
    st = lib.load_state(session_id)
    changed = False
    if tool == "Skill":
        name = inp.get("skill") or inp.get("name") or ""
        if name:
            lib.record_skill(st, name)
            changed = True
    elif tool == "Read":
        path = inp.get("file_path") or ""
        if path:
            lib.record_read(st, path)
            changed = True
    if changed:
        lib.save_state(session_id, st)
    return 0


if __name__ == "__main__":
    sys.exit(main())
