# Materials Science — Landscape Overview

## The Four Families and the Tetrahedron

Materials science is structured around one central organizing insight:
**structure determines properties, processing controls structure, performance is the goal.**

```
                    MATERIALS SCIENCE LANDSCAPE
    ═══════════════════════════════════════════════════════════

                         PERFORMANCE
                             /\
                            /  \
                           /    \
                          /      \
                         /        \
                        /          \
             STRUCTURE ────────────── PROPERTIES
                        \          /
                         \        /
                          \      /
                           \    /
                            \  /
                             \/
                         PROCESSING

    The tetrahedron: every node affects every other node.
    No face is independent.

    STRUCTURE:    atomic bonding, crystal lattice, microstructure,
                  defects, grain size, phase distribution

    PROPERTIES:   mechanical (E, σ_y, K_IC), thermal (α, k, T_m),
                  electrical (σ, ε_r), optical (n, α_abs), magnetic

    PROCESSING:   casting, rolling, forging, heat treatment,
                  powder processing, vapor deposition, polymerization

    PERFORMANCE:  fatigue life, corrosion resistance, wear,
                  specific strength, thermal efficiency
```

---

## The Four Material Families

```
    MATERIALS
    │
    ├── METALS & ALLOYS
    │   ├── Ferrous: plain carbon steels (1xxx), alloy steels,
    │   │            stainless (304, 316, 17-4PH), tool steels
    │   ├── Aluminum: 1xxx (pure), 2xxx (Cu), 6xxx (Mg-Si), 7xxx (Zn)
    │   ├── Titanium: Ti-6Al-4V (α+β), Ti-6Al-2Sn-4Zr-2Mo (near-α)
    │   ├── Nickel superalloys: Inconel 718, René N6, CMSX-4 (DS/SC)
    │   ├── Copper alloys: brasses (Cu-Zn), bronzes (Cu-Sn), beryllium Cu
    │   └── Refractory: W (T_m=3422°C), Mo, Ta, Re, Nb
    │
    ├── CERAMICS & GLASSES
    │   ├── Oxide: Al₂O₃ (corundum), ZrO₂ (cubic/tetragonal/monoclinic),
    │   │          MgO, SiO₂ (quartz, cristobalite, fused silica)
    │   ├── Non-oxide: SiC (3C/4H/6H polytypes), Si₃N₄, BN, WC, TiN
    │   ├── Glasses: soda-lime (window), borosilicate (Pyrex), fused silica,
    │   │           metallic glasses (Zr-Cu-Al-Ni, amorphous = no grain boundaries)
    │   └── Piezoelectric/ferroelectric: PZT (Pb(Zr,Ti)O₃), BaTiO₃, LiNbO₃
    │
    ├── POLYMERS
    │   ├── Thermoplastics: PE, PP, PS, PVC, PMMA, Nylon 6/66, PET, PC
    │   ├── High-performance: PEEK, PTFE (Teflon), PEI (Ultem), PI (Kapton)
    │   ├── Thermosets: epoxy (DGEBA + amine), vinyl ester, phenolic (Bakelite)
    │   └── Elastomers: NR (natural rubber cis-1,4-PI), SBR, EPDM, silicone (PDMS)
    │
    └── COMPOSITES
        ├── Polymer matrix (PMC): CFRP (C fiber/epoxy), GFRP (glass/polyester)
        ├── Metal matrix (MMC): SiC/Al, TiB₂/Al, W/Cu (heat sinks)
        ├── Ceramic matrix (CMC): SiC/SiC (jet engine hot section, 2000°C capable)
        ├── Natural: bone (30% collagen + 70% hydroxyapatite), wood, nacre
        └── Structural: reinforced concrete (concrete + rebar), plywood
```

### Property Comparison Table

| Property            | 4340 Steel | Al 7075   | Ti-6Al-4V  | CFRP (UD) | Si₃N₄      | PEEK      |
|--------------------|-----------|-----------|------------|-----------|------------|-----------|
| ρ (g/cm³)          | 7.85      | 2.81      | 4.43       | 1.58      | 3.20       | 1.32      |
| E (GPa)            | 210       | 72        | 114        | 135 axial | 310        | 3.6       |
| σ_y (MPa)          | 1620      | 503       | 1100       | —         | —          | 91        |
| σ_UTS (MPa)        | 1760      | 572       | 1170       | 1500 axial| 800        | 100       |
| K_IC (MPa√m)       | 48        | 24        | 55         | 30-60     | 5-8        | 5         |
| T_m or T_g (°C)   | 1425      | 660       | 1660       | ~180 resin| 1900       | 143 T_g   |
| k (W/m·K)          | 44        | 130       | 6.7        | 3-10      | 20         | 0.25      |
| E/ρ (GPa·cm³/g)    | 27        | 26        | 26         | 85        | 97         | 2.7       |
| σ_y/ρ (MPa·cm³/g)  | 206       | 179       | 248        | —         | —          | 69        |

CFRP wins on specific modulus and specific strength — why aerospace uses it despite cost.

---

## Ashby Property Charts

Ashby charts plot one material property against another on log-log axes.
Each material family clusters in a distinct region. Performance indices
(material selection criteria derived from structural analysis) appear as
straight lines with characteristic slope on log-log plots.

### E vs Density (Stiffness Chart)

```
    E (GPa)
    1000 ┤  Diamond●   ●SiC ●Al₂O₃ ●Si₃N₄
         │                   ●W
     300 ┤          ●steels ●Ti alloys
         │    ●Ni alloys
     100 ┤         ●Al alloys    ●CFRP (axial)
         │    ●Mg alloys
      30 ┤               ●GFRP
         │  ●concrete
      10 ┤  ●woods (grain)
         │       ●Nylon
       3 ┤  ●HDPE
         │     ●PP
       1 ┤  ●elastomers
         │
     0.1 ┤──────────────────────────────────── ρ (g/cm³)
         0.1      0.3     1      3      10   30

    Performance indices (slope on log-log plot):
      Stiff tie (tension):        E/ρ       slope 1
      Stiff beam (bending):       E^(1/2)/ρ slope 2
      Stiff panel (plate):        E^(1/3)/ρ slope 3
    Higher index = lighter component for same stiffness.
    CFRP (axial) and ceramics outperform metals.
```

### Strength vs Toughness (Damage Tolerance)

```
    σ_y (MPa)
    3000 ┤   ●maraging steel  ●UHSS (steel cord)
    2000 ┤   ●spring steel    ●Ti-6Al-4V
    1000 ┤   ●Al 7075-T6      ●Ni superalloys
     500 ┤   ●Al 2024         ●Cu alloys       ●CFRP
     200 ┤   ●1020 steel
     100 ┤   ●Nylon ●PP                        ●GFRP
      50 ┤   ●epoxy
      20 ┤   ●ZrO₂(TZP)
      10 ┤   ●Al₂O₃  ●SiC  ●Si₃N₄
       5 ┤   ●soda-lime glass   ●PMMA
         │
       1 ┤──────────────────────────────────── K_IC (MPa√m)
         0.1      1      3     10     30    100   300

    Upper-right quadrant = both strong AND tough.
    Ceramics: high σ_y, low K_IC → catastrophic brittle failure.
    Metals: ductile flow blunts crack tip → high K_IC.
    Toughened ceramics: ZrO₂ transformation toughening → better K_IC.
```

---

## The Physics → Chemistry → Engineering Bridge

```
    ┌──────────────────────────────────────────────────┐
    │  QUANTUM MECHANICS (Schrödinger, Hilbert space)   │
    │  ψ, Ĥ, eigenvalues → atomic orbital shapes, E   │
    └──────────────────────┬───────────────────────────┘
                           │
                           ▼
    ┌──────────────────────────────────────────────────┐
    │  ATOMIC BONDING                                   │
    │  • Ionic:    Madelung energy, Coulomb             │
    │  • Covalent: MO theory, hybridization, σ/π bonds │
    │  • Metallic: free electrons, Fermi sea            │
    │  • van der Waals: London dispersion               │
    │                                                   │
    │  Mie potential: U(r) = A/r^n - B/r^m            │
    │  Bond energy E_b, equilibrium r₀, curvature      │
    │  → E_elastic ∝ d²U/dr²|_{r₀} / r₀              │
    │  → T_m ∝ E_b                                     │
    │  → α_thermal ∝ asymmetry of U(r) potential well  │
    └──────────────────────┬───────────────────────────┘
                           │
                           ▼
    ┌──────────────────────────────────────────────────┐
    │  CRYSTAL STRUCTURE                                │
    │  14 Bravais lattices, space groups               │
    │  FCC (Cu, Al, Ni): CN=12, APF=0.74               │
    │  BCC (Fe, W, Cr):  CN=8,  APF=0.68               │
    │  HCP (Ti, Mg, Zn): CN=12, APF=0.74               │
    │  → density = nA/(V_c·N_A)                        │
    │  → slip systems determine ductility              │
    └──────────────────────┬───────────────────────────┘
                           │
                           ▼
    ┌──────────────────────────────────────────────────┐
    │  DEFECTS                                          │
    │  • Point: vacancies, interstitials, substitutionals│
    │  • Line: edge/screw dislocations                  │
    │  • Planar: grain boundaries, stacking faults      │
    │  → Dislocations enable plastic flow              │
    │  → Blocking dislocations = hardening mechanisms  │
    └──────────────────────┬───────────────────────────┘
                           │
                           ▼
    ┌──────────────────────────────────────────────────┐
    │  MICROSTRUCTURE                                   │
    │  Grain size d, phase fractions f_α/f_β           │
    │  Precipitate size r, spacing λ                   │
    │  Controlled by: T, t, ε during processing        │
    └──────────────────────┬───────────────────────────┘
                           │
                           ▼
    ┌──────────────────────────────────────────────────┐
    │  PROPERTIES                                       │
    │  σ_y = f(d, ρ_disloc, r_precipitate, c_solute)  │
    │  E = essentially independent of microstructure   │
    │  K_IC = f(crack tip plasticity, grain size)      │
    └──────────────────────────────────────────────────┘
```

### Band Theory Chain (for Electrical Properties)

```
    Schrödinger in periodic potential V(r+R) = V(r):
    [−ℏ²/2m ∇² + V(r)] ψ_k(r) = E_k ψ_k(r)

    Bloch theorem: ψ_k(r) = u_k(r) · e^{ik·r}
    where u_k has lattice periodicity.

    → Energy bands E_n(k) for each band n
    → Band gaps where no allowed E_k states exist

    Fermi level E_F placement determines class:
    ┌─────────────────────────────────────────────────────┐
    │                                                     │
    │  E_F in partially filled band → METAL               │
    │  (Fe, Cu, Al: high σ_e, free electrons)             │
    │                                                     │
    │  E_F in gap, small gap (< 2 eV) → SEMICONDUCTOR     │
    │  (Si: 1.1 eV, Ge: 0.67 eV, GaAs: 1.43 eV)          │
    │  Thermally excited carriers, doping shifts E_F      │
    │                                                     │
    │  E_F in large gap (> 3 eV) → INSULATOR              │
    │  (SiO₂: 9 eV, Al₂O₃: 7 eV, diamond: 5.5 eV)        │
    │                                                     │
    └─────────────────────────────────────────────────────┘

    Conductivity: σ = n·e·μ = n·e²·τ/m*
      n = carrier density (from Fermi-Dirac + DOS)
      μ = drift mobility (limited by scattering: phonon, impurity)
      τ = mean free time between scattering events
      m* = effective mass = ℏ²/(d²E/dk²) at band extremum
```

---

## Materials Selection Methodology (Ashby Method)

### Step 1: Define Function, Constraints, Objectives, Free Variables

```
    FUNCTION:     What does the component do?
                  → "bear tensile load", "act as thermal insulator",
                    "transmit electromagnetic radiation"

    CONSTRAINTS:  Non-negotiable limits:
                  → must survive T > 800°C
                  → must be sterilizable (autoclave at 134°C)
                  → must be optically transparent at λ = 532 nm
                  → cost < $50/kg

    OBJECTIVES:   What to optimize:
                  → minimize mass, minimize cost, maximize lifetime,
                    maximize thermal efficiency

    FREE VARS:    What you can choose:
                  → material family and grade
                  → geometry (shape factor φ incorporates I-beam, etc.)
```

### Step 2: Derive Performance Index

**Example: lightest stiff tie rod** (axial tension, fixed cross-section area A)

```
    Stiffness requirement: F/δ = EA/L ≥ S_required  → A ≥ SL/E
    Mass:                  m = ρAL ≥ ρSL²/E
    Minimize mass          → maximize E/ρ

    Performance index M_I = E/ρ

    In Ashby E-ρ chart: draw line E/ρ = const (slope 1 on log-log)
    All materials on or above this line meet stiffness at same or less mass.
```

**Example: lightest stiff beam** (bending, fixed length L, width b free)

```
    EI/L³ ≥ C for stiffness, I = bh³/12, m = ρbhL
    Solve: minimize ρ/E^(1/2) → maximize E^(1/2)/ρ  (slope 2 on log-log)
```

**Example: lightest stiff panel** (plate of fixed area, thickness free)

```
    maximize E^(1/3)/ρ  (slope 3 on log-log)
    → CFRP and foams can beat metals for panels
```

### Step 3: Screen for Constraints

Eliminate materials that violate hard constraints:
- T_max < T_service → remove polymers below ~200°C
- K_IC < 5 MPa√m → remove for any fracture-critical application
- σ_electrical > 10⁻⁸ S/m → remove insulators for electrical contacts

### Step 4: Rank Survivors by Objective

Sort remaining candidates by M_I value. Plot on chart.

### Common Performance Indices

| Function                        | Constraint        | Performance Index     |
|---------------------------------|-------------------|-----------------------|
| Stiff tie rod (axial)           | Fixed length, A   | E/ρ                   |
| Stiff beam (bending)            | Fixed length      | E^(1/2)/ρ             |
| Stiff panel (plate)             | Fixed dimensions  | E^(1/3)/ρ             |
| Strong tie rod                  | Fixed cross-section| σ_y/ρ                |
| Strong beam                     | Fixed length      | σ_y^(2/3)/ρ           |
| Spring (elastic energy density) | Volume limited    | σ_y²/E                |
| Damage tolerant plate           | Any               | K_IC/σ_y (= crack size)|
| Thermal shock resistance        | Steep ΔT          | σ_y·k / (E·α_T)       |
| Heat sink                       | Fixed weight      | k/ρ                   |
| Thermal insulation panel        | Fixed thickness   | 1/(k·ρ·c_p)^(1/2)     |
| Fatigue-limited shaft           | Stress amplitude  | σ_e^(2/3)/ρ           |
| Bearing surface                 | Wear rate         | H/k_w (hardness/wear coeff)|

---

## Measurement and Characterization Methods

```
    ┌──────────────────────────────────────────────────────────────────┐
    │              CHARACTERIZATION METHOD MATRIX                      │
    │                                                                  │
    │  Technique   │ What measured        │ Scale    │ Destructive?   │
    │  ────────────┼──────────────────────┼──────────┼───────────────  │
    │  XRD (Bragg) │ Crystal structure,   │ bulk avg │ No            │
    │              │ phase ID, lattice    │          │               │
    │              │ param, texture, stress│         │               │
    │  ────────────┼──────────────────────┼──────────┼───────────────  │
    │  TEM (HRTEM) │ Atomic columns,      │ 0.1-100nm│ Yes (lamella) │
    │              │ dislocations, phases │          │               │
    │  ────────────┼──────────────────────┼──────────┼───────────────  │
    │  SEM + EDS   │ Microstructure,      │ 10nm-1mm │ Light prep    │
    │              │ fracture, composition│          │               │
    │  ────────────┼──────────────────────┼──────────┼───────────────  │
    │  EBSD        │ Grain orientation,   │ 50nm-1mm │ Light polish  │
    │              │ IPF maps, textures   │          │               │
    │  ────────────┼──────────────────────┼──────────┼───────────────  │
    │  APT         │ 3D atom-by-atom chem │ < 100nm  │ Yes (needle)  │
    │              │ segregation, clusters│          │               │
    │  ────────────┼──────────────────────┼──────────┼───────────────  │
    │  Nanoindent  │ E, H at nm scale     │ nm-μm    │ Minimal       │
    │  ────────────┼──────────────────────┼──────────┼───────────────  │
    │  DSC         │ T_g, T_m, ΔH_f       │ mg sample│ No (mostly)   │
    │  TGA         │ Decomposition, mass  │ mg sample│ Yes           │
    │  ────────────┼──────────────────────┼──────────┼───────────────  │
    │  DMA         │ E'(ω), E''(ω), tan δ │ mg-g     │ No            │
    │  ────────────┼──────────────────────┼──────────┼───────────────  │
    │  Tensile     │ E, σ_y, UTS, ε_f     │ mm-cm    │ Yes           │
    │  Charpy      │ CVN impact energy    │ standard │ Yes           │
    │  J-integral  │ K_IC, J_IC           │ standard │ Yes           │
    │  Jominy      │ Hardenability profile│ bar      │ Yes           │
    │  ────────────┼──────────────────────┼──────────┼───────────────  │
    │  Hall effect │ Carrier n, mobility μ│ device   │ No            │
    │  4-pt probe  │ Resistivity ρ_e      │ film/bulk│ No            │
    │  ────────────┼──────────────────────┼──────────┼───────────────  │
    │  Raman       │ Bonding, strain,     │ μm spot  │ No            │
    │              │ carbon allotropes    │          │               │
    └──────────────────────────────────────────────────────────────────┘
```

---

## Historical Arc

| Era       | Discovery                                           | Impact                          |
|-----------|-----------------------------------------------------|---------------------------------|
| ~3000 BCE | Bronze (Cu + 10% Sn)                                | First alloy engineering         |
| ~1200 BCE | Iron smelting                                       | Iron Age (stronger than bronze) |
| 1856      | Bessemer converter                                  | Cheap bulk steel                |
| 1900      | Martensitic transformation understood               | Heat treatment science          |
| 1912      | X-ray diffraction (von Laue, Bragg)                | Crystal structure determination  |
| 1934      | Dislocation concept (Orowan, Polanyi, Taylor)       | Plasticity theory               |
| 1947      | Transistor (Bell Labs)                              | Semiconductor age               |
| 1957      | Age hardening mechanism (coherency strain)          | High-strength Al alloys         |
| 1960s     | Fracture mechanics (Irwin, Rice J-integral)         | Safe-life design                |
| 1970s     | DS/SC Ni superalloys                                | 1000°C+ turbine entry T         |
| 1980s     | CFRP scale-up for aerospace                        | F-18, A320 composites           |
| 1991      | Carbon nanotubes (Iijima, NEC)                      | Nanomaterials field born        |
| 2004      | Graphene isolation (Geim, Novoselov, Manchester)    | 2D materials era                |
| 2022+     | Solid-state batteries, high-entropy alloys          | Energy storage, extreme service |

---

## Bridge to Learner's Prior Knowledge

### Quantum Mechanics Bridge
The Schrodinger equation maps onto materials as follows:
- Atomic bonds: molecular orbital theory = linear combination of atomic orbitals (LCAO)
- Band theory: Bloch's theorem, band structure E_n(k), effective mass tensor
- Fermi-Dirac statistics for electron occupation
- Phonons (quantized lattice vibrations) → thermal conductivity, heat capacity

Key equation you know: Ĥ|ψ⟩ = E|ψ⟩
Materials application: H = -ℏ²∇²/2m + V_lattice(r) → solved in reciprocal space via plane wave basis

### Linear Algebra / Differential Geometry Bridge
- Stress tensor σ_ij: rank-2, symmetric (6 independent components for 3D)
- Strain tensor ε_ij: symmetric, relates to displacement field u by ε_ij = ½(∂u_i/∂x_j + ∂u_j/∂x_i)
- Generalized Hooke's law: σ_ij = C_ijkl ε_kl (rank-4 stiffness tensor, up to 21 independent constants for triclinic, reduces to 3 for cubic: C₁₁, C₁₂, C₄₄)
- Tensor rotation: C'_ijkl = R_im R_jn R_kp R_lq C_mnpq (Voigt notation simplifies this)
- Crystallographic texture: orientation distribution function (ODF) = probability density on SO(3)

### Thermodynamics Bridge
- Gibbs free energy G = H - TS: minimum at equilibrium (const T, P)
- Chemical potential μ_i = (∂G/∂n_i)_{T,P,n_{j≠i}}
- Phase diagrams = equilibrium G minimization at each T, c
- Spinodal decomposition: ∂²G/∂c² < 0 → no nucleation barrier, uphill diffusion
- Nucleation rate J ∝ exp(-ΔG*/kT) where ΔG* = 16πγ³/3(ΔG_v)² for sphere

### Distributed Systems Bridge
Polycrystalline materials ARE distributed systems:
- Each grain = node with local state (orientation tensor, dislocation density ρ)
- Grain boundaries = interfaces with: segregation, diffusion flux, sliding
- Collective mechanical behavior (macroscopic yielding) = emergent from local slip avalanches
- Texture (statistical distribution of grain orientations) = global correlation from processing history
- Failure = percolation of damage through network (like fault propagation in distributed systems)

---

## Decision Cheat Sheet — Which Family for What?

| Application Need                  | Primary Choice      | Secondary         | Avoid          |
|-----------------------------------|--------------------|--------------------|----------------|
| Jet engine turbine blades (1000°C)| Ni single-crystal  | ODS alloys         | Al, polymers   |
| Airframe (stiff, light)           | CFRP               | Al 7075            | Steel (heavy)  |
| Biomedical implant (load-bearing) | Ti-6Al-4V / PEEK   | Co-Cr alloys       | Stainless (Ni allergy) |
| Electronic substrate (heat sink)  | Cu, AlN, diamond   | Al (cheap)         | Polymers       |
| Semiconductor device              | Si, GaAs, GaN      | SiC (power)        | Metals         |
| Cutting tool (wear resistance)    | WC-Co cermet       | TiN/TiAlN coating  | Plain steel    |
| Spring (elastic energy storage)   | Spring steel, PEEK | Carbon fiber       | Ceramics       |
| Optical window (IR)               | Sapphire (Al₂O₃)   | ZnSe, Ge           | Polymers       |
| Magnet (permanent)                | NdFeB              | SmCo               | Al, ceramics   |
| Chemical reactor (acid)           | PTFE, Hastelloy C  | Ceramic            | Al, Cu         |
| Li-ion battery anode              | Graphite, Si       | Li metal           | Metals (react w/ Li) |
| Thermal barrier coating (TBC)     | 8YSZ (ZrO₂+8%Y₂O₃)| CMAS-resistant new | Metals         |

---

## Common Confusion Points

**Hardness ≠ toughness, hardness ≠ stiffness**: Three distinct concepts.
- Hardness (HV, HRC): resistance to plastic indentation. Increases with dislocation barriers.
- Toughness (K_IC, Charpy CVN): energy to propagate a crack. Requires ductility to blunt crack tip.
- Stiffness (E, Young's modulus): resistance to elastic deformation. Determined by bond stiffness, nearly microstructure-independent.
- You can have hard+brittle (glass: high HV, low K_IC), tough+soft (annealed copper), stiff+brittle (SiC: high E, low K_IC).

**Phase diagram shows equilibrium — processing gives non-equilibrium**:
The Fe-C equilibrium diagram says a 0.4%C steel at room T has α-ferrite + Fe₃C.
But quench rapidly enough and you get martensite (metastable BCT, never appears on equilibrium diagram).
Equilibrium is the attractor; kinetics determines whether you reach it.

**Alloying does not simply average properties**: Adding 10% Ni to Fe does not give 90%Fe + 10%Ni properties.
The alloy's crystal structure, band structure, and defect energetics change fundamentally.
Austenitic stainless steel (18Cr-8Ni) has FCC structure even at room T; plain carbon steel is BCC.

**Grain boundary = strongest path OR weakest path depending on conditions**:
At low T, grain boundaries block dislocation motion → polycrystalline stronger than single crystal (Hall-Petch).
At high T (T/T_m > 0.5), grain boundary diffusion and sliding → grain boundaries are the failure sites (creep, hot cracking).
