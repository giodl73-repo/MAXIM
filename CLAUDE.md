# C:\src\reference — Reference Library

## Project Purpose

A **self-authored reference library** organized by field. Each field is a subdirectory containing numbered guides. Every guide follows the same format: layered ASCII diagrams, mental models, practical comparisons, and decision cheat sheets. Never dumbed down.

---

## Library Structure

```
reference/
│
│  SESSION 1 — Modern Software Engineering
├── computing/          Modern software engineering (23 modules)
├── data-science/       Python stack, classical ML, MLOps (planned)
├── ai-engineering/     LLMs, agents, evals harness, safety (5 modules)
│
│  SESSION 2 — Physics & Mathematics
├── mathematics/        Vector calc, topology, probability — toolbox for physics
├── physics/            E&M, Maxwell, MHD, liquid metals, quantum, zero-point energy
│
│  SESSION 3 — Languages
├── languages/          16 languages × taxonomy + per-language reference cards (19 files)
│
│  SESSION 4 — Query Languages
├── query-languages/    SQL, PostgreSQL, T-SQL, MySQL, SQLite, KQL, analytical, DuckDB
│
│  SESSION 7 — Natural Sciences
├── natural-sciences/   Chemistry, biochemistry, earth sciences, biology, plasma science
│
│  SESSION 8 — Astronomy & Planetary Sciences
└── astronomy/          Precession, Earth motions, Milankovitch, orbital mechanics
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
| `data-science/06-AZURE-ML.md` | Azure Machine Learning — workspaces, compute, pipelines, managed endpoints, AzureML SDK v2 | 🔜 Next |

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
| `astronomy/04-STELLAR-PHYSICS.md` | Stellar structure, HR diagram, nucleosynthesis, stellar evolution, compact objects | 🔜 Queued |
| `astronomy/05-COSMOLOGY.md` | Big Bang, expansion, CMB, dark matter/energy, large-scale structure | 🔜 Queued |

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
| 2026-02-22 | 03-SKLEARN.md authored. Estimator API uniformity (fit/predict/transform/score), Pipeline + ColumnTransformer (data leakage prevention), preprocessing taxonomy (scalers/encoders/imputers), StratifiedKFold, cross_validate multi-metrics, GridSearchCV + RandomizedSearchCV double-underscore param naming, metrics (ROC-AUC vs accuracy on imbalanced), algorithm reference (Ridge/Lasso, HistGBM/XGBoost/LightGBM), unsupervised (KMeans/DBSCAN/PCA/t-SNE), feature selection, class_weight + SMOTE, joblib persistence, 8-step ML workflow. |
| 2026-02-22 | 04-PYTORCH.md authored. Tensor memory model (float32 default, from_numpy zero-copy, .to(device)), autograd dynamic graph (backward, gradient accumulation, no_grad, detach), nn.Module (forward vs __call__, train/eval semantics), full layer reference, CrossEntropyLoss expects logits, AdamW vs Adam correct L2, CosineAnnealingLR/OneCycleLR, Dataset/DataLoader (pin_memory, num_workers), complete 4-step training loop, mixed precision (float16+GradScaler, bfloat16 for A100+), clip_grad_norm_, checkpoint pattern, transfer learning (freeze/unfreeze + per-layer LR), residual block + self-attention modules, torch.compile(), PyTorch Lightning. |
| 2026-02-22 | 05-MLOPS.md authored. data-science/ track nearly complete. MLflow (mlflow.start_run, autolog, Model Registry stage transitions), W&B (wandb.init/log, Sweeps with Bayesian optimization), MLflow vs W&B comparison table, DVC data versioning + dvc.yaml pipeline DAG, Great Expectations data validation, FastAPI serving endpoint, BentoML service, ONNX export + ORT inference, Evidently drift reports + PSI/KS thresholds, retraining pipeline sketch, CI/CD ML GitHub Actions YAML, feature store offline/online architecture. |

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

## Instructions for Claude

- When asked to create a new guide, follow `computing/01-PACKAGE.md` style exactly
- New guides go in the appropriate field directory (`computing/`, `data-science/`, etc.)
- Check this file first to know what's done and what's queued
- Update the Artifact Index status when a file is completed
- Add an entry to the Session Log at the end of each working session
- The learner is a peer, not a student — write accordingly
- Bridge to Azure/VSTS/.NET concepts where natural — don't force it
- **32,000 token limit**: keep each guide file under ~32,000 tokens so it fits in a single context window load. Split into Part 1 / Part 2 if a topic runs long.
