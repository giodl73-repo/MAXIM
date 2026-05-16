---
wave: gold-reset-wave15-sample-1-remediation
date_open: 2026-05-15
date_close: 2026-05-15
status: complete
source_wave: gold-certification-reset
---

# Gold Reset Wave 15 Sample 1 Remediation

## Mission

Repair and re-panel the first programming-language-theory Wave 15 sample before
restoring Current Certified Gold.

## Claim Boundary

| Guide | Invariant |
|---|---|
| `programming-language-theory/01-LAMBDA-CALCULUS.md` | `lambda-calculus-landscape` |
| `programming-language-theory/02-TYPE-THEORY.md` | `type-theory-landscape` |
| `programming-language-theory/03-OPERATIONAL-SEM.md` | `operational-semantics-landscape` |
| `programming-language-theory/04-DENOTATIONAL-SEM.md` | `denotational-semantics-landscape` |

## Pulse Status

| Pulse | Status | Governing Roles | Evidence |
|---|---|---|---|
| 01 - Repair and R2 panel | DONE | reference-editor, expert-skeptic, bridge-builder, index-weaver | `panels/r2-wave15-sample-1/R2-consolidated.md` |

## Validation Gates

| Gate | Result |
|---|---|
| Mechanical prerequisite | PASS: `proof.exe check --daVinci -e --no-fail proof.toml <4 guides>` returned OK and output contained no `FAIL` |
| Editorial repair | PASS: lambda-calculus, type-theory, operational-semantics, and denotational-semantics cheat sheets rebuilt as diagnostic tables |
| R2 panel | PASS: guide-specific scoring, reader tasks, and adversarial closure recorded |
| Registry update | PASS: only these four repaired guides restored to Current Certified Gold |

## Closeout

Wave 15 sample 1 restores four programming-language-theory guides with
reset-era R2 evidence.

