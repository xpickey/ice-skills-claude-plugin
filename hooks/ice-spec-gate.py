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
# V01R02 (2026.09.06 · คำถามของ user "ทำอย่างไรไม่ให้คิดหรือออกแบบก่อนโหลด"): ด่านเดิมดักเฉพาะไฟล์กำหนดเนื้อหา
# แต่ผลลัพธ์ชิ้นแรกของการคิดอาจเป็นไฟล์อื่นในโฟลเดอร์ผลงาน (ร่าง โครงเรื่อง บันทึกแนวทาง) ซึ่งเขียนได้โดยยังไม่โหลดสกิล
# จึงขยายให้ดักทุกไฟล์ที่เขียนลงโฟลเดอร์ผลงานของงานลูกค้า — เครื่องกันการคิดในหัวไม่ได้ แต่กันผลลัพธ์แรกของการคิดได้
WORK_OUTPUT = re.compile(r"/(20 - Output|20-Output|40 - Present Proposal|_build|90-Brain)/", re.I)


NUM_ON_SLIDE = re.compile(r"\d+(?:[.,]\d+)?\s*(?:%|เปอร์เซ็นต์|เท่า|วัน|เดือน|ปี|ชั่วโมง|ล้าน|พัน|บาท|คน|ราย|ครั้ง|ข้อ)")
FAKE_EVIDENCE = re.compile(r"^\s*\[?\s*(?:ตัวอย่าง|สมมติ|NEED FROM USER|รอ|ไม่มี|placeholder|TBD)", re.I)


def _numbers_without_evidence(text):
    """คืนรายการ 'หน้า N: ตัวเลข' ที่ action_title/key_message มีตัวเลขแต่ evidence ไม่ใช่แหล่งจริง"""
    out = []
    blocks = re.split(r"^##\s+", text, flags=re.M)
    for b in blocks[1:]:
        head = b.split("\n", 1)[0].strip()
        f = {}
        for line in b.split("\n")[1:]:
            m = re.match(r"^\s*(action_title|key_message|evidence)\s*:\s*(.*)$", line)
            if m:
                f[m.group(1)] = m.group(2).strip()
        shown = " ".join(x for x in (f.get("action_title", ""), f.get("key_message", "")) if x)
        nums = NUM_ON_SLIDE.findall(shown)
        ev = f.get("evidence", "")
        if nums and (not ev or FAKE_EVIDENCE.match(ev)):
            out.append(f"{head}: {', '.join(nums[:3])} (evidence: {ev[:40] or 'ว่าง'})")
    return out


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
    is_spec = bool(path and SPEC_PATTERN.search(path))
    is_work_output = bool(path and WORK_OUTPUT.search(path) and path.endswith((".md", ".txt", ".json", ".yaml", ".yml", ".html")))
    if not (is_spec or is_work_output):
        return 0
    if "/.claude/" in path or "iCE-Skills-Marketplace" in path:
        return 0  # ไฟล์ระบบของทีมเอง ไม่ใช่ spec ของงานลูกค้า
    # ด่านเนื้อหา (2026.09.06 ซ้อมจริง — user ทัก "80% มีอะไรอ้างอิงหรือ"): ตัวเลขบน action_title/key_message ต้องมี evidence ที่เป็นแหล่งจริง
    # ถ้ายังไม่มีตัวเลขจริง ห้ามใส่ตัวเลขบนหน้า ให้เขียนช่องว่างรอค่า — ตรวจเฉพาะ content-spec ที่เขียนทั้งไฟล์ (Write) หรือส่วนที่แก้ (Edit)
    if "content-spec" in path.lower():
        body = inp.get("content") or inp.get("new_string") or ""
        bad = _numbers_without_evidence(body)
        if bad:
            return deny("ไฟล์กำหนดเนื้อหามีตัวเลขบนหน้าที่ไม่มีแหล่งอ้างอิงจริง: " + " · ".join(bad[:4]) +
                        " — ตัวเลขทุกตัวที่จะปรากฏบนสไลด์ต้องมี evidence เป็นแหล่งจริง (ไฟล์ลูกค้า ประชุม TOR เอกสารผลิตภัณฑ์) ถ้ายังไม่มี ให้ตัดตัวเลขออกจาก action_title/key_message แล้วเขียนว่ารอค่าจากลูกค้าแทน "
                        "เหตุผล: user ทักตัวเลข 80% ที่กุขึ้นเป็นตัวอย่างในการซ้อม 2026.09.06 ว่าอวดอ้างเกินจริง")
    session_id = payload.get("session_id") or "unknown"
    st = lib.load_state(session_id)
    if not st.get("required") and not st.get("read_first"):
        return 0
    ms, mr = lib.missing_required(st)
    if not ms and not mr:
        return 0
    parts = []
    if ms:
        parts.append("โหลด skill เหล่านี้ก่อน (เรียกด้วย Skill tool หรือเปิดอ่าน ~/.claude/skills/<ชื่อ>/SKILL.md ทั้งไฟล์ ระบบนับให้ทั้งสองทาง): " + ", ".join(ms))
    if mr:
        parts.append("เปิดอ่านไฟล์เหล่านี้ก่อน: " + ", ".join(mr))
    what = "ไฟล์กำหนดเนื้อหา" if is_spec else "ไฟล์ผลงานในโฟลเดอร์ของงานนี้"
    return deny(f"ยังเขียน{what}ไม่ได้ เพราะยังโหลด skill ที่ประเภทงานนี้ต้องใช้ไม่ครบ — " + " · ".join(parts) + " — เหตุผล: งานสิงหาคม–กันยายน 2026 ที่คิดก่อนโหลด skill ต้องกลับมาแก้ภาษา สี และเลย์เอาต์ซ้ำหลายสิบรอบ")


if __name__ == "__main__":
    sys.exit(main())
