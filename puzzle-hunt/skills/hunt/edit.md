# /hunt edit — Editorial Review of Author Submissions

The admin reviews puzzle submissions from module authors before blind testing. Catches errors, trims verbosity, evaluates deviations, ensures brief compliance.

## Usage

```
/hunt edit <module>          — review one module's submission
/hunt edit all               — review all submitted modules
/hunt edit <module> approve  — approve for testing
/hunt edit <module> revise   — request revision with specific notes
```

---

## What the Editor Checks

For each submitted puzzle, evaluate:

### 1. Brief Compliance
Does the puzzle match what was assigned?
- Correct mechanism? (Or did the author deviate?)
- Correct answer word? (Or did they pick something different?)
- Correct domain? (Or did they drift into another game/section?)
- If deviated: is the deviation BETTER? (The Skeptic is sometimes right.)

### 2. Factual Accuracy
Are all facts correct against world/ data?
- Every number, rule, stat, name must be verifiable in world/
- Flag anything with [VERIFY] or no source
- Check game-specific rules (the Speedster often gets these wrong)

### 3. Principles Check
Run against the 20 design principles:
- Riven Standard: is the puzzle IS the game?
- No Over-Scaffolding: does the worksheet do the work?
- No Computation Without Deduction: is there a deduction step?
- Interlock: do clues cross-reference?
- Snyder's Computer Test: could a script solve it?

### 4. Length and Voice
- Too long? (The Methodical writes 3x more than needed)
- Too short? (The Speedster skips detail)
- Voice consistent with the hunt's narrator?
- Solver-facing content separated from author's working notes?

### 5. Extraction Verification
- Does the mechanism actually produce the answer word?
- Is the extraction clean and unambiguous?
- Does it work with the meta? (crossing letters if crossword)

---

## Editorial Verdicts

| Verdict | Meaning | Author action |
|---------|---------|---------------|
| **APPROVE** | Ready for blind testing | None — puzzle moves to /puzzle test |
| **REVISE: minor** | Small fixes needed | Author fixes specific items, resubmits |
| **REVISE: major** | Significant rework | Author rewrites sections, admin re-reviews |
| **REJECT** | Doesn't match brief or is fundamentally broken | Author starts over or puzzle goes back to pool |
| **APPROVE WITH NOTES** | Passes but editor made inline edits | Author reviews edits, confirms |

---

## Handling Author Personalities

| Author type | Common issue | Editorial approach |
|-------------|-------------|-------------------|
| The Methodical | Over-documents. 200 lines when 80 suffice. | Trim aggressively. Separate working notes from solver content. |
| The Speedster | Errors in details. Ships before verifying. | Line-by-line fact check. Send back with specific bug list. |
| The Skeptic | Deviates from brief. Argues about principles. | Evaluate the deviation honestly. If better: approve. If not: explain why with evidence. |
| The Social | Messy file with collaboration notes mixed in. | Clean up. Keep the collaboration insights, remove the process. |
| The Lurker | No notes. No communication. Mystery box. | Review extra carefully — no author context means editor must reverse-engineer intent. |

---

## Output

Save editorial review to: `reviews/editorial-review.md`

For each module:
```markdown
## M[N] — [Game] — [Author]

**Brief compliance:** MATCH / DEVIATED (describe)
**Factual accuracy:** N errors found (list)
**Principles:** N/18 pass (flag failures)
**Length:** OK / TOO LONG (trim to ~N lines) / TOO SHORT (expand)
**Voice:** OK / NEEDS ADJUSTMENT (notes)
**Extraction:** VERIFIED / BROKEN (describe)

**Verdict:** APPROVE / REVISE / REJECT

**Required fixes:**
1. (specific, actionable)
2. ...

**Editor notes:**
(context, praise, concerns)
```

After all modules reviewed, update PUZZLES.md status column and add editorial comments via `/puzzle <id> comment`.
