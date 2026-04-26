# Milankovitch Cycles
## Orbital Mechanics, Insolation Forcing, and the Pacemaker of Ice Ages

---

## 1. The Full Picture — Three Parameters, Three Timescales

```
  THE THREE ORBITAL PARAMETERS THAT DRIVE CLIMATE

  ┌─────────────────────────────────────────────────────────────────────────────┐
  │  PARAMETER        PERIOD(S)        RANGE          CLIMATE EFFECT            │
  ├─────────────────────────────────────────────────────────────────────────────┤
  │  Eccentricity e   ~100 kyr         0.000–0.060    Seasonal contrast,        │
  │                   ~413 kyr         (now: 0.0167)  modulates precession amp. │
  ├─────────────────────────────────────────────────────────────────────────────┤
  │  Obliquity ε      ~41 kyr          22.1°–24.5°    High-latitude summer      │
  │                                    (now: 23.44°)  insolation; controls      │
  │                                                   polar ice buildup         │
  ├─────────────────────────────────────────────────────────────────────────────┤
  │  Climate prec.    ~23 kyr          e·sin(λ̃)      NH summer at perihelion   │
  │  (axial+apsidal)  ~19 kyr          amplitude      vs aphelion; tropical     │
  │                                    ∝ e (→0 at    monsoon timing             │
  │                                    e=0)                                     │
  └─────────────────────────────────────────────────────────────────────────────┘

  ICE VOLUME RECORD (schematic, last 800 kyr)

  Cold ┤                ██  ██            ██  ██     ██        ██ ███
  (ice)│              ██████████       ███████████████        ████████
       │            ████████████     █████████████████     ████████████
  Warm ┤────────────────────────────────────────────────────────────────→ time
       800 kyr ago  700   600   500   400   300   200   100   now

  Dominant period in last 800 kyr:  ~100 kyr  (eccentricity)
  Dominant period 1–3 Myr ago:      ~41 kyr   (obliquity)
  Precession (~23 kyr):             always present, modulated by eccentricity

  The shift ~900 kyr ago (Mid-Pleistocene Transition, MPT) from 41-kyr to
  100-kyr glacial cycles is one of the major open problems in paleoclimatology.
```

---

## 2. Eccentricity — Shape of the Orbit

### 2.1 Orbital Mechanics Basis

Earth's orbit is a Keplerian ellipse perturbed by the other planets — primarily Jupiter and Saturn.

```
                                     ●  aphelion (July ~4)
                                    /
              ─────────────────────/────────────────────────
             /           ←   a   →/←  ae  →                 \
            │                     ●──────────────────────────●
            │                     F₁ (Sun)    F₂ (empty)     │
             \                                               /
              ─────────────────────────────────────────────
                                    \
                                     ●  perihelion (Jan ~3)

  a  = semi-major axis = 1.000 AU (conserved to first order — energy conserved)
  b  = semi-minor axis = a√(1−e²)
  e  = eccentricity = c/a where c = F₁F₂ distance

  Current: e = 0.0167  →  aphelion/perihelion distance ratio = (1+e)/(1-e) = 1.034
           Earth is 3.4% farther from Sun in July than January

  At e = 0.06 (near maximum): ratio = 1.128  →  12.8% farther at aphelion
  At e ≈ 0 (near minimum):   nearly circular orbit, no preferred perihelion season
```

**Why a is conserved but e is not:**
Orbital energy E = −GM_☉/(2a) depends only on a. Slow planetary perturbations conserve energy on orbit-average → a secular. But angular momentum L = √(GM_☉ a(1−e²)) can change as Jupiter deflects Earth slightly → e oscillates while a stays fixed.

### 2.2 Forcing Frequencies

Eccentricity is driven by resonances between the orbital periods of Earth, Jupiter, and Saturn:

```
  ECCENTRICITY SPECTRAL PEAKS (Berger & Loutre parameterization)

  Period (kyr)    Amplitude    Cause
  ─────────────────────────────────────────────────────────────────────
  413             0.012        g₂ − g₅  (Earth−Jupiter perihelion beat)  ← most stable
  ~125            0.010        g₄ − g₅  (Jupiter−Mars resonance terms)
  ~95             0.020        g₁ − g₅
  ~123            0.011        g₃ − g₅
  ─────────────────────────────────────────────────────────────────────
  ~100 kyr "period": beat envelope of ~95 + ~125 kyr terms — not a single frequency

  gᵢ = secular frequency of ith planet's perihelion precession
  g₅ = Jupiter's secular frequency (~4.25"/yr)

  413-kyr cycle: most stable, serves as orbital metronome in long chronologies
  100-kyr cycle: actually a spectral cluster, not a pure line
```

### 2.3 Effect on Insolation

Eccentricity does **not** change total annual insolation significantly:

```
  Annual mean insolation ∝ 1/√(1−e²) ≈ 1 + e²/2

  At e = 0.06:  change ≈ 0.18%  →  ~0.6 W/m² at solar constant 1361 W/m²
  At e = 0.017: change ≈ 0.01%  →  tiny

  What eccentricity DOES affect:
  ┌────────────────────────────────────────────────────────────────────────┐
  │ 1. Seasonal contrast                                                   │
  │    Earth at perihelion receives (1+e)²/(1−e)² more flux than aphelion │
  │    At e=0.06: 27% more flux at perihelion than aphelion               │
  │    At e=0.017: 6.9% more flux at perihelion than aphelion             │
  │                                                                        │
  │ 2. Duration asymmetry (Kepler's 2nd law)                              │
  │    Equal areas in equal times → Earth moves faster at perihelion       │
  │    Northern summer (aphelion currently): ~186 days                     │
  │    Northern winter (perihelion currently): ~179 days                   │
  │    At e=0.06: asymmetry would be ~2× larger                           │
  │                                                                        │
  │ 3. Precession amplitude modulation                                     │
  │    Climate precession index = e·sin(λ̃)                               │
  │    When e→0: precession has no climate effect (no "preferred" season   │
  │    for perihelion)                                                      │
  └────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Precession of Perihelion — The Apsidal Cycle

Axial precession (covered in 01-EARTH-MOTIONS.md) is not the whole story for climate. The perihelion itself also precesses — in the *prograde* direction — due to planetary perturbations.

```
  TWO PRECESSIONS IN OPPOSITE DIRECTIONS

  ┌──────────────────────────────────────────────────────────────────────┐
  │  Axial precession:      ~50.3 "/yr  RETROGRADE (westward)           │
  │  Apsidal precession:    ~11.45"/yr  PROGRADE (eastward)             │
  │  Combined rate:         ~61.75"/yr                                  │
  │  Climate precession period: 360° × 3600" / 61.75"/yr ≈ 21,000 yr   │
  └──────────────────────────────────────────────────────────────────────┘

  WHAT MATTERS FOR CLIMATE: the longitude of perihelion relative to the equinoxes

        λ̃ = longitude of perihelion measured from vernal equinox
        rate of change: dλ̃/dt = axial precession (retro) + apsidal (pro)

  When λ̃ = 90°:  Northern Hemisphere summer at perihelion → HOT NH summers
  When λ̃ = 270°: NH summer at aphelion → COOL NH summers → ice accumulation
  Currently:      λ̃ ≈ 283° → NH summer near aphelion (slight cooling bias)

  CYCLE THROUGH THE SEASONS (schematic, ~21 kyr period)

  ┌────────────────────────────────────────────────────────────────────┐
  │  Now (~2000 CE):  perihelion in January  (NH winter)               │
  │  +5,500 yr:       perihelion in April    (NH spring)               │
  │  +10,500 yr:      perihelion in July     (NH summer) ← hot NH      │
  │  +15,500 yr:      perihelion in October  (NH autumn)               │
  │  +21,000 yr:      perihelion in January again                      │
  └────────────────────────────────────────────────────────────────────┘
```

### 3.1 The Two Climate Precession Periods

The ~21 kyr average splits into two peaks in the spectrum:

```
  SPECTRAL PEAKS OF e·sin(λ̃) (Berger's parameterization):

  Period (kyr)    Source
  ─────────────────────────────────────────────────────────────────────
  23.716          dominant axial precession + g₂ term (Jupiter)
  22.428          second luni-solar precession term
  18.976          g₃ term (Venus + Earth resonance)
  19.155          another eccentricity term
  ─────────────────────────────────────────────────────────────────────
  Commonly simplified to: ~23 kyr + ~19 kyr peaks
```

---

## 4. The Insolation Formula

The three orbital parameters combine to determine the solar flux at any latitude and time of year.

### 4.1 Top-of-Atmosphere Daily-Mean Insolation

```
  W(φ, t) = (S₀/π) · (ā/r)² · [h₀ sin φ sin δ + cos φ cos δ sin h₀]

  where:
    S₀  = solar constant = 1361 W/m²
    φ   = latitude
    δ   = solar declination (function of obliquity ε and orbital position)
    r   = Earth–Sun distance at time t = a(1−e²)/(1 + e cos ν)
    ā   = mean Earth–Sun distance (1 AU)
    h₀  = half-day angle = arccos(−tan φ · tan δ)   [h₀ = 0 at polar night, π at midnight sun]
    ν   = true anomaly (angle from perihelion)

  THE (ā/r)² TERM:
  This is the "insolation boost" factor. When r < ā (near perihelion):
    (ā/r)² > 1 → more flux
  When r > ā (near aphelion):
    (ā/r)² < 1 → less flux
  The boost is proportional to e and the perihelion–season timing.
```

### 4.2 The Milankovitch Target: 65°N Caloric Summer

Milankovitch argued that **Northern Hemisphere summer insolation at 65°N** is the key climate driver. The Northern Hemisphere has more land area at high latitudes than the Southern Hemisphere — so if NH high-latitude summers are cold, snow persists year-round → ice sheets grow.

```
  WHY 65°N?
  ─────────────────────────────────────────────────────────────────────────
  Too far south (e.g., 45°N): winter/summer contrast dominated by tilt,
                               not sensitive enough to orbital parameters
  Too far north (e.g., 85°N): polar night / midnight sun extremes dominate,
                               less sensitive to perihelion timing
  65°N: sweet spot — receives significant summer insolation, ice-free in
        interglacials, near ice sheet margins during glacials

  MILANKOVITCH'S ORIGINAL CALCULATION (1941):
  Caloric summer half-year insolation at 65°N, plotted vs time
  → matched known European glacial chronology qualitatively
  → validation had to wait for deep-sea sediment cores (1970s)
```

### 4.3 Orbital Parameters → Insolation Change (sensitivity table)

```
  EFFECT ON SUMMER (JJA) INSOLATION AT 65°N

  Parameter      Change                  ΔW at 65°N (approx)
  ───────────────────────────────────────────────────────────────────────
  Obliquity      +1°                     +0.5 W/m² (summer), larger at pole
                 22.1° → 24.5°           +12 W/m² peak-to-peak
  Eccentricity   0 → 0.06               +25 W/m² (if perihelion in summer)
  Precession     NH summer at peri.      +40–50 W/m² vs. aphelion case
                 vs. aphelion            (largest seasonal signal)
  ───────────────────────────────────────────────────────────────────────
  Total plausible range:  ±60–80 W/m² at 65°N summer
  (Global annual mean changes are far smaller — precession nearly cancels
   between hemispheres on annual basis)
```

---

## 5. Astronomical Solutions — Laskar et al.

The orbital parameters cannot be integrated analytically over geological time — the solar system is **chaotic**. Numerical integration is the only tool.

```
  MAJOR SOLUTIONS

  ┌──────────────────┬───────────────────┬──────────────────────────────────────┐
  │ Solution         │ Year              │ Validity / Notes                     │
  ├──────────────────┼───────────────────┼──────────────────────────────────────┤
  │ Berger 1978      │ 1978 (analytic)   │ ±5 Myr; series expansion, fast       │
  │ Berger & Loutre  │ 1991              │ ±2 Myr; improved series              │
  │ BER90            │ 1990              │ Standard for SPECMAP era             │
  │ La2004           │ Laskar et al.2004 │ ±50 Myr eccentricity, ±20 Myr ε/ψ  │
  │ La2010a,b        │ Laskar et al.2010 │ ±50 Myr; two solutions (uncertainty) │
  └──────────────────┴───────────────────┴──────────────────────────────────────┘

  CHAOS LIMITS:

  Lyapunov time of solar system:    ~5 Myr
  Eccentricity reliable to:         ±50 Myr   (weakly chaotic — large-scale structure)
  Obliquity reliable to:            ±20–40 Myr (coupled to precession, more sensitive)
  Beyond ~50 Myr:                   only statistical → "chaotic zone" occupancy fractions

  ┌─────────────────────────────────────────────────────────────────────────────┐
  │  ROLE OF THE MOON IN STABILIZING OBLIQUITY                                 │
  │                                                                             │
  │  The same lunisolar torque that drives precession also provides a           │
  │  gyroscopic stabilization of the obliquity.                                 │
  │                                                                             │
  │  Without the Moon:                                                          │
  │    Precession rate → 0 (no lunar torque) → resonance with planetary        │
  │    forcing frequencies → obliquity could wander 0°–85° chaotically         │
  │    on timescales of ~10–100 Myr (Laskar & Robutel 1993)                    │
  │                                                                             │
  │  Mars (no large moon): obliquity chaotic between ~10°–60° on ~5 Myr scale  │
  │  Earth (with Moon): obliquity confined to 22.1°–24.5° range (±1.2°)       │
  │                                                                             │
  │  The Moon is a long-term climate stabilizer.                                │
  └─────────────────────────────────────────────────────────────────────────────┘
```

---

## 6. The Proxy Record — Reading the Ice Age Signal

### 6.1 The δ¹⁸O Proxy

Orbital theory predicts insolation. To test it, you need a paleoclimate record with age control independent of orbital assumptions.

```
  δ¹⁸O IN FORAMINIFERA (marine sediment cores)

  Ocean isotope physics:
  ─────────────────────
  H₂¹⁶O evaporates preferentially over H₂¹⁸O (lighter → higher vapor pressure)
  → atmospheric water vapor is ¹⁶O-enriched
  → precipitation/snow is ¹⁶O-enriched
  → glacial ice is ¹⁶O-enriched (sequesters ¹⁶O)
  → ocean becomes ¹⁸O-enriched during glacials

  Foram shells record ocean δ¹⁸O at time of formation:

  δ¹⁸O = [(¹⁸O/¹⁶O)_sample / (¹⁸O/¹⁶O)_standard − 1] × 1000  (‰, per mil)

  Glacial:      high δ¹⁸O  (ocean heavy, much ice on land)
  Interglacial: low δ¹⁸O   (ocean lighter, ice melted)

  TWO SIGNALS MIXED IN δ¹⁸O:
  1. Ice volume (dominant, ~70%) — global signal
  2. Bottom water temperature (~30%) — local signal (heavier ¹⁸O at lower T)
  Both go in same direction: glacial → high δ¹⁸O
```

### 6.2 SPECMAP and the Pacemaker Paper

The critical test of Milankovitch theory:

```
  HAYS, IMBRIE & SHACKLETON (1976) — "Pacemaker of the Ice Ages"
  Science, 194, 1121–1132

  Used:   Two Indian Ocean cores with high sedimentation rates (good time resolution)
          Radio-tuned to geomagnetic reversals for independent chronology
  Method: Spectral analysis of δ¹⁸O and SST records

  RESULT — Three dominant periods found in data:
  ┌────────────────────────────────────────────────────────────────┐
  │  Observed in δ¹⁸O   Predicted by orbital theory  Parameter   │
  │  ~100 kyr           ~95–125 kyr eccentricity beat eccentricity│
  │  ~41 kyr            ~41 kyr                       obliquity   │
  │  ~23 kyr            ~23 + ~19 kyr                 precession  │
  └────────────────────────────────────────────────────────────────┘

  Phases matched predictions → orbital forcing is the *pacemaker*.
  Most important result in 20th-century paleoclimatology.

  SPECMAP (1984, Imbrie et al.):
  5-core stacked δ¹⁸O, tuned to orbital solution → global reference chronology
  Extended to 800 kyr → confirmed all three frequencies at higher resolution

  LR04 (Lisiecki & Raymo 2005):
  57-core stack, 5.3 Myr record → standard modern reference
```

### 6.3 Marine Isotope Stages (MIS)

```
  MIS NUMBERING:  odd = warm (interglacial);  even = cold (glacial)

  MIS 1       Holocene — now through ~11.7 kyr (current interglacial)
  MIS 2       Last Glacial Maximum ~26–19 kyr ago (sea level ~120 m lower)
  MIS 5e      Last interglacial ~130–115 kyr; warmer than today, sea level +6–9 m
  MIS 7       Penultimate interglacial ~240–210 kyr
  MIS 11      "Super-interglacial" ~424–374 kyr; closest orbital analog to MIS 1
  MIS 19      ~790 kyr; oldest clear 100-kyr cycle
  ─────────────────────────────────────────────────────────────────────────
  Before MIS 22 (~900 kyr): 41-kyr world
  After MIS 22:              100-kyr world (the "Late Pleistocene glaciations")
```

---

## 7. Open Problems

### 7.1 The 100-kyr Problem

The most vexing issue in Milankovitch theory:

```
  THE PARADOX:

  Eccentricity forcing strength:   weakest of the three (changes annual mean
                                   insolation by only ~0.1%)
  Eccentricity period dominance:   strongest in the last 800 kyr ice record

  PROPOSED RESOLUTIONS:

  ┌─────────────────────────────────────────────────────────────────────────┐
  │ 1. Nonlinear ice sheet response                                         │
  │    Ice sheets have their own ~100-kyr free oscillation timescale        │
  │    (build slowly under gravity + temperature balance, collapse fast)    │
  │    Eccentricity provides weak pacing to synchronize internal oscillation│
  │                                                                         │
  │ 2. Precession modulation                                                │
  │    Precession signal amplitude ∝ e; at e~0 → no precession forcing      │
  │    → 100-kyr gaps in precession allow ice buildup                       │
  │    → envelope of precession amplitude has ~100-kyr periodicity          │
  │                                                                         │
  │ 3. CO₂ feedback                                                         │
  │    Ice cores show CO₂ correlates with temperature at ~100 kyr           │
  │    CO₂ may amplify weak orbital signal (but CO₂ lags T by ~800 yr       │
  │    — it's a feedback, not forcing)                                      │
  │                                                                         │
  │ 4. Resonance / stochastic resonance                                     │
  │    Noise + weak periodic forcing → large-amplitude response at          │
  │    forcing period                                                       │
  │                                                                         │
  │ Current consensus: likely combination of 1+2+3; no definitive answer    │
  └─────────────────────────────────────────────────────────────────────────┘
```

### 7.2 The Mid-Pleistocene Transition (MPT)

```
  ~1.2 Myr ago → ~0.7 Myr ago:  transition from 41-kyr to 100-kyr world

  ─────────────────────────────────────────────────────────────────────────
  Before MPT (>1.2 Myr):   ice ages every ~41 kyr, smaller amplitude
  After MPT (<0.7 Myr):    ice ages every ~100 kyr, much larger amplitude
  ─────────────────────────────────────────────────────────────────────────

  KEY FACT: orbital parameters did NOT change at the MPT
            → the shift is internal to the climate system

  Hypotheses:
  • Gradual regolith erosion under ice sheets (Raymo 1997)
    Thick sediment → slippery base → small ice; erode sediment → bedrock
    → larger, more stable ice sheets → 100-kyr mode
  • Long-term CO₂ drawdown (weathering, carbonate compensation)
  • Threshold crossing in deep-water circulation
  • None fully confirmed — active research area
```

### 7.3 The Half-Precession Problem

Deep tropics show ~11 kyr (half-precession) signal in speleothem records. The explanation involves the **intertropical convergence zone** (ITCZ) shifting twice per precession cycle — once when NH is at perihelion, once when SH is. Monsoon records (Dongge Cave, China; Hulu Cave, China) show clean precession and half-precession signals driven by Asian Summer Monsoon intensity.

---

## 8. Putting It Together — The Insolation Forcing Stack

```
  HOW THE THREE PARAMETERS COMBINE

  65°N June insolation = f(ε, e, λ̃)

  Dominant contributions (relative amplitude at 65°N June):

  ┌──────────────────────────────────────────────────────────────────────┐
  │  Term                        Period      Rel. amplitude              │
  ├──────────────────────────────────────────────────────────────────────┤
  │  e · cos(λ̃) component        ~23 kyr     large (precession×ecc)    │
  │  obliquity ε                  ~41 kyr     significant               │
  │  eccentricity e (direct)      ~100 kyr    small                     │
  │  e · cos(λ̃) second term      ~19 kyr     medium                    │
  │  413-kyr eccentricity         413 kyr     small but very stable     │
  └──────────────────────────────────────────────────────────────────────┘

  BERGER'S ANALYTICAL APPROXIMATION (to ~1 W/m² at 65°N):

  W(65°N, summer) ≈ W₀
    + Σᵢ Aᵢ · cos(fᵢ · t + φᵢ)          [obliquity terms, period ~41 kyr]
    + Σⱼ Bⱼ · e · sin(λ̃ + ψⱼ)           [precession terms, period ~23/19 kyr]
    + small eccentricity direct terms

  The eccentricity e appears as a *modulator* of precession amplitude.
  This is why e=0 epochs are climate "quiet periods" — precession goes silent.

  LAST 150 KYR INSOLATION AT 65°N JUNE (schematic):

  W/m²  ← high                                                   now
  540 ─┤              ██                                          │
  520 ─┤           █████████                   ████              │
  500 ─┤          ██████████               ███████████           ██
  480 ─┤       █████████████            ██████████████         ████
  460 ─┤     ███████████████          ███████████████        ██████
  440 ─┤────────────────────────────────────────────────────────────→
       150 kyr ago   120    90      60      30          0
                ↑                              ↑
           MIS 5e                        LGM ~21 kyr
        (last interglacial)
```

---

## 9. Chronological Tools

```
  AGE CONTROL FOR ORBITAL CHRONOLOGY

  ┌──────────────────────────────────────────────────────────────────────────┐
  │ Method                   Range          Precision     Notes              │
  ├──────────────────────────────────────────────────────────────────────────┤
  │ ²³⁰Th/²³⁴U (U-Th)       0–600 kyr      ±1–2 kyr      Corals, speleothems│
  │ ¹⁴C (radiocarbon)        0–50 kyr       ±200–1000 yr  Organic matter     │
  │ ⁴⁰Ar/³⁹Ar               >50 kyr        ±1–5 kyr      Volcanic ash       │
  │ Geomagnetic reversals    any            known age      Brunhes/Matuyama  │
  │                                          (±5 kyr)      at 780 kyr        │
  │ Orbital tuning           any            ±2–5 kyr      Circular — assumes │
  │                                                        Milankovitch valid │
  ├──────────────────────────────────────────────────────────────────────────┤
  │ Key anchor: Brunhes–Matuyama reversal at 780 kyr BP (Ar/Ar dated)        │
  │ Allows orbital tuning to extend confidently past ¹⁴C range               │
  └──────────────────────────────────────────────────────────────────────────┘

  SAROS CYCLE (eclipse chronology — separate application of orbital periods):
  223 synodic months = 242 draconic months = 239 anomalistic months = 18.03 yr
  → eclipses repeat (shifted 8 hr in longitude) every 18 yr 11 days
  Uses all three Moon orbital periods simultaneously — beautiful resonance
```

---

## Decision Cheat Sheet

```
  WHICH MILANKOVITCH FACTOR MATTERS WHEN?

  ┌────────────────────────────────────────────────────────────────────────────┐
  │ Question                              │ Parameter                          │
  ├────────────────────────────────────────┼────────────────────────────────────┤
  │ Why did ice ages occur every 41 kyr   │ Obliquity — high latitude summer   │
  │ in early Pleistocene?                  │ insolation pacing                  │
  ├────────────────────────────────────────┼────────────────────────────────────┤
  │ Why are recent ice ages ~100 kyr?      │ Eccentricity (pacing) + ice sheet  │
  │                                        │ internal dynamics (100-kyr problem)│
  ├────────────────────────────────────────┼────────────────────────────────────┤
  │ Why do African monsoons pulse at       │ Precession (~23 kyr) — controls    │
  │ ~21 kyr? (Green Sahara periods)        │ NH summer insolation and ITCZ      │
  ├────────────────────────────────────────┼────────────────────────────────────┤
  │ Which parameter is most stable over    │ 413-kyr eccentricity cycle —        │
  │ tens of millions of years?             │ Laskar: reliable to ±50 Myr        │
  ├────────────────────────────────────────┼────────────────────────────────────┤
  │ When is precession forcing strongest? │ When e is large (e·sin(λ̃) large)  │
  │ When is it zero?                       │ When e ≈ 0 (nearly circular orbit) │
  ├────────────────────────────────────────┼────────────────────────────────────┤
  │ Does warming happen globally at once?  │ No — precession signal is anti-    │
  │                                        │ phased between hemispheres;        │
  │                                        │ obliquity and eccentricity are     │
  │                                        │ in-phase globally                  │
  ├────────────────────────────────────────┼────────────────────────────────────┤
  │ Is CO₂ a Milankovitch forcing?         │ No — it's a feedback. CO₂ lags     │
  │                                        │ orbital forcing by ~800–2000 yr,   │
  │                                        │ amplifies the initial insolation   │
  │                                        │ signal via greenhouse effect       │
  └────────────────────────────────────────┴────────────────────────────────────┘
```

---

## Common Confusion Points

**"Milankovitch cycles cause ice ages" — are they sufficient?**
No. Orbital forcing explains *timing* and *pacing* but not amplitude. Ice-albedo feedback (bright ice reflects more → cooler → more ice), CO₂ feedback, and ocean circulation changes amplify a modest insolation signal into a multi-km ice sheet. Orbital forcing alone, without feedbacks, would produce temperature changes of ~1°C; observed glacial-interglacial difference is ~5–8°C globally.

**"Precession period is ~26,000 yr but climate precession is ~21,000 yr"**
Axial precession (26 kyr) moves the equinoxes westward. Apsidal precession (112 kyr) moves the perihelion eastward. For climate, what matters is the perihelion position *relative to the equinoxes* — combining both rates gives ~21 kyr. These are the same rotation but measured in different reference frames.

**"High eccentricity → warmer Earth"**
Not meaningfully. Total annual insolation increases by ~0.18% at e=0.06 — negligible for global mean temperature. What eccentricity does is *increase seasonal contrast* and *modulate the precession amplitude*. The hemispheres compensate almost perfectly in annual average.

**"We're overdue for an ice age"**
The orbital forcing is currently ice-age-unfavorable (low eccentricity reducing precession amplitude, obliquity near midrange). Berger & Loutre (2002) calculated the next glaciation would be delayed ~50,000 yr even without anthropogenic CO₂. With current CO₂ levels, it's likely pushed back 100,000+ yr.

**"The 100-kyr cycle is the eccentricity cycle"**
Approximately — but it's really the *beat envelope* of the ~95 kyr and ~125 kyr eccentricity terms. The spectrum has no single 100-kyr peak; what you see in the ice record is a cluster around 100 kyr that smears across this range. The 413-kyr cycle is the purer, more stable eccentricity period.

**Phase vs period — the precession "paradox"**
Precession determines the *season* when perihelion falls. When NH summer falls at perihelion: hotter summers, more melt, less ice → interglacial. This seems counterintuitive — shouldn't hotter summers mean warming? Yes, but hotter NH summers also correlate with *cooler SH winters* (precession is antisymmetric). The NH wins because more land at high northern latitudes amplifies the ice-albedo feedback.
