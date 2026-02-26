# Ecosystem Energetics — Energy Flow, Trophic Efficiency, GPP/NPP

## The Big Picture

<!-- @editor[bridge/P2]: Energy flow through trophic levels is directly analogous to entropy increase in irreversible processes; MIT physics/math background makes this a natural anchor -->
Ecosystems are open thermodynamic systems: energy flows in (solar radiation or chemosynthesis), is transformed and degraded at each biological step, and exits as heat. Unlike nutrients (which cycle), energy flows in one direction — it cannot be recycled. This asymmetry between energy flow and nutrient cycling is the central organizing principle of ecosystem ecology.

```
+------------------------------------------------------------------+
|              ECOSYSTEM ENERGY BUDGET                              |
|                                                                   |
|  SOLAR INPUT (~340 W/m² global average)                          |
|       |                                                           |
|       | ~1-3% captured by photosynthesis (terrestrial)          |
|       v                                                           |
|  GROSS PRIMARY PRODUCTION (GPP)                                  |
|       |                                                           |
|       | Plant respiration (~50% of GPP)                          |
|       v                                                           |
|  NET PRIMARY PRODUCTION (NPP) = available to consumers           |
|       |                                                           |
|       | Herbivory (~10% eaten in terrestrial; ~30-70% aquatic)  |
|       v                                                           |
|  HERBIVORE BIOMASS → CARNIVORE → TOP PREDATOR                   |
|       (each trophic transfer: ~10% efficiency, Lindeman)         |
|                                                                   |
|  DETRITAL PATHWAY: ~90% of NPP not eaten → dead organic matter   |
|  Decomposers (bacteria/fungi) process → CO₂ + nutrients          |
+------------------------------------------------------------------+
```

---

## Primary Production — Capturing Solar Energy

### Gross vs Net Primary Production

```
GPP (Gross Primary Production):
  Total rate of photosynthesis by autotrophs
  = Carbon fixed from CO₂ into organic molecules per unit time

Ra (Autotrophic Respiration):
  Plant respiration to maintain its own metabolism

NPP (Net Primary Production):
  NPP = GPP - Ra
  = Energy actually available to consumers (herbivores, detritivores)
  ≈ 50% of GPP (rough global average; varies widely)
```

**Units:** gC/m²/yr (grams carbon per square meter per year) or J/m²/yr

### Global NPP Patterns

```
ECOSYSTEM           NPP (gC/m²/yr)    AREA (10⁶ km²)  TOTAL (PgC/yr)
------------------  ----------------  ---------------  ---------------
Tropical rainforest ~1000–2000        17.0             ~17
Tropical seasonal   ~600–800          7.5              ~5
Temperate forest    ~400–700          10.4             ~5
Boreal forest       ~200–400          13.7             ~3
Temperate grassland ~150–300          8.9              ~2
Desert/semidesert   ~5–75             18.0             ~1
Tundra              ~50–100           9.5              <1
Total terrestrial                                      ~55–60 PgC/yr

Open ocean          ~100–150          332              ~40
Continental shelf   ~200–400          27               ~5
Algal beds/reef     ~500–1000         0.6              <1
Total marine                                           ~45–50 PgC/yr

GLOBAL TOTAL: ~100–110 PgC/yr (1 PgC = 10¹⁵ g carbon)
```

**Controls on NPP:**
- **Terrestrial:** Water availability (dominant globally) + temperature + nutrients (N, P most limiting)
- **Aquatic:** Light + nutrients (N, P, Fe in open ocean)
- **Polar:** Temperature + light seasonality

---

## Lindeman Trophic Efficiency — The 10% Rule

Raymond Lindeman (1942) analyzed energy transfer through a Minnesota lake food chain and found ~10% efficiency at each trophic level:

```
TROPHIC ENERGY BUDGET:

ENERGY AT TROPHIC LEVEL:  100 units

 ↓ Ingested by next level: 10 units

FATE OF 100 UNITS AT ONE TROPHIC LEVEL:
  Not eaten (falls to detritus): 50–80 units
  Eaten but not assimilated: 10–30 units (feces)
  Assimilated but respired: 5–20 units
  → GROWTH (available to next level): ~10 units

LINDEMAN EFFICIENCY = Production(n+1) / Production(n) ≈ 0.10
```

**The 10% rule is a rough average** — actual efficiencies range from ~5% to ~20%:
- Endotherms (birds, mammals): lower (~5–10%) — high metabolic cost of body temperature
- Ectotherms (fish, invertebrates): higher (~10–25%) — less energy on thermoregulation
- Aquatic ecosystems: generally higher than terrestrial

**Practical implication — human food:**
```
PROTEIN CALORIES IN FOOD CHAIN:
  1 million kcal of plant → 100,000 kcal of beef (10% efficiency)
  1 million kcal of plant → 10,000 kcal of predatory fish

  IMPLICATION: Meat production is energetically costly.
  A diet with trophic level 2.5 uses ~10× more primary production
  than a plant-based diet (trophic level 2.0)
```

---

## Ecological Efficiency Terminology

Multiple efficiency terms used in the literature:

```
ASSIMILATION EFFICIENCY = Assimilated / Ingested
  (how much of what's eaten is absorbed; feces are the remainder)
  Herbivores: 20–60% (plant cell walls hard to digest)
  Carnivores: 60–90% (prey tissue easily digested)

NET PRODUCTION EFFICIENCY = Production / Assimilation
  (how much assimilated energy goes to growth vs respiration)
  Ectotherms: ~20–40%
  Endotherms: ~1–5% (most energy → thermoregulation)

TROPHIC LEVEL TRANSFER EFFICIENCY = Production(n+1) / Production(n)
  = Assimilation × Net production efficiency
  ≈ 10% typical
```

---

## Ecological Pyramids

Three types, representing different aspects of food web structure:

### Pyramid of Energy (Always Pyramid-Shaped)

```
ENERGY (J/m²/yr):
          Top carnivore:    10
         Carnivore:       100
       Herbivore:        1,000
    Producers:         10,000

Always pyramid-shaped — 2nd law of thermodynamics: energy can only decrease.
```

### Pyramid of Biomass

```
BIOMASS (g/m²):
  Usually pyramidal (terrestrial):
  P > H > C (producers dominate)

  BUT can be INVERTED (aquatic):
          Zooplankton: 21 g/m²
     Phytoplankton: 4 g/m²  (inverted!)

  Why? Phytoplankton turn over very rapidly (~1 day doubling time)
  Despite low standing biomass, they produce a lot per unit time.
  Biomass = instantaneous snapshot; production = rate.
```

### Pyramid of Numbers

Can be any shape:
- Normal: pasture (many plants → fewer insects → fewer birds)
- Inverted: single oak tree supporting millions of insects

---

## Secondary Production and Detrital Food Web

Most terrestrial NPP (~90%) is NOT consumed by herbivores while alive. It enters the **detrital food web** as dead organic matter:

```
DETRITAL PATHWAY:

Dead plant material → Physical fragmentation (weathering, invertebrates)
                    → Microbial decomposers (bacteria, fungi)
                    → Mineralizes nutrients → available for plants

DECOMPOSITION RATE controlled by:
  Temperature: Q₁₀ ≈ 2–3 (rate doubles per 10°C)
  Moisture: waterlogged soils → anaerobic → slow
  C:N ratio: high C:N (wood, straw) → slow; low C:N (leaves, dung) → fast
  Lignin content: lignin extremely resistant to decomposition

DECOMPOSITION INDEX: k = ln(M₀/Mₜ)/t
  k high → fast decomposition (tropical: k ≈ 1–2/yr; leaf litter gone in months)
  k low → slow (boreal forest floor: k ≈ 0.05–0.1/yr; litter accumulates)
```

**Soil organic matter (SOM)** = accumulated partially-decomposed organic material. Represents ~3× as much carbon as the atmosphere. Changes in SOM decomposition rates due to warming → positive feedback to climate change.

---

## Net Ecosystem Production (NEP) and Carbon Balance

```
GPP = total photosynthesis (CO₂ fixed)
Ra  = autotroph respiration (CO₂ released)
NPP = GPP - Ra  (net plant production)
Rh  = heterotroph respiration (decomposers + consumers)
NEP = NPP - Rh  = net ecosystem carbon balance

NEP > 0: ecosystem is a CARBON SINK (accumulating C)
NEP < 0: ecosystem is a CARBON SOURCE (releasing C)
NEP ≈ 0: steady state (mature forests, old-growth)

NBP (Net Biome Production) = NEP ± disturbance fluxes (fire, harvest, etc.)
```

**Amazon: source or sink?** — The Amazon basin has long been a carbon sink. With deforestation + droughts, some areas are now net sources. The 2021 study found eastern Amazon a net CO₂ emitter for the first time due to deforestation + drought stress.

---

## Decision Cheat Sheet

| Ecological question | Key concept |
|--------------------|-------------|
| How much energy available at level 3? | NPP × 10% × 10% = 1% of NPP |
<!-- @editor[content/P1]: Claim may be incorrect -- verify: "Cattle: ectotherm" -- cattle are endotherms (mammals); factual error in parenthetical -->
| Why is beef more resource-intensive than chicken? | Cattle: ectotherm → lower trophic efficiency; also cattle are trophic level 2 in grasslands |
| Why do tropical forests have high NPP? | Warm + wet = high photosynthetic rate year-round |
| Why is lake phytoplankton biomass lower than zooplankton? | High turnover rate; biomass ≠ production |
| Which pathway processes most terrestrial NPP? | Detrital; ~90% of NPP enters via dead organic matter |
| Is old-growth forest a carbon sink? | Generally NEP ≈ 0; carbon inputs ≈ outputs |

---

## Common Confusion Points

**Production vs standing biomass** — A crop of fast-growing algae can have low standing biomass but high production. A tropical forest has huge standing biomass but moderate NPP per unit area. The pyramid of biomass and pyramid of energy can look very different.

**The 10% rule applies to production, not biomass** — The 10% refers to the fraction of *production* at one level that is converted to *production* at the next level. Not 10% of bodies eaten = 10% of predator bodies.

**Respiration ≠ bad** — Plant respiration is ~50% of GPP but is necessary for maintaining plant structure, growth, and reproduction. The comparison is often made that "plants respire a lot" but this is just normal metabolism, not waste.

**NPP per unit area: tropical rainforest vs open ocean** — Tropical forests have ~10× higher NPP/m² than open ocean. But the ocean is ~71% of Earth's surface, so marine total NPP ≈ terrestrial total NPP globally.