# Ancient Games — From Senet to the Mesoamerican Ball Court

## The Big Picture

```
ANCIENT GAME DISTRIBUTION — 3100 BCE to 600 CE
════════════════════════════════════════════════

EGYPT                    MESOPOTAMIA              INDIA/PERSIA
──────                   ──────────               ────────────
Senet (3100 BCE)         Royal Game of Ur         Pachisi (~500 CE)
Mehen (~3000 BCE)          (2600 BCE)             Chaturanga (~600 CE)
Hounds & Jackals         Liubo analogs            Gyan Chaupar (karma)
  (~2000 BCE)
                         CHINA                    GREECE/ROME
MESOAMERICA              ─────                    ──────────
───────────              Liubo (~200 BCE)         Petteia (strategy)
Ball game (~1400 BCE     Go/Weiqi (~400 BCE       Latrunculi (strategy)
  courts; rubber balls     confirmed)             Tabula (race)
  ~3500 BCE)             Mahjong (much later)     Tesserae (dice)
  Peak: 1500+ courts                              Knucklebones/astragali

AFRICA
──────
Mancala family (earliest boards ~700 CE confirmed,
  but sowing mechanic likely far older)
Bao, Oware, Awele

NORDIC/CELTIC
─────────────
Tafl family (hnefatafl ~400 CE)
Fidchell (Irish)

SHARED MECHANICS ACROSS CULTURES
─────────────────────────────────
  Race games: pieces move along track, luck-determined distance
  Territory/capture: control space, remove opponent pieces
  Sowing: distribute tokens, capture based on count rules
  Betting: risk goods on uncertain outcomes
```

---

## Section 1: Senet — Egypt's Journey Through the Underworld

### What Survives

Senet is the oldest known board game with surviving physical evidence: game boards and pieces found in Pre-dynastic Egyptian tombs (~3100 BCE). Faience (glazed ceramic) game pieces. Elaborate game boxes found in 18th dynasty tombs — Tutankhamun's tomb contained four senet boards.

The **critical problem**: we do not have a rule set from the formative period. All rule reconstructions are scholarly inference from board iconography, hieroglyphic references, and the game's religious context.

```
SENET BOARD — 30 SQUARES (3 × 10 grid)
═══════════════════════════════════════

Direction of movement:
  Row 1: left to right (squares 1-10)
  Row 2: right to left (squares 11-20)
  Row 3: left to right (squares 21-30, exit)

+────┬────┬────┬────┬────┬────┬────┬────┬────┬────+
│ 1  │ 2  │ 3  │ 4  │ 5  │ 6  │ 7  │ 8  │ 9  │10  │
+────┼────┼────┼────┼────┼────┼────┼────┼────┼────+
│ 20 │ 19 │ 18 │ 17 │ 16 │ 15 │ 14 │ 13 │ 12 │11  │
+────┼────┼────┼────┼────┼────┼────┼────┼────┼────+
│ 21 │ 22 │ 23 │ 24 │ 25 │ 26 │ 27 │ 28 │ 29 │30  │
+────┴────┴────┴────┴────┴────┴────┴────┴────┴────+
       ^              ^    ^    ^    ^    ^    ^
      Nfr           Special squares (inferred):
    (beauty)        27 = House of Water (penalty)
     safe           28 = Three Truths
                    29 = Two Truths
                    30 = Sun/Ra (exit to afterlife)

THROW STICKS (4 flat sticks, black one side, white other):
  All white (4 white up):  value = 1
  1 black:                 value = 2
  2 black:                 value = 3
  3 black:                 value = 4
  All black (4 black up):  value = 5
```

### Religious Significance

By the New Kingdom (1550-1070 BCE), senet had acquired profound funerary meaning. Chapter 17 of the *Book of the Dead* depicts the deceased playing senet against an invisible opponent — the game represents the soul's journey through Duat (the underworld). Winning = successful passage to the Field of Reeds (Egyptian paradise). The game became a talismanic object, buried with the dead.

This is a pattern that repeats across cultures: games acquire religious or metaphysical significance, reinforcing their cultural persistence. The Mesoamerican ball game, Indian dice games (Mahabharata's dice game precipitates the Kurukshetra war), Norse tafl — all have cosmological dimensions.

### Probability Analysis

If throw sticks have equal probability p=0.5 of landing black or white (4 sticks), the throw probabilities form a binomial distribution B(4, 0.5):

```
P(k black out of 4) = C(4,k) * (0.5)^4

k=0 (all white = move 1): C(4,0)/16 = 1/16  =  6.25%
k=1 (one black = move 2): C(4,1)/16 = 4/16  = 25.00%
k=2 (two black = move 3): C(4,2)/16 = 6/16  = 37.50%
k=3 (three black = move 4): C(4,3)/16 = 4/16 = 25.00%
k=4 (all black = move 5): C(4,4)/16 = 1/16  =  6.25%

Expected value: E[X] = sum(x * P(x)) = (1+8+18+16+5)/16 = 48/16 = 3

The all-white and all-black throws (values 1 and 5)
are equally rare. The mid-range (3) is most common.
```

---

## Section 2: The Royal Game of Ur — Rules We Actually Have

### Discovery

Sir Leonard Woolley excavated the Royal Cemetery of Ur (Iraq) 1922-1934, finding multiple game boards in the "death pits" — mass burial sites of queens with retinues. The game dates to ~2600-2400 BCE. The boards are inlaid with shell, lapis lazuli, and red limestone — prestige objects for wealthy owners.

```
ROYAL GAME OF UR — BOARD LAYOUT
═════════════════════════════════

  4-square        8-square shared       4-square
  starting zone   playing zone          ending zone
+────+────+────+ +────+────+────+────+────+────+────+────+
|    |    | ✿  | |    |    |    |    |    |    |    |    |
|    | P1 |    | |  <──── P1 moves this direction ────>  |
+────+────+────+ +────+────+────+────+────+────+────+────+
|    |    | ✿  | |    |    | ✿  |    |    |    |    |    |  <- shared
+────+────+────+ +────+────+────+────+────+────+────+────+
|    |    | ✿  | |    |    |    |    |    |    |    |    |
|    | P2 |    | |  <──── P2 moves this direction ────>  |
+────+────+────+ +────+────+────+────+────+────+────+────+

✿ = Rosette squares: safe from capture AND grant extra turn
    (throw again immediately)
Shared zone: opponent pieces on same square are sent off the board
Starting zone: own pieces only (safe)
Goal: be first player to bear off all 7 pieces past the end
```

### The Cuneiform Rulebook

In 1983, Irving Finkel of the British Museum translated cuneiform tablet SM 62193 (~170 BCE, written by Iti-Marduk) — the only surviving ancient rulebook for a board game anywhere in the world. This is a late-period version (2,400 years after the earliest known boards), likely modified from the original, but it gives us:

- Tetrahedral dice with two of four vertices marked (binary outcome per die)
- Four dice thrown simultaneously, value = number of marked vertices landing up
- 7 pieces per player
- Rosette squares grant extra turns
- Shared track has combat (sending opponent pieces back to start)
- Winning condition: bear off all pieces past final rosette

Finkel demonstrated the game live on YouTube in 2017 (vs Tom Scott), generating millions of views and making this the most-watched explanation of a 4,500-year-old game.

### Dice Mathematics

Tetrahedral dice: 2 of 4 vertices marked, so P(marked vertex up) = 2/4 = 0.5.
Four dice thrown simultaneously:

```
Throw value = count of marked vertices landing "up"
P(k) = C(4,k) * (0.5)^4 — identical to senet throw sticks

P(0) = 1/16  =  6.25%   → move 0 (pass/forfeit? unclear)
P(1) = 4/16  = 25.00%   → move 1
P(2) = 6/16  = 37.50%   → move 2
P(3) = 4/16  = 25.00%   → move 3
P(4) = 1/16  =  6.25%   → move 4 (special: land on rosette?)

E[X] = 2.0 (excluding 0 or treating 0 as another value)

This same binomial distribution appears in:
  - Egyptian throw sticks (senet)
  - Mesopotamian tetrahedral dice (Royal Game of Ur)
  - Korean yut sticks (4 flat sticks, still used today)
This is not coincidence — it's a convergent solution to
"generate bounded random integers with simple equipment."
```

---

## Section 3: Go (Weiqi/Baduk/Igo) — Maximum Combinatorial Depth

### Origins and Spread

Go is traditionally dated to 2500+ BCE (Emperor Yao allegedly invented it to educate his unruly son Danzhu), but this attribution is mythological. The earliest reliable historical references place Go in the Spring and Autumn period (~500 BCE). Han dynasty texts (~200 BCE) reference Go as established culture. The game spread eastward:

```
GO TRANSMISSION HISTORY
════════════════════════

~500 BCE:  Go/Weiqi established in China (Spring & Autumn period)
~200 BCE:  Han dynasty writings confirm widespread play
~5th CE:   Introduced to Korea as Baduk (바둑)
~7th CE:   Introduced to Japan as Igo (囲碁)

JAPANESE INSTITUTIONAL DEVELOPMENT:
  Tokugawa shogunate (1603-1868): four official Go houses
    (iemoto) stipended by government:
    - Hon'inbō
    - Yasui
    - Inoue
    - Hayashi
  Players held ranks and competed formally.
  This is the world's first professional game league.

1924: Nihon Ki-in (Japan Go Association) founded.
1958: Korean Baduk Association founded.
1975: Chinese Weiqi Association restructured (post-Cultural Revolution)

MODERN DOMINANCE: China, Korea, Japan — in that order
by recent world championship results.
China and Korea dominate post-2000s; Japanese schools
declined relative to Korean dominance in 1990s-2000s.
```

### Rules and Structure

```
GO BOARD: 19x19 intersections (361 playable points)
══════════════════════════════════════════════════════

Stones placed ON intersections (grid lines cross).
Black plays first.

Basic capture example (liberties):
  ┌─┬─┬─┐     ┌─┬─┬─┐
  │ │B│ │     │ │B│ │
  ├─┼─┼─┤     ├─┼─┼─┤    B = Black stone
  │B│B│ │     │B│B│W│    W = White stone
  ├─┼─┼─┤     ├─┼─┼─┤
  │ │B│ │     │ │B│ │
  └─┴─┴─┘     └─┴─┴─┘
  Group has 4   W fills last liberty = Black group
  liberties     captured and removed from board

SPECIAL RULES:
  Ko: Cannot recreate the immediately previous board position.
      (Prevents infinite capture-recapture loops)
  Suicide: Cannot place a stone with no liberties (self-capture)
           unless it captures opponent group. (Chinese rules allow
           self-capture; Japanese rules forbid it — small
           practical difference)
  Seki: Mutually alive groups sharing liberties — both live,
        neither player removes the other.

SCORING:
  Territory scoring (Japanese): empty points inside your
    territory + captured stones. White gets komi.
  Area scoring (Chinese): stones on board + empty territory.
    Different counting, same game result in most cases.
  Komi (現在): 6.5 points to White (compensates Black's
    first-move advantage). Historically evolved:
    4.5 → 5.5 → 6.5 (determined empirically via statistics
    of professional game outcomes)
```

### Combinatorial Complexity vs Chess

```
CHESS vs GO: SEARCH SPACE COMPARISON
══════════════════════════════════════

                    CHESS              GO (19x19)
Board positions:    ~10^47             ~10^170
Game tree nodes:    ~10^123            ~10^360
Avg branching:      ~35                ~250
Avg game length:    ~80 half-moves     ~300 half-moves
AI achieved
superhuman play:    1997 (Deep Blue)   2016 (AlphaGo)
Approach used:      Alpha-beta +       MCTS + deep
                    evaluation func.   neural networks

WHY GO RESISTED AI LONGER:
  Chess: material count + positional factors = adequate
         evaluation function. 1 queen = 9 pawns.
         Rule-based heuristics work.

  Go: NO useful local heuristic exists. A group that
      appears alive can die 30 moves later based on
      global board state. A "weak" looking position
      may be secretly dominant. Experienced players
      evaluate positions by pattern recognition /
      intuition, not calculation — hence "intuition"
      was the bottleneck for AI.
      MCTS with rollouts helped but couldn't match
      human experts until AlphaGo added value and
      policy networks.
```

### AlphaGo and AlphaZero Significance

AlphaGo (2016) defeated Lee Sedol 4-1 in a globally-watched match. **Move 37** in Game 2 (a shoulder hit on the 5th line) was called by commentators "not a human move" — a placement no professional would seriously consider. Lee Sedol took a break after seeing it. He later said: "I thought AlphaGo was based on probability calculation and that it was merely a machine. But when I saw this move, I changed my mind. Surely AlphaGo is creative."

AlphaZero (2017): trained only against itself with no human game data, learned chess in 4 hours and Go in 8 hours, defeated Stockfish 8 (chess) and AlphaGo (Go). The implications for human Go theory: centuries of established joseki (corner sequences) that humans treated as near-optimal were shown to be suboptimal. AlphaZero preferred different opening patterns entirely.

### Mathematical Connections

- **Combinatorial game theory** (Berlekamp, Conway, Guy, *Winning Ways*, 1982): Go endgames decompose into sums of independent combinatorial games, each with a game value in Conway's {L|R} notation. Cold games (where L < R) have surreal number values and add like ordinary numbers. Hot games — where both players want to move because the position has positive "temperature" — form a broader class. Most active Go endgame positions are hot games; only fully settled positions reduce to surreal numbers. The sum of independent positions is still computed via {L|R} arithmetic, and optimal play means always choosing the highest-temperature position.
- **Temperature**: In CGT, each Go position has a "temperature" (the value of the next move there). As the game progresses, temperature drops. Optimal play: always play the highest-temperature position.
- **Computational hardness**: Determining if a Go position is alive or dead is PSPACE-complete. Generalized n×n Go is EXPTIME-complete.

---

## Section 4: The Mancala Family — Sowing Mechanics

### Geographic Distribution

Mancala is a family of 200+ games, not a single game. The name derives from Arabic *naqala* (to move). Distribution spans Africa, the Middle East, South Asia, Southeast Asia, and the Caribbean (via the slave trade — enslaved Africans brought their games to the New World).

```
MANCALA FAMILY DISTRIBUTION
═════════════════════════════

AFRICA (most diverse):
  West Africa: Oware (Ghana), Awele, Wari
  East Africa: Bao (Tanzania/Kenya — most complex variant)
               Omweso (Uganda)
  North Africa: Mancala/Kalah (simplified)
  Central/South: Various

MIDDLE EAST:
  Mancala variants along trade routes
  Played in Turkey, Syria, Yemen

SOUTH/SOUTHEAST ASIA:
  Congkak (Malay Archipelago — simultaneous sowing!)
  Sungka (Philippines)
  Pallankuzhi (South India — 14 pits)

CARIBBEAN (transplanted):
  Warri/Wari (Antigua, Barbuda — identical to Oware)
  Introduced by enslaved West Africans
```

### The Sowing Mechanic

```
OWARE STARTING POSITION
════════════════════════

Player 2 (top):
     6    5    4    3    2    1    (pit labels)
  +────+────+────+────+────+────+
  │  4 │  4 │  4 │  4 │  4 │  4 │
  +────+────+────+────+────+────+
  +────+────+────+────+────+────+
  │  4 │  4 │  4 │  4 │  4 │  4 │
  +────+────+────+────+────+────+
     1    2    3    4    5    6    (pit labels)
Player 1 (bottom)

SOWING EXAMPLE:
  P1 picks up pit 3 (contains 4 seeds):
  Place 1 seed in pits 4, 5, 6, then P2's pit 6
  (go counterclockwise, skip own store, wrap around)

  Final position of last seed determines capture:
  If last seed lands in OPPONENT's pit containing
  exactly 2 or 3 seeds (making it 3 or 4 total,
  counting the just-placed seed): CAPTURE.
  Back-capture: if the pit before also has 2-3,
  capture that too, continuing backward.

GRAND SLAM (usually forbidden):
  If sowing would capture ALL opponent's seeds,
  instead no capture occurs (opponent must not
  be left with no seeds to play).
```

### Computational Depth of Oware

The 2×6 board with 4 seeds each (48 total) is the standard form. Despite the simple appearance:

- **State space**: approximately 2 × C(48+11, 11) ≈ large but finite
- **Complexity class**: Generalized mancala is PSPACE-hard (proven). Sprague-Grundy theory applies to simplified impartial variants (where both players have the same moves), but standard Oware is partisan (each player sows from their own side), so Grundy analysis does not directly apply — the game falls under the broader Conway {L|R} framework rather than pure Nim equivalence.
- **Optimal play**: Human champions can play near-optimally but not perfectly on a fixed board; computer solvers have largely mapped 2×6 Oware
- **Draw possibility**: Both players can cycle if the opponent has very few seeds — games have maximum move limits to prevent infinite games

**Bao** (East African variant, played on 4×8 board with 128 seeds) is considered by experts to be significantly deeper than chess in practical terms — the combinatorial explosion from 4 rows means no computer has solved it or come close to optimal play.

---

## Section 5: The Mesoamerican Ball Game (Ōllamaliztli)

### Archaeological Record

The Mesoamerican ball game has the oldest known rubber artifacts anywhere: solid and hollow rubber balls from El Manatí (Veracruz, Mexico) dating to ~3500-3000 BCE. These predate the ball courts by over 1,000 years — the balls were initially ritual objects (offerings in sacred springs), not sporting equipment.

**Courts**: Over 1,500 I-shaped ball courts identified archaeologically. Distribution:

```
COURT DISTRIBUTION
══════════════════

Northernmost: Snaketown, Arizona (USA)
Southernmost: Western Nicaragua
Peak density: Classic Maya lowlands, Oaxaca, Veracruz

COURT SIZE RANGE:
  Smallest: ~8m playing alley
  Largest: Chichen Itza Great Ball Court — 168m × 70m
           (with 8m-high walls and 6m-diameter rings
           mounted 8m above the floor)
  Average Classic period: ~40m × 8m playing alley
```

The game spans from ~1400 BCE (earliest confirmed courts) to the Spanish conquest in 1521 CE and beyond — a continuous 3,000-year tradition.

### Court Architecture

```
BALL COURT PLAN VIEW (Classic Maya type)
═════════════════════════════════════════

  ┌───────────────────────────────────────┐
  │           End zone (temple)           │
  └──────────────────────────────────────┘
       |                         |
  ┌────┴─────────────────────────┴────┐
  │ S │                           │ S │
  │ l │                           │ l │
  │ o │      PLAYING ALLEY        │ o │
  │ p │                           │ p │
  │ e │     ──────── ① ────────   │ e │
  │ d │         Vertical ring     │ d │
  │   │         mounted on wall   │   │
  │ W │         (Classic period)  │ W │
  │ a │                           │ a │
  │ l │                           │ l │
  │ l │                           │ l │
  └────┬─────────────────────────┬────┘
       |                         |
  ┌───────────────────────────────────────┐
  │           End zone (temple)           │
  └───────────────────────────────────────┘

Wall slope (talud): balls bounce off sloped walls —
  key playing surface, not just a boundary.
Stone rings (① ): appear ~300-600 CE in Classic period.
  Diameter ~20-30cm clearance. Mounted ~3-8m high
  on side wall. Getting ball through ring = special score
  or instant victory (Spanish sources say instant win).
```

### Rules (Reconstructed)

Rules vary by period, region, and cultural context. Sources: Spanish chronicles (post-conquest), the Popol Vuh (Maya creation epic), codices, and court iconography.

```
AGREED ELEMENTS:
  Ball: solid rubber, ~20-30cm, possibly 1-4 kg weight
  Contact: hips, knees, elbows — NOT hands or feet
  Equipment: stone/wood yoke worn at hips (protective + ball-striking)
             hand/knee/elbow padding of leather
  Team size: typically 2-4 per side
  Scoring: unclear; possibly points for forcing ball out of bounds,
           for ball touching wall/floor in opponent's zone,
           or for getting ball through stone ring
  Ring ball: through the ring = major event (instant win or
             large point award); extremely rare

DEBATED ELEMENTS:
  Sacrifice: yes, attested. Who? Winners? Losers? Captives
             unrelated to game? All three attested in different
             sources and time periods.
  Ball composition: fully solid vs hollow rubber (both found
                    archaeologically at different periods)
  Gambling: extensively attested — spectators and players
            wagered heavily
```

### Cultural and Cosmological Significance

The Maya Popol Vuh (K'iche' Maya creation epic, written down ~1550s from oral tradition):
- The Hero Twins (Hunahpu and Xbalanque) are ballplayers
- They are summoned to Xibalba (underworld) by the death gods
- They play ball games against the lords of Xibalba as a series of ordeals
- The game represents the cycle of the sun and moon, death and rebirth
- The Hero Twins are the ancestors of the Maya people

The ball court is a liminal space — a threshold between the living world and the underworld. This is not metaphor; it is cosmological architecture.

---

## Section 6: Roman Games

### Knucklebones (Astragali)

The universal ancient gambling/game device: ankle bones from sheep or goats (astragali), used for gaming across Mediterranean, Near East, and Asia. Evidence from Egypt, Greece, Rome, Persia, and India.

```
ASTRAGALUS — 4 USABLE SIDES
════════════════════════════

An astragalus has 4 non-symmetric usable sides
(the other 2 sides are rounded and cannot stand):

Side Name       Approximate Frequency
─────────────   ─────────────────────
Concave narrow  ~10%  (Greek: "Venus" = highest value)
  (chion/χίον)
Convex broad    ~40%  (Greek: "dog" = lowest value)
  (kyon/κύων)
Flat side A     ~40%  (middle value)
Flat side B     ~10%  (middle value)

FOUR ASTRAGALI THROWN: best throw = "Venus cast"
= one of each side, very low probability.
Named throws documented in Greek/Roman sources.

CRITICAL POINT: Astragali are NOT fair dice.
The irregular bone shape creates non-uniform
probability distribution. Ancient users did not
recognize this as a statistical problem.
This was implicitly "fine" — rare throws had
prestige, common throws were expected.
```

### Tabula — The Roman Backgammon

Tabula was played across the Roman Empire and is clearly the ancestor of backgammon:

```
TABULA vs MODERN BACKGAMMON
════════════════════════════

Feature              Tabula (Roman)      Backgammon (modern)
───────              ──────────────      ───────────────────
Dice count           3 cubic dice        2 cubic dice
Board points         24                  24
Checkers/player      15                  15
Entry point          Same point for all  Opposite quadrants
Movement direction   Same direction      Opposite directions
Doubling cube        No                  Yes (added ~1920s)
Hitting (capturing)  Yes                 Yes
Bearing off          Yes                 Yes

Emperor Zeno (~480 CE): A specific backgammon-like position
recorded with Zeno's name — the oldest documented specific
game position in history. He was in a terrible situation.
```

### Latrunculi — Roman Strategy Game

Latrunculi ("little soldiers") was widely played in Roman times; Ovid, Varro, Seneca, and others mention it. Rules are **not fully preserved**.

Known features:
- Grid board (multiple sizes found: from 8×8 to 12×8)
- Two players, colored pieces
- Custodian capture (surround a piece on two sides to capture it)
- Dux ("commander") piece with possibly different movement
- Mentioned as a game of skill superior to dice games

The game likely influenced later medieval race and strategy games, but the direct lineage is unclear.

---

## Comparison Table

| Game | Date | Region | Perfect Info | Stochastic | Solved | Complexity |
|------|------|--------|-------------|-----------|--------|------------|
| Senet | 3100 BCE | Egypt | Yes | Yes (sticks) | No (rules unknown) | Low |
| Royal Game of Ur | 2600 BCE | Mesopotamia | Yes | Yes (dice) | Near | Low-medium |
| Oware (Mancala) | ~700 CE confirmed | Africa | Yes | No | Near (2x6) | PSPACE-hard |
| Mesoamerican Ball | ~1400 BCE courts | Americas | Yes | No | N/A | N/A |
| Liubo | ~500 BCE | China | Yes | Yes (die) | No | Low |
| Go (19x19) | ~400 BCE confirmed | E. Asia | Yes | No | No | EXPTIME (general) |
| Latrunculi | ~100 BCE | Rome | Yes | No | No (rules lost) | Unknown |
| Tabula | ~100 CE | Rome | Yes | Yes (dice) | No | Medium |
| Hnefatafl | ~400 CE | Norse | Yes | No | Near | Medium |

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| Oldest game with physical evidence? | Senet, ~3100 BCE Egypt |
| Oldest known written rulebook for any game? | Royal Game of Ur, ~170 BCE cuneiform (Iti-Marduk) |
| Highest combinatorial complexity ancient game? | Go — state space ~10^170, exceeds chess by 123 orders of magnitude |
| Game with most archaeological sites? | Mesoamerican ball game — 1,500+ courts |
| Oldest rubber objects in history? | El Manatí rubber balls, ~3500 BCE (pre-court) |
| Which ancient game is still professionally played? | Go (Baduk/Weiqi/Igo) — active world championship circuit |
| First professional game competition? | Japanese Go houses under Tokugawa shogunate (~1600s) |
| Roman race game closest to modern? | Tabula → direct backgammon ancestor |
| Which ancient game has surviving rules? | Royal Game of Ur (late-period cuneiform); Go (rules unchanged) |

---

## Common Confusion Points

**"Senet rules are known"**: They are not. Multiple scholarly reconstructions exist (Kendall, Crist, Bell) with different interpretations. Rules likely varied by period and region. Tutankhamun's senet board ≠ Pre-dynastic senet.

**"Go is 4,000 years old"**: Traditional attribution; not archaeologically confirmed. Spring and Autumn period (~500 BCE) is the earliest reliable evidence. The 4,000-year figure is cultural mythology — important culturally but not historically verified.

**"The ball game sacrifice — losers were killed"**: Both winners and losers are depicted being sacrificed in different sources. The Maya Hero Twins (Popol Vuh) are ballplayers who are killed and reborn. Some courts show captive warriors (not ballplayers) being sacrificed. The simple "losers die" narrative is modern oversimplification.

**"Mancala is a children's game"**: Oware at tournament level requires deep calculation. Bao (4×8 board) has never been solved computationally. The sowing mechanic enables combinatorial depth that is not obvious from watching casual play.

**"Astragali are fair dice"**: Not at all. Bone shape creates systematic non-uniform probabilities. Ancient users did not identify this as a bias — they simply assigned values to common and rare throws.

**"Go superseded chess in AI difficulty"**: Both were hard in different ways. Chess required breakthrough evaluation; Go required learned intuition. Go's branching factor (~250) vs chess (~35) made brute-force approaches fail faster. AlphaGo's contribution was not greater compute — it was the insight that learned value and policy networks could replace evaluation functions and search pruning.
