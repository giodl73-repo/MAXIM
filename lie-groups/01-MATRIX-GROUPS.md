# Matrix Lie Groups — Concrete Examples

## The Big Picture

Matrix Lie groups are Lie groups realized as groups of invertible matrices. They are the primary
working objects — abstract Lie theory is built from and tested against these concrete examples.
Every classical Lie group appears here.

```
+----------------------------------------------------------------------+
|                    MATRIX LIE GROUPS: TAXONOMY                       |
+----------------------------------------------------------------------+
|                                                                      |
|  GENERAL LINEAR (base case)                                          |
|  GL(n,R) = {A in M_n(R) : det A != 0}   dim = n^2                  |
|  GL(n,C) = {A in M_n(C) : det A != 0}   dim = 2n^2                 |
|                                                                      |
|  DETERMINANT-1 CONSTRAINT                                            |
|  SL(n,R) = {A in GL(n,R) : det A = 1}   dim = n^2-1                |
|  SL(n,C) = {A in GL(n,C) : det A = 1}   dim = 2n^2-2               |
|                                                                      |
|  ORTHOGONAL / UNITARY (preserve inner product)                       |
|  O(n)  = {A in GL(n,R) : A^T A = I}     dim = n(n-1)/2             |
|  SO(n) = {A in O(n) : det A = 1}         dim = n(n-1)/2             |
|  U(n)  = {A in GL(n,C) : A† A = I}      dim_R = n^2                |
|  SU(n) = {A in U(n) : det A = 1}         dim_R = n^2-1             |
|                                                                      |
|  SYMPLECTIC (preserve skew form)                                     |
|  Sp(2n,R) = {A in GL(2n,R) : A^T J A = J}  dim = n(2n+1)          |
|  Sp(n) (compact form)                                                |
|                                                                      |
|  CLASSICAL SERIES (Cartan's notation):                               |
|  A_n <-> SU(n+1)  B_n <-> SO(2n+1)  C_n <-> Sp(n)  D_n <-> SO(2n)|
|                                                                      |
+----------------------------------------------------------------------+
```

---

## General Linear Group GL(n,R)

**Definition:** GL(n,R) = { A in M_n(R) : det(A) != 0 }

This is an **open subset** of M_n(R) isomorphic to R^(n^2) — the preimage of R \ {0} under the
continuous map det: M_n(R) -> R. Open subsets of R^m are automatically smooth manifolds, so the
manifold structure is free. The group operations are polynomial in the matrix entries, hence smooth.

```
M_n(R) iso R^(n^2)  --det-->  R
                              |
GL(n,R) = det^{-1}(R\{0})    R \ {0} = (-inf,0) union (0,inf)
                              |
                              Two components:
                              det > 0  ->  orientation-preserving
                              det < 0  ->  orientation-reversing
```

**Topology:**
- dim = n^2
- NOT connected: two components (det > 0 and det < 0)
- NOT compact: entries can go to infinity
- Fundamental group: pi_1(GL(n,R)) = pi_1(O(n)) via deformation retract

**Lie algebra:** gl(n,R) = M_n(R) with bracket [X,Y] = XY - YX (all n x n matrices).

---

## Special Linear Group SL(n,R)

**Definition:** SL(n,R) = { A in GL(n,R) : det(A) = 1 }

The kernel of det: GL(n,R) -> R*. Since det is a Lie group homomorphism, SL(n,R) is a normal
subgroup and a Lie subgroup of GL(n,R).

**Dimension:** The constraint det(A) = 1 removes 1 degree of freedom, so dim = n^2 - 1.

**Lie algebra:** sl(n,R) = { X in M_n(R) : tr(X) = 0 }

Why trace zero? Differentiate det(exp(tX))|_{t=0} = 1:

```
d/dt det(exp(tX))|_{t=0} = tr(X) = 0
```

This is a fundamental fact: det(exp(X)) = exp(tr(X)), so det(exp(X)) = 1 iff tr(X) = 0.

**SL(2,R):** The simplest non-compact non-abelian Lie group. Its unitary representations are
infinite-dimensional and classify into principal series, discrete series, and complementary series.
Relevant to 2D conformal field theory and modular forms.

---

## Orthogonal and Special Orthogonal Groups

**Definition:** O(n) = { A in GL(n,R) : A^T A = I }

These are matrices preserving the Euclidean inner product <x,y> = x^T y on R^n.

```
CONDITION A^T A = I IMPOSES:
  - Each column has unit length
  - Columns are mutually orthonormal
  - det(A) = pm 1  (since det(A^T)det(A) = det(I) = 1)

O(n): det = pm 1, two connected components
SO(n): det = +1, connected (orientation-preserving rotations)
```

**Lie algebra:** so(n) = { X in M_n(R) : X + X^T = 0 } = skew-symmetric matrices.

Dimension: skew-symmetric n x n matrices have n(n-1)/2 free entries (strictly upper triangle).
- so(2): 1-dimensional, spanned by [[0,-1],[1,0]]
- so(3): 3-dimensional, the cross-product algebra (isomorphic to R^3 with cross product)
- so(4): 6-dimensional, isomorphic to so(3) direct sum so(3)

**Topology of SO(n):**

| Group | pi_1 | pi_2 | pi_3 | Notes |
|-------|------|------|------|-------|
| SO(2) | Z | 0 | 0 | Circle S^1 |
| SO(3) | Z/2Z | 0 | Z | Real proj space RP^3 |
| SO(4) | Z/2Z | 0 | Z+Z | |
| SO(n), n>=5 | Z/2Z | 0 | Z | Stable range |

The fact that pi_1(SO(3)) = Z/2Z is why SU(2) -> SO(3) is a double cover. See 04-SU2-SO3.md.

**Low-dimensional isomorphisms:**
```
SO(2) iso U(1) iso S^1
SO(3) iso SU(2)/Z_2 iso RP^3
SO(4) iso (SU(2) x SU(2))/Z_2
```

---

## Unitary and Special Unitary Groups

**Definition:** U(n) = { A in GL(n,C) : A† A = I }

where A† = conj(A)^T (conjugate transpose). These are matrices preserving the Hermitian inner
product <x,y> = x† y on C^n.

```
REAL vs COMPLEX:
  O(n)  subset GL(n,R): preserves real inner product x^T y
  U(n)  subset GL(n,C): preserves complex inner product x† y

U(n) generalizes O(n) to the complex setting.
"Unitary columns" = orthonormal in the Hermitian sense.
```

**Real dimension of U(n):**
An n x n complex matrix has 2n^2 real degrees of freedom. The constraint A†A = I is equivalent
to the matrix being Hermitian positive definite with all eigenvalues 1, which imposes n^2 real
conditions. So dim_R(U(n)) = 2n^2 - n^2 = n^2.

**Special unitary SU(n):** det A = 1 removes 1 more real dimension (the U(1) factor).
dim_R(SU(n)) = n^2 - 1.

**Lie algebra:**
- u(n) = { X in M_n(C) : X + X† = 0 } = skew-Hermitian matrices
- su(n) = { X in u(n) : tr(X) = 0 }

Note: physicists write generators as Hermitian (H = iX), so [H_i, H_j] = i f_{ijk} H_k with real
structure constants. Mathematicians work with skew-Hermitian X directly.

**Critical instances:**

| Group | dim | Topology | Physics role |
|-------|-----|----------|--------------|
| U(1) | 1 | S^1 | Electromagnetism gauge group |
| SU(2) | 3 | S^3 | Weak force; double cover of SO(3) |
| SU(3) | 8 | — | Strong force (QCD); 8 gluons = 8 generators |
| SU(5) | 24 | — | Grand unification candidate |

---

## Symplectic Groups

**Definition:** Sp(2n,R) = { A in GL(2n,R) : A^T J A = J }

where J = block([[0, I_n], [-I_n, 0]]) is the standard symplectic matrix.

These preserve the symplectic form omega(x,y) = x^T J y — a non-degenerate skew-symmetric
bilinear form. Symplectic forms only exist in even dimensions (hence Sp(2n)).

```
SYMPLECTIC vs ORTHOGONAL:
  Orthogonal: A^T A = I   (preserve symmetric form sum x_i y_i)
  Symplectic: A^T J A = J  (preserve skew form sum (x_i y_{n+i} - x_{n+i} y_i))

  Orthogonal matrices: finite orbits (compact group SO(n))
  Symplectic matrices: unbounded orbits (non-compact Sp(2n,R))
```

**Lie algebra:** sp(2n,R) = { X : X^T J + J X = 0 }, dim = n(2n+1).

**Variants:**

| Group | Form preserved | Compact? | Notes |
|-------|---------------|---------|-------|
| Sp(2n,R) | Real symplectic | No | Phase space symmetry |
| Sp(2n,C) | Complex symplectic | No | Complex geometry |
| Sp(n) = USp(2n) | Hermitian + symplectic | Yes | C-series compact form |

Sp(1) iso SU(2) iso S^3 (unit quaternions).

**Physics:** Sp(2n,R) is the symmetry group of the 2n-dimensional phase space in Hamiltonian
mechanics. Linear canonical transformations (preserving Hamilton's equations) form Sp(2n,R).

---

## The Classical Groups: Summary Table

| Group | Definition | Preserved structure | dim | Compact? | Connected? |
|-------|-----------|--------------------|----|---------|-----------|
| GL(n,R) | det != 0 | nothing | n^2 | No | No (2 comp.) |
| GL(n,C) | det != 0 | nothing | 2n^2 | No | Yes |
| SL(n,R) | det = 1 | volume | n^2-1 | No | Yes (n>=2) |
| SL(n,C) | det = 1 | complex volume | 2(n^2-1) | No | Yes |
| O(n) | A^T A=I | Euclidean inner prod | n(n-1)/2 | Yes | No (2 comp.) |
| SO(n) | A^T A=I, det=1 | orientation + metric | n(n-1)/2 | Yes | Yes |
| U(n) | A†A=I | Hermitian inner prod | n^2 | Yes | Yes |
| SU(n) | A†A=I, det=1 | Hermitian + volume | n^2-1 | Yes | Yes |
| Sp(2n,R) | A^T JA=J | symplectic form | n(2n+1) | No | Yes |
| Sp(n) | compact symp | Hermitian + symp | n(2n+1) | Yes | Yes |

---

## Topology: Compact vs Non-Compact

**Compact groups** (O(n), SO(n), U(n), SU(n), Sp(n)):

```
COMPACTNESS CRITERION FOR CLOSED MATRIX SUBGROUPS:
  A closed subgroup of GL(n,R) is compact iff it is bounded.

  O(n): A^T A=I forces all entries in [-1,1].  Bounded + Closed -> Compact
  U(n): A†A=I forces all entries in unit disk.  Bounded + Closed -> Compact
  SL(n,R): no bound on entries (diagonal [[t,0],[0,1/t]] -> inf). Not compact.
```

**Why compactness matters for representations:**
- Compact groups have finite-dimensional irreducible unitary representations
- All representations are completely reducible (Weyl's theorem)
- Characters completely determine representations
- Peter-Weyl: L^2(G) decomposes as a direct sum of matrix coefficient spaces

Non-compact groups (GL, SL, Sp(R)) have unitary representations that are infinite-dimensional.
This requires functional analysis (Harish-Chandra modules, etc.) and is substantially harder.

---

## Other Important Lie Groups

**The Euclidean group SE(n):** Rigid motions of Euclidean space (rotations + translations).

```
SE(n) = SO(n) semi-direct R^n  (semidirect product)

Elements: (R, t) where R in SO(n), t in R^n
Action: x |-> Rx + t
Multiplication: (R_1,t_1).(R_2,t_2) = (R_1 R_2, R_1 t_2 + t_1)

Matrix form in homogeneous coordinates:
  [ R | t ]
  [---+---]   in GL(n+1,R)
  [ 0 | 1 ]
```

SE(3) is the configuration space of a rigid body. Relevant to robotics. See 09-APPLICATIONS.md.

**The Lorentz group O(3,1):** Preserves the Minkowski metric diag(-1,1,1,1). Non-compact.
The proper orthochronous subgroup SO^+(3,1) is the symmetry of special relativity.
Its double cover is SL(2,C) — the same covering role SU(2) plays for SO(3).

**The Heisenberg group:**
```
H = { [[1, a, c], [0, 1, b], [0, 0, 1]] : a,b,c in R }
```
Non-abelian nilpotent Lie group. Underlying algebraic structure of [x_hat, p_hat] = i hbar.

---

## Embeddings and Inclusions

```
GL(n,C) -------> GL(2n,R)      [z = a+bi |-> [[a,-b],[b,a]] block]
    |                 |
  SL(n,C)          GL(n,R)
    |                 |
  SU(n)  -------> SO(2n)
    |
  U(n)   -------> O(2n)

Compact chain:
  SU(n) subset U(n) subset O(2n)
  Sp(n) subset U(2n) subset O(4n)
```

---

## Decision Cheat Sheet

| You need... | Use this group |
|------------|----------------|
| All invertible linear transformations on R^n | GL(n,R) |
| Volume-preserving linear maps | SL(n,R) |
| Rotations in R^n | SO(n) |
| Rotations + reflections | O(n) |
| Unitary transformations on C^n | U(n) |
| Unitary + det=1 | SU(n) |
| Gauge group of electromagnetism | U(1) |
| Gauge group of weak force | SU(2) |
| Gauge group of strong force (QCD) | SU(3) |
| Rigid body motion in 3D | SE(3) = SO(3) semi-direct R^3 |
| Hamiltonian mechanics linear symmetry | Sp(2n,R) |
| Spacetime symmetry (special relativity) | SO(3,1) or its cover SL(2,C) |

---

## Common Confusion Points

**O(n) vs SO(n):** O(n) includes reflections (det = -1). SO(n) is the connected component of the
identity — pure rotations. In physics you almost always want SO(n). "O" = Orthogonal, "S" = Special.

**U(n) vs SU(n):** U(n) = U(1) x SU(n) locally but not globally. SU(n) has center Z_n (diagonal
matrices e^{2pi i k/n} I for k=0,...,n-1). In physics, SU(2) and SU(3) appear because we quotient
out the overall U(1) phase freedom.

**"Real dimension" of complex groups:** U(n) is a real Lie group of real dimension n^2. When you
say SU(3) has 8 generators, that is 8 real dimensions (the Gell-Mann matrices).

**Sp(2n) notation ambiguity:** Some authors write Sp(n) for the group acting on R^{2n}; others
write Sp(2n) for the same group. The compact symplectic group Sp(n) has dimension n(2n+1). Always
verify the convention in any given source.

**"Matrix Lie group" vs "Lie group":** By Ado's theorem, every finite-dimensional Lie algebra
embeds in gl(n,R) for some n. But not every Lie group is a matrix group — the universal cover of
SL(2,R) has no faithful finite-dimensional representation. In practice, all classically relevant
groups are matrix groups.
