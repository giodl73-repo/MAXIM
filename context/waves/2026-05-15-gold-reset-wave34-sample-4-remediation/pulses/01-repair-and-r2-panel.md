---
pulse: 01
title: Repair and R2 Panel
status: complete
---

# Pulse 01 - Repair and R2 Panel

## Scope

Repair and certify the fourth Wave 34 reset sample:

- `entomology/04-EUSOCIALITY.md`
- `entomology/05-INSECT-PLANT.md`
- `entomology/06-POLLINATION.md`

## Pre-implementation Scout

Command:

```powershell
C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml entomology\04-EUSOCIALITY.md entomology\05-INSECT-PLANT.md entomology\06-POLLINATION.md
```

Scout result: proof-clean with Da Vinci invariants present. Editorial review
found Gold-blocking issues around lookup-style cheat sheets, overstrong eusocial
biomass and haplodiploidy language, single-molecule honey-bee queen claims,
overbroad insect-plant scale framing, and pollination/crop-dependence and
decline overclaims.

## Changes

| Guide | Repair |
|---|---|
| `entomology/04-EUSOCIALITY.md` | Reframed eusocial biomass and haplodiploidy claims, caveated queen-development mechanisms, and rebuilt the cheat sheet around eusociality, caste, bee/wasp/termite, and pheromone diagnostics. |
| `entomology/05-INSECT-PLANT.md` | Reframed insect-plant interactions without overclaiming exact scale and rebuilt the cheat sheet around herbivory, coevolution, plant defenses, counter-defenses, galls, mutualism, tritrophic signals, and monarch/milkweed diagnostics. |
| `entomology/06-POLLINATION.md` | Reframed pollination dependence by species, crop value, and calories; caveated decline and honey-bee claims; rebuilt the cheat sheet around crop dependence, syndromes, honey bees, buzz pollination, decline, pesticide, conservation, and deception diagnostics. |

## Gates

| Gate | Status |
|---|---|
| Proof + Da Vinci | PASS |
| Targeted editorial repair | PASS |
| R2 reference-editor panel | PASS |
| Consolidated Gold decision | PASS |

## Validation

```powershell
git --no-pager diff --check -- entomology\04-EUSOCIALITY.md entomology\05-INSECT-PLANT.md entomology\06-POLLINATION.md
$proofOut = C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml entomology\04-EUSOCIALITY.md entomology\05-INSECT-PLANT.md entomology\06-POLLINATION.md 2>&1; $proofOut; if ($proofOut -match 'FAIL') { exit 1 }
```

Result: PASS.

