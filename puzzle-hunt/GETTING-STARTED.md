# Getting Started — Your First Puzzle Hunt

A step-by-step walkthrough for building a puzzle hunt from scratch using this toolkit.

---

## Prerequisites

- Claude Code installed and working
- A content library (any structured collection of knowledge — files, books, a website)
- This toolkit directory

---

## Step 1: Install (5 minutes)

```bash
# Copy skills to Claude Code
cp -r skills/* ~/.claude/skills/    # macOS/Linux
xcopy /E skills\* %USERPROFILE%\.claude\skills\   # Windows

# Start Claude Code in this directory
cd puzzlehunt
claude
```

Claude reads `CLAUDE.md` automatically and knows about all the skills.

---

## Step 2: Set Your Scope (30 minutes)

Run `/puzzle-plan` and answer the questions:

- **What's your content?** Point to your content library.
- **How big?** Start small — 8-12 puzzles is a great first hunt.
- **Who's solving?** Solo? Team? Casual? Expert?
- **Theme?** Optional but recommended. Gives the hunt personality.

The skill writes `SCOPE.md` for you.

---

## Step 3: Get Your First Review (20 minutes)

```
/puzzle-review full SCOPE.md
```

9-12 expert personas evaluate your scope. You'll get feedback on feasibility, audience fit, and structure. Adjust based on their input.

This is the first gate. Don't skip it — the panel catches problems you won't see.

---

## Step 4: Design Rounds (30 minutes)

Fill in `ROUNDS.md`:
- How many rounds?
- How many puzzles per round?
- What's the meta for each round?
- How do rounds unlock each other?

For your first hunt: **1 round, 8 puzzles, 1 meta.** Keep it simple.

Review: `/puzzle-review full ROUNDS.md`

---

## Step 5: Brainstorm Puzzles (1 hour)

This is the fun part. For each section of your content, brainstorm 2-3 puzzle ideas. Write them as one-line briefs in `PUZZLES.md`. Don't self-censor — generate more than you need.

Think about:
- What does this section TEACH? (The Riven Standard: the puzzle IS the field)
- What's the aha? (One clean insight per puzzle)
- What type? (Cipher, crossword, logic grid, identification, calculation, visual, physical...)
- Would you tell someone about this at dinner? (The Dinner Party Test)

Review: `/puzzle-review rank PUZZLES.md` — the panel picks the best ones.

---

## Step 6: Assign Puzzles (30 minutes)

Take the panel's rankings and fill in the full `PUZZLES.md` registry:
- Which puzzles go in which slots
- Answer words for each (encoded — see CLAUDE.md § Answer Security)
- 3 testers assigned per puzzle
- Difficulty ratings

Review: `/puzzle-review full PUZZLES.md`

---

## Step 7: Design the Meta (1 hour)

Fill in `meta/META-DESIGN.md`:
- What mechanism combines the feeder answers?
- What's the meta answer?
- Can it be solved with 80% of feeders? (Katz's rule)
- Can it be brute-forced? (It shouldn't be)

Review: `/puzzle-review full meta/META-DESIGN.md`

---

## Step 8: Author Puzzles (the main work)

For each puzzle:

```
/puzzle-author <puzzle-id>
```

The skill reads your content library, writes the full puzzle page with worksheet, and verifies against the 18 principles.

Then test:

```
/puzzle-test <puzzle-id>
```

3 expert personas solve it blind and score it. Target: ≥22/30 with all dimensions ≥4.

If it fails:
```
/puzzle-test iterate <puzzle-id>
```

Fix → retest → fix → retest. Max 3 iterations.

Track progress: `/puzzle-status`

---

## Step 9: Assemble (1 hour)

Once all puzzles pass:
- Verify the meta works with actual answer words
- Check difficulty curve across the hunt
- Write narrative elements (intro, flavor text, closing)
- Design hint system if using one (see `HINTS.md`)
- Final review: `/puzzle-review full` on the complete hunt

---

## Step 10: Ship It

Your puzzle hunt is ready. Package it however you like:
- Print as a book
- Deploy as a website
- Run as a live event
- Email as a PDF

---

## Tips from Experience

**What we learned from building a 52-puzzle hunt:**

1. **Pure computation always fails testing.** If the solver just applies formulas, it's an exercise, not a puzzle. Add a deduction layer.

2. **The first draft is always over-scaffolded.** Remove the inline tables, the step-by-step instructions, the letter-count hints. Trust the solver.

3. **The answer word matters.** If the solver can guess it from the topic, there's no surprise. DNA puzzle → GENETIC is boring. DNA puzzle → ALCHEMY is a revelation.

4. **Interlock transforms quizzes into puzzles.** If every clue can be solved independently, it's a quiz. Make at least 2-3 clues depend on each other.

5. **Test blind, always.** The author knows the answer. The tester doesn't. The gap between those two experiences is where all the bugs live.

6. **The principles are earned, not invented.** Every one of the 18 principles came from a test failure or a panel finding. Read them before authoring. Check them before shipping.

7. **Start small.** 8 puzzles, 1 meta, 1 round. Get the pipeline working. Then scale.
