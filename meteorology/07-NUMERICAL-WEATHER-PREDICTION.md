# Numerical Weather Prediction — GFS vs ECMWF, Ensembles, Chaos

## The Big Picture

Numerical weather prediction (NWP) is applied fluid dynamics: discretize the atmosphere onto a grid, solve the primitive equations forward in time. The engineering challenge is that errors grow exponentially (Lorenz, 1963), hard-limiting forecast skill to ~2 weeks no matter how good the model. Beyond that limit, probabilistic (ensemble) approaches are the only scientific answer.

```
+------------------------------------------------------------------+
|                    NWP SYSTEM OVERVIEW                           |
|                                                                  |
|  OBSERVATIONS                                                    |
|  (surface, radiosonde, radar, satellite, buoy, aircraft)         |
|           |                                                      |
|           v                                                      |
|  DATA ASSIMILATION (4D-Var, EnKF)                                |
|  Best estimate of atmospheric state (analysis)                   |
|           |                                                      |
|           v                                                      |
|  INITIAL CONDITIONS (analysis + 0hr forecast)                    |
|           |                                                      |
|           v                                                      |
|  NWP MODEL (step forward in time: 60s–10min timesteps)           |
|  Dynamics: Primitive equations + physics parameterizations       |
|           |                                                      |
|           v                                                      |
|  OUTPUT: T, P, wind, humidity, precipitation on grid             |
|  Post-processing: Model output statistics (MOS), bias correction |
+------------------------------------------------------------------+
```

---

## The Primitive Equations

The governing equations of NWP (simplified; σ-coordinate form):

```
CONSERVATION OF MOMENTUM (3 components):
  du/dt = fv - (1/ρ)(∂p/∂x) + F_x  [zonal; x-direction]
  dv/dt = -fu - (1/ρ)(∂p/∂y) + F_y  [meridional; y-direction]
  dw/dt = -g - (1/ρ)(∂p/∂z) + F_z  [vertical; often hydrostatic approx]

CONTINUITY (mass conservation):
  ∂ρ/∂t + ∇·(ρV) = 0

THERMODYNAMIC ENERGY:
  dT/dt = (Q̇)/(cpρ) + (α/cp)(dp/dt)
  (T changes from: heating Q̇ + adiabatic compression/expansion)

MOISTURE:
  dq/dt = E - C + D
  (specific humidity from: evaporation - condensation + diffusion)

EQUATION OF STATE:
  p = ρRT_v
  (T_v = virtual temperature accounting for moisture)
```

**Hydrostatic approximation** — vertical momentum equation simplified to dw/dt ≈ 0, giving ∂p/∂z = -ρg. Valid for large-scale (horizontal >> vertical scale). Fails in convection → convection must be parameterized (global models) or explicitly resolved (convection-allowing models, ≤ 4 km grid).

---

## Model Grids and Resolution

```
GLOBAL MODELS:
  Resolution ~12–25 km horizontal; 50–137 vertical levels
  Domain: entire globe (spherical harmonics or reduced Gaussian grid)
  Time step: ~1–7 minutes (governed by CFL stability criterion)

REGIONAL MODELS (LAM: Limited Area Models):
  Resolution ~1–4 km horizontal (convection-allowing)
  Domain: continental or regional
  Nested within global model for boundary conditions

VERTICAL LEVELS:
  Terrain-following sigma coordinates (σ = p/p_surface) near surface
  Pressure coordinates in upper troposphere
  Hybrid sigma-pressure in between
  Coverage: surface to ~1 hPa (stratosphere)
```

**Horizontal resolution vs what it resolves:**

| Grid spacing | Features resolved | Model type |
|-------------|-----------------|------------|
| 100 km | Synoptic (fronts, large cyclones) | Old global; climate models |
| 25 km | Synoptic systems well; mesoscale beginning | Current global NWP |
| 12 km | Mesoscale convective systems | Operational NWP (GFS) |
| 3 km | Individual thunderstorms | Convection-allowing (HRRR) |
| 1 km | Storm-scale; tornado vortices beginning | Research; some operations |

---

## Physics Parameterizations — The Art

Everything below the model grid scale must be *parameterized* — estimated from resolved-scale variables:

```
PROCESS           PARAMETERIZATION APPROACH        WHY IT MATTERS
----------------  --------------------------------   --------------------
Deep convection   Kain-Fritsch, Arakawa-Schubert;  Controls tropical
                  triggered when CAPE > threshold;  rainfall, ITCZ; #1
                  adjusts temperature/moisture      source of model error

Shallow convection Similar but for non-precipitating Major in boundary
                  cumulus                           layer moisture

Boundary layer    K-theory, TKE closure;            Surface fluxes;
turbulence        Surface exchange coefficients      wind near surface

Radiation         RRTMG, LBLRTM;                    Energy balance;
(SW + LW)         Gas absorption, cloud optical      temperature
                  properties                         structure

Microphysics      Bulk or bin; categories:          Precipitation type;
                  cloud water, rain, ice, snow,      QPF accuracy
                  graupel, hail

Land surface      Noah-LSM, CLM; soil moisture,     Boundary layer
                  vegetation, albedo, heat flux      development

Sea ice           Thermodynamic + dynamic models    Arctic forecasting
```

**Convective parameterization** is the hardest and most error-prone. In convection-allowing models (≤3 km), explicit convection replaces parameterization, dramatically improving precipitation timing and location.

---

## GFS vs ECMWF — Skill Comparison

```
MODEL          SPONSOR      GRID(2025)   ENSEMBLE    NOTABLE STRENGTH
-----------    ----------   ----------   ---------   ----------------------
GFS            NOAA/NCEP    ~13 km Δx    GEFS        Free/open data;
(Global        (US)         127 levels   (30+mem)    good NAm. coverage
Forecast                                             2-week extended
System)

ECMWF IFS      European     ~9 km Δx     EPS (50+1   Consistently best
(IFS model)    Centre       137 levels   members)    global model;
                                                     superior tropics;
                                                     best medium range
                                                     (days 5-10)

GFS-FV3        NOAA         ~13 km        GEFS       Upgraded 2019
               (upgraded)                 updated    (FV3 core)

ICON           Germany (DWD) ~13 km       ICON-EPS   Good European
                             90 levels               performance

Unified Model  UK Met Office ~10 km       MOGREPS    Good short range
```

**Why ECMWF wins** — Data assimilation is better (4D-Var with careful observation QC), higher vertical resolution in upper atmosphere, ensemble design more sophisticated, more physical parameterization research investment. ECMWF is a consortium model — 35 nations; insulated from political pressures; focused purely on NWP quality.

**The "GFS Fail" narrative** — During Hurricane Sandy 2012, ECMWF correctly forecast the unusual left turn landfall 5 days out while GFS kept it going out to sea. Accelerated US investment in model improvement.

---

## Data Assimilation — The Analysis Problem

The initial conditions are everything. Errors in initial conditions double in ~1–2 days.

```
PROBLEM: Atmospheric state is continuous (infinite degrees of freedom).
         Observations are sparse and irregular.
         Models have ~10⁹ grid points.

SOLUTION: 4D-Variational Data Assimilation (4D-Var):
  Minimize cost function:
  J = (x-xb)ᵀ B⁻¹ (x-xb) + Σ (y-H(x))ᵀ R⁻¹ (y-H(x))

  Where:
    x = analysis state (what we're solving for)
    xb = background/prior (short-range forecast from previous cycle)
    B = background error covariance matrix
    y = observations
    H = observation operator (converts model state to obs type)
    R = observation error covariance

  Essentially: find the state that balances prior knowledge (model
  background) with observations, weighted by their error statistics.
```

4D-Var is constrained nonlinear optimization over ~10⁹ variables: minimize J subject to the PDE constraint that x must be a physically realizable atmospheric trajectory. The adjoint model computes ∇ₓJ exactly — the same reverse-mode automatic differentiation used in backpropagation, implemented on the full NWP model. This makes 4D-Var the largest-scale inverse problem routinely solved in science.

**EnKF (Ensemble Kalman Filter)** — alternative to 4D-Var; uses ensemble spread to estimate background error covariances. Less computationally demanding for background error estimation. Many operational centers now use hybrid EnKF/4D-Var.

**Key observation types** (by impact rank):
1. Satellite radiances (AMSU, IASI, CrIS) — most data by volume
2. Radiosondes (~800 stations globally, twice daily)
3. Aircraft (AMDAR/ACARS) — especially over oceans
4. Scatterometer winds (ocean surface wind vectors)
5. GPS radio occultation — temperature/humidity profiles
6. Surface observations (SYNOP, METAR, buoys)

---

## Ensemble Forecasting — Quantifying Uncertainty

Since exact future state is unknowable beyond ~2 weeks, run **many slightly different forecasts** to map out the probability distribution:

```
ENSEMBLE DESIGN:
  Initial condition perturbations:
    - Bred vectors (GEFS): fastest-growing perturbations
    - Singular vectors (ECMWF): optimal growing perturbations
    - EnKF spread: flow-dependent perturbations

  Stochastic physics perturbations (model uncertainty):
    - SPPT (Stochastically Perturbed Parameterization Tendencies)
    - SKEB (Stochastic Kinetic Energy Backscatter)

  Multi-model ensembles:
    - NAEFS (GFS + Canadian), TIGGE (all major NWP ensembles)
    - Blend models → reduce systematic bias

OUTPUT INTERPRETATION:
  Ensemble mean: most likely outcome (smears out features for long range)
  Ensemble spread: uncertainty in forecast
  Probability products: P(rain > X mm), P(wind > Y km/h)
  Spaghetti plots: individual member tracks
```

**Ensemble skill score** — ECMWF EPS ensemble mean forecast valid at day 7 is as good as a deterministic (single) forecast valid at day 5 (approximately). Ensemble mean is always better than any single deterministic run beyond day 3.

---

## Lorenz Chaos — The Predictability Limit

Edward Lorenz (1963) discovered deterministic chaos in a simplified atmospheric convection model. Key implications:

```
LORENZ ATTRACTOR:
  Small changes in initial state → large changes in final state
  Error growth is EXPONENTIAL:
    δ(t) = δ₀ × e^(λt)
    where λ = Lyapunov exponent (>0 for chaotic system)

ATMOSPHERIC PREDICTABILITY:
  Error doubling time ~ 1–3 days (varies with flow regime)
  Beyond ~2 weeks: all deterministic skill is lost
  The 2-week limit is FUNDAMENTAL, not a technology limit

  "A butterfly in Brazil can set off a tornado in Texas"
  (Lorenz, 1972) — but the butterfly cannot be controlled,
  and the tornado prediction requires knowing EVERY butterfly.

PRACTICAL FORECASTING LIMITS:
  1–2 days: > 90% skill; excellent
  3–4 days: Good; major events well-captured
  5–7 days: Reasonable; synoptic patterns
  8–10 days: Low-confidence; ensemble needed
  11–14 days: Pattern/regime only; no specifics
  > 14 days: Climate tendencies only (seasonal/MJO/ENSO influence)
```

**Predictable exceptions** — some phenomena are more predictable: the MJO (30–90 day tropical wave) can extend forecast skill for certain variables to 3–4 weeks. El Niño/La Niña influences seasonal probabilities. Blocking events, once established, can be maintained in forecasts for longer.

---

## Decision Cheat Sheet

| Forecast question | Tool to use |
|------------------|-------------|
| 0–3 day forecast (specific location) | High-resolution deterministic (HRRR for US convection) |
| 3–7 day synoptic pattern | GFS, ECMWF; compare for confidence |
| 7–10+ day extended | ECMWF EPS ensemble mean/spread |
| Tropical cyclone track | Consensus (TVCA, FV3-GFS, ECMWF) |
| Probability of precipitation > threshold | Ensemble probability products |
| Week 2 pattern (e.g., warm/cold anomaly) | CPC Week 2 outlooks; ECMWF extended |
| Seasonal outlook (3-month) | CPC CAS/OIL; ENSO-based statistical models |

---

## Common Confusion Points

**Model resolution and accuracy** — Resolution helps (resolving convection explicitly improves QPF) but is not the only factor. Physics parameterizations, data assimilation quality, and ensemble design matter equally. A 25-km model with better parameterizations can beat a 5-km model with poor ones.

**ECMWF is better than GFS in medium range, not always short range** — For 0–24 hour, high-resolution models tuned to specific regions (HRRR for US convection, UKmet for UK) may outperform ECMWF for specific applications. ECMWF's advantage is clearest for 5–10 day global forecasts.

**"The models disagree" in media** — When GFS and ECMWF show different scenarios, forecasters must use subjective judgment about which is more likely. High ensemble spread = high uncertainty = expect hedged public forecasts. This is not a model failure — it's the chaotic atmosphere being genuinely unpredictable.

**Bias correction (MOS)** — Raw NWP output is not directly issued as a forecast. Model Output Statistics (MOS) applies statistical corrections learned from model bias vs observations over many runs. Local effects (terrain, coast) are captured in MOS but not in model physics.
