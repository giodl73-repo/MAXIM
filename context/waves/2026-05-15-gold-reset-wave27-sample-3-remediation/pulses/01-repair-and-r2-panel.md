---
pulse: 01
title: Repair and R2 Panel
status: complete
---

# Pulse 01 - Repair and R2 Panel

## Scope

- `computing/11-DOCKER.md`
- `computing/12-KUBERNETES.md`
- `computing/13-CICD.md`
- `computing/14-IAC.md`

## Pre-implementation Scout

The guides were proof-clean and invariant-covered, but retained factory-era
command/platform/tool selector tables without enough diagnostic caveats for
Current Certified Gold.

## Changes

| Guide | Repair |
|---|---|
| `computing/11-DOCKER.md` | Rebuilt the cheat sheet around packaging, local run, Compose, volumes, bind mounts, image size, registries, debugging, disk pressure, and Azure targets. |
| `computing/12-KUBERNETES.md` | Rebuilt the cheat sheet around Deployments, exposure, ingress, config/secrets, stateful workloads, autoscaling, rollout, packaging, tenancy, and platform choice. |
| `computing/13-CICD.md` | Rebuilt the cheat sheet around PR validation, merge blocking, image publish, Kubernetes deploy, approvals, artifacts, pipeline speed, matrix testing, cloud credentials, and private runners. |
| `computing/14-IAC.md` | Rebuilt the cheat sheet around Azure-only, multi-cloud, language IaC, config management, previews, state, modules, infra CI/CD, imports, and environment separation. |

## Gates

| Gate | Status |
|---|---|
| Proof + Da Vinci | PASS |
| Targeted editorial repair | PASS |
| R2 reference-editor panel | PASS |
| Consolidated Gold decision | PASS |

## Validation

```powershell
git --no-pager diff --check -- computing\11-DOCKER.md computing\12-KUBERNETES.md computing\13-CICD.md computing\14-IAC.md
$proofOut = C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml computing\11-DOCKER.md computing\12-KUBERNETES.md computing\13-CICD.md computing\14-IAC.md 2>&1; $proofOut; if ($proofOut -match 'FAIL') { exit 1 }
```

Result: PASS.

