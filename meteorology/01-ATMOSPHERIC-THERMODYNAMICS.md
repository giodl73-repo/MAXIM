# Atmospheric Thermodynamics — Stability, Lapse Rates, CAPE

## The Big Picture

Atmospheric thermodynamics governs whether air parcels rise or sink — the fundamental question determining where convection (thunderstorms, clouds) occurs and where the atmosphere is stable. The core framework is parcel theory: track a hypothetical air parcel lifted through the environment and ask whether it is buoyant (continues rising) or negatively buoyant (sinks back).

```
+---------------------------------------------------------------+
|              STABILITY DECISION FRAMEWORK                     |
|                                                               |
|  Take an air parcel, lift it by some amount dz                |
|                                                               |
|  Compare parcel temperature to environment temperature:       |
|                                                               |
|  T_parcel > T_environment  →  parcel WARMER than surroundings |
|                               →  less dense, BUOYANT          |
|                               →  UNSTABLE, rises freely       |
|                                                               |
|  T_parcel < T_environment  →  parcel COOLER than surroundings |
|                               →  denser, negatively buoyant   |
|                               →  STABLE, sinks back           |
|                                                               |
|  T_parcel = T_environment  →  NEUTRAL stability               |
+---------------------------------------------------------------+
```

---

## Lapse Rates — How Temperature Changes with Altitude

**Environmental Lapse Rate (ELR)** = measured temperature decrease with altitude in the actual atmosphere. Averages ~6.5°C/km in the standard atmosphere, but varies enormously with time, place, season.

**Dry Adiabatic Lapse Rate (DALR)** = rate at which an unsaturated air parcel cools when lifted (or warms when lowered) without exchanging heat with surroundings.

```
DALR = g/cp = 9.8°C/km ≈ 10°C/km (dry parcel)
```

Derived from: dT/dz = -g/cp where g = 9.8 m/s², cp = ~1004 J/(kg·K)

**Saturated Adiabatic Lapse Rate (SALR)** = rate of temperature change for a *saturated* parcel being lifted. Condensation releases latent heat, partially offsetting cooling.

```
SALR ≈ 4–9°C/km (variable; depends on T)
     ~ 4°C/km in warm, humid tropical air (lots of condensation)
     ~ 9°C/km in cold air (little condensation)
```

### Stability Classification

```
Environmental Lapse Rate (ELR) compared to DALR and SALR:

ELR < SALR:        ABSOLUTELY STABLE
                   Even saturated parcel sinks back
                   → No convection possible

SALR < ELR < DALR: CONDITIONALLY UNSTABLE
                   Dry parcel: stable
                   Saturated parcel: unstable
                   → If lifted past LCL, will continue rising
                   → Most common condition in atmosphere

ELR > DALR:        ABSOLUTELY UNSTABLE
                   Even dry parcel rises freely
                   → Rare; usually eliminates itself quickly
                   through convective overturning

Special case:
ELR = 0 (isothermal) or ELR < 0 (temp increases with height):
INVERSION — strongest stability; lid on convection
```

---

## Parcel Lifting — Key Levels on a Sounding

```
HEIGHT
  |         EL (Equilibrium Level) ← top of storm; parcel as cold as env
  |         |          ← CAPE = positive area between LFC and EL
  |         |         /
  |         |        /   Parcel temp > Environmental temp
  |         |       /    → FREE CONVECTION
  |         |      /
  |      LFC (Level of Free Convection) ← parcel first becomes buoyant
  |         |
  |         | ← CIN (negative area; "cap" lid on convection)
  |         |
  |      LCL (Lifting Condensation Level) ← condensation starts; cloud base
  |         |
  |         |  (parcel lifted mechanically: front, orography, etc.)
  |
  SURFACE   ← parcel starts here
```

**LCL (Lifting Condensation Level)** — altitude where parcel cools to dewpoint → saturation → cloud base forms. Approximately: LCL (m) ≈ 125 × (T - Td) where T = surface temperature, Td = dewpoint (°C).

**LFC (Level of Free Convection)** — altitude above LCL where parcel first becomes warmer than environment → self-sustaining convection begins. Requires overcoming the CIN cap first.

**EL (Equilibrium Level)** — altitude where buoyant parcel cools back to environmental temperature → convection stops. Corresponds approximately to cloud top of deep convective systems.

---

## CAPE and CIN — The Energy Budget

**CAPE (Convective Available Potential Energy)** = integrated positive buoyancy from LFC to EL. Units: J/kg.

```
CAPE = integral from LFC to EL of: g × (Tv_parcel - Tv_env) / Tv_env × dz

CAPE VALUES AND INTERPRETATION:
< 300 J/kg    Little/no CAPE        → At most weak showers
300–1000      Moderate              → Ordinary thunderstorms possible
1000–2500     Large                 → Strong thunderstorms, hail
2500–3500     Very large            → Severe thunderstorms, large hail
> 3500        Extreme               → Potential supercell + tornadoes
```

**CIN (Convective Inhibition)** = integrated negative buoyancy from surface to LFC. Units: J/kg (negative value).

```
CIN:
Small (0 to -50 J/kg)    → Easy to overcome; storms fire readily
                             (but may lack organization)
Moderate (-50 to -200)   → Cap; storms fire when cap is eroded
                             or overcome by forcing → explosive
                             development (classic "loaded gun"
                             severe weather setup)
Large (> -200 J/kg)      → Cap too strong; storms suppressed
                             even with forcing
```

**The "loaded gun" sounding** — high CAPE + moderate CIN + wind shear = severe weather setup. The cap (CIN) prevents premature convection, allowing CAPE to build. When the cap breaks, dramatic explosive development occurs. Classic setup for Great Plains severe outbreaks.

---

## Thermodynamic Diagrams — The Skew-T Log-P

The standard tool for analyzing atmospheric soundings:

```
SKEW-T LOG-P DIAGRAM ELEMENTS:
Y-axis: log(pressure) — height proxy
X-axis: temperature, but isotherms are SKEWED to the right

LINES:
  Solid vertical (nearly): Temperature of environment (T profile)
  Dashed (parallel, skewed): Dewpoint profile (Td profile)
  Dry adiabats: lines along which unsaturated parcel moves (DALR)
  Saturated adiabats: lines along which saturated parcel moves (SALR)
  Mixing ratio lines: constant specific humidity lines

READ FROM:
  LCL: Where T and Td lines converge
  LFC: Where lifted parcel (following DALR then SALR) crosses T profile
  EL:  Where lifted parcel (SALR) returns to T profile at top
  CAPE: Positive area between parcel path and environment T
  CIN:  Negative area (parcel colder than environment below LFC)
  Wind: Barbs plotted on the right side at each level
```

---

## Potential Temperature and Equivalent Potential Temperature

**Potential temperature θ** — temperature a parcel would have if brought adiabatically to 1000 mb:

```
θ = T × (1000/P)^(R/cp)   [Kelvin; P in mb]
```

θ is conserved for dry adiabatic processes. In a stable atmosphere, θ increases with altitude. In a well-mixed boundary layer, θ is constant (mixed layer = "θ = constant").

**Equivalent potential temperature θₑ** — also includes moisture content (adds latent heat from condensation). Conserved for moist adiabatic processes. Used to identify air mass boundaries (fronts appear as θₑ gradients).

---

## Temperature Inversions

An inversion = temperature increases with height (ELR < 0). Inversions suppress convection by acting as a "lid":

```
INVERSION TYPE        CAUSE                          SIGNIFICANCE
------------------    ----------------------------   --------------------
Radiation inversion   Surface cools at night by      Morning fog, smog;
                      longwave emission; cold         eliminates by
                      surface chills air above it     afternoon

Subsidence inversion  Descending (sinking) air        Persistent marine
(marine layer)        warms adiabatically; creates    stratus (California
                      lid on surface layer            coast); poor air
                                                       quality episodes

Frontal inversion     Warm air overrides cold air     Marks frontal surface;
                      at frontal slope                stratiform clouds below

Trade wind inversion  Descending branch of Hadley     Limits trade wind
                      cell warms at ~1.5–2 km         cumulus; defines top
                                                       of cloud layer in
                                                       tropics
```

---

## Decision Cheat Sheet

| Condition | Implication |
|-----------|-------------|
| ELR > DALR (10°C/km) | Absolutely unstable; convective overturning inevitable |
| ELR between SALR and DALR | Conditionally unstable; most common |
| Strong temperature inversion | Lid; convection suppressed |
| High CAPE (>2500 J/kg) + moderate CIN | "Loaded gun" severe weather setup |
| LCL – surface separation large (Td much lower than T) | Dry air; high cloud bases; downdraft evaporation → microbursts |
| LCL near surface (T ≈ Td) | Humid; low cloud bases; fog potential |

---

## Common Confusion Points

**DALR vs SALR** — The DALR (~10°C/km) applies to unsaturated air; once condensation starts, latent heat is released, so the parcel cools more slowly: SALR (~4–9°C/km). The DALR is a constant; the SALR varies with temperature because warmer air holds more moisture and releases more latent heat.

**CAPE units and vertical velocity** — CAPE in J/kg relates to maximum updraft speed by: w_max ≈ √(2×CAPE). With 3000 J/kg CAPE: w_max ≈ √6000 ≈ 77 m/s ≈ 280 km/h. Actual updrafts are lower due to entrainment of environmental air (dilution of buoyancy).

**CIN is necessary for big storms** — Counterintuitively, you need *some* CIN for severe weather. Zero CIN means convection fires continuously but remains weak and disorganized. Moderate CIN allows CAPE to accumulate; when CIN breaks, explosive development occurs.

**Adiabatic ≠ no heat exchange everywhere** — "Adiabatic" means no heat exchange with surroundings. But condensation within the parcel releases latent heat — that's internal heat exchange within the parcel itself. The SALR is still "adiabatic" in the sense of no exchange with the environment.
