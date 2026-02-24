# Process Integration — A Layered Guide

## The Big Picture

Process integration orchestrates hundreds of individual unit process steps into
a coherent manufacturing flow. The key division: FEOL (front end of line) builds
transistors; BEOL (back end of line) builds the copper interconnect pyramid
connecting them. Everything must be compatible — thermally, chemically, mechanically.

```
PROCESS INTEGRATION OVERVIEW
════════════════════════════════════════════════════════════════════

FEOL — Front End of Line
  Objective: Fabricate transistors and their immediate contacts
  Materials: Si, SiGe, SiO₂, Si₃N₄, HfO₂, TiN, TaC, W
  Temperature budget: up to 1050°C (dopant activation)
  ─────────────────────────────────────────────────────────────
  STI → Well implants → Gate stack (HKMG) → S/D epitaxy
  → Spacers → S/D implant → Silicide → Contacts (W) → Pre-Metal Dielectric

MIDDLE END (MEOL) — Contacts to M1
  Objective: Land vertical connections to transistor terminals
  Key: W (tungsten) plugs or Ru contacts at 2 nm node
  Height: ~100-200 nm of dielectric + via

BEOL — Back End of Line
  Objective: Route signals, power, clock across chip
  Materials: Cu, low-k SiCOH, TaN/Ta barrier, ULK dielectric
  Temperature budget: <400°C (Cu flows at higher T; low-k degradation)
  ─────────────────────────────────────────────────────────────
  Metal 1 → Via 1 → Metal 2 → ... → Metal 15+ → Pad metal (Al/thick Cu)
  Each level: dielectric deposition → litho → etch → barrier → Cu → CMP

BACK-SIDE POWER DELIVERY (BSPDN) — emerging at 2 nm:
  Power rails moved to back side of wafer (via nano-TSVs)
  Front side freed for signal-only routing → density improvement
```

---

## FEOL: Building Transistors

```
FEOL PROCESS SEQUENCE (CMOS, gate-last HKMG, FinFET example)

1. SHALLOW TRENCH ISOLATION (STI):
   - LPCVD Si₃N₄ hard mask
   - Litho + RIE: etch Si ~300 nm deep trenches
   - HDP-CVD SiO₂ fill (void-free)
   - CMP planarize to Si₃N₄ surface
   - Wet strip Si₃N₄ → exposed Si between STI blocks

2. WELL FORMATION:
   - Triple-well implants: deep n-well, p-well, n-well
   - Photoresist mask for each well type
   - Dopant activation anneal: 900-1000°C, 30 min in furnace
   - Well depth: 0.5-2 µm; well doping: 10¹⁶-10¹⁷ cm⁻³

3. FIN FORMATION (FinFET specific):
   - SADP to define fin pitch → Si fin etch via RIE (HBr/Cl₂)
   - Fin width: 5-7 nm (at 7 nm node)
   - STI recess: wet HF to expose fin sides → gate can wrap fin

4. DUMMY GATE (gate-last approach):
   - LPCVD poly-Si + SiO₂ hard mask
   - Gate litho + etch → dummy gate at target CD
   - Offset spacer: thin SiO₂ ALD → spacer etch (controls S/D proximity)

5. SOURCE/DRAIN FORMATION:
   - Halo implant (tilted, same type as body) → reduce DIBL
   - Main spacer deposition: ALD Si₃N₄ (~10-15 nm wide)
   - Source/drain etch: remove Si in S/D regions
   - Epitaxial SiGe (PMOS) or SiP (NMOS): selective CVD growth
     → Creates strain in channel + raised S/D (lower resistance)
   - S/D doping: in-situ doped epitaxy (boron in SiGe for PMOS)

6. SILICIDE (Ohmic contact to S/D and poly gate):
   - PVD Ni or NiPt deposition (~8 nm)
   - Anneal: NiSi forms at ~450°C
   - Selective wet etch: remove unreacted Ni (not silicide)
   - Result: low-resistance NiSi contacts

7. PMD (Pre-Metal Dielectric) and REPLACEMENT METAL GATE:
   - PECVD/CVD SiO₂ blanket deposition → planarization (CMP)
   - Open gate area: CMP + selective etch to expose dummy poly-Si gate
   - HF strip dummy oxide
   - ALD HfO₂ (2 nm): gate dielectric
   - ALD TiN: work function metal layer (NMOS or PMOS tuned)
   - CVD W or ALD Ru: gate fill
   - Gate metal CMP → completed replacement metal gate

8. CONTACTS (MEOL):
   - PMD etch: open contact holes to S/D and gate (stopping on silicide)
   - ALD Ti/TiN liner + CVD W fill → W plug
   - CMP planarize → flat surface with W plug tops exposed
   - At 2 nm: Ru contacts (Ru has lower resistivity than W at sub-10 nm dimensions)
```

---

## BEOL: Copper Damascene Interconnects

```
COPPER DAMASCENE PROCESS

WHY COPPER?
  Al (original BEOL metal): ρ_Al = 2.7 µΩ·cm, prone to electromigration at high J
  Cu (since ~1998, IBM 180 nm): ρ_Cu = 1.68 µΩ·cm (37% lower), 5× better EM resistance
  Couldn't be dry-etched (CuClₓ not volatile at room temp) → invented Damascene

SINGLE DAMASCENE (metal layer only):
  1. Deposit low-k dielectric (ILD): PECVD SiCOH or CVD SiO₂
  2. Litho + RIE: etch trenches for metal lines (not through dielectric)
  3. ALD TaN barrier (0.5-2 nm) + ALD/PVD Ta liner (~2-5 nm)
  4. PVD Cu seed layer (~20-50 nm)
  5. Electrochemical deposition (ECD): Cu fills trench from seed up
     (Bottom-up fill: additives suppress top growth, accelerate bottom → void-free)
  6. CMP: remove Cu above dielectric level → planar surface

DUAL DAMASCENE (metal + via in one fill):
  1. Deposit etch stop (SiCN) + ILD dielectric
  2. Via first: etch via holes through all ILD
     OR trench first: etch trenches; vias aligned to trench bottoms
  3. Both trench and via open → single barrier/seed/fill step
  4. Single Cu ECD fills both vias and trenches simultaneously
  5. CMP planarizes
  Advantage: one less Cu deposition + CMP cycle per via/trench pair

ELECTROCHEMICAL DEPOSITION (ECD):
  Cu²⁺ + 2e⁻ → Cu   (reduction at wafer cathode)
  Additive chemistry (from IBM/ATMI research):
    Suppressors (PEG): slow deposition on top → push Cu bottom-up
    Accelerators (SPS): accumulate at via bottom → accelerate bottom fill
    Levelers: prevent overfill / superfilling on top
  Result: void-free superfilling of 10:1 aspect ratio vias

CMP (CHEMICAL MECHANICAL POLISHING):
  Abrasive slurry (SiO₂ or Al₂O₃ particles in H₂O₂ chemistry)
  Rotating pad + wafer → mechanical + chemical removal
  Planarize: removes Cu from high points, stops at ILD
  Within-wafer uniformity: <1% CMP key spec (non-uniform → resistance variation)
  Post-CMP clean: remove particles + Cu contamination

BARRIER LAYERS:
  TaN/Ta or CoWP or Ru are barrier to Cu diffusion into dielectric
  Cu diffuses into SiO₂ in hours at room temperature → killer contamination
  TaN (ALD, 0.5-2 nm) is the primary diffusion barrier
  As dimensions shrink: barrier takes larger fraction of via → resistance increases
  At 3 nm: Ru or Co barriers being adopted (thinner effective barrier possible)
```

---

## RC Delay and Low-k Dielectrics

```
INTERCONNECT RC DELAY

THE PROBLEM:
  Interconnect RC delay dominated performance at <0.25 µm (1998+)
  Before Cu switch: polysilicon local interconnect, Al for global
  RC time constant: τ = R × C = (ρ·L/A) × (ε·A/d)
    = ρ·ε·L²/d²  (scales with L² at fixed aspect ratio)
  → As chips got larger + wires longer → RC delay dominated transistor delay

RESISTANCE:
  R = ρ·L/(W·H)  where W×H = cross-sectional area
  Reducing Cu resistivity: limit grain scattering, line-edge roughness
  At 10 nm wire width: ρ_effective ≈ 5-10 µΩ·cm (vs bulk 1.68) due to size effects
  Surface + grain boundary scattering increases resistivity severely at nm scale

CAPACITANCE:
  ILD capacitance C = ε₀·k·A/d
  Reduce k → reduce C → reduce RC

LOW-k DIELECTRIC EVOLUTION:
  SiO₂:        k = 3.9   (1970s-1998, original gate + ILD)
  FSG:          k = 3.5   (fluorinated silicate glass, late 1990s)
  SiCOH (CDO): k = 2.7-3.0  (carbon-doped oxide, PECVD, post-2000)
  Porous SiCOH: k = 2.3-2.5  (nanoporous, voids lower k; CVD post-2006)
  ULK (ultra-low-k): k = 2.0-2.3 (more porous, more fragile)
  Air gap:      k = 1.0   (literally air between lines; hard to fill later, selective)

AIR GAP INTEGRATION:
  Etch away ILD between metal lines selectively → air gap (k=1)
  Cap with PECVD conformal dielectric that bridges over air gap but doesn't fill it
  Intel used air gaps at 14 nm; industry adopts more broadly at 5 nm+

MECHANICAL FRAGILITY ISSUE:
  Lower k = more porous = mechanically weaker
  CMP shear stress can crack ULK dielectric → integration challenge
  Requires careful CMP optimization, hardmask stacks, deposition control

RESISTANCE × CAPACITANCE CROSSOVER:
  Modern timing: 50% gate delay + 50% interconnect delay (even in best flows)
  At 2 nm node: interconnect RC often dominates → BSPDN (backside power delivery)
    removes power rail resistance from critical signal path
```

---

## Metal Layer Stack

```
METAL LAYER ARCHITECTURE (3 nm node example)

LAYER        PURPOSE                      PITCH (nm)   METAL
─────────────────────────────────────────────────────────────
Contact (Co) Transistor to M0            24 nm        W or Ru
M0 (local)   Power straps, standard cell  20-24 nm    Ru or Co
V0           Contact to M1               20-24 nm     Ru or Co
M1 (semi-local) Signal routing           20-24 nm    Cu (thin)
V1           M1 to M2                    20-24 nm    Cu
M2           Signal routing              24-30 nm    Cu
V2           M2 to M3                    24-30 nm    Cu
M3-M8        Intermediate routing        40-80 nm    Cu
Vx           Vias between Mx             40-80 nm    Cu
M9-M13       Regional routing            100-200 nm  Cu (thicker)
M14-M15      Global routing (clock/power) 400+ nm    Thick Cu or Al
AP (top Al)  Bond pads or RDL start       5-10 µm    Al or thick Cu

NOTE: Total BEOL stack height at 3 nm: ~10-12 µm of Cu/dielectric layers
TOTAL PROCESS STEPS including FEOL+BEOL+litho: 600-1,000

CONTACT METAL EVOLUTION:
  W tungsten (legacy contact): high resistivity at nm scale
  Co (cobalt) or Ru (ruthenium): lower resistivity at nm scale, better fill
  M0/V0 with Ru: Samsung 3GAE, Intel 4
  Goal: minimize interface resistance between contact → transistor
```

---

## Chemical Mechanical Polishing (CMP)

```
CMP — CHEMICAL MECHANICAL POLISHING

APPLICATIONS:
  STI CMP (SiO₂ over Si₃N₄ stop)
  PMD CMP (oxide over contacts)
  Copper CMP (remove overburden, stop at ILD)
  Tungsten CMP (plug planarization)
  High-k gate CMP (gate metal planarize)

MECHANISM:
  Preston's equation: MRR = kP × P × V
    MRR = material removal rate
    kP = Preston coefficient (chemical + mechanical)
    P = applied pressure
    V = relative velocity

  Chemical: slurry chemistry reacts with surface → forms softer compound
    Cu: H₂O₂ + BTA (benzotriazole) → form Cu-BTA complex
  Mechanical: abrasive particles (SiO₂, CeO₂) remove softened material
  Net: high spots polished faster (more contact pressure) → global planarization

SELECTIVITY IN CU CMP:
  Cu removal rate: fast
  Barrier (TaN/Ta) removal rate: moderate
  ILD removal rate: slow (need to stop here)
  Selectivity Cu:barrier:ILD ≈ 50:10:1 (endpoint when barrier exposed)
  Dishing: Cu surface below ILD level (too much pressure) → resistance increase
  Erosion: ILD over dense Cu features erodes faster → uniformity issue

WITHIN-WAFER UNIFORMITY:
  Spec: <1% within-wafer range for leading-edge
  Achieved by: zonal pressure heads on polishing head, pad conditioning, endpoint
  Multi-head systems: 4-5 independent pressure zones on 300 mm wafer
```

---

## Decision Cheat Sheet

| Challenge | Integration Solution |
|-----------|---------------------|
| Transistor leakage at short L | FinFET / GAA architecture + HKMG |
| Gate oxide leakage (SiO₂ <1.2 nm) | High-k HfO₂ via ALD |
| Cu diffusion into dielectric | ALD TaN/Ta diffusion barrier |
| Interconnect RC delay | Low-k SiCOH (k=2.7) or ULK + air gaps |
| Via resistance at nm scale | Ru or Co contacts (lower ρ vs W) |
| Power delivery resistance | BSPDN (backside power delivery, 2 nm node) |
| Topography growth → litho issues | CMP after every metal layer |
| Electromigration in thin wires | Cu (5× better EM than Al) + barrier design |

---

## Common Confusion Points

**FEOL and BEOL are separated by more than just order**: FEOL uses silicon-aggressive chemistries
(HF, hot H₃PO₄) and high temperatures (1000°C+). BEOL is fundamentally incompatible — Cu dissolves
in HF and melts flows start near 400°C. The temperature budget must strictly decrease after first
Cu deposition. Any FEOL anneal schedule change must account for diffusion effects on BEOL later.

**CMP is not just "grinding"**: CMP achieves sub-nanometer surface roughness on 300 mm wafers
consistently. The chemistry is critical — without H₂O₂ and BTA in copper slurry, the abrasive
alone would scratch the surface badly. The balance of chemical softening + mechanical removal
gives the combination of speed and quality.

**"Low-k" dielectrics are the weakest link mechanically**: ULK porous SiCOH (k=2.0-2.3) has
mechanical modulus ~5-10 GPa vs SiO₂'s 70 GPa. CMP shear stress can crack it. Integration
requires careful control of aspect ratio, pattern density loading, and hardmask stacks to protect
the ULK during processing.

**Interconnects now limit scaling as much as transistors**: At 2 nm, wire pitch ~20 nm means
Cu resistivity is 3-5× bulk (surface scattering). The industry is evaluating alternative metals
(Ru, Mo, W) for narrow lines where they beat Cu's size-effect degradation. The metal interconnect
problem is arguably harder than the transistor problem.
