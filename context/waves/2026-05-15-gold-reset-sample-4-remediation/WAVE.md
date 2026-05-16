---
wave: gold-reset-sample-4-remediation
date_open: 2026-05-15
date_close: 2026-05-15
status: complete
source_wave: gold-certification-reset
---

# Gold Reset Sample 4 Remediation

## Mission

Run a fourth Wave 37 slice through the reset-era Gold process: repair substantive
editorial weaknesses in geology guides, validate proof/Da Vinci coverage, and
restore Certified Gold only with guide-specific R2 evidence.

## Claim Boundary

This wave certifies only:

| Guide | Invariant |
|---|---|
| `geology/03-SEDIMENTARY-ROCKS.md` | `sedimentary-rock-formation-pathway` |
| `geology/04-METAMORPHIC-ROCKS.md` | `metamorphic-framework` |
| `geology/06-EARTHQUAKES-VOLCANOES.md` | `earthquake-volcano-distribution` |

It does not restore Gold to the wider factory backlog.

## Pulse Status

| Pulse | Status | Governing Roles | Evidence |
|---|---|---|---|
| 01 - Repair and R2 panel | DONE | reference-editor, expert-skeptic, bridge-builder, index-weaver | `panels/r2-sample-4/R2-consolidated.md` |

## Validation Gates

| Gate | Result |
|---|---|
| Mechanical prerequisite | PASS: `proof.exe check --daVinci -e --no-fail proof.toml <3 guides>` returned OK and output contained no `FAIL` |
| Editorial repair | PASS: recall-style cheat sheets replaced; overbroad geology analogies and hazard claims caveated |
| R2 panel | PASS: guide-specific scores, reader tasks, and adversarial closure recorded |
| Registry update | PASS: only the three repaired guides restored to Current Certified Gold |

## Closeout

This wave continues the reset doctrine: proof-clean factory candidates are not
Gold until they survive guide-specific editorial repair and panel review.

