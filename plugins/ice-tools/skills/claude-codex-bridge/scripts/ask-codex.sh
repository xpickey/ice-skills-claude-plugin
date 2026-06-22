#!/usr/bin/env bash
# Claude ↔ Codex bridge helper (V01R01).
# Claude calls this via Bash to converse with Codex gpt-5.5, turn by turn.
# Claude drives the loop; Codex keeps its own session memory across turns.
#
# Usage:
#   ask-codex.sh --new     "<prompt>"   # start a fresh thread
#   ask-codex.sh --resume  "<prompt>"   # continue the saved thread (Codex remembers)
#
# Env:
#   BRIDGE_DIR   working/transcript dir (default: a per-day dir under $TMPDIR)
#   BRIDGE_SANDBOX   codex sandbox for --new (default: read-only;
#                    set to workspace-write ONLY when Codex must edit files —
#                    ask the user first)
#
# Verified Codex CLI quirks (v0.137.0, from --help, do not "fix" these):
#   * `codex exec` has NO -a/--ask-for-approval flag; approval = sandbox mode.
#   * `codex exec resume` accepts FEWER flags than `codex exec`:
#       NO -s/--sandbox and NO -C/--cd (it inherits them from the saved session).
#   * session id comes from the JSONL event {"type":"thread.started","thread_id":...}
#   * --output-last-message gives ONLY the final reply (no banner/error/token line).
#   * stderr carries skill/MCP load noise → kept in err.log, not mixed into reply.
set -uo pipefail   # NB: no -e, so we can log codex's stderr before reacting

DIR="${BRIDGE_DIR:-${TMPDIR:-/tmp}/claude-codex-bridge}"
SANDBOX="${BRIDGE_SANDBOX:-read-only}"
SID_FILE="$DIR/session-id"
LAST="$DIR/last.txt"
EVENTS="$DIR/events.jsonl"
ERRLOG="$DIR/err.log"
TRANSCRIPT="$DIR/transcript.md"
mkdir -p "$DIR"

mode="${1:-}"; prompt="${2:-}"
if [[ -z "$mode" || -z "$prompt" ]]; then
  echo "usage: ask-codex.sh --new|--resume \"<prompt>\"" >&2; exit 2
fi
ts() { date "+%Y-%m-%d %H:%M:%S"; }

rc=0
if [[ "$mode" == "--new" ]]; then
  # full flag set: exec accepts -s and -C
  codex exec --json -o "$LAST" --skip-git-repo-check -s "$SANDBOX" -C "$DIR" \
    "$prompt" >"$EVENTS" 2>"$ERRLOG" || rc=$?
elif [[ "$mode" == "--resume" ]]; then
  sid="$(cat "$SID_FILE" 2>/dev/null || true)"
  if [[ -z "$sid" ]]; then echo "no saved session-id; run --new first" >&2; exit 3; fi
  # reduced flag set: resume rejects -s and -C (inherits from session)
  codex exec resume "$sid" --json -o "$LAST" --skip-git-repo-check \
    "$prompt" >"$EVENTS" 2>"$ERRLOG" || rc=$?
else
  echo "unknown mode: $mode (use --new or --resume)" >&2; exit 2
fi

if [[ $rc -ne 0 ]]; then
  echo "codex exec failed (exit $rc). Real error (noise filtered):" >&2
  grep -iE "error|fatal|unexpected|usage" "$ERRLOG" \
    | grep -ivE "rmcp|mcp::|failed to load skill|githubcopilot" | head -5 >&2
  exit $rc
fi

# capture / refresh session id from thread.started (fallback: session_meta id)
new_sid="$(grep -o '"thread_id":"[^"]*"' "$EVENTS" 2>/dev/null | head -1 | sed 's/.*:"//;s/"//')"
[[ -z "$new_sid" ]] && new_sid="$(grep -o '"id":"[0-9a-f-]\{36\}"' "$EVENTS" 2>/dev/null | head -1 | sed 's/.*:"//;s/"//')"
[[ -n "$new_sid" ]] && echo "$new_sid" >"$SID_FILE"

reply="$(cat "$LAST" 2>/dev/null || echo "(no reply captured)")"

{
  echo ""
  echo "### CLAUDE → CODEX  ($(ts))  [$mode]"
  echo "$prompt"
  echo ""
  echo "### CODEX → CLAUDE  ($(ts))  [session ${new_sid:-?}]"
  echo "$reply"
  echo ""
  echo "---"
} >>"$TRANSCRIPT"

echo "$reply"
