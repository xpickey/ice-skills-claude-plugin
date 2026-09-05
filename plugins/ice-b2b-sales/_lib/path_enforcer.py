#!/usr/bin/env python3
"""
path_enforcer.py
=================
Path security enforcement for iCE Cognitive Compass.

Part of: Phase 1 Foundation Layer (V02R01 §10.1 Anti-Cross-Contamination, §12.8 Security Checkpoints)
Conforms to: CLAUDE.md V07R01

Purpose:
  ป้องกัน Agent เขียนเอกสาร/file ออกนอก `active_opportunity_folder`
  ตามข้อกำหนด Q25 (Block + Alert + Log)

Security Rules:
  1. ต้องระบุ requesting_agent_id + active_opportunity_folder ทุกครั้ง
  2. Target path ต้องอยู่ภายใน active_opportunity_folder (sub-folder อนุญาต)
  3. Path traversal (../) — REJECT
  4. Absolute path นอก scope — REJECT
  5. ทุก violation ต้อง log

Usage (CLI):
  python3 path_enforcer.py validate <target_path> <active_folder> <requesting_agent>
  python3 path_enforcer.py check-write <target_path> <active_folder> <requesting_agent>

Usage (Python import):
  from path_enforcer import validate_path, check_write_allowed, PathEnforcementError
"""

import sys
from pathlib import Path

# Shared helpers (single source of truth — see _lib/common.py)
sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import now_iso  # noqa: E402


# === Configuration ===
CUSTOMER_ROOT = Path("/Users/xpickey/Documents/Claude/Customer")
GLOBAL_LOG_FILE = CUSTOMER_ROOT / "_security-violations.log"

# Allowed root paths for writes (sales-admin scope)
ALLOWED_ROOTS = [
    CUSTOMER_ROOT,
]


# === Exception ===

class PathEnforcementError(Exception):
    """Raised when path validation fails."""
    pass


# === Utility ===
# now_iso moved to _lib/common.py (imported above).


def resolve_safe(path_str: str) -> Path:
    """Resolve path safely. Reject path traversal."""
    if ".." in Path(path_str).parts:
        raise PathEnforcementError(f"Path traversal detected: {path_str}")
    return Path(path_str).expanduser().resolve()


def is_subpath(target: Path, parent: Path) -> bool:
    """Check if target is inside parent (after resolve)."""
    try:
        target.relative_to(parent)
        return True
    except ValueError:
        return False


# === Core Enforcement ===

def validate_path(target_path: str, active_folder: str,
                  requesting_agent: str) -> dict:
    """Validate target path is safe to write.

    Args:
        target_path: The path Agent wants to write
        active_folder: Current locked Opportunity folder
        requesting_agent: Agent name requesting the operation

    Returns:
        dict with keys:
          - allowed (bool)
          - reason (str)
          - resolved_target (str)
          - active_folder (str)
          - requesting_agent (str)

    Raises:
        PathEnforcementError on any violation (Q25 — Block + Alert + Log)
    """
    if not requesting_agent or requesting_agent.strip() == "":
        _log_violation("MISSING_AGENT_ID", target_path, active_folder, "unknown")
        raise PathEnforcementError(
            "requesting_agent must be specified (V02R01 §4.3 Universal Access rule)"
        )

    if not active_folder or active_folder.strip() == "":
        _log_violation("MISSING_ACTIVE_FOLDER", target_path, "none", requesting_agent)
        raise PathEnforcementError(
            "active_folder must be specified — no active Opportunity context"
        )

    # Resolve paths safely
    try:
        target = resolve_safe(target_path)
        active = resolve_safe(active_folder)
    except PathEnforcementError as e:
        _log_violation("PATH_TRAVERSAL", target_path, active_folder, requesting_agent)
        raise

    # Check target is inside active_folder
    if not is_subpath(target, active):
        # Check if target is in another allowed root (e.g., Customer root for metadata ops)
        within_allowed_root = any(is_subpath(target, root) for root in ALLOWED_ROOTS)

        # Special exemption: writes to _registry.json or _active-session.json
        # at Customer root are allowed (metadata manager operations)
        is_metadata_op = (
            target.parent == CUSTOMER_ROOT and
            target.name in ("_registry.json", "_active-session.json")
        )

        if not is_metadata_op:
            _log_violation(
                "OUT_OF_SCOPE",
                str(target),
                str(active),
                requesting_agent
            )
            raise PathEnforcementError(
                f"Target path '{target}' is NOT inside active_folder '{active}'. "
                f"Agent '{requesting_agent}' blocked from writing outside Opportunity scope."
            )

    return {
        "allowed": True,
        "reason": "Path within active_opportunity_folder",
        "resolved_target": str(target),
        "active_folder": str(active),
        "requesting_agent": requesting_agent,
        "validated_at": now_iso()
    }


def check_write_allowed(target_path: str, active_folder: str,
                        requesting_agent: str) -> bool:
    """Non-raising variant — returns True/False instead of exception."""
    try:
        validate_path(target_path, active_folder, requesting_agent)
        return True
    except PathEnforcementError:
        return False


# === Violation Logging ===

def _log_violation(violation_type: str, target: str, active: str,
                   agent: str) -> None:
    """Append violation entry to global security log."""
    GLOBAL_LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    entry = (
        f"{now_iso()} | VIOLATION | {violation_type} | "
        f"agent={agent} | target={target} | active={active}\n"
    )
    with open(GLOBAL_LOG_FILE, "a", encoding="utf-8") as f:
        f.write(entry)


# === CLI Entry Point ===

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 path_enforcer.py <command> [args...]", file=sys.stderr)
        print("Commands: validate | check-write", file=sys.stderr)
        sys.exit(1)

    cmd = sys.argv[1]
    args = sys.argv[2:]

    try:
        if cmd == "validate":
            if len(args) != 3:
                raise ValueError("Args: <target_path> <active_folder> <requesting_agent>")
            result = validate_path(*args)
            print(f"ALLOWED: {result['resolved_target']}")
            sys.exit(0)

        elif cmd == "check-write":
            if len(args) != 3:
                raise ValueError("Args: <target_path> <active_folder> <requesting_agent>")
            allowed = check_write_allowed(*args)
            print("ALLOWED" if allowed else "BLOCKED")
            sys.exit(0 if allowed else 1)

        else:
            print(f"Unknown command: {cmd}", file=sys.stderr)
            sys.exit(1)

    except PathEnforcementError as e:
        print(f"BLOCKED: {e}", file=sys.stderr)
        sys.exit(2)

    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
