# Probability and the Boltzmann Distribution

## The Big Picture

The foundations of statistical mechanics rest on one core postulate (equal a priori probabilities for microstates) and one derivation (the Boltzmann distribution as the most probable distribution for a system in contact with a heat reservoir). From these emerge Boltzmann's entropy S = k ln Ω and the partition function Z. The derivation is essentially a constrained optimization — maximize entropy subject to a fixed average energy — which connects directly to the Jaynes maximum entropy principle and to Lagrange multipliers from constrained optimization.

```
FOUNDATIONS STRUCTURE
═══════════════════════════════════════════════════════════════════════════════

  POSTULATE:  All accessible microstates (given macrostate constraints)
              are equally probable.
                │
                ▼
  MICROSTATE COUNTING:  Ω(E, N, V) = number of microstates
                │
                ▼
  BOLTZMANN ENTROPY:  S = k_B ln Ω
                │
                ▼
  BOLTZMANN DISTRIBUTION: P(n) ∝ e^{-E_n/k_BT}
  (derived by maximizing entropy subject to fixed ⟨E⟩)
                │
                ▼
  PARTITION FUNCTION Z = Σ e^{-βE_n}
                │
                ▼
  ALL THERMODYNAMICS  (via F = −kT ln Z and derivatives)
```

---

## Microstates and Macrostates

<!-- @editor[audience/P2]: The macrostate/microstate definitions are written at introductory level — this learner knows thermodynamics. The coin example (4 coins, 2 heads) is pedagogically correct but far below the calibration level. The learner needs the *combinatorial scaling* argument (why Ω grows as e^N) to understand why fluctuations vanish in the thermodynamic limit, not a 4-coin illustration. Consider replacing with the N-coin binomial / Stirling argument that shows the Gaussian sharpening. -->

**Macrostate**: defined by macroscopic variables (N, V, T, P, ...) — what we measure.
**Microstate**: complete specification of the state of every particle (positions and momenta in classical mechanics, quantum numbers in quantum mechanics).

**Crucial asymmetry**: Many microstates correspond to the same macrostate.

```
EXAMPLE: 4 coins, each H or T
  Macrostate "2 heads":  microstates = {HHTT, HTHT, HTTH, THHT, THTH, TTHH}
                         Ω = 6
  Macrostate "4 heads":  microstates = {HHHH}
                         Ω = 1

  Entropy of "2 heads": S = k ln 6 ≈ 1.79k
  Entropy of "4 heads": S = k ln 1 = 0

  The "2 heads" state is overwhelmingly more probable — for N = 4.
  For N = 10²³, the asymmetry is so extreme that deviations from the
  maximum-entropy state are never observed.
```

**The second law**: Systems evolve toward macrostates with higher Ω. Not by any force, but by pure combinatorics — there are more ways to be in the high-entropy state.

---

## Boltzmann's S = k ln Ω

The entropy is:

    S = k_B ln Ω(E, N, V)

**Properties of S**:
1. **Additivity**: For two independent systems, Ω_total = Ω₁ × Ω₂, so S_total = S₁ + S₂.
2. **Maximum at equilibrium**: S is maximized over all accessible distributions.
3. **Third law**: Ω = 1 at T = 0 (unique ground state for nondegenerate systems), so S → 0.

**Temperature from entropy**:

    1/T = ∂S/∂E|_{N,V}    ⟹   T = (∂E/∂S)_{N,V}

Two systems in thermal contact reach equilibrium (maximum combined entropy) when:

    ∂S₁/∂E₁ = ∂S₂/∂E₂    ⟹    T₁ = T₂

This is the statistical mechanical definition of temperature: systems at the same temperature have the same (∂S/∂E).

**Pressure from entropy**:

    P/T = ∂S/∂V|_{N,E}    ⟹    P = T ∂S/∂V|_{N,E}

**Chemical potential from entropy**:

    μ/T = −∂S/∂N|_{E,V}

---

## Derivation of the Boltzmann Distribution

**Setup**: System (small, "subsystem") in contact with a large heat reservoir at temperature T. Total energy E_total = E_system + E_reservoir is fixed.

**Goal**: Find probability P(n) for the system to be in microstate n with energy E_n.

**Method**: Count the microstates of the reservoir consistent with the system being in state n.

When system is in state n (energy E_n), reservoir has energy E_R = E_total − E_n. Number of reservoir microstates:

    Ω_R(E_R) = e^{S_R(E_R)/k_B}

Taylor expand ln Ω_R around E_R = E_total (since E_n << E_total for large reservoir):

    ln Ω_R(E_total − E_n) = ln Ω_R(E_total) − (∂ ln Ω_R/∂E_R) E_n + ...
                           = const − β E_n    (where β = 1/k_BT = ∂ ln Ω_R/∂E_R)

So:

    P(n) ∝ Ω_R(E_total − E_n) ∝ e^{−β E_n}    **BOLTZMANN DISTRIBUTION**

**Normalization** gives the partition function:

    P(n) = e^{-β E_n} / Z    where Z = Σ_m e^{-β E_m}

**Key insight**: The Boltzmann distribution is entirely a property of the RESERVOIR (through β = 1/kT), not of the system. The system can be anything.

---

## Derivation via Maximum Entropy (Jaynes)

<!-- @editor[bridge/P2]: The Jaynes MaxEnt derivation is present but doesn't land the connection this learner most needs: the Lagrange multiplier β here is exactly the dual variable in a convex optimization problem (Legendre-Fenchel duality). A learner with MIT math background will recognize that the exponential family distribution is the general solution to any MaxEnt problem with linear constraints — and that this is why logistic regression, Gaussian, Poisson, and exponential distributions all take the same e^{linear} form. One sentence bridging MaxEnt → exponential family → ML would pay off. -->

Alternatively: find the distribution {p_n} that **maximizes entropy** subject to:

    Σ_n p_n = 1    (normalization)
    Σ_n p_n E_n = U    (fixed average energy)

Use Lagrange multipliers:

    maximize:  S = −k_B Σ_n p_n ln p_n
    subject to: Σ_n p_n = 1 and Σ_n p_n E_n = U

Lagrangian: L = −k_B Σ p_n ln p_n − λ₁(Σ p_n − 1) − λ₂(Σ p_n E_n − U)

∂L/∂p_n = 0:  −k_B(ln p_n + 1) − λ₁ − λ₂ E_n = 0

    ⟹  p_n = e^{−1 − λ₁/k_B} e^{−λ₂ E_n/k_B}

From normalization: identify λ₂/k_B = β = 1/(k_BT), and the first factor = 1/Z.

Result: **p_n = e^{-βE_n} / Z** — the Boltzmann distribution.

**This is the Lagrange multiplier derivation of the Boltzmann distribution**: temperature β is the Lagrange multiplier enforcing the energy constraint.

---

## The Partition Function

    Z(β, N, V) = Σ_n e^{-β E_n}    (canonical partition function)

For continuous classical systems (classical limit):

    Z = (1/h^{3N} N!) ∫ d³ᴺr d³ᴺp e^{-β H(r,p)}

The N! accounts for indistinguishability of identical particles.

**From Z, everything follows**:

| Quantity | Formula |
|---------|---------|
| Free energy | F = −k_BT ln Z |
| Internal energy | U = −∂(ln Z)/∂β = k_BT² ∂(ln Z)/∂T |
| Entropy | S = k_B(ln Z + βU) = −∂F/∂T |
| Pressure | P = k_BT ∂(ln Z)/∂V |
| Heat capacity | C_V = ∂U/∂T |

**The magic**: Z is a sum (or integral) over microscopic states. Once evaluated, all macroscopic thermodynamics follows by taking derivatives — no additional physics needed.

---

## Classical Equipartition Theorem

In the classical limit, each quadratic degree of freedom contributes k_BT/2 to the average energy:

    ⟨(1/2)ax²⟩ = k_BT/2    for any quadratic term ax² in the Hamiltonian

**Applications**:

| System | Degrees of freedom | Total ⟨E⟩ | C_V |
|--------|------------------|----------|-----|
| Monatomic gas (3D translations) | 3 translational | (3/2)Nk_BT | (3/2)Nk_B |
| Diatomic gas (classical, rigid) | 3 trans + 2 rot | (5/2)Nk_BT | (5/2)Nk_B |
| Diatomic gas (with vibration) | +2 (KE + PE) | (7/2)Nk_BT | (7/2)Nk_B |
| Harmonic oscillator | 2 (KE + PE) | k_BT | k_B |

**Failure of equipartition at low T**: When k_BT << ℏω (energy spacing of quantum levels), the quantum system does NOT satisfy equipartition. A diatomic gas at room temperature has C_V = (5/2)k_B per molecule — vibrational modes are "frozen out" (ℏω_vib >> k_BT). At very low T, even rotational modes freeze out.

This failure of equipartition is one of the historical motivations for quantum mechanics.

---

## Gibbs Entropy and Ensemble Averaging

**Gibbs entropy** (general form, works for quantum and classical):

    S_Gibbs = −k_B Σ_n P(n) ln P(n)    = k_B ⟨−ln P⟩

For the canonical ensemble:
    P(n) = e^{-βE_n}/Z
    ln P(n) = −βE_n − ln Z
    S = −k_B Σ_n P_n(−βE_n − ln Z) = k_Bβ⟨E⟩ + k_B ln Z = k_B ln Z + U/T = (U − F)/T

Which is correct: F = U − TS → S = (U − F)/T. Consistent!

**Ensemble average**:

    ⟨A⟩ = Σ_n P(n) A(n) = (1/Z) Σ_n A(n) e^{-β E_n}

**Fluctuations**:

    ⟨(ΔE)²⟩ = ⟨E²⟩ − ⟨E⟩² = k_BT² C_V

The variance of energy = k_BT² × heat capacity. Large heat capacity → large energy fluctuations. But relative fluctuations: √⟨(ΔE)²⟩/⟨E⟩ ~ 1/√N → 0 for large N (macroscopic system is self-averaging).

---

## The Maxwell-Boltzmann Speed Distribution

For an ideal gas in the classical limit, the speed distribution follows from the Boltzmann factor e^{-βp²/2m}:

**Velocity distribution**: f(**v**) = (m/2πk_BT)^{3/2} exp(−mv²/2k_BT) (Gaussian in each component)

**Speed distribution** (after integrating over all directions):

    f(v) = 4π v² (m/2πk_BT)^{3/2} e^{-mv²/2k_BT}    (Maxwell-Boltzmann distribution)

Key values:
- Most probable speed: v_p = √(2k_BT/m)
- Mean speed: ⟨v⟩ = √(8k_BT/πm) = v_p√(4/π) ≈ 1.13v_p
- RMS speed: v_rms = √(3k_BT/m) = v_p√(3/2) ≈ 1.22v_p

For N₂ at room temperature (T = 300K, m = 28 amu): v_rms ≈ 517 m/s.

---

## Decision Cheat Sheet

| Need to... | Formula |
|-----------|--------|
| Entropy of macrostate | S = k_B ln Ω |
| Probability of microstate n | P(n) = e^{-βE_n}/Z |
| Partition function | Z = Σ_n e^{-βE_n} |
| Free energy | F = −k_BT ln Z |
| Average energy from Z | U = −∂ln Z/∂β |
| Temperature definition (stat mech) | 1/T = ∂S/∂E|_{N,V} |
| Maxwell-Boltzmann speed distribution | f(v) ∝ v² e^{-mv²/2k_BT} |
| Equipartition (classical, quadratic DoF) | ⟨(1/2)ax²⟩ = k_BT/2 |

---

## Common Confusion Points

**Boltzmann distribution assumes contact with a reservoir**: The derivation requires the system to be small compared to the reservoir. For an isolated system, use the microcanonical ensemble (all microstates equally probable at fixed E). For large systems, both give the same results.

**Entropy is extensive, not intensive**: S ∝ N for large systems. Entropy per particle S/N → const. This is why ln Ω grows proportionally to N.

**The N! factor prevents the Gibbs paradox**: For classical identical particles, dividing phase space by N! accounts for indistinguishability. Without it, mixing two containers of the same gas would increase entropy — which is wrong (Gibbs paradox). The N! makes entropy extensive.

**Equipartition fails at low T for quantum systems**: The classical equipartition theorem gives each quadratic mode k_BT/2 of energy. But if the quantum level spacing ℏω >> k_BT, the mode cannot be thermally excited — it contributes nearly zero. This explains why specific heats of solids decrease at low T (Einstein and Debye models).

<!-- @editor[content/P2]: Missing: the Gibbs entropy formula S = −k Σ p_n ln p_n should be connected explicitly to Shannon entropy H = −Σ p_n log₂ p_n here at the foundations level, not deferred to 09-CONNECTIONS.md. This is where the identity is *derived* (both emerge from the same axiomatic constraints), and this learner already knows Shannon entropy. The connection at derivation time is more illuminating than a mapping table later. -->

<!-- @editor[content/P2]: The Maxwell-Boltzmann speed distribution section derives the result but never states the practical use case: it sets the scale for when quantum statistics are required (nλ³ ~ 1 is the quantum crossover). The thermal de Broglie wavelength λ = h/√(2πmkT) should appear here with the quantum criterion, not only in 04-QUANTUM-STATS.md. -->
