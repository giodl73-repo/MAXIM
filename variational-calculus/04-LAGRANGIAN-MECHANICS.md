# Lagrangian Mechanics

## The Big Picture

Lagrangian mechanics reformulates Newtonian mechanics using the **principle of stationary
action**. It is more powerful than F=ma: it works in any coordinate system, handles
constraints naturally, and directly reveals conservation laws via symmetry.

```
+-----------------------------------------------------------------------+
|              LAGRANGIAN MECHANICS ARCHITECTURE                         |
|                                                                       |
|  NEWTONIAN                 LAGRANGIAN                                 |
|  ---------                 ----------                                 |
|  F = ma for each particle  δS = 0 (action is stationary)             |
|  Coordinates: Cartesian    Generalized coordinates q_i               |
|  Constraints: eliminated   Automatically handled                      |
|  Conservation laws:        Follow from symmetry (Noether)             |
|    found case-by-case       systematically                            |
|  Vectors (forces)          Scalar (Lagrangian function)               |
|  Frame-dependent           Covariant (works in any frame)             |
|                                                                       |
|  CENTRAL OBJECT:  L(q, q̇, t) = T − V                                |
|  T = kinetic energy,  V = potential energy                            |
|                                                                       |
|  E-L EQUATIONS:   d/dt(∂L/∂q̇ᵢ) = ∂L/∂qᵢ                           |
|  "Momentum rate = generalized force"                                  |
|                                                                       |
+-----------------------------------------------------------------------+
```

---

## From Newton to Lagrange

### D'Alembert's Principle (The Bridge)

```
  VIRTUAL WORK PRINCIPLE:
  For a system of N particles at equilibrium, the virtual work of
  all forces through any virtual displacement δr is zero:
  Σᵢ Fᵢ · δrᵢ = 0  (virtual displacements δr consistent with constraints)

  D'ALEMBERT'S PRINCIPLE (dynamics):
  Extend to dynamics by including inertial forces:
  Σᵢ (Fᵢ − mᵢr̈ᵢ) · δrᵢ = 0

  KEY STEP: eliminate constraint forces from the equation.
  Write rᵢ = rᵢ(q₁,...,q_n, t) (parameterize by generalized coords).
  Constraint forces do no virtual work → disappear from the equation.
  → ONLY APPLIED FORCES remain.
```

### Generalized Coordinates

```
  A system with N particles in 3D has 3N degrees of freedom.
  Holonomic constraints reduce these to n < 3N DOF.

  GENERALIZED COORDINATES: q = (q₁,...,q_n)
  Any convenient set of independent parameters that fully describe
  the configuration of the system.

  EXAMPLES:
  ┌─────────────────────────────────────────────────────────────────┐
  │ Double pendulum:     q = (θ₁, θ₂)  (two angles)               │
  │ Rigid body rotation: q = (φ, θ, ψ)  (Euler angles)            │
  │ Molecule:            q = (COM position, bond lengths, angles)  │
  │ Elastic rod:         q(s,t) = shape function (infinite DOF)    │
  │ EM field:            q = A_μ(x,t)  (gauge potential — field)   │
  └─────────────────────────────────────────────────────────────────┘

  TRANSFORMATION:
  rᵢ = rᵢ(q₁,...,q_n, t)   (particle positions from generalized coords)
  ṙᵢ = Σⱼ (∂rᵢ/∂qⱼ)q̇ⱼ + ∂rᵢ/∂t
```

---

## The Lagrangian and the E-L Equations

```
  LAGRANGIAN:  L(q, q̇, t) = T(q, q̇, t) − V(q, t)

  KINETIC ENERGY:
  T = ½ Σᵢ mᵢ|ṙᵢ|² = ½ Σⱼₖ Mⱼₖ(q) q̇ⱼ q̇ₖ
  (M = mass matrix, depends on q for curvilinear coordinates)

  EULER-LAGRANGE EQUATIONS:
  d/dt(∂L/∂q̇ᵢ) − ∂L/∂qᵢ = 0  for i = 1,...,n

  NOTATION:
  pᵢ ≡ ∂L/∂q̇ᵢ   (CANONICAL MOMENTUM conjugate to qᵢ)
  Qᵢ ≡ ∂L/∂qᵢ   (GENERALIZED FORCE)

  E-L: ṗᵢ = Qᵢ   ("Newton's 2nd in generalized form")
```

---

## Key Examples

### Simple Pendulum

```
  Generalized coordinate: q = θ (angle from vertical)
  Position: x = ℓ sin θ, y = −ℓ cos θ

  T = ½mℓ²θ̇²
  V = −mgℓ cos θ  (zero at top)

  L = T − V = ½mℓ²θ̇² + mgℓ cos θ

  ∂L/∂θ̇ = mℓ²θ̇,   ∂L/∂θ = −mgℓ sin θ

  E-L: d/dt(mℓ²θ̇) + mgℓ sin θ = 0
       mℓ²θ̈ + mgℓ sin θ = 0
       θ̈ + (g/ℓ) sin θ = 0   ← nonlinear pendulum equation

  Small angle: θ̈ + (g/ℓ)θ = 0  (SHO with ω = √(g/ℓ))
```

### Double Pendulum

```
  Two rods, lengths ℓ₁, ℓ₂, masses m₁, m₂.
  q = (θ₁, θ₂).

  T = ½m₁ℓ₁²θ̇₁² + ½m₂[(ℓ₁θ̇₁cosθ₁+ℓ₂θ̇₂cosθ₂)² + (ℓ₁θ̇₁sinθ₁+ℓ₂θ̇₂sinθ₂)²]

  T = ½(m₁+m₂)ℓ₁²θ̇₁² + ½m₂ℓ₂²θ̇₂² + m₂ℓ₁ℓ₂θ̇₁θ̇₂cos(θ₁−θ₂)

  V = −(m₁+m₂)gℓ₁cosθ₁ − m₂gℓ₂cosθ₂

  Two coupled nonlinear E-L equations → chaotic dynamics.

  KEY POINT: Lagrangian formulation handles the coupling naturally.
  With Newton's approach: you'd need to find internal forces (tensions)
  in both rods — much more work.
```

### Particle in Electromagnetic Field

```
  L = ½m|ṙ|² − q(φ − ṙ·A/c)

  where φ = electric potential, A = vector potential.

  ∂L/∂ṙ = mṙ + qA/c  (canonical momentum includes field term!)

  E-L: d/dt(mṙ + qA/c) = −q∇φ + q/c ∇(ṙ·A)

  Using dA/dt = ∂A/∂t + (ṙ·∇)A and Maxwell's relations:
  mṙ̈ = q(E + ṙ×B/c)   (Lorentz force)

  KEY POINT: Canonical momentum p = mṙ + qA/c ≠ kinetic momentum mṙ.
  The difference matters for quantum mechanics (minimal coupling).
```

### Rigid Body Rotation

```
  Generalized coordinates: Euler angles (φ, θ, ψ)
  (or quaternion parameterization in modern robotics)

  T = ½ ωᵀ I ω = ½ Σᵢⱼ Iᵢⱼ ωᵢ ωⱼ

  where I = moment of inertia tensor, ω = angular velocity.

  L = ½ ωᵀ I ω − V

  E-L equations → EULER'S EQUATIONS OF RIGID BODY MOTION:
  I₁ω̇₁ − (I₂−I₃)ω₂ω₃ = N₁
  I₂ω̇₂ − (I₃−I₁)ω₃ω₁ = N₂
  I₃ω̇₃ − (I₁−I₂)ω₁ω₂ = N₃

  where N = external torque.
  Without torque: ω precesses in body frame → Euler's free rotation.
```

---

## Conservation Laws from the Lagrangian

```
  CYCLIC COORDINATE:  ∂L/∂qᵢ = 0  (L does not explicitly contain qᵢ)

  → d/dt(∂L/∂q̇ᵢ) = 0  →  pᵢ = ∂L/∂q̇ᵢ = CONST  (conserved)

  EXAMPLES:
  ┌─────────────────────────────────────────────────────────────────┐
  │ L = ½m(ṙ² + r²θ̇²) − V(r)  [central force, polar coords]      │
  │ ∂L/∂θ = 0 → p_θ = mr²θ̇ = const  (angular momentum conserved) │
  │ ∂L/∂θ = 0 means V = V(r) only: isotropy → ang. mom. conserved │
  │                                                                 │
  │ L = ½m(ẋ² + ẏ²) − V(x−a, y)  [translation symmetry in x]    │
  │ ∂L/∂(x−a)/∂x = 0 for translations x→x+c                       │
  │ → px = mẋ = const  (x-momentum conserved)                     │
  └─────────────────────────────────────────────────────────────────┘

  ENERGY CONSERVATION (from time-translation symmetry):
  If L has no explicit t: dH/dt = 0
  H = Σᵢ q̇ᵢ ∂L/∂q̇ᵢ − L = T + V  (when T is quadratic in q̇)
```

---

## Lagrangian for Continuous Systems: Field Theory

The Lagrangian formulation extends naturally to fields (infinite DOF):

```
  LAGRANGIAN DENSITY: L(φ, ∂_μφ, x)  where φ(x,t) is a field.

  ACTION: S[φ] = ∫ L d⁴x  (4D spacetime integral)

  E-L FOR FIELDS (scalar field theory):
  ∂L/∂φ − ∂_μ (∂L/∂(∂_μφ)) = 0

  EXAMPLES:
  ┌─────────────────────────────────────────────────────────────────┐
  │ Free scalar: L = ½(∂_μφ)(∂^μφ) − ½m²φ²                       │
  │   E-L: □φ + m²φ = 0  (Klein-Gordon equation)                  │
  │                                                                 │
  │ EM field: L = −¼ F_μν F^μν  where F = dA (field strength)     │
  │   E-L: ∂_μF^μν = 0  (Maxwell's equations!)                    │
  │                                                                 │
  │ GR: L = √(−g) R  (Einstein-Hilbert action, R = Ricci scalar)  │
  │   E-L: G_μν = 0  (Einstein vacuum equations)                  │
  │   With matter: G_μν = 8πT_μν                                  │
  └─────────────────────────────────────────────────────────────────┘

  The entire Standard Model of particle physics is defined by
  a single Lagrangian density — arguably the most compact and
  complete description of physics yet discovered.
```

---

## Advantages Over Newton

```
  ADVANTAGE 1: COORDINATE-FREE
  L = T − V is a scalar.
  E-L equations same form in ANY coordinate system.
  Newton: F = ma requires VECTOR components in the chosen basis.
  Lagrange: choose coordinates for the problem (polar, spherical, etc.).

  ADVANTAGE 2: CONSTRAINTS AUTOMATIC
  Holonomic constraints: just use fewer generalized coordinates.
  Constraint forces never appear (they do no virtual work).
  Newton: must explicitly find normal forces, tension, etc.

  ADVANTAGE 3: CONSERVED QUANTITIES SYSTEMATIC
  Cyclic coordinate → conserved momentum (trivially).
  Noether's theorem: every symmetry → conservation law.
  Newton: each conservation law requires separate proof.

  ADVANTAGE 4: GENERALIZES BEYOND MECHANICS
  EM fields, quantum fields, general relativity — all use the action principle.
  Newton's F=ma doesn't generalize to these contexts.

  DISADVANTAGE:
  L = T − V only works for conservative forces.
  Friction, non-conservative forces: add Rayleigh dissipation function.
  L = L(q,q̇,t) doesn't directly give constraint forces (multipliers do).
```

---

## Constraints: Worked Comparison

```
  PROBLEM: Particle on a sphere of radius R in gravity.

  NEWTONIAN APPROACH:
  Three coordinates (x,y,z) + constraint x²+y²+z² = R².
  Forces: gravity (−mg ẑ) + normal force N (radial).
  Newton: m(ẍ,ÿ,z̈) = (0,0,−mg) + N(x,y,z)/R
  Four equations (3 Newton + constraint) for four unknowns (x,y,z,N).
  Awkward: N must be solved for.

  LAGRANGIAN APPROACH:
  Two coordinates (θ,φ) (spherical angles), constraint solved by choice.
  T = ½mR²(θ̇² + sin²θ·φ̇²)
  V = −mgR cos θ
  E-L for θ: mR²θ̈ = mR²sinθcosθ·φ̇² − mgR sinθ
  E-L for φ: d/dt(mR²sin²θ·φ̇) = 0   (φ is cyclic if V is axisymmetric)
  Two equations, two unknowns. Normal force never appears.
```

---

## Decision Cheat Sheet

| Situation | Lagrangian approach |
|-----------|---------------------|
| Particle in gravity | L = ½mṙ² − mgz; E-L gives Newton's 2nd |
| Central force | Polar coords; p_θ = mr²θ̇ conserved |
| Constraint (ball on surface) | Use 2 angular coords; constraint solved by construction |
| EM field | L = ½mṙ² − q(φ − ṙ·A/c); canonical momentum p = mṙ + qA/c |
| Rigid body | Euler angles; T = ½ωᵀIω |
| Field theory | Lagrangian density L(φ,∂φ); E-L = PDE for fields |
| Conserved quantity | Find cyclic coordinate (∂L/∂qᵢ = 0) |

---

## Common Confusion Points

**"Canonical momentum p = ∂L/∂q̇ — is this the same as mv?"**
Only for free particles or simple potentials. For a particle in an EM field:
p = mv + qA/c (canonical momentum includes the vector potential contribution).
In curved coordinates: p = Σ M_{ij}q̇ⱼ (involves the mass matrix). In quantum mechanics,
canonical momentum corresponds to −iℏ∂/∂q, not to kinematic momentum mv = −iℏ∂/∂q − qA/c.

**"Is the Lagrangian always T − V?"**
No — T − V is correct for conservative mechanical systems. For EM fields: L = −¼F_μνF^μν.
For relativistic particle: L = −mc²√(1−v²/c²) − V. For dissipative systems: no standard
Lagrangian exists (Rayleigh function added separately). The definition of L is: the function
whose E-L equations give the correct equations of motion.

**"The principle of least action — but is the action really minimized?"**
Not always — it's stationary (δS=0), which could be a minimum, maximum, or saddle.
For short paths, S is typically a minimum. For long paths or paths that have passed conjugate
points, S can be a saddle point. The physical trajectory is the unique stationary path
satisfying the boundary conditions — minimum or not.
