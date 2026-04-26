# 10 — Cartographic Design

## Making Maps That Work

Cartographic design is the discipline of translating geographic data into visual form that serves the reader's task. The theoretical foundation is visual perception science and information theory; the practical constraints are projection, scale, and symbolization. A well-designed map is one where the visual encoding matches the data structure and the reader's cognitive task. A poorly designed map is one where visual choices obscure, mislead, or overwhelm.

```
CARTOGRAPHIC DESIGN ELEMENTS — THE FULL SYSTEM
═══════════════════════════════════════════════════════════════════════

  CONTENT DECISIONS (what to show):
  ├── Selection: which features to include at this scale
  ├── Classification: how to group continuous data into categories
  └── Generalization: how to simplify complex features

  VISUAL ENCODING (how to represent it):
  ├── Visual variables (Bertin's system): position, size, color value,
  │   color hue, texture/pattern, shape, orientation
  ├── Symbol design: point/line/polygon symbolization
  └── Typography: labels, titles, legends

  LAYOUT (how to organize the page):
  ├── Visual hierarchy: figure-ground, contrast, emphasis
  ├── Map furniture: title, legend, scale bar, north arrow, credits
  └── Composition: balance, white space, focal point

  COMMUNICATION CONTEXT:
  ├── Audience: expert vs general public vs children
  ├── Medium: print vs screen vs presentation
  └── Purpose: navigation vs analysis vs argument

═══════════════════════════════════════════════════════════════════════
```

---

## Visual Hierarchy and Figure-Ground

Visual hierarchy is the organization of a map's elements so that the reader's eye is guided to the most important information first, then progressively to supporting information.

```
VISUAL HIERARCHY LEVELS
══════════════════════════════════════════════════════════════════════

  FIGURE: elements that appear to come forward visually
  GROUND: background that recedes

  Factors that make elements read as figure:
  ├── Higher contrast (darker against lighter background)
  ├── Saturated color against desaturated
  ├── Enclosed (inside a polygon) vs open
  ├── Warmer colors advance; cooler recede
  ├── Thicker lines advance
  └── Complex pattern advances vs plain ground

  TYPICAL HIERARCHY STRUCTURE:
  ┌────────────────────────────────────────────────────────────┐
  │  LEVEL 1: Primary data (what the map is about)             │
  │  Example: thematic data, highlighted route, earthquake     │
  │  Design: highest contrast, most saturated color,           │
  │          bold/thick symbols                                │
  │                                                            │
  │  LEVEL 2: Reference context (where it is)                  │
  │  Example: coastlines, major roads, country borders         │
  │  Design: medium weight, desaturated, no fill or light fill │
  │                                                            │
  │  LEVEL 3: Supporting detail (additional context)           │
  │  Example: secondary roads, minor cities, grid lines        │
  │  Design: light/thin, low contrast                          │
  │                                                            │
  │  LEVEL 4: Background (base map)                            │
  │  Example: ocean, terrain shading, land area                │
  │  Design: very light, desaturated, no visual noise          │
  └────────────────────────────────────────────────────────────┘

══════════════════════════════════════════════════════════════════════
```

The principle: data at every level should be legible but should not compete with data at a higher level. A reference map (road atlas) has road network at Level 1. A choropleth map has the thematic data at Level 1 with roads dropped to Level 3 or omitted.

---

## Color in Maps

Color is the most powerful and most misused visual variable in cartography. The three dimensions of color — hue (red vs blue vs yellow), value/lightness (light vs dark), and saturation/chroma (vivid vs muted) — serve different purposes.

```
COLOR DIMENSIONS AND THEIR CARTOGRAPHIC USES
══════════════════════════════════════════════════════════════════════

  HUE (which color — red, green, blue, etc.):
  ├── Encodes CATEGORICAL differences (nominal data)
  ├── Land use: green=forest, yellow=cropland, red=urban
  ├── No implied order in hue alone
  └── Best for: qualitative distinctions

  VALUE/LIGHTNESS (light vs dark, same hue):
  ├── Encodes ORDERED/QUANTITATIVE variation (ordinal, ratio)
  ├── Light = low value; dark = high value (conventional)
  ├── Perceived as ordered — "dark = more"
  └── Best for: sequential quantitative data (one direction)

  SATURATION/CHROMA (vivid vs muted):
  ├── Often used for emphasis or data emphasis vs background
  ├── Saturated = important; desaturated = background
  └── Can encode data quality/confidence (vivid = certain)

  COMBINED:
  Diverging color schemes: two hues, light center, dark at both ends
  (e.g., blue → white → red for temperature anomaly)
  Encodes: direction AND magnitude

══════════════════════════════════════════════════════════════════════
```

### ColorBrewer — Designing for Perception

Cynthia Brewer's ColorBrewer (colorbrewer2.org) is the standard tool for cartographic color scheme selection. It was developed from perceptual research on how humans perceive map colors.

```
COLORBREWER SCHEME TYPES
══════════════════════════════════════════════════════════════════════

  SEQUENTIAL (one direction, quantitative):
  ┌────────────────────────────────────────────────────────────┐
  │  Light to dark in one hue (or hue + value)                 │
  │  Example: pale yellow → orange → dark red                  │
  │  Use for: quantities increasing in one direction           │
  │  (population, income, temperature above zero)              │
  └────────────────────────────────────────────────────────────┘

  DIVERGING (two directions from midpoint):
  ┌────────────────────────────────────────────────────────────┐
  │  Two hues, light center, dark at both extremes             │
  │  Example: dark blue ← white → dark red                     │
  │  Use for: data with meaningful midpoint                    │
  │  (temperature anomaly from mean, vote swing from baseline, │
  │  positive/negative change, correlation -1 to +1)           │
  └────────────────────────────────────────────────────────────┘

  QUALITATIVE (categorical):
  ┌────────────────────────────────────────────────────────────┐
  │  Distinct hues, similar lightness/saturation               │
  │  No implied order                                          │
  │  Use for: land use, political parties, species, nations    │
  │  Maximum: ~8–12 categories (cognitive limit for color IDs) │
  └────────────────────────────────────────────────────────────┘

  COLORBLIND SAFETY:
  ColorBrewer indicates which schemes are safe for:
  ├── Deuteranopia/protanopia (red-green colorblind): ~8% of men
  ├── Tritanopia (blue-yellow colorblind): ~0.01%
  └── Achromatopsia (no color): ~0.003%

  8% of men have red-green color blindness.
  If your map uses a red-to-green scale, 1 in 12 male readers
  sees it as two shades of brown/olive. This is not rare.
  Use orange-to-blue or use lightness variation as backup.

══════════════════════════════════════════════════════════════════════
```

### Why Rainbow Color Scales Are Bad

The rainbow (spectral) color scale — violet → blue → green → yellow → orange → red — is the most common poor color choice in scientific visualization and mapping.

Problems:
1. **Non-linear perceived brightness**: yellow appears much lighter than blue or red, creating a false ridge in the data at the yellow band
2. **No natural ordering**: there is no intuitive mapping from "low" to "high" across violet-to-red
3. **Colorblind-hostile**: red and green are both in the scale; deuteranopes see similar shades for different values
4. **Artificial edges**: the spectrum creates apparent boundaries in continuous data where none exist (the "blue-green boundary" is a perceptual artifact, not a data feature)

The default color scale in most scientific software (matplotlib's "jet" was rainbow; Python eventually changed the default to "viridis" in 2015) was rainbow. The community push to replace it with perceptually uniform sequential scales (viridis, magma, plasma) took years and produced measurable improvements in data interpretation accuracy.

---

## Typography on Maps

Text on maps is harder than text in documents because it competes with the map content, must be placed to avoid obscuring features, and must convey hierarchy through visual differentiation.

```
MAP TYPOGRAPHY HIERARCHY
══════════════════════════════════════════════════════════════════════

  LEVEL 1: Map title
  Size: largest; placement: dominant corner; weight: bold
  Font style: can be decorative (within taste limits)

  LEVEL 2: Region/country/state names
  Size: large; all-caps or small caps often used
  Tracking: spaced out (especially for names spanning an area)
  Font style: usually sans-serif for clarity

  LEVEL 3: City/town names
  Size: medium; graduated by population (large city = larger font)
  Style: if serif base: use serif; if sans: use sans

  LEVEL 4: Feature names (rivers, mountains, roads)
  Size: small; river names often italic (by convention)
  Placement: curved text following river line

  LEVEL 5: Supplementary labels, notes
  Size: smallest; muted color

  FONT CONVENTIONS (not rules, but conventions):
  ├── Serif fonts: traditional cartography, topographic maps
  ├── Sans-serif fonts: modern, screen-friendly, small sizes
  ├── Italic: water features (rivers, lakes, ocean) by convention
  ├── ALL CAPS: administrative regions, major political units
  └── Small Caps: secondary admin units, neighborhoods

══════════════════════════════════════════════════════════════════════
```

### Label Placement Rules

Automated label placement is a hard computational problem — it is essentially a constraint satisfaction problem with spatial non-overlap constraints, priority ordering, and aesthetic preferences.

```
LABEL PLACEMENT PRIORITIES
══════════════════════════════════════════════════════════════════════

  FOR POINT FEATURES (cities, POIs):
  ┌────────────────────────────────────────────────────────────┐
  │  Priority placement positions (in order):                  │
  │  1. Upper right (default preferred)                        │
  │  2. Upper left                                             │
  │  3. Lower right                                            │
  │  4. Lower left                                             │
  │  5. Directly right                                         │
  │  6. Directly above                                         │
  │  7. Directly left                                          │
  │  8. Directly below (least preferred — visually tied to dot)│
  └────────────────────────────────────────────────────────────┘

  NEVER:
  ├── Label crossing the coast (if feature is coastal city)
  ├── Label obscuring another feature it's labeling
  ├── Ambiguous placement (label could refer to two features)
  └── Label overlapping another label of equal or higher priority

  FOR LINE FEATURES (rivers, roads):
  ├── Curved text following the line
  ├── Readable: text should read left-to-right
  │   (for steep lines: acceptable to read uphill)
  ├── Placed along straightest segment
  └── Repeated along long features (not just once at each end)

  FOR POLYGON FEATURES (countries, regions):
  ├── Center of polygon (or centroid)
  ├── Text spread across the polygon (increased tracking)
  ├── Do not cross polygon boundary if possible
  └── If polygon is too small: leader line to label outside

══════════════════════════════════════════════════════════════════════
```

---

## Generalization

As scale decreases (more of the world in less space), features must be simplified. Generalization is the process of reducing detail while preserving the essential characteristics of features.

```
GENERALIZATION OPERATIONS
══════════════════════════════════════════════════════════════════════

  SIMPLIFICATION (remove vertices from lines/polygons):
  ┌────────────────────────────────────────────────────────────┐
  │  Ramer-Douglas-Peucker algorithm:                          │
  │  1. Connect first and last point of line                   │
  │  2. Find point farthest from this connecting line          │
  │  3. If distance < threshold ε: delete all intermediate pts │
  │  4. If distance ≥ ε: keep point; recurse on two halves     │
  │  Result: simplified line that deviates <ε from original    │
  │  Complexity: O(n log n) average; O(n²) worst case          │
  │                                                            │
  │  Visual result: coastlines look smooth at small scale      │
  │  without the jagged appearance of over-dense vertices      │
  └────────────────────────────────────────────────────────────┘

  SMOOTHING: replace sharp angles with curves
  AGGREGATION: merge nearby features (small islands → one polygon)
  ELIMINATION: remove features too small to see at scale
  DISPLACEMENT: move features apart to avoid overlap (road + rail)
  COLLAPSE: replace building footprint with point symbol
  TYPIFICATION: replace pattern with representative sample
               (many trees → scattered tree symbols)

  SCALE-DEPENDENT RULES:
  ├── 1:1,000  (cadastral): every property boundary, all buildings
  ├── 1:10,000 (local): building footprints, minor roads
  ├── 1:100,000 (regional): major roads only, simplified coastline
  ├── 1:1,000,000 (national): cities as points, rivers simplified
  └── 1:50,000,000 (world): countries only, capitals

  MULTI-SCALE DATABASES:
  Modern GIS maintains multiple generalization levels.
  Each tile zoom level uses a different generalization.
  OSM generates different vector tile layers per zoom.

══════════════════════════════════════════════════════════════════════
```

---

## Map Furniture

The standard supporting elements of a map:

```
MAP FURNITURE — ELEMENTS AND WHEN TO USE THEM
══════════════════════════════════════════════════════════════════════

  TITLE:
  ├── Required: always
  ├── Contents: what + where + when ("County Population 2020")
  └── Placement: dominant visual position

  LEGEND:
  ├── Required: for thematic maps, specialized symbols
  ├── NOT required: self-evident reference maps
  │   (everyone knows roads are lines, cities are dots)
  ├── Contents: every non-obvious symbol explained
  └── Placement: non-competing corner; can be outside map frame

  SCALE BAR:
  ├── Required: almost always (especially for print)
  ├── NOT needed: web maps (users can read scale from zoom)
  ├── Type: graphic bar (survives map copying/resizing)
  │        NOT text ratio (1:24,000 becomes wrong if map resized)
  └── Size: appropriate to map extent (read comfortably)

  NORTH ARROW:
  ├── Required: when north is NOT up (rotated maps)
  ├── NOT required: when north is up (which it should be by default)
  ├── Note: north arrow is not a compass rose
  │   (compass roses show all 16/32 wind directions — nautical charts)
  └── Rule: if you're adding a north arrow to a north-up map
            to look professional, you're adding chartjunk

  DATA SOURCES + DATE:
  ├── Required: always (credibility and reproducibility)
  └── Example: "Data: USGS National Map, 2023"

  CRS / PROJECTION NOTE:
  ├── Required: for professional/scientific maps
  └── Example: "Projection: Albers Equal-Area Conic, NAD83"

══════════════════════════════════════════════════════════════════════
```

---

## Persuasion and Propaganda Maps

Every map makes arguments. Understanding the mechanisms of persuasion in maps is the critical-thinking skill for reading maps you didn't make.

```
MAP MANIPULATION TECHNIQUES
══════════════════════════════════════════════════════════════════════

  PROJECTION CHOICE:
  ├── Showing your country larger than it is: use projection where
  │   your country is at the latitude of least distortion
  ├── Cold War US government: often used projections where Russia
  │   appeared closer to US (azimuthal, polar projections)
  │   → made nuclear threat feel more immediate
  └── "The world needs a new map" arguments: always suspect
      because any "correction" replaces one lie with another

  COLOR CHOICE:
  ├── Red = danger, communism, enemy: Cold War red maps
  │   Soviet bloc = red, free world = white/blue
  │   → Soviets used same colors with roles reversed
  ├── Electoral maps: "red state/blue state" is arbitrary
  │   (US Republican = red, Democrat = blue since ~2000)
  │   Other countries use opposite or different conventions
  └── Heat maps: red typically = more/worse; depends on context

  WHAT TO OMIT:
  ├── Scale omission: a map of "terrorist incidents" that doesn't
  │   normalize by population size or land area
  │   → densely populated regions always look worse
  ├── Context omission: a map of crime that doesn't show
  │   poverty/unemployment as context
  └── Temporal cherry-picking: choose start/end dates to show
      maximum/minimum trend

  GERRYMANDERING — MAUP AS POLITICS:
  ┌────────────────────────────────────────────────────────────┐
  │  PACKING: concentrate opponent voters in a few districts   │
  │           → they win those districts by huge margins       │
  │           → fewer total districts won                      │
  │                                                            │
  │  CRACKING: split opponent concentrations across districts  │
  │           → they're a minority in many districts           │
  │           → wins in none                                   │
  │                                                            │
  │  The same set of point data (voters + their preferences)   │
  │  can be districted to produce dramatically different       │
  │  outcomes. The map = the political outcome.                │
  └────────────────────────────────────────────────────────────┘

  THE GALL-PETERS VS MERCATOR CONTROVERSY (recap):
  Both are arguments. Mercator: navigation matters. Peters: area
  equity matters. Neither is "objective." Choose based on purpose.

══════════════════════════════════════════════════════════════════════
```

---

## The Modern Web Map Stack — Design Considerations

```
WEB MAP DESIGN SYSTEM
══════════════════════════════════════════════════════════════════════

  BASE MAP STYLE:
  ├── Dark basemap: for data with colored points/lines/areas
  │   (data stands out against dark background)
  ├── Light basemap: for printed maps, official documents
  ├── Satellite basemap: when terrain context is essential
  └── Minimal basemap: maximize data visibility, minimize context

  MAPBOX GL STYLE SPECIFICATION:
  JSON structure:
  {
    "version": 8,
    "sources": { ... vector tile sources ... },
    "layers": [
      // each layer: id, type, source, filter, paint, layout
      { "id": "background", "type": "background",
        "paint": { "background-color": "#f8f4f0" } },
      { "id": "water", "type": "fill",
        "paint": { "fill-color": "#aad3df" } },
      { "id": "roads-major", "type": "line",
        "paint": { "line-color": "#ffffff",
                   "line-width": ["interpolate", ["linear"],
                     ["zoom"], 10, 1, 18, 8] } }
    ]
  }

  Layer rendering order: bottom layer in array = drawn first.
  Data layers on top; base layers below.

  RESPONSIVE DESIGN:
  ├── Touch interaction: finger-size hit targets (44px+)
  ├── Small screen: remove less important layers at mobile zoom
  ├── High DPI: use @2x tile variants if available
  └── Accessibility: add screen reader description of map content

══════════════════════════════════════════════════════════════════════
```

---

## Design for Accessibility

```
ACCESSIBLE MAP DESIGN
══════════════════════════════════════════════════════════════════════

  COLOR BLINDNESS (most common):
  ├── Don't rely on red/green distinction alone (8% of men)
  ├── Use ColorBrewer colorblind-safe palettes
  ├── Supplement color with pattern texture
  ├── Test with Coblis or similar simulator
  └── Ensure sufficient lightness contrast (not just hue)

  WCAG CONTRAST REQUIREMENTS:
  Text on background: minimum 4.5:1 contrast ratio (AA)
  Large text (>18pt): minimum 3:1
  UI components: minimum 3:1
  Maps: no formal requirement but aim for text ≥ 4.5:1

  LOW VISION:
  ├── Minimum font size for legibility: 9pt print, 12px screen
  ├── Provide ability to increase text size
  └── Don't encode meaning in text size alone

  SCREEN READERS / COGNITIVE:
  ├── Provide text alternative for map content
  ├── Key findings should appear in text, not map-only
  └── Complex maps: provide summary table of key data

══════════════════════════════════════════════════════════════════════
```

---

## Common Confusion Points

**"A north arrow is always needed."** Only when the map is rotated from north-up. Adding a north arrow to a standard north-up map is cartographic clutter. The convention is: north-up unless there's a reason to rotate; add north arrow only if rotated.

**"Scale ratio (1:24,000) survives copying."** A printed scale ratio is correct only for the specified print size. If you copy the map at 75%, the ratio is wrong. Always use a graphic scale bar, which copies at correct ratio.

**"More colors = more information."** False. Colors beyond ~8 hues are not reliably distinguishable in a legend. More colors often indicate more categories than the reader can track. Reconsider the data classification before adding more colors.

**"Dark maps are just aesthetic."** Dark basemaps improve data layer visibility because bright-colored data points/areas stand out more clearly against dark backgrounds than light ones. The choice is functional, not purely aesthetic.

---

## Decision Cheat Sheet

| Design choice | Use when | Avoid when |
|--------------|----------|-----------|
| Sequential color scheme | One direction of data variation | Data has a meaningful center/zero |
| Diverging color scheme | Data varies ± around meaningful midpoint | No natural midpoint in data |
| Qualitative color scheme | Categorical data | Ordered data |
| Rainbow color scale | Never | Always |
| ColorBrewer safe palette | Most cases | — |
| Dark basemap | Visualizing point/line data | Print output, formal documents |
| North arrow | Map is rotated from north-up | Map is standard north-up |
| Graphic scale bar | Always for print | Rarely for web maps |
| Scale ratio text | Never (changes with print size) | — |
| Bold/thick lines | Primary data | Background context |
| All caps labels | Country/region names | Point features, road names |
| Italic labels | Water bodies (river, ocean) | Land features |
| 8+ color classes | Never (cognitive limit) | — |
| Ramer-Douglas-Peucker | Simplifying polylines for smaller scale | Maintaining detailed topology |
