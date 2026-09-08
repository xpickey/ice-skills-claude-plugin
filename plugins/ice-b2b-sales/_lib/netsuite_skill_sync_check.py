# -*- coding: utf-8 -*-
"""ตรวจว่า skill ของ NetSuite ที่นำเข้าจาก Oracle ยังตรงกับต้นทางหรือไม่ และของที่ทีมแก้เองยังอยู่ครบหรือไม่

ที่มา: skill ตระกูล netsuite-* ใน plugin นี้คัดลอกมาจากคลังโค้ดสาธารณะ
oracle/netsuite-suitecloud-sdk โฟลเดอร์ packages/agent-skills ซึ่ง Oracle แก้ไขเองเรื่อย ๆ
โดยไม่มีใครมาบอกเรา สคริปต์นี้จึงทำหน้าที่สี่อย่างในการรันครั้งเดียว

  ① เทียบเนื้อความของ SKILL.md ทุกตัวกับต้นทาง โดยข้ามส่วนหัว frontmatter
     เพราะทีมแปลช่อง description ในส่วนนั้นเป็นภาษาไทยเอง จึงต่างจากต้นทางโดยตั้งใจเสมอ
  ② ตรวจว่าช่อง description ของทุกตัวยังเป็นภาษาไทยอยู่ ข้อนี้จำเป็นเพราะข้อ ① ข้ามส่วนนั้นไป
     ถ้าไม่ตรวจซ้ำตรงนี้ การคัดลอกทับที่ทำให้ description กลับไปเป็นภาษาอังกฤษจะไม่มีใครเห็น
     ผลที่ตามมาคือระบบเลือก skill ไม่เจอเมื่อผู้ใช้พิมพ์ภาษาไทย ซึ่งเป็นผู้ใช้หลักของระบบนี้
  ③ เทียบไฟล์ประกอบในโฟลเดอร์ references/ ของแต่ละ skill ทีละไฟล์ด้วยรหัสย่อของ git
     พร้อมรายงานไฟล์ที่ต้นทางมีแต่เราไม่มี และไฟล์ที่เรามีแต่ต้นทางไม่มี
  ④ รายงาน skill ชุดใหม่ที่ Oracle เพิ่มเข้ามาแต่เรายังไม่ได้นำเข้า

สิ่งที่ต้องมีก่อนรัน: ต้องติดตั้ง GitHub CLI (คำสั่งชื่อ gh) และเข้าสู่ระบบด้วย gh auth login แล้ว
และเครื่องต้องต่ออินเทอร์เน็ตได้ เพราะสคริปต์ดึงไฟล์จากต้นทางมาเทียบสด ถ้าดึงไม่ได้
สคริปต์จะหยุดพร้อมข้อความบอกสาเหตุและจบด้วยรหัส 2 ไม่ใช่รายงานว่าทุกอย่างเรียบร้อย

วิธีรัน — ยืนที่รากของคลังโค้ด iCE-Skills-Marketplace แล้วสั่ง:
    python3 plugins/ice-b2b-sales/_lib/netsuite_skill_sync_check.py
สคริปต์หาโฟลเดอร์ skills จากตำแหน่งของตัวเอง จึงรันจากที่อื่นก็ได้ผลเดียวกัน

รหัสจบของคำสั่ง (สิ่งที่ระบบปฏิบัติการคืนให้ ดูได้ด้วย echo $? ต่อท้าย):
    0 = ไม่พบเรื่องที่ต้องจัดการ
    1 = พบเรื่องที่ต้องจัดการ อ่านรายการท้ายผลแล้วทำตามขั้นตอนในหัวข้อถัดไป
    2 = ตรวจไม่สำเร็จ เช่น ไม่มีคำสั่ง gh หรือดึงข้อมูลจากต้นทางไม่ได้ — ยังไม่รู้ผล ห้ามสรุปว่าเรียบร้อย

เมื่อผลออกมาว่ามีเรื่องต้องจัดการ ห้ามคัดลอกไฟล์จากต้นทางทับทันที ให้ทำสามขั้นนี้:
  1. ดูความต่างจริงก่อน ด้วยคำสั่งนี้ (แทน <ชื่อ skill> ด้วยชื่อโฟลเดอร์ที่สคริปต์ฟ้อง):
       gh api repos/oracle/netsuite-suitecloud-sdk/contents/packages/agent-skills/<ชื่อ skill>/SKILL.md \
         --jq .content | base64 -d > /tmp/upstream-SKILL.md
       diff /tmp/upstream-SKILL.md plugins/ice-b2b-sales/skills/<ชื่อ skill>/SKILL.md
  2. ของที่ทีมแก้เองและต้องรักษาไว้ทุกครั้ง ดูได้จากตัวแปร KNOWN_LOCAL_EDITS ข้างล่าง
     ซึ่งบอกทั้งว่าเพิ่มอะไรไว้ และไฟล์ประกอบที่เราเพิ่มเองมีชื่อขึ้นต้นด้วยอะไร
  3. รวมของใหม่จาก Oracle เข้ากับของเราด้วยมือ แล้วรันสคริปต์นี้ซ้ำจนได้รหัสจบ 0
"""
import base64
import hashlib
import json
import os
import re
import subprocess
import sys

REPO = "oracle/netsuite-suitecloud-sdk"
UPSTREAM_DIR = "packages/agent-skills"
SKILLS_DIR = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "skills"))

# ทะเบียนความต่างที่ทีมตั้งใจสร้างเอง ประกาศไว้ที่นี่เพื่อไม่ให้เครื่องตรวจฟ้องซ้ำทุกครั้งจนคนเลิกอ่านผล
#   note        คำอธิบายว่าเราเพิ่มอะไรไว้และเมื่อไหร่ แสดงในผลการตรวจเพื่อเตือนผู้ที่จะรวมของใหม่
#   extra_files ชื่อขึ้นต้นของไฟล์ประกอบที่เราเพิ่มเอง สคริปต์จะไม่ฟ้องว่าเป็นไฟล์แปลกปลอม
# เพิ่มรายการที่นี่ได้ต่อเมื่อความต่างนั้นเป็นของที่ทีมเขียนเองจริงและตรวจแล้ว
# ห้ามเพิ่มเพื่อกลบผลที่ยังไม่ได้ตรวจ เพราะจุดประสงค์ของทะเบียนคือทำให้ผลที่เหลือน่าเชื่อถือ ไม่ใช่ทำให้ผลผ่าน
KNOWN_LOCAL_EDITS = {
    "netsuite-finance-analyst": {
        "note": "แปล description เป็นภาษาไทย และย้าย compatibility จาก frontmatter มาเป็นข้อความใต้หัวเรื่อง "
                "เพราะตัวตรวจปลั๊กอินของ Codex รับเฉพาะช่อง metadata ที่กำหนดไว้ เนื้อหาความสามารถเดิมยังอยู่ครบ",
        "extra_files": [],
    },
    "netsuite-suitescript-records-reference": {
        "note": "หัวข้อ REST Web Services (SuiteTalk REST) — Record API พร้อมไฟล์ประกอบ references/rest-*.md "
                "ที่ทีมสกัดจาก REST API Browser รุ่น 2024.2 เมื่อ 2026.08.07 ต้นทางของ Oracle ไม่มีส่วนนี้ "
                "ถ้าส่วนนี้หายไป ทีมจะตอบคำถามเรื่องชื่อ field ฝั่ง REST ไม่ได้ และจะเผลอตอบด้วยชื่อ field "
                "ฝั่ง SuiteScript ซึ่งเป็นคนละชุดกัน",
        "extra_files": ["references/rest-"],
    },
}

THAI = re.compile(r"[฀-๿]")


class UpstreamError(Exception):
    """ดึงข้อมูลจากต้นทางไม่ได้ — ยังไม่รู้ผล ห้ามสรุปว่าเรียบร้อย"""


def gh(*args):
    try:
        r = subprocess.run(["gh"] + list(args), capture_output=True, text=True)
    except FileNotFoundError:
        raise UpstreamError("ไม่พบคำสั่ง gh — ติดตั้ง GitHub CLI แล้วรัน gh auth login ก่อน")
    if r.returncode != 0:
        raise UpstreamError("เรียกต้นทางไม่สำเร็จ: gh %s\n%s" % (" ".join(args), r.stderr.strip()))
    return r.stdout


def upstream_tree():
    """คืน dict {path ใต้ packages/agent-skills: รหัสย่อของ git} ของไฟล์ทุกไฟล์ในต้นทาง"""
    raw = gh("api", "repos/%s/git/trees/HEAD?recursive=1" % REPO)
    out = {}
    for node in json.loads(raw).get("tree", []):
        p = node.get("path", "")
        if node.get("type") == "blob" and p.startswith(UPSTREAM_DIR + "/"):
            out[p[len(UPSTREAM_DIR) + 1:]] = node["sha"]
    if not out:
        raise UpstreamError("ต้นทางไม่คืนรายการไฟล์ใด ๆ ใน %s — โครงสร้าง repo อาจเปลี่ยน" % UPSTREAM_DIR)
    return out


def git_blob_sha(path):
    """รหัสย่อแบบเดียวกับที่ git ใช้ คำนวณเองได้โดยไม่ต้องมี git ในเครื่อง"""
    data = open(path, "rb").read()
    h = hashlib.sha1()
    h.update(b"blob %d\x00" % len(data))
    h.update(data)
    return h.hexdigest()


def split_frontmatter(text):
    """คืนคู่ (ส่วนหัว, เนื้อความ) — ถ้าไม่มีส่วนหัว คืน ("", ทั้งไฟล์)"""
    lines = text.splitlines(True)
    if lines and lines[0].strip() == "---":
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                return "".join(lines[1:i]), "".join(lines[i + 1:])
    return "", text


def body_digest(text):
    return hashlib.md5(split_frontmatter(text)[1].encode("utf-8")).hexdigest()


def local_skills():
    return sorted(
        d for d in os.listdir(SKILLS_DIR)
        if d.startswith("netsuite-") and os.path.isfile(os.path.join(SKILLS_DIR, d, "SKILL.md"))
    )


def local_files(skill):
    """รายชื่อไฟล์ทั้งหมดของ skill หนึ่งตัว เขียนเป็น path สัมพัทธ์กับโฟลเดอร์ skill นั้น"""
    root = os.path.join(SKILLS_DIR, skill)
    out = []
    for dirpath, _dirnames, filenames in os.walk(root):
        for fn in filenames:
            if fn == ".DS_Store":
                continue
            full = os.path.join(dirpath, fn)
            out.append(os.path.relpath(full, root))
    return sorted(out)


def check(skill, tree, todo):
    """ตรวจ skill หนึ่งตัว พิมพ์ผล และเติมเรื่องที่ต้องจัดการลงใน todo"""
    known = KNOWN_LOCAL_EDITS.get(skill, {})
    path = os.path.join(SKILLS_DIR, skill, "SKILL.md")
    text = open(path, encoding="utf-8").read()

    up_key = "%s/SKILL.md" % skill
    if up_key not in tree:
        print("  %-42s ต้นทางไม่มีตัวนี้ (เป็น skill ที่ทีมเขียนเอง จึงไม่ต้องเทียบ)" % skill)
        return

    remote = base64.b64decode(
        gh("api", "repos/%s/contents/%s/%s" % (REPO, UPSTREAM_DIR, up_key), "--jq", ".content")
    ).decode("utf-8")

    # ① เนื้อความ
    if body_digest(text) == body_digest(remote):
        print("  %-42s เนื้อความตรงกับต้นทาง" % skill)
    elif known:
        print("  %-42s เนื้อความต่างเพราะทีมแก้เอง (ประกาศไว้แล้ว)" % skill)
        print("  %-42s   → %s" % ("", known["note"]))
    else:
        print("  %-42s เนื้อความต่างจากต้นทางโดยไม่ได้ประกาศ" % skill)
        todo.append("%s: เนื้อความต่างจากต้นทาง ให้เทียบด้วย diff ก่อนตัดสินใจ" % skill)

    # ② ช่อง description ต้องยังเป็นภาษาไทย
    fm = split_frontmatter(text)[0]
    m = re.search(r"^description:\s*(.*)$", fm, re.M)
    if not m:
        print("  %-42s   ⚠ ไม่มีช่อง description ในส่วนหัว" % "")
        todo.append("%s: ไม่มีช่อง description ในส่วนหัว ระบบจะเลือก skill นี้ไม่เจอ" % skill)
    elif not THAI.search(m.group(1)):
        print("  %-42s   ⚠ ช่อง description ไม่ใช่ภาษาไทยแล้ว" % "")
        todo.append("%s: ช่อง description กลับไปเป็นภาษาอังกฤษ ระบบจะเลือก skill นี้ไม่เจอเมื่อผู้ใช้พิมพ์ไทย" % skill)

    # ③ ไฟล์ประกอบ
    up_files = {p[len(skill) + 1:]: sha for p, sha in tree.items() if p.startswith(skill + "/")}
    lo_files = set(local_files(skill))
    allowed = tuple(known.get("extra_files", []))

    missing = sorted(set(up_files) - lo_files)
    extra = sorted(f for f in lo_files - set(up_files) if not (allowed and f.startswith(allowed)))
    changed = sorted(
        f for f in (set(up_files) & lo_files)
        if f != "SKILL.md" and git_blob_sha(os.path.join(SKILLS_DIR, skill, f)) != up_files[f]
    )

    for label, items, hint in (
        ("ไฟล์ประกอบที่ต้นทางมีแต่เราไม่มี", missing, "ให้ดึงเข้ามา"),
        ("ไฟล์ประกอบที่เรามีแต่ต้นทางไม่มีและไม่ได้ประกาศไว้", extra, "ตรวจว่าเป็นของที่ทีมเพิ่มเองหรือไม่ ถ้าใช่ให้ขึ้นทะเบียนใน KNOWN_LOCAL_EDITS"),
        ("ไฟล์ประกอบที่เนื้อหาต่างจากต้นทาง", changed, "ให้เทียบด้วย diff ก่อนตัดสินใจ"),
    ):
        if items:
            print("  %-42s   ⚠ %s: %s" % ("", label, ", ".join(items)))
            todo.append("%s: %s (%s) — %s" % (skill, label, ", ".join(items), hint))


def main():
    try:
        tree = upstream_tree()
    except UpstreamError as e:
        print("ตรวจไม่สำเร็จ: %s" % e, file=sys.stderr)
        print("ยังไม่รู้ผล ห้ามสรุปว่าของในมือตรงกับต้นทาง", file=sys.stderr)
        return 2

    names = local_skills()
    if not names:
        print("ไม่พบ skill ตระกูล netsuite- ในโฟลเดอร์ %s" % SKILLS_DIR, file=sys.stderr)
        return 2

    todo = []
    print("== เทียบ skill ที่เรามีกับต้นทาง ==")
    for name in names:
        try:
            check(name, tree, todo)
        except UpstreamError as e:
            print("ตรวจ %s ไม่สำเร็จ: %s" % (name, e), file=sys.stderr)
            return 2

    # ④ skill ชุดใหม่ที่ต้นทางเพิ่มแต่เรายังไม่มี
    # นับเป็น skill เฉพาะโฟลเดอร์ที่มี SKILL.md เท่านั้น — ต้นทางมีโฟลเดอร์อื่นปนอยู่ด้วย (เช่น scripts, test)
    up_skills = sorted({p.split("/")[0] for p in tree if p.endswith("/SKILL.md")})
    new = [s for s in up_skills if s not in names]
    print()
    print("== skill ชุดใหม่ที่ต้นทางมีแต่เรายังไม่ได้นำเข้า ==")
    if new:
        for s in new:
            print("  %s" % s)
        todo.append(
            "ต้นทางมี skill ที่เรายังไม่มี: %s — ถ้าตัดสินใจนำเข้า ต้องทำสามอย่างคู่กันเสมอ "
            "คือคัดลอกโฟลเดอร์เข้า plugins/ice-b2b-sales/skills/ · แปลช่อง description เป็นไทยพร้อมคำกระตุ้น · "
            "เพิ่มชื่อลงในแถวที่เหมาะสมของ hooks/skill-routing.yaml และลงทะเบียนความรู้ด้าน product "
            "ในไฟล์ agents/solution-knowledge-agent.md" % ", ".join(new)
        )
    else:
        print("  ไม่มี")

    print()
    if todo:
        print("สรุป: มีเรื่องต้องจัดการ %d เรื่อง" % len(todo))
        for i, t in enumerate(todo, 1):
            print("  %d. %s" % (i, t))
        print()
        print("ขั้นตอนที่ถูกต้องอยู่ในหัวไฟล์สคริปต์นี้ หัวข้อ \"เมื่อผลออกมาว่ามีเรื่องต้องจัดการ\" — ห้ามคัดลอกทับทันที")
        return 1

    print("สรุป: ตรวจ %d ตัว ไม่พบเรื่องที่ต้องจัดการ" % len(names))
    return 0


if __name__ == "__main__":
    sys.exit(main())
