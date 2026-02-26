# Soils and Fertility — Texture, CEC, NPK, pH, Organic Matter

## The Big Picture

Soil is the living foundation of agriculture — not just dirt but a complex system integrating mineral weathering, organic decomposition, microbial metabolism, and plant-root interactions. Managing fertility means managing all of these simultaneously. The lesson learned from industrial agriculture: treating soil as an inert substrate to add chemicals to eventually degrades the system; treating it as a living ecosystem sustains productivity.

```
+---------------------------------------------------------------+
|                    SOIL SYSTEM OVERVIEW                        |
|                                                                |
|  MINERAL FRACTION          ORGANIC FRACTION                   |
|  (45-55% by volume)        (1-6% by volume)                   |
|  Sand/silt/clay            Humus, root debris                 |
|  (texture, structure)      (fertility, water retention)       |
|                                                                |
|  PORE SPACE                BIOLOGICAL FRACTION                |
|  (25-50% by volume)        (~0.1% by volume but critical)     |
|  Air + water               Bacteria, fungi, earthworms,       |
|  (drainage, aeration,      nematodes, arthropods              |
|   root penetration)        (nutrient cycling, structure)      |
|                                                                |
|  KEY OUTPUTS: Plant-available water, nutrients, physical      |
|               support, temperature buffering                   |
+---------------------------------------------------------------+
```

---
## Engineering Bridges

```
SOIL CONCEPT                  SYSTEMS / ENGINEERING EQUIVALENT
──────────────────────────────────────────────────────────────────────────────
CEC (Cation Exchange Capacity) Buffered charge reservoir (capacitor)
  Clay and humus have negative  → surface charge acts like a capacitor plate;
  surface charge → hold cations   holds ions against leaching by electrostatic
  CEC = total buffering capacity → capacitance (C = Q/V)
  High CEC (heavy clay, SOM-rich)→ large capacitor; nutrients resist leaching
  Low CEC (sandy)               → small capacitor; nutrients flush immediately
  Nutrient leaching             → capacitor discharge; rate governed by flux
  Fertilizer addition           → charging the capacitor

Soil pH as state variable       System state governing subsystem behavior
  pH controls: nutrient availability, microbial activity, mineral solubility
  Optimal pH 6.0–7.0 (most crops) → operating point of the system
  pH < 5.5: Al³⁺ and Mn²⁺ become soluble → toxic to roots (fail state)
  pH > 7.5: P, Fe, Zn, Mn become insoluble → deficiency (different fail state)
  Liming (CaCO₃): adjusts pH toward target → same as setpoint correction in PID
  pH as state variable: once set, governs which processes are possible

Soil nutrient cycling           Coupled ODE system with multiple compartments
  N cycle: NH₄⁺ ↔ NO₃⁻ ↔ N₂    → nitrification rate, denitrification rate,
    plant uptake, leaching         mineralization rate → k_ij in compartment model
  P cycle: mineral P → solution P → plant uptake → organic P → mineral
    → phosphorus is tightly cycled (no gas phase); behavior like closed loop

Soil water retention curve      Nonlinear transfer function
  θ(ψ): volumetric water content → pressure head (matric potential)
  High ψ (moist): small ψ change → large θ change (high storage capacity)
  Low ψ (dry): large ψ change → small θ change (less responsive)
  "Field capacity" and "wilting  → threshold operating points separating
    point"                          favorable, stressed, and failed regimes

Soil organic matter (SOM)       Integrator with drift
  dSOM/dt = C_input - k·SOM     → first-order model; steady state = C_in/k
  Tillage increases k (oxidation)→ parameter shift; new (lower) equilibrium
  Cover crops / no-till          → increase C_in; shift equilibrium upward
  Multi-century timescale        → very slow integrator; actions today visible
                                    in soil state decades later (long delay)
```

## Soil Texture — Physical Framework

Texture = relative proportions of sand, silt, clay particles:

```
PARTICLE SIZE CLASSIFICATION (USDA):
  Sand:    0.05–2.0 mm    (visible; gritty feel)
  Silt:    0.002–0.05 mm  (smooth, floury; visible in microscope)
  Clay:    <0.002 mm      (colloidal; sticky when wet)

SOIL TEXTURE TRIANGLE:
         100% Clay
           /\
          /  \
    Clay / C  \
        /------\
  SiCl / SCl  SiL\
      /  CL  SL   \
  Silt/Si L    S   \Sand
     100% Silt  100% Sand

Key textures:
  Sandy loam: high sand, easy drainage, low fertility
  Loam: balanced (best for most crops)
  Clay loam: fine-grained, high fertility, drainage risk
  Heavy clay: compaction, waterlogging issues
```

**Soil structure vs texture** — Texture is fixed (particle sizes). Structure is how particles aggregate into clumps (aggregates, peds). Good structure improves aeration, drainage, and root penetration. Tillage destroys structure; organic matter builds it.

**Field capacity and wilting point:**
- Field capacity: maximum water held against gravity (drainage complete)
- Wilting point: minimum water at which plants can extract moisture
- Plant-available water (PAW) = Field capacity - Wilting point
- Loam PAW: ~15-20% by volume; Sandy soils: 5-10%; Clay: 15-25% (but slow release)

---

## Cation Exchange Capacity (CEC)

CEC = soil's ability to hold positively charged plant-available nutrients:

```
MECHANISM:
  Clay minerals and organic matter carry negative surface charges
  These bind positively charged cations (Ca²⁺, Mg²⁺, K⁺, Na⁺, H⁺, Al³⁺)
  Cations are held reversibly (can be exchanged by other cations + plant roots)

  CLAY PLATELET (negative surface):
  ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─
  Ca²⁺  Mg²⁺  K⁺   Ca²⁺  NH₄⁺  H⁺
  (loosely held; exchangeable)

CEC MEASURED IN: cmol(+)/kg or meq/100g
  Sandy soils:    ~2-10 (low CEC; leach easily)
  Clay soils:     ~20-60 (high CEC; hold nutrients well)
  Organic matter: ~100-300 (very high CEC; why adding OM improves fertility)

BASE SATURATION:
  % of CEC occupied by base cations (Ca, Mg, K, Na) vs H + Al
  High base saturation (>80%) = fertile soil
  Low base saturation = acidic, often leached
```

---

## NPK Macronutrients — The Big Three

### Nitrogen (N)

```
FUNCTION: Protein synthesis (amino acids), chlorophyll, enzymes
FORM TAKEN UP: NO₃⁻ (nitrate) and NH₄⁺ (ammonium)
DEFICIENCY SYMPTOM: Yellowing (chlorosis), starting with old leaves
                    (N is mobile; moves from old to new growth)

SOIL N DYNAMICS:
  Organic N (protein, humus) → Mineralization → NH₄⁺
                                                    ↓ Nitrification
                               NO₃⁻  ←──────────────
                                 |
                         Plant uptake
                         OR
                         Denitrification → N₂ (lost)
                         OR
                         Leaching (NO₃⁻ is mobile; washed below root zone)

N MANAGEMENT:
  Apply close to uptake time (split applications)
  Nitrification inhibitors slow nitrification → keep N as NH₄⁺ longer
  Cover crops capture residual N (prevents winter leaching)
```

### Phosphorus (P)

```
FUNCTION: Energy transfer (ATP), DNA/RNA, root development, seed formation
FORM TAKEN UP: H₂PO₄⁻ and HPO₄²⁻
DEFICIENCY SYMPTOM: Purple tinge on leaves (especially corn seedlings)

P CHEMISTRY:
  P is very immobile in soil (unlike N)
  Binds strongly to Fe and Al oxides at low pH
  Binds to Ca at high pH
  → P availability is pH-dependent (peak availability pH 6-7)

MYCORRHIZAL NETWORKS: Critical for P uptake
  Arbuscular mycorrhizal fungi (AMF) extend root reach dramatically
  Plants provide C to fungi; fungi access P in pores too small for roots
  40-80% of plant P can come via mycorrhizae

P MINING vs CYCLING:
  Soil P test: Olsen method (NaHCO₃ extraction) or Mehlich-3
  Build-up P: years of excess application → "legacy P" that leaches
  Legacy P drives eutrophication for decades after input stops
```

### Potassium (K)

```
FUNCTION: Stomatal regulation, protein synthesis, disease resistance,
          water balance, enzyme activation
FORM TAKEN UP: K⁺
DEFICIENCY: Scorched leaf edges (marginal chlorosis/necrosis)
            Tip burn on leafy vegetables

K IN SOIL:
  Held by clay mineral interlayers (slowly available) + exchangeable K
  K is generally well-supplied in non-leached soils
  Sandy/tropical soils leach K → may need supplementation
  Luxury consumption: crops take up more than needed (K saturation)
```

---

## Secondary Macronutrients and Micronutrients

| Nutrient | Function | Deficiency Symptom | Common Issue |
|---------|---------|-------------------|-------------|
| Ca | Cell wall strength, signaling | Blossom end rot (tomato) | Acidic/leached soils |
| Mg | Chlorophyll (center atom), enzyme | Interveinal chlorosis | Sandy, acidic soils |
| S | Protein (cysteine, methionine) | Yellowing, young leaves | After SO₂ reductions |
| Fe | Chlorophyll synthesis, electron transport | Interveinal chlorosis, young leaves | High pH soils (calcareous) |
| Mn | Photosynthesis, enzyme | Similar to Fe; swamp disease in cereals | High pH, waterlogged |
| Zn | Enzyme activation, hormone | Stunted growth, small leaves | Calcareous/high pH soils |
| B | Cell wall, pollen germination | Die-back, hollow stem | Sandy, leached soils |
| Mo | Nitrate reduction enzyme | Needed in tiny amounts; pH-sensitive | Acid soils |
| Cl | Osmotic regulation | Wilting, chlorosis | Rarely deficient |

---

## Soil pH — Master Variable

Soil pH controls nutrient availability, microbial activity, and plant health:

```
pH 4.0  4.5  5.0  5.5  6.0  6.5  7.0  7.5  8.0  8.5
  |     |    |    |    |    |    |    |    |    |
  ACIDIC           NEUTRAL           ALKALINE

NUTRIENT AVAILABILITY BY pH:
  N: best 6.0–8.0 (nitrification rate)
  P: best 6.0–7.0 (neither Al-P nor Ca-P fixation)
  K,S,Ca,Mg: best 6.0–8.5 (generally available)
  Fe,Mn,Zn,Cu: available in acid; precipitate in alkaline
  Mo,B: available in neutral-alkaline; unavailable in acid
  Al, Mn: TOXIC in acid (pH <5.0–5.5)

OPTIMAL pH FOR MOST CROPS: 6.0–7.0
  (some exceptions: blueberries: 4.5–5.5; alfalfa: 6.5–7.5)

ADJUSTING pH:
  Too acid: Apply lime (CaCO₃, Ca(OH)₂ = agricultural lime)
  Too alkaline: Apply sulfur (S → H₂SO₄ by bacteria)
               or acidifying fertilizers (ammonium sulfate)
```

---

## Soil Organic Matter (SOM) — The Foundation of Fertility

SOM = accumulation of partially decomposed plant/animal/microbial material:

```
SOM BENEFITS:
  Nutrient cycling: Mineralization releases N, P, S, micronutrients
  CEC: High CEC per unit mass (100-300 cmol+/kg vs clay 20-60)
  Water retention: Each 1% OM increase → ~0.01 m³/m³ more water held
  Structure: Aggregation by fungal hyphae + polysaccharides
  Buffering: Resists pH change
  Biology: Energy source for soil microbiome

SOM CONSISTS OF:
  Active fraction (~10%): Labile; fast turnover (days to months)
                          Immediately available nutrients
  Slow fraction (~40–60%): Moderate turnover (years to decades)
  Passive fraction (~30–50%): Stabilized (charcoal, mineral-bound);
                               slow turnover (centuries to millennia)
                               = the "carbon sink" component

BUILDING SOM:
  Cover crops + crop residue retention
  Composting
  Reduced tillage / no-till (tillage breaks up aggregates → accelerates decomposition)
  Perennial crops (continuous root turnover)

LOSING SOM:
  Tillage: 20–50% of SOM loss in first decades of cultivation
  Erosion: removes topsoil with highest OM concentration
  Continuous fallow + bare soil (no input; only decomposition)
```

**Soil carbon as climate lever:** Converting degraded/tilled soils to no-till or agroforestry can sequester 0.5–1 t C/ha/yr. If applied globally to the ~2 billion ha of degraded agricultural soils, could offset ~1–2 Gt CO₂/yr (~2–5% of current anthropogenic emissions).

---

## Decision Cheat Sheet

| Soil situation | Management action |
|---------------|------------------|
| Compacted, poor drainage, heavy machinery | Reduce tillage; increase OM; improve drainage; subsoiling if needed |
| Low CEC (sandy soil); nutrients leach | Increase OM; apply smaller more frequent applications |
| pH < 5.5; stunted crops | Apply agricultural lime; test for Al toxicity |
| pH > 7.5; Fe or Mn chlorosis | Apply chelated micronutrients; ammonium fertilizers; sulfur |
| Yellow old leaves; N deficiency | Sidedress with N; split applications |
| Purple leaves (corn); P deficiency | Check pH first (P unavailable at low pH); apply P if pH OK |
| Low SOM; declining yields | Cover crops, compost, no-till; SOM takes 5–20 years to build |

---

## Common Confusion Points

**Soil test results ≠ direct N application rate** — Standard soil tests don't accurately measure plant-available N (too dynamic). N recommendations come from yield-based calculations, leaf tissue tests, and presidedress N tests (PSNT). P and K tests are more reliable for calibrated recommendations.

**Organic matter ≠ always high with organic farming** — Organic farming prohibits synthetic fertilizers but doesn't automatically build SOM. Key factor is tillage frequency and organic inputs (compost, manure). No-till conventional farming may have higher SOM than organic farming with intensive tillage.

**"Nutrient-rich soil" ≠ productive soil** — A high-clay tropical Oxisol may have abundant nutrients chemically present but most are tightly bound to Fe/Al oxides — unavailable to plants. Available nutrient pool ≠ total nutrient pool.

**CEC ≠ plant food on demand** — CEC holds nutrients against leaching, but availability still depends on pH, soil moisture, and biological activity. A high-CEC soil can still be deficient in specific nutrients if pH is wrong or competition (Al³⁺) fills exchange sites.
