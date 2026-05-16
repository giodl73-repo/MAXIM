---
wave: gold-reset-wave13-final-remediation
date_open: 2026-05-15
date_close: 2026-05-15
status: complete
source_wave: gold-certification-reset
---

# Gold Reset Wave 13 Final Remediation

## Mission

Repair and re-panel the final Wave 13 natural-sciences biology sample before
restoring Current Certified Gold.

## Claim Boundary

| Guide | Invariant |
|---|---|
| `natural-sciences/06-BIOMOLECULES.md` | `biomolecule-four-classes` |
| `natural-sciences/07-ENZYMES.md` | `enzymology-landscape` |
| `natural-sciences/08-METABOLISM.md` | `cellular-metabolic-map` |
| `natural-sciences/09-MOLECULAR-BIO.md` | `molecular-biology-central-dogma` |

## Pulse Status

| Pulse | Status | Governing Roles | Evidence |
|---|---|---|---|
| 01 - Repair and R2 panel | DONE | reference-editor, expert-skeptic, bridge-builder, index-weaver | `panels/r2-wave13-final/R2-consolidated.md` |

## Validation Gates

| Gate | Result |
|---|---|
| Mechanical prerequisite | PASS: `proof.exe check --daVinci -e --no-fail proof.toml <4 guides>` returned OK and output contained no `FAIL` |
| Editorial repair | PASS: biomolecules, enzymes, metabolism, and molecular biology cheat sheets rebuilt as diagnostic tables |
| R2 panel | PASS: guide-specific scoring, reader tasks, and adversarial closure recorded |
| Registry update | PASS: only these four repaired guides restored to Current Certified Gold |

## Closeout

Wave 13 final remediation restores the remaining natural-sciences biology guides
with reset-era R2 evidence.

