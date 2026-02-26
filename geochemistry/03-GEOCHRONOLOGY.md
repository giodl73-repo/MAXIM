# Geochronology: U-Pb, Ar-Ar, and Other Systems

## The Big Picture

Geochronology is the science of absolute age determination. The key insight: radioactive decay is an atomic clock that cannot be wound back or sped up by geological processes. Different systems answer different questions depending on their half-lives and the minerals that host them.

```
+------------------------------------------------------------------+
|                    GEOCHRONOLOGY TOOLKIT                          |
+------------------------------------------------------------------+
|                                                                  |
|  METHOD        HALF-LIFE    MATERIAL     TIME RANGE   QUESTION  |
|  ------        ---------    --------     ----------   --------  |
|  U-Pb zircon   4.47/0.70 Ga Zircon       1 Myr-4.6 Ga Rock age  |
|  U-Pb mono.    4.47 Ga      Monazite     ~10 Myr-4 Ga Metamorphism|
|  Ar-Ar         1.25 Ga (K)  Feldspar,    1 kyr-4.5 Ga Cooling T |
|                             hornblende                            |
|  Rb-Sr         48.8 Ga      Whole rock   10 Myr-4.5 Ga Rock age |
|  Sm-Nd         106 Ga       Garnet/whole 100 Myr-4 Ga Crustal age|
|  Re-Os         42.3 Ga      Molybdenite  ~1 Myr-4 Ga  Ore deposit|
|  Lu-Hf         37.1 Ga      Garnet,      1 Myr-4 Ga  Metamorphism|
|                             zircon                                |
|  Fission track ~variable    Apatite,     1 kyr-~1 Ga  Cooling   |
|                             zircon                               |
|  (U-Th)/He     ~variable    Apatite,     100 kyr-1 Ga Low-T cool.|
|                             zircon                               |
|  ¹⁴C           5730 yr      Organic C    0-50,000 yr  Age of org.|
+------------------------------------------------------------------+
```

---

## U-Pb Geochronology: The Gold Standard

### Why U-Pb is the Best System

```
U-Pb ADVANTAGES
===============

  THREE INDEPENDENT CLOCKS:
    ²³⁸U → ²⁰⁶Pb    t½ = 4.468 Gyr   (slow decay)
    ²³⁵U → ²⁰⁷Pb    t½ = 703.8 Myr  (faster decay)
    ²³²Th → ²⁰⁸Pb   t½ = 14.05 Gyr  (Th-Pb additional)

    ²³⁸U/²³⁵U = 137.818 in modern Earth/solar system (constant!)
    → Two independent decay schemes must agree if system closed
    → CONCORDIA: both give same age = system closed = valid age

  ZIRCON (ZrSiO₄): ideal host mineral
    High U (10-1000 ppm), ZERO initial Pb (Pb²⁺ doesn't fit in lattice)
    → D₀ = 0 → all Pb is radiogenic → no initial Pb correction needed
    Chemical durability: survives erosion, metamorphism (partly), subduction
    Wide T range utility: crystallizes in granite, reworks into sediment
    Tiny: ~100 μm; in situ analysis with SHRIMP or LA-ICP-MS

  PROCEDURE:
    Separate zircons from rock
    Polish to expose interior (ignoring rim/core distinctions if needed)
    SHRIMP or LA-ICP-MS: measure ²⁰⁶Pb/²³⁸U + ²⁰⁷Pb/²³⁵U per spot
    Calculate apparent age from each ratio
    Plot on Concordia diagram
```

### The Concordia Diagram

```
CONCORDIA DIAGRAM
=================

  X-axis: ²⁰⁷Pb/²³⁵U
  Y-axis: ²⁰⁶Pb/²³⁸U

  Concordia CURVE: locus of points where both ratios give the same age
    At t=0: both ratios = 0 (pure U, no Pb yet)
    As time passes: both ratios increase (Pb accumulates)
    The curve is the path of a perfectly closed system

  A SINGLE CLOSED ZIRCON GRAIN: plots on the concordia curve
    → Age read directly from the curve

  DISCORDANT GRAIN: plots BELOW the concordia curve
    Reason: Pb loss (most common); inheritance (plots above)
    Pb loss at event time t₂ moves point off concordia toward origin
    Multiple grains with different Pb loss: scatter along a DISCORDIA LINE
    DISCORDIA LINE: connects upper intercept (original crystallization age)
                    and lower intercept (age of Pb loss event)

  VISUAL:
                   ¹
                   |  . Concordia curve
                 0.5|    .  (ages labeled)
    ²⁰⁶Pb/²³⁸U     |      . 1 Ga
                   |     ./  .
                 0.2|    .   .  .  3 Ga
                   |  ./  ← Discordia line
                   | .
                   +----+----+----+
                   0   0.5   1    2
                        ²⁰⁷Pb/²³⁵U

  Upper intercept = crystallization age (~3 Ga in example)
  Lower intercept = Pb loss event (~0 = recent disturbance)
```

---

## Ar-Ar Geochronology: Thermochronology

```
K-Ar AND Ar-Ar SYSTEMS
=======================

  ⁴⁰K → ⁴⁰Ar + β⁺  (10.72%);  t½(combined) = 1.248 Gyr
         + ⁴⁰Ca + β⁻ (89.28%)
  λ_Ar = 5.81 × 10⁻¹¹ yr⁻¹

  CLASSIC K-Ar:
    Measure K separately (FAAS/ICP); measure Ar separately (noble gas MS)
    Problem: cannot distinguish initial Ar from radiogenic Ar in same analysis
    Must assume ⁴⁰Ar₀ = 0 (zero initial argon) — often invalid

  Ar-Ar IMPROVEMENT:
    Irradiate sample in nuclear reactor: ³⁹K → ³⁹Ar (proxy for K)
    Now both ³⁹Ar (proxy for K) and ⁴⁰Ar measured in same aliquot
    ⁴⁰Ar/³⁹Ar ratio = function of age
    Can use age spectra: heat sample in steps → release Ar from different sites
    Plateau if system closed; disturbed patterns diagnose open-system behavior

  AGE SPECTRUM:
    Step-heating: each step = different T; different mineral domains
    +---------+-------+----------+---------+
    | low T   | mid T | plateau  | high T  |
    | steps   | steps | (valid)  | steps   |
    +---------+-------+----------+---------+
    age  ↑                 ___________
    (Ma)     disturbed  __/           \__
             domains   /               disturbed
                              Plateau = reliable age
    Plateau: ≥3 contiguous steps, ≥50% of ³⁹Ar, within 2σ

  CLOSURE TEMPERATURE (Tc):
    Different minerals retain Ar above different temperatures
    MINERAL       Tc (°C)   GEOLOGICAL MEANING
    -------       -------   -----------------
    Hornblende    500-530°C  Time rock cooled past 500°C
    Muscovite     340-380°C  Medium-grade metamorphism closure
    Biotite       280-320°C  Cooling through ~300°C
    K-feldspar    150-200°C  Low-T uplift/exhumation
    Plagioclase   200-250°C  Shallow crustal cooling

    Tc varies with cooling rate and grain size; Dodson equation:
    Tc = E_a/R / [ln(ART_c²D₀/(E_a × dT/dt × a²))]
    (activation energy, diffusivity, cooling rate — diffusion-controlled)
```

---

## Multiple Thermochronometers: Time-Temperature Paths

```
THERMOCHRONOLOGY TOOLBOX
==========================

  SYSTEM          Tc (°C)     MINERAL
  ------          -------     -------
  Hornblende Ar   500°C       Hornblende
  Biotite Ar      300°C       Biotite
  Zircon FT       240°C       Zircon
  Apatite Ar      70-120°C    Apatite (He retention)
  Apatite FT      60-120°C    Apatite (fission track)

  TIME-TEMPERATURE PATH RECONSTRUCTION:
    Multiple systems → constrain when the rock cooled through each Tc

    Temperature
    1000°C |.....                    ← Granite intrudes (U-Pb zircon age)
           |      ..
     500°C |         ... .           ← Hornblende Ar-Ar age
           |               ..
     300°C |                  ..     ← Biotite Ar-Ar age
           |                     .
     100°C |                      .. ← Apatite FT/He age
           +---+----+----+----+----+----
               4 Ga  3 Ga 2 Ga 1 Ga now

  GEOLOGICAL INTERPRETATION:
    Slow cooling: thick, stable crust (Precambrian shields)
    Fast cooling: rapid exhumation (mountain building, erosion)
    Reheating step: burial under sediments or magmatic intrusion
    → T-t path is the TECTONIC HISTORY of the rock
```

---

## Fission Track Dating

```
FISSION TRACK DATING
=====================

  PRINCIPLE:
    ²³⁸U spontaneously fissions (not alpha decay): ~1/2 million times less
    common than alpha decay
    Each fission event leaves a linear damage trail (track) in the crystal
    Track length ~15-20 μm in apatite (shorter in disturbed samples)
    Tracks accumulate over time → density proportional to age

  PROCEDURE:
    Polish mineral surface
    Etch with acid (reveals tracks as pits or channels)
    Count track density with microscope
    Irradiate to count uranium (induced fission of ²³⁵U with neutrons)
    Compare spontaneous : induced tracks → age

  TRACK ANNEALING:
    Tracks anneal (partially heal) at elevated temperature
    Apatite: fully anneal at T > 120°C
             partially anneal at 60-120°C (PARTIAL ANNEALING ZONE, PAZ)
             preserve at T < 60°C
    → Apatite FT records time since cooling below ~120°C

  TRACK LENGTH DISTRIBUTION:
    Fresh tracks: ~16 μm
    Annealed tracks: shorter, rounder
    Average track length + distribution → T-t path detail
    Short average + wide distribution: slow cooling through PAZ
    Long average + narrow distribution: rapid cooling
```

---

## Re-Os System: Ore Deposit Dating

```
Re-Os GEOCHRONOLOGY
====================

  ¹⁸⁷Re → ¹⁸⁷Os + β⁻    t½ = 41.6 Gyr

  MINERALS:
    Molybdenite (MoS₂): very high Re (ppm-%), minimal initial Os
    → nearly zero initial ¹⁸⁷Os → all Os is radiogenic
    → calculate age from single mineral (no isochron needed)

    Arsenopyrite, pyrite, magnetite: lower Re but usable
    Crude oil: Re-Os dates petroleum source rock maturation

  APPLICATIONS:
    Porphyry Cu-Mo deposits: molybdenite ages = mineralization age
    Critical for exploration (when did the ore system operate?)
    PGE deposits (platinum group elements): high Os; mantle melts
    Subcontinental lithospheric mantle age: Re-Os Re-depletion age

  Os ISOTOPES AS MANTLE TRACER:
    ¹⁸⁷Os/¹⁸⁸Os:
    Primitive mantle: ~0.1070
    Continental crust: very high (high Re/Os → accumulated ¹⁸⁷Os)
    Depleted peridotite: very low (Re depleted from mantle)
    → Os isotopes trace recycled crustal material in mantle-derived rocks
    → High ¹⁸⁷Os/¹⁸⁸Os in basalt = crustal contamination or recycled crust
```

---

## ¹⁴C: Radiocarbon Dating

```
RADIOCARBON DATING
==================

  ¹⁴C PRODUCTION:
    Cosmic ray neutrons hit atmospheric N: ¹⁴N + n → ¹⁴C + p
    ¹⁴C oxidized to ¹⁴CO₂ → enters the carbon cycle
    Atmospheric ¹⁴C/¹²C maintained at ~1.2 × 10⁻¹²

  ¹⁴C DECAY:
    ¹⁴C → ¹⁴N + β⁻    t½ = 5730 yr

  CALIBRATION:
    Atmospheric ¹⁴C varies over time (solar activity, geomagnetic field)
    Raw ¹⁴C date ≠ calendar age; requires calibration curve
    INTCAL23: calibration back to ~55,000 yr BP using tree rings, corals, speleothems
    "BP" = before present = before 1950 (arbitrary choice; pre-atomic bomb)

  RANGE: 100 - 50,000 yr BP
    < 100 yr: post-industrial carbon dilution; bomb carbon spike (1950s+)
    > 50,000 yr: ¹⁴C levels too low to measure reliably

  AMS ADVANTAGE:
    Accelerator Mass Spectrometry: count individual ¹⁴C atoms
    Much smaller samples (1 mg carbon vs grams for beta counting)
    Sea-floor sediment, ice core samples, individual seeds possible

  RESERVOIR EFFECT:
    Deep ocean: old water (no exchange with atmosphere); depleted ¹⁴C
    Ocean reservoir age: ~400 yr offset from atmosphere
    Marine organisms: must correct for reservoir age
    → Marine shells: subtract ~400 yr correction
```

---

## Decision Cheat Sheet

| Question | Answer |
|---|---|
| Why is zircon the preferred mineral for U-Pb? | Zero initial Pb (Pb²⁺ excluded from lattice); high U; chemically durable; survives recycling events; tiny → in situ analysis |
| What does concordia plot reveal? | Whether a system is closed (on the curve) or discordant (Pb loss); upper intercept of discordia = crystallization age |
| What is Ar-Ar's advantage over K-Ar? | Measures ³⁹Ar (proxy for K) and ⁴⁰Ar in same analysis; step-heating provides age spectrum diagnosing open-system behavior; no separate K analysis needed |
| What is closure temperature? | Temperature below which a mineral retains its daughter product; system "locks in" the clock at Tc; depends on cooling rate and grain size |
| What is a T-t path? | Time-temperature path reconstructed from multiple thermochronometers with different Tc values; records tectonic/exhumation history |
| Why can't you date seawater carbonate with Ar-Ar? | No K in calcite/aragonite; need K-bearing minerals for Ar-Ar |
| What limits ¹⁴C to 50,000 yr? | ¹⁴C/¹²C becomes unmeasurably small; too few ¹⁴C atoms remain to count reliably even with AMS |
| What does the discordia lower intercept mean? | Age of Pb loss event (often a metamorphic or hydrothermal event that reset the system); can date secondary events |

---

## Common Confusion Points

**Age ≠ crystallization age always**: Ar-Ar dates cooling through Tc, not crystallization. U-Pb in zircon dates crystallization (if on concordia). Rb-Sr whole-rock isochron dates last isotopic homogenization event. Always clarify what geological event the date is recording.

**Discordance doesn't invalidate the analysis**: A discordant sample is telling you something important (Pb loss event, multiple growth phases). Geologists routinely extract two ages from discordant arrays: original crystallization and later disturbance.

**¹⁴C "ages" are not calendar ages**: Raw ¹⁴C output is a "radiocarbon age" in yr BP. It requires calibration against the INTCAL curve to convert to calendar years. Around 3000-3500 BP, the calibration curve has a plateau → ambiguous calendar dates (a single ¹⁴C date maps to multiple calendar possibilities).

**U-Pb and Pb-Pb are not the same thing**: U-Pb uses both parent and daughter; requires knowing U/Pb ratio. Pb-Pb (plotting ²⁰⁷Pb/²⁰⁴Pb vs ²⁰⁶Pb/²⁰⁴Pb) uses only Pb isotopes — useful when U is unknown or in ancient samples where Pb is all that remains.

**Fission track annealing is temperature-dependent, not time**: At 150°C, apatite tracks anneal in thousands of years. At 60°C, they persist for hundreds of millions of years. The "partial annealing zone" (PAZ) is a critical concept — samples that spent time in the PAZ will have anomalously young or complex track distributions.
