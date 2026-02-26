# Scripting Languages — Taxonomy & Landscape

---

## 0. Object Pipeline → Text Stream: The Fundamental Shift

The single most disorienting aspect of moving from PowerShell (or NuShell, or any object-pipeline shell) to Bash/Zsh/Fish is not the syntax — it is the pipeline model. Everything else follows from this.

```
OBJECT PIPELINE vs TEXT STREAM — THE CORE MENTAL MODEL
═══════════════════════════════════════════════════════════════════════════════

Object Pipeline (PowerShell, NuShell)
─────────────────────────────────────
  Get-Process | Where-Object { $_.CPU -gt 100 } | Select-Object Name, CPU
       │                    │                           │
   returns                 receives                 receives
   [Process[]]          [Process]               [Process]
   (.NET objects)       access .CPU              access .Name, .CPU
                        (typed property)         (typed properties)

  ┌──────────────────────────────────────────────────────┐
  │  Objects flow through pipes. Properties are typed.   │
  │  No parsing. No delimiter assumptions. No ambiguity. │
  └──────────────────────────────────────────────────────┘

Text Stream (Bash, Zsh, Fish, sh)
──────────────────────────────────
  ps aux | awk '$3 > 10 { print $1, $3 }' | sort -k2 -rn
     │           │                               │
  prints       receives text,               receives text,
  lines of     splits on whitespace,        sorts as text
  text         compares column 3            by column 2

  ┌──────────────────────────────────────────────────────┐
  │  Strings flow through pipes. Everything is text.     │
  │  You parse structure out of strings at each stage.   │
  │  Field position, delimiter, quoting — all manual.    │
  └──────────────────────────────────────────────────────┘

The consequence:
  - PS:   pipeline stages NEVER need to parse — they query properties
  - Bash: pipeline stages ALWAYS need to parse — grep/awk/cut/sed are parsers
  - PS:   structured data is first-class (objects, hashtables)
  - Bash: structured data is emergent (you impose structure via tools)
```

### Concept-Level Bridge: Object Shell → Text Shell

This mapping holds for any typed/object pipeline shell moving to a text stream shell — PowerShell is just the most common instance.

| Concept | Object Shell (PS) | Text Stream Shell (Bash/Zsh) | Notes |
|---------|-------------------|------------------------------|-------|
| Pipeline unit | .NET object | newline-delimited string | Fundamental difference |
| Property access | `$_.PropertyName` | `awk '{print $3}'` or `cut -f3 -d,` | Parse out of text |
| Filtering | `Where-Object { $_.Size -gt 100 }` | `awk '$3 > 100'` or `grep` | Text needs positional logic |
| Sorting | `Sort-Object -Property CPU -Descending` | `sort -k3 -rn` | Column position in text |
| Formatting | `Select-Object Name, CPU \| Format-Table` | `column -t` or `printf` | No intrinsic structure |
| Error channel | Separate error stream (`$ErrorActionPreference`) | stderr (fd 2) / `$?` | Both use separate channels |
| Exit status | `$LASTEXITCODE` (external) / `$?` (cmdlet, bool) | `$?` (integer, 0=success) | PS `$?` is bool, not int |
| Null sink | `Out-Null` or `> $null` | `> /dev/null` | Discard pipeline output |
| Startup profile | `$PROFILE` | `~/.bashrc` / `~/.bash_profile` | Interactive-only by default |
| Script security gate | `ExecutionPolicy` (RemoteSigned, Bypass) | `chmod +x` + shebang | Unix: file permission model |
| Structured data | Hashtables, PSCustomObject, .NET types | jq (JSON), awk (CSV), python | No native structured types |
| Error on failure | `$ErrorActionPreference = "Stop"` | `set -euo pipefail` | Both "strict mode" patterns |
| Print to stderr | `Write-Error "msg"` | `echo "msg" >&2` | Redirect to fd 2 |
| Print without pipeline | `Write-Host "msg"` (terminal-only) | `echo "msg" >&2` (idiom) | Neither goes into pipeline |
| Capture output | `$x = Get-Thing` | `x=$(cmd)` | Subshell in bash captures stdout |
| Time a command | `Measure-Command { Get-Process }` | `time cmd` | |
| PATH variable | `$env:PATH` | `$PATH` | env: namespace in PS |
| Temp variables | `$env:TMPDIR` / `$env:TEMP` | `$TMPDIR` / `/tmp` | |
| Env vars | `$env:FOO = "bar"` | `export FOO=bar` | PS scopes to process |

### The Quoting Shift

Both shells have quoting rules, but the mechanics differ:

```
PowerShell quoting:
  'literal — no $expansion'          → single = literal always
  "interpolates $var and $($expr)"   → double = interpolates
  ` (backtick)                       → escape character (NOT backslash)
  @' ... '@                          → here-string (literal)
  @" ... "@                          → here-string (interpolating)

Bash quoting:
  'no $expansion whatsoever'         → single = literal always (same)
  "$var expands, \n escapes"         → double = interpolates (same idea)
  \ (backslash)                      → escape character (different from PS backtick)
  <<EOF                              → heredoc (interpolating by default)
  <<'EOF'                            → heredoc (literal, like @' '@)
  $'tab\there\nnewline'             → ANSI-C quoting (bash-only, no PS equiv)

The trap: PS uses backtick as escape; Bash uses backslash.
  PS:    Write-Host "column1`tcolumn2"     # tab
  Bash:  echo -e "column1\tcolumn2"        # tab (echo -e or printf)
  Both:  printf "column1\tcolumn2\n"       # portable (printf is both PS and Unix)
```

## 1. The Landscape

```
SCRIPTING LANGUAGE GENEALOGY
═══════════════════════════════════════════════════════════════════════════════

Branch 1 — Windows scripting lineage
─────────────────────────────────────
  COMMAND.COM / CMD.EXE
  (1981 DOS)
       │
       ├─→  AUTOEXEC.BAT, batch files (.bat)
       │    (simple sequential scripts, no real control flow until DOS 6)
       │
       ├─→  Windows Scripting Host (1996)
       │        ├─→ VBScript (.vbs)  — COM automation, IE scripting
       │        └─→ JScript (.js)    — JS-like, COM automation
       │
       └─→  PowerShell 1.0 (2006, Monad)
                ├── .NET Framework CLR, compiled to CIL
                ├── Object pipeline (not text streams — revolutionary departure)
                ├── verb-noun cmdlet naming
                ├── PowerShell 2.0–5.1 (Windows-only, .NET Framework)
                └─→  PowerShell 7+ (2019, .NET Core / .NET 5+)
                         ├── Cross-platform (Windows / macOS / Linux)
                         ├── Open source (GitHub: PowerShell/PowerShell)
                         └── pwsh binary (distinct from Windows powershell.exe)

Branch 2 — Unix/POSIX shell lineage
─────────────────────────────────────
  Thompson shell — /bin/sh (1971, Ken Thompson, V1 Unix)
       │  Basic I/O redirection, pipes, sequential execution
       │
       ├─→  Bourne sh (1979, Steve Bourne, Unix V7)
       │        ├── Variables, control flow, functions
       │        ├── The definitive POSIX ancestor
       │        └─→  POSIX.1 sh standard (1988, IEEE Std 1003.1)
       │                   ↓ spec, not implementation
       │
       ├─→  C shell / csh (1978, Bill Joy, BSD)
       │        ├── C-like syntax (if/foreach/while)
       │        ├── History expansion (!!)
       │        ├── Job control
       │        └─→  tcsh (1981) — extended csh (still used on BSDs)
       │
       ├─→  Korn shell / ksh (1983, David Korn, AT&T)
       │        ├── Superset of Bourne sh
       │        ├── Associative arrays, arithmetic (( ))
       │        └─→  ksh93, mksh (MirOS ksh, used on Android)
       │
       ├─→  Bash — Bourne Again SHell (1989, Brian Fox, GNU Project)
       │        ├── POSIX superset + bash extensions
       │        ├── [[ ]] test construct, arrays, process substitution
       │        ├── Default shell: macOS <10.15, most Linux distros
       │        └── macOS 10.15+: zsh default (Apple GPL avoidance)
       │
       ├─→  Zsh — Z Shell (1990, Paul Falstad)
       │        ├── POSIX + Bash extensions + additional power
       │        ├── Spelling correction, glob qualifiers, themes
       │        ├── Oh My Zsh ecosystem (2009)
       │        └── macOS 10.15+ default shell
       │
       └─→  Fish — Friendly Interactive SHell (2005, Axel Liljencrantz)
                ├── NOT POSIX compatible (intentional design choice)
                ├── Autosuggestions, syntax highlighting built-in
                ├── Simpler variable model (set name value, no $( ) quoting hell)
                └── Scripting works but rarely used for portability

Branch 3 — Text-processing DSLs
─────────────────────────────────────
  ed — line editor (1971, Ken Thompson / Dennis Ritchie)
  (address + command model; the grandfather of regex-based editing)
       │
       ├─→  sed — stream editor (1974, Lee McMahon, Bell Labs)
       │        ├── Single-pass, line-oriented
       │        ├── Compiled per-invocation to simple state machine
       │        ├── Address ranges, substitution, deletion, branching
       │        └── POSIX standard; GNU sed adds extensions
       │
       ├─→  AWK (1977, Aho / Weinberger / Kernighan, Bell Labs)
       │        ├── Pattern-action model: /regex/ { action }
       │        ├── Automatic record splitting (FS, OFS, RS, NR, NF)
       │        ├── Built-in arithmetic, associative arrays, printf
       │        ├── Compiled per-invocation (like a micro-compiler)
       │        └── gawk (GNU AWK), mawk (fast), nawk (new AWK = original)
       │
       └─→  Perl (1987, Larry Wall)
                ├── "Practical Extraction and Report Language"
                ├── Superset of AWK + sed + sh concepts
                ├── Full language: OOP, refs, closures, modules (CPAN)
                ├── Compiled to bytecode, interpreted by perlc
                ├── Sigil-based scalar/array/hash distinction
                └── The dominant text/sysadmin language before Python

Branch 4 — Scripting-capable general-purpose (context only; not covered here)
──────────────────────────────────────────────────────────────────────────────
  Python (1991) — replaced Perl as "glue language" of choice
  Ruby (1995)   — elegant OOP scripting; Chef/Puppet infra tooling
  Lua (1993)    — embeddable, tiny runtime; Neovim config, game scripting
  Node.js (2009)— JavaScript as scripting; common in CI/npm scripts
```

---

## 2. Three-Category Taxonomy

```
SCRIPTING CATEGORY TAXONOMY
═══════════════════════════════════════════════════════════════════════════════

┌─────────────────────────────────────────────────────────────────────────────┐
│  INTERACTIVE SHELLS                                                         │
│  Designed for human use (REPL), also script-first capable                   │
│  Bash ● Zsh ● Fish ● PowerShell                                             │
└─────────────────────────────────────────────────────────────────────────────┘
         ▲ readline/libedit integration, history, tab-complete, prompts

┌─────────────────────────────────────────────────────────────────────────────┐
│  SCRIPT-FIRST                                                               │
│  Automation-oriented; not designed for interactive use                      │
│  Batch/CMD ● sh (POSIX) ● Perl                                              │
└─────────────────────────────────────────────────────────────────────────────┘
         ▲ No fancy prompt, minimal interactive editing, designed to be invoked

┌─────────────────────────────────────────────────────────────────────────────┐
│  TEXT-PROCESSING DSLs                                                       │
│  Pipeline-oriented; pattern-action or stream-transformation model           │
│  sed ● AWK                                                                  │
└─────────────────────────────────────────────────────────────────────────────┘
         ▲ Always invoked via shell pipeline; not interactive shells at all
```

| Language   | Category         | Portability              | Typing Model                  | Primary Paradigm              |
|------------|------------------|--------------------------|-------------------------------|-------------------------------|
| Batch/CMD  | Script-first     | Windows only             | Untyped (string-everything)   | Imperative, GOTO-based        |
| PowerShell | Interactive/Auto | Win native; cross (pwsh) | Dynamic, .NET type system     | Object pipeline + imperative  |
| Bash       | Interactive shell| POSIX superset; ubiquitous | Untyped (string + integer)  | Imperative, pipeline          |
| sh (POSIX) | Script-first     | Universal POSIX           | Untyped (string only)         | Imperative, pipeline          |
| Zsh        | Interactive shell| POSIX + extensions        | Untyped (string + float)      | Imperative, pipeline          |
| Fish       | Interactive shell| Non-POSIX; install-only   | Untyped (string + list)       | Imperative, pipeline          |
| AWK        | Text DSL         | POSIX; universal          | Dual (string/number by context)| Pattern-action, record model |
| sed        | Text DSL         | POSIX; universal          | Untyped (line strings)        | Pattern-address, stream       |
| Perl       | Script-first     | Universal (CPAN)          | Dynamic, context-dependent    | Multi-paradigm (OOP/FP/proc)  |

---

## 3. Execution Model Comparison

```
EXECUTION MODELS
═══════════════════════════════════════════════════════════════════════════════

Batch / CMD
─────────────────────────────────────────────────────────────────────────────
  script.bat ──→ cmd.exe ──→ direct interpretation, line by line
                              No shebang (cmd.exe is hardcoded)
                              No subprocess isolation — runs in current cmd
                              CALL launches child cmd.exe
                              Windows registry file association: .bat/.cmd → cmd.exe
  Execution: purely interpreted, no bytecode, no JIT
  Environment: %ERRORLEVEL%, %PATH%, %COMSPEC%

PowerShell
─────────────────────────────────────────────────────────────────────────────
  script.ps1 ──→ pwsh.exe ──→ lexer → parser → AST → compiled to CIL
                                                       ↓
                                                 .NET CLR (JIT to native)
  Pipeline: NOT text streams
            ┌─────────┐     ┌─────────┐     ┌─────────┐
            │ Cmdlet  │ ──→ │ .NET    │ ──→ │ Cmdlet  │
            │ outputs │     │ objects │     │ receives│
            └─────────┘     └─────────┘     └─────────┘
  ExecutionPolicy: security gate before script runs (Bypass, RemoteSigned, etc.)
  Profiles: $PROFILE loaded on interactive start (~/.bashrc equivalent)

Bash / sh / Zsh
─────────────────────────────────────────────────────────────────────────────
  ./script.sh ──→ kernel exec() reads shebang ──→ /bin/bash
                                                    ↓
                                             line-by-line interpretation
                                             (parsing + execution interleaved)
  Pipeline: text streams
            ┌─────────┐     ┌──────┐     ┌─────────┐
            │ cmd A   │ ──→ │ pipe │ ──→ │ cmd B   │
            │ stdout  │     │(fd)  │     │ stdin   │
            └─────────┘     └──────┘     └─────────┘
  subprocess: fork() + exec() for each external command
  builtins: cd, echo, test, [ ] executed without fork
  Execution: interpreted; some shells compile to internal bytecode (zsh, ksh)
  Env vars: exported vars (export FOO) visible to child processes only

Fish
─────────────────────────────────────────────────────────────────────────────
  ./script.fish ──→ fish interpreter ──→ AST-based evaluation
  Universal variables: persist across sessions (stored in ~/.config/fish/)
  Universal env: set -U FOO bar (no equivalent in Bash/sh)
  NOT fork-based for builtins; different scoping rules
  Autoloads functions from ~/.config/fish/functions/name.fish

AWK
─────────────────────────────────────────────────────────────────────────────
  awk 'program' file ──→ awk compiler ──→ internal bytecode ──→ execution
                          (per-invocation, like a micro-compiler)
  Record model:
            ┌─────────────────────────────────────────────┐
            │  Input stream                               │
            │  ┌─────────────────────┐                   │
            │  │ Record (RS-delimited│ → $0 (whole record)│
            │  │ default: newline)   │ → $1 $2 $3...      │
            │  └─────────────────────┘   (FS-delimited)   │
            └─────────────────────────────────────────────┘
  Pattern-action: /regex/ { action }   ← matches per record
                  BEGIN  { action }   ← before first record
                  END    { action }   ← after last record

sed
─────────────────────────────────────────────────────────────────────────────
  sed 'script' file ──→ compiled to state machine ──→ line-by-line execution
  Address + command model:
            address  command
            3        d          ← delete line 3
            /regex/  s/a/b/g    ← substitute on matching lines
            1,10     p          ← print lines 1–10
  Hold space (h/H/g/G/x) = the one "register" available

Perl
─────────────────────────────────────────────────────────────────────────────
  perl script.pl ──→ perl compiler ──→ op-tree (bytecode) ──→ interpreter
                      (full compilation before execution; syntax errors caught upfront)
  Optional JIT: B::C, Inline::C, or experimental Perl JIT backends
  One-liner mode: perl -e 'code'
                  perl -p -e 'code' ← per-line sed-like (prints each line)
                  perl -n -e 'code' ← per-line, no auto-print
                  perl -i -e 'code' ← in-place edit (like sed -i)
  Context system: scalar context vs list context — not a type system,
                  a runtime dispatch mechanism (explained in section 6)
```

---

## 4. Platform Matrix

| Language   | Windows native | WSL         | macOS native    | Linux native | Docker/CI default |
|------------|---------------|-------------|-----------------|--------------|-------------------|
| Batch/CMD  | Yes (built-in) | No          | No              | No           | No (Windows containers only) |
| PowerShell 5.1 | Yes (built-in) | No      | No              | No           | No                |
| PowerShell 7+  | Install    | Yes         | Install (brew)  | Install      | Yes (mcr.microsoft.com/powershell) |
| Bash       | No (git-bash is shim) | Yes | Yes (<10.15 default) | Yes (most distros) | **Yes — ubiquitous** |
| sh (POSIX) | No           | Yes (/bin/sh) | Yes (/bin/sh → dash/bash) | Yes (dash or bash) | **Yes — universal** |
| Zsh        | No           | Install     | **Yes (10.15+ default)** | Install | Install required |
| Fish       | No           | Install     | Install (brew)  | Install      | Install required |
| AWK        | Git Bash only | Yes (gawk) | Yes (gawk/awk)  | Yes (gawk)   | **Yes — in base images** |
| sed        | Git Bash only | Yes        | Yes (BSD sed ≠ GNU sed) | Yes (GNU sed) | **Yes — in base images** |
| Perl       | Strawberry Perl | Yes       | Yes (system perl) | Yes (usually) | Most images |

**Key:**
- "Windows native" = runs without WSL or extra installs on stock Windows
- Docker/CI default = present in ubuntu:latest, debian:slim, alpine (note: alpine uses busybox ash)
- **Bold** = can safely assume present in CI runners without explicit install

**macOS Gotcha:** macOS ships BSD versions of sed and AWK, which differ from GNU versions.
`sed -i ''` on macOS vs `sed -i` on Linux. Use `gsed` / `gawk` (brew) for GNU compat.

---

## 5. POSIX Compliance Spectrum

```
POSIX COMPLIANCE SPECTRUM
═══════════════════════════════════════════════════════════════════════════════

 Strict POSIX ◄─────────────────────────────────────────────────────► Non-POSIX

 /bin/sh      bash          zsh          ksh93       Perl        Fish   Batch  PowerShell
 (dash/ash)   (superset)    (mostly)     (mostly)    (own world)
     │             │            │             │           │          │      │       │
     │             │            │             │           │          │      │       │
  IEEE Std      POSIX +      POSIX +      POSIX +    AWK/sed    Intentionally Windows
  1003.1        bash-isms    zsh-isms     ksh-isms   inspired   breaks POSIX  object
  only          (arrays,     (1-indexed   (typeset)  but not    for UX       pipeline
                [[ ]], etc)  arrays, etc) assoc arr) POSIX sh   reasons      model
```

**Why POSIX compliance matters:**

| Scenario | Recommended | Why |
|----------|-------------|-----|
| Dockerfile `RUN` scripts | `sh` or `bash` | Docker default shell is `/bin/sh` (usually dash) |
| Alpine Linux scripts | `sh` (POSIX) | Alpine uses busybox ash — not bash |
| GitHub Actions `run:` | `bash` (default) | Explicitly `shell: bash` to be safe |
| Portable across Linux distros | `sh` (POSIX) only | Can't assume bash version or arrays |
| `/etc/init.d/` scripts | `sh` | SysV init uses `/bin/sh` |
| Interactive dev machine | Whatever you want | Portability irrelevant for personal config |

**The `#!/bin/sh` trap:** On macOS, `/bin/sh` is bash in POSIX-compat mode. On Debian/Ubuntu, `/bin/sh` is dash (a fast, minimal POSIX-only shell). On Alpine, it's busybox ash. Code that works on macOS with `#!/bin/sh` may fail on Alpine.

### shellcheck — Static Analysis for Shell Scripts

`shellcheck` is the standard linter for `bash`/`sh` scripts. Think of it as the ESLint or Roslyn analyzer for shell: it catches POSIX violations, quoting bugs, deprecated patterns, and portability hazards before runtime.

```bash
# Install
brew install shellcheck          # macOS
apt-get install shellcheck       # Debian/Ubuntu
# Or in CI: https://github.com/koalaman/shellcheck

# Basic usage
shellcheck script.sh             # check with inferred dialect (from shebang)
shellcheck -s sh script.sh       # enforce POSIX sh compliance
shellcheck -s bash script.sh     # check as bash
shellcheck -s dash script.sh     # check against dash (Alpine default)

# In CI (GitHub Actions)
- run: shellcheck **/*.sh
  shell: bash
```

**What shellcheck catches:**

| Category | Example bug | shellcheck message |
|----------|-------------|-------------------|
| Unquoted expansion | `for f in $list` | SC2068: quote $list to prevent word splitting |
| POSIX violation | `[[ $a == $b ]]` with `#!/bin/sh` | SC2039: [[ ]] is bash, not sh |
| Deprecated syntax | `\`cmd\`` (backtick) | SC2006: use $() instead |
| Array misuse | `"${arr[@]}"` in sh context | SC2039: arrays not in POSIX sh |
| Missing quotes | `if [ $a = $b ]` | SC2086: double-quote $a |
| Bad shebang | `#!/bin/bash` on non-bash system | SC1008: shebang variation note |
| Unused variables | `local x=5` (never read) | SC2034: x appears unused |
| `set -e` edge cases | `if bad_cmd; then` | notes where -e won't trigger |

**CI integration pattern:**

```yaml
# GitHub Actions: enforce sh compliance on Docker scripts
- name: Lint shell scripts
  run: |
    shellcheck -s sh Dockerfile.scripts/*.sh    # enforce POSIX for Alpine compat
    shellcheck -s bash ci/**/*.sh               # bash lint for CI scripts
```

`shellcheck` is the difference between "it works on my Mac" and "it works in your Alpine container". For anyone shipping Dockerfiles or GitHub Actions, run it.

---

## 6. Binding & Type Theory Note

All shell scripting languages are **dynamically typed** — types resolved at runtime — but the mechanisms differ significantly.

```
TYPE / BINDING MODELS ACROSS SCRIPTING LANGUAGES
═══════════════════════════════════════════════════════════════════════════════

Language     Type model              Binding time     Analogy
─────────────────────────────────────────────────────────────────────────────
Bash/sh/Zsh  Strings + integers      Runtime          Untyped lambda calculus
             (everything is a string; arithmetic coerces)
             declare -i x: weak type annotation (still a string internally)

Fish         Strings + lists         Runtime          Similar to Bash; cleaner
             (all vars are strings; arrays are first-class, not string hacks)

AWK          Dual: string ↔ number   Context-dependent  Like eval() in JS
             Same cell: if used in arithmetic context → number
                        if used in string context → string
             "007" + 0 → 7 (numeric)
             "007" "" → "007" (string)
             This is NOT a type system; it's a coercion-dispatch system.
             Comparable to untyped λ-calculus with semantic coercion functions.

Perl         Scalar context /        Context-dispatch  More complex than AWK
             List context            at runtime        "context polymorphism"
             $x = @array;           ← scalar context: count of array
             @x = @array;           ← list context: copy of array
             Sigils ($, @, %) are NOT types; they're access-mode indicators.
             $foo[0] vs @foo[0..2] vs %foo{key} — same underlying structure,
             different access mode (context dispatch, not type dispatch)

PowerShell   .NET types at runtime   Runtime (late     Dynamic but richer
             [string], [int], [bool] binding) with     than bash
             Optional type          optional early     $x = [int]"42" ← parse
             annotations            annotation         Get-Member shows types

Batch/CMD    Everything is a string  Runtime           Pure untyped
             SET /A is the only arithmetic mode; even then stored as string
```

**Connection to CS theory:**

All of these are **late-binding interpreters** — name resolution and dispatch happen at runtime. Compare to the compilation/JIT tiers you saw in `computing/22-COMPILERS.md`:

```
JIT TIER COMPARISON (from 22-COMPILERS.md)
                                        ┌──────────────────────────────────┐
Bash line: name=value                   │ No compilation; eval at runtime  │
           echo "$name"                 └──────────────────────────────────┘
                    ↓ equivalent tier:  V8 Ignition (bytecode interpreter)

PowerShell: pwsh compiles to CIL        ┌──────────────────────────────────┐
            .NET CLR JITs to native     │ Like V8 Maglev/Turbofan on hot   │
                                        │ paths — but not adaptive, always  │
                                        └──────────────────────────────────┘

AWK/sed: compiled per-invocation        ┌──────────────────────────────────┐
         to internal bytecode           │ Like tsc/esbuild ahead-of-time;  │
                                        │ entire program compiled before    │
                                        │ first record processed            │
                                        └──────────────────────────────────┘

Perl: full compile to op-tree           ┌──────────────────────────────────┐
      before execution starts           │ Like Java javac → bytecode;      │
                                        │ syntax errors caught upfront      │
                                        └──────────────────────────────────┘
```

**`set -euo pipefail` is not a type system.** It's rudimentary error propagation:
- `-e`: exit on any non-zero exit code (like C's `assert(rc == 0)` everywhere)
- `-u`: unbound variable reference = error (like nullable warnings in C#, but at runtime)
- `-o pipefail`: pipe failure propagates (pipe exit code = rightmost non-zero)

This gives you some of the safety of strict typing but only at the coarsest granularity (exit codes), not at the value level.

### Perl's Context System — A Formal Look

Perl's scalar/list context duality is the single most disorienting feature for any programmer coming from a statically typed language. The surface confusion is syntax ("why does the same variable give different answers?"). The deep issue is that Perl implements **context-directed dispatch** — a mechanism with no direct analog in C#, Java, Go, or Rust.

```
PERL CONTEXT DISPATCH — FORMAL MODEL
═══════════════════════════════════════════════════════════════════════════════

Standard type dispatch (C#, Go, Rust):
  The TYPE of the VALUE determines which operation runs.
  int x = 5;   // x's type determines what + means

Perl context dispatch:
  The CONTEXT OF THE CALL SITE determines how a value is evaluated.
  The expression itself doesn't change — the caller's expectation does.

  my @arr = (1, 2, 3);

  Scalar context (caller wants one thing):
    my $n = @arr;          → 3      (count of elements)
    if (@arr)              → true   (truthy if non-empty)
    print "len=" . @arr;  → "len=3" (stringifies to count)

  List context (caller wants a list):
    my @copy = @arr;       → (1, 2, 3)   (all elements)
    my ($a, $b) = @arr;    → $a=1, $b=2  (destructuring)
    push @other, @arr;     → appends all three elements
```

**The formal model:** Perl's context propagates *downward* through the expression tree. The left-hand side of an assignment determines the context in which the right-hand side is evaluated. A scalar variable (`$x = ...`) imposes scalar context. An array variable (`@x = ...`) imposes list context.

```perl
# Context flows from the assignment target downward

$x  = localtime();     # scalar context → "Wed Feb 25 14:00:00 2026"
@x  = localtime();     # list context   → (0, 0, 14, 25, 1, 126, 3, 55, 0)
                       #                   sec min hr  mday mon  yr  wday yday isdst

# Identical call; completely different return value
# localtime() inspects its calling context and returns accordingly
```

**The type-theoretic framing:** This is runtime-resolved *overloading on calling context*, not on argument type. The closest analogy in a statically typed language is a C# method that checks whether its caller is in an `IEnumerable` vs scalar context — except Perl does this at runtime, pervasively, for all expressions. Haskell's `Read` type class is the closest structural analog: `read "42" :: Int` vs `read "42" :: Double` — the type annotation at the call site determines what `read` returns. Perl's context system is the same mechanism made implicit and runtime-resolved.

```perl
# Sigils ($, @, %) are NOT types — they are access-mode indicators
# The SAME underlying data accessed with different sigils:

my @arr = (1, 2, 3);
$arr[0]     # scalar access: element 0          → 1
@arr[0..1]  # list slice: elements 0 and 1      → (1, 2)
@arr        # list context: whole array          → (1, 2, 3)
scalar @arr # forced scalar context: count       → 3

my %hash = (a => 1, b => 2);
$hash{a}    # scalar access: value at key 'a'   → 1
@hash{qw(a b)}  # hash slice: values at a, b   → (1, 2)
%hash       # list context: key-value pairs     → ('a',1,'b',2)
scalar %hash    # hash statistics string (or bool in Perl 5.26+)

# The sigil change ($arr vs @arr vs %hash) indicates HOW you're accessing,
# not what type it is. This is the parser telling Perl which context to use.
```

**Why this matters in practice:**

```perl
# Classic bugs from context confusion:

# Bug 1: wantarray — functions can detect their own context
sub flexible {
    if (wantarray()) { return (1, 2, 3) }  # list context
    else             { return "single" }    # scalar context
}
my @list = flexible();    # → (1, 2, 3)
my $val  = flexible();    # → "single"

# Bug 2: grep and map impose list context
my @found = grep { /pattern/ } @arr;    # @found = matching elements
my $count = grep { /pattern/ } @arr;    # $count = NUMBER of matches  ← scalar context!

# Bug 3: printf/print impose list context on args
printf "%d\n", @arr;    # WRONG: prints element count (1 arg in scalar context)
printf "%d\n", $arr[0]; # RIGHT: prints first element

# Bug 4: sort returns list; in scalar context, undefined behavior pre-5.36
my @sorted = sort @arr;   # correct
my $sorted = sort @arr;   # undefined/warned in modern Perl — don't do this
```

**Quick rule of thumb:** When debugging unexpected Perl behavior, ask "what context is this expression in?" before anything else. Most Perl surprises reduce to "the context wasn't what I expected."

---

## 7. Decision Tree

```
WHICH SCRIPTING APPROACH?
═══════════════════════════════════════════════════════════════════════════════

Start
  │
  ▼
Must run on Windows without WSL?
  ├─ YES ──→ Complex logic / object manipulation?
  │           ├─ YES ──→ PowerShell (pwsh 7 or Windows PowerShell)
  │           └─ NO  ──→ Batch (only if legacy environment forces it)
  │                       └── If you have a choice: PowerShell anyway
  │
  └─ NO ──→ Must be portable across any Linux/Docker/CI?
             ├─ YES ──→ Alpine or minimal containers?
             │           ├─ YES ──→ sh (POSIX) — safest bet
             │           └─ NO  ──→ bash (GitHub Actions default; ubuntu base images)
             │
             └─ NO ──→ Developer workstation only?
                         ├─ YES ──→ Interactive experience priority?
                         │           ├─ YES ──→ Zsh (macOS default; Oh My Zsh ecosystem)
                         │           │          Fish (if you want truly modern UX + non-POSIX)
                         │           └─ NO  ──→ Bash (most compatible, widely documented)
                         │
                         └─ NO ──→ What's the data shape?
                                     │
                                     ├─ Structured text / CSV / TSV / logs?
                                     │   ├─ Simple field extraction / aggregation ──→ AWK
                                     │   └─ Complex transforms + CPAN libs     ──→ Perl
                                     │
                                     ├─ In-place file editing (find/replace)?
                                     │   ├─ Simple patterns       ──→ sed
                                     │   └─ Complex patterns      ──→ Perl -i
                                     │
                                     ├─ Complex OOP / modules / web scraping?
                                     │   └── Python or Perl (CPAN)
                                     │
                                     └─ Piped one-liners in shell?
                                         ├─ Field-based (columns, CSV) ──→ AWK one-liner
                                         ├─ Line-based (substitute)    ──→ sed one-liner
                                         └─ Arbitrary parsing          ──→ perl -pe / -ne
```

**Quick lookup:**

| If you need...                        | Use         |
|---------------------------------------|-------------|
| Windows automation + .NET objects     | PowerShell  |
| Docker / Alpine / CI portability      | sh (POSIX)  |
| Linux CI scripts (ubuntu images)      | Bash        |
| Best interactive shell, macOS         | Zsh         |
| Best interactive shell, opinionated   | Fish        |
| Extract columns from CSV/TSV/logs     | AWK         |
| In-place file substitution            | sed / perl -i |
| Complex text parsing + CPAN ecosystem | Perl        |
| Legacy Windows systems / .bat files   | Batch (CMD) |

---

## 8. Common Confusion Points

**`bash` ≠ `sh`**
Bash is a superset of POSIX sh. Scripts with `#!/bin/sh` must use only POSIX features — no `[[ ]]`, no arrays, no `$(( ))` with bash extensions. On Ubuntu/Debian, `/bin/sh` is dash (not bash). Bash-only code under `#!/bin/sh` will fail silently or with subtle errors.

**Fish is NOT Bash-compatible**
You cannot source a Bash script in Fish. You cannot run Bash-style `FOO=bar cmd`. Fish uses `set FOO bar`, not `FOO=bar`. If a tool says "add this to your .bashrc", the Fish equivalent is different and usually goes in `~/.config/fish/config.fish` or a function file.

**PowerShell `$?` vs `$LASTEXITCODE` — two different things**
- `$?` = `$true`/`$false` — success/failure of the last *PowerShell* cmdlet
- `$LASTEXITCODE` = integer exit code of the last *external process* (like `git`, `docker`, `node`)
- Running `git status` and then checking `$?` tells you if PowerShell itself errored, not git's exit code
- For external commands: check `$LASTEXITCODE`, or use `$?` only after cmdlets

**Zsh arrays are 1-indexed; Bash arrays are 0-indexed**
```zsh
# Zsh
a=(one two three)
echo $a[1]   # → "one"  (1-indexed)

# Bash
a=(one two three)
echo ${a[0]} # → "one"  (0-indexed)
```
This is the most common trap when migrating scripts between Bash and Zsh.

**AWK and sed are not interactive shells**
They are stream processors invoked *from* a shell. They have no concept of a current working directory in the interactive sense, no job control, no environment inheritance beyond what the invoking shell provides via `-v` or the environment.

**`echo` is not portable**
- Bash `echo -e` interprets escape sequences; sh `echo -e` may print `-e` literally
- BSD `echo` (macOS) vs GNU `echo` (Linux) differ
- Use `printf` for portable formatted output across all POSIX systems

**PowerShell `Write-Host` vs `Write-Output`**
- `Write-Host` writes to the *terminal* — bypasses the pipeline, cannot be captured
- `Write-Output` (or just bareword output) goes into the pipeline
- `$x = Write-Host "hi"` → `$x` is empty; `$x = Write-Output "hi"` → `$x = "hi"`
- Analogy: `Write-Host` is like `Console.Error.Write()` (goes to screen, not stream)

**`set -e` does not make Bash safe**
Common false sense of security. `set -e` does NOT trigger on:
- Commands in `if` conditions: `if bad_cmd; then` — exit code consumed by `if`
- Commands in `&&` or `||` chains
- Subshell expressions `$(bad_cmd)`... when result is used in an assignment
Always combine `set -euo pipefail` and still test critical commands explicitly.

**Perl's `eq` vs `==`**
- `==` is numeric comparison
- `eq` is string comparison
- `"007" == 7` → true (numeric: 7 == 7)
- `"007" eq "7"` → false (string)
Opposite of most languages. Forgetting this causes subtle bugs.

**macOS BSD vs Linux GNU tools**
macOS ships with BSD-derived sed, AWK, date, etc. Key differences:
- `sed -i ''` (macOS) vs `sed -i` (Linux) for in-place edit
- `date -v +1d` (macOS BSD date) vs `date -d "+1 day"` (GNU date)
- `awk` on macOS is BWK nawk, not gawk — some gawk extensions unavailable
Use `brew install gnu-sed gawk coreutils` on macOS and alias/PATH-prefix for scripts that need GNU behavior.
