---
wave: gold-reset-wave11-sample-2-remediation
date_open: 2026-05-15
date_close: 2026-05-15
status: complete
source_wave: gold-certification-reset
---

# Gold Reset Wave 11 Sample 2 Remediation

## Mission

Repair and re-panel the second Wave 11 medicine/disease sample before restoring
Current Certified Gold.

## Claim Boundary

| Guide | Invariant |
|---|---|
| `medicine/06-CANCER-DRUGS.md` | `cancer-drug-mechanisms` |
| `disease/01-BACTERIAL.md` | `bacterial-disease-gram-classification` |
| `disease/02-VIRAL.md` | `viral-disease-baltimore` |
| `disease/03-FUNGAL-PARASITIC-PRION.md` | `fungal-parasitic-prion-classes` |

## Pulse Status

| Pulse | Status | Governing Roles | Evidence |
|---|---|---|---|
| 01 - Repair and R2 panel | DONE | reference-editor, expert-skeptic, bridge-builder, index-weaver | `panels/r2-wave11-sample-2/R2-consolidated.md` |

## Validation Gates

| Gate | Result |
|---|---|
| Mechanical prerequisite | PASS: `proof.exe check --daVinci -e --no-fail proof.toml <4 guides>` returned OK and output contained no `FAIL` |
| Editorial repair | PASS: cancer drugs, bacterial disease, viral disease, and fungal/parasitic/prion disease cheat sheets rebuilt as diagnostic tables |
| R2 panel | PASS: guide-specific scoring, reader tasks, and adversarial closure recorded |
| Registry update | PASS: only these four repaired guides restored to Current Certified Gold |

## Closeout

Wave 11 sample 2 restores one medicine guide and three disease guides with
reset-era R2 evidence.

