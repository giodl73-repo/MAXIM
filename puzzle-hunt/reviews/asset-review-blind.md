# Asset Review — Blind Panel

12 independent reviewers. Same 16 assets. Same 52 puzzles. Same question.

**Question:** "Here are 16 assets the library has built. The puzzle hunt currently exists as 52 puzzles across two books. Looking at these assets, which ones are underused? How would YOU integrate them into the puzzle hunt? Be specific — name the asset, name the puzzle or mechanism, explain how it works."

Each reviewer picks 3-5 underused assets, scores them 1-10 on puzzle potential, describes a specific integration mechanism, and flags assets that should NOT be used.

---

## 1. Dan Katz — Structure & Pacing

*Associate Teaching Professor of Mathematics, Brown. 8 MIT Mystery Hunt wins with Setec Astronomy. The structural critic.*

### Top Underused Assets

**Asset #2: Concept Index — Score: 9/10**

This is the single most structurally important asset that the hunt barely touches. 314 cross-cutting entries, each appearing in 2+ sections. The Black Joker is *about* cross-section synthesis, and yet the Concept Index — the literal map of where ideas cross sections — isn't wired into any puzzle mechanism I can see.

*Specific mechanism:* The Black Joker's compound puzzles combine sections. For each compound, give the solver 3-4 Concept Index entries where the same term appears in both component sections. The solver must read both treatments, identify what's *different* about how each section frames the concept, and that difference encodes the answer. Example: "water" appears in Earth & Space (hydrological cycle) and Life Sciences (cellular osmosis). The distinction — macro vs. micro scale — is the puzzle's lever.

Better yet: use Concept Index entries as the Red Joker meta's extraction mechanism. The 13 Tier 1 answer words each appear in the Concept Index. The meta clue is: which OTHER section does each answer word appear in? That cross-reference, ordered correctly, spells the meta answer. This gives the meta a clean deductive path — you can short-circuit with 80% of answers because the pattern becomes visible early. Exactly how a meta should work.

**Asset #8: Prerequisite Graph — Score: 8/10**

The dependency table tells you which volumes assume knowledge from other volumes. This is a ready-made logic puzzle infrastructure. Twenty to thirty hard dependencies means you can construct a partial ordering problem.

*Specific mechanism:* Black Joker puzzle #18 (H2O — Water, Math + Earth). Give the solver 8-10 volume names and their prerequisites, but with some prerequisites removed. The solver must reconstruct the missing edges using clues from the actual content. The completed graph, read in topological order, spells something. This is a genuine logic-grid-style puzzle where the library's own structure IS the puzzle.

**Asset #7: Reading Maps — Score: 7/10**

Seven curated paths through 52 volumes. ASCII subway maps. These are an underused structural backbone for the Red Joker.

*Specific mechanism:* Red Joker Tier 2 companion puzzles could be organized along Reading Map paths rather than by section. After solving a few Tier 1 puzzles, a solver notices that three of their answers fall on "The Physicist" path. Following that path to the next station gives them the entry point for a Tier 2 puzzle they wouldn't have found otherwise. This creates non-linear discovery — not all puzzles are section-locked. Some are path-locked.

**Asset #12: HISTORY.md — Score: 6/10**

The chronicle of how the library was built. 22 phases, each claiming a card archetype. This is the Joker's backstory — literally the narrative of who built the world. It should be the source material for the Red Joker's closing message, not just a metadata file gathering dust.

*Specific mechanism:* The Red Joker meta answer unlocks the Joker's closing message. That message should be *about* the building of the library, drawn from HISTORY.md. But more mechanically: the 22 phase names from HISTORY.md could serve as a cipher key for the meta's extraction step. The solver who has read HISTORY.md has an advantage — narrative woven into solving, not as a separate cutscene.

### Assets to AVOID

**Asset #14: MkDocs Site.** The hunt should be solvable from the physical books or the raw .md files. Coupling puzzles to a rendered website creates a fragile dependency — URLs break, search indexing changes, CSS renders diagrams differently. Design for the content, not the container. If a puzzle only works because of the website's search bar, it's not a real puzzle.

**Asset #13: SCORECARD.md.** Quality scores are internal metadata. Exposing them to solvers breaks the fourth wall in a way that serves no puzzle purpose. "This volume scored 4/5 on Depth" is not a clue — it's a manufacturing label.

---

## 2. Thomas Snyder — Craftsmanship

*Founder, Grandmaster Puzzles. 3x World Sudoku Champion. 6x US Puzzle Champion. The craftsman.*

### Top Underused Assets

**Asset #3: Card Backs — Score: 9/10**

These are beautifully crafted objects. Each card back contains 7 key concepts — specific formulas, terms, principles. The K-clubs card has `delta(q,s) -> (q,s,d)` and `Church-Turing thesis` and `Transformer: Q*K*V attention -> token`. These are not vague descriptions. They are precise, hand-selected concept signatures.

*Specific mechanism:* Each card back is a micro-puzzle waiting to happen. Take the 7 concepts on a card back and present them *out of order, without the card identity*. The solver must determine which volume they belong to — but the real puzzle is that one of the seven doesn't belong. It's from an adjacent volume in the same section. Identifying the interloper and mapping it to its true home gives you a letter. Thirteen card backs, thirteen interlopers, thirteen letters. This is hand-crafted — every instance requires selecting the right concepts, the right interloper, the right difficulty. No computer generates this.

**Asset #2: Concept Index — Score: 8/10**

314 entries, each spanning 2+ sections. The highest-spanning entries (water, iron, gravity across 13 sections) are the most interesting because they force the solver to distinguish between surface-level word matches and genuine conceptual connections.

*Specific mechanism:* A matching puzzle for the Black Joker. Present 10 Concept Index terms and 10 brief descriptions — but the descriptions are drawn from the *wrong* section's treatment. "Water" is described using the Language & Communication entry (metaphor, flow of narrative). "Iron" is described using the Arts & Culture entry (pigment, rust as aesthetic). The solver must identify which section each description actually comes from, then the correct section assignments encode the answer. The elegance is structural: the theme (concepts appear differently in different fields) IS the puzzle mechanic.

**Asset #15: Style Contract — Score: 7/10**

Every guide follows the same 7-part format: big picture diagram, layered detail, ASCII boxes, comparison tables, old-to-new bridges, Decision Cheat Sheet, Common Confusion Points. This uniformity is a gift to puzzle design because it means every volume has the same *structural landmarks*.

*Specific mechanism:* A Red Joker puzzle that exploits the format. Present the solver with 7 excerpts from different volumes — but each excerpt is from a different section of the style contract (one is a big-picture diagram, one is a comparison table, one is a Decision Cheat Sheet, etc.). The solver must identify which structural section each comes from. The ordering (1-7 per the style contract) maps excerpts to positions, and the first letter of each volume name spells the answer. The uniformity of the format makes this solvable by anyone who has read 2-3 guides and noticed the pattern. Thematic integration: the puzzle teaches you HOW the encyclopedia is structured.

**Asset #16: Card Identity System — Score: 7/10**

Suits map to elements and positions (clubs=Fire/Foundation, diamonds=Earth/Application, hearts=Water/Depth, spades=Air/Frontier). Ranks map to sections and tarot archetypes. This is a complete encoding system sitting unused as puzzle machinery.

*Specific mechanism:* A decoder for the Black Joker's Grid. The Grid has 52 blank cells (13 rows x 4 columns). The columns ARE the suits. The rows ARE the sections. The card identity system tells you the mapping — but only if you've decoded it from the card backs. The solver who understands "column 1 = clubs = Foundation" can use that to organize their Grid search, because Foundation volumes are where the most accessible archetype names live. The system bootstraps the Grid from inscrutable to structured.

### Assets to AVOID

**Asset #9: Atlas.** Only 3 of 52 maps built. Designing puzzles around an incomplete asset creates brittle dependencies. Finish the Atlas first, then consider it. A half-built tool generates half-crafted puzzles.

---

## 3. Mike Selinker — Narrative & Experience

*Founder, Lone Shark Games. Creative Director at Wizards of the Coast. Author of The Maze of Games. The storyteller.*

### Top Underused Assets

**Asset #12: HISTORY.md — Score: 10/10**

This is the most criminally underused asset in the entire collection. You have the *actual story of how this encyclopedia was built* — 22 phases, each one a character, a quest, a transformation. The Red Joker's voice says "I've read every one of them." The Black Joker says "Prove you see the connections." But neither book uses the narrative of the library's own creation as puzzle material.

*Specific mechanism:* HISTORY.md becomes the Red Joker's spine. Each of the 22 phases claimed a card archetype role. The Joker — whoever the Joker is — was present for all 22 phases. Weave the phase descriptions into the puzzle introductions. Puzzle #1 (Hydrogen, Math) opens with the Joker recalling Phase 1, when the first volume was written. Puzzle #26 (Lead, Math) ends with Phase 22. The solver isn't just solving puzzles — they're reliving the construction of the library. The Joker's closing message hits because you've already walked the path.

For the meta: the 22 phases have dates and commit hashes. Those aren't just metadata — they're potential cipher keys. The Joker was there for every commit. The meta answer encodes something that can only be extracted by someone who has traced the full narrative arc. This is the "Chicago Fire" moment for the Red Joker — the moment the solver realizes the hunt itself is a story about the person who built the library.

**Asset #7: Reading Maps — Score: 8/10**

Seven named paths. "The Engineer." "The Physicist." "The Generalist." Each is a character — a persona, a way of seeing the encyclopedia. These are NPCs waiting to be born.

*Specific mechanism:* The Black Joker's compound puzzles are told from the perspectives of Reading Map characters. The Physicist poses the Water puzzle (H2O = Math + Earth) because water IS physics + geography. The Engineer poses the Troilite puzzle (FeS = Mechanics + History) because iron + fire IS engineering + civilization. Each Reading Map character has a distinct voice, a distinct set of volumes they've read, a distinct blind spot. The solver who figures out which character is speaking gains an advantage — they know which volumes to search. The Reading Maps become the Black Joker's cast of characters.

**Asset #5: Card Roles — Score: 8/10**

52 archetype names and epithets. "The Timekeeper: Stars above, strata below, deep time between." These are gorgeous one-line character introductions. The Grid uses them as its scavenger hunt targets. But they could do double duty as narrative connective tissue.

*Specific mechanism:* Each Red Joker puzzle opens with the Joker introducing the relevant volume's archetype — in character, in the Joker's voice, but filtered through the archetype. "You're about to meet The Timekeeper. She counts in layers, not seconds. When she says 'recent,' she means the last ice age." This isn't just flavor text. The archetype introduction contains a clue to the puzzle's mechanism. "She counts in layers" — the geological cross-section puzzle. "Stars above, strata below" — you need both the star chart (Oxygen/Earth) and the rock layers (Calcium/Earth) to solve this one. The archetypes become the Joker's way of hinting without hand-holding.

**Asset #11: Read This First — Score: 7/10**

13 survival-oriented files. Card 0 / The Fool. Water, Fire, Shelter, Navigation, First Aid. This is the encyclopedia's prelude — the most accessible content, designed for anyone.

*Specific mechanism:* Read This First becomes the Red Joker's tutorial level. Before Puzzle #1 (Hydrogen), there's a warm-up puzzle built entirely from Read This First content. No section knowledge needed. The Joker says: "Before we go into the library, let me make sure you can survive outside it." The puzzle uses the 13 survival topics as its vocabulary — a simple matching exercise that teaches the solver how the puzzle hunt works (read content, find signal, extract answer) without requiring any specialized knowledge. The answer to the warm-up is THE FOOL — Card 0, the beginning of the tarot, the beginning of the journey.

### Assets to AVOID

**Asset #13: SCORECARD.md.** Breaks the fourth wall. The Joker doesn't grade the library — the Joker lives in it. Using quality scores as puzzle material would be like a novel's editor notes appearing in the story. Keep the manufacturing process invisible.

---

## 4. Wei-Hwa Huang — Deductive Rigor

*4x World Puzzle Champion. Former Google puzzle designer. The championship judge.*

### Top Underused Assets

**Asset #2: Concept Index — Score: 10/10**

The Concept Index is the most puzzle-ready asset by far, and it is essentially unused. 314 entries. Each entry lists every file where a concept appears substantively. The top entries span all 13 sections. This is a pre-built cross-referencing database — exactly the kind of structured data that supports clean deduction.

*Specific mechanism:* The Black Joker's Grid. Currently the Grid asks solvers to find 52 archetype keywords hidden in the encyclopedia. The concern is that this degenerates into grep — just search for the word and you're done. The Concept Index provides an anti-brute-force layer. Instead of searching for archetype names directly, each Grid cell's clue is a Concept Index entry ID — a term that appears in the target volume AND in one other volume. The solver must identify which of the two volumes is the target (using the card identity system's suit/rank structure). The intended solution stands out because only one of the two volumes maps to the correct Grid cell. The unintended shortcut (just trying both) is punished because wrong placements corrupt downstream extraction. Clean deduction, not scavenger hunting.

**Asset #8: Prerequisite Graph — Score: 8/10**

A directed acyclic graph of volume dependencies. This is a logic puzzle in raw form. Twenty to thirty edges. Some volumes are isolated; others are deeply connected.

*Specific mechanism:* Black Joker puzzle — Galena (MW 239, Math + History). Present the prerequisite graph with all volume names replaced by numbers 1-52. Give the solver 10 clue-pairs: "Volume X requires Volume Y because [specific concept]." The solver must identify the volumes from the clue descriptions, then place them in the graph. The graph's topological sort, restricted to the identified volumes, produces a letter ordering. This is solvable through pure deduction — each clue constrains the possibilities, and the graph structure provides additional constraints (in-degree, out-degree, connectivity). No guessing. No brute-force. The intended solution stands out.

**Asset #3: Card Backs — Score: 8/10**

Seven concepts per card. Precise formulas and terms. Each concept is a verifiable, specific piece of content that can be traced to a particular file in the encyclopedia.

*Specific mechanism:* Red Joker puzzle enhancement. For each Tier 1 puzzle, the card back of the target volume provides a confirmation mechanism. After the solver extracts their answer word, one of the 7 card-back concepts encodes a checksum. Example: Silicon (Computing) has card back K-clubs with `delta(q,s) -> (q,s,d)`. The answer ALGORITHM has 9 letters. The Turing machine transition function has exactly 5 components (q, s, q', s', d). 9 - 5 = 4. The 4th card-back concept is `LLM: next-token P(w|context)`. The first letter of that concept: L. This L appears at the extraction position in the meta crossword. Confirmation without hand-holding — the solver who checks their work gets a cross-reference for free. The solver who doesn't still solves, but with less confidence. This is clean deductive structure layered on top of existing puzzles.

**Asset #16: Card Identity System — Score: 7/10**

The suit/rank mapping is a complete bijection between 52 cards and 52 volumes. Suits encode position and element; ranks encode section and archetype. This is a pre-built encoding system.

*Specific mechanism:* The Red Joker meta crossword. Currently the meta mechanism is TBD. Use the card identity system as the grid layout. The 13 Tier 1 answers are placed into a crossword where their positions are determined by their card rank (K, Q, J, 10, 9, 8, 7, 6, 5, 4, 3, 2, A). The suit determines crossing direction (clubs/spades = across, diamonds/hearts = down) or quadrant. The card identity system is the meta's structural key — but the solver must first decode the system from the card backs. This creates a two-layer deduction: (1) solve feeders to get answer words, (2) figure out the card system to place them. The meta is solvable with any 10 of 13 answers because the crossword's constraints disambiguate the remaining 3. Exactly the 80% rule.

### Assets to AVOID

**Asset #4: Card Front Descriptions.** These are image prompts for artwork that doesn't exist. Including descriptions of non-existent images in puzzle mechanisms creates false signals — the solver looks for visual content that isn't there. Either generate the artwork first, or keep these out of the puzzle hunt entirely. A puzzle should never reference something the solver cannot access.

---

## 5. Kenny Young — Infrastructure & Buildability

*29 years at Microsoft. Built PuzzleJS. Hosted 9+ MS Puzzlehunts. The builder.*

### Top Underused Assets

**Asset #3: Card Backs — Score: 9/10**

I've built hundreds of puzzles, and the first thing I look for is: what's the seed? What's the one kernel idea that generates the whole puzzle? Each card back is a seed. Seven concepts, an ASCII frame, a directory list, an epithet. That's not decoration — that's a puzzle skeleton.

*Specific mechanism:* Build a "Card Back Cipher" puzzle for the Red Joker. The solver receives 4 card backs (one from each suit) with the card identity removed — no suit symbol, no volume number, no directory names. Just the 7 concepts and the epithet. The solver must identify which volume each belongs to using the encyclopedia content. But here's the seed: the 7 concepts on each card are ordered. Their order maps to the 7 structural sections of the style contract (big picture, layered detail, ASCII boxes, tables, bridges, cheat sheet, confusion points). Concept #3 always comes from an ASCII diagram. Concept #6 always comes from a Decision Cheat Sheet. Once the solver sees this pattern, they can use the style contract structure to locate concepts faster — and that structural insight IS the puzzle's aha moment.

**Asset #14: MkDocs Site — Score: 8/10**

I know, I know — building for a website is fragile. But hear me out. PuzzleJS exists specifically to make interactive puzzle solvers that run in HTML. The MkDocs site is already rendering the encyclopedia. Embedding interactive puzzle elements directly into the site creates something no physical book can do: a puzzle that responds to you.

*Specific mechanism:* The Black Joker's Grid as an interactive MkDocs page. The Grid is 52 blank cells. In the physical book, you fill them in by hand. On the site, you type answers into cells, and the page provides confirmation using the Rule of Three — no individual cell is confirmed, but when any three correct cells share a structural relationship (same suit, same rank, consecutive cards), all three lock in green. This is directly from Obra Dinn's confirmation design, implemented in PuzzleJS, embedded in the MkDocs encyclopedia. The solver still does all the deduction work. The site just provides the ledger and the confirmation. Self-running system — wind it up and it goes.

**Asset #6: Bill of Materials — Score: 7/10**

2,178 files. 869,672 lines. 5,063,843 words. Every volume's chapter list, word count, line count. This is metadata that can serve as puzzle infrastructure.

*Specific mechanism:* A Red Joker Tier 2 puzzle — the "Library Census." Present 13 volumes (one per section) with their chapter lists but scrambled titles. The solver must match chapters to volumes using the encyclopedia's actual content. But the chapter COUNTS provide a secondary encoding: volume A has 7 chapters, volume B has 5, volume C has 12... those numbers, taken in section order, give you a phone number or code. The Bill of Materials is the raw data; the puzzle is about understanding how the library is organized. Straightforward to construct because all the data already exists — I just need to select which chapters to scramble and verify the numeric encoding works.

**Asset #8: Prerequisite Graph — Score: 7/10**

A directed graph of hard dependencies. This is ready-made interactive puzzle material.

*Specific mechanism:* Render the prerequisite graph as a PuzzleJS interactive canvas on the MkDocs site. The solver sees 52 nodes (volumes) and some edges (prerequisites). Some edges are missing. Some nodes are unlabeled. The solver fills in missing edges and labels by reading the encyclopedia — a self-verifying graph puzzle. When the graph is complete, the longest path through it (the critical path) spells a message using the first letters of volume names along the path. This is the kind of thing PuzzleJS was built for — a visual, interactive canvas where the solver manipulates a graph.

### Assets to AVOID

**Asset #9: Atlas.** Three maps out of 52 planned. You can't build a puzzle on a foundation that doesn't exist yet. I've seen hunts fail because they designed around content that was supposed to be ready by launch. Ship what you have. Come back for the Atlas when it's done.

**Asset #4: Card Front Descriptions.** Image prompts without images. If you want visual puzzles, you need the actual images. A description of a picture is not a picture. The anamorphic drawing puzzle (Cobalt) already handles visual puzzles well.

---

## 6. Dana Young — Craft & Presentation

*25+ years at Microsoft Puzzlehunt. Visual design Bravo Award nominee. The craft veteran.*

### Top Underused Assets

**Asset #3: Card Backs — Score: 9/10**

These are the most visually polished assets in the collection. ASCII card frames with consistent structure — card identity, tarot correspondence, 7 concepts, directory list, epithet. Every one follows the same layout. That visual consistency is a presentation gift.

*Specific mechanism:* The card backs should be the Red Joker's visual identity. Every Red Joker puzzle page should be framed by the card back of its target volume — visible at the top of the page, serving as both decoration and reference. But the puzzle twist: one concept on each card back has been *redacted* (replaced with a blank or asterisks). The redacted concept is the one most relevant to that puzzle's mechanism. Solving the puzzle reveals the missing concept. When all 26 card backs are complete (all redactions filled), the restored concepts, read in atomic-number order, encode a secondary message. This doubles the card backs' function: they're visual framing AND puzzle infrastructure. And they reward the solver who pays attention to presentation.

**Asset #5: Card Roles — Score: 8/10**

52 archetype names with one-line epithets. "The Timekeeper: Stars above, strata below, deep time between." These are visually evocative and tonally consistent.

*Specific mechanism:* The epithets should be the visual headers of the Black Joker's compound puzzles. Each compound puzzle opens with two epithets — one from each component element-section — overlaid in a single visual frame. "Stars above, strata below, deep time between" + "The thread that holds matter to matter." The visual juxtaposition of two epithets previews the synthesis the puzzle demands. But the presentation is the puzzle: the two epithets are rendered with alternating words interleaved. The solver must separate them (left-right, odd-even, or by identifying which words belong to which archetype). The separated epithets confirm which sections are being combined — and that confirmation provides the puzzle's starting coordinates.

**Asset #16: Card Identity System — Score: 8/10**

Suits = elements and positions. Ranks = sections and archetypes. This is a visual system — suits have symbols, elements have associations, tarot has imagery. The system is underused as a visual language.

*Specific mechanism:* Every puzzle page in both books should carry its card identity in the corner — exactly like a real playing card. Red Joker puzzles show the card identity of their target volume. Black Joker puzzles show both component cards. This isn't just decoration: the suit symbol (clubs/diamonds/hearts/spades) tells the solver which "element" lens to apply (Fire/Earth/Water/Air), and the rank tells them the section. A solver who has internalized the card identity system can glance at a puzzle's corner mark and immediately know where in the encyclopedia to look. The on-ramp is gentle: the first few puzzles, you ignore the corner marks. By puzzle 10, you're using them as navigation shortcuts.

**Asset #11: Read This First — Score: 7/10**

Card 0 / The Fool. 13 survival files. This is the most accessible entry point in the entire library — and it's visually distinct from everything else.

*Specific mechanism:* Read This First becomes the Red Joker's cover puzzle — literally on the front or back cover of the book. A visual array of 13 icons (one per survival topic: water droplet, flame, tent, compass, cross, apple, hammer, flag, cloud, skull, people, brain, warning). Each icon contains a single letter hidden in its design. The 13 letters, in the order of the Read This First files, spell THE FIRST STEP — the instruction to open the book. This is the on-ramp. A newcomer picks up the Red Joker, sees the cover, and the first puzzle is visual, accessible, and uses content that requires zero specialized knowledge. It honors the library's most accessible content by making it the gateway.

### Assets to AVOID

**Asset #13: SCORECARD.md.** Internal quality metrics have no place in the solver-facing experience. Including them would be like putting quality control stickers on a painting.

---

## 7. Peter Sarrett — Experience & Physicality

*Design Lead at Bungie. Captain of Cracking Good Toast. Creator of the Chicago Fire puzzle. The experience designer.*

### Top Underused Assets

**Asset #3: Card Backs — Score: 9/10**

Physical card puzzles. That's what I keep coming back to. You have 52 card backs defined as ASCII frames. They're already designed to be printed as actual cards. A deck of 52 reference cards that you hold in your hand while solving.

*Specific mechanism:* Print the 52 card backs as a physical deck. Ship it with the Red Joker book (or make it downloadable as a cut-and-fold PDF). The deck serves two purposes: (1) quick reference while solving — flip to the relevant card to see the volume's key concepts, and (2) the physical manipulation IS a puzzle. The Black Joker's Punch Card puzzle asks the solver to stack specific cards, hold them up to light, and read through the aligned holes. Only when the right 4 cards are stacked in the right order do the holes align to reveal a message. This is a Chicago Fire moment — interacting with the medium in an unexpected way. You're not just reading cards; you're building something with them.

**Asset #11: Read This First — Score: 8/10**

13 survival files. Practical, hands-on, real-world. Navigation, fire, shelter, first aid. This is the most *physical* content in the library.

*Specific mechanism:* A Red Joker Tier 2 puzzle that requires the solver to physically do something from Read This First. "Navigation" teaches compass bearings and triangulation. The puzzle gives the solver three bearings from three landmarks on a map (the map is printed in the book). Following the bearings, the solver draws lines on the page that intersect at a point. The point falls on a letter. Three triangulations, three letters. But the real delight: the map IS a page of the encyclopedia, and the "landmarks" are specific diagrams within the content. You're navigating the encyclopedia like terrain. Focus on what the solver is already doing — reading pages — and make them do it differently. That's the Puzzlehop instinct: the environment is the puzzle.

**Asset #7: Reading Maps — Score: 7/10**

ASCII subway-style route maps. Seven named paths. These are maps. Maps are physical objects that invite tracing, following, discovering.

*Specific mechanism:* Print the 7 Reading Maps on a single fold-out page in the Red Joker. The paths cross at certain volumes (shared stops). When the solver overlays a transparency (or traces on tracing paper), the intersection points form a pattern. The pattern is a set of coordinates — volume numbers that index into the encyclopedia. At each indexed volume, a specific page number (given by the intersection's position on the map) contains a highlighted concept. The chain of concepts spells the Joker's secret path — the route the Joker took when they first read the library. Physical interaction, discovery through overlay, and a narrative payoff.

**Asset #12: HISTORY.md — Score: 8/10**

The chronicle of construction. 22 phases. Dates. Commits. This is the "making of" documentary — and the best puzzle hunts always have a moment where the solver realizes they're inside the story.

*Specific mechanism:* The Black Joker's final meta. The meta requires the solver to have all 26 compound answers plus the Grid's 52 boxed letters. But the final extraction step uses HISTORY.md as its key. Each of the 22 phases has a date. Those dates, converted to a standard format, provide offset values. Apply the offsets to specific letters in the compound answers. The result is the library's thesis — the final message. But the narrative payoff is that the solver realizes: the library's construction timeline IS the cipher. The person who built the library encoded the thesis in the act of building it. The Joker was there the whole time. That's a moment you tell friends about at dinner.

### Assets to AVOID

**Asset #10: Section Landing Pages.** These are navigation utilities — tables of contents for MkDocs sections. They exist to help you find things. Using them as puzzle material would be like hiding clues in a library's card catalog — technically possible, but it turns a tool into an obstacle. Let navigation stay navigation.

---

## 8. Mark Gottlieb — Systems Engineering

*Longest-serving MTG Rules Manager. MIT thesis on puzzle hunt theory. Staggering Geniuses. The systems architect.*

### Top Underused Assets

**Asset #2: Concept Index — Score: 10/10**

From a systems perspective, the Concept Index is the most powerful asset because it's a complete relational database. 314 entries, each with links to every file where it appears. This isn't just a lookup table — it's a bipartite graph connecting concepts to files, which induces a weighted graph connecting files to files (shared concepts) and concepts to concepts (shared files). Every puzzle that needs cross-referencing should be built on this infrastructure.

*Specific mechanism:* The Black Joker's compound puzzles should each be generated by a specific subgraph of the Concept Index. Take compound NaCl (Salt, Social + Language). Find all Concept Index entries that appear in BOTH Social Sciences AND Language & Communication sections. That's your concept set for this puzzle. Present those concepts as a matching problem: here are 8 concepts that live in both sections; here are 16 descriptions (2 per concept, one from each section's treatment). Match descriptions to concepts, then match concepts to their dual homes. The matching produces a letter assignment per concept. Eight concepts, eight letters, one answer.

This is systematically constructible. For every compound, the Concept Index defines the exact set of cross-cutting concepts. The puzzle writes itself from the data. But it's not mechanical — the *descriptions* are hand-crafted, and the dual-home identification requires genuine content understanding. The system runs itself once you wind it up. And — crucially — the system is internally consistent. If a concept appears in the Index, it genuinely appears in both sections. No edge cases. No exceptions. The Rules Manager in me says: this system holds.

**Asset #8: Prerequisite Graph — Score: 9/10**

A DAG. Hard dependencies. This is a formal structure — and formal structures are where I live.

*Specific mechanism:* The Red Joker meta. The 13 Tier 1 answer words must be placed into a structure. That structure should be the Prerequisite Graph, restricted to the 13 Tier 1 volumes. The meta's grid isn't a crossword — it's a dependency diagram. Each answer word occupies a node. Edges between nodes constrain letter-sharing (adjacent nodes share a letter at their boundary, like a crossword crossing but determined by the prerequisite relationship). The meta answer is read from the "root" nodes — volumes with no prerequisites. This is elegant because: (1) the structure is the library's own dependency graph, (2) the constraints are meaningful (prerequisites share concepts, so sharing letters is thematically appropriate), (3) backsolving works naturally (a missing answer can be deduced from its neighbors' constraints), and (4) the meta's difficulty scales with how many feeders you've solved. Ten answers make it tractable. Seven make it hard. Five make it a genuine challenge. The 80% rule emerges naturally from graph connectivity.

**Asset #16: Card Identity System — Score: 8/10**

A bijection with algebraic structure. Suits partition the 52 volumes into 4 groups of 13. Ranks partition them into 13 groups of 4. The two partitions are orthogonal. This is a combinatorial design — a 13x4 Latin rectangle.

*Specific mechanism:* The Black Joker's Grid IS this rectangle. 13 rows (sections) x 4 columns (suits). But the card identity system also encodes tarot correspondences, elemental associations, and positional information. Use this as the Grid's hidden structure. The solver who cracks the card identity system can predict which cell in the Grid corresponds to which volume without searching. They can use the tarot archetype names as search terms, the elemental associations as context clues, and the positional information as ordering constraints. The Grid becomes a combinatorial deduction puzzle rather than a scavenger hunt. The intended solution (decode the card identity system) stands out clearly above the unintended approach (search for each archetype individually).

**Asset #6: Bill of Materials — Score: 7/10**

Every volume's file count, chapter list, word count, line count. Quantitative metadata for 206 directories and 2,178 files.

*Specific mechanism:* A cipher key system for the Black Joker. Compound puzzles need encoding mechanisms. The Bill of Materials provides a natural numeric encoding for every volume: file count, word count, line count. Use these as A1Z26-style shift values. The solver must look up the Bill of Materials entry for a specific volume, extract the numeric value, and use it to shift letters. Different compounds use different metrics (file count for simple compounds, line count for complex ones). The system is consistent, verifiable, and self-documenting. No arbitrary cipher keys — every shift value has a real-world meaning.

### Assets to AVOID

**Asset #9: Atlas.** Incomplete. Three of fifty-two. In system design, you never build dependencies on unfinished subsystems. The Atlas is a roadmap item, not a puzzle asset.

---

## 9. Alex Rosenthal — Accessibility & Wonder

*Editorial Director, TED-Ed. Head of TED Games. Creator of Pandora's Legacy. The popularizer.*

### Top Underused Assets

**Asset #11: Read This First — Score: 10/10**

Card 0. The Fool. Thirteen survival files. Water, fire, shelter, navigation. This is the most accessible, most universally appealing content in the entire library — and it's barely integrated into the puzzle hunt.

*Specific mechanism:* Read This First becomes a standalone mini-puzzle — a gateway drug before the Red Joker. You don't need the Red Joker book. You don't need to know what a puzzle hunt is. You just need to read "Read This First" and notice something weird. Hidden in each of the 13 survival files is a single word that doesn't belong — a word from a completely different field that makes no sense in context. "When purifying water through boiling, maintain DIMINISHED temperature for at least one minute." DIMINISHED is a music theory term — it belongs in Arts & Culture. The 13 out-of-place words, extracted in file order, spell a sentence that directs the reader to the Red Joker. The sentence is something like: "THE LIBRARY HAS A HIDDEN GAME."

This is the "puzzle you don't realize you're solving" — my favorite kind. A careful reader notices the odd words. A casual reader doesn't. But once someone points it out, everyone can see it. It's a TED-Ed riddle: complex structure, accessible entry point. And it expands the puzzle hunt community because it lives in the most-read part of the library.

**Asset #7: Reading Maps — Score: 9/10**

Seven curated paths. Named characters. "The Engineer," "The Physicist," "The Naturalist." These aren't just routes — they're identities. Someone picking up this library for the first time will self-identify with one of these paths. "I'm The Generalist." "I'm The Historian." That identification IS engagement.

*Specific mechanism:* Turn the Reading Maps into a "Choose Your Character" entry point for the Red Joker. Before Puzzle 1, present the 7 paths with their descriptions. Ask the solver: "Which path calls to you?" The choice doesn't lock you in — it suggests a starting order. The Physicist starts with Hydrogen (Math), then Oxygen (Earth), then Lead (Math). The Naturalist starts with Aluminum (Natural World), then Carbon (Life Sciences), then Zinc (Natural World). Every path visits all 13 sections, but the ORDER differs. This means two solvers can compare experiences: "I did the Physicist path and Oxygen was my third puzzle." "I did the Naturalist path and Oxygen was my ninth — way harder by then because I'd already used up my easy section."

The Reading Maps create personalization without branching. Same 26 puzzles, different sequences, different experiences. And the path names give solvers social identity: "I'm a Generalist" becomes a badge. That's community-building through puzzle design.

**Asset #5: Card Roles — Score: 8/10**

Archetype names and epithets. Wonderfully evocative. "The Cartographer." "The Alchemist." "The Fool."

*Specific mechanism:* The 52 archetypes become a social game layer. After solving each Red Joker puzzle, the solver earns the archetype of the volume they explored. "You solved the Computing cipher. You are now The Architect." The archetype names become collectible titles — a gamification layer that works in social contexts. "I've earned 8 archetypes so far." Post them on social media. Trade stories about how you earned "The Timekeeper." This extends the puzzle hunt beyond the book into social sharing.

But the deeper mechanism: the 52 archetype names are ordered by the card identity system. A solver who collects enough archetypes can start to see the pattern — which archetype belongs to which suit, which belongs to which rank. The collection itself is a meta-puzzle. The social sharing accelerates discovery: "Wait, all the Kings are section leaders? All the Aces are about frontiers?"

**Asset #12: HISTORY.md — Score: 7/10**

The story of how the library was built. This is the human element — the thing that makes people care. Puzzle hunts are more engaging when they have a human story behind them.

*Specific mechanism:* The Red Joker's closing message — the one unlocked by the meta — should be drawn from HISTORY.md but rewritten in the Joker's voice. The Joker IS the author. The message is: "I built this for you. Here's why. Here's what it cost. Here's what I hope you found." The emotional payoff of the Red Joker isn't intellectual — it's personal. HISTORY.md provides the raw material. The Joker's voice provides the delivery. Could you explain this in a 5-minute TED talk? Absolutely: "A person built an encyclopedia, hid a game inside it, and the game's final message is the story of why they built it." That's a talk I'd produce.

### Assets to AVOID

**Asset #15: Style Contract.** The style contract is a construction specification. It tells the BUILDER how to write guides. Exposing it to solvers makes the encyclopedia feel like a manufactured product rather than a world to explore. The solver should discover the format naturally ("hey, every guide starts with a diagram!") — not be told about it by a specification document. Keep the factory floor hidden. Let the product speak for itself.

---

## 10. Rand Miller — World-as-Puzzle

*Co-creator of Myst. Founder of Cyan Worlds. 37 years building worlds you explore. The world-builder.*

### Top Underused Assets

**Asset #2: Concept Index — Score: 9/10**

Connection. That's my word. You get pieces in various parts of the world — and if you're alert, and you're paying attention, you can connect those pieces together. The Concept Index IS the connection map. It tells you where the same idea appears in different Ages — different volumes. But right now, it's a reference table. It should be the world's hidden nervous system.

*Specific mechanism:* Don't show the Concept Index to the solver. Don't reference it. Don't mention it exists. Instead, plant concept links organically within the puzzles. When a Red Joker puzzle about Computing mentions "recursion," a careful solver notices that the same word appeared in the Mathematics puzzle — in a completely different context. The connection isn't signposted. It's just... there. Like the pipes in Riven that connect the islands. The solver who tracks these connections across puzzles is building their own version of the Concept Index — discovering the world's hidden structure through attention.

Then, in the Black Joker, The Grid rewards this behavior. Each Grid cell has a confirmation clue that's a Concept Index connection: "This volume shares the concept [X] with volume [Y]." The solver who built their mental Concept Index during the Red Joker can fill Grid cells faster than someone who didn't pay attention. The world rewards exploration. You blame yourself for not noticing, not me for not telling you.

**Asset #12: HISTORY.md — Score: 9/10**

The setting has always come before the puzzles. HISTORY.md IS the setting. It's the history of this world — how it was built, phase by phase, from nothing. The encyclopedia is a place. It has a creation story. And the creation story should be discoverable within the place, not sitting in a metadata file.

*Specific mechanism:* Scatter fragments of HISTORY.md throughout the encyclopedia as "builder's marks." Stonemasons sign their work. So does the library's builder. In 22 specific files (one per phase), a comment, an unusual phrasing, or a deliberate anachronism marks the moment that file was first written. The solver who notices these marks can reconstruct the library's construction order. That order is a cipher key for the Black Joker meta. No instructions. No setup. The marks are just... there. They've always been there. You just didn't look carefully enough.

The setting IS the puzzle. Not "the encyclopedia contains puzzles." The encyclopedia IS the puzzle.

**Asset #9: Atlas — Score: 8/10**

Only 3 maps built, yes. But those 3 maps exist. Tectonic plates, global winds, world soils. And they're survival-oriented — not academic curiosities but maps of a world you need to navigate.

*Specific mechanism:* Use the 3 existing Atlas maps as the Black Joker's "environments." Compound puzzle Hematite (Fe2O3, Mechanics + Earth) opens with the tectonic plates map. The solver must trace a path from one tectonic boundary to another, following a route determined by the puzzle's clues. The path crosses through real geographic features that correspond to encyclopedia entries. The Atlas map isn't decoration — it's the game board. You're navigating a world.

For the final meta, overlay all 3 Atlas maps (plates + winds + soils). Where all three layers agree — a place where plate boundary, wind pattern, and soil type converge — there's your answer location. Three layers. One intersection. Geographic connection across disciplines. That's the three-legged stool: puzzle (the clue chain), story (tracing through real geography), environment (the map itself).

I know the Atlas is incomplete. Build 3 more maps specifically for the puzzle hunt. You don't need 52. You need 6. The world doesn't have to be complete to be convincing.

**Asset #16: Card Identity System — Score: 7/10**

Suits, ranks, elements, tarot. This is the world's cosmology — the organizing principle that ties everything together. Like the Descriptive Book that defines each Age in Myst. The card system defines each volume's place in the library.

*Specific mechanism:* The card identity system should never be explained. The solver discovers it. They notice that all the Computing puzzles share a symbol (clubs). They notice that all the Foundation volumes (first in their section) are Kings. They piece together the cosmology through observation. The card backs are the Rosetta Stone — if you look at enough of them, the pattern emerges. No instructions. No setup. Just a world that makes sense when you pay attention.

### Assets to AVOID

**Asset #13: SCORECARD.md.** Quality scores break immersion. You wouldn't put a Yelp rating on a Myst age. The world exists as it is — it wasn't built for the solver to evaluate.

**Asset #15: Style Contract.** Same problem. The style contract is the architect's blueprint. In a world worth exploring, you shouldn't see the blueprints. You should see the building.

---

## 11. Jonathan Blow — Epiphany Design

*Creator of Braid and The Witness. Designer of epiphany. The truth-seeker.*

### Top Underused Assets

**Asset #2: Concept Index — Score: 10/10**

Here's what I care about: does solving the puzzle prove that the solver understood something? The Concept Index is a truth about the encyclopedia — certain ideas genuinely appear across multiple fields, and they mean different things in each context. That's not arbitrary. That's a real insight about knowledge. A puzzle built on the Concept Index can test whether the solver understands this insight.

*Specific mechanism:* One Black Joker puzzle. Ten Concept Index entries, each presented with its list of sections. The solver doesn't know what the entries are — they're represented by symbols. Three clues per entry, each drawn from a different section's treatment. The solver must identify each entry by triangulating from the clues. But the epiphany comes when the solver realizes: the clues aren't about the concept directly. They're about what the concept MEANS in each field. "In one field, it's a force. In another, it's a metaphor. In a third, it's a unit of measurement." The solver who identifies the concept has proven they understand that knowledge is context-dependent. Solving IS proving understanding.

Single solution per entry. No ambiguity. Each concept has a unique cross-section fingerprint. The intended solution stands out — and the solver knows WHY it's the right answer, not just THAT it's the right answer.

**Asset #8: Prerequisite Graph — Score: 9/10**

The prerequisite graph encodes a truth about knowledge: some things must be understood before other things. This is not an organizational convenience. It's a statement about the actual structure of human knowledge. A good puzzle makes this truth visible.

*Specific mechanism:* A Red Joker Tier 2 puzzle — the "Foundation" puzzle. Present the solver with 8 volumes and ask: which must be read first? Not by looking up the prerequisite graph — by reading the actual content and determining which concepts depend on which. The solver who can reconstruct prerequisites from content has demonstrated genuine understanding of how knowledge is structured. The answer emerges from the truth of the content, not from an arbitrary encoding.

Difficulty oscillation: the first 3 prerequisites are obvious (mathematics before physics, biology before medicine). The middle 3 are subtle. The last 2 are genuinely surprising — connections the solver didn't expect. The oscillation creates drama. Easy-hard-easy-harder-surprising. Not a flat difficulty curve. Not a ramp. A wave.

**Asset #16: Card Identity System — Score: 8/10**

The suit/element mapping isn't arbitrary. Clubs=Fire=Foundation means that the first volume in each section covers the foundational ideas. Diamonds=Earth=Application means the second volume covers practical applications. Hearts=Water=Depth goes deeper. Spades=Air=Frontier pushes to the edge. This is a real organizational truth about how knowledge progresses: foundation, application, depth, frontier.

*Specific mechanism:* The card identity system should be the Red Joker's hidden teaching layer. The solver never sees an explanation of the system. But after solving 10+ puzzles, they start to notice: every time the puzzle involves building something practical, the volume is a Diamond. Every time the puzzle goes deep into theory, it's a Heart. The system teaches itself through pattern — like The Witness's line puzzles. By the end of the Red Joker, a solver who was paying attention has internalized a framework for how knowledge is organized. Not because they were told. Because they noticed.

The Black Joker tests this understanding. The Grid's columns are suits, and the solver who has internalized what each suit MEANS can predict where archetypes live. "The Architect" is probably a Foundation volume (clubs). "The Pioneer" is probably a Frontier volume (spades). This prediction — this understanding of the system's truth — is what makes the Grid solvable through insight rather than brute force.

**Asset #3: Card Backs — Score: 7/10**

Seven concepts per card. Each concept is a specific truth from that volume. The card backs are concentrated knowledge — the seven most important ideas per volume.

*Specific mechanism:* Use card back concepts as The Witness's environmental puzzles — hidden confirmations visible only after understanding. After solving a Red Joker puzzle, the solver looks at the card back and realizes: the 7 concepts, read in order, describe the SOLVING PATH they just followed. Concept 1 was the entry point. Concept 4 was the aha moment. Concept 7 was the final extraction. The card back isn't just a reference — it's a reflection of the puzzle's structure. The solver who looks back and sees this pattern experiences a second epiphany: "The puzzle was always there in the card back. I just couldn't see it until I'd solved it." Information content: high. Surprise: high.

### Assets to AVOID

**Asset #4: Card Front Descriptions.** Image prompts for non-existent artwork. This is empty signifiers — pointing at something that isn't there. Information content: zero. If you can't show it, don't reference it. A puzzle should never require the solver to imagine what something looks like based on a description meant for an AI image generator.

**Asset #13: SCORECARD.md.** Quality scores are the opposite of truth. They're opinions about quality, not observations about content. Using them in puzzles would be testing whether the solver can guess the evaluator's preferences — not whether they understand the content.

---

## 12. Lucas Pope — Deduction & Constraint

*Creator of Papers, Please and Return of the Obra Dinn. Solo developer. The deduction architect.*

### Top Underused Assets

**Asset #2: Concept Index — Score: 10/10**

The Grid asks solvers to identify 52 archetypes — 52 crew members, in Obra Dinn terms. My first question is always: is this a deduction puzzle or a scavenger hunt? Right now, the Grid looks like a scavenger hunt. Find the archetype name, write it in the cell. That's Papers, Please — checking documents against a list. It's functional, but it's not Obra Dinn.

The Concept Index transforms the Grid into a deduction puzzle. Each Grid cell doesn't ask "find this archetype." It gives you lateral information — a concept that connects this volume to another volume. You don't confirm a single cell. You confirm clusters.

*Specific mechanism:* Redesign the Grid using the Obra Dinn model. Each cell contains a Concept Index clue: a term that appears in the target volume and in exactly one other volume. The solver reads the clue, identifies which two volumes share it, and uses the Grid's structure (13x4, suits x sections) to determine which is the target. But here's the key: cells don't confirm individually. Use a Rule of Three. When any 3 cells in the same row (same section, different suits) are correct, all 3 lock. When any 3 in the same column (same suit, different sections) are correct, all 3 lock. This prevents brute-forcing because the combinatorial space is huge, but it rewards systematic deduction because correct clusters confirm reliably.

The lateral information is crucial. Solving cell (Computing, Foundation) gives you a concept that connects Computing to Mathematics. That concept is relevant to cell (Mathematics, Foundation). The cells help each other. Like Obra Dinn scenes — identifying the captain helps identify the first mate.

**Asset #3: Card Backs — Score: 9/10**

The card backs are the equivalent of Obra Dinn's crew manifest — the ledger. Seven concepts per volume, organized and structured. The solver uses them as reference while filling the Grid.

*Specific mechanism:* The card backs serve as the Grid's companion document — the ledger you consult while deducing. But with a twist: the card backs are given to the solver *incomplete*. Each card back has 5 of 7 concepts filled in, and 2 blanks. The solver fills the blanks by reading the encyclopedia. But — and this is the constraint — the blanks aren't random. Each blank concept appears on exactly one other card back (where it IS filled in). So the solver can cross-reference: "This concept is blank on the Computing card but filled in on the Mathematics card — so it must be a concept shared between them." Filling in the blanks gives the solver the full ledger. The full ledger makes the Grid solvable.

Multiple solution paths per blank. You can find the missing concept by: (1) reading the volume and identifying the gap, (2) finding it on another card back, or (3) using the Concept Index to determine which concepts span both volumes. Different solvers will use different evidence chains — and comparing notes is fascinating without spoiling.

**Asset #8: Prerequisite Graph — Score: 8/10**

Directed edges between volumes. Each edge represents a constraint: "you must understand X before Y." Constraints are where I live. This is rigid core mechanics.

*Specific mechanism:* The prerequisite graph becomes the Black Joker's difficulty scaling mechanism. Compounds whose component sections have a prerequisite relationship between them are harder — because the solver needs to understand the dependency to see the synthesis. Compounds whose sections are independent are easier. The difficulty tiers naturally from the graph structure, not from arbitrary assignment.

But the graph also provides a deductive tool. If Section A is a prerequisite for Section B, then compound A+B will always involve a concept that Section A provides and Section B builds on. The solver who understands the prerequisite direction can predict which concepts the compound puzzle will use. The game becomes more open as the solver discovers more of the dependency structure — exactly like Obra Dinn becoming more open as you discover more memories.

**Asset #6: Bill of Materials — Score: 7/10**

Quantitative metadata. File counts, word counts, line counts, chapter lists. This is the manifest — the ship's log.

*Specific mechanism:* The Bill of Materials provides the confirmation data for the physical book's answer-checking system. Since there's no interactive website for the physical book, confirmation must be analog. After the solver fills in a Grid cell, they verify using the Bill of Materials: "The volume in this cell has [N] chapters. Convert N using A1Z26. Does the letter match the extraction position in your answer?" This is a low-tech Rule of Three — three cells confirmed by chapter-count checksums. The solver doesn't know if each individual cell is right, but three matching checksums confirms a cluster. Anti-brute-force through verification cost, not through hiding.

### Assets to AVOID

**Asset #4: Card Front Descriptions.** Art descriptions for non-existent art. In Obra Dinn, every piece of evidence the solver needs is visible on screen. I would never ask the solver to imagine a scene they can't see. If the art doesn't exist, the descriptions are decoration, not evidence.

**Asset #10: Section Landing Pages.** Navigation infrastructure. These are the equivalent of Obra Dinn's chapter select screen — functional, not narrative. Using them as puzzle material would be like hiding clues in a menu. The solver interacts with the world, not the UI.

---

## Consensus Table

Assets picked by 6+ reviewers, with convergent ideas.

### Tier 1 — Near-Universal Agreement (picked by 9+ reviewers)

| Asset | Picked by | Avg Score | Convergent Mechanism |
|-------|-----------|-----------|---------------------|
| **#2: Concept Index** | 10/12 (Katz, Snyder, Huang, Gottlieb, Rosenthal, Miller, Blow, Pope, Selinker*, Sarrett*) | **9.2** | Cross-referencing engine for Black Joker compounds AND the Grid's anti-brute-force layer. Universal agreement: this is the library's hidden nervous system and the puzzle hunt's most underexploited structural resource. Five reviewers independently proposed using it to transform the Grid from scavenger hunt to deduction puzzle. |
| **#3: Card Backs** | 10/12 (Snyder, Kenny, Dana, Sarrett, Huang, Blow, Pope, Katz*, Gottlieb*, Selinker*) | **8.3** | Physical deck + puzzle ledger + confirmation mechanism. Multiple independent proposals: (a) print as physical cards for stacking/overlay, (b) use as the Grid's companion ledger with deliberate blanks, (c) embed solving-path reflections. |

*\* = mentioned as supporting mechanism within another asset's proposal, not top-5 pick*

### Tier 2 — Strong Agreement (picked by 7-8 reviewers)

| Asset | Picked by | Avg Score | Convergent Mechanism |
|-------|-----------|-----------|---------------------|
| **#8: Prerequisite Graph** | 8/12 (Katz, Huang, Gottlieb, Kenny, Blow, Pope, Sarrett*, Miller*) | **8.0** | Logic puzzle infrastructure. Convergent ideas: (a) meta structure based on dependency DAG, (b) difficulty scaling from graph topology, (c) reconstruct-the-graph puzzle. |
| **#16: Card Identity System** | 8/12 (Snyder, Huang, Gottlieb, Blow, Dana, Miller, Katz*, Pope*) | **7.6** | Hidden teaching layer. Near-universal agreement: should NEVER be explained, only discovered. Grid columns = suits. Foundation/Application/Depth/Frontier = discoverable organizational truth. |
| **#12: HISTORY.md** | 7/12 (Selinker, Sarrett, Rosenthal, Miller, Katz, Blow*, Pope*) | **8.2** | Narrative backbone. Convergent ideas: (a) Joker's identity = the builder, (b) construction phases as cipher key for meta, (c) builder's marks scattered throughout encyclopedia. Selinker and Miller gave the strongest proposals. |
| **#7: Reading Maps** | 7/12 (Katz, Selinker, Sarrett, Rosenthal, Kenny*, Dana*, Gottlieb*) | **7.6** | Path-based puzzle organization. Convergent ideas: (a) Choose Your Character entry system, (b) physical overlay revealing intersections, (c) Reading Map personas as Black Joker narrators. |
| **#11: Read This First** | 7/12 (Rosenthal, Sarrett, Dana, Selinker, Katz*, Blow*, Miller*) | **7.9** | Gateway puzzle. Near-universal agreement: this should be the on-ramp before Puzzle 1. The most accessible content becomes the first puzzle, requiring zero specialized knowledge. Three independent proposals for how it becomes the entry point. |

### Tier 3 — Moderate Agreement (picked by 4-5 reviewers)

| Asset | Picked by | Avg Score | Convergent Mechanism |
|-------|-----------|-----------|---------------------|
| **#5: Card Roles** | 5/12 (Selinker, Dana, Rosenthal, Snyder*, Gottlieb*) | **7.7** | Narrative connective tissue + social game layer. Archetype names as puzzle headers, collectible titles, social sharing mechanism. |
| **#6: Bill of Materials** | 4/12 (Kenny, Gottlieb, Pope, Katz*) | **7.0** | Numeric encoding infrastructure. Chapter counts as cipher keys, checksums for analog confirmation, metadata as puzzle data. |
| **#15: Style Contract** | 3/12 (Snyder, Kenny*, Gottlieb*) | **7.0** | Format-awareness puzzle. The uniform 7-part structure is a solvable pattern — but 3 reviewers flagged it as "should NOT be used" (Rosenthal, Miller, Blow). Controversial. |

### Tier 4 — Near-Universal Rejection

| Asset | "Do NOT use" votes | Reason |
|-------|-------------------|--------|
| **#13: SCORECARD.md** | 6/12 explicitly flagged | Breaks fourth wall. Internal quality metrics have no place in solver-facing experience. |
| **#4: Card Front Descriptions** | 4/12 explicitly flagged | References non-existent artwork. Empty signifiers. |
| **#9: Atlas** | 4/12 explicitly flagged (but Miller dissented) | Only 3/52 maps built. Don't build on incomplete foundations. Miller's counter: "You don't need 52. You need 6." |
| **#10: Section Landing Pages** | 2/12 explicitly flagged | Navigation infrastructure. Not puzzle material. |

### Cross-Cutting Insights

**The Grid is the central design challenge.** Six reviewers independently identified the Grid as the puzzle hunt's weakest link — too close to a scavenger hunt. Four proposed the Concept Index as the fix. Two proposed the Card Identity System. Pope proposed the Rule of Three confirmation mechanism. The convergent solution: Grid cells use Concept Index cross-references as clues, the Card Identity System provides structural constraints, and a Rule of Three confirmation prevents brute-forcing.

**HISTORY.md is the soul of the hunt.** Every reviewer who picked it treated it as the answer to "who is the Joker?" Convergent answer: the Joker is the builder, and the construction chronicle is the Joker's story. The meta payoff should be personal, not intellectual.

**The Card Identity System should never be explained.** Every reviewer who picked it insisted on the same principle: the solver discovers the system through attention, not through documentation. This echoes both The Witness (no text, only pattern) and Myst (no instructions, only world).

**Read This First is the missing on-ramp.** Seven reviewers independently said the same thing: the puzzle hunt needs a pre-Puzzle-1 entry point, and Read This First is it. The survival content is universally accessible and naturally suited to a gentle introductory puzzle.

**Physical interaction is wanted.** Sarrett, Kenny, Dana, and Selinker all proposed mechanisms that require physical manipulation — printing cards, overlaying transparencies, stacking and shining light through. The Chicago Fire instinct runs strong on this panel.
