# Geologic Time — Radiometric Dating, Stratigraphy, Mass Extinctions

**Bridge — relative vs absolute dating as logical clocks vs wall clocks:** Any distributed systems engineer knows the Lamport clock / vector clock distinction: logical clocks establish *happened-before* ordering (A occurred before B) without providing wall-clock timestamps. Steno's stratigraphic principles are exactly Lamport clocks for rock layers: superposition gives you a total ordering of events (this layer is younger than that one; this dike is younger than the rock it cuts), but no timestamps. William Smith's faunal succession extends this across disconnected outcrops — like a distributed system where each node's local log can be synchronized via shared causal events (fossil assemblages). Radiometric dating is the wall clock: it adds absolute timestamps to the logical sequence, calibrating the relative ordering to SI units of time. The analogy holds for precision too: U-Pb dating of zircon achieves <0.1% precision on billion-year-old events — equivalent to timestamping a distributed transaction to within a millisecond despite the event occurring a decade ago.

## The Big Picture

Before the 20th century, geologists could only determine *relative* time (A is older than B). Radiometric dating (post-1905) provided *absolute* time. The combination — stratigraphy for sequence + radiometric dating for calibration — built the geologic time scale to its current precision of <0.1% uncertainty in many periods.

```
+---------------------------------------------------------------+
|           TWO PILLARS OF GEOLOGIC TIME                        |
|                                                                |
|  RELATIVE DATING              ABSOLUTE DATING                 |
|  (sequence, not numbers)      (numbers from isotope decay)    |
|                                                                |
|  Steno's principles           Radiometric methods:            |
|  Faunal succession            U-Pb, K-Ar, Rb-Sr              |
|  Lithostratigraphy            Ar-Ar, Sm-Nd, Re-Os            |
|  Biostratigraphy              U-series, C-14 (short times)   |
|  Magnetostratigraphy                                          |
|  Chemostratigraphy            RESULT: ages with error bars   |
|                                                               |
|  RESULT: sequence of          RESULT: absolute age in        |
|  events, no numbers           Ma or Ga                       |
+---------------------------------------------------------------+
```

---

## Relative Dating Principles

These establish *which came first* without any numbers:

```
PRINCIPLE              STATED BY     APPLICATION
---------------------  -----------   ----------------------------------
Superposition          Steno 1669    Lower strata = older (undeformed)
Original horizontality Steno         Tilted beds were deformed after deposit
Lateral continuity     Steno         Beds extend until environment changes
Cross-cutting          Steno         Dike/fault is younger than what it cuts
Inclusion              Steno         Clast/xenolith older than hosting rock
Unconformity           Hutton 1788   Gap in record; missing time
Faunal succession      W. Smith 1799 Each stratum has unique fossil assemblage
Index fossil           Smith         Specific fossils = specific time interval
```

### Types of Unconformity

```
ANGULAR                    DISCONFORMITY              NONCONFORMITY
UNCONFORMITY               (parallel layers but       (sediment on igneous/
                           with gap/erosion)           metamorphic)

  ///////  older tilted            ~~erosion~~        ======= sediment
  ///////  strata                  ==========         -------
  -------                          ==========         ******* granite
  ======= younger strata          ==========         ******* (basement)
  =======                         ==========
                                   (time gap implied
                                    by fossil absence)
```

Hutton's famous unconformity at Siccar Point (1788): tilted Silurian rocks beneath horizontal Devonian — "no vestige of a beginning, no prospect of an end" (recognition of deep time).

---

## Radiometric Dating — The Physics

Radioactive isotopes decay at constant rates described by first-order kinetics:

```
N(t) = N₀ × e^(-λt)

Where:
  N₀ = initial number of parent atoms
  N(t) = remaining parent atoms at time t
  λ = decay constant (unique to each isotope)
  t₁/₂ = half-life = ln(2)/λ

SOLVING FOR AGE:
  t = (1/λ) × ln(1 + D/P)

Where:
  D = daughter isotope (measured)
  P = parent isotope (measured)
  λ = known decay constant
```

### Key Dating Systems

| System | Parent → Daughter | Half-life | Age Range | Best For |
|--------|-----------------|-----------|-----------|---------|
| **U-Pb** | ²³⁸U→²⁰⁶Pb, ²³⁵U→²⁰⁷Pb | 4.47 Ga, 704 Ma | 1 Ma – 4.6 Ga | Zircon; most robust |
| **K-Ar** | ⁴⁰K→⁴⁰Ar | 1.25 Ga | 10 ka – 4.6 Ga | Volcanic rocks, micas |
| **Ar-Ar** | ³⁹Ar proxy | (same decay) | 10 ka – 4.6 Ga | Better than K-Ar (same sample simultaneous measurement) |
| **Rb-Sr** | ⁸⁷Rb→⁸⁷Sr | 48.8 Ga | 10 Ma – 4.6 Ga | Metamorphic, igneous |
| **Sm-Nd** | ¹⁴⁷Sm→¹⁴³Nd | 106 Ga | >100 Ma | Ancient rocks, garnets |
| **Re-Os** | ¹⁸⁷Re→¹⁸⁷Os | 41.6 Ga | >100 Ma | Sulfide minerals, organic-rich shale |
| **U-series** | ²³⁸U→²³⁴U→²³⁰Th | 75 ka (Th) | 1 ka – 500 ka | Carbonates, coral, speleothems |
| **¹⁴C** | ¹⁴C→¹⁴N | 5,730 yr | 100–50,000 yr | Organic carbon; archaeology |

### Concordia Diagram (U-Pb)

The power of U-Pb dating: two independent clocks (²³⁸U/²⁰⁶Pb and ²³⁵U/²⁰⁷Pb). If both give same age = concordant → highly reliable. If discordant, the Wetherill concordia diagram shows when lead was lost (metamorphic event) and when the mineral originally crystallized.

```
²⁰⁷Pb/²³⁵U
    ^          Concordia curve
    |         /          Each point on curve = a specific age
    |        / (concordant data plot ON the curve)
    |       /
    |      *  (discordant points plot BELOW the line)
    |     / \
    |    /   \
    +---/-----\----------------> ²⁰⁶Pb/²³⁸U
        (upper intercept = original crystallization age)
        (lower intercept = disturbance event)
```

**Zircon (ZrSiO₄)** is the ideal U-Pb geochronometer: incorporates U but not Pb on crystallization (initial Pb correction is zero), extremely resistant to diffusion and weathering. World's oldest zircon grains: Jack Hills, Australia at 4.4 Ga.

---

## The Geologic Time Scale — Calibrated

Full eon→era→period→epoch hierarchy:

```
EON           ERA          PERIOD           EPOCH               Ma
----------    ----------   ---------------  ------------------  ------
PHANEROZOIC   CENOZOIC     Quaternary       Holocene            0.0117
                                            Pleistocene         2.58
                           Neogene          Pliocene            5.33
                                            Miocene             23.0
                           Paleogene        Oligocene           33.9
                                            Eocene              56.0
                                            Paleocene           66.0
              MESOZOIC     Cretaceous                           145.0
                           Jurassic                             201.3
                           Triassic                             251.9
              PALEOZOIC    Permian                              298.9
                           Carboniferous    Pennsylvanian       323.2
                                            Mississippian       358.9
                           Devonian                             419.2
                           Silurian                             443.8
                           Ordovician                           485.4
                           Cambrian                             538.8

PROTEROZOIC   NEOPROTER.   Ediacaran                           635
              MESOPROTER.                                       1000
              PALEOPROTER.                                      1600–2500

ARCHEAN                                                         2500–4000

HADEAN                                                          4000–4600
```

**GSSP (Global Boundary Stratotype Section and Point)** — The formal "golden spike" that defines each time boundary as a specific point in a specific rock outcrop. Ratified by International Commission on Stratigraphy.

---

## The Fossil Record — Biostratigraphy

**Index fossil** = species with:
1. Wide geographic distribution (correlate across continents)
2. Short stratigraphic range (precise time indicator)
3. Easy identification
4. Abundance

Classic index fossils: Graptolites (Ordovician-Silurian), Ammonites (Triassic-Cretaceous), Foraminifera (Mesozoic-Present), Trilobites (Cambrian-Permian).

**Biozone types:**
- Range zone: extent of one species' occurrence
- Concurrent range zone: overlap of two species
- Abundance zone: peak occurrence of a species

---

## Mass Extinctions — Catastrophic Boundary Events

The Big 5 (and their causes/recovery times):

```
EXTINCTION   AGE (Ma)  LOSS (MARINE)   CAUSE                  RECOVERY
-----------  --------  --------------  ---------------------   --------
End-         444       ~57% genera     Glaciation (Gondwana    5–10 Ma
Ordovician              (2 pulses)      ice sheet) → cooling
                                        + sea level drop

Late         ~375–360  ~35% genera     Multiple pulses;        15–20 Ma
Devonian               (~70% spp)      anoxic oceans;
                                        possibly impacts

End-Permian  252.17    ~96% marine     Siberian Traps LIP      8–10 Ma
(P-T)                  genera;         → CO₂, SO₂, methane;   (slowest
                        ~70% land spp  ocean anoxia;           recovery)
                        (worst ever)    temp +10°C

End-         ~201      ~47% genera     CAMP LIP + initial      4–6 Ma
Triassic               (disputed)      Atlantic rifting;
                                        ocean acidification

K-Pg         66.04     ~75% spp        Chicxulub impactor      2–4 Ma
                        (non-avian      (~10 km) + Deccan       (birds,
                        dinos, mosasaurs, Traps LIP;            mammals
                        ammonites)       "impact winter"       radiate)
```

**Current extinction** — the "Sixth Mass Extinction": species loss rates 100–1000× background. Unlike the Big 5, this one is biotic-driven (Homo sapiens).

---

## Chemostratigraphy — Chemical Signals in Rock

```
SIGNAL                 WHAT IT RECORDS             USE
--------------------   -------------------------   -----------------------
δ¹³C excursion         Carbon cycle perturbation   Mass extinctions, PETM
(negative spike)       (organic carbon burial       (Paleocene-Eocene
                        or methane release)          Thermal Maximum)

δ¹⁸O (foraminifera)    Seawater temperature +       Ice volume, ocean temp
                        ice volume                    (paleoclimate proxy)

⁸⁷Sr/⁸⁶Sr in          Continental weathering        Mountain building phases,
seawater carbonates    intensity                      sea level changes

Iridium anomaly        Extraterrestrial input         Impact events (K-Pg
                        (chondritic abundance)         boundary 30×-300×
                                                       background)

Pt, Os anomalies        Same as Ir                    Impact + LIP volcanism
```

---

## Decision Cheat Sheet

| Dating need | Method |
|-------------|--------|
| Age of volcanic rock (K-feldspar, biotite) | Ar-Ar or K-Ar |
| Age of zircon (any igneous) | U-Pb (TIMS or SHRIMP) |
| Age of organic material <50,000 yr | Radiocarbon (¹⁴C) |
| Age of cave speleothem or coral | U-series (²³⁰Th/²³⁴U) |
| Age of very old metamorphic terrain | Sm-Nd or Lu-Hf |
| Age of sulfide ore deposit | Re-Os |
| Time sequence without numbers | Steno's principles + biostratigraphy |

---

## Common Confusion Points

**Half-life and useful range** — ¹⁴C (t₁/₂ = 5,730 yr) can only date material up to ~50,000 yr (≈8–9 half-lives; beyond that, insufficient ¹⁴C remains to measure). Using ¹⁴C on a million-year-old sample gives spurious "young" ages from contamination. Always match method to age range.

**Radiometric dating errors** — Error bars (e.g., "252.17 ± 0.06 Ma") reflect measurement precision, not fundamental uncertainty. Modern U-Pb can achieve <0.1% precision. The GTS boundary dates are themselves refined continuously as new measurements come in.

**"Carbon dating" ≠ all radiometric dating** — ¹⁴C dates *organic* material *younger* than ~50,000 years. It cannot date rocks, fossils (unless organic), or anything in the millions-of-years range. Journalists (and some textbooks) conflate all radiometric dating with "carbon dating."

**Geologic column ≠ any single real section** — The standard geologic column is a composite constructed from hundreds of sections worldwide where particular periods have the best exposures. No single place on Earth shows all periods continuously.
