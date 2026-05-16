# R2 Reference Editor Panel - Gold Reset Wave 15 Sample 2

## Scope

| Guide | Invariant | Score |
|---|---|---:|
| `programming-language-theory/05-CURRY-HOWARD.md` | `curry-howard-correspondence` | 4.6 |
| `programming-language-theory/06-DEPENDENT-TYPES.md` | `dependent-types-landscape` | 4.6 |
| `programming-language-theory/07-EFFECT-SYSTEMS.md` | `effect-systems-landscape` | 4.6 |
| `programming-language-theory/08-COMPILER-SEMANTICS.md` | `compiler-semantics-landscape` | 4.6 |

## Findings

| Role | Finding | Disposition |
|---|---|---|
| reference-editor | Factory-era selector tables were too lookup-oriented. | Repaired into diagnostic `If you need to diagnose...` tables. |
| expert-skeptic | Advanced PL guidance needs caveats about partial languages, control effects, extraction targets, termination checking, transformer order, effect handlers, CompCert UB boundaries, and partial-evaluation scope. | Added caveats for each diagnostic claim. |
| bridge-builder | Existing guide bodies already bridge proof terms, dependent types, effects, and compiler IRs to production systems. | Preserved bridges; cheat sheets now route diagnostic use. |
| index-weaver | Cross-reference sections were present and proof-clean. | No link rewiring required. |

## Guide Notes

| Guide | Reader-Task Evidence |
|---|---|
| `programming-language-theory/05-CURRY-HOWARD.md` | Reader can diagnose proof/program correspondences by separating implication, products, sums, falsehood, classical control, continuations, linearity, reuse, and normalization. |
| `programming-language-theory/06-DEPENDENT-TYPES.md` | Reader can diagnose dependent-type tool choices by separating mathematics libraries, verified algorithms, research ergonomics, protocols, vectors, state machines, F*, Pi types, and Sigma types. |
| `programming-language-theory/07-EFFECT-SYSTEMS.md` | Reader can diagnose effect-system choices by separating monads, transformer/typeclass stacks, algebraic handlers, resumable effects, ownership, session types, and capture checking. |
| `programming-language-theory/08-COMPILER-SEMANTICS.md` | Reader can diagnose compiler-semantics claims by separating verified compilation, CPS, SSA, Core, STG, LLVM lowering, and partial evaluation. |

## Verdict

PASS. All four guides satisfy Current Certified Gold after reset-era repair,
proof/Da Vinci validation, and guide-specific reader-task review.

