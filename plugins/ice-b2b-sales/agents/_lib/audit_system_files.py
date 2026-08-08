#!/usr/bin/env python3
"""audit_system_files.py — ด่านตรวจความอ่านรู้เรื่องของไฟล์ระบบ (agent · skill · reference · CLAUDE.md)

V01R05 · 2026.08.08 · FLEET READABILITY V3 Phase 4

ทำอะไร
------
ตรวจว่าไฟล์ระบบหนึ่งไฟล์ "อ่านลำพังแล้วเข้าใจ" ตามมาตรฐานที่ประกาศไว้ใน
`~/.claude/agents/reference/fleet-writing-standard.md` หรือไม่ โดยตรวจ 4 ข้อที่ตรวจด้วยเครื่องได้:

  C1 UNDEFINED-CODE  รหัสภายในระบบที่ไฟล์ใช้ แต่ไม่ได้นิยามไว้ในไฟล์ตัวเอง
                     (เช่น ใช้ ⑤ หรือ D-P3 โดยไม่มีบรรทัดไหนบอกว่ามันคืออะไร)
  C2 NO-GLOSSARY     ไฟล์ใช้รหัสตั้งแต่ 3 ตัวขึ้นไป แต่ไม่มีหัวข้อนิยาม/ตารางนิยามเลย
  C3 FRAGMENT        สัดส่วนบรรทัดคำสั่งที่เป็นเศษวลี (สั้นมากและไม่มีคำกริยา/คำบ่งชี้)
  C4 SHORT-HEADING   หัวข้อที่สั้นจนไม่สื่อความ (เช่น "## กฎ" "## Rules")

เกณฑ์ตัดสิน (ปรับได้ด้วย flag)
-----------------------------
  FAIL  = มี C1 (รหัสไม่นิยาม) หรือ C2 หรือ สัดส่วนเศษวลี > --fragment-max (ค่าตั้งต้น 35%)
  WARN  = มีเฉพาะ C4 หรือสัดส่วนเศษวลีอยู่ระหว่าง 25% ถึงเพดาน
  PASS  = ไม่เข้าเงื่อนไขข้างบน

ใช้อย่างไร
---------
  python3 audit_system_files.py PATH [PATH ...]        # ไฟล์หรือโฟลเดอร์ก็ได้
  python3 audit_system_files.py ~/.claude/skills --summary
  python3 audit_system_files.py ~/.claude/agents --json report.json
  python3 audit_system_files.py ~/.claude/agents --gate  # โหมดด่าน: เจอ FAIL แล้ว exit 1

exit code: 0 = ไม่มีไฟล์ FAIL · 1 = มีไฟล์ FAIL (ใช้เป็นด่านใน deploy) · 2 = เรียกใช้ผิดวิธี
"""

import argparse
import json
import os
import re
import sys

# ── รหัสภายในระบบที่ "ถ้าใช้ ต้องนิยามในไฟล์ตัวเอง" ────────────────────────────
# key = ชื่อที่แสดงในรายงาน · value = regex ที่ใช้หาในเนื้อไฟล์
CODE_PATTERNS = {
    "team-code(เลขวงกลม)": r"[②③④⑤⑥⑦]",
    "D-P0..D-P5": r"\bD-P[0-5]\b",
    "DM-0..DM-5": r"\bDM-[0-5]\b",
    "L0/L1/L2": r"(?<![A-Za-z0-9])L[012](?![0-9A-Za-z])",
    "TAAE": r"\bTAAE\b",
    "RAILS": r"\bRAILS\b",
    "SSOT": r"\bSSOT\b",
    "MEDDPICC": r"\bMEDDPICC\b",
    "envelope/ซองผลงาน": r"\benvelope\b",
    "DISK-IS-TRUTH": r"DISK-IS-TRUTH",
    "ICE_BUILD/ICE_SMARTFIX": r"ICE_(BUILD|SMARTFIX|BUILDER|INLINE_APPROVED)",
    "H-rule(H1..H10)": r"(?<![A-Za-z0-9])H(?:10|[1-9])(?![0-9A-Za-z])",
    "A1 gate": r"\bA1[ /]?gate\b",
    "V##R##": r"V##R##",
    "TOR": r"\bTOR\b",
    "tier(DRAFT/FAST/FULL)": r"(?<![A-Za-z])(qa_)?tier\b",
}

# คำที่บ่งบอกว่าบรรทัดนั้น "นิยาม" ของสิ่งที่พูดถึง
DEFINE_MARKERS = ("คือ", "หมายถึง", "ย่อจาก", "ได้แก่", "นิยาม", "กำหนดว่า", "แปลว่า",
                  "=", "means", "stands for", ":")

# หัวข้อหรือบรรทัดตัวหนาที่ถือว่าเป็นส่วนนิยาม (บาง agent เขียนนิยามเป็นบรรทัดตัวหนา ไม่ใช่หัวข้อ)
GLOSSARY_HEADING = re.compile(
    r"^[>\s]*(#{1,4}|\*\*)\s*[^\n]{0,40}?(นิยาม|ศัพท์|ตัวย่อ|glossary|definitions?)", re.IGNORECASE
)

# รูปแบบ "รายการนิยาม": บรรทัดที่ขึ้นต้นด้วยคำตัวหนา แล้วตามด้วยคำอธิบาย
# เช่น "> · **SSOT (Single Source of Truth)** แหล่งข้อมูลจริงเพียงแห่งเดียว…"
GLOSSARY_ENTRY = re.compile(r"^[>\s·\-*+\d.]*\*\*(?P<term>[^*]{1,120})\*\*\s*\S")

# คำกริยา/คำบ่งชี้ที่ทำให้บรรทัดหนึ่ง "เป็นคำสั่งที่อ่านรู้เรื่อง" ไม่ใช่เศษวลี
VERB_MARKERS = (
    "ต้อง", "ห้าม", "ให้", "ใช้", "เป็น", "คือ", "มี", "ทำ", "อ่าน", "เขียน", "ตรวจ", "ส่ง",
    "เลือก", "ถาม", "หยุด", "แจ้ง", "เก็บ", "สร้าง", "แก้", "รัน", "บันทึก", "ยืนยัน", "จบ",
    "must", "should", "use", "run", "check", "read", "write", "ask", "stop", "send", "keep",
    "build", "fix", "verify", "return", "never", "always", "do ", "is ", "are ",
)

SKIP_DIR_NAMES = {".git", "node_modules", "__pycache__", ".venv-doc", "assets", "scripts",
                  "archive", "voice_profiles", "templates"}

# ── ขอบเขตการตรวจ ────────────────────────────────────────────────────────────
# entry (ค่าตั้งต้น) = ไฟล์ "ประตูหน้า" ที่ model อ่านแล้วต้องทำงานได้ทันที ได้แก่ SKILL.md ของทุก skill,
#   ไฟล์ agent, ไฟล์กติกากลางใน agents/reference/ และ CLAUDE.md — เป็นชุดที่กฎเหล็ก H10 บังคับ
# deep = รวมไฟล์ reference ย่อยของ skill ด้วย (คลังความรู้/ตารางข้อมูล) — ใช้ตอนอยากสำรวจภาพรวม
#   ไม่ใช้เป็นด่าน deploy เพราะไฟล์ตารางข้อมูลมีสัดส่วนบรรทัดสั้นสูงโดยธรรมชาติ
ENTRY_NAMES = {"SKILL.md", "CLAUDE.md"}

# ไฟล์บันทึกประวัติและ log = เอกสารบันทึกเหตุการณ์ ไม่ใช่คำสั่งที่ model ต้องอ่านแล้วลงมือทำ
# จึงไม่อยู่ในด่านนี้ (การบังคับให้มีตารางนิยามในไฟล์ประวัติจะได้ความยาวโดยไม่ได้ความเข้าใจเพิ่ม)
RECORD_FILE_HINTS = ("changelog", "-log", "_log", "qa-log")


def is_record_file(path: str) -> bool:
    name = os.path.basename(path).lower()
    return any(h in name for h in RECORD_FILE_HINTS)


def is_entry_file(path: str) -> bool:
    name = os.path.basename(path)
    if name in ENTRY_NAMES:
        return True
    if is_record_file(path):
        return False
    parent = os.path.basename(os.path.dirname(path))
    grandparent = os.path.basename(os.path.dirname(os.path.dirname(path)))
    return parent == "agents" or (parent == "reference" and grandparent == "agents")


def strip_frontmatter(text: str) -> str:
    """ตัดบล็อก YAML frontmatter ออก — คอมเมนต์ในนั้นเขียนไว้ให้ผู้ดูแลไฟล์ ไม่ใช่เนื้อกติกาที่ผู้อ่านต้องใช้"""
    if not text.startswith("---"):
        return text
    end = text.find("\n---", 3)
    return text[end + 4:] if end != -1 else text


def strip_code_blocks(text: str):
    """คืน (เนื้อที่ตัด code block ออกแล้ว, จำนวนบล็อกที่ตัด) — กันโค้ดตัวอย่างมาปนการนับ"""
    out, inside, count = [], False, 0
    for line in text.split("\n"):
        if line.lstrip().startswith("```"):
            inside = not inside
            if inside:
                count += 1
            continue
        if not inside:
            out.append(line)
    return "\n".join(out), count


def has_definition(prose: str, label: str, pattern: str) -> bool:
    """ไฟล์นิยามรหัสนี้ไว้เองหรือไม่ — ถือว่านิยามเมื่อรหัสปรากฏในบรรทัดที่มีคำบ่งชี้การนิยาม"""
    rx = re.compile(pattern)
    for line in prose.split("\n"):
        if not rx.search(line):
            continue
        if line.lstrip().startswith("|") and line.count("|") >= 3:
            return True  # แถวตารางนิยาม
        if GLOSSARY_ENTRY.match(line):
            return True  # บรรทัดรายการนิยาม (ขึ้นต้นด้วยคำตัวหนาแล้วตามด้วยคำอธิบาย) ที่กล่าวถึงรหัสนี้
        if any(mk in line for mk in DEFINE_MARKERS):
            return True
    return False


def audit_file(path: str, fragment_max: float) -> dict:
    raw = open(path, encoding="utf-8", errors="replace").read()
    prose, _ = strip_code_blocks(strip_frontmatter(raw))
    lines = prose.split("\n")

    used, undefined = [], []
    for label, pattern in CODE_PATTERNS.items():
        hits = len(re.findall(pattern, prose))
        if hits == 0:
            continue
        used.append(label)
        if not has_definition(prose, label, pattern):
            undefined.append(f"{label} (พบ {hits} ครั้ง)")

    has_glossary = any(GLOSSARY_HEADING.match(l.strip()) for l in lines)

    bullets, fragments = 0, []
    for line in lines:
        s = line.strip()
        if not re.match(r"^([-*+]|\d+\.)\s+", s):
            continue
        body = re.sub(r"^([-*+]|\d+\.)\s+", "", s)
        body_plain = re.sub(r"[*`_#>|]", "", body).strip()
        if not body_plain:
            continue
        # ข้ามรายการแบบ "ศัพท์ — คำอธิบาย" หรือ "`ตัวเลือก` คำอธิบาย" — เป็นรายการนิยาม/ตัวเลือก
        # ไม่ใช่บรรทัดคำสั่ง จึงสั้นได้ตามธรรมชาติ (มาตรฐานเล็งไปที่ "คำสั่งที่เขียนเป็นเศษวลี")
        is_entry = bool(re.match(r"^(\*\*|`)", body.strip())) or any(
            sep in body_plain for sep in ("—", "–", " = ", ": ", " → ")
        )
        bullets += 1
        if not is_entry and len(body_plain) < 40 and not any(v in body_plain for v in VERB_MARKERS):
            fragments.append(body_plain[:60])
    frag_ratio = (len(fragments) / bullets) if bullets else 0.0

    short_headings = []
    for line in lines:
        m = re.match(r"^(#{1,6})\s+(.*)$", line.strip())
        if not m:
            continue
        title = re.sub(r"[*`#⭐🔴⛔⚠️️0-9.§\s]+", " ", m.group(2)).strip()
        if 0 < len(title) < 8:
            short_headings.append(m.group(2).strip()[:50])

    verdict = "PASS"
    reasons = []
    if undefined:
        verdict, _ = "FAIL", reasons.append(f"รหัสที่ใช้แต่ไม่นิยามในไฟล์: {', '.join(undefined)}")
    if len(used) >= 3 and not has_glossary:
        verdict = "FAIL"
        reasons.append(f"ใช้รหัสระบบ {len(used)} ชนิด แต่ไม่มีหัวข้อนิยามในไฟล์")
    if frag_ratio > fragment_max:
        verdict = "FAIL"
        reasons.append(f"บรรทัดคำสั่งเป็นเศษวลี {frag_ratio:.0%} (เพดาน {fragment_max:.0%})")
    elif frag_ratio > fragment_max * 0.7 and verdict == "PASS":
        verdict = "WARN"
        reasons.append(f"บรรทัดคำสั่งเป็นเศษวลี {frag_ratio:.0%} — ใกล้เพดาน")
    if short_headings and verdict == "PASS":
        verdict = "WARN"
        reasons.append(f"หัวข้อสั้นจนไม่สื่อความ {len(short_headings)} จุด")

    return {
        "file": path,
        "verdict": verdict,
        "reasons": reasons,
        "codes_used": used,
        "codes_undefined": undefined,
        "has_glossary": has_glossary,
        "bullets": bullets,
        "fragment_ratio": round(frag_ratio, 3),
        "fragment_examples": fragments[:5],
        "short_headings": short_headings[:5],
    }


def collect(paths, scope="entry"):
    found = []
    for p in paths:
        p = os.path.expanduser(p)
        if os.path.isfile(p):
            found.append(p)  # ระบุไฟล์ตรง = ตรวจเสมอ ไม่ว่าขอบเขตจะเป็นแบบใด
            continue
        for root, dirs, files in os.walk(p):
            dirs[:] = [d for d in dirs if d not in SKIP_DIR_NAMES]
            for f in files:
                if not f.endswith(".md") or f.endswith(".bak"):
                    continue
                full = os.path.join(root, f)
                if scope == "entry" and not is_entry_file(full):
                    continue
                found.append(full)
    return sorted(set(found))


def main():
    ap = argparse.ArgumentParser(description="ตรวจความอ่านรู้เรื่องของไฟล์ระบบ")
    ap.add_argument("paths", nargs="+", help="ไฟล์ .md หรือโฟลเดอร์")
    ap.add_argument("--fragment-max", type=float, default=0.35, help="เพดานสัดส่วนเศษวลี (0-1)")
    ap.add_argument("--summary", action="store_true", help="แสดงเฉพาะสรุปและไฟล์ที่ไม่ผ่าน")
    ap.add_argument("--json", metavar="OUT", help="เขียนรายงานเป็นไฟล์ JSON")
    ap.add_argument("--scope", choices=["entry", "deep"], default="entry",
                    help="entry = SKILL.md + agent + reference กลาง + CLAUDE.md (ค่าตั้งต้น · ใช้เป็นด่าน) · "
                         "deep = รวมไฟล์ reference ย่อยของ skill ด้วย (สำรวจภาพรวมเท่านั้น)")
    ap.add_argument("--gate", action="store_true", help="โหมดด่าน: มี FAIL แล้วคืน exit 1")
    args = ap.parse_args()

    files = collect(args.paths, args.scope)
    if not files:
        print("ไม่พบไฟล์ .md ในเส้นทางที่ระบุ", file=sys.stderr)
        return 2

    results = [audit_file(f, args.fragment_max) for f in files]
    fails = [r for r in results if r["verdict"] == "FAIL"]
    warns = [r for r in results if r["verdict"] == "WARN"]

    for r in results:
        if args.summary and r["verdict"] == "PASS":
            continue
        mark = {"PASS": "✅", "WARN": "⚠️ ", "FAIL": "❌"}[r["verdict"]]
        print(f"{mark} {r['verdict']:4}  {r['file']}")
        for reason in r["reasons"]:
            print(f"        · {reason}")

    print(f"\nรวม {len(results)} ไฟล์ — ผ่าน {len(results)-len(fails)-len(warns)} · "
          f"เตือน {len(warns)} · ไม่ผ่าน {len(fails)}")

    if args.json:
        with open(args.json, "w", encoding="utf-8") as fh:
            json.dump(results, fh, ensure_ascii=False, indent=2)
        print(f"รายงานฉบับเต็ม: {args.json}")

    if args.gate and fails:
        print("\n🔴 ด่านไม่ผ่าน — แก้ไฟล์ที่ขึ้น FAIL ก่อน deploy "
              "(กฎเหล็ก H10: ไฟล์ระบบต้องอ่านลำพังแล้วเข้าใจ)", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
