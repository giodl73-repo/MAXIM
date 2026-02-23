# Scripting: Batch (CMD)

> Windows' original automation language. Ugly, fragile, irreplaceable in some Windows contexts. Knowing the traps is 80% of knowing Batch.

---

## Language Snapshot

| Attribute | Value |
|-----------|-------|
| Platform | Windows only (cmd.exe) |
| Extension | `.bat`, `.cmd` |
| Shebang | None (cmd.exe is implicit) |
| Paradigm | Imperative, sequential, GOTO-based |
| Typing | Strings only (`SET /A` for integer arithmetic) |
| Execution | cmd.exe interpreter; no compilation |

---

## The Core Weirdness — cmd.exe Parsing Order

```
cmd.exe processes each line in this fixed order:

  1. Variable expansion       %var%  resolved BEFORE anything else
  2. Special char parsing     & | < > ( ) ^ resolved
  3. FOR/IF block recognition
  4. Command execution
  5. Delayed expansion        !var!  resolved HERE (only with ENABLEDELAYEDEXPANSION)

Why this matters:
  SETLOCAL ENABLEDELAYEDEXPANSION
  SET count=0
  FOR %%f IN (*.txt) DO (
    SET /A count+=1
    ECHO %count%   ← WRONG: always prints 0 — expanded at parse time, not loop time
    ECHO !count!   ← RIGHT: expanded at execution time, inside the loop
  )

This single expansion-order quirk explains ~70% of Batch mysteries.
```

---

## Syntax Reference Card

### Variables

```batch
@ECHO OFF                         :: suppress command echo — always first line
SETLOCAL                          :: localize variable changes to this script
SETLOCAL ENABLEDELAYEDEXPANSION   :: required for !var! inside FOR/IF blocks

SET name=hello                    :: assign (NO SPACES around = !)
SET "name=hello world"            :: safer form — handles spaces in value
ECHO %name%                       :: expand
ECHO !name!                       :: expand inside FOR/IF with delayed expansion

SET /A count=0                    :: integer variable
SET /A count+=1                   :: increment
SET /A result=2*3+4               :: arithmetic expression

SET /P answer=Enter value:        :: read from user (prompt, no newline)

:: Substring / replace
ECHO %name:~0,5%                  :: chars 0–4 (first 5)
ECHO %name:~-3%                   :: last 3 chars
ECHO %name:hello=world%           :: replace "hello" with "world"

:: Critical special variables
ECHO %~dp0                        :: directory of current script (ends with \)
ECHO %~nx0                        :: name.ext of current script
ECHO %CD%                         :: current working directory
ECHO %ERRORLEVEL%                 :: last external command exit code
ECHO %TIME% %DATE%
ECHO %TEMP%
ECHO %COMPUTERNAME% %USERNAME% %USERDOMAIN%
```

### String Quoting

```batch
:: No single-quote string literal — only double quotes
SET "msg=hello world"            :: quotes define value boundary; not stored in value
ECHO "%msg%"                     :: quoted: & | < > treated as literals
ECHO %msg%                       :: unquoted: dangerous if msg contains & | < >

:: Escaping special chars with ^ (caret) — only outside double quotes
ECHO 1 ^& 2                      :: ^ escapes &
ECHO 1 ^| 2                      :: ^ escapes |
ECHO 1 ^> file                   :: ^ escapes >
ECHO ^<xml^>                     :: ^ escapes < >
ECHO line1^
line2                            :: ^ at end-of-line = line continuation

:: Inside "double quotes" — special chars are literal, ^ does NOT escape
ECHO "Hello & World"             :: & is safe here without ^

:: TRAP: delayed expansion and ! in strings
:: With ENABLEDELAYEDEXPANSION, literal ! must be escaped as ^^!
ECHO It^^!s a trap                :: prints: It!s a trap
```

### Arrays (Simulated)

```batch
:: Batch has no array type. Two practical workarounds:

:: Method 1: numbered variable names
SET arr[0]=apple
SET arr[1]=banana
SET arr[2]=cherry

SETLOCAL ENABLEDELAYEDEXPANSION
FOR /L %%i IN (0,1,2) DO ECHO !arr[%%i]!

:: Method 2: space-separated list with FOR
SET list=apple banana cherry
FOR %%i IN (%list%) DO ECHO %%i

:: Counting items — no built-in; track manually
SET count=0
FOR %%i IN (%list%) DO SET /A count+=1

:: TRAP: items with spaces break Method 2 entirely
:: Use Method 1 (indexed vars) when items can contain spaces
```

### Arithmetic

```batch
SET /A result=2+3*4              :: 14 (standard precedence)
SET /A result=2*(3+4)            :: 14
SET /A x=10/3                    :: 3 (integer division — no float!)
SET /A x=10%%3                   :: 1 (modulo — %% in .bat, % in interactive cmd)
SET /A "hex=0xFF"                :: hex literal
SET /A "oct=010"                 :: octal literal (leading zero = octal)

:: No float. Delegate to PowerShell:
FOR /F %%r IN ('powershell -NoProfile -Command "1.5 * 2.5"') DO SET result=%%r
```

### Conditionals

```batch
:: String comparison
IF "%var%"=="hello" (ECHO match) ELSE (ECHO no match)
IF /I "%var%"=="HELLO" ECHO case-insensitive    :: /I flag
IF NOT "%var%"=="hello" ECHO not hello

:: Numeric comparison — use these keywords, NOT operators
:: EQU NEQ LSS LEQ GTR GEQ
IF %count% GTR 5 ECHO greater
IF %count% EQU 0 ECHO zero

:: File/path existence
IF EXIST file.txt ECHO file exists
IF EXIST "dir\" ECHO is a directory     :: trailing \ tests for directory
IF NOT EXIST "%output_dir%" MKDIR "%output_dir%"

:: Variable defined
IF DEFINED myvar ECHO defined
IF NOT DEFINED myvar ECHO not defined

:: Exit code — ERRORLEVEL trap
somecommand.exe
IF ERRORLEVEL 1 ECHO failed           :: TRUE if exit code >= 1
IF %ERRORLEVEL% EQU 1 ECHO exactly 1  :: TRUE only if == 1
:: For specific codes, check from highest to lowest:
IF ERRORLEVEL 3 GOTO code3
IF ERRORLEVEL 2 GOTO code2
IF ERRORLEVEL 1 GOTO code1

:: Multiline syntax
IF condition (
    ECHO line1
    ECHO line2
) ELSE (
    ECHO other
)
```

### switch/case (No Built-in — Patterns)

```batch
:: No switch/case. Two patterns:

:: Pattern 1: IF-ELSE chain
SET choice=B
IF "%choice%"=="A" (ECHO chose A) ELSE IF "%choice%"=="B" (ECHO chose B) ELSE ECHO other

:: Pattern 2: GOTO dispatch table (cleaner for many cases)
IF "%choice%"=="A" GOTO do_a
IF "%choice%"=="B" GOTO do_b
IF "%choice%"=="C" GOTO do_c
GOTO unknown

:do_a
ECHO chose A
GOTO end_choice
:do_b
ECHO chose B
GOTO end_choice
:do_c
ECHO chose C
GOTO end_choice
:unknown
ECHO unknown choice
:end_choice
```

### Loops

```batch
:: FOR over literal list
FOR %%i IN (a b c) DO ECHO %%i

:: FOR over files (wildcards)
FOR %%f IN (*.txt) DO ECHO %%f
FOR %%f IN ("C:\path\*.log") DO ECHO %%~f    :: %%~f strips quotes

:: FOR /L — numeric range  (start, step, end)  inclusive
FOR /L %%i IN (1,1,10) DO ECHO %%i
FOR /L %%i IN (10,-1,0) DO ECHO %%i          :: countdown

:: FOR /F — parse command output
FOR /F "tokens=1,2 delims=," %%a IN (data.csv) DO ECHO %%a %%b
FOR /F "tokens=*" %%a IN ('dir /b *.txt') DO ECHO %%a
FOR /F "usebackq tokens=*" %%a IN (`command`) DO ...     :: backtick in usebackq mode
FOR /F "skip=1 tokens=2" %%a IN (file.txt) DO ECHO %%a  :: skip header line

:: FOR /D — directories only
FOR /D %%d IN (*) DO ECHO %%d

:: FOR /R — recursive (walk subtree)
FOR /R "C:\path" %%f IN (*.log) DO ECHO %%f

:: WHILE simulation — Batch has no while keyword
SET /A i=0
:while_loop
IF %i% GEQ 10 GOTO while_end
ECHO %i%
SET /A i+=1
GOTO while_loop
:while_end
```

### Functions / Subroutines

```batch
:: CALL :label executes a labeled section as a subroutine
CALL :my_func hello world
ECHO Return value: %result%
GOTO :EOF        :: skip over subroutine definitions when running top-to-bottom

:my_func
:: Parameters arrive as %1, %2, ...
SET param1=%~1   :: %~1 strips surrounding quotes from argument
SET param2=%~2
:: No formal return — communicate via SET
SET result=%param1%_%param2%
EXIT /B 0        :: CRITICAL: EXIT /B returns from subroutine
                 :: plain EXIT closes the entire cmd.exe session!

:: %~N modifier reference for arguments and FOR variables:
::   %~f1  fully qualified path
::   %~d1  drive letter only (C:)
::   %~p1  path only (\some\dir\)
::   %~n1  name without extension
::   %~x1  extension (.txt)
::   %~dp1 drive + path = directory (most useful — equivalent of %~dp0 for args)
```

### I/O and Redirection

```batch
ECHO Hello World             :: stdout
ECHO Error message >&2       :: stderr
ECHO.                        :: blank line — ECHO. not "ECHO " (space)
TYPE file.txt                :: cat equivalent
MORE file.txt                :: paged output

:: Redirection
command > out.txt            :: stdout → file (overwrite)
command >> out.txt           :: stdout → file (append)
command 2> err.txt           :: stderr → file
command 2>&1                 :: redirect stderr to stdout
command > out.txt 2>&1       :: both streams → file
command > NUL                :: discard stdout  (NUL not /dev/null)
command > NUL 2>&1           :: discard everything

:: Pipes
dir /b | FIND "txt"
TYPE file.txt | FINDSTR /I "error"

:: Read file line by line
FOR /F "usebackq delims=" %%l IN ("file.txt") DO ECHO %%l
```

### Exit Codes and Error Handling

```batch
:: Exit code from this script
EXIT /B 0        :: success
EXIT /B 1        :: error

:: Check after external command
someapp.exe
IF ERRORLEVEL 1 (
    ECHO Failed with code %ERRORLEVEL%
    EXIT /B 1
)

:: Conditional execution operators
command1 && command2    :: cmd2 only if cmd1 succeeded (ERRORLEVEL 0)
command1 || GOTO err    :: jump if cmd1 failed

:: Batch has no try/catch — structure with GOTO
:err
ECHO Something failed
EXIT /B 1
```

### Script Arguments

```batch
ECHO Script:  %0           :: full script path as invoked
ECHO Arg 1:   %1
ECHO Arg 2:   %2
ECHO All args: %*           :: all args as single string

:: Validate required argument
IF "%1"=="" (ECHO Usage: %~nx0 ^<name^> & EXIT /B 1)

:: SHIFT — move argument window
SHIFT                       :: %2 becomes %1, %3 becomes %2, etc.

:: Parse named flags manually
:parse_args
IF "%1"=="" GOTO args_done
IF /I "%1"=="/name"    (SET name=%2    & SHIFT & SHIFT & GOTO parse_args)
IF /I "%1"=="/verbose" (SET verbose=1  & SHIFT          & GOTO parse_args)
SHIFT & GOTO parse_args     :: skip unknown flag
:args_done
```

### Common Patterns

```batch
:: Get script's own directory — use this everywhere for relative paths
SET SCRIPT_DIR=%~dp0
SET CONFIG=%SCRIPT_DIR%config.ini
SET LOG=%SCRIPT_DIR%logs\output.log

:: Check if running as administrator
NET SESSION >NUL 2>&1
IF %ERRORLEVEL% NEQ 0 (ECHO Requires elevation & EXIT /B 1)

:: Create directory if absent
IF NOT EXIST "%output_dir%" MKDIR "%output_dir%"

:: Delete file if present
IF EXIST "temp.txt" DEL /Q "temp.txt"

:: Invoke PowerShell and capture result
FOR /F %%r IN ('powershell -NoProfile -Command "Get-Date -Format yyyy-MM-dd"') DO SET today=%%r

:: Timestamp for log file names (via WMIC — deprecated Win11 but widely available)
FOR /F "tokens=2 delims==" %%i IN ('wmic OS get LocalDateTime /value') DO SET dt=%%i
SET timestamp=%dt:~0,8%_%dt:~8,6%
```

---

## What Makes It Distinct

```
Batch is not a designed language — it evolved from CP/M's SUBMIT.COM
and COMMAND.COM's interactive mode. The "design" decisions are
archaeological artifacts, not intentional choices.

Key architectural facts:

  cmd.exe is a single-pass line processor, not a tree-based interpreter.
  There is no AST. Commands are tokenized and dispatched sequentially.
  Control flow (GOTO, FOR, IF) is bolted onto a system designed for
  interactive one-liners, which is why:

  ┌────────────────────────────────────────────────────────┐
  │  Feature         │  Why it works the way it does       │
  ├────────────────────────────────────────────────────────┤
  │  %var% expansion │  Done before line execution         │
  │  !var! expansion │  Bolted on later — needs opt-in     │
  │  GOTO :EOF       │  :EOF is a magic virtual label       │
  │  EXIT /B         │  /B added later to fix EXIT bug      │
  │  FOR %%i syntax  │  % used by both vars and for-vars;  │
  │                  │  %% in script avoids collision       │
  │  No arrays       │  SET is a flat key-value store       │
  │  No floats       │  SET /A added after the fact         │
  └────────────────────────────────────────────────────────┘

The key mental model: Batch is line-oriented macro expansion,
not a programming language runtime. Think of it closer to a
sophisticated .cmd text substitution system.
```

---

## Ecosystem

| Tool | Unix analog | Notes |
|------|-------------|-------|
| `FINDSTR` | `grep` | Limited POSIX-ish regex; `-R` for recursive |
| `FIND` | `grep -F` | Fixed-string search; simpler than FINDSTR |
| `XCOPY` | `cp -r` | Recursive copy with filtering |
| `ROBOCOPY` | `rsync` | Mirror, retry, bandwidth throttle — powerful |
| `SORT` | `sort` | Sort stdin/file |
| `WHERE` | `which` | Find executable on PATH |
| `TIMEOUT` | `sleep` | Wait N seconds |
| `CHOICE` | (none) | Interactive keypress menu |
| `WMIC` | (none) | WMI queries — deprecated Win11; use PS |
| `REG` | (none) | Registry CRUD from command line |
| `SCHTASKS` | `cron` | Task Scheduler management |
| `SC` | `systemctl` | Service control |
| `NET` | (none) | User/share/service management |
| `TASKLIST` / `TASKKILL` | `ps` / `kill` | Process enumeration/termination |

---

## Gotchas and Traps

| Trap | Issue | Fix |
|------|-------|-----|
| Spaces in `SET` | `SET name = hello` stores `name ` (with space) as key | `SET "name=hello"` — always quote the whole assignment |
| `%ERRORLEVEL%` in IF block | Expanded before IF executes; reads stale value | Use `IF ERRORLEVEL n` form, or `(CALL)` trick to force re-read |
| `EXIT` vs `EXIT /B` | Bare `EXIT` terminates the cmd.exe process/window | Always `EXIT /B` in scripts and subroutines |
| Delayed expansion off | `!var!` inside FOR loop reads stale `%var%` | `SETLOCAL ENABLEDELAYEDEXPANSION` at script top |
| `!` literals with delayed expansion | Literal `!` treated as variable delimiter | Escape as `^^!` or use `SETLOCAL DISABLEDELAYEDEXPANSION` around that block |
| `%%` vs `%` for loop vars | In .bat files: `%%i`; in interactive cmd: `%i` | Always `%%i` in scripts |
| Paths with spaces in FOR | `FOR %%f IN (*.txt)` breaks on `my file.txt` | Always quote expansion: `"%%f"` and use `%%~f` to strip quotes |
| `ECHO.` vs `ECHO ` | `ECHO ` (trailing space) may echo "ECHO is on" | Always `ECHO.` for blank line |
| Octal trap in `SET /A` | `SET /A x=010` → 8 (octal) not 10 | Strip leading zeros from user-supplied numbers |
| `ERRORLEVEL` semantics | `IF ERRORLEVEL 1` is `>= 1`, catches 1,2,3,... | Check from highest to lowest for specific code testing |
| Nested parentheses | `(` and `)` in variable values break IF/FOR blocks | Quote values: `SET "val=a(b)"` and use delayed expansion |

---

## Bridge to Unix/Bash

| Batch | Bash | PowerShell |
|-------|------|-----------|
| `%var%` | `$var` | `$var` |
| `SET var=val` | `var=val` | `$var = val` |
| `ECHO %ERRORLEVEL%` | `echo $?` | `$LASTEXITCODE` |
| `FOR /F %%i IN ('cmd')` | `for i in $(cmd)` | `foreach ($i in (cmd))` |
| `IF EXIST file` | `[[ -f file ]]` | `Test-Path file` |
| `IF EXIST "dir\"` | `[[ -d dir ]]` | `Test-Path dir -PathType Container` |
| `> NUL` | `> /dev/null` | `> $null` or `\| Out-Null` |
| `2>&1` | `2>&1` | `2>&1` |
| `EXIT /B 0` | `exit 0` | `exit 0` |
| `%~dp0` | `$(dirname "$0")` | `$PSScriptRoot` |
| `CALL :func` | `func_name` | `function Func { }` |
| `SETLOCAL` | subshell `( )` or `local` | (scoped by default) |
| `GOTO label` | (no equivalent) | (no equivalent) |
| `SET /A x=x+1` | `(( x++ ))` or `x=$((x+1))` | `$x++` |
| `FINDSTR /I "pat" file` | `grep -i "pat" file` | `Select-String -Pattern "pat"` |
| `ROBOCOPY src dst /MIR` | `rsync -av --delete src/ dst/` | `Robocopy` (still available in PS) |
| `FOR /R %%f IN (*.txt)` | `find . -name "*.txt"` | `Get-ChildItem -Recurse -Filter "*.txt"` |
| `%%~dpf` modifiers | `$(dirname ...)` / `$(basename ...)` | `Split-Path`, `[IO.Path]::Get*` |

---

## Decision Cheat Sheet

| Use Batch when... | Use something else when... |
|-------------------|---------------------------|
| Legacy `.bat` scripts already exist and must not change | Anything new on Windows — prefer PowerShell |
| Calling environment guarantees cmd.exe only, no PS | Need float math, real arrays, or structured error handling |
| Simple `.bat` launcher that bootstraps a PS/Python script | Need to process JSON, XML, or structured data |
| CI/CD agent where only cmd.exe is available | Need portability beyond Windows |
| Quick file ops: copy, move, delete, call exe | Script complexity exceeds ~20 lines |

> Rule of thumb: Write in PowerShell. Wrap in a `.bat` launcher only when the caller is cmd.exe and cannot run `pwsh`. A one-line `.bat` that does `@powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0script.ps1" %*` is the standard escape hatch.
