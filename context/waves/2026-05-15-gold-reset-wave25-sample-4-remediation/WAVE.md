---
wave: gold-reset-wave25-sample-4-remediation
date_open: 2026-05-15
date_close: 2026-05-15
status: complete
source_wave: gold-certification-reset
---

# Gold Reset Wave 25 Sample 4 Remediation

## Mission

Repair and re-panel the fourth Wave 25 biomedical-engineering sample before
restoring Current Certified Gold.

## Claim Boundary

| Guide | Invariant |
|---|---|
| `biomedical-engineering/05-NEURAL-INTERFACES.md` | `neural-interface-signal-hierarchy` |
| `biomedical-engineering/06-PROSTHETICS.md` | `prosthetics-landscape` |
| `biomedical-engineering/07-MEDICAL-DEVICES.md` | `medical-device-regulatory-framework` |
| `biomedical-engineering/08-TISSUE-ENGINEERING.md` | `tissue-engineering-landscape` |

## Pulse Status

| Pulse | Status | Governing Roles | Evidence |
|---|---|---|---|
| 01 - Repair and R2 panel | DONE | reference-editor, expert-skeptic, bridge-builder, index-weaver | `panels/r2-wave25-sample-4/R2-consolidated.md` |

## Validation Gates

| Gate | Result |
|---|---|
| Mechanical prerequisite | PASS: `proof.exe check --daVinci -e --no-fail proof.toml <4 guides>` returned OK and output contained no `FAIL` |
| Editorial repair | PASS: neural interfaces, prosthetics, medical devices, and tissue engineering cheat sheets rebuilt as diagnostic tables |
| R2 panel | PASS: guide-specific scoring, reader tasks, and adversarial closure recorded |
| Registry update | PASS: only these four repaired guides restored to Current Certified Gold |

## Closeout

Wave 25 sample 4 restores four biomedical-engineering guides with reset-era R2 evidence.

