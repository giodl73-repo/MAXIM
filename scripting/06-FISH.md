# Scripting: Fish

> Friendly Interactive SHell — breaks POSIX intentionally to achieve discoverability and consistency. Your interactive shell; not for scripts others will run.

## The Shell Landscape

```
Shell Space: POSIX Compatibility vs Interactive UX Quality

  High  │
  Inter-│                              ╔══════════════╗
  active│                              ║     Fish     ║  <- designed for humans
  UX    │                              ║  autosugg.   ║     not for /bin/sh compat
        │               ┌─────────────╫──────────────╫──┐
        │               │    Zsh      ╚══════════════╝  │
        │               │  (+ Oh My   Zsh is mid-POSIX, │
        │               │    Zsh)     high UX w/plugins  │
        │               └─────────────────────────────-─┘
        │    ┌──────────────────┐
        │    │      Bash        │
        │    │   ubiquitous;    │
        │    │   POSIX-close;   │
        │    │   UX: workable   │
        │    └──────────────────┘
  Low   │  ┌──────┐
  Inter-│  │  sh  │  <- POSIX reference; minimal; CI/container default
  active│  └──────┘
  UX    │
        └──────────────────────────────────────────────────────
             Low POSIX compat            High POSIX compat

  Practical read:
    Fish  = best daily-driver terminal; worst script portability
    Zsh   = good balance; POSIX-compatible enough; extensible
    Bash  = universal automation; fine interactively; not exciting
    sh    = /bin/sh in containers, CI, Makefiles; zero extras

  Decision axis:
    "Will a human type in this shell daily?" → Fish wins
    "Will a machine run this script?"        → Bash/sh wins
```

---

## When to Choose Fish

Fish is an interactive shell designed to serve the human at the keyboard. It is not a scripting language for automation. The choice is orthogonal to your OS or stack.

```
Decision tree for any developer:

  ┌─────────────────────────────────────────┐
  │ Is this your daily interactive terminal?│
  └────────────────┬────────────────────────┘
                   │
           YES ────┤
                   ▼
          ┌─────────────────────────────────────────────┐
          │ Fish gives you: autosuggestions from history │
          │ syntax highlighting as you type              │
          │ tab completion auto-generated from man pages │
          │ web config UI (fish_config)                  │
          │ consistent syntax (no POSIX legacy quirks)   │
          └────────────────────┬────────────────────────┘
                               │
                     Do you need Zsh?
                               │
           YES if: you already have heavy Zsh config,
                   you need POSIX-compatible scripting
                   inline with interactive use,
                   or team standardizes on Zsh.
                               │
           NO if:  starting fresh; don't script in
                   your interactive shell; want the
                   best UX out of the box.

  NO ─────┤
          ▼
    CI/CD scripts, Dockerfiles, Makefiles, cron jobs:
    → Use bash or sh. Fish may not be installed.
      Even if Fish is installed, don't shebang #!/usr/bin/fish
      for scripts others will run.
```

**Zsh vs Fish directly:** Zsh with Oh My Zsh approaches Fish's UX — but requires plugin configuration. Fish gives you the same capability out of the box. If you want to think about your terminal as a product that "just works," Fish is cleaner. If you want POSIX script compatibility in your interactive shell, Zsh is the call.

---

## Language Snapshot

| Attribute | Value |
|-----------|-------|
| Platform | macOS, Linux, Windows (WSL) |
| Extension | `.fish` |
| Shebang | `#!/usr/bin/env fish` |
| Paradigm | Interactive-first; scripting with non-POSIX syntax |
| Typing | Strings (all values); no separate numeric type |
| Execution | Interpreted; no POSIX compatibility |

---

## The Fish Philosophy

```
Design choices in Fish:
  ┌──────────────────────────────────────────────────────────────┐
  │ 1. Discoverability: tab-complete everything, syntax highlight │
  │    while typing, man page auto-generated from functions       │
  │ 2. No legacy cruft: drop POSIX quirks that cause confusion   │
  │    (no set -e, no word-splitting, no $'...' ANSI)            │
  │ 3. Consistent syntax: one way to do each thing               │
  │    (set for all vars; if/else/end everywhere)                 │
  │                                                               │
  │ Cost: scripts written for Fish don't run in Bash/sh          │
  │       CI/CD can't run Fish scripts directly (no /bin/fish)   │
  └──────────────────────────────────────────────────────────────┘
```

---

## POSIX Incompatibility: The Boundary You Must Internalize

Fish's syntax is a clean break from POSIX — not a superset, not compatible. This has practical consequences beyond "syntax is different."

```
Things that silently break when you run them in Fish or source them from Fish:

  .env files:
    POSIX:  export DATABASE_URL=postgres://...    # works in bash
    Fish:   export DATABASE_URL=postgres://...    # FAILS — not Fish syntax

  Makefiles that shell out:
    make uses /bin/sh by default — runs POSIX sh, not Fish
    Your Fish config (aliases, functions, $PATH changes) is NOT visible to make

  CI/CD steps:
    GitHub Actions, GitLab CI, Azure Pipelines — all default to bash or sh
    A .fish script uploaded as a CI step will fail unless the runner has Fish installed
    and the step explicitly invokes fish script.fish

  Source-ing shell configs:
    source ~/.bashrc              # FAILS in Fish — bash syntax inside
    source .env                   # FAILS — export syntax
    # Correct in Fish:
    set -x DATABASE_URL "postgres://..."   # set individual vars
    # Or: use 'bass' plugin to evaluate bash expressions inside Fish
```

**The rule:** Fish is your keyboard interface. The moment automation or portability enters the picture, write bash. The two don't mix without a compatibility shim.

**Common POSIX idioms and their Fish equivalents:**

| POSIX / Bash | Fish equivalent |
|---|---|
| `export VAR=value` | `set -gx VAR value` |
| `source file.sh` | `source file.fish` (only works on Fish files) |
| `if [ condition ]` | `if test condition` |
| `$(command)` | `(command)` |
| `$?` | `$status` |
| `$@` / `$*` | `$argv` |
| `export -f funcname` | Functions don't export across processes in Fish |

---

## Syntax Reference Card

### Variables

```fish
# set is the ONLY way to assign variables
set name hello                      # assign (no $ on LHS, no = !)
set name "hello world"              # string with spaces

# Scopes
set -l name value                   # local (to current function/block)
set -g name value                   # global (process-wide)
set -x name value                   # export to environment (like export)
set -U name value                   # universal (persists across ALL sessions!)

# Expand
echo $name                          # expand
echo "$name"                        # quoting doesn't change expansion in fish
echo (string length $name)          # use string builtin for operations

# Unset
set -e name                         # erase variable
set -el name                        # erase local
set -eg name                        # erase global

# Test if set
set -q name                         # exit 0 if set, 1 if not
if set -q name; echo "set"; end

# Read-only
set -r name value                   # read-only (Fish 3.6+)

# Special variables
$PATH                               # colon-joined; Fish also shows as array $PATH[1], $PATH[2]
$HOME  $USER  $TERM  $SHELL
$status                             # exit code of last command (NOT $?)
$argv                               # script/function arguments (NOT $@ or $*)
$__fish_config_dir                  # ~/.config/fish
$__fish_data_dir                    # fish data dir
```

---

## Universal Variables: Fish's Persistent Store

`set -U` is Fish's most architecturally distinct feature. It has no equivalent in bash or zsh.

```
Variable scope comparison across shells:

  Shell / scope    Survives current    Survives new      Survives
                   command             terminal window   reboot
  ──────────────────────────────────────────────────────────────
  Bash env var     YES (exported)      NO                NO
  Zsh env var      YES (exported)      NO                NO
  Fish global (-g) YES (in session)    NO                NO
  Fish export (-x) YES (exported)      NO                NO
  Fish universal   YES                 YES               YES  ← unique
  (-U)
```

**Storage:** `~/.local/share/fish/fish_variables` — a plain text file Fish manages.

**How it works:**

```fish
set -U EDITOR nvim               # Set once. Persists across all terminals, reboots.
set -U my_project_root /src/myapp

# In a new terminal, tomorrow:
echo $EDITOR                     # → nvim   (no .bashrc equivalent needed)

# Universal vars are shared across ALL open Fish sessions simultaneously.
# Change it in one terminal → immediately visible in all others.
set -U THEME dark
# → terminal A, B, C all see THEME=dark without restart
```

**When to use each scope:**

| Scope | Flag | Use for |
|---|---|---|
| Local | `-l` | Temp var inside a function |
| Global | `-g` | Session-duration state; cleared on shell exit |
| Exported | `-x` | Passing env vars to child processes |
| Universal | `-U` | Personal config (EDITOR, GOPATH, etc.) — replaces ~/.bashrc exports |

**Universal variables replace** the pattern of adding `export EDITOR=nvim` to `~/.bashrc`. You set it once with `set -U`, and it's there forever across all sessions. Fish's `~/.config/fish/config.fish` therefore tends to be much shorter than a typical `.bashrc`.

---

### String Quoting

```fish
# Single quotes: literal (same as POSIX)
echo 'no $expansion here'

# Double quotes: variable expansion only
set name world
echo "hello $name"                  # → hello world
echo "result: (math 1+2)"          # → result: (math 1+2)  — NOT expanded!
echo "result: $(math 1+2)"          # → also not expanded in fish
echo "result: "(math 1+2)           # CORRECT: concatenate string + command sub

# No special $'...' ANSI-C quoting in Fish
# Use: printf '\t' or \t in echo with -e (but echo -e isn't reliable)
# Use: echo -e '\t' works in fish but not portable

# String manipulation via string builtin
string length "hello"               # → 5
string upper "hello"                # → HELLO
string lower "HELLO"                # → hello
string sub -s 1 -l 3 "hello"        # → hel (1-indexed! start=1, length=3)
string replace "l" "L" "hello"      # → heLlo (first only)
string replace -a "l" "L" "hello"   # → heLLo (all)
string match -r '\d+' "abc123"      # regex match → 123
string split / /usr/local/bin       # → usr local bin
string split0 ... | ...             # null-byte split for binary safety
string join ", " one two three      # → one, two, three
string trim "  hello  "             # → hello
string pad -r -w 10 "hi"            # → hi        (right-pad)
string escape "it's a 'test'"       # shell-escape
string unescape ...
```

### Arrays

```fish
# Fish arrays: space-separated in set, 1-INDEXED (like Zsh)
set fruits apple banana cherry

echo $fruits                        # → apple banana cherry
echo $fruits[1]                     # → apple (1-indexed!)
echo $fruits[2]                     # → banana
echo $fruits[-1]                    # → cherry (last)
echo $fruits[1 3]                   # → apple cherry (multiple indices)
echo $fruits[1..2]                  # → apple banana (range)

count $fruits                       # → 3 (length)
echo (count $fruits)                # count as expression

# Append
set fruits $fruits grape            # rebuild with new element
set -a fruits grape                 # append (fish 3.0+)

# Delete
set -e fruits[2]                    # erase index 2

# Iterate
for fruit in $fruits
    echo $fruit
end

# Slice
echo $fruits[2..]                   # from index 2 to end
echo $fruits[..2]                   # from start to index 2

# Check membership
contains banana $fruits && echo "has banana"
```

### Arithmetic

```fish
# math builtin (supports float, no $(( )))
math 2 + 3                          # → 5
math "2 * 3 + 4"                    # → 10 (quotes prevent shell interpretation)
math 10 / 3                         # → 3.333333... (float by default!)
math -s 0 10 / 3                    # → 3 (0 decimal places = integer)
math "2 ^ 10"                       # → 1024 (exponent with ^, not **)
math "1.5 * 2.5"                    # → 3.75
math sin\(0\)                       # → 0 (trig functions available)
math "floor(3.7)"                   # → 3

# Store result
set result (math 2 + 3)

# Comparison in conditions — use math or test
if test (math "2 + 2") -eq 4; echo "yes"; end
if math "2 + 2 == 4" > /dev/null; echo "yes"; end  # math returns 0/1 exit code for bool
```

### Conditionals

```fish
# if/else/end (NOT fi — end terminates all blocks in Fish)
if test "$x" = "hello"
    echo match
else if test $x -gt 5
    echo greater
else
    echo other
end

# test is the condition command (POSIX test / [ ])
test -f file.txt                    # file exists
test -d dir                         # directory
test -z "$var"                      # empty string
test -n "$var"                      # non-empty
test "$a" = "$b"                    # string equality

# string match for pattern testing
if string match -q "hello" $var; echo "matched"; end
if string match -qr '^\d+$' $var; echo "all digits"; end   # regex

# Command exit code
if grep -q "pattern" file.txt
    echo "found"
end

# NOT — use not keyword
if not test -f file.txt
    echo "missing"
end

# Compound conditions
if test -f file -a -r file          # POSIX -a (AND)
    echo "readable file"
end
# Or: chain with ; and / ; or (Fish 2.x) or && / || (Fish 3.0+)
if test -f file && test -r file
    echo "readable file"
end
```

### switch/case

```fish
switch $var
    case "hello"
        echo "got hello"
    case "foo" "bar"               # multiple patterns on one case
        echo "foo or bar"
    case "*.txt"                   # glob pattern
        echo "a text file"
    case '*'                       # default (no quotes needed, but OK)
        echo "other"
end
```

### Loops

```fish
# for-in
for item in apple banana cherry
    echo $item
end

# for-in array
for item in $array
    echo $item                     # no quoting issue — fish doesn't word-split
end

# for-in command output
for line in (cat file.txt)         # command substitution with ()
    echo $line
end

# while
while test $count -lt 10
    echo $count
    set count (math $count + 1)
end

# break / continue
for x in $items
    if test "$x" = "skip"; continue; end
    if test "$x" = "stop"; break; end
    process $x
end

# Sequence
for i in (seq 1 10)
    echo $i
end
for i in (seq 1 2 20)              # seq start step end
    echo $i
end
```

### Functions

```fish
# Define
function greet
    echo "Hello, $argv[1]!"
end

# With --argument-names
function greet --argument-names name greeting
    echo "$greeting, $name!"
end

# With description (shows in help)
function greet --description "Greet someone"
    echo "Hello, $argv[1]!"
end

# With on-event (event handler)
function on_exit --on-event fish_exit
    echo "goodbye!"
end

# Local variable
function my_func
    set -l x "local value"          # -l = local scope
    echo $x
end

# Return value: via exit code (true/false) or echo for capture
function is_even
    if math "$argv[1] % 2 == 0" > /dev/null
        return 0                    # true
    else
        return 1                    # false
    end
end

function get_value
    echo "the value"               # caller captures with ()
end
set result (get_value)

# Persist a function to disk
funcsave greet                      # saves to ~/.config/fish/functions/greet.fish

# List functions
functions                           # all functions
functions greet                     # show source of greet
functions --erase greet             # delete
```

---

## Function Autoloading

Fish autoloads functions by filename — the same pattern as Ruby autoload, Node module resolution, and Python's `__init__.py` conventions. This is how Fish's entire standard library works.

```
~/.config/fish/functions/
├── greet.fish          ← defines function greet
├── mkcd.fish           ← defines function mkcd
├── fish_prompt.fish    ← defines your prompt (special name)
└── fish_greeting.fish  ← defines startup greeting (special name)

When you type: mkcd /tmp/test
Fish sees:     "mkcd" is not a builtin or known function
Fish searches: ~/.config/fish/functions/mkcd.fish
Fish sources:  the file (defines the function)
Fish calls:    mkcd /tmp/test
```

**How to use this in practice:**

```fish
# Create a new function file
funced mkcd                         # opens $EDITOR for mkcd function
funcsave mkcd                       # saves to ~/.config/fish/functions/mkcd.fish

# Or write directly
# ~/.config/fish/functions/mkcd.fish:
function mkcd --description "mkdir and cd into it"
    mkdir -p $argv[1] && cd $argv[1]
end

# Now 'mkcd' is available in all Fish sessions, instantly.
# No 'source', no 'export', no restart needed.
```

**Startup files (always sourced, not autoloaded):**

```
~/.config/fish/config.fish          ← runs on every Fish startup (like .bashrc)
~/.config/fish/conf.d/*.fish        ← sourced alphabetically at startup
~/.config/fish/functions/*.fish     ← autoloaded on demand (not at startup)
```

The autoload model means Fish sessions start fast — function files are parsed only when called. For large personal toolkits with dozens of functions, this matters.

---

### I/O & Redirection

```fish
echo "stdout"
echo "stderr" >&2
read -l var                         # read one line from stdin (-l = local)
read -l -P "Enter: " var            # with prompt

# Same redirection as bash
cmd > file      cmd >> file         # stdout
cmd 2> file     cmd 2>&1           # stderr
cmd > /dev/null 2>&1                # discard all
echo "input" | cmd                  # pipe

# Command substitution with () (not $() like bash)
set size (wc -l < file.txt)
echo "Lines: $size"

# No here-doc in Fish — use: printf, string, or pipe
printf '%s\n' "line one" "line two" | cmd
echo "
line one
line two
" | cmd
```

### Exit Codes & Error Handling

```fish
# $status (NOT $? like bash)
some_command
echo $status                        # 0 = success, non-0 = error

# Check in condition
if some_command
    echo "succeeded"
end

if not some_command
    echo "failed"
end

# No set -e in Fish
# Fish propagates errors through $status; use if/not to handle
some_command; or exit 1             # ; or syntax (Fish 2)
some_command || exit 1              # || (Fish 3+)
some_command && next_command        # &&

# exit
exit 0
exit 1
exit $status                        # propagate

# No try/catch — Fish error handling is command-centric
```

### Arguments

```fish
# $argv is the argument list (1-indexed array)
$argv[1]                            # first arg
$argv[2]                            # second
$argv[-1]                           # last
count $argv                         # number of args

# Function args
function my_func
    set -l first $argv[1]
    set -l rest $argv[2..]          # slice: all but first
    for arg in $argv; echo $arg; end
end

# No getopts — use argparse (Fish 2.7+)
function my_cmd
    argparse 'n/name=' 'v/verbose' -- $argv
    or return 1
    # _flag_name (from --name), _flag_verbose (from --verbose)
    if set -q _flag_verbose; echo "verbose mode"; end
    echo "name: $_flag_name"
end
my_cmd --name Alice --verbose
my_cmd -n Alice -v
```

---

## What Makes Fish Distinct

- **Autosuggestions**: gray completions from history as you type (right arrow to accept)
- **Syntax highlighting**: live coloring as you type (red = unknown command)
- **Tab completion from man pages**: `fish_update_completions` auto-generates from man pages
- **`fish_config`**: web-based configuration UI (`fish_config` opens browser)
- **Universal variables**: `set -U` persists across ALL terminals and sessions
- **No `export` needed**: `set -x` = exported; universal vars auto-available everywhere
- **`abbreviations`**: `abbr --add gc 'git commit'` expands inline (unlike aliases — you see the expanded form in history)
- **`funced`** + `funcsave`: edit and persist functions interactively

---

## Abbreviations vs Aliases vs Functions

Three mechanisms for shortening commands. They behave differently in ways that matter for shell hygiene.

```
Execution model comparison:

  abbr (abbreviation):
    You type:   gc
    Fish sees:  gc<space> or gc<enter>
    Fish does:  inline text expansion → "git commit" in the command line
    History:    "git commit" (the expansion, not "gc")
    Sharing:    If someone sees your history, they see the real command

  alias:
    You type:   gc
    Fish does:  calls a function named gc, which calls "git commit"
    History:    "gc" (the alias name — opaque)
    Sharing:    Someone reading your history sees "gc" — no context

  function:
    You type:   mkcd /tmp/test
    Fish does:  runs function body
    History:    "mkcd /tmp/test"
    Use for:    multi-line logic, argument handling, anything beyond simple aliasing
```

**Side-by-side comparison:**

| | `abbr` | `alias` | `function` |
|---|---|---|---|
| Expansion | Inline text | Function call | Function call |
| History shows | Expanded form | Alias name | Function name + args |
| Multi-line logic | No | No | Yes |
| Arguments (`$argv`) | No (static text) | No (simple wrapper) | Yes |
| Persisted with | `abbr --add` (auto-saved) | `funcsave` | `funcsave` |
| Interactive benefit | High (readable history) | Low | N/A |
| Best for | Git shortcuts, common commands | Compatibility shims | Real tooling |

**Fish's preference is abbreviations for interactive shortcuts.** The reason: your shell history is a debugging artifact. When something goes wrong and you look back at your history, `git commit -m "wip"` tells you what happened. `gc` does not.

```fish
# Adding abbreviations
abbr --add gc 'git commit'
abbr --add gca 'git commit -a'
abbr --add gp 'git push'
abbr --add ll 'ls -la'

# List all abbreviations
abbr --list

# Remove
abbr --erase gc

# Abbreviations persist automatically — no funcsave needed
# Stored in universal variable fish_user_abbreviations
```

---

## Plugin Managers: Fisher and Oh My Fish

Fish's ecosystem is managed through one of two plugin managers. Every modern interactive shell has this layer — Fish is no different.

```
Plugin ecosystem:

  ┌────────────────────────────────────────────────────────┐
  │                    Fisher (recommended)                 │
  │  - Pure Fish implementation (no dependencies)          │
  │  - Install: curl -sL git.io/fisher | source && ...     │
  │  - Usage: fisher install <github-user/repo>            │
  │  - Stores plugins in: ~/.config/fish/functions/ etc.   │
  │  - Lightweight; plugins are just Fish functions        │
  └────────────────────────────────────────────────────────┘

  ┌────────────────────────────────────────────────────────┐
  │                 Oh My Fish (OMF) — older               │
  │  - Heavier framework; more opinionated structure       │
  │  - Install: curl ... | fish                            │
  │  - Usage: omf install <plugin>                         │
  │  - Larger plugin registry (but overlap with Fisher)    │
  │  - Less actively maintained                            │
  └────────────────────────────────────────────────────────┘

  Recommendation: Fisher for new setups.
```

**Fisher quickstart:**

```fish
# Install Fisher
curl -sL https://raw.githubusercontent.com/jorgebucaran/fisher/main/functions/fisher.fish | source && fisher install jorgebucaran/fisher

# Install plugins
fisher install jorgebucaran/autopair.fish      # auto-close brackets/quotes
fisher install PatrickF1/fzf.fish              # fzf for Ctrl-R, Ctrl-T, Ctrl-Alt-F
fisher install jethrokuan/z                    # smart directory jumping (z proj)
fisher install edc/bass                        # run bash utilities (source .env, etc.)
fisher install jorgebucaran/nvm.fish           # nvm without bash dependency

# Prompt themes
fisher install IlanCosman/tide@v6              # tide: configurable powerline-style prompt
fisher install pure-fish/pure                  # pure: minimal async prompt

# Manage
fisher list                                    # installed plugins
fisher update                                  # update all
fisher remove jethrokuan/z                     # uninstall
```

**Plugins worth knowing:**

| Plugin | What it does |
|---|---|
| `PatrickF1/fzf.fish` | Fuzzy file/history/directory search — replaces Ctrl-R with fzf |
| `jethrokuan/z` | `z projectname` jumps to most-visited matching dir |
| `edc/bass` | Lets you run bash scripts inside Fish: `bass source .env` |
| `jorgebucaran/nvm.fish` | Node version management without bash dependency |
| `jorgebucaran/autopair.fish` | Auto-closes `(`, `[`, `"` as you type |
| `IlanCosman/tide` | Prompt: shows git status, node version, last command time, etc. |

**`bass` deserves special mention** — it's the bridge between Fish's clean world and the bash-centric tooling ecosystem. When you need to `source .env` or run a bash-based SDK setup script from within Fish, `bass` executes it in bash and imports the resulting environment changes into Fish.

---

## Ecosystem

| Tool | Purpose |
|------|---------|
| Fisher | Plugin manager (`fisher install jorgebucaran/autopair.fish`) |
| Oh My Fish (OMF) | Alternative plugin manager (older) |
| `fzf.fish` | fzf integration for Ctrl-R, Ctrl-T |
| `z` / `zoxide` | Smart directory jumping (`z proj`) |
| `tide` / `pure` | Prompt themes |
| `fish_config` | Built-in web UI for themes/functions |
| `fish_update_completions` | Regenerate completions from man pages |
| `functions/` | `~/.config/fish/functions/*.fish` — auto-loaded |
| `conf.d/` | `~/.config/fish/conf.d/*.fish` — sourced at startup |

---

## Gotchas & Traps

| Trap | Issue | Fix |
|------|-------|-----|
| `$?` doesn't exist | Fish uses `$status` | Use `$status` or `if cmd; ...` |
| No `export` | `export VAR=val` is not native | `set -gx VAR val` or `set -x VAR val` |
| `set var=value` | Wrong: creates var named "var=value" | `set var value` (no = !) |
| `()` vs `$()` | Command sub is `(cmd)` not `$(cmd)` | Fish: `set x (cmd)` |
| No POSIX compat | Bash scripts don't run in Fish | Don't `source` bash scripts in Fish |
| No `&&` / `||` (Fish <3.0) | Old Fish used `; and` / `; or` | Update to Fish 3.0+ |
| `if/else/end` not `fi` | Shell muscle memory | `end` terminates all blocks |
| Universal vars persist | `set -U x 1` persists forever | Clean up with `set -eU x` |
| No `~/.fishrc` | Config is `~/.config/fish/config.fish` | XDG convention |
| Word-split in `()` | `for x in (cmd)` splits on whitespace | Fish has no workaround (use file or null-sep) |

---

## Common Confusion Points

These are conceptual mismatches — not syntax errors, but mental model collisions that send you to the wrong diagnosis.

**"I can just source my .bashrc in Fish"**
No. Fish syntax is incompatible with bash. `source ~/.bashrc` will fail or produce garbage. Fish's config model is different: use `set -U` for persistent vars (no `.bashrc` equivalent needed), and `~/.config/fish/config.fish` for startup logic. Use the `bass` plugin if you need to evaluate bash environment setup.

**"Fish scripts will work in CI"**
No. CI runners (GitHub Actions, GitLab CI, Azure Pipelines) default to bash or sh. Even if you write valid Fish scripts, the runner won't have Fish unless you explicitly install it. Keep CI scripts in bash.

**"Universal variables are like .env files"**
Not quite. `.env` files are text files you source into a shell session — they're per-invocation and scoped to that session. Universal variables are Fish's own persistent store, shared across all Fish sessions simultaneously. They're closer to user preferences (like `EDITOR`, `GOPATH`) than to project-scoped configuration. Don't use universal variables for project secrets — use `.env` files sourced with `bass source .env`.

**"abbr is just a faster alias"**
The distinction matters for history readability. `abbr` expands to the full command in the command line before execution — your history shows `git commit -m "fix bug"`. `alias` is a function wrapper — your history shows `gc`. For daily interactive use, abbreviations give you transparent, searchable shell history.

**"I need to restart Fish to pick up config changes"**
Usually not. New functions saved with `funcsave` are available immediately in all open Fish sessions (autoloaded on demand). Universal variable changes (`set -U`) are visible across all open terminals instantly. The only thing that requires a restart is changing `config.fish` or `conf.d/` files — but even then, `exec fish` replaces the current session cleanly.

**"Fish's `if` needs [ ] like bash"**
No. `if [ condition ]` is POSIX. In Fish, `if` takes a command and checks its exit code. The equivalent of `[ -f file ]` is `test -f file`. Fish does support `[ ]` syntax because `[` is a command, but Fish's own idiom is `test`.

---

## Decision Cheat Sheet

| Use Fish when... | Don't use Fish when... |
|-----------------|----------------------|
| Your interactive terminal shell | CI/CD scripts (no /bin/fish guaranteed) |
| Developer UX: autosuggestions, completions | Scripts others will run |
| macOS or Linux daily driver | POSIX compatibility required |
| Personal automation scripts | Docker/container scripts |
| Want web config UI (`fish_config`) | Team uses bash |
