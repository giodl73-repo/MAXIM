# Representation Theory of Lie Groups

## The Big Picture

A representation is a way of realizing an abstract group as linear transformations on a vector
space. Representation theory asks: what are all the ways a group G can act linearly? The answer
for compact groups is completely understood and beautiful. For non-compact groups it is harder.

```
+----------------------------------------------------------------------+
|              REPRESENTATION THEORY: THE FULL PICTURE                 |
+----------------------------------------------------------------------+
|                                                                      |
|  GROUP G (abstract)  ----rho---->  GL(V) (concrete linear maps)     |
|                                                                      |
|  QUESTION: Classify all representations rho: G -> GL(V)             |
|                                                                      |
|  STEP 1: Reduce to irreducibles                                      |
|  V = V_1 + V_2 + ... + V_k  (direct sum of irreps)                  |
|  (Weyl's theorem for compact groups)                                  |
|                                                                      |
|  STEP 2: Classify irreducibles                                       |
|  For compact G: irreps <--> dominant integral weights lambda         |
|  Labeled by highest weight. Character formula gives dimensions.      |
|                                                                      |
|  STEP 3: Decompose products                                          |
|  V_lambda tensor V_mu = sum_nu c^nu_{lambda mu} V_nu                |
|  Clebsch-Gordan (for SU(2)); Littlewood-Richardson (for GL)          |
|                                                                      |
|  KEY TOOLS:                                                          |
|  - Schur's lemma: Hom_G(V,W) for irreps                             |
|  - Characters: chi_V(g) = tr(rho(g))                                |
|  - Peter-Weyl: L^2(G) = hat-sum_pi V_pi tensor V_pi*                |
|                                                                      |
+----------------------------------------------------------------------+
```

---

## Basic Definitions

**Representation:** A Lie group representation is a Lie group homomorphism:
```
rho: G -> GL(V)
```
where V is a finite-dimensional (or infinite-dimensional) vector space over R or C.

At the Lie algebra level, differentiating at the identity gives a Lie algebra representation:
```
d_rho: g -> gl(V) = End(V)
```
satisfying d_rho([X,Y]) = d_rho(X)d_rho(Y) - d_rho(Y)d_rho(X).

**Subrepresentation (invariant subspace):** A subspace W subset V is invariant (G-invariant) if
rho(g)W subset W for all g in G. Then the restriction rho|_W is a subrepresentation.

**Irreducible representation (irrep):** A nonzero representation (V, rho) with no proper nonzero
G-invariant subspaces. "Atomic" — cannot be decomposed further.

**Completely reducible (semisimple):** Every subrepresentation has a complementary invariant
subspace. Equivalently, V = direct sum of irreducibles.

---

## Schur's Lemma

The foundational structural result:

**Schur's Lemma:** Let (V, rho) and (W, sigma) be irreducible representations of G. Let
phi: V -> W be a G-equivariant linear map (phi . rho(g) = sigma(g) . phi for all g).

1. Either phi = 0 or phi is an isomorphism.
2. If V = W (same irrep), then phi = lambda * I for some scalar lambda in C.

**Proof of 1:** ker(phi) is a G-invariant subspace of V. By irreducibility, ker(phi) = 0 or V.
  If ker = 0, phi is injective; image of phi is G-invariant subspace of W, so image = W. Done.

**Proof of 2:** phi has an eigenvalue lambda (since C is algebraically closed). Then phi - lambda*I
  is also G-equivariant and has nontrivial kernel, so phi - lambda*I = 0 by part 1.

**Consequences:**
```
Hom_G(V, W) = { 0             if V, W are non-isomorphic irreps
              { C * id_V       if V = W (over C)

As a matrix: if G acts on C^n via rho, matrices commuting with all rho(g) are scalar multiples of I.
This is the mathematical content of "observables commute with symmetry."
```

---

## Complete Reducibility (Weyl's Theorem)

**Theorem (Weyl):** Every finite-dimensional representation of a compact Lie group is completely
reducible (semisimple).

**Proof sketch:** Use the invariant inner product. For compact G, define:
```
<u, v>_G = integral_G <rho(g)u, rho(g)v> dg
```
where dg is Haar measure (the unique G-invariant measure on G). This average of a Hermitian inner
product is G-invariant. For any invariant subspace W, its orthogonal complement W^perp under
this invariant inner product is also invariant. So W has an invariant complement.

**Haar measure existence:** Every compact Lie group (indeed any locally compact group) has a
unique (up to scaling) left-invariant measure, the Haar measure. This is what makes compact
groups tractable.

**Contrast with non-compact:** The left regular representation of SL(2,R) on L^2(SL(2,R)) has
invariant subspaces without invariant complements — complete reducibility fails.

---

## Characters

The character of a representation (V, rho) is the function:
```
chi_V: G -> C
chi_V(g) = tr(rho(g))
```

**Properties:**

| Property | Formula | Note |
|----------|---------|------|
| Class function | chi_V(hgh^{-1}) = chi_V(g) | Character depends only on conjugacy class |
| Direct sum | chi_{V+W}(g) = chi_V(g) + chi_W(g) | Additive |
| Tensor product | chi_{V tensor W}(g) = chi_V(g) * chi_W(g) | Multiplicative |
| Dual | chi_{V*}(g) = conj(chi_V(g)) | Complex conjugate |
| Dimension | chi_V(e) = dim(V) | Value at identity = dimension |

**Character orthogonality (for compact G):**
```
<chi_V, chi_W>_G = integral_G chi_V(g) conj(chi_W(g)) dg = delta_{V,W}
```
where the integral uses normalized Haar measure (vol(G) = 1) and V, W are irreducible.

This is the analogue of Fourier series orthogonality: {chi_pi} form an orthonormal basis for
the space of class functions on G (square-integrable with respect to Haar measure).

**Decomposition formula:** For any representation V:
```
V = direct_sum_pi V_pi^{m_pi}  where m_pi = <chi_V, chi_{pi}>_G
```
The multiplicity of irrep pi in V is the inner product of their characters.

---

## The Peter-Weyl Theorem

The central theorem of harmonic analysis on compact Lie groups. It generalizes Fourier series to
non-abelian groups.

**Theorem (Peter-Weyl, 1927):** Let G be a compact Lie group. Then:

1. The matrix coefficient functions {rho^pi_{ij}(g)} form a dense subset of L^2(G).

2. As a unitary G x G representation (left and right translation):
```
L^2(G) iso hat-sum_{pi irr} V_pi tensor V_pi*

where the hat-sum is a Hilbert space direct sum
and pi ranges over all equivalence classes of irreducible unitary reps.
```

3. The functions {sqrt(dim V_pi) * rho^pi_{ij}} form an orthonormal basis for L^2(G).

**For G = S^1 = U(1):** Irreps are e^{int}: z -> z^n for n in Z. Matrix coefficients are e^{ino}.
Peter-Weyl becomes: {e^{ino}/sqrt(2pi)} is an orthonormal basis for L^2(S^1). This is Fourier series.

**For G = SU(2):** Irreps are V_j for j = 0, 1/2, 1, 3/2, ... (spin-j representations) with
dim V_j = 2j+1. The Peter-Weyl decomposition of L^2(SU(2)) is:
```
L^2(SU(2)) iso direct_sum_{j=0,1/2,1,...} C^{2j+1} tensor C^{2j+1}
```
The (2j+1)^2-dimensional piece corresponds to the spin-j representation appearing with multiplicity 2j+1.

**Fourier on Groups analogy:**
```
Abelian case (S^1):           Non-abelian case (G compact):
  f = sum_n f_hat(n) e^{ino}    f = sum_pi (dim pi) tr(rho_pi(g) * f_hat(pi))
  f_hat(n) = integral f e^{-ino}  f_hat(pi) = integral f(g) rho_pi(g^{-1}) dg
  Parseval: ||f||^2 = sum|f_hat|^2  ||f||^2 = sum_pi (dim pi) tr(f_hat(pi)† f_hat(pi))
```
See 09-APPLICATIONS.md for how this is used in equivariant networks.

---

## Representations of SU(2) and so(3) in Detail

SU(2) is the cleanest example to work through completely.

**Lie algebra su(2):** Spanned by {iH, E, F} (or equivalently {L_x, L_y, L_z} via so(3) iso):
```
H = [[1,0],[0,-1]],  E = [[0,1],[0,0]],  F = [[0,0],[1,0]]

[H,E] = 2E,   [H,F] = -2F,   [E,F] = H

(This is the sl(2) triple — the prototypical semisimple Lie algebra computation)
```

**Irreducible representations V_j (j = 0, 1/2, 1, 3/2, ...):**

V_j is (2j+1)-dimensional with basis |j,m> for m = -j, -j+1, ..., j-1, j, and action:
```
H|j,m> = 2m|j,m>           (H is diagonal: eigenvalues 2m)
E|j,m> = sqrt((j-m)(j+m+1)) |j,m+1>   (raising operator)
F|j,m> = sqrt((j+m)(j-m+1)) |j,m-1>   (lowering operator)
```

The highest weight vector |j,j> satisfies E|j,j> = 0 (cannot raise further). Starting from
the highest weight and applying F repeatedly generates the entire irrep.

**Physical interpretation:**
- j is the spin quantum number
- m is the magnetic quantum number (z-component of angular momentum)
- E, F are raising/lowering operators J_+, J_-
- The (2j+1)-dimensional representation corresponds to spin-j particle
- Electrons: j=1/2 (2 states: spin up, spin down)
- Photons: j=1 (3 polarization states)
- Gravitons: j=2 (5 states)
- Scalar Higgs: j=0 (1 state)

---

## The Highest Weight Classification (General)

For any compact semisimple Lie group G (see 05-ROOT-SYSTEMS.md and 06-SEMISIMPLE.md for the
general setup), the irreducible representations are classified by dominant integral weights.

**Setup:** Choose a maximal abelian subalgebra h subset g (Cartan subalgebra). For SU(n) this
is the diagonal matrices. The roots alpha are the non-zero weights of the adjoint representation.

**Dominant integral weight:** An element lambda in h* satisfying:
1. <lambda, alpha_check> in Z for all roots alpha (integrality)
2. <lambda, alpha_check> >= 0 for all simple roots alpha (dominance)

where alpha_check = 2*alpha/|alpha|^2 is the coroot.

**Theorem (highest weight):** The map lambda |--> V_lambda (irrep with highest weight lambda) is
a bijection from dominant integral weights to irreducible representations of G.

**Weyl dimension formula:** dim V_lambda = prod_{alpha>0} <lambda + rho, alpha_check> / <rho, alpha_check>

where rho = (1/2) * sum_{alpha>0} alpha is the Weyl vector (half-sum of positive roots).

For SU(2): single simple root alpha = 1, dominant weights are lambda = j >= 0, rho = 1/2.
dim V_j = (j + 1/2) / (1/2) = 2j+1. Matches the formula above.

---

## Tensor Products and Clebsch-Gordan

**Tensor product of representations:** If (V, rho) and (W, sigma) are G-representations,
(V tensor W, rho tensor sigma) is defined by (rho tensor sigma)(g) = rho(g) tensor sigma(g).

By complete reducibility, V tensor W decomposes into irreps. The multiplicities are given by
Clebsch-Gordan coefficients.

**For SU(2):** The Clebsch-Gordan rule:
```
V_j1 tensor V_j2 = direct_sum_{j=|j1-j2|}^{j1+j2} V_j
```
Each j appears with multiplicity 1, and |j1-j2| <= j <= j1+j2. This is the triangle rule from
quantum mechanics for combining angular momenta.

**For SU(3):** The product rule is more complex (two quantum numbers) and given by the
Littlewood-Richardson rule via Young tableaux. The famous quark model: quarks are the 3-dim
fundamental rep V_{(1,0)} of SU(3)_flavor; baryons = 3 tensor 3 tensor 3 contains a singlet.

---

## Induced and Restricted Representations

**Restriction:** If H subset G is a subgroup and (V, rho) is a G-rep, restricting to H gives
Res^G_H(V). The branching problem asks how irreps decompose under restriction.

**Induction:** Given an H-rep (W, sigma), the induced G-rep Ind^G_H(W) = C^inf(G) tensor_{C^inf(H)} W
(sections of an associated bundle). For finite groups this is exact Frobenius reciprocity.

**Frobenius reciprocity:**
```
Hom_G(Ind^G_H W, V) iso Hom_H(W, Res^G_H V)
```
The physics application: the spectrum of a particle in a field with symmetry group H inside
a theory with symmetry G is computed by induced representations.

---

## Decision Cheat Sheet

| Task | Tool |
|------|------|
| Show a rep is irreducible | Show it has no proper invariant subspaces |
| Decompose a rep into irreps | Compute <chi_V, chi_pi> for each irrep pi |
| Find all irreps of SU(2) | V_j for j = 0, 1/2, 1, ...; dim = 2j+1 |
| Find all irreps of compact G | Dominant integral weights in h* |
| Check if two irreps are isomorphic | Compare characters (they determine the rep) |
| Decompose V tensor W for SU(2) | Triangle rule: sum_{j=|j1-j2|}^{j1+j2} V_j |
| Harmonic analysis on G | Peter-Weyl: L^2(G) = hat-sum_pi V_pi tensor V_pi* |

---

## Common Confusion Points

**"Characters determine representations":** True for compact groups. The character chi_V (as a
class function) determines V up to isomorphism. Two representations are isomorphic iff they have
the same character. This fails for non-compact groups.

**"Irreducible over R vs over C":** Over R, a representation irreducible over C may decompose.
Example: the 2-dim rep of SO(2) is irreducible over R (rotations have no real eigenvectors for
general angles) but over C it decomposes into e^{i theta} and e^{-i theta}. When physicists say
"representations," they almost always mean over C.

**"Highest weight vector is unique":** Up to scaling. In V_j, the vector |j,j> is the unique
(up to scale) vector killed by the raising operator E. Its weight (eigenvalue of H) is 2j, which
is the highest weight.

**"Peter-Weyl is just Fourier series":** Peter-Weyl strictly generalizes Fourier series to
non-abelian compact groups. For abelian G, all irreps are 1-dimensional (characters), and
Peter-Weyl reduces to the Pontryagin duality / Fourier series. For non-abelian G, irreps are
higher-dimensional and the "Fourier transform" takes values in matrices (the operators f_hat(pi)).

**"Complete reducibility holds for all groups":** No. Weyl's theorem applies to compact groups
(or semisimple Lie algebras over C). For solvable Lie algebras, representations need not be
semisimple — this is why the unipotent radical of a Borel subgroup matters in algebraic geometry.
