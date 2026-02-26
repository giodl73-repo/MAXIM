# Quantum Pioneers — Planck, Bohr, De Broglie, Heisenberg, Schrödinger, Born, Pauli

## The Quantum Crisis

Classical physics in 1900 was considered nearly complete. Two "small clouds"
remained on the horizon (Lord Kelvin's phrase). Those clouds destroyed classical
physics.

```
THE TWO PROBLEMS THAT BROKE CLASSICAL PHYSICS
===============================================

PROBLEM 1: BLACKBODY RADIATION
  A blackbody absorbs all incident radiation and re-emits based on temperature.
  Classical prediction (Rayleigh-Jeans): intensity ∝ f² → diverges at high f.
  ("Ultraviolet catastrophe" — classical physics predicts infinite energy.)
  Planck's fix (1900): energy comes in discrete packets ε = hf. Finite.

PROBLEM 2: PHOTOELECTRIC EFFECT
  Shine light on metal. Electrons are ejected with kinetic energy
  independent of light intensity, depending on frequency.
  Classical wave theory: more intensity → more energy → higher-KE electrons.
  Observation: more intensity → more electrons, not higher energy.
  Einstein's fix (1905): light is made of photons. E_photon = hf.

Both fixes require: E = hf (energy = Planck's constant × frequency).
h = 6.626 × 10⁻³⁴ J·s (Planck's constant) — a new constant of nature.
```

---

## Max Planck (1858–1947)

### Who He Was

German theoretical physicist. Kaiser Wilhelm Society. Nobel Prize 1918.
Lost his son Erwin to the Nazis (executed for alleged complicity in the
1944 assassination plot against Hitler). Remained in Germany throughout.
His constant h is in every quantum formula.

### The Contribution: Quantization of Energy

**The Blackbody Problem and Planck's Desperate Fix**

```
THE BLACKBODY SPECTRUM
=======================

Classical (Rayleigh-Jeans): u(f,T) = (8πf²/c³) · kT
  Works at low frequency. Diverges as f → ∞ ("ultraviolet catastrophe").

Wien's law (empirical): u(f,T) = (8πhf³/c³) · exp(-hf/kT)
  Works at high frequency. Wrong at low frequency.

Planck (1900): u(f,T) = (8πhf³/c³) · 1/(exp(hf/kT) - 1)

  This is the Planck distribution. It:
    - Reduces to Rayleigh-Jeans for hf << kT (low frequency)
    - Reduces to Wien for hf >> kT (high frequency)
    - Fits all observations perfectly

THE KEY ASSUMPTION:
  Oscillators in the blackbody wall can only have energies E = nhf
  for integer n = 0, 1, 2, ...
  Energy comes in "quanta" of size hf.
  This is not classical — classically, energy is continuous.

Planck himself called it "an act of desperation" — he didn't believe
it was physically real. He thought he was just doing a mathematical trick.
Einstein (1905) took it seriously and applied it to light itself.
```

---

## Niels Bohr (1885–1962)

### Who He Was

Danish physicist. Nobel Prize 1922. Created the Copenhagen Interpretation
of quantum mechanics. Ran the Institute for Theoretical Physics in Copenhagen
(now the Niels Bohr Institute) which was the center of quantum mechanics
development in the 1920s.

### The Contribution: The Bohr Model and Complementarity

**The Bohr Model of the Hydrogen Atom (1913)**

```
BOHR MODEL
===========

Rutherford (1911) showed: atoms have a tiny massive nucleus.
Problem: Classical EM says electrons orbiting a nucleus would
  RADIATE ENERGY continuously and spiral into the nucleus in ~10⁻¹¹ seconds.
  Obviously wrong — atoms are stable.

Bohr's postulates:
  1. Electrons occupy only discrete orbits with angular momentum L = nℏ (n = 1,2,3,...)
     ℏ = h/2π = 1.055 × 10⁻³⁴ J·s (reduced Planck constant)

  2. Electrons in allowed orbits do NOT radiate. (Ad hoc — no classical justification.)

  3. Atoms emit/absorb radiation only when electrons jump between orbits:
     E_photon = hf = E_n₁ - E_n₂

Energy levels: E_n = -13.6 eV / n²  (for hydrogen)
  (13.6 eV = ionization energy of hydrogen)

BALMER SERIES (visible light from hydrogen):
  n = 3 → 2: λ = 656 nm (red)
  n = 4 → 2: λ = 486 nm (blue-green)
  These match observations EXACTLY.
```

The Bohr model is WRONG as a physical model (electrons are not in orbits).
But it gave exactly the right energy levels for hydrogen. Its success
demanded explanation — which came from de Broglie and Schrödinger.

**The Copenhagen Interpretation and Complementarity**

Bohr's philosophical contribution: the Copenhagen interpretation.

```
BOHR'S COMPLEMENTARITY
========================

Wave-particle duality: particles behave like waves in some experiments,
  like particles in others. BOTH descriptions are needed.
  They are COMPLEMENTARY — not contradictory.

Measurement and observation: The act of measurement disturbs the system.
  There is no "underlying reality" independent of measurement.
  It makes no sense to ask "where was the electron before I measured it?"

Bohr vs Einstein:
  Einstein: "God does not play dice." Quantum mechanics must be incomplete.
  Bohr: "Stop telling God what to do."

  The Bohr-Einstein debates at Solvay (1927, 1930) are the greatest
  intellectual exchanges in the history of physics.
  Einstein proposed thought experiments to refute uncertainty.
  Bohr showed each one was internally consistent with QM.
```

---

## Louis de Broglie (1892–1987)

### Who He Was

French physicist, Duke of Broglie. His PhD thesis (1924) proposed matter waves.
Nobel Prize 1929. This is one of the most audacious and correct PhD theses in history.

### The Contribution: Matter Waves

**The De Broglie Hypothesis**

```
DE BROGLIE WAVELENGTH
======================

Einstein (1905): Light has energy E = hf and momentum p = h/λ.
  Light has wave-particle duality.

De Broglie (1924): IF light has particle properties (photons),
  THEN particles should have wave properties.

  λ = h/p   (de Broglie wavelength for any particle)

  p = mv for non-relativistic particle, p = γmv relativistically.

For an electron at 1 eV:
  λ ≈ 1.23 nm  (comparable to atomic spacing — diffraction possible)

For a baseball (0.145 kg, 40 m/s):
  λ ≈ 10⁻³⁴ m  (unobservably small — quantum effects negligible)

CONFIRMATION:
  Davisson-Germer (1927): Electrons diffract off nickel crystal lattice.
  The diffraction pattern matches de Broglie's prediction perfectly.

BOHR MODEL EXPLAINED:
  The allowed orbits have circumference = integer multiple of de Broglie wavelength.
  2πr_n = nλ = nh/mv
  → L = mvr = nℏ  (Bohr's quantization condition — now EXPLAINED!)
```

---

## Werner Heisenberg (1901–1976)

### Who He Was

German physicist. Nobel Prize 1932. Created matrix mechanics (1925) — the first
complete formulation of quantum mechanics. During WWII, led the German nuclear
weapons program, which failed (for reasons still debated: incompetence, sabotage,
or deliberate delay?).

### The Contribution: Matrix Mechanics and the Uncertainty Principle

**Matrix Mechanics (1925)**

```
HEISENBERG'S MATRIX MECHANICS
================================

Heisenberg's approach: ONLY talk about OBSERVABLE quantities.
  Not: "the electron is at position x with momentum p"
  But: "the electron can emit photon of energy hf with probability P"

Represent observables as MATRICES:
  Position: x̂ (an infinite matrix)
  Momentum: p̂ (an infinite matrix)
  Hamiltonian: Ĥ (energy matrix)

Schrödinger equation (matrix form):
  iℏ d|ψ⟩/dt = Ĥ|ψ⟩  where |ψ⟩ is a vector in Hilbert space

Key: x̂p̂ ≠ p̂x̂  (matrices don't commute!)
  [x̂, p̂] = x̂p̂ - p̂x̂ = iℏ

This commutation relation IS quantum mechanics.
Everything follows from it.
```

**The Uncertainty Principle (1927)**

```
HEISENBERG UNCERTAINTY PRINCIPLE
==================================

ΔxΔp ≥ ℏ/2

  Δx = standard deviation of position measurements
  Δp = standard deviation of momentum measurements

The more precisely you know position, the less precisely you can know momentum.
And vice versa.

THIS IS NOT ABOUT MEASUREMENT DISTURBANCE:
  It's a fundamental property of waves.
  A wave localized in space has a spread in wavenumber k = p/ℏ.
  The Fourier transform mathematics: Δx · Δk ≥ 1/2
  → Δx · Δ(p/ℏ) ≥ 1/2
  → ΔxΔp ≥ ℏ/2

  A particle localized to Δx = 0.1 nm:
  Δp ≥ ℏ/(2·0.1nm) ≈ 5.3 × 10⁻²⁵ kg·m/s
  → Δv ≥ 5.8 × 10⁵ m/s for an electron

TIME-ENERGY UNCERTAINTY:
  ΔEΔt ≥ ℏ/2

  Energy and time are canonically conjugate.
  An excited state with lifetime τ has energy uncertainty ΔE ≈ ℏ/τ.
  This is the natural linewidth of spectral lines.

APPLICATIONS:
  - Zero-point energy: harmonic oscillator ground state E₀ = ℏω/2
    (not zero — uncertainty prevents it)
  - Stability of atoms: electrons can't fall into nucleus
    (would require infinite momentum uncertainty → infinite kinetic energy)
  - Tunneling: particles can pass through barriers they couldn't classically
  - Nuclear reactions: protons can fuse despite Coulomb barrier (quantum tunneling)
```

---

## Erwin Schrödinger (1887–1961)

### Who He Was

Austrian physicist, later at the Dublin Institute for Advanced Studies.
Nobel Prize 1933 (with Dirac). His wave equation (1926) is the other
complete formulation of QM, equivalent to Heisenberg's matrices.
Famous for Schrödinger's cat thought experiment (his own attempt to show
QM is absurd — used against him by many-worlds advocates).

### The Contribution: The Wave Equation

**The Schrödinger Equation (1926)**

```
SCHRÖDINGER EQUATION
=====================

TIME-DEPENDENT (general):
  iℏ ∂ψ/∂t = Ĥψ = [-ℏ²/(2m) ∇² + V(r,t)] ψ

  ψ(r,t) = complex wave function (probability amplitude)

TIME-INDEPENDENT (stationary states):
  Ĥψ = Eψ
  [-ℏ²/(2m) ∇² + V(r)] ψ(r) = E ψ(r)

  Solutions: standing wave solutions with definite energy E.
  Boundary conditions → discrete eigenvalues E_n → quantization emerges naturally.

BORN'S INTERPRETATION:
  |ψ(r,t)|² = probability density of finding particle at r at time t.
  (Max Born proposed this interpretation; Schrödinger resisted it.)

HYDROGEN ATOM SOLUTION:
  V(r) = -e²/(4πε₀r)  (Coulomb potential)
  Eigenvalues: E_n = -13.6 eV / n²  (Bohr model energies, DERIVED correctly)
  Eigenfunctions: ψ_nlm(r,θ,φ) = R_nl(r) · Y_lm(θ,φ)
    - R_nl: radial wave function (Laguerre polynomials)
    - Y_lm: spherical harmonics
    - Quantum numbers n, l, m naturally emerge from boundary conditions
```

**Schrödinger's Cat (1935)**

Schrödinger's thought experiment to expose the weirdness of Copenhagen:
A cat in a box with radioactive decay → poison mechanism. If the atom
decays, the cat dies. Before opening the box, QM says the cat is in a
superposition of alive and dead.

Schrödinger's intended conclusion: QM cannot apply to macroscopic objects.
Modern understanding: **decoherence** — the cat interacts with billions of
particles (air molecules, photons) that "measure" it continuously. The
superposition collapses almost instantly. Quantum coherence doesn't survive
at cat-scale.

---

## Max Born (1882–1970)

### Who He Was

German-British physicist. Nobel Prize 1954 (delayed — the statistical
interpretation of quantum mechanics was controversial for 30 years).
Fled Nazi Germany in 1933. Taught at Cambridge, Edinburgh.

### The Contribution: The Probability Interpretation

**The Born Rule**

```
BORN'S STATISTICAL INTERPRETATION (1926)
==========================================

Schrödinger produced wave functions ψ. But what IS ψ?

Born's proposal: |ψ(r,t)|² = probability density.
  If you measure the particle's position, the probability of finding it
  in volume d³r at r is |ψ(r,t)|² d³r.

Normalization: ∫|ψ(r,t)|² d³r = 1 (particle must be somewhere)

This was NOT Schrödinger's interpretation.
Schrödinger thought ψ represented a real physical wave (charge density).
Born said: ψ is a probability amplitude, not a physical wave.

The Born rule is the core of the measurement axiom of QM.
Everything we know about QM comes from Born's rule:
  - Expectation value: ⟨A⟩ = ∫ ψ* Â ψ d³r
  - If eigenstates: P(eigenvalue aₙ) = |⟨φₙ|ψ⟩|²

This is where "God plays dice" (Einstein's objection) comes from.
The outcome of a measurement is fundamentally probabilistic.
```

---

## Wolfgang Pauli (1900–1958)

### Who He Was

Austrian-Swiss physicist. "The Scourge of God" — notorious for savage critiques
of weak work. The "Pauli effect": equipment allegedly broke down near him. Nobel
Prize 1945. Predicted the neutrino in 1930 (confirmed experimentally in 1956).

### The Contribution: The Exclusion Principle and Spin

**The Pauli Exclusion Principle (1925)**

```
PAULI EXCLUSION PRINCIPLE
==========================

No two fermions (particles with half-integer spin) can occupy the same
quantum state simultaneously.

Quantum state = (n, l, m_l, m_s) for an electron.
  n = principal quantum number (energy level)
  l = orbital angular momentum quantum number
  m_l = magnetic quantum number
  m_s = spin quantum number (±1/2)

CONSEQUENCE FOR ATOMS:
  First shell (n=1): maximum 2 electrons (m_s = +1/2, -1/2)
  Second shell (n=2): maximum 8 electrons
  Third shell (n=3): maximum 18 electrons
  → The periodic table structure emerges from the exclusion principle.

CONSEQUENCE FOR MATTER:
  White dwarfs and neutron stars are supported by DEGENERACY PRESSURE:
  electrons (or neutrons) resist compression because they cannot
  all occupy the same ground state.
  If compression force exceeds degeneracy pressure → collapse to black hole.

FERMIONS vs BOSONS:
  Fermions (spin 1/2, 3/2, ...): obey Pauli exclusion. Antisymmetric wavefunction.
    Electrons, protons, neutrons, quarks, neutrinos.
  Bosons (spin 0, 1, 2, ...): prefer to occupy the same state. Symmetric wavefunction.
    Photons, gluons, W/Z bosons, Higgs, pions.
    → Bose-Einstein condensate: bosons pile into the ground state at low temperature.
    → Laser: many photons in the same mode (bosonic condensation).
```

**Spin**

Pauli introduced the 2-component spinor description of electron spin (1927).
Electron spin cannot be explained by classical rotation — it's intrinsically
quantum. The spin-statistics theorem (Pauli 1940) proves: half-integer spin
particles are fermions (antisymmetric), integer spin particles are bosons
(symmetric).

---

## Comparison Table

| Figure | Dates | Core Contribution | What They Built On | Legacy |
|--------|-------|-------------------|--------------------|--------|
| **Planck** | 1858–1947 | Energy quantization E=hf | Classical EM, thermodynamics | All of QM |
| **Bohr** | 1885–1962 | Atomic model, Copenhagen interpretation | Planck, Rutherford | Atomic physics, QM philosophy |
| **De Broglie** | 1892–1987 | Matter waves λ=h/p | Einstein's photons | Wave mechanics, electron microscopy |
| **Heisenberg** | 1901–1976 | Matrix mechanics, uncertainty principle | Bohr, Planck | All of QM, QFT |
| **Schrödinger** | 1887–1961 | Wave equation, wave mechanics | De Broglie | All of modern chemistry (orbitals) |
| **Born** | 1882–1970 | Probability interpretation of ψ | Schrödinger | The measurement postulate |
| **Pauli** | 1900–1958 | Exclusion principle, spin | QM formalism | Periodic table, matter stability |

---

## Who to Cite for What

| Concept | Cite | Notes |
|---------|------|-------|
| Quantization of energy E = nhf | Planck | 1900 blackbody |
| Planck constant h | Planck | |
| Bohr atomic model, energy levels | Bohr | 1913 |
| Complementarity, Copenhagen interpretation | Bohr | |
| Matter waves λ = h/p | De Broglie | 1924 |
| Matrix mechanics | Heisenberg | 1925 |
| Uncertainty principle ΔxΔp ≥ ℏ/2 | Heisenberg | 1927 |
| Wave equation (Schrödinger equation) | Schrödinger | 1926 |
| Probability interpretation |ψ|² | Born | 1926 |
| Exclusion principle | Pauli | 1925 |
| Spin (quantum) | Pauli (Uhlenbeck + Goudsmit proposed spin) | |
| Neutrino prediction | Pauli | 1930 (confirmed 1956) |

---

## Common Confusion Points

**"The uncertainty principle is about measurement disturbing the system"** — This
is the "observer disturbance" interpretation, which is NOT what Heisenberg's
principle says. The uncertainty is INTRINSIC to wave-like objects. A particle
doesn't have a definite position and momentum simultaneously — the concepts are
ill-defined simultaneously. The Ozawa-Arthurs inequality and more recent work
show the measurement-disturbance perspective is separable from the intrinsic
uncertainty.

**"Schrödinger's cat shows QM doesn't work for large objects"** — Schrödinger's
cat was intended to show the absurdity of the Copenhagen interpretation. Modern
understanding via decoherence explains why macroscopic superpositions don't
survive: environmental interaction collapses them effectively instantaneously.
The many-worlds interpretation maintains that the cat IS in superposition, but
the observer becomes entangled with it.

**"Wave-particle duality means something is both a wave and a particle"** — More
precisely: quantum objects don't fit either classical description. In some
experimental contexts, wave-like behavior (diffraction, interference) is manifest.
In others, particle-like behavior (localized detection, discrete energies) is manifest.
The appropriate description depends on the measurement setup.

**"Bohr's model explains atoms"** — It gives the right energies for hydrogen.
It fails for any multi-electron atom (helium and beyond). It doesn't explain
why electrons don't radiate (just postulates it). The Schrödinger equation with
proper electron-electron repulsion terms explains multi-electron atoms (with
approximations like Hartree-Fock or DFT).
