# R2 Consolidated Panel - Gold Reset Wave 33 Sample 2

## Verdict

PASS. The electrical-grid Wave 33 sample satisfies Gold Rubric v2 after targeted
repair, proof/Da Vinci validation, and guide-specific R2 review.

## Certified Scope

| Guide | Score | Invariant | Decision |
|---|---:|---|---|
| `electrical-grid/00-OVERVIEW.md` | 4.6 | `electrical-grid-overview-stack` | Certified Gold |
| `electrical-grid/02-RENEWABLES.md` | 4.6 | `renewables-inverter-interface` | Certified Gold |
| `electrical-grid/03-TRANSMISSION.md` | 4.6 | `high-voltage-transmission-why` | Certified Gold |

## Evidence Categories

| Required Evidence | Result |
|---|---|
| Proof output parsed for literal `FAIL` | PASS: focused command exited cleanly and contained no `FAIL` |
| Da Vinci invariants | PASS: all three scoped invariants present |
| Guide-specific rubric notes | PASS: see `R2-reference-editor.md` |
| Adversarial findings | PASS: answer-table, grid-balance, inverter, curtailment, and AC/HVDC threshold issues repaired |
| Reader-task check | PASS: all three guides support diagnostic reader decisions |
| BLOCK/WARN status | PASS: no remaining BLOCK or WARN findings |

## Reader-Task Checks

| Guide | Reader Task | Result |
|---|---|---|
| `electrical-grid/00-OVERVIEW.md` | Diagnose a grid claim by separating instantaneous balance, frequency response, voltage support, capacity factor, net load, market price, and cascade risk. | PASS |
| `electrical-grid/02-RENEWABLES.md` | Diagnose a renewable-integration claim by separating PV yield, inverter control, wind resource, turbine technology, offshore economics, curtailment, and capture-price value. | PASS |
| `electrical-grid/03-TRANSMISSION.md` | Diagnose a transmission claim by separating voltage class, conductor mechanics, thermal/stability/voltage limits, HVDC fit, reactive power, and AC power-flow physics. | PASS |

## Certification Rule Applied

Factory hardening made these guides Candidate-Hardened. Current Certified Gold
is restored only because reset-era repair and this R2 panel supply guide-specific
evidence.

