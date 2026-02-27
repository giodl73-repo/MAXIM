# Bonding and Band Theory — From Atomic Orbitals to Conductivity

## The Big Picture

```
    BONDING AND BANDS LANDSCAPE
    ══════════════════════════════════════════════════════════

    Atomic orbitals          → Bonding types        → Band theory
    1s, 2s, 2p, 3d, 4f           ionic                   energy bands
    quantum numbers              covalent                 band gaps
    wavefunctions                metallic                 Fermi level
    Aufbau + Hund's rules        van der Waals            DOS

                           ↓
                    Crystal structure
                    (periodic lattice)
                           ↓
               Bloch's theorem + reciprocal lattice
                           ↓
                  Band structure E_n(k)
                           ↓
              Metal / Semiconductor / Insulator
                           ↓
              Electrical, optical, thermal properties
```

The cascade from quantum mechanics to engineering properties runs entirely
through bonding → bands. The key insight: properties are determined by how
electrons are shared between atoms.

---

## Four Bonding Types

### 1. Ionic Bonding

Electron transfer from electropositive atom to electronegative atom → electrostatic attraction.
Examples: NaCl, MgO, Al₂O₃, ZnO, GaAs (partially ionic).

**Madelung Energy**: Energy of a crystal of ions relative to separated neutral atoms.

$$U = -\frac{A \cdot N \cdot e^2}{4\pi\epsilon_0 r_0} \left(1 - \frac{1}{n}\right)$$

- A = Madelung constant (depends on crystal structure, not ion types)
  - NaCl structure: A = 1.7476
  - CsCl structure: A = 1.7627
  - Wurtzite (ZnS): A = 1.6413
- N = number of ion pairs per mole = N_Avogadro
- r₀ = equilibrium nearest-neighbor distance
- n = Born exponent (hardness of repulsion, 5–12 from compressibility)

Born-Mayer repulsive term: U_rep = B·exp(-r/ρ) where ρ ~ 0.03 nm.

Full lattice energy (Born-Haber cycle):
$$U = -\frac{A N e^2}{4\pi\epsilon_0 r_0}\left(1 - \frac{\rho}{r_0}\right)$$

```
    Example: NaCl
    A = 1.7476, r₀ = 2.81 Å (Na-Cl distance = (a/2) where a=5.62 Å)
    n = 8 (from compressibility)
    U = -(1.7476 × 6.022×10²³ × (1.602×10⁻¹⁹)²) / (4π × 8.85×10⁻¹² × 2.81×10⁻¹⁰)
      × (1 - 1/8)
    U ≈ -756 kJ/mol
    Experimental (Born-Haber): -788 kJ/mol (correction needed for zero-point energy)

    Properties of ionic crystals:
    → High melting points (strong electrostatic bonds): NaCl 801°C, MgO 2852°C
    → Brittle: shift by one lattice repeat → like-charge alignment → repulsion
    → Non-conducting at room T (mobile ions only above T_m)
    → Transparent in visible (band gap >> photon energy)
    → Soluble in polar solvents (water dipole breaks ion pairs)
```

### 2. Covalent Bonding

Electron sharing between atoms with similar electronegativity. Directional bonds.

**Molecular Orbital (MO) Theory**: Linear combination of atomic orbitals (LCAO)

For two H atoms with 1s orbitals φ_A and φ_B:

$$\psi_\pm = \frac{1}{\sqrt{2(1\pm S)}}(\phi_A \pm \phi_B)$$

where S = ⟨φ_A|φ_B⟩ = overlap integral.

```
    Energy of bonding (ψ₊) and antibonding (ψ₋) MOs:
                                    ψ₋ (antibonding)  σ*
                                 ↗
    Energy     ─────────────── 1s (atom A)    ─────────────── 1s (atom B)
                                 ↘
                                    ψ₊ (bonding)      σ

    Bond order = (bonding electrons - antibonding electrons) / 2
    H₂: 2 bonding, 0 antibonding → bond order = 1
    He₂: 2 bonding, 2 antibonding → bond order = 0 → no bond

    N₂: σ(1s)² σ*(1s)² σ(2s)² σ*(2s)² π(2p)⁴ σ(2p)²
    = (2-2+2-2+4+2)/2 = 3 → triple bond
```

**Hybridization**: promotion + mixing of atomic orbitals

```
    sp³ hybridization (diamond, Si, Ge, methane):
      Mix one 2s + three 2p → four equivalent sp³ hybrid orbitals
      Tetrahedral geometry, bond angle 109.5°
      Each sp³ orbital forms a σ bond
      Diamond: C-C bond length 1.54 Å, E_bond = 347 kJ/mol per bond
      Hardest natural material (all σ bonds, fully 3D network)

    sp² hybridization (graphene, graphite, benzene, alkenes):
      Mix one 2s + two 2p → three sp² orbitals (trigonal planar, 120°)
      One unhybridized p_z orbital perpendicular to plane → π bonds
      Graphene: sp² network → π electrons delocalized over 2D lattice
      → Dirac cone, massless fermions, minimum conductivity

    sp hybridization (acetylene, CO₂, carbon nanotubes):
      Mix one 2s + one 2p → two sp (linear, 180°)
      Two unhybridized p orbitals → two π bonds
```

Covalent bond properties:
- Directional (unlike ionic/metallic) → forms specific geometries
- Hard and brittle when 3D network (diamond, SiC, Si₃N₄)
- High melting point: diamond T_m ~ 3825°C (subl.), SiC T_m ~ 2730°C
- Non-conducting unless band gap is small (Si = semiconductor)

### 3. Metallic Bonding

Valence electrons delocalized across entire crystal → "electron sea"

**Free Electron Model (Drude-Sommerfeld)**:

Treat metal as N ions in a box filled with free electrons.

Electron energy levels are standing waves in a cubic box of side L:

$$E = \frac{\hbar^2}{2m}\left(\frac{\pi^2}{L^2}\right)(n_x^2 + n_y^2 + n_z^2)$$

or equivalently in k-space: $E = \frac{\hbar^2 k^2}{2m}$ where $k = (n_x, n_y, n_z)\pi/L$.

At T=0, fill states from lowest energy up to **Fermi energy** E_F:

$$\boxed{E_F = \frac{\hbar^2}{2m}\left(3\pi^2 n\right)^{2/3}}$$

where n = electron density (electrons/m³).

```
    Fermi energies for common metals:
    Cu: n = 8.49×10²⁸ m⁻³ → E_F = 7.04 eV (T_F = 81,600 K!)
    Al: n = 18.1×10²⁸ m⁻³ → E_F = 11.7 eV
    Na: n = 2.65×10²⁸ m⁻³ → E_F = 3.15 eV

    Key insight: T_F >> T_room (room T = 0.025 eV ≈ 300 K << T_F)
    → Only electrons within ~kT of E_F are thermally excited
    → Most electrons "frozen" → quantum effect is crucial
    → This is why metals don't contribute R per electron to heat capacity
    (Classical Dulong-Petit would predict C_V = 3/2 R per electron)
    (Quantum: C_V = π²nk²T/(2E_F) << 3/2 R at room T)
```

**Fermi-Dirac Distribution**:

Probability that an electron state of energy E is occupied:

$$f(E) = \frac{1}{e^{(E-E_F)/kT} + 1}$$

```
    T = 0: f(E) = 1 for E < E_F, f(E) = 0 for E > E_F (step function)
    T > 0: smearing by ~kT around E_F
    kT at room T = 0.026 eV → smearing is tiny compared to E_F ~ 5-10 eV

    f(E_F) = 0.5 exactly (definition of E_F at T > 0)
```

**Density of States** (3D free electron):

$$g(E) = \frac{4\pi(2m)^{3/2}}{h^3} E^{1/2} = C \cdot E^{1/2}$$

```
    DOS increases as E^(1/2) → more states available at higher energy
    In lower dimensions:
      2D: g(E) = const (step function for each subband)
      1D: g(E) ∝ E^(-1/2) (Van Hove singularities at band edges)
      0D: g(E) ∝ δ(E - E_n) (discrete levels, quantum dot)

    These dimension-dependent DOS shapes are the origin of quantum
    dot colors, nanowire electronic properties, etc.
```

**Metallic bond properties**:
- Non-directional → metals flow (dislocations, ductility)
- Partially filled band → high electrical conductivity
- Electrons also carry thermal energy → k_thermal ∝ σ_electrical (Wiedemann-Franz)
- Metallic luster: free electrons absorb and re-emit all photon energies up to ℏω_plasma
- Thermal expansion: asymmetric potential well → mean position shifts with T

### 4. Van der Waals / Secondary Bonding

Induced dipole-dipole interactions. Weak, non-directional.

**London Dispersion** (instantaneous dipole-induced dipole):
$$U_{London} = -\frac{C_6}{r^6}$$
C₆ = 3α²I/4(4πε₀)² where α = polarizability, I = ionization potential.

```
    Interaction strength scales with polarizability → larger atoms bind more strongly
    Noble gases: He (very weak) → Xe (stronger)
    T_b: He = 4.2 K, Ne = 27 K, Ar = 87 K, Kr = 120 K, Xe = 165 K

    Graphite layers: held by van der Waals (π electron polarizability large)
    Layer spacing 3.35 Å → easy cleavage (pencil marks paper!)
    Interlayer binding energy ~ 0.04 eV/atom << C-C covalent 3.5 eV/atom

    Gecko adhesion: vdW from ~500 nm setae (billions of contacts)
    Combined area effect → macroscopic adhesion without sticky substance
```

**Hydrogen Bonds**: special case, partially covalent in character.
O-H···O, N-H···N, F-H···F. Energy 5-40 kJ/mol.
Critical for: water properties (unusually high T_b, T_m), protein secondary structure
(α-helix, β-sheet), DNA base pairing (A=T: 2 H-bonds, G≡C: 3 H-bonds).

---

## Band Theory: Crystalline Solids

In a periodic crystal, electron wavefunctions must satisfy Bloch's theorem.

### From Atomic Orbitals to Band Structure

**Tight-Binding Model**: Start with isolated atomic orbitals; turn on nearest-neighbor hopping.

For a 1D chain of N atoms with spacing a, orbital energy ε₀, overlap integral γ:

$$E(k) = \epsilon_0 - 2\gamma\cos(ka)$$

```
    k ranges from -π/a to +π/a (1st Brillouin zone)

    E_min at k=0:   E = ε₀ - 2γ   (if γ > 0, bonding character)
    E_max at k=±π/a: E = ε₀ + 2γ  (antibonding character)

    Bandwidth = 4γ = width of energy band
    More overlap (smaller r, more delocalized) → larger γ → wider band

    For 3D: tighter binding → bands can overlap (metals) or not (insulators)
    This is the origin of the distinction between metal, semiconductor, insulator
```

**Bloch's Theorem**: In any periodic potential V(r+R) = V(r):

$$\psi_{n\mathbf{k}}(\mathbf{r}) = e^{i\mathbf{k}\cdot\mathbf{r}} u_{n\mathbf{k}}(\mathbf{r})$$

where u has the lattice periodicity. The quantum number k is the crystal momentum.

```
    Band index n, crystal momentum k both needed to label states.
    k lives in the Brillouin zone (reciprocal lattice unit cell).

    Reduced zone scheme: fold all bands into first BZ
    Extended zone scheme: unfold bands across multiple BZ copies
    Repeated zone scheme: show all bands periodically in k-space
```

### Reciprocal Lattice and Brillouin Zones

For a direct lattice with primitive vectors a₁, a₂, a₃, the reciprocal lattice has:

$$\mathbf{b}_1 = 2\pi \frac{\mathbf{a}_2 \times \mathbf{a}_3}{\mathbf{a}_1 \cdot (\mathbf{a}_2 \times \mathbf{a}_3)}$$

(and cyclic permutations).

```
    Real space lattice → Reciprocal lattice:
    FCC (a) → BCC (4π/a)
    BCC (a) → FCC (4π/a)
    SC (a)  → SC  (2π/a)

    First Brillouin Zone = Wigner-Seitz cell of reciprocal lattice
    = volume closer to Γ (k=0) than to any other reciprocal lattice point

    BZ for FCC: truncated octahedron (14 faces: 6 squares + 8 hexagons)
    BZ for BCC: rhombic dodecahedron (12 faces)
    BZ for SC:  cube

    High-symmetry points (notation for cubic):
    Γ = (0,0,0) center
    X = (1,0,0)π/a face center
    L = (1,1,1)π/a zone corner (face diagonal in BZ)
    K = (3/4, 3/4, 0) zone edge midpoint

    Band structure usually plotted along Γ→X→M→Γ→L path
```

### Metals, Semiconductors, Insulators

```
    ┌─────────────────────────────────────────────────────────┐
    │  METAL (partially filled band):                          │
    │                                                          │
    │  ───────────── E_F (middle of conduction band)           │
    │  ╔═══════════╗                                           │
    │  ║           ║  ← states above E_F available            │
    │  ╚═══════════╝                                           │
    │  ╔═══════════╗                                           │
    │  ║███████████║  ← filled states below E_F               │
    │  ╚═══════════╝                                           │
    │                                                          │
    │  Even infinitesimal electric field accelerates electrons │
    │  → σ_e ~ 10⁷ S/m (Cu), 10⁶ S/m (Al)                   │
    │  Resistivity: ρ_e = m/(ne²τ) increases with T           │
    │  (more phonon scattering at higher T)                    │
    │                                                          │
    ├─────────────────────────────────────────────────────────┤
    │  SEMICONDUCTOR (E_F in small gap, E_g ~ 0.5-3 eV):       │
    │                                                          │
    │  ─────────────   ← conduction band (CB, mostly empty)   │
    │       E_g ↕                                             │
    │  ─────────────   ← valence band (VB, mostly full)       │
    │                                                          │
    │  E_F lies in gap. At T=0: perfectly insulating.          │
    │  At T>0: thermal excitation across E_g                  │
    │  n_i = √(N_c N_v) exp(-E_g/2kT) intrinsic carriers      │
    │  Sensitive to temperature and doping                     │
    │                                                          │
    ├─────────────────────────────────────────────────────────┤
    │  INSULATOR (E_F in large gap, E_g > 3-4 eV):            │
    │                                                          │
    │  ─────────────   ← conduction band (empty)              │
    │       E_g ↕   (too large for thermal or optical          │
    │  ─────────────   ← valence band (full)  excitation)     │
    │                                                          │
    │  σ_e ~ 10⁻¹⁴ S/m for SiO₂                              │
    │  Transparent in visible (E_photon < E_g)                 │
    └─────────────────────────────────────────────────────────┘
```

### Effective Mass

Near a band minimum/maximum, E(k) is approximately parabolic:

$$E(\mathbf{k}) \approx E_0 + \frac{\hbar^2 k^2}{2m^*}$$

Effective mass:
$$m^* = \hbar^2 \left(\frac{d^2E}{dk^2}\right)^{-1}$$

```
    Key insights from effective mass:
    → Band curvature sets m*: flatter band → larger m* → heavier electron
    → Near band MAXIMUM: d²E/dk² < 0 → m* < 0 → HOLE
      Hole = absence of electron in otherwise full valence band
      Hole moves opposite to electron: like bubble in liquid
      Hole charge = +e, mobility μ_h usually < μ_e

    Effective masses for common semiconductors:
    Si:    m*_e = 0.26m₀, m*_h = 0.36m₀ (averaged)
    GaAs:  m*_e = 0.067m₀, m*_h = 0.47m₀ (very light electron → high mobility)
    Ge:    m*_e = 0.12m₀,  m*_h = 0.21m₀
    GaN:   m*_e = 0.20m₀,  m*_h = 0.80m₀
```

---

## Band Gaps of Common Materials

| Material     | E_g (eV) | Type    | Class        | λ_gap (nm) | Application          |
|--------------|---------|---------|--------------|-----------|----------------------|
| Diamond      | 5.5     | Indirect| Wide-gap ins | 225       | UV windows           |
| GaN          | 3.4     | Direct  | Semiconductor| 365       | Blue/UV LED, 5G      |
| SiC (4H)     | 3.2     | Indirect| Semiconductor| 387       | Power electronics    |
| GaP          | 2.26    | Indirect| Semiconductor| 549       | Green LED (w/ N)     |
| GaAs         | 1.43    | Direct  | Semiconductor| 868       | Laser, solar cell    |
| InP          | 1.35    | Direct  | Semiconductor| 919       | Fiber optics         |
| Si           | 1.12    | Indirect| Semiconductor| 1107      | CMOS, solar cells    |
| Ge           | 0.67    | Indirect| Semiconductor| 1851      | IR detector          |
| InAs         | 0.36    | Direct  | Semiconductor| 3444      | Mid-IR detector      |
| InSb         | 0.17    | Direct  | Semiconductor| 7300      | Far-IR, night vision |
| Graphene     | 0       | —       | Semimetal    | —         | THz, transparent electrode |

**Direct vs Indirect Band Gap**:
- Direct: conduction band minimum at same k as valence band maximum → photon alone can excite electron across gap → efficient light emission (LEDs, lasers use direct-gap materials)
- Indirect: conduction minimum at different k → phonon required to conserve momentum → inefficient light emission (Si terrible for LEDs), but bulk photovoltaics OK (phonons available)

---

## Hall Effect — Measuring Carrier Type and Density

Apply current in x-direction, magnetic field B in z-direction.
Lorentz force on carriers: F = q(v × B)

```
    ┌─────────────────────────────────────────────┐
    │                                              │
    │   B ↑ (into page)                           │
    │   ──────────────────────────────────────    │
    │   I_x →    ●  ●  ●  ●                      │
    │            electrons move ←                 │
    │   Lorentz force on e⁻: F = -e(v × B)       │
    │   v = -v_x x̂, B = B_z ẑ                   │
    │   F = -e(-v_x x̂ × B_z ẑ) = ev_x B_z ŷ    │
    │   → electrons accumulate on +y face          │
    │   → Hall voltage V_H = positive on -y face  │
    │                                              │
    │   Hall coefficient R_H = E_y/(J_x B_z)      │
    │   For electrons: R_H = -1/(ne) < 0          │
    │   For holes:     R_H = +1/(pe) > 0          │
    │                                              │
    │   → Sign of R_H tells carrier type!          │
    │   → Magnitude gives carrier density n = 1/|R_H e| │
    └─────────────────────────────────────────────┘

    Hall mobility: μ_H = R_H · σ = |R_H|/ρ_e

    Example: measure R_H = -4.7×10⁻¹⁰ m³/C for Si sample
    n-type (negative R_H)
    n = 1/(|R_H|·e) = 1/(4.7×10⁻¹⁰ × 1.6×10⁻¹⁹) = 1.33×10²⁸ m⁻³
    = 1.33×10²² cm⁻³ (heavily doped)
```

---

## Phonons and Thermal Properties

Atomic vibrations in crystals are quantized as phonons.

```
    1D diatomic chain (two masses M, m, spring constant K):
    Dispersion relation: ω² = K(M+m)/Mm ± K√[(M+m)²/M²m² - 4sin²(ka/2)/Mm]
    Two branches:
    Acoustic: ω → 0 as k → 0 (center of mass motion, sound waves)
    Optical:  ω → finite as k → 0 (opposite motion, interacts with photons)

    At k → 0 (acoustic): v_sound = a√(K/m_reduced) ≈ √(E/ρ_mass)
    Sound speed in steel: v_s = √(210×10⁹/7800) = 5188 m/s ✓
```

**Heat Capacity Models**:
- Einstein: each atom is independent quantum oscillator at ω_E
  C_V = 3Nk (ℏω_E/kT)² e^{ℏω_E/kT}/(e^{ℏω_E/kT}-1)²
  → Goes to 0 as T→0 (quantum effect), approaches 3Nk (Dulong-Petit) at high T
- Debye: continuum of acoustic phonons up to cutoff frequency ω_D
  C_V ∝ T³ at low T (Debye T³ law)
  θ_D = ℏω_D/k: Al=428K, Fe=470K, Cu=343K, Diamond=2230K

**Thermal Conductivity** (phonon-mediated, for insulators):
$$k = \frac{1}{3} C_V v_s \Lambda$$
C_V = heat capacity/volume, v_s = sound speed, Λ = phonon mean free path.

For metals: both electrons and phonons contribute; electrons dominate.
Wiedemann-Franz law: k_electron/σ_e T = L₀ = π²k_B²/(3e²) = 2.44×10⁻⁸ W·Ω/K²
(The Lorenz number L₀ is nearly universal for metals.)

---

## Bridge to Quantum Mechanics (Learner's Background)

In atomic physics the potential is spherical -> hydrogen-like eigenvalues. In a crystal the potential is periodic -> Bloch solutions and energy bands:

```
    Atomic physics: spherical potential V(r)
    → hydrogen solutions: n, l, m_l, m_s quantum numbers
    → energy levels: E_n = -13.6/n² eV for hydrogen

    Materials science: periodic potential V(r+R) = V(r)
    → Bloch solutions: ψ_{nk}(r) = u_{nk}(r) e^{ik·r}
    → energy bands: E_n(k), continuous in k
    → Brillouin zone replaces principal quantum number as primary index

    Connection:
    Isolated atoms → molecular orbitals (LCAO, 2 atoms)
                  → bonding/antibonding levels split
                  → bands (N atoms, N states per band, N → ∞)
    This is the tight-binding limit of band theory.

    The spread of atomic levels into bands:
    Core levels (1s, 2s, 2p): very little overlap → very flat bands
    Valence levels (3s, 3p, 3d, 4s): large overlap → wide bands
    → 3d transition metals: narrow d-band + wide sp band → complex DOS
    → Explains magnetism in Fe, Co, Ni (partial filling of d-band near E_F)
```

### Ferromagnetism via Band Theory

In Fe, the 3d band is split by exchange interaction:

```
    Spin-up d-band (spin ↑): shifted down in energy → more occupied
    Spin-down d-band (spin ↓): shifted up → less occupied
    → Net spin → magnetic moment ~ 2.2 μ_B per Fe atom
    → Stoner criterion for ferromagnetism: g(E_F) · I > 1
      g(E_F) = DOS at Fermi level, I = Stoner exchange integral
      Fe, Co, Ni satisfy this; Pd and Pt are close but don't
```

### Superconductivity (Brief)

Below T_c, Cooper pairs of electrons form (electron-phonon interaction):
- Paired electrons have opposite k and spin → bosonic → condense into single quantum state
- Energy gap 2Δ opens at E_F → zero resistance for currents below critical density
- BCS T_c ~ 1.13 ℏω_D exp(-1/g(E_F)V) where V = electron-phonon coupling
- High-T_c superconductors (YBCO, T_c=93K): d-wave symmetry, cuprate planes, not fully understood

---

## Mie Potential: Bonding → Elastic Modulus → Thermal Expansion

The interaction potential between two atoms:

$$U(r) = \frac{A}{r^m} - \frac{B}{r^n}$$

(Lennard-Jones: m=12, n=6 for noble gas dimers)

```
    At equilibrium r₀: dU/dr = 0 → -mA/r₀^{m+1} + nB/r₀^{n+1} = 0

    Young's modulus from bond stiffness:
    E ≈ (1/r₀) · d²U/dr² |_{r₀}
    → Stronger bonds (deep well, large d²U/dr²) → higher E
    Diamond: E = 1050 GPa   (strong covalent C-C)
    Tungsten: E = 411 GPa   (strong metallic)
    Iron:     E = 211 GPa
    Aluminum: E = 70 GPa    (weaker metallic)
    HDPE:     E = 0.8 GPa   (weak van der Waals between chains)

    Thermal expansion from potential asymmetry:
    U(r) ≈ U₀ + ½k(r-r₀)² - g(r-r₀)³ + ...  (anharmonic expansion)
    Mean position ⟨r⟩_T = r₀ + gkT/k² (shifts to larger r at higher T)
    α_thermal ∝ g/k (ratio of anharmonicity to stiffness)
    Strong bonds (symmetric wells) → low α
    Diamond: α = 1×10⁻⁶ K⁻¹, Invar (Fe-36Ni): α ≈ 1×10⁻⁶ K⁻¹ (anomaly: magnetostrictive cancellation)
    Al: α = 23×10⁻⁶ K⁻¹, Polymers: α = 100-200×10⁻⁶ K⁻¹
```

---

## Decision Cheat Sheet

| Question                             | Relevant Physics                          |
|--------------------------------------|------------------------------------------|
| Why is Al a conductor but Si not?    | Al: partially filled band; Si: full VB, E_g=1.1 eV gap |
| Why is diamond so hard?              | sp³ covalent, 3D network, highest Debye T |
| Why is steel stiff (E=210 GPa)?      | Metallic bonding, tight Fe d-orbitals     |
| Why is copper transparent in UV?     | Photon energy > plasma frequency ℏω_p ~ 10 eV |
| Why does GaAs make better laser than Si? | Direct band gap → radiative recombination |
| Why does n-type Si have R_H < 0?     | Electron carriers, Hall coefficient = -1/ne |
| Why does doping increase conductivity?| Shifts E_F into band → more carriers     |
| Why does Au look golden?             | Interband transitions starting at 2.4 eV (blue absorbed) |
| Why is SiO₂ insulating in MOSFET?   | E_g = 9 eV → no electrons thermally excited at room T |
| Why higher T → higher resistivity in metal? | More phonon scattering → shorter τ → lower σ |

---

## Common Confusion Points

**Band gap vs HOMO-LUMO gap**: Band gap (E_g) is the solid-state equivalent of HOMO-LUMO gap
in a molecule. In solids the levels spread into bands; the gap is between the highest filled
band and lowest empty band. HOMO = top of VB, LUMO = bottom of CB.

**Effective mass can be negative or anisotropic**: The effective mass is defined as the
inverse curvature of E(k). At a band MAXIMUM, the curvature is negative → m* < 0. This
describes holes. In many real materials m* is a tensor (anisotropic), e.g., Si has
longitudinal m*_l = 0.92m₀ and transverse m*_t = 0.19m₀ for its 6 conduction band valleys.

**Conductor/semiconductor distinction is not sharp**: At any finite temperature, even
an "insulator" has some thermally excited carriers. The engineering distinction is
practical: if you can't meaningfully dope or thermally excite the material at device
operating T, call it an insulator. Operationally: E_g > 3 eV = insulator for room-T electronics.

**Band theory doesn't explain everything**: Mott insulators (e.g., NiO) should be metallic
by band theory (odd number of electrons per unit cell) but are insulators because electron-electron
Coulomb repulsion (correlation) opens a Hubbard gap. Band theory (single-electron) fails for
these strongly-correlated systems. High-T superconductors fall in this category.
