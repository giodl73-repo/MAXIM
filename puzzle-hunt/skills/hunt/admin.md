# /admin — Hunt Administration

Post-plan administration: modules, authors, scheduling, integration.

## Usage

```
/admin modules              — list all modules and their status
/admin modules assign <id> <author>  — assign a module to an author
/admin modules create <scope> <round> — create a new module
/admin authors              — list all authors and their workload
/admin authors add <name> <type>     — register a new author (human/ai)
/admin schedule             — show the build schedule (what's blocking what)
/admin checklist            — integration checklist (pre-ship)
/admin onboard              — generate an onboarding brief for a new author
/admin honor <callsign>     — claim a NATO phonetic callsign for a session
```

---

## /admin modules

Reads `MODULES.md` and displays:

```
MODULE REGISTRY

ID   Scope           Round  Author       Status         Puzzle(s)
───  ─────           ─────  ──────       ──────         ─────────
M1   single_puzzle   1      unassigned   unassigned     I
M2   single_puzzle   1      unassigned   unassigned     II
M3   single_puzzle   1      unassigned   unassigned     III
M4   single_puzzle   1      unassigned   unassigned     IV
M5   single_puzzle   1      unassigned   unassigned     V
M6   meta            1      unassigned   unassigned     ∞
```

## /admin modules assign <id> <author>

Updates MODULES.md and PUZZLES.md:
- Sets the module's author
- Updates the puzzle's assigned author
- Logs a comment on the puzzle: `[date] Assigned to <author> via module M<id>`

## /admin modules create <scope> <round>

Creates a new module row in MODULES.md with:
- Auto-incremented ID
- Scope (single_puzzle, round, meta, physical_build, narrative, testing_pass, ux_app, website, print_assets)
- Round assignment
- Status: unassigned

---

## /admin authors

Reads MODULES.md author registry:

```
AUTHOR REGISTRY

ID   Name              Type    Modules    Completed    Active
───  ────              ────    ───────    ─────────    ──────
A1   Claude Opus 4.6   ai      3          1            M2
A2   Kenny             human   0          0            —
```

## /admin authors add <name> <type>

Adds a row to the MODULES.md author registry. Type: `human` or `ai`.

## /admin onboard

Generates a brief for a new author joining the project:

```markdown
# Welcome to [Hunt Name]

You are author [name], assigned to Module [id].

## Your Module
- Scope: [single_puzzle / round / etc.]
- Puzzle(s): [list]
- Round: [number]

## What You Need
1. Read the scenario CLAUDE.md for hunt identity and voice rules
2. Read toolkit/PRINCIPLES.md for the 20 quality principles
3. Run `/puzzle <id> brief` to see your puzzle's full brief
4. Run `/puzzle <id> author` to start writing
5. Run `/puzzle <id> test` when done — target ≥22/30

## Your Toolkit
- `/puzzle <id>` — see everything about your puzzle
- `/puzzle <id> check` — verify against principles before testing
- `/puzzle <id> comment` — log notes and questions

## Questions?
Add comments via `/puzzle <id> comment` — the admin will see them.
```

---

## /admin schedule

Shows dependencies and blocking:

```
BUILD SCHEDULE

Week 1: Author puzzles I, II, III (parallel — no dependencies)
Week 2: Author puzzles IV, V (parallel)
Week 3: Test all 5 puzzles (can overlap with late authoring)
Week 4: Design meta (requires all 5 answer words locked)
Week 5: Test meta, integration, polish
```

Blocking chain:
- Meta design blocked until all 5 answer words are PASS
- Integration blocked until meta is PASS
- Ship blocked until integration review passes

---

## /admin checklist

Pre-ship integration checklist:

```
INTEGRATION CHECKLIST

[ ] All 5 puzzles: status = PASS or SHIP
[ ] Meta crossword: constructable with actual answer words
[ ] Meta: tested and passing
[ ] Answer words: no duplicates, no unintended overlaps
[ ] Difficulty curve: verified across the 5 puzzles
[ ] Narrator voice: consistent across all pages
[ ] Hints: written (if using hint system)
[ ] Answer encoding: all answers in ANSWERS.md, encoded
[ ] Physical elements: templates verified (if any)
[ ] PUZZLES.md: all statuses current
[ ] CLAUDE.md: all stages marked ✅
[ ] Final review: /hunt review on assembled hunt
```

---

## /admin honor <callsign>

Claims a NATO phonetic callsign for the current session.

1. Read MODULES.md honor table
2. Verify callsign is unclaimed
3. Write the transmission (one line — a clue for the 26-clue meta)
4. Update MODULES.md
5. Commit

---

## Data Sources

Reads/writes:
- `MODULES.md` — module registry, author registry, honor table
- `PUZZLES.md` — puzzle assignments, status updates
- Scenario `CLAUDE.md` — stage progress
