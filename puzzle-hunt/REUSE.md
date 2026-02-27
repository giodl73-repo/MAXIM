# REUSE — Library Asset Utilization in the Puzzle Hunt

How well is the puzzle hunt using what the library already built? Every asset scored 1-10.

**10** = the asset IS a puzzle mechanism. Fully load-bearing.
**7** = used meaningfully but could go deeper.
**5** = referenced but not structurally integrated.
**3** = mentioned in design docs but not in any puzzle.
**1** = exists in the library, completely ignored by the hunt.

---

## Major Assets

### The 52 Content Volumes (the encyclopedia itself)
**Current score: 9/10**
Every Red Joker puzzle sends the solver INTO the encyclopedia. The Codon puzzle requires reading molecular biology. The Cipher puzzle requires reading cryptography. The Star Chart requires reading astronomy. The encyclopedia IS the puzzle substrate.
**Gap**: Some Tier 2 puzzles reference sections shallowly (skim for keywords vs. genuine engagement). The Black Joker compound puzzles are still underspecified — many say "combine sections X and Y" without specifying WHAT in those sections to read.
**To reach 10**: Every puzzle should reference specific files, not just sections.

---

### Concept Index (`CONCEPT-INDEX.md`)
**Current score: 8/10** (was 1/10 before today)
The Concept Index mechanism (`CONCEPT-INDEX-MECHANISM.md`) makes the Index a puzzle lookup table. Numbers in compound puzzles are section references; the solver discovers the Index to find which concept spans those sections. Addresses Snyder's "15 of 26 compounds lack depth" critique.
**Gap**: Not yet verified that the Index has enough entries with unique section patterns. Not yet integrated into specific compound puzzles.
**To reach 10**: Verify uniqueness of section patterns. Assign specific concepts to specific compound puzzles. Confirm the Index is discoverable in the MkDocs navigation.

---

### Card System (`cards/ROLES.md`, `cards/CONCEPTS.md`)
**Current score: 8/10**
Each Red Joker puzzle invokes one of the 52 archetypes. Card IDs determine meta crossword slot placement. The Grid (Black Joker Puzzle 0) uses all 52 archetype names as the scavenger hunt target. The Joker's voice references archetypes in every puzzle intro.
**Gap**: Only 13 of 52 archetypes are directly invoked in Red Joker puzzles. The card IMAGE CONCEPTS (visual descriptions) are unused. The suit structure (♣♦♥♠) is not used in any puzzle mechanism.
**To reach 10**: Use suit identity in the meta mechanism. Use image concepts as visual clues. The 39 uninvoked archetypes should have subtle presence (even if not as puzzle anchors).

---

### Bill of Materials (`BILL-OF-MATERIALS.md`)
**Current score: 2/10**
The BOM catalogs every file in every volume. Currently not referenced by any puzzle.
**Potential**: The BOM is a MASTER TABLE with file counts, word counts, line counts per directory. Those numbers could be puzzle data — "which volume has exactly 17 files?" or word counts as encoding. It's the encyclopedia's own census.
**To reach 7**: Use BOM data in at least one compound puzzle (e.g., a puzzle where file counts or word counts encode something).
**To reach 10**: The BOM becomes a reference tool the solver needs — like Obra Dinn's crew manifest.

---

### Reading Maps (`READING-MAPS.md`)
**Current score: 1/10**
Curated learning paths through the 52 volumes. Seven named paths (The Engineer, The Physicist, The Generalist, etc.). Completely unused.
**Potential**: A Reading Map could structure a Black Joker compound — "follow The Physicist's path and solve puzzles at each stop." Or: the paths themselves contain hidden connections that are puzzle data.
**To reach 5**: Reference Reading Maps in the Black Joker intro as suggested exploration routes.
**To reach 10**: A compound puzzle where the solver must FOLLOW a Reading Map and collect answers at each stop — the path IS the puzzle.

---

### Prerequisite Graph (`PREREQUISITES.md`)
**Current score: 1/10**
Dependency table showing which volumes assume knowledge from which others. ~20-30 hard dependencies. Completely unused.
**Potential**: The dependency arrows ARE connections between sections. A puzzle could present the graph and ask: "which volume is the bottleneck?" or "what's the longest dependency chain?" The graph could be puzzle data for the Black Joker.
**To reach 5**: Reference Prerequisites in the Red Joker's difficulty curve design (order puzzles by dependency).
**To reach 10**: A compound puzzle that uses the graph structure — find the critical path, extract from the nodes on it.

---

### Atlas (`atlas/`)
**Current score: 1/10**
52 survival-oriented maps planned. Currently 3 built (Tectonic Plates, Global Winds, World Soils). Completely unused by the puzzle hunt.
**Potential**: The atlas IS geographic puzzle content. Star chart connect-the-dots (Puzzle #8/O) is the closest to using atlas-style content, but doesn't reference the actual atlas files. A geographic compound puzzle could use real atlas maps as the puzzle substrate.
**To reach 5**: The Star Chart puzzle references atlas/astronomy maps.
**To reach 10**: A compound puzzle that requires plotting on an actual atlas map — the atlas becomes the worksheet.

---

### Section Landing Pages (`sections/*.md`)
**Current score: 3/10**
14 landing pages with directory tables. Referenced indirectly (puzzles say "the Computing section") but not used structurally.
**Potential**: The landing pages list every directory in each section. Those lists could contain hidden ordering or patterns. Or: the section descriptions contain clues for compound puzzles.
**To reach 7**: Red Joker puzzle reference lines point to landing pages as entry points.

---

### Read This First (`read-this-first/`)
**Current score: 3/10**
13 survival-oriented files (Water, Fire, Shelter, etc.). Card 0 / The Fool. Referenced in the Joker voice design (the Fool is the precursor to the Joker) but no puzzle uses this content.
**Potential**: Read This First is about FUNDAMENTALS — the things you need to know before anything else. It could anchor a warm-up puzzle or the Red Joker's Hydrogen (Z=1) tutorial.
**To reach 7**: Hydrogen puzzle draws from Read This First content.
**To reach 10**: The Fool (Card 0) is the gateway between the encyclopedia and the Joker books — a bridging page that hints at the puzzle hunt's existence.

---

### MkDocs Site (`mkdocs.yml`, rendered HTML)
**Current score: 2/10**
The encyclopedia renders as a navigable website. The puzzle hunt was designed for the Markdown source, not the rendered site. The V1 "medium shift" (source vs. HTML) was abandoned in the addendum pivot.
**Potential**: The rendered site has SEARCH. A solver could use site search to find archetype names for The Grid. The navigation structure (tabs, sections) is itself information. The HTML rendering could contain elements invisible in source (or vice versa).
**To reach 5**: Acknowledge that solvers may use the rendered site for The Grid search.
**To reach 10**: One puzzle that works differently in source vs. rendered form — the medium shift lives after all.

---

### Style Contract (from `CLAUDE.md`)
**Current score: 4/10**
Every guide follows the same format: big picture diagram, layered detail, ASCII boxes, comparison tables, old→new bridges, decision cheat sheets. The puzzle hunt implicitly relies on this consistency (solvers know what to expect in each file).
**Potential**: The style contract's predictable structure could be puzzle data — "the Decision Cheat Sheet in every guide has a specific format; what's different about THIS one?" Or: the bridges (old→new) could contain hidden patterns.
**To reach 7**: One puzzle explicitly uses the style contract's structure as the mechanism (e.g., "every 00-OVERVIEW has a landscape diagram — what's the one element that's different in this section's diagram?").

---

### Archetype Epithets (from `cards/ROLES.md`)
**Current score: 5/10**
Each card has a one-sentence epithet: "Lever, arch, wing — the first engineering." Used in the Joker's puzzle intros (narrative voice) but not as puzzle DATA.
**Potential**: The epithets are poetic, dense, and unique. They could be cipher keys, pattern sources, or identification clues in The Grid. "Which archetype's epithet contains the word 'channel'?" → The Analyst.
**To reach 8**: Use epithets as clues in The Grid — the solver matches epithet fragments to archetype names.

---

### Card Backs (`cards/backs/*.md`) — BUILT
**Current score: 2/10**
52 ASCII card frames. Each has: card identity, tarot correspondence, 7 KEY CONCEPTS (specific formulas, terms, principles), directory list, epithet. These are FINGERPRINTS — each card's 7 concepts uniquely identify it.
**Potential**: The 7 concepts per card are the Grid solver's MANIFEST. Like Obra Dinn's crew portraits. "This volume contains Carnot efficiency and Rankine cycles — that's 7♦ The Alchemist." The card backs could be printed as reference cards in the Black Joker book.
**To reach 8**: Print card backs as reference material in Black Joker. Solver uses them to narrow Grid identifications.
**To reach 10**: Card backs ARE the deduction tool. The solver matches in-encyclopedia content to card-back fingerprints to determine which archetype hides where.

### Card Front Descriptions (`cards/CONCEPTS.md`) — NOT YET BUILT
**Current score: 1/10**
52 image prompts describing card art. Descriptions only — no actual artwork exists yet. Flairs added from honored phases.
**Potential**: When card art IS built, it can be designed WITH the puzzle hunt in mind. Hidden visual elements, encoded details, subtle clues baked into the art. A casual reader sees beautiful illustrations. A Grid solver sees 52 clue-bearing images.
**To reach 5**: Design art with dual purpose (beauty + puzzle) when the time comes.
**To reach 10**: Each card front contains a visual clue that helps solve The Grid — the art IS part of the puzzle.

---

### HISTORY.md (Phase Chronicle)
**Current score: 1/10**
The chronicle of how the library was built. 22 phases, each with a card role. Completely unused.
**Potential**: The history is a STORY — how 52 volumes were built in 6 days. A puzzle could reference specific commits, phase numbers, or the order in which sections were built. Meta-puzzle: "in what order were the sections created?" The history answers it.
**To reach 5**: The Joker's closing monologue references the building of the library (it does — "I built this library in X days").

---

### TRACKER.md
**Current score: 1/10**
Tracks which directories are complete, stubbed, or queued. Batch status.
**Potential**: Low. Internal project management. Not naturally puzzle data.

---

### SCORECARD.md
**Current score: 1/10**
6-dimension quality scores for all 52 volumes. Every volume rated on Length, Suit Fit, Cohesion, Style, Depth, Archetype.
**Potential**: The scores ARE data. "Which volume scored lowest on Archetype?" or "Sort volumes by Depth score." Could be puzzle data for a meta-level compound.
**To reach 5**: A compound puzzle that uses volume quality scores as input data — the solver must find the volumes with specific score patterns.

---

## Score Summary

| Asset | Current | Potential | Gap | Priority |
|-------|---------|-----------|-----|----------|
| 52 Content Volumes | 9 | 10 | Specify files, not just sections | P2 |
| Concept Index | 8 | 10 | Verify uniqueness, assign to compounds | **P0** |
| Card System (Roles + Concepts) | 8 | 10 | Use suits, image concepts, uninvoked archetypes | P1 |
| Bill of Materials | 2 | 7 | Use as reference tool or data source | P2 |
| Reading Maps | 1 | 10 | Path-following compound puzzles | **P1** |
| Prerequisite Graph | 1 | 8 | Graph-structure puzzles | P2 |
| Atlas | 1 | 10 | Geographic puzzle substrate | P2 (atlas incomplete) |
| Section Landing Pages | 3 | 7 | Entry point references | P3 |
| Read This First | 3 | 7 | Hydrogen warm-up, Fool gateway | P2 |
| MkDocs Site | 2 | 5 | Search for Grid, medium-shift | P3 |
| Style Contract | 4 | 7 | Structure-as-data puzzles | P3 |
| Archetype Epithets | 5 | 8 | Grid clues, cipher keys | P2 |
| Card Backs (7 concepts each) | 2 | 10 | Grid manifest — Obra Dinn crew portraits | **P1** |
| Card Front Art (unbuilt) | 1 | 10 | Design art with hidden puzzle layer | P2 (when art is built) |
| HISTORY.md | 1 | 5 | Meta-story reference | P3 |
| TRACKER.md | 1 | 2 | Internal only | — |
| SCORECARD.md | 1 | 5 | Scores as data | P3 |

### Before asset integration (start of session):
**Average utilization: 3.3/10** · Potential: 7.4/10 · Gap: 4.1

### After asset integration (blind review applied):
**Average utilization: 6.1/10** · Potential: 7.8/10 · Gap: 1.7

| Asset | Before | After | What changed |
|-------|--------|-------|-------------|
| Concept Index | 8 | 8 | Already integrated earlier today |
| Card Backs | 2 | **8** | Grid manifest, Obra Dinn crew portraits |
| Reading Maps | 1 | **7** | Replaces MgO compound as path-following puzzle |
| Prerequisite Graph | 1 | **7** | Replaces AlN compound as DAG puzzle |
| Read This First | 3 | **7** | Hydrogen warm-up content |
| Card Identity System | 3 | **7** | Discovered, never explained — enrichment layer |
| HISTORY.md | 1 | **5** | Joker's identity and closing monologue fuel |
| Archetype Epithets | 5 | **6** | Grid matching clues |
| Bill of Materials | 2 | **5** | Grid floor plan (third deduction tool) |

---

## Top Actions to Close the Gap

| Priority | Action | Assets activated | Score gain |
|----------|--------|-----------------|------------|
| **P0** | Verify Concept Index mechanism and assign to 15 compound puzzles | Concept Index (8→10) | +2 |
| **P1** | Design a Reading Map compound puzzle ("follow the path") | Reading Maps (1→7) | +6 |
| **P1** | Use suit identity in meta mechanism; use image concepts as Grid clues | Card System (8→10) | +2 |
| **P2** | Link Hydrogen warm-up to Read This First content | Read This First (3→7) | +4 |
| **P2** | Use BOM as Obra-Dinn-style manifest for The Grid | Bill of Materials (2→7) | +5 |
| **P2** | Use epithets as matching clues in The Grid | Epithets (5→8) | +3 |
| **P2** | Use Prerequisites graph in a compound puzzle | Prerequisites (1→7) | +6 |
| **P3** | Reference atlas in Star Chart puzzle | Atlas (1→3) | +2 |

**If all P0-P2 actions are completed: average utilization rises from 3.3 to 6.8/10.**
