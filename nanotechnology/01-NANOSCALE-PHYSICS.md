# Nanoscale Physics: Quantum Confinement, Surface-to-Volume, van der Waals

## The Big Picture

Below ~100 nm, three physical regimes shift simultaneously. Classical mechanics yields to
quantum mechanics for electrons. Bulk thermodynamics yields to surface thermodynamics for
atoms. Gravity and viscous drag yield to van der Waals forces for particles.

```
PHYSICAL REGIMES AT THE NANOSCALE
===================================

PHENOMENON          MACRO (>1 um)     NANO (1-100 nm)    ATOMIC (<1 nm)
------------------  ----------------  -----------------  ----------------
Electron behavior   Fermi sea, bands  Confined levels    Orbitals, bonds
Optical properties  Bulk bandgap      Size-tunable gap   Atomic transitions
Melting point       Fixed (bulk)      Depressed by size  Not applicable
Dominant force      Gravity, inertia  van der Waals      Chemical bonds
Thermal fluctuation kT negligible     kT comparable to   kT > bond energy
                                      quantum gaps       (chemistry)
Mechanical behavior Continuum         Dislocation-free   Molecular dynamics
                                      crystal possible

KEY TRANSITIONS:
  100 nm: van der Waals forces become significant
   50 nm: Phonon mean free path effects on thermal conductivity
   10 nm: Quantum confinement becomes significant for semiconductors
    5 nm: Surface atoms are majority; melting point depression large
    2 nm: Quantum dot emission tunable across visible spectrum
```

---

## Quantum Confinement

### Particle-in-a-Box: The Fundamental Model

When an electron is confined to a box of size L (one dimension), its energy levels become
discrete:

```
PARTICLE-IN-A-BOX ENERGY LEVELS
=================================

       E_n = n^2 * h^2 / (8 * m * L^2)

where:
  n = quantum number (1, 2, 3, ...)
  h = Planck constant (6.626e-34 J*s)
  m = electron mass (9.109e-31 kg)
  L = box size (confinement dimension)

Energy level spacing: delta_E = E_(n+1) - E_n = (2n+1) * h^2 / (8mL^2)

At L = 10 nm (quantum dot size):
  E_1 = (1)^2 * (6.626e-34)^2 / (8 * 9.109e-31 * (10e-9)^2)
      = 6.0e-21 J = 0.038 eV

At L = 5 nm:
  E_1 = 0.15 eV  (4x larger -- inverse square scaling)

At L = 2 nm:
  E_1 = 0.94 eV  (25x larger -- visible photon energy)
```

**Key insight**: Confine an electron in smaller box → higher ground state energy →
larger effective band gap → shorter emission wavelength (blue shift).

### Quantum Confinement in 1D, 2D, 3D

```
CONFINEMENT GEOMETRY
=====================

Bulk semiconductor:     No confinement, continuous DOS, 3D electron gas
                        DOS(E) ~ sqrt(E)

Quantum well (2D):      Confined in z, free in x,y
                        Layered epitaxy (GaAs/AlGaAs)
                        DOS(E) = step function (constant per subband)
                        Used in: laser diodes, LEDs, HEMTs

Quantum wire (1D):      Confined in y,z, free in x
                        CNT is the prototype
                        DOS(E) ~ 1/sqrt(E) -- van Hove singularities
                        Ballistic transport possible

Quantum dot (0D):       Confined in all 3 dimensions
                        Discrete atomic-like energy levels
                        DOS(E) = delta functions
                        Used in: QLED displays, bioimaging, solar cells
```

### Quantum Dot Emission Wavelength → Bandgap → Size Relationship

For CdSe quantum dots (most studied system):

```
CdSe QUANTUM DOT: SIZE → BANDGAP → EMISSION
=============================================

The effective bandgap (Eg_eff) is the bulk bandgap plus confinement energy:

  Eg_eff = Eg_bulk + E_confinement

Brus equation (simplified):
  Eg_eff = Eg_bulk + (h^2 / 8R^2) * (1/m_e* + 1/m_h*) - 1.8e^2 / (4*pi*epsilon*epsilon_0*R)

where R = nanocrystal radius, m_e*/m_h* = effective masses, epsilon = dielectric constant

PRACTICAL RESULT FOR CdSe:

  Diameter    Eg_eff    Emission    Color
  --------    ------    --------    -----
  2.0 nm      2.8 eV    ~460 nm     Blue
  2.5 nm      2.5 eV    ~500 nm     Green-blue
  3.0 nm      2.2 eV    ~550 nm     Green
  4.0 nm      1.9 eV    ~620 nm     Orange
  5.0 nm      1.8 eV    ~660 nm     Red
  7.0 nm      1.7 eV    ~710 nm     Near-IR

CdSe bulk Eg = 1.74 eV (715 nm, near-IR)
Confinement blue-shifts emission: SMALLER dot = BLUER light
This is directly tunable via synthesis temperature and time.
```

---

## Surface-to-Volume Ratio

### The Core Scaling Law

For a sphere of diameter d:
```
  Surface area = pi * d^2
  Volume       = pi * d^3 / 6
  SA/V         = 6 / d

  d = 1 cm  -> SA/V = 600 m^-1     (bulk material, surface negligible)
  d = 1 um  -> SA/V = 6e6 m^-1     (microparticle, surface matters)
  d = 100 nm -> SA/V = 6e7 m^-1    (nanoparticle, surface dominates)
  d = 10 nm  -> SA/V = 6e8 m^-1    (quantum dot, mostly surface atoms)
  d = 1 nm   -> SA/V = 6e9 m^-1    (cluster, ~every atom is surface)
```

At 3 nm diameter, roughly 50% of atoms are surface atoms.
At 1 nm, essentially all atoms are at or near the surface.

### Consequences of High SA/V

**1. Melting Point Depression (Gibbs-Thomson Effect)**

Nanoparticles melt at lower temperature than bulk because surface atoms have fewer
bonds and surface tension dominates:

```
  T_melt(R) = T_melt(bulk) * [1 - (2 * gamma * V_m) / (R * L_f)]

where:
  gamma = surface energy (J/m^2)
  V_m   = molar volume
  R     = particle radius
  L_f   = latent heat of fusion

Gold:
  Bulk T_melt = 1064 C
  At R = 5 nm: T_melt ~ 700 C
  At R = 2 nm: T_melt ~ 300 C

Application: nanoparticle silver inks can be sintered at 150 C
  (vs 960 C for bulk silver) -- critical for printed electronics on plastic.
```

**2. Catalytic Reactivity**

Reaction rate per gram scales as SA/V. But more than that -- nanoparticle catalysts
expose crystallographic faces (corners, edges, terraces) at high density.
Gold nanoparticles <5 nm catalyze CO oxidation at room temperature;
bulk gold is inert. Same element, different physics.

**3. Optical Properties Change (see plasmonics below)**

**4. Mechanical Properties**

Nanoparticles and nanowires can approach theoretical strength (E/10 to E/100)
because at <100 nm, dislocation-free crystals are possible. Dislocations are
the normal mechanism of plastic deformation -- eliminate them and material
approaches the bond-strength limit.

---

## van der Waals Forces at the Nanoscale

### Pairwise Interaction and Hamaker Constant

Between two atoms, the London dispersion force (a component of van der Waals):
```
  F(r) = -d/dr [C_6 / r^6] = 6*C_6 / r^7   (attractive)
```

But for extended bodies, pairwise summation gives the Hamaker approach:

```
VAN DER WAALS BETWEEN MACROSCOPIC BODIES
==========================================

Two spheres of radius R separated by distance D (D << R):
  F = -A * R / (6 * D^2)

Two flat plates (area A, separation D):
  F/A = -A_H / (6 * pi * D^3)

Sphere near flat surface:
  F = -A_H * R / (6 * D^2)

where A_H = Hamaker constant (material-dependent, ~10e-20 to 10e-19 J for
common materials in vacuum)

AT D = 10 nm:
  Force on a 100 nm sphere near a surface ~ 0.1 to 10 nN
  This is enormous compared to the weight of the sphere (~10^-18 N for Au nanoparticle)
  van der Waals >> gravity by 6-7 orders of magnitude
```

### Gecko Adhesion: Engineering van der Waals

Gecko foot has hierarchical structure: lamellae -> setae (2 um) -> spatulae (200 nm).
Spatulae make van der Waals contact with any surface. Total contact area:
~1 billion spatulae per gecko. No chemistry, no glue -- pure van der Waals.

```
GECKO ADHESION NUMBERS:
  Spatula: 200 nm wide, makes van der Waals contact
  Each spatula: ~10 nN adhesion force
  1 billion spatulae per gecko (~100 g)
  Total adhesion: ~10 N (2 lbs) -- holds a 100g gecko

  Shear strength of van der Waals contact at 10 nm separation:
    F ~ A_H * R / (6 * D^2) -- sufficient for reversible dry adhesion

Synthetic gecko tape (Carbon Research Lab, DARPA Geckskin):
  Aligned CNT arrays replicating spatula geometry at scale
  100 N/cm^2 shear adhesion demonstrated (2008, Dastoor et al.)
```

### Casimir Effect

When two uncharged conducting plates are very close (<1 um), quantum vacuum fluctuations
create an attractive force:

```
CASIMIR FORCE BETWEEN PARALLEL PLATES:
  F/A = (pi^2 * hbar * c) / (240 * D^4)

  D = 100 nm: F/A ~ 0.1 Pa (small but measurable)
  D = 10 nm:  F/A ~ 10^4 Pa (significant engineering challenge)

  For MEMS/NEMS: Casimir force causes "stiction" -- when two surfaces get
  within ~10 nm they attract and stick permanently. Major fabrication challenge.
  Solution: surface roughening, hydrophobic coatings, supercritical CO2 drying.
```

---

## Nanoscale Thermal Transport

### Phonon Mean Free Path

Heat in crystalline solids travels by phonons (quantized lattice vibrations).
Mean free path lambda of phonons in silicon at 300K is ~300 nm.

```
THERMAL CONDUCTIVITY MODIFICATION AT NANOSCALE
================================================

When characteristic dimension L < lambda (phonon MFP):
  Thermal conductivity is REDUCED (more boundary scattering)
  k_eff ~ k_bulk * lambda_eff / lambda_bulk

Silicon:
  k_bulk = 150 W/m/K (bulk)
  k at 50 nm wire ~ 20-30 W/m/K (boundary scattering dominant)
  k at 10 nm wire ~ 5 W/m/K

Applications:
  THERMOELECTRICS: Want low thermal conductivity + high electrical conductivity
    (ZT = S^2*sigma*T/kappa). Nanostructuring reduces kappa without killing sigma.
    PbTe quantum dots in PbSe: ZT ~ 2.2 (vs 0.8 bulk)

  TRANSISTORS: 5nm MOSFET has thin SOI layer -- thermal spreading to substrate
    is phonon-bottlenecked. Self-heating is a major challenge below 10nm node.
    Heat flux: 100 W/mm^2 in CPU hot spots.
```

---

## Size-Dependent Optical Properties: Plasmon Resonance

### Localized Surface Plasmon Resonance (LSPR)

In metal nanoparticles (gold, silver), conduction electrons oscillate collectively
in resonance with incident light:

```
GOLD NANOPARTICLE PLASMONICS
==============================

Bulk gold: appears gold/yellow (interband absorption ~2.3 eV)

Gold nanoparticle:
  Conduction electrons form plasma
  External EM field drives collective oscillation
  Resonance condition (dipole mode, Mie theory, quasistatic approx):
    epsilon_1(omega) = -2 * epsilon_medium   (Frohlich condition)

For gold in water:
  ~20 nm sphere: LSPR ~ 520 nm (green absorbed -> red/purple transmitted)
  ~100 nm sphere: LSPR ~ 570 nm (red shift with size)
  Gold nanorods: LSPR 600-900 nm (tunable by aspect ratio)
  Gold nanocages/shells: LSPR into NIR (tissue transparent window)

Gold nanoparticle colors:
  2 nm: bulk-like, slightly brown
  5 nm: orange-red
  20 nm: red (wine red -- classic colloidal gold, used in pregnancy tests)
  80 nm: blue-purple
  200 nm: dark blue

Wavelength red-shifts with increasing size; shape controls it further.

LSPR field enhancement near particle surface: |E|^2 / |E_0|^2 ~ 10^2 to 10^4
Used in: Surface-Enhanced Raman Spectroscopy (SERS), single-molecule detection,
         solar cell enhancement, photothermal therapy
```

---

## Summary: Physical Laws at the Nanoscale

```
NANOTECHNOLOGY PHYSICS CHEAT SHEET
=====================================

QUANTUM CONFINEMENT:
  Energy levels: E_n = n^2 * h^2 / (8mL^2)
  Smaller box -> higher energy -> larger bandgap -> shorter wavelength
  CdSe: 2 nm = blue, 5 nm = red

SURFACE-TO-VOLUME:
  SA/V = 6/d for sphere
  At d < 10 nm: surface atoms dominate thermodynamics
  Melting point drops, reactivity rises, strength rises

VAN DER WAALS:
  Atom-atom: F ~ 1/r^7
  Body-body: F ~ A_H * R / D^2 (sphere-flat)
  Dominates gravity at <100 nm by 6+ orders of magnitude
  Enables gecko adhesion, causes MEMS stiction

CASIMIR EFFECT:
  F/A ~ hbar*c / D^4
  Attractive; stiction risk at <10 nm separation in NEMS

THERMAL:
  Phonon MFP in Si ~ 300 nm
  Below MFP: k_eff << k_bulk (boundary scattering)
  Used in thermoelectrics; challenge in transistor heat dissipation

PLASMONICS:
  Collective electron oscillation in metal NP
  LSPR wavelength tunable by size, shape, material
  Au: 520-900 nm (sphere to rod); field enhancement 100-10000x
```

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| Why does a 3nm CdSe QD emit blue and a 6nm emit red? | Quantum confinement: smaller L = larger E_n = larger Eg = shorter wavelength |
| Why do gold nanoparticles appear red? | LSPR at 520 nm absorbs green, transmits red |
| Why do nanoparticles melt at lower T? | Surface atoms have fewer bonds; surface energy term dominates |
| Why do nanoparticles stick to surfaces? | van der Waals >> gravity below 100 nm |
| Why does Si have low k at 10nm? | Phonon mean free path (300 nm) >> dimension: boundary scattering |
| What makes NEMS stick together? | Casimir force at <10 nm separation |
| What's the most important confinement geometry for displays? | 0D quantum dot (discrete levels, tunable emission) |
| What's the most important confinement geometry for transistors? | 2D quantum well or nanowire (FinFET = 2D, GAA = 1D) |

---

## Common Confusion Points

**"Quantum effects only matter for quantum computers."** Wrong. Quantum confinement is
already in your TV (QLED uses quantum dot emission), your phone (FinFET transistors
use quantum tunneling gate current), and your MRI (iron oxide nanoparticle contrast agents).

**"Smaller nanoparticle = more properties change."** True, but not linearly. There are
characteristic length scales (de Broglie wavelength, phonon MFP, LSPR resonance
condition) where specific transitions happen.

**"van der Waals forces are weak."** Between two atoms, yes. Between two surfaces at
10 nm separation, no -- they dominate every other force and are the primary engineering
challenge in MEMS/NEMS device stiction.

**"The Casimir force is exotic/irrelevant."** It is measurable and has been confirmed to
high precision. In NEMS (sub-100 nm gaps), it is an engineering consideration, not a
curiosity.

**"Thermal conductivity always increases with purity/crystallinity."** True in bulk.
At nanoscale, geometry (thin film, nanowire, quantum well) introduces boundary scattering
that dominates even in perfect crystals.
