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
|                    GEOGRAPHY FIELD MAP                                |
|                                                                      |
|  PHYSICAL GEOGRAPHY                  HUMAN GEOGRAPHY                 |
|  ──────────────────                  ──────────────                  |
|  Geomorphology (landforms)           Population + Urban              |
|  Climatology (patterns)              Economic geography              |
|  Biogeography (species)              Political geography             |
|  Hydrology (water)                   Cultural geography              |
|  Pedology (soils)                    Historical geography            |
|  Oceanography (seas)                                                  |
|                                                                      |
|  INTEGRATING FRAMEWORKS              ANALYTICAL TOOLS                |
|  ─────────────────────               ─────────────────               |
|  Geographic determinism              GIS + Remote Sensing            |
|  Possibilism                         Spatial autocorrelation         |
|  World-systems theory                MAUP (scale effects)            |
|  Geopolitics                         Satellite/NDVI data             |
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
  Gerrymandering exploits MAUP deliberately

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
  GIS (Geographic Information Systems):
  Software: ArcGIS (ESRI), QGIS (open source), Google Earth Engine
  Layers: vector (points/lines/polygons) + raster (grid cells)
  Operations: overlay analysis, buffer, interpolation, network analysis
  Applications: disease mapping, supply chain, electoral analysis,
                urban planning, climate vulnerability

  REMOTE SENSING:
  Satellite imagery (Landsat, Sentinel, commercial: Planet)
  NDVI: Normalized Difference Vegetation Index = (NIR - Red)/(NIR + Red)
  → 0-1 scale; tropical forest ~0.7, bare soil ~0.1
  Applications: land cover change, deforestation detection, crop yield
                estimation, urban heat island mapping, flood extent

  SPATIAL STATISTICS:
  Moran's I: measures spatial autocorrelation (-1 to +1)
  Kriging: geostatistical interpolation using variogram
  Hot spot analysis (Getis-Ord Gi*): identifies spatial clusters
  Spatial regression: accounts for spatial dependencies

  CARTOGRAPHIC PROJECTIONS:
  All projections distort at least one of: shape/area/distance/direction
  Mercator: preserves shape (conformal); greatly distorts area at poles
  → Greenland appears same size as Africa (actually 1/14th the area)
  Peters/Gall-Peters: equal area; distorts shape
  Robinson: compromise (both distorted moderately)
  For data visualization: choose projection that matches analytic need
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
