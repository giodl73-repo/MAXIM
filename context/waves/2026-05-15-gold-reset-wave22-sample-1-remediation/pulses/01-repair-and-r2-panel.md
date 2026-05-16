---
pulse: 01
title: Repair and R2 Panel
status: complete
---

# Pulse 01 - Repair and R2 Panel

## Scope

- `criminology/01-CLASSICAL-THEORIES.md`
- `criminology/02-STRAIN-ANOMIE.md`
- `criminology/03-SOCIAL-CONTROL.md`
- `criminology/04-WHITE-COLLAR.md`

## Pre-implementation Scout

The guides were proof-clean and invariant-covered, but retained factory-era
theory lookup and selector tables. Current Certified Gold requires diagnostic
reader-task support with caveats.

## Changes

| Guide | Repair |
|---|---|
| `criminology/01-CLASSICAL-THEORIES.md` | Rebuilt the classical criminology table around deterrence, proportional punishment, routine activity, situational prevention, rational choice, and hyperbolic-discounting caveats. |
| `criminology/02-STRAIN-ANOMIE.md` | Rebuilt the strain/anomie table around Durkheim, Merton, Cohen, Cloward-Ohlin, Agnew, and Messner-Rosenfeld caveats. |
| `criminology/03-SOCIAL-CONTROL.md` | Rebuilt the social control table around Hirschi, self-control, age-graded control, labeling, moral enterprise, stigma, differential association, and conflict theory. |
| `criminology/04-WHITE-COLLAR.md` | Rebuilt the white-collar table around class bias, fraud triangle, organizational offending, neutralization, prosecution rarity, and corporate/occupational distinctions. |

## Gates

| Gate | Status |
|---|---|
| Proof + Da Vinci | PASS |
| Targeted editorial repair | PASS |
| R2 reference-editor panel | PASS |
| Consolidated Gold decision | PASS |

## Validation

```powershell
git --no-pager diff --check -- criminology\01-CLASSICAL-THEORIES.md criminology\02-STRAIN-ANOMIE.md criminology\03-SOCIAL-CONTROL.md criminology\04-WHITE-COLLAR.md
$proofOut = C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml criminology\01-CLASSICAL-THEORIES.md criminology\02-STRAIN-ANOMIE.md criminology\03-SOCIAL-CONTROL.md criminology\04-WHITE-COLLAR.md 2>&1; $proofOut; if ($proofOut -match 'FAIL') { exit 1 }
```

Result: PASS.

