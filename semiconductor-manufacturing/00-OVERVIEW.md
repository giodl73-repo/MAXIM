# Semiconductor Manufacturing — A Layered Guide

## The Big Picture

A modern chip fab operates at tolerances measured in atoms. Moore's Law compressed
transistors from 10 µm (1971) to 2 nm (2025) — a 5,000× reduction in 54 years.
This module maps the complete manufacturing stack from sand to packaged chip.

```
SEMICONDUCTOR MANUFACTURING STACK
════════════════════════════════════════════════════════════════════

LEVEL 7: SUPPLY CHAIN & GEOPOLITICS
  ASML (lithography) · AMAT/Lam/TEL (deposition/etch) · KLA (inspection)
  Taiwan concentration · CHIPS Act · export controls

LEVEL 6: PACKAGING & INTEGRATION
  Wire bond → flip-chip → 2.5D CoWoS (HBM stacks) → 3D hybrid bonding
  Chiplet disaggregation (UCIe) · System-in-Package (SiP)

LEVEL 5: YIELD & ECONOMICS
  Defect density · Yield models (Murphy/Seeds) · Cost per die
  Learning curve · N+1 node economics

LEVEL 4: PROCESS INTEGRATION
  FEOL: transistors (logic + SRAM)
  BEOL: interconnects (10-15 Cu layers, W vias, low-k dielectric)
  CMP at each layer for planarization

LEVEL 3: UNIT PROCESSES
  Lithography (DUV/EUV patterning)
  Deposition (CVD/ALD/PVD — add material)
  Etching (RIE/DRIE — remove material)
  Ion implant (doping) · Anneal · Clean · CMP

LEVEL 2: TRANSISTOR ARCHITECTURE
  Planar MOSFET → FinFET (22 nm+) → GAA nanosheet (2 nm+)
  Short channel effects · Vt control · Leakage management

LEVEL 1: SUBSTRATE
  Czochralski Si crystal → ingot → wafer (300 mm) → clean/polish
  n-type / p-type doping · SOI · Strained Si

LEVEL 0: RAW MATERIAL
  SiO₂ sand → metallurgical-grade Si → electronic-grade Si (11 nines pure)
```

---

<!-- @editor[audience/P2]: "Moore's Law: History and Slowdown" section restates Moore's Law from 1965→2025 with full transistor count table and Dennard scaling derivation — calibration explicitly says learner does NOT need "Moore's Law stated"; compress to the slowdown mechanics (Dennard break ~2005, power wall, architectural pivot to multi-core and chiplets) and cut the historical table; the learner already owns this history -->

## Moore's Law: History and Slowdown

```
MOORE'S LAW (1965 → 2025)

1965: Gordon Moore (Intel): transistor count doubles every ~2 years
  Original: halve cost per transistor; correlates with dimension scaling

HISTORICAL SCALING:
  Year  Node      Transistors/mm²   Example Chip
  ─────────────────────────────────────────────────
  1971  10 µm     ~2,000            Intel 4004 (2,300 transistors)
  1989  1 µm      ~1M               Intel 486
  2000  180 nm    ~10M              Pentium 4
  2006  65 nm     ~200M             Core 2 Duo
  2012  22 nm     ~2B               Ivy Bridge (FinFET debut)
  2016  14 nm     ~8B               Kaby Lake
  2020  7 nm      ~100B             AMD Zen 3, Apple M1
  2022  3 nm      ~170B             Apple A16, M2
  2025  2 nm      ~400B+            TSMC N2 / Intel 20A+

DENNARD SCALING (the real driver 1974-2005):
  As dimensions scaled by 0.7×: area ÷2, frequency ×1.4, power constant
  At ~2005, Dennard scaling broke: leakage current → power density hit thermal wall
  "Power wall": CPUs stopped getting faster, went multi-core

MODERN LANDSCAPE (2025):
  Physical density scaling continues but slower
  "1 nm" nodes: marketing names ≠ physical gate length (gate ≈ 5-10 nm)
  Performance improvements: architectural (Amdahl) + packaging (chiplets + 3D)
  Energy/operation still improves ~15% per node → density + efficiency, not clock speed
```

---

## Industry Structure: Fabless / IDM / Foundry

```
SEMICONDUCTOR INDUSTRY MODEL EVOLUTION
════════════════════════════════════════════════════════════════════

IDM (Integrated Device Manufacturer) — 1970s-1990s dominant model:
  Design → Fab → Test → Package under one roof
  Examples: Intel, Samsung, Texas Instruments, Micron
  Advantage: tight vertical integration
  Disadvantage: $15-20B per leading-edge fab (2024), enormous capital burden

FABLESS MODEL (1980s onward):
  Design only; outsource all manufacturing to foundry
  Examples: Qualcomm, AMD (spun off fab → GlobalFoundries 2009),
            NVIDIA, Apple Silicon, Broadcom, MediaTek, Marvell
  Advantage: focus on IP; no fab capex
  Disadvantage: dependent on foundry; less supply chain control

FOUNDRY MODEL:
  Pure-play manufacturing for fabless customers
  Examples: TSMC (leading-edge dominant), GlobalFoundries (mature nodes),
            SMIC (China), UMC (mature nodes), Samsung Foundry (IDM hybrid)

TSMC DOMINANCE (2025):
  ~90% of leading-edge logic (≤7 nm)
  ~60% of total foundry revenue
  Apple, NVIDIA, AMD, Qualcomm all on TSMC
  Single TSMC site (Hsinchu/Tainan, Taiwan) = irreplaceable global chokepoint

EQUIPMENT TIER (upstream suppliers):
  Sell tools to fabs — not chip designers
  ASML (litho), Applied Materials (AMAT), Lam Research, KLA, Tokyo Electron (TEL)
  Materials: Shin-Etsu/Sumco (wafers), JSR/TOK (photoresists), Entegris (chemicals)

REVENUE BREAKDOWN (2024):
  Logic (CPU/GPU/mobile AP): ~$400B total (Taiwan/Korea/US/Europe fabs)
  Memory (DRAM/NAND): ~$150B (Samsung/SK Hynix/Micron)
  Foundry services: ~$130B (TSMC leads)
```

---

<!-- @editor[bridge/P2]: Missing photolithography → information encoding bridge — spatial frequency content of circuit patterns (k₁·λ/NA) is directly analogous to Nyquist sampling: the diffraction limit is the spatial Nyquist limit, and multi-patterning is spatial oversampling; an MIT math/TCS reader maps this immediately, and the analogy explains why each successive resolution doubling requires exponentially more litho steps -->

<!-- @editor[bridge/P2]: Missing yield curve → reliability engineering bridge — Murphy's model (infant-mortality defect clustering → binomial yield distribution) is the manufacturing analog of the software reliability bathtub curve (burn-in failures + steady-state + wear-out); die yield binning by speed/power grade is also directly analogous to SLA-tier provisioning; learner has the MTTF/SLA modeling background from VSTS/Azure infrastructure -->

## Fab Process Flow at a Glance

```
WAFER MANUFACTURING FLOW (~600-800 process steps at 3 nm node)
════════════════════════════════════════════════════════════════════

START
  │
  ▼
Wafer preparation
  Czochralski growth → slicing → CMP → cleaning
  300 mm diameter, ~775 µm thick
  │
  ▼
FEOL (Front End of Line) — Build transistors
  Shallow Trench Isolation (STI) — electrically isolate wells
  Well formation — implant N/P dopants, anneal
  Gate stack — high-k/metal gate (HKMG) deposition
  Source/drain — epitaxial SiGe/SiP growth (strain engineering)
  Silicide — NiSi contacts to S/D and gate
  Contact (W plugs) — connect S/D/gate to metal layers
  │
  ▼
BEOL (Back End of Line) — Build interconnects
  Metal 1-15: alternating Cu damascene lines + vias
    For each layer:
      Dielectric deposition (low-k SiCOH or SiO₂)
      Lithography + etch trenches/vias
      Ta/TaN barrier + Cu seed
      Electroplating Cu
      CMP → flat surface for next layer
  Top metal: Al bond pads (wire bond) or thick redistribution layer (RDL) for flip-chip
  │
  ▼
Wafer-level testing
  Probe card contacts each die → sort good/bad
  │
  ▼
Dicing
  Diamond saw or laser → individual dies
  │
  ▼
Packaging
  Wire bond / flip-chip / 2.5D / 3D (see 07-PACKAGING.md)
  │
  ▼
Final test + binning
  Speed-binned: fastest → highest price (Intel i9 vs i5 from same wafer)
  Voltage-binned: lowest voltage → premium tier

TOTAL TIME: ~3 months fab + 1-2 weeks test/package
LAYERS: up to 100+ individual process steps at 3 nm
```

---

## The Key Numbers

```
CHARACTERISTIC DIMENSIONS (leading edge, 2024-2025)

Feature                       3 nm node    2 nm node
────────────────────────────────────────────────────
Gate length (physical)        12-15 nm     10-12 nm
Gate pitch                    48 nm        42 nm
Metal pitch (M1)              24 nm        20 nm
Contacted poly pitch (CPP)    48 nm        42 nm
Transistor type               FinFET       GAA nanosheet
Interconnect layers           15-18        15-20
EUV layers                    ~15          ~20+
Transistor density            ~170 MT/mm²  ~300+ MT/mm²

FAB ECONOMICS
  Leading-edge fab cost:      $15-20B (TSMC N3 fab = ~$20B)
  EUV tool cost:              $150-380M per machine (NXE:3600D)
  Wafer cost (3 nm):          ~$20,000 per 300 mm wafer
  Dies per wafer (1 cm² die): ~600 gross; ~450 after yield
  Cost per die (typical):     $50-400 depending on size + yield
```

---

## Module Map

```
MODULE MAP
════════════════════════════════════════════════════════════════════

01-SILICON-SUBSTRATE.md    Czochralski, wafer prep, doping, SOI
02-LITHOGRAPHY.md          DUV/EUV, multi-patterning, ASML
03-DEPOSITION.md           CVD/ALD/PVD, epitaxy, conformal films
04-ETCHING.md              RIE, DRIE, wet etch, endpoint detection
05-TRANSISTOR-SCALING.md   MOSFET → FinFET → GAA, scaling limits
06-PROCESS-INTEGRATION.md  FEOL/BEOL, Cu damascene, low-k RC delay
07-PACKAGING.md            Flip-chip, CoWoS, TSV, chiplets
08-YIELD-ECONOMICS.md      Defect density, yield models, cost per die
09-SUPPLY-CHAIN.md         ASML/AMAT/Lam/KLA, Taiwan risk, CHIPS Act
```

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| Why is leading-edge fab so concentrated in Taiwan? | Decades of compound investment (TSMC), network of local suppliers, government support — not easily replicated |
| What's actually "2 nm"? | A marketing label — physical gate ≈10 nm; "nm" refers to density/architecture benchmark, not a dimension |
| Why did CPU clock speeds plateau ~2005? | Dennard scaling broke (leakage → heat); power wall hit; industry pivoted to multi-core |
| Why are chiplets suddenly important (2020s)? | Advanced packaging (CoWoS, 3D) partly substitutes for atomic-scale fab improvements |
| What limits below 2 nm? | Variability (quantum tunneling through gate), interconnect RC delay, heat density, lithography resolution |

---

## Common Confusion Points

**"Node name" ≠ any physical dimension**: The TSMC "3nm" node has a gate length of ~12-15 nm.
Node names are competitive marketing labels since ~16 nm. Compare transistor density (MT/mm²) for
honest comparisons, not node names.

**Moore's Law ≠ just transistor count**: The original observation was about cost per transistor.
When people say "Moore's Law is slowing," they mean the rate of cost/transistor improvement has
slowed, not that transistors aren't getting smaller.

**Fabless doesn't mean fabs don't matter**: Apple designs the M4 chip (fabless perspective) but
is entirely dependent on TSMC's 3 nm process. The "fabless" label describes the business model,
not the importance of manufacturing to product success.

**TSMC isn't a monopoly by coercion**: It's a monopoly by accumulated advantage — 30+ years of
process R&D, customer relationships, equipment partnerships, and compound learning. Samsung
Foundry and Intel Foundry Services are genuine alternatives but currently trail by 1-2 nodes.
