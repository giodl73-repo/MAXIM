# Games History — Overview
<!-- @editor[bridge/P2]: No bridge from formal language theory / automata to game trees — a learner with MIT TCS background will immediately recognize extensive-form games as trees with labeled nodes and labeled edges (information sets as equivalence classes on histories); make this connection explicit near the extensive-form diagram -->

## The Big Picture

```
GAMES AS HUMAN UNIVERSAL — 5,000 Years of Formalized Play
===========================================================

ANCIENT                    CLASSICAL              MEDIEVAL/EARLY MODERN
3100 BCE ───────────────── 600 CE ─────────────── 1400–1700 CE
  │                          │                         │
Senet (Egypt)            Chaturanga (India)        Chess modernized
Royal Game of Ur         Go spreads to Japan       Card games (suits)
Mancala family           Tafl variants (Norse)     Dice games codified
Mesoamerican ball game   Liubo (China)             Gambling houses
Knucklebones/astragali   Roman Latrunculi          Billiards appears

EARLY MODERN              INDUSTRIAL              20TH CENTURY          DIGITAL
1700–1850                 1850–1950               1950–1985             1985–present
   │                         │                       │                     │
Whist → Bridge           Monopoly (1903)         Go professional       Video games
Hazard → Craps           Kriegsspiel → D&D       Chess engines         Internet play
Snooker invented         Poker standardized      Contract Bridge       Esports
Billiards professionalized  WSOP founded (1970)  Vegas expansion       Mobile F2P

INFORMATION STRUCTURE     AGENCY STRUCTURE        RANDOMNESS STRUCTURE
  Perfect Information  ←──────────────────────→  Imperfect Information
  Chess, Go, Checkers                             Poker, Backgammon, Solitaire

  Zero-Sum          ←──────────────────────────→  Cooperative / Non-Zero-Sum
  Chess, Poker                                    Pandemic, bridge (partnership)

  Deterministic     ←──────────────────────────→  Stochastic
  Chess, Go                                       Backgammon, Poker, Craps
```

---

## Section 1: Game Theory Vocabulary — The Mathematical Substrate

Games aren't just entertainment — they're the physical instantiation of formal mathematical structures. Most of probability theory was literally born from gambling. The vocabulary here maps directly to what you know from discrete math.

### Information Structure

```
PERFECT INFORMATION                   IMPERFECT INFORMATION
════════════════════                  ═════════════════════

All players see the complete          Private information exists.
game state at all times.              Some state is hidden.

                                      Sub-cases:
  Chess: both players see               INCOMPLETE INFORMATION:
  all pieces on the board.              Players don't know each
                                        other's type/payoffs.
  Go: all stones visible.               (Harsanyi's Bayesian games)
  Checkers: open board.
                                        IMPERFECT RECALL:
  Formalism: every               →      Player forgets own actions
  information set is a                  (unusual, but theoretically
  singleton. Game tree nodes            possible — some card games
  have unique information sets.         with discard pile shuffled)

COMPLETE INFORMATION                  INCOMPLETE INFORMATION
(payoffs known to all)                (types/payoffs uncertain)

  Poker: you know the rules            Mechanism design territory.
  and payoffs.                         Auctions: bidders don't
  Poker is IMPERFECT but               know others' valuations.
  COMPLETE information.
```

Critical distinction the literature muddies: **imperfect** vs **incomplete** information are orthogonal axes. Chess is perfect + complete. Poker is imperfect + complete (you know the rules and payoff structure, just not opponents' hole cards). Most auctions are imperfect + incomplete.

### Zero-Sum vs Cooperative

```
ZERO-SUM                              NON-ZERO-SUM
════════                              ════════════

Σ payoffs = 0 (or constant)           Pareto improvements possible.
What I win, you lose.
                                      COOPERATIVE: players can
  Chess: I win (+1), you              form binding agreements.
  lose (-1).                            Bridge partnerships.
                                        Team sports.
  Poker (heads-up): every              Pandemic (board game).
  chip I win you lost.
                                      COMPETITIVE NON-ZERO-SUM:
  Von Neumann 1928: minimax            No binding agreements, but
  theorem — in zero-sum               joint outcomes not fixed-sum.
  games, there exists a                 Prisoner's Dilemma structure.
  saddle point in mixed                 Negotiation games.
  strategies.

Minimax theorem:
  max_x min_y f(x,y) = min_y max_x f(x,y)
  where f is the payoff function,
  x is row player's mixed strategy,
  y is column player's mixed strategy.
  (von Neumann, 1928)
```

### Skill vs Luck Spectrum

```
PURE SKILL                                              PURE CHANCE
══════════                                              ═══════════
     │                                                       │
     │    Chess   Go    Checkers                             │
     │      │      │       │                                 │
     │      ▼      ▼       ▼                                 │
     │   ┌─────────────────────┐                            │
     │   │ SOLVED or NEAR-SOLVED│                            │
     │   │ No randomness.       │                            │
     │   │ Tree search dominates│                            │
     │   └─────────────────────┘                            │
     │                                                       │
     │         Backgammon    Bridge    Scrabble              │
     │              │           │         │                  │
     │              ▼           ▼         ▼                  │
     │         ┌──────────────────────────────┐             │
     │         │ SKILL-DOMINANT WITH VARIANCE │             │
     │         │ Luck flattens short-term      │             │
     │         │ results but skill dominates   │             │
     │         │ over large sample sizes.      │             │
     │         └──────────────────────────────┘             │
     │                                                       │
     │                  Poker (all variants)                 │
     │                        │                              │
     │                        ▼                              │
     │              ┌──────────────────┐                    │
     │              │ SKILL + SIGNIFICANT│                   │
     │              │ VARIANCE           │                   │
     │              │ Requires large N   │                   │
     │              │ to demonstrate edge│                   │
     │              └──────────────────┘                    │
     │                                                       │
     │                                    Roulette  Slots   │
     │                                        │        │    │
     │                                        ▼        ▼    │
     │                              ┌──────────────────────┐│
     │                              │ HOUSE EDGE DOMINANT  ││
     │                              │ No skill reduces EV  ││
     │                              │ Negative EV guaranteed││
     │                              └──────────────────────┘│
     │                                                       │
══════════════════════════════════════════════════════════════
```

The mathematical formalization: if we define skill as the mutual information between player decisions and outcomes, chess maximizes this (near-total correlation over large samples), slots minimize it (zero correlation).

### Solution Concepts

**Nash Equilibrium**: A strategy profile (s₁*, s₂*, ..., sₙ*) where no player i can improve their payoff by unilaterally deviating from sᵢ*.

Formally: uᵢ(sᵢ*, s₋ᵢ*) ≥ uᵢ(sᵢ, s₋ᵢ*) for all sᵢ ∈ Sᵢ

<!-- @editor[content/P2]: PPAD-completeness claim needs more precision for this learner — PPAD is a subclass of TFNP (total function problems guaranteed to have a solution by a parity/existence argument); Daskalakis-Goldberg-Papadimitriou 2006 (3+ players) and Chen-Deng 2006 (2-player) are major TCS results worth naming since this learner will recognize their significance -->
Nash's 1950 theorem guarantees existence in finite games with mixed strategies. The challenge is *selection* among multiple equilibria and *computation* (PPAD-complete for general games).

**Dominant Strategies**: Strategy sᵢ strictly dominates sᵢ' if:
uᵢ(sᵢ, s₋ᵢ) > uᵢ(sᵢ', s₋ᵢ) for ALL s₋ᵢ

Iterated elimination of strictly dominated strategies (IESDS) simplifies many games.

**Minimax** (zero-sum specific): Von Neumann's theorem says the minimax value equals the maximin value — the game has a well-defined value. In chess this means there's a theoretically optimal game value (win, draw, or loss for White), even though it's computationally unreachable.

**Pareto Optimality**: An outcome is Pareto optimal if no alternative exists that improves at least one player without worsening another. In non-zero-sum games, Nash equilibria are often NOT Pareto optimal (Prisoner's Dilemma).

```
NORMAL FORM vs EXTENSIVE FORM
══════════════════════════════

NORMAL FORM (Strategic Form):         EXTENSIVE FORM (Game Tree):
Players choose strategies              Explicit temporal structure.
simultaneously.
                                            Root (chance or P1)
     Player 2                               /              \
     Left   Right                        P1:A            P1:B
P1 Top | 3,1 | 0,2 |                    /    \          /    \
   Bot | 1,0 | 2,3 |                  P2:C  P2:D    P2:E  P2:F
                                       /\    /\      /\    /\
Normal form collapses the          (1,1)(2,0)(0,2)(3,1)(2,2)(1,3)(0,1)(2,2)
sequential structure.
Useful for simultaneous games.     Extensive form preserves:
                                   - Temporal order
                                   - Information sets (dashed boxes
                                     around nodes P2 can't distinguish)
                                   - Chance nodes (Nature moves)
                                   - Subgame perfect equilibria
```

<!-- @editor[content/P2]: Backward induction connection missing — SPE via backward induction is the natural algorithm for finite perfect-information games (like chess), and this is directly analogous to dynamic programming; the learner's MIT TCS background means this bridge (backward induction = DP on the game tree) would be immediately useful here -->
**Subgame perfect equilibrium** (Selten 1965): Nash equilibrium that is a Nash equilibrium in every subgame. Eliminates non-credible threats. Critical for sequential games — chess, for example, has an SPE (theoretically).

---

## Section 2: Game Taxonomy

### Spatial Taxonomy of Game Types

```
┌─────────────────────────────────────────────────────────────────────┐
│                        GAME SPACE                                    │
│                                                                      │
│  ABSTRACT STRATEGY          WAR GAMES           RACE GAMES          │
│  ──────────────────          ─────────           ──────────          │
│  Chess, Go, Checkers,        Chess (can be       Senet, Backgammon, │
│  Othello, Hive               framed as),         Parcheesi, Sorry,  │
│  No theme, pure logic.       Warhammer,          Snakes/Ladders.    │
│  Perfect information.        Kriegsspiel,        Luck + movement.   │
│                              ASL, Twilight Imp.                     │
│                                                                      │
│  CAPTURE GAMES              GAMBLING GAMES       DEXTERITY          │
│  ─────────────              ──────────────       ──────────         │
│  Mancala (territory),        Poker, Craps,       Lawn bowling,      │
│  Fox & Geese,                Blackjack, Bingo,   Shuffleboard,      │
│  Tafl (Norse),               Roulette, Slots.    Croquet,           │
│  Reversi/Othello.            Betting structure.  Billiards/Snooker. │
│                                                                      │
│  COOPERATIVE               DEDUCTION/SOCIAL     DECK-BUILDING       │
│  ────────────              ─────────────────    ─────────────       │
│  Pandemic, Spirit           Clue/Cluedo,         Dominion, Marvel   │
│  Island, Arkham Horror.     Werewolf, Mafia,     Champions,         │
│  Players vs game.           Codenames.           Hearthstone.       │
│  Pareto alignment.          Bayesian inference.                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Game Design Primitives

Every game can be decomposed into six primitives:

| Primitive | Description | Examples |
|-----------|-------------|---------|
| **State space** | All possible configurations | Chess: ~10^47 legal positions; Go: ~10^170 |
| **Actions** | Legal moves from a state | Chess: average 35 legal moves per position |
| **Information** | What each player observes | Perfect (chess) vs imperfect (poker) |
| **Agency** | Player decisions matter | Chess: total agency; slots: zero |
| **Feedback loops** | How outcomes affect future states | Compounding advantages, snowball effects |
| **Payoff structure** | Terminal rewards | Win/lose/draw vs continuous scoring |

**Branching factor × depth = search complexity:**
- Tic-tac-toe: b≈4, d=9 → trivially solved
- Checkers: b≈10, d≈70 → solved (Schaeffer 2007)
- Chess: b≈35, d≈80 → not solved, engines superhuman
- Go: b≈250, d≈150 → not solved, engines superhuman post-AlphaGo 2016

---

## Section 3: Why Games Matter — Functions and Origins

### The Evolutionary Substrate

Johan Huizinga's *Homo Ludens* (1938) argued play precedes culture — animals play before they develop culture, and human culture itself contains a play element at its core. The German Kulturspiele tradition: play is not trivial, it is foundational.

```
EVOLUTIONARY FUNCTIONS OF GAMES
═════════════════════════════════

SKILL PRACTICE (safe failure)         SOCIAL BONDING
─────────────────────────────         ──────────────
  Animals play-fight before          Shared games create
  real combat. Human children         in-group cohesion.
  develop motor/cognitive             Common reference points.
  skills through play without         Alliance formation (bridge
  mortal stakes.                       partners, gaming clans).

RISK SIMULATION                       RESOURCE COMPETITION
───────────────                        (under safe conditions)
  Chess: practice military            Poker trains zero-sum
  strategy without armies.             negotiation/bluffing.
  Economic games: practice            Monopoly (originally):
  resource management.                 demonstrate economic
  Probability calibration.             dynamics to players.

STATUS COMPETITION                    CULTURAL TRANSMISSION
──────────────────                    ─────────────────────
  Games as socially acceptable        Rules encode cultural
  dominance hierarchies.               values. Chess encodes
  Board room to board game.            medieval hierarchy.
  Chess as intelligence signal.        Go encodes East Asian
  Poker as risk tolerance signal.      aesthetics of balance.
```

### Mathematics Born from Games

This is not hyperbole: formal probability theory was invented to solve gambling problems.

- **1654**: Pascal and Fermat's correspondence on the "Problem of Points" (how to divide stakes if a game of chance is interrupted) → foundations of probability
- **1657**: Huygens, *De ratiociniis in ludo aleae* — first formal treatment of expected value
- **1713**: Bernoulli, *Ars Conjectandi* — law of large numbers, expected value formalized
- **1812**: Laplace, *Théorie analytique des probabilités* — building on centuries of gambling analysis
- **1928**: Von Neumann's minimax theorem — game theory from chess analysis
- **1944**: Von Neumann & Morgenstern, *Theory of Games and Economic Behavior*
- **1950**: Nash equilibrium — from poker-like strategic reasoning

The arrow goes: gambling games → probability theory → statistics → decision theory → economics → AI planning.

---

## Section 4: The Full Historical Arc

```
GAMES HISTORY TIMELINE
═══════════════════════

3100 BCE ─── SENET (Egypt)
              │ Oldest surviving game boards + pieces.
              │ Race game with binary throw sticks.
              │ Religious symbolism (journey through afterlife).
              │
2600 BCE ─── ROYAL GAME OF UR (Mesopotamia)
              │ Cuneiform rulebook survives.
              │ Binary tetrahedral dice.
              │
~2500 BCE ── GO/WEIQI (China — traditional date, debated)
              │ Earliest written records: Han dynasty.
              │ Territory control abstraction.
              │ Highest combinatorial complexity of any game.
              │
~1300 BCE ── MESOAMERICAN BALL GAME
              │ 1,500+ courts found archaeologically.
              │ Rubber ball (earliest known vulcanized rubber use).
              │
500 BCE ──── MANCALA FAMILY
              │ Sowing/capturing mechanic.
              │ African/Asian/Caribbean spread.
              │
~600 CE ──── CHATURANGA (India)
              │ 4-player dice chess → 2-player abstract strategy.
              │ Piece types map to military: infantry, cavalry,
              │ elephants, chariots.
              │
~750 CE ──── SHATRANJ (Persia/Arabia)
              │ Islam spreads chess worldwide.
              │ Counsellor (firz) and elephant (fil) pieces
              │ have limited movement.
              │
~900 CE ──── PLAYING CARDS (China)
              │ Tang dynasty paper cards.
              │
1300s ─────── MAMLUK DECK (Egypt/Syria)
              │ 52 cards, 4 suits. Foundation of modern deck.
              │
1475 ────── CHESS REVOLUTION (Europe)
              │ Queen and bishop gain modern movement.
              │ Game tempo doubles.
              │
1500s ─────── CARD GAMES PROLIFERATE
              │ Trick-taking (proto-Bridge), gambling games.
              │
1742 ────── EDMOND HOYLE codifies Whist.
              │ First systematic game rulebook.
              │
~1800s ──── PROFESSIONAL CHESS emerges.
              │ Morphy, Anderssen, Steinitz — Romantic era.
              │
1830s-60s ── POKER on Mississippi riverboats.
              │
1875 ────── SNOOKER invented (British India).
              │
1895 ────── SLOT MACHINE (Charles Fey).
              │
1903 ────── LANDLORD'S GAME → Monopoly.
              │
1925 ────── CONTRACT BRIDGE (Vanderbilt).
              │
1928 ────── Von Neumann minimax theorem.
              │
1944 ────── Theory of Games (von Neumann/Morgenstern).
              │
1950 ────── Nash equilibrium.
              │
1950s ─────── SHANNON / TURING — chess programs sketched.
              │
1962 ────── SPACEWAR! — first widely distributed video game.
              │
1970 ────── WSOP founded (poker professionalized).
              │
1972 ────── PONG (Atari). Home console era begins.
              │
1974 ────── D&D (Gygax/Arneson). RPG genre born.
              │
1978-83 ─── ARCADE GOLDEN AGE (Space Invaders, Pac-Man).
              │
1985 ────── NES saves video game market.
              │
1992 ────── TD-GAMMON: first neural net to reach expert play.
              │
1995 ────── SETTLERS OF CATAN: Eurogame revolution.
              │
1997 ────── DEEP BLUE defeats Kasparov (chess).
              │
2003 ────── POKER BOOM (Moneymaker, online explosion).
              │
2003 ────── STEAM: digital distribution transforms PC gaming.
              │
2008 ────── MOBILE GAMES (App Store). F2P model.
              │
2016 ────── ALPHAGO defeats Lee Sedol (Go).
              │
2017 ────── ALPHAZERO: tabula rasa, beats Stockfish in 4 hours.
              │
2017 ────── LIBRATUS/PLURIBUS: poker solved heads-up + 6-handed.
              │
2017 ────── FORTNITE: battle royale + battle pass model.
              │
2019 ────── GLOOMHAVEN/$9M Kickstarter board game renaissance.
              │
2021 ────── DOTA 2 INTERNATIONAL: $40M prize pool.
```

---

## Section 5: The Computational Structure of Games

For the MIT TCS background: games map cleanly onto complexity classes.

```
GAME COMPLEXITY HIERARCHY
══════════════════════════

GAME                COMPLEXITY          STATUS
──────              ──────────          ──────
Tic-tac-toe         O(1) (forced draw)  Solved trivially
Nim                 PTIME               Solved (Sprague-Grundy 1930s)
Checkers            PTIME-checkable     Solved (Schaeffer 2007)
  (weakly)          weakly
Oware (Mancala)     PSPACE-hard         Not solved
Chess               EXPTIME-complete    Not solved (proved EXP-hard
  (generalized)     (generalized)       by Fraenkel/Lichtenstein)
Go                  PSPACE-hard         Not solved (standard)
  (standard 19×19)  (more precisely:    AlphaGo dominates but
                    EXPTIME-complete    game not solved
                    generalized)
Poker (heads-up     PPAD-complete?      Near-solved by Libratus/
 NL Hold'em)        (Nash computation)  Pluribus via abstraction
Backgammon          Stochastic          TD-Gammon, GNU BG near-optimal
                    (chance nodes)      via RL
```

<!-- @editor[content/P2]: Sprague-Grundy theory absent from the complexity section — for a TCS reader this is a glaring gap; the theorem that every impartial game is equivalent to a Nim heap (Grundy value), and that sums of games have Grundy value = XOR of individual values, is one of the cleanest results in combinatorial game theory; fits naturally here alongside the EXPTIME/PSPACE complexity discussion -->
**Key insight**: Shannon's 1950 paper "Programming a Computer for Playing Chess" estimated ~10^120 possible chess games (Shannon number). The branching factor of ~35 and average game length of ~80 means tree search alone is hopeless — you need evaluation functions, which is what all modern engines do. AlphaZero replaced handcrafted evaluation with neural networks.

```
GAME TREE SEARCH TAXONOMY
══════════════════════════

MINIMAX (perfect play baseline):
  Maximize own score, assume opponent minimizes.
  Exponential in depth.

ALPHA-BETA PRUNING:
  Prune branches where opponent would never go.
  Reduces effective branching factor: b^d → b^(d/2)
  Doubles searchable depth at same compute budget.

MCTS (Monte Carlo Tree Search):
  Sample random playouts instead of full evaluation.
  Key in Go before AlphaGo.
  Used in AlphaGo as the search backbone.

NEURAL EVAL + MCTS (AlphaZero style):
  Policy network: predicts good moves (pruning).
  Value network: evaluates positions (no random playouts).
  Self-play generates training data.
  Tabula rasa: no human games used in training.

COUNTERFACTUAL REGRET MINIMIZATION (CFR):
  For imperfect information games (poker).
  Iteratively reduces regret of not playing actions.
  CFR+ converges to Nash equilibrium in 2-player zero-sum.
  Libratus/Pluribus use this + abstraction.
```

---

## Section 6: Cultural Transmission and Social Stratification

Games as social mirrors:

| Game | Social Class Associated | Era | What it Signaled |
|------|------------------------|-----|-----------------|
| Chess | Aristocracy, clergy | Medieval-Renaissance | Intelligence, military strategy |
| Whist → Bridge | Upper middle class | 18th-20th century | Education, patience, partnership |
| Poker | Gamblers, frontier | 19th century → democratized | Risk tolerance, bluff, masculine |
| Snooker | Working class UK | Late 19th-20th century | Pub culture, precision |
| Golf | Upper class | 19th-20th century | Status, networking |
| Video games | Initially teenage boys | 1970s-2000s | Then: universal demographic |
| Esports | Global youth | 2010s-present | Digital skill, reflexes |

The class associations shift over time — chess was once aristocratic, now fully democratized via Lichess/Chess.com (free, 100M+ users). The internet collapsed most class barriers in games by removing geographic and social gatekeeping.

---

## Decision Cheat Sheet

| You want to understand... | Go to... |
|---------------------------|----------|
| Oldest surviving games | 01-ANCIENT-GAMES.md |
| Chess history and evolution | 02-CHESS.md |
| Playing card origins and trick-taking | 03-CARD-GAMES.md |
| Poker history and game theory | 04-POKER.md |
| Billiards, pool, snooker | 05-BILLIARDS-POOL.md |
| Dice, craps, probability origins | 06-DICE-GAMBLING.md |
| Monopoly, wargames, Eurogames, D&D | 07-BOARD-GAMES-MODERN.md |
| Video games from Spacewar! to esports | 08-VIDEO-GAMES.md |
| Nash equilibrium formalism | mathematics/ (game theory) |
| Probability theory foundations | mathematics/ (probability) |
| AI game-playing algorithms | ai-engineering/ |

---

## Common Confusion Points

**"Nash equilibrium = optimal play"**: Not in multi-player games. NE guarantees no unilateral improvement, but coordinated deviations can improve all players' outcomes (cooperative game theory). In poker (2-player), NE is the right solution concept; at a 9-player table, the math is messier.

**"Chess is more complex than Go"**: Chess has more complex rules; Go has vastly larger state space. Chess: ~10^47 legal positions, branching ~35. Go: ~10^170 legal positions, branching ~250. Go was harder for AI precisely because evaluation functions based on material/position heuristics don't work — AlphaGo needed learned value networks.

**"Probability theory caused gambling"**: Causation reversed. Gambling preceded formal probability by millennia. Pascal and Fermat formalized probability *because* gamblers had hard questions about fair division of stakes. Gambling created the demand that mathematics then satisfied.

**"Poker is solved"**: Near-solved in heads-up NLHE (Libratus 2017). 6-player NLHE is "essentially solved" by Pluribus (2019) in the sense that Pluribus beats human pros, but the full game tree is not solved — it uses abstraction. Generalized multi-player poker with arbitrary stack depths is not solved.

**"Zero-sum games have a unique Nash equilibrium"**: Von Neumann's minimax theorem says they have a value (unique in payoffs), but multiple strategy profiles can achieve that value. In chess, many lines may be objectively equal draws at perfect play.

**"Minimax requires full game tree"**: Alpha-beta pruning and forward pruning cut this drastically. AlphaZero's policy network provides even more aggressive pruning — it only explores moves the policy network considers plausible. The full game tree for chess is never built.
