# Ocean Chemistry — Seawater Composition, Carbonate System, Ocean Acidification, Oxygen Minimum Zones

## The Big Picture

```
+===========================================================================+
|                  SEAWATER CHEMICAL STRUCTURE                               |
+===========================================================================+
|                                                                           |
|  MAJOR IONS (> 1 mmol/kg)     CONSERVATIVE TRACERS                       |
|  ─────────────────────────    ────────────────────                        |
|  Cl⁻     548 mmol/kg  19.4 g/kg   Salinity, Na⁺, Cl⁻ ratios              |
|  Na⁺     470 mmol/kg  10.8 g/kg   constant relative to each other        |
|  SO₄²⁻   28 mmol/kg   2.65 g/kg   → diagnostic of water mass mixing       |
|  Mg²⁺    53 mmol/kg   1.27 g/kg                                           |
|  Ca²⁺    10 mmol/kg   0.41 g/kg   NON-CONSERVATIVE (consumed/produced)    |
|  K⁺      10 mmol/kg   0.38 g/kg   ─────────────────────────────────────   |
|  HCO₃⁻    2.3 mmol/kg 0.14 g/kg   O₂, CO₂, nutrients (NO₃,PO₄,Si)       |
|  Br⁻     0.84 mmol/kg 0.07 g/kg   → vary with biological activity        |
|                                                                           |
|  RESIDENCE TIMES (ocean water mass exchange):                             |
|  Cl⁻ > 10⁸ yr   SO₄²⁻ ~10⁷ yr   Na⁺ ~7×10⁷ yr   Ca²⁺ ~10⁶ yr           |
|  (long residence = conservative; short = reactive)                        |
+===========================================================================+
```

---

## Conservative vs. Non-Conservative Ions

```
RULE OF CONSTANT PROPORTIONS (Forchhammer, 1865):
  Major ions maintain constant proportions relative to chlorinity
  regardless of total salinity.
  → Na⁺/Cl⁻ ≈ 0.858 everywhere in open ocean
  → Mg²⁺/SO₄²⁻ ratio constant

  WHY: Residence times >> ocean mixing timescale (~1000 yr)
  So any regional input is diluted/mixed globally before significant change

  VIOLATIONS OF CONSTANT PROPORTIONS:
    Hydrothermal vents: remove Mg²⁺, SO₄²⁻ from seawater
    Anoxic basins (Black Sea): SO₄²⁻ depleted by sulfate reduction
    Evaporite formation: Ca²⁺, SO₄²⁻ removed
    River input: different composition from seawater
    These are real but small perturbations in the open ocean

MAJOR ION RESIDENCE TIMES:
  Cl⁻:   230 million yr     (hardly ever removed — conservative)
  Na⁺:   83 million yr
  Mg²⁺:  13 million yr      (removed by hydrothermal vents)
  SO₄²⁻: 11 million yr      (removed by diagenesis, some hydrothermal)
  Ca²⁺:  1.1 million yr     (removed by CaCO₃ precipitation, biologically)
  K⁺:    12 million yr
  HCO₃⁻: ~100,000 yr       (reactive via carbonate system)
```

---

## The Carbonate System — Seawater Buffer Chemistry

The carbonate system is the most consequential equilibrium chemistry in the ocean. It controls pH, CaCO₃ solubility, and the ocean's capacity to absorb atmospheric CO₂.

### Equilibria

```
CO₂ SYSTEM IN SEAWATER:

  CO₂(atm) ⇌ CO₂(aq)                    KH = Henry's constant
  CO₂(aq) + H₂O ⇌ H₂CO₃                K0
  H₂CO₃ ⇌ H⁺ + HCO₃⁻                   pK1 ≈ 6.0 at 25°C, 35 PSU
  HCO₃⁻ ⇌ H⁺ + CO₃²⁻                   pK2 ≈ 9.1 at 25°C, 35 PSU

  Together: CO₂(aq) + H₂O ⇌ H⁺ + HCO₃⁻ (dominant at ocean pH)

THE FOUR VARIABLES — know any two, calculate all others:
  DIC  = dissolved inorganic carbon = [CO₂] + [HCO₃⁻] + [CO₃²⁻]   ~2100 μmol/kg
  TA   = total alkalinity ≈ [HCO₃⁻] + 2[CO₃²⁻] + [B(OH)₄⁻] + ...  ~2350 μeq/kg
  pH   = −log[H⁺]                                                    8.1–8.3
  pCO₂ = partial pressure of CO₂                                     ~410 μatm (2024)

OCEAN SURFACE pH: ~8.1 (slightly alkaline, dominated by HCO₃⁻ at this pH)
  DIC speciation at pH 8.1:
    CO₂(aq): ~1% of DIC
    HCO₃⁻: ~91% of DIC  ← dominant species
    CO₃²⁻: ~8% of DIC
```

### Buffering — The Revelle Factor

```
BJERRUM PLOT (species fractions vs. pH):
  pH < 6:   CO₂(aq) dominant
  pH 6–9:   HCO₃⁻ dominant   ← seawater range
  pH > 9:   CO₃²⁻ dominant

REVELLE FACTOR (buffer factor):
  Revelle factor R = (ΔpCO₂/pCO₂) / (ΔDIC/DIC)

  R ≈ 9–15 depending on temperature and current DIC/TA state
  HIGH R (warm water, high pCO₂) → less efficient CO₂ buffer
  LOW R (cold water, high CO₃²⁻) → more efficient CO₂ buffer

  R ≈ 10 means: to increase DIC by 1%, pCO₂ must increase 10%
  → Ocean is a LESS efficient CO₂ buffer than you might expect from total DIC

  CONSEQUENCE:
    As we add CO₂, R increases (less CO₃²⁻ available)
    → Future ocean less efficient at absorbing CO₂
    → Carbon cycle feedback: atmospheric CO₂ increases faster as R increases

ALKALINITY CONTROLS:
  Alkalinity dominated by carbonate/bicarbonate, borate
  Biological CaCO₃ PRECIPITATION removes TA:
    Ca²⁺ + 2HCO₃⁻ → CaCO₃ + CO₂ + H₂O  (decreases TA and DIC)
    Net effect: raises pCO₂ in surface water slightly (counterintuitive)
  CaCO₃ DISSOLUTION increases TA → better pH buffering
```

---

## Ocean Acidification

```
ANTHROPOGENIC CO₂ → OCEAN ACIDIFICATION:

  Since preindustrial (~1750):
    Atmospheric CO₂: 280 → 420 ppm (2024) (+50%)
    Ocean surface pCO₂: ~280 → ~415 μatm
    Ocean surface pH: ~8.18 → ~8.08 (−0.10 pH units, ongoing)
    [H⁺] increased ~26% (because pH is logarithmic)
    [CO₃²⁻] decreased ~25–30% since preindustrial

  RCP 8.5 projection (high emissions):
    2100: pH → ~7.75 (total drop ~0.4 units)
    [CO₃²⁻] → ~50% of preindustrial
    Aragonite saturation Ω → <1 in Arctic/Antarctic by 2050s

SATURATION STATE:
  Ω_calcite = [Ca²⁺][CO₃²⁻] / K'sp
  Ω > 1: supersaturated → CaCO₃ stable (organisms can precipitate shells)
  Ω = 1: saturation horizon
  Ω < 1: undersaturated → CaCO₃ dissolves

  Modern surface: Ω_calcite ≈ 5–6 (tropics), ~2 (Arctic)
  Modern surface: Ω_aragonite ≈ 3–4 (tropics), ~1–1.5 (Arctic)
  Aragonite more soluble than calcite:
    Many corals, pteropods build aragonite → more vulnerable

BIOLOGICAL IMPACTS:
  Calcifiers under stress when Ω < ~2 (not just when Ω < 1):
    Pteropods: shells dissolve rapidly when Ω_aragonite < 1
    Oyster larvae: massive die-offs in Pacific Northwest hatcheries (2007–2008)
    Cold-water corals: lose skeleton formation ability, already in undersaturated water
    Tropical coral reefs: combined stress of warming + acidification
    Benefit?: some organisms grow faster in mildly elevated CO₂ (CO₂ fertilization,
    seagrasses, some macroalgae, coccolithophores — but offset by other stressors)
```

---

## Nutrient Cycles

```
REDFIELD RATIO:
  In bulk phytoplankton biomass:
    C : N : P = 106 : 16 : 1 (by atoms) — Redfield (1934)

  Oceanic dissolved nutrient ratio ~ Redfield:
    → Biological uptake and remineralization maintain it globally
    → Suggests C, N, P cycling are coupled by biology

  MODERN REFINEMENT: "Extended Redfield":
    (CH₂O)₁₀₆(NH₃)₁₆(H₃PO₄)(H₄SiO₄)₁₅ including silica for diatoms
    C:N:P:Si = 106:16:1:15 (for siliceous phytoplankton)

MACRO NUTRIENTS:
  NO₃⁻ (nitrate): limiting nutrient in most of ocean
    Surface: depleted (< 1 μM) in subtropical gyres
    Deep: ~30–45 μM in North Atlantic deep water, ~43 μM in deep Pacific
    Remineralization: organic N → NH₄⁺ → NO₂⁻ → NO₃⁻ (nitrification)

  PO₄³⁻ (phosphate): rarely limiting in open ocean; limiting in some lakes
    Deep ocean: ~2.5 μM (Atlantic) to ~3.5 μM (Pacific)
    No gaseous phase → harder to fix new phosphorus

  Si(OH)₄ (silicic acid): limiting for diatoms/radiolaria/sponges
    Deep ocean: varies widely (5–180 μM)
    Much higher in deep Pacific/Southern Ocean

MICRO NUTRIENTS:
  Fe (iron): LIMITING nutrient in Southern Ocean, equatorial Pacific, N. Pacific
    (HNLC regions: High Nutrient, Low Chlorophyll)
    Surface: <1 nM, often <0.1 nM
    Sources: atmospheric dust, sediment diffusion, hydrothermal vents, glacial meltwater
    Iron fertilization experiments (IRONEX, SOIREE): confirmed iron limitation
    Southern Ocean iron limit reduces efficiency of biological carbon pump globally
```

---

## The Biological Pump

```
BIOLOGICAL CARBON PUMP:

  Surface:  CO₂ fixation by phytoplankton → organic particles
  Sinking:  ~20% of surface production sinks below thermocline
            ~5–10% reaches seafloor
  Deep:     Remineralization releases CO₂ to deep water
  Burial:   <0.5% of surface production buried in sediment (permanent removal)

  EXPORT PRODUCTION: ~10 GtC/yr sink below 100 m globally
  BURIAL: ~0.1 GtC/yr buried in sediment

  PUMP EFFICIENCY CONTROLS:
    Bloom formation: large cells, aggregates → fast sinking (>100 m/day)
    Grazing: mesozooplankton fecal pellets = efficient sink vector
    Ballast: dense mineral particles (CaCO₃, SiO₂) accelerate sinking
    Microbial loop: small cells reprocessed in surface → don't sink (leak back)

BIOLOGICAL PUMP + CARBONATE PUMP:
  Soft tissue pump: organic C sinking → deep DIC increase (reduces alkalinity near surface)
  Carbonate pump: CaCO₃ shells sinking → transfers alkalinity to deep
    Net surface effect: raises pCO₂ slightly
    Deep effect: CaCO₃ dissolution restores alkalinity
  The two pumps work in opposition for pH and pCO₂ but together for deep DIC
```

---

## Oxygen Minimum Zones (OMZ)

```
OMZ FORMATION:

  Respiration of sinking organic matter consumes O₂ at mid-depth (200–1000 m)
  Slow ventilation (sluggish circulation, far from O₂ source) → O₂ not replenished
  Threshold: O₂ < 20 μmol/kg → aerobic fauna excluded
  Extreme OMZ: O₂ < 1 μmol/kg → euxinic conditions

  LOCATION OF MAJOR OMZs:
    Eastern Pacific (California, Peru upwelling zones): most intense global OMZs
    Arabian Sea and Bay of Bengal (Indian Ocean): large OMZs
    Eastern Atlantic: moderate
    Deep Black Sea: permanently anoxic below 200 m (classic example)

  DENITRIFICATION IN OMZ:
    When O₂ → 0: bacteria use NO₃⁻ as terminal electron acceptor
    NO₃⁻ → NO₂⁻ → N₂O → N₂ (nitrogen gas)
    → PERMANENT REMOVAL of fixed nitrogen from ocean
    → N₂O (potent greenhouse gas) released to atmosphere from OMZ boundaries
    OMZ denitrification ~ 60% of global marine N loss

CLIMATE AND OMZ EXPANSION:
  Warming → less O₂ solubility → lower baseline O₂
  Increased stratification → less ventilation → less O₂ supply
  Observed: OMZs expanding (~5% per decade in some regions since 1960s)
  Implication: denitrification increases → less fixed N for productivity
  → Negative feedback on primary production
```

---

## Trace Metals and Isotopes

```
TRACE METAL DISTRIBUTIONS (nutrient-type vs. scavenged-type):

  NUTRIENT-TYPE (correlate with nutrients, depleted at surface):
    Fe, Zn, Ni, Cd — taken up by phytoplankton, remineralized at depth

  SCAVENGED-TYPE (short residence time, removed by particle adsorption):
    Al, Pb, Th — depleted in deep water, higher near particle sources
    ²³⁴Th/²³⁸U disequilibrium: particle flux tracer (residence time ~24 days)

  CONSERVATIVE-TYPE (no biological interaction):
    Li, Cs, Rb — behave like salinity

  KEY EXAMPLE — Cadmium:
    Cd/phosphate ratio is nearly constant in seawater (Cd follows PO₄)
    Cd/Ca ratio in foraminifera fossils → paleoproxy for deep water nutrients
    → reconstructs ancient ocean circulation patterns

STABLE ISOTOPES AS PROXIES:
  δ¹³C: biological fractionation (light carbon preferentially fixed by photosynthesis)
    Deep water δ¹³C decreases as organic matter remineralized → old water is ¹³C-depleted
    δ¹³C of foram shells → reconstructs ancient ocean circulation
  δ³⁴S: sulfur cycling in sediments
  ⁸⁷Sr/⁸⁶Sr: conservative (residence ~5 Myr) → records continental weathering rates
  δ¹¹B: pH proxy in foram shells (boron speciation pH-dependent)
    Used to reconstruct past ocean pH → past atmospheric CO₂
```

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| Why does ocean pH stay near 8.1? | Bicarbonate/carbonate buffering system; TA >> DIC in seawater |
| What is the Revelle factor? | Buffer factor: ratio of relative pCO₂ change to relative DIC change; ~9–15 |
| What is ocean acidification? | CO₂ absorption → H₂CO₃ formation → H⁺ release → pH drop (~0.1 units since 1750) |
| What is aragonite saturation? | Ω_aragonite = [Ca²⁺][CO₃²⁻]/K'sp; <1 means aragonite dissolves |
| What is the Redfield ratio? | C:N:P = 106:16:1 — stoichiometry of marine phytoplankton and deep-water nutrients |
| What limits productivity in Southern Ocean? | Iron (HNLC region — high macronutrients, but low chlorophyll due to Fe limitation) |
| What is an OMZ? | Oxygen Minimum Zone: mid-depth region depleted of O₂ by organic matter respiration |
| What happens in OMZ? | Denitrification: NO₃⁻ → N₂; N₂O produced; aerobic fauna excluded |
| Why is conservative ion ratio constant? | Residence times >> ocean mixing timescale → globally homogenized |

---

## Common Confusion Points

**Adding CO₂ to seawater raises pCO₂ and lowers pH but does NOT immediately dissolve carbonate**: Ocean acidification first reduces CO₃²⁻ (by pushing equilibrium toward HCO₃⁻) before saturation state drops below 1.0. Carbonate shells don't suddenly dissolve at pH 8.0; they begin experiencing stress when Ω drops from ~4 to ~2. The process is gradual but ongoing.

**Alkalinity is not the same as pH or basicity**: Total Alkalinity (TA) is the capacity to neutralize acid — it's measured by titration, not a pH electrode. TA = ~2350 μeq/kg in modern seawater while pH = 8.1. High TA doesn't mean high pH; it means more buffering capacity. When organisms precipitate CaCO₃, they LOWER TA (consuming carbonate equivalents), which actually slightly raises pCO₂.

**HNLC regions have nutrients but not productivity**: High Nutrient, Low Chlorophyll regions (Southern Ocean, equatorial Pacific, NE Pacific) have ample N and P but low productivity because Fe is limiting. This is not "excess capacity" but an iron-capped system. The Fe came originally from dust blown from continents; remote ocean regions receive almost none.

**Conservative ≠ constant concentration**: Conservative ions maintain constant RATIOS to salinity. But their absolute concentration varies with salinity (more dilute near rivers/ice melt, more concentrated in evaporation zones). Chloride is conservative but varies from ~19 to ~25 g/kg between fresh-influenced and evaporating basins.

**Biological pump ≠ 100% carbon removal**: Only ~0.3–0.5% of surface production is permanently buried. The rest (~99.7%) is remineralized back to CO₂ somewhere in the water column or at the seafloor and returns to the atmosphere on the thermohaline timescale (~1000 yr). The pump is a DELAY mechanism, not permanent sequestration (on geological timescales).
