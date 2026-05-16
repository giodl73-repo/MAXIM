---
wave: gold-reset-wave14-sample-5-remediation
date_open: 2026-05-15
date_close: 2026-05-15
status: complete
source_wave: gold-certification-reset
---

# Gold Reset Wave 14 Sample 5 Remediation

## Mission

Repair and re-panel the fifth Wave 14 sample across materials and
natural-sciences before restoring Current Certified Gold.

## Claim Boundary

| Guide | Invariant |
|---|---|
| `materials/04-METALS-ALLOYS.md` | `metals-alloys-landscape` |
| `materials/06-NANOMATERIALS.md` | `nanomaterials-landscape` |
| `materials/09-COMPUTATIONAL-MATERIALS.md` | `multiscale-materials-simulation` |
| `natural-sciences/10-CELL-BIOLOGY.md` | `prokaryote-eukaryote-comparison` |

## Pulse Status

| Pulse | Status | Governing Roles | Evidence |
|---|---|---|---|
| 01 - Repair and R2 panel | DONE | reference-editor, expert-skeptic, bridge-builder, index-weaver | `panels/r2-wave14-sample-5/R2-consolidated.md` |

## Validation Gates

| Gate | Result |
|---|---|
| Mechanical prerequisite | PASS: `proof.exe check --daVinci -e --no-fail proof.toml <4 guides>` returned OK and output contained no `FAIL` |
| Editorial repair | PASS: metals-alloys, nanomaterials, computational-materials, and cell-biology cheat sheets rebuilt as diagnostic tables |
| R2 panel | PASS: guide-specific scoring, reader tasks, and adversarial closure recorded |
| Registry update | PASS: only these four repaired guides restored to Current Certified Gold |

## Closeout

Wave 14 sample 5 restores three materials guides and one natural-sciences guide
with reset-era R2 evidence.

