---
wave: second-gold-promotion
date_open: 2026-05-14
date_close: 2026-05-14
status: complete
source_wave: next-gold-candidate-nominations
---

# Second Gold Promotion

## Mission

Run the first post-pilot Gold scoring panel and promote the next cross-section of
guides only if proof, invariants, reader tasks, and rubric scores agree.

## Mechanical Gate

```powershell
C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail natural-sciences\01-ATOMIC-QUANTUM.md pigments\01-PREHISTORIC-EARTH.md computer-architecture\01-ISA-FUNDAMENTALS.md proof.toml
```

Result: pass.

## R1 Score Table

| Guide | Tier | Average | Decision |
|---|---:|---:|---|
| `natural-sciences/01-ATOMIC-QUANTUM.md` | Gold | 4.6 | Quantum-to-chemistry ladder is dense, accurate, and well bridged to numerical methods |
| `pigments/01-PREHISTORIC-EARTH.md` | Gold | 4.6 | Strong chemistry/craft/archaeology synthesis; opening figure repaired and protected |
| `computer-architecture/01-ISA-FUNDAMENTALS.md` | Gold | 4.7 | Excellent systems bridge from ISA to compiler, micro-ops, and memory models |

## Dimension Scores

| Dimension | Atomic Quantum | Earth Pigments | ISA |
|---|---:|---:|---:|
| Landscape power | 5 | 5 | 5 |
| Layering integrity | 5 | 5 | 5 |
| ASCII precision | 4 | 5 | 5 |
| Explanatory compression | 4 | 5 | 5 |
| Decision utility | 5 | 4 | 5 |
| Confusion handling | 5 | 4 | 5 |
| Bridge quality | 5 | 4 | 5 |
| Cross-reference value | 5 | 5 | 5 |
| Voice | 4 | 5 | 5 |
| Factual confidence | 4 | 4 | 4 |

## Reader Task Results

| Guide | Reader Tasks Pass? | Notes |
|---|---|---|
| Atomic Quantum | yes | Explains why hydrogen is exact, why multi-electron atoms need approximation, where spectroscopy validates the model, and which computational method to choose |
| Earth Pigments | yes | Explains pigment chemistry, prehistoric manufacturing, durability, and conservation/craft consequences |
| ISA Fundamentals | yes | Explains RISC/CISC tradeoffs, x86 decode reality, instruction formats, and language-memory-model mapping |

## Content Actions Completed

| Action | File |
|---|---|
| Repaired fragile nested opening diagram | `pigments/01-PREHISTORIC-EARTH.md` |
| Added cross-reference table | `natural-sciences/01-ATOMIC-QUANTUM.md` |
| Added cross-reference table | `pigments/01-PREHISTORIC-EARTH.md` |
| Added cross-reference table | `computer-architecture/01-ISA-FUNDAMENTALS.md` |

## Closeout

The Gold Registry now has eight certified guides across computing, distributed
systems, atlas, chemistry, music, material culture, and computer architecture.
The promotion process is repeatable: nominate, protect, score, polish, promote.
