# Modern Software Engineering — Reference Library

> A self-authored technical reference for a senior engineering leader re-entering hands-on work.
> Every guide follows the same format: layered diagrams, mental models, decision cheat sheets.
> No dumbing down. Pure signal.

---

## How This Works

Each module is a standalone `.md` file in this directory. Read them in track order or jump to
whatever you're working with. Every file answers three questions:

1. **What is this thing and where does it sit in the stack?**
2. **How does it relate to the things I already know?**
3. **What do I actually reach for, and when?**

---

## Completed Modules

| Module | File | Description |
|--------|------|-------------|
| Package Management | [`PACKAGE.md`](./PACKAGE.md) | All package managers, all layers — system, language, meta. npm, pip, nuget, cargo, docker. How they nest. |

---

## Curriculum

### Track 1 — Foundations

> The new plumbing. Things that replaced Source Depot, MSBuild, and shared drives.

| # | Module | File | Bridge From |
|---|--------|------|-------------|
| 1.1 | Package Management | [`PACKAGE.md`](./PACKAGE.md) ✅ | NuGet, MSBuild references |
| 1.2 | Git Modern Workflow | `GIT.md` | Source Depot, VSTS check-ins |

```
Source Depot / VSTS          Git + GitHub / Azure DevOps
==================           ===========================
shelve                   ->  stash
check in                 ->  commit + push
branch                   ->  branch (cheap, local, everywhere)
code review in VSTS      ->  Pull Request
gated build              ->  branch protection + CI checks
enlist                   ->  clone
sync                     ->  fetch + pull
```

---

### Track 2 — JavaScript Runtime Layer

> JavaScript escaped the browser. Understanding this layer unlocks everything in modern web dev.

| # | Module | File | What You'll Understand After |
|---|--------|------|------------------------------|
| 2.1 | JavaScript & TypeScript | `JS-TS.md` | Why TypeScript exists, ES modules vs CommonJS, how TS becomes JS |
| 2.2 | Build Tools & Bundlers | `BUILD.md` | What Vite/Webpack actually do, why you need them, dev vs prod builds |

```
The JS Runtime Layer

  Browser JS (1995-2009)       Node.js (2009-now)          Runtimes (2020-now)
  ====================         ====================         ===================
  Runs in browser only         Runs on the server           Deno, Bun
  No modules                   CommonJS modules (require)   ES modules native
  No packages                  npm ecosystem                Web standards API
  DOM only                     Full OS access               V8 / JavaScriptCore
```

---

### Track 3 — Frontend

> The browser as an application platform. This is where Power Apps concepts translate.

| # | Module | File | What You'll Understand After |
|---|--------|------|------------------------------|
| 3.1 | Frontend Frameworks | `FRONTEND.md` | React vs Vue vs Angular, component model, JSX |
| 3.2 | Rendering Patterns | `RENDERING.md` | SPA vs SSR vs SSG vs ISR vs RSC — when each one wins |
| 3.3 | State Management | `STATE.md` | Redux, Zustand, context — the state problem and its solutions |

```
Rendering Strategy Spectrum

  ←— more server                                    more client —→

  Static Site    SSR           SSR + hydration    SPA           CSR
  (HTML files)   (per request) (Next.js / Nuxt)   (React app)   (raw fetch)

  Fastest CDN    Fresh data    Best of both       Rich UX       Simple
  No JS needed   SEO good      SEO + interactivity JS heavy     JS heavy
```

---

### Track 4 — Backend & Data

> APIs, databases, and auth. The service layer you built in .NET, now in Node/Python/Go.

| # | Module | File | What You'll Understand After |
|---|--------|------|------------------------------|
| 4.1 | Backend APIs | `BACKEND.md` | REST vs GraphQL vs tRPC, OpenAPI/Swagger, Express/Fastify |
| 4.2 | Databases Modern | `DATABASE.md` | Postgres still king, ORMs (Prisma/EF Core analog), Redis, migrations |
| 4.3 | Auth & Security | `AUTH.md` | OAuth2, OIDC, JWT, sessions — the full flow |

```
API Layer Evolution

  SOAP / WCF (2000s)     REST (2010s)          GraphQL / tRPC (2020s)
  ==================     ===========           ======================
  WSDL contracts     ->  OpenAPI/Swagger    ->  Schema-first type-safe
  Heavy XML          ->  JSON                   JSON over HTTP
  Code-gen clients   ->  Manual or generated    Auto-generated clients
  WS-Security        ->  JWT / OAuth2            Same auth, better DX
```

---

### Track 5 — Infrastructure

> How code moves from your laptop to a server that isn't yours.

| # | Module | File | What You'll Understand After |
|---|--------|------|------------------------------|
| 5.1 | Containers | `DOCKER.md` | Docker, Dockerfile, docker-compose, why containers won |
| 5.2 | Orchestration | `KUBERNETES.md` | Kubernetes — what problem it solves, how it works |
| 5.3 | CI/CD Modern | `CICD.md` | GitHub Actions vs Azure Pipelines, workflows, runners |
| 5.4 | Infrastructure as Code | `IAC.md` | Terraform, Bicep (Azure native), Pulumi — infra as version-controlled code |

```
Deployment Evolution

  2000s                  2010s                  2020s
  =====                  =====                  =====
  FTP to server          Virtual machines        Containers
  Manual install         Provisioned scripts     Kubernetes
  "Works on my box"      Chef/Puppet/Ansible     Terraform/Bicep
  Manual rollback        Deployment slots        GitOps + ArgoCD
  Alert via pager        Nagios/SCOM             Prometheus + Grafana
```

---

### Track 6 — Operations

> Running the thing at scale. This is where your Azure Data Factory and ADF pipeline experience
> translates into modern observability and orchestration patterns.

| # | Module | File | What You'll Understand After |
|---|--------|------|------------------------------|
| 6.1 | Observability | `OBSERVABILITY.md` | Logs + metrics + traces, OpenTelemetry, Grafana stack |
| 6.2 | Monorepos | `MONOREPO.md` | Turborepo, Nx — managing many packages in one repo |
| 6.3 | Cloud-Native Patterns | `CLOUD-NATIVE.md` | Microservices, event-driven arch, service mesh, Kafka |

```
Observability — The Three Pillars

  LOGS                METRICS              TRACES
  ====                =======              ======
  What happened       How much / how fast  Where did it go

  Structured JSON     Prometheus           OpenTelemetry
  ELK / Loki          Grafana              Jaeger / Tempo
  "Error in order     "p99 latency         "Request A called
   service at 14:32"   = 340ms"             B called C — 180ms in DB"
```

---

## Reading Order (Recommended)

```
If you're setting up a project:
  PACKAGE.md -> GIT.md -> JS-TS.md -> BUILD.md

If you're building a web app:
  JS-TS.md -> BUILD.md -> FRONTEND.md -> BACKEND.md -> DATABASE.md

If you're shipping it:
  DOCKER.md -> CICD.md -> KUBERNETES.md -> OBSERVABILITY.md

If you're on Azure specifically:
  IAC.md (Bicep section) -> CICD.md (Azure Pipelines) -> CLOUD-NATIVE.md
```

---

## Format Reference

Every module follows this structure:

```
# Title

## The Big Picture
[One diagram showing the whole landscape]

## Layer 1 / Section 1
[Drill down with diagrams]

## Layer 2 / Section 2
...

## How They Nest Together
[Real-world composition example]

## Concept Glossary

## Common Confusion Points

## Decision Cheat Sheet
[Table: I want to do X → use Y]
```

---

## Status

Last updated: **2026-02-22**
Modules complete: **1 / 17**
Currently building: **GIT.md** (next session)
