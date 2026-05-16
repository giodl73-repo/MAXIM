---
pulse: 01
title: Repair and R2 Panel
status: complete
---

# Pulse 01 - Repair and R2 Panel

## Scope

- `computing/15-OBSERVABILITY.md`
- `computing/16-MONOREPO.md`
- `computing/18-TESTING.md`
- `computing/20-AZURE.md`

## Pre-implementation Scout

The guides were proof-clean and invariant-covered, but retained factory-era
direct selector tables. These were insufficient for reset-era Gold because they
answered "what do I use" without exposing operational caveats.

## Changes

| Guide | Repair |
|---|---|
| `computing/15-OBSERVABILITY.md` | Rebuilt the cheat sheet around logs, metrics, traces, OTel, dashboards, alerting, KQL/LogQL, histograms, business events, SLOs, lock-in, Azure Monitor, and Pushgateway caveats. |
| `computing/16-MONOREPO.md` | Rebuilt the cheat sheet around workspaces, affected builds, remote cache, Turbo/Nx tradeoffs, pnpm, module boundaries, versioning, dependency graph, and filtered tests. |
| `computing/18-TESTING.md` | Rebuilt the cheat sheet around unit, component, integration, MSW, E2E, browser, visual, accessibility, snapshot, coverage, codegen, focused runs, and contract testing caveats. |
| `computing/20-AZURE.md` | Rebuilt the cheat sheet around Azure service category diagnosis rather than a lookup list. |

## Gates

| Gate | Status |
|---|---|
| Proof + Da Vinci | PASS |
| Targeted editorial repair | PASS |
| R2 reference-editor panel | PASS |
| Consolidated Gold decision | PASS |

## Validation

```powershell
git --no-pager diff --check -- computing\15-OBSERVABILITY.md computing\16-MONOREPO.md computing\18-TESTING.md computing\20-AZURE.md
$proofOut = C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml computing\15-OBSERVABILITY.md computing\16-MONOREPO.md computing\18-TESTING.md computing\20-AZURE.md 2>&1; $proofOut; if ($proofOut -match 'FAIL') { exit 1 }
```

Result: PASS.

