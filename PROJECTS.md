# MAXIM — Project Roadmap

Master tracker for library-level artifacts beyond the 52 content volumes. Each project has a status, a scope, and a home.

**Content volumes**: tracked in `TRACKER.md` (192 directories, ~1,800 files)
**Editorial quality**: tracked in `REVIEW.md` (@editor tags, sweep/fix progress)
**Phase history**: tracked in `HISTORY.md` (card roles, session chronicle)

This file tracks everything else.

---

## Active Projects

### 1. Editorial Fix Pass
**Status**: 🔄 In progress
**Home**: `REVIEW.md`
**Skill**: `/reference-review fix <dir>` · `/reference-review fix-batch <section>`
**Scope**: ~695 @editor tags across 58 directories. 95 P1s, 541 P2s, 57 P3s.
**Goal**: Zero outstanding tags → all 168 directories at "polished" status.
**Notes**: Fix skill added to `/reference-review`. First batch of 8 parallel agents launched 2026-02-26. Manufacturing test fix verified quality before scale-up.

---

### 2. Concept Index
**Status**: 🟡 Skill built, pilot complete, full build pending
**Home**: `CONCEPT-INDEX.md`
**Skill**: `/reference-index build` · `/reference-index update <dir>`
**Scope**: Cross-cutting concept index — entries for terms discussed substantively in 2+ sections. Estimated 400-600 entries at full scale.
**Pilot**: 10-directory pilot produced 89 entries. Format proven: `**Term** — [dir/NN](dir/NN-FILENAME.md)` with MkDocs links.
**Next**: Full build after fix pass completes (content needs to be stable before indexing).

---

### 3. Bill of Materials
**Status**: ❌ Not started
**Home**: `BILL-OF-MATERIALS.md` (proposed)
**Skill**: None yet
**Scope**: Master table of contents across all 52 volumes. For each volume:
- Card identity (suit, rank, tarot name, epithet)
- Directory name and file count
- Chapter list (every .md file with its title)
- Word/line count
- Status (polished / draft / stub)

**Purpose**: The "back of the box." One page that answers: what's in this library?
**Notes**: Mechanically derivable — scan every directory, read first heading of each file, count lines. Could be auto-generated and refreshed by a skill.

---

### 4. Reading Maps
**Status**: ❌ Not started
**Home**: `READING-MAPS.md` (proposed)
**Skill**: None yet
**Scope**: 5-7 curated learning paths through the 52 volumes. Each path is a sequence of 8-12 volumes with one sentence per stop explaining why it's next.

**Proposed paths**:

| Path | Theme | Key volumes |
|------|-------|-------------|
| The Engineer | Build things that work | K♣ Computing → 8♣ Technology → 7♣ Mechanics → J♣ Electronics |
| The Physicist | From measurement to theory | J♣ → J♦ → J♥ → J♠ (the four Jacks) |
| The Generalist | Breadth-first through all 13 sections | One volume per section, chosen for accessibility |
| The Theorist | Mathematical foundations → applications | J♥ Formalist → J♠ Theorist → K♥ Prover → 5♠ Selector |
| The Builder | Material culture → construction | 4♣ → 4♦ → 4♥ → 7♣ → 7♥ → 8♣ |
| The Naturalist | Living world from atom to ecosystem | 5♣ → 2♣ → 2♠ → 3♥ → 3♦ |
| The Historian | Ideas through time | 6♣ → 6♦ → 6♥ → 6♠ (the four Sixes) |

**Format**: ASCII subway-style maps showing the route with branches and cross-connections. Not just a list — a visual map.

---

### 5. Prerequisite Graph
**Status**: ❌ Not started
**Home**: `PREREQUISITES.md` (proposed)
**Skill**: None yet
**Scope**: Dependency table showing which volumes assume knowledge from which other volumes. Not a full DAG (most volumes are self-contained) — just the real dependencies.

**Format**:
```
Volume                     Assumes
─────────────────────────────────────────────
quantum-computing/         mathematics/ (probability, linear algebra)
complex-analysis/          mathematics/ (calculus, topology basics)
signal-processing/         mathematics/ (Fourier), electronics/
...
```

**Notes**: Most volumes should be readable standalone. The graph captures the ~20-30 hard dependencies where reading order genuinely matters. Pairs with Reading Maps — the maps are curated paths, the graph is the raw dependency data.

---

### 6. Atlas — Survival Reference Maps
**Status**: ❌ Not started
**Home**: `atlas/` directory (proposed)
**Skill**: None yet
**Scope**: ASCII reference maps focused on survival-relevant natural features. NOT political maps. The features that matter when infrastructure is gone.

**Proposed structure**:

```
atlas/
├── 00-OVERVIEW.md          World overview — continents, oceans, major currents
├── 01-NORTH-AMERICA.md     Mountain ranges, rivers, watersheds, passes, coasts
├── 02-SOUTH-AMERICA.md     Andes, Amazon basin, Patagonia, altiplano
├── 03-EUROPE.md            Alps, Pyrenees, Scandinavian range, Rhine/Danube
├── 04-AFRICA.md            Rift Valley, Sahara, Congo basin, Great Lakes
├── 05-ASIA.md              Himalayas, Steppes, Yangtze/Mekong, Siberia
├── 06-OCEANIA.md           Great Dividing Range, NZ Alps, Pacific islands
├── 07-ARCTIC-ANTARCTIC.md  Polar regions, ice sheets, passages
├── 08-OCEANS-CURRENTS.md   Gulf Stream, thermohaline, gyres, trade winds
├── 09-MOUNTAIN-RANGES.md   Global mountain systems — all major ranges compared
├── 10-RIVERS-WATERSHEDS.md Global river systems — length, discharge, basins
├── 11-CLIMATE-ZONES.md     Köppen zones, growing seasons, rainfall patterns
├── 12-RESOURCES.md         Major mineral deposits, freshwater, arable land
```

**Content per regional file**:
- ASCII map of the region showing terrain (mountains, rivers, coasts)
- Key elevations and passes (traversable routes)
- Watershed boundaries (which rivers drain where)
- Climate and growing season notes
- Resource locations (water, arable land, minerals)
- Historical movement corridors (why people went where they went)

**Design principle**: Ties to Read This First. If you have the survival guide and the atlas, you can orient yourself on the planet. The atlas answers "where am I and what's around me?" — the survival guide answers "now what do I do?"

**Notes**: 12 files, ~same scale as a content directory. Could be a 53rd volume (The Joker?) or filed under Earth & Space.

---

## Planned / Ideas

These are logged for future consideration. No commitment yet.

### Colophon
How the library was built. AI-assisted, 5 days, card deck metaphor, toolchain (MkDocs Material, EB Garamond). Derivable from HISTORY.md but reader-facing rather than internal.

### Bibliography Stubs
Per-volume "further reading" — canonical textbooks and papers. Enormous scope (52 volumes × 5-10 sources each = 250-500 references). Low priority but high long-term value.

### Glossary
Definitions of key terms. Overlaps with Concept Index (which gives locations, not definitions). Possibly redundant — revisit after full index build.

### How to Use This Library
Reader-facing guide: how to navigate, what the card symbols mean, how bridges work, what the style contract promises. Currently implicit in CLAUDE.md — could be extracted into a reader-facing version.

---

## Status Summary

| # | Project | Status | Files | Blocking? |
|---|---------|--------|-------|-----------|
| 1 | Editorial Fix Pass | 🔄 In progress | REVIEW.md | Blocks Index build |
| 2 | Concept Index | 🟡 Pilot done | CONCEPT-INDEX.md | Blocked by #1 |
| 3 | Bill of Materials | ❌ Not started | — | Independent |
| 4 | Reading Maps | ❌ Not started | — | Benefits from #5 |
| 5 | Prerequisite Graph | ❌ Not started | — | Independent |
| 6 | Atlas | ❌ Not started | — | Independent |

**Dependency chain**: Fix Pass → Concept Index (content must stabilize before indexing)
**Everything else is independent** — can be built in any order.
