# /hunt publish — Build a Clean Solver-Facing Distribution

Package a hunt for distribution. Strips all working pipeline files and answer content, leaving only what a solver should see. Produces a zip ready to send.

## Usage

```
/hunt publish              — build solver zip for current scenario
/hunt publish dry-run      — show what would be included/excluded without writing
/hunt publish all          — package all scenarios in the scenarios/ directory
```

---

## What Gets Included

| File/Directory | Include? | Notes |
|---------------|----------|-------|
| `puzzles/*.md` | ✅ Scrubbed | Answer lines, solution sections, author notes removed |
| `world/` | ✅ As-is | Solvers may reference world data |
| `delivery/` | ✅ As-is | Site HTML, print assets, prop specs — already solver-facing |
| `SCOPE.md` | ✅ As-is | Sets the theme and framing |
| `ROUNDS.md` | ✅ As-is | Round/puzzle structure (no answers) |
| `meta/` | ❌ Excluded | Contains full answer extraction tables |
| `ANSWERS.md` | ❌ Excluded | Answer key |
| `PUZZLES.md` | ❌ Excluded | Briefs contain target answer words |
| `PUZZLE-POOL.md` | ❌ Excluded | May contain answer words |
| `reviews/` | ❌ Excluded | Editorial reviews reference answers |
| `tests/` | ❌ Excluded | Test results reference answers |
| `CLAUDE.md` | ❌ Excluded | Pipeline status tracker with answer notes |
| `SCENARIO.md` | ❌ Excluded | Dev brief |
| `BUGS-local.md` | ❌ Excluded | Dev notes |

---

## Puzzle File Scrubbing Rules

For each puzzle `.md` file, remove:

1. **Answer lines** — any line containing `Answer:` (case-insensitive)
2. **ROT13 lines** — any line containing `ROT13:`
3. **Verification notes** — trailing author notes after the final `---` separator that contain slot positions, super-meta extraction notes, or scoring
4. **Solution Space content** — keep the `## Solution Space` heading but replace filled-in answers with blank lines for the solver
5. **Solutions sections** — remove `### Solutions` and all content below it
6. **Author metadata** — lines like `*Author: The Methodical*` at the top

Replace removed answer content with appropriate blank work space:
- Extraction tables: replace letter column with `?`
- Solution grids: replace values with `___`
- Answer line: replace with `**Answer:** _ _ _ _ _`

---

## Special Cases

**Magazine format** (e.g., Games Magazine): Keep the solutions page — solutions belong in the back of a magazine. Scrub answer lines from individual puzzle pages only.

**Physical-first hunts** (e.g., Grand Larceny): Puzzle files that already use blanks (`_ _ _ _`) need minimal scrubbing. Verify and pass through.

**World data**: Include as-is. Solvers are expected to reference world/ files — that's how the hunt works.

---

## Answer Leak Verification

After scrubbing, grep the output directory for known answer words before packaging:

```
grep -ri "answer:" output/ | grep -v "_ _ _"  → should return nothing
```

Also spot-check 3 random puzzle files to confirm they're clean.

If any leaks are found, fix them before proceeding.

---

## Output

Creates `[scenario-name]-solver.zip` in the project root, or `solver-hunts.zip` if packaging multiple scenarios.

Log what was included, excluded, and scrubbed in a brief publish report.

---

## Backport Reminder

After writing this skill, copy it to `~/.claude/skills/hunt-publish/SKILL.md` in the reference library.
