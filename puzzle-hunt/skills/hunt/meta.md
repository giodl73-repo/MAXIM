# /hunt meta — Meta Puzzle Design and Verification

Design, verify, and test meta puzzles that combine feeder answers.

## Usage

```
/hunt meta                — show meta design status for active scenario
/hunt meta design         — guided meta design (mechanism, answer, grid)
/hunt meta verify         — verify the meta works with current answer words
/hunt meta grid           — show/build the crossword grid (if crossword meta)
/hunt meta test           — blind-test the meta with 3 experts
```

## What It Does

Reads the scenario's `meta/META-DESIGN.md` and `PUZZLES.md` to:
- Show which feeder answers are locked vs TBD
- Verify crossword constructability (if crossword meta)
- Check 80% rule (solvable with N-1 of N feeders)
- Check backsolving potential
- Run the meta through the expert panel

## Verification Checklist

When `/hunt meta verify` runs:
- [ ] All feeder answer words confirmed (none TBD)
- [ ] Meta mechanism produces the correct meta answer
- [ ] Crossword crossings all valid (if applicable)
- [ ] Solvable with 80% of feeders (Katz's rule)
- [ ] Cannot be brute-forced from partial info (Huang)
- [ ] The meta answer is surprising yet inevitable (Selinker)
