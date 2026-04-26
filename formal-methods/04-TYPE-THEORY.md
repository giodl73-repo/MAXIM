# Type Theory

## The Big Picture

Type theory is the bridge between logic, programming languages, and proof assistants.
You know lambda calculus from MIT — this builds that directly into modern PL practice.

```
+--------------------------------------------------------------------------+
|                          TYPE THEORY HIERARCHY                           |
|                                                                          |
|  SIMPLY TYPED LAMBDA CALCULUS (STLC)                                     |
|  Base types + function types. Strong normalization. No self-application. |
|  No polymorphism. Every term has exactly one type.                       |
+--------------------------------------------------------------------------+
            | add parametric polymorphism
            v
+--------------------------------------------------------------------------+
|  SYSTEM F  (Girard 1971 / Reynolds 1974)                                 |
|  Universal type: ΛX. t  /  forall X. T                                   |
|  Haskell's forall. Rank-2 polymorphism. Parametricity / free theorems.   |
+--------------------------------------------------------------------------+
            | add type constructors
            v
+--------------------------------------------------------------------------+
|  SYSTEM F-omega                                                          |
|  Type-level functions (type constructors). Kind system: * -> * -> *.     |
|  Haskell type classes, higher-kinded types, Functor, Monad.              |
+--------------------------------------------------------------------------+
            | add type-level computation on values
            v
+--------------------------------------------------------------------------+
|  DEPENDENT TYPES (Martin-Lof Type Theory, CIC, Lean 4)                   |
|  Pi type:   (x : A) -> B(x)    -- return type depends on VALUE of arg    |
|  Sigma type: (x : A) × B(x)    -- second component type depends on first |
|  Vector n: Array whose length is IN THE TYPE.                            |
|  Propositions as types. Proofs as programs. Coq, Lean 4, Agda.           |
+--------------------------------------------------------------------------+
            | add paths/higher structure
            v
+--------------------------------------------------------------------------+
|  HOMOTOPY TYPE THEORY (HoTT)                                             |
|  Types as spaces. Paths as equality proofs. Univalence axiom.            |
|  Higher inductive types. Cubical type theory (computational content).    |
|  Agda cubical, Lean 4 (classical, not cubical).                          |
+--------------------------------------------------------------------------+

  INDUSTRIAL IMPLEMENTATIONS:
  STLC:     Every typed language. Java (before generics), C (structs).
  System F: Haskell, Scala, F#, Rust generics, TypeScript generics.
  F-omega:  Haskell (type classes), Scala (implicit parameters).
  Dep. types: Coq, Lean 4, Agda, Idris, F* (crypto verification).
  Affine/linear: Rust ownership + borrow checker.
```

---

## STLC: Simply Typed Lambda Calculus

You know this. The relevant pieces for what follows:

```
  Types: T ::= B | T1 -> T2
  Terms: t ::= x | \x:T.t | t1 t2

  Typing rules:
  Gamma |- x : T          [if x:T in Gamma]
  Gamma, x:T1 |- t : T2   => Gamma |- \x:T1.t : T1 -> T2
  Gamma |- t1 : T1->T2
  Gamma |- t2 : T1         => Gamma |- t1 t2 : T2

  Key properties:
  - Strong normalization: every well-typed term terminates
  - Unique types (up to alpha-equivalence)
  - No self-application: \x. x x is untypable
  - Subject reduction: if t:T and t -> t', then t':T

  The strong normalization property is what makes STLC useless as a
  general-purpose programming language — you cannot write general
  recursion. (That's why languages add fix or mu.)
```

---

## System F: Parametric Polymorphism

Girard (1971, logic — "second-order propositional logic") and Reynolds (1974, PL —
"polymorphic lambda calculus") independently discovered this.

### The Type System

```
  Extend STLC with:
  - Type variable: alpha, beta, ...
  - Universal type: forall alpha. T
  - Type abstraction: \Alpha. t  (introduces type variable)
  - Type application: t [T]  (instantiates type variable)

  Classic example — polymorphic identity:
  id : forall alpha. alpha -> alpha
  id = \Alpha. \x:Alpha. x

  id [Int] 5      -- instantiate at Int, apply to 5
  id [Bool] true  -- instantiate at Bool, apply to true

  Polymorphic composition:
  compose : forall a b c. (b -> c) -> (a -> b) -> (a -> c)
  compose = \A. \B. \C. \f:B->C. \g:A->B. \x:A. f (g x)
```

### Parametricity and Free Theorems (Reynolds 1983)

The deep result: the polymorphic type of a function DETERMINES its behavior.
If you don't know the type, you cannot do type-specific things to it.

```
  Free theorem for id : forall a. a -> a:
  For any function f : A -> B:
    f . id[A] = id[B] . f
  In words: "id does nothing" — no matter what function f you apply,
  it commutes through the identity.

  Free theorem for map : forall a b. (a -> b) -> [a] -> [b]:
  For any function f : A -> B and g : B -> C:
    map (g . f) = map g . map f
  This is the functor law — it follows FOR FREE from the type.

  Why this matters for verification:
  You get theorems about code FOR FREE, just from the types.
  No proof needed — it follows from parametricity.
  This is "free theorems" (Wadler 1989).
```

### Rank-n Polymorphism

```
  Rank-1 (HM polymorphism): type variables only at the outermost level.
  forall a. a -> a -> a

  Rank-2: type variables can appear under one ->
  (forall a. a -> a) -> Int -> Int

  Rank-n: type variables can appear under n levels of ->

  Haskell default: Rank-1 (Hindley-Milner inference).
  Haskell with RankNTypes extension: Rank-2 and higher.
  Full System F: all ranks. Type inference is UNDECIDABLE for Rank-3+.

  F# / OCaml: Rank-1 only (HM inference, decidable).
  Coq/Lean 4: all ranks (but require explicit type annotations for rank-2+).
```

### Impredicativity

```
  System F is IMPREDICATIVE: you can instantiate forall a. T[a]
  with types that themselves contain forall.

  forall a. a -> a -> a    can be instantiated with
  a = (forall b. b -> b)   to get
  (forall b. b -> b) -> (forall b. b -> b) -> (forall b. b -> b)

  This is powerful but creates complications:
  - Type inference with impredicativity is undecidable in general
  - Rust generics: predicative (cannot instantiate with forall types directly)
  - Haskell: controlled impredicativity (ImpredicativeTypes extension)
  - Coq's Prop: impredicative (necessary for logic — forall X:Prop. phi[X])
  - Coq's Set/Type: predicative (to avoid Girard's paradox)
```

---

## System F-omega: Higher-Kinded Types

F-omega adds type constructors — functions at the type level.

### Kind System

```
  Kinds classify types:
  * (pronounced "star") = kind of proper types (Int, Bool, String -> Int)
  * -> * = kind of type constructors (Maybe, List, IO)
  (* -> *) -> * = kind of type constructor consumers
  (* -> * -> *) = kind of binary type constructors (Either, Map, Arrow)

  Examples:
  Int    : *          (a proper type)
  Maybe  : * -> *     (takes a type, gives a type)
  Either : * -> * -> * (takes two types, gives a type)
  Functor: (* -> *) -> Constraint  (in Haskell — a type class over * -> *)

  Type-level computation (Haskell type families):
  type family Elem (c :: * -> *) :: *
  type instance Elem [] = a           -- Elem [a] = a
  type instance Elem (Map k) = v      -- Elem (Map k v) = v
```

### Type Classes as F-omega Dictionaries

```
  Haskell type class:
  class Functor f where
    fmap :: (a -> b) -> f a -> f b

  Compiles to:
  data FunctorDict f = FunctorDict { fmap :: forall a b. (a->b) -> f a -> f b }

  Constraint:  Functor f  ==  implicit FunctorDict f argument passed around
  The type checker infers and inserts dictionary passing automatically.

  F# equivalent: inline functions with ^T static constraints.
  Rust equivalent: trait objects or generic bounds (monomorphization or vtable).
```

---

## Dependent Types

The big leap: types can now DEPEND on VALUES.

### Pi Types (Dependent Function Types)

```
  Non-dependent: A -> B   (return type is always B, regardless of input)
  Dependent:    (x : A) -> B(x)   (return type can VARY based on input VALUE)

  Example: a function that returns a list of length n
  replicate : (n : Nat) -> a -> Vector a n
  replicate 3 'x'  : Vector Char 3   -- type says length is 3
  replicate 5 'x'  : Vector Char 5   -- type says length is 5

  If you call:  head (replicate 0 'x')  -- head of empty vector
  This is a TYPE ERROR -- not a runtime error.
  The type Vector Char 0 does not match the requirement (n+1).

  Matrix multiplication:
  matMul : Matrix m n -> Matrix n p -> Matrix m p
  -- Dimension mismatch is a compile-time type error.
  -- The compiler KNOWS the dimensions.

  Why this matters for verification:
  Many runtime errors become compile-time type errors.
  Buffer overflows: impossible if the type says the vector has length n
  and all accesses are in-bounds (provable from the type).
```

### Sigma Types (Dependent Pair Types)

```
  Non-dependent pair: A × B   (both components have fixed types)
  Dependent pair:    (x : A) × B(x)   (second type depends on first value)

  Example: a list together with a proof it is sorted
  SortedList = (l : List Int) × Sorted l

  fst : SortedList -> List Int       -- extract the list
  snd : (p : SortedList) -> Sorted (fst p)  -- extract the proof

  Example: a natural number together with its bound
  BoundedNat (n : Nat) = (k : Nat) × (k < n)

  Sigma types represent:
  - Existential statements: ∃x:A. B(x)   (witness + proof)
  - Subtypes: {x : A | B(x)}  (elements of A satisfying B)
  - Refined types: similar to F*'s refinement types
```

### Martin-Lof Type Theory (MLTT)

```
  MLTT (1975, Per Martin-Lof): the standard dependent type theory.
  Four key type formers (each with formation, introduction, elimination, computation):

  1. Pi types (universal):     (x : A) -> B(x)
     Intro: lambda abstraction  \x. t
     Elim:  function application t u
     Computation: beta reduction (\x. t) u = t[u/x]

  2. Sigma types (existential): (x : A) × B(x)
     Intro: pair  (a, b)  where b : B(a)
     Elim:  projections fst, snd (or dependent elimination)
     Computation: fst (a,b) = a, snd (a,b) = b

  3. Identity type:  Id_A(a, b)  (or a =_A b)
     Intro: refl : Id_A(a, a)  (a is equal to itself)
     Elim:  J rule (path induction -- if it holds for refl, it holds for all paths)
     This is where HoTT gets interesting.

  4. Inductive types (W-types in MLTT, generalized inductives in CIC):
     Nat, List, Tree, etc.
     Intro: constructors
     Elim:  recursors / eliminators

  Universes: Type_0 : Type_1 : Type_2 : ...  (stratified to prevent paradox)
```

---

## HoTT: Homotopy Type Theory

HoTT (Homotopy Type Theory, Univalent Foundations Program, 2013) reinterprets MLTT
through the lens of algebraic topology.

### The Core Insight

```
  In MLTT: a proof of a = b (identity type) is a path from a to b.
  In HoTT: take this LITERALLY.

  Types as spaces:      elements as points.
  Equality proofs (a = b) as paths between points.
  Proofs of equality of paths (p = q) as homotopies between paths.
  And so on, up to arbitrary dimensions.

  Old view: "a = b has a unique proof (refl)"
            (proof-irrelevance for propositional equality)
  HoTT view: "there can be MULTIPLE distinct proofs of a = b"
             (they are paths, and paths can be different)

  Why this matters:
  In MLTT, you cannot distinguish a = b from refl (they're "the same proof").
  In HoTT, you can have non-trivial paths (homotopies, fibrations).
  This enables: circles, spheres, and other spaces as types.
```

### Univalence Axiom (Voevodsky)

```
  (A ≃ B) ≃ (A = B)

  "Equivalent types are equal."

  Equivalence: A ≃ B means there exist f : A -> B and g : B -> A
  such that f . g = id and g . f = id (up to homotopy).

  Consequence: isomorphic mathematical structures are EQUAL.
  In Lean 4 / Coq without univalence: two isomorphic groups
  are related but not definitionally equal. Theorems about
  one group must be manually transferred to the other.
  With univalence: proving A ≃ B lets you immediately reuse
  ALL theorems about A for B.

  This is why Mathlib cares about univalence — it enables
  massive reuse across isomorphic structures.

  Computational content: classical HoTT (Lean 4, Coq + HoTT library)
  uses univalence as an axiom (no computational reduction rule).
  Cubical type theory (Agda cubical, Cubical Lean) gives
  univalence computational content — you can run HoTT programs.
```

---

## Hindley-Milner: Type Inference for Polymorphism

The type inference algorithm underlying OCaml, F#, Haskell, and Rust's core:

```
  Problem: Given an untyped expression, infer its most general type.

  Algorithm W (Damas-Milner, 1982):
  1. Assign fresh type variables to unknowns
  2. Generate constraints from the expression structure
  3. Solve constraints via unification
  4. Generalize free type variables (let-polymorphism)

  Example:
  let id = \x -> x
  -- Step 1: assign x : alpha (fresh variable)
  -- Step 2: body x has type alpha, lambda has type alpha -> alpha
  -- Step 4: generalize alpha to get: id : forall a. a -> a

  let compose = \f -> \g -> \x -> f (g x)
  -- Results in: forall a b c. (b -> c) -> (a -> b) -> (a -> c)

  Key limitation: let-polymorphism
  id = \x -> x             -- polymorphic: forall a. a -> a
  f = \id -> (id 1, id 'a') -- this FAILS in HM
  -- Because id inside f must have ONE concrete type in HM

  This is why GHC needs RankNTypes for certain patterns,
  and why you sometimes need explicit type annotations in F#/OCaml.

  Completeness: Algorithm W always finds the MOST GENERAL type.
  If a type exists, W finds it. (For rank-1 polymorphism.)
  Decidability: inference is decidable for rank-1, undecidable for rank-3+.
```

---

## Rust: Affine Types and Ownership

Rust's ownership system is a practical implementation of affine/linear type theory.

```
  Linear type system: every value must be used EXACTLY ONCE.
  Affine type system: every value must be used AT MOST ONCE.
  Rust uses affine types (you can drop without using).

  The ownership rules:
  - Each value has exactly one owner at a time
  - When the owner goes out of scope, the value is dropped
  - You can MOVE a value (transfer ownership — old binding invalid)
  - You can BORROW a value (temporary reference — original still valid)
    - Shared borrow (&T): multiple simultaneous readers
    - Exclusive borrow (&mut T): single writer, no simultaneous readers

  Type-theoretically:
  move = consuming the value (use the linear variable)
  borrow = substructural permission (can use without consuming)
  lifetime 'a = region variable (from region-based memory management)

  The borrow checker IS a type soundness checker:
  let x = vec![1, 2, 3];
  let r = &x;        // shared borrow: type of r is &'a Vec<i32>
  drop(x);           // ERROR: cannot move x while r borrows it
  println!("{}", r); // would be use-after-free

  This is not a runtime check — it is a COMPILE-TIME TYPE ERROR.
  Soundness of the borrow checker (RustBelt project, 2017):
  Formally verified in Iris/Coq that Rust's type system is sound
  (no undefined behavior in safe Rust).
```

### The Lifetime System

```
  Lifetimes are region variables (from Tofte-Talpin region inference, 1994):

  fn longest<'a>(s1: &'a str, s2: &'a str) -> &'a str {
    if s1.len() > s2.len() { s1 } else { s2 }
  }
  -- 'a says: the returned reference lives as long as BOTH inputs

  Lifetime subtyping: 'a: 'b means 'a outlives 'b (lifetime is at least b).
  Variance: &'a T is covariant in 'a (longer lifetimes are subtypes).
            &'a mut T is invariant in T (Liskov substitution breaks mutability).

  Lifetime inference: the compiler infers most lifetimes via a
  constraint-solving pass (similar to HM unification).
  Explicit annotations needed when inference is ambiguous.
```

---

## TypeScript: Structural Typing at Scale

TypeScript's type system is not just System F — it includes structural subtyping,
conditional types, and type-level computation that reaches Turing completeness.

### Structural Subtyping

```typescript
// Nominal (Java, C#): types are subtypes because they're declared to be.
// Structural (TypeScript): types are subtypes if they have compatible shapes.

interface Point { x: number; y: number; }
interface Point3D { x: number; y: number; z: number; }

function draw(p: Point): void { /* ... */ }
const p3: Point3D = { x: 1, y: 2, z: 3 };
draw(p3);   // OK! Point3D has everything Point requires.
            // No explicit "implements Point" needed.

// This is Liskov substitution built into the type checker:
// a value with MORE fields satisfies a type requiring FEWER fields.
// Point3D <: Point (structural subtyping)
```

### Conditional Types and Type-Level Computation

```typescript
// Conditional types: if/then/else at the type level
type IsArray<T> = T extends any[] ? "yes" : "no";
type Test1 = IsArray<number[]>;  // "yes"
type Test2 = IsArray<string>;    // "no"

// Infer: extract parts of a type pattern
type ReturnType<T> = T extends (...args: any[]) => infer R ? R : never;
type Fn = (x: string) => number;
type R = ReturnType<Fn>;  // number

// Mapped types: transform every property of a type
type Readonly<T> = { readonly [K in keyof T]: T[K] };
type Partial<T>  = { [K in keyof T]?: T[K] };
type Required<T> = { [K in keyof T]-?: T[K] };

// Template literal types:
type EventName<T extends string> = `on${Capitalize<T>}`;
type MouseEvent = EventName<"click">;  // "onClick"
```

### TypeScript Types Are Turing Complete

```
  Type-level Church numerals in TypeScript:
  type Zero = never;
  type Succ<N extends any[]> = [1, ...N];
  type Add<A extends any[], B extends any[]> = [...A, ...B];

  (Proven by multiple people — TypeScript conditional types can
  simulate Turing machines at the type level.)

  Practical implication: type checking can be SLOW for complex types.
  Recursive conditional types can trigger the "type instantiation is
  excessively deep" error (TypeScript's cut-off for infinite recursion).

  This is the price of expressiveness.
```

---

## C# Variance: Covariance and Contravariance

From your C# background — this is F-omega subtyping in practice:

```
  Liskov Substitution: if S <: T, then a value of S can be used where T expected.

  For generic types G<T>:
  Covariance (out):  G<S> <: G<T>  when S <: T
                     Safe for producers (you read values out)
                     IEnumerable<out T>, IReadOnlyList<out T>

  Contravariance (in): G<T> <: G<S>  when S <: T (reversed!)
                       Safe for consumers (you write values in)
                       Action<in T>, IComparer<in T>

  Invariance:          G<S> and G<T> are unrelated even if S <: T
                       Safe for both read and write
                       List<T>, IList<T>

  Why it works:
  IEnumerable<Cat> <: IEnumerable<Animal>  -- cats IS-A animals when reading
  Action<Animal> <: Action<Cat>            -- can process Animals CAN process Cats

  Why List<Cat> ≢ List<Animal>:
  List<Cat> cats = new List<Cat>();
  List<Animal> animals = cats;  // if this were allowed...
  animals.Add(new Dog());       // ...you could add a Dog to a Cat list!
  cats[0].Meow();               // type confusion: runtime crash

  In type theory terms:
  Covariance:     G<->  is covariant in T (G is a functor in T)
  Contravariance: G<->  is contravariant in T
  Invariance:     G<->  is invariant in T (both read and write paths)
```

---

## Decision Cheat Sheet

| I want to... | Type system / Tool |
|---|---|
| Polymorphic functions, type inference | HM / System F (Haskell, F#, OCaml, Rust) |
| Higher-kinded abstractions (Functor, Monad) | System F-omega (Haskell, Scala) |
| Encode array lengths or matrix dims in types | Dependent types (Lean 4, Idris, F*) |
| Prevent use-after-free at compile time | Affine types / Rust ownership |
| Flexible structural subtyping | TypeScript structural types |
| Type-level if/else on type structure | TypeScript conditional types |
| Verify security properties of programs | F* (refinement types + Z3) or Coq |
| Prove type system soundness | Coq or Lean 4 (RustBelt uses Iris/Coq) |
| Represent equivalence of structures | HoTT / univalence (Lean 4 + Mathlib) |
| Understand read/write variance in C# generics | Covariance/contravariance annotations |

---

## Common Confusion Points

**"Dependent types are just fancier generics"**

Generics parameterize types over other types (System F). Dependent types parameterize
types over VALUES. The difference: `Vector<T>` (generic) vs `Vector<T, n>` where `n`
is a runtime value whose type-level inclusion makes bounds-checking a type error.

**"HoTT is impractical / academic"**

HoTT's univalence is now in Lean 4 (via classical logic). Mathlib uses it pervasively.
The isomorphism-transport pattern ("move a theorem about A to an isomorphic B") is
enormously useful in formalized mathematics, where you constantly deal with multiple
representations of the same structure.

**"Rust's borrow checker is ad-hoc / heuristic"**

It is a type system. The rules (ownership, borrowing, lifetimes) correspond precisely
to an affine/linear type theory with region variables. The RustBelt project (Jung et al.,
2017) proved the type system sound in Coq — "well-typed Rust programs do not have
undefined behavior." It is not heuristic.

**"TypeScript's any type breaks the type system"**

Yes. `any` disables type checking for that value. It is an escape hatch, not a feature.
`unknown` is the safe version: it requires explicit type narrowing before use.
`never` is the empty type (no values inhabit it) — the logical false.

**"HM inference always works, just don't annotate"**

HM inference is incomplete for rank-2 and higher polymorphism. Functions like
`runST` in Haskell require explicit rank-2 annotations. F# sometimes requires
annotations where OCaml would not (value restriction differences).
Lean 4 and Coq require annotations wherever inference is ambiguous or undecidable.
