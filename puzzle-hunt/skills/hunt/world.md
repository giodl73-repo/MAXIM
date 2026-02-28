# /hunt world — Fictional World Design

For hunts set in invented universes. Establishes canonical data before authoring begins. Authors verify against `world/` — not their memory, not each other's puzzle files.

## Usage

```
/hunt world init          — design the universe (genre, era, tone, core systems)
/hunt world systems       — define what data tables the world needs
/hunt world data <system> — populate a data table (bestiary, items, achievements, etc.)
/hunt world lock          — freeze world/ canon — no changes after authoring begins
/hunt world audit         — verify all puzzle files reference world/, not invented facts
```

---

## When to Use

Use during Stage 1–2, before assignment. For fictional hunts:

- **Stage 1 (SCOPE):** establish the universe concept — name, genre, era, tone, core hook
- **Stage 2 (STRUCTURE):** design the systems — what data tables will puzzles reference?
- **Before Stage 4 (ASSIGNMENT):** populate and lock all data tables authors will need

Do not assign puzzles until world/ is locked.

---

## The Fictional World Advantage

Real-world hunts are constrained by facts. Fictional worlds can be **designed for puzzle affordances**:

| Puzzle type you want | Design the world to have... |
|---------------------|----------------------------|
| Grid deduction | A bestiary with exactly N×M unique stat combinations |
| Logic puzzle | A crafting system with specific combination rules |
| Extraction | Achievement names where initials or hidden letters spell something |
| Spatial puzzle | A map with exactly the right topology |
| Identification | Characters/enemies with distinguishing traits that narrow uniquely |
| Meta | A "true ending" that requires specific inputs from feeder answers |

Design the world to fit the puzzles, not the other way around.

---

## /hunt world init

Guides design of the universe concept. Produces `world/WORLD.md`.

Ask:
1. What is the universe? (game, film, mythology, invented genre — be specific)
2. What is the era/aesthetic? (8-bit, grimdark, cozy, sci-fi, etc.)
3. What is the core dramatic hook? (what are solvers "doing" in this world?)
4. What are the 3–5 core systems? (the game mechanics / world rules)
5. What is the meta's target? (what does "solving the hunt" mean in-universe?)

Output:
```markdown
# [Universe Name] — World Overview

**Genre/Aesthetic:** [...]
**Hook:** [one sentence — what solvers are doing]
**Core systems:** [list]
**Meta target:** [what the super-meta solution represents in-universe]

## Tone
[paragraph — voice, register, how the world feels]

## Canon Rules
[bullet list of what is/isn't true in this universe]
```

---

## /hunt world systems

Lists the data tables the world needs, based on the puzzle pool.

For each planned puzzle, identify what data it references. Group into systems.

Example output for a 16-bit RPG:
```
WORLD SYSTEMS

System          Puzzles that reference it    Data needed
──────          ────────────────────────    ────────────
bestiary        P1 (grid deduction)          enemies × stats grid
items           P2 (crafting logic)          items × combination rules
achievements    P3 (extraction)              achievement names + descriptions
locations       P4 (map navigation)          region map + connections
battle system   P5 (mini-game)               move list, damage formulas
save file       P6 (pattern recognition)     save data format + fields
lore/story      P7, P8 (identification)      character bios, quest log
cheat codes     meta                         input sequences
```

---

## /hunt world data <system>

Populates one data table. Writes to `world/<system>.md`.

**Design checklist before writing the table:**
- [ ] Does it have the right number of entries for the puzzle mechanism?
- [ ] Are combinations/properties unique enough for deduction to work?
- [ ] Are names extractable? (initials, hidden letters, length patterns)
- [ ] Are the rules learnable from the data — can solvers infer the system?
- [ ] No accidental patterns that create unintended solutions?

---

## /hunt world lock

Freezes world/ canon. Writes `world/LOCKED.md` with timestamp.

After locking:
- No data table changes without admin approval
- Any change requires impact assessment: which puzzles reference the changed field?
- Changes logged in LOCKED.md with rationale

```markdown
# world/ Canon Lock

Locked: [date]
Systems locked: bestiary, items, achievements, locations, battle system, save file, lore

## Change Log
| Date | System | Change | Impact | Approved by |
|------|--------|--------|--------|------------|
```

---

## /hunt world audit

After authoring, verifies consistency. For each puzzle file:
- Does every named entity appear in world/?
- Do all stats/numbers match world/ data exactly?
- Are any facts invented (not in world/)?

Output:
```
WORLD AUDIT

P1 — bestiary: 12/12 entities verified ✓
P2 — items: 2 items not in world/items.md ✗ (Moonblade, Tether Scroll)
P3 — achievements: all verified ✓
...

ACTION REQUIRED: P2 author invented 2 items. Either add to world/ or revise puzzle.
```

---

## Directory Structure

```
world/
├── WORLD.md          ← universe overview, tone, canon rules
├── LOCKED.md         ← lock log and change history
└── systems/
    ├── bestiary.md
    ├── items.md
    ├── locations.md
    ├── characters.md
    ├── achievements.md
    ├── mechanics.md
    └── [any system the hunt needs]
```
