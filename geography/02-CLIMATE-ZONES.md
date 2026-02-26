# Climate Zones & Biomes

## The Big Picture

Climate is the statistical description of atmospheric conditions over decades.
The Köppen classification is the canonical system — empirically derived from
vegetation distributions in the 1900s, it remains the standard framework.
Every climate zone is the product of four interacting controls: latitude,
altitude, continentality, and ocean currents. Biomes map onto climate zones
with remarkable fidelity — you can reconstruct one from the other.

```
+----------------------------------------------------------------------+
|                    CLIMATE CONTROL HIERARCHY                          |
|                                                                      |
|  LATITUDE              → primary driver (solar angle → insolation)  |
|  │                                                                   |
|  ├── Tropical (0°-23.5°N/S)  ←──── ITCZ (follows solar zenith)    |
|  │     ITCZ migration → wet-dry seasonality ←──── Ocean SST         |
|  │                                                                   |
|  ├── Subtropical (23.5°-35°): HIGH PRESSURE BELTS                   |
|  │     Descending air → deserts      ←──── Cold upwelling currents  |
|  │     (Sahara, Arabian, Sonoran)          amplify dryness on W coasts
|  │                                                                   |
|  ├── Temperate (35°-60°): MIDLATITUDE WESTERLIES                    |
|  │     Storm tracks; ocean moderation ←── Warm currents (Gulf Stream)
|  │     4 seasons on continental interiors ←── Continentality effect  |
|  │                       ↑                                           |
|  │                 OROGRAPHY: mountains intercept westerly flow     |
|  │                 Windward: wet; Leeward: rain shadow / dry         |
|  │                 (Pacific NW wet / Great Basin dry)               |
|  │                                                                   |
|  ├── ALTITUDE (cross-cuts all latitude zones):                       |
|  │     −6.5°C per 1000m → compressed climate zones vertically       |
|  │     Mountains create local climate envelope regardless of latitude|
|  │                                                                   |
|  └── Polar (60°-90°): COLD POLAR HIGH PRESSURE                     |
|        Ice caps, tundra, permafrost                                  |
+----------------------------------------------------------------------+
```

---

## Section 1: Climate Controls

```
  LATITUDE (primary):
  Solar angle → energy per unit area
  Tropics receive ~2.5× more solar energy than poles
  → Controls base temperature + drives atmospheric circulation

  ALTITUDE:
  Environmental lapse rate: ~6.5°C/1000m rise
  At 5000m: ~32.5°C cooler than sea level
  Mountains create compressed climate zones vertically
  (Andean pisos altitudinales: discussed below)
  Orographic effect: rainfall asymmetry across mountain ranges

  CONTINENTALITY:
  Interior of continents = away from ocean moderating effect
  → Larger temperature range (hotter summers, colder winters)
  → Less moisture (far from evaporation source)
  Compare: Lisbon (maritime Csa) vs Moscow (Dfb/Dfc) same ~latitude

  OCEAN CURRENTS:
  ┌──────────────────────────────────────────────────────────────┐
  │ WARM CURRENTS (equatorward → poleward flow):                 │
  │ Gulf Stream/North Atlantic Drift: warms W Europe; UK/Ireland │
  │   ~10°C warmer than same latitude in Canada/Russia           │
  │ Kuroshio: warms Japan's Pacific coast                        │
  │ Effect: mild, wet climates on western coasts in midlatitudes  │
  │                                                              │
  │ COLD CURRENTS (poleward → equatorward flow):                 │
  │ California Current: cools W USA; summer fog (San Francisco)  │
  │ Humboldt/Peru Current: cold and dry; Atacama Desert          │
  │ Benguela: cold and dry; Namib Desert                         │
  │ Canary: dry NW Africa coast                                  │
  │ Effect: desert formation on W coasts at subtropical latitudes │
  └──────────────────────────────────────────────────────────────┘

  ITCZ (Intertropical Convergence Zone):
  Belt of convergence near equator where trade winds meet
  Rising air → convection → heavy rainfall → tropical rainforest
  Migrates seasonally following solar zenith
  → African/Asian wet season follows ITCZ migration (monsoons)
  Over ocean: narrow; over land: broader seasonal movement

  OROGRAPHIC EFFECT:
  Windward side: air rises → cools → condenses → precipitation
  Leeward side: air descends → warms → dry (rain shadow)
  Examples: Pacific NW (windward wet) vs eastern Cascades/Rockies (dry)
            Western Ghats (wet) vs Deccan Plateau (rainshadow)
            Southern Alps NZ (3000mm W coast, 600mm E coast)
```

---

## Section 2: Köppen Classification

```
  SYSTEM OVERVIEW:
  Five primary groups based on temperature + precipitation thresholds
  Each group has subtypes based on seasonal distribution

  A — TROPICAL (all months ≥18°C):
  ┌──────────────────────────────────────────────────────────────┐
  │ Af (Tropical Rainforest): no dry month (<60mm)               │
  │   Amazon, Congo, SE Asia (Borneo, Sumatra)                   │
  │   Characteristics: high humidity, minimal temperature range, │
  │   highest biodiversity on Earth                              │
  │                                                              │
  │ Am (Tropical Monsoon): brief dry season but ≥100mm wettest   │
  │   month; makes up for dry season                             │
  │   Sri Lanka, coastal SE Asia, parts of Amazon               │
  │                                                              │
  │ Aw (Tropical Savanna): distinct dry season (<60mm/month)     │
  │   African savanna, Brazilian cerrado, Indian Deccan plateau  │
  │   Wet + dry season follows ITCZ migration                   │
  └──────────────────────────────────────────────────────────────┘

  B — DRY (evapotranspiration > precipitation):
  ┌──────────────────────────────────────────────────────────────┐
  │ BW (Desert): extreme aridity                                  │
  │   BWh: hot desert — Sahara, Arabian, Sonoran, Australian     │
  │         interior; year-round high pressure + cold upwelling  │
  │   BWk: cold desert — Gobi, Atacama interior, Patagonia;      │
  │         continentality + rain shadow                         │
  │                                                              │
  │ BS (Steppe): semi-arid                                       │
  │   BSh: hot steppe — Sahel, inner Australia                   │
  │   BSk: cold steppe — Central Asia, US Great Plains           │
  │   Transition zone between desert and more humid climates     │
  └──────────────────────────────────────────────────────────────┘

  C — TEMPERATE (warmest month >10°C, coldest -3°C to 18°C):
  ┌──────────────────────────────────────────────────────────────┐
  │ Cs (Mediterranean): dry summer, wet winter                   │
  │   Csa: hot summer (>22°C) — Mediterranean Basin, California  │
  │         central valley, central Chile, SW Australia, S Africa│
  │   Csb: warm summer — coastal California, Portugal, W Oregon  │
  │   Fire-adapted shrubland (chaparral/maquis/fynbos)           │
  │   Summer dryness: subtropical high pressure moves poleward   │
  │                                                              │
  │ Cf (Temperate, no dry season):                               │
  │   Cfa: humid subtropical — SE USA, SE China, SE South America│
  │         Japan; hot/humid summer; mild winter                 │
  │   Cfb: oceanic — W Europe, Pacific NW, SE Australia;         │
  │         mild year-round, overcast, no extreme months         │
  │   Cfc: subpolar oceanic — Scotland, Iceland, far SW Norway   │
  └──────────────────────────────────────────────────────────────┘

  D — CONTINENTAL (warmest month >10°C, coldest < -3°C):
  ┌──────────────────────────────────────────────────────────────┐
  │ Dfa/Dfb: humid continental — Great Plains/Midwest USA,       │
  │   NE USA, Central Europe, N China                            │
  │   Dfa: hot summer; Dfb: warm summer                          │
  │   Large temperature range; four distinct seasons             │
  │                                                              │
  │ Dfc: subarctic/boreal — S Canada, Russia (taiga belt),       │
  │   Scandinavia; short cool summer; very cold winter           │
  │   Huge: covers ~25% of Earth's land area                     │
  │   Dfd: extremely cold winter (Siberia: -68°C record)         │
  └──────────────────────────────────────────────────────────────┘

  E — POLAR (warmest month <10°C):
  ┌──────────────────────────────────────────────────────────────┐
  │ ET (Tundra): warmest month 0-10°C; brief summer; permafrost  │
  │   Arctic coasts, high mountains                              │
  │   Vegetation: mosses, sedges, dwarf shrubs, lichens          │
  │                                                              │
  │ EF (Ice Cap): all months <0°C; Greenland interior, Antarctica│
  └──────────────────────────────────────────────────────────────┘
```

---

## Section 3: Biome Distribution

```
  BRIDGE — KOPPEN AS A DECISION TREE CLASSIFIER:
  Koppen (1900, revised 1936) is a threshold-based rule system empirically
  derived from vegetation distributions — exactly how an engineer would
  build a rule-based classifier from training data. The classification logic:

  IF all_months_temp ≥ 18°C → A (Tropical)
    IF driest_month ≥ 60mm → Af (Rainforest)
    ELSE IF driest_month ≥ (100 - annual_precip/25) → Am (Monsoon)
    ELSE → Aw (Savanna)
  ELIF evapotranspiration > precipitation → B (Dry)
    Threshold: P < 20×(T + 7) for winter rain regime, etc.
    (multiple sub-rules for BWh/BWk/BSh/BSk)
  ELIF coldest_month > 18°C → (invalid — already A)
  ...and so on as a decision tree over temperature + precipitation thresholds.

  The biome-climate correlation achieves ~90% accuracy with just mean annual
  temperature × mean annual precipitation as features — a two-feature linear
  classifier in climate space. Koppen zones are the decision boundaries.
  Modern GCMs output raster grids that are literally classified pixel-by-pixel
  using these rules to produce future Köppen maps.

  BIOME-CLIMATE RELATIONSHIP:
  Climate envelope determines which biome occurs — ~90% predictable from
  mean annual temperature × mean annual precipitation alone

  ┌─────────────────────────────────────────────────────────────────┐
  │             BIOME DISTRIBUTION (temperature × precipitation)    │
  │                                                                 │
  │  Temperature (warm → cold)                                      │
  │  High ↓                                                         │
  │        Tropical RF  │ Tropical dry  │  Savanna                  │
  │        (Af)         │ forest        │  (Aw)                     │
  │  ───────────────────┼───────────────┼─────────────────────────  │
  │        Humid subtrop│ Mediterranean │  Temperate                │
  │        (Cfa)        │ (Cs) shrubland│  grassland (BS/D)         │
  │  ───────────────────┼───────────────┼─────────────────────────  │
  │        Temperate    │ Mixed forest  │  Desert (BW)              │
  │        deciduous    │               │                           │
  │        (Cfb/Cfa)    │               │                           │
  │  ───────────────────┼───────────────┼─────────────────────────  │
  │        Boreal/taiga │ Boreal (Dfc)  │  Cold desert              │
  │  ───────────────────┼───────────────┼─────────────────────────  │
  │  Low T  Tundra (ET) │               │  Ice cap (EF)             │
  │        ←────────────────────────────────────────→              │
  │               Wet (high precip)     Dry (low precip)           │
  └─────────────────────────────────────────────────────────────────┘

  TROPICAL RAINFOREST:
  Characteristics: ~2000-4000mm/yr; temp 25-30°C; low seasonality
  Biodiversity: >50% of all species on 7% of land area
  Layers: emergent, canopy, understory, shrub, ground
  Soils: paradoxically infertile — nutrients in biomass, not soil

  SAVANNA:
  Fire-adapted; C4 grasses dominate; wet/dry seasonality
  African savanna supports megafauna (lacking in other biomes)
  Cerrado (Brazil): world's most biodiverse savanna

  MEDITERRANEAN (Chaparral/Maquis/Fynbos):
  Convergent evolution on 5 continents at same latitude (30-45°)
  Shrubs adapted to summer drought + fire: thick waxy leaves, deep roots
  Post-fire regeneration strategies (resprouting/seeding)

  BOREAL FOREST (TAIGA):
  Largest terrestrial biome by area (~17M km²)
  Dominated by conifer monocultures (spruce, fir, pine, larch)
  Soil: Spodosols (acidic, leached, podzolized)
  Carbon storage: comparable to tropical forests

  TUNDRA:
  Permafrost layer below surface; limits rooting depth
  Active layer thaws seasonally → waterlogging, thermokarst lakes
  Climate feedback: permafrost thaw → CH₄ and CO₂ release
  Rapidly warming (Arctic amplification: 2-4× global average rate)
```

---

## Section 4: Altitude as Latitude Analog

```
  ANDEAN PISOS ALTITUDINALES (altitudinal climate zones):
  ┌──────────────────────────────────────────────────────────────┐
  │ Tierra Caliente: 0-1000m; tropical; sugarcane, bananas,      │
  │   cacao; humid; original colonist disease zone              │
  │                                                              │
  │ Tierra Templada: 1000-2000m; "temperate"; coffee, maize,    │
  │   temperate crops; most colonial capitals sited here (Bogotá,│
  │   Mexico City, Guatemala City — disease avoidance + climate) │
  │                                                              │
  │ Tierra Fría: 2000-3500m; cool; potatoes, wheat, barley       │
  │   (Inca staples); major Andean cities at this elevation      │
  │                                                              │
  │ Tierra Helada: 3500-4800m; frost common; root crops, llamas  │
  │   pastoralism; treeline upper boundary                       │
  │                                                              │
  │ Páramo/Puna: 4800m+; frost nightly; specialized high-altitude│
  │   shrubs; above treeline; Andean glaciers                    │
  └──────────────────────────────────────────────────────────────┘

  TREELINE:
  Global altitude ~3000m in tropics → lower at higher latitudes
  Temperature threshold: mean July temp <10°C → treeless
  Equivalent to polar treeline (boreal-tundra boundary)
  Climate warming → treeline advancing upslope/poleward

  ALPINE ZONES ON ALL CONTINENTS:
  Each major mountain range has its own altitudinal zonation
  East African equatorial mountains (Kilimanjaro): tropical base →
    montane forest → heath/moorland → alpine desert → snow cap
```
---

## Section 5: Climate Zone Shifts Under Warming

```
  PROJECTED KOPPEN ZONE MIGRATIONS (RCP 8.5, 2°C+ warming):
  ┌────────────────────────────────────────────────────────────────┐
  │ TROPICAL ZONES (A) EXPANDING POLEWARD:                         │
  │ → Tropical wet-dry zone (Aw) migrating ~50–200 km poleward    │
  │ → Subtropics (B zones) following: Sahara expanding S + N edges│
  │ → Sahel wetter in some models (ITCZ shift); drier in others   │
  │   (high model disagreement due to vegetation feedbacks)        │
  │                                                                │
  │ MEDITERRANEAN ZONES (Cs) POLEWARD + WIDER:                     │
  │ → Cs zones expanding 100–200 km poleward in both hemispheres  │
  │ → California: longer fire seasons; summer drought intensifying │
  │ → Mediterranean Basin: more extreme summer dryness             │
  │ → SW Australia: significant drying trend already observed      │
  │                                                                │
  │ BOREAL (Dfc) CONTRACTING FROM SOUTH:                           │
  │ → Temperate (C zones) advancing into current D zone territory  │
  │ → Boreal forest gaining from north (Arctic boundary retreats)  │
  │ → Net effect: latitudinal compression of boreal belt           │
  │                                                                │
  │ POLAR (E) ZONES SHRINKING:                                     │
  │ → ET tundra converting to Dfc boreal in some projections       │
  │ → Permafrost thaw boundary advancing northward                 │
  │ → EF (ice cap) zone: Greenland margins transitioning           │
  └────────────────────────────────────────────────────────────────┘

  TREELINE DYNAMICS:
  Alpine treeline: advancing upslope 1–4 m/decade in Alps, Rockies,
    Scandinavia; measured via repeat photography and remote sensing
  Polar treeline: boreal advancing into tundra; shrubification of
    Arctic observed via NDVI (AVHRR 30-year record shows greening)
  Rate mismatch: trees migrate at 5–20 km/decade; climate zones
    shifting at 20–40 km/decade → climate debt accumulates
    (vegetation lags climate envelope, especially after disturbance)

  BIOME REDISTRIBUTION PROJECTIONS:
  Amazon dieback hypothesis: ~4°C warming + deforestation → tipping
    point where Amazon forest transitions to savanna/cerrado
    (positive feedback: less transpiration → less rainfall → drying)
  Coral reefs: effectively no viable reef habitat at >2°C above
    pre-industrial if current thermal tolerance not exceeded
  Permafrost: ~17% of global carbon stock at risk of mobilization
    as CO₂/CH₄ under sustained Arctic warming

  OBSERVED CHANGE (already documented):
  Koppen zone boundary shifts: ~5.5% of global land area shifted
    zones 1950–2010 (Chen & Chen 2013)
  Arid/semi-arid (B zones): expanded by ~5% in same period
  Every decade since 1980: warmest decade in instrumental record
```

---

## Decision Cheat Sheet

| Climate Question | Answer |
|---|---|
| What creates the Sahara? | Subtropical high pressure (descending dry air) + cold Canary Current on NW coast |
| Why is W Europe mild? | Gulf Stream/N Atlantic Drift (warm ocean current) shifts climate poleward |
| Why is the Atacama the driest place on Earth? | Cold Humboldt Current + rain shadow of Andes + subtropical high pressure — triple mechanism |
| What drives monsoons? | ITCZ seasonal migration + differential heating of land vs ocean |
| How do I read a climate zone from biome? | Tropical RF → Af; Savanna → Aw; Mediterranean shrubland → Cs; Boreal → Dfc; Tundra → ET |
| What's altitude's temperature effect? | −6.5°C per 1000m rise (lapse rate) |
| What creates orographic rainfall? | Windward uplift → cooling → condensation; leeward sinking → warming → dry |

---

## Common Confusion Points

**Deserts are not defined by temperature**: the Gobi Desert is cold; the Atacama
is cool. Deserts are defined by aridity (evapotranspiration > precipitation).
Cold deserts occur in rain shadows, interior continents, or where cold currents
create dry conditions.

**Mediterranean climates are winter-wet, summer-dry**: the opposite of the
intuition many people have. The California drought "fire season" is summer-fall
— when the Mediterranean dry season hits. Seasonal dry patterns drive fire risk,
not annual totals.

**Tropical soils are not fertile**: this surprises people looking at lush
rainforests. The forest IS the fertility — nutrient cycling is so rapid that
cutting the forest exposes infertile, often toxic latosol. Amazon deforestation
for agriculture typically fails within 5 years.

**Climate ≠ weather**: climate is the 30-year statistical norm; weather is
what happens today. A cold winter doesn't contradict climate warming — you
need decadal data. The 30-year WMO climate normals (1991-2020) are the reference.
