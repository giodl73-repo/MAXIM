---
pulse: 01
title: Repair and R2 Panel
status: complete
---

# Pulse 01 - Repair and R2 Panel

## Scope

- `anthropology/03-PRIMATOLOGY.md`
- `anthropology/04-EVOLUTIONARY-ANTHROPOLOGY.md`
- `anthropology/05-CULTURAL-ANTHROPOLOGY.md`
- `anthropology/06-ARCHAEOLOGY.md`

## Pre-implementation Scout

The guides were proof-clean and invariant-covered, but retained factory-era
research/framework/method lookup tables without enough diagnostic caveats for
Current Certified Gold.

## Changes

| Guide | Repair |
|---|---|
| `anthropology/03-PRIMATOLOGY.md` | Rebuilt the cheat sheet around primate phylogeny, color vision, brain size, alarm calls, tool use, culture, ape language, self-recognition, theory of mind, and bonobo/chimp contrast. |
| `anthropology/04-EVOLUTIONARY-ANTHROPOLOGY.md` | Rebuilt the cheat sheet around kin altruism, cooperation, punishment, incest avoidance, childhood, grandmother effects, mating systems, cross-cultural claims, naturalistic fallacy, and adaptation tests. |
| `anthropology/05-CULTURAL-ANTHROPOLOGY.md` | Rebuilt the cheat sheet around field research, survey/behavior mismatch, gifts, prestige exchange, ritual, off-sites, marriage, kinship terms, interpretive validity, and cultural change. |
| `anthropology/06-ARCHAEOLOGY.md` | Rebuilt the cheat sheet around site discovery, radiocarbon, TL/OSL, volcanic dating, dendrochronology, Bayesian dating, Harris Matrix, seriation, CRM, and NAGPRA. |

## Gates

| Gate | Status |
|---|---|
| Proof + Da Vinci | PASS |
| Targeted editorial repair | PASS |
| R2 reference-editor panel | PASS |
| Consolidated Gold decision | PASS |

## Validation

```powershell
git --no-pager diff --check -- anthropology\03-PRIMATOLOGY.md anthropology\04-EVOLUTIONARY-ANTHROPOLOGY.md anthropology\05-CULTURAL-ANTHROPOLOGY.md anthropology\06-ARCHAEOLOGY.md
$proofOut = C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml anthropology\03-PRIMATOLOGY.md anthropology\04-EVOLUTIONARY-ANTHROPOLOGY.md anthropology\05-CULTURAL-ANTHROPOLOGY.md anthropology\06-ARCHAEOLOGY.md 2>&1; $proofOut; if ($proofOut -match 'FAIL') { exit 1 }
```

Result: PASS.

