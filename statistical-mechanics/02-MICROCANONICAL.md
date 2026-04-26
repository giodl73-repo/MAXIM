# Microcanonical Ensemble

## The Big Picture

The microcanonical ensemble is the foundational ensemble: an isolated system with fixed energy
E, volume V, and particle number N. No energy or particles are exchanged with any reservoir.
The fundamental postulate says all accessible microstates are equally probable. Entropy S = k ln Ω
then follows immediately. The second law becomes a counting theorem: systems evolve toward
macrostates with the most microstates, because those are overwhelmingly more probable.

```
MICROCANONICAL ENSEMBLE — STRUCTURE
═══════════════════════════════════════════════════════════════════════════════

  ISOLATED SYSTEM: (N, V, E) all fixed
  ┌─────────────────────────────────────────────────────────────────┐
  │                                                                 │
  │   FUNDAMENTAL POSTULATE:                                        │
  │   All microstates with energy E ± δE are equally probable.      │
  │                                                                 │
  │   Ω(E, N, V) = number of microstates in [E, E+δE]               │
  │                                                                 │
  │   S(E, N, V) = k_B ln Ω(E, N, V)        ← BOLTZMANN ENTROPY     │
  │                                                                 │
  │   From S, recover all of thermodynamics:                        │
  │   1/T = ∂S/∂E|_{N,V}     P/T = ∂S/∂V|_{N,E}                   │
  │   μ = −T ∂S/∂N|_{E,V}    (chemical potential)                   │
  │                                                                 │
  └─────────────────────────────────────────────────────────────────┘

  KEY OBJECTS:
  ┌──────────────────────┬──────────────────────────────────────────┐
  │ Ω(E, N, V)           │ density of states Ω(E) or g(E)           │
  │ number of microstates│ Ω = ∫ d³ᴺr d³ᴺp δ(H − E) / (h³ᴺ N!)   │
  ├──────────────────────┼──────────────────────────────────────────┤
  │ S = k_B ln Ω         │ entropy from counting                    │
  ├──────────────────────┼──────────────────────────────────────────┤
  │ 1/T = ∂S/∂E          │ temperature from entropy slope           │
  ├──────────────────────┼──────────────────────────────────────────┤
  │ C_V = T ∂S/∂T = ∂U/∂T│ heat capacity from U(T) = U(E(T))       │
  └──────────────────────┴──────────────────────────────────────────┘
```

---

## Counting Microstates — Classical Phase Space

For a classical system of N particles in 3D with Hamiltonian H(q, p):

**Phase space volume** in the shell [E, E + δE]:

    Ω(E) = (1 / h³ᴺ N!) ∫_{E < H < E+δE} d³ᴺq d³ᴺp

The factors:
- **h³ᴺ**: Heisenberg uncertainty principle — each phase space cell has volume h³ per dimension. This makes Ω dimensionless.
- **N!**: identical particles are indistinguishable — permuting them gives the same physical microstate.

**Cumulative phase space volume** Φ(E) = number of states with H < E:

    Φ(E) = (1 / h³ᴺ N!) ∫_{H < E} d³ᴺq d³ᴺp

So Ω(E) = (∂Φ/∂E) δE (with the energy shell width δE, which drops out of all physical quantities since we take logs).

---

## Ideal Gas — Microcanonical Calculation

The ideal gas is the paradigmatic exactly-solvable microcanonical system. Hamiltonian:

    H = Σᵢ pᵢ²/(2m)     (N particles, 3D, no interactions)

**Phase space integral**: The energy constraint H = E defines a 3N-dimensional hypersphere of radius R = √(2mE) in momentum space, with surface area proportional to R^{3N-1}.

    Φ(E) = V^N / (h³ᴺ N!) × (volume of 3N-dimensional sphere of radius √(2mE))
          = V^N / (h³ᴺ N!) × π^{3N/2} (2mE)^{3N/2} / Γ(3N/2 + 1)

Taking the surface area (δ-function on energy shell):

    Ω(E) ∝ V^N E^{3N/2 - 1} / (h³ᴺ N!) × (2πm)^{3N/2} / Γ(3N/2)

**Entropy** (using Stirling: ln(N!) ≈ N ln N − N):

    S = k_B ln Ω = Nk_B [ln(V/N) + (3/2) ln(2πmE/3Nk_B) + (5/2)] + const

This is the **Sackur-Tetrode equation** for the entropy of an ideal gas.

**Temperature from 1/T = ∂S/∂E|_{N,V}**:

    1/T = k_B (3N/2) / E    ⟹    E = (3/2) Nk_BT    ✓ (equipartition)

**Pressure from P/T = ∂S/∂V|_{N,E}**:

    P/T = Nk_B/V    ⟹    PV = Nk_BT    ✓ (ideal gas law)

Both of these emerge from pure counting — no dynamics, no forces, just geometry of phase space.

---

## The Density of States

The density of states g(E) is the number of microstates per unit energy:

    g(E) = dΩ/dE = dΦ/dE

For N non-interacting quantum particles, the energy levels are discrete, and:

    g(E) = Σ_n δ(E − E_n)

For a 3D ideal gas, the single-particle density of states (energy range [ε, ε+dε]):

    g₁(ε) = (V / 4π²) (2m/ℏ²)^{3/2} √ε = (3N/2) N(ε)/ε ... depends on normalization

The **many-body** density of states grows as:

    g(E) ∝ E^{3N/2 - 1}    (for N ideal gas particles)

This enormous growth with E is why the entropy S = k ln Ω grows with energy, and why
systems absorb heat without decreasing entropy: Ω grows so fast that even transferring
energy to a system dramatically increases the number of accessible microstates.

```
DENSITY OF STATES g(E) FOR DIFFERENT SYSTEMS:

  3D ideal gas:      g(E) ∝ E^{3N/2 - 1}  (polynomial, huge exponent)
  1D harmonic osc:   g(E) = const          (equally spaced levels)
  2D harmonic osc:   g(E) ∝ E              (linearly increasing)
  3D harmonic osc:   g(E) ∝ E²             (quadratically increasing)
  Spin-1/2 chain:    g(E) = C(N, N/2+E/2Δ) (combinatorial, peaks at E=0)

  The rate of growth of g(E) with E determines the heat capacity C_V.
  Slow growth → small C_V. Fast growth → large C_V.
```

---

## The Second Law from Counting

The argument below is maximum likelihood estimation in disguise: maximizing Ω_total = Ω_A(E_A) × Ω_B(E − E_A) over E_A is maximizing a product of probabilities (a likelihood). Taking logarithms converts the product to a sum — the log-likelihood — and the optimality condition ∂ ln Ω_A/∂E_A = ∂ ln Ω_B/∂E_B is the score equation. Temperature equality at equilibrium is the MLE solution.

**Setup**: Two systems A and B, initially isolated at energies E_A and E_B, then allowed to exchange energy (total E = E_A + E_B is fixed).

The total number of microstates:

    Ω_total(E_A) = Ω_A(E_A) × Ω_B(E − E_A)

Equilibrium = the value of E_A that **maximizes** Ω_total.

Setting ∂ln Ω_total/∂E_A = 0:

    ∂ ln Ω_A / ∂E_A = ∂ ln Ω_B / ∂E_B    ⟹    1/T_A = 1/T_B    ⟹    T_A = T_B

```
SECOND LAW AS PROBABILITY:

  Before contact:
  E_A = E_A^{init}  (one particular split)
  E_B = E − E_A^{init}

  After contact:
  System explores ALL energy splits consistent with E_A + E_B = E.
  The probability of split E_A is:
  P(E_A) ∝ Ω_A(E_A) × Ω_B(E − E_A)

  ┌────────────────────────────────────────────────────────┐
  │  Ω_total peaks ENORMOUSLY at E_A = E_A^{eq}.           │
  │  For N ~ 10²³, the peak is so sharp (width ~ N^{-1/2}) │
  │  that deviations from equilibrium are never observed.  │
  │                                                        │
  │  The second law is NOT a fundamental law.              │
  │  It is an overwhelming probabilistic tendency.         │
  └────────────────────────────────────────────────────────┘
```

**Quantifying the peak**: For two ideal gas systems each with N particles:

    ln Ω_total(E_A) = const + (3N/2) ln E_A + (3N/2) ln(E − E_A)

This is a sum of logs peaked at E_A = E/2 with Gaussian width ΔE_A/E ~ 1/√N.

For N = 10²³: relative width ≈ 10⁻¹¹·⁵. The deviation from equilibrium is thermodynamically unobservable.

---

## Negative Temperature and Population Inversion

The microcanonical ensemble allows formal **negative temperatures** when Ω(E) is a decreasing function of E.

For a spin-1/2 system in a magnetic field (energy bounded above):

```
SPIN-1/2 SYSTEM: N spins, each ±1 in field B
  Energy: E = −μB Σᵢ sᵢ ∈ [−NμB, +NμB]

  Ω(E) = C(N, N/2 + E/2μB)  (binomial coefficient)
  Peaks at E = 0, falls off on both sides.

  For E < 0 (most spins aligned with field):
  ∂S/∂E > 0  ⟹  T > 0   (normal)

  For E > 0 (most spins anti-aligned, INVERTED POPULATION):
  ∂S/∂E < 0  ⟹  T < 0   (negative temperature)

  Negative T is HOTTER than +∞.  Order:
  0 K < ... < 300 K < ... < +∞ = −∞ < ... < −300 K < 0 K
  (cyclic in β = 1/kT, not in T itself)
```

**Laser physics**: Population inversion (negative temperature spin system coupled to photon field) is the mechanism behind laser gain. The energy flows from the negative-T spin system to the positive-T photon field — from the "hotter" to the "colder" system, consistent with entropy maximization.

---

## Microcanonical vs. Canonical — When They Differ

```
ENSEMBLE EQUIVALENCE (thermodynamic limit N → ∞):
  In the thermodynamic limit, all ensembles give identical results.
  They differ for:

  1. SMALL SYSTEMS (N ~ 1–100):
     Fluctuations are large. Microcanonical: exact fixed E.
     Canonical: energy fluctuates by ~√N relative to N → O(1/√N) relative.
     For N = 10, this matters.

  2. FIRST-ORDER PHASE TRANSITIONS:
     Canonical: forbidden region of ⟨E⟩ (latent heat gap).
     Microcanonical: S(E) has a convex dip — negative heat capacity is possible
     in finite systems. Caloric curve T(E) can be non-monotone.

  3. LONG-RANGE INTERACTIONS (gravity, plasma):
     Ensemble non-equivalence persists even in the thermodynamic limit.
     Self-gravitating systems can have negative heat capacity in the
     microcanonical ensemble (gravo-thermal catastrophe).
```

**Negative heat capacity in the microcanonical ensemble**: For self-gravitating clusters (star clusters, galaxy clusters), adding energy (injecting kinetic energy) causes the system to contract and heat up, radiating more energy than injected. The Jeans instability and gravo-thermal catastrophe are microcanonical phenomena with no canonical analog.

---

## Quantum Microcanonical — Counting Discrete Levels

For quantum systems, the energy spectrum is discrete. The microcanonical ensemble counts quantum states in [E, E+δE]:

    Ω(E) = number of energy eigenstates with E_n ∈ [E, E+δE]

**Harmonic oscillator ladder** (1D, energy spacing ℏω):

    E_n = ℏω(n + 1/2),    n = 0, 1, 2, ...
    g(E) = 1/ℏω  (constant density of states)
    S = k_B ln(E/ℏω + const) = k_B ln(n)

**3D harmonic crystal (Einstein model)**: 3N oscillators at the same frequency ω.

    Ω(E) = C(E/ℏω + 3N − 1, 3N − 1)  (distributing n quanta among 3N oscillators)

At high T (k_BT >> ℏω): Ω grows polynomially → equipartition → C_V = 3Nk_B (Dulong-Petit).
At low T (k_BT << ℏω): Ω ~ e^{-ℏω/k_BT} → quantum freeze-out → C_V → 0.

**The Debye model** improves on Einstein by using a spectrum of frequencies ω_k (phonons) up to a Debye cutoff ω_D. The density of states goes as g(ω) ∝ ω² for ω < ω_D. This gives C_V ∝ T³ at low T — observed in all crystalline solids.

**Why C_V ∝ T³ follows from g(ω) ∝ ω²**: The total energy U = ∫₀^{ω_D} ℏω × g(ω) × n_BE(ω) dω where n_BE = 1/(e^{βℏω}−1). At low T (βℏω_D >> 1), the upper limit extends to ∞ and the substitution x = βℏω gives U ∝ T^4 ∫₀^∞ x³/(e^x−1) dx, so C_V = ∂U/∂T ∝ T³. The exponent 3 = d+1−1 for d = 3 with g(ω) ∝ ω^{d-1}. The g(ω) ∝ ω² density of states from the table above directly determines the low-T power law.

---

## Decision Cheat Sheet

| Need to... | Formula / Approach |
|-----------|-------------------|
| Find entropy of isolated system | S = k_B ln Ω(E, N, V) |
| Count microstates of ideal gas | Phase space sphere surface area ∝ E^{3N/2-1} |
| Recover temperature | 1/T = ∂S/∂E|_{N,V} |
| Recover pressure | P/T = ∂S/∂V|_{N,E} |
| Prove second law | Maximize Ω_A(E_A)×Ω_B(E-E_A); equilibrium at T_A = T_B |
| Ideal gas entropy | Sackur-Tetrode: S = Nk_B[ln(V/N) + (3/2)ln(4πmE/3Nh²) + 5/2] |
| Negative temperature | ∂S/∂E < 0 → T < 0 (inverted population) |
| Low-T heat capacity | Count quantum energy levels; Einstein → exp decay; Debye → T³ |

---

## Common Confusion Points

**The energy shell width δE drops out**: The entropy is S = k_B ln Ω where Ω counts states in a shell [E, E+δE]. Changing δE changes Ω by an additive O(ln δE) term, negligible compared to O(N). So thermodynamic results are independent of δE.

**N! is not optional for classical identical particles**: Without N!, the entropy of an ideal gas is not extensive (Gibbs paradox): mixing two identical gases would increase entropy, which is wrong. The N! factor is a classical approximation to the quantum indistinguishability that forbids permuted states from being distinct.

**Microcanonical negative heat capacity is real, not pathological**: In gravitational systems, energy and temperature can move in opposite directions. Adding energy causes collapse and heating. This is not an error — it is the gravo-thermal catastrophe, responsible for core collapse of globular clusters. The canonical ensemble conceals this by coupling to a heat bath that prevents the instability.

**The second law holds statistically, not absolutely**: In a finite system at finite time, the entropy can decrease by a small amount. The fluctuation theorems (Jarzynski, Crooks) quantify exactly how probable such violations are: P(ΔS > 0)/P(ΔS < 0) = e^{|ΔS|/k_B}. For macroscopic ΔS, the ratio is e^{10²³} — violations are never observed in practice but are logically possible.
