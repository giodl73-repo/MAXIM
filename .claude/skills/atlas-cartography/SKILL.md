# /atlas — Survival Reference Atlas Cartography

Generate reference maps for the 52-card atlas. Each map is one file in `atlas/`, thematically linked to a card in the MAXIM deck, ordered for survivalist priority.

**Hybrid format**: Geographic maps use **inline SVG** (vector, real coordinates, correct aspect ratio). Mechanism diagrams and cross-sections use **ASCII code blocks** (where monospace shines). Tables are standard Markdown.

## Usage

```
/atlas generate <number>          — generate a single map (e.g., /atlas generate 05)
/atlas generate <range>           — generate a range (e.g., /atlas generate 05-08)
/atlas generate section <N>       — generate all 4 maps in a section (e.g., /atlas generate section II)
/atlas audit <file>               — unit-test a geographic map's feature positions
/atlas legend                     — regenerate the master glyph legend in 00-OVERVIEW.md
```

---

## Design Authority

These rules derive from a design review panel: Edward Tufte (information design), Massimo Vignelli (systematic graphic design), Richard Saul Wurman (information architecture), R. Buckminster Fuller (systems cartography), and a working cartographer composite (Pelto/Nelson/Imhof). Full reviews are in `atlas/REVIEWS.md`.

**The Tufte Principle** — the atlas's guiding law:
> *Let the maps be schematic, let the diagrams be precise, and let the tables be comprehensive.*

---

## Map Structure Template

Every atlas file follows this skeleton:

```markdown
# NN — Title

*Card♣ Archetype Name — one-line thematic link.*

---

## [Diagram 1 — the primary visual]

## [Diagram 2-N — supporting visuals, mechanism explanations]

## [Key Data Table(s)]

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|

## Cross-References
```

### What each section does:
- **Title + card line**: identity. One line. No box, no preamble.
- **Diagrams**: the core content. Multiple maps/cross-sections/schematics per file. Each inside a code block.
- **Tables**: dense reference data. Tufte: "tables are the most honest form of data display."
- **Decision Cheat Sheet**: the "what do I use when" lookup. Mandatory.
- **Cross-References**: links to related atlas maps and library volumes.

### What is REMOVED (per reviewer feedback):
- ~~"WHY THIS MAP IS THIRD" preamble boxes~~ — the survivalist sequencing is documented in 00-OVERVIEW. Individual files don't repeat it.
- ~~Decorative `═══` frame borders around code blocks~~ — chartjunk. Code blocks have their own borders in every rendering context.
- ~~Emoji~~ — violate the monospace contract, render inconsistently.

---

## The Three Contracts

Before drawing anything, define three things (Vignelli):

### 1. Format Standard

| Format | Use |
|--------|-----|
| **Inline SVG** | Geographic maps — coastlines, distributions, positioned features, regional/continental maps |
| **ASCII code block (80 col)** | Cross-sections, mechanism diagrams, latitude-band charts, star charts |
| **Markdown table** | Data tables, cheat sheets, comparisons |

ASCII frame borders (`═══`) are NOT used — the code block fence is the frame.

### 1b. Scale Selection Rubric

Every map should ask: **world, continent, or both?** The answer depends on what the map is trying to show.

| Scale | viewBox | Use when | Examples |
|-------|---------|----------|---------|
| **World** (equirectangular) | `-185 -90 370 180` | The thesis IS the global pattern. Latitude bands, planet-wide distributions. | Plate boundaries, desert belts, biome bands, flyway overview |
| **Continent** (regional crop) | Per continent (see table) | Features need individual labels. >15 items compete for space at world scale. | Rivers with tributaries, cities, trade routes, mineral deposits |
| **World + Continent** (multi-SVG) | 1 world overview + 2-6 continent details | Both the global pattern AND the regional detail matter. | Rivers (world overview + per-continent detail), trade routes, disease vectors |
| **Regional** (sub-continent) | Custom crop | Single-country or sub-region focus. | Mediterranean, Caribbean, Middle East, Southeast Asia |

**Decision test**: If you need to label more than ~12 features on a world map, split to continents. If the thesis requires seeing all continents at once, keep the world map as an overview and add continent maps below.

**Standard continent bounding boxes** (available via `build_continent_svg.py`):

| Continent | Lon range | Lat range | Width | Use |
|-----------|-----------|-----------|-------|-----|
| North America | -170 to -50 | 7 to 84 | 900px | Rivers, biomes, mineral deposits |
| South America | -82 to -34 | -56 to 13 | 700px | Andes, Amazon, grain belts |
| Europe | -12 to 45 | 34 to 72 | 800px | Trade routes, rivers, industry |
| Africa | -20 to 52 | -36 to 38 | 750px | Rivers, resources, disease zones |
| Asia | 25 to 180 | -10 to 78 | 960px | Monsoon, trade, Silk Road |
| Oceania | 110 to 180 | -48 to -8 | 800px | Reefs, Pacific routes |
| Middle East | 24 to 64 | 12 to 42 | 800px | Oil, water, conflict |
| Southeast Asia | 90 to 155 | -12 to 30 | 900px | Spice routes, rice, straits |
| Caribbean | -90 to -58 | 10 to 28 | 800px | Hurricane corridor, trade |
| Mediterranean | -6 to 42 | 28 to 48 | 900px | Classical trade, wine, olives |

**Extraction command**:
```bash
python build_continent_svg.py --continent africa --mode full --precision 1
```

**Multi-SVG layout pattern** (world + continents):
```markdown
## Overview — World Distribution
<svg viewBox="-185 -90 370 180" ...>  <!-- world coastlines + thematic overview -->

## Africa — Regional Detail
<svg viewBox="-20 -38 72 74" ...>     <!-- continent coastlines + dense labels -->

## Asia — Regional Detail
<svg viewBox="25 -78 155 88" ...>     <!-- continent coastlines + dense labels -->
```

The world map shows the pattern. The continent maps show the detail. The reader zooms in mentally.

### 2. Master Glyph Legend

One symbol vocabulary, enforced across all 52 maps. Published once in `00-OVERVIEW.md`.

| Glyph | Meaning | Context |
|-------|---------|---------|
| `▲` | Mountain / volcano / high terrain | Geographic maps, cross-sections |
| `~` or `≈` | River / flowing water | Geographic maps |
| `≈` (in labels) | Ocean / large water body | Ocean labels only |
| `░` | Desert / arid zone | Geographic maps |
| `○` | Lake / enclosed water body | Geographic maps |
| `║` | Mid-ocean ridge / rift | Tectonic maps |
| `╱` `╲` `│` `─` | Coastline / boundary | Geographic maps |
| `·` | Interior land (light fill) | Geographic maps — NOT used for cities or stars |
| `★` | Pole star / primary navigation star | Celestial maps ONLY |
| `↑` `↓` `→` `←` | Flow direction / wind / current | Mechanism diagrams |
| `├── N km ──┤` | Scale bar | Below every geographic map |

**Context rule**: Where a glyph could be ambiguous (e.g., celestial vs geographic), the file type provides context. Sky maps are an explicit different domain — `·` means "star" in celestial charts, "land" in geographic maps. This is acceptable because no file mixes the two.

### 3. Coordinate Protocol

**Regional SVG maps** (single hemisphere, e.g., Florida): Use `cx="-longitude"`, `cy="-latitude"`. Western longitudes are already negative, so `cx = -80` for 80°W. The viewBox handles projection.

**World SVG maps** (both hemispheres): Use the standard cartographic convention: `x = longitude` (positive east, negative west), `y = -latitude` (negative north, positive south). This is equivalent to the regional convention for the Western hemisphere but differs for the Eastern hemisphere — `x = 40` means 40°E, not -40°W.

**Pacific-centered maps** (Ring of Fire, ocean currents): The Pacific straddles ±180°. Use real longitudes for the Americas (negative values), and `longitude - 360` for East Asian/Oceanian features (e.g., Japan at 140°E → `x = -220`). Set the viewBox to span the shifted range (e.g., `"-260 -75 280 150"`).

| Map scope | x convention | y convention | Example: Tokyo (139.7°E, 35.7°N) |
|-----------|-------------|-------------|----------------------------------|
| Regional (W hemisphere) | `cx = -longitude` | `cy = -latitude` | n/a (E hemisphere) |
| World | `x = longitude` | `y = -latitude` | `x=139.7, y=-35.7` |
| Pacific-centered | `x = longitude - 360` (E hem) | `y = -latitude` | `x=-220.3, y=-35.7` |

**ASCII diagrams**: For latitude-band diagrams, use consistent latitude axis (90N at top, 90S at bottom) across all files so readers can visually cross-reference wind belts → desert belts → soil orders.

---

## Two Visual Forms

### Form 1: Inline SVG — Geographic Maps

For any map showing geographic positions, coastlines, distributions, or spatial relationships. SVG solves the aspect ratio and coordinate accuracy problems that ASCII cannot.

**Style: Light / Warm** (locked in for all 52 maps)
- Background: `#faf8f5` (warm off-white)
- Land fill: `#e8e4dc` (cream)
- Coastline stroke: `#444`, width 0.04-0.06
- City dots: `#444`, radius 0.04-0.08 (scaled by importance)
- Labels: `#333` (cities), `#555` (secondary), `#777` (features)
- Water labels: `#a0b0c0`, italic
- Grid lines: `#e0ddd8`, width 0.02
- Lat/lon labels: `#aaa`, size 0.20
- Scale bar: `#444`, with tick marks
- Font: Georgia, serif (matches MkDocs Material EB Garamond theme)
- Feature labels (Everglades, etc.): `#7a8a6a` italic for natural features

**Coordinate system:**
- `x = -longitude` (west is negative, so -80 for 80°W)
- `y = -latitude` (SVG y increases downward; negating latitude puts north at top)
- viewBox: `"-maxlon -maxlat width height"` e.g., `"-90 -32 16 8"` for Florida

**This means city positions use REAL coordinates directly:**
```xml
<!-- Miami at 80.19°W, 25.76°N -->
<circle cx="-80.19" cy="-25.76" r="0.07" fill="#444"/>
```

No conversion math. No aspect ratio correction. No grid arithmetic. The SVG viewBox + width/height handles everything.

**Rules:**
- Width 800-960px, height proportional to region aspect ratio
- ~25-50 coastline control points per region (recognizable, not USGS-precise)
- Lat/lon grid lines every 2-5° depending on map scale
- Scale bar in SVG (line + tick marks + text)
- All city/feature coordinates from real gazeteer data
- Context coastlines (neighboring regions) as dashed `stroke-dasharray="0.08"`

**Reference implementation:** `atlas/_test_florida.html` — the approved Florida prototype.

### Form 2: ASCII Code Blocks — Mechanism Diagrams

For cross-sections, atmospheric circulation, soil horizons, latitude-band charts, star charts, and any diagram showing WHY a pattern exists (not WHERE things are spatially).

**These are the atlas's strongest content** (unanimous reviewer verdict).

**Rules:**
- 80 columns standard width
- No decorative `═══` frame borders
- Consistent visual grammar for cross-sections: left edge = vertical axis, horizontal rules separate layers, arrows indicate motion
- Latitude-band diagrams share the same vertical axis (latitude) to enable cross-file comparison
- Every diagram answers "WHY this pattern exists" not just "WHERE things are"
- Multiple diagrams per file encouraged — this is where the atlas earns its keep
- Master glyph legend applies (see § Master Glyph Legend)

---

## Scale Bars

Every SVG geographic map includes an SVG scale bar:

```xml
<!-- 200 km scale bar example -->
<line x1="-89.2" y1="-24.4" x2="-87.4" y2="-24.4" stroke="#444" stroke-width="0.035"/>
<line x1="-89.2" y1="-24.3" x2="-89.2" y2="-24.5" stroke="#444" stroke-width="0.035"/>
<line x1="-87.4" y1="-24.3" x2="-87.4" y2="-24.5" stroke="#444" stroke-width="0.035"/>
<text x="-88.7" y="-24.55" font-size="0.18" fill="#444">200 km</text>
```

Calculate bar length: at the equator 1° longitude ≈ 111 km; at 45°N ≈ 79 km. A 200 km bar at 30°N ≈ 2.08° of longitude.

---

## Common-Scale Reference

In `00-OVERVIEW.md`, include a continent size comparison at a single common scale so the reader can see relative sizes:

```
CONTINENT SILHOUETTES — COMMON SCALE
Africa     ████████████████████████████████  30.4 M km²
Asia       ███████████████████████████████████████████████  44.6 M km²
N. America ██████████████████████████  24.7 M km²
S. America ███████████████████  17.8 M km²
Antarctica ███████████████  14.0 M km²
Europe     ███████████  10.2 M km²
Oceania    █████████  8.5 M km²
```

---

## Ocean as Primary Feature

Per Fuller: the ocean is 71% of Earth's surface and must not be treated as negative space. Specific guidance:

- In `00-OVERVIEW.md`, the world overview should convey one continuous world ocean, not five disconnected fragments
- Map 18 (Ocean Currents) should show the ocean as the primary feature with continents as interruptions
- Tectonic maps should give the Pacific Plate (103M km²) visual weight proportional to its size
- Use light fill (`· · ·`) for ocean where distinguishing it from unmarked land matters

---

## Longitude Gap — Celestial Navigation

Per Fuller: Map 04 must explain WHY longitude was the unsolved navigation problem for 3,000 years:
- Latitude = geometry (star altitude)
- Longitude = time (Earth rotates 15°/hour; without an accurate clock, you can't determine longitude)
- Harrison's chronometer (1761) solved it
- This connects Map 04 back to Map 01 (Earth's rotation) and forward to technology maps

---

## Forward References

Per Wurman: dead links are a trust problem. Rules:
- Cross-references to unwritten maps should use the format: `→ [atlas/NN-TITLE.md](NN-TITLE.md) *(planned)*`
- When a map is generated, remove the `*(planned)*` suffix from all references to it
- Never link to a file that doesn't exist without marking it as planned

---

## File Naming Convention

```
atlas/
├── 00-OVERVIEW.md
├── 01-TECTONIC-PLATES.md         Section I: Earth & Space (3s)
├── 02-GLOBAL-WINDS.md
├── 03-WORLD-SOILS.md
├── 04-CELESTIAL-NAVIGATION.md
├── 05-GLOBAL-BIOMES.md           Section II: Natural World (2s)
├── ...
├── 52-REVOLUTION-ORIGINS.md      Section XIII: People (As)
├── REVIEWS.md                    Design review archive
└── _test_scale.md                Scale experiments (not published)
```

Full plan with all 52 card-to-map assignments is in `PROJECTS.md` § Atlas.

---

## Coastline Data Pipeline — Natural Earth

**Never hand-draw continent outlines.** Use the Natural Earth extraction pipeline instead.

### Source Data

[Natural Earth](https://www.naturalearthdata.com/) 110m land polygons (public domain). Downloaded to `atlas/_geodata/ne_110m_land.shp`.

### Extraction Script

`atlas/_geodata/build_world_svg.py` converts shapefiles to inline SVG `<path>` elements:

```bash
cd atlas/_geodata

# Full coastlines — for geographic reference maps (plate boundaries, seismic zones)
python build_world_svg.py --mode full --min-area 1 --precision 0 > world_full.svg
# → 92 polygons, ~49KB, all recognizable land

# Context coastlines — for thematic overlays (deserts, breadbaskets, biomes)
python build_world_svg.py --mode context --min-area 5 --precision 0 > world_context.svg
# → 47 polygons, ~41KB, all continents + major islands

# Light coastlines — minimal context for concept maps (star visibility, radio propagation)
python build_world_svg.py --mode context --min-area 20 --precision 0 > world_light.svg
# → 19 polygons, ~33KB, continents only
```

### How to Use

1. Run the extraction script for your map type
2. Paste the generated `<path>` elements into your SVG block
3. Add your thematic layer on top (boundaries, labels, data overlays)
4. The paths already use atlas styling (`fill="#e8e4dc"` for full, `fill="none"` for context)

### Three Tiers

| Tier | min_area | Polygons | Size | Use for |
|------|----------|----------|------|---------|
| **Full** | 1 | 92 | ~49KB | Geographic reference maps — plate boundaries, mountain passes, biomes |
| **Context** | 5 | 47 | ~41KB | Thematic overlays — deserts, breadbaskets, migration routes |
| **Light** | 20 | 19 | ~33KB | Concept maps — star visibility, radio propagation, projections |

### Requirements

Python with `geopandas` and `shapely` (both installed). Natural Earth 110m shapefile in `atlas/_geodata/`.

---

## Generation Workflow

When generating a new atlas map:

1. **Read the plan**: Check `PROJECTS.md` for the card assignment, thematic link, and map title
2. **Determine which content needs SVG vs ASCII**:
   - Geographic/spatial content → SVG (coastlines, distributions, feature positions)
   - Mechanism/process content → ASCII code block (cross-sections, circulation models, profiles)
   - Most maps are a MIX of both
3. **Generate coastlines**: Run `build_world_svg.py` with the appropriate tier (full/context/light). Paste the output into your SVG block.
4. **Add thematic layers**: Plate boundaries, desert ellipses, data markers, labels, etc. on top of the coastline base layer.
5. **Add grid, labels, scale bar, legend**: Every SVG geographic map must have these.
6. **Draft ASCII diagrams**: 80-column width. No `═══` borders. Focus on WHY patterns exist.
7. **Draft tables**: Dense reference data. Every map gets at least one comparison table.
8. **Draft cheat sheet**: The decision cheat sheet is mandatory.
9. **Add cross-references**: Link to related atlas maps and library volumes. Mark unwritten targets as *(planned)*.
8. **Preview check**: SVG renders in MkDocs Material and browsers. Test with `start <file>.html` if needed.

**Important**: The 52 content volumes (computing/, mathematics/, etc.) keep ASCII art unchanged. Only the atlas directory uses SVG for geographic maps.

---

## Audience

Same learner as the main library (see CLAUDE.md): VP of Engineering, MIT double major, peer-level technical tone. The atlas adds a survival context — these maps answer practical questions about the physical world. No dumbing down, but also no unnecessary academic formalism. The reader is smart, curious, and wants to understand mechanisms, not just memorize locations.
