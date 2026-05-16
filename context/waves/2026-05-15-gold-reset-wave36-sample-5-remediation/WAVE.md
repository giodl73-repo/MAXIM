---
wave: gold-reset-wave36-sample-5-remediation
date_open: 2026-05-15
date_close: 2026-05-15
status: complete
source_wave: gold-certification-reset
---

# Gold Reset Wave 36 Sample 5 Remediation

## Mission

Complete the furniture portion of Wave 36 reset review: repair substantive
editorial defects, validate proof/Da Vinci coverage, and restore Certified Gold
only with guide-specific R2 evidence.

## Claim Boundary

This wave certifies only:

| Guide | Invariant |
|---|---|
| `furniture/06-MATERIALS-MODERN.md` | `modern-furniture-materials-table` |
| `furniture/07-IKEA-MODEL.md` | `ikea-system-map` |
| `furniture/08-ERGONOMICS-SEATING.md` | `seating-problem-anthropometrics` |
| `furniture/09-CONTEMPORARY.md` | `contemporary-furniture-stack` |

It does not restore Gold to the wider Wave 36 factory backlog.

## Pulse Status

| Pulse | Status | Governing Roles | Evidence |
|---|---|---|---|
| 01 - Repair and R2 panel | DONE | reference-editor, expert-skeptic, bridge-builder, index-weaver | `panels/r2-wave36-sample-5/R2-consolidated.md` |

## Validation Gates

| Gate | Result |
|---|---|
| Mechanical prerequisite | PASS: `proof.exe check --daVinci -e --no-fail proof.toml <4 guides>` returned OK and output contained no `FAIL` |
| Editorial repair | PASS: lookup-style tables, material/process overclaim, ergonomics wording, and CNC typo corrected |
| R2 panel | PASS: guide-specific scores, reader tasks, and adversarial closure recorded |
| Registry update | PASS: only the four repaired furniture guides restored to Current Certified Gold |

## Closeout

This sample completes the furniture reset slice. The furniture factory cohort is
Gold again only where reset-era repair, skeptical review, and reader-task
evidence now exist.

