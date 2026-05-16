---
pulse: 01
title: Repair and R2 Panel
status: complete
---

# Pulse 01 - Repair and R2 Panel

## Scope

- `intellectual-history/02-SOCIOLOGY-KNOWLEDGE.md`
- `intellectual-history/07-POSTSTRUCTURALISM.md`
- `social-history/03-HISTORY-FROM-BELOW.md`
- `social-history/08-MEMORY-HISTORY.md`

## Pre-implementation Scout

The guides were proof-clean and invariant-covered, but retained factory-era
navigation cheat sheets. Current Certified Gold requires diagnostic reader-task
support with caveats.

## Changes

| Guide | Repair |
|---|---|
| `intellectual-history/02-SOCIOLOGY-KNOWLEDGE.md` | Rebuilt the sociology of knowledge navigation table around Marx, Mannheim, Merton, Strong Programme/Latour, Bourdieu, and reflexivity caveats. |
| `intellectual-history/07-POSTSTRUCTURALISM.md` | Rebuilt the poststructuralism navigation table around Saussure, Barthes, Derrida, Foucault, Lyotard, Deleuze, and reception caveats. |
| `social-history/03-HISTORY-FROM-BELOW.md` | Rebuilt the history-from-below navigation table around Thompson, moral economy, social bandits, radical religion, everyday resistance, and oral-history caveats. |
| `social-history/08-MEMORY-HISTORY.md` | Rebuilt the memory history navigation table around collective memory, sites of memory, history/memory distinction, trauma, postmemory, commemoration, and difficult histories. |

## Gates

| Gate | Status |
|---|---|
| Proof + Da Vinci | PASS |
| Targeted editorial repair | PASS |
| R2 reference-editor panel | PASS |
| Consolidated Gold decision | PASS |

## Validation

```powershell
git --no-pager diff --check -- intellectual-history\02-SOCIOLOGY-KNOWLEDGE.md intellectual-history\07-POSTSTRUCTURALISM.md social-history\03-HISTORY-FROM-BELOW.md social-history\08-MEMORY-HISTORY.md
$proofOut = C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml intellectual-history\02-SOCIOLOGY-KNOWLEDGE.md intellectual-history\07-POSTSTRUCTURALISM.md social-history\03-HISTORY-FROM-BELOW.md social-history\08-MEMORY-HISTORY.md 2>&1; $proofOut; if ($proofOut -match 'FAIL') { exit 1 }
```

Result: PASS.

