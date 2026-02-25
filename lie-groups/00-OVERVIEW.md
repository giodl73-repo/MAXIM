# Lie Groups — Landscape and Directory Map

## The Big Picture

A Lie group is a group that is also a smooth manifold — algebraic structure and geometric structure
fused into one object. The multiplication and inversion maps are smooth. This fusion is the entire
point: Lie groups are the mathematical language of continuous symmetry.

```
+------------------------------------------------------------------+
|                     LIE GROUPS: THE LANDSCAPE                    |
+------------------------------------------------------------------+
|                                                                  |
|  CONCRETE MATRIX GROUPS           ABSTRACT STRUCTURE             |
|  (the examples you work with)     (the theory behind them)       |
|                                                                  |
|  GL(n,R), GL(n,C)  ──────────┐   Lie Algebra  g = T_e G         |
|  SL(n,R), SL(n,C)  ──────────┤   Bracket [X,Y]: g × g → g       |
|  O(n), SO(n)        ──────────┤   Exponential map exp: g → G     |
|  U(n), SU(n)        ──────────┤   Baker-Campbell-Hausdorff        |
|  Sp(2n)             ──────────┘   Lie's three theorems            |
|         |                                   |                    |
|         v                                   v                    |
|  +------------------+          +----------------------+          |
|  | REPRESENTATIONS  |          | CLASSIFICATION       |          |
|  | G → GL(V)        |          | A_n  B_n  C_n  D_n   |          |
|  | Schur's lemma    |          | E6   E7   E8          |          |
|  | Characters χ(g)  |          | F4   G2               |          |
|  | Peter-Weyl thm   |          | Dynkin diagrams       |          |
|  +------------------+          +----------------------+          |
|         |                                   |                    |
|         v                                   v                    |
|  +----------------------------------------------------------+    |
|  |                    APPLICATIONS                           |    |
|  |  Physics: gauge theory, SU(3)×SU(2)×U(1) Standard Model |    |
|  |  Geometry: principal bundles, connections, holonomy      |    |
|  |  ML: equivariant networks, SE(3)-GNNs                    |    |
|  |  Robotics: SE(3) rigid body kinematics                   |    |
|  |  Harmonic analysis: Fourier as Peter-Weyl on S¹          |    |
|  +----------------------------------------------------------+    |
|                                                                  |
+------------------------------------------------------------------+
```

---

## Why Lie Groups Matter

### Three Independent Motivations (that turn out to be the same thing)

**From physics:** Every conservation law corresponds to a continuous symmetry (Noether's theorem).
Energy conservation ↔ time translation invariance. Momentum ↔ spatial translation. Angular momentum
↔ rotational symmetry SO(3). The Standard Model of particle physics *is* a Lie group: SU(3)×SU(2)×U(1).

**From mathematics:** The classification of simple Lie algebras — completed by Killing and Cartan in the
1880s–90s — is one of the great achievements of 19th-century mathematics. Four infinite families
(A, B, C, D) and five exceptional cases (G₂, F₄, E₆, E₇, E₈). Clean, finite, complete.

**From modern ML/robotics:** Neural networks that process 3D geometry need to be *equivariant* under
rotations and translations — what the network learns should not depend on how you orient the molecule
or robot in space. The symmetry group is SE(3) = SO(3) ⋉ R³ (special Euclidean group). Building
equivariance into architecture requires understanding Lie group representations.

---

## The Central Idea: Local = Global for Lie Groups

The key insight connecting Lie algebra to Lie group:

```
INFINITESIMAL (local, linear, easy)   ←→   GLOBAL (nonlinear, curved)
       Lie algebra  g                            Lie group  G
       tangent space at identity               the full manifold
       bracket [X,Y]                           multiplication g·h
       structure constants                     global topology

    exp: g ──────────────────────────────────> G
         X  ──────────────────────────────────> e^X

    log: G ──────────────────────────────────> g  (near identity)
```

The exponential map lets you study the group (curved, nonlinear) by studying the algebra (flat,
linear). This is the fundamental computational tool — most practical calculations happen in g, then
you exponentiate.

---

## The Five-Level Hierarchy

```
LEVEL 1: TOPOLOGICAL GROUP
  Group G + Hausdorff topology, multiplication and inversion continuous
  Example: (R, +), (S¹, ×), (GL(n,R), matrix multiplication)

       ↓  add smooth structure

LEVEL 2: LIE GROUP
  Topological group where G is a smooth manifold,
  multiplication G×G → G and inversion G → G are smooth maps
  Example: GL(n,R) open subset of M_n(R) ≅ R^(n²)

       ↓  differentiate at identity

LEVEL 3: LIE ALGEBRA  g = Lie(G) = T_e G
  Tangent space at identity with Lie bracket [·,·]
  Skew-symmetric: [X,Y] = -[Y,X]
  Jacobi identity: [X,[Y,Z]] + [Y,[Z,X]] + [Z,[X,Y]] = 0

       ↓  classify

LEVEL 4: ROOT SYSTEM  Φ ⊂ h*
  For semisimple g: Cartan subalgebra h, roots α,
  Weyl group W, Dynkin diagram

       ↓  represent

LEVEL 5: REPRESENTATION  ρ: G → GL(V)
  Irreducible reps classified by highest weights
  Physical fields live here
```

---

## Directory Map

| File | Topic | Key Concepts |
|------|-------|-------------|
| 01-MATRIX-GROUPS.md | Concrete matrix Lie groups | GL, SL, O, SO, U, SU, Sp — definitions, topology, compactness |
| 02-LIE-ALGEBRAS.md | Lie algebra theory | Bracket, exponential map, BCH formula, Lie's theorems |
| 03-REPRESENTATIONS.md | Representation theory | Irreps, Schur's lemma, characters, Peter-Weyl |
| 04-SU2-SO3.md | SU(2) and SO(3) in depth | Double cover, spinors, quaternions, angular momentum |
| 05-ROOT-SYSTEMS.md | Root systems and weights | Roots, coroots, Weyl group, Dynkin diagrams, Cartan matrix |
| 06-SEMISIMPLE.md | Classification theorem | A_n/B_n/C_n/D_n, exceptional algebras, Killing form |
| 07-GAUGE-THEORY.md | Physics applications | U(1), SU(2), SU(3), Standard Model gauge group |
| 08-DIFFERENTIAL-GEOMETRY.md | Geometry applications | Principal bundles, connections, curvature, holonomy |
| 09-APPLICATIONS.md | Modern applications | Equivariant NNs, robotics SE(3), Fourier on groups |

---

## Prerequisites and Cross-References

```
WHAT YOU NEED TO KNOW FIRST:
+-------------------+     +-------------------+     +-------------------+
| Linear Algebra    |     | Multivariable Calc|     | Group Theory      |
| Eigenvalues       |     | Manifolds, tangent|     | Homomorphisms     |
| Determinants      |     | spaces, smooth    |     | Quotient groups   |
| Inner products    |     | maps, derivatives |     | Normal subgroups  |
+-------------------+     +-------------------+     +-------------------+
         \                        |                        /
          \                       v                       /
           +----------------------------------------------+
           |              THIS DIRECTORY                   |
           |  Lie groups = groups + smooth manifold        |
           +----------------------------------------------+
                          |              |
           +--------------+              +--------------+
           v                                            v
+-------------------+                        +-------------------+
| Algebraic Topology|                        | Differential Geom |
| Homotopy groups   |                        | Fiber bundles      |
| Covering spaces   |                        | Riemannian metrics |
+-------------------+                        +-------------------+
```

---

## Historical Arc

| Period | Mathematician | Contribution |
|--------|--------------|--------------|
| 1870s | Sophus Lie | Continuous groups of transformations of ODEs |
| 1880s | Wilhelm Killing | Classification of complex simple Lie algebras |
| 1894 | Élie Cartan | Corrected Killing's work, completed classification |
| 1900s | Cartan | Exterior calculus, symmetric spaces |
| 1913 | Weyl | Character formula for compact groups |
| 1920s | Weyl | Quantum mechanics + representation theory |
| 1954 | Yang–Mills | Non-Abelian gauge theory: SU(2) in physics |
| 1973 | Standard Model | SU(3)×SU(2)×U(1) established |
| 2017+ | SE(3)-GNNs | Equivariant networks for 3D geometry |

---

## The Compact/Non-Compact Divide

The most important structural distinction:

```
COMPACT LIE GROUPS                  NON-COMPACT LIE GROUPS
+-------------------------+          +-------------------------+
| SO(n), SU(n), Sp(n)     |          | GL(n,R), SL(n,R)        |
| U(n), O(n)              |          | SO(p,q) Lorentz group   |
|                         |          | Sp(2n,R) symplectic     |
| Properties:             |          |                         |
| - Finite volume         |          | Properties:             |
| - All reps unitary      |          | - Infinite volume       |
| - Peter-Weyl applies    |          | - Infinite-dim unitary  |
| - Representations       |          |   reps (for physics)    |
|   are fully reducible   |          | - Harish-Chandra theory |
| - Weyl's theorem        |          |                         |
+-------------------------+          +-------------------------+
   PHYSICS: internal sym                PHYSICS: spacetime sym
   (gauge groups)                       (Poincaré, Lorentz)
```

**Rule of thumb:** Compact groups have beautiful finite-dimensional representation theory. Non-compact
groups require functional analysis for their unitary representations. The Standard Model gauge group
is compact. Spacetime symmetry groups (Poincaré, Lorentz) are not.

---

## Common Confusion Points

**"Lie group vs Lie algebra" confusion:** The group G is the geometric object (curved). The algebra
g is the linearization at the identity (flat). They contain the same information locally (Lie's
third theorem). Globally, multiple non-isomorphic groups can share the same Lie algebra — they
differ in topology (connected components, fundamental group).

**"The exponential map isn't exp(matrix)":** For matrix groups it *is* the matrix exponential
exp(X) = Σ Xⁿ/n!. For abstract Lie groups it's defined via integral curves of left-invariant vector
fields. They agree for matrix groups, which is why matrix groups are the right starting point.

**"SU(2) and SO(3) are different":** They have the same Lie algebra but SU(2) is the double cover
of SO(3). This is not a technicality — it is why spinors exist in quantum mechanics. A spin-1/2
particle picks up a factor of -1 under 2π rotation. See 04-SU2-SO3.md.

**"Simple vs semisimple":** Simple: no nontrivial ideals. Semisimple: direct sum of simples (no
abelian ideals). Every compact connected Lie group is locally a product of a semisimple group and
a torus (abelian). U(1) is simple as an abelian group but its Lie algebra is 1-dimensional abelian,
not simple in the Lie algebra sense.
