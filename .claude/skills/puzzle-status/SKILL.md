# /puzzle-status — Pipeline Dashboard

Show the current state of all 52 puzzles across authoring, testing, revision, and assembly.

## Usage

```
/puzzle-status              — full dashboard (all 52 puzzles)
/puzzle-status red          — Red Joker only (26 elements)
/puzzle-status black        — Black Joker only (26 compounds)
/puzzle-status tests        — test results summary
/puzzle-status next         — what to do next (prioritized action list)
```

---

## How It Works

Scan the file system and report:

### 1. Authoring Status
For each of the 52 puzzle files in `joker/red/` and `joker/black/`:
- Count lines. If > 35 → **Authored**. If ≤ 35 → **Scaffold only**.
- List authored puzzles with their answer words (decode from `memory/k53.md` if needed — A1Z26 → periodic table encoding).

### 2. Test Status
For each file in `puzzle-hunt/tests/*-RESULTS.md`:
- Extract the verdict (PASS / REVISE / REDESIGN)
- Extract the score (N/30)
- Flag any REVISE puzzles that have been revised (check file modification dates or version markers)

### 3. Revision Status
Compare test results to puzzle file timestamps:
- If REVISE verdict exists AND puzzle file is newer than test file → **Revised, needs retest**
- If REVISE verdict exists AND puzzle file is older → **Needs revision**
- If no test exists → **Untested**

### 4. Assembly Status
Check for:
- `joker/red/00-OPENING.md` — has real content?
- `joker/red/99-CLOSING.md` — has meta crossword?
- `joker/black/00-THE-GRID.md` — populated with real keywords?
- `joker/black/99-CLOSING.md` — has meta content?
- `joker/templates/` — all templates present?

### 5. Summary Counts

```
RED JOKER (Vol. 53)
  Authored:  NN/26
  Tested:    NN/26 (NN pass, NN revise, NN untested)
  Revised:   NN need revision, NN revised awaiting retest

BLACK JOKER (Vol. 54)
  Authored:  NN/26
  Tested:    NN/26
  Grid:      NN/52 keywords embedded

META
  Red crossword: designed / not designed
  Black extraction: designed / not designed
  5 candidate pairs: confirmed / TBD

OVERALL: NN/52 puzzles ship-ready
```

---

## The `/puzzle-status next` Command

Prioritized action list based on current state:

1. **Revisions needed** — puzzles with REVISE verdict not yet fixed (highest priority)
2. **Retests needed** — revised puzzles awaiting retest
3. **Untested authored puzzles** — authored but never tested
4. **Unauthored puzzles** — scaffolds without content
5. **Meta design** — crossword grid, Grid population, extraction mechanisms
6. **Assembly** — opening, closing, templates

For each action, show: the puzzle identifier, what needs doing, and which skill to invoke (`/puzzle-author`, `/puzzle-test`, `/puzzle-test iterate`).

---

## Implementation

This skill reads files, it does not write them. It uses:
- `joker/red/*.md` and `joker/black/*.md` (line counts)
- `puzzle-hunt/tests/*-RESULTS.md` (verdicts and scores)
- `puzzle-hunt/FINAL-52.md` (the assignment table)
- `puzzle-hunt/TEST-CREWS.md` (tester assignments)
- `.claude/` project memory `k53.md` (encoded answers — decode for display)

Display the dashboard in a clean table format. Color-code if terminal supports it: green for PASS, red for REVISE, yellow for untested, grey for scaffold.
