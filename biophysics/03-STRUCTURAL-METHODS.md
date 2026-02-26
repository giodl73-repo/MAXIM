# Structural Biology Methods — X-ray Crystallography, NMR, and Cryo-EM

## The Big Picture

```
┌──────────────────────────────────────────────────────────────────────────┐
│              STRUCTURAL BIOLOGY METHOD LANDSCAPE                          │
│                                                                            │
│  METHOD         RESOLUTION  SIZE RANGE      KEY LIMITATION               │
│  ─────────────  ──────────  ─────────────   ──────────────────────────── │
│  X-ray crystal  0.5-3 Å     1 kDa - 10 MDa  Must crystallize              │
│  NMR            1-3 Å       <50 kDa          Size limit, assignment effort │
│  Cryo-EM        1.5-4 Å     100 kDa - GDa   Small proteins still hard     │
│  Cryo-ET        2-5 nm      10-100s MDa      In situ tomography            │
│  SAXS           ~1 nm       1 kDa - 1 GDa   Low resolution, envelope only │
│  AFM            ~1 nm       Any size         Low resolution, surface only  │
│                                                                            │
│  DOMINANCE SHIFT:                                                          │
│  1950s-2010s:  X-ray crystallography dominated (~90% of PDB)              │
│  2013-present: Cryo-EM resolution revolution (Kühlbrandt, Frank, Henderson│
│                Nobel 2017) displaced X-ray for large complexes            │
│                                                                            │
<!-- @editor[content/P2]: PDB statistics may be outdated — as of 2024-2025, PDB had ~220,000+ total entries; X-ray ~170,000, NMR ~14,000, cryo-EM ~30,000+; verify current numbers -->
│  2024 PDB statistics:                                                      │
│  X-ray:   ~86,000 entries (~60% of total)                                 │
│  NMR:     ~13,000 entries (~9%)                                            │
│  Cryo-EM: ~30,000 entries (~21%, growing fastest)                         │
└──────────────────────────────────────────────────────────────────────────┘
```

---

## Section 1 — X-ray Crystallography

### The Physical Basis

X-rays have wavelengths ~0.1-2.5 Å — comparable to interatomic distances. When
X-rays scatter from a periodic crystal, constructive interference produces diffraction
spots. The crystal amplifies the signal by having ~10¹⁵ unit cells contributing to
each reflection.

**Bragg's law:**

```
  Diffraction condition:  2d·sin(θ) = nλ

  d = spacing between parallel planes of atoms
  θ = angle between incident beam and crystal plane
  λ = X-ray wavelength
  n = integer (order of diffraction)

  Consequence: only specific angles (θ) give constructive interference.
  Measuring all (θ, φ) positions of diffraction spots → spacing d for all planes
  → 3D electron density map.

  Resolution: d_min = λ / (2 sin(θ_max))
    λ = 1.0 Å, θ_max = 60°: d_min = 0.58 Å  (atomic resolution)
    λ = 1.0 Å, θ_max = 15°: d_min = 1.9 Å   (most PDB depositions)
```

### The Crystallography Pipeline

```
  ┌──────────────────────────────────────────────────────────────────┐
  │  STEP           DETAIL                      BOTTLENECK?          │
  │  ─────────────  ───────────────────────────  ───────────────────  │
  │  1. Expression  Produce mg quantities of     Often rate-limiting  │
  │     & purif.    pure, homogeneous protein     for difficult targets│
  │  2. Crystalliz. Hanging drop vapor diff.     Highly empirical,    │
  │     ation       HT screening, robot plates   many conditions to   │
  │                                              try (T, pH, PEG)     │
  │  3. Data        Synchrotron or rotating-     Needs good crystals  │
  │     collection  anode; rotate crystal;        (large, ordered)    │
  │                 collect millions of spots                         │
  │  4. Data        Indexing, integrating,        Mostly automated    │
  │     processing  scaling; CCP4, XDS, HKL2000                       │
  │  5. Phase       Solve the phase problem       THE hard step        │
  │     determina.  (see below)                                       │
  │  6. Model build Place atoms into density;     Semi-manual, expert │
  │                 Coot for manual fitting                           │
  │  7. Refinement  REFMAC, PHENIX; minimize      R-factor monitoring │
  │                 R-factor                                          │
  │  8. Validation  Ramachandran plot, R/Rfree,   Critical for PDB    │
  │                 geometry checks               deposition          │
  └──────────────────────────────────────────────────────────────────┘
```

### The Phase Problem
<!-- @editor[audience/P3]: The learner knows Fourier analysis from MIT — the explanation that you need amplitude and phase for inverse FT can be tightened; the physical insight (detector loses phase) is the important part, not the Fourier transform definition -->

This is the fundamental difficulty in crystallography. The detector measures
intensities I(hkl) = |F(hkl)|², which gives only the amplitude of each structure
factor F. To compute the electron density by Fourier transform, you need both
amplitude AND phase:

```
  ρ(x,y,z) = (1/V) Σ_hkl  F(hkl) × exp[-2πi(hx + ky + lz)]

  F(hkl) = |F(hkl)| × exp[iφ(hkl)]

  Measured: |F(hkl)|²  →  |F(hkl)|  (amplitude only)
  Lost:     φ(hkl)   ← PHASE PROBLEM
```

**Solutions to the phase problem:**

```
  Method              When to use               Principle
  ──────────────────  ────────────────────────  ─────────────────────────
  Molecular           Homolog structure exists   Use known structure phases
  replacement (MR)    (>30% sequence identity)   as starting estimate

  SIR/MIR             No homolog; can soak in    Heavy atom gives anomalous
  (isomorphous        heavy atoms (Hg, Pt, Au)   signal; difference Fourier
  replacement)                                   locates heavy atom positions

  SAD/MAD             No homolog; use tunable    Anomalous scattering near
  (anomalous)         synchrotron; Se-Met        absorption edge gives
                      incorporation              phase information

  Ab initio           Small proteins <1200 atoms Direct methods; uses
  (direct methods)    at resolution <1.2 Å       triplet phase relationships
```

Today, ~70% of new structures use molecular replacement (MR) because so many
structures exist as search models. SAD phasing (usually Se-Met) handles the rest.

### R-factor: The Quality Metric

The R-factor measures agreement between observed and calculated structure factors:

```
  R = Σ_hkl |F_obs - F_calc| / Σ_hkl F_obs

  R-factor interpretation:
    R > 0.40 → very poor model or wrong solution
    R ≈ 0.20-0.25 → typical final structure
    R < 0.15 → excellent (usually high resolution)

  Rfree: R calculated on ~5% of data withheld from refinement
    Used to detect overfitting (R << Rfree → overfitted)
    |R - Rfree| < 0.05 → healthy model; > 0.10 → suspicious

  Resolution and R-factor:
    2.0 Å structure: R ≈ 0.20 acceptable
    1.0 Å structure: R ≈ 0.12 expected (more atoms resolved)
```

### Limitations of Crystallography

1. **Must crystallize**: many proteins resist crystallization (membrane proteins,
   IDPs, flexible complexes). Crystallization selects for rigid, stable conformations.
2. **Crystal contacts**: the packing arrangement may distort the biologically
   relevant structure or trap one conformation from an ensemble.
3. **Static snapshot**: the structure is an average over ~10¹⁵ unit cells and
   time-averaged over the data collection. Dynamics are invisible.
4. **Radiation damage**: high-flux X-rays reduce disulfide bonds, break Asp/Glu
   carboxylates. Cryo-cooling (100 K) mitigates but doesn't eliminate this.

---

## Section 2 — NMR Spectroscopy

### Physical Basis

Nuclear magnetic resonance exploits the quantum spin states of nuclei (¹H, ¹³C,
¹⁵N, ³¹P). In a magnetic field, spin-½ nuclei adopt α (parallel) or β (antiparallel)
orientations with energy difference ΔE = ħγB₀:

```
  Larmor frequency: ω₀ = γB₀

  Typical: 600 MHz spectrometer, ¹H Larmor freq = 600 MHz
           900 MHz spectrometer: better dispersion and sensitivity

  Chemical shift δ (ppm): measures electron shielding at each nucleus
    Upfield (small δ): shielded, electron-rich environment
    Downfield (large δ): deshielded, electron-poor environment

  Each atom in a unique chemical environment → unique resonance frequency
  → ¹H spectrum shows one peak per chemically distinct proton
```

### Assignment Pipeline

For a 100-residue protein with uniform ¹³C,¹⁵N labeling:

```
  1. HSQC: one peak per N-H → "fingerprint" of protein state
  2. 3D HNCA: connect each NH to its Cα and preceding Cα
  3. 3D HNCACB: connect NH to Cα, Cβ, preceding Cα, Cβ
  4. Walk along backbone: each residue type has characteristic Cα/Cβ shifts
  5. Side chain assignment: HCCH-TOCSY, NOESY
  → Sequential assignment: identify which peak = which residue
```

This is labor-intensive. A 150-residue protein takes weeks to months to fully assign.
Above ~50 kDa, peaks overlap too severely for complete assignment (rotational
correlation time τc too long → fast relaxation → broad linewidths).

### NOE Constraints: Source of Distance Information

The Nuclear Overhauser Effect (NOE) arises from dipolar coupling between spins.
The NOE intensity falls off as 1/r⁶:

```
  NOE intensity ∝ 1/r⁶   (distance r between two protons)

  Observable range: r < 5-6 Å

  Typical protein structure determination:
    - 10-20 NOE distance constraints per residue
    - 1000-2000 total NOEs for 100-residue protein
    - Combined with dihedral angle restraints from coupling constants
    - Structure calculated by constrained energy minimization (CNS, XPLOR-NIH)
    - Ensemble of 20 structures shown (not a single model)
```

NMR gives an **ensemble**, not a single structure. The spread within the ensemble
reflects both experimental uncertainty and genuine structural flexibility. This is
a feature: NMR directly reports on conformational dynamics.

### NMR-Specific Information Unavailable from X-ray

```
  NMR provides unique information:
  ──────────────────────────────────────────────────────────────────────
  Dynamics (ps-ns): R₁, R₂, NOE relaxation → order parameters (S²)
  Dynamics (μs-ms): CPMG relaxation dispersion → exchange rates
  Hydrogen exchange: backbone amide protection → folding core
  Solution state:   native state in buffer, not crystal contacts
  Titrations:       follow CSP (chemical shift perturbation) upon ligand binding
  pKa values:       direct from pH-dependent shift titrations
```

The S² order parameter (0 = fully disordered, 1 = completely rigid) maps flexibility
across every residue. This is inaccessible to X-ray at any resolution.

---

## Section 3 — Cryo-EM Revolution

### Why Cryo-EM Changed Everything

Before ~2013 (the "resolution revolution"), cryo-EM gave 6-20 Å maps — enough for
domain arrangement but not atomic details. Two advances changed this:

```
  1. DIRECT ELECTRON DETECTORS (2012-2013):
     Previous: scintillator-coupled CCD cameras
     → electrons scatter photons → photon blur → MTF degrades

     New: direct detection of electrons → no scintillator blur
     → motion correction of individual movie frames possible
     → large improvement in high-frequency contrast

  2. IMPROVED IMAGE PROCESSING:
     Relion, cryoSPARC: Bayesian maximum-likelihood particle alignment
     → statistical treatment of noisy single-particle images
     → iterative refinement converges to accurate 3D map
```

Result: Cryo-EM routinely achieves 1.5-3.5 Å resolution for proteins >100 kDa.
The 2017 Nobel Prize (Henderson, Frank, Dubochet) recognized the foundational work.

### Sample Preparation

```
  1. Protein in solution (usually 0.1-5 mg/mL)
  2. Apply 3 μL to glow-discharged carbon/gold grid
  3. Blot excess with filter paper (blot time critical: ~2-4 s)
  4. Plunge into liquid ethane at -170°C (vitrification)
  → Water vitrifies (amorphous ice), not crystalline ice
  → Proteins frozen in native-like hydrated state
  → No crystal contacts, no fixation artifacts
```

### The Imaging Challenge: Contrast Transfer Function (CTF)

This is the central technical concept. The electron microscope does not form a
simple projection image — it modulates the image via the contrast transfer function:

```
  CTF(q) = -2 sin[π λ Δf q² - (π λ³ Cs q⁴)/2]

  where:
    q = spatial frequency
    λ = electron wavelength (0.025 Å at 200 keV, 0.020 Å at 300 keV)
    Δf = defocus (μm, typically 0.5-3 μm underfocus)
    Cs = spherical aberration coefficient

  CTF oscillates between +1 and -1 as function of spatial frequency:
    → CTF = +1: good contrast (phase contrast contribution)
    → CTF = 0: no contrast (Thon ring zeros)
    → CTF = -1: inverted contrast

  Must CTF-correct all images before combining into 3D map.
  Thon rings (visible in power spectrum of raw images) are used to fit CTF.
```

**Why this matters**: CTF zeros at specific spatial frequencies mean no information
at those frequencies. Information is "missing" in bands. Averaging many particles at
different defoci (different CTF patterns) fills in the gaps.

### Single-Particle Reconstruction

```
  START: ~10⁵ - 10⁶ particle images (boxed from micrographs)
     ↓
  2D classification: average similar views → clean 2D classes
  (remove ice contamination, broken particles, aggregates)
     ↓
  3D initial model generation (ab initio or prior model)
     ↓
  3D classification: separate conformational heterogeneity
     ↓
  3D refinement: iterative: assign each particle an orientation
  (5 Euler angles + 2 in-plane shifts), compute new 3D map,
  re-align particles, repeat until convergence
     ↓
  Post-processing: B-factor sharpening, local resolution estimation
  (RELION, cryoSPARC: Fourier Shell Correlation = 0.143 criterion)
     ↓
  Map → model: Coot (manual) + Phenix/REFMAC (real-space refinement)
```

### Why Cryo-EM Displaced X-ray for Large Complexes

```
  CRYSTALLOGRAPHY                      CRYO-EM
  ────────────────────────────────────────────────────────────────────
  Must crystallize (HARD for large,    No crystals needed
  flexible, heterogeneous complexes)

  Crystal contacts constrain           Native-like solution state
  conformation                         (multiple conformations isolable)

  Unit cell averaging: one conformation 3D classes: multiple conformations
  per asymmetric unit                  from same dataset

  Radiation damage at 100K             Radiation damage minimized
                                       by dose fractionation

  Best for: small-medium rigid         Best for: large complexes,
  proteins, large crystals            membrane proteins, flexible
                                       assemblies, ribosomes, viruses
```

The ribosome (2.5 MDa), SARS-CoV-2 spike (3 MDa trimers), and nuclear pore complex
(120 MDa) are impossible or impractical to crystallize but yield sub-3 Å cryo-EM maps.

### Current Cryo-EM Limitations

1. **Small proteins**: below ~100 kDa, particle signal-to-noise too low; below ~50 kDa,
   orientation determination becomes unreliable without specialized methods.
2. **Preferred orientation**: particles that adsorb to the air-water interface adopt
   preferred orientations → incomplete Euler angle coverage → anisotropic resolution.
3. **Conformational heterogeneity**: flexible regions cannot be resolved even in
   high-resolution maps; IDPs remain invisible.
4. **Cryo-ET resolution**: in-situ tomography of cellular structures → 2-5 nm
   resolution (subtomogram averaging can reach ~3 Å for abundant complexes).

---

## Section 4 — Comparing the Methods

```
┌────────────────────────────────────────────────────────────────────────────┐
│  COMPARISON TABLE                                                           │
│                                                                             │
│  Feature          X-ray crystal   NMR            Cryo-EM                  │
│  ─────────────────────────────────────────────────────────────────────────│
│  Resolution       0.5-3 Å         1-3 Å          1.5-4 Å (large proteins) │
│  Size range       Any (with Xtal)  <50 kDa        >100 kDa preferred       │
│  Sample state     Crystal          Solution        Vitrified solution      │
│  Dynamics info    Limited (B-factors) Excellent    Limited (class averages) │
│  Time required    Weeks-months    Months-years    Weeks-months             │
│  Unique strength  Atomic detail,  Dynamics, IDPs, Large complexes,         │
│                   high throughput  flexibility     heterogeneity            │
│  Key limitation   Must crystallize <50 kDa limit  Small proteins hard      │
│  Data type        Reciprocal space (direct) NMR   Real space (direct)      │
│                   (diffraction)   frequency space  (electron density)       │
└────────────────────────────────────────────────────────────────────────────┘
```

### Which Method for What

```
  ┌─────────────────────────────────────────────────┐
  │  STRUCTURAL METHOD DECISION TREE                │
  │                                                 │
  │  Protein size?                                  │
  │    < 5 kDa: NMR or X-ray (if crystallizes)     │
  │    5-50 kDa: X-ray OR NMR                       │
  │    50-100 kDa: X-ray preferred; cryo-EM emerging│
  │    > 100 kDa: Cryo-EM preferred                 │
  │                                                 │
  │  Flexibility / disorder?                        │
  │    Ordered core: X-ray or cryo-EM              │
  │    Flexible regions: NMR                        │
  │    Fully disordered: NMR (ensemble) or MD sim   │
  │                                                 │
  │  Want dynamics?                                 │
  │    ps-ns: NMR relaxation                        │
  │    μs-ms: NMR CPMG or relaxation dispersion     │
  │    ms-s: H/D exchange, NMR, SAXS                │
  │    Multiple conformations: cryo-EM 3D classes   │
  │                                                 │
  │  In cellular context?                           │
  │    Cryo-ET (tomography) + subtomogram averaging │
  └─────────────────────────────────────────────────┘
```

---

<!-- @editor[bridge/P2]: No old-world bridge section — natural parallels: Fourier transforms / signal processing to crystallographic phase problem and NMR, Bayesian inference to cryo-EM particle classification, inverse problems in imaging to structural biology reconstruction -->

## Decision Cheat Sheet

| Situation | Method | Why |
|-----------|--------|-----|
| Small rigid protein, need atomic resolution | X-ray | Highest resolution, tractable if crystallizes |
| Need backbone dynamics at every residue | NMR | R₁/R₂/NOE relaxation, S² order parameters |
| Large complex (ribosome, proteasome, spike) | Cryo-EM | No crystallization needed, >100 kDa ideal |
| Need to know conformation in solution, not crystal | NMR or Cryo-EM | Crystal contacts can distort |
| Want multiple conformations from one dataset | Cryo-EM 3D classification | Heterogeneity handled computationally |
| Protein is IDP (intrinsically disordered) | NMR | Crystal and cryo-EM both give poor density |
| Drug binding site mapping | X-ray (soaking) or cryo-EM | Co-crystal or grid soaking |
| No homolog, no prior structure | SAD/MAD (X-ray) or ab initio cryo-EM | Phase problem solutions |

---

## Common Confusion Points

**The phase problem is not an issue in cryo-EM.** Electron microscopy forms a
direct image in real space — the lens system does the Fourier transform optically.
The challenge is the signal-to-noise ratio and CTF correction, not phase recovery.
This is why cryo-EM does not face the crystallographic phase problem.

**Cryo-EM resolution is not uniform.** Local resolution estimation (Resmap, RELION)
shows that rigid cores resolve to 1.5-2 Å while flexible loops may be 4-6 Å in
the same map. "2.5 Å resolution" means the best-resolved regions, not the whole map.

**NMR structures are ensembles by necessity.** The 20-structure bundle deposited in
the PDB does not mean the protein is disordered. It reflects the experimental
uncertainty given the number of constraints. Backbone regions with many NOEs converge
well; exposed loops with few NOEs show more spread. The ensemble is a probability
distribution over conformational space, not multiple distinct states.

**R-factor alone doesn't validate a structure.** Low R-factor with poor Rfree means
overfitting (wrong structure fitted to noise). Ramachandran outliers, clashscore,
and B-factor distributions must all be evaluated. The PDB validation server and
wwPDB deposition pipeline require passing geometric checks.

**Resolution ≠ accuracy for all parts of the structure.** At 2.5 Å, the backbone
trace is reliable but sidechain rotamers in surface loops may be wrong. At 1.0 Å,
hydrogen atoms are visible and alternative conformations can be modeled. Resolution
is an upper bound on accuracy, not a guarantee.
