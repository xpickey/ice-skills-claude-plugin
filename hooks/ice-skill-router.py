#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ด่านก่อนคิด — hook UserPromptSubmit (V01R01 · 2026.09.05)

ทำงานทุกครั้งที่ user พิมพ์ข้อความ: อ่านตาราง skill-routing.yaml จับคู่ข้อความและโฟลเดอร์ที่ทำงานอยู่
แล้วฉีดข้อความเข้า context ว่า "งานนี้ต้องโหลด skill อะไรก่อนเริ่มคิด" พร้อมการ์ดกฎที่ user ย้ำบ่อย
บันทึกเส้นทางที่จับได้ลงสภาพ session เพื่อให้ด่าน Write spec และด่าน build ตรวจย้อนได้

เหตุผลที่ต้องเป็น hook: log สิงหาคม–กันยายน 2026 พบว่า 56 session ที่สร้างเอกสาร โหลด skill ออกแบบ
ก่อนลงมือเพียง 4 session — กติกาที่ให้ model "นึกเอง" ไม่ทำงาน จึงให้เครื่องเป็นคนบอกทุกครั้ง
ผลลัพธ์: stdout ธรรมดา = ข้อความที่ Claude เห็นเป็นบริบทเพิ่ม (ตามเอกสาร UserPromptSubmit)
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.realpath(__file__))))
import ice_route_lib as lib  # noqa: E402

NO_ROUTE_LOG = os.path.join(lib.STATE_DIR, "no-route.log")
WORK_WORDS = ("ทำ", "สร้าง", "เขียน", "ปรับ", "แก้", "build", "create", "write", "draft", "ร่าง", ".pptx", ".docx", ".xlsx")


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return 0
    prompt = payload.get("prompt") or payload.get("user_prompt") or ""
    if not prompt or prompt.startswith("/") or prompt.startswith("<"):
        return 0  # คำสั่ง slash และข้อความระบบ ไม่ต้องจับเส้นทาง
    cwd = payload.get("cwd") or os.getcwd()
    session_id = payload.get("session_id") or "unknown"

    routes = lib.load_table()
    hits = lib.match_routes(prompt, cwd, routes)
    if not hits:
        if any(w in prompt for w in WORK_WORDS) and len(prompt) > 40:
            os.makedirs(lib.STATE_DIR, exist_ok=True)
            with open(NO_ROUTE_LOG, "a", encoding="utf-8") as fh:
                fh.write(json.dumps({"session": session_id, "cwd": cwd, "prompt": prompt[:200]}, ensure_ascii=False) + "\n")
            print("ด่านก่อนคิด: ข้อความนี้ไม่ตรงกับเส้นทาง skill ใดในตาราง — ก่อนลงมือ ให้ประกาศในคำตอบแรกว่าจะใช้ skill ตระกูลใดและเพราะอะไร (ระบบบันทึกกรณีนี้ไว้เพื่อเพิ่มแถวในตารางภายหลัง)")
        return 0

    st = lib.load_state(session_id)
    st = lib.merge_routes_into_state(st, hits)
    lib.save_state(session_id, st)

    ms, mr = lib.missing_required(st)
    lines = ["ด่านก่อนคิด (ตารางเส้นทาง skill ของทีม) — งานนี้เข้าเส้นทาง: " + " · ".join(f"{r['id']} ({r.get('label','')})" for r in hits)]
    if st["required"]:
        status = "ยังไม่ได้โหลด: " + ", ".join(ms) if ms else "โหลดครบแล้ว"
        lines.append("ต้องโหลดก่อนเขียน spec หรือ build (ด่านจะปฏิเสธถ้ายังไม่โหลด): " + ", ".join(st["required"]) + " — " + status)
    if st["recommended"]:
        lines.append("ควรโหลดเพิ่มถ้าเนื้อหาเกี่ยวข้อง: " + ", ".join(st["recommended"]))
    if st["read_first"]:
        pending = [os.path.basename(p) for p in mr]
        lines.append("ไฟล์ที่ต้องเปิดอ่านก่อนออกแบบ: " + ", ".join(os.path.basename(p) for p in st["read_first"]) + (" — ยังไม่ได้เปิด: " + ", ".join(pending) if pending else " — เปิดครบแล้ว"))
    for r in hits:
        if r.get("note"):
            lines.append("หมายเหตุ [" + r["id"] + "]: " + r["note"])
    lines.append("ลำดับที่ถูกต้อง: โหลด skill ที่ระบุ → เปิดไฟล์ที่ระบุ → จึงเขียน spec → จึง build (ห้ามคิดหรือสร้างก่อนโหลด)")
    cards = []
    for r in hits:
        c = r.get("card")
        if c and c not in cards:
            cards.append(c)
    for c in cards:
        p = lib.expand(c)
        if os.path.exists(p):
            with open(p, encoding="utf-8") as fh:
                lines.append("\n--- การ์ดกฎประจำ (" + os.path.basename(p) + ") ---\n" + fh.read().strip())
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    sys.exit(main())
