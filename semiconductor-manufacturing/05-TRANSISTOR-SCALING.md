# Transistor Scaling — A Layered Guide

## The Big Picture

The MOSFET has been scaled from 10 µm (1971) to ~10 nm (2025) gate lengths.
Planar geometry hit a wall at ~20 nm from short-channel effects. FinFET
provided a decade of continued scaling. Gate-all-around (GAA) nanosheet transistors
are now taking over at 2 nm and below.

```
TRANSISTOR ARCHITECTURE EVOLUTION
════════════════════════════════════════════════════════════════════

PLANAR MOSFET (1960-2011, 10 µm → 22 nm):
  Gate
   │
───┴─── Gate oxide (SiO₂ → high-k HfO₂)
───────  Channel (Si, p-type for NMOS)
  S/D   Bulk Si

  One gate surface controls channel
  Short-channel effects: gate loses control as L shrinks

FINFET (2011-2022, 22 nm → 3 nm):
    ┌──────┐
    │ Gate │  Gate wraps 3 sides of fin
    │ ┌──┐ │  (top + two sides)
    │ │Fi│ │
    │ │n │ │  Enhanced gate control
    │ └──┘ │
    └──────┘
  Source ───── Drain through fin

GAA NANOSHEET (2022+, 3 nm and below):
  Gate wraps ALL FOUR sides of multiple Si nanosheets
  Stacked 3-5 nanosheets per transistor → multiple channels in parallel
  → Maximum electrostatic control, lowest leakage

  [Gate surrounds each nanosheet completely]
  ────────────────────────────────── ← Nanosheet 3
  [Gate surrounds each nanosheet completely]
  ────────────────────────────────── ← Nanosheet 2
  [Gate surrounds each nanosheet completely]
  ────────────────────────────────── ← Nanosheet 1
  Source                              Drain
```

---

<!-- @editor[audience/P2]: MOSFET Fundamentals section derives transistor operation from first principles — Vgs/Vt threshold voltage, IDS current equations (linear and saturation regions), subthreshold slope from Boltzmann — calibration explicitly says learner does NOT need "what a transistor is"; this section belongs in an introductory guide, not a reference targeting MIT TCS/Math; replace with the scaling-relevant parameters (Ion/Ioff ratio, SS approaching Boltzmann limit, effective oxide thickness) framed as engineering constraints, not device physics lecture -->

## MOSFET Fundamentals

```
NMOS MOSFET OPERATION

STRUCTURE:
  p-type Si substrate
  n+ source (S), n+ drain (D) — heavily doped
  Thin gate insulator (SiO₂ or HfO₂) over channel
  Gate electrode (poly-Si or metal)

           Gate (G)
              │
  S ─── [gate oxide] ─── D
        p-Si channel
        ──────────────

THRESHOLD VOLTAGE Vt:
  Vt = flat-band voltage + charge terms + 2φ_F
  At V_GS < Vt: channel depleted, minimal current (subthreshold leakage)
  At V_GS > Vt: inversion layer forms (electrons) → conducting channel

CHANNEL CURRENT (long channel):
  Linear region (V_DS < V_GS - Vt):
    I_D = µn·Cox·(W/L)·[(V_GS - Vt)·V_DS - V_DS²/2]

  Saturation (V_DS ≥ V_GS - Vt):
    I_D = ½·µn·Cox·(W/L)·(V_GS - Vt)²

  Cox = ε_ox / t_ox   (gate capacitance per area)
  µn = electron mobility (~450 cm²/V·s in channel vs bulk 1350)
  W/L = width-to-length ratio (design parameter)

KEY DESIGN PARAMETERS:
  Vt: threshold voltage (sets speed vs leakage trade-off)
  Ion: on-state current (determines drive strength, speed)
  Ioff: off-state leakage (determines standby power)
  SS (subthreshold slope): mV/decade to turn transistor on/off
    Ideal: 60 mV/decade at room temperature (Boltzmann limit)
    FinFET/GAA: 65-70 mV/decade (near-ideal)
    Planar short-channel: 80-120 mV/decade (degraded by short-channel effects)
```

---

## Short-Channel Effects: Why Planar Scaling Hit a Wall

```
SHORT-CHANNEL EFFECTS (SCE)

As gate length L shrinks:
  Drain depletion region approaches source depletion region
  → Source and drain "share" electrostatic control with gate
  → Gate loses ability to fully shut off the channel

KEY SHORT-CHANNEL EFFECTS:

1. DRAIN-INDUCED BARRIER LOWERING (DIBL):
   High V_DS lowers source-end barrier → threshold voltage drops
   DIBL = ΔVt / ΔV_DS (mV/V) — ideally 0; SCE causes 50-200 mV/V
   → Vt depends on V_DS → circuit design complications

2. THRESHOLD VOLTAGE ROLLOFF:
   Vt decreases as L decreases (for fixed doping/oxide)
   → Can't reduce L without compensating (higher doping, thinner oxide, body bias)
   → Higher doping → worse mobility + variability

3. SUBTHRESHOLD SLOPE DEGRADATION:
   SS > 60 mV/decade as SCE worsens
   → Higher Voff for same Ion → more power waste

4. PUNCH-THROUGH:
   Source and drain depletion regions merge at high V_DS
   → Uncontrolled current flows deep in bulk → catastrophic

5. GATE OXIDE LEAKAGE:
   SiO₂ thinner than ~1.2 nm → direct tunneling → substantial gate current
   → Intel: 90 nm node (2003), SiO₂ ≈ 1.2 nm → switched to HfO₂ + metal gate

NATURAL LENGTH λ (screening length):
  λ = √(ε_Si/ε_ox · t_Si · t_ox)
  SCE under control when L > 3λ
  To scale L, must reduce t_ox (→ high-k) AND t_Si (→ SOI or FinFET/GAA)
```

---

## FinFET: 3D Gate Geometry

```
FINFET (Fin Field-Effect Transistor)

INVENTION: Chenming Hu + UC Berkeley team, ~1998 (patented 2001)
FIRST HVM: Intel 22 nm Ivy Bridge (2011) — "tri-gate transistor"

KEY GEOMETRY:
  Si fin: thin vertical slab, width W_fin (typically 5-7 nm at 7 nm node)
  Gate wraps over top + two sides (tri-gate = 3 surfaces)
  Effective W = 2·H_fin + W_fin (counting all gate-controlled surfaces)

WHY BETTER THAN PLANAR:
  The fin itself is thin (W_fin = 5-7 nm) → natural length λ is small
  Gate controls channel from 3 sides → much better electrostatic control
  Can scale L aggressively (down to ~7 nm gate length) without losing control

MULTIPLE FINS PER TRANSISTOR:
  To increase drive current: multiple parallel fins
  Width = n_fins × (2·H_fin + W_fin)
  Digital logic: 1-4 fins per transistor

FINFET PROCESS CHALLENGES:
  Fin formation: RIE + SADP → fins at tight pitch (<30 nm)
  Fin height H_fin: typically 40-60 nm (creates 3D topography for all subsequent steps)
  Isolation: SiO₂ fill between fins; fin dipping (recess STI to expose fin sides)
  Epitaxial S/D merging: adjacent fins merge S/D regions → lower resistance
  Gate last (HKMG-last) process: sacrificial poly gate → remove → replace with HKMG
    Critical: prevents high-k gate from seeing high-temperature dopant anneal

FINFET SCALING LIMITS:
  Fin width can't go below ~5 nm: quantum confinement changes band structure
  At 3 nm node, fin pitch ≈ 25-30 nm → fins start to be quantum-mechanically coupled
  Multiple independent fins → GAA nanosheets become better
```

---

## GAA Nanosheet Transistors

```
GAA (GATE-ALL-AROUND) NANOSHEET TRANSISTORS

WHY:
  At 2 nm / 3 nm: need even better gate control than FinFET
  GAA = gate surrounds all 4 sides of channel → perfect electrostatic control
  Multiple nanosheets = increase drive current (parallel channels)

NANOSHEET DIMENSIONS (TSMC N2, Samsung 3GAE):
  Nanosheet width: 15-25 nm (tunable — different for PMOS/NMOS optimization)
  Nanosheet thickness: 4-6 nm (thinner → better electrostatic control)
  Nanosheet count: 3-5 per transistor
  Vertical spacing between sheets: ~10 nm (for inner spacer + gate)

FABRICATION SEQUENCE (SiGe/Si superlattice approach):

  1. Grow alternating Si/SiGe superlattice (3-5 pairs) on substrate
     SiGe: sacrificial (will be removed)
     Si: nanosheets (will be channels)

  2. Pattern fins (same as FinFET start)

  3. Inner spacer formation:
     Laterally etch SiGe between sheets (selective SiGe etch: Cl₂/HBr)
     ALD spacer material fills recesses → inner spacers isolate gate from S/D

  4. Epitaxial source/drain (surrounds all nanosheets)

  5. Gate last (HKMG): remove sacrificial poly gate
     ↓
     Selective etch SiGe nanosheets (HCl gas or wet etchant → only SiGe removed)
     ↓
     Si nanosheets suspended (inner spacers hold them)
     ↓
     ALD high-k + metal gate wraps around each nanosheet completely

FORKSHEET TRANSISTOR (next step):
  Intel and imec concept: NMOS and PMOS forksheets separated by dielectric wall
  Side-by-side instead of FinFET n/p pair → smaller cell area
  Still research (2025)

CFET (Complementary FET):
  PMOS stacked directly above NMOS on same footprint
  Extreme density: 1 CFET ≈ 2 standard nanosheet transistors area
  Requires wafer bonding or complex NMOS-first + PMOS-on-top process
  Intel 14A / TSMC N1 era (2027-2028 roadmap)
```

---

## Doping and Ion Implantation

```
ION IMPLANTATION

HOW IT WORKS:
  Dopant ions (As, P, B, BF₂, In) accelerated at 1-200 keV
  Implanted into Si → penetrate to defined depth
  Energy → depth profile; dose (ions/cm²) → concentration

STOPPING MECHANISMS:
  Nuclear stopping: ion collides with Si nuclei → scatter, displace atoms → damage
  Electronic stopping: ion loses energy to electron excitation → ionization
  Range distribution: Gaussian approximation
    Rp = projected range (peak depth, depends on energy + mass)
    ΔRp = straggle (standard deviation of range)

ANNEALING:
  Post-implant damage must be repaired: rapid thermal anneal (RTA) or laser anneal
  RTA: 1000-1100°C for 1-10 s → electrically activates dopants, repairs crystal
  Spike anneal: <1 s at high T → minimize dopant diffusion while maximizing activation
  Laser (millisecond or nanosecond): melt-recrystallization → ultra-shallow junctions

ULTRA-SHALLOW JUNCTIONS (USJ):
  Source/drain extensions at <10 nm depth required for sub-10 nm MOSFETs
  BF₂ implant (heavier → shallower range than B)
  Cluster ion implantation (B₁₀H₁₄⁺): spreads dose → shallower, lower damage
  Plasma doping (PLAD): alternative to beamline implant for conformal doping

HALO (POCKET) IMPLANTS:
  Tilted implant of same type as body (e.g., p-type for NMOS)
  Creates higher-doped regions under S/D → reduces DIBL
  Critical for planar down to FinFET transition; FinFET reduces need (better geometry)
```

---

## High-k/Metal Gate (HKMG)

```
HIGH-k/METAL GATE (HKMG)

THE PROBLEM (Intel 90 nm node, 2003):
  SiO₂ gate oxide below 1.2 nm → direct tunneling leakage unacceptable
  P = A·e^(-B·tox) → gate leakage 10-100 A/cm² at <1.2 nm SiO₂

HIGH-k SOLUTION:
  Replace SiO₂ (k=3.9) with HfO₂ (k=22) or HfSiO (k=12-16)
  Same EOT (electrical thickness) but physically thicker → less tunneling

  EOT = t_high-k × (ε_SiO₂ / ε_high-k)
  EOT = 2 nm HfO₂ × (3.9/22) = 0.35 nm equivalent
  Physical thickness 2 nm → tunneling negligible (tunneling ∝ exp(-2 nm))

METAL GATE:
  Old poly-Si gate: Fermi-level pinning on high-k → wrong Vt for CMOS
  Fix: replace poly-Si with metals
  NMOS: low work function metal (TiN, TaC, La₂O₃-doped TiN) → low Vt
  PMOS: high work function metal (TiN with Al-free anneal, MoN, TiAlN) → correct Vt

GATE-FIRST vs GATE-LAST:
  Gate-first: deposit HKMG early → high-T anneal damages high-k
  Gate-last (replacement metal gate, RMG): deposit sacrificial poly → do all high-T →
    remove poly → deposit HKMG in completed structure → ALD to backfill
  Gate-last is now universal at 14 nm and below
  Challenge: HKMG fills into tight space left by removed poly gate

WORK FUNCTION ENGINEERING:
  V_t ≈ WF_metal - WF_Si - fixed charge terms - Qinv/Cox
  Tune Vt by: metal composition, aluminum content in TiN, La/Al interfacial layers
  Multi-Vt: same metal, different anneal/thin film → 4-5 Vt options per node
  Low-Vt: fast/power-hungry; High-Vt: slow/low-leakage
```

---

## Decision Cheat Sheet

| Generation | Key Transistor Feature | Node |
|------------|----------------------|------|
| Planar MOSFET | SiO₂ gate, poly-Si gate | 10 µm → 22 nm |
| Strained Si | SiGe S/D, tensile Si channel | 90 nm (2003) |
| High-k/Metal Gate | HfO₂ + TiN/TaC | 45 nm (Intel 2007, TSMC 28 nm 2011) |
| FinFET | 3D tri-gate, much better SCE control | 22 nm (Intel 2011), 16/14 nm industry |
| GAA Nanosheet | Gate wraps all 4 sides, multiple sheets | 3 nm (Samsung 2022), 2 nm (TSMC 2025) |
| CFET (roadmap) | PMOS over NMOS, same footprint | Sub-1 nm (2028+) |

---

## Common Confusion Points

**Gate length ≠ channel length ≠ node name**: Physical gate length at "3 nm" node is ~12-15 nm.
Channel length under the gate is the gate length minus undergate spacer effects. "3 nm" is a density
benchmark (transistors/mm²), not any physical measurement.

**FinFET isn't strictly "3D"**: A FinFET fin is 2D in the sense that a single fin is a vertical
slab. The 3D aspect is that the gate wraps over three surfaces (as opposed to planar's one surface).
The fin itself is fabricated with the same planar lithography tools.

**HKMG gate-last adds many process steps**: Inserting HKMG into the space left by a sacrificial
poly-Si gate requires: poly removal (CMP + wet), HKMG ALD + metal deposition, CMP planarization.
This adds ~50 process steps compared to gate-first. The complexity is justified by the superior
interface quality of depositing HKMG on a fully processed structure.

**GAA doesn't automatically beat FinFET on everything**: GAA offers better electrostatic control
(lower leakage, better SCE), but introduces process complexity for inner spacers and nanosheet
release. At 3 nm, Samsung's 3GAE GAA yielded worse than TSMC's N3 FinFET initially. Architecture
wins on fundamentals but manufacturing maturity matters.
