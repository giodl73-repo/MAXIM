---
pulse: 01
title: Repair and R2 Panel
status: complete
---

# Pulse 01 - Repair and R2 Panel

## Scope

Repair and certify the final Wave 36 reset sample:

- `games-history/04-POKER.md`
- `games-history/05-BILLIARDS-POOL.md`

## Pre-implementation Scout

Command:

```powershell
C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml games-history\04-POKER.md games-history\05-BILLIARDS-POOL.md
```

Scout result: proof-clean with Da Vinci invariants present. Editorial review
found Gold-blocking poker "solved" overclaims, a pot-odds percentage error,
CFR+ wording overreach, a snooker fastest-147 venue/time error, and lookup-style
decision tables.

## Changes

| Guide | Repair |
|---|---|
| `games-history/04-POKER.md` | Replaced solved-language with superhuman/abstraction caveats, corrected pot-odds math, softened CFR+ convergence wording, and rebuilt the cheat sheet diagnostically. |
| `games-history/05-BILLIARDS-POOL.md` | Corrected Ronnie O'Sullivan's fastest 147 venue/time and rebuilt the cheat sheet around cue-sport diagnostic frames. |

## Gates

| Gate | Status |
|---|---|
| Proof + Da Vinci | PASS |
| Targeted editorial repair | PASS |
| R2 reference-editor panel | PASS |
| Consolidated Gold decision | PASS |

## Validation

```powershell
git --no-pager diff --check -- games-history\04-POKER.md games-history\05-BILLIARDS-POOL.md
C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml games-history\04-POKER.md games-history\05-BILLIARDS-POOL.md | Tee-Object -Variable proofOut; if ($proofOut -match 'FAIL') { exit 1 }
```

Result: PASS.

