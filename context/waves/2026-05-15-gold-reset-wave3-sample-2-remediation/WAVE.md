---
wave: gold-reset-wave3-sample-2-remediation
date_open: 2026-05-15
date_close: 2026-05-15
status: complete
source_wave: gold-certification-reset
---

# Gold Reset Wave 3 Sample 2 Remediation

## Mission

Repair and re-panel the second Wave 3 topology sample before restoring Current
Certified Gold.

## Claim Boundary

| Guide | Invariant |
|---|---|
| `topology/05-CONNECTEDNESS.md` | `connectedness-hierarchy` |
| `topology/06-FUNDAMENTAL-GROUP.md` | `fundamental-group-loops` |
| `topology/08-COHOMOLOGY.md` | `cohomology-dual-ring-structure` |
| `topology/09-MANIFOLDS.md` | `manifolds-locally-euclidean` |

## Pulse Status

| Pulse | Status | Governing Roles | Evidence |
|---|---|---|---|
| 01 - Repair and R2 panel | DONE | reference-editor, expert-skeptic, bridge-builder, index-weaver | `panels/r2-wave3-sample-2/R2-consolidated.md` |

## Validation Gates

| Gate | Result |
|---|---|
| Mechanical prerequisite | PASS: `proof.exe check --daVinci -e --no-fail proof.toml <4 guides>` returned OK and output contained no `FAIL` |
| Editorial repair | PASS: connectedness, fundamental-group, cohomology, and manifolds decision tables rebuilt as diagnostic tables |
| R2 panel | PASS: guide-specific scoring, reader tasks, and adversarial closure recorded |
| Registry update | PASS: only these four repaired guides restored to Current Certified Gold |

## Closeout

Wave 3 sample 2 restores four topology guides with reset-era R2 evidence.

