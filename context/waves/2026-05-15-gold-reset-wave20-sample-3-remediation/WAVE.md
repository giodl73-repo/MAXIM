---
wave: gold-reset-wave20-sample-3-remediation
date_open: 2026-05-15
date_close: 2026-05-15
status: complete
source_wave: gold-certification-reset
---

# Gold Reset Wave 20 Sample 3 Remediation

## Mission

Repair and re-panel the quantum hardware/communication and statistical-mechanics
Wave 20 sample before restoring Current Certified Gold.

## Claim Boundary

| Guide | Invariant |
|---|---|
| `quantum-computing/04-HARDWARE-COMPLEXITY.md` | `quantum-computing-stack` |
| `quantum-computing/06-QUANTUM-COMMUNICATION.md` | `qkd-protocol-family` |
| `statistical-mechanics/06-RENORMALIZATION.md` | `renormalization-group-flow` |
| `statistical-mechanics/07-ISING-MODELS.md` | `ising-model-landscape` |

## Pulse Status

| Pulse | Status | Governing Roles | Evidence |
|---|---|---|---|
| 01 - Repair and R2 panel | DONE | reference-editor, expert-skeptic, bridge-builder, index-weaver | `panels/r2-wave20-sample-3/R2-consolidated.md` |

## Validation Gates

| Gate | Result |
|---|---|
| Mechanical prerequisite | PASS: `proof.exe check --daVinci -e --no-fail proof.toml <4 guides>` returned OK and output contained no `FAIL` |
| Editorial repair | PASS: quantum hardware, quantum communication, renormalization, and Ising model cheat sheets rebuilt as diagnostic tables |
| R2 panel | PASS: guide-specific scoring, reader tasks, and adversarial closure recorded |
| Registry update | PASS: only these four repaired guides restored to Current Certified Gold |

## Closeout

Wave 20 sample 3 restores two quantum-computing guides and two statistical
mechanics guides with reset-era R2 evidence.

