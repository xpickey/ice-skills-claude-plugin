#!/usr/bin/env python3
"""
deploy_fleet.py — iCE Fleet Deploy Pipeline (V01R01 | 2026.07.10)

ทำซ้ำขั้นตอน STEP 12 ของ Fleet Rewrite V2 ให้เป็นคำสั่งเดียว:
  sync (active → marketplace) → bump versions → git commit → push (ถามยืนยัน) →
  claude plugin update → checksum (cache vs active — ปิด version drift)

ใช้อย่างไร (รันจากที่ไหนก็ได้):
  python3 ~/.claude/plugins/marketplaces/ice-skills/scripts/deploy_fleet.py --check
      # dry-run: โชว์ว่าไฟล์ไหน active ต่างจาก marketplace (ยังไม่แตะอะไร)
  python3 .../deploy_fleet.py --sync
      # copy active → marketplace (ยังไม่ commit — ดู git diff เองได้)
  python3 .../deploy_fleet.py --sync --bump tools=1.6.1,b2b=1.3.1,academic=1.4.1
      # sync + ตั้ง version ใหม่ใน plugin.json
  python3 .../deploy_fleet.py --deploy
      # commit ทุกอย่างที่ค้าง + push (ถาม y/N ก่อน) + plugin update + checksum
  python3 .../deploy_fleet.py --all --bump tools=1.6.1,b2b=1.3.1,academic=1.4.1
      # ครบวงจร: check → sync → bump → deploy
  python3 .../deploy_fleet.py --checksum
      # เทียบ cache กับ active อย่างเดียว (ตรวจ drift)

หมายเหตุ: หลัง deploy ต้อง restart Claude (Code/Desktop/CLI) เพื่อโหลด plugin ใหม่
กติกาความปลอดภัย: ไม่ force-push · marketplace มี uncommitted อื่นอยู่ → เตือนก่อน sync ·
push ต้องพิมพ์ y ยืนยันเสมอ (external action)
"""
import argparse, filecmp, json, shutil, subprocess, sys
from pathlib import Path

HOME = Path.home()
A = HOME / ".claude/agents"                                    # active agents
S = HOME / ".claude/skills"                                    # active skills
M = HOME / ".claude/plugins/marketplaces/ice-skills"           # marketplace repo
C = HOME / ".claude/plugins/cache/ice-skills"                  # plugin cache

# ---- แผนที่ไฟล์: active → ตำแหน่งใน marketplace (ตาม Fleet Rewrite V2 2026.07.10) ----
B2B_AGENTS = ["iCE-Compass-Next.md", "kim-assistant.md", "sales-process-agent.md",
              "solution-knowledge-agent.md", "deliverable-gen-agent.md", "qa-master-agent.md"]
B2B_REFS   = ["loop-engineering.md", "compass-changelog.md", "team-memory.md", "fleet-changelog.md"]
ACA_AGENTS = ["thesis-ai-det-col-agent.md"]
ACA_REFS   = ["team-memory.md", "fleet-changelog.md"]
TOOL_AGENTS = ["codex-bridge-agent.md", "openrouter-agent.md"]
CB = "claude-codex-bridge"
CB_FILES = ["SKILL.md", "scripts/ask-codex.sh",
            "references/01_codex_cli_reference.md", "references/02_protocol.md",
            "references/03_antiAI_handoff.md", "references/04_presets.md",
            "references/05_review_contract.md", "references/verdict.schema.json"]

def file_map():
    """คืน list ของ (active_path, marketplace_path) ทุกคู่"""
    pairs = []
    for f in B2B_AGENTS: pairs.append((A / f, M / "plugins/ice-b2b-sales/agents" / f))
    for f in B2B_REFS:   pairs.append((A / "reference" / f, M / "plugins/ice-b2b-sales/agents/reference" / f))
    for f in ACA_AGENTS: pairs.append((A / f, M / "plugins/ice-academic/agents" / f))
    for f in ACA_REFS:   pairs.append((A / "reference" / f, M / "plugins/ice-academic/agents/reference" / f))
    for f in TOOL_AGENTS: pairs.append((A / f, M / "plugins/ice-tools/agents" / f))
    for f in CB_FILES:   pairs.append((S / CB / f, M / "plugins/ice-tools/skills" / CB / f))
    pairs.append((S / "openrouter-bridge/SKILL.md", M / "plugins/ice-tools/skills/openrouter-bridge/SKILL.md"))
    return pairs

PLUGIN_KEYS = {"tools": "ice-tools", "b2b": "ice-b2b-sales", "academic": "ice-academic"}

def run(cmd, **kw):
    print(f"  $ {' '.join(cmd)}")
    return subprocess.run(cmd, **kw)

def cmd_check():
    """dry-run: ไฟล์ไหน active ต่างจาก marketplace"""
    diff, missing, same = [], [], 0
    for src, dst in file_map():
        if not src.exists(): missing.append(str(src)); continue
        if dst.exists() and filecmp.cmp(src, dst, shallow=False): same += 1
        else: diff.append((src, dst))
    print(f"\n== CHECK: เหมือนกัน {same} · ต่าง/ยังไม่มี {len(diff)} · active หาย {len(missing)} ==")
    for src, dst in diff: print(f"  ≠ {dst.relative_to(M)}")
    for m in missing: print(f"  ⚠ active ไม่มีไฟล์: {m}")
    return diff

def cmd_sync():
    st = subprocess.run(["git", "-C", str(M), "status", "--short"], capture_output=True, text=True)
    if st.stdout.strip():
        print("⚠ marketplace repo มีของค้างอยู่ก่อนแล้ว:\n" + st.stdout)
        if input("ทำต่อไหม? [y/N] ").strip().lower() != "y": sys.exit(1)
    n = 0
    for src, dst in file_map():
        if not src.exists(): print(f"  ⚠ ข้าม (active ไม่มี): {src}"); continue
        dst.parent.mkdir(parents=True, exist_ok=True)
        if not dst.exists() or not filecmp.cmp(src, dst, shallow=False):
            shutil.copy2(src, dst); print(f"  → {dst.relative_to(M)}"); n += 1
    print(f"== SYNC: copy {n} ไฟล์ ==")

def cmd_bump(spec):
    """spec เช่น tools=1.6.1,b2b=1.3.1,academic=1.4.1 — ตั้ง version (description ไม่แตะ — แก้เองถ้าต้องการ)"""
    for part in spec.split(","):
        key, ver = part.split("=")
        plugin = PLUGIN_KEYS[key.strip()]
        pj = M / "plugins" / plugin / ".claude-plugin/plugin.json"
        d = json.loads(pj.read_text())
        old = d["version"]; d["version"] = ver.strip()
        pj.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n")
        print(f"  {plugin}: {old} → {ver.strip()}")

def current_versions():
    out = {}
    for key, plugin in PLUGIN_KEYS.items():
        pj = M / "plugins" / plugin / ".claude-plugin/plugin.json"
        out[plugin] = json.loads(pj.read_text())["version"]
    return out

def cmd_deploy():
    vers = current_versions()
    msg = (f"Deploy iCE skill update (ice-academic {vers['ice-academic']}, "
           f"ice-b2b-sales {vers['ice-b2b-sales']}, ice-tools {vers['ice-tools']})")
    run(["git", "-C", str(M), "add", "-A"])
    st = subprocess.run(["git", "-C", str(M), "status", "--short"], capture_output=True, text=True)
    if not st.stdout.strip():
        print("== ไม่มีอะไรใหม่ให้ commit — ข้ามไป plugin update + checksum ==")
    else:
        print(st.stdout)
        run(["git", "-C", str(M), "commit", "-m", msg])
    # push — ถามยืนยันเสมอ (external action)
    if input(f"\nPush ขึ้น GitHub เลยไหม? ({msg}) [y/N] ").strip().lower() == "y":
        run(["git", "-C", str(M), "fetch", "origin"])
        behind = subprocess.run(["git", "-C", str(M), "log", "--oneline", "HEAD..origin/main"],
                                capture_output=True, text=True).stdout.strip()
        if behind:
            print(f"⚠ remote มี commit ใหม่กว่า:\n{behind}\n→ รัน git rebase origin/main แก้ conflict เองก่อน แล้วรัน --deploy ใหม่")
            sys.exit(1)
        r = run(["git", "-C", str(M), "push"])
        if r.returncode != 0: print("❌ push ล้มเหลว — ดูข้อความข้างบน"); sys.exit(1)
        print("✅ pushed")
    else:
        print("(ยังไม่ push — commit อยู่ local · รัน --deploy อีกครั้งเมื่อพร้อม)")
    # plugin update ทั้ง 3 + checksum
    run(["claude", "plugin", "marketplace", "update", "ice-skills"])
    for plugin in PLUGIN_KEYS.values():
        run(["claude", "plugin", "update", f"{plugin}@ice-skills"])
    cmd_checksum()
    print("\n📌 อย่าลืม restart Claude (Code/Desktop/CLI) เพื่อโหลด plugin ใหม่")

def cmd_checksum():
    vers = current_versions()
    plugin_of = lambda dst: dst.relative_to(M / "plugins").parts[0]
    ok, drift = 0, []
    for src, dst in file_map():
        plugin = plugin_of(dst)
        rel = Path(*dst.relative_to(M / "plugins" / plugin).parts)
        cache_file = C / plugin / vers[plugin] / rel
        if src.exists() and cache_file.exists() and filecmp.cmp(src, cache_file, shallow=False): ok += 1
        else: drift.append(str(cache_file))
    print(f"\n== CHECKSUM (cache {vers} vs active): identical {ok} · drift {len(drift)} ==")
    for d in drift: print(f"  ❌ {d}")
    if not drift: print("  ✅ version drift = 0")

if __name__ == "__main__":
    p = argparse.ArgumentParser(description="iCE Fleet Deploy Pipeline")
    p.add_argument("--check", action="store_true", help="dry-run เทียบ active vs marketplace")
    p.add_argument("--sync", action="store_true", help="copy active → marketplace")
    p.add_argument("--bump", metavar="tools=X,b2b=Y,academic=Z", help="ตั้ง version ใน plugin.json")
    p.add_argument("--deploy", action="store_true", help="commit + push(ถาม) + plugin update + checksum")
    p.add_argument("--checksum", action="store_true", help="เทียบ cache vs active อย่างเดียว")
    p.add_argument("--all", action="store_true", help="check → sync → (bump) → deploy")
    a = p.parse_args()
    if not any([a.check, a.sync, a.bump, a.deploy, a.checksum, a.all]): p.print_help(); sys.exit(0)
    if a.check or a.all: cmd_check()
    if a.sync or a.all: cmd_sync()
    if a.bump: cmd_bump(a.bump)
    if a.deploy or a.all: cmd_deploy()
    elif a.checksum: cmd_checksum()
