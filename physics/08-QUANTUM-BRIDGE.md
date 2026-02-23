# Quantum Bridge — From Classical E&M to Quantum Mechanics

## The Big Picture

Classical physics — Maxwell's equations, Newton's laws — failed spectacularly
at atomic scales. Three experimental facts could not be explained. Each fix
required abandoning a deeply held assumption. The result was quantum mechanics.

```
+------------------------------------------------------------------------+
|                    THE CRISIS AND THE RESOLUTION                       |
|                                                                        |
|  EXPERIMENT              CLASSICAL FAILURE      QUANTUM FIX            |
|  ──────────              ────────────────       ──────────             |
|  Blackbody radiation     UV catastrophe         Energy quantized        |
|  Photoelectric effect    Intensity should work  Light comes in quanta   |
|  Atomic spectra          Atoms should collapse  Stable quantum orbits   |
|  Compton scattering      Waves don't bounce     Photons have momentum   |
|                                                                        |
|  THE THEORY (Schrödinger, Heisenberg, Dirac — 1925-1928):             |
|                                                                        |
|  iℏ ∂ψ/∂t = Ĥψ          ← Schrödinger equation                       |
|                                                                        |
|  ψ: wavefunction (complex, probabilistic)                              |
|  Ĥ: Hamiltonian operator (total energy)                                |
|  This is an eigenvalue problem. It IS linear algebra.                  |
|                                                                        |
|  Hilbert space (infinite-dim complex vector space)                     |
|  + Hermitian operators + eigenvalues = all of QM                       |
+------------------------------------------------------------------------+
```

You have Artin cold. QM is that same linear algebra machinery — applied to
infinite-dimensional function spaces, with complex scalars, over the field ℂ.
The Schrödinger equation is: find the eigenvectors of Ĥ.

---

## Failure 1 — Blackbody Radiation and Planck's Quantization

**Blackbody**: a perfect absorber and emitter of radiation. A cavity with a
small hole is a good approximation. Heat it up — what spectrum does it emit?

**Classical prediction** (Rayleigh-Jeans law): treat the EM field in the
cavity as a collection of standing wave modes. By equipartition (classical
stat mech), each mode gets average energy kT. Count the modes at each frequency:

```
  u(ν) dν = (8πν²/c³) × kT × dν    (energy density per frequency interval)
              ──────────    ──
              mode count   energy/mode
```

At low ν: agrees with experiment.
At high ν: diverges as ν² → ∞. **Ultraviolet catastrophe.**
A hot object should emit infinite power. It clearly doesn't.

**Planck's fix** (1900): assume energy in each mode cannot be arbitrary —
it comes in discrete quanta of size E = hν.

```
  h = 6.626 × 10⁻³⁴ J·s    (Planck's constant)
  ℏ = h/2π = 1.055 × 10⁻³⁴ J·s
```

At high ν: the quantum hν is so large compared to kT that the mode is
almost never excited — effectively frozen out. The UV catastrophe disappears.

Planck's law:

```
         8πhν³/c³
  u(ν) = ──────────────────
          e^(hν/kT) - 1

  → Rayleigh-Jeans at low ν  (hν << kT: e^(hν/kT) - 1 ≈ hν/kT)
  → Exponential cutoff at high ν  (hν >> kT: exponentially suppressed)
```

Planck thought quantization was a mathematical trick. Einstein took it seriously.

---

## Failure 2 — Photoelectric Effect and the Photon

Shine light on a metal. Electrons are ejected. Classical prediction: any
frequency, with enough intensity, should eject electrons.

**Observations**:
- Below a threshold frequency ν₀: no electrons, regardless of intensity
- Above ν₀: electrons ejected immediately, even at low intensity
- Electron kinetic energy depends on frequency, not intensity
- Intensity increases electron count but not their energy

**Classical explanation**: impossible. Waves should accumulate energy gradually —
given enough time and intensity, any frequency should work.

**Einstein's explanation** (1905, Nobel 1921):
Light consists of discrete quanta (**photons**), each with energy E = hν.
One photon ejects one electron. If hν < φ (work function), the photon cannot
eject the electron regardless of how many photons arrive.

```
  KE_max = hν - φ    (kinetic energy of ejected electron)
  φ = hν₀           (work function = energy to remove electron from surface)
```

Plot KE_max vs ν → straight line with slope h. This measured Planck's constant
from purely optical experiments.

**The photon**: a quantum of the EM field. Energy E = hν = ℏω. Momentum p = h/λ = ℏk.
Massless, travels at c, spin-1. The particle of light.

---

## Failure 3 — Atomic Stability and the Bohr Model

**The problem**: a classical electron orbiting a proton is an accelerating charge.
Accelerating charges radiate (Larmor radiation — module 04). Radiating electrons
lose energy, spiral inward, and crash into the nucleus in ~10⁻¹¹ s.
Atoms cannot exist classically.

**Observation**: atoms are stable. And they emit light only at discrete frequencies
(spectral lines) — not a continuous spectrum.

**Bohr's model** (1913, semi-classical):
Postulate: electrons occupy discrete orbits where the angular momentum is
quantized: L = nℏ, n = 1, 2, 3, ...

For hydrogen (Coulomb force provides centripetal acceleration):

```
  Energy levels:    En = -13.6 eV / n²

  n=1:  E₁ = -13.6 eV  (ground state)
  n=2:  E₂ = -3.4  eV
  n=3:  E₃ = -1.51 eV
  n→∞:  E∞ = 0         (ionized)
```

Transitions between levels emit or absorb photons:
hν = Eᵢ - Eⱼ (energy conservation)

```
  HYDROGEN SPECTRUM:

  n=5 ─────  -0.54 eV
  n=4 ─────  -0.85 eV  ┐
  n=3 ─────  -1.51 eV  │ Paschen series (IR)
  n=2 ─────  -3.40 eV  │ Balmer series (visible: Hα=656nm red, Hβ=486nm blue)
  n=1 ─────  -13.6 eV    Lyman series (UV)
```

Bohr's model: correct energy levels for hydrogen, wrong for everything else.
The orbits are fiction — quantum mechanics replaces them with probability clouds.
But the energy level formula survives in the full theory.

---

## Wave-Particle Duality

**de Broglie hypothesis** (1924): if light (a wave) has particle properties,
particles should have wave properties. Every particle has an associated
wavelength:

```
        h       h      ℏ
  λ = ─────  = ───  = ───
         p      mv     p
```

```
  Electron at 1 eV:    λ ≈ 1.2 nm   (atomic/molecular scale)
  Electron at 100 eV:  λ ≈ 0.12 nm  (X-ray scale, crystal diffraction)
  Proton at 1 MeV:     λ ≈ 29 fm    (nuclear scale)
  Baseball at 10 m/s:  λ ≈ 10⁻³⁵ m  (unmeasurable)
```

The de Broglie wavelength for macroscopic objects is so small that wave
behavior is completely unobservable. QM smoothly reduces to classical
mechanics at large scales.

**Double-slit experiment** (the central mystery):

```
  Source  → [slit 1]  →  screen
          → [slit 2]  →

  Classical particles: two bands on screen (one from each slit)
  Classical waves:     interference pattern (bright and dark fringes)
  Electrons:           INTERFERENCE PATTERN (even one electron at a time)

  An individual electron passes through — and interferes with itself.
  It is in superposition of going through both slits simultaneously.

  Now watch which slit:
  If you detect which slit the electron used → interference vanishes.
  Measurement collapses the superposition.
```

This is not a technology limitation. It is the fundamental nature of reality
at quantum scales. Feynman called it "the only mystery" of quantum mechanics.

---

## Heisenberg Uncertainty Principle

You know this from signals and systems (6.003):

```
  SIGNALS:   A signal localized in time has broad frequency content.
             Δt · Δω ≥ 1/2     (bandwidth-time product)

  QUANTUM:   A particle localized in position has broad momentum content.
             Δx · Δp ≥ ℏ/2
```

These are the same mathematical statement. The de Broglie relation p = ℏk
maps momentum to wavenumber, and the Fourier uncertainty relation does the rest.

**Uncertainty is not about measurement disturbance.** It is an intrinsic
property of the wavefunction — a quantum particle simply does not have a
definite position AND a definite momentum simultaneously. Both are undefined,
not unknown.

**Energy-time uncertainty**:

```
  ΔE · Δt ≥ ℏ/2
```

An energy eigenstate (definite E) persists forever (Δt = ∞).
An excited state that decays in time Δt has an energy spread ΔE ~ ℏ/Δt.
This is why spectral lines have finite width.

**Zero-point energy consequence**: a particle confined to a box cannot have
zero kinetic energy — that would mean Δp = 0, requiring Δx = ∞ (unconfined).
The minimum energy is nonzero: E_min ~ ℏ²/2mL². This is the origin of
zero-point energy — preview of module 09.

---

## The Schrödinger Equation

The fundamental equation of non-relativistic quantum mechanics:

```
  ┌──────────────────────────────────────────────────┐
  │                                                  │
  │   iℏ ∂ψ/∂t = Ĥψ                                 │
  │                                                  │
  │   Ĥ = -ℏ²/2m ∇² + V(r,t)                        │
  │       ─────────   ──────                         │
  │       kinetic      potential                     │
  │                                                  │
  └──────────────────────────────────────────────────┘
```

ψ(r,t) is the **wavefunction** — a complex-valued function of position and time.
It is not directly observable. What IS observable:

**Born rule**: |ψ(r,t)|² is the probability density of finding the particle at r.

```
  P(particle in volume dV at r) = |ψ(r,t)|² dV

  Normalization:  ∫|ψ|² dV = 1    (particle must be somewhere)
```

**Stationary states**: when V is time-independent, separate variables:
ψ(r,t) = φ(r) × e^(-iEt/ℏ)

The spatial part satisfies the **time-independent Schrödinger equation**:

```
  Ĥφ = Eφ    ← THIS IS AN EIGENVALUE EQUATION

  Ĥ is the Hamiltonian operator (Hermitian)
  φ is an energy eigenstate (eigenvector)
  E is the energy eigenvalue (real, because Ĥ is Hermitian)
```

This is exactly the linear algebra of Artin chapters 3-5, now over
infinite-dimensional complex vector spaces (Hilbert spaces).

---

## QM as Linear Algebra — The Full Dictionary

```
  LINEAR ALGEBRA              QUANTUM MECHANICS
  ──────────────              ─────────────────
  Vector space V              Hilbert space ℋ
  Vector |v⟩                  State vector |ψ⟩ (Dirac notation)
  Inner product ⟨u|v⟩         ∫ φ*(r) ψ(r) dV
  Linear operator A           Observable operator Â (Hermitian)
  Eigenvector Av = λv         Ĥ|ψ_n⟩ = E_n|ψ_n⟩
  Eigenvalue λ                Measurement outcome E_n (real)
  Basis expansion v=Σcᵢeᵢ    |ψ⟩ = Σ cₙ|ψ_n⟩ (superposition)
  Coefficient cᵢ = ⟨eᵢ|v⟩    Amplitude cₙ = ⟨ψ_n|ψ⟩
  |cᵢ|² (normalized)         Probability of measuring Eₙ
  Unitary transformation      Time evolution operator e^(-iĤt/ℏ)
  Hermitian matrix A=A†       Observable Â = Â†
  Orthonormal basis           Energy eigenstates ⟨ψₙ|ψₘ⟩ = δₙₘ
```

**Dirac bra-ket notation**:
- Ket |ψ⟩: state vector (column vector in finite dim)
- Bra ⟨ψ|: its dual (row vector, complex conjugate transpose)
- Inner product: ⟨φ|ψ⟩ = ∫φ*(r)ψ(r)dV (a complex number)
- Outer product: |ψ⟩⟨ψ| (a projection operator)
- Expectation value: ⟨Â⟩ = ⟨ψ|Â|ψ⟩ (average measurement outcome)

---

## Key Operators

```
  OBSERVABLE        OPERATOR                    EIGENVALUES
  ──────────        ────────                    ───────────
  Position x        x̂ = multiply by x           continuous
  Momentum p        p̂ = -iℏ ∂/∂x               continuous
  Kinetic energy    T̂ = p̂²/2m = -ℏ²/2m ∇²      continuous
  Potential energy  V̂ = V(r) multiply by V      continuous
  Hamiltonian       Ĥ = T̂ + V̂                  discrete (bound states)
  Angular momentum  L̂ = r̂ × p̂                  ℏ√(l(l+1)), l=0,1,2,...
  L_z               L̂_z = -iℏ ∂/∂φ             mℏ, m=-l,...,l
  Spin (z-comp)     Ŝ_z = (ℏ/2)σ_z             ±ℏ/2
```

**Canonical commutation relation** — the heart of QM:

```
  [x̂, p̂] = x̂p̂ - p̂x̂ = iℏ

  Non-commuting observables → uncertainty principle:
  ΔA · ΔB ≥ |⟨[Â,B̂]⟩|/2

  [x̂, p̂] = iℏ  →  ΔxΔp ≥ ℏ/2  ✓
```

---

## The Hydrogen Atom — QM Solution

Solve Ĥψ = Eψ with V(r) = -e²/4πε₀r. Use spherical coordinates.

Separate: ψ_nlm(r,θ,φ) = R_nl(r) · Y_l^m(θ,φ)

Y_l^m are **spherical harmonics** — eigenfunctions of L̂² and L̂_z.
(These appear in EM — antenna radiation patterns, multipole expansions.)

**Quantum numbers**:

```
  n = 1, 2, 3, ...           principal quantum number
                              determines energy: En = -13.6 eV/n²

  l = 0, 1, 2, ..., n-1      orbital angular momentum quantum number
                              orbital shape: s(l=0), p(l=1), d(l=2), f(l=3)
                              |L| = ℏ√(l(l+1))

  m = -l, -l+1, ..., 0, ..., l   magnetic quantum number
                              z-component: Lz = mℏ
                              (2l+1) values for each l

  s = ±1/2                   spin quantum number (intrinsic)
```

**The orbitals** — probability clouds, not orbits:

```
  l=0 (s orbital):   spherically symmetric, no angular nodes
  l=1 (p orbital):   dumbbell shape, one angular node
  l=2 (d orbital):   four-lobed, two angular nodes
```

**Degeneracy**: for hydrogen, all states with the same n have the same energy
(n² degenerate states, ignoring spin). This degeneracy is broken by:
- External magnetic field (Zeeman effect) — splits m levels
- Electron-electron repulsion (multi-electron atoms) — splits l levels
- Spin-orbit coupling (relativistic) — splits s levels

---

## Spin — The Non-Classical Angular Momentum

Electrons have an intrinsic angular momentum with no classical analog.
It cannot be explained by the electron "spinning" — that would require
superluminal surface speed.

Spin-1/2 particles (electrons, protons, neutrons, quarks):

```
  |↑⟩ = spin up,    Sz = +ℏ/2    (eigenvalue of Ŝ_z)
  |↓⟩ = spin down,  Sz = -ℏ/2

  General spin state: |χ⟩ = α|↑⟩ + β|↓⟩,   |α|² + |β|² = 1
```

**Pauli matrices** — the spin operators (in units of ℏ/2):

```
        [0  1]          [0  -i]          [1   0]
  σx =  [1  0]   σy =   [i   0]   σz =   [0  -1]

  Spin operators: Ŝ = (ℏ/2)(σx x̂ + σy ŷ + σz ẑ)
```

You know these from Artin — they generate the Lie algebra su(2), which is
the Lie algebra of SU(2). The spin-1/2 representation of SU(2) is the
**fundamental representation** — the smallest non-trivial one.

**Why spin matters**:
- Pauli exclusion principle: no two fermions can occupy the same quantum state
  (including spin). This is why electrons fill orbitals in pairs (↑↓).
- Determines whether a particle is a fermion (half-integer spin) or boson
  (integer spin) — and therefore its statistical behavior (Fermi-Dirac vs Bose-Einstein)
- The electron spin magnetic moment: μ = -gₑμ_B S/ℏ
  (gₑ ≈ 2.002 — slightly more than 2, the "anomalous" magnetic moment,
  explained by QED to 10 decimal places — one of physics' greatest predictions)

---

## The Connection Back to E&M — Quantizing the Field

The EM field is not just a classical field — it must also be quantized.
This leads to **quantum electrodynamics** (QED).

Quantize each mode (k, polarization) of the EM field as a quantum harmonic
oscillator. For a harmonic oscillator, energy eigenvalues are:

```
  E_n = (n + 1/2)ℏω    n = 0, 1, 2, 3, ...
              ─────
              zero-point energy
```

**n is the number of photons** in that mode. Photons are the quanta of the EM field.

**Vacuum state** (n=0): zero photons. But the energy is NOT zero:

```
  E_vacuum = (1/2)ℏω    for each mode

  Sum over all modes: E_vac = Σ_k (1/2)ℏω_k = ∞
```

This infinite zero-point energy is the **quantum vacuum energy problem** —
the starting point of module 09. The vacuum is not empty. Every mode of
every quantum field has a ground-state energy of ℏω/2. Summing over all
frequencies and all fields gives infinity.

How to deal with this infinity, what it implies physically, and what the
Casimir effect reveals about it — that is module 09.

---

## The 6.012 Gap — Semiconductor Physics Requires QM

6.012 (MIT Microelectronic Devices and Circuits) is the course you didn't take.
It sits between QM and circuit theory. Now you have the QM foundation. What 6.012 adds:

**Band theory**: electrons in a periodic crystal lattice → Schrödinger equation
with periodic potential V(r) → Bloch's theorem → energy bands.

```
  FREE ELECTRON: continuous E vs k (quadratic: E = ℏ²k²/2m)

  PERIODIC LATTICE: gaps open at Brillouin zone boundaries:
  ────────────────────────────────────
  conduction band  (empty, electrons can flow)
  ─────────── gap Eg ──────────────────
  valence band     (full, electrons blocked)
  ────────────────────────────────────

  Conductor:  no gap or overlapping bands
  Insulator:  large gap (Eg > 4 eV)
  Semiconductor: small gap (Si: Eg = 1.1 eV, GaAs: 1.4 eV)
```

**Fermi-Dirac distribution**: electrons are fermions. At temperature T,
probability of state at energy E being occupied:

```
  f(E) = 1/(e^((E-Ef)/kT) + 1)    (Fermi-Dirac)

  At T=0: all states below Ef filled, all above empty (step function)
  At T>0: thermal broadening near Ef ~ kT
```

**Doping and p-n junctions**: add impurities to shift Fermi level.
n-type (donor atoms): extra electrons, Ef near conduction band.
p-type (acceptor atoms): extra holes, Ef near valence band.
p-n junction: built-in electric field at the interface → diode behavior.
Forward bias lowers barrier → current flows. Reverse bias raises it → blocks.

**MOSFET**: voltage on gate modulates conducting channel between drain and source.
Threshold voltage Vt: gate voltage needed to invert the semiconductor surface,
forming the channel. QM determines Vt through band bending calculations.

This is the chain: Maxwell → QM → band theory → semiconductor devices → transistors → 6.002 circuits.
6.012 is the middle layer you can now approach from both ends.

---

## Decision Cheat Sheet

| Concept | Key equation | Physical meaning |
|---------|-------------|-----------------|
| Photon energy | E = hf = ℏω | EM field quantized |
| Photon momentum | p = h/λ = ℏk | Light has momentum |
| de Broglie wavelength | λ = h/p | Particles have wave nature |
| Uncertainty | ΔxΔp ≥ ℏ/2 | Bandwidth-time theorem for matter |
| Wavefunction meaning | P = |ψ|² dV | Probability density |
| Schrödinger | Ĥψ = Eψ | Eigenvalue problem for energy |
| Hermitian operators | Â = Â† | Real eigenvalues (real measurement outcomes) |
| Spin-1/2 generators | (ℏ/2)σᵢ | Fundamental rep of SU(2) (Artin!) |
| H atom energy levels | En = -13.6/n² eV | From Coulomb potential eigenvalue problem |
| Field quantization | E_n = (n+½)ℏω | n = photon number, ½ = zero-point |

---

## Common Confusion Points

**The wavefunction is not a physical wave.**
It is not a wave of anything material — it is a probability amplitude.
Its absolute square gives probability density. It lives in configuration
space (3N dimensions for N particles), not physical 3D space.

**Measurement does not just reveal a pre-existing value.**
Before measurement, position is genuinely undefined — not merely unknown.
The act of measurement forces the particle into a definite state.
Bell's theorem (1964) and subsequent experiments prove that hidden variables
(the particle "really" had a definite position we just didn't know) cannot work.

**The Schrödinger equation is deterministic.**
Between measurements, ψ evolves deterministically according to iℏ∂ψ/∂t = Ĥψ.
Randomness only enters at the moment of measurement (or in the many-worlds
interpretation, it doesn't enter at all — observers also split).
The measurement problem is not solved — it is the deepest open question in
the foundations of QM.

**Spin is not rotation.**
An electron would have to rotate 720° (not 360°) to return to its initial
spin state. No physical spinning ball does this. Spin is an intrinsic quantum
property with no classical analog — a purely quantum degree of freedom.

**Zero-point energy is not extractable (in standard QM).**
The ground state energy ℏω/2 is the minimum — you cannot remove it by
cooling down (you'd need T = 0 K, unreachable). It is the energy you cannot
take away. This doesn't mean it has no physical consequences — the Casimir
effect (module 09) demonstrates it does. But you cannot "tap" it as a
power source without violating thermodynamics.

**The connection to Artin runs deep.**
SU(2) in Artin (matrix group, 2×2 unitary determinant-1 matrices) IS the
symmetry group of quantum spin. The spin-1/2 representation IS the fundamental
representation. The commutation relations of Pauli matrices ARE the Lie algebra
su(2) = so(3). The representation theory Artin skims — irreducible representations
labeled by j = 0, 1/2, 1, 3/2, ... — IS the classification of all particle spins.
You already had the mathematics. Now it has physical content.
