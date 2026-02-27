# Library Assets — Available for Puzzle Hunt Use

These assets exist in the reference library. The puzzle hunt currently uses some of them. Which ones should be used more, and how?

---

## 1. The 52 Content Volumes
~2,178 files across 206 directories. 13 sections. 5 million words. Every guide follows the same format: landscape diagram, layered detail, ASCII boxes, comparison tables, old→new bridges, decision cheat sheets.

## 2. Concept Index (`CONCEPT-INDEX.md`)
314 cross-cutting entries. Each entry = a term that appears substantively in 2+ sections, with links to every file where it's discussed. Top entries span 13 sections (water, iron, gravity). Built by 8 parallel extraction agents.

## 3. Card Backs (`cards/backs/*.md`)
52 ASCII card frames. Each card back has: playing card identity, tarot correspondence, **7 key concepts** (specific formulas, terms, principles from that volume), directory list, and epithet. Example — K♣: `TM: tape · head · state · δ(q,s)→(q,s,d)` / `Church-Turing thesis · decidability` / `Transformer: Q·K·V attention → token`.

## 4. Card Front Descriptions (`cards/CONCEPTS.md`)
52 image prompts describing card art. No actual artwork exists yet — only textual descriptions. Example — 7♦ The Alchemist: "An energy diagram — reactants at high energy, products at low, activation barrier, ΔH arrow down."

## 5. Card Roles (`cards/ROLES.md`)
52 archetype names and one-line epithets. Example — 3♣ The Timekeeper: "Stars above, strata below, deep time between."

## 6. Bill of Materials (`BILL-OF-MATERIALS.md`)
Master table of contents. Every volume's card identity, directory name, file count, chapter list (every .md file with title), word count, line count. 206 directories · 2,178 files · 869,672 lines · 5,063,843 words.

## 7. Reading Maps (`READING-MAPS.md`)
7 curated learning paths through the 52 volumes. ASCII subway-style route maps. Named paths: The Engineer, The Physicist, The Generalist, The Theorist, The Builder, The Naturalist, The Historian. Each path = 8-12 volumes with one sentence per stop.

## 8. Prerequisite Graph (`PREREQUISITES.md`)
Dependency table: which volumes assume knowledge from which others. ~20-30 hard dependencies. Most volumes are self-contained. The graph captures where reading order genuinely matters.

## 9. Atlas (`atlas/`)
52 survival-oriented maps planned (3 built so far). Tectonic plates, global winds, world soils, mountain passes, ocean currents, trade routes, etc. Card-mapped. ASCII cross-sections + SVG geographic maps.

## 10. Section Landing Pages (`sections/*.md`)
14 pages, one per MkDocs section. Each has a directory table listing all volumes in that section with descriptions.

## 11. Read This First (`read-this-first/`)
13 survival-oriented files. Card 0 / The Fool. Topics: Water, Fire, Shelter, Navigation, First Aid, Food, Tools, Signals, Weather, Hazards, Community, Psychology, Warnings.

## 12. HISTORY.md
Chronicle of how the library was built. 22 phases, each claiming a card archetype role. Dates, commits, narrative descriptions, cumulative scale. The story of building the encyclopedia.

## 13. SCORECARD.md
6-dimension quality scores for all 52 volumes: Length, Suit Fit, Cohesion, Style, Depth, Archetype. Each scored 0-5. Mean 26.5/30. 42 A's, 9 B's, 1 C.

## 14. MkDocs Site (`.mkdocs/mkdocs.yml`)
The encyclopedia renders as a navigable website with search, tabs, section navigation. Material for MkDocs theme. EB Garamond text, JetBrains Mono code.

## 15. Style Contract (from `CLAUDE.md`)
Every guide follows: (1) big picture diagram, (2) layer downward, (3) ASCII boxes for diagrams, (4) tables for comparisons, (5) old→new bridges, (6) Decision Cheat Sheet, (7) Common Confusion Points.

## 16. Card Identity System (from `cards/backs/INDEX.md`)
Suits = volume position + element (♣=Fire/Foundation, ♦=Earth/Application, ♥=Water/Depth, ♠=Air/Frontier). Ranks = section + tarot archetype. Full mapping of 52 cards to tarot, elements, and volume positions.
