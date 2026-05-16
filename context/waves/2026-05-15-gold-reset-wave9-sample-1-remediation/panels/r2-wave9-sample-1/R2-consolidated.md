# R2 Consolidated Panel - Gold Reset Wave 9 Sample 1

## Verdict

PASS. The Wave 9 sequencing technology, genome assembly, personalized medicine,
and adaptive immunity sample satisfies Gold Rubric v2 after targeted repair,
proof/Da Vinci validation, and guide-specific R2 review.

## Certified Scope

| Guide | Score | Invariant | Decision |
|---|---:|---|---|
| `genomics/01-SEQUENCING-TECH.md` | 4.6 | `sequencing-technology-generations` | Certified Gold |
| `genomics/02-GENOME-ASSEMBLY.md` | 4.6 | `genome-assembly-graph-problem` | Certified Gold |
| `genomics/09-PERSONALIZED-MEDICINE.md` | 4.6 | `personalized-medicine-clinical-genomics` | Certified Gold |
| `immunology/02-ADAPTIVE-IMMUNITY.md` | 4.6 | `adaptive-immunity-ml-analogy` | Certified Gold |

## Evidence Categories

| Required Evidence | Result |
|---|---|
| Proof output parsed for literal `FAIL` | PASS: focused command exited cleanly and contained no `FAIL` |
| Da Vinci invariants | PASS: all four scoped invariants present |
| Guide-specific rubric notes | PASS: see `R2-reference-editor.md` |
| Adversarial findings | PASS: selector table issues repaired |
| Reader-task check | PASS: all four guides support diagnostic reader decisions |
| BLOCK/WARN status | PASS: no remaining BLOCK or WARN findings |

## Reader-Task Checks

| Guide | Reader Task | Result |
|---|---|---|
| `genomics/01-SEQUENCING-TECH.md` | Diagnose sequencing choices by separating small variants, validation, assembly, SVs, field sequencing, methylation, single-cell, spatial, T2T, and RNA-seq. | PASS |
| `genomics/02-GENOME-ASSEMBLY.md` | Diagnose assembly workflow by separating reference alignment, de novo assembly, SVs, chromosome-scale scaffolding, T2T, phasing, quality metrics, and pangenomes. | PASS |
| `genomics/09-PERSONALIZED-MEDICINE.md` | Diagnose clinical genomics by separating rare disease, cancer risk, tumor drivers, ctDNA, PGx, warfarin, abacavir, NIPT, PGT, screening, WGS, and immunotherapy biomarkers. | PASS |
| `immunology/02-ADAPTIVE-IMMUNITY.md` | Diagnose adaptive immunity by separating B/T maturation, thymic selection, MHC restriction, costimulation, cross-presentation, affinity maturation, AID, anergy, and CTLA-4. | PASS |

## Certification Rule Applied

Factory hardening made these guides Candidate-Hardened. Current Certified Gold
is restored only because reset-era repair and this R2 panel supply guide-specific
evidence.

