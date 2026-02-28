# /puzzle — Puzzle Management

The single entry point for working with any puzzle. View, navigate, edit, comment, check status, see history.

## Usage

```
/puzzle <id>                — show puzzle overview (brief + status + scores + history)
/puzzle <id> brief          — show/edit the full puzzle brief
/puzzle <id> page           — show the authored puzzle page
/puzzle <id> tests          — show all test results for this puzzle
/puzzle <id> history        — show revision history (versions, scores, fixes)
/puzzle <id> comment <text> — add a comment/note to the puzzle
/puzzle <id> status <code>  — update status (BRIEF, AUTHORED, TESTING, PASS, REVISE, SHIP)
/puzzle <id> assign <author>— assign to an author/module
/puzzle <id> testers        — show assigned testers and their profiles
/puzzle <id> principles     — check puzzle against all 18 principles
/puzzle <id> answer         — show encoded answer (decode from ANSWERS.md)
/puzzle <id> meta           — show how this puzzle feeds into the meta
/puzzle list                — list all puzzles with status summary
/puzzle board               — kanban-style board (columns: BRIEF → AUTHORED → TESTING → PASS → SHIP)
```

---

## /puzzle <id> — Overview

Shows everything about a puzzle in one view:

```
╔══════════════════════════════════════════════════════╗
║  Puzzle III — Castle Age — Technologies              ║
╠══════════════════════════════════════════════════════╣
║  Type:     Tech Tree Gap-Fill                        ║
║  Domain:   Technologies                              ║
║  Diff:     3/5                                       ║
║  Status:   AUTHORED                                  ║
║  Score:    —/30 (untested)                           ║
║  Answer:   (encoded — see ANSWERS.md)                ║
║  Author:   unassigned                                ║
║  Module:   —                                         ║
╠══════════════════════════════════════════════════════╣
║  Testers:  Huang · Snyder · Gottlieb                 ║
║  Meta:     feeds → ∞ (WOLOLO crossword)              ║
╠══════════════════════════════════════════════════════╣
║  Brief:    6 missing techs in dependency chain.      ║
║            Interlock: 2 techs constrain each other.  ║
║            Riven: IS the tech tree.                  ║
╠══════════════════════════════════════════════════════╣
║  Comments:                                           ║
║    [Stage 3] Panel picked unanimously (3-0)          ║
║    [Stage 4] Needs answer word with O or L for meta  ║
╠══════════════════════════════════════════════════════╣
║  History:                                            ║
║    v0  BRIEF     Stage 4                             ║
╚══════════════════════════════════════════════════════╝
```

---

## /puzzle <id> brief — Full Brief

Shows (or creates/edits) the detailed puzzle brief. This is what an author needs to write the puzzle.

```markdown
# Brief: Puzzle III — Tech Tree Gap-Fill

## Identity
- **ID:** III
- **Round:** 1 (Castle Age)
- **Domain:** Technologies
- **Type:** Tech Tree Gap-Fill (dependency reasoning)
- **Difficulty:** 3/5
- **Answer:** (encoded in ANSWERS.md)

## Mechanism
[Detailed description of how the puzzle works]
- Present an ASCII tech tree with 6 blanks
- Each blank is a specific AoE technology
- Dependencies constrain which tech can fill each blank
- The solver must know the AoE tech tree to fill them

## Interlock Design
[How clues depend on each other]
- Blank 3 depends on Blank 1 (prerequisite chain)
- Blank 5 and Blank 6 share a dependency — solving one narrows the other

## Extraction
[How the answer is derived from the solved puzzle]
- First letters of the 6 missing tech names spell the answer
- Or: specific letters at indexed positions

## Content References
[What the solver needs to know]
- AoE2 tech tree (University, Blacksmith, Monastery branches)
- Technology prerequisites (Fletching → Bodkin Arrow → Bracer)

## Narrator Intro (draft)
> The research queue is broken. Six technologies are missing from the tree. The Castle Age waits.

## Principles Checklist
- [ ] Riven Standard: IS the tech tree
- [ ] Interlock: 2+ dependency constraints
- [ ] No Over-Scaffolding: don't label which branch each blank is on
- [ ] Surprise the Answer: answer word not guessable from "tech tree"
- [ ] Snyder's Computer Test: dependencies add deduction, not just lookup

## Notes
[Comments, open questions, reviewer feedback]
```

---

## /puzzle <id> comment <text>

Appends a timestamped comment to the puzzle's notes section in PUZZLES.md:

```
[2026-02-27 Stage 4] Panel picked unanimously (3-0)
[2026-02-27 Stage 5] Needs O or L in answer for meta crossword
[2026-02-28 Stage 6] Authored v1, sent to testing
[2026-02-28 Testing] 24/30 PASS — minor fix: clue 4 ambiguous
```

---

## /puzzle <id> principles

Runs the puzzle against all 18 design principles and reports pass/fail:

```
Principle Check: Puzzle III

✅ 1. The Riven Standard — IS the tech tree
✅ 2. Solving = Proving Understanding
✅ 3. Blame the Player
✅ 4. No Over-Scaffolding
⚠️ 5. Surprise the Answer — TBD (answer word not chosen yet)
✅ 6. Reading Reward ≥ 4
✅ 7. One Aha
✅ 8. The Book Test
✅ 9. No Deliberate Errors
✅ 10. Interlock — 2 dependency pairs
✅ 11. Snyder's Computer Test — dependencies prevent scripting
...

14/18 pass, 1 TBD, 3 not applicable
```

---

## /puzzle board

Kanban view of all puzzles:

```
BRIEF          AUTHORED       TESTING        PASS           SHIP
─────          ────────       ───────        ────           ────
I  Civs        (empty)        (empty)        (empty)        (empty)
II Units
III Techs
IV  Maps
V   Strategy
∞   Meta
```

---

## /puzzle list

Table view:

```
ID   Domain          Type                  Status    Score   Author
───  ──────          ────                  ──────    ─────   ──────
I    Civilizations   Bonus Matcher         BRIEF     —       —
II   Units           Tournament Bracket    BRIEF     —       —
III  Technologies    Tech Tree Gap-Fill    BRIEF     —       —
IV   Maps            Resource Map          BRIEF     —       —
V    Strategy        Economy Puzzle        BRIEF     —       —
∞    Meta            Crossword → WOLOLO    BRIEF     —       —
```

---

## /puzzle <id> meta

Shows how this puzzle connects to the meta:

```
Puzzle III feeds → Meta ∞ (WOLOLO crossword)

Answer word: (encoded)
Position in crossword: Slot 3 (across/down TBD)
Crossing letters: shares letter with Puzzle I at position N
Highlighted squares in this word: position(s) TBD

If this puzzle's answer changes, verify:
- Crossword grid still constructable
- Crossing letters still valid
- WOLOLO still extractable from highlights
```

---

## Data Sources

This skill reads from:
- Scenario's `PUZZLES.md` — the master registry
- Scenario's `ANSWERS.md` — encoded answers
- Scenario's `puzzles/<id>.md` — authored puzzle pages
- Scenario's `tests/<id>-RESULTS.md` — test results
- Scenario's `reviews/` — panel feedback
- Scenario's `ROUNDS.md` — round/meta structure
- `toolkit/PRINCIPLES.md` — for principle checks
- `toolkit/profiles/` — for tester profile display

This skill writes to:
- Scenario's `PUZZLES.md` — status updates, comments
- Scenario's `CLAUDE.md` — stage progress updates
