# Lie Algebras and the Exponential Map

## The Big Picture

The Lie algebra is the linearization of the Lie group at the identity. It captures the group's
infinitesimal structure: to first order, the group looks like a vector space with a bilinear
operation (the bracket) encoding how the group is non-commutative. The exponential map connects
the two levels.

```
+----------------------------------------------------------------------+
|               THE LIE ALGEBRA–LIE GROUP CORRESPONDENCE              |
+----------------------------------------------------------------------+
|                                                                      |
|  LIE ALGEBRA g = T_e G                 LIE GROUP G                  |
|  (tangent space at identity)           (the smooth manifold)         |
|                                                                      |
|  - Vector space                        - Smooth manifold             |
|  - Bracket [X,Y]: g x g -> g          - Multiplication G x G -> G   |
|  - Skew-symmetric: [X,Y]=-[Y,X]       - Smooth, associative         |
|  - Jacobi identity                     - Identity element e          |
|                                                                      |
|         exp: g  ---------------------> G                            |
|                X |-------------------> e^X                          |
|                                                                      |
|         log: G  ---------------------> g  (local, near e)           |
|                                                                      |
|  LINEAR, FLAT, EASY                    CURVED, NONLINEAR, GLOBAL     |
|  Can add: X + Y in g                  Multiplication: g.h in G       |
|  Can differentiate                    May not commute                |
|                                                                      |
+----------------------------------------------------------------------+
```

---

## Definition: Lie Algebra

A **Lie algebra** over a field k is a k-vector space g equipped with a bilinear operation
[.,.]: g x g -> g (the Lie bracket) satisfying:

1. **Skew-symmetry:** [X,Y] = -[Y,X] for all X,Y in g

2. **Jacobi identity:** [X,[Y,Z]] + [Y,[Z,X]] + [Z,[X,Y]] = 0 for all X,Y,Z in g

Note: [X,X] = 0 follows from skew-symmetry (put Y=X).

The Jacobi identity is not obvious — it says the bracket satisfies a derivative-like rule:
[X,-] acts as a derivation on g. Writing ad_X(Y) = [X,Y], the Jacobi identity becomes
ad_X([Y,Z]) = [ad_X(Y), Z] + [Y, ad_X(Z)], exactly the Leibniz rule for ad_X.

**For matrix Lie groups:** g = T_e G, the bracket is the commutator [X,Y] = XY - YX of matrices.

---

## Lie Algebras of the Classical Groups

Derivation pattern: if G = {A : F(A) = 0} for some constraint F, then g consists of vectors X
such that dF_I(X) = 0 (first-order perturbation preserves the constraint).

```
GROUP G        CONSTRAINT          LIE ALGEBRA g           BASIS EXAMPLE
GL(n,R)        det != 0            gl(n,R) = M_n(R)         E_ij (matrix units)
SL(n,R)        det = 1             sl(n,R) = {tr=0}          E_ij - delta_{ij}/n * I
O(n)           A^T A = I           so(n) = {X + X^T = 0}    E_ij - E_ji
U(n)           A†A = I            u(n) = {X + X† = 0}       i*H_ij (skew-Herm)
SU(n)          A†A=I, det=1       su(n) = {skew-Herm, tr=0} Pauli matrices (n=2)
Sp(2n,R)       A^T J A = J        sp(2n,R) = {X^T J+JX=0}  ...
```

**Derivation of so(n):** Let A(t) = I + tX + O(t^2) be a curve in O(n) with A(0)=I.
  A(t)^T A(t) = I  =>  (I + tX^T)(I + tX) = I  =>  X^T + X = O(t)  =>  X + X^T = 0.

**Derivation of su(n):** Skew-Hermitian (from U(n) condition) plus trace-zero (from det=1).

---

## The Exponential Map

**For matrix groups:** The matrix exponential is:

```
exp: g -------> G
     X |------> e^X = I + X + X^2/2! + X^3/3! + ... = sum_{n=0}^{inf} X^n / n!
```

This series converges for all X in M_n(R) or M_n(C). Key properties:

| Property | Formula | Notes |
|----------|---------|-------|
| exp(0) = I | | Base point is identity |
| exp(X)^{-1} = exp(-X) | | Inverse |
| det(exp(X)) = exp(tr(X)) | | Crucial for SL and SU |
| exp(A X A^{-1}) = A exp(X) A^{-1} | | Equivariance |
| exp((s+t)X) = exp(sX)exp(tX) | | One-parameter subgroup |
| exp(X+Y) = exp(X)exp(Y) IF [X,Y]=0 | | Commuting case only |

**Local diffeomorphism:** exp is a local diffeomorphism near 0 in g: there exist neighborhoods
U of 0 in g and V of e in G such that exp: U -> V is a diffeomorphism. This is the content of
the inverse function theorem applied to d(exp)_0 = I (the identity map on T_0 g = g).

**Not surjective in general:** exp(g) need not cover all of G. For compact connected G, it does
(by a Riemannian geometry argument). For SL(2,R), the matrix [[-1,-1],[0,-1]] is not in exp(sl(2,R)).

---

## One-Parameter Subgroups

For each X in g, the map phi_X: R -> G defined by phi_X(t) = exp(tX) is a Lie group homomorphism.

```
phi_X(0) = I  (identity)
phi_X(s+t) = phi_X(s) phi_X(t)  (homomorphism)
phi_X'(0) = X  (tangent vector at identity)
```

Conversely, every smooth homomorphism R -> G has this form. So the Lie algebra elements are in
bijection with one-parameter subgroups of G.

**Example in SO(3):** The matrix X = [[0,-1,0],[1,0,0],[0,0,0]] generates rotation about the z-axis:
```
exp(tX) = [[cos t, -sin t, 0],
           [sin t,  cos t, 0],
           [0,      0,     1]]
```
This is the rotation matrix R_z(t). The three generators of so(3) generate the three basic rotations.

---

## The Baker-Campbell-Hausdorff Formula

When X and Y do not commute, exp(X)exp(Y) != exp(X+Y). The BCH formula expresses
log(exp(X)exp(Y)) as a series in X, Y, and their iterated brackets:

```
log(exp(X)exp(Y)) = X + Y
                  + (1/2)[X,Y]
                  + (1/12)([X,[X,Y]] + [Y,[Y,X]])
                  - (1/24)[Y,[X,[X,Y]]]
                  + ...
```

The remarkable fact: this series involves *only brackets* — no bare X^2 terms. This means the
entire expression lies in the Lie algebra g, not just in the associative algebra of matrices.

**Dynkin's explicit formula:**
```
log(exp(X)exp(Y)) = sum_{n=1}^{inf} (-1)^{n-1}/n * sum_{p+q=n, p_i+q_i>=1}
  [X^{p_1} Y^{q_1} X^{p_2} Y^{q_2} ... X^{p_n} Y^{q_n}] / (p_1! q_1! ... p_n! q_n!)
```
where [X^p Y^q] means [X,...[X,[Y,...[Y,...]...]]] (nested brackets).

**BCH convergence:** The series converges when ||X|| + ||Y|| is sufficiently small. Near the
identity, the group multiplication is encoded entirely by the Lie bracket.

**Why BCH matters:** It shows that the Lie algebra completely determines the local group structure.
This is the content of Lie's third theorem: every finite-dimensional Lie algebra is the Lie algebra
of a simply-connected Lie group, and that group is unique up to isomorphism.

---

## The Adjoint Representation

Every Lie group acts on its own Lie algebra by conjugation:

```
Ad: G -------> GL(g)    (the adjoint representation)
    g |------> Ad_g where Ad_g(X) = g X g^{-1}

ad: g -------> gl(g) = End(g)    (the adjoint at algebra level)
    X |------> ad_X where ad_X(Y) = [X,Y]
```

These are related by: exp(ad_X) = Ad_{exp(X)}.

**The Killing form** is defined using ad:
```
B(X,Y) = tr(ad_X . ad_Y)
```
It is a symmetric bilinear form on g, invariant under the adjoint action.
- B non-degenerate iff g is semisimple (Cartan's criterion)
- B negative definite iff g is compact semisimple
See 06-SEMISIMPLE.md for how this is used in classification.

---

## Lie's Three Theorems

Lie's three foundational theorems (proved by Lie ~1880, rigorized by Cartan and others):

```
THEOREM 1: Every Lie group G determines a Lie algebra g = T_e G.
           Lie group homomorphism phi: G -> H differentiates to
           Lie algebra homomorphism dphi: g -> h.

THEOREM 2: Every Lie algebra homomorphism f: g -> h integrates
           (uniquely) to a Lie group homomorphism F: G_tilde -> H
           where G_tilde is the simply-connected cover of G.

THEOREM 3 (Lie-Cartan): Every finite-dimensional Lie algebra g
           over R or C is the Lie algebra of a unique simply-connected
           Lie group G_tilde.
```

The correspondence:

```
{simply-connected Lie groups} <--1-to-1--> {finite-dim Lie algebras}
{Lie groups with Lie algebra g}  <-------> {discrete subgroups of Z(G_tilde)}
```

Groups with the same Lie algebra form a family parameterized by subgroups of the center of the
simply-connected cover. Example: SU(2) and SO(3) share Lie algebra su(2) iso so(3), and
SO(3) = SU(2)/Z_2 where Z_2 is the center of SU(2).

---

## Structure Theory: Ideals and Derived Series

**Ideal:** A subspace h subset g is an ideal if [g,h] subset h. This is the Lie algebra analog
of a normal subgroup.

**Simple Lie algebra:** No ideals except 0 and g. (Excludes the 1-dim abelian case by convention.)

**Semisimple Lie algebra:** Direct sum of simple Lie algebras. Equivalently: no abelian ideals.

**Solvable Lie algebra:** The derived series g^(0) = g, g^(k+1) = [g^(k), g^(k)] reaches 0.

**Levi decomposition:** Every Lie algebra g decomposes as:
```
g = r semi-direct s
```
where r = rad(g) is the solvable radical (largest solvable ideal) and s is a semisimple subalgebra
(Levi factor). The semisimple part is classified by root systems. The solvable part is classified
by... solvable Lie algebras, which are much harder.

---

## Structural Properties of so(3) in Detail

so(3) is the prototypical example to keep in mind:

```
BASIS: L_x = [[0,0,0],[0,0,-1],[0,1,0]]
       L_y = [[0,0,1],[0,0,0],[-1,0,0]]
       L_z = [[0,-1,0],[1,0,0],[0,0,0]]

BRACKET: [L_x, L_y] = L_z
         [L_y, L_z] = L_x
         [L_z, L_x] = L_y

This is the same as the cross product! so(3) iso (R^3, x)
(where x denotes cross product)

CASIMIR: L^2 = L_x^2 + L_y^2 + L_z^2 commutes with all L_i
         (up to sign: C_2 = -(L_x^2 + L_y^2 + L_z^2) is positive)

EXPONENTIATION:
  exp(theta * n_hat . L) = I + sin(theta) (n_hat . L) + (1-cos theta)(n_hat . L)^2
  This is Rodrigues' rotation formula.
```

---

## Decision Cheat Sheet

| Concept | What it is | Key formula |
|---------|-----------|-------------|
| Lie algebra g | Tangent space T_e G | g = {X : exp(tX) in G for all t} |
| Bracket [X,Y] | Commutator XY-YX for matrix groups | Measures non-commutativity |
| exp map | g -> G | exp(X) = sum X^n/n! |
| One-parameter subgroup | phi_X(t) = exp(tX) | phi_X: R -> G homomorphism |
| BCH formula | log(exp(X)exp(Y)) | X+Y+(1/2)[X,Y]+... |
| Adjoint rep Ad | G acts on g by conjugation | Ad_g(X) = gXg^{-1} |
| Killing form | B(X,Y) = tr(ad_X ad_Y) | Non-deg iff semisimple |

---

## Common Confusion Points

**"exp is not surjective":** For compact connected groups, exp: g -> G is surjective (every
element is a rotation, which can be written as e^X for skew-symmetric X). For non-compact groups,
this fails. SL(2,R) has elements not in the image of exp.

**"BCH converges everywhere":** BCH only converges in a neighborhood of 0. For global group
multiplication, you cannot use BCH — you need the actual manifold structure of G.

**"The bracket is the commutator":** For matrix groups, [X,Y] = XY - YX. For abstract Lie
algebras arising from, say, vector fields, the bracket is the Lie bracket of vector fields. They
are the same thing when you realize the abstract group as a matrix group (which is always possible
by Ado's theorem for finite-dimensional Lie algebras).

**"g determines G uniquely":** Only the simply-connected cover is unique. Multiple groups can have
the same Lie algebra (they differ by quotients by discrete central subgroups). To get G from g,
you need to specify the global topology — how many-sheeted the cover you want.

**"Semisimple means simple":** No. Simple = irreducible (no ideals). Semisimple = direct sum of
simples. A semisimple Lie algebra may have multiple simple summands. The Killing form is
non-degenerate for semisimple; it's non-degenerate and negative-definite for compact semisimple.
