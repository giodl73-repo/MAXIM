# Climate Science — Overview: Earth's Energy Budget

<!-- @editor[diagram/P2]: Opening diagram is a detailed energy budget — not a landscape of climate science as a whole. The Module Map table at line 191 is the actual landscape; promote it to the opening position and use the energy budget as a drill-down under its own section -->

## The Big Picture: Radiative Balance

```
SOLAR INPUT AND EARTH'S ENERGY BUDGET
======================================

Solar constant: 1,361 W/m²
Average over sphere: 1361/4 = 340 W/m² (spherical vs. disk factor)

     INCOMING: 340 W/m²
          ↓
     ┌────┴─────────────────────────────────────────────────┐
     │                  ATMOSPHERE                           │
     │  ↑ 77 W/m² reflected by clouds/atmosphere (albedo)  │
     │  ↑ 23 W/m² absorbed by O₃/water vapor               │
     │         ↓ 240 W/m² reaches surface                   │
     └──────────────────────────────────────────────────────┘
          ↑ 30 W/m² reflected by surface (surface albedo)
          ↓ 168 W/m² absorbed by surface

OUTGOING LONGWAVE RADIATION (OLR):
  Surface emits ~396 W/m² as thermal IR (~10 μm peak)
  Greenhouse gases absorb most of this, re-emit in all directions
  Only ~240 W/m² escapes to space

NET (pre-industrial): IN ≈ OUT ≈ 240 W/m² → stable climate
NET (2024):          IN > OUT by ~0.9 W/m² → ongoing warming

NATURAL GREENHOUSE EFFECT:
  Without atmosphere: Earth surface temperature = 255 K (-18°C)
  With natural greenhouse: 288 K (+15°C)
  Difference: +33°C — the natural greenhouse effect
```

---

<!-- @editor[structure/P2]: No comparison tables in the body — entire guide is ASCII code blocks. Add at least one table (e.g., major GHGs compared: gas, concentration, forcing, lifetime, GWP) -->

## Greenhouse Gas Physics: Why Molecular Absorption Matters

```
MOLECULAR ABSORPTION — SPECTROSCOPIC BASIS
==========================================

Earth's surface emits IR peaking at ~10 μm (Wien's law: λ_max = 2898/T)

GAS ABSORPTION BANDS:
  CO₂:   15 μm (bending mode) ← directly overlaps surface emission peak
          4.3 μm (asymmetric stretch — solar, less important for warming)
  H₂O:   6.3 μm, 2.7 μm, + rotational bands throughout far-IR
          Broadband "continuum" absorption — H₂O is #1 greenhouse gas
  CH₄:   7.7 μm, 3.3 μm
  N₂O:   17 μm, 7.8 μm, 4.5 μm
  O₃:    9.6 μm — sits in the "atmospheric window"

"ATMOSPHERIC WINDOW" (8–12 μm):
  Largely transparent except O₃ at 9.6 μm
  About 40 W/m² escapes through this window to space
  As CO₂ increases: wings of 15μm band widen, narrowing the window

WHY MORE CO₂ STILL MATTERS AT HIGH CONCENTRATIONS:
  Center of CO₂ 15μm band is already optically thick — "saturated"
  But: spectral wings are not saturated
  Adding CO₂ widens the absorption into the wings
  → more IR trapped, even though center was already opaque
  This is the correct physics — "CO₂ is saturated" argument is wrong
```

---

## Radiative Forcing: Quantifying the Perturbation

```
RADIATIVE FORCING (RF):
  Instantaneous perturbation to Earth's energy balance at tropopause
  Units: W/m²
  Positive: more energy absorbed → warming tendency
  Negative: more energy reflected/emitted → cooling tendency

FORCING FORMULA FOR CO₂ (Myhre et al. 1998, IPCC standard):
  ΔF = 5.35 × ln(C/C₀)

  Pre-industrial C₀ = 280 ppm
  2024 C = ~422 ppm

  ΔF = 5.35 × ln(422/280) = 5.35 × ln(1.507) = 5.35 × 0.410 = 2.2 W/m²

  Each CO₂ doubling (280→560→1120): same additional ~3.7 W/m²
  Logarithmic relationship = diminishing marginal forcing per ppm added
  BUT: we're adding more ppm faster → net forcing still accelerating

MAJOR FORCING AGENTS (IPCC AR6, 2021):
  Well-mixed GHGs (CO₂ + CH₄ + N₂O + F-gases):  +3.84 W/m²
  Land-use change (albedo):                       -0.20 W/m²
  Aerosols (total — direct + cloud effects):      -1.01 W/m²  ← uncertain
  Black carbon:                                   +0.27 W/m²
  NET ANTHROPOGENIC:                              +2.72 W/m²

  Aerosols are a masked "warming in the bank" — if we reduce air
  pollution (good for health), we lose the cooling mask and see
  more rapid warming from the underlying CO₂/CH₄ forcing
```

---

<!-- @editor[bridge/P2]: No old-world bridge anywhere in the guide. Natural bridge: the learner knows thermodynamics (Stefan-Boltzmann, blackbody radiation, Wien's law) from MIT physics — open with "you already know radiative equilibrium from thermo; climate science is that equation plus feedbacks" -->

## Climate Sensitivity: Translating Forcing to Temperature

```
EQUILIBRIUM CLIMATE SENSITIVITY (ECS):
  Definition: global mean temperature change at equilibrium
              after a sustained CO₂ doubling
  Forcing per doubling: ~3.7 W/m²
  Planck (no-feedback) response: ΔT₀ = ΔF / (4σT³) ≈ 1.2°C
  Actual response: larger, because feedbacks amplify

  ECS = ΔT₀ / (1 - Σfᵢ)  where fᵢ are feedback parameters

  FEEDBACK BREAKDOWN:
  ┌────────────────┬──────────────────┬─────────────────────────┐
  │ Feedback       │ Value (W/m²/K)   │ Notes                   │
  ├────────────────┼──────────────────┼─────────────────────────┤
  │ Planck         │ -3.2             │ Stabilizing; fundamental │
  │ Water vapor    │ +1.8             │ Well-constrained, strong  │
  │ Lapse rate     │ -0.4             │ Complex; tropical vs pole │
  │ Surface albedo │ +0.3             │ Ice-albedo feedback       │
  │ Cloud total    │ -0.4 to +0.4     │ PRIMARY UNCERTAINTY       │
  └────────────────┴──────────────────┴─────────────────────────┘

  IPCC AR6 (2021) best estimates:
    ECS likely range: 2.5 – 4.0°C
    Best estimate:    3.0°C
    Very likely:      2.0 – 5.0°C

TRANSIENT CLIMATE RESPONSE (TCR):
  Warming at CO₂ doubling under 1%/yr increase scenario
  Lower than ECS because ocean thermal inertia delays warming
  TCR likely range: 1.4 – 2.2°C

TCRE (Transient Climate Response to cumulative Emissions):
  °C per 1000 GtCO₂ — most operationally useful for carbon budgets
  TCRE ≈ 0.45°C per 1000 GtCO₂
  Simple: every ~2,200 GtCO₂ emitted → ~1°C additional warming
```

---

## Historical Climate Record

```
PROXY METHODS FOR RECONSTRUCTING PAST CLIMATES:
┌───────────────┬──────────────┬─────────────────────────────────────┐
│ Proxy         │ Archive      │ Signal                              │
├───────────────┼──────────────┼─────────────────────────────────────┤
│ Ice cores     │ Greenland,   │ δ¹⁸O → temperature; trapped gas    │
│               │ Antarctica   │ → paleo-CO₂, CH₄; tephra layers     │
│               │ 800,000 yr   │                                     │
├───────────────┼──────────────┼─────────────────────────────────────┤
│ Tree rings    │ Wood         │ Ring width/density → temp/precip    │
│               │ dendro-chron.│ ~10,000 yr; seasonal resolution     │
├───────────────┼──────────────┼─────────────────────────────────────┤
│ Ocean sediment│ Foram shells │ δ¹⁸O → SST + ice volume            │
│               │ 65 Myr       │ Mg/Ca → SST; alkenone → SST        │
├───────────────┼──────────────┼─────────────────────────────────────┤
│ Speleothems   │ Cave         │ Stalagmite δ¹⁸O → precipitation    │
│               │              │ pattern; U-Th dating                │
├───────────────┼──────────────┼─────────────────────────────────────┤
│ Coral         │ Reef coral   │ δ¹⁸O + Sr/Ca → SST back ~500 yr   │
├───────────────┼──────────────┼─────────────────────────────────────┤
│ Instrumental  │ Thermometer  │ 1850–present; ~100 yr gridded       │
│               │ records      │ Berkeley Earth / GISTEMP / HadCRUT  │
└───────────────┴──────────────┴─────────────────────────────────────┘

TEMPERATURE MILESTONES:
  Pre-industrial baseline:  1850–1900 average
  1850–1900:                0.0°C (definition)
  1980–2000:                +0.4°C
  2023:                     +1.45°C (hottest year in instrumental record)
  2024:                     +1.5°C first full calendar year above 1.5°C

  Rate of warming: ~0.19°C/decade (1981–2024, accelerating)
  Rate of CO₂ increase: ~2.5 ppm/year (also accelerating)

  Last time this warm: Pliocene (~3 million years ago, 2–3°C warmer)
  Last time CO₂ this high: also Pliocene (~380–420 ppm)
```

---

## Module Map

| Module | Topic | Key Concept |
|--------|-------|-------------|
| 00 | Overview (this) | Radiative forcing, GHG physics, ECS |
| 01 | Carbon Cycle | Reservoirs, fluxes, ocean chemistry |
| 02 | Climate Models | EBMs → GCMs → ESMs, validation |
| 03 | Feedbacks & Tipping | Water vapor, ice-albedo, AMOC, permafrost |
| 04 | Emissions Pathways | SSP scenarios, remaining carbon budget |
| 05 | Impacts | Sea level, extremes, agriculture, risk |
| 06 | Mitigation & Geoengineering | Renewables, CDR, SAI |

---

## Decision Cheat Sheet

<!-- @editor[structure/P2]: Decision Cheat Sheet is a module navigation table, not a decision tool — reframe as "use X when Y" rows (e.g., "Evaluating whether CO₂ is saturated → 00 GHG physics; Estimating remaining emission budget → 04 Carbon budget math") -->

| I want to understand... | Go to |
|---|---|
| Why CO₂ causes warming (physics) | 00 (this) |
| How long CO₂ stays in atmosphere | 01 |
| How climate models work | 02 |
| Why tipping points matter | 03 |
| How much CO₂ we can still emit | 04 |
| Projected sea level rise | 05 |
| Whether solar geoengineering works | 06 |

---

## Common Confusion Points

**"CO₂ is already saturated"**: The *center* of the 15μm absorption band is optically thick, but the spectral *wings* are not. Adding more CO₂ widens absorption into wings and narrows the atmospheric window. The saturation argument fails basic spectroscopy.

**CO₂ vs temperature in ice cores**: At glacial-interglacial transitions, CO₂ lags temperature by ~800 years. The mechanism: Milankovitch orbital forcing initiates warming; this outgasses CO₂ from oceans (lower CO₂ solubility at higher T); CO₂ then amplifies the warming as a feedback. Today, anthropogenic emissions are the *forcing*, not a feedback. The causal direction has reversed.

**ECS vs TCR vs TCRE**: ECS = long-run temperature per CO₂ doubling at equilibrium. TCR = temperature at doubling under 1%/yr CO₂ scenario (ocean inertia keeps this lower). TCRE = temperature per cumulative emissions in °C/1000GtCO₂ (most useful for budget calculations). They're different questions.

**The 1.5°C target is about risk, not a physical cliff**: Crossing 1.5°C doesn't trigger catastrophe at exactly that moment. It's a risk threshold — probability of activating certain tipping elements increases, more extreme events occur, adaptation costs rise sharply. The IPCC framing is probabilistic, not binary.

**Attribution science is established**: Modern attribution (whether a specific extreme event was made more likely/severe by climate change) uses counterfactual modeling — run climate models with and without anthropogenic forcing, compare event probability distributions. It's not speculation; it's the same methodology as pharmaceutical clinical trials.
