# Watershed Analysis — Watershed Delineation, DEM Analysis, Strahler Stream Order, Drainage Density

## The Big Picture

```
+===========================================================================+
|                  WATERSHED ANALYSIS AS GRAPH THEORY                        |
|         A drainage network is a directed acyclic graph on a DEM           |
+===========================================================================+
|                                                                           |
|  DIGITAL ELEVATION MODEL (DEM) — raster grid of elevation values          |
|      │                                                                    |
|      ▼ Flow direction algorithm (D8, D-inf, MFD)                         |
|  FLOW DIRECTION GRID — each cell points to lowest neighbor                |
|      │                                                                    |
|      ▼ Flow accumulation (upstream cell count)                           |
|  FLOW ACCUMULATION GRID — each cell: # of upstream cells                 |
|      │                                                                    |
|      ├──► STREAM NETWORK — cells with accumulation > threshold            |
|      │         Graph topology: tributary confluence = node merge          |
|      │                                                                    |
|      └──► WATERSHED BOUNDARY — all cells draining to a given outlet      |
|               = divide (ridgeline) connecting highest surrounding cells   |
|               = catchment area contributing to outlet                    |
|                                                                           |
+===========================================================================+
```

---

## Digital Elevation Models (DEMs)

```
DEM DATA SOURCES:

  SRTM (Shuttle Radar Topography Mission, 2000):
    1 arc-second (~30 m) resolution globally
    Radar interferometry (C-band + X-band)
    Vertical accuracy: ~5–10 m RMSE (varies by terrain)
    Gap-filled in some problematic areas
    Free globally via USGS EarthExplorer

  ALOS PALSAR (Japan):
    12.5 m resolution globally
    Good forest penetration (L-band radar sees through canopy)
    Best available global DEM for forested terrain

  ASTER GDEM (Terra satellite):
    30 m resolution, photogrammetric stereo method
    Noisier than SRTM in flat terrain; better over high-relief areas

  USGS 3DEP (US only):
    1 m (urban, high-priority), 3 m, 10 m resolution
    LiDAR-derived in many areas — most accurate available
    BareSurface vs. Surface (includes vegetation) — critical distinction for hydrology

  LIDAR DEMs:
    Airborne LiDAR: 0.5–1 m resolution, ±5–15 cm vertical accuracy
    Ground point filtering removes buildings and vegetation → bare-earth DEM
    Required for accurate floodplain mapping

DEM PREPROCESSING:
  Hydrological conditioning: essential before flow routing
    Pit filling: sink cells (depressions) filled to ensure continuous drainage
    (Natural depressions in landscape: wetlands, lakes → problem for flow routing)
    Burning streams: carve stream channel into DEM where known location
    (Prevents "leaking" of streams across ridges due to DEM error)
```

---

## Flow Direction Algorithms

```
D8 ALGORITHM (most common):
  Each cell drains to ONE of 8 neighbors (N, NE, E, SE, S, SW, W, NW)
  Choice: steepest descent neighbor
  Slope to each neighbor: Δz / distance (diagonal = √2 × cell size)

  LIMITATION: all flow concentrated to single path
  → artificial flow concentration, poor lateral dispersion
  → problematic for divergent hillslopes (ridges)

D-INFINITY (Tarboton, 1997):
  Flow direction = continuous angle (0–2π)
  Flow split between two adjacent cells based on angle
  Better represents divergent hillslope flow
  Computational cost: higher

MFD (Multiple Flow Direction):
  Flow distributed to all downslope neighbors, weighted by slope
  Best for representing broad wetland flow and diffuse hillslope drainage
  Poor for defined channel networks (too diffuse)

PRACTICAL CHOICE:
  D8: stream networks, watershed delineation (sharp drainage divides) ✓
  D-infinity: hillslope flow paths, shallow groundwater
  MFD: broad floodplain inundation, wetland flow
```

---

## Flow Accumulation and Stream Network Extraction

```
FLOW ACCUMULATION ALGORITHM:
  For each cell: count all cells upstream (including self) = 1 + sum of upstream cells
  Terminal cells: value = 1 (no one drains to them)
  Outlet cell: value = total cells in watershed

  This is a topological sort on the flow-direction DAG (directed acyclic graph)
  Computationally: O(n log n) or better with spatial partitioning

STREAM NETWORK EXTRACTION:
  Threshold T: cells with accumulation > T are "stream cells"
  T too high → few long streams (misses small tributaries)
  T too low → every cell is a stream (unrealistic)

  CALIBRATION:
    Match extracted channel heads to field verification or high-resolution imagery
    Often: T equivalent to 0.1–1 km² contributing area for humid region streams
    Arid: larger threshold (channels only form with larger contributing area)

  STREAM NETWORK STATISTICS:
    Channel density = total stream length / watershed area (km/km²)
    Stream frequency = number of streams / watershed area (streams/km²)
    Bifurcation ratio (Rb): count(order-n streams) / count(order-(n+1) streams)
      Typical Rb = 3–5
```

---

## Strahler Stream Order

```
STRAHLER ORDERING SYSTEM (1952):
  Fingertip tributaries (headwaters): order 1
  Two order-1 streams join → order 2
  Two order-2 streams join → order 3
  Two streams of SAME order join → increment by 1
  Lower order meets higher order → higher order continues (no change)

  EXAMPLE:
       1──┐
       1──┘ → 2──┐
       1──┐      │ → 3──┐
       1──┘ → 2──┘      │ → 4
       1──┐              │
       1──┘ → 2──┐      │
              2──┘ → 3──┘

  The MAIN STEM is the highest-order stream through the basin.
  Mississippi River: ~9th order (drainage basin: 3.2 million km²)
  Typical small catchment stream: 1st–3rd order
  Amazon: ~12th order

HORTON'S LAWS (derived from Strahler order):
  Law of stream numbers:  N(w) = R_b^(Ω-w)
    N(w) = number of streams of order w
    R_b = bifurcation ratio (~3–5)
    Ω = basin order (highest order)

  Law of stream lengths:  L(w) = L_1 × R_L^(w-1)
    R_L = length ratio (~1.5–3.5)

  Law of drainage areas:  A(w) = A_1 × R_A^(w-1)
    R_A = area ratio (~3–6)

  These self-similar scaling laws = fractal structure of river networks
  The drainage network is a self-similar branching fractal
  (same geometric structure at multiple scales → Hack's law, Tokunaga trees)

TOPOLOGICAL NETWORK PROPERTIES:
  Bifurcation ratio R_b controls flood peak timing:
    High R_b (less branching) → more synchronized tributary peaks → flashier floods
    Low R_b → more staggered arrivals → attenuated peak
```

---

## Watershed Delineation

```
DELINEATION ALGORITHM:
  Given outlet point (pour point) on DEM:
  1. Start at outlet cell
  2. Identify all cells that drain to outlet (trace upstream through flow-direction grid)
  3. Boundary = all cells at the edge of contributing area

  IMPLEMENTATION: simple BFS/DFS on flow-direction grid
    Similar to connected components algorithm on a graph
    Efficient O(n) once flow-direction grid is computed

TOPOGRAPHIC INDICES:

  TOPOGRAPHIC WETNESS INDEX (TWI):
    TWI = ln(a / tan(β))
    a = specific upslope contributing area (m²/m) = flow accumulation × cell width
    β = local slope angle

    High TWI → large upslope area + gentle slope → saturated, wetland areas
    Low TWI → small upslope area + steep → well-drained, upland areas
    Used to: identify soil moisture patterns, probable saturation zones,
             prime locations for wetlands, saturated excess runoff generation

  STREAM POWER INDEX (SPI):
    SPI = a × tan(β)
    Proxy for erosive power of water at a point
    High SPI → high-energy gully and channel formation potential

  SLOPE POSITION CLASSIFICATION:
    Combine TWI, curvature, elevation within catchment
    → ridgetop, shoulder, backslope, footslope, toeslope, channel
    Widely used in soil mapping, terrain analysis

WATERSHED BOUNDARY PRECISION:
  DEM resolution limits accuracy:
    30 m DEM → watershed boundary uncertainty ±30 m
    1 m LiDAR → boundary uncertainty ±1 m
  Flat terrain (< 0.1% slope): major errors in flow routing
    (Small elevation errors redirect drainage over large areas)
  Coastal and tidal areas: dynamic boundary that changes with tide
```

---

## Drainage Network Patterns

```
PLAN-VIEW DRAINAGE PATTERNS (visible on maps, reflect underlying geology):

  DENDRITIC:
    Tree-like, random branching
    Uniform substrate (isotropic geology)
    Most common pattern in nature

  PARALLEL:
    Tributaries nearly parallel
    Uniform regional slope or parallel structural fabric (dikes, faults)

  TRELLIS:
    Main streams perpendicular to tributaries
    Folded sedimentary rock (ridges and valleys)
    Example: Valley and Ridge province, Appalachians

  RECTANGULAR:
    Right-angle bends in streams
    Jointed or faulted bedrock (fractures at 90°)

  RADIAL:
    Streams radiate outward from a central high point
    Volcanic cone, dome uplift
    Example: Mt. Rainier, Black Hills

  ANNULAR:
    Streams follow concentric arcs around a dome
    Eroded structural dome with alternating hard/soft rock rings

  DERANGED:
    No clear pattern, many lakes, poorly integrated
    Recently glaciated terrain (Laurentian Shield, Scandinavia)
    Glaciers destroy pre-existing drainage → new drainage slowly developing

DRAINAGE PATTERN → QUICK GEOLOGICAL DIAGNOSIS:
  Trellis → folded Appalachian-type geology
  Radial → volcanic or dome structure
  Deranged → glaciated terrain
  Dendritic → homogeneous geology, mature drainage
```

---

## Hydrograph Response and Catchment Properties

```
RUNOFF RESPONSE CHARACTERISTICS:

  FLASHY CATCHMENT:
    Small area, steep slopes, impervious cover (urban), sparse vegetation
    Short Tc, high peak flows, rapid recession
    High Rb (bifurcation ratio)

  SLOW RESPONSE CATCHMENT:
    Large area, gentle slopes, forested, permeable soils, many lakes/wetlands
    Long Tc, low peak flows relative to rainfall, slow recession
    Low Rb, high storage

TIME OF CONCENTRATION METHODS:
  Kirpich (1940): Tc = 0.0195 L^0.77 S^-0.385
    L = channel length (m), S = channel slope
    Simple, widely used for small catchments

  SCS Lag Method: Tc = Tlag / 0.6
    Tlag = CN-based lag time from SCS formulas

  Velocity-area method: Tc = Σ(L_i / V_i)
    Sum of travel times through different segments
    V from Manning equation for each segment

SPECIFIC DISCHARGE (UNIT AREA RUNOFF):
  q = Q / A (m³/s/km²)
  Allows comparison of runoff rates between different-sized catchments
  Flood frequency: "unit area" scale is standardized across basins
  For example: 100-yr specific discharge maps show regional pattern
    (eastern US: 1–5 m³/s/km², arid SW: 0.01–0.1 m³/s/km²)
```

---

## GIS and Computational Tools

```
STANDARD HYDROLOGICAL GIS WORKFLOW:

  DATA → DEM preparation → Pit filling → Flow direction → Flow accumulation
       → Stream network → Watershed delineation → Morphometric analysis

TOOLS:
  ArcGIS Hydrology toolbox (Arc Hydro): industry standard, expensive
  QGIS + SAGA GIS: open source, capable, free
  TauDEM (Terrain Analysis Using Digital Elevation Models):
    Utah State University, command-line, parallel processing
    Best for large DEMs (national-scale analysis)
  GRASS GIS r.watershed: classic, robust, open source
  Whitebox GAT: free academic tool, excellent teaching/research
  SWAT (Soil and Water Assessment Tool): full watershed simulation model
    Uses DEM + soil + land use + weather → continuous water balance simulation
    Widely used for NPS pollution, climate change impact studies

LARGE-SCALE PRODUCTS:
  HydroBASINS: Pfafstetter watershed coding system, global drainage basins
    Pfafstetter code: 0–9 at each level, encodes topology
    10-level hierarchy → each drainage basin has unique 10-digit code
  HydroSHEDS: global hydrological data derived from SRTM
  NHDPlus (US National Hydrography Dataset): national stream network + attributes
```

---

<!-- @editor[bridge/P2]: No dedicated bridge section — the graph-theory framing (DAG, topological sort, BFS/DFS, connected components, fractal branching) is outstanding but scattered through multiple sections; a consolidated "CS Bridges" callout would make these jump out for the learner -->

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| What algorithm delineates watersheds from a DEM? | D8 flow direction → flow accumulation → upslope trace from outlet |
| What is Strahler order? | Hierarchical stream ordering; two same-order streams join → increment; headwaters = 1 |
| What does TWI indicate? | Topographic Wetness Index: high = likely saturated/wetland; low = well-drained upland |
| What is bifurcation ratio? | Count(order n) / Count(order n+1); typically 3–5; controls flood peak timing |
| What DEM resolution is needed for accurate watershed delineation? | Depends on catchment size; LiDAR (1 m) for urban/floodplain; 10–30 m for regional |
| What is a deranged drainage pattern? | No organized pattern; many lakes; recently glaciated terrain |
| Why burn streams into a DEM? | Force hydrological flow direction to match known channel locations; prevent routing errors |
| What controls Tc? | Channel slope, channel length, roughness; smaller/steeper catchment → shorter Tc |

---

## Common Confusion Points

**Watershed = catchment = drainage basin**: These terms are used interchangeably in hydrology. A watershed is the upslope area contributing water to a specific outlet point. The watershed divide is the ridgeline separating two watersheds. Subwatershed = subbasin = tributary catchment.

**Flow accumulation ≠ discharge**: The flow accumulation grid counts upstream CELLS, not water volume. To convert to contributing area: multiply by (cell size)². To estimate peak discharge, you still need a rainfall-runoff model. Flow accumulation is purely a topographic property.

**Pits are usually errors, but sometimes real**: "Pits" in a DEM (cells lower than all neighbors with no outlet) are usually artifacts of DEM error. Most flow routing tools "fill" them automatically. But some pits are real — closed basins (playas, prairie potholes, Carolina Bays) where water truly doesn't drain to a stream. In these cases, pit-filling creates incorrect hydrology.

**Strahler order vs. Shreve order**: Strahler (binary): only joins of same-order increment the order. Shreve (additive): Shreve order = total number of first-order streams contributing. Both are valid; Strahler is more common for geomorphology; Shreve is additive (conserves count). Also: Hack's main stem vs. Strahler main stem give different stream lengths.

**Watershed boundaries are 3D surfaces**: The watershed divide is the line on a DEM where flow is ambiguous — goes to either side. In the real landscape, the topographic divide approximately equals the subsurface groundwater divide, but they can differ significantly where geology creates preferential flow paths (karst, highly permeable basalt) that cross apparent topographic divides.
