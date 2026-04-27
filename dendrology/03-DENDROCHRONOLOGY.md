# Dendrochronology: Tree Rings, Climate Records, Cross-Dating

## The Big Picture

Dendrochronology is the science of using tree-ring sequences as a high-resolution proxy for time and past environmental conditions. A tree ring is a physical record of one year's cambial activity — its width, density, and chemistry encode the growing-season conditions of that year with annual precision. The field extends calendar-year records back ~13,000 years and serves as the primary calibration tool for radiocarbon dating.

```
DENDROCHRONOLOGY FRAMEWORK

  RING ANATOMY:
  +------------+
  | Earlywood  |
  | Latewood   |
  | Width      |
  | Density    |
  | Chemistry  |
  +------------+
        |
        v
  CLIMATE SIGNAL (temp, precip, drought, CO2)

  CROSS-DATING:
  +-------------+
  | Living trees|
  | Dead trees  |
  | Subfossil   |
  | wood        |
  +-------------+
        |
        v
  CALENDAR YEAR ASSIGNMENT (exact dates)

  MASTER CHRONOLOGY:
  +-----------------------+
  | Last ring = present   |
  | Floating chrono.      |
  | Extended back         |
  | thousands of years    |
  +-----------------------+
        |
        v
  14C CALIBRATION — IntCal curves
  (archaeology, geology, ecology)
```

---

## Section 1 — Ring Anatomy: Earlywood and Latewood

Each annual ring in a temperate, seasonal-climate tree consists of two zones formed in sequence:

```
RING STRUCTURE (transverse section):

  <------------ ONE ANNUAL RING ------------>
  +===========+---------------------------+
  | EARLYWOOD |        LATEWOOD           |
  +===========+---------------------------+
  |Wide lumen |  Narrow lumen             |
  |Thin wall  |  Thick wall               |
  |Low density|  High density             |
  |Light color|  Dark color               |
  +===========+---------------------------+
       ^                  ^
  Rapid spring        Summer stress,
  growth, water       season-end signal
  availability

  RING BOUNDARY: latewood of year N | earlywood of year N+1
  (sharp boundary, visible without magnification in most species)
```

### What Ring Width Encodes

Ring width integrates **all factors** limiting cambial growth during the season:

```
  RING WIDTH = f(temperature, precipitation, photoperiod, nutrients,
                  competition, insect damage, fire stress, CO2, age)

  LIMITING FACTOR model:
  In any given year, the MOST LIMITING resource controls ring width
  --> cool-summer species: width ~ summer temperature
  --> semi-arid species: width ~ annual/growing-season precipitation
  --> humid, temperate species: mixed signal (less useful climatically)
```

### Maximum Latewood Density (MXD)

A second proxy variable: the maximum X-ray density of the latewood zone. MXD is a stronger temperature signal than ring width for many high-latitude/high-altitude conifers — specifically capturing **late-summer temperature**. Used in the Northern Hemisphere temperature reconstructions (Briffa et al., Science 1998).

---

## Section 2 — Cross-Dating: The Core Method

Cross-dating is the matching of ring-width patterns (or other ring characteristics) from multiple trees to establish absolute calendar dates. It is the methodological foundation without which dendrochronology cannot function.

```
CROSS-DATING LOGIC:

  Tree A: rings from 1823–2024 (living)
  +--+--+-+--+--++--+--+-+-++--+--+--+
  year:  1823 ...  1900 ... 1950 ... 2024

  Tree B: old wood (beam from building), approximate age unknown
  +--+-+-++--+--+--++--+--+-+-++--+--+
  The PATTERN of wide and narrow rings is unique to a climate period

  Cross-dating: slide B along A until patterns align

    Tree A: --+--+-+--+--++--+--+-+-++--+--+--+
    Tree B:             +--+-+-++--+--+--+
              ^                 ^
          year 1867           year 1923
          (beam felled after 1923)
```

### The "Pointer Year" Concept

Pointer years are years with an exceptionally strong growth response shared across a region — very narrow rings in dry/cold years, very wide rings in optimal years. They serve as anchors:

- Negative pointer: frost year, severe drought
- Positive pointer: exceptional growing season
- Volcanic events (e.g., Tambora 1815, Pinatubo 1991) leave frost-ring scars or suppressed rings across continental scales

### COFECHA and Statistical Cross-Dating

Modern cross-dating uses software (COFECHA) that computes Pearson correlations between 50-year overlapping windows of each series against the master chronology. Acceptable correlation threshold typically r > 0.3 (p < 0.01), but for confident dating r > 0.5 preferred.

---

## Section 3 — Building a Master Chronology

A master chronology is a composite ring-width record built by averaging detrended ring-width series from many trees. The averaging suppresses tree-individual variation and amplifies the shared climate signal.

```
CHRONOLOGY CONSTRUCTION PIPELINE:

  [Field sampling]
      |   -- increment borer; 2 cores per tree, at breast height
      |   -- minimum 20 trees per site for robust signal
      v
  [Skeleton plotting / visual cross-dating]
      |   -- pencil marks on graph paper (narrow rings = tall marks)
      |   -- pattern matching by eye before computer
      v
  [Ring measurement]
      |   -- optical measuring stage, 0.001 mm resolution
      |   -- or digital image analysis (WinDENDRO, CooRecorder)
      v
  [Detrending (standardization)]
      |   -- removes age-related trend (rings get narrower as tree ages)
      |   -- fits curve (negative exponential, cubic spline, etc.)
      |   -- produces Ring Width Index (RWI): deviations around trend
      v
  [Averaging / Signal-Free Standardization]
      |   -- Express Population Signal (EPS) must be > 0.85
      |   -- Running Window Analysis of Variance
      v
  [Master Chronology]
      -- final product: annual RWI series with expressed climate signal
      -- archived in ITRDB (International Tree Ring Data Bank, NOAA)
```

### Detrending Methods

| Method | Removes | Preserves | Use Case |
|--------|---------|-----------|----------|
| Negative exponential | Age trend | High/medium frequency | Most common; conservative |
| Cubic smoothing spline | Age + low-frequency trends | High frequency | Climate variability > 100 yr removed |
| Regional Curve Standardization (RCS) | Age trend only | ALL frequencies | Millennium-length temperature reconstruction |
| Signal-free method | Trend + circular bias | Climate signal | Best practice; Melvin & Briffa 2008 |

---

## Section 4 — The Bristlecone Pine Record

The longest continuous tree-ring chronology comes from Great Basin bristlecone pine (*Pinus longaeva*) in the White Mountains of California and the Schulman Grove at ~3,400 m elevation.

```
BRISTLECONE PINE CHRONOLOGY:

  Living trees: up to ~4,850 yr (Methuselah, WPN-114)
                up to ~5,067 yr (unnamed, discovered 2012)

  Dead subfossil wood: found on surface (preserved by cold, dry conditions)

  Chronology reaches back: ~9,000 years BP (before present)

  Environmental conditions (limiting factors):
  +-- High elevation: summer temperature is primary growth limit
  +-- Semi-arid: low precipitation and slow decomposition preserves wood
  +-- Exposed ridge: wind removes snow quickly; cambium active only June–Aug
  +-- Age: tree rings become microscopically thin in extreme old age
      --> specialist preparation, polarized light microscopy required

  CLIMATE SIGNAL: Ring width + MXD = summer temperature proxy
  Key reconstruction: Salzer et al. (2014) — last 3,700 yr summer temperature
```

### Why Bristlecones Matter for Radiocarbon

The bristlecone chronology provided the first calibration of radiocarbon dates to calendar years (Suess, 1970). Before this, 14C dates were reported as "radiocarbon years BP" with no calendar correction. The Suess curve revealed wiggles in atmospheric 14C — caused by solar activity (de Vries effect) and ocean circulation — that made calibration non-trivial.

---

## Section 5 — Radiocarbon Calibration

### The Calibration Problem

Radiocarbon dating assumes atmospheric 14C concentration has been constant. It has not. Variations caused by:
1. **Solar activity** (11-yr Schwabe cycle, 87-yr Gleissberg, 205-yr deVries/Suess cycles)
2. **Ocean circulation** (deep-water upwelling changes the fraction of 14C in surface CO2)
3. **Geomagnetic field strength** (modulates cosmic ray flux)

```
CALIBRATION CURVE STRUCTURE:

  CALENDAR YEAR (x-axis)   <-- from tree rings (exact)
  14C YEARS BP (y-axis)    <-- from AMS or decay counting

  Ideally: straight 1:1 diagonal line
  Reality:
    +-- Wiggles (10–200 yr period): solar Schwabe/deVries cycles
    +-- Plateaus: ~200–500 14C yr span maps to single calendar decade
    +-- Rapid excursions: Miyake events (see below)
    +-- Long-term offset: systematic 14C enrichment/depletion over millennia
```

### IntCal Curves

The **IntCal** family of calibration curves (IntCal20 is current, 2020) is built from:

| Material | Time Range | Precision |
|----------|-----------|-----------|
| Tree rings | 0–13,910 cal yr BP | ±1–5 yr |
| Kauri wood (*Agathis australis*) | 13,000–55,000 cal yr BP | ±20–200 yr |
| Speleothems (U-Th dated) | 14,000–55,000 cal yr BP | ±100–500 yr |
| Varved lake sediments | 10,000–14,500 cal yr BP | ±50–100 yr |
| Foraminifera | > 14,000 cal yr BP | ±200–1000 yr |

Tree rings provide the highest-precision segment (0–14,000 yr BP). Beyond that, other archives take over with progressively larger uncertainty.

### Calibration Plateaus and the "Halstatt Plateau"

The most problematic period for 14C dating is the **Hallstatt Plateau** (~800–400 BC, or ~2800–2400 cal yr BP), where atmospheric 14C was elevated and relatively flat for ~400 years. A single 14C date from this period produces a probability distribution spanning the entire plateau — essentially useless for precise dating. Solution: **wiggle-matching** (dating multiple samples from a sequence and fitting the wiggle pattern).

### Miyake Events

Ultra-rapid rises in atmospheric 14C discovered via tree rings:

| Event | Calendar Year | ΔΔ14C | Cause |
|-------|--------------|-------|-------|
| Miyake 775 | 774/775 CE | +12‰ in 1 yr | Solar proton event (SPE) |
| Miyake 993 | 993/994 CE | +9‰ in 1 yr | SPE |
| Miyake ~5480 BCE | 5480–5470 BCE | +18‰ | Unclear; possibly SPE |

These are useful as absolute time markers — any wood containing the 775 CE ring can be dated to exactly that year by measuring 14C in the specific ring.

---

## Section 6 — Climate Proxy Records

### Types of Dendroclimatic Reconstructions

```
RECONSTRUCTION TARGETS:

  TEMPERATURE:
  Best proxies: high-elevation or high-latitude conifers (T-limited)
  Methods: MXD preferred over ring width; multiple regression on instrumental data
  Reach: 1,000+ yr with reasonable confidence; 2,000 yr with careful calibration

  PRECIPITATION / DROUGHT:
  Best proxies: semi-arid species (precipitation-limited)
  Index: Palmer Drought Severity Index (PDSI) reconstructed from ring width
  Examples: North American Drought Atlas (Cook et al.) — 2,000 yr PDSI grid

  VOLCANIC FORCING:
  Frost rings (frozen cambial cells) in conifers: growing season frost event
  Multiple trees affected simultaneously = large volcanic eruption signal
  Tambora 1815: widest growth suppression in N. Hemisphere record
  Toba ~74,000 BP: detectable but ring records don't reach this far

  SOLAR ACTIVITY:
  14C in tree rings (produced by cosmic ray flux inversely related to solar output)
  10Be from ice cores + tree ring calendar = combined solar proxy
```

### Verification and Calibration Procedure

Dendroclimatic reconstructions are not taken at face value. Standard protocol:

```
  [Calibration period]: overlap of tree-ring record with instrumental data
    --> typically 1850–present; some records to 1700 with careful screening
    --> regression tree-ring index on climate variable

  [Verification period]: hold-out period not used in calibration
    --> compute r², RE (reduction of error), CE (coefficient of efficiency)
    --> RE > 0 and CE > 0 required for credible reconstruction

  [Validation]: compare to independent proxies (speleothems, ice cores, historical docs)
```

---

## Section 7 — Skeletal Plotting

Before computing software, cross-dating was done entirely by hand on skeleton plots. Still taught as the foundational method.

```
SKELETON PLOT (1 column per ring year, height = departure from expected):

  Year:   1890 1891 1892 1893 1894 1895 1896 1897 1898 1899
  Plot:    |    |    |  | |    |    |  | |    |    |  | |
           |    |    | || |    |    | || |    |    | || |
           |    |    ||||  |   |    ||||  |   |    ||||
           |    |  ||||||  |   |  ||||||  |   |  ||||||

  Tall bar = narrow ring (deficient year -- drought/cold)
  Short bar = normal
  No bar    = average to wide ring (no mark needed)

  Pointer years (very tall bars) create the matching fingerprint
  Cross-dating: pattern of tall bars must align between samples
  A "signature year" visible in 80%+ of trees in a region
    --> 1816 ("Year Without a Summer", Tambora): widely expressed
```

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| What method dates a medieval roof beam to a specific year? | Cross-dating against regional master chronology |
| Why can't I date a tropical hardwood beam by ring count alone? | Tropical rings may not be annual; need anatomical verification |
| What is the longest continuous tree-ring chronology? | Great Basin bristlecone: ~9,000 yr BP |
| Why does a 14C date sometimes span 400 years of calendar time? | Calibration plateau (Hallstatt, ~800–400 BC) |
| What is the MXD proxy and when is it preferred over width? | Maximum latewood density; preferred for summer temperature reconstruction in northern conifers |
| How is a dendroclimatic reconstruction validated? | Split-period calibration/verification with RE and CE statistics > 0 |
| What event produces a detectable frost ring across a continent? | Large volcanic eruption causing growing-season frost (Tambora 1815) |

---

## Common Confusion Points

**Ring count ≠ cross-dating.**
Simply counting rings on a stump does not give a calendar date and cannot distinguish missing rings from multiple rings. Cross-dating with a master chronology is required.

**Missing rings are real and common under stress.**
A tree under severe drought may fail to form a complete ring. This produces a "missing ring" that will be misidentified as one fewer year. This is why minimum sample depth (≥20 trees) and rigorous cross-dating are mandatory.

**False rings (intra-annual density fluctuations) can mimic annual rings.**
Droughts mid-season can create latewood-like tissue before a return to normal growth. Anatomically indistinguishable from a ring boundary unless confirmed by crossdating. Most common in Mediterranean species, semi-arid conifers.

**Radiocarbon years BP are not calendar years BP.**
A "radiocarbon date of 3500 BP" calibrates to ~3,800–3,900 cal yr BP (calendar years before 1950). Always use the calibrated age with probability distribution (OxCal, Calib, or Bchron software) — never report raw 14C age as a calendar date.

**Dendrochronology is not just about climate.**
Applications include: archaeology (building construction dates), art history (panel painting dates — Dendro of Dutch masters), forensic science (timber trafficking), ecology (fire history, insect outbreak cycles), hydrology (flood reconstruction from scar records).
