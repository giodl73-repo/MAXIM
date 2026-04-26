# Hamiltonian Mechanics and Phase Space

## The Big Picture

Hamiltonian mechanics transforms Lagrangian mechanics via a **Legendre transform**, replacing
velocities q̇ with momenta p. The result is a 2n-dimensional phase space with a remarkably
symmetric structure that reveals the deep geometry of dynamics.

```
+-----------------------------------------------------------------------+
|              LAGRANGIAN vs. HAMILTONIAN                               |
|                                                                       |
|  LAGRANGIAN           HAMILTONIAN                                     |
|  -----------          -----------                                     |
|  State: (q, q̇)       State: (q, p)  [phase space]                     |
|  n 2nd-order ODEs     2n 1st-order ODEs                               |
|  L = T − V            H = T + V  (usually energy)                     |
|  q̈ = f(q, q̇)         q̇ = ∂H/∂p,  ṗ = −∂H/∂q                      |
|  Tangent bundle TQ    Cotangent bundle T*Q                            |
|                                                                       |
|  ADVANTAGES OF HAMILTONIAN:                                           |
|  • Phase space geometry (symplectic structure)                        |
|  • Conservation: {H, f} = 0 ↔ f is conserved                          |
|  • Canonical transformations simplify problems                        |
|  • Direct path to quantum mechanics                                   |
|  • Statistical mechanics (Liouville's theorem)                        |
|                                                                       |
+-----------------------------------------------------------------------+
```

---

## The Legendre Transform

The transformation from Lagrangian to Hamiltonian:

```
  STEP 1: CANONICAL MOMENTA
  pᵢ = ∂L/∂q̇ᵢ   (n equations)

  STEP 2: INVERT (if possible)
  Express q̇ᵢ = q̇ᵢ(q, p, t) from the p equations.
  Requires: ∂²L/∂q̇ᵢ∂q̇ⱼ nonsingular (Hessian invertible).

  STEP 3: LEGENDRE TRANSFORM
  H(q, p, t) = Σᵢ pᵢ q̇ᵢ − L(q, q̇, t)
  where q̇ on the right is expressed as a function of (q,p).

  EXAMPLE: L = ½m|q̇|² − V(q)
  p = mq̇  →  q̇ = p/m
  H = p·(p/m) − [½m|p/m|² − V] = |p|²/2m + V(q)  ← Kinetic + potential!

  EXAMPLE: Relativistic particle:
  L = −mc²√(1−v²/c²) − V
  p = mv/√(1−v²/c²)  →  v = pc/√(m²c²+p²)
  H = √(m²c⁴ + p²c²) + V   ← Relativistic energy-momentum relation!
```

---

## Hamilton's Equations

The equations of motion in phase space:

```
  HAMILTON'S EQUATIONS:
  ┌────────────────────────────────────────────────────────────────┐
  │   dqᵢ/dt = ∂H/∂pᵢ     (velocity = slope of H in p-direction)│
  │   dpᵢ/dt = −∂H/∂qᵢ    (force = −slope of H in q-direction)     │
  └────────────────────────────────────────────────────────────────┘

  These replace: n 2nd-order E-L equations
  With:          2n 1st-order equations

  ENERGY CONSERVATION:
  dH/dt = Σ (∂H/∂qᵢ q̇ᵢ + ∂H/∂pᵢ ṗᵢ) + ∂H/∂t
        = Σ (∂H/∂qᵢ ∂H/∂pᵢ − ∂H/∂pᵢ ∂H/∂qᵢ) + ∂H/∂t
        = ∂H/∂t

  If H has no explicit t: dH/dt = 0. Energy is conserved.

  DERIVATION from Lagrangian:
  d/dt(H) = d/dt(Σpᵢq̇ᵢ − L) = Σ(ṗᵢq̇ᵢ + pᵢq̈ᵢ − ∂L/∂qᵢq̇ᵢ − ∂L/∂q̇ᵢq̈ᵢ − ∂L/∂t)
  Use E-L: ṗᵢ = ∂L/∂qᵢ, and pᵢ = ∂L/∂q̇ᵢ → terms cancel.
  = −∂L/∂t = ∂H/∂t  ■
```

---

## Phase Space and Symplectic Structure

```
  PHASE SPACE: M = {(q₁,...,q_n, p₁,...,p_n)} = T*Q  (cotangent bundle)

  SYMPLECTIC FORM:
  ω = Σᵢ dpᵢ ∧ dqᵢ   (the canonical symplectic 2-form)

  PROPERTIES OF ω:
  • Closed: dω = 0
  • Non-degenerate: ω(v,w) = 0 for all w → v = 0
  • Antisymmetric: ω(v,w) = −ω(w,v)

  HAMILTONIAN VECTOR FIELD X_H:
  ω(X_H, ·) = dH  defines X_H uniquely (via non-degeneracy of ω).
  In coordinates: X_H = Σ(∂H/∂pᵢ ∂/∂qᵢ − ∂H/∂qᵢ ∂/∂pᵢ)
  This is EXACTLY Hamilton's equations!

  SYMPLECTIC VOLUME:
  ω^n = ω ∧ ω ∧ ... ∧ ω (n times) is the volume form on phase space.
  Up to a constant: vol = dq₁∧dp₁∧...∧dqₙ∧dpₙ
```

### Liouville's Theorem

```
  The Hamiltonian flow preserves phase space volume.

  If ρ(q,p,t) = density of phase space points (ensemble),

  LIOUVILLE'S EQUATION:
  ∂ρ/∂t + Σᵢ (∂ρ/∂qᵢ q̇ᵢ + ∂ρ/∂pᵢ ṗᵢ) = 0
  ∂ρ/∂t + {H, ρ} = 0   (where {·,·} = Poisson bracket)

  Or: dρ/dt = 0 (density constant along trajectories).

  IMPLICATIONS:
  • An ensemble of initial conditions occupying volume V_0 will
    always occupy the same phase space volume V_0.
  • Phase space is incompressible under Hamiltonian flow.
  • No attractor in phase space for Hamiltonian systems.
  • Foundation of statistical mechanics: equal a priori probabilities.
  • Poincaré recurrence theorem (finite volume phase space → returns).
```

---

## Poisson Brackets

The Poisson bracket is the fundamental operation on observables:

```
  POISSON BRACKET:
  {f, g} = Σᵢ (∂f/∂qᵢ ∂g/∂pᵢ − ∂f/∂pᵢ ∂g/∂qᵢ)

  PROPERTIES:
  • Antisymmetry:    {f,g} = −{g,f}
  • Bilinearity:     {αf+βg, h} = α{f,h} + β{g,h}
  • Leibniz rule:    {fg, h} = f{g,h} + {f,h}g
  • Jacobi identity: {f,{g,h}} + {g,{h,f}} + {h,{f,g}} = 0
  These are the axioms of a Lie algebra!

  CANONICAL BRACKETS:
  {qᵢ, qⱼ} = 0
  {pᵢ, pⱼ} = 0
  {qᵢ, pⱼ} = δᵢⱼ

  TIME EVOLUTION OF OBSERVABLES:
  df/dt = {f, H} + ∂f/∂t

  CONSERVATION: f is conserved ↔ {f, H} = 0  (f commutes with H)

  QUANTUM MECHANICS CORRESPONDENCE:
  Classical {f, g} → Quantum [F̂, Ĝ]/(iℏ)
  Classical canonical relations → Canonical commutation relations:
  [q̂ᵢ, p̂ⱼ] = iℏδᵢⱼ   (Heisenberg uncertainty principle!)
```

---

## Integrable Systems

A Hamiltonian system with n DOF is **completely integrable** if it has n independent
conserved quantities in involution:

```
  COMPLETELY INTEGRABLE (Liouville-Arnold):
  Exists n functions f₁,...,f_n such that:
  • {fᵢ, H} = 0 for all i  (all conserved)
  • {fᵢ, fⱼ} = 0 for all i,j  (in involution)
  • f₁,...,f_n are independent (gradients linearly independent)

  LIOUVILLE-ARNOLD THEOREM:
  If these hold, the level sets {f₁=c₁,...,f_n=c_n} (when compact)
  are n-dimensional tori T^n.
  Motion on each torus is quasi-periodic: qᵢ(t) = angle variables that
  increase linearly with time.

  ACTION-ANGLE VARIABLES (J, θ):
  J = action (labels the torus): Jᵢ = 1/(2π) ∮ pᵢ dqᵢ
  θ = angle (position on torus): θ̇ᵢ = ∂H/∂Jᵢ = ωᵢ (const. freq.)

  H(J) depends only on J → Hamilton's eqs trivially solved.

  EXAMPLES OF INTEGRABLE SYSTEMS:
  • 1D systems with conservative force (n=1, trivially integrable)
  • Harmonic oscillator in any dimension
  • Kepler problem (planetary motion): H,L²,Lz conserved
  • Euler's rigid body (torque-free): H,L²,L₃ conserved
  • KdV soliton equation (infinite-dimensional, ∞ conserved quantities)
  • Toda lattice
  • Hard sphere gas in 1D

  NON-INTEGRABLE = CHAOTIC:
  Most systems are NOT integrable.
  KAM theorem: for small perturbations of integrable systems,
  most tori survive but some are destroyed → transition to chaos.
```

---

## Canonical Transformations

Transformations of phase space that preserve Hamilton's equations:

```
  A transformation (q,p) → (Q,P) is CANONICAL if it preserves ω:
  Σ dPᵢ ∧ dQᵢ = Σ dpᵢ ∧ dqᵢ   (symplectic condition)

  Equivalently: {Qᵢ, Qⱼ}_{q,p} = 0,  {Pᵢ, Pⱼ}_{q,p} = 0,
                {Qᵢ, Pⱼ}_{q,p} = δᵢⱼ

  GENERATING FUNCTIONS:
  F₁(q, Q):  p = ∂F₁/∂q,   P = −∂F₁/∂Q,  K = H + ∂F₁/∂t
  F₂(q, P):  p = ∂F₂/∂q,   Q = ∂F₂/∂P,   K = H + ∂F₂/∂t

  STRATEGY: Find a canonical transformation where H(Q,P) = E (constant).
  Then Q̇ = ∂H/∂P = 0, Ṗ = −∂H/∂Q = 0: trivially solved!
  This is the Hamilton-Jacobi approach.

  KEY CANONICAL TRANSFORMATIONS:
  • Identity: F₂ = Σ qᵢPᵢ  (trivial)
  • Point transformation: Q = Q(q), P transforms contravariantly
  • Fourier transform (quantum mechanics): q ↔ p exchange
  • Action-angle: (q,p) → (J,θ) for integrable systems
```

---

## Hamilton-Jacobi Equation

The "ultimate" canonical transformation approach:

```
  Find F₂(q, P, t) = S(q, α, t) [Hamilton's principal function]
  such that the new Hamiltonian K = 0 (motion trivial in (Q,P)).

  Condition: H(q, ∂S/∂q, t) + ∂S/∂t = 0

  HAMILTON-JACOBI EQUATION:
  ┌────────────────────────────────────────────────────────────────┐
  │  ∂S/∂t + H(q, ∂S/∂q, t) = 0                                    │
  └────────────────────────────────────────────────────────────────┘

  This is a PDE for S(q,t). Once solved:
  Q = ∂S/∂P = const   (α's, initial data)
  p = ∂S/∂q

  STATIONARY CASE:  S = W(q) − Et  (time-independent H)
  H(q, ∂W/∂q) = E  (EIKONAL EQUATION for W)

  CONNECTION TO QUANTUM MECHANICS:
  Schrödinger equation: iℏ ∂ψ/∂t = Ĥψ
  WKB ansatz: ψ = e^{iS/ℏ}
  Leading-order O(ℏ⁰): ∂S/∂t + H(q, ∇S) = 0  (Hamilton-Jacobi!)

  Quantum mechanics → classical mechanics as ℏ → 0.
  The action S is the phase of the wavefunction.
```

---

## Statistical Mechanics Connection

Liouville's theorem connects Hamiltonian mechanics to thermodynamics:

```
  MICROCANONICAL ENSEMBLE:
  All phase space points with H(q,p) = E have equal probability.
  Density: ρ ∝ δ(H − E).
  Volume of energy shell Ω(E) = ∫_{H=E} dΩ.
  Entropy: S = k_B log Ω(E).

  CANONICAL ENSEMBLE (Boltzmann):
  System at temperature T.
  Density: ρ ∝ e^{−H/k_BT} (Boltzmann factor).
  Partition function: Z = ∫ e^{−H/k_BT} dqdp.
  Free energy: F = −k_BT log Z.

  ERGODIC HYPOTHESIS:
  Time average of f along trajectory = phase space average of f.
  ∫₀ᵀ f(q(t),p(t)) dt/T → ∫ f ρ dqdp  as T→∞.

  VALIDITY: true for "generic" systems (ergodic by mixing).
  Fails for integrable systems (confined to tori, never ergodic).
  Fails near KAM tori (partially chaotic systems).
```

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| Legendre transform L → H? | H = Σp_i q̇_i − L, with q̇ expressed via p_i = ∂L/∂q̇_i |
| Hamilton's equations? | q̇_i = ∂H/∂p_i, ṗ_i = −∂H/∂q_i |
| Time evolution of observable f? | df/dt = {f,H} + ∂f/∂t |
| When is f conserved? | {f,H} = 0 (f Poisson-commutes with H) |
| Canonical brackets? | {q_i,p_j} = δ_{ij}, {q_i,q_j} = {p_i,p_j} = 0 |
| Phase space volume preserved? | Yes — Liouville's theorem |
| Completely integrable system? | n conserved quantities in involution → action-angle variables |
| H-J equation? | ∂S/∂t + H(q,∇S) = 0 (connects to eikonal equation) |
| Classical → quantum? | {f,g} → [F̂,Ĝ]/(iℏ); S → phase of wavefunction |

---

## Common Confusion Points

**"H = T + V for a pendulum. Why is this different from L = T − V?"**
The Hamiltonian H represents total energy, while the Lagrangian L represents T−V (no direct
physical interpretation as energy). The Legendre transform flips the sign of V. For a simple
particle: L = T−V, H = p²/2m + V = T+V. In relativistic mechanics or field theory, H and L
can look quite different.

**"Liouville's theorem says volumes are preserved. Does this contradict dissipation / attractors?"**
Yes — Hamiltonian systems cannot have attractors. A dissipative system (like a damped oscillator)
is NOT Hamiltonian; you can't write it as q̇=∂H/∂p, ṗ=−∂H/∂q. The damped oscillator's phase
space volume contracts (all trajectories spiral into the origin). Hamiltonian = conservative =
volume-preserving. Dissipative systems require adding non-Hamiltonian terms (Rayleigh dissipation
function in Lagrangian setting, or just augmenting Hamilton's equations).

**"The quantum canonical commutation relations [q̂,p̂]=iℏ — does this come from Poisson brackets?"**
Historically: Dirac (1925) observed the classical → quantum correspondence {f,g}_{classical} →
[F̂,Ĝ]/(iℏ). Dirac's quantization rule: replace Poisson brackets by commutators divided by iℏ.
This gives {q,p}=1 → [q̂,p̂]=iℏ. This is not a derivation — it's a quantization prescription.
The rigorous version is geometric quantization (Kirillov-Kostant-Souriau theory), which uses
the symplectic structure ω to construct the Hilbert space and operators.
