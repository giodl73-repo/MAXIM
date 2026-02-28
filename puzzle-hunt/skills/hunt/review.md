# /puzzle-review — Expert Panel Review for Puzzle Hunt Design

Run a 9-expert review panel against any puzzle hunt design document. Each reviewer evaluates from a distinct lens, scores puzzles, and produces a ranked lineup. Results are synthesized into a consensus punchlist.

## Usage

```
/puzzle-review full <file>           — full 9-reviewer panel against a design document
/puzzle-review rank <file>           — 9 reviewers rank a puzzle pool (pick best per slot)
/puzzle-review single <name> <file>  — one specific reviewer evaluates a document
/puzzle-review synthesize            — synthesize most recent reviews into consensus punchlist
/puzzle-review panel                 — list the 9 reviewers and their lenses
```

---

## The Panel

9 expert reviewers. Profiles stored in `toolkit/profiles/`. Each brings a distinct, non-overlapping lens.

| # | Name | Lens | Profile |
|---|------|------|---------|
| 1 | **Dan Katz** | Structure & pacing | `toolkit/profiles/dan-katz.md` |
| 2 | **Thomas Snyder** | Individual puzzle craftsmanship | `toolkit/profiles/thomas-snyder.md` |
| 3 | **Mike Selinker** | Narrative & experience architecture | `toolkit/profiles/mike-selinker.md` |
| 4 | **Wei-Hwa Huang** | Deductive rigor & solve-path quality | `toolkit/profiles/wei-hwa-huang.md` |
| 5 | **Kenny Young** | Infrastructure & buildability | `toolkit/profiles/kenny-young.md` |
| 6 | **Dana Young** | Craft, presentation & accessibility | `toolkit/profiles/dana-young.md` |
| 7 | **Peter Sarrett** | Experience design & physicality | `toolkit/profiles/peter-sarrett.md` |
| 8 | **Mark Gottlieb** | Systems engineering & academic rigor | `toolkit/profiles/mark-gottlieb.md` |
| 9 | **Alex Rosenthal** | Accessibility & wonder | `toolkit/profiles/alex-rosenthal.md` |

### Coverage Matrix

| Concern | Primary | Secondary |
|---------|---------|-----------|
| Hunt structure, sizing, pacing | Dan Katz | Mark Gottlieb |
| Individual puzzle elegance | Thomas Snyder | Wei-Hwa Huang |
| Narrative integration | Mike Selinker | Alex Rosenthal |
| Solve-path deductive rigor | Wei-Hwa Huang | Thomas Snyder |
| Buildability / construction | Kenny Young | Dana Young |
| Visual / presentation quality | Dana Young | Peter Sarrett |
| Accessibility to non-experts | Alex Rosenthal | Dana Young |
| Experience / delight / surprise | Peter Sarrett | Mike Selinker |
| Systemic consistency | Mark Gottlieb | Dan Katz |
| Physical / medium interaction | Peter Sarrett | Kenny Young |

---

## Modes

### `/puzzle-review full <file>`

Full panel review. All 9 reviewers read the target file (plus supporting context) and write independent reviews.

**Process:**
1. Read the target design document
2. Read all 9 profiles from `toolkit/profiles/`
3. Read supporting context: `[scenario CLAUDE.md — read for hunt structure]`, `cards/ROLES.md`, `cards/CONCEPTS.md`
4. Launch 9 parallel agents (one per reviewer), each with:
   - The reviewer's profile
   - The design document
   - The supporting context
   - Instructions to review FROM THAT REVIEWER'S PERSPECTIVE using their documented philosophy
5. Each agent saves its review to `reviews/[round]-[name].md`
6. After all 9 complete, run synthesis (see `/puzzle-review synthesize`)

**Agent prompt template for each reviewer:**
```
You are simulating a review from [NAME] — [CREDENTIALS].

Read these files:
1. [TARGET DOCUMENT]
2. [PROFILE PATH] — [Name]'s profile and philosophy
3. [scenario CLAUDE.md — read for hunt structure] — the two-book structure
4. cards/ROLES.md — the card/archetype structure

Write a thorough review FROM [NAME]'S PERSPECTIVE using their documented
philosophy. Their lens is [LENS DESCRIPTION].

Key [NAME] concerns: [LIST FROM PROFILE]

[MODE-SPECIFIC INSTRUCTIONS]

Save to: reviews/[round]-[name].md
```

**Agent settings:**
- `mode: "bypassPermissions"` — agents need to write review files
- `run_in_background: true` — all 9 run in parallel
- Each agent reads the profile to absorb the reviewer's voice and concerns

### `/puzzle-review rank <file>`

Ranking mode. Each reviewer picks their ideal lineup from a pool of candidates.

**Additional instructions per reviewer:**
- For each slot/section, pick top 2-3 candidates and explain why
- Score each pick on the reviewer's primary dimensions
- Flag any puzzles that should be eliminated (fundamentally flawed)
- End with "[Name]'s [Adjective] 13" — their ideal lineup
- Include top 3-5 picks for physical/cross-section puzzles

### `/puzzle-review single <name> <file>`

Run a single reviewer. Useful for quick feedback or testing changes.

**Valid names:** `katz`, `snyder`, `selinker`, `huang`, `kenny`, `dana`, `sarrett`, `gottlieb`, `rosenthal`

**Name → profile mapping:**
| Short name | Full name | Profile path |
|-----------|-----------|-------------|
| katz | Dan Katz | toolkit/profiles/dan-katz.md |
| snyder | Thomas Snyder | toolkit/profiles/thomas-snyder.md |
| selinker | Mike Selinker | toolkit/profiles/mike-selinker.md |
| huang | Wei-Hwa Huang | toolkit/profiles/wei-hwa-huang.md |
| kenny | Kenny Young | toolkit/profiles/kenny-young.md |
| dana | Dana Young | toolkit/profiles/dana-young.md |
| sarrett | Peter Sarrett | toolkit/profiles/peter-sarrett.md |
| gottlieb | Mark Gottlieb | toolkit/profiles/mark-gottlieb.md |
| rosenthal | Alex Rosenthal | toolkit/profiles/alex-rosenthal.md |

### `/puzzle-review synthesize`

Synthesize the most recent round of reviews into a consensus document.

**Process:**
1. Find the most recent round of reviews in `reviews/` (by filename prefix)
2. Read all reviews from that round
3. Produce a synthesis document with:
   - **Consensus findings** (5+ reviewers agree)
   - **Per-puzzle verdicts** (aggregate scores, KEEP/REDESIGN/REPLACE)
   - **Meta assessment** (if applicable)
   - **Structural recommendations**
   - **Priority action items** (P0-P3)
   - **Disagreements** (where reviewers contradict each other)
4. Save to `reviews/[ROUND]-SYNTHESIS.md`

### `/puzzle-review panel`

Display the panel roster, credentials summary, and coverage matrix. No agents launched — just reads and displays `toolkit/profiles/ (list all .md files)`.

---

## Review Naming Convention

Reviews are named: `reviews/[round]-[name].md`

| Round prefix | Meaning |
|-------------|---------|
| (no prefix) | Round 1 (V1 design, historical) |
| round2- | Round 2 (89-puzzle pool ranking) |
| round3- | Round 3 (next review cycle) |
| roundN- | Round N |

The synthesis file is named: `reviews/ROUNDN-SYNTHESIS.md`

---

## Reviewer Philosophy Quick Reference

For constructing review prompts, here are the key concerns per reviewer (full details in profiles):

**Dan Katz** — "Hunt. Is. Too. Long." 80% rule for metas. Anti-mettleneck. Backsolving as safety valve. Write for the middle, not elites. Narrative woven into solving.

**Thomas Snyder** — Hand-crafted supremacy. Intentional solving paths. Themes are structural, not cosmetic. Anti-computer-generation. Every element serves a purpose. Championship standards.

**Mike Selinker** — Narrative is load-bearing. High-tension memorable moments. Personality in design. Self-running systems. "Be the person known for that thing." The Dinner Party Test.

**Wei-Hwa Huang** — Intended solution must stand out. Anti-guessing. Clean deductive paths. Skill isolation. Combinatorial craft, not random encoding. Confirmation checkpoints.

**Kenny Young** — Buildability. Seed quality (one core idea). Practical construction labor. Fragility to edits. Prototype first. "If the Morse lines look forced, fall back."

**Dana Young** — Visual integration. On-ramp for newcomers. Honor the host medium. Long-game durability. Seamlessness. The "book test" — can you solve it with just the book and a pencil?

**Peter Sarrett** — "Chicago Fire" moments. Trust the player. Kill sacred pillars. Environmental design. Reading Reward dimension. Focus on what players are already doing. Medium IS the puzzle.

**Mark Gottlieb** — Structural soundness. Consistency across the system. Edge cases (Rules Manager instinct). Theoretical coherence. The Karlov Manor parallel. Academic rigor.

**Alex Rosenthal** — The TED-Ed Test ("explain in one sentence, non-puzzler says 'wait, really?'"). Joy and wonder. Accessibility. Community expansion. Virality. "Puzzles are everywhere." Magic vs. arts-and-crafts.

---

## Context Files

These files should be provided to reviewers as supporting context (in addition to the target document):

| File | Purpose |
|------|---------|
| `[scenario CLAUDE.md — read for hunt structure]` | Two-book structure, Elements vs Compounds framing |
| `PUZZLES.md (scenario's master registry)` | Complete 52-puzzle assignment |
| `ROUNDS.md (scenario's structure)` | Periodic table framing, numerology |
| `CLAUDE.md (scenario's voice guide)` | Narrative voice guide |
| `meta/META-DESIGN.md (scenario's meta design)` | Black Joker: The Grid + synthesis puzzles |
| `cards/ROLES.md` | 52 archetype roles |
| `cards/CONCEPTS.md` | 52 card image concepts |

Not all context files are needed for every review. Use judgment:
- For a full design review: TWO-JOKERS + FINAL-52 + ROLES
- For a puzzle pool ranking: PUZZLE-POOL + TWO-JOKERS + ROLES
- For a narrative review: JOKER-VOICE + TWO-JOKERS + CONCEPTS

---

## Adding Reviewers

To add a new reviewer to the panel:

1. Create a profile at `toolkit/profiles/[name].md` following the existing format:
   - Identity (role, affiliation, credentials)
   - Puzzle hunt credentials (specific hunts, wins, innovations)
   - Design philosophy (documented positions, published writing)
   - Review lens (what they evaluate, their key questions)
   - Key sources (links to their work)
2. Add them to `toolkit/profiles/ (list all .md files)`
3. Update the panel table and coverage matrix in this skill file
4. The skill supports up to 12 reviewers (a full puzzle hunt team)
