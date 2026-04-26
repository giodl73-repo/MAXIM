# Normal Form Games — Strategy, Dominance, and Nash Equilibrium

## The Big Picture

A normal form game captures simultaneous-move strategic interaction. Every player chooses
a strategy once, without observing others' choices. The payoff to each player depends on
the full joint strategy profile.

```
+------------------------------------------------------------------+
|                  NORMAL FORM GAME STRUCTURE                      |
|                                                                  |
|  PRIMITIVES                  DERIVED OBJECTS                     |
|  ----------                  ---------------                     |
|                                                                  |
|  N = {1,...,n}  players      Δ(Sᵢ) = mixed strategy space      |
|  Sᵢ  finite pure strats      uᵢ: Δ(S₁)×...×Δ(Sₙ) → ℝ          |
|  uᵢ: S₁×...×Sₙ → ℝ payoff   (extended multilinearly)           |
|                                                                  |
|  SOLUTION LADDER (most selective → least)                        |
|  ----------------------------------------                        |
|                                                                  |
|  Dominant Strategy Equilibrium                                   |
|          |  (sᵢ* dominates all others for all opponents)         |
|          v                                                       |
|  IESDS / Rationalizability                                       |
|          |  (iterated elimination of strictly dominated strats)  |
|          v                                                       |
|  Nash Equilibrium (pure)                                         |
|          |  (σᵢ* ∈ BR(σ*₋ᵢ) for all i)                        |
|          v                                                       |
|  Nash Equilibrium (mixed)   <-- always exists (Kakutani)         |
|          |                                                       |
|          v                                                       |
|  Correlated Equilibrium     <-- convex polytope, contains NE     |
|          |                      computable in poly time (LP)     |
|          v                                                       |
|  Rationalizability                                               |
|                                                                  |
+------------------------------------------------------------------+
```

---

## Formal Definitions

### The Game

A finite n-player **normal form game** is a tuple G = (N, {Sᵢ}ᵢ∈N, {uᵢ}ᵢ∈N) where:

- N = {1, 2, ..., n} — finite set of players
- Sᵢ — finite set of **pure strategies** for player i (|Sᵢ| = mᵢ)
- S = S₁ × ... × Sₙ — joint strategy space
- uᵢ: S → ℝ — **payoff function** for player i

Notation: s₋ᵢ = (s₁, ..., sᵢ₋₁, sᵢ₊₁, ..., sₙ) denotes all strategies except i's.

### Mixed Strategies

A **mixed strategy** for player i is σᵢ ∈ Δ(Sᵢ), the probability simplex over Sᵢ:

    Δ(Sᵢ) = { σᵢ : Sᵢ → [0,1]  |  Σₛ σᵢ(s) = 1 }

Geometrically: Δ(Sᵢ) is the (mᵢ - 1)-dimensional simplex. Pure strategies are vertices.

**Expected payoff** under mixed strategies (using independence):

    uᵢ(σ) = Σ_{s ∈ S} [Πⱼ σⱼ(sⱼ)] · uᵢ(s)

This is multilinear in each σⱼ — linear in σᵢ holding others fixed. That linearity is
crucial: it means a player is indifferent over their support in equilibrium.

**Support**: supp(σᵢ) = { sᵢ ∈ Sᵢ  |  σᵢ(sᵢ) > 0 }

### Two-Player Matrix Representation

```
  Two players: Row player (1) chooses rows, Column player (2) chooses columns.
  Entry (i,j): payoff pair (u₁(i,j), u₂(i,j))

  Prisoner's Dilemma:
               C (cooperate)    D (defect)
  C (cooperate)   (3, 3)          (0, 4)
  D (defect)      (4, 0)          (1, 1)

  Row player payoffs form matrix A; column player payoffs form matrix B.
  Zero-sum: B = -A.
```

---

## Dominance

### Strict Dominance

Strategy sᵢ is **strictly dominated** by σᵢ ∈ Δ(Sᵢ) if:

    uᵢ(σᵢ, s₋ᵢ) > uᵢ(sᵢ, s₋ᵢ)  for all  s₋ᵢ ∈ S₋ᵢ

Key: sᵢ may be dominated by a mixed strategy even if no pure strategy dominates it.

```
  Example: Rock-Paper-Scissors — no pure strategy dominates, but in
  the 4x4 game with a "Bomb" strategy (loses to everything), Bomb
  is strictly dominated by any pure strategy.
```

### Weak Dominance

σᵢ **weakly dominates** sᵢ if it does at least as well in all cases and strictly better
in some. Iterated elimination of weakly dominated strategies (IEWDS) is order-dependent
and can eliminate Nash equilibria — use IESDS instead.

### IESDS and Rationalizability

**Iterated Elimination of Strictly Dominated Strategies (IESDS)**:

    R⁰ᵢ = Sᵢ
    Rᵏ⁺¹ᵢ = { sᵢ ∈ Rᵏᵢ | sᵢ is not strictly dominated in (N, {Rᵏⱼ}, {uⱼ}) }
    R∞ᵢ = ∩ₖ Rᵏᵢ

**Properties**:
- **Order-independent**: the set R∞ᵢ does not depend on elimination order
- **Epistemic foundation**: R∞ᵢ = set of strategies consistent with **common knowledge
  of rationality** (each player is rational, knows others are rational, knows others know
  this, ad infinitum)
- If IESDS eliminates all but one profile, that profile is the **unique rationalizable**
  outcome and is the unique NE

**Rationalizable strategies** (Bernheim / Pearce 1984): strategy sᵢ is rationalizable
if it survives IESDS. Equivalently, sᵢ is a best response to some belief over R∞₋ᵢ.

In two-player games: rationalizable = survives IESDS. In n-player (n > 2): rationalizability
is slightly weaker (allows correlated beliefs over opponents). The distinction rarely matters.

---

## Best Response

**Best response correspondence**:

    BRᵢ(σ₋ᵢ) = argmax_{σᵢ ∈ Δ(Sᵢ)} uᵢ(σᵢ, σ₋ᵢ)

Since uᵢ is linear in σᵢ, BRᵢ(σ₋ᵢ) is always a face of the simplex Δ(Sᵢ). In particular,
if there is a unique best pure strategy, BRᵢ(σ₋ᵢ) = that pure strategy (a vertex).

**Key property**: σᵢ ∈ BRᵢ(σ₋ᵢ) iff σᵢ assigns positive probability only to strategies
in:  argmax_{sᵢ} uᵢ(sᵢ, σ₋ᵢ)

This gives the **support characterization of NE**: in any NE σ*, every strategy in
supp(σᵢ*) is a pure best response to σ*₋ᵢ.

```
  COMPUTING BEST RESPONSES IN 2×2 GAMES:

  If column plays (q, 1-q):
    Row's expected payoff from strategy 1: u₁(1,q) = q·a + (1-q)·b
    Row's expected payoff from strategy 2: u₁(2,q) = q·c + (1-q)·d

  Row is indifferent when: q·a + (1-q)·b = q·c + (1-q)·d
                           q(a-b-c+d) = d-b
                           q* = (d-b)/(a-b-c+d)

  Mixed NE: find q* that makes Row indifferent, find p* that makes
  Column indifferent. The opponent's mixing enforces your indifference.
```

---

## Nash Equilibrium

### Definition

A **Nash Equilibrium** is a strategy profile σ* ∈ Δ(S₁) × ... × Δ(Sₙ) such that:

    ∀i ∈ N: σᵢ* ∈ BRᵢ(σ*₋ᵢ)

Equivalently: no player can strictly increase their expected payoff by unilateral deviation.

This is a fixed point of the best response correspondence:
BR: Δ(S) → 2^{Δ(S)}, σ ↦ BR₁(σ₋₁) × ... × BRₙ(σ₋ₙ)

### Nash Existence Theorem

**Theorem (Nash 1950/1951)**: Every finite game has at least one Nash equilibrium
(in mixed strategies).

**Proof sketch via Kakutani**:

```
  Define: Δ(S) = Δ(S₁) × ... × Δ(Sₙ)  (compact, convex subset of ℝᴹ)

  Define: BR: Δ(S) → 2^{Δ(S)}, σ ↦ ×ᵢ BRᵢ(σ₋ᵢ)

  Verify Kakutani conditions:
  1. Δ(S) is compact and convex.          ✓ (product of simplices)
  2. BR(σ) is nonempty for all σ.         ✓ (max of continuous function
                                              on compact set)
  3. BR(σ) is convex for all σ.           ✓ (BR is a face of simplex;
                                              convex combinations of
                                              best responses are BR)
  4. BR has a closed graph.               ✓ (uᵢ continuous, argmax is
                                              upper hemicontinuous)

  Kakutani: ∃ σ* ∈ BR(σ*)  ⟹  Nash equilibrium exists.    □
```

The 1951 proof via Brouwer: define a continuous function f: Δ(S) → Δ(S) that "pushes"
each player toward their best response, then apply Brouwer. Kakutani's version is cleaner
conceptually since BR is naturally set-valued.

**Key nuances**:
- Existence guarantees at least one NE; there may be many
- Generically (for random payoff matrices), NE in the interior of the simplex are isolated
- Odd number theorem (Wilson 1971): generically, finite games have an odd number of NE

---

## Canonical 2×2 Games

### Prisoner's Dilemma

```
               Cooperate (C)    Defect (D)
  Cooperate       (3, 3)          (0, 4)
  Defect          (4, 0)          (1, 1)
```

**Analysis**:
- D strictly dominates C for both players (regardless of opponent's play: 4 > 3, 1 > 0)
- Unique NE: (D, D) with payoff (1, 1)
- Pareto-dominated by (C, C) with payoff (3, 3)
- **Social dilemma**: individual rationality ⟹ collective irrationality
- No escape in one-shot game; repetition and reputation can sustain (C, C)

### Coordination Game and Stag Hunt

```
  Pure coordination:          Stag Hunt:
       A      B                    Stag    Hare
  A  (2,2)  (0,0)           Stag  (4,4)  (0,3)
  B  (0,0)  (1,1)           Hare  (3,0)  (3,3)
```

**Stag Hunt analysis**:
- Two pure NE: (Stag, Stag) and (Hare, Hare)
- (Stag, Stag) is **payoff-dominant** (Pareto-superior)
- (Hare, Hare) is **risk-dominant** (best response under uncertainty; Harsanyi-Selten)
- Mixed NE: Row mixes with p(Stag) = 3/4 to make Column indifferent
- **Equilibrium selection problem**: multiple NE, no dominant strategy
- Risk dominance criterion: NE σ* risk-dominates σ** iff each player prefers σ* when
  opponent randomizes uniformly between the two NE

### Battle of the Sexes

```
           Opera (O)    Football (F)
  Opera     (2, 1)         (0, 0)
  Football  (0, 0)         (1, 2)
```

**Analysis**:
- Two pure NE: (O, O) and (F, F) — coordination with conflicting preferences
- Mixed NE: Column plays O with prob p = 1/3, Row plays O with prob q = 2/3
  - Row indifference condition (Row mixes iff Column's mixing makes Row indifferent):
    Column plays O with prob p: Row payoff from O = 2p, from F = (1-p)
    Equate: 2p = 1-p → p = 1/3
  - Column indifference condition (Column mixes iff Row's mixing makes Column indifferent):
    Row plays O with prob q: Column payoff from O = q, from F = 2(1-q)
    Equate: q = 2(1-q) → q = 2/3
  - Mixed NE payoffs:
    Row:    2 × (1/3) = 2/3
    Column: (2/3) × 1 + (1/3) × 0 = 2/3   [Column gets 1 from O,O and 0 from F,O]
    Both receive 2/3 — strictly worse than either pure NE (which gives 2 to one player, 1 to the other)
- Mixed NE is less efficient than either pure NE — a classic illustration

### Matching Pennies (Zero-Sum)

```
           Heads (H)    Tails (T)
  Heads     (+1, -1)     (-1, +1)
  Tails     (-1, +1)     (+1, -1)
```

**Analysis**:
- Zero-sum: B = -A, so payoffs sum to 0
- No pure NE (each player wants to react to the other)
- Unique NE: both mix (1/2, 1/2) — the minimax solution
- Von Neumann minimax: max_σ₁ min_σ₂ u₁(σ₁, σ₂) = min_σ₂ max_σ₁ u₁(σ₁, σ₂) = 0

---

## Zero-Sum Games and the Minimax Theorem

For two-player zero-sum games (B = -A), NE reduces to the minimax problem.

**von Neumann Minimax Theorem (1928)**:

    max_{x ∈ Δ(m)} min_{y ∈ Δ(n)} xᵀAy = min_{y ∈ Δ(n)} max_{x ∈ Δ(m)} xᵀAy

The value V of the game exists; both players have minimax strategies achieving V.

### LP Duality Connection

```
  Row player's problem:              Column player's problem:
  max V                              min W
  subject to:                        subject to:
    Aᵀx ≥ V · 1   (each col ≥ V)     Ay ≤ W · 1  (each row ≤ W)
    Σxᵢ = 1                           Σyⱼ = 1
    x ≥ 0                             y ≥ 0

  These are LP duals. LP strong duality ⟺ minimax theorem.
  V = W at optimality. Nash 1950 used this; von Neumann 1928 proved it
  via Brouwer before LP duality was formalized.
```

**Connection to Farkas' lemma**: The minimax theorem follows from the fact that two convex
sets (the column player's min-payoff envelope and the row player's max-payoff envelope)
cannot be strictly separated if they overlap at V. Farkas gives the certificate.

---

## Correlated Equilibrium

**Aumann (1974, 1987)**: A **correlated equilibrium** is a joint distribution μ ∈ Δ(S)
such that for each player i, every recommended strategy sᵢ, and every deviation s'ᵢ:

    Σ_{s₋ᵢ} μ(sᵢ, s₋ᵢ) · uᵢ(sᵢ, s₋ᵢ) ≥ Σ_{s₋ᵢ} μ(sᵢ, s₋ᵢ) · uᵢ(s'ᵢ, s₋ᵢ)

Interpretation: a mediator samples a profile s from μ and tells each player i their
recommendation sᵢ (not the others'). Given my recommendation, I don't want to deviate.

```
  NE vs CE:

  Nash Equilibrium:          σᵢ* are independent distributions
                             μ = σ₁* ⊗ σ₂* ⊗ ... ⊗ σₙ*  (product measure)

  Correlated Equilibrium:    μ can be any joint distribution on S
                             (not necessarily a product measure)

  Set containment:
    conv(NE) ⊆ CE     (convex hull of all NE is contained in CE)
    CE ⊇ NE           (every NE is a CE — use independent mixing)

  Battle of the Sexes correlated equilibrium:
  μ(O,O) = 1/2, μ(F,F) = 1/2 achieves expected payoff (3/2, 3/2) for both
  — better than the mixed NE (2/3, 2/3) and fair unlike either pure NE!
  (A "traffic light" correlated device: flip coin, coordinate on the outcome.)
```

**Why CE matters**:
- The set of CE is a **convex polytope** (the constraints are linear in μ) — computable
  in polynomial time via LP
- Nash computation is PPAD-complete; CE computation is in P
- No-regret learning converges to CE (not NE) — practically important
- Cheap talk (pre-game communication without commitment) can implement CE

---

## PPAD-Completeness of Nash

**Theorem (Daskalakis, Goldberg, Papadimitriou 2006; Chen, Deng, Teng 2009)**:
Computing a Nash equilibrium of a two-player game (given as a bimatrix) is PPAD-complete.

**What is PPAD?**

```
  PPAD = Polynomial Parity Argument on Directed graphs

  The foundational PPAD problem (EOPL or END-OF-LINE):
  Given a directed graph where every node has in-degree ≤ 1 and
  out-degree ≤ 1, given a source vertex (in-degree 0, out-degree 1),
  find another source or sink.

  By a parity argument: the number of sources and sinks must have
  the same parity. Given one source, another source or sink MUST exist.
  But finding it may require traversing an exponentially long path.

  PPAD ⊆ TFNP ⊆ FNP

  TFNP = Total Function NP = problems where a solution always exists
         (Nash always exists by Kakutani, so it's in TFNP)

  If PPAD = P, then many cryptographic hardness assumptions fail.
  Widely believed PPAD ≠ P.
```

**Why isn't Nash NP-hard?** NP-hardness is for decision problems where a solution may not
exist. "Does this game have a Nash equilibrium?" is trivially YES (always). You can't
reduce 3-SAT to it because a NO instance of 3-SAT would need a game with no NE — impossible.
PPAD captures a different form of hardness: finding a solution that is guaranteed to exist.

**The reduction**: Nash can be encoded as an END-OF-LINE instance. The path from source
to sink traces the Lemke-Howson algorithm's pivoting steps through a polytope. Each pivot
is locally computable; the path may be exponentially long.

**Implications**:
- No polynomial-time algorithm for Nash is known (or expected)
- Lemke-Howson runs in exponential worst case
- For specific game classes (zero-sum = LP; potential games = simple dynamics), efficient
  algorithms exist
- Practical approach: heuristics, support enumeration for small games, Lemke-Howson for
  moderate sizes

---

## Multiplicity and Equilibrium Selection

Most interesting games have **multiple Nash equilibria**. How to pick one?

```
  EQUILIBRIUM SELECTION CRITERIA:
  ================================

  Payoff dominance (Pareto):
    σ* payoff-dominates σ** if uᵢ(σ*) ≥ uᵢ(σ**) ∀i with strict ≥ for some i
    Intuition: choose the NE everyone prefers.
    Problem: doesn't account for risk.

  Risk dominance (Harsanyi-Selten 1988):
    In 2×2 games: σ* risk-dominates σ** if it is the best response when
    the opponent randomizes uniformly between the two NE.
    Captures "safety" under uncertainty about opponents.

  Trembling-hand perfect (Selten 1975):
    NE σ* is THP if it is a limit of NE of ε-perturbed games
    (all strategies played with ε > 0 probability).
    Eliminates weakly dominated strategies.

  Proper equilibrium (Myerson 1978):
    Refinement of THP where more costly mistakes are made with smaller prob.

  Focal point / Schelling point:
    Salience and pre-game communication; not captured by equilibrium theory.
    "Meet in NYC without coordinating" — Grand Central at noon.
```

---

## Decision Cheat Sheet

| Situation | Tool | Notes |
|-----------|------|-------|
| One strategy beats all regardless of opponents | Dominant strategy equilibrium | Check first — rarest but cleanest |
| Can eliminate some strategies | IESDS | Order-independent for strict dom |
| Need all equilibria of a 2-player game | Support enumeration / Lemke-Howson | Exponential worst case |
| Zero-sum 2-player | LP (minimax) | Polynomial, equivalent to NE |
| Want cheap coordination with mediator | Correlated equilibrium | LP polytope, poly-time |
| Need NE for large game efficiently | Not generally possible (PPAD) | Use approximations or special structure |
| Repeated game, want cooperation | Folk theorem conditions | Check δ ≥ δ* threshold |
| Population dynamics | Replicator dynamics (see 05-EVOLUTIONARY) | ESS ⊆ Nash |

---

## Common Confusion Points

**"Player mixes because they are uncertain"**: No. In a mixed NE, a player mixes because
mixing makes the opponent exactly indifferent between their own strategies. The mixing is
strategic, not epistemic. The player mixing may be completely indifferent between their
support strategies — they have no preference to mix.

**"The mixed NE is unstable / unreasonable"**: Mixed NE are often Pareto-inferior to pure
NE. In Battle of the Sexes, mixed NE gives (2/3, 2/3) vs (2,1) or (1,2) for pure NE. But
the mixed NE is the only NE that doesn't require coordination — it's the "uncoordinated"
outcome.

**"Strict dominance can be by a mixed strategy"**: You may check all pairs of pure
strategies and find none dominates another, yet a mixed strategy strictly dominates a pure
one. Always check mixed dominance in IESDS. Example: in a 3×3 game, mixing (1/2, 1/2)
over strategies 1 and 2 may dominate strategy 3.

**"IESDS can eliminate Nash equilibria"**: IESDS with strict dominance never eliminates
Nash equilibria — every NE survives. IEWDS (weak) can eliminate NE. The distinction is
important for refinement theory.

**"Nash existence requires finite games"**: The theorem as stated requires finitely many
players and finite strategy sets (to get the simplex is compact and convex). Extensions to
infinite strategy sets (e.g., Cournot with continuous quantities) require more work:
upper hemicontinuity, quasi-concavity of payoffs, etc. Existence holds in many but not all
infinite games.

**"Dominant strategy = Nash"**: Every dominant strategy equilibrium is Nash, but most NE
are not dominant strategy equilibria. Dominant strategy is much stronger (best response
for every possible opponent strategy, not just in equilibrium).
