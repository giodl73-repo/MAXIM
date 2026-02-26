# Meteorology — Overview

## The Big Picture

The atmosphere is a thin fluid shell (99% of mass below 30 km; Earth's radius is 6,371 km) driven by differential solar heating and shaped by Earth's rotation. Weather is the short-term state; climate is the long-term statistics. All of meteorology follows from fluid dynamics + thermodynamics applied to a rotating, stratified fluid on a sphere.

```
+------------------------------------------------------------------+
|                    ATMOSPHERE AS A SYSTEM                         |
|                                                                   |
|  ENERGY IN: Solar radiation (short-wave)                         |
|  ENERGY OUT: Longwave infrared + reflected short-wave            |
|                                                                   |
|  CIRCULATION ENGINES:                                            |
|  ┌─────────────────────────────────────────────────────┐         |
|  │ Differential heating (equator hot, poles cold)      │         |
|  │    ↓                                                │         |
|  │ Pressure gradients + Coriolis deflection            │         |
|  │    ↓                                                │         |
|  │ Hadley/Ferrel/Polar cells (mean circulation)        │         |
|  │    ↓                                                │         |
|  │ Jet streams, Rossby waves (synoptic variability)    │         |
|  │    ↓                                                │         |
|  │ Frontal systems, cyclones (weather systems)         │         |
|  └─────────────────────────────────────────────────────┘         |
|                                                                   |
|  WATER CYCLE: Evaporation → Condensation → Precipitation        |
|  (latent heat release = primary driver of thunderstorms)         |
+------------------------------------------------------------------+
```

---

## Atmospheric Layers

```
ALTITUDE (km)   LAYER          TEMP PROFILE        KEY FEATURE
--------------  -----------    ----------------    -------------------------
0–12 km         TROPOSPHERE    Decreases with alt  All weather; 75% of mass;
                               (~6.5°C/km)         well-mixed; tropopause top

12–50 km        STRATOSPHERE   Increases with alt  Ozone layer (15–35 km);
                               (UV absorption)     jet aircraft fly here;
                               -60°C to 0°C        very stable (no weather)

50–85 km        MESOSPHERE     Decreases with alt  Meteors burn up;
                               coldest point       noctilucent clouds
                               (-90°C at top)      at top

85–500 km       THERMOSPHERE   Increases (solar    Auroras; ISS orbit;
                               EUV absorption)     very low density

>500 km         EXOSPHERE      Gradual transition  Molecules escaping
                               to space            to space
```

**Tropopause height** — varies with latitude: ~16 km at tropics, ~10–12 km at mid-latitudes, ~8 km at poles. Higher tropopause over tropics = deeper convective storms possible there.

---

## Atmospheric Composition

```
GAS              VOLUME %    SOURCE           ROLE
---------------  ----------  ---------------  ---------------------------
N₂               78.08%      Biogenic         Largely inert; provides
                                               pressure
O₂               20.95%      Biogenic         Respiration; photochemistry
Ar               0.93%       Geogenic         Inert (primordial + K-40)
CO₂              0.042%      Biogenic+anthro  Primary greenhouse gas;
                 (420 ppm)                    photosynthesis
H₂O vapor        0–4%        Evaporation      Dominant greenhouse gas;
                 (variable)                   latent heat transport
O₃ (ozone)       0.000004%   Photochemical    UV shield in stratosphere
CH₄              0.00019%    Biogenic+anthro  Greenhouse gas (28×CO₂ GWP)
N₂O              0.000033%   Biogenic+anthro  Greenhouse gas (273×CO₂ GWP)
Aerosols         Trace        Various          Cloud condensation nuclei;
                                               direct radiative effects
```

---

## Weather vs Climate Scales

```
SCALE           TIME           SPACE          EXAMPLES
-----------     -----------    -----------    ----------------------------------
Micro           Seconds–       Meters         Turbulence, surface layer
                minutes
Mesoscale       Minutes–       1–1000 km      Thunderstorms, sea breezes,
(meso-α,β,γ)   hours                         mountain/valley winds
Synoptic        Hours–days     100–5000 km    Fronts, cyclones, anticyclones
                                              (the "weather map" scale)
Planetary/      Weeks–months   Global         Rossby waves, jet streams,
long-wave                                     teleconnections
Climatic        Decades–       Global         ENSO, PDO, ice ages
                centuries
```

---

## Global Circulation Cells

```
90°N  POLAR HIGH
      |
      | Polar Easterlies
60°N  POLAR FRONT + JET STREAM ← major storm track
      | Westerlies (Ferrel cell)
30°N  SUBTROPICAL HIGH ("horse latitudes") + jet stream
      | NE Trade Winds
 0°   ITCZ (Intertropical Convergence Zone) ← rainforests, deep convection
      | SE Trade Winds
30°S  SUBTROPICAL HIGH
      | Westerlies (Ferrel cell)
60°S  POLAR FRONT + JET STREAM
      |
90°S  POLAR HIGH
```

**Hadley cell** — heated equatorial air rises (ITCZ), flows poleward aloft, sinks at ~30° → subtropical deserts (Sahara, Arabian, Sonoran, Atacama, Australian). Trade winds are the surface return flow.

**Ferrel cell** — thermally indirect (mechanically driven by Hadley and Polar cells); mid-latitude westerlies.

**ITCZ migration** — follows the solar heating; moves northward in NH summer (bringing monsoon rains to South Asia, Sahel), southward in NH winter. Its position over continents vs oceans causes regional wet/dry seasonality.

---

## Computational Bridge

Meteorology is numerical PDE solving under chaos. The atmosphere obeys the Navier-Stokes equations on a rotating sphere — the same equations as computational fluid dynamics, constrained to a thin stratified shell. Data assimilation (4D-Var, EnKF) is Bayesian state estimation at 10⁹-variable scale: blend a prior (model forecast) with heterogeneous observations weighted by error covariances to produce the best initial condition. Ensemble forecasting is Monte Carlo uncertainty propagation through a deterministic chaotic system — the Lorenz attractor is not a metaphor, it is the actual dynamics. Teleconnections (ENSO, NAO) are the leading eigenvectors of spatiotemporal covariance matrices: PCA on global atmospheric fields. The hard 2-week predictability limit follows from positive Lyapunov exponents, not insufficient compute.

## Directory Map

| File | Core Concept |
|------|-------------|
| `01-ATMOSPHERIC-THERMODYNAMICS.md` | Stability, lapse rates, CAPE, parcel theory |
| `02-ATMOSPHERIC-DYNAMICS.md` | Forces, Coriolis, geostrophic balance, jet streams |
| `03-AIR-MASSES-FRONTS.md` | Air mass taxonomy, Norwegian cyclone model |
| `04-CYCLONES-ANTICYCLONES.md` | Extratropical cyclone lifecycle, vorticity |
| `05-PRECIPITATION-CLOUDS.md` | Bergeron-Findeisen, cloud classification |
| `06-SEVERE-WEATHER.md` | Supercells, tornadoes, tropical cyclones |
| `07-NUMERICAL-WEATHER-PREDICTION.md` | GFS vs ECMWF, ensemble, chaos limit |
| `08-OBSERVATION-SYSTEMS.md` | Radiosonde, Doppler radar, satellites |
| `09-TELECONNECTIONS.md` | ENSO, NAO, MJO — climate modes |

---

## Decision Cheat Sheet

| I need to... | Go to |
|---|---|
| Understand why the jet stream meanders | `02-ATMOSPHERIC-DYNAMICS.md` — Rossby waves, potential vorticity |
| Know how a mid-latitude cyclone develops | `04-CYCLONES-ANTICYCLONES.md` — vorticity, divergence |
| Understand why storms form where they do | `03-AIR-MASSES-FRONTS.md` — baroclinic zones |
| Know how NWP models actually work | `07-NUMERICAL-WEATHER-PREDICTION.md` — primitive equations, 4D-Var, ensemble |
| Understand why forecasts fail past 2 weeks | `07-NUMERICAL-WEATHER-PREDICTION.md` — Lorenz chaos, Lyapunov exponents |
| Know what the radar is showing | `08-OBSERVATION-SYSTEMS.md` — Doppler, dual-pol, NEXRAD |
| Understand seasonal climate signals (El Niño, etc.) | `09-TELECONNECTIONS.md` — ENSO, MJO, NAO |
| Understand why tornado alleys exist | `06-SEVERE-WEATHER.md` — supercell environments, wind shear |
| Know why CAPE and CIN matter | `01-ATMOSPHERIC-THERMODYNAMICS.md` — parcel theory, stability |

---

## Common Confusion Points

**Weather vs climate** — Weather is the atmospheric state at a specific time and place; climate is the statistical distribution of that state over decades. "Climate is what you expect; weather is what you get." A heat wave is weather; an increasing trend in heat wave frequency is climate.

**Atmosphere thickness illusion** — The atmosphere looks thick in photos from orbit but is extremely thin relative to Earth: 99% of atmospheric mass is below 30 km altitude, yet Earth's radius is 6,371 km. The ratio is ~0.005. If Earth were a basketball, the weather-making atmosphere would be 0.1 mm thick.

**Pressure decreases exponentially with altitude** — The pressure scale height is ~8 km (pressure halves every ~5.5 km). At Denver (1.6 km), pressure is ~83% of sea level. At Mt. Everest (8.8 km), it's ~33%. There's no abrupt "edge" — just exponential thinning.
