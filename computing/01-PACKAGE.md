# Package Management Systems — A Layered Guide

## The Big Picture

Package managers exist at **different layers** of the software stack. The confusion comes from the fact that they overlap, nest inside each other, and sometimes compete.

```
+---------------------------------------------------------------+
|                    SYSTEM / OS LAYER                          |
|  winget, choco, apt, brew, scoop                              |
|  Installs: runtimes, tools, apps, drivers                     |
+---------------------------------------------------------------+
        |           |           |           |           |
        v           v           v           v           v
   +---------+ +---------+ +---------+ +---------+ +---------+
   | Python  | | Node.js | | .NET    | | Rust    | | Java    |
   | RUNTIME | | RUNTIME | | RUNTIME | | RUNTIME | | RUNTIME |
   +---------+ +---------+ +---------+ +---------+ +---------+
        |           |           |           |           |
        v           v           v           v           v
   +---------+ +---------+ +---------+ +---------+ +---------+
   |  pip    | |  npm    | |  nuget  | |  cargo  | |  maven  |
   | poetry  | |  pnpm   | |  dotnet | |         | | gradle  |
   |  uv     | |  yarn   | |         | |         | |         |
   | LANG PM | | LANG PM | | LANG PM | | LANG PM | | LANG PM |
   +---------+ +---------+ +---------+ +---------+ +---------+
        |           |           |           |           |
        v           v           v           v           v
   +---------+ +---------+ +---------+ +---------+ +---------+
   |requests | | react   | |Newtonsft| | serde   | | spring  |
   |numpy    | | express | |EF Core  | | tokio   | | jackson |
   | LIBS    | | LIBS    | | LIBS    | | LIBS    | | LIBS    |
   +---------+ +---------+ +---------+ +---------+ +---------+
```

**Read this diagram bottom-up**: Libraries are installed by language package managers, which run on runtimes, which are installed by system package managers.

---

## Layer 1: System / OS Package Managers

These install **anything** — runtimes, tools, applications, even other package managers.

| Manager | OS | Registry | Installs |
|---------|-----|----------|----------|
| **winget** | Windows | Microsoft Store / winget repo | Apps, tools, runtimes |
| **choco** | Windows | chocolatey.org | Apps, tools, runtimes, dev tools |
| **scoop** | Windows | GitHub buckets | CLI tools, dev tools (no admin needed) |
| **apt** | Debian/Ubuntu | distro repos | Everything on Linux |
| **brew** | macOS (+ Linux) | Homebrew formulae | CLI tools, apps, runtimes |
| **snap** | Linux | Snap Store | Sandboxed apps |
| **flatpak** | Linux | Flathub | Sandboxed desktop apps |
| **pacman** | Arch Linux | Arch repos + AUR | Everything on Arch |

### What makes them "system-level"?

They manage **the OS environment itself**. When you run `choco install python` or `winget install Python.Python.3`, you're putting `python.exe` on your PATH so every other tool can find it.

```
You type: choco install nodejs
                |
                v
Chocolatey downloads Node.js installer
                |
                v
Node.js runtime + npm are now on your PATH
                |
                v
Now you can run: npm install react
```

### Windows: winget vs choco vs scoop

```
                  +------------------+
                  |    YOU WANT TO   |
                  |  INSTALL STUFF   |
                  +------------------+
                     /     |     \
                    /      |      \
                   v       v       v
            +--------+ +--------+ +--------+
            | winget | | choco  | | scoop  |
            +--------+ +--------+ +--------+
            |Built-in| |Most    | |No admin|
            |to Win11| |packages| |needed  |
            |Simple  | |Auto-   | |Dev-tool|
            |        | |update  | |focused |
            +--------+ +--------+ +--------+

  Think of it as:
  - winget = Windows "app store" from the command line
  - choco  = apt/brew for Windows (broadest catalog)
  - scoop  = lightweight, no-admin, CLI-tool focused
```

**You can use all three** — they don't conflict. Most people pick one as primary.

---

## Layer 2: Language / Runtime Package Managers

These install **libraries and frameworks** for a specific programming language. They only work after the runtime is installed (by Layer 1).

### The Major Ecosystems

```
+------------------------------------------------------------------+
|                        LANGUAGE LAYER                            |
|                                                                  |
|  PYTHON          NODE.JS         .NET           RUST             |
|  -------         --------        -----          -----            |
|  Registry:       Registry:       Registry:      Registry:        |
|  PyPI             npmjs.com      nuget.org      crates.io        |
|                                                                  |
|  Managers:       Managers:       Manager:       Manager:         |
|  pip             npm             dotnet CLI     cargo            |
|  poetry          pnpm            (nuget CLI)                     |
|  uv              yarn                                            |
|  conda           bun                                             |
|                                                                  |
|  Lock file:      Lock file:      Lock file:     Lock file:       |
|  requirements.   package-        packages.      Cargo.lock       |
|  txt / poetry.   lock.json       lock.json                       |
|  lock / uv.lock                                                  |
|                                                                  |
|  Project file:   Project file:   Project file:  Project file:    |
|  pyproject.toml  package.json    .csproj        Cargo.toml       |
+------------------------------------------------------------------+
```

### Python Ecosystem (the most confusing one)

Python has the most package managers because the ecosystem evolved messily over 30 years.

```
                    PYTHON PACKAGING
                    ================

  +----------+    The OG. Comes with Python.
  |   pip    |    pip install requests
  +----------+    No lock file. No environments.
       |
       v
  +----------+    pip + virtual environments.
  | venv/    |    Isolates per-project dependencies.
  | virtualenv    python -m venv .venv
  +----------+    source .venv/bin/activate
       |
       v
  +----------+    pip + venv + lock file + publishing.
  | poetry   |    poetry add requests
  +----------+    Closest to npm's experience.
       |
       v
  +----------+    Blazing fast pip/poetry replacement.
  |    uv    |    Written in Rust. Drop-in compatible.
  +----------+    uv pip install requests
       |
       |          Totally separate ecosystem.
       v          Installs Python ITSELF + packages.
  +----------+    Has its own package repo (conda-forge).
  |  conda   |    Used heavily in data science.
  +----------+    conda install numpy
```

**Which to use?**
- Starting fresh in 2026: **uv** (fast, modern, handles everything)
- Data science: **conda** or **mamba** (handles C/Fortran deps that pip can't)
- Legacy projects: **pip + venv** (it works, everyone knows it)

### Node.js Ecosystem

```
                    NODE.JS PACKAGING
                    =================

  +----------+    Comes with Node.js.
  |   npm    |    npm install react
  +----------+    The default. Everyone has it.
       |
  +----------+    Faster, stricter, disk-efficient.
  |   pnpm   |    Uses symlinks + content-addressable store.
  +----------+    pnpm install react
       |
  +----------+    Facebook's alternative to npm.
  |   yarn   |    yarn add react
  +----------+    Plug'n'Play mode (no node_modules).
       |
  +----------+    Runtime + package manager + bundler.
  |   bun    |    All-in-one. Written in Zig.
  +----------+    bun install react
```

**All four** read `package.json` and install from **npmjs.com**. They differ in speed, disk usage, and lock file format — but the packages are the same.

```
  Same registry (npmjs.com)
  Same project file (package.json)
  Different lock files:
    npm  -> package-lock.json
    pnpm -> pnpm-lock.yaml
    yarn -> yarn.lock
    bun  -> bun.lockb
```

### .NET Ecosystem

```
                    .NET PACKAGING
                    ==============

  +-------------+
  | dotnet CLI  |
  +-------------+
  Command: dotnet add package Newtonsoft.Json — The one and only. Simple.
         |
         v
  +-------------+
  |  nuget.org  |
  +-------------+
  The registry. Like PyPI or npmjs.
         |
         v
  +-------------+
  |   .csproj   |
  +-------------+
  Project file. Lists dependencies. <PackageReference Include="..." />
         |
         v
  +-------------------+
  | packages.lock.json|
  +-------------------+
  Lock file (opt-in).
```

.NET is refreshingly simple — one CLI (`dotnet`), one registry (nuget.org), one project format (`.csproj`). The older `nuget.exe` CLI still exists but `dotnet` handles it all now.

### Other Ecosystems (Quick Reference)

| Language | Manager | Registry | Project File | Lock File |
|----------|---------|----------|-------------|-----------|
| **Rust** | cargo | crates.io | Cargo.toml | Cargo.lock |
| **Go** | go mod | proxy.golang.org | go.mod | go.sum |
| **Ruby** | gem / bundler | rubygems.org | Gemfile | Gemfile.lock |
| **PHP** | composer | packagist.org | composer.json | composer.lock |
| **Java** | maven | Maven Central | pom.xml | - |
| **Java** | gradle | Maven Central | build.gradle | gradle.lockfile |
| **Swift** | SPM | GitHub/custom | Package.swift | Package.resolved |
| **Dart** | pub | pub.dev | pubspec.yaml | pubspec.lock |

---

## Layer 3: Meta / Cross-Language Managers

Some tools span multiple languages or manage environments rather than packages.

```
+----------------------------------------------------------------+
|                     META LAYER                                 |
|                                                                |
|  CONTAINERS        VERSION MGR       MONOREPO        TASK      |
|  ----------        -----------       --------        ------    |
|  docker            asdf              nx              make      |
|  podman            mise (rtx)        turborepo       just      |
|  nix               pyenv             lerna           task      |
|                    nvm               pnpm workspaces           |
|                    fnm                                         |
|                    volta                                       |
+----------------------------------------------------------------+
```

### Version Managers — "Which Python/Node do I use?"

These don't install packages — they install **different versions of runtimes**.

```
  Problem: Project A needs Node 18, Project B needs Node 22.

  Solution: Version managers.

  For Node.js:
  +-------+     +---------+     +--------+
  |  nvm  | or  |  volta  | or  |  fnm   |
  +-------+     +---------+     +--------+
       |
       v
  Switches which `node` is on your PATH
  based on the project you're in.

  For Python:
  +--------+     +-------+
  | pyenv  | or  |  uv   |
  +--------+     +-------+
       |
       v
  Switches which `python` is on your PATH.
```

### Docker / Containers — "Ship the whole environment"

```
  Without Docker:                    With Docker:
  +-----------+                      +-------------------+
  | Your code |                      | Container         |
  | + deps    |                      | +---------------+ |
  | depend on |                      | | OS (Ubuntu)   | |
  | YOUR OS   |  -- "works on my    | | Python 3.12   | |
  | YOUR Python    machine" -->      | | pip packages  | |
  | YOUR Node  |                     | | Node 22       | |
  +-----------+                      | | npm packages  | |
                                     | | Your code     | |
                                     | +---------------+ |
                                     +-------------------+
                                     Ships EVERYTHING.
```

Docker doesn't replace pip/npm — it **wraps them**. Inside a Dockerfile you still run `pip install` and `npm install`.

---

## How They All Nest Together

This is the key mental model. Here's a real example of what happens when you set up a Python web project on Windows:

```
LAYER 0: Operating System
  Windows 11
     |
     |  winget install Python.Python.3.12
     v
LAYER 1: System Package Manager installs Runtime
  Python 3.12 is now on PATH
     |
     |  python -m venv .venv
     v
LAYER 2a: Virtual Environment (isolates this project)
  .venv/ created
     |
     |  pip install django
     v
LAYER 2b: Language Package Manager installs Libraries
  django + its dependencies in .venv/lib/
     |
     |  django depends on sqlparse, asgiref
     v
LAYER 3: Transitive Dependencies (automatic)
  pip resolves the full dependency tree
```

And here's a Node.js + Python project (common in web dev):

```
choco install nodejs python         <-- System layer
     |
     +---> node + npm on PATH
     +---> python + pip on PATH
              |
              +---> npm install      <-- Node packages (frontend)
              |     package.json
              |     node_modules/
              |       react/
              |       webpack/
              |
              +---> pip install      <-- Python packages (backend)
                    requirements.txt
                    .venv/
                      django/
                      celery/
```

---

## Concept Glossary

### Registry vs Manager vs Lock File

```
  REGISTRY            MANAGER             LOCK FILE
  (the store)         (the shopper)       (the receipt)
  --------            --------            ----------
  npmjs.com           npm                 package-lock.json
  PyPI                pip                 (none by default!)
  nuget.org           dotnet              packages.lock.json
  crates.io           cargo               Cargo.lock

  Holds all the       Resolves versions,  Records EXACT versions
  published           downloads, installs installed. Ensures
  packages.           into your project.  reproducible builds.
```

### Dependencies vs DevDependencies vs Peer Dependencies (Node.js)

```
  dependencies        Your app NEEDS these to run.
                      npm install express
                      Ships to production.

  devDependencies     Only needed during development.
                      npm install --save-dev jest
                      Testing, linting, building.

  peerDependencies    "I expect the HOST project to provide this."
                      Used by plugins/libraries.
                      e.g., a React component expects React to exist.
```

### Global vs Local Install

```
  GLOBAL                              LOCAL (per-project)
  ------                              -------------------
  npm install -g typescript           npm install typescript
  pip install black                   pip install black (in venv)

  Goes in a system-wide location.     Goes in node_modules/ or .venv/
  Available everywhere.               Available only in this project.
  Version conflicts across projects.  Each project has its own version.

  Rule of thumb:
  - CLI tools you use everywhere -> global (typescript, black, eslint)
  - Libraries your code imports  -> local (react, django, numpy)
```

---

## Common Confusion Points

### "I installed Python with choco but pip doesn't work"

```
  choco install python    <-- installs Python runtime
  refreshenv              <-- reload PATH (or restart terminal)
  python -m pip install   <-- NOW pip works
```

Choco installs the runtime. The language PM (pip) comes bundled with it. You may need to refresh your shell.

### "npm vs npx — what's the difference?"

```
  npm install typescript     Installs the package into node_modules/
  npx tsc                    RUNS a package (downloads temporarily if needed)

  npm = install and manage
  npx = run without permanently installing
```

### "pip install vs conda install — can I mix them?"

```
  conda creates its own environment with its own Python.
  pip installs into whatever Python is active.

  Mixing them INSIDE a conda environment can break things.

  Safe pattern:
    conda install numpy scipy     <-- conda-native packages first
    pip install some-rare-thing   <-- pip only for what conda lacks
```

### "dotnet add package vs nuget install — which one?"

```
  dotnet add package Newtonsoft.Json   <-- Modern. Use this.
  nuget install Newtonsoft.Json        <-- Old CLI. Downloads but
                                           doesn't add to project.
```

Always use `dotnet add package` for .NET projects.

---

## Your Windows Setup (Practical Map)

Based on a typical dev setup on Windows:

```
+-----------------------------------------------------------+
|  SYSTEM LAYER (pick one or two)                           |
|                                                           |
|  choco / winget / scoop                                   |
|  Install: python, nodejs, dotnet-sdk, rust, git, vscode   |
+-----------------------------------------------------------+
         |              |              |
         v              v              v
  +-----------+  +-----------+  +-----------+
  | Python    |  | Node.js   |  | .NET SDK  |
  | 3.12      |  | 22 LTS    |  | 9.0       |
  +-----------+  +-----------+  +-----------+
  | pip / uv  |  | npm /pnpm |  | dotnet    |
  | venv      |  |           |  |           |
  +-----------+  +-----------+  +-----------+
  | django    |  | react     |  | EF Core   |
  | numpy     |  | express   |  | ASP.NET   |
  | pandas    |  | vite      |  | xunit     |
  +-----------+  +-----------+  +-----------+
```

---

## Decision Cheat Sheet

| I want to... | Use |
|---|---|
| Install Python/Node/.NET on Windows | `winget` or `choco` |
| Install a CLI tool I use everywhere | System PM (`choco install ripgrep`) |
| Add a Python library to my project | `pip install` (in a venv) or `uv add` |
| Add a JS library to my project | `npm install` or `pnpm add` |
| Add a .NET library to my project | `dotnet add package` |
| Run different Node versions per project | `nvm`, `fnm`, or `volta` |
| Run different Python versions per project | `pyenv` or `uv` |
| Ship my whole environment reproducibly | Docker |
| Manage a monorepo with many packages | `pnpm workspaces`, `nx`, or `turborepo` |
