# Puzzle Hunt Toolkit

Build puzzle hunts with Claude Code. Plug in any content library — an encyclopedia, a textbook, a codebase, a museum collection — and create a puzzle hunt around it.

---

## Quick Start

```bash
# 1. Copy this toolkit directory somewhere
cp -r toolkit/ ~/my-puzzle-hunt/

# 2. Install the skills
cp -r skills/* ~/.claude/skills/

# 3. Create your scenario directory
mkdir -p scenarios/my-hunt/{puzzles,reviews,tests,meta}

# 4. Start Claude Code
cd ~/my-puzzle-hunt
claude

# 5. Begin designing
/puzzle-plan
```

---

## What's in the Toolkit

| File/Directory | Purpose |
|---------------|---------|
| `CLAUDE.md` | This file — Claude reads it automatically |
| `PRINCIPLES.md` | 20 design principles with tests (the quality bar) |
| `GETTING-STARTED.md` | Step-by-step tutorial (10 steps from blank to ship) |
| `HINTS.md` | Hint system design template |
| `profiles/` | 12 expert reviewer personas for blind testing |
| `skills/hunt/` | Hunt-level skills (plan, review, status, meta, admin) |
| `skills/puzzle/` | Puzzle-level skills (manage, author, test) |
| `templates/` | Puzzle page template + 20 puzzle type guides |

---

## Skills — Two Namespaces

### `/hunt` — Hunt-level (the admin runs these)

| Command | What it does |
|---------|-------------|
| `/hunt plan` | 11-stage design workflow with review gates |
| `/hunt world` | Fictional universe design — canon, data tables, lock protocol |
| `/hunt review full <file>` | 12-expert panel reviews any document |
| `/hunt review rank <file>` | Panel ranks a puzzle pool |
| `/hunt resume` | Resume pipeline from next incomplete stage (crash-safe) |
| `/hunt publish` | Build clean solver-facing distribution zip (strips answers, working files) |
| `/hunt status` | Pipeline dashboard |
| `/hunt meta` | Meta design, verification, grid building |
| `/hunt edit` | Editorial review of author submissions before blind testing |
| `/hunt print` | Generate print-ready PDFs for puzzles, props, labels, game manual |
| `/hunt props` | Physical asset logistics — inventory, team kits, distribution, day-of checklist |
| `/hunt site` | Hunt website — scaffold, theme, puzzle pages, standings, answer submission |
| `/hunt modules` | Module assignment and tracking |
| `/hunt authors` | Author registry and workload |
| `/hunt schedule` | Build schedule and dependencies |
| `/hunt checklist` | Pre-ship integration checklist |
| `/hunt onboard` | Generate brief for a new author |
| `/hunt honor <callsign>` | Claim a NATO phonetic callsign |

### `/puzzle` — Puzzle-level (authors use these)

| Command | What it does |
|---------|-------------|
| `/puzzle <id>` | Overview — brief, status, scores, history |
| `/puzzle <id> brief` | View/edit the full puzzle brief |
| `/puzzle <id> author` | Write the puzzle from its brief |
| `/puzzle <id> test` | 3 experts solve it blind, score it |
| `/puzzle <id> test iterate` | Fix and retest until passing (≥22/30) |
| `/puzzle <id> check` | Run against 18 design principles |
| `/puzzle <id> comment <text>` | Add a note |
| `/puzzle <id> status <code>` | Update status |
| `/puzzle list` | List all puzzles with status |
| `/puzzle board` | Kanban view |

---

## The Pipeline

```
Stage 1:  SCOPE           → what's the hunt about?
  ↓ review gate
Stage 2:  STRUCTURE       → rounds, puzzle counts, metas
  ↓ review gate
Stage 3:  PUZZLE POOL     → brainstorm candidates
  ↓ review gate (panel ranks)
Stage 4:  ASSIGNMENT      → assign puzzles to slots
  ↓ review gate
Stage 5:  META DESIGN     → how feeder answers combine
  ↓ review gate
Stage 6:  AUTHORING       → write every puzzle
  ↓ testing gate (blind test each)
Stage 7:  EDITORIAL       → admin reviews submissions (/hunt edit)
  ↓ edit gate
Stage 8:  INTEGRATION     → assemble, verify crossings
  ↓ review gate
Stage 9:  DELIVERY BUILD  → website, print, UX components
  ↓ build gate
Stage 10: PLATFORM TEST   → puzzles work in actual delivery medium
  ↓ test gate
Stage 11: POLISH          → final pass, hints, answer encoding
  ↓ ship it
```

Each gate is a checkpoint. The expert panel evaluates before you proceed. You can loop back to any earlier stage.

---

## The Expert Panel

12 reviewer personas, each with a documented design philosophy. Claude reads each profile and evaluates from that perspective.

| # | Name | Lens | Origin |
|---|------|------|--------|
| 1 | Dan Katz | Structure & pacing | MIT Mystery Hunt (8 wins) |
| 2 | Thomas Snyder | Puzzle craftsmanship | 3x World Sudoku Champion |
| 3 | Mike Selinker | Narrative & experience | Lone Shark Games, Puzzlecraft |
| 4 | Wei-Hwa Huang | Deductive rigor | 4x World Puzzle Champion |
| 5 | Kenny Young | Buildability | 24-year MS Puzzlehunt veteran |
| 6 | Dana Young | Craft & accessibility | 25-year MS Puzzlehunt veteran |
| 7 | Peter Sarrett | Experience design | "Chicago Fire" puzzle, Puzzlehop |
| 8 | Mark Gottlieb | Systems engineering | MIT thesis on puzzle hunt theory |
| 9 | Alex Rosenthal | Accessibility & wonder | TED-Ed, TED Games |
| 10 | Rand Miller | World-as-puzzle | Myst, Cyan Worlds |
| 11 | Jonathan Blow | Epiphany design | Braid, The Witness |
| 12 | Lucas Pope | Deductive identification | Papers Please, Obra Dinn |

---

## 20 Design Principles (Summary)

The full list with sources and tests is in `PRINCIPLES.md`. The top 5:

1. **The Riven Standard** — the puzzle IS what the field does, not overlaid on it
2. **Solving = Proving Understanding** — the solver knows more after solving
3. **Blame the Player** — every clue is fair in retrospect
4. **No Over-Scaffolding** — worksheets provide space, not instructions
5. **No Computation Without Deduction** — pure-computation puzzles always fail testing

---

## Your Scenario

Create a directory for your hunt:

```
scenarios/
└── my-hunt/
    ├── SCOPE.md       ← Stage 1 (copy from GETTING-STARTED.md prompts)
    ├── ROUNDS.md      ← Stage 2
    ├── PUZZLES.md     ← Stage 4 (master registry — puzzles, testers, status)
    ├── HINTS.md       ← Stage 8
    ├── meta/          ← Stage 5
    ├── puzzles/       ← Stage 6 (authored puzzle pages)
    ├── reviews/       ← panel output
    └── tests/         ← blind test results
```

Tell Claude: "Let's work on the my-hunt scenario." All operations target that directory.

**Important:** Every scenario needs a `world/` directory with verified reference data. This is the knowledge base puzzles are built on. See `world/WORLD.md` for the overview and data files for specific domains. Authors verify all puzzle facts against world/ files — not memory.

---

## Answer Security

**Plaintext answers must NEVER appear in git-tracked files.** They're searchable in history forever.

During `/puzzle-plan` Stage 1, choose your encoding system:

| Option | How it works | Pros | Cons |
|--------|-------------|------|------|
| **ROT13** | Shift each letter 13 positions | Universal, trivial to decode | Well-known, easy to crack |
| **Base64** | Standard encoding | Looks like gibberish, any tool decodes | Not thematic |
| **Custom cipher** | Your own mapping (A→?, B→?, etc.) | Thematic, unique to your hunt | Must document the key |
| **Don't store answers** | Keep them only in your head | Maximum security | Risky if you forget |

Store encoded answers in `.claude/` project memory (gitignored), not in the repo. Document your encoding key in `.claude/` as well — never in a committed file.

---

## Extending the Toolkit

- **Add reviewer personas**: create a new profile in `profiles/` following the existing format
- **Add puzzle types**: add to `templates/TYPES.md`
- **Add principles**: add to `PRINCIPLES.md` with source, test, and priority position
- **Customize the pipeline**: edit the stages in `skills/puzzle-plan/SKILL.md`
