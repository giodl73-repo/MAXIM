# Reference Library — Tracker

**Status key:** ✅ Complete | 🔜 Stubs (files exist, content to write) | ❌ Not started

Each directory has a `STATUS.md` with its full file list.

---

## Summary Dashboard

| Directory | Files | Status |
|-----------|-------|--------|
| [`computing/`](computing/STATUS.md) | 28 | ✅ |
| [`ai-engineering/`](ai-engineering/STATUS.md) | 5 | ✅ |
| [`data-science/`](data-science/STATUS.md) | 17 | ✅ |
| [`mathematics/`](mathematics/STATUS.md) | 24 | ✅ |
| [`languages/`](languages/STATUS.md) | 19 | ✅ |
| [`query-languages/`](query-languages/STATUS.md) | 13 | ✅ |
| [`scripting/`](scripting/STATUS.md) | 10 | ✅ |
| [`os/`](os/STATUS.md) | 8 | ✅ |
| [`physics/`](physics/STATUS.md) | 10 | ✅ |
| [`electronics/`](electronics/STATUS.md) | 8 | ✅ |
| [`materials/`](materials/STATUS.md) | 7 | ✅ |
| [`neuroscience/`](neuroscience/STATUS.md) | 5 | ✅ |
| [`economics/`](economics/STATUS.md) | 5 | ✅ |
| [`information-theory/`](information-theory/STATUS.md) | 5 | ✅ |
| [`natural-sciences/`](natural-sciences/STATUS.md) | 18 | ✅ |
| [`astronomy/`](astronomy/STATUS.md) | 12 | ✅ |
| [`biology/`](biology/STATUS.md) | 7 | ✅ |
| [`quantum-computing/`](quantum-computing/STATUS.md) | 5 | ✅ |
| [`control-theory/`](control-theory/STATUS.md) | 5 | ✅ |
| [`finance/`](finance/STATUS.md) | 5 | ✅ |
| [`mechanical/`](mechanical/STATUS.md) | 6 | ✅ |
| [`structural/`](structural/STATUS.md) | 5 | ✅ |
| [`chemical-eng/`](chemical-eng/STATUS.md) | 6 | ✅ |
| [`nuclear/`](nuclear/STATUS.md) | 6 | ✅ |
| [`codes/`](codes/STATUS.md) | 10 | ✅ |
| [`world-languages/`](world-languages/STATUS.md) | 15 | ✅ |
| [`historical-geography/`](historical-geography/STATUS.md) | 18 | ✅ |
| [`periodic-table/`](periodic-table/STATUS.md) | 12 | ✅ |
| [`animal-phylogeny/`](animal-phylogeny/STATUS.md) | 13 | ✅ |
| [`mythology/`](mythology/STATUS.md) | 12 | ✅ |
| [`linguistics/`](linguistics/STATUS.md) | 10 | ✅ |
| [`music-theory/`](music-theory/STATUS.md) | 10 | ✅ |
| [`cognitive-science/`](cognitive-science/STATUS.md) | 10 | ✅ |
| [`human-biology/`](human-biology/STATUS.md) | 11 | 🔜 |
| [`disease/`](disease/STATUS.md) | 11 | 🔜 |
| [`medicine/`](medicine/STATUS.md) | 11 | 🔜 |
| [`philosophy/`](philosophy/STATUS.md) | 7 | 🔜 |
| [`aeronautics/`](aeronautics/STATUS.md) | 6 | 🔜 |

**Complete: 339 files | To write: 46 files (33 detailed stubs, 13 empty stubs)**

---

## Session Prompts

One-line agent prompt for each session. Read `CLAUDE.md` + the directory's `STATUS.md` before writing.

| Session | Directory | Prompt |
|---------|-----------|--------|
| 15 | `human-biology/` | Every major body system — musculoskeletal, cardiovascular, respiratory, nervous, endocrine, immune, digestive, renal, reproductive, integumentary + overview |
| 16 | `disease/` | All disease categories — bacterial, viral, fungal/parasitic/prion, cancer, cardiovascular, metabolic/endocrine, autoimmune, neurological/psychiatric, genetic/developmental, epidemiology |
| 17 | `medicine/` | All drug classes — antibiotics, antivirals/vaccines, cardiovascular, CNS, endocrine/metabolic, cancer, immunomodulators, respiratory/GI, anesthesia, diagnostics/imaging + overview |
| — | `philosophy/` | Classical + modal logic (Gödel bridge), epistemology, metaphysics, philosophy of mind, ethics (AI ethics), philosophy of science — MIT TCS bridges throughout |
| — | `aeronautics/` | Aerodynamics, propulsion (Brayton/Isp), flight mechanics (6-DOF), avionics (INS/FMS), structures (aeroelasticity) |

---

## Agent Prompt Template

```
You are writing session {N} of the reference library.

1. Read CLAUDE.md for style contract and learner profile
2. Read {directory}/STATUS.md for the full file list and planned coverage
3. Write every file listed. Follow computing/01-PACKAGE.md format exactly.
4. Each file: Big Picture diagram → layered sections → Decision Cheat Sheet → Common Confusion Points
5. Peer-level. No handholding. MIT TCS background assumed.
6. Update STATUS.md when done — mark all files ✅
```
