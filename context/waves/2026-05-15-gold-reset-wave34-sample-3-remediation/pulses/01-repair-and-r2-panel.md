---
pulse: 01
title: Repair and R2 Panel
status: complete
---

# Pulse 01 - Repair and R2 Panel

## Scope

Repair and certify the third Wave 34 reset sample:

- `entomology/01-INSECT-BODY-PLAN.md`
- `entomology/02-DIVERSITY-CLASSIFICATION.md`
- `entomology/03-METAMORPHOSIS.md`

## Pre-implementation Scout

Command:

```powershell
C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml entomology\01-INSECT-BODY-PLAN.md entomology\02-DIVERSITY-CLASSIFICATION.md entomology\03-METAMORPHOSIS.md
```

Scout result: proof-clean with Da Vinci invariants present. Editorial review
found Gold-blocking issues around lookup-style cheat sheets, overly simple
tracheal size-limit language, termite classification wording, species-count
overprecision, holometaboly-origin certainty, and pupal memory overstatement.

## Changes

| Guide | Repair |
|---|---|
| `entomology/01-INSECT-BODY-PLAN.md` | Reframed the body plan as an engineering stack, caveated tracheal size limits, and rebuilt the cheat sheet around identity, cuticle, gas exchange, circulation, vision, mouthparts, flight muscle, and reproductive-structure diagnostics. |
| `entomology/02-DIVERSITY-CLASSIFICATION.md` | Corrected termite wording, replaced order lookup table with diagnostic order-identification support, and caveated described-species and social-insect claims. |
| `entomology/03-METAMORPHOSIS.md` | Caveated the holometaboly-origin model, rebuilt the cheat sheet around developmental diagnostics, and narrowed the Drosophila memory-survival claim. |

## Gates

| Gate | Status |
|---|---|
| Proof + Da Vinci | PASS |
| Targeted editorial repair | PASS |
| R2 reference-editor panel | PASS |
| Consolidated Gold decision | PASS |

## Validation

```powershell
git --no-pager diff --check -- entomology\01-INSECT-BODY-PLAN.md entomology\02-DIVERSITY-CLASSIFICATION.md entomology\03-METAMORPHOSIS.md
$proofOut = C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml entomology\01-INSECT-BODY-PLAN.md entomology\02-DIVERSITY-CLASSIFICATION.md entomology\03-METAMORPHOSIS.md 2>&1; $proofOut; if ($proofOut -match 'FAIL') { exit 1 }
```

Result: PASS.

