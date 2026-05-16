---
wave: gold-reset-wave21-sample-4-remediation
date_open: 2026-05-15
date_close: 2026-05-15
status: complete
source_wave: gold-certification-reset
---

# Gold Reset Wave 21 Sample 4 Remediation

## Mission

Repair and re-panel the public-health control and global-health Wave 21 sample
before restoring Current Certified Gold.

## Claim Boundary

| Guide | Invariant |
|---|---|
| `public-health/03-INFECTIOUS-DISEASE-CONTROL.md` | `infectious-disease-transmission-framework` |
| `public-health/05-CHRONIC-DISEASE.md` | `global-ncd-burden` |
| `public-health/06-ENVIRONMENTAL-HEALTH.md` | `environmental-health-causal-chain` |
| `public-health/07-GLOBAL-HEALTH.md` | `global-health-governance-ecosystem` |

## Pulse Status

| Pulse | Status | Governing Roles | Evidence |
|---|---|---|---|
| 01 - Repair and R2 panel | DONE | reference-editor, expert-skeptic, bridge-builder, index-weaver | `panels/r2-wave21-sample-4/R2-consolidated.md` |

## Validation Gates

| Gate | Result |
|---|---|
| Mechanical prerequisite | PASS: `proof.exe check --daVinci -e --no-fail proof.toml <4 guides>` returned OK and output contained no `FAIL` |
| Editorial repair | PASS: infectious disease control, chronic disease, environmental health, and global health cheat sheets rebuilt as diagnostic tables |
| R2 panel | PASS: guide-specific scoring, reader tasks, and adversarial closure recorded |
| Registry update | PASS: only these four repaired guides restored to Current Certified Gold |

## Closeout

Wave 21 sample 4 restores four public-health guides with reset-era R2 evidence.

