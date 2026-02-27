# Statistical Mechanics — Landscape and Taxonomy

## The Big Picture

Statistical mechanics is the bridge between microscopic laws (Newtonian or quantum mechanics of individual particles) and macroscopic observables (temperature, pressure, entropy, heat capacity). The central insight is that macroscopic behavior emerges from statistical properties of an astronomically large number (N ~ 10²³) of microscopic degrees of freedom. You don't need to know the trajectory of every molecule — only the probability distribution over microstates. The partition function is the key object: it encodes all thermodynamic information.

<!-- @editor[content/P2]: Overview diagram is strong but the "Ten Files" table lacks conceptual grouping — would benefit from showing which files are foundations (01–04), which are the deep physics peaks (05–06), and which are bridges to CS/ML (07–09). A two-tier index (foundations vs. advanced clusters) would help this learner route through the material more efficiently. -->

```
STATISTICAL MECHANICS — CONCEPTUAL STRUCTURE
═══════════════════════════════════════════════════════════════════════════════

  MICROSCOPIC                     STATISTICAL                  MACROSCOPIC
  (quantum or classical)          (probability)                (thermodynamics)

  Hamiltonian H(q,p)             Partition function Z         Free energy F = −kT ln Z
  Quantum states {|n⟩}           Boltzmann weights e^{-βEₙ}  Entropy S = −∂F/∂T
  Energy levels Eₙ               Ensemble averages ⟨A⟩        Internal energy U = ⟨H⟩
  Symmetry (B-E vs F-D)          Distribution functions       Equation of state p(V,T)
                                  ──────────────────────────   ──────────────────
                                  Connects atomic physics      What we measure
                                  to observations              in the lab

  THREE ENSEMBLES:
  ┌────────────────┬─────────────────────────┬────────────────────────┐
  │ Microcanonical │  fixed N, V, E           │  Z = Ω(E) (density of │
  │                │  isolated system         │  states); S = k ln Ω  │
  ├────────────────┼─────────────────────────┼────────────────────────┤
  │ Canonical      │  fixed N, V, T           │  Z = Σ e^{-βEₙ}       │
  │                │  heat bath at T          │  F = −kT ln Z         │
  ├────────────────┼─────────────────────────┼────────────────────────┤
  │ Grand canonical│  fixed μ, V, T           │  Z_G = Σ e^{-β(E−μN)} │
  │                │  heat+particle bath      │  Ω = −kT ln Z_G       │
  └────────────────┴─────────────────────────┴────────────────────────┘
```

---

## The Ten Files at a Glance

```
FILE                      CORE CONTENT
─────────────────────────────────────────────────────────────────────────
00-OVERVIEW               This file — landscape, ensembles, partition function
01-FOUNDATIONS            Boltzmann distribution, entropy, microstates
02-MICROCANONICAL         Isolated systems, density of states, ideal gas
03-CANONICAL              Canonical ensemble, partition function, Legendre structure
04-QUANTUM-STATS          Fermi-Dirac and Bose-Einstein distributions, quantum gases
05-PHASE-TRANSITIONS      Phases, Ising model, critical phenomena, universality
06-RENORMALIZATION        Wilson renormalization group, fixed points, scaling
07-ISING-MODELS           Exact Ising solutions, lattice systems, mean-field
08-NON-EQUILIBRIUM        Transport, fluctuation theorems, Langevin, Boltzmann equation
09-CONNECTIONS            Thermodynamics via Legendre transforms, information theory
```

---

## The Fundamental Question

Consider a macroscopic system (1 cm³ of gas ≈ 2.7×10¹⁹ molecules). The system has an astronomical number of microstates (specific positions and momenta of all molecules) consistent with the macrostate (given N, V, E). Statistical mechanics answers: **what macroscopic behavior emerges?**

**Boltzmann's insight** (1877): Entropy is proportional to the number of microstates:

    S = k_B ln Ω

where Ω = number of microstates consistent with the macrostate, and k_B = 1.38×10⁻²³ J/K (Boltzmann's constant).

This single equation connects macroscopic entropy (thermodynamics) to microscopic counting (statistical mechanics). It is engraved on Boltzmann's tombstone in Vienna.

---

## The Boltzmann Factor

**The most important equation in statistical mechanics**:

    P(state n) ∝ e^{-E_n / k_B T} = e^{-β E_n}    where β = 1/(k_B T)

This says: the probability of finding a system in a state with energy E_n decreases exponentially with E_n (weighted by thermal energy k_B T).

**Physical meaning**:
- High T (hot): all states roughly equally likely (exponential flattens)
- Low T (cold): low-energy states strongly favored (exponential sharp)
- At T = 0: only ground state occupied

The Boltzmann factor e^{-βE} is the mathematical foundation of:
- Classical statistical mechanics (Maxwell-Boltzmann distribution)
- Quantum statistical mechanics (Fermi-Dirac, Bose-Einstein)
- Chemical equilibrium constants (K = e^{−ΔG/RT})
- Reaction rate theory (Arrhenius: k ∝ e^{−E_a/RT})

---

## The Partition Function — Everything Follows from Z

**Canonical partition function** (fixed N, V, T):

    Z = Σ_n e^{-β E_n}  (sum over all quantum states)
    Z = ∫ d³r d³p / h³ e^{-β H(r,p)}  (classical, per particle; divide by N! for identical particles)

**All thermodynamics from Z**:

```
FROM THE PARTITION FUNCTION Z:

  Helmholtz free energy:   F = −k_B T ln Z           ← fundamental relation
  Internal energy:         U = −∂(ln Z)/∂β = k_BT²∂(ln Z)/∂T
  Entropy:                 S = −∂F/∂T = k_B(ln Z + βU)
  Pressure:                P = −∂F/∂V = k_BT ∂(ln Z)/∂V
  Heat capacity:           Cv = ∂U/∂T
  Chemical potential:      μ = ∂F/∂N

  ┌─────────────────────────────────────────────────────────────────┐
  │  ONCE YOU HAVE Z, ALL THERMODYNAMIC QUANTITIES FOLLOW           │
  │  BY DIFFERENTIATION. No need to compute them independently.     │
  └─────────────────────────────────────────────────────────────────┘
```

---

## Thermodynamic Potentials — Legendre Transform Structure

The different ensembles correspond to different Legendre transforms of the energy function. From the MIT math background: this is the same Legendre transform that appears in classical mechanics (Lagrangian ↔ Hamiltonian) and convex analysis.

```
THERMODYNAMIC POTENTIALS:

  U(S,V,N)  = internal energy  (fundamental relation: dU = TdS − PdV + μdN)

  Legendre transform on S:
  F(T,V,N) = U − TS  = Helmholtz free energy  (dF = −SdT − PdV + μdN)

  Legendre transform on V:
  H(S,P,N) = U + PV  = Enthalpy  (dH = TdS + VdP + μdN)

  Double Legendre transform:
  G(T,P,N) = U − TS + PV = Gibbs free energy  (dG = −SdT + VdP + μdN)

  Each potential is MINIMIZED at equilibrium for given control variables:
  F minimized for fixed T, V   (canonical ensemble)
  G minimized for fixed T, P   (most chemical reactions, fixed T and P)
  H minimized for fixed S, P   (adiabatic processes)
```

---

## Connections to Other Fields

### Statistical Mechanics ↔ Information Theory

Shannon entropy H = −Σ pᵢ log₂ pᵢ is the same mathematical object as Boltzmann entropy S = −k Σ pᵢ ln pᵢ (up to units: k = k_B, and a factor of ln 2 from the logarithm base).

**Jaynes Maximum Entropy Principle**: The equilibrium distribution is the one that *maximizes entropy* subject to the constraints you know. Given only ⟨E⟩ is known, MaxEnt gives the Boltzmann distribution e^{-βE}. Given also ⟨N⟩, MaxEnt gives the grand canonical distribution.

This makes statistical mechanics a special case of Bayesian inference applied to physical systems.

### Statistical Mechanics ↔ Quantum Mechanics

| Classical SM | Quantum SM |
|------------|-----------|
| Maxwell-Boltzmann (distinguishable) | Fermi-Dirac (fermions) or Bose-Einstein (bosons) |
| Phase space integral ∫ d³rd³p | Sum over quantum states Σ_n |
| Equipartition theorem | Quantum energy levels (discrete) |
| k_BT >> ℏω: classical | k_BT << ℏω: quantum (low T or high frequency) |

### Statistical Mechanics ↔ Field Theory / Renormalization

The path integral in quantum field theory is formally identical to the partition function in statistical mechanics, with imaginary time τ = iℏ/kT. Wilson's renormalization group (originally developed for critical phenomena in stat mech) became the foundational tool for modern quantum field theory.

<!-- @editor[content/P2]: This section names the QFT↔stat mech correspondence and the RG connection but does not mention the ML bridge at all — the overview's "Connections" section is incomplete given this learner's calibration. A brief pointer to stat mech → energy-based models → diffusion models as Langevin stochastic processes belongs here to complete the three-way overview. Covered deeply in 09-CONNECTIONS.md but should be surfaced at the landscape level. -->

---

## Scales and Orders of Magnitude

| System | N (particles) | Key energy scale | Interesting physics |
|--------|--------------|-----------------|---------------------|
| Ideal gas, 1 L at STP | 2.7×10²² | k_BT ≈ 0.025 eV (300K) | Equation of state |
| Electrons in metal | ~10²² | E_F ≈ 5 eV (Fermi energy) | Fermi-Dirac |
| Superconductor | ~10²² | k_BT_c ≈ 0.001 eV | Cooper pairs, BCS |
| Liquid He-4 | ~10²² | k_BT_λ ≈ 0.0002 eV | Bose-Einstein condensation |
| Neutron star | ~10⁵⁷ | E_F ~ MeV | Ultra-degenerate Fermi gas |
| CMB photons (universe) | ~10⁸⁸ | k_BT ~ 2.7 K | Bose-Einstein (photons) |

---

## Decision Cheat Sheet

| Question | Ensemble / Approach |
|---------|-------------------|
| Isolated system, fixed E, N, V | Microcanonical: S = k ln Ω |
| System at fixed T, V | Canonical: Z = Σ e^{-βEₙ}; F = −kT ln Z |
| System exchanging particles | Grand canonical: fugacity, chemical potential |
| Fermions (electrons, protons) | Fermi-Dirac: f(E) = 1/(e^{β(E-μ)}+1) |
| Bosons (photons, helium-4, phonons) | Bose-Einstein: n(E) = 1/(e^{β(E-μ)}-1) |
| Phase transitions | Ising model, Landau theory, critical exponents |
| Scale invariance, universality | Renormalization group |
| Non-equilibrium | Boltzmann equation, Langevin equation, FDT |
| Connection to information | Shannon entropy = Boltzmann entropy (same math) |

---

## Common Confusion Points

**Temperature is not a microscopic concept**: Temperature is a macroscopic quantity defined by how entropy changes with energy: 1/T = ∂S/∂E|_{N,V}. An individual particle does not have a temperature — only a large ensemble does.

**Entropy is not a measure of disorder**: The "entropy = disorder" mnemonic is pedagogically useful but technically imprecise. Entropy is k log(number of accessible microstates). Ice has lower entropy than water not because it's "more ordered" in some vague sense, but because there are fewer microstates consistent with its macrostate.

**The three ensembles give equivalent results in the thermodynamic limit**: For N → ∞, V → ∞ with N/V fixed, the microcanonical, canonical, and grand canonical ensembles give identical macroscopic predictions. They differ only for small systems or near phase transitions (where fluctuations are important).

**Boltzmann's H-theorem does not fully prove the second law**: The H-theorem shows that the Boltzmann H-function decreases over time for classical gases, establishing irreversibility from apparently reversible microscopic dynamics. But this relies on the Stosszahlansatz (molecular chaos assumption) which introduces the time asymmetry. The full statistical mechanical derivation of the second law remains a deep foundational question.

<!-- @editor[content/P2]: Missing confusion point: "Ensemble equivalence breaks near phase transitions" — the overview says ensembles give identical results for large N but doesn't flag the critical point exception, which is a key gotcha (microcanonical can show negative heat capacity in phase coexistence region; canonical cannot). This is covered in 02-MICROCANONICAL.md but should be flagged at overview level as a non-obvious trap. -->
