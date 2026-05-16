---
wave: gold-reset-sample-2-remediation
date_open: 2026-05-15
date_close: 2026-05-15
status: complete
source_wave: gold-certification-reset
---

# Gold Reset Sample 2 Remediation

## Mission

Run the next Wave 37 sample through the stricter reset-era Gold path: identify
candidate blockers, repair the guides, validate proof/Da Vinci coverage, and
restore Certified Gold only with guide-specific panel evidence.

## Claim Boundary

This wave certifies only:

| Guide | Invariant |
|---|---|
| `games-history/06-DICE-GAMBLING.md` | `gambling-mathematics-origin` |
| `genomics/00-OVERVIEW.md` | `genomics-landscape` |
| `geography/04-BIOGEOGRAPHY.md` | `biogeography-frameworks` |

It does not restore Gold to the wider factory backlog.

## Pulse Status

| Pulse | Status | Governing Roles | Evidence |
|---|---|---|---|
| 01 - Repair and R2 panel | DONE | reference-editor, ascii-cartographer, expert-skeptic, bridge-builder, index-weaver | `panels/r2-sample-2/R2-consolidated.md` |

## Validation Gates

| Gate | Result |
|---|---|
| Mechanical prerequisite | PASS: `proof.exe check --daVinci -e --no-fail proof.toml <3 guides>` returned OK and output contained no `FAIL` |
| Editorial repair | PASS: factual slip, stale tooling language, overclaim/caveat gaps, and weak decision tables repaired |
| R2 panel | PASS: guide-specific scores, reader tasks, and adversarial closure recorded |
| Registry update | PASS: only the three repaired guides restored to Current Certified Gold |

## Closeout

This wave continues the reset pattern: a factory guide is not Gold because it
was proof-clean; it becomes Gold only after the panel finds and closes the real
editorial issues.

