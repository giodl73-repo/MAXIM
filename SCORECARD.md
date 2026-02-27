# SCORECARD — Volume Quality Rubric

*Scoring rubric for the 52-card deck. Used to identify improvement targets, track quality over time, and prioritize editorial passes.*

*Each volume scores 0–5 on six dimensions. Max score = 30. Rescore after each editorial pass.*

---

## The Six Dimensions

### 1. LENGTH — Is the volume the right size for binding?

| Score | Criteria |
|-------|----------|
| 5 | 250–400 pages. Ideal binding range. |
| 4 | 200–250 or 400–450. Acceptable. |
| 3 | 150–200 or 450–500. Thin or thick but bindable. |
| 2 | 100–150 or 500–560. Problematic — very thin hardcover or near binding limit. |
| 1 | <100 or >560. Requires structural intervention (combine or split). |
| 0 | Not applicable (annex-dependent, not yet measured). |

### 2. SUIT FIT — Does the content match its suit's role?

The four suits define a progression within every section:

| Suit | Role | What to look for |
|------|------|-----------------|
| ♣ | **Foundation** | Substrate, earliest, most fundamental. Opens the section. Covers the base concepts a reader needs before the other three. |
| ♦ | **Application** | Theory meets practice. Tools, methods, applied knowledge. The "how to use it" volume. |
| ♥ | **Depth** | Technical core, advanced topics. The hardest volume in the section. Assumes ♣ and ♦. |
| ♠ | **Frontier** | Emerging, current edges, newest additions. The volume most likely to need updating. |

| Score | Criteria |
|-------|----------|
| 5 | Directories clearly embody the suit's role. Foundation feels foundational. Frontier feels cutting-edge. Natural fit. |
| 4 | Mostly fits. One directory is slightly misplaced but doesn't break the narrative. |
| 3 | Adequate but the suit identity is weak. Directories could swap between suits without much difference. |
| 2 | Poor fit. A "Foundation" volume that skips basics, or a "Frontier" volume with only established content. |
| 1 | Wrong suit. Content clearly belongs in a different volume position. |

### 3. COHESION — Do the directories within the volume belong together?

| Score | Criteria |
|-------|----------|
| 5 | Directories tell a unified story. A reader moving through them feels a natural arc. Cross-references are obvious. |
| 4 | Good grouping. One directory is slightly orphaned but still relevant to the section. |
| 3 | Functional but arbitrary. Directories share a section but could be re-grouped without loss. |
| 2 | Forced grouping. Directories feel like they were assigned to fill space rather than for thematic reasons. |
| 1 | Incoherent. Directories have no clear relationship beyond the section label. |

### 4. STYLE — Does every file follow the style contract?

Per CLAUDE.md: landscape diagram first, layered ASCII diagrams, comparison tables, old→new bridges, Decision Cheat Sheet, Common Confusion Points.

| Score | Criteria |
|-------|----------|
| 5 | Every file follows the full style contract. Diagrams do real work. Cheat sheets are actionable. Bridges connect universally. |
| 4 | Minor gaps — one file missing a cheat sheet, or a diagram that's decorative rather than structural. |
| 3 | Mixed. Some files are excellent, others are text-heavy with minimal diagrams or missing sections. |
| 2 | Significant style gaps. Multiple files missing landscape diagrams or cheat sheets. Walls of text. |
| 1 | Style contract largely ignored. Files read as prose essays, not reference guides. |

### 5. DEPTH — Is the content at the right level for the learner profile?

The learner is a peer: MIT Math + TCS, VP of Software Engineering, deep .NET/Azure/VSTS background. Never dumb down. Never over-explain known concepts.

| Score | Criteria |
|-------|----------|
| 5 | Every file hits peer level. CS foundations assumed. Bridges from old-world to new-world are precise. A Google engineer, a Rails dev, and a Python data scientist all get full value. |
| 4 | Mostly right. One file over-explains something the learner knows, or under-explains something genuinely novel. |
| 3 | Uneven. Some files are pitch-perfect, others read like they're written for a different audience (too basic or too niche). |
| 2 | Significant audience mismatch. Multiple files explain things from scratch that the learner profile already knows. |
| 1 | Wrong audience entirely. Reads like a textbook introduction or assumes no prior knowledge. |

### 6. ARCHETYPE — Does the volume embody its card's archetype role?

Each card has a named archetype (The Architect, The Taxonomist, The Healer, etc.) and an epithet. The archetype isn't just a label — the best volumes feel like they were written *by* that archetype.

| Score | Criteria |
|-------|----------|
| 5 | The archetype is palpable. The Healer volume feels like it was written by someone who treats patients. The Voyager volume makes you feel the distance. Epithet resonates on every page. |
| 4 | Good fit. The archetype works but isn't strongly felt throughout — more a label than a voice. |
| 3 | Neutral. The archetype could be swapped for another without anyone noticing. |
| 2 | Mismatch. The archetype suggests one tone (e.g., "The Brewer" → craft, fermentation, hands-on) but the content feels clinical or detached. |
| 1 | Archetype actively misleads. The name creates expectations the content doesn't meet. |

---

## Scoring Scale

| Total | Grade | Meaning |
|-------|-------|---------|
| 25–30 | **A** | Print-ready. This volume is a finished product. |
| 20–24 | **B** | Good. One or two dimensions need a targeted pass. |
| 15–19 | **C** | Adequate. Needs an editorial pass before printing. |
| 10–14 | **D** | Significant issues. Multiple dimensions below par. |
| <10 | **F** | Structural problems. May need directory reassignment or rewrite. |

---

## The Scores

*Full scoring: 2026-02-26. 13-agent content sweep + metadata analysis.*

| Card | Vol | Role | Len | Suit | Coh | Style | Depth | Arch | **Total** | **Grade** |
|------|-----|------|-----|------|-----|-------|-------|------|-----------|-----------|
| 2♣ | NW·I | The Taxonomist | 5 | 5 | 5 | 5 | 5 | 5 | **30** | **A** |
| 2♦ | NW·II | The Brewer | 4 | 5 | 5 | 5 | 5 | 5 | **29** | **A** |
| 2♥ | NW·III | The Collector | 4 | 4 | 4 | 4 | 4 | 4 | **24** | **B** |
| 2♠ | NW·IV | The Ecologist | 4 | 5 | 5 | 4 | 4 | 3 | **25** | **A** |
| 3♣ | ES·I | The Timekeeper | 4 | 5 | 5 | 4 | 4 | 3 | **25** | **A** |
| 3♦ | ES·II | The Forecaster | 4 | 5 | 5 | 5 | 5 | 4 | **28** | **A** |
| 3♥ | ES·III | The Cultivator | 4 | 4 | 4 | 4 | 4 | 3 | **23** | **B** |
| 3♠ | ES·IV | The Voyager | 4 | 5 | 4 | 3 | 5 | 4 | **25** | **A** |
| 4♣ | MC·I | The Colorist | 5 | 5 | 5 | 5 | 5 | 5 | **30** | **A** |
| 4♦ | MC·II | The Forger | 5 | 5 | 5 | 5 | 5 | 5 | **30** | **A** |
| 4♥ | MC·III | The Binder | 4 | 4 | 4 | 5 | 5 | 4 | **26** | **A** |
| 4♠ | MC·IV | The Joiner | 4 | 5 | 5 | 5 | 5 | 5 | **29** | **A** |
| 5♣ | LS·I | The Naturalist | 5 | 5 | 5 | 5 | 5 | 4 | **29** | **A** |
| 5♦ | LS·II | The Empiricist | 4 | 5 | 5 | 5 | 4 | 5 | **28** | **A** |
| 5♥ | LS·III | The Healer | 5 | 5 | 5 | 4 | 4 | 4 | **27** | **A** |
| 5♠ | LS·IV | The Selector | 5 | 5 | 4 | 5 | 5 | 5 | **29** | **A** |
| 6♣ | HI·I | The Chronicler | 3 | 5 | 5 | 5 | 5 | 5 | **28** | **A** |
| 6♦ | HI·II | The Sage | 3 | 5 | 4 | 4 | 5 | 4 | **25** | **A** |
| 6♥ | HI·III | The Dialectician | 4 | 5 | 5 | 5 | 5 | 5 | **29** | **A** |
| 6♠ | HI·IV | The Ethicist | 4 | 5 | 4 | 4 | 5 | 4 | **26** | **A** |
| 7♣ | M·I | The Constructor | 1 | 5 | 5 | 5 | 5 | 5 | **26** | **A** |
| 7♦ | M·II | The Alchemist | 2 | 5 | 5 | 4 | 4 | 3 | **23** | **B** |
| 7♥ | M·III | The Provider | 5 | 5 | 5 | 5 | 5 | 5 | **30** | **A** |
| 7♠ | M·IV | The Instrumentalist | 4 | 4 | 4 | 5 | 4 | 4 | **25** | **A** |
| 8♣ | T·I | The Fabricator | 3 | 5 | 5 | 4 | 5 | 5 | **27** | **A** |
| 8♦ | T·II | The Verifier | 4 | 5 | 5 | 5 | 5 | 5 | **29** | **A** |
| 8♥ | T·III | The Planner | 4 | 5 | 4 | 5 | 5 | 4 | **27** | **A** |
| 8♠ | T·IV | The Operator | 3 | 5 | 4 | 4 | 4 | 3 | **23** | **B** |
| 9♣ | SS·I | The Strategist | 4 | 5 | 5 | 5 | 5 | 5 | **29** | **A** |
| 9♦ | SS·II | The Governor | 3 | 5 | 4 | 4 | 5 | 5 | **26** | **A** |
| 9♥ | SS·III | The Witness | 4 | 4 | 4 | 4 | 4 | 4 | **24** | **B** |
| 9♠ | SS·IV | The Correspondent | 5 | 5 | 4 | 4 | 4 | 4 | **26** | **A** |
| 10♣ | LC·I | The Scribe | 5 | 5 | 5 | 5 | 5 | 4 | **29** | **A** |
| 10♦ | LC·II | The Broadcaster | 5 | 5 | 5 | 4 | 4 | 5 | **28** | **A** |
| 10♥ | LC·III | The Interpreter | 4 | 5 | 5 | 4 | 5 | 5 | **28** | **A** |
| 10♠ | LC·IV | The Narrator | 4 | 5 | 4 | 3 | 5 | 5 | **26** | **A** |
| J♣ | MP·I | The Experimenter | 2 | 5 | 5 | 4 | 5 | 4 | **25** | **A** |
| J♦ | MP·II | The Analyst | 5 | 5 | 4 | 5 | 5 | 5 | **29** | **A** |
| J♥ | MP·III | The Formalist | 3 | 5 | 5 | 4 | 5 | 5 | **27** | **A** |
| J♠ | MP·IV | The Theorist | 5 | 5 | 5 | 4 | 5 | 4 | **28** | **A** |
| Q♣ | AC·I | The Composer | 5 | 5 | 5 | 5 | 5 | 5 | **30** | **A** |
| Q♦ | AC·II | The Surveyor | 3 | 4 | 3 | 4 | 4 | 4 | **22** | **B** |
| Q♥ | AC·III | The Performer | 5 | 5 | 4 | 4 | 4 | 4 | **26** | **A** |
| Q♠ | AC·IV | The Editor | 4 | 5 | 4 | 3 | 3 | 2 | **21** | **B** |
| K♣ | C·I | The Architect | 5 | 5 | 5 | 5 | 5 | 5 | **30** | **A** |
| K♦ | C·II | The Craftsman | 4 | 5 | 4 | 4 | 4 | 4 | **25** | **A** |
| K♥ | C·III | The Prover | 4 | 5 | 5 | 5 | 5 | 5 | **29** | **A** |
| K♠ | C·IV | The Sentinel | 2 | 5 | 4 | 3 | 3 | 2 | **19** | **C** |
| A♣ | P·I | The Discoverer | 4 | 5 | 5 | 5 | 5 | 5 | **29** | **A** |
| A♦ | P·II | The Inventor | 2 | 5 | 5 | 4 | 4 | 5 | **25** | **A** |
| A♥ | P·III | The Visionary | 3 | 5 | 5 | 5 | 5 | 5 | **28** | **A** |
| A♠ | P·IV | The Witness | 3 | 4 | 4 | 4 | 4 | 3 | **22** | **B** |

---

## Grade Distribution

```
 A (25-30)  ████████████████████████████████████████████  42 volumes
 B (20-24)  █████████  9 volumes
 C (15-19)  █  1 volume

 Perfect 30: 2♣ NW·I · 4♣ MC·I · 4♦ MC·II · 7♥ M·III · Q♣ AC·I · K♣ C·I

 Mean: 26.5 / 30     Median: 27 / 30
```

**6 perfect scores.** 42 of 52 volumes grade A. One C (K♠). No D's or F's.

---

## Top 10 Volumes (by total score)

| Rank | Card | Vol | Total | Perfect dimensions |
|------|------|-----|-------|--------------------|
| 1 | 2♣ | NW·I — The Taxonomist | **30** | All six |
| 1 | 4♣ | MC·I — The Colorist | **30** | All six |
| 1 | 4♦ | MC·II — The Forger | **30** | All six |
| 1 | 7♥ | M·III — The Provider | **30** | All six |
| 1 | Q♣ | AC·I — The Composer | **30** | All six |
| 1 | K♣ | C·I — The Architect | **30** | All six |
| 7 | 2♦ | NW·II — The Brewer | **29** | Style, Depth, Archetype |
| 7 | 4♠ | MC·IV — The Joiner | **29** | Style, Depth, Archetype |
| 7 | 5♣ | LS·I — The Naturalist | **29** | Style, Depth |
| 7 | 5♠ | LS·IV — The Selector | **29** | Style, Depth, Archetype |

---

## Bottom 10 Volumes (priority improvement targets)

| Rank | Card | Vol | Total | Weakest Dimensions | Key Issue |
|------|------|-----|-------|-------------------|-----------|
| 52 | K♠ | C·IV — The Sentinel | **19** | Arch=2, Style=3, Depth=3 | Reads as operational guides, not unified principle. Needs cross-domain integration + theoretical grounding. |
| 51 | Q♠ | AC·IV — The Editor | **21** | Arch=2, Style=3, Depth=3 | Sports-science is thematic misfit for "The Editor." Graphics + comics excellent, rest uneven. |
| 50 | Q♦ | AC·II — The Surveyor | **22** | Coh=3, Len=3 | Five loosely related "visual" topics. Weakest cohesion in deck. |
| 49 | A♠ | P·IV — The Witness | **22** | Arch=3, Len=3 | Volume lacks thematic coherence. Three different kinds of change-makers. |
| 48 | 3♥ | ES·III — The Cultivator | **23** | Arch=3 | "Cultivator" fits agriculture but not mineralogy/planetary-science. |
| 48 | 7♦ | M·II — The Alchemist | **23** | Arch=3, Len=2 | Energy-systems orphaned; thermodynamic cycle center fragmented. |
| 48 | 8♠ | T·IV — The Operator | **23** | Arch=3, Len=3 | Design-choice focus vs. operational-behavior epithet. Archetype drift. |
| 46 | 2♥ | NW·III — The Collector | **24** | All dimensions=4 | Solid but uniform 4s. Style less aggressive, archetype more label than voice. |
| 46 | 9♥ | SS·III — The Witness | **24** | All dimensions=4 | Slightly explanatory register. Teaching vs. reference voice. |
| 44 | 2♠ | NW·IV — The Ecologist | **25** | Arch=3 | Ecologist voice thin — reads more "marine biologist explaining reefs" than systems ecologist. |

---

## Improvement Actions by Priority

### Archetype Issues (voice — fix in editorial pass)

| # | Volume | Arch Score | Issue | Action |
|---|--------|-----------|-------|--------|
| 1 | K♠ C·IV The Sentinel | **2** | Three operational domains, no unified "truth is distributed" principle | Add unifying overview: Byzantine consensus, trust models, verify-everything thesis |
| 2 | Q♠ AC·IV The Editor | **2** | Sports-science doesn't fit "design cuts to what matters" | Consider swapping sports-science to AC·III (The Performer = performance optimization) |
| 3 | 2♠ NW·IV The Ecologist | **3** | Systems-ecology voice muted | Strengthen OVERVIEW to foreground trophic dynamics, nutrient cycling, carrying capacity |
| 4 | 3♣ ES·I The Timekeeper | **3** | Deep-time persona not felt in writing voice | Astronomy lacks OVERVIEW — adding one with temporal framing would fix this |
| 5 | 3♥ ES·III The Cultivator | **3** | Only fits agriculture; mineralogy/planetary-science are discovery, not cultivation | Strengthen OVERVIEW to frame all four as "ground-level understanding" |
| 6 | 7♦ M·II The Alchemist | **3** | Thermodynamic transformation center is fragmented | Strengthen energy-systems; tie chemical-eng + nuclear + energy via exergy narrative |
| 7 | 8♠ T·IV The Operator | **3** | Design-selection focus, not operational dynamics | Add real-time decision-making content: grid response, load forecasting, nano fabrication control |
| 8 | A♠ P·IV The Witness | **3** | Three kinds of change-makers, not unified | Strengthen OVERVIEW thesis: "leverage points in systems" as the unifying principle |

### Style Issues (contract compliance — fix in content pass)

| # | Volume | Style Score | Issue | Action |
|---|--------|-----------|-------|--------|
| 1 | K♠ C·IV | **3** | No cross-volume integration diagram | Add unified Sentinel diagram showing consensus → authority → trust |
| 2 | Q♠ AC·IV | **3** | Fashion is market-analysis, not design-method; sports-science missing cheat sheet | Tighten to design principles |
| 3 | 10♠ LC·IV | **3** | More essayistic/humanistic than chart-driven | Add decision cheat sheets; strengthen ASCII diagram density |
| 4 | 3♠ ES·IV | **3** | Remote-sensing directory may be thin/missing | Verify remote-sensing content completeness |

### Length Issues (structural — accept or expand)

| # | Volume | Pages | Action |
|---|--------|-------|--------|
| 1 | 7♣ M·I | 124 | Accept as thin — content scored 5/5/5 on substance |
| 2 | 7♦ M·II | 173 | Expand energy-systems to strengthen both length and archetype |
| 3 | K♠ C·IV | 186 | Frontier dirs grow naturally; also needs depth/archetype work |
| 4 | A♦ P·II | 187 | Biographical — accept; deepen explorer technical substrate |

---

## Revision History

| Date | Pass | Dimensions Scored | Notes |
|------|------|------------------|-------|
| 2026-02-26 | First | Length, Suit Fit, Cohesion | Metadata-only pass from VOLUMES.md |
| 2026-02-26 | Second | Style, Depth, Archetype | 13-agent content sweep. All 52 volumes fully scored. |

---

*This file is the quality dashboard. VOLUMES.md is the structural source of truth. Together they tell you what to print and what to fix first.*
