---
pulse: 01
title: Repair and R2 Panel
status: complete
---

# Pulse 01 - Repair and R2 Panel

## Scope

- `quantum-computing/04-HARDWARE-COMPLEXITY.md`
- `quantum-computing/06-QUANTUM-COMMUNICATION.md`
- `statistical-mechanics/06-RENORMALIZATION.md`
- `statistical-mechanics/07-ISING-MODELS.md`

## Pre-implementation Scout

The guides were proof-clean and invariant-covered, but retained factory-era
direct answer tables, ASCII recommendation matrices, and model selector tables.
Current Certified Gold requires diagnostic reader-task support with caveats.

## Changes

| Guide | Repair |
|---|---|
| `quantum-computing/04-HARDWARE-COMPLEXITY.md` | Rebuilt the hardware/complexity answer table around fidelity, qubit count, platform uncertainty, annealing, RSA timeline, PQC standards, factoring complexity, and NP-complete limits. |
| `quantum-computing/06-QUANTUM-COMMUNICATION.md` | Rebuilt the QKD ASCII recommendation matrix around information-theoretic security, fiber distance regimes, satellite/repeater options, device independence, QBER aborts, and PQC alternatives. |
| `statistical-mechanics/06-RENORMALIZATION.md` | Rebuilt the RG table around universality, exponents, mean-field validity, relevant perturbations, epsilon expansion, 1D Ising, QFT bridge, and scaling relations. |
| `statistical-mechanics/07-ISING-MODELS.md` | Rebuilt the Ising selector tables around dimensional cases, Hopfield phases, BKT transition, and Monte Carlo diagnostics. |

## Gates

| Gate | Status |
|---|---|
| Proof + Da Vinci | PASS |
| Targeted editorial repair | PASS |
| R2 reference-editor panel | PASS |
| Consolidated Gold decision | PASS |

## Validation

```powershell
git --no-pager diff --check -- quantum-computing\04-HARDWARE-COMPLEXITY.md quantum-computing\06-QUANTUM-COMMUNICATION.md statistical-mechanics\06-RENORMALIZATION.md statistical-mechanics\07-ISING-MODELS.md
$proofOut = C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml quantum-computing\04-HARDWARE-COMPLEXITY.md quantum-computing\06-QUANTUM-COMMUNICATION.md statistical-mechanics\06-RENORMALIZATION.md statistical-mechanics\07-ISING-MODELS.md 2>&1; $proofOut; if ($proofOut -match 'FAIL') { exit 1 }
```

Result: PASS.

