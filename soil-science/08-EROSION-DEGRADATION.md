# Soil Erosion and Degradation: USLE, Wind, Salinization, Compaction

## The Big Picture

Soil degradation is the decline in soil quality and productivity from human or natural causes. Erosion (water and wind), salinization, compaction, and organic matter depletion are the four dominant mechanisms of degradation. They destroy the foundation of food security — and most occur invisibly and irreversibly on human timescales.

```
SOIL DEGRADATION — MECHANISMS AND INTERACTIONS

  PHYSICAL                CHEMICAL              BIOLOGICAL
  +------------------+   +------------------+  +------------------+
  | Water erosion    |   | Salinization     |  | OM depletion     |
  | Wind erosion     |   | Acidification    |  | Reduced microbial|
  | Compaction       |   | Alkalinization   |  | diversity        |
  | Hard setting     |   | Metal contamin.  |  | Loss of fauna    |
  | Crusting         |   | Nutrient deple.  |  | (earthworms etc.)|
  | Waterlogging     |   | Pesticide accum. |  |                  |
  +------------------+   +------------------+  +------------------+
          |                      |                      |
          +----------------------+----------------------+
                                 |
                         DESERTIFICATION
                    (terminal land degradation in dryland systems)
```

---

## Section 1 — Water Erosion

### USLE / RUSLE

The Universal Soil Loss Equation (Wischmeier & Smith, 1965) and its Revised version (Renard et al., 1997) are the most widely used erosion prediction tools.

```
  USLE / RUSLE:
  A = R × K × L × S × C × P

  Where:
    A = average annual soil loss (tonnes/ha/yr)
    R = rainfall erosivity factor (MJ·mm/ha·hr·yr)
    K = soil erodibility factor (t·ha·hr/ha·MJ·mm)
    L = slope length factor (dimensionless)
    S = slope steepness factor (dimensionless)
    C = cover-management factor (dimensionless; 0–1)
    P = support practice factor (dimensionless; 0–1)

  FACTOR DESCRIPTIONS AND RANGES:

  R (Rainfall erosivity):
  Kinetic energy × intensity of rain; erosive power of rainfall
  USA Corn Belt: ~100–200 MJ·mm/ha·hr·yr
  Humid tropics (convective): 500–1000+ (very erosive)
  Arid: < 50 (low rain erosivity, but wind erosion higher)

  K (Soil erodibility):
  Resistance of soil surface to detachment and transport
  Sandy loam: ~0.05 t·ha·hr/ha·MJ·mm (low erodibility; drains fast)
  Silt loam: ~0.35–0.40 (HIGHEST erodibility; prone to sealing)
  Clay: ~0.02–0.20 (low; structure resists detachment)
  Key: high silt = high erodibility; organic matter reduces K

  L × S (Topographic factor):
  LS = (λ/22.1)^m × (65.41 sin²θ + 4.56 sinθ + 0.065)
  Short steep slopes: LS = 5–10; terraced/flat: LS = 0.1–0.5

  C (Cover-management factor):
  Continuous fallow (bare soil): C = 1.0 (reference)
  Moldboard plow, corn: C = 0.4–0.6
  No-till with residue: C = 0.1–0.2
  Established pasture: C = 0.01–0.05
  Forest with understory: C = 0.001–0.01
  This factor is the most powerful management leverage point
```

### Example Calculation

```
  EXAMPLE: Corn field in Iowa
  R = 150 MJ·mm/ha·hr·yr (Iowa rainfall erosivity)
  K = 0.38 (Tama silty clay loam; high silt content)
  L = 1.2 (65 m field length)
  S = 2.1 (6% slope steepness)
  C = 0.5 (conventionally tilled corn)
  P = 0.6 (contour farming)

  A = 150 × 0.38 × 1.2 × 2.1 × 0.5 × 0.6
  A = 150 × 0.38 × 1.2 × 2.1 × 0.3
  A = 150 × 0.38 × 0.756 = 43 t/ha/yr

  COMPARE to soil formation rate: ~0.5–2 t/ha/yr
  This field is losing soil 20–80× faster than it can form
  T-VALUE (tolerable soil loss): 5–11 t/ha/yr (NRCS standard by soil depth)
  This field is 4–9× above the tolerable loss rate
```

### Erosion Stages

```
  WATER EROSION SEQUENCE:

  1. RAINDROP IMPACT (splash erosion):
     Kinetic energy: KE = 0.5mv²; 5mm rain = ~1 million drops/m²
     Detaches 50–90 tonnes/ha if soil is bare!
     Aggregate break-up; dispersed particles seal surface

  2. SHEET EROSION:
     Thin layer of turbulent water flows across surface
     Removes finest, most nutrient-rich particles (clay, OM, microbes)
     Invisible: you cannot see it happening in real time
     Often the largest mass transport pathway

  3. RILL EROSION:
     Concentrated flow creates small channels < 30 cm deep
     Can be tilled out; may be visible as parallel rills

  4. GULLY EROSION:
     Deep channels > 30 cm; cannot be tilled out
     Irreversible without major intervention
     Accelerates: 1 gully captures more runoff --> enlarges

  5. STREAMBANK/CHANNEL EROSION:
     Lateral undercutting; collapse of overhangs
     Sediment input to rivers; turbidity problems
```

---

## Section 2 — Wind Erosion

Wind erosion is the dominant degradation process in arid and semi-arid regions and on exposed agricultural soils in dry continental interiors.

```
  WIND EROSION MECHANICS — THREE TRANSPORT MODES:

  SALTATION (50–70% of total mass):
  Sand-sized particles (0.1–0.5 mm) bounce along surface
  Lifted by drag force; bounce on impact; knock other particles loose
  Saltation height: 20–50 cm above ground
  Distance: 0.5–2 m per bounce

  CREEP (5–25%):
  Particles too heavy to saltate (> 0.5 mm)
  Pushed along surface by saltating particles
  Very slow; mostly near source

  SUSPENSION (15–40%):
  Fine particles (< 0.1 mm; silt + clay) lifted into air column
  Can travel thousands of kilometers
  Saharan dust deposits in Amazonia; Chinese loess in Pacific
  Health impact: PM10/PM2.5 respiratory disease

  THRESHOLD VELOCITY:
  Fluid threshold: ~5–7 m/s (15–25 km/h) to initiate saltation
  Impact threshold: ~3–4 m/s to maintain saltation (lower once started)
  (Non-erodible elements: > 6 mm gravel, crop residue, vegetation shield surface)

  WEQ (WIND EROSION EQUATION):
  E = f(I, K, C, L, V)
  I = soil erodibility (texture + structure)
  K = ridge roughness (tillage-created ridges reduce erosion)
  C = climatic factor (wind speed + soil moisture)
  L = unsheltered field length (bigger = more erosion)
  V = vegetative cover
```

---

## Section 3 — Soil Salinization

Salinization is the accumulation of soluble salts in the root zone to concentrations that reduce plant growth. It is the most widespread form of chemical soil degradation in irrigated agriculture.

### Primary vs. Secondary Salinization

```
  PRIMARY SALINIZATION:
  Natural accumulation in arid basins; ancient marine sediments
  Occurs without human intervention
  Examples: Naturally saline soils in Great Basin, Australian inland, Sahel
  Management: avoid; use salt-tolerant species; no cure in situ

  SECONDARY SALINIZATION (human-induced):
  Caused by irrigation with saline water + poor drainage
  MECHANISM:
  Irrigate --> water evaporates + transpires --> salts left behind
  Groundwater rises (capillary) --> evaporation concentrates salts at surface
  "Irrigation-induced" salinization: estimated 20–30% of all irrigated land affected

  SCALE OF PROBLEM:
  Global irrigated land: ~270 million ha
  Estimated degraded by salinization: 45–50 million ha (~18%)
  Annual loss to new salinization: ~1–2 million ha/yr
  Lost irrigation productivity: equivalent to ~0.3–0.5 million ha/yr at moderate degradation
```

### Salt Chemistry and Plant Effects

```
  SOIL SALINITY MEASUREMENT:
  EC (electrical conductivity) of saturated paste extract: ECe (dS/m)
  Normal soil: ECe < 2 dS/m
  Slightly saline: 2–4 dS/m
  Moderately saline: 4–8 dS/m (most crops affected above 4)
  Strongly saline: 8–16 dS/m
  Extremely saline: > 16 dS/m (only halophytes)

  PLANT RESPONSE — THRESHOLD-SLOPE MODEL:
  Maas-Hoffman model: Y = 100 - b(ECe - ECt)
  ECt = threshold ECe (no yield reduction below this level)
  b = % yield reduction per dS/m above threshold

  CROP SALT TOLERANCES:
  +-----------+------+-------+-------------------------------------------+
  | Crop      | ECt  | Slope | Classification                            |
  |           |(dS/m)| (%/   |                                           |
  |           |      |  dS/m)|                                           |
  +-----------+------+-------+-------------------------------------------+
  | Barley    | 8    | 5     | Tolerant (halophyte boundary)            |
  | Beet (sug)| 7    | 5.9   | Tolerant                                 |
  | Wheat     | 6    | 7.1   | Moderately tolerant                      |
  | Cotton    | 7.7  | 5.2   | Tolerant                                 |
  | Corn      | 1.7  | 12    | Moderately sensitive                     |
  | Soybean   | 5    | 20    | Moderately tolerant                      |
  | Potato    | 1.7  | 12    | Moderately sensitive                     |
  | Carrot    | 1    | 14    | Sensitive                                |
  | Strawberry| 1    | 33    | Very sensitive                           |
  +-----------+------+-------+-------------------------------------------+

  PHYSIOLOGY OF SALT DAMAGE:
  Osmotic effect: low water potential of saline soil; water flows OUT of roots
  Ion-specific toxicity: Na+ and Cl- interfere with enzyme function at high concentrations
  Nutrient imbalance: high Na+ displaces Ca2+, K+, Mg2+ from exchange sites
```

---

## Section 4 — Soil Compaction

Compaction is the rearrangement of soil particles under pressure, reducing pore space and increasing bulk density. It is the most widespread physical degradation in intensive agriculture.

```
  COMPACTION MECHANICS:
  Applied pressure > soil shear strength --> particles rearrange
  Air expelled from pores; pore volume decreases
  Bulk density increases; porosity decreases; hydraulic conductivity decreases

  COMPACTION SUSCEPTIBILITY:
  MOST SUSCEPTIBLE: moist silt loam (water lubricates particle movement)
  LEAST SUSCEPTIBLE: very wet clay (strength low, but plastic -- deforms; doesn't compact)
                     very dry clay (too rigid to compact without shattering)
                     sandy soil at field capacity (particles lock)

  COMPACTION LAYERS:
  +-- Surface compaction: top 10–15 cm; from tillage implements when wet
  +-- PLOWPAN (tillage pan): at tillage depth (15–25 cm)
      Dense layer created by plow sole pressure over many years
      Bulk density: 1.7–1.9 g/cm³ (vs. normal 1.2–1.5)
      Root growth stops or greatly slowed at plowpan
  +-- Subsoil compaction: 25–60 cm depth; from heavy machinery axle loads
      Very difficult to alleviate; persists 10–30 years
      Caused by: modern harvester axle loads > 10 tonnes

  MODERN FARM EQUIPMENT PROBLEM:
  1950s combine: ~3 tonnes axle load
  2010s combine (full grain tank): 15–18 tonnes axle load
  Contact pressure well exceeds subsoil bearing capacity during harvest
  Subsoil compaction from a single wheel pass can persist 20+ years
```

### Compaction Effects

```
  EFFECTS OF COMPACTION:

  PHYSICAL:
  Bulk density > 1.6 g/cm³ (loam): root elongation rate drops 50–90%
  Hydraulic conductivity: reduced 100–1000× in compacted layer
  Drainage: surface ponding; anaerobic conditions; delayed field access
  Pore continuity: macropores collapsed; preferential flow paths destroyed

  BIOLOGICAL:
  Earthworm populations: 50–80% lower in compacted vs. non-compacted soil
  Mycorrhizal colonization: reduced (hyphae cannot penetrate compacted soil)
  Microbial activity: reduced aeration --> slower aerobic decomposition

  YIELD IMPACT:
  Subsoil compaction: 5–20% yield reduction in dry years (drought stress)
  Surface compaction: variable; 5–30% in wet years (waterlogging)
  Compaction cost in EU agriculture: estimated ~3 billion €/yr (Schjønning et al. 2015)

  REMEDIATION:
  Surface compaction: can be reversed with one deep tillage pass (subsoiler to 40 cm)
                      or by deep-rooted cover crops (radish, turnip)
  Subsoil compaction: extremely difficult; deep tillage partially helps
                       biological remediation by tap-rooted crops (alfalfa: 2–4 m roots)
                       takes 10–20+ years for full recovery
```

---

## Section 5 — Desertification

Desertification = severe land degradation in arid, semi-arid, and dry sub-humid areas resulting from climatic variations AND human activities.

```
  DESERTIFICATION DEFINITION (UNCCD 1994):
  "Land degradation in arid, semi-arid, and dry sub-humid areas resulting
   from various factors including climatic variations and human activities"

  GLOBAL EXTENT:
  Dryland area: ~41% of Earth's land surface
  Population: ~2 billion people in drylands
  Degraded drylands: ~3.6 billion ha (UNCCD estimate)
  Actively desertifying: ~6 million ha/yr (UNCCD)

  DRIVERS:
  +-- Overgrazing: removal of vegetative cover; soil exposure; compaction by hooves
  +-- Deforestation: increased runoff; reduced evapotranspiration; wind erosion
  +-- Overcultivation: soil structural degradation; salinity; nutrient depletion
  +-- Climate (drought, temperature increase): reduced growing season;
      longer water stress periods; reduced cover

  FEEDBACK LOOPS:
  Bare soil --> more surface heating --> less cloud formation --> less rain
  --> more bare soil (climate feedback)
  Bare soil --> erosion --> loss of silt/clay (texture coarsen) --> less water retention
  --> less vegetation --> more erosion (soil degradation feedback)

  INDICATOR SPECIES:
  Increasing: annual grasses, forbs, shrubs (native and invasive)
  Decreasing: perennial grasses, multi-layer vegetation structure
```

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| Which USLE factor has the most management leverage? | C (cover-management factor); no-till reduces A by 5–10× vs. conventional corn |
| What soil texture is most vulnerable to water erosion? | Silt loam (high K factor; seals easily; detaches readily) |
| What is the primary mechanism of secondary salinization? | Irrigation water evapotranspires; salts left behind; groundwater rise concentrates salts at surface |
| At what ECe does corn yield start to decline? | > 1.7 dS/m (most sensitive major crop); barley tolerates to 8 dS/m |
| What is a plowpan and how does it form? | Dense layer at tillage depth (15–25 cm) from repeated plow sole pressure; BD 1.7–1.9 g/cm³ |
| Why is subsoil compaction from modern combines so difficult to fix? | Axle loads 15–18 t; compaction penetrates to 40–60 cm; only 5–15 years of biological activity partially reverses it |
| What are the two feedbacks that accelerate desertification? | Climate feedback (bare soil → less rain) + soil degradation feedback (erosion → coarser texture → less water retention) |

---

## Common Confusion Points

**USLE predicts average annual soil loss, not event-level erosion.**
A single intense storm can move more soil than the entire USLE-predicted annual average. The equation is calibrated for planning at the field scale over many years — it is not a storm event model. Peak storm erosion requires modified event-based approaches.

**Soil erosion and sediment delivery are different.**
Not all eroded soil reaches a stream. Deposition occurs on footslopes, in buffer strips, and in channels. Sediment delivery ratio (SDR) is typically 0.1–0.5 (10–50% of eroded soil reaches watercourse). The environmental impact depends on what is delivered, not what is eroded.

**Salinity reclamation requires both leaching AND drainage.**
You cannot reduce salt content in a saline soil without both: (1) adding large amounts of freshwater to leach salts downward, AND (2) drainage to remove the salt-laden water. Leaching without drainage only raises the saline water table. In low-lying irrigated areas without tile drainage, desalinization is essentially impossible.

**Not all bulk density increases indicate compaction.**
Bulk density varies naturally with texture (clay soils have lower BD than sands), depth (BD usually increases with depth), and moisture. A silt loam with BD = 1.4 g/cm³ might be acceptable; a sandy loam at 1.4 g/cm³ is fine. The problem is BD exceeding the species-specific critical thresholds for root penetration.
