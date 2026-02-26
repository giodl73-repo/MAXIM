# Carbon Nanostructures: Fullerenes, Nanotubes, Graphene

## The Big Picture

Carbon forms multiple nanoscale allotropes with radically different properties.
All are built from sp2-hybridized carbon (graphene-like bonding) but differ in
topology: flat, cylindrical, spherical. The electronics, mechanics, and chemistry
derive from the same benzene-ring C-C bonding network in different geometries.

```
CARBON NANOSTRUCTURE FAMILY TREE
==================================

           sp3 (tetrahedral)          sp2 (planar, delocalized pi)
           ----------------          ----------------------------
           Diamond (3D)               Graphite (bulk)
                                             |
                              +--------------+--------------+
                              |              |              |
                         Graphene (2D)   Nanotube (1D)  Fullerene (0D)
                              |              |              |
                         Single layer   SWCNT / MWCNT     C60 (C70, C84...)
                         Bilayer        Armchair            Endohedral
                         Multilayer     Zigzag              fullerenes
                                        Chiral
                              |              |              |
                    Derivatives:        Applications:     Applications:
                    Graphene oxide       Electronics       Superconductors
                    Reduced GO           Composites        Lubricants
                    Fluorographene       Sensors           Photovoltaics
                    Graphane             Filters
```

---

## C60 Buckminsterfullerene

### Structure and Discovery

```
C60 STRUCTURE
==============

Icosahedral symmetry (Ih point group):
  60 carbon atoms at vertices of a truncated icosahedron
  20 hexagonal faces
  12 pentagonal faces
  Each C: bonded to 2 six-membered rings + 1 five-membered ring
  Two bond lengths:
    C-C at pentagon/hexagon junction: 1.45 angstrom (single-bond-like)
    C-C at hexagon/hexagon junction: 1.40 angstrom (double-bond-like)
  Diameter: 0.7 nm (van der Waals: 1.0 nm)
  Pi electrons: 60 (delocalized over cage)

Like a soccer ball: 20 white hexagons + 12 black pentagons

DISCOVERY (1985):
  Curl, Kroto, Smalley (Rice/Sussex)
  Mass spectrometry of carbon vapor (graphite laser vaporization)
  Anomalously stable cluster at m/z = 720 (60 x 12 = 720)
  Proposed truncated icosahedron structure
  Nobel Prize in Chemistry 1996

SYNTHESIS (Kratschmer-Huffman, 1990):
  AC arc discharge between graphite rods in He atmosphere
  Soot contains ~10-15% C60 + ~5% C70 + traces of larger fullerenes
  Extraction: dissolve in toluene (C60 is surprisingly soluble: 2.8 mg/mL)
  Purification: column chromatography or HPLC
  Production: tons per year; cost ~$20-100/gram
```

### C60 Chemistry and Applications

```
C60 REACTIVITY:
  Acts as electron acceptor (can accept up to 6 electrons reversibly)
  E_red (C60/C60-): -0.98 V vs. SCE
  Forms adducts: Diels-Alder, [2+2], nucleophilic addition to C=C

Endohedral fullerenes (X@C60):
  Atom or ion trapped inside cage
  N@C60: trapped N atom -- quantum computing qubit candidate
  La@C60, Sc3N@C80: metallofullerenes -- MRI contrast agents (narrow emission)
  Radioactive 177Lu@C60: radiotherapy research

APPLICATIONS:
  Lubricant additive: C60 "molecular ball bearings" in polymer matrices
  Organic photovoltaics: PCBM (phenyl-C61-butyric acid methyl ester)
    n-type acceptor in bulk heterojunction OPV cells (P3HT:PCBM was the standard 2005-2015)
    Now largely replaced by non-fullerene acceptors (NFA) with better performance
  Superconductors: K3C60 (alkali-doped) Tc = 18 K, Cs3C60: 38 K (highest molecular SC)
  Antioxidant: C60 in squalene -- traps free radicals (many active electrons)
    Published lifespan extension in rats (Baati 2012) -- not reproducible in all studies
  Drug delivery: functionalized C60 + drug conjugates (research)
```

---

## Carbon Nanotubes (CNT)

### Structure: Chirality Vector

```
NANOTUBE CHIRALITY AND ELECTRONIC TYPE
========================================

A SWCNT is a rolled sheet of graphene.
The roll direction defines the chirality vector (n,m):

Graphene lattice:
  a1, a2 = lattice vectors
  Chirality vector C_h = n*a1 + m*a2

Special cases:
  (n,0): zigzag nanotube (tube axis perpendicular to C-C bonds)
  (n,n): armchair nanotube (C-C bonds at 30 degrees to tube axis)
  (n,m): chiral nanotube (all other cases)

METALLIC vs. SEMICONDUCTING:
  Rule: if (n-m) mod 3 == 0, the tube is metallic; otherwise semiconducting

  Armchair (n,n): ALWAYS metallic (ballistic conductors)
    (5,5): metallic, 0.68 nm diameter
    (10,10): metallic, 1.36 nm diameter

  Other:
    (6,4): (6-4=2, 2 mod 3 = 2 != 0) -> semiconducting
    (9,0): (9-0=9, 9 mod 3 = 0) -> metallic
    (10,0): (10-0=10, 10 mod 3 = 1) -> semiconducting

Diameter formula: d = (a / pi) * sqrt(n^2 + nm + m^2)
  where a = 0.246 nm (graphene lattice constant)

In random synthesis: ~1/3 metallic, ~2/3 semiconducting (approximately)
Separation of metallic from semiconducting: gel chromatography, density gradient,
  DNA wrapping, dielectrophoresis -- none yet at manufacturing scale cost
```

### SWCNT Properties

```
SINGLE-WALL CNT PROPERTIES
============================

Property            Value              Notes
-------------------  -----------------  --------------------------------
Diameter            0.7 - 2.0 nm       Most common 1-1.5 nm
Length              1 um - cm          Synthesis and handling dependent
Young's modulus     ~1 TPa             World-record stiffness (axial)
Tensile strength    ~100 GPa           In IDEAL tubes; real ~10-50 GPa
                                       (defects, ends limit real strength)
Electrical          Metallic: ~10^6 S/cm  Exceeds copper resistivity
conductivity        (armchair)            (in defect-free short tubes)
Current capacity    ~10^9 A/cm^2       100x higher than copper
Thermal conduct.    ~3500 W/m/K        Higher than diamond in axial direction
(axial)             (single tube)      Radial: much lower
Bandgap (semi.)     ~0.5-1.5 eV        Tunable by diameter
  vs. diameter      Eg ~ 0.9 eV/d(nm)
```

### MWCNT and Synthesis

```
MULTIWALL CNT (MWCNT)
=======================

Concentric SWCNT, typically 5-50 walls, ~5-30 nm outer diameter
Inter-wall spacing: 0.34 nm (same as graphite interlayer)
Electronic properties: always metallic (outermost shell dominates)
Mechanical: E ~ 0.3-1 TPa (lower than SWCNT due to defects between walls)

SYNTHESIS METHODS:
  Arc discharge:
    Graphite electrodes in He/Ar atmosphere
    DC current -> plasma -> vaporization -> nanotube formation
    High quality but small quantity, hard to scale
    SWCNT: requires metal catalyst (Fe, Co, Ni) in anode
    MWCNT: no catalyst needed

  Laser ablation:
    Pulsed laser on graphite target with Co/Ni catalyst
    High quality SWCNT
    Low throughput, expensive laser

  CVD (commercial production method):
    CH4 or C2H2 + H2 over Fe/Co/Ni nanoparticle catalyst at 700-900 C
    Scalable: kilograms/day production (commercial)
    MWCNT: high yield, relatively cheap ($5-50/g)
    SWCNT: possible but chirality-uncontrolled mixture

CURRENT CNT LIMITATIONS IN APPLICATIONS:
  Chirality control: synthesis gives mixture of all (n,m) types
    -> mixture of metallic/semiconducting -- bad for transistors
  Alignment: random orientation in composites limits mechanical benefit
  Dispersion: CNTs bundle (van der Waals attraction) -- hard to separate
    Surfactants, polymers, functionalization help but add mass, reduce properties
  Long-range contamination: metal catalyst residue (Fe, Ni) -- health concern
    Especially for in-vivo biomedical applications
```

---

## Graphene

### Band Structure and Unique Physics

```
GRAPHENE BAND STRUCTURE
========================

Graphene = single atomic layer of sp2 carbon, hexagonal lattice

Two sublattices (A and B):
  Two atoms per unit cell
  Tight-binding calculation gives:
  E(k) = +/- t * |sum of e^(ik.delta)|
  where t = 2.7 eV (hopping parameter), delta = nearest-neighbor vectors

DIRAC CONE:
  At K and K' points of Brillouin zone, conduction and valence bands TOUCH
  (zero bandgap -- semimetal)
  Near K points:
    E = +/- hbar * v_F * |k|
  where v_F ~ 10^6 m/s (Fermi velocity, 1/300 of speed of light)

  This is the Dirac equation for massless fermions!
  Electrons in graphene behave as MASSLESS DIRAC FERMIONS
  (relativistic quantum mechanics in a 2D carbon sheet)

Consequences:
  Extremely high carrier mobility at room temperature: 200,000 cm^2/V/s
    (vs. 1,400 cm^2/V/s in silicon, 8,500 in GaAs)
  Quantum Hall effect at room temperature (anomalous QHE)
    Hall conductance: sigma_xy = 4e^2/h * (N + 1/2), N integer
    The extra 1/2 (Berry phase pi) is a signature of Dirac fermions
  Klein tunneling: Dirac fermions pass through potential barriers (no backscattering)
    -> suppresses Anderson localization
  Half-integer QHE: 1/2 shift from Berry phase
```

### Graphene Discovery: Geim and Novoselov

```
SCOTCH TAPE METHOD (2004):
  Graphite (HOPG) + Scotch tape -> peel layers -> thinner and thinner
  Transfer to SiO2/Si substrate
  Look under optical microscope: monolayer visible due to thin-film interference
  AFM: confirm ~0.34 nm step height
  Characterized: field effect transistor, Hall effect, QHE

  Nobel Prize in Physics 2010: Geim and Novoselov (Manchester)

  Why SiO2 on Si?
    280 nm SiO2 on Si creates specific optical path length
    Monolayer graphene produces 2.3% contrast in white light
    Color: faint blue-grey (just visible)
    At other SiO2 thicknesses (90 nm, 200 nm): contrast too low to see
    This serendipitous choice enabled the discovery
```

### Graphene Properties

```
GRAPHENE PROPERTIES TABLE
===========================

Property                    Value                Notes
--------------------------  -------------------  -----------------------
Thickness                   0.335 nm (1 atom)    Thinnest possible material
Young's modulus (in-plane)  ~1 TPa               Strongest per thickness
Tensile strength            ~130 GPa             Theoretical limit
Carrier mobility            ~200,000 cm^2/V/s    Suspended, low T
                            ~10,000-15,000        On substrate, RT
Optical opacity             2.3% per layer        pi*alpha where alpha = fine structure const
Thermal conductivity        3500-5300 W/m/K      Suspended monolayer
  (in-plane)
Electrical sheet resistance ~31 Ohm/sq (undoped) Metallic
Bandgap                     0 eV                 Semimetal (limits transistor use)
```

### Why Graphene Is NOT (yet) in Transistors

```
THE GRAPHENE TRANSISTOR PROBLEM
=================================

A transistor needs an ON/OFF ratio of >10^4 for digital logic.
Graphene has zero bandgap -> cannot be fully turned off.
Leakage current remains large even at Vg = 0.

On/off ratio for graphene FET: ~2-20 (useless for logic)
Compare: Si MOSFET: 10^6 to 10^8

SOLUTIONS TRIED:
  1. Bilayer graphene + perpendicular field: opens ~50 meV gap
     -> on/off ~10^3 at low T; room T: 10^2 (still too low)

  2. Graphene nanoribbons (GNR): lateral confinement opens bandgap
     Eg ~ 0.2-2 eV for width 1-10 nm
     On/off > 10^6 demonstrated for 2 nm GNR
     Challenge: edge roughness kills mobility; making 1-2 nm GNR precisely is hard

  3. Bilayer graphene + alignment + twist angle: moire superlattice
     "Magic angle" (1.1 degrees) -> correlated insulating state
     Interesting physics, not for transistors

CURRENT STATUS:
  Graphene RF transistors: cutoff frequency >300 GHz (no off state needed for RF)
  Graphene THz detectors: photodetector, not transistor
  Graphene electrodes: transparent conductor (but ITO is cheaper and works fine)
  Graphene as copper interconnect replacement: major semiconductor fab interest
    (IBM, GlobalFoundries working on graphene 2024-2026)
    Graphene has lower resistivity at narrow widths than Cu (no surface scattering)
```

### Graphene Derivatives

```
GRAPHENE DERIVATIVES
=====================

Graphene oxide (GO):
  Graphene with -OH, -COOH, epoxide groups on basal plane and edges
  Made by: Hummers method (graphite + H2SO4 + KMnO4 + NaNO3)
  Properties: electrically insulating (disrupted pi conjugation)
              strongly hydrophilic (disperses in water, unlike graphene)
  Bandgap: 2-3 eV (tunable by oxidation degree)
  Applications: precursor to rGO; filtration membranes (precise nm-scale apertures)

Reduced graphene oxide (rGO):
  GO + chemical/thermal/laser reduction -> partial restoration of graphene structure
  Electrical conductivity: 1-1000 S/m (vs. graphene ~10^6 S/m)
  Surface area: 400-1500 m^2/g (vs. theoretical graphene 2630 m^2/g)
  Applications: energy storage (supercapacitor electrodes), composites,
    flexible electronics (cheap, scalable vs. CVD graphene)
  Trade-off: defects limit conductivity; chemical reproducibility variable

CVD graphene:
  CH4 + H2 on Cu foil at 1000 C -> monolayer graphene (catalytic Cu stops growth at 1 layer)
  Transfer: etch Cu, transfer to target substrate (PMMA carrier)
  Quality: large single-crystal domains (cm-scale on Cu)
  Applications: transparent electrodes (OPV, OLED, touch screens)
               Research transistors, Hall sensors
  Production: roll-to-roll on Cu foil achieved (Samsung 2010)
  Challenge: transfer is slow/expensive; grain boundaries limit device performance
```

---

## Application Status: Hype vs. Reality

| Application | Claimed | Actual Status (2026) |
|-------------|---------|---------------------|
| Graphene transistors replacing Si | Common claim | Not happening -- no bandgap |
| CNT transistors for VLSI | IBM road map | Sub-1nm node prototype (2021); not in production |
| Graphene as copper replacement | Interconnect material | IBM/GF working on it; 2028+ timeframe |
| CNT structural composites (aerospace) | High-performance materials | MWCNT in epoxy for lightning strike (Boeing) -- real |
| Graphene in Li-ion batteries | Higher capacity | rGO in anode composites: real but modest improvement |
| C60 in OPV solar | Commercial solar cells | Replaced by non-fullerene acceptors (2016+) |
| CNT fiber stronger than steel | Exotic engineering | Single CNT: yes. Macroscopic fiber: ~10 GPa (real) |
| Graphene filtration membranes | Water desalination | GO membranes in R&D; not commercial-scale yet |

---

## Decision Cheat Sheet

| Need... | Use... |
|---------|--------|
| High-conductivity 1D wire at nm scale | Metallic SWCNT (armchair) |
| Semiconducting channel for FET | Semiconducting SWCNT or graphene nanoribbon |
| Mechanical reinforcement in composites | MWCNT (cheap, available) |
| Electron acceptor in organic solar cell | PCBM (C60 derivative) or non-fullerene acceptor |
| Transparent flexible electrode | CVD graphene (large area) or rGO (cheap) |
| Supercapacitor electrode material | rGO or CNT (high SA, conducting) |
| Fundamental 2D physics research | CVD graphene on substrate |
| Twist-angle superlattice (magic angle) | BN-encapsulated bilayer graphene |

---

## Common Confusion Points

**"Carbon nanotubes are already in everyday products."** MWCNT composites are in some
aerospace/sporting goods. But CNT transistors are not in commercial chips. Graphene
transistors are not commercially deployed. Many "graphene product" marketing claims are
for graphite-containing composites, not true graphene.

**"Graphene's 200,000 cm^2/V/s mobility is what you get in devices."** That's for
suspended graphene at low temperature. On a substrate, at room temperature, you get
10,000-15,000 cm^2/V/s -- still high, but 10-15x less than the headline number.

**"CNT chirality determines whether it's metallic."** The (n-m) mod 3 rule is correct but
it is a zero-temperature calculation. At room temperature, near-metallic semiconducting
tubes have very small bandgaps that thermally close. The practical threshold for
semiconducting behavior in transistors is bandgap > ~0.4 eV, which requires
small-diameter tubes.

**"SWCNT and MWCNT are interchangeable."** No. MWCNT are always metallic (mixed walls).
SWCNT can be semiconducting. For transistors, only SWCNT work. For composites and
conductors, MWCNT are fine and much cheaper.
