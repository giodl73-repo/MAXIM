---
pulse: 01
title: Repair and R2 Panel
status: complete
---

# Pulse 01 - Repair and R2 Panel

## Scope

Repair and certify the fifth Wave 34 reset sample:

- `entomology/07-INSECT-ECOLOGY.md`
- `entomology/08-ECONOMIC-ENTOMOLOGY.md`
- `entomology/09-FORENSIC-MEDICAL.md`

## Pre-implementation Scout

Command:

```powershell
C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml entomology\07-INSECT-ECOLOGY.md entomology\08-ECONOMIC-ENTOMOLOGY.md entomology\09-FORENSIC-MEDICAL.md
```

Scout result: proof-clean with Da Vinci invariants present. Editorial review
found Gold-blocking issues around lookup-style cheat sheets, overbroad insect
food-web phrasing, brittle pest-threshold tables, outdated corn-borer framing,
and forensic PMI wording that sounded more exact than insect evidence permits.

## Changes

| Guide | Repair |
|---|---|
| `entomology/07-INSECT-ECOLOGY.md` | Reframed insects' food-web roles and rebuilt the cheat sheet around population growth, regulation, degree-days, outbreaks, aquatic indicators, food webs, migration, and climate diagnostics. |
| `entomology/08-ECONOMIC-ENTOMOLOGY.md` | Updated European corn borer currentness, replaced brittle pest-threshold lookup table with diagnostic IPM support, and emphasized EIL/ET, biocontrol, Bt, resistance, threshold, and invasive-pest diagnostics. |
| `entomology/09-FORENSIC-MEDICAL.md` | Reframed forensic entomology around minimum PMI and uncertainty, and rebuilt the cheat sheet around PMI, succession, degree-days, vector competence, vectorial capacity, malaria/arbovirus control, and tick-borne disease diagnostics. |

## Gates

| Gate | Status |
|---|---|
| Proof + Da Vinci | PASS |
| Targeted editorial repair | PASS |
| R2 reference-editor panel | PASS |
| Consolidated Gold decision | PASS |

## Validation

```powershell
git --no-pager diff --check -- entomology\07-INSECT-ECOLOGY.md entomology\08-ECONOMIC-ENTOMOLOGY.md entomology\09-FORENSIC-MEDICAL.md
$proofOut = C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml entomology\07-INSECT-ECOLOGY.md entomology\08-ECONOMIC-ENTOMOLOGY.md entomology\09-FORENSIC-MEDICAL.md 2>&1; $proofOut; if ($proofOut -match 'FAIL') { exit 1 }
```

Result: PASS.

