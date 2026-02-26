# 16 — Monorepos

## The Big Picture

```
Polyrepo vs Monorepo
=====================

  Polyrepo (one repo per project)    Monorepo (everything in one repo)
  ================================   ==================================

  github.com/org/api                 github.com/org/myapp
  github.com/org/web                   apps/
  github.com/org/shared-ui              api/
  github.com/org/design-system          web/
  github.com/org/utils                  admin/
                                       packages/
                                         shared-ui/
                                         design-system/
                                         utils/
                                         config/

  Cross-repo changes:                Cross-package changes:
    5 PRs, 5 CI runs                   1 PR, 1 CI run
    Versioning ceremony                No versioning required (internal)
    "Which version of utils?"          Always on latest
    Consumers lag on updates           Change + consumer updated together
```

```
The Core Problems a Monorepo Tool Solves
=========================================

  ┌─────────────────────────────────────────────────────────────────┐
  │  Problem 1: Only rebuild what changed                           │
  │                                                                 │
  │  You changed packages/utils.                                    │
  │  Don't rebuild apps/web, apps/admin if they don't use utils.   │
  │  Do rebuild apps/api because it imports utils.                  │
  │                                                                 │
  │  Problem 2: Run tasks in correct order                          │
  │                                                                 │
  │  apps/api depends on packages/utils.                           │
  │  Build utils before building api — not after, not in parallel. │
  │                                                                 │
  │  Problem 3: Cache results                                       │
  │                                                                 │
  │  utils hasn't changed since last build.                         │
  │  Don't rebuild it — replay the cached output.                   │
  │  Remote cache: share across machines and CI.                    │
  └─────────────────────────────────────────────────────────────────┘
```

```
Tool Landscape
===============

  Turborepo          Nx              pnpm workspaces    Lerna (legacy)
  =========          ==             ================    ==============

  Fast, simple       Full platform   Package manager     Predecessor to
  Zero config        Code gen        layer only          Nx — mostly
  task pipeline      Plugins         (use with Turbo)    superseded
  Remote cache       Generators
  (Vercel)           Project graph
                     IDE plugin

  Best for:          Best for:       Best for:
    JS/TS monorepos    Large teams     Simple multi-
    Next.js / Vite     Enterprise      package repos
    Lean setup         Full stack      without task
                       Nx Console      orchestration
```

---

## npm / pnpm / yarn Workspaces

<!-- @editor[bridge/P2]: No Source Depot / multi-repo → workspaces bridge here. This reader managed massive multi-repo enlsitments (Windows source, Office). Opening the workspaces section with the JavaScript mechanics before establishing "this is the equivalent of a Source Depot enlistment with project references" misses the entry point. The bridge table at the bottom covers it but the conceptual landing should happen here. -->

Every modern package manager understands monorepos natively. Workspaces are the foundation — monorepo tools build on top.

```json
// package.json (root)
{
  "name": "myapp",
  "private": true,
  "workspaces": [
    "apps/*",
    "packages/*"
  ]
}
```

```
What workspaces give you:
  1. Single node_modules at root (hoisted)
  2. Local packages linked automatically (no npm publish)
  3. Install all packages in one: npm install (at root)
  4. Run scripts across packages: npm run build --workspaces
```

```bash
# pnpm workspaces (pnpm-workspace.yaml)
packages:
  - 'apps/*'
  - 'packages/*'

# Run command in specific package
pnpm --filter api dev
pnpm --filter @myapp/utils build

# Run in all packages
pnpm -r build

# Run in packages affected by changes (with turbo)
pnpm turbo build --filter=...[HEAD^1]
```

---

## Turborepo

Turborepo adds task orchestration and caching on top of workspaces. Its job is to run the right tasks in the right order, fast.

### Setup

```bash
# Add to existing repo
npx turbo init

# Or create new
npx create-turbo@latest
```

```
repo/
├── apps/
│   ├── web/            package.json { "name": "@myapp/web" }
│   └── api/            package.json { "name": "@myapp/api" }
├── packages/
│   ├── ui/             package.json { "name": "@myapp/ui" }
│   └── config/         package.json { "name": "@myapp/config" }
├── turbo.json
└── package.json        (workspaces: ["apps/*", "packages/*"])
```

### turbo.json — The Pipeline

<!-- @editor[bridge/P2]: The `"dependsOn": ["^build"]` concept maps directly to MSBuild project references / .csproj dependency ordering — MSBuild also walks the project dependency graph before building dependents. Worth a one-line call-out: this is the turbo.json equivalent of `<ProjectReference>` dependency ordering in MSBuild. Currently no bridge at this critical concept. -->

```json
{
  "$schema": "https://turbo.build/schema.json",
  "pipeline": {
    "build": {
      "dependsOn": ["^build"],   // ^ means: run deps' build first
      "outputs": ["dist/**", ".next/**"]
    },
    "test": {
      "dependsOn": ["^build"],   // tests need deps built
      "outputs": []
    },
    "lint": {
      "outputs": []
    },
    "dev": {
      "cache": false,            // dev servers shouldn't cache
      "persistent": true         // long-running process
    },
    "typecheck": {
      "dependsOn": ["^build"]
    }
  }
}
```

```
"^build" means: before running this package's build,
run build in all packages it depends on first.

If api depends on ui:
  turbo build
    1. build @myapp/ui     (no deps)
    2. build @myapp/api    (waited for ui)
    3. build @myapp/web    (no deps — ran in parallel with api)
```

### Running Tasks

```bash
# Run build across all packages (in dependency order)
turbo build

# Run multiple tasks
turbo build test lint

# Run for specific package + its dependencies
turbo build --filter=@myapp/api

# Run for packages changed since last commit
turbo build --filter=...[HEAD^1]

# Run for packages that depend on a changed package
turbo build --filter=...@myapp/ui...

# Dry run — see what would run
turbo build --dry-run
```

### Caching

<!-- @editor[bridge/P1]: Remote cache is the most important new concept in this file — it has no MSBuild or Source Depot analog. MSBuild incremental build is local-only and per-machine; VSTS/ADO build caching existed but was limited. Turbo remote cache (content-addressable, shared across all machines and CI runs) is genuinely new. The current text just describes mechanics. Add an explicit note: "No direct .NET/MSBuild analog — this is new. MSBuild's `/incremental` flag is local-only and doesn't survive a clean CI agent. Turbo remote cache is a shared content-addressed store: if any machine (local or CI) built a given input hash, every other machine gets the output instantly." This is the key value prop and the reader needs it flagged as new territory. -->

```
How Turbo cache works
======================

  Hash inputs:
    - Source files in the package
    - package.json + lockfile
    - turbo.json pipeline config
    - Environment variables (if listed in env)

  If hash matches a previous run → replay cached output
  If hash differs → run the task, cache the result

  Cache hit:  >>> FULL TURBO  (replays in milliseconds)
  Cache miss: normal run, then cached for next time
```

```bash
# Local cache: .turbo/ directory
# Remote cache: Vercel Remote Cache (or self-hosted)

# Enable Vercel remote cache
turbo login
turbo link

# Now CI and local share the same cache
# PR CI hits cache from your local build — instant
```

### Environment Variables in Cache

```json
{
  "pipeline": {
    "build": {
      "dependsOn": ["^build"],
      "outputs": ["dist/**"],
      "env": ["NODE_ENV", "API_URL"]   // these affect cache hash
    }
  }
}
```

List env vars that affect build output. Different `NODE_ENV` values = different cache entries.

---

## Nx

Nx is a more opinionated, full-featured monorepo platform. Core concepts are the same as Turbo (task graph, caching, affected commands) but it adds generators, plugins, and an IDE extension.

### Project Graph

```bash
# Visualize the dependency graph in browser
nx graph
```

```
@myapp/web ──────────────► @myapp/ui
     │                          │
     └──────► @myapp/utils ◄────┘
                   │
              @myapp/api
```

Nx builds this graph by analyzing imports — no manual configuration needed.

### Affected Commands

```bash
# Only run tests for projects affected by changes on this branch
nx affected --target=test --base=main --head=HEAD

# Only build affected projects
nx affected --target=build

# See what's affected without running
nx affected --target=build --dry-run
```

This is the key CI optimization: on a PR that only touches `packages/utils`, Nx runs tests for `utils`, `api`, and `web` (because they depend on `utils`) — but skips `packages/config` (unaffected).

### Generators

```bash
# Generate a new library
nx generate @nx/react:library shared-ui --directory=packages

# Generate a new app
nx generate @nx/next:app dashboard --directory=apps

# Generate a component in an existing lib
nx generate @nx/react:component Button --project=shared-ui
```

Generators scaffold code, update `tsconfig.json` paths, add the package to the workspace — all in one command.

### nx.json

```json
{
  "targetDefaults": {
    "build": {
      "dependsOn": ["^build"],
      "cache": true
    },
    "test": {
      "cache": true
    }
  },
  "namedInputs": {
    "default": ["{projectRoot}/**/*", "sharedGlobals"],
    "production": ["default", "!{projectRoot}/**/*.spec.ts"]
  },
  "nxCloud": true    // remote cache via Nx Cloud
}
```

---

## Package Structure — Shared Code

The main reason to use a monorepo: share code across apps without publishing to npm.

```
packages/
├── ui/                    Shared React components
│   ├── src/
│   │   ├── Button.tsx
│   │   └── index.ts       // export * from './Button'
│   ├── package.json       { "name": "@myapp/ui", "main": "dist/index.js" }
│   └── tsconfig.json
│
├── utils/                 Shared utilities (date formatting, validation, etc.)
│   ├── src/
│   └── package.json       { "name": "@myapp/utils" }
│
├── types/                 Shared TypeScript types (API contracts, DTOs)
│   ├── src/
│   └── package.json       { "name": "@myapp/types" }
│
└── config/                Shared tooling config (eslint, tsconfig, vitest)
    ├── eslint-base.js
    ├── tsconfig.base.json
    └── package.json       { "name": "@myapp/config" }
```

```json
// apps/web/package.json
{
  "name": "@myapp/web",
  "dependencies": {
    "@myapp/ui": "*",       // "*" = always use local workspace version
    "@myapp/utils": "*",
    "@myapp/types": "*"
  }
}
```

### TypeScript Path Aliases

```json
// tsconfig.base.json (root)
{
  "compilerOptions": {
    "paths": {
      "@myapp/ui": ["packages/ui/src/index.ts"],
      "@myapp/utils": ["packages/utils/src/index.ts"],
      "@myapp/types": ["packages/types/src/index.ts"]
    }
  }
}
```

Each app extends this base, so `import { Button } from "@myapp/ui"` resolves to the local source — no build step needed during dev.

---

## CI in a Monorepo

```yaml
# GitHub Actions — Turbo with remote cache
name: CI

on:
  push:
    branches: [main]
  pull_request:

jobs:
  build-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 2              # needed for --filter=[HEAD^1]

      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: npm

      - run: npm ci

      - name: Build + Test (Turbo)
        run: turbo build test lint
        env:
          TURBO_TOKEN: ${{ secrets.TURBO_TOKEN }}   # remote cache auth
          TURBO_TEAM: ${{ vars.TURBO_TEAM }}

      # For Nx:
      # - run: npx nx affected --target=test --base=origin/main
```

Remote cache means: if you ran `turbo build` locally with no changes, CI hits 100% cache — finishes in seconds instead of minutes.

---

## Common Confusion Points

**Workspaces ≠ Turborepo/Nx.**
npm/pnpm/yarn workspaces handle package linking and installation. Turbo/Nx handle task orchestration and caching. You need both. Workspaces alone will re-run everything every time.

**`"^build"` in turbo.json.**
The `^` means "topological" — run this task in dependencies first. Without it, tasks run in parallel regardless of dependency order. You almost always want `^build` for build tasks.

**Turbo cache is per-machine by default.**
The local `.turbo/` cache is only on your machine. CI gets no benefit unless you set up remote cache (Vercel Remote Cache, self-hosted). Remote cache is the main value prop for CI.

**Don't put everything in one giant package.**
A monorepo isn't a monolith. Keep packages focused. `packages/utils` shouldn't import from `apps/web` — dependencies should point inward (apps depend on packages, not the reverse). Nx enforces this with `enforceModuleBoundaries`.

**Version management: internal vs published packages.**
Internal packages (`"@myapp/ui"`) don't need versioning — consumers always use the latest. Published packages (npm-published libraries) still need versioning. Tools like Changesets handle the latter in a monorepo.

**pnpm vs npm in monorepos.**
pnpm is preferred for monorepos: stricter hoisting (prevents phantom dependencies), faster installs, smaller `node_modules`. The `--filter` flag is also more powerful than npm's `--workspace`.

---

## Old World Bridge

<!-- @editor[content/P2]: Bridge table maps MSBuild incremental to "Turbo/Nx cache + affected commands" but doesn't call out the critical difference: MSBuild incremental is local-only and timestamp-based, while Turbo remote cache is content-addressed and shared across all machines. A reader coming from MSBuild will assume "incremental build" means what they already know — that assumption is wrong and leads to misunderstanding the remote cache value proposition. Add a note to that row. -->

| Source Depot / VSTS / .NET Ecosystem | Monorepo Equivalent |
|---|---|
| One large Source Depot enlistment | Monorepo (same idea — one checkout, many projects) |
| Solution file (.sln) containing multiple projects | Workspace root with `apps/*` and `packages/*` |
| Project references in .csproj | `dependencies` in package.json pointing to sibling packages |
| NuGet package for internal shared code | Workspace package (no publish needed) |
| VSTS build with multiple build definitions | Turbo/Nx pipeline running affected tasks |
| Global Assembly Cache (GAC) | Hoisted `node_modules` at workspace root |
| MSBuild dependency ordering | `"dependsOn": ["^build"]` in turbo.json |
| Build incremental (only changed projects) | Turbo/Nx cache + affected commands |
| Shared .editorconfig, .ruleset across projects | `packages/config` with shared ESLint/TSConfig |

---

## Decision Cheat Sheet

| I want to... | Use |
|---|---|
| Share code between apps without publishing to npm | Monorepo with workspaces |
| Build only what changed | Turborepo or Nx with affected commands |
| Cache build outputs across CI runs | Remote cache (Turbo → Vercel, Nx → Nx Cloud) |
| Simple task orchestration, lean setup | Turborepo |
| Code generation, IDE integration, enterprise scale | Nx |
| Manage package installs in a monorepo | pnpm workspaces (preferred) |
| Enforce that apps don't import from other apps | Nx module boundaries |
| Publish some packages to npm, keep others internal | Changesets for versioning + Turbo/Nx for building |
| Visualize which packages depend on what | `nx graph` or `turbo build --graph` |
| Run only tests for code a PR touches | `nx affected --target=test` or `turbo --filter=...[HEAD^1]` |
