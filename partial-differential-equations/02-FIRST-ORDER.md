# First-Order PDEs and Method of Characteristics

## The Big Picture

First-order PDEs are the entry point to PDE theory and reveal the deepest geometric ideas.
The method of characteristics turns a PDE into a system of ODEs — reducing a harder problem
to a solved one.

```
+-----------------------------------------------------------------------+
|              FIRST-ORDER PDE TAXONOMY                                  |
|                                                                       |
|  LINEAR:         a(x,y)u_x + b(x,y)u_y = c(x,y)                     |
|                  Characteristics: ODEs dx/a = dy/b = du/c             |
|                                                                       |
|  SEMILINEAR:     a(x,y)u_x + b(x,y)u_y = c(x,y,u)                  |
|                  Characteristics: same curves, but u evolves          |
|                  nonlinearly along them                               |
|                                                                       |
|  QUASILINEAR:    a(x,y,u)u_x + b(x,y,u)u_y = c(x,y,u)              |
|                  Characteristics DEPEND ON SOLUTION u                 |
|                  → characteristics can cross → SHOCKS                 |
|                                                                       |
|  FULLY NONLINEAR: F(x,y,u,u_x,u_y) = 0                              |
|                  More complex geometry; Monge cones; Hamilton-Jacobi  |
|                                                                       |
|  KEY RESULTS:                                                         |
|  • Every first-order PDE is hyperbolic (info propagates along chars)  |
|  • Characteristics can cross → solution becomes multi-valued → shocks |
|  • Entropy condition selects the "physical" weak solution             |
|                                                                       |
+-----------------------------------------------------------------------+
```

---

## Linear First-Order PDEs: Transport Equation

The simplest first-order PDE:

```
  u_t + c·u_x = 0,   u(x,0) = u₀(x)

  Physical meaning: u is transported rigidly at speed c.

  Solution:  u(x,t) = u₀(x − ct)

  Proof: Set ξ = x − ct. Then u(x,t) = u₀(ξ).
  Check: u_t = u₀'(ξ)·(−c),  u_x = u₀'(ξ)·(1)
         u_t + c·u_x = u₀'(ξ)·(−c + c) = 0.  ✓

  CHARACTERISTICS:  lines x − ct = const (slope 1/c in x-t plane)
                    Solution is CONSTANT along each characteristic.
```

---

## Method of Characteristics: The General Theory

For a quasilinear first-order PDE in two variables:

```
  a(x,y,u) u_x + b(x,y,u) u_y = c(x,y,u)     (*)

  GEOMETRIC VIEW:
  Think of the solution u(x,y) as a surface z = u(x,y) in (x,y,z)-space.
  The PDE says the normal to the surface (u_x, u_y, −1) is perpendicular
  to the vector field V = (a, b, c):
      V · (u_x, u_y, −1) = a·u_x + b·u_y − c = 0

  So the vector field V is TANGENT to the solution surface.

  CHARACTERISTIC EQUATIONS:
  The curves (x(t), y(t), z(t)) tangent to V satisfy:
      dx/dt = a(x,y,z)
      dy/dt = b(x,y,z)
      dz/dt = c(x,y,z)

  These are ODESS — solve them to find the solution surface.
```

### Algorithm: Method of Characteristics

```
  GIVEN: PDE  a(x,y,u) u_x + b(x,y,u) u_y = c(x,y,u)
         IC:  u(x,0) = u₀(x)  (data on y=0 curve)

  STEP 1: Parameterize initial data.
          At y=0: x = x₀, z = u₀(x₀)  (parameter: x₀)

  STEP 2: Solve the characteristic ODEs.
          For each starting point (x₀, 0, u₀(x₀)):
          dx/dt = a(x,y,z),  x(0) = x₀
          dy/dt = b(x,y,z),  y(0) = 0
          dz/dt = c(x,y,z),  z(0) = u₀(x₀)

  STEP 3: The solution curves (x(t;x₀), y(t;x₀), z(t;x₀))
          sweep out the solution surface z = u(x,y).

  STEP 4: Invert: given (x,y), find (t,x₀) such that
          x(t;x₀) = x, y(t;x₀) = y.
          Then u(x,y) = z(t;x₀).
```

---

## Worked Example: Variable-Coefficient Transport

```
  PDE:   u_t + x·u_x = 0,  u(x,0) = u₀(x)

  Characteristic equations:
      dx/dt = x,   x(0) = x₀
      dt/dt = 1,   t(0) = 0
      dz/dt = 0,   z(0) = u₀(x₀)

  Solve:  x(t) = x₀·e^t,  t(t) = t,  z(t) = u₀(x₀)

  Invert: x₀ = x·e^{−t}

  Solution:  u(x,t) = u₀(x·e^{−t})

  The characteristics are x = x₀·e^t (exponential expansion).
  Information from x₀ at t=0 arrives at x = x₀·e^t at time t.
```

---

## Quasilinear PDEs and Shock Formation

The inviscid Burgers equation is the prototype:

```
  u_t + u·u_x = 0,   u(x,0) = u₀(x)

  Physical meaning: each "parcel" of fluid moves at speed u.
  Fast parts overtake slow parts → compression → shock.

  CHARACTERISTIC EQUATIONS:
      dx/dt = u,   x(0) = x₀
      dt/dt = 1
      du/dt = 0,   u(0) = u₀(x₀)

  Solution along characteristics:  u = u₀(x₀) = const
  Characteristics:  x = x₀ + u₀(x₀)·t  (straight lines in x-t plane)

  SHOCK FORMATION:
  Characteristics cross when a faster one (higher u₀) catches a
  slower one (lower u₀).

  Two characteristics x₀ and x₀+δ cross when:
  x₀ + u₀(x₀)t = x₀+δ + u₀(x₀+δ)t
  → t = −δ/(u₀(x₀+δ) − u₀(x₀)) → −1/u₀'(x₀)  as δ→0

  BREAKING TIME:  t_b = min_{x₀} { 1/(−u₀'(x₀)) : u₀'(x₀) < 0 }

  Shock forms at the minimum of 1/(−u₀') where u₀' < 0.
  (Wherever the initial profile has a downward slope.)
```

### Shock Diagram

```
  Initial data: u₀(x) = 1 for x<0, 0 for x>0 (step function — a shock)

  x-t DIAGRAM:
  t
  ^   /  /  /  /  |\ \ \ \
  |  / fast /  |   \ slow\
  | / chars/   |    \chars\
  |/      /    |     \     \
  +-------+----+-----------+---> x
                |
            x = shock position (moves right at speed ½)

  Characteristics from x<0 all have speed u₀=1 (slope 1 in t-x).
  Characteristics from x>0 all have speed u₀=0 (vertical).
  → Initial shock is a shock for all time.

  RANKINE-HUGONIOT CONDITION:
  Shock speed s = [f(u_R) − f(u_L)] / (u_R − u_L)
  where f(u) = u²/2 (flux for Burgers).
  Here: s = (0 − ½)/(0 − 1) = ½.
```

---

## Weak Solutions and the Entropy Condition

When characteristics cross, classical (smooth) solutions break down.
The PDE must be interpreted in the **weak** (integral) sense.

```
  WEAK FORMULATION of u_t + f(u)_x = 0:

  ∫∫ [u·φ_t + f(u)·φ_x] dx dt = 0  for all test functions φ ∈ C_c^∞

  Allows discontinuous solutions (shocks).

  BUT: weak solutions are not unique in general.

  ENTROPY CONDITION (Oleinik / Lax):
  Physical shocks must satisfy: characteristics impinge on the shock.

  For scalar conservation law u_t + f(u)_x = 0,
  across a shock with speed s:
      f'(u_L) > s > f'(u_R)

  (Characteristics from both sides run into the shock, not away.)

  ALTERNATIVE (Entropy pairs):
  The physical solution satisfies ∂_t η(u) + ∂_x q(u) ≤ 0
  for all convex entropy functions η (with entropy flux q = η'f').
```

---

## Rarefaction Waves

Not all initial data leads to shocks. Where characteristics spread apart,
you get a **rarefaction wave** (smooth expansion fan):

```
  Initial data: u₀(x) = 0 for x<0, 1 for x>0 (step up)

  Characteristics from x<0: speed u₀=0 (vertical).
  Characteristics from x>0: speed u₀=1 (slope 1).
  GAP between them (0 < x/t < 1): fill with rarefaction.

  Rarefaction solution: u(x,t) = x/t  for 0 < x/t < 1.

  x-t DIAGRAM:
  t
  ^  |      /
     |  rf /
     | fan/
     |   /
     |  /
     | /
     +---------> x
     0

  The fan fills in self-similar: u = x/t along rays x/t = const.
```

---

## General First-Order Systems: Cauchy-Kovalevskaya

```
  CAUCHY-KOVALEVSKAYA THEOREM:

  For a PDE F(x,u,∂u/∂x_i,...) = 0 analytic near a point,
  with analytic initial data on a non-characteristic surface:
  → A unique analytic solution exists near that surface.

  This is the PDE analogue of the ODE existence theorem.

  LIMITATIONS:
  • Requires ANALYTICITY (real analytic functions — very restrictive)
  • Non-characteristic surface (solution can be specified there)
  • Local result only
  • Fails for ill-posed problems (backward heat equation is analytic
    but the Cauchy problem is still ill-posed in the Hadamard sense)

  The Holmgren uniqueness theorem complements it:
  If an analytic PDE has two C∞ solutions with the same analytic
  Cauchy data, they must agree locally.
```

---

## Hamilton-Jacobi Equation

The fully nonlinear first-order PDE connecting characteristics to optimal control:

```
  H(x, ∇S) = E   (time-independent Hamilton-Jacobi)
  or:
  S_t + H(x, ∇S) = 0   (time-dependent Hamilton-Jacobi)

  where H is the Hamiltonian, S is the "action" function.

  CHARACTERISTICS = HAMILTONIAN RAYS:
      dx_i/dt = ∂H/∂p_i
      dp_i/dt = −∂H/∂x_i
  where p = ∇S.

  These are exactly Hamilton's equations from mechanics!

  CONNECTION TO OPTICS:
  The eikonal equation |∇S|² = n(x)² is H-J with H = |p|²/n².
  Characteristics = light rays (Fermat's principle).

  CONNECTION TO OPTIMAL CONTROL:
  The Bellman value function V(x,t) = min-cost-to-go satisfies
  the HJB equation: V_t + min_u [f(x,u)·∇V + L(x,u)] = 0.
  (See variational-calculus/08-OPTIMAL-CONTROL.md)

  VISCOSITY SOLUTIONS (Crandall-Lions, 1983):
  H-J equations need a notion of weak solution — viscosity solutions —
  because classical solutions generically develop singularities.
```

---

## Decision Cheat Sheet

| Situation | Method |
|-----------|--------|
| Linear first-order PDE | Method of characteristics (ODE system) |
| Quasilinear first-order PDE | Method of characteristics; watch for shock formation |
| When do shocks form? | When characteristics cross (t_b = 1/max(−u₀')) |
| Multiple shocks / complex data | Weak solutions with entropy condition |
| Smooth expansion regions | Rarefaction wave (self-similar solution) |
| Fully nonlinear first-order | Hamilton-Jacobi theory; viscosity solutions |
| Analytic coefficients + analytic data | Cauchy-Kovalevskaya theorem (local existence) |
| Conservation law u_t + f(u)_x = 0 | Rankine-Hugoniot condition for shock speed |

---

## Common Confusion Points

**"Why do characteristics move at speed u in Burgers' equation?"**
Because the PDE says u_t + u·u_x = 0. Rewrite: Du/Dt = 0 along curves dx/dt = u. This
says u is constant along the curves where the curve speed equals u. So each "bit" of fluid
carries its velocity with it — faster bits move faster, eventually overtaking slower bits.

**"The solution is multi-valued after characteristics cross — what does that mean?"**
It means the classical smooth solution no longer exists. The graph of u becomes folded.
The physical resolution is a shock — a discontinuity where the solution jumps. The
Rankine-Hugoniot condition tells you how fast the jump moves. The entropy condition
tells you which jump is physical (characteristics must enter the shock, not leave it).

**"Rarefaction vs. shock — how do I know which one I get?"**
Look at the initial profile. Where u₀ is decreasing (compressive), characteristics converge
→ shock. Where u₀ is increasing (expansive), characteristics diverge → rarefaction.
For a step function: step down → shock, step up → rarefaction.

**"Does the method of characteristics work in 3D?"**
Yes. For a(x,y,z,u)u_x + b(·)u_y + c(·)u_z = d(·) you get a 4-component ODE system
(x,y,z,u)(t). The same geometric picture holds: solution is a 3-manifold in 4-space swept
out by the characteristic curves.
