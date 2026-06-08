#!/usr/bin/env python3
"""
build_xlsx.py — generic XLSX builder for sales agents.

Usage:
    python3 build_xlsx.py spec.json out.xlsx

spec.json schema:
{
  "sheets": [
    {
      "name": "Sheet1",
      "headers": ["A", "B", "C"],
      "rows": [["x", 1, 2.5], ...],
      "formulas": {"D2": "=B2+C2", ...},      # optional
      "freeze": "B2",                          # optional
      "column_widths": {"A": 30, "B": 12},     # optional
      "header_fill": "1F4E79",                 # optional hex
      "header_font_color": "FFFFFF"            # optional hex
    }
  ]
}
"""
import sys, json
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter


def fill(hex_):
    return PatternFill(start_color=hex_, end_color=hex_, fill_type="solid")


def build(spec_path, out_path):
    with open(spec_path) as f:
        spec = json.load(f)
    wb = Workbook()
    wb.remove(wb.active)
    for sht in spec.get("sheets", []):
        ws = wb.create_sheet(title=sht["name"][:31])
        headers = sht.get("headers", [])
        if headers:
            ws.append(headers)
            hdr_fill = fill(sht.get("header_fill", "1F4E79"))
            hdr_font = Font(bold=True, color=sht.get("header_font_color", "FFFFFF"))
            for j, _ in enumerate(headers, start=1):
                c = ws.cell(row=1, column=j)
                c.fill = hdr_fill
                c.font = hdr_font
                c.alignment = Alignment(horizontal="center", vertical="center")
        for row in sht.get("rows", []):
            ws.append(row)
        for cell, formula in (sht.get("formulas") or {}).items():
            ws[cell] = formula
        for col, width in (sht.get("column_widths") or {}).items():
            ws.column_dimensions[col].width = width
        if sht.get("freeze"):
            ws.freeze_panes = sht["freeze"]
        thin = Side(border_style="thin", color="CCCCCC")
        border = Border(left=thin, right=thin, top=thin, bottom=thin)
        for row in ws.iter_rows(min_row=1, max_row=ws.max_row, max_col=ws.max_column):
            for c in row:
                c.border = border
    wb.save(out_path)
    print(f"OK: wrote {out_path} with {len(wb.sheetnames)} sheets")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("usage: build_xlsx.py spec.json out.xlsx", file=sys.stderr)
        sys.exit(2)
    build(sys.argv[1], sys.argv[2])
