---
pulse: 01
title: Repair and R2 Panel
status: complete
---

# Pulse 01 - Repair and R2 Panel

## Scope

- `programming-language-theory/05-CURRY-HOWARD.md`
- `programming-language-theory/06-DEPENDENT-TYPES.md`
- `programming-language-theory/07-EFFECT-SYSTEMS.md`
- `programming-language-theory/08-COMPILER-SEMANTICS.md`

## Pre-implementation Scout

The guides were proof-clean and invariant-covered, but retained factory-era
concept, feature, need, and topic selector tables. Current Certified Gold
requires diagnostic reader-task support with caveats.

## Changes

| Guide | Repair |
|---|---|
| `programming-language-theory/05-CURRY-HOWARD.md` | Rebuilt the table around implication, products, sums, empty types, classical control, continuations, linear implication, unrestricted use, and normalization. |
| `programming-language-theory/06-DEPENDENT-TYPES.md` | Rebuilt the table around Lean, Coq, Agda, Idris, vectors, state machines, F*, Pi types, and Sigma types. |
| `programming-language-theory/07-EFFECT-SYSTEMS.md` | Rebuilt the table around monads, mtl, algebraic effects, OCaml 5, ownership, session types, and capture checking. |
| `programming-language-theory/08-COMPILER-SEMANTICS.md` | Rebuilt the table around CompCert, CPS, SSA, GHC Core, STG, LLVM IR, and partial evaluation. |

## Gates

| Gate | Status |
|---|---|
| Proof + Da Vinci | PASS |
| Targeted editorial repair | PASS |
| R2 reference-editor panel | PASS |
| Consolidated Gold decision | PASS |

## Validation

```powershell
git --no-pager diff --check -- programming-language-theory\05-CURRY-HOWARD.md programming-language-theory\06-DEPENDENT-TYPES.md programming-language-theory\07-EFFECT-SYSTEMS.md programming-language-theory\08-COMPILER-SEMANTICS.md
$proofOut = C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml programming-language-theory\05-CURRY-HOWARD.md programming-language-theory\06-DEPENDENT-TYPES.md programming-language-theory\07-EFFECT-SYSTEMS.md programming-language-theory\08-COMPILER-SEMANTICS.md 2>&1; $proofOut; if ($proofOut -match 'FAIL') { exit 1 }
```

Result: PASS.

