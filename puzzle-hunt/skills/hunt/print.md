# /hunt print — Print Production & PDF Generation

Generates print-ready files for all puzzle hunt materials. Output is HTML with print CSS — open in any browser and Print → Save as PDF. No special tooling required.

## Usage

```
/hunt print puzzle <id>       — generate print-ready HTML for one puzzle
/hunt print all               — generate all puzzle pages as a batch
/hunt print cover             — generate hunt cover page / welcome packet
/hunt print manual            — generate a themed "game manual" style booklet
/hunt print props             — generate all prop labels and tags
/hunt print kit               — full print kit: all puzzles + cover + props
/hunt print checklist         — what still needs to be printed before the event
```

---

## Output Structure

All print files go to `delivery/print/`:

```
delivery/print/
├── puzzles/
│   ├── P01-[name].html
│   ├── P02-[name].html
│   └── ...
├── props/
│   ├── labels-[prop-name].html    ← one sheet per prop type
│   └── tags-team-kits.html        ← one sheet for team kit labels
├── cover.html
├── manual.html                    ← optional game manual / flavor booklet
└── PRINT-CHECKLIST.md
```

---

## Puzzle Page Layout

Each puzzle page is a single HTML file with print CSS. Sections:

```
┌─────────────────────────────────────────────┐
│  [Hunt logo/name]              [Puzzle title] │
│  [Round name]                  [Puzzle ID]    │
├─────────────────────────────────────────────┤
│                                               │
│  [Flavor text / narrative hook]               │
│                                               │
├─────────────────────────────────────────────┤
│                                               │
│  [Puzzle content — grid, clues, worksheet]    │
│                                               │
│                                               │
├─────────────────────────────────────────────┤
│  Answer: __ __ __ __ __ __ __                 │
│  [QR code → website answer submission]        │
└─────────────────────────────────────────────┘
```

**Print specs:**
- Page size: Letter (8.5×11) or A4 — configurable in theme
- Margins: 0.75in all sides
- Font: readable at 11pt minimum
- Images: 300dpi equivalent or SVG only
- Color: design for both color and B&W printing (don't rely on color alone)
- QR code: links to `[site-url]/submit/[puzzle-id]`

---

## /hunt print puzzle <id>

Reads:
- `puzzles/[id]/puzzle.md` — puzzle content
- `scenarios/[hunt]/SCOPE.md` — hunt name, theme
- `delivery/THEME.md` — visual theme (fonts, colors, logo)

Generates `delivery/print/puzzles/[id]-[name].html` with:
1. Hunt header and puzzle title
2. Flavor text (from puzzle brief)
3. Puzzle content formatted for print (grids, tables, worksheets)
4. Answer blanks + QR code
5. Print CSS: page breaks, no nav elements, correct margins

---

## /hunt print props

Reads `delivery/props/PROPS.md` (see `/hunt props`).

Generates label sheets — one HTML file per prop type, formatted for:
- **Avery 5160** (1×2.625in, 30-up) — small labels for items
- **Avery 5163** (2×4in, 10-up) — larger labels for envelopes, boxes
- **Tent cards** — folded table cards for teams
- **Tags** (3×5in with hole punch) — for physical objects

Each label contains:
- Team name (if team-specific)
- Item name and ID
- Hunt-themed decoration (border, icon)
- Instructions if needed (e.g., "Open when you solve Puzzle 3")

---

## /hunt print manual

For fictional-world hunts, generates a themed "in-universe" document.

For IRONFALL: the original 1993 game manual — a printable booklet with:
- Character bios (actually puzzle flavor)
- "How to play" section (actually puzzle instructions in disguise)
- Maps, bestiary entries, item descriptions
- Back cover with copyright notice (fictional publisher, fictional year)

Format: A5 booklet (two A5 pages per A4 sheet, folded). Or standard letter.

---

## Theme File

`delivery/THEME.md` defines the visual language used across all print output:

```markdown
# [Hunt Name] — Print Theme

**Font (body):** [name] — [fallback]
**Font (headers):** [name] — [fallback]
**Primary color:** #[hex]
**Secondary color:** #[hex]
**Background:** #[hex] (use white for B&W printing)
**Logo:** delivery/assets/logo.[svg|png]
**Page border:** [none | thin rule | decorative]
**Flavor:** [one sentence — the aesthetic, e.g., "pixel art, CRT scanlines, 8-bit"]

## CSS Overrides
[any custom CSS rules for the hunt's look]
```

---

## Print Checklist

`/hunt print checklist` reads all puzzle statuses and prop inventory, then outputs:

```
PRINT CHECKLIST — [Hunt Name]

Puzzles (N teams × M pages each)
  [ ] P01 — [name]         N copies     delivery/print/puzzles/P01-name.html
  [ ] P02 — [name]         N copies     delivery/print/puzzles/P02-name.html
  ...

Props
  [ ] Cipher wheels        N sets       delivery/print/props/labels-cipher-wheels.html
  [ ] Team kit labels      N sets       delivery/print/props/tags-team-kits.html
  ...

Other
  [ ] Cover / welcome      N copies     delivery/print/cover.html
  [ ] Game manual          N copies     delivery/print/manual.html  [if applicable]

Total estimated print jobs: N pages × N teams
```
