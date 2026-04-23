# MAXIM — A Reference Library

> A personal encyclopedia of what humans know, organized as a deck of cards.
> 13 sections · 4 volumes each · 52 volumes total · ~2,170 guides · ~14,070 pages.

Every guide follows the same shape: **landscape diagram first, then layers downward, decision cheat sheet at the end.** ASCII throughout, no pictures that can't be reproduced with a typewriter. Written for a capable reader — enough structure to navigate a field you haven't studied, enough depth to stay useful after you have.

---

## Start Here

| If you're... | Go to |
|---|---|
| New to the library | [`FOREWORD.md`](FOREWORD.md) — why it exists, how to use it |
| Looking for a specific topic | [`index.md`](index.md) — linked entry points for every section |
| Wondering what's covered | [`TRACKER.md`](TRACKER.md) — full status, 217 directories |
| Looking for a reading path | [`READING-MAPS.md`](READING-MAPS.md) — 13 curated routes through the library |
| Curious about cross-connections | [`CONCEPT-INDEX.md`](CONCEPT-INDEX.md) — ideas that recur across sections |
| Building physical volumes | [`BILL-OF-MATERIALS.md`](BILL-OF-MATERIALS.md) · [`VOLUMES.md`](VOLUMES.md) · [`COLOPHON.md`](COLOPHON.md) |

---

## The 13 Sections

Each section has its own landing page with a landscape diagram, directory map, and curated entry points. For per-directory file counts and coverage detail, see [`TRACKER.md`](TRACKER.md).

| # | Section | Landing Page |
|---|---|---|
| 1 | Computing & Software | [`sections/computing-software.md`](sections/computing-software.md) |
| 2 | Mathematics & Physics | [`sections/mathematics-physics.md`](sections/mathematics-physics.md) |
| 3 | Mechanics *(classical engineering, antiquity → ~1900)* | [`sections/mechanics.md`](sections/mechanics.md) |
| 4 | Technology *(modern engineering, 1900 →)* | [`sections/technology.md`](sections/technology.md) |
| 5 | Life Sciences | [`sections/life-sciences.md`](sections/life-sciences.md) |
| 6 | Earth & Space | [`sections/earth-space.md`](sections/earth-space.md) |
| 7 | History & Ideas | [`sections/history-ideas.md`](sections/history-ideas.md) |
| 8 | Social Sciences | [`sections/social-sciences.md`](sections/social-sciences.md) |
| 9 | Language & Communication | [`sections/language-communication.md`](sections/language-communication.md) |
| 10 | Arts & Culture | [`sections/arts-culture.md`](sections/arts-culture.md) |
| 11 | Material Culture | [`sections/material-culture.md`](sections/material-culture.md) |
| 12 | Natural World | [`sections/natural-world.md`](sections/natural-world.md) |
| 13 | People *(the Ace — origin and culmination)* | [`sections/people.md`](sections/people.md) |

All 13 sections are **complete**. Batches 1–13 done; full library reviewed and clean.

---

## Companions & Projects

Standalone works that extend the core library.

| Project | What it is |
|---|---|
| [`atlas/`](atlas/00-OVERVIEW.md) | **Atlas** — SVG hybrid maps with Natural Earth coastlines. 52 maps planned, one per volume. |
| [`naturalis/`](naturalis/00-OVERVIEW.md) | **Naturalis** — visual companion to the Natural World section (silhouettes, plates, specimens). |
| [`puzzle-hunt/`](puzzle-hunt/) | **Puzzle Hunt** — layered cryptographic puzzle embedded across the library. |
| [`joker/`](joker/) | **Joker** — the 53rd card. Hidden companion to the deck. |
| [`cards/`](cards/) | **Cards** — one-page summaries, one per volume. |
| [`read-this-first/`](read-this-first/) | **Volume 0** — water, fire, shelter, food, healing, and how to copy these books by hand. |

Full list of library-level initiatives: [`PROJECTS.md`](PROJECTS.md). Expansion process: [`EXPANSION.md`](EXPANSION.md).

---

## Style Contract

Every file follows the format established in [`computing/01-PACKAGE.md`](computing/01-PACKAGE.md):

1. **Landscape diagram first** — one picture of the whole territory.
2. **Layer downward** — each section drills into one piece.
3. **ASCII boxes** for system diagrams, flow charts, decision trees.
4. **Tables** for comparisons and cheat sheets.
5. **Old-world → new-world bridges** where prior art exists (universal CS concepts first, widely-known tools second, stack-specific last).
6. **Decision Cheat Sheet** at the end — the "what do I use when" table.
7. **Common Confusion Points** — gotchas called out explicitly.

No guide assumes you're a beginner. No guide assumes you already know the topic. Details in [`CLAUDE.md`](CLAUDE.md).

---

## Review System

Guides are reviewed with inline `@editor` HTML comments that are grep-able as a live dashboard:

```bash
grep -rn "@editor"         # all outstanding issues
grep -rn "@editor\[.*P1"   # blocking issues only
```

Types: `stub` · `structure` · `audience` · `diagram` · `bridge` · `content`. Priorities: `P1` (blocking) · `P2` (degrades) · `P3` (polish). Workflow and examples in [`CLAUDE.md`](CLAUDE.md).

---

## How This Was Made

Written in February 2026 with AI assistance. The author directed structure, style, audience, and scope. The AI did the heavy lifting of composition across 217 directories and ~2,170 files. Every guide was then reviewed, tagged for issues, and revised until clean. See [`HISTORY.md`](HISTORY.md) for session history and [`FOREWORD.md`](FOREWORD.md) for the philosophy.

---

## License

Content is licensed under [CC BY-SA 4.0](LICENSE.md) — copy, translate, and redistribute freely. The most durable backup is the number of copies in the number of hands in the number of places. Make more.
