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

**SVG maps**: Use real geographic coordinates directly. `cx="-longitude"`, `cy="-latitude"`. No conversion math needed — the SVG viewBox handles projection and aspect ratio.

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

## Generation Workflow

When generating a new atlas map:

1. **Read the plan**: Check `PROJECTS.md` for the card assignment, thematic link, and map title
2. **Determine which content needs SVG vs ASCII**:
   - Geographic/spatial content → SVG (coastlines, distributions, feature positions)
   - Mechanism/process content → ASCII code block (cross-sections, circulation models, profiles)
   - Most maps are a MIX of both
3. **Draft SVG maps**: Use real coordinates (`cx="-lon" cy="-lat"`). Light/warm style. 25-50 coastline control points per region. Include grid lines, labels, scale bar.
4. **Draft ASCII diagrams**: 80-column width. No `═══` borders. Focus on WHY patterns exist.
5. **Draft tables**: Dense reference data. Every map gets at least one comparison table.
6. **Draft cheat sheet**: The decision cheat sheet is mandatory.
7. **Add cross-references**: Link to related atlas maps and library volumes. Mark unwritten targets as *(planned)*.
8. **Preview check**: SVG renders in MkDocs Material and browsers. Test with `start <file>.html` if needed.

**Important**: The 52 content volumes (computing/, mathematics/, etc.) keep ASCII art unchanged. Only the atlas directory uses SVG for geographic maps.

---

## Audience

Same learner as the main library (see CLAUDE.md): VP of Engineering, MIT double major, peer-level technical tone. The atlas adds a survival context — these maps answer practical questions about the physical world. No dumbing down, but also no unnecessary academic formalism. The reader is smart, curious, and wants to understand mechanisms, not just memorize locations.
