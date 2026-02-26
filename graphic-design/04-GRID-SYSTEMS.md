# Grid Systems and Layout

## The Big Picture

```
+------------------------------------------------------------------+
|                    GRID SYSTEMS TAXONOMY                          |
|                                                                  |
|  MANUSCRIPT      COLUMN       MODULAR         HIERARCHICAL       |
|  (single block)  (multi-col)  (rows + cols)   (custom)           |
|                                                                  |
|  Books           Newspapers   Magazines       Posters            |
|  Reports         Web layouts  Catalogs        Annual reports     |
|  Long-form text  Dashboards   Complex docs    Editorial spread   |
|                                                                  |
|  COMPLEXITY --------------------------------------------->        |
|  FLEXIBILITY <---------------------------------------------      |
|                                                                  |
|  All grids share: margins, columns, gutters, baselines           |
+------------------------------------------------------------------+
```

---

## Grid Anatomy

Every grid is built from the same vocabulary:

```
+--MARGIN--+--COLUMN--+--GUTTER--+--COLUMN--+--MARGIN--+
|          |          |          |          |          |
|          |  Content |  Space   |  Content |          |
|          |  lives   |  between |  lives   |          |
|          |  here    |  columns |  here    |          |
|          |          |          |          |          |
+----------+----------+----------+----------+----------+

MARGIN     White space between content and page edge
           Creates breathing room; protects from binding

COLUMN     Vertical zone for content
           Width determines: text measure, image size

GUTTER     Gap between columns
           Keeps content visually separate
           Too narrow = columns read as one

BASELINE   Horizontal line on which text sits
GRID       Repeating horizontal divisions
           Sets vertical rhythm: all elements snap to
           a common vertical unit

FLOWLINES  Horizontal lines dividing layout into bands
           (used in modular grids)
```

---

## Grid Type 1: Manuscript Grid

The simplest grid. One content block per page.

```
+---------------------------+
|  MARGIN                   |
|  +---------------------+  |
|  |                     |  |
|  |   TEXT BLOCK        |  |
|  |                     |  |
|  |   (One column)      |  |
|  |                     |  |
|  |   Books, reports,   |  |
|  |   academic papers   |  |
|  |                     |  |
|  +---------------------+  |
|  MARGIN                   |
+---------------------------+

KEY DECISIONS:
  Margin proportions (inner/outer/top/bottom)
  Text measure (column width in characters: 65-75 optimal)
  Leading (line spacing: typically 120% of type size)

CLASSICAL MARGIN PROPORTIONS (Van de Graaf canon):
  Inner: 1 unit
  Top:   1.5 units
  Outer: 2 units
  Bottom: 3 units

  These are not arbitrary -- they derive from
  folded-page geometry going back to medieval manuscripts.
```

---

## Grid Type 2: Column Grid

Multiple vertical columns. Content can span one or more.

```
2-COLUMN                3-COLUMN              6-COLUMN
+-----------+           +----+----+----+      (flexible)
|     |     |           |    |    |    |
| col | col |           | 1  | 2  | 3  |      Can combine:
|     |     |           |    |    |    |      1+1+1 = narrow
|     |     |           | OR |    |    |      2+1   = asymmetric
+-----------+           |    | 1  +----+      3     = wide text
                        | col| wide    |
                        +----+---------+

ASYMMETRIC COLUMN GRIDS (common in Swiss design)
  2/3 + 1/3 split: main text left, notes/captions right
  1/4 + 3/4 split: navigation + content (web origin here)

WHY MULTI-COLUMN:
  Newspaper: many independent stories; column = story boundary
  Magazine: text + images interleave across columns
  Web: responsive (columns drop at narrow viewport)
```

---

## Grid Type 3: Modular Grid

Columns PLUS horizontal divisions = a field of cells.

```
+--+--+--+--+
|  |  |  |  |   Each module = one unit
+--+--+--+--+   Content occupies 1, 2, 3... modules
|  |  |  |  |
+--+--+--+--+   ADVANTAGES:
|  |  |  |  |   - Images can be precisely sized
+--+--+--+--+   - Consistent proportions throughout
|  |  |  |  |   - Complex layouts remain coherent
+--+--+--+--+

FILLING A MODULAR GRID:

+--+--+--+--+
|XXXXXXXX|  |    X = image spanning 2x2 modules
|XXXXXXXX|  |    o = small image (1x1)
+--+--+--+--+    T = text block
|T |o |T |T |
+--+--+--+--+
|T    |T |T |    Text spanning 2 modules
+-----+--+--+

The grid IS the invisible structure.
What the reader sees is the content, not the grid.
```

---

## Grid Type 4: Hierarchical / Organic Grid

Custom grid built from the content, not imposed on it.

```
HIERARCHICAL APPROACH:
  Not "here is a 4-column grid, fit content into it"
  But "here is the content; what structure does it demand?"

COMMON IN:
  Posters (single purpose, one read path)
  Annual reports (mixed content, prestige feel)
  Exhibition graphics (scale and space vary)
  Long-form editorial features

  +--------------------+
  | HEADLINE ZONE      |
  | (dominant)         |
  +--------------------+
  | | Main  | Sidebar  |
  | | text  | callout  |
  | |       | image    |
  +---------+----------+

  The columns here are determined by the relative importance
  of main text vs. sidebar -- not a preset unit system.
```

---

## Baseline Grid: Vertical Rhythm

Every well-composed layout has a baseline grid -- an invisible horizontal rhythm
that text and elements snap to.

```
SETTING UP A BASELINE GRID
---------------------------
Body type: 12pt
Leading: 15pt (line-height: 125%)
Baseline grid unit: 15pt

All other text must land on multiples of 15pt:
  Caption (9pt): 1 grid unit leading (fits 15pt)
  Body (12pt): 1 grid unit (15pt)
  Subhead (16pt): 2 grid units (30pt)
  Section head (24pt): 2 grid units (30pt) + top margin

  WHY THIS WORKS:
  Turn any page upside down. All text baselines
  on both sides of the spread will align.
  This is the "typographic color" of the page --
  consistent gray, no jumpy rhythm.

IN CSS (web equivalent):
  --baseline: 1.5rem;   (if body = 1rem = 16px, baseline = 24px)
  Use rem units and multiples: margin-top: 1.5rem, 3rem, etc.
```

---

## Constructing a Grid: Muller-Brockmann Method

```
STEP 1: Define format
  Page size: 210mm x 297mm (A4)

STEP 2: Define margins
  Top: 20mm  Bottom: 25mm  Inner: 20mm  Outer: 25mm
  Live area: 165mm x 252mm

STEP 3: Define number of columns
  For body text: measure should be ~65-75 characters
  At 9pt Helvetica: ~65 chars = ~50mm column width
  3 columns = 3 x 50mm + 2 gutters (5mm each) = 160mm (fits)

STEP 4: Define grid unit
  Column: 50mm wide
  Gutter: 5mm

STEP 5: Define baseline
  Body: 9/11pt  -> baseline unit: 11pt
  All rows in modular grid = multiple of 11pt

STEP 6: Document in a spec sheet
  This becomes the designer's constraint and the
  production team's instruction.
```

---

## Grid in Web Layout

The web grid evolved directly from print, then diverged.

```
PRINT -> WEB TRANSLATION
------------------------

Print: fixed page; absolute units (mm, pt)
Web:   fluid viewport; relative units (%, vw, rem)

EARLY WEB (1990s-2000s): No real grid
  Tables used for layout (hack)
  Fixed-width (760px for 800px monitors)

WEB FRAMEWORKS (2010s):
  Bootstrap, Foundation -> 12-column fluid grid
  960.gs -> 12/16/24 column grid systems

MODERN CSS GRID (2017+):
  grid-template-columns: repeat(12, 1fr)
  gap: 1.5rem

  .hero { grid-column: 1 / -1; }    /* full width */
  .main { grid-column: 1 / 9; }     /* 8 of 12 cols */
  .sidebar { grid-column: 9 / 13; } /* 4 of 12 cols */

RESPONSIVE GRID:
  Columns collapse at breakpoints:
  Desktop: 12 cols
  Tablet:  8 cols (or same 12 narrower)
  Mobile:  4 cols (or stack to 1)
```

---

## Layout Composition Principles

Grid provides structure; these principles govern what goes where:

```
VISUAL HIERARCHY
  Size + weight + color + position = reading order
  Reader enters at largest/most prominent element
  Moves to next in hierarchy
  Designer controls this sequence

  +----HEADLINE----+
  |  (primary)     |
  +----------------+
  SUBHEAD (secondary, smaller)
  Body text (tertiary, smallest)
  Caption (quaternary, smallest + different weight)

ENTRY POINT
  Every layout needs one dominant element.
  Swiss posters: one large photograph or abstract form.
  Magazine cover: one face, one dominant headline.
  Web homepage: one value proposition headline.

VISUAL FLOW
  Z-pattern (scanning): Top-left -> top-right -> bottom-left -> bottom-right
  F-pattern (reading): Top line -> left side scan -> bottom
  Both observed in eye-tracking studies.
  Design either accommodates or deliberately subverts these.

PROPORTION: THE GOLDEN RATIO
  phi = 1.618
  Rectangle: short side x phi = long side
  Used in margin proportions, image sizing, layout division
  Not mandatory, not magic -- but produces pleasing proportions
  because it appears throughout natural systems.
```

---

## White Space as a Design Element

```
PASSIVE WHITE SPACE        ACTIVE WHITE SPACE
-------------------        ------------------
Unintentional gaps         Deliberately placed breathing room
Happens when layout        Used to isolate elements, create
isn't filled deliberately  emphasis, signal premium quality

SIGNAL VALUE:
  Dense layout -> lots of information, affordable, busy
  Open layout  -> few key ideas, premium, calm

MAGAZINE EXAMPLE:
  Consumer magazine: dense columns, small margins, many ads
  Luxury magazine (Vogue, Wallpaper): large white space,
  single image per spread, big margins = quality signal

  White space is expensive (fewer words per page =
  more pages = more paper cost). Therefore it signals
  the publisher values quality over information density.
```

---

## Common Confusion Points

**"Grid = columns"** -- A grid includes margins, gutters, columns, AND baseline.
Columns alone are not a grid. Baseline grid is what separates professional work
from amateur layouts.

**"The content should determine the grid"** -- Partially. The grid should be
designed for the type of content, but once set, content conforms to it. Changing
the grid for each piece defeats the purpose (consistency, efficiency, system).

**"More columns = more flexibility"** -- A 12-column grid is flexible but
cognitively expensive. Simple content on a complex grid often looks worse than
simple content on a 3-column grid used well.

**"CSS grid and print grid are the same thing"** -- Same conceptual basis, different
execution. Print grids are fixed; web grids must handle variable viewport widths,
variable content lengths, and accessibility zoom. The principles transfer; the
implementation diverges.

---

## Decision Cheat Sheet

| Content type                           | Grid to use                     |
|----------------------------------------|---------------------------------|
| Long-form text (book, report)          | Manuscript grid                 |
| Newspaper, news site                   | 6-12 column                     |
| Magazine editorial spread              | Modular (4x4 or 6x6)            |
| Corporate brochure                     | 3-column + baseline             |
| Complex data dashboard                 | Modular grid                    |
| Poster or promotional piece            | Hierarchical / organic          |
| Web layout (multi-purpose)             | 12-column responsive            |
| Document with footnotes/marginalia     | Asymmetric 2/3 + 1/3            |
| Finding out why my layout looks wrong  | Check baseline grid first       |
