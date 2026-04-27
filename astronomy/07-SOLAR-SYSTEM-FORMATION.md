# Solar System Formation
## Nebular Hypothesis, Disk Physics, Accretion, Nice Model, Grand Tack

---

## 1. The Full Formation Sequence

```
  TIMELINE  (t = 0 set by CAI formation = 4.5672 Gyr ago)

  t = 0          Calcium-Aluminum-rich Inclusions (CAIs) condense
                 First solids from solar nebula — oldest dated material
  0–1 Myr        Protoplanetary disk assembled around proto-Sun
                 Dust settles to midplane; grain growth begins
  0–3 Myr        Streaming instability → first planetesimals (~100 km)
  1–5 Myr        Runaway → oligarchic accretion; pebble accretion builds
                 giant planet cores (Jupiter first, then Saturn)
  ~3–5 Myr       Jupiter reaches runaway gas accretion threshold (~10 M_E core)
  ~3–5 Myr       GRAND TACK: Jupiter migrates in to ~1.5 AU, tacks at 2:3
                 resonance with Saturn, migrates back out to ~5.2 AU
  ~5 Myr         T Tauri stellar wind clears disk gas (disk lifetime ~1–10 Myr)
  5–100 Myr      Giant impact phase: planetary embryos collide, terrestrial
                 planets assemble
  50–150 Myr     Moon-forming impact (Theia + proto-Earth → Earth + Moon)
  ~600–800 Myr   NICE MODEL instability: Jupiter/Saturn cross 2:1 MMR →
                 Uranus/Neptune scattered out → LATE HEAVY BOMBARDMENT (LHB)
  ~800 Myr       Solar system reaches roughly current architecture

  THE KEY ACTORS:
  ┌──────────────────────────────────────────────────────────────────────────┐
  │  Solar nebula gas   → carries angular momentum, drives migration         │
  │  Dust/ice grains    → feedstock for all solids                           │
  │  Planetesimals      → first self-gravitating bodies, meteorite parents   │
  │  Planetary embryos  → oligarchic stage, 0.01–0.1 M_Earth                 │
  │  Giant planet cores → ~10 M_Earth, trigger runaway gas accretion         │
  │  Gas giants         → gravitational architects, migration engines        │
  └──────────────────────────────────────────────────────────────────────────┘
```

---

## 2. The Solar Nebula — Disk Formation and Structure

### 2.1 Collapse and Angular Momentum

A molecular cloud core (T ~ 10 K, n ~ 10⁴ cm⁻³) collapses when its Jeans mass is exceeded:

```
  M_J = (5kT/Gm_H)^(3/2) · (3/4πρ)^(1/2)   ← thermal pressure vs self-gravity

  Collapse is not spherical: any slight rotation → centrifugal barrier
  → material falls to centrifugal radius r_c = j²/(GM_*)
    where j = specific angular momentum of infalling gas

  RESULT: disk, not sphere
  ┌───────────────────────────────────────────────────────────────────────┐
  │  Collapsing cloud (slow rotation)  →  protostar + protoplanetary disk │
  │  Disk radius ~ 10–100 AU                                              │
  │  Disk mass ~ 0.01–0.1 M_☉   (typically ~1% of stellar mass)           │
  │  Disk lifetime ~ 1–10 Myr (median ~3 Myr; set by viscous evolution    │
  │                              + photoevaporation by stellar UV/X-ray)  │
  └───────────────────────────────────────────────────────────────────────┘
```

### 2.2 Minimum Mass Solar Nebula (MMSN)

Hayashi (1981): take current planetary masses, add H/He to solar composition, spread:

```
  MMSN surface density profiles:

  Σ_gas  ≈ 1700 (r/1 AU)^(−3/2)  g/cm²     gas+dust together
  Σ_rock ≈ 7.1  (r/1 AU)^(−3/2)  g/cm²     rocky condensates (inside snowline)
  Σ_ice  ≈ 30   (r/1 AU)^(−3/2)  g/cm²     beyond snowline (ice+rock)

  Total disk mass: ~0.01–0.07 M_☉  (MMSN is a lower bound)

  SCALE HEIGHT:
  H/r = c_s / v_K  ≈ 0.033 (r/1 AU)^(1/4)    c_s = sound speed, v_K = Keplerian

  Disk is thin: H/r ~ 3% at 1 AU → "thin disk" approximation valid
  Gas pressure support: v_gas ≈ v_K (1 − η) where η ~ (H/r)² ~ 10⁻³
  → gas orbits slightly sub-Keplerian → headwind on solid particles
```

### 2.3 The Snowline and Condensation Sequence

Temperature decreases outward → different volatiles condense at different distances:

```
  CONDENSATION SEQUENCE (from hot nebula center outward):

  T (K)     Distance    Condensates
  ──────────────────────────────────────────────────────────────────────
  1400      ~0.1 AU     Corundum (Al₂O₃), hibonite, spinel — CAI precursors
  1300      ~0.3 AU     Iron-nickel metal
  1000      ~0.7 AU     Forsterite, enstatite (Mg-silicates)
   680      ~1.0 AU     FeS (troilite), alkali-bearing silicates
   400      ~2.0 AU     Phyllosilicates (hydrous minerals)
   170      ~2.7 AU     H₂O ICE ← THE SNOWLINE
   ~90      ~10 AU      NH₃ ice
   ~50      ~30 AU      CO₂ ice, CH₄ ice, CO ice
  ──────────────────────────────────────────────────────────────────────

  THE SNOWLINE AT ~2.7 AU:
  Beyond snowline: Σ_solid jumps by ~4× (ice adds to rock)
  → crosses oligarchic isolation mass threshold for giant planet cores
  → explains why all giant planets formed beyond ~3 AU
  → explains asteroid belt S-type (dry, inside) vs C-type (wet, outside) gradient

  Snowline migrates inward as disk cools: possibly as close as 1 AU
  at early times → water delivery to Earth via C-type impactors from ~2-4 AU
```

---

## 3. Grain Growth — From Dust to Planetesimals

### 3.1 The Meter Barrier

Grain growth from μm → km involves collisions at increasing relative velocities:

```
  GROWTH REGIMES:

  Size          Mechanism              Outcome
  ────────────────────────────────────────────────────────────────────────
  0.1 μm–1 mm  Brownian motion        Sticking (Van der Waals, charge)
               → fractal aggregates
  1 mm–10 cm   Turbulent relative     Still sticking (at low v_rel)
               velocity               Chondrule-like aggregates
  10 cm–1 m    ← THE METER BARRIER → bouncing, fragmentation, OR
                                      rapid orbital decay:

  METER-BARRIER PROBLEM:
  ┌──────────────────────────────────────────────────────────────────────┐
  │ 1. Bouncing: ~cm particles bounce rather than stick                  │
  │ 2. Fragmentation: ~m particles shatter on collision                  │
  │ 3. Radial drift: sub-Keplerian gas → headwind → inward spiral:       │
  │    dr/dt ≈ −2η v_K St / (1 + St²)    (Stokes number St ≈ 1 at ~1 m)  │
  │    Peak drift at St=1: ~1 AU per ~100 yr at 1 AU → lost to star      │
  └──────────────────────────────────────────────────────────────────────┘
```

### 3.2 Streaming Instability — Skipping the Barrier

```
  KEY INSIGHT (Youdin & Goodman 2005, Johansen et al. 2007):
  Drifting "pebbles" concentrate in pressure maxima or feedback clumps.
  When local solid/gas ratio > ~1: aerodynamic back-reaction on gas
  → gas slows → reduced headwind → pebbles concentrate further
  → runaway: clump collapses gravitationally → PLANETESIMAL

  ┌──────────────────────────────────────────────────────────────────────┐
  │  STREAMING INSTABILITY bypasses meter barrier:                       │
  │  pebbles (~cm–m) → direct gravitational collapse → ~100 km bodies    │
  │  (Kuiper Belt "cold classical" binaries support this: nearly equal   │
  │   size, prograde, low inclination — consistent with pebble cloud     │
  │   collapse, not accretion from random collisions)                    │
  └──────────────────────────────────────────────────────────────────────┘

  Characteristic planetesimal size from streaming: ~50–200 km
  (matches Kuiper Belt size frequency distribution break at ~100 km)
```

---

## 4. Planetesimal Accretion — From 100 km to Planets

### 4.1 Gravitational Focusing and Runaway Growth

```
  GRAVITATIONAL FOCUSING:

  Capture cross-section: σ = πR² (1 + v_esc²/v_∞²) = πR² (1 + Θ)

  Θ = Safronov number = v_esc²/v_∞² = (2GM)/(Rv_∞²)

  For small bodies: Θ ≪ 1 → σ ≈ πR² (geometric, orderly growth M ∝ t)
  For large bodies: Θ ≫ 1 → σ ≈ πR² Θ ∝ M/v²  (runaway growth, M ∝ t^n, n > 1)

  RUNAWAY ACCRETION:
  Large bodies have lower random velocities (dynamical friction from small bodies)
  → larger Θ → larger cross section → grow faster → runaway
  dM/dt ∝ M^(4/3) (runaway regime)

  RESULT: runaway produces a few bodies much larger than the swarm
  → the "runaway body" is an embryo or protoplanet
```

### 4.2 Oligarchic Accretion

```
  Once embryos dominate the local mass:
  → they heat the nearby planetesimals (excite random velocities)
  → smaller bodies have higher v_∞ → lower Θ for all → slower growth
  → growth becomes self-limiting → OLIGARCHIC regime

  Oligarchs are separated by ~3-5 mutual Hill radii:
  R_Hill = r · (M_planet / 3M_☉)^(1/3)
  Spacing: Δa ~ b·R_Hill, b ~ 10

  ISOLATION MASS (when oligarch has accreted all available material in its feeding zone):

  M_iso ≈ √(2π) (b R_H)^(3/2) Σ r^(1/2) / M_☉^(1/2)

  At 1 AU (inside snowline): M_iso ~ 0.05–0.1 M_Earth  ← terrestrial planet embryo
  At 5 AU (beyond snowline): M_iso ~ 5–15 M_Earth       ← giant planet core!

  Timeline:
  ┌────────────────────────────────────────────────────────────────────┐
  │ 1 AU:  embryos reach ~0.1 M_Earth in ~0.1–1 Myr                    │
  │ 5 AU:  cores reach ~10 M_Earth in ~1–5 Myr (pebble accretion)      │
  │ 30 AU: cores barely grow in disk lifetime (→ Uranus/Neptune late)  │
  └────────────────────────────────────────────────────────────────────┘
```

### 4.3 Pebble Accretion — The Speed Solution

Classic core accretion (Pollack 1996) was too slow at 5 AU. Pebble accretion (Lambrechts & Johansen 2012) is ~100× faster:

```
  PEBBLE ACCRETION:
  Drifting pebbles (St ~ 0.01–0.1, roughly cm-scale) are captured
  by a growing protoplanet in the planet's Hill sphere.
  Headwind-deflected pebbles on approach → enhanced capture cross section.

  Growth rate (2D settling regime, planet fills Hill sphere vertically):
  dM/dt ≈ 2 R_H² Ω Σ_pebble    where Ω = orbital frequency

  Much faster than planetesimal accretion (R_H >> R_planet)

  PEBBLE ISOLATION MASS:
  When planet mass exceeds:
  M_iso,pebble ~ h³ M_☉ ≈ 20 M_Earth at 5 AU   (h = H/r = disk aspect ratio)

  Planet opens partial gap in pebble disk → pebble flux stops → growth halts
  → Next step: trigger runaway gas accretion (for giants) or be stranded (super-Earths)

  KEY: Pebble accretion explains why Jupiter formed before Saturn (closer,
  faster pebble flux), why giant cores needed ~3–5 Myr not 8 Myr.
```

---

## 5. Giant Planet Formation

### 5.1 Core Accretion (Pollack et al. 1996)

```
  THREE-PHASE CORE ACCRETION:

  Phase 1: Solid core growth (pebble + planetesimal accretion)
           Core grows to ~10 M_Earth; thin gas envelope
           Timescale: ~1–5 Myr (pebble accretion)

  Phase 2: Slow envelope growth (quasi-hydrostatic)
           Solid accretion slows; envelope gradually grows
           Both solid and gas contribute roughly equally
           Timescale: ~1–3 Myr (disk-lifetime limited)

  Phase 3: RUNAWAY GAS ACCRETION (crossover point)
           When M_core ≈ M_envelope: ~10–20 M_Earth
           Envelope contracts faster than gas can be supplied
           → accretion rate of gas increases exponentially
           → Jovian mass reached in ~10⁴ yr (essentially instantaneous)

  ┌──────────────────────────────────────────────────────────────────────┐
  │  DISK LIFETIME CONSTRAINT:                                           │
  │  Disk gas dissipates in 1–10 Myr (median ~3 Myr)                     │
  │  Giant planet MUST reach runaway phase before disk clears            │
  │  → Jupiter and Saturn managed it; Uranus/Neptune did not fully       │
  │    → "failed cores" → ice giants (H/He envelope but not Jovian)      │
  └──────────────────────────────────────────────────────────────────────┘
```

### 5.2 Gravitational Instability (Boss 1997)

```
  TOOMRE Q PARAMETER:
  Q = c_s κ / (π G Σ)    κ = epicyclic frequency ≈ Ω for near-circular orbits

  Q < 1: disk gravitationally unstable → fragments into clumps

  ADDITIONAL COOLING CRITERION (Gammie 2001):
  t_cool < Ω^(−1) / β   where β ~ a few
  → Disk must cool faster than it orbits for fragments to survive
  → Slow cooling: clumps shear apart → spiral arms, disk heating
  → Fast cooling: clumps collapse → proto-giant planet

  WHEN GI WORKS:
  ● Massive disk (M_disk > 0.1 M_☉) at early times
  ● Large radii (> 40–100 AU): long t_orb → easier to cool fast enough
  ● First few × 10⁴ yr after disk forms (before disk stabilizes)

  EVIDENCE FOR GI:
  Directly imaged giant planets at large radii (> 50 AU) likely formed by GI:
    HR 8799 b,c,d,e (5–70 MJ at 15–70 AU)
    Beta Pictoris b (~9 MJ at ~8 AU)

  SOLAR SYSTEM GIANTS: core accretion almost certainly (right timescale,
  solar composition with enhanced rock/ice consistent with solid core)
```

---

## 6. Planetary Migration

### 6.1 Type I and Type II Migration

```
  TYPE I MIGRATION (M_planet < gap-opening mass):
  Planet excites density waves at Lindblad resonances in disk.
  Inner disk resonance: planet pushes inward → positive angular mom. → disk gains AM
  Outer disk resonance: planet pulls outward → outer disk loses AM
  NET: asymmetry → planet loses angular momentum → INWARD drift

  Rate: da/dt ≈ −C (M_planet/M_*) (Σ r² / M_*) (r/H)² Ω r   [C ~ few, sign conventions vary]
  Timescale: ~10⁵–10⁶ yr for Earth-mass at 1 AU in MMSN
  PROBLEM: Type I can destroy forming terrestrial planets → disk structure must help
  Outward migration possible near opacity transitions (heat source reversal)

  TYPE II MIGRATION (M_planet > gap-opening mass):
  Planet opens a gap when:  M > M_gap ~ (H/r)² h M_* / α   [α = disk viscosity]
  Planet locked in gap, moves with viscous disk evolution:
  t_mig ~ t_visc = r² / ν  ~ r² Ω / (α c_s²)  ≈ 10⁴–10⁶ yr

  ┌──────────────────────────────────────────────────────────────────────┐
  │  HOT JUPITERS: formed beyond snowline (~3–5 AU) → Type II migration  │
  │  → ended up at ~0.05 AU (orbital period < 5 days)                    │
  │  Stopped by: disk inner edge (magnetospheric cavity), tidal locking, │
  │  disk dispersal → halted migration                                   │
  └──────────────────────────────────────────────────────────────────────┘
```

---

## 7. The Grand Tack — Jupiter's Migration Explains the Inner Solar System

Walsh, Morbidelli, Raymond, O'Brien & Mandell (2011):

```
  THE PROBLEM IT SOLVES:
  ┌──────────────────────────────────────────────────────────────────────┐
  │  Mars is too small: models without migration predict ~1 M_Earth;     │
  │  actual Mars: 0.107 M_Earth                                          │
  │  Asteroid belt too empty: models predict ~1 M_Earth in belt;         │
  │  actual belt: ~5×10⁻⁴ M_Earth                                        │
  └──────────────────────────────────────────────────────────────────────┘

  THE GRAND TACK SEQUENCE:

  1. Jupiter forms at ~3–5 AU (core accretion + runaway gas)
     → begins Type II migration INWARD

  2. Saturn forms shortly after at ~5–8 AU
     → also migrates inward, faster (lower mass → smaller gap → faster)

  3. Saturn catches Jupiter at ~1.5 AU in the 2:3 mean-motion resonance

  4. Jupiter-Saturn 2:3 resonance REVERSES MIGRATION (outward)
     → The "tack" (sailing analogy: reversing direction)

  5. Jupiter ends at ~5.2 AU; Saturn ends at ~9.5 AU
     → roughly current architecture

  CONSEQUENCES:
  ┌────────────────────────────────────────────────────────────────────────┐
  │  Jupiter swept through 1.5–3 AU (inward pass):                         │
  │  → Scattered S-type (rocky) planetesimals inward AND outward           │
  │  → Depleted mass reservoir between 1–3 AU                              │
  │  → Mars's feeding zone mass-depleted → Mars stays small                │
  │                                                                        │
  │  On outward pass:                                                      │
  │  → Scattered C-type (volatile-rich) bodies from 5–8 AU inward          │
  │  → Some implanted into asteroid belt → explains C-type in outer belt   │
  │  → Some C-type impacted Earth → water delivery to early Earth          │
  │                                                                        │
  │  Asteroid belt composition:                                            │
  │  Before Grand Tack: S-type everywhere                                  │
  │  After: S-type inner, C-type outer → matches observed gradient         │
  └────────────────────────────────────────────────────────────────────────┘
```

---

## 8. The Giant Impact Phase — Terrestrial Planet Assembly

After disk dispersal (~5 Myr), ~10-20 planetary embryos remain in the inner solar system:

```
  GIANT IMPACT PHASE (~5–100 Myr):

  Embryos are on crossing orbits → gravitational interactions
  → close encounters → mergers (giant impacts)
  → chaotic, stochastic — specific outcomes not reproducible in simulation

  N-BODY STATISTICAL RESULT:
  ● Typically 2–4 terrestrial planets produced
  ● Final architecture sensitive to giant planet positions (Jupiter/Saturn)
  ● High-e Jupiter → excited embryos → faster accretion but fewer planets
  ● Current JS architecture: moderate eccentricities → roughly correct

  THE MOON-FORMING IMPACT:
  ┌──────────────────────────────────────────────────────────────────────┐
  │  Theia: ~0.1 M_Earth (Mars-sized), on Venus-crossing orbit           │
  │  Collision: oblique, ~45°, v_impact ~ 10 km/s                        │
  │  Result: proto-Earth (now ~Earth mass) + debris disk → Moon          │
  │                                                                      │
  │  EVIDENCE FOR THIS MODEL:                                            │
  │  ● Lunar oxygen isotopes match Earth's mantle exactly                │
  │    (Earth + Theia must have been isotopically similar — same region) │
  │  ● Moon is iron-depleted: high-T impact vaporized + ejected Fe       │
  │  ● Moon has no volatiles: impact desiccated the debris               │
  │  ● Earth's obliquity (23.5°): impact tilt                            │
  │                                                                      │
  │  TIMING (Hf-W chronometer):                                          │
  │  ¹⁸²Hf → ¹⁸²W (t₁/₂=8.9 Myr): W to core, Hf stays in mantle          │
  │  Compare W isotope ratio in lunar mantle vs Earth mantle             │
  │  → Moon-forming impact: 50–150 Myr after CAI formation               │
  └──────────────────────────────────────────────────────────────────────┘
```

---

## 9. The Nice Model — Late Dynamical Instability

Gomes, Morbidelli, Tsiganis & Levison (2005) — "Nice model" (from Nice, France):

```
  INITIAL STATE (after disk dispersal, ~5 Myr):
  4 giant planets in compact, nearly circular orbits inside ~15 AU:
  Jupiter (~5.5 AU), Saturn (~8 AU), "Uranus" (~11 AU), "Neptune" (~14 AU)
  Massive disk of planetesimals (Pluto-sized) from ~15–30 AU

  SLOW DIVERGENCE (~600 Myr):
  Giant planets slowly migrate: Jupiter in slightly, others out slightly
  → due to planetesimal scattering (planets exchange energy with disk)
  → Uranus and Neptune slowly migrate outward through planetesimal disk

  THE TRIGGER — JUPITER/SATURN 2:1 MMR CROSSING:
  ~600–800 Myr after formation (i.e., ~3.9 Gyr ago):
  Jupiter and Saturn diverge through the 2:1 mean motion resonance
  → Resonance crossing excites eccentricities of ALL giant planets

  INSTABILITY:
  → Uranus and Neptune scattered outward into planetesimal disk
  → Disk disrupted → thousands of Pluto-sized bodies scattered inward
  → LHB: intense cratering on inner solar system bodies

  LATE HEAVY BOMBARDMENT (LHB):
  ┌──────────────────────────────────────────────────────────────────────┐
  │  Evidence: Apollo samples show lunar craters cluster at ~3.9 Gyr     │
  │  Many large impact basins formed in ~50–200 Myr window               │
  │  Also seen in asteroid belt: isotopic reset ages cluster at 3.9 Gyr  │
  │  Mars also shows intensive bombardment in this era                   │
  └──────────────────────────────────────────────────────────────────────┘

  POST-INSTABILITY OUTCOMES:
  ● Jupiter Trojans: captured from scattered disk bodies during instability
  ● Kuiper Belt: Neptune migrated outward, swept up Plutinos into 3:2 MMR
  ● Scattered disk: bodies ejected by Neptune → current scattered disk population
  ● One extra giant planet? Some models need a 5th giant (later ejected)

  REVISION (Nice 2.0, instability timing):
  More recent models: instability may have occurred EARLIER (~5-50 Myr)
  → "Cataclysm" vs "sustained bombardment" debate ongoing
  → JWST + Rubin Observatory may constrain via small body populations
```

---

## 10. Meteorite Chronology — Reading Solar System History in Rock

### 10.1 CAIs and Chondrules

```
  CAIs (Calcium-Aluminum-rich Inclusions):
  ────────────────────────────────────────────────────────────────────────
  Age:          4.5672 ± 0.0006 Gyr (Pb-Pb)  ← t = 0 for solar system
  Found in:     Carbonaceous chondrites (CI, CM, CV, CO types)
  Mineralogy:   Corundum (Al₂O₃), hibonite, spinel, melilite, pyroxene
  Formation T:  >1400 K (highest-T condensates)
  Formed near:  Proto-Sun, then scattered outward to planetesimal zone
  Significance: First solids to condense from solar nebula; record nebula T

  CHONDRULES:
  ────────────────────────────────────────────────────────────────────────
  What:         Silicate spherules (0.1–3 mm), rapidly melted + cooled
  Age:          2–4 Myr after CAIs (²⁶Al-²⁶Mg chronometer)
  Cooling rate: ~100–1000 K/hr (preserve glass, not equilibrium crystals)
  Origin:       Shock waves in protoplanetary disk? X-wind? Still debated.
  Abundance:    60-80% of ordinary chondrites by volume
  Significance: Dominant component of primitive meteorites; disk process recorder
```

### 10.2 Short-Lived Radionuclides — The Solar System Clock

```
  RADIONUCLIDE     t₁/₂        USE
  ──────────────────────────────────────────────────────────────────────────
  ²⁶Al → ²⁶Mg     0.72 Myr    Heat source for early differentiation;
                               relative ages of meteorites to 0.1 Myr precision
  ⁶⁰Fe → ⁶⁰Ni     2.6 Myr    Supernova injection marker; inner solar system
                               heterogeneity evidence
  ¹⁸²Hf → ¹⁸²W    8.9 Myr    Core formation timing (W siderophile → core;
                               Hf lithophile → mantle)
  ¹⁰⁷Pd → ¹⁰⁷Ag   6.5 Myr    Planetesimal differentiation timing
  ¹²⁹I → ¹²⁹Xe    15.7 Myr   Atmospheric volatile evolution

  KEY RESULTS:
  ┌──────────────────────────────────────────────────────────────────────┐
  │  ²⁶Al/²⁷Al = 5×10⁻⁵ at t=0 (from CAIs)                               │
  │  → ²⁶Al decay heated planetesimals that formed in first ~2 Myr       │
  │  → Bodies formed EARLY: melted + differentiated (iron meteorite      │
  │    parents, achondrite parents)                                      │
  │  → Bodies formed LATE: didn't melt (chondrites — undifferentiated)   │
  │                                                                      │
  │  ¹⁸²Hf-¹⁸²W:                                                         │
  │  Earth's core formed within ~30–40 Myr of CAIs                       │
  │  Moon-forming impact: ~50–150 Myr after CAIs                         │
  └──────────────────────────────────────────────────────────────────────┘

  SUPERNOVA INJECTION:
  ²⁶Al, ⁶⁰Fe abundances suggest a nearby supernova injected freshly-
  synthesized radionuclides just before solar system formation (<1 Myr before)
  → Possible trigger for molecular cloud collapse
  → Explains why ²⁶Al was so abundant (too much for galactic background alone)
```

---

## 11. Comparison — Other Planetary Systems

```
  TRAPPIST-1 (7 Earth-sized planets, all within 0.06 AU):
  ─────────────────────────────────────────────────────────────────────────
  In-situ formation impossible: disk mass at < 0.1 AU insufficient
  Likely: formed at several AU → migrated inward via Type I, trapped in
  resonance chain (8:5:3:2 etc.) as inner edge stopped migration
  → Consistent with relatively water-rich composition (formed near snowline)

  HOT JUPITERS (~1% of stars have them):
  Formed at 3–10 AU → Type II migration inward → halted at disk edge
  (Magnetospheric cavity at ~0.05 AU; orbital periods < 5 days)
  Hot Jupiter formation depletes outer disk → often no other planets

  SYSTEMS WITH NO JUPITER ANALOG:
  More frequent rocky planets at large radii?
  Or, disk not massive enough to form gas giant → "super-Earth" systems
  TRAPPIST-1 star is M-dwarf: disk 10-100× lower mass → no Jovian possible

  THE SOLAR SYSTEM IS ODD:
  ● Jupiter at 5.2 AU (most Jupiter-analogues are closer)
  ● No super-Earth inside Mercury's orbit (very common elsewhere)
  ● Grand Tack may explain why: Jupiter swept the inner disk clean
  ● Earth-like planet around Sun-like star in "warm zone": uncommon
    (Kepler statistics: ~10-20% of G dwarfs have Earth-size planets in HZ)
```

---

## Decision Cheat Sheet

```
  ┌────────────────────────────────────────────────────────────────────────────┐
  │ Question                               │ Answer                            │
  ├────────────────────────────────────────┼───────────────────────────────────┤
  │ What sets t=0 in solar system history? │ CAI formation: 4.5672 Gyr ago     │
  ├────────────────────────────────────────┼───────────────────────────────────┤
  │ Why are giant planets beyond ~3 AU?    │ Snowline at ~2.7 AU: solids 4×    │
  │                                        │ more abundant → isolation mass    │
  │                                        │ crosses ~10 M_Earth threshold     │
  ├────────────────────────────────────────┼───────────────────────────────────┤
  │ Why is Mars so small?                  │ Grand Tack: Jupiter swept the      │
  │                                        │ 1-3 AU region, depleting mass      │
  ├────────────────────────────────────────┼───────────────────────────────────┤
  │ Why are there no planets in the belt?  │ Grand Tack depletion + Jupiter    │
  │                                        │ MMRs dynamically excited remaining│
  ├────────────────────────────────────────┼───────────────────────────────────┤
  │ What caused the Late Heavy Bombardment?│ Nice model 2:1 JS resonance        │
  │                                        │ crossing → giant planet instability│
  ├────────────────────────────────────────┼───────────────────────────────────┤
  │ Why are Uranus/Neptune "ice giants"    │ Failed cores: disk dispersed      │
  │ not gas giants?                        │ before reaching runaway gas       │
  │                                        │ accretion threshold               │
  ├────────────────────────────────────────┼───────────────────────────────────┤
  │ When did Earth's core form?            │ Within ~30-40 Myr of CAIs         │
  │ When did the Moon form?                │ ~50–150 Myr after CAIs            │
  ├────────────────────────────────────────┼───────────────────────────────────┤
  │ Why did early planetesimals melt?      │ ²⁶Al (t₁/₂=0.72 Myr) decay heat;  │
  │                                        │ only if formed in first ~2 Myr    │
  ├────────────────────────────────────────┼───────────────────────────────────┤
  │ How did water get to Earth?            │ C-type asteroids implanted by      │
  │                                        │ Grand Tack outward phase; δD/H    │
  │                                        │ of Earth oceans matches C-types   │
  └────────────────────────────────────────┴───────────────────────────────────┘
```

---

## Common Confusion Points

**"The solar system formed from the Big Bang"**
No. The solar system formed ~9 Gyr after the Big Bang, from a molecular cloud that was itself enriched by previous generations of stars. The H and He came from Big Bang nucleosynthesis; the heavier elements (C, O, Si, Fe, etc.) came from stellar nucleosynthesis and supernovae over the intervening 9 Gyr.

**"The meter barrier means planets can't form"**
It means planetesimals can't form by slow pairwise growth. Streaming instability bypasses the barrier: pebbles concentrate and gravitationally collapse directly to ~100 km planetesimals, skipping the ~1 m regime entirely. The barrier is a problem for one formation pathway, not for planet formation in general.

**"Jupiter is responsible for protecting Earth (the Jupiter Shield)"**
Oversimplified and partly wrong. Jupiter does deflect some long-period comets — but it also sends some comets INTO the inner solar system. Simulations suggest Jupiter is roughly neutral or slightly harmful for Earth impact rates on long timescales. The "Jupiter as shield" idea was popular in the 1990s but is not the current consensus.

**"The Nice model explains why the LHB happened at exactly 3.9 Gyr"**
The Nice model explains a *dynamical instability* that could cause an LHB-like event. Whether the LHB is a narrow "cataclysm" at 3.9 Gyr or a declining bombardment is debated — Apollo samples are biased toward the large basin-forming events (which cluster at 3.9 Gyr), potentially creating an artifact. Recent crater-counting on the Moon (GRAIL data) and meteorite ages don't fully resolve this.

**"Grand Tack and Nice model are the same thing"**
Different events at different times. Grand Tack: ~3-5 Myr, while disk gas still exists, Jupiter migrates inward and back. Nice model: ~600-800 Myr, long after disk dispersal, Jupiter/Saturn cross the 2:1 resonance during slow planetesimal-driven migration. Grand Tack sculpts the inner solar system; Nice model sculpts the outer solar system and causes the LHB.

**"Chondrites are the oldest meteorites"**
Chondrites are *undifferentiated* (never melted) but not the oldest material in them. CAIs within chondrites are the oldest dated solar system objects. Chondrules formed 2-4 Myr after CAIs. The *parent bodies* of achondrites (differentiated) and iron meteorites formed very early (within ~1-2 Myr of CAIs) and melted from ²⁶Al heat — they're actually *younger in age but from earlier-formed parent bodies*.
