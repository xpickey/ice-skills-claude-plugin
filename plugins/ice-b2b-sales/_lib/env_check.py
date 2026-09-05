#!/usr/bin/env python3
"""ตรวจสภาพแวดล้อมเครื่องมือเอกสารของ fleet — ตอบคำถามเดียว: "งานที่จะทำ ใช้ตัวแปลภาษาตัวไหน และของครบไหม"

ทำไมต้องมีไฟล์นี้ (บทเรียน 2026.08.09 · งานบทความวิชาการที่ 8):
มีคนเช็ค python-docx ด้วย python ของ .venv-doc แล้วไม่เจอ จึงรายงานว่าเครื่องมือใช้ไม่ได้
ทั้งที่ python ของระบบมีครบมาตลอด — ต้นเหตุคือ "ข้อเท็จจริงเรื่องสภาพแวดล้อมถูกเขียนไว้เป็นข้อความ
ในไฟล์กติกา ซึ่งผู้อ่านอาจไม่ได้อ่าน หรืออ่านแล้วข้อความนั้นเก่าไปแล้ว"
ทางแก้ถาวรคือย้ายข้อเท็จจริงนั้นมาอยู่ในเครื่องมือที่ "รันแล้วรู้ผลจากของจริง ณ ตอนนั้น"

วิธีใช้:
    python3 ~/.claude/agents/_lib/env_check.py build      # ก่อนสร้างเอกสาร (PRE-BUILD CHECK) ← ใส่ชื่องานเสมอ
    python3 ~/.claude/agents/_lib/env_check.py read       # ก่อนอ่าน/แปลงเอกสาร
    python3 ~/.claude/agents/_lib/env_check.py thai       # ก่อนงานที่ต้องตัดคำ/ตรวจภาษาไทย
    python3 ~/.claude/agents/_lib/env_check.py            # ภาพรวมทุกงาน — exit สะท้อนทุกงานรวมกัน
                                                          # อย่าใช้โหมดนี้ตัดสินงานเดียว (งานอื่นขาดก็ exit 1)

exit 0 = ครบใช้งานได้ · exit 1 = ขาดจริงสำหรับตัวแปลภาษาที่งานนั้นกำหนด (ข้อความบอกวิธีติดตั้ง)
· exit 2 = เรียกผิดวิธี (ชื่องานไม่รู้จัก หรือใส่ flag ที่ขึ้นต้นด้วยขีด)
"""
from __future__ import annotations

import importlib.util
import shutil
import subprocess
import sys
from pathlib import Path

LIB = Path(__file__).resolve().parent
VENV_DOC = LIB / ".venv-doc" / "bin" / "python"

# งาน → (ไลบรารีที่ต้องมี, ตัวแปลภาษาที่เป็นเจ้าของงานนี้, วิธีติดตั้งเมื่อขาด)
JOBS: dict[str, dict] = {
    "build": {
        "หน้าที่": "สร้างและแก้ไฟล์ .docx / .xlsx / .pptx",
        "interpreter": sys.executable,
        "interpreter_label": "python3 ของระบบ",
        "modules": {"docx": "python-docx", "openpyxl": "openpyxl", "pptx": "python-pptx"},
        "install": '{py} -m pip install python-docx openpyxl python-pptx',
    },
    "read": {
        "หน้าที่": "อ่าน/แปลงเอกสารเป็น Markdown + คัดกรอง PDF + OCR ในเครื่อง",
        "interpreter": str(VENV_DOC),
        "interpreter_label": "python ของ .venv-doc (แยกไว้เฉพาะงานอ่าน)",
        "modules": {"anydoc": "firecrawl-anydoc", "pdf_inspector": "pdf-inspector"},
        "install": '{py} -m pip install firecrawl-anydoc pdf-inspector',
    },
    "thai": {
        "หน้าที่": "ตัดคำไทย ตรวจสระซ้ำ แปลงจำนวนเงินเป็นตัวหนังสือ",
        "interpreter": sys.executable,
        "interpreter_label": "python3 ของระบบ",
        "modules": {"pythainlp": "pythainlp"},
        "install": '{py} -m pip install pythainlp',
    },
}


def probe(interpreter: str, modules: dict[str, str]) -> dict[str, bool]:
    """ถามตัวแปลภาษาตัวนั้นจริง ๆ ว่ามีโมดูลอะไรบ้าง — ไม่เดาจากของที่ process นี้ import ได้"""
    if interpreter == sys.executable:
        return {m: importlib.util.find_spec(m) is not None for m in modules}
    if not Path(interpreter).exists():
        return dict.fromkeys(modules, False)
    code = "import importlib.util as u;print(','.join(m for m in %r if u.find_spec(m)))" % list(modules)
    try:
        out = subprocess.run([interpreter, "-c", code], capture_output=True, text=True, timeout=30)
        found = set(filter(None, out.stdout.strip().split(",")))
    except (subprocess.SubprocessError, OSError):
        return dict.fromkeys(modules, False)
    return {m: m in found for m in modules}


def report(job: str) -> bool:
    spec = JOBS[job]
    interpreter = spec["interpreter"]
    results = probe(interpreter, spec["modules"])
    missing = [spec["modules"][m] for m, ok in results.items() if not ok]

    print(f"\n[{job}] {spec['หน้าที่']}")
    print(f"  ตัวแปลภาษาที่ต้องใช้: {spec['interpreter_label']}")
    print(f"    {interpreter}")
    for mod, pkg in spec["modules"].items():
        print(f"  {'✅' if results[mod] else '❌'} {pkg}")

    if missing:
        if interpreter != sys.executable and not Path(interpreter).exists():
            # venv หายทั้งตัว — คำสั่ง pip ของ path ที่ไม่มีอยู่รันไม่ได้ ต้องสร้าง venv ก่อน
            print("  → ตัวแปลภาษาของงานนี้ยังไม่มีอยู่จริง — สร้างก่อนด้วย:")
            print(f"     python3.12 -m venv {VENV_DOC.parent.parent}")
            print(f"     แล้วติดตั้ง: {spec['install'].format(py=interpreter)}")
        else:
            print(f"  → ขาด {', '.join(missing)} · ติดตั้งด้วย:")
            print(f"     {spec['install'].format(py=interpreter)}")
    return not missing


def extras() -> None:
    """เครื่องมือนอก Python ที่งานเอกสารพึ่งพา — บอกผลตามจริง ไม่ทำให้ทั้งชุดล้มเหลว"""
    print("\n[เครื่องมือประกอบ] (✅ = มีแล้ว · ⬜ = ยังไม่มี — ไม่นับเป็นความล้มเหลว แต่ฟีเจอร์ที่ระบุจะใช้ไม่ได้)")
    for cmd, ใช้ทำอะไร in (
        ("pdftoppm", "แปลงหน้า PDF เป็นภาพก่อน OCR (มากับ poppler)"),
        ("soffice", "แปลงไฟล์เป็น PDF สำหรับดูภาพ — ⚠️ ผลที่ได้ใช้ยืนยันฟอนต์ไม่ได้"),
    ):
        print(f"  {'✅' if shutil.which(cmd) else '⬜'} {cmd} — {ใช้ทำอะไร}")
    word = Path("/Applications/Microsoft Word.app")
    print(f"  {'✅' if word.exists() else '⬜'} Microsoft Word — ใช้ยืนยันว่าไฟล์เปิดได้จริงไม่ขึ้น Repair")


def main() -> int:
    flags = [a for a in sys.argv[1:] if a.startswith("-")]
    if flags:
        # กันเข้าใจผิด: `--build` จะถูกมองเป็น flag ไม่ใช่ชื่องาน — บอกตรง ๆ ดีกว่าเงียบแล้วตรวจทุกงาน
        print(f"ไม่รับ flag {flags[0]!r} — ใส่ชื่องานเปล่า ๆ: {', '.join(JOBS)} (เช่น env_check.py build)", file=sys.stderr)
        return 2
    args = sys.argv[1:]
    if args and args[0] not in JOBS:
        print(f"ไม่รู้จักงาน {args[0]!r} — เลือกจาก: {', '.join(JOBS)}", file=sys.stderr)
        return 2

    if ".venv-doc" in sys.executable:
        # สคริปต์นี้ต้องรันด้วย python3 ของระบบ — รันด้วย python ของ venv แล้วงาน build/thai จะถูกถามผิดตัวทันที
        print("⚠️ กำลังรัน env_check ด้วย python ของ .venv-doc — ผลของงาน build/thai จะไม่ตรงความจริง")
        print("   รันใหม่ด้วย: python3 ~/.claude/agents/_lib/env_check.py " + (args[0] if args else ""))
        return 2

    jobs = args or list(JOBS)
    status = {j: report(j) for j in jobs}
    ok = all(status.values())
    if not args:
        extras()

    print()
    if ok:
        print("✅ ครบตามที่งานต้องใช้")
    else:
        failed = [j for j, v in status.items() if not v]
        passed = [j for j, v in status.items() if v]
        print(f"❌ ขาดของในงาน: {', '.join(failed)}" + (f" · งานที่ครบดี: {', '.join(passed)}" if passed else ""))
        print("   ติดตั้งตามคำสั่งข้างบนแล้วรันซ้ำ · exit 1 นี้สะท้อนเฉพาะงานที่ระบุข้างต้น")
        print("   หมายเหตุ: ไลบรารีที่ 'หาไม่เจอ' นอกสคริปต์นี้ ส่วนใหญ่เกิดจากเรียกผิดตัวแปลภาษา")
        print("   ก่อนสรุปว่าขาดจริง ให้ดูบรรทัด 'ตัวแปลภาษาที่ต้องใช้' ของงานนั้นก่อนเสมอ")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
