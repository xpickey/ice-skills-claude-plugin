#!/usr/bin/env bash
# Claude ↔ Codex bridge helper (V02R01 | 2026.07.10).
# Claude calls this via Bash to converse with Codex, turn by turn.
# Claude drives the loop; Codex keeps its own session memory across turns.
#
# Usage:
#   ask-codex.sh [--session <name>] [--schema <file>] --new     "<prompt>"   # start a fresh thread
#   ask-codex.sh [--session <name>] [--schema <file>] --resume  "<prompt>"   # continue saved thread
#   ask-codex.sh --list-sessions                                             # show known threads
#
# New in V02R01 (all flags verified against codex-cli 0.137.0 --help on 2026.07.10):
#   --session <name>   isolate threads per name (parallel shards / per-opportunity) —
#                      no --session = legacy single-thread dir (back-compat with V01)
#   --schema <file>    pass a JSON Schema to codex --output-schema (exec AND resume support it)
#                      → forces structured verdict JSON per references/05_review_contract.md
#                      (feature-detected at runtime: flag missing in future CLI → warn + proceed without)
#   --list-sessions    list known session dirs + ids
#   overwrite guard:   --new on an existing thread saves old id to session-id.prev + warns
#
# Env:
#   BRIDGE_DIR       base working dir (default: $TMPDIR/claude-codex-bridge)
#   BRIDGE_SANDBOX   codex sandbox for --new (default: read-only; workspace-write ONLY with user consent)
#
# Verified Codex CLI facts (v0.137.0, probed 2026.07.10 — do not "fix" these):
#   * `codex exec` accepts -s and -C; `codex exec resume` does NOT (inherits from session).
#   * `codex exec resume [SESSION_ID]` takes a UUID (or thread name) positionally; also --last.
#   * `--output-schema <FILE>` exists on BOTH exec and resume.
#   * `-m/--model` exists on both (not used by default here).
#   * session id comes from JSONL event {"type":"thread.started","thread_id":...}
#   * --output-last-message gives ONLY the final reply; stderr noise stays in err.log.
set -uo pipefail   # NB: no -e, so we can log codex's stderr before reacting

BASE="${BRIDGE_DIR:-${TMPDIR:-/tmp}/claude-codex-bridge}"
SANDBOX="${BRIDGE_SANDBOX:-read-only}"
SKILL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SESSION=""            # empty = legacy default dir (back-compat)
SCHEMA=""
mode=""
prompt=""

ts() { date "+%Y-%m-%d %H:%M:%S"; }

# ---- parse args ------------------------------------------------------------
while [[ $# -gt 0 ]]; do
  case "$1" in
    --session)
      SESSION="${2:-}"
      if [[ -z "$SESSION" ]]; then echo "--session needs a name" >&2; exit 2; fi
      # ต้องขึ้นต้นด้วย alnum — กัน '.'/'..'/ชื่อซ่อน (Codex review H1/M3 2026.07.10: '..' ทะลุไปทับ default thread)
      if [[ ! "$SESSION" =~ ^[A-Za-z0-9][A-Za-z0-9._-]*$ ]]; then
        echo "invalid session name '$SESSION' (ต้องขึ้นต้น a-z/0-9 · allowed: A-Z a-z 0-9 . _ -)" >&2; exit 2
      fi
      shift 2 ;;
    --schema)
      SCHEMA="${2:-}"
      if [[ -z "$SCHEMA" ]]; then echo "--schema needs a file path" >&2; exit 2; fi
      if [[ ! -f "$SCHEMA" ]]; then echo "schema file not found: $SCHEMA" >&2; exit 2; fi
      shift 2 ;;
    --list-sessions|--new|--resume)
      # mode ถูกตั้งแล้ว = ผู้เรียกผสม flag ผิด (Codex review M4) → usage ไม่เดา
      if [[ -n "$mode" ]]; then echo "conflicting modes: '$mode' และ '$1' — ใช้ได้ทีละ mode" >&2; exit 2; fi
      mode="$1"
      if [[ "$1" != "--list-sessions" ]]; then
        prompt="${2:-}"; shift; [[ $# -gt 0 ]] && shift
      else shift; fi ;;
    *)
      echo "unknown arg: $1" >&2
      echo "usage: ask-codex.sh [--session <name>] [--schema <file>] --new|--resume \"<prompt>\" | --list-sessions" >&2
      exit 2 ;;
  esac
done

# ---- list sessions ---------------------------------------------------------
if [[ "$mode" == "--list-sessions" ]]; then
  echo "base: $BASE"
  if [[ -f "$BASE/session-id" ]]; then
    echo "  (default)  id=$(cat "$BASE/session-id")  last=$(date -r "$BASE/session-id" "+%Y-%m-%d %H:%M" 2>/dev/null || echo '?')"
  fi
  if [[ -d "$BASE/sessions" ]]; then
    for d in "$BASE/sessions"/*/; do
      [[ -d "$d" ]] || continue
      name="$(basename "$d")"
      if [[ -f "$d/session-id" ]]; then
        echo "  $name  id=$(cat "$d/session-id")  last=$(date -r "$d/session-id" "+%Y-%m-%d %H:%M" 2>/dev/null || echo '?')"
      else
        echo "  $name  (no thread started yet)"
      fi
    done
  fi
  exit 0
fi

if [[ -z "$mode" || -z "$prompt" ]]; then
  echo "usage: ask-codex.sh [--session <name>] [--schema <file>] --new|--resume \"<prompt>\" | --list-sessions" >&2
  exit 2
fi

# ---- resolve session dir ---------------------------------------------------
if [[ -n "$SESSION" ]]; then DIR="$BASE/sessions/$SESSION"; else DIR="$BASE"; fi
SID_FILE="$DIR/session-id"
LAST="$DIR/last.txt"
EVENTS="$DIR/events.jsonl"
ERRLOG="$DIR/err.log"
TRANSCRIPT="$DIR/transcript.md"
mkdir -p "$DIR"

# ---- schema feature-detection (runtime — CLI updates for sure) --------------
# ตรวจกับ command path ที่จะรันจริง (Codex review M2: exec กับ resume อาจต่างกันใน version หน้า)
SCHEMA_ARGS=()
if [[ -n "$SCHEMA" ]]; then
  if [[ "$mode" == "--resume" ]]; then HELP_CMD=(codex exec resume --help); else HELP_CMD=(codex exec --help); fi
  if "${HELP_CMD[@]}" 2>/dev/null | grep -q -- "--output-schema"; then
    SCHEMA_ARGS=(--output-schema "$SCHEMA")
  else
    echo "WARN: this codex CLI path (${HELP_CMD[*]}) has no --output-schema — proceeding WITHOUT schema; use contract fallback ladder (ref 05 §9)" >&2
  fi
fi

# ---- overwrite guard on --new ----------------------------------------------
if [[ "$mode" == "--new" && -f "$SID_FILE" ]]; then
  cp "$SID_FILE" "$SID_FILE.prev" 2>/dev/null || true
  echo "WARN: session '${SESSION:-default}' already had thread $(cat "$SID_FILE") — starting NEW thread replaces it (old id saved to session-id.prev). Use --resume to continue instead." >&2
fi

# ---- run codex ---------------------------------------------------------------
rc=0
if [[ "$mode" == "--new" ]]; then
  # full flag set: exec accepts -s and -C
  # '--' terminator กัน prompt ที่ขึ้นต้นด้วย - ถูกกินเป็น flag (Codex review H2 · clap รองรับ)
  codex exec --json -o "$LAST" --skip-git-repo-check -s "$SANDBOX" -C "$DIR" \
    ${SCHEMA_ARGS[@]+"${SCHEMA_ARGS[@]}"} \
    -- "$prompt" >"$EVENTS" 2>"$ERRLOG" || rc=$?
elif [[ "$mode" == "--resume" ]]; then
  sid="$(cat "$SID_FILE" 2>/dev/null || true)"
  if [[ -z "$sid" ]]; then echo "no saved session-id for '${SESSION:-default}'; run --new first" >&2; exit 3; fi
  # reduced flag set: resume rejects -s and -C (inherits from session) — but accepts --output-schema
  codex exec resume --json -o "$LAST" --skip-git-repo-check \
    ${SCHEMA_ARGS[@]+"${SCHEMA_ARGS[@]}"} \
    -- "$sid" "$prompt" >"$EVENTS" 2>"$ERRLOG" || rc=$?
fi

if [[ $rc -ne 0 ]]; then
  echo "codex exec failed (exit $rc). Real error (noise filtered):" >&2
  grep -iE "error|fatal|unexpected|usage" "$ERRLOG" \
    | grep -ivE "rmcp|mcp::|failed to load skill|githubcopilot" | head -5 >&2
  echo "$(ts) | ${SESSION:-default} | $mode | rc=$rc" >>"$SKILL_DIR/_bridge-sessions.log" 2>/dev/null || true
  exit $rc
fi

# capture session id — เฉพาะจาก thread.started เท่านั้น (Codex review H3: generic-UUID fallback เสี่ยงจับ id ผิด → resume ผิด thread)
new_sid="$(grep -o '"thread_id":"[^"]*"' "$EVENTS" 2>/dev/null | head -1 | sed 's/.*:"//;s/"//')"
if [[ -n "$new_sid" ]]; then
  echo "$new_sid" >"$SID_FILE"
elif [[ "$mode" == "--new" ]]; then
  # --new ต้องได้ id ใหม่เสมอ — ไม่ได้ = fail ดัง ๆ กัน session-id เก่าค้างแล้ว resume ผิด thread (Codex review M1)
  echo "ERROR: no thread.started id captured from new thread — session-id NOT updated (old id preserved in ${SID_FILE}.prev if any). Do not --resume; investigate events.jsonl" >&2
  echo "$(ts) | ${SESSION:-default} | $mode | rc=4-no-thread-id" >>"$SKILL_DIR/_bridge-sessions.log" 2>/dev/null || true
  exit 4
fi
# --resume: ไม่เจอ thread.started = ไม่แตะ SID_FILE (id เดิมยังถูก)

reply="$(cat "$LAST" 2>/dev/null || echo "(no reply captured)")"

{
  echo ""
  echo "### CLAUDE → CODEX  ($(ts))  [$mode${SESSION:+ · session=$SESSION}${SCHEMA:+ · schema}]"
  echo "$prompt"
  echo ""
  echo "### CODEX → CLAUDE  ($(ts))  [session ${new_sid:-?}]"
  echo "$reply"
  echo ""
  echo "---"
} >>"$TRANSCRIPT"

echo "$(ts) | ${SESSION:-default} | $mode | rc=0" >>"$SKILL_DIR/_bridge-sessions.log" 2>/dev/null || true

echo "$reply"
