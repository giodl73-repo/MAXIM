# Poker — From Riverboats to Game Theory Optimal

## The Big Picture

```
POKER EVOLUTION
════════════════

PRECURSORS                FORMATIVE              STANDARDIZATION
~1480–1830                1830–1900              1900–1970
──────────                ─────────              ──────────────
Primero (Italy/Spain):    Mississippi riverboats  Texas Hold'em
  3 cards, betting,        professional gamblers   invented ~Robstown TX
  partial hand reveal     First documentation:    5-card draw/stud
Poque (France):           J.H. Green, 1834        dominate casinos
  bluffing game,          20-card deck            Standard hand rankings
  vying mechanic          5-card hands            codified
As-Nas (Persia?):         deck grows 52 cards     WSOP founded 1970
  disputed connection     Wild cards introduced
                          Stud variants emerge

BOOM ERA                  GTO ERA                 MODERN
1970–2011                 2011–present            2015–present
──────────                ─────────               ────────────
WSOP expansion            Black Friday 2011:      GTO solvers standard
Hold'em standardizes      DOJ indicts online      (PioSolver, GTO+)
Moneymaker 2003           sites (US)              Pluribus 2019:
Online explosion          Nash equilibrium in     6-player NLHE solved
ESPN coverage             poker studied           Live high-stakes
PokerStars peak           Academic poker          Short-deck (6+) rise
  (2005-2010)             Libratus 2017 HU        Streaming poker
                          NLHE solved             GTO taught as base
```

---

## Section 1: Origins — Disputed and Murky

### The Candidate Ancestors

No single clean lineage for poker exists. Three main candidates:

**Primero** (Spain/Italy, ~1480s-1530s): The earliest confirmed ancestor sharing poker's core DNA. 3-card game. Players received 3 cards, could exchange. Hands had value rankings. Most importantly: **betting with incomplete information** — you bet on your hand without showing it. Vying (raising bets before showdown) was the key mechanic. Documented in Spanish and Italian sources, referenced in English literature (~1530s).

**Poque** (France, ~17th-18th century): French card game with a bluffing/vying mechanic. Name etymology: French *poque* may relate to *pocher* (to poke, bluff). Brought to Louisiana by French colonists. New Orleans was the center of French card-game culture in North America. The evolution Poque → Poker is phonetically natural and geographically plausible.

**As-Nas** (Persia): A Persian card game with hand rankings and betting. Some scholars (including Jonathan Green) claimed it was poker's direct ancestor via Persian sailors. This is disputed. The structural similarities may reflect parallel development of betting games rather than direct transmission. Consensus among card game historians: As-Nas connection is unproven and possibly spurious.

```
WHAT ALL PRECURSORS SHARE:
  - Private cards (players don't see each other's hands)
  - Betting rounds
  - Hand rankings (some combinations beat others)
  - Bluffing/vying: you can bet without having the best hand

WHAT MODERN POKER ADDED:
  - Community cards (Hold'em variants)
  - Multiple betting rounds
  - No-limit betting structure
  - Tournament format
  - Sophisticated game theory
```

### Jonathan H. Green and the Mississippi River (1830s-1860s)

The earliest direct documentary evidence: Jonathan H. Green, a reformed gambler, wrote "An Exposure of the Arts and Miseries of Gambling" (1843). He documented seeing the game played on Mississippi riverboats in the early 1830s:

- 20-card deck (A,K,Q,J,10 in each suit)
- 4 players, 5 cards each (exactly 20 cards)
- Bet on your 5-card hand — no draw, no community cards
- Hands: 4-of-a-kind, full house, 3-of-a-kind, pairs

Green called it the "cheating game" — implying it had a reputation for being exploited by professionals cheating unsophisticated gamblers.

```
MISSISSIPPI RIVERBOAT CONTEXT
═══════════════════════════════

Professional gamblers traveled the river routes between
New Orleans, Natchez, Memphis, and St. Louis.
River travel was slow (days per trip) — captive audience.

PROFESSIONAL GAMBLING TECHNIQUES DOCUMENTED:
  Marked cards: scratched/bent corner systems
  Cold deck: substituting pre-arranged deck for the deck in play
  Holdout devices: mechanical sleeve devices holding back aces
  Collusion: telegraph signals between confederates
  Base dealing: dealing second card from top (keeping top card)
  Stripping the deck: removing cards imperceptibly

Jonathan H. Green's book was partly a public warning:
  "Professionals on the boats are experts at every form
  of cheating. The unwary traveler is almost certainly
  being cheated if a stranger offers to play cards."

Despite (or because of) this reputation, poker spread
from river towns to the frontier — California gold rush
(1848), Civil War soldiers, wild west territories.
```

---

## Section 2: Texas Hold'em — Dominant Modern Form

### The Texas Origin Story

```
TEXAS HOLD'EM TIMELINE
════════════════════════

~early 1900s: Game invented in Robstown, Texas (near Corpus Christi).
              Texas Legislature officially recognized Robstown
              as origin in 2007 (ceremonial; no historical records).

~1925-1960: Played in Texas card rooms and illegal casinos.
             Traveling gamblers spread it northward.

~1963-1967: Spread to Las Vegas by a group of Texas gamblers
            including Crandall Addington, Doyle Brunson,
            Amarillo Slim Preston, Puggy Pearson.

1967: First Las Vegas Texas Hold'em game at the Golden Nugget,
      then at the Dunes, then at Binion's Horseshoe.

1970: Benny Binion opens the World Series of Poker at
      Binion's Horseshoe. First champion: Johnny Moss
      (selected by vote of players, not tournament format).

1971: First WSOP with elimination tournament format.

HOLD'EM vs 5-CARD STUD (why Hold'em won):
  5-card stud: 1 hole card, 4 face-up cards.
    Near-perfect information by the end.
    Bluffing very limited.
    Skill ceiling: lower.

  Texas Hold'em: 2 hole cards, 5 community cards.
    Multiple betting rounds with imperfect information
    (hole cards unknown throughout).
    Significant bluffing range.
    Skill expression: deep (hand reading, range analysis,
    bet sizing, position exploitation).
```

### Hold'em Structure

```
TEXAS HOLD'EM ANATOMY
══════════════════════

SETUP:
  2-10 players. Standard 52-card deck.
  Dealer button rotates clockwise each hand.
  Small blind (left of button): forced bet (half big blind)
  Big blind (2 left of button): forced bet (1 unit)

STREETS (betting rounds):
  PREFLOP:
    Each player receives 2 private hole cards.
    Action starts left of big blind.
    Options: fold, call (match big blind), raise.
    Action continues until all active players even.

  FLOP:
    3 community cards dealt face-up.
    Action starts left of dealer.
    Options: check (no bet), bet, fold, call, raise.

  TURN:
    1 community card added (4 total).
    Same action structure.

  RIVER:
    1 final community card (5 total).
    Final betting round.
    Showdown: if multiple players remain, best 5-card hand
    using any combination of 2 hole + 5 community wins.

BETTING STRUCTURES:
  Limit: fixed bet sizes (2-4 Limit, 4-8 Limit, etc.)
  Pot-Limit: max bet = current pot size
  No-Limit: any bet up to all chips in front of you
    ("No-Limit" changed the game fundamentally — can
    bet enough to make calling mathematically incorrect
    even with the best hand)
```

### Position — The Most Important Non-Card Factor

```
POSITION SIGNIFICANCE
══════════════════════

TABLE POSITIONS (6-handed):
  UTG (Under the Gun): worst position — acts first preflop
  HJ (Hijack): 2nd from dealer
  CO (Cutoff): 1 right of dealer
  BTN (Button/Dealer): BEST position — acts last postflop
  SB (Small Blind): forced bet, acts second-to-last postflop
  BB (Big Blind): forced bet, acts last preflop, early postflop

WHY POSITION MATTERS:
  Acting LAST means you have MORE INFORMATION when deciding.
  You see what all opponents do before committing chips.

  Button vs UTG win rates at same skill level:
    Approximately 3-5 bb/100 hands difference in EV.
    This is enormous — professional edges are <1 bb/100.

POSITIONAL ADVANTAGE IN PRACTICE:
  From button: wider range of hands playable
               can profitably play suited connectors, pairs, etc.
  From UTG: only strongest hands worth playing
            (AA, KK, QQ, AK, AQs, JJ, etc. in most formats)

  "Position is king" — agreed across all poker formats.
  A weaker hand in position often beats a stronger hand
  out of position because the positional player gains
  information advantage in every postflop decision.
```

---

## Section 3: The Poker Boom — Moneymaker Effect

### WSOP Before the Boom (1970–2002)

The World Series of Poker grew slowly but was always significant in the poker world:

```
WSOP GROWTH PRE-BOOM
═════════════════════

Year  Main Event Entries  First Prize
────  ──────────────────  ──────────
1970  ~6 (invitational)   $30,000 (first was gift)
1971  6                   $30,000
1973  13                  $130,000
1980  73                  $365,000
1989  178                 $755,000 (Phil Hellmuth wins,
                                    youngest ME champion)
1995  273                 $1,000,000 (Dan Harrington wins)
2000  512                 $1,500,000 (Chris Ferguson wins)
2002  631                 $2,000,000 (Robert Varkonyi wins)

BEFORE 2003: WSOP is poker's championship, but niche.
  No TV deals (ESPN shows tape-delayed). Small prize pool.
  Professional poker players are 500-1,000 worldwide.
```

### The Moneymaker Effect (2003–2011)

```
2003: THE YEAR POKER CHANGED
══════════════════════════════

CHRIS MONEYMAKER:
  27-year-old accountant from Tennessee.
  Entered a $39 online satellite tournament on PokerStars.
  Won entry to the WSOP Main Event (value: $10,000).
  Had never played live poker in a major tournament.
  His name: MONEYMAKER. (Real surname, not a nickname.)

2003 WSOP MAIN EVENT:
  839 entrants (massive for the time).
  Moneymaker defeats Sammy Farha heads-up.
  Key moment: Moneymaker bluffs Farha off a flush
  with a stone bluff (air). Farha folds. ESPN shows
  the hole cards — Moneymaker had nothing.
  Prize: $2,500,000.

ESPN COVERAGE:
  Hole card cameras (introduced ~2002) made it possible
  to show viewers what players were actually holding.
  The drama of Moneymaker's bluffs and hero calls became
  genuinely cinematic. Millions watched.

WHAT HAPPENED NEXT:
  2003: PokerStars, PartyPoker user registrations spike 200%
  2004: WSOP Main Event entries: 2,576 (3x increase in 1 year)
  2005: WSOP Main Event: 5,619 entrants
  2006: WSOP Main Event: 8,773 entrants (all-time record)
        First prize: $12,000,000 (Jamie Gold wins)

Online poker peak:
  PokerStars: millions of players, billions in deposits
  PartyPoker: briefly largest poker site, pre-UIGEA
  2006: Unlawful Internet Gambling Enforcement Act (UIGEA)
        signed into law (as rider to port security bill).
        PartyPoker exits US market. PokerStars stays.

BLACK FRIDAY (April 15, 2011):
  DOJ indicts PokerStars, Full Tilt Poker, Absolute Poker
  on charges of bank fraud, money laundering, violating UIGEA.
  Player funds frozen. Full Tilt cannot pay players (~$390M).
  PokerStars acquires Full Tilt (2012), eventually returns
  player funds globally. PokerStars eventually sells to Amaya
  Gaming (~2014) and becomes licensed in multiple jurisdictions.
  US online poker severely disrupted. State-by-state licensing
  begins (New Jersey, Nevada, Delaware).
```

---

## Section 4: Game Theory in Poker

This is where poker intersects directly with the mathematics you know from MIT. Poker is a stochastic, imperfect-information zero-sum game. The formal game theory treatment is substantive.

### Nash Equilibrium in Poker

```
NASH EQUILIBRIUM IN HEADS-UP NLHE
═══════════════════════════════════

Poker (2-player) is a finite, extensive-form game with
imperfect information.

Nash's existence theorem guarantees a Nash equilibrium
exists in mixed strategies.

In heads-up (2-player) zero-sum games:
  NE = minimax strategy = unexploitable strategy
  (by the minimax theorem for zero-sum games)

At NE: you cannot be exploited by ANY opponent strategy.
  If you play NE, your EV = game value regardless of opponent.
  Opponent playing NE cannot improve by deviating.

BUT: NE in poker doesn't mean maximizing EV against a specific
  opponent. Against a weak opponent who always calls:
    NE strategy: balanced bluffing and value
    Exploitative strategy: value bet only (never bluff)
    Exploitative EV > NE EV against this opponent.
    But exploitative strategy is exploitable by an optimal
    opponent who knows you never bluff.

The tradeoff:
  NE (GTO): can't be exploited, may leave EV on table
  Exploitative play: maximizes EV vs specific weakness,
    but is exploitable if that weakness is corrected.
```

### GTO (Game Theory Optimal) in Practice

```
MODERN GTO UNDERSTANDING
═════════════════════════

What GTO means in poker:
  Playing a strategy such that the opponent cannot
  profitably deviate, regardless of what they do.

KEY INSIGHT: GTO doesn't mean "optimal for all opponents."
  It means "unexploitable." These are different.
  Against a fish (weak player), GTO EV < exploitative EV.
  Against a good player who adjusts, GTO is correct.

Mixed strategies in GTO poker:
  A pure strategy (always/never do X) is exploitable.
  Must mix between actions at certain frequencies.

  Example: river bet with a strong hand = value bet.
           river check-raise with a strong hand = bluff catch.
           If you ALWAYS value bet strong hands, opponent
           folds all bluff catchers → you win less.
           Need to sometimes check strong hands to protect
           your checking range (otherwise opponent bluffs
           your checks profitably forever).

BALANCED RANGES:
  In GTO, your ranges at each decision point must be
  balanced — both value hands and bluffs in appropriate
  proportions.

  River value:bluff ratio ≈ determined by pot odds:
    If you bet pot: opponent needs 33% equity to call.
    You need: 2 value bets for every 1 bluff.
    (If opponent always calls: bluff EV = 0 at this ratio)
    (If opponent always folds: all bets profit)
    Mixed strategy bluffing makes opponent indifferent.
```

### Pot Odds and Expected Value

```
FUNDAMENTAL POKER MATH
════════════════════════

POT ODDS:
  The ratio of the current pot to the cost of a call.
  Pot = $100, opponent bets $50, call costs $50.
  You're calling $50 to win $150 (pot + bet) = 3:1
  (note: you win $100 profit + your $50 back on stack)
  Actually: $50 to win $150 total = 33% required equity.

  Required equity to call = call_size / (pot + call_size)
  $50 / ($100 + $50 + $50) = $50/$200 = 25% to call
  (where pot = $100, villain_bet = $50, your_call = $50)

EQUITY:
  Your probability of winning the hand if run to showdown.
  A + K flush draw on the flop vs. pair = ~35% equity.
  AK preflop vs. JJ = ~46% equity (slightly behind).

EXPECTED VALUE:
  EV = (Prob win × Win amount) - (Prob lose × Loss amount)

  Example: pot = $100, opponent bets $50, you're 40% to win:
    EV(call) = 0.40 × ($100 + $50) - 0.60 × $50
             = 0.40 × $150 - 0.60 × $50
             = $60 - $30 = +$30
    Calling is +EV.

IMPLIED ODDS:
  Future bets you expect to win if you make your hand.
  A flush draw might be -EV to call the flop bet in isolation,
  but if you'll win opponent's entire stack when you hit (+EV
  including implied odds), calling is correct.
  Implied odds = how much more money you expect to win.
```

### Counterfactual Regret Minimization (CFR)

The algorithm that cracked poker. This is the AI equivalent of AlphaZero for chess, but for imperfect-information games.

```
CFR IN POKER
═════════════

MOTIVATION:
  Minimax (alpha-beta) doesn't apply to imperfect-info games.
  You can't just evaluate positions because positions include
  private information (hole cards = information sets contain
  multiple game states).

INFORMATION SETS:
  At any decision point, the acting player has an
  "information set" = all game histories consistent with
  what they've observed (their hole cards + all public info).
  Multiple game histories can be in the same info set.

REGRET:
  Counterfactual regret for action a at information set I:
  How much better would I have done IF I had always
  played action a at this information set in the past?

CFR ALGORITHM (simplified):
  For each information set, maintain:
    - Strategy: probability distribution over actions
    - Regret accumulator for each action

  Each iteration:
  1. Traverse game tree, compute counterfactual values
     (what value do I get reaching this node and playing
     this action, assuming all other nodes play current strategy)
  2. Update regrets: regret[a] += CF_value[a] - avg_CF_value
  3. Update strategy: play actions proportional to positive regret
     (Regret Matching)

  After T iterations:
    Average strategy converges to Nash equilibrium
    in 2-player zero-sum games at rate O(1/sqrt(T))

LIBRATUS (Carnegie Mellon, 2017):
  First AI to defeat professional heads-up NLHE players.
  4 players × 20 days × 120,000 hands.
  Defeated top HU specialists by 14.7 bb/100 on average.
  Used CFR+ (variant) with game abstraction.

PLURIBUS (2019):
  Extended to 6-player NLHE (multi-player makes NE harder).
  Multi-player poker is NOT zero-sum → minimax inapplicable.
  Pluribus uses a Nash-like solution for 6-player.
  Defeated professional players in 6-handed play.
  Most significant AI milestone for multi-player incomplete-
  information games.
<!-- @editor[content/P2]: The "Nash-like solution" phrasing understates what Pluribus actually uses — Pluribus computes a "blueprint" strategy for the full game using a variant of MCCFR (Monte Carlo CFR), then uses real-time search (depth-limited solving) during actual play; the key technical insight is that in >2-player games there is no minimax theorem guaranteeing a unique value, so Pluribus targets a strategy that is unexploitable in a looser sense; this is a meaningful distinction for a TCS reader -->
<!-- @editor[content/P2]: The convergence rate of CFR (O(1/√T)) is stated above but the improvement to CFR+ (linear convergence in practice, Tammelin 2014) is missing — CFR+ is what Libratus and modern solvers actually use, and it converges much faster in practice -->
```

---

## Section 5: Tournament Structure and Variance

### Tournament vs Cash Game

```
CASH GAMES vs TOURNAMENTS
══════════════════════════

CASH GAMES:
  Chips = real money (1 chip = $1 or fixed denomination).
  Buy in for fixed amount, can rebuy or leave anytime.
  EV is simple: win rate in $ per hour or bb/100 hands.
  Skill translates directly to $/hour income.

TOURNAMENTS:
  Buy in = fixed entry fee. Get chips (no cash value).
  Elimination: lose all chips, you're out.
  Prize pool: top X% of field paid, usually top 15%.
  Standard payout: 1st ~30%, gradual diminution.

  ICM (Independent Chip Model):
    Converts chip counts to prize equity.
    A chip leader with 50% of chips does NOT have 50%
    of prize equity — because of the nonlinear payout.
    ICM adjusts all decisions near the money bubble
    and at final table.

BLIND STRUCTURE:
  Blinds double approximately every 15-60 minutes.
  This forces action — you can't wait forever for
  premium hands.
  "M" (Dan Harrington): ratio of stack to total blinds+antes.
  M = stack / (SB + BB + antes)
  M > 20: green zone (full poker flexibility)
  M 10-20: yellow zone (must be selective)
  M 5-10: orange zone (push/fold territory)
  M < 5: red zone (push any ace, any pair)
```

### Bankroll Management and Variance

```
VARIANCE IN POKER
══════════════════

Standard deviation in NLHE cash: approximately 100 bb/100 hands
(100 big blinds per 100 hands is a typical standard deviation)

A winning player with +5 bb/100 edge:
  E[winnings] = 5 bb per 100 hands
  Std dev      = 100 bb per 100 hands
  95% CI over 10,000 hands: ±200 bb total

  Downswings of 200-300 bb (20-30 buy-ins) are NOT uncommon
  for winning players. This is not bad luck — it's expected.

REQUIRED BANKROLL:
  Conventional wisdom: 20 buy-ins minimum for cash games
  (gives ~95% confidence of not going broke before
  statistical edge manifests over large sample)
  Tournament players: 100+ buy-ins (higher variance)

KELLY CRITERION (from finance, directly applicable):
  Optimal fraction of bankroll to risk per bet:
  f* = (bp - q) / b
  where p = win probability, q = 1-p, b = odds received
  Maximizes long-term geometric growth rate.
  Full Kelly has high variance; Half-Kelly often used.
```

---

## Section 6: Notable Players and Cultural History

### The Legends

```
POKER LEGENDS
═════════════

DOYLE BRUNSON ("Texas Dolly"):
  2× WSOP Main Event champion (1976, 1977).
  Both times won with 10-2 offsuit (now "Doyle Brunson hand").
  "Super System" (1979): first comprehensive poker strategy
  book. Revolutionary — gave away professional secrets.
  Considered the bible of poker for decades.
  Phil Hellmuth's mentor. Died 2023 at 89.

PHIL HELLMUTH:
  17 WSOP bracelets (most in history).
  1989 World Champion (age 24, youngest at the time).
  Known for extreme emotional reactions to bad beats.
  His nickname, "Poker Brat," is self-aware.
  Despite personality, legitimate claim to GOAT status
  in live tournament poker. Consistently results at WSOP.

STU UNGAR:
  Three-time WSOP Main Event champion (1980, 1981, 1997).
  Considered by many the greatest natural poker talent ever.
  Also was possibly the best gin rummy player alive.
  Drug addiction, bankruptcy, won 1997 Main Event nearly
  penniless (staked by someone who believed in him).
  Died 1998 at 45, impoverished. The tragedy of genius.

PHIL IVEY:
  "The Tiger Woods of poker." 10 WSOP bracelets.
  Considered the best all-around poker player.
  Baccarat edge-sorting dispute (~$20M won, then sued
  by casinos — courts ruled he must repay Crockfords £7.7M).

DANIEL NEGREANU:
  "Kid Poker." 6 WSOP bracelets, 2 WPT titles.
  Two WSOP Player of the Year awards.
  Famous for live hand-reading and table talk.
  GTO vs exploitative debate: Negreanu publicly skeptical
  of pure GTO, advocates exploitative reads.
  Bet on himself vs Doug Polk in 25,000-hand challenge
  (2020-2021). Lost by ~$1.2M.

VANESSA SELBST:
  3 WSOP bracelets. Highest-earning female poker player.
  Yale Law degree. Argued poker should be a sport.
  Retired from professional poker to focus on data science
  and socially responsible investing.
```

### Poker Variants Reference

```
MAJOR POKER VARIANTS
═════════════════════

VARIANT            CARDS              NOTES
───────            ─────              ─────
Texas Hold'em      2 hole + 5 comm.   Dominant worldwide
Omaha Hi           4 hole + 5 comm.   Must use exactly 2 hole
                   (use exactly 2)    Higher-variance than HE
Omaha Hi-Lo        4 hole + 5 comm.   Split pot: best high AND best low
                                      (qualifying low: 8 or better)
7-Card Stud        7 cards, 4 up      Pre-Hold'em dominant game
7-Stud Hi-Lo       7 cards, split     Split pot variant
Razz               7 cards            Lowest hand wins (A=low)
2-7 Triple Draw    5 cards, 3 draws   Lowest unpaired hand wins
Badugi             4 cards, 3 draws   4-suit lowest unique hand
HORSE              5-game rotation    H=HE, O=Omaha, R=Razz, S=Stud,
                                      E=Stud Hi-Lo 8-or-better
Short Deck (6+)    52-card minus      2-5 removed; flush > full house
                   2-5 (36 cards)     Popular in Asia, growing globally
```

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| When was poker first documented? | Jonathan H. Green, 1843, Mississippi riverboats (~1830s) |
| Why did Texas Hold'em win? | 2 hole cards maintain more imperfect information longer; more skill expression |
| Who sparked the poker boom? | Chris Moneymaker, 2003 WSOP — online qualifier wins $2.5M |
| What is Black Friday in poker? | April 15, 2011 — DOJ indicted PokerStars, Full Tilt, Absolute Poker |
| What is GTO? | Game Theory Optimal — unexploitable strategy (Nash equilibrium in poker) |
| What is CFR? | Counterfactual Regret Minimization — algorithm that converges to NE in poker |
| When was HU NLHE "solved"? | Libratus 2017 (Carnegie Mellon) beat top human pros |
| When was 6-max poker solved? | Pluribus 2019 (Carnegie Mellon/Facebook) beat pros in 6-max |
| Basic pot odds formula | Required equity = call_size / (pot + call_size) |
| Kelly Criterion in poker | f* = (bp - q) / b — maximize long-run geometric growth |

---

## Common Confusion Points

**"GTO play is always best"**: GTO is unexploitable. Against weak players who make systematic errors, exploitative play captures more EV. GTO is a baseline; exploiting deviations from GTO is where the money is made in practice.

**"Poker is mostly luck"**: Over a single session, variance dominates. Over 10,000+ hands (a few months of regular play), skill is the deterministic factor. Professional players maintain edges of 5-10 bb/100 over large samples, which translates to consistent income. The legal question (is poker gambling?) hinges on this distinction.

**"Libratus/Pluribus means poker is solved"**: Heads-up NLHE with infinite stakes is not fully solved (the game tree is astronomical). Libratus used abstraction (simplifying the game before solving) and won in practice. The abstract game is solved; the unabstracted infinite-stack game is not. Pluribus solved 6-max with its own nuanced definition of "solved."

**"The best hand preflop always wins"**: In NL Hold'em, hand equity is not deterministic. Pocket aces are ~80% to win against pocket kings — not a guarantee. Bad beats are inevitable and the math says they happen frequently.

**"Bluffing is the key skill in poker"**: At high levels, bluffing is mechanical (determined by balanced range construction, not instinct). The deeper skills are: range construction, bet sizing, reading population tendencies, ICM adjustment, exploiting specific player patterns. A player who never bluffs but has excellent fundamentals can beat a player who bluffs well but has poor fundamentals.

**"Online poker is rigged"**: Major licensed sites (PokerStars, GGPoker, etc.) use certified RNG systems audited by independent firms. Rigging would destroy the business. Offshore unlicensed sites are a different matter.
