---
pulse: 01
title: Repair and R2 Panel
status: complete
---

# Pulse 01 - Repair and R2 Panel

## Scope

- `ethics/07-RESEARCH-ETHICS.md`
- `ethics/08-AI-ETHICS.md`
- `international-relations/08-FOREIGN-POLICY.md`
- `colors/01-COLOR-PHYSICS.md`

## Pre-implementation Scout

The guides were proof-clean and invariant-covered, but retained factory-era
framework selector and answer-key tables. Current Certified Gold requires
diagnostic reader-task support with caveats.

## Changes

| Guide | Repair |
|---|---|
| `ethics/07-RESEARCH-ETHICS.md` | Rebuilt the research ethics framework table around Nuremberg, Helsinki, Belmont, Common Rule, HIPAA, GDPR, and IRB-level caveats. |
| `ethics/08-AI-ETHICS.md` | Rebuilt the AI ethics selector around alignment, instrumental convergence, RLHF, fairness criteria, explainability, regulation, and autonomous weapons caveats. |
| `international-relations/08-FOREIGN-POLICY.md` | Rebuilt the foreign-policy framework table around rational actor, organizational process, bureaucratic politics, prospect theory, groupthink, two-level games, and coercive diplomacy caveats. |
| `colors/01-COLOR-PHYSICS.md` | Rebuilt the color physics answer key around Rayleigh/Mie scattering, sunsets, thin films, structural color, blackbody temperature, yellowing, and chromophore caveats. |

## Gates

| Gate | Status |
|---|---|
| Proof + Da Vinci | PASS |
| Targeted editorial repair | PASS |
| R2 reference-editor panel | PASS |
| Consolidated Gold decision | PASS |

## Validation

```powershell
git --no-pager diff --check -- ethics\07-RESEARCH-ETHICS.md ethics\08-AI-ETHICS.md international-relations\08-FOREIGN-POLICY.md colors\01-COLOR-PHYSICS.md
$proofOut = C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml ethics\07-RESEARCH-ETHICS.md ethics\08-AI-ETHICS.md international-relations\08-FOREIGN-POLICY.md colors\01-COLOR-PHYSICS.md 2>&1; $proofOut; if ($proofOut -match 'FAIL') { exit 1 }
```

Result: PASS.

