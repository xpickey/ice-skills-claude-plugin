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


# ที่อยู่ไฟล์เต็มในซองคำสั่ง — ARTIFACT ด้านบนจับเฉพาะชื่อไฟล์ (ไม่มีเครื่องหมายทับ) จึงต้องมีอีกตัวสำหรับหา path จริงบนดิสก์
ARTIFACT_PATH = re.compile(r"((?:/|~/)[^\s\"'`]+\.(?:pptx|docx|xlsx|pdf|md))")

PLACEHOLDER = re.compile(r"\[(?:รอ|NEED FROM USER|TBD|XXX|TODO)[^\]]*\]|รอตัวเลข|ตัวอย่างข้อความ|\bTBD\b|\bXXX\b|lorem ipsum", re.I)


def _placeholders_in(path):
    """คืนรายการข้อความรอเติมที่พบในไฟล์เอกสาร (pptx/docx/md) — ว่าง = ไม่พบ"""
    texts = []
    try:
        if path.endswith(".pptx"):
            from pptx import Presentation
            for s in Presentation(path).slides:
                for sh in s.shapes:
                    if getattr(sh, "has_text_frame", False):
                        texts.append(sh.text_frame.text)
        elif path.endswith(".docx"):
            from docx import Document
            d = Document(path)
            texts = [p.text for p in d.paragraphs] + [c.text for t in d.tables for r in t.rows for c in r.cells]
        else:
            texts = [open(path, encoding="utf-8", errors="ignore").read()]
    except Exception:
        return []
    return [m.group(0) for t in texts for m in PLACEHOLDER.finditer(t or "")]


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
    # คีย์ = ชื่อไฟล์ล้วน: ตัดคำที่อยู่หน้าชื่อไฟล์ (เช่น "ตรวจ X.pptx" → "X") และเลขรุ่น
    # บทเรียนซ้อมจริง 2026.09.06: คำหน้าชื่อไฟล์ติดมาในคีย์ ทำให้เปลี่ยนคำแล้วนับใหม่ = เลี่ยงเพดานได้
    key = "(ไม่ระบุไฟล์)"
    if names:
        base = os.path.basename(names[0]).strip()
        base = re.sub(r"^.*[\s]", "", base) if re.search(r"[\u0e00-\u0e7f]\s", base) else base
        key = re.sub(r"_?V\d\dR\d\d.*$", "", base)
    # ด่านก่อนส่งตรวจ (2026.09.06 ซ้อมจริง): งานที่ประกาศว่าเป็นฉบับสุดท้ายต้องไม่มีข้อความรอเติม และผลตรวจอัตโนมัติล่าสุดต้องไม่ FAIL
    # เหตุผล: อริสพบ "[รอตัวเลขจริงจากลูกค้า]" บนสไลด์ของงาน is_final และผู้สร้างส่งต่อทั้งที่ audit เตือน — ทั้งสองอย่างเครื่องกันได้ก่อนเสียรอบตรวจ
    if re.search(r"is_final\s*:\s*true", prompt, re.I):
        art = next((a for a in ARTIFACT_PATH.findall(prompt) if os.path.isfile(a)), None)
        if art:
            art = art.strip()
            holders = _placeholders_in(art)
            if holders:
                deny(f"งานนี้ประกาศว่าเป็นฉบับสุดท้าย (is_final: true) แต่ในไฟล์ยังมีข้อความรอเติม {len(holders)} จุด เช่น {holders[:3]} — "
                     "ให้เติมค่าจริง หรือตัดข้อความนั้นออก หรือเปลี่ยนเป็น is_final: false ก่อนส่งตรวจ เหตุผล: ผู้ตรวจจะรายงานเรื่องนี้เป็นข้อบกพร่องแน่นอน จึงเสียรอบตรวจเปล่า")
                return 0
            rec = os.path.join(os.path.dirname(art), "_build", ".last-built.json")
            if not os.path.exists(rec):
                rec = os.path.join(os.path.dirname(art), ".last-built.json")
            try:
                aud = json.load(open(rec)).get("_audits", {}).get(os.path.basename(art), {})
            except Exception:
                aud = {}
            bad = [k for k, v in aud.items() if v == "FAIL"]
            if bad:
                deny(f"ผลตรวจอัตโนมัติล่าสุดของไฟล์นี้ยังไม่ผ่าน ({', '.join(bad)}) — ให้แก้ให้ผ่านแล้วสร้างใหม่ก่อนส่งตรวจ "
                     "เหตุผล: ผู้ตรวจไม่ตรวจซ้ำสิ่งที่เครื่องตรวจแล้ว การส่งไฟล์ที่เครื่องบอกว่าไม่ผ่านคือการเสียรอบตรวจเปล่า")
                return 0
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
