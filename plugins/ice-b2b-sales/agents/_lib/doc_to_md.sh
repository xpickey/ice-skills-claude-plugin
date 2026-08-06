#!/usr/bin/env bash
# doc_to_md.sh — wrapper ให้ agent เรียกได้โดยไม่ต้องรู้ path ของ venv
# V01R01 | 2026.08.06 | ผูกกับ skill ice-doc-reader
#
# ทำไมต้องมี wrapper: anydoc/pdf-inspector ต้องใช้ python 3.12 ใน venv เฉพาะ
# (python3 ของระบบ = 3.9 + PEP 668 ห้ามติดตั้งลง site-packages)
# agent ไม่ต้องจำ path — เรียกไฟล์นี้พอ
set -uo pipefail
LIB="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PY="$LIB/.venv-doc/bin/python"
if [ ! -x "$PY" ]; then
  echo "❌ ไม่พบ venv เครื่องมือเอกสารที่ $PY" >&2
  echo "   สร้างใหม่: python3.12 -m venv '$LIB/.venv-doc' && '$LIB/.venv-doc/bin/pip' install firecrawl-anydoc pdf-inspector" >&2
  exit 4
fi
exec "$PY" "$LIB/doc_to_md.py" "$@"
