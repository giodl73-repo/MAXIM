# Dice and Gambling — From Astragali to Probability Theory

## The Big Picture

```
GAMBLING AND MATHEMATICS — MUTUAL ORIGIN
═════════════════════════════════════════

ANCIENT GAMBLING           PROBABILITY THEORY           MODERN MATHEMATICS
3000 BCE – 1650 CE         1650 – 1820                  1820 – present
──────────────────         ──────────────               ──────────────────
Astragali (ankle bones)    Pascal–Fermat 1654:          Kolmogorov axioms
  used as dice               Problem of Points          Measure theory
Cubic dice ~3000 BCE         (divide stakes)            Stochastic processes
  (Mesopotamia, Egypt)     Huygens 1657:               Martingales
Roman tesserae               De ratiociniis             Random variables
  (often loaded)             in ludo aleae             Central limit theorem
Hazard (dice game)         Bernoulli 1713:              Kelly criterion
  → Craps                    Ars Conjectandi            Information theory
Backgammon lineage:          (LLN, EV formalized)       (Shannon 1948)
  Senet → Tabula           Moivre 1718:
  → Tables → Backgammon      Doctrine of Chances
                           Laplace 1812:               THE DIRECTION:
                             Théorie Analytique        Gambling → Probability
                             des Probabilités          Probability → Statistics
                                                       Statistics → Decision Theory
                                                       Decision Theory → AI

Gambling is not a social problem that happened to
produce mathematics. Gambling IS the original
empirical laboratory for probability theory.
The demand was: "what is a fair division of stakes?"
The mathematics existed to answer that demand.
```

---

## Section 1: Astragali — Pre-Cubic Dice

### What They Are

Astragalus (plural: astragali): the ankle bone of a hoofed mammal — typically sheep, goats, deer, or cattle. Four usable sides (the other two are too rounded to land stably). Used as gaming devices across virtually every ancient Mediterranean culture from approximately 3500 BCE onward.

```
ASTRAGALUS ANATOMY
═══════════════════

Cross-section of a sheep/goat astragalus:

           ┌─────────────┐
           │  CONVEX     │  broad convex side
           │  BROAD      │  most common landing ~40%
           └─────────────┘
     ┌─────┐         ┌─────┐
     │     │         │     │
     │ FLAT│         │ FLAT│  flat sides ~40% combined
     │     │         │     │  (approximately equal)
     └─────┘         └─────┘
           ┌─────────────┐
           │  CONCAVE    │  concave narrow side
           │  NARROW     │  least common ~10-20%
           └─────────────┘

Four sides, NOT equally probable.
Different cultures assigned different values to each side.

GREEK VALUES (one documented system):
  Concave narrow (χίον/chion): 1 — lowest
  Convex broad (κύων/kyon):    3 or 4 (dog, unlucky)
  Flat A (βασιλεύς):          4 (king)
  Flat B (various):            6
  (Systems varied by region and period)

ROMAN VALUES:
  One system: knucklebone (narrow concave) = 1
  Others = 3, 4, 6
  "Venus throw" (set of 4): one of each different face
  = highest, most prized.
```

### Cultural Distribution

Astragali appear in:
- Egyptian tomb paintings (~3500 BCE)
- Greek symposium culture (aristocratic gambling)
- Roman gambling (both aristocratic and plebian)
- Mesoamerican contexts (pre-Columbian)
- Persian, Indian, and Chinese contexts

They represent the near-universal human solution to the problem: "how do we generate bounded random numbers with natural, readily available objects?"

The transition to cubic dice (~3000 BCE) happened in parallel — cubic dice were found alongside astragali in the same archaeological contexts. The two technologies coexisted for millennia.

---

## Section 2: Cubic Dice — Standardization and Cheating

### Early Dice

```
ANCIENT CUBIC DICE
═══════════════════

EARLIEST: ~3000 BCE, Mesopotamia (Iran/Iraq).
  Also: Mohenjo-daro (Indus Valley), ~2600 BCE.
  Material: bone, ivory, clay, wood, glass.

OPPOSITE FACES SUM TO 7 (modern convention):
  This is NOT universal in antiquity.
  Opposing-faces = 7 was a MODERN convention.
  Ancient dice found with irregular face arrangement.
  Chinese dice: 1 and 4 colored RED.
    (1 = lucky in Chinese culture;
     4 = unlucky because 四 sì sounds like 死 sǐ = death.
     Both colored red to distinguish from others.)
  Western dice: white with black pips; 1 opposite 6,
    2 opposite 5, 3 opposite 4.

LOADED DICE (Roman era and before):
  Drilled and filled with lead on one face.
  Face with lead tends to land face-DOWN.
  → The opposite face lands face-UP more often.
  Archaeological evidence: many Roman dice specimens show
  systematic weighting.

  Modern loaded dice equivalent:
    "Tops and Bottoms": 2 sides the same
    (e.g., two 6-faces) — instantly detectable.
    Mercury-loaded: liquid mercury shifts, adjusting weight
    dynamically based on how held before throw.
```

### Probability of Standard Dice

```
PROBABILITY DISTRIBUTIONS FOR DICE
════════════════════════════════════

SINGLE DIE (fair):
  Each face: P(i) = 1/6 for i ∈ {1,2,3,4,5,6}
  E[X] = (1+2+3+4+5+6)/6 = 21/6 = 3.5
  Var[X] = E[X²] - (E[X])² = 91/6 - 12.25 = 2.9167
  Std dev: ~1.708

TWO DICE (sum):
  Min=2, Max=12.
  Sum=7 most likely: P(7) = 6/36 = 1/6
  Sum=2 or 12 least likely: P(2) = P(12) = 1/36
  E[sum] = 7 (by linearity of expectation)

  Distribution (triangular):
  Sum:  2    3    4    5    6    7    8    9    10   11   12
  Count:1    2    3    4    5    6    5    4    3    2    1
  P(%): 2.8  5.6  8.3  11.1 13.9 16.7 13.9 11.1  8.3  5.6  2.8

THREE DICE (craps uses this):
  Sum range: 3-18. E[sum] = 10.5
  Most common: 10, 11 (each with 27/216 ≈ 12.5%)
  Important in craps: sum=7 with 2 dice (16.7%)
  is different from sum=7 with 3 dice (~11.6%)

CHEVALIER DE MÉRÉ'S PROBLEM (1654):
  Question: Why does rolling 4 dice and needing at least
  one 6 differ slightly from rolling 24 pairs of dice
  and needing at least one pair of 6s?
  Naively: P(6 on one die) = 1/6; 4 dice: 4/6 > 50%? NO.
  P(at least one 6 in 4 rolls) = 1 - (5/6)^4 = 51.77%
  P(at least one double-6 in 24 rolls) = 1 - (35/36)^24 = 49.14%
  De Méré had gambled on both, thinking both were > 50%.
  He was right about 4 dice, wrong about 24 pairs.
  This problem motivated the Pascal-Fermat correspondence.
```

---

## Section 3: Pascal, Fermat, and Probability Theory

This is the moment gambling created mathematics. The year 1654 marks the formal birth of probability theory.

### The Problem of Points

A gambler named Chevalier de Méré posed a question to Blaise Pascal: if a game of chance is interrupted midway, how should the stakes be divided fairly between the players, given the current score?

```
THE PROBLEM OF POINTS
══════════════════════

SCENARIO:
  Two players, equal skill, bet $100 each ($200 total pot).
  First to win 3 rounds takes the pot.
  Game interrupted with Player A leading 2-1.

  How should the $200 be divided?

WRONG ANSWER (naive): 2/3 to A, 1/3 to B (ratio of wins).
  But A needs 1 more win; B needs 2 more wins.
  If each round is 50/50, what's the probability each
  wins the match from this point?

PASCAL'S SOLUTION:
  From 2-1, at most 2 more rounds needed (either A wins
  the next one, or B wins the next two).
  Consider all possible 2-round outcomes (exhaustive):

  Round 3: A wins (prob 1/2) → A wins match regardless
  Round 3: B wins (prob 1/2)
    Round 4: A wins (prob 1/4) → A wins match
    Round 4: B wins (prob 1/4) → B wins match (tied 2-2, but
             wait — A needs 3, so B wins if they tie)

  Actually from 2-1 (A needs 1, B needs 2):
  P(A wins match) = P(A wins next round)
                  + P(B wins next, A wins round after)
                = 1/2 + (1/2)(1/2) = 1/2 + 1/4 = 3/4

  P(B wins match) = P(B wins both next rounds)
                = (1/2)(1/2) = 1/4

  FAIR DIVISION: A gets (3/4) × $200 = $150
                 B gets (1/4) × $200 = $50

FERMAT'S APPROACH: Enumerated all possible game completions.
  Pascal and Fermat agreed on the answer by different methods.
  Their correspondence (July-October 1654) is the founding
  document of probability theory.
```

### The Mathematical Harvest

The Problem of Points generalized into the expected value framework:

```
PROBABILITY THEORY FROM GAMBLING
═══════════════════════════════════

CHRISTIAAN HUYGENS (1629-1695):
  "De ratiociniis in ludo aleae" (1657) — first published
  probability textbook. Formalized expected value (EV):
    E[X] = sum(x_i × P(x_i))
  Derived from the gambling principle: "a fair price for
  a game is the expected outcome."

JACOB BERNOULLI (1655-1705):
  "Ars Conjectandi" (1713, posthumous):
  - Law of Large Numbers (first formal proof):
    Sample average converges to E[X] as n → ∞.
  - Bernoulli trials (repeated independent experiments).
  - Binomial distribution formalized.
  Quote: "Even a stupid person... after observing many
  trials... can satisfy himself as to the probability."

ABRAHAM DE MOIVRE (1667-1754):
  "The Doctrine of Chances" (1718, with later editions):
  - Normal distribution as limit of binomial distribution
    (precursor to Central Limit Theorem).
  - Birthday problem (approximate first formulation).
  - Stirling's formula (collaboration with Stirling).
  He earned his living partly by answering gamblers'
  probability questions for payment in London coffee houses.

PIERRE-SIMON LAPLACE (1749-1827):
  "Théorie analytique des probabilités" (1812):
  - Classical definition of probability: P = favorable/total
  - Bayesian probability formalized (though Bayes 1763 first)
  - Central Limit Theorem (formal proof)
  - Moment generating functions

THE LINEAGE:
  Gambling problem → Pascal/Fermat 1654
  → Huygens 1657 (EV formalized)
  → Bernoulli 1713 (LLN, binomial distribution)
  → De Moivre 1718 (normal approximation)
  → Laplace 1812 (CLT, classical probability)
  → Kolmogorov 1933 (axiomatic probability theory)
  → Modern statistics, machine learning, AI
```

---

## Section 4: Hazard — The Craps Ancestor

### Hazard

Hazard was the most important European gambling dice game from roughly 1400 to 1900, when it was displaced by craps. It's structurally complex but was widely played.

```
HAZARD RULES
═════════════

Two dice. Two phases:

PHASE 1 — CHOOSING THE MAIN:
  "Caster" (shooter) calls a "main" — a number between 5 and 9.
  This is the target number for the caster.

PHASE 2 — ROLLING FOR CHANCE:
  Caster rolls two dice.

  IMMEDIATE OUTCOMES:
    If caster rolls the main: "Nick" = CASTER WINS instantly.
    If caster rolls 11 or 12 (if main is 5 or 9): Nick = WIN
    If caster rolls 11 or 12 (if main is 6, 7, or 8):
      Depends on exact main — complex tables existed.
    If caster rolls 2 or 3: "Out" = CASTER LOSES instantly.

  SETTING A "CHANCE":
    If none of the above: the rolled number becomes the "chance."
    Caster keeps rolling until:
      Rolls the chance again: WINS
      Rolls the main: LOSES

  This two-number mechanic (chance vs main) is identical
  in structure to craps (point vs 7).
```

Hazard is mentioned in Chaucer's Canterbury Tales (~1390): "They daunce and pleye at dees bothe day and nyght" — "dice" (dees) in the tavern scenes. It's also central to Dickens' Regency-era gambling dens.

### Craps — American Simplification

```
HAZARD → CRAPS EVOLUTION
═════════════════════════

FRENCH VERSION OF HAZARD:
  In France, "crabs" was the worst throw in Hazard
  (a losing combination). Anglicized to "crabs."
  French New Orleans brought the game to America.

BERNARD DE MARIGNY:
  Bernard Xavier Philippe de Marigny de Mandejeuil
  (1785-1868) — French Creole aristocrat of Louisiana.
  Brought Hazard to New Orleans, simplified it.
  Called it "crabs" which Americans shortened to "craps."
  Lost much of his fortune gambling on the game.
  The street he built in New Orleans (now Burgundy Street
  and Craps Street, later Bienville Street) was named
  after the game in his era.

AMERICAN CRAPS SIMPLIFICATION:
  Eliminated the "main" selection. Simplified pass/don't pass.
  Modern craps: roll a 7 or 11 on come-out = instant win.
                roll 2, 3, or 12 on come-out = instant loss (craps).
                any other number = "point." Roll point again = win.
                roll 7 after point = "seven-out" = loss.
```

### Modern Craps Mathematics

```
CRAPS BETTING ANALYSIS
════════════════════════

PASS LINE BET (most basic):
  Win: come-out 7 or 11 = P(7) + P(11) = 6/36 + 2/36 = 8/36
  Lose: come-out 2,3,12 = 1/36 + 2/36 + 1/36 = 4/36
  Point: 4,5,6,8,9,10 = 24/36

  P(win given point = 4): P(4)/[P(4)+P(7)] = 3/9 = 1/3
  P(win given point = 5): P(5)/[P(5)+P(7)] = 4/10 = 2/5
  P(win given point = 6): P(6)/[P(6)+P(7)] = 5/11
  P(win given point = 8): same as 6 = 5/11
  P(win given point = 9): same as 5 = 2/5
  P(win given point = 10): same as 4 = 1/3

  Overall P(pass line wins):
  = 8/36 + (6/36)(1/3) + (8/36)(2/5) + (10/36)(5/11)
    come-out win  point 4+10      point 5+9      point 6+8
  = 8/36 + 2/36 × 2 + (8/36)(2/5) × 2 + (10/36)(5/11) × 2
    (accounting for both point values that share win prob)
  ≈ 0.4929 = 49.29%

  House edge = 50% - 49.29% = 1.41% (standard published figure)

BETS AND THEIR EDGES:
  Pass/Come line:          1.41% house edge
  Don't Pass/Come:         1.36% (slightly better)
  Free Odds (behind line): 0.00% house edge (true odds payout!)
  Place 6 or 8:            1.52%
  Place 5 or 9:            4.00%
  Place 4 or 10:           6.67%
  Hardways 6 or 8:         9.09%
  Hardways 4 or 10:       11.11%
  Proposition "any 7":    16.67%
  Proposition "any craps": 11.11%

FREE ODDS: The unique zero-edge bet.
  After establishing a point, you can bet "free odds"
  behind your pass line bet. These pay TRUE odds:
    Point 4 or 10: pays 2:1
    Point 5 or 9: pays 3:2
    Point 6 or 8: pays 6:5
  No house edge — casino offers this because it's covered
  by the 1.41% edge on the required pass line bet.
  The more odds you take, the lower your overall edge.
  3-4-5× odds tables (common): effective overall edge ~0.37%.
  100× odds tables (rare): overall edge → near 0.
```

---

## Section 5: Backgammon — The Dice Race Game

### Historical Lineage

```
BACKGAMMON LINEAGE
═══════════════════

3100 BCE: SENET (Egypt) — race game, throw sticks
                │
2600 BCE: ROYAL GAME OF UR (Mesopotamia) — race, tetrahedral dice
                │
~500 BCE: TABLES family — various European race games
                │
100 CE:  TABULA (Rome) — 3 dice, 24 points, 15 checkers each
         Emperor Zeno's bad position documented (~480 CE)
                │
~600 CE: NARD — Persian/Arab game (possibly influenced by
         backgammon, or variant of Tabula)
                │
~1600 CE: TABLES → BACKGAMMON (English name first documented 1645)
                │
1920s:   DOUBLING CUBE ADDED — transformed strategy fundamentally
                │
Present: WORLD BACKGAMMON CHAMPIONSHIP
         TD-Gammon AI (1992), GNU Backgammon (open source)
```

### Backgammon Rules

```
BACKGAMMON BOARD
═════════════════

     13  14  15  16  17  18     19  20  21  22  23  24
   +─────────────────────────+──+─────────────────────────+
   │  ▼   ▼   ▼   ▼   ▼   ▼   │  │  ▲   ▲         ▲   ▲ │
   │ ●●  ●   ●         ○○○  │  │  ●●●●● ●         ○○  │
   │                         │  │                         │
   │ BAR                     │  │                         │
   │                         │  │                         │
   │  ▼      ▼   ▼      ▼   │  │   ▼         ▼          │
   │ ●● ○○  ○   ●●●  ○○  │  │  ●●        ●●●●●        │
   +─────────────────────────+──+─────────────────────────+
     12  11  10   9   8   7      6   5   4   3   2   1

● = Black (moves from 24→1), ○ = White (moves 1→24)
Both try to bear off all checkers from their home board.

BASIC RULES:
  Roll 2 dice, move one or two checkers exactly those amounts.
  Can land on empty point or own point (multiple checkers ok).
  If you land on opponent's lone checker (blot): BAR that checker.
  Barred checkers re-enter from opponent's home (points 19-24 for Black).
  Must re-enter all checkers before moving others.
  Once all checkers in home board: bear off (roll to remove them).
  First player to bear off all 15 checkers: wins.

GAMMON: opponent has borne off 0 checkers = 2× stake.
BACKGAMMON: opponent has checker on bar or in your home = 3× stake.
```

### The Doubling Cube

The doubling cube was added to backgammon around 1920-1925 (exact origin disputed, possibly New York or Chicago). It transformed backgammon into a much deeper strategic game:

```
DOUBLING CUBE MECHANICS
════════════════════════

The cube starts at 2 (but is "off" meaning stakes = 1).
Either player may offer to DOUBLE the stakes on their turn
before rolling.
Opponent must:
  ACCEPT: game continues at doubled stakes; acceptor "owns" cube
          (only acceptor can now re-double)
  REJECT (PASS): game ends immediately; offerer wins current stakes

STRATEGY IMPLICATIONS:
  If I'm winning but not crushing: should I double?
    Double when your opponent's take threshold is near.
  If I'm losing and offered the cube: should I accept?
    Accept when your winning probability > ~20% (the "take point")

TAKE POINT CALCULATION:
  If you decline: lose 1 unit.
  If you accept and eventually win: win 2 units.
  If you accept and eventually lose: lose 2 units.
  Take if: P(win after accept) × 2 - (1-P) × 2 > -1
  Simplify: 2P - 2(1-P) > -1
            4P - 2 > -1
            4P > 1
            P > 25%
  So take when winning probability > 25% (simplified analysis;
  more complex analysis involving recubes adjusts this).

GAMMON IMPACT: If opponent has gammon chance (wins 2× base),
  your take point rises (need more than 25% to compensate
  for gammon risk).

"CUBE OWNERSHIP" and cube strategy:
  Owning the cube = option to re-double.
  This has real value. Accept a double partly because
  you gain cube ownership and can re-double if the
  position shifts.
```

### TD-Gammon — The AI Precursor

## Engineering Bridge: TD-Gammon as MDP Policy Evaluation

```
DOMAIN CONCEPT                CS / ENGINEERING EQUIVALENT
──────────────────────────────────────────────────────────────────────────────
Backgammon board position     State s in a Markov Decision Process (MDP)
  + whose turn + dice roll      next state depends only on current state +
                                action + dice (Markov property)

TD(λ) update rule             Bellman equation for policy evaluation:
  V(s) ← V(s) + α[r + γV(s') - V(s)]    V(s) = r + γ · E[V(s')]
  temporal difference error               Bellman residual driven to zero

Neural network V(s)           Function approximator for the value function
  (2 hidden layers, 80 units)   replaces tabular V(s) — necessary because
                                backgammon has ~10^20 states

Self-play training            On-policy evaluation: the MDP's transition
                                probabilities are defined by the current
                                policy (which is being learned simultaneously)
```

TD-Gammon showed that TD learning on an MDP — with a neural function approximator and self-play — converges to near-optimal policy evaluation without any domain knowledge. The same Bellman-equation-plus-NN architecture reappears in AlphaGo's value network 24 years later.

```
TD-GAMMON (Gerald Tesauro, IBM, 1992)
═══════════════════════════════════════

WHY IT MATTERS HISTORICALLY:
  TD-Gammon was the FIRST game AI to achieve near-expert
  play using neural networks + self-play reinforcement
  learning. Predates Deep Blue. Predates AlphaGo by 24 years.

METHOD:
  Temporal Difference Learning (TD(λ)) applied to backgammon.
  Neural network: 2 hidden layers, 80 hidden units.
  Training: played against itself from random initialization.
  No backgammon knowledge encoded.
  No human game data in training.
  Only supervised signal: win/lose at end of game.

  TD(λ) update rule:
    V(s_t) ← V(s_t) + α[r_t+1 + γV(s_t+1) - V(s_t)]
  where V(s) = estimated value of state s,
        α = learning rate, γ = discount factor.
  After each game, update all states in the trajectory.

RESULT:
  After 1.5 million self-play games: near world-champion level.
  Human players examined TD-Gammon's moves and found them
  remarkably sound. Some TD-Gammon moves influenced human
  backgammon theory (revised opening book recommendations).

SIGNIFICANCE FOR AI:
  Self-play + RL can generate expert-level play without
  human knowledge. This insight directly inspired:
  - AlphaGo (2016): same architecture concept with MCTS
  - AlphaZero (2017): same tabula rasa self-play for chess/go/shogi

"TD-Gammon is to game AI what the ENIAC is to computing —
you can see the modern lineage from it." — AI historian perspective
```

---

## Section 6: Roulette and Slots — Pure Casino Games

### Roulette

```
ROULETTE MATHEMATICS
═════════════════════

EUROPEAN (single zero): 37 pockets (0-36)
AMERICAN (double zero): 38 pockets (0-36 + 00)

HOUSE EDGE:
  European: E[loss] = (1/37) × 1 per unit = 2.70%
    (on single-number bet: P(win)=1/37, pays 35:1
     E = 35/37 - 36/37 = -1/37 ≈ -2.70%)
  American: E[loss] = (2/38) × 1 per unit = 5.26%
    (double zero doubles the house advantage)

All roulette bets have the SAME house edge (2.70% or 5.26%).
This is mathematically required by the structure.
The "even money" bets (red/black, odd/even, high/low)
seem 50/50 but the 0 (and 00) are green and belong to no
bet category — they all lose.

GAMBLER'S FALLACY (roulette's famous fallacy):
  "Red has come up 10 times in a row; black is 'due.'"
  This is incorrect. Each spin is independent.
  P(red on spin 11) = 18/38 = 47.4% regardless of history.
  Roulette wheels have no memory.

MONTE CARLO FALLACY (famous historical incident):
  August 18, 1913: a roulette ball fell on black 26 times
  in a row at the Monte Carlo Casino.
  Gamblers lost millions betting "red is due."
  The probability of 26 consecutive blacks: ~(18/38)^26 ≈ 0.000073%
  Rare, but had to happen eventually given all the spins.
```

### Slot Machines

```
SLOT MACHINE HISTORY
═════════════════════

1895: Charles Fey invents Liberty Bell (San Francisco).
  3 reels, 5 symbols: horseshoe, diamond, spade, heart, bell.
  "Bell" = highest payout (3 bells = Liberty Bell jackpot).
  Mechanical: spinning drums with physical symbols.
  Payout at 50% (extremely poor by modern standards).

1907: Herbert Mills creates Operator Bell — fruit symbols.
  Cherries, melons, oranges, lemons replaced the card suits.
  BAR symbol: from Bell-Fruit Gum company logo.
  "Fruit machine" term (British English) derives from these.

1963: First electromechanical slot (Bally Money Honey).
  Unlimited coin payout. Bottom hopper.

1976: First video slot machine (Fortune Coin, Las Vegas).
  CRT display instead of mechanical reels.

1990s-2000: RNG-based slots completely replace mechanical.
  Random Number Generator: PRNG generates outcome BEFORE
  the reels spin. Spinning animation is cosmetic.

MODERN SLOT MATH:
  RTP (Return to Player): percentage of wagered money
  returned to players over time.
    Las Vegas slots: typically 85-98% RTP by law.
    UK machines: typically 92%+ regulated.
    Online slots: typically 95-99% (lower overhead).
  House edge = 100% - RTP.

  VOLATILITY:
    Low volatility: frequent small wins (slots near 95% RTP
                    paid frequently)
    High volatility: rare large wins (jackpot machines)
    Both can have same RTP but wildly different short-term variance.

"NEAR MISS" PROGRAMMING:
  Physical reels could be independently weighted.
  Jackpot symbol could appear more often above/below the
  payline than ON the payline, creating artificial near-misses.
  Regulated (banned in many jurisdictions) but remains
  a known dark pattern in machine design.
```

---

## Section 7: The Gambler's Ruin and Bankroll Theory

```
GAMBLER'S RUIN PROBLEM
═══════════════════════

SETUP: Two players, A and B.
  A starts with $a, B starts with $b.
  Each round: A wins $1 with prob p, loses $1 with prob q=1-p.
  Game ends when one player is ruined (reaches $0).

  This is a random walk on {0, 1, ..., a+b} with absorbing
  barriers at 0 and a+b.

  Martingale derivation (Doob's optional stopping theorem):
    If p ≠ q: M_t = (q/p)^X_t is a martingale.
    If p = q: M_t = X_t itself is a martingale.
    Apply optional stopping at the hitting time of
    {0, a+b}. Since M_0 = E[M_τ]:
      (q/p)^a = P(ruin) · (q/p)^0 + (1-P(ruin)) · (q/p)^(a+b)
    Solve for P(ruin) to recover the formula below.
    This is a cleaner derivation than the difference-
    equation approach and generalizes to asymmetric walks.

PROBABILITY OF RUIN (player A is ruined):
  If p ≠ q:  P(A ruined) = [(q/p)^a - (q/p)^(a+b)] / [1 - (q/p)^(a+b)]
  If p = q:  P(A ruined) = b / (a+b)

  Specifically, P(A eventually ruins B) =
  If p ≠ q:  P(A wins) = [1 - (q/p)^a] / [1 - (q/p)^(a+b)]
  If p = q:  P(A wins) = a / (a+b)

APPLICATION: Casino vs. Gambler
  Casino has essentially infinite bankroll (b → ∞).
  Even if p > 0.5 (favorable game for gambler!), as b → ∞:
    P(gambler ruined) → 1 if p < 0.5 (unfavorable)
    P(gambler ruined) → exp(−2ka) if p > 0.5 (favorable game)
  With any house edge (p < 0.5), the gambler is
  GUARANTEED to eventually be ruined.

  The only way to "beat" the casino: win your target amount
  and leave immediately (finite session, don't play forever).
  But even then: expected loss is fixed at house_edge × wagered.
```

### Kelly Criterion

```
KELLY CRITERION (J.L. Kelly Jr., 1956)
════════════════════════════════════════

PROBLEM: How much of your bankroll should you bet per round
to maximize long-run wealth accumulation?

SETUP:
  Each bet: win with probability p, lose with probability q=1-p.
  Win pays b:1 (win b units for every 1 unit risked).
  Current bankroll: W.

KELLY FRACTION:
  f* = (bp - q) / b = p - q/b

  Example: coin flip, p=0.55, q=0.45, even money (b=1):
    f* = 0.55 - 0.45/1 = 0.10
    Bet 10% of bankroll each round.

  Example: blackjack with count (+2 true count gives 1% edge):
    p ≈ 0.505, b ≈ 1.0 (simplification):
    f* = 0.505 - 0.495 = 0.01 = 1% of bankroll.
    Matches card counter bet sizing in practice.

WHY KELLY MAXIMIZES LONG-RUN GROWTH:
  The Kelly criterion maximizes E[log(W)] — expected log wealth.
  This is equivalent to maximizing the geometric growth rate.
  Bet more than f*: growth rate decreases (overbetting).
  Bet less than f*: growth rate decreases (underbetting).
  f* is the unique maximum of the log-wealth growth function.

PRACTICAL USE:
  Professional poker, sports betting, investing (Buffett, Thorp):
  All use Kelly or fractional Kelly (0.25× to 0.5× Kelly)
  to manage bankroll and maximize long-run growth.
  Full Kelly: high variance. Half Kelly: lower variance,
  approximately same long-run growth.

  Ed Thorp (Beat the Dealer, card counting book):
  PhD mathematician who derived Kelly for blackjack.
  Later applied it to hedge fund management (Princeton-Newport
  Partners, one of the first quant hedge funds, 1969-1988).
```

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| Are astragali fair dice? | No — asymmetric bone shape creates non-uniform probabilities |
| When were cubic dice invented? | ~3000 BCE, Mesopotamia and Indus Valley |
| What caused formal probability theory? | Pascal-Fermat correspondence (1654) — Problem of Points (gambling) |
| What is De Méré's problem? | P(one 6 in 4 dice)≠P(double-6 in 24 pairs) by the margin 51.77% vs 49.14% |
| Pass line house edge in craps? | 1.41% |
| What is the only zero-edge bet in craps? | Free Odds (behind the pass line) |
| European vs American roulette house edge? | 2.70% vs 5.26% (single vs double zero) |
| Who invented slot machine? | Charles Fey, Liberty Bell, 1895 |
| TD-Gammon significance? | First neural net self-play to reach expert game performance (1992) — precursor to AlphaGo |
| Kelly Criterion formula? | f* = (bp - q) / b = p - q/b |

---

## Common Confusion Points

**"Probability theory was invented by mathematicians studying gambling"**: The causation goes the other way — gamblers had practical questions about fair division of stakes and hired mathematicians to solve them. Pascal and Fermat were responding to specific gambling puzzles, not engaging in abstract research.

**"In craps, 7 is always bad"**: The number 7 is good on the come-out roll (natural, wins pass line) but bad after a point is established (seven-out, loses). The psychological framing of 7 as "unlucky" at the craps table comes from the losing scenario.

**"The Gambler's Fallacy is just superstition"**: It's a specific mathematical error — treating dependent sequential events as if they're dependent when they're not. "Due to come" up has no statistical meaning for independent events. However, if you observe many outcomes and suspect the wheel is biased, *then* past outcomes are informative about whether the device is fair.

**"Backgammon is mostly luck"**: At high levels, the doubling cube strategy is deep enough that skill dominates over large samples. Backgammon has more luck than chess (dice) but significantly less than might appear. World-class players consistently beat weaker players in long matches despite the randomness.

**"The Kelly Criterion tells you the optimal bet size"**: Kelly maximizes expected log wealth, which is the right objective for long-run growth. However, full Kelly is aggressive — a run of bad luck can lose 90%+ of bankroll before recovery. Most practitioners use fractional Kelly (0.25-0.5×) for variance reduction.

**"Card counting is the same as the Gambler's Ruin solution"**: Card counting works because a blackjack shoe is *not* an independent sequence — removing cards changes probabilities for subsequent cards. This is Bayes' theorem in action (conditioning on observed cards). Roulette is genuinely memoryless; blackjack is not.
