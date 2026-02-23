# Climate Models

## Model Hierarchy, GCMs, Parameterization, Ensemble Methods, Uncertainty

## The Big Picture: Model Hierarchy

```
CLIMATE MODEL HIERARCHY (increasing complexity →)

EBM          RCM/1D-RC   AGCM/OGCM    GCM (coupled)   ESM
====         =========   =========    =============    ===
Energy       Vertical     Separate     Atmos + Ocean   + Carbon
Balance      column       atmos or     coupled         + Land carbon
Models       (temp        ocean        + Sea ice       + Ice sheets
             profile)     models       + Land surface  + Aerosols
                                                       + Chemistry

Analytical   Process      Regional     Global          Earth
insight      understanding downscaling  projection      projection

°C/W/m²      T(z) profile  Regional     Global temp     Carbon
sensitivity               detail       + precip        feedbacks

IPCC line:    ← Research tools      │      Projection tools →
```

Each model type answers different questions. The choice depends on what you're trying to constrain — not on "more complex = better."

---

## Energy Balance Models (EBMs)

### Zero-Dimensional EBM

```
  THE SIMPLEST CLIMATE MODEL:

  dT/dt = (1/C) × [S(1-α)/4 - σT⁴]

  where:
    T = global mean surface temperature
    C = heat capacity of climate system (ocean dominates)
    S = solar constant (1361 W/m²)
    α = planetary albedo (0.30)
    σ = Stefan-Boltzmann constant (5.67×10⁻⁸ W/m²/K⁴)
    σT⁴ = outgoing longwave radiation

  EQUILIBRIUM: dT/dt = 0
    T_eq = [S(1-α)/(4σ)]^(1/4) = 255 K = -18°C

  THE GREENHOUSE EFFECT IN THE EBM:
    Replace σT⁴ with σT⁴/ε where ε = emissivity of atmosphere
    (ε < 1 because GHGs trap some OLR)
    → T_eq increases to match observed 288 K

  WHY EBMs ARE USEFUL DESPITE SIMPLICITY:
    Analytically tractable: can derive ECS exactly
    Parameter sensitivity is transparent
    Fast: compute climate sensitivity in milliseconds
    Good for testing feedbacks conceptually

  ECS FROM EBM:
    ΔT = ΔF / λ  where λ = climate feedback parameter (W/m²/K)
    λ = λ_Planck + λ_WV + λ_LR + λ_albedo + λ_cloud
    λ_Planck = -3.2 W/m²/K (stabilizing, always present)
    ECS = -ΔF₂ₓCO₂ / λ = 3.7 / λ
```

---

## General Circulation Models (GCMs)

### Architecture

```
  COUPLED GCM = AGCM + OGCM + SEA ICE + LAND SURFACE MODEL
  ┌──────────────────────────────────────────────────────────────┐
  │  ATMOSPHERIC GCM (AGCM)                                      │
  │  Horizontal resolution: 50–100 km typical (1–2° lat/lon)    │
  │  High-resolution: 25 km (~0.25°)                            │
  │  Vertical levels: 30–90 levels (surface to ~80 km)          │
  │  Time step: 20–30 minutes                                    │
  │  Variables: T, u, v, w, q (water vapor), surface pressure   │
  ├──────────────────────────────────────────────────────────────┤
  │  OCEAN GCM (OGCM)                                            │
  │  Resolution: 0.25°–1° (coarser runs faster; 1° = standard)  │
  │  Vertical levels: 30–60 depth levels (surface to ~6000 m)   │
  │  Time step: 30–60 minutes                                    │
  │  Variables: T, S (salinity), u, v, w, density               │
  ├──────────────────────────────────────────────────────────────┤
  │  SEA ICE MODEL                                               │
  │  Thermodynamic (melt/freeze) + dynamic (drift)              │
  │  Viscous-plastic or elastic-viscous-plastic rheology         │
  ├──────────────────────────────────────────────────────────────┤
  │  LAND SURFACE MODEL                                          │
  │  CLM (Community Land Model), JSBACH, CABLE                  │
  │  Soil temperature/moisture, evapotranspiration, vegetation  │
  │  Runoff generation → ocean freshwater flux                  │
  └──────────────────────────────────────────────────────────────┘

  COUPLING:
  Atmosphere ↔ Ocean: exchange heat, momentum, freshwater at interface
  Every 1-6 hours: exchange fluxes (Oasis3/MCT coupler)
  Flux adjustment: historical approach to correct model biases;
                   modern models avoid it (physically inconsistent)
```

### Dynamical Core

```
  PRIMITIVE EQUATIONS (hydrostatic, spherical geometry):
    ∂u/∂t + (u·∇)u - fv = -∂Φ/∂x + Fλ
    ∂v/∂t + (u·∇)v + fu = -∂Φ/∂y + Fφ
    ∂Φ/∂p = -α = -RT/p  (hydrostatic)
    ∂ω/∂p + ∇·u = 0   (continuity)
    ∂T/∂t + (u·∇)T + ωσ = Q/cp  (thermodynamic)
    ∂q/∂t + (u·∇)q = E - P    (water vapor)

  where f = Coriolis parameter, Φ = geopotential, α = specific volume
  These 5 equations govern large-scale atmospheric dynamics

  HYDROSTATIC APPROXIMATION:
    Valid for scales >> horizontal resolution
    Breaks down for convection (vertical acceleration significant)
    → convection must be parameterized, not resolved

  NUMERICAL METHODS:
    Spectral: expand in spherical harmonics; T85 = truncation at
              wavenumber 85 → ~1.4° resolution
    Finite difference: gridded, traditional
    Finite volume: conservative (matter/energy conserved exactly)
                   Modern preference; used in CESM/WRF

  CFL STABILITY CONDITION:
    Time step ≤ grid spacing / wave speed
    Reducing grid spacing by 2× requires 2× shorter time step
    → 3D refinement costs 8× (2× in each of x, y, t)
    → high-resolution models are enormously more expensive
```

---

## Parameterization: The Core Challenge

```
  THE PROBLEM:
  Grid cell: typically 50-100 km × 50-100 km × 1-3 km vertical
  Processes smaller than grid: cannot be explicitly resolved
  But: these subgrid processes profoundly affect large-scale dynamics

  WHAT MUST BE PARAMETERIZED:
  ┌────────────────────┬─────────────────────────────────────────┐
  │ Process            │ Scale     │ Parameterization approach   │
  ├────────────────────┼───────────┼─────────────────────────────┤
  │ Deep convection    │ 1-10 km   │ Mass flux (Arakawa-Schubert)│
  │ (thunderstorms)    │           │ or relaxed Arakawa-Schubert │
  │                    │           │ or Kain-Fritsch             │
  ├────────────────────┼───────────┼─────────────────────────────┤
  │ Shallow convection │ 0.1-1 km  │ Shallow convection scheme   │
  │ (cumulus clouds)   │           │ (boundary layer turbulence) │
  ├────────────────────┼───────────┼─────────────────────────────┤
  │ Cloud microphysics │ μm-mm     │ Bulk microphysics: prognostic│
  │ (droplet/ice)      │           │ cloud water, ice, snow, rain │
  ├────────────────────┼───────────┼─────────────────────────────┤
  │ Ocean eddy mixing  │ 10-100 km │ Gent-McWilliams eddy-induced│
  │                    │           │ advection parameterization  │
  ├────────────────────┼───────────┼─────────────────────────────┤
  │ Boundary layer     │ 10-1000 m │ Turbulent kinetic energy;   │
  │ turbulence         │           │ mixing length theory        │
  ├────────────────────┼───────────┼─────────────────────────────┤
  │ Land-surface       │ < grid    │ Tiling approach: multiple   │
  │ heterogeneity      │           │ vegetation/soil tiles per   │
  │                    │           │ grid cell; area-weighted avg│
  └────────────────────┴───────────┴─────────────────────────────┘

  PARAMETERIZATION UNCERTAINTY:
  Parameters in these schemes are "tuned" to match observed climate
  Different tuning choices → different model behavior → uncertainty
  This is a key source of inter-model spread
```

### Clouds: The Primary Uncertainty Source

```
  CLOUD RADIATIVE EFFECT (CRE):
  Low clouds (stratocumulus):
    SW (solar) cooling: reflect ~47 W/m² back to space
    LW (thermal) effect: small (low clouds are warm; warm = OLR ≈ surface OLR)
    Net: STRONG COOLING

  High clouds (cirrus):
    SW effect: modest (thin ice clouds, partial transparency)
    LW (thermal) warming: +26 W/m² (cold clouds emit less OLR)
    Net: NET WARMING

  THE CLOUD FEEDBACK PROBLEM:
  As climate warms:
  Do low clouds decrease? (less coverage → less SW reflection → amplifying +)
  Do low clouds increase? (more coverage → more SW reflection → negative -)
  This question is NOT yet definitively answered

  CONSTRAINED BY:
  Observational constraint (Sherwood et al. 2020, Nature):
    Used observations of atmospheric mixing to constrain
    ECS lower bound → "very likely above 2.5°C"
    Key advance: ruled out low ECS values (< 2.5°C)

  SATELLITE OBSERVATIONS (CERES):
    Measure radiative fluxes at TOA
    Cloud fraction, optical depth, height
    Constrain CRE and feedback sign in models
    STILL: cloud feedbacks uncertain within ~1 W/m²/K
```

---

## Earth System Models (ESMs)

```
  GCM + BIOGEOCHEMISTRY + VEGETATION DYNAMICS + ICE SHEETS

  ADDITIONAL COMPONENTS:
  ┌────────────────────────────────────────────────────────────┐
  │  Carbon cycle:                                             │
  │    Ocean biogeochemistry (OMIP): DIC, alkalinity,         │
  │    phytoplankton, biological pump                         │
  │    Land carbon: NPP, respiration, fire, permafrost        │
  │    → prognostic CO₂ (C4MIP simulations)                   │
  │                                                            │
  │  Atmospheric chemistry:                                    │
  │    Tropospheric ozone, OH, aerosol chemistry               │
  │    Methane oxidation, NOₓ chemistry                        │
  │                                                            │
  │  Dynamic vegetation:                                       │
  │    Competition between plant functional types              │
  │    Biome shifts under warming                              │
  │    Albedo and evapotranspiration feedbacks                 │
  │                                                            │
  │  Interactive aerosols:                                     │
  │    Dust, sea salt, sulfate, black carbon, organic aerosol  │
  │    Aerosol-cloud interactions (indirect effect)            │
  │                                                            │
  │  Ice sheet model:                                          │
  │    BISICLES, PISM — Greenland/Antarctic dynamics           │
  │    Sea level contribution; coupled via freshwater flux     │
  └────────────────────────────────────────────────────────────┘

  COST: ESMs are 5-20× more computationally expensive than GCMs
  Required computation: largest runs use >10,000 CPU cores for months
  DOE, NSF, NCAR, MPI, GFDL, UK Met Office, CNRM — major centers
```

---

## CMIP and Ensemble Methods

### CMIP6: The Model Comparison Framework

```
  CMIP (Coupled Model Intercomparison Project):
    Coordinated by WCRP (World Climate Research Programme)
    Common protocols: same scenarios, same output variables
    → allows model comparison apples-to-apples

  CMIP6 (current, AR6):
    40+ models from 20+ institutions globally
    Scenario runs: SSP (Shared Socioeconomic Pathways)
    ScenarioMIP: SSP1-1.9, SSP1-2.6, SSP2-4.5, SSP3-7.0, SSP5-8.5

  CMIP6 ECS RANGE:
    1.8–5.7°C (wider than CMIP5 2.1–4.7°C)
    Some models ECS > 5°C → "hot models" problem
    Constrained after: emerged constraints remove highest-ECS models
    AR6 likely range: 2.5–4.0°C (narrower than raw CMIP6)
```

### Three Sources of Uncertainty

```
  UNCERTAINTY IN CLIMATE PROJECTIONS:
  ┌────────────────────────────────────────────────────────────┐
  │  1. SCENARIO UNCERTAINTY (emissions pathway)               │
  │     What do humans emit?                                   │
  │     Dominant at LONG lead times (>50 years)                │
  │     Reducible by: policy choices                           │
  │                                                            │
  │  2. MODEL UNCERTAINTY (structural)                         │
  │     How sensitive is the climate system?                   │
  │     Dominant at MEDIUM lead times (10-50 years)            │
  │     Reducible by: better observations, process research    │
  │                                                            │
  │  3. INTERNAL VARIABILITY (chaotic atmosphere)              │
  │     What decade/year is climate in its cycle?              │
  │     Dominant at SHORT lead times (< 10-15 years)           │
  │     NOT reducible — fundamental to chaotic dynamics        │
  └────────────────────────────────────────────────────────────┘

  PRACTICAL:
  For 2030 temperature: internal variability dominates
  For 2050 temperature: model uncertainty and scenarios comparable
  For 2100 temperature: scenario uncertainty dominates
  → Uncertainty doesn't go away but its CHARACTER changes

  INITIAL-CONDITION ENSEMBLE:
  Run same model 40-50 times with tiny initial perturbations
  → Spread = internal variability range
  → Mean = forced response (signal extracted from noise)
  CanESM5: 25-member ensemble; CESM2: 100+ member LENS2
```

---

## Model Validation

### Historical Period Validation

```
  BENCHMARK: 1850–2024 observed temperature record
  Models must reproduce:
    Observed warming trend (~1.2°C over 1850-2024)
    Volcanic eruptions (cooling spikes: Krakatau 1883, Pinatubo 1991)
    El Niño/La Niña interannual variability
    Mid-20th century slowdown (1940s-1970s — aerosol masking)

  WHAT MODELS DO WELL:
    Global mean temperature trend (by construction — tuned)
    Broad spatial patterns of warming
    Stratospheric cooling (fingerprint of GHG-forced warming)

  WHAT MODELS DO LESS WELL:
    Regional precipitation (especially over land)
    Tropical precipitation variability
    Sea ice extent (some models drift)
    Cloud fraction and CRE
    Arctic amplification magnitude
```

### Paleoclimate Validation

```
  THE GOLD STANDARD FOR LONG-TERM MODEL PERFORMANCE:

  LAST GLACIAL MAXIMUM (LGM, ~21,000 yr ago):
    Known forcing: ice sheets + CO₂ (~190 ppm)
    Observed cooling: ~4-7°C globally (proxy-based)
    Models must reproduce LGM cooling with same sensitivity
    Emergent constraint: LGM cooling vs modern amplification
    → constrains ECS lower bound

  PALEOCENE-EOCENE THERMAL MAXIMUM (PETM, ~56 Myr ago):
    Rapid CO₂ injection (~1,000-2,000 GtC in < 10,000 yr)
    Warming: ~5-8°C globally
    Ocean acidification
    ECS analogue: but CO₂ background different, slower than modern
    Best studied rapid warming event in geological record

  HOLOCENE THERMAL OPTIMUM (~8,000-5,000 yr ago):
    Northern hemisphere insolation maximum (orbital)
    Warmer than preindustrial: ~0.5-1.0°C globally
    Models validated against proxy reconstructions
```

---

## Regional Downscaling

```
  PROBLEM: GCM grid (50-100 km) too coarse for local impacts
  (river basin management, urban heat islands, extreme events)

  DYNAMICAL DOWNSCALING:
    Nested RCM (Regional Climate Model) within GCM domain
    WRF (Weather Research and Forecasting): 4-12 km resolution
    Use GCM boundary conditions; resolve local topography
    EXPENSIVE: 3D grid refinement costs 8× per factor-of-2

  STATISTICAL DOWNSCALING:
    Learn statistical relationships between large-scale and local
    Apply those relationships under future GCM-forced scenarios
    BCSD (Bias Correction Spatial Disaggregation)
    Delta method: add GCM-projected change to observed local climatology
    Quantile mapping: correct model bias distribution-wide

  ASSUMPTIONS (where stats downscaling can fail):
    Stationarity: relationships learned from past hold in future
    If climate changes CHARACTER (not just mean): this breaks
    Example: if storm tracks shift, storm-temperature relationships change

  CORDEX (Coordinated Regional Climate Downscaling Experiment):
    Like CMIP but for regional models
    Covers major inhabited regions at 12-50 km
```

---

## Decision Cheat Sheet

| I want to understand... | Model type |
|---|---|
| Climate sensitivity (theoretical) | EBM |
| How feedback loops work | EBM / 1D RCM |
| Global temperature projections | GCM (CMIP6) |
| Carbon cycle feedbacks | ESM (C4MIP) |
| Regional climate impacts | RCM / statistical downscaling |
| Uncertainty ranges | Multi-model ensemble (CMIP6) |
| Internal variability | Large initial-condition ensemble |

---

## Common Confusion Points

**Climate models are not weather forecasts**: GCMs don't predict what the temperature will be on July 14, 2050. They project the *distribution* of possible temperatures — the statistics of climate, not the sequence of weather. Demanding that models "predict" specific weather events is a category error.

**All CMIP6 models are not equal**: The ECS range in CMIP6 (1.8-5.7°C) includes models that don't match observed present-day cloud properties. Emergent constraints (using observational properties to weight models) narrow this to ~2.5-4.0°C. Raw model spread isn't the policy-relevant range.

**Resolution does not fix parameterization problems**: Making the grid finer helps with topography and regional patterns, but convection, cloud microphysics, and ocean mixing still require parameterization at any computationally feasible resolution. The deep uncertainties are in the physics, not the grid.

**"Model uncertainty" and "prediction uncertainty" are different**: Model uncertainty = we don't know the true ECS. Scenario uncertainty = we don't know future emissions. Internal variability = the climate system is chaotic. These combine differently and have different policy implications. Only scenario uncertainty is directly reducible by human choices.
