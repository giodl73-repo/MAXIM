# Stratigraphy — Rock Strata, Relative Dating, Index Fossils, Unconformities, GSSP Boundary Markers

## The Big Picture

```
+===========================================================================+
|                  STRATIGRAPHY AS VERSION CONTROL                           |
|     The rock record is a commit history; strata are commits; disconform-  |
|     ities are deleted commits; GSSPs are release tags                     |
+===========================================================================+
|                                                                           |
|  TOOLS:                                                                   |
|  Lithostratigraphy:   rock TYPE and character → physical tracing          |
|  Biostratigraphy:     fossil content → time                               |
|  Chronostratigraphy:  age of strata → absolute time scale                 |
|  Magnetostratigraphy: magnetic polarity → GPTS calibration                |
|  Chemostratigraphy:   isotope and geochemical signals → global events     |
|  Sequence stratigraphy: cyclical sea level → systems tracts               |
|                                                                           |
|  FUNDAMENTAL LAWS:                                                        |
|  Superposition:    younger strata above older (unless disturbed)          |
|  Original horiz.:  strata form nearly horizontally                        |
|  Lateral continuity: strata extend in all directions until termination    |
|  Cross-cutting:    intrusion/fault is younger than rock it cuts           |
+===========================================================================+
```

---

## Lithostratigraphy

```
STRATIGRAPHIC HIERARCHY AS CONTAINMENT SCHEMA:

  Bed < Member < Formation < Group < Supergroup
  → Containment hierarchy: each unit fully nested inside the next
  → Same structure as: Java packages (com.group.formation.member.bed)
                        DNS labels, URL path segments, filesystem directories
  Formation = "table" in relational DB: bounded, named, independently mappable
  Member = "partition" of a table: subset by lithologic criteria
  Unconformity = schema migration break: older "schema" (rock type) ends;
    new schema begins; gap in record (some versions were never committed)

  Walther's Law: vertical facies sequence = spatial-to-temporal projection
    In a conformable sequence, lateral environments map to vertical layers
    as shoreline migrates: beach → lagoon → offshore, seen in time as a
    vertical stack: offshore mudstone → lagoonal limestone → beach sandstone
    ANALOGY: reading a spatial grammar as a time series
    (same logic as: compiler parsing a sequential token stream that encodes
    a spatial structure — the parse tree reconstructs the grammar)

LITHOSTRATIGRAPHIC UNITS (rock type and character):
  Formation: fundamental unit — named body of rock with distinctive lithology
    Named: geographic locality + rock type (e.g., Green River Formation, Entrada Sandstone)
    Mappable at 1:24,000 scale (typical US geological survey standard)
    Thickness: meters to thousands of meters

  Group: two or more related formations (e.g., Williston Group)
  Member: subdivision of a formation (distinctive subset)
  Bed: smallest formal unit (a layer with consistent character)

  FACIES: rock character reflecting depositional environment
    Turbidite facies: graded beds, Bouma sequence → submarine slope/fan
    Fluvial facies: cross-bedding, channel scours, fining-upward → river
    Carbonate facies: reef core, talus, lagoonal lime mudstone → shallow marine
    Facies transitions: lateral changes in environment → correlate environments
    Walther's Law: in conformable sequence, vertical facies = lateral facies
      (Today's lateral environments become vertical sequence as shoreline migrates)

CORRELATION:
  Physical: trace formation laterally by similar lithology
  Biostratigraphy: match by index fossil occurrence
  Geophysical: well logs (gamma ray, resistivity) → electrofacies
  Seismic: sequence boundaries as reflectors
```

---

## Biostratigraphy

### Index Fossils and Biozones

```
INDEX FOSSIL CRITERIA:
  1. Wide geographic distribution (marine — best for global correlation)
  2. Short stratigraphic range (tight time constraint)
  3. Easily recognizable morphology (non-specialist identification)
  4. Abundant preservation (enough specimens to find everywhere)

  BEST INDEX FOSSILS:
    Planktonic foraminifera (Cenozoic): globally distributed, rapidly evolving
      Foram zones: ~200-kyr precision in favorable sections
    Ammonites (Mesozoic): evolved fast, died at K-Pg → abundant, distinctive
    Graptolites (Paleozoic): planktonic, global, rapidly evolving, simple but distinctive
    Conodonts (Paleozoic-Triassic): phosphatic teeth of eel-like animals
      Extraordinary biostratigraphic precision: 100-kyr zones in some intervals
    Trilobites (Cambrian-Permian): diverse, evolving — Cambrian zonation

BIOZONES:
  Interval zone: defined by first and last appearance of two taxa
  Range zone: range of single taxon (first to last occurrence)
  Assemblage zone: characteristic association of taxa
  Concurrent range zone: overlap of two taxa's ranges (more precise)

  DIACHRONISM: same biozone boundary at different absolute ages in different regions
    Because: organisms migrate between regions over time
    → Biostratigraphic "correlation" is not necessarily exact time correlation
    → Biostratigraphy gives regional relative time; absolute time needs radiometric calibration
```

---

## Chronostratigraphy and the Time Scale

```
CHRONOSTRATIGRAPHIC vs. GEOCHRONOLOGIC UNITS:
  Chronostratigraphy: the ROCKS formed during a time interval
    Eonothem / Erathem / System / Series / Stage (rocks)
  Geochronology: the TIME INTERVAL itself
    Eon / Era / Period / Epoch / Age (time)

  Equivalent: System ↔ Period
              Series ↔ Epoch
              Stage ↔ Age

  Example: "Cretaceous System" = rocks; "Cretaceous Period" = 66–145 Ma time interval

GSSPS — THE SYSTEM OF TAGS:
  Global Standard Stratotype Section and Point:
    Physical reference point in a specific outcrop
    Marks boundary between two chronostratigraphic units (period/epoch/age boundary)
    Defined by: a specific horizon in rock (often with geochemical, biostratigraphic, or magnetic signal)
    Ratified by: International Stratigraphic Commission (ICS)
    Marked by: golden spike (literal metal marker in rock)

  Example — K-Pg Boundary GSSP:
    Location: El Kef, Tunisia
    Marked by: sharp iridium anomaly (high Ir from extraterrestrial source)
    + abrupt change in foram assemblage (tropical species gone, surviving species dominant)
    + clay layer with shocked quartz
    Age: 66.043 ± 0.011 Ma

  DEBATE OVER GSSPs:
    "Anthropocene" GSSPs currently contested (officially NOT ratified as of 2024)
    ~ 100 GSSPs defined in total for 100 formal boundary definitions
```

---

## Unconformities

```
UNCONFORMITY: a gap in the geologic record — missing time between two rock units

  TYPES:

  ANGULAR UNCONFORMITY:
    Lower unit tilted/folded → erosion → upper unit deposited horizontally
    Gap: folding time + erosion time

    LOWER STRATA (tilted, older)
    ────────────────────────────────  ← UNCONFORMITY SURFACE (erosion plane)
    UPPER STRATA (horizontal, younger)

    Famous example: Siccar Point, Scotland (Hutton, 1788)
      Silurian greywackes tilted vertical → unconformity → Devonian Old Red Sandstone
      Hutton: "We find no vestige of a beginning, no prospect of an end"
      → Deep time concept: Earth is very old

  DISCONFORMITY:
    Parallel strata separated by an erosion surface
    Harder to detect (no angular relationship)
    Gap identified by: missing biozones, weathering surface, irregular erosion topography

  NONCONFORMITY:
    Sedimentary rock deposited on eroded igneous or metamorphic rock
    Major gap implied: time for crystalline rock formation + cooling + uplift + erosion

  PARACONFORMITY:
    Parallel strata, no visible erosion surface — but missing time (identified by biostratigraphy)

MAGNITUDE OF GAPS:
  Hutton's Unconformity (Siccar Point): ~80–100 million years of missing record
  Great Unconformity (base of Cambrian in Grand Canyon): 1.2 billion years of missing time
    Pre-Cambrian metamorphic rocks → angular unconformity → Cambrian Tapeats Sandstone
    "The Great Unconformity": 500+ million years of record simply absent
    Cause disputed: Snowball Earth glaciation? Cambrian transgression erosion?
```

---

## Sequence Stratigraphy

```
SEQUENCE STRATIGRAPHY AS CYCLICAL SIGNAL DETECTION:

  Forcing signal: sea level oscillation (Milankovitch orbital cycles, tectonics)
  → Periodic input drives predictable sediment stacking patterns
  → Pattern recognition in rock record = deconvolving the signal from noise
    (diagenesis, local tectonics, erosion gaps = noise on the global signal)

  SYSTEMS TRACTS = STATE MACHINE driven by sea level position:

    State 1: LOWSTAND (sea level below shelf edge)
      Entry: sea level falls below shelf break
      Action: incised valleys cut into shelf; submarine fans build in deep water
      Transition: sea level rises above shelf edge → go to State 2

    State 2: TRANSGRESSION (sea level rising)
      Entry: flooding surface
      Action: shoreline retreats landward; retrogradational stacking
      Transition: rate of rise slows → sediment supply exceeds accommodation → State 3

    State 3: HIGHSTAND (sea level near maximum, slowing)
      Entry: maximum flooding surface (MFS)
      Action: progradational stacking; shoreline builds seaward
      Transition: sea level falls → State 1 (unconformity marks transition)

  Each cycle (State 1→2→3→1) = one depositional sequence bounded by unconformities
  Parasequence = one shallowing-upward event within a systems tract (smaller cycle)
  Stacking patterns: retrogradational (TST), aggradational, progradational (HST)
    → reading the "phase" of the sea level cycle from rock geometry

CONCEPT (Vail, Mitchum, and Posamentier, Exxon Production Research, 1977):
  Sea level changes create predictable rock stacking patterns
  Same pattern repeated worldwide → global sea level signal recognizable everywhere
  Used in: petroleum exploration, basin analysis, correlation

SEQUENCE:
  Package of sediments bounded above and below by sequence boundaries (unconformities)
  Each sequence records: sea level fall → regression → unconformity
                         → sea level rise → transgression → flooding surface
                         → sea level highstand → progradation → next fall

SYSTEMS TRACTS:
  ┌─────────────────────────────────────────┐
  │  Highstand Systems Tract (HST)          │ ← Building out seaward (regression)
  ├─────────────────────────────────────────┤ ← Maximum Flooding Surface (MFS)
  │  Transgressive Systems Tract (TST)      │ ← Backstepping landward (transgression)
  ├─────────────────────────────────────────┤ ← Transgressive Surface
  │  Lowstand Systems Tract (LST)           │ ← Basin floor fans, slope aprons
  └─────────────────────────────────────────┘ ← Sequence Boundary (SB)

  LOWSTAND: incised valleys on shelf, submarine fan in deep water
  TRANSGRESSION: retrogradational stacking (shoreline moves landward)
  HIGHSTAND: progradational stacking (shoreline moves seaward)

PARASEQUENCES:
  Shallowing-upward unit bounded by flooding surfaces
  Water deepens (flooding surface) → gradually shallows as sediment fills
  Stack of parasequences = transgressive systems tract
  Typical thickness: 1–30 m (tidal cycles, orbital cycles)

EUSTASY vs. LOCAL SUBSIDENCE:
  Accommodation = rate of sea level rise (eustasy + subsidence)
  Eustasy: global sea level change
  Subsidence: local crustal sinking (thermal, tectonic loading)
  Both create accommodation for sediment accumulation
  Distinguishing them requires correlation between basins
```

---

## Magnetostratigraphy

```
GEOMAGNETIC POLARITY TIME SCALE (GPTS):
  Earth's magnetic field reverses irregularly (geomagnetic polarity reversals)
  Average reversal frequency: ~4–5 reversals per million years (currently)
  Longest polarity chron: Cretaceous Normal Superchron (120–83 Ma) — 37 Myr without reversal
  Shortest: some chrons last only ~20,000 years

  RECORDING IN ROCK:
    Igneous rock: magnetite minerals align with field during crystallization (thermoremanent)
    Sediment: clay minerals orient during deposition (depositional remanent)

  CHRON NOMENCLATURE:
    C1n (Brunhes Normal): 0–780 ka
    C1r (Matuyama Reversed): 780 ka–2.58 Ma (includes 3 brief normal subchrons)
    C2n (Gauss Normal): 2.58–3.59 Ma

  PRACTICAL USE:
    Paleomagnetic samples from section → normal/reversed sequence
    Match sequence to GPTS → age assignment (requires at least one radiometric anchor)
    Excellent for: continental deposits with no marine biostratigraphy
    (terrestrial mammal sites often rely primarily on magnetostratigraphy)

MAGNETICS IN THE SEAFLOOR:
  Seafloor spreading: new crust records polarity at ridge
  Magnetic anomaly stripes: symmetric about mid-ocean ridge
  Vine-Matthews-Morley hypothesis (1963): explains stripes
  → Confirmed seafloor spreading and plate tectonics
  → Also calibrates the GPTS back to ~170 Ma
```

---

## Chemostratigraphy

```
CARBON ISOTOPES (δ¹³C):
  Photosynthesis preferentially takes up ¹²C → organic carbon is ¹³C-depleted
  Carbonates (shells, limestone) are ¹³C-enriched relative to organic carbon

  NEGATIVE δ¹³C EXCURSION (CIE, Carbon Isotope Excursion):
    Sudden injection of ¹²C-enriched carbon into ocean/atmosphere
    Source: volcanic CO₂ (slightly depleted), methane hydrate dissociation (very depleted)
    Signal: δ¹³C drops in carbonate record
    Examples: P-T boundary (-3 to -6‰), PETM (-3‰), K-Pg (<-1‰)

  POSITIVE δ¹³C EXCURSION:
    Enhanced burial of organic carbon → ocean ¹³C enriched
    Lomagundi event (~2.3–2.1 Ga): largest positive excursion known (+10 to +15‰)
    → Massive photosynthetic burial → oxygen released → Great Oxidation Event

OXYGEN ISOTOPES (δ¹⁸O):
  Primary temperature proxy in marine carbonates
  Temperature effect: colder water → heavier δ¹⁸O in foram shell
  Ice volume effect: continental ice stores ¹⁶O → ocean ¹⁸O-enriched
  Both signals recorded simultaneously → disentangle using Mg/Ca for temperature
  LR04 stack: global Cenozoic δ¹⁸O stack (Lisiecki and Raymo, 2005)
    Shows 41-kyr oscillations until ~1 Ma, then 100-kyr cycles

STRONTIUM ISOTOPES (⁸⁷Sr/⁸⁶Sr):
  Long residence time (~5 Myr) → changes slowly
  Reflects mix of mantle (low ⁸⁷Sr/⁸⁶Sr, unradiogenic) and weathering (high)
  Useful for: large-scale tectonic/erosion rate changes
  Sr curve through geologic time: calibrated independently → correlation tool
  Seawater Sr homogeneous globally → shell measurements = seawater value
```

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| What makes a good index fossil? | Wide distribution, short range, abundant, distinctive morphology |
| What is a GSSP? | Global Standard Stratotype Section and Point — physical rock reference for period boundary |
| What is an angular unconformity? | Lower strata tilted/folded, eroded, then upper strata deposited horizontally |
| What is the Great Unconformity? | ~1.2 Gyr gap at base of Cambrian Grand Canyon section — still debated cause |
| What does chemostratigraphy measure? | Isotope ratios (δ¹³C, δ¹⁸O, ⁸⁷Sr/⁸⁶Sr) in sedimentary rock → global events, correlations |
| What is sequence stratigraphy? | Sea level cycles create predictable sediment packages — used in petroleum exploration |
| How is magnetostratigraphy calibrated? | Match rock normal/reversed sequence to GPTS (calibrated by radiometric dates + seafloor anomalies) |
| What is Walther's Law? | Vertical facies sequence = lateral facies sequence — environments migrate through time |

---

## Common Confusion Points

**Chronostratigraphy ≠ geochronology**: Chronostratigraphy describes rock units (systems, series, stages). Geochronology describes time intervals (periods, epochs, ages). "The Cretaceous System was deposited during the Cretaceous Period." This seems pedantic but matters when discussing whether you're talking about a rock body or a time interval.

**Biostratigraphic zones ≠ time lines**: A biozone boundary is when an organism first or last appeared at a given location. But organisms migrate, and the same species might appear earlier in lower latitudes (favorable conditions) and later in high latitudes (colonization lag). Biozone boundaries are time-transgressive — they're not perfect global time planes. Chemostratigraphic events (δ¹³C excursions, iridium anomaly) are more likely to be instantaneous global signals.

**Sequence boundaries are not just unconformities**: Sequence boundaries include both exposed unconformities on the shelf AND correlative conformities in the deep basin where sedimentation was continuous even during sea level fall. The same boundary appears as a hiatus on the shelf and as a conformable surface in the basin center — same event, different expression.

**Magnetostratigraphy gives relative sequence, not absolute dates**: A polarity sequence of N-R-N-R tells you the sequence but not WHICH chrons. You need at least one independent radiometric age or biostratigraphic tie to anchor the sequence to the GPTS. Once anchored, the remaining chrons fall into place — but pattern matching can be ambiguous if the section has gaps.

**Hutton's unconformity was not just geological observation**: When Hutton discovered Siccar Point in 1788 and realized the angular unconformity represented ~80 Myr of missing time, it was a fundamental philosophical shift. Biblical timescales (~6,000 yr) were incompatible with this — the Earth had to be vastly older than scripture stated. The concept of "deep time" (geological time on million-year scales) was born here, preceding Darwin by 70 years and enabling evolutionary biology.
