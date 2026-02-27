# Crystal Structure — Crystallography, Defects, and Diffraction

## The Big Picture

```
    CRYSTAL STRUCTURE LANDSCAPE
    ════════════════════════════════════════════════════════════

    Atomic arrangement
         │
         ├── LATTICE TYPE (how lattice points are arranged)
         │   14 Bravais lattices in 3D
         │   → 7 crystal systems (cubic, tetragonal, orthorhombic,
         │     hexagonal, trigonal, monoclinic, triclinic)
         │
         ├── BASIS (what sits on each lattice point)
         │   1 atom, 2 atoms, molecule, ion pair...
         │   Space group = lattice + basis symmetry (230 total)
         │
         ├── UNIT CELL (smallest repeating volume)
         │   FCC, BCC, HCP, diamond cubic, NaCl structure...
         │
         ├── MILLER INDICES
         │   Planes (hkl), directions [uvw], families {hkl}, <uvw>
         │
         ├── DIFFRACTION
         │   Bragg's law, systematic absences, structure factor
         │
         └── DEFECTS
             Point → Line → Planar → Volume
             (vacancies → dislocations → grain boundaries → precipitates)
```

---

## The 14 Bravais Lattices

```
    Crystal System    Lattice Types              a,b,c   α,β,γ
    ─────────────────────────────────────────────────────────────
    Cubic             P, I (BCC), F (FCC)        a=b=c   90°,90°,90°
    Tetragonal        P, I                       a=b≠c   90°,90°,90°
    Orthorhombic      P, C, I, F                 a≠b≠c   90°,90°,90°
    Hexagonal         P                          a=b≠c   90°,90°,120°
    Rhombohedral      P (= Trigonal)             a=b=c   α=β=γ≠90°
    Monoclinic        P, C                       a≠b≠c   90°,β,90°
    Triclinic         P                          a≠b≠c   α≠β≠γ≠90°

    P = Primitive (corner atoms only)
    I = Body-centered (P + 1 atom at cube center)
    F = Face-centered (P + 1 atom on each face)
    C = Base-centered (P + 1 atom on top and bottom face)
```

Engineering relevance: most structural metals are cubic (FCC, BCC) or hexagonal (HCP).

---

## FCC, BCC, HCP in Detail

### Face-Centered Cubic (FCC)

Examples: Cu, Al, Ni, Au, Ag, Pt, γ-Fe (austenite), Pb

```
    Unit cell: cube with atoms at 8 corners + 6 face centers

         ●─────────●
        /|    ●   /|
       / |        / |
      ●─────────●  |
      |  ●─────|──●
      | /      | /
      |/       |/
      ●─────────●

    Atoms per unit cell:
      Corners: 8 × (1/8) = 1
      Faces:   6 × (1/2) = 3
      Total:   4 atoms/unit cell

    Lattice parameter a (from hard sphere model):
      Close-packed direction: [110] face diagonal
      4r = a√2  →  r = a√2/4 = a/(2√2)

    Coordination number: 12
    (each atom touches 4 in same layer + 4 above + 4 below)

    Atomic packing factor (APF):
      APF = (4 atoms × (4/3)πr³) / a³
          = 4 × (4/3)π(a/2√2)³ / a³
          = 4 × (4/3)π/(2√2)³
          = 4 × (4/3)π/16√2
          = π/(3√2)
          ≈ 0.7405  (highest possible for equal spheres)

    Close-packed planes: {111} — three Miller planes
    Close-packed directions: <110> — six directions
    Slip systems: {111}<110>
    Number of independent slip systems: 4 planes × 3 directions = 12
    → 12 slip systems makes FCC VERY DUCTILE
```

### Body-Centered Cubic (BCC)

Examples: α-Fe (ferrite), W, Cr, Mo, V, Nb, Ta, Na, K

```
    Unit cell: cube with 1 atom at center + 8 at corners

    Atoms per unit cell:
      Corners: 8 × (1/8) = 1
      Center:  1 × 1     = 1
      Total:   2 atoms/unit cell

    Close-packed direction: [111] body diagonal
      4r = a√3  →  r = a√3/4

    Coordination number: 8
    (but next-nearest neighbors at a are also close: 6)

    APF = (2 × (4/3)πr³) / a³
        = 2 × (4/3)π(a√3/4)³ / a³
        = (4π/3) × (3√3/64) × 2
        = π√3/8
        ≈ 0.6802

    Slip systems: {110}<111>, {112}<111>, {123}<111>
    Dominant: {110}<111> → 6 planes × 2 directions = 12 systems
    Also: {112}<111> → 12 × 1 = 12, {123}<111> → 24 × 1 = 24
    Total: ~48 systems → BCC also ductile (but not as ordered as FCC)

    Key difference from FCC: no compact {111}-type close-packed PLANE
    → Peierls stress higher → BCC metals stronger but less ductile at low T
    → BCC shows ductile-to-brittle transition (DBT) temperature
    → FCC metals remain ductile to cryogenic T
```

### Hexagonal Close-Packed (HCP)

Examples: Ti (α), Mg, Zn, Co, Cd, Zr, Be

```
    Unit cell: hexagonal prism

    Parameters: a (basal plane), c (height)
    Ideal c/a = √(8/3) ≈ 1.633
    Real: Mg=1.624, Zn=1.856 (non-ideal), Ti=1.587

    Atoms per unit cell: 6
      Corners:  2 hexagons × 6 corners × (1/6) = 2
      Face centers: 2 × (1/2) = 1
      Interior: 3 × 1 = 3
      Total: 6 atoms (or 2-atom basis per lattice point, 3 lattice points)

    APF = 0.7405 (same as FCC — both are close-packed)

    Coordination number: 12

    Stacking: FCC = ABC ABC... HCP = AB AB...
      A layer: atoms at (0,0,0)
      B layer: atoms at (1/3, 2/3, 1/2)
      A layer: atoms at (0,0,1) [c period]

    Slip systems:
    Basal:    (0001)<11̄20>  — 1 plane × 3 directions = 3 systems
    Prismatic: {101̄0}<11̄20>— 3 planes × 1 direction = 3 systems
    Pyramidal: {101̄1}<11̄20>— 6 planes × 1 direction = 6 systems
    <c+a>:    {112̄2}<112̄3̄>  — 6 planes × 1 direction = 6 systems

    Without <c+a> slip, HCP cannot accommodate c-axis strains
    → Mg: brittle along c-axis without pyramidal activation
    → Ti: better because pyramidal slip is more accessible
```

### Comparison Table

| Property                | FCC     | BCC     | HCP     |
|-------------------------|---------|---------|---------|
| Atoms/cell              | 4       | 2       | 6       |
| CN                      | 12      | 8       | 12      |
| APF                     | 0.7405  | 0.6802  | 0.7405  |
| Slip systems (primary)  | 12      | 12+     | 3 (basal)|
| Close-packed plane?     | Yes {111}| No     | Yes (0001)|
| DBT behavior            | No      | Yes     | Partial |
| Interstitial sites      | Oct (a/2), Tet (a/4) | Oct (a/2), Tet | Oct, Tet |
| Examples                | Cu,Al,Ni| Fe,W,Cr | Ti,Mg,Zn|

---

## Miller Indices

### Directions [uvw]

The direction is a vector in the unit cell coordinate system.
Steps:
1. Pick head and tail of vector
2. Take differences in a, b, c fractional coordinates
3. Clear fractions to smallest integers
4. Enclose in square brackets [uvw]
5. Negative = bar notation: [1̄00] = [-100]

```
    a-axis direction:  [100]
    b-axis direction:  [010]
    body diagonal:     [111]
    face diagonal FCC close-packed: [110]
    BCC body diagonal (slip direction): [111]

    Family <uvw> includes all symmetrically equivalent directions:
    <100> = [100], [010], [001], [1̄00], [01̄0], [001̄]  (6 members, cubic)
    <110> = 12 members in cubic
    <111> = 8 members in cubic
```

### Planes (hkl)

Miller indices for a plane: find intercepts on a, b, c axes (in units of a, b, c),
take reciprocals, clear fractions to smallest integers.

```
    Plane intersecting at:    Intercepts:   Reciprocals:   Miller:
    a=1, b=∞, c=∞            1, ∞, ∞       1, 0, 0        (100)
    a=1, b=1, c=∞            1, 1, ∞       1, 1, 0        (110)
    a=1, b=1, c=1            1, 1, 1       1, 1, 1        (111)
    a=1/2, b=∞, c=∞          1/2, ∞, ∞    2, 0, 0        (200)
    a=1, b=2, c=3            1, 2, 3       1, 1/2, 1/3    (632) after clearing

    Negative intercept (plane crosses negative side): bar over index
    (1̄10) = plane with negative a-intercept, positive b-intercept, parallel to c
```

### Interplanar Spacing d_hkl (Cubic)

$$d_{hkl} = \frac{a}{\sqrt{h^2 + k^2 + l^2}}$$

```
    d_100 = a/1 = a
    d_110 = a/√2
    d_111 = a/√3
    d_200 = a/2

    For tetragonal: 1/d² = (h²+k²)/a² + l²/c²
    For hexagonal:  1/d² = (4/3)(h²+hk+k²)/a² + l²/c²
```

### Worked Example: FCC Al (a = 4.05 Å)

```
    Identify close-packed plane and direction:
    Close-packed plane in FCC = {111}
    d_111 = 4.05/√3 = 2.338 Å  ← smallest d, lowest XRD angle (approx)
    d_110 = 4.05/√2 = 2.864 Å
    d_100 = 4.05 Å

    Close-packed direction: <110>
    Vector [110] = a(1,1,0), length = a√2 = 5.728 Å
    Atoms touch along [110]: 4r = a√2 → r = 1.432 Å
```

---

## X-Ray Diffraction

### Bragg's Law

Constructive interference when path difference = nλ:

$$\boxed{\lambda = 2 d_{hkl} \sin\theta}$$

```
    Incoming beam             Diffracted beam
         ╲                      ╱
          ╲  θ              θ  ╱
    ───────●──────────────────●───── Plane 1 (d_hkl)
            ╲                ╱
             ╲θ            θ╱
    ──────────●────────────●──────── Plane 2
              ← extra path = 2d sinθ →

    For constructive interference: 2d sinθ = nλ (n=1,2,...)

    Typically n=1 and we write (hkl) with all multiples:
    (200) for 2nd-order diffraction from (100) planes
    → treat (200) as its own Miller plane with d_200 = d_100/2

    Typical X-ray sources: Cu Kα₁ λ=1.5406 Å, Mo Kα₁ λ=0.7093 Å
    Typical 2θ range for Cu Kα: 10°-120°
    At 2θ=40°: θ=20°, d = 1.5406/(2 sin 20°) = 2.25 Å
```

### Structure Factor F_hkl

Not all (hkl) planes give peaks — selection rules from basis atom positions.

The structure factor is:

$$F_{hkl} = \sum_j f_j \exp\left[2\pi i (h x_j + k y_j + l z_j)\right]$$

where sum is over all atoms j in unit cell with fractional coordinates (x_j, y_j, z_j)
and f_j = atomic scattering factor (∝ number of electrons, varies with sinθ/λ).

Intensity I_hkl ∝ |F_hkl|²

**FCC systematic absences**: Atoms at (0,0,0), (1/2,1/2,0), (1/2,0,1/2), (0,1/2,1/2)

```
    F_hkl = f[1 + e^{iπ(h+k)} + e^{iπ(h+l)} + e^{iπ(k+l)}]

    If h,k,l all even OR all odd: F = 4f → PEAK
    If h,k,l mixed (some even, some odd): F = 0 → ABSENT

    FCC allowed: (111)✓, (200)✓, (220)✓, (311)✓, (222)✓
    FCC absent:  (100)✗, (110)✗, (210)✗, (211)✗
```

**BCC systematic absences**: Atoms at (0,0,0) and (1/2,1/2,1/2)

```
    F_hkl = f[1 + e^{iπ(h+k+l)}]

    h+k+l even:   F = 2f → PEAK
    h+k+l odd:    F = 0  → ABSENT

    BCC allowed: (110)✓, (200)✓, (211)✓, (220)✓, (310)✓, (222)✓
    BCC absent:  (100)✗, (111)✗, (210)✗
```

### Powder Diffraction Pattern

In a powder, all orientations are present → rings at angles satisfying Bragg's law.

```
    Diffractometer scan output (Cu Kα, Al powder):

    Intensity
        │    ║
        │    ║
        │    ║     ║
        │    ║     ║     ║       ║
        │    ║     ║     ║       ║    ║
        └────╨─────╨─────╨───────╨────╨────── 2θ
             38.5° 44.7° 65.1°   78.2°  82.4°
             (111) (200) (220)    (311)  (222)

    d-spacings (Å):  2.338   2.025  1.431   1.221   1.169
    a from d_111: a = 2.338 × √3 = 4.049 Å ✓ (literature: 4.050 Å)

    Powder XRD workflow:
    1. Identify peaks by 2θ position
    2. Calculate d_hkl from Bragg's law
    3. Assign (hkl) from systematic absences and ratio analysis
    4. Refine lattice parameter a from all peaks (Rietveld method)
    5. Peak broadening → crystallite size (Scherrer), microstrain
```

### Scherrer Equation (Crystallite Size)

Peak broadening β (FWHM in radians) from finite crystallite size D:

$$D = \frac{K\lambda}{\beta \cos\theta}$$

K = Scherrer constant ≈ 0.9 (for spherical crystallites).
This sets a floor on peak width — instrument broadening and microstrain add to β.

---

## Crystal Defects

### Point Defects

```
    ┌─────────────────────────────────────────────────────────┐
    │  POINT DEFECTS                                          │
    │                                                         │
    │  Vacancy: missing atom □                                │
    │    Equilibrium concentration: n/N = exp(-E_f/kT)        │
    │    E_f ≈ 1 eV for Cu → n/N ≈ 10⁻⁶ at 900°C            │
    │    Vacancies required for solid-state diffusion         │
    │                                                         │
    │  Interstitial: extra atom in gap between lattice sites  │
    │    Octahedral or tetrahedral holes in FCC/BCC           │
    │    Carbon in iron: octahedral (BCC): r_oct=0.19a,       │
    │    r_C=0.77 Å → enormous strain → limited solubility    │
    │    (0.022%C max in α-Fe at 727°C)                       │
    │                                                         │
    │  Substitutional: foreign atom replacing host atom       │
    │    Hume-Rothery rules for extensive solid solution:     │
    │    1. Size: |r_A-r_B|/r_A < 15%                         │
    │    2. Crystal structure: same                            │
    │    3. Electronegativity: similar (|Δχ| < 0.4)           │
    │    4. Valence: same preferred (higher valence dissolves) │
    │    Cu-Ni: complete mutual solubility (isomorphous)      │
    │    Cu-Zn: up to 35% Zn (α-brass) → more is β, γ phases  │
    │                                                         │
    │  Frenkel defect: atom displaced from lattice → vacant   │
    │    site + interstitial pair (conserves N_atoms)         │
    │    Common in ionic crystals with large size mismatch    │
    │                                                         │
    │  Schottky defect: cation-anion vacancy pair             │
    │    Maintains charge neutrality in ionic crystals        │
    │    NaCl: equal number of Na⁺ and Cl⁻ vacancies          │
    └─────────────────────────────────────────────────────────┘
```

### Line Defects: Dislocations

Dislocations are the fundamental carriers of plastic deformation.
Proposed 1934 independently by Orowan, Polanyi, and Taylor.

**Edge Dislocation**: extra half-plane of atoms

```
    Compression region above dislocation line:
    ● ● ● ● ● ●
    ● ● ● ● ● ●        ← extra half-plane ends here
    ● ● ● │ ● ●   ←── dislocation line (perpendicular to page)
    ● ● ● ● ● ●
    ● ● ● ● ● ●
    Tension region below

    Burgers circuit: go around dislocation, closure failure = Burgers vector b
    For edge dislocation: b ⊥ to dislocation line
    |b| = a/√2 for FCC {111}<110> slip: b = a/2[110] = a/√2
    Stress field: σ_xy ∝ Gb/r (decays as 1/r from dislocation core)
```

**Screw Dislocation**: lattice is sheared parallel to dislocation line

```
    Steps going around dislocation line = Burgers vector
    For screw: b ∥ to dislocation line
    Stress field: τ = Gb/(2πr)  (pure shear, no normal stress)
    Screw dislocations can cross-slip to alternate plane
    Edge dislocations cannot cross-slip (extra plane is fixed)
```

**Burgers Vector b**: The closure failure in a Burgers circuit around the dislocation.

For an FCC metal, the primary Burgers vector:

$$\mathbf{b} = \frac{a}{2}\langle110\rangle$$

magnitude $|\mathbf{b}| = a/\sqrt{2}$

Energy per unit length ∝ Gb² → shortest b is energetically favorable → Frank's rule:
a dislocation with b₁ splits if |b₁|² > |b₂|² + |b₃|² with b₁ = b₂ + b₃.

For FCC: partial dislocations (b = a/6<112>) have lower energy than perfect dislocations.

**Dislocation Density ρ_d**:
- Annealed metals: ρ_d ~ 10¹⁰ m/m³ = 10¹⁰ m⁻²
- Cold-worked: ρ_d ~ 10¹⁴–10¹⁶ m⁻²
- Taylor hardening: τ = αGb√ρ_d

### FCC Slip Systems in Detail

12 slip systems: {111}<110>

```
    Four {111} slip planes: (111), (1̄11), (11̄1), (111̄)
    Three <110> directions on each: e.g., on (111): [101̄], [1̄10], [01̄1]
    (note: [110] does NOT lie in (111) — check via h·u+k·v+l·w = 0)

    Schmid factor: m = cos φ · cos λ
      φ = angle between tensile axis and slip plane normal
      λ = angle between tensile axis and slip direction
      Shear stress resolved on slip system: τ = σ · m
      Slip begins when τ reaches τ_CRSS (critical resolved shear stress)

    Highest Schmid factor = 0.5 (for φ = λ = 45°)
    Typical τ_CRSS values:
      Pure FCC (Al): 0.5–1 MPa
      Pure BCC (Fe): 5–10 MPa
      After cold work: 100–500 MPa
```

### Planar Defects

**Grain Boundaries**: interfaces between crystallites of different orientation.

```
    Low-angle grain boundary (θ < 10°): array of edge dislocations
      Spacing between dislocations: D = b/θ (θ in radians)
      Energy: γ_gb = γ_0 θ(A - ln θ) (Read-Shockley equation)

    High-angle grain boundary (θ > 10-15°):
      Structure: bad fit → atomic structure complex → less ordered
      Energy: γ_gb ≈ 0.5–1.0 J/m² for most metals
      (compare grain surface energy γ_s ≈ 1–3 J/m²)
      Dihedral angle φ: cos(φ/2) = γ_gb/(2γ_s)

    Special grain boundaries:
      Twin (Σ3): coincidence site lattice, low energy γ ≈ 0.02 J/m²
        FCC: {111} coherent twin (stacking fault = AB AB C AB AB...)
      Σ5, Σ7: other low-energy coincidence site lattice boundaries
```

**Stacking Faults**: wrong stacking sequence

```
    FCC stacking: ... A B C A B C A B C ...
    Intrinsic SF:  ... A B C A B A B C ...  (one C missing)
    Extrinsic SF:  ... A B C A C B A B C... (extra C inserted)

    Stacking fault energy γ_SFE (mJ/m²):
      Al: 166   (high → narrow stacking faults → dislocations recombine easily)
      Cu: 78    (medium)
      Ni: 128   (high)
      Co: 15    (low → wide → planar slip → HCP transformation)
      Austenitic stainless: 15-30 (low → planar slip → TWIP/TRIP effects)

    Low γ_SFE → wide partial dislocation separation → difficult cross-slip
    → planar slip bands → TWIP (twinning-induced plasticity) steels
```

### Volume Defects

- **Precipitates**: second-phase particles forming within matrix
  - Coherent: crystal planes continuous across interface (small misfit → elastic strain)
  - Semi-coherent: periodic misfit dislocations at interface
  - Incoherent: no crystal continuity (large particles, long aging times)
  - Key to precipitation hardening (see 04-METALS-ALLOYS.md)

- **Voids and Pores**: empty spaces from solidification shrinkage, gas evolution, radiation damage

- **Inclusions**: non-metallic phases (oxides, sulfides) incorporated during processing
  - MnS in steel: elongated by rolling → anisotropic toughness
  - Oxide stringers: stress concentration sites → fatigue initiation

---

## Hall-Petch Strengthening

```
    σ_y = σ_0 + k_y / √d

    σ_0  = friction stress (lattice resistance + solid solution hardening)
    k_y  = Hall-Petch coefficient (material-dependent, ~0.1-0.5 MPa·m^(1/2))
    d    = mean grain diameter

    Mechanism: dislocations pile up at grain boundaries
    Pile-up generates stress concentration at boundary → activates slip in next grain
    Smaller d → shorter pile-up → harder to transmit slip → higher σ_y

    Example: annealed AISI 1020 steel
      d = 100 μm: σ_y = 250 MPa
      d = 10 μm:  σ_y = 250 + (k/√(10μm) - k/√(100μm))
                      ≈ 340 MPa (assuming k = 0.28 MPa·m^(1/2))
      d = 1 μm:   σ_y ≈ 530 MPa

    Breaking down: d < 10–20 nm → grain boundary sliding, inverse Hall-Petch
    → nanocrystalline metals softer than expected

    Microstructural refinement methods:
      1. Rapid solidification (melt spinning, LPSO alloys)
      2. Severe plastic deformation: ECAP, HPT, ARB
      3. Recrystallization control (pinning by second-phase particles — Zener pinning)
      4. Controlled rolling (HSLA steels: Nb, Ti, V microalloying)

    Zener pinning of grain growth:
      r_grain < r_c where r_c = 4r_p/(3f)
      r_p = particle radius, f = volume fraction
      → Fine TiN particles pin grain growth during HSLA steel hot rolling
```

---

## Amorphous vs Crystalline: Comparison

```
    ┌──────────────────────────────┬──────────────────────────────┐
    │  CRYSTALLINE                  │  AMORPHOUS (GLASS)           │
    ├──────────────────────────────┼──────────────────────────────┤
    │  Long-range order            │  Short-range order only      │
    │  (periodic lattice)          │  (like snapshot of liquid)   │
    ├──────────────────────────────┼──────────────────────────────┤
    │  Sharp diffraction peaks     │  Broad halo in XRD           │
    ├──────────────────────────────┼──────────────────────────────┤
    │  Anisotropic (single xtal)   │  Isotropic                   │
    │  Isotropic (polycrystal)     │                              │
    ├──────────────────────────────┼──────────────────────────────┤
    │  Grain boundaries = defects  │  No grain boundaries         │
    │  → scatter at GBs           │  → better corrosion         │
    ├──────────────────────────────┼──────────────────────────────┤
    │  Slip on specific planes     │  Shear bands (localized)     │
    │  → work hardens              │  → no work hardening        │
    ├──────────────────────────────┼──────────────────────────────┤
    │  Sharp T_m (first-order)     │  Glass transition T_g        │
    │                              │  (second-order-like, kinetic)│
    ├──────────────────────────────┼──────────────────────────────┤
    │  Examples: Fe, Al, Cu, Si    │  Silica glass, metallic glass│
    │            NaCl, Al₂O₃      │  Zr₄₁Ti₁₄Cu₁₂Ni₁₀Be₂₃ (Vitreloy)│
    └──────────────────────────────┴──────────────────────────────┘

    Metallic glasses: amorphous metals made by rapid quenching (>10⁶ K/s)
    or multi-component alloy design (competing crystal structures)
    Properties: no grain boundaries → no grain boundary corrosion
    Near-theoretical strength (no dislocations to nucleate on)
    BUT: brittle → catastrophic shear band failure
    Applications: transformer cores (low hysteresis), sporting goods
```

---

## Worked Examples

### Example 1: Determine Crystal Structure from XRD

Cu Kα radiation (λ = 1.5406 Å). Observed 2θ peaks: 43.3°, 50.4°, 74.1°, 89.9°, 95.1°

```
    Step 1: Calculate d from Bragg's law d = λ/(2 sinθ):
      43.3° → d = 2.087 Å
      50.4° → d = 1.808 Å
      74.1° → d = 1.278 Å
      89.9° → d = 1.090 Å
      95.1° → d = 1.044 Å

    Step 2: Calculate d₁²/d_n²:
      d₁²/d₁² = 1.000
      d₁²/d₂² = (2.087/1.808)² = 1.333 ≈ 4/3
      d₁²/d₃² = (2.087/1.278)² = 2.665 ≈ 8/3
      d₁²/d₄² = (2.087/1.090)² = 3.666 ≈ 11/3
      d₁²/d₅² = (2.087/1.044)² = 4.000 ≈ 12/3

    Step 3: Multiply ratios by 3: 3, 4, 8, 11, 12
    These are (h²+k²+l²) values:
      3  = 1²+1²+1²   → (111) ✓ FCC allowed
      4  = 2²+0²+0²   → (200) ✓ FCC allowed
      8  = 2²+2²+0²   → (220) ✓ FCC allowed
      11 = 3²+1²+1²   → (311) ✓ FCC allowed
      12 = 2²+2²+2²   → (222) ✓ FCC allowed

    Step 4: Identify as FCC. Calculate a:
      From d₁ = 2.087 Å for (111): a = d₁√3 = 3.615 Å
    → This is FCC copper (literature: 3.615 Å) ✓
```

### Example 2: Calculate Dislocation Density from Yield Strength

An FCC copper sample has σ_y = 200 MPa. G(Cu) = 48 GPa, b = 2.56 Å, α = 0.5.

```
    Taylor hardening: σ_y = σ_0 + αGb√ρ
    Assume σ_0 = 10 MPa (friction stress of annealed Cu)
    200 - 10 = 0.5 × 48×10⁹ × 2.56×10⁻¹⁰ × √ρ
    190 = 6.144 √ρ
    √ρ = 30.9 m⁻¹
    ρ = 955 m⁻² × 10² ≈ 9.6×10¹³ m⁻²

    Compare annealed Cu: ρ ~ 10¹⁰ m⁻²
    → Heavily cold worked (10,000× increase in dislocation density)
```

---

## Decision Cheat Sheet

| Question                              | Answer / Tool                           |
|---------------------------------------|----------------------------------------|
| What crystal structure does alloy have?| XRD phase identification               |
| What grain size?                      | EBSD (automated, statistical), SEM+etching |
| How many phases present?              | XRD + Rietveld refinement, SEM-EDS     |
| Dislocation density?                  | TEM dark field, XRD peak broadening    |
| Texture (preferred orientation)?      | EBSD pole figures, ODF                 |
| Grain boundary character?             | EBSD Σ-values, TEM                     |
| Single crystal vs polycrystal?        | XRD (sharp spots vs rings)             |
| Coherent vs incoherent precipitate?   | HRTEM / HAADF-STEM                     |
| Phase transformation T?              | DSC + in-situ XRD                      |
| Vacancy concentration?                | Positron annihilation spectroscopy     |

---

The mathematical backbone of crystallography is group theory: the 14 Bravais lattices are the 14 distinct translation groups in 3D; the 32 point groups are the finite subgroups of O(3) compatible with translational periodicity (the crystallographic restriction — only 1, 2, 3, 4, 6-fold rotations survive); the 230 space groups are the semidirect products of point groups with translation groups (including screw axes and glide planes). Bloch's theorem in band theory (02-BONDING-BANDS) follows directly: it says eigenstates of the Hamiltonian transform as irreducible representations of the translation group, labeled by wavevector k.

## Common Confusion Points

**Miller index (hkl) vs [hkl]**: Parentheses denote planes, brackets denote directions.
{hkl} is the family of equivalent planes, <uvw> is the family of equivalent directions.
In cubic systems [hkl] is always perpendicular to (hkl), but NOT in other systems.

**Burgers vector ≠ slip direction for partial dislocations**: The perfect Burgers vector
a/2<110> in FCC can split into two partials a/6<112> + a/6<112̄>. Partial dislocations
cannot slip independently — they're connected by a stacking fault ribbon. The width
of the ribbon = γ_SFE matters enormously for deformation mechanism.

**d₁₁₁ ≠ d₁₀₀ even in cubic**: A common mistake. In FCC, the first allowed peak is
actually (111) not (100) because (100) is systematically absent. The spacing d₁₁₁ = a/√3
is SMALLER than d₁₀₀ = a, but appears first in a scan because the structure factor allows it.

**Diffraction peak width ≠ only from crystallite size**: Scherrer gives an apparent
crystallite size from peak broadening. But microstrain (non-uniform elastic strains from
dislocations, compositional fluctuations) ALSO broadens peaks. Williamson-Hall analysis
separates size and strain contributions: β cosθ vs sin θ plot (size-only = horizontal line,
strain adds a slope).
