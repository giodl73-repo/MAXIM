---
wave: gold-reset-wave27-sample-1-remediation
date_open: 2026-05-15
date_close: 2026-05-15
status: complete
source_wave: gold-certification-reset
---

# Gold Reset Wave 27 Sample 1 Remediation

## Mission

Repair and re-panel the first Wave 27 computing sample before restoring Current
Certified Gold.

## Claim Boundary

| Guide | Invariant |
|---|---|
| `computing/02-GIT.md` | `git-mental-model` |
| `computing/03-JS-TS.md` | `js-ts-stack` |
| `computing/04-BUILD.md` | `build-tool-landscape` |
| `computing/05-FRONTEND.md` | `frontend-framework-landscape` |

## Pulse Status

| Pulse | Status | Governing Roles | Evidence |
|---|---|---|---|
| 01 - Repair and R2 panel | DONE | reference-editor, expert-skeptic, bridge-builder, index-weaver | `panels/r2-wave27-sample-1/R2-consolidated.md` |

## Validation Gates

| Gate | Result |
|---|---|
| Mechanical prerequisite | PASS: `proof.exe check --daVinci -e --no-fail proof.toml <4 guides>` returned OK and output contained no `FAIL` |
| Editorial repair | PASS: Git, JS/TS, Build, and Frontend cheat sheets rebuilt as diagnostic tables |
| R2 panel | PASS: guide-specific scoring, reader tasks, and adversarial closure recorded |
| Registry update | PASS: only these four repaired guides restored to Current Certified Gold |

## Closeout

Wave 27 sample 1 restores four guides with reset-era R2 evidence.

