---
wave: proof-and-ascii-repair
date_open: 2026-04-25
date_close: 2026-04-27
status: archived
source: git-history
history_phases: []
---

# Proof and ASCII Repair

## Mission

Introduce proof-driven Markdown/ASCII validation and repair alignment, table,
and navigation issues across the library after the original February build.

## Backfill Boundary

This wave is reconstructed entirely from commit subjects. It has no matching
`/honor` phase yet, so it remains an execution-only backfill.

## Commit-Derived Pulses

| Pulse | Status | Evidence |
|---|---|---|
| 01 - README and navigation cleanup | done | `bd77eb9`, `4b48fe4`, `e0265ca` |
| 02 - Language ASCII repairs | done | `2d342f8`, `ad1afca`, `5fafbca`, `52de452`, `078498e` |
| 03 - Proof draft pipeline repairs | done | `1bc6123`, `3579f43`, `fbdb615`, `c3d7a74`, `ab7e7c6` |
| 04 - Proof configuration and table cleanup | done | `a03b8dc`, `9dd9989`, `3187627` |
| 05 - Directory-by-directory ASCII convergence | done | repair commits from `29204ca` through `9c40aa4` |

## Close Evidence

This wave is the direct predecessor to the current quality-control work. It
proved that mechanical validation can catch real defects, but also exposed the
risk of broad automated fixing and the need for gold/silver proof modes.

## Carry-Forward

The current active wave should turn this experience into a safer staged proof
policy: stricter for gold pilots, conservative for global sweeps, and never
dependent on blind bulk transformation.
