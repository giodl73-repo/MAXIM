# Scripting: Fish

> Friendly Interactive SHell — breaks POSIX intentionally to achieve discoverability and consistency. Your interactive shell; not for scripts others will run.

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

## Decision Cheat Sheet

| Use Fish when... | Don't use Fish when... |
|-----------------|----------------------|
| Your interactive terminal shell | CI/CD scripts (no /bin/fish guaranteed) |
| Developer UX: autosuggestions, completions | Scripts others will run |
| macOS or Linux daily driver | POSIX compatibility required |
| Personal automation scripts | Docker/container scripts |
| Want web config UI (`fish_config`) | Team uses bash |
