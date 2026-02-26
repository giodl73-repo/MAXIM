# Extensive Form Games — Sequential Play, Credibility, and Incomplete Information

## The Big Picture

Extensive form games capture temporal structure: who moves when, what they know, and
what choices they face. They generalize normal form (which is a special case with one
simultaneous round) to arbitrary sequential interaction.

```
+------------------------------------------------------------------+
|                 EXTENSIVE FORM GAME STRUCTURE                     |
|                                                                  |
|  GAME TREE                    INFORMATION STRUCTURE              |
|  ----------                   ---------------------              |
|  Nodes (histories)            Perfect info: info sets = singletons|
|  Actions (edges)              Imperfect info: non-singleton sets  |
|  Information sets             Incomplete info: private types      |
|  (partition of nodes)         (Harsanyi: convert to imperfect)   |
|  Terminal nodes + payoffs                                        |
|  Player assignment per node                                      |
|                                                                  |
|  SOLUTION CONCEPTS BY SETTING                                    |
|  ----------------------------                                    |
|                                                                  |
|  Perfect info, finite     -->  Backward induction (Zermelo)      |
|                           -->  Subgame perfect equilibrium (SPE)  |
|                                                                  |
|  Imperfect info (general) -->  Subgame perfect equilibrium       |
|                           -->  Perfect Bayesian Equilibrium (PBE) |
|                           -->  Sequential Equilibrium             |
|                                                                  |
|  Incomplete info          -->  Bayesian Nash Equilibrium (BNE)   |
|  (private types)          -->  PBE (with beliefs over types)      |
|                                                                  |
|  Infinitely repeated      -->  Folk Theorem (SPE can sustain      |
|                                any feasible individually          |
|                                rational payoff)                   |
+------------------------------------------------------------------+
```

---

## Formal Definitions

### The Game Tree

An **extensive form game** with perfect recall specifies:

- **Histories** H: set of all possible histories (sequences of actions); ∅ ∈ H (root)
- **Terminal histories** Z ⊆ H: sequences with no continuation
- **Player function** P: H\Z → N ∪ {c} (assigns each non-terminal history to a player
  or to nature c)
- **Actions** A(h) = { a | (h, a) ∈ H }: available actions at history h
- **Information sets** Iᵢ: partition of {h ∈ H | P(h) = i} into information sets
  - h, h' in same info set ⟹ A(h) = A(h') (same actions available — player can't
    distinguish them)
- **Payoff functions** uᵢ: Z → ℝ
- **Probability distribution** for nature's moves at chance nodes

### Strategies

A **strategy** for player i is a function sᵢ: Iᵢ → A mapping each information set to
an action from that set's action space.

**Critical point**: A strategy specifies behavior at every information set, including
those unreached by the strategy itself. This is not redundant — off-path behavior
determines what happens after deviations and thus affects whether threats are credible.

```
  Example: Entry Deterrence

  Entrant moves first: Enter (E) or Stay Out (S)
  Incumbent responds to E: Fight (F) or Accommodate (A)

  Game tree:

                    [Entrant]
                   /         \
                 E             S
                /               \
         [Incumbent]         (-1, 2)   <- Entrant stays out; Inc. monopoly
            /       \
          F           A
         /             \
      (-3,-1)          (1, 1)

  Payoffs: (Entrant, Incumbent)

  Strategies:
  - Entrant: {E, S}
  - Incumbent: {F, A}  (only one info set; reached only if Entrant plays E)

  Nash equilibria:
  - (E, A): payoff (1,1) — Entrant enters, Incumbent accommodates
  - (S, F): payoff (-1, 2) — Entrant stays out, "threatened" by Fight

  (S, F) is NE because if Entrant stays out, Incumbent's F vs A doesn't
  matter — they never reach that node. But F is non-credible: if Entrant
  actually entered, Incumbent prefers A (1 > -1).

  Subgame perfect equilibrium: (E, A) only.
  SPE eliminates (S, F) because Incumbent's subgame (after E) has
  unique NE: A. Plugging in: Entrant prefers E.
```

---

## Backward Induction and Zermelo's Theorem

### Backward Induction Algorithm

For finite perfect information games:

```
  BACKWARD INDUCTION
  ==================

  1. At each terminal node, the payoffs are given.

  2. Work backward from terminal nodes:
     At each penultimate node (whose children are all terminal),
     the player assigns the action yielding their highest payoff.

  3. Replace the subtree with the resulting payoff vector.

  4. Repeat until root is reached.

  Result: a complete strategy profile and associated payoff.
```

### Zermelo's Theorem (1913)

**Theorem**: Every finite, perfect information, two-player zero-sum game has a determined
outcome: one player has a winning strategy, or both have drawing strategies.

**Proof sketch**: By backward induction on tree depth. At leaf nodes, outcome is determined.
At each inner node: if it's player 1's move, player 1 chooses the child with best outcome
(by induction, already determined). If it's player 2's move, player 2 chooses accordingly.
Backward induction terminates at the root with a determined value. □

**Application to chess**: Chess is determined — there exists an optimal strategy for both
players. We don't know what it is (chess game tree has ~10^120 nodes). Zermelo's theorem
is a pure existence result, not an algorithm.

**Generalization**: For non-zero-sum games with multiple players, backward induction
yields a subgame perfect equilibrium (not necessarily unique when there are ties).

---

## Subgame Perfect Equilibrium

### Subgame Definition

A **subgame** of an extensive form game is a subtree that:
1. Begins at a single decision node h
2. Contains all successors of h
3. Contains every information set of every player that intersects the subtree
   (information sets must be entirely within the subgame or entirely outside)

Condition 3 ensures the subgame is a proper game (no information set is "cut").

### SPE Definition

A strategy profile s* is a **subgame perfect equilibrium** iff it induces a Nash
equilibrium in every subgame.

**Selten (1965)**: SPE eliminates Nash equilibria supported by non-credible off-path threats.

```
  Finding SPE:
  1. Identify all proper subgames (start from smallest)
  2. Solve each subgame for NE
  3. Replace each subgame with the NE payoffs
  4. Solve the reduced game
  5. Compose strategies from each subgame NE

  For perfect information games, backward induction directly yields SPE.
```

### The Centipede Game

```
  Two players alternate for T rounds.
  At each node: TAKE terminates the game.
                PASS continues.
  Payoffs grow if play continues; but taking now beats waiting.

  Round:     1        2        3        4      ...    T
  Move:   [P1]     [P2]     [P1]     [P2]          [P1/P2]
           |         |        |        |               |
          Pass     Pass     Pass     Pass           Take
           |         |        |        |               |
  payoffs:          (1,5)   (5,1)   (25,5)...

  Backward induction: at round T, current player takes (strictly better).
  At round T-1, current player anticipates opponent takes at T, so takes now.
  Induction collapses: take at round 1.

  Theoretical prediction: Player 1 takes immediately, payoff ≈ (1, 0).
  Experimental result:    Players cooperate for many rounds, earning much more.

  Implications:
  - SPE/backward induction may not predict actual behavior
  - Finite game unraveling is sensitive to last-period rationality
  - Common knowledge of rationality is strong — even ε-irrationality changes things
  - Behavioral game theory: players may have non-standard utility (altruism, signaling)
```

---

## Repeated Games

### Finitely Repeated Games

**Theorem**: If the stage game has a unique Nash equilibrium, then the unique SPE of the
T-period finitely repeated game is to play that Nash equilibrium in every period.

**Proof**: Backward induction from period T. In period T (last round), the unique NE is
played regardless of history. Given that, period T-1 players cannot use period T play as
a reward/punishment device. Inducting backward to period 1: unique NE in every period. □

**Corollary**: Prisoner's Dilemma finitely repeated — cooperation cannot be sustained.

**Exception**: If the stage game has multiple NE with different payoffs, cooperation can
be sustained in early periods by threatening to play the "bad" NE in later periods
(Benoit-Krishna 1985).

### Infinitely Repeated Games

For stage game G, the **infinitely repeated game** G∞(δ) has:
- Players play G in periods t = 0, 1, 2, ...
- Discount factor δ ∈ (0, 1) — present value of future payoffs
- Period t payoff discounted by δᵗ
- Player i's total payoff: (1-δ) Σ_{t=0}^∞ δᵗ · uᵢ(sᵗ)

**Grim Trigger Strategy** in Prisoner's Dilemma:
```
  Play C in period 0.
  Play C in period t if all prior periods had (C,C).
  Play D forever if any deviation occurred.

  Is (Grim Trigger, Grim Trigger) an SPE?

  Cooperation payoff: (1-δ)·3 + (1-δ)δ·3 + ... = 3

  Defect-now payoff: (1-δ)·4 + (1-δ)δ·1 + (1-δ)δ²·1 + ...
                   = (1-δ)·4 + δ·1
                   = 4 - 3δ

  Cooperation preferred iff:
  3 ≥ 4 - 3δ  ⟺  δ ≥ 1/3

  For δ ≥ 1/3, grim trigger sustains cooperation as SPE.
```

**One-Shot Deviation Principle**: Strategy profile σ is an SPE iff no player can increase
their payoff by deviating in a single period and then following σ thereafter. Reduces
checking infinitely many deviations to one-step checks.

### Folk Theorem (Fudenberg-Maskin 1986)

**Setup**: Let G be a finite stage game. Define:

- **Feasible payoff vectors**: V = convex hull of { u(s) | s ∈ S }
- **Minimax value** for player i: vᵢ = min_{σ₋ᵢ} max_{σᵢ} uᵢ(σᵢ, σ₋ᵢ)
  (what others can hold player i down to)
- **Individually rational (IR) payoffs**: V* = { v ∈ V | vᵢ > vᵢ for all i }

**Theorem (Folk Theorem)**: For any v ∈ V* (feasible and strictly individually rational),
there exists δ̄ < 1 such that for all δ ≥ δ̄, there is an SPE of G∞(δ) with expected
payoff vector v.

```
  FOLK THEOREM PICTURE (Prisoner's Dilemma):

  Payoff to Player 2
  4 |         *
    |       / |
  3 | *---*   |
    | |   |   |
  1 | *   |   |
    |     |   |
    +-----+---+---> Payoff to Player 1
    1     3   4

  * = pure strategy payoffs
  Shaded region above minimax values (1,1): all these payoffs
  achievable as SPE for sufficiently patient players.
  Minimax value = (1,1) = the NE payoff in the stage game.
```

**Caveats**:
- "Sufficiently patient" (δ → 1) may require very high δ
- Multiple equilibria — Folk theorem is an existence result, not a selection result
- Requires players to observe past play (perfect monitoring version)
- With imperfect monitoring: weaker Folk theorems hold under conditions

---

## Incomplete Information: Harsanyi Types

### The Setup

**Incomplete information**: players have **private types** θᵢ ∈ Θᵢ drawn from a joint
distribution F ∈ Δ(Θ₁ × ... × Θₙ). A player's type encodes their private information
(valuation in an auction, cost in a negotiation, etc.).

**Harsanyi's insight (1967)**: Incomplete information can be converted to imperfect
information by introducing a prior type draw by nature at the start of the game.

```
  INCOMPLETE INFO → IMPERFECT INFO CONVERSION

  Before:
    Player 1 knows their cost c₁ ∈ {low, high}
    Player 2 doesn't know c₁

  Harsanyi:
    Nature draws (c₁, c₂) ~ F at start of game (before player moves)
    Player i observes cᵢ but not c₋ᵢ
    Now: both players have private info, game is imperfect information

  Common prior assumption: both players know F (the joint distribution).
  This is the standard modeling assumption.
  Its relaxation leads to "non-common priors" models (much harder).
```

### Bayesian Nash Equilibrium

A **strategy** in a Bayesian game for player i is σᵢ: Θᵢ → Δ(Sᵢ) (maps types to
mixed strategies over actions).

A **Bayesian Nash Equilibrium** is σ* such that for each player i and type θᵢ:

    σᵢ*(θᵢ) ∈ argmax_{σᵢ} E_{θ₋ᵢ|θᵢ}[ uᵢ(σᵢ, σ*₋ᵢ(θ₋ᵢ), θᵢ, θ₋ᵢ) ]

Each type of each player plays a best response given beliefs about others' types and
strategies.

```
  Example: First-Price Auction (2 bidders, values uniform on [0,1])

  Each bidder i has private valuation vᵢ ~ U[0,1], independent.
  Strategy: bᵢ(vᵢ) = ? (bid as function of value)

  BNE: bᵢ(vᵢ) = vᵢ/2  (bid half your value)

  Derivation: Assume opponent bids b₋ᵢ(v) = αv for some α.
  Bidder i wins iff bᵢ > αv₋ᵢ, i.e., v₋ᵢ < bᵢ/α, probability bᵢ/α.
  Expected payoff: (vᵢ - bᵢ) · (bᵢ/α)
  FOC in bᵢ: -bᵢ/α + (vᵢ - bᵢ)/α = 0 → bᵢ = vᵢ/2.
  So α = 1/2. Symmetric BNE: both bid half their value.
```

---

## Signaling Games

### Structure

A **signaling game** has:
- **Sender** (player 1) with private type θ ∈ Θ, drawn from prior μ₀
- **Sender** chooses message m ∈ M
- **Receiver** (player 2) observes m (not θ), chooses action a ∈ A
- Payoffs: u₁(θ, m, a) and u₂(θ, m, a)

```
  SIGNALING GAME TREE

  Nature
  /       \
 θ₁        θ₂    (with probs μ₀(θ₁), μ₀(θ₂))
 |          |
 Sender     Sender    <- Sender knows type
  |  \       |  \
 m₁  m₂    m₁  m₂   <- Sender chooses message

  [R observing m₁]        [R observing m₂]
  Receiver doesn't know which type sent m₁
  Information set: {(θ₁, m₁), (θ₂, m₁)} after observing m₁

  Receiver
  a₁  a₂            <- Receiver responds to observed message
```

### Equilibrium Types

**Separating equilibrium**: different types send different messages. Receiver can perfectly
infer sender's type from the message. Reveals all information.

**Pooling equilibrium**: all types send the same message. Receiver learns nothing from
the message. Beliefs at message = prior μ₀.

**Semi-separating (partial pooling)**: some types separate, some pool.

### Perfect Bayesian Equilibrium (PBE)

A **Perfect Bayesian Equilibrium** requires:
1. Each player's strategy is sequentially rational given beliefs (Bayesian Nash condition)
2. Beliefs are updated by Bayes' rule wherever possible (on-path information sets)
3. Beliefs at off-path information sets can be arbitrary (but must be specified)

**Why beliefs matter**: Off-path information sets are never reached in equilibrium, but
they determine whether deviations are profitable. Different belief specifications can
support different equilibria.

---

## Beer-Quiche Game (Cho-Kreps 1987)

### Setup

```
  Types: Weak (W) — prefers Quiche for breakfast
         Strong (S) — prefers Beer for breakfast

  Nature: Prob(Weak) = 0.1, Prob(Strong) = 0.9

  After breakfast, a Bully decides whether to Duel or Not.
  Bully prefers dueling Weak, avoids dueling Strong.
  Players prefer not dueling.

  Payoffs (simplified):
  - Weak + Beer: (-1 from disliked breakfast, -2 if Duel) vs (0 if No Duel)
  - Weak + Quiche: (0 from preferred breakfast, -2 if Duel) vs (1 if No Duel)
  - Strong + Beer: (1, -2 if Duel) vs (2 if No Duel)
  - Strong + Quiche: (-1, -2 if Duel) vs (0 if No Duel)

  Bully: gets +1 from Dueling Weak, -1 from Dueling Strong.
  Bully duels iff Prob(Weak | message) > 0.5.
```

### The Paradox

**Pooling on Beer** (both types drink Beer):
- Bully sees Beer: posterior = prior = 0.1 weak → Bully doesn't duel
- No type wants to deviate to Quiche (Quiche signals weakness, triggers duel)
- This is a PBE with off-path belief: "Quiche drinker is probably Weak"

**Pooling on Quiche** (both types eat Quiche):
- Bully sees Quiche: posterior = 0.1 weak → Bully doesn't duel
- Off-path belief after seeing Beer: "Beer drinker is Weak" (supports not deviating)
- This is also a PBE!

Both pooling equilibria are valid PBE. But intuitively, Strong type has no reason to
send the off-equilibrium message (Beer/Quiche) — the out-of-equilibrium deviator must
be Weak. This informal reasoning suggests the "Beer-pool" equilibrium is more robust.

### Intuitive Criterion (Cho-Kreps D1 Refinement)

A message m is **equilibrium dominated** for type θ if, for every action a the receiver
might play, type θ prefers the equilibrium payoff to the best possible deviation payoff
at m. If message m is not equilibrium-dominated for type θ₁ but is for type θ₂, then
the belief after m should assign probability 1 to θ₁.

The **Intuitive Criterion** eliminates pooling-on-Quiche: Beer is equilibrium-dominated
for Weak type (Strong can always benefit from Beer regardless of Bully's response) but
not for Strong type. So after seeing Beer, belief = Prob(Strong) = 1 → Bully doesn't
duel → Strong deviates to Beer → pooling on Quiche fails.

Surviving equilibrium: pooling on Beer (or separating: Strong drinks Beer, Weak eats Quiche).

---

## Spence Job Market Signaling (1973)

**Setup**:
- Workers have ability θ ∈ {low (L), high (H)}
- Workers choose education level e ∈ [0, ∞) at cost c(e, θ) — single-crossing condition:
  ∂²c/∂e∂θ < 0 (education is cheaper for high-ability workers)
- Firms observe e (not θ), compete for workers, pay wage w(e) = expected ability given e

**Key insight**: Education need not have any direct productivity value. It serves as a
**costly signal** because the single-crossing property makes it too costly for low types
to mimic high types.

```
  SIGNALING EQUILIBRIUM (separating):

  High type chooses e* such that:
    Low type prefers w(0) to w(e*) - c(e*, L)
    High type prefers w(e*) to w(0) - c(e*, H)  [prefers to signal]

  Single-crossing ensures a range of e* exists:
    e* ∈ [ c_L^{-1}(w_H - w_L),  c_H^{-1}(w_H - w_L) ]

  Any e* in this range supports a separating equilibrium.
  Multiple equilibria → refinements (Riley 1979, least-cost separation).

  Result: High-ability workers educate even though education adds nothing
  productive. Education is pure signaling. Pareto-inferior to first-best
  (no private info) but stable given private information.
```

**Spence Nobel 2001** (with Akerlof for adverse selection, Stiglitz for screening).

---

## Decision Cheat Sheet

| Setting | Solution Concept | Key Tool |
|---------|-----------------|----------|
| Finite perfect info game | Backward induction / SPE | Work leaves → root |
| Non-credible threats present | SPE (eliminates them) | Subgame decomposition |
| Simultaneous within sequential | SPE + mixed NE in subgames | Check each subgame |
| Incomplete info, static | Bayesian NE | Type-contingent strategies |
| Incomplete info, dynamic | Perfect Bayesian Equilibrium | Bayesian updating on path |
| Signaling: which equilibria? | PBE + refinements | Intuitive Criterion (D1) |
| Sustaining cooperation long-run | Folk theorem | Check δ ≥ δ*(payoffs) |
| Finitely repeated, unique stage NE | SPE = repeat stage NE | No scope for cooperation |
| Observable deviations | Grim trigger / TfT in G∞(δ) | One-shot deviation principle |

---

## CS and Systems Bridges

| Extensive form concept | Formal / systems analogue |
|---|---|
| Game tree (extensive form) | Computation tree — nodes are computation states, branches are transitions; backward induction is exactly the tree-recursion pattern (base case at leaves, combine upward) |
| Information set | Indistinguishable states in partial-information search (POMDP belief states, imperfect-information game trees in alpha-beta pruning) |
| Subgame | Well-defined recursive subproblem — SPE is optimal substructure (Bellman) applied to strategic games |
| Backward induction / SPE | Dynamic programming: solve leaves first, propagate values up; non-credible threats are sub-optimal sub-solutions that disappear under DP |
| Bayesian updating on path | Bayes' theorem applied at each information set — identical to exact inference in a directed graphical model along an observed path |
| Grim trigger strategy | State machine with two states (cooperate / punish) and a one-way transition; the "no recovery" property is a design choice enforcing Nash credibility |
| Folk theorem δ ≥ δ* | Discount factor threshold is a capacity-planning condition: sustained cooperation requires the future to be heavy enough to outweigh one-shot defection gain |
| Sequential rationality (PBE) | Eliminates strategies with "dead code" — beliefs about unreached information sets must be consistent and on-path strategies must be best responses given those beliefs; analogous to liveness + safety invariants in concurrent systems |

## Common Confusion Points

**"A strategy is a plan"**: A strategy in an extensive form game is a complete contingency
plan — it specifies what to do at every information set, even those never reached. A "plan
of action" (only specifying what to do on the equilibrium path) is not a strategy. Off-path
specifications matter for determining whether the strategy profile is an NE or SPE.

**"SPE eliminates all bad NE"**: SPE eliminates Nash equilibria supported by non-credible
threats. But it can still have multiple equilibria (especially in imperfect information
games). SPE is a refinement, not a selection criterion. For further selection: Cho-Kreps,
Sequential Equilibrium, proper equilibrium.

**"Folk theorem says anything is possible"**: Folk theorem says any individually rational
feasible payoff is achievable as SPE for patient players. "Individually rational" means
each player gets at least their minimax value. Not literally anything.

**"Backward induction works for imperfect information games"**: Backward induction requires
singleton information sets to be well-defined (otherwise "going backward" is ambiguous —
what does the player know at this node?). For imperfect information games, use SPE
(backward induction on subgames) or PBE.

**"PBE requires on-path consistency"**: PBE only constrains beliefs to be Bayes-consistent
on the equilibrium path. Off-path beliefs are free. This creates many equilibria. Sequential
equilibrium adds consistency: off-path beliefs must be limits of Bayes-consistent beliefs
under small perturbations. Technically stronger; often same set of equilibria in practice.

**"Common prior assumption"**: Harsanyi's type-space formalization requires a common prior
— both players know the joint distribution F over types. If players have different priors
about opponents' types, the analysis changes fundamentally (Aumann/Brandenburger). The
common prior is a modeling convenience, not always descriptively accurate.
