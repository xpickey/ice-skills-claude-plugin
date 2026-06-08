# Reference 06 — Slide Layouts (The 12 Canonical Patterns)

This reference catalogs the 12 foundational slide layouts used in professional B2B PowerPoint decks. Each layout is optimized for a specific purpose and designed to work with any industry theme.

**Critical principle:** Never use the same layout in consecutive slides. Monotony is the most visible tell of an AI-generated deck. Mix text-heavy and visual-heavy; vary the visual weight and information density.

---

## Intro — Layout Variety Rules

The human eye notices repetition faster than it notices color or typography. A deck that cycles through the same three layouts will feel assembled, not authored.

**Essential rules:**
- No layout appears twice in a row (ever).
- No layout appears three times in a row, even non-consecutively (e.g., slides 2, 4, 6).
- Alternate between text-dominant and visual-dominant layouts within every 3–5 slides.
- Title slides and section dividers always use **Title Hero**.
- Workflow diagrams and dashboard slides always own their own slide; never share with body text.
- Use **Stat Callout** sparingly: once per 5 slides maximum (otherwise loses dramatic impact).

**The anti-pattern:** "Slide 1 Two-Column, Slide 2 Two-Column, Slide 3 Icon Rows, Slide 4 Two-Column" feels robotic.

**The pattern:** "Slide 1 Two-Column, Slide 2 Stat Callout, Slide 3 Icon Rows, Slide 4 Process Flow, Slide 5 Half-Bleed Image" feels authored.

---

## The 12 Layouts

### 1. Title Hero

**Purpose:** Opening slide of every deck. Sets tone, establishes theme, signals professionalism.

**When to use:** Slide 1 only (unless using section dividers).

**Wireframe:**
```
┌─────────────────────────────────────┐
│                                     │
│  [ACCENT COLOR BLOCK or IMAGE]      │
│                                     │
│     Company Name / Logo             │
│     HEADLINE (60–72pt)              │
│     Subheadline (24–28pt, muted)    │
│     Date / Presenter Name (footer)  │
│                                     │
└─────────────────────────────────────┘
```

**Grid:**
- Canvas: 13.33" × 7.5" (16:9)
- Margins: 0.5" all sides
- Accent block (left or full-bleed): 7–13" wide
- Text column (right or overlay): 5–6" wide

**Element count:**
- Headline: 1 line (max 12 words)
- Subheadline: 1–2 lines (optional)
- Visual: 1 hero image or color block (not multiple small images)

**Variants:**
- Full-bleed image with text overlay (text on semi-transparent dark box)
- Split layout: accent color block left, headline right
- Centered text over hero image (use sparingly; requires high contrast)
- Dark theme variant: full-bleed dark image, light text overlay

**Anti-patterns:**
- Headline + subheadline + 3 body bullets (too much text)
- Multiple decorative elements competing with headline
- Small logo in corner (logo should be 0.5–0.75" wide, integrated or omitted)
- Decorative line under the title (signals AI-generated)

---

### 2. Two-Column

**Purpose:** Introduce a concept with text on one side, illustration or chart on the other. Workhorse of most decks.

**When to use:** Concept explanation, feature introduction, problem–solution pairs.

**Wireframe:**
```
┌────────────────┬────────────────┐
│                │                │
│   TITLE        │                │
│                │  [ILLUSTRATION]│
│  • Bullet 1    │   or CHART     │
│  • Bullet 2    │                │
│  • Bullet 3    │                │
│  • Bullet 4    │                │
│                │                │
└────────────────┴────────────────┘
```

**Grid:**
- Left column: 5.5"–6" wide (title + bullets)
- Right column: 5.5"–6" wide (image or chart)
- Inter-column gutter: 0.33"
- Top margin (title): 0.5"
- Body starts 2" from top

**Element count:**
- Title: 1 line (max 10 words)
- Bullets: 3–5 items (max 10 words per bullet)
- Right-side visual: 1 illustration, chart, or icon set
- Max text per slide: ~80 words body + title

**Variants:**
- Image left, text right (less common but acceptable)
- 1/3–2/3 split (emphasize image or text depending on content)
- Right-side visual is small UI mockup, diagram, or simple icon
- Text background: light fill (0.25" padding) to separate from image

**Anti-patterns:**
- Text wraps under the image (layout breaks at smaller projections)
- Image too small (should occupy >45% of slide)
- Bullet text >2 lines (words should be 8–12 per bullet max)
- Icon + illustration both on right side (too crowded)

---

### 3. Stat Callout (Large Number)

**Purpose:** Highlight a single dramatic statistic. High-impact, minimal information density.

**When to use:** Opening a new section, answer to a pain question, dramatic proof point. Use sparingly (max 1 per 5 slides).

**Wireframe:**
```
┌─────────────────────────────────────┐
│                                     │
│         [OPTIONAL LABEL]            │
│                                     │
│             78%                     │
│         [LARGE NUMBER]              │
│                                     │
│      of enterprises report          │
│      faster time-to-market          │
│                                     │
│      [Optional 1-line context]      │
│                                     │
└─────────────────────────────────────┘
```

**Grid:**
- Canvas: 13.33" × 7.5"
- Number: centered, 72–96pt, primary theme color
- Label / description: 14–18pt, muted color
- Context line (optional): 12–14pt, center or left-aligned
- Margins: 1" top/bottom, 0.5" sides

**Element count:**
- Number: 1 (e.g., "78%", "$2.3B", "4 weeks")
- Label: 1 line (max 8 words)
- Context: 1 line (max 12 words, optional)
- Visual: 1 accent color block or minimal icon (optional; not required)

**Variants:**
- With subtle background shape (circle, rectangle, curved accent)
- Dark slide with light number (high contrast)
- Small icon above number (e.g., growth arrow, checkmark)
- Two supporting sub-stats below main number (smaller font, secondary color)

**Anti-patterns:**
- Number too small (70pt minimum)
- Multiple numbers on one slide (reduces impact; use **Stat Callout Grid** instead)
- Bullet points below the stat (defeats purpose; use Two-Column instead)
- Decorative gradient or shadow behind number

---

### 4. Stat Callout Grid

**Purpose:** Show 2x2 or 1x3 statistics at equal visual weight.

**When to use:** Multi-metric summary (e.g., financial dashboard, key metrics slide).

**Wireframe:**
```
┌─────────────────┬─────────────────┐
│     58%         │     $14M        │
│  Customer       │   Annual        │
│  Retention      │   Growth        │
├─────────────────┼─────────────────┤
│     3.2x        │     92 days     │
│  Payback        │   Implementation│
│  Period         │   Cycle         │
└─────────────────┴─────────────────┘
```

**Grid:**
- 2x2 layout: 4 cells, each ~5.5" × 3.5"
- 1x3 layout: 3 cells, each ~4" wide
- Borders: light grey (0.5pt) or none
- Cell padding: 0.3"–0.5"
- Center all content within cells

**Element count:**
- Per cell: 1 large number (48–56pt), 1 label (14–16pt)
- Total per slide: 4 or 6 stats

**Variants:**
- Colored backgrounds per cell (primary color family)
- Small sparkline or trend arrow per stat
- Alternating cell backgrounds (checkerboard)
- 3-column layout for horizontal emphasis

**Anti-patterns:**
- Unequal cell sizes
- More than 6 stats on one slide (loses readability)
- Mixed units without clear category labels
- Decorative icons cluttering the cells

---

### 5. Icon + Text Rows

**Purpose:** List capabilities, agenda items, or process steps as vertical rows. Excellent for "what we do" and meeting agendas.

**When to use:** Feature lists, capability overviews, agenda, checklist of deliverables.

**Wireframe:**
```
┌──────────────────────────────────────┐
│  TITLE                               │
├──────────────────────────────────────┤
│ [ICON]  Bold Header                  │
│         One-line description text    │
│                                      │
│ [ICON]  Bold Header                  │
│         One-line description text    │
│                                      │
│ [ICON]  Bold Header                  │
│         One-line description text    │
│                                      │
│ [ICON]  Bold Header                  │
│         One-line description text    │
└──────────────────────────────────────┘
```

**Grid:**
- Icon size: 0.5"–0.75" (consistent across all rows)
- Icon + text left margin: 0.75"
- Row height: 1.2"–1.5" with 0.3" between rows
- Text column width: 5.5" (wraps description to 1 line max)

**Element count:**
- Rows: 3–5 per slide
- Per row: 1 icon, 1 bold header (max 6 words), 1 description (max 12 words, 1 line)
- Title: 1 line (max 10 words, optional but recommended)

**Variants:**
- Icon position: left aligned, center, or left-margin indent
- Icon colors: all primary, or color per row (use theme accent sparingly)
- Background: light tinted rows, or solid backgrounds
- Horizontal divider line between rows (optional)

**Anti-patterns:**
- Inconsistent icon sizes
- Description text >1 line (forces reader to work)
- Icons that don't relate to the text (visual noise)
- All 5 rows using different icon styles (should be from one set)

---

### 6. 2x2 Grid

**Purpose:** Compare or contrast four equal concepts. Matrix views, decision frameworks, competitive positioning.

**When to use:** Framework quadrants, 2x2 matrices (impact / effort, cost / speed), comparison sets.

**Wireframe:**
```
┌──────────────────┬──────────────────┐
│   QUADRANT 1     │   QUADRANT 2     │
│  [Icon/Concept]  │  [Icon/Concept]  │
│  • Attribute     │  • Attribute     │
│  • Attribute     │  • Attribute     │
├──────────────────┼──────────────────┤
│   QUADRANT 3     │   QUADRANT 4     │
│  [Icon/Concept]  │  [Icon/Concept]  │
│  • Attribute     │  • Attribute     │
│  • Attribute     │  • Attribute     │
└──────────────────┴──────────────────┘
```

**Grid:**
- Quadrants: 5.5" × 3.25" each (with 0.33" gutter between)
- Centered heading per quadrant: 16–18pt bold
- Body text per quadrant: 12–14pt, 2–3 bullets max
- Dividing lines: primary color (1.5pt) or light grey (0.5pt)
- Padding within quadrant: 0.4"

**Element count:**
- Per quadrant: 1 title, 1 icon, 2–3 bullet points
- Total per slide: 4 quadrants (no more)

**Variants:**
- Colored background per quadrant (related color family)
- Small metric/number in corner of each quadrant
- Icons only (no text) for simplified concept map
- Axis labels at edges (e.g., "Low Cost / High Speed")

**Anti-patterns:**
- Unequal quadrant text density (one has 5 bullets, one has 1)
- Quadrant background colors too saturated (readability)
- Text size varies widely within grid
- Decorative images in quadrants

---

### 7. 2x3 / 3x2 Grid

**Purpose:** Show six related items (pain points, features, capabilities, use cases).

**When to use:** Pain point matrices, feature sets, use-case gallery, before-and-after pairs.

**Wireframe:**
```
┌──────────┬──────────┬──────────┐
│ ITEM 1   │ ITEM 2   │ ITEM 3   │
│ [Icon]   │ [Icon]   │ [Icon]   │
│ Label    │ Label    │ Label    │
├──────────┼──────────┼──────────┤
│ ITEM 4   │ ITEM 5   │ ITEM 6   │
│ [Icon]   │ [Icon]   │ [Icon]   │
│ Label    │ Label    │ Label    │
└──────────┴──────────┴──────────┘
```

**Grid:**
- Cell size (3-column): 3.5" × 2.8" each
- Cell size (2-column): 5.5" × 2.8" each
- Gutter: 0.33" between cells
- Content per cell: centered title (14–16pt), icon (0.5"–0.75"), label (12pt)

**Element count:**
- Per cell: 1 icon, 1 label (max 3 words)
- Total per slide: 6 items

**Variants:**
- Alternating cell background colors
- Small checkmark or badge in corner (status indicator)
- Left label + right icon (horizontal alignment)
- Color-coded per category

**Anti-patterns:**
- Text wraps in cells (keep labels to 1 line)
- Icons vary in size across grid
- >6 items (use multiple slides instead)
- Mixed icon styles

---

### 8. Half-Bleed Image

**Purpose:** Dramatic visual statement with light text overlay or adjacent text block.

**When to use:** Case study openings, customer testimonials, environmental or context-setting, product showcase.

**Wireframe (Image Left):**
```
┌─────────────────────┬───────────────┐
│                     │  Title        │
│                     │  Subheading   │
│  [FULL-BLEED IMAGE] │               │
│  (left half, no     │  • Bullet 1   │
│   margin)           │  • Bullet 2   │
│                     │  • Bullet 3   │
│                     │               │
└─────────────────────┴───────────────┘
```

**Grid:**
- Image side: 6.66"–7" wide, full height (0 margin touching edge)
- Text side: 5.67"–6" wide, standard margins (0.5")
- No gap between image and text (seamless)
- Image top aligns with slide top (extends to edge)

**Element count:**
- Image: 1 hero photograph or illustration
- Title: 1 line (max 10 words)
- Text: 3–5 bullets (or narrative paragraph, max 40 words)
- Optional: small logo, watermark, or data source citation

**Variants:**
- Image on right, text on left
- Image full-bleed with text overlay (dark semi-transparent box behind text)
- Bottom-bleed variant (image bottom half, text top half)
- Curved or diagonal dividing line (risky; use rarely)

**Anti-patterns:**
- Image and text competing for visual dominance
- White/light text on bright areas of image (illegible)
- Image with visible watermarks or low resolution
- Text positioned too close to image edge (crowded)

---

### 9. Process Flow (Numbered Steps)

**Purpose:** Show sequential process, timeline, or methodology with 3–5 steps.

**When to use:** Implementation roadmap, onboarding flow, methodology steps, decision tree.

**Wireframe:**
```
┌────────┐   ┌────────┐   ┌────────┐
│   1    │──→│   2    │──→│   3    │
│ STEP   │   │ STEP   │   │ STEP   │
│ Description   Description   Description
└────────┘   └────────┘   └────────┘
```

**Grid:**
- Step box: 1.2" × 1.2" (circles or squares)
- Step number: 36–48pt, centered
- Connector arrow: 0.33" long (primary color, 2–3pt stroke)
- Description text: 11–12pt, center or left-aligned below box
- Horizontal spacing: 1.5"–2" between boxes

**Element count:**
- Steps: 3, 4, or 5 (not more)
- Per step: 1 number, 1 label (max 2 words), 1 description (max 12 words, 1 line)
- Title: optional (1 line, top of slide)

**Variants:**
- Vertical flow (steps stacked top-to-bottom)
- Step box colors: primary, secondary, accent (cycling)
- Icons inside step boxes instead of numbers
- Timeline variant: steps with durations (e.g., "Week 1–2", "Week 3–4")

**Anti-patterns:**
- Step boxes too small for text (unreadable)
- Arrows pointing inconsistent directions
- Description text >1 line (breaks flow)
- >5 steps (use multiple slides or Phased Timeline)

---

### 10. Workflow Diagram

**Purpose:** Show system architecture, data flow, or organizational structure with boxes and connecting lines.

**When to use:** Technical architecture, integration diagrams, org charts, process maps with swim lanes.

**Wireframe:**
```
    ┌──────────┐
    │ Input    │
    └────┬─────┘
         │
    ┌────▼─────┐
    │ Process  │
    │ Layer    │
    └────┬─────┘
         │
    ┌────▼─────┐
    │ Output   │
    └──────────┘
```

**Grid:**
- Box size: variable (1.5"–3" wide depending on content)
- Connector lines: 1.5–2pt stroke, primary color
- Labels on lines: 10–11pt, positioned above line
- Padding within boxes: 0.2"–0.3"
- Vertical spacing between layers: 0.75"–1"

**Element count:**
- Boxes: 4–8 per slide (not more; use multiple slides for large systems)
- Per box: 1 title (bold, 12–14pt), optional description (11pt, 1 line max)
- Connector lines: as many as needed to show relationships
- Optional: color-coding by category, legend

**Variants:**
- Swim lanes (horizontal or vertical sections for different teams/systems)
- Circular flow diagram (inputs and outputs loop back)
- Data flow diagram (labeled arrows: "user input", "API call", etc.)
- Org chart layout (hierarchical, boxes at different levels)

**Anti-patterns:**
- >8 boxes on one slide (visual overload; split into two slides)
- Crossing connector lines without clear purpose
- Inconsistent box sizes
- Text inside boxes >2 lines (breaks visual clarity)

---

### 11. Phased Timeline

**Purpose:** Show multi-phase implementation, roadmap, or project schedule across months or quarters.

**When to use:** Project roadmap, contract service delivery, product launch phases, year-over-year plan.

**Wireframe:**
```
├────────────────────────────────────┤
│  PHASE 1   │   PHASE 2   │  PHASE 3 │
│ (Q1–Q2)    │   (Q3)      │  (Q4)    │
│ • Prep     │  • Deploy   │  • Ops   │
│ • Design   │  • Train    │  • Opti  │
│ [Owner]    │  [Owner]    │  [Owner] │
└────────────┴─────────────┴──────────┘
```

**Grid:**
- Phase column width: proportional to duration (e.g., 8 weeks vs. 4 weeks)
- Phase heading: 14–16pt bold
- Duration label: 11–12pt muted (e.g., "Weeks 1–4")
- Content per phase: 2–3 bullet points (max 8 words each)
- Optional owner name: 10–11pt, bottom of phase box
- Vertical dividers: primary color (1pt) or light grey (0.5pt)

**Element count:**
- Phases: 3–5 per slide
- Per phase: 1 title, 2–3 bullets, optional owner name
- Total text per slide: ~40 words max

**Variants:**
- Milestone markers (diamond shapes at key dates)
- Color per phase (cycle through theme palette)
- Dependency arrows between phases
- Effort/resource indicator per phase (small bar chart)

**Anti-patterns:**
- Phase columns with vastly different widths (misrepresents duration)
- Bullet text >8 words (requires reading effort)
- >5 phases (use Dashboard or multiple slides)
- Milestone dates without visual emphasis

---

### 12. Dashboard / Scorecard

**Purpose:** Display metrics, KPIs, or performance snapshot in a grid. Best for quarterly reviews, status reports, and executive summaries.

**When to use:** QBR slides, executive dashboard, health scorecard, balanced metrics summary.

**Wireframe:**
```
┌──────────┬──────────┬──────────┐
│ Revenue  │ Churn    │ NPS      │
│ $12.4M   │ 2.1%     │ 52       │
│ +8% MoM  │ -0.3%    │ +4 pts   │
├──────────┼──────────┼──────────┤
│ Headcount│ Pipeline │ Win Rate │
│ 342      │ $45M     │ 28%      │
│ +12      │ +$8M     │ +3%      │
└──────────┴──────────┴──────────┘
```

**Grid:**
- Tile size: 3" × 2.5" (3 columns × 2 rows, max 6 tiles)
- Tile padding: 0.25"–0.3"
- KPI value: 36–48pt, primary color
- KPI label: 12–13pt muted
- Trend indicator: small arrow/sparkline (11pt) or color-coded +/- (green/red)
- Tile background: light fill (primary color @ 5% opacity) or white with border

**Element count:**
- Tiles: 4–6 per slide (cap at 6; layout breaks at 7+)
- Per tile: 1 KPI label, 1 value, 1 trend/direction (optional)

**Variants:**
- Status-coded colors (green/yellow/red for on-track / at-risk / off-track)
- Small chart per tile (sparkline, mini bar chart)
- Category headers above tile groups (e.g., "Revenue Metrics", "People Metrics")
- Linear gauge (horizontal bar) showing % to goal

**Anti-patterns:**
- >6 tiles per slide
- Trend directions unclear (always show + or -)
- Tile sizes vary
- Confusing color coding (must be intuitive)

---

## Layout Decision Matrix

Use this table to match your deck type and slide purpose to a layout.

| Slide Purpose | Title Hero | Two-Column | Stat Callout | Icon Rows | 2x2 Grid | 2x3 Grid | Half-Bleed | Process | Workflow | Timeline | Dashboard |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Deck opening / section divider | ✓ | | | | | | | | | | |
| Introduce concept w/ visual | | ✓ | | | | | | | | | |
| Dramatic proof point / metric | | | ✓ | | | | | | | | |
| Multi-metric summary | | | | | | ✓ | | | | | ✓ |
| Feature / capability list | | | | ✓ | | ✓ | | | | | |
| Compare quadrants / matrix | | | | | ✓ | | | | | | |
| Problem–solution pair | | ✓ | | | ✓ | | ✓ | | | | |
| Implementation roadmap | | | | | | | | ✓ | | ✓ | |
| System / architecture | | | | | | | | | ✓ | | |
| Org structure / swim lanes | | | | | | | | | ✓ | | |
| Project timeline | | | | | | | | | | ✓ | |
| Health / KPI snapshot | | | | | | | | | | | ✓ |
| Customer case study | | ✓ | | | | | ✓ | | | |
| Meeting agenda | | | | ✓ | | | | | | | |
| Risk or pain matrix | | | | | ✓ | ✓ | | | | | |

---

## Global Mixing Rules

**Rule 1: No Layout Repetition**
Never use the same layout in slides N and N+1. Violation instantly signals AI generation.

**Rule 2: Variety Within 5 Slides**
Within any 5-slide window, deploy at least 3 different layouts. This ensures flow and maintains visual interest.

**Rule 3: Balance Visual Weight**
Alternate text-heavy (Two-Column, Icon Rows, process descriptions) with visual-heavy (Half-Bleed, Workflow, Stat Callout).

**Rule 4: Max Stat Callout Frequency**
Use Stat Callout once per 5 slides. Overuse dilutes impact.

**Rule 5: Dedicated Slides**
Workflow Diagrams, Dashboard Scorecards, and Phased Timelines own their own slide. Never combine a Workflow Diagram with body bullets, for example.

**Rule 6: Title Slide Exclusivity**
Title Hero is only for the deck opening. Section dividers may use it, but sparingly (e.g., every 10 slides or at major section breaks).

---

## Spacing & Grid (Universal)

**Canvas:**
- 16:9 widescreen: 13.33" wide × 7.5" tall (standard)
- 4:3 legacy: 10" wide × 7.5" tall (only if projector requires; rare)

**Margins:**
- All sides: 0.5" minimum
- Title area: top 0.5" to 2"
- Body area: 2" to 6.5"
- Footer area: bottom 0.3" (page number, date, footer text)

**Inter-element spacing:**
- Between title and body: 0.25"–0.5"
- Between body sections: 0.3"–0.5"
- Between rows (Icon Rows, grid): 0.2"–0.3"

**12-column grid alignment (for pixel-perfect work):**
- Column width on 16:9: 13.33" / 12 = 1.06" per column
- Use this for aligning icons, text blocks, images across slides
- Most users will never be this precise, but design teams often use it

---

## Common Layout Mistakes (Anti-Patterns)

1. **Title too close to body text** — leaves no breathing room. Result: crowded, hard to read.
   - **Fix:** Always 0.5" minimum between title and body text.

2. **Two-Column with text wrapping under image** — layout collapses on projectors or exports.
   - **Fix:** Ensure text and image are truly side-by-side; text box width = column width.

3. **Icons inconsistent in size** (Icon Rows layout) — screams "assembled, not designed."
   - **Fix:** All icons same size, same style, from one icon set.

4. **Process Flow boxes too small** — numbers or step labels unreadable at 10 feet.
   - **Fix:** Minimum box 1.2" × 1.2"; font size 28pt minimum for number.

5. **Dashboard with 8+ KPIs** — exceeds cognitive load, loses purpose.
   - **Fix:** Cap at 6 tiles; split into two slides if more are needed.

6. **Half-Bleed Image colliding with text** — image/text edges too close, unreadable text.
   - **Fix:** Ensure 0.3"–0.5" padding between image edge and text start.

7. **Decorative line under title** — classic AI-generated tell.
   - **Fix:** Use color blocks or section dividers instead; thin horizontal rules feel dated.

8. **Stat Callout with body bullets** — defeats purpose of high impact.
   - **Fix:** Stat Callout owns the slide; pair with optional 1-line context only.

9. **Grid cells with unequal text density** — one cell has 5 bullets, another has 1 word.
   - **Fix:** Balance information per cell (visually and informationally).

10. **Mixing icon styles in one layout** — some filled, some outlined, different visual language.
    - **Fix:** Use icons from a single set (e.g., Feather, Heroicons, or system icons from the theme library).

---

**End of 06-layouts.md.** Continue to `07-color-system.md` for 60-30-10 application, or `05-typography.md` for font pairing rules.
