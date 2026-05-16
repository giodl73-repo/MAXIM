---
pulse: 01
title: Repair and R2 Panel
status: complete
---

# Pulse 01 - Repair and R2 Panel

## Scope

- `cognitive-science/03-REASONING-JUDGMENT.md`
- `cognitive-science/04-LANGUAGE-THOUGHT.md`
- `cognitive-science/05-PROBLEM-SOLVING.md`
- `cognitive-science/06-DEVELOPMENT.md`

## Pre-implementation Scout

The guides were proof-clean and invariant-covered, but their cheat sheets were
answer or best-approach tables. Current Certified Gold requires diagnostic
reader-task support with caveats.

## Changes

| Guide | Repair |
|---|---|
| `cognitive-science/03-REASONING-JUDGMENT.md` | Rebuilt the bias/correction table around availability, representativeness, anchoring, framing, confirmation, planning fallacy, sunk cost, and loss aversion. |
| `cognitive-science/04-LANGUAGE-THOUGHT.md` | Rebuilt the language/thought table around color perception, number, Wason framing, neural networks, concepts, Language of Thought, and conceptual metaphor caveats. |
| `cognitive-science/05-PROBLEM-SOLVING.md` | Rebuilt the problem-solving table around search, heuristic space, representational change, mental set, analogy, incubation, and deliberate practice. |
| `cognitive-science/06-DEVELOPMENT.md` | Rebuilt the development table around object permanence, ZPD, false belief, marshmallow test, nature/nurture, and autism/ToM caveats. |

## Gates

| Gate | Status |
|---|---|
| Proof + Da Vinci | PASS |
| Targeted editorial repair | PASS |
| R2 reference-editor panel | PASS |
| Consolidated Gold decision | PASS |

## Validation

```powershell
git --no-pager diff --check -- cognitive-science\03-REASONING-JUDGMENT.md cognitive-science\04-LANGUAGE-THOUGHT.md cognitive-science\05-PROBLEM-SOLVING.md cognitive-science\06-DEVELOPMENT.md
$proofOut = C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml cognitive-science\03-REASONING-JUDGMENT.md cognitive-science\04-LANGUAGE-THOUGHT.md cognitive-science\05-PROBLEM-SOLVING.md cognitive-science\06-DEVELOPMENT.md 2>&1; $proofOut; if ($proofOut -match 'FAIL') { exit 1 }
```

Result: PASS.

