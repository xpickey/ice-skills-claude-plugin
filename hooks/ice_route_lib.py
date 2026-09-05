#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ไลบรารีกลางของ hook เส้นทาง skill (V01R01 · 2026.09.05)

หน้าที่: อ่านตาราง skill-routing.yaml · จับคู่ข้อความของ user กับเส้นทาง · เก็บและอ่าน "สภาพของ session"
(เส้นทางที่จับได้ · skill ที่โหลดแล้ว · ไฟล์ที่อ่านแล้ว) ในไฟล์ JSON หนึ่งไฟล์ต่อ session

ผู้เรียกใช้: ice-skill-router.py · ice-skill-record.py · ice-spec-gate.py · ice-prebuild-guard.sh (ผ่านคำสั่ง check)
ที่เก็บสภาพ session: ~/.claude/state/ice-session/<session_id>.json
"""
import fnmatch
import json
import os
import re
import sys
import time

HERE = os.path.dirname(os.path.abspath(os.path.realpath(__file__)))
TABLE = os.path.join(HERE, "skill-routing.yaml")
STATE_DIR = os.path.expanduser("~/.claude/state/ice-session")


def load_table(path=TABLE):
    import yaml  # PyYAML 6 มีในเครื่องนี้ (ตรวจ 2026.09.05)
    with open(path, encoding="utf-8") as fh:
        data = yaml.safe_load(fh) or {}
    return data.get("routes", [])


def _norm(text):
    return str(text if text is not None else "").lower()


try:
    from pythainlp.tokenize import word_tokenize as _th_tok
except Exception:  # ไม่มี PyThaiNLP = ถอยไปจับข้อความย่อยเหมือนเดิม
    _th_tok = None

_TH_SHORT = 4  # คำไทยยาวไม่เกินเท่านี้ (ตัวอักษร) ต้องตรงระดับคำ ไม่ใช่ข้อความย่อย


def _keyword_hit(keyword, text):
    """คำภาษาอังกฤษล้วนจับแบบทั้งคำ (กัน word ไปตรงกับ keyword, pain ไปตรงกับ campaign)
    คำที่มีอักษรไทยจับแบบข้อความย่อย ยกเว้นคำไทยสั้น (≤4 ตัวอักษร เช่น มจร · APA ไทย) ต้องตรงระดับคำ
    ที่ PyThaiNLP ตัดให้ — บทเรียน 2026.09.05: "มจร" ไปจับใน "ซ้อมจริง" ทำให้ deck งานขายถูกบังคับโหลด skill วิชาการ"""
    k = _norm(keyword)
    if re.fullmatch(r"[a-z0-9 .\-]+", k):
        return re.search(r"(?<![a-z0-9])" + re.escape(k) + r"(?![a-z0-9])", text) is not None
    if k not in text:
        return False
    if _th_tok is not None and re.fullmatch(r"[\u0e00-\u0e7f]+", k) and len(k) <= _TH_SHORT:
        toks = [w for w in _th_tok(text, keep_whitespace=False) if w.strip()]
        return k in toks
    return True


def match_routes(prompt, cwd, routes=None):
    """คืนรายการแถวที่ตรงกับข้อความและโฟลเดอร์ (ตามลำดับในตาราง)"""
    routes = routes if routes is not None else load_table()
    p = _norm(prompt)
    cwd = cwd or ""
    hits = []
    for r in routes:
        when = r.get("when", {}) or {}
        kw_hit = any(_keyword_hit(k, p) for k in when.get("any_of", []) or [])
        path_hit = any(fnmatch.fnmatch(cwd, pat) or fnmatch.fnmatch(cwd + "/", pat) for pat in when.get("path", []) or [])
        if kw_hit or path_hit:
            hits.append(r)
    return hits


def expand(path):
    return os.path.expanduser(path)


# ── สภาพของ session ────────────────────────────────────────────────────────────
def state_path(session_id):
    sid = re.sub(r"[^A-Za-z0-9_.-]", "_", session_id or "unknown")
    os.makedirs(STATE_DIR, exist_ok=True)
    return os.path.join(STATE_DIR, sid + ".json")


def load_state(session_id):
    p = state_path(session_id)
    if os.path.exists(p):
        try:
            return json.load(open(p, encoding="utf-8"))
        except Exception:
            pass
    return {"routes": [], "required": [], "recommended": [], "read_first": [], "loaded": [], "read": [], "updated": None}


def save_state(session_id, st):
    st["updated"] = time.strftime("%Y-%m-%dT%H:%M:%S")
    json.dump(st, open(state_path(session_id), "w", encoding="utf-8"), ensure_ascii=False, indent=1)


def merge_routes_into_state(st, hits):
    for r in hits:
        if r["id"] not in st["routes"]:
            st["routes"].append(r["id"])
        for key in ("required", "recommended", "read_first"):
            for item in r.get(key, []) or []:
                if item not in st[key]:
                    st[key].append(item)
    return st


def skill_name_from_read_path(path):
    m = re.search(r"/skills/([^/]+)/SKILL\.md$", path or "")
    return m.group(1) if m else None


def record_skill(st, name):
    base = (name or "").split(":")[-1]
    if base and base not in st["loaded"]:
        st["loaded"].append(base)


def record_read(st, path):
    if not path:
        return
    real = expand(path)
    if real not in st["read"]:
        st["read"].append(real)
    sk = skill_name_from_read_path(real)
    if sk:
        record_skill(st, sk)


def missing_required(st):
    """คืน (skill ที่ยังไม่โหลด, ไฟล์ read_first ที่ยังไม่เปิด)"""
    miss_skill = [s for s in st.get("required", []) if s not in st.get("loaded", [])]
    read_set = {os.path.realpath(p) for p in st.get("read", [])}
    miss_read = [p for p in st.get("read_first", []) if os.path.realpath(expand(p)) not in read_set]
    return miss_skill, miss_read


# ── ใช้จาก shell: python3 ice_route_lib.py check <session_id>  → exit 0 ครบ · exit 3 ขาด (พิมพ์รายการที่ขาด) ──
if __name__ == "__main__":
    if len(sys.argv) >= 3 and sys.argv[1] == "check":
        st = load_state(sys.argv[2])
        ms, mr = missing_required(st)
        if not st.get("required") and not st.get("read_first"):
            sys.exit(0)  # ไม่มีเส้นทางบังคับใน session นี้
        if not ms and not mr:
            sys.exit(0)
        parts = []
        if ms:
            parts.append("skill ที่ยังไม่ได้โหลด: " + ", ".join(ms))
        if mr:
            parts.append("ไฟล์ที่ยังไม่ได้เปิดอ่าน: " + ", ".join(os.path.basename(x) for x in mr))
        print(" · ".join(parts))
        sys.exit(3)
    print("usage: ice_route_lib.py check <session_id>")
    sys.exit(2)
