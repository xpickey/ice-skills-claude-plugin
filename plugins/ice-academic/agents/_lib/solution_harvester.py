#!/usr/bin/env python3
"""
solution_harvester.py — Solution Harvest helper for portfolio-intelligence Mode 5.

Part of: iCE Cognitive Compass V02R01 Improvement Round 7 (2026.05.22)
Conforms to: CLAUDE.md V07R01 + H1-H4 anti-hallucination

Purpose:
  Extract Proposed Solution patterns from a completed opportunity folder,
  generate draft Vertical Reference Knowledge entry, save to pending-review/
  for human-in-the-loop review (Approve / Modify / Reject), then promote
  to vertical-reference-knowledge/{Vertical}/solutions/ on approval.

  Captures 4 Pattern Dimensions:
    - Process Patterns (industry-specific business process flow)
    - Application Design Patterns (module/architecture choices)
    - Approach Patterns (methodology, phasing, RACI)
    - Practice Patterns (lessons learned + anti-patterns + champion moves)

Usage (CLI):
  python3 solution_harvester.py harvest <opportunity_path>
  python3 solution_harvester.py list-pending [<vertical>]
  python3 solution_harvester.py promote <draft_path>
  python3 solution_harvester.py reject <draft_path> "<reason>"

Version: V01R01 | Date: 2026.05.22
"""

import sys
import json
from pathlib import Path
from datetime import datetime

# Shared helpers (single source of truth — see _lib/common.py).
# read_json now returns {} for a missing file and reads utf-8; every caller here
# already guards with .exists() first, so behavior is unchanged. write_json is atomic.
sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import now_iso, now_date, read_json, write_json  # noqa: E402

VKR_ROOT = Path("/Users/xpickey/Documents/Claude/Portfolio-Insights/vertical-reference-knowledge")
CUSTOMER_ROOT = Path("/Users/xpickey/Documents/Claude/Customer")


VERTICAL_MAP = {
    "BFSI-Reinsurance": ["reinsurance", "broker", "insurance broker", "bfsi"],
    "Telco": ["telecom", "telco", "carrier", "mobile network"],
    "Manufacturing": ["manufacturing", "factory", "industrial", "production"],
    "Retail": ["retail", "consumer", "wholesale", "ecommerce"],
    "Healthcare": ["healthcare", "hospital", "clinic", "pharma", "medical"],
    "Energy-Utilities": ["energy", "utility", "power", "oil", "gas"],
    "Public-Sector-TH": ["government", "ministry", "public sector", "ราชการ", "รัฐ"],
    "Logistics": ["logistics", "shipping", "freight", "supply chain"],
    "Hospitality": ["hospitality", "hotel", "resort", "tourism"],
    "Education": ["education", "university", "school", "academic"]
}


def detect_vertical(industry, profile_text=""):
    """Map industry to one of 10 verticals."""
    if not industry:
        return "Unknown"
    text = (industry + " " + profile_text).lower()
    for vertical, keywords in VERTICAL_MAP.items():
        if any(kw in text for kw in keywords):
            return vertical
    return "Unknown"


def lookup_customer_industry(customer_code):
    """Fetch industry from /Customer/_registry.json."""
    reg_file = CUSTOMER_ROOT / "_registry.json"
    if not reg_file.exists():
        return ""
    reg = read_json(reg_file)
    return reg.get("customers", {}).get(customer_code, {}).get("industry", "")


def read_opp_context(opp_path):
    """Extract structured context from opportunity folder."""
    opp_json = opp_path / "_opportunity.json"
    if not opp_json.exists():
        raise FileNotFoundError(f"_opportunity.json not at {opp_json}")
    d = read_json(opp_json)

    # Optional customer profile (cross-opp)
    profile_text = ""
    for f in sorted(opp_path.parent.glob("customer-profile_V*.md")):
        profile_text = f.read_text(encoding="utf-8")[:5000]

    # Activity log tail
    log = opp_path / "_activity.log"
    log_tail = ""
    if log.exists():
        log_tail = "\n".join(log.read_text(encoding="utf-8").splitlines()[-30:])

    # Stage artifacts
    artifacts = {}
    for sd in opp_path.iterdir():
        if sd.is_dir() and sd.name[:2].isdigit():
            files = [f.name for f in sd.iterdir() if f.is_file()]
            if files:
                artifacts[sd.name] = files

    return {
        "opp_path": str(opp_path),
        "customer_code": d.get("customer_code", "Unknown"),
        "opportunity_name": d.get("opportunity_name", "Unknown"),
        "current_phase": d.get("current_phase"),
        "current_stage": d.get("current_stage"),
        "closure": d.get("closure", {}),
        "product_solutions": d.get("product_solutions", []),
        "deal_size_thb": d.get("deal_size_thb"),
        "meddpicc": d.get("meddpicc", {}),
        "why_framework": d.get("why_framework", {}),
        "stakeholders": d.get("stakeholders", []),
        "competitors": d.get("competitors", []),
        "profile_text": profile_text,
        "artifacts": artifacts,
        "log_tail": log_tail,
    }


def build_draft(ctx, vertical):
    """Compose Vertical Reference Knowledge draft."""
    closure = ctx.get("closure", {})
    why = ctx.get("why_framework", {})
    meddpicc = ctx.get("meddpicc", {})

    sol_code = f"SOL-{ctx['customer_code']}-{ctx['opportunity_name']}".replace(" ", "_")

    # Format meddpicc
    meddpicc_lines = []
    for k, v in meddpicc.items():
        if k != "last_updated":
            meddpicc_lines.append(f"- {k}: {v}")
    meddpicc_text = "\n".join(meddpicc_lines) if meddpicc_lines else "*[Empty]*"

    # Format stakeholders
    sh = ctx.get("stakeholders", [])
    if sh:
        sh_lines = []
        for s in sh[:10]:
            if isinstance(s, dict):
                sh_lines.append(f"  - {s.get('name', '?')} | {s.get('role', '?')}")
            else:
                sh_lines.append(f"  - {s}")
        sh_text = "\n".join(sh_lines)
    else:
        sh_text = "  *[Not captured — USER FILL]*"

    # Format competitors
    comp = ctx.get("competitors", [])
    comp_text = "\n".join(f"- {c}" for c in comp) if comp else "*[Not captured]*"

    # Format artifacts
    art_lines = []
    for stage, files in sorted(ctx.get("artifacts", {}).items()):
        art_lines.append(f"  - {stage}/ ({len(files)} files)")
        for f in files[:3]:
            art_lines.append(f"    - {f}")
    art_text = "\n".join(art_lines) if art_lines else "  *[No artifacts]*"

    return f"""# {sol_code} — Vertical Reference Knowledge DRAFT

> **Status:** DRAFT — Pending User Review (Approve / Modify / Reject)
> **Vertical:** {vertical}
> **Source Opportunity:** {ctx['customer_code']}/{ctx['opportunity_name']}
> **Closure Status:** {closure.get("closure_status", "Unknown")}
> **Closure Date:** {closure.get("closure_date", "Unknown")}
> **Closure Value (THB):** {closure.get("closure_outcome_value_thb", "Unknown")}
> **Harvested:** {now_iso()}
> **Harvester:** solution_harvester.py V01R01

---

## Solution Context

- **Customer:** {ctx['customer_code']}
- **Industry / Vertical:** {vertical}
- **Product / Solution Stack:** {", ".join(ctx.get("product_solutions", [])) or "[Not specified]"}
- **Deal Size (THB):** {ctx.get("deal_size_thb", "Unknown")}
- **Phase at Harvest:** {ctx.get('current_phase')} / {ctx.get('current_stage')}

---

## 1. Process Patterns (Industry-Specific Business Process Flow)

> **DRAFT — User to review/edit**

### Why Change (Pain Driver)
{why.get("why_change", "*[Not captured — USER FILL from Discovery notes]*")}

### Why Now (Trigger)
{why.get("why_now", "*[Not captured]*")}

### Why Invest (Quantified Value)
{why.get("why_invest", "*[Not captured]*")}

### Industry-Specific Process Consideration ({vertical})
*[USER TO FILL — what makes this process unique to {vertical}?]*

---

## 2. Application Design Patterns (Modules + Architecture)

> **DRAFT — User to review/edit**

### Module Stack Proposed
- {", ".join(ctx.get("product_solutions", [])) or "[Not specified]"}

### Integration Architecture
*[USER TO FILL — API patterns, data flow, integration touch-points]*

### Customization vs Standard Decisions
*[USER TO FILL — what kept standard, what customized, why]*

### Industry-Specific Module Choices
*[USER TO FILL — what modules chosen because of {vertical}?]*

---

## 3. Approach Patterns (Methodology + Phasing)

> **DRAFT — User to review/edit**

### Implementation Methodology
*[USER TO FILL — AIM, Activate, FastTrack, iCE Methodology variant?]*

### Phasing Decision
*[USER TO FILL — Big bang vs phased? How many phases?]*

### Stakeholders Engaged
{sh_text}

### Why Us (Differentiator)
{why.get("why_us", "*[Not captured]*")}

### Industry-Specific Approach
*[USER TO FILL — what approach worked specifically for {vertical}?]*

---

## 4. Practice Patterns (Lessons + Anti-Patterns + Champion Moves)

> **DRAFT — User to review/edit**

### Lessons Learned
{closure.get("lessons_learned", "*[Not captured in closure block — USER FILL]*")}

### Why Stay (Long-Term Value)
{why.get("why_stay", "*[Not captured]*")}

### MEDDPICC Quality Signature
{meddpicc_text}

### Competitive Landscape
{comp_text}

### Champion Development Pattern
*[USER TO FILL — who was champion? what made them strong?]*

### Anti-Patterns to Avoid
*[USER TO FILL — what almost killed the deal? what to do differently?]*

---

## 5. Source Attribution

- **Opportunity Folder:** {ctx['opp_path']}
- **Activity Log Tail (last 30 entries):**

```
{ctx['log_tail'][:2000]}
```

- **Artifacts Available:**
{art_text}

---

## 6. User Review Decisions

> **Awaiting User decision — choose 1:**
>
> **(a) Approve as-is** — promote to `solutions/` folder
> **(b) Modify** — User edits inline, then promote
> **(c) Reject** — discard, log reason

### Review Notes (USER FILL after decision)

- Decision: [Approve / Modify / Reject]
- Date: [YYYY.MM.DD]
- Notes: [Why this decision]
- Edits Made (if Modify): [Summary]
- Rejection Reason (if Reject): [Why discarded]

---

*Generated by solution_harvester.py V01R01 — Solution Harvest Loop (Round 7)*
"""


def update_registry(vertical, sol_delta=0, pending_delta=0):
    """Update _registry.json counts."""
    reg_file = VKR_ROOT / "_registry.json"
    if not reg_file.exists():
        return
    reg = read_json(reg_file)
    if vertical in reg.get("verticals", {}):
        v = reg["verticals"][vertical]
        v["solution_count"] = max(0, v.get("solution_count", 0) + sol_delta)
        v["pending_count"] = max(0, v.get("pending_count", 0) + pending_delta)
        v["last_harvest"] = now_iso()
        reg["last_updated"] = now_iso()
        write_json(reg_file, reg)


def harvest(opp_path_str):
    """Harvest opportunity → draft in pending-review/."""
    opp_path = Path(opp_path_str)
    if not opp_path.exists():
        return {"error": f"Opportunity not found: {opp_path}"}

    ctx = read_opp_context(opp_path)
    industry = lookup_customer_industry(ctx["customer_code"])
    vertical = detect_vertical(industry, ctx.get("profile_text", ""))

    if vertical == "Unknown":
        return {
            "error": f"Could not detect vertical for industry='{industry}'",
            "industry": industry,
            "suggestion": "Add industry keywords to VERTICAL_MAP"
        }

    pending = VKR_ROOT / vertical / "pending-review"
    pending.mkdir(parents=True, exist_ok=True)
    sol_code = f"SOL-{ctx['customer_code']}-{ctx['opportunity_name']}".replace(" ", "_")
    draft_file = pending / f"{sol_code}_DRAFT_{now_date()}.md"
    draft_file.write_text(build_draft(ctx, vertical), encoding="utf-8")
    update_registry(vertical, pending_delta=1)

    return {
        "status": "draft_created",
        "vertical": vertical,
        "customer": ctx["customer_code"],
        "opportunity": ctx["opportunity_name"],
        "draft_path": str(draft_file),
        "draft_size_bytes": draft_file.stat().st_size,
        "next_action": "User reviews draft + decides Approve/Modify/Reject via iCE-b2b-Compass Step 1.5.C"
    }


def promote(draft_str):
    """Move draft pending-review/ → solutions/."""
    draft = Path(draft_str)
    if not draft.exists():
        return {"error": f"Draft not found: {draft}"}
    if "pending-review" not in draft.parts:
        return {"error": "Draft must be in pending-review/ folder"}

    vertical_dir = draft.parent.parent
    sol_dir = vertical_dir / "solutions"
    sol_dir.mkdir(exist_ok=True)

    new_name = draft.name.replace("_DRAFT_", "_V01R01_")
    dest = sol_dir / new_name
    if dest.exists():
        new_name = new_name.replace(".md", f"_promoted_{now_date()}.md")
        dest = sol_dir / new_name

    content = draft.read_text(encoding="utf-8")
    content = content.replace(
        "> **Status:** DRAFT — Pending User Review (Approve / Modify / Reject)",
        f"> **Status:** APPROVED — promoted from pending-review on {now_iso()}"
    )
    dest.write_text(content, encoding="utf-8")
    draft.unlink()

    update_registry(vertical_dir.name, sol_delta=1, pending_delta=-1)

    return {
        "status": "promoted",
        "vertical": vertical_dir.name,
        "from": str(draft),
        "to": str(dest)
    }


def reject(draft_str, reason):
    """Move draft → archive/ with rejection note."""
    draft = Path(draft_str)
    if not draft.exists():
        return {"error": f"Draft not found: {draft}"}

    vertical_dir = draft.parent.parent
    arch_dir = vertical_dir / "archive"
    arch_dir.mkdir(exist_ok=True)

    new_name = draft.name.replace("_DRAFT_", "_REJECTED_")
    dest = arch_dir / new_name

    content = draft.read_text(encoding="utf-8")
    content = f"""> **REJECTED:** {now_iso()}
> **Reason:** {reason}
> **Original Draft Below**

---

""" + content
    dest.write_text(content, encoding="utf-8")
    draft.unlink()
    update_registry(vertical_dir.name, pending_delta=-1)

    return {
        "status": "rejected",
        "vertical": vertical_dir.name,
        "archived_to": str(dest),
        "reason": reason
    }


def list_pending(vertical_filter=None):
    """List all pending drafts."""
    results = []
    for vd in VKR_ROOT.iterdir():
        if not vd.is_dir():
            continue
        if vertical_filter and vd.name != vertical_filter:
            continue
        pending = vd / "pending-review"
        if not pending.exists():
            continue
        for draft in pending.glob("*.md"):
            results.append({
                "vertical": vd.name,
                "draft_path": str(draft),
                "filename": draft.name,
                "size_bytes": draft.stat().st_size,
                "modified_at": datetime.fromtimestamp(draft.stat().st_mtime).strftime("%Y.%m.%dT%H:%M:%S")
            })
    return sorted(results, key=lambda r: r["modified_at"], reverse=True)


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    cmd = sys.argv[1]

    if cmd == "harvest":
        if len(sys.argv) < 3:
            print("Usage: harvest <opportunity_path>")
            sys.exit(1)
        print(json.dumps(harvest(sys.argv[2]), ensure_ascii=False, indent=2))

    elif cmd == "list-pending":
        vf = sys.argv[2] if len(sys.argv) > 2 else None
        results = list_pending(vf)
        if not results:
            print("No pending drafts" + (f" in {vf}" if vf else ""))
        else:
            print(f"Pending drafts ({len(results)}):")
            for r in results:
                print(f"  [{r['vertical']}] {r['filename']} | {r['size_bytes']}B | {r['modified_at']}")

    elif cmd == "promote":
        if len(sys.argv) < 3:
            print("Usage: promote <draft_path>")
            sys.exit(1)
        print(json.dumps(promote(sys.argv[2]), ensure_ascii=False, indent=2))

    elif cmd == "reject":
        if len(sys.argv) < 4:
            print("Usage: reject <draft_path> <reason>")
            sys.exit(1)
        print(json.dumps(reject(sys.argv[2], sys.argv[3]), ensure_ascii=False, indent=2))

    else:
        print(f"Unknown command: {cmd}")
        sys.exit(1)


if __name__ == "__main__":
    main()
