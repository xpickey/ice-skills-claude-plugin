#!/usr/bin/env python3
"""
metadata_manager.py
====================
Manages metadata files for iCE Cognitive Compass.

Part of: Phase 1 Foundation Layer (V02R01 §6.2.1, §7.2)
Conforms to: CLAUDE.md V07R01 (Date Format YYYY.MM.DD)

Managed Files:
  - _registry.json       : Master Customer/Opportunity index
  - _active-session.json : Current session lock
  - _opportunity.json    : Per-Opportunity metadata
  - _activity.log        : Append-only activity log

Usage (CLI):
  python3 metadata_manager.py registry-read
  python3 metadata_manager.py registry-add-customer <code> <full_name_th> <full_name_en> <industry> <tier>
  python3 metadata_manager.py registry-add-opportunity <customer_code> <opportunity_name>
  python3 metadata_manager.py session-read
  python3 metadata_manager.py session-set <customer> <opportunity> <phase> <process_agent>
  python3 metadata_manager.py session-clear
  python3 metadata_manager.py opportunity-read <customer> <opportunity>
  python3 metadata_manager.py opportunity-init <customer> <opportunity>
  python3 metadata_manager.py opportunity-update-stage <customer> <opportunity> <new_stage>
  python3 metadata_manager.py opportunity-update-phase <customer> <opportunity> <new_phase> <process_agent> <reason>
  python3 metadata_manager.py activity-log <customer> <opportunity> <agent> <action_type> <description>

Usage (Python import):
  from metadata_manager import (
      registry_read, registry_add_customer, registry_add_opportunity,
      session_read, session_set, session_clear,
      opportunity_read, opportunity_init, opportunity_update_stage, opportunity_update_phase,
      activity_log
  )
"""

import json
import sys
from datetime import datetime
from pathlib import Path

# Shared helpers (single source of truth — see _lib/common.py)
sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import now_iso, now_date, read_json, write_json, ISO_FMT  # noqa: E402

# === Configuration ===
CUSTOMER_ROOT = Path("/Users/xpickey/Documents/Claude/Customer")
REGISTRY_FILE = CUSTOMER_ROOT / "_registry.json"
ACTIVE_SESSION_FILE = CUSTOMER_ROOT / "_active-session.json"

# Sub-folders per Opportunity (V02R01 §7.1)
OPPORTUNITY_SUBFOLDERS = [
    "00-Customer-Profile",
    "10-RFP-Requirement",
    "20-Discovery",
    "30-Solution",
    "40-Estimation",
    "50-Proposal",
    "60-Negotiation",
    "70-Contract",
    "80-Handover",
    "90-PostSale"
]


# === Utility Functions ===
# now_iso, now_date, read_json, write_json moved to _lib/common.py (imported above).
# write_json is now atomic (tmp + os.replace) — protects the master _registry.json
# and _active-session.json from corruption on interrupted writes.


# === Registry Operations ===

def registry_read() -> dict:
    """Read master registry."""
    if not REGISTRY_FILE.exists():
        return {
            "version": "1.0",
            "schema_version": "V02R01",
            "last_updated": now_iso(),
            "customers": {}
        }
    return read_json(REGISTRY_FILE)


def registry_add_customer(code: str, full_name_th: str, full_name_en: str,
                          industry: str, tier: str) -> dict:
    """Add new customer to registry.

    Args:
        code: Customer short code (e.g., PTT, CPF)
        full_name_th: Thai legal name
        full_name_en: English legal name
        industry: Industry sector
        tier: Enterprise / Mid-market / SME / Government / SOE

    Returns:
        Updated customer entry
    """
    reg = registry_read()
    if code in reg.get("customers", {}):
        raise ValueError(f"Customer code '{code}' already exists in registry")

    reg["customers"][code] = {
        "full_name_th": full_name_th,
        "full_name_en": full_name_en,
        "industry": industry,
        "tier": tier,
        "created_at": now_iso(),
        "historical_aliases": [],
        "group_parent": None,
        "active_opportunities": [],
        "closed_opportunities": [],
        "total_value_thb": 0,
        "customer_profile_path": f"Customer/{code}/customer-profile_V01R01_{now_date()}.md"
    }
    reg["last_updated"] = now_iso()
    write_json(REGISTRY_FILE, reg)

    # V02R02 Recall Pack A — auto-create customer-level profile file
    customer_profile_init(code, full_name_th, full_name_en, industry, tier)

    return reg["customers"][code]


def customer_profile_init(code: str, full_name_th: str, full_name_en: str,
                          industry: str, tier: str) -> Path:
    """V02R02 Recall Pack A — Create customer-level profile file at /Customer/{code}/ root.

    This file persists ACROSS all opportunities for a given customer — for Customer Recall
    when a new project is opened in an existing customer.

    Per sales-admin spec V01R01 Section "Customer Profile Template" — 5 sections:
      1. Basic Identity
      2. Financial Snapshot
      3. Pain Mapping
      4. Stakeholders + Power Map
      5. Tech Stack + Architecture

    Returns the Path of the created file.
    """
    customer_folder = CUSTOMER_ROOT / code
    customer_folder.mkdir(parents=True, exist_ok=True)

    profile_file = customer_folder / f"customer-profile_V01R01_{now_date()}.md"

    if profile_file.exists():
        return profile_file  # do not overwrite existing

    template = f"""# {code} — Customer Profile

> **Version:** V01R01 | **Last Updated:** {now_date()}
> **Conforms to:** iCE Cognitive Compass V02R01 + Improvement Round 2 Recall Pack
> **Scope:** Persistent across all opportunities for this customer (Customer Recall enabler)

---

## 1. Basic Identity

- **Full Name (TH):** {full_name_th}
- **Full Name (EN):** {full_name_en}
- **Short Code:** {code}
- **Industry:** {industry}
- **Tier:** {tier}
- **Address:** [TBD — fill at first Discovery]
- **Established:** [TBD]
- **Website:** [TBD]
- **Stock Listing:** [TBD if PAE]
- **Group Parent:** [TBD if subsidiary]

## 2. Financial Snapshot (Latest FY)

- **Fiscal Year:** [TBD]
- **Total Revenue:** [TBD]
- **Net Profit:** [TBD]
- **ROE:** [TBD]
- **Auditor:** [TBD]
- **Audit Opinion:** [TBD]
- **Source:** [URL or document path]

## 3. Pain Mapping (Cross-Opportunity)

| Pain Theme | First Identified In | Status | Solution Sold |
|---|---|---|---|
| [Pain 1] | [Opportunity code] | Active / Resolved / Recurring | [Product] |

> Populated incrementally by sales-process-presale-agent during Discovery in each opportunity.

## 4. Stakeholders + Power Map (Consolidated)

| Name | Role | Department | Influence | Champion Strength | Last Engaged | Engaged In |
|---|---|---|---|---|---|---|
| [Name] | CFO | Finance | High | Strong | [date] | [opp code] |

> Consolidated across all opportunities — same person may engage in multiple deals.

## 5. Tech Stack + Architecture

### Current State (As-Is)
- **Core Systems:** [TBD]
- **Integration Pattern:** [TBD]
- **Data Platforms:** [TBD]
- **Cloud Provider:** [TBD]

### Target State (To-Be — across portfolio)
- [Project 1] → [Solution sold or proposed]
- [Project 2] → [Solution sold or proposed]

### Design Preferences Observed
- **Language Directive:** [TBD — TH primary / EN / Bilingual]
- **Font Pair (deliverables):** [TBD — e.g., Sarabun + Inter]
- **Template Preference:** [TBD — e.g., iCE-Propose / Cobalt]
- **Channel Preference:** [TBD — email / Drive / face-to-face]

---

## Past Opportunities (Auto-Updated by portfolio-intelligence Mode 4)

| Code | Status | Solution | Value | Close Date | Outcome |
|---|---|---|---|---|---|
| (none yet) | | | | | |

---

*Auto-generated by metadata_manager.customer_profile_init({code}) at {now_iso()}*
*Maintained by sales-admin-agent — R-bump on each opportunity that adds new insight*
"""
    profile_file.write_text(template, encoding="utf-8")

    # Log creation in registry
    return profile_file


def registry_add_opportunity(customer_code: str, opportunity_name: str) -> None:
    """Add opportunity to customer's active list."""
    reg = registry_read()
    if customer_code not in reg.get("customers", {}):
        raise ValueError(f"Customer '{customer_code}' not in registry")

    customer = reg["customers"][customer_code]
    if opportunity_name not in customer["active_opportunities"]:
        customer["active_opportunities"].append(opportunity_name)
    reg["last_updated"] = now_iso()
    write_json(REGISTRY_FILE, reg)


def registry_close_opportunity(customer_code: str, opportunity_name: str,
                               win_or_lost: str) -> None:
    """Move opportunity from active to closed list.

    Args:
        win_or_lost: 'Win' or 'Lost' or 'Disqualified'
    """
    reg = registry_read()
    customer = reg["customers"].get(customer_code)
    if not customer:
        raise ValueError(f"Customer '{customer_code}' not in registry")

    if opportunity_name in customer["active_opportunities"]:
        customer["active_opportunities"].remove(opportunity_name)
    closed_entry = {
        "name": opportunity_name,
        "outcome": win_or_lost,
        "closed_at": now_iso()
    }
    customer.setdefault("closed_opportunities", []).append(closed_entry)
    reg["last_updated"] = now_iso()
    write_json(REGISTRY_FILE, reg)


def registry_rebrand_customer(old_code: str, new_code: str,
                              new_full_name_th: str, new_full_name_en: str) -> None:
    """Rename customer (rebrand). Preserves history in historical_aliases."""
    reg = registry_read()
    if old_code not in reg.get("customers", {}):
        raise ValueError(f"Customer '{old_code}' not in registry")
    if new_code in reg.get("customers", {}):
        raise ValueError(f"New code '{new_code}' already exists")

    customer = reg["customers"].pop(old_code)
    customer.setdefault("historical_aliases", []).append({
        "old_code": old_code,
        "old_name_th": customer.get("full_name_th"),
        "old_name_en": customer.get("full_name_en"),
        "renamed_at": now_iso()
    })
    customer["full_name_th"] = new_full_name_th
    customer["full_name_en"] = new_full_name_en
    reg["customers"][new_code] = customer
    reg["last_updated"] = now_iso()
    write_json(REGISTRY_FILE, reg)


# === Active Session Operations ===

def session_read() -> dict:
    """Read current active session, return empty dict if no session."""
    return read_json(ACTIVE_SESSION_FILE)


def session_set(customer: str, opportunity: str, phase: str,
                process_agent: str, language_directive: str = None,
                qa_mode: str = "smart") -> dict:
    """Set active session context (Opportunity Context Lock)."""
    folder = CUSTOMER_ROOT / customer / opportunity
    if not folder.exists():
        raise FileNotFoundError(f"Opportunity folder does not exist: {folder}")

    session = {
        "session_id": now_iso().replace(":", "").replace(".", "").replace("T", "-")[:18],
        "started_at": now_iso(),
        "mode": "opportunity",
        "active_customer": customer,
        "active_opportunity": opportunity,
        "active_phase": phase,
        "active_process_agent": process_agent,
        "active_folder": str(folder.resolve()),
        "language_directive": {
            "type": language_directive or "ask_user",
            "set_at": now_iso(),
            "applies_to": "session_default"
        },
        "qa_mode": qa_mode,
        "locked_at": now_iso()
    }
    write_json(ACTIVE_SESSION_FILE, session)
    return session


def session_clear() -> None:
    """Clear active session (used when User exits or switches Opportunity)."""
    if ACTIVE_SESSION_FILE.exists():
        ACTIVE_SESSION_FILE.unlink()


def session_update_language(language_directive: str) -> dict:
    """Update language directive mid-session."""
    session = session_read()
    if not session:
        raise ValueError("No active session to update")
    session["language_directive"] = {
        "type": language_directive,
        "set_at": now_iso(),
        "applies_to": "session_default"
    }
    write_json(ACTIVE_SESSION_FILE, session)
    return session


# === Opportunity Operations ===

def opportunity_path(customer: str, opportunity: str) -> Path:
    return CUSTOMER_ROOT / customer / opportunity


def opportunity_file(customer: str, opportunity: str) -> Path:
    return opportunity_path(customer, opportunity) / "_opportunity.json"


def opportunity_init(customer: str, opportunity: str,
                     product_solutions: list = None,
                     created_at: str = None) -> dict:
    """Initialize new opportunity with default metadata + create 10 sub-folders.

    Returns the initialized _opportunity.json content.
    """
    opp_folder = opportunity_path(customer, opportunity)
    opp_folder.mkdir(parents=True, exist_ok=True)

    # Create 10 sub-folders (V02R01 §7.1)
    for sub in OPPORTUNITY_SUBFOLDERS:
        (opp_folder / sub).mkdir(exist_ok=True)

    # Initialize empty _activity.log
    (opp_folder / "_activity.log").touch()

    # Initialize _opportunity.json
    opp_data = {
        "customer_code": customer,
        "opportunity_name": opportunity,
        "created_at": created_at or now_date(),
        "current_phase": "Pre-Sale",
        "current_stage": "Prospect",
        "customer_journey_state": "Prospect",
        "active_process_agent": "sales-process-presale-agent",
        "phase_history": [
            {
                "phase": "Pre-Sale",
                "active_process_agent": "sales-process-presale-agent",
                "entered_at": now_iso(),
                "exited_at": None,
                "duration_days": None,
                "transition_reason": "Initial creation",
                "key_milestones": []
            }
        ],
        "stage_history": [
            {
                "stage": "Prospect",
                "entered_at": now_iso(),
                "exited_at": None
            }
        ],
        "product_solutions": product_solutions or [],
        "deal_size_thb": 0,
        "probability_pct": 0,
        "expected_close_date": None,
        "meddpicc": {
            "metrics": None,
            "economic_buyer": None,
            "decision_criteria": None,
            "decision_process": None,
            "paper_process": None,
            "identify_pain": None,
            "champion": None,
            "competition": None,
            "overall_score": 0,
            "last_updated": now_iso()
        },
        "why_framework": {
            "why_change": None,
            "why_now": None,
            "why_invest": None,
            "why_us": None,
            "why_stay": None
        },
        "stakeholders": [],
        "competitors": [],
        "customer_email_domains": [],
        "bulk_send_threshold": 5,
        "closure": {
            "closure_status": "Unknown",
            "closure_date": None,
            "closure_reason": None,
            "closure_outcome_value_thb": None,
            "lessons_learned": None,
            "last_closure_update": None
        },
        "owner": "xpickey",
        "last_activity_at": now_iso()
    }
    write_json(opportunity_file(customer, opportunity), opp_data)

    # Update registry
    registry_add_opportunity(customer, opportunity)

    # Log creation
    activity_log(customer, opportunity, "metadata_manager", "create_opportunity",
                 f"Initialized opportunity {customer}/{opportunity}")
    return opp_data


def opportunity_read(customer: str, opportunity: str) -> dict:
    """Read _opportunity.json content."""
    path = opportunity_file(customer, opportunity)
    if not path.exists():
        raise FileNotFoundError(f"Opportunity metadata not found: {path}")
    return read_json(path)


def opportunity_update_stage(customer: str, opportunity: str,
                             new_stage: str) -> dict:
    """Update current stage (Stage transition within Phase).
    Requires user confirmation per Q7 — caller must verify before calling.
    """
    data = opportunity_read(customer, opportunity)
    old_stage = data.get("current_stage")
    if old_stage == new_stage:
        return data

    # Close current stage in stage_history
    for entry in reversed(data["stage_history"]):
        if entry.get("exited_at") is None:
            entry["exited_at"] = now_iso()
            break

    # Add new stage entry
    data["stage_history"].append({
        "stage": new_stage,
        "entered_at": now_iso(),
        "exited_at": None
    })
    data["current_stage"] = new_stage
    data["last_activity_at"] = now_iso()
    write_json(opportunity_file(customer, opportunity), data)

    activity_log(customer, opportunity, "metadata_manager", "stage_transition",
                 f"Stage: {old_stage} -> {new_stage}")
    return data


def opportunity_update_phase(customer: str, opportunity: str,
                             new_phase: str, new_process_agent: str,
                             transition_reason: str = "User confirmed",
                             key_milestones: list = None) -> dict:
    """Update current phase (Phase transition — major boundary).
    Requires user confirmation per Q8 — caller must verify before calling.
    """
    data = opportunity_read(customer, opportunity)
    old_phase = data.get("current_phase")
    if old_phase == new_phase:
        return data

    # Close current phase in phase_history
    for entry in reversed(data["phase_history"]):
        if entry.get("exited_at") is None:
            entry["exited_at"] = now_iso()
            entered = datetime.strptime(entry["entered_at"], ISO_FMT)
            exited = datetime.now()
            entry["duration_days"] = (exited - entered).days
            break

    # Add new phase entry
    data["phase_history"].append({
        "phase": new_phase,
        "active_process_agent": new_process_agent,
        "entered_at": now_iso(),
        "exited_at": None,
        "duration_days": None,
        "transition_reason": transition_reason,
        "key_milestones": key_milestones or []
    })
    data["current_phase"] = new_phase
    data["active_process_agent"] = new_process_agent
    data["customer_journey_state"] = new_phase
    data["last_activity_at"] = now_iso()
    write_json(opportunity_file(customer, opportunity), data)

    activity_log(customer, opportunity, "metadata_manager", "phase_transition",
                 f"Phase: {old_phase} -> {new_phase} (Reason: {transition_reason})")
    return data


def opportunity_update_closure(customer: str, opportunity: str,
                                closure_status: str,
                                closure_date: str = None,
                                closure_reason: str = None,
                                closure_outcome_value_thb: float = None,
                                lessons_learned: str = None) -> dict:
    """V02R02 Recall Enhancement — Update closure metadata for past opportunity.

    Used when iCE-b2b-Compass collects User answers on ambiguous past opportunities
    detected by portfolio-intelligence Mode 4 Customer Recall.

    Args:
        closure_status: Won / Lost / Stalled / Unknown / Active / Churned / Renewed / Withdrawn
        closure_date: YYYY.MM.DD (when deal actually closed or last meaningful activity)
        closure_reason: Free text — why deal ended as it did
        closure_outcome_value_thb: Final realized value (for Won) or potential lost value (for Lost)
        lessons_learned: Free text — what to remember for future deals (anti-pattern fuel)

    Returns:
        Updated _opportunity.json content
    """
    VALID_STATUS = ["Won", "Lost", "Stalled", "Unknown", "Active",
                    "Churned", "Renewed", "Withdrawn"]
    if closure_status not in VALID_STATUS:
        raise ValueError(f"closure_status must be one of {VALID_STATUS}, got '{closure_status}'")

    data = opportunity_read(customer, opportunity)
    if "closure" not in data:
        data["closure"] = {}

    data["closure"]["closure_status"] = closure_status
    if closure_date is not None:
        data["closure"]["closure_date"] = closure_date
    if closure_reason is not None:
        data["closure"]["closure_reason"] = closure_reason
    if closure_outcome_value_thb is not None:
        data["closure"]["closure_outcome_value_thb"] = closure_outcome_value_thb
    if lessons_learned is not None:
        data["closure"]["lessons_learned"] = lessons_learned
    data["closure"]["last_closure_update"] = now_iso()
    data["last_activity_at"] = now_iso()

    write_json(opportunity_file(customer, opportunity), data)

    activity_log(customer, opportunity, "metadata_manager",
                 "closure_update",
                 f"Closure status: {closure_status}, date: {closure_date}, reason: {closure_reason}")
    return data


def opportunity_detect_ambiguity(customer: str, opportunity: str) -> dict:
    """V02R02 Recall Enhancement — Detect if past opportunity has ambiguous closure status.

    Used by portfolio-intelligence Mode 4 Customer Recall to identify which past opps
    need User clarification.

    Returns:
        {
            "is_ambiguous": bool,
            "ambiguity_reasons": list of strings,
            "questions_for_user": list of structured questions
        }
    """
    data = opportunity_read(customer, opportunity)
    closure = data.get("closure", {})
    closure_status = closure.get("closure_status", "Unknown")
    closure_date = closure.get("closure_date")
    closure_reason = closure.get("closure_reason")

    current_phase = data.get("current_phase", "Unknown")
    current_stage = data.get("current_stage", "Unknown")

    ambiguity_reasons = []
    questions = []

    # Rule 1: closure_status explicitly Unknown
    if closure_status == "Unknown":
        ambiguity_reasons.append("closure_status is 'Unknown' — never set by anyone")
        questions.append({
            "field": "closure_status",
            "question": f"Opportunity {opportunity} จบลงอย่างไรครับ?",
            "options": [
                "Won (Closed-Won)",
                "Lost (Closed-Lost)",
                "Stalled (active แต่ไม่มี movement)",
                "Active (ยังดำเนินอยู่)",
                "Churned (Customer ยกเลิกหลัง Win)",
                "Renewed (Customer renew หลัง Win)",
                "Withdrawn (ถอนข้อเสนอ)",
            ]
        })

    # Rule 2: Phase=Customer but no closure_status set
    if current_phase == "Customer" and closure_status == "Unknown":
        ambiguity_reasons.append(f"current_phase is 'Customer' but closure_status not set")

    # Rule 3: Stage indicates close-related but no closure date
    if any(kw in current_stage.lower() for kw in ["won", "lost", "close"]) and not closure_date:
        ambiguity_reasons.append(f"current_stage '{current_stage}' suggests close but closure_date missing")
        questions.append({
            "field": "closure_date",
            "question": f"Opportunity {opportunity} ปิดเมื่อวันที่ไหนครับ? (YYYY.MM.DD)",
            "options": None
        })

    # Rule 4: No closure_reason for Won/Lost
    if closure_status in ("Won", "Lost") and not closure_reason:
        ambiguity_reasons.append(f"closure_status is '{closure_status}' but closure_reason missing")
        questions.append({
            "field": "closure_reason",
            "question": f"Opportunity {opportunity} — ทำไม {closure_status}? (สำคัญมากเพื่อ Learning Loop)",
            "options": None
        })

    # Rule 5: stage_history shows long inactivity (heuristic — check last_activity_at)
    # If last_activity_at > 90 days ago and not in Customer Phase, flag as Stalled?
    # (placeholder — heuristic check can be enhanced later)

    return {
        "is_ambiguous": len(ambiguity_reasons) > 0,
        "ambiguity_reasons": ambiguity_reasons,
        "questions_for_user": questions
    }


def opportunity_update_meddpicc(customer: str, opportunity: str,
                                meddpicc_update: dict) -> dict:
    """Update MEDDPICC scores. Caller must verify with User first (Q19 Hybrid)."""
    data = opportunity_read(customer, opportunity)
    data["meddpicc"].update(meddpicc_update)
    data["meddpicc"]["last_updated"] = now_iso()
    data["last_activity_at"] = now_iso()
    write_json(opportunity_file(customer, opportunity), data)

    activity_log(customer, opportunity, "metadata_manager", "meddpicc_update",
                 f"MEDDPICC updated: {list(meddpicc_update.keys())}")
    return data


# === Activity Log Operations ===

def activity_log(customer: str, opportunity: str, agent: str,
                 action_type: str, description: str) -> None:
    """Append entry to _activity.log (Q17 — Full log all actions, Q18 — keep forever)."""
    log_file = opportunity_path(customer, opportunity) / "_activity.log"
    log_file.parent.mkdir(parents=True, exist_ok=True)
    entry = f"{now_iso()} | {agent} | {action_type} | {description}\n"
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(entry)


# === CLI Entry Point ===

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 metadata_manager.py <command> [args...]", file=sys.stderr)
        sys.exit(1)

    cmd = sys.argv[1]
    args = sys.argv[2:]

    try:
        if cmd == "registry-read":
            print(json.dumps(registry_read(), ensure_ascii=False, indent=2))

        elif cmd == "registry-add-customer":
            if len(args) != 5:
                raise ValueError("Args: <code> <name_th> <name_en> <industry> <tier>")
            result = registry_add_customer(*args)
            print(json.dumps(result, ensure_ascii=False, indent=2))

        elif cmd == "registry-add-opportunity":
            if len(args) != 2:
                raise ValueError("Args: <customer_code> <opportunity_name>")
            registry_add_opportunity(*args)
            print("OK")

        elif cmd == "customer-profile-init":
            if len(args) != 5:
                raise ValueError("Args: <code> <name_th> <name_en> <industry> <tier>")
            path = customer_profile_init(*args)
            print(f"OK: {path}")

        elif cmd == "session-read":
            print(json.dumps(session_read(), ensure_ascii=False, indent=2))

        elif cmd == "session-set":
            if len(args) < 4:
                raise ValueError("Args: <customer> <opportunity> <phase> <process_agent> [language_directive] [qa_mode]")
            result = session_set(*args[:4],
                                 language_directive=args[4] if len(args) > 4 else None,
                                 qa_mode=args[5] if len(args) > 5 else "smart")
            print(json.dumps(result, ensure_ascii=False, indent=2))

        elif cmd == "session-clear":
            session_clear()
            print("OK")

        elif cmd == "opportunity-read":
            if len(args) != 2:
                raise ValueError("Args: <customer> <opportunity>")
            print(json.dumps(opportunity_read(*args), ensure_ascii=False, indent=2))

        elif cmd == "opportunity-init":
            if len(args) < 2:
                raise ValueError("Args: <customer> <opportunity>")
            result = opportunity_init(*args[:2])
            print(json.dumps(result, ensure_ascii=False, indent=2))

        elif cmd == "opportunity-update-stage":
            if len(args) != 3:
                raise ValueError("Args: <customer> <opportunity> <new_stage>")
            print(json.dumps(opportunity_update_stage(*args), ensure_ascii=False, indent=2))

        elif cmd == "opportunity-update-phase":
            if len(args) < 4:
                raise ValueError("Args: <customer> <opportunity> <new_phase> <process_agent> [reason]")
            print(json.dumps(
                opportunity_update_phase(*args[:4],
                                          transition_reason=args[4] if len(args) > 4 else "User confirmed"),
                ensure_ascii=False, indent=2))

        elif cmd == "activity-log":
            if len(args) != 5:
                raise ValueError("Args: <customer> <opportunity> <agent> <action_type> <description>")
            activity_log(*args)
            print("OK")

        elif cmd == "closure-update":
            # V02R02 Recall Enhancement
            if len(args) < 3:
                raise ValueError("Args: <customer> <opportunity> <closure_status> [date] [reason] [value_thb] [lessons]")
            customer = args[0]
            opportunity = args[1]
            closure_status = args[2]
            closure_date = args[3] if len(args) > 3 and args[3] != "-" else None
            closure_reason = args[4] if len(args) > 4 and args[4] != "-" else None
            closure_value = float(args[5]) if len(args) > 5 and args[5] != "-" else None
            lessons = args[6] if len(args) > 6 and args[6] != "-" else None
            result = opportunity_update_closure(customer, opportunity, closure_status,
                                                closure_date, closure_reason,
                                                closure_value, lessons)
            print(json.dumps(result.get("closure", {}), ensure_ascii=False, indent=2))

        elif cmd == "closure-detect-ambiguity":
            # V02R02 Recall Enhancement
            if len(args) != 2:
                raise ValueError("Args: <customer> <opportunity>")
            result = opportunity_detect_ambiguity(*args)
            print(json.dumps(result, ensure_ascii=False, indent=2))

        else:
            print(f"Unknown command: {cmd}", file=sys.stderr)
            sys.exit(1)

    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
