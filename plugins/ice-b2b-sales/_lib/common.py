"""
common.py — Shared utilities for iCE Cognitive Compass.Next _lib helpers.

Single source of truth for timestamp formatting and JSON I/O, consolidating
copies that previously lived (and silently diverged) across metadata_manager.py,
solution_harvester.py, knowledge_sync.py, and path_enforcer.py.

Design decisions (best-of-all-prior-versions):
  - write_json/write_json_atomic: atomic (tmp + os.replace) AND mkdir parent AND utf-8.
    The registry/session files are the master index of the whole fleet; a non-atomic
    write that is interrupted mid-flush would corrupt them. The atomic pattern already
    existed in solution_harvester/knowledge_sync; it is now the default everywhere.
  - read_json: returns {} for a missing file (every caller already guards with
    .exists(), verified 2026.06.08) and always reads utf-8 for Thai content.

V01R01 | 2026.06.08
"""

import json
import os
from datetime import datetime
from pathlib import Path

# Canonical date/time formats (CLAUDE.md V07R02 — YYYY.MM.DD)
ISO_FMT = "%Y.%m.%dT%H:%M:%S"
DATE_FMT = "%Y.%m.%d"


def now_iso() -> str:
    """Return current timestamp in YYYY.MM.DDTHH:MM:SS format."""
    return datetime.now().strftime(ISO_FMT)


def now_date() -> str:
    """Return current date in YYYY.MM.DD format."""
    return datetime.now().strftime(DATE_FMT)


def read_json(path) -> dict:
    """Read a JSON file as utf-8. Return {} if the file does not exist.

    All callers guard with .exists() before relying on contents, so returning {}
    for a missing file is safe and avoids a FileNotFoundError surprise.
    """
    path = Path(path)
    if not path.exists():
        return {}
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def write_json(path, data) -> None:
    """Atomically write `data` as pretty utf-8 JSON, creating parent dirs.

    Writes to a temp file in the same directory then os.replace()s it into place,
    so a crash mid-write never leaves a half-written (corrupt) destination file.
    """
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    os.replace(tmp, path)
