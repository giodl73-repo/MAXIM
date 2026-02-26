# Build Tools & Bundlers — A Layered Guide

## The Big Picture

Build tools solve a problem that doesn't exist in .NET: browsers can't natively consume a modern frontend codebase. You need a build step to transform it into something a browser can load efficiently.

```
+------------------------------------------------------------------+
|                    THE BUILD TOOL LANDSCAPE                      |
|                                                                  |
|  SOURCE (what you write)       OUTPUT (what the browser gets)   |
|  ----------------------        ------------------------------    |
|  TypeScript                    Minified JavaScript bundles       |
|  JSX / TSX                     Hashed filenames (cache busting)  |
|  CSS Modules / SASS            Optimized CSS                     |
|  Images, fonts, SVG            Base64-inlined or hashed assets   |
|  ES Modules (hundreds)         A few large bundles               |
|  node_modules deps             Tree-shaken (dead code removed)   |
|                                                                  |
|                        BUILD TOOL                                |
|                      (the transform)                             |
|                                                                  |
|  TRANSPILERS          BUNDLERS           DEV SERVERS             |
|  ----------           --------           -----------             |
|  tsc                  Webpack            Vite dev server         |
|  esbuild              Rollup             Webpack DevServer       |
|  SWC                  esbuild            Turbopack               |
|  Babel                Vite (uses         parcel                  |
|                        Rollup in prod,                           |
|                        esbuild in dev)                           |
+------------------------------------------------------------------+
```

**Transpilers** transform code (TS→JS, JSX→JS, new syntax→old). **Bundlers** combine many files into fewer files, optimize them, and handle non-JS assets. Most modern tools do both.

---

## Why Bundlers Exist

### The HTTP Problem

```
  Without a bundler:
  Your app has 300 JS files. Browser makes 300 HTTP requests.
  Even with HTTP/2 multiplexing, this has overhead.
  Each module resolution requires a round trip.

  +--------+     GET /src/app.js           +--------+
  |        | --> GET /src/router.js     --> |        |
  | Browser|     GET /src/auth.js          | Server |
  |        |     GET /src/utils.js         |        |
  |        |     ...×300                   |        |
  +--------+                               +--------+

  With a bundler:
  +--------+     GET /dist/app.a3f1c9.js   +--------+
  | Browser| --> GET /dist/vendor.82be4a.js| Server |
  +--------+     GET /dist/styles.cf2d1e.css +------+

  2-3 HTTP requests. Cached aggressively (hashed filenames).
```

### The Module Problem

```
  Browser support for native ES modules (import/export) arrived ~2018.
  Before that: no module system in browsers. Period.

  Node.js packages use CommonJS (require/module.exports).
  Browsers can't run require() — it doesn't exist.
  Even today, most npm packages can't be directly used in a browser.

  Bundler resolves this:
  - Reads your import graph (every import statement)
  - Follows it into node_modules
  - Combines everything into browser-runnable JS
  - Handles CJS/ESM interop automatically
```

### The Assets Problem

```
  Modern frontend isn't just JS. A React component might import:

  import styles from './Button.module.css'   // CSS
  import logo from './logo.svg'              // image
  import data from './config.json'           // data

  None of these are valid JS imports.
  Bundlers transform them:
  - CSS Modules → inject <style> at runtime, export class name map
  - SVG → inline as React component OR as a URL string
  - JSON → inline as a JS object
  - Images → URL reference or base64-encoded string
```

---

## The Tool Genealogy

Understanding why each tool exists requires the timeline:

```
  ~2012   GRUNT / GULP
  -----   Task runners. "Do things in sequence."
          grunt minify, grunt concat, grunt sass
          Not bundlers — just scripted transforms.
          Now: almost entirely replaced.

  ~2012   BROWSERIFY
  -----   First real bundler. "Let you use require() in the browser."
          Solved the CJS-in-browser problem.
          Now: obsolete.

  ~2014   WEBPACK
  -----   The dominant bundler for ~8 years.
          Solved everything: modules, assets, code splitting, HMR.
          Highly configurable. Notoriously complex.
          Still: widely used, especially in Create React App / Next.js.

  ~2015   ROLLUP
  -----   Built for libraries, not apps.
          Invented tree-shaking. Clean ESM output.
          Powers Vite in production mode.
          Still: the right choice for publishing libraries.

  ~2018   PARCEL
  -----   "Zero config webpack alternative."
          Auto-detects everything. Good DX.
          Less adopted than expected.

  ~2020   ESBUILD
  -----   Written in Go. 10-100x faster than Webpack/Rollup.
          Transforms and bundles but limited plugin ecosystem.
          Not a full Webpack replacement, but powers Vite in dev mode.

  ~2020   SWC
  -----   Written in Rust. Like esbuild — blazing fast transpiler.
          Drop-in Babel replacement. Used by Next.js 12+.

  ~2021   VITE
  -----   The modern default for new projects.
          Dev: esbuild (fast transforms, native ESM serving)
          Prod: Rollup (optimized bundling)
          Best DX of any tool so far.

  ~2022   TURBOPACK
  -----   Written in Rust by Vercel (Next.js team).
          Webpack successor. Incremental compilation.
          Still maturing — Next.js 13+ uses it optionally.
```

---

## Core Concepts Every Bundler Implements

### Entry Point and the Module Graph

```
  ENTRY POINT
  app.ts
     |
     ├── import router from './router'
     │       ├── import { Link } from './components/Link'
     │       └── import express from 'node_modules/express'
     │
     ├── import { auth } from './auth'
     │       └── import jwt from 'node_modules/jsonwebtoken'
     │
     └── import './styles/main.css'
             └── @import './variables.css'

  Bundler follows every import recursively → MODULE GRAPH
  Then bundles leaf-to-root → OUTPUT BUNDLE(S)
```

<!-- @editor[bridge/P2]: The MSBuild conceptual bridge is absent at the module graph level. The learner knows MSBuild's dependency graph between targets (Target A depends on Target B's outputs, MSBuild topologically sorts and executes). The bundler's module graph is the same concept applied to files: each file is a node, each import is a directed edge, the bundler does a topological sort and emits leaf-to-root. The incremental build analogy is also exact: MSBuild checks input/output timestamps to skip unchanged targets; Vite's dev server checks file modification times and module graph ancestry to invalidate only the changed subgraph. Adding "MSBuild targets/tasks/incremental build → bundler plugin hooks/module graph invalidation" as an explicit ASCII comparison here would be high-value for this reader. -->

### Tree Shaking

```
  Dead code elimination based on static import analysis.

  // math.ts — exports 3 functions
  export function add(a, b) { return a + b }
  export function subtract(a, b) { return a - b }
  export function multiply(a, b) { return a * b }

  // app.ts — only uses one
  import { add } from './math'

  WEBPACK / ROLLUP / ESBUILD analyze the import graph.
  subtract and multiply are never imported anywhere.
  They are EXCLUDED from the bundle ("shaken out").

  Requires ESM (import/export). CJS (require) is not tree-shakeable
  because require() is dynamic — can't be analyzed statically.

  This is why the ecosystem migrated from CJS to ESM.
  A 10KB utility library you use one function from → stays 10KB
  unless it ships ESM and your bundler tree-shakes.
```

### Code Splitting

```
  Instead of one giant bundle, split into multiple chunks.
  Load only what's needed for the current route/page.

  STATIC SPLIT (vendor chunk):
  +--------------+    +-----------------+
  | app.abc123.js|    | vendor.def456.js|
  | Your code    |    | react, lodash,  |
  | ~50 KB       |    | big libraries   |
  +--------------+    | ~300 KB, cached |
                      +-----------------+
  app bundle changes on every deploy.
  vendor bundle stays cached in browser across deploys.

  DYNAMIC SPLIT (route-based lazy loading):
  import('./pages/Dashboard')   // loaded only when user visits /dashboard
  import('./pages/Settings')    // loaded only when user visits /settings

  Result: initial page load is small. Route chunks load on demand.
```

### Hashed Filenames (Cache Busting)

```
  Every output file gets a content hash in its filename:
  app.a3f1c9d2.js    (hash changes only when content changes)

  WHY:
  Browser caches files by URL. If the URL is always app.js,
  the browser might serve stale cached JS after a deploy.

  With content hashes:
  - File content unchanged → same hash → browser uses cache ✓
  - File content changed  → new hash → browser fetches new version ✓
  - Vendor libs rarely change → vendor hash stable → long-cached ✓
```

### Source Maps

```
  Your source:    TypeScript, many files, readable names
  The bundle:     Minified JS, one file, mangled names: a(b,c){return b+c}

  A .map file links output positions back to source positions.
  DevTools uses it to show you the original TypeScript in the debugger.

  app.abc123.js          actual browser code (minified)
  app.abc123.js.map      "line 1, col 47 = src/auth.ts, line 23, col 12"

  In production: ship maps to error tracking (Sentry) but not browsers.
  In development: always on.
```

### Hot Module Replacement (HMR)

```
  Traditional dev workflow:
  Edit file → bundler rebuilds EVERYTHING → browser hard-reloads
  React app loses state: you navigated to a nested page,
  now you're back at root.

  HMR:
  Edit file → only that module is re-executed → state preserved
  Change the color of a button → button updates in place.
  No full reload. No lost state.

  Vite's HMR is native ESM based — surgical updates.
  Webpack's HMR requires more configuration.
```

---

## Vite — The Modern Default

Vite (French: "fast") is the tool you should reach for first in 2026 for any new browser-targeted project.

```
  ARCHITECTURE: DEV vs PROD are fundamentally different

  DEVELOPMENT MODE
  +--------------------------------------------------+
  | Browser requests http://localhost:5173/app.ts    |
  |                                                  |
  | Vite dev server intercepts:                      |
  | 1. Transforms file on demand (esbuild, <10ms)   |
  | 2. Serves as native ES module                   |
  | 3. Browser handles module graph resolution       |
  |                                                  |
  | No bundling. Each file served individually.      |
  | Startup is instant regardless of project size.   |
  | HMR is fast because only changed modules update. |
  +--------------------------------------------------+

  PRODUCTION BUILD
  +--------------------------------------------------+
  | vite build                                       |
  |                                                  |
  | Uses Rollup internally:                          |
  | - Full bundle optimization                       |
  | - Tree shaking                                   |
  | - Code splitting                                 |
  | - Asset hashing                                  |
  | - CSS extraction                                 |
  | Output: dist/ ready for deployment               |
  +--------------------------------------------------+
```

### Vite Config

```typescript
  // vite.config.ts
  import { defineConfig } from 'vite'
  import react from '@vitejs/plugin-react'
  import path from 'path'

  export default defineConfig({
    plugins: [
      react()             // enables JSX transform + React Fast Refresh (HMR)
    ],

    resolve: {
      alias: {
        '@': path.resolve(__dirname, './src')   // import from '@/utils'
      }
    },

    build: {
      outDir: 'dist',
      sourcemap: true,
      rollupOptions: {
        output: {
          manualChunks: {
            vendor: ['react', 'react-dom'],    // split vendor chunk
          }
        }
      }
    },

    server: {
      port: 3000,
      proxy: {
        '/api': 'http://localhost:8080'        // forward /api to backend
      }
    }
  })
```

### Vite Project Structure

```
  project/
  ├── index.html          Entry point (Vite serves from root, not /public)
  ├── vite.config.ts
  ├── src/
  │   ├── main.tsx        App entry (referenced in index.html)
  │   ├── App.tsx
  │   └── ...
  ├── public/             Static assets served as-is (no hashing)
  │   └── favicon.ico
  └── dist/               Build output (gitignored)
      ├── index.html
      ├── assets/
      │   ├── app.a3f1c9.js
      │   └── vendor.82be4a.js
      └── ...
```

### Vite Plugins

```
  @vitejs/plugin-react       React JSX + Fast Refresh
  @vitejs/plugin-react-swc   React JSX via SWC (faster)
  @vitejs/plugin-vue         Vue SFC support
  vite-plugin-svgr           Import SVGs as React components
  vite-tsconfig-paths        Honor tsconfig path aliases

  Install: npm install --save-dev @vitejs/plugin-react
  Add to plugins array in vite.config.ts
```

---

## Webpack — The Incumbent

Webpack is the tool you'll encounter in existing codebases, especially anything built before ~2022.

```
  STRENGTHS:
  - Mature ecosystem, plugin for everything
  - Handles every asset type imaginable
  - Fine-grained control over chunking
  - Create React App (legacy), Next.js (pre-13) use it

  WEAKNESSES:
  - Config is notoriously verbose and confusing
  - Slow cold starts on large projects
  - Incremental rebuilds are fast but not Vite-fast
  - Being replaced by Vite for new projects
```

### Webpack Config (simplified)

```javascript
  // webpack.config.js
  const path = require('path')
  const HtmlWebpackPlugin = require('html-webpack-plugin')

  module.exports = {
    entry: './src/index.tsx',       // where the module graph starts

    output: {
      path: path.resolve(__dirname, 'dist'),
      filename: '[name].[contenthash].js',   // content-hashed names
      clean: true,                            // clean dist before build
    },

    module: {
      rules: [
        {
          test: /\.tsx?$/,            // for .ts and .tsx files...
          use: 'ts-loader',           // ...use TypeScript loader
          exclude: /node_modules/,
        },
        {
          test: /\.css$/,
          use: ['style-loader', 'css-loader'],  // CSS pipeline
        },
      ],
    },

    resolve: {
      extensions: ['.tsx', '.ts', '.js'],  // resolve in this order
    },

    plugins: [
      new HtmlWebpackPlugin({ template: './index.html' }),
    ],

    devServer: {
      hot: true,           // HMR
      port: 3000,
    },
  }
```

### Webpack Loaders vs Plugins

```
  LOADERS                           PLUGINS
  -------                           -------
  Transform individual files        Operate on the full bundle
  Applied per file type             Applied during build lifecycle
  Configured in module.rules        Configured in plugins array

  ts-loader     TS → JS             HtmlWebpackPlugin    inject script tags
  css-loader    CSS → JS module     MiniCssExtractPlugin extract CSS file
  file-loader   copy asset, return  DefinePlugin         replace constants
                URL string          BundleAnalyzerPlugin visualize bundle
```

---

## esbuild — The Speed Engine

esbuild is written in Go. It is 10-100x faster than Webpack/Rollup for the same transformations.

```
  WHAT IT DOES:
  - Transpiles TypeScript (strips types, no type checking)
  - Transpiles JSX
  - Bundles ES modules
  - Minifies
  - Tree shakes

  WHAT IT DOESN'T DO (well):
  - Full plugin ecosystem (limited vs webpack)
  - Code splitting (basic support only)
  - CSS modules (not built-in)
  - HMR (not its job)

  WHO USES IT:
  - Vite dev server (transforms on demand)
  - ESBuild CLI for fast builds of simple projects
  - CI pipelines where speed matters
  - Library authors for fast builds

  USAGE:
  npx esbuild src/index.ts --bundle --outfile=dist/out.js --platform=node
  npx esbuild src/index.ts --bundle --outfile=dist/out.js --platform=browser
```

---

## SWC — The Rust Transpiler

SWC (Speedy Web Compiler) is to Babel what esbuild is to tsc: a drop-in replacement that's dramatically faster.

```
  SWC vs Babel:
  +-------------------+-------------------+
  | Babel             | SWC               |
  +-------------------+-------------------+
  | Written in JS     | Written in Rust   |
  | Slow              | 20x faster        |
  | Huge plugin eco   | Growing eco       |
  | The original      | The replacement   |
  | transform tool    |                   |
  +-------------------+-------------------+

  WHO USES IT:
  - Next.js (replaced Babel with SWC in v12)
  - Vite can use it via @vitejs/plugin-react-swc
  - Jest via @swc/jest for fast test transforms

  NOTE: SWC transforms only. No type checking. Still pair with tsc --noEmit.
```

---

## Rollup — Library Bundling

Rollup is the right tool when you're building a library to publish to npm, not an app.

```
  APP BUNDLER (Webpack/Vite)     LIBRARY BUNDLER (Rollup)
  ----------------------         -----------------------
  Output: 1-3 large bundles      Output: multiple formats
  Includes all deps              Marks deps as "external"
  (react bundled in)             (react NOT bundled — consumer provides it)
  Hashed filenames               Clean filenames (lib.js, lib.cjs)
  Optimized for browser          Optimized for npm consumers

  Rollup output formats:
  esm    → import/export (for bundlers consuming your lib)
  cjs    → require/module.exports (for Node.js)
  umd    → works in browser script tag AND require() AND import
  iife   → self-executing, for direct browser <script> include

  vite build --mode lib    uses Rollup under the hood for lib mode
```

---

## Babel — The Legacy Transpiler

Babel was the original JS transpiler (2014). It enabled using ES2015+ features before browsers supported them.

```
  WHAT BABEL DOES:
  - Transforms modern JS syntax to older JS
  - Transforms JSX to React.createElement() calls
  - Plugins for every proposal/syntax
  - Does NOT type-check TypeScript (just strips types)

  STATUS IN 2026:
  - Still widely used in legacy Webpack setups
  - Create React App uses it
  - Being replaced by SWC and esbuild (10-20x faster)
  - New projects should not reach for Babel first

  .babelrc / babel.config.json:
  {
    "presets": [
      ["@babel/preset-env", { "targets": "defaults" }],
      "@babel/preset-typescript",
      ["@babel/preset-react", { "runtime": "automatic" }]
    ]
  }

  @babel/preset-env       Modern JS → target browser JS
  @babel/preset-typescript  Strip TS types
  @babel/preset-react     JSX → React calls
```

---

## The TypeScript / Bundler Relationship

These two tools touch the same files but do different jobs. They need to be configured together.

```
  tsconfig.json                  vite.config.ts / webpack.config.js
  --------------------------     ----------------------------------
  Governs type checking          Governs bundling/serving
  Governs output format (tsc)    Governs output format (bundler)

  KEY SETTING INTERACTION:

  tsconfig "module"              What bundler expects
  --------------------           --------------------
  "ESNext"                       Vite/Rollup/esbuild: use this
  "CommonJS"                     Node.js without ESM
  "NodeNext"                     Node.js native ESM

  tsconfig "moduleResolution"    Must match bundler behavior
  ---------------------------
  "Bundler"                      For Vite/esbuild/Rollup (modern)
  "Node16" / "NodeNext"          For Node.js native ESM
  "Node"                         Legacy (don't use for new projects)

  tsconfig "noEmit": true        When bundler handles compilation
                                 (Vite, Webpack with ts-loader)
                                 tsc only type-checks, doesn't emit files

  The typical modern setup:
  tsconfig.json: { "noEmit": true, "module": "ESNext", "moduleResolution": "Bundler" }
  vite.config.ts: handles actual compilation and bundling
  CI: run tsc --noEmit AND vite build in parallel
```

---

## npm Scripts — The Glue

```
  package.json scripts wire build tools to simple commands:

  {
    "scripts": {
      "dev":     "vite",                        // start dev server
      "build":   "tsc --noEmit && vite build",  // type-check then bundle
      "preview": "vite preview",                // preview prod build locally
      "test":    "vitest",
      "lint":    "eslint src --ext .ts,.tsx"
    }
  }

  npm run dev       -> starts Vite dev server on localhost:5173
  npm run build     -> produces dist/
  npm run preview   -> serves dist/ locally for QA

  "prebuild" and "postbuild" hooks run automatically:
  "prebuild": "rimraf dist"    cleans dist before every build
```

---

## Bundle Analysis — Finding What's Big

```
  When your bundle is unexpectedly large, visualize it:

  Vite:
  npm install --save-dev rollup-plugin-visualizer
  // vite.config.ts: plugins: [visualizer({ open: true })]
  vite build   -> opens treemap in browser

  Webpack:
  npm install --save-dev webpack-bundle-analyzer

  You'll find:
  - A library included twice (CJS + ESM versions)
  - A huge utility library where you only use one function
  - Unintentionally bundled server-only code
  - moment.js with all 160KB of locale data
```

---

## Common Confusion Points

### "Vite is fast but the production build is slow?"

```
  Correct. This is by design.

  Dev server: esbuild-based, no bundling, serves ESM directly.
  Instant. No Rollup involved.

  Production build: Rollup-based, full optimization.
  Rollup is slower but produces optimal chunks.
  "Slow" here means seconds, not minutes.
  For actual slow prod builds, check what Rollup is bundling.
```

### "Should I use tsc or esbuild to compile TypeScript?"

```
  They do different things:

  tsc:     Type checks AND compiles.
           Slow. Catches all type errors.
           Use for: CI type checking gate.

  esbuild: Transpiles ONLY (strips types, no checking).
           Fast. Misses type errors.
           Use for: dev server transforms, fast production bundling.

  Modern pattern: both.
  tsc --noEmit  (just check, no output)
  esbuild / vite build  (just transform, no check)
  Run both in CI. Fail on either.
```

### "What's the difference between a loader and a plugin in Webpack?"

```
  Loader: transforms ONE file's content.
    input: file bytes → output: JS string
    e.g., ts-loader transforms myComponent.ts into JS

  Plugin: hooks into the BUILD PROCESS.
    Can access the full module graph, modify output, inject assets.
    e.g., HtmlWebpackPlugin creates index.html with script tags injected.

  Rule of thumb: if it transforms a file type, it's a loader.
  If it does something more broad, it's a plugin.
```

### "Vite vs Next.js — are these the same thing?"

```
  NO. Different layers.

  Vite:      Build tool. Serves and bundles your app.
             Framework-agnostic.
             You choose React/Vue/Svelte/etc.
             Client-side rendering by default.

  Next.js:   React meta-framework.
             Adds: routing, SSR, SSG, API routes, image optimization.
             Uses Webpack (legacy) or Turbopack (new) under the hood.
             Opinionated full-stack framework.

  Analogy: Vite is like MSBuild. Next.js is like ASP.NET MVC.
  One is the build engine; the other is the application framework.

  Use Vite when: building a pure SPA, a library, or using a
                 non-Next framework (Vue, Svelte, React without SSR).
  Use Next.js when: you need SSR, SSG, or a full-stack React framework.
```

### "Why does import './styles.css' work in JS?"

```
  It shouldn't — CSS is not a JS module.
  The bundler intercepts it.

  Webpack: css-loader parses CSS, style-loader injects <style> at runtime.
  Vite: built-in CSS handling, injects <style> in dev, extracts file in prod.

  It's a bundler convention, not a JavaScript feature.
  This code WILL break if you try to run it with plain Node.js.
```

---

## Old World → New World Bridge

| .NET / MSBuild concept | Frontend build equivalent | Notes |
|---|---|---|
| MSBuild | Webpack / Vite / Rollup | The build orchestrator |
| `.csproj` targets | `package.json` scripts | Where build steps are defined |
| `bin/Release/` | `dist/` | Output directory |
| Assembly linker | Bundler | Combines modules into outputs |
| `web.config` bundling (System.Web.Optimization) | Webpack / Vite | Same concept: bundle+minify |
| T4 templates | Vite plugins / code generators | Transform files at build time |
| Conditional compilation `#if DEBUG` | `import.meta.env.MODE`, `process.env.NODE_ENV` | `"development"` vs `"production"` |
| `dotnet watch` | Vite dev server / `webpack serve` | Watch + rebuild on change |
| Strong-named assemblies / GAC | npm packages / node_modules | Dependency resolution |
| ILMerge (merge assemblies) | Bundle all deps into one output | Rollup UMD for single-file libs |
| Source step-through debugging | Source maps + DevTools | Same intent, different mechanism |
| PDB files | `.map` files | "Where in source does this output line correspond to?" |
| `csc.exe` (C# compiler) | `tsc` / `esbuild` / `swc` | The actual code transformer |
| Roslyn analyzers | ESLint / TypeScript strict mode | Static analysis during build |
| NuGet restore → `packages/` | `npm install` → `node_modules/` | Dependency materialization step |
| MSBuild Target (named unit of work with inputs/outputs) | Vite/Rollup plugin hook (buildStart, transform, generateBundle) | Plugin hooks are the extensibility model |
| MSBuild incremental build (skip target if outputs newer than inputs) | Vite module graph invalidation (only re-transform changed files and their dependents) | Same concept: skip unchanged work |
| MSBuild dependency between targets (DependsOnTargets) | Module graph edges (import statements drive rebuild order) | The import graph IS the dependency graph |

<!-- @editor[bridge/P2]: The MSBuild targets/tasks conceptual bridge in the table above is present but thin. The learner built VSTS and knows MSBuild at architectural depth: targets have Inputs/Outputs attributes that enable incremental builds; the build engine evaluates the dependency graph of targets; a Task is an atomic unit of work (ITask interface). Vite's plugin system maps exactly: a plugin is an object with named hook functions (buildStart, resolveId, load, transform, generateBundle, writeBundle) that correspond to phases of the Rollup build lifecycle — the same DAG-driven, hook-based extensibility model. A small ASCII diagram showing the Vite/Rollup plugin hook lifecycle alongside the MSBuild target lifecycle phases would make this concrete for someone who already understands the model deeply in the .NET world. -->

---

## Decision Cheat Sheet

| I want to... | Use |
|---|---|
| Start a new React / Vue app | Vite (`npm create vite@latest`) |
| Start a new Next.js app | Next.js (`npx create-next-app@latest`) |
| Build a library to publish on npm | Rollup (or Vite in lib mode) |
| Work on an existing Webpack app | Stay on Webpack; migrate to Vite when opportunity arises |
| Speed up TypeScript compilation | esbuild or SWC (replace tsc for emit, keep tsc for type-check) |
| Replace Babel | SWC |
| Type-check in CI without emitting | `tsc --noEmit` |
| See what's making my bundle large | rollup-plugin-visualizer (Vite) or webpack-bundle-analyzer |
| Lazy-load a route | `import()` dynamic import — bundler handles the split |
| Configure path aliases (@/components) | `resolve.alias` in vite.config or `paths` in tsconfig |
| Add CSS Modules to Vite | Built-in: name files `.module.css`, import as object |
| Understand a Webpack config I inherited | Read the `entry`, `output`, `module.rules`, `plugins` sections in that order |
| Know if Vite or Webpack is being used | Check `package.json` devDependencies and scripts |
