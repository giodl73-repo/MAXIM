---
pulse: 01
title: Repair and R2 Panel
status: complete
---

# Pulse 01 - Repair and R2 Panel

## Scope

Repair and certify the fourth reset sample:

- `geology/03-SEDIMENTARY-ROCKS.md`
- `geology/04-METAMORPHIC-ROCKS.md`
- `geology/06-EARTHQUAKES-VOLCANOES.md`

## Pre-implementation Scout

Command:

```powershell
C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml geology\03-SEDIMENTARY-ROCKS.md geology\04-METAMORPHIC-ROCKS.md geology\06-EARTHQUAKES-VOLCANOES.md
```

Scout result: proof-clean with Da Vinci invariants present. Editorial review
still found Gold-blocking "lite polish" surfaces: recall-style cheat sheets and
claims that needed stronger caveats.

## Changes

| Guide | Repair |
|---|---|
| `geology/03-SEDIMENTARY-ROCKS.md` | Rebuilt the cheat sheet around basin/field diagnostic questions and removed taste as a primary halite test. |
| `geology/04-METAMORPHIC-ROCKS.md` | Caveated isochemical metamorphism against metasomatism and rebuilt the cheat sheet around protolith, grade, facies, fluids, and retrograde overprint. |
| `geology/06-EARTHQUAKES-VOLCANOES.md` | Replaced deterministic Cascadia "overdue" language, corrected Mw 9 energy framing, and rebuilt the hazard decision table. |

## Gates

| Gate | Status |
|---|---|
| Proof + Da Vinci | PASS |
| Targeted editorial repair | PASS |
| R2 reference-editor panel | PASS |
| Consolidated Gold decision | PASS |

## Validation

```powershell
git --no-pager diff --check -- geology\03-SEDIMENTARY-ROCKS.md geology\04-METAMORPHIC-ROCKS.md geology\06-EARTHQUAKES-VOLCANOES.md
C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml geology\03-SEDIMENTARY-ROCKS.md geology\04-METAMORPHIC-ROCKS.md geology\06-EARTHQUAKES-VOLCANOES.md | Tee-Object -Variable proofOut; if ($proofOut -match 'FAIL') { exit 1 }
```

Result: PASS.

