#!/usr/bin/env python3
"""
knowledge_sync.py
==================
Document Sync Hook helper for iCE Cognitive Compass.

Part of: V02R01 Improvement Round 4 (2026.05.21)
Conforms to: CLAUDE.md V07R01

Purpose:
  Scan agent-specific document folders (Product-Document/{agent_name}/incoming/),
  extract content from new files, append structured knowledge to a consolidated
  knowledge_base.md, move processed files to processed/, and update manifest
  with file hash + timestamp to prevent re-ingestion.

  Used by 3 iCE Layer 3 agents (Round 4):
    - iCE-tax-thailand-agent  → Product-Document/iCE-Tax/
    - iCE-netsuite-bundle-agent → Product-Document/iCE-NS-Bundle/
    - iCE-loan-agent → Product-Document/iCE-Loan/

  Pattern: incoming → ingest → processed (archive) + knowledge_base.md append

Anti-Hallucination Discipline:
  - File hash-based dedup — re-running on same file is no-op
  - Every knowledge entry carries source attribution (filename + ingest timestamp)
  - Knowledge base is APPEND-ONLY — past entries never overwritten
  - Manifest is auto-managed — do not edit manually

Invocation:
  CLI:    python3 knowledge_sync.py sync <agent_doc_root>
          python3 knowledge_sync.py status <agent_doc_root>
          python3 knowledge_sync.py list-pending <agent_doc_root>

  Python: from knowledge_sync import sync_agent_docs, get_status

Version: V01R01 | Date: 2026.05.21
"""

import sys
import json
import hashlib
import shutil
from pathlib import Path

# Shared helpers (single source of truth — see _lib/common.py + office_readers.py)
sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import now_iso, now_date  # noqa: E402
from office_readers import read_docx, read_pptx, read_xlsx, read_pdf, read_md_or_txt  # noqa: E402


# ---------- Utilities ----------
# now_iso, now_date moved to _lib/common.py.
# read_docx/read_pptx/read_xlsx/read_pdf/read_md_or_txt moved to _lib/office_readers.py
# (imported above) — read_file() dispatcher below still calls them by the same names.


def compute_file_hash(path: Path) -> str:
    """SHA-256 hash of file contents. Used for dedup."""
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()[:16]  # 16-char prefix is plenty for dedup


def read_manifest(manifest_path: Path) -> dict:
    """Read knowledge manifest. Returns empty schema if missing."""
    if manifest_path.exists():
        with open(manifest_path) as f:
            return json.load(f)
    return {
        "version": "V01R01",
        "schema_version": "V02R01",
        "agent": manifest_path.parent.parent.name,
        "doc_root": str(manifest_path.parent.parent),
        "last_sync_at": None,
        "files_processed": [],
        "knowledge_base_file": "knowledge_base.md",
        "description": "Auto-managed by knowledge_sync.py — tracks ingested files."
    }


def write_manifest(manifest_path: Path, data: dict) -> None:
    """Write manifest atomically."""
    tmp = manifest_path.with_suffix(".tmp")
    with open(tmp, "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    tmp.replace(manifest_path)


# ---------- File Readers ----------

def read_file(path: Path) -> str:
    """Dispatch to appropriate reader based on extension."""
    ext = path.suffix.lower()
    if ext == ".docx":
        return read_docx(path)
    elif ext == ".pptx":
        return read_pptx(path)
    elif ext == ".xlsx":
        return read_xlsx(path)
    elif ext == ".pdf":
        return read_pdf(path)
    elif ext in (".md", ".txt"):
        return read_md_or_txt(path)
    else:
        return f"[ERROR: unsupported file type {ext} — file {path.name} skipped]"


# ---------- Sync Core ----------

SUPPORTED_EXTENSIONS = {".pdf", ".docx", ".pptx", ".xlsx", ".md", ".txt"}


def scan_incoming(incoming_dir: Path) -> list:
    """Return list of files in incoming/ with supported extensions."""
    if not incoming_dir.exists():
        return []
    return sorted([
        f for f in incoming_dir.iterdir()
        if f.is_file()
        and f.suffix.lower() in SUPPORTED_EXTENSIONS
        and not f.name.startswith(".")
    ])


def is_already_processed(file_hash: str, manifest: dict) -> bool:
    """Check if file with given hash is in manifest."""
    return any(entry.get("hash") == file_hash for entry in manifest.get("files_processed", []))


def append_to_knowledge_base(kb_path: Path, source_filename: str, content: str,
                              ingest_timestamp: str) -> None:
    """Append new ingestion to consolidated knowledge_base.md."""
    if not kb_path.exists():
        # Initialize with header
        kb_path.write_text(f"""# Knowledge Base — Auto-Generated

**Agent:** {kb_path.parent.parent.name}
**Schema:** V01R01 | iCE Cognitive Compass V02R01 Round 4
**Build pattern:** Append-only by knowledge_sync.py — do not edit manually

---

""", encoding="utf-8")

    entry = f"""

---

## Source: `{source_filename}`

**Ingested:** {ingest_timestamp}
**File Type:** {Path(source_filename).suffix}

### Content

{content}

---
"""
    with open(kb_path, "a", encoding="utf-8") as f:
        f.write(entry)


def sync_agent_docs(agent_doc_root: Path, verbose: bool = True) -> dict:
    """Main sync routine — process all new files in incoming/.

    Args:
        agent_doc_root: Path to agent's doc folder (e.g., Product-Document/iCE-Tax/)
        verbose: Print progress to stdout

    Returns:
        Sync report dict with files_ingested + files_skipped + errors
    """
    incoming = agent_doc_root / "incoming"
    processed = agent_doc_root / "processed"
    knowledge = agent_doc_root / "knowledge"

    if not incoming.exists():
        return {"error": f"incoming/ not found at {incoming}"}
    processed.mkdir(exist_ok=True)
    knowledge.mkdir(exist_ok=True)

    manifest_path = knowledge / "knowledge_manifest.json"
    kb_path = knowledge / "knowledge_base.md"

    manifest = read_manifest(manifest_path)

    files = scan_incoming(incoming)
    if verbose:
        print(f"## Sync — {agent_doc_root.name}")
        print(f"   Found {len(files)} file(s) in incoming/")

    ingested = []
    skipped = []
    errors = []

    for f in files:
        file_hash = compute_file_hash(f)
        if is_already_processed(file_hash, manifest):
            skipped.append({"file": f.name, "reason": "hash already in manifest (already ingested)"})
            if verbose:
                print(f"   ⊘ {f.name} — already processed (hash dedup)")
            continue

        content = read_file(f)
        if content.startswith("[ERROR:"):
            errors.append({"file": f.name, "error": content})
            if verbose:
                print(f"   ✗ {f.name} — {content[:80]}...")
            continue

        timestamp = now_iso()
        append_to_knowledge_base(kb_path, f.name, content, timestamp)

        # Move to processed/
        dest = processed / f.name
        # Handle name collision (rare — different content, same name)
        if dest.exists():
            dest = processed / f"{f.stem}__{file_hash[:8]}{f.suffix}"
        shutil.move(str(f), str(dest))

        ingested.append({
            "file": f.name,
            "hash": file_hash,
            "ingested_at": timestamp,
            "content_chars": len(content),
            "moved_to": str(dest.relative_to(agent_doc_root))
        })
        if verbose:
            print(f"   ✓ {f.name} — ingested ({len(content)} chars) → moved to processed/")

    # Update manifest
    manifest["last_sync_at"] = now_iso()
    manifest["files_processed"].extend(ingested)
    write_manifest(manifest_path, manifest)

    report = {
        "agent": agent_doc_root.name,
        "sync_timestamp": manifest["last_sync_at"],
        "files_scanned": len(files),
        "files_ingested": ingested,
        "files_skipped": skipped,
        "errors": errors,
        "knowledge_base_path": str(kb_path),
        "knowledge_base_size_bytes": kb_path.stat().st_size if kb_path.exists() else 0,
        "total_files_in_manifest": len(manifest["files_processed"])
    }

    if verbose:
        print(f"   Ingested: {len(ingested)} | Skipped: {len(skipped)} | Errors: {len(errors)}")
        print(f"   Total in manifest: {report['total_files_in_manifest']}")

    return report


def get_status(agent_doc_root: Path) -> dict:
    """Return current state without modifying anything."""
    incoming = agent_doc_root / "incoming"
    processed = agent_doc_root / "processed"
    knowledge = agent_doc_root / "knowledge"
    manifest_path = knowledge / "knowledge_manifest.json"
    kb_path = knowledge / "knowledge_base.md"

    manifest = read_manifest(manifest_path)
    pending = scan_incoming(incoming) if incoming.exists() else []
    processed_files = list(processed.iterdir()) if processed.exists() else []

    return {
        "agent": agent_doc_root.name,
        "doc_root": str(agent_doc_root),
        "last_sync_at": manifest.get("last_sync_at"),
        "files_pending_in_incoming": len(pending),
        "files_in_processed": len(processed_files),
        "files_in_manifest": len(manifest.get("files_processed", [])),
        "knowledge_base_exists": kb_path.exists(),
        "knowledge_base_size_bytes": kb_path.stat().st_size if kb_path.exists() else 0,
        "pending_file_names": [f.name for f in pending]
    }


# ---------- CLI ----------

def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)

    cmd = sys.argv[1]
    doc_root = Path(sys.argv[2])

    if not doc_root.exists():
        print(f"ERROR: doc_root does not exist: {doc_root}", file=sys.stderr)
        sys.exit(1)

    if cmd == "sync":
        report = sync_agent_docs(doc_root, verbose=True)
        print()
        print(json.dumps(report, ensure_ascii=False, indent=2))

    elif cmd == "status":
        status = get_status(doc_root)
        print(json.dumps(status, ensure_ascii=False, indent=2))

    elif cmd == "list-pending":
        status = get_status(doc_root)
        if status["files_pending_in_incoming"] == 0:
            print(f"No files pending in {doc_root}/incoming/")
        else:
            print(f"Pending files in {doc_root}/incoming/ ({status['files_pending_in_incoming']}):")
            for name in status["pending_file_names"]:
                print(f"  - {name}")

    else:
        print(f"Unknown command: {cmd}", file=sys.stderr)
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
