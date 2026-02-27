# Electrostatics — Charges, Fields, and Potential

## The Big Picture

Electrostatics is E&M with everything frozen in time. No moving charges,
no changing fields. Just charges sitting still and the fields they create.
It is the foundation everything else builds on.

```
+------------------------------------------------------------------------+
|                      ELECTROSTATICS LANDSCAPE                          |
|                                                                        |
|   SOURCE          CREATES            FIELD          DESCRIBED BY       |
|   ──────          ───────            ─────          ────────────       |
|                                                                        |
|   charge q  ──>  force on           E(x,y,z)       ∇·E  = ρ/ε₀       |
|   (scalar)        other charges     vector field    ∇×E  = 0           |
|                                          │                             |
|                                          │ E = -∇V                    |
|                                          ▼                             |
|                                     V(x,y,z)       ∇²V = -ρ/ε₀       |
|                                     scalar field   (Poisson)           |
|                                                    ∇²V = 0             |
|                                                    (Laplace, no charge) |
+------------------------------------------------------------------------+
```

The whole of electrostatics is:
1. Charges create E fields
2. E fields exert forces on other charges
3. V is a scalar shortcut — one number per point instead of three
4. Everything reduces to solving Poisson's or Laplace's equation

---

## Charge

Electric charge is a fundamental property of matter. Two facts dominate everything:

**Quantization**: charge comes in integer multiples of the elementary charge:

```
  e = 1.602 × 10⁻¹⁹ C     (C = Coulomb, the SI unit)

  Electron: q = -e
  Proton:   q = +e
  Neutron:  q = 0
```

**Superposition**: electric effects add linearly. The force on charge q from
a collection of other charges is the vector sum of individual forces. This
linearity is non-trivial — it is a property of the vacuum and breaks down
at extreme field strengths (nonlinear QED).

**Charge density**: for continuous distributions instead of point charges:

```
  ρ(x,y,z)  — volume charge density (C/m³)
  σ(x,y)    — surface charge density (C/m²)
  λ(x)      — line charge density (C/m)

  Total charge in volume V:  Q = ∫∫∫_V ρ dV
```

---

## Coulomb's Law

Force between two point charges q₁ and q₂ separated by distance r:

```
         1    q₁q₂
  F  =  ───  ─────  r̂
        4πε₀   r²

  r̂ = unit vector pointing from q₁ to q₂
  ε₀ = 8.854 × 10⁻¹² C²/(N·m²)   (permittivity of free space)
  1/4πε₀ = 8.988 × 10⁹ N·m²/C²   ≈ 9 × 10⁹
```

Same sign → F points along +r̂ → repulsion.
Opposite sign → F points along -r̂ → attraction.

**The r² falloff** — inverse square law. Same geometry as gravity (Newton).
Not a coincidence — both are solutions to Laplace's equation in 3D.
The number of field lines from a point source is fixed; they spread over
a sphere of area 4πr², so density drops as 1/r².

```
  r=1:  ████████   intensity 1
  r=2:  ████       intensity 1/4
  r=3:  ██         intensity 1/9
             ↑
         same number of lines, larger sphere
```

**Coulomb vs. gravity**: electrostatic force between an electron and proton
is ~10³⁶ times stronger than their gravitational attraction. Gravity dominates
at cosmic scales only because matter is electrically neutral in bulk.

---

## Electric Field

Rather than tracking force between every pair of charges, define the **field**:
the force per unit charge that a positive test charge would feel at each point.

```
         F          1    q
  E  =  ───  =    ─────  ─  r̂
        q₀        4πε₀  r²

  E is a vector field: direction + magnitude at every point in space
```

For a point charge q at the origin:
- E points radially outward if q > 0 (source)
- E points radially inward if q < 0 (sink)
- |E| falls as 1/r²

```
  POSITIVE CHARGE (+q)        NEGATIVE CHARGE (-q)

    ↗  ↑  ↖                     ↘  ↓  ↙
    →  +  ←   NO —              →  -  ←   YES
    ↘  ↓  ↙                     ↗  ↑  ↖

    field lines out               field lines in
```

**Superposition**: for multiple charges, E_total is the vector sum:

```
         1    N    qᵢ
  E  =  ───  Σ   ────  r̂ᵢ
        4πε₀ i=1  rᵢ²
```

For continuous distributions, the sum becomes an integral:

```
         1       ρ(r')
  E(r) = ───  ∫ ──────  (r - r') dV'
         4πε₀   |r-r'|³
```

**Field lines**: curves that are everywhere tangent to E. They:
- Start on positive charges (sources)
- End on negative charges (sinks)
- Never cross (E is single-valued)
- Density of lines ∝ |E| (closer together = stronger field)

---

## Gauss's Law — The Shortcut for Symmetric Problems

Applying the divergence theorem (from vector calculus — see `mathematics/01-VECTOR-CALC.md`) to ∇·E = ρ/ε₀ gives:

```
  ∮∮_S E·dA = Q_enc/ε₀

  Net electric flux through any closed surface
  = total charge enclosed / ε₀
```

This is exact and always true. It becomes a *calculation tool* when the
geometry is symmetric enough that |E| is constant over a well-chosen surface.

**The Gaussian surface strategy**:
1. Identify the symmetry (spherical, cylindrical, planar)
2. Choose a surface where E is constant and perpendicular (or parallel) everywhere
3. Pull |E| out of the integral: ∮ E·dA = |E| × (surface area)
4. Set equal to Q_enc/ε₀ and solve for |E|

### Example 1: Point charge (spherical symmetry)

Choose a sphere of radius r centered on charge q.
E is radially outward, perpendicular to sphere everywhere, constant magnitude.

```
  ∮ E·dA = |E| × 4πr²  =  q/ε₀

         q
  |E| = ────    ← recovers Coulomb's law
        4πε₀r²
```

### Example 2: Infinite line charge (cylindrical symmetry)

Line charge density λ (C/m). Choose a cylinder of radius r, length L.

```
  E is radial, perpendicular to curved surface. Zero flux through end caps.

  ∮ E·dA = |E| × 2πrL  =  λL/ε₀

          λ
  |E| = ──────    ← falls as 1/r, not 1/r² (2D source, not 3D)
        2πε₀r
```

### Example 3: Infinite plane of charge (planar symmetry)

Surface charge density σ (C/m²). Choose a pillbox straddling the plane.

```
  E is perpendicular to plane, pointing away on both sides.
  Flux only through the two end caps, each of area A.

  ∮ E·dA = 2|E|A  =  σA/ε₀

          σ
  |E| = ────    ← constant! Independent of distance.
        2ε₀
```

An infinite plane of charge creates a uniform field. This is why parallel
plate capacitors (two planes) create uniform fields between the plates.

---

## Electric Potential V

The electric field E has three components at each point. The potential V has one.
Trading the vector field for a scalar field is always worth it when possible.

**Definition**: V is the work done per unit charge by an external agent moving a
positive test charge from a reference point (usually infinity) to point r:

```
         1    q
  V(r) = ───  ─       (potential of point charge)
         4πε₀ r

  Units: Volts = J/C   (energy per charge — this is the voltage from 6.002)
```

**V and E**: From the gradient theorem (module 02):

```
  E = -∇V

  The electric field is the negative gradient of the potential.
  E points from high V to low V — downhill on the potential surface.

  V(b) - V(a) = -∫_a^b E·dl    (potential difference = line integral of E)
```

This is exactly the voltage you know from circuits:
- Voltage = potential difference between two points
- Batteries maintain a potential difference by doing chemical work
- Current flows from high to low potential (conventional)

**Equipotential surfaces**: surfaces of constant V. Since E = -∇V and gradient
is perpendicular to level surfaces, **E is always perpendicular to equipotentials**.
Field lines cross equipotentials at right angles.

```
  V=30  ─────────────────
  V=20  ─────────────────      →→→→→→→→→  E field lines
  V=10  ─────────────────      (perpendicular to equipotentials)
  V=0   ─────────────────
```

**Superposition for V**: since V is a scalar, superposition is just addition:

```
         1    N   qᵢ
  V  =  ───  Σ  ────      (much easier than vector E superposition)
        4πε₀ i=1  rᵢ
```

Calculate V by scalar addition, then get E by taking -∇V. Often easier than
computing E directly.

---

## Conductors in Electrostatics

A conductor has free electrons that can move in response to E fields.
In static equilibrium, they must have stopped moving. Consequence:

```
  E = 0 inside a conductor (in electrostatics)
```

If E ≠ 0 inside, charges would still be moving — not static equilibrium.

**Consequences**:

```
  1. E = 0 inside conductor
     ↓
  2. V = constant inside conductor
     (E = -∇V = 0 means no gradient means flat potential)
     ↓
  3. Any net charge resides on the surface
     (∇·E = ρ/ε₀, but ∇·E = 0 inside, so ρ = 0 inside)
     ↓
  4. E at the surface is perpendicular to the surface
     (tangential E would accelerate surface charges along surface)
     ↓
  5. E just outside surface: |E| = σ/ε₀
     (apply Gauss's law with a pillbox at the surface)
```

**Faraday cage**: A closed conducting shell shields its interior from external
E fields. E = 0 inside regardless of external field. This is why you're safe
in a car during lightning, and why RF shielding works.

**Sharp points concentrate charge**: Surface charge density σ is highest where
the surface curves most sharply. E = σ/ε₀ is therefore highest at sharp points —
this is how lightning rods work and why Van de Graaff generators spark at edges.

---

## Engineering Bridge: The Laplacian in Computation

```
CONTINUOUS LAPLACIAN               DISCRETE / COMPUTATIONAL EQUIVALENT
──────────────────────────────────────────────────────────────────────────────
∇²V = 0 (Laplace)                  Graph Laplacian L = D - A
  V at each point is the average     V at each node is the average of
  of its neighbors (mean value       its neighbors — same mean value
  property of harmonic functions)    property on the discrete graph

∇²V = -ρ/ε₀ (Poisson)             Lv = b (discrete Poisson equation)
  Source-driven potential              Charge sources at specific nodes
  Solved by: FEM (mesh domain),       Solved by: sparse linear algebra
  BEM (mesh boundary only),            (conjugate gradient, multigrid)
  spectral methods (Fourier basis)

Eigenvalues of ∇²                  Eigenvalues of L (spectral graph theory)
  Modes of vibration, resonance       Fiedler value = algebraic connectivity
  Continuous spectrum for open         Graph partitioning, clustering
  domains; discrete for bounded       Community detection in networks
```

The graph Laplacian L = D - A (where D is the degree matrix and A is the adjacency matrix) is the discrete analog of the continuous Laplacian. Spectral graph theory — PageRank, spectral clustering, graph neural networks — is discrete harmonic analysis. The Poisson equation you solve in electrostatics is the same equation (with different boundary conditions) that FEM solvers solve for structural analysis, heat transfer, and fluid flow.

## Poisson's and Laplace's Equations

From E = -∇V and ∇·E = ρ/ε₀:

```
  ∇·E = ∇·(-∇V) = -∇²V = ρ/ε₀

  ∇²V = -ρ/ε₀        ← POISSON'S EQUATION (charge present)
  ∇²V = 0            ← LAPLACE'S EQUATION (no charge)
```

**This is the workhorse of electrostatics.** Given a charge distribution and
boundary conditions (V on conductors, V at infinity), solve for V everywhere,
then E = -∇V.

**Laplace's equation** ∇²V = 0 governs V in charge-free regions. Its solutions
(harmonic functions) have no local maxima or minima — V smoothly interpolates
between boundary values. This means the potential everywhere between two
conductors is determined entirely by the potentials on those conductors.

```
  PARALLEL PLATE CAPACITOR:

  +V₀ ═══════════════  ← conductor at V = +V₀
                        ← solve ∇²V = 0 between plates
  -V₀ ═══════════════  ← conductor at V = -V₀

  Solution: V(x) = V₀(1 - 2x/d)  — linear between plates
  Field:    E = -∇V = 2V₀/d  (uniform, pointing from + to - plate)
```

---

## Energy in the Electric Field

To assemble a charge distribution, work must be done against (or by) the
Coulomb forces. That energy is stored in the electric field itself.

**Energy density** (energy per unit volume stored in E field):

```
        ε₀
  u = ──── E²     (J/m³)
         2
```

**Total electrostatic energy**:

```
        ε₀
  U = ────  ∫∫∫ E² dV
         2
```

Integrate over all space. The energy is distributed throughout the field,
not localized at the charges. This is a non-trivial statement — the field
is physically real and carries energy.

**Capacitor energy** (connects to 6.002):

```
        1          Q²       1
  U = ─── CV²  =  ────  =  ─── QV
        2          2C        2

  C = ε₀A/d   for parallel plate capacitor (area A, separation d)
```

---

## Decision Cheat Sheet

| Situation | Tool | Why |
|-----------|------|-----|
| Find E from point charge | Coulomb's law | Direct |
| Find E from symmetric distribution | Gauss's law integral form | Pull E out of integral |
| Find E from arbitrary distribution | Solve ∇²V = -ρ/ε₀, then E = -∇V | Scalar easier than vector |
| Find V from E | V = -∫E·dl | Gradient theorem |
| Find E from V | E = -∇V | Gradient |
| V in charge-free region | Solve ∇²V = 0 with boundary conditions | Laplace's equation |
| E inside conductor | E = 0 | Electrostatic equilibrium |
| E just outside conductor | E = σ/ε₀, perpendicular | Boundary condition |
| Energy stored | U = (ε₀/2)∫E² dV | Field energy density |

---

**Forward connections**: The electrostatic energy density u = epsilon_0 E^2 / 2 has a quantum analog: each EM mode carries zero-point energy 1/2 hbar omega (see `09-ZERO-POINT-ENERGY.md`). The macroscopic dielectric constant epsilon arises from the microscopic polarizability of atoms/molecules in a material — the connection to semiconductor physics and band theory is covered in `08-QUANTUM-BRIDGE.md`.

## Common Confusion Points

**V is defined up to a constant — only differences matter.**
Absolute potential has no physical meaning; only ΔV = V(b) - V(a) does.
The choice V = 0 at infinity is a convention, convenient for isolated charges.
In circuit analysis, you choose a ground node as V = 0 arbitrarily.

**E = 0 inside a conductor does NOT mean no charges inside.**
It means no NET charge density inside (ρ = 0). A hollow conductor can have
charges on its inner surface induced by a charge placed inside the cavity.
Gauss's law guarantees the outer surface has equal and opposite charge.

**The 1/r vs 1/r² distinction.**
Point charge (3D source): E ~ 1/r², V ~ 1/r.
Line charge (2D source): E ~ 1/r, V ~ ln(r).
Plane charge (1D source): E ~ constant, V ~ r.
Each reduction in source dimension reduces the falloff by one power of r.

**Gauss's law is always true; the calculation trick only works for symmetry.**
∮ E·dA = Q_enc/ε₀ holds for any closed surface around any charge distribution.
But you can only extract |E| from the integral when symmetry guarantees
constant |E| and constant angle between E and dA across the surface.
Without symmetry, you know the total flux but not the field at each point.

**Potential energy vs potential.**
V is potential energy per unit charge (J/C = Volt).
U = qV is the actual potential energy of charge q in potential V.
When you say "voltage drop of 5V," you mean 5 J/C of energy is released
per unit charge flowing through — exactly as in circuit analysis.
