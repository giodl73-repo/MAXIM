---
wave: gold-reset-wave7-sample-1-remediation
date_open: 2026-05-15
date_close: 2026-05-15
status: complete
source_wave: gold-certification-reset
---

# Gold Reset Wave 7 Sample 1 Remediation

## Mission

Repair and re-panel the first Wave 7 signal-processing sample before restoring
Current Certified Gold.

## Claim Boundary

| Guide | Invariant |
|---|---|
| `signal-processing/04-CONVOLUTION-CORRELATION.md` | `convolution-correlation-operations` |
| `signal-processing/05-Z-TRANSFORM.md` | `z-transform-correspondence` |
| `signal-processing/06-STOCHASTIC-SIGNALS.md` | `stochastic-signal-framework` |
| `signal-processing/07-SPECTRAL-ESTIMATION.md` | `spectral-estimation-problem` |

## Pulse Status

| Pulse | Status | Governing Roles | Evidence |
|---|---|---|---|
| 01 - Repair and R2 panel | DONE | reference-editor, expert-skeptic, bridge-builder, index-weaver | `panels/r2-wave7-sample-1/R2-consolidated.md` |

## Validation Gates

| Gate | Result |
|---|---|
| Mechanical prerequisite | PASS: `proof.exe check --daVinci -e --no-fail proof.toml <4 guides>` returned OK and output contained no `FAIL` |
| Editorial repair | PASS: convolution/correlation, z-transform, stochastic-signal, and spectral-estimation cheat sheets confirmed as diagnostic tables |
| R2 panel | PASS: guide-specific scoring, reader tasks, and adversarial closure recorded |
| Registry update | PASS: only these four repaired guides restored to Current Certified Gold |

## Closeout

Wave 7 sample 1 restores four signal-processing guides with reset-era R2
evidence.

