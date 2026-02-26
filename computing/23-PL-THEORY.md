# 23 — Programming Language Theory in Modern Systems

## The Frame

The theory lives in the textbooks. This guide maps it to the production languages you interact with and the design decisions embedded in their type systems. Lambda calculus, the Curry-Howard correspondence, Hindley-Milner, subtyping, linear types — all of it is assumed known. The question is: where does it appear, what does it explain, and what does it predict?

```
TYPE SYSTEM EXPRESSIVENESS LATTICE
====================================

  More expressive →→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→
  Less decidable →→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→→

  STLC ──→ HM ──→ System F ──→ Fω ──→ CoC ──→ MLTT
    │         │        │          │       │       │
    │         │        │          │       │       └─ Lean 4, Agda
    │         │        │          │       └───────── Coq, Agda
    │         │        │          └───────────────── Haskell + TypeFamilies
    │         │        └──────────────────────────── Haskell + RankNTypes
    │         │                                       GHC Core (System F + coercions)
    │         └────────────────────────────────────── OCaml, Haskell, F#, Elm
    └──────────────────────────────────────────────── toy languages

  Level       You gain                  You lose              Production language
  ──────────  ────────────────────────  ────────────────────  ──────────────────
  STLC        Base types + A → B        Polymorphism          (toy)
  HM          Let-polymorphism          —                     OCaml, F#, Haskell core
              Complete inference
  System F    Rank-n polymorphism       Type inference        Haskell (RankNTypes)
              Explicit ∀               decidability          GHC Core IR
  Fω          Type operators            —                     Haskell (TypeFamilies)
              Type-level functions                            Scala 3 type lambdas
  CoC         Dependent products        Decidable             Coq, Agda
              Proofs are programs       typechecking in
                                        general
  MLTT        Proof-relevant types      Normalization         Lean 4, Agda
              Univalence (HoTT)         decidability in
                                        full generality

  GHC extension → type system level:
    {-# LANGUAGE RankNTypes #-}      → System F (rank-2+ polymorphism)
    {-# LANGUAGE TypeFamilies #-}    → Fω (type-level functions)
    {-# LANGUAGE DataKinds #-}       → limited dependent types (kind-level data)
    {-# LANGUAGE GADTs #-}           → bounded System Fω
    {-# LANGUAGE TypeInType #-}      → kinds are types (approaching CoC)

  Why GHC Core is System F with coercions, not Fω:
    GHC Core uses explicit coercions (type-equality witnesses) rather than
    type-level functions to handle GADTs and newtypes. A GADT pattern match
    produces a coercion proof that two types are equal; the coercion is
    erased at runtime but must be justified in Core. This keeps GHC Core
    in the decidable fragment while still handling GADTs expressively.
    Coercions also enable zero-cost newtype wrapping/unwrapping.
```

---

## Lambda Calculus as a Substrate

You know the lambda calculus. The production relevance: every language with first-class functions is, at some level of abstraction, lambda calculus with extensions. The design question is which extensions, and which reduction strategy.

### Reduction Strategies in Production

```
Call-by-value (strict evaluation):
  Arguments evaluated before function application
  JavaScript, Python, Rust, C, Java — almost all production languages
  Pro: predictable evaluation order, easy reasoning about side effects
  Con: evaluates arguments even if not used

Call-by-name (lazy, not memoized):
  Arguments substituted unevaluated; evaluated at each use
  Rarely used in production (code expansion, repeated work)
  Haskell's operational model conceptually (but implemented as call-by-need)

Call-by-need (lazy, memoized):
  Like call-by-name but each argument evaluated at most once (thunks)
  Haskell's actual evaluation strategy
  Pro: non-terminating argument to unused parameter = fine
       natural corecursion (infinite data structures)
  Con: space leaks (thunks accumulate), hard to reason about memory

Call-by-push-value (CBPV — Levy 1999):
  Unifies CBV and CBN in one framework
  Values and computations are syntactically distinct
  Emerging in effect system research (Koka, Effekt)
```

### Closures — Implementation Details

A closure is a lambda term paired with its captured environment. The interesting part is how different languages implement that pairing:

**Heap-allocated closure record (V8, most JITs):** A closure is a pair of (function pointer, environment record). The environment record is heap-allocated and holds the captured variables as fields. Capturing N variables = N fields in the record. The GC keeps the record alive as long as the closure is reachable.

**Rust's capture strategy** — determined by usage, not declaration:
- `|x| x + n` where `n` is in scope: the compiler determines whether to capture `n` by shared reference (`&n`) or exclusive reference (`&mut n`) based on how `n` is used inside the closure
- `move |x| x + n`: force-captures `n` by value (moves it into the closure) — the closure owns its environment, which makes it `'static` (can be sent across threads)
- Non-capturing closures (`|x| x + 1`): no environment record — compiled to a plain function pointer, zero allocation

```rust
let n = 5;

// Capturing by reference — closure borrows n
let add_n = |x| x + n;       // type: impl Fn(i32) -> i32
                              // layout: (fn_ptr, &n)

// Capturing by move — closure owns n
let add_n = move |x| x + n;  // type: impl Fn(i32) -> i32
                              // layout: (fn_ptr, n: i32) — n moved in

// Non-capturing — zero-cost, function pointer
let inc = |x: i32| x + 1;   // coerces to fn(i32) -> i32, no allocation
```

The zero-cost claim: a non-capturing Rust closure is identical to a named function at the machine code level. This is why closures as callbacks in Rust don't impose overhead when the captured environment is empty.

---

## The Type Theory Hierarchy

STLC, HM, System F, Fω, CoC, MLTT — you proved these theorems. One line each:

- **STLC**: base types + function arrows, no polymorphism, all terms normalize
- **HM**: adds let-polymorphism with complete inference (Algorithm W); the sweet spot for production languages
- **System F**: explicit ∀, rank-n polymorphism, inference undecidable in general — HM is the rank-1 fragment
- **Fω**: adds type operators (type-level functions), basis for Haskell's kind system
- **CoC**: terms and types unified, dependent products, the λ-cube corner — Coq's core
- **MLTT**: proof-relevant identity types, univalence in HoTT — Lean 4, Agda

GHC extension to type system level mapping is in the landscape diagram above. The key design choice repeated below:

**Why GHC chose System F + coercions over Fω for GHC Core:** Type-level functions (Fω) require type-level beta reduction during type checking, which complicates the metatheory and the implementation. Coercions keep the core calculus simpler — each type equality is an explicit proof term (a coercion) that witnesses the equality at a specific point in the derivation. The cost: GADTs and newtypes generate coercions that must be tracked through the IR. The benefit: GHC Core's metatheory is well-studied and its type checking is decidable.

### Curry-Howard in Production

The correspondence shows up in real systems more than you might expect:

```
Logic                     Type Theory              Production
═════                     ═══════════              ══════════
Proposition P             Type A                   TypeScript: `type P = ...`
Proof of P                Term of type A           A value inhabiting the type
Implication P → Q         Function type A → B      (x: A) => B
Conjunction P ∧ Q         Product type A × B       [A, B] tuple
Disjunction P ∨ Q         Sum type A + B           A | B (union type)
⊥ (falsehood)             Empty type (never)       TypeScript: `never`
¬P (negation)             P → ⊥                    (x: P) => never
Universal ∀x. P(x)        Dependent product Πx. P  <T>(x: T) => ...
Existential ∃x. P(x)      Dependent sum Σx. P      (TS approximation: opaque types)

The TypeScript `never` type is genuinely the empty type —
the type with no inhabitants. A function returning `never` doesn't return.
Exhaustiveness checking in switch statements uses `never`:

  type Shape = Circle | Square;
  function area(s: Shape): number {
    switch (s.kind) {
      case "circle": return ...;
      case "square": return ...;
      default:
        const _exhaustive: never = s;  // type error if Shape gains a new case
        throw new Error("unreachable");
    }
  }
```

---

## Type Inference — Hindley-Milner in Detail

HM is the sweet spot: complete inference + principal types + decidable. Understanding it explains both what TypeScript's inference does and why it sometimes fails.

### Algorithm W

You implemented Algorithm W. The derivation for `f x = x + 1` — assign type variables, generate constraints, unify, generalize — is a standard homework problem. The short version:

```
Unification-based inference summary:
  1. Assign fresh type variables to unknowns
  2. Generate equality constraints from the AST structure
  3. Unify (Robinson unification — most general unifier)
  4. Generalize free variables at let-bindings (let-polymorphism)

Principal type theorem: if a term is typeable, W finds its most general type.
"Most general" = every other valid type is a substitution instance of it.
This is why OCaml/Haskell infer types you didn't write.
```

### Where TypeScript Diverges from HM

TypeScript has HM-style inference but deliberately breaks several HM invariants for JavaScript compatibility:

```
1. No principal types for some expressions:
   const f = (x) => x;  // inferred as (x: unknown) => unknown in some contexts
   HM would give ∀α. α → α
   TS can't always generalize (no rank-1 restriction in same way)

2. Inference is bidirectional, not purely constraint-based:
   TypeScript uses "contextual typing" — the expected type flows inward
   const arr: number[] = [1, 2, 3];  // literal types inferred as number, not 1|2|3
   Without the annotation: [1, 2, 3] inferred as (1 | 2 | 3)[]

3. No let-generalization at the value level:
   TypeScript does generalize generic functions but not every let-binding
   This is deliberate — full HM generalization interacts badly with mutation

4. Subtyping breaks principal types:
   HM assumes no subtyping. TypeScript has structural subtyping.
   These interact in non-trivial ways (variance, conditional types).
   The combination makes TypeScript's type inference incomplete in general.
```

### GHC's Type Inference — OutsideIn(X)

GHC does not use Algorithm W. It uses OutsideIn(X) (Vytiniotis, Peyton Jones, Schrijvers, Sulzmann — ICFP 2011), designed to handle qualified types (type class constraints), GADTs, and multi-parameter type classes — all of which stump pure HM.

The key insight: OutsideIn propagates "wanted" constraints outward rather than doing bottom-up unification.

```
Algorithm W (HM):
  Bottom-up: generate constraints at each node, unify immediately
  Can't handle: type class constraints (which impose global requirements)
                GADTs (which require local type refinements to propagate)

OutsideIn(X):
  Separates "given" constraints (what we know at this point)
  from "wanted" constraints (what we need to prove)

  Given: local type assumptions (what enclosing bindings have established)
  Wanted: constraints generated by the expression being checked

  Propagation: wanted constraints float upward to the enclosing binding
  Resolution: solved at the outermost scope where enough information exists

  This is why `show . read` requires a type annotation:
    show :: Show a => a -> String
    read :: Read a => String -> a
    show . read :: Read a, Show a => String -> String
    The constraint `a` has nothing to resolve it — annotation required.

  But `show (read "42" :: Int)` works:
    The annotation `:: Int` resolves `a = Int`, satisfying both constraints.
    OutsideIn picks this up and solves the wanted constraints.

  Why Haskell type errors are sometimes far from the source:
    OutsideIn floats wanted constraints outward.
    The failure is reported at the enclosing binding where resolution fails,
    not necessarily at the use site that generated the constraint.
    This is architecturally correct but pedagogically confusing.
```

---

## Subtyping — Structural vs Nominal

### The Two Regimes

```
Nominal subtyping (Java, C#, Swift classes):
  A <: B iff A is declared to extend/implement B
  The name matters. Two types with identical structure are unrelated
  unless declared.

  class Point { x: number; y: number; }
  class Coord { x: number; y: number; }
  // Point and Coord are unrelated — different names

Structural subtyping (TypeScript, OCaml):
  A <: B iff A has at least the structure of B
  The name doesn't matter. Compatibility is determined by shape.

  type Point = { x: number; y: number };
  type HasX  = { x: number };
  // Point <: HasX — Point has everything HasX requires + more

Duck typing with static checking = structural subtyping.
```

### Variance

For a type constructor `F`, how does `F<A>` relate to `F<B>` when `A <: B`?

```
Covariant F:     A <: B  implies  F<A> <: F<B>    (same direction)
  ReadonlyArray<Cat> <: ReadonlyArray<Animal>   (if Cat <: Animal)
  Safe: you can read from F<A> wherever F<B> is expected

Contravariant F: A <: B  implies  F<B> <: F<A>    (reversed)
  (Animal → void) <: (Cat → void)               (if Cat <: Animal)
  A function that handles any Animal can substitute for one needing Cat
  Safe: you can write/consume into F<A> wherever F<B> is expected

Invariant F:     Neither
  Array<Cat> ≮ Array<Animal>                    (mutable array)
  If it were covariant: push(new Dog()) via Animal[] reference = runtime error
  TypeScript arrays are unsoundly covariant (historical JavaScript compat)

Bivariant F:     Both directions (unsound)
  TypeScript method parameters are bivariant by default (--strictFunctionTypes
  changes function type parameters to contravariant — the sound choice)
```

```typescript
// TypeScript variance in practice
interface Producer<T> { produce(): T }   // covariant in T (only returns)
interface Consumer<T> { consume(x: T): void }  // contravariant in T (only takes)
interface Transformer<T> { transform(x: T): T } // invariant in T (both)

// TypeScript 4.7+ explicit variance annotations
interface Box<out T> { value: T }    // out = covariant
interface Sink<in T> { send(x: T): void }  // in = contravariant
```

---

## TypeScript's Type System — The Full Picture

TypeScript's type system is substantially more expressive than HM. It has features drawn from research that only existed in dependently-typed languages a decade ago.

### Conditional Types

```typescript
// Conditional types: type-level if-then-else
type IsArray<T> = T extends any[] ? true : false;
type A = IsArray<number[]>;  // true
type B = IsArray<string>;    // false

// Distributive conditional types: distributes over unions
type Flatten<T> = T extends any[] ? T[number] : T;
type C = Flatten<string[] | number>;  // string | number
// When T = string[] | number:
//   Flatten<string[]> | Flatten<number>
//   = string | number

// Infer keyword — pattern matching on types
type ReturnType<T> = T extends (...args: any[]) => infer R ? R : never;
type D = ReturnType<(x: number) => string>;  // string

// Recursive conditional types (since TS 4.1)
type DeepReadonly<T> =
  T extends (infer U)[]      ? DeepReadonlyArray<U> :
  T extends object           ? DeepReadonlyObject<T> :
  T;
type DeepReadonlyArray<T> = ReadonlyArray<DeepReadonly<T>>;
type DeepReadonlyObject<T> = { readonly [K in keyof T]: DeepReadonly<T[K]> };
```

### Mapped Types

```typescript
// Mapped types: transform every property
type Partial<T> = { [K in keyof T]?: T[K] };
type Required<T> = { [K in keyof T]-?: T[K] };  // -? removes optional
type Readonly<T> = { readonly [K in keyof T]: T[K] };

// Key remapping (TS 4.1+)
type Getters<T> = {
  [K in keyof T as `get${Capitalize<string & K>}`]: () => T[K]
};
type G = Getters<{ name: string; age: number }>;
// { getName: () => string; getAge: () => number }
```

### Template Literal Types

```typescript
// Type-level string manipulation
type EventName<T extends string> = `on${Capitalize<T>}`;
type E = EventName<"click" | "focus">;  // "onClick" | "onFocus"

// CSS property validation at the type level
type CSSProperty = `${"margin" | "padding"}-${"top" | "right" | "bottom" | "left"}`;
// "margin-top" | "margin-right" | ... | "padding-left"  (8 members)
```

### The Turing Completeness Proof

TypeScript's type system is Turing complete. The proof via encoding a Turing machine in types was given by Rúnar Bjarnason (2019). A simpler proof via recursive types:

```typescript
// Peano arithmetic in the type system
type Zero = { kind: "zero" };
type Succ<N> = { kind: "succ"; prev: N };
type Two = Succ<Succ<Zero>>;
type Three = Succ<Two>;

// Addition: Add<Two, Three> = Five
type Add<A, B> =
  A extends Zero ? B :
  A extends Succ<infer Prev> ? Succ<Add<Prev, B>> : never;

// This recursion can loop: tsc adds a depth limit (100) and gives
// "Type instantiation is excessively deep and possibly infinite"
// That error IS the tsc escape hatch from the halting problem.
```

The depth limit is tsc's guard against infinite type evaluation — the type-level analog of the halting problem.

---

## Linear and Affine Types — Rust's Ownership

Substructural type systems restrict which structural rules the type system obeys:

```
Structural rules:
  Weakening:  If Γ ⊢ e : T, then Γ, x:A ⊢ e : T    (unused variables ok)
  Contraction: If Γ, x:A, y:A ⊢ e : T,
               then Γ, z:A ⊢ e[z/x, z/y] : T         (variable used twice ok)
  Exchange:   Variables can be reordered in context

Linear types:   Allow neither weakening nor contraction
                Every variable used exactly once
Affine types:   Allow weakening, not contraction
                Every variable used at most once (can be dropped)
Relevant types: Allow contraction, not weakening
                Every variable used at least once
```

**Rust's ownership system is affine typing:**

```rust
let s = String::from("hello");
let t = s;           // move: s transferred to t (contraction forbidden)
println!("{}", s);   // ERROR: s used after move — affine violation

// To use twice, must clone (explicit duplication) or borrow
let s2 = s.clone();  // explicit copy — both s and s2 valid
let r = &s;          // borrow: temporary shared access (re-lends)
```

### The Ownership → Linear Types Correspondence

```
Linear type system            Rust ownership
══════════════════            ═════════════
Linear variable (use once)    Owned value (moved on use)
Variable sharing              Borrow (&T)
Exclusive access              Mutable borrow (&mut T)
Explicit duplication          .clone()
Linear function               fn(T) -> U  (consumes T)
Unrestricted function         fn(&T) -> U (borrows T)

The borrow checker is a decision procedure for affine type checking.
Well-typedness in the affine system = the borrow checker accepts the program.
The type system is sound: no accepted program has use-after-free or data races.
```

### Lifetimes as Region Types

Rust's lifetime annotations are an implementation of **region-based memory management** (Tofte & Talpin 1997). Every reference has a lifetime parameter that bounds how long it may be used:

```rust
// Lifetime annotation makes the region explicit
fn longest<'a>(s1: &'a str, s2: &'a str) -> &'a str {
  if s1.len() > s2.len() { s1 } else { s2 }
}
// 'a is a region variable.
// The contract: both inputs live at least as long as 'a;
//               the output lives no longer than 'a.
// The borrow checker verifies this at every call site.
```

The NLL algorithm (22-COMPILERS) computes lifetime bounds as a dataflow problem on MIR — it's finding the minimal region that satisfies all constraints.

---

## Algebraic Data Types and Pattern Matching

ADTs + exhaustive pattern matching are the PL-theory contribution most visibly adopted by mainstream languages over the last decade.

```
Sum types (disjoint unions):
  type Result<T, E> = Ok(T) | Err(E)   -- Rust
  type Shape = Circle | Square | Triangle  -- TypeScript union

Product types (records/tuples):
  struct Point { x: f64, y: f64 }   -- Rust
  type Point = { x: number; y: number }  -- TypeScript

Algebraic = sums of products. Every ADT is expressible this way.
```

```
Language adoption timeline:
  Haskell (1990):   ADTs + pattern matching as core design
  Scala (2004):     case classes + match
  F# (2005):        discriminated unions + match
  Swift (2014):     enums with associated values + switch
  Rust (2015):      enums + match (exhaustive by default)
  Kotlin (2016):    sealed classes + when
  TypeScript (2016+): discriminated unions + narrowing
  Java (2021+):     sealed classes + pattern matching (JEP 406, 441)
  Python (2021):    match statement (structural pattern matching)
  C# (2019+):       switch expressions + positional patterns
```

The exhaustiveness check (switch must handle every case) is the type-theoretic property that prevents "forgot to handle the new enum case" bugs. It's why Rust's `match` requires a `_` arm if not exhaustive.

---

## Type Classes vs Interfaces vs Traits

Three mechanisms for ad-hoc polymorphism — functions that work over multiple types — with different theoretical foundations:

```
Haskell type classes:
  class Eq a where
    (==) :: a -> a -> Bool

  instance Eq Int where ...
  instance Eq a => Eq [a] where ...  -- conditional instances

  Dictionary-passing translation:
    Compiler generates a dictionary (record of function pointers)
    per instance. Passes it implicitly at call sites.

Rust traits:
  Direct descendant of Haskell type classes.
  Trait objects (&dyn Trait) use vtables (like OOP interfaces).
  impl Trait (monomorphization) generates a copy per concrete type.
  Orphan rules: can only implement a trait if you own the trait or the type.
  (Prevents coherence violations — two implementations of same trait for same type)

TypeScript interfaces / structural:
  No explicit declaration of conformance.
  {x: number} satisfies {x: number} automatically.
  No "instance" relationship — structural check at each use site.
  No dictionary passing — erased at runtime.
  Limitation: can't write "this type has an Eq instance" as a constraint.
```

**Scala 3's `given`/`using` as dictionary-passing translation:**

Scala 3's `given` introduces a dictionary instance; `using` requires one at the call site. This is a direct surface-level encoding of the dictionary-passing translation that Haskell does implicitly.

```scala
// Scala 3 given/using — explicit dictionary passing
trait Eq[A]:
  def eqv(a: A, b: A): Boolean

given Eq[Int] with
  def eqv(a: Int, b: Int): Boolean = a == b

def assertEq[A](a: A, b: A)(using eq: Eq[A]): Unit =
  assert(eq.eqv(a, b))

assertEq(1, 1)  // compiler inserts the Eq[Int] dictionary at call site
```

The key distinction from C# interface dispatch (which this learner knows from .NET): C# requires declaring conformance at definition site (`class Foo : IEquatable<Foo>`). Scala's `given` and Haskell's `instance` both allow **retroactive conformance** — you can add an `Eq` instance for `Int` in a library that has nothing to do with `Int`'s definition. This is the same capability Rust's traits provide, and it solves the expression problem for the operations axis.

C# in .NET has no retroactive conformance for interfaces. The closest approximation is extension methods, but those don't participate in generic constraints — you can't write `where T : IEquatable<T>` and satisfy it retroactively.

### The Expression Problem

A classic PL design tension, first stated by Wadler (1998):

```
Given:
  - A set of types (Circle, Square)
  - A set of operations (area, perimeter)

Can you add both new types AND new operations without modifying existing code?

OOP solution:    Easy to add new types (new subclass).
                 Hard to add new operations (modify base class + all subclasses).

FP solution:     Easy to add new operations (new function over the ADT).
                 Hard to add new types (modify pattern match in all functions).

Solutions:
  Type classes (Haskell) / Traits (Rust):
    New type → new instance (no modification to existing code)
    New operation → new type class (no modification to existing types)
    ✅ Solves the expression problem

  Open classes (Ruby, JavaScript prototype):
    Monkey-patching: add methods to existing types
    ✅ Solves it dynamically, at the cost of safety

  Tagless final (Haskell / Scala):
    Encode operations as type class constraints, types as interpreters
    ✅ Solves it in a more principled way at the cost of complexity
```

---

## Semantics

Three frameworks for specifying what programs mean. All three appear in practice:

### Operational Semantics

Defines meaning by reduction rules. Small-step (`e → e'`, one step) and big-step (`e ⇓ v`, evaluate to value) are the two standard presentations; Progress + Preservation (Wright & Felleisen) is the canonical type safety proof structure. You've proved these for multiple calculi. The value here is where these techniques break down and what replaced them:

**RustBelt (Jung, Jourdan, Krebbers, Dreyer — POPL 2018):**

Standard syntactic type safety (Progress + Preservation) does not scale to a language with `unsafe` code and ownership. The theorem "well-typed programs don't get stuck" doesn't account for:
- Code that is safe at the boundary (`unsafe` function with a correct pre-condition) but whose interior violates the type system temporarily
- Ownership invariants that hold globally but are transiently violated inside `unsafe` blocks
- The interaction between `Arc<T>` (atomic reference counting) and aliasing

RustBelt proves Rust's type system sound using a **logical relation** argument in Iris — a higher-order concurrent separation logic. The key move: instead of proving a syntactic property of the type system, RustBelt defines a semantic model where each Rust type `T` is interpreted as a predicate on memory states. Safety means: if a value is typed `T`, the memory satisfies `T`'s predicate. `unsafe` code is proved correct by showing it establishes the required predicates before returning.

The separation logic (Iris) handles ownership and aliasing: the `*` operator in Iris is separating conjunction — `P * Q` means P and Q describe disjoint portions of the heap. This makes ownership invariants expressible as logical assertions.

```
Why syntactic safety fails for Rust:
  Progress: "well-typed e is either a value or steps"
  — false in the presence of unsafe blocks that can produce UB

  Preservation: "if ⊢ e : T and e → e', then ⊢ e' : T"
  — the borrow checker is not a standard type system rule;
    it's a separate analysis on MIR

RustBelt's fix:
  Define a semantic interpretation [[T]] for each type T
  Prove: if v : T in the surface type system, then v ∈ [[T]] holds
  Prove: operations on v that respect [[T]] cannot cause UB
  The separation logic handles the heap ownership part
```

Standard proof techniques from 6.820 get you most of the way. For a production language with `unsafe`, you need the step up to logical relations + separation logic.

### Denotational Semantics

Maps programs to mathematical objects (sets, domains, functions).

```
[[e]] : Environment → Value   (interpretation function)

[[λx.e]] ρ = λv. [[e]] (ρ[x ↦ v])   -- lambda is a function
[[e₁ e₂]] ρ = [[e₁]] ρ ([[e₂]] ρ)   -- application is function application

Used in:
  Reasoning about program equivalence (⟦e₁⟧ = ⟦e₂⟧ → they're the same)
  Compiler correctness proofs (translation preserves denotation)
  Type theory foundations (domain theory for recursive types)

Scott domains solve the recursion problem:
  f = λx. f x  (diverges)
  Needs a domain with a "bottom" element ⊥ representing divergence
  D ≅ [D → D] — a domain isomorphic to its own function space
  Dana Scott's CPO construction (1969) makes this precise
```

### Axiomatic Semantics (Hoare Logic)

Specifies behavior via pre/post-conditions.

```
{P} C {Q}   — Hoare triple
  If P holds before executing C, then Q holds after

{x = n} x := x + 1 {x = n + 1}

Weakest precondition:
  wp(C, Q) = weakest P such that {P} C {Q}
  Predicate transformer semantics (Dijkstra 1975)

Used in:
  Formal verification (Dafny, Why3, Frama-C)
  Separation logic (extends Hoare logic with heap reasoning)
  Rust's unsafe code reasoning (RustBelt project)

RustBelt (2018, POPL):
  Formal semantic model of Rust in Iris (a higher-order concurrent separation logic)
  Proves that the Rust type system is sound: safe code cannot exhibit UB
  Handles the hard cases: Arc, Mutex, raw pointer manipulation in unsafe blocks
```

---

## Research → Production Pipeline

The lag between PL research publication and mainstream language adoption is typically 10–20 years:

```
Research            Year    Production landing
══════════════      ════    ══════════════════════════════
Hindley-Milner      1969    OCaml (1996), F# (2005)
Dependent types     1972    Agda (2007), Idris (2011), Lean 4 (2021)
Hoare logic         1969    Dafny (2008), VeriFast, Frama-C
Type classes        1989    Haskell, Rust traits (2015)
Linear types        1987    Rust ownership (2015)
Region types        1997    Rust lifetimes (2015) — 18 year lag
Algebraic effects   ~2001   OCaml 5 effects (2022), Koka (2014)
Gradual typing      2006    TypeScript (2012), mypy (2012) — 6 year lag
Row polymorphism    ~1991   Elm (2012), PureScript

Rust is, from a PL theory standpoint, the most theory-dense production
language to achieve mainstream adoption. It ships:
  Affine types, region types, trait-based bounded polymorphism,
  HRTB (higher-ranked trait bounds = rank-2 polymorphism),
  GATs (generic associated types = limited type operators),
  const generics (limited dependent types)
```

### What's Coming Next

```
Algebraic effects (replacing monads for effectful programming):
  OCaml 5 (2022): multicore + effects
  Koka: full effect system with handlers
  The pitch: composable effects without monad transformer stacks
  Timeline to mainstream: 5–10 years (dependent on OCaml/Koka uptake)

Dependent types in mainstream:
  Idris 2, Lean 4 exist but require PL expertise to use
  Gradual dependent types (mixing with inference) is active research
  Timeline: 10–15 years to mainstream

Linear types in more languages:
  Move types in Swift (2024 proposal)
  Unique types in Clean
  Checked C extensions
  Already mainstream via Rust — likely to spread

Better effect inference / async:
  async/await is a partial effect system (marks IO-effectful functions)
  Rust's async is particularly principled (poll-based, zero-cost)
  Full effect inference (no explicit marks) is research-grade
```

---

## Common Confusion Points

**HM inference is not the same as TypeScript inference.**
HM gives principal types and is complete (if a type exists, it's found). TypeScript's inference is bidirectional with subtyping — it's neither complete nor always finds the most general type. The incompleteness is intentional: full HM + subtyping is undecidable.

**Structural typing is not duck typing.**
Duck typing (Python, JavaScript) is structural typing checked at runtime. TypeScript's structural typing is checked statically. They have the same model but very different failure modes.

**Linear types and GC are not opposed.**
Linear types guarantee each value is used exactly once — this enables compile-time deallocation (the value's last use is its deallocation point). But you can have linear types with a GC (Haskell's linear types extension). The choice of memory management is orthogonal to the substructural discipline.

**`never` in TypeScript is not the same as `undefined` or `null`.**
`never` is the empty type — no value can be produced. `undefined` and `null` are inhabited types (with one value each). A function returning `never` doesn't return (throws or infinite loops). A function returning `undefined` returns, with the value `undefined`. The distinction matters for exhaustiveness checking.

**Rust's borrow checker is not the type checker.**
They're separate phases on separate IRs. Type checking runs on HIR (with full generic types). Borrow checking runs on MIR (after monomorphization, on the CFG). NLL computes liveness on MIR. They're related but distinct analyses.

**Covariant arrays in TypeScript are unsound.**
`string[] <: object[]` in TypeScript (covariant). This allows:
```typescript
const strings: string[] = ["a", "b"];
const objects: object[] = strings;  // allowed (covariant)
objects.push(42);                   // type-checks — 42 is an object
strings[2].toUpperCase();           // runtime error — 42 is not a string
```
TypeScript made this trade deliberately for practical compatibility with JavaScript patterns. It's a known unsoundness.

---

## Theory → Tools Map

```
Concept                     Where it lives in the tools you use
═══════════════             ════════════════════════════════════════════
HM type inference           TypeScript inference, OCaml/F# type inference
Algorithm W                 ghc (Haskell), ocaml type checker
OutsideIn(X)                GHC's actual inference algorithm (constraints + GADTs)
Structural subtyping        TypeScript, OCaml module types
Variance (co/contra)        TypeScript in/out annotations, Scala +/-
Conditional types           TypeScript conditional types
Dependent types (limited)   TypeScript template literals, const generics in Rust
Affine types                Rust ownership + move semantics
Region types                Rust lifetimes + borrow checker (NLL)
Type classes / Traits       Rust traits, Haskell type classes
Dictionary passing          Haskell instances, Scala 3 given/using
Algebraic effects           OCaml 5 effects, async/await (partial)
Hoare logic                 Dafny, RustBelt proofs, separation logic
Operational semantics       ECMAScript spec, language standard definitions
Denotational semantics      Compiler correctness proofs (CompCert)
Curry-Howard                TypeScript `never`, Coq/Lean proofs
Parametricity / free thm.   TypeScript generic constraints, Haskell theorems
Row polymorphism            Elm types, OCaml polymorphic variants
Gradual typing              TypeScript (any = dynamic boundary), mypy
RustBelt / Iris             Why Rust's safety proof needs separation logic
System F + coercions        GHC Core IR design
```

---

## Decision Cheat Sheet

| I want to understand... | Concept |
|---|---|
| Why TypeScript inference sometimes gives `unknown` instead of a type | Bidirectional inference + context dependency; incomplete vs HM |
| Why Rust rejects a program that seems correct | Affine type violation or lifetime constraint not satisfiable by NLL |
| Why TypeScript's `never` shows up in exhaustiveness checking | `never` is the empty type — Curry-Howard bottom |
| Why covariant arrays in TypeScript can cause runtime errors | Mutable containers should be invariant; TS chose unsound covariance |
| Why Rust trait orphan rules exist | Coherence: one implementation per (type, trait) pair, globally |
| Why TypeScript type eval gives "excessively deep" error | TC type system hitting tsc's depth limit guard against non-termination |
| Why Haskell compiles so slowly | Full HM + type class resolution + GHC Core optimization passes |
| Why adding a new case to a union type breaks many places | Exhaustiveness checking — intentional, the point of ADTs |
| Where `async/await` sits in type theory | Partial effect system — marks IO-effectful computation |
| Why Rust lifetimes are hard to learn | They're region type annotations — not in most programmers' prior experience |
| Why GHC type errors appear far from the source | OutsideIn(X) floats wanted constraints outward; error at resolution site |
| Why `show . read` needs a type annotation in Haskell | OutsideIn(X): the constraint `a` has no resolving information without annotation |
| Why Scala 3 `given` differs from C# interface dispatch | Scala: retroactive conformance (add instance for type you don't own); C#: declaration-site only |
| Why Rust's type safety proof needed Iris | Syntactic progress+preservation fails for unsafe; RustBelt uses logical relations + separation logic |
| Why GHC Core is System F, not Fω | Coercions keep the core calculus decidable while supporting GADTs and newtypes |
