# Category Theory

## The Big Picture

```
+====================================================================+
|          CATEGORY THEORY — THE LANGUAGE OF STRUCTURE               |
+====================================================================+
|                                                                    |
|  CATEGORY C:                                                       |
|  - Objects: Ob(C)                                                  |
|  - Morphisms: Hom(A,B) for each pair A, B                         |
|  - Composition: f: A→B, g: B→C  ↦  g∘f: A→C                      |
|  - Identity: id_A: A→A for each object A                          |
|  - Associativity: (h∘g)∘f = h∘(g∘f)                              |
|  - Unit laws: id∘f = f, f∘id = f                                  |
|                                                                    |
|  FUNCTOR F: C → D: maps objects to objects, morphisms to           |
|  morphisms, preserving composition and identity.                   |
|                                                                    |
|  NATURAL TRANSFORMATION η: F ⟹ G: for each object A, a           |
|  morphism η_A: F(A) → G(A), natural in A (commuting square).      |
|                                                                    |
|  ADJUNCTION: F ⊣ G means Hom(F(A),B) ≅ Hom(A,G(B)) natural.     |
|                                                                    |
|  YONEDA LEMMA: Nat(Hom(A,-), F) ≅ F(A) — objects are determined  |
|  by how other objects map into them.                               |
+====================================================================+
```

Category theory is the "mathematics of mathematics." It doesn't study any
particular structure but rather the relationships between structures.
Its language permeates modern algebra, topology, logic, and computer science.

---

## Categories

```
EXAMPLES OF CATEGORIES:

Set:   Objects = sets, morphisms = functions.
Grp:   Objects = groups, morphisms = group homomorphisms.
Ab:    Objects = abelian groups, morphisms = group homomorphisms.
Ring:  Objects = rings, morphisms = ring homomorphisms.
Vect_k: Objects = k-vector spaces, morphisms = linear maps.
Top:   Objects = topological spaces, morphisms = continuous maps.
Pos:   Objects = posets, morphisms = order-preserving maps.
Cat:   Objects = (small) categories, morphisms = functors.

DEGENERATE CASES:
  Monoid as category: one object *, Hom(*,*) = elements of monoid.
    Composition = monoid multiplication.
  Group as category: one object, all morphisms invertible.
  Poset as category: objects = elements, Hom(a,b) has one element iff a ≤ b.
    The morphism is the "evidence that a ≤ b."

OPPOSITE CATEGORY C^op: same objects, morphisms reversed.
  f: A→B in C becomes f^op: B→A in C^op.
  Every concept in category theory has a "dual" obtained by C → C^op.
  Dual of "product" = "coproduct". Dual of "limit" = "colimit".
```

---

## Functors

```
FUNCTOR F: C → D:
  F maps: Ob(C) → Ob(D) and Hom_C(A,B) → Hom_D(F(A),F(B)).
  Preserves: F(g∘f) = F(g)∘F(f) and F(id_A) = id_{F(A)}.

COVARIANT vs CONTRAVARIANT:
  Covariant: F(f: A→B) = F(f): F(A)→F(B).
  Contravariant: F(f: A→B) = F(f): F(B)→F(A). (Reverses arrows.)
  Contravariant functor C→D = covariant functor C^op→D.

EXAMPLES:
  Forgetful functor U: Grp → Set (forget group structure).
  Free functor F: Set → Grp (free group on a set).
  Powerset: Set → Set (covariant: f↦f(−), contravariant: f↦f^{-1}(−)).
  Hom(A,-): C → Set: B ↦ Hom(A,B). Covariant. (Representable functor.)
  Hom(-,B): C → Set: A ↦ Hom(A,B). Contravariant.
  Tensor: M ⊗_R -: R-Mod → R-Mod.
  Homology: Top → Ab (a covariant functor from spaces to abelian groups).
  Galois correspondence: subfields ↔ subgroups is a contravariant functor.
  K-theory: C* algebras → Ab (topological K-theory).

FULL, FAITHFUL, ESSENTIALLY SURJECTIVE:
  Full: each Hom(A,B) → Hom(FA,FB) is surjective.
  Faithful: each Hom(A,B) → Hom(FA,FB) is injective.
  Equivalence of categories: F is full, faithful, and essentially surjective.
    (Essentially surjective: every D-object is isomorphic to some F(C).)
```

---

## Natural Transformations

```
NATURAL TRANSFORMATION η: F ⟹ G (between functors F,G: C → D):
  For each A ∈ Ob(C): a morphism η_A: F(A) → G(A) in D.
  Naturality condition: for every f: A → B in C:
    G(f) ∘ η_A = η_B ∘ F(f)
  (The square commutes: both paths from F(A) to G(B) agree.)

NATURAL ISOMORPHISM: η is a natural transformation where every η_A is an isomorphism.
  F ≅ G means they're naturally isomorphic.

EXAMPLES:
  Double dual: V → V** (for f.d. vector spaces).
    The map v ↦ (φ ↦ φ(v)) is natural in V.
    Compare: V ≅ V* (for f.d. inner product spaces) but NOT naturally.
  Determinant: GL_n(-): Ring → Grp, with det a natural transformation.
  Group cohomology: H^n(-,M): Grp → Ab.

THE NATURALITY OF DETERMINANT:
  For ring homomorphism φ: R → S:
    GL_n(R) → GL_n(S)  (apply φ entrywise)
    det_R: GL_n(R) → R*   det_S: GL_n(S) → S*
  Naturality: φ(det_R(A)) = det_S(φ(A)).
  (Applying ring map then taking determinant = taking determinant then applying ring map.)
```

---

## Adjunctions

```
ADJUNCTION F ⊣ G (F left adjoint, G right adjoint):
  F: C → D,  G: D → C.
  Natural bijection: Hom_D(F(A), B) ≅ Hom_C(A, G(B)).
  "Maps out of FA ↔ maps into GB."

UNIT AND COUNIT:
  Unit: η_A: A → G(F(A)) (from C to C, "universal map into adjoint")
  Counit: ε_B: F(G(B)) → B (from D to D, "universal map from adjoint")
  Triangle identities: G(ε)∘η_G = id_G and ε_F∘F(η) = id_F.

EXAMPLES OF ADJUNCTIONS (pervasive in mathematics):
  Free ⊣ Forgetful: Free(S) ⊣ U(G).
    Hom_Grp(Free(S), G) ≅ Hom_Set(S, U(G)).
    "Group maps from free group = functions from generating set."

  Product ⊣ Diagonal: (- × A) ⊣ Hom(A,-).
    Hom(B×A, C) ≅ Hom(B, Hom(A,C)).  [Curry-Howard!]
    This is the tensor-hom adjunction for sets/vector spaces.

  Tensor ⊣ Hom: M⊗_R - ⊣ Hom_R(M,-).
    Hom_R(M⊗N, P) ≅ Hom_R(N, Hom_R(M,P)).

  Colimit ⊣ Constant: (computing colimit) ⊣ (sending to constant diagram).

  Suspension ⊣ Loop: Σ ⊣ Ω in homotopy theory.

  Sheafification ⊣ Inclusion: in sheaf theory/algebraic geometry.

CURRY-HOWARD CORRESPONDENCE (PROGRAMMING):
  Products × correspond to conjunction ∧.
  Functions A→B correspond to implication A⟹B.
  The adjunction Hom(B×A, C) ≅ Hom(B, A→C) is "currying."
  In Haskell: curry :: ((a,b) -> c) -> a -> b -> c.
```

---

## Limits and Colimits

```
DIAGRAM: A functor J → C (from small category J to category C).

LIMIT (= "cone over the diagram"):
  An object L with maps L → J(i) for each i ∈ J, universal with this property.
  "Best approximation to the whole diagram from the outside."

COLIMIT (= "cocone over the diagram"):
  An object C with maps J(i) → C for each i, universal with this property.
  "Best approximation from the inside."

SPECIFIC LIMITS:
  Product: diagram = two objects A, B (no morphisms between them).
    Limit = A × B (with projections). Exists in Set, Grp, Top, etc.

  Pullback (fiber product): diagram A →^f C ←^g B.
    Limit = A ×_C B = {(a,b) : f(a)=g(b)}.
    In algebraic geometry: fiber product of schemes = intersection.

  Equalizer: diagram A ⇉ B (two parallel arrows).
    Limit = {a ∈ A : f(a) = g(a)}.

  Terminal object: limit of empty diagram.
    Set: {*}. Grp: {e}. Top: {*}.

SPECIFIC COLIMITS:
  Coproduct: two objects A, B.
    Set: disjoint union A ⊔ B.
    Grp: free product A * B (most general group containing A and B).
    Ab: A ⊕ B (direct sum = product for abelian groups).
    Top: disjoint union.

  Pushout (amalgamated product): C →^f A, C →^g B.
    Colimit = A *_C B = (A * B) / (f(c) = g(c) for all c ∈ C).
    Van Kampen theorem: π₁(X∪Y) = π₁(X) *_{π₁(X∩Y)} π₁(Y). [Pushout of groups!]

  Coequalizer: A ⇉ B.
    B / (f(a) ~ g(a) for all a ∈ A).

  Initial object: colimit of empty diagram.
    Set: ∅. Grp: {e}. Ring: Z (initial ring).
```

---

## Yoneda Lemma

```
YONEDA LEMMA: For functor F: C → Set and object A ∈ Ob(C):
  Nat(Hom_C(A, -), F) ≅ F(A)   naturally in both A and F.

  Natural transformations from the representable functor Hom(A,-) to F
  are in bijection with elements of F(A).

YONEDA EMBEDDING: The functor y: C → [C^op, Set] by A ↦ Hom(-,A).
  This functor is FULL and FAITHFUL (an embedding).
  "An object A is completely determined by the functor Hom(-,A)."
  = "Objects are determined by how other things map into them."

COROLLARY: If Hom(X, A) ≅ Hom(X, B) naturally in X, then A ≅ B.
  Universal properties determine objects uniquely up to isomorphism.

APPLICATIONS:
  Universal properties are all instances of Yoneda.
  Products: Hom(X, A×B) ≅ Hom(X,A)×Hom(X,B) naturally.
  Tensor products: defined by universal bilinear map.
  Group cohomology: H^n(G, M) ≅ Nat(F_n, M) for appropriate F_n.

REPRESENTABLE FUNCTORS:
  F: C → Set is representable if F ≅ Hom(A,-) for some A.
  "A" represents F. Universal property = representation.
  Yoneda says: representation is unique up to isomorphism.
```

---

## Monads

```
MONAD (T, η, μ) on category C:
  T: C → C  (endofunctor)
  η: Id ⟹ T  (unit, natural transformation)
  μ: T∘T ⟹ T  (multiplication/join, natural transformation)
  Satisfying: μ ∘ Tη = id_T = μ ∘ ηT  and  μ ∘ μT = μ ∘ Tμ.
  (Just like a monoid: unit and associative multiplication.)

  "A monad is just a monoid in the category of endofunctors."
  (Famously quoted; this is technically precise.)

EXAMPLES:
  List monad (in Haskell: [] monad):
    T(A) = List(A) = A* (all finite lists of A's).
    η(a) = [a] (singleton list).
    μ([[a,b],[c,d]]) = [a,b,c,d] (concatenation/flatten).

  Maybe monad: T(A) = A ⊔ {Nothing}.
    Models failure/partiality.

  State monad: T(A) = (S → A × S).
    Models stateful computation.

  Continuation monad: T(A) = ((A → R) → R).
    Models continuation-passing style.

  Reader monad: T(A) = (E → A).
    Models access to environment.

  IO monad (Haskell): Models effects; keeps purity.

KLEISLI CATEGORY:
  Morphisms A → T(B) in C become morphisms A → B in the Kleisli category.
  Composition: A →^f T(B) →^{T(g)} T(T(C)) →^{μ_C} T(C).
  This is "effectful computation chaining" — the essence of monadic bind (>>=).

CONNECTION TO ADJUNCTIONS:
  Every adjunction F ⊣ G gives a monad T = G∘F.
  Conversely, every monad arises from an adjunction (Kleisli or Eilenberg-Moore).
```

---

## Connection to Programming

```
HASKELL TYPE SYSTEM ≈ CARTESIAN CLOSED CATEGORY (CCC):

Product type (a, b) → categorical product A × B.
Sum type Either a b → categorical coproduct A ⊔ B.
Function type a -> b → internal hom (exponential) B^A.
                        or "Hom(A, B)" as an object.

CURRY-HOWARD-LAMBEK CORRESPONDENCE:
  Logic          ↔  Types          ↔  Category theory
  Proposition    ↔  Type           ↔  Object
  Proof          ↔  Term/Program   ↔  Morphism
  Conjunction P∧Q↔  (P, Q)         ↔  Product P×Q
  Implication P⟹Q↔  P -> Q         ↔  Exponential Q^P
  Truth ⊤        ↔  ()             ↔  Terminal object
  Falsum ⊥       ↔  Void           ↔  Initial object
  Cut rule       ↔  Let binding    ↔  Composition

FUNCTOR LAWS (Haskell):
  fmap id = id
  fmap (g . f) = fmap g . fmap f
  These are exactly the functor axioms F(id)=id, F(g∘f)=F(g)∘F(f).

MONAD LAWS (Haskell):
  return a >>= f = f a           (left unit: μ∘ηT = id)
  m >>= return = m               (right unit: μ∘Tη = id)
  (m >>= f) >>= g = m >>= (\x -> f x >>= g) (associativity: μ∘μT = μ∘Tμ)

TYPE THEORY EXTENSIONS:
  Dependent types (Π-types, Σ-types) → locally Cartesian closed categories.
  Homotopy type theory (HoTT) → ∞-toposes (Voevodsky, Lurie).
  Universes in type theory → Grothendieck universes in set theory.
```

---

## Decision Cheat Sheet

| Concept | What it does |
|---------|-------------|
| Category | Organizes objects and their relationships (morphisms) |
| Functor | Structure-preserving map between categories |
| Natural transformation | Morphism between functors (coherent family) |
| Adjunction F⊣G | Hom(F-,−) ≅ Hom(-,G-); universal properties |
| Yoneda | Objects are their "probes" (representable functors) |
| Limit | Universal cone; includes products, pullbacks, equalizers |
| Colimit | Universal cocone; includes coproducts, pushouts, quotients |
| Monad | Monoid in endofunctor category; models effects in PL |
| Cartesian closed | Has products and exponentials; models typed lambda calculus |

---

## Common Confusion Points

**"Category theory is just language with no content."**
Yoneda's lemma is a real theorem with content: representable functors are determined
by a single element. All universal properties (tensor products, free groups, limits)
follow from it. The derived category, topos theory, and higher category theory are
genuine mathematical advances, not just new vocabulary.

**"A functor is the same as a homomorphism."**
A homomorphism is a morphism in an algebraic category (Grp, Ring, etc.).
A functor is a map between categories — it maps both objects and morphisms.
A functor from a one-object category (= a monoid) to Set is exactly a monoid action.
Functors generalize algebra-level homomorphisms to a higher level.

**"Every adjunction gives a unique monad."**
The monad T = GF is uniquely determined by the adjunction. But a given monad
can arise from multiple different adjunctions. The two canonical ones are:
the Kleisli category (the free one) and the Eilenberg-Moore category (the "free" one
in the other direction). Beck's theorem characterizes when G comes from a monad.

**"Monads in Haskell are exactly the categorical monads."**
Haskell's Monad typeclass implements the Kleisli category of a monad in Hask
(the category of Haskell types and functions). The >>= operator is exactly
Kleisli composition. The laws (left/right unit, associativity) are exactly
the monad axioms. So yes, they're the same — modulo set-theoretic foundations.
