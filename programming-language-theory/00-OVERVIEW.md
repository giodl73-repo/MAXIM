# Programming Language Theory: Foundations and Frontiers — Landscape

## The Big Picture

PLT is the mathematical study of programming languages: what they mean, what they can express, how they ensure correctness. The central unifying insight — the Curry-Howard correspondence — reveals that type systems are logics, programs are proofs, and computation is proof normalization. This is not a metaphor; it is a theorem.

You know lambda calculus. You know type theory from MIT TCS. This module is about where all of that surfaces in production systems — and where the field is going.

```
+--------------------------------------------------------------------------+
|                    PROGRAMMING LANGUAGE THEORY LANDSCAPE                  |
+--------------------------------------------------------------------------+
|                                                                          |
|  FOUNDATIONS (what everything is built on)                               |
|  ┌──────────────────────────────────────────────────────────────────┐   |
|  │  Lambda calculus: universal model of computation                 │   |
|  │  Type theory: logic of programs                                  │   |
|  │  Semantics: mathematical meaning of programs                     │   |
|  └──────────────────────────────────────────────────────────────────┘   |
|              │                    │                   │                  |
|              ▼                    ▼                   ▼                  |
|  OPERATIONAL SEM         DENOTATIONAL SEM        TYPE SAFETY            |
|  How programs run:       What programs mean:     Progress +             |
|  small-step, big-step,   Scott domains,          Preservation:          |
|  abstract machines       fixed points,           typed programs         |
|  (SECD, CEK, STG)        game semantics          don't get stuck        |
|                                                                          |
|  THE CENTRAL UNIFYING INSIGHT: CURRY-HOWARD CORRESPONDENCE               |
|  ┌──────────────────────────────────────────────────────────────────┐   |
|  │  PROPOSITIONS  ────────────────────────────  TYPES               │   |
|  │  PROOFS        ────────────────────────────  PROGRAMS            │   |
|  │  NORMALIZATION ────────────────────────────  EVALUATION          │   |
|  │  IMPLICATION   ────────────────────────────  FUNCTION TYPE A→B   │   |
|  │  CONJUNCTION   ────────────────────────────  PRODUCT TYPE A×B    │   |
|  │  DISJUNCTION   ────────────────────────────  SUM TYPE A+B        │   |
|  └──────────────────────────────────────────────────────────────────┘   |
|                                                                          |
|  MODERN EXTENSIONS (where theory enters production)                      |
|  ┌──────────────┬─────────────────┬──────────────────────────────────┐  |
|  │ DEPENDENT    │ EFFECT          │ GRADUAL TYPING                   │  |
|  │ TYPES        │ SYSTEMS         │ Siek/Taha 2006                   │  |
|  │ Coq, Agda,   │ Algebraic eff., │ TypeScript (industrial)          │  |
|  │ Lean, Idris  │ monads          │ Unsound by design                │  |
|  ├──────────────┼─────────────────┼──────────────────────────────────┤  |
|  │ REFINEMENT   │ SESSION TYPES   │ LINEAR TYPES                     │  |
|  │ TYPES        │ Linear typing   │ Rust ownership                   │  |
|  │ LiquidHaskell│ for protocols   │ Affine types = use once          │  |
|  │ F*, F7       │ Honda 1993      │ Borrow checker                   │  |
|  └──────────────┴─────────────────┴──────────────────────────────────┘  |
+--------------------------------------------------------------------------+
```

---

## Where PLT Shows Up in Production

The theory you studied has direct production counterparts. These are not analogies — they are the same mathematics with different notation:

```
PLT THEORY → PRODUCTION LANGUAGE MAPPING:

Lambda calculus + substitution
    → Every interpreter's core (JavaScript V8, Python CPython)
    → GHC's Core language is literally System Fc (typed lambda calculus)

Hindley-Milner type inference (Algorithm W)
    → Haskell, OCaml, F# type inference
    → The reason you never write types in idiomatic Haskell/OCaml
    → Rust's type inference is HM with extensions

System F (universal quantification ∀α.τ)
    → Java/C# generics (bounded polymorphism variant)
    → Haskell forall (explicit)
    → TypeScript generics (structural variant)

Subtyping + variance
    → TypeScript: structural subtyping throughout
    → Java: covariant arrays (known unsoundness)
    → Kotlin: declaration-site variance (in/out keywords)
    → Scala: variance annotations

Scott domains + fixed points
    → Denotational meaning of recursive programs
    → Haskell's lazy evaluation model
    → Bottom (⊥) as the undefined value

Linear types
    → Rust: ownership system IS affine type system
    → Rust borrow rules ≡ linear type checking rules

Dependent types
    → Coq, Agda, Lean (production verification tools)
    → Ada 2012 (subset via aspects)
    → TypeScript template literal types (a taste)

CPS transform
    → Compilers use CPS or ANF as intermediate representation
    → GHC's STG is a form of CPS
    → V8's deoptimization uses CPS structure

Operational semantics (small-step)
    → Specification of JavaScript semantics (TC39 spec is basically SOS)
    → Rust's reference semantics specified using Stacked Borrows model
```

---

## Module Map

```
+-----------------------------------------------------------------------+
|                    PLT MODULE MAP                                       |
+-----------------------------------------------------------------------+
|                                                                       |
|  01-LAMBDA-CALCULUS   Syntax, substitution, reduction,               |
|                       Church/Scott encoding, Y combinator,           |
|                       CBV/CBN/CBNeed, de Bruijn indices             |
|                                                                       |
|  02-TYPE-THEORY       STLC, System F (∀), Hindley-Milner (let-poly), |
|                       System Fω (HKTs), subtyping, covariance,       |
|                       bounded polymorphism, structural/nominal       |
|                                                                       |
|  03-OPERATIONAL-SEM   Big-step vs. small-step, SECD machine,        |
|                       CEK machine, Krivine, G-machine/STG,          |
|                       CPS, ANF                                       |
|                                                                       |
|  04-DENOTATIONAL-SEM  Scott domains (dcpo), fixed points,           |
|                       adequacy theorem, full abstraction,            |
|                       game semantics, CCCs                          |
|                                                                       |
|  05-CURRY-HOWARD      STLC ↔ propositional logic,                   |
|                       System F ↔ second-order logic,                |
|                       classical logic ↔ CPS, linear logic ↔ Rust   |
|                                                                       |
|  06-DEPENDENT-TYPES   Π/Σ types, MLTT, Coq/CIC, Agda,             |
|                       Idris, Lean, decidability                     |
|                                                                       |
|  07-EFFECT-SYSTEMS    Monads (Moggi), algebraic effects,            |
|                       Haskell effect libraries, capability effects,  |
|                       OCaml 5 effects, linear types and effects     |
|                                                                       |
|  08-COMPILER-SEM      CompCert, CPS/ANF transforms, SSA,           |
|                       GHC pipeline (Core → STG → Cmm),             |
|                       LLVM IR, partial evaluation                   |
|                                                                       |
|  09-MODERN-FRONTIERS  Gradual typing, TypeScript soundness,         |
|                       refinement types (LiquidHaskell, F*),         |
|                       session types, HoTT, cubical type theory      |
+-----------------------------------------------------------------------+
```

---

## The Field's Open Problems

These are genuinely open — not solved:

```
OPEN PROBLEMS IN PLT (as of 2025):

1. SCALING DEPENDENT TYPE CHECKING
   Full decidability requires termination checking
   Termination checking is undecidable in general
   Current systems (Coq, Agda) use conservative approximations
   → Cannot check some valid programs
   → How to extend without losing decidability?

2. EFFECT SYSTEMS AT SCALE
   Monads compose poorly (monad transformer explosion: n effects → 2ⁿ stacks)
   Algebraic effects compose well but have control flow complications
   No consensus on the "right" effect system for mainstream language
   → Scala is experimenting with capture checking
   → OCaml 5 landed effects but design is evolving

3. GRADUAL TYPING AND PERFORMANCE
   Gradual typing requires runtime type checks (casts)
   These checks kill performance
   Typed Racket: progressive elaboration works; performance still a challenge
   TypeScript: erased (no runtime checks) → unsound
   → Can you have sound gradual typing without performance overhead?

4. FULL ABSTRACTION
   Milner's problem (1977): PCFL lacks full abstraction (operational ≡ ≠ denotational ≡)
   Game semantics solved it for sequential languages (Abramsky et al.)
   Still open for higher-order concurrent languages with shared mutable state
   → Rust's ownership model may enable progress here

5. HOMOTOPY TYPE THEORY / UNIVALENT FOUNDATIONS
   Voevodsky's univalence axiom: equivalent types are identical
   Gives computational content to isomorphism (huge for math formalization)
   Cubical type theory gives constructive proof of univalence
   → How to scale Lean/Coq/Agda to all of mainstream mathematics?
   → Mathlib project (Lean 4) is the current frontier

6. LINEAR TYPES AND ALIASING
   Rust's borrow checker is sound but conservative
   (Some valid programs rejected)
   → RustBelt project: formal semantics for Rust's unsafe
   → Stacked Borrows (Miri): operational model for Rust memory
   → Can we make borrow checking less conservative without losing safety?
```

---

## Decision Cheat Sheet

| If you need to understand... | Go to |
|-----------------------------|-------|
| Why Haskell's type inference works | 02-TYPE-THEORY (HM, Algorithm W) |
| What Rust's borrow checker is doing | 05-CURRY-HOWARD (linear types) + 09-MODERN-FRONTIERS |
| TypeScript's unsoundness | 02-TYPE-THEORY (structural typing, covariance) + 09-MODERN-FRONTIERS |
| How GHC compiles Haskell | 03-OPERATIONAL-SEM (STG) + 08-COMPILER-SEM |
| What Coq/Agda/Lean are based on | 06-DEPENDENT-TYPES |
| Where monads come from | 07-EFFECT-SYSTEMS (Moggi) |
| Why CPS is used in compilers | 03-OPERATIONAL-SEM + 08-COMPILER-SEM |
| What "types as propositions" means precisely | 05-CURRY-HOWARD |
| How denotational semantics handles recursion | 04-DENOTATIONAL-SEM (Scott domains, fixed points) |
| Session types and protocol verification | 09-MODERN-FRONTIERS |

---

## Common Confusion Points

**Lambda calculus is not a programming language**: It's a mathematical model of computation. Production languages implement it plus: I/O, mutable state, exceptions, concurrency — all of which require extending the pure calculus (effect systems are the theory of these extensions).

**Type safety (progress + preservation) is not the same as type soundness**: Type safety means "well-typed programs don't get stuck" (no runtime type errors). Type soundness means "the type system correctly tracks the runtime behavior." TypeScript is neither: it's intentionally unsound (some type errors not caught; no runtime checks). Typed Racket aims for soundness at the boundary.

**Curry-Howard is a correspondence, not a compiler**: The correspondence is a deep mathematical relationship between type theories and logics. It doesn't mean every program is a proof of something useful. The correspondence is most directly exploited in Coq, Agda, Lean — where you *are* writing proofs that happen to also be programs.

**HM type inference does not scale to all of System F**: Hindley-Milner inference is decidable and efficient. Type inference for full System F (rank-n polymorphism) is undecidable. GHC extends HM with rank-n types but requires annotations for rank-2+ (the `runST` case). This is why you sometimes need type signatures in Haskell — not because inference fails, but because it can't handle impredicative polymorphism automatically.
