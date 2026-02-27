# Prerequisites — Volume Dependency Graph

*Which volumes assume knowledge from which other volumes. Most volumes are self-contained. This graph captures the ~30 hard dependencies where reading order genuinely matters.*

**How to read this**: If volume A appears in the "Assumes" column for volume B, you should read A before B (or at least have equivalent background). Volumes not listed here are standalone — pick them up in any order.

---

## Hard Dependencies

These are real prerequisites — the target volume uses notation, concepts, or frameworks introduced in the source without re-explaining them.

```
PREREQUISITE GRAPH — HARD DEPENDENCIES
═══════════════════════════════════════

J♣ mathematics / physics / electronics
 │
 ├──→ J♦ quantum-computing          (linear algebra, probability, Dirac notation)
 ├──→ J♦ control-theory             (Laplace transforms, transfer functions, state-space)
 ├──→ J♦ signal-processing          (Fourier analysis, complex exponentials, Z-transform)
 ├──→ J♦ information-theory         (probability, entropy, logarithms)
 ├──→ J♦ materials                  (quantum mechanics, crystal structure, band theory)
 ├──→ J♠ complex-analysis           (calculus, topology basics)
 ├──→ J♠ fluid-dynamics             (vector calc, PDEs, continuum mechanics)
 ├──→ J♠ statistical-mechanics      (probability, thermodynamics, partition functions)
 ├──→ J♠ partial-differential-eqs   (multivariable calculus, ODEs, boundary conditions)
 ├──→ J♠ variational-calculus       (calculus, Euler-Lagrange, functional analysis)
 ├──→ J♠ lie-groups                 (abstract algebra, topology, manifolds)
 ├──→ 7♦ nuclear                    (nuclear physics from physics/, thermodynamics)
 └──→ 7♦ chemical-eng               (thermodynamics, kinetics, transport phenomena)

J♥ number-theory / abstract-algebra / topology / probability-statistics /
   differential-geometry / numerical-methods
 │
 ├──→ J♠ complex-analysis           (topology, algebra for Riemann surfaces)
 ├──→ J♠ lie-groups                 (abstract algebra groups/rings, diff-geo manifolds)
 ├──→ J♠ variational-calculus       (functional analysis, measure theory from prob-stats)
 └──→ J♠ statistical-mechanics      (probability distributions, partition functions)

5♣ natural-sciences / biology / botany / ecology
 │
 ├──→ 5♦ neuroscience               (cell biology, ion channels, membrane potential)
 ├──→ 5♦ cognitive-science           (neuroscience basics, information processing)
 ├──→ 5♥ medicine                    (human biology, physiology, pathology)
 ├──→ 5♥ genomics                    (molecular biology, DNA/RNA, gene expression)
 ├──→ 5♥ immunology                  (cell biology, molecular recognition)
 ├──→ 5♠ evolutionary-biology        (genetics, population biology, ecology)
 ├──→ 5♠ biophysics                  (physics + biology — both required)
 └──→ 5♠ pharmacology                (biochemistry, receptor biology, metabolism)

K♣ computing / ai-engineering / data-science
 │
 ├──→ K♦ languages                   (package management, build tools, runtime models)
 ├──→ K♦ os                          (processes, memory, filesystems, networking)
 ├──→ K♥ cryptography                (number theory helps; computing/25-SECURITY assumed)
 └──→ K♥ machine-learning-theory     (probability, optimization, data-science basics)

K♦ languages / query-languages / scripting / os
 │
 └──→ K♠ distributed-systems         (networking, concurrency, consensus)

7♣ mechanical / structural / aeronautics
 │
 ├──→ 7♦ energy-systems              (thermodynamics from mechanical/)
 ├──→ 7♥ hvac                        (thermodynamics, fluid mechanics, heat transfer)
 └──→ 7♠ manufacturing               (materials science, mechanical processes)

8♣ semiconductor-manufacturing / telecommunications / robotics
 │
 └──→ 8♠ nanotechnology              (semiconductor physics, lithography, materials)

9♣ economics / finance / game-theory
 │
 ├──→ 9♦ political-science           (public choice theory, institutional economics)
 └──→ 9♠ international-relations     (game theory, political economy)

6♣ historical-geography / history-of-science / economic-history
 │
 ├──→ 6♥ intellectual-history        (base chronology of events and ideas)
 └──→ 6♥ social-history              (economic and geographic context)
```

---

## Soft Dependencies

These aren't prerequisites — you can read the target without the source — but the source adds significant context. The target volume will make more sense with this background.

| Target | Benefits from | Why |
|--------|--------------|-----|
| J♦ quantum-computing | K♥ cryptography | Post-quantum crypto motivation; Shor's algorithm context |
| J♦ control-theory | 7♣ mechanical | Physical systems that control theory governs |
| J♦ signal-processing | 7♠ acoustics | Audio/acoustic applications of DSP |
| 5♦ cognitive-science | 6♦ philosophy | Philosophy of mind, consciousness debates |
| 5♦ neuroscience | J♦ information-theory | Neural coding, mutual information, free energy |
| 7♠ acoustics | J♣ physics (waves) | Wave equation, impedance, resonance |
| 7♠ optics | J♣ physics (E&M) | Maxwell's equations, electromagnetic spectrum |
| 8♦ formal-methods | 6♥ logic | Predicate logic, proof theory, model checking |
| 8♦ systems-engineering | K♣ computing | Software architecture patterns, requirements engineering |
| Q♣ music-theory | J♣ physics (acoustics) | Harmonic series, Fourier decomposition of timbre |
| Q♣ architecture | 7♣ structural | Load paths, material properties, forces |
| Q♦ cartography | 3♥ geography | Map projections need geographic context |
| 9♣ game-theory | J♥ probability-statistics | Mixed strategies, Bayesian games |
| 9♣ behavioral-economics | 9♥ psychology | Cognitive biases, heuristics |
| 4♦ metalworking | J♦ materials | Crystal structure, phase diagrams, heat treatment |
| 4♦ ceramics | 5♣ natural-sciences (chemistry) | Silicate chemistry, sintering, vitrification |
| 3♣ astronomy | J♣ physics | Gravity, nuclear fusion, spectroscopy |
| 3♦ climate-science | J♣ physics + 3♣ geology | Radiation balance, carbon cycle, ocean circulation |
| A♣–A♠ People | The sections they belong to | Biographies assume field context |

---

## The Independence Principle

**Most volumes are deliberately self-contained.** The style contract requires each guide to open with a landscape diagram and build from first principles within its domain. A reader should be able to pick up any volume and get value.

The dependencies above are exceptions — cases where a volume genuinely builds on another's notation or framework. If you're reading linearly through a section (I → II → III → IV), the dependencies are already satisfied by design. They only matter when jumping across sections.

**Rule of thumb**: Within a section, read Foundation (♣) before Frontier (♠). Across sections, check this graph.

---

## Section Reading Order (within each section)

Every section follows the same suit progression:

```
♣ Foundation → ♦ Application → ♥ Depth → ♠ Frontier
```

This is always safe. The ♣ volume introduces concepts that ♦ applies, ♥ deepens, and ♠ extends. No exceptions.

---

## Critical Paths (longest dependency chains)

```
1. THE MATHEMATICS TOWER (8 volumes deep)
   J♣ math/physics → J♥ abstract-algebra → J♠ lie-groups
                    → J♥ topology         → J♠ complex-analysis
                    → J♥ diff-geometry    → J♠ variational-calculus
                    → J♥ prob-stats       → J♠ statistical-mechanics

2. THE LIFE SCIENCES CHAIN (4 volumes deep)
   5♣ biology → 5♦ neuroscience → 5♦ cognitive-science → 5♥ medicine

3. THE COMPUTING STACK (4 volumes deep)
   K♣ computing → K♦ languages → K♦ os → K♠ distributed-systems

4. THE ENGINEERING LADDER (3 volumes deep)
   J♣ physics → 7♣ mechanical → 7♥ hvac
                              → 7♦ energy-systems
                              → 7♠ manufacturing
```

The Mathematics Tower is the deepest — J♠ (Frontier) assumes everything in J♣ (Foundation) and J♥ (Depth). This is the only section where the dependency chain runs 3+ volumes deep. Every other section tops out at 2.
