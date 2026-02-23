# 06 — Thematic Maps

## Maps as Argument

A reference map says "here is where things are." A thematic map says "here is what varies where." The distinction is fundamental. Thematic maps are rhetorical devices — arguments encoded in spatial form. Every choice of map type, color scheme, data classification, and projection is an argument about what the data means.

```
THEMATIC MAP DESIGN SPACE
══════════════════════════════════════════════════════════════════════

  DATA TYPE × GEOGRAPHIC AGGREGATION
  ─────────────────────────────────────────────────────────────

  Data type:
  ├── Counts (absolute values): population, cases, dollars
  ├── Rates (normalized values): per capita, per km², percentages
  ├── Ratios: unemployment rate, infection rate
  ├── Categorical: land use type, party affiliation, biome
  └── Continuous field: temperature, elevation, density

  Geographic aggregation:
  ├── Points: individual locations (addresses, events)
  ├── Lines: flows, routes, connections
  ├── Polygons: administrative units (counties, countries)
  └── Continuous surface: raster, interpolated field

  MATCH DATA TYPE TO MAP TYPE:
  ┌──────────────────┬────────────────────────────────────┐
  │  Data type       │  Best map type(s)                  │
  ├──────────────────┼────────────────────────────────────┤
  │  Count by region │  Choropleth (normalized) or dot    │
  │  Rate by region  │  Choropleth (rate is appropriate)  │
  │  Continuous field│  Isoline / raster / heat map       │
  │  Point locations │  Dot map / proportional symbol     │
  │  Flows           │  Flow map / OD matrix              │
  │  Categorical     │  Choropleth (categorical palette)  │
  │  Time series     │  Small multiples / animation       │
  └──────────────────┴────────────────────────────────────┘

══════════════════════════════════════════════════════════════════════
```

---

## John Snow's Cholera Map (1854)

The 1854 Broad Street cholera outbreak in Soho, London, is the most cited case study in the history of spatial analysis. Snow's map is typically described as the founding document of epidemiology. The actual story is more nuanced and more interesting.

```
BROAD STREET CHOLERA OUTBREAK — THE FULL PICTURE
══════════════════════════════════════════════════════════════════════

  BACKGROUND:
  - August 31, 1854: cholera cases begin appearing in Soho
  - Within 10 days: 500 deaths in a small geographic area
  - Prevailing theory: miasma (disease caused by bad air)
  - Snow's theory (since 1849): cholera spread by contaminated water

  SNOW'S MAP:
  ┌────────────────────────────────────────────────────────────┐
  │  BASE: street map of Soho neighborhood                     │
  │  DATA LAYER 1: black bars = cholera deaths (each bar = 1) │
  │  DATA LAYER 2: dots = water pump locations                 │
  │                                                            │
  │  Pattern visible: deaths cluster around Broad Street pump  │
  │  Deaths thin out away from Broad Street pump              │
  │  Deaths near OTHER pumps: few                              │
  └────────────────────────────────────────────────────────────┘

  THE PUMP HANDLE STORY (partially mythologized):
  ┌────────────────────────────────────────────────────────────┐
  │  September 8, 1854: Snow presents to Board of Guardians    │
  │  Pump handle removed same day                             │
  │  Outbreak was already declining (cases had peaked Sept 2) │
  │  Handle removal probably did not end the outbreak         │
  │  Snow himself acknowledged this                           │
  └────────────────────────────────────────────────────────────┘

  THE ACTUAL EVIDENCE THAT MATTERED:
  Snow didn't just make a map. He gathered the full evidence case:

  1. The map (spatial clustering around Broad St. pump)
  2. Interview data: traced ~73 deaths — did they use Broad St pump?
  3. The negative cases: brewery workers (had their own water supply,
     didn't drink from the pump) — zero deaths
  4. The Lion Brewery workers drank from the pump — deaths occurred
  5. The Widow Eley: lived far away, had water from Broad St. sent
     to her because she liked the taste — died of cholera
  6. The Workhouse: had its own water supply, few deaths despite
     being in the epicenter
  7. The Southwark water supply comparison (1853): households served
     by Southwark & Vauxhall Company (contaminated Thames water)
     had cholera rate 14× higher than those served by Lambeth
     Company (cleaner upstream water) — Snow's quasi-experiment

  The map was convincing, not conclusive. The full evidence package
  was what built the case. The map made the pattern visible;
  the interviews explained the exceptions.

══════════════════════════════════════════════════════════════════════
```

### What Snow Actually Proved

Snow's contribution was twofold: (1) the spatial reasoning that identified the pump as the likely source, and (2) the epidemiological method — identifying an "exposed" group and an unexposed group, comparing their outcomes. His London water supply study (comparing districts served by different water companies) is closer to a controlled experiment than his map, and was arguably his more rigorous scientific contribution.

The map's fame derives from its clarity as a visualization. It makes a spatial pattern immediately visible to a viewer. But "the map proved it" overstates the case. Snow used the map as one piece of evidence in a comprehensive epidemiological argument.

---

## Charles Minard's Napoleon Campaign Map (1869)

Edward Tufte, in *The Visual Display of Quantitative Information*, calls Minard's map of Napoleon's 1812 Russian campaign "probably the best statistical graphic ever drawn." That assessment is defensible.

```
MINARD'S NAPOLEON MAP — SIX VARIABLES IN TWO DIMENSIONS
══════════════════════════════════════════════════════════════════════

  The map encodes:
  1. GEOGRAPHY: campaign route across Russia
  2. ARMY SIZE: band width = number of soldiers
     (starts: 422,000; Moscow: 100,000; returns: 10,000)
  3. DIRECTION: separate colors (tan = advance, black = retreat)
  4. TEMPERATURE: bottom graph (in Réaumur scale, linked to retreat)
  5. DATE: marked at key points during retreat
  6. RIVER CROSSINGS: labeled (Berezina disaster shown)

  Visual structure:
  ┌──────────────────────────────────────────────────────────────┐
  │  Left (Poland border) → Right (Moscow) → back Left          │
  │                                                              │
  │  Advance (tan): ████████████████████                         │
  │                  (wide — 422,000 men)                        │
  │                         ████████                             │
  │                          (narrowing — attrition)             │
  │                                    ██  ← Moscow              │
  │                         (100,000 remain)                     │
  │  Retreat (black):               ██                           │
  │                           ████                               │
  │             ██████████████ ← 10,000 survive                  │
  │                                                              │
  │  Below: temperature graph drops to -30°R during retreat      │
  └──────────────────────────────────────────────────────────────┘

  What makes it work (Tufte's analysis):
  ├── The data IS the graphic — no chartjunk
  ├── Six variables visible simultaneously without confusion
  ├── The story is devastating — the width of the retreat band
  │   shows the scale of human catastrophe directly
  ├── Causal inference supported: temperature drops align with
  │   major army losses; Berezina crossing visible as sudden
  │   narrowing
  └── No scales/axes needed — the band IS the quantity

══════════════════════════════════════════════════════════════════════
```

The Minard map is not "just" a map — it is a temporal narrative, a statistical chart, and a geographic visualization simultaneously. The causal story (cold kills armies) emerges from the relationship between the temperature panel and the band width, which is only visible because both are referenced to the same geographic/temporal x-axis.

Minard made several other flow maps (cotton trade, wine exports) using the same technique. The Napoleon map is the masterpiece because the data has inherent drama — the army that entered Russia with 422,000 soldiers returned with approximately 10,000.

---

## Choropleth Maps

The most common thematic map type, and the most frequently misused.

```
CHOROPLETH MAPS — MECHANICS AND PITFALLS
══════════════════════════════════════════════════════════════════════

  DEFINITION:
  Regions shaded in proportion to a statistical variable.
  "Choropleth" = Greek: khora (region/area) + plethos (multitude)

  CORRECT USE:
  ├── Normalized/rate data: income per capita, cases per 100k
  ├── Continuous variables that make sense across a region
  └── Where the region is the relevant geographic unit

  INCORRECT USE:
  ├── Raw counts: makes big regions look more significant
  │   Example: plotting total COVID deaths by state →
  │   California appears worst; plotting per-capita →
  │   different story
  ├── Very small/large regions not comparable
  └── When the phenomenon doesn't fill the region uniformly

  DATA CLASSIFICATION CHOICES:
  ┌─────────────────────────────────────────────────────────────┐
  │  Equal interval: split range into equal-width bins          │
  │  (good when data is roughly uniform; bad with outliers)     │
  │                                                             │
  │  Quantile: equal number of items per bin                    │
  │  (good for skewed data; hides the actual distribution)      │
  │                                                             │
  │  Natural breaks (Jenks): minimize within-class variance     │
  │  (finds natural groupings; computationally heavy)           │
  │                                                             │
  │  Standard deviation: bins by SD from mean                   │
  │  (highlights outliers; statistical audience)                │
  │                                                             │
  │  Manual: define breaks based on domain knowledge            │
  │  (poverty line, legal thresholds, etc.)                     │
  └─────────────────────────────────────────────────────────────┘

  THE MODIFIABLE AREAL UNIT PROBLEM (MAUP):
  ┌─────────────────────────────────────────────────────────────┐
  │  Aggregating point data to regions produces different        │
  │  results depending on HOW you draw the region boundaries.   │
  │                                                             │
  │  Scale problem: county-level vs state-level patterns differ │
  │  Zone problem: gerrymandering makes this visceral           │
  │               Drawing different district boundaries with    │
  │               the same points produces opposite electoral  │
  │               outcomes — this is MAUP weaponized           │
  │                                                             │
  │  The choropleth LOOKS objective. The boundaries are not.    │
  └─────────────────────────────────────────────────────────────┘

══════════════════════════════════════════════════════════════════════
```

### Simpson's Paradox in Choropleth Maps

A choropleth can show a trend at one geographic level that reverses at another — a spatial manifestation of Simpson's Paradox. The classic US example: a choropleth of political party preference at county level looks very different from a choropleth at census tract level, not because people changed, but because the aggregation unit changed. Densely populated urban counties can show Republican-majority by county even when the total votes within them favor Democrats, if the urban census tracts are overwhelmingly Democratic but a large fraction of the county's land area is rural.

---

## Dot Density Maps

```
DOT DENSITY MAPS — MECHANICS AND APPROPRIATE USE
══════════════════════════════════════════════════════════════════════

  DEFINITION:
  Each dot represents a fixed count of the variable.
  Dots placed randomly within the geographic unit.

  Example: US population map
  - 1 dot = 1,000 people
  - Each county gets N dots placed randomly within its boundary
  - Dense clusters of dots = high population
  - Empty areas = low population

  STRENGTHS:
  ├── Shows raw counts (not just rates) — you see scale
  ├── The dot density visually represents the data
  ├── Works for multiple categories (different colored dots
  │   for Republican and Democratic voters, for example)
  └── More honest than choropleth for sparse populations
      (a huge, sparsely populated county doesn't "fill in"
       as uniformly dark the way choropleth does)

  WEAKNESSES:
  ├── Dots don't show actual locations within the unit
  │   (randomly placed within county — may be in a lake)
  ├── Reading absolute values requires counting or estimating
  ├── Overlapping dots at high density become unreadable
  └── 1-dot-N-people ratio requires calibration per dataset

  THE RACIAL DOT MAP (2010 US Census):
  ┌──────────────────────────────────────────────────────────┐
  │  1 dot = 1 person; color = race/ethnicity               │
  │  308 million dots rendered at full resolution            │
  │  Makes segregation patterns immediately visible          │
  │  Technically challenging: rendering 300M dots at         │
  │  interactive zoom required tile-based vector rendering   │
  └──────────────────────────────────────────────────────────┘

══════════════════════════════════════════════════════════════════════
```

---

## Proportional Symbol Maps

```
PROPORTIONAL SYMBOL MAPS — DESIGN AND PERCEPTION
══════════════════════════════════════════════════════════════════════

  DEFINITION:
  Symbols (circles, squares, icons) scaled to variable value.
  Positioned at the location the data represents.

  CIRCLE AREA vs RADIUS CONFUSION:
  ┌──────────────────────────────────────────────────────────┐
  │  If city A has 2× the population of city B:             │
  │                                                          │
  │  CORRECT: scale circle AREA proportionally              │
  │  Area = π·r²  →  r = √(value/π·k)                       │
  │  Doubling value → circle ~1.41× bigger in radius        │
  │                                                          │
  │  COMMON ERROR: scale circle RADIUS proportionally       │
  │  Doubling value → circle 4× bigger in area              │
  │  This exaggerates differences between large values       │
  │                                                          │
  │  Perceptual reality: people underestimate circle area    │
  │  Flannery correction: overscale by 0.57 exponent        │
  │  (empirically matches perception) — rarely used          │
  └──────────────────────────────────────────────────────────┘

  GRADUATED vs PROPORTIONAL:
  Graduated: a few discrete size classes (small/medium/large)
  Proportional: continuously scaled to value
  Graduated: cleaner; loses detail
  Proportional: more precise; harder to read

  OVERLAPPING SYMBOLS:
  Major problem when many symbols exist in a small area.
  Solutions:
  ├── Transparency (α blending)
  ├── Offset (move overlapping symbols slightly)
  ├── Hollow symbols (show overlap through stacking)
  └── Zoom/interaction (web maps: expand on click)

══════════════════════════════════════════════════════════════════════
```

---

## Isoline / Isopleth Maps

```
ISOLINE MAPS — TYPES AND CONSTRUCTION
══════════════════════════════════════════════════════════════════════

  An isoline connects all points with equal value.

  Common types:
  ├── CONTOUR LINES: equal elevation (topographic maps)
  │   Most common; 20m or 40m or 100m intervals typical
  ├── ISOBARS: equal atmospheric pressure (weather maps)
  ├── ISOTHERMS: equal temperature
  ├── ISOHYETS: equal rainfall
  ├── ISOSEISMALS: equal earthquake intensity
  └── ISOPLETHS: equal value of any ratio variable

  CONSTRUCTION (pre-digital):
  ┌──────────────────────────────────────────────────────────┐
  │  1. Sample points with known values across area          │
  │  2. Interpolate between known points                     │
  │  3. Connect equal-value interpolated positions           │
  │                                                          │
  │  Interpolation method matters:                           │
  │  - Linear: simple, discontinuous at sample points        │
  │  - IDW (Inverse Distance Weighting): smoother            │
  │  - Kriging: geostatistical, accounts for spatial         │
  │    autocorrelation (assumes nearby points more similar)  │
  └──────────────────────────────────────────────────────────┘

  READING CONTOUR MAPS:
  ┌──────────────────────────────────────────────────────────┐
  │  Close contour spacing → steep slope                     │
  │  Wide spacing → gentle slope                             │
  │  Closed concentric contours → hill (or depression)       │
  │  V-shape pointing uphill → valley (V = Valley)           │
  │  V-shape pointing downhill → ridge (same rule, reversed) │
  │  Hachure marks on contours → depression (bowl)           │
  └──────────────────────────────────────────────────────────┘

══════════════════════════════════════════════════════════════════════
```

---

## Cartograms

```
CARTOGRAMS — DISTORTING GEOGRAPHY TO SHOW DATA
══════════════════════════════════════════════════════════════════════

  DEFINITION:
  A cartogram replaces geographic area with a data variable.
  Regions are enlarged/shrunk to be proportional to the variable.

  TYPES:
  ├── CONTIGUOUS: regions maintain adjacency relationships
  │   Borders still touch; regions distorted
  │   Dorling cartogram: replace regions with proportional circles
  │   (maintains centers, loses adjacency)
  │
  ├── NON-CONTIGUOUS: regions maintain shape, scaled separately
  │   White space between regions
  │   Cleaner shapes; loses geographic context
  │
  └── TILE-GRID CARTOGRAM: each region = equal-size tile
      Hex maps of US states: each state gets 1 hexagon
      (Wyoming and California have equal visual weight)
      Best for fair comparison of uniform-unit data

  EXAMPLES:
  ┌──────────────────────────────────────────────────────────┐
  │  Electoral map (votes):                                   │
  │  Geographic: US looks mostly Republican (land area)      │
  │  Vote cartogram: proportional to electoral votes         │
  │  Population cartogram: proportional to population        │
  │  Each shows a different truth about the same election    │
  └──────────────────────────────────────────────────────────┘

  WORLDMAPPER (www.worldmapper.org):
  ├── 700+ cartograms of global data
  ├── World population cartogram: Asia dominates
  ├── World income cartogram: US/Europe dominate
  ├── Malaria cartogram: Sub-Saharan Africa dominates
  └── The visual contrast between maps reveals inequality

  CONSTRUCTION CHALLENGE:
  Contiguous cartograms require solving an optimization problem:
  distort region areas to target values while maintaining
  contiguity and minimizing shape distortion.
  Algorithms: Dougenik/Chrisman/Niemeyer (1985), diffusion-based
  (Gastner/Newman 2004), flow-based.
  Computationally expensive for large datasets.

══════════════════════════════════════════════════════════════════════
```

---

## Flow Maps

Flow maps encode movement, trade, or transfer as lines with width proportional to volume. Minard invented the form; it has many descendants.

```
FLOW MAPS — DESIGN PRINCIPLES
══════════════════════════════════════════════════════════════════════

  MINARD'S ORIGINAL INSIGHTS:
  ├── Width of flow = volume/quantity
  ├── Direction encoded in color or arrowhead
  ├── Start/end points anchored geographically
  └── Multiple flows can overlay (but get messy quickly)

  MODERN VARIATIONS:
  ├── OD (Origin-Destination) matrix visualization:
  │   Lines between all origin-destination pairs
  │   Width = volume; color = direction/type
  │   Problem: N cities = N² lines = spaghetti
  │   Solution: filter to significant flows only
  │
  ├── Radial flow: all lines from one origin
  │   (flight map from hub city)
  │   Shows connectivity, volume from one source
  │
  ├── Sankey diagram: flow as area-preserving streams
  │   Energy flows, budget allocations, material flows
  │   Technically a flow chart; often overlaid on map
  │
  └── Animated flow: particles moving along routes
      (real-time data: ship AIS, aircraft, Twitter activity)

  DESIGN CHALLENGES:
  ├── Crossing lines obscure relationships
  ├── Bidirectional flows overlap (use parallel offset)
  ├── Very different magnitudes → thin flows invisible
  └── Scale: work globally but hard to read locally

══════════════════════════════════════════════════════════════════════
```

---

## Map Type Decision Framework

```
THEMATIC MAP TYPE SELECTION
══════════════════════════════════════════════════════════════════════════

  START HERE:
  ↓
  What is your data geometry?
  ├── POINTS → proportional symbol, dot, heat map
  ├── LINES → flow map
  └── POLYGONS → choropleth, cartogram

  If POLYGONS:
  ↓
  Is your variable normalized (rate/ratio) or count?
  ├── COUNT: be very careful with choropleth
  │   (big regions look more significant)
  │   Consider dot map or proportional symbol instead
  └── RATE/RATIO: choropleth appropriate

  If CHOROPLETH:
  ↓
  What color scheme?
  ├── Sequential (light→dark): one variable, one direction
  │   (e.g., income: white=low, dark blue=high)
  ├── Diverging (two colors from center): ±deviation from midpoint
  │   (e.g., above/below average, vote swing)
  └── Qualitative (distinct colors): categorical data
      (e.g., land use type, party affiliation)

  Do you want to compare area-proportional values?
  └── CARTOGRAM: distort regions to be proportional to data

  Are you showing movement/flow?
  └── FLOW MAP: Minard-style proportional width flows

  Are you showing a continuous field (temperature, elevation)?
  └── ISOLINE or RASTER SURFACE (heat map)

══════════════════════════════════════════════════════════════════════════
```

---

## The Argument Embedded in Every Thematic Map

Two data scientists mapping the same election results will produce maps that look completely different depending on:
- Geographic unit (county vs census tract vs precinct)
- Variable (total votes vs margin vs vote share)
- Color scheme (continuous vs classed; which colors)
- Map projection (geographic area vs population area)
- What to do with 3rd-party votes (combine? separate?)

None of these choices is uniquely correct. Each produces a different argument. The responsible thematic mapper:

1. Chooses the unit of analysis that matches the phenomenon being studied
2. Normalizes where appropriate (rate, not count, for area-variable phenomena)
3. Labels the map clearly: what does a unit represent?
4. Chooses a color scheme appropriate to the data type
5. States the data source, date, and classification method

The irresponsible thematic mapper chooses the combination that most strongly supports a predetermined conclusion and presents it as objective.

---

## Common Confusion Points

**"Choropleth maps are always about rates."** Not always — but they *should* use rates when regions vary greatly in population or area. Absolute count choropleths are systematically misleading.

**"Minard's map is great data visualization."** Yes, but it's also a thematic map making an argument about historical causation (cold killed the army). The visualization's power comes from how it reveals causation through the temperature-loss correlation.

**"Cartograms are more accurate than regular maps."** A population cartogram is more accurate for population comparisons. A geographic map is more accurate for area comparisons. Neither is "more accurate" in general — they answer different questions.

**"The MAUP is a statistical artifact, not a design concern."** MAUP is fundamental. Gerrymandering is MAUP weaponized as politics. Ecological fallacy (inferring individual behavior from aggregate statistics) is MAUP's epistemic consequence. These matter.

---

## Decision Cheat Sheet

| Show: | Use: | Avoid: |
|-------|------|--------|
| Count by region | Proportional symbol or dot density | Choropleth (raw counts) |
| Rate/ratio by region | Choropleth | None (this is correct use) |
| Point locations with count | Proportional symbol or dot density | Choropleth |
| Population-fair comparison | Cartogram or hex map | Geographic choropleth |
| Continuous field | Isoline or raster | Choropleth |
| Movement/flow | Flow map | Any non-flow type |
| Two variables simultaneously | Bivariate choropleth | Overlapping single-variable |
| Time change | Small multiples or animation | Single static map |
