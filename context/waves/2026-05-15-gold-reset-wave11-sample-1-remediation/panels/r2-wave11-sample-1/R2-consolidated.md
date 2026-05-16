# R2 Consolidated Panel - Gold Reset Wave 11 Sample 1

## Verdict

PASS. The Wave 11 antivirals/vaccines, cardiovascular drugs, CNS drugs, and
endocrine/metabolic drugs sample satisfies Gold Rubric v2 after targeted repair,
proof/Da Vinci validation, and guide-specific R2 review.

## Certified Scope

| Guide | Score | Invariant | Decision |
|---|---:|---|---|
| `medicine/02-ANTIVIRALS-VACCINES.md` | 4.6 | `antiviral-vaccine-platforms` | Certified Gold |
| `medicine/03-CARDIOVASCULAR-DRUGS.md` | 4.6 | `cardiovascular-drug-targets` | Certified Gold |
| `medicine/04-CNS-DRUGS.md` | 4.6 | `cns-drug-message-passing` | Certified Gold |
| `medicine/05-ENDOCRINE-METABOLIC.md` | 4.6 | `endocrine-metabolic-drug-targets` | Certified Gold |

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
| `medicine/02-ANTIVIRALS-VACCINES.md` | Diagnose antiviral therapy by separating pathogen, drug activation, resistance, suppression/cure distinction, timing, renal risk, and interaction caveat. | PASS |
| `medicine/03-CARDIOVASCULAR-DRUGS.md` | Diagnose cardiovascular drug selection by separating lipid, RAAS, HF, arrhythmia, anticoagulation, HIT, and ACS/PCI contexts. | PASS |
| `medicine/04-CNS-DRUGS.md` | Diagnose CNS therapeutics by separating depression/bipolar/psychosis/anxiety/seizure/pain/OUD states and monitoring or dependence caveats. | PASS |
| `medicine/05-ENDOCRINE-METABOLIC.md` | Diagnose endocrine/metabolic therapy by separating diabetes comorbidity, thyroid emergency sequencing, bone severity, gout phase, and screening constraints. | PASS |

## Certification Rule Applied

Factory hardening made these guides Candidate-Hardened. Current Certified Gold
is restored only because reset-era repair and this R2 panel supply guide-specific
evidence.

