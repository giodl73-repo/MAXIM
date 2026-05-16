# R2 Reference Editor Panel - Gold Reset Wave 15 Sample 1

## Scope

| Guide | Invariant | Score |
|---|---|---:|
| `programming-language-theory/01-LAMBDA-CALCULUS.md` | `lambda-calculus-landscape` | 4.6 |
| `programming-language-theory/02-TYPE-THEORY.md` | `type-theory-landscape` | 4.6 |
| `programming-language-theory/03-OPERATIONAL-SEM.md` | `operational-semantics-landscape` | 4.6 |
| `programming-language-theory/04-DENOTATIONAL-SEM.md` | `denotational-semantics-landscape` | 4.6 |

## Findings

| Role | Finding | Disposition |
|---|---|---|
| reference-editor | Factory-era selector tables were too lookup-oriented. | Repaired into diagnostic `If you need to diagnose...` tables. |
| expert-skeptic | PL theory guidance needs caveats about termination, WHNF, inference decidability, effect restrictions, machine sharing, CPS/ANF interpretation, and adequacy versus full abstraction. | Added caveats for each diagnostic claim. |
| bridge-builder | Existing guide bodies already bridge lambda calculus, type theory, operational machines, and semantic domains to production language implementation. | Preserved bridges; cheat sheets now route diagnostic use. |
| index-weaver | Cross-reference sections were present and proof-clean. | No link rewiring required. |

## Guide Notes

| Guide | Reader-Task Evidence |
|---|---|
| `programming-language-theory/01-LAMBDA-CALCULUS.md` | Reader can diagnose lambda-calculus implementation issues by separating capture, evaluation equivalence, WHNF, encodings, recursion, indices, and lazy/eager sharing. |
| `programming-language-theory/02-TYPE-THEORY.md` | Reader can diagnose type-system choices by separating STLC, System F, HM inference, higher kinds, bounded subtyping, structural typing, and dependent types. |
| `programming-language-theory/03-OPERATIONAL-SEM.md` | Reader can diagnose operational models by separating SECD, CEK, Krivine, STG, CPS, and ANF use cases with caveats. |
| `programming-language-theory/04-DENOTATIONAL-SEM.md` | Reader can diagnose semantic-model claims by separating domains, continuity, fixed points, adequacy, full abstraction, game semantics, and categorical correspondence. |

## Verdict

PASS. All four guides satisfy Current Certified Gold after reset-era repair,
proof/Da Vinci validation, and guide-specific reader-task review.

