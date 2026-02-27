# [82] --- Lead

**J&#9829; The Formalist** &middot; Math & Physics &middot; &#9733; T1

---

> The Formalist cares about what survives transformation. Rotate it, reflect it, translate it -- if the truth still holds, it was always true. One proof in this section is incomplete. Eight steps are missing. Finish it.

---

## The Puzzle

**Type:** Proof Completion -- fill missing steps in a mathematical derivation
**References:** mathematics/, abstract-algebra/

Below is a derivation titled *From Structure to Conservation*. Eight linked propositions trace a path from algebraic axioms to physical law. Each proposition contains exactly one blank, marked `________`. Each blank is a single specific mathematical term or named result that appears in the encyclopedia.

Fill every blank. Read the first letter of each answer, top to bottom.

The propositions are not independent. Some blanks constrain others. What you write in Step VI only makes sense if Step V is correct. What Step III names determines what Step VII must be. If your eight letters do not form a word, at least one blank is wrong.

---

### I.

Consider a physical system whose configuration evolves along a path q(t). The action functional is S[q] = integral from t_1 to t_2 of L(q, dq/dt, t) dt, where L is the Lagrangian. Hamilton's principle asserts that among all paths connecting two fixed endpoints, the physical trajectory is the one for which the action is `________` -- meaning its first variation vanishes: delta S = 0. This does not require S to be a minimum; saddle points of the action are equally valid.

The variational condition delta S = 0 yields the Euler-Lagrange equations:

```
d/dt (dL/dq_i-dot) - dL/dq_i = 0
```

*The missing word is the precise variational-calculus term for "first variation vanishes." The encyclopedia discusses this condition in the context of Hamilton's principle and the Euler-Lagrange derivation. It is not "minimal" and not "extremal."*

---

### II.

The structure of the solutions to the Euler-Lagrange equations is governed by the symmetry group of the Lagrangian. To study representations of the symmetric group S_n (the group of all permutations of n objects), one needs a combinatorial tool: `________` tableaux. These are arrays of integers 1 through n placed into the cells of a partition diagram (a left-justified arrangement of boxes with row lengths lambda_1 >= lambda_2 >= ...), subject to the rule that entries strictly increase along each row and strictly increase down each column. Each standard tableau of shape lambda indexes a basis vector of the Specht module S^lambda, and the distinct partitions of n enumerate all inequivalent irreducible representations of S_n over the complex numbers.

*The missing word is a proper name. The encyclopedia's treatment of representation theory describes these combinatorial objects in the section on S_n representations. The same file connects them to equivariant neural networks.*

---

### III.

Why does every complex representation of a finite group decompose into irreducible pieces? The answer is `________`'s theorem: if G is a finite group and V is a finite-dimensional representation of G over a field whose characteristic does not divide |G|, then V is completely reducible. The proof constructs a G-invariant complement to any G-invariant subspace W <= V by averaging an arbitrary projection pi over the group:

```
pi-bar = (1/|G|) sum_{g in G} rho(g) . pi . rho(g)^{-1}
```

The averaged map pi-bar is idempotent, G-equivariant, and its kernel is a G-invariant complement to W. The theorem fails in characteristic p dividing |G|, which is why modular representation theory requires entirely different tools (Brauer characters, decomposition matrices, defect groups).

*The missing word is a mathematician's surname. It appears in abstract-algebra/ in the discussion of complete reducibility, immediately before Schur's lemma.*

---

### IV.

The map rho in Step III -- from the group G to the invertible linear maps GL(V) -- is a specific instance of a `________`: a structure-preserving map between algebraic objects. For groups, the defining property is rho(gh) = rho(g) rho(h). The kernel of any such map is a normal subgroup of the domain, and the first isomorphism theorem states that G / ker(rho) is isomorphic to im(rho). In the language of category theory, every algebraic category (groups, rings, modules, topological spaces) is defined by its objects and its collection of these structure-preserving maps, and the entire subject of abstract algebra can be reorganized as the study of categories and the maps between them.

*The missing word is the general name for the arrows in a category. In group theory it appears with the prefix "homo-"; in category theory it stands alone as the fundamental concept. The abstract-algebra overview names it as the central object of categorical reasoning.*

---

### V.

Finite groups capture discrete symmetry (reflections, permutations). Physical symmetries -- rotations, translations, phase shifts -- are continuous, and their groups are Lie groups: groups that are simultaneously smooth manifolds. The bridge between a Lie group G and its linearization is the `________` map, defined by the power series

```
exp(X) = I + X + X^2/2! + X^3/3! + ...
```

where X is an element of the Lie algebra g. For the rotation group SO(3), exponentiating a skew-symmetric matrix theta * K (where K encodes the rotation axis) produces the rotation matrix. For SU(2), exponentiating i*theta*sigma/2 (with sigma a Pauli matrix) produces the unitary transformation. This map is a local diffeomorphism near the origin of g -- every group element sufficiently close to the identity is in its image.

*The missing word names this specific map. The encyclopedia defines it in the Lie groups section of mathematics/ and uses it repeatedly when moving between Lie algebras and Lie groups.*

---

### VI.

The Lie algebra g -- the domain of the map in Step V -- is defined as the `________` space to the Lie group G at the identity element e. For a matrix Lie group, this is the set {X : exp(tX) in G for all t in R}. It is a vector space equipped with a bilinear bracket [X, Y] = XY - YX satisfying:

```
Antisymmetry:    [X, Y] = -[Y, X]
Jacobi identity: [X, [Y, Z]] + [Y, [Z, X]] + [Z, [X, Y]] = 0
```

The dimension of this space equals the number of independent continuous symmetries of G. For SO(3): dim = 3 (three rotation axes). For SU(2): dim = 3 (three Pauli generators). For SU(3): dim = 8 (the eight Gell-Mann matrices, hence eight gluons).

*The missing word is a geometric term from differential geometry. It describes the best linear approximation to a curved space at a point. The encyclopedia uses this exact phrase -- "the [blank] space at the identity" -- when defining the Lie algebra.*

---

### VII.

Assembling the machinery: a `________` of a group G on a vector space V is a homomorphism rho: G -> GL(V). For finite groups, Step III's theorem guarantees that rho decomposes as a direct sum of irreducible components. For compact Lie groups, the Peter-Weyl theorem provides the analogous guarantee. The irreducible components of SU(2) are indexed by a half-integer s = 0, 1/2, 1, 3/2, ..., with dimension 2s + 1. In quantum mechanics, these are the spin-s particles: scalars (s=0), spinors (s=1/2), vectors (s=1). The character chi_rho(g) = tr(rho(g)) -- the trace of the matrix assigned to each group element -- uniquely identifies each irreducible component, by Schur's orthogonality relations.

*The missing word names the central object that all of Steps II--VI have been constructing: the concept of a group acting on a vector space through invertible linear maps. It appears throughout mathematics/ and abstract-algebra/ and is the title of a dedicated file in each.*

---

### VIII.

The final link. Noether's theorem states that every continuous one-parameter symmetry of the Lagrangian produces a conserved quantity. The proof uses Steps I and VII together: if the Lagrangian L is invariant under an infinitesimal transformation generated by a one-parameter subgroup of G (acting on q via the object named in Step VII), then the Euler-Lagrange equations from Step I imply that the quantity (dL/dq_i-dot) * delta_q_i is constant along physical trajectories.

But the deepest unification lies in category theory. The `________` lemma states that for any object A in a category C, the functor Hom(-, A) completely determines A up to isomorphism. In the category of groups, this means a group is fully characterized by the totality of homomorphisms into it. In the category of representations from Step VII, this means a representation is determined by all intertwiners from every other representation. The claim is structural: what an object IS equals how it relates to everything else. The concept you have been spelling -- the concept this entire derivation concerns -- is precisely that principle.

*The missing word is a proper name. The lemma appears in abstract-algebra/ in the category theory file, and the encyclopedia calls it "the mathematical foundation of programming to interfaces." It is the formal reason that the morphisms of Step IV carry all the information.*

---

## Worksheet

| Step | The blank describes... | Your answer | First letter |
|------|----------------------|-------------|:------------:|
| I    | Variational condition on the action | _________________ | [___] |
| II   | Proper name: tableaux classifying S_n irreps | _________________ | [___] |
| III  | Proper name: complete reducibility theorem | _________________ | [___] |
| IV   | Categorical name: structure-preserving map | _________________ | [___] |
| V    | Named map: Lie algebra to Lie group | _________________ | [___] |
| VI   | Geometric term: the space that IS the Lie algebra | _________________ | [___] |
| VII  | Central concept: group acting on vector space | _________________ | [___] |
| VIII | Proper name: "objects = their morphisms" lemma | _________________ | [___] |

---

### Interlock Check

Before reading off your answer, verify these constraints hold:

- **V constrains VI.** Step V names a map. Step VI names its domain. The map in V sends elements of the space in VI to elements of the group. If your V is the name of a map and your VI is not the geometric name for that map's domain, one is wrong.
- **III constrains VII.** Step III names a theorem guaranteeing that a certain algebraic object decomposes into irreducible pieces. Step VII names that algebraic object. If the theorem in III is about complete reducibility of something, then VII must name that something.
- **IV constrains VIII.** Step IV names the general concept of a structure-preserving map (the arrows in a category). Step VIII names a lemma asserting that all information about an object is encoded in those arrows. These two terms must be consistent: VIII's lemma is a statement about the maps named in IV.
- **Letter check.** If your eight first letters do not form a recognizable English word that describes what a group encodes, what a Lie algebra linearizes, and what Noether's theorem converts into conservation laws -- recheck your blanks.

---

**Your answer** (8 letters): _ _ _ _ _ _ _ _

*You may find the Mathematics and Abstract Algebra sections helpful.*
