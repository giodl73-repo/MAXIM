---
pulse: 01
title: Repair and R2 Panel
status: complete
---

# Pulse 01 - Repair and R2 Panel

## Scope

- `anthropology/07-COGNITIVE-CULTURAL.md`
- `anthropology/08-APPLIED-ANTHROPOLOGY.md`
- `archaeology/00-OVERVIEW.md`
- `architecture/00-OVERVIEW.md`

## Pre-implementation Scout

The guides were proof-clean and invariant-covered, but retained factory-era
framework/tool/use-case/approach selector tables without enough diagnostic
caveats for Current Certified Gold.

## Changes

| Guide | Repair |
|---|---|
| `anthropology/07-COGNITIVE-CULTURAL.md` | Rebuilt the cheat sheet around distributed cognition, extended mind, situated action, material engagement, sociotechnical systems, niche construction, dual inheritance, WEIRD psychology, Dunbar layers, and cognitive archaeology. |
| `anthropology/08-APPLIED-ANTHROPOLOGY.md` | Rebuilt the cheat sheet around manuals, actual workflow, top-down redesign, participation, collaboration-as-compliance, behavior research, indigenous data, human remains, repatriation, and product translation. |
| `archaeology/00-OVERVIEW.md` | Rebuilt the cheat sheet around material/text conflict, non-literate societies, history from below, textual chronology, diet/health/demography, trade networks, paradigm limits, and migration/diffusion. |
| `architecture/00-OVERVIEW.md` | Rebuilt the cheat sheet around long spans, seismic resistance, hot-dry and hot-humid strategies, delivery speed, design control, certification, and adaptive reuse. |

## Gates

| Gate | Status |
|---|---|
| Proof + Da Vinci | PASS |
| Targeted editorial repair | PASS |
| R2 reference-editor panel | PASS |
| Consolidated Gold decision | PASS |

## Validation

```powershell
git --no-pager diff --check -- anthropology\07-COGNITIVE-CULTURAL.md anthropology\08-APPLIED-ANTHROPOLOGY.md archaeology\00-OVERVIEW.md architecture\00-OVERVIEW.md
$proofOut = C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml anthropology\07-COGNITIVE-CULTURAL.md anthropology\08-APPLIED-ANTHROPOLOGY.md archaeology\00-OVERVIEW.md architecture\00-OVERVIEW.md 2>&1; $proofOut; if ($proofOut -match 'FAIL') { exit 1 }
```

Result: PASS.

