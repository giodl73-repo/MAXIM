---
wave: gold-reset-wave25-sample-3-remediation
date_open: 2026-05-15
date_close: 2026-05-15
status: complete
source_wave: gold-certification-reset
---

# Gold Reset Wave 25 Sample 3 Remediation

## Mission

Repair and re-panel the third Wave 25 sample before restoring Current Certified
Gold across future astrobiology missions and biomedical engineering.

## Claim Boundary

| Guide | Invariant |
|---|---|
| `astrobiology/09-FUTURE-MISSIONS.md` | `astrobiology-mission-pipeline` |
| `biomedical-engineering/02-BIOMATERIALS.md` | `biomaterials-landscape` |
| `biomedical-engineering/03-MEDICAL-IMAGING.md` | `medical-imaging-modalities` |
| `biomedical-engineering/04-BIOSENSORS.md` | `biosensor-architecture` |

## Pulse Status

| Pulse | Status | Governing Roles | Evidence |
|---|---|---|---|
| 01 - Repair and R2 panel | DONE | reference-editor, expert-skeptic, bridge-builder, index-weaver | `panels/r2-wave25-sample-3/R2-consolidated.md` |

## Validation Gates

| Gate | Result |
|---|---|
| Mechanical prerequisite | PASS: `proof.exe check --daVinci -e --no-fail proof.toml <4 guides>` returned OK and output contained no `FAIL` |
| Editorial repair | PASS: future missions, biomaterials, medical imaging, and biosensors cheat sheets rebuilt as diagnostic tables |
| R2 panel | PASS: guide-specific scoring, reader tasks, and adversarial closure recorded |
| Registry update | PASS: only these four repaired guides restored to Current Certified Gold |

## Closeout

Wave 25 sample 3 restores four guides with reset-era R2 evidence.

