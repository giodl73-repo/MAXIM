# R2 Consolidated Panel - Gold Reset Wave 34 Sample 2

## Verdict

PASS. The second Wave 34 reset sample satisfies Gold Rubric v2 after targeted
editorial repair, proof/Da Vinci validation, and guide-specific R2 review.

## Certified Scope

| Guide | Score | Invariant | Decision |
|---|---:|---|---|
| `energy-systems/09-HYDROPOWER.md` | 4.6 | `hydropower-landscape` | Certified Gold |
| `energy-systems/10-GRID-DISPATCH.md` | 4.6 | `grid-dispatch-job-scheduling` | Certified Gold |
| `entomology/00-OVERVIEW.md` | 4.6 | `arthropod-tree-of-life` | Certified Gold |

## Evidence Categories

| Required Evidence | Result |
|---|---|
| Proof output parsed for literal `FAIL` | PASS: focused command exited cleanly and contained no `FAIL` |
| Da Vinci invariants | PASS: all three scoped invariants present |
| Guide-specific rubric notes | PASS: see `R2-reference-editor.md` |
| Adversarial findings | PASS: lookup-table, hydropower dispatchability, grid optimization, BESS/DR, insect biomass, decline, and termite-classification issues repaired |
| Reader-task check | PASS: all three guides now support diagnostic reader decisions |
| BLOCK/WARN status | PASS: no remaining BLOCK or WARN findings |

## Reader-Task Checks

| Guide | Reader Task | Result |
|---|---|---|
| `energy-systems/09-HYDROPOWER.md` | Diagnose a hydro claim by separating reservoir storage, turbine head/flow fit, grid services, pumped-storage duration, methane risk, fish passage, and climate hydrology. | PASS |
| `energy-systems/10-GRID-DISPATCH.md` | Diagnose a dispatch claim by separating merit order, unit commitment, nodal prices, VRE curtailment, BESS state of charge, demand response, and reliability products. | PASS |
| `entomology/00-OVERVIEW.md` | Diagnose an entomology claim by separating arthropod/insect identity, order-level traits, metamorphosis, pollination dependency, decline metric, and termite phylogeny. | PASS |

## Certification Rule Applied

Factory hardening made these guides Candidate-Hardened. Current Certified Gold
is restored only because reset-era repair and this R2 panel supply guide-specific
evidence.

