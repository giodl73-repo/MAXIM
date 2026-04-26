# Computational Materials Science

## Big Picture: Bridging Scales

```
┌────────────────────────────────────────────────────────────────────────┐
│              MULTISCALE MATERIALS SIMULATION HIERARCHY                 │
│                                                                        │
│  SCALE        METHOD              TIME         ATOMS        COST       │
│  ─────────────────────────────────────────────────────────────────     │
│  Electrons    DFT / QMC           ps           1–1000       High       │
│  Atoms        MD (classical)      ns–μs        10⁶–10⁸      Medium     │
│  Grains       Phase field         ms–s         N/A          Low-Med    │
│  Components   FEA                 s–years      N/A          Low        │
│                                                                        │
│  ┌───────────┐    ┌──────────┐    ┌──────────┐    ┌────────────┐       │
│  │  DFT      │ ──►│   MD     │ ──►│  Phase   │ ──►│    FEA     │      │
│  │ Kohn-Sham │    │ Newton   │    │  Field   │    │ Continuum  │      │
│  │ electrons │    │ + force  │    │ diffuse  │    │ mechanics  │      │
│  │           │    │ field    │    │ interface│    │            │      │
│  └───────────┘    └──────────┘    └──────────┘    └────────────┘      │
│     10⁻¹⁰m          10⁻⁹m           10⁻⁶m           10⁻³m            │
│                                                                        │
│  KEY: No single method spans all scales.                               │
│  Multiscale: parameterize coarser model from finer model.             │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 1. Density Functional Theory

### Foundations

```
  MANY-ELECTRON PROBLEM: H Ψ(r₁,...,rₙ) = E Ψ(r₁,...,rₙ)
  Exact but exponentially hard: wavefunction in 3N dimensions

  HOHENBERG-KOHN THEOREM (1964):
    1. Ground-state electron density ρ(r) uniquely determines
       all ground-state properties (energy, geometry, etc.)
    2. Variational principle: E[ρ] ≥ E_ground for any trial ρ

  Result: 3N-dimensional problem → 3-dimensional problem
  Price: E_xc[ρ] = exchange-correlation functional — UNKNOWN
```

### Kohn-Sham Equations

```
┌─────────────────────────────────────────────────────────────────────┐
│  Kohn-Sham (1965): replace interacting electrons with               │
│  non-interacting electrons in an effective potential                │
│                                                                     │
│  [-ℏ²/2m ∇² + V_eff(r)] φᵢ(r) = εᵢ φᵢ(r)                         │
│                                                                     │
│  V_eff = V_ext + V_Hartree + V_xc                                   │
│    V_ext:     external (nuclear) potential                          │
│    V_Hartree: electron-electron Coulomb (mean field)                │
│    V_xc:      exchange-correlation correction                       │
│                                                                     │
│  ρ(r) = Σᵢ |φᵢ(r)|²   (sum over occupied orbitals)                  │
│                                                                     │
│  SELF-CONSISTENT FIELD (SCF) LOOP:                                  │
│    Guess ρ → compute V_eff → solve KS equations → new ρ → repeat    │
└─────────────────────────────────────────────────────────────────────┘
SCF convergence is a fixed-point iteration (rho -> F(rho) -> fixed point). Anderson mixing (also called DIIS — direct inversion in the iterative subspace) accelerates convergence by using the history of residuals to extrapolate toward the fixed point, analogous to Krylov subspace methods in linear algebra. Convergence is not guaranteed in general but is reliable for most materials with appropriate mixing parameters.
```

### XC Functionals and Jacob's Ladder

```
  LEVEL 1 — LDA (Local Density Approximation):
    E_xc = ∫ ε_xc(ρ(r)) ρ(r) d³r
    Only depends on local density. Works surprisingly well for metals.
    Overbinds molecules (~1 eV error).

  LEVEL 2 — GGA (Generalized Gradient Approximation):
    E_xc = ∫ ε_xc(ρ, ∇ρ) d³r
    PBE (Perdew-Burke-Ernzerhof): workhorse for solids
    BLYP, B3LYP: workhorse for chemistry

  LEVEL 3 — Meta-GGA:
    Also uses kinetic energy density τ(r) = Σ |∇φᵢ|²/2
    SCAN functional: satisfies all 17 known exact constraints

  LEVEL 4 — Hybrid (HF + DFT):
    E_xc = α E_x^HF + (1-α) E_x^DFT + E_c^DFT
    B3LYP (α=0.2): chemistry standard, good bandgaps
    HSE06: screened hybrid for solids (O(N) scaling)

  LEVEL 5 — RPA, double hybrids:
    Expensive but highly accurate
    Used for benchmarking, not routine calculations

  COMMON FAILURES:
  - Van der Waals / dispersion: add -D3 correction (Grimme)
  - Strongly correlated (NiO, UO₂): DFT+U Hubbard correction
  - Bandgaps systematically underestimated by LDA/GGA
```

### Practical DFT

```
  PLANE WAVE BASIS:
    Periodic system → Bloch theorem → expand in plane waves e^{ik·r}
    k-points: sample Brillouin zone (Monkhorst-Pack grid)
    Cutoff energy E_cut: determines basis set size (~300–700 eV)

  PSEUDOPOTENTIALS / PAW:
    Core electrons: tightly bound, irrelevant to bonding
    Replace: all-electron → pseudopotential (frozen core approx.)
    PAW (Projector Augmented Wave): most accurate, VASP default

  CODES: VASP (closed), Quantum ESPRESSO (open), WIEN2k, FHI-aims

  TYPICAL CALCULATION:
    1. Crystal structure → POSCAR/CIF input
    2. Choose XC functional, k-grid, E_cut
    3. Structure relaxation: minimize forces on atoms
    4. Electronic structure: bands, DOS, charge density
    5. Properties: elastic constants, phonons, formation energies
```

---

## 2. Molecular Dynamics

### Classical MD

```
┌─────────────────────────────────────────────────────────────────────┐
│  NEWTON'S EQUATIONS: mᵢ r̈ᵢ = Fᵢ = -∂U/∂rᵢ                        │
│                                                                     │
│  Integrate: Verlet algorithm (symplectic, time-reversible)          │
│    r(t+Δt) = 2r(t) - r(t-Δt) + Δt² F(t)/m   (2nd order)          │
│    Velocity Verlet:                                                 │
│      r(t+Δt) = r(t) + v(t)Δt + Δt² F(t)/2m                        │
│      v(t+Δt) = v(t) + Δt[F(t) + F(t+Δt)]/2m                       │
│                                                                     │
│  Timestep: Δt ~ T_vib/20 → 1 fs (atomic), 2–4 fs with constraints   │
│  Trajectory length: MD can reach ns–μs (fast bond vibrations limit) │
└─────────────────────────────────────────────────────────────────────┘
```

### Force Fields

```
  EMPIRICAL POTENTIALS:
  Lennard-Jones (noble gases):
    U(r) = 4ε [(σ/r)¹² - (σ/r)⁶]
    r⁻¹² repulsion (Pauli), r⁻⁶ attraction (van der Waals)

  EAM (Embedded Atom Method — metals):
    U = Σ F(ρᵢ) + Σᵢⱼ φ(rᵢⱼ)
    F: embedding energy as function of local electron density ρ
    Captures metallic bonding (delocalized electrons) better than LJ

  AMBER/CHARMM/OPLS (biomolecules):
    U = bonds + angles + dihedrals + nonbonded(vdW + Coulomb)
    Parameters fit to experimental data or ab initio calculations

  REACTIVE FORCE FIELDS (ReaxFF):
    Bond order varies with geometry → can model reactions
    Slower than EAM but handles chemistry
    Used for: combustion, corrosion, crack propagation

  MACHINE-LEARNED POTENTIALS: (see Section 4)
```

### Enhanced Sampling

```
  PROBLEM: MD timescale << rare event timescale
  Example: protein folding (ms), nucleation (hours), diffusion barriers

  SOLUTIONS:
  ┌─────────────────────────────────────────────────────────────────┐
  │  Metadynamics:                                                  │
  │  Add Gaussian bias V_bias(ξ) along collective variable ξ        │
  │  Fills free energy minima — recovers F(ξ) as -V_bias            │
  │  Risk: overfilling — use well-tempered metadynamics             │
  │                                                                 │
  │  Umbrella Sampling:                                             │
  │  Restrain system near transition state with harmonic bias       │
  │  Run many windows, combine with WHAM → F(ξ) profile             │
  │                                                                 │
  │  Replica Exchange (REMD):                                       │
  │  N copies at different T; periodically swap coordinates         │
  │  High-T replicas escape barriers, low-T replicas sample well    │
  │                                                                 │
  │  Transition Path Sampling:                                      │
  │  Sample only reactive trajectories (A → B)                      │
  │  No a priori reaction coordinate required                       │
  └─────────────────────────────────────────────────────────────────┘
```

---

## 3. Phase Field Modeling

### Core Idea

```
┌─────────────────────────────────────────────────────────────────────┐
│  SHARP INTERFACE → DIFFUSE INTERFACE:                               │
│                                                                     │
│  Sharp:  grain boundary = mathematical surface (hard to compute)    │
│  Diffuse: order parameter φ(r) smoothly varies 0→1 across boundary  │
│                                                                     │
│  ORDER PARAMETER: φ = 0 (phase A), φ = 1 (phase B), 0<φ<1 (boundary)│
│                                                                     │
│  FREE ENERGY FUNCTIONAL (Landau-Ginzburg):                          │
│    F[φ] = ∫ [f(φ) + κ/2 |∇φ|²] d³r                               │
│    f(φ) = bulk free energy (double-well shape for two-phase)        │
│    κ/2 |∇φ|²: interfacial energy (penalizes sharp gradients)        │
└─────────────────────────────────────────────────────────────────────┘
```

### Allen-Cahn and Cahn-Hilliard

```
  ALLEN-CAHN (non-conserved order parameter):
    ∂φ/∂t = -M δF/δφ = M[∇²φ - f'(φ)/κ]
    Models: grain growth, solidification, antiphase domain coarsening
    φ not conserved — volume of phase can change

  CAHN-HILLIARD (conserved — spinodal decomposition):
    ∂c/∂t = ∇·[M ∇(δF/δc)] = M ∇²[f''(c)c - κ∇²c]
    Models: spinodal decomposition, phase separation in alloys
    c conserved — total composition fixed (∫c d³r = const)
    Note: Cahn-Hilliard is a 4th-order parabolic PDE (dc/dt ~ -M kappa nabla^4 c + ...).
    In the spinodal region where f''(c) < 0, the nabla^2 c term has wrong-sign diffusion
    (uphill diffusion — concentration gradients amplify rather than smooth). The nabla^4 c
    term from the gradient energy provides regularization, selecting a characteristic
    wavelength for the spinodal decomposition pattern. Same regularization structure as
    the Swift-Hohenberg and thin-film equations.

  COUPLED PROBLEM (solidification — Kim-Steinbach):
    Phase field + diffusion + latent heat + anisotropy
    → Dendritic growth patterns (snowflake morphology)
    Benchmark: NIST solidification challenge

  PARAMETERS from DFT/MD:
    Interface energy γ → κ in F[φ]
    Diffusivity D → M
    Free energy landscape f(c) → thermodynamic database (CALPHAD)
```

---

## 4. Machine-Learned Potentials

### The Revolution

```
  CLASSICAL FF: fast (ps/atom/step), limited chemistry
  AIMD (ab initio MD): accurate, O(N³), max ~1000 atoms
  MLP: DFT accuracy + classical MD speed

  ARCHITECTURE EVOLUTION:
  ┌─────────────────────────────────────────────────────────────────┐
  │  Behler-Parrinello NN (2007):                                   │
  │  Atom-centered symmetry functions → NN → atomic energy Eᵢ       │
  │  E_total = Σ Eᵢ  (additivity assumption)                        │
  │  Trained on DFT energies, forces, stresses                      │
  │                                                                 │
  │  Message-Passing NN (SchNet, DimeNet, PaiNN):                   │
  │  Atoms = nodes, bonds = edges                                   │
  │  Aggregate: vᵢ ← Σⱼ f(vⱼ, vᵢ, rᵢⱼ)  (message passing)       │
  │  Equivariant: NequIP, MACE (respect 3D rotational symmetry)     │
  │  ~10× better data efficiency than symmetry functions            │
  │                                                                 │
  │  Foundation Models:                                             │
  │  MACE-MP-0 (2023): trained on MPTrj (150k structures)           │
  │  M3GNet, CHGNet: properties + dynamics                          │
  │  Universal: no per-material training → instant deployment       │
  │  GNoME (DeepMind, 2023): 2.2M stable crystal structures         │
  └─────────────────────────────────────────────────────────────────┘
```

---

## 5. Materials Informatics

### Databases and Representations

```
  DATABASES:
  ┌──────────────────────┬───────────┬─────────────────────────────┐
  │ Database             │ Entries   │ Content                     │
  ├──────────────────────┼───────────┼─────────────────────────────┤
  │ Materials Project    │ 154k      │ DFT energy, bands, elastic  │
  │ AFLOW                │ 3.5M      │ High-throughput DFT         │
  │ OQMD                 │ 1.2M      │ Formation energies          │
  │ NOMAD                │ 12M       │ Calculations archive        │
  │ ICSD                 │ 280k      │ Experimental crystal struct.│
  │ CSD                  │ 1.2M      │ Molecular crystal data      │
  └──────────────────────┴───────────┴─────────────────────────────┘

  CRYSTAL REPRESENTATIONS:
  Coulomb Matrix: Cᵢⱼ = ZᵢZⱼ/|Rᵢ-Rⱼ| (i≠j), Zᵢ²·4·2/3 (i=j)
  SOAP (Smooth Overlap of Atomic Positions): density expansion
  ACSF (atom-centered symmetry functions): Behler-Parrinello input
  Crystal graph: atoms = nodes, bonds = edges + edge features
  MatBERT, CrystalBERT: language models for crystal structure
```

### Property Prediction Workflow

```
┌─────────────────────────────────────────────────────────────────────┐
│  HIGH-THROUGHPUT SCREENING WORKFLOW:                                │
│                                                                     │
│  1. Define search space (compositional, structural, dopants)        │
│  2. Generate candidates (substitution, prototype enumeration)       │
│  3. Fast screening: ML property prediction                          │
│  4. DFT calculation on top candidates (~100–1000)                   │
│  5. Experimental validation (~10)                                   │
│  6. Iterate: add DFT results to training set                        │
│                                                                     │
│  ACTIVE LEARNING:                                                   │
│  Uncertainty quantification (GP, ensemble) → query points where     │
│  model is uncertain → targeted DFT → model improves                 │
│  Bayesian optimization: acquisition function (UCB, EI) guides       │
│  search toward unexplored high-performance regions                  │
│                                                                     │
│  SUCCESS STORIES:                                                   │
│  - Lithium superionic conductors (Sendek, 2017): ML screening       │
│    identified LiZnPS₄ from 12,000 candidates                        │
│  - GNoME (DeepMind, 2023): 2.2M stable crystals predicted           │
│    vs. 48k known; 736 experimentally validated                      │
│  - High-entropy alloys: ML predicts phase stability                 │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 6. CALPHAD and Thermodynamic Modeling

```
  CALPHAD (CALculation of PHAse Diagrams):
  Model Gibbs free energy G(T, P, xᵢ) for each phase
  Fit parameters to experimental + DFT data
  Minimize G → equilibrium phases (phase diagram)

  G_phase = G_ref + G_ideal + G_excess + G_mag
    G_ref:    reference (weighted pure elements)
    G_ideal:  -T Σ xᵢ ln xᵢ  (ideal mixing entropy)
    G_excess: Redlich-Kister: Σ Lᵏᵢⱼ xᵢxⱼ(xᵢ-xⱼ)ᵏ (interaction)
    G_mag:    magnetic contribution (Inden-Hillert-Jarl)

  DATABASES: TCFE (steels), TCAL (Al alloys), assessed thermodynamics
  CODES: Thermo-Calc, Pandat, OpenCalphad

  INTEGRATION WITH DFT:
    SQS (Special Quasirandom Structures): mimic random alloy in DFT
    Cluster Expansion (CE): expand E(σ) in basis of cluster functions
    ML + CALPHAD: replace CALPHAD functionals with neural networks
```

---

## Decision Cheat Sheet

```
┌──────────────────────────────────┬────────────────────────────────────┐
│  Problem                         │  Method                            │
├──────────────────────────────────┼────────────────────────────────────┤
│  Electronic structure, bandgap,  │  DFT (PBE for metals, hybrid for   │
│  formation energy, bonding       │  semiconductors)                   │
├──────────────────────────────────┼────────────────────────────────────┤
│  Dynamics of thousands of atoms  │  Classical MD (EAM, AMBER, ReaxFF) │
│  ns–μs timescale                 │                                    │
├──────────────────────────────────┼────────────────────────────────────┤
│  Dynamics with chemical accuracy │  Machine-learned potential (MACE,  │
│  millions of atoms               │  NequIP, MACE-MP-0)                │
├──────────────────────────────────┼────────────────────────────────────┤
│  Grain growth, microstructure,   │  Phase field (Allen-Cahn /         │
│  solidification, phase separation│  Cahn-Hilliard)                    │
├──────────────────────────────────┼────────────────────────────────────┤
│  Equilibrium phase diagram       │  CALPHAD + Thermo-Calc             │
│  for multicomponent alloy        │                                    │
├──────────────────────────────────┼────────────────────────────────────┤
│  Predict material property from  │  Graph NN (SchNet, DimeNet, CGCNN) │
│  structure                       │  trained on Materials Project      │
├──────────────────────────────────┼────────────────────────────────────┤
│  Screen 10k+ candidate materials │  ML surrogate + active learning    │
│  for specific property target    │  + DFT validation on top candidates│
├──────────────────────────────────┼────────────────────────────────────┤
│  Strongly correlated electrons   │  DFT+U, DMFT, or quantum chemistry │
│  (NiO, cuprates, rare earths)    │  (CCSD(T) for molecules)           │
└──────────────────────────────────┴────────────────────────────────────┘
```

---

## Common Confusion Points

**DFT is not MD.** DFT solves for the electronic ground state at fixed nuclear positions. MD moves the nuclei using forces. AIMD (Ab Initio MD) = DFT for forces + MD for nuclear motion — slow but accurate, ~100 ps max.

**The bandgap problem.** LDA/GGA systematically underestimate bandgaps by 30–100% (even predict metals for some semiconductors). Hybrid functionals (HSE06) and GW approximation fix this. Always use beyond-GGA for electronic applications.

**Periodic vs. aperiodic.** Plane-wave DFT codes (VASP, QE) assume periodic boundary conditions. Molecules need supercells with vacuum padding or a localized-basis code (Gaussian, FHI-aims).

**Force field transferability.** EAM fits for pure Fe may not work for Fe-Cr alloys. Classical FFs are not transferable across chemistry — always validate against DFT for new systems. Universal MLPs (MACE-MP-0) are more transferable but still have limits.

**CALPHAD extrapolation.** CALPHAD is interpolative within its database. Ternary and higher-order systems use binary interaction parameters without ternary corrections — can fail badly. Always check against independent DFT or experiments.

**The timescale gap.** Classical MD reaches μs with heroic effort. Phase transitions, diffusion, nucleation, and protein folding happen at ms–s. Enhanced sampling (metadynamics, replica exchange) bridges this partially. Some problems are genuinely inaccessible to atomistic simulation.
