# /puzzle-plan — Design a Puzzle Hunt

Walk through the complete design process for a puzzle hunt, from blank page to construction-ready plan. Each stage has a review gate — the expert panel evaluates before you proceed.

## Universal Rule: Update CLAUDE.md

**Every skill that produces a deliverable MUST update the scenario's CLAUDE.md.**

After completing any stage or action:
1. Read the scenario's `CLAUDE.md`
2. Update the file status table (mark the stage ✅)
3. Add any new notes (answer count, test scores, revision status)
4. Save

This keeps the scenario CLAUDE.md as the single source of truth. Any Claude instance opening the scenario sees the current state immediately.

## Usage

```
/puzzle-plan                    — start from scratch (guided walkthrough)
/puzzle-plan library <path>     — set the content library path
/puzzle-plan stage              — show current stage and what's next
/puzzle-plan stage <N>          — jump to a specific stage
```

---

## The 8 Stages

Each stage produces a deliverable. Each gate requires a panel review before proceeding. You can loop back to any earlier stage if the review surfaces issues.

```
Stage 1: SCOPE           → what's the hunt about?
    ↓ review gate
Stage 2: WORLD BUILDING  → research and verify the knowledge base
    ↓ review gate
Stage 3: STRUCTURE       → how many rounds, puzzles, metas?
    ↓ review gate
Stage 4: PUZZLE POOL     → brainstorm all candidate puzzles
    ↓ review gate (panel ranks the pool)
Stage 5: ASSIGNMENT      → assign puzzles to slots
    ↓ review gate
Stage 6: META DESIGN     → design meta puzzles for each round
    ↓ review gate
Stage 7: AUTHORING       → write every puzzle
    ↓ testing gate (blind test each puzzle)
Stage 8: INTEGRATION     → assemble into books/rounds, verify crossings
    ↓ review gate
Stage 9: POLISH          → final pass, answer verification, difficulty curve
    ↓ ship it
```

---

## Stage 1: SCOPE

**Goal:** Define the hunt's identity.

**Questions to answer:**
- What content library does this hunt use? (path, structure, size)
- Who is the audience? (solo puzzler? team of 12? general public?)
- What's the theme/framing? (deck of cards? periodic table? mythology? custom?)
- What's the tone? (friendly guide? cryptic challenge? competitive?)
- What's the scale? (10 puzzles? 50? 100?)
- Is there a narrative? (narrator character? story arc?)
- Physical format? (book? website? hybrid?)

**Deliverables:**
1. `SCOPE.md` — one page capturing all decisions
2. `CLAUDE.md` — **auto-generated** scenario CLAUDE.md containing:
   - Hunt summary table (name, theme, scale, audience, format)
   - Content library path and description
   - Narrator voice rules (tone, catchphrase, constraints)
   - Content domains → puzzle type mapping
   - File status table (all 8 stages, initially "—" except Stage 1 "✅")
   - Toolkit path references
   - Claude instructions specific to this scenario

The scenario CLAUDE.md is the **persistent context file**. Every subsequent skill:
- READS it to know the hunt's identity, voice, and state
- UPDATES it when producing deliverables (marking stages ✅, adding notes)

**Review gate:** `/hunt review full SCOPE.md` — panel evaluates scope for feasibility, audience fit, and narrative coherence.

---

## Stage 2: WORLD BUILDING

**Goal:** Research and verify the knowledge base the hunt is built on. Every fact a puzzle will use must live here.

**Process:**
1. Create `world/` directory in the scenario
2. Create `world/WORLD.md` — overview listing all data domains
3. For each content domain in the hunt, create a reference file:
   - Identify the key facts, rules, data tables, relationships
   - Research thoroughly (game wikis, official docs, encyclopedias, primary sources)
   - Format as clean, scannable tables
   - Mark uncertain facts with `[VERIFY]`
4. Cross-check: does every puzzle concept from the SCOPE have supporting data?

**Questions to answer:**
- What are the content domains? (For AoE: civilizations, units, techs, maps, economy)
- What's the primary source? (Game data? Encyclopedia? Official docs?)
- How much data does each puzzle need? (A matching puzzle needs 8+ entries. A calculation puzzle needs exact numbers.)
- Are there conflicts between sources? (Different game versions, errata, community disputes)

**Deliverables:**
1. `world/WORLD.md` — overview with data file index and verification rules
2. `world/*.md` — one file per domain, with verified reference tables
3. Updated scenario `CLAUDE.md` (Stage 2 ✅, world/ files listed)

**Quality bar:** An author who has never played the game (or read the encyclopedia) should be able to write a factually correct puzzle using ONLY the world/ files.

**Review gate:** `/hunt review full world/WORLD.md` — panel evaluates completeness and accuracy. Gottlieb checks for systemic consistency. Rosenthal checks accessibility (is enough context given for non-experts?).

---

## Stage 3: STRUCTURE

**Goal:** Define rounds, puzzle counts, and meta architecture.

**Flexible structures the toolkit supports:**

### Single-round (simplest)
```
N puzzles → 1 meta → final answer
```

### Multi-round (MIT Mystery Hunt style)
```
Round 1: N puzzles → meta 1
Round 2: N puzzles → meta 2
Round 3: N puzzles → meta 3
...
All round metas → super-meta → final answer
```

### Two-book (Red/Black Joker style)
```
Book 1: N individual puzzles → meta 1
Book 2: N synthesis puzzles → meta 2
Both metas → combined final answer
```

### Progressive unlock
```
Solve puzzles to unlock new rounds
Meta answers from early rounds are inputs to later rounds
```

**Questions to answer:**
- How many rounds?
- How many puzzles per round?
- Does each round have a meta?
- Is there a super-meta / meta-meta?
- How do rounds relate to each other? (independent? sequential? interlocking?)
- What's the difficulty curve across rounds?
- What's the numbering system? (sequential? thematic? encoded?)

**Deliverable:** `STRUCTURE.md` — round map, puzzle counts, meta architecture, numbering.

**Review gate:** `/puzzle-review full STRUCTURE.md` — panel evaluates structure for pacing (Katz), meta robustness (Huang), narrative arc (Selinker), buildability (Kenny).

---

## Stage 4: PUZZLE POOL

**Goal:** Generate more puzzle ideas than you need. The panel will rank them.

**Process:**
1. For each round/section, brainstorm 3-5 candidate puzzles
2. For each candidate: name, one-line pitch, mechanism, section reference, estimated difficulty
3. Include physical/visual puzzles, cross-section puzzles, identification puzzles, construction puzzles — variety is key
4. Don't self-censor — bad ideas spark good ones

**Deliverable:** `PUZZLE-POOL.md` — all candidates with one-line briefs.

**Review gate:** `/puzzle-review rank PUZZLE-POOL.md` — each reviewer picks their ideal lineup per round. Consensus emerges. See which puzzles land on 8+ of 12 lists (locks) vs. 4-7 (contenders) vs. 0-3 (cut).

---

## Stage 5: ASSIGNMENT

**Goal:** Assign specific puzzles to specific slots based on pool rankings.

**Process:**
1. Take the consensus locks from Stage 3
2. Fill remaining slots from contenders
3. Verify: mechanism variety (no two puzzles use the same type), difficulty curve (ramps per round), visual variety (grids, diagrams, text, physical)
4. Assign each puzzle: answer word, section reference, puzzle type, round placement

**Deliverable:** `ASSIGNMENT.md` — the complete puzzle-to-slot mapping.

**Review gate:** `/puzzle-review full ASSIGNMENT.md` — panel evaluates the full assignment for systemic coherence (Gottlieb), variety (Snyder), buildability (Kenny), experience arc (Selinker).

---

## Stage 6: META DESIGN

**Goal:** Design the meta puzzle(s) that combine feeder answers.

**Meta types supported:**
- **Crossword:** feeder answers fill a grid, highlighted squares spell the meta answer
- **Acrostic:** first letters of feeder answers spell the meta answer
- **Pattern recognition:** feeder answers share a hidden property
- **Jigsaw:** feeder answers are pieces that assemble into something
- **Elimination:** multiple candidate answers, evidence narrows to one (Clue-style)
- **Physical:** assemble a 3D object, overlay pages, punch card
- **Custom:** design your own

**For multi-round hunts:** design each round's meta AND the super-meta. The super-meta should use round-meta answers as inputs.

**Deliverable:** `meta/META-DESIGN.md` — mechanism, answer words, extraction method, verification that the meta is solvable with 80% of feeders (Katz's rule).

**Review gate:** `/puzzle-review full meta/META-DESIGN.md` — panel evaluates meta solvability (Katz 80% rule), deductive rigor (Huang), narrative payoff (Selinker), backsolving potential (Katz).

---

## Stage 7: AUTHORING

**Goal:** Write every puzzle.

**Process:**
For each puzzle in the assignment:
1. `/puzzle-author <puzzle-id>` — writes the full puzzle page
2. Verify against PRINCIPLES.md (18 design principles)
3. `/puzzle-test <puzzle-id>` — 3 blind testers score it
4. If PASS (≥22/30, all dimensions ≥4) → done
5. If REVISE → fix issues, retest (max 3 iterations)
6. If REDESIGN → go back to pool, pick alternate

**Deliverable:** Complete puzzle files in `puzzles/` with test results in `tests/`.

**Testing gate:** Every puzzle must pass blind testing before proceeding. No exceptions. The principles are the bar.

---

## Stage 8: INTEGRATION

**Goal:** Assemble puzzles into the final hunt format.

**Checklist:**
- [ ] All puzzles pass testing
- [ ] Meta crosswords/grids are constructable with the actual answer words
- [ ] Difficulty curve verified across each round
- [ ] Answer words verified (no duplicates, no unintended overlaps)
- [ ] Physical puzzles verified (templates print correctly)
- [ ] Narrative elements written (intro, per-puzzle flavor, closing)
- [ ] Numbering verified (no collisions, gaps are intentional)
- [ ] Cross-references verified (if puzzles interlock across rounds)

**Deliverable:** Assembled hunt in `puzzles/` with navigation/ordering.

**Review gate:** `/puzzle-review full` on the complete assembled hunt — full panel pass, Gottlieb's system integrity check, Dana's visual/physical assessment.

---

## Stage 9: LIVE TEST

**Goal:** Simulate a full team solving the hunt end-to-end.

**Three teams, three stages of testing:**

### Team 1: Design Team (Stages 4-7)
Selected during `/hunt plan` Stage 4. The admin picks 12 reviewers from the 29-profile panel who best match the hunt's content domains. These reviewers evaluate puzzle briefs, rank the pool, and blind-test individual puzzles during authoring. **The admin can change the roster** between stages — different experts for different puzzles.

### Team 2: Beta Testers (Stage 8)
Same 12-person panel roster, but now they test the ASSEMBLED hunt (not individual puzzles). They see the full round structure, difficulty curve, and meta. They test integration, not just individual puzzles. **The admin can swap reviewers** if domain expertise is needed.

### Team 3: Live Solve Simulation (Stage 9) — THE REAL TEST
**12 fresh agents simulate a real team solving the hunt.**

This is NOT expert review. This is a play-test. 12 agents are spawned, each with a DIFFERENT solver personality:

| Agent | Personality | Behavior |
|-------|-----------|----------|
| Captain | Organized, delegates, tracks progress | Assigns puzzles to team members |
| Speedster | Grabs puzzles fast, solves quickly, sometimes wrong | First to attempt, first to get stuck |
| Methodical | Slow, thorough, rarely wrong | Takes 3x longer but never needs revision |
| Lateral | Makes unexpected connections, sees meta patterns early | Skips feeders, jumps to meta prematurely |
| Newbie | First puzzle hunt, needs hand-holding | Tests accessibility — if they're lost, the hunt fails |
| Specialist | Deep knowledge in 1-2 domains, useless elsewhere | Tests domain balance |
| Social | Talks to everyone, shares partial answers | Tests whether sharing helps or hurts |
| Skeptic | "This clue must be wrong" — tests robustness | Finds edge cases and alternate interpretations |
| Artist | Focuses on physical/visual puzzles, ignores text-heavy ones | Tests if the hunt works for visual learners |
| Sprinter | Wants to finish fast, skips hard puzzles | Tests 80% rule — can you get the meta without 100%? |
| Lurker | Reads everything, says nothing, solves alone | Tests solo experience within a team |
| Cheerleader | Celebrates every solve, keeps morale up | Tests emotional arc — is the hunt FUN? |

**How it works:**
1. All 12 agents are spawned in parallel
2. The Captain assigns puzzles (or agents self-select)
3. Each agent works in character — solving, getting stuck, asking for help, sharing answers
4. Agents update a shared solve-state file (which puzzles are solved, what answers are known)
5. When enough feeders are solved, agents attempt the meta
6. The simulation produces: solve order, time estimates, stuck points, team dynamics, meta discovery moment

**What it measures:**
- Total simulated solve time
- Which puzzles caused the most stuckness
- Whether the meta was discoverable with the team's partial answers
- Whether the Newbie could participate
- Whether the Sprinter could shortcut to the meta
- Whether the hunt was FUN (the Cheerleader's vibe check)

**Deliverable:** `tests/live-solve-simulation.md` — full transcript of the 12-agent solve with timing, dynamics, and recommendations.

**This is the final gate.** If the live simulation exposes problems, loop back to Stage 7 (fix puzzles) or Stage 6 (fix meta).

---

## Stage 10: POLISH

**Goal:** Final quality pass after live test.

- [ ] Answer verification: every puzzle's extraction produces the correct answer
- [ ] Difficulty curve: confirmed by live simulation
- [ ] Hint system: do you provide hints? If so, write them
- [ ] Answer confirmation: how does a solver know they got the right answer?
- [ ] Answer encoding: encode the master answer key (see CLAUDE.md § Answer Security)
- [ ] Print/publish prep: formatting, page breaks, templates
- [ ] Live test passed: no blocking issues from 12-agent simulation

**Deliverable:** Ship-ready hunt.

---

## Looping Back

Any review gate can send you back to an earlier stage:

- Pool review reveals structural problems → back to Stage 2
- Assignment review reveals meta incompatibility → back to Stage 5
- Puzzle testing reveals systemic issues → back to Stage 4
- Integration reveals missing pieces → back to Stage 6

This is normal. The pipeline is designed for iteration.

---

## Hunt Structures — Examples

### Small hunt (game night)
- 1 round, 8 puzzles, 1 meta
- Solo or team of 4
- 2-3 hours

### Medium hunt (weekend project)
- 3 rounds × 8 puzzles = 24 puzzles + 3 metas + 1 super-meta
- Team of 4-8
- Full weekend

### Large hunt (MIT/Microsoft scale)
- 6 rounds × 12 puzzles = 72 puzzles + 6 metas + 1 super-meta
- Team of 12-200
- 24-72 hours

### Two-book hunt (Red/Black Joker style)
- Book 1: 26 guided puzzles + meta
- Book 2: 26 synthesis puzzles + meta + physical builds
- Solo or team
- Multi-week

The toolkit scales to any of these. The principles and pipeline are the same regardless of size.
