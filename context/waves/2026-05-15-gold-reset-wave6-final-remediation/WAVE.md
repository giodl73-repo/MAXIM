---
wave: gold-reset-wave6-final-remediation
date_open: 2026-05-15
date_close: 2026-05-15
status: complete
source_wave: gold-certification-reset
---

# Gold Reset Wave 6 Final Remediation

## Mission

Repair and re-panel the final Wave 6 numerical-PDE and variational-calculus
sample before restoring Current Certified Gold.

## Claim Boundary

| Guide | Invariant |
|---|---|
| `partial-differential-equations/09-NUMERICAL-PDES.md` | `numerical-pde-methods-landscape` |
| `variational-calculus/01-FUNCTIONALS.md` | `functionals-vs-functions` |
| `variational-calculus/02-EULER-LAGRANGE.md` | `euler-lagrange-equation` |
| `variational-calculus/03-CONSTRAINTS.md` | `constrained-variation` |

## Pulse Status

| Pulse | Status | Governing Roles | Evidence |
|---|---|---|---|
| 01 - Repair and R2 panel | DONE | reference-editor, expert-skeptic, bridge-builder, index-weaver | `panels/r2-wave6-final/R2-consolidated.md` |

## Validation Gates

| Gate | Result |
|---|---|
| Mechanical prerequisite | PASS: `proof.exe check --daVinci -e --no-fail proof.toml <4 guides>` returned OK and output contained no `FAIL` |
| Editorial repair | PASS: numerical-PDE and variational-calculus decision tables rebuilt as diagnostic tables |
| R2 panel | PASS: guide-specific scoring, reader tasks, and adversarial closure recorded |
| Registry update | PASS: only these four repaired guides restored to Current Certified Gold |

## Closeout

Wave 6 final restores one numerical-PDE guide and three variational-calculus
guides with reset-era R2 evidence.

