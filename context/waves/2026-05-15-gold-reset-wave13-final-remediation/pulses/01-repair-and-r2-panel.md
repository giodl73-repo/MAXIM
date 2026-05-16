---
pulse: 01
title: Repair and R2 Panel
status: complete
---

# Pulse 01 - Repair and R2 Panel

## Scope

- `natural-sciences/06-BIOMOLECULES.md`
- `natural-sciences/07-ENZYMES.md`
- `natural-sciences/08-METABOLISM.md`
- `natural-sciences/09-MOLECULAR-BIO.md`

## Pre-implementation Scout

The guides were proof-clean and invariant-covered, but retained factory-era
question/concept/detail selector tables. Current Certified Gold requires
diagnostic reader-task support with explicit caveats.

## Changes

| Guide | Repair |
|---|---|
| `natural-sciences/06-BIOMOLECULES.md` | Rebuilt the biomolecules table around histidine catalysis, hydrophobic folding, DNA melting, fat packing, cellulose specificity, disulfide context, DNA/RNA chemistry, groove binding, cholesterol, and glycine flexibility. |
| `natural-sciences/07-ENZYMES.md` | Rebuilt the enzymes table around inhibition signatures, kcat/Km, cooperativity, BPG allostery, Km interpretation, phosphorylation, and synthase/synthetase nomenclature. |
| `natural-sciences/08-METABOLISM.md` | Rebuilt the metabolism table around glycolysis regulation, fatty acids, FADH2, brain fuel, lactate, Cori cycle, gluconeogenesis, NADPH, and fat energy density. |
| `natural-sciences/09-MOLECULAR-BIO.md` | Rebuilt the molecular-biology table around Okazaki fragments, origin licensing, Pol II capping, TATA boxes, alternative splicing, release factors, miRNA, PAM, Kozak sequence, and retroviral integration. |

## Gates

| Gate | Status |
|---|---|
| Proof + Da Vinci | PASS |
| Targeted editorial repair | PASS |
| R2 reference-editor panel | PASS |
| Consolidated Gold decision | PASS |

## Validation

```powershell
git --no-pager diff --check -- natural-sciences\06-BIOMOLECULES.md natural-sciences\07-ENZYMES.md natural-sciences\08-METABOLISM.md natural-sciences\09-MOLECULAR-BIO.md
$proofOut = C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml natural-sciences\06-BIOMOLECULES.md natural-sciences\07-ENZYMES.md natural-sciences\08-METABOLISM.md natural-sciences\09-MOLECULAR-BIO.md 2>&1; $proofOut; if ($proofOut -match 'FAIL') { exit 1 }
```

Result: PASS.

