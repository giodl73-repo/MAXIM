# Universal Scripting Cheat Sheet

8 languages × 12 topics. Comparison tables first (feature-first lookup), language quick cards second (language-first lookup).

Languages covered: Batch, PowerShell, Bash, sh (POSIX), Zsh, Fish, AWK, Perl

---

# Part A — Comparison Tables

---

### Topic 1: File Extension & Invocation

| Language   | Extension     | Shebang Line                            | Run Command                                  | Notes                                                        |
|------------|---------------|-----------------------------------------|----------------------------------------------|--------------------------------------------------------------|
| Batch      | `.bat` / `.cmd` | None — cmd.exe only                   | `script.bat` or `call script.bat`            | `@echo off` at top to suppress command echo                  |
| PowerShell | `.ps1`        | Optional: `#!/usr/bin/env pwsh`         | `pwsh script.ps1` or `.\script.ps1`          | ExecutionPolicy may block; `Set-ExecutionPolicy RemoteSigned` |
| Bash       | `.sh`         | `#!/usr/bin/env bash` or `#!/bin/bash`  | `bash script.sh` or `chmod +x && ./script.sh` | Prefer `env bash` for portability across `/usr/local/bin`   |
| sh (POSIX) | `.sh`         | `#!/bin/sh`                             | `sh script.sh`                               | POSIX only; no Bash extensions; safest for Docker/Alpine     |
| Zsh        | `.zsh`        | `#!/usr/bin/env zsh`                    | `zsh script.zsh`                             | Rarely scripted standalone; usually interactive config       |
| Fish       | `.fish`       | `#!/usr/bin/env fish`                   | `fish script.fish`                           | Not POSIX compat; can't source Bash scripts                  |
| AWK        | `.awk`        | `#!/usr/bin/awk -f`                     | `awk -f script.awk file` or `awk '{...}' file` | Usually inline one-liners passed directly to shell          |
| Perl       | `.pl`         | `#!/usr/bin/perl` or `#!/usr/bin/env perl` | `perl script.pl`                          | `perl -e 'code'` one-liners; `perl -w` for warnings         |

---

### Topic 2: Variables — Declare, Assign, Expand

| Language   | Assign                        | Expand                  | Declare / Type Hint               | Unset / Clear                        |
|------------|-------------------------------|-------------------------|-----------------------------------|--------------------------------------|
| Batch      | `SET myvar=hello` (no spaces!)| `%myvar%`               | `SETLOCAL` (scope); `SET /A` for int | `SET myvar=` (set to empty)       |
| PowerShell | `$name = "value"`             | `$name` / `"...$name..."` | `[string]$name = "value"`; `[int]` etc | `Remove-Variable name` or `$name = $null` |
| Bash       | `name=value` (NO spaces around `=`) | `$name` or `${name}` | `declare -r` readonly; `declare -i` integer; `declare -a` array | `unset name` |
| sh (POSIX) | `name=value`                  | `$name` or `${name}`    | `readonly name`                   | `unset name`                         |
| Zsh        | `name=value`                  | `$name`                 | `typeset -r` readonly; `typeset -i` int; `typeset -f` float | `unset name` |
| Fish       | `set name value` (no `=`!)    | `$name`                 | `set -l` local; `set -x` export; `set -U` universal (persists) | `set -e name` |
| AWK        | `var = value` (inside program) | `var`                  | No declaration; vars spring into existence | `delete arr[key]` for arrays only |
| Perl       | `my $name = "value"`          | `$name`                 | `my` lexical; `our` package-global; `local` dynamic scoping | `undef $name`; `delete $hash{key}` |

**Critical:** Bash `name=value` with spaces around `=` is a syntax error. `name = value` tries to run `name` as a command with `=` and `value` as arguments.

---

### Topic 3: String Quoting & Interpolation

| Language   | Single Quotes               | Double Quotes                          | Other                                          | Notes                                                  |
|------------|-----------------------------|----------------------------------------|------------------------------------------------|--------------------------------------------------------|
| Batch      | No single quotes (literal chars) | `"string"` — sometimes literal! | `^` escapes special chars; `%%` = literal `%` in scripts | Quoting in Batch is famously broken; `"` may not work as expected with all commands |
| PowerShell | `'literal — no $expansion'` | `"expands $var and $($expr)"`          | Here-string: `@' '@` (literal) / `@" "@` (interpolating) | Single quote is truly literal; backtick `` ` `` is escape char |
| Bash       | `'no $expansion whatsoever'` | `"$var expands, \n escapes"`          | `$'tab\there\n'` (ANSI-C quoting); here-doc `<<EOF` | `$'...'` is Bash-only, not POSIX sh |
| sh (POSIX) | `'literal'`                 | `"$var expands"`                       | Here-doc `<<EOF`; no `$'...'`                  | Truly portable; `$'...'` not available                 |
| Zsh        | `'literal'`                 | `"$var expands"`                       | Same as Bash + `$'...'`; prompt expansion `%n` etc | `"${(U)var}"` — parameter expansion flags are powerful |
| Fish       | `'literal'`                 | `"$var expands"`                       | No here-doc; no `$'...'`; `\t` works in `"..."` | Simpler quoting model than Bash; no ANSI-C quoting |
| AWK        | n/a                         | `"strings only"`                       | `/regex/` for patterns; `\n \t` in strings     | Single quotes used by the *shell* to pass the AWK program; AWK itself only has double quotes |
| Perl       | `'literal $no_expand \n-literal'` | `"$var interpolates \n \t"`     | `q(...)` = single-quote-like; `qq(...)` = double-quote-like; `qw(word list)` = `("a","b","c")` | Extensive quoting operators; heredoc: `<<'END'` / `<<"END"` |

---

### Topic 4: Arrays / Lists

| Language   | Create                           | Access                     | Length           | Iterate                                  | Notes                                                 |
|------------|----------------------------------|----------------------------|------------------|------------------------------------------|-------------------------------------------------------|
| Batch      | `SET arr[0]=val` (naming trick)  | `%arr[0]%`                 | No built-in      | `FOR /L %%i IN (0,1,N) DO ...`           | Not real arrays; just variable name convention        |
| PowerShell | `$a = @(1, 2, 3)` or `$a = 1,2,3` | `$a[0]`, `$a[-1]` (last) | `$a.Count`       | `foreach ($x in $a)` or `$a \| ForEach-Object` | Slices: `$a[1..3]`; `-contains`; `Where-Object`     |
| Bash       | `a=(1 2 3)` or `a=( $(cmd) )`   | `${a[0]}`, `${a[-1]}` (4.0+) | `${#a[@]}`     | `for x in "${a[@]}"; do`                 | 0-indexed; assoc arrays: `declare -A h; h[key]=val`   |
| sh (POSIX) | No arrays                        | Use positional params `$1 $2` | `$#`          | `for x in $list; do` (IFS-split)         | Biggest POSIX portability cost; workaround: `"$@"`    |
| Zsh        | `a=(1 2 3)`                      | `$a[1]` (**1-indexed!**)   | `$#a` or `${#a}` | `for x in $a; do` or `for x in "${a[@]}"` | **1-indexed** — biggest Bash↔Zsh trap; assoc: `typeset -A` |
| Fish       | `set a 1 2 3`                    | `$a[1]` (1-indexed)        | `count $a`       | `for x in $a; end`                       | 1-indexed like Zsh; no associative arrays natively    |
| AWK        | `a[key] = val` (assoc only)      | `a[key]` or `a[i]`         | n/a (no `.length`) | `for (k in a) { ... }`                | Only associative arrays; no ordered integer arrays    |
| Perl       | `@a = (1, 2, 3)`                 | `$a[0]`, `$a[-1]`          | `scalar @a` or `$#a + 1` | `foreach my $x (@a) { ... }` | `push/pop/shift/unshift/splice`; hash: `%h = (k => v)` |

---

### Topic 5: Arithmetic

| Language   | Integer Arithmetic             | Float Arithmetic              | Increment            | Notes                                                     |
|------------|-------------------------------|-------------------------------|----------------------|-----------------------------------------------------------|
| Batch      | `SET /A result=1+2*3`         | No native float               | `SET /A x+=1`        | `SET /A` only; use VBScript/Perl for float; no parens needed in `SET /A` |
| PowerShell | `$x = 1 + 2 * 3`             | `$x = 1.5 * 2.0`             | `$x++` / `$x += 1`  | Full .NET numeric types; `[Math]::Pow(2,10)` for functions |
| Bash       | `$(( 1 + 2 * 3 ))`           | Use `bc -l <<< "1.5*2"`       | `(( x++ ))`          | `$(( ))` integer only; no native float; `expr` is old/slow |
| sh (POSIX) | `$(( 1 + 2 ))`               | Use `awk 'BEGIN{print 1.5*2}'` | `x=$(( x + 1 ))`    | `$(( ))` is POSIX; `expr` works but slower                |
| Zsh        | `$(( 1 + 2 ))` or `(( x=1+2 ))` | `$(( 1.5 + 2.5 ))`        | `(( x++ ))`          | **Zsh supports float in `(( ))`** — unlike Bash           |
| Fish       | `math "1 + 2 * 3"`           | `math "1.5 + 2.5"`            | `set x (math $x + 1)` | `math` built-in; supports float natively; `math -s0` for integer |
| AWK        | `result = 1 + 2 * 3`         | `result = 1.5 * 2`            | `x++` (C-style)      | Full C-style arithmetic; float native; `int()`, `sqrt()`, `log()`, `exp()` |
| Perl       | `$r = 1 + 2 * 3`             | `$r = 1.5 * 2`                | `$x++` / `$x += 1`  | `**` exponent; `POSIX::floor()`, `POSIX::ceil()`; `use POSIX;` |

---

### Topic 6: if / else Conditionals

**Batch:**
```batch
IF "%var%"=="hello" (
    echo match
) ELSE (
    echo no match
)
IF EXIST file.txt echo exists
IF NOT EXIST file.txt echo missing
IF ERRORLEVEL 1 echo failed          REM true if exit code >= 1
IF /I "%var%"=="HELLO" echo case-insensitive
IF "%a%"=="%b%" echo equal
```

**PowerShell:**
```powershell
if ($x -eq 5)          { "equal" }
elseif ($x -gt 5)      { "greater" }
else                   { "less" }

# Comparison operators (NOT ==, !=, <, >)
# String: -eq -ne -lt -gt -le -ge -like (wildcard) -match (regex) -contains
# Numeric: same operators; PowerShell infers context
# File:  Test-Path $path
#        (Test-Path $path -PathType Leaf)   for file
#        (Test-Path $path -PathType Container) for directory
if ($?) { "last cmdlet succeeded" }            # cmdlet success
if ($LASTEXITCODE -eq 0) { "external cmd ok" } # external process
```

**Bash:**
```bash
if [[ "$var" == "hello" ]]; then    # [[ ]] is bash-only
    echo match
elif [[ $x -gt 5 ]]; then
    echo greater
else
    echo other
fi

# [[ ]] vs [ ]:
#   [[ ]] — bash extension; no word-splitting; regex with =~; safer
#   [ ]   — POSIX; available in sh; more quoting traps

# String tests (inside [[ ]]):  == != < > (lexicographic)
# Numeric tests:                -eq -ne -gt -lt -ge -le
# File tests:  -f (regular file) -d (dir) -e (exists) -r -w -x -s (non-empty) -L (symlink)
# Regex:       [[ "$str" =~ ^[0-9]+$ ]]

if command; then echo "exit 0"; fi   # test a command's exit code directly
```

**sh (POSIX):**
```sh
if [ "$var" = "hello" ]; then    # NOTE: = not == in [ ]
    echo match
fi
# Must use [ ] not [[ ]]
# Numeric: -eq -ne -gt -lt -ge -le (same as bash)
# String: =  !=  (no < > without escaping: \< \>)
```

**Zsh:**
Same as Bash with `[[ ]]`, but critical difference:
`[[ $a = $b ]]` in Zsh is **PATTERN match** (glob), not string equality. Use `==` for equality:
```zsh
[[ $a == "hello" ]]    # equality in Zsh
[[ $a = "hel*" ]]      # GLOB pattern match in Zsh (not equality!)
[[ $a =~ "^hel" ]]     # regex match (same as bash)
```

**Fish:**
```fish
if test "$var" = "hello"
    echo match
else if test $x -gt 5
    echo greater
else
    echo other
end

# test is the Fish equivalent of [ ]
# String: = != (test)  or  string match -q pattern $var
# Numeric: -eq -ne -gt -lt -ge -le  (test flags)
# File: -f -d -e -r -w -x (test flags)
# NO [[ ]] in Fish
```

**AWK:**
```awk
{
    if ($1 == "hello")   print "string match"
    else if ($2 > 100)   print "numeric greater"
    else if ($3 ~ /^[A-Z]/) print "regex match"
    else                 print "other"
}
# ~ is regex match; !~ is negated regex match
# C-style: == != > < >= <=  for numeric
# String comparison: == != (lexicographic)
```

**Perl:**
```perl
if ($var eq "hello") {       # eq for string
    print "match\n";
} elsif ($x > 5) {           # > for numeric
    print "greater\n";
} else {
    print "other\n";
}

# Strings: eq ne lt gt le ge  (NOT == != > < >= <=)
# Numbers: == != > < >= <=   (NOT eq ne lt gt le ge)
# Regex:   $str =~ /pattern/  or  $str !~ /pattern/
# File:    -f $path (file), -d (dir), -e (exists), -r -w -x

# Postfix form (Perl specialty):
print "yes\n" if $x > 0;
print "no\n"  unless $x;     # unless = if not
```

---

### Topic 7: case / switch

| Language   | Syntax / Approach | Pattern Support | Notes |
|------------|-------------------|-----------------|-------|
| Batch      | No built-in — IF/ELSE chain or GOTO labels | No patterns | `IF "%x%"=="a" GOTO case_a` |
| PowerShell | `switch ($x) { "a" { ... } "b" { ... } default { ... } }` | Wildcard: `switch -Wildcard`; Regex: `switch -Regex ($x) { "^a.*" { ... } }` | Can match multiple branches unless `break` used; `switch -File` to process lines |
| Bash       | `case $var in pattern) ... ;; esac` | Glob patterns: `a*`, `[aA]`, `a\|b` | `;;` terminates each arm; `;&` falls through; `;;&` tests next pattern |
| sh (POSIX) | Same `case...esac` syntax | Glob patterns | POSIX standard; `\|` for alternation in patterns |
| Zsh        | Same as Bash + `(( ))` arithmetic case | Glob + regex with `(#b)` flag | `case` is same; `zsh` adds pattern flags for extended matching |
| Fish       | `switch $var; case "a"; ...; case "b" "c"; ...; case "*"; ...; end` | Glob patterns | No `;;`; use newline or `;` between cases; multiple patterns per `case` |
| AWK        | No switch — use if/else chain | n/a | Can use associative arrays as dispatch tables |
| Perl       | No built-in switch (`given/when` experimental/deprecated) | n/a | Use if/elsif chain, or hash dispatch: `$dispatch{$key}->()` |

**Bash case example:**
```bash
case $lang in
  bash|sh) echo "bourne family"  ;;
  zsh)     echo "z shell"        ;;
  fish)    echo "friendly fish"  ;;
  *)       echo "unknown"        ;;
esac
```

**Perl hash dispatch (idiomatic replacement for switch):**
```perl
my %actions = (
    'start' => sub { start_service() },
    'stop'  => sub { stop_service()  },
);
my $fn = $actions{$cmd} // sub { die "unknown: $cmd" };
$fn->();
```

---

### Topic 8: Loops — for, while, break/continue

**Batch:**
```batch
REM for-each over list
FOR %%i IN (a b c) DO echo %%i

REM counted loop (start, step, end)
FOR /L %%i IN (1,1,10) DO echo %%i

REM loop over files
FOR %%f IN (*.txt) DO echo %%f

REM while simulation (no native while)
:loop
IF NOT condition GOTO end
...
GOTO loop
:end

REM Note: %%i in scripts; %i in interactive cmd
```

**PowerShell:**
```powershell
foreach ($item in $collection) { Write-Output $item }
for ($i = 0; $i -lt 10; $i++) { Write-Output $i }
while ($condition) { ... }
do { ... } while ($condition)         # do-while
do { ... } until ($condition)         # do-until (rare)
1..10 | ForEach-Object { $_ }         # pipeline loop; $_ = current item
$collection | ForEach-Object { $_.Name }
# break and continue work inside all loop types
```

**Bash:**
```bash
for item in a b c; do echo "$item"; done
for (( i=0; i<10; i++ )); do echo $i; done   # C-style; bash-only
for file in *.txt; do process "$file"; done  # glob expansion
while [[ condition ]]; do ...; done
until [[ condition ]]; do ...; done          # until = while not
while IFS= read -r line; do                 # read file line by line (canonical)
    process "$line"
done < file.txt
break     # exit loop
continue  # next iteration
```

**sh (POSIX):**
```sh
for item in a b c; do echo "$item"; done
# No C-style for (( )) — POSIX doesn't have it
while [ condition ]; do ...; done
until [ condition ]; do ...; done
while IFS= read -r line; do ...; done < file.txt
```

**Zsh:**
```zsh
for item in a b c; do echo "$item"; done
for (( i=0; i<10; i++ )); do echo $i; done    # same as Bash
for f in *.txt; do ...; done                  # glob
# Zsh-specific compact forms:
repeat 5 { echo "five times" }
for f (*.txt) { process $f }                  # no do/done
while [[ condition ]]; do ...; done
```

**Fish:**
```fish
for item in a b c; echo $item; end
for i in (seq 1 10); echo $i; end             # seq generates sequence
for f in *.txt; process $f; end              # glob
while test condition; ...; end
# No until; no C-style for
# No break/continue — use return or restructure
break; continue  # These DO work in Fish (added in Fish 3.x)
```

**AWK:**
```awk
# C-style for
for (i = 0; i < 10; i++) { print i }

# for-in over associative array
for (key in arr) { print key, arr[key] }

# while
while (condition) { ... }

# do-while
do { ... } while (condition)

next   # continue (skip to next record)
exit   # break out of record processing (runs END block)
```

**Perl:**
```perl
foreach my $item (@array) { print "$item\n" }
for my $item (@array) { ... }              # same as foreach
for (my $i=0; $i<10; $i++) { ... }        # C-style
while ($condition) { ... }
until ($condition) { ... }
do { ... } while ($condition);
# Loop control:
next;  # continue (skip to next iteration)
last;  # break (exit loop)
redo;  # redo current iteration without re-evaluating condition
```

---

### Topic 9: Functions / Subroutines

**Batch:**
```batch
CALL :myFunc "arg1" "arg2"
echo Result: %RESULT%

:myFunc
SET result=%~1          REM %~1 strips surrounding quotes from %1
echo Inside func: %~1
EXIT /B 0               REM EXIT /B = return from subroutine (NOT exit the script!)
                        REM EXIT without /B exits the entire script
```

**PowerShell:**
```powershell
# Basic function
function Get-Upper { param([string]$Name) return $Name.ToUpper() }
$x = Get-Upper -Name "hello"

# Advanced function (CmdletBinding gives -Verbose, -ErrorAction, etc.)
function Invoke-Deploy {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory, ValueFromPipeline)]
        [string]$Target,
        [int]$Retries = 3,
        [switch]$DryRun
    )
    process { ... }   # called once per pipeline input
}
# Return: last expression value is returned; explicit: return $val
# Output goes to pipeline — don't use Write-Host to "return" values
```

**Bash:**
```bash
my_func() {
    local x="$1"            # local variable — always use local!
    local y="${2:-default}"  # default value if $2 unset
    echo "result"           # "return value" is stdout output
    return 0                # return code only; 0-255 range
}
result=$(my_func "arg")     # capture stdout as return value
my_func "arg" || echo "failed"  # check return code
```

**sh (POSIX):**
```sh
my_func() {
    local x="$1"    # local is technically non-POSIX but supported by dash/ash/bash
    echo "result"
    return 0
}
result=$(my_func "arg")
```

**Zsh:**
```zsh
my_func() {
    local x="$1"
    echo "result"
    return 0
}
# autoload: define function in a file, load on first call
autoload -U my_func      # loads from $fpath directories
# Zsh functions can use typeset for local variables too
```

**Fish:**
```fish
function my_func --argument-names first second --description "Does a thing"
    echo "got $first and $second"
end

# Call:
my_func arg1 arg2

# Persist across sessions:
funcsave my_func    # saves to ~/.config/fish/functions/my_func.fish

# Note: Fish functions can't return values via $() — use set + output capture:
set result (my_func arg)
```

**AWK:**
```awk
function square(n,    local_var) {   # extra params = local variables (AWK trick)
    local_var = n * n
    return local_var
}
BEGIN {
    print square(5)    # → 25
}
{
    print square($1)   # called per record
}
# AWK has no closures, no first-class functions
# "Local variable" trick: extra params in signature initialized to ""
```

**Perl:**
```perl
sub my_func {
    my ($arg1, $arg2) = @_;      # @_ = all arguments
    my $result = $arg1 . $arg2;
    return $result;              # or just last expression value
}
my $r = my_func("hello", "world");

# Anonymous sub / closure:
my $fn = sub { my ($x) = @_; return $x * 2 };
$fn->(5);   # → 10

# Prototype (rarely needed):
sub max ($$) { $_[0] > $_[1] ? $_[0] : $_[1] }
```

---

### Topic 10: I/O — Output, Input, Redirection, Pipes

| Language   | Print stdout              | Print stderr                  | Read input          | Redirect stdout | Redirect stderr | Pipe | Discard output |
|------------|---------------------------|-------------------------------|---------------------|-----------------|-----------------|------|----------------|
| Batch      | `ECHO text`               | `ECHO text >&2`               | `SET /P var=Prompt:` | `> file`        | `2> file`       | `\|`  | `> NUL`        |
| PowerShell | `Write-Output "text"` or bareword | `Write-Error "msg"` / `$host.ui.WriteErrorLine()` | `Read-Host "Prompt"` | `> file` or `Out-File` | `2> file` | `\|` | `Out-Null` or `> $null` |
| Bash       | `echo "text"` / `printf "%s\n" "text"` | `echo "err" >&2` | `read -r var` / `read -r -p "Prompt: " var` | `> file` / `>> file` | `2>file` / `2>&1` / `&>file` | `\|` | `> /dev/null` / `&>/dev/null` |
| sh (POSIX) | `echo "text"` / `printf` | `echo "err" >&2`              | `read var`          | `> file`        | `2>file` / `2>&1` | `\|` | `> /dev/null`  |
| Zsh        | `print "text"` (preferred) / `echo` | `print "err" >&2` | `read var` / `vared var` (interactive) | `> file` | `2>file` / `&>file` | `\|` | `> /dev/null`  |
| Fish       | `echo "text"` / `printf` | `echo "err" >&2`              | `read -l var` / `read -P "Prompt: " -l var` | `> file` | `2>file` | `\|` | `> /dev/null`  |
| AWK        | `print "text"` / `printf "%s\n", "text"` | `print "err" > "/dev/stderr"` | Via piped input (`< file` in shell) | `print > "file"` / `print >> "file"` | `print \| "cmd"` | `\| cmd` | `> "/dev/null"` |
| Perl       | `print "text\n"` / `say "text"` (5.10+) | `print STDERR "err\n"` | `my $line = <STDIN>` / `chomp(my $l = <STDIN>)` | `open(my $fh, '>', 'file')` | Same pattern | `\|` (shell) / `open(my $fh, '|-', 'cmd')` | `> /dev/null` (shell) |

**PowerShell pipeline note:** `Write-Host` writes directly to the terminal, bypassing the pipeline. It cannot be captured with `$x = Write-Host "hi"`. Use `Write-Output` or bare expression output to put objects into the pipeline.

**Bash `read` canonical pattern:**
```bash
while IFS= read -r line; do    # IFS= prevents trimming whitespace
    echo "$line"               # -r prevents backslash interpretation
done < file.txt
```

---

### Topic 11: Exit Codes & Error Handling

| Language   | Get exit code                    | Set exit code | Auto-exit on failure          | Try/catch equivalent                    |
|------------|----------------------------------|---------------|-------------------------------|-----------------------------------------|
| Batch      | `%ERRORLEVEL%`                   | `EXIT /B 1`   | No — must check `IF ERRORLEVEL` manually | No; `IF ERRORLEVEL 1 GOTO err` |
| PowerShell | `$LASTEXITCODE` (external) / `$?` (cmdlet, bool) | `exit 1` | `$ErrorActionPreference = "Stop"` | `try { } catch { } finally { }` |
| Bash       | `$?`                             | `exit 1`      | `set -euo pipefail`           | No native; use `if cmd; then ...; fi` or `cmd \|\| handler` |
| sh (POSIX) | `$?`                             | `exit 1`      | `set -e`                      | Same pattern as Bash                    |
| Zsh        | `$?`                             | `exit 1`      | `set -e` / `setopt ERR_EXIT`  | Same as Bash                            |
| Fish       | `$status` (**NOT `$?`**)         | `exit 1`      | No `set -e` — Fish has different error model | `if not cmd; handle_error; end` |
| AWK        | `exit 0` / `exit 1`             | `exit N`      | No automation                 | No; use conditional logic in `END {}`   |
| Perl       | `$?` (for `system()`), `$!` (errno) | `exit 1`  | `use autodie;` (throws on system call failure) | `eval { die "err" }; if ($@) { handle }` |

**Bash `set -euo pipefail` breakdown:**
```bash
set -e         # exit immediately on any command with non-zero exit code
               # EXCEPTIONS: if/while/until condition tests; && || ; commands after !
set -u         # treat unset variables as errors (instead of empty string)
set -o pipefail # pipe exit code = rightmost non-zero exit code in pipe
               # Without this: ls bad_dir | wc -l exits 0 (wc succeeded)

# Robust error handler pattern:
set -euo pipefail
trap 'echo "Error on line $LINENO"; exit 1' ERR
```

**PowerShell `$?` vs `$LASTEXITCODE`:**
```powershell
git status                     # external command
if ($LASTEXITCODE -ne 0) { ... }   # CORRECT: check external exit code
if (-not $?) { ... }               # WRONG for external: $? just reflects PS internal state

Get-Item "nonexistent"             # PowerShell cmdlet
if (-not $?) { ... }               # CORRECT for cmdlet failure
```

---

### Topic 12: Script Arguments

| Language   | First arg       | All args (array) | Count    | Loop all args                    | Shift / consume                  |
|------------|----------------|------------------|----------|----------------------------------|----------------------------------|
| Batch      | `%1`           | `%*` (string, not array) | No built-in | `FOR %%A IN (%*) DO ...`   | `SHIFT` — `%2` becomes `%1`     |
| PowerShell | `$args[0]` or named param | `$args` / `@args` for splatting | `$args.Count` | `foreach ($a in $args)` | Use `param()` block instead of `$args` |
| Bash       | `$1`           | `"$@"` (quoted array) / `$*` (string) | `$#` | `for arg in "$@"; do` | `shift` / `shift N`             |
| sh (POSIX) | `$1`           | `"$@"`           | `$#`     | `for arg in "$@"; do`            | `shift` / `shift N`             |
| Zsh        | `$1`           | `"$@"` or `$argv` | `$#` or `$#argv` | `for arg in "$@"; do`  | `shift` / `shift N`             |
| Fish       | `$argv[1]`     | `$argv`          | `count $argv` | `for arg in $argv; end`   | No `shift`; use `$argv[2..]` slice |
| AWK        | `ARGV[1]` (script arguments) | `ARGV` array | `ARGC - 1` | `for (i=1; i<ARGC; i++)` | n/a (ARGV is read-only) |
| Perl       | `$ARGV[0]`     | `@ARGV`          | `scalar @ARGV` | `foreach my $a (@ARGV)` | `shift @ARGV` (or `shift` — defaults to `@ARGV` in main) |

**Bash `$@` vs `$*`:**
```bash
# With args: one "two three" four
"$@"  →  "one"  "two three"  "four"   # each arg separately quoted — ALWAYS use this
"$*"  →  "one two three four"         # all args as ONE string (IFS-joined)
$@    →  one  two  three  four        # word-split — spaces in args break things
```

**PowerShell named params (preferred over `$args`):**
```powershell
param(
    [Parameter(Mandatory)]
    [string]$Target,
    [int]$Port = 8080,
    [switch]$Verbose
)
# Called as: .\script.ps1 -Target prod -Port 443 -Verbose
```

---

# Part B — Per-Language Quick Cards

---

### Batch Quick Card

```batch
@echo off
SETLOCAL EnableDelayedExpansion     :: isolate variables; enable !var! inside loops

:: Variables
SET name=hello                      :: assign (NO spaces around =)
SET /A num=2+3*4                    :: integer arithmetic
ECHO %name%                         :: expand
SET name=                           :: unset (set to empty)

:: Strings
SET greeting=Hello %name%           :: concatenation is just adjacent
IF "%name%"=="hello" ECHO match     :: compare (case-sensitive)
IF /I "%name%"=="HELLO" ECHO ci     :: /I = case-insensitive

:: Arrays (simulated)
SET arr[0]=alpha
SET arr[1]=beta
ECHO %arr[0]%
FOR /L %%i IN (0,1,2) DO ECHO !arr[%%i]!   :: requires EnableDelayedExpansion

:: Arithmetic
SET /A result=10/3                  :: integer division only
SET /A x+=1                        :: increment

:: if/else
IF "%var%"=="a" (
    ECHO a
) ELSE IF "%var%"=="b" (
    ECHO b
) ELSE (
    ECHO other
)
IF EXIST file.txt ECHO exists
IF ERRORLEVEL 1 ECHO failed         :: true if ERRORLEVEL >= 1

:: Loops
FOR %%i IN (a b c) DO ECHO %%i
FOR /L %%i IN (1,1,10) DO ECHO %%i  :: start,step,end
FOR /F "tokens=1,2 delims=," %%a IN (file.csv) DO ECHO %%a %%b
FOR /R "C:\dir" %%f IN (*.txt) DO ECHO %%f   :: recursive files

:: Functions (subroutines)
CALL :myFunc "arg1" "arg2"
GOTO :EOF

:myFunc
ECHO Got: %~1                       :: %~1 strips quotes
SET result=%~1
EXIT /B 0                           :: EXIT /B = return; EXIT = quit script

:: I/O
ECHO stdout
ECHO stderr >&2
SET /P userInput=Enter value:       :: read from stdin
ECHO text > file.txt
ECHO text >> file.txt               :: append
TYPE file.txt | FIND "pattern"
ECHO text > NUL                     :: discard

:: Exit codes
ECHO Exit code: %ERRORLEVEL%
EXIT /B 0
EXIT /B 1

:: Arguments
ECHO First: %1
ECHO All: %*
SHIFT                               :: %2 becomes %1, etc.
```

---

### PowerShell Quick Card

```powershell
#!/usr/bin/env pwsh
Set-StrictMode -Version Latest      # catches unset vars, method calls on null
$ErrorActionPreference = "Stop"     # throw on cmdlet errors (like set -e for cmdlets)

# Variables
$name = "hello"
[string]$typed = "typed"
[int]$num = 42
$arr = @(1, 2, 3)
$hash = @{ key = "val"; other = 2 }

# Strings
"interpolates $name and $($name.ToUpper())"
'literal — no $expansion'
@"
multiline
interpolating $name heredoc
"@
$s = "hello"; $s.Length; $s.ToUpper(); $s.Replace("h","H")
"hello" -match "^hel"              # regex test; $Matches populated
"hello" -like "hel*"               # wildcard

# Arrays
$a = @(1, 2, 3)       # or just: $a = 1, 2, 3
$a[0]; $a[-1]          # first; last
$a.Count
$a += 4                # append (creates new array)
$a | Where-Object { $_ -gt 1 }
$a | ForEach-Object { $_ * 2 }
$a[1..3]               # slice

# Hashtable
$h = @{ name = "alice"; age = 30 }
$h.name; $h["age"]
$h.Keys; $h.Values
$h.ContainsKey("name")

# Arithmetic
$x = 2 + 3 * 4         # standard precedence
$x++; $x--; $x += 5
[Math]::Pow(2, 10)
[Math]::Round(3.7)

# if/else
if ($x -eq 5)      { "equal" }
elseif ($x -gt 5)  { "greater" }
else               { "less" }
# Operators: -eq -ne -gt -lt -ge -le -like -match -contains -in
# File: Test-Path, (Get-Item $path) -is [System.IO.FileInfo]

# switch
switch ($x) {
    1       { "one" }
    { $_ -gt 10 } { "big" }   # scriptblock condition
    default { "other" }
}
switch -Regex ($str) { "^[0-9]+" { "number" } }

# Loops
foreach ($item in $collection) { $item }
for ($i = 0; $i -lt 10; $i++) { $i }
while ($condition) { }
do { } while ($condition)
1..10 | ForEach-Object { $_ }
$collection | Where-Object { $_.Active } | ForEach-Object { $_.Name }

# Functions
function Get-Value {
    [CmdletBinding()]
    param([Parameter(Mandatory)][string]$Name, [int]$Default = 0)
    return $Name.Length + $Default
}
$r = Get-Value -Name "test" -Default 5

# I/O
Write-Output "to pipeline"
Write-Host "to terminal only (not captured)"
Write-Error "to error stream"
$input = Read-Host "Enter value"
Get-Content file.txt | ForEach-Object { $_ }
Set-Content file.txt "content"
Add-Content file.txt "append"
"text" | Out-File file.txt

# Exit codes
$LASTEXITCODE                      # external process exit code
$?                                  # last cmdlet success (bool)
exit 1

# Error handling
try {
    Get-Item "nonexistent" -ErrorAction Stop
} catch [System.IO.FileNotFoundException] {
    Write-Error "Not found: $_"
} catch {
    Write-Error "Error: $_"
} finally {
    # cleanup
}

# Arguments
param([string]$Target, [int]$Port = 8080, [switch]$DryRun)
# or ad-hoc: $args[0], $args.Count
```

---

### Bash Quick Card

```bash
#!/usr/bin/env bash
set -euo pipefail
trap 'echo "Error on line $LINENO"' ERR

# Variables
name=value              # assign (NO spaces around =!)
echo "$name"            # expand (ALWAYS quote to prevent word-splitting)
echo "${name}_suffix"   # unambiguous expansion
unset name
readonly CONST=42       # immutable

# Default values
echo "${var:-default}"   # use default if var unset or empty
echo "${var:=default}"   # assign default if unset
echo "${var:?error msg}" # error if unset

# Strings
'no interpolation'
"$var interpolates \n"
$'tab\there\nnewline'     # ANSI-C quoting (bash-only)
${#str}                   # string length
${str#prefix}             # remove shortest prefix match
${str##prefix}            # remove longest prefix match
${str%suffix}             # remove shortest suffix match
${str/old/new}            # substitute first
${str//old/new}           # substitute all

# Arrays
a=(one two three)
echo "${a[0]}"            # 0-indexed
echo "${a[-1]}"           # last element (bash 4.0+)
echo "${#a[@]}"           # length
echo "${a[@]}"            # all elements
a+=(four)                 # append
unset 'a[1]'              # remove element
declare -A h              # associative array
h[key]=val; echo "${h[key]}"

# Arithmetic (integers only)
$(( 2 + 3 * 4 ))
(( x++ ))
(( x += 5 ))
(( x == 5 ))              # returns 0/1 exit code (use in if)
# Float: bc -l <<< "1.5 * 2.0"

# if/else
if [[ "$a" == "$b" ]]; then    # [[ ]] = bash test (safer)
    echo equal
elif [[ $x -gt 5 ]]; then
    echo greater
else
    echo other
fi
if [[ -f file ]]; then ...     # file exists and is regular
if [[ -d dir ]]; then ...      # directory exists
if [[ -z "$str" ]]; then ...   # string is empty
if [[ -n "$str" ]]; then ...   # string is non-empty
if [[ "$str" =~ ^[0-9]+$ ]]; then ... # regex match

# case
case $var in
    a|b)   echo "a or b"  ;;
    c*)    echo "starts c" ;;
    *)     echo "other"   ;;
esac

# Loops
for item in a b c; do echo "$item"; done
for (( i=0; i<10; i++ )); do echo $i; done
for file in *.txt; do echo "$file"; done
while [[ condition ]]; do ...; done
until [[ condition ]]; do ...; done
while IFS= read -r line; do echo "$line"; done < file.txt

# Functions
my_func() {
    local x="$1"
    local y="${2:-default}"
    echo "result"       # return value via stdout capture
    return 0            # exit code (0-255 only)
}
result=$(my_func "arg")
my_func || { echo "failed"; exit 1; }

# I/O
echo "stdout"
printf "%s: %d\n" "label" 42
echo "stderr" >&2
read -r var
read -r -p "Enter: " var
cat file | cmd > out 2>&1
cmd > /dev/null 2>&1    # discard all output
cmd &> /dev/null        # same (bash shorthand)
exec 3>&1               # save stdout to fd 3

# Exit codes & error handling
echo $?                 # last exit code
exit 1
cmd || fallback_cmd
cmd && success_cmd
cmd || { cleanup; exit 1; }

# Arguments
# $0 = script name, $1 $2 ... = positional
# "$@" = all args quoted individually (ALWAYS use this)
# "$*" = all args as one string (rarely what you want)
# $# = count
for arg in "$@"; do echo "$arg"; done
shift                   # $2 → $1, $3 → $2, etc.
shift 2                 # skip first 2

# Subshell & command substitution
result=$(cmd)           # capture stdout
(cd /tmp && do_thing)   # subshell (dir change doesn't affect parent)
{ cmd1; cmd2; }         # group in current shell
```

---

### sh (POSIX) Quick Card

```sh
#!/bin/sh
# POSIX sh — maximum portability; runs on dash, ash, busybox, bash, zsh

# Variables
name=value              # NO spaces around =
echo "$name"            # always quote
unset name
readonly CONST=42

# Default values (POSIX)
echo "${var:-default}"  # default if unset/empty
echo "${var:=default}"  # assign default if unset
echo "${var:?error}"    # fatal if unset

# Strings
'literal'
"$var expands"
# No $'...' ANSI-C quoting in POSIX sh
# No arrays

# Arithmetic (POSIX)
x=$(( 2 + 3 * 4 ))
x=$(( x + 1 ))
# No (( x++ )) as standalone — use x=$(( x + 1 ))
# Float: awk 'BEGIN { printf "%.2f\n", 1.5 * 2 }'

# if/else — MUST use [ ] not [[ ]]
if [ "$a" = "$b" ]; then    # NOTE: = not ==
    echo equal
elif [ "$x" -gt 5 ]; then
    echo greater
else
    echo other
fi
[ -f file ]     # file exists (regular)
[ -d dir ]      # dir exists
[ -z "$str" ]   # string empty
[ -n "$str" ]   # string non-empty

# case
case $var in
    a|b) echo "a or b" ;;
    *)   echo "other"  ;;
esac

# Loops
for item in a b c; do echo "$item"; done
# No C-style for (( )) — not POSIX
while [ condition ]; do ...; done
until [ condition ]; do ...; done
while IFS= read -r line; do ...; done < file.txt

# Functions
my_func() {
    local x="$1"        # local is widely supported but not strictly POSIX
    echo "result"
    return 0
}
result=$(my_func arg)

# I/O
echo "stdout"
printf "%s\n" "portable print"   # prefer printf over echo for portability
echo "err" >&2
read var                          # no -r in strict POSIX (use it anyway — supported widely)
cmd > file 2>&1
cmd > /dev/null 2>&1

# Exit codes
echo $?
exit 0

# Arguments — same as Bash
# $1 $2 ... "$@" $# shift
for arg in "$@"; do echo "$arg"; done
```

---

### Zsh Quick Card

```zsh
#!/usr/bin/env zsh
setopt ERR_EXIT PIPE_FAIL UNSET    # equivalent of set -euo pipefail

# Variables
name=value
echo "$name"
unset name
typeset -r CONST=42    # readonly
typeset -i num=0       # integer
typeset -f float=0.0   # float

# Strings
'literal'
"$name interpolates"
${(U)name}             # uppercase (parameter expansion flag)
${(L)name}             # lowercase
${(#)str}              # length  (or $#str)

# Arrays — 1-INDEXED (unlike Bash 0-indexed)
a=(one two three)
echo $a[1]             # "one" — 1-indexed!
echo $a[-1]            # last element
echo $#a               # length
echo $a[@]             # all elements
a+=(four)              # append
typeset -A h           # associative array
h[key]=val

# Glob qualifiers (Zsh superpower)
echo *.txt(.)          # regular files only
echo *(/)              # directories only
echo *(m-7)            # modified within 7 days
echo *(*x*)            # executable files

# Arithmetic — supports float unlike Bash
$(( 2 + 3 * 4 ))
$(( 1.5 + 2.5 ))       # float works!
(( x++ ))
(( x = 3.14 * r * r )) # float arithmetic

# if/else
if [[ "$a" == "$b" ]]; then   # == for equality
    echo equal
elif [[ $x -gt 5 ]]; then
    echo greater
fi
# CRITICAL ZSH DIFFERENCE:
# [[ $a = $b ]]   → GLOB/PATTERN match (not equality!)
# [[ $a == $b ]]  → equality test
# [[ $a =~ $pat ]] → regex match (same as bash)

# Loops
for item in a b c; do echo "$item"; done
for (( i=0; i<10; i++ )); do echo $i; done
for f in *.txt; do ...; done
repeat 5 { echo "five times" }    # Zsh-only
for f (*.txt) { echo $f }         # Zsh compact form (no do/done)
while [[ condition ]]; do ...; done

# Functions
my_func() {
    local x="$1"
    echo "result"
    return 0
}
# Autoload (load from $fpath on first call)
autoload -U compinit    # used for completion functions
fpath=(~/.zsh/functions $fpath)

# I/O
print "preferred over echo in Zsh"
print -r "raw (no escape processing)"
echo "stderr" >&2
read -r var
read -r "var?Prompt: "   # Zsh prompt syntax
print -u 2 "to stderr"  # Zsh way

# Exit codes
echo $?
exit 1
setopt ERR_EXIT          # exit on error (like set -e)

# Arguments (same as Bash)
# $1 $2 ... "$@" $# shift
# Also: $argv array (Zsh alias for positional params)
for arg in "$@"; do echo "$arg"; done
```

---

### Fish Quick Card

```fish
#!/usr/bin/env fish
# Fish is NOT POSIX. Intentionally different syntax.

# Variables
set name value           # NO = sign
set -l name value        # local scope
set -x NAME value        # export to environment (like export in bash)
set -U name value        # universal — persists across sessions
set -e name              # unset/erase variable
echo $name               # expand

# Strings
'literal no $expansion'
"$name interpolates"
# No heredoc; no $'...' ANSI-C quoting
# String manipulation:
string length "hello"    # → 5
string upper "hello"     # → HELLO
string sub -l 3 "hello"  # → hel (first 3 chars)
string split , "a,b,c"   # → a b c (list)
string match "*.txt" file.txt  # glob match
string match -r "^[0-9]+" "42abc"  # regex match

# Arrays (lists) — 1-INDEXED
set a one two three
echo $a[1]               # "one" — 1-indexed
echo $a[-1]              # last
count $a                 # length
echo $a                  # all elements
set a $a four            # append (reassign with new element)
# No associative arrays natively; use two parallel lists or temp file

# Arithmetic
math "2 + 3 * 4"         # → 14
math "1.5 + 2.5"         # → 4  (float supported)
math -s 0 "7 / 2"        # → 3 (integer mode)
set x (math $x + 1)      # increment x

# if/else — uses `test` or `string` commands
if test "$a" = "hello"
    echo match
else if test $x -gt 5
    echo greater
else
    echo other
end

if test -f file.txt; echo file exists; end
if test -d dir; echo dir exists; end
if string match -q "pattern" $var; echo matched; end

# switch/case
switch $var
    case "a"
        echo a
    case "b" "c"           # multiple patterns per case
        echo b or c
    case "*"               # default
        echo other
end

# Loops
for item in a b c; echo $item; end
for i in (seq 1 10); echo $i; end
for f in *.txt; echo $f; end
while test condition; ...; end
break                      # exit loop (Fish 3.x+)
continue                   # next iteration (Fish 3.x+)

# Functions
function my_func --argument-names first second --description "Help text"
    echo "first: $first"
    echo "second: $second"
    return 0
end

# Capture return value (output, not exit code)
set result (my_func arg1 arg2)

# Persist function across sessions
funcsave my_func           # → ~/.config/fish/functions/my_func.fish
funced my_func             # open in editor

# I/O
echo "stdout"
printf "%s\n" "formatted"
echo "stderr" >&2
read -l var                # local var from stdin
read -P "Prompt: " -l var  # with prompt
cmd > file
cmd >> file
cmd 2> errfile
cmd | other_cmd
cmd > /dev/null

# Exit codes — NOTE: $status not $?
echo $status               # last exit code (NOT $? like bash)
exit 1
if not cmd                 # equivalent of "if ! cmd" in bash
    echo "command failed"
end

# Arguments
echo $argv[1]              # first argument (1-indexed)
echo $argv                 # all arguments
count $argv                # count
for arg in $argv; echo $arg; end
# No shift; use: set argv $argv[2..]  to consume first
```

---

### AWK Quick Card

```awk
#!/usr/bin/awk -f
# Run: awk -f script.awk file.txt
# Or inline: awk '{ print $1 }' file.txt
# Or with -F: awk -F, '{ print $2 }' file.csv

# Program structure:
# BEGIN  { ... }      # runs once before first record
# /pattern/ { ... }  # runs on records matching pattern
# { ... }            # runs on every record (no pattern = all)
# END    { ... }     # runs once after last record

# Special variables
# NR  = record number (line count so far)
# NF  = number of fields in current record
# $0  = entire current record
# $1..$NF = individual fields
# FS  = field separator (default: any whitespace)
# OFS = output field separator (default: space)
# RS  = record separator (default: newline)
# ORS = output record separator (default: newline)
# FILENAME = current input file name

BEGIN {
    FS = ","      # set CSV input (or use -F, on command line)
    OFS = "\t"    # tab-separated output
    count = 0
}

/^#/ { next }     # skip comment lines (next = continue to next record)

NF == 0 { next }  # skip empty lines

{
    count++
    print $1, $2  # print fields 1 and 2 (OFS between them)
    printf "%s: %d\n", $1, $2 + 0  # C-style printf
}

END {
    print "Total records:", count > "/dev/stderr"
    print count    # to stdout
}

# Variables — no declaration; spring into existence
# Dual type: string or number depending on context
# "007" + 0  → 7  (numeric context)
# "007" ""   → "007" (string context)

# Arithmetic
{ result = ($1 + $2) / 2; print result }
{ if ($3 > 100) print $0 }

# String operations
{ print length($1) }        # string length
{ print toupper($1) }       # uppercase
{ print tolower($1) }       # lowercase
{ if ($1 ~ /^[0-9]+/) ... } # regex match with ~
{ if ($1 !~ /error/) ... }  # negated regex

# Associative arrays
{ count[$1]++ }             # count occurrences of field 1
END { for (k in count) print k, count[k] }

# Functions
function max(a, b,    local_tmp) {  # extra params = local vars (AWK trick)
    return (a > b) ? a : b
}
{ print max($1, $2) }

# Control flow
{ if ($1 > 100) print "big"
  else print "small" }

{ for (i = 1; i <= NF; i++) printf "%s ", $i; print "" }

{ while ($1 > 0) { print $1; $1-- } }

# Getline
{ while ((getline line < "other.txt") > 0) print line }

# Multi-file processing
FNR == 1 { print "--- File:", FILENAME }  # FNR resets per file; NR is global

# Output redirection inside AWK
{ print $0 > "output.txt" }   # write (once-open, append for subsequent)
{ print $0 >> "output.txt" }  # always append
{ print $0 | "sort" }          # pipe to command

# Common one-liners (run from shell)
# awk '{print NR, $0}' file             # add line numbers
# awk 'NR%2==0' file                    # print even lines
# awk '{sum+=$1} END{print sum}' file   # sum column 1
# awk -F, '{print $2}' file.csv         # extract CSV column 2
# awk '!seen[$0]++' file                # deduplicate (order-preserving)
# awk 'NR==5' file                      # print line 5
# awk '/start/,/end/' file              # print between patterns (range)
```

---

### Perl Quick Card

```perl
#!/usr/bin/perl
use strict;     # require variable declarations (my/our/local)
use warnings;   # warn on suspicious constructs
use 5.010;      # or: use feature 'say';  enables say, given/when, etc.

# Variables — sigils indicate access mode
my $scalar = "hello";     # scalar: string, number, reference
my @array  = (1, 2, 3);   # array (ordered list)
my %hash   = (a => 1, b => 2);  # hash (associative)

# Scalar
$scalar = 42;
$scalar = "string";
$scalar = 3.14;
print length($scalar), "\n";
print uc($scalar), "\n";       # uppercase
print lc($scalar), "\n";       # lowercase

# String operators (NOT the same as numeric!)
"ab" eq "ab"    # string equality (NOT ==)
"ab" ne "cd"    # string inequality
"ab" lt "cd"    # string less-than
"abc" . "def"   # string concatenation
"x" x 3         # repetition: "xxx"
# Numeric operators: == != > < >= <= + - * / % **

# String interpolation
my $name = "world";
print "Hello, $name!\n";          # interpolates
print 'Hello, $name!\n';          # literal (no interpolation, \n is literal)
print qq(Hello, $name!\n);        # like "..."
print q(Hello, $name!\n);         # like '...'
my @words = qw(one two three);    # quoted word list: ("one","two","three")

# Context system — IMPORTANT
my @arr = (1, 2, 3);
my $count = @arr;         # scalar context: count → 3
my @copy  = @arr;         # list context: copy
print scalar @arr, "\n";  # force scalar context

# Array operations
push @arr, 4;             # append
my $last = pop @arr;      # remove last
unshift @arr, 0;          # prepend
my $first = shift @arr;   # remove first
my @slice = @arr[1..2];   # slice
my @sorted = sort @arr;
my @reversed = reverse @arr;
my @filtered = grep { $_ > 1 } @arr;
my @mapped = map { $_ * 2 } @arr;

# Hash operations
$hash{key} = "value";
my $val = $hash{key};
delete $hash{key};
exists $hash{key};
keys %hash;               # list of keys
values %hash;             # list of values
while (my ($k, $v) = each %hash) { print "$k=$v\n" }

# Arithmetic
$x = 2 ** 10;             # exponentiation (2^10 = 1024)
$x++;  $x--;  $x += 5;

# if/else
if ($x == 5)      { print "equal\n" }
elsif ($x > 5)    { print "greater\n" }
else              { print "less\n" }
unless ($x)       { print "falsy\n" }         # unless = if not
print "yes\n" if $x > 0;                       # postfix form
print "no\n"  unless $x;                       # postfix unless

# Regex
if ($str =~ /^hello/i) { print "matched\n" }   # /i = case-insensitive
if ($str !~ /error/)   { ... }                  # negated match
$str =~ s/old/new/g;                            # substitute (in-place)
$str =~ s/(\w+)/uc($1)/ge;                      # substitute with code /e
my @matches = ($str =~ /(\d+)/g);               # extract all matches

# Loops
foreach my $item (@arr) { print "$item\n" }
for my $item (@arr) { ... }                     # same
for (my $i=0; $i<10; $i++) { ... }             # C-style
while ($condition) { ... }
until ($condition) { ... }
do { ... } while ($condition);
next;    # continue (skip to next iteration)
last;    # break (exit loop)
redo;    # redo current iteration

# Functions
sub my_func {
    my ($arg1, $arg2) = @_;     # @_ = argument list
    my $result = $arg1 . $arg2;
    return $result;
}
my $r = my_func("hello", "world");

# Anonymous subs / closures
my $double = sub { return $_[0] * 2 };
$double->(5);    # → 10; note -> dereference operator

# References
my $aref = \@arr;           # reference to array
my $href = \%hash;          # reference to hash
my $sref = \$scalar;        # reference to scalar
my $cref = sub { ... };     # code reference (anonymous sub)

# Dereference
@{$aref};  $aref->[0];     # array deref
%{$href};  $href->{key};   # hash deref
${$sref};                   # scalar deref
$cref->();                  # code deref

# I/O
print "stdout\n";
say "stdout with newline";    # say = print + \n (use 5.010+)
print STDERR "error\n";
my $line = <STDIN>;
chomp $line;                  # remove trailing newline
while (my $line = <STDIN>) { chomp $line; ... }
open(my $fh, '<', 'file.txt') or die "Can't open: $!";
while (<$fh>) { chomp; print "$_\n" }
close $fh;
open(my $out, '>', 'out.txt') or die $!;
print $out "text\n";

# One-liners (run from shell)
# perl -e 'print "hello\n"'
# perl -p -e 's/foo/bar/g' file.txt        # sed-like: print each line
# perl -n -e 'print if /pattern/' file.txt # grep-like: no auto-print
# perl -i -p -e 's/foo/bar/g' file.txt     # in-place edit (like sed -i)
# perl -i.bak -p -e 's/foo/bar/g' file.txt # in-place with backup

# Exit codes
exit 0;
exit 1;
my $rc = system("git status");   # system() returns exit code * 256
$rc >> 8;                        # actual exit code
$rc == 0 or die "git failed: $!";

# Error handling
use autodie;                     # die on failed open/system/etc. automatically
eval { die "something\n" };
if ($@) { print "caught: $@" }  # $@ = last exception

# Common modules
use File::Basename;   # dirname, basename
use File::Path;       # make_path, remove_tree
use Cwd;              # getcwd, abs_path
use POSIX;            # floor, ceil, strftime
use List::Util qw(sum min max first reduce);
use Scalar::Util qw(looks_like_number blessed reftype);
use Data::Dumper;     # debug: print Dumper(\@arr);
```

---

## Quick Reference: Feature Gap Summary

| Feature              | Batch | PS   | Bash | sh   | Zsh  | Fish | AWK  | Perl |
|----------------------|-------|------|------|------|------|------|------|------|
| Real arrays          | No    | Yes  | Yes  | No   | Yes  | Yes  | Assoc| Both |
| Assoc arrays         | No    | Yes  | 4.0+ | No  | Yes  | No   | Yes  | Yes  |
| Float arithmetic     | No    | Yes  | No   | No   | Yes  | Yes  | Yes  | Yes  |
| Regex built-in       | No    | Yes  | `=~` | No  | `=~` | `str`| `~`  | Yes  |
| try/catch            | No    | Yes  | No   | No   | No   | No   | No   | eval |
| Typed variables      | No    | .NET | weak | No  | weak | No   | No   | No   |
| Object model         | No    | .NET | No   | No   | No   | No   | No   | Yes  |
| First-class functions| No    | Yes  | No   | No   | No   | No   | No   | Yes  |
| Array index base     | 0(ish)| 0    | 0    | N/A  | 1    | 1    | N/A  | 0    |
| POSIX compatible     | No    | No   | Super| Yes  | Super| No   | Yes  | N/A  |
| Interactive shell    | Yes   | Yes  | Yes  | No   | Yes  | Yes  | No   | No   |
