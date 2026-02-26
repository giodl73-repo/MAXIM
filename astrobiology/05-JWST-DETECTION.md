# JWST and Atmospheric Characterization

## The Big Picture

```
+-----------------------------------------------------------------------+
|                    JWST EXOPLANET SCIENCE                              |
+-----------------------------------------------------------------------+
|                                                                       |
|  TRANSIT SPECTROSCOPY          EMISSION SPECTROSCOPY                  |
|  +----------------------+      +------------------------+             |
|  | Planet crosses star  |      | Planet behind star     |             |
|  | Starlight through    |      | Difference = planet    |             |
|  | limb atmosphere      |      | thermal emission       |             |
|  | --> absorption lines |      | --> temperature profile|             |
|  +----------------------+      +------------------------+             |
|          |                              |                             |
|          v                              v                             |
|  Transmission spectrum          Emission spectrum                     |
|  (limb composition)             (dayside T-P profile)                 |
|                                                                       |
|  DIRECT IMAGING (coronagraphy)                                        |
|  JWST NIRCam: too small for Earth-twins around sun-like stars         |
|  Future: HWO / LUVOIR for direct imaging of Earth-analogs             |
+-----------------------------------------------------------------------+
```

---

## Transit Spectroscopy: The Method

```
TRANSIT SPECTROSCOPY
=====================

                        STAR
                         *
                        / \
                       /   \
Planet -->  O         /     \
             \       /       \
              ----*-- chord ------  (transit path)

During transit:
  Flux_out = Flux_star
  Flux_in  = Flux_star * (1 - (Rplanet/Rstar)^2)
  + atmosphere contribution

Wavelength-dependent:
  At absorption wavelength of CO2 (4.3 micron):
    Effective planet radius is LARGER (atmosphere absorbs)
    Transit depth is slightly deeper
  At window wavelength:
    Effective planet radius is smaller (no atmosphere)
    Transit depth is shallower

  Plot (Rplanet/Rstar)^2 vs wavelength --> transmission spectrum
  Peaks at molecular absorption wavelengths

WHAT YOU MEASURE:
Not the spectrum of the atmosphere directly.
The DIFFERENCE in planet apparent size with wavelength.
This constrains atmospheric composition and scale height.

SCALE HEIGHT:
H = kT / (mu * g)
k = Boltzmann constant
T = temperature
mu = mean molecular weight
g = gravity

High scale height = puffier atmosphere = easier to detect.
Hot Jupiter: H ~ 500-1000 km (huge signal)
Super-Earth: H ~ 20-50 km (tiny signal)
Earth around Sun: H ~ 8 km (almost undetectable with JWST)
```

---

## Emission Spectroscopy and Secondary Eclipse

```
SECONDARY ECLIPSE METHOD
=========================

     [1]              [2]              [3]
  Planet visible    Planet behind    Planet emerges
  beside star       star             again
    *O               *               *  O

  [1] = star + planet flux
  [2] = star flux only
  Difference [1] - [2] = planet flux

  This gives: PLANET EMISSION SPECTRUM (dayside)
  Temperature-pressure (T-P) profile
  Dayside chemical composition
  Thermal phase curves: longitude-resolved temperature map

WHAT JWST HAS ACHIEVED WITH SECONDARY ECLIPSE:
- TRAPPIST-1b: secondary eclipse measured (2023, Greene et al.)
  No thermal emission redistribution --> no thick atmosphere?
  Or bare rock or very thin atmosphere
- TRAPPIST-1c: secondary eclipse (2023, Zieba et al.)
  Not consistent with Venus-like CO2 atmosphere
  Consistent with bare rock or thin atmosphere
  Both 1b and 1c: negative results, narrowing parameter space
```

---

## TRAPPIST-1 System: The Prime Target

```
TRAPPIST-1 SYSTEM
==================

Star: TRAPPIST-1 (2MASS J23062928-0502285)
  Type: M8 ultracool dwarf
  Mass: 0.089 solar masses
  Temperature: 2,550 K (very red/infrared)
  Distance: 12.43 pc (40.5 light-years)
  Age: 7.6 +/- 2.2 Gyr

PLANETS:
+--------+------+--------+-----+------------------+----------------+
| Planet | Rp   | Mp     | Porb| Flux (vs Earth)  | Status (2025)  |
+--------+------+--------+-----+------------------+----------------+
| b      | 1.12 | 1.37   | 1.5d| 4.2x (hot)       | No thick atm   |
| c      | 1.10 | 1.31   | 2.4d| 2.3x (hot)       | Not Venus-like |
| d      | 0.79 | 0.39   | 4.0d| 1.1x (HZ inner)  | Awaiting obs.  |
| e      | 0.92 | 0.69   | 6.1d| 0.66x (HZ)       | Best HZ target |
| f      | 1.04 | 1.04   |  9d | 0.38x (HZ)       | HZ target      |
| g      | 1.13 | 1.32   | 12d | 0.26x (HZ outer) | HZ target      |
| h      | 0.77 | 0.33   | 19d | 0.17x (cold)     | Cold           |
+--------+------+--------+-----+------------------+----------------+
(Rp in R_Earth, Mp in M_Earth, Flux relative to Earth)

BEST HZ CANDIDATES: TRAPPIST-1e, 1f, 1g
  - Inside or near circumstellar HZ
  - Rocky (density consistent with Earth-like composition)
  - 1e is the most Earth-like in terms of flux
  - Requires many transits to build up signal

JWST OBSERVATION TIMELINE:
  2022-2023: 1b, 1c secondary eclipses -- no thick CO2 atmosphere
  2024-2025: 1d primary transit campaigns beginning
  2025-2030: 1e, 1f, 1g will require 20-50+ transits each
  Approximate JWST time: 100-200 hours per planet for weak detection

M-DWARF HABITABILITY DEBATE:
  PRO:
  - Many M-dwarf planets in HZ are close-in -> many transits per year
  - M-dwarfs are most common star type (75% of all stars)
  - Long stellar lifetimes (>100 Gyr) -> more time for evolution

  CON:
  - Flaring: M-dwarfs are active, especially young
    XUV flares can strip atmospheric oxygen
    TRAPPIST-1 is older (7.6 Gyr) and less active now
  - Tidal locking: synchronous rotation likely
    One side always facing star, one always dark
    Climate models: may still be habitable with thick enough atmosphere
  - Pre-main-sequence luminosity: during early phase, M-dwarf
    was much brighter -- inner planets may have lost water before
    the star dimmed to current luminosity
    TRAPPIST-1b and 1c may have lost their water this way
```

---

## JWST Atmospheric Detection Milestones

```
JWST EXOPLANET DETECTIONS (key results through 2025):

2022:
CO2 in WASP-39b (transmission spectrum, NIRSpec PRISM):
- WASP-39b: hot Jupiter, Saturn mass, ~1 atm pressure
- 4.3 micron CO2 absorption detected at >25 sigma
- First definitive CO2 detection in any exoplanet atmosphere
- Also: SO2, H2O, CO, K (photochemistry of SO2 was unexpected)

2023:
TRAPPIST-1b: secondary eclipse, no thick CO2 atmosphere
TRAPPIST-1c: secondary eclipse, not Venus-like
K2-18b: CO2, CH4 confirmed; tentative DMS
VHS 1256b: CO2, H2O, CH4, CO in brown dwarf (photochemistry)
55 Cancri e: secondary eclipse suggests possible silicate/SiO atmosphere
  ("lava world" with magma ocean on dayside)

2024-2025:
WASP-121b: chemical gradients -- day-night temperature differences
Multiple hot Jupiters: cloud properties, chemistry
L 98-59 d: sub-Neptune with water vapor constraints

THE NOISE FLOOR PROBLEM:
Earth twin around Sun = 1 R_Earth around 1 R_Sun
(Rp/Rs)^2 = (6,371 km / 695,700 km)^2 = 84 ppm
Scale height of Earth atmosphere: 8 km
Atmospheric transit depth = 2 * H * Rp / Rs^2 ~ 2 ppm
JWST precision: ~10-30 ppm per transit for bright stars
Conclusion: ~100 transits needed to detect Earth's atmosphere
At 365-day period: 100 years of observation
NOT FEASIBLE WITH JWST.

FEASIBLE WITH JWST:
- Gas giants: large transit depths (1-2%), detectable easily
- Sub-Neptunes around small stars: K2-18b, LP 890-9c
- Super-Earths around M-dwarfs: TRAPPIST-1 system (requires many transits)
- Lava worlds (very hot, thin high-T atmosphere): 55 Cnc e
```

---

## Future Telescopes: The Path to Earth Twins

```
FUTURE TELESCOPE CAPABILITIES
================================

CURRENT (JWST, 2021-):
  Mirror: 6.5 m gold-coated beryllium
  Wavelength: 0.6 - 28 micron (near/mid-IR)
  Coronagraph: limited (contrast ~10^-4 for NIRCam)
  Earth-twin: NOT FEASIBLE (noise floor)

NEAR-TERM:
  ELT (Extremely Large Telescope, 2028?): 39m primary
    High-resolution spectroscopy (R~100,000)
    High-contrast coronagraphy
    Could detect O2 in TRAPPIST-1e (many hours)

HABITABLE WORLDS OBSERVATORY (HWO, 2040s):
  Recommended by Astro2020 Decadal Survey
  Mirror: ~6 m UV/optical/near-IR (UVOIR)
  Coronagraph: contrast ~10^-10 (required for Earth-twin)
  Goal: direct imaging of 25 nearby Earth-like planets
         transmission spectroscopy of ~100 exoplanets
  Can detect: O2, O3, H2O, CO2, CH4 in Earth-analogs around
              sun-like stars within 10-20 pc

LUVOIR (Large UV/Optical/IR Surveyor):
  Earlier proposal to HWO; now subsumed into HWO concept
  15 m mirror (LUVOIR-A) or 8 m (LUVOIR-B)
  LUVOIR-A: could detect biosignatures on ~50 Earth-like planets

WHAT HWO NEEDS (contrast requirements):
  Planet/star contrast at 550 nm: ~10^-10 for Earth/Sun
  JWST coronagraph: ~10^-4
  Current ground-based: ~10^-6
  Required improvement: 10,000x over JWST
  Technology: shaped-pupil coronagraph + starshade (external occulter)
```

---

## Decision Cheat Sheet

| Method | What you get | Best for | JWST capable? |
|---|---|---|---|
| Transit spectroscopy | Limb atmosphere composition | Sub-Neptunes, M-dwarf HZ | Yes (large/close planets) |
| Secondary eclipse | Dayside T-P profile and composition | Hot planets | Yes |
| Phase curve | Longitudinal temperature map | Hot Jupiters | Yes |
| Direct imaging | Full disk reflectance spectrum | Near, large planets | Marginally |
| High-res ground-based | O2, CO2, H2O at R~100,000 | TRAPPIST-1 system | No (needs ELT) |

| Target | Priority | Why | Transits needed |
|---|---|---|---|
| TRAPPIST-1e/f/g | Highest near-term | HZ, rocky, 40 ly | 20-50 each |
| K2-18b | High (already interesting) | DMS tentative, sub-Neptune | More to confirm |
| LHS 1140b | High | HZ rocky super-Earth, quiet star | ~30 |
| 55 Cancri e | Medium (not HZ) | Lava world, atmospheric chemistry | Done |

---

## Common Confusion Points

**"JWST is designed to look for life on exoplanets."**
JWST was designed as a general astrophysics telescope, optimized for infrared. Exoplanet atmospheric spectroscopy is one capability among many. It can detect atmospheres of hot giant planets easily and rocky planet atmospheres of M-dwarf systems with many transits. It cannot detect life on Earth analogs around sun-like stars.

**"TRAPPIST-1b and 1c results were negative so the HZ planets are probably bare rocks too."**
1b and 1c are *inside* the inner edge of the HZ — they receive more flux than Venus and likely experienced runaway greenhouse or atmospheric escape. Their rocky nature says nothing about 1e, 1f, 1g which are in the HZ and have had different evolution. The negative results are informative but not generalizable to the HZ planets.

**"The transmission spectrum directly gives you the atmosphere composition."**
Transit spectroscopy measures the wavelength-dependent apparent size of the planet. This gives you absorption features, which constrain chemical abundances. But there are degeneracies: clouds/hazes can flatten spectra (K2-18b initially showed flat featureless spectrum until JWST), multiple molecules can overlap, and retrieval models introduce uncertainties. It is inverse modeling, not direct measurement.

**"HWO/LUVOIR will definitively detect life."**
HWO aims to detect biosignature gases (O2, O3, H2O, CO2, CH4) in the *atmospheres* of nearby Earth-like planets. Even a full atmospheric spectrum showing multiple biosignatures would be highly suggestive but not absolutely definitive — each gas has an abiotic explanation. The combination of multiple biosignatures would represent the strongest evidence achievable with remote sensing. Definitive proof likely requires in-situ measurement or returned samples.

**"The K2-18b DMS result is confirmed."**
As of 2025-2026, the DMS signal in K2-18b is tentative (~2 sigma), unconfirmed, and requires additional observations. The journal paper (Madhusudhan et al. 2023) explicitly describes it as requiring confirmation. This is not a detection; it is a data point that justifies more telescope time.
