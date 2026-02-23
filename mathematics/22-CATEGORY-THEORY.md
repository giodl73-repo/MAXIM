# Category Theory — Complete Reference

## The Big Picture

Category theory is the mathematics of mathematical structure — it studies objects and the structure-preserving maps between them, abstracted away from what the objects actually are. From your MIT TCS background, you already know it shows up in type theory (functors ↔ polymorphism, monads ↔ computational effects, adjunctions ↔ Curry-Howard). This guide makes those connections explicit and builds from scratch.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  CATEGORY THEORY LANDSCAPE                                                   │
│                                                                              │
│  Foundations                          Universal Constructions                │
│  ──────────────────────────────        ──────────────────────────────────     │
│  Category: objects + morphisms        Products, coproducts                  │
│  Functor: structure-preserving map    Limits, colimits                       │
│  Natural transformation: functor map  Equalizers, pullbacks, pushouts       │
│  Isomorphism, equivalence             Initial/terminal objects               │
│                                                                              │
│  Adjunctions                          Monads                                 │
│  ──────────────────────────────        ──────────────────────────────────     │
│  F ⊣ G: universal property           T = GF, unit/counit, monad laws        │
│  Unit and counit                      Kleisli category                       │
│  Triangle identities                  Eilenberg-Moore algebras               │
│  Freeness and forgetfulness           Every adjunction gives a monad        │
│                                                                              │
│  PL Theory Connections                Higher Categories                     │
│  ──────────────────────────────        ──────────────────────────────────     │
│  Curry-Howard: proofs = programs      2-categories (morphisms of morphisms)  │
│  Types = objects, terms = morphisms   ∞-categories (homotopy theory)        │
│  Products = pair types                Topos theory (generalized sets)       │
│  Coproducts = sum types               Homotopy type theory (HoTT)          │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 1. Categories

### Definition

A **category** 𝒞 consists of:
```
Objects:  Ob(𝒞) — a collection of objects.
Morphisms: For each pair A, B ∈ Ob(𝒞), a collection Hom(A,B) of morphisms A → B.

Composition: For f: A→B, g: B→C, a morphism g∘f: A→C.
Identity: For each A, a morphism id_A: A→A.

Laws:
  Associativity: (h∘g)∘f = h∘(g∘f)
  Unit:          id_B ∘ f = f = f ∘ id_A   for f: A→B
```

### Key Examples

| Category | Objects | Morphisms | Notes |
|----------|---------|-----------|-------|
| **Set** | Sets | Functions | The paradigm example |
| **Grp** | Groups | Group homomorphisms | |
| **Top** | Topological spaces | Continuous maps | |
| **Vect_k** | k-vector spaces | Linear maps | |
| **Pos** | Posets | Monotone functions | |
| **Cat** | Small categories | Functors | Categories form a category |
| **Hask** | Haskell types | Haskell functions | (up to ⊥ and seq issues) |
| **Mon** | Monoids | Monoid homomorphisms | |
| **Ring** | Rings | Ring homomorphisms | |

**Discrete category**: Objects = set S, only identity morphisms. No structure.

**Indiscrete category**: Every pair (A,B) has exactly one morphism.

**Monoid as category**: One object *, morphisms = monoid elements, composition = monoid operation. Monoids are exactly one-object categories.

**Poset as category**: Objects = elements, at most one morphism A→B (iff A ≤ B). Functors between posets = monotone functions. Adjunctions between posets = Galois connections.

### Special Morphisms

```
Monomorphism (monic): f: A→B where f∘g = f∘h → g = h.   [generalized injective]
Epimorphism (epic):   f: A→B where g∘f = h∘f → g = h.    [generalized surjective]
Isomorphism:          f: A→B s.t. ∃g: B→A with g∘f=id_A and f∘g=id_B.
Endomorphism:         f: A→A.
Automorphism:         isomorphism from A to A.

In Set: mono = injection, epi = surjection, iso = bijection.
In Top: mono = injection (even non-homeomorphisms can be monic).
        epi ≠ surjection (ℚ→ℝ is epic in Hausdorff spaces but not surjective).
```

---

## 2. Functors

### Definition

A **functor** F: 𝒞 → 𝒟 between categories assigns:
```
Object map:   A ↦ F(A) for each A ∈ Ob(𝒞)
Morphism map: (f: A→B) ↦ (F(f): F(A)→F(B)) for each morphism f

Laws:
  Preserves identity:    F(id_A) = id_{F(A)}
  Preserves composition: F(g∘f) = F(g) ∘ F(f)

This is a covariant functor.
```

**Contravariant functor**: Reverses arrows. F(f: A→B) = F(f): F(B)→F(A). F(g∘f) = F(f)∘F(g).

Equivalently: a contravariant functor F: 𝒞 → 𝒟 is a covariant functor F: 𝒞^{op} → 𝒟 where 𝒞^{op} has all arrows reversed.

### Functor Examples

**Forgetful functors**: "Forget" algebraic structure.
```
U: Grp → Set: sends group (G,·) to underlying set G, homomorphism to underlying function.
U: Ring → Grp: forgets multiplicative structure.
U: Vect_k → Set: forgets vector space structure.
```

**Free functors**: "Freely" add structure.
```
F: Set → Grp: free group on generators.
F: Set → Mon: free monoid = lists (strings).
F: Set → Vect_k: free vector space = formal linear combinations.
```

Free and forgetful functors are always adjoint: F ⊣ U (free left-adjoint to forgetful).

**Power set functor**:
```
P: Set → Set
  P(A) = ℙ(A) (power set)
  P(f: A→B) = (S ↦ f(S)) : ℙ(A) → ℙ(B)  [covariant: direct image]
  P*(f) = (T ↦ f⁻¹(T)) : ℙ(B) → ℙ(A)    [contravariant: preimage]
```

**Hom functors**: For fixed B, Hom(-,B): 𝒞^{op} → Set (contravariant).
For fixed A, Hom(A,-): 𝒞 → Set (covariant).
```
Hom(A,-)  sends C → Hom(A,C),  (f: C→D) ↦ (g ↦ f∘g)   [post-compose]
Hom(-,B)  sends C → Hom(C,B),  (f: A→C) ↦ (g ↦ g∘f)   [pre-compose]
```

### The Yoneda Lemma

One of the most important results in category theory:

```
Yoneda Lemma:
  For any functor F: 𝒞 → Set and any object A ∈ 𝒞:
  Nat(Hom(A,-), F) ≅ F(A)

  Natural transformations from the representable functor Hom(A,-)
  to any functor F are in bijection with elements of F(A).
```

**Corollary** (Yoneda embedding): The functor y: 𝒞 → Fun(𝒞^{op}, Set) defined by A ↦ Hom(-,A) is **fully faithful**. Categories embed faithfully into functor categories.

**Intuition**: An object A is completely determined by how all other objects map into it (its "incoming maps"). You can reconstruct A from its Hom-set behavior. "An object is known by its relationships."

**Practical consequence**: Two objects A, B are isomorphic iff Hom(C,A) ≅ Hom(C,B) naturally in C. Universal properties define objects up to isomorphism.

---

## 3. Natural Transformations

### Definition

For functors F, G: 𝒞 → 𝒟, a **natural transformation** η: F ⇒ G assigns:
- For each object A ∈ Ob(𝒞), a morphism η_A: F(A) → G(A) in 𝒟.

Such that for each morphism f: A → B in 𝒞:
```
Naturality square commutes:
  F(A) ──F(f)──→ F(B)
   |                |
  η_A              η_B
   ↓                ↓
  G(A) ──G(f)──→ G(B)

i.e., η_B ∘ F(f) = G(f) ∘ η_A
```

**Natural isomorphism**: η where every component η_A is an isomorphism.

### Examples

```
Double dual embedding for vector spaces:
  η_V: V → V** defined by η_V(v)(f) = f(v)  [evaluation]
  This is a natural transformation from Id_{Vect} to (-)**
  It's a natural isomorphism for finite-dimensional vector spaces.
  (Not natural in the sense that V ≅ V* requires choosing a basis — that's unnatural!)

Determinant: det: GL_n(-) → (-)*  (from matrix groups to multiplicative units)
  det is natural: det(f∘g) = det(f)·det(g) for any ring homomorphism.

List.map in Haskell: for each f: a → b, map f: List a → List b.
  map is a natural transformation between two endofunctors on Hask.
```

### Functor Categories

For categories 𝒞, 𝒟: the **functor category** [𝒞, 𝒟] (or 𝒟^𝒞):
- Objects: functors F: 𝒞 → 𝒟
- Morphisms: natural transformations η: F ⇒ G

Composition of natural transformations:
- Vertical composition: (α: F⇒G, β: G⇒H) → β∘α: F⇒H [component-wise]
- Horizontal composition: (α: F⇒G: 𝒜→ℬ, β: H⇒K: ℬ→𝒞) → β·α: H∘F ⇒ K∘G

**2-category structure**: Objects=categories, 1-morphisms=functors, 2-morphisms=natural transformations. The first non-trivial example of higher categorical structure.

---

## 4. Universal Properties and Limits

### Terminal and Initial Objects

```
Terminal object 1: for all A, ∃! morphism A → 1.
  Set: terminal = {*} (any singleton set)
  Grp: terminal = trivial group {e}
  Top: terminal = one-point space

Initial object 0: for all A, ∃! morphism 0 → A.
  Set: initial = ∅ (empty set)
  Grp: initial = trivial group
  Ring: initial = ℤ (integers)

Terminal/initial objects are unique up to unique isomorphism.
```

### Products and Coproducts

**Product** A×B with projections π₁: A×B→A, π₂: A×B→B:
```
Universal property: for any C with f: C→A, g: C→B,
  ∃! (f,g): C → A×B with π₁∘(f,g)=f, π₂∘(f,g)=g.

Set: Cartesian product A×B.
Grp: direct product G×H.
Top: product topology.
Types: pair type A×B (and types).
Logic: conjunction A∧B.
```

**Coproduct** A+B with injections ι₁: A→A+B, ι₂: B→A+B:
```
Universal property: for any C with f: A→C, g: B→C,
  ∃! [f,g]: A+B → C with [f,g]∘ι₁=f, [f,g]∘ι₂=g.

Set: disjoint union A⊔B.
Grp: free product G*H.
Top: disjoint union topology.
Types: sum type A|B (or types).
Logic: disjunction A∨B.
```

### Limits and Colimits

**Limit** of a diagram F: J → 𝒞 (J = "shape" category):
```
Cone over F: object L with morphisms λⱼ: L → F(j) making all triangles commute.
Limit = universal cone (initial among all cones).

Examples:
  J = {• •} (discrete, two objects): limit = product A×B
  J = {• → • ← •}: limit = pullback (fiber product)
  J = {• ⇉ •} (parallel arrows): limit = equalizer
  J = empty category: limit = terminal object

Limits in Set: subset of product satisfying compatibility conditions.
  lim F = { (aⱼ) ∈ ∏ⱼ F(j) : ∀(f: j→k), F(f)(aⱼ) = aₖ }
```

**Colimit** of F: J → 𝒞:
```
Cocone under F: object C with morphisms μⱼ: F(j) → C.
Colimit = universal cocone (terminal among all cocones).

Examples:
  J = {• •}: colimit = coproduct A+B
  J = {• → • ← •}: colimit = pushout
  J = {• ⇉ •}: colimit = coequalizer
  J = empty: colimit = initial object
  J = ℕ (sequence): colimit = direct limit (filtered colimit)

Colimits in Set: quotient of coproduct by compatibility equivalence relation.
```

**Key fact**: Left adjoints preserve colimits; right adjoints preserve limits.

---

## 5. Adjunctions

### Definition

An **adjunction** F ⊣ G (F left adjoint, G right adjoint) between F: 𝒞→𝒟, G: 𝒟→𝒞 is:
```
A natural bijection: Hom_𝒟(F(A), B) ≅ Hom_𝒞(A, G(B))

Natural in both A ∈ Ob(𝒞) and B ∈ Ob(𝒟).
```

Equivalently (via Yoneda): there exist natural transformations:
```
Unit:   η: Id_𝒞 ⇒ G∘F   (η_A: A → GF(A))
Counit: ε: F∘G ⇒ Id_𝒟   (ε_B: FG(B) → B)

Satisfying triangle identities:
  (εF) ∘ (Fη) = Id_F     (G∘ε) ∘ (η∘G) = Id_G
  i.e., for each A: ε_{F(A)} ∘ F(η_A) = id_{F(A)}
         for each B: G(ε_B) ∘ η_{G(B)} = id_{G(B)}
```

### Adjunction Examples

**Free-forgetful**:
```
F ⊣ U: Free ⊣ Forgetful

Example: F: Set → Grp (free group), U: Grp → Set (underlying set).
  Hom_Grp(F(S), G) ≅ Hom_Set(S, U(G))
  Group homomorphisms from free group on S = functions from S to underlying set of G.

Unit: η_S: S → U(F(S)) = inclusion of generators into free group.
Counit: ε_G: F(U(G)) → G = evaluation (map each generator g ∈ G to g ∈ G).

Same pattern: free monoid (lists) ⊣ forgetful (Mon→Set),
  free vector space ⊣ forgetful, free ring ⊣ forgetful.
```

**Currying**:
```
(- × A) ⊣ (- → A)^{op}   in Set (or suitable CCC)
  or  - ⊗ A ⊣ A → -        in a closed monoidal category

Hom(B × A, C) ≅ Hom(B, A → C)

This is the categorical formulation of currying!
Unit: η_B: B → (A → B×A)  i.e., η_B(b)(a) = (b,a)
Counit: ε_C: (A→C) × A → C  i.e., ε_C(f,a) = f(a)   [evaluation]

Curry-Howard connection:
  (A ∧ B) → C  ≅  A → (B → C)   [logical form]
  This is the same adjunction in the Cartesian closed category of propositions.
```

**Diagonal-product/coproduct**:
```
Δ: 𝒞 → 𝒞×𝒞  (diagonal: A ↦ (A,A))
Δ ⊣ (×) [product is right adjoint to diagonal]
(+) ⊣ Δ [coproduct is left adjoint to diagonal]

Expresses: "product is the right way to combine; coproduct is the left way."
```

**Galois connection** (adjunction between posets):
```
For posets P, Q with f: P→Q (monotone), g: Q→P (monotone):
  f ⊣ g  iff  f(p) ≤ q  ↔  p ≤ g(q)

Example: Galois theory.
  P = subfields of splitting field (reversed by ⊆).
  Q = subgroups of Galois group.
  f(L) = Gal(K/L), g(H) = Fix(H).
  f ⊣ g is the fundamental theorem of Galois theory.
```

### Adjunctions Generate Monads

Every adjunction F ⊣ G produces a monad T = G∘F on 𝒞:
```
T = G∘F: 𝒞 → 𝒞
Unit η: Id_𝒞 ⇒ T    (from adjunction unit)
Multiplication μ: T² ⇒ T   defined as μ_A = G(ε_{F(A)}): GFGF(A) → GF(A)

Monad laws follow from triangle identities.
```

Conversely (Kleisli / Eilenberg-Moore): every monad comes from an adjunction.

---

## 6. Monads

### Definition

A **monad** on 𝒞 is a triple (T, η, μ) where:
```
T: 𝒞 → 𝒞   (endofunctor)
η: Id ⇒ T   (unit / return)
μ: T² ⇒ T   (multiplication / join / bind)

Monad laws (associativity and unit):
  μ ∘ Tμ = μ ∘ μT   [associativity]
  μ ∘ Tη = id = μ ∘ ηT  [left and right unit]

Commutative diagrams:
  T³ ──Tμ──→ T²
  |              |
  μT            μ
  ↓              ↓
  T²  ──μ───→ T
```

### Monads as Computations (Haskell / PL Theory)

In Haskell, a monad is a typeclass:
```haskell
class Functor f => Monad f where
  return :: a -> f a              -- unit η
  (>>=)  :: f a -> (a -> f b) -> f b  -- bind (derived from μ and fmap)

-- Laws:
-- Left unit:  return a >>= f  =  f a
-- Right unit: m >>= return    =  m
-- Assoc:      (m >>= f) >>= g = m >>= (\x -> f x >>= g)

-- Note: (>>=) = flip (μ ∘ T(-))
-- join :: f (f a) -> f a    -- multiplication μ
-- join = (>>= id)
```

**The key insight**: Monads encode computational effects in a pure type system.

| Monad | Effect encoded | return | bind |
|-------|---------------|--------|------|
| Maybe | Partiality/failure | Just | chain, propagate Nothing |
| List | Nondeterminism | [x] | cartesian product |
| IO | Side effects | pure a | sequential composition |
| State s | Mutable state | pure a | thread state through |
| Reader r | Read-only environment | const a | pipe environment |
| Writer w | Logging/output | (a, mempty) | accumulate w |
| Cont r | Continuations | \k -> k a | CPS transform |
| Either e | Checked exceptions | Right | propagate Left |

**Kleisli category**: For monad T on 𝒞, define 𝒞_T (Kleisli category):
- Objects: same as 𝒞
- Morphisms: A →_T B = A → T(B) in 𝒞 (Kleisli arrows / "effectful functions")
- Composition: f:A→T(B), g:B→T(C): compose as g⋄f = μ_C ∘ T(g) ∘ f

This is exactly `>>=` bind chaining: `f >=> g = \x -> f x >>= g`.

### Monad Transformers

Stack monads to combine effects:
```haskell
newtype StateT s m a = StateT { runStateT :: s -> m (a, s) }

instance Monad m => Monad (StateT s m) where
  return a = StateT $ \s -> return (a, s)
  m >>= k  = StateT $ \s -> do
               (a, s') <- runStateT m s
               runStateT (k a) s'

-- Stack: StateT s (ExceptT e IO) a = s -> IO (Either e (a, s))
```

**mtl (monad transformer library)**: defines typeclasses (MonadState, MonadError, MonadReader) so code is polymorphic over monad stack.

---

## 7. Topos Theory (Sketch)

### What is a Topos?

A **topos** is a category that behaves like **Set** — it has enough structure to do internal logic and set-theory-like constructions.

```
Elementary topos: a category 𝒞 with:
  1. Finite limits (products, equalizers, pullbacks)
  2. Exponentials A^B (function objects / "internal hom")
     Hom(C×A, B) ≅ Hom(C, B^A)   [currying in the category]
  3. Subobject classifier Ω:
     Sub(A) ≅ Hom(A, Ω) for all A.
     In Set: Ω = {0,1} = Bool; Hom(A,{0,1}) = characteristic functions = subsets.
     In a general topos: Ω is the "truth value object."
```

**Examples of toposes**:
- **Set**: the prototypical topos. Ω = {⊤,⊥}.
- **Sh(X)** (sheaves on topological space X): Ω = "open set" sheaf.
- **Fun(G, Set)** (G-sets, G a group): Ω = power set of G (orbits).
- **sSet** (simplicial sets): abstract model for homotopy theory.

**Internal logic**: Every topos has an internal intuitionistic higher-order logic. The law of excluded middle (P ∨ ¬P) holds only in Boolean toposes (like Set). Constructive mathematics is "internal logic of a topos."

---

## 8. Connections to Programming Language Theory

### Curry-Howard-Lambek Correspondence

Three-way correspondence:
```
Logic           Types               Category Theory
──────────────  ───────────────     ──────────────────────────
Proposition     Type                Object
Proof           Program / Term      Morphism (A → B)
Conjunction     Product type A×B    Categorical product
Disjunction     Sum type A+B        Categorical coproduct
Implication     Function type A→B   Internal hom / exponential
True (⊤)        Unit type           Terminal object
False (⊥)       Empty type          Initial object
Universal quant Polymorphic type    End / natural transformation
Existential q   Dependent sum Σ     Coend
Curry (A∧B→C)≡(A→B→C) Curry: (A×B)→C ≅ A→(B→C) × ⊣ →
Modus ponens    Function application Composition with eval
```

**STLC (Simply Typed Lambda Calculus) = Cartesian closed categories**:
- Products for pair types
- Exponentials for function types
- Terminal object for unit type
- Closed monoidal category

**Linear types (Rust's ownership)**: Linear logic / linear type theory = Symmetric monoidal closed categories (not Cartesian). Resources can't be freely copied or discarded. ⊗ (tensor) ≠ × (product): tensor doesn't have diagonal (no copy) or weakening (no discard).

### Functors as Polymorphism

```haskell
class Functor f where
  fmap :: (a -> b) -> f a -> f b
```

A Haskell `Functor` is exactly an endofunctor on the category **Hask** (ignoring ⊥):
- Object map: a ↦ f a (type constructor)
- Morphism map: (a→b) ↦ (f a → f b) (fmap)
- Preserves id: `fmap id = id`
- Preserves composition: `fmap (g.f) = fmap g . fmap f`

**Parametric polymorphism = natural transformation**: A polymorphic function `α :: forall a. F a -> G a` is a natural transformation F ⇒ G. Naturality is automatic by "free theorems" (Wadler's theorems for free — follow from parametricity).

### Coalgebras and Corecursion

```
Algebra:   F(A) → A   (F-algebra, folds / catamorphisms)
Coalgebra: A → F(A)   (F-coalgebra, unfolds / anamorphisms)

For F(X) = 1 + A×X:
  F-algebras = lists (fold from base case + cons)
  F-coalgebras = streams / infinite lists (unfold: produce head + tail)

Initial algebra: least fixed point μX.F(X) — inductive types (Natural numbers, List, Tree)
Final coalgebra: greatest fixed point νX.F(X) — coinductive types (Stream, infinite Tree)

Bisimulation = equality for coalgebras.
```

---

## 9. Category Theory in Practice

### Where It Shows Up

| Domain | CT concept | Concrete instance |
|--------|-----------|-------------------|
| Haskell | Functor, Monad, Applicative | Type classes, do-notation |
| Rust | Monad (Result chaining with ?) | Error propagation without exceptions |
| Database | Functors | Natural joins as limits; union/intersection as colimits |
| SQL | Colimits | UNION as coproduct, JOIN as pullback |
| Git | Colimit / pushout | Three-way merge = pushout in category of file trees |
| Type inference | Adjunction | Hindley-Milner: generalize ⊣ instantiate |
| Compiler IRs | Functor | Map over AST nodes |
| Recursion schemes | Initial algebras | Catamorphism = fold, anamorphism = unfold |
| Optics (Haskell lens) | Profunctor | Lens = profunctor in specific (Cartesian) profunctor |
| Dependent types | Fibration | Type families as fibered categories |

### Monoid = One-Object Category (Recall)

Every monoid M is a one-object category where morphisms are elements and composition is the monoid operation. A monoid homomorphism is a functor between one-object categories.

This is why "monoid" appears so pervasively — it is the minimal algebraic structure a category can have.

### Applicative Functors (between Functor and Monad)

```haskell
class Functor f => Applicative f where
  pure  :: a -> f a
  (<*>) :: f (a -> b) -> f a -> f b
```

CT interpretation: Applicative = lax monoidal functor (F, φ, ι) where:
- φ_{A,B}: F(A) ⊗ F(B) → F(A ⊗ B)  [lax monoidal structure]
- ι: I → F(I)                         [unit preservation]

Every Monad is Applicative; every Applicative is a Functor. Applicative captures "context-independent effects" — the structure of effects is fixed by the applicative, not the values.

---

## Decision Cheat Sheet

```
Question:                                    Tool:
────────────────────────────────────────     ──────────────────────────────────────────
Are two constructions "the same"?           Find a natural isomorphism between them
Is a construction canonical/natural?        Check if it's a natural transformation
What does a functor preserve?               Check if properties are stated categorically
Does F preserve products/coproducts?       Check if F is left/right adjoint
Is there a "best" map into/out of X?        Universal property (limit/colimit)
Curry (A×B→C) = (A→B→C)?                   × ⊣ → adjunction (Cartesian closed category)
Effect in a pure type system?               Monad
Combine effects?                            Monad transformer stack or free monad
Inductive type / fold?                      Initial F-algebra, catamorphism
Coinductive type / unfold?                  Final F-coalgebra, anamorphism
Parametrically polymorphic function?       Natural transformation (free theorem)
Linear resource types?                      Symmetric monoidal closed category (not CCC)
```

---

## Common Confusion Points

**Category theory is not just abstract nonsense**: It identifies which properties are "the right" properties to have — precisely those characterizable by universal properties. Two objects satisfying the same universal property are isomorphic. This gives structure-independent proofs.

**Natural transformations are not just "compatible families"**: The naturality square must commute for every morphism in the source category, not just objects. This is what makes naturality strong enough to derive free theorems.

**Functor ≠ parametric polymorphism in full generality**: In Haskell, `fmap` must satisfy functor laws. The compiler doesn't enforce them (only equational reasoning / QuickCheck). In proof assistants (Coq, Agda), the laws are part of the type.

**Adjunction is not symmetric**: F ⊣ G ≠ G ⊣ F (the latter would require G ⊣ F, which is a different pair). Adjoints are unique up to natural isomorphism: if F ⊣ G and F ⊣ G', then G ≅ G' naturally.

**Monad ≠ "a monad in Haskell"**: Haskell's Monad class is a convenient encoding of the mathematical monad. The mathematical concept is about endofunctors with unit and multiplication satisfying laws. Haskell's `IO` monad captures side effects; in the math it just encodes the sequencing structure.

**Initial vs terminal algebras**: Initial F-algebra (μX.FX) gives inductive types (natural numbers, finite lists). Final F-coalgebra (νX.FX) gives coinductive types (streams, infinite trees). They're categorically dual; which you want depends on whether you're building from base cases or generating infinite data.

**Yoneda lemma insight**: The lemma says you can "probe" objects by mapping other objects into them. Two objects A, B are isomorphic iff they respond identically to all probes — this is how universal properties characterize objects up to unique isomorphism.
