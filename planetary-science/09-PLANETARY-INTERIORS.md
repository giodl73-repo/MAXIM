# Planetary Interiors and Magnetic Fields

## The Big Picture

We cannot drill to the core of any planet (except partially Earth). Everything we know about planetary interiors comes from indirect probes: seismology, gravity fields, magnetic fields, moment of inertia, and heat flow. Planetary magnetism comes from convective dynamos in electrically conducting fluid layers.

```
+------------------------------------------------------------------+
|              PLANETARY INTERIOR INVESTIGATION                    |
+------------------------------------------------------------------+
|                                                                  |
|  PROBE METHOD          WHAT IT CONSTRAINS     MISSIONS           |
|  -----------          ------------------     --------           |
|  Seismology           Wave speed profiles    InSight (Mars)     |
|                       (density, composition)  Apollo (Moon)      |
|                       Discontinuities                            |
|                                                                  |
|  Gravity field (J₂)   Mass distribution       All orbiters       |
|  Moment of inertia    Core mass fraction                         |
|                                                                  |
|  Tidal response (k₂)  Rigidity vs fluid       Cassini, Galileo   |
|  Love numbers         core/ocean presence                        |
|                                                                  |
|  Magnetic induction   Conducting fluid layer  Galileo (Ganymede) |
|  (induced field)      (ocean, metallic core)                     |
|                                                                  |
|  Heat flow            Thermal state           HP3 (InSight)      |
|                       Radioactive inventory                      |
|                                                                  |
|  Surface geology      Volcanism, tectonics    All landers        |
+------------------------------------------------------------------+
```

---

## Seismology: Reading the Interior with Waves

The mathematics of planetary seismology is the wave equation applied to an elastic medium with spatially varying parameters. Two complementary approaches:

**Travel-time tomography**: P and S waves are ray-like at high frequency. Measure arrival time differences at multiple stations for many earthquakes → invert for the velocity field v(r,θ,φ) that best explains the travel times. This is exactly the same inverse problem as CT scanning: project measurements + algebraic reconstruction. The Earth's core was identified via the S-wave shadow zone (S-waves vanish beyond ~105° from the source because liquid iron has G=0); the inner core boundary by PKiKP reflections.

**Normal mode seismology**: At low frequencies, a planet rings like a bell in its normal modes — discrete eigenfrequencies of the elastic wave equation with spherical boundary conditions. Earth has ~10,000 observable modes below 10 mHz. The eigenfrequency spectrum is the Fourier transform of the seismogram in the long-period limit; fitting observed mode frequencies to model predictions constrains density and elastic moduli as functions of depth. The 1960 Chilean earthquake was the first event that excited a resolvable normal mode spectrum; InSight's detection of Martian normal modes in 2021-22 was the first such observation on another planet.

### Wave Types

```
SEISMIC WAVE TYPES
==================

  P-WAVES (Primary / Pressure)
    Compressional; particles oscillate parallel to propagation
    Travel through solid AND liquid
    Faster than S-waves
    v_P = √[(K + 4G/3) / ρ]  (K = bulk modulus, G = shear modulus, ρ = density)

  S-WAVES (Secondary / Shear)
    Shear; particles oscillate perpendicular to propagation
    Travel ONLY through solid (G=0 in fluids → v_S=0)
    KEY DIAGNOSTIC: S-wave shadow zone = liquid layer identified

  SURFACE WAVES (Love, Rayleigh)
    Travel along surface; most destructive on Earth
    Useful for constraining crustal thickness

WAVE VELOCITIES vs DEPTH (Earth reference)
==========================================

  Depth (km)   Structure          v_P (km/s)  v_S (km/s)
  ----------   ---------          ----------  ----------
  0-10         Crust              5-7         3-4
  0-35         Continental crust  varies      varies
  35-660       Upper mantle       7.8-10      4.4-5.5
  410          Olivine → wadsleyite (phase change) — SEISMIC DISCONTINUITY
  660          Ringwoodite → perovskite (phase change) — SEISMIC DISCONTINUITY
  660-2890     Lower mantle       10.5-13.7   5.5-7.2
  2890         Core-Mantle Boundary (CMB) — S-waves stop propagating
  2890-5150     Outer core (liquid) 8.0-10.4  0 (S-waves don't propagate)
  5150-6370     Inner core (solid)  11.0-11.3  3.5
```

### Seismic Discontinuities

```
MAJOR EARTH DISCONTINUITIES
============================

  MOHOROVIČIĆ DISCONTINUITY ("Moho"):
    Base of crust → top of mantle
    Depth: ~7 km oceanic, ~35 km continental
    Jump in seismic velocity: P-wave from ~6 km/s to ~8 km/s
    First identified by Mohorovičić 1909 from earthquake records

  410 km DISCONTINUITY:
    Olivine (α) transforms to Wadsleyite (β)
    Pressure-induced phase change, not composition change
    Sharp reflector; globally consistent

  660 km DISCONTINUITY:
    Ringwoodite → Perovskite + Magnesiowüstite
    Endothermic phase change → impedes whole-mantle convection
    Debated: does it act as a barrier to mantle mixing?

  CORE-MANTLE BOUNDARY (CMB, 2890 km):
    Silicate mantle meets liquid iron-nickel alloy
    Largest density jump in the Earth
    S-waves cannot propagate below (outer core is liquid)
    D" layer: 200-300 km thick zone above CMB; complex structure

  INNER CORE BOUNDARY (ICB, 5150 km):
    Liquid outer core → solid inner core
    P-wave velocity jump; PKIKP waves refracted through inner core
    Inner core is anisotropic (fast P-waves along rotation axis)
    Inner core rotation slightly faster than mantle (debated)
```

---

## InSight: Mars Interior Results

```
INSIGHT SEISMOLOGY RESULTS (2018-2022)
=======================================

  CRUSTAL STRUCTURE:
    Thickness: 20-37 km (northern hemisphere, Elysium site)
    Up to 55-70 km in the southern highlands
    2 or 3 crustal layers (two-layer or three-layer models)
    ~10% porosity in upper crust (consistent with impact gardening)

  MANTLE:
    S-wave velocity: 4.2-4.4 km/s
    Less iron-rich than expected from models
    Lithosphere thickness: ~400-600 km (THICK; stagnant lid confirmed)
    Low-velocity zone at ~100-150 km? (possible partial melt zone)

  CORE:
    Radius: ~1830 km (±40 km)
    LARGER THAN PREDICTED by pre-InSight models (~1700-1800 km)
    Liquid Fe-S (inferred from wave reflection; no inner solid core)
    Higher light element fraction than expected (S, O, H?)

  MARSQUAKES:
    1318 events detected before dust killed solar panels (Dec 2022)
    Largest: May 2022, magnitude 5 (teleseismic event)
    Types: low-frequency (deep?) and high-frequency (shallow/near-surface)
    No detected impacts capable of generating core-crossing waves

  INTERPRETATION:
    Mars is seismically ACTIVE — not geologically dead
    Core is lighter than expected → question for formation models
    Thick lithosphere → poor heat conductor → still hot inside?
```

---

## Planetary Differentiation

```
DIFFERENTIATION PROCESS
========================

  1. ACCRETION HEAT:
     Large impacts deposit kinetic energy as heat
     Early planetary interiors were largely molten (magma ocean phase)

  2. DENSITY SORTING:
     Molten state allows gravitational separation
     Iron (ρ ~ 7-8 g/cm³) sinks to center
     Silicates (ρ ~ 3-4 g/cm³) rise to form mantle
     Volatile elements partition to crust or escape to atmosphere

  3. TIMESCALE:
     Very fast for large bodies: iron "rain" through a magma ocean
     Hf-W chronometry: core formation Earth: <30-40 Myr after t=0
     Mars: <5 Myr (!)
     Moon: core formation ambiguous (thin crust, small core fraction)

  4. CONSEQUENCE: LAYERED STRUCTURE
     Core: iron-nickel alloy + light elements (O, S, Si, H)
     Mantle: silicates (Mg, Fe, Si, O), phases change with depth
     Crust: low-density minerals (feldspars, silica-rich) + LILEs

  SIDEROPHILE ELEMENTS:
    "Iron-loving" (Fe/Ni/Co/PGEs) — concentrated in core
    Depleted in silicate mantle/crust relative to cosmic abundance
    Earth's mantle has more PGEs than expected → "late veneer" hypothesis:
    PGE-rich chondrite accretion AFTER core formation
```

---

## Magnetic Fields and Dynamo Theory

### Dynamo Requirements

```
PLANETARY DYNAMO REQUIREMENTS
==============================

  A self-sustaining dynamo requires:

  1. ELECTRICALLY CONDUCTING FLUID
     Liquid iron alloy (Earth outer core, gas giant cores)
     Metallic hydrogen (Jupiter, Saturn)
     Superionic/ionic water-ammonia (Uranus, Neptune)

  2. CONVECTION in that fluid
     Thermal: hot fluid rises (cooling from above)
     Compositional: light elements released as inner core grows
     Earth has BOTH; compositional is dominant today

  3. ROTATION (Coriolis effect)
     Organizes convection cells into elongated columns parallel to rotation axis
     Rotating columns preferentially generate magnetic field (α-effect)
     Fast rotation → more organized → stronger field
     Venus: slow rotation → insufficient Coriolis → no dynamo?

  ABSENCE OF FIELD:
    Mars: dynamo active in Noachian (~4.1-3.9 Ga), then died
          Why? Core fully crystallized? Heat flux too low?
          Evidence: Noachian crust has strong remnant magnetization (stripes)
    Venus: no dynamo; slow rotation + possibly no inner solid core
    Moon: ancient dynamo (3-4 Ga); now dead (small core, rapidly cooled)
```

### Field Characteristics

```
MAGNETIC FIELD COMPARISON
==========================

  BODY        FIELD TYPE         TILT    DIPOLE      SOURCE
  ----        ----------         ----    ------       ------
  Earth       Dipole (dominant)  11°     0.3 T surf  Liquid Fe outer core
  Jupiter     Dipole + high      10°     ~4 G eq     Metallic hydrogen
  Saturn      Dipole (aligned!)  <1°     ~0.2 G eq   Metallic H + helium rain?
  Uranus      Complex/multipole  59°     ~0.23 G     Ionic water mantle?
  Neptune     Complex/multipole  47°     ~0.14 G     Ionic water mantle?
  Mercury     Weak dipole        ~5°     ~300 nT     Liquid Fe core (offset)
  Moon        None (global)      --      --          Dead; crustal remnants
  Mars        None (global)      --      --          Dead; crustal remnants (S hemi)
  Ganymede    Dipole             ~4°     ~120 nT     Liquid Fe core?

  GEOMAGNETIC REVERSALS (Earth):
    Field reverses polarity on average every ~300,000 yr
    Last reversal: 780,000 years ago (Brunhes-Matuyama)
    Reversal takes ~1000-10,000 years; field weakens then rebuilds
    During reversal: weaker field → more cosmic ray exposure
    Seafloor spreading creates "magnetic stripes" = record of reversals

  SATURN'S NEAR-PERFECT ALIGNMENT:
    Saturn's dipole is aligned to within 0.06° of rotation axis (!) — unique
    Why? Helium rain layer above metallic H may "filter" non-axisymmetric field components
    Theoretical puzzle: Cowling's theorem says axisymmetric dynamo impossible in simple geometry
```

---

## Heat Sources and Heat Transport

```
PLANETARY HEAT BUDGET
======================

  HEAT SOURCES:
  1. Accretion heat: kinetic energy of impactors → ~3×10⁷ J/kg for Earth
  2. Core formation: gravitational energy release ~1.5×10⁷ J/kg for Earth
  3. Radioactive decay: ²³⁸U, ²³⁵U, ²³²Th, ⁴⁰K
     → Dominant source for small/medium bodies (Moon, Mars)
     → Still active; accounts for ~50% of Earth's internal heat flux

  EARTH's HEAT FLUX:
    ~47 TW total; split:
    ~20 TW: radioactive decay
    ~27 TW: secular cooling (planet cooling down from formation)
    Average surface: 87 mW/m² (highly variable: 250+ mW/m² at MOR)

  HEAT TRANSPORT MECHANISMS:
  CONDUCTION:     Solid lithosphere; slow; ~10-40 mW/m² in old crust
  CONVECTION:     Mantle; vigorous; accounts for most heat loss in Earth
  ADVECTION:      Magma extrusion (volcanism); fast but localized
  RADIATION:      Negligible in solid/liquid interiors

  MANTLE CONVECTION MODES:
  Plate tectonics:  Lithosphere participates in convection; Earth only (confirmed)
  Stagnant lid:     Thick immobile lithosphere; heat escapes via volcanism
                    Mars, Venus, Mercury, Moon (all single-plate?)
  Episodic overturn: Stagnant lid until heat builds up → catastrophic overturns
                    Possible model for Venus's ~500 Ma global resurfacing

  RAYLEIGH NUMBER FOR MANTLE:
    Ra = αgΔTd³ / (κν)
    Earth mantle Ra ~ 10⁷ → vigorous convection
    Ra > 1000 → convection occurs
    Small Ra (cold, thick, stiff) → conductive lid (stagnant)
```

---

## Equation of State and Interior Modeling

```
INTERIOR MODELING APPROACH
===========================

  STEP 1: Choose composition model
    Bulk composition from meteorite/spectral analogy
    Divide into layers: iron core, silicate mantle, crust

  STEP 2: Apply equation of state (EOS)
    P = f(ρ, T) for each material
    High-pressure phases (Bridgmanite, post-perovskite)
    Experimental data from diamond anvil cells + shock experiments
    Mie-Grüneisen EOS commonly used

  STEP 3: Integrate hydrostatic equilibrium
    dP/dr = -ρg(r)
    g(r) = G M(r) / r²
    From surface inward; adjust layer thicknesses to match:
    - Total mass
    - Moment of inertia factor C/MR²
    - Love numbers (tidal deformation)
    - Seismic wave speeds (if available)

  STEP 4: Match observational constraints
    Moment of inertia: C/MR² = ∫ r² dm / (MR²)
    From precession rate + J₂ gravity harmonic
    Lower C/MR² = more centrally concentrated

  CURRENT FRONTIER:
    Ab initio molecular dynamics (DFT-MD) for high-P/T EOS
    Giant impact simulations: SPH (smoothed particle hydrodynamics) codes
      such as Gadget, SWIFT, and custom solvers (e.g., Benz & Asphaug codes)
      — these use LAPACK internally for linear algebra but LAPACK itself is
      a dense linear algebra library, not a simulation code
    Exoplanet interior models: mass-radius relations predict bulk composition
    (radius gap in exoplanets visible in mass-radius diagram)
```

---

## Decision Cheat Sheet

| Question | Answer |
|---|---|
| Why can't S-waves travel through liquid? | Shear modulus G=0 in fluids → v_S = √(G/ρ) = 0; they can't sustain shear deformation |
| How do we know Earth has a liquid outer core? | S-wave shadow zone (no S-waves at 103°-143° from source); P-wave velocity drop at 2890 km |
| What drives Earth's dynamo today? | Compositional convection (light elements released as inner core solidifies) + thermal convection, both organized by Coriolis force |
| Why is Mars's core larger than predicted? | InSight seismology shows radius ~1830 km; implies higher light element content (S, O, H) diluting the iron → lower density |
| What is the 660 km discontinuity? | Phase transition: ringwoodite → bridgmanite + magnesiowüstite; endothermic; resists convective overturn across this boundary |
| How do we detect subsurface oceans on moons? | Magnetic induction: varying Jovian magnetic field induces currents in a conducting layer (saltwater ocean) → measured by magnetometer orbiter |
| What is the Hf-W chronometer? | ¹⁸²Hf decays to ¹⁸²W (half-life 8.9 Myr); Hf is lithophile (silicate), W is siderophile (core); core-mantle fractionation age recorded in W isotopes |
| What causes magnetic reversals? | Chaotic fluctuations in outer core convection that occasionally cause the dipole to collapse and rebuild with opposite polarity; not fully predictable |

---

## Common Confusion Points

**The inner core is not hot because it's compressed**: The inner core is solid (not liquid) despite being at higher temperature than the outer core because the pressure at ~5150 km depth raises the melting point of iron above the actual temperature there. It's crystallographically solid, not thermally cool.

**Earth's magnetic field does not protect from solar wind by "reflecting" it**: The field deflects the solar wind plasma by the Lorentz force (charged particles spiral around field lines). The magnetosphere is a pressure balance region: solar wind dynamic pressure balanced by Earth's magnetic field pressure. Reconnection still allows some particles in at the poles.

**Moment of inertia factor 0.4 = uniform sphere; real planets are always less**: All differentiated planets have C/MR² < 0.4 because they have dense cores. The Moon's 0.394 implies very little differentiation (small iron core). Earth's 0.331 implies significant concentration of mass toward center.

**Seismic tomography is not the same as a CAT scan**: In medical CT, you control the X-ray source. In seismic tomography, you use earthquakes as sources (not controlled) and infer the 3D velocity structure from travel time anomalies. It's an inverse problem with non-unique solutions.

**Planetary magnetic fields do not need to look like Earth's**: Uranus and Neptune have chaotic multipole fields offset from the center and rotational axis. Saturn has a near-perfect axisymmetric field. Jupiter has a strong dipole. All are driven by different conducting-fluid geometries.
