#!/usr/bin/env python3
"""
fact_checker.py
================
Anti-Hallucination Fact Checker for iCE Cognitive Compass.

Part of: V02R01 Improvement Round 1 (2026.05.20)
Conforms to: CLAUDE.md V07R01 H1-H4 (Anti-Hallucination Hard Rules)

Purpose:
  Extract facts (numbers, money, percentages, dates, proper nouns) from
  customer-facing artifacts (.docx, .pptx, .xlsx) and match against
  source documents (_opportunity.json, customer profile, registered facts).

  Flags unmatched facts as potential hallucinations — surfaces to
  qa-master-agent for BLOCKED verdict per H2 (no fabricated KPI/financial)
  and H1 (no fabricated customer/project names).

Invocation:
  qa-master-agent Dimension 3 Consistency invokes as sub-routine
  before computing verdict on Customer-Facing artifacts.

Usage (CLI):
  python3 fact_checker.py check-docx <target.docx> <source1.json> [source2.md ...]
  python3 fact_checker.py check-pptx <target.pptx> <source1.json> [source2.md ...]
  python3 fact_checker.py check-xlsx <target.xlsx> <source1.json> [source2.md ...]
  python3 fact_checker.py extract <target.docx|.pptx|.xlsx>

Usage (Python import):
  from fact_checker import check_artifact, extract_facts, match_against_source

Output JSON schema:
  {
    "target": "path",
    "facts_extracted": {
      "numbers": [...],
      "money": [...],
      "percentages": [...],
      "dates": [...],
      "proper_nouns": [...]
    },
    "matched_in_source": [...],
    "unmatched_potential_hallucinations": [
      {"fact": str, "type": str, "context": str, "severity": "high|medium|low"}
    ],
    "hallucination_risk_score": 0-100,
    "verdict_recommendation": "PASS|CONDITIONAL|FAIL|BLOCKED"
  }

Version: V01R01 | Date: 2026.05.20
"""

import re
import sys
import json
from pathlib import Path

# Shared readers (single source of truth — see _lib/office_readers.py).
# These have parse-time try/except, so a malformed/locked customer file returns an
# "[ERROR: ...]" sentinel instead of crashing the QA fact-check. read_source below
# checks the sentinel so an unreadable office file never feeds garbage to the regex.
sys.path.insert(0, str(Path(__file__).resolve().parent))
from office_readers import read_docx, read_pptx, read_xlsx, ERROR_PREFIX  # noqa: E402

# ---------- Pattern Library ----------

# Money patterns — THB, USD, EUR, etc.
MONEY_RE = re.compile(
    r"(?:THB|USD|EUR|GBP|JPY|฿|\$)\s*([\d,]+(?:\.\d+)?)\s*(?:M|K|B|million|thousand|billion|ล้าน|พัน)?",
    re.IGNORECASE,
)
# Also catch numbers followed by currency
MONEY_RE_2 = re.compile(
    r"([\d,]+(?:\.\d+)?)\s*(?:THB|USD|EUR|baht|บาท|million baht|ล้านบาท)",
    re.IGNORECASE,
)

# Percentages
PCT_RE = re.compile(r"(\d+(?:\.\d+)?)\s*(?:%|percent|เปอร์เซ็นต์|pct)")

# Dates — YYYY.MM.DD (V07R01 standard), YYYY-MM-DD, DD/MM/YYYY, Buddhist 25xx
DATE_RE = re.compile(
    r"(?:(?:20|25)\d{2}[.\-/](?:0?[1-9]|1[0-2])[.\-/](?:0?[1-9]|[12]\d|3[01]))|"
    r"(?:(?:0?[1-9]|[12]\d|3[01])[/\-](?:0?[1-9]|1[0-2])[/\-](?:20|25)\d{2})|"
    r"(?:พ\.ศ\.\s*25\d{2})|(?:FY\s*20\d{2})"
)

# Generic numbers (last resort — for quantities)
NUMBER_RE = re.compile(r"\b(\d{1,3}(?:,\d{3})+(?:\.\d+)?|\d+(?:\.\d+)?)\b")

# Proper nouns — capitalized words (English) + Thai company patterns
PROPER_NOUN_EN = re.compile(r"\b[A-Z][a-zA-Z]{2,}(?:\s+[A-Z][a-zA-Z]+){0,4}\b")
# Thai company indicators
THAI_COMPANY_RE = re.compile(r"บริษัท\s+[ก-๙\sA-Za-z0-9]+\s+จำกัด(?:\s+\(มหาชน\))?")

# Acronyms to preserve (NOT fabrication risk — they're standard terms)
KNOWN_ACRONYMS = {
    "TFRS", "IFRS", "OIC", "BOT", "SEC", "SET", "PAE",
    "TQR", "TQM", "EPM", "ERP", "GFMIS", "MEDDPICC",
    "ROE", "ROI", "NPV", "IRR", "ARR", "NRR", "GRR",
    "MOU", "NDA", "SoW", "MSA", "TOR", "RFP", "RFI",
    "CFO", "CIO", "CEO", "COO", "CTO", "CMO",
    "QBR", "EBR", "AMS", "SLA", "API", "SaaS",
    "Q1", "Q2", "Q3", "Q4", "H1", "H2", "FY2025", "FY2026", "FY2027",
    "Pre-Sale", "Close-Won", "Close-Lost",
    "WIN", "FOCUS", "ACTIVE", "EARLY",
    "CLAUDE", "iCE",
}


# ---------- Extraction ----------

def extract_money(text):
    """Extract money figures with currency context."""
    results = []
    for m in MONEY_RE.finditer(text):
        results.append({"value": m.group(0).strip(), "amount": m.group(1)})
    for m in MONEY_RE_2.finditer(text):
        results.append({"value": m.group(0).strip(), "amount": m.group(1)})
    return list({r["value"]: r for r in results}.values())  # dedupe


def extract_percentages(text):
    """Extract percentages."""
    results = []
    for m in PCT_RE.finditer(text):
        results.append({"value": m.group(0).strip(), "pct": float(m.group(1))})
    return results


def extract_dates(text):
    """Extract date strings."""
    return list(set(m.group(0).strip() for m in DATE_RE.finditer(text)))


def extract_numbers(text):
    """Extract generic numbers (>= 100 — small numbers tend to be ordinal)."""
    results = []
    for m in NUMBER_RE.finditer(text):
        raw = m.group(0).replace(",", "")
        try:
            val = float(raw)
            if val >= 100:  # filter ordinals 1-99
                results.append({"value": m.group(0), "numeric": val})
        except ValueError:
            pass
    return results


def extract_proper_nouns(text):
    """Extract proper nouns (English capitalized phrases + Thai companies).
    Filters out known acronyms and common words."""
    results = set()
    for m in PROPER_NOUN_EN.finditer(text):
        token = m.group(0).strip()
        if token not in KNOWN_ACRONYMS and len(token) > 3:
            results.add(token)
    for m in THAI_COMPANY_RE.finditer(text):
        results.add(m.group(0).strip())
    return sorted(results)


# ---------- File Readers ----------
# read_docx / read_pptx / read_xlsx moved to _lib/office_readers.py (imported above),
# which adds parse-time error handling these inline copies lacked.

def read_source(path):
    """Read source file — JSON or text (always utf-8 for Thai content)."""
    path = Path(path)
    try:
        if path.suffix == ".json":
            with open(path, "r", encoding="utf-8") as f:
                return json.dumps(json.load(f), ensure_ascii=False)
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return f"{ERROR_PREFIX} source read failed for {path.name} — {e}]"


# ---------- Matching ----------

def normalize(s):
    """Normalize for matching — lowercase, strip commas, strip whitespace."""
    return re.sub(r"[,\s]", "", s.lower())


def match_against_source(target_facts, source_text):
    """Check each fact against source text — return matched + unmatched."""
    source_norm = normalize(source_text)
    matched = []
    unmatched = []

    def check(fact_dict_or_str, fact_type):
        if isinstance(fact_dict_or_str, dict):
            fact = fact_dict_or_str.get("value", str(fact_dict_or_str))
        else:
            fact = str(fact_dict_or_str)
        fact_norm = normalize(fact)
        if fact_norm in source_norm:
            matched.append({"fact": fact, "type": fact_type})
        else:
            # Try alternate forms (with/without comma in numbers)
            # Extract just digits
            digits = re.sub(r"[^\d.]", "", fact)
            if digits and digits in source_norm:
                matched.append({"fact": fact, "type": fact_type})
            else:
                severity = "high" if fact_type in ("money", "percentage") else "medium"
                unmatched.append({"fact": fact, "type": fact_type, "severity": severity})

    for f in target_facts.get("money", []):
        check(f, "money")
    for f in target_facts.get("percentages", []):
        check(f, "percentage")
    for f in target_facts.get("dates", []):
        check(f, "date")
    for f in target_facts.get("numbers", []):
        check(f, "number")
    for f in target_facts.get("proper_nouns", []):
        check(f, "proper_noun")

    return matched, unmatched


def compute_risk_score(unmatched):
    """Compute hallucination risk score 0-100 based on unmatched count + severity."""
    if not unmatched:
        return 0
    high = sum(1 for u in unmatched if u["severity"] == "high")
    medium = sum(1 for u in unmatched if u["severity"] == "medium")
    score = min(100, high * 15 + medium * 5)
    return score


def verdict_from_risk(score):
    """Map risk score to qa-master verdict."""
    if score == 0:
        return "PASS"
    elif score <= 20:
        return "CONDITIONAL"
    elif score <= 50:
        return "FAIL"
    else:
        return "BLOCKED"


# ---------- Main API ----------

def extract_facts(target_path):
    """Extract all facts from a target artifact.

    If a reader fails (missing lib / corrupt / locked file) it returns an
    "[ERROR: ...]" sentinel; we surface that as an _error field and skip regex
    extraction so the sentinel text is never mistaken for document content.
    """
    path = Path(target_path)
    if path.suffix == ".docx":
        text = read_docx(path)
    elif path.suffix == ".pptx":
        text = read_pptx(path)
    elif path.suffix == ".xlsx":
        text = read_xlsx(path)
    else:
        try:
            with open(path, "r", encoding="utf-8") as f:
                text = f.read()
        except Exception as e:
            text = f"{ERROR_PREFIX} read failed for {path.name} — {e}]"

    if text.startswith(ERROR_PREFIX):
        return {"_error": text, "money": [], "percentages": [],
                "dates": [], "numbers": [], "proper_nouns": []}

    return {
        "money": extract_money(text),
        "percentages": extract_percentages(text),
        "dates": extract_dates(text),
        "numbers": extract_numbers(text),
        "proper_nouns": extract_proper_nouns(text),
    }


def check_artifact(target_path, source_paths):
    """Full check — extract facts, match against sources, compute risk."""
    facts = extract_facts(target_path)

    # Concatenate all sources
    source_combined = "\n".join(read_source(s) for s in source_paths)

    matched, unmatched = match_against_source(facts, source_combined)
    risk = compute_risk_score(unmatched)
    verdict = verdict_from_risk(risk)

    return {
        "target": str(target_path),
        "sources_checked": [str(s) for s in source_paths],
        "facts_extracted": facts,
        "matched_in_source": matched,
        "unmatched_potential_hallucinations": unmatched,
        "hallucination_risk_score": risk,
        "verdict_recommendation": verdict,
    }


# ---------- CLI ----------

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    cmd = sys.argv[1]

    if cmd == "extract":
        if len(sys.argv) < 3:
            print("Usage: fact_checker.py extract <target>")
            sys.exit(1)
        result = extract_facts(sys.argv[2])
        print(json.dumps(result, indent=2, ensure_ascii=False))

    elif cmd in ("check-docx", "check-pptx", "check-xlsx", "check"):
        if len(sys.argv) < 4:
            print(f"Usage: fact_checker.py {cmd} <target> <source1> [source2 ...]")
            sys.exit(1)
        target = sys.argv[2]
        sources = sys.argv[3:]
        result = check_artifact(target, sources)
        print(json.dumps(result, indent=2, ensure_ascii=False))

    else:
        print(f"Unknown command: {cmd}")
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
