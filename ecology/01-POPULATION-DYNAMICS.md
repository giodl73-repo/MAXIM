# Population Dynamics — Growth Models, Lotka-Volterra, r/K, Metapopulation

## The Big Picture

Population dynamics is the quantitative core of ecology. The mathematical structure — differential equations, stability analysis, stochastic models — maps directly to systems theory and control theory. The same frameworks used to model predator-prey cycles appear in epidemiology (SIR models), pharmacokinetics, and even software deployment pipelines.

```
+---------------------------------------------------------------+
|              POPULATION DYNAMICS FRAMEWORK                     |
|                                                                |
|  SINGLE SPECIES           MULTI-SPECIES                       |
|  dN/dt = f(N, environment) dN₁/dt = f(N₁, N₂, ...)          |
|                                                                |
|  Exponential growth  ←→  Lotka-Volterra predator-prey        |
|  Logistic growth     ←→  Competition models                  |
|  Structured models   ←→  Mutualism models                    |
|  Stochastic models   ←→  Food web models                     |
|                                                                |
|  SPATIAL EXTENSION: Metapopulation (patch dynamics)          |
|  EVOLUTIONARY: r vs K selection; life history theory         |
+---------------------------------------------------------------+
```

---

## Single-Species Growth Models

### Exponential Growth

In a constant, unlimited environment:

```
DISCRETE:   N(t+1) = λN(t)     λ = finite rate of increase
CONTINUOUS: dN/dt = rN          r = intrinsic rate of natural increase

SOLUTION:   N(t) = N₀ × e^(rt)

r = b - d  (per capita birth rate minus death rate)
λ = e^r    (λ > 1 = growth; λ < 1 = decline; λ = 1 = stable)
```

**Doubling time** = ln(2)/r ≈ 0.693/r

Population doubles every 70/r% years (rule of 70 — same as finance compound interest).

### Logistic Growth — Density Dependence

Real populations can't grow without bound. At some carrying capacity K, births = deaths:

```
dN/dt = rN(1 - N/K)

WHERE:
  r = intrinsic rate of increase (maximal; at N→0)
  K = carrying capacity (equilibrium at N = K)
  (1 - N/K) = density-dependent damping term

SOLUTION: Sigmoidal (S-curve)
  N(t) = K / (1 + ((K-N₀)/N₀) × e^(-rt))

N << K: growth ≈ exponential (N/K ≈ 0)
N ≈ K/2: fastest growth (inflection point)
N → K: growth slows to zero
N > K: negative growth (population declines)
```

**Carrying capacity is not a fixed number** — K depends on resource availability, which changes with seasons, climate, human land use. "K" is a simplification; real populations track a moving target.

**Per capita growth rate vs density:**
```
r_actual = r_max × (1 - N/K)
At N=0: r_actual = r_max
At N=K: r_actual = 0
At N>K: r_actual < 0
```

---

## Lotka-Volterra Predator-Prey Model

Alfred Lotka (1925) and Vito Volterra (1926) independently derived the classic predator-prey equations:

```
PREY (N): dN/dt = rN - αNP
          [grows exponentially] - [killed by predators]

PREDATOR (P): dP/dt = βNP - dP
              [grows from prey] - [dies at rate d]

PARAMETERS:
  r = prey intrinsic growth rate
  α = predation rate (probability of predator-prey encounter → kill)
  β = conversion efficiency (prey eaten → predator offspring)
  d = predator mortality rate

EQUILIBRIUM (coexistence):
  N* = d/β   (prey level that sustains predators)
  P* = r/α   (predator level that controls prey)
```

**Dynamics — cyclic oscillations:**

```
PHASE PLANE:

P (predators)
^
|        → prey increasing, predators following
|    2  3
|   /  \
|  1    4
|   \  /
|    --
|
+-----------> N (prey)

1. Many prey, few predators: prey grow, predators grow
2. Many prey, many predators: predators suppress prey
3. Few prey, many predators: predators starve, decline
4. Few prey, few predators: prey recover, cycle repeats
```

**Classic example: Canadian lynx and snowshoe hare** (Hudson Bay Company fur records, 1845–1935). Hare population peaks precede lynx peaks by 1–2 years. Period: ~10 years. However, the cycle is not purely predator-prey — food availability, disease, and plant defenses all contribute.

**Phase-plane analysis:** The Lotka-Volterra system is a conservative nonlinear oscillator — the same mathematical structure as the simple pendulum (conservative Hamiltonian system). The "energy" conserved is V(N,P) = βN - d·ln(N) + αP - r·ln(P) (constant on each orbit). This means:
- Orbits are closed curves (neutrally stable) — no damping, no growth in amplitude
- The equilibrium (N*, P*) is a center, not a stable spiral — perturbations produce a different closed orbit, not a return to the same one
- Structurally unstable: adding any realistic nonlinearity (prey saturation, predator interference) converts neutrally stable cycles into either stable limit cycles (Rosenzweig-MacArthur) or damped spirals

**Limitations of L-V:** Neutral stability (cycles don't damp or grow — structurally unstable). Real systems have dampening or limit cycles due to nonlinear terms. Extensions: Rosenzweig-MacArthur model, Holling functional responses.

**Holling functional responses:**

```
TYPE I: Linear (passive filter feeders)
  Consumption ∝ N (constant proportion)

TYPE II: Saturating (most vertebrate predators)
  Consumption plateaus (handling time limits)
  At high N, predator is always handling prey
  → "Prey switching" + "low-density prey escape"

TYPE III: Sigmoidal (prey switching, learning predators)
  At low N: reduced hunting effort (other prey available)
  At medium N: switch + learn → rising
  At high N: saturates like Type II
  → Stabilizes predator-prey dynamics at low prey density
```

---

## r vs K Selection

MacArthur and Wilson (1967) described a life history continuum:

```
r-SELECTED                        K-SELECTED
(opportunistic)                   (equilibrium)

Early reproduction                Late reproduction
Many offspring                    Few offspring
Little parental care              High parental care
Short lifespan                    Long lifespan
Small body size (often)           Large body size (often)
Fast development                  Slow development
High juvenile mortality           Low juvenile mortality
Population tracks resources       Population near K
Colonizers of disturbed habitat   Dominate stable habitat
"Weedy" species                   "Climax" species

EXAMPLES:
Dandelion, mosquito, mouse        Elephant, whale, oak, eagle
Annual plants                     Long-lived trees
r/K is a continuum, not binary
```

**r/K selection is oversimplified** — Ecologists now prefer life history theory frameworks that explicitly model the trade-offs between current vs future reproduction, survival, and growth. But r/K is still useful as a conceptual shorthand.

---

## Age-Structured Population Models — Leslie Matrix

Real populations have age classes with different birth and death rates:

```
n(t+1) = M × n(t)

         [F₀  F₁  F₂  F₃]   [n₀(t)]   [n₀(t+1)]
         [P₀  0   0   0 ]   [n₁(t)]   [n₁(t+1)]
M × n =  [0   P₁  0   0 ] × [n₂(t)] = [n₂(t+1)]
         [0   0   P₂  0 ]   [n₃(t)]   [n₃(t+1)]

Where:
  Fᵢ = fecundity of age class i
  Pᵢ = survival probability from age i to i+1

EIGENVALUE OF M = dominant λ = finite rate of increase
  λ > 1: population growing
  λ = 1: stable
  λ < 1: declining

EIGENVECTOR = stable age distribution
              (relative proportion in each age class at equilibrium)
```

**Linear algebra connection:** The Leslie matrix M is a non-negative matrix (entries ≥ 0). By the Perron-Frobenius theorem, a primitive non-negative matrix has a unique dominant real eigenvalue λ₁ > 0, and the corresponding eigenvector has all positive entries. This is exactly the stable age distribution — power iteration on M converges to the dominant eigenvector regardless of initial age distribution n(0). The rate of convergence to the stable age distribution is governed by |λ₂/λ₁| (ratio of second to first eigenvalue magnitude). Sensitivity of λ₁ to matrix entries = elasticity analysis — which entry has proportionally the largest effect on population growth rate.

**Sensitivity analysis** — which age class contributes most to population growth? Depends on species life history. For long-lived species (elephant seals), adult survival matters most. For short-lived species, juvenile survival or fecundity. Conservation implication: target the life stage that most limits population growth.

---

## Metapopulation Theory

Levins (1969): A "population of populations" — a network of local populations connected by dispersal, each subject to local extinction and recolonization:

```
CLASSIC LEVINS METAPOPULATION:
  p = fraction of patches occupied
  dp/dt = cp(1-p) - ep

  c = colonization rate
  e = extinction rate

  EQUILIBRIUM: p* = 1 - e/c
  CONDITION for metapopulation persistence: c > e

  IMPLICATION: Even if e > 0 (local populations always go extinct),
               the metapopulation can persist if c is large enough
```

**Source-sink dynamics:**
- **Source** patches: high-quality habitat; local birth > death; exports emigrants
- **Sink** patches: low-quality habitat; local death > birth; sustained only by immigration from sources

**Mainland-island model:** One large, never-extinct "mainland" source + many small islands. Islands go extinct but are recolonized from mainland. Different from Levins (no mainland → patch model).

**Distributed systems parallel:** Source-sink dynamics map directly onto primary/replica patterns. Source patches (birth > death, net emigration) are primaries: they generate more than they consume and export the surplus. Sink patches (death > birth, sustained by immigration) are replicas: they would fail without the continuous replication stream from the primary. A metapopulation fails if sources are removed — even if many sinks remain occupied (they're all running on borrowed time). In service mesh terms: source patches are the healthy nodes that route traffic (emigrants) to downstream nodes; isolate them with habitat fragmentation and the entire mesh fails.

**Conservation implication of metapopulation theory:**
- Habitat connectivity is critical — without dispersal corridors, patches become isolated → higher local extinction probability
- Even a species abundant in some patches may be threatened if those patches are isolated
- Northern spotted owl conservation: old-growth forest patches as network

---

## Stochastic Demography — Extinction Risk

Small populations face extinction risks beyond deterministic dynamics:

```
STOCHASTIC RISKS:
  Environmental stochasticity: year-to-year variation in r
    (droughts, harsh winters) → variance adds

  Demographic stochasticity: random deaths/births in small N
    (even at K=0 average drift, small N → random extinction)
    Important when N < ~100 individuals

  Genetic: inbreeding depression, loss of adaptive variation
    (minimum viable population: MVP ~50-500 individuals)

  Allee effects: positive density dependence at low N
    (hard to find mates; reduced anti-predator defense)
    → Below Allee threshold, population → 0 even with resources
```

**Minimum viable population (MVP)** — population size below which extinction is likely within a specified time. Rule of thumb (50/500 rule): ≥50 to avoid inbreeding depression short-term; ≥500 for long-term adaptive potential (Franklin 1980). More nuanced analyses: MVP depends on life history, environmental variability, and threat type.

---

## Decision Cheat Sheet

| Population question | Model to use |
|--------------------|-------------|
| Is population growing/declining? | Calculate r or λ from census data |
| When will population reach carrying capacity? | Logistic model; K = resource-limited ceiling |
| Will predator-prey cycle? | Lotka-Volterra; check if α, β, r, d allow coexistence |
| Which age class to protect? | Leslie matrix + sensitivity/elasticity analysis |
| Can habitat patch support population? | Metapopulation: is colonization > extinction? |
| Is small population at extinction risk? | MVP analysis; assess Allee effect thresholds |

---

## Common Confusion Points

**Logistic growth "carrying capacity K" is not a law of nature** — K is an emergent property of resource availability. Human infrastructure can change K (agriculture raises K for humans; deforestation lowers K for many species). K is not a magic number built into a species — it's a population × environment interaction.

**Lotka-Volterra cycles are neutrally stable** — In the basic model, cycles have constant amplitude (neutrally stable); they don't damp down or blow up. Real-world cycles generally show one or the other, suggesting additional biological mechanisms. The model captures the *type* of dynamics, not the quantitative reality.

**r vs K is about allocation, not success** — Both r-selected and K-selected species are evolutionarily successful in their environments. Calling K-selected species "more advanced" is wrong. Mosquitoes and dandelions are extraordinarily successful precisely because of their r-selected traits.

**"Invasive" ≠ "r-selected"** — Some invasive species are K-selected (large slow-reproducing species like Burmese pythons, lionfish). The key invasive characteristic is being released from natural enemies (enemy release hypothesis), not always fast reproduction.