# Chess — From Chaturanga to AlphaZero

## The Big Picture

```
CHESS EVOLUTION: 600 CE to Present
════════════════════════════════════

CHATURANGA         SHATRANJ            EUROPEAN CHESS      MODERN CHESS
(India, ~600 CE)   (Persia, ~700 CE)   (1475 CE)           (1886–present)
──────────────     ───────────────     ──────────────      ─────────────
4-player game      2-player            Queen replaces      Standardized rules
Dice used          No dice             firz (unlimited)    FIDE 1924
Rajas, elephants,  Fil (2-diag leap)   Bishop replaces     Elo rating 1960
horses, chariots   Firz (1-diag only)  fil (long diag)     Computer era 1997
                   Shahmat = checkmate  Game tempo 2×       AI dominance 2006+

CHESS ERAS (analogous to programming language generations)
═══════════════════════════════════════════════════════════

ROMANTIC          POSITIONAL         HYPERMODERN        SOVIET            COMPUTER
1800–1886         1886–1920s         1920s–1940s        1945–1990s        1997–present
──────────        ──────────         ──────────         ──────────        ──────────
Attack, sac.      Prophylaxis,       Control center     Systematic        Engine prep,
Aesthetics.       weak squares,      with pieces,       training,         opening theory
Morphy,           pawn structure.    not pawns.         schools,          explosion,
Anderssen.        Steinitz.          Nimzovich.         Botvinnik.        tablebases.

WORLD CHAMPIONS (select):
  1886: Steinitz (first official champion)
  1894–1921: Lasker (27 years — record reign)
  1927: Capablanca (positional purity)
  1927–1946: Alekhine (combinational genius)
  1948–1963: Botvinnik (Soviet system founder)
  1972: Fischer (Cold War match, 12.5 vs 12.5 vs Spassky)
  1985–2000: Kasparov (peak 2851 Elo, lost to Deep Blue 1997)
  2013–present: Carlsen (peak 2882 Elo, world record)
```

---

## Section 1: Origins — Chaturanga to Shatranj

### Chaturanga (India, ~600 CE)

Chaturanga (Sanskrit: "four-armed," referring to the four divisions of the Indian army) appears in the Gupta Empire period (~600 CE), though some researchers argue for origins 200+ years earlier. The Harshacharita (~625 CE) is among the earliest textual references.

```
CHATURANGA ARMY MAP TO CHESS PIECES
══════════════════════════════════════

Sanskrit      Military unit       Modern chess piece
─────────     ─────────────       ──────────────────
Raja          King (elephant)     King
Mantri        Counsellor          Queen (originally)
Hasti         War elephant        Bishop
Ashva         Horse               Knight
Ratha         Chariot             Rook
Padati        Foot soldier        Pawn

Two key variants:
1. Four-player chaturanga (4 kings, dice determine which
   piece moves) — original?
2. Two-player abstract version (no dice) — what transmitted
   to Persia
```

The dice version is thought to be earlier (gambling tradition); the two-player version represents abstraction — removing randomness to create a pure strategy game. This is a historically rare transformation: games almost never remove randomness, as chance maintains player engagement for weaker players.

### Shatranj (Persia, ~700 CE)

When the Sassanid Empire (Persia) absorbed the game from India in the 6th-7th centuries CE, it became Shatranj (from Sanskrit "chaturanga" via sound change). The Islamic conquest of Persia spread Shatranj across the entire Arab world by the 9th century.

```
SHATRANJ PIECE MOVEMENTS (key differences from modern chess)
═════════════════════════════════════════════════════════════

Piece     Shatranj movement         Modern chess
──────    ─────────────────         ─────────────
Firz      1 square diagonally       Queen: unlimited any direction
  (Queen  only (very weak)          (strongest piece)
  origin)
Fil       Jumps exactly 2 squares   Bishop: unlimited diagonal
  (Bishop diagonally (skips over    (long-range piece)
  origin) intervening square)
Shah      Same as modern king       King (identical)
Faras     Same as modern knight     Knight (identical)
Rukh      Same as modern rook       Rook (identical)
Baidaq    1 forward, no initial     Pawn (mostly same, no
          2-square move; promotes   double initial move,
          to firz ONLY             promotes to firz only)

SHATRANJ GAMEPLAY IMPLICATIONS:
  No queen = no powerhouse piece. Positional maneuvering.
  Game typically 70-120 moves long (much slower than modern).
  No castling. No en passant.
  Win conditions: checkmate OR stalemate (both count as wins).
  "Bare king" (capturing all opponent's pieces) = win.
```

Notable Shatranj players: Al-Adli (~800 CE) wrote the first known Shatranj book. Al-Razi followed. These players were the first documented chess professionals, patronized by caliphs.

The Chatrang-namak (~600 CE) — a Pahlavi text — narrates the story of chess being brought from India to Persia as a puzzle for the Shah to solve, and the Persian invention of Nard (backgammon) sent back to India as a counter-puzzle. This mythological exchange captures the real cultural transmission.

---

## Section 2: The 1475 Revolution — Modern Chess Born

### The Changes

Around 1475, European players — particularly in Spain and Italy — modified Shatranj in ways that transformed the game fundamentally. This was not gradual evolution; it was a rapid rule change in the late 15th century.

```
THE TWO CRITICAL CHANGES
════════════════════════

CHANGE 1: FERZ/FIRZ → QUEEN
  Before: Ferz (from Shatranj firz = counsellor) moved
          one square diagonally. Very weak.
  After: Queen can move ANY number of squares in ANY
         direction (combines rook + bishop movement).
         Becomes most powerful piece.

  Impact: Tactical threats suddenly appear from across
          the board. Tempo of game roughly doubles.
          Sacrificial attacks become possible because
          queen can generate threats quickly.

CHANGE 2: FIL → BISHOP
  Before: Fil (elephant) jumped exactly 2 squares
          diagonally — strange, limited range.
  After: Bishop moves unlimited distance diagonally.
         Stays on one color but has long-range influence.

  Impact: Bishops become major tactical pieces. Color
          weakness (having wrong bishop for endgame)
          becomes strategically important.

MINOR CHANGES ALSO ADDED:
  - Pawn double-advance on first move
  - En passant rule (consequence of double-advance)
  - Castling (king + rook swap for king safety)
  - Stalemate = draw (was a win in Shatranj)
  - Pawn promotes to any piece (not just queen/ferz)
```

### First Documented Masters

```
EARLY MODERN CHESS MASTERS
════════════════════════════

1497: Ruy López's contemporary Luis Ramírez de Lucena
      "Repetición de Amores y Arte de Ajedrez" — first
      surviving printed chess book with new queen rules.
      Describes 11 chess openings, 150 problems.
      "Lucena position" (rook endgame winning technique)
      named after him, though not originating here.

1561: Ruy López de Segura, "Libro de la Invención Liberal
      y Arte del Juego del Ajedrez" — describes the Ruy
      López Opening (1.e4 e5 2.Nf3 Nc6 3.Bb5), still
      one of the most theoretically rich openings.
      First systematic opening theory.

~1600s: Italian school (Greco, Gioacchino) vs Spanish school.
        "Giuoco Piano" (quiet game) vs Ruy López.
        These names persist in modern theory today.
```

---

## Section 3: Chess Eras — Paradigm Shifts in Understanding

Treating chess eras like software paradigm shifts works well: each era represents a new mental model of the game, not just stylistic preference.

### Era 1: Romantic Chess (1800s–1886)

The Romantic era valued combinatorial brilliance: spectacular sacrifices, aggressive attacks, the "brilliancy prize" game. King safety was secondary to the initiative. The best players were expected to be attackers.

```
ROMANTIC ERA HALLMARKS
═══════════════════════

PAUL MORPHY (1837-1884, USA):
  - Considered the strongest player of his era at age 20
  - Defeated all European masters in 1857-1858 tour
  - Played fast, aggressive combinations
  - Returned to New Orleans, refused further chess play
  - Died at 47, reclusive — tragic genius archetype

ADOLF ANDERSSEN (Germany):
  - Immortal Game (1851, vs Kieseritzky):
    Sacrificed BOTH rooks and the queen, then won
    by checkmate with only minor pieces remaining.
  - Evergreen Game (1852): another famous sacrifice game.
  - These games are still shown to beginners as art.

THE AESTHETIC STANDARD:
  A game where you sacrifice material for a forced mate
  = beautiful. Material advantage = less interesting.
  "The best move is sometimes not the most beautiful."
```

### Era 2: Classical/Positional Chess (1886–1920s)

Wilhelm Steinitz became the first official World Champion in 1886 by defeating Johannes Zukertort. More importantly, Steinitz had developed a *theory* of chess:

```
STEINITZ'S PRINCIPLES (chess theory's foundation)
═══════════════════════════════════════════════════

The position has a VALUE independent of tactical tricks.
A player should only attack when they have an advantage.
Advantages are:
  1. STATIC: better pawn structure, more space, better
             bishop vs bad knight (or vice versa)
  2. DYNAMIC: lead in development, king safety differential

ACCUMULATION OF SMALL ADVANTAGES:
  You don't need a brilliancy. Win a pawn, trade to an
  endgame, convert the material advantage. This is the
  positional approach.

KEY CONCEPTS INTRODUCED/FORMALIZED:
  Prophylaxis: prevent opponent's plans before attacking
  Outpost: knight on advanced square that cannot be
           attacked by pawns (e.g., d5 with no c/e pawns)
  Open file: control with rooks
  Weak squares: squares no longer defended by pawns
  Pawn structure: doubled pawns (weak), isolated pawn
                  (weak but active), passed pawn (strength)
  King centralization in the endgame: king is active piece
```

Steinitz's student Emanuel Lasker held the title 27 years (1894–1921) — the longest reign ever. Lasker was a mathematician (PhD from Erlangen, proved Lasker's theorem in algebra) who treated chess as a psychological battle as much as a technical one.

José Raúl Capablanca (Cuba, champion 1921-1927) exemplified positional clarity to the extreme — effortless simplicity, the "chess machine." He lost only 34 games in his career.

### Era 3: Hypermodern Revolution (1920s–1940s)

```
HYPERMODERN CHALLENGE TO CLASSICAL THEORY
═══════════════════════════════════════════

CLASSICAL TEACHING:
  "Occupy the center with pawns (e4+d4)."
  A strong pawn center controls space and restricts
  opponent's pieces.

HYPERMODERN CHALLENGE (Nimzovich, Réti, Grünfeld):
  "Let the opponent build a pawn center — then attack it."
  Pieces (bishops, knights) can control the center
  from a distance without occupying it with pawns.
  A large pawn center is a target, not just an asset.

HYPERMODERN OPENINGS STILL PLAYED TODAY:
  Nimzo-Indian Defense: 1.d4 Nf6 2.c4 e6 3.Nc3 Bb4
    (Pin the c3 knight, fight d4-e4 center from afar)
  King's Indian Defense: 1.d4 Nf6 2.c4 g6 3.Nc3 Bg7
    (Fianchetto bishop, allow opponent big center,
     then attack it with f5 or e5)
  Grünfeld Defense: 1.d4 Nf6 2.c4 g6 3.Nc3 d5
    (Accept big center for Black, attack with pieces)
  Réti Opening: 1.Nf3 (hypermodern first move, no e4/d4)

Aaron Nimzovich "My System" (1925/1930): defining text
of hypermodern theory. Introduced concepts of:
  - Blockade (knight on e5 blockades passed pawn)
  - Overprotection (protect key squares more than necessary)
  - Prophylaxis (prevent threats before they exist)
```

### Era 4: Soviet School (1945–1990s)

The Soviet Union made chess a state sport after WWII, treating it as proof of intellectual superiority. This produced a systematic, industrial approach to chess improvement.

```
THE BOTVINNIK SYSTEM
═════════════════════

Mikhail Botvinnik (World Champion 1948-1963 with two
interruptions): engineer + chess machine.

SYSTEMATIC TRAINING APPROACH:
  - Preparation: deep opening theory research for EACH
    specific opponent (knowing their weaknesses)
  - Physical training: chess requires stamina (6-hour games)
  - Self-analysis: post-game written analysis, no computer
  - Interruptions: take breaks to avoid clock pressure errors
  - Strategy over tactics: win positions methodically

SOVIET CHESS DOMINANCE:
  World Champions: Botvinnik, Smyslov, Tal (the exception),
  Petrosian, Spassky, Karpov, Kasparov
  From 1948 to 1972 (Fischer), ALL world champions Soviet.
  From 1975 to 1993, ALL world champions Soviet.

CHESS SCHOOLS (state-funded):
  Moscow, Leningrad, Baku, Tbilisi, Odessa...
  Young players identified early, given state support.
  Equivalent to modern sports academies.

OPENING THEORY EXPLOSION:
  Soviets systematically analyzed and documented openings.
  ECO (Encyclopedia of Chess Openings) system developed.
  Hundreds of opening lines named and analyzed.
  Pre-game preparation became a distinct skill.
```

### The Fischer Interruption (1972)

Bobby Fischer (USA, 1943-2008) won the 1972 World Championship match against Boris Spassky 12.5-8.5. The context:

```
FISCHER vs SPASSKY, 1972 REYKJAVIK — COLD WAR CHESS
═════════════════════════════════════════════════════

Context: Nixon/Brezhnev Cold War. Two months. 24 games.
Watched by millions globally. Front page news daily.

Game 1: Spassky wins after Fischer blunders in drawn endgame.
Game 2: Fischer FORFEITS (refuses to play, complains about
        cameras). Spassky 2-0 after forfeit.
Game 3: Played in a back room (Fischer demands no cameras).
        Fischer wins with extraordinary Nimzo-Indian.

After Game 3: Fischer wins 12.5-8.5. Spassky applauds
from the audience after the final game.

FISCHER'S SIGNIFICANCE:
  - First non-Soviet world champion in 24 years
  - Peak rating 2785 (1972), #2 of all time in peak Elo
  - "Fischer Random" (Chess960): shuffled starting positions
    to eliminate opening preparation. His invention.
  - Refused to defend title in 1975 (Karpov). Disappeared.
  - Returned in 1992 for rematch vs Spassky (illegal game,
    Yugoslavia sanctions). Fischer vanished again.
  - Brilliant, paranoid, antisemitic (despite being Jewish),
    died 2008 in Iceland — the most tragic brilliant chess figure.
```

### Era 5: Computer Revolution (1986–present)

```
CHESS AI TIMELINE
═════════════════

1948: Norbert Wiener suggests chess programs; Alan Turing
      designs paper algorithm (Turochamp) — too slow to run.

1950: Claude Shannon's "Programming a Computer for Playing Chess"
      — defines evaluation functions, minimax, alpha-beta pruning.
      Shannon Number: ~10^120 possible chess games estimated.

1956: Los Alamos chess program — first running chess program
      (6x6 board, no bishops).

1968-1974: CHESS (Northwestern) — first competitive programs.
            Mac Hack wins against tournament players.

1989: Deep Thought (IBM precursor) — draws with Kasparov once.

1996: Deep Blue defeats Kasparov in Game 1 (first ever game
      loss for Kasparov to a computer in tournament play).
      Kasparov wins match 4-2.

1997: Deep Blue REMATCH.
      Kasparov loses match 3.5-2.5.
      KEY MOMENT: Game 2, move 36 — Deep Blue plays Bc4.
      Kasparov assumes the move is a known database line
      (IBM had fed Deep Blue grandmaster games). He resigns.
      Later analysis: Bc4 was a random pruning artifact —
      Deep Blue couldn't find a good move, played safe.
      Kasparov is broken psychologically. He asks to see
      the logs; IBM refuses.

2006: Deep Fritz 10 defeats Kramnik (then World Champion)
      4-2 in a formal match. Computers now clearly superhuman.

2017: ALPHAZERO — trained from scratch (tabula rasa), no human
      games used. Self-play only. Learned chess in 4 hours.
      Defeated Stockfish 8 (best engine at time): 28W-0L-72D.
```

### Deep Blue vs Kasparov: The Landmark

```
1997 MATCH: DEEP BLUE (IBM) vs KASPAROV
═════════════════════════════════════════

Deep Blue specifications:
  - 30 processors + 480 chess chips
  - 200 million positions/second evaluated
  - 10-12 ply (5-6 moves ahead) with selective extensions
  - Grandmaster database: millions of games
  - Endgame tablebases: perfect play from 5 pieces

Kasparov's strategy: psychological pressure, opening novelties
  not in DB, positional complexity computers handle poorly.

Game 1: Kasparov wins (Deep Blue plays well, Kasparov wins carefully)
Game 2: Deep Blue wins (Bc4 "phantom" move breaks Kasparov)
Game 3: Draw
Game 4: Draw
Game 5: Kasparov wins (blunders from Deep Blue)
Game 6: Deep Blue wins (Kasparov resigned in drawn position)

Final: 3.5–2.5, Deep Blue wins.

KASPAROV'S FAMOUS POST-MATCH CLAIM:
  "The machine was playing like a god." He accused IBM of
  human intervention (having a grandmaster advise the machine
  during Game 2). IBM denied it. Logs were never released.
  The question was never definitively settled.
```

### AlphaZero: The Paradigm Shift

```
ALPHAZERO (DeepMind, 2017)
═══════════════════════════

Training:
  Input: raw board position
  No opening books, no endgame tablebases
  No human games used in training
  Self-play from random moves
  Training time: 4 hours for chess, 8 hours for Go

Architecture:
  - Policy network: predicts probability of each legal move
  - Value network: evaluates position (-1 to +1)
  - Monte Carlo Tree Search: uses policy + value for guidance
    rather than random rollouts
  - 40 residual blocks, 256 filters per block

vs Stockfish 8 (100 games, 1 minute/move):
  AlphaZero: 28W 0L 72D (from white: 25W 0L 25D)
             (from black: 3W 0L 47D)
  Caveat: Stockfish 8 was not given its opening book or
  endgame tablebases in this match, and used 1 min/move
  without access to the pondering mode it normally uses.
  The chess engine community criticized the methodology —
  a properly configured Stockfish would have been stronger.
  A later 2019 paper with fairer conditions still showed
  AlphaZero winning, but the margin was narrower.

WHAT IT REVEALED ABOUT HUMAN CHESS THEORY:
  - AlphaZero favored King's Indian and Sicilian aggressively
    (humans thought these positions were slightly worse for Black
    with best play — AlphaZero played them anyway and won)
  - e4 preferred over d4 (AlphaZero: "e4 is more ambitious")
  - Sacrificed pawns for piece activity more willingly than
    human engines (Stockfish was material-greedy)
  - King safety evaluated differently — marched king into the
    center in the middlegame in ways that horrified human analysis
  - Long-term positional sacrifices: gave up material for
    "invisible" compensation engines miss (piece activity,
     pawn structure 30 moves in the future)

The conclusion: 500 years of human chess theory has significant
bias toward what humans can calculate and remember, not toward
what is actually optimal.
```

---

## Section 4: Elo Rating System

Arpad Elo (1903-1992), a Hungarian-American physics professor, developed the Elo system for the United States Chess Federation, adopted by FIDE in 1970.

```
ELO RATING MATHEMATICS
════════════════════════

Expected score for player A vs player B:
  E_A = 1 / (1 + 10^((R_B - R_A)/400))

  If R_A = R_B: E_A = 0.5 (50% expected)
  If R_A = R_B + 400: E_A = 0.909 (91% expected)
  If R_A = R_B - 400: E_A = 0.091 (9% expected)

Rating update after game:
  R_A_new = R_A + K × (S_A - E_A)

  where S_A = actual score (1=win, 0.5=draw, 0=loss)
  K = K-factor (volatility constant):
    K=40 for new players (< 30 games)
    K=20 for established players
    K=10 for players rating 2400+

CALIBRATION:
  1000 = beginner
  1200 = casual club player
  1500 = serious club player
  1800 = strong club player
  2000 = candidate master
  2200 = national master (NM)
  2300 = FIDE master (FM)
  2400 = international master (IM)
  2500 = grandmaster (GM)
  2700 = super-grandmaster ("2700 club")
  2800+ = world champion tier
  2882 = Magnus Carlsen peak (2014), all-time record

LIMITATIONS:
  - Rating inflation over time (pool grows, new players start low)
  - K-factor choices are arbitrary
  - Assumes normally distributed performance
  - Doesn't capture time-of-day, preparation, psychological state
  - Computer assistance cheating undermines system (see Hans Niemann 2022)
```

---

## Section 5: Chess Theory Concepts

### Tactical Patterns (the vocabulary)

```
TACTICAL MOTIFS
════════════════

FORK: One piece attacks two pieces simultaneously.
  Knights excel at forks (8 possible directions).
  "Knight fork" = most common tactic in beginners' games.

PIN: Attacking a piece that cannot move because doing so
  would expose a more valuable piece behind it.
  ABSOLUTE pin: exposes the King (cannot move legally)
  RELATIVE pin: exposes the Queen (can move, just bad)

SKEWER: Like a pin reversed — attack valuable piece,
  force it to move, capture the piece behind it.
  Attack the queen, queen moves, win the rook.

DISCOVERED CHECK: Move a piece to expose a check from
  the piece behind it. Devastating because both pieces
  can threaten simultaneously.

ZWISCHENZUG: "In-between move" (German). Instead of
  the expected recapture, play an interim forcing move
  first. Changes the assessment of exchanges.

DEFLECTION: Force a key defender to move.
OVERLOADING: Force a piece to guard too many things.
INTERFERENCE: Place a piece on a square that cuts off
  defense/attack.
```

### Key Endgame Concepts

```
FUNDAMENTAL ENDGAME POSITIONS
═══════════════════════════════

LUCENA POSITION (rook endgame, winning):
  Advanced king + pawn + rook vs rook.
  Technique: "build a bridge" — rook cuts off opposing
  king, king advances, pawn promotes.

PHILIDOR POSITION (rook endgame, drawing):
  Defending with rook vs rook + pawn.
  Key: keep rook on 6th rank until pawn advances to 6th,
  then switch to checking from behind.

OPPOSITION:
  Two kings "in opposition" means they face each other
  with one square between them. The player NOT to move
  has the opposition — their king controls the square
  the opponent's king wants to enter.
  Critical in pawn endgames.

KEY SQUARES (pawn endgames):
  For a pawn on e4, the "key squares" are d6, e6, f6.
  If the attacking king reaches any key square, the pawn
  promotes regardless of where the defending king stands.

TREBUCHET (mutual zugzwang):
  A position where whoever must move loses. Both kings
  oppose each other's key squares. Rare but decisive.
```

---

## Section 6: Chess Variants and Online Era

### Fischer Random / Chess960

Bobby Fischer proposed Chess960 as a solution to the opening preparation arms race:

```
CHESS960 RULES
═══════════════

Starting position randomized according to rules:
  - Bishops must be on opposite colors
  - King must be between the two rooks (for castling)
  - There are exactly 960 legal starting positions

RATIONALE:
  In classical chess, the first 15-20 moves are often
  pure memorization (opening theory books run to volumes).
  Magnus Carlsen prepared 30+ moves in specific lines.
  Fischer argued: this rewards preparation, not chess skill.

  Chess960 forces improvisation from move 1.
  True chess thinking begins immediately.

ADOPTION:
  Not mainstream until Magnus Carlsen embraced it (~2018).
  2019: first Chess960 World Championship (Carlsen wins).
  Now played regularly at elite level.
```

### Online Chess Democratization

```
ONLINE CHESS IMPACT (2000–present)
════════════════════════════════════

PLATFORMS:
  Chess.com: 100M+ registered users (2023)
              Acquired Twitch chess channel Chess24 (2022)
  Lichess: open source, free, no ads. ~4M games/day.

FORMATS:
  Classical: 60-90+ minutes/side (tournament standard)
  Rapid: 10-30 minutes/side
  Blitz: 3-5 minutes/side
  Bullet: 1 minute/side
  Hyperbullet: 30 seconds/side

  Online shifted elite play toward faster formats.
  Carlsen's "Speed Chess Championship" (Chess.com) became
  a major event — testing different cognitive skills.

THE MAGNUS EFFECT:
  Magnus Carlsen consistently ranked #1 from ~2010 to 2023.
  His 2013 victory over Anand was anticipated for years.
  In 2023, Carlsen DECLINED to defend his Classical title —
  citing the format as too drawish and slow to demonstrate
  superiority. A structural comment on classical chess.

HANS NIEMANN CHEATING SCANDAL (2022):
  Magnus Carlsen resigned from the Sinquefield Cup after
  losing to Hans Niemann (a relatively unknown 19-year-old).
  Carlsen strongly implied cheating without stating it directly.
  Chess.com analysis: Niemann's statistical results in online
  play suggested AI assistance in hundreds of games.
  Impact: cheating detection, engine assistance, OTB cheating
  (over-the-board) all became major topics.
  Niemann sued Carlsen, Chess.com, and others for defamation.
  Case settled 2023.
```

---

## Decision Cheat Sheet

| You want to know... | Answer |
|---------------------|--------|
| When was modern chess created? | 1475, Spain/Italy — queen and bishop got modern movement |
| Why queen is most powerful | 1475 change: firz (1-diagonal) → unlimited any direction |
| First official world champion | Wilhelm Steinitz, 1886 |
| Cold War chess match | Fischer vs Spassky, 1972, Reykjavik (Fischer wins 12.5-8.5) |
| First computer to beat reigning champion | Deep Blue beats Kasparov, 1997 (3.5-2.5) |
| AlphaZero significance | Tabula rasa, 4 hours training, defeated Stockfish — revealed human theory biases |
| Elo formula for expected score | E_A = 1/(1 + 10^((R_B - R_A)/400)) |
| Magnus Carlsen peak rating | 2882 (2014), all-time record |
| Fischer Random purpose | Eliminate opening preparation memorization, 960 starting positions |
| Soviet chess dominance dates | 1948–1972, then 1975–1993 (Fischer interruption) |

---

## Common Confusion Points

**"Chess was invented in India"**: Chaturanga originated in India, but modern chess emerged through Persian Shatranj and then European modification. The game changed so substantially in 1475 that calling modern chess "Indian" is misleading — it's more accurately "European chess built on Indian/Persian foundations."

**"Deep Blue won the 1996 match"**: Deep Blue won Game 1 of the 1996 match but Kasparov won the overall 1996 match 4-2. Deep Blue won the 1997 REMATCH 3.5-2.5. The distinction matters.

**"AlphaZero solved chess"**: No. AlphaZero achieved superhuman play via neural evaluation + MCTS but did not solve chess. Chess has ~10^47 legal positions — it cannot be solved by enumeration. Even the question "is the starting position a win for White, Black, or a draw?" remains unanswered. The working assumption of experts is that perfect play results in a draw. What *is* solved: all positions with 7 or fewer pieces, via Syzygy tablebases (Lomonosov 2012). The method is retrograde analysis — backward induction (DP) from all terminal positions over the endgame DAG, exactly Bellman's principle applied to the exhaustive state space. These databases provide provably perfect play from any 7-piece position and are integrated into all modern engines.

**"The Elo system is a chess-specific invention"**: Elo's expected score formula E_A = 1/(1 + 10^((R_B - R_A)/400)) is a special case of the Bradley-Terry paired comparison model from statistics (1952). Bradley-Terry assigns each item a "strength" parameter and models pairwise comparison probabilities as logistic functions of strength differences — exactly what Elo does. The model extends naturally to any domain requiring pairwise skill estimation (sports, recommendation systems, LLM evaluation via Chatbot Arena).

**"The Elo system is fair"**: It's a good approximation but has known biases: rating inflation over time, K-factor arbitrariness, doesn't account for opponent selection bias, doesn't measure playing strength per se but performance relative to opposition.

**"Stalemate is the same in all chess variants"**: In Shatranj, stalemate was a WIN for the player who achieved it. In modern chess, it's a draw. This is a known historical change that new players sometimes don't realize was a deliberate rule modification.

**"Magnus Carlsen is world champion"**: As of 2023-2024, Carlsen declined to defend his title. The current classical chess World Champion is Ding Liren (China), who won the 2023 championship match against Ian Nepomniachtchi after Carlsen withdrew.
