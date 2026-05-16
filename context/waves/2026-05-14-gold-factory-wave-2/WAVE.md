# Gold Factory Wave 2

## Mission

Continue the factory model after the 24-guide wave, but keep the gate strict:
baseline-proof broad clusters, extract only the proof-clean promotion lane, and
defer noisy clusters to future diagram/table repair waves.

## Scope

| Guide | Promotion Target | Invariant |
|---|---|---|
| `abstract-algebra/02-SUBGROUPS-QUOTIENTS.md` | quotient and homomorphism exemplar | `quotients-homomorphisms-architecture` |
| `abstract-algebra/04-RINGS-IDEALS.md` | ring hierarchy exemplar | `ring-hierarchy` |
| `abstract-algebra/05-POLYNOMIALS-FIELDS.md` | field extension exemplar | `field-extensions-tower` |
| `abstract-algebra/06-GALOIS-THEORY.md` | Galois correspondence exemplar | `galois-correspondence` |
| `abstract-algebra/08-MODULES-LINEAR-ALGEBRA.md` | module theory exemplar | `modules-vector-spaces-over-rings` |
| `abstract-algebra/09-CATEGORY-THEORY.md` | category-theory language exemplar | `category-theory-structure-language` |
| `abstract-algebra/10-APPLICATIONS.md` | applied algebra exemplar | `abstract-algebra-applications` |
| `acoustics/07-UNDERWATER-ACOUSTICS.md` | underwater acoustics exemplar | `underwater-acoustics-applications` |
| `acoustics/08-ULTRASOUND.md` | ultrasound application exemplar | `ultrasound-frequency-application-map` |
| `acoustics/09-NOISE-VIBRATION.md` | noise/vibration control exemplar | `noise-vibration-control-framework` |
| `agriculture/04-MECHANIZATION-HISTORY.md` | mechanization-history exemplar | `mechanization-timeline` |
| `agriculture/06-GREEN-REVOLUTION.md` | Green Revolution systems exemplar | `green-revolution-yield-impacts` |

## Baseline Findings

| Finding | Resolution |
|---|---|
| Anthropology 02, 03, 05, 07, and 08 had multiple ASCII box drift errors | Deferred to a future anthropology diagram-healing wave |
| Number Theory and Topology candidate paths revealed overview/table/ASCII noise | Deferred to math repair lane rather than mixing with a Gold promotion |
| Abstract Algebra 03 and 07 had table pipe issues | Deferred; promoted only the clean abstract-algebra subset |
| Aeronautics 03-05 remained noisy from prior scouting | Kept in repair queue |
| Selected 12-guide cohort proofed clean before promotion | Added Cross-References and Da Vinci invariants, then re-proofed |

## Gold Rubric v2 Scores

| Guide | Explanation | Diagrams | Tables | Bridges | Cross-links | Proof | Overall |
|---|---:|---:|---:|---:|---:|---:|---:|
| `abstract-algebra/02-SUBGROUPS-QUOTIENTS.md` | 4.6 | 4.6 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |
| `abstract-algebra/04-RINGS-IDEALS.md` | 4.6 | 4.6 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |
| `abstract-algebra/05-POLYNOMIALS-FIELDS.md` | 4.6 | 4.6 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |
| `abstract-algebra/06-GALOIS-THEORY.md` | 4.7 | 4.6 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |
| `abstract-algebra/08-MODULES-LINEAR-ALGEBRA.md` | 4.6 | 4.6 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |
| `abstract-algebra/09-CATEGORY-THEORY.md` | 4.6 | 4.6 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |
| `abstract-algebra/10-APPLICATIONS.md` | 4.6 | 4.6 | 4.7 | 4.7 | 4.6 | 5.0 | 4.6 |
| `acoustics/07-UNDERWATER-ACOUSTICS.md` | 4.6 | 4.6 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |
| `acoustics/08-ULTRASOUND.md` | 4.6 | 4.6 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |
| `acoustics/09-NOISE-VIBRATION.md` | 4.6 | 4.6 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |
| `agriculture/04-MECHANIZATION-HISTORY.md` | 4.6 | 4.6 | 4.6 | 4.8 | 4.6 | 5.0 | 4.6 |
| `agriculture/06-GREEN-REVOLUTION.md` | 4.6 | 4.6 | 4.6 | 4.8 | 4.6 | 5.0 | 4.6 |

## Reader-Task Checks

| Task Family | Representative Pass |
|---|---|
| Algebraic structure | Quotients, rings, fields, Galois theory, modules, category theory, and applications form a coherent abstract-algebra ladder |
| Applied sound | Underwater acoustics, ultrasound, and noise/vibration complete the acoustics application surface after the first factory wave |
| Agricultural modernization | Mechanization and the Green Revolution connect labor substitution, platform dependencies, genetics, chemistry, and irrigation |

## Validation

```powershell
git -C C:\src\maxim diff --check
Set-Location -LiteralPath C:\src\maxim
C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml abstract-algebra\02-SUBGROUPS-QUOTIENTS.md abstract-algebra\04-RINGS-IDEALS.md abstract-algebra\05-POLYNOMIALS-FIELDS.md abstract-algebra\06-GALOIS-THEORY.md abstract-algebra\08-MODULES-LINEAR-ALGEBRA.md abstract-algebra\09-CATEGORY-THEORY.md abstract-algebra\10-APPLICATIONS.md acoustics\07-UNDERWATER-ACOUSTICS.md acoustics\08-ULTRASOUND.md acoustics\09-NOISE-VIBRATION.md agriculture\04-MECHANIZATION-HISTORY.md agriculture\06-GREEN-REVOLUTION.md
C:\src\proof\target\debug\proof.exe check -e --no-fail context\gold\REGISTRY.md context\waves\2026-05-14-gold-factory-wave-2\WAVE.md context\waves\PHASES.md
```

## Decision

Promote all twelve selected guides to Certified Gold. Keep the noisy candidates
explicitly deferred instead of lowering the factory gate.
