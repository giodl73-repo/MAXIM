# Nanotechnology Applications: Nanocomposites, Coatings, Catalysis, Energy

## The Big Picture

This module surveys deployed nanotechnology applications -- where nanoscale materials
are in commercial products today, and where promising research is approaching
commercialization. Emphasis on technical mechanism, not marketing claims.

```
NANOTECHNOLOGY APPLICATION MATURITY MAP
=========================================

PRODUCTION (commodity)     COMMERCIAL (growing)      EMERGING (R&D/pilot)
==========================  ========================  ========================
Semiconductor transistors   LNP mRNA vaccines         Si nanowire batteries
Catalytic converter NP      QLED displays             CNT structural composites
Sunscreen (TiO2/ZnO NP)     Nanosilica concrete       Graphene interconnects
MEMS sensors (accelerom.)   Nano-Ag antimicrobial     DNA storage/computing
Iron oxide MRI contrast     Nanocomposite coatings    Nanopore diagnostics
                            Nanocellulose composites  Theranostic NP
                            EUV (EUV process itself)  NEMS mass sensors
                            Clay nanocomposites        Molecular electronics
                            TiO2 self-clean glass     Quantum dot solar cells

Revenue anchor:
  Semiconductor fab: $500B/yr (most of it is nano-scale)
  Nanoparticle market: ~$15B/yr (catalysts, pigments, cosmetics)
  Nanomedicine market: ~$200B/yr (includes all nanoformulations)
```

---

## Nanocomposites

### Carbon Nanotube / Epoxy Composites

```
CNT COMPOSITE MECHANICS
=========================

Why CNT in polymer:
  MWCNT Young's modulus: 200-500 GPa
  Epoxy matrix Young's modulus: 3-5 GPa
  Rule of mixtures (upper bound for aligned):
    E_composite = f * E_CNT + (1-f) * E_matrix
    At f = 0.05 (5 vol%): E ~ 0.05*350 + 0.95*4 ~ 21.3 GPa
    Compare to neat epoxy: 4 GPa -> 5x improvement

  BUT: real composites don't reach rule of mixtures
  Reasons:
    1. CNT misalignment (random orientation reduces benefit by ~5x)
    2. Poor CNT-matrix interface (slippage instead of load transfer)
    3. CNT agglomeration (bundles don't disperse as individual tubes)
    4. Length limitation (aspect ratio controls load transfer efficiency)

  Practical improvement (MWCNT/epoxy, 1-2 wt%):
    Tensile strength: +10-30%
    Fracture toughness: +20-50% (CNT bridging cracks is the mechanism)
    Electrical conductivity: +10^6 (percolation threshold at ~0.1 wt%)

BOEING 787 LIGHTNING STRIKE PROTECTION:
  Fuselage: carbon fiber reinforced polymer (CFRP) -- excellent structural properties
  PROBLEM: CFRP is electrically less conductive than aluminum
    Lightning strike: current must disperse; CFRP alone causes delamination
  SOLUTION: CNT-enhanced outer ply (copper mesh is alternative, heavier)
    MWCNT percolation network provides conductivity
    Current disperses over larger area -> less localized damage
    Weight saving vs. copper mesh: ~20-30 kg per aircraft

AEROSPACE QUALIFICATION:
  FAA/EASA: extensive coupon + component + full-scale testing required
  Certification timeline: 5-10 years for structural application
  Data requirement: full material property characterization
    including fatigue, impact, environmental (humidity, temperature cycling)
```

### Clay Nanocomposites (Nanoclay)

```
MONTMORILLONITE CLAY NANOCOMPOSITES
=====================================

Clay structure:
  Montmorillonite (MMT): 2:1 phyllosilicate
  Platelet structure: 1 nm thick, 100-500 nm lateral
  Layer spacing: 1.2 nm (natural), expandable by intercalation
  Aspect ratio: 100-1000 (high -- good for barrier properties)
  Surface: negatively charged (cation exchange capacity)

Nanocomposite fabrication:
  1. MELT BLENDING: clay + polymer + extruder
     Simplest; often doesn't fully exfoliate clay
  2. SOLUTION INTERCALATION: swell clay in solvent, mix polymer
     Better exfoliation possible
  3. IN-SITU POLYMERIZATION: monomer + clay, then polymerize
     Best exfoliation (Toyota Nylon-6/MMT 1988 -- historic first)

Morphologies:
  a. INTERCALATED: polymer chains between layers, layer spacing increased
     (better than conventional but not optimal)
  b. EXFOLIATED: layers fully separated, dispersed in polymer matrix
     (optimal -- maximum aspect ratio, maximum interface area)

PROPERTY IMPROVEMENTS (exfoliated nanocomposite):
  Barrier properties: 2-5x reduction in O2/water vapor permeability
    Tortuosity mechanism: platelets force gas molecules to travel long, tortuous path
    Critical for food packaging: extend shelf life without additional laminate layer
  Tensile modulus: 40-70% increase at 5 wt% clay
  Thermal stability: increased HDT (heat deflection temperature) +20-50 C
  Flame retardancy: intercalated MMT forms protective char layer

COMMERCIAL APPLICATIONS:
  Nylon-6/MMT (Toyota, 1993): engine timing belt cover -- historic first commercial product
  PET/clay beer bottle: extended CO2 shelf life
  Tire inner liner: reduced O2 permeability, lighter than butyl rubber
  Packaging: Nanocor, Southern Clay Products supply clay
  Flame retardant coatings for cable insulation
```

### Nanosilica in Concrete

```
NANOSILICA CONCRETE ENHANCEMENT
=================================

Mechanism:
  Silica nanoparticles (5-100 nm, amorphous SiO2): two effects:
  1. POZZOLANIC REACTION:
     SiO2 (nano) + Ca(OH)2 (portlandite from cement hydration)
     -> C-S-H (calcium silicate hydrate, the binding phase)
     Converts weak Ca(OH)2 crystals -> additional strong C-S-H
  2. FILLER EFFECT:
     NP fill inter-particle voids between cement grains
     Denser packing -> lower porosity -> lower permeability

  Comparison: microsilica (silica fume, 0.1-1 um) has same pozzolanic effect
  but nanosilica reacts faster and fills smaller voids

PROPERTY IMPROVEMENTS (0.5-3 wt% nanosilica):
  Compressive strength: +10-30%
  Early strength (1-day): significant (important for construction scheduling)
  Durability: 50% reduction in chloride ion permeability
    -> critical for marine or road salt environments (rebar corrosion)
  Alkali-silica reaction suppression (potential -- research ongoing)

APPLICATIONS:
  High-performance concrete (HPC): bridges, tunnels, high-rise
  Rapid-set concrete: faster construction, cold weather
  Shotcrete: tunnel lining (early strength critical)
  Cost: nanosilica ~$20-100/kg vs. cement ~$0.10/kg
    Usually used at 0.5-2% dosage -- cost premium 5-20% over plain concrete
    Economically justified for high-value or critical applications
```

---

## Functional Coatings

### TiO2 Self-Cleaning Surfaces

See 04-NANOMATERIALS.md for photocatalytic mechanism.

```
COMMERCIAL TiO2 COATINGS
=========================

Pilkington Activ (self-cleaning glass):
  CVD anatase TiO2, ~15 nm thickness
  Dual mechanism:
    Photocatalytic: UV light (sunlight) -> OH radicals -> degrade organics
    Superhydrophilic: UV activation -> water contact angle < 5 degrees
      (vs. normal glass: 20-40 degrees contact angle)
    Water sheets off in thin film (vs. beads) -> washes debris away
  Applications: windows, skylights, building facades, greenhouses

  Cost premium: ~20-30% over standard float glass
  Payback: reduced cleaning frequency (significant for buildings with difficult access)
  Performance limits: needs UV light (ineffective at night; indoor glass has limited effect)

ANTI-REFLECTION SiO2 COATINGS:
  Solar panels: SiO2 NP anti-reflection coating
  Mechanism: graded refractive index or porous SiO2 (n = 1.2-1.3, between glass n=1.5 and air n=1.0)
  Reflection reduced: from 4% (uncoated glass) to <1%
  Energy yield improvement: 3-4% per year
  Manufacturing: sol-gel or PECVD, roll-to-roll possible
```

### Nano-Silver Antimicrobial Coatings

```
ANTIMICROBIAL APPLICATIONS (Ag NP)
=====================================

See 04-NANOMATERIALS.md for mechanism (Ag+ release + ROS)

Applications:
  Wound dressings: Acticoat (nanocrystalline Ag, <20 nm, ~10 mg Ag/cm^2)
    Clinical evidence: reduces colonization by MRSA, P. aeruginosa
    Cochrane review: evidence moderate; best data for partial thickness burns
    Dressing change every 3-7 days vs. daily for other antiseptics -> cost offset

  Textiles: Ag NP in sportswear (Nike Dri-FIT Ag)
    Kills odor-causing bacteria (Staphylococci, Brevibacteria)
    Durability: Ag NP can leach in washing -> reduced efficacy over time
    Also: environmental concern (Ag+ toxic to aquatic organisms)

  Hospital surfaces: Ag NP coating on touch surfaces (bed rails, door handles)
    Reduces surface bacterial counts
    Limited evidence for reduction in healthcare-associated infections (HAI)
    Cost: high; coating durability in hospital cleaning environment: moderate

  Food packaging: Ag NP in polymer for food contact antimicrobial
    Regulatory issue: FDA/EU requires evaluation of migration into food
    EFSA: provisional approval for specific Ag-based materials
```

---

## Catalysis

### Heterogeneous Catalysis with Nanoparticles

```
SURFACE AREA AND CATALYTIC ACTIVITY
=====================================

Fundamental relationship:
  Reaction rate = (molecules reacted) / (time) = k_surface * (surface area) * (concentration)

  Surface area scales as 1/d (for spheres: SA/mass = 6/(rho*d))
  At d = 1 nm (Pt cluster): SA = 280 m^2/g
  At d = 10 nm:              SA = 28 m^2/g
  At d = 100 nm (fine powder): SA = 2.8 m^2/g
  Bulk Pt (mm crystal):      SA ~ 0.001 m^2/g (negligible)

  -> 1 nm Pt nanoparticles: 280,000x more surface area per gram than bulk Pt
  -> With Pt at $30,000/kg: motivation to use every atom

CATALYTIC CONVERTER (AUTOMOTIVE):
  Substrate: ceramic monolith (cordierite, 600 cells/in^2 square channels)
  Washcoat: CeO2 (ceria) + Al2O3 with ~50-100 m^2/g surface area
  Active metals: Pt, Pd, Rh nanoparticles (1-5 nm) deposited on washcoat
    Pt: CO + HC oxidation
    Pd: CO + HC oxidation, lower cost per PGM activity
    Rh: NOx reduction (critical for NO -> N2)
  Loading: 1-10 g/converter (variable; typical 1-3 g for passenger car)

  THREE-WAY CATALYST REACTIONS:
    CO + 1/2 O2 -> CO2         (oxidation)
    CxHy + O2 -> CO2 + H2O     (oxidation)
    2NO + 2CO -> N2 + 2CO2     (reduction + oxidation)

  Lambda window: efficient only at stoichiometric A/F ratio (lambda = 1.0)
  CeO2 oxygen storage: CeO2 <-> Ce2O3 buffers oxygen during transients

GOLD CATALYSIS AT NANOSCALE:
  Bulk gold: inert, does not adsorb O2 or CO at room temperature
  Au NP <5 nm: catalyzes CO oxidation at -70 C
  Mechanism debate: interface perimeter sites (Au-TiO2) vs. quantum size effects
  Applications: CO removal in hydrogen fuel cells, volatile organic compound oxidation
```

---

## Energy Applications

### Nanostructured Battery Electrodes

```
SILICON ANODE CHALLENGE AND SOLUTION
======================================

Graphite anode (current standard):
  Capacity: 372 mAh/g (6C + Li+ -> LiC6, 1 Li per 6 C atoms)
  Expansion: ~10% volume change during lithiation
  Well-understood, stable SEI, 1000+ cycles

Silicon anode:
  Capacity: 3579 mAh/g theoretical (Si + 3.75 Li -> Li15Si4)
  ~10x graphite capacity -- massive improvement if it works
  PROBLEM: 300% volume expansion during lithiation
    Expansion -> mechanical stress -> particle cracking -> SEI fracture
    Exposed fresh Si surface -> SEI re-growth -> Li consumption -> capacity fade
    After 50-100 cycles: capacity drops to <50% of initial

NANOSTRUCTURE SOLUTIONS:
  1. Si NANOWIRES (Cui, Stanford 2008):
     1D wire: can expand radially without cracking (free surface on sides)
     Demonstrated: 75% capacity retention over 700 cycles (research)
     Challenge: mass production of aligned nanowires at scale (not trivial)

  2. Si NANOPARTICLES (<150 nm critical size):
     Below critical size: fracture energy > strain energy -> particles don't crack
     Critical diameter: ~150 nm for Si (below this, stress insufficient to crack)
     Practical: 80-100 nm Si NP mixed with graphite
     Used commercially: Panasonic/Tesla NCA cells use 5-10% Si NP in graphite

  3. YOLK-SHELL NP (Cui 2012):
     Si core inside hollow carbon shell with engineered void space
     Si expands into void space during lithiation; shell stays intact
     Carbon shell: electron conductor + maintains SEI location
     Research cells: >1000 cycles with >80% capacity retention

  4. Si-GRAPHENE COMPOSITE:
     Si NP anchored on graphene sheets
     Graphene: elastic buffer, electron conductor, Li+ channel
     Multiple commercial variants: Amprius (350 Wh/kg cell), SiNode

COMMERCIAL STATE (2025):
  100% Si anode: not in production (too much expansion)
  Si/graphite blend (5-15% Si): in production (Panasonic 21700, Samsung SDI)
  Si capacity contribution: 10-20% of total cell capacity
  Next: 30-50% Si with engineered nanostructure -> 350+ Wh/kg cells
```

### Quantum Dot Solar Cells

```
QD SOLAR CELL PHYSICS
======================

Motivation: Shockley-Queisser limit (31.1% for single junction) can be exceeded

QD MECHANISMS:
  1. BANDGAP TUNING:
     QD size -> bandgap -> absorb specific wavelength
     Multi-junction: stack QDs of different sizes to capture more solar spectrum
     Unlike bulk multi-junction (requires lattice-matched epitaxy), QDs can be mixed

  2. MULTIPLE EXCITON GENERATION (MEG):
     High-energy photon (>2Eg) can create 2+ exciton-hole pairs in one QD
     Efficiency limit: ~100-135% IQE possible (>1 electron per photon)
     Demonstrated: PbSe QD, IQE >100% measured (Nozik, NREL 2004)
     Challenge: extract both electrons before they recombine (fast recombination)

  3. HOT CARRIER EXTRACTION:
     Hot carriers (before thermalization) have energy above bandgap
     QD quantum confinement slows phonon emission (phonon bottleneck)
     Slower cooling -> more time to extract at higher energy
     Theoretical limit: ~67% efficiency

CURRENT PERFORMANCE (2025):
  CdSe/CdS QD solar cell: ~16% PCE (certified)
  CsPbI3 perovskite QD: ~17-18% PCE (emerging)
  PbS QD: ~13% PCE, IR sensitivity
  QD performance vs. perovskite thin film (25%+): still below
  QD advantage: stability potential, non-toxic InP variants in development
  Challenge: ligand passivation, charge transport through QD film
```

---

## Application Maturity Summary Table

| Technology | Stage | TRL | Notes |
|------------|-------|-----|-------|
| EUV semiconductor fab | Production | 9 | $500B industry |
| Catalytic converter NP | Production | 9 | In every modern car |
| MEMS sensors | Production | 9 | Every smartphone |
| TiO2/ZnO sunscreen NP | Production | 9 | Commodity |
| LNP (mRNA vaccine) | Commercial | 8-9 | Hundreds of millions of doses |
| PEGylated liposome (Doxil) | Commercial | 9 | FDA approved since 1995 |
| QLED displays (QD film) | Commercial | 8-9 | Samsung, LG, TCL |
| Clay nanocomposites | Commercial | 8 | Packaging, automotive |
| Nanosilica concrete | Commercial | 7-8 | Growing adoption |
| Nano-Ag wound dressings | Commercial | 8 | Clinical use, evidence moderate |
| CNT/epoxy composites | Commercial | 7-8 | Aerospace lightning strike |
| CNT structural fiber | Limited commercial | 6-7 | Kuraray, others |
| Si NP in battery anode | Commercial (limited) | 7-8 | 5-15% Si/graphite blends |
| QD biomedical imaging | Research/clinical trial | 4-5 | Toxicity concerns |
| Graphene interconnects | Pilot | 5-6 | IBM 2024-2026 demos |
| CNT transistors | Prototype | 4-5 | IBM sub-1nm node (2021) |
| Si nanowire full anode | R&D | 3-4 | Not production-ready |
| DNA origami drug delivery | Research | 2-3 | Animal studies |
| Molecular electronics | Research | 2 | Reproducibility unsolved |
| Nanotube space elevator | Theoretical | 1 | No path to manufacturing |

---

## Decision Cheat Sheet

| Engineering problem | Nanotechnology solution | Maturity |
|---------------------|------------------------|----------|
| CFRP lightning strike | MWCNT conductive layer | Commercial |
| Concrete durability | Nanosilica pozzolanic additive | Commercial |
| Food shelf life (O2 barrier) | Clay nanocomposite packaging | Commercial |
| Self-cleaning building glass | TiO2 photocatalytic coating | Commercial |
| Hospital surface infection | Ag NP surface coating | Commercial (evidence limited) |
| Higher energy density batteries | Si NP in graphite anode | Limited commercial |
| Solar cell efficiency boost | QD multi-junction | Research |
| UV protection transparent | TiO2/ZnO NP in polymer | Mature |
| Catalyst activity per gram | PGM nanoparticles on high-SA support | Mature |

---

## Common Confusion Points

**"Carbon nanotubes make composite 10x stronger."** Marketing claim. Practical strength
improvements are 10-30% for well-dispersed MWCNT composites. The 10x claim assumes
aligned, well-bonded SWCNT -- not achievable at manufacturing scale with current methods.

**"Nanosilica makes concrete nano-engineered."** Nanosilica is an additive at <3%.
The concrete is still 95%+ conventional portland cement and aggregate. The nanotechnology
is real but the concrete is not a nanocomposite in a deep structural sense -- it is
conventional concrete with enhanced pozzolanic chemistry.

**"Silicon anodes are the next big battery breakthrough."** They have been "10 years away"
since about 2010. The expansion problem is fundamental and requires nanoengineering
at scale that is technically difficult and expensive. Progress is real (Tesla's 4680 cell
uses ~10% Si), but the full-silicon promise is incremental, not a step change.

**"Graphene in product X" (tennis rackets, batteries, clothing)."** Many products labeled
"graphene" contain graphite flakes or graphene oxide, not monolayer graphene. The EU
Graphene Flagship tested numerous commercial "graphene products" and found most contained
<10% few-layer graphene by mass, with the rest being multilayer graphite. Check the
Raman spectroscopy before believing marketing.
