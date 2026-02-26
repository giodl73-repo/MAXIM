# Dependent Types: Π/Σ Types, MLTT, Coq, Agda, Idris, Lean

## The Big Picture

Dependent types are types that depend on *values*. This collapses the distinction between types and terms — a type can mention a runtime value. The result: types can express arbitrary properties of programs, and type-checking becomes theorem-proving.

```
+--------------------------------------------------------------------------+
|                    DEPENDENT TYPES LANDSCAPE                              |
+--------------------------------------------------------------------------+
|                                                                          |
|  THE KEY TYPES:                                                          |
|  Π (x:A). B(x) — dependent function type                               |
|    "the type of a function that takes x:A and returns something of       |
|     type B(x), where the RETURN TYPE depends on the VALUE x"             |
|  Σ (x:A). B(x) — dependent pair type                                    |
|    "a pair where the SECOND COMPONENT'S TYPE depends on the FIRST"       |
|                                                                          |
|  EXPRESSIVENESS EXAMPLES:                                                |
|  Vec A n — vector of length n (n is a VALUE in the type)               |
|  (n : Nat) → IsPrime n → ... — function only callable with prime n      |
|  head : Π (n : Nat). Vec A (n+1) → A   (safe head: non-empty by type)  |
|                                                                          |
|  TOOLS (from most to least foundational):                               |
|  Martin-Löf Type Theory (MLTT, 1975) — the foundation                  |
|  Calculus of Inductive Constructions (CIC) — Coq's foundation           |
|  Agda — MLTT-based, pattern matching, cubical option                    |
|  Lean 4 — Mathlib, theorem proving at scale                             |
|  Idris 2 — practical dependent types, linear types built in             |
|                                                                          |
|  DECIDABILITY CAVEAT:                                                    |
|  Type-checking with dependent types requires deciding type equality     |
|  Type equality requires deciding term equality                          |
|  Undecidable in general (Π₂-complete with full computation in types)   |
|  Solution: termination checker restricts recursive definitions           |
+--------------------------------------------------------------------------+
```

---

## 1. The Dependent Type Vocabulary

**Π type (dependent product)**:
```
Π (x:A). B(x)  — also written ∀(x:A), B(x) in Coq / ∀ x : A → B x in Agda

When B does not mention x: Π (x:A). B = A → B   (ordinary function type)
When B mentions x: the return type varies with the argument value

EXAMPLE: Safe vector head

  Vec A n   -- type of vectors of A elements with length n
  Vec A 0   -- empty vector (no elements)
  Vec A 3   -- vector of exactly 3 elements

  Unsafe head: [A] → A  (fails at runtime on empty list)
  Safe head:   Π (n : Nat). Vec A (n+1) → A
               (the input must be a vector of length ≥ 1 — enforced by type)

  Calling safe_head: you must provide a vector of length ≥ 1
  The type (n+1) ensures the vector is non-empty
  If you have an empty vector (Vec A 0), you CANNOT call this function
  → No runtime check needed; impossibility is in the type

ANOTHER EXAMPLE: Append

  append : Π (m n : Nat). Vec A m → Vec A n → Vec A (m+n)
           ↑ ↑                                          ↑
           |_|_________________________________ the types count elements

  Type system verifies: appending a 3-vector and a 4-vector gives a 7-vector
```

**Σ type (dependent sum)**:
```
Σ (x:A). B(x)  — also written {x : A | B x} (subset type) / ∃ x, B x in Coq

When B does not mention x: Σ (x:A). B = A × B   (ordinary product/pair)
When B mentions x: the second type is constrained by the first value

EXAMPLE: Prime numbers

  PrimeNat : Type = Σ (n : Nat). IsPrime n
  A value of type PrimeNat is a PAIR: (n, proof_that_n_is_prime)

  You cannot construct a PrimeNat without providing a proof of primality
  Type-level guarantee: values of PrimeNat are ACTUALLY prime

EXAMPLE: Bounded arrays

  BoundedIndex (n : Nat) : Type = Σ (i : Nat). i < n
  A BoundedIndex for array of size n is a pair: (index, proof that index < n)
  → Access array[i] where i : BoundedIndex n is always in bounds
  → No out-of-bounds access possible; type system prevents it
```

---

## 2. Martin-Löf Type Theory (MLTT)

Per Martin-Löf (1975, 1984) — the foundation of all constructive dependent type systems:

```
MLTT COMPONENTS:

1. TYPE FORMATION RULES: what counts as a type
   A : Type   ("A is a type" is a judgment)

2. INTRODUCTION RULES: how to construct values
   λ (x:A). body : Π (x:A). B(x)    (function introduction)
   (a, b) : Σ (x:A). B(x)            (pair introduction)

3. ELIMINATION RULES: how to use values
   f : Π (x:A). B(x)   →   f a : B(a)    (function application)
   p : Σ (x:A). B(x)   →   p.1 : A, p.2 : B(p.1)  (projection)

4. IDENTITY TYPES (intensional equality):
   Id_A(a, b) : Type   "the type of proofs that a = b in type A"
   refl : Id_A(a, a)   "reflexivity proof"

   If you have a proof p : Id_A(a, b), you can substitute b for a in
   any property P, by "transporting along p" (J eliminator)

INTENSIONAL vs. EXTENSIONAL IDENTITY:
  Intensional (MLTT): proofs of equality are data; there may be multiple
    distinct proofs of the same equality (relevant in HoTT)
  Extensional: if a = b then the proof is trivial (unique); equality reflection
    adds power but makes type-checking undecidable

UNIVERSES (to avoid Russell's paradox):
  Without care: "the type of all types" = Russell's paradox
  MLTT solution: universe hierarchy
    Type₀ : Type₁
    Type₁ : Type₂
    Type₂ : Type₃  ...
  The type of Type₀ is Type₁ (not Type₀ itself)
  → No self-referential paradox
  Coq's Sort/Prop/Set hierarchy is this
```

---

## 3. Coq: Calculus of Inductive Constructions

Coq = CIC (Coquand, Huet, Paulin-Mohring). The CIC extends System F with:
- Dependent types (Π, Σ)
- Universe hierarchy
- **Inductive types** (algebraic data types with induction principles)
- **Tactics language** (proof search via user-provided hints)

```
COQ INDUCTIVE TYPE EXAMPLES:

  Inductive nat : Type :=
  | O : nat
  | S : nat → nat.

  (* nat is defined with two constructors: zero and successor *)
  (* Coq automatically derives: *)
  (* nat_rect : ∀ P:nat→Type, P O → (∀ n, P n → P (S n)) → ∀ n, P n *)
  (* (the induction principle for nat) *)

  Inductive list (A : Type) : Type :=
  | nil : list A
  | cons : A → list A → list A.

  Inductive vec (A : Type) : nat → Type :=
  | vnil : vec A O
  | vcons : ∀ n, A → vec A n → vec A (S n).

  (* vec A n: the index n is a nat value in the type *)
  (* Different constructors give different index values *)
  (* This is an "indexed inductive family" *)

COQ PROOF EXAMPLE:

  Theorem plus_comm : ∀ n m : nat, n + m = m + n.
  Proof.
    intros n m.
    induction n as [| k IHk].
    - (* n = O *) simpl. rewrite <- plus_n_O. reflexivity.
    - (* n = S k *) simpl. rewrite IHk. rewrite plus_n_Sm. reflexivity.
  Qed.

  (* The proof is a program of type ∀ n m : nat, Id_nat(n+m, m+n) *)
  (* Tactics are proof search; the kernel checks the term it produces *)
```

**Coq's termination checking**:
```
FIXPOINT TERMINATION REQUIREMENT:

  Fixpoint fact (n : nat) : nat :=
  match n with
  | O   => 1
  | S k => (S k) * fact k    (* recursive call on k, which is structurally smaller *)
  end.

  Coq requires: recursive calls must be on STRUCTURALLY SMALLER arguments
  (each call uses a constructor-stripped subterm of the original argument)
  → Every structurally recursive function terminates

  For more complex recursion (well-founded, measure-based):
  Use Program Fixpoint with explicit termination proof
  Or use the well-founded recursion combinator

  WHY THIS IS REQUIRED:
  A non-terminating function of type False → False would be
  a circular proof — would make the system inconsistent (prove False)
  Termination = logical consistency
```

---

## 4. Agda

Agda is a dependently typed language based on MLTT with a more Haskell-like syntax. Developed by Ulf Norell (2007).

```
AGDA EXAMPLE: Vector with safe operations

  data Vec (A : Set) : ℕ → Set where
    []  : Vec A zero
    _∷_ : ∀ {n} → A → Vec A n → Vec A (suc n)

  -- Safe head: only callable on non-empty vectors
  head : ∀ {A n} → Vec A (suc n) → A
  head (x ∷ _) = x

  -- Append: type encodes length addition
  _++_ : ∀ {A m n} → Vec A m → Vec A n → Vec A (m + n)
  [] ++ ys = ys
  (x ∷ xs) ++ ys = x ∷ (xs ++ ys)

AGDA'S KEY FEATURES:

1. PATTERN MATCHING as elimination principle
   More natural than explicit J-eliminator
   "With" patterns for auxiliary computations

2. UNIVERSE POLYMORPHISM: Set, Set₁, Set₂, ...
   Functions polymorphic over universe levels

3. CUBICAL AGDA OPTION:
   Implements cubical type theory (Coquand et al.)
   Provides computational content for univalence (HoTT)
   univalence is an AXIOM in standard Agda, but a THEOREM in Cubical Agda

4. COPATTERNS: coinductive definitions by observation
   (defining infinite data by how it responds to projections)
```

---

## 5. Lean 4 and Mathlib

Lean 4 (de Moura, Ullrich, 2021): a new language designed for both proof and programming:

```
LEAN 4 ARCHITECTURE:

  Kernel: dependent type checker (small, trusted)
  Elaborator: type inference, tactic execution, unification
  Metaprogramming: Lean 4 tactics are Lean 4 programs
    (no separate tactic language — macros and elaboration)

MATHLIB: The mathematics library for Lean 4
  Goal: formalize all of undergraduate + graduate mathematics
  Size (2025): ~1.5 million lines of code
  Coverage: algebra, topology, analysis, number theory, combinatorics,
            category theory, algebraic geometry (starting)

EXAMPLE (number theory in Lean 4):

  theorem infinitely_many_primes : ∀ n : ℕ, ∃ p : ℕ, n < p ∧ Nat.Prime p := by
    intro n
    exact Nat.exists_infinite_primes (n + 1)

  -- The Lean proof is a term of type ∀ n : ℕ, ∃ p : ℕ, n < p ∧ Nat.Prime p
  -- Machine-verified by the kernel

LEAN 4 FOR SOFTWARE:
  Can write ordinary programs in Lean 4 (it compiles to C)
  Pure Lean functions can be extracted and run
  Blurs the line between proof and programming (like Coq extraction)
```

---

## 6. Idris 2: Practical Dependent Types

Edwin Brady's Idris 2 (2020): dependent types designed for verified programming, not just proof:

```
IDRIS 2 KEY FEATURES:

1. LINEAR TYPES (Quantitative Type Theory):
   Functions can be annotated with multiplicity:
     0   — zero uses (erased at runtime, compile-time only)
     1   — exactly one use (linear)
     ω   — unrestricted

   Example:
   read : (1 f : File) → IO (String, File)  -- f must be used exactly once
   (prevents: use after close, forgotten handles)

2. PROTOCOLS AS TYPES:
   Door : DoorState → Type
   data DoorState = Open | Closed

   openDoor  : (1 d : Door Closed) → IO (Door Open)
   closeDoor : (1 d : Door Open) → IO (Door Closed)
   readFromDoor : (1 d : Door Open) → IO (String, Door Open)

   State machine encoded in types.
   Cannot read from a closed door; cannot open an already-open door.
   Linear types ensure you can't use a door in the wrong state.

3. FIRST-CLASS TYPES:
   Type is a value; types can be computed at runtime
   (within limits — dependent types require evaluation at compile time)
```

---

## 7. Decidability of Type Checking

```
TYPE-CHECKING WITH DEPENDENT TYPES:

  Checking t : T  requires checking T is a valid type
  T may contain terms: e.g., T = Vec A (f n) where f is a function
  To check Vec A (f n) = Vec A (g m), need to check f n = g m
  → Type equality requires deciding TERM EQUALITY
  → With arbitrary computation in types: undecidable

HOW COQ/AGDA/LEAN HANDLE THIS:

  REDUCTION: both sides reduced to a normal form
             definitional equality = reducibility to same normal form

  TERMINATION CHECKER: guarantees all terms in types normalize
    → Type checking is DECIDABLE given termination checker
    → At the cost of: some valid programs rejected by conservative checker

  EXAMPLE: Coq rejects
    Fixpoint bad n := bad n     (* doesn't terminate *)
  Even if bad is used only at compile time in types.

  SEMI-DECIDABILITY: In general (without termination restriction),
  dependent type checking is Π₂-complete (two-level undecidability)
  → Termination restriction gives decidability

PROOF ASSISTANTS IN CRYPTOGRAPHY:
  EverCrypt (F*): verified implementations of cryptographic primitives
  miTLS: verified TLS 1.3 implementation
  Fiat-Crypto: verified elliptic curve arithmetic (in Coq)
    → Used in Chrome and Firefox (extracted from Coq)
  These are production uses of dependent types for security verification
```

---

## Decision Cheat Sheet

| Feature | Tool | Use case |
|---------|------|---------|
| Mathematical proof | Lean 4 + Mathlib | Formalize mathematics |
| Verified algorithms | Coq | CompCert, Fiat-Crypto |
| Dependent types + patterns | Agda | Type theory research |
| Verified protocols + linear types | Idris 2 | Protocol state machines |
| Length-indexed vectors | All of the above | Array safety |
| Interface state machines | Idris 2 | File handles, network sockets |
| Cryptography verification | F* (Coq subset) | EverCrypt, miTLS |
| Π type | Dependent function | Safe lookup, heterogeneous lists |
| Σ type | Dependent pair | Subset types, protocols |

---

## Common Confusion Points

**Π type and universal quantification are the same**: Π (x:A). B(x) is both "dependent function type" and "for all x:A, there is a B(x)". When A = Nat, it's truly a universally quantified statement about all natural numbers. This unification is the point — computation and logic are the same thing.

**Induction principle ≠ inductive definition**: In Coq, when you define an inductive type like `nat`, Coq automatically generates the induction principle `nat_rect`. The induction principle is the elimination rule for the type. You're not separately specifying induction — it's derived from the type definition.

**Termination checking is conservative**: The structural recursion checker in Coq/Agda accepts only functions where recursive calls use constructor-stripped subterms. Some valid terminating functions are rejected. You can prove termination externally (with `Program Fixpoint` in Coq, explicit measure in Agda) but it's more work.

**Coq extracts to OCaml, not Rust**: Coq's `Extraction` command generates OCaml or Haskell code from proofs. The extracted code runs efficiently but is in a garbage-collected language. For systems code (Rust, C), you verify in Coq and manually implement in the target language (or use tools like F* which targets C).
