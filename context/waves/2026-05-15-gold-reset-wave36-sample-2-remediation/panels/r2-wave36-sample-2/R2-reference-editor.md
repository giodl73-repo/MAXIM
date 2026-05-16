# R2 Reference Editor Review - Gold Reset Wave 36 Sample 2

## Scope

| Guide | Invariant |
|---|---|
| `formal-methods/03-THEOREM-PROVING.md` | `proof-assistant-landscape` |
| `formal-methods/04-TYPE-THEORY.md` | `type-theory-hierarchy` |
| `freshwater-biology/00-OVERVIEW.md` | `freshwater-biology-landscape` |

## Rubric Findings

### `formal-methods/03-THEOREM-PROVING.md`

| Dimension | Score | Note |
|---|---:|---|
| Landscape | 4.6 | Proof assistant foundations, kernels, automation, landmark proofs, and workflows are connected. |
| Diagrams | 4.5 | Landscape and LCF diagrams remain proof-clean and useful. |
| Conceptual accuracy | 4.6 | Tool recommendations now include trust-boundary caveats. |
| Peer tone | 4.6 | Speaks to verification architecture rather than proof-assistant tourism. |
| Bridges | 4.6 | Type-checker/proof-checker bridge remains strong. |
| Decision support | 4.7 | Cheat sheet now maps verification tasks to tools and watch-outs. |

Decision: PASS at 4.6.

### `formal-methods/04-TYPE-THEORY.md`

| Dimension | Score | Note |
|---|---:|---|
| Landscape | 4.6 | STLC, System F, F-omega, dependent types, HoTT, HM, Rust, TS, and C# variance form a coherent hierarchy. |
| Diagrams | 4.5 | Type-theory hierarchy remains proof-clean. |
| Conceptual accuracy | 4.6 | Lean/Mathlib univalence claim is corrected; HoTT is distinguished from mainstream Lean. |
| Peer tone | 4.6 | Leverages lambda-calculus and PL background appropriately. |
| Bridges | 4.7 | Bridges to Rust, TypeScript, C#, F#, and verification are practical. |
| Decision support | 4.7 | Cheat sheet now supports type-system selection and failure-mode reasoning. |

Decision: PASS at 4.6.

### `freshwater-biology/00-OVERVIEW.md`

| Dimension | Score | Note |
|---|---:|---|
| Landscape | 4.6 | Lakes, rivers, wetlands, groundwater, nutrients, food webs, conservation, and water quality are mapped. |
| Diagrams | 4.5 | Freshwater landscape diagram is proof-clean and useful. |
| Conceptual accuracy | 4.6 | Overview metrics are tied to guide-level mechanisms and monitoring frames. |
| Peer tone | 4.6 | Treats limnology as coupled physical/chemical/biological systems. |
| Bridges | 4.5 | Cross-links route the reader to concrete mechanisms. |
| Decision support | 4.7 | Cheat sheet now asks diagnostic freshwater questions instead of naming guide files. |

Decision: PASS at 4.6.

## Adversarial Closure

| Concern | Closure |
|---|---|
| Formal-methods guides could be tool catalogues rather than verification decision aids. | Repaired tables now ask verification and type-system questions with watch-outs. |
| Type Theory contained a false Lean/Mathlib univalence claim. | Text now states mainstream Lean/Mathlib is not univalent and uses other transfer machinery. |
| Freshwater overview could remain a guide index. | Repaired table now maps ecological problems to physical, chemical, biological, and watershed frames. |

No BLOCK or WARN findings remain for the scoped Gold claims.

