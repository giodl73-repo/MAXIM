---
pulse: 01
title: Repair and R2 Panel
status: complete
---

# Pulse 01 - Repair and R2 Panel

## Scope

- `variational-calculus/07-DIRECT-METHODS.md`
- `variational-calculus/08-OPTIMAL-CONTROL.md`
- `variational-calculus/09-ML-CONNECTIONS.md`
- `statistical-mechanics/06-RENORMALIZATION.md`

## Pre-implementation Scout

The guides were proof-clean and invariant-covered; three retained factory-era
question/problem selector tables, while renormalization already had the target
diagnostic form. Current Certified Gold requires diagnostic reader-task support
with explicit caveats.

## Changes

| Guide | Repair |
|---|---|
| `variational-calculus/07-DIRECT-METHODS.md` | Rebuilt the table around existence, weak lower semicontinuity, quasiconvexity, coercivity, weak limits, relaxation, Gamma-convergence, and Sobolev embeddings. |
| `variational-calculus/08-OPTIMAL-CONTROL.md` | Rebuilt the table around E-L, PMP, LQR, HJB, adjoints, bang-bang control, Neural ODEs, and stochastic control. |
| `variational-calculus/09-ML-CONNECTIONS.md` | Rebuilt the table around gradient flow, momentum, Neural ODEs, natural gradient, optimal transport, Wasserstein distance, VAEs, mechanics-aware nets, diffusion, and interpolation. |
| `statistical-mechanics/06-RENORMALIZATION.md` | Confirmed existing diagnostic table covers universality, critical exponents, mean-field validity, relevant perturbations, epsilon expansion, 1D Ising, stat-mech/QFT bridge, and scaling relations. |

## Gates

| Gate | Status |
|---|---|
| Proof + Da Vinci | PASS |
| Targeted editorial repair | PASS |
| R2 reference-editor panel | PASS |
| Consolidated Gold decision | PASS |

## Validation

```powershell
git --no-pager diff --check -- variational-calculus\07-DIRECT-METHODS.md variational-calculus\08-OPTIMAL-CONTROL.md variational-calculus\09-ML-CONNECTIONS.md statistical-mechanics\06-RENORMALIZATION.md
$proofOut = C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml variational-calculus\07-DIRECT-METHODS.md variational-calculus\08-OPTIMAL-CONTROL.md variational-calculus\09-ML-CONNECTIONS.md statistical-mechanics\06-RENORMALIZATION.md 2>&1; $proofOut; if ($proofOut -match 'FAIL') { exit 1 }
```

Result: PASS.

