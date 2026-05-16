---
pulse: 01
title: Repair and R2 Panel
status: complete
---

# Pulse 01 - Repair and R2 Panel

## Scope

- `archaeology/07-MEDIEVAL-ARCHAEOLOGY.md`
- `archaeology/08-HISTORICAL-ARCHAEOLOGY.md`
- `archaeology/09-ARCHAEOLOGICAL-THEORY.md`
- `architecture-history/01-ANCIENT.md`

## Pre-implementation Scout

The guides were proof-clean and invariant-covered, but retained factory-era
method-selector and answer-key cheat sheets. Current Certified Gold requires
diagnostic reader-task support with caveats.

## Changes

| Guide | Repair |
|---|---|
| `archaeology/07-MEDIEVAL-ARCHAEOLOGY.md` | Rebuilt the medieval archaeology selector around timber dating, pottery, pathogen aDNA, trade, rural social history, abandonment, buildings archaeology, and document-bias caveats. |
| `archaeology/08-HISTORICAL-ARCHAEOLOGY.md` | Rebuilt the historical archaeology selector around documentary bias, conflict archaeology, discard analysis, hybrid culture, industrial processes, forensic standards, and document/material divergence. |
| `archaeology/09-ARCHAEOLOGICAL-THEORY.md` | Rebuilt the theory matrix around culture history, processualism, post-processualism, pluralism, paradigm layering, politics, and formation-process caveats. |
| `architecture-history/01-ANCIENT.md` | Rebuilt the ancient architecture answer key around span limits, dome geometry, concrete, orders, entasis, vault thrust, pyramid mass, and Roman arch scaling caveats. |

## Gates

| Gate | Status |
|---|---|
| Proof + Da Vinci | PASS |
| Targeted editorial repair | PASS |
| R2 reference-editor panel | PASS |
| Consolidated Gold decision | PASS |

## Validation

```powershell
git --no-pager diff --check -- archaeology\07-MEDIEVAL-ARCHAEOLOGY.md archaeology\08-HISTORICAL-ARCHAEOLOGY.md archaeology\09-ARCHAEOLOGICAL-THEORY.md architecture-history\01-ANCIENT.md
$proofOut = C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml archaeology\07-MEDIEVAL-ARCHAEOLOGY.md archaeology\08-HISTORICAL-ARCHAEOLOGY.md archaeology\09-ARCHAEOLOGICAL-THEORY.md architecture-history\01-ANCIENT.md 2>&1; $proofOut; if ($proofOut -match 'FAIL') { exit 1 }
```

Result: PASS.

