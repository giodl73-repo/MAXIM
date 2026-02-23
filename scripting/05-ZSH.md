# Scripting: Zsh

> macOS default since Catalina (2019). The developer shell: Bash superset with better interactive UX, but 1-indexed arrays and subtle compatibility traps if you switch contexts.

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
  │  Scripts that others run           → Bash (portable)      │
  │  CI/CD, Docker, shared automation  → Bash                 │
  │  Scripts only you run locally      → Either; zsh if pref  │
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

### 7. case, Loops, Functions

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

### 8. setopt — Zsh Options

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

### 9. I/O and Redirection

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

### 10. Startup Files

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

---

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
