# Game Theory — Strategic Interaction

---

## Big Picture

<!-- @editor[diagram/P2]: Diagram lists game components and applications but doesn't show relationships between solution concepts — e.g., how Nash refines to SPE refines to PBE, how normal form maps to extensive form, how Bayesian games generalize complete-info games -->
```
GAME THEORY: mathematical study of strategic interaction among rational agents

A GAME requires:
  Players: who is acting?
  Actions: what can each player do?
  Payoffs: what does each player get for each outcome?
  Information: what does each player know when choosing?

SOLUTION CONCEPTS: predict what rational players will do
  Nash equilibrium: no player wants to unilaterally deviate
  Backward induction: work backwards from end of game tree
  Bayesian Nash: with uncertainty about opponent types
  Subgame perfect: credible threats only

APPLICATIONS IN TECH:
  • Auctions (Google Ads, spectrum)
  • Platform competition (winner-take-all)
  • Security (adversarial settings)
  • Multi-agent RL (Nash as convergence point)
  • P2P protocols (BitTorrent incentive design)
  • Cryptoeconomics (blockchain consensus as game)
```

---

## Normal Form Games

A game specified by:
- N players
- Action sets A₁, ..., Aₙ (each player chooses aᵢ ∈ Aᵢ)
- Payoff functions uᵢ(a₁,...,aₙ): payoff to player i given action profile

### Prisoner's Dilemma

```
              PLAYER 2
              Cooperate  Defect
PLAYER 1  Cooperate  (3, 3)    (0, 4)
          Defect     (4, 0)    (1, 1)

DOMINANT STRATEGY: Defect (D) regardless of what other does
  If P2 cooperates: D gives 4 > 3 (cooperate)
  If P2 defects: D gives 1 > 0 (cooperate)
  → D is strictly dominant for both → unique NE = (D,D)

PARETO INEFFICIENCY: (D,D) payoff = (1,1) < (C,C) payoff = (3,3)
  Individual rationality → collective irrationality
  Captures: arms races, environmental agreements, open-source contribution
```

### Nash Equilibrium

```
DEFINITION: A profile (a₁*,...,aₙ*) is a Nash Equilibrium if:
  For all i, for all aᵢ ∈ Aᵢ:
  uᵢ(aᵢ*, a₋ᵢ*) ≥ uᵢ(aᵢ, a₋ᵢ*)

  No player can profitably deviate given others' strategies.

EXISTENCE (Nash 1950):
  Every finite game has at least one Nash equilibrium (in mixed strategies).
  Proof: fixed-point theorem (Brouwer or Kakutani)
  ← Also a certificate of computational hardness: finding NE is PPAD-complete

MIXED STRATEGY: probability distribution over actions
  σᵢ ∈ Δ(Aᵢ): randomize to keep opponent indifferent
  At mixed NE: each player mixes only over best responses
  → Mixing is rational iff all mixed strategies give equal expected payoff
```

### Battle of the Sexes and Coordination Games

```
              PLAYER 2
              Opera   Football
PLAYER 1  Opera    (2,1)    (0,0)
          Football  (0,0)    (1,2)

PURE NE: (Opera,Opera) and (Football,Football) — coordination required
MIXED NE: P1 plays Opera with prob 2/3; P2 plays Opera with prob 1/3
  (verify: P2 is indifferent when P1 mixes 2/3: 1×2/3 + 0×1/3 = 2/3 = 0×2/3 + 2×1/3)
  Expected payoffs in mixed NE: both get 2/3 (less than either pure NE)

FOCAL POINTS (Schelling): In practice, players coordinate on "salient" NE
  Even without communication, most players choose the same prominent option
  → Game theory + psychology: culture, salience, preplay communication matter
```

### Dominant Strategies

```
STRICTLY DOMINANT: aᵢ is strictly dominant if uᵢ(aᵢ, a₋ᵢ) > uᵢ(a'ᵢ, a₋ᵢ) for all a₋ᵢ, a'ᵢ ≠ aᵢ
WEAKLY DOMINANT: ≥ with at least one strict

ITERATED ELIMINATION OF STRICTLY DOMINATED STRATEGIES (IESDS):
  Remove all strictly dominated strategies, update opponents' beliefs, repeat
  Result: rationalization of strategies for common knowledge of rationality
  If IESDS converges to unique profile → that's the unique NE (e.g., Prisoner's Dilemma)
  Requires: common knowledge of rationality (all rational, all know all rational, ...)

RATIONALIZABLE STRATEGIES:
  Strategies that survive iterated dominance = rationalizable
  NE ⊂ rationalizable strategies (NE is subset of rationalizable)
```

---

## Extensive Form Games (Dynamic Games)

Games with sequential moves represented as a game tree.

### Backward Induction

```
PRINCIPLE: Start from end nodes, work backwards
  At each decision node, player chooses action that maximizes their payoff
  Given optimal future play

EXAMPLE: Centipede Game
  P1 →(Go down: 1,0)  →(Go down: 0,2)  →(Go down: 3,1)  ... (6,5)
  ↓stay              ↓stay              ↓stay
  P1 gets 1          P2 gets 2          P1 gets 3

  Backward induction: P1 takes 3 at last node; P2 anticipates → takes 2 at node before; ...
  → P1 takes 1 at first node! Both get 1 even though cooperation gives 6,5.
  Experimental: people cooperate for many rounds (violates backward induction)
  → Limited rationality, altruism, reputation
```

### Subgame Perfect Equilibrium (SPE)

```
SUBGAME: subtree of game starting at an information set (player knows they're in this subgame)
SUBGAME PERFECT NE: Nash equilibrium in every subgame
  Eliminates incredible threats (Nash NE allows empty threats off the equilibrium path)

ENTRY DETERRENCE GAME:
  Incumbent threatens "Fight" if Entrant enters.
  Nash NE allows (Stay Out, Fight) — Entrant stays out fearing fight.
  BUT: If Entrant enters, Incumbent's payoff: Fight=-1 < Accommodate=1 → Won't fight!
  SPE: (Enter, Accommodate) — Entrant correctly anticipates incumbent won't fight
  → Strategic commitment (investing in capacity) can make threat credible
     (Dixit 1980: commitment changes payoff matrix → threat becomes credible)
```

### Repeated Games

```
SETUP: Same stage game G played for T periods (or infinitely)
  History: all past actions observable (perfect monitoring)
  Strategy: function from history to action

FINITE HORIZON: Backward induction → NE of stage game played each period
  Unique stage game NE (e.g., Prisoner's Dilemma) → iterated → same NE each period

INFINITE HORIZON (Folk Theorem):
  With δ = discount factor (patience):
  Any payoff vector that is feasible AND individually rational (≥ minmax payoffs)
  can be supported as subgame perfect NE for δ sufficiently close to 1.

GRIM TRIGGER STRATEGY:
  "Cooperate until anyone defects; then defect forever"
  Supports cooperation in Prisoner's Dilemma if:
  Gain from defection one period ≤ Cost of punishment (lose cooperation forever)
  δ/(1-δ) × (3-1) ≥ (4-3) → δ ≥ 1/3
  → Sufficiently patient players can cooperate → "shadow of the future"

TIT-FOR-TAT (Axelrod 1984):
  Cooperate on round 1; copy opponent's last action thereafter
  Won repeated prisoner's dilemma tournaments
  Properties: nice (cooperates first), retaliatory, forgiving, clear
```

---

## Games with Incomplete Information

### Bayesian Games

```
TYPE: θᵢ ∈ Θᵢ captures private information of player i
  Distribution: p(θ₁,...,θₙ) = common prior

BAYESIAN NE:
  Each player maximizes EXPECTED utility given their type and beliefs about others:
  σᵢ*(θᵢ) = argmax_{aᵢ} Σ_{θ₋ᵢ} p(θ₋ᵢ|θᵢ) uᵢ(aᵢ, σ₋ᵢ*(θ₋ᵢ), θ)

EXAMPLE: First-price sealed bid auction (see 03-MECHANISM-DESIGN for details)
  Players: bidders with private valuations vᵢ ~ Uniform[0,1]
  Bayesian NE: bid bᵢ(vᵢ) = vᵢ × (N-1)/N  (shade bid below valuation)
```

### Signaling Games

```
SENDER (informed) → sends message m ∈ M → RECEIVER (uninformed) → takes action a ∈ A
Payoffs depend on sender's type θ, message m, and receiver's action

PERFECT BAYESIAN EQUILIBRIUM (PBE):
  Combines: strategies + beliefs (receiver's posterior p(θ|m))
  Beliefs updated by Bayes' rule on equilibrium path

SEPARATING EQUILIBRIUM: Different types send different messages
  → Receiver can infer type perfectly → first-best information

POOLING EQUILIBRIUM: All types send same message
  → Receiver learns nothing → posterior = prior

CHEAP TALK (Crawford-Sobel):
  Sender has no cost for messages → cannot fully separate (only partitional)
  More aligned interests → more information transmitted
  → Basis for AI assistant alignment: AI's incentives must align to give useful advice
```

---

## Evolutionary Game Theory

```
SETUP: Large population, players drawn randomly to play game,
       strategies heritable, payoff = fitness (reproductive success)

EVOLUTIONARY STABLE STRATEGY (ESS):
  Strategy σ* is ESS if for any mutant σ ≠ σ*:
  u(σ*, εσ + (1-ε)σ*) > u(σ, εσ + (1-ε)σ*)  for small ε > 0

  "Invasion proof": a small mutant population cannot grow
  ESS → NE (not vice versa; ESS is refinement)

HAWK-DOVE GAME:
              Dove    Hawk
  Dove:      (3,3)   (1,4)
  Hawk:      (4,1)   (0,0)  (V=4, C=8 → V<C → mixed ESS)

  ESS: mix Hawk with probability p = V/C = 1/2

REPLICATOR DYNAMICS:
  ẋᵢ = xᵢ[fᵢ(x) - f̄(x)]   (fraction of strategy i grows if above-average fitness)
  Fixed points = NE; stable fixed points ≈ ESS
  Connects game theory to evolutionary biology and multi-agent RL (policy gradient dynamics)
```

---

## Decision Cheat Sheet

| Solution concept | When to use | Key property |
|-----------------|-------------|-------------|
| Nash equilibrium | One-shot simultaneous game | No unilateral deviation profitable |
| Iterated dominance | When dominant strategies exist | Fewer assumptions than NE |
| Backward induction | Finite perfect-info sequential game | Credible strategies only |
| Subgame perfect NE | Infinite/extensive form game | Eliminates empty threats |
| Perfect Bayesian NE | Sequential game with private info | Beliefs + Bayes updating |
| Folk theorem | Repeated game | Cooperation possible if δ high enough |
| ESS | Population dynamics | Invasion-resistant strategies |
| Correlated equilibrium | With coordination device | Weakens rationality assumptions; easier to compute |

| Common game | Structure | Key insight |
|-------------|-----------|-------------|
| Prisoner's Dilemma | Both defect (unique NE) | Individual rationality → collective failure |
| Stag Hunt | Two NE (risky, safe) | Coordination; risk vs reward |
| Hawk-Dove | Mixed NE | Conflict costs → mixed population |
| Battle of Sexes | Two pure NE | Multiple equilibria → need focal point |
| Centipede | Backward induction | Rationality → early exit, experiment says cooperate |
| Ultimatum | SPE = reject small but accept any | Experiment: people reject "unfair" offers |

<!-- @editor[structure/P2]: Missing Common Confusion Points section — natural gotchas: Nash equilibrium is not necessarily "optimal" or "fair", mixed strategy equilibrium does not mean players literally randomize, backward induction assumes common knowledge of rationality, dominant strategy vs dominated strategy, SPE vs NE -->
<!-- @editor[content/P2]: Correlated equilibrium appears in Decision Cheat Sheet but has no coverage in the body — either add a section or remove from the table -->
