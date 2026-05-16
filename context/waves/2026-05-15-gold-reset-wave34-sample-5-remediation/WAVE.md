---
wave: gold-reset-wave34-sample-5-remediation
date_open: 2026-05-15
date_close: 2026-05-15
status: complete
source_wave: gold-certification-reset
---

# Gold Reset Wave 34 Sample 5 Remediation

## Mission

Continue Wave 34 reset review with the final entomology cohort: repair
substantive editorial defects, validate proof/Da Vinci coverage, and restore
Certified Gold only with guide-specific R2 evidence.

## Claim Boundary

This wave certifies only:

| Guide | Invariant |
|---|---|
| `entomology/07-INSECT-ECOLOGY.md` | `insect-ecology-levels` |
| `entomology/08-ECONOMIC-ENTOMOLOGY.md` | `economic-entomology-framework` |
| `entomology/09-FORENSIC-MEDICAL.md` | `entomology-human-welfare-interface` |

It does not restore Gold to the wider Wave 34 factory backlog.

## Pulse Status

| Pulse | Status | Governing Roles | Evidence |
|---|---|---|---|
| 01 - Repair and R2 panel | DONE | reference-editor, expert-skeptic, bridge-builder, index-weaver | `panels/r2-wave34-sample-5/R2-consolidated.md` |

## Validation Gates

| Gate | Result |
|---|---|
| Mechanical prerequisite | PASS: `proof.exe check --daVinci -e --no-fail proof.toml <3 guides>` returned OK and output contained no `FAIL` |
| Editorial repair | PASS: insect ecology, economic entomology, and forensic/medical diagnostic tables rebuilt; overstrong ecology, pest, threshold, and PMI claims corrected |
| R2 panel | PASS: guide-specific scores, reader tasks, and adversarial closure recorded |
| Registry update | PASS: only the three repaired entomology guides restored to Current Certified Gold |

## Closeout

This sample continues Wave 34 reset with scoped certification backed by
reset-era repair, skeptical review, and reader-task evidence.

