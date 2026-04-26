# Scripting: Zsh

> macOS default since Catalina (2019). The developer shell: Bash superset with better interactive UX, but 1-indexed arrays and subtle compatibility traps if you switch contexts.

---

## Shell Landscape

```
Shell Family Tree and Zsh Architecture
─────────────────────────────────────────────────────────────────────

  POSIX sh (1988) ── the standard; least common denominator
    │
    ├─── dash     /bin/sh on Ubuntu/Debian; strict POSIX; no arrays
    │
    ├─── bash     POSIX superset; CI/CD default; team scripts
    │    │
    │    └──── zsh (1990)  bash-compatible superset + interactive UX
    │               macOS default since 10.15 Catalina (2019)
    │               1-indexed arrays; native float; glob qualifiers
    │               NOT POSIX by default (SH_WORD_SPLIT off, etc.)
    │
    ├─── ksh (1983)  Korn shell; contributed many features bash/zsh absorbed
    │
    └─── fish    NOT POSIX; different syntax; great UX; no portability

Deployment contexts:
  macOS (10.15+)         → /bin/zsh   (default login + interactive shell)
  Linux (most distros)   → zsh available via package manager; not default
  WSL2 (Windows)         → zsh installable; common dev setup
  CI runners / Docker    → bash (never rely on zsh being present)

Zsh Layered Architecture:
  ┌──────────────────────────────────────────────────────────────┐
  │  Plugin Layer        Oh-My-Zsh / Prezto / Zinit / Antidote   │
  │  Prompt Layer        Starship / Powerlevel10k / pure         │
  ├──────────────────────────────────────────────────────────────┤
  │  Completion System   compinit / _arguments / zstyle           │
  │  ZLE (Line Editor)   bindkey / keymaps / custom widgets       │
  ├──────────────────────────────────────────────────────────────┤
  │  Option System       setopt / unsetopt (~250 named options)  │
  │  Module System       zmodload (compiled C modules)           │
  ├──────────────────────────────────────────────────────────────┤
  │  Zsh Binary          parameter flags, glob qualifiers, float  │
  └──────────────────────────────────────────────────────────────┘

Interactive vs scripting split:
  Interactive  → Zsh (macOS default; richer UX; plugins; completion)
  Shared scripts → Bash (CI, Docker, team automation — never assume zsh)
  Personal scripts → Either; zsh fine if you only run them locally
```

---

## Language Snapshot

| Attribute | Value |
|-----------|-------|
| Platform | macOS (default since 10.15), Linux (available), Windows (WSL) |
| Extension | `.zsh` |
| Shebang | `#!/usr/bin/env zsh` |
| Paradigm | Interactive shell + scripting; POSIX-mostly-compatible |
| Typing | Untyped strings; `typeset -i` for integer; native float in `(( ))` |
| Execution | Interpreted; fork/exec model like bash |
| Version | macOS ships 5.8.1 (stuck on GPL v2); Homebrew gives 5.9+ |

---

## When You Actually Script in Zsh

```
The honest framing:

  ┌──────────────────────────────────────────────────────────┐
  │  Interactive shell on dev machine  → Zsh (macOS default) │
  │  Scripts that others run           → Bash (portable)     │
  │  CI/CD, Docker, shared automation  → Bash                │
  │  Scripts only you run locally      → Either; zsh if pref │
  └──────────────────────────────────────────────────────────┘

Zsh is your interactive shell. Your shared scripts (CI, Docker,
team automation) should use Bash. Cross-contamination causes
subtle bugs — especially around array indexing and word splitting.

Know Zsh well so you can write your ~/.zshrc. Know Bash for
everything that runs on a server.
```

---

## Syntax Reference Card

### 1. Variables

```zsh
# Standard — same as Bash
name=hello
name="hello world"
typeset -r CONST=42        # readonly (zsh uses typeset; declare also works)
typeset -i count=0          # integer-typed
typeset -l lower_var        # auto-lowercase on assignment
typeset -u upper_var        # auto-uppercase on assignment
export VAR=value

# Expand — same as Bash
echo "$name"
echo "${name:-default}"
echo "${#name}"             # length

# Zsh extended parameter flags: ${(flags)var}
echo ${(U)name}             # uppercase expansion (without changing the variable)
echo ${(L)name}             # lowercase expansion
echo ${(C)name}             # capitalize each word
echo ${(q)name}             # shell-quoted (safe for eval)
echo ${(qq)name}            # single-quoted form
echo ${(j:,:)array}         # join array elements with comma
echo ${(s: :)str}           # split string on space into array context

# Split multiline string into array
lines=( ${(f)"$(cat file.txt)"} )   # (f) splits on newlines
print -l "${lines[@]}"              # print one per line
```

### 2. THE CRITICAL ZSH DIFFERENCE: 1-Indexed Arrays

```zsh
# Zsh arrays are 1-INDEXED (like awk, MATLAB, Lua — NOT like Bash/Python/C)
a=(one two three)
echo $a[1]         # → one   (FIRST element — index 1, not 0)
echo $a[0]         # → empty string (no element at index 0)
echo $a[-1]        # → three (last element)
echo $a[2,-1]      # → two three (slice: index 2 through last)
echo $a[2,3]       # → two three (slice: index 2 through 3)

echo ${#a}         # → 3 (length — no [@] required in zsh)
echo $#a           # → 3 (same — zsh syntax sugar)

# Bash comparison table
# ┌─────────────────┬───────────────┬───────────────┐
# │  Operation      │  Bash         │  Zsh          │
# ├─────────────────┼───────────────┼───────────────┤
# │  First element  │  ${a[0]}      │  $a[1]        │
# │  Last element   │  ${a[-1]}     │  $a[-1]       │
# │  Length         │  ${#a[@]}     │  ${#a} / $#a  │
# │  All elements   │  "${a[@]}"    │  "${a[@]}"    │
# │  Indices        │  "${!a[@]}"   │  "${(k)a[@]}" │
# └─────────────────┴───────────────┴───────────────┘
#
# This 0 vs 1 difference is the #1 Bash→Zsh porting bug.

# Iterate (zsh doesn't word-split bare array expansion)
for item in $a; do echo "$item"; done        # works — zsh respects array elements
for item in "${a[@]}"; do echo "$item"; done # also works; bash-compat form

# Array operations
a+=(four)            # append
a[2]=new             # replace element at index 2
unset 'a[2]'         # delete element (zsh re-indexes automatically — no sparse)

# Associative arrays (zsh 4+ — which means always in practice)
typeset -A h
h[name]="Alice"
h[age]=42
echo $h[name]
echo ${(k)h}         # keys
echo ${(v)h}         # values
for k v in "${(@kv)h}"; do echo "$k=$v"; done   # key-value pairs together
```

### 3. String Quoting

```zsh
# Same as Bash:
'literal — no expansion whatsoever'
"$var interpolation, $(command substitution)"
$'ANSI-C\tescapes\n'

# Zsh glob in double quotes: does NOT expand (consistent)
# Zsh-specific auto-quoting:
echo ${(q)var}    # shell-quoted: "hello world" → 'hello world'
echo ${(qq)var}   # single-quoted always
echo ${(qqqq)var} # $'...' ANSI-C form

# Here-doc — same as Bash
cat <<EOF
text with $var expansion
EOF

cat <<'EOF'
literal $var — no expansion
EOF
```

### 4. Extended Globbing

```zsh
# Zsh globbing: no shopt needed — extended glob is built-in
ls *.txt          # standard glob
ls **/*.txt       # recursive glob (zsh native; bash needs shopt -s globstar)

# Glob qualifiers: appended to glob in parentheses
ls **/*(.)        # (.) = regular files only
ls **/*(/)        # (/) = directories only
ls **/*(*)        # (*) = executables
ls **/*(@)        # (@) = symlinks
ls **/*(L0)       # (L0) = empty files (length exactly 0)
ls **/*(Lk+100)   # (Lk+100) = files larger than 100 KB
ls *(m-7)         # (m-7) = modified in last 7 days
ls *(om)          # (om) = sort by modification time (newest first)
ls *(Om)          # (Om) = sort oldest first
ls *(om[1,5])     # newest 5 files only

# Glob qualifiers table
# .   regular files      /   directories        *   executables
# @   symlinks           L0  empty files        Ln  exactly n bytes
# Lk+ > n KB            m-n  modified < n days  om  sort mod time
# ^   negate qualifier   ,   OR between quals

# Negation glob
ls ^*.txt         # everything except .txt files (with EXTENDED_GLOB setopt)
ls *~*.txt        # same: * except files matching *.txt

# zmv — bulk rename (must autoload)
autoload -U zmv
zmv '(*).txt' '$1.md'       # rename all .txt to .md; $1 = captured group
zmv -n '(*).txt' '$1.md'    # dry run: print what would happen
zmv '(**/)(*).txt' '$1$2.md'  # recursive rename preserving path

# Qualifier combinatorics
ls **/*(.)                  # regular files only
ls **/*(^.)                 # NOT regular files (^ negates qualifier)
ls **/*(/)                  # directories only
ls **/*(^/)                 # not directories
ls **/*(^./)                # neither regular files nor directories (devices, sockets, etc.)
ls **/*(.,/)                # regular files OR directories (, = OR between qualifiers)
ls **/*(*.^/)               # executables that are not directories
ls **/*(Lm+1^/)             # files larger than 1MB that are not directories

# The e: qualifier — arbitrary code evaluation per file
# $REPLY is set to each candidate filename before your code runs
# If the code returns non-zero, the file is excluded
ls *(e:'[[ -s $REPLY ]]':)          # files that are non-empty (like Lk+1 but more explicit)
ls *(e:'[[ ! -L $REPLY ]]':)        # files that are not symlinks (no -@ qualifier needed)
print -l **/*(e:'(( $+commands[$REPLY:t] ))':)  # files whose basename is a known command
# e: is the escape hatch when no built-in qualifier covers your predicate

# Glob flags (set at start of pattern, affect matching behavior)
# Must have setopt EXTENDED_GLOB active
ls (#i)*.TXT               # (#i) case-insensitive: matches .txt .TXT .Txt etc.
ls (#i)readme*             # case-insensitive prefix match
[[ "Hello" == (#i)hello ]] # (#i) in conditional too

# (#b) — enable backreference capture in glob patterns
# Captured groups go into $match array
if [[ "2024-02-15" == (#b)([0-9]##)-([0-9]##)-([0-9]##) ]]; then
    echo "year=$match[1] month=$match[2] day=$match[3]"
fi
# (#b) is the glob equivalent of regex capture groups

# (#m) — set $MATCH to the matched portion
for f in *; do
    [[ $f == (#m)*[0-9]* ]] && echo "contains number: $MATCH"
done

# (#s) and (#e) — anchor at start/end of string (like ^ and $ in regex)
[[ "hello" == (#s)hel* ]]  # anchored at start
[[ "hello" == *llo(#e) ]]  # anchored at end

# ## in patterns — one-or-more (like + in regex; * is zero-or-more)
ls [0-9]##.log              # files like 1.log, 42.log but not .log

# Glob flag summary:
# (#i)  case-insensitive matching
# (#b)  enable backreference capture → $match array
# (#m)  set $MATCH to matched substring
# (#s)  anchor at string start
# (#e)  anchor at string end
# (#l)  approximate matching (within edit distance)
```

### 5. Arithmetic

```zsh
# Integer — same as Bash
$(( 2 + 3 * 4 ))
(( x++ ))
(( x > 5 )) && echo "yes"

# ZSH SUPERPOWER: native float in (( )) — unlike Bash
echo $(( 1.5 + 2.5 ))      # → 4.0  (Bash would error or return 0)
echo $(( 10.0 / 3 ))        # → 3.3333333333333335
echo $(( sqrt(2) ))         # → 1.4142135623730951 (math functions!)
echo $(( sin(3.14159) ))    # → 2.65e-06 (trig functions)
echo $(( log(2.718281828) )) # → 1.0 (natural log)

# Declare float variable
typeset -F 2 result         # float with 2 decimal places
result=$(( 1.0 / 3.0 ))
echo $result                # → 0.33

# Float format
typeset -E 4 sci            # scientific notation, 4 significant digits
sci=$(( 12345.6789 ))
echo $sci                   # → 1.2346e+04
```

### 6. Conditionals

```zsh
# [[ ]] works the same as Bash — same operators, same file tests
if [[ "$a" == "$b" ]]; then ...   # equality
if [[ "$a" =~ ^[0-9]+$ ]]; then   # regex

# ZSH TRAP: = vs == in [[ ]]
str="hello"
[[ "$str" = h* ]]     # pattern match (both zsh and bash treat this as glob)
[[ "$str" == h* ]]    # same result — more explicit
[[ "$str" = hello ]]  # exact match — works in both
[[ "$str" == hello ]] # unambiguous equality — prefer this

# Zsh-specific condition
[[ -v varname ]]      # test if variable is set (zsh 5.3+)
                      # works without the $ sign: -v PATH, not -v $PATH

# Everything else: file tests, numeric tests — identical to Bash
[[ -f file ]]   [[ -d dir ]]   [[ -n "$str" ]]
[[ $x -gt $y ]] [[ $x -eq $y ]]
```

### 7. Completion System

Zsh's completion system is the most powerful tab-completion engine of any shell. Every serious Zsh user ends up here eventually — both to configure existing completions and to write new ones for internal tools.

```zsh
# Initialize the completion system (required in ~/.zshrc)
autoload -Uz compinit
compinit                        # loads completions; generates ~/.zcompdump cache

# ~/.zcompdump: compiled completion cache — speeds up startup
# If completions seem stale or broken, regenerate:
compinit -d ~/.zcompdump        # explicit cache file path
rm -f ~/.zcompdump && compinit  # full rebuild

# Practical: only regenerate dump once per day (common .zshrc pattern)
autoload -Uz compinit
if [[ -n ~/.zcompdump(#qN.mh+24) ]]; then
    compinit                    # regenerate if dump is > 24 hours old
else
    compinit -C                 # -C: skip security check; use cached dump
fi

# zstyle: configure completion behavior via context patterns
# Context pattern: :completion:<function>:<completer>:<command>:<argument>:<tag>
# Most useful patterns use wildcards:
zstyle ':completion:*' menu select           # arrow-key menu selection
zstyle ':completion:*' list-colors "${(s.:.)LS_COLORS}"  # colorize completions
zstyle ':completion:*' matcher-list 'm:{a-z}={A-Za-z}'   # case-insensitive
zstyle ':completion:*:descriptions' format '%F{yellow}-- %d --%f'  # group headers
zstyle ':completion:*' group-name ''         # group completions by type
zstyle ':completion:*:*:kill:*' menu yes select  # menu for kill completions
zstyle ':completion:*:*:kill:*:processes' list-colors '=(#b) #([0-9]#)*=0=01;31'

# Writing a custom completion function
# Convention: completion functions are named _commandname
# File lives somewhere on $fpath

# Simple example: complete subcommands for a tool called "mytool"
_mytool() {
    local -a subcommands
    subcommands=(
        'start:start the service'
        'stop:stop the service'
        'status:show service status'
        'config:edit configuration'
    )
    _describe 'subcommand' subcommands   # _describe: simple list with descriptions
}
compdef _mytool mytool                   # bind completion function to command

# _arguments: the full-featured option parser (handles -- flags, positionals)
_mytool_full() {
    _arguments \
        '(-v --verbose)'{-v,--verbose}'[enable verbose output]' \
        '(-o --output)'{-o,--output}'[output file]:output file:_files' \
        '--format=[output format]:format:(json yaml text)' \
        '1:subcommand:(start stop status config)' \
        '*:remaining args:_files'
}
compdef _mytool_full mytool

# _arguments spec format:
# 'spec[description]:message:action'
#   spec:    option spec (e.g., '-v', '--verbose', '(-v --verbose)--verbose')
#   message: label shown in completion menu
#   action:  completion action (_files, _directories, (a b c), _command, etc.)

# Useful completion actions:
# _files            complete filenames
# _directories      complete only directories
# _commands         complete command names
# (a b c)           complete from explicit list
# ->state           set state for state machine (for complex completions)

# Testing your completion:
# After adding to .zshrc or fpath: source ~/.zshrc; compinit
# Use _complete_debug to trace what's happening:
# bindkey '^Xh' _complete_help    # hit Ctrl-X h during completion for debug
```

### 8. ZLE — Zsh Line Editor

ZLE is Zsh's readline equivalent: the subsystem that handles keyboard input at the prompt. Most interactive shell UX lives here.

```zsh
# bindkey: bind keystrokes to widgets (actions)
# -e: emacs keymap (default)  -v: vi keymap  -a: vi command (vicmd) keymap

bindkey -e                     # use emacs keybindings (default; common on macOS)
bindkey -v                     # use vi keybindings

# Keymap model: keymaps are named sets of bindings
# main       → current default keymap (starts as emacs or viins)
# emacs      → emacs-style bindings
# viins      → vi insert mode (active when typing normally in vi mode)
# vicmd      → vi command mode (active after pressing Esc in vi mode)

# View all current bindings:
bindkey                        # list all bindings in current keymap
bindkey -M viins               # list bindings in viins keymap specifically

# Essential bindings (emacs map — most common)
# Ctrl-A   → beginning-of-line
# Ctrl-E   → end-of-line
# Ctrl-W   → backward-kill-word (delete word left of cursor)
# Alt-B    → backward-word (move cursor left one word)
# Alt-F    → forward-word (move cursor right one word)
# Ctrl-R   → history-incremental-search-backward (type to filter)
# Ctrl-P   → up-line-or-history (previous command)
# Ctrl-N   → down-line-or-history

# Rebind keys:
bindkey '^[[A' up-line-or-search    # Up arrow → search history prefix
bindkey '^[[B' down-line-or-search  # Down arrow → search history prefix
bindkey '^[^[[D' backward-word      # Alt-Left → move word left
bindkey '^[^[[C' forward-word       # Alt-Right → move word right

# Custom widgets: define a shell function, register it as a ZLE widget
my-widget() {
    BUFFER="echo hello world"   # BUFFER: current command line content
    CURSOR=${#BUFFER}           # CURSOR: position (0-indexed; move to end)
    zle redisplay               # redraw the prompt
}
zle -N my-widget                # register function as widget
bindkey '^X^H' my-widget        # bind it to Ctrl-X Ctrl-H

# Useful ZLE variables available inside widgets:
# BUFFER    → entire current command line as a string
# CURSOR    → cursor position (integer, 0 = before first char)
# LBUFFER   → text left of cursor
# RBUFFER   → text right of cursor
# KEYS      → key sequence that triggered this widget
# HISTNO    → current history entry number

# Practical widget: insert current date
insert-date() { LBUFFER+=$(date +%F); }
zle -N insert-date
bindkey '^X^D' insert-date

# fzf integration hooks into ZLE:
# Ctrl-R   → fzf-history-widget (replaces incremental search with fuzzy picker)
# Ctrl-T   → fzf-file-widget (insert file path)
# Alt-C    → fzf-cd-widget (cd to selected directory)
# These are set up by sourcing: source <(fzf --zsh)   (fzf 0.48+)
# or: source /usr/share/fzf/key-bindings.zsh
```

### 9. case, Loops, Functions

```zsh
# case — identical to Bash
case $var in
    pattern) cmd ;;
    *)       default ;;
esac

# For-in — mostly same; key difference: no word-splitting on bare arrays
for item in $array; do echo "$item"; done   # works in Zsh (not in Bash with spaces)
for item in "${array[@]}"; do ...           # bash-compat form; also works in Zsh

# Zsh-specific loop forms
repeat 5 { echo "five times" }             # no for/do/done — zsh compact syntax
for f (*.txt) { process $f }              # C-shell-style; works in Zsh
for f in **/*.txt; do process "$f"; done   # recursive glob with standard for

# While — identical to Bash
while [[ $i -lt 10 ]]; do (( i++ )); done

# Functions — identical to Bash syntax
my_func() {
    local x="$1"
    echo "$x"
    return 0
}
result=$(my_func arg)

# Autoload: define function body in a file on $fpath, load on first call
autoload -Uz my_func          # -U: no alias expansion; -z: zsh style
# File: somewhere in $fpath named "my_func" containing just the body
```

### 10. setopt — Zsh Options

```zsh
# Options that matter for scripting and interactive use
setopt HIST_IGNORE_DUPS       # don't save consecutive duplicate history entries
setopt HIST_IGNORE_ALL_DUPS   # don't save any duplicate history entries
setopt SHARE_HISTORY          # share history across all open terminals
setopt HIST_VERIFY             # show history expansion before executing
setopt AUTO_PUSHD              # cd automatically pushes to directory stack
setopt PUSHD_IGNORE_DUPS       # no duplicate dirs in pushd stack
setopt CORRECT                 # suggest correction for mistyped commands
setopt EXTENDED_GLOB           # enable #, ^, ~ glob operators
setopt NULL_GLOB               # no error if glob matches nothing (shopt nullglob)
setopt GLOB_DOTS               # include dotfiles in glob patterns
setopt NO_BEEP                 # disable bell/beep
setopt PROMPT_SUBST            # allow $(cmd) in PROMPT variable

# Print current options
setopt           # list all enabled options
unsetopt BEEP    # disable an option

# Check if option is set
[[ -o histignorealldups ]] && echo "dedup on"

# For scripts — same safety net as bash
set -euo pipefail    # works in Zsh too
# or Zsh-native:
setopt ERR_EXIT      # exit on error (= set -e)
setopt NOUNSET       # unset var = error (= set -u)
setopt PIPE_FAIL     # pipe fails on any stage failure (= set -o pipefail)
```

### 11. I/O and Redirection

```zsh
# Standard redirection — identical to Bash
cmd > file   cmd >> file   cmd < file   cmd 2>&1   cmd &> file

# print builtin — preferred over echo in Zsh
print "message"               # reliable echo; no -e portability issues
print -n "no newline"
print -l one two three        # print each argument on its own line
print -r "no \escape"         # raw: like echo with -E
print "error" >&2

# Zsh multios — write to multiple files without tee
print "log line" > file1 > file2    # Zsh writes to BOTH (Bash: only file2)
print "log" >> file1 >> file2       # append to both
cmd | tee file                      # still the portable / explicit way

# Everything else: here-doc, here-string, process substitution — same as Bash
diff <(sort file1) <(sort file2)
```

### 12. Startup Files

```
Zsh startup sequence — which file to put things in:

  Login shell (ssh, terminal login, macOS Terminal.app):
  ┌──────────────┬────────────────┬───────────────────────────────────┐
  │  /etc/zshenv │  ~/.zshenv     │  ALWAYS sourced; env vars only    │
  │  /etc/zprofile│ ~/.zprofile   │  Login shells only; after zshenv  │
  │  /etc/zshrc  │  ~/.zshrc      │  Interactive; aliases, funcs, PS1 │
  │  /etc/zlogin │  ~/.zlogin     │  Login shells only; after zshrc   │
  └──────────────┴────────────────┴───────────────────────────────────┘

  Interactive non-login (new terminal tab, tmux pane):
    /etc/zshenv → ~/.zshenv → /etc/zshrc → ~/.zshrc

  Script execution (#!/usr/bin/env zsh):
    /etc/zshenv → ~/.zshenv  ONLY (no .zshrc)

Guidelines:
  ~/.zshenv    → PATH, EDITOR, LANG, MANPATH; must be fast; no output
  ~/.zprofile  → login-only env (JAVA_HOME, rbenv init, etc.)
  ~/.zshrc     → everything interactive: prompt, aliases, completions,
                  functions, plugin manager, history settings
  ~/.zlogin    → rarely needed; runs after zshrc on login
```

---

## What Makes Zsh Distinct

```
Key differentiators from Bash:

  1. NO WORD-SPLITTING on array expansion
     Bash: for x in ${a[@]}   — word-splits; breaks on spaces
     Zsh:  for x in $a        — each element is one word; no quoting needed
     → Makes array handling more predictable

  2. 1-INDEXED ARRAYS
     Bash: ${a[0]} is first element
     Zsh:  $a[1]  is first element; $a[0] is empty
     → The one thing most likely to burn you when porting

  3. NATIVE FLOAT ARITHMETIC
     Bash: $(( 1.5 + 2.5 )) → 0 or error
     Zsh:  $(( 1.5 + 2.5 )) → 4.0
     → No need for bc/awk for simple float math

  4. EXTENDED GLOB BUILT-IN
     Bash: shopt -s globstar; shopt -s extglob
     Zsh:  ** and glob qualifiers available always
     → ls **/*(om[1,10]) just works

  5. PARAMETER FLAGS ${(flags)var}
     Zsh:  ${(U)var}, ${(q)var}, ${(j:,:)arr}, ${(s: :)str}
     Bash: external tools (tr, sed) or multi-step operations
     → String manipulation without subshell spawning

  6. PROGRAMMABLE COMPLETION
     Bash: completion scripts via complete/compgen
     Zsh:  _arguments, _files, zstyle — much richer
     → Typed argument completion, partial completion, menu selection
```

---

## Plugin Managers and .zshrc Structure

Every modern shell has a plugin ecosystem. This is Zsh's — and the choice of plugin manager has a measurable impact on terminal startup time.

```
Plugin Manager Tradeoffs
──────────────────────────────────────────────────────────────────
                     Oh-My-Zsh    Prezto      Zinit       Antidote
─────────────────────────────────────────────────────────────────
Startup time         200-500ms    80-200ms    10-50ms     20-80ms
(typical, varies)

Philosophy           batteries-   opinionated  explicit    explicit
                     included     defaults     everything  lockfile

Learning curve       low          low-medium   steep       medium

Lazy loading         no           no           yes         partial
                                               (native)

Plugin ecosystem     largest      medium       any git     any git
                     (OH-MY-ZSH)  (modules)    source      source

Best for             new users    clean setup  startup-    teams
                                              critical     (lockfile)
──────────────────────────────────────────────────────────────────
```

**Zinit lazy loading** — the main reason to use it over Oh-My-Zsh:

```zsh
# Zinit: plugins load asynchronously after prompt appears
# 'wait' = defer until after first prompt render
# 'lucid' = suppress the "Loaded plugin X" message

zinit ice wait lucid
zinit load zsh-users/zsh-autosuggestions      # loads after prompt appears

zinit ice wait lucid atinit"zicompinit"
zinit load zdharma-continuum/fast-syntax-highlighting  # load + compinit together

# Turbo mode: chain ice modifiers
zinit ice wait"1" lucid as"completion"
zinit snippet https://raw.githubusercontent.com/docker/cli/master/contrib/completion/zsh/_docker
```

**Minimal viable .zshrc skeleton** — ordered correctly:

```zsh
# ── 1. Environment (fast — no output, no external commands) ──────
export PATH="$HOME/.local/bin:$PATH"
export EDITOR=nvim
export LANG=en_US.UTF-8

# ── 2. History ───────────────────────────────────────────────────
HISTFILE="$HOME/.zsh_history"
HISTSIZE=50000
SAVEHIST=50000
setopt HIST_IGNORE_DUPS HIST_IGNORE_SPACE SHARE_HISTORY HIST_VERIFY

# ── 3. Options ───────────────────────────────────────────────────
setopt AUTO_PUSHD PUSHD_IGNORE_DUPS EXTENDED_GLOB NULL_GLOB NO_BEEP

# ── 4. Completion ────────────────────────────────────────────────
autoload -Uz compinit
# Only regenerate dump if > 24h old (avoids 100ms penalty every start)
if [[ -n ${ZDOTDIR:-~}/.zcompdump(#qN.mh+24) ]]; then
    compinit
else
    compinit -C
fi
zstyle ':completion:*' menu select
zstyle ':completion:*' matcher-list 'm:{a-z}={A-Za-z}'
zstyle ':completion:*' list-colors "${(s.:.)LS_COLORS}"

# ── 5. Key bindings ──────────────────────────────────────────────
bindkey -e                                    # emacs keybindings
bindkey '^[[A' up-line-or-search              # Up: history prefix search
bindkey '^[[B' down-line-or-search            # Down: history prefix search

# ── 6. Aliases ───────────────────────────────────────────────────
alias ls='ls --color=auto'
alias ll='ls -lh'
alias la='ls -lAh'
alias ..='cd ..'

# ── 7. Plugins (sourced last — may take time) ────────────────────
# Option A: Oh-My-Zsh (batteries included, slowest)
# source "$HOME/.oh-my-zsh/oh-my-zsh.sh"

# Option B: manual (fastest; just source what you need)
source "$HOME/.zsh/zsh-autosuggestions/zsh-autosuggestions.zsh"
source "$HOME/.zsh/fast-syntax-highlighting/fast-syntax-highlighting.plugin.zsh"

# Option C: Zinit with lazy loading (fast startup + full ecosystem)
# source "$HOME/.local/share/zinit/zinit.git/zinit.zsh"
# zinit ice wait lucid; zinit load zsh-users/zsh-autosuggestions

# ── 8. Prompt (after plugins — may depend on them) ───────────────
# Option A: Starship (cross-shell; fast; no Zsh deps)
# eval "$(starship init zsh)"

# Option B: Powerlevel10k (Zsh-only; instant prompt support)
# source "$HOME/.p10k.zsh"   # p10k configure generates this

# Option C: minimal built-in
autoload -Uz vcs_info
precmd() { vcs_info }
zstyle ':vcs_info:git:*' formats ' (%b)'
PROMPT='%F{green}%~%f${vcs_info_msg_0_}%# '

# ── 9. Tool integrations (eval is slow; put last) ────────────────
# eval "$(fzf --zsh)"         # fzf keybindings and completion
# eval "$(zoxide init zsh)"   # zoxide (smart cd)
# eval "$(rbenv init -)"      # rbenv
```

**Profiling startup time:**

```zsh
# Add to top of .zshrc:
zmodload zsh/zprof

# Add to bottom of .zshrc:
zprof

# Or: time a fresh shell start
time zsh -i -c exit
# Repeat 5x and average; anything under 100ms is good

# Find what's slow line-by-line:
zsh -xvs 2>&1 | head -100    # trace mode; shows each line as executed
```

## Ecosystem

| Tool | Purpose | Notes |
|------|---------|-------|
| Oh My Zsh | Plugin/theme framework | Most popular; slows startup if not trimmed |
| Prezto | Lighter OMZ alternative | More opinionated defaults |
| Zinit / Antidote | Fast plugin managers | Lazy-loading; measurable startup improvement |
| Starship | Cross-shell prompt | Works in Zsh, Bash, Fish, PowerShell |
| `fzf` + zsh integration | Fuzzy history/file search | Ctrl-R (history), Ctrl-T (files), Alt-C (dirs) |
| `z` / `zoxide` | Jump to frequent directories | `z proj` → `cd ~/dev/myproject` |
| `zsh-autosuggestions` | Fish-like history suggestions | Shows ghost text from history |
| `zsh-syntax-highlighting` | Live syntax coloring at prompt | Red for invalid commands |
| `zmv` | Bulk rename via glob patterns | `autoload -U zmv` |
| `zcalc` | Interactive calculator | `autoload -U zcalc`; supports float |
| `compinit` | Initialize completion system | Required in .zshrc for tab completion |

---

## Gotchas and Traps

| Trap | Issue | Fix |
|------|-------|-----|
| **1-indexed arrays** | `$a[0]` is empty; `$a[1]` is first | Always use 1-based indexing in Zsh |
| Porting Bash arrays | `${a[0]}` in Zsh = empty string, not first element | Search-replace `[0]` → `[1]` when porting |
| `=` in `[[ ]]` | `=` is pattern match, not just equality | Use `==` for unambiguous string equality |
| No word-splitting on arrays | `$a` in Zsh vs Bash behave differently | Code that works in one may not in the other |
| Startup file ordering | `.zshrc` not sourced for scripts | Use `.zshenv` for env vars needed in scripts |
| `autoload` for builtins | `zmv`, `zcalc`, `zed` not available by default | `autoload -Uz zmv zcalc` in `.zshrc` |
| Wrong shebang | `#!/bin/sh` invokes dash, not Zsh | `#!/usr/bin/env zsh` for Zsh features |
| macOS ships old Zsh | `/bin/zsh` = 5.8.1 (2020, stuck on GPL v2) | `brew install zsh` + add to `/etc/shells` + `chsh` |
| Oh My Zsh startup time | Large plugin set → slow terminal open | `zprof` to profile; use lazy loading |
| `SHARE_HISTORY` collisions | Fast typing can get wrong completions from another terminal | Expected behavior; use Ctrl-R to be precise |

---

## Bridge: Bash to Zsh

| Bash | Zsh | Notes |
|------|-----|-------|
| `${a[0]}` | `$a[1]` | First element — INDEX SHIFT |
| `${a[-1]}` | `$a[-1]` | Last element — same |
| `${#a[@]}` | `${#a}` or `$#a` | Length |
| `for x in "${a[@]}"` | `for x in "${a[@]}"` or `for x in $a` | Both work in Zsh |
| `declare -A h` | `typeset -A h` | Assoc array; both work |
| `${!h[@]}` | `${(k)h}` | Keys of assoc array |
| `${h[@]}` | `${(v)h}` | Values |
| `tr '[:upper:]' '[:lower:]'` | `${(L)var}` | Lowercase |
| `shopt -s globstar` | built-in | `**` always works in Zsh |
| `shopt -s nullglob` | `setopt NULL_GLOB` | |
| `shopt -s extglob` | `setopt EXTENDED_GLOB` | |
| `set -e` | `set -e` or `setopt ERR_EXIT` | Both work |
| `source file` | `source file` or `. file` | Both work |
| `echo -e "tab:\t"` | `print "tab:\t"` | `print` is reliable |
| `mapfile -t a < f` | `a=( ${(f)"$(< f)"} )` | Read file lines into array |
| `${str,,}` lowercase | `${(L)str}` | Parameter flag syntax |
| `${str^^}` uppercase | `${(U)str}` | |
| `BASH_REMATCH[1]` | `match[1]` | Regex capture groups |

### Portability: Zsh-isms That Silently Fail Under `#!/bin/bash`

If you're writing scripts that might run under either shell, these are the landmines. Zsh-only constructs don't generate errors in Bash — they silently produce wrong results.

```bash
# LANDMINE 1: Array indexing
# In Zsh: a[1] is the first element
# In Bash: a[1] is the SECOND element (0-indexed)
a=(one two three)
echo $a[1]             # Zsh: "one" | Bash: word-splits "$a" and appends "[1]" literally
echo ${a[1]}           # Zsh: "one" | Bash: "two" (second element)
echo ${a[0]}           # Zsh: ""    | Bash: "one" (first element)
# → Scripts that access $a[1] and expect the first element are Zsh-only

# LANDMINE 2: Glob qualifiers
ls **/*(.)             # Zsh: regular files only | Bash: literal string "**/*(.)": syntax error
ls *(om[1,5])          # Zsh: 5 newest files     | Bash: tries to run as subshell — errors
# → Any glob with (qualifiers) is Zsh-only

# LANDMINE 3: Parameter expansion flags
echo ${(U)name}        # Zsh: uppercase | Bash: syntax error
echo ${(f)"$(cat f)"}  # Zsh: split on newlines into array | Bash: syntax error
echo ${(j:,:)array}    # Zsh: join with comma | Bash: syntax error
# → ${(flags)var} is entirely Zsh-only

# LANDMINE 4: print builtin
print "hello"          # Zsh: reliable output | Bash: not a builtin; calls /usr/bin/print if exists
print -l one two three # Zsh: one per line    | Bash: error or wrong output
# → Use printf or echo in cross-shell scripts

# LANDMINE 5: Compact loop syntax
repeat 5 { echo hi }          # Zsh: valid | Bash: syntax error
for f (*.txt) { process $f }  # Zsh: valid | Bash: syntax error
# → These are Zsh-specific; use standard for/do/done

# LANDMINE 6: Bare array expansion without word splitting
a=("hello world" "foo bar")
for x in $a; do echo "$x"; done   # Zsh: two iterations | Bash: four (word-splits)
# → Bash requires "${a[@]}" to preserve elements with spaces

# SAFE ZONE — these work identically in bash and zsh:
set -euo pipefail          # both support this
[[ "$a" == "$b" ]]         # identical in both
[[ -f file && -r file ]]   # identical in both
diff <(sort f1) <(sort f2) # process substitution — both support it
cat <<'EOF'                # here-doc — identical in both
literal text
EOF
while IFS= read -r line; do   # line reading — identical in both
    echo "$line"
done < file
declare -A h               # assoc arrays: bash 4+, zsh 4+ (both common)
```

| Construct | Safe in both? | Notes |
|-----------|:---:|-------|
| `set -euo pipefail` | yes | identical behavior |
| `[[ ]]` tests | yes | same syntax and semantics |
| Process substitution `<()` | yes | both support it |
| Here-docs | yes | identical |
| `while IFS= read -r` | yes | standard line reading |
| `declare -A` / `typeset -A` | yes | both keywords work in both shells |
| `${a[0]}` first element | NO | Bash:first, Zsh:empty |
| `${(f)...}` flags | NO | Zsh-only syntax |
| Glob qualifiers `*(.)` | NO | Zsh-only |
| `print` builtin | NO | Zsh builtin; not in Bash |
| `repeat N { }` | NO | Zsh-only loop |
| `for x (list) { }` | NO | Zsh-only syntax |
| Bare `$array` in for | NO | Zsh doesn't word-split; Bash does |

## Common Confusion Points

**1. `$a[0]` returns empty string, not an error**

```zsh
a=(one two three)
echo $a[0]     # → ""  (empty — no element at index 0 in Zsh)
echo $a[1]     # → one (first element)
```

This is the most dangerous Zsh behavior for anyone coming from Bash, Python, C, or any 0-indexed language. It doesn't error — it silently returns empty. If you use `${a[0]}` in Zsh expecting the first element, your code runs without complaint and produces wrong output. The fix is mechanical: audit every `[0]` and change to `[1]` when porting from Bash.

**2. Unquoted `$array` in Zsh doesn't word-split (but the same code breaks in Bash)**

```zsh
# Zsh
a=("hello world" "foo bar")
for x in $a; do echo "$x"; done    # two iterations: "hello world", "foo bar"
# Each array element stays intact — Zsh does not word-split bare array expansion

# Bash — same code, different result
a=("hello world" "foo bar")
for x in $a; do echo "$x"; done    # four iterations: "hello", "world", "foo", "bar"
# Bash word-splits on spaces within elements
```

This means Zsh code that looks fine — and is fine in Zsh — silently produces wrong results in Bash. The portable form `"${a[@]}"` works correctly in both shells. If portability matters, always use the quoted form.

**3. `setopt` and `set -o` are different option namespaces**

```zsh
setopt HIST_IGNORE_DUPS     # Zsh-native option name (caps or lowercase, _ or no _)
set -o histignoredups       # POSIX set -o form — both work in Zsh
set -e                      # POSIX short form — equivalent to setopt ERR_EXIT

# They operate on the same underlying options via different interfaces.
# setopt NOUNSET  ≡  set -u  ≡  setopt -o nounset
# All three set the same flag; pick one style and be consistent.

# Where people get confused: setopt is NOT a superset of set.
# set has its own namespace (the POSIX flags: -e, -u, -x, -n, etc.)
# setopt controls Zsh-specific options (HIST_*, PUSHD_*, GLOB_*, etc.)
# Many Zsh options have no set -o equivalent.
# To see all options and their current state: setopt (lists enabled options)
# To find the name of a Zsh option: man zshoptions
```

**4. Scripts don't source `.zshrc` — startup file ordering matters**

```zsh
# A script run as: ./myscript.zsh  (or zsh myscript.zsh)
# Sources: /etc/zshenv → ~/.zshenv  ONLY
# Does NOT source: .zshrc, .zprofile, .zlogin

# If your script relies on PATH, aliases, or functions from .zshrc:
# → Those are not available in scripts
# → Move them to .zshenv (for env vars) or explicitly source what you need
# → Or add: source ~/.zshrc at the top of your script (rarely the right fix)

# The mental model:
# .zshenv  → environment that everything needs (PATH, EDITOR, LANG)
# .zshrc   → interactive session config (completions, aliases, plugins, prompt)
# Scripts are not interactive sessions — they don't get .zshrc automatically
```

## Decision Cheat Sheet

| Use Zsh when... | Use Bash instead when... |
|-----------------|-------------------------|
| Your interactive shell on macOS/Linux | Writing scripts for CI/CD pipelines |
| Developer experience: completions, plugins, prompt | Portability across Linux environments |
| Extended globbing interactively (`**`, qualifiers) | Docker `RUN` commands |
| Float arithmetic needed in shell | Team expects Bash; script will run on servers |
| Writing personal `.zshrc` automation | You don't control the target shell |
| zmv for bulk file renaming | GitHub Actions, Alpine containers |
| You're on macOS and not writing shared scripts | Anything that might run on a minimal Linux |
