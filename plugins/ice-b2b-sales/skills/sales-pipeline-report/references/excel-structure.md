# Excel Output Structure — iCE Sales Pipeline Summary Workbook

## Sheet Overview

| Sheet | Content |
|---|---|
| `Summary` | Total committed KPIs + category totals |
| `NetNew` | NetNew deals matrix by category × quarter |
| `Recurring` | Recurring revenue by product × category |
| `By BU` | NetNew breakdown by Business Unit (if data available) |
| `Deal List` | Full deal-level table with all fields |
| `Data Notes` | Data quality issues, assumptions, source file info |

---

## Sheet 1: Summary

```
Row 1:  iCE SALES PIPELINE SUMMARY — FY[YEAR] — As of [DATE]
Row 3:  Total Committed:  ฿XXX.XM     Total Deals: NNN
Row 4:  NetNew:           ฿XXX.XM     Recurring:   ฿XXX.XM
Row 6:  [4-column category summary table]
        Category | Total | Deals | NetNew | Recurring | Q1 | Q2 | Q3 | Q4
        WIN      | ...
        FOCUS    | ...
        ACTIVE   | ...
        EARLY    | ...
        TOTAL    | ...
```

**Formatting:**
- Header row: Navy background (#1A2332), white text, bold
- WIN row: Light green background
- FOCUS row: Light orange background
- ACTIVE row: Light blue background
- EARLY row: Light gray background
- Amount cells: Number format `฿#,##0.0,,M` or `฿#,##0`
- Conditional formatting on Total column: data bars

---

## Sheet 2: NetNew

Category × Quarter matrix:
```
         Q1        Q2        Q3        Q4        Total     Deals
WIN      ฿X.XM     -         -         -         ฿X.XM     N
FOCUS    ฿X.XM     ฿X.XM     -         -         ฿X.XM     N
ACTIVE   ฿X.XM     ฿X.XM     ฿X.XM     ฿X.XM     ฿X.XM     N
EARLY    ฿X.XM     ฿X.XM     ฿X.XM     ฿X.XM     ฿X.XM     N
TOTAL    ฿X.XM     ฿X.XM     ฿X.XM     ฿X.XM     ฿X.XM     N
```

---

## Sheet 3: Recurring

Product × Category matrix:
```
Product          | WIN | FOCUS | ACTIVE | EARLY | Total | Deals
SW Subscription  | ... | ...   | ...    | ...   | ...   | N
SW Maintenance   | ... | ...   | ...    | ...   | ...   | N
AMS Service      | ... | ...   | ...    | ...   | ...   | N
SW License       | ... | ...   | ...    | ...   | ...   | N
TOTAL            | ... | ...   | ...    | ...   | ...   | N
```

---

## Sheet 5: Deal List

Full normalized deal table with these columns:
```
Source Sheet | Company | Opportunity | Product/Service | BU (if available) |
Stage (Original) | Category (Mapped) | Revenue Type | Q1 | Q2 | Q3 | Q4 | Total |
Decommitted (Y/N) | Notes
```

- Filter dropdowns on all columns
- Freeze row 1
- Alternating row colors
- Sort by Category (WIN first) then Total descending

---

## Sheet 6: Data Notes

Document all data quality issues:
```
Issue          | Source Sheet | Description                        | Resolution
Duplicate AMS  | AMS          | AMS sheet = copy of Sale-SW        | Used prior file / ฿X.XM
Decommitted    | All          | N deals had Grand Total = 0        | Excluded from totals
Missing BU     | All          | BU column not in pivot export      | Grouped by Product as proxy
Unknown Stages | Imp-Service  | N rows had unrecognized stage names | Mapped to EARLY
```

Include source file name, version, and date of extract at top of sheet.

---

## Formatting Rules

- Column widths: auto-fit after population, minimum 1"
- Header rows: freeze, bold, colored background
- Amount format: `_-฿* #,##0_-` for Thai Baht; or `$#,##0` for USD
- Use `0.0,,M` format for millions display in summary sheets
- Borders: thin inner borders, medium outer borders per table
- Tab colors: Navy=Summary, Green=NetNew, Teal=Recurring, Blue=By BU, Gray=Deal List, Red=Data Notes
