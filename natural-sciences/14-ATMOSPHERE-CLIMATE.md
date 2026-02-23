# 14-ATMOSPHERE-CLIMATE — Atmospheric Science & Climate

> Atmospheric layers, radiation balance, greenhouse effect, global circulation,
> ocean-atmosphere coupling, climate forcing and feedbacks, and how GCMs work.
> The physics of why Earth has the climate it does — and why it's changing.

---

## Atmospheric Structure

```
LAYER          HEIGHT (km)   TEMP PROFILE   KEY PROCESSES
────────────────────────────────────────────────────────────────────
Troposphere    0–12 (avg)    Decreases      Weather, water cycle, CO₂/CH₄/N₂O
               0–8 (poles)   6.5°C/km       Convection, clouds, precipitation
               0–16 (tropics) (lapse rate)

Tropopause     12 km         Isothermal     Cold trap: water vapor freezes out
                                            → stratosphere stays dry

Stratosphere   12–50 km      INCREASES      Ozone absorbs UV → heating
                             ~1°C/km        Very stable (inversion): no convection
                                            Ozone layer 15–35 km (O₃ peak ~25 km)

Stratopause    50 km         Maximum

Mesosphere     50–85 km      Decreases      Coldest layer of atmosphere (−85°C)
                                            Meteors burn up here

Mesopause      85 km         Minimum        ~−90°C — coldest natural T on Earth

Thermosphere   85–600+ km    Increases      Absorbs X-ray/EUV; ions (ionosphere)
                             to 1000–2000°C Very low density → "hot" = few fast molecules

Exosphere      >600 km       —              Atoms escape to space; no clear boundary

COMPOSITION (dry): N₂ 78.1%, O₂ 20.9%, Ar 0.93%, CO₂ 0.042% (420 ppm, rising)
  Water vapor: 0–4% (highly variable, most important greenhouse gas by quantity)
```

---

## Radiation Balance

### The Energy Budget

```
INCOMING SOLAR:
  Solar constant: S₀ = 1361 W/m²
  Earth cross-section: πR²; surface area: 4πR²
  Average insolation: S₀/4 = 340 W/m²

  Planetary albedo: α ≈ 0.30 (30% reflected: clouds ~20%, surface ~10%)
  Absorbed solar: S₀(1−α)/4 = 238 W/m²

OUTGOING LONGWAVE RADIATION (OLR):
  Earth emits as approximate blackbody: F = εσT⁴
  At equilibrium: absorbed solar = OLR
  238 = σT_eff⁴  →  T_eff = 255 K = −18°C

  Actual surface temperature: ~288 K = +15°C
  Difference: 33°C = GREENHOUSE EFFECT

Greenhouse effect:
  Atmosphere transparent to solar shortwave (0.3–3 µm)
  Greenhouse gases absorb/re-emit terrestrial longwave (3–100 µm)
  Net: surface receives both solar + downwelling longwave radiation
  → surface warmer than T_eff
```

### Greenhouse Gases and Radiative Forcing

```
Gas         Concentration   Lifetime   GWP₁₀₀   Forcing contribution
──────────────────────────────────────────────────────────────────────
H₂O         0–4%           days       —         50% (largest! but feedback, not forcing)
CO₂         420 ppm        centuries  1         ~2.1 W/m² above pre-industrial
CH₄         1.9 ppm        ~12 yr     ~84        ~0.5 W/m²
N₂O         0.33 ppm       ~114 yr    ~273       ~0.2 W/m²
O₃ (trop.)  variable       weeks      —         ~0.4 W/m²
CFCs        ppt range      decades    thousands  ~0.3 W/m² (also O₃ depleting)

GWP = global warming potential (vs CO₂ over 100-year horizon)
Radiative forcing (RF): change in net irradiance at tropopause (W/m²)
  RF from CO₂: ΔF ≈ 5.35 × ln(C/C₀) W/m²   (logarithmic, not linear!)
  Doubling CO₂ (C₀→2C₀): ΔF = 3.7 W/m²

Molecular basis of greenhouse absorption:
  Only molecules with oscillating dipole moment absorb IR
  CO₂: symmetric stretch (IR inactive); asymmetric stretch + bend (IR active)
  H₂O: polar → all modes IR active → broadband absorber
  N₂, O₂: no dipole → IR transparent (but dominate atmosphere by mass)
```

### Atmospheric Windows

```
WAVELENGTH (µm)   TRANSMISSION   KEY ABSORBERS
0.3–0.7           High           Visible light passes through (why sky is bright)
0.7–3             Moderate       Some H₂O absorption bands
3–5               Low            CO₂, H₂O
8–12              WINDOW         Relatively transparent → surface IR escapes directly
                                 Clouds close this window
12–100            Low            H₂O, CO₂, O₃

The 8–12 µm window: key to cooling
  CO₂ band: 14–16 µm (outside window)
  CH₄ band: 3.3 + 7.7 µm (partially in window → higher GWP than CO₂ per molecule)
  Closing the window with more GHGs → more warming
```

---

## Atmospheric Photochemistry

### Ozone Layer

```
Chapman mechanism (stratospheric O₃ production):
  O₂ + hν (λ < 242 nm) → 2O      (photolysis)
  O + O₂ + M → O₃ + M           (three-body recombination)
  O₃ + hν (λ 200–300 nm) → O + O₂ (photolysis)
  O + O₃ → 2O₂                  (termination)

Net: UV radiation balanced by O₃ production
  UV-B (280–315 nm) and UV-C (<280 nm) mostly absorbed

CFC (chlorofluorocarbon) destruction mechanism:
  CF₂Cl₂ + hν → CF₂Cl• + Cl•   (photolysis in stratosphere)
  Cl• + O₃ → ClO• + O₂          (catalytic destruction)
  ClO• + O → Cl• + O₂           (Cl• regenerated → chain reaction)
  Net: O₃ + O → 2O₂,   one Cl• destroys ~100,000 O₃ molecules

Montreal Protocol (1987): phase-out of CFCs → O₃ recovery underway (~2065 full recovery)
Antarctic ozone hole: polar stratospheric clouds (PSCs) at −78°C → heterogeneous
  chemistry activates chlorine → spring depletion when sunlight returns
```

---

## Global Atmospheric Circulation

### Pressure and Wind Patterns

```
HADLEY CELLS (0°–30° latitude):
  Equatorial ITCZ (Intertropical Convergence Zone):
    Intense solar heating → rising moist air → thunderstorms → tropical rainforests
  Upper troposphere divergence → poleward flow
  Subtropical descending branch (~30°N/S):
    Adiabatic warming on descent → dry → deserts (Sahara, Arabian, Atacama, Australian)
  Low-level return flow: trade winds (NE in N. hemisphere, SE in S. hemisphere)

FERREL CELLS (30°–60°):
  Thermally indirect (driven by eddy momentum flux from Hadley + Polar cells)
  Surface westerlies (prevailing winds of mid-latitudes)
  Less organized than Hadley cells

POLAR CELLS (60°–90°):
  Cold air sinks at poles → outflows as polar easterlies → converges at ~60° → rises

CORIOLIS EFFECT:
  F_Cor = −2Ω × v   (Ω = Earth's angular velocity, v = wind velocity)
  Deflects flow rightward in N. hemisphere, leftward in S. hemisphere
  Responsible for: trade wind direction, cyclone rotation, geostrophic winds
  Strength: zero at equator, maximum at poles → Coriolis parameter f = 2Ω sin(φ)
```

### Jet Streams

```
Subtropical jet (~30°N/S, ~12 km): marks poleward edge of Hadley cell
  Speed: 100–200 km/h; persistent, narrow

Polar front jet (~60°N/S, ~10 km): thermal wind along temperature gradient
  Meanders as Rossby waves (planetary waves); position determines mid-lat weather

Thermal wind relation:
  ∂v_g/∂z = (g/fT) ∂T/∂y    (geostrophic wind increases with height in proportion to horizontal T gradient)
  Jet streams are the vertical integral of pole-equator temperature gradient

Rossby waves:
  Planetary-scale westerly meanders (wavelength ~5000 km)
  Quasi-stationary if phase speed = mean flow → blocking events → persistent heatwaves/cold snaps
  Driven by: land-sea temperature contrast, topography, latent heat
```

---

## Ocean-Atmosphere Coupling

### Thermohaline Circulation (THC / AMOC)

```
Global overturning circulation driven by density differences:
  Density = f(temperature, salinity): ρ ≈ ρ₀(1 − α_T(T−T₀) + β_S(S−S₀))

Atlantic Meridional Overturning Circulation (AMOC):
  Warm salty surface water flows N in Atlantic → Gulf Stream
  North Atlantic: cooled by atmosphere → dense → SINKS → North Atlantic Deep Water (NADW)
  Southward return flow at depth → upwells in Southern Ocean + Pacific/Indian
  Return at surface: ~1000-year round trip (conveyor belt)

AMOC transports ~17 Sv (sverdrups; 1 Sv = 10⁶ m³/s) northward
  Carries ~1.3 PW of heat to N. Europe (why London ~15°C warmer than same latitude in Canada)

Climate sensitivity of AMOC:
  Freshwater from melting Greenland → reduces salinity → reduces sinking → weakens AMOC
  Potential tipping point: AMOC collapse → rapid (decades) cooling in N. Atlantic + Europe
  Palaeoclimate evidence: Younger Dryas (~12,900–11,700 yr BP) — abrupt cooling ~10°C in decades
    Caused by: meltwater flood from Lake Agassiz → N. Atlantic freshwater pulse → AMOC shutdown
```

### El Niño-Southern Oscillation (ENSO)

```
Normal (La Niña-like):
  Walker circulation: trade winds push warm water W → thermocline tilts
  Cold upwelling off Peru → productive Pacific → warm pool in western Pacific

El Niño:
  Trade winds weaken → warm water flows E → thermocline flattens
  Warm SST off Peru → atmospheric convection shifts E
  Global teleconnections: droughts in Australia/SE Asia, floods in Peru/Ecuador,
                          reduced hurricane activity in Atlantic, warmer winters in US/Canada

Southern Oscillation Index (SOI): pressure difference Tahiti − Darwin
  El Niño: SOI negative (Tahiti high, Darwin low)
  La Niña: SOI positive

ENSO periodicity: ~2–7 years (irregular), strongest interannual climate signal
Predictability: ~6–12 months ahead (coupled ocean-atmosphere initialization)
```

---

## Climate Sensitivity and Feedbacks

### Climate Sensitivity

```
Equilibrium Climate Sensitivity (ECS): temperature change from doubled CO₂ at new equilibrium
  Best estimate: ~3°C (2.5–4°C likely range, IPCC AR6)
  Transient Climate Response (TCR): ~1.8°C (smaller; ocean heat uptake not yet equilibrated)

ΔT = λ × RF    (λ = climate sensitivity parameter ~0.8 K/W/m²)
RF from 2×CO₂ ≈ 3.7 W/m²  →  ΔT ≈ 3°C
```

### Feedback Mechanisms

```
POSITIVE FEEDBACKS (amplify warming):
  Water vapor: warming → more evaporation → more H₂O (strong GHG) → more warming
               Amplification factor: ~2× (most important positive feedback)
  Ice-albedo: warming → ice melts → lower albedo → more solar absorption → more warming
              Arctic amplification: 2–4× global average warming in Arctic
  Planck (blackbody): warming → more OLR → negative feedback (stabilizing) — the main restoring force
  Lapse rate: warming changes vertical T profile → partially offsets H₂O feedback in tropics
  Cloud feedback: UNCERTAIN — low clouds (negative, reflect solar) vs high clouds (positive, trap IR)
                  Net cloud feedback: slightly positive (~+0.4 W/m²/K) per CMIP6 models

NEGATIVE FEEDBACKS (stabilize):
  Planck (blackbody): primary restoring force (T⁴ → OLR increases rapidly with T)
  Vegetation/carbon cycle: complex; generally stabilizing on long timescales

Feedback factor:
  f = 1/(1 − Σfᵢ)   where fᵢ = individual feedback parameter/Planck feedback
  Planck alone: f = 1 (no amplification)
  With all feedbacks: f ≈ 2.5–3 → 3°C sensitivity
```

---

## General Circulation Models (GCMs)

### Architecture

```
DISCRETIZATION:
  Horizontal: spectral transform (~50–100 km resolution) or finite difference/volume
  Vertical: 30–100+ levels (pressure coordinates); hybrid σ-pressure near surface
  Timestep: 20–30 min (atmosphere), hours (ocean)

GOVERNING EQUATIONS (primitive equations):
  Momentum (Navier-Stokes + Coriolis + hydrostatic approx):
    ∂u/∂t = −v·∇u + fv − (1/ρ)∂p/∂x + Fᵤ
    ∂v/∂t = −v·∇v − fu − (1/ρ)∂p/∂y + Fᵥ
  Hydrostatic: ∂p/∂z = −ρg
  Thermodynamic energy: ∂T/∂t = −v·∇T + (κ/ρcₚ)∂²T/∂z² + Q_rad + Q_conv
  Continuity: ∇·(ρv) + ∂ρ/∂t = 0
  Water vapor: ∂q/∂t = −v·∇q + E − P + diffusion

PARAMETERIZATIONS (sub-grid processes):
  Convection: mass flux schemes (Arakawa-Schubert, Zhang-McFarlane)
  Boundary layer: turbulent mixing, surface fluxes
  Radiation: two-stream approximation, correlated-k for gas absorption
  Clouds: microphysics schemes (droplet activation, ice nucleation)
  Ocean coupling: SST, sea ice, AMOC (in coupled models)

ESMs (Earth System Models): add biogeochemistry, land surface, aerosols, ice sheets
```

### Why GCMs Are Hard

```
Scale problem: cloud microphysics (µm) → planetary circulation (10,000 km)
  Can't resolve both → must parameterize subgrid processes
  Parameterization errors → systematic biases

Butterfly effect: atmosphere chaotic beyond ~2 weeks (Lorenz, 1963)
  → ensemble approaches (many runs) for probabilistic forecasts
  → climate statistics predictable even though individual weather events aren't

Model validation:
  Historical runs: reproduce observed 20th century warming? (yes, broadly)
  Paleoclimate tests: Last Glacial Maximum, Eocene, Pliocene
  Emergent constraints: observed correlations constrain uncertain parameters
```

---

## Decision Cheat Sheet

| Question | Concept | Key number/relation |
|----------|---------|---------------------|
| What is Earth's effective temperature without greenhouse effect? | Radiation balance | 255 K (−18°C); actual 288 K → 33°C warming from GHE |
| Why is the stratosphere stable? | Temperature inversion | Temperature increases with height → inhibits convection |
| Why are trade winds easterly? | Hadley cell + Coriolis | Surface return flow deflected by Coriolis to become NE/SE |
| Why does CO₂ have log forcing? | Beer-Lambert saturation | ΔF ≈ 5.35 ln(C/C₀); main CO₂ bands partially saturated |
| What is climate sensitivity? | ECS | ~3°C per CO₂ doubling (likely range 2.5–4°C) |
| What drives AMOC? | Thermohaline | Salinity + temperature → density → deep water formation |
| Why is the Antarctic ozone hole in spring? | Polar stratospheric clouds | PSCs in winter → activate Cl; sunlight in spring triggers catalytic destruction |
| Why does El Niño affect global weather? | Teleconnections | Warm Pacific SST shifts Hadley circulation → precipitation pattern changes globally |
| What is the biggest uncertainty in climate models? | Cloud feedback | Low cloud response to warming uncertain in sign and magnitude |

---

## Common Confusion Points

**Weather and climate are different timescales but same physics**
Weather = specific atmospheric state (deterministic limit ~2 weeks, Lorenz chaos).
Climate = statistical distribution of weather (predictable trends over decades).
The same equations govern both. "Climate is what you expect, weather is what you get."
Climate change shifts the distribution — makes certain extremes more probable.

**CO₂ forcing is logarithmic, not linear**
Each doubling of CO₂ gives approximately the same forcing (~3.7 W/m²).
Going from 280 → 560 ppm: +3.7 W/m². Going from 560 → 1120 ppm: another +3.7 W/m².
This is because CO₂ absorption bands partially saturate — additional CO₂ affects
the wings of the bands rather than the already-opaque center.

**Water vapor is a feedback, not a forcing**
Water vapor is the strongest greenhouse gas (~50% of total GHE).
But atmospheric H₂O is controlled by temperature (saturation vapor pressure).
It doesn't accumulate independently — it responds to other forcings.
Adding CO₂ → warming → more H₂O → more warming (positive feedback, ~2× amplification).

**"The greenhouse effect" is not a catastrophe — it's necessary for life**
Without any greenhouse effect: Earth = 255 K = −18°C (frozen).
The current GHE provides +33°C to reach +15°C (habitable).
The problem is the ENHANCED greenhouse effect from anthropogenic GHG additions —
a perturbation on top of the natural GHE, shifting a stable system.

**Ice cores show CO₂ lagging temperature — does this disprove causation?**
In orbital (Milankovitch) cycles: orbital forcing → warming → CO₂ releases from ocean
→ CO₂ amplifies warming (positive feedback). CO₂ lags by ~1000 years.
This is CO₂ acting as a feedback, which is consistent with it also being a forcing.
The Antarctic ice core lag does not say CO₂ can't cause warming — it says
that in glacial cycles, temperature led. Causation can run in both directions.
