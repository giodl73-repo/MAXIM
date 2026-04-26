# Archaeological Dating Methods

## The Big Picture

```
+------------------------------------------------------------------+
|              DATING METHODS BY TIME RANGE                        |
|                                                                  |
|  Method         Useful range     Material        Precision       |
|  ─────────────────────────────────────────────────────────────   |
|  Radiocarbon    0–50,000 BP      Organic matter  ±20–200 yr      |
|  Dendrochronology 0–13,000 BP   Tree rings      ±1 year          |
|  OSL/IRSL       100–500,000 BP  Sediments       ±5–15%           |
|  TL             100–500,000 BP  Heated minerals ±5–15%           |
|  K-Ar / Ar-Ar   >100,000 BP     Volcanic rock   varies           |
|  U-series       1,000–500,000 BP Carbonate/bone ±1–2%            |
|  Archaeomagnetic 0–10,000 BP    Fired contexts  ±25–100 yr       |
|  Dendro+C14     0–14,000 BP     Charcoal/grain  very high        |
|  Typology/seriation Relative     Artifact form  comparative      |
+------------------------------------------------------------------+

TWO TYPES:
  ABSOLUTE dating: gives calendar years (or range) — the actual age
  RELATIVE dating: gives older/younger sequence — no calendar age
```

---

## Radiocarbon Dating (¹⁴C)

The most widely used absolute dating method in archaeology.

### The Physics

```
¹⁴C PRODUCTION AND DECAY:
  Cosmic rays → neutrons → hit ¹⁴N in upper atmosphere
  ¹⁴N + n → ¹⁴C + p (nuclear reaction)
  ¹⁴C + O₂ → ¹⁴CO₂ → enters photosynthesis → incorporated into all life

  ¹⁴C/¹²C ratio in living organisms ≈ atmospheric ratio (~1.2 × 10⁻¹²)
  At death: no new ¹⁴C incorporated → existing ¹⁴C decays

RADIOACTIVE DECAY:
  N(t) = N₀ · e^(−λt)
  where:
    N(t) = ¹⁴C atoms at time t
    N₀   = initial ¹⁴C atoms at death
    λ    = decay constant = ln(2) / t₁/₂
    t₁/₂ = half-life of ¹⁴C = 5,730 ± 40 years (true half-life)
           (5,568 ± 30 yr = Libby half-life, used historically)

  Inverting: t = (1/λ) · ln(N₀/N(t))

  Libby Nobel Prize 1960: invented ¹⁴C dating; brilliant insight
  from basic nuclear physics
```

### The ¹⁴C Date and Conventional Radiocarbon Age

A laboratory measurement gives a **Conventional Radiocarbon Age (CRA)** in "years before present" (BP, where "present" = AD 1950 by convention):

- Expressed as: 3250 ± 35 BP
- The ±35 is the **1-sigma measurement error** (analytical uncertainty)
- This is NOT yet a calendar age — it must be calibrated

### Calibration — The Crucial Step

**The problem**: ¹⁴C production is not constant over time — solar activity, Earth's magnetic field, and other factors vary atmospheric ¹⁴C. If you assume it's constant, you get the wrong calendar date.

**The solution**: calibration against independent chronological records with known calendar ages.

```
CALIBRATION CURVE CONSTRUCTION:
  Tree rings (dendrochronology): each ring = 1 year known age
  ¹⁴C-date the ring → known calendar year → known ¹⁴C ratio
  Build continuous curve back to ~14,000 BP (tree ring)
  Extended by: corals, speleothems, lake varves → IntCal21 curve to 55,000 BP

  IntCal21 (2020): international calibration dataset
  Published by IntCal Working Group; used by OxCal software (Oxford)
```

**Bayesian calibration** (OxCal approach):

```
BAYESIAN CALIBRATION PROCEDURE:
  Prior: the ¹⁴C measurement (normal distribution from lab)
  Likelihood: the calibration curve (probability that true age =
    calendar age given the ¹⁴C measurement)
  Posterior: calendar date probability distribution

  Bayes' theorem: P(age|measurement) ∝ P(measurement|age) × P(age)

This is not unusual statistics — it's the explicit application of
Bayesian inference to the calibration problem.

OUTPUT:
  A probability distribution over calendar years
  Reported as: cal BP 3400–3250 (95.4% probability)
            or: 1450–1300 cal BC (95.4% probability = 2σ range)

MULTI-CONTEXT BAYESIAN MODELLING:
  Combine ¹⁴C dates WITH stratigraphic constraints
  "This charcoal must be older than this grain above it"
  → Dramatically tightens the calendar age ranges
  → Stratigraphic sequence = prior constraints in the Bayesian model
  → Now standard for high-resolution studies
```

### Measurement Methods

| Method | Principle | Sample size | Range |
|--------|-----------|-------------|-------|
| Conventional beta counting | Count beta decays from ¹⁴C | 20–100 g | 0–40 ka |
| AMS (Accelerator Mass Spectrometry) | Count ¹⁴C atoms directly | 1–10 mg | 0–55 ka |

**AMS** (Accelerator Mass Spectrometry) revolutionized ¹⁴C dating (1970s). Instead of waiting for atoms to decay (slow), you accelerate ions and count ¹⁴C atoms directly in a tandem accelerator/mass spectrometer:

```
AMS WORKFLOW:
  Sample → graphite target → sputter → negative C ions
  → Accelerate to MeV energies
  → Magnetic + electric fields → separate by mass
  → Count ¹⁴C / ¹³C / ¹²C ions
  → Ratio → ¹⁴C age

AMS advantages:
  Tiny samples (single seed, 1 mg of charcoal)
  Faster (hours vs. days)
  Better precision for small samples
  → Transformed geoarchaeology; can date individual seeds/bones
```

### Key Problems and Complications

```
RADIOCARBON COMPLICATIONS:
  OLD WOOD EFFECT:
    If long-lived tree is dated, ¹⁴C age = age of ring growth,
    not when the wood was used
    → Short-lived material preferred: single seeds, annual grain,
      short-lived twigs, nuts, animal bone collagen
    → Long-lived charcoal "terminus post quem" (TPQ) at best

  MARINE RESERVOIR EFFECT:
    Ocean ¹⁴C is depleted (old carbon cycling)
    Marine shells appear ~400 years "too old" (regional variation)
    → Correction: Marine20 calibration curve + local ΔR offset
    → Human diet: if diet heavily marine, bone dates offset

  FRESHWATER RESERVOIR EFFECT:
    Rivers drawing on groundwater with old carbon → older apparent ages
    → Can affect fish bone, freshwater mollusc dates significantly

  HARD WATER EFFECT:
    Plants growing in limestone-rich water absorb ¹⁴C-depleted CO₂
    → Dates too old; important for calcareous environments

  CONTAMINATION:
    Modern roots in samples → ¹⁴C-rich contamination → dates too young
    Sample pretreatment (acid-alkali-acid) removes most contamination
    Human handling → skin oils (modern C) contaminate small samples

  BOMB CARBON (post-AD 1950):
    Nuclear testing spiked atmospheric ¹⁴C
    Post-1950 samples unusable with standard calibration
    Forensic application: ¹⁴C in teeth → birth year estimate
```

---

## Dendrochronology

**Tree rings = annual climate record AND calendar chronology.**

```
PRINCIPLE:
  Trees in seasonal climates add one ring per year
  Ring width varies with growing conditions
  → Characteristic pattern of wide/narrow rings

  CROSSDATING:
    Living tree → known ring sequence back 200+ years
    Ancient beam from building → matches pattern from living tree
    → Extends chronology back further
    Pattern from one tree ← → pattern from another overlapping tree
    Build continuous chronology backward
```

**European oak chronology**: back to ~7,000 BC (from Irish bog oaks, German subfossils). This is the calibration anchor for ¹⁴C.

**Precision**: to the calendar year. Sometimes to the season (spring wood vs. late wood).

```
WIGGLE MATCHING:
  Multiple ¹⁴C dates from sequential tree rings
  Each date has a position on the calibration curve
  The ring sequence constrains how they fit together
  → Extremely precise calendar date (±5–10 years)
  Even better: date ¹⁴C + dendro together
```

**Applications**:
- Precise dating of timber buildings (cut date = outermost ring)
- Dating of panel paintings (art history)
- Climate reconstruction (width/density = summer temperature/precipitation)
- Identifying forgeries (wood from wrong period)

---

## Optically Stimulated Luminescence (OSL)

**The principle**: sediment grains (quartz, feldspar) trap electrons in crystal defects when exposed to ionizing radiation from natural radioactivity. When exposed to sunlight or heat, those electrons are released (the "clock resets"). In the dark (buried sediment), electrons accumulate again. Measuring the trapped charge = measuring time since last light exposure.

```
OSL CLOCK MECHANISM:
  Grains exposed to light → electrons escape traps → clock reset to zero
  Grains buried in sediment → radiation from U/Th/K in surrounding soil
    → electrons accumulate in traps (proportional to time × dose rate)
  Lab: stimulate with green/blue light → measure light output (luminescence)
  Equivalent Dose (Gy) = total radiation received
  Dose Rate (Gy/ka) = radiation per unit time (from measured radioactivity)
  Age = Equivalent Dose / Dose Rate

PRECISION: ±5–15% (much less precise than radiocarbon or dendro)
RANGE: 100–500,000 BP (fills gap between C14 and K-Ar)
IDEAL FOR: dating when sediments were deposited, not when artifacts were made
```

**Archaeological applications**:
- Date when a sediment was last exposed to light (buried in a ditch, covered by a floor)
- Date burned flints (heated → zero; cools → accumulates again)
- Middle Paleolithic/Neanderthal sites beyond ¹⁴C range
- Dating submerged or desert sites lacking organic material

**Limitation**: requires that the sediment was fully bleached (zeroed) by light before burial. Incompletely bleached grains → overestimated age. Single-grain OSL measures individual grains to detect partial bleaching.

---

## Thermoluminescence (TL)

Same mechanism as OSL but triggered by heat (not light). Useful for:
- Fired ceramics (zeroed by firing → accumulates since)
- Burned flints (Middle Paleolithic range)
- Brick, tile, terracotta

**Application**: Authenticate ancient ceramics — a genuine ancient pot has accumulated dose; a recently fired fake shows near-zero age. Major authentication tool in art market.

---

## Potassium-Argon (K-Ar) and Argon-Argon (⁴⁰Ar/³⁹Ar)

```
PRINCIPLE:
  ⁴⁰K → ⁴⁰Ar (by electron capture) + ⁴⁰Ca (by beta decay)
  t₁/₂ = 1.25 × 10⁹ years (partial half-life for ⁴⁰Ar branch)

  At volcanic eruption: argon gas released (clock reset to zero)
  After cooling: ⁴⁰Ar accumulates from ⁴⁰K decay
  Measure ⁴⁰Ar/⁴⁰K → age

ARCHAEOLOGICAL USE:
  Cannot date archaeology directly (no K-bearing pottery)
  Dates volcanic tuffs and ash layers CONTAINING or BRACKETING
  archaeological finds

  Example: Olduvai Gorge, Tanzania:
    Bed I tuff dated by K-Ar → 1.85–1.75 Ma
    Homo habilis remains from Bed I → archaeologically bracketed
    Same logic for all East African hominid sites

⁴⁰Ar/³⁹Ar (incremental heating):
  Neutron irradiation converts ³⁹K → ³⁹Ar (proportional to K)
  Progressive heating releases Ar at different T
  → Multiple measurements; detect argon loss; more robust
  → Better for small samples, disturbed samples, very old material
```

---

## Uranium-Series Dating

```
U-SERIES PRINCIPLE:
  ²³⁸U → ²³⁴U → ²³⁰Th ... (decay chain)
  Fresh carbonate (speleothem, coral) incorporates U but not Th
  (Th insoluble in water; U soluble → differential uptake)
  → ²³⁰Th = 0 at formation; grows by ²³⁴U decay
  Measure ²³⁰Th/²³⁴U → age

PRECISION: ±1–2% (very good for its range)
RANGE: 1,000 to ~500,000 years
MATERIALS: speleothems (best), coral, travertine, bone (problematic — open system)

ARCHAEOLOGICAL APPLICATIONS:
  Date flowstone sealing archaeological layers in caves
  Homo sapiens cave art dated by flowstone overlying paint
    → Sulawesi (Indonesia) cave art >45,000 BP
    → Neanderthal art in Spain: 65,000 BP (U-series on stalagmite)
  Date spring deposits in open-air hominin sites
```

---

## Archaeomagnetic Dating

```
PRINCIPLE:
  Earth's magnetic pole "wanders" (secular variation) over centuries
  Fired features (hearths, kilns, burned floors) record the field
  direction at time of last cooling
  If the secular variation curve is known for a region,
  you can match observed direction → calendar date range

CONSTRUCTION OF CURVES:
  Hearths with independent dates (¹⁴C) → known field direction
  Build regional secular variation master curve
  UK curve extends back 4,000+ years with good resolution

PRECISION: ±25–100 years for well-studied regions
MATERIALS: in-situ fired contexts (must not have been disturbed since firing)
REGIONS: Europe has best-developed reference curves
```

---

## Seriation and Typological Dating

**Relative methods**: no calendar age, but establish sequence.

```
SERIATION:
  Ford's frequency seriation (1950s):
  Archaeological types appear, rise in popularity, then decline
  → Battleship-shaped frequency curves
  If assemblages plotted in order so shapes are battleship curves,
  you have the correct chronological sequence (but not absolute dates)

  Useful when you have many assemblages and need to order them
  without independent dates

TYPOLOGICAL DATING:
  Well-dated artifact types (coins, pottery forms, brooches) used
  to date the contexts they come in:
  → Roman Samian pottery: many forms dated by known kiln sites
  → British coins: dated to reign and sometimes specific year
  → Terra sigillata: factory stamps datable to Dragendorff forms
  → TERMINUS POST QUEM (TPQ): layer can't be earlier than its latest datable artifact
  → TERMINUS ANTE QUEM (TAQ): layer must be earlier than what seals it
```

---

## Combining Methods — Bayesian Modelling

Modern practice combines multiple independent dating methods with stratigraphic constraints in a Bayesian framework:

```
BAYESIAN SEQUENCE MODELLING (OxCal software):
  Input:
    ¹⁴C dates on specific materials from specific contexts
    Stratigraphic sequence (from Harris Matrix)
    Dendro dates where available
    Coin TPQ dates

  Model structure:
    SEQUENCE { (stratigraphic order)
      Phase { early contexts → C14 dates }
      Phase { middle contexts → C14 dates }
      Phase { late contexts → C14 dates + coin TPQ }
    }

  Output:
    Posterior probability distributions for each event
    Phase start/end dates with realistic probability ranges
    Overall model goodness-of-fit test (A% agreement index)

This approach can reduce single-date uncertainties from ±200 years
to ±20–50 years when stratigraphic sequence well-defined.

Stonehenge phasing study (Darvill/Parker Pearson 2012, Bayesian):
  Combined 25 ¹⁴C dates with stratigraphic sequence
  Defined phases with ±15–50 year precision
  Far better than any individual date alone
```

---

## Decision Cheat Sheet

| Situation | Preferred Method |
|-----------|-----------------|
| Charred wood or grain, 0–50 ka | AMS ¹⁴C + Bayesian calibration |
| Single-year precision for timber structure | Dendrochronology |
| Sediment burial date, 10–500 ka | OSL (single-grain for partial bleaching risk) |
| Fired ceramics authentication or dating | TL |
| East African hominin site with volcanic tuff | K-Ar / ⁴⁰Ar/³⁹Ar on tuff |
| Cave site with speleothem sealing archaeology | U-series on flowstone |
| Medieval British sequence with hearths | Archaeomagnetic dating |
| Multiple ¹⁴C dates + stratigraphy | Bayesian modelling in OxCal |
| No organic material, known artifact type | Typological dating (TPQ/TAQ) |

---

## Common Confusion Points

**¹⁴C date ≠ calendar date**: A raw ¹⁴C age (e.g., "3250 ± 35 BP") is NOT a calendar year BC/AD. It must be calibrated against the IntCal curve using software (OxCal, CALIB, BCal). Never report uncalibrated ¹⁴C dates as calendar years.

**Short-lived vs. long-lived carbon**: Charcoal from a tree that lived 400 years has ¹⁴C ages spanning 400 years. Dating the charcoal tells you when the wood formed, not when it was burned. Single seeds, annual grain, bone collagen (from the animal's diet during its lifetime) are much better — they represent a short biological window.

**OSL dates sediment burial, not artifact manufacture**: An OSL date on sand tells you when that sand was last exposed to light, not when the artifact in it was made. This is a proxy for burial date if the sediment was undisturbed.

**Marine reservoir correction is not uniform**: The ocean's ¹⁴C offset varies regionally (from ~300 to >1,000 years) due to oceanographic factors (upwelling, circulation). Always apply a local ΔR correction. The standard marine calibration (Marine20) gives global average; regional datasets refine it.

**K-Ar dates volcanic minerals, not bones**: K-Ar cannot directly date hominin bones or artifacts. It dates the volcanic rocks (tuffs, lava flows) that geologically bracket the archaeological horizon. The archaeological age is inferred from the bracketing geology, not directly from the remains.

**Wiggle-matching is not the same as dendrochronology**: Wiggle-matching uses ¹⁴C dates at known ring-number intervals on wood without extending a ring-width chronology. It's a combined C14 + tree ring spacing approach. Full dendrochronology requires matching ring-width patterns to a master chronology — it doesn't just count rings.
