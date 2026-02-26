# Cooperative Game Theory — Coalitions, Fair Division, and Bargaining

## The Big Picture

Cooperative (coalitional) game theory asks: when agents can form binding agreements and
make side payments, which coalitions will form and how will they distribute the gains?
Instead of specifying individual strategies, it abstracts to the **value** each coalition
can guarantee itself.

```
+------------------------------------------------------------------+
|                COOPERATIVE GAME THEORY STRUCTURE                  |
|                                                                  |
|  PRIMITIVES                     SOLUTION CONCEPTS               |
|  ----------                     ----------------                |
|                                                                  |
|  (N, v) where:                  STABILITY:                      |
|  N = {1,...,n} players          Core — no coalition wants to    |
|  v: 2^N → ℝ                     defect from the grand coalition |
|  v(S) = what coalition S                                        |
|    can guarantee itself         FAIRNESS / UNIQUENESS:          |
|  v(∅) = 0                       Shapley value — unique fair     |
|                                  allocation (4 axioms)           |
|  TU game: transferable utility  Nucleolus — minimizes worst-     |
|  (money can flow freely)         case excess; unique; in core   |
|                                                                  |
|  BARGAINING (2-player):         NASH BARGAINING:                |
|  Disagreement point d           Maximizes (u₁-d₁)(u₂-d₂)       |
|  Feasible set U ⊆ ℝ²           (4 axioms → unique)              |
|                                                                  |
|  NON-COOPERATIVE FOUNDATION:    RUBINSTEIN ALTERNATING OFFERS:  |
|  Rubinstein (1982) shows         Unique SPE; converges to Nash   |
|  Nash bargaining solution        bargaining as δ → 1            |
|  as limiting case of SPE                                        |
+------------------------------------------------------------------+
```

---

## Formal Setup

### Characteristic Function Game

A **TU cooperative game** (transferable utility) is (N, v) where:
- N = {1, ..., n} — finite set of players
- v: 2^N → ℝ — **characteristic function** with v(∅) = 0
- v(S) = the **worth** of coalition S (what S can achieve independently)

**Superadditivity**: v(S ∪ T) ≥ v(S) + v(T) for disjoint S, T ⊆ N.
(Merging coalitions never hurts — motivation for forming the grand coalition N.)

**Convexity** (stronger): v(S ∪ T) + v(S ∩ T) ≥ v(S) + v(T) for all S, T ⊆ N.
Convex games always have non-empty cores and the Shapley value is always in the core.

### Imputations

An **imputation** is x ∈ ℝⁿ such that:
- **Efficiency**: Σᵢ xᵢ = v(N) (full distribution of grand coalition's value)
- **Individual rationality**: xᵢ ≥ v({i}) for all i (no one does worse than solo)

The set of imputations is a (n-1)-dimensional simplex.

---

## The Core

### Definition

The **core** is the set of allocations that no coalition can improve upon:

    Core(v) = { x ∈ ℝⁿ | Σᵢ xᵢ = v(N)  and  Σᵢ∈S xᵢ ≥ v(S) ∀S ⊆ N }

x is in the core iff coalition S cannot "block" — S cannot redistribute its worth v(S)
to make all members of S strictly better off.

```
  EXAMPLE: Three-player majority voting game
  v(S) = 1 if |S| ≥ 2, else v(S) = 0.

  Core conditions:
    x₁ + x₂ ≥ 1 (coalition {1,2} can guarantee 1)
    x₁ + x₃ ≥ 1
    x₂ + x₃ ≥ 1
    x₁ + x₂ + x₃ = 1

  Adding all three coalition conditions:
    2(x₁ + x₂ + x₃) ≥ 3  →  2 ≥ 3. Contradiction.

  Core is EMPTY. The majority game has no stable allocation.
  Any allocation can be blocked by a 2-player majority coalition.
```

### Bondareva-Shapley Theorem and LP Duality

**Definition**: A **balanced collection** of coalitions is a family {S₁, ..., Sₖ} with
weights {λₛ} such that for each player i:

    Σ_{S ∋ i} λₛ = 1    (each player is "covered" with total weight 1)

A game is **balanced** if for every balanced collection:

    Σₛ λₛ v(S) ≤ v(N)

**Theorem (Bondareva 1963, Shapley 1967)**: The core of (N, v) is non-empty iff the
game is balanced.

```
  LP DUALITY CONNECTION (MIT TCS bridge):

  The core non-emptiness question is equivalent to LP feasibility.

  PRIMAL (core feasibility):
  Find x ∈ ℝⁿ such that:
    Σᵢ xᵢ = v(N)
    Σᵢ∈S xᵢ ≥ v(S) for all S ⊆ N

  DUAL:
  Find λₛ ≥ 0 for each S ⊆ N such that:
    Σₛ∋ᵢ λₛ = 1 for all i ∈ N     (dual equality constraints)
    Σₛ λₛ v(S) ≤ v(N)              (dual objective ≤ v(N))

  Core is non-empty iff dual has no "bad" (infeasibility-certifying) solution.
  Bondareva-Shapley: core non-empty ⟺ balanced ⟺ LP primal feasible.

  Convex games are balanced (by a direct argument):
    λₛ = (|S|-1)!(n-|S|)!/n!  (Shapley weights) forms a balanced collection,
    and convexity ensures the inequality holds.
```

---

## The Shapley Value

### Axioms

**Efficiency (EFF)**: Σᵢ φᵢ(v) = v(N) (total value is distributed)
**Symmetry (SYM)**: If π(v)(S) = v(π(S)) for all S (symmetry under player relabeling),
then φᵢ(v) = φⱼ(v) whenever i and j are symmetric
**Null Player (NULL)**: If v(S ∪ {i}) = v(S) for all S (i adds nothing), then φᵢ(v) = 0
**Additivity (ADD)**: φ(v + w) = φ(v) + φ(w) for all games v, w

**Theorem (Shapley 1953)**: There is a unique value satisfying EFF + SYM + NULL + ADD:

### Shapley Value Formula

    φᵢ(v) = Σ_{S ⊆ N\{i}} [ |S|! (n-|S|-1)! / n! ] · [ v(S ∪ {i}) - v(S) ]

**Interpretation**: Average marginal contribution of player i over all orderings of players.

```
  ORDERING INTERPRETATION:

  Consider all n! orderings of players (permutations).
  In each ordering, player i arrives at some position.
  When i arrives: add i to the coalition already formed (predecessors).
  Marginal contribution = v(predecessors ∪ {i}) - v(predecessors)

  Shapley value = average marginal contribution over all n! orderings.

  WEIGHTS: |S|!(n-|S|-1)!/n!
  = probability that ordering has:
    - S as the set of players before i
    - n - |S| - 1 players after i
  = |S|! (orderings of S before i) × (n-|S|-1)! (orderings after) / n!
```

### Computation Example: Airport Game

```
  Three airlines: A (small plane, runway needs 1km),
                  B (medium, needs 2km),
                  C (large, needs 3km).

  Cost of runway of length k: c(k) = k.
  Coalition S's cost: c(max type in S)

  v(S) = cost savings = c(N) - c(N\S)  [reframe as savings game]

  Or: cost allocation game where v(S) = 0 (no savings from standing alone)
  and we want to allocate c(N) = 3 among A, B, C.

  Marginal cost of adding C beyond {A,B}: 3 - 2 = 1
  Marginal cost of adding B beyond {A}: 2 - 1 = 1
  Marginal cost of adding A to ∅: 1 - 0 = 1

  In any ordering, A always contributes 1, B contributes extra 1 only
  if B arrives after A (or B is first and covers up to 2km), C covers
  the last unit when C arrives.

  By symmetry of marginal contributions across orderings:
  φ_A = 1 (A always costs 1 in any ordering)
  φ_B - φ_A = 1 allocated to "medium category" users = B only
  φ_C - φ_B = 1 allocated to "large category" users = C only

<!-- @editor[content/P1]: Airport game computation shows draft working ("let me be exact") and approximate results — clean up to show definitive Shapley value derivation with all 6 orderings and verified arithmetic -->
  More precisely: φ_A = 11/6, φ_B = 5/6, φ_C = 3/6? — let me be exact.

  The cost game: c({A}) = 1, c({B}) = 2, c({C}) = 3, c({A,B}) = 2,
  c({A,C}) = 3, c({B,C}) = 3, c({N}) = 3.

  By nucleolus / Shapley for cost games:
  A pays: average over orderings of (marginal cost when A arrives)
  Ordering ABC: A first → pays 1. B arrives at cost 2, marginal 1. C at 3, marginal 1.
  Ordering ACB: A first → pays 1. C at 3, marginal 2. B next, marginal 0 (already 3).
  Ordering BAC: B first → pays 2. A arrives, no extra cost (runway already ≥ 1). C → 1.
  ...etc.

  Shapley value (cost): φ_A = 11/18 ≈ 0.61, φ_B = 7/9 ≈ 0.78, φ_C = 47/18 ≈ 2.61
  (sums to 3 = c(N)) — each airline pays their fair share based on runway usage.
```

### Alternative Axiomatization (Young 1985)

Replace ADD with **Monotonicity (MON)**: If v(S ∪ {i}) ≥ w(S ∪ {i}) for all S
(player i's marginal contribution weakly increases), then φᵢ(v) ≥ φᵢ(w).

Young proved: EFF + SYM + MON uniquely characterizes the Shapley value.
This is arguably more natural than additivity.

### SHAP Values in Machine Learning

Shapley values are used in **SHAP (SHapley Additive exPlanations)** for explainable AI:
- Treat each feature as a "player"
- v(S) = model prediction using only features in S (marginal over excluded features)
- φᵢ = Shapley value = feature i's average marginal contribution to predictions
- SHAP satisfies efficiency, symmetry, dummy, additivity — the Shapley axioms

---

## The Nucleolus

### Motivation

The core may be empty, or it may be large (many allocations). The **nucleolus** provides
a unique point that:
- Is in the core if the core is non-empty
- Is well-defined even if the core is empty
- Minimizes the "worst injustice" any coalition faces

### Definition

For allocation x, the **excess** of coalition S is:

    e(S, x) = v(S) - Σᵢ∈S xᵢ

(positive excess = coalition S is "unhappy" — they could do better on their own)

The **nucleolus** minimizes the maximum excess lexicographically:

    θ(x) = sorted vector of all excesses in decreasing order
    Nucleolus = argmin_x θ(x)  (lexicographic minimization)

```
  LEXICOGRAPHIC MINIMIZATION:

  First minimize the largest excess (worst-off coalition).
  Among allocations achieving that minimum, minimize the second-largest.
  Continue.

  Uniqueness: At each step, the minimization is a convex LP (minimize
  the maximum of linear functions). The constraint set shrinks
  monotonically. The nucleolus is unique.
```

**Properties**:
- Always unique
- Always in the core if the core is non-empty (since core = {x | max excess ≤ 0})
- Satisfies a form of fairness (lexicographically minimizes complaints)
- Computable via sequence of linear programs (Maschler-Peleg-Shapley 1979)

---

## Nash Bargaining Solution

### Setup

**Two-player bargaining game**: (U, d) where:
- U ⊆ ℝ² is the **feasible payoff set** (convex, compact)
- d = (d₁, d₂) ∈ U is the **disagreement point** (what happens if negotiation fails)
- Assume ∃ u ∈ U with u > d (gains from agreement exist)

### Nash Axioms

**Pareto Efficiency (PAR)**: The solution f(U, d) is not dominated in U.
**Symmetry (SYM)**: If (U, d) is symmetric and d₁ = d₂, then f₁ = f₂.
**Scale Invariance (SI)**: Affine transformations of payoffs don't change the solution
(utility is ordinal up to positive linear transformation).
**Independence of Irrelevant Alternatives (IIA)**: If U' ⊆ U and f(U, d) ∈ U', then
f(U', d) = f(U, d).

**Theorem (Nash 1950)**: The unique function satisfying PAR + SYM + SI + IIA is:

    f(U, d) = argmax_{u ∈ U, u ≥ d} (u₁ - d₁)(u₂ - d₂)

The **Nash Bargaining Solution (NBS)** maximizes the product of utility gains from
disagreement.

```
  GEOMETRIC INTERPRETATION:

  The NBS is the point on the Pareto frontier of U that maximizes
  the "Nash product" — the area of the rectangle from d to u.

  Disagreement  u₂
  point         |       Pareto frontier
  d             |      /
                |    *  ← NBS (max rectangle area from d)
                |  /  \
                |/    |
  ──────────────d─────+───► u₁
                      max (u₁-d₁)(u₂-d₂)
```

### Kalai-Smorodinsky Alternative

**IIA is controversial**: adding an option that no one would choose can change the solution
(IIA says it shouldn't). Kalai-Smorodinsky (1975) replace IIA with:

**Monotonicity**: If U ⊆ U' and the "ideal point" (max achievable payoffs separately)
stays the same, then f(U', d) ≥ f(U, d) component-wise.

**Kalai-Smorodinsky Solution**: the point on the Pareto frontier where u₁-d₁ / u₂-d₂
equals the ratio of the ideal payoffs. Proportionally fair in a different sense.

---

## Rubinstein Alternating Offers (1982)

### Setup

Non-cooperative bargaining: two players split a pie of size 1.

```
  PROTOCOL:
  Period 0: Player 1 proposes (x, 1-x).
  If Player 2 accepts: game ends with payoffs (x, 1-x).
  If Player 2 rejects:
  Period 1: Player 2 proposes (1-y, y).
  If Player 1 accepts: game ends with payoffs (δ₁(1-y), δ₂y).
  ...
  Discount factor: payoff at period t is discounted by δᵢᵗ.
```

### Unique SPE

**Theorem (Rubinstein 1982)**: The alternating offers game has a unique SPE:
- Player 1's share: x* = (1 - δ₂) / (1 - δ₁δ₂)
- Player 2's share: 1 - x* = δ₂(1 - δ₁) / (1 - δ₁δ₂)
- Agreement reached immediately in period 0.

**Derivation** (one-shot deviation principle):

```
  Let v₁ = SPE payoff to Player 1 when they propose (period 0 perspective).
  Let w₁ = SPE payoff to Player 1 when they respond (period 1 perspective).

  When Player 2 proposes (period 1):
    Player 2 offers Player 1 exactly δ₁·v₁ (making them indifferent to accept/reject)
    Player 2 gets: 1 - δ₁·v₁
    From Player 1's perspective at response: w₁ = δ₁·v₁

  When Player 1 proposes (period 0):
    Player 1 offers Player 2 exactly δ₂·(1 - δ₁·v₁)
    (Player 2's outside option: wait, get δ₂×(their share when they propose))
    Player 1 gets: v₁ = 1 - δ₂(1 - δ₁v₁) = 1 - δ₂ + δ₁δ₂v₁
    v₁(1 - δ₁δ₂) = 1 - δ₂
    v₁ = (1 - δ₂) / (1 - δ₁δ₂)   □
```

### Connection to Nash Bargaining

**Symmetric case**: δ₁ = δ₂ = δ.

    x* = (1 - δ) / (1 - δ²) = 1 / (1 + δ)

As δ → 1: x* → 1/2. Both players get equal share — the Nash bargaining solution for
the symmetric case with equal weights.

**General case**: as period length Δ → 0 (δᵢ = e^{-rᵢΔ} → 1), the Rubinstein SPE
converges to the Nash bargaining solution with bargaining weights proportional to 1/rᵢ
(less patient player = higher discount rate = smaller share).

```
  RUBINSTEIN → NASH BARGAINING:

  v₁ = (1 - δ₂)/(1 - δ₁δ₂)
     ≈ (r₂Δ)/((r₁ + r₂)Δ) as Δ → 0
     = r₂/(r₁ + r₂)

  So the patient player (small r) gets more of the surplus.
  This corresponds to NBS with weights α₁ = 1/r₁, α₂ = 1/r₂
  (generalized Nash product: (u₁-d₁)^α₁ (u₂-d₂)^α₂).

  Rubinstein provides the non-cooperative foundation for Nash bargaining:
  the axiomatic cooperative solution emerges as the unique SPE of a
  natural strategic protocol.
```

---

## Voting Power Indices

Cooperative game theory applies to voting: what is player i's **power** in a voting game?

**Simple game**: v(S) = 1 if S is a "winning coalition" (e.g., majority), else v(S) = 0.

**Shapley-Shubik Power Index**: Shapley value of the voting game. Player i's power =
probability that i is the "pivotal" voter — adds their vote to the coalition that flips
from losing to winning.

```
  Example: UN Security Council (simplified)
  5 permanent members (P1-P5), 10 elected members (E1-E10).
  Winning condition: ≥9 votes AND all 5 permanent members agree.

  Pivotal orderings:
  A permanent member is pivotal in the ordering where their
  addition tips the vote from ≤8 to ≥9 AND their veto matters.

  Shapley-Shubik: permanent members have disproportionately high power
  despite representing 5/15 of the Council numerically.
```

**Banzhaf Power Index**: Player i's power = (number of coalitions where i is critical) /
(total critical memberships). Doesn't weight orderings equally.

- Shapley-Shubik: probability-based, uses orderings (Shapley value = SS index)
- Banzhaf: non-normalized, pure counting of "swings"

---

## Decision Cheat Sheet

| Question | Concept | Notes |
|----------|---------|-------|
| Is this allocation stable? | Core | Check Σᵢ∈S xᵢ ≥ v(S) for all S |
| Does a stable allocation exist? | Bondareva-Shapley | Balanced game ↔ non-empty core |
| What is the "fair" allocation? | Shapley value | Unique under 4 axioms; average marginal contribution |
| Need a unique stable point | Nucleolus | Always in core; lex-min excess; compute via LP sequence |
| Two-player bargaining axiomatics | Nash bargaining | Max (u₁-d₁)(u₂-d₂); 4 axioms |
| Two-player bargaining strategically | Rubinstein | Unique SPE; δ → 1 gives NBS |
| Measuring voting power | Shapley-Shubik or Banzhaf | SS = probability pivotal; Bz = swing counting |
| Explain ML model features | SHAP values | Shapley value applied to feature coalitions |
| Cost sharing problem | Airport game / Shapley | Shapley allocates marginal costs fairly |

---

<!-- @editor[bridge/P2]: No explicit old-world bridge section — cooperative GT connects to the learner's background: LP duality (MIT), cost allocation in shared infrastructure (Azure shared services), fair division in org budgets, Shapley/SHAP for ML model interpretability -->
## Common Confusion Points

**"Core = Shapley value"**: These are completely different concepts. The core is a set
(possibly empty, possibly large). The Shapley value is a unique point (always exists,
may or may not be in the core). Convex games: Shapley value is always in the core.
General games: Shapley value can be outside the core.

**"Nucleolus is in the core"**: Nucleolus is in the core when the core is non-empty.
If the core is empty, the nucleolus still exists (it lexicographically minimizes the
maximum excess — the "least unhappy" allocation), but the maximum excess is positive.

**"Nash bargaining requires equal splits"**: Nash bargaining gives equal splits only
when the game is symmetric and players have equal disagreement points. The generalized
Nash bargaining solution has weights (u₁-d₁)^α₁(u₂-d₂)^α₂ where αᵢ is player i's
"bargaining power" — can model asymmetric situations.

**"Rubinstein gives equal split"**: Only as δ → 1 with equal discount rates. For
unequal discount rates, the impatient player gets less. First-mover advantage: player
proposing first gets x* = (1-δ₂)/(1-δ₁δ₂) > 1/2 when δ₂ < 1. As δ → 1 this advantage
vanishes.

**"Cooperative and non-cooperative game theory contradict each other"**: No — they model
different settings. Rubinstein demonstrates this explicitly: a cooperative solution (NBS)
emerges from a non-cooperative protocol (alternating offers). The cooperative approach
abstracts away the details of negotiation; the non-cooperative approach specifies them.
The results are consistent.

**"Shapley value is additive over games"**: Yes, by the additivity axiom. If v and w are
two games on the same player set, φ(v + w) = φ(v) + φ(w). This makes Shapley value
useful for combining multiple value sources (e.g., a project with multiple revenue streams).
It also makes SHAP values in ML interpretable — feature contributions are additive.
