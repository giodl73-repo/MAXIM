# Modern Frontiers: Gradual Typing, Refinement Types, Session Types, HoTT

## The Big Picture

The current frontiers of type theory are about extending static guarantees to more programs in more languages, verifying richer properties, and providing formal foundations for newer programming paradigms. Several of these have moved from theoretical to industrial in the last decade.

```
+--------------------------------------------------------------------------+
|                    MODERN FRONTIERS LANDSCAPE                             |
+--------------------------------------------------------------------------+
|                                                                          |
|  GRADUAL TYPING (Siek/Taha 2006)     REFINEMENT TYPES (Freeman 1991)   |
|  Mix static + dynamic types          Base types + logical predicates    |
|  Blame assignment on type error      Liquid types, LiquidHaskell, F*   |
|  TypeScript = industrial gradual TS  F* used for EverCrypt, miTLS       |
|  Typed Racket = sound gradual TS     Array bounds, null safety, security |
|                                                                          |
|  SESSION TYPES (Honda 1993)          LINEAR TYPES IN PRODUCTION         |
|  Communication protocols as types    Rust = affine type system          |
|  Channel type = remaining protocol   Ownership tracks aliasing          |
|  Deadlock freedom from linearity     Stacked Borrows formal semantics   |
|  Global types → local by projection  RustBelt: Iris separation logic    |
|                                                                          |
|  HOMOTOPY TYPE THEORY (HoTT)         CUBICAL TYPE THEORY                |
|  Voevodsky univalence axiom          Constructive proof of univalence   |
|  Types as spaces; equiv = equality   Computational content for HITs     |
|  Lean 4 Mathlib frontier             Coquand et al.; Cubical Agda       |
+--------------------------------------------------------------------------+
```

---

## 1. Gradual Typing

Siek and Taha (2006) — the foundational paper for mixing static and dynamic types:

**The core idea**:
```
GRADUAL TYPING:

  Standard types:  Int, String, Bool → fully statically typed
  Dynamic type:    ? (or "dynamic", or "any") → like dynamic typing
  Gradual type:    Int → ? (function from Int to something unknown)

  TYPE CONSISTENCY (≈):
    Type A is consistent with type B if they MIGHT be compatible:
    Int ≈ Int    (obviously)
    Int ≈ ?      (? is consistent with everything)
    ? ≈ String   (? is consistent with everything)
    Int ≈ String (NOT consistent)

  KEY: consistency ≈ is NOT transitive
    Int ≈ ?  and  ? ≈ String  does NOT give  Int ≈ String
    (Transitivity would make the type system useless)

CAST INSERTION (compiling gradual programs):

  When you assign an Int to a ? variable:
    x : Int → y : ?
    Compile: y = <? ← Int> x    (upcast: always safe)

  When you assign a ? variable to an Int:
    z : ? → w : Int
    Compile: w = <Int ← ?> z    (downcast: may fail at runtime)
    Runtime check: if z is actually an Int, succeed; else runtime error

BLAME ASSIGNMENT:
  When a cast fails at runtime, which part of the code is to blame?
  Blame tracks: who inserted the type annotation that caused the error
  → If your typed code fails, the untyped code you called is "to blame"
  → Blame theorem: well-typed code cannot be blamed
```

**Typed Racket (Tobin-Hochstadt, Felleisen 2006)** — sound gradual typing:
```
TYPED RACKET: the reference implementation of sound gradual typing

  Gradually typed modules: some files are #lang typed/racket, others untyped
  Contracts inserted at typed/untyped boundaries
  If an untyped function is called from typed code: contract check at call site
  If typed function called from untyped code: contract check at return

  SOUNDNESS:
    If typed code has type T, it produces a value of type T or raises a
    contract violation error attributing blame to the correct module
    → Well-typed Typed Racket code CANNOT produce wrong-type values

  PERFORMANCE COST:
    Every boundary crossing = contract check = potential overhead
    Gradual typing can be slow for programs with many typed/untyped crossings
    Research area: efficient gradual types (Vitousek et al., cast calculi)
```

**TypeScript: industrial gradual typing (unsound by design)**:
```
TYPESCRIPT vs. TYPED RACKET:

             TypeScript           Typed Racket
  Soundness: Intentionally NO     YES (at boundaries)
  Checks:    Erased at runtime    Contracts inserted
  Blame:     No runtime blame     Runtime blame tracking
  Speed:     Zero overhead        Overhead at boundaries
  Goal:      Catch most bugs,     Sound reasoning about
             maximum usability    typed code

TYPESCRIPT'S DELIBERATE UNSOUNDNESS HOLES:
  1. any type defeats all checking
  2. as casts: x as SomeType (unchecked)
  3. Covariant method parameters (should be contravariant)
  4. @ts-ignore suppresses errors
  5. Type assertions on external data (JSON.parse → any)

FROM TS DESIGN GOALS:
  "TypeScript's type system is not fully sound. There are some places
   where unsoundness was an intentional choice to allow more patterns
   to be expressed."

WHY UNSOUNDNESS IS SOMETIMES RIGHT:
  Usability: if you type-annotate existing JS and all existing patterns fail,
             nobody adopts the type system
  Gradual adoption: need to be able to type parts of programs
  Developer experience: false positives are costly (real errors ignored)
```

---

## 2. Refinement Types

Refinement types (Freeman and Pfenning 1991, Xi and Pfenning 1999) extend a base type with a predicate:

**Syntax and semantics**:
```
REFINEMENT TYPE SYNTAX:
  {x : B | p(x)}   ("the set of values of base type B satisfying predicate p")

EXAMPLES:
  {n : Int | n > 0}          positive integers
  {n : Int | n >= 0 && n < len a}  valid index into array a
  {s : String | length s > 0}       non-empty string

TYPING WITH REFINEMENTS:
  If e : {x : Int | x > 0} and f : (y : Int | y > 0) → String
  Then f e : String   (safely — no runtime check needed)

  If the predicate cannot be verified at compile time:
    → Require runtime check (subtype check = predicate evaluation)
    → Or: fail to typecheck (programmer must provide proof)
```

**Liquid Types (Rondon, Kawaguchi, Jhala 2008)**:
```
LIQUID TYPES (Logically Qualified Types):

  KEY INSIGHT: Predicates restricted to a grammar of "qualifiers"
    Qualifier = conjunction of atomic predicates from a fixed set Q
    Q = {x > 0, x ≥ 0, x < y, x = y, ...} (user-specified + library)

  INFERENCE via HORN CLAUSES:
    Generate subtyping constraints from typing rules
    Each constraint: κ ⊆ {x | p(x)} (where κ is a qualifier variable)
    Solve using predicate abstraction (CEGAR) or SMT solver
    → FULLY AUTOMATIC for many common patterns

LIQUIDHASKELL:
  LiquidHaskell is Haskell + liquid types
  Predicates are Haskell expressions (arbitrary refinements)
  Uses Z3 SMT solver to discharge proof obligations

  EXAMPLE:

  {-@ head :: {v : [a] | len v > 0} -> a @-}
  head :: [a] -> a
  head (x:_) = x

  head [] cannot be called — the type requires a non-empty list.
  LiquidHaskell verifies this statically via Z3.

  MORE COMPLEX:

  {-@ take :: n:Nat -> xs:{[a] | len xs >= n} -> {[a] | len v = n} @-}
  take :: Int -> [a] -> [a]

  Types track list lengths exactly.
```

**F* (Swamy et al., Microsoft Research)** — refinement types + effects + proofs:
```
F*: the verification tool for security-critical code

  F* = dependent types + refinement types + effect system (Dijkstra monad)

  KEY APPLICATIONS:
    EverCrypt: verified cryptographic library (chacha20, poly1305, ECDH)
      → Used in NSS (Mozilla), BoringSSL variant, WireGuard
    miTLS: formally verified TLS 1.3 implementation
    HACL*: verified low-level C crypto (used in Firefox, Chrome)
    Project Everest: end-to-end verification of HTTPS stack

  F* EXAMPLE:

  val factorial: n:nat → Tot nat (decreases n)
  let rec factorial n =
    if n = 0 then 1 else n * factorial (n-1)

  (* nat = {x:int | x ≥ 0} *)
  (* Tot nat = total function returning nat (no IO, no exceptions) *)
  (* decreases n = termination proof hint *)

  val array_index: a:array int → n:{x:nat | x < length a} → Tot int
  let array_index a n = index a n
  (* The index n must be provably in bounds — checked at call site *)
```

---

## 3. Session Types

Honda (1993), Takeuchi, Honda, Kubo (1994) — types for communication protocols:

**The key idea**:
```
SESSION TYPES: channel type = remaining protocol

  A CHANNEL of session type S is a channel whose future communication
  must follow protocol S.

  PROTOCOL TYPES:
    !Int.S   = "send an Int, then continue with protocol S"
    ?Int.S   = "receive an Int, then continue with protocol S"
    end      = "channel is closed"
    !Bool.(!Int.end)   = "send Bool, then send Int, then close"

  DUALITY:
    If I have channel of type !Int.S
    Then my communication partner has channel of type ?Int.S
    (send ↔ receive dually)

  TYPING RULE FOR SEND:
    Γ, c : !T.S ⊢ send c v ; P     when Γ ⊢ v : T
    After sending: c's type becomes S (the remaining protocol)

  LINEARITY REQUIRED:
    Channel must be used LINEARLY (exactly once per operation)
    Prevents: using the channel again after it's been closed
    Ensures: the protocol is followed in the right order
```

**Global types and projection**:
```
GLOBAL SESSION TYPES (Carbone, Honda, Yoshida 2007):

  A GLOBAL TYPE describes the overall protocol from all participants' view:
    A → B : Int ; B → C : Bool ; end
    "A sends Int to B, then B sends Bool to C, then done"

  PROJECTION: derive each participant's local type by projection
    A's type: !Int.end      (A sends Int, then done)
    B's type: ?Int.!Bool.end (B receives Int, then sends Bool, then done)
    C's type: ?Bool.end     (C receives Bool, then done)

  DEADLOCK FREEDOM:
    If all participants follow their projected types,
    no deadlock can occur (no circular waiting)
    → Guaranteed by type system

RUST-INSPIRED SESSION TYPES (Sesh, Recto, etc.):
  Several Rust crates implement session types using Rust's ownership:
  The channel type encodes the session type in a phantom type parameter
  Each send/receive operation returns the channel with updated type
  Linear ownership ensures the channel is used according to protocol
```

---

## 4. Linear Types in Production: Rust

Rust is the dominant production application of linear type theory:

```
RUST AS AFFINE TYPE SYSTEM:

  Every value is:
  T (owned): used at most once (affine; can be dropped = discarded)
    move: transfers ownership (linear "use")
    drop: implicit at end of scope (affine = can discard)

  &T (shared reference): can copy freely; no mutation
    Corresponds to: !T in linear logic (unrestricted read-only access)
    Multiple &T to the same T: all frozen for borrow duration

  &mut T (exclusive reference): one at a time; can mutate
    Corresponds to: linear T (use exactly once per borrow)
    EXCLUSIVE: while &mut T lives, no other reference to T
    After &mut T drops: T is "returned" to its owner

BORROW CHECKER = LINEAR TYPE CHECKER:

  The borrow checker enforces:
    1. You cannot have both &T and &mut T to the same T simultaneously
    2. You cannot have two &mut T to the same T simultaneously
    3. You cannot use T after moving it (linear use)
    4. All borrows must end before T is dropped or moved

  THESE RULES ARE EXACTLY the rules of linear logic:
    Rule 1 = the linearity/exclusivity of ⊗ in linear logic
    Rule 3 = use exactly once

FORMALIZATION (RustBelt, Jung et al. POPL 2018):
  Uses "Iris": a concurrent separation logic framework (Coq library)
  Models Rust's operational semantics (Stacked Borrows)
  Proves: safe Rust code cannot exhibit UB (data races, dangling pointers)
  Critical insight: unsafe Rust requires invariants; safe code cannot break them
```

---

## 5. Homotopy Type Theory (HoTT)

Voevodsky's Univalent Foundations (2009–2013), popularized in "HoTT Book" (2013):

**The key insight** — types as spaces:
```
HOMOTOPY TYPE THEORY:

  In HoTT, types are interpreted as TOPOLOGICAL SPACES (or homotopy types):
    A value a : A = a POINT in space A
    A proof p : Id_A(a, b) = a PATH from point a to point b in space A
    A proof of Id(p, q) = a HOMOTOPY (path between paths)

  UNIVALENCE AXIOM (Voevodsky):
    (A ≃ B) ≃ (A = B)    "equivalent types are EQUAL types"

    A ≃ B means: there's an isomorphism between A and B
    (a bijection respecting all structure)

    Voevodsky's insight: ISOMORPHIC MATHEMATICAL STRUCTURES SHOULD BE EQUAL
    This is what mathematicians have always "meant" but couldn't formalize.

  PRACTICAL CONSEQUENCE:
    If you prove something about ℤ (integers),
    and ℤ ≃ ℤ_even × Bool (isomorphism),
    then your theorem automatically transfers to ℤ_even × Bool.
    No "transport" lemma needed — they are literally equal types.
```

**Higher Inductive Types (HITs)**:
```
HIGHER INDUCTIVE TYPES:

  In standard type theory: inductive types have point constructors only.
  HITs also have PATH CONSTRUCTORS (equality proofs as constructors).

  EXAMPLE: The circle S¹
    Type S¹ with constructors:
      base : S¹                    (a point)
      loop : Id(base, base)        (a path from base to itself)

  This is NOT just isomorphic to Unit — it has a non-trivial loop!
  π₁(S¹) = ℤ  (the fundamental group of the circle is the integers)
  In standard type theory: cannot express non-trivial topology

  QUOTIENT TYPES VIA HITS:
    A / R = A with constructors from A
            plus: for each (a, b) with R a b, a proof Id(a, b)
    This collapses a to b whenever R a b holds
    Example: ℤ = pairs (m, n : ℕ) quotiented by (m+n₀ = m₀+n)
```

---

## 6. Cubical Type Theory

Coquand et al. (2015) — gives computational content to univalence:

```
UNIVALENCE IN STANDARD HOTT vs. CUBICAL:

  Standard HoTT: univalence is an AXIOM
    axiom univalence : (A ≃ B) → (A = B)
    No computational rule: the axiom "fires" in types but not in terms
    → Blocked computation (terms that can't reduce to normal form)
    → Extract programs from proofs but some proofs have no extraction

  CUBICAL TYPE THEORY:
    Paths are FUNCTIONS from the interval [0,1] → Type
    Equality p : a = b is literally a function p : I → A with p 0 = a, p 1 = b

    Univalence is PROVABLE (not an axiom) in cubical type theory
    With computational content: you CAN extract programs from proofs involving univ.

CUBICAL AGDA:
  Agda has an option --cubical (or --erased-cubical)
  Enables: dependent path types, univalence as theorem, HITs
  Used for: formalization of higher category theory, algebraic topology

LEAN 4 AND HoTT:
  Lean 4 chose NOT to be HoTT-based (uses classical logic + UIP)
  UIP = Uniqueness of Identity Proofs (all proofs of a = b are equal)
  This is incompatible with HoTT (which has multiple distinct paths)
  Lean 4 is for mathematics that doesn't need HoTT structure;
  Agda is for HoTT-based formalization
```

---

## Decision Cheat Sheet

| Need | System | Status |
|------|--------|--------|
| Mix typed + untyped code soundly | Typed Racket | Production |
| TypeScript-style type checking | TypeScript | Production (intentionally unsound) |
| Array bounds, null safety, security | LiquidHaskell / F* | Production for security-critical |
| Verified cryptography | F* (EverCrypt, HACL*) | Production (in Firefox, Chrome) |
| Memory safety via types | Rust (affine types) | Production |
| Communication protocol types | Session types in Rust crates | Experimental in production |
| Formalizing mathematics | Lean 4 + Mathlib | Active (Mathlib 1.5M lines) |
| Homotopy theory formalization | Cubical Agda | Research frontier |
| Univalent foundations | HoTT / Cubical | Research frontier |

---

## Common Confusion Points

**Gradual typing ≠ optional type annotations**: Optional annotations (like Python type hints) are not gradual typing. Gradual typing has a formal semantics with consistency relations, blame assignment, and cast insertion. Python's mypy is gradual in some respects but not fully — it doesn't insert runtime checks (you need tools like Beartype for that).

**Refinement types ≠ dependent types**: Dependent types allow types to depend on values (Π types, Vec A n). Refinement types restrict a base type with a predicate. Refinement types are less expressive (you can't express Vec A n directly) but more automatable (SMT can discharge predicates; no interactive proofs needed for most common cases).

**Session types are theory-rich but production-thin**: Session types are well-developed theoretically. Production-level session type libraries exist for Rust and Haskell (sesh, session-types crates) but they're not mainstream. The overhead of encoding session types in a language not designed for them is significant. Languages designed around them (Links, ATS) are research prototypes.

**HoTT univalence is incompatible with UIP**: Uniqueness of Identity Proofs (UIP: all proofs that a = b are definitionally equal) is incompatible with univalence (which requires multiple distinct proofs). Lean 4 chooses UIP + classical logic → simpler math but no univalence. Agda with HoTT chooses univalence → richer but more complex. These are genuine tradeoffs.
