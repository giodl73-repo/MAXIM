# R2 Reference Editor Review - Gold Reset Wave 27 Sample 3

## Scope

| Guide | Invariant |
|---|---|
| `computing/11-DOCKER.md` | `docker-packaging-problem` |
| `computing/12-KUBERNETES.md` | `kubernetes-docker-gap` |
| `computing/13-CICD.md` | `cicd-platforms` |
| `computing/14-IAC.md` | `iac-problem` |

## Rubric Findings

| Guide | Score | Note |
|---|---:|---|
| `computing/11-DOCKER.md` | 4.6 | Docker guidance now separates image construction, local/runtime differences, persistence, live mounts, registries, debug ephemerality, cleanup risk, and deployment target fit. |
| `computing/12-KUBERNETES.md` | 4.6 | Kubernetes guidance now separates workload, exposure, ingress, secrets, storage, autoscaling, rollout/migration, packaging, tenancy, and platform ownership caveats. |
| `computing/13-CICD.md` | 4.6 | CI/CD guidance now separates PR gates, branch protection, image provenance, deploy health, approvals, artifacts, caching, matrix scope, identity, and runner trust. |
| `computing/14-IAC.md` | 4.6 | IaC guidance now separates cloud scope, state safety, previews, modules, imports, CI/CD blast radius, and environment isolation. |

## Adversarial Closure

| Concern | Closure |
|---|---|
| Cheat sheets were command, platform, or tool selectors. | Rebuilt all four as diagnostic tables with "Start With" and "Key Caveat" columns. |
| Container/Kubernetes guidance risked operational shortcuts. | Added persistence, readiness, platform, rollback, stateful, and ownership caveats. |
| CI/CD/IaC guidance risked tool recipes without governance. | Added gates, provenance, identity, approval, state, module, import, and blast-radius caveats. |

No BLOCK or WARN findings remain for the scoped Gold claims.

