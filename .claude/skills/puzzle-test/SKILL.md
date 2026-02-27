# /puzzle-test — Beta-Test a Puzzle with the Expert Panel

Present a completed puzzle to a selection of expert reviewers for scoring and feedback. The puzzle is shown CLEAN — no design notes, no "this is what I was going for." The testers see what a solver would see.

## Usage

```
/puzzle-test <element-or-compound>     — test a puzzle with 3-5 selected reviewers
/puzzle-test <element> full            — test with all 12 reviewers
/puzzle-test <element> single <name>   — test with one specific reviewer
/puzzle-test iterate <element>         — apply feedback and re-test until passing
/puzzle-test status                    — show test results for all authored puzzles
```

---

## The Testing Process

### 1. Select Testers

Default: 5 reviewers selected for relevance to the puzzle type.

| Puzzle type | Default testers |
|------------|----------------|
| Cipher / code-breaking | Huang, Snyder, Kenny, Blow, Pope |
| Crossword / word puzzle | Katz, Snyder, Dana, Rosenthal, Gottlieb |
| Logic grid / deduction | Huang, Snyder, Katz, Pope, Gottlieb |
| Calculation / diagram | Kenny, Snyder, Sarrett, Dana, Gottlieb |
| Identification / matching | Rosenthal, Dana, Miller, Pope, Katz |
| Visual / physical | Sarrett, Dana, Miller, Blow, Selinker |
| Narrative / timeline | Selinker, Katz, Rosenthal, Miller, Dana |
| Cross-section synthesis | Blow, Miller, Selinker, Katz, Snyder |

### 2. Present the Puzzle Clean

Each tester agent receives:
- The puzzle page ONLY (from `joker/`)
- The relevant encyclopedia files (what a solver would have access to)
- Their reviewer profile (for voice/perspective)
- NO design notes, NO intended solution, NO scoring rubric

The tester is told:
```
You are [NAME]. You have been given a puzzle page and access to
the encyclopedia. Solve the puzzle. Then evaluate it.

1. ATTEMPT TO SOLVE IT. Show your work. Note where you get stuck.
2. SCORE IT on these dimensions (1-5 each):
   - Clarity: Is it clear what you're supposed to do?
   - Solvability: Can you reach the answer with the materials provided?
   - Elegance: Is the mechanism clean? One aha?
   - Reading Reward: Did solving require genuine engagement with the content?
   - Fun: Would you enjoy this? Would you recommend it?
   - Confirmation: Can you tell if your answer is right?
3. FLAG any issues:
   - Ambiguous clues (multiple valid interpretations)
   - Broken paths (clue references content that doesn't exist)
   - Red herrings (unintentional misdirection)
   - Difficulty spikes (one step much harder than the rest)
   - Factual errors
4. SUGGEST specific fixes for any issues found.
```

### 3. Collect Results

Each tester saves their results to:
`puzzle-hunt/tests/[element]-[tester-name].md`

### 4. Synthesize

After all testers report, synthesize into:
`puzzle-hunt/tests/[element]-RESULTS.md`

Contains:
- **Aggregate score** (average across dimensions)
- **Pass/Fail** (passing = all dimensions ≥ 4, overall ≥ 22/30)
- **Issues found** (by severity: blocking, major, minor)
- **Suggested fixes** (from testers, prioritized)
- **Verdict**: PASS (ready to ship), REVISE (fix and re-test), or REDESIGN (fundamental problems)

---

## The Iterate Loop

### `/puzzle-test iterate <element>`

Automatic fix-and-retest loop:

```
1. Read test results from puzzle-hunt/tests/[element]-RESULTS.md
2. If PASS → done, congratulations
3. If REVISE:
   a. Apply the prioritized fixes to the puzzle page
   b. Save updated puzzle to joker/
   c. Re-test with the SAME testers (they see the revised version)
   d. Collect new results
   e. If PASS → done
   f. If still REVISE → loop (max 3 iterations)
   g. If REDESIGN → stop, flag for manual intervention
4. If REDESIGN → stop, describe the fundamental problem
```

Each iteration is saved:
- `puzzle-hunt/tests/[element]-v1-RESULTS.md`
- `puzzle-hunt/tests/[element]-v2-RESULTS.md`
- `puzzle-hunt/tests/[element]-v3-RESULTS.md`

### Passing Criteria

| Dimension | Minimum | Target |
|-----------|---------|--------|
| Clarity | 4 | 5 |
| Solvability | 4 | 5 |
| Elegance | 4 | 5 |
| Reading Reward | 4 | 5 |
| Fun | 4 | 5 |
| Confirmation | 3 | 4 |
| **Overall** | **22/30** | **27/30** |

A puzzle PASSES at 22/30 with no dimension below 4 (except Confirmation at 3).
A puzzle is EXCELLENT at 27/30.
A puzzle is PERFECT at 30/30.

### Issue Severity

| Severity | Definition | Action |
|----------|-----------|--------|
| **Blocking** | Puzzle cannot be solved as written | Must fix before re-test |
| **Major** | Puzzle is solvable but the experience is significantly degraded | Should fix |
| **Minor** | Polish issue, doesn't affect solvability | Fix if easy, otherwise note |

---

## Status Dashboard

### `/puzzle-test status`

Reads all files in `puzzle-hunt/tests/` and displays:

```
PUZZLE TEST STATUS

Element   | Compound  | Status    | Score  | Version | Issues
----------|-----------|-----------|--------|---------|-------
Si (14)   |           | PASS      | 28/30  | v2      | 0
C (6)     |           | REVISE    | 21/30  | v1      | 2 major
NaCl (58) |           | UNTESTED  | —      | —       | —
...
```

---

## Reviewer Profiles

All 12 reviewers are available for testing. Profiles in `puzzle-hunt/profiles/`.

| # | Name | Best for testing |
|---|------|-----------------|
| 1 | Dan Katz | Structure, meta-feeding, difficulty calibration |
| 2 | Thomas Snyder | Craftsmanship, deductive path, elegance |
| 3 | Mike Selinker | Narrative, memorability, personality |
| 4 | Wei-Hwa Huang | Solve-path rigor, brute-force resistance |
| 5 | Kenny Young | Construction quality, practical issues |
| 6 | Dana Young | Visual presentation, book-test, accessibility |
| 7 | Peter Sarrett | Experience, reading reward, physical interaction |
| 8 | Mark Gottlieb | Systemic consistency, edge cases, meta integration |
| 9 | Alex Rosenthal | Accessibility, wonder, TED-Ed test |
| 10 | Rand Miller | Diegetic integration, world-as-puzzle, connection |
| 11 | Jonathan Blow | Epiphany quality, information content, "be smart" vs "feel smart" |
| 12 | Lucas Pope | Deductive identification, confirmation design, lateral information |

---

## After Testing

When a puzzle passes:
1. The puzzle page in `joker/` is final
2. Run `/puzzle-test status` to see overall progress
3. Move to the next puzzle in Kenny's build order:
   - Carbon (Codons) → Sodium (Logic Grid) → Salt (NaCl) → Oxygen (Star Chart) → Cobalt (Anamorphic go/no-go)

When all 26 Red Joker puzzles pass, the Red Joker is ready to assemble.
When all 26 Black Joker puzzles pass, the Black Joker is ready to assemble.

---

## The Full Pipeline

```
/puzzle-author Si       → Write the Silicon/Cipher puzzle
                           ↓
/puzzle-test Si         → 5 testers attempt it clean
                           ↓
                        PASS? → Ship it
                        REVISE? ↓
/puzzle-test iterate Si → Fix issues, re-test (up to 3x)
                           ↓
                        PASS? → Ship it
                        REDESIGN? → Manual intervention
```
