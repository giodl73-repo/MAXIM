---
pulse: 01
title: Repair and R2 Panel
status: complete
---

# Pulse 01 - Repair and R2 Panel

## Scope

- `medicine/06-CANCER-DRUGS.md`
- `disease/01-BACTERIAL.md`
- `disease/02-VIRAL.md`
- `disease/03-FUNGAL-PARASITIC-PRION.md`

## Pre-implementation Scout

The guides were proof-clean and invariant-covered, but retained factory-era
cancer/question selector tables. Current Certified Gold requires diagnostic
reader-task support with explicit caveats.

## Changes

| Guide | Repair |
|---|---|
| `medicine/06-CANCER-DRUGS.md` | Rebuilt the cancer-drugs table around CML, NSCLC, melanoma, breast, prostate, CLL, AML, ovarian BRCA, and MSI-H tumor-agnostic therapy. |
| `disease/01-BACTERIAL.md` | Rebuilt the bacterial table around Gram barriers, MRSA, cholera toxin, EHEC antibiotics, Listeria treatment, and biofilm resistance. |
| `disease/02-VIRAL.md` | Rebuilt the viral table around negative-strand RNA, HIV latency, influenza reassortment, CMV activation, neuraminidase inhibitors, and HCV SVR. |
| `disease/03-FUNGAL-PARASITIC-PRION.md` | Rebuilt the fungal/parasitic/prion table around antifungal targets, Aspergillus/Mucor, malaria relapse, toxoplasma reactivation, prion treatment limits, and PrP templating. |

## Gates

| Gate | Status |
|---|---|
| Proof + Da Vinci | PASS |
| Targeted editorial repair | PASS |
| R2 reference-editor panel | PASS |
| Consolidated Gold decision | PASS |

## Validation

```powershell
git --no-pager diff --check -- medicine\06-CANCER-DRUGS.md disease\01-BACTERIAL.md disease\02-VIRAL.md disease\03-FUNGAL-PARASITIC-PRION.md
$proofOut = C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml medicine\06-CANCER-DRUGS.md disease\01-BACTERIAL.md disease\02-VIRAL.md disease\03-FUNGAL-PARASITIC-PRION.md 2>&1; $proofOut; if ($proofOut -match 'FAIL') { exit 1 }
```

Result: PASS.

