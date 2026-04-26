# Exoplanet Detection and Demographics

## The Big Picture

~5,700 confirmed exoplanets as of 2025, with thousands more candidates. The field is split into two halves: detection methods (how we find them) and demographics (what the population statistics imply about planet formation).

```
+------------------------------------------------------------------+
|                    EXOPLANET LANDSCAPE                           |
+------------------------------------------------------------------+
|                                                                  |
|  DETECTION METHODS        POPULATION RESULTS                     |
|  -----------------        -----------------                      |
|  Transit (Kepler/TESS)    Super-Earths / mini-Neptunes most common
|  Radial velocity          Radius gap at ~1.8 R⊕                  |
|  Direct imaging           Hot Jupiters: rare but detectable       |
|  Astrometry (Gaia)        Occurrence rates: ~1 planet/star        |
|  Microlensing             Rocky HZ planets: relatively common     |
|  Pulsar timing            Giant planets: metal-rich star bias     |
|                                                                  |
|  KEY INSTRUMENTS          DEMOGRAPHICS                           |
|  ---------------          ------------                           |
|  Kepler (2009-2018)       ~75% of planets are smaller than Neptune|
|  TESS (2018-)             "Hot Jupiters" ~0.5% of FGK stars      |
|  HARPS/ESPRESSO (RV)      Super-Earths ~50% of FGK stars         |
|  JWST (2021-)             Occurrence peaks at 1-2 R⊕ and 2-4 R⊕ |
|  ELT/GMT (2030+)                                                  |
+------------------------------------------------------------------+
```

---

## Detection Methods

The two dominant detection techniques are direct applications of physics you already own:

**Radial velocity = Kepler's laws + Doppler spectroscopy.** The star and planet orbit their common center of mass. Kepler's third law (P² ∝ a³/M_star) gives the semi-major axis from the measured period. The star's reflex velocity amplitude K = (2πG/P)^(1/3) × m_p sin(i) / (m_star + m_p)^(2/3) — so measuring K gives m_p sin(i), the minimum planetary mass. The Doppler shift in stellar absorption lines at the ~m/s precision level is the measurement; modern echelle spectrographs achieve this by recording thousands of spectral lines simultaneously and fitting the shift across all of them.

**Transit = occultation photometry.** When a planet transits, it blocks a fraction of the stellar disk equal to (R_planet/R_star)². A 1% dip in flux → R_planet ≈ 0.1 R_star (roughly Jupiter-sized). Combined RV + transit gives both mass and radius, and therefore bulk density — the physical observable that constrains interior composition.

### Radial Velocity (RV)

```
RADIAL VELOCITY METHOD
======================

  PRINCIPLE:
    Planet orbits star → both orbit center of mass
    Star wobbles toward and away from us
    Doppler shifts the stellar spectrum (blueshift approaching, redshift receding)

  MEASURED:
    Δv = (m_p / m_star) × v_planet × sin(i)
    where i = orbital inclination

  SENSITIVITY:
    Jupiter around Sun: Δv = 12.5 m/s (detectable)
    Earth around Sun:   Δv = 0.09 m/s (requires next-gen instruments)
    Modern HARPS:       ~30 cm/s precision (ESPRESSO: ~10 cm/s)

  WHAT IT MEASURES:
    Orbital period P → semi-major axis a (via Kepler's 3rd law)
    m_p × sin(i) → minimum mass (true mass unknown without inclination)
    Eccentricity e → orbital shape
    NOT size (radius) — need transit for that

  HISTORY:
    1995: 51 Peg b — first hot Jupiter confirmed (Mayor & Queloz, Nobel 2019)
    Surprised everyone: Jupiter-mass planet at 0.05 AU (4-day orbit)
```

### Transit Method

```
TRANSIT METHOD
==============

  PRINCIPLE:
    Planet crosses in front of star → blocks fraction of light
    Periodic dips in brightness with period = orbital period

    ΔF/F = (R_p/R_star)²
    Earth transit across Sun: ΔF/F = (0.009)² = 8 × 10⁻⁵ (80 ppm)
    Jupiter transit:          ΔF/F = (0.10)²  = 1%

  WHAT IT MEASURES:
    Radius ratio R_p/R_star
    Orbital period
    Inclination (transit requires nearly edge-on: i ≈ 90°)
    Atmospheric composition (transmission spectroscopy during transit)

  LIMITATIONS:
    Geometric: only ~0.5% of randomly oriented orbits transit
    (closer planets: higher probability)
    False positives: eclipsing binaries, background stars

  KEPLER TELESCOPE (2009-2018):
    Monitored 150,000+ stars continuously
    Discovered ~2,700 confirmed planets
    Found: small planets are common; Hot Jupiters are rare; HZ planets exist

  TESS (2018-):
    All-sky survey; 26 sectors; ~85% of sky coverage
    Focuses on bright nearby stars (better for follow-up)
    Optimized for finding rocky planets around M dwarfs
```

### Direct Imaging

```
DIRECT IMAGING
==============

  CHALLENGE:
    Star-planet contrast ratio:
    Jupiter (reflected light): ~10⁻⁹ contrast at visible wavelengths
    Earth: ~10⁻¹⁰ contrast
    Star is BILLIONS of times brighter than the planet

  TECHNIQUES:
    Coronagraph: blocks starlight; reveals faint companions
    Starshade: external occulter (kilometers away from telescope)
    Adaptive optics + coronagraphy: current state of art

  WHAT'S IMAGED:
    Young, massive planets far from their stars (self-luminous: hot from formation)
    HR 8799 b,c,d,e: 4 planets directly imaged; 24-70 AU from star
    Beta Pictoris b: ~10 AU; disk interaction visible
    Fomalhaut b (controversial): dust cloud, not planet?

  JWST CONTRIBUTION:
    Mid-IR imaging of warm planet emission
    First direct spectroscopy of exoplanet atmosphere (HR 8799 b)
    VHS 1256 b: complex atmosphere spectrum (clouds, CO, CO₂, CH₄, H₂O)

  FUTURE:
    Roman Space Telescope: coronagraph instrument for reflected light
    ELTs (2030s): 30-39 m aperture + AO → rocky planet direct imaging possible
```

### Other Methods

```
OTHER DETECTION METHODS
========================

  ASTROMETRY:
    Measure star's position on sky → tiny wobble reveals planet
    Gaia: astrometric planet search for stars within ~100 pc
    Expected 10,000-20,000 giant planet detections from Gaia data

  MICROLENSING:
    Distant star acts as gravitational lens; planet-star system
    lens briefly magnifies background star
    Sensitive to: planets at 1-10 AU from any star in Galaxy
    No follow-up possible (one-time event; too faint to re-observe)
    Finds: cold Neptunes, cold super-Earths around solar-type stars

  PULSAR TIMING:
    First confirmed exoplanets (1992): 3 Earth-mass planets around PSR 1257+12
    (Not considered "real" planets by many — formed from supernova debris)
    Technique: measure pulse arrival time variations

  TIMING VARIATIONS (TTV):
    In multi-planet systems, planet-planet interactions shift transit times
    Kepler used TTV to confirm non-transiting companions
    Measures true masses (not m sin i) for transiting planets
```

---

## Atmospheric Characterization

### Transmission Spectroscopy

```
TRANSMISSION SPECTROSCOPY
==========================

  During transit, starlight passes through planet's limb atmosphere

  LIMB                         STELLAR DISK
  ----                         ------------
  +-------+                   +-------------------+
  |       |                   |                   |
  |  atm  |  starlight -->    |       STAR        |
  |  layer|                   |                   |
  |       |                   +-------------------+
  +-------+

  Molecules absorb at specific wavelengths → less light at those wavelengths
  → absorption features in transmission spectrum

  JWST HAS DETECTED IN EXOPLANET ATMOSPHERES:
    WASP-39 b:  CO₂, CO, H₂O, SO₂, Na, K, H₂S (2022)
    K2-18 b:    CH₄, CO₂, possible DMS (dimethyl sulfide) — debated
    TRAPPIST-1b: likely no thick atmosphere (thermal emission flat)
    LHS 1140 b:  potential water-rich atmosphere (2024)

  EMISSION SPECTROSCOPY:
    During secondary eclipse (planet behind star)
    Measure planet's own thermal emission
    Constrains temperature profile and day/night contrast
```

---

## Demographics: What Kepler Found

### The Radius Gap

```
THE RADIUS GAP (~1.8 R⊕)
=========================

  Kepler radius distribution shows a DIP at ~1.5-2.0 R⊕

  <1.5 R⊕:  Super-Earths / rocky planets (common)
  1.5-2.0 R⊕: GAP (underrepresented)
  2.0-4.0 R⊕: Sub-Neptunes / mini-Neptunes (common)
  >4.0 R⊕:  Gas giants (less common)

  WHY THE GAP?
  Two mechanisms, probably both acting:

  1. PHOTOEVAPORATION (Owen & Wu 2013):
     XUV radiation from young star strips H/He envelope
     Small rocky cores (< ~1.5 R⊕) get stripped to bare rock
     Larger rocky cores retain thin H/He envelope → sub-Neptune
     Gap forms at "valley" between stripped and non-stripped

  2. CORE-POWERED MASS LOSS (Gupta & Schlichting):
     Internal heat from planet's own luminosity drives evaporation
     Same qualitative effect; different timescale

  Observed: gap location depends on orbital period (close-in = more stripped)
  Gap moves to smaller radii for closer planets → consistent with evaporation
```

### Occurrence Rates

```
PLANET OCCURRENCE RATES (FGK stars, Kepler)
============================================

  SIZE RANGE     PERIOD 10-200 d    FRACTION OF STARS
  ----------     ---------------    -----------------
  1-2 R⊕         Any habitable?     ~25-50%  (super-Earths)
  2-4 R⊕         10-200 days        ~20-30%  (sub-Neptunes)
  4-8 R⊕         10-200 days        ~5-10%   (Neptune-size)
  > 8 R⊕ (Jup.)  10-200 days        ~3-5%
  Hot Jupiter    P < 10 days        ~0.5-1%

  TOTAL: Roughly 1 planet per star on average (Fressin et al. 2013)
  Many stars have multiple planets in compact configurations
  (TRAPPIST-1: 7 planets within ~0.06 AU)

  HABITABLE ZONE ROCKY PLANETS:
  η_⊕ (eta-Earth): ~10-50% of FGK stars have rocky HZ planet
  Wide uncertainty because HZ planets are hardest to detect reliably
```

### The Hot Jupiter Puzzle

```
HOT JUPITER FORMATION PUZZLE
==============================

  Hot Jupiters:
    Orbital period: < 10 days (some < 1 day)
    Mass: > 0.3 Jupiter masses
    Cannot form where they orbit (too hot, too little mass)
    → MUST have migrated from beyond the frost line

  MIGRATION MECHANISMS:
  1. Disk migration (Type II):
     Planet opens a gap in the protoplanetary disk
     Disk torques drag the planet inward
     Must halt: disk dissipation, or tidal interaction with star

  2. High-eccentricity migration:
     Planet scattered to high-e orbit by planet-planet interaction
     Tidal circularization at close approach
     Results in low-e, close-in orbit (final state = hot Jupiter)

  EVIDENCE:
  Orbit alignment: many hot Jupiters have misaligned orbits (sky-plane tilt)
  → Implies late-stage scattering, not smooth disk migration (which would be aligned)
  But some hot Jupiters ARE aligned → probably both mechanisms operate

  DESERT:
  "Hot Neptune desert": very few Neptune-mass planets at <10 days
  Explanation: atmospheric escape strips them to hot super-Earths
  (Hot Jupiters survive because their gravity retains H/He)
```

---

## Key Systems

```
BENCHMARK EXOPLANET SYSTEMS
============================

  SYSTEM          TYPE           WHY IMPORTANT
  ------          ----           -------------
  51 Peg b        Hot Jupiter    First exoplanet confirmed (1995)
  HD 209458 b     Hot Jupiter    First transit detection (1999)
  TRAPPIST-1      7 rocky        3 in HZ; ultracool M dwarf; atmospheric target
  (5 planets)
  Proxima Cen b   Rocky, HZ?     Nearest star; RV-only; no transit
  HR 8799 b-e     4 giant        Directly imaged system; GCM studied
  Kepler-186 f    Rocky, HZ      First Earth-size planet in HZ (2014)
  K2-18 b         Sub-Neptune HZ JWST detected CH₄, CO₂; "Hycean" candidate?
  LHS 1140 b      Rocky, HZ      Potentially habitable; JWST atmospheric study
  GJ 1132 b       Rocky          Lost atmosphere; now secondary atmosphere?
  TOI-700 d       Rocky, HZ      TESS discovery; JWST target
  WASP-76 b       Ultra-hot Jup  Iron rain (Fe vapor condenses on night side)
```

---

## Biosignatures and Next Steps

```
BIOSIGNATURE SEARCH
===================

  CANDIDATE BIOSIGNATURES IN ATMOSPHERES:
    O₂/O₃:       Photosynthesis product; most discussed
    N₂O:         Produced by denitrifying bacteria; no known abiotic source
    CH₄ + CO₂:   Disequilibrium pair; chemical reaction destroys one without
                 biological replenishment
    DMS:          Dimethyl sulfide; ocean biology on Earth
    Phosphine:    PH₃; no known high-T abiotic pathway (controversial)

  FALSE POSITIVES:
    O₂ from abiotic CO₂ photolysis (dry rocky planet)
    CH₄ from serpentinization (water + rock)
    → Context matters: O₂ only significant with liquid water evidence

  JWST LIMITATIONS:
    Rocky planet atmospheres require ~100 transits of bright nearby star
    TRAPPIST-1 planets: possible with hundreds of hours telescope time
    True Earth-twin biosignature detection: requires next-generation telescope

  NEXT-GENERATION:
    Habitable Worlds Observatory (HWO, ~2040s): 6m telescope, starshade
    Target: directly image ~25 Earth-analogs around nearby stars
    Detect O₂, H₂O, CH₄ in reflected light spectra
```

---

## Decision Cheat Sheet

| Question | Answer |
|---|---|
| How do we measure planet mass? | Radial velocity (m sin i) or transit timing variations (true mass) |
| How do we measure planet radius? | Transit (R_p/R_star from ΔF/F = (R_p/R_star)²) |
| What causes the radius gap? | Atmospheric photoevaporation or core-powered mass loss strips H/He from small cores; gap at ~1.5-2.0 R⊕ |
| What fraction of stars have rocky planets in the HZ? | η_⊕ ≈ 10-50% (uncertain; based on Kepler statistics extrapolated to longer periods) |
| How were hot Jupiters formed? | Cannot form in place; migrated inward via disk migration or high-eccentricity scattering + tidal circularization |
| Best current target for biosignature search? | TRAPPIST-1 system (especially e and f); LHS 1140 b — rocky, near HZ, M dwarf, observable with JWST |
| What did Kepler's most important discovery change? | That small planets (sub-Neptune) are the most common type, not gas giants — solar system is atypical |
| What is a Hycean world? | Hypothetical planet type: liquid water ocean under a thick H₂-rich atmosphere; may inhabit a wider temperature range than Earth-like HZ |

---

## Common Confusion Points

**Radial velocity gives minimum mass**: RV measures m_p × sin(i). If the orbit is face-on (i ≈ 0), the measured signal is zero even if the planet is massive. You need inclination (from transit or astrometry) to get true mass.

**Transit probability decreases with orbital period**: Close-in planets are far more likely to transit. The transit probability is approximately R_star/a. A Venus-analog transits ~1/100 randomly oriented orbits; an Earth-analog ~0.5%. This biases the Kepler sample toward close-in, short-period planets.

**TRAPPIST-1 planets are not confirmed habitable**: Three planets orbit within the classical habitable zone, but TRAPPIST-1 is an ultracool M dwarf that emits intense XUV radiation. The planets may have had their atmospheres stripped early, or they may retain them — JWST is actively studying this. Habitability is not the same as being in the HZ.

**The radius gap is not a gap in planet existence**: Planets at 1.5-2.0 R⊕ do exist; the gap is a statistical underdensity in the Kepler sample — there are fewer of them than you'd expect from a smooth distribution. The gap is a diagnostic of atmospheric stripping physics.

**Direct imaging sees very few planets**: Current direct imaging probes only young massive planets (>1 Jupiter mass) at wide separations (>5-10 AU). The "typical" planet found by Kepler (2-3 R⊕ at 0.1-0.5 AU) is completely inaccessible to current direct imaging.
