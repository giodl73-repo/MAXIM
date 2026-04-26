# 04 — Map Projections

## The Unsolvable Problem

Projections are the core theoretical problem in cartography. The impossibility result is clean: Gauss proved in 1827 that no smooth mapping from a sphere to a plane can preserve all metric properties. Every map projection is a specific choice of which distortions to accept in exchange for which properties to preserve.

```
THE DISTORTION IMPOSSIBILITY — FORMAL STATEMENT
══════════════════════════════════════════════════════════════════════

  Gauss's Theorema Egregium (1827):
  ────────────────────────────────
  Gaussian curvature K is an intrinsic invariant.
  It is preserved by any isometry (distance-preserving map).

  Sphere: K = 1/R² > 0  (everywhere)
  Plane:  K = 0         (everywhere)

  Since K(sphere) ≠ K(plane), no isometry exists between them.

  Therefore: every projection must introduce distortion.

  The four properties that cannot simultaneously be preserved:
  ┌──────────────────────────────────────────────────────────────┐
  │  CONFORMAL (shape-preserving):                               │
  │  Angles between curves preserved at every point              │
  │  Local shapes correct; area wrong                            │
  │                                                              │
  │  EQUAL-AREA (area-preserving):                               │
  │  Areas of regions proportional to their true areas           │
  │  Area correct; local shapes distorted                        │
  │                                                              │
  │  EQUIDISTANT (distance-preserving):                          │
  │  Distances from one or two specific points correct           │
  │  Cannot be globally equidistant                              │
  │                                                              │
  │  GNOMONIC (great-circle-preserving):                         │
  │  Great circles (shortest paths) render as straight lines     │
  │  Strong distortion of both area and shape away from center   │
  └──────────────────────────────────────────────────────────────┘

  A projection can preserve at most one of conformal or equal-area.
  (These are mutually exclusive everywhere except at a tangent point.)

══════════════════════════════════════════════════════════════════════
```

The mathematical content: a projection is a smooth map f: S² → ℝ². The distortion at each point is captured by the metric tensor pulled back through f. If f is conformal, the metric tensor at each point is a scalar multiple of the identity (angles preserved, distances scaled uniformly). If f is equal-area, the Jacobian of f has determinant equal to 1 (or a constant) at each point. These two conditions cannot simultaneously hold everywhere because the Gaussian curvature of S² is nonzero.

---

## The Tissot Indicatrix

The standard visualization tool for projection distortion is the Tissot indicatrix, introduced by Nicolas Auguste Tissot in 1859.

```
TISSOT INDICATRIX — WHAT IT SHOWS
══════════════════════════════════════════════════════════════════════

  Concept: Draw a tiny circle on the sphere at each grid point.
           Project it through the map projection.
           The resulting shape reveals the local distortion.

  Possible shapes:
  ┌──────────────────────────────────────────────────────────────┐
  │  Circle (same size): no distortion (impossible globally)     │
  │  Circle (different sizes): equal-area, scale varies          │
  │  Ellipse (equal area): conformal → shape distorted           │
  │  Ellipse (different area): neither                           │
  │  Ellipse with equal semi-axes: conformal at that point       │
  └──────────────────────────────────────────────────────────────┘

  On a conformal projection (Mercator):
  - All indicatrices are circles
  - But circles at high latitudes are larger than at equator
  - Greenland looks the same shape as a circle at equator
  - But it appears much larger (because the circle is bigger)

  On an equal-area projection (Mollweide):
  - All indicatrices have equal area
  - But the circles at high latitudes are elongated ellipses
  - Regions look squashed toward the poles

══════════════════════════════════════════════════════════════════════
```

The Tissot indicatrix is the projection equivalent of the error ellipsoid in measurement theory — a geometric representation of the distortion tensor at each point, making the abstract linear algebra visible.

---

## Projection Families

```
PROJECTION FAMILIES — CLASSIFICATION TREE
════════════════════════════════════════════════════════════════════

  By projection surface:
  ├── CYLINDRICAL: sphere projected onto cylinder
  │   ├── Standard: cylinder tangent at equator
  │   │   Mercator, Plate Carée (equirectangular), Miller
  │   └── Transverse: cylinder tangent at a meridian
  │       Transverse Mercator (UTM uses this)
  │
  ├── CONIC: sphere projected onto cone
  │   ├── Albers Equal-Area Conic
  │   ├── Lambert Conformal Conic
  │   └── Polyconic (older US survey standard)
  │
  ├── AZIMUTHAL (planar): sphere projected onto tangent plane
  │   ├── Gnomonic — great circles as straight lines
  │   ├── Stereographic — conformal, used for polar regions
  │   ├── Lambert Azimuthal Equal-Area
  │   └── Azimuthal Equidistant
  │
  └── PSEUDO-CYLINDRICAL: meridians are curves, not lines
      ├── Mollweide — equal-area, oval world
      ├── Robinson — compromise, used by National Geographic 1988–98
      └── Winkel Tripel — compromise, National Geographic current

  By property:
  ├── CONFORMAL: Mercator, Lambert Conformal Conic, Stereographic
  ├── EQUAL-AREA: Albers, Mollweide, Gall-Peters, Lambert AEA
  ├── EQUIDISTANT: Azimuthal Equidistant (from center only)
  ├── GNOMONIC: Gnomonic (great circles only)
  └── COMPROMISE: Robinson, Winkel Tripel, Natural Earth

════════════════════════════════════════════════════════════════════
```

---

## Mercator Projection (1569) — The Navigator's Solution

Gerardus Mercator's 1569 world map introduced the projection that bears his name. The driving requirement was navigational: a sailor needed to be able to plot a constant compass bearing as a straight line on the chart.

```
MERCATOR PROJECTION — MATHEMATICS AND PROPERTIES
══════════════════════════════════════════════════════════════════════

  The navigational requirement:
  ┌────────────────────────────────────────────────────────────┐
  │  A rhumb line (loxodrome) = path of constant compass bearing│
  │  On a sphere: spirals toward pole (never reaches it)       │
  │  On a Mercator chart: straight line                        │
  │                                                            │
  │  Navigator's use: draw straight line from current pos      │
  │  to destination → read bearing → steer that bearing        │
  │  → arrive (approximately)                                  │
  └────────────────────────────────────────────────────────────┘

  Mathematical construction:
  ┌────────────────────────────────────────────────────────────┐
  │  Standard parametrization:                                 │
  │  x = R·λ  (longitude → x, linear)                          │
  │  y = R·ln|tan(π/4 + φ/2)|  (latitude → y, nonlinear)       │
  │                                                            │
  │  Where φ = latitude, λ = longitude, R = Earth radius       │
  │                                                            │
  │  The y formula is the Gudermannian function's inverse.     │
  │  Mercator arrived at this geometrically; Edward Wright     │
  │  (1599) provided the mathematical derivation — it requires │
  │  computing ∫ sec(φ)dφ, which is the integral of secant.    │
  │  This was a hard problem in 1569 (calculus didn't exist).  │
  └────────────────────────────────────────────────────────────┘

  Properties:
  ├── Conformal: angles preserved locally (rhumb lines work)
  ├── Not equal-area: scale factor = 1/cos(φ) = sec(φ)
  │   At equator (φ=0): scale factor = 1
  │   At 60° latitude:  scale factor = 2   (2× too big)
  │   At 75° latitude:  scale factor = 3.9 (4× too big)
  │   At 85° latitude:  scale factor = 11  (11× too big)
  ├── Poles: cannot be shown (y → ±∞ as φ → ±90°)
  └── Great circles: curves (except equator and meridians)

  The Greenland problem:
  ┌────────────────────────────────────────────────────────────┐
  │  Greenland: actual area ~2.2 million km²                   │
  │  Africa:    actual area ~30 million km²  (14× larger)      │
  │  On Mercator: Greenland appears about the same size Africa │
  │  Because Greenland is at ~60-80°N; scale factor ~2-6×      │
  └────────────────────────────────────────────────────────────┘

══════════════════════════════════════════════════════════════════════
```

The Mercator projection was not "adopted by imperialists to make Europe look big." It was adopted by navigators because it made compass navigation work. The fact that it makes high-latitude regions (which include most of Europe, all of Canada, all of Russia) appear large relative to equatorial regions (which include most of Africa, South Asia, equatorial South America) has political implications — those implications were not Mercator's intent, but they are real.

### The Peters Controversy

In 1974, Arno Peters published his "Peters Projection" — a cylindrical equal-area projection that he claimed was a corrective to the Mercator projection's inherent imperialism. The controversy is illuminating:

```
GALL-PETERS CONTROVERSY
══════════════════════════════════════════════════════════════════════

  Peters's claims (1974):
  - His projection is the only "fair" map (equal-area)
  - Mercator deliberately distorts to make Europe look large
  - All previous cartographers conspired in this distortion
  - His projection is "new" (he coined "Peters Projection")

  Problems:
  ├── Not new: James Gall published the identical projection in 1855
  │   It's correctly called the Gall-Peters projection
  │
  ├── Equal-area but shape-distorting:
  │   Africa and South America appear vertically elongated
  │   High latitudes appear horizontally stretched
  │   Shapes are as distorted as Mercator — just differently
  │
  ├── Not the only equal-area projection:
  │   Mollweide (1805), Goode's Homolosine (1923), Lambert (1772)
  │   all predate Peters and have better aesthetic properties
  │
  └── The "conspiracy" claim:
      Mercator was adopted for navigation, not politics.
      Navigational use does not require nor imply political endorsement.

  What Peters got right:
  ├── Equal-area projections have real value for area comparison
  ├── Projection choice does have real-world perception effects
  └── The dominant world map projection (Mercator) is genuinely
      not appropriate for general audience use (school maps, etc.)

  Resolution (1988+):
  National Geographic switched from Van der Grinten to Robinson (1988)
  National Geographic switched from Robinson to Winkel Tripel (1998)
  UN uses Robinson (compromise)
  Cartographic profession consensus: Winkel Tripel or Robinson
  for general audience world maps

══════════════════════════════════════════════════════════════════════
```

The Peters controversy clarified something important: projection choice is a design decision with ethical dimensions, but the ethical analysis requires accuracy. Claiming that Mercator is uniquely evil misrepresents the history; claiming that projection choice has no political implications understates the real effect of visual representation on perception.

---

## Equal-Area Projections

```
EQUAL-AREA PROJECTION COMPARISON
══════════════════════════════════════════════════════════════════════

  MOLLWEIDE (1805):
  - Oval outline; meridians as ellipses; parallels as straight lines
  - Equal-area everywhere
  - Shape distortion: moderate in center, severe at edges
  - Best use: world thematic maps where area comparison matters

  GOODE'S HOMOLOSINE (1923):
  - Sinusoidal for equatorial band, Mollweide for higher latitudes
  - Interrupted (cut at oceans to reduce land distortion)
  - Equal-area
  - Best use: global thematic data on land masses
  - Drawback: can't navigate across the interruptions

  ALBERS EQUAL-AREA CONIC:
  - Two standard parallels where scale is exact
  - Equal-area between standard parallels
  - Excellent for mid-latitude countries (US 48 states, Russia)
  - The USGS standard for US national maps
  - Best use: regional/national maps at mid-latitudes

  GALL-PETERS:
  - Cylindrical equal-area
  - Vertical stretch at high latitudes (Africa looks elongated)
  - Equal-area globally
  - Best use: showing area relationships across all latitudes
  - Aesthetic problems: shapes distorted at all latitudes

══════════════════════════════════════════════════════════════════════
```

---

## Conformal Projections

```
CONFORMAL PROJECTION COMPARISON
══════════════════════════════════════════════════════════════════════

  NOTE: EPSG codes are standardized integer identifiers for coordinate reference systems,
  maintained by the International Association of Oil & Gas Producers (formerly EPSG).
  Lookup: epsg.io. Key codes: EPSG:4326 = WGS84 geographic (lat/lon, degrees);
  EPSG:3857 = Web Mercator (x/y, meters, spherical). Use in PostGIS/QGIS/PROJ.

  MERCATOR:
  - Cylindrical conformal
  - Straight rhumb lines
  - Used for: nautical charts, weather maps (winds are angles)
  - Web Mercator (EPSG:3857): used by Google Maps, OpenStreetMap
    tiles (slightly different math — treats Earth as sphere not
    ellipsoid — introduces ~0.33% error; fine for web mapping)

  TRANSVERSE MERCATOR:
  - Cylindrical rotated 90° — tangent line is a meridian
  - Very accurate within ~3° of central meridian
  - Used for: UTM (Universal Transverse Mercator) grid system
    which divides Earth into 60 zones, each 6° wide
  - Each UTM zone: essentially its own Transverse Mercator
  - Also: US State Plane Coordinate System (large-scale surveys)

  LAMBERT CONFORMAL CONIC:
  - Two standard parallels; conformal
  - Good for east-west extent in mid-latitudes
  - Used for: aeronautical charts (FAA sectionals), US state maps
  - Scale error under 1% within ~2° of standard parallels

  STEREOGRAPHIC:
  - Azimuthal conformal — circles on sphere = circles on map
  - Used for: polar regions (UPS — Universal Polar Stereographic
    for latitudes above 84°N and below 80°S)
  - Also: whole-hemisphere views in scientific publications

══════════════════════════════════════════════════════════════════════
```

### UTM — The Practical Grid System

UTM deserves detailed treatment because it is the practical coordinate system used for most large-scale surveying, military mapping, and GIS work.

```
UNIVERSAL TRANSVERSE MERCATOR (UTM)
══════════════════════════════════════════════════════════════════════

  Coverage: 80°S to 84°N (poles handled by UPS)

  Structure:
  - 60 zones, each 6° of longitude wide
  - Zone 1: 180°W to 174°W
  - Zone 60: 174°E to 180°E
  - Each zone: 20 latitude bands, C through X (8° each)
    (I and O omitted — confusion with 1 and 0)

  Within each zone:
  - Transverse Mercator centered on zone's central meridian
  - False Easting: 500,000m (to avoid negative x values)
  - False Northing: 0m (northern hemisphere) or 10,000,000m (S)
  - Scale factor: 0.9996 at central meridian
    (slightly reduces scale to minimize max error across zone)

  Coordinate format: Zone + Easting + Northing
  Example: "18T 585736 4511183"
  = Zone 18T (New York City area)
  = 585736 meters east of zone's false origin
  = 4511183 meters north of equator

  Accuracy:
  - Within one zone: <1mm error for most surveying purposes
  - Across zone boundaries: coordinates are discontinuous
    (you CANNOT do geometry across UTM zone boundaries)
  - For cross-zone work: use geographic (lat/lon) coordinates

══════════════════════════════════════════════════════════════════════
```

---

## Azimuthal Projections

```
AZIMUTHAL PROJECTIONS
══════════════════════════════════════════════════════════════════════

  All azimuthal projections share:
  - Centered on a single point (can be any point on Earth)
  - Circular symmetry around that center
  - Azimuths (bearings) from center are correct

  GNOMONIC:
  - Projection from Earth's center onto tangent plane
  - Property: ALL great circles appear as straight lines
  - Use: plotting great circle routes (shortest path navigation)
  - Problem: extreme distortion away from center
    (hemisphere cannot be shown — distortion → ∞)

  STEREOGRAPHIC:
  - Projection from antipode of tangent point
  - Property: conformal (circles on sphere = circles on map)
  - Use: polar maps, hemispheric scientific maps
  - Can show full hemisphere (with some distortion at edges)

  AZIMUTHAL EQUIDISTANT:
  - Not a "real" geometric projection — constructed to be equidist
  - Property: distances from center point are correct
  - Use: maps centered on a city showing all destinations by dist;
    UN emblem uses this centered on North Pole
  - Cannot show opposite pole

  LAMBERT AZIMUTHAL EQUAL-AREA:
  - Property: areas correct
  - Use: continental maps, thematic maps of hemispheres
  - Used by EU for Europe reference maps

══════════════════════════════════════════════════════════════════════
```

The gnomonic projection deserves special emphasis for navigation: it is the only projection on which any great circle — the shortest path between two points on a sphere — plots as a straight line. Before digital navigation, ocean navigators would transfer a route from a gnomonic chart (where they drew the great circle route as a straight line) onto a Mercator chart (where they identified a series of rhumb line segments approximating the great circle). Two chart types, each doing what the other cannot.

---

## Compromise Projections

```
COMPROMISE PROJECTIONS — WHEN NEITHER PROPERTY IS PARAMOUNT
══════════════════════════════════════════════════════════════════════

  ROBINSON (1963, Arthur Robinson):
  - Pseudocylindrical; neither conformal nor equal-area
  - Constructed empirically to "look right" (tabulated, not formula)
  - National Geographic: 1988–1998
  - Poles shown as lines (not points)
  - Moderate distortion everywhere — no severe distortion anywhere

  WINKEL TRIPEL (1921, Oswald Winkel):
  - Average of equirectangular and Aitoff projections
  - "Tripel" = three: minimizes area, distance, and direction errors
  - National Geographic: 1998–present
  - Lower average distortion than Robinson by modern metrics
  - Used by many atlases as the current "best compromise"

  NATURAL EARTH (2007, Tom Patterson and Bernhard Jenny):
  - Pseudocylindrical; constructed numerically
  - Designed for natural Earth background maps and terrain
  - Even flatter poles than Robinson
  - Software-optimized design (coefficients from optimization)

  SELECTION GUIDE:
  ┌──────────────────────────────────────────────────────────────┐
  │  Purpose                → Recommended projection             │
  │  Navigation (sea)       → Mercator                           │
  │  Navigation (air, GC)  → Lambert Conformal Conic / Gnomonic  │
  │  Thematic (area)        → Albers / Mollweide / Gall-Peters   │
  │  General world map      → Winkel Tripel / Robinson           │
  │  Regional mid-lat map   → Lambert CC or Albers               │
  │  Polar region           → Stereographic / Azimuthal EA       │
  │  US national map (USGS) → Albers Equal-Area Conic            │
  │  Web slippy map         → Web Mercator (EPSG:3857)           │
  │  Survey / GPS coords    → UTM (zone-specific TM)             │
  └──────────────────────────────────────────────────────────────┘

══════════════════════════════════════════════════════════════════════
```

---

## Web Mercator — The Modern Default

Web Mercator (EPSG:3857, also called "Pseudo-Mercator") is worth understanding separately because it is the projection used by Google Maps, OpenStreetMap, Bing Maps, and virtually every web mapping application.

```
WEB MERCATOR — WHAT IT IS AND WHY IT'S USED
══════════════════════════════════════════════════════════════════════

  Mathematical difference from true Mercator:
  ┌────────────────────────────────────────────────────────────┐
  │  True Mercator: projects onto ellipsoid (WGS84)            │
  │  Web Mercator: projects as if Earth were a sphere          │
  │  (using spherical formula with WGS84 equatorial radius)    │
  │                                                            │
  │  Error: up to ~0.33% in scale near the equator             │
  │  This is invisible at web map zoom levels                  │
  └────────────────────────────────────────────────────────────┘

  Why it was adopted:
  ├── Tiles are square: at each zoom level, world fits in 2ⁿ × 2ⁿ tiles
  │   (zoom 0 = 1 tile = whole world; zoom 1 = 4 tiles; etc.)
  ├── Efficient: tiles cache well (static PNG files)
  ├── Simple: x/y calculation straightforward
  └── Google chose it for Google Maps (2005); industry followed

  The tile scheme:
  ┌────────────────────────────────────────────────────────────┐
  │  Zoom 0: 1 tile  (256×256px = whole world)                 │
  │  Zoom 1: 4 tiles (2×2 grid)                                │
  │  Zoom n: 4ⁿ tiles (2ⁿ × 2ⁿ grid)                           │
  │  Zoom 18: 68 billion tiles (street level)                  │
  │                                                            │
  │  Tile URL format: /tiles/{z}/{x}/{y}.png                   │
  │  z = zoom level, x = column, y = row                       │
  │                                                            │
  │  This is a function: f(z,x,y) → PNG                        │
  │  Precomputed and cached; server complexity is generating   │
  │  and storing tiles, not computation per request            │
  └────────────────────────────────────────────────────────────┘

  Limitation: Distorts area at high latitudes (same as Mercator).
  At zoom 0, Greenland appears nearly as large as Africa.
  Most users don't notice because they zoom in for their use case.

══════════════════════════════════════════════════════════════════════
```

---

## Bridge to Mathematics

Map projections are a concrete application of topics from differential geometry and complex analysis:

- **Conformal maps** in 2D are exactly the holomorphic functions with nonzero derivative (Riemann mapping theorem context). The Mercator projection's formula `y = ln|tan(π/4 + φ/2)|` can be derived from complex analysis.
- **The Tissot indicatrix** is the image of the unit circle under the projection's derivative map (the Jacobian) — a direct application of the linear approximation to a smooth map.
- **Equal-area condition**: the Jacobian determinant equals 1 (or a constant). This is exactly the condition for a volume-preserving map in measure theory.
- **Gaussian curvature** is the intrinsic quantity that makes the sphere non-isometric to the plane. It is computed from the metric tensor: `K = R₁₂₁₂ / det(g)` where R is the Riemann curvature tensor.

---

## Common Confusion Points

**"Mercator is bad because it distorts Africa."** Mercator is bad for general audience world maps because it distorts area. It is excellent for navigation because it preserves local angles. Evaluating a tool outside its design purpose is a category error.

**"The Peters projection is more accurate."** Neither Gall-Peters nor Mercator is "more accurate" — they preserve different properties. Gall-Peters distorts shapes severely (Africa looks like a tall oval). The question is: accurate *for what purpose?*

**"You should use Mercator for your interactive web map."** Web Mercator (EPSG:3857) is appropriate for street-level tile rendering. For any map that compares areas, choropleth, or spatial statistics, it introduces systematic errors. Use a local projected CRS or equal-area projection for analytical work.

**"UTM coordinates work anywhere."** UTM coordinates are only meaningful within a single zone. Computing distances or doing geometry across zone boundaries using UTM coordinates is wrong. Convert to geodetic (lat/lon) first, or use a single global CRS like ECEF.

---

## Decision Cheat Sheet

| Use case | Projection | Why |
|----------|-----------|-----|
| Nautical chart | Mercator | Rhumb lines as straight lines |
| Aeronautical sectional | Lambert Conformal Conic | Shape-accurate for airways |
| US national thematic map | Albers Equal-Area Conic | Area-accurate, good shape |
| World population density | Gall-Peters or Mollweide | Equal-area for fair comparison |
| General world map | Winkel Tripel | Best overall compromise |
| Web slippy map tiles | Web Mercator (EPSG:3857) | Industry standard, efficient tiling |
| GPS/survey coordinates | UTM or geographic (EPSG:4326) | Metric, local accuracy |
| Ocean route planning | Gnomonic + Mercator | GC on gnomonic, steer by Mercator |
| Polar navigation | Polar Stereographic | Conformal, covers poles |
| Teaching area distortion | Gall-Peters vs Mercator | Direct visual comparison |
