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

<!-- @editor[bridge/P2]: No computational bridge for the learner — meteorology is applied PDE solving (Navier-Stokes), optimization (data assimilation), and chaos theory. A 3-sentence bridge here connecting "atmosphere as a system" to the math/CS concepts that govern it would orient an MIT TCS reader powerfully -->
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

<!-- @editor[structure/P1]: Missing Decision Cheat Sheet section — "which guide do I read for X?" table would orient the reader -->
## Common Confusion Points

**Weather vs climate** — Weather is the atmospheric state at a specific time and place; climate is the statistical distribution of that state over decades. "Climate is what you expect; weather is what you get." A heat wave is weather; an increasing trend in heat wave frequency is climate.

**Atmosphere thickness illusion** — The atmosphere looks thick in photos from orbit but is extremely thin relative to Earth: 99% of atmospheric mass is below 30 km altitude, yet Earth's radius is 6,371 km. The ratio is ~0.005. If Earth were a basketball, the weather-making atmosphere would be 0.1 mm thick.

**Pressure decreases exponentially with altitude** — The pressure scale height is ~8 km (pressure halves every ~5.5 km). At Denver (1.6 km), pressure is ~83% of sea level. At Mt. Everest (8.8 km), it's ~33%. There's no abrupt "edge" — just exponential thinning.
