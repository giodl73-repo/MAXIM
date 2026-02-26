# Game Theory — Strategic Interaction

---

## Big Picture

```
GAME THEORY: mathematical study of strategic interaction among rational agents

REPRESENTATION FORMS AND THEIR RELATIONSHIP:
  Normal form:    players, action sets, payoff functions — simultaneous play
  Extensive form: game tree with information sets — adds timing and information
  Bayesian game:  types θᵢ drawn from prior; payoffs depend on type profile
        │
        │  complete info + simultaneous → Normal form
        │  complete info + sequential   → Extensive form
        │  incomplete info              → Bayesian game (normal or extensive)
        ▼
SOLUTION CONCEPT HIERARCHY (each refines the one above):

  CORRELATED EQUILIBRIUM        ← weakest; allows coordination device
        │  contains all Nash equilibria as special cases
        ▼
  NASH EQUILIBRIUM              ← no unilateral deviation profitable
        │  applied to extensive form:
        ▼
  SUBGAME PERFECT EQUILIBRIUM   ← NE in every subgame; eliminates empty threats
        │  with incomplete information:
        ▼
  PERFECT BAYESIAN EQUILIBRIUM  ← SPE + consistent beliefs via Bayes' rule

  Bayesian NE = NE of the Bayesian game (incomplete info, simultaneous)
  PBE = SPE analog for sequential games with incomplete info

REFINEMENT DIRECTION: more restrictive → fewer equilibria → stronger predictions
  CE ⊇ NE ⊇ SPE ⊇ PBE  (each set ⊆ the one to its left)
  Nash always exists (mixed); SPE always exists in finite games

APPLICATIONS IN TECH:
  • Auctions (Google Ads, spectrum) — Bayesian NE, VCG
  • Platform competition (winner-take-all) — repeated games, folk theorem
  • Security (adversarial settings) — minimax, zero-sum
  • Multi-agent RL (Nash as fixed point of best-response dynamics)
  • P2P protocols (BitTorrent) — incentive design, mechanism design
  • Cryptoeconomics (blockchain consensus) — repeated game with fork threat
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

---

## Correlated Equilibrium

```
DEFINITION (Aumann 1974, 1987):
  A correlation device (mediator) draws a signal profile (s₁,...,sₙ) from
  distribution p over S = S₁×...×Sₙ and privately tells each player i their
  signal sᵢ. Players choose actions based on sᵢ.

  Profile is a correlated equilibrium if no player benefits from deviating
  given their signal:
  For all i, all sᵢ, all alternative action a'ᵢ:
  Σ_{s₋ᵢ} p(s₋ᵢ|sᵢ) u_i(a(sᵢ), a(s₋ᵢ)) ≥ Σ_{s₋ᵢ} p(s₋ᵢ|sᵢ) u_i(a'ᵢ, a(s₋ᵢ))

  (Following the signal is a best response given what following the signal
  reveals about others' signals.)

RELATIONSHIP TO NASH:
  Every Nash equilibrium is a correlated equilibrium (set p = product of
  mixed strategy distributions; signals are independent).
  CE contains NE as a special case.
  CE may achieve higher social welfare than any Nash equilibrium.

EXAMPLE: Battle of the Sexes
  Pure NE: (Opera,Opera) = (2,1) or (Football,Football) = (1,2).
  Mixed NE payoffs: both get 2/3.
  CE: mediator tosses coin → tells P1 "Opera" or "Football," tells P2 same.
  Expected payoffs: (1.5, 1.5) — Pareto-dominates the mixed NE.
  This CE is achieved by both following a public random signal.

WHY CE MATTERS FOR CS/ENGINEERING:
  CE is easier to compute than Nash: CE is a linear program (O(|A|² constraints).
  NE is PPAD-complete.
  In multi-agent RL: no-regret learning algorithms (multiplicative weights,
  online gradient descent) converge to CE in self-play, not Nash.
  → In practice, distributed agents learning independently converge to CE.

  Regret minimization → CE: if all players minimize their own regret
  (achievable by algorithms), the empirical distribution of play
  converges to the set of correlated equilibria.
```

---

## Common Confusion Points

**Nash equilibrium is not optimal or fair**: NE is a stability concept — no player can profitably deviate. It says nothing about welfare (Prisoner's Dilemma NE is Pareto dominated). It says nothing about fairness (a NE can involve zero for one player). It is not necessarily unique. For welfare-improving results, need mechanism design (VCG, matching) or cooperation (repeated game folk theorem).

**Mixed strategy equilibrium does not mean players literally randomize**: The standard interpretation: at a mixed NE, each player randomizes to make *others* indifferent among their mixed strategies. A deeper interpretation (purification theorem, Harsanyi): players have privately known payoff perturbations; the mixed NE is a limit of pure-strategy BNE of nearby games. In practice: mixed NE represents a population distribution of pure strategies, or uncertainty about opponent behavior, not a literal coin flip.

**Backward induction requires common knowledge of rationality (CKR)**: SPE derivation applies backward induction: P2 will choose optimally at their last node, so P1 anticipates that, etc. This requires not just that both players are rational, but that P1 knows P2 is rational, P2 knows P1 knows P2 is rational, and so on infinitely. CKR is a strong assumption; centipede game experiments show it fails in practice.

**Dominant strategy vs dominated strategy**: A *dominant* strategy is best regardless of opponents' play (you want it). A *dominated* strategy is worse than some other strategy regardless of opponents' play (you never want it). IESDS eliminates strictly dominated strategies; this is weaker than assuming dominant strategies exist. Dominant strategy IC in mechanism design means truth-telling is a dominant strategy — the strongest IC notion.

**SPE vs NE**: Every SPE is a NE, not vice versa. NE allows players to make threats that they would never rationally carry out off the equilibrium path. SPE (via backward induction / one-shot deviation principle) requires strategies to be optimal in every subgame, including off-path ones. SPE eliminates "incredible threats" — the key refinement for dynamic games.
