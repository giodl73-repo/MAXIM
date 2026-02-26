# Ocean Physics — Density Stratification, Thermocline, Halocline, Pycnocline, SOFAR Channel

## The Big Picture

```
+===========================================================================+
|                  OCEAN WATER COLUMN STRUCTURE                              |
|            Density stratification controls everything                      |
+===========================================================================+
|                                                                           |
|  SURFACE MIXED LAYER (0–100 m)                                            |
|  ─────────────────────────────                                            |
|  Wind mixing, wave breaking → well-mixed T and S                          |
|  Strong diurnal heating/cooling cycle                                     |
|  σt nearly uniform within layer                                           |
|                                                                           |
|  THERMOCLINE / PYCNOCLINE (100–1000 m)                                    |
|  ─────────────────────────────────────                                    |
|  Temperature drops sharply: 25°C → 4°C                                   |
|  Density increases sharply: stratification suppresses vertical mixing     |
|  Permanent thermocline in tropics; seasonal at mid-latitudes              |
|                                                                           |
|  DEEP WATER (1000 m to bottom)                                            |
|  ───────────────────────────────                                          |
|  T ≈ 1–4°C nearly uniform; slight increase with depth (adiabatic)        |
|  S variable by water mass history (NADW, AABW signatures)                 |
|  Very slow movement (mm/s to cm/s)                                        |
|                                                                           |
+===========================================================================+
```

---

## Density of Seawater — The Equation of State

The seawater equation of state ρ(T, S, P) is a thermodynamic PVT surface — the same concept as any equation of state in engineering thermodynamics, but parameterized empirically for seawater (TEOS-10: 44-coefficient polynomial). The Brunt-Väisälä frequency N = √[−(g/ρ₀)(∂ρ/∂z)] is directly analogous to a spring-mass oscillator: a water parcel displaced vertically experiences a restoring buoyancy force proportional to the density gradient, oscillating at frequency N (imaginary N means the restoring force is destabilizing — convective instability). The SOFAR channel is a waveguide: sound refracts toward the velocity minimum exactly as light refracts toward the refractive-index maximum in a graded-index optical fiber, producing long-range acoustic propagation with cylindrical rather than spherical spreading loss (1/r instead of 1/r²).

Seawater density (ρ) depends on three variables:

```
ρ = f(T, S, P)

Temperature effect:  ↑T → ↓ρ  (warm water floats)
Salinity effect:     ↑S → ↑ρ  (salty water sinks)
Pressure effect:     ↑P → ↑ρ  (compressibility, ~0.5% per 1000 m)

NUMERICAL EXAMPLE:
  Surface tropical water: T=28°C, S=35 PSU, P=0 → ρ ≈ 1022 kg/m³
  Deep North Atlantic:    T=2°C,  S=35 PSU, P=0 → ρ ≈ 1028 kg/m³
  Density difference: 6 kg/m³ → 0.6% → enormous stabilizing stratification

Sigma-t (σt) notation:  σt = ρ - 1000  (so 1027 kg/m³ → σt = 27)
```

The full equation of state (EOS-80 or TEOS-10) is a polynomial with 44+ coefficients in T, S, and P. The linearized approximation suffices for most conceptual work:

```
ρ ≈ ρ₀ [1 - α(T - T₀) + β(S - S₀)]

α (thermal expansion coefficient):  ~2×10⁻⁴ °C⁻¹ (increases with T)
β (haline contraction coefficient): ~7.5×10⁻⁴ PSU⁻¹
```

---

## T-S Diagrams (Temperature-Salinity Space)

```
T-S DIAGRAM — water masses plot as distinct clusters

  30°C │  Tropical Surface
       │         ×
  25°C │
       │
  20°C │          Mediterranean Water ×  (T=12, S=36.5)
       │
  15°C │
       │
  10°C │   Antarctic Intermediate (AAIW)  ×
       │   (T~5°C, S~34.3)
   5°C │
       │  North Atlantic Deep Water ×
   0°C │  (T=2-4°C, S=34.9-35.0)
       │
  -2°C │× AABW (T<0°C, S~34.65)
       └──────────────────────────────────── S (PSU)
          33      34      35      36      37

KEY PRINCIPLE: Each water mass has a characteristic (T,S) signature
that is conserved during advection (only modified by mixing).
Mixing plots along straight lines in T-S space.
```

Water masses identified in T-S space:
| Water Mass | T (°C) | S (PSU) | Formation Region |
|-----------|--------|---------|-----------------|
| AABW (Antarctic Bottom Water) | <0 to 2 | 34.64–34.72 | Weddell/Ross Seas |
| NADW (N. Atlantic Deep Water) | 2–4 | 34.9–35.0 | Norwegian/Labrador Seas |
| AAIW (Antarctic Intermediate) | 3–7 | 33.8–34.5 | Antarctic Convergence |
| Mediterranean Outflow Water | 8–12 | 36–37 | Strait of Gibraltar |
| North Pacific Intermediate | 4–8 | 33.9–34.4 | NW Pacific |

---

## The Three Clines

```
THERMOCLINE              HALOCLINE               PYCNOCLINE
────────────             ──────────              ───────────
Defined by:              Defined by:             Defined by:
  ∂T/∂z steep              ∂S/∂z steep             ∂ρ/∂z steep

Tropics:                 Arctic/subpolar:        Always present where
  permanent, strong        surface fresh layer     stratification exists
  100–500 m deep           from sea ice melt
                         Amazon outflow:         PERMANENT pycnocline:
Mid-latitudes:             plume halocline           tropics/subtropics
  seasonal                 suppresses mixing
  erased by winter                               SEASONAL pycnocline:
  convection             Persian Gulf:               mid-latitudes
                           inverse halocline
High latitudes:            (evaporation >
  absent or very weak       precipitation)
```

**Buoyancy frequency (Brunt-Väisälä frequency)**:

```
N² = -(g/ρ₀)(∂ρ/∂z)

N is the frequency at which a displaced water parcel oscillates vertically.
N ≈ 0.01–0.1 rad/s in thermocline (period 1–10 min)
N ≈ 0 in mixed layer (neutral stability)
N imaginary (N² < 0) → convective instability → overturning

This is directly analogous to the Brunt-Väisälä frequency in atmospheric science.
```

---

## Mixed Layer Dynamics

```
WIND MIXING:
  Wind stress τ acts on surface → turbulent Ekman layer
  Mixed layer depth h controlled by energy balance:
    Turbulent KE input (wind) vs. PE required to mix stratification

  Monin-Obukhov length L:
    L < 0: convective (night/winter cooling dominates)
    L > 0: mechanically forced (wind dominates)

LANGMUIR CIRCULATION:
  Wind + Stokes drift → counter-rotating helical cells (Langmuir cells)
  Cell spacing ~2× mixed layer depth
  Produces surface windrows (floating material concentrates in convergence zones)
  Significantly enhances mixed-layer deepening vs. pure Ekman mixing

SEASONAL THERMOCLINE CYCLE (mid-latitudes):
  Winter: strong winds + surface cooling → deep convection →
          thermocline eroded to 200–300 m
  Spring: warming + decreasing wind → thermocline reform at ~50 m
  Summer: strong stratification at ~20–50 m
  Fall: thermocline deepens again as cooling begins
```

---

## Sound Propagation and the SOFAR Channel

Sound speed in seawater depends on T, S, and P:

```
c ≈ 1449 + 4.6T - 0.055T² + 0.00029T³ + (1.34 - 0.01T)(S - 35) + 0.016z

where T = temperature (°C), S = salinity (PSU), z = depth (m)

Key effects:
  Temperature: ↑T → ↑c  (dominant in upper ocean)
  Salinity:    ↑S → ↑c  (minor effect)
  Pressure:    ↑P → ↑c  (dominant in deep ocean, ~0.016 m/s per meter depth)
```

This creates a **sound velocity minimum** at intermediate depth:

```
SOUND VELOCITY PROFILE (typical mid-ocean):

  0 m  ─────   c ≈ 1520 m/s (warm surface)
               │ decreasing (temperature effect)
 800 m ─────   c ≈ 1480 m/s  ← SOFAR CHANNEL AXIS
               │ increasing (pressure effect)
4000 m ─────   c ≈ 1510 m/s (deep water)

SOFAR = Sound Fixing And Ranging Channel
Sound rays bend toward the velocity minimum.
Once trapped in the channel, sound propagates
thousands of km with very little spreading loss
(cylindrical spreading: 1/r, vs. spherical: 1/r²).
```

**SOFAR applications**:
- WWII: SOFAR bombs — aircrew ditching aircraft could drop explosive charge, tracked by shore hydrophones
- 1960s: Project Caesar / SOSUS — Cold War submarine detection network, 1000s of hydrophones
- Blue whale calls travel oceanic basin-scale via SOFAR
- Floats (RAFOS) use SOFAR pulses for position tracking at depth

---

## Internal Waves

```
SURFACE WAVES:  restoring force = gravity on free surface
INTERNAL WAVES: restoring force = buoyancy within stratified water

Internal wave frequency range: f < ω < N
  f = Coriolis parameter (inertial frequency, ~1.4×10⁻⁴ rad/s at mid-latitudes)
  N = Brunt-Väisälä frequency (buoyancy, ~0.01–0.1 rad/s in thermocline)

Properties:
  Wavelengths: 0.1 m to 100s km
  Periods: minutes to days
  Amplitudes: 10–100 m vertical displacement (invisible at surface)
  Phase speed: much slower than surface waves
  GROUP velocity perpendicular to phase velocity (unlike surface waves)

GENERATION:
  Barotropic tides flowing over topography (ridges, seamounts, continental slopes)
  → internal tide (baroclinic tide, ω = tidal frequency, but internal mode)
  Wind stress at surface, Kelvin-Helmholtz instability at shear interfaces

BREAKING:
  Internal waves propagate energy into deep ocean
  Break near boundaries, mixing diapycnal (cross-density) transport
  Major energy source for deep ocean mixing (~1–2 TW total)
  Without internal wave breaking, thermohaline overturning would be much weaker
```

---

## Pressure and the Hydrostatic Equation

```
HYDROSTATIC EQUATION:
  dP/dz = -ρg    (z positive upward)

Typical ocean pressures:
  100 m:   ~10 bar (10 atm, ~1 MPa)
  1000 m:  ~100 bar (10 MPa)
  10000 m: ~1000 bar (100 MPa)

Rule of thumb: pressure increases ~1 dbar (decibar) per meter depth
  Oceanographers often report depth in decibars — they're nearly equal.

STERIC SEA LEVEL:
  Thermal expansion of the water column changes sea surface height.
  Warming by 1°C over 500 m water column:
    δh = α × ΔT × H ≈ 2×10⁻⁴ × 1 × 500 = 0.1 m
  Steric sea level rise is ~50% of observed 20th century sea level rise.
```

---

## Heat Budget and Heat Fluxes

```
OCEAN SURFACE HEAT BUDGET:

  Q_net = Q_SW - Q_LW - Q_H - Q_E

  Q_SW = shortwave solar radiation (absorbed)      +100 to +300 W/m²
  Q_LW = longwave back-radiation (lost)            -30 to -80 W/m²
  Q_H  = sensible heat flux (turbulent)            -5 to -100 W/m²
  Q_E  = latent heat flux (evaporation)            -50 to -200 W/m²

Evaporation dominates latent heat loss.
Western boundary currents (Gulf Stream, Kuroshio) lose 500+ W/m² to atmosphere
in winter — largest ocean-to-atmosphere heat flux on Earth.

OCEAN HEAT CONTENT (OHC):
  Measured in Joules (typically ×10²² J)
  0–700 m layer tracked by Argo
  OHC increase ≈ 7×10²³ J/yr in 2010s (excess greenhouse forcing trapped)
  This is the primary metric for global warming accounting
```

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| What controls density layering? | Temperature (dominant in tropics), salinity (dominant at high latitudes), pressure |
| What is σt? | ρ − 1000 in kg/m³ — shorthand density notation |
| What is potential temperature θ? | T corrected for adiabatic compression — use θ for water mass comparisons |
| What is the SOFAR channel? | Sound velocity minimum at ~800–1200 m depth; sound trapped, propagates basin-scale |
| Why is there no permanent thermocline at high latitudes? | Winter convection and deep mixing erase it seasonally |
| What is N (Brunt-Väisälä frequency)? | Oscillation frequency of a parcel displaced vertically; N² = −(g/ρ₀)(∂ρ/∂z) |
| What drives internal waves? | Tidal flow over topography, wind stress, shear instabilities |
| What is steric sea level? | Sea surface height change due to density changes (thermal expansion / salinity change) |

---

## Common Confusion Points

**Thermocline vs. pycnocline vs. halocline**: They're defined by which variable creates the stratification (T, S, ρ). In most of the ocean, the pycnocline and thermocline coincide because temperature dominates density. In the Arctic, a halocline (freshwater from sea ice melt) overlies saltier water, making S the dominant stratification control — temperature may even increase with depth (because cold freshwater floats over slightly warmer saltier water).

**In situ vs. potential temperature**: Seawater is slightly compressible. A parcel sinking 1000 m warms adiabatically by ~0.1°C. If you measure T at 4000 m and get 2.5°C, the potential temperature θ might be 2.0°C. Always compare water masses using θ, not in situ T. The modern standard (TEOS-10) goes further, using Conservative Temperature Θ.

**Depth vs. pressure**: Oceanographers sometimes use depth (meters) and pressure (decibars) interchangeably because 1 dbar ≈ 1 m depth. Precisely, ΔP = ρgΔz, so pressure depends on the density of everything above — in dense deep water, 1 dbar is slightly less than 1 m.

**Sound speed minimum**: You might expect sound to go fastest at the warm surface. Temperature effect wins in the upper ocean (warm surface → fast), but below the thermocline, pressure wins (cold deep water → fast). The minimum is at the crossover (~800–1200 m). This is a refraction duct — Snell's law bends rays toward the velocity minimum.

**Neutral density vs. isopycnal surfaces**: Density surfaces tilt due to the geoid, temperature/salinity variation, and pressure effects. "Neutral density" (γ) is the modern oceanographic concept — a surface a water parcel can move along without doing work against buoyancy. It's not the same as a constant-σθ surface, especially in the deep ocean near Antarctica.
