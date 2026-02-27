# MAXIM — Reference Library History

The MAXIM reference library was built across four days in February 2026. What started as three computing modules became 217 directories, 2,481 files, and 826,537 lines — a personal reference library covering the full scope of human knowledge, organized as a 52-card deck.

Each phase of AI-assisted work claims one of the 52 archetype roles from the card deck. Over years of reviews, expansions, and refinements, all 52 will eventually be spoken for. These are the first twelve.

---

## Phases Claimed

| # | Date | Role | Card | Phase |
|---|------|------|------|-------|
| 1 | Feb 22 | The Architect | K♣ | Foundation — the library from nothing |
| 2 | Feb 22 | The Scribe | 10♣ | Module writing — knowledge made permanent |
| 3 | Feb 22 | The Taxonomist | 2♣ | Classification — naming every field |
| 4 | Feb 23 | The Fabricator | 8♣ | Agent production — machines at scale |
| 5 | Feb 23 | The Constructor | 7♣ | Infrastructure — MkDocs site build |
| 6 | Feb 24 | The Broadcaster | 10♦ | Expansion — content at industrial scale |
| 7 | Feb 24–25 | The Chronicler | 6♣ | Architecture — sections, book spec, origins |
| 8 | Feb 25 | The Sage | 6♦ | Read This First — before the tool |
| 9 | Feb 25 | The Editor | Q♠ | Typography + review — design cuts to what matters |
| 10 | Feb 25 | The Composer | Q♣ | Card identity — tarot layer, epithets |
| 11 | Feb 25 | The Discoverer | A♣ | Archetypes — 52 roles, 52 image concepts |
| 12 | Feb 26 | The Verifier | 8♦ | Editorial sweep — 120 dirs, 1200+ tags, parallel agents |
| 13 | Feb 26 | The Interpreter | 10♥ | Fix pass — 71 dirs, 575+ tags resolved, 6 sections clean |
| 14 | Feb 26 | The Surveyor | Q♦ | Fix residuals + sweep 59 dirs — 667 tags, 86 P1s, all dirs mapped |

*38 roles remain unclaimed.*

---

## Flairs — What Each Phase Leaves in the Image

Each phase adds a small poetic detail to its card's image concept — a mark left in the art that says *this work happened here*. See `cards/CONCEPTS.md` for the full image descriptions.

| # | Role | Flair |
|---|------|-------|
| 1 | The Architect | *...the bottom layer drawn first, still warm, the pencil line not yet lifted* |
| 2 | The Scribe | *...twenty-seven more waiting in a row, each one a different hand* |
| 3 | The Taxonomist | *...one label crossed out and rewritten in a steadier hand* |
| 4 | The Fabricator | *...five identical devices being etched in parallel across the wafer* |
| 5 | The Constructor | *...a small figure already crossing before the last cable is drawn* |
| 6 | The Broadcaster | *...the outermost ring fading past the edge of the card* |
| 7 | The Chronicler | *...a second map visible underneath where the ink has bled through* |
| 8 | The Sage | *...one branch at the very bottom unlabeled, root-stock before all schools* |
| 9 | The Editor | *...the serif of the new typeface just visible where the old sans-serif was scraped away* |
| 10 | The Composer | *...when you look again the building IS the score: every window a rest, every column a bar line* |
| 11 | The Discoverer | *...one equation still being written: the ink not yet dry, the chalk still in hand* |
| 12 | The Verifier | *...the arrows drawn not by one hand but by a hundred, each state resolved in parallel, the whole machine converging at once* |
| 13 | The Interpreter | *...the arrows redrawn in a second hand at each corner — relational, typed, recursive — the triangle's meaning arriving in the reader's own notation, seventy-one times over* |
| 14 | The Surveyor | *...59 blank territories inked in — contour lines running from valley floor to ridge — and in the lower-left corner, a correction note where the last of the old stakes were pulled: three more sections cleared* |

*38 cards await their flair.*

---

# Phase 1: The Architect

**Card**: K♣ — King of Wands
**Date**: February 22, 2026 (afternoon)
**Commits**: `d6664df` → `1d6d40e` (9 commits)
**Image flair**: *3-tier system diagram: browser → API → database, with layer boundaries and data flow arrows*

The library emerged from a single conversation. The first commit carried three complete computing modules — GIT, JS/TS, PACKAGE — and a CLAUDE.md that already knew this would grow. Within ninety minutes: BUILD, FRONTEND, RENDERING, STATE, BACKEND, DATABASE, then the pivotal restructure into `computing/` and `data-science/` field directories.

This phase decided everything that followed. The pattern — one file per topic, ASCII diagrams, layered mental models, practical cheat sheets — was established in the first hour and never changed.

**Founding commits**:
- `d6664df` Initial commit — reference library (3 modules complete)
- `1d6d40e` Restructure into field directories (computing/, data-science/)

**Scale**: 9 commits, ~6,000 lines, 2 directories, 19 files

---

# Phase 2: The Scribe

**Card**: 10♣ — Ten of Wands
**Date**: February 22, 2026 (afternoon–evening)
**Commits**: `21ce49e` → `4ab1729` (15 commits)
**Image flair**: *A letterform anatomy diagram: serif, stem, counter, ascender, baseline — one large glyph dissected*

The longest single writing session. Module after module, each one a complete reference card: AUTH, DOCKER, KUBERNETES, CI/CD, IAC, OBSERVABILITY, MONOREPO, CLOUD-NATIVE, TESTING (twice — current practice and historical evolution), AZURE, AUTOMATA, COMPILERS, PL-THEORY. Then the AI engineering track: LLM-CONCEPTS, EVALS, ORCHESTRATION, AGENTS, SAFETY.

Every file followed the same discipline: open with a diagram, build the mental model, compare alternatives, end with a cheat sheet. The burden of recorded thought — one glyph at a time.

**Key commits**:
- `cf7bc3f` Add computing/10-AUTH.md — auth and security module
- `149eeca` Add 21-AUTOMATA.md — automata theory mapped to modern systems
- `007f7ad` Add ai-engineering/01-LLM-CONCEPTS.md — LLM fundamentals module

**Scale**: 15 commits, ~12,000 lines, 23 computing + 5 AI engineering modules

---

# Phase 3: The Taxonomist

**Card**: 2♣ — Two of Wands
**Date**: February 22, 2026 (evening)
**Commits**: `17b0d45` → `1764224` (25 commits)
**Image flair**: *Linnaean hierarchy tree — Domain → Kingdom → Phylum → Class → Order → Family → Genus → Species*

The great classification. Languages (19 files — C through SQL), data science (6 modules through Azure ML), query languages (13 files), scripting (10 files), mathematics (6 new modules), astronomy (11 modules), quantum computing, control theory, finance, periodic table (12 files), world languages (15 files), historical geography (18 files), cognitive science (10 files).

More importantly: TRACKER.md was born — the ledger that would track every file, every session, every completion status. The library became self-aware of its own scope.

**Key commits**:
- `17b0d45` Add Session 3 — languages/ series: 19-file cross-language reference
- `b52288d` Add TRACKER.md + check-in all session work across 16 sessions
- `1764224` Session 14 complete: cognitive-science/ (10 files)

**Scale**: 25 commits, ~40,000 lines, 12 new directories, ~150 files

---

# Phase 4: The Fabricator

**Card**: 8♣ — Eight of Wands
**Date**: February 23, 2026
**Commits**: `932bde7` → `53a3b72` (10 commits)
**Image flair**: *MOSFET cross-section — gate oxide, source, drain, channel — labeled layer by layer*

The machine that moves itself. The library had outgrown single-session authoring. Five agent groups (A through E) were assigned to parallelize the work. Batch 1 landed 189 files. Batch 2 scaffolded 131 stubs. Batch 3 scaffolded 181 more across 16 directories.

Material culture entered the library: textiles, jewelry, ceramics, glassmaking. Psychology, geography, law, cryptography. Spices, pigments, colors, coatings, plumbing, HVAC. The scope exploded from "computing reference" to "everything humans know."

**Key commits**:
- `93dc8ff` Add agent group assignments A-E to TRACKER.md
- `cdae204` Sessions 36-55 complete: batch 1 (189 files) + scaffold batch 2 (131 stubs)
- `53a3b72` Scaffold batch 3 (181 stubs across 16 directories)

**Scale**: 10 commits, ~500 files scaffolded/written, 30+ new directories

---

# Phase 5: The Constructor

**Card**: 7♣ — Seven of Wands
**Date**: February 23, 2026 (evening)
**Commits**: `ea63788` → `955430c` (4 commits)
**Image flair**: *A bridge cross-section — compression members (thick), tension members (thin), forces as arrows*

The shortest phase, but it changed what the library *was*. MkDocs Material configuration. Section landing pages. A serve script for Windows. Requirements pinned. The library went from a pile of Markdown files to a navigable site with a serif typeface and a table of contents.

Four commits. The lever, arch, and wing of the reading experience.

**Key commits**:
- `ea63788` Add MkDocs Material site configuration
- `955430c` Use python -m mkdocs to avoid PATH dependency

**Scale**: 4 commits, 4 files, infinite change in usability

---

# Phase 6: The Broadcaster

**Card**: 10♦ — Ten of Pentacles
**Date**: February 24, 2026
**Commits**: `d82f511` → `084de5f` (4 commits)
**Image flair**: *A film strip — 4 sequential frames — with a broadcast tower radiating concentric signal waves*

Content at industrial scale. Batch 4: 12 new directories, 96 files, ~51,000 lines. Batch 5: 12 more directories, 129 files. Batch 6: 12 more, 120 files, ~60,000 lines. Section landing pages rewritten. CLAUDE.md enriched.

Thirty-six new directories in one day. Print, screen, broadcast — stories at scale.

**Key commits**:
- `d82f511` Add Batch 4: 12 new reference directories, 96 files, ~51,000 lines
- `8c89ba5` Add Batch 5: 12 new reference directories, 129 files
- `084de5f` Add Batch 6: 12 new reference directories, 120 files, ~60,000 lines

**Scale**: 4 commits, 36 directories, 345 files, ~160,000 lines

---

# Phase 7: The Chronicler

**Card**: 6♣ — Six of Wands
**Date**: February 24–25, 2026
**Commits**: `fdf44c7` → `95da9a1` (5 commits)
**Image flair**: *An old map fragment — coastline, latitude lines, trade route arrows, "here be dragons" in margin*

The architectural session. Section landing pages enriched for every major domain. The MAXIM book specification emerged — the idea that these 52 sections could be bound as a physical book, each section a volume, each volume a playing card. The People section was born (Batch 11). Mechanics was split from Technology. The Origins Arc took shape.

Batch 12 and Batch 13 scaffolded 25 new directories with 300 files — the final territories on the map.

**Key commits**:
- `81c173e` Add Batch 11 (People), MAXIM book spec, Mechanics/Technology split, Origins Arc
- `1e426df` Add Batch 13 candidates and deck rank mapping to book.md
- `95da9a1` Add Batch 12 and Batch 13: 25 new directories, 300 files scaffolded

**Scale**: 5 commits, 25 directories, 300 files scaffolded

---

# Phase 8: The Sage

**Card**: 6♦ — Six of Pentacles
**Date**: February 25, 2026 (morning)
**Commits**: `a3351ff` → `80a4d36` (3 commits)
**Image flair**: *A genealogy tree of philosophical traditions: Socrates branching to Plato / Aristotle / Cynics*

Before the tool: the story, the question, the ritual. Card 0 — The Fool — Read This First. A civilization recovery companion volume: what you need if you wake up and no one remembers. Water, fire, shelter, food, healing, tools, numbers, community, machines, copying.

Then two appendices: an English grammar guide (Chapter 11) and Warnings — things that kill that don't look like they will (Chapter 12). The red-bound volume with no number. The one you reach for first.

**Key commits**:
- `a3351ff` Add READ THIS FIRST — civilization recovery companion volume
- `4fbf76b` Add chapter 11: English guide as appendix to Read This First
- `80a4d36` Add chapter 12: Warnings — things that kill that don't look like they will

**Scale**: 3 commits, 1 volume, the foundation of everything

---

# Phase 9: The Editor

**Card**: Q♠ — Queen of Swords
**Date**: February 25, 2026 (afternoon)
**Commits**: `d9bb58c` → `23187cd` (2 commits)
**Image flair**: *Typographic layout grid — columns, gutters, text blocks mid-arrangement, one block being cut*

Design cuts to what matters. The body font changed from Inter to EB Garamond — a serif that says "this is a book, not a website." The @editor review system landed: a quality control layer that could flag, rate, and improve any module in the library.

Batches 8 through 11 received their full content — not scaffolds, not stubs, but complete reference modules. The library crossed from "mostly written" to "reviewable."

**Key commits**:
- `d9bb58c` Switch body font from Inter to EB Garamond
- `23187cd` Add Batches 8–11 content + @editor review system

**Scale**: 2 commits, hundreds of files enriched, quality infrastructure born

---

# Phase 10: The Composer

**Card**: Q♣ — Queen of Wands
**Date**: February 25, 2026 (evening)
**Commits**: `fed2124` → `a22c55f` (4 commits)
**Image flair**: *Musical staff fragment — clef, time signature, notes — overlaid on a building elevation*

The library received its identity. Batches 12–13 completed: 217 directories, ~2,170 files — the full scope. Then the 52 playing cards were created, each carrying a tarot identity, an epithet, and 7 key concepts. Sixteen weak epithets were upgraded to four and five stars. Six incomplete directories were expanded to full 10-module scope.

Column, chord, canvas — the built and composed world. The content was complete. Now it had a face.

**Key commits**:
- `fed2124` Add Batches 12–13: complete reference library (217 dirs, ~2,170 files)
- `19337ac` Add tarot identity layer and upgrade card epithets across all 52 volumes
- `494f853` Expand 6 incomplete directories to full 10-module scope

**Scale**: 4 commits, library complete, identity established

---

# Phase 11: The Discoverer

**Card**: A♣ — Ace of Wands
**Date**: February 25, 2026 (night)
**Commits**: `aac0f5b`
**Image flair**: *A field of great equations — E=mc², ∇·E=ρ/ε₀, e^iπ+1=0, F=ma — arranged like stars, and one equation still being written: the ink not yet dry, the chalk still in hand*

The naming session. 52 archetype roles were matched to the 52 cards — The Architect, The Timekeeper, The Selector, The Revolutionary. Then 52 image concepts: what each card's visual should show. Not the person — the thing they produce. A proof tree. A kiln cross-section. A broken chain.

The roles were lost to a crashed session and recovered by mining conversation logs at byte offsets in a 51MB JSONL file. The image concepts were found intact in an assistant message at line 4417. Everything was saved.

The Discoverer's flair: *one equation still being written*. Because discovery is not the formula — it's the moment before.

**Key commits**:
- `aac0f5b` Add card archetype roles, image concepts, and move originals to backs/

**Scale**: 1 commit, 52 roles, 52 concepts, 54 files moved to backs/

---

# Phase 12: The Verifier

**Card**: 8♦ — Eight of Pentacles
**Date**: February 26, 2026
**Commits**: `d35cdf5` → `296b242` (~60 commits)
**Image flair**: *...the arrows drawn not by one hand but by a hundred, each state resolved in parallel, the whole machine converging at once*

The longest session in the library's history. One hundred and twenty directories swept against a four-level editorial rubric. Every file read. Every landscape diagram checked. Every Decision Cheat Sheet tested for decision-worthiness. Every claim spot-checked. Twelve hundred tags injected at the exact point of each finding — invisible in rendered output, grep-able for dashboards, gone when fixed.

The session began with a broken `.claude.json` and a lost conversation. It ended with a review skill that could orchestrate itself — agents launching agents, each one reading ten files, applying the rubric, writing tags, updating REVIEW.md, committing, and going idle. The pipeline hummed: eight agents in parallel, self-committing, results flowing in every few minutes. The Verifier's state machine resolved a hundred paths at once.

Eight directories came back perfect — every file polished, zero tags: astronomy (12 files), ethics (10), international relations (10), codes (10), spices (11), zoology (10), marine biology (10), composite materials (10). The later batches were dramatically cleaner than the early ones — the AI learned the style contract as it wrote, and by the final batches the quality was publication-ready.

The dominant finding across the library: missing old-world bridges. The content was accurate and well-structured everywhere, but the connection from each domain to what this specific reader already knows — control theory, type systems, graph algorithms, distributed systems, formal verification — was absent in roughly 60% of files. The bridge is the gap between "good reference" and "reference that clicks for this reader at 11pm."

**Key commits**:
- `d35cdf5` First sweep commit (medicine/)
- `8b98ba4` Updated review skill with sweep-batch mode
- `bca1a27` Astronomy — first perfect score (12/12 polished)
- `2019117` Ethics — second perfect score (10/10 polished)
- `296b242` Final commit (furniture/)

**Scale**: ~60 commits, ~120 directories swept, ~1,200 @editor tags injected, 8 perfect-score directories (83 polished files), 7 complete sections

---

# Phase 13: The Interpreter

**Card**: 10♥ — Ten of Cups
**Date**: February 26, 2026
**Commits**: `b51b1a6` (1 commit)
**Image flair**: *...the arrows redrawn in a second hand at each corner — relational, typed, recursive — the triangle's meaning arriving in the reader's own notation, seventy-one times over*

The Interpreter's work is translation — and translation is never free. Something is always gained and something is lost in the crossing. Seventy-one directories had been swept and tagged: the content was accurate, the structure present, but the bridges were missing. Each `@editor[bridge]` tag marked a gap in the semiotic triangle — a SIGN floating without an arrow to connect it to what this reader already knows how to signify. Phase 12 had named the disease. Phase 13 drew the arrows.

Mathematics came first: measure theory reframed as the formal extension of probability's intuitions; representation theory as the algebra behind equivariant neural networks; optimization as convergence certificates with Lipschitz constants and Nesterov lower bounds. Then the life sciences, translated not through biology's vocabulary but through engineering's — the heart as a PID controller, neurons as threshold logic units with Heaviside activations, the immune system as a distributed intrusion detection system with clonal memory. Geology became state-machine transitions between mineral phases; rhetoric became protocol analysis; sociology became graph theory with cluster coefficients. Each domain was rendered twice: once in its own language, once in the reader's native notation of systems, graphs, formal verification, and type theory.

Six sections graduated clean. Earth & Space: all 14 directories. History & Ideas: all 15. Social Sciences: 15. Language & Communication: 11. Life Sciences: 16. Mathematics: 24 files, 122 tags resolved. The semiotic triangle is not decorative — it describes what every act of teaching requires: a sign, a reader who can receive it, and an arrow that survives the crossing. This phase drew those arrows, seventy-one times over, in the reader's own hand.

**Key commits**:
- `b51b1a6` Fix 71 dirs, 575+ @editor tags resolved — bridges across all domains

**Scale**: 71 directories fixed, ~575 @editor tags resolved, 6 sections at 100% clean (Earth & Space, History & Ideas, Social Sciences, Language & Communication, Life Sciences, plus mathematics/), 543 files improved

---

---

# Phase 14: The Surveyor

**Card**: Q♦ — Queen of Diamonds
**Date**: February 26, 2026
**Commits**: `eb0f92a` → `0a74737` (~25 commits)
**Image flair**: *...59 blank territories inked in — contour lines running from valley floor to ridge — and in the lower-left corner, a correction note where the last of the old stakes were pulled: three more sections cleared*

The Surveyor's work is comprehensive mapping. Before you can fix a thing you must know where everything is. Phase 14 did two jobs: it finished the outstanding fix residuals from the previous session, then it surveyed the entire unmapped half of the library.

Job one: cleanup. Three batches of fix agents swept the remaining unresolved directories — art-history (12 tags), furniture / textiles / metalworking / glassmaking, periodic-table / mycology / animal-phylogeny / food-plants — resolving every outstanding tag. Material Culture graduated clean: all 11 directories. Natural World graduated clean: all 12. Arts & Culture partial — art-history clean, 16 others pending next pass. 197 tags resolved, three sections at 100%.

Job two: the survey. 32 parallel sweep agents fanned out across the unmapped half: Mathematics & Physics (19 directories), Mechanics (14), Technology (9), Arts & Culture (16), and the last Life Sciences holdout (cognitive-science). Each agent read every file end-to-end, applied all four levels of the rubric — structure contract, audience fit, developmental quality, content accuracy — and drove @editor stakes at every problem point. Then committed.

667 stakes planted. 86 P1 blocking issues found.

The P1 distribution maps the library's actual fault lines:

**numerical-methods** (7 P1s): The automatic differentiation → backpropagation bridge is broken across four files. Every ML engineer reading numerical-methods needs to see that AD *is* backprop — the chain rule implemented as a data structure — and those files don't say it.

**hvac** (5 P1s): Carnot efficiency is absent from the entire refrigeration chain. A VP of Engineering reads HVAC and immediately asks "what's the theoretical limit?" — the answer should be in every efficiency table. It isn't.

**topology** (5 P1s): ∞-categories and Homotopy Type Theory are entirely absent despite being the most active frontier in the field. Morse theory missing. Knot theory thin. The files cover classical topology well but stop at the tree line.

**music-theory** (4 P1s): These are the most natural missed bridges in the entire library. Fourier analysis equals harmonic series decomposition — why a chord sounds like its components. Counterpoint is constraint satisfaction programming. Sonata form is a finite state machine with named states. Any MIT TCS graduate sees these immediately. The guides didn't say them.

**cognitive-science** (4 P1s): Turing's original *Computing Machinery and Intelligence* paper formulates the Turing Test as a decidability question — can a finite judge distinguish a machine from a person? The Chomsky hierarchy is in every TCS course. VAE/ELBO connects directly to information theory. All three absent.

**complex-analysis** (4 P1s): Elliptic curves in complex analysis are the same curves as in elliptic curve cryptography — the isomorphism should be explicit. L-functions and the Riemann hypothesis are absent from what should be their home.

The pattern is consistent across every domain: the universal CS bridges — the ones that any senior engineer would immediately recognize — are the gaps. Control theory bridges to error budgets and rate limiters but not to backpressure and admission control. Materials science bridges to semiconductor manufacturing but not to the state-machine metaphor for phase transformations. Each P1 is a crossing that wasn't drawn.

All 168 directories are now swept — 167 with tags pending fix, 1 (virology) permanently blocked by content policy. The topographic map of the library's terrain is complete. The next pass draws the bridges.

**Key commits**:
- `eb0f92a` Fix art-history + Material Culture (ceramics, coatings, culinary-history, etc.) — 86 files
- `410b296` Fix furniture, textiles, metalworking, glassmaking
- `bb94143` Fix periodic-table, mycology, animal-phylogeny, food-plants
- `275dcd7` Sweep physics/ — 22 tags, 4 P1s
- `fa7b60f` Sweep topology/ — 27 tags, 5 P1s
- `f958212` Sweep architecture-history, architecture, music-theory — 35 tags, 5 P1s
- `0a74737` Sweep 59 dirs — 667 @editor tags, 86 P1s — update REVIEW.md

**Scale**: 59 new directories swept, 667 @editor tags injected, 86 P1 blocking issues, 3 sections graduated clean (Material Culture, Natural World, Arts & Culture/art-history), all 168 tracked directories now swept (virology excepted)

---

## What Comes Next

The library has content. The cards have identity. The roles have names. The image concepts have been described.

Now the cards need faces — 52 new ASCII art visuals, each illustrating the archetype's concept. The current card files (ASCII boxes with 7 key concepts) live in `cards/backs/`. The new designs will live in `cards/` as the primary face of each volume.

38 roles remain unclaimed. Years of reviews, expansions, corrections, and reimaginations ahead. Each session that does meaningful work claims a card.

---

## Cumulative Scale

| Metric | Count |
|--------|-------|
| Directories | 217 |
| Files | 2,481 |
| Lines written | 826,537 |
| Commits | ~143 |
| Days | 5 |
| Cards designed | 52 + The Fool |
| Directories reviewed | 167 of 168 (virology blocked) |
| @editor tags injected | ~1,867 |
| @editor tags resolved | ~575 |
| Tags outstanding | 667 |
| P1 blocking issues | 86 |
| Clean directories | 108 |
| Roles claimed | 14 of 52 |
| Roles remaining | 38 |
