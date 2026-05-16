---
wave: gold-reset-wave17-sample-4-remediation
date_open: 2026-05-15
date_close: 2026-05-15
status: complete
source_wave: gold-certification-reset
---

# Gold Reset Wave 17 Sample 4 Remediation

## Mission

Repair and re-panel the middle leatherworking Wave 17 sample before restoring
Current Certified Gold.

## Claim Boundary

| Guide | Invariant |
|---|---|
| `leatherworking/04-CUTTING-SKIVING.md` | `leather-cutting-tool-landscape` |
| `leatherworking/05-TOOLING-CARVING.md` | `leather-tooling-workflow` |
| `leatherworking/06-DYEING-FINISHING.md` | `leather-finishing-sequence` |
| `leatherworking/07-STITCHING-SEWING.md` | `saddle-vs-lock-stitch` |

## Pulse Status

| Pulse | Status | Governing Roles | Evidence |
|---|---|---|---|
| 01 - Repair and R2 panel | DONE | reference-editor, expert-skeptic, bridge-builder, index-weaver | `panels/r2-wave17-sample-4/R2-consolidated.md` |

## Validation Gates

| Gate | Result |
|---|---|
| Mechanical prerequisite | PASS: `proof.exe check --daVinci -e --no-fail proof.toml <4 guides>` returned OK and output contained no `FAIL` |
| Editorial repair | PASS: cutting/skiving, tooling/carving, dyeing/finishing, and stitching/sewing cheat sheets rebuilt as diagnostic tables |
| R2 panel | PASS: guide-specific scoring, reader tasks, and adversarial closure recorded |
| Registry update | PASS: only these four repaired guides restored to Current Certified Gold |

## Closeout

Wave 17 sample 4 restores four leatherworking guides with reset-era R2 evidence.

