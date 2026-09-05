#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ตัวชี้วัดการทำงานของทีม agent จาก log จริง — audit_fleet_logs.py (V01R01 · 2026.09.05)

ใช้ทำอะไร: วัดซ้ำทุกสัปดาห์ (เลขาคิม Lane 2) หรือเมื่อ user ถาม ว่ากลไกที่แก้เมื่อ 2026.09.05 ได้ผลจริงไหม
อ่าน transcript ใน ~/.claude/projects ตามช่วงวันที่ แล้วรายงานตัวชี้วัด 6 ตัวที่ผูกกับต้นตอในรายงาน
LLM-Memory/70-Fleet/fleet-review-2026-08-09-log-analysis.md:
  1. session ที่สร้างเอกสาร: โหลด skill ออกแบบ/เขียน "ก่อน" เขียน spec หรือ build กี่ session (เป้า 100% · เดิม 4/56)
  2. คำสั่งแก้/สั่งซ้ำของ user แยกหมวด (ภาษา · ออกแบบ/สี/icon · เลย์เอาต์ · ตรวจวน · อ่านไฟล์) (เป้า 0)
  3. รอบส่งตรวจกับอริสต่อ session สูงสุด (เป้า ≤3)
  4. จำนวน build ต่อ session และรุ่นไฟล์ที่เกิด (เป้า ลดลงจากเดิมเฉลี่ย 24 build/session)
  5. ข้อความที่ไม่เข้าตารางเส้นทาง (no-route.log) — ผู้สมัครเพิ่มแถวในตาราง
  6. token ที่ใช้ต่อ session

วิธีใช้:  python3 ~/.claude/agents/_lib/audit_fleet_logs.py --since 2026-09-01 [--until 2026-09-30] [--json]
"""
import argparse
import collections
import glob
import json
import os
import re

ROOT = os.path.expanduser("~/.claude/projects")
NO_ROUTE = os.path.expanduser("~/.claude/state/ice-session/no-route.log")
CATS = collections.OrderedDict([
    ("ภาษา", r"ลิเก|ไม่ AI|business user|business wording|ภาษา business|เวิ่น|บรรยายเกิน|เกินจริง|ไม่ย่อคำ|ทับศัพท์|แปลตรง|เหมือนแปล|อังกฤษแปลไทย|สำนวน|เขียนเป็น AI"),
    ("ออกแบบ-สี-icon", r"infograph|inforgraph|อินโฟ|icon|ไอคอน|color code|ไล่เฉด|ไล่สี|ชุดสี|ไม่สวย|template|แม่แบบ"),
    ("เลย์เอาต์-ฟอนต์", r"ทับกัน|ซ้อน|ตกขอบ|ล้น|ฟอนต์|font|ตัดคำ"),
    ("ตรวจวน", r"วน(ๆ|ไป|ซ้ำ)|กี่รอบ|อีกรอบ|ไม่จบ|เปลือง|เสียเวลา|บอกแล้ว|ย้ำ"),
    ("อ่านไฟล์-ความจำ", r"อ่านไฟล์(ใหม่|ล่าสุด|จริง)|อย่าเอาจากความจำ|ไม่ใช้ความจำ|ผมมีแก้ไป|เหมือนใหม่หมด"),
])
DESIGN_SKILLS = {"b2b-slide-designer", "b2b-presentation-creator", "ice-doc-builder", "ice-writing-register", "ice-b2b-enterprise-sale", "thesis-ai-det-col"}


def text_of(c):
    if isinstance(c, str):
        return c
    if isinstance(c, list):
        return "\n".join(b.get("text", "") for b in c if isinstance(b, dict) and b.get("type") == "text")
    return ""


def scan(since, until):
    rows = []
    for f in glob.glob(ROOT + "/*/*.jsonl"):
        first = None
        s = dict(file=f, sid=os.path.basename(f)[:8], cwd=None, user=0, builds=0, qa=0, out_tok=0, versions=set(),
                 first_skill=None, first_spec=None, first_build=None, hits=collections.Counter(), turn=0)
        try:
            fh = open(f, "rb")
        except OSError:
            continue
        for line in fh:
            try:
                j = json.loads(line)
            except Exception:
                continue
            ts = j.get("timestamp")
            if ts and first is None:
                first = ts[:10]
                if first < since or first > until:
                    break
            if s["cwd"] is None and j.get("cwd"):
                s["cwd"] = j["cwd"]
            t = j.get("type")
            if t == "user":
                txt = text_of(j.get("message", {}).get("content"))
                if txt and not j.get("isMeta") and not txt.startswith("<") and not txt.startswith("This session is being continued"):
                    s["user"] += 1
                    for k, p in CATS.items():
                        if re.search(p, txt, re.I):
                            s["hits"][k] += 1
            elif t == "assistant":
                s["turn"] += 1
                m = j.get("message", {})
                s["out_tok"] += (m.get("usage") or {}).get("output_tokens", 0)
                for b in m.get("content") or []:
                    if not isinstance(b, dict) or b.get("type") != "tool_use":
                        continue
                    n, inp = b["name"], b.get("input") or {}
                    if n == "Skill" and (inp.get("skill") or "").split(":")[-1] in DESIGN_SKILLS and s["first_skill"] is None:
                        s["first_skill"] = s["turn"]
                    if n == "Read":
                        mm = re.search(r"/skills/([^/]+)/SKILL\.md$", inp.get("file_path", ""))
                        if mm and mm.group(1) in DESIGN_SKILLS and s["first_skill"] is None:
                            s["first_skill"] = s["turn"]
                    if n in ("Write", "Edit") and re.search(r"spec", inp.get("file_path", ""), re.I) and s["first_spec"] is None:
                        s["first_spec"] = s["turn"]
                    if n in ("Agent", "Task") and "qa-master" in str(inp.get("subagent_type", "")):
                        s["qa"] += 1
                    if n == "Bash":
                        cmd = inp.get("command", "")
                        if re.search(r"ICE_BUILD=|build_[a-z0-9_]*\.py", cmd) and re.search(r"pptx|docx|xlsx", cmd, re.I):
                            s["builds"] += 1
                            if s["first_build"] is None:
                                s["first_build"] = s["turn"]
                        s["versions"].update(re.findall(r"V\d\dR\d\d", cmd))
        if first and since <= first <= until and (s["user"] or s["builds"]):
            s["date"] = first
            rows.append(s)
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--since", required=True)
    ap.add_argument("--until", default="2999-12-31")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    rows = scan(a.since, a.until)
    build_sessions = [r for r in rows if r["builds"] > 0]
    before = sum(1 for r in build_sessions if r["first_skill"] and r["first_skill"] < min(x for x in (r["first_spec"], r["first_build"]) if x) if (r["first_spec"] or r["first_build"]))
    hits = collections.Counter()
    for r in rows:
        hits.update(r["hits"])
    over_cap = [(r["sid"], r["qa"]) for r in rows if r["qa"] > 3]
    noroute = []
    if os.path.exists(NO_ROUTE):
        for line in open(NO_ROUTE, encoding="utf-8"):
            try:
                noroute.append(json.loads(line))
            except Exception:
                pass
    rep = {
        "period": [a.since, a.until], "sessions": len(rows), "build_sessions": len(build_sessions),
        "skill_before_work": f"{before}/{len(build_sessions)}",
        "user_corrections": dict(hits),
        "qa_rounds_max": max((r["qa"] for r in rows), default=0), "qa_over_cap": over_cap,
        "builds_avg": round(sum(r["builds"] for r in build_sessions) / len(build_sessions), 1) if build_sessions else 0,
        "versions_avg": round(sum(len(r["versions"]) for r in build_sessions) / len(build_sessions), 1) if build_sessions else 0,
        "out_tokens_total": sum(r["out_tok"] for r in rows),
        "no_route_entries": len(noroute), "no_route_samples": [n.get("prompt", "")[:80] for n in noroute[-5:]],
    }
    if a.json:
        print(json.dumps(rep, ensure_ascii=False, indent=1))
        return
    print(f"== ตัวชี้วัดทีม agent {a.since} → {a.until} · {rep['sessions']} session (สร้างเอกสาร {rep['build_sessions']}) ==")
    print(f"  โหลด skill ก่อนเขียน spec/build: {rep['skill_before_work']}   (เป้า ทุก session · ส.ค.–ก.ย. 2026 = 4/56)")
    print(f"  คำสั่งแก้/สั่งซ้ำของ user: " + " · ".join(f"{k} {v}" for k, v in hits.items()) + "   (เป้า 0 · เดิม ภาษา 38 ออกแบบ 87 เลย์เอาต์ 25 ตรวจวน 40 อ่านไฟล์ 28)")
    print(f"  รอบตรวจกับอริสสูงสุด/session: {rep['qa_rounds_max']} · เกินเพดาน 3: {len(over_cap)} session {over_cap[:5]}   (เดิม สูงสุด 17 · เกิน 16/28)")
    print(f"  build เฉลี่ย/session: {rep['builds_avg']} · รุ่นไฟล์เฉลี่ย: {rep['versions_avg']}   (เดิม 24 build)")
    print(f"  output token รวม: {rep['out_tokens_total']:,}")
    print(f"  ข้อความที่ไม่เข้าตารางเส้นทาง: {rep['no_route_entries']} รายการ — ตัวอย่างล่าสุด: {rep['no_route_samples']}")


if __name__ == "__main__":
    main()
