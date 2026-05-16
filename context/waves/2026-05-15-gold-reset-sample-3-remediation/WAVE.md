---
wave: gold-reset-sample-3-remediation
date_open: 2026-05-15
date_close: 2026-05-15
status: complete
source_wave: gold-certification-reset
---

# Gold Reset Sample 3 Remediation

## Mission

Run a third Wave 37 slice through the reset-era Gold process: audit the factory
claim, repair real editorial weaknesses, validate proof/Da Vinci coverage, and
restore Certified Gold only with guide-specific panel evidence.

## Claim Boundary

This wave certifies only:

| Guide | Invariant |
|---|---|
| `games-history/07-BOARD-GAMES-MODERN.md` | `modern-board-game-timeline` |
| `games-history/08-VIDEO-GAMES.md` | `video-game-history-timeline` |
| `geology/02-IGNEOUS-ROCKS.md` | `igneous-rock-framework` |

It does not restore Gold to the wider factory backlog.

## Pulse Status

| Pulse | Status | Governing Roles | Evidence |
|---|---|---|---|
| 01 - Repair and R2 panel | DONE | reference-editor, ascii-cartographer, expert-skeptic, bridge-builder, index-weaver | `panels/r2-sample-3/R2-consolidated.md` |

## Validation Gates

| Gate | Result |
|---|---|
| Mechanical prerequisite | PASS: `proof.exe check --daVinci -e --no-fail proof.toml <3 guides>` returned OK and output contained no `FAIL` |
| Editorial repair | PASS: stale/overbroad claims and recall-style decision surfaces repaired |
| R2 panel | PASS: guide-specific scores, reader tasks, and adversarial closure recorded |
| Registry update | PASS: only the three repaired guides restored to Current Certified Gold |

## Closeout

This wave reinforces the reset rule. Factory proof made the guides eligible for
review; targeted editorial repair and a reset-era panel made the scoped Gold
claims defensible.

