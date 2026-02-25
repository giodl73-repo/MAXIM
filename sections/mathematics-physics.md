# Mathematics & Physics

20 directories · Formal foundations — pure math through quantum, with the applied bridges between them

---

## Landscape

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                           MATHEMATICS & PHYSICS                                     │
└─────────────────────────────────────────────────────────────────────────────────────┘

 PURE MATHEMATICS
 ┌─────────────────┐   ┌───────────────────┐   ┌──────────────────┐
 │  mathematics/   │   │  number-theory/   │   │ abstract-algebra/ │
 │  vector calc    │   │  primes · modular │   │  groups · rings   │
 │  linear algebra │   │  Diophantine      │   │  fields · Galois  │
 │  ODEs · PDEs    │   │  RSA foundations  │   │  representation   │
 │  probability    │   │  analytic NT      │   │  homomorphisms    │
 │  topology primer│   └───────────────────┘   └──────────────────┘
 │  numerical meth │           │                        │
 └────────┬────────┘           └────────────┬───────────┘
          │                                 │
          │                        ┌────────▼────────┐
          │                        │    topology/    │
          │                        │  point-set      │
          │                        │  manifolds      │
          │                        │  homology /     │
          │                        │  cohomology     │
          │                        │  fundamental    │
          │                        │  group          │
          │                        └────────────────-┘
          │
          ▼
 APPLIED MATHEMATICS
 ┌──────────────────────┐   ┌─────────────────────┐   ┌──────────────────┐
 │  signal-processing/  │   │  information-theory/ │   │  control-theory/ │
 │  Fourier/Laplace/z   │   │  entropy · capacity  │   │  transfer fn     │
 │  FFT · filters · DSP │   │  source/channel code │   │  PID · state sp. │
 │  wavelets · Nyquist  │   │  compression · AIT   │   │  Lyapunov        │
 └──────────┬───────────┘   └─────────────────────┘   │  optimal ctrl    │
            │                                          └──────────────────┘
            ▼
 PHYSICAL LAYER
 ┌──────────────────┐   ┌──────────────────┐   ┌─────────────────────┐
 │    physics/      │   │   electronics/   │   │    materials/       │
 │  E&M · Maxwell   │   │  circuits · PCB  │   │  crystal structure  │
 │  mechanics · MHD │   │  op-amps · CMOS  │   │  phase diagrams     │
 │  thermodynamics  │   │  digital logic   │   │  failure modes      │
 │  liquid metals   │   │  power elec.     │   │  mech/thermal/elec  │
 │  quantum intro   │   └──────────────────┘   └─────────────────────┘
 └────────┬─────────┘
          │
          ▼
 QUANTUM LAYER
 ┌──────────────────────────────────────────────────────────┐
 │  quantum-computing/                                      │
 │  qubits · gates · Shor/Grover · error correction        │
 │  hardware platforms (superconducting/photonic/ion trap)  │
 └──────────────────────────────────────────────────────────┘
```

---

## Directories

| Directory | Focus | Entry Point | Bridges to |
|-----------|-------|-------------|------------|
| `mathematics/` | Vector calculus, linear algebra, ODEs/PDEs, probability theory, topology primer, numerical methods (Newton/Runge-Kutta/finite difference) | `01-VECTOR-CALC.md` — grad/div/curl/Stokes/Green | `physics/` for E&M application; `signal-processing/` for Fourier analysis; `control-theory/` for state-space |
| `number-theory/` | Primes, modular arithmetic, Chinese Remainder Theorem, Diophantine equations, RSA/DH/ECC mathematical foundations, analytic number theory (Riemann hypothesis framing) | `01-PRIMES.md` — prime distribution and sieve methods | `abstract-algebra/` for algebraic structures; `cryptography/` (Computing) for application |
| `abstract-algebra/` | Groups, rings, fields, Galois theory, homomorphisms/isomorphisms, representation theory, applications to coding theory | `01-GROUPS.md` — group axioms through Lagrange/Sylow | `number-theory/` for finite fields; `topology/` for algebraic topology; `cryptography/` (Computing) for elliptic curves |
| `topology/` | Point-set topology, metric spaces, compactness/connectedness, manifolds, homology/cohomology, fundamental group, applications to data (TDA) | `01-POINT-SET.md` — open sets through compactness | `mathematics/` for continuity foundations; `abstract-algebra/` for algebraic topology |
| `signal-processing/` | Fourier series/transform, Laplace transform, z-transform, filter design (FIR/IIR), FFT algorithms, DSP, wavelets, Nyquist-Shannon, sampling theory | `01-FOURIER.md` — Fourier series through DFT | `mathematics/` for functional analysis substrate; `physics/` for wave phenomena; `electronics/` for analog filter implementation |
| `information-theory/` | Shannon entropy, mutual information, channel capacity (Shannon-Hartley), source coding (Huffman/LZ), channel coding (Hamming/turbo/LDPC), algorithmic information theory | `01-ENTROPY.md` — entropy through KL divergence | `signal-processing/` for coding channel models; `cryptography/` (Computing) for entropy in key generation |
| `control-theory/` | Transfer functions, Bode plots, PID tuning, state-space representation, controllability/observability, stability (Lyapunov, Routh-Hurwitz), optimal control (LQR/LQG) | `01-TRANSFER-FUNCTIONS.md` — Laplace domain control | `mathematics/` for ODEs; `signal-processing/` for frequency-domain analysis; `robotics/` (Engineering) for implementation |
| `physics/` | Classical E&M (Coulomb through Maxwell equations), mechanics (Lagrangian/Hamiltonian), thermodynamics (laws through stat mech), MHD, liquid metals, quantum mechanics intro | `01-EM-FIELDS.md` — electrostatics through Maxwell | `mathematics/` for PDEs and vector calculus; `electronics/` for circuit-level E&M; `materials/` for condensed matter |
| `electronics/` | Circuit analysis (KVL/KCL/Thevenin), passive/active components, op-amp configurations, digital logic (gates through flip-flops), PCB layout, power electronics | `01-CIRCUIT-FUNDAMENTALS.md` — charge, current, KVL/KCL | `physics/` for electromagnetic substrate; `materials/` for semiconductor physics; `signal-processing/` for analog filter design |
| `materials/` | Crystal structure (Bravais lattices, Miller indices), phase diagrams (lever rule, eutectic), mechanical properties (stress/strain, fatigue, fracture mechanics), thermal/electrical properties | `01-CRYSTAL-STRUCTURE.md` — lattice types through X-ray diffraction | `physics/` for quantum band theory; `electronics/` for semiconductor materials; `chemical-eng/` (Engineering) for materials processing |
| `quantum-computing/` | Qubit models (Bloch sphere), quantum gates and circuits, key algorithms (Shor factoring, Grover search), quantum error correction (stabilizer codes), hardware platforms comparison | `01-QUBITS.md` — superposition, entanglement, measurement | `physics/` for quantum mechanics substrate; `cryptography/` (Computing) for post-quantum motivation; `mathematics/` for linear algebra and group theory |
| `probability-statistics/` | Measure-theoretic probability foundations, distributions and limit theorems (LLN/CLT), stochastic processes (Markov chains/Brownian motion/martingales), statistical inference (MLE/hypothesis testing), Bayesian methods (MCMC), regression models, time series, information geometry | `01-PROBABILITY-FOUNDATIONS.md` — sigma-algebras and probability spaces before distributions | `information-theory/` (entropy and KL divergence are shared objects); `statistics-applied/` (Social Sciences — applied methods vs. mathematical foundations); `ai-engineering/` (probabilistic ML) |
| `differential-geometry/` | Smooth manifolds, tangent/cotangent bundles, differential forms and Stokes theorem, Riemannian metrics and geodesics, connections and parallel transport, curvature tensors, Lie groups and algebras, fiber bundles, gauge theories | `01-MANIFOLDS.md` — charts and atlases before tensor machinery | `topology/` (shared manifold language); `physics/` (general relativity, Yang-Mills); `control-theory/` and `robotics/` (Lie groups for SE(3) rigid body motion); `mathematics/` (extends multivariable calculus) |
| `numerical-methods/` | IEEE 754 floating-point and error analysis, linear system solvers (LU/QR/Cholesky/iterative), eigenvalue algorithms (QR/SVD/Lanczos), interpolation and approximation, numerical integration (Gaussian quadrature/Monte Carlo), ODEs (Runge-Kutta/stiff solvers), PDEs (FD/FEM/spectral), optimization, scientific computing stack (BLAS/SciPy/Julia) | `01-FLOATING-POINT.md` — error propagation before any algorithm | `mathematics/` (the computational implementation of its content); `physics/` and Engineering (simulation of physical systems); Computing `data-science/` (NumPy/SciPy are this in practice) |
| `complex-analysis/` | Analytic functions and Cauchy-Riemann equations, contour integration and Cauchy's integral theorem, residue theorem and Laurent series (the complex analyst's Swiss Army knife), conformal mappings and applications to fluid flow and potential theory, Riemann surfaces as the natural domain of multi-valued functions, entire and meromorphic function theory, analytic continuation, harmonic functions and the Dirichlet problem | `01-ANALYTIC-FUNCTIONS.md` — Cauchy-Riemann equations and analyticity before integration | `topology/` (Riemann surfaces are complex manifolds); `physics/` (conformal field theory, potential theory); `signal-processing/` (complex analysis underlies the z-transform and filter theory) |
| `fluid-dynamics/` | Continuum hypothesis and governing equations (Navier-Stokes from first principles — the most important unsolved problem in classical physics), inviscid flow (Euler equations, Bernoulli, potential flow, vorticity), viscous flow and Reynolds number as the key dimensionless parameter, boundary layer theory (Prandtl's breakthrough — why thin layers dominate), turbulence phenomenology (Kolmogorov cascade, RANS, LES, DNS), compressible flow and shock waves (normal/oblique shocks, expansion fans), aerodynamics (Kutta-Joukowski, lifting-line theory), CFD methods | `01-CONTINUUM-MECHANICS.md` — the continuum hypothesis and derivation of governing equations | `mathematics/` (PDEs — Navier-Stokes is a PDE system); `aeronautics/` (Engineering) for applications; `statistical-mechanics/` for the kinetic theory underpinning |
| `statistical-mechanics/` | Boltzmann's statistical interpretation of entropy — the conceptual revolution; microcanonical ensemble (equal-a-priori-probability); canonical ensemble and the partition function as the generating function of thermodynamics; grand canonical ensemble; quantum statistics (Fermi-Dirac and Bose-Einstein — why metals conduct and why lasers work); phase transitions and critical phenomena (order parameters, universality classes); renormalization group (the tool that explains why universality exists); Ising model as the paradigm; non-equilibrium SM (fluctuation theorems, Langevin/Fokker-Planck) | `01-FOUNDATIONS.md` — probability and the Boltzmann distribution before ensemble machinery | `physics/` (thermodynamics is recovered from SM); `information-theory/` (entropy is the same object in both); `partial-differential-equations/` (Fokker-Planck, diffusion equations) |
| `partial-differential-equations/` | Classification (elliptic/parabolic/hyperbolic — the three regimes that determine everything about solution behavior), well-posedness (Hadamard's conditions), first-order PDEs and characteristics, wave equation (d'Alembert formula, characteristics, energy methods), heat equation (fundamental solution, maximum principle, Fourier series), Laplace/Poisson equations (mean-value property, Green's functions, harmonic analysis), Fourier and eigenfunction methods, weak solutions and Sobolev spaces (why classical solutions are insufficient), numerical PDE methods (FD, FEM, spectral) | `01-CLASSIFICATION.md` — elliptic/parabolic/hyperbolic and what the classification implies | `mathematics/` (vector calculus and ODEs are prerequisites); `physics/` (E&M, heat, quantum are all governed by PDEs); `numerical-methods/` for the computational side |
| `variational-calculus/` | Functionals and the variational derivative (the Fréchet/Gateaux derivatives of functionals), Euler-Lagrange equations (the central result — when does a functional achieve an extremum?), constrained variation and Lagrange multipliers, Lagrangian mechanics as variational principle (Hamilton's principle), Hamiltonian mechanics and symplectic geometry, second variation and stability criteria, direct methods in the calculus of variations (existence theory, coercivity, weak lower semicontinuity), optimal control (Pontryagin maximum principle as a generalization of E-L), connections to gradient descent and ML loss minimization | `01-FUNCTIONALS.md` — the functional derivative before the Euler-Lagrange derivation | `mathematics/` (ODEs and PDEs are the equations that come out of E-L); `physics/` (the Lagrangian/Hamiltonian formulation); `partial-differential-equations/` (variational weak formulations underlie FEM) |
| `lie-groups/` | Smooth manifolds that are also groups — the synthesis of algebra and differential geometry: matrix Lie groups (GL(n), SL(n), O(n), U(n), Sp(n) — concrete before abstract), Lie algebras and the exponential map (the local-to-global bridge), the adjoint representation, SU(2) and SO(3) and angular momentum in quantum mechanics, root systems and Dynkin diagrams (the classification of semisimple Lie algebras), representation theory (Peter-Weyl theorem, highest weight theory), Lie groups in gauge theory (SU(3)×SU(2)×U(1) as the Standard Model gauge group), applications to robotics (SE(3) rigid body motion) and computer vision | `01-MATRIX-GROUPS.md` — concrete matrix groups before abstract definition | `abstract-algebra/` (group theory is prerequisite); `differential-geometry/` (Lie groups are the principal example of smooth manifolds); `physics/` (gauge theory, particle physics) |

---

## Paths

### From MIT foundations into applied engineering math
`mathematics/` → `signal-processing/` → `control-theory/`
*The vector calc and ODE machinery from your MIT background plugs directly into the s-domain and state-space formulations — this path makes explicit what those courses were building toward.*

### Cryptographic mathematics
`number-theory/` → `abstract-algebra/` → `cryptography/` (Computing & Software)
*RSA and ECC are group-theoretic constructions over number fields — build the algebraic machinery first, then the cryptographic application is almost immediate.*

### Physics into hardware
`physics/` → `electronics/` → `materials/` → `semiconductor-manufacturing/` (Engineering)
*Maxwell through circuits through solid-state physics through fab — the vertical stack from equations to transistors.*

---

## Adjacent Sections

| Section | The bridge |
|---------|------------|
| Computing & Software | `number-theory/` + `abstract-algebra/` are the mathematical underpinnings of everything in `cryptography/`. `information-theory/` underpins compression, entropy sources for key generation, and conceptually grounds LLM tokenization. `signal-processing/` is directly below audio/image ML pipelines in `ai-engineering/`. |
| Engineering | `signal-processing/` feeds directly into `acoustics/` and `telecommunications/` — the transform tools are shared. `control-theory/` is the mathematical substrate for `robotics/` and industrial process control in `chemical-eng/`. `physics/` and `materials/` underlie the entire physical engineering track. |
| Earth & Space | `physics/` MHD section is the governing framework for solar physics and magnetospheric dynamics in `astronomy/`. Thermodynamics in `physics/` connects to atmospheric dynamics in Earth sciences. |
