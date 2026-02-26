# 15-PLASMA-FUNDAMENTALS — Plasma Physics Fundamentals

> Debye shielding, plasma frequency, single-particle motion, MHD equations,
> transport, and waves. The fourth state of matter — and why collective
> behavior makes it qualitatively different from an ionized gas.

---

## What is a Plasma?

```
A plasma is a quasi-neutral gas of charged particles that exhibits COLLECTIVE behavior.

Three conditions distinguish plasma from weakly ionized gas:
  1. QUASI-NEUTRALITY: n_e ≈ n_i  (charge neutrality over scales >> λ_D)
  2. DEBYE SHIELDING:  λ_D << system size L  (field screened beyond Debye length)
  3. COLLECTIVE:       ωₚ >> ν_collision    (plasma oscillations faster than collisions)

Plasma parameter (coupling parameter):
  Λ = n_e · λ_D³  (number of particles in Debye sphere)
  Ideal plasma: Λ >> 1  (many particles per Debye sphere → collective dominates)
  Strongly coupled: Λ < 1  (inter-particle potential > thermal energy → dense/cold)

PLASMA EXAMPLES:
  System              n_e (m⁻³)    T_e (eV)    λ_D (m)     Classification
  ──────────────────────────────────────────────────────────────────────
  Solar wind          10⁶–10⁷      10–50       10–50       Collisionless, hot
  Solar corona        10¹²–10¹³    100–200     0.001       Hot, tenuous
  Tokamak plasma      10¹⁹–10²⁰   10,000      10⁻⁴        Hot, magnetized
  Glow discharge      10¹⁶         1–3         10⁻⁴        Cold, magnetized
  Lightning bolt      10²⁰         ~1 eV       10⁻⁵        Dense, transient
  Laser-plasma        10²⁶–10²⁸   keV–MeV     10⁻⁹        Dense, hot

(1 eV = 11,605 K — plasma physicists measure temperature in energy units)
```

---

## Debye Shielding

### Derivation

A test charge q placed in a plasma is shielded by a cloud of opposite charges.

```
Poisson equation:  ∇²φ = −ρ/ε₀

Charge density (assuming Boltzmann distribution of electrons + fixed ions):
  n_e = n₀ exp(+eφ/k_BT_e)   (electrons attracted to positive potential)
  n_i = n₀ exp(−eφ/k_BT_i)   (ions repelled — or fixed if T_i → ∞)

Linearized (eφ << k_BT):
  ρ = e(n_i − n_e) ≈ −n₀e²φ(1/k_BT_e + 1/k_BT_i)

Substituting into Poisson:
  ∇²φ = φ/λ_D²

where:  1/λ_D² = n₀e²/ε₀ (1/k_BT_e + 1/k_BT_i) = 1/λ_De² + 1/λ_Di²

Solution (spherical):
  φ(r) = (q/4πε₀r) · exp(−r/λ_D)    (Yukawa / screened Coulomb potential)

Debye length:
  λ_De = √(ε₀k_BT_e / n_e e²)

  λ_De (m) = 7430 √(T_e(eV) / n_e(m⁻³))     (useful numerical formula)

Examples:
  Tokamak: T_e = 10 keV, n_e = 10²⁰ m⁻³  →  λ_D ~ 7 × 10⁻⁵ m = 70 µm
  Solar wind: T_e = 10 eV, n_e = 10⁶ m⁻³  →  λ_D ~ 7 m
```

---

## Plasma Frequency

The natural oscillation frequency of the electron fluid:

```
Derivation:
  Displace electron slab by δx → charge separation → restoring E-field
  n_e e δx = ε₀ E   →   E = n_e e δx / ε₀
  Equation of motion: m_e ẍ = −eE = −(n_e e²/m_e ε₀) x = −ωₚₑ² x

Electron plasma frequency:
  ωₚₑ = √(n_e e²/ ε₀ m_e)
  fₚₑ = ωₚₑ/2π = 9 √(n_e) Hz   (n_e in m⁻³)

Ion plasma frequency:
  ωₚᵢ = √(n_i Z²e²/ ε₀ m_i)   << ωₚₑ  (because m_i >> m_e)

Physical meaning:
  EM waves with ω < ωₚ cannot propagate in plasma (reflected/absorbed)
  → Radio waves reflected by ionosphere (f < fₚ ≈ 1–10 MHz)
  → Opacity of solar interior to certain frequencies
  → Plasma mirror for laser pulse compression
```

---

## Characteristic Scales

```
Quantity                   Formula                          Physical meaning
────────────────────────────────────────────────────────────────────────────
Debye length λ_D          √(ε₀k_BT_e/n_ee²)              Shielding scale
Plasma frequency ωₚ       √(ne²/ε₀m)                     Oscillation frequency
Cyclotron frequency Ω     eB/m  (electrons: Ωₑ; ions: Ωᵢ) Gyration about field
Larmor radius r_L         v_⊥/Ω = mv_⊥/eB               Gyration radius
Alfvén speed v_A          B/√(µ₀ρ)                        MHD wave speed
Sound speed c_s           √(γk_BT/m)                      Acoustic wave speed
Thermal speed v_th        √(k_BT/m)                       Typical particle speed
Mean free path λ_mfp      v_th/ν_collision                 Distance between collisions

Magnetization:   r_L << system scale  (plasma magnetized)
Collisionality:  λ_mfp >> system scale (collisionless limit; λ_mfp << → collisional)
```

---

## Single-Particle Motion

### Cyclotron Motion

Charged particle in uniform magnetic field B = B ẑ:

```
Equation of motion:  m(dv/dt) = q(v × B)

Solution: circular (helical) motion about field line
  v_⊥ = v_⊥₀ (cos Ωt x̂ − sin Ωt ŷ)
  v_∥ = constant (no force along B)

Cyclotron (Larmor) frequency:
  Ωₑ = eB/m_e = 1.76 × 10¹¹ B (rad/s)    (electrons)
  Ωᵢ = ZeB/m_i = 9.58 × 10⁷ ZB/A (rad/s)  (ions, Z=charge, A=mass number)

Larmor radius:
  r_L = m v_⊥ / (qB) = v_⊥ / Ω

  Electron in tokamak (T=10 keV, B=5T): r_Le ~ 0.05 mm
  Proton in tokamak: r_Li ~ 2 mm   (√(m_i/m_e) ~ 43× larger)
```

### Guiding Center Drifts

When additional forces F act on a gyrating particle, the guiding center drifts:

```
General drift formula:
  v_drift = (F × B) / (qB²)

E × B drift (most important):
  F = qE  →  v_E×B = (E × B) / B²
  SAME for ions and electrons (no q dependence) → no current, just bulk flow
  Example: radial E in tokamak → toroidal rotation of entire plasma

Gradient drift (∇B perpendicular to B):
  v_∇B = (mv_⊥²/2) (B × ∇B) / (qB³)
  Opposite sign for ions and electrons → CURRENT (drives instabilities)

Curvature drift (field line curvature):
  v_κ = (mv_∥²)(R_c × B) / (qB² R_c²)
  Opposite for ions/electrons → current

Polarization drift (time-varying E):
  v_pol = (m/qB²) dE_⊥/dt
  Ions only (m_i/m_e ratio): determines low-frequency plasma dielectric
```

### Magnetic Mirror

Particle moving along B into region of increasing |B|:

```
Adiabatic invariant (magnetic moment):
  µ = mv_⊥² / (2B) = constant  (as long as B changes slowly compared to Ωₑ)

Conservation of µ + energy → reflection condition:
  sin²θ_mirror = B_min/B_max   where θ = pitch angle = arctan(v_⊥/v_∥)

Particles with θ > θ_mirror → trapped (mirror bounce)
Particles with θ < θ_mirror → loss cone → escape

Applications:
  Earth's Van Allen radiation belts: trapped particles bounce between poles
  Magnetic mirror fusion concept (1950s) — superseded by tokamak/stellarator
  Solar wind interaction with magnetosphere: loss cone escape
```

---

## Fluid Description: MHD

When λ_mfp << L (collisional) or for large-scale (Λ >> 1) behavior, use fluid equations.

### Ideal MHD Equations

```
Continuity:    ∂ρ/∂t + ∇·(ρv) = 0

Momentum:      ρ(∂v/∂t + v·∇v) = −∇p + J×B

Ohm's law:     E + v×B = 0            (ideal: perfect conductor)

Faraday:       ∂B/∂t = −∇×E = ∇×(v×B)

Ampère (slow): ∇×B = µ₀ J            (displacement current neglected)
Gauss:         ∇·B = 0

Energy:        ∂/∂t(p/ργ) + v·∇(p/ργ) = 0   (adiabatic)

Key parameters:
  Alfvén speed:  v_A = B/√(µ₀ρ)
  Plasma beta:   β = p_thermal/p_magnetic = nk_BT/(B²/2µ₀)
```

### Resistive MHD

Real plasmas have finite resistivity η:

```
Ohm's law:  E + v×B = ηJ

Induction equation:
  ∂B/∂t = ∇×(v×B) − ∇×(ηJ) = ∇×(v×B) + (η/µ₀)∇²B

Magnetic Reynolds number:
  Rm = VL/η_m   (η_m = η/µ₀ = magnetic diffusivity)

  Rm >> 1: ideal limit, field "frozen" to fluid (flux freezing)
  Rm << 1: diffusive limit, field diffuses through fluid

Lundquist number: S = v_A L / η_m  (ratio of Alfvén transit to diffusion time)
  Tokamak: S ~ 10⁸–10¹⁰
  Solar corona: S ~ 10¹²–10¹⁴
```

### Flux Freezing (Alfvén's Theorem)

In ideal MHD: magnetic flux through any fluid element is conserved.
Field lines are "frozen into" the plasma and move with it.

```
∂B/∂t = ∇×(v×B)   →   d(Φ_B)/dt = 0   along fluid element

Physical consequence: plasma and field move together
  → B-field topology preserved (no reconnection)
  → Exception: resistive layers → reconnection → topology change (see 16-PLASMA-DYNAMICS.md)

Applications:
  Star formation: collapse of gas cloud → B-field compressed → magnetic braking
  Solar wind: B-field lines spiral outward (Parker spiral) frozen to solar wind
  MHD pumping in metallurgy: apply B → E×B drift → contactless liquid metal stirring
```

---

<!-- @editor[bridge/P2]: No old-world bridge for plasma waves — dispersion relations are the same mathematical structure as signal processing and wave optics. EM waves in plasma (cutoff at omega_p) parallel to waveguide cutoff frequencies. The learner's engineering background makes waveguide-to-plasma the natural bridge. -->
## Plasma Waves

### Wave Taxonomy

```
ELECTROMAGNETIC WAVES IN PLASMA:
  O-mode (ordinary): E ∥ k ⊥ B
    Dispersion: ω² = ωₚ² + k²c²
    Cutoff: ω < ωₚ → evanescent (reflected by ionosphere)

  X-mode (extraordinary): E ⊥ B, k ⊥ B
    Multiple cutoffs and resonances; more complex dispersion

ELECTROSTATIC WAVES (k ∥ E, no B perturbation):
  Electron plasma waves (Langmuir waves):
    ω² = ωₚₑ² + 3k²v_the²   (Bohm-Gross dispersion)
    Landau damping: electrons with v ≈ ω/k absorb wave → collisionless damping

  Ion acoustic waves:
    ω/k ≈ c_s = √(Z k_B T_e/m_i)   (like sound, driven by electron pressure)
    Undamped if T_e >> T_i

MAGNETOHYDRODYNAMIC WAVES (k ∥ B or k ⊥ B):
  Alfvén wave: transverse, k ∥ B
    ω = k v_A = k B/√(µ₀ρ)
    Non-compressive; field line tension restoring force
    Observed in: solar corona (heating?), tokamak (TAE modes), magnetosphere

  Fast magnetosonic: compressive, k ⊥ B
    v_fast = √(v_A² + c_s²)

  Slow magnetosonic: compressive, k ∥ B roughly
    v_slow < v_A, c_s  (both field and pressure restoring)

Whistler wave: right-hand circularly polarized EM wave, f between Ωᵢ and Ωₑ
  Dispersion: ω = Ωₑ cos θ (kc/ωₚ)²
  Audible in HF receivers as descending tone → lightning source
```

---

## Transport in Magnetized Plasma

```
CROSS-FIELD TRANSPORT (⊥ to B) — classical theory:
  Diffusion coefficient: D_⊥ = r_L² ν_collision
  Heat conductivity: χ_⊥ ∝ D_⊥

PARALLEL TRANSPORT (∥ to B):
  D_∥ = v_th²/ν_collision >> D_⊥ by factor (r_L/λ_mfp)²
  Highly anisotropic: parallel >> perpendicular

ANOMALOUS TRANSPORT (actual tokamak transport):
  Classical (neoclassical) theory severely underestimates actual transport
  Observed cross-field diffusion ~ 10–100× classical (Bohm diffusion: D_Bohm ∝ k_BT/eB)
  Cause: micro-turbulence (drift waves, ITG modes, TEM modes)
  Controlling turbulent transport → key challenge in fusion research
```

---

## Decision Cheat Sheet

| Question | Concept | Key formula |
|----------|---------|-------------|
| Is this gas a plasma? | Three conditions | λ_D << L, ωₚ >> ν_coll, Λ >> 1 |
| How far does a charge's field penetrate? | Debye length | λ_D = 7430 √(T_e(eV)/n_e(m⁻³)) m |
| What frequency do electrons oscillate at? | Plasma frequency | ωₚ = √(ne²/ε₀mₑ); fₚ = 9√n Hz |
| What radius does an electron gyrate? | Larmor radius | r_L = mv_⊥/eB |
| Why does the ionosphere reflect radio? | Cutoff at ωₚ | EM wave ω < ωₚ → evanescent → reflected |
| What speed do MHD waves travel? | Alfvén speed | v_A = B/√(µ₀ρ) |
| What fraction of plasma energy is in pressure vs B-field? | Plasma beta | β = nkT/(B²/2µ₀) |
| Why are field lines "frozen" to plasma? | Flux freezing | Rm >> 1 → induction >> diffusion |
| When is a particle magnetically trapped? | Loss cone | sin²θ < B_min/B_max → escapes |

---

## Common Confusion Points

**Plasma is not simply "hot gas" or "ionized gas"**
Any gas has some ionization above absolute zero. Plasma requires collective behavior
— Debye shielding, plasma oscillations, and collective response to fields.
A candle flame is weakly ionized but is NOT a plasma (Λ << 1, no collective behavior).
The fourth state distinction is about collective behavior, not ionization fraction.

**Quasi-neutrality does not mean perfect neutrality**
n_e ≈ n_i to high precision (1 part in ~10¹⁰), but small deviations generate
large electric fields that rapidly restore neutrality. The quasi-neutral approximation
breaks down at scales ≤ λ_D (sheaths, double layers).

**E×B drift carries no current**
Because it's charge-independent, E×B drift moves all species identically — no charge separation,
no current. It's a bulk flow of plasma. Gradient and curvature drifts ARE charge-dependent
and drive the azimuthal currents that cause instabilities in tokamaks.

**Landau damping has no collisions**
Classical wave damping requires collisions (viscosity, resistivity). Landau damping
is purely collisionless — particles with v ≈ vᵩₕₐₛₑ exchange energy with the wave
via resonant interaction. Particles slightly slower than the wave absorb energy;
particles slightly faster give energy. In a Maxwellian, more slow particles → net damping.
This is a fundamental kinetic effect with no fluid analog.

**MHD is a single-fluid model — it loses two-fluid and kinetic physics**
MHD treats plasma as a single conducting fluid. It cannot describe:
- Ion and electron dynamics separately
- Kinetic effects (Landau damping, wave-particle resonance)
- Collisionless reconnection
- Hall effect (important at scales below ion skin depth c/ωₚᵢ)
Extended MHD, two-fluid, and kinetic (PIC, Vlasov) models progressively add these.
