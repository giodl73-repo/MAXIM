# Game Theory — The Mathematics of Strategic Interaction

## The Big Picture

Game theory is the mathematical study of decision-making when outcomes depend on the choices of multiple agents. It sits at the intersection of mathematics, economics, computer science, and biology.

```
+------------------------------------------------------------------+
|                    GAME THEORY LANDSCAPE                          |
|                                                                  |
|  BY FORM              BY INFORMATION       BY COOPERATION        |
|  --------             ----------------     ---------------       |
|                                                                  |
|  NORMAL FORM          COMPLETE INFO        NON-COOPERATIVE       |
|  Simultaneous move    All payoffs known    Players act           |
|  Strategy spaces      to all players       independently         |
|  Nash equilibrium                          Nash / SPE / BNE      |
|                                                                  |
|  EXTENSIVE FORM       INCOMPLETE INFO      COOPERATIVE           |
|  Sequential move      Private types        Binding agreements    |
|  Game trees           (Harsanyi types)     Core, Shapley value   |
|  Backward induction   Bayesian NE                                |
|                                                                  |
|  COOPERATIVE FORM     PERFECT INFO         EVOLUTIONARY          |
|  Coalition functions  See all past moves   Selection dynamics    |
|  Core, nucleolus      (chess, go)          ESS, replicator eq.   |
|  Shapley value        IMPERFECT INFO                             |
|                       Non-singleton        ALGORITHMIC           |
|                       info sets            PPAD, PoA, PoS        |
|                       (poker)                                    |
|                                                                  |
|  + MECHANISM DESIGN: design the game to achieve desired outcomes |
+------------------------------------------------------------------+
```

**The central question**: What happens when rational (or evolving) agents interact
strategically? Can we predict outcomes? Can we design systems where self-interest
aligns with social optimality?

---

## Historical Timeline

```
1713  Waldegrave — mixed strategy solution to card game (precursor, not published)

1913  Zermelo — every finite perfect-information game has a determined outcome
      (chess: White wins, Black wins, or draw with perfect play)
      First rigorous theorem in game theory.

1921  Borel — formalizes mixed strategies; conjectures minimax theorem

1928  von Neumann — MINIMAX THEOREM (the founding result)
      max_x min_y x^T A y = min_y max_x x^T A y
      Every finite two-person zero-sum game has a saddle point in mixed strategies.
      Original proof via Brouwer fixed point theorem.

1944  von Neumann + Morgenstern — "Theory of Games and Economic Behavior"
      - VNM expected utility theory (axiomatizes rational preferences under risk)
      - Two-person zero-sum theory fully formalized
      - Cooperative game theory introduced (characteristic function)
      Arguably the most influential economics book of the 20th century.

1950  Nash — Nash equilibrium concept (23-page PhD thesis, age 22)
      Generalizes minimax to n-player non-zero-sum games.
      Existence proved via Kakutani fixed point theorem.

1951  Nash — existence proof via Brouwer (cleaner); mixed strategy version confirmed

1953  Shapley — Shapley value for cooperative games (unique fair allocation)
             — Stochastic games (Markov decision processes with multiple agents)
      2012 Nobel (with Roth) for matching theory

1957  Luce + Raiffa — "Games and Decisions" (definitive textbook)

1965  Selten — Subgame Perfect Equilibrium (SPE)
      Eliminates non-credible threats via backward induction refinement.
      1994 Nobel (with Nash, Harsanyi)

1967  Harsanyi — Bayesian games and type spaces
      Reduces incomplete information to imperfect information.
      Bayesian Nash Equilibrium (BNE) formalized.
      1994 Nobel (with Nash, Selten)

1973  Maynard Smith + Price — Evolutionary Stable Strategy (ESS)
      Game theory for populations; no rationality assumption needed.

1974  Aumann — Correlated Equilibrium
      Generalizes Nash; mediator sends correlated recommendations.
      Larger set than Nash; achievable by cheap talk.
      2005 Nobel (with Schelling)

1982  Rubinstein — alternating offers bargaining with discounting
      Non-cooperative foundation for Nash bargaining solution.

1982  Fudenberg + Maskin — Folk Theorem (rigorous statement)
      Infinitely repeated games sustain cooperation under patience.

1983  Kreps + Wilson — Sequential Equilibrium
      Refinement of PBE with consistent belief systems at limits.

1985  Cho + Kreps — Intuitive Criterion for signaling game refinements

1991  Monderer + Shapley (published 1996) — Potential games
      Congestion games are potential games; pure NE always exists.

2001  Spence Nobel — Job market signaling (with Akerlof, Stiglitz)

2005  Aumann Nobel — Correlated equilibrium, common knowledge

2006  Daskalakis, Goldberg, Papadimitriou — Nash computation is PPAD-complete
      (confirmed for 2-player by Chen/Deng/Teng 2009)

2007  Myerson, Maskin, Hurwicz Nobel — Mechanism design

2012  Roth + Shapley Nobel — Matching theory and market design

2020  Milgrom + Wilson Nobel — Auction theory, FCC spectrum auctions
```

---

## Three Major Forms — Structural Comparison

```
+--------------------+--------------------+--------------------+
|   NORMAL FORM      |  EXTENSIVE FORM    | COOPERATIVE FORM   |
+--------------------+--------------------+--------------------+
| Simultaneous moves | Sequential moves   | Binding agreements |
|                    | (or simultaneous   | allowed            |
|                    |  with info sets)   |                    |
+--------------------+--------------------+--------------------+
| Represented by:    | Represented by:    | Represented by:    |
| Payoff matrix /    | Game tree:         | Characteristic     |
| payoff functions   | nodes, actions,    | function:          |
| uᵢ: S₁×...×Sₙ→ℝ  | info sets,         | v: 2^N → ℝ        |
|                    | terminal payoffs   |                    |
+--------------------+--------------------+--------------------+
| Solution concepts: | Solution concepts: | Solution concepts: |
| Nash equilibrium   | Backward induction | Core               |
| Dominant strategy  | Subgame perfect NE | Shapley value      |
| Correlated eq.     | Perfect Bayesian   | Nucleolus          |
| IESDS/Rationaliz.  | Sequential eq.     | Nash bargaining    |
+--------------------+--------------------+--------------------+
| Key games:         | Key games:         | Key applications:  |
| Prisoner's Dilemma | Chess, go (perfect)| Cost allocation    |
| Battle of Sexes    | Poker (imperfect)  | Voting power       |
| Stag Hunt          | Entry deterrence   | Coalition formation|
| Matching Pennies   | Signaling games    | Profit sharing     |
| Cournot oligopoly  | Centipede game     | Airport games      |
+--------------------+--------------------+--------------------+
```

---

## Key Distinctions Table

| Dimension | Category A | Category B | Key Implication |
|-----------|-----------|-----------|-----------------|
| **Payoff structure** | Zero-sum: Σuᵢ = 0 | Non-zero-sum | Zero-sum: minimax = Nash; LP solvable |
| **Information (ex ante)** | Complete: all payoffs known | Incomplete: private types θᵢ | Incomplete → Harsanyi type spaces, BNE |
| **Information (moves)** | Perfect: all moves observed | Imperfect: non-singleton info sets | Imperfect → mixed strategies often needed |
| **Timing** | Simultaneous | Sequential | Sequential → extensive form, SPE |
| **Agreements** | Non-cooperative | Cooperative | Cooperative → core, Shapley value |
| **Horizon** | Finite | Infinite/repeated | Infinite → Folk theorem, cooperation |
| **Agents** | Rational | Evolutionary | Evolutionary → ESS, replicator dynamics |

---

## Core Solution Concepts — Containment Hierarchy

```
  SOLUTION CONCEPT LANDSCAPE (non-cooperative)
  =============================================

  Most permissive                              Most restrictive
  <---------------------------------------------------------->

  Rationalizability                                    Dominant
  (survives IESDS)                                     Strategy
       |                                               Equilibrium
       v                                                    ^
  Correlated                                               |
  Equilibrium (CE)   <--  CE ⊇ Nash (NE)                 |
       |                  NE ⊆ CE                         |
       v                                                   |
  Nash Equilibrium ----> NE ⊆ CE                          |
       |                                                   |
       +----------> Subgame Perfect (SPE) ⊆ NE            |
       |            [refinement: credible]                 |
       +----------> Perfect Bayesian (PBE) ⊆ NE           |
       |            [refinement: beliefs]                  |
       +----------> Sequential Equilibrium ⊆ PBE          |
                    [refinement: consistent beliefs]       |
                                                           |
  ESS (Evolutionary Stable Strategy):                      |
       ESS ⊆ NE (every ESS is Nash, not vice versa)       |
```

**Cooperative vs non-cooperative**: Core and Shapley value are cooperative concepts —
they presuppose binding agreements and are not refinements of Nash.

---

## The MIT Math/TCS Connections

Game theory was built on machinery you know from MIT. Here are the key bridges:

```
+------------------------------+------------------------------------+
|  MIT MATH/TCS CONCEPT        |  WHERE IT APPEARS IN GAME THEORY  |
+------------------------------+------------------------------------+
| Brouwer Fixed Point Theorem  | Nash 1951 existence proof          |
| f: D^n → D^n continuous      | BR: Δ(S) → Δ(S) has fixed point   |
| has a fixed point            | where Δ(S) = probability simplex   |
+------------------------------+------------------------------------+
| Kakutani Fixed Point Theorem | Nash 1950 existence proof          |
| Set-valued generalization    | BR correspondence: Δ(S) → 2^Δ(S)  |
| of Brouwer (upper hemi-      | is upper hemicontinuous with       |
| continuous, convex values)   | nonempty convex values             |
+------------------------------+------------------------------------+
| Linear Programming + Duality | Zero-sum minimax = primal-dual LP  |
| Primal: max cᵀx, Ax ≤ b     | Correlated equilibrium: LP polytope|
| Dual: min bᵀy, Aᵀy ≥ c     | Core non-emptiness: LP duality     |
|                              | (Bondareva-Shapley theorem)        |
+------------------------------+------------------------------------+
| Probability Simplex Δ(S)     | Mixed strategy spaces              |
| Prob distributions over      | Nash: fixed point on Δ(S₁)×...×Δ(Sₙ)|
| finite sets                  | Support of NE = indifference sets  |
+------------------------------+------------------------------------+
| PPAD Complexity Class        | Nash computation hardness (2006-09)|
| Polynomial Parity Arg on     | Not NP-hard (solution always exists)|
| Directed graphs; PPAD ⊆      | PPAD-complete = hard in a          |
| TFNP ⊆ FNP                  | different sense than NP            |
+------------------------------+------------------------------------+
| Arrow's Impossibility        | Gibbard-Satterthwaite theorem:     |
| (no fair voting rule over    | any deterministic dominant-strategy|
| ≥3 alternatives)             | IC mechanism is dictatorial        |
+------------------------------+------------------------------------+
| Graph theory / Trees         | Extensive form game trees          |
| Rooted directed trees        | Information sets = node partitions |
| with labeled edges           | SPE via leaf-to-root induction     |
+------------------------------+------------------------------------+
| Bipartite matching           | Gale-Shapley stable matching       |
| Hall's theorem               | Stability = no blocking pairs      |
| Augmenting paths             | Deferred acceptance = max matching |
+------------------------------+------------------------------------+
| Online learning / Regret     | No-regret dynamics → CE            |
| EXP3, Hedge algorithms       | Time-average of no-regret play     |
| Adversarial bandits          | converges to correlated equilibria |
+------------------------------+------------------------------------+
| Farkas' lemma                | Minimax theorem: separating        |
| (alternatives theorem)       | hyperplane between convex sets     |
+------------------------------+------------------------------------+
```

---

## Applications by Domain

```
+-------------------------------+--------------------------------+
|  ECONOMICS & MARKETS          |  COMPUTER SCIENCE              |
|  ---------------------        |  ---------------               |
|  Industrial organization      |  Algorithmic mechanism design  |
|  (Cournot/Bertrand oligopoly) |  Internet routing (PoA, PoS)   |
|  Auction design (FCC, ads,    |  PPAD-completeness of Nash     |
|   ad markets, procurement)    |  Multi-agent RL / AI planning  |
|  Contract theory / insurance  |  Cryptographic protocol design |
|  Trade negotiations           |  Network formation games       |
|                               |  Distributed systems incentives|
+-------------------------------+--------------------------------+
|  POLITICAL SCIENCE            |  BIOLOGY                       |
|  -----------------            |  -------                       |
|  Voting power indices         |  Evolutionary stable strategies|
|  Arms races (MAD deterrence)  |  Kin selection (Hamilton's rb>c|
|  Legislative bargaining       |  Signaling (honest vs cheap)   |
|  International negotiations   |  Animal conflict (Hawk-Dove)   |
|  Constitutional design        |  Cooperation (reciprocal alt.) |
+-------------------------------+--------------------------------+
|  SOCIAL/MARKET DESIGN         |  ENGINEERING                   |
|  -----------------            |  -----------                   |
|  NRMP residency matching      |  Network congestion control    |
|  School choice mechanisms     |  P2P systems incentive design  |
|  Kidney exchange (Roth)       |  Cloud resource allocation     |
|  Platform economics (2-sided) |  Spectrum allocation design    |
|  Social norms (Folk theorem)  |  Load balancing (PoA bounds)   |
+-------------------------------+--------------------------------+
```

---

## Guide Map for This Series

```
  game-theory/
  |
  +-- 00-OVERVIEW.md          (this file)
  |   Full landscape, history, distinctions, MIT bridges
  |
  +-- 01-NORMAL-FORM.md
  |   Formal definition G=(N,{Sᵢ},{uᵢ}), mixed strategies (Δ(Sᵢ)),
  |   dominance/IESDS, Nash existence (Kakutani), PPAD-completeness,
  |   canonical games (PD, BoS, Stag Hunt, Matching Pennies),
  |   zero-sum/minimax/LP duality, correlated equilibrium
  |
  +-- 02-EXTENSIVE-FORM.md
  |   Game trees, backward induction, Zermelo's theorem, SPE,
  |   Centipede paradox, repeated games, Folk theorem,
  |   incomplete info (Harsanyi types), signaling, Beer-Quiche,
  |   PBE, Cho-Kreps Intuitive Criterion, job market signaling
  |
  +-- 03-MECHANISM-DESIGN.md
  |   "Inverse game theory": design rules, revelation principle,
  |   IC/IR constraints, Gibbard-Satterthwaite, Groves/VCG,
  |   Vickrey second-price, revenue equivalence theorem,
  |   Myerson optimal auction, combinatorial auctions,
  |   Gale-Shapley matching, NRMP, school choice
  |
  +-- 04-COOPERATIVE.md
  |   Characteristic function, superadditivity, convexity,
  |   core (LP duality / Bondareva-Shapley), Shapley value
  |   (axioms + formula), nucleolus (sequence of LPs),
  |   Nash bargaining (axioms + product), Rubinstein alternating
  |   offers (SPE → unique solution)
  |
  +-- 05-EVOLUTIONARY.md
      ESS conditions, replicator dynamics, Hawk-Dove, kin selection,
      Price of Anarchy (Braess paradox, routing bounds),
      potential games, PPAD-completeness, no-regret learning,
      MARL, AlphaGo/Pluribus as game-theoretic agents
```

---

## Decision Cheat Sheet

| Question | Where to Look |
|----------|--------------|
| Predict behavior in simultaneous game | 01-NORMAL-FORM — Nash equilibrium |
| Does a Nash equilibrium always exist? | 01-NORMAL-FORM — Kakutani fixed point |
| How hard to compute Nash? | 01-NORMAL-FORM — PPAD section |
| Analyze sequential / dynamic games | 02-EXTENSIVE-FORM — SPE |
| Eliminate non-credible threats | 02-EXTENSIVE-FORM — backward induction |
| Handle private information / types | 02-EXTENSIVE-FORM — Harsanyi/BNE |
| Signaling: what equilibria arise? | 02-EXTENSIVE-FORM — PBE, Beer-Quiche |
| Design an auction or market | 03-MECHANISM-DESIGN — VCG, Myerson |
| Make agents reveal private info | 03-MECHANISM-DESIGN — Revelation principle |
| Which auction maximizes revenue? | 03-MECHANISM-DESIGN — Myerson optimal |
| Match students to schools fairly | 03-MECHANISM-DESIGN — Gale-Shapley |
| Fairly share coalition gains/costs | 04-COOPERATIVE — Shapley value |
| Is this allocation coalition-stable? | 04-COOPERATIVE — Core |
| Model bargaining with outside options | 04-COOPERATIVE — Nash/Rubinstein |
| Quantify cost of selfish routing | 05-EVOLUTIONARY — Price of Anarchy |
| Model strategy evolution in population | 05-EVOLUTIONARY — ESS, replicator dynamics |
| Design incentives for distributed system | 03-MECHANISM-DESIGN + 05-EVOLUTIONARY |

---

## Common Confusion Points

**Nash equilibrium vs. optimality**: NE is a stability concept, not an efficiency concept.
The Prisoner's Dilemma NE (both defect) is Pareto-dominated. NE = no one wants to
deviate; it says nothing about social welfare.

**Minimax theorem vs. Nash equilibrium**: Von Neumann's minimax (1928) applies only to
two-player zero-sum games. Nash (1950) generalizes to n-player non-zero-sum. In two-player
zero-sum, NE = minimax solution — they coincide. In general: distinct concepts.

**Mixed strategy interpretation**: In a mixed strategy NE, a player mixing is indifferent
between their support strategies. The mixing makes the opponent indifferent. Mixed NE is
about the opponent's incentive constraints, not the mixing player's preference for
randomness. "Why would I randomize if I'm indifferent?" — because not randomizing lets
opponents exploit your deterministic strategy.

**Subgame perfect vs. Nash**: Every SPE is a NE; not every NE is subgame perfect. Non-SPE
Nash equilibria survive on non-credible off-path threats. Backward induction eliminates them.

**PPAD-completeness is not NP-hardness**: Nash always exists (Kakutani), so the decision
problem "does a Nash equilibrium exist?" is trivially yes. PPAD = Polynomial Parity
Argument on Directed graphs — total search problems where a solution is guaranteed to exist
but finding it is computationally hard. PPAD ⊆ TFNP ⊆ FNP. PPAD-hard ≠ NP-hard.

**Cooperative vs. non-cooperative game theory**: These are not opposing schools — they
model different institutional assumptions. Cooperative GT: binding agreements possible,
question is which coalition forms and how to split. Non-cooperative GT: no binding agreements,
question is what strategies rational agents choose. Rubinstein (1982) showed you can derive
cooperative solutions from non-cooperative foundations — the divide is more about modeling
than ontology.
