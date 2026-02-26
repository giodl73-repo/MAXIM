# Isotope Systems: Radiogenic and Stable

## The Big Picture

Isotope geochemistry uses the natural variation in isotopic compositions to constrain ages, temperatures, reservoirs, and biological processes. Two fundamentally different isotope systems:

```
+------------------------------------------------------------------+
|                    ISOTOPE SYSTEMS TAXONOMY                       |
+------------------------------------------------------------------+
|                                                                  |
|  RADIOGENIC ISOTOPES          STABLE ISOTOPES                    |
|  -----------------            ---------------                    |
|  Parent decays to daughter    Fractionation shifts ratios        |
|  Daughter accumulates         Temperature-dependent              |
|  → GEOCHRONOLOGY              → PALEOTHERMOMETRY                 |
|  → TRACER (mantle domain)     → PALEOHYDROLOGY                   |
|                               → BIOSIGNATURE                     |
|                                                                  |
|  Examples:                    Examples:                          |
|  U → Pb (U-Pb dating)         ¹⁸O/¹⁶O (paleotemperature)       |
|  Rb → Sr (Rb-Sr isochron)     D/H (hydrology, climate)          |
|  Sm → Nd (crustal growth)     ¹³C/¹²C (carbon cycle)            |
|  Re → Os (ore formation)      ³⁴S/³²S (sulfur cycling)          |
|  K → Ar (thermochronology)    ¹¹B/¹⁰B (ocean pH)               |
|  Hf → W (core formation)                                        |
+------------------------------------------------------------------+
```

---

<!-- @editor[bridge/P2]: No bridge from the learner's math/physics background to the isochron method — the isochron is fundamentally linear regression on a scatter plot where slope = f(time), a concept an MIT math major grasps instantly. Framing it as "linear regression where the slope encodes age" would anchor the entire section -->
## Radioactive Decay Fundamentals

```
DECAY EQUATIONS
===============

  FUNDAMENTAL: N(t) = N₀ × e^(-λt)
    where N = number of parent atoms
    λ = decay constant (s⁻¹ or yr⁻¹)
    t = time

  DAUGHTER ACCUMULATION:
    D* = N₀ - N(t) = N₀(1 - e^(-λt)) = N(t)(e^(λt) - 1)
    D = D₀ + N(e^(λt) - 1)
    where D₀ = initial daughter present at t=0

  HALF-LIFE:
    t½ = ln(2)/λ = 0.693/λ

  PRACTICAL FORM (isochron equation):
    D/D_ref = (D/D_ref)₀ + (N/D_ref)(e^(λt) - 1)
    Plot D/D_ref vs N/D_ref → straight line with slope = (e^(λt) - 1)
    → solve for t
    Y-intercept = initial ratio (geochemically useful!)
```

---

## Major Radiogenic Systems

```
RADIOGENIC DECAY SYSTEMS SUMMARY
===================================

  SYSTEM   PARENT    DAUGHTER  t½ (Ga)  APPLICATION
  ------   ------    --------  ------   -----------
  U-Pb     ²³⁸U      ²⁰⁶Pb    4.47 Ga  Zircon dating; solar system age
           ²³⁵U      ²⁰⁷Pb    0.704 Ga Concordia cross-check
  Rb-Sr    ⁸⁷Rb      ⁸⁷Sr     48.8 Ga  Crustal ages; mantle reservoirs
  Sm-Nd    ¹⁴⁷Sm    ¹⁴³Nd     106 Ga   Crustal growth; mantle structure
  Re-Os    ¹⁸⁷Re    ¹⁸⁷Os     42.3 Ga  Ore deposits; mantle Os
  Lu-Hf    ¹⁷⁶Lu    ¹⁷⁶Hf     37.1 Ga  Zircon dating; mantle sources
  K-Ar     ⁴⁰K       ⁴⁰Ar     1.25 Ga  Thermochronology; volcanic ages
  ¹⁴C      ¹⁴C       ¹⁴N      5730 yr  Archaeological/young material

  SHORT-LIVED (extinct) SYSTEMS:
  Hf-W     ¹⁸²Hf    ¹⁸²W     8.9 Myr  Core formation (solar system first 50 Myr)
  Al-Mg    ²⁶Al     ²⁶Mg     0.72 Myr Solar system chronology; heating source
  Pd-Ag    ¹⁰⁷Pd   ¹⁰⁷Ag    6.5 Myr  Differentiation of asteroids
```

### The Rb-Sr System

```
Rb-Sr SYSTEM DETAILS
=====================

  ⁸⁷Rb → ⁸⁷Sr + β⁻    t½ = 48.8 Gyr
  λ = 1.42 × 10⁻¹¹ yr⁻¹

  ISOCHRON FORM:
    ⁸⁷Sr/⁸⁶Sr = (⁸⁷Sr/⁸⁶Sr)₀ + (⁸⁷Rb/⁸⁶Sr)(e^(λt) - 1)

  ⁸⁶Sr = non-radiogenic reference isotope (stable, not from decay)

  WHY ⁸⁷Rb/⁸⁶Sr VARIES:
    Rb: LILE, incompatible → higher in felsic/crustal rocks
    Sr: compatible in plagioclase, carbonates → variable
    Mafic rocks: low Rb/Sr; felsic rocks: high Rb/Sr

  INITIAL ⁸⁷Sr/⁸⁶Sr RATIO:
    Measures the Sr isotopic composition at the time of crystallization
    High initial ratio (>0.710): crustal contamination (old crustal Sr with
    accumulated radiogenic ⁸⁷Sr)
    Low initial ratio (~0.702-0.705): mantle-derived, little crustal input
    → STRONTIUM INITIAL RATIO IS A CRUSTAL CONTAMINATION INDICATOR

  APPLICATIONS:
    Dating old rocks (Precambrian cratons)
    Tracing mantle reservoirs (MORB vs OIB vs EM)
    Seawater ⁸⁷Sr/⁸⁶Sr curve: record of continental weathering over time
      → Used in chemostratigraphy (global correlation)
```

### The Sm-Nd System

```
Sm-Nd SYSTEM DETAILS
=====================

  ¹⁴⁷Sm → ¹⁴³Nd + α    t½ = 106 Gyr
  λ = 6.54 × 10⁻¹²  yr⁻¹

  ISOCHRON FORM:
    ¹⁴³Nd/¹⁴⁴Nd = (¹⁴³Nd/¹⁴⁴Nd)₀ + (¹⁴⁷Sm/¹⁴⁴Nd)(e^(λt) - 1)

  KEY CONCEPT: εNd notation
    εNd = [(¹⁴³Nd/¹⁴⁴Nd_sample)/(¹⁴³Nd/¹⁴⁴Nd_CHUR) - 1] × 10,000
    where CHUR = Chondritic Uniform Reservoir (model for primitive mantle)
    εNd = 0: chondritic (primitive mantle)
    εNd > 0 (positive): depleted mantle (Sm/Nd > chondritic; more Sm retained)
    εNd < 0 (negative): crustal rocks (Sm/Nd < chondritic; Nd extracted)

  WHY Sm/Nd FRACTIONATES DIFFERENTLY FROM Rb/Sr:
    Sm and Nd are both REEs → similar behavior; small fractionation
    BUT: garnet strongly prefers HREE (Sm) over LREE (Nd)
    → Melts from garnet-bearing mantle: high Nd/Sm (garnet retained Sm)
    → Residues: high Sm/Nd (HREE-enriched)
    → Continental crust: time-integrated low Sm/Nd → negative εNd

  MODEL AGE (T_DM):
    "When did this material last equilibrate with depleted mantle?"
    Uses depleted mantle evolution line as reference
    ~Age when the crust was last extracted from mantle
    Crustal extraction model ages: 1-3 Ga for most continental crust
```

---

## Stable Isotope Fundamentals

### Mass-Dependent Fractionation

```
STABLE ISOTOPE FRACTIONATION
=============================

  WHY ISOTOPES FRACTIONATE:
    Different masses → different zero-point energy → different bond strength
    Heavier isotopes have lower zero-point energy → stronger bonds
    → Heavier isotopes concentrated in more ordered/compact phases

  FRACTIONATION FACTOR (α):
    α_A-B = R_A / R_B  where R = ¹⁸O/¹⁶O (or D/H, ¹³C/¹²C, etc.)
    If α > 1: phase A enriched in heavy isotope relative to B

  TEMPERATURE DEPENDENCE:
    ln(α) ≈ A/T² + B/T + C  (empirically fit)
    At high T: fractionation → 0 (thermal equilibrium smears differences)
    At low T: large fractionation (equilibrium more complete, differences larger)
    → Low-T processes give large isotope effects (evaporation, precipitation)
    → High-T processes (magmatism >1000°C): small fractionation

  δ NOTATION:
    δ¹⁸O (‰) = [(¹⁸O/¹⁶O_sample)/(¹⁸O/¹⁶O_SMOW) - 1] × 1000
    SMOW = Standard Mean Ocean Water (reference for water)
    Positive δ¹⁸O: enriched in ¹⁸O relative to standard
    Negative δ¹⁸O: depleted in ¹⁸O (lighter, more ¹⁶O)

  STANDARDS:
    ¹⁸O/¹⁶O, D/H: SMOW (water); V-PDB (carbonates)
    ¹³C/¹²C:      V-PDB (Vienna Pee Dee Belemnite)
    ³⁴S/³²S:      V-CDT (Canyon Diablo Troilite)
    ¹¹B/¹⁰B:      NBS 951 (boric acid)
```

---

## Key Stable Isotope Systems

```
STABLE ISOTOPE SYSTEMS SUMMARY
================================

  SYSTEM   RATIO     RANGE (‰)   MAIN FRACTIONATION   APPLICATION
  ------   -----     ---------   ------------------   -----------
  O        ¹⁸O/¹⁶O  -60 to +40  Evaporation, precip   Paleotemperature
                                  Mineral crystallization  Hydrology
  H        D/H       -500 to +50 Evaporation, vapor     Paleohydrology
                                  exchange               Water source
  C        ¹³C/¹²C  -100 to +5  Photosynthesis C3/C4   Carbon cycle
                                  Marine carbonates       Biosignature
  S        ³⁴S/³²S  -50 to +40  Bacterial reduction    Ore formation
                                  Oxidation reactions    Paleoenvironment
  N        ¹⁵N/¹⁴N  -20 to +30  Denitrification        Nutrient cycling
                                  N₂ fixation
  B        ¹¹B/¹⁰B  -30 to +40  pH-dependent spec.     Ocean pH proxy
                                  (boric acid vs borate)

  KINETIC vs EQUILIBRIUM FRACTIONATION:
    Equilibrium: both phases exchange; heavier in more ordered phase
    Kinetic: one-way process (evaporation); lighter isotopes move faster
    Most geological processes: mix of both
    Rayleigh fractionation: progressive enrichment in heavy isotope
    as a reservoir is depleted (e.g., progressive ice sheet growth)
```

---

## Radiogenic Isotope Ratios as Tracers

```
FOUR-ISOTOPE (Sr-Nd-Pb-Hf) MANTLE ARRAY
==========================================

  Sr, Nd, Pb, Hf isotope ratios together constrain mantle source
  Different systems respond to different events due to different
  parent/daughter element behaviors

  SR-ND CORRELATION:
    εNd increases as ⁸⁷Sr/⁸⁶Sr decreases (for most oceanic basalts)
    "Mantle array": regression through DM (depleted) to EM (enriched)
    MORB: high εNd, low ⁸⁷Sr/⁸⁶Sr (depleted)
    EM2 OIB: low εNd, high ⁸⁷Sr/⁸⁶Sr (enriched)
    Crustal rocks fall off the mantle array (lower εNd for given Sr)

  PB ISOTOPES:
    ²⁰⁶Pb/²⁰⁴Pb, ²⁰⁷Pb/²⁰⁴Pb, ²⁰⁸Pb/²⁰⁴Pb
    ²⁰⁴Pb: completely non-radiogenic reference
    Three independent chronometers: U-Pb, U-Pb, Th-Pb
    "Geochron": primordial Pb composition line on Pb-Pb diagrams
    HIMU: very high ²⁰⁶Pb/²⁰⁴Pb → ancient high μ (U/Pb) reservoir

  Hf-Nd CORRELATION:
    εHf and εNd strongly correlated in oceanic basalts
    Hf in zircon (very compatible) → different behavior than bulk Nd
    Garnet: high Lu/Hf → over time, high εHf in garnet-bearing residue
```

---

## Short-Lived Radiogenic Systems

```
SHORT-LIVED NUCLIDE CHRONOMETRY
=================================

  PRINCIPLE:
    Some nuclides had short half-lives (<100 Myr)
    Fully decayed in early solar system
    But their daughter products preserved in early-formed minerals
    → Record events in the FIRST 100 MYR of solar system history

  ²⁶Al - ²⁶Mg SYSTEM (t½ = 717,000 yr):
    ²⁶Al was present in early solar system (confirmed by CAIs)
    Very high ²⁶Al/²⁷Al in CAIs (~5 × 10⁻⁵)
    → CAIs formed within first ~1 Myr of solar system
    Bodies that melted due to ²⁶Al heating (parent bodies of iron meteorites)
    → Must have accreted within first 2-3 Myr (while ²⁶Al still hot)

  ¹⁸²Hf - ¹⁸²W SYSTEM (t½ = 8.9 Myr):
    Hf is lithophile (stays in silicate); W is siderophile (goes to core)
    Core formation separates Hf from W
    If core formed WHILE ¹⁸²Hf was still alive:
      Silicate retains all the Hf → generates excess ¹⁸²W
      Core: low ¹⁸²W (no Hf present to generate it)
    Earth's mantle: high ¹⁸²W/¹⁸⁴W relative to chondrites
    → Earth's core formed within first ~30-40 Myr

  EXTINCT NUCLIDE SOURCES:
    Nearby supernova injection into protosolar nebula
    Spallation by early active Sun (for some nuclides)
    ²⁶Al is key supernova indicator → iron meteorite parent body heating
```

---

## Decision Cheat Sheet

| Question | Answer |
|---|---|
| What is εNd and what does it mean? | Deviation of ¹⁴³Nd/¹⁴⁴Nd from chondrite in parts per 10,000; positive = depleted mantle source; negative = old crustal material |
| Why is the Sm-Nd system useful for old rocks? | Long half-life (106 Gyr); Sm and Nd are REEs so they're immobile compared to Rb/Sr; less susceptible to hydrothermal alteration |
| What is δ¹⁸O measuring? | Deviation of ¹⁸O/¹⁶O from standard (SMOW or V-PDB) in per mille; reflects temperature (equilibrium fractionation) or water source |
| Why is ²⁶Al important for the early solar system? | It heated early-accreted bodies (bodies that accreted <2-3 Myr after CAIs melted due to ²⁶Al decay); also a high-precision chronometer for first Myr of solar system |
| What does a high initial ⁸⁷Sr/⁸⁶Sr tell you? | The magma interacted with old crust (high Rb/Sr history over long time generates high ⁸⁷Sr/⁸⁶Sr) — diagnostic of crustal contamination |
| What is the Hf-W chronometer good for? | Core formation timing in planets and asteroids — Hf lithophile, W siderophile; excess ¹⁸²W in silicate records Hf decay after core separation |
| How does boron isotope ratio record ocean pH? | Boron speciation (B(OH)₃ vs B(OH)₄⁻) is pH-dependent; different δ¹¹B; carbonates record ambient seawater B speciation → paleoacidity proxy |

---

## Common Confusion Points

**Radioactive decay is not equilibrium chemistry**: Decay is a nuclear process completely independent of temperature, pressure, or chemical state. The rate cannot be changed by any geological process (at ordinary conditions). This is why radiometric dates are robust.

**Isochron age ≠ crystallization age always**: An isochron date records the last time the system was homogenized in the daughter isotope. Metamorphic events can reset the system (called "open system behavior"). A freshly crystallized granite will show age = 0 if metamorphism mixed the Sr. Always check for disturbance indicators.

**εNd and εHf are referenced to CHUR, not zero**: εNd = 0 means "same as chondritic," not "no neodymium." Positive εNd means the sample has MORE ¹⁴³Nd/¹⁴⁴Nd than chondrites, indicating time-integrated Sm/Nd > chondritic (depleted mantle has removed Nd preferentially).

**Stable isotope fractionation decreases at high temperature**: This is exactly the opposite of what intuition might suggest. At magmatic temperatures (>800°C), virtually all isotope systems have fractionations <1‰ — they're nearly useless as thermometers. The big signals (10-30‰) come from low-temperature processes like evaporation, condensation, and biochemical reactions.
