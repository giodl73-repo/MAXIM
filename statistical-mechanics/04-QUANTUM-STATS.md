# Quantum Statistics: Fermi-Dirac and Bose-Einstein

## The Big Picture

Classical particles are distinguishable; quantum particles are not. Swapping two identical
quantum particles either multiplies the wavefunction by +1 (bosons) or −1 (fermions) — and
this single sign difference produces two entirely different statistics. Fermions obey the
Pauli exclusion principle and pile up below the Fermi energy; bosons can all pile into the
ground state (Bose-Einstein condensation). Photons and phonons are bosons with zero chemical
potential. Electrons in metals are fermions with a Fermi energy that governs all their
low-temperature behavior.

```
QUANTUM STATISTICS LANDSCAPE
═══════════════════════════════════════════════════════════════════════════════

  PARTICLE SYMMETRY UNDER EXCHANGE:

  ψ(x₁,x₂) = +ψ(x₂,x₁)  BOSONS:   integer spin (0, 1, 2, ...)
                                     photons, phonons, ⁴He, W/Z bosons
                                     ANY number in a single quantum state

  ψ(x₁,x₂) = −ψ(x₂,x₁)  FERMIONS: half-integer spin (1/2, 3/2, ...)
                                     electrons, protons, neutrons, quarks
                                     AT MOST ONE per quantum state (Pauli)

  ┌─────────────────────┬────────────────────┬────────────────────────────┐
  │                     │ BOSONS             │ FERMIONS                   │
  ├─────────────────────┼────────────────────┼────────────────────────────┤
  │ Mean occupation     │ n(ε) = 1/(e^{β(ε-μ)}-1) │ n(ε) = 1/(e^{β(ε-μ)}+1) │
  │ Distribution        │ Bose-Einstein      │ Fermi-Dirac                │
  │ Occupation at ε=μ   │ → ∞ (diverges)    │ = 1/2                      │
  │ T=0 occupancy       │ all in ground state│ 1 for ε<μ, 0 for ε>μ      │
  │ Low-density limit   │ Maxwell-Boltzmann  │ Maxwell-Boltzmann          │
  │ Signature behavior  │ BEC, superfluidity │ Fermi pressure, metal e⁻   │
  └─────────────────────┴────────────────────┴────────────────────────────┘
```

---

## Why Symmetry Determines Statistics

### The Derivation from the Grand Canonical Ensemble

Consider a single quantum mode (state) with energy ε. The mode can be occupied by 0, 1, 2, ... particles. The grand canonical partition function for this mode:

**Fermions** (Pauli: occupation n ∈ {0, 1} only):

    z_F = Σ_{n=0}^{1} e^{-β(ε−μ)n} = 1 + e^{-β(ε−μ)}

**Bosons** (occupation n ∈ {0, 1, 2, ...}):

    z_B = Σ_{n=0}^{∞} e^{-β(ε−μ)n} = 1 / (1 − e^{-β(ε−μ)})    (geometric series, valid for μ < ε)

**Mean occupation** ⟨n⟩ = −∂(ln z)/∂(βε):

    FERMIONS:  ⟨n_F⟩ = 1 / (e^{β(ε−μ)} + 1)    [FERMI-DIRAC DISTRIBUTION]
    BOSONS:    ⟨n_B⟩ = 1 / (e^{β(ε−μ)} − 1)    [BOSE-EINSTEIN DISTRIBUTION]

The +1 vs −1 in the denominator is the sole difference — arising from Pauli exclusion (occupation ≤ 1 for fermions). Everything else follows.

```
GEOMETRIC INTERPRETATION:

  FERMIONS: mode is either empty or occupied.
  ┌────┬────┐
  │ 0  │ 1  │
  └────┴────┘
  Average: between 0 and 1, S-shaped as function of ε.

  BOSONS: mode can have any occupation.
  ┌────┬────┬────┬────┬────┬────┐
  │ 0  │ 1  │ 2  │ 3  │ 4  │...│
  └────┴────┴────┴────┴────┴────┘
  Average: diverges as ε → μ from above (ε > μ required).

  CLASSICAL LIMIT (e^{β(ε−μ)} >> 1):
  Both → n ≈ e^{-β(ε−μ)} = e^{βμ} e^{-βε}   (Maxwell-Boltzmann)
  Classical statistics is the low-density, high-temperature limit.
```

---

## Fermi-Dirac Statistics and the Fermi Gas

### The Fermi Function

    f(ε) = 1 / (e^{β(ε−μ)} + 1)

Properties:
- f(ε) ∈ (0, 1) always
- f(μ) = 1/2 always (regardless of T)
- At T = 0: f(ε) = θ(μ−ε) (step function — sharp Fermi surface)
- Width of transition region: ~4k_BT around μ (from Taylor expansion)

### Fermi Energy and Fermi Level

**Fermi energy E_F**: the chemical potential at T = 0.

For non-interacting electrons in a box (free electron model), fix electron density n = N/V.

Density of states in 3D: g(ε) = (V/2π²)(2m/ℏ²)^{3/2} √ε × (2 for spin)

Number equation at T = 0:

    N = ∫_0^{E_F} g(ε) dε    ⟹    E_F = (ℏ²/2m)(3π²n)^{2/3}

```
FERMI ENERGY FOR ELECTRONS IN METALS:
  n ~ 10²⁸ m⁻³ (for Cu, n = 8.5×10²⁸ m⁻³)
  E_F ~ 5−10 eV
  T_F = E_F/k_B ~ 50,000−100,000 K

  Room temperature T = 300 K << T_F.
  Electrons are DEEPLY degenerate: k_BT/E_F ≈ 0.006.
  Nearly all electrons are in states below E_F.
  Only electrons within ~k_BT of E_F are thermally active.
```

### Low-Temperature Expansion (Sommerfeld Expansion)

Any integral I = ∫₀^∞ φ(ε) f(ε) dε at low T can be expanded in powers of (k_BT/E_F):

    I = ∫₀^μ φ(ε) dε + (π²/6)(k_BT)² φ'(μ) + (7π⁴/360)(k_BT)⁴ φ'''(μ) + ...

This is the **Sommerfeld expansion**. Applying to the total energy U of a Fermi gas:

    U = (3/5) N E_F [1 + (5π²/12)(k_BT/E_F)² + ...]
    C_V = (π²/2) N k_B (k_BT/E_F) + ...    ← linear in T

```
SOMMERFELD RESULT: C_V = γ T    (electronic heat capacity)
  γ = π² N k_B² / (2 E_F)  = π² k_B²/(2) × g(E_F) × V

  This LINEAR-IN-T heat capacity is the fingerprint of a Fermi gas.
  At very low T, it dominates over the Debye phonon contribution (T³).

  BRIDGE TO EXPERIMENTS:
  Measuring C_V/T at low T:
  C_V/T = γ + A T²
  Intercept γ → electronic density of states g(E_F)
  Slope A → Debye phonon contribution (3D: A = 12π⁴Nk_B/5T_D³)
```

### Fermi Pressure at Zero Temperature

Even at T = 0, a Fermi gas has nonzero pressure (Fermi pressure or degeneracy pressure):

    P = (2/3)(U/V) = (2/5)(N/V) E_F ∝ n^{5/3}

This is purely quantum-mechanical — it arises from Pauli exclusion forcing electrons into high-energy states, not from thermal motion.

**White dwarf and neutron star stability**: Fermi pressure of electrons (white dwarfs) or neutrons (neutron stars) supports them against gravitational collapse. A white dwarf is a degenerate Fermi gas. When the mass exceeds the Chandrasekhar limit (~1.4 M_☉), relativistic effects reduce the Fermi pressure exponent from 5/3 to 4/3, insufficient to support the star.

---

## Bose-Einstein Statistics and Condensation

### The Bose Function

    n_B(ε) = 1 / (e^{β(ε−μ)} − 1)

Constraints:
- μ < ε_min (= 0 for ground state) always; otherwise n_B would diverge or go negative
- n_B(ε) → ∞ as ε → μ+ (occupation diverges at the chemical potential)
- At high T, μ is very negative; μ → 0 as T → T_c (BEC transition)

### Bose-Einstein Condensation

**Setup**: N non-interacting bosons in a box of volume V. The total number is:

    N = Σ_k n_B(ε_k) = N_excited + N_0

where N_0 is the occupation of the ground state (ε = 0) and N_excited counts excited states.

**Critical temperature T_c**: The maximum number of excited-state bosons (with μ = 0) is:

    N_excited^{max}(T) = ∫_0^∞ g(ε) n_B(ε)|_{μ=0} dε ∝ T^{3/2} (in 3D)

Setting N_excited^{max}(T_c) = N:

    k_B T_c = (2πℏ²/m)(n/ζ(3/2))^{2/3}    where ζ(3/2) ≈ 2.612

```
BEC MECHANISM:

  T > T_c:  All N bosons in excited states. μ < 0.
  T = T_c:  μ reaches 0. Excited states are "full" for the given N.
  T < T_c:  Excess bosons (N − N_excited) accumulate in ground state.

  Ground state occupation below T_c:
  N_0 / N = 1 − (T/T_c)^{3/2}    (fraction in BEC)

  At T = 0: ALL N bosons in ground state.

  This is a MACROSCOPIC occupation of a single quantum state.
  The ground state wavefunction becomes macroscopically coherent:
  ψ_0 acts like a classical field with definite phase.
  → SUPERFLUIDITY, LASER COHERENCE (for photons), SUPERCONDUCTIVITY analog.
```

### Real BEC: Dilute Atomic Gases

First achieved in 1995 (Cornell, Wieman — ⁸⁷Rb; Ketterle — Na). Nobel Prize 2001.

```
EXPERIMENTAL ROUTE TO BEC:
  Laser cooling → T ~ μK (laser slowing and Doppler cooling)
  Magnetic trapping → harmonic potential V(r) = (1/2)mω²r²
  Evaporative cooling → T ~ nK, n ~ 10¹⁴ cm⁻³
  BEC: T_c ~ 100 nK for typical densities

  For a HARMONIC TRAP (not a box), density of states g(ε) ∝ ε².
  BEC transition: k_BT_c = ℏω̄ (N/ζ(3))^{1/3}  where ω̄ = (ωₓω_yω_z)^{1/3}
  Below T_c: N_0/N = 1 − (T/T_c)³ (different exponent from box: 3 vs 3/2)
```

---

## Photons and Phonons — Bosons with μ = 0

Photons and phonons are bosons, but they have **no conservation law** for particle number. Therefore μ = 0 — there is no Lagrange multiplier enforcing ⟨N⟩ = const.

**Planck distribution** (photons in thermal equilibrium, Blackbody radiation):

    ⟨n⟩ = 1 / (e^{βℏω} − 1)    (μ = 0 Bose-Einstein)

Energy density per unit frequency:

    u(ω) = (ℏω³/π²c³) / (e^{βℏω} − 1)    (Planck spectral distribution)

```
PLANCK vs CLASSICAL RAYLEIGH-JEANS:
  Classical (μ → 0 in equipartition): u(ω) → k_BT ω²/π²c³  (diverges!)
  Quantum (Planck):                   u(ω) → Planck cutoff
                                      → resolves the ULTRAVIOLET CATASTROPHE

  Wien's law: peak at ω_max = 2.82 k_BT/ℏ  (λ_max T = 2.9 mm·K)
  Stefan-Boltzmann: total radiated power P = σT⁴  (σ = 5.67×10⁻⁸ W/m²K⁴)
```

**Debye model** (phonons — sound quanta): Same Bose-Einstein form, but phonons have a finite bandwidth (Debye cutoff ω_D). At low T:

    C_V = (12π⁴/5) Nk_B (T/T_D)³    (Debye T³ law)

where T_D = ℏω_D/k_B is the Debye temperature.

---

## Spin Statistics Theorem

**Why bosons → +1 and fermions → −1 under exchange?** The spin-statistics theorem (Pauli 1940, proof via QFT): in any relativistic quantum field theory, integer-spin particles are bosons and half-integer-spin particles are fermions.

The proof requires:
1. Lorentz invariance
2. Causality (commutators vanish outside light cone)
3. Positive-definite energy

The proof is notoriously non-trivial — Feynman called it "one of the most important but least well-explained results" in physics. The key insight: the canonical commutation relations (bosons) and anticommutation relations (fermions) are not chosen by hand — they are forced by the joint requirements of Lorentz invariance and microcausality (fields at spacelike separation must commute or anticommute). Assuming the wrong statistics — bosonic electrons or fermionic photons — gives negative-norm states (negative probabilities) or an energy spectrum unbounded below.

```
SPIN-STATISTICS THEOREM:

  Spin 0, 1, 2, ...: BOSONS    (symmetric wavefunction)
  Spin 1/2, 3/2, ...: FERMIONS  (antisymmetric wavefunction)

  Consequence — PAULI EXCLUSION:
  Antisymmetric ψ(x₁,x₂) = −ψ(x₂,x₁) implies ψ(x,x) = 0.
  Two fermions cannot be in the same state (same position AND same spin).
  This is why matter is rigid — you cannot compress electrons.
```

---

## Comparing the Three Distributions

```
OCCUPATION vs ENERGY:

  ε ≪ μ:
  Fermi-Dirac:    n_F → 1  (filled)
  Bose-Einstein:  n_B → large (piling up)
  Maxwell-Boltzmann: e^{β(μ−ε)} → large (but wrong regime for MB)

  ε = μ:
  Fermi-Dirac:    n_F = 1/2
  Bose-Einstein:  n_B → ∞

  ε ≫ μ  (β(ε−μ) >> 1, classical limit):
  Fermi-Dirac:    n_F ≈ e^{-β(ε−μ)}  (MB)
  Bose-Einstein:  n_B ≈ e^{-β(ε−μ)}  (MB)
  Both → Maxwell-Boltzmann: n_MB = e^{β(μ−ε)}

  Classical limit valid when n λ³ << 1  (phase space density << 1 per cell)
  where λ = h/√(2πmkT) is the thermal de Broglie wavelength.
```

| Property | Fermi-Dirac | Bose-Einstein | Maxwell-Boltzmann |
|---------|------------|--------------|------------------|
| Spin | half-integer | integer | (classical limit) |
| Max occupation | 1 (Pauli) | ∞ | ∞ |
| μ at T=0 | = E_F > 0 | = ε_min = 0 | −∞ |
| Phase transition | none (cross-over) | BEC at T_c | — |
| Examples | e⁻, p, n in metal/star | photons, phonons, ⁴He | hot dilute gas |
| T=0 behavior | filled Fermi sea | all in ground state | collapses to ground |

---

## Decision Cheat Sheet

| Need to... | Formula |
|-----------|--------|
| Mean occupation of fermion mode ε | n_F = 1/(e^{β(ε-μ)}+1) |
| Mean occupation of boson mode ε | n_B = 1/(e^{β(ε-μ)}-1) |
| Classical limit (both) | n ≈ e^{-β(ε-μ)} when e^{β(ε-μ)} >> 1 |
| Fermi energy (3D free electrons) | E_F = (ℏ²/2m)(3π²n)^{2/3} |
| Electronic heat capacity | C_V = (π²/2)Nk_B(T/T_F) (linear in T) |
| BEC critical temperature (box) | k_BT_c = (2πℏ²/m)(n/ζ(3/2))^{2/3} |
| BEC ground state fraction | N_0/N = 1−(T/T_c)^{3/2} |
| Planck distribution | ⟨n⟩ = 1/(e^{βℏω}−1) with μ=0 |
| Fermi pressure at T=0 | P = (2/5)(N/V)E_F |

---

## Common Confusion Points

**Chemical potential μ for photons/phonons is zero — but why?** Photon number is not conserved (emission and absorption are allowed). When you minimize F over particle number, ∂F/∂N = μ = 0 — there's no constraint to enforce. For bosons that are conserved (⁴He, cold atoms), μ is real and negative, approaching zero at T_c.

**The Fermi energy is the chemical potential at T=0, not at finite T**: At finite T, the chemical potential μ(T) shifts slightly from E_F. For metals: μ(T) ≈ E_F[1 − (π²/12)(k_BT/E_F)² + ...]. The shift is tiny because T << T_F for metals.

**BEC does not require interactions**: Ideal non-interacting bosons show BEC. In real systems (liquid ⁴He, cold atoms), interactions modify the transition temperature but BEC still occurs. The key physics is purely quantum statistical — macroscopic occupation of the ground state.

**The Gross-Pitaevskii equation connects BEC to superfluidity**: For a weakly interacting condensate, the macroscopic wavefunction Ψ(r,t) satisfies the Gross-Pitaevskii equation: iℏ ∂Ψ/∂t = [−ℏ²∇²/(2m) + V(r) + g|Ψ|² ] Ψ, where g = 4πℏ²a_s/m (a_s = s-wave scattering length). This is a nonlinear Schrödinger equation — the condensate is a classical field whose phase gradient carries the superfluid current: v_s = (ℏ/m)∇φ. The GP equation is where BEC connects to superfluidity, vortices, and soliton dynamics.

**The Fermi-Dirac function is the logistic sigmoid**: The Fermi function f(ε) = 1/(e^{β(ε−μ)}+1) is exactly σ(β(μ−ε)) where σ(x) = 1/(1+e^{-x}) is the logistic sigmoid used as the activation function in neural networks. In an RBM (restricted Boltzmann machine), the conditional probability P(h_j = 1 | v) = σ(W_j·v + c_j) is literally Fermi-Dirac occupancy with β = 1 and effective chemical potential μ = W_j·v + c_j. The correspondence is exact, not approximate.

**The classical limit is NOT "high temperature" in general**: The classical limit requires nλ³ << 1 (low phase-space density). High T reduces λ ∝ T^{-1/2}, which helps, but also high T with high density can still be quantum. A neutron star at T = 10⁸ K is still deeply quantum (degenerate) because n is huge.
