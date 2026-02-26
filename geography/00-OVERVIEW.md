# Geography — Overview

## The Big Picture

Geography is the study of place, space, and the relationships between humans
and their physical environment. It straddles the natural sciences (climatology,
geomorphology, ecology) and social sciences (economic, political, cultural
geography). The field's lasting contribution is the recognition that WHERE
something occurs is often as explanatory as WHAT it is. Tobler's First Law:
"Everything is related to everything else, but near things are more related
than distant things."

```
+----------------------------------------------------------------------+
|                    GEOGRAPHY — LAYERED SYSTEM VIEW                   |
|                                                                      |
|  PHYSICAL SUBSTRATE (internal + external Earth processes)            |
|  ─────────────────────────────────────────────────────              |
|  Tectonics/Climate/Soils/Hydrology/Biogeography/Oceanography        |
|          │                    │                                      |
|          │  feedbacks:        │  feedbacks:                          |
|          │  deforestation     │  irrigation salinization             |
|          │  → erosion,        │  → soil loss; urbanization          |
|          │  CO₂ → warming     │  → flood risk                       |
|          ▼                    ▼                                      |
|  HUMAN GEOGRAPHY (overlaid on, and reshaping, the substrate)        |
|  ─────────────────────────────────────────────────────              |
|  Population + Urban │ Economic geography │ Political geography       |
|  Cultural geography │ Historical geography                           |
|                                                                      |
|  ANALYTICAL TOOLCHAIN                                               |
|  ──────────────────                                                  |
|  SCALE: local ──────────────────────────────────── global           |
|         (parcel) (neighborhood) (city) (region) (planet)            |
|  GIS/PostGIS: spatial queries on vector + raster layers             |
|  Remote sensing: image ML pipeline over multispectral data          |
|  Spatial stats: Moran's I, Kriging, hot-spot analysis               |
|  MAUP: results change as aggregation unit changes                   |
|  → connects physical measurements to human patterns                 |
+----------------------------------------------------------------------+
```

---

## Section 1: Core Analytical Concepts

```
  KEY CONCEPTS:
  ┌────────────────────────────────────────────────────────────────┐
  │ LOCATION                                                        │
  │ Absolute: lat/long, address, coordinate system                 │
  │ Relative: positional to other places (3 miles from X)          │
  │                                                                │
  │ PLACE: human meaning attached to locations                     │
  │ SPACE: the expanse between places; can be social (social       │
  │        distance), functional, perceived                        │
  │                                                                │
  │ SCALE: local vs regional vs national vs global                │
  │ Scale matters: processes visible at one scale may disappear   │
  │ at another; patterns aggregate differently                     │
  │                                                                │
  │ REGION: area with common characteristics (formal/functional/  │
  │ perceptual); a mental or analytical construct, not given       │
  └────────────────────────────────────────────────────────────────┘

  TOBLER'S FIRST LAW OF GEOGRAPHY (1970):
  "Everything is related to everything else,
  but near things are more related than distant things"
  → Spatial autocorrelation: adjacent areas tend to be similar
  → Foundation of kriging, spatial statistics, geostatistics

  MODIFIABLE AREAL UNIT PROBLEM (MAUP):
  Statistical results depend on HOW you aggregate spatial data
  Same underlying data → different conclusions depending on:
  • Scale: county vs state vs region level analysis
  • Aggregation: which units are combined
  Gerrymandering exploits MAUP deliberately — district boundaries
  are chosen to produce desired electoral outcomes by controlling
  which units are aggregated. The computational problem (optimize
  boundary placement to achieve a target outcome) is NP-hard in the
  general case; the legal constraint (compactness measures, equal
  population) bounds the feasible solution space. Algorithmic
  redistricting (shortest-splitline, Markov chain ensemble methods)
  attempts to remove human discretion from the aggregation choice.

  HUMAN-ENVIRONMENT INTERACTION:
  The reciprocal relationship between humans and environment:
  → Humans adapt to environment (pastoral nomadism in dry zones)
  → Humans modify environment (deforestation, irrigation, urbanization)
  → Environment constrains and channels human activity
```

---

## Section 2: Geographic Determinism — The Debate

```
  ENVIRONMENTAL DETERMINISM (discredited):
  Climate/environment → human character → institutions → civilizational outcomes
  Montesquieu (1748): hot climates → "languid" peoples → despotism
  Ratzel (1882): environment determines culture
  Huntington (1915): civilization shaped by climate stimulation
  Status: scientifically rejected; provided justification for racism

  POSSIBILISM (Vidal de la Blache, early 20th C):
  Environment sets limits and opportunities; humans choose within them
  Culture + technology determine how those possibilities are used
  → More defensible; but can be tautological (anything is possible)

  DIAMOND — GUNS, GERMS, AND STEEL (1997):
  Geographic luck explanation for cross-continental inequality
  ┌────────────────────────────────────────────────────────────────┐
  │ DIAMOND'S CAUSAL CHAIN:                                        │
  │                                                                │
  │ Eurasia's E-W axis → crops/animals spread along same latitude │
  │ → same climate → rapid diffusion of domesticates              │
  │                                                                │
  │ Americas/Africa N-S axes → climate barriers → slower diffusion│
  │                                                                │
  │ Domesticable plants + animals → food surplus → population     │
  │ density → specialization → state capacity → technology →      │
  │ military advantage + disease immunity                          │
  │                                                                │
  │ 13 large domesticable mammals in Eurasia; 1 in Americas       │
  │ (llama); 0 in sub-Saharan Africa (zebras aren't domesticable) │
  └────────────────────────────────────────────────────────────────┘

  WHAT SURVIVES THE CRITIQUE OF DIAMOND:
  • E-W axis advantage for crop diffusion is documented
  • Zoonotic disease from animal domestication is real
  • Early agricultural advantage compounds over millennia
  • Geographic luck DID matter for initial state formation

  WHAT DOESN'T SURVIVE:
  • Ignores subsequent agency, institutions, colonial extraction
  • Overpredicts from geography (New Guinea should be rich by logic)
  • Selection on outcomes (explains European success, leaves gaps)
  • Proximate explanation labeled as ultimate (institutions matter independently)
  • Acemoglu/Robinson ("Why Nations Fail") shows institutions matter
    independently of geography — same geography, different outcomes
    (Nogales, AZ vs Nogales, Mexico; North vs South Korea)

  CURRENT CONSENSUS:
  Geography → early advantage (climate/disease/agriculture)
  Institutions → proximate cause of current divergence
  Both matter; neither alone is sufficient
```

---

## Section 3: Geographic Foundations of History

```
  RIVER VALLEY CIVILIZATIONS:
  ┌────────────────────────────────────────────────────────────────┐
  │ Tigris-Euphrates (Mesopotamia): seasonal flooding + silt;     │
  │   first writing (Sumer), first cities, irrigation networks    │
  │                                                                │
  │ Nile: predictable annual flood + narrow fertile corridor;     │
  │   isolation (desert buffer) → long political continuity       │
  │                                                                │
  │ Indus: less excavated; Harappa/Mohenjo-Daro; urban planning   │
  │                                                                │
  │ Yellow/Yangtze: loess soil; hydraulic state management;       │
  │   China's north-south agricultural/climate divide still visible│
  └────────────────────────────────────────────────────────────────┘

  BARRIER AND HIGHWAY EFFECTS:
  Mountain barriers: Alps → Rome isolated N Europe contact
                     Himalayas → South Asia geographic unit
                     Hindu Kush → Central Asia corridor (Khyber Pass)
  Water highways: Mediterranean as Roman lake (connectivity)
                  Straits: Constantinople controls Black Sea access

  ISLAND/PENINSULA EFFECTS:
  Islands: UK island position → defensive moat vs costly engagement
  Peninsulas: Korea/Italy/Iberia → contested spaces, trade routes
  Isthmus: Panama → bottleneck; historically very different on each side

  STEPPES AND NOMADIC POWER:
  Eurasian steppe: continuous grassland highway from Hungary to Mongolia
  → Cavalry mobility → successive nomadic empires (Mongols, Turks, Huns)
  → Agricultural sedentary states consistently vulnerable to steppe raids
  → Wall-building (Great Wall, Hadrian's Wall) as response
```

---

## Section 4: Spatial Analysis Tools

```
  GIS (Geographic Information Systems) — the spatial database stack:
  Conceptually: a spatial RDBMS with geometry types + spatial indexes
  PostGIS: spatial extension to PostgreSQL; ST_Within, ST_Intersects,
           ST_Buffer, ST_Distance — SQL over geometry; R-tree indexes
  QGIS: open-source desktop GIS (ArcGIS ESRI is the commercial equiv.)
  Google Earth Engine: planetary-scale raster compute (serverless)
  Layers: vector (points/lines/polygons with attributes) +
          raster (georeferenced grid; pixel = value at location)
  Core operations: spatial join, overlay, buffer, dissolve, network analysis

  DEVELOPER TOOLCHAIN (Python spatial stack):
  GDAL: the foundational C++ library; reads/writes 200+ vector + raster
        formats; everything else depends on it
  Shapely: geometric operations in Python (union, intersection, difference)
  GeoPandas: GeoDataFrame = pandas DataFrame + geometry column + CRS
             → spatial joins, dissolve, overlay as DataFrame ops
  Rasterio: Python GDAL wrapper for raster I/O + windowed reads
  Pyproj: coordinate reference system transforms (PROJ under the hood)

  CLOUD-NATIVE SPATIAL FORMATS:
  COG (Cloud-Optimized GeoTIFF): tiled + overviewed raster; HTTP range
    requests enable reading subregions without downloading full file
  Zarr: N-dimensional array store; replaces NetCDF for climate model data;
    chunked + compressed; S3-native; xarray reads it like an array
  GeoParquet: columnar vector format; geometry as WKB in Parquet column;
    spatial predicate pushdown in DuckDB / Spark

  REMOTE SENSING (image ML pipeline framing):
  Input: multispectral satellite imagery (Landsat 8: 11 bands; Sentinel-2: 13)
  Band math: NDVI = (NIR - Red)/(NIR + Red) → vegetation index
             NDWI = (Green - NIR)/(Green + NIR) → water extent
  Pipeline: ingest COG → cloud-mask → composite → classification → change detection
  Google Earth Engine executes this over petabytes server-side
  Supervised classification: pixel-wise ML (RF, SVM, CNN) on band values
  Applications: land cover mapping, deforestation alerts, crop yield,
                flood extent, urban expansion, glacier retreat

  SPATIAL STATISTICS (graph signal processing framing):
  Tobler's Law = spatial autocorrelation assumption: adjacent nodes
    in the spatial graph tend to have correlated values
  Moran's I: global spatial autocorrelation statistic (-1 to +1);
    analogous to signal autocorrelation coefficient in time series
  Kriging: geostatistical interpolation; fits a variogram (covariance
    function of distance) then uses it as a spatial kernel for
    Gaussian process regression — interpolation with uncertainty bounds
  Getis-Ord Gi*: local statistic identifying spatial clusters (hot spots)
    vs dispersed cold spots; Z-score per feature
  Spatial regression: OLS with spatially correlated residuals violates
    independence; spatial lag model (Moran's I correction) or spatial
    error model handles the dependence structure

  CARTOGRAPHIC PROJECTIONS (coordinate transforms):
  All map projections are bijective transforms from ellipsoidal (lat/lon)
    to planar coordinates; all distort at least one of: shape/area/distance
  Mercator: conformal (preserves angles/shapes locally); area distortion
    extreme at poles; Greenland appears same size as Africa (1/14th actual)
  Gall-Peters: equal-area; shape distorted; political statement (global south)
  Robinson/Winkel Tripel: compromise projections for world maps
  UTM (Universal Transverse Mercator): 60 zones × 6°; nearly conformal
    within each zone; what most local GIS work uses
  For data viz: use equal-area projections for choropleth; conformal for
    navigation; match projection to the decision being made

  MAUP → SPATIAL AGGREGATION:
  Statistical results are not projection-invariant to aggregation unit.
  Same data → different conclusions at county vs state vs census tract.
  This is the same as choosing bin widths in a histogram, but in 2D.
  Solutions: multi-scale analysis, dasymetric mapping (weight by ancillary
    data), areal interpolation (transfer values across mismatched units)
```

---

## Module Map

| Module | Topic | Key Concepts |
|--------|-------|-------------|
| `01-PHYSICAL-GEOGRAPHY` | Tectonics, geomorphology, rock cycle, soils | Plate boundaries, landform types, soil orders, volcanism |
| `02-CLIMATE-ZONES` | Köppen classification, climate controls, biomes | A/B/C/D/E zones, ITCZ, orographic effect, biome distribution |
| `03-OCEAN-ATMOSPHERE` | Thermohaline circulation, ENSO, monsoons | AMOC, gyres, El Niño/La Niña, teleconnections |
| `04-BIOGEOGRAPHY` | Species distributions, island biogeography, range shifts | Wallace Line, MacArthur-Wilson, NPP, invasive species |
| `05-POPULATION-URBAN` | Demographic transition, urbanization, migration | DTM stages, Zipf's Law, megacities, migration flows |
| `06-GEOPOLITICS-RESOURCES` | Oil, water, rare earths, chokepoints, Arctic | Hormuz/Malacca, aquifer stress, REE supply chains |
| `07-ECONOMIC-GEOGRAPHY` | Agglomeration, core-periphery, GVCs, ports | Marshall districts, world-systems, smile curve, TEU |

---

## Decision Cheat Sheet

| Geographic Question | Analytic Entry Point |
|---|---|
| Why is X region wealthy/poor? | Institutions (primary) + geographic constraints (secondary); avoid pure determinism |
| Why do cities form where they are? | Central place theory + access to water/trade + agglomeration effects |
| Why do species distributions end sharply? | Tectonic history (Wallace Line) + climate barriers |
| Why does climate vary across small distances? | Orographic effect, ocean currents, continentality |
| How does resource location shape geopolitics? | Chokepoints + resource curse + great power competition for access |
| Why do some agricultural areas succeed? | Soil (CLORPT), water access, climate zone, market connectivity |

---

## Common Confusion Points

**Geographic determinism is not the same as geography mattering**: saying that
the Sahara creates a transportation barrier is an observation. Saying that
Africans are incapable of complex civilization because of their climate is
determinism. Geography constrains and shapes options; it does not determine
culture or character.

**Scale confusion is endemic**: crime rates differ by neighborhood vs city vs
state vs country levels. Urban sprawl looks different at parcel vs metro scale.
Always ask: at what scale was this finding established, and does it transfer?

**"Natural boundaries" are political constructs**: the Rhine, Danube, Himalayan
crest, or 49th parallel were not foreordained as national borders. States chose
geographic features as convenient lines. Geography creates friction, not destiny.

**Megacity ≠ rich city**: Tokyo and Lagos are both megacities. Size is driven by
population growth + migration, not development level. The governance challenges
are fundamentally different.
