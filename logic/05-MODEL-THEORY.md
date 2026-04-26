# Model Theory and Completeness

## The Big Picture

Model theory studies the relationship between formal languages and their interpretations
(models). The central question: which structures satisfy which sentences? It provides the
semantic foundation for FOL and yields powerful tools — compactness, Löwenheim-Skolem,
ultraproducts — that have applications across mathematics.

```
+-------------------------------------------------------------------+
|                    MODEL THEORY LANDSCAPE                         |
|                                                                   |
|  CORE MACHINERY                                                   |
|  +--------------------+                                           |
|  | Signatures         |  ← defines the language                  |
|  | Structures         |  ← give meaning to the language          |
|  | Theories           |  ← sets of sentences true in a class     |
|  | Satisfiability     |                                           |
|  | Elementary equiv.  |  ← same theory (same FOL sentences)      |
|  +--------------------+                                           |
|           |                                                       |
|           | (core machinery feeds)                                |
|           v                                                       |
|  FUNDAMENTAL THEOREMS                                             |
|  +------------------------------------------------------------+   |
|  | Completeness (Godel 1929): T consistent → T has a model   |   |
|  |   ↓ immediate consequence                                  |   |
|  | Compactness: T has a model iff every finite subset does    |   |
|  |   ← also proved directly via Ultraproducts (Los's thm)    |   |
|  |                                                            |   |
|  | Lowenheim-Skolem (down): infinite model → countable model  |   |
|  | Upward LS (Skolem 1922): model of size κ → model any λ≥κ  |   |
|  |   → Together: FOL cannot pin down cardinality              |   |
|  |                                                            |   |
|  | Craig Interpolation: proved via cut elimination            |   |
|  | Beth Definability: follows from Craig Interpolation        |   |
|  +------------------------------------------------------------+   |
|           |                                                       |
|           | (theorems enable)                                     |
|           v                                                       |
|  THEORY CLASSIFICATION          ULTRAPRODUCTS                     |
|  +--------------------+         +-----------------------------+   |
|  | Complete theories  |         | Ultrafilter (needs AC)      |   |
|  | κ-Categorical      |         | Ultraproduct M^I/U          |   |
|  | Model-complete    |←─ QE ──→| Los's theorem               |   |
|  | Quantifier elim.  |         |   → proves Compactness       |   |
|  +--------------------+         |   → non-standard models     |   |
|           |                     +-----------------------------+   |
|           | (classification gives)                                |
|           v                                                       |
|  APPLICATIONS                                                     |
|  +-----------------------------------------------------------+    |
|  | RCF (Tarski): QE → decidable real closed fields           |    |
|  | ACF (algebraically closed): QE → decidable; Nullstellensatz|   |
|  | DLO: QE → complete, decidable; ω-categorical              |    |
|  | Non-standard analysis: ultrapowers of R → infinitesimals  |    |
|  | SMT theories: each background theory uses QE or Nelson-Op |    |
|  | O-minimality: tame topology from ordered field structure  |    |
|  +-----------------------------------------------------------+    |
+-------------------------------------------------------------------+
```

---

## Structures and Theories

### Structures (Review)

A structure M = (D, I) interprets a signature sigma:
- D: non-empty domain
- I maps constants to elements of D, function symbols to functions, predicates to relations.

### Theories

A **theory** T is a set of sentences (closed formulas). The theory of a structure M:
```
  Th(M) = {phi : M |= phi}   (all sentences true in M)
```

Th(M) is always **complete**: for every sentence phi, either phi in Th(M) or neg phi in Th(M).

A theory T is:
- **Satisfiable** if it has a model.
- **Consistent** if no contradiction is derivable (equivalent to satisfiable by completeness).
- **Complete** if for every sentence phi, T |- phi or T |- neg phi.
- **Categorical** if all models of T of a given cardinality are isomorphic.

---

## Gödel Completeness Theorem (1929)

The semantic-syntactic bridge for FOL:

```
  GODEL COMPLETENESS (1929):
  For any FOL theory T and sentence phi:

    T |= phi    iff    T |- phi

  Equivalently: if T has no model, T |- bot (i.e., T is inconsistent).

  PROOF SKETCH (Henkin 1949 method, cleaner than Godel's original):

  1. Assume T is consistent. Build a "maximal consistent" extension T*.
  2. T* is obtained by adding, for every sentence phi, either phi or neg phi.
     (Uses Zorn's lemma / transfinite induction.)
  3. For every Exists x. phi in T*, add a witness constant c with phi[c/x] in T*.
     (These are Henkin constants.)
  4. The resulting T* has a "term model": domain = closed terms,
     interpret a = a, f(t) = f(t), P(t1..tk) iff P(t1..tk) in T*.
  5. This term model satisfies all of T* (by construction), hence all of T.
  6. Therefore T is satisfiable.

  Contrapositive: if T has no model (T |= bot), then T |- bot.
```

**Consequences**:
- Compactness (see below) — follows immediately from the proof.
- Soundness + completeness: |- and |= coincide for FOL.

---

## Compactness Theorem

Perhaps the most useful theorem in model theory:

```
  COMPACTNESS:
  A set T of sentences has a model iff every FINITE subset of T has a model.

  Equivalently:
  If T |= phi, then some finite T0 subset of T already has T0 |= phi.

  PROOF: Immediate from completeness.
  If T |= phi, then T |- phi.
  But a derivation is finite — it uses only finitely many axioms from T.
  So some finite T0 |- phi, hence T0 |= phi.
```

### Applications of Compactness

**Non-standard models**: There exist models of arithmetic larger than the standard naturals.
```
  Let T = PA union {c > 0, c > 1, c > 2, c > 3, ...}
  (Add a new constant c and axioms saying it exceeds every standard numeral.)

  Every finite subset is satisfiable: for {c > 0, ..., c > n}, set c = n+1.
  By compactness: T has a model.
  That model contains "infinitely large" element c beyond all standard naturals.
  This is a non-standard model of PA.
```

**Four-Color Theorem via compactness** (conceptual):
```
  If every finite graph is 4-colorable, then every graph is.
  Proof: Let T say "G is a graph with vertices v1, v2, ... and given edges."
  Add 4 color predicates. Every finite sub-theory (finite subgraph) is 4-colorable.
  Compactness gives a model (4-coloring) for all of G.
```

**Lower-bound transfer**:
```
  If phi holds in structures of arbitrarily large cardinality, it holds in infinite ones.
  (Because the finite subsets of "phi holds in a structure of size > n" are all satisfiable.)
```

---

## Löwenheim-Skolem Theorems

### Downward (Löwenheim 1915, Skolem 1920)

```
  DOWNWARD LOWENHEIM-SKOLEM:
  If T has an infinite model, then T has a countable model.

  More generally: if T has a model of cardinality kappa >= |L| (language cardinality),
  then T has a model of every cardinality lambda >= |L|.
```

### Upward (Skolem 1922)

```
  UPWARD LOWENHEIM-SKOLEM:
  If T has an infinite model of cardinality kappa,
  then T has a model of every cardinality lambda >= kappa.
```

### Skolem's Paradox

```
  PARADOX (Skolem 1922):
  ZFC set theory has a model (by LS, if ZFC is consistent).
  By downward LS, it has a countable model.
  But ZFC proves "uncountable sets exist" (e.g., R is uncountable).

  HOW CAN A COUNTABLE MODEL CONTAIN "UNCOUNTABLE" SETS?

  RESOLUTION:
  The countable model M |= "R is uncountable" means:
  there is no function in M from N to R that is a bijection.

  But from OUTSIDE M, there are only countably many elements of M,
  and a bijection from N to M(R) exists (just not inside M).

  "Uncountable" is RELATIVE to the model: it means no bijection exists in M.
  Not that no bijection exists absolutely.
```

This is a profound point: first-order theories cannot pin down the "true" cardinality
of their intended model. FOL cannot express uncountability absolutely.

---

## Elementary Equivalence and Isomorphism

```
  ISOMORPHISM:
  M ~= N if there is a bijection f: D_M -> D_N preserving structure.
  Isomorphic structures satisfy exactly the same sentences (and formulas with assignments).

  ELEMENTARY EQUIVALENCE:
  M ≡ N if M and N satisfy the same sentences (same theory).
  Written: Th(M) = Th(N).

  RELATIONSHIP:
  Isomorphic => Elementarily equivalent. Converse FAILS for infinite structures.

  Example:
  (Q, <) ≡ (R, <) as linear orders (both satisfy same FOL sentences).
  But they are not isomorphic (different cardinalities, different order properties).

  CATEGORICITY:
  A theory is kappa-categorical if all models of cardinality kappa are isomorphic.

  (Q, <) ordering is omega-categorical (all countable dense linear orders without
  endpoints are isomorphic — back-and-forth argument).
  PA is NOT omega-categorical (has many non-isomorphic countable models).
```

---

## Quantifier Elimination

A theory T admits **quantifier elimination** if every formula is equivalent (modulo T) to
a quantifier-free formula.

```
  WHY IT MATTERS: Quantifier-free formulas are decidable in many theories.
  QE gives decidability of the theory.

  EXAMPLES WITH QE:

  Theory of real closed fields (Tarski 1948):
    Every formula over (R, 0, 1, +, *, <) is equivalent to a quantifier-free formula.
    Consequence: RCF is decidable. (Cylinder Algebraic Decomposition is the algorithm.)
    Example: Exists y. y^2 = x  ===  x >= 0  (quantifier-free!)

  Dense linear orders without endpoints (DLO):
    Every formula over (Q, <) has QE.
    Consequence: DLO is complete and decidable.

  Algebraically closed fields (ACF):
    Every formula over C (complex numbers) has QE.
    Consequence: ACF is complete and decidable.
    (This is the model-theoretic view of the Hilbert Nullstellensatz.)

  Presburger arithmetic (Presburger 1929):
    Every formula over (N, 0, 1, +) has QE with divisibility predicates.
    Consequence: Presburger arithmetic is decidable.

  NO QUANTIFIER ELIMINATION:
  Peano arithmetic: Exists x. x*x = y (squareness) is not quantifier-free expressible.
  This is related to why PA is not decidable.
```

---

## Ultraproducts

A powerful construction for building new models from old ones.

### Ultrafilters

```
  An ultrafilter U on a set I is a collection of subsets of I such that:
  (1) I in U
  (2) If A in U and A subset B, then B in U
  (3) If A, B in U, then A inter B in U
  (4) For every A subset I: either A in U or I\A in U (but not both)

  Principal ultrafilter: U = {A : i0 in A} for a fixed i0. (trivial case)
  Non-principal (free) ultrafilter: contains no finite sets.
  Existence of non-principal ultrafilters requires Axiom of Choice.
```

### Ultraproduct Construction

Given structures M_i indexed by I, and ultrafilter U on I:

```
  ULTRAPRODUCT M^I/U:

  Domain: equivalence classes of functions f: I -> union(D_{M_i})
  under the equivalence: f ~ g  iff  {i : f(i) = g(i)} in U

  Interpret P([f1],...,[fk]) iff  {i : M_i |= P(f1(i),...,fk(i))} in U
```

### Łoś's Theorem

```
  LOS'S THEOREM (fundamental theorem of ultraproducts):
  For any sentence phi:
    M^I/U |= phi   iff   {i : M_i |= phi} in U

  If all M_i are the same structure M:
    M^I/U |= phi   iff   M |= phi

  (Ultrapower of M satisfies the same sentences as M.)
```

**Application — Compactness from Łoś:**
```
  If every finite subset of T has a model:
  Index the models by finite subsets: for each S, M_S |= S.
  Form ultraproduct over a suitable ultrafilter.
  Łoś's theorem gives the ultraproduct satisfies all of T.
```

**Application — Non-standard analysis:**
```
  Take ultrapowers of R: R* = R^N/U (non-principal U).
  R* is an ordered field containing infinitesimals: epsilon with 0 < epsilon < 1/n for all n in N.
  R* |= same first-order sentences as R (by Łoś).
  This is the rigorous foundation of Robinson's non-standard analysis.
```

---

## Craig Interpolation and Beth Definability

```
  CRAIG INTERPOLATION THEOREM:
  If phi |= psi, then there exists chi (over the common signature of phi and psi) such that:
    phi |= chi  and  chi |= psi

  chi uses only the non-logical symbols shared by phi and psi.

  Proof: via cut elimination in sequent calculus.

  APPLICATION: phi is an abstract specification; psi is a concrete implementation.
  chi is an interface or contract between them.
  Craig interpolation is why interface types exist in programming languages.
```

```
  BETH DEFINABILITY THEOREM:
  A predicate P is implicitly definable in T (all models of T that agree on
  the rest agree on P) iff it is explicitly definable (there is a formula phi
  equivalent to P in all models of T).

  "Implicit definability = explicit definability" — a strong uniqueness result.
```

---

## Decision Cheat Sheet

| I want to... | Use |
|---|---|
| Show a theory has a model | Build it (Henkin construction) or use compactness |
| Show a theory has models of all infinite cardinalities | Upward Löwenheim-Skolem |
| Show a theory has a countable model | Downward Löwenheim-Skolem |
| Check if two structures are elementarily equivalent | Compare their theories |
| Decide if a theory is complete | Check if it is categorical, or find QE |
| Decide if a theory is decidable | Find quantifier elimination |
| Build non-standard models | Compactness (add infinitely large/small constants) |
| Build new models via averaging | Ultraproducts + Łoś's theorem |
| Find an interpolant between two statements | Craig interpolation |

---

## Common Confusion Points

**Isomorphism vs. elementary equivalence.**
Isomorphism is structure-preserving bijection (stronger). Elementary equivalence is same
first-order theory (weaker). The two coincide only for finite structures. Non-isomorphic
infinite structures can be elementarily equivalent.

**Skolem's paradox is not a paradox.**
A countable model of ZFC "believes" R is uncountable because it has no internal bijection
from N to R. The bijection exists externally but not within the model. FOL cannot express
absolute uncountability — all it can say is "no internal bijection exists."

**Compactness fails for second-order logic.**
FOL is compact; SOL is not. SOL can pin down the naturals up to isomorphism (categorical),
but then compactness fails. The price of categoricity is loss of compactness.

**QE doesn't mean the theory is trivial.**
Real closed fields have QE and are decidable, but they are rich enough to express all
real algebraic geometry. QE says the theory is "tame" not "simple."

**Non-standard models of PA are not "wrong."**
They satisfy all PA axioms. From PA's perspective, they are valid models. The "standard" model
is standard only from our external perspective — PA itself cannot distinguish it.
