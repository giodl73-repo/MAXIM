---
wave: gold-reset-wave20-sample-5-remediation
date_open: 2026-05-15
date_close: 2026-05-15
status: complete
source_wave: gold-certification-reset
---

# Gold Reset Wave 20 Sample 5 Remediation

## Mission

Repair and re-panel the connections and opening fluid-dynamics Wave 20 sample
before restoring Current Certified Gold.

## Claim Boundary

| Guide | Invariant |
|---|---|
| `differential-geometry/05-CONNECTIONS.md` | `connections-overview` |
| `fluid-dynamics/01-CONTINUUM-MECHANICS.md` | `continuum-mechanics-structure` |
| `fluid-dynamics/02-INVISCID-FLOW.md` | `inviscid-flow-conceptual-structure` |
| `fluid-dynamics/03-VISCOUS-FLOW.md` | `navier-stokes-full-structure` |

## Pulse Status

| Pulse | Status | Governing Roles | Evidence |
|---|---|---|---|
| 01 - Repair and R2 panel | DONE | reference-editor, expert-skeptic, bridge-builder, index-weaver | `panels/r2-wave20-sample-5/R2-consolidated.md` |

## Validation Gates

| Gate | Result |
|---|---|
| Mechanical prerequisite | PASS: `proof.exe check --daVinci -e --no-fail proof.toml <4 guides>` returned OK and output contained no `FAIL` |
| Editorial repair | PASS: connections, continuum mechanics, inviscid flow, and viscous flow cheat sheets rebuilt as diagnostic tables |
| R2 panel | PASS: guide-specific scoring, reader tasks, and adversarial closure recorded |
| Registry update | PASS: only these four repaired guides restored to Current Certified Gold |

## Closeout

Wave 20 sample 5 restores one differential-geometry guide and three
fluid-dynamics guides with reset-era R2 evidence.

