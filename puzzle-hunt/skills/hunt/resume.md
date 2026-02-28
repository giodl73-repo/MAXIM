# /hunt resume — Resume a Hunt from Where It Left Off

Read the scenario's `CLAUDE.md`, identify the next incomplete stage, and continue the pipeline. Crash-safe: every invocation picks up exactly where the previous session ended.

## Usage

```
/hunt resume              — read CLAUDE.md, show state, proceed to next stage
/hunt resume status       — show current state only, do not proceed
/hunt resume stage <N>    — force a specific stage regardless of CLAUDE.md status
```

---

## How It Works

### Step 1 — Read the scenario CLAUDE.md

Find the pipeline status table. It looks like this:

```
| Stage | Status | Deliverable | Notes |
|-------|--------|-------------|-------|
| 1. SCOPE      | Done | SCOPE.md         |       |
| 2. STRUCTURE  | Done | ROUNDS.md        |       |
| 3. PUZZLE POOL| Done | PUZZLE-POOL.md   |       |
| 4. ASSIGNMENT | --   | PUZZLES.md       |       |
```

The first row with `--` in the Status column is **the next stage**.

### Step 2 — Show a recovery summary

Output a brief state-of-play so the user understands what's been done and what's next:

```
HUNT RESUME — [Hunt Name]
━━━━━━━━━━━━━━━━━━━━━━━━
  ✅ Stage 1: SCOPE
  ✅ Stage 2: STRUCTURE
  ✅ Stage 3: PUZZLE POOL
  ⏭  Stage 4: ASSIGNMENT ← proceeding now
  --  Stage 5: META DESIGN
  --  Stage 6: AUTHORING
  ...
```

### Step 3 — Proceed with the next stage

Unless `status` flag was given, immediately begin the next stage.

---

## Stage Dispatch Table

| Stage | What to do |
|-------|------------|
| 1. SCOPE | Run Stage 1 of `/hunt plan`. Create `SCOPE.md` and scenario `CLAUDE.md`. |
| 2. STRUCTURE | Run Stage 2 of `/hunt plan`. Create `ROUNDS.md`. For fictional worlds, run `/hunt world`. |
| 3. PUZZLE POOL | Run Stage 3 of `/hunt plan`. Create `PUZZLE-POOL.md`. Then `/hunt review rank PUZZLE-POOL.md`. |
| 4. ASSIGNMENT | Run Stage 4 of `/hunt plan`. Create or complete `PUZZLES.md` with full briefs and coordinated answers. |
| 5. META DESIGN | Run `/hunt meta`. Create `meta/META-DESIGN.md`. Verify 80% rule. |
| 6. AUTHORING | For each puzzle in `PUZZLES.md` with status `--`: run `/puzzle <id> author`. Then `/puzzle <id> test`. Stage is done when all puzzles pass. |
| 7. EDITORIAL | Run `/hunt edit` on all submitted puzzles. Create `reviews/editorial-review.md`. |
| 8. INTEGRATION | Run Stage 8 checklist from `/hunt plan`. Create `reviews/integration-check.md`. |
| 9. DELIVERY BUILD | Run `/hunt site`, `/hunt print`, `/hunt props` as appropriate for this hunt's delivery format. |
| 10. PLATFORM TEST | Run live-solve simulation. Create `tests/live-solve-simulation.md`. |
| 11. POLISH | Final pass: verify all extractions, encode answers, confirm difficulty curve, finalize hints if any. |

---

## During Authoring (Stage 6)

Stage 6 is the longest stage. On resume, handle it granularly:

1. Read `PUZZLES.md` — find every puzzle with status `--` or `in progress`
2. Show per-puzzle state:
   ```
   Stage 6: AUTHORING
     ✅ P1 — authored + tested (PASS)
     ✅ P2 — authored + tested (PASS)
     ✍  P3 — authored, not yet tested
     --  P4 — not yet started
     --  P5 — not yet started
   ```
3. Continue with the first incomplete puzzle:
   - If authored but untested → run `/puzzle <id> test`
   - If not started → run `/puzzle <id> author` then `/puzzle <id> test`
   - If REVISE → run `/puzzle <id> test iterate`

Stage 6 is complete when every puzzle in `PUZZLES.md` shows PASS.

---

## Updating CLAUDE.md

After completing each stage, update the scenario `CLAUDE.md`:
- Change `--` to `Done` in the pipeline status table
- Add notes (file name, puzzle count, test scores, anything useful)
- Save before moving to the next stage

This is what makes `/hunt resume` safe to call repeatedly — the CLAUDE.md is always authoritative.

---

## On Crash or Partial Completion

If a stage is partially done (some deliverables exist but the stage isn't marked Done):

1. Check what exists in the file system
2. Do not redo work that's already complete
3. Complete only what's missing
4. Update CLAUDE.md and proceed

Example: Stage 6 is not marked Done, but 4 of 6 puzzles have authored files and 3 have PASS test results. Resume picks up from puzzle 4 (authored, needs testing) — it does not re-author puzzles 1-3.

---

## Flags

`/hunt resume status` — read-only. Shows the state summary without proceeding. Good for orientation after a crash without committing to any action.

`/hunt resume stage <N>` — forces a specific stage. Use when you want to redo a stage (e.g., you changed the meta and need to re-run Stage 5) or when the CLAUDE.md status is out of sync with reality.
