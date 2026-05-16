---
wave: gold-figure-invariants
date_open: 2026-05-14
date_close: 2026-05-14
status: complete
source_wave: maxim-quality-control-spine
---

# Gold Figure Invariants

## Mission

Protect the first canonical Gold figures identified by the pilot audit, and
repair any diagram defects exposed while moving them under proof.

## Pulse Status

| Pulse | Status | Evidence |
|---|---|---|
| 01 - Package stack invariant | DONE | `proof.toml` pins `computing/01-PACKAGE.md#the-big-picture:0` |
| 02 - Consensus landscape invariant | DONE | `proof.toml` pins `distributed-systems/03-CONSENSUS.md#the-big-picture:0` |
| 03 - Global Winds invariant | DONE | `proof.toml` pins `atlas/02-GLOBAL-WINDS.md#the-three-cell-model:0` |
| 04 - Atlas ASCII repairs | DONE | `atlas/02-GLOBAL-WINDS.md` monsoon and cyclone diagrams now pass focused proof |

## Validation

```powershell
C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail computing\01-PACKAGE.md distributed-systems\03-CONSENSUS.md atlas\02-GLOBAL-WINDS.md
```

## Closeout

This wave converts the pilot audit's "protect canonical guides" recommendation
into an executable guardrail. It does not make global proof stricter; it pins a
small set of high-signal figures first, matching the staged-proof plan.
