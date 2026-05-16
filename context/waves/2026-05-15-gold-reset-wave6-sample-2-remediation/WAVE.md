---
wave: gold-reset-wave6-sample-2-remediation
date_open: 2026-05-15
date_close: 2026-05-15
status: complete
source_wave: gold-certification-reset
---

# Gold Reset Wave 6 Sample 2 Remediation

## Mission

Repair and re-panel the second Wave 6 PDE sample before restoring Current
Certified Gold.

## Claim Boundary

| Guide | Invariant |
|---|---|
| `partial-differential-equations/05-LAPLACE-POISSON.md` | `laplace-poisson-landscape` |
| `partial-differential-equations/06-FOURIER-METHODS.md` | `fourier-methods-pde-landscape` |
| `partial-differential-equations/07-GREENS-FUNCTIONS.md` | `greens-function-concept` |
| `partial-differential-equations/08-VARIATIONAL-WEAK.md` | `weak-formulation-concept` |

## Pulse Status

| Pulse | Status | Governing Roles | Evidence |
|---|---|---|---|
| 01 - Repair and R2 panel | DONE | reference-editor, expert-skeptic, bridge-builder, index-weaver | `panels/r2-wave6-sample-2/R2-consolidated.md` |

## Validation Gates

| Gate | Result |
|---|---|
| Mechanical prerequisite | PASS: `proof.exe check --daVinci -e --no-fail proof.toml <4 guides>` returned OK and output contained no `FAIL` |
| Editorial repair | PASS: Laplace/Poisson, Fourier methods, Green's functions, and weak-form decision tables rebuilt as diagnostic tables |
| R2 panel | PASS: guide-specific scoring, reader tasks, and adversarial closure recorded |
| Registry update | PASS: only these four repaired guides restored to Current Certified Gold |

## Closeout

Wave 6 sample 2 restores four PDE guides with reset-era R2 evidence.

