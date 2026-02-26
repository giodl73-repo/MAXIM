# Stable Isotope Paleoclimatology

## The Big Picture

Stable isotope ratios in ancient geological materials are frozen snapshots of past environmental conditions: temperature, ice volume, precipitation, salinity, and ocean chemistry. The key systems are oxygen (δ¹⁸O), hydrogen (δD), carbon (δ¹³C), and boron (δ¹¹B).

```
+------------------------------------------------------------------+
|              STABLE ISOTOPE PROXY TOOLKIT                         |
+------------------------------------------------------------------+
|                                                                  |
|  PROXY    ARCHIVE         RECORDS              RESOLUTION        |
|  -----    -------         -------              ----------        |
|  δ¹⁸O    Forams (marine) T°C + ice volume     1 kyr-orbital     |
|           Ice cores       Temperature + hydrol. Annual-orbital   |
|           Speleothems     Cave T + rainfall    Annual-seasonal   |
|           Corals          Sea surface T        Seasonal          |
|                                                                  |
|  δD       Ice cores       Temperature          Annual            |
|                                                                  |
|  δ¹³C     Marine sed.    Carbon cycle state   10 kyr-orbital    |
|           Organic matter Photosynthesis type                     |
|           Carbonates     Dissolved inorganic C                   |
|                                                                  |
|  δ¹¹B     Forams         Ocean pH             10 kyr             |
|           Corals         Surface ocean pH     Seasonal           |
|                                                                  |
|  Δ¹⁷O    Sulfates        Past photosynthesis  Myr-scale         |
|  (mass ind.) Barite       rates                                  |
+------------------------------------------------------------------+
```

---

## δ¹⁸O: The Master Paleoclimate Proxy

### How Oxygen Fractionates

```
OXYGEN ISOTOPE FRACTIONATION
==============================

  ¹⁶O (99.76%) and ¹⁸O (0.20%) and ¹⁷O (0.04%)

  EVAPORATION (ocean → vapor):
    H₂¹⁶O evaporates preferentially (lighter → higher vapor pressure)
    Vapor is depleted in ¹⁸O relative to ocean water
    δ¹⁸O_vapor ≈ δ¹⁸O_ocean - 10‰ (at tropical temperatures)

  RAYLEIGH DISTILLATION (during poleward transport):
    As vapor moves to higher latitudes, it rains/snows out
    Each precipitation event removes ¹⁸O preferentially
    Remaining vapor gets progressively more depleted
    Polar precipitation: δ¹⁸O ≈ -30 to -50‰
    (Antarctica: -55‰ at center; SMOW = 0 by definition)

  TEMPERATURE EFFECT ON PRECIPITATION:
    Colder → more fractionation → more negative δ¹⁸O
    ~0.7‰ per 1°C change in air temperature (ice cores)
    → ICE CORE δ¹⁸O directly records air temperature history

  CARBONATE PRECIPITATION:
    CaCO₃ precipitates from water; ¹⁸O fractionation depends on T°C
    δ¹⁸O_calcite ≈ δ¹⁸O_water - 0.22(T - 16.9)  [Epstein et al.]
    (approximate; multiple calibration equations exist)
    Warmer T → lower δ¹⁸O in carbonate
    → δ¹⁸O of marine carbonates records paleotemperature
```

### The Benthic Foram δ¹⁸O Record

```
MARINE δ¹⁸O RECORD (CENOZOIC)
================================

  MATERIAL: Benthic (deep-sea) foraminifera in marine sediment cores
  They calcify at bottom water temperature (~2°C modern)

  The benthic δ¹⁸O record since 65 Ma:

  Ma    δ¹⁸O (‰)    Climate state
  ---   ---------    -------------
  65    ~1.0         Warm; little or no ice; Eocene greenhouse
  50    ~0.5         PETM spike; brief warming event (negative excursion)
  34    ~2.5         EOT: Eocene-Oligocene Transition; Antarctic glaciation begins
  14    ~2.0         Mid-Miocene Climatic Optimum
  10    ~3.5         East Antarctic Ice Sheet intensification
  2.7   ~4.5         Northern Hemisphere Glaciation begins
  0     ~3.5-4.5     Modern; Pleistocene glacial-interglacial cycles

  AMBIGUITY: δ¹⁸O records BOTH temperature AND ice volume
    Glaciation: ice sheets store ¹⁶O → ocean becomes ¹⁸O-enriched
    Ice volume effect: ~0.1‰ per 10 m sea level change
    Temperature effect: ~0.25‰ per 1°C bottom water T change
    DECONVOLUTION REQUIRES: Mg/Ca ratio (temperature-only proxy)
    or independent sea-level reconstruction
```

---

## The PETM: δ¹³C and δ¹⁸O Excursions Combined

```
PALEOCENE-EOCENE THERMAL MAXIMUM (PETM, ~55.9 Ma)
===================================================

  SIGNAL:
    δ¹³C: negative excursion of -3 to -5‰ in <10,000 yr
    δ¹⁸O: negative excursion of ~1-1.5‰ (warming signal)
    Dissolution horizon in sediment (ocean acidification)

  WHAT THIS MEANS:
    δ¹³C excursion = massive injection of ¹³C-depleted carbon into atmosphere
    Organic carbon: δ¹³C ~ -25‰; methane: ~ -60‰; limestone: ~0‰
    Size of excursion: implies ~2000-4500 Gt C injected
    δ¹⁸O excursion: ~5-8°C warming over ~10,000 yr; lasted ~200,000 yr

  CARBON SOURCE CANDIDATES:
    Methane hydrate dissociation (ACES: "gun" hypothesis)
    Volcanic outgassing (North Atlantic Igneous Province)
    Oxidation of organic-rich marine sediments
    Permafrost thaw (much less CO₂ reserve then)
    CONSENSUS: Multiple sources; trigger unclear; biotic feedbacks

  BIOTIC RESPONSE:
    Mass extinction of benthic forams (~40-50% species)
    Range expansions of surface-dwelling species
    Mammal dispersal events (North America-Europe connection)
    Recovery took ~200,000 yr → useful for Anthropocene projection

  CARBON ISOTOPE EXCURSIONS (CIEs) as a CHEMOSTRATIGRAPHIC TOOL:
    CIEs are globally synchronous → used for correlation
    Other CIEs: Oceanic Anoxic Events (OAEs), Triassic-Jurassic boundary,
    End-Permian, Cambrian
    Each marks a global perturbation to the carbon cycle
```

---

## Ice Cores: High-Resolution Climate Archives

```
ICE CORE RECORD
================

  ARCHIVE:
    Vostok (Russia): 400 kyr; 4 glacial cycles
    EPICA Dome C (Antarctica): 800 kyr; 8 glacial cycles; deepest record
    GISP2 / GRIP (Greenland): 110 kyr; annual layers in upper section

  INFORMATION:
    δ¹⁸O or δD: air temperature (above)
    Air bubbles: trapped ancient atmosphere → CO₂, CH₄ concentrations
    Dust: continental aridity, atmospheric circulation
    Volcanic sulfate: timing of major eruptions
    Sea salt: ocean proximity/storm tracks
    Pollen (in some): regional vegetation

  THE EPICA 800,000-yr RECORD:
    8 complete glacial-interglacial cycles
    CO₂ ranges: 180 ppm (glacial) to 280 ppm (interglacial)
    CH₄ ranges: 350 ppb (glacial) to 720 ppb (interglacial)
    Temperature range: ~8-10°C between glacial and interglacial

  MILANKOVITCH CYCLES (confirmed in ice cores):
    100 kyr eccentricity: dominant in past 900 kyr (Late Pleistocene)
    41 kyr obliquity: dominant 2.6-0.9 Ma ("41 kyr world")
    23 kyr precession: always present; modulates ice volume
    The "MPT" (Mid-Pleistocene Transition, ~0.9 Ma): switch from 41 to 100 kyr
    → internal glacial dynamics changed; possibly ice sheet size effect

  TEMPORAL RESOLUTION:
    Annual layers preserved in Greenland at ~100-200 m depth
    Annual resolution to ~100,000 yr BP in Greenland
    Deeper: layers thin and fold; only ~2000-yr resolution at 800 kyr
```

---

## Speleothems: The Cave Record

```
SPELEOTHEM OXYGEN ISOTOPES
============================

  ARCHIVE: Stalagmites, stalactites in caves (CaCO₃)
  ADVANTAGE:
    Found on every continent
    Can be dated precisely by U-Th (within caves → closed system)
    Annual layers in some → seasonal resolution
    Record rainfall and temperature in cave region

  WHAT δ¹⁸O RECORDS IN SPELEOTHEMS:
    Depends on location:
    High-latitude caves (Europe, China): mainly temperature + ice volume
    Monsoon regions (East Asia, India): mainly AMOUNT EFFECT of rainfall
    Amount effect: heavy rainfall → depleted δ¹⁸O in precipitation
    → δ¹⁸O_speleothem records monsoon intensity, not temperature directly

  DONGGE CAVE (China):
    Heshang Cave records East Asian Monsoon
    Stalagmite records last 160 kyr at sub-decadal resolution
    Shows monsoon strength correlates with Greenland ice core temperature
    → Northern Hemisphere insolation drives both ice extent and monsoon

  GREAT CAVE (Borneo):
    δ¹⁸O negative during MIS 3 (warmer) interstadials (stronger monsoon)
    High correlation with Greenland interstadials
    Demonstrates teleconnection: North Atlantic ↔ SE Asian monsoon

  LIMITATIONS:
    Must check for equilibrium precipitation (kinetic effects introduce bias)
    δ¹⁸O of drip water must be characterized
    Local effects (evaporation in cave) can complicate interpretation
```

---

## δD and the Deuterium Excess

```
HYDROGEN ISOTOPES
=================

  H = ¹H (99.985%) and D = ²H (0.015%)

  δD = [(D/H)_sample / (D/H)_SMOW - 1] × 1000

  METEORIC WATER LINE (Craig 1961):
    δD = 8 × δ¹⁸O + 10  (Global Meteoric Water Line, GMWL)
    All precipitation lies roughly along this line
    Slope = 8 from equilibrium fractionation relationship between D/H and ¹⁸O/¹⁶O

  DEUTERIUM EXCESS (d):
    d = δD - 8 × δ¹⁸O
    Ideal evaporation from ocean: d ≈ 10‰
    Higher d: evaporation under low humidity (Mediterranean in summer)
    Lower d: prolonged isotopic equilibration (warm, humid source)
    USES:
      Tracks moisture source regions
      Ice cores: d excess traces source of water vapor for Antarctic snow
      → Changes in Southern Ocean / Indian Ocean evaporation conditions

  ICE CORE δD (EPICA):
    EPICA Dome C: δD range ≈ -370 to -440‰
    Temperature reconstruction: ΔT ≈ ΔδD / 6.2 (Jouzel calibration)
    Last glacial max: ~8°C colder at Dome C than interglacial
```

---

## Boron Isotopes: Paleo-pH Proxy

```
BORON ISOTOPE pH PROXY
=======================

  PRINCIPLE:
    Boron exists in seawater as:
    Boric acid:  B(OH)₃  (δ¹¹B ~ +27‰; dominant at low pH)
    Borate ion:  B(OH)₄⁻ (δ¹¹B ~ +19‰; dominant at high pH)
    Equilibrium: B(OH)₃ + H₂O ⇌ B(OH)₄⁻ + H⁺
    pKb ≈ 8.6 in seawater (pH of modern surface ocean ≈ 8.1)

    At low pH: boric acid dominant → high δ¹¹B in solution
    At high pH: borate dominant → low δ¹¹B in borate

    Foraminifera incorporate BORATE (not boric acid) into calcite
    → δ¹¹B_foram records δ¹¹B_borate → records pH of ambient seawater

  MODERN CALIBRATION:
    δ¹¹B_foram = m × pH + b  (linear in calibration)
    Validated in modern forams against measured pH

  APPLICATION TO CENOZOIC OCEAN pH:
    Eocene (50 Ma): pH ~7.5-7.8 (lower)
    Oligocene-Miocene: pH ~7.9-8.1
    Modern: ~8.1 (decreasing due to CO₂ uptake)
    PETM: pH drop of ~0.3-0.5 units in <10 kyr (ocean acidification confirmed)

  LIMITATION:
    Vital effects: biological forams don't all precipitate in equilibrium
    Must use well-calibrated species (Globigerina, Cibicidoides)
    Seawater δ¹¹B changed over time (requires independent constraint)
```

---

## Decision Cheat Sheet

| Question | Answer |
|---|---|
| What does a negative δ¹⁸O excursion in benthic forams mean? | Warming and/or ice sheet melting (sea-level rise releases ¹⁶O back to ocean) |
| How do you separate T from ice volume in δ¹⁸O? | Use Mg/Ca paleothermometry (independent T proxy) to isolate the temperature signal; subtract from total δ¹⁸O to get ice-volume component |
| What is the GMWL? | Global Meteoric Water Line: δD = 8δ¹⁸O + 10; all fresh precipitation roughly plots on this line |
| What does deuterium excess record? | Conditions at evaporation source (low relative humidity = high d-excess); used to track moisture source changes in ice cores |
| What did the PETM δ¹³C excursion size tell us? | Magnitude of carbon injection (~2000-4500 Gt C of ¹³C-depleted carbon); source was isotopically light (organic carbon, methane) not just volcanic CO₂ |
| How far back can ice cores go? | ~800 kyr (EPICA Dome C); a proposed "Beyond EPICA" project targets ~1.5 Myr at low accumulation site |
| What is a carbon isotope excursion (CIE)? | Global negative shift in δ¹³C recording rapid injection of ¹³C-depleted carbon into the ocean-atmosphere system; used for global correlation |
| What limits the boron pH proxy? | Vital effects in foraminiferal calcification; changes in seawater δ¹¹B over time; species-specific calibration required |

---

## Common Confusion Points

**δ¹⁸O in marine carbonates reflects BOTH temperature and ice volume**: This is the most common error in popular science. A negative excursion could mean warmer OR less ice (or both). The DSDP/ODP/IODP benthic foram stack requires Mg/Ca to deconvolve. Always specify what you're interpreting.

**Amount effect vs temperature effect on δ¹⁸O**: In mid-to-high latitudes, lower temperature → more negative δ¹⁸O (temperature effect dominates). In tropical monsoon regions, heavier rainfall → more negative δ¹⁸O (amount effect dominates). The same signal means different things in different settings.

**Ice core CO₂ lags temperature by ~800 yr in glacial cycles**: This does NOT mean CO₂ doesn't drive climate. During deglaciation, the initial warming is triggered by insolation (Milankovitch), then CO₂ rises (degassing from warming ocean) and amplifies via greenhouse feedback. The CO₂ lag is a feedback confirmation, not a refutation of CO₂'s role.

**Speleothem age uncertainty**: U-Th dating of speleothems requires the system to have been closed to U and Th since formation. Detrital Th contamination (from clay particles) requires correction. Ages are typically reported with ±2σ uncertainties of 0.1-2% depending on age and sample quality.
