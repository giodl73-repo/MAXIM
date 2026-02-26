# Self-Assembly: DNA Origami, Block Copolymers, Colloidal Assembly

## The Big Picture

Self-assembly is the spontaneous organization of components into ordered structures
driven by thermodynamic forces, without external direction at each step. This is
bottom-up nanofabrication at its most scalable -- trillions of components organize
simultaneously rather than sequentially.

```
SELF-ASSEMBLY HIERARCHY
========================

LEVEL 1: MOLECULAR (single nm)
  Surfactant micelles, lipid bilayers
  Self-assembled monolayers (SAM)
  Protein folding, alpha-helix, beta-sheet
  DNA double helix

LEVEL 2: SUPRAMOLECULAR (1-10 nm)
  DNA origami structures
  Protein complexes
  Block copolymer microdomains
  Host-guest inclusion complexes

LEVEL 3: MESOSCALE (10-100 nm)
  Block copolymer phase-separated domains
  Colloidal crystal arrays (photonic crystals)
  Virus-like particles
  Micelles, vesicles

LEVEL 4: MACROSCALE (> 100 nm)
  Colloidal self-assembly into opals
  Liquid crystal domains
  Block copolymer thin film patterns

DRIVING FORCES:
  Hydrophobic effect     (entropy-driven, solvation shells)
  Hydrogen bonding       (directional, specific, ~1-10 kcal/mol)
  Pi-pi stacking         (aromatic rings, ~1-3 kcal/mol)
  van der Waals          (~0.1-1 kcal/mol per interaction pair)
  Electrostatics         (long-range, shielded by salt in solution)
  Excluded volume        (entropic, hard sphere repulsion)
```

---

## Thermodynamic Driving Force

### When Is Self-Assembly Spontaneous?

```
GIBBS FREE ENERGY OF SELF-ASSEMBLY
=====================================

  delta_G = delta_H - T * delta_S

Self-assembly is spontaneous when delta_G < 0

PARADOX: Self-assembly creates order (lower entropy of assembled state)
  How can entropy drive it?

ANSWER: The TOTAL entropy includes the solvent (water)

Water entropy contribution:
  Hydrophobic surfaces force water into ordered clathrate cages around them
  This order COSTS entropy (delta_S_water < 0 when hydrophobe exposed)
  Burying hydrophobic surfaces in assembly RELEASES water molecules to bulk
  Bulk water has higher entropy than ordered cage water
  Net: delta_S_total can be POSITIVE even though delta_S_assembly is negative

This is the HYDROPHOBIC EFFECT -- the dominant driving force for most bio self-assembly

HYDROPHOBIC EFFECT NUMBERS:
  Transfer of CH2 group from water to hydrophobic phase:
    delta_H ~ 0 kcal/mol (nearly enthalpically neutral)
    delta_S ~ +3 cal/mol/K (entropy gain from water release)
    at 300K: T*delta_S ~ +0.9 kcal/mol (favorable)
  Per alkyl chain: ~1 kcal/mol per CH2 group (8-12 CH2 in surfactant)
  Micelle formation: delta_G_mic ~ -8 to -12 kcal/mol (favorable)

COMPARISON TO THERMAL ENERGY:
  kT at 300K = 0.026 eV = 0.6 kcal/mol
  One hydrogen bond: ~3-7 kcal/mol (5-12 kT)
  One base pair (DNA): ~1-2 kcal/mol (2-3 kT) -- fragile alone!
  20 base pairs of DNA duplex: ~20-40 kcal/mol (VERY stable)
  Self-assembly relies on COOPERATIVITY -- many weak interactions sum to stability
```

---

## DNA Origami

### Rothemund's Breakthrough (2006)

Paul Rothemund (Caltech) demonstrated in 2006 that a 7249-nucleotide single-stranded
scaffold DNA could be folded into arbitrary 2D shapes using short synthetic "staple" strands.

```
DNA ORIGAMI PRINCIPLE
======================

SCAFFOLD STRAND:
  M13mp18 bacteriophage genome: 7249 nt single-stranded circular DNA
  Commercially available, cheap to replicate in bacteria
  Acts as the "long backbone" of the structure

STAPLE STRANDS:
  200-250 synthetic oligonucleotides, each ~32 nt
  Each staple hybridizes to two specific non-adjacent regions of scaffold
  Forces scaffold to fold into designed shape

DESIGN PROCESS:
  Computer-aided design (caDNAno, DAEDALUS software)
  Specify 2D or 3D structure
  Software assigns scaffold routing and staple sequences
  Synthesize staples (commercial oligo synthesis, ~$10-20 per staple)

FOLDING:
  Mix scaffold + all staples in buffer (Mg2+ critical for helix stabilization)
  Heat to 65 C (denature any secondary structure)
  Cool slowly over 2-24 hours: staples progressively hybridize
  Correct fold is thermodynamically most stable state (equilibrium)

RESOLUTION: 6 nm spatial precision (limited by DNA helix pitch 3.4 nm/10 bp)

WHAT CAN BE MADE:
  2D: rectangles, triangles, smiley faces, maps, letters (~80% yield)
  3D: boxes with lids (can be opened by a "key" DNA strand)
      barrels, cylinders
      cages for drug delivery
      nanoscale breadboards for organizing proteins, NP
  Dynamic: structures that change shape when a trigger strand is added
           (strand displacement: one sequence displaced by complementary strand)
```

### DNA Origami Applications

```
DNA ORIGAMI APPLICATIONS
=========================

DRUG DELIVERY:
  DNA box (Andersen 2009): 42 nm x 36 nm x 36 nm box with lid
  Lid opens when specific DNA aptamer binds (e.g., PDGF-binding aptamer)
  Conditional release: only opens in presence of target molecule
  Research: payload drugs/proteins inside; not in clinical use yet
  Challenge: DNase in blood degrades DNA (protect with PEG, CpG methylation)

MOLECULAR RULER / TEMPLATE:
  Place gold nanoparticles at defined positions (DNA-conjugated NP)
    onto DNA origami surface (spatial resolution: 6 nm)
  Study distance-dependent FRET, plasmon coupling
  Template for organizing single molecules for single-molecule microscopy

BIOSENSING:
  DNA origami nanochannel (Plesa 2013): insert origami into lipid bilayer
  Design pore size by origami geometry
  Better-defined pore than protein nanopores

STRUCTURAL DNA NANOTECHNOLOGY (broader field):
  Holliday junction tiles (Seeman 1982): first DNA nanostructure
  DNA bricks (Ke 2012): LEGO-like modular design
  3D wireframe meshes (DAEDALUS): DNA edges define polyhedral frames
```

---

## Block Copolymers

### Phase Separation and Self-Assembly

Block copolymers are polymers with two (or more) chemically distinct blocks covalently
joined. Thermodynamic incompatibility drives them to segregate, but the covalent bond
prevents macrophase separation -- instead, they form ordered nanoscale domains.

```
BLOCK COPOLYMER PHASE DIAGRAM
==============================

Polystyrene-block-Poly(methyl methacrylate) (PS-b-PMMA) system:

f_PS = volume fraction of PS block

f_PS:    0.10   0.20   0.30   0.50   0.70   0.80   0.90
Phase:   Sphrs  Cyl    Gyr    Lamel  Gyr    Cyl    Sphrs
         (PMMA  (PMMA         (alt.         (PS    (PS
         matrix  cylind.)     lamell.)      cylind) matrix)

LAMELLAR (f_PS ~ 0.5):
  Alternating PS and PMMA lamellae
  Period (L0) = 10-50 nm (depends on molecular weight)
  PS | PMMA | PS | PMMA | PS
  ---|------|---|------|---
  Each stripe: L0/2 thick

CYLINDER (f_PS ~ 0.3 or 0.7):
  PS or PMMA cylinders in the other matrix
  Cylinder diameter: ~10-30 nm
  Hexagonally packed

SPHERE (f_PS ~ 0.1 or 0.9):
  Spheres of minority block in matrix
  BCC or FCC packing

GYROID (f_PS ~ 0.35 or 0.65):
  Bicontinuous cubic phase
  Complex interconnected 3D structure
  Useful for filtration membranes, electrode scaffolds
```

### Directed Self-Assembly (DSA) for Semiconductor Lithography

```
DIRECTED SELF-ASSEMBLY FOR LITHOGRAPHY
========================================

PROBLEM: BCP self-assembly gives the right length scale (10-50 nm)
         but the orientation and placement of domains is random

DSA SOLUTION: Pre-pattern the substrate to guide BCP assembly

GRAPHOEPITAXY:
  Shallow trenches (made by conventional lithography) guide BCP orientation
  BCP fills trench and aligns relative to trench walls
  Multiplication: 2x trench width -> 2 lamellar lines per trench (pitch doubling)

  Trench width = 4 * L0:
  |          trench         |
  |  --  --  --  --  --     |   <- 5 lines of PS (or PMMA) per trench
  +-------------------------+   <- trench walls made by 193 nm lithography
  -> sub-20 nm lines from 80 nm lithographic trench

CHEMOEPITAXY:
  Chemical pre-pattern: alternating brush layers grafted to substrate
  PS-preferring brush and PMMA-preferring brush defined by DUV lithography
  BCP assembles on pre-pattern; PS domains prefer PS brush regions
  Achieves 4x or 8x pattern multiplication

STATUS:
  IBM chemoepitaxy DSA: demonstrated 29.9 nm pitch (2013)
  Samsung DSA research: demonstrated 7.5 nm half-pitch
  Production use: still limited -- defect density too high for logic (~10^-3 defects/domain)
  Most promising near-term use: contact hole (via) optimization (rounding)
  Key advantage vs. EUV: no expensive equipment; uses existing 193i scanners
```

---

## Colloidal Self-Assembly

```
COLLOIDAL CRYSTAL FORMATION
=============================

DRIVING FORCES:
  Hard-sphere entropy: monodisperse particles at high volume fraction spontaneously
    crystallize into FCC or HCP lattice (Alder-Wainwright 1957 simulation)
    Entropic crystallization: crystal has higher translational entropy than liquid
    at phi > 0.49 (hard sphere phase transition)

  Depletion force: addition of polymer (depletant) creates entropic attraction
    Polymer exclusion from gap between particles -> osmotic pressure -> attraction
    Controls: particle clustering and crystallization kinetics

OPAL STRUCTURE:
  Silica or polystyrene microspheres (200-1000 nm) self-assemble into FCC lattice
  Gravity sedimentation or vertical deposition (substrate pulled from suspension)
  Result: 3D photonic crystal

  PHOTONIC BANDGAP:
    Periodic dielectric structure creates photonic bandgap (forbidden wavelengths)
    Analogous to electronic bandgap in semiconductors but for photons
    Opal period lambda_Bragg = 2n*d*cos(theta) (Bragg condition for each photon)
    500 nm silica spheres: forbidden wavelength ~600 nm (visible green-red)
    -> Color without dye: iridescent like butterfly wings (structural color)

INVERSE OPAL:
  Infiltrate opal template with TiO2, polymer, carbon
  Remove template by calcination or dissolution
  Interconnected 3D porous network with controlled pore size
  Applications: photocatalyst, solar cell electrode, tissue scaffold
```

---

## Biological Self-Assembly Examples

```
BIOLOGICAL SELF-ASSEMBLY (nature's proof of concept)
======================================================

VIRAL CAPSIDS:
  Tobacco mosaic virus (TMV): 300 nm x 18 nm rod
    2130 identical coat protein subunits self-assemble around RNA genome
    Each subunit: ~17 kDa, 158 aa
    Assembly: nucleation on specific RNA sequence, helical extension
    Extremely monodisperse, robust to pH/temperature variation
    Applications: template for mineralization, drug loading

  T4 phage: complex assembly with tail spike, base plate
    Several hundred proteins, 20+ different types, sequential assembly cascade
    Each sub-assembly folds independently, then assembles hierarchically

ACTIN POLYMERIZATION:
  G-actin (globular, 42 kDa) + ATP -> F-actin (filamentous, ~7 nm diameter)
  Treadmilling: polymerize at + end, depolymerize at - end
    -> directed transport without external force
  Cells use actin for: cell migration, cytokinesis, muscle contraction

PROTEIN FOLDING:
  Linear amino acid sequence folds to unique 3D structure
  Driven by: hydrophobic collapse, hydrogen bonds, disulfide bridges
  Thermodynamics: multiple weak interactions sum to > 50 kJ/mol stability
  Misfolding -> aggregation -> amyloid -> disease (Parkinson's, Alzheimer's)
  Self-assembly can go wrong: aggregation is competing kinetic trap
```

---

## Limits of Self-Assembly

```
WHAT SELF-ASSEMBLY CANNOT DO (easily)
======================================

DEFECT DENSITY:
  Self-assembly creates ordered structures, but equilibrium has defects
  DNA origami: ~80-90% correct fold (10-20% incorrect/incomplete)
  BCP for lithography: ~10^-3 defect density (IC manufacturing needs <10^-8)
  Colloidal crystals: grain boundaries, point defects, stacking faults
  Biological: protein misfolding is the failure mode

POSITIONAL PRECISION:
  Self-assembly places things "near" where you want them
  DNA origami: 6 nm position precision (limited by helix geometry)
  BCP: +/- 2-5 nm positional accuracy (useful but not nm-exact)
  Lithography: 1-2 nm overlay (much better for circuit patterning)

ERROR CORRECTION:
  Mechanical assembly: bad parts can be detected and removed
  Self-assembly: bad parts often trapped in final structure
    (kinetic trapping vs. thermodynamic equilibrium)
  DNA systems: strand displacement allows some error correction
  Biology: quality control via proteases (destroy misfolded proteins)

COMPLEX HIERARCHIES:
  Simple shapes: easy
  Complex 3D machines with moving parts: hard
    Biological cells are the only demonstrated working example
    Drexler's molecular assemblers: no demonstration after 40 years
```

---

## Decision Cheat Sheet

| Goal | Self-Assembly Method |
|------|---------------------|
| 6 nm spatial precision for NP placement | DNA origami scaffold |
| 10-30 nm period patterns over cm^2 area | Block copolymer thin film |
| Nanotube/nanostructure organization | DNA origami template |
| Photonic crystal, structural color | Colloidal self-assembly |
| Porous 3D scaffold with controlled pore size | Inverse opal template |
| Functionalize substrate surface uniformly | Self-assembled monolayer (SAM) |
| Drug carrier with conditional release | DNA origami box or liposome |
| 3D printable hydrogel scaffold | Peptide amphiphile or CNF self-assembly |

---

## Common Confusion Points

**"Self-assembly violates the second law (creates order from chaos)."** No. Entropy
increases globally -- the assembled state + released solvent molecules has higher total
entropy than the disassembled state + ordered solvent. The key is counting ALL entropy.

**"DNA origami requires custom DNA for each design."** The scaffold (M13) is reused.
Only the 200-250 staple strands are redesigned for each shape. Oligo synthesis is $0.10-0.20
per base at commercial scale. Total cost per shape design: $50-200 in oligos.

**"Block copolymers can replace EUV for chip manufacturing."** For specific applications
(contact hole rectification) they are already used. For general-purpose 2D patterning with
arbitrary circuit layout, the defect density and overlay accuracy do not yet meet IC
production standards. They are a complement to, not replacement for, optical lithography.

**"Self-assembly can build machines."** Biological cells are self-assembled machines --
the only proven example. In synthetic chemistry, self-assembled mechanical bonds
(rotaxanes, catenanes -- Sauvage/Stoddart/Feringa Nobel 2016) demonstrate nanoscale
mechanical motion. But complex, functional, programmable synthetic nanomachines remain
unsolved.
