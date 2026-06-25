#!/usr/bin/env bash
# Claude ↔ OpenRouter bridge helper (V01R01).
# Claude calls this via Bash to consult ANY model on OpenRouter, turn by turn.
# Claude drives the loop. OpenRouter is STATELESS → this helper keeps the
# conversation history locally (messages.json) and resends it every turn.
#
# Usage:
#   ask-openrouter.sh --models                      # list available models (id + pricing)
#   ask-openrouter.sh --new    [--model X] "<p>"    # start a fresh conversation
#   ask-openrouter.sh --resume [--model X] "<p>"    # continue (resends full history)
#   ask-openrouter.sh --pick                         # print the 5-model picker menu + exit 7
#
# Model selection (--model accepts a full id OR a short alias):
#   gpt → openai/gpt-5.1 · sonnet → anthropic/claude-sonnet-4 · opus → anthropic/claude-opus-4
#   gemini → google/gemini-2.5-pro · flash → google/gemini-2.5-flash
#   r1 → deepseek/deepseek-r1 · llama → meta-llama/llama-3.3-70b-instruct
#   (aliases resolve to a best-guess current id; verify live with --models)
# If --model is OMITTED on --new → helper prints the 5-model picker and exits 7
#   (Claude then asks the user / picks per task; never silently defaults).
#
# Env:
#   OPENROUTER_API_KEY   REQUIRED — set in ~/.hermes/.env (uncomment) or export
#   OPENROUTER_MODEL     optional explicit default (skips the picker if set)
#   BRIDGE_DIR           working/transcript dir (default per-day under $TMPDIR)
#
# Best practice (OpenRouter docs, verified 2026.06): endpoint
# /api/v1/chat/completions · headers Authorization+Content-Type (required),
# HTTP-Referer+X-Title (optional attribution) · body {model,messages[]} ·
# models list GET /api/v1/models · errors return JSON {"error":{...}} on HTTP 200-ish
# so we MUST inspect .error, not just the HTTP code.
set -uo pipefail   # no -e: we inspect errors before reacting

DIR="${BRIDGE_DIR:-${TMPDIR:-/tmp}/claude-openrouter-bridge}"
HIST="$DIR/messages.json"
RESP="$DIR/response.json"
TRANSCRIPT="$DIR/transcript.md"
MODEL_FILE="$DIR/model"
BASE="${OPENROUTER_BASE_URL:-https://openrouter.ai/api/v1}"
mkdir -p "$DIR"
ts() { date "+%Y-%m-%d %H:%M:%S"; }

# ── key load (env, or source ~/.hermes/.env) ────────────────────────────
if [[ -z "${OPENROUTER_API_KEY:-}" && -f "$HOME/.hermes/.env" ]]; then
  # pull only the OPENROUTER_API_KEY line if it is uncommented
  k="$(grep -E '^\s*OPENROUTER_API_KEY=' "$HOME/.hermes/.env" 2>/dev/null | head -1 | cut -d= -f2-)"
  [[ -n "$k" ]] && export OPENROUTER_API_KEY="$k"
fi
require_key() {
  if [[ -z "${OPENROUTER_API_KEY:-}" ]]; then
    echo "✗ OPENROUTER_API_KEY not set." >&2
    echo "  1) create a key: https://openrouter.ai/keys" >&2
    echo "  2) uncomment+set in ~/.hermes/.env:  OPENROUTER_API_KEY=sk-or-..." >&2
    echo "     (or: export OPENROUTER_API_KEY=sk-or-...)" >&2
    exit 4
  fi
}

# ── alias → model id ────────────────────────────────────────────────────
resolve_model() {
  case "$1" in
    gpt)     echo "openai/gpt-5.1" ;;
    sonnet)  echo "anthropic/claude-sonnet-4" ;;
    opus)    echo "anthropic/claude-opus-4" ;;
    gemini)  echo "google/gemini-2.5-pro" ;;
    flash)   echo "google/gemini-2.5-flash" ;;
    r1)      echo "deepseek/deepseek-r1" ;;
    llama)   echo "meta-llama/llama-3.3-70b-instruct" ;;
    *)       echo "$1" ;;   # already a full id
  esac
}

# ── 5-model picker (printed when no model chosen) ───────────────────────
print_picker() {
  cat >&2 <<'MENU'
เลือก model สำหรับงานนี้ (เรียงเก่งสุด → เหมาะพอดี) — ส่ง --model <alias|id>:
  1. r1       deepseek/deepseek-r1            — reasoning หนัก ถกเชิงลึก (ราคากลาง)
  2. sonnet   anthropic/claude-sonnet-4       — allround เขียน/วิเคราะห์ดีรอบด้าน
  3. gpt      openai/gpt-5.1                  — second opinion ต่างค่าย/persona review
  4. gemini   google/gemini-2.5-pro           — context ยาว/เอกสารใหญ่
  5. flash    google/gemini-2.5-flash         — เร็ว/ถูก ร่าง-สรุปเร็ว
(ดูรายการ+ราคาเต็ม: ask-openrouter.sh --models)
MENU
}

curl_headers=(
  -H "Authorization: Bearer ${OPENROUTER_API_KEY:-}"
  -H "Content-Type: application/json"
  -H "HTTP-Referer: https://iceconsulting.co.th"
  -H "X-Title: iCE Cognitive Compass — openrouter-bridge"
)

mode="${1:-}"

# ── --models : list catalog (id + prompt/completion price) ──────────────
if [[ "$mode" == "--models" ]]; then
  require_key
  curl -sS "${curl_headers[@]}" "$BASE/models" 2>/dev/null \
    | jq -r '.data[] | "\(.id)\t$\(.pricing.prompt // "?")/in  $\(.pricing.completion // "?")/out"' \
    | sort | head -100
  exit 0
fi

# ── --pick : just show the menu ─────────────────────────────────────────
if [[ "$mode" == "--pick" ]]; then print_picker; exit 7; fi

# ── parse --model (optional) then prompt ────────────────────────────────
shift || true
MODEL=""
if [[ "${1:-}" == "--model" ]]; then MODEL="$(resolve_model "${2:-}")"; shift 2 || true; fi
prompt="${1:-}"

if [[ "$mode" != "--new" && "$mode" != "--resume" ]]; then
  echo "usage: ask-openrouter.sh --models | --pick | --new|--resume [--model X] \"<prompt>\"" >&2
  exit 2
fi
if [[ -z "$prompt" ]]; then echo "missing prompt" >&2; exit 2; fi
require_key

# resolve model: flag > env OPENROUTER_MODEL > saved (resume) > picker
if [[ -z "$MODEL" ]]; then
  if [[ -n "${OPENROUTER_MODEL:-}" ]]; then MODEL="$(resolve_model "$OPENROUTER_MODEL")"
  elif [[ "$mode" == "--resume" && -f "$MODEL_FILE" ]]; then MODEL="$(cat "$MODEL_FILE")"
  else print_picker; exit 7; fi   # no silent default — ask Claude/user to pick
fi
echo "$MODEL" >"$MODEL_FILE"

# ── build messages array (stateless → resend full history) ──────────────
if [[ "$mode" == "--new" || ! -f "$HIST" ]]; then echo '[]' >"$HIST"; fi
# append the new user turn
jq --arg c "$prompt" '. + [{"role":"user","content":$c}]' "$HIST" >"$HIST.tmp" && mv "$HIST.tmp" "$HIST"

payload="$(jq -n --arg m "$MODEL" --slurpfile msgs "$HIST" \
  '{model:$m, messages:$msgs[0]}')"

http="$(curl -sS -w '\n%{http_code}' "${curl_headers[@]}" \
  -d "$payload" "$BASE/chat/completions" 2>/dev/null)"
body="$(printf '%s' "$http" | sed '$d')"
code="$(printf '%s' "$http" | tail -1)"
printf '%s' "$body" >"$RESP"

# ── error guard: inspect .error even on HTTP 200 ────────────────────────
err="$(printf '%s' "$body" | jq -r '.error.message // empty' 2>/dev/null)"
if [[ -n "$err" || "$code" -ge 400 ]]; then
  echo "✗ OpenRouter error (HTTP $code, model $MODEL): ${err:-unknown}" >&2
  printf '%s' "$body" | jq -r '.error // .' 2>/dev/null | head -10 >&2
  exit 5
fi

reply="$(printf '%s' "$body" | jq -r '.choices[0].message.content // empty')"
if [[ -z "$reply" ]]; then echo "✗ empty reply (model $MODEL)" >&2; exit 6; fi

# append assistant turn to history (so --resume remembers)
jq --arg c "$reply" '. + [{"role":"assistant","content":$c}]' "$HIST" >"$HIST.tmp" && mv "$HIST.tmp" "$HIST"

# transcript audit
{
  echo ""
  echo "### CLAUDE → OPENROUTER  ($(ts))  [$mode · model=$MODEL]"
  echo "$prompt"
  echo ""
  echo "### OPENROUTER → CLAUDE  ($(ts))  [model=$MODEL]"
  echo "$reply"
  echo ""
  echo "---"
} >>"$TRANSCRIPT"

echo "$reply"
