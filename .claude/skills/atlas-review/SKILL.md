# /atlas-review — Atlas SVG Design Review

Review atlas map files against the cartographic design spec. Invokes a 5-member design panel (Tufte, Vignelli, Wurman, Fuller, working cartographer) to evaluate SVG geographic maps, ASCII mechanism diagrams, and overall information design.

## Usage

```
/atlas-review map <number>           — review a single map (e.g., /atlas-review map 01)
/atlas-review section <N>            — review all 4 maps in a section (e.g., /atlas-review section I)
/atlas-review coastlines             — audit continent outline accuracy across all maps
/atlas-review status                 — summary of reviewed/unreviewed maps
```

---

## Design Authority

The panel derives from a prior design review (full text in `atlas/REVIEWS.md`):

| Reviewer | Focus |
|----------|-------|
| **Edward Tufte** | Data-ink ratio, chartjunk, label clarity, information density |
| **Massimo Vignelli** | Systematic grid, font hierarchy, family consistency across maps |
| **Richard Saul Wurman** | Information architecture, cross-references, dead links, reader wayfinding |
| **R. Buckminster Fuller** | Ocean as primary feature, systems thinking, longitude gap, global perspective |
| **Working Cartographer** | Coordinate accuracy, coastline fidelity, scale bars, projection math, glyph consistency |

---

## Reference Files

Before reviewing, the agent MUST read:

1. **Design spec**: `reference\.claude\skills\atlas-cartography\SKILL.md` — the full SVG style guide, coordinate protocol, glyph legend, and generation workflow
2. **Approved prototype**: `reference\atlas\_test_florida.html` — the gold-standard Florida SVG (light/warm style, `cy="-lat"` coordinate fix)
3. **Project plan**: `reference\PROJECTS.md` § Atlas — all 52 card-to-map assignments
4. **The map file(s)** being reviewed

---

## Two Visual Forms

The atlas uses a hybrid format. Each form has different review criteria:

### SVG Geographic Maps — Review Criteria

| # | Criterion | What to Check | Priority |
|---|-----------|---------------|----------|
| 1 | **Coordinate convention** | World maps: `x = longitude` (positive east, negative west), `y = -latitude`. Regional maps: `cx = -longitude`, `cy = -latitude` (per Florida prototype). No mixing. | P1 |
| 2 | **Coastline fidelity** | Continent outlines recognizable? India visible as distinct peninsula? Mediterranean separating Europe/Africa? Horn of Africa? Great Australian Bight? 25-30 control points per continent for world maps. | P1 |
| 3 | **Feature placement** | Cities, deserts, mountain ranges, etc. at correct real-world coordinates? Verify 3-5 key features against known positions. | P1 |
| 4 | **Light/warm palette** | Background `#faf8f5`, land `#e8e4dc`, strokes `#444` width 0.04-0.06 (regional) or 0.3-0.5 (world), labels `#333`/`#555`/`#777`, water labels `#a0b0c0` italic, grid `#e0ddd8`, features `#7a8a6a` italic. Font: Georgia, serif. | P2 |
| 5 | **Scale bar** | Present on every SVG. Math correct (1° longitude = 111 km × cos(latitude)). Tick marks and label. | P2 |
| 6 | **Grid lines** | Lat/lon grid at appropriate intervals (2-5° regional, 30° world). Labels on at least 2 edges. | P2 |
| 7 | **Legend** | Present if map uses color coding or symbols. Clean box, matches map symbology. | P2 |
| 8 | **Context coastlines** | Neighboring regions shown as dashed `stroke-dasharray` lines? Helps orient the reader without competing with primary content. | P3 |
| 9 | **viewBox** | Aspect ratio correct for the region? Width 800-960px? No wasted whitespace? Southern hemisphere not clipped if content requires it? | P2 |
| 10 | **Label collision** | No overlapping text? Labels readable at rendered size? Hierarchical font sizes (primary 3-3.5, secondary 2-2.5, annotation 1.5-2, lat/lon 2-2.5)? | P2 |

### ASCII Mechanism Diagrams — Review Criteria

| # | Criterion | What to Check | Priority |
|---|-----------|---------------|----------|
| 1 | **80-column width** | No lines exceed 80 characters. | P2 |
| 2 | **No `═══` frame borders** | Code block fence IS the frame. No decorative borders. | P2 |
| 3 | **Answers "WHY"** | Diagram explains a mechanism/process, not just locations. Cross-sections, circulation models, profiles. | P1 |
| 4 | **Glyph legend compliance** | Uses master glyph vocabulary from `00-OVERVIEW.md`. No invented symbols without justification. | P2 |
| 5 | **Consistent axis** | Latitude-band diagrams share the same vertical axis (90N top, 90S bottom) for cross-file comparison. | P2 |

---

## Common Coordinate Errors

These are the most frequent bugs. Check for all of them:

| Error | How to Detect | Example |
|-------|--------------|---------|
| **Eastern hemisphere negation** | Features east of Greenwich should have positive x in world maps. If Japan is at x=140 instead of x=-140 on a Pacific-centered map, it's in the Atlantic. | Ring of Fire SVG had Kamchatka at x=50 (Atlantic) instead of x=-160 (Pacific) |
| **Latitude sign flip** | In the `y = -latitude` convention, northern latitudes are negative y, southern are positive y. If Australia is at negative y, it's in the Arctic. | Florida prototype v1 had peninsula upside-down before cy=-lat fix |
| **Scale bar math** | 1° longitude = 111.32 × cos(lat) km. At 30°N: 96.4 km/°. At 60°N: 55.7 km/°. Don't use equatorial scale for high-latitude maps. | A 200 km bar at 30°N ≈ 2.08° (not 1.80°) |
| **viewBox clipping** | If content extends beyond the viewBox, it's invisible. Check that all labeled features fall within the viewBox range. | Star visibility map clipped at 35S, hiding Canopus |
| **Convention mixing** | Regional maps (Florida-style) use `x = -longitude`. World maps use `x = longitude`. Don't mix conventions within one SVG. | |

---

## Review Output Format

### Per-Map Review

```
ATLAS MAP REVIEW: 01-TECTONIC-PLATES.md
────────────────────────────────────────────────────────────────

SVG #1: World Plate Boundaries
  Coordinate convention:  ✓ correct (x=lon, y=-lat for world map)
  Coastline fidelity:     ✗ India missing, shapes crude (~18 pts/continent)
  Feature placement:      ✓ plate boundary positions reasonable
  Palette compliance:     ✓ light/warm, all colors match spec
  Scale bar:              ✓ present, math correct
  Grid + labels:          ✓ 30° intervals, labeled
  Legend:                 ✓ clean 3-type legend
  Overall:               NEEDS WORK — coastline resolution insufficient

SVG #2: Ring of Fire
  Coordinate convention:  ✗ BROKEN — western Pacific in wrong hemisphere
  ...
  Overall:               REDO — critical coordinate error

ASCII #1: Boundary Cross-Sections
  80-col width:           ✓
  No frame borders:       ✗ uses ═══ frame borders (lines 75, 127)
  Answers WHY:            ✓ explains divergent/convergent/transform mechanisms
  Glyph compliance:       ✓
  Overall:               PASS (remove ═══ borders)

────────────────────────────────────────────────────────────────
SUMMARY
  SVGs:    1 pass, 1 needs-work, 0 redo   →  1 needs-work (of 2)
  ASCII:   1 pass                          →  clean
  Tables:  present and useful
  Cheat sheet: present
  Cross-refs: present, forward links marked *(planned)*

  P1 FIXES REQUIRED:
  1. [SVG #2] Negate western Pacific longitudes (Kamchatka→x=-160, Japan→x=-140, etc.)
  2. [SVG #1] Add India as distinct polygon (~73E,24N to 80E,8N to 88E,22N)
  3. [ASCII #1] Remove ═══ frame borders (lines 75, 127)

  P2 FIXES:
  4. [SVG #1] Increase continent outline control points to 25-30 each
  5. [SVG #1] Add Mediterranean gap between Europe and Africa
  ...
```

### Section Review

```
ATLAS SECTION REVIEW: Section I — Earth & Space (3s)
────────────────────────────────────────────────────────────────
Map                        SVGs  ASCII  P1  P2  P3  Status
────────────────────────────────────────────────────────────────
01-TECTONIC-PLATES.md       2     1     3   2   0   needs-work
02-GLOBAL-WINDS.md          1     5     0   1   0   pass
03-WORLD-SOILS.md           1     3     0   1   0   pass
04-CELESTIAL-NAVIGATION.md  1     6     1   2   1   needs-work
────────────────────────────────────────────────────────────────
TOTAL                       5    15     4   6   1

Blocking P1 issues: 4
Maps ready for use: 2 of 4
```

---

## Mode: `map <number>`

1. Read the design spec (`atlas-cartography/SKILL.md`)
2. Read the Florida prototype (`atlas/_test_florida.html`)
3. Read the target map file (`atlas/NN-*.md`)
4. For each SVG in the file:
   - Check all 10 SVG criteria
   - Verify 3-5 feature coordinates against known real-world positions
   - Check for common coordinate errors (see table above)
5. For each ASCII diagram:
   - Check all 5 ASCII criteria
6. Check map structure: title line, card identity, diagrams, tables, cheat sheet, cross-references
7. Output the per-map review format

**Do NOT edit files.** Review only. Output the review as text.

---

## Mode: `section <N>`

1. Identify the 4 maps in the section (from PROJECTS.md)
2. Review each map per the `map` mode
3. Output individual reviews + section summary table
4. Flag any cross-map inconsistencies (e.g., different coastline shapes for same continent in adjacent maps)

**Do NOT edit files.** Review only.

---

## Mode: `coastlines`

Specialized audit of continent outline accuracy across all existing atlas maps.

1. Find all `.md` files in `atlas/` containing `<svg`
2. Extract all `<path>` elements that represent continent outlines (typically fill `#e8e4dc` or `fill="none"` with continent-shaped coordinates)
3. For each continent outline found:
   - Count control points
   - Check for key shape features (India peninsula, Mediterranean gap, Horn of Africa, etc.)
   - Flag shared vs. divergent outlines across maps
4. Output a continent audit:

```
COASTLINE AUDIT
──────────────────────────────────────────────────────
Continent       Points  India?  Med?  Horn?  Bight?  Files
──────────────────────────────────────────────────────
North America     22     —      —     —      —       01,02,03,04
South America     28     —      —     —      —       01,02,03
Europe            20     —      ✗     —      —       01,03
Africa            24     —      —     ✗      —       01,03
Asia              30     ✗      —     —      —       01,03,04
Australia         14     —      —     —      ✗      01,03
Antarctica        10     —      —     —      —       01
──────────────────────────────────────────────────────
RECOMMENDATION: Create shared continent path library
```

**Do NOT edit files.** Audit only.

---

## Mode: `status`

1. List all 53 atlas files (00-OVERVIEW + 01-52)
2. For each file that exists:
   - Count SVGs (`<svg` tags)
   - Count ASCII code blocks
   - Note if previously reviewed
3. Output status table:

```
ATLAS STATUS
──────────────────────────────────────────
Section    Maps  Exist  SVGs  Reviewed
──────────────────────────────────────────
Overview   1     1      0     —
I. E&S     4     4      5     ✓
II. NW     4     0      0     —
...
──────────────────────────────────────────
TOTAL      53    5      5     1 section
```

---

## Shared Continent Outline Library

After the coastline audit, if outlines diverge across maps, recommend extracting a shared set of continent `<path>` definitions. Each continent should be defined once at 25-30 control points, then reused by all world maps. Key features required:

| Continent | Min Points | Must Include |
|-----------|-----------|-------------|
| North America | 25 | Great Lakes indent, Gulf of Mexico, Florida peninsula, Baja, Alaska |
| South America | 25 | Brazilian bulge, Patagonian taper, Chilean coast |
| Europe | 25 | Iberian peninsula, Italian boot, Scandinavian peninsula, Mediterranean coast |
| Africa | 25 | Horn of Africa, Gulf of Guinea indent, Cape of Good Hope |
| Asia | 30 | Indian peninsula, Arabian peninsula, SE Asian peninsulas, Kamchatka, Japan (as island) |
| Australia | 20 | Great Australian Bight, Cape York, Gulf of Carpentaria |
| Antarctica | 12 | Antarctic Peninsula, Ross Sea indent |

This library would live in `atlas/_continent_paths.md` as a reference (not imported — each SVG is self-contained in Markdown).
