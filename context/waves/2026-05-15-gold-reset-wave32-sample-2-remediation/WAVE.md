---
wave: gold-reset-wave32-sample-2-remediation
date_open: 2026-05-15
date_close: 2026-05-15
status: complete
source_wave: gold-certification-reset
---

# Gold Reset Wave 32 Sample 2 Remediation

## Mission

Repair and re-panel the Wave 32 science sample: dendrology overview, curvature,
fiber bundles, and disease overview.

## Claim Boundary

| Guide | Invariant |
|---|---|
| `dendrology/00-OVERVIEW.md` | `dendrology-landscape` |
| `differential-geometry/06-CURVATURE.md` | `curvature-hierarchy` |
| `differential-geometry/08-FIBER-BUNDLES.md` | `fiber-bundle-overview` |
| `disease/00-OVERVIEW.md` | `disease-classification-overview` |

## Pulse Status

| Pulse | Status | Governing Roles | Evidence |
|---|---|---|---|
| 01 - Repair and R2 panel | DONE | reference-editor, expert-skeptic, bridge-builder, index-weaver | `panels/r2-wave32-sample-2/R2-consolidated.md` |

## Validation Gates

| Gate | Result |
|---|---|
| Mechanical prerequisite | PASS: `proof.exe check --daVinci -e --no-fail proof.toml <4 guides>` returned OK and output contained no `FAIL` |
| Editorial repair | PASS: lookup tables rebuilt as diagnostic tables; disease burden and causal claims caveated |
| R2 panel | PASS: guide-specific scoring, reader tasks, and adversarial closure recorded |
| Registry update | PASS: only these four repaired guides restored to Current Certified Gold |

## Closeout

Wave 32 sample 2 restores four science/disease guides with reset-era R2 evidence.

