# C:\src\reference — Reference Library

## Project Purpose

A **self-authored reference library** organized by field. Each field is a subdirectory containing numbered guides. Every guide follows the same format: layered ASCII diagrams, mental models, practical comparisons, and decision cheat sheets. Never dumbed down.

---

## Library Structure

The library is organized into 11 MkDocs sections. Section landing pages live in `sections/`. Full status in `TRACKER.md`. Expansion process in `EXPANSION.md`.

**Target: 168 directories · ~1,680 content files · ~15,000 printed pages · ~38 bound volumes**
Batches 1–6 complete (120 directories). Batches 7–10 scaffolded (48 directories, stubs).

```
reference/
├── sections/                  ← 11 MkDocs section landing pages (navigation layer)
│
├── Computing & Software       10 directories
│   computing/ · ai-engineering/ · data-science/ · languages/ · query-languages/
│   scripting/ · os/ · cryptography/
│   computer-architecture/ · machine-learning-theory/                    [Batch 8D/10A]
│
├── Mathematics & Physics      20 directories
│   mathematics/ · physics/ · electronics/ · materials/ · quantum-computing/
│   control-theory/ · signal-processing/ · information-theory/
│   number-theory/ · abstract-algebra/ · topology/
│   probability-statistics/ · differential-geometry/ · numerical-methods/ [Batch 6]
│   complex-analysis/ · fluid-dynamics/ · statistical-mechanics/          [Batch 7A]
│   partial-differential-equations/ · variational-calculus/ · lie-groups/ [Batch 7B]
│
├── Engineering                23 directories
│   mechanical/ · structural/ · aeronautics/ · chemical-eng/ · nuclear/
│   energy-systems/ · electrical-grid/ · hvac/ · plumbing/ · construction-materials/
│   semiconductor-manufacturing/ · telecommunications/ · acoustics/
│   robotics/ · optics/ · biomedical-engineering/ · formal-methods/
│   transportation/ · urban-planning/ · environmental-engineering/
│   manufacturing/ · systems-engineering/ · materials-processing/         [Batch 8B]
│
├── Life Sciences              18 directories
│   natural-sciences/ · biology/ · botany/ · ecology/ · human-biology/
│   neuroscience/ · cognitive-science/ · disease/ · medicine/ · nutrition/
│   genomics/ · immunology/ · microbiology/                               [Batch 6]
│   evolutionary-biology/ · virology/ · biophysics/                       [Batch 7C]
│   pharmacology/ · developmental-biology/                                [Batch 10A]
│
├── Earth & Space              14 directories
│   astronomy/ · geography/ · geology/ · meteorology/ · climate-science/
│   oceanography/ · hydrology/ · paleontology/ · agriculture/ · mineralogy/ [Batch 6]
│   planetary-science/ · geochemistry/ · space-exploration/               [Batch 9B]
│   astrobiology/                                                          [Batch 10D]
│
├── History & Ideas            15 directories
│   historical-geography/ · history-of-science/ · economic-history/ · military-history/
│   anthropology/ · philosophy/ · mythology/ · religious-studies/ · archaeology/ [Batch 6]
│   logic/ · intellectual-history/ · social-history/                      [Batch 8A]
│   political-history/ · philosophy-of-mind/ · ethics/                    [Batch 10D/10B]
│
├── Social Sciences            16 directories
│   economics/ · finance/ · behavioral-economics/ · political-science/ · law/
│   psychology/ · sociology/ · organizational-behavior/ · game-theory/
│   statistics-applied/ · public-health/ · demography/
│   criminology/ · media-studies/ · education/ · international-relations/ [Batch 8C/10B]
│
├── Language & Communication   12 directories
│   linguistics/ · world-languages/ · codes/ · typography/
│   printing-publishing/ · cinema-film/ · radio-television/
│   literature/ · rhetoric/                                                [Batch 6]
│   philosophy-of-language/ · semiotics/ · translation/                   [Batch 8D/10B]
│
├── Arts & Culture             17 directories
│   art-history/ · architecture-history/ · architecture/ · music-theory/
│   photography/ · colors/ · cartography/ · games-history/ · sports-history/ · watchmaking/
│   theater-performance/                                                   [Batch 6]
│   dance/ · industrial-design/ · marine-biology/                         [Batch 7D]
│   graphic-design/ · fashion/ · comics-sequential-art/ · sports-science/ [Batch 9D/10C]
│
├── Material Culture           11 directories
│   pigments/ · coatings/ · textiles/ · ceramics/ · glassmaking/ · jewelry/ · metalworking/
│   plastics-polymers/ · papermaking/ · composite-materials/              [Batch 9C]
│   furniture/                                                             [Batch 10C]
│
└── Natural World              12 directories
    periodic-table/ · animal-phylogeny/ · spices/ · food-plants/ · culinary-history/
    fermentation-spirits/ · mycology/                                      [Batch 6]
    marine-biology/ · entomology/ · ornithology/ · zoology/ · horticulture/ [Batch 7D/9A/10C]
```

### Batch Status

| Batch | Directories | Status |
|-------|-------------|--------|
| 1–5 | 60 directories | ✅ Complete |
| 6 | 12 directories (probability-statistics, differential-geometry, numerical-methods, genomics, immunology, microbiology, literature, theater-performance, rhetoric, mineralogy, archaeology, mycology) | ✅ Complete |
| 7 | 12 directories (complex-analysis, fluid-dynamics, statistical-mechanics, partial-differential-equations, variational-calculus, lie-groups, evolutionary-biology, virology, biophysics, dance, industrial-design, marine-biology) | 🔜 Stubs scaffolded |
| 8 | 12 directories (logic, intellectual-history, social-history, manufacturing, systems-engineering, materials-processing, criminology, media-studies, education, philosophy-of-language, semiotics, computer-architecture) | 🔜 Stubs scaffolded |
| 9 | 12 directories (entomology, ornithology, zoology, planetary-science, geochemistry, space-exploration, plastics-polymers, papermaking, composite-materials, graphic-design, fashion, comics-sequential-art) | 🔜 Stubs scaffolded |
| 10 | 12 directories (machine-learning-theory, pharmacology, developmental-biology, political-history, translation, international-relations, furniture, horticulture, sports-science, astrobiology, philosophy-of-mind, ethics) | 🔜 Stubs scaffolded |

---

## Learner Profile

| Attribute | Detail |
|-----------|--------|
| **Role** | VP of Software Engineering, Microsoft |
| **Age** | 52 |
| **Education** | MIT double major — Mathematics + Theoretical Computer Science |
| **Deep background** | .NET, ADO.NET, Azure Data Factory, Power Query, Power Apps |
| **Leadership gap** | ~10 years as leader, not hands-on coder |
| **Conceptual depth** | Full — compilers, linkers, runtime models, distributed systems |
| **Old tooling known** | RAID, Source Depot (MS internal VCS), VSTS → Azure DevOps, MSBuild |
| **New tooling learning** | Git (mostly there), npm/node ecosystem, containers, frontend, CI/CD |
| **Communication style** | Peer-level technical. ASCII diagrams. No handholding. Direct. |

### What Does NOT Need Explaining
- General software architecture concepts
- Compiler/linker/runtime theory (MIT TCS — knows this deeply)
- Automata, formal languages, computability theory (MIT TCS)
- Type theory, lambda calculus fundamentals (MIT TCS)
- Database fundamentals
- CI/CD philosophy (they built it at VSTS)
- Azure services context (they worked on Azure)

### What DOES Need Explaining
- The specific modern *tools* — npm vs pnpm vs yarn, Docker CLI, etc.
- How things nest and relate — the layered mental model
- What replaced what from the old world
- Naming conventions and ecosystem vocabulary

---

## Style Contract

Follow `computing/01-PACKAGE.md` format exactly:

1. **Start with the Big Picture** — one diagram showing the whole landscape
2. **Layer downward** — each section drills into one piece
3. **Use ASCII boxes** for system diagrams, flow charts, decision trees
4. **Use tables** for comparisons and cheat sheets
5. **"Old world → new world" bridges** where the learner has prior art
6. **End with Decision Cheat Sheet** — the "what do I use when" table
7. **Common Confusion Points** section for gotchas

---

## Instructions for Claude

- When asked to create a new guide, follow `computing/01-PACKAGE.md` style exactly
- New guides go in the appropriate field directory — check the section map above
- Check `TRACKER.md` to know what's done, what's stubbed, and what's queued
- Update `TRACKER.md` when a file is completed (not this file)
- The learner is a peer, not a student — write accordingly
- Bridge to Azure/VSTS/.NET concepts where natural — don't force it
- **32,000 token limit**: keep each guide file under ~32,000 tokens. Split into Part 1 / Part 2 if a topic runs long.
- **Section landing pages**: `sections/` holds one landing page per MkDocs section. When adding a new directory, add it to the relevant `sections/*.md` Directories table and wire it into `.mkdocs/mkdocs.yml`. See `EXPANSION.md` for the full process.
- **AGENT PERMISSION BUG — CRITICAL**: Background agents (`run_in_background: true`) cannot get Write/Bash permissions approved — the approval dialog never shows, so writes are silently blocked and the agent fails. **Always spawn file-writing agents in the foreground** (omit `run_in_background`) OR use `mode: "bypassPermissions"`. For large multi-session content generation, write files directly in the main conversation rather than delegating to background agents.
