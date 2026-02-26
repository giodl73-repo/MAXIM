# Quantum Field Theory — Dirac, Feynman, Schwinger, Tomonaga, Yang, Mills

## The Synthesis: Combining QM with Special Relativity

Quantum mechanics (1925–1930) worked perfectly for non-relativistic atoms.
But atoms also emit photons — and photon emission/absorption requires a relativistic
theory. Extending QM to be relativistically consistent led to quantum field theory.

```
THE QFT PROGRAM
===============

PROBLEM: Schrödinger equation is non-relativistic (first order in time,
  second order in space — asymmetric). At high energies, need SR.

DIRAC (1928): Relativistic wave equation for spin-1/2 particles.
  Automatically predicts spin. Predicts ANTIMATTER (positron, 1932).

JORDAN + PAULI (1928): "Second quantization" — fields are quantized,
  not just particles. The number of particles can change.
  Photon emission = creation of a photon quantum from the EM field.

QED PROBLEM (1930–1947):
  Naive calculations of electron self-energy (photon emission + reabsorption)
  give INFINITE answers.

RENORMALIZATION (1947–1949):
  Tomonaga, Schwinger, Feynman each independently show how to remove infinities.
  The technique: absorb infinities into redefinitions of mass and charge.
  Nobel Prize 1965 (Tomonaga, Schwinger, Feynman).

YANG-MILLS (1954): Generalize electromagnetism to non-abelian gauge theories.
  Leads (eventually) to the Standard Model.
```

---

## Paul Dirac (1902–1984)

### Who He Was

British physicist, Cambridge. Among the most mathematically creative physicists
in history. Nobel Prize 1933 (with Schrödinger). Famously antisocial ("Dirac"
became a unit at Cambridge for one word per hour). Said of him: "There is no
God, and Dirac is His prophet."

His *Principles of Quantum Mechanics* (1930) remains a masterwork of mathematical
presentation.

### The Contribution: The Dirac Equation and Antimatter

**The Dirac Equation (1928)**

```
DIRAC'S REASONING
=================

Schrödinger: iℏ ∂ψ/∂t = Ĥψ
  H = p²/2m (non-relativistic)
  First order in t, second order in x — not Lorentz covariant.

Klein-Gordon: -ℏ² ∂²ψ/∂t² = [(-iℏ∇)²c² + m²c⁴]ψ
  Second order in t AND x — Lorentz covariant.
  Problem: predicts NEGATIVE probabilities (|ψ|² can go negative).

Dirac's idea: Find an equation that is FIRST ORDER in both t and x.
  This requires a matrix equation.

THE DIRAC EQUATION:
  (iℏγᵘ∂_μ - mc)ψ = 0

  γᵘ are the Dirac matrices (4×4):
    γ⁰γᵘ + γᵘγ⁰ = 2g^(μν) (anticommutation relations)
    This is the algebra of a Clifford algebra.

  ψ is a 4-component spinor (not a scalar or ordinary vector).

AUTOMATIC PREDICTIONS:
  1. Electron spin = ℏ/2 (not assumed — it falls out of the 4-component structure)
  2. g-factor = 2 (magnetic moment = 2× what naive spin would give)
     Actually measured: g = 2.00231930... (computed to 12 decimal places in QED)
  3. ANTIMATTER: The equation has solutions with NEGATIVE ENERGY.
```

**Antimatter — The Prediction**

```
DIRAC'S PREDICTION OF ANTIMATTER
==================================

The Dirac equation has positive energy solutions (E > 0) AND negative energy
solutions (E < 0). What do the negative energy solutions mean?

Dirac's "sea" interpretation (1929):
  All negative energy states are FILLED by electrons (Pauli exclusion).
  If one negative-energy electron absorbs a photon and jumps to positive energy,
  it leaves a "hole" in the sea.
  The hole behaves like a particle with positive charge and electron mass.

Carl Anderson (1932): Observed this particle in cloud chamber cosmic ray tracks.
  The positron (anti-electron).

MODERN INTERPRETATION (Feynman/Stückelberg):
  A positron = an electron traveling backward in time.
  Antimatter = matter with time-reversed charge flow.
  (Not mystical — just how the mathematics works out in QFT.)

CONSEQUENCES:
  Every particle has a corresponding antiparticle.
  Particle + antiparticle → annihilate to photons (E = 2mc²).
  The Big Bang created equal matter and antimatter — slight asymmetry
  (CP violation) explains why matter dominates today.
```

**Dirac Delta Function and Dirac Notation**

```
OTHER DIRAC CONTRIBUTIONS
==========================

Dirac delta function: δ(x)
  "Function" that is zero everywhere except at x=0, where it's infinite,
  and integrates to 1: ∫ δ(x) dx = 1

  Formally: a distribution, not a function.
  Used in: QM (position eigenstates), signal processing (impulse response),
  Green's functions for PDEs, probability theory.

Dirac notation (bra-ket):
  |ψ⟩ = "ket" (column vector / state vector)
  ⟨ψ| = "bra" (row vector / dual)
  ⟨φ|ψ⟩ = inner product (probability amplitude)
  |ψ⟩⟨ψ| = projection operator (measurement)

  Used in: ALL of quantum mechanics, quantum information, quantum computing.
  Every quantum circuit simulator, every quantum algorithm uses Dirac notation.
```

---

## Richard Feynman (1918–1988)

### Who He Was

American physicist, Caltech. Nobel Prize 1965. Worked on the Manhattan Project
(cracking safes at Los Alamos for fun). Developed Feynman diagrams and path integrals.
Also did pioneering work in: superfluidity (liquid helium), parton model (quarks),
quantum computing (proposed quantum computers in 1982).
Famously known for his teaching (Feynman Lectures on Physics).

### The Contribution: Path Integrals and QED Renormalization

**Feynman Diagrams**

```
FEYNMAN DIAGRAMS
=================

A Feynman diagram is a picture of a quantum process and a COMPUTATIONAL RECIPE.

Electron-electron scattering (QED):

  e⁻ ──────•─────── e⁻          "Lowest order" diagram
            |
           γ (virtual photon)
            |
  e⁻ ──────•─────── e⁻

Each vertex: multiply by coupling constant α^(1/2)
  (α = e²/4πε₀ℏc ≈ 1/137 — the fine structure constant)

Rules (Feynman rules):
  External fermion line entering: u(p) (spinor)
  External fermion line leaving: ū(p) (adjoint spinor)
  Internal photon propagator: -ig_μν/k²
  Vertex: -ieγᵘ (electromagnetic coupling)
  Integrate over undetermined momenta

HIGHER ORDER CORRECTIONS:
  More complex diagrams with more vertices → higher powers of α.
  Since α ≈ 1/137 << 1, higher-order corrections are small.
  QED is a perturbation theory in α.

Feynman diagrams are not just pictures — each diagram has an exact mathematical
value (a complex number contributing to the amplitude).
The amplitude squared gives the probability.
```

**Path Integral Formulation**

```
FEYNMAN'S PATH INTEGRAL
========================

Classical mechanics: particle takes ONE path (the one that extremizes action).
Quantum mechanics: particle takes ALL paths simultaneously.

The probability amplitude for going from x_i to x_f is:
  ⟨x_f|e^(-iĤt/ℏ)|x_i⟩ = ∫ Dx(t) · exp(iS[x(t)]/ℏ)

  The integral is over ALL paths x(t) connecting x_i to x_f.
  Each path contributes a phase factor exp(iS/ℏ).

For ℏ → 0 (classical limit):
  Paths with S near the minimum contribute coherently.
  Paths with S far from minimum have wildly varying phases → cancel.
  The classical path (extremal action) dominates.
  → Classical mechanics recovered.

For quantum processes:
  Paths near the classical path contribute.
  But quantum tunneling comes from paths that "go through" the barrier
  with imaginary action (Euclidean path integral).

This formulation:
  - Connects QM directly to classical mechanics
  - Makes the classical limit transparent
  - Is the natural language for quantum field theory (QFT path integrals)
  - Is used in lattice QCD (numerical computations in QFT)
  - Underlies Feynman's derivation of QED renormalization
```

**QED Renormalization — The Infinity Problem and Its Solution**

```
THE INFINITY PROBLEM
=====================

Self-energy of electron: e⁻ emits a virtual photon and reabsorbs it.
  Compute the energy shift: integrate over all photon momenta k.
  The integral diverges logarithmically! ∫ dk/k → ∞

RENORMALIZATION (Tomonaga, Schwinger, Feynman, 1947–1949):
  The "bare" electron mass m₀ and charge e₀ we started with are NOT
  the physical mass m and charge e.
  Physical mass = bare mass + infinite correction.
  But: m₀ is ALSO infinite, in just the right way to cancel.
  The DIFFERENCE (physical measured quantities) is finite.

  This is not a trick — it's the statement that we can only ever measure
  dressed (renormalized) quantities, never bare ones.
  The theory must be expressed in terms of measurable quantities.

PREDICTIONS:
  Anomalous magnetic moment of electron:
    g/2 = 1 + α/2π + ... (QED expansion)
    Theoretical: 1.00115965218178 ± 0.00000000000028
    Experimental: 1.00115965218059 ± 0.00000000000028

  Agreement to 12 decimal places — the most precisely tested theory in physics.
```

---

## Julian Schwinger (1918–1994) and Sin-Itiro Tomonaga (1906–1979)

### Who They Were

Schwinger (American, Harvard) and Tomonaga (Japanese, Tokyo) independently
developed renormalized QED — simultaneously with Feynman but using different,
more mathematically rigorous methods.

Schwinger's approach: operator methods, Green's functions, generating functionals.
Tomonaga's approach: covariant perturbation theory (wartime Japan, 1943–1947).

Freeman Dyson showed all three approaches (Feynman's diagrams, Schwinger's operators,
Tomonaga's covariant perturbation) were mathematically equivalent.

The 1965 Nobel Prize in Physics: Tomonaga, Schwinger, Feynman.

Schwinger is also responsible for: source theory (an alternative to diagrams),
the Schwinger effect (pair production in strong electric fields), and the
Dyson-Schwinger equations (exact QFT relations).

---

## Chen-Ning Yang (1922– ) and Robert Mills (1927–1999)

### Who They Were

Yang: Chinese-American physicist, Institute for Advanced Study Princeton,
later SUNY Stony Brook. Nobel Prize 1957 (with Lee, for parity violation).

Mills: American physicist, short collaboration with Yang before turning to
other work.

### The Contribution: Yang-Mills Gauge Theory

**Gauge Invariance in Electromagnetism**

```
GAUGE SYMMETRY (ELECTROMAGNETISM)
===================================

Maxwell's equations are invariant under:
  A_μ → A_μ + ∂_μ Λ  (shift the 4-potential by a gradient)

This is a U(1) gauge transformation — multiplying the electron field by
a phase that can vary in space and time:
  ψ → e^(iα(x))ψ

The electromagnetic field A_μ adjusts to keep the equations invariant.
The photon is the "gauge boson" — the particle mediating the U(1) symmetry.

U(1) gauge group = complex numbers of modulus 1 = circle group.
It is ABELIAN: e^(iα) · e^(iβ) = e^(iβ) · e^(iα).
```

**Yang-Mills: Non-Abelian Gauge Theory (1954)**

```
YANG-MILLS THEORY
==================

Yang and Mills asked: What if the gauge group is NON-ABELIAN?

Replace U(1) with SU(2) (2×2 unitary matrices with det=1):
  ψ → g(x)ψ   where g(x) ∈ SU(2)
  A_μ → g A_μ g⁻¹ - (i/g) (∂_μg)g⁻¹  (more complex transformation)

The "gauge bosons" for SU(2) come in a TRIPLET (W⁺, W⁻, W⁰)
  and are themselves charged — they interact with each other.
  (Unlike photons, which don't interact with each other.)

PROBLEM: Naively, gauge bosons are massless. W and Z bosons
  (weak force carriers) are massive.
  Solution: HIGGS MECHANISM (Higgs, Brout, Englert, 1964)
  The Higgs field gives mass to gauge bosons while preserving gauge invariance.

THE STANDARD MODEL:
  U(1)_Y × SU(2)_L × SU(3)_C

  - U(1)_Y: Hypercharge (Bᵘ boson)
  - SU(2)_L: Weak isospin (W¹,W²,W³ bosons)
    Combined with U(1): Electroweak = W±, Z⁰, γ (Weinberg-Salam-Glashow)
  - SU(3)_C: Color charge (8 gluons) → QCD

  The Higgs field breaks SU(2)_L × U(1)_Y to U(1)_em.
  This gives W and Z their masses; photon remains massless.

Every particle physics experiment since 1970 tests Yang-Mills theories.
```

---

## Comparison Table

| Figure | Dates | Core Contribution | Mathematical Depth | Legacy |
|--------|-------|-------------------|--------------------|--------|
| **Dirac** | 1902–1984 | Dirac equation, antimatter, Dirac notation | Clifford algebras, spinors | All of relativistic QM, antimatter |
| **Feynman** | 1918–1988 | Path integrals, Feynman diagrams, QED | Functional integrals | QFT computations, quantum computing |
| **Schwinger** | 1918–1994 | QED renormalization (operator method) | Green's functions | QFT formalism |
| **Tomonaga** | 1906–1979 | QED renormalization (covariant) | Relativistic perturbation | QFT |
| **Yang + Mills** | 1922–, 1927–1999 | Non-abelian gauge theories | Lie groups, fiber bundles | Standard Model |

---

## Who to Cite for What

| Concept | Cite | Notes |
|---------|------|-------|
| Dirac equation (relativistic QM) | Dirac | 1928 |
| Antimatter prediction (positron) | Dirac | 1929 (discovered by Anderson 1932) |
| Dirac delta function | Dirac | |
| Bra-ket notation | Dirac | *Principles of QM* 1930 |
| Path integral formulation of QM | Feynman | 1948 |
| Feynman diagrams | Feynman | 1949 |
| QED renormalization | Tomonaga + Schwinger + Feynman | 1947–1949 |
| Fine structure constant α ≈ 1/137 | Sommerfeld (named) | Appears in Dirac/QED |
| Yang-Mills gauge theory | Yang + Mills | 1954 |
| Gauge symmetry → force carriers | Yang-Mills → Standard Model | SU(3)×SU(2)×U(1) |

---

## Common Confusion Points

**"Feynman diagrams are just pictures"** — They are precisely defined calculational
tools with Feynman rules. Each line, vertex, and propagator has an exact mathematical
value. The diagram summarizes an integral; the rules tell you exactly what integral
to compute. They are pictures of mathematics, not illustrations.

**"Renormalization is sweeping infinities under the rug"** — This was Dirac's criticism.
The modern view (Wilson's effective field theory): renormalization is about the
relevant degrees of freedom at a given scale. QED is a low-energy effective theory.
At high energies, new physics appears. The divergences signal the breakdown of the
theory at some scale (the Planck scale, presumably). This is not cheating — it's
physics at the relevant energy scale.

**"The Standard Model is the Theory of Everything"** — It is the most accurate theory
in physics, covering all known particles and three of four forces. It excludes:
gravity (GR is not quantized in the Standard Model), dark matter, dark energy, and
does not explain the matter-antimatter asymmetry or the hierarchy problem. It is
extraordinarily successful but incomplete.

**"Virtual particles are real"** — Virtual particles are internal lines in Feynman
diagrams. They are off-shell (don't satisfy E² = p²c² + m²c⁴). They are a
calculational fiction. You cannot observe a virtual particle — only the net
effect of all diagrams at a given order. The "Casimir effect" is sometimes
attributed to virtual photons, but it can be computed without any reference
to them.
