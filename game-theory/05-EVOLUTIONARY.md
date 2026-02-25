# Evolutionary Game Theory and Algorithmic Game Theory

## The Big Picture

Two major extensions of classical game theory: evolutionary GT replaces rational deliberation
with selection pressure on strategies; algorithmic GT applies computational complexity
theory to the questions of strategic interaction.

```
+------------------------------------------------------------------+
|         EVOLUTIONARY AND ALGORITHMIC GAME THEORY                  |
|                                                                  |
|  EVOLUTIONARY GAME THEORY        ALGORITHMIC GAME THEORY        |
|  -------------------------        -------------------------       |
|  Maynard Smith / Price (1973)     Papadimitriou, Roughgarden,   |
|  Rational agents → populations    Tardos (2000s)               |
|  Strategies evolve by selection   Efficiency of equilibria      |
|                                                                  |
|  Key concepts:                    Key concepts:                 |
|  ESS — invasion resistance        Price of Anarchy (PoA)       |
|  Replicator dynamics              Price of Stability (PoS)     |
|  Hawk-Dove game                   Potential games              |
|  Kin selection / cooperation      Congestion games             |
|                                   PPAD-completeness of Nash     |
|                                                                  |
|  CONNECTION: No-regret learning   ←→  CE as stable state        |
|  MARL, AlphaGo, Pluribus          ←→  Nash in large game spaces |
+------------------------------------------------------------------+
```

---

## Evolutionary Game Theory

### From Rationality to Selection

Classical game theory assumes payoff-maximizing rational agents. Evolutionary GT replaces
this with: strategies that earn higher fitness (payoff) reproduce more. Over time, fitter
strategies dominate.

**Players** are not individuals — they are population states. **Strategies** are traits.
**Payoffs** are fitness. No deliberation required.

```
  CLASSICAL GT vs EVOLUTIONARY GT

  Classical:                        Evolutionary:
  Agent chooses strategy to         Strategy has fitness (expected payoff
  maximize expected payoff          vs population average)
  Equilibrium: no incentive         Equilibrium: no mutant can invade
  to deviate                        and spread
  Rational deliberation assumed     Selection mechanism does the work
  Static concept                    Dynamic process
  Nash ↔ fixed point of BR          ESS ↔ asymptotically stable state
                                    under replicator dynamics
```

### Replicator Dynamics

Let xᵢ be the fraction of the population playing strategy i. Let n strategies total.

**Fitness of strategy i**:  fᵢ(x) = Σⱼ xⱼ aᵢⱼ  where A = [aᵢⱼ] is the payoff matrix

**Average fitness**:  f̄(x) = Σᵢ xᵢ fᵢ(x) = xᵀAx

**Replicator equation**:

    ẋᵢ = xᵢ [fᵢ(x) - f̄(x)]

Strategies with above-average fitness grow; below-average shrink; average stays at 0.

**Properties**:
- Leaves the simplex invariant: if xᵢ ≥ 0 and Σᵢ xᵢ = 1, this holds for all t
- Interior equilibria: ẋᵢ = 0 iff fᵢ(x) = f̄(x) for all i with xᵢ > 0
- Corner equilibria (xᵢ = 1): always fixed points
- **Every Nash equilibrium is a fixed point of the replicator dynamics**
  (converse fails: stable fixed points are Nash, but unstable fixed points may be Nash)

```
  REPLICATOR DYNAMICS ON THE SIMPLEX (3 strategies)

       x₃ = 1
        △
       /|\
      / | \
     /  |  \
    /   |   \
   / ←  |  → \
  /_____|_____\
 x₁=1         x₂=1

  Each vertex = monomorphic population (all play one strategy)
  Interior point = polymorphic population
  Trajectories show how population composition evolves

  Nash equilibria correspond to rest points.
  ESS corresponds to asymptotically stable rest points.
```

**Fundamental theorem of natural selection** (analog): d/dt f̄(x) ≥ 0 in some cases
(not always — with frequency-dependent fitness, average fitness can decrease). The analog
is more nuanced than in standard population genetics.

---

## Evolutionary Stable Strategy (ESS)

### Definition

Strategy σ* is an **Evolutionary Stable Strategy (ESS)** if it can resist invasion by
any small mutant population playing σ ≠ σ*.

Formally: ∃ ε̄ > 0 such that for all σ ≠ σ* and all ε ∈ (0, ε̄):

    u(σ*, εσ + (1-ε)σ*) > u(σ, εσ + (1-ε)σ*)

The incumbent σ* outperforms any rare mutant σ in a population mostly playing σ*.

**Equivalent conditions**: σ* is ESS iff:

1. **u(σ*, σ*) > u(σ, σ*)** (strict Nash condition), OR
2. **u(σ*, σ*) = u(σ, σ*)** AND **u(σ*, σ) > u(σ, σ)**
   (equal fitness against incumbent but strict advantage against mutant)

```
  ESS CONDITIONS DECOMPOSED:

  Condition 1: σ* is a strict Nash equilibrium (strictly dominates all deviations)
               → σ* can immediately repel any invader

  Condition 2: σ* is a non-strict Nash but "stable against mutants"
               → Invaders get same fitness initially, but σ* does better in
                 mutant-vs-mutant encounters

  ESS IMPLIES NASH: If σ* is ESS, then σ* is NE.
  Proof: If σ* is not NE, ∃ σ with u(σ, σ*) > u(σ*, σ*).
  For small enough ε, u(σ, εσ + (1-ε)σ*) > u(σ*, εσ + (1-ε)σ*)
  (by continuity). So σ* fails the ESS definition. □

  NE DOES NOT IMPLY ESS:
  Condition: u(σ*, σ*) = u(σ, σ*) but u(σ*, σ) = u(σ, σ)
  → Non-strict NE; mutant does equally well in all encounters
  → Not ESS; mutant drifts to fixation (neutral drift)
```

### ESS and Replicator Dynamics

**Taylor-Jonker Theorem (1978)**: σ* is an ESS iff it is **asymptotically stable** under
the replicator dynamics.

- ESS → asymptotically stable (interior ESS attracts all nearby initial conditions)
- Asymptotically stable rest point → ESS (converse holds for interior rest points)
- The theorem provides a dynamical interpretation for ESS

**Rock-Paper-Scissors**: Unique interior Nash equilibrium (1/3, 1/3, 1/3). Under
replicator dynamics: periodic orbits around the interior fixed point (not asymptotically
stable). Therefore: the interior NE is NOT an ESS.

---

## Hawk-Dove Game

The canonical ESS example from biology.

```
  Context: Two animals contest a resource of value V.
  Hawk strategy: fight until opponent retreats or both injured.
  Dove strategy: display, retreat if opponent fights.

  Hawk-Hawk: both fight; winner gets V, loser pays C (injury cost).
             Expected payoff: (V - C)/2 each.
  Hawk-Dove: Hawk gets V, Dove retreats (no cost). (V, 0).
  Dove-Hawk: Dove retreats. (0, V). [symmetric]
  Dove-Dove: Display; each gets V/2 with no injury. (V/2, V/2).

  Matrix (row player's payoff):
              Hawk          Dove
  Hawk    (V-C)/2          V
  Dove       0            V/2
```

**Case 1: V > C** (resource worth more than injury cost)
- Hawk strictly dominates Dove
- Unique NE: (Hawk, Hawk) with payoff (V-C)/2 > 0
- ESS: Hawk is ESS (pure strategy, strict NE)

**Case 2: V < C** (fighting is costly)
- No pure strategy ESS
- Mixed ESS: p* = V/C (probability of Hawk)

```
  Mixed ESS computation:
  At mixed ESS x* = (p*, 1-p*), fitness must be equal:
  f_Hawk(x*) = f_Dove(x*)
  p*(V-C)/2 + (1-p*)·V = p*·0 + (1-p*)·V/2
  p*(V-C)/2 + V - p*V = V/2 - p*V/2
  p*(V-C)/2 = V/2 - p*V + p*V/2 - V + p*V = ... solving:
  p*(V-C)/2 + p*V = V - V/2 + p*V/2 + p*V/2 - p*V... (simplify directly)

  Equal fitness condition:
  p*(V-C)/2 + (1-p*)V = (1-p*)V/2
  LHS - RHS = p*(V-C)/2 + (1-p*)V - (1-p*)V/2 = 0
            = p*(V-C)/2 + (1-p*)V/2 = 0
  p*(V-C)/2 = -(1-p*)V/2
  p*(V-C) = -(1-p*)V
  pV - pC = -V + pV
  -pC = -V
  p* = V/C  ✓

  Population fraction V/C play Hawk, (1-V/C) play Dove.
  The mixed ESS is stable: if too many Hawks, injury cost exceeds benefit;
  Doves flourish. If too many Doves, Hawks do well; Hawk fraction grows.
```

---

## Cooperation: Kin Selection and Reciprocal Altruism

### Hamilton's Rule

**Kin selection**: organisms may sacrifice individual fitness to help relatives, because
relatives share genes.

**Hamilton's Rule (1964)**: An altruistic behavior evolves iff:

    r · b > c

where r = coefficient of relatedness, b = benefit to recipient, c = cost to actor.

```
  RELATEDNESS COEFFICIENTS:
  Identical twins: r = 1
  Parent-child:    r = 1/2
  Siblings:        r = 1/2
  Half-siblings:   r = 1/4
  First cousins:   r = 1/8

  Haldane's quip: "I would lay down my life for two brothers
  or eight cousins." (r·b > c: 2·(1/2) = 1 > 1, or 8·(1/8) = 1 > 1)

  Game theory interpretation:
  The payoff function includes effects on relatives weighted by r.
  Altruism is "selfish" from the gene's perspective.
```

### Iterated Prisoner's Dilemma and Reciprocal Altruism

Axelrod's tournaments (1980, 1984): submitted strategies played round-robin in iterated PD.
Tit-for-Tat (cooperate first; mirror opponent's last move) won both tournaments.

**Properties of TfT**:
- Nice: never defects first
- Provocable: immediately punishes defection
- Forgiving: returns to cooperation after opponent cooperates
- Clear: simple and predictable

But TfT is NOT an ESS against ALL strategies. Grim Trigger can do better; All-Defect
can invade a Tit-for-Tat population in noisy environments.

**Spatial structure**: In spatially structured populations (agents on a graph, interact
only with neighbors), cooperation can be sustained even in one-shot PD. Cooperating
clusters can be stable even against defectors at the boundary (Nowak-May 1992).

---

## Price of Anarchy and Price of Stability

### Motivation

When selfish agents make decisions (routing traffic, choosing servers, selecting strategies),
the resulting equilibrium may be inefficient. How much does selfishness cost?

```
  SOCIAL WELFARE = Σᵢ uᵢ(s)  (or some objective function)

  Optimum (OPT):   social planner controls all agents, maximizes SW
  Nash equilibrium: no one can unilaterally improve their utility

  PRICE OF ANARCHY (PoA) = OPT / (worst NE social welfare)
  (or worst NE cost / OPT for minimization problems)

  PRICE OF STABILITY (PoS) = OPT / (best NE social welfare)

  PoA ≥ PoS ≥ 1 (PoA ≤ PoS in cost minimization sense)
  PoA = 1: every NE is socially optimal
  PoA = 2: worst-case NE is half as good as optimum
```

### Braess's Paradox

```
  BRAESS'S PARADOX (1968): Adding a road can make everyone worse off.

  Original network (2000 drivers, A → D):
  ┌────────────────────────────────┐
  │                                │
  │  A ──x/100──► B ──50──► D     │
  │  A ──50────► C ──x/100──► D   │
  │                                │
  │  x = number of drivers on edge │
  │  Cost = latency (time to travel)│
  └────────────────────────────────┘

  With 1000 on each path:
  A→B→D: 1000/100 + 50 = 60 min.
  A→C→D: 50 + 1000/100 = 60 min.
  NE: 1000 on each path. Total cost = 60. PoA = 1.

  Add a free road from B to C:
  ┌────────────────────────────────┐
  │  A ──x/100──► B               │
  │               │               │
  │               0 (free edge)   │
  │               │               │
  │               ▼               │
  │  A ──50────► C ──x/100──► D  │
  │               (also B→D: 50) │
  └────────────────────────────────┘

  New NE: All 2000 drivers take A→B→C→D (the zero-cost detour is attractive):
  Cost: 2000/100 + 0 + 2000/100 = 20 + 0 + 20 = 40... wait.

  Let's be precise: with all 2000 on A→B→C→D:
  A→B: 2000/100 = 20
  B→C: 0
  C→D: 2000/100 = 20
  Total: 40 min.

  But original path A→B→D: 2000/100 + 50 = 70 min (if everyone uses new route)
  Original path A→C→D: 50 + 2000/100 = 70 min.
  New route A→B→C→D: 20 + 0 + 20 = 40 min.

  All drivers prefer the new route: NE = 2000 on A→B→C→D, cost = 40.
  But wait — original NE was 60 min for each driver.
  After adding the free edge: NE is 40 min — better! (Braess usually shows cost increase)

  The standard Braess has the free edge and the new equilibrium is 80 min.
  The key: in equilibrium, the congestion-sensitive edges get all 2000 drivers,
  and the social optimum (splitting) gives lower cost than the NE (everyone crowds
  onto the "free" path). PoA > 1 due to coordination failure.
```

### Roughgarden-Tardos PoA Bounds

**Selfish routing** in networks: each user routes from source to destination to minimize
their own latency.

```
  NETWORK ROUTING GAME:
  - Directed graph G = (V, E)
  - Latency functions lₑ(x) on each edge (non-decreasing, x = flow)
  - k user classes, each routes flow rₖ from sₖ to tₖ
  - Nash equilibrium = Wardrop equilibrium (no user benefits from rerouting)

  PoA BOUNDS (Roughgarden-Tardos 2002):

  Linear latency functions lₑ(x) = aₑx + bₑ:
    PoA ≤ 4/3  (tight: Braess-like examples achieve 4/3)

  Polynomial latency lₑ(x) = aₑx^d + bₑ:
    PoA ≤ Φ(d)  where Φ(d) → ∞ as d → ∞

  General monotone latency (unbounded):
    PoA can be arbitrarily large (e.g., step functions)

  KEY TECHNIQUE: Bounding method.
    Cost(NE) ≤ α · Cost(OPT) via the "smoothness" framework.
    Show: Σₑ lₑ(fₑ) · fₑ ≤ α · Σₑ lₑ(fₑ*) · fₑ* + C
    Where fₑ = NE flows, fₑ* = optimal flows.
    Directly gives PoA ≤ α.
```

---

## Potential Games and Congestion Games

### Potential Games

**Definition (Monderer-Shapley 1996)**: A game G = (N, {Sᵢ}, {uᵢ}) is an **exact
potential game** if there exists Φ: S → ℝ such that for all i, sᵢ, s'ᵢ, s₋ᵢ:

    uᵢ(s'ᵢ, s₋ᵢ) - uᵢ(sᵢ, s₋ᵢ) = Φ(s'ᵢ, s₋ᵢ) - Φ(sᵢ, s₋ᵢ)

Every individual's unilateral payoff change equals the change in a global potential Φ.

**Key properties**:
- Best-response dynamics (each player repeatedly improves their payoff) converges to NE
- Every local maximum of Φ is a pure NE
- Finite improvement property: no cycles in best-response dynamics
- Pure NE always exists (Φ has a maximum on finite S)

### Congestion Games

**Definition (Rosenthal 1973)**: A finite set of resources R. n players, each choosing
a strategy = subset of resources. Payoff to player i using resources Sᵢ:

    uᵢ(S₁,...,Sₙ) = Σ_{r ∈ Sᵢ} fᵣ(nᵣ)

where nᵣ = |{j : r ∈ Sⱼ}| = number of players using resource r, and fᵣ is a resource-
specific function of congestion.

**Theorem (Rosenthal 1973)**: Every congestion game has the **Rosenthal potential**:

    Φ(S₁,...,Sₙ) = Σ_r Σ_{k=1}^{nᵣ} fᵣ(k)

Rosenthal potential is an exact potential function → every congestion game is a potential
game → pure NE always exists in congestion games.

**Network congestion games** are a special case: resources = edges, strategies = paths.
This is the natural model for selfish routing.

```
  PoA + POTENTIAL GAMES:

  For cost-sharing congestion games (fᵣ(k) = cᵣ/k):
    PoS ≤ H_n = 1 + 1/2 + 1/3 + ... + 1/n   (harmonic number)
    (Anshelevich et al. 2004)

  The potential function argument: the NE that minimizes Φ has
  cost ≤ H_n · OPT. The best NE is a social approximation.
```

---

## Smoothness Framework (Roughgarden 2009)

A game is **(λ, μ)-smooth** if for all strategy profiles s and s*:

    Σᵢ uᵢ(s*ᵢ, s₋ᵢ) ≥ λ · OPT(s*) - μ · Cost(s)

**Theorem**: If a game is (λ, μ)-smooth, then:
- PoA ≤ 1/(λ - μ) for pure NE
- Same bound extends to correlated and coarse correlated equilibria (important for no-regret
  learning convergence)

Smoothness is a property of the game's utility structure that gives PoA bounds that extend
to learning dynamics — not just NE but any "no-regret" outcome.

---

## PPAD-Completeness of Nash

See also 01-NORMAL-FORM.md for the full treatment.

```
  COMPLEXITY LANDSCAPE FOR EQUILIBRIUM COMPUTATION:

  ┌──────────────────────────────────────────────────────────┐
  │  2-player zero-sum: LP-solvable in poly time             │
  │  (minimax = LP primal-dual)                              │
  └──────────────────────────────────────────────────────────┘
                        │
  ┌──────────────────────────────────────────────────────────┐
  │  Potential games: best-response dynamics converges       │
  │  (finite improvement property)                           │
  │  But worst case: exponential number of steps             │
  └──────────────────────────────────────────────────────────┘
                        │
  ┌──────────────────────────────────────────────────────────┐
  │  General 2-player bimatrix: PPAD-complete                │
  │  (Daskalakis/Goldberg/Papadimitriou 2006;                │
  │   Chen/Deng/Teng 2009)                                   │
  └──────────────────────────────────────────────────────────┘
                        │
  ┌──────────────────────────────────────────────────────────┐
  │  Correlated equilibrium: LP-solvable in poly time        │
  │  (linear constraints; exponentially many but             │
  │   can solve via separation oracle / ellipsoid method)    │
  └──────────────────────────────────────────────────────────┘

  PPAD and FP (fixed-point) problems:
  - Brouwer fixed point: PPAD-complete
  - Sperner's lemma on subdivision: PPAD-complete
  - Nash equilibrium: PPAD-complete (via both)
  - Arrow-Debreu market equilibria: PPAD (some complete, some in P)
```

---

## No-Regret Learning and Convergence to Equilibria

### Regret Minimization

In online learning: an agent plays a strategy in each round, observes outcomes, updates.
**External regret**: did I do better if I had played the single best fixed strategy?
**Swap regret**: did I do better if I had swapped strategy i for strategy j in all rounds?

```
  REGRET DEFINITION:

  T rounds, actions aᵢᵗ, loss ℓᵢᵗ(aᵢᵗ).

  External regret of player i:
    Rᵢ = (1/T) Σₜ ℓᵢᵗ(aᵢᵗ) - min_{a} (1/T) Σₜ ℓᵢᵗ(a)

  No-regret algorithm: Rᵢ → 0 as T → ∞.
  EXP3 (exponential weights): Rᵢ = O(√(log m / T)) for m strategies.
  Hedge / multiplicative weights: same rate.
```

### Convergence to Correlated Equilibria

**Theorem (Aumann/Hart, Foster-Vohra 1997)**: If all players use no-regret (swap-regret)
algorithms, the **time-average** of the joint strategy distribution converges to the set
of **correlated equilibria**.

```
  NO-REGRET → CE:

  Each player minimizes swap regret.
  Swap regret → 0 iff time-average play converges to a CE.

  Why: Swap regret of player i being 0 means:
  for all i, j: cannot improve by always swapping strategy i → j
  ↕
  No player benefits from a systematic deviation rule given the
  joint distribution of play
  ↕
  CE conditions

  Note: With only external regret (not swap regret), convergence
  is to coarse correlated equilibria (a weaker concept).
```

**Convergence to Nash**: No-regret dynamics do NOT generally converge to Nash equilibria
in non-zero-sum games. In two-player zero-sum games, they do (fictitious play and EXP3
both converge to minimax NE). In general: CEs, not NEs.

### Fictitious Play

**Fictitious play (Brown 1951)**: Each player plays a best response to the empirical
frequency of opponents' play.

- Converges to NE in 2-player zero-sum (Robinson 1951)
- Converges in 2×2 games (Monderer-Shapley 1996 — all 2×2 are potential-like)
- Does NOT generally converge: Shapley 1964 example (3×3 game with cycling)

---

## Multi-Agent Reinforcement Learning (MARL)

```
  CLASSICAL RL:                    MARL:
  Single agent in environment      Multiple agents, all learning
  State s, action a, reward r      Others are part of the environment
  Markov Decision Process          Markov Game (stochastic game)
  Bellman equations → Q-learning   No fixed Q-function (others learn)

  PROBLEM: Non-stationarity.
  From agent i's perspective, other agents are part of the environment.
  But other agents are learning = environment is non-stationary.
  Standard convergence guarantees (Q-learning, policy gradient) break.

  APPROACHES:
  ┌─────────────────────────────────────────────────────┐
  │ Independent Q-learning: ignore other agents         │
  │ Ignores non-stationarity; works in practice         │
  │                                                     │
  │ Nash Q-learning: compute Nash at each step          │
  │ Tractable only for small state/action spaces        │
  │                                                     │
  │ Mean-field games: N → ∞ agents; each interacts     │
  │ with population mean; reduces to single-agent RL   │
  │                                                     │
  │ No-regret + MARL: use EXP3/Hedge in each round;   │
  │ convergence to CE (not NE) — computationally valid │
  └─────────────────────────────────────────────────────┘
```

### AlphaGo, AlphaStar, Libratus, Pluribus

```
  GAME-THEORETIC AI (modern):

  AlphaGo / AlphaZero (DeepMind 2016-2017):
  - Two-player zero-sum perfect information (Go)
  - Self-play training converges toward Nash equilibrium
  - MCTS with neural value/policy networks
  - Self-play = fictitious play + deep RL
  - Nash equilibrium exists; self-play approximates it

  AlphaStar (DeepMind 2019):
  - StarCraft II — imperfect information, multi-agent
  - League training: population of agents (Nash support)
  - Policy space game solved via Nash equilibrium of meta-game
  - PSRO (Policy Space Response Oracles) algorithm

  Libratus (CMU 2017) / Pluribus (CMU 2019):
  - 2-player heads-up NL Texas Hold'em (Libratus)
  - 6-player NL Texas Hold'em (Pluribus)
  - Counterfactual regret minimization (CFR) — no-regret in game trees
  - Abstracts betting actions and cards; solves abstracted game
  - CFR+ converges to approximate Nash in zero-sum extensive form games
  - Pluribus (6-player): Nash doesn't directly generalize; uses "BluePrint"
    strategy trained by self-play + search at runtime

  CFR ALGORITHM:
  At each information set h, for each action a:
    Counterfactual regret = how much better I'd have done
    always playing a when I reached h?
  Minimize counterfactual regret at each information set.
  Regret matching: σ(a) ∝ max(R(a), 0) [positive regret only]
  Convergence: T_rounds of CFR → ε-Nash with ε = O(1/√T)
```

---

## Decision Cheat Sheet

| Question | Concept | Notes |
|----------|---------|-------|
| Does a population strategy resist invasion? | ESS | Check two conditions; ESS ⊆ Nash |
| What population state is dynamically stable? | Replicator dynamics | ESS ↔ asymp. stable |
| How costly is selfish behavior? | Price of Anarchy | Worst NE / optimal |
| Best achievable by selfishness? | Price of Stability | Best NE / optimal |
| Does best-response dynamics converge? | Potential game? | Finite improvement property |
| Network routing equilibrium | Wardrop / selfish routing | PoA ≤ 4/3 for linear latency |
| Efficient Nash computation? | PPAD-complete in general | LP for zero-sum; heuristics generally |
| Learning without knowing opponents | No-regret algorithms | EXP3, Hedge; converge to CE |
| Multi-agent RL setting | MARL + no-regret | CE convergence; Nash for zero-sum |
| Poker/imperfect info game | CFR variants | Converges to ε-Nash in zero-sum EFG |

---

## Common Confusion Points

**"ESS = Nash"**: Every ESS is a Nash equilibrium; not every Nash is ESS. Strict Nash ⟹
ESS. Non-strict Nash may or may not be ESS (needs stability against second-order selection).
Rock-Paper-Scissors: interior NE exists but is not ESS (population cycles).

**"Replicator dynamics always converges to Nash"**: Fixed points of replicator dynamics
are Nash equilibria; the converse direction. But dynamics may cycle, oscillate, or converge
to a non-NE rest point (corner of simplex). Convergence is only guaranteed for specific
game classes (dominance-solvable, potential games, zero-sum in 2-player case).

**"PoA measures efficiency"**: PoA = worst-case NE / optimum. PoA = 1 means every NE
equals the social optimum. PoA > 1 means there exist inefficient NE. But PoA only gives
an upper bound; in many instances the actual NE may be near-optimal even when PoA is large.

**"No-regret learning converges to Nash"**: Only for two-player zero-sum. In general
multi-player non-zero-sum: no-regret (with swap regret) converges to correlated equilibria.
External regret alone gives coarse correlated equilibria (an even weaker concept).

**"Potential games always have unique NE"**: Potential games always have at least one
pure NE (global maximum of Φ). But they may have many NE (multiple maxima of Φ). Best-
response dynamics converges to some pure NE but not necessarily to the social optimum.

**"Self-play in deep RL converges to Nash"**: Self-play provably converges to Nash in
two-player zero-sum games (via connection to fictitious play / no-regret). For general
n-player non-zero-sum: self-play does not converge to Nash in theory, and may cycle in
practice. AlphaStar's league training addresses this via population-based methods (PSRO).
