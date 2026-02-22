# C:\src\reference — Modern Software Engineering Reference Library

## Project Purpose

This directory is a **self-authored reference library** — a collection of technical guides built
iteratively to bring a senior engineering leader current on modern software tooling, practices,
and ecosystem concepts. Each guide follows the PACKAGE.md format: layered ASCII diagrams, mental
models, practical comparisons, and decision cheat sheets. Never dumbed down.

---

## Learner Profile

| Attribute | Detail |
|-----------|--------|
| **Role** | VP of Software Engineering, Microsoft |
| **Age** | 52 |
| **Deep background** | .NET, ADO.NET, Azure Data Factory, Power Query, Power Apps |
| **Leadership gap** | ~10 years as leader, not hands-on coder |
| **Conceptual depth** | Full — compilers, linkers, runtime models, distributed systems |
| **Old tooling known** | RAID, Source Depot (MS internal VCS), VSTS → Azure DevOps, MSBuild |
| **New tooling learning** | Git (mostly there), npm/node ecosystem, containers, frontend, CI/CD |
| **Communication style** | Peer-level technical. ASCII diagrams. No handholding. Direct. |

### What Does NOT Need Explaining
- General software architecture concepts
- Compiler/linker/runtime theory
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

Follow 01-PACKAGE.md format exactly:

1. **Start with the Big Picture** — one diagram showing the whole landscape
2. **Layer downward** — each section drills into one piece
3. **Use ASCII boxes** for system diagrams, flow charts, decision trees
4. **Use tables** for comparisons and cheat sheets
5. **"Old world → new world" bridges** where the learner has prior art
6. **End with Decision Cheat Sheet** — the "what do I use when" table
7. **Common Confusion Points** section for gotchas

---

## Artifact Index

| File | Topic | Status |
|------|-------|--------|
| `01-PACKAGE.md` | Package managers — all layers | ✅ Complete |
| `02-GIT.md` | Git modern workflow — branching, PRs, remotes | ✅ Complete |
| `03-JS-TS.md` | JavaScript & TypeScript — modules, type system, transpilation | ✅ Complete |
| `04-BUILD.md` | Build tools & bundlers — Vite, Webpack, esbuild, Rollup | ✅ Complete |
| `05-FRONTEND.md` | Frontend frameworks — React, Vue, Angular, component model | ✅ Complete |
| `06-RENDERING.md` | Rendering patterns — SPA, SSR, SSG, ISR, RSC | ✅ Complete |
| `07-STATE.md` | State management — Redux, Zustand, Jotai, context | ✅ Complete |
| `08-BACKEND.md` | Backend APIs — REST, GraphQL, tRPC, OpenAPI | ✅ Complete |
| `09-DATABASE.md` | Databases modern — Postgres, ORMs, migrations, Redis | 🔜 Next |
| `10-AUTH.md` | Auth & security — OAuth2, OIDC, JWT, sessions | 🔜 Queued |
| `11-DOCKER.md` | Containers — Docker, Dockerfile, docker-compose | 🔜 Queued |
| `12-KUBERNETES.md` | Orchestration — Kubernetes concepts, deployments | 🔜 Queued |
| `13-CICD.md` | CI/CD modern — GitHub Actions vs Azure Pipelines | 🔜 Queued |
| `14-IAC.md` | Infrastructure as Code — Terraform, Bicep, Pulumi | 🔜 Queued |
| `15-OBSERVABILITY.md` | Observability — logs, metrics, tracing, OpenTelemetry | 🔜 Queued |
| `16-MONOREPO.md` | Monorepos — Turborepo, Nx, workspaces | 🔜 Queued |
| `17-CLOUD-NATIVE.md` | Cloud-native patterns — microservices, events, service mesh | 🔜 Queued |

---

## Curriculum Tracks

```
Track 1: Foundations          Track 2: JS Runtime Layer      Track 3: Frontend
  01-PACKAGE.md ✅               03-JS-TS.md ✅                 05-FRONTEND.md ✅
  02-GIT.md ✅                   04-BUILD.md ✅                 06-RENDERING.md ✅
                                                               07-STATE.md ✅
                                 (Node.js server in BACKEND)    07-STATE.md

Track 4: Backend & Data       Track 5: Infrastructure        Track 6: Operations
  08-BACKEND.md                  11-DOCKER.md                   15-OBSERVABILITY.md
  09-DATABASE.md                 12-KUBERNETES.md               16-MONOREPO.md
  10-AUTH.md                     13-CICD.md                     17-CLOUD-NATIVE.md
                                 14-IAC.md
```

---

## Session Log

| Date | What Was Done |
|------|---------------|
| 2026-02-22 | Project initialized. PACKAGE.md already authored. CLAUDE.md + README.md created. |
| 2026-02-22 | GIT.md authored. Covers three-tree model, branching, merge vs rebase, PR workflow, worktrees, old-world bridge. |
| 2026-02-22 | JS-TS.md authored. Covers JS engine/environment/spec layers, CJS vs ESM, TS type system, tsconfig, compilation pipeline. |
| 2026-02-22 | BUILD.md authored. Covers bundler genealogy, core concepts (tree-shaking, code splitting, HMR), Vite/Webpack/esbuild/Rollup/SWC/Babel, MSBuild bridge. |
| 2026-02-22 | Files renamed 01–17. CLAUDE.md and README.md references updated. |
| 2026-02-22 | 05-FRONTEND.md authored. Covers component model, React hooks, Vue, Angular, Svelte, RSC, styling approaches, WinForms/WPF/XAML bridge. |
| 2026-02-22 | 06-RENDERING.md authored. Covers CSR/SPA, SSR, SSG, ISR, streaming SSR, RSC, islands, hydration, Next.js App Router, Razor/Blazor bridge. |
| 2026-02-22 | 07-STATE.md authored. Covers state categories, useReducer, Context perf limits, Zustand, Redux Toolkit, Jotai, TanStack Query, colocation principle. |
| 2026-02-22 | 08-BACKEND.md authored. Covers REST design, HTTP verbs/status codes, OpenAPI, GraphQL, tRPC, Express/Fastify/NestJS, Zod validation, ASP.NET/WCF bridge. |

---

## Instructions for Claude

- When asked to create a new guide, follow 01-PACKAGE.md style exactly
- Check this file first to know what's done and what's queued
- Update the Artifact Index status when a file is completed
- Add an entry to the Session Log at the end of each working session
- The learner is a peer, not a student — write accordingly
- Bridge to Azure/VSTS/.NET concepts where natural — don't force it
