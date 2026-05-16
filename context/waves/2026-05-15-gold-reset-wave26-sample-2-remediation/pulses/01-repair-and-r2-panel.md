---
pulse: 01
title: Repair and R2 Panel
status: complete
---

# Pulse 01 - Repair and R2 Panel

## Scope

- `cinema-film/05-CLASSICAL-HOLLYWOOD.md`
- `cinema-film/06-WORLD-CINEMA.md`
- `cinema-film/07-CINEMATOGRAPHY-OPTICS.md`
- `cinema-film/08-EDITING-THEORY.md`

## Pre-implementation Scout

The guides were proof-clean and invariant-covered, but retained factory-era
lookup tables. Current Certified Gold requires diagnostic reader-task support
with caveats.

## Changes

| Guide | Repair |
|---|---|
| `cinema-film/05-CLASSICAL-HOLLYWOOD.md` | Rebuilt the cheat sheet around Paramount, block booking, Production Code, B-films, star loans, contracts, star systems, and studio output volume. |
| `cinema-film/06-WORLD-CINEMA.md` | Rebuilt the movement table around diagnostic formal/economic caveats for Expressionism, Montage, Poetic Realism, Neorealism, Japanese Golden Age, French New Wave, and New Hollywood. |
| `cinema-film/07-CINEMATOGRAPHY-OPTICS.md` | Rebuilt the cheat sheet around focal length, perspective, aperture, shutter, grain/noise, DI, dynamic range, and log gamma caveats. |
| `cinema-film/08-EDITING-THEORY.md` | Rebuilt the editing concept table around Kuleshov, match action, jump cuts, graphic/smash cuts, ASL, NLEs, LUTs, Avid, and Resolve as diagnostic questions. |

## Gates

| Gate | Status |
|---|---|
| Proof + Da Vinci | PASS |
| Targeted editorial repair | PASS |
| R2 reference-editor panel | PASS |
| Consolidated Gold decision | PASS |

## Validation

```powershell
git --no-pager diff --check -- cinema-film\05-CLASSICAL-HOLLYWOOD.md cinema-film\06-WORLD-CINEMA.md cinema-film\07-CINEMATOGRAPHY-OPTICS.md cinema-film\08-EDITING-THEORY.md
$proofOut = C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml cinema-film\05-CLASSICAL-HOLLYWOOD.md cinema-film\06-WORLD-CINEMA.md cinema-film\07-CINEMATOGRAPHY-OPTICS.md cinema-film\08-EDITING-THEORY.md 2>&1; $proofOut; if ($proofOut -match 'FAIL') { exit 1 }
```

Result: PASS.

