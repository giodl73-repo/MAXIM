# Type Theory: STLC, System F, Hindley-Milner, Subtyping

## The Big Picture

Type theory is lambda calculus + types. The progression STLC → System F → Hindley-Milner → System Fω → subtyping covers all the type systems you encounter in production languages. The key engineering question is always the same: what can be inferred automatically vs. what requires annotation?

```
+--------------------------------------------------------------------------+
|                    TYPE THEORY LANDSCAPE                                 |
+--------------------------------------------------------------------------+
|                                                                          |
|  EXPRESSIVENESS vs. INFERABILITY TRADEOFF:                              |
|                                                                          |
|  STLC          System F       HM          System Fω    Dependent         |
|  (simple       (universal     (let-poly   (higher-     types             |
|   types)        quant.)        subset      kinded)      Coq/Agda)        |
|    │               │             │            │              │           |
|    ▼               ▼             ▼            ▼              ▼           |
|  Fully         Type inf.      Fully        Inf. for       Undecidable   |
|  inferrable    undecidable    inferrable   monomorphic    in general    |
|               (Boehm 1985)   (Algorithm W) let; annot     (need         |
|                               O(n·α(n))    for rank-2+    termination   |
|                                                           checker)       |
|                                                                          |
|  PRODUCTION LANGUAGE MAPPING:                                            |
|  Haskell/OCaml/F#: HM core + extensions (rank-n with annotation)       |
|  Rust: HM-based (inferred within functions, explicit at signatures)     |
|  Java/C#: bounded polymorphism (F<: variant)                            |
|  TypeScript: structural subtyping + unsound covariance                  |
|  Scala: local type inference + subtyping + variance                     |
+--------------------------------------------------------------------------+
```

---

## 1. Simply Typed Lambda Calculus (STLC)

**Syntax**:
```
Types:  τ ::= B | τ → τ     (base types, function types)
Terms:  t ::= x | λx:τ.t | t t

Typing context: Γ = {x₁:τ₁, ..., xₙ:τₙ}

TYPING RULES:

  Γ, x:τ ⊢ x : τ                      (T-Var)

  Γ, x:τ₁ ⊢ t : τ₂
  ─────────────────────                 (T-Abs)
  Γ ⊢ λx:τ₁.t : τ₁ → τ₂

  Γ ⊢ t₁ : τ₁ → τ₂    Γ ⊢ t₂ : τ₁
  ─────────────────────────────────     (T-App)
  Γ ⊢ t₁ t₂ : τ₂
```

**The key theorems**:
```
PROGRESS: If ⊢ t : τ then either t is a value or ∃t' : t → t'
          (well-typed programs don't get stuck)

PRESERVATION: If ⊢ t : τ and t → t' then ⊢ t' : τ
              (types are preserved under reduction)

Together: TYPE SAFETY — well-typed programs either run forever
          or produce a value of the right type.
          "Well-typed programs can't go wrong" (Milner)
```

**STLC limitations**: Every term is strongly normalizing — STLC cannot express non-terminating programs. The Y combinator is untypable in STLC. This makes STLC total (every term terminates) but not Turing-complete in the operational sense.

---

## 2. System F: Universal Polymorphism

Girard (1971, logic context) and Reynolds (1974, programming context) independently discovered System F:

```
SYSTEM F SYNTAX:

Types:  τ ::= α | τ → τ | ∀α.τ
Terms:  t ::= x | λx:τ.t | t t | Λα.t | t[τ]

                              ↑           ↑
                         type abstraction  type application

EXAMPLE — polymorphic identity:

  id : ∀α. α → α
  id = Λα. λx:α. x

  id [Int] 42 : Int      (instantiate α := Int)
  id [Bool] true : Bool  (instantiate α := Bool)

EXAMPLE — polymorphic composition:

  compose : ∀α. ∀β. ∀γ. (β → γ) → (α → β) → (α → γ)
  compose = Λα. Λβ. Λγ. λf:β→γ. λg:α→β. λx:α. f (g x)
```

**Impredicativity of System F**: In ∀α.τ, α ranges over all types, including ∀α.τ itself. This is impredicative — the quantifier binds over a universe including itself. This is what makes type inference for full System F undecidable (Boehm 1985, Wells 1999).

```
IMPREDICATIVITY EXAMPLE:

  id : ∀α. α → α can be instantiated at:
  id [∀α. α → α] id : (∀α. α → α) → (∀α. α → α)

  The type ∀α. α → α is a valid instantiation for α itself.
  This self-reference makes inference undecidable.

  Contrast predicative polymorphism (ML/HM):
  The quantifier in let bindings ranges only over monotypes
  → Inference decidable (this is Milner's restriction)
```

**Parametricity (Reynolds 1983)**: Any closed term of type ∀α. τ[α] must be "parametrically polymorphic" — it cannot inspect the type α. From the type alone you can deduce the behavior:

```
PARAMETRICITY (FREE THEOREMS):

  f : ∀α. [α] → [α]         (list to list)
  → f must return a permutation/sublist of input
    (can't create elements of unknown type α)

  f : ∀α. α → α
  → f = id  (the only function of this type)

  f : ∀α. ∀β. (α → β) → [α] → [β]
  → f = map  (the only sensible function of this type)

  Wadler's "Theorems for free!" (1989):
  Types give you theorems about programs for free — no proofs needed.
```

---

## 3. Hindley-Milner: The Engineering Sweet Spot

HM (Hindley 1969 independently; Milner 1978 for ML) is the subsystem of System F that admits complete type inference:

**The key restriction — let-polymorphism**:
```
HM SYNTAX (types):

  Monotype: τ ::= α | τ → τ | T τ₁...τₙ   (no ∀ inside)
  Polytype: σ ::= ∀α₁...αₙ.τ               (∀ only at top level)

  CRITICAL: ∀ never appears nested inside a monotype
  This is the predicativity restriction.

HM TERM SYNTAX:

  t ::= x | λx.t | t t | let x = t₁ in t₂

  λ-abstraction: monomorphic (x has one type in scope of λ)
  let-binding: polymorphic (x can be instantiated differently)

HM TYPING:

  Generalization (at let):
    If Γ ⊢ t₁ : τ and α₁...αₙ ∉ FV(Γ)
    Then Γ, x:∀α₁...αₙ.τ ⊢ let x=t₁ in t₂

  Instantiation:
    If Γ ⊢ t : ∀α.τ
    Then Γ ⊢ t : τ[τ'/α] for any monotype τ'

EXAMPLE:

  let id = λx.x in
    (id 42, id true)

  id gets type: ∀α. α → α   (generalized at let-binding)
  id 42:   instantiate α := Int  → Int
  id true: instantiate α := Bool → Bool
  Result:  (Int, Bool)

  If id were under λ (not let), it would be monomorphic!
  λf. (f 42, f true)  ← TYPECHECKING FAILS in HM
                         f must have a single type in λ scope
```

**Algorithm W** (Milner 1978; Damas-Milner 1982):
```
ALGORITHM W (outline):

  W(Γ, x):        Look up x in Γ, instantiate fresh type variables
  W(Γ, λx.t):     Fresh α for x; W(Γ,x:α, t) = (S, τ); return (S, Sα → τ)
  W(Γ, t₁ t₂):   W(Γ, t₁) = (S₁, τ₁)
                  W(S₁Γ, t₂) = (S₂, τ₂)
                  Fresh β; unify(S₂τ₁, τ₂ → β) = S₃
                  Return (S₃∘S₂∘S₁, S₃β)
  W(Γ, let x=t₁ in t₂):
                  W(Γ, t₁) = (S₁, τ₁)
                  σ = generalize(S₁Γ, τ₁)   ← generalize free vars
                  W(S₁Γ, x:σ, t₂) = (S₂, τ₂)
                  Return (S₂∘S₁, τ₂)

  UNIFICATION: Robinson unification
  Complexity: O(n · α(n)) where α is inverse Ackermann — near-linear

  RESULT: Principal type theorem — W finds the most general type,
          or fails (type error)
```

**HM limits in practice**:
```
WHERE HM NEEDS ANNOTATIONS:

1. Rank-2 polymorphism:
   runST :: (∀s. ST s a) → a
   The ∀s is inside the argument type position — HM can't infer this
   (forall quantifier inside → position of function type)
   Needs: explicit annotation in Haskell

2. Impredicative instantiation:
   id id :: (a → a) → (a → a)   ← inferring id's type as (∀a.a→a)→... fails in HM
   GHC needs ImpredicativeTypes extension, still limited

3. GADTs (generalized algebraic data types):
   Type equalities in patterns require type annotations
   (requires OutsideIn(X) algorithm extension, not pure HM)

4. Higher-rank polymorphism generally:
   GHC's RankNTypes extension: allows rank-n but requires annotations
```

---

## 4. System Fω: Higher-Kinded Types

System Fω extends System F with **type constructors** — functions over types:

```
KINDS:
  κ ::= * | κ → κ

  * = kind of proper types (Int, Bool, Maybe Int)
  * → * = kind of type constructors (Maybe, List, IO)
  * → * → * = binary type constructors (Either, Map)

KIND CHECKING:
  Int : *
  Maybe : * → *
  Maybe Int : *      (apply * → * to * → *)
  Either : * → * → *
  Either String Int : *

SYSTEM Fω:
  Allows abstraction over type constructors
  ΛF:*→*. λxs : F Int. ...   ← abstract over type constructor F

PRODUCTION: HASKELL'S HIGHER-KINDED TYPES:

  class Functor f where           -- f : * → *
    fmap :: (a → b) → f a → f b

  class (Functor f) => Applicative f where
    pure :: a → f a
    (<*>) :: f (a → b) → f a → f b

  class (Applicative m) => Monad m where
    (>>=) :: m a → (a → m b) → m b

  f, m are higher-kinded type variables of kind * → *
  HM alone cannot express these (HM has kind * only)
  System Fω is needed to type these typeclass definitions

SCALA KIND PROJECTOR:
  F[_] in Scala = Haskell's f : * → *
  EitherT[IO, _, _] type aliases = kind * → * → *
  cats/scalaz heavily use this
```

---

## 5. Subtyping

Subtyping adds a partial order on types with the **subsumption** rule:

```
SUBTYPING RULE:
  Γ ⊢ t : τ₁    τ₁ <: τ₂
  ─────────────────────────    (T-Sub / Subsumption)
  Γ ⊢ t : τ₂

  τ₁ <: τ₂ means: "τ₁ is a subtype of τ₂"
  = any value of type τ₁ can safely be used where τ₂ is expected

WIDTH subtyping for records:
  {x:Int, y:Bool} <: {x:Int}    (more fields ≤ fewer fields)
  Objects with more methods are subtypes of objects with fewer

Depth subtyping (when is covariance safe?):
  {x: τ₁} <: {x: τ₂} if τ₁ <: τ₂   ← only safe for READ-ONLY fields
```

**Variance — the fundamental question**:
```
VARIANCE OF F[−] WRT SUBTYPING:

  COVARIANT:     A <: B → F[A] <: F[B]    (same direction)
  CONTRAVARIANT: A <: B → F[B] <: F[A]    (reversed)
  INVARIANT:     neither in general

FUNCTION ARROW IS CONTRAVARIANT IN ARGUMENT, COVARIANT IN RESULT:

  τ₁ → τ₂  <:  σ₁ → σ₂
  iff σ₁ <: τ₁  (argument: contravariant — σ₁ is more general)
   AND τ₂ <: σ₂ (result: covariant — τ₂ is more specific)

  INTUITION:
    If f : Animal → String
    Then f is also usable as Cat → String  (Cat <: Animal)
    (f can handle anything f can handle + more; so if you give it a Cat, fine)
    Contravariance: argument type gets WIDER when subtype

    If g : Cat → Siamese
    Then g is also usable as Cat → Animal  (Siamese <: Animal)
    Covariance: return type gets NARROWER when subtype

JAVA'S UNSOUND COVARIANT ARRAYS:
  Java: String[] <: Object[]   (covariant)
  This is UNSOUND:
    Object[] arr = new String[10];  // compiles (covariant)
    arr[0] = 42;                    // compiles (Object fits in Object[])
    // Runtime: ArrayStoreException (42 is not a String)
    // The type system LIED — requires runtime check

KOTLIN'S SOLUTION: declaration-site variance
  Array<T> is invariant (no implicit subtyping between arrays)
  List<out T> is covariant (read-only, so safe)
  Consumer<in T> is contravariant (write-only, so safe)
  in/out keywords = explicit variance annotation
```

---

## 6. Bounded Polymorphism: F<:

System F with subtyping (Cardelli, Wegner 1985; Pierce, Turner 1994):

```
F<: SYNTAX:

Types:  τ ::= α | τ → τ | ∀α<:τ.τ | {l:τ,...}
             (bounded quantification)

  ∀α<:Animal.α → α
  = polymorphic function over any subtype of Animal

  JAVA/KOTLIN/SCALA/TYPESCRIPT EQUIVALENT:
  <T extends Animal> T identity(T x) { return x; }  // Java
  fun <T : Animal> identity(x: T): T = x             // Kotlin

PIERCE SCRAP: F<: was expected to model object-oriented subtyping.
  But bounded polymorphism is UNDECIDABLE in its full form (Pierce-Turner 1994)
  → all mainstream languages use BOUNDED POLYMORPHISM with restrictions
  → Java uses nominal F<: (not structural); TypeScript uses structural
```

---

## 7. TypeScript: Structural Subtyping and Its Unsoundness

TypeScript is an industrial example of a deliberately unsound type system:

```
STRUCTURAL SUBTYPING IN TYPESCRIPT:
  { x: number, y: number } <: { x: number }   (width subtyping: more fields)
  No nominal class hierarchy needed for subtyping
  DUCK TYPING made static: if it has the right fields, it's compatible

KNOWN UNSOUNDNESS HOLES (by design):

1. COVARIANT METHOD PARAMETERS:
   TypeScript class methods: parameters are covariant (not contravariant)
   class Animal { makeSound(a: Animal): void }
   class Cat extends Animal { makeSound(c: Cat): void }
   Cat.makeSound <: Animal.makeSound in TypeScript's system
   (Correct: Cat.makeSound should be contravariant in argument = NOT a subtype)
   This is unsound. TypeScript chose soundness for usability.

2. TYPE ASSERTIONS (as):
   x as string  ← no runtime check; just type annotation
   Any type can be asserted to any other via as unknown as T

3. any TYPE:
   Explicit escape hatch; defeats all type checking
   unknown is the sound alternative (must narrow before use)

4. COVARIANT GENERICS BY DEFAULT:
   Array<string> <: Array<unknown> in TypeScript
   (arrays are covariant; only safe for read-only use)

5. FUNCTION RETURN TYPE COVARIANCE:
   Correct — TypeScript gets this right

TYPESCRIPT TEAM'S EXPLICIT TRADEOFF:
  "TypeScript is not trying to be maximally sound.
   It is trying to be practical and catch most bugs."
  Unsoundness is documented: https://github.com/microsoft/TypeScript/wiki/TypeScript-Design-Goals
```

---

## Decision Cheat Sheet

| Type system | Inference | Expressiveness | Production use |
|-------------|-----------|----------------|----------------|
| STLC | Fully inferrable | No recursion | Foundation only |
| System F | Undecidable | Full polymorphism | Haskell Core internally |
| HM | Complete (Algorithm W) | Let-polymorphism | Haskell, OCaml, F#, Rust |
| System Fω | Inferrable for mono | Higher-kinded types | Haskell kind system |
| F<: (bounded) | Decidable subsets | Subtyping + generics | Java, Kotlin, C# |
| Structural subtyping | Local inference | Structural compatibility | TypeScript, Go (interfaces) |
| Dependent types | Undecidable | Express any property | Coq, Agda, Lean |

---

## Common Confusion Points

**HM let-polymorphism vs. OCaml value restriction**: In OCaml, generalization happens only for syntactic values (not arbitrary expressions). `let x = ref []` doesn't get polymorphic type — it's monomorphic (the value restriction prevents unsound generalization of mutable references). Haskell doesn't need this because it's pure.

**Rank-1 vs. rank-2+ polymorphism**: HM infers rank-1 polymorphism (∀ only at outermost). Haskell's `runST : ∀s. ST s a → a` is rank-2 because the ∀s is inside an argument type. You can write rank-2 types in GHC with `{-# LANGUAGE RankNTypes #-}` but you must annotate them.

**Java generics are not System F polymorphism**: Java generics use type erasure at runtime (no type passing at runtime). Reified generics (C# at runtime) keep type information. The difference matters for reflection and type witnesses. F<: doesn't specify erasure vs. reification — that's an implementation choice.

**TypeScript's structural subtyping is not the same as Go's implicit interfaces**: TypeScript has explicit type declarations and uses structural compatibility for assignment and function arguments. Go's interface satisfaction is also structural but happens at interface assignment. TypeScript has much richer type operations (intersection, union, conditional types).
