---
pulse: 01
title: Repair and R2 Panel
status: complete
---

# Pulse 01 - Repair and R2 Panel

## Scope

- `historiography/05-SOCIAL-CULTURAL-TURN.md`
- `historiography/06-POSTMODERN-CHALLENGE.md`
- `historiography/08-GLOBAL-HISTORY.md`
- `historiography/09-PHILOSOPHY-OF-HIST.md`

## Pre-implementation Scout

The guides were proof-clean and invariant-covered, but retained factory-era
school, position, approach, and question/answer selector tables. Current
Certified Gold requires diagnostic reader-task support with caveats.

## Changes

| Guide | Repair |
|---|---|
| `historiography/05-SOCIAL-CULTURAL-TURN.md` | Rebuilt the social/cultural table around ordinary lives, class, microhistory, cultural meaning, gender, subaltern recovery, and history-from-below diagnostics. |
| `historiography/06-POSTMODERN-CHALLENGE.md` | Rebuilt the postmodern table around positivism, White, Foucault, practical realism, relativism, denial misuse, and linguistic-turn impact. |
| `historiography/08-GLOBAL-HISTORY.md` | Rebuilt the global-history table around world systems, connected histories, provincializing Europe, comparison, Atlantic history, Big History, global labels, and public-history reframing. |
| `historiography/09-PHILOSOPHY-OF-HIST.md` | Rebuilt the philosophy table around causation, covering laws, counterfactuals, periodization, objectivity, metanarratives, narrative explanation, and postmodern challenge. |

## Gates

| Gate | Status |
|---|---|
| Proof + Da Vinci | PASS |
| Targeted editorial repair | PASS |
| R2 reference-editor panel | PASS |
| Consolidated Gold decision | PASS |

## Validation

```powershell
git --no-pager diff --check -- historiography\05-SOCIAL-CULTURAL-TURN.md historiography\06-POSTMODERN-CHALLENGE.md historiography\08-GLOBAL-HISTORY.md historiography\09-PHILOSOPHY-OF-HIST.md
$proofOut = C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml historiography\05-SOCIAL-CULTURAL-TURN.md historiography\06-POSTMODERN-CHALLENGE.md historiography\08-GLOBAL-HISTORY.md historiography\09-PHILOSOPHY-OF-HIST.md 2>&1; $proofOut; if ($proofOut -match 'FAIL') { exit 1 }
```

Result: PASS.

