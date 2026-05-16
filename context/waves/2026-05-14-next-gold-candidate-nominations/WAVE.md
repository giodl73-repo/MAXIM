---
wave: next-gold-candidate-nominations
date_open: 2026-05-14
date_close: 2026-05-14
status: complete
source_wave: pilot-r3-gold-promotion
---

# Next Gold Candidate Nominations

## Mission

Move beyond the five-guide pilot by nominating the next cross-section of Gold
candidates and protecting their opening figures before a full scoring panel.

## Selection Logic

The sample intentionally spans three different strengths:

| Candidate | Why this one |
|---|---|
| `natural-sciences/01-ATOMIC-QUANTUM.md` | Natural World / science exemplar; strong quantum-to-chemistry landscape |
| `pigments/01-PREHISTORIC-EARTH.md` | Material Culture exemplar; chemistry, archaeology, and craft meet in one guide |
| `computer-architecture/01-ISA-FUNDAMENTALS.md` | Computing frontier-adjacent exemplar; directly serves the learner's systems background |

## Pulse Status

| Pulse | Status | Evidence |
|---|---|---|
| 01 - Candidate proof probe | DONE | Focused proof passes for all three nominated guides |
| 02 - Pigment diagram repair | DONE | `pigments/01-PREHISTORIC-EARTH.md` top landscape no longer uses fragile nested boxes |
| 03 - Da Vinci coverage | DONE | `proof.toml` adds `atomic-quantum-landscape`, `earth-pigments-iron-oxide`, and `isa-design-space` |
| 04 - Registry update | DONE | `context/gold/REGISTRY.md` lists the three guides as Gold candidates |

## Validation

```powershell
C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail natural-sciences\01-ATOMIC-QUANTUM.md pigments\01-PREHISTORIC-EARTH.md computer-architecture\01-ISA-FUNDAMENTALS.md proof.toml
```

## Closeout

The next Gold wave has concrete targets and mechanical protection. The next
step is a scoring panel, not another nomination pass.
