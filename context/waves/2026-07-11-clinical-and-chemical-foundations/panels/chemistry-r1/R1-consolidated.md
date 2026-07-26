# Chemistry R1 - Consolidated

## Decision

**PASS - no unresolved BLOCK or WARN findings.**

## Repair Summary

| Area | Result |
|---|---|
| Inorganic kinetics | Ni(II), Pd(II), and Pt(II) lability/inertness are no longer collapsed into one rule. |
| Synthesis design | Added competing disconnections, rejected alternatives, sequencing, and a bounded crossed-Claisen/reduction route. |
| Analytical chemistry | Updated to ICH Q2(R2)/Q14, qualified primary-method language, and specified electrochemical equation units. |
| Separations | Corrected selectivity to use adjusted retention factors and dead time. |
| NMR | Corrected geminal coupling, field scaling, and absent-NOE interpretation. |
| Crystallography | Bounded atom-position/absolute-configuration claims and corrected inversion-twin language. |
| Physical chemistry | Corrected canonical partition-function derivation and standard-state treatment; added an executable calculation. |
| Computational chemistry | Added an end-to-end reproducible workflow; corrected basis notation and RDKit logP; labeled unpinned values as expectations. |
| Measurement/safety | Corrected GUM Type A/B, coverage/tolerance handling, glove-selection logic, and reactive-class wording. |

## Validation

- Chemistry PROOF check: 12 files, 0 errors, 0 warnings.
- PROOF backfill: 12/12 round trips.
- CROP strict view inspection: all views valid.
- FLETCH registry: 61 entries, 0 findings.
- `git diff --check`: clean.

The module satisfies the wave quality gate: durable peer-level explanations,
conceptual diagrams, decision-useful tables, concrete reader tasks, explicit
ownership boundaries, and no unresolved adversarial findings.
