# Theorem Proving and Proof Assistants

## The Big Picture

Proof assistants are type checkers for mathematics. You write a term, the kernel
checks its type. A proof is a term whose type is the proposition being proved.

```
+--------------------------------------------------------------------------+
|                    PROOF ASSISTANT LANDSCAPE                             |
|                                                                            |
|  FOUNDATION         TOOL           ECOSYSTEM        PRIMARY USE          |
|  ──────────         ────           ─────────        ───────────          |
|                                                                            |
|  CIC (Coq)          Coq 8.x        Coq stdlib,      Compilers,           |
|  Calculus of        (INRIA)        MathComp, CF     math, program        |
|  Inductive Const.                  Coquelicot       extraction           |
|                                                                            |
|  MLTT + univ.       Lean 4         Mathlib4         Mathematics          |
|  (Lean 4)           (2021+)        (>100k thms)     software (growing)   |
|                                                                            |
|  HOL (Church)       Isabelle/HOL   AFP (Archive     OS kernels,          |
|  Higher-order       (TU Munich)    of Formal        crypto proofs,       |
|  logic              (Paulson)      Proofs)          CS theory            |
|                                                                            |
|  HOL (Church)       HOL4           CakeML compiler  Compilers,           |
|  LCF style          (Edinburgh/    ARM/x86 ISA      hardware,            |
|                     Cambridge)     proofs           low-level systems    |
|                                                                            |
|  Simple HOL         HOL Light      Flyspeck (Kepler)Formal math          |
|  LCF minimal        (Harrison,     geometry         proofs               |
|                     Intel/MSR)                                           |
+--------------------------------------------------------------------------+

  All proof assistants share this architecture:
  ┌──────────────────────────────────────────────────────────────┐
  │  TACTIC LAYER  (user-facing: automation, search, tactics)    │
  │       |                                                        │
  │  ELABORATOR    (fills implicit arguments, type inference)    │
  │       |                                                        │
  │  KERNEL        (the trusted core — checks proof terms)       │
  │       |                                                        │
  │  LOGIC         (type theory or higher-order logic)           │
  └──────────────────────────────────────────────────────────────┘

  Only the kernel needs to be trusted.
  Thousands of lines of tactics can be buggy — the kernel catches errors.
  Coq kernel: ~3000 lines OCaml. Lean 4 kernel: ~3000 lines C++.
```

---

## The LCF Architecture: Trust Through Minimalism

Edinburgh LCF (1979, Milner et al.) established the architecture still used today.

```
  Problem: How do you trust a large proof automation system?

  LCF answer: Make the trusted core TINY.
              Everything else is untrusted but checkable.

  +-----------------------------------+
  | UNTRUSTED LAYER (arbitrary code)  |
  | - Tactics                         |
  | - Search procedures               |
  | - Decision procedures             |
  | - Imported libraries              |
  +-----------------------------------+
              | produces
              v
  +-----------------------------------+
  | TRUSTED KERNEL (abstract type)    |
  | - Proof term: an abstract type    |
  | - Only derivation rules can       |
  |   construct values of type "thm"  |
  | - Kernel validates EVERY step     |
  | - Cannot forge a theorem          |
  +-----------------------------------+

  The key insight: the kernel is an abstract type in the
  implementation language (ML, OCaml, Haskell). The type
  system prevents forgery — you cannot produce a value of
  type "thm" (theorem) without going through the inference rules.

  This means: a bug in automation code produces a type error,
  not a false proof. Security through types.
```

---

## Curry-Howard Correspondence

The deep connection between type theory and logic. You know lambda calculus from MIT —
this is the bridge to proof assistants:

```
  LOGIC                          TYPE THEORY                  PROGRAM
  ─────                          ───────────                  ───────
  Proposition P                  Type A                       Set of values
  Proof of P                     Term t : A                   Program of type A
  P /\ Q  (conjunction)          A × B  (product type)        Pair
  P \/ Q  (disjunction)          A + B  (sum type)            Either/variant
  P -> Q  (implication)          A -> B (function type)       Function
  True                           Unit type                    ()
  False                          Empty type                   Void
  Forall x:D. P(x)               Pi type (x:D) -> P(x)        Dep. function
  Exists x:D. P(x)               Sigma type (x:D) × P(x)      Dep. pair
  Not P = P -> False             A -> Void                    Diverging function

  Proof of P is a PROGRAM of type P.
  Type-checking is proof-checking.
  Running the program is... not well-defined (proofs aren't run).

  In a proof assistant:
  - Writing a proof = writing a term (program)
  - Checking the proof = type-checking the term
  - A type error = an invalid proof step

  Coq's `Prop` sort: propositions as types, but proofs are erased
  at extraction time. You prove using Prop, extract code using Type.
```

### Curry-Howard-Lambek: The Triple Correspondence

```
  LOGIC         TYPE THEORY      CATEGORY THEORY
  ─────         ───────────      ───────────────
  Propositions  Types            Objects
  Proofs        Programs         Morphisms
  Proof norm.   Reduction        Composition
  Conjunction   Product          Product object
  Implication   Function space   Exponential object
  Hypothesis    Variable         Identity morphism
  Cut rule      Substitution     Composition

  Practical implication: proof assistants are programming languages.
  Writing proofs = programming in a dependently-typed language.
  This is not a metaphor — it is the implementation.
```

---

## Coq: The Calculus of Inductive Constructions

### Core Type Theory

Coq is based on CIC (Calculus of Inductive Constructions), which extends STLC with:

```
  STLC          + Dependent types     (Pi and Sigma types)
                + Inductive types     (nat, list, tree, etc.)
                + A universe hierarchy (Type0 : Type1 : Type2 : ...)
                + Prop (impredicative, proof-irrelevant sort)
                + Set  (computational data)

  Universe hierarchy prevents Russell's paradox:
  Type : Type would be inconsistent (Girard's paradox).
  Solution: Type_i : Type_{i+1}. Coq handles this automatically.

  Inductive types (examples):
  Inductive nat : Set :=
  | O : nat
  | S : nat -> nat.

  Inductive list (A : Type) : Type :=
  | nil : list A
  | cons : A -> list A -> list A.

  Inductive Eq (A : Type) (x : A) : A -> Prop :=
  | refl : Eq A x x.
  (* Propositional equality *)
```

### Tactics and Proof Scripts

In Coq, users write proof scripts (tactic sequences) that construct proof terms:

```coq
Theorem plus_comm : forall n m : nat, n + m = m + n.
Proof.
  intros n m.          (* introduce hypotheses *)
  induction n as [| n' IHn'].
  - (* base case: n = 0 *)
    simpl.             (* simplify: 0 + m = m *)
    rewrite Nat.add_0_r.
    reflexivity.
  - (* inductive case: n = S n' *)
    simpl.             (* (S n') + m = S (n' + m) *)
    rewrite IHn'.      (* use induction hypothesis *)
    rewrite Nat.add_succ_r.
    reflexivity.
Qed.

(* What actually happened:
   The tactics constructed a proof term of type:
   forall n m : nat, n + m = m + n
   The kernel checked the term.
   Qed = accept the proof. *)
```

### Code Extraction

Coq can extract verified algorithms to OCaml or Haskell:

```coq
(* Define a verified sorting algorithm *)
Require Import List Sorting.

Fixpoint insert (x : nat) (l : list nat) : list nat :=
  match l with
  | [] => [x]
  | y :: t => if x <=? y then x :: l else y :: insert x t
  end.

Theorem insert_sorted : forall x l,
  Sorted l -> Sorted (insert x l).
(* ... proof ... *)

(* Extract to OCaml: *)
Extraction "sort.ml" insert.
(* Generates: sort.ml with verified OCaml code *)
```

---

## Lean 4: Modern Dependent Type Theory

Lean 4 (2021) is a redesign that makes the proof assistant also a programming language.
It is currently the most active research PA and has the best library coverage for mathematics.

### Type Theory

```
  Lean 4 uses Martin-Lof Type Theory with:
  - Universes: Prop, Type 0, Type 1, ...
  - Dependent Pi types: (x : A) -> B x
  - Sigma types: (x : A) × B x  (or { x : A // B x })
  - Inductive types (generalized)
  - Quotient types (built-in)
  - Classical axioms in Mathlib (law of excluded middle, choice)

  Prop is proof-irrelevant (all proofs of P are equal).
  Type 0 is the computational universe (programs live here).
  Universe polymorphism: functions can work across universes.
```

### Lean 4 Syntax

```lean
-- Dependent function type: list whose length is specified
def vecHead {α : Type} {n : Nat} (v : Vector α (n + 1)) : α :=
  v.head   -- type: Vector α (n+1) -> α
           -- length is in the TYPE, so empty vector is a type error

-- Proof example: commutativity of addition
theorem Nat.add_comm (m n : Nat) : m + n = n + m := by
  induction m with
  | zero =>
    simp [Nat.zero_add]
  | succ m ih =>
    rw [Nat.succ_add, ih, Nat.add_succ]

-- Tactic proof vs term-mode proof:
-- Tactic mode (above): write proof steps
-- Term mode: write the proof term directly
theorem and_comm (p q : Prop) : p ∧ q -> q ∧ p :=
  fun ⟨hp, hq⟩ => ⟨hq, hp⟩
-- This IS the proof term. No tactics needed for simple cases.
```

### Mathlib4: The Mathematics Library

```
  Mathlib4 (2024 stats):
  - >100,000 theorems formalized
  - Covers: number theory, algebra (groups, rings, fields, modules),
    topology, analysis (real, complex, functional), measure theory,
    combinatorics, category theory, differential geometry

  Notable achievements:
  - Fermat's Last Theorem prerequisites (modularity theorem machinery)
  - Perfectoid spaces (Peter Scholze's 2018 Fields Medal work)
  - Sphere Eversion formalized
  - Polynomial Freiman-Ruzsa conjecture (Lean proof 2023)

  Lean 4 as AI target:
  - AlphaProof (Google DeepMind, 2024): solved 4/6 IMO problems
    using Lean 4 as the proof language
  - Many theorem-proving LLMs target Lean 4 specifically
    because of Mathlib coverage
```

---

## Isabelle/HOL: Higher-Order Logic

Isabelle/HOL uses a different foundation than Coq/Lean. It is based on classical
Higher-Order Logic (HOL), which is simpler (no dependent types) but powerful enough
for almost all of mathematics.

### Architecture

```
  Isabelle = generic theorem proving framework
  Isabelle/HOL = instantiation with HOL as the logic

  HOL foundation:
  - Simply-typed lambda calculus (STLC)
  - Axioms for function extensionality, choice, infinity
  - Boolean type (Prop)
  - Classical: excluded middle is an axiom
  - Quantifiers: All x. P x, Ex x. P x

  Isar proof language:
  (Human-readable structured proofs)

  theorem add_comm: "m + n = n + (m :: nat)"
  proof (induction m)
    case 0
    show "0 + n = n + 0" by simp
  next
    case (Suc m)
    then show "Suc m + n = n + Suc m" by simp
  qed

  Sledgehammer:
  - Calls external first-order ATPs (Vampire, E, Prover9)
  - Translates HOL goal to first-order problem
  - ATP finds a proof
  - Isabelle reconstructs the proof internally (for soundness)
  - Massively increases automation: "press Sledgehammer, get a proof"
```

### Archive of Formal Proofs (AFP)

```
  AFP (isabelle.in.tum.de/afp/):
  - ~700+ formalized theories (2024)
  - Notable entries:
    - Godel's Incompleteness Theorems (Shannon)
    - JinjaThreads (Java bytecode semantics)
    - CryptHOL (cryptographic game-based proofs)
    - DFS/BFS algorithms with correctness proofs
    - Gauss Jordan elimination
    - Abstract algebra hierarchy
    - seL4 functional correctness proof
```

---

## Landmark Large-Scale Proofs

### CompCert: The Verified C Compiler (Leroy, INRIA)

```
  What: A C compiler (ISO C99 subset) formally verified in Coq.

  Proof theorem:
  "If the source program has defined behavior,
   the compiled program has the same observable behavior."

  Scale: ~100,000 lines of Coq
         ~3000 lines of unverified OCaml (parser, pretty printer)

  Architecture:
  C source -> CompCert C -> Clight -> Cminor -> RTL -> LTL -> Linear
                  (multiple intermediate languages, each with
                   formal semantics, and forward simulation proofs
                   between each adjacent pair)

  Deployment:
  - Airbus A350/A380 fly-by-wire software (via DO-178C tools)
  - Nuclear plant safety systems (CEA LIST tools)
  - Cryptographic implementations (where LLVM optimizations
    could break constant-time properties)

  Key insight: the verified compiler closes the gap between
  "we proved the source code correct" and "the binary is correct."
  Without a verified compiler, optimizations can break proofs.
```

### seL4: The Verified OS Microkernel

```
  What: L4-family microkernel, ~10k LOC C.

  Proof chain (Isabelle/HOL):
  Abstract spec (Isabelle/HOL)
    |  functional correctness proof
    v
  Executable spec (Haskell)   <- prototype + spec in one
    |  refinement proof
    v
  C implementation            <- actual kernel source
    |  (binary analysis + CompCert-based)
    v
  ARM binary executable

  Properties proven (with trust assumptions):
  1. Functional correctness: every system call implements its spec
  2. Integrity: one domain cannot write another domain's memory
  3. Confidentiality: information cannot flow between domains
  4. Availability: (partial) no resource starvation
  5. WCET bounds (on specific configs)

  Trust assumptions (the TCB):
  - Isabelle/HOL kernel is correct
  - ARM assembly semantics used are correct
  - Hardware behaves as specified (no microarchitectural attacks)
  - Hardware correctly initializes (bootloader)

  Cost: 11 person-years initial, ~1M lines of Isabelle proof
  Deployed: F/A-18 avionics (Boeing), DARPA HACMS, Northrop Grumman
```

### Four-Color Theorem (Gonthier, 2005)

```
  What: Every planar map can be colored with 4 colors such that
        no two adjacent regions have the same color.

  History:
  - Appel & Haken (1976): proof by computer enumeration of 1,936
    reducible configurations. Controversial: how to trust the code?
  - Gonthier (2005): formalized in Coq. 60,000 lines of Coq proof.
    Entirely checkable by the kernel.

  Key contribution: not just proving the theorem, but developing
  techniques for large-scale formalization in Coq.
  Led to: MathComp library (ssreflect tactic language).
```

### Feit-Thompson Odd Order Theorem (Coq, 2012)

```
  What: Every finite group of odd order is solvable.
  Original proof (1963): 255 pages, one of longest proofs at the time.

  Coq formalization (Gonthier et al., 2012):
  - ~170,000 lines of Coq
  - 6 years of work by a team of researchers
  - Required developing substantial group theory in Coq first

  Significance: demonstrates proof assistants can handle
  serious graduate-level mathematics, not just textbook results.
```

---

## Proof Engineering Workflow

For software verification (not pure mathematics):

```
  ┌────────────────────────────────────────────────────────────────┐
  │  1. SPECIFY: Write formal spec in proof assistant              │
  │     - Define data types (states, operations)                   │
  │     - State invariants (what must always hold)                 │
  │     - State functional spec (what each function should do)     │
  ├────────────────────────────────────────────────────────────────┤
  │  2. IMPLEMENT: Write or import the implementation             │
  │     - Can be in the PA's language (Coq Gallina, Lean 4)       │
  │     - Can be external C/Rust + axiomatized interface          │
  ├────────────────────────────────────────────────────────────────┤
  │  3. PROVE: Construct the proofs                                │
  │     - Start with easy lemmas (typing, structural)              │
  │     - Work toward the main theorem                             │
  │     - Use automation: simp, omega, decide, Sledgehammer        │
  │     - Hand-prove complex inductive cases                       │
  ├────────────────────────────────────────────────────────────────┤
  │  4. EXTRACT (if applicable): Export to target language        │
  │     - Coq -> OCaml/Haskell                                    │
  │     - Lean 4 -> Lean executable (it's also a PL)              │
  │     - Otherwise: use proof as certification + manual impl.    │
  ├────────────────────────────────────────────────────────────────┤
  │  5. MAINTAIN: Proofs must be updated when code changes         │
  │     This is the ongoing cost — proofs are brittle to change.   │
  │     Proof refactoring is real work.                            │
  └────────────────────────────────────────────────────────────────┘
```

---

## Automation Layers

```
  LEVEL 0: Type checking
  The kernel verifies every step. You provide explicit proof terms.
  Used only when debugging or for very simple proofs.

  LEVEL 1: Basic tactics
  apply, intro, rewrite, induction, constructor, exact, assumption
  Works for straightforward structural proofs.

  LEVEL 2: Arithmetic/decision procedures
  omega, linarith, ring, field, decide, norm_num
  Fully automated for linear arithmetic, ring equalities, finite computations.

  LEVEL 3: Simplification
  simp, simp_all, aesop (Lean 4), auto (Isabelle), crush (Coq)
  Applies lemma databases + rewrite rules automatically.
  Often closes easy goals; sometimes sends you in circles.

  LEVEL 4: SMT oracles
  Lean 4: native_decide (compiles + runs decision procedures)
  Isabelle: Sledgehammer -> calls Z3/CVC5/Vampire/E
  Coq: Z3 plugin via coq-hammer
  These call external solvers, return justifications for kernel to check.

  LEVEL 5: First-order ATP
  Sledgehammer (Isabelle) -> Vampire, E, Prover9
  Translates HOL goal to FOL, ATPs search for proofs,
  Isabelle reconstructs proof in HOL for soundness.
  Works for ~40% of "interesting" goals automatically.
```

---

## Auto-Active Verification: Dafny

Dafny occupies a different tier from Coq/Lean/Isabelle: you write annotated code (pre/postconditions, loop invariants, decreases clauses) and Z3 discharges proof obligations automatically. No tactic scripting. This is the most accessible entry point to deductive verification for working engineers.

```
DAFNY MODEL:
  Code + annotations → verification conditions (VCs) → Z3 solver

  method Max(a: int, b: int) returns (r: int)
    ensures r >= a && r >= b        // postcondition
    ensures r == a || r == b        // result is one of the inputs
  {
    if a >= b { r := a; } else { r := b; }
  }
  // Z3 automatically proves both postconditions hold.

  KEY CONCEPTS:
  Ghost variables:  exist only for verification, erased at compile time
  Loop invariants:  must hold before and after each iteration
  Decreases clause: proves termination (well-founded ordering)
  Preconditions:    what the caller must guarantee (requires)
  Postconditions:   what the method guarantees (ensures)

  COMPARISON TO HOARE TRIPLES:
  {P} S {Q} — Dafny automates the proof of {P}S{Q} via VC generation + SMT.
  The programmer writes P and Q; Dafny+Z3 verify S connects them.
  vs. Coq/Lean: programmer writes both the code and the proof interactively.

  PRACTICAL SCOPE:
  Excellent for: algorithm correctness, data structure invariants, API contracts.
  Not designed for: deep mathematical proofs (use Lean/Coq) or hardware (use HOL/Isabelle).
  Microsoft-built (MSR); used in AWS (Zelkova), VMware, and academic verification courses.
```

---

## Decision Cheat Sheet

| Situation | Tool |
|-----------|------|
| Verifying a distributed algorithm (infinite state) | Lean 4 or Coq (or TLA+ TLAPS for lighter proofs) |
| Verifying a compiler or language runtime | Coq (CompCert precedent, large ecosystem) |
| Verifying an OS kernel / security architecture | Isabelle/HOL (seL4 precedent) |
| Formalizing mathematics | Lean 4 + Mathlib (largest library, fastest) |
| Verifying cryptographic protocol game-based | CryptHOL (Isabelle) or EasyCrypt |
| Extracting verified OCaml/Haskell code | Coq (extraction) or HOL4 (for CakeML) |
| Lightweight algorithm verification in CI | Dafny (Z3-based, lighter learning curve) |
| Need fast iteration on proofs | Lean 4 (best IDE support, fast elaborator) |
| Historical academic literature | Isabelle (most AFP entries, Sledgehammer) |

---

## Common Confusion Points

**"Proof assistants are for mathematicians, not engineers"**

CompCert, seL4, CryptoVerif, and Dafny are engineering tools. The distinction is
fading — Lean 4 is simultaneously a proof assistant and a general-purpose language.

**"Tactics are the proofs"**

Tactics construct proof terms. The actual proof is the term; tactics are the
program that builds it. If tactics are buggy, the kernel rejects the term.
You can always inspect the underlying proof term.

**"Classical logic breaks constructive proofs / program extraction"**

In Coq: classical axioms (law of excluded middle, axiom of choice) live in Prop,
which is proof-irrelevant and erased at extraction. If you only use classical
reasoning in Prop and constructive reasoning in Set/Type, extraction still works.
Lean 4 Mathlib uses classical logic pervasively — it is not designed for extraction.

**"A verified compiler means the binary is always correct"**

CompCert's guarantee: the compiled binary has the same observable behavior as
the source (for defined-behavior C). It does not guarantee:
- The source is correct (that's a separate proof)
- The hardware is correct
- The OS is correct
- Side-channel attacks are prevented (constant-time not guaranteed)

**"seL4 means the OS cannot be compromised"**

seL4's proofs assume the hardware behaves correctly, the assembly semantics is
accurate, and there are no hardware side channels. Spectre/Meltdown violate the
hardware assumption. The proof is correct relative to its stated trust base.
