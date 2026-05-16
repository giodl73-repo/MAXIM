---
pulse: 01
title: Repair and R2 Panel
status: complete
---

# Pulse 01 - Repair and R2 Panel

## Scope

- `programming-language-theory/01-LAMBDA-CALCULUS.md`
- `programming-language-theory/02-TYPE-THEORY.md`
- `programming-language-theory/03-OPERATIONAL-SEM.md`
- `programming-language-theory/04-DENOTATIONAL-SEM.md`

## Pre-implementation Scout

The guides were proof-clean and invariant-covered, but retained factory-era
concept, type-system, and machine selector tables. Current Certified Gold
requires diagnostic reader-task support with caveats.

## Changes

| Guide | Repair |
|---|---|
| `programming-language-theory/01-LAMBDA-CALCULUS.md` | Rebuilt the lambda-calculus table around capture, evaluation order, WHNF, encodings, recursion, de Bruijn indices, and lazy/eager performance. |
| `programming-language-theory/02-TYPE-THEORY.md` | Rebuilt the type-theory table around STLC, System F, Hindley-Milner, F-omega, bounded subtyping, structural subtyping, and dependent types. |
| `programming-language-theory/03-OPERATIONAL-SEM.md` | Rebuilt the operational-semantics table around SECD, CEK, Krivine, STG, CPS, and ANF. |
| `programming-language-theory/04-DENOTATIONAL-SEM.md` | Rebuilt the denotational-semantics table around Scott domains, continuity, fixed points, adequacy, full abstraction, game semantics, and CCCs. |

## Gates

| Gate | Status |
|---|---|
| Proof + Da Vinci | PASS |
| Targeted editorial repair | PASS |
| R2 reference-editor panel | PASS |
| Consolidated Gold decision | PASS |

## Validation

```powershell
git --no-pager diff --check -- programming-language-theory\01-LAMBDA-CALCULUS.md programming-language-theory\02-TYPE-THEORY.md programming-language-theory\03-OPERATIONAL-SEM.md programming-language-theory\04-DENOTATIONAL-SEM.md
$proofOut = C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml programming-language-theory\01-LAMBDA-CALCULUS.md programming-language-theory\02-TYPE-THEORY.md programming-language-theory\03-OPERATIONAL-SEM.md programming-language-theory\04-DENOTATIONAL-SEM.md 2>&1; $proofOut; if ($proofOut -match 'FAIL') { exit 1 }
```

Result: PASS.

