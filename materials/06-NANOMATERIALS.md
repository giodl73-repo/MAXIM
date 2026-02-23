# Nanomaterials and Quantum Confinement

## The Big Picture

```
    NANOMATERIALS LANDSCAPE
    ══════════════════════════════════════════════════════════

    SIZE: bulk (>100nm) → mesoscale (100nm-1μm) → nanoscale (<100nm)
                                                           │
    PHYSICS:  ─────────────────────────────────────────────┤
    Bulk: continuous bands,     │  Nanoscale: discrete E levels,
    classical transport,        │  quantum confinement,
    surface ≈ negligible        │  surface effects dominate

    DIMENSIONALITY:
    3D: bulk                    E ~ k²        g(E) ∝ E^(1/2)
    2D: thin film / QW          E ~ k_x²+k_y² g(E) = step function
    1D: nanowire / CNT          E ~ k_x²       g(E) ∝ E^(-1/2)
    0D: quantum dot             E = discrete    g(E) = δ functions

    CARBON ALLOTROPES: graphite → graphene → CNT → fullerene
    FABRICATION: top-down (lithography) → bottom-up (CVD, ALD, self-assembly)
    APPLICATIONS: displays, transistors, batteries, sensors, cancer therapy
```

---

## Quantum Confinement Physics

### When Does Quantum Confinement Matter?

Confinement becomes significant when the size L is comparable to the
de Broglie wavelength of the electron:

$$\lambda_{dB} = \frac{h}{p} = \frac{h}{\sqrt{2m^* E_F}}$$

For semiconductors (m* << m₀ and smaller E_F than metals):

```
    Si conduction band: m* = 0.26m₀
    E_F ≈ kT ≈ 0.026 eV (near band edge for lightly doped)
    λ_dB = h/√(2 × 0.26 × 9.11×10⁻³¹ × 0.026 × 1.6×10⁻¹⁹)
         = 6.63×10⁻³⁴ / √(2.43×10⁻³¹)
         = 6.63×10⁻³⁴ / 1.56×10⁻¹⁵·⁵
         ≈ 10-40 nm depending on E

    → Quantum confinement in semiconductors: L < 10-20 nm
    → For metals: much larger E_F (eV range) → λ_dB < 1 nm → must get VERY small
    → For organic molecules: already at quantum limit (bond lengths ~ 0.15 nm)
```

### Particle in a Box (Infinite Square Well)

Energy quantization in 1D box of length L:

$$E_n = \frac{n^2 h^2}{8 m^* L^2}, \quad n = 1, 2, 3, ...$$

```
    The level spacing:
    ΔE = E_2 - E_1 = 3h²/(8m*L²)
    ΔE scales as 1/L² — smaller box → larger gaps → visible at optical energies

    3D box (quantum dot, L_x = L_y = L_z = L):
    E_{n_x, n_y, n_z} = (h²/8m*L²)(n_x² + n_y² + n_z²)
    Ground state (1,1,1): E₀ = 3h²/(8m*L²)

    Example: CdSe quantum dot, L = 3 nm, m* = 0.12m₀:
    E₀ = 3×(6.63×10⁻³⁴)²/(8×0.12×9.11×10⁻³¹×(3×10⁻⁹)²)
       = 3×4.40×10⁻⁶⁷/(8×0.12×9.11×10⁻³¹×9×10⁻¹⁸)
       = 1.32×10⁻⁶⁶/7.9×10⁻⁴⁸ = 1.67×10⁻¹⁹ J = 1.04 eV
    But this is kinetic energy in the box (zero-point).
```

### Brus Equation: Size-Dependent Bandgap

For a spherical quantum dot of radius r, the effective bandgap:

$$\boxed{E_g(r) = E_g^{bulk} + \frac{\hbar^2 \pi^2}{2\mu r^2} - \frac{1.8 e^2}{4\pi\varepsilon_0 \varepsilon_r r}}$$

where:
- 1st term: bulk bandgap
- 2nd term: confinement energy (particle-in-sphere, reduced mass μ = m_e*m_h*/(m_e*+m_h*))
- 3rd term: Coulomb attraction between electron and hole (exciton correction)

```
    Dominance:
    Small r: confinement (∝ 1/r²) dominates → large blue shift
    Large r: Coulomb (∝ 1/r) competes → smaller blue shift
    Very large r: → bulk E_g recovered

    CdSe quantum dots (bulk E_g = 1.74 eV, λ_bulk = 713 nm):
    r = 1.5 nm (3 nm QD): E_g ≈ 2.9 eV → blue (λ ≈ 428 nm)
    r = 2.0 nm (4 nm QD): E_g ≈ 2.5 eV → cyan (λ ≈ 496 nm)
    r = 2.7 nm (5.4 nm QD): E_g ≈ 2.2 eV → green (λ ≈ 564 nm)
    r = 3.3 nm (6.6 nm QD): E_g ≈ 2.0 eV → orange (λ ≈ 620 nm)
    r = 4.0 nm (8 nm QD): E_g ≈ 1.8 eV → red (λ ≈ 689 nm)
    → Full visible spectrum from a single material by size control!

    Applications:
    QLED displays: InP or CdSe QDs replace conventional phosphors
    Better color gamut (narrower emission) vs YAG:Ce phosphor
    Biomedical imaging: QD labels, longer lifetime than organic dye
    Solar concentration: QD-doped windows redirect light to edges
```

---

## Density of States: Dimensional Dependence

```
    3D (bulk): g₃D(E) = (4π(2m*)^{3/2})/h³ × E^{1/2}

    2D (quantum well, one confined direction):
    g₂D(E) = m*/(πℏ²) × Σ_n θ(E - E_n)
    = step function: constant value m*/(πℏ²) for each occupied subband
    Steps occur at each quantized energy level E_n = n²h²/(8m*L²)

    1D (quantum wire, two confined directions):
    g₁D(E) = (1/πℏ)√(m*/2) × Σ_n (E - E_n)^{-1/2} θ(E - E_n)
    = Van Hove singularities: g diverges as E → E_n from above

    0D (quantum dot, three confined directions):
    g₀D(E) = 2 × Σ_n δ(E - E_n)
    = discrete delta function spikes (factor 2 for spin)

    Why this matters for devices:
    QW lasers: 2D → sharper DOS near band edge → lower threshold current density
    than bulk lasers (same number of carriers → more inverted at lasing E)
    QW HEMT: 2D electron gas (2DEG) confined at AlGaN/GaN interface
    → high density + no ionized impurity scattering → high mobility
    QD laser: 0D → ultra-sharp gain → lowest threshold, temperature-insensitive
```

---

## Carbon Allotropes

### Graphite

```
    Layer structure: sp² hybridized carbon, hexagonal (honeycomb) lattice
    In-plane: C-C = 1.42 Å (covalent, σ + π bonds)
    Interlayer: 3.35 Å (van der Waals)
    AB stacking (Bernal graphite), or ABC, or turbostratic (random)

    Properties:
    In-plane: E ≈ 1000 GPa (stiffer than steel in-plane)
    Interlayer: E ≈ 36 GPa (easy cleavage)
    σ_electrical,in-plane: 25,000 S/cm (semimetal, 2D electron gas)
    Thermal: k_in-plane ≈ 1500 W/m·K (phonon-dominated, very high)
    Uses: pencil lead, dry lubricant, electrode (batteries, capacitors, EDM)
```

### Graphene

Single layer of graphite. First isolated 2004 by Geim and Novoselov (scotch tape method).
Nobel Prize in Physics 2010.

```
    Band structure: Two atoms per unit cell (A and B sublattice)
    → Two energy bands that touch at K and K' points of BZ
    → Conical dispersion at Dirac points: E = ±ℏv_F|k|

    Fermi velocity: v_F = 1.0×10⁶ m/s ≈ c/300 (not c, but universal)
    → Massless Dirac fermions: E = v_F p (linear, not quadratic)
    → m* = 0 at neutrality point (Dirac point)

    Minimum conductivity:
    σ_min = 4e²/(πh) = 4e²/h × (1/π) ≈ 6.45 × 10⁻⁵ S (per square)
    Even at zero carrier density, graphene has finite conductivity
    (Klein tunneling through barriers → no Anderson localization)

    Ambipolar field effect: gate voltage moves E_F above (n-type) or below (p-type)
    Dirac point. Resistance maximum at CNP (charge neutrality point).

    Quantum Hall effect: at T = 4 K, B = 45 T:
    Half-integer QHE: σ_xy = 4e²/h × (n+1/2), n = 0, ±1, ±2...
    Anomalous "n+1/2" is signature of massless Dirac fermions (Berry phase π)
    Room temperature QHE also observed (unique to graphene)

    Key properties (mechanically measured):
    E ≈ 1 TPa (intrinsic stiffness — strongest material per atom)
    σ_UTS ≈ 130 GPa (theoretical)
    Thermal conductivity: k ≈ 5000 W/m·K (highest known material)
    Optical transparency: πα ≈ 2.3% per layer (α = fine structure constant)
    → Can image individual graphene layers optically (2.3% contrast on SiO₂)

    Challenges for electronics:
    Zero bandgap → cannot turn off transistor (I_off/I_on ratio poor)
    Solutions: graphene nanoribbons (GNR) — edge effects open gap
    Bilayer graphene under electric field: gap up to 0.3 eV
    Substitutional doping (N or B): shifts E_F but small gap
    Current status: graphene interconnects, transparent electrodes more practical
    than logic transistors
```

### Carbon Nanotubes (CNTs)

CNTs = rolled-up graphene sheet. Structure indexed by chiral vector (n,m).

```
    Chiral vector: C_h = n·a₁ + m·a₂
    a₁, a₂ = graphene lattice vectors (|a| = 2.46 Å)

    Diameter: d = |C_h|/π = a√(n²+nm+m²)/π = (0.0783√(n²+nm+m²)) nm

    Chirality determines electrical properties:
    n - m = 3k (k integer): METALLIC (zero bandgap)
    n - m ≠ 3k:             SEMICONDUCTOR (bandgap ∝ 1/d)

    Special cases:
    Armchair (n,n): always metallic (e.g., (10,10): d=1.36 nm)
    Zigzag (n,0): metallic if n = 3k, else semiconductor
    (10,0): n-m = 10, not divisible by 3 → semiconductor
    (12,0): n-m = 12 = 3×4 → metallic

    Bandgap for semiconducting CNT:
    E_g ≈ 2γ₀a/(√3 × d) ≈ 0.9 eV/d[nm]
    where γ₀ = 2.9 eV (C-C tight-binding overlap)
    (6,5) SWCNT: d = 0.76 nm → E_g = 0.9/0.76 = 1.18 eV

    Properties of SWCNTs:
    E (axial): 1 TPa (similar to graphene)
    σ_UTS: ~63 GPa (theoretical), ~37 GPa (measured)
    Current carrying capacity: 10⁹ A/cm² (vs 10⁶ for Cu — 1000× better)
    Thermal conductivity: k ≈ 3000-5000 W/m·K (axial)
    Ballistic transport: electrons travel without scattering in short CNTs

    MWCNT (multi-wall): outer shells are always metallic (large diameter)
    Useful for: composite reinforcement (CNT/epoxy, CNT/Al)
    Challenge: CNTs are hard to separate by chirality → mixed metallic + semiconductor
    Density gradient separation, gel chromatography: partial success
    IBM's carbon nanotube transistors (2017): E_g = 1.2 eV semiconducting CNT
    → I_on/I_off > 10⁵, performance comparable to Si at 5nm node
```

### C₆₀ Buckminsterfullerene

```
    Cage molecule: 60 C atoms, 12 pentagons + 20 hexagons (soccer ball)
    Diameter: 0.71 nm
    Symmetry: icosahedral (I_h), HOMO-LUMO gap: 1.9 eV
    Good electron acceptor (3 accessible reduction steps)
    Discovered 1985: Kroto, Curl, Smalley (Nobel 1996)
    Production: graphite arc discharge → 15% C₆₀ yield

    Functionalized fullerenes:
    PCBM [6,6]-phenyl-C61-butyric acid methyl ester: organic solar cells
    (e-acceptor in P3HT:PCBM bulk heterojunction)
    Fullerene derivatives in perovskite solar cells (ETL)
    Higher fullerenes: C₇₀, C₈₄, C₂₄₀ (large structures)
    Endohedral: metal@C₆₀ (e.g., Sc₃N@C₈₀ → spin qubit candidate)
```

---

## Fabrication: Top-Down

### Optical Lithography

```
    Resolution limit (Rayleigh criterion):
    R = k₁ · λ / NA
    k₁ = process factor (0.25 for state-of-art)
    λ = wavelength of light
    NA = numerical aperture of lens (n sinθ, max ~1.35 for water immersion)

    DUV (deep UV) ArF excimer: λ = 193 nm, NA = 1.35
    Minimum single-exposure feature: R = 0.25 × 193/1.35 = 35.7 nm
    With double patterning (DP, LELE): 17.8 nm
    With self-aligned double patterning (SADP): ~7 nm pitch

    EUV (extreme UV): λ = 13.5 nm, NA = 0.33 (current), 0.55 (High-NA)
    Single exposure: R = 0.25 × 13.5/0.33 = 10.2 nm → 3nm node features
    High-NA EUV (ASML 0.55 NA): R = 0.25 × 13.5/0.55 = 6.1 nm → beyond 2nm node
    EUV source: tin plasma from CO₂ laser pulses, 50,000 tin droplets/second
    EUV tool cost: $170M per scanner (ASML NXE:3400, 2023 ~$400M for EUV NXE:3600)

    Patterning flow:
    1. Deposit material (Si, metal, dielectric)
    2. Spin coat photoresist (PR) – chemically amplified resist (CAR), 30-100 nm thick
    3. Expose: stepper/scanner projects reticle image onto wafer
    4. Post-exposure bake: activate chemical amplification
    5. Develop: dissolve exposed (positive) or unexposed (negative) PR
    6. Etch: transfer pattern to underlying material (dry: RIE/ALE, wet: HF, KOH)
    7. Strip PR: O₂ plasma or solvent
    8. Repeat hundreds of times for full device (Intel 12-layer metal stack)
```

### Reactive Ion Etching (RIE) and Atomic Layer Etching (ALE)

```
    RIE: plasma of reactive gas (CHF₃/O₂ for SiO₂, Cl₂/BCl₃ for Al/GaN)
    → Ion bombardment (physical) + chemical reaction
    → Directional (anisotropic): vertical sidewalls
    Etch rate: 10-1000 nm/min depending on material and conditions
    Selectivity: ratio of etch rates (PR:Si or SiO₂:Si ~ 10-100:1)

    ALE (Atomic Layer Etching): digital version of RIE
    Step 1: surface modification (self-limiting, e.g., Cl₂ adsorption)
    Step 2: ion activation (remove only the modified layer, not the bulk)
    Result: ~1 atomic layer per cycle, Å-level precision
    → Required for FinFET and GAAFET fabrication at sub-10nm
```

### E-beam Lithography (EBL)

```
    Direct-write with focused electron beam (no mask)
    Resolution: 10 nm (limited by forward scattering and SE range)
    Sub-5 nm features in research (PMMA resist, cold development)
    Throughput: ~1 cm²/hr (vs 100 wafers/hr for optical)
    → Research, photomask writing, not production

    PMMA resist (poly(methyl methacrylate)):
    E-beam breaks chain → smaller fragments → more soluble in MIBK/IPA developer
    Positive-tone: exposed area develops away
    Resolution: <10 nm possible with optimized conditions
```

---

## Fabrication: Bottom-Up

### Chemical Vapor Deposition (CVD)

```
    Gas phase precursors → surface reaction → thin film or nanomaterial
    Graphene CVD (on Cu foil): CH₄ + H₂ at 1000°C
    Cu catalyzes C-H bond breaking → surface diffusion → graphene nucleation
    Large-area (30×30 inch) graphene for transparent electrodes

    CNT CVD: Fe nanoparticle catalyst + CH₄/C₂H₂ at 600-900°C
    SiNW (silicon nanowire): VLS (vapor-liquid-solid) with Au catalyst + SiH₄
    Au catalyst forms eutectic droplet → absorbs Si → nanowire grows below

    Plasma-Enhanced CVD (PECVD):
    Lower deposition T (200-400°C vs 600-1000°C for thermal CVD)
    Used for SiN_x, SiO₂, a-Si in CMOS (temperature-sensitive layers)

    MOCVD (Metal-Organic CVD): epitaxial III-V compound semiconductors
    GaN from Ga(CH₃)₃ + NH₃ at 1000°C on sapphire or SiC substrate
    InGaN (LED active layer): TMIn + TMGa + NH₃, In content sets wavelength
    Wafer: 4-6 inch GaN-on-sapphire, 150 layers, 3h growth → ~100 LED dice/wafer
```

### Atomic Layer Deposition (ALD)

```
    Self-limiting sequential surface reactions:
    Cycle 1: expose precursor A (e.g., TMA = Al(CH₃)₃) → saturates surface
             purge excess A
    Cycle 2: expose precursor B (e.g., H₂O) → reacts with surface-bound A
             purge → Al₂O₃ monolayer formed
    Repeat: one cycle ≈ 1-2 Å of Al₂O₃ (0.9 Å/cycle for thermal ALD)

    Self-limiting nature: each step saturates → no more deposition once all surface sites react
    → Perfect conformality (covers high-aspect-ratio features)
    → Sub-Å precision of thickness
    → Uniform composition (no step-coverage issues of sputtering)

    Key ALD materials:
    Al₂O₃: gate dielectric, moisture barrier, passivation
    HfO₂: high-κ gate oxide (Intel 45nm 2007 onward, replacing SiO₂)
    TiN, TaN, W: diffusion barriers, contacts, fill
    ZnO: transparent conductor, TCO
    Pt, Ru: noble metal electrodes
    Li₃PO₄, LiPON: solid electrolytes for thin-film batteries

    Applications: DRAM capacitors (HfO₂ ALD, 1000:1 aspect ratio),
    FinFET gate dielectric (HfO₂ by ALD), solar cell passivation (Al₂O₃ on Si)
```

### Molecular Beam Epitaxy (MBE)

```
    Ultra-high vacuum (10⁻¹⁰ torr) deposition of single-crystal thin films
    Elemental sources (effusion cells) heated to evaporate → molecular beams → substrate
    One monolayer at a time (0.28 nm/s for GaAs)
    Real-time monitoring: RHEED (reflection high-energy electron diffraction)
    → Oscillations in RHEED intensity = layer-by-layer growth

    Key capabilities:
    1. Atomic-scale control of composition and doping profiles
    2. Ultra-sharp heterointerfaces (< 1 ML transition)
    3. In-situ analysis (Auger, mass spec, RHEED)
    4. Complex quantum well superlattice structures

    Examples:
    AlGaAs/GaAs quantum well heterostructure (HEMT): modulation doping →
    2DEG mobility > 10⁶ cm²/V·s at 4K (no impurity scattering)
    InGaAs/AlInAs HEMTs: highest f_T transistors for mm-wave applications
    Topological insulator films (Bi₂Se₃, Bi₂Te₃): pristine surface states
    Magnetic superlattices (Fe/Cr): discovery of GMR (Nobel 2007)
```

---

## MEMS: Micro-Electro-Mechanical Systems

```
    Coupling of electrical and mechanical function on silicon chip.
    Fabricated by MEMS-specific processes (bulk and surface micromachining).

    CANTILEVER RESONATOR:
    Silicon beam anchored at one end, free at other.
    Resonant frequency: f₀ = (1/2π)√(k/m_eff) ≈ (1/2π)√(Ewh³/4L³ × 1/0.24ρhwL)

    For rectangular Si cantilever (width w, thickness h, length L):
    f₀ = (1.875²/2πL²)√(EI/ρA) ≈ (h/L²)√(E/12ρ) × constant
    Example: L=100μm, h=1μm, w=10μm, E=170 GPa, ρ=2330 kg/m³:
    f₀ ≈ 500 kHz (in vacuum)

    Applications: AFM cantilevers, mass sensors (fg sensitivity!),
    RF filters, gyroscopes

    THIN FILM STRESS:
    When depositing thin film on substrate, film stress causes wafer bowing.
    Stoney's equation: σ_f = (E_s h_s²) / (6(1-ν_s) h_f R)
    σ_f = film biaxial stress, E_s = substrate modulus, h_s = substrate thickness,
    h_f = film thickness, R = wafer radius of curvature

    MEMS GYROSCOPE (phone/car stability):
    Vibrating MEMS mass in Coriolis effect:
    F_Coriolis = 2m(v × Ω) where Ω = rotation rate
    Drive mode: oscillate mass at resonant frequency
    Sense mode: perpendicular displacement measured by capacitance change
    Resolution: ~0.001°/s (MEMS), vs 0.00001°/s (ring laser gyro)
    Cost: $1-$10 (MEMS) vs $10,000-$100,000 (laser gyro)
```

---

## Li-ion Battery Nanostructuring

Battery performance is fundamentally limited by solid-state transport at the nanoscale.

```
    STANDARD LI-ION CELL:
    Cathode: LiCoO₂ (LCO) or NMC (LiNi₀.₈Mn₀.₁Co₀.₁O₂)
    Anode: graphite (layered carbon, LiC₆)
    Electrolyte: LiPF₆ in EC/DMC (organic, 10⁻² S/cm at 25°C)
    Separator: polyolefin membrane

    Rate capability limited by:
    1. Li-ion diffusion in electrode particles: D_Li ≈ 10⁻¹² cm²/s (cathode)
    2. Solid electrolyte interface (SEI) formation on anode

    Nanostructuring benefits:
    Smaller particles → shorter diffusion path → faster charge/discharge
    Characteristic diffusion time: t = L²/D (L = particle radius)
    Graphite (8μm radius): t = (8×10⁻⁶)²/10⁻¹⁴ = 6400 s ≈ 2h (1C rate limited)
    Nanoparticle (50 nm radius): t = (50×10⁻⁹)²/10⁻¹⁴ = 0.25 s (much faster!)

    SILICON ANODE NANOSTRUCTURING:
    Si theoretical capacity: 3579 mAh/g (vs 372 mAh/g for graphite)
    → 10× improvement possible if Si could work
    Problem: Si expands 300% on lithiation (Li₃.₇₅Si)
    → Pulverization after few cycles → capacity fade

    Solutions:
    1. Si nanowires (Y. Cui, Stanford 2008): can accommodate strain along length
       L_nanowire > diameter → expansion along L → no pulverization
    2. Si nanoparticles (< 150 nm critical radius): fracture toughness criterion
       K_IC/σ_expansion > √(π a_c) → small enough not to crack
    3. Hollow Si nanostructures: void absorbs expansion (Cui group)
    4. Si in carbon matrix: confining + conducting matrix
    Commercial: Tesla 4680 cell uses ~5% Si in graphite anode

    LFP NANOSTRUCTURING (LiFePO₄):
    LFP: safe, cycle-stable, good rate capability
    Native conductivity: σ_electronic = 10⁻⁹ S/cm (insulating)
    Nanoparticles (50-100 nm) + C coating → electronic network
    → SONY/A123 LFP: 100nm particles → competitive with NMC for power cells
    Used in: power tools, Chinese EV market (BYD Blade battery)
```

---

## Decision Cheat Sheet

| Application                    | Nanomaterial             | Why                                |
|-------------------------------|-------------------------|------------------------------------|
| QLED display (color tunable)  | CdSe/ZnS QD            | Size-tunable color, narrow emission|
| Transparent electrode          | Graphene, ITO           | 2.3%/layer absorption, conductive  |
| CNT composite reinforcement    | MWCNT + polymer          | 1 TPa modulus, kg/g vs GPa/g       |
| Drug delivery                  | Lipid NP, PLGA NP       | Size controls uptake, targeting     |
| Catalyst (HER, CO₂RR)         | Pt NP on CNT/graphene   | High surface area, exposed sites    |
| MEMS sensor                    | Si microfabrication     | Batch manufacturing, CMOS integrate |
| Li-ion anode (high capacity)  | Si nanowire/nanoparticle | Overcome expansion problem          |
| Gate dielectric (high-κ)       | HfO₂ by ALD             | Reduces leakage, same capacitance   |
| Biosensor                      | ZnO NW, graphene FET    | Surface sensitivity, fast response |
| Cancer therapy (thermal)       | Fe₃O₄ NP (SPIONs)       | Magnetic hyperthermia, MRI contrast |

---

## Common Confusion Points

**"Nano" doesn't always mean quantum**: A 100 nm gold nanoparticle has a size-dependent
localized surface plasmon resonance (LSPR — classical electromagnetic effect), but its
electronic properties are essentially bulk. True quantum confinement (discrete levels)
requires L < 10 nm for most semiconductors. The term "nanomaterial" covers both regimes.

**Graphene ≠ graphite ≠ carbon fiber**: Graphene is a single atomic layer of sp² carbon.
Graphite is multi-layer graphene with weak interlayer vdW coupling. Carbon fiber is
polycrystalline graphitic fiber made from PAN precursor with crystallites oriented along
fiber axis — not graphene. Carbon fiber strength comes from the oriented sp² network,
but it's not a quantum material.

**Quantum dots are not bulk semiconductor pieces**: Their optical and electronic properties
are fundamentally different from bulk because the discrete energy levels arise from
confinement. The "semiconductor" label is maintained because the material (CdSe, InP, etc.)
is the same, but the physics is quantum-dot physics. A 3nm CdSe QD absorbs blue light;
bulk CdSe absorbs red (E_g = 1.74 eV).

**ALD is slow but that's the point**: ALD deposits ~1 Å per cycle, ~100 cycles/min maximum.
That's ~10 nm/min — far slower than sputtering (100-1000 nm/min). But the self-limiting
mechanism guarantees perfect conformality over high-aspect-ratio features (capacitor trenches
with 50:1 aspect ratio, FinFET gate oxides). Sputtering can't do this — it deposits on
line-of-sight surfaces only. For <3nm conformal films, ALD is the only option.
