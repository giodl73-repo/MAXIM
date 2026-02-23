# C:\src\reference — Reference Library

## Project Purpose

A **self-authored reference library** organized by field. Each field is a subdirectory containing numbered guides. Every guide follows the same format: layered ASCII diagrams, mental models, practical comparisons, and decision cheat sheets. Never dumbed down.

---

## Library Structure

```
reference/
│
│  SESSION 1 — Modern Software Engineering
├── computing/          25 modules — COMPLETE
├── data-science/       NumPy, Pandas, sklearn, PyTorch, MLOps, Azure ML — 6/6 COMPLETE
├── ai-engineering/     LLMs, evals, orchestration, agents, safety — 5 modules COMPLETE
│
│  SESSION 2 — Physics, Mathematics & Electronics
├── mathematics/        Vector calc, topology, probability, diff geometry — 11 modules COMPLETE
├── physics/            E&M, Maxwell, MHD, liquid metals, quantum, ZPE — 10 modules COMPLETE
├── electronics/        (planned)
│
│  SESSION 3 — Programming Languages
├── languages/          16 languages × taxonomy + reference cards — 19 files COMPLETE
│
│  SESSION 4 — Query Languages
├── query-languages/    SQL, PostgreSQL, T-SQL, MySQL, SQLite, KQL, BigQuery, Snowflake,
│                       Spark, DuckDB, MongoDB, Redis, GraphQL — 13 files COMPLETE
│
│  SESSION 5 — Scripting Languages
├── scripting/          Batch, PowerShell, Bash, Zsh, Fish, awk, sed, Perl — 10 files COMPLETE
│
│  SESSION 6 — Operating Systems
├── os/                 Windows, Linux, macOS, iOS, Android, cross-platform — 8 files COMPLETE
│
│  SESSION 7 — Natural Sciences
├── natural-sciences/   Chemistry, biochemistry, earth sciences, biology — in progress
│
│  SESSION 8 — Astronomy & Planetary Sciences
├── astronomy/          Earth motions, Milankovitch, celestial mechanics, stellar — 4 files
│
│  SESSION 9 — Aeronautics
├── aeronautics/        Aerodynamics, propulsion, flight mechanics, avionics — PLANNED
│
│  SESSION 10 — Mechanical Engineering
├── mechanical/         Thermodynamics, fluid mechanics, heat transfer, machine design — PLANNED
│
│  SESSION 11 — Structural Engineering & Architecture
├── structural/         Statics, structural analysis, bridges, materials, architecture — PLANNED
│
│  SESSION 12 — Chemical Engineering
├── chemical-eng/       Thermodynamics, reaction kinetics, transport phenomena, process design — PLANNED
│
│  SESSION 13 — Nuclear Engineering
├── nuclear/            Reactor physics, neutronics, thermal hydraulics, safety systems — PLANNED
│
│  SESSION 14 — Philosophy
└── philosophy/         Logic, epistemology, metaphysics, philosophy of mind, ethics — PLANNED
```

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

## computing/ — Artifact Index

| File | Topic | Status |
|------|-------|--------|
| `computing/01-PACKAGE.md` | Package managers — all layers | ✅ Complete |
| `computing/02-GIT.md` | Git modern workflow — branching, PRs, remotes | ✅ Complete |
| `computing/03-JS-TS.md` | JavaScript & TypeScript — modules, type system, transpilation | ✅ Complete |
| `computing/04-BUILD.md` | Build tools & bundlers — Vite, Webpack, esbuild, Rollup | ✅ Complete |
| `computing/05-FRONTEND.md` | Frontend frameworks — React, Vue, Angular, component model | ✅ Complete |
| `computing/06-RENDERING.md` | Rendering patterns — SPA, SSR, SSG, ISR, RSC | ✅ Complete |
| `computing/07-STATE.md` | State management — Redux, Zustand, Jotai, context | ✅ Complete |
| `computing/08-BACKEND.md` | Backend APIs — REST, GraphQL, tRPC, OpenAPI | ✅ Complete |
| `computing/09-DATABASE.md` | Databases modern — Postgres, ORMs, migrations, Redis | ✅ Complete |
| `computing/10-AUTH.md` | Auth & security — OAuth2, OIDC, JWT, sessions | ✅ Complete |
| `computing/11-DOCKER.md` | Containers — Docker, Dockerfile, docker-compose | ✅ Complete |
| `computing/12-KUBERNETES.md` | Orchestration — Kubernetes concepts, deployments | ✅ Complete |
| `computing/13-CICD.md` | CI/CD modern — GitHub Actions vs Azure Pipelines | ✅ Complete |
| `computing/14-IAC.md` | Infrastructure as Code — Terraform, Bicep, Pulumi | ✅ Complete |
| `computing/15-OBSERVABILITY.md` | Observability — logs, metrics, tracing, OpenTelemetry | ✅ Complete |
| `computing/16-MONOREPO.md` | Monorepos — Turborepo, Nx, workspaces | ✅ Complete |
| `computing/17-CLOUD-NATIVE.md` | Cloud-native patterns — microservices, events, service mesh | ✅ Complete |
| `computing/18-TESTING.md` | Modern testing stack — Vitest, Playwright, Testing Library, MSW | ✅ Complete |
| `computing/19-TESTING-EVOLUTION.md` | The arc: manual → TDD → chaos → eval harnesses | ✅ Complete |
| `computing/20-AZURE.md` | Azure services map — all the products, how they nest, when to use each | ✅ Complete |
| `computing/21-AUTOMATA.md` | Automata theory — DFA/NFA, pushdown, Turing machines, decidability | ✅ Complete |
| `computing/22-COMPILERS.md` | Compiler & interpreter design — lexing, parsing, IR, codegen, SSA | ✅ Complete |
| `computing/23-PL-THEORY.md` | Programming language theory — type theory, lambda calculus, semantics | ✅ Complete |
| `computing/24-NETWORKING.md` | Networking — IP/subnetting, TCP, DNS, HTTP/1.1/2/3, TLS 1.3, WebSockets, gRPC, CDN, LB | ✅ Complete |
| `computing/25-SECURITY.md` | Security & Cryptography — AES-GCM, EC/RSA, Argon2id, PKI, secrets mgmt, OWASP Top 10, zero-trust, supply chain, STRIDE, container security | ✅ Complete |

---

## computing/ — Curriculum Tracks

```
Track 1: Foundations          Track 2: JS Runtime Layer      Track 3: Frontend
  01-PACKAGE.md ✅               03-JS-TS.md ✅                 05-FRONTEND.md ✅
  02-GIT.md ✅                   04-BUILD.md ✅                 06-RENDERING.md ✅
                                                               07-STATE.md ✅

Track 4: Backend & Data       Track 5: Infrastructure        Track 6: Operations
  08-BACKEND.md ✅               11-DOCKER.md ✅                 15-OBSERVABILITY.md ✅
  09-DATABASE.md ✅              12-KUBERNETES.md ✅             16-MONOREPO.md ✅
  10-AUTH.md ✅                  13-CICD.md ✅                   17-CLOUD-NATIVE.md ✅
                                 14-IAC.md ✅

Track 7: Testing
  18-TESTING.md ✅               19-TESTING-EVOLUTION.md ✅

Track 8: Azure
  20-AZURE.md ✅

Track 9: CS Theory (MIT TCS background — bridge to modern tooling)
  21-AUTOMATA.md ✅              22-COMPILERS.md ✅             23-PL-THEORY.md ✅

Track 10: Networking
  24-NETWORKING.md ✅

Track 11: Security
  25-SECURITY.md ✅
```

---

## data-science/ — Artifact Index

| File | Topic | Status |
|------|-------|--------|
| `data-science/01-NUMPY.md` | NumPy — arrays, broadcasting, vectorized ops, linear algebra substrate | ✅ Complete |
| `data-science/02-PANDAS.md` | Pandas — DataFrame, indexing, groupby, merge, time series, performance | ✅ Complete |
| `data-science/03-SKLEARN.md` | scikit-learn — estimator API, preprocessing, pipelines, model selection, classical ML | ✅ Complete |
| `data-science/04-PYTORCH.md` | PyTorch — tensors, autograd, nn.Module, training loop, GPU, from scratch to transfer | ✅ Complete |
| `data-science/05-MLOPS.md` | MLOps — experiment tracking (MLflow/W&B), model registry, deployment, drift detection | ✅ Complete |
| `data-science/06-AZURE-ML.md` | Azure Machine Learning — workspaces, compute, pipelines, managed endpoints, AzureML SDK v2 | ✅ Complete |

---

## ai-engineering/ — Artifact Index

| File | Topic | Status |
|------|-------|--------|
| `ai-engineering/01-LLM-CONCEPTS.md` | LLMs — tokens, context, RAG, fine-tuning | ✅ Complete |
| `ai-engineering/02-EVALS-HARNESS.md` | Eval harness engineering — PromptFoo, Braintrust, RAGAS, LLM-as-judge, CI | ✅ Complete |
| `ai-engineering/03-ORCHESTRATION.md` | LangChain, LlamaIndex, Semantic Kernel | ✅ Complete |
| `ai-engineering/04-AGENTS.md` | Agent patterns, tool use, memory, multi-agent | ✅ Complete |
| `ai-engineering/05-SAFETY.md` | Red-teaming, hallucination detection, bias | ✅ Complete |

---

## languages/ — Artifact Index

| File | Language | Status |
|------|----------|--------|
| `languages/00-OVERVIEW.md` | Taxonomy — genealogy, paradigm map, type-system axes, early/late binding | ✅ Complete |
| `languages/01-CHEATSHEET.md` | Universal comparison: 16 languages × 10 topics + per-language quick cards | ✅ Complete |
| `languages/02-C.md` | C | ✅ Complete |
| `languages/03-CPP.md` | C++ | ✅ Complete |
| `languages/04-JAVA.md` | Java | ✅ Complete |
| `languages/05-CSHARP.md` | C# (home base) | ✅ Complete |
| `languages/06-PYTHON.md` | Python | ✅ Complete |
| `languages/07-JAVASCRIPT.md` | JavaScript | ✅ Complete |
| `languages/08-TYPESCRIPT.md` | TypeScript | ✅ Complete |
| `languages/09-RUST.md` | Rust | ✅ Complete |
| `languages/10-GO.md` | Go | ✅ Complete |
| `languages/11-HASKELL.md` | Haskell | ✅ Complete |
| `languages/12-FSHARP.md` | F# | ✅ Complete |
| `languages/13-KOTLIN.md` | Kotlin | ✅ Complete |
| `languages/14-SWIFT.md` | Swift | ✅ Complete |
| `languages/15-SCALA.md` | Scala | ✅ Complete |
| `languages/16-RUBY.md` | Ruby | ✅ Complete |
| `languages/17-SQL.md` | SQL (PostgreSQL + T-SQL) | ✅ Complete |

---

## astronomy/ — Artifact Index

| File | Topic | Status |
|------|-------|--------|
| `astronomy/01-EARTH-MOTIONS.md` | Precession, nutation, Chandler wobble, obliquity — all Earth rotational/orbital motions | ✅ Complete |
| `astronomy/02-MILANKOVITCH.md` | Orbital mechanics + Milankovitch cycles — eccentricity, obliquity, precession → ice ages | ✅ Complete |
| `astronomy/03-CELESTIAL-MECHANICS.md` | Two-body problem, orbital elements, perturbation theory, Lagrange points, resonances, tidal mechanics, chaos | ✅ Complete |
| `astronomy/04-STELLAR-PHYSICS.md` | Stellar structure, HR diagram, nucleosynthesis, stellar evolution, compact objects | ✅ Complete |
| `astronomy/05-COSMOLOGY.md` | Big Bang, expansion, CMB, dark matter/energy, large-scale structure | ✅ Complete |

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
| 2026-02-22 | 09-DATABASE.md authored. Covers Postgres, Prisma, Drizzle, migrations, connection pooling, Redis use cases, managed services, ADO.NET/EF bridge. |
| 2026-02-22 | Restructured into field directories: computing/, data-science/, ai-engineering/. Added 18-TESTING, 19-TESTING-EVOLUTION stubs. |
| 2026-02-22 | 10-AUTH.md authored. Covers sessions vs JWT, OAuth2, OIDC, PKCE, refresh tokens, token storage, providers, attacks, Entra/ADFS bridge. |
| 2026-02-22 | 11-DOCKER.md authored. Covers containers vs VMs, images/layers/caching, Dockerfile (basic + multi-stage), docker compose (app+postgres+redis), volumes, env secrets, registries, networking, IIS/Azure bridge. |
| 2026-02-22 | 12-KUBERNETES.md authored. Covers cluster architecture, Pod/Deployment/Service/Ingress/ConfigMap/Secret, HPA, rolling updates, rollbacks, Helm, AKS, App Service/VSTS bridge. |
| 2026-02-22 | 13-CICD.md authored. Covers GitHub Actions anatomy, matrix builds, Docker build+push, AKS deploy, Azure Pipelines (YAML + classic bridge), runners/agents, environments/approvals, caching, artifacts, VSTS bridge. |
| 2026-02-22 | 14-IAC.md authored. Covers declarative vs imperative, Terraform (HCL, state, modules, Azure example), Bicep (syntax, modules, what-if, deploy), Pulumi (TypeScript), GitOps pattern, ARM/Portal bridge. |
| 2026-02-22 | 15-OBSERVABILITY.md authored. Covers logs/metrics/traces pillars, structured logging (Pino), Prometheus (metrics types, PromQL, alerting), distributed traces (OTel spans, context propagation), OpenTelemetry SDK+Collector, Grafana stack, Azure Monitor+App Insights, SLI/SLO/SLA, SCOM bridge. |
| 2026-02-22 | 16-MONOREPO.md authored. Covers polyrepo vs monorepo tradeoffs, npm/pnpm workspaces, Turborepo (pipeline, caching, remote cache, filters), Nx (graph, affected, generators), shared package structure, TS path aliases, CI integration, Source Depot/.sln bridge. |
| 2026-02-22 | 17-CLOUD-NATIVE.md authored. Covers monolith→microservices spectrum, distributed systems tax, event-driven (queues/topics/Kafka), resilience patterns (circuit breaker, retry, bulkhead, saga), service mesh, API gateway, blue/green, canary, feature flags, 12-Factor, WCF/ESB/MSMQ bridge. |
| 2026-02-22 | 18-TESTING.md authored. Covers testing trophy, Vitest (unit, integration, mocking), Testing Library (behavior-first queries), MSW (network-level mocking), Playwright (E2E, page objects, codegen), coverage, CI integration, MSTest/Selenium bridge. |
| 2026-02-22 | 19-TESTING-EVOLUTION.md authored. Covers 5 eras: manual QA → TDD (mock trap) → pyramid/E2E (flakiness) → property-based/chaos/contract → AI eval harnesses (PromptFoo, Braintrust, RAGAS, LLM-as-judge). |
| 2026-02-22 | Session 6 initialized. os/ series: 8 files. 00-OVERVIEW (OS genealogy Unix/NT/Darwin, kernel architectures, 5 core abstractions cross-OS vocabulary, privilege rings, boot sequences). 01-CHEATSHEET (universal matrix 5 OSes × 20 topics, per-OS vocabulary load-in cards, dev box setup). 02-WINDOWS (NT stack, WPF→WinUI3 genealogy, Worker Services, PowerShell, WSL2, UAC/tokens, registry hives, ETW, SDK-style csproj). 03-LINUX (distro families + Azure Linux, FHS, systemd, cgroups/namespaces, eBPF, bash, SELinux/AppArmor). 04-MACOS (XNU Mach+BSD+IOKit, launchd, signing+notarization+Gatekeeper, APFS+SIP, Apple Silicon). 05-IOS (Xcode, provisioning+entitlements, App Sandbox, SwiftUI, async/await/actors, BGTaskScheduler, APNs, TestFlight). 06-ANDROID (ART+Zygote, four components, Gradle+AGP, Jetpack Compose, MVVM+Room/Hilt/WorkManager, Kotlin coroutines, ADB, Play Store). 07-CROSS-PLATFORM (.NET MAUI, React Native JSI, Flutter custom renderer, Electron contextBridge, Tauri Rust commands, Capacitor, decision matrix). Session6.md created. |
| 2026-02-22 | 20-AZURE.md authored. Full Azure services map: compute (VM/App Service/AKS/ACA/Functions), storage, databases (SQL/Cosmos/Postgres/Redis), messaging (Service Bus/Event Hubs/Event Grid), networking (VNet/Front Door/App Gateway), security (Key Vault/Managed Identity/Entra), AI (AOAI/AI Search). |
| 2026-02-22 | Added Track 9: CS Theory (21-AUTOMATA, 22-COMPILERS, 23-PL-THEORY). Learner profile updated: MIT double major Math + TCS. |
| 2026-02-22 | 21-AUTOMATA.md authored. Chomsky hierarchy as engineering constraint, ReDoS/NFA vs DFA engines, V8 Irregexp pipeline, lexer architecture, LL/LR/Earley/PEG parsers, XState statecharts, decidability limits of static analysis, Turing-completeness hazards. |
| 2026-02-22 | 22-COMPILERS.md authored. IR design (TAC, SSA, phi nodes, dom tree), LLVM IR, optimization passes (DCE/CSE/inlining/LTO), V8 Ignition→Maglev→Turbofan JIT tiers, sea of nodes, rustc MIR + borrow checker (NLL/Polonius), tsc incremental compilation, esbuild design, WASM, compiler correctness (CompCert, Alive2). |
| 2026-02-22 | 23-PL-THEORY.md authored. Type theory hierarchy (STLC→HM→System F→CoC), Curry-Howard in TS (never, exhaustiveness), HM vs TS inference, structural/nominal subtyping, variance, affine types → Rust ownership, region types → lifetimes (NLL/Polonius), TS conditional/mapped/template literal types + TC proof, ADTs, type classes/traits, operational/denotational/axiomatic semantics, RustBelt, research→production timeline. |
| 2026-02-22 | ai-engineering/ track started. 01-LLM-CONCEPTS.md authored. Next-token prediction, BPE tokenization, context window mechanics, Transformer architecture (attention, MHA, FFN, RoPE), pre-training + alignment (RLHF/DPO/Constitutional AI), sampling + KV cache + speculative decoding, context engineering (zero-shot/few-shot/CoT/ReAct), RAG, fine-tuning vs prompting, LoRA/QLoRA, model families map. |
| 2026-02-22 | 02-EVALS-HARNESS.md authored. Eval anatomy (dataset × prompt × scoring × threshold), scoring taxonomy (deterministic to probabilistic), LLM-as-judge design, PromptFoo (YAML config, multi-provider compare, red-team, CI mode), Braintrust (SDK, experiment comparison, UI), RAGAS (context recall/precision, faithfulness, answer relevancy), LangSmith (prod tracing → dataset flywheel), roll-your-own loop, eval-as-CI-gate with GitHub Actions, dataset engineering, cost-aware eval, common confusion points. |
| 2026-02-22 | 03-ORCHESTRATION.md authored. LangChain (LCEL pipe composition, RAG chain, memory, tools+agents, known pain points), LlamaIndex (ingestion pipeline, HyDE/QuestionsAnsweredExtractor, SubQuestionQueryEngine), Semantic Kernel (Kernel+Plugin model, auto function calling, Planner, C# .NET first-class, Azure-native pattern), framework comparison table, no-framework option (direct SDK tool-use loop), chunking strategies, embedding model selection, common confusion points (LangGraph, vector store ≠ retrieval strategy). |
| 2026-02-22 | 04-AGENTS.md authored. ReAct loop anatomy + minimal implementation, tool design principles (one responsibility, errors as returns, timeouts), tool description as prompt engineering, memory taxonomy (in-context/episodic/semantic/procedural), summary buffer + selective retrieval patterns, five agent patterns (single, prompt chaining, parallelization, evaluator-optimizer, orchestrator/subagent), LangGraph (StateGraph, conditional edges, checkpointer, human-in-the-loop interrupt), multi-agent topologies, production hardening (loop detection, context size guard, prompt injection defense, cost metrics), agent evals (trajectory eval), decision cheat sheet. |
| 2026-02-22 | 05-SAFETY.md authored. ai-engineering/ track complete. Hallucination taxonomy (intrinsic/extrinsic, closed/open domain), SelfCheckGPT consistency sampling, citation forcing + CoT mitigation. Prompt injection taxonomy (direct/indirect/tool hijacking), structural delimiter defense, tool result wrapping. Jailbreak patterns. Red-teaming (PromptFoo redteam, Garak, PyRIT multi-turn orchestrator). Output guardrails (Guardrails AI, NeMo Guardrails/Colang, Llama Guard classifier). PII (Microsoft Presidio detect + redact + synthetic replace). Bias taxonomy + counterfactual eval. System prompt hardening anatomy. EU AI Act tiers + NIST AI RMF. CI safety gates. Over-refusal as second failure mode. |
| 2026-02-22 | 02-PANDAS.md authored. DataFrame memory model (Series + shared Index), Pandas 2 Arrow backend, .loc/.iloc/.at disambiguation, SettingWithCopyWarning + chained indexing, dtypes (nullable Int64/boolean/StringDtype, category), missing data (dropna/fillna/ffill/interpolate), filtering (.query, .str accessor), method chaining pattern, groupby split-apply-combine (agg/transform/filter/apply), merge/join all types, reshape (pivot/melt/stack/explode), time series (resample/rolling/shift/pct_change/tz), performance hierarchy (vectorized → eval → apply → iterrows), Polars comparison, decision cheat sheet. |
| 2026-02-22 | data-science/ track started. Defined 6-module arc (NumPy → Pandas → sklearn → PyTorch → MLOps → Azure ML). 01-NUMPY.md authored: ndarray memory model (strides, views vs copies, contiguity + BLAS), dtypes, array creation, indexing (basic/fancy/boolean/np.ix_), broadcasting rules + keepdims, ufuncs, axis operations, np.linalg (solve/eig/SVD/QR/Cholesky, batch), np.fft (1-D/2-D, rfft, fftshift), performance patterns (vectorize, in-place, float32), decision cheat sheet. |
| 2026-02-22 | Session 3 initialized. languages/ series: 19 files. 00-OVERVIEW.md (language genealogy ASCII tree, paradigm spectrum, 6 type-system axes, early/late binding depth, nominal/structural/duck, expression problem). 01-CHEATSHEET.md (universal comparison tables: 16 languages × 10 topics + per-language quick cards). 02-C through 17-SQL: individual reference cards for C, C++, Java, C#, Python, JavaScript, TypeScript, Rust, Go, Haskell, F#, Kotlin, Swift, Scala, Ruby, SQL. Each covers: type system snapshot, syntax reference card (equality, logical ops, delimiter semantics, collection literals, if/match, strings/chars, null/Option, functions, error handling), what makes it distinct, ecosystem, gotchas from C#. |
| 2026-02-22 | Session 8 initialized. astronomy/ directory. 01-EARTH-MOTIONS.md authored: full hierarchy of Earth motions (rotation/Chandler/nutation/precession/obliquity), oblate spheroid root cause (J₂, Hd), precession rate formula (lunisolar torque, cos ε, tidal forcing ratio Moon/Sun=2.18), Euler angle framework (ψ/θ/φ), nutation (IAU 2000A, dominant 18.6 yr term ±17"/±9"), Chandler wobble (305 day Euler vs 433 day actual, non-rigidity, excitation problem), obliquity variation (22.1°–24.5° over 41 kyr, Jupiter forcing), pole star drift timeline (Thuban→Polaris→Vega→Polaris), zodiacal age precession (Hipparchus discovery), year type comparison (tropical/sidereal/anomalistic/draconic), GR corrections (geodetic/Lense-Thirring). |
| 2026-02-22 | 02-MILANKOVITCH.md authored. Eccentricity (~95/125/413 kyr beats, Jupiter/Saturn resonances), apsidal precession (~112 kyr prograde), climate precession index e·sin(λ̃) (~23+~19 kyr), insolation formula W(φ,t), 65°N summer target, Hays-Imbrie-Shackleton 1976 "Pacemaker" result, SPECMAP 1984/LR04 2005, MIS stages, 100-kyr problem (open), MPT (~900 kyr, no orbital change), Moon as obliquity stabilizer, La2004/La2010 validity limits (±50/±20 Myr), CO₂ as feedback not forcing. Session8.md created. |
| 2026-02-22 | 03-CELESTIAL-MECHANICS.md authored. Two-body reduction (reduced mass, conic sections, Kepler's laws as corollaries, vis-viva), six orbital elements + Kepler's equation (M=E−e sin E), three-body problem (Poincaré, restricted case, Jacobi integral), Lagrange L1–L5 (stability, Routh's criterion, halo orbits, mission examples: SOHO/JWST/Trojans), Lagrange planetary equations + J₂ perturbations (nodal regression, apsidal precession, sun-synchronous at 97–98°, Molniya at 63.43°), mean motion resonances (Kirkwood gaps, Laplace 4:2:1 Io/Europa/Ganymede, Plutinos 3:2, Trojans 1:1), secular resonances (ν₆ inner belt boundary), tidal forces (Roche limit 2.44R(ρ₁/ρ₂)^(1/3), tidal locking timescale, Mercury 3:2 spin-orbit, Io tidal heating), orbital maneuvers (Hohmann, gravity assist, Tsiolkovsky), solar system chaos (Lyapunov 5 Myr, Mercury 1% instability, Moon as obliquity stabilizer). |
| 2026-02-22 | 04-STELLAR-PHYSICS.md authored. Four stellar structure equations + Virial theorem (negative heat capacity of gravity) + three timescales, HR diagram (OBAFGKM, L∝M⁴, lifetime table), Gamow peak, pp chain I/II/III, CNO cycle, triple-α + Hoyle resonance (first anthropic physics prediction), advanced burning stages (C/Ne/O/Si timescales, iron wall, NSE), B²FH nucleosynthesis (s-process AGB, r-process NS mergers/GW170817), stellar evolution tracks (low/high mass), Chandrasekhar limit + Type Ia dark energy discovery, TOV equation + NS/pulsars/P-Ṗ diagram, BH (Schwarzschild/Kerr/Hawking T), SN taxonomy, Pop I/II/III. |
| 2026-02-22 | 05-COSMOLOGY.md authored. astronomy/ track COMPLETE. FLRW metric + Friedmann equations, ΛCDM parameters (Planck 2018), cosmic timeline (Planck epoch→inflation→BBN→recombination→today), inflation (horizon/flatness/monopole problems, slow-roll, n_s=0.9651, tensor modes), BBN (n/p=1/7 freeze-out, Y_p=25%, lithium problem), CMB (last scattering surface, T=2.7255K, acoustic peaks, power spectrum C_ℓ reading cosmological parameters), dark matter evidence (5 independent lines: rotation curves, Zwicky, lensing, Bullet Cluster, BBN), DM candidates (WIMPs undetected, axions, fuzzy DM), dark energy (1998 discovery, w=−1.03±0.03, cosmological constant problem 10¹²³, DESI 2024 hints w₀w_a), large-scale structure (cosmic web, Meszaros effect, matter power spectrum, BAO standard ruler), distance ladder (5 rungs), Hubble tension (67.4 vs 73.0, 5σ, unresolved), GW (GW150914, GW170817 multi-messenger, NANOGrav GWB), cosmological distances (comoving/D_A/D_L/event horizon), fate of universe (de Sitter heat death, Big Rip if phantom). |
| 2026-02-22 | 03-SKLEARN.md authored. Estimator API uniformity (fit/predict/transform/score), Pipeline + ColumnTransformer (data leakage prevention), preprocessing taxonomy (scalers/encoders/imputers), StratifiedKFold, cross_validate multi-metrics, GridSearchCV + RandomizedSearchCV double-underscore param naming, metrics (ROC-AUC vs accuracy on imbalanced), algorithm reference (Ridge/Lasso, HistGBM/XGBoost/LightGBM), unsupervised (KMeans/DBSCAN/PCA/t-SNE), feature selection, class_weight + SMOTE, joblib persistence, 8-step ML workflow. |
| 2026-02-22 | 04-PYTORCH.md authored. Tensor memory model (float32 default, from_numpy zero-copy, .to(device)), autograd dynamic graph (backward, gradient accumulation, no_grad, detach), nn.Module (forward vs __call__, train/eval semantics), full layer reference, CrossEntropyLoss expects logits, AdamW vs Adam correct L2, CosineAnnealingLR/OneCycleLR, Dataset/DataLoader (pin_memory, num_workers), complete 4-step training loop, mixed precision (float16+GradScaler, bfloat16 for A100+), clip_grad_norm_, checkpoint pattern, transfer learning (freeze/unfreeze + per-layer LR), residual block + self-attention modules, torch.compile(), PyTorch Lightning. |
| 2026-02-22 | 05-MLOPS.md authored. data-science/ track nearly complete. MLflow (mlflow.start_run, autolog, Model Registry stage transitions), W&B (wandb.init/log, Sweeps with Bayesian optimization), MLflow vs W&B comparison table, DVC data versioning + dvc.yaml pipeline DAG, Great Expectations data validation, FastAPI serving endpoint, BentoML service, ONNX export + ORT inference, Evidently drift reports + PSI/KS thresholds, retraining pipeline sketch, CI/CD ML GitHub Actions YAML, feature store offline/online architecture. |
| 2026-02-22 | 06-AZURE-ML.md authored. data-science/ track COMPLETE. Workspace architecture (storage/ACR/Key Vault/App Insights), hub-and-spoke pattern, RBAC roles. Compute types (Instance/Cluster/Serverless/Attached), SKU decision table, LowPriority preemptible. Data layer (Datastores, URI File/Folder/MLTable, versioned Data Assets). Environments (curated vs custom conda YAML + Dockerfile). Command Job (single-node + distributed TorchDistribution multi-GPU), Sweep Job (Bayesian + Bandit termination), AutoML (classification/regression/forecasting, featurization, ensembling). Pipelines (Component YAML + Python decorator, DAG assembly, caching/reuse). Model Registry (stage tracking via tags, MLflow flavors, version listing). Online Endpoints (ManagedOnline, scoring script, deploy + invoke, blue/green canary traffic split, MLflow no-script deploy). Batch Endpoints (mini-batch, append_row output). MLflow integration (auto-inject MLFLOW_TRACKING_URI, autolog, MlflowClient search_runs). Responsible AI Dashboard (SHAP, error analysis, causal, counterfactual). CLI v2 YAML + GitHub Actions CI/CD. Azure AI Studio vs AzureML Studio distinction. Prompt Flow (flow.dag.yaml, pf CLI, deploy). Security (Managed Identity, Private Endpoints, CMK). Cost management (min=0 clusters, auto-stop, LowPriority). AzureML vs SageMaker vs Vertex vs Databricks comparison. |
| 2026-02-22 | Session 5 initialized. scripting/ series: 10 files. 00-OVERVIEW (genealogy: Windows CMD→PowerShell, sh→Bash→Zsh→Fish, ed→sed→AWK→Perl; three-category taxonomy; execution model diagrams; POSIX compliance spectrum; decision tree). 01-CHEATSHEET (8 languages × 12 topics: file ext/shebang, variables, string quoting, arrays, arithmetic, if/else, case/switch, loops, functions, I/O+redirection, exit codes, arguments; per-language quick cards; feature gap matrix). 02-BATCH (delayed expansion trap + cmd.exe parsing order diagram, FOR /F/D/R/L patterns, EXIT /B vs EXIT, %~dp0 pattern, Batch→PS bridge table). 03-POWERSHELL (object pipeline vs text pipeline diagram, $? vs $LASTEXITCODE distinction, Write-Host vs Write-Output trap, try/catch, PS5.1 vs PS7, PS→Bash bridge). 04-BASH (fork/exec model, quoting word-splitting trap, arrays + mapfile, set -euo pipefail sharp edges, process substitution, POSIX sh portability table, PS→Bash bridge). 05-ZSH (1-indexed arrays, extended glob qualifiers, float in (( )), setopt options, startup file order, zmv). 06-FISH (set scopes -l/-g/-x/-U, string builtins, math float, argparse, universal vars, $status vs $?). 07-AWK (record/field model, built-in vars table, dual-type system, string functions, assoc arrays, 25+ one-liners inc NR==FNR file-join, SQL analogy diagram, gawk extensions). 08-SED (address types, all core commands, hold space h/H/g/G/x, N/P/D multiline, labels+branching, GNU vs BSD table, 20+ patterns). 09-PERL (sigil-shift rule, scalar/list context, regex as grammar operators, one-liner -n/-p/-i/-a/-F, closures, Perl vs Python decision). |

| 2026-02-22 | CLAUDE.md updated: artifact indexes for all directories (mathematics/ 13 modules, physics/ 10 modules, natural-sciences/ 4 files, os/ 8 files, scripting/ 10 files). Library Structure updated with Sessions 10–14 planned: Mechanical Engineering, Structural Engineering, Chemical Engineering, Nuclear Engineering, Philosophy. Session 9 (Aeronautics) initialized. |
| 2026-02-22 | 24-NETWORKING.md authored. TCP/IP stack diagram + real HTTPS call trace (all layers), IP/subnetting/CIDR/NAT/IPv6, TCP 3-way handshake + 4-way teardown + congestion control (CUBIC/BBR) + TIME_WAIT + Nagle, DNS resolution chain + all record types + split-horizon + DNSSEC + DoH/DoT, HTTP/1.1 HOL blocking → HTTP/2 binary framing + HPACK + multiplexing → HTTP/3 QUIC 0-RTT + connection migration, TLS 1.3 1-RTT handshake + ECDHE forward secrecy + SNI + ALPN + mTLS + OCSP stapling, WebSockets upgrade + framing + vs SSE, gRPC HTTP/2 wire format + 4 streaming modes + Protobuf varints + status codes, CDN Anycast + Cache-Control anatomy + ETag + origin shield, L4 vs L7 load balancers + consistent hashing ring + health checks + connection draining, reverse proxy patterns (nginx/Caddy/Envoy), network security (NSG/zero-trust/Private Link/DDoS/rate limiting), ports table, WCF→gRPC/REST bridge table. |
| 2026-02-22 | 25-SECURITY.md authored. Full security & cryptography reference. Cryptography fundamentals: AES modes (ECB/CBC/CTR/GCM — AEAD), ChaCha20-Poly1305, RSA (Bleichenbacher/OAEP), ECDSA (PS3 k-reuse story), Ed25519 deterministic nonce, X25519 ECDH, ECDLP group theory bridge. Hash functions (MD5/SHA-1 broken, SHA-256/BLAKE3/SHA-3), length extension attack, HMAC construction, Poly1305, timing-safe comparison. KDFs: Argon2id (PHC winner, m=64MB), bcrypt 72-byte truncation gotcha, HKDF for TLS 1.3 key schedule. CSPRNG. PKI: X.509 chain, CT logs, OCSP stapling, Let's Encrypt ACME. Secrets management: HashiCorp Vault (dynamic secrets, Transit engine), Azure Key Vault + Managed Identity, SOPS, Sealed Secrets, secret scanning tools. TLS 1.3 handshake + ECDHE forward secrecy + mTLS. OWASP Top 10 (2021) deep dive: IDOR, JWT alg:none + algorithm confusion, SQL/command/NoSQL/SSTI injection, SSRF + IMDS exploitation. Zero-trust: BeyondCorp model, Entra Conditional Access, PIM JIT. Supply chain: SBOM (CycloneDX/SPDX), SLSA 4 levels, Sigstore/Cosign keyless signing. Threat modeling: STRIDE table, DFD trust boundaries, attack trees, PASTA. Container security: non-root, seccomp, distroless, multi-stage builds, Trivy/Grype. Cloud IAM: Managed Identity vs service principal, PIM, Conditional Access, security headers. Security testing: SAST/DAST/SCA/fuzzing tool table + CI integration YAML. Old-world bridge: Kerberos→JWT, ADFS→Entra OIDC, WIA→Managed Identity, AD CS→Let's Encrypt, BinaryFormatter removal. |
| 2026-02-22 | mathematics/ modules 14–22 planned: complex analysis, optimization, information theory, combinatorics/graphs, number theory, numerical methods, statistics, measure theory, category theory. 14-COMPLEX-ANALYSIS.md authored. ℂ as algebraic closure of ℝ, polar form + Euler, Riemann sphere. Holomorphic = CR equations = Jacobian is conformal. C¹⟹analytic miracle (contrast with ℝ). Cauchy's theorem, Cauchy integral formula, all derivatives from one formula. Laurent series + singularity classification (removable/pole/essential). Residue theorem + three standard contour types for real integrals. Multivalued functions (log z, zᵃ), branch cuts, Riemann surfaces, monodromy. Conformal maps, Möbius transformations, Riemann mapping theorem, Schwarz-Christoffel. Harmonic functions + Dirichlet problem via Poisson kernel. Analytic continuation + identity theorem. Gamma function + Riemann hypothesis sketch. Applications: potential flow, electrostatics, Wick rotation in QM, Bromwich/inverse Laplace, Hardy spaces + H∞ control. |
| 2026-02-22 | Session 4 initialized. query-languages/ series: 13 files. 00-OVERVIEW (data model taxonomy, relational algebra → SQL bridge, SQL standards SQL-86→SQL:2023, ACID/BASE/SAGA, CAP, when SQL vs NoSQL decision tree). 01-SQL-CORE (30-year refresh: CTEs, recursive CTEs, window functions with OVER anatomy, ROWS/RANGE frames, MERGE, temporal tables, JSON SQL:2016, GENERATE_SERIES, indexes, EXPLAIN). 02-POSTGRESQL (JSONB operators, arrays, LATERAL=CROSS APPLY, RETURNING, materialized views, FTS, partitioning, RLS, pgvector, PostGIS, TimescaleDB). 03-TSQL (25-year refresh timeline, CROSS/OUTER APPLY, MERGE+OUTPUT, JSON+OPENJSON+FOR JSON, temporal tables, TRY/CATCH+THROW, sp_executesql safe dynamic SQL, Query Store, DMVs, Azure SQL tiers, Synapse distribution). 04-MYSQL (InnoDB architecture, ON DUPLICATE KEY UPDATE, window funcs 8.0+, CTEs 8.0+, JSON, utf8mb4 trap, EXPLAIN type hierarchy, replication/binlog). 05-SQLITE (serverless architecture, type affinity+STRICT mode, WAL mode, foreign_keys PRAGMA, JSON1, FTS5, WITHOUT ROWID, in-memory testing pattern, date as TEXT). 06-KQL (Azure Monitor/App Insights/Sentinel/ADX ecosystem, pipe syntax, time functions+bin(), has vs contains, dynamic type, let statements, join kinds, make-series anomaly detection, SQL→KQL translation table, common App Insights/Monitor/Sentinel hunting patterns). 07-ANALYTICAL (cloud DW evolution, BigQuery/Snowflake/Databricks/Synapse comparison, QUALIFY, PIVOT, time travel, MERGE INTO, materialized views, dbt integration, external tables, medallion architecture, OLAP functions). 08-SPARKSQL (Catalyst architecture, SQL API vs DataFrame API equivalence, Delta Lake MERGE/OPTIMIZE/ZORDER/VACUUM/time travel, broadcast joins, structured streaming with watermarks, explain modes, AQE). 09-DUCKDB (in-process OLAP, vectorized columnar, direct Parquet/CSV/JSON/S3/ADLS query, PIVOT auto-detection, LIST/STRUCT/MAP nested types, lambdas, Python zero-copy, httpfs/spatial/delta extensions). 10-MONGODB (MQL CRUD operators, aggregation pipeline stages, $lookup pipeline form, $facet/$bucket, expression operators, index types including TTL/partial/wildcard/2dsphere, Atlas Search Lucene + Atlas Vector Search for RAG). 11-REDIS (String/Hash/List/Set/ZSet/Stream commands, MULTI/EXEC/WATCH CAS, Pub/Sub vs Streams, Lua scripting, RediSearch FT.CREATE/FT.SEARCH/KNN vector, RedisJSON, distributed lock pattern). 12-GRAPHQL (SDL schema with scalar/enum/union/interface, query/mutation/subscription syntax, variables/fragments/directives, N+1+DataLoader, schema-first vs code-first, Apollo Federation, Hasura, persisted queries, REST vs GraphQL decision). Session4.md created. |

---

## query-languages/ — Artifact Index

| File | Topic | Status |
|------|-------|--------|
| `query-languages/00-OVERVIEW.md` | Landscape, relational algebra, SQL standards history, ACID/BASE | ✅ Complete |
| `query-languages/01-SQL-CORE.md` | ANSI SQL — the 30-year refresh (CTEs, window functions, JSON, temporal) | ✅ Complete |
| `query-languages/02-POSTGRESQL.md` | PostgreSQL: JSONB, arrays, LATERAL, full-text, pgvector, EXPLAIN ANALYZE | ✅ Complete |
| `query-languages/03-TSQL.md` | T-SQL: SQL Server + Azure SQL + Synapse (APPLY, MERGE, OUTPUT, JSON, temporal) | ✅ Complete |
| `query-languages/04-MYSQL.md` | MySQL / MariaDB: InnoDB, window functions (8.0+), utf8mb4, JSON | ✅ Complete |
| `query-languages/05-SQLITE.md` | SQLite: embedded, WAL, STRICT, JSON1, FTS5, in-memory testing | ✅ Complete |
| `query-languages/06-KQL.md` | KQL: Azure Monitor / Log Analytics / App Insights / ADX / Sentinel | ✅ Complete |
| `query-languages/07-ANALYTICAL.md` | Cloud DW SQL: BigQuery + Snowflake + Databricks + Synapse, dbt, medallion | ✅ Complete |
| `query-languages/08-SPARKSQL.md` | Spark SQL + Delta Lake: DataFrame API, MERGE INTO, streaming, ZORDER | ✅ Complete |
| `query-languages/09-DUCKDB.md` | DuckDB: OLAP in-process, direct Parquet/CSV query, PIVOT, lambdas | ✅ Complete |
| `query-languages/10-MONGODB.md` | MongoDB MQL + aggregation pipeline, indexes, Atlas Vector Search | ✅ Complete |
| `query-languages/11-REDIS.md` | Redis: data structures, Streams, Lua, RediSearch KNN, distributed lock | ✅ Complete |
| `query-languages/12-GRAPHQL.md` | GraphQL: SDL schema, query/mutation/subscription, N+1 + DataLoader, federation | ✅ Complete |

---

## os/ — Artifact Index

| File | Topic | Status |
|------|-------|--------|
| `os/00-OVERVIEW.md` | OS taxonomy — genealogy (Unix/NT/Darwin), kernel architectures, 5 core abstractions, privilege rings, security models, boot sequence, cross-OS vocabulary table | ✅ Complete |
| `os/01-CHEATSHEET.md` | Universal comparison: Windows/Linux/macOS/iOS/Android × 20 topics + per-OS vocabulary load-in cards + dev environment setup | ✅ Complete |
| `os/02-WINDOWS.md` | Windows dev — NT architecture, WinForms/WPF/WinUI3/MAUI genealogy, Worker Services, PowerShell, WSL2, UAC/tokens/Credential Guard, registry deep dive, ETW, networking, WinGet, SDK-style MSBuild | ✅ Complete |
| `os/03-LINUX.md` | Linux dev — kernel/VFS/proc/sys, distro families (Debian/RHEL/Arch/Azure Linux), FHS, systemd (units/journal/timers), containers as Linux primitives, eBPF, shell scripting, permissions, networking, storage, SELinux/AppArmor | ✅ Complete |
| `os/04-MACOS.md` | macOS dev — XNU/Mach/BSD/IOKit, SDK onion, app bundle, launchd/XPC, signing+notarization+Gatekeeper, APFS+SIP, Homebrew, SwiftUI vs AppKit, Apple Silicon + Rosetta 2 | ✅ Complete |
| `os/05-IOS.md` | iOS dev — Xcode build system, provisioning+certificates+entitlements, app sandbox+privacy, UIKit/SwiftUI, Swift concurrency (async/await/actors), networking, background execution, push notifications, TestFlight+App Store | ✅ Complete |
| `os/06-ANDROID.md` | Android dev — ART+Zygote, four app components, AndroidManifest, Gradle+AGP, Jetpack Compose, MVVM+Jetpack (ViewModel/Room/Hilt/WorkManager), Kotlin coroutines, Retrofit, Android Keystore, ADB, APK/AAB distribution | ✅ Complete |
| `os/07-CROSS-PLATFORM.md` | Cross-platform — abstraction spectrum, .NET MAUI, React Native (New Architecture/JSI), Flutter (custom renderer), Electron (main/renderer/IPC), Tauri (Rust+webview), Capacitor, code sharing strategies, full decision matrix | ✅ Complete |

---

## scripting/ — Artifact Index

| File | Topic | Status |
|------|-------|--------|
| `scripting/00-OVERVIEW.md` | Landscape — genealogy (Windows/POSIX/DSL), taxonomy, execution models, POSIX compliance spectrum, decision tree | ✅ Complete |
| `scripting/01-CHEATSHEET.md` | Universal comparison: 8 languages × 12 topics + per-language quick cards + feature gap matrix | ✅ Complete |
| `scripting/02-BATCH.md` | Windows CMD/Batch — delayed expansion, FOR /F, EXIT /B vs EXIT, special chars, Batch→PowerShell bridge | ✅ Complete |
| `scripting/03-POWERSHELL.md` | PowerShell 7 — object pipeline, $? vs $LASTEXITCODE, try/catch, PS5.1 vs PS7, PS→Bash bridge | ✅ Complete |
| `scripting/04-BASH.md` | Bash 5 — fork/exec model, quoting rules, arrays, set -euo pipefail, POSIX sh portability table, PS→Bash bridge | ✅ Complete |
| `scripting/05-ZSH.md` | Zsh — 1-indexed arrays, extended globbing, float arithmetic, setopt, startup file order | ✅ Complete |
| `scripting/06-FISH.md` | Fish — set/argparse/math builtins, universal vars, non-POSIX syntax, Fisher, interactive-only framing | ✅ Complete |
| `scripting/07-AWK.md` | AWK/gawk — record/field model, built-ins, string functions, associative arrays, 25+ practical one-liners, SQL analogy | ✅ Complete |
| `scripting/08-SED.md` | sed — address types, commands (s/d/p/a/i/c/y/N/P/D), hold space, labels/branching, GNU vs BSD table | ✅ Complete |
| `scripting/09-PERL.md` | Perl 5 — sigils, context, regex as grammar, one-liner mode (-n/-p/-i/-a), CPAN, Modern Perl 5.36 | ✅ Complete |

---

## mathematics/ — Artifact Index

| File | Topic | Status |
|------|-------|--------|
| `mathematics/01-VECTOR-CALC.md` | Gradient, divergence, curl, del operator ∇, Maxwell preview | ✅ Complete |
| `mathematics/02-INTEGRAL-THEOREMS.md` | Divergence theorem, Stokes, Gradient theorem — Maxwell in integral form | ✅ Complete |
| `mathematics/03-TRIG.md` | Unit circle, Euler's formula e^(iθ), phasors, hyperbolic trig | ✅ Complete |
| `mathematics/04-POWER-SERIES.md` | Taylor, Maclaurin, radius of convergence, generating functions, asymptotic | ✅ Complete |
| `mathematics/05-GROUPS-SETS-ALGEBRA.md` | Groups, rings, fields, Lie groups, U(1)/SU(2)/SU(3), Noether's theorem | ✅ Complete |
| `mathematics/06-LINEAR-ALGEBRA.md` | Vector spaces, matrices, eigenvalues, SVD, spectral theorem, QM dictionary | ✅ Complete |
| `mathematics/07-DIFFEQ.md` | ODEs (all types), PDEs (heat/wave/Laplace), Green's functions, physics bestiary | ✅ Complete |
| `mathematics/08-TOPOLOGY.md` | Open sets, compactness, π₁, fiber bundles, topological insulators, Dirac monopoles | ✅ Complete |
| `mathematics/09-MANIFOLDS.md` | Manifolds, differential forms, exterior derivative, generalized Stokes, Maxwell as dF=0 | ✅ Complete |
| `mathematics/10-DIFFERENTIAL-GEOMETRY.md` | Curvature, geodesics, Riemann tensor, Christoffel symbols, Einstein field equations decoded | ✅ Complete |
| `mathematics/11-PROBABILITY.md` | Distributions, Bayes, CLT, Markov chains, Boltzmann, Master Theorem | ✅ Complete |
| `mathematics/12-FOURIER.md` | Fourier series/transform, FFT, windowing, uncertainty principle, 2D FT | ✅ Complete |
| `mathematics/13-LAPLACE.md` | Laplace transform, transfer functions, Bode plots, z-transform comparison | ✅ Complete |
| `mathematics/14-COMPLEX-ANALYSIS.md` | Complex numbers, analytic functions, Cauchy-Riemann, contour integration, residues, conformal maps | ✅ Complete |
| `mathematics/15-OPTIMIZATION.md` | Lagrange multipliers, KKT, convex sets, duality, LP/QP, gradient descent as math | 🔜 Next |
| `mathematics/16-INFORMATION-THEORY.md` | Shannon entropy, mutual information, KL divergence, channel capacity, ML bridges | 🔜 Queued |
| `mathematics/17-COMBINATORICS-GRAPHS.md` | Counting, generating functions, graph theory, trees, planarity, Ramsey, extremal | 🔜 Queued |
| `mathematics/18-NUMBER-THEORY.md` | Primes, modular arithmetic, Euler's theorem, quadratic reciprocity, p-adics, crypto | 🔜 Queued |
| `mathematics/19-NUMERICAL-METHODS.md` | Newton's method, quadrature, finite differences, stability, condition numbers | 🔜 Queued |
| `mathematics/20-STATISTICS.md` | Estimation, MLE, hypothesis testing, Bayesian inference, regression theory | 🔜 Queued |
| `mathematics/21-MEASURE-THEORY.md` | Lebesgue integration, σ-algebras, L² spaces, rigorous probability foundation | 🔜 Queued |
| `mathematics/22-CATEGORY-THEORY.md` | Functors, natural transformations, monads, adjunctions, connections to PL theory | 🔜 Queued |

---

## physics/ — Artifact Index

| File | Topic | Status |
|------|-------|--------|
| `physics/01-ELECTROSTATICS.md` | Coulomb's law, Gauss's law, potential V, conductors, Poisson equation | ✅ Complete |
| `physics/02-MAGNETOSTATICS.md` | Biot-Savart, Ampere's law, vector potential A, no monopoles | ✅ Complete |
| `physics/03-MAXWELL.md` | All four equations, displacement current fix, c = 1/√μ₀ε₀, wave derivation | ✅ Complete |
| `physics/04-EM-WAVES.md` | Plane waves, polarization, Poynting vector, skin depth, EM spectrum | ✅ Complete |
| `physics/05-MOTORS-GENERATORS.md` | Faraday, back-EMF, transformers, three-phase, steam→grid chain | ✅ Complete |
| `physics/06-MHD.md` | Induction equation, Alfvén waves, Hartmann flow, tokamaks, dynamos | ✅ Complete |
| `physics/07-LIQUID-METALS.md` | Hg/Ga/Na properties, EM pumping, Sadoway battery, fringe claim evaluation | ✅ Complete |
| `physics/08-QUANTUM-BRIDGE.md` | Planck→Schrödinger, Hilbert space, Hermitian operators, SU(2) spin | ✅ Complete |
| `physics/09-ZERO-POINT-ENERGY.md` | Casimir effect, Lamb shift, Hawking radiation, cosmological constant problem | ✅ Complete |
| `physics/10-GRAVITY-EM.md` | GEM equations, Lense-Thirring, Meissner levitation, fringe final answers | ✅ Complete |

---

## natural-sciences/ — Artifact Index

| File | Topic | Status |
|------|-------|--------|
| `natural-sciences/00-OVERVIEW.md` | Landscape — field taxonomy, cross-discipline connections, session arc | ✅ Complete |
| `natural-sciences/01-ATOMIC-QUANTUM.md` | Atomic structure, quantum numbers, periodic table, electron configurations, spectroscopy | ✅ Complete |
| `natural-sciences/08-METABOLISM.md` | Metabolic pathways — glycolysis, Krebs cycle, oxidative phosphorylation, ATP accounting | ✅ Complete |
| `natural-sciences/14-ATMOSPHERE-CLIMATE.md` | Atmospheric layers, composition, circulation, greenhouse effect, climate feedback loops | ✅ Complete |

---

## Instructions for Claude

- When asked to create a new guide, follow `computing/01-PACKAGE.md` style exactly
- New guides go in the appropriate field directory (`computing/`, `data-science/`, etc.)
- Check this file first to know what's done and what's queued
- Update the Artifact Index status when a file is completed
- Add an entry to the Session Log at the end of each working session
- The learner is a peer, not a student — write accordingly
- Bridge to Azure/VSTS/.NET concepts where natural — don't force it
- **32,000 token limit**: keep each guide file under ~32,000 tokens so it fits in a single context window load. Split into Part 1 / Part 2 if a topic runs long.
- **AGENT PERMISSION BUG — CRITICAL**: Background agents (`run_in_background: true`) cannot get Write/Bash permissions approved — the approval dialog never shows, so writes are silently blocked and the agent fails. **Always spawn file-writing agents in the foreground** (omit `run_in_background`) OR use `mode: "bypassPermissions"`. For large multi-session content generation, write files directly in the main conversation rather than delegating to background agents.
