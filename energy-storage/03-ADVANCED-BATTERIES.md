# Advanced Batteries: Solid-State, Sodium-Ion, Lithium-Sulfur, Li-Air

## The Big Picture

Beyond commercial Li-ion lies a spectrum of advanced battery chemistries. Each addresses
a specific Li-ion limitation: solid-state attacks the flammability and energy density
ceiling; sodium-ion attacks cost and material scarcity; Li-S and Li-air attack theoretical
energy density limits. All face genuine engineering challenges that explain why they are
not in production at scale despite decades of research.

```
ADVANCED BATTERY TECHNOLOGY ROADMAP
======================================

CURRENT COMMERCIAL:          NEAR-TERM (2025-2030):        LONG-TERM (2030+):
Li-ion (NMC/NCA/LFP)         Solid-state (automotive)      Li-S (practical)
  ~300 Wh/kg cell level       ~350-450 Wh/kg               ~500-600 Wh/kg
  $60-100/kWh cell             $80-120/kWh (initially)      ?
                              Na-ion (STATIONARY)
                               ~150-180 Wh/kg              Li-air (if ever)
                               $40-60/kWh                  ~3000 Wh/kg theoretical

CHALLENGE HIERARCHY:
  Solid-state: solid-solid interface resistance, manufacturing
  Na-ion: lower energy density (acceptable for grid, limiting for EV)
  Li-S: polysulfide shuttle, cycle life
  Li-air: oxygen cathode, dendrites, round-trip efficiency
```

---

## Solid-State Batteries

### Why Solid State?

```
LIQUID ELECTROLYTE PROBLEMS -> SOLID ELECTROLYTE SOLUTIONS
============================================================

PROBLEM 1: FLAMMABILITY
  Liquid electrolyte (EC/DMC): flash point 25 C, flammable
  -> Thermal runaway -> fire / explosion
  Solid electrolyte: nonflammable ceramic or sulfide -> eliminates fire risk

PROBLEM 2: ELECTROCHEMICAL STABILITY WINDOW
  Liquid: unstable vs. lithium metal anode (forms SEI, consumes Li)
  Solid (LLZO ceramic): stable vs. Li metal at 0 V
  -> Use lithium metal anode directly

PROBLEM 3: ENERGY DENSITY CEILING WITH GRAPHITE ANODE
  Graphite: 372 mAh/g
  Lithium metal: 3860 mAh/g (~10x)
  Graphite needed because liquid electrolyte + Li metal = dendrite growth + fire
  Solid electrolyte mechanically blocks dendrite propagation (in theory)
  -> Li metal anode is the prize that drives solid-state development

POTENTIAL GAINS WITH LI METAL + SOLID ELECTROLYTE:
  Cell energy density: ~500+ Wh/kg (vs. 300 Wh/kg for Li-ion)
  Temperature range: wider (solid doesn't freeze or boil)
  No liquid leakage
  Potentially longer cycle life (if interface stable)
```

### Solid Electrolyte Types

```
SOLID ELECTROLYTE COMPARISON
==============================

OXIDE CERAMICS:
  LLZO (Li7La3Zr2O12 -- "Lithium Lanthanum Zirconate"):
    Ionic conductivity: 0.3-1.0 mS/cm (bulk)
    Electrochemical window: ~0-6 V vs. Li/Li+ (excellent)
    Stability vs. Li metal: good (thin Li3N/Li2O interphase forms, stable)
    Mechanical: hard, brittle (crack during cycling or handling)
    Sinterable into dense pellets at 1000+ C
    Interface resistance: Li/LLZO interface is the key problem
      -> not intimate contact between rigid Li metal and rigid ceramic
      -> high impedance unless pressure or interlayer used
    Toyota, Solid Power, QuantumScape: LLZO development programs
    Status: pouch cell prototypes; not in production automotive cells yet

SULFIDE CERAMICS:
  LGPS (Li10GeP2S12 -- Kanno 2011):
    Ionic conductivity: ~12 mS/cm (comparable to liquid electrolyte!)
    Electrochemical window: narrow (~1.7-2.1 V vs. Li/Li+ intrinsically)
      Below 1.7 V: reduces at anode interface
      Above 2.1 V: oxidizes at cathode interface
      BUT: kinetically limited, artificial interphase forms -> effective window wider
    Moisture sensitivity: reacts with H2O to produce H2S gas (toxic!)
      Manufacturing requires extremely dry environment (<0.1 ppm H2O)
    Better ionic conductivity makes sulfide attractive despite challenges

  Li6PS5Cl (argyrodite):
    Conductivity: ~3-5 mS/cm
    Easier to synthesize than LGPS
    Samsung SDI, Solid Power: using argyrodite variants

POLYMER:
  PEO (polyethylene oxide) + Li salt (LiTFSI):
    Conductivity at 25 C: 0.01-0.1 mS/cm (too low for room-temp fast charge)
    Conductivity at 80 C: >1 mS/cm (requires elevated temperature)
    Bolloré Bluecar: PEO cell, operated at 80 C (heated battery)
    Flexible, easy to manufacture (roll-to-roll)
    No moisture sensitivity
    Disadvantage: requires heating, narrow temperature range

COMPOSITE (ceramic + polymer):
  Ceramic filler in polymer matrix
  Improved mechanical properties and conductivity vs. pure polymer
  Research area: LLZO particles in PEO, PVDF matrices
```

### Manufacturing Challenges

```
SOLID-STATE MANUFACTURING CHALLENGES
======================================

CHALLENGE 1: SOLID-SOLID INTERFACE RESISTANCE
  In liquid cell: electrolyte wets electrode surface intimately
  In solid cell: two rigid solids in contact -> limited contact area
  Contact resistance dominates at electrode-electrolyte interface
  Volume change during cycling (Si: 300%, graphite: 10%) -> interface cracks

  Solutions being explored:
    - Applied stack pressure (stack maintained under compression in housing)
    - Interlayer coating on electrode (Li3PO4, ZnO, Al2O3 ALD)
    - In-situ forming Li metal anode (deposit Li from cathode on first charge)
    - Soft sulfide electrolyte (more compliant than oxide)

CHALLENGE 2: THIN FILM DEPOSITION
  Sulfide electrolyte: best as thin film (<50 um)
  ALD, PVD, solution casting approaches
  Scale-up: roll-to-roll casting being developed (Toyota aim: 2027)

CHALLENGE 3: DENDRITE SUPPRESSION
  Solid electrolyte was supposed to block Li dendrites
  Reality: dendrites can propagate through grain boundaries in ceramic
  LLZO: dendrites enter grain boundaries under pressure, grow through ceramic
  At low stack pressure: dendrites not suppressed
  At high pressure: dendrites suppressed (>5 MPa needed per some studies)
  Design implication: solid-state pack needs pressure management hardware

TIMELINE (as of 2026):
  Toyota: solid-state EV prototype 2026, production 2027-2028 (repeatedly delayed)
  QuantumScape (VW partnership): anode-less LLZO cell, >1000 cycles demonstrated
  Samsung SDI: sulfide-based, production target 2027
  Solid Power (BMW/Ford partnership): sulfide pilot line 2024
  Most realistic estimate: volume production for premium EVs 2028-2030
```

---

## Sodium-Ion Batteries

### Why Sodium?

```
SODIUM vs. LITHIUM
===================

Na vs. Li:
  Abundance: Na = 23,600 ppm (earth crust), Li = 20 ppm -> 1000x more abundant
  Cost: NaCO3 = $0.20/kg vs. Li2CO3 = $20-80/kg (price volatile)
  E° vs. NHE: Na/Na+ = -2.71 V (vs. Li/Li+ = -3.04 V)
    -> Na cell voltage ~0.3-0.4 V lower than comparable Li cell
  Na+ ionic radius: 1.02 Angstrom (vs. Li+ 0.76 Angstrom)
    -> Na+ needs larger host lattice sites -> harder to find good materials
  Theoretical specific capacity: Na/g = 23.4 mAh/g lower than Li/g = 26.2 mAh/g
    (by mole, similar; by mass, Na is 23/7 = 3.3x heavier)

Bottom line: Na-ion will always have lower energy density than Li-ion
  BUT: at grid storage scale, $/kWh matters far more than Wh/kg
```

### Na-Ion Chemistry

```
NA-ION CATHODE AND ANODE MATERIALS
====================================

CATHODE OPTIONS:
  Prussian blue analog (PBA):
    Chemical formula: Na2MFe(CN)6 (M = Mn, Co, Ni, Fe)
    Structure: open framework (like zeolite for Na+)
    Capacity: ~120-160 mAh/g
    Advantages: simple synthesis, cheap raw materials, aqueous synthesis possible
    Disadvantages: lattice water causes degradation; structural distortions
    CATL (China): commercial PBA Na-ion cells, debut 2021

  Layered transition metal oxide:
    NaxMO2 (M = Mn, Fe, Cu, Ni, Ti combinations)
    Analogous to NMC/NCA in Li-ion
    O3 or P2 structure (different stacking of MO2 layers)
    Capacity: 100-160 mAh/g
    Challenge: more phase transitions during cycling vs. Li-ion analogs
    Advantage: no Co, can use Fe/Mn (abundant)

ANODE OPTIONS:
  Hard carbon (preferred):
    Disordered carbon (random graphene-like layers, nanopores)
    Na+ inserts into nanopores and defects (vs. intercalation in graphite)
    Na+ does NOT intercalate into crystalline graphite well
      (NaC6 is thermodynamically unstable -- key difference from Li)
    Hard carbon capacity: ~250-350 mAh/g for Na+
    Process: pyrolysis of organic precursors (cellulose, sucrose, biomass) at 1200-1600 C
    Commercially available, cost comparable to synthetic graphite

  Sodium metal: potential anode (with solid electrolyte, same issues as Li metal)

FULL CELL PERFORMANCE:
  NaPBA (CATL AB cell 2022):
    160 Wh/kg cell level
    cycle life: 2000+ cycles to 80%
    Operating temperature: -20 to 60 C (Na+ faster kinetics at low T vs. Li-ion)
    Cost: ~$40-50/kWh cell (target vs. LFP ~$55/kWh)
    No Li: no geopolitical supply chain risk for Li or Co

APPLICATIONS:
  Stationary grid storage: primary target
  Two-wheelers (e-bikes): weight less critical
  EV entry-level: China market (CATL supplying Chery, BYD exploring)
  Europe/US grid: growing interest (2025+)
```

---

## Lithium-Sulfur (Li-S) Batteries

### The Energy Density Promise

```
LI-S THEORETICAL CAPACITY
===========================

Cathode reaction (reduction):
  S8 + 16Li+ + 16e- -> 8Li2S
  (all steps: S8 -> Li2S8 -> Li2S6 -> Li2S4 -> Li2S2 -> Li2S)

Specific capacity of S: 1675 mAh/g (based on 16 electrons per S8 = 2 electrons per S)
Cell voltage: ~2.1 V (vs. Li/Li+)
Specific energy: 1675 mAh/g * 2.1 V = 2600 Wh/kg (cathode only)
vs. LiCoO2: 137 mAh/g * 3.9 V = 535 Wh/kg

Li-S theoretical: ~2600 Wh/kg cathode, ~1700 Wh/kg complete cell
Current Li-ion: ~300 Wh/kg cell
Potential improvement: ~5-6x

Li2S is INSOLUBLE; S8 is INSOLUBLE; but intermediates (Li2Sx, x>2) are SOLUBLE
```

### The Polysulfide Shuttle Problem

```
POLYSULFIDE SHUTTLE
====================

Discharge reaction sequence:
  S8 -> Li2S8 -> Li2S6 -> Li2S4 (all soluble in liquid electrolyte)
  Li2S4 -> Li2S2 -> Li2S (insoluble)

SHUTTLE MECHANISM:
  Long-chain polysulfides (Li2S8, Li2S6) dissolve and diffuse to lithium anode
  At anode: polysulfides are reduced (instead of Li+ being stripped)
    Li2S8 + 2Li -> 2Li2S4 (short-chain)
    Short-chain diffuses back to cathode: Li2S4 + 2Li+ + 2e- -> Li2S2 + Li2S
  Net: sulfur "shuttles" between electrodes, consuming lithium continuously

CONSEQUENCES:
  Self-discharge: cell loses capacity standing (shuttle continues without load)
  Columbic efficiency <100%: charge consumed by shuttle, not stored
  Lithium anode corrosion: polysulfides react with Li -> Li2S on anode
  Capacity fade: sulfur material becomes inactive (Li2S precipitates randomly)
  Typical commercial-grade Li-S (2024): ~300-400 cycles to 80% (vs. >1000 for Li-ion)

SHUTTLE MITIGATION STRATEGIES:
  1. ETHER ELECTROLYTE: polysulfides more soluble in DOL/DME (dimethoxyethane)
     Counterintuitive: MORE solubility -> better kinetics, faster discharge
     But shuttle still occurs -- fundamental tension

  2. POROUS CARBON CATHODE HOSTS: sulfur confined in micropores
     Physical confinement of sulfur and polysulfides
     High surface area carbon (>2000 m^2/g) -- MOF-derived carbons, CNT, graphene
     Practical capacity: ~800-1000 mAh/g (much less than 1675 mAh/g theoretical)

  3. SOLID-STATE ELECTROLYTE: eliminates solubility -- polysulfides can't dissolve
     Sulfide solid electrolyte (LGPS) + Li-S cathode: promising combination
     Early results: reduced shuttle, but Li2S formation kinetics slow at solid interface

  4. INTERLAYER: separator coating (e.g., Al2O3, TiO2) blocks polysulfide migration
     Some success: Coulombic efficiency improves

CURRENT BEST PERFORMANCE (2025):
  Oxis Energy (UK): ~400 Wh/kg cell, ~400 cycles (before closure 2021)
  Lyten / Sion Power: ~500 Wh/kg target, 300-500 cycles demonstrated
  Aviation application (weight-critical): HAPS (High Altitude Pseudo-Satellite) drones
    Airbus Zephyr: uses Li-S (SionPower) for stratospheric flight (weight critical)
  Consumer: not yet (cycle life insufficient)
```

---

## Lithium-Air (Li-O2) Batteries

### The Ultimate Energy Density

```
LI-AIR THEORETICAL ENERGY DENSITY
====================================

Cathode reaction: 2Li + O2 -> Li2O2  (or Li2O with 4 electrons)
  Using atmospheric oxygen as cathode reactant (not stored in battery)

Specific energy:
  Li-O2: 3460 Wh/kg (Li only, O2 from air)
  Gasoline: 13,000 Wh/kg (includes O2 for combustion)
  Li-ion NMC: ~300 Wh/kg (complete cell)

If achievable: battery energy density approaching gasoline (before 4x ICE efficiency advantage)

FUNDAMENTAL REACTIONS:
  Discharge: 2Li -> 2Li+ + 2e- (anode)
             O2 + 2Li+ + 2e- -> Li2O2 (cathode, E° = 2.96 V vs. Li/Li+)
  Charge:    Li2O2 -> 2Li+ + O2 + 2e- (should be reversible)

  But: overpotential during charge is large (>1 V above discharge)
    Discharge: ~2.6-2.8 V; Charge: ~4.0-4.2 V
    Round-trip efficiency: ~65-70% (poor vs. Li-ion 90-95%)
```

### Why Li-Air Is Not Commercial

```
LI-AIR CHALLENGES (each alone would be disqualifying)
=======================================================

1. SOLID PRODUCT BLOCKING:
   Li2O2 (solid, insoluble) forms and clogs cathode pores
   As cathode fills with Li2O2: resistance rises, capacity lost
   Cathode must be redesigned for each charge cycle

2. CARBON CATHODE INSTABILITY:
   Standard approach: porous carbon air electrode
   Problem: LiO2 (intermediate) reacts with carbon: LiO2 + C -> Li2CO3
   Li2CO3 is electrochemically irreversible -> capacity fade per cycle
   Alternative: metal (Au, Ru) electrode -- expensive; TiC, MnO2 -- research

3. LITHIUM METAL ANODE:
   Same dendrite/safety issues as solid-state Li
   Especially severe with liquid electrolyte

4. ELECTROLYTE DECOMPOSITION:
   O2 radicals (superoxide) are highly reactive
   Organic electrolytes react with O2-: DMF, DMSO, ionic liquids
   Finding stable electrolyte: major unsolved research challenge
   Contenders: DMSO (partially stable), ionic liquids (expensive), solid-state

5. CO2 AND H2O POISONING:
   Real air contains CO2 and H2O
   CO2 reacts: Li2O2 + CO2 -> Li2CO3 (irreversible)
   H2O reacts: Li2O2 + H2O -> LiOH (partially reversible)
   Requires: dry, CO2-free air supply -> needs air scrubbing system (adds weight/cost)

STATUS: Best lab Li-O2 cells achieve ~50-100 cycles. Not close to practical.
Cambridge (Clare Grey group), MIT (Yang Shao-Horn) are prominent research centers.
The challenges are fundamental chemistry, not just engineering.
```

---

## Advanced Battery Comparison

| Technology | Energy Density | Cycle Life | Key Challenge | Timeline |
|------------|---------------|------------|---------------|----------|
| Li-ion (NMC811) | 300 Wh/kg | 1000-2000 | Cost, Ni supply | NOW |
| Li-ion (LFP) | 200 Wh/kg | 3000-6000 | Lower energy | NOW |
| Solid-state (oxide) | 400-500 Wh/kg | >1000 (target) | Interface resistance | 2028-2030 |
| Solid-state (sulfide) | 400-500 Wh/kg | >1000 (target) | H2O sensitivity, manufacturing | 2027-2029 |
| Na-ion (PBA) | 150-170 Wh/kg | 2000+ | Energy density | NOW (China) |
| Na-ion (layered oxide) | 170-200 Wh/kg | 1500+ | Phase stability | 2025-2027 |
| Li-S | 350-500 Wh/kg | 300-500 | Shuttle, cycle life | 2025+ niche |
| Li-air | 1000+ Wh/kg possible | <100 | Multiple fundamental | 2040+ if ever |

---

## Decision Cheat Sheet

| You need... | Technology |
|-------------|-----------|
| Highest energy density NOW | NMC811 / NCA (commercial Li-ion) |
| Cheaper, abundant materials, grid storage | Na-ion (PBA or layered oxide) |
| Non-flammable battery for EVs | Solid-state (2028+ realistic) |
| 5x energy density (theoretical) | Li-S (but cycle life limited) |
| Weight-critical aerospace | Li-S (HAPS drones) |
| Research, understand fundamentals | Li-air (purely scientific now) |

---

## Common Confusion Points

**"Solid-state batteries are 5 years away" (since 2010)** The joke is real. Toyota alone
has announced solid-state EV timelines that shifted right by 2-3 years at least four times.
The interface resistance and dendrite problems are harder than initially thought. The 2028-2030
timeline for limited volume production is now more realistic -- but it has been said before.

**"Sodium-ion is just a cheaper Li-ion."** Not quite -- Na+ is larger (harder to intercalate),
Na/Na+ potential is 0.3V less negative than Li/Li+ (lower cell voltage), and graphite anodes
don't work for Na+. Different materials are needed. The system is not a drop-in substitute.

**"Li-S can replace Li-ion in 5 years."** The polysulfide shuttle is a fundamental
electrochemistry problem. The best commercial Li-S cells (Sion Power) achieve ~300-500
cycle life -- inadequate for most applications. Aviation (weight-critical, limited cycles)
is the bridgehead market, not consumer electronics or EVs.
