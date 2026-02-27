# Cartography — Overview

## Maps as Compressed Worldview

A map is not a picture of the world. It is an argument about the world — which features matter, how large things are relative to each other, what belongs at the center, and what gets omitted entirely. Every cartographic choice encodes a perspective. Understanding cartography means understanding that compression is always lossy, and the loss is never neutral.

```
THE CARTOGRAPHIC STACK
═══════════════════════════════════════════════════════════════════════

  REALITY: 3D rotating ellipsoidal Earth with complex terrain
           covered in cultural and physical features

  ↓  GEODESY: measure the actual shape precisely
     (geoid, reference ellipsoid, datum — see 05-TRIANGULATION)

  ↓  PROJECTION: map curved surface → flat plane
     (introduces distortion — shape, area, distance, direction)
     (one property preserved at cost of others — see 04-PROJECTIONS)

  ↓  SCALE: decide level of abstraction
     (1:1,000 = detailed; 1:50,000,000 = continental)

  ↓  GENERALIZATION: simplify features for chosen scale
     (coastlines, road networks, label density)

  ↓  SYMBOLIZATION: encode information as visual variables
     (color, size, shape, pattern, orientation, value)

  ↓  MAP: flat, bounded, finite representation
     (always a lie — the useful kind)

═══════════════════════════════════════════════════════════════════════
```

This is structurally analogous to compilation. You start with a rich, multi-dimensional source (the world) and apply a series of lossy transformations to produce a target artifact optimized for a specific use case (navigation, analysis, argument). The chain is: measurement → projection → abstraction → symbolization → rendering. Change any parameter and you get a different artifact from the same source.

---

## The Fundamental Impossibility

Gauss proved it in 1827: a sphere cannot be mapped to a plane without distortion. This is not a technology limitation — it is a theorem.

```
GAUSSIAN CURVATURE — THE CORE PROBLEM
══════════════════════════════════════════════════════════════

  Gaussian curvature K = κ₁ × κ₂
  (product of principal curvatures at a point)

  Sphere:  K = 1/r²  > 0  (positive — curves in both directions)
  Plane:   K = 0          (flat)

  Theorema Egregium (Gauss, 1827):
  Gaussian curvature is an intrinsic property — invariant
  under any isometric (distance-preserving) transformation.

  ∴  No isometric map from sphere to plane is possible.

  Translation: You CANNOT preserve all of these simultaneously:
  ┌────────────────────────────────────────────────────────┐
  │  AREA      — regions have correct relative sizes       │
  │  SHAPE     — angles preserved at every point          │
  │  DISTANCE  — distances to/from one point correct      │
  │  DIRECTION — bearing between any two points correct   │
  └────────────────────────────────────────────────────────┘

  Every projection preserves some subset at cost of others.
  The choice of projection is the choice of acceptable lies.

══════════════════════════════════════════════════════════════
```

This connects directly to differential geometry: a sphere is a 2-manifold with constant positive curvature; a Euclidean plane is the flat manifold. Any smooth mapping between them has nonzero distortion tensor somewhere. Cartographic projections differ in *where* and *what kind* of distortion they accept.

---

## Map Type Taxonomy

```
MAP TYPES — FULL TAXONOMY
═══════════════════════════════════════════════════════════════════════════════

  PRIMARY PURPOSE
  ├── REFERENCE MAPS — "where is this?"
  │   ├── Topographic  — terrain, elevation, named features
  │   ├── Road/street  — transportation network
  │   ├── Political    — borders, capitals, admin divisions
  │   ├── Nautical chart — depths (bathymetry), hazards, aids to nav
  │   └── Aeronautical — airways, airspace, elevation (for pilots)
  │
  ├── THEMATIC MAPS — "what quantity varies where?"
  │   ├── Choropleth     — shaded regions by variable (GDP, votes)
  │   ├── Dot density    — dots proportional to count
  │   ├── Proportional symbol — circles/squares scaled to value
  │   ├── Isoline/isopleth   — contour lines (elevation, temperature)
  │   ├── Cartogram      — area distorted by data variable
  │   ├── Flow map       — lines showing movement/volume
  │   └── Heat map       — continuous density surface
  │
  └── NAVIGATIONAL MAPS — "how do I get there?"
      ├── Portolan chart  — medieval sailing directions
      ├── Mercator chart  — rhumb line navigation
      ├── Great circle charts — shortest path (air/sea)
      └── Digital turn-by-turn — routed graph with real-time data

  SCALE RANGES
  ├── Large scale    — 1:1,000 to 1:50,000   (detailed, small area)
  ├── Medium scale   — 1:50,000 to 1:500,000 (regional)
  └── Small scale    — 1:500,000+             (continental, world)

  NOTE: "large scale" = large ratio = zoomed in (confusingly named)
        1:1,000 shows more detail than 1:1,000,000

═══════════════════════════════════════════════════════════════════════════════
```

The reference/thematic/navigational trichotomy cuts across a separate axis: *what is the primary abstraction?* Reference maps prioritize location accuracy. Thematic maps prioritize data encoding. Navigational maps prioritize route affordance. The same underlying geodata generates all three.

---

## Historical Arc

```
CARTOGRAPHIC HISTORY — TIMELINE OF BREAKTHROUGHS
══════════════════════════════════════════════════════════════════════════════

  600 BCE  Babylonian World Map (clay tablet)
           ┌────────────────────────────────────────────────────────┐
           │ Ocean ring surrounding disk of earth                   │
           │ Babylon at center; mythological outer regions          │
           │ PURPOSE: cosmological / sacred, not navigational       │
           └────────────────────────────────────────────────────────┘

  ~150 CE  Ptolemy's Geographia
           ┌────────────────────────────────────────────────────────┐
           │ Coordinate system: latitude/longitude                  │
           │ Conic projection (first systematic projection)         │
           │ 8,000 named places with coordinates                    │
           │ PURPOSE: geographic reference, first "scientific" map  │
           │ PROBLEM: Mediterranean ~25% too long (cumulative error)│
           └────────────────────────────────────────────────────────┘

  4th–5th c  Peutinger Table (Roman itinerary)
           ┌────────────────────────────────────────────────────────┐
           │ Distance between places, not geographic accuracy       │
           │ Roads, towns, way stations across Roman Empire         │
           │ PURPOSE: logistics and military routing                │
           └────────────────────────────────────────────────────────┘

  ~1300    T-O Maps (mappa mundi)
           ┌────────────────────────────────────────────────────────┐
           │ Jerusalem at center, East at top, Ocean surrounding    │
           │ Theological cosmography, not navigation                │
           │ Hereford Mappa Mundi (~1300) — most famous example    │
           └────────────────────────────────────────────────────────┘

  13th c.  Portolan Charts
           ┌────────────────────────────────────────────────────────┐
           │ Mediterranean sailing charts — empirically accurate    │
           │ No coordinate grid; purely measurement-based           │
           │ Compass rose network, accurate coastlines              │
           │ PURPOSE: navigation. Accurate without theory.          │
           └────────────────────────────────────────────────────────┘

  1406     Ptolemy rediscovered in Western Europe (Florence)
  1492     Columbus crosses Atlantic using dead reckoning
  1507     Waldseemüller names America — maps naming the world
  1569     Mercator's projection
           ┌────────────────────────────────────────────────────────┐
           │ Rhumb lines as straight lines                          │
           │ The navigator's essential tool for 400+ years          │
           │ Area distortion at poles accepted as trade-off         │
           └────────────────────────────────────────────────────────┘

  1600s–   National Triangulation Surveys
  1800s    ┌────────────────────────────────────────────────────────┐
           │ France, Britain, India — precision measurement         │
           │ Establishes accurate base for national topographic maps│
           │ Discovers Earth is oblate spheroid, not perfect sphere │
           └────────────────────────────────────────────────────────┘

  1854     John Snow's cholera map — thematic mapping as science
  1869     Minard's Napoleon campaign map — 6 variables, 2D plane

  1900s    Aerial photography → photogrammetry → systematic coverage
  1960s    Corona satellite — first overhead imagery of denied areas
  1960s    Roger Tomlinson's GIS — Canada Land Inventory
           ┌────────────────────────────────────────────────────────┐
           │ Maps become computable data, not just documents        │
           └────────────────────────────────────────────────────────┘

  1972     Landsat 1 — first civilian multispectral satellite
  1978     GPS satellites begin launching (NAVSTAR)
  1995     GPS fully operational (24 satellites); Corona declassified
  2000     Selective Availability removed — 10m accuracy for all
  2004     OpenStreetMap founded
  2005     Google Maps launches — the AJAX slippy map revolution
  2010s    LiDAR archaeology; drone surveys; vector tiles
  2020s    Planet Labs — daily imaging of entire Earth's surface

══════════════════════════════════════════════════════════════════════════════
```

The key inflection points:

**Ptolemy (~150 CE)**: Introduced coordinates — the idea that location is a mathematical tuple, not a narrative description. This is the foundational abstraction. Lost in Western Europe for 1,200 years, then rediscovered and triggered the Age of Exploration.

**Portolan charts (13th c.)**: Demonstrated that empirical measurement could beat theory for practical accuracy. Surveyors with compasses produced better sailing charts than scholars with Ptolemy's system. Accuracy from practice, not from having the right model.

**Mercator (1569)**: Solved the navigator's core problem — plot a constant bearing as a straight line. Required a non-trivial mathematical transformation (the integral of the secant function, though Mercator himself used a geometric construction). Conformal but not equal-area.

**Triangulation surveys (1600s–1800s)**: Made maps legally defensible. National borders, property lines, tax assessments — all required precision that itinerary distances couldn't provide. Geodesy became a state function.

**GIS (1960s)**: Decoupled the map from the paper. Geographic data became queryable, layerable, analyzable. Maps became outputs of computation rather than primary documents. This is the shift from artifact to data structure.

**GPS + Web (2000–2005)**: Democratized both position knowledge and map consumption. Slippy maps on mobile phones made every person a real-time GPS-tracked entity on a queryable map. Combined with OSM's crowd-sourced data model, maps became a platform rather than a product.

---

## The Projection Zoo — Preview

```
PROJECTION TRADEOFF SPACE
══════════════════════════════════════════════════════════════

  PRESERVE AREA              PRESERVE SHAPE
  (equal-area)               (conformal)
       │                          │
  Mollweide               Mercator (cylindrical)
  Gall-Peters             Lambert Conformal Conic
  Goode's Homolosine      Stereographic
  Albers Equal-Area       Transverse Mercator
       │                          │
       └──────────┬───────────────┘
                  │
            COMPROMISE
            (neither perfectly)
            ├── Robinson
            ├── Winkel Tripel (National Geographic standard)
            └── Natural Earth

  SPECIAL PURPOSE:
  ├── Gnomonic     — great circles as straight lines (navigation)
  ├── Azimuthal equidistant — distances from center correct (polar)
  └── Orthographic — looks like globe from space (aesthetic)

══════════════════════════════════════════════════════════════
```

Full treatment with mathematics in 04-PROJECTIONS.md.

---

## Bridges

**Mathematics**: Gaussian curvature, differential geometry, first and second fundamental forms of surfaces. Map projections are explicit constructions in Riemannian geometry. The Tissot indicatrix (a small circle on the Earth rendered through a projection) is the geometric visualization of the local distortion tensor at each point. Where the indicatrix is circular, the projection is locally conformal; where it is equal-area, all indicatrices have equal area.

**Astronomy**: Celestial navigation (finding position via star angles) fed directly into cartography — latitude from pole star altitude, longitude from lunar distances or chronometers. The transit of Venus expeditions (Cook, 1769) were simultaneously astronomical events and cartographic expeditions that produced the first accurate Pacific charts.

**Computing/GIS**: Modern digital cartography is a database plus rendering problem. A Web Mercator tile server is a function `(z, x, y) → PNG` over a spatially indexed database. The slippy map is a UI pattern built on lazy tile loading via HTTP. PostGIS extends PostgreSQL with spatial types and the full suite of geometric/geographic operators.
The tile scheme is a **quadtree**: zoom level z gives a 2^z x 2^z grid, and tile (z,x,y) contains exactly 4 children at (z+1, 2x, 2y), (z+1, 2x+1, 2y), (z+1, 2x, 2y+1), (z+1, 2x+1, 2y+1). The tile URL encodes the quadtree path. This is the same spatial indexing structure used in spatial databases (R-tree) and game engines (octree).

**GIS as spatial database**: GIS = relational database + geometry column type + spatial index (R-tree) + spatial predicates (ST_Intersects, ST_DWithin, ST_Buffer). Tomlinson's 1963 insight was that **map overlay = relational join** — two thematic layers overlaid spatially is the same operation as joining two tables on a shared key. PostGIS is PostgreSQL extended with this. Any database-familiar engineer can reason about GIS operations as SQL with a geometry type.

**Data visualization**: Thematic maps are a specialized subclass of information visualization. The design principles for effective maps overlap heavily with Tufte's principles for statistical graphics — data-ink ratio, avoiding chartjunk, encoding data in appropriate visual variables (color hue vs lightness vs size).

---

## What a Map Is Not

A map is not objective. Every map:

- **Has a projection** — chooses which distortion to accept
- **Has a scale** — decides what is too small to show
- **Has an extent** — decides what is off the edge
- **Has a center** — communicates (often implicitly) what is important
- **Has a symbolization scheme** — encodes judgment about feature relationships
- **Was made for a purpose** — that purpose shapes every choice

The Mercator projection makes Europe look large relative to Africa because that served 16th-century European navigators. The Peters projection was marketed as corrective by making Africa look proportionally large, but introduced its own shape distortions. Both are arguments. Neither is "correct." The question is always: correct for what purpose?

Understanding this is the meta-skill: any map you encounter is the output of a long chain of choices made by people with specific purposes, audiences, and often agendas. Reading a map well means reading the choices, not just the content.

---

## Module Guide

| File | Topic | Key Concepts |
|------|-------|-------------|
| 01-ANCIENT-MAPS | Babylonian to medieval | What maps were for before accuracy mattered |
| 02-PORTOLAN-CHARTS | Medieval sailing charts | Empirical accuracy without theory |
| 03-AGE-OF-EXPLORATION | 1400–1800 expansion | Maps as state secrets; naming the New World |
| 04-PROJECTIONS | The math of flattening | Mercator, equal-area, compromise projections |
| 05-TRIANGULATION-GEODESY | Measuring Earth precisely | Triangulation, geoid, WGS84, datum |
| 06-THEMATIC-MAPS | Maps as argument | Snow, Minard, choropleth, cartogram |
| 07-AERIAL-REMOTE-SENSING | Seeing from above | Photogrammetry, Landsat, LiDAR, SAR |
| 08-GIS | Geographic information systems | Vector/raster, PostGIS, spatial queries |
| 09-GPS-DIGITAL | GPS to Google Maps | Trilateration, slippy maps, OSM |
| 10-CARTOGRAPHIC-DESIGN | Making effective maps | Color, hierarchy, typography, propaganda |

## Decision Cheat Sheet

| Task | Approach | Why |
|------|----------|-----|
| Choropleth (area comparison) map | Equal-area projection (Albers, Mollweide) | Area must be preserved for visual comparison of density/rate data |
| Navigation / bearing measurement | Conformal projection (Mercator) | Angles preserved = constant compass bearing = straight rhumb lines |
| Web mapping application | EPSG:3857 (Web Mercator) + Leaflet or MapboxGL | Industry standard tile system; all basemaps use this CRS |
| Spatial SQL queries on geodata | PostGIS (PostgreSQL + spatial extension) | Full SQL + geometry types + R-tree spatial index + OGC predicates |
| Survey-grade positioning (cm) | RTK GPS (Real-Time Kinematic) | Carrier-phase corrections give cm-level accuracy vs. m-level standalone |
| Satellite/aerial image analysis | QGIS or Google Earth Engine | Raster analysis, multispectral bands, change detection |
| Offline field data collection | QField (mobile QGIS) or ArcGIS Field Maps | GPS-tagged feature collection with custom attribute forms |
| Global thematic comparison | Robinson or Natural Earth projection | Compromise projections — neither conformal nor equal-area but visually balanced |

---

## Common Confusion Points

**"EPSG:4326 and EPSG:3857 are the same — both use WGS84"**
False. EPSG:4326 is WGS84 geographic coordinates (latitude/longitude in degrees). EPSG:3857 is Web Mercator (x/y in meters, using a spherical approximation of WGS84). They have different units, different projections, and different coordinate ranges. Mixing them without reprojection produces wildly incorrect results.

**"Web Mercator is standard Mercator"**
False. Web Mercator uses a spherical approximation (EPSG:3857) while standard Mercator uses the WGS84 ellipsoid. The difference is ~0.33% — negligible for web mapping but unacceptable for geodetic work or legal survey boundaries.

**"GIS = ArcGIS"**
GIS is the discipline. ArcGIS (Esri) is one commercial implementation. QGIS (open-source), PostGIS (spatial database), GRASS, and Google Earth Engine are equally valid tools. The conceptual framework (spatial data + topology + overlay analysis) is tool-independent.

**"GPS uses triangulation"**
GPS uses **trilateration** (distance measurement from known positions), not triangulation (angle measurement). Each satellite provides a sphere of constant distance; the intersection of 4+ spheres gives the receiver position. Triangulation uses angles; trilateration uses distances.

**"A map with a north arrow is always north-up"**
The north arrow exists precisely because the map may not be north-up. Many navigation maps, building plans, and oblique-view maps orient differently. The arrow tells you which way is north on that specific map.
