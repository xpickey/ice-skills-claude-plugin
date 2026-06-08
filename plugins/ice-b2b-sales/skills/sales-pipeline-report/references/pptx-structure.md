# PowerPoint Structure — iCE Sales Pipeline Executive Deck

## Slide Overview (11 Slides)

| # | Slide | Content Type |
|---|---|---|
| 1 | Title | Hero KPIs + date |
| 2 | Executive Overview — Total Pipeline | KPI cards + charts |
| 3–6 | Stage Detail (WIN / FOCUS / ACTIVE / EARLY) | Table + insights |
| 7 | Executive Overview — NetNew Pipeline | KPI cards + charts |
| 8 | NetNew Detail | Matrix + top deals |
| 9 | Risks & Key Actions | Risk cards + action cards |
| 10 | NetNew by Business Unit | BU × Category × Quarter matrix |
| 11 | Recurring by Product/Service | Product × Category × Quarter matrix |

---

## Slide 1: TITLE

**Layout:** Dark background (Navy #1A2332), full bleed
**Content:**
- Company/report name (top-left, small, gray)
- Main title: "iCE Sales Pipeline Report" (large, white, Trebuchet MS Bold 40pt)
- Subtitle: Fiscal year + report date (orange #E8913A, 16pt)
- Two hero KPIs side-by-side:
  - Total Committed: `฿XXX.XM` — orange
  - NetNew Pipeline: `฿XXX.XM` — purple #8E44AD
- Footer: "Confidential — [Company Name]" (small, gray, bottom right)

---

## Slide 2: EXECUTIVE OVERVIEW — Total Pipeline

**Layout:** Light background, 2-section layout
**Top section:** 4 KPI cards (WIN | FOCUS | ACTIVE | EARLY)
- Each card: colored left border + icon + hero amount + deal count + NetNew/Recurring split

**Bottom section:** Two charts side-by-side
- LEFT: Stacked Bar — Total pipeline by quarter (Q1–Q4), stacked by category
- RIGHT: Doughnut — Pipeline by Service Type (Implementation / Software / AMS)

**Title bar:** Slate #2C3E50 background, white text "TOTAL PIPELINE OVERVIEW"

---

## Slides 3–6: Stage Detail (One per category)

**Template (repeat for WIN / FOCUS / ACTIVE / EARLY):**

**Header bar:** Category color + icon + name + total amount (right-aligned)

| Category | Color | Icon |
|---|---|---|
| WIN | #27AE60 Green | ✅ |
| FOCUS | #E8913A Orange | 🔥 |
| ACTIVE | #3498DB Blue | 🎯 |
| EARLY | #7F8C9B Gray | 🌱 |

**Body:** Deal table with columns:
```
Company | Opportunity Name | Product/Service | Stage | Q1 | Q2 | Q3 | Q4 | Total | Type
```
- Header row: slate background, white text
- Alternating rows: white / #F8F9FA
- Amount columns: right-aligned, colored by NetNew (purple) or Recurring (teal)
- Sort by Total descending

**Footer insight bar:** 2–3 key insights (e.g., "🔑 X deals need PO confirmation this quarter")

**Slide title:** "[CATEGORY] — [N] Deals | NetNew ฿XX.XM | Recurring ฿XX.XM"

---

## Slide 7: EXECUTIVE OVERVIEW — NetNew Pipeline ⭐

**Same structure as Slide 2 but filtered to NetNew deals only**

- 4 KPI cards showing NetNew amounts per category
- LEFT chart: Stacked Bar — NetNew by quarter, stacked by category
- RIGHT chart: Doughnut — NetNew by Business Unit (or Product if BU unavailable)

---

## Slide 8: NETNET DETAIL ⭐

**Two panels:**

**LEFT: Category × Quarter Matrix**
```
         Q1      Q2      Q3      Q4      Total
WIN      ฿X.XM   —       —       —       ฿X.XM
FOCUS    ฿X.XM   ฿X.XM   —       —       ฿X.XM
ACTIVE   ฿X.XM   ฿X.XM   ฿X.XM   ฿X.XM   ฿X.XM
EARLY    ฿X.XM   ฿X.XM   ฿X.XM   ฿X.XM   ฿X.XM
TOTAL    ฿X.XM   ฿X.XM   ฿X.XM   ฿X.XM   ฿X.XM
```

**RIGHT: Top 10 NetNew Deals**
```
Rank | Company | Opportunity | Category | Quarter | Amount
```

---

## Slide 9: RISKS & KEY ACTIONS

**Layout:** 3 + 3 card grid

**Risk cards (top row, red-tinted):**
1. Pipeline concentration risk (% in EARLY stage)
2. Q-end closing pressure (FOCUS deals in current quarter)
3. Data/coverage gap (e.g., missing BU, AMS data quality)

**Action cards (bottom row, green-tinted):**
1. Priority deals to accelerate to WIN this quarter
2. FOCUS deals requiring executive sponsor engagement
3. Pipeline coverage action (fill gaps in Q3/Q4)

**Bottom bar:** Single "Executive Bottom Line" sentence in orange

---

## Slide 10: NETNET BY BUSINESS UNIT

**Full-width matrix table:**
```
BU          | WIN        | FOCUS      | ACTIVE     | EARLY      | Q1    | Q2    | Q3    | Q4    | Total
BU Name 1   | ฿X.XM (N)  | ฿X.XM (N)  | ...
BU Name 2   | ...
TOTAL       | ...
```

**Note:** If BU data unavailable, group by Product/Service as proxy and note this in slide footer.

---

## Slide 11: RECURRING BY PRODUCT/SERVICE

**Full-width matrix table:**
```
Product          | WIN    | FOCUS  | ACTIVE | EARLY  | Total  | Deals
SW Subscription  | ...
SW Maintenance   | ...
AMS Service      | ...
SW License       | ...
TOTAL            | ...
```

Charts below table: Bar chart comparing recurring revenue by product type.

---

## Chart Specifications

### Stacked Bar (Quarterly)
```javascript
// pptxgenjs config
{
  type: 'bar',
  barDir: 'col',
  barGrouping: 'stacked',
  dataLabelFormatCode: '฿#,##0.0,,M',
  chartColors: ['#27AE60', '#E8913A', '#3498DB', '#7F8C9B'],  // WIN/FOCUS/ACTIVE/EARLY
  legendPos: 'b',
  showLegend: true,
  valAxisLabelFormatCode: '฿#,##0.0,,M'
}
```

### Doughnut Chart
```javascript
{
  type: 'doughnut',
  holeSize: 50,
  chartColors: ['#3498DB', '#8E44AD', '#E8913A'],  // Service types
  showLabel: true,
  showPercent: true,
  legendPos: 'b'
}
```
