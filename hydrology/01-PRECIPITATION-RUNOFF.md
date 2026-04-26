# Precipitation and Runoff — Rainfall-Runoff Mechanics, Infiltration, SCS Curve Number, Unit Hydrograph

## The Big Picture

```
+===========================================================================+
|                   RAINFALL-RUNOFF PROCESS                                 |
|       From precipitation to stream hydrograph                             |
+===========================================================================+
|                                                                           |
|  RAINFALL                                                                 |
|     │ Interception (forest canopy: 10–40%)                               |
|     │ Evaporation from wet surfaces                                       |
|     ▼                                                                     |
|  NET PRECIPITATION (throughfall + stemflow + direct on bare soil)         |
|     │                                                                     |
|     ├──► INFILTRATION into soil surface                                   |
|     │        │                                                            |
|     │        ├──► SOIL WATER (storage, ET by plants)                     |
|     │        │                                                            |
|     │        └──► PERCOLATION to groundwater (recharge)                  |
|     │                    │                                                |
|     │                    └──► BASEFLOW to streams (slow, days–months)    |
|     │                                                                     |
|     └──► EXCESS RAINFALL when rainfall > infiltration rate               |
|              │ (Hortonian overland flow)                                  |
|              OR when soil is saturated                                    |
|              │ (saturation excess overland flow — Dunne mechanism)        |
|              ▼                                                            |
|         DIRECT RUNOFF → storm hydrograph → channel flow                  |
+===========================================================================+
```

---

## Precipitation Types and Measurement

```
PRECIPITATION FORMATION:
  Orographic: air forced upward by terrain → cools → condenses
    → windward side wet, leeward side "rain shadow" (dry)
  Convective: surface heating → unstable air rises → thunderstorms
    → intense, localized, short duration
  Frontal/cyclonic: warm/cold front boundary lifting
    → widespread, moderate intensity, longer duration

MEASUREMENT:
  Rain gauge: direct measurement, 0.2–0.25 mm tipping bucket resolution
  Radar (WSR-88D, Doppler): reflectivity → rainfall rate (Z-R relationship)
    Coverage: 200–300 km radius, 5-min updates
    Error sources: bright band, terrain blocking, partial beam blockage
  Satellite: TRMM (1998–2015), GPM (2014–): passive microwave + radar
    Global 0.1° resolution; 3-hourly data (IMERG product)

SPATIAL AVERAGING METHODS:
  Thiessen polygons: weight each gauge by its area of influence
  Inverse distance weighting: IDW, simple, widely used
  Kriging: geostatistical interpolation, optimal linear unbiased estimator
  (Kriging is standard optimal spatial interpolation — same math as Gaussian process regression)
```

---

## Infiltration Theory

### Horton's Infiltration Capacity Model

```
HORTON (1933):
  Infiltration capacity f_c decreases exponentially from initial rate f_0 to
  final rate f_c (saturated hydraulic conductivity K_s):

  f(t) = f_c + (f_0 - f_c) exp(-kt)

  f_0 = initial infiltration rate (dry soil): 25–250 mm/hr (varies widely)
  f_c = final saturated rate: 0.5–50 mm/hr (depends on soil type)
  k   = decay constant (typically 2–5 hr⁻¹)

  Hortonian overland flow: rainfall rate i > f_c → ponding → overland flow
  Common in: urban areas, crusted agricultural soils, arid systems

GREEN-AMPT MODEL (1911, physically-based):
  Piston-flow assumption: sharp wetting front advances into dry soil

  f(t) = K_s [1 + (ψ_f ΔΘ)/F(t)]

  where K_s = saturated K, ψ_f = capillary suction at wetting front,
        ΔΘ = soil moisture deficit, F(t) = cumulative infiltration

  More physically meaningful — relates to measurable soil properties
  Used in Green-Ampt model for design storms
```

### Soil Water and Soil Moisture States

```
SOIL WATER STATES:
  Saturation:        all pores filled, ψ = 0
  Field capacity:    after gravity drainage (1–3 days), ψ ≈ -33 kPa (clay) to -10 kPa (sand)
  Wilting point:     plant-unavailable water, ψ ≈ -1500 kPa
  Plant available:   field capacity − wilting point → "available water capacity"

  Typical values (volumetric water content θ, m³/m³):
    Sand:    saturation 0.45, field capacity 0.10, wilting 0.04
    Clay:    saturation 0.55, field capacity 0.40, wilting 0.25
    Loam:    saturation 0.50, field capacity 0.30, wilting 0.15

HYDRAULIC CONDUCTIVITY K:
  Saturated K (K_s): depends strongly on soil texture and structure
    Gravel: 10,000 mm/hr
    Sand:   100–1000 mm/hr
    Loam:   10–50 mm/hr
    Clay:   0.5–5 mm/hr

  Unsaturated K(ψ): decreases dramatically as soil dries
    At wilting point: K ≈ 10⁻⁶ of K_s → essentially impermeable
```

---

## SCS (NRCS) Curve Number Method

```
CURVE NUMBER (CN) METHOD — Soil Conservation Service 1954, now NRCS

PURPOSE: Estimate direct runoff from a storm rainfall event
UBIQUITY: Used for virtually all stormwater and design applications in US

CORE EQUATION:
  Q = (P - Ia)² / (P - Ia + S)     for P > Ia
  Q = 0                              for P ≤ Ia

  Q = direct runoff (mm or inches)
  P = rainfall (mm or inches)
  Ia = initial abstraction = 0.2S (standard assumption)
  S = maximum potential retention = 25400/CN - 254  (mm, for SI)

  CN ranges from 0 (perfect absorption) to 100 (total runoff = rainfall)

CN DETERMINATION:
  Depends on: HSG (Hydrologic Soil Group) + land cover/use + antecedent moisture

  HYDROLOGIC SOIL GROUP:
    A: Low runoff potential (sand, gravel, deep soils, high infiltration)
       CN ~ 30–40 for natural areas
    B: Moderately low runoff potential
       CN ~ 40–55 for natural areas
    C: Moderately high runoff potential
       CN ~ 55–70 for natural areas
    D: High runoff potential (clay, shallow soils, high water table)
       CN ~ 70–80 for natural areas

  LAND USE EFFECT ON CN (for HSG C):
    Open water:          CN = 100
    Impervious surface:  CN = 98
    Commercial/industrial: CN = 94
    Residential (1/4 acre lots): CN = 83
    Agricultural cropland: CN = 72
    Meadow/grass:          CN = 71
    Forest (good):         CN = 70
    Undisturbed woodland:  CN = 55

ANTECEDENT MOISTURE CONDITION:
  AMC I (dry):   subtract ~15–20 from table CN
  AMC II (normal): use table CN
  AMC III (wet):  add ~15–20 to table CN

EXAMPLE:
  P = 100 mm, CN = 80 (medium-density residential, HSG C)
  S = 25400/80 - 254 = 63.5 mm
  Ia = 0.2 × 63.5 = 12.7 mm
  Q = (100 - 12.7)² / (100 - 12.7 + 63.5) = 87.3² / 150.8 = 50.6 mm
  Runoff ratio: 50.6/100 = 50.6%
```

---

## Unit Hydrograph Theory

```
UNIT HYDROGRAPH (UH) — Sherman (1932)

CONCEPT:
  Standardized direct runoff hydrograph from 1 unit of direct runoff depth
  (typically 1 mm or 1 inch over the catchment) produced by a rainfall
  of unit duration.

THREE ASSUMPTIONS:
  1. PROPORTIONALITY: Q ∝ rainfall excess (2× rainfall → 2× hydrograph at each time)
  2. TIME INVARIANCE: same storm, same season → same hydrograph shape
  3. LINEAR SUPERPOSITION: direct runoffs from separate time periods add linearly

DERIVATION:
  Observed stream hydrograph from known rainfall → subtract baseflow →
  direct runoff hydrograph → divide by observed rainfall excess depth →
  unit hydrograph

CONVOLUTION (apply UH to design storm):
  Divide design storm into incremental periods
  For each period: U(t) × Qi = contribution to hydrograph
  Sum all contributions at each time step (linear convolution)
  Add baseflow → design storm hydrograph

  THIS IS DIGITAL SIGNAL PROCESSING:
  Direct runoff Q = UH ⊛ rainfall excess P (discrete convolution)
  Same math as impulse response in linear systems theory
  UH is the unit impulse response of the catchment

SCS DIMENSIONLESS UNIT HYDROGRAPH:
  Synthetic UH (no observed data needed)
  Based on empirical data from many catchments
  Tp = (D/2) + Tlag
    D = storm duration, Tlag = lag time = 0.6 × Tc
    Tc = time of concentration (travel time through catchment)
  Peak: Qp = 0.208 × A / Tp  (m³/s per mm, A in km², Tp in hr)
```

---

## Hydrograph Components

```
STORM HYDROGRAPH ANATOMY:

       Q
       │                    PEAK DISCHARGE
       │                  ╱────────────────────
       │                ╱     RECESSION LIMB
       │              ╱
       │     RISING  ╱
       │      LIMB  ╱
       │           ╱
       │──────────╱────────────────────────────── baseflow
       │         ↑ BASEFLOW                        ↘
       └────────────────────────────────────────────── t
                  ↑                    ↑
               storm                 end of direct
               start                 runoff (baseflow only)

  BASEFLOW SEPARATION:
    Straight line method: draw line from start of rise to end of direct runoff
    Recession curve method: fit exponential decay to recession limb Q(t) = Q₀ exp(-t/k)
    Master recession curve: composite recession from many events

  HYDROGRAPH CHARACTERISTICS:
    Tc (time of concentration): time for water from furthest point to reach outlet
    Tp (time to peak): time from centroid of rainfall to peak flow
    T_r (recession time): time from peak to baseflow return
    Volume under hydrograph = total direct runoff volume (verify against CN estimate)
```

---

## Rational Method (Peak Flow)

```
RATIONAL METHOD (Mulvaney, 1850):
  Q = C × i × A / 360    (m³/s, with A in ha, i in mm/hr)
  Q = C × i × A          (for traditional US units: ft³/s, A in acres, i in in/hr)

  C = runoff coefficient (0.1–0.95)
  i = rainfall intensity (mm/hr) for duration = Tc (time of concentration)
  A = drainage area

  i from IDF (Intensity-Duration-Frequency) curves:
    IDF: intensity vs. duration for various return periods (10-yr, 25-yr, 100-yr)
    Each location has a unique IDF curve (NOAA Atlas 14 in US)

  ASSUMPTIONS:
    Steady-state: rainfall duration ≥ Tc (whole catchment contributing simultaneously)
    Uniform distribution of rainfall
    Constant C (fixed land use)
    Linear response

  VALIDITY: Small catchments (< 200 ha), urban drainage design
  LIMITATIONS: Doesn't capture storage, not valid for long-duration events
  ALTERNATIVE: SCS method for larger catchments and volume calculations

RUNOFF COEFFICIENTS C:
  Rooftops, pavement:   0.70–0.95
  Lawns (flat, clay):   0.25–0.35
  Business districts:   0.70–0.95
  Parks, cemeteries:    0.10–0.25
  Natural meadow:       0.10–0.20
  Forest:               0.10–0.20
```

---

## Snowmelt Hydrology

```
SNOW HYDROLOGY RELEVANCE:
  ~35% of global freshwater runoff comes from snowmelt
  Spring snowmelt dominates: western US, Alps, Himalayas, Scandinavia
  Warmer winters → earlier snowmelt → shifted timing → summer water deficit

DEGREE-DAY METHOD:
  Snowmelt rate M = Mf × (T_a - T_base)

  M  = melt rate (mm/day water equivalent)
  Mf = degree-day factor (mm/°C/day, typically 3–6 mm/°C/day)
       (varies: shaded forest 3, open clear sky 6)
  T_a = air temperature (°C)
  T_base = base temperature (0°C)

ENERGY BALANCE METHOD (more accurate):
  M = (Q_n + Q_h + Q_e + Q_g + Q_r) / (ρ_w × L_f)

  Q_n = net radiation, Q_h = sensible heat flux, Q_e = latent heat flux
  Q_g = ground heat flux, Q_r = rain heat flux
  L_f = latent heat of fusion (334 kJ/kg)

  Net radiation drives ~80% of snowmelt in most conditions.
  Rain on snow events: can rapidly melt large volumes → extreme floods
    (1950 "Rain on Snow" Pacific Northwest floods, European Alpine floods)

SWE (SNOW WATER EQUIVALENT):
  Mass of water in snowpack = depth × density / 1000
  Fresh snow: ρ ≈ 50–100 kg/m³ → 1 m snow = 50–100 mm SWE
  Settled old snow: ρ ≈ 400–600 kg/m³
  Measured by: snow courses (manual), automated snow pillows, airborne gamma
```

---

## Design Storm and IDF Curves

```
INTENSITY-DURATION-FREQUENCY (IDF) RELATIONSHIPS:
  For a given return period T (years) and duration D (minutes or hours):
    i = a / (D + b)^n     (empirical formula, region-specific coefficients)

  READING AN IDF CURVE:
    Horizontal axis: storm duration (5 min to 24 hr)
    Vertical axis: rainfall intensity (mm/hr or in/hr)
    Lines: return period (2-yr, 5-yr, 10-yr, 25-yr, 100-yr)

    For drainage design: choose return period = design standard (e.g., 10-yr for minor,
    100-yr for major system)
    Read intensity at duration = Tc of catchment → rational method Q peak

  DESIGN STORM TEMPORAL DISTRIBUTION:
    Chicago Design Storm: peaks near the middle of event (most common in US)
    Huff quartile distributions: peak in 1st, 2nd, 3rd, 4th quartile
    SCS 24-hr distributions: Type I (Pacific coast), Type II (most of US),
                              Type III (Gulf Coast, East Coast heavy rain)
```

---

## Bridges from CS and Engineering

```
RAINFALL-RUNOFF CONCEPT       CS / ENGINEERING EQUIVALENT
──────────────────────────────────────────────────────────────────────────────
Unit Hydrograph (UH)          LTI system impulse response
  Q(t) = UH ⊛ P_excess(t)      → discrete convolution (same as FIR filter)
  UH shape = catchment TF       → characterizes gain + timing at each frequency
  Superposition of periods      → linearity allows addition of responses
  Limitation (large storms)     → nonlinear regime; LTI breaks down
                                  (same as small-signal approximation in EE)

Kriging (spatial rainfall)    Gaussian process (GP) regression
  Variogram γ(h)                → covariance kernel as function of separation h
  Kriging system (linear eq.)   → GP posterior mean; same closed-form solution
  Kriging variance              → GP posterior variance (uncertainty estimate)
  "Optimal unbiased estimator"  → minimum MSE under stationarity assumption

Horton infiltration f(t)      First-order exponential decay
  f(t) = fc + (f0-fc)e^{-kt}   → RC discharge curve; k = 1/time constant
  "Saturated K" floor           → steady-state; equivalent to DC gain in a filter

Green-Ampt model              Moving boundary problem
  Sharp wetting front           → Stefan problem in heat conduction
  Capillary suction ψ_f         → surface tension as a driving potential

SCS Curve Number Q(P)         Nonlinear sigmoid mapping
  Q = (P - Ia)² / (P - Ia + S) → threshold + nonlinear amplification
  CN = 98 (impervious)          → near-unity gain; CN = 30 → heavy attenuation
  Antecedent moisture           → state-dependent gain (system with memory)

IDF Curves                    Extreme value statistics at fixed durations
  i = a/(D+b)^n                 → power-law tail; same form as Pareto-type EVT
  Return period T               → 1/P(exceedance) per year — not a fixed cycle
  Design storm selection        → threshold for acceptable tail risk

Snowmelt degree-day model     Linear threshold model
  M = Mf × max(T_a - 0, 0)     → ReLU activation; accumulates as integral
  SWE as state variable         → integrator (running sum of melt increments)
```

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| What is Hortonian vs. Dunne overland flow? | Hortonian: rain > infiltration rate; Dunne: saturation excess (soil full) |
| What CN means? | Higher CN → more runoff; CN=100 → all rain runs off; CN=30 → little runoff |
| How does forest affect runoff? | Lower CN (interception, high infiltration) → less runoff vs. cropland or urban |
| What is a unit hydrograph? | Linear impulse response of a catchment to 1 mm of direct runoff — it's a transfer function |
| What is Tc? | Time of concentration — longest travel time from catchment edge to outlet |
| What is baseflow? | Groundwater discharge sustaining river between storms; slow recession curve |
| What are IDF curves? | Intensity-Duration-Frequency: rainfall intensity vs. storm duration for various return periods |
| What is SWE? | Snow Water Equivalent: water content of snowpack (depth × density) |

---

## Common Confusion Points

**CN is a property of soil AND land use AND antecedent moisture together**: The same soil type gets different CN values for forest vs. impervious surface vs. agricultural land. Urbanization increases CN dramatically — a meadow CN=55 becomes parking lot CN=98. The CN method is the most widely misused tool in hydrology because practitioners forget the antecedent moisture condition and use tabulated CN without site verification.

**Unit hydrograph linearity assumption**: The UH assumes proportionality and superposition — the same UH works for any storm. In reality, the assumption breaks down for large storms (channel storage and routing change), frozen ground, and antecedent moisture extremes. But it's a practical and useful linearization that works well for design flood estimation when data are limited.

**Rational method gives peak FLOW only, not volume**: The rational method Q = CiA gives peak discharge for use in pipe/culvert sizing. It does NOT give runoff volume or hydrograph shape. For volume calculations (reservoir design, storage sizing, water balance), use the CN method. Engineers sometimes confuse the two, leading to design errors.

**Baseflow is not from rain**: Baseflow is groundwater discharging to the stream. It sustains streamflow between rain events. In humid climates, baseflow may be 50–80% of annual streamflow. In arid climates, baseflow may be essentially zero (ephemeral streams). Baseflow can take months to years to respond to recharge events — it's the slow memory of the groundwater system.

**Evapotranspiration cannot exceed available energy**: Potential ET (the maximum if water is unlimited) is constrained by net radiation minus ground heat flux. In practice: ET ≤ Rn/λ (Rn = net radiation, λ = latent heat of vaporization). You cannot exceed this energy budget. Claims of ET > PET are physically impossible. Actual ET ≤ Potential ET ≤ Energy limit.
