# Biosignatures: What to Look For

## The Big Picture

```
+-----------------------------------------------------------------------+
|                    BIOSIGNATURE SPACE                                  |
+-----------------------------------------------------------------------+
|                                                                       |
|  ATMOSPHERIC          SURFACE            CHEMICAL          TECHNICAL  |
|  BIOSIGNATURES        BIOSIGNATURES      BIOSIGNATURES     SIGNATURES |
|  +-----------+        +----------+       +----------+      +--------+ |
|  | O2 / O3   |        | Veg. red |       | Chirality|      | Radio  | |
|  | N2O       |        | edge     |       | Isotope  |      | Laser  | |
|  | CH4 + O2  |        | Circular |       | fractionat|     | IR     | |
|  | DMS       |        | polar.   |       | Molecular |     | excess | |
|  | isoprene  |        |          |       | complexity|     |        | |
|  +-----------+        +----------+       +----------+      +--------+ |
|                                                                       |
|  KEY PRINCIPLE: No single biosignature is sufficient.                 |
|  Each has abiotic false positives. Ensemble approach required.        |
+-----------------------------------------------------------------------+
```

A **biosignature** is any measurable attribute that, taken in context, can only be produced by life or is strongly enhanced by life. The critical qualifier is "in context" — all individual biosignatures have abiotic explanations. The ensemble of biosignatures, combined with planetary context, is the actual diagnostic.

---

## Atmospheric Biosignatures

### Oxygen and Ozone

```
O2 / O3 AS BIOSIGNATURE
=========================

On Earth: 21% O2 -- entirely biological origin.
Photosynthesis: 6CO2 + 6H2O + light --> C6H12O6 + 6O2
Without life, O2 would drop to ppb levels within millions of years.

ABIOTIC SOURCES OF O2:
1. Photolysis of CO2: CO2 + hv --> CO + O
   O + O --> O2 (minor but real)
2. Photolysis of H2O: H2O + hv --> H + OH
   OH + OH --> H2O2 --> H2O + 1/2 O2
3. "False positive" scenarios:
   - Desiccation of ocean world: H2O photolysis + H escape to space
     Leaves O2 behind (Luger & Barnes 2015)
     Could produce 2+ bar O2 on a Venus-like runaway world
   - CO2-rich atmosphere + high UV: photolysis accumulation
   Especially problematic for M-dwarf targets (high XUV)

OZONE (O3):
- Detectable at much lower O2 mixing ratios than O2 itself
- O3 absorption at 9.6 micron (mid-IR) and UV Hartley band
- Easier to detect than O2 from JWST perspective
- Same abiotic concerns as O2

WHY O2 ALONE IS NOT ENOUGH:
O2 + context is the key.
O2 + N2O + CH4 = very strong (biological disequilibrium)
O2 + no CO = strong (abiotic mechanism would leave CO)
O2 + CO2-only atmosphere = concern (photolysis false positive)
```

### Methane + Oxygen Disequilibrium

```
CH4 + O2 DISEQUILIBRIUM
=========================

On Earth: CH4 at 1.8 ppm, O2 at 21%
Thermodynamically: these SHOULD NOT coexist
CH4 + 2O2 --> CO2 + 2H2O (spontaneous, fast at geological time)
Atmospheric lifetime of CH4 in O2-rich atmosphere: ~10 years

CONCLUSION: Detecting both simultaneously requires CONTINUOUS SOURCES.
- O2 source: photosynthesis
- CH4 source: methanogenesis, wetlands, livestock, termites

This is the strongest simple atmospheric biosignature pair:
CH4 >> 10 ppm + O2 >> 0.1% in same atmosphere
= requires massive biological fluxes to maintain
= essentially impossible to produce abiotically

FUTURE EARTH ANALOG IN 2+ Ga:
As Sun brightens, Earth will lose ocean, O2 production declines.
Last biosignature visible from interstellar distance: N2O.
Then silence.
```

### Nitrous Oxide (N2O)

```
N2O AS BIOSIGNATURE
====================

Sources on Earth:
- Denitrifying bacteria: NO3- --> N2O --> N2
- Nitrifying bacteria: NH4+ --> NO2- --> NO3- (N2O byproduct)
- ~99% biological on Earth
- Abiotic: lightning, some volcanic activity (minor)

Why N2O is valuable:
- No significant abiotic source at detectable levels
- Detectable in mid-IR at 8.5 and 17 micron
- Less susceptible to false positives than O2

Limitation:
- Photochemically destroyed by UV in high-UV environments
- M-dwarf planets: intense UV may destroy N2O rapidly
- Only detectable if biological flux is large enough to maintain
  against photodestruction
```

### Dimethyl Sulfide (DMS)

```
DMS AS POTENTIAL BIOSIGNATURE
================================

On Earth:
- Produced by marine phytoplankton (DMSP --> DMS)
- ~1-4 ppb atmospheric concentration
- Abiotic sources: essentially none at significant levels
- Spectral feature: ~9.5 micron (overlaps ozone)

2023 JWST K2-18b:
- Madhusudhan et al. reported tentative detection of DMS
- K2-18b: sub-Neptune (8.6 Earth mass), ~2.6 R_Earth
  potentially ocean world ("Hycean" world -- Madhusudhan)
- DMS + CO2 + CH4 detected (CO2 and CH4 robust; DMS marginal)
- CONTROVERSY: signal is at ~2 sigma level (very weak)
  Alternative: DMS could be confused with other molecules
  at current spectral resolution
  Abiotic DMS production pathways exist in principle
- Status (2026): requires more JWST observations to confirm/refute

Why this matters: If confirmed, this would be the first potential
biosignature detection on an exoplanet.
Current consensus: insufficient evidence.
```

---

## Surface Biosignatures

### The Vegetation Red Edge

```
VEGETATION RED EDGE (VRE)
==========================

Chlorophyll absorption:
- Absorbs strongly in blue (~450 nm) and red (~680 nm)
- Reflects strongly in near-IR (~700-750 nm)
- Sharp "cliff" in reflectance at ~700 nm

    Reflectance
    |                     +----------- NIR plateau
    |          green bump |
    |    +-+               |
    |  __/ \______________/ ^-- sharp edge at ~700 nm
    +--+----+----+----+----+----+--> wavelength
       400   500  600  700  800  900 nm

EARTH FROM SPACE:
VRE is detectable in Earth's disk-integrated spectrum.
Amplitude: ~10% reflectance change across the edge.
Varies seasonally with vegetation cover.

ON EXOPLANETS:
- Requires high-contrast direct imaging
- LUVOIR / HWO could potentially detect VRE on an Earth-like planet
- Not detectable with transit spectroscopy (measures limb, not disk)

CONCERN:
Different photosynthetic pigments absorb at different wavelengths.
On a world orbiting a red star (M-dwarf), optimal pigments might
absorb near-IR -- producing a "red edge" at a different wavelength.
Kiang et al. (2007): explored pigment evolution under different spectra.
An exoplanet forest might look black or purple rather than green.
```

### Circular Polarization

```
CIRCULAR POLARIZATION
======================

Life on Earth is homochiral:
- L-amino acids (not D) in proteins
- D-sugars (not L) in nucleic acids
This handedness is universal and biological.

Abiotic chemistry: racemic mixtures (equal L and D)
(Note: Murchison meteorite shows slight L-amino acid excess --
but much less than biological homochirality)

CIRCULAR POLARIZATION BIOSIGNATURE:
Homochiral molecules scatter light with net circular polarization.
Racemic mixtures: zero net circular polarization.

Circular polarimetry can detect:
- Photosynthetic pigments
- Chiral molecules in general

Instrument challenge: circular polarization signal is very small
(~0.01% of total intensity from disk-integrated signal).
Requires dedicated coronagraph + polarimeter.
Not feasible with JWST. Possible with future LUVOIR/HWO.
```

---

## Chemical Biosignatures

### Isotope Fractionation

```
ISOTOPE FRACTIONATION AS BIOSIGNATURE
=======================================

CARBON:
Biological carbon fixation (RuBisCO in Calvin cycle):
Preferentially incorporates 12C over 13C.
Fractionation: delta-13C ~ -25 to -30 per mil vs. VPDB standard
(relative depletion of 13C in organic matter)

Abiotic carbon (carbonates): delta-13C ~ 0 to +5 per mil
Abiotic organic synthesis: delta-13C ~ -5 to -15 per mil

READING ANCIENT BIOSIGNATURES IN ROCK:
If you find carbonaceous material in ancient rock with
delta-13C ~ -25 per mil, this is consistent with biology.
NOT PROOF -- some abiotic synthesis fractionates carbon too.
But: in context with other evidence, it's meaningful.

Jack Hills zircons (4.1 Ga): carbon inclusions at -25 per mil
Pilbara stromatolites (3.5 Ga): isotopic signatures consistent with biology

SULFUR:
Sulfate-reducing bacteria fractionate 32S vs 34S significantly
Mass-independent fractionation (MIF-S) in Archean record
indicates anoxic atmosphere before 2.4 Ga.

Mars application:
If Mars returned samples show organic carbon with
biogenic carbon isotope signature (~-25 per mil),
this is a key line of evidence.
```

### Molecular Complexity

```
MOLECULAR COMPLEXITY AS BIOSIGNATURE
======================================

Marshall et al. (2021) "Identifying molecules as biosignatures":
Molecular assembly index (MA) -- measures minimum number of
molecular bond operations to assemble a molecule.

Key claim:
- Abiotic chemistry produces molecules with MA < ~15
- Biological molecules consistently have MA > 15
- This is because life produces copies of specific complex molecules
  while abiotic chemistry produces diverse random molecules

APPLICATIONS:
- Mass spectrometry can measure MA in principle
- Possible instrument for future Mars or ocean world missions
- Not yet validated for all abiotic vs. biotic scenarios

SEAGER'S BIOSIGNATURE GAS TAXONOMY:
Sara Seager et al. (2016): catalog of all molecules <6 atoms
relevant as atmospheric biosignatures.
~14,000 molecules surveyed.
Criteria: must be volatile, spectroscopically active, abiotic
explanations considered.
Result: a shortlist of ~50 priority molecules beyond the classics.
```

---

## Technosignatures

```
TECHNOSIGNATURES
=================

Definition: any observable manifestation of technology
Created by intelligent life; NOT life in general.

RADIO SIGNALS:
+---------------------------+
| Narrow-band radio signals |  No natural source produces narrow-band
|                           |  coherent signals at specific frequencies.
|                           |  "Wow!" signal (1977): 1420 MHz = 21 cm
|                           |  hydrogen line ("cosmic waterhole")
+---------------------------+
| Properties of a          |  Drifting frequency (Doppler from planet)
| genuine technosignal:    |  Non-repeating (we haven't seen repeat)
|                          |  Amplitude inconsistent with natural source
+---------------------------+

DYSON SPHERES / MEGASTRUCTURES:
Dyson (1960): advanced civilization builds shell around star
to capture all stellar energy.
Observable: excess infrared emission beyond stellar spectrum.
Tabby's Star (KIC 8462852): unusual dipping light curve.
Proposed as megastructure (Boyajian 2015).
Current consensus: dust/comets, not technology.

LASER TECHNOSIGNATURES:
Optical SETI: laser pulses beamed toward us.
Advantage: much higher information density than radio.
Disadvantage: requires precise aim.
PANOSETI project: dedicated all-sky optical SETI search.

BIOSIGNATURE vs. TECHNOSIGNATURE:
+----------------------------+----------------------------+
| Biosignature               | Technosignature            |
+----------------------------+----------------------------+
| Could be primitive life     | Requires intelligence      |
| Atmospheric, surface        | Radio, optical, structure  |
| Passive (no intent)         | Active or artifact         |
| JWST detectable (in future) | Requires targeted search   |
+----------------------------+----------------------------+
```

---

<!-- @editor[bridge/P2]: No old-world bridge — the false positive / ensemble approach is Bayesian inference (posterior from multiple independent priors); the "no single biosignature is sufficient" principle is a direct analog of defense-in-depth / multi-factor authentication reasoning — natural bridge to probability theory and systems design -->

## The False Positive Problem

```
FALSE POSITIVE ANALYSIS
========================

For every biosignature, there is a known or hypothesized abiotic source.
This is not an argument against looking -- it's an argument for
requiring MULTIPLE INDEPENDENT LINES OF EVIDENCE.

+------------------+------------------+-------------------------+
| Biosignature     | Abiotic source   | Context that matters    |
+------------------+------------------+-------------------------+
| O2               | H2O photolysis   | Also need: no CO,       |
|                  | CO2 photolysis   | disequil. partners      |
| CH4              | Serpentinization | Need O2 too (disequil.) |
|                  | Volcanic         |                         |
| N2O              | Lightning        | Need large flux         |
| DMS              | Unknown abiotic? | Signal strength, context|
| Red edge         | Some minerals    | Spectral shape, variab. |
|                  | (red minerals)   | seasonal cycle?         |
| Isotope fract.   | FTT synthesis    | Large effect size       |
| Chirality        | Meteorite slight | Must be large excess    |
+------------------+------------------+-------------------------+

Seager framework: "Biosignature gas" = gas produced at detectable
flux by life that cannot be explained by standard abiotic chemistry
in the planetary context observed.

ENSEMBLE APPROACH:
No single gas is definitive.
A planet with O2 + CH4 + N2O + red edge + carbon isotopes +
homochirality -- all simultaneously -- is very hard to explain
without life even if each individual line has abiotic explanations.
The ensemble probability swamps the abiotic alternatives.
```

---

## Decision Cheat Sheet

| Biosignature | Detection method | Strongest false positive concern | Confidence with ensemble |
|---|---|---|---|
| O2 | Transmission spectrum, direct imaging | Photolysis, desiccation | High if paired with CH4, N2O |
| O3 | Mid-IR 9.6 micron | Same as O2 | Proxy for O2 |
| CH4 + O2 | Transmission spectrum | CH4 alone = abiotic | Very high pair |
| N2O | Mid-IR 8.5, 17 micron | Lightning (minor) | Good standalone |
| DMS | Mid-IR ~9.5 micron | Unknown | Currently weak (K2-18b) |
| Red edge | Reflectance spectrum | Mineral reflectance | Medium; needs variability |
| Circular polar. | Polarimetry | Minerals | Not feasible with JWST |
| Carbon isotopes | Mass spec (in-situ) | FTT abiotic synthesis | Good in context |
| MA index | Mass spec | Validation needed | Promising, unproven |

---

## Common Confusion Points

**"O2 is the definitive biosignature for a planet."**
O2 has known abiotic sources, especially for planets around M-dwarfs. O2 alone requires context. The *combination* of O2 + CH4 (chemical disequilibrium pair) is far stronger. O3 is detectable at lower mixing ratios and is often a proxy for O2.

**"JWST can detect life on exoplanets now."**
JWST can detect *atmospheres* of some exoplanets. It cannot currently detect Earth-like biosignatures at Earth-like concentrations on an Earth-like planet around a sun-like star — that requires ~100+ transits, which is not feasible. JWST is exploring more favorable cases: large gas-rich planets, ocean worlds around M-dwarfs. The K2-18b DMS detection is marginal and unconfirmed.

**"The K2-18b DMS detection means we found life."**
The DMS detection in K2-18b is at ~2-sigma level — barely above noise. This is explicitly not a detection; it's a tentative signal requiring confirmation. The journal paper itself says "tentative." More JWST observations are needed. The scientific community consensus is: interesting, not convincing.

**"Biosignatures only work for atmospheric detection."**
Atmospheric biosignatures are the main focus for exoplanets because we can do spectroscopy. But for solar system bodies, chemical biosignatures (isotope fractionation, molecular complexity, chirality) in returned samples or in-situ measurements may be even more powerful.

**"If we find a technosignature, we have found intelligence."**
Technosignatures indicate *past or present* technology. A Dyson sphere around a star 1,000 light-years away was built 1,000+ years ago. We cannot know if the civilization still exists. A radio signal tells us technology existed at the time the signal was sent.
