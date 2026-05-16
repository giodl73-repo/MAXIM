---
wave: gold-reset-wave37-final-remediation
date_open: 2026-05-15
date_close: 2026-05-15
status: complete
source_wave: gold-certification-reset
---

# Gold Reset Wave 37 Final Remediation

## Mission

Finish the remaining Wave 37 reset backlog with real Gold evidence: repair the
last geology, geotechnical, and glassmaking candidates; validate proof/Da Vinci
coverage; and restore Certified Gold only with guide-specific R2 review.

## Claim Boundary

This wave certifies only:

| Guide | Invariant |
|---|---|
| `geology/10-PLANETARY-GEOLOGY.md` | `comparative-planetary-geology` |
| `geotechnical-engineering/03-CONSOLIDATION.md` | `consolidation-two-problems` |
| `geotechnical-engineering/05-SLOPE-STABILITY.md` | `slope-stability-analysis-hierarchy` |
| `geotechnical-engineering/06-SHALLOW-FOUNDATIONS.md` | `shallow-foundation-design-flow` |
| `geotechnical-engineering/07-DEEP-FOUNDATIONS.md` | `deep-foundation-selection` |
| `geotechnical-engineering/09-GROUND-IMPROVEMENT.md` | `ground-improvement-selection-map` |
| `glassmaking/00-OVERVIEW.md` | `glassmaking-supply-chain` |
| `glassmaking/02-RAW-MATERIALS.md` | `soda-lime-glass-batch` |
| `glassmaking/03-FORMING-TECHNIQUES.md` | `glass-forming-techniques` |

It does not certify any guide outside this scoped final Wave 37 slice.

## Pulse Status

| Pulse | Status | Governing Roles | Evidence |
|---|---|---|---|
| 01 - Repair and R2 panel | DONE | reference-editor, expert-skeptic, bridge-builder, index-weaver | `panels/r2-wave37-final/R2-consolidated.md` |

## Validation Gates

| Gate | Result |
|---|---|
| Mechanical prerequisite | PASS: `proof.exe check --daVinci -e --no-fail proof.toml <9 guides>` returned OK and output contained no `FAIL` |
| Editorial repair | PASS: factory lookup tables replaced with diagnostic decision surfaces; factual typos/overclaims fixed |
| R2 panel | PASS: guide-specific scores, reader tasks, and adversarial closure recorded |
| Registry update | PASS: only the nine repaired guides restored to Current Certified Gold |

## Closeout

Together with reset samples 1-5, this closes Wave 37's reset-era remediation.
The old factory wave remains provenance for Candidate-Hardened status; the reset
waves are the certification evidence.

