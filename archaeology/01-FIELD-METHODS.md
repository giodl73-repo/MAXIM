# Archaeological Field Methods

## The Big Picture

```
+------------------------------------------------------------------+
|              FIELD ARCHAEOLOGY: THE DATA COLLECTION PIPELINE     |
|                                                                  |
|  DISCOVERY          EVALUATION         EXCAVATION                |
|  Find sites         Assess potential   Recover data              |
|                                                                  |
|  Desk-based         Fieldwalking       Open-area excavation      |
|  assessment         Trial trenches     Quadrant method           |
|  Remote sensing     Geophysics         Watching brief            |
|  LiDAR/aerial       Test pits          Developer-funded digging  |
|                                                                  |
|  POST-EXCAVATION    REPORTING          ARCHIVE                   |
|  Finds analysis     Grey literature    Deposition to museum      |
|  Dating             Published report   Digital archive           |
|  Environmental      Online database    Repatriation (if relevant)|
+------------------------------------------------------------------+

KEY PRINCIPLE: Excavation is irreversible destruction.
Every layer removed is gone forever. Recording IS the excavation.
```

---

## Survey Methods

### Desk-Based Assessment

Before any fieldwork: compile all prior knowledge.

- Historic maps (Ordnance Survey series, cadastral maps)
- Aerial photograph archives (USGS NAPP, Cambridge AP collection)
- National monument records (HER in UK; NRHP in US; state databases)
- Geological and soil surveys
- Published excavation reports
- LiDAR digital terrain models (now freely available in many regions)

**The desk-based model is exactly like technical due diligence before a project** — you should know what's already known before spending field resources.

### Pedestrian Survey (Fieldwalking)

```
FIELDWALKING PROCEDURE:
  Transects: field divided into grid; walkers spaced 5–15 m apart
  Each transect walked systematically → all artifacts picked up
  GPS coordinates recorded for each find
  Surface finds plotted → density maps → identify likely site zones

WHAT IT DETECTS:
  Plowed sites: erosion brings subsurface finds to surface
  Works well in Mediterranean (large sherds visible in plowed fields)
  Less effective in woodland, pasture, areas with topsoil cover

SAMPLING STRATEGIES:
  Total collection: everything picked up in survey zone
  Selective: only significant or diagnostic finds recorded
  Statistical: randomly sampled transects from larger universe
```

### Geophysical Survey

Non-invasive methods that sense below-ground features before digging:

```
MAGNETOMETRY (most common):
  Measures Earth's magnetic field variations
  Detects: hearths (heated → remanent magnetism), pits (magnetic fill),
    iron objects, fired features, some walls
  Speed: ~1 ha/day; resolution ~0.25 m
  FLUXGATE GRADIOMETER: portable; measures field gradient
  Output: grayscale anomaly plot → excavator targets anomalies

GROUND-PENETRATING RADAR (GPR):
  Pulses of radar signal → reflects off interfaces between materials
  Detects: walls, floors, voids, pits, ditches, graves
  3D volume: multiple transects → depth slices
  Best in: dry sandy soil; poor in: wet clay (signal absorbed)
  Speed: slower than mag; better 3D resolution for structures

RESISTIVITY / ERT:
  Current injected → resistivity of soil measured
  High resistivity: walls (stone/brick), dry features
  Low resistivity: pits, ditches (moist fills)

LIDAR (remote sensing):
  Airborne laser scanning; penetrates forest canopy
  Returns: digital terrain model at 1-5 cm resolution
  DISCOVERIES: Caracol (Belize, 2010): 200 km² of Maya settlement
  Angkor Wat environs: urban infrastructure; rethought settlement scale
  Stonehenge environs: hundreds of unknown features
  The Maya lowlands and Amazon basin rewritten by LiDAR

AERIAL PHOTOGRAPHY:
  Crop marks: buried features cause differential growth above
    → Ditches = lusher crop; walls = stressed crop
  Shadow marks: oblique light shows subtle earthworks
  Soil marks: plowed-out monuments visible as soil color
  Best for: large features, floodplains, agricultural landscapes
```

---

## Excavation Techniques

### Open-Area Excavation

```
OPEN-AREA (HORIZONTAL) EXCAVATION:
  Large area cleared simultaneously to expose entire floor plan
  Reveals: spatial relationships, room plans, activity areas
  Used for: settlements, houses, public buildings, complex sites

  +--------------+
  |              |  Sondage (test pit): earlier, to check stratigraphy
  |   Excavation |  Baulks (sections): left at intervals for section recording
  |     area     |  Units: 5×5 m or 10×10 m grid squares
  |   /     \    |
  |  /       \   |
  | / baulks  \  |  Sections kept until the relevant context understood
  +--------------+

ADVANTAGE: understand spatial relationships within a period
DISADVANTAGE: deeper earlier levels hard to expose simultaneously
```

### Quadrant Method

Used for burial mounds, ring ditches, circular monuments:

```
QUADRANT METHOD:
       N
       |
  NW   |   NE
       |
  -----+-----  Mound divided into quadrants
       |        Two opposite quadrants excavated first
  SW   |   SE   → Sections on all 4 sides
       |
       S

  Reveals: mound construction sequence
  Primary burial (original) vs. secondary burials (later insertions)
  Core mound sequence vs. later enlargements
  Profile: ditch, bank, inner mound, mound cap
```

### Single Context Recording (SCR)

Developed at Winchester (1960s), standardized in the 1970s. Now universal in professional UK archaeology; widely used globally.

```
SINGLE CONTEXT RECORDING SYSTEM
+------------------------------------------------------------------+
|  PRINCIPLE: each stratigraphic unit = one record sheet           |
|                                                                  |
|  Each "context" gets:                                            |
|  Context number (unique sequential, e.g., F.001, F.002, ...)   |
|  Type: deposit (layer/fill), cut, structure, interface           |
|  Description: colour, texture, inclusions of deposit           |
|  Dimensions: extent, depth, dimensions                         |
|  Relationships: above/below/cuts/is cut by other contexts      |
|  Interpretation: function/period (pencilled in; changed later) |
|  Finds: list of associated finds numbers                       |
|  Samples: environmental/scientific sample numbers              |
|  Plans and sections at specific scales                         |
|                                                                  |
|  CONTEXT NUMBER = the immutable audit key                        |
|  An artifact found in F.047 can always be traced to F.047      |
|  Every bag, every sample, every photo references context number  |
|  → Like a database foreign key linking all records to location |
+------------------------------------------------------------------+
```

### Finds Recording

```
ARTIFACT NUMBERING SYSTEM:
  Site code: e.g., BRON23 (Bronzeham 2023)
  Context: F.087
  Find number: 045 (sequential within context)
  → Full number: BRON23/F.087/045

Every artifact bagged individually (or by type per context)
Tag in bag + number on bag
Day register of finds: who found, where, when
Photography: in situ photograph before lifting (significant finds)
GPS: important finds GPS-located

SPECIAL FINDS:
  Metal detected: GPS coordinates + depth; stored separately
  Human remains: separate protocols; bioarchaeologist required
  Fragile: immediate conservation assessment
  Organic: wet sieve, cold store, conservation immediately

BULK FINDS:
  Pottery sherds, animal bone → bagged by context
  Separated by material type (pottery, bone, tile, CBM, glass, metal)
  Weight recorded; retained for analysis

ENVIRONMENTAL SAMPLES:
  Bulk soil sample (30–40 liters): flotation for seeds, charcoal, bone
  Monolith: undisturbed column for micromorphology
  Pollen column: from appropriate waterlogged/peat contexts
  Radiocarbon samples: short-lived plant material; charred grain preferred
```

---

## The Harris Matrix and Stratigraphic Analysis

```
HARRIS MATRIX: DAG OF ALL CONTEXTS
+------------------------------------------------------------------+
|  Nodes = context numbers                                         |
|  Edges = stratigraphic relationship (older → younger)          |
|                                                                  |
|  Four valid relationships:                                       |
|  A is above B (A younger; superposition)                       |
|  A is equal to B (correlation; same event)                    |
|  A cuts B (A younger; interface relationship)                  |
|  A is filled by B (A is a cut; B is the fill of A)            |
|                                                                  |
|  MATRIX CONSTRUCTION:                                          |
|  Start with known relationships from section drawings          |
|  Each context block placed above those it overlies            |
|  Correlated contexts at same level                            |
|  Result: topological sequence from oldest (bottom) to         |
|    youngest (top) — the relative chronology                   |
|                                                                  |
|  PHASING: groups of contexts = phases                          |
|  Phase 1 (earliest): all contexts below certain relationships  |
|  Phase 2: next group                                           |
|  → Simplifies matrix to site narrative                        |
+------------------------------------------------------------------+

EXAMPLE MATRIX READING:
  [001] ← Topsoil (youngest by definition)
    |
  [010] ← Medieval plough soil
    |
  [020] ← Construction trench for medieval wall [W.001]
    |
  [030] ← Saxon occupation deposit (oldest; above natural)
    |
  [999] ← Natural / Sterile subsoil

  Wall [W.001]: contemporary with [020] (its construction cut)
  Relative sequence: 999 → 030 → 020/W.001 → 010 → 001
```

---

## GIS in Field Archaeology

```
ARCHAEOLOGICAL GIS LAYERS
+------------------------------------------------------------------+
|  BASE LAYERS:                                                    |
|  → Digital terrain model (LiDAR or surveyed)                  |
|  → Historic maps, cadastral boundaries                         |
|  → Satellite/aerial imagery                                    |
|  → Geological/soil maps                                        |
|                                                                  |
|  SURVEY LAYERS:                                                  |
|  → Fieldwalking transects + artifact density                  |
|  → Geophysics anomalies                                       |
|  → Previous site locations                                    |
|                                                                  |
|  EXCAVATION LAYERS:                                            |
|  → Trench outlines + context polygons                        |
|  → Feature centroids                                          |
|  → Finds + sample locations (GPS points)                     |
|  → Section line positions                                     |
|  → Photographic extent coverage                              |
|                                                                  |
|  ANALYSIS LAYERS:                                              |
|  → Site catchment (resource territories)                     |
|  → Viewshed (what can be seen from monument)                 |
|  → Least-cost paths (route modeling)                         |
|  → Hotspot analysis (artifact density clusters)              |
+------------------------------------------------------------------+
```

**Total Station and GNSS**: Modern excavations use total station (precise to ±2 mm) for feature and section survey, supplemented by RTK GNSS (GPS, precise to ~20 mm). All contexts, finds, and sections are surveyed in 3D coordinates. The site plan assembles from these measurements.

**Photogrammetry and 3D recording**: Drone or DSLR images → Structure from Motion (SfM) software → textured 3D mesh. Used for: excavation surfaces before removal, section faces, entire sites. Resolution: sub-centimeter from close-range photography. This is the same photogrammetry used in construction and engineering surveys.

---

## Section Drawing and Recording

```
SECTION DRAWING: cross-section through deposit sequence
  Vertical slice shows: deposit sequence, relative depths, interfaces

DRAWING CONVENTIONS:
  Scale: 1:20 or 1:10 for detail; 1:50 for whole trench
  Datum: horizontal line at known height (ordnance datum or site datum)
  Scale bar: always included
  North arrow (for plan drawings)
  Colour coding: deposit types hatched/shaded by convention
  Context numbers: each layer labelled with its number

  Surviving section after excavation ↓
  +------------------------------------------+
  |  F.001 Topsoil (grey brown silty loam)   |
  |    ↕                                     |
  |  F.020 Gravel metalling (road surface)   |
  |    ↕                                     |
  |  F.030 Dump layer (mixed finds)          |
  |    ↕                                     |
  |  F.040 Pit fill (occupation deposit)     |
  |    ↕   (cut = F.041, cut into F.050)     |
  |  F.050 Clay natural subsoil              |
  +------------------------------------------+

MICROMORPHOLOGY: undisturbed soil block (monolith) → thin section
→ Microscopic examination of deposit formation processes
→ Identifies: hearth ashes, dung layers, phytoliths, burnt bone
→ Tells you formation processes that are invisible macroscopically
```

---

## Watching Briefs and Developer-Funded Archaeology

In most countries with planning law, commercial developers must fund archaeological evaluation and excavation before construction if significant archaeology is anticipated.

```
UK MODEL (PPG16/NPPF):
  Developer funds desk-based assessment
  → Significance established
  → Mitigation strategy: preservation in situ OR excavation
  → If excavation required: developer funds excavation + post-ex + report
  → Archaeological contractor hired; local authority advises
  → Data deposited in county HER + museum archive

US MODEL (Section 106, NHPA):
  Federal undertakings require compliance with NHPA Section 106
  State Historic Preservation Officer (SHPO) consultation
  CRM (Cultural Resource Management) archaeology firms do the work
  → Very large industry; most US professional archaeologists work in CRM

PROBLEM: grey literature
  Commercial excavation reports often not published formally
  Hard to find, not peer-reviewed, variable quality
  → Being addressed by ADS (UK), tDAR, OpenContext databases
```

---

## Decision Cheat Sheet

| Use this method when... | Method | Notes |
|-------------------------|--------|-------|
| Fast site-wide coverage needed (1 ha/day) | Magnetometry | Best for pits, hearths, ditches; poor on non-magnetic stone walls |
| 3D structural resolution needed (walls, voids) | Ground-Penetrating Radar (GPR) | Slower; best in dry sand; poor in wet clay |
| Large-scale terrain mapping under forest canopy | LiDAR | Reveals sub-canopy earthworks; km² coverage; has rewritten Maya and Angkor archaeology |
| Assessing a site before any physical intervention | Desk-based assessment + geophysics | Always first; establishes what is already known |
| Exposing a full settlement plan of one period | Open-area excavation | Reveals spatial relationships; hard to get deep earlier levels simultaneously |
| Excavating a burial mound or circular monument | Quadrant method | Reveals construction sequence and primary vs. secondary burials |
| Tracking all finds back to exact location after excavation | Single Context Recording (SCR) | Context number = permanent foreign key; every find, photo, sample references it |
| Dating a timber structure to single-year precision | Dendrochronology | Requires surviving timber; matches tree-ring master sequences |
| Reconstructing deposit formation at microscopic scale | Micromorphology (soil thin sections) | Identifies hearth ashes, dung layers, phytoliths invisible to naked eye |
| Developer-funded work with planning constraints | Watching brief + evaluation trenches | Standard UK/EU model; developer pays; data archived in HER |

---

## Common Confusion Points

**Stratigraphy is physical layers, not the Harris Matrix**: Stratigraphy is the actual physical sequence of deposits. The Harris Matrix is a diagram that records and represents that physical sequence. The matrix is derived from the stratigraphy — it's the formal documentation of what you observed in the ground.

**Context numbers are not chronological**: F.001 is not necessarily older than F.002. Context numbers are assigned sequentially as contexts are identified during excavation. Chronological ordering comes from the Harris Matrix analysis.

**Removing vs. leaving baulks**: Baulks (earth sections between excavation squares) are left to record the vertical sequence. They're only removed once the sections are drawn and recorded. Removing baulks early destroys the section record.

**Single context recording vs. arbitrary levels**: Some traditions excavate in arbitrary 10 cm levels regardless of stratigraphy (common in Americanist archaeology). SCR excavates by natural stratigraphy (each cultural/geological layer removed as one unit). SCR gives much better stratigraphic control but requires trained field judgment to identify deposit boundaries.

**Post-excavation is not optional**: The excavation produces thousands of context sheets, bags of finds, environmental samples, photographs, drawings. Post-excavation — the analysis, dating, interpretation, and report writing — typically takes 2–3× as long as the fieldwork itself. The site exists primarily in the archive after excavation.
