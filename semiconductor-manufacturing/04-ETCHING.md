# Etching — A Layered Guide

## The Big Picture

Etching selectively removes material from the wafer. Lithography defines where;
etching executes the cut. The central tension: isotropic etching (removes in all
directions equally) vs. anisotropic etching (removes only vertically). High-aspect-
ratio structures require near-perfect anisotropy.

```
ETCHING TAXONOMY
════════════════════════════════════════════════════════════════════

ETCHING
├── WET ETCHING (liquid chemicals)
│   ├── Isotropic (attacks all crystal planes equally)
│   │   Examples: HF for SiO₂, H₃PO₄ for Si₃N₄
│   └── Anisotropic (crystal-plane selective)
│       Example: KOH etches Si <110> fast, <111> very slow
│       → V-grooves in MEMS
│
└── DRY ETCHING (gas/plasma)
    ├── Physical (ion bombardment, sputtering)
    │   Pure physical: directional but low selectivity
    ├── Chemical (reactive gas species)
    │   Pure chemical: isotropic, high selectivity, no ion damage
    └── RIE (Reactive Ion Etching) — DOMINANT
        Physical + chemical synergy:
        → Anisotropic (ions directional) + high selectivity (chemistry)
        → Can't be achieved by either mechanism alone
```

---

## Wet Etching

```
WET ETCHING — ISOTROPIC

MECHANISM:
  Liquid etchant diffuses to surface → chemical reaction → soluble product → diffuses away
  Three transport steps: diffusion to surface, surface reaction, product diffusion away
  Rate limited by slowest step

KEY WET ETCHANTS:

HF (Hydrofluoric acid):
  Etches SiO₂ rapidly: SiO₂ + 6HF → H₂SiF₆ + 2H₂O
  Selectivity: SiO₂ >> Si, Si₃N₄ (SiO₂:Si selectivity ~1000:1)
  BHF (Buffered HF = NH₄F + HF): controlled etch rate, prevents pH drift
  Applications: oxide strip, pre-gate clean, STI recess, contact etch (assisted)

H₃PO₄ (Phosphoric acid, 85%, 160°C):
  Etches Si₃N₄ selectively over SiO₂ (selectivity ~35:1 at 160°C)
  Used for: nitride spacer wet strip during GAA nanosheet release

SC1 (Standard Clean 1: NH₄OH + H₂O₂ + H₂O):
  Removes particles and organic contamination
  Slightly etches SiO₂ (helps lift particles)
  SC2 (HCl + H₂O₂ + H₂O): removes metals

H₂O₂ + H₂SO₄ (Piranha):
  Aggressive oxidation: removes all organic contamination, photoresist
  "Piranha" dissolves organic material rapidly

SELECTIVITY DEFINITION:
  S = etch rate of target / etch rate of masking layer
  Good wet etch selectivity: >50:1
  Problem: isotropic wet etch undercuts resist/oxide mask horizontally
    Undercut = etch depth × lateral_etch_factor
    → Limits patterning to features > ~1 µm

ANISOTROPIC WET ETCHING (Si only):
  KOH (potassium hydroxide, 30%, 80°C):
    Etch rate: <110> >> <100> >> <111>
    <110>/<111> ratio: ~400:1 → very selective
    Creates V-grooves (54.7° angle from wafer surface)
  TMAH (tetramethylammonium hydroxide): CMOS-compatible alternative (no K⁺ contamination)
  Applications: MEMS microstructures, pressure sensors, accelerometers
```

---

## Reactive Ion Etching (RIE)

```
RIE — REACTIVE ION ETCHING

THE KEY INSIGHT (1970s discovery):
  In an SF₆ plasma, fluorine radicals etch Si isotropically
  Ion bombardment alone (Ar+ sputtering) etches Si, but slowly and non-selectively
  Combined F radicals + ion bombardment: etch rate 10-100× higher than either alone
  AND etch is anisotropic (only where ions hit = horizontal surfaces)
  → Synergy: ions damage bonds → radicals react with damaged bonds → volatile products removed

RIE CHAMBER:
              Gas inlet
                │
  ┌─────────────────────────────┐
  │    Upper electrode (grounded or RF)    │
  │                             │
  │         Plasma zone         │  ← RF plasma (13.56 MHz + 27.12 MHz)
  │    (reactive radicals + ions)│
  │                             │
  │    [  Wafer  ]              │  ← Lower electrode (powered, DC bias)
  └─────────────────────────────┘
        Gas exhaust
        (vacuum pump)

Sheath at wafer: electric field accelerates ions downward → vertical bombardment
Radicals: diffuse isotropically but only enhance etch where ions hit
Result: anisotropic profile

IMPORTANT ETCH GASES:

Si etching:
  SF₆/O₂: fast, isotropic or slightly anisotropic (F radicals dominant)
  HBr/Cl₂ + O₂: anisotropic (SiBrₓ sidewall passivation)
  Used for: gate poly-Si etch, Si fin etch

SiO₂ etching:
  CHF₃/CF₄ or C₄F₈/O₂: fluorocarbon chemistry
  C-F polymer deposits on sidewalls → inhibits lateral etch → anisotropic
  Selectivity over Si: 10-20:1 (with polymer chemistry)

Si₃N₄ etching:
  CHF₃ or CH₂F₂: similar fluorocarbon chemistry
  Selectivity over SiO₂: 5-10:1 (depends on gas mix)

Metal etching (Al, W, TiN):
  Cl₂ + BCl₃: aluminum (AlClₓ volatile products)
  SF₆ or NF₃ + Cl₂: tungsten (WF₆ volatile)
  Cl₂/Ar: TiN hard mask, barrier metals

ETCH SELECTIVITY:
  Selectivity in RIE set by:
  1. Thermodynamic: which reaction products are volatile (Si-Cl₂ → SiCl₄ volatile; oxide less so)
  2. Kinetic: ion bombardment threshold differs per material
  3. Passivation: fluorocarbon polymer preferentially deposits on SiO₂ vs Si

ETCH RATE TERMS:
  Etch rate: nm/min or Å/min (typical 100-500 nm/min for RIE)
  Selectivity: S = ER_target / ER_mask (want S >> 1)
  Uniformity: (ERmax-ERmin)/(2×ERavg) < 2% acceptable
  Profile angle: 90° = perfectly vertical (anisotropic); <90° = tapered
  CD bias: difference between printed CD and etched CD (RIE loading, ILD)
```

---

## DRIE: Deep Reactive Ion Etching

```
DRIE — DEEP REACTIVE ION ETCHING (Bosch Process)

PROBLEM:
  Standard RIE: aspect ratio ~3-5:1 limited
  Deep trenches (MEMS, TSV, DT capacitors in DRAM) need 10:1 to 100:1
  And still vertical sidewalls

BOSCH PROCESS (Robert Bosch GmbH, 1994 patent):
  Alternating cycles of:
    1. ETCH step (SF₆, ~10 s):
       F radicals + ions → isotropic Si etch (undercuts slightly)
    2. PASSIVATION step (C₄F₈, ~5 s):
       C₄F₈ plasma deposits thin fluoropolymer on ALL surfaces
    3. Next ETCH step:
       Ions remove polymer from horizontal surfaces (floor)
       Polymer protects sidewalls from lateral F-radical attack
    4. Etch continues downward; repeat

SCALLOPING:
  Each cycle: tiny lateral undercut before passivation → "scallops" on sidewall
  Scallop amplitude: 50-200 nm depending on cycle time
  Fine-tuned: shorter cycles → smoother walls but lower throughput
  Modern DRIE: scallops <50 nm, sidewall angle 88-90°

ACHIEVABLE:
  Aspect ratio: up to 50:1 or more
  Etch depth: up to 700 µm (through-wafer)
  Etch rate: 3-20 µm/min (much faster than RIE)
  Selectivity to SiO₂ mask: 100-200:1

APPLICATIONS:
  TSV (Through-Silicon Via): 5-100 µm diameter × 50-150 µm deep
  MEMS: cantilevers, accelerometers, gyroscopes (Bosch MEMs chips)
  DRAM capacitor trench: 6:1 to 10:1 aspect ratio deep trench capacitors
  NEMS: nano-resonators
  Power device mesa structures
```

---

## Endpoint Detection

```
ENDPOINT DETECTION

WHY IT MATTERS:
  Etch too little: residual material (short circuits, incomplete contact)
  Etch too much: over-etch damages underlying layer, alters device properties
  Target: stop exactly when target layer is cleared

METHODS:

1. OPTICAL EMISSION SPECTROSCOPY (OES) — most common:
   Monitor light emission from plasma during etch
   Emission spectrum changes when target material is consumed
   Example: Si etch by Cl₂/HBr → SiCl* (414 nm) emission drops when Si consumed
   CN (388 nm) emission appears when resist cleared
   Alert: step change in emission → endpoint detected

2. LASER INTERFEROMETRY:
   Coherent laser reflects off wafer surface
   As film etches, reflected beam changes phase → oscillating intensity
   Period = λ/(2n) of film → calculate etch rate + remaining thickness
   Excellent for controlled partial etches (e.g., etch 50% of dielectric)
   Requires transparent film and smooth surface

3. MASS SPECTROMETRY (residual gas analysis):
   Sample etch byproduct gases via QMS
   Monitor specific m/z fragments
   HF (m/z=20) spike → end of SiO₂ etch
   Good for ultra-thin films where OES signal is weak

4. ETCH TIME + RATE (blanket wafer calibration):
   Pre-measure etch rate on monitor wafer
   Set etch time = target_thickness / etch_rate + overetch%
   Simple but affected by loading effects, chamber state, film-to-film variation

APC (ADVANCED PROCESS CONTROL):
  Measure pre-etch thickness (scatterometry/ellipsometry)
  Model etch rate from previous runs + chamber history
  Adjust etch time + bias per-wafer
  Reduces CD variability dramatically
```

---

## Atomic Layer Etching (ALE)

```
ATOMIC LAYER ETCHING (ALE)

THE ALD INVERSE:
  ALD deposits one monolayer per cycle (self-limiting)
  ALE removes one monolayer per cycle (self-limiting)

MECHANISM (thermal ALE of Al₂O₃ example):
  Half-cycle A: HF pulse → fluorinates top monolayer (AlF₃)
  Purge
  Half-cycle B: TMA pulse → reacts with AlF₃ → volatile Al(CH₃)ₓFₓ desorbs
  Purge
  Result: exactly one monolayer (∼0.1 nm) removed

PLASMA ALE (for Si):
  Cycle A: Cl₂ adsorption → chlorinates exactly top monolayer of Si
  Cycle B: Ar⁺ ions at precisely threshold energy → remove only Cl-modified layer
    (ions too energetic → sputter; too slow → no reaction; must be in "ALE window")

APPLICATIONS:
  GAA transistor: release nanosheet by etching sacrificial SiGe selectively between Si
  FinFET fin trimming: control fin width to atomic precision
  High-k gate etch (post-high-k metal gate last process)
  Memory: removing exactly 1 layer of cell material for yield improvement
  Still emerging in HVM (leading edge uses selective etch + etch bias control)

ALE vs ALD SYMMETRY:
  ALD: add → A + B pulse → net gain
  ALE: remove → A + B pulse → net loss
  Can sequence them for atomic-level growth + etch = atomic precision 3D sculpting
```

---

## Decision Cheat Sheet

| Etch Application | Method |
|-----------------|--------|
| SiO₂ removal (isotropic, large features) | Wet HF or BHF |
| Si₃N₄ removal (CMOS-compatible) | Wet H₃PO₄ at 160°C |
| Si or poly-Si gate etch (vertical, high sel.) | RIE: HBr/Cl₂/O₂ |
| Contact/via oxide etch (anisotropic) | RIE: CHF₃/C₄F₈ fluorocarbon |
| Metal (Al/W/TiN) etch | RIE: Cl₂/BCl₃ or SF₆ |
| Deep trench MEMS/TSV (high aspect ratio) | DRIE Bosch process |
| Gate stack precision trim (atomic scale) | ALE (plasma or thermal) |
| Etch end point for oxide breakthrough | OES (λ-specific emission) |
| Etch end point for thin film (measured depth) | Laser interferometry |

---

## Common Confusion Points

**RIE selectivity is chemistry + physics, not just one**: Selectivity in RIE comes from (a) volatility
of etch products (AlCl₃ vs AlO — chlorine gives volatile product), (b) passivation (fluorocarbon
polymer protects SiO₂ sidewalls), and (c) threshold ion energy differences. Changing gas mix
dramatically changes selectivity.

**"Plasma etching" isn't a synonym for RIE**: Pure plasma etching (barrel reactor) uses radicals only —
isotropic, good selectivity, but no anisotropy. RIE adds directional ion bombardment. Then there's
ICP (inductively coupled plasma) which has separate plasma generation + bias — more control.

**Bosch scallops aren't a defect to eliminate, just a trade-off**: The scalloping in DRIE is inherent
to the pulsed chemistry. Applications that care about smooth sidewalls (optical MEMS, high-Q
resonators) use cryogenic DRIE (continuous passivation by SiOxFy at -100°C) which can give nearly
scallop-free sidewalls at the cost of higher complexity.

**Selectivity is relative, not absolute**: "SiO₂:Si selectivity of 20:1 in CHF₃/O₂" means you
etch 20 nm oxide for every 1 nm Si consumed. But if you overetch 2× to ensure clearance, you
lose 2/20 = 10% of the Si — potentially destructive at nm-scale transistors. This is why endpoint
detection is critical: minimize overetch time.
