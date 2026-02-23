# C:\src\reference — Reference Library

## Project Purpose

A **self-authored reference library** organized by field. Each field is a subdirectory containing numbered guides. Every guide follows the same format: layered ASCII diagrams, mental models, practical comparisons, and decision cheat sheets. Never dumbed down.

---

## Library Structure

```
reference/
│
│  SESSION 1 — Modern Software Engineering
├── computing/          28 modules (25 complete + 3 stubs)
├── data-science/       17 modules (6 complete + 11 stubs)
├── ai-engineering/     5 modules — COMPLETE
│
│  SESSION 2 — Physics, Mathematics & Electronics
├── mathematics/        22 modules (19 complete + 3 stubs)
├── physics/            10 modules — COMPLETE
├── electronics/        8 modules — COMPLETE
├── materials/          7 modules — COMPLETE
│
│  SESSION 3 — Programming Languages
├── languages/          19 files — COMPLETE
│
│  SESSION 4 — Query Languages
├── query-languages/    13 files — COMPLETE
│
│  SESSION 5 — Scripting Languages
├── scripting/          10 files — COMPLETE
│
│  SESSION 6 — Operating Systems
├── os/                 8 files — COMPLETE
│
│  SESSION 7 — Natural Sciences
├── natural-sciences/   16 files (14 complete + 2 stubs)
│
│  SESSION 8 — Astronomy & Planetary Sciences
├── astronomy/          12 files — COMPLETE
│
│  Specialized Tracks
├── neuroscience/       5 files — COMPLETE
├── economics/          5 files — COMPLETE
├── information-theory/ 5 files — COMPLETE
├── biology/            7 files (2 complete + 5 stubs)
│
│  PLANNED
├── philosophy/         7 stubs
├── aeronautics/        6 stubs
├── mechanical/         6 stubs
├── structural/         5 stubs
├── chemical-eng/       6 stubs
├── nuclear/            6 stubs
├── quantum-computing/  5 stubs
├── control-theory/     5 stubs
└── finance/            5 stubs
```

**Full status in `TRACKER.md`.**

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
- New guides go in the appropriate field directory (`computing/`, `data-science/`, etc.)
- Check `TRACKER.md` to know what's done, what's stubbed, and what's queued
- Update `TRACKER.md` when a file is completed (not this file)
- The learner is a peer, not a student — write accordingly
- Bridge to Azure/VSTS/.NET concepts where natural — don't force it
- **32,000 token limit**: keep each guide file under ~32,000 tokens. Split into Part 1 / Part 2 if a topic runs long.
- **AGENT PERMISSION BUG — CRITICAL**: Background agents (`run_in_background: true`) cannot get Write/Bash permissions approved — the approval dialog never shows, so writes are silently blocked and the agent fails. **Always spawn file-writing agents in the foreground** (omit `run_in_background`) OR use `mode: "bypassPermissions"`. For large multi-session content generation, write files directly in the main conversation rather than delegating to background agents.
