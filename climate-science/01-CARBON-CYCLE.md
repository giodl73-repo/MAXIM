# The Carbon Cycle

## Reservoirs, Fluxes, Ocean Chemistry, Anthropogenic Perturbation

## The Big Picture: Carbon Reservoirs and Fluxes

```
GLOBAL CARBON CYCLE (units: GtC = gigatons of carbon)

                    ATMOSPHERE
                    ~~870 GtC~~
                    420 ppm CO₂
                   ↑↗         ↘↓
         GPP        |           |    Resp.
         ~120 GtC/yr|           |    ~118 GtC/yr
              (net  |           |    terrestrial
             land sink: ~3 GtC/yr)
                   ↗             ↘
        TERRESTRIAL BIOSPHERE          OCEAN SURFACE
          ~550 GtC vegetation          ~900 GtC DIC
          ~1,700 GtC soil organic      ~38,000 GtC total ocean
          ~1,500 GtC permafrost                  ↕
                                       gas exchange: ~80 GtC/yr
                                       net ocean sink: ~3 GtC/yr

        FOSSIL FUELS / LITHOSPHERE
          ~5,000 GtC accessible fossil C
          ~40,000,000 GtC total lithosphere
          Volcanic outgassing: ~0.1 GtC/yr

ANTHROPOGENIC PERTURBATION (~10 GtC/yr fossil + ~1.5 GtC/yr LUC):
  Fate of emitted CO₂:
    ~45% stays in atmosphere (airborne fraction)
    ~25% taken up by land ecosystems (CO₂ fertilization, etc.)
    ~30% absorbed by ocean (Henry's Law dissolution)

  NET RESULT:
  CO₂ rising ~2.5 ppm/year (accelerating)
```

---

<!-- @editor[structure/P2]: No comparison tables — entire guide is ASCII code blocks. Add at least one rendered Markdown table (e.g., reservoir comparison: name, stock GtC, turnover time, trend) -->

## Reservoir Deep Dive

### Atmosphere

```
  Current content: ~870 GtC as CO₂ (2024: ~422 ppm)
  Residence time: CO₂ molecule: ~4 years (rapid exchange with
                  land and ocean biosphere)
                  BUT: perturbation lifetime ≠ molecule lifetime
                  If we emit 1 tonne CO₂:
                  ~50% absorbed within decades (biosphere/ocean)
                  ~20% absorbed within centuries (ocean)
                  ~20% absorbed within millennia (ocean sediment)
                  ~10% remains for >100,000 years (rock weathering)

  THE 10% PROBLEM:
  Even after 1,000 years, 10% of each emission pulse remains
  CO₂ is effectively permanent on human civilization timescales
```

### Ocean Carbon

```
  OCEAN CARBON SPECIATION:
  CO₂ dissolved in seawater participates in equilibrium:

  CO₂(g) ⇌ CO₂(aq)         [Henry's Law: K_H = 3.4×10⁻² mol/L/atm]
  CO₂(aq) + H₂O ⇌ H₂CO₃    [weak carbonic acid]
  H₂CO₃ ⇌ H⁺ + HCO₃⁻       [pKa₁ = 6.35]
  HCO₃⁻ ⇌ H⁺ + CO₃²⁻        [pKa₂ = 10.33]

  At seawater pH ~8.1:
    ~1% as CO₂(aq)
    ~91% as HCO₃⁻ (bicarbonate)
    ~8% as CO₃²⁻ (carbonate)

  DIC (Dissolved Inorganic Carbon) = CO₂ + H₂CO₃ + HCO₃⁻ + CO₃²⁻
  Total ocean DIC: ~38,000 GtC
  (44× more than atmosphere — ocean is the dominant carbon reservoir)
```

<!-- @editor[bridge/P2]: No old-world bridge in the guide. Natural bridge here: the learner knows equilibrium chemistry and Henry's Law from MIT — connect "you know Le Chatelier's principle and carbonate equilibria; the Revelle factor is the climate-scale consequence of the buffer capacity you learned in gen chem" -->

### The Revelle Factor (Buffer Chemistry)

```
  WHY OCEAN UPTAKE IS LIMITED:

  The Revelle factor (R) relates fractional change in CO₂ to
  fractional change in DIC:

  R = (ΔpCO₂/pCO₂) / (ΔDIC/DIC) ≈ 10 at modern ocean chemistry

  INTERPRETATION:
  A 10% increase in atmospheric CO₂ pCO₂ causes only ~1% increase
  in ocean DIC → ocean can't absorb proportionally as CO₂ rises

  The buffer capacity DECREASES as ocean acidifies:
  As pH falls → less CO₃²⁻ available to buffer new CO₂ additions
  → airborne fraction of emissions INCREASES over time
  → acceleration of atmospheric CO₂ growth relative to emissions

  Roger Revelle (1957): "large-scale geophysical experiment" of
  adding CO₂ to atmosphere and ocean; measured Revelle factor;
  convinced Keeling to start continuous CO₂ measurement (1958)
```

---

## Ocean Acidification

```
  pH CHANGE SINCE PRE-INDUSTRIAL:
  Pre-industrial ocean surface pH: ~8.18
  2024 ocean surface pH: ~8.08
  Change: -0.10 pH units

  BUT: pH is logarithmic → 0.1 unit change = 26% increase in [H⁺]

  CALCIFICATION IMPACTS:
  CO₃²⁻ + Ca²⁺ → CaCO₃ (calcification by marine organisms)
  As pH falls → [CO₃²⁻] falls → CaCO₃ less supersaturated

  ORGANISMS AFFECTED:
    Pteropods (sea butterflies): shells dissolve in lab conditions
    Oysters/mussels: reduced shell growth, larval failure observed
    Coral reefs: bleaching + reduced calcification
    Foraminifera: thinner shells in high-CO₂ conditions

  ARAGONITE SATURATION STATE (Ω):
  Aragonite (coral form of CaCO₃) is more soluble than calcite
  Pre-industrial: Ω ~3.5 globally; coral reefs safe
  2024: Ω ~2.8 globally; Arctic < 1.5 (undersaturated)
  Projection: Tropical coral reefs threatened at Ω < 1.5
  (all aragonite dissolving) — reached if CO₂ > ~550 ppm
```

---

## The Biological Pump

```
  HOW OCEAN SEQUESTERS CARBON FROM SURFACE TO DEPTH:

  Sunlit surface (photic zone, 0–200 m):
    Phytoplankton: CO₂ + H₂O → CH₂O + O₂ (photosynthesis)
    Net: CO₂ from atmosphere dissolved into organic carbon

  Sinking:
    Dead organic matter, fecal pellets, marine snow sink
    "Export flux": ~10 GtC/yr leaves photic zone
    Only ~0.1 GtC/yr reaches deep seafloor (90% remineralized)

  Deep ocean:
    Bacteria remineralize organic carbon → CO₂ released into deep water
    Deep water is undersaturated with O₂, high in CO₂ (high DIC)
    THIS IS WHY deep water can't exchange with atmosphere directly
    → effectively sequestered on millennial timescales
    (deep water residence time ~1,000 years before upwelling)

  NET:
  Biological pump transfers ~10 GtC/yr from surface to deep
  This is why ocean has so much more carbon than atmosphere
```

---

## The Terrestrial Carbon Cycle

### Carbon Fluxes on Land

```
  GPP (Gross Primary Production): ~120 GtC/yr
    CO₂ fixed by photosynthesis globally
    Gross — before plant respiration

  Ra (Autotrophic respiration): ~60 GtC/yr
    Plants respire ~50% of GPP

  NPP (Net Primary Production): ~60 GtC/yr
    GPP - Ra; what's available to rest of ecosystem

  Rh (Heterotrophic respiration): ~57 GtC/yr
    Microbes decomposing dead organic matter

  NEP (Net Ecosystem Production): ~3 GtC/yr
    The current land SINK = NPP - Rh
    This carbon accumulates in ecosystems

  MECHANISMS OF THE LAND SINK:
  1. CO₂ fertilization: higher CO₂ → higher photosynthesis rate
     (diminishing returns; N/P limitation matters more)
  2. Northern hemisphere afforestation / forest regrowth
  3. Extended growing seasons (warming → longer frost-free period)

  VULNERABILITY:
  Warming increases Rh (Q₁₀ ~ 2: 10°C warming → ~2× respiration)
  Land sink may weaken or become a source above 2–3°C warming
```

### Permafrost: The Sleeping Giant

```
  PERMAFROST CARBON STOCK:
  ~1,500 GtC frozen organic matter (peat, organic soil)
  Accumulated under cold conditions over 10,000+ years
  Distribution: Siberia (~40%), Alaska, Canada, Tibet, Andes

  THE THAW MECHANISM:
  Permafrost thaw → microbial decomposition of organic matter
  Aerobic conditions → CO₂ release (waterlogged → CH₄ release)
  CH₄ from thermokarst lakes is especially potent (GWP-20 = 80)

  FEEDBACK TIMING:
  "Fast" feedback: active layer deepening → surface emissions
                   Detectable now in high-latitude observations
  "Slow" feedback: deep talik formation, coastal erosion
                   Decades to centuries to fully mobilize

  SCALE OF RISK:
  If 10% of permafrost C mobilizes = 150 GtC additional to atmosphere
  = equivalent to ~15 years of current emissions
  This is not in current IPCC models at full magnitude
  → one reason actual warming may exceed model projections
```

---

## Non-CO₂ Greenhouse Gases

### Methane (CH₄)

```
  SOURCES (GtC-equivalent/yr):
    Wetlands (natural): ~160 MtCH₄/yr  ← largest single source
    Agriculture: ~170 MtCH₄/yr
      Ruminant enteric fermentation: ~95 MtCH₄/yr
      Rice paddies: ~30 MtCH₄/yr
      Manure: ~45 MtCH₄/yr
    Fossil fuel (coal/gas/oil production + use): ~110 MtCH₄/yr
    Permafrost/thermokarst: ~20 MtCH₄/yr (growing)
    Landfills: ~60 MtCH₄/yr

  ATMOSPHERIC CHEMISTRY:
    Lifetime: ~9 years (oxidized to CO₂ + H₂O by OH radical)
    GWP-100: 28 (28× CO₂ over 100 years)
    GWP-20:  80 (more relevant for short-term warming)
    Current concentration: ~1,900 ppb (2.7× pre-industrial)
    Growth rate: accelerating since 2006 — unclear why (wetlands? fracking?)

  WHY CH₄ MATTERS URGENTLY:
    Short lifetime → reducing CH₄ emissions has near-term benefit
    GWP-20 = 80 → methane is a major near-term warming driver
    "Fast mitigation" — reducing methane gives faster response
    than CO₂ reductions (CO₂ persists for centuries)
```

### Nitrous Oxide (N₂O)

```
  SOURCES:
    Agriculture: ~5.0 MtN₂O/yr (largest single source)
      Synthetic N fertilizer → soil nitrification/denitrification
    Natural soils: ~6.0 MtN₂O/yr
    Oceans: ~4.0 MtN₂O/yr

  ATMOSPHERIC CHEMISTRY:
    Lifetime: ~114 years
    GWP-100: 265
    Current: ~334 ppb (1.24× pre-industrial 270 ppb)
    Stratospheric destruction: reacts with O* → NO
    → contributes to ozone layer depletion

  AGRICULTURAL CONNECTION:
    Haber-Bosch process (N₂ + H₂ → NH₃) → synthetic fertilizer
    → food production for 8 billion people
    → also → N₂O emissions
    The same process that feeds humanity is driving 6% of warming
```

---

## The Airborne Fraction and Carbon Budget

```
  AIRBORNE FRACTION:
    = CO₂ remaining in atmosphere / CO₂ emitted
    Historical average: ~45%
    (55% absorbed by land + ocean annually)

    But as ocean acidifies and land sink may weaken →
    airborne fraction likely to increase over time

  REMAINING CARBON BUDGET (IPCC AR6):
  For 50% probability of staying below:
    1.5°C: ~500 GtCO₂ remaining (as of Jan 2020)
           ~400 GtCO₂ remaining (as of Jan 2024 — ~11 years at
           current ~40 GtCO₂/yr emissions)
    2.0°C: ~1,350 GtCO₂ remaining (as of Jan 2020)

  Note: budget uncertainties = ±220 GtCO₂ due to:
    - Permafrost feedback not fully included
    - Non-CO₂ GHG trajectory
    - Aerosol masking
```

---

## Decision Cheat Sheet

| I want to understand... | Section |
|---|---|
| How much carbon is where | Reservoir overview |
| Why ocean can't absorb more CO₂ | Revelle factor |
| Why oceans are acidifying | Ocean chemistry |
| How marine ecosystems are affected | Ocean acidification |
| What permafrost risk looks like | Permafrost section |
| Why methane matters for near-term | CH₄ section |
| How much CO₂ we can still emit | Carbon budget |

---

## Common Confusion Points

**Atmospheric CO₂ lifetime vs perturbation lifetime**: An individual CO₂ molecule cycles through the atmosphere every ~4 years. But the *perturbation* (net addition above pre-industrial) lasts because emissions exceed sinks. ~10% of each emission pulse lasts >100,000 years. "CO₂ lasts 100 years" is a common figure that actually refers to ~half-life, not full lifetime.

**The 30% ocean sink is not reliable**: As atmospheric CO₂ rises, ocean pCO₂ also rises (Henry's Law). As ocean pH falls, buffer capacity decreases (Revelle factor increases). The ocean sink cannot indefinitely absorb a constant fraction of rising emissions.

**Methane oxidizes to CO₂**: After ~9 years in atmosphere, CH₄ is oxidized by OH radicals to CO₂. So methane emissions don't disappear — they become long-lived CO₂. GWP-100 = 28 accounts for this. The 9-year lifetime means reducing methane *now* has near-term impact before conversion.

**Permafrost feedback is not in most climate models**: IPCC AR6 models include some permafrost CO₂ feedback but not the full CH₄ from thermokarst lakes or the deep talik dynamics. This is a known source of potential underestimation of future warming.
