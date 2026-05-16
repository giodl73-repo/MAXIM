---
pulse: 01
title: Repair and R2 Panel
status: complete
---

# Pulse 01 - Repair and R2 Panel

## Scope

- `international-relations/03-CONSTRUCTIVISM.md`
- `international-relations/04-NUCLEAR-DETERRENCE.md`
- `international-relations/05-POWER-TRANSITION.md`
- `international-relations/06-INTERNATIONAL-INSTITUTIONS.md`

## Pre-implementation Scout

The guides were proof-clean and invariant-covered, but retained factory-era
direct theory-answer tables. Current Certified Gold requires diagnostic
reader-task support with caveats.

## Changes

| Guide | Repair |
|---|---|
| `international-relations/03-CONSTRUCTIVISM.md` | Rebuilt the constructivism answer table around anarchy, norm diffusion, Cold War identity change, securitization, postcolonial IR, and feminist IR. |
| `international-relations/04-NUCLEAR-DETERRENCE.md` | Rebuilt the nuclear deterrence answer table around MAD, credibility, ABM, INF, multipolarity, and hypersonics. |
| `international-relations/05-POWER-TRANSITION.md` | Rebuilt the power transition answer table around parity, dissatisfaction, Gilpin, peaceful transition, Thucydides Trap, interdependence, and hegemonic stability. |
| `international-relations/06-INTERNATIONAL-INSTITUTIONS.md` | Rebuilt the institutions answer table around UNSC veto, MFN, WTO DSM, IMF conditionality, ICC enforcement, and institutional effectiveness. |

## Gates

| Gate | Status |
|---|---|
| Proof + Da Vinci | PASS |
| Targeted editorial repair | PASS |
| R2 reference-editor panel | PASS |
| Consolidated Gold decision | PASS |

## Validation

```powershell
git --no-pager diff --check -- international-relations\03-CONSTRUCTIVISM.md international-relations\04-NUCLEAR-DETERRENCE.md international-relations\05-POWER-TRANSITION.md international-relations\06-INTERNATIONAL-INSTITUTIONS.md
$proofOut = C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml international-relations\03-CONSTRUCTIVISM.md international-relations\04-NUCLEAR-DETERRENCE.md international-relations\05-POWER-TRANSITION.md international-relations\06-INTERNATIONAL-INSTITUTIONS.md 2>&1; $proofOut; if ($proofOut -match 'FAIL') { exit 1 }
```

Result: PASS.

