# Scripting: Bash

> The lingua franca of CI/CD, containers, and Linux automation. Text streams, POSIX superset, and `set -euo pipefail` as the minimum safety net.

---

## Language Snapshot

| Attribute | Value |
|-----------|-------|
| Platform | Linux (default), macOS (available), Windows (WSL/Git Bash/MSYS2) |
| Extension | `.sh` (convention, not enforced) |
| Shebang | `#!/usr/bin/env bash` (portable) or `#!/bin/bash` (specific) |
| Paradigm | Imperative, command-centric, POSIX superset |
| Typing | Untyped strings; `declare -i` for integer |
| Execution | Fork/exec model; commands are processes |
| Version | Bash 5.x on modern Linux; macOS ships 3.2 (GPL) — upgrade via Homebrew |

---

## Architecture: The Fork/Exec Model

```
script.sh
┌──────────────────────────────────────────────────────┐
│  bash process (PID 1234)                             │
│                                                      │
│  command1                                            │
│  └─► fork() → child PID 1235                        │
│      exec("ls", args)                                │
│      parent waits (waitpid), reads exit code         │
│                                                      │
│  var=$(command2)                                     │
│  └─► fork() + anonymous pipe → capture stdout       │
│      runs in subshell; env changes do NOT propagate  │
│                                                      │
│  (subshell) { ... }                                  │
│  └─► fork() → child gets COPY of env                │
│      variable changes in child lost at exit          │
│                                                      │
│  { group; cmds; }                                    │
│  └─► same process — env changes DO propagate        │
└──────────────────────────────────────────────────────┘

Everything is a command. [[ ]] is a command. true/false are commands.
Exit code 0 = success (true). Non-zero = failure (false).
```

---

## Syntax Reference Card

### 1. Variables

```bash
# Assign — NO SPACES around =
name=hello
name="hello world"        # quote if contains spaces
readonly CONST=42         # immutable
declare -i count=0        # integer-typed variable
declare -r CONF=val       # readonly
declare -l lower          # auto-lowercase on assignment
declare -u upper          # auto-uppercase on assignment
export PATH="$PATH:/new/bin"  # export to child processes

# Expand
echo "$name"              # always quote — prevents word splitting + glob expansion
echo "${name}"            # explicit braces — required for ${name}suffix disambiguation
echo "${#name}"           # string length
echo "${name:-default}"   # use default if unset or empty
echo "${name:=default}"   # assign default if unset
echo "${name:?error msg}" # abort with error if unset
echo "${name:+other}"     # use "other" if set, else empty

# Subshell capture
result=$(command)         # preferred over backticks
result=`command`          # legacy — avoid; nesting is painful

# Unset
unset name
```

### 2. String Quoting

```bash
# Single quotes: EVERYTHING is literal — no expansion whatsoever
echo 'no $expansion, no \n escape, no $(cmd)'
# → prints literally: no $expansion, no \n escape, no $(cmd)

# Double quotes: $var, ${}, $() expand; everything else is literal
name="world"
echo "hello $name"            # → hello world
echo "result: $(( 2+3 ))"     # → result: 5
echo "date: $(date +%F)"      # → date: 2026-02-22

# ANSI-C quoting $'...' (bash/zsh only, not POSIX sh)
echo $'tab:\there\nnewline'   # → tab:    here\nnewline (actual tab and newline)
echo $'\x41\x42\x43'          # → ABC (hex escapes)
echo $'\u2603'                 # → snowman unicode (bash 4.2+)

# The word-splitting trap — the #1 beginner mistake
file="my file.txt"
rm $file     # WRONG: tries to rm "my" and "file.txt" separately
rm "$file"   # CORRECT: one argument

# Glob expansion in unquoted vars
pattern="*.txt"
ls $pattern   # shell expands globs — may or may not be what you want
ls "$pattern" # literal *.txt string — passed as-is to ls
              # for glob patterns: use arrays: files=(*.txt); ls "${files[@]}"
```

### 3. Arrays

```bash
# Indexed arrays (0-based)
a=(one two three)
a=( $(ls *.txt) )          # from command output (word-splits on whitespace)
mapfile -t a < file.txt    # read lines into array (bash 4+, no word-splitting)

echo "${a[0]}"             # first element
echo "${a[-1]}"            # last element (bash 4.3+)
echo "${a[@]}"             # all elements — each as separate word; ALWAYS quote!
echo "${a[*]}"             # all elements as single IFS-separated string
echo "${#a[@]}"            # length
echo "${!a[@]}"            # indices: 0 1 2

a+=("four")                # append single element
a+=("five" "six")          # append multiple

unset 'a[1]'               # delete index 1 (creates sparse array)
a=("${a[@]}")              # re-index after deletion (compacts to dense)

# Slice
echo "${a[@]:1:2}"         # 2 elements starting at index 1

# Associative arrays (bash 4+)
declare -A h
h[name]="Alice"
h[age]=42
echo "${h[name]}"
echo "${!h[@]}"            # keys
echo "${h[@]}"             # values
for k in "${!h[@]}"; do
    echo "$k = ${h[$k]}"
done

# CRITICAL: always quote array expansion
for item in "${a[@]}"; do  # CORRECT — handles elements with spaces
    echo "$item"
done
for item in ${a[@]}; do    # WRONG — word-splits on spaces inside elements
    echo "$item"
done
```

### 4. Arithmetic

```bash
# Integer arithmetic only — no native float
result=$(( 2 + 3 * 4 ))   # → 14
result=$(( 10 / 3 ))       # → 3 (integer division — truncates)
result=$(( 10 % 3 ))       # → 1 (modulo)
result=$(( 2 ** 10 ))      # → 1024 (exponent)

(( x++ ))                  # increment (no $ needed inside (( )))
(( x += 5 ))
(( x > 5 )) && echo "yes"  # (( )) returns exit code 0=true, 1=false

# declare -i enforces integer — assignment auto-evaluates arithmetic
declare -i count=0
count+=1                   # equivalent to (( count += 1 ))

# Float: pipe through bc or awk
echo "scale=2; 10/3" | bc              # → 3.33
result=$(awk 'BEGIN {print 1.5 * 2.5}')  # → 3.75
result=$(python3 -c "print(1.5 * 2.5)")  # → 3.75

# printf for formatted numbers
printf "%.2f\n" 3.14159    # → 3.14

# Trap: (( x = 0 )) returns exit code 1 (the result is 0 = falsy)
# With set -e this aborts the script!
(( x = 0 )) || true        # safe workaround
x=0                        # simpler: just use assignment
```

### 5. Conditionals

```bash
# [[ ]] is bash-specific (preferred); [ ] is POSIX sh
# Use [[ ]] in all bash scripts unless cross-shell portability required

# String tests
[[ "$a" == "$b" ]]         # equal (case-sensitive)
[[ "$a" != "$b" ]]         # not equal
[[ "$a" == foo* ]]         # glob pattern match (right side UNQUOTED for glob)
[[ "$a" =~ ^[0-9]+$ ]]     # regex match (right side UNQUOTED)
                            # capture groups land in ${BASH_REMATCH[@]}
[[ -z "$a" ]]              # empty string (zero length)
[[ -n "$a" ]]              # non-empty string
[[ "$a" < "$b" ]]          # lexicographic less than

# Numeric tests — use -eq/-ne/-gt etc., NOT == for numbers
[[ $x -eq $y ]]   [[ $x -ne $y ]]   [[ $x -gt $y ]]
[[ $x -lt $y ]]   [[ $x -ge $y ]]   [[ $x -le $y ]]
# Or arithmetic context for numeric comparisons:
(( x == y ))   (( x > y ))   (( x != y ))

# File tests
[[ -f file ]]      # regular file exists
[[ -d dir ]]       # directory exists
[[ -e path ]]      # any file/dir/symlink exists
[[ -r file ]]      # readable by current user
[[ -w file ]]      # writable
[[ -x file ]]      # executable
[[ -s file ]]      # non-empty file (size > 0)
[[ -L file ]]      # symlink
[[ file1 -nt file2 ]]  # file1 newer than file2
[[ file1 -ot file2 ]]  # file1 older than file2

# Compound conditions
[[ -f file && -r file ]]         # AND inside [[ ]]
[[ -f file || -d file ]]         # OR inside [[ ]]
[[ ! -f file ]]                  # NOT
[[ -f file ]] && [[ -r file ]]   # AND as separate commands

# Command exit code as condition (0 = true, non-zero = false)
if grep -q "pattern" file; then echo "found"; fi
if command; then ...             # runs command; tests its exit code

# Full if/elif/else
if [[ condition ]]; then
    echo "true"
elif [[ other ]]; then
    echo "elif"
else
    echo "false"
fi

# One-liner idioms
[[ -f file ]] && echo "exists"
[[ -f file ]] || echo "missing"
[[ -f file ]] || { echo "missing" >&2; exit 1; }  # group with { }

# POSIX [ ] vs bash [[ ]] differences
# [ ] requires quoting vars: [ "$a" = "$b" ] not [ $a = $b ]
# [ ] uses = not ==
# [ ] no regex support, no glob on right side
# [ ] && and || go OUTSIDE: [ cond1 ] && [ cond2 ]
```

### 6. case/esac

```bash
case $var in
    "hello")
        echo "got hello"
        ;;
    "foo"|"bar")        # multiple patterns with |
        echo "foo or bar"
        ;;
    [0-9]*)             # glob: starts with digit
        echo "starts with number"
        ;;
    *.txt)              # glob: ends with .txt
        echo "text file"
        ;;
    *)                  # default
        echo "no match"
        ;;
esac

# Fallthrough (bash 4+): ;& falls to next clause body
case $x in
    a) echo "a" ;&     # falls through to b's body
    b) echo "b" ;;
esac

# ;;& (bash 4+): test next pattern too (instead of short-circuiting)
case $x in
    *[0-9]*) echo "has digit" ;;&
    *[a-z]*) echo "has lowercase" ;;
esac
```

### 7. Loops

```bash
# For-in: iterate literal list
for item in one two three; do
    echo "$item"
done

# For-in array (CRITICAL: quote the expansion)
for item in "${array[@]}"; do
    echo "$item"
done

# C-style for
for (( i=0; i<10; i++ )); do
    echo $i
done

# Glob iteration
for f in *.txt; do
    [[ -f "$f" ]] || continue   # guard: skip literal "*.txt" if no matches
    process "$f"
done

# Reading file line by line
while IFS= read -r line; do    # IFS= preserves leading whitespace; -r no backslash interp
    echo "$line"
done < file.txt

while IFS= read -r line; do    # from command output via process substitution
    echo "$line"
done < <(command)

# WRONG way to read lines
for line in $(cat file); do    # word-splits on whitespace, breaks on spaces
    echo "$line"
done

# While
i=0
while [[ $i -lt 10 ]]; do
    echo $i
    (( i++ ))
done

# Until (loop until condition is true — opposite of while)
until [[ $condition ]]; do ...; done

# Infinite loop
while true; do
    sleep 1
done

# break and continue
for x in "${arr[@]}"; do
    [[ "$x" == "skip" ]] && continue
    [[ "$x" == "stop" ]] && break
done

# Loop with index
for i in "${!array[@]}"; do
    echo "[$i] = ${array[$i]}"
done
```

### 8. Functions

```bash
# Define (two syntaxes — functionally identical in bash)
my_func() {
    local first="$1"           # local scope — CRITICAL; without local it's global
    local second="$2"
    local -a arr=("${@:3}")    # all args from $3 onward into local array
    echo "processed: $first $second"  # "return value" via stdout capture
    return 0                   # exit code only: 0=success, 1-255=error
}

function my_func {             # bash-specific syntax; identical behavior
    ...
}

# Call and capture output
result=$(my_func arg1 arg2)

# Call and check exit code
if my_func arg1 arg2; then
    echo "succeeded"
fi

# Return values — Bash has NO mechanism to return arbitrary data via return
# Convention 1: capture stdout (cleanest)
result=$(compute_value)

# Convention 2: nameref output parameter (bash 4.3+)
get_value() {
    local -n _ret=$1    # nameref: _ret is an alias for the variable named by $1
    _ret="the computed value"
}
get_value my_var
echo "$my_var"          # → the computed value

# Convention 3: set a global (avoid — hard to reason about)
_result=""
compute() { _result="computed value"; }
compute
echo "$_result"

# Cleanup with trap
cleanup() {
    local exit_code=$?
    rm -f /tmp/myfile.tmp
    echo "cleaned up" >&2
    exit $exit_code
}
trap cleanup EXIT        # runs on ANY exit (normal, error, or signal)
trap cleanup INT TERM    # also handles Ctrl-C and kill
```

### 9. I/O and Redirection

```bash
# Output
echo "message"                # appends newline; portability issues with -e / -n
printf "formatted %s\n" "$var"  # preferred: consistent across shells and platforms
printf "%.2f\n" 3.14159
echo "error message" >&2       # write to stderr (fd 2)

# Input
read -r var                   # read line from stdin; -r disables backslash interpretation
read -rp "Enter name: " name  # with prompt
read -rs password             # silent (passwords)
read -rt 5 var                # timeout after 5 seconds (exits non-zero on timeout)
read -ra arr                  # read whitespace-split tokens into array

# Redirection
cmd > file           # stdout to file (overwrite)
cmd >> file          # stdout append
cmd < file           # stdin from file
cmd 2> err.log       # stderr to file
cmd 2>&1             # redirect stderr to wherever stdout currently goes
cmd > file 2>&1      # both stdout and stderr to file (CORRECT order)
cmd 2>&1 > file      # WRONG: stderr→old stdout (terminal), stdout→file
cmd &> file          # bash shorthand: both stdout+stderr to file
cmd &>> file         # bash shorthand: both append
cmd > /dev/null 2>&1 # discard all output

# Pipelines
cmd1 | cmd2 | cmd3   # stdout of cmd1 → stdin of cmd2, etc.
echo "input" | cmd

# PIPESTATUS: check exit codes of each stage individually
cmd1 | cmd2 | cmd3
echo "${PIPESTATUS[@]}"   # e.g., "0 1 0" — cmd2 failed
# with set -o pipefail: pipe returns first non-zero exit code

# Here-doc
cat <<EOF
Line one
Line two with $var expansion
EOF

cat <<'EOF'            # single-quoted delimiter: no expansion
Literal $var stays literal
EOF

cat <<-EOF             # strip leading TABS (not spaces) from body
	indented
	content
EOF

# Here-string
grep "pattern" <<< "string to search in"
read var <<< "assign this value"

# Process substitution (bash-only — not POSIX)
diff <(sort file1) <(sort file2)       # treat command output as a file descriptor
tee >(gzip > archive.gz) >(wc -l)     # write to two sinks simultaneously

# Subshell vs command group
(cmd1; cmd2)     # subshell fork — env changes do NOT affect parent
{ cmd1; cmd2; }  # same process — env changes DO affect parent
                  # trailing ; and space before } are required syntax
```

### 10. Exit Codes and Error Handling

```bash
# Last exit code
echo $?           # 0 = success, 1-255 = error/failure

# Explicit exit
exit 0            # success
exit 1            # general error (convention)
exit 2            # misuse of shell/command (convention)

# Recommended header for robust scripts
set -euo pipefail
# -e            exit immediately on any command that returns non-zero
# -u            treat unset/undefined variables as errors (catches typos)
# -o pipefail   pipe exit code = rightmost non-zero stage (not just last cmd)

# -e sharp edges — these do NOT trigger -e:
# - Commands in if condition:  if failing_cmd; then ...
# - With || or &&:             failing_cmd || true
# - Inside functions called from conditions: if check_func; then
# - Subshell exit:             result=$(failing_cmd) — this DOES trigger it

# Manual error handling
if ! cmd; then
    echo "cmd failed" >&2
    exit 1
fi

cmd || { echo "failed" >&2; exit 1; }   # inline one-liner

# set -u trap: fires on ${arr[@]} when array is empty
# Workaround for empty arrays:
for item in "${arr[@]+"${arr[@]}"}"; do  # expand only if set
    echo "$item"
done

# Capture stderr separately
err=$(cmd 2>&1 >/dev/null)    # capture stderr; discard stdout

# Cleanup handler
cleanup() {
    local exit_code=$?
    rm -f /tmp/work.tmp
    exit $exit_code
}
trap cleanup EXIT

# Signal handling
trap 'echo "Interrupted" >&2; exit 130' INT    # 130 = 128+SIGINT
trap 'echo "Terminated" >&2; exit 143' TERM   # 143 = 128+SIGTERM
trap '' HUP                                     # ignore SIGHUP

# Subshell exit codes are visible
(exit 5)
echo $?    # → 5
```

### 11. Script Arguments

```bash
$0         # script name (full path or as invoked)
$1 $2 $3   # positional parameters
"$@"       # all args, each separately quoted — ALWAYS use this form
"$*"       # all args joined with IFS separator (rarely what you want)
$#         # argument count

# Loop all arguments
for arg in "$@"; do
    echo "arg: $arg"
done

# shift: consume arguments one by one
echo "first: $1"
shift           # $2 becomes $1, $3 becomes $2, etc.
echo "was \$2: $1"

# Named argument parsing (manual — handles --flag value and --flag=value)
verbose=0
positional=()
while [[ $# -gt 0 ]]; do
    case "$1" in
        --name)        name="$2";           shift 2 ;;
        --verbose|-v)  verbose=1;           shift   ;;
        --name=*)      name="${1#--name=}"; shift   ;;
        --)            shift;               break   ;;  # end of options
        -*)            echo "Unknown: $1" >&2; exit 1 ;;
        *)             positional+=("$1"); shift   ;;
    esac
done
# positional[@] now has non-option arguments

# getopts (POSIX, single-character flags only)
while getopts "vn:o:" opt; do
    case $opt in
        v) verbose=1           ;;
        n) name="$OPTARG"      ;;
        o) output="$OPTARG"    ;;
        ?) echo "Usage: $0 [-v] [-n name] [-o output]" >&2; exit 1 ;;
    esac
done
shift $(( OPTIND - 1 ))   # remove parsed options; positionals remain in "$@"
```

### 12. String Operations

```bash
# Substring extraction: ${var:offset:length}
str="hello world"
echo "${str:0:5}"      # → hello   (chars 0-4)
echo "${str:6}"        # → world   (from index 6 to end)
echo "${str:(-5)}"     # → world   (last 5; parentheses required for negative offset)

# Prefix removal: # (shortest match) and ## (longest/greedy)
file="path/to/file.txt"
echo "${file#*/}"      # → to/file.txt   (remove shortest prefix matching */)
echo "${file##*/}"     # → file.txt      (remove longest prefix matching */ — basename)
echo "${file%.*}"      # → path/to/file  (remove shortest suffix matching .*)
echo "${file%%.*}"     # → path/to/file  (remove longest suffix — same here)
echo "${file%/*}"      # → path/to       (dirname equivalent)

# Replace: ${var/pattern/replacement}
echo "${str/world/bash}"    # → hello bash   (first occurrence)
echo "${str//l/L}"          # → heLLo worLd  (all occurrences)
echo "${str/#hello/HELLO}"  # → HELLO world  (anchored at start)
echo "${str/%world/WORLD}"  # → hello WORLD  (anchored at end)

# Case conversion (bash 4+)
echo "${str,,}"        # → hello world  (all lowercase)
echo "${str^^}"        # → HELLO WORLD  (all uppercase)
echo "${str^}"         # → Hello world  (capitalize first char only)
echo "${str^^[aeiou]}" # → hEllO wOrld  (uppercase matching chars only)

# Test containment
[[ "$str" == *world* ]]  # glob: contains "world"
[[ "$str" =~ world ]]    # regex: contains "world"

# Length
echo "${#str}"         # → 11

# Trim whitespace (no built-in — compose from parameter expansion)
str="  hello  "
trimmed="${str#"${str%%[! ]*}"}"   # ltrim (remove leading spaces)
trimmed="${str%"${str##*[! ]}"}"   # rtrim (remove trailing spaces)
# Practical: use sed or xargs for readability
trimmed=$(echo "$str" | xargs)    # trims both ends via word-splitting
```

---

## What Makes Bash Distinct

```
Bash's conceptual model: COMMANDS, not expressions.

  Everything is a command. Commands return exit codes.
  "Conditions" [[ ]] are just commands that return 0 or 1.
  Pipelines wire commands via anonymous kernel pipes.

  Word splitting and glob expansion happen AFTER variable substitution:
    files=$(ls *.txt)         # splits on whitespace — fragile
    rm $files                 # word-splits again — dangerous
    files=(*.txt)             # CORRECT: array preserves filenames with spaces

  The universal quoting rule:
    Quote ALL variable expansions: "$var"  "${arr[@]}"
    Exception: inside [[ ]] and (( )) — word-splitting doesn't apply there

  Execution model:
    script runs in a bash process
    each external command = fork() + exec()
    var=$(...) = fork() + pipe + subshell (env changes are lost)
    source file = no fork — runs in current process (env changes persist)
```

---

## POSIX sh Portability: Bash-Only vs Portable

| Feature | Bash | POSIX sh | Notes |
|---------|------|----------|-------|
| `[[ ]]` | Yes | No | Use `[ ]` for sh portability |
| Indexed arrays | Yes | No | No arrays in POSIX sh |
| `declare -A` assoc arrays | Yes | No | Bash 4+ only |
| `$(( ))` arithmetic | Yes | Yes | POSIX |
| `(( ))` arithmetic | Yes | No | Bash-only |
| `local` keyword | Yes | Mostly | Non-POSIX but universal in practice |
| `$'...'` ANSI-C quoting | Yes | No | |
| Process substitution `<()` | Yes | No | |
| `mapfile` / `readarray` | Yes | No | Bash 4+ |
| `source` / `.` | Both | `.` only | |
| `${var,,}` case conversion | Yes | No | Bash 4+ |
| `read -a` into array | Yes | No | |
| `**` recursive glob | Yes | No | Requires `shopt -s globstar` |
| `;&` fallthrough in `case` | Yes | No | Bash 4+ |

> Rule: `#!/bin/sh` scripts must use POSIX-only features.
> Docker `RUN` and Alpine use `/bin/sh` → dash (strict POSIX).
> Use `bash -c` or `#!/bin/bash` shebang when you need bash features.

---

## Ecosystem

| Tool | Role | Notes |
|------|------|-------|
| `shellcheck` | Static linter — catches quoting traps, unbound vars | Run in CI; VSCode extension available |
| `shfmt` | Formatter | Consistent indentation and style |
| `jq` | JSON processing in shell | `curl api | jq '.data[].name'` |
| `yq` | YAML/JSON/XML processing | Like jq for YAML |
| `fzf` | Fuzzy interactive selection | History search, file picker, menu UI |
| `bats` | Bash automated testing | TAP-compliant test framework for shell |
| `envsubst` | Env var substitution in templates | Kubernetes manifest injection |
| `xargs` | Build commands from stdin | `find . -name "*.log" | xargs rm` |
| `parallel` | Parallel command execution | GNU parallel — N-way fan-out |
| `direnv` | Per-directory `.envrc` auto-loading | Dev environment management |

---

## Gotchas and Traps

| Trap | Issue | Fix |
|------|-------|-----|
| Spaces around `=` | `x = 5` calls a command named "x" with args | `x=5` — no spaces |
| Unquoted `$var` | Word splitting and glob expansion surprise you | Always `"$var"` |
| `$@` vs `$*` | `"$*"` joins all args; `"$@"` preserves them | Always `"$@"` |
| `set -e` with `\|\|` | `failing_cmd \|\| true` silently disables -e for that line | `if ! failing_cmd; then true; fi` |
| `set -u` + empty array | `${arr[@]}` is unbound if array is empty | `${arr[@]+"${arr[@]}"}` guard |
| `[[ ]]` vs `[ ]` | `[ ]` needs quotes everywhere; uses `=` not `==`; no regex | Use `[[ ]]` in bash scripts |
| Subshell variable leak | `while read; done \| cmd` runs loop in subshell | Use `while ... done < <(cmd)` process substitution |
| `cd` failure | `cd /path` fails; script may continue if not caught | `cd /path \|\| { echo "cd failed" >&2; exit 1; }` |
| Glob with no match | `for f in *.txt` → `f="*.txt"` literally if no files | `shopt -s nullglob` or `[[ -f "$f" ]]` guard |
| `source` vs `./script` | `./script` is subshell — env changes are lost | `source script` to propagate env changes |
| Arithmetic zero | `(( x = 0 ))` returns exit code 1 — triggers `set -e` | `x=0` or `(( x = 0 )) \|\| true` |
| `echo -e` portability | `-e` behavior varies across shells and distros | Use `printf` instead |
| Uninitialized var typo | `echo $PTAH` silently expands to empty | `set -u` catches this |

---

## Bridge: PowerShell to Bash

| PowerShell | Bash | Notes |
|-----------|------|-------|
| `$var = "value"` | `var=value` | No spaces; no `$` on left side |
| `$?` (boolean) | `$?` (integer) | PS: True/False; Bash: 0=success, 1+=error |
| `$LASTEXITCODE` | `$?` | Bash only has one exit code variable |
| `@("a","b","c")` | `a=("a" "b" "c")` | 0-indexed in Bash |
| `$a.Count` | `${#a[@]}` | |
| `$a[0]` | `${a[0]}` | Both 0-indexed |
| `foreach ($x in $a)` | `for x in "${a[@]}"` | |
| `if (Test-Path $p)` | `if [[ -f "$p" ]]` | `-d` for directory |
| `> $null` | `> /dev/null` | Discard output |
| `> $null 2>&1` | `&> /dev/null` | Discard all output |
| `try { } catch { }` | `if ! cmd; then; fi` or `trap` | No try/catch in bash |
| `-ErrorAction Stop` | `set -euo pipefail` | Script-level; not per-command |
| `$PSScriptRoot` | `$(dirname "$(realpath "$0")")` | Script's own directory |
| `Write-Error "msg"` | `echo "msg" >&2` | Write to stderr |
| `Write-Host "msg"` | `echo "msg"` | Write to stdout |
| `Read-Host "prompt"` | `read -rp "prompt: " var` | |
| `$env:VAR` | `$VAR` | Just the name; `export VAR=val` to set |
| `-like "foo*"` | `[[ "$x" == foo* ]]` | Glob match |
| `-match "regex"` | `[[ "$x" =~ regex ]]` | Regex match |
| `$matches[1]` | `${BASH_REMATCH[1]}` | Regex capture groups |
| `Set-Location path` | `cd path` | |
| `Get-ChildItem *.txt` | `ls *.txt` or `find . -name "*.txt"` | |
| `Get-Content file` | `cat file` | |
| `Select-Object -First 5` | `head -5` | |
| `Where-Object { $_.prop -eq val }` | `grep`, `awk`, `jq` | No objects — text streams |
| `$_.PropertyName` | Column in `awk`, key in `jq` | Bash works with text, not objects |

---

## Decision Cheat Sheet

| Use Bash when... | Use sh when... | Use PowerShell when... |
|-----------------|---------------|----------------------|
| CI/CD scripts (GitHub Actions, GitLab CI) | Docker `RUN` commands | Windows automation |
| Linux server automation | Alpine/minimal container scripts | Azure resource management |
| Calling Unix tools natively (find, grep, sed, awk) | Init scripts / boot scripts | Working with .NET objects |
| Scripting alongside Makefiles | Maximum POSIX portability | Structured object pipelines |
| Developer environment scripts on Linux/macOS | Embedded systems / IoT | Team that lives in Windows |
| When the target machine has bash | When you don't know the shell | Azure PowerShell / Az module |
