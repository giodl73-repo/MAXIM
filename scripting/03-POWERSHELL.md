# Scripting: PowerShell

> .NET-native shell where the pipeline moves objects, not text. The fundamental difference from every Unix shell — and from Batch.

```
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│  POWERSHELL ECOSYSTEM MAP                                                                 │
│                                                                                           │
│  ┌──────────────────────────────────┐   ┌──────────────────────────────────────────────┐ │
│  │  Windows PowerShell 5.1          │   │  PowerShell 7.x (pwsh)                       │ │
│  │  powershell.exe                  │   │  Install: winget / GitHub releases / MSI      │ │
│  │  Runtime: .NET Framework 4.x     │   │  Runtime: .NET 8+                             │ │
│  │  Ships with Windows — always     │   │  Windows / Linux / macOS                      │ │
│  │  present, never updated          │   │  Actively developed; new features land here   │ │
│  └──────────────┬───────────────────┘   └──────────────────┬───────────────────────────┘ │
│                 │                                           │                              │
│       Legacy / Windows-only APIs               Cross-platform + modern syntax             │
│                 │                                           │                              │
│  ┌──────────────▼───────────────────────────────────────────▼───────────────────────────┐ │
│  │  HOSTING ENVIRONMENTS                                                                  │ │
│  │                                                                                        │ │
│  │  Interactive                  Scripted / Automated                                     │ │
│  │  ─────────────────────        ───────────────────────────────────────────────────────  │ │
│  │  Windows Terminal             Azure Pipelines  — AzurePowerShell@5 task (pre-authed)   │ │
│  │  VS Code integrated           GitHub Actions   — shell: pwsh step                      │ │
│  │  Windows Terminal             Azure Functions  — PowerShell runtime (isolated process)  │ │
│  │  PowerShell ISE (5.1 only)    Azure Automation — runbooks (hosted PS 7 or 5.1)         │ │
│  │  SSH remote sessions          Docker containers — mcr.microsoft.com/powershell image   │ │
│  └────────────────────────────────────────────────────────────────────────────────────────┘ │
│                                                                                           │
│  ┌─────────────────────────────────────────────────────────────────────────────────────┐  │
│  │  MODULE ECOSYSTEM LAYERS                                                              │  │
│  │                                                                                       │  │
│  │  4. Private feed / internal modules    ← NuGet / Azure Artifacts feed               │  │
│  │  3. Az.* (Azure SDK modules)           ← PSGallery; sub-modules by service area     │  │
│  │  2. Community modules                  ← PSGallery (Pester, dbatools, PSReadLine…)  │  │
│  │  1. Built-in modules                   ← Ship with Windows (ActiveDirectory, CIM…)  │  │
│  │                                                                                       │  │
│  │  PSModulePath controls search order    ← $env:PSModulePath (colon-separated dirs)   │  │
│  │  Autoloading: PS 3+ discovers modules automatically when a command is typed         │  │
│  └─────────────────────────────────────────────────────────────────────────────────────┘  │
│                                                                                           │
│  ┌─────────────────────────────────────────────────────────────────────────────────────┐  │
│  │  EXECUTION POLICY (Windows only — not a security boundary, a convenience guardrail) │  │
│  │                                                                                       │  │
│  │  Restricted      — no scripts (default on client Windows)                           │  │
│  │  RemoteSigned     — local scripts OK; downloaded scripts need signature             │  │
│  │  Unrestricted    — all scripts, warns on downloaded                                 │  │
│  │  Bypass           — no checking at all (use in CI/CD: -ExecutionPolicy Bypass)      │  │
│  │                                                                                       │  │
│  │  Scope precedence (highest wins):                                                     │  │
│  │  MachinePolicy > UserPolicy > Process > CurrentUser > LocalMachine                  │  │
│  │  Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass   ← CI-safe             │  │
│  └─────────────────────────────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## Language Snapshot

| Attribute | Value |
|-----------|-------|
| Platform | Windows built-in: PS 5.1 (`powershell.exe`) / Cross-platform: PS 7 (`pwsh`) |
| Extension | `.ps1` |
| Shebang | `#!/usr/bin/env pwsh` (Linux/Mac only; Windows ignores it) |
| Paradigm | Object-oriented, pipeline-first, imperative |
| Typing | Dynamic with optional .NET type annotations; full CLR type system |
| Execution | Compiled to CIL, run on .NET CLR — not text-interpreted like Bash/Batch |

---

## The Core Insight — Object Pipeline

```
Unix shell pipeline:
  cmd1  ──text──►  cmd2  ──text──►  cmd3
                   parses            parses
                   previous          previous
                   text output       text output

  Every stage re-parses. grep/awk/cut are text parsers gluing stages together.
  Column positions are implicit contracts. Format changes break everything.

PowerShell pipeline:
  Cmdlet1  ──objects──►  Cmdlet2  ──objects──►  Cmdlet3
           Process[]      filters by             projects
                          .CPU property          .Name, .Id

  No parsing. Objects carry named, typed properties. The schema is explicit.
  Get-Member gives you the full property/method list at any point.

  Get-Process | Where-Object CPU -gt 100 | Sort-Object CPU -Desc | Select-Object Name,CPU -First 10

  vs Bash (must know ps aux column layout, fragile on different distros):
  ps aux | awk 'NR>1 {print $3, $11}' | sort -rn | head -10

Consequence: awk/cut/grep are rarely needed in PS.
The object model also enables: Export-Csv, ConvertTo-Json, Compare-Object,
Group-Object, Measure-Object — all operating on structured data, not text.
```

---

## PS 5.1 vs PS 7 — Know Which You're On

```
Windows built-in:   powershell.exe  = Windows PowerShell 5.1
Cross-platform:     pwsh            = PowerShell 7.x (install separately)

Key differences:
  Feature                   PS 5.1          PS 7+
  ─────────────────────────────────────────────────────
  Ternary  $x ? a : b       no              yes
  Null coalesce  ??          no              yes
  Null assign   ??=          no              yes
  -split, -join pipeline     limited         better
  Default encoding           UTF-16 LE       UTF-8
  Linux/Mac support          no              yes
  ForEach-Object -Parallel   no              yes
  $IsWindows, $IsLinux       no              yes
  Pipeline chain operators   no              yes (&&, ||)

In CI/CD: explicitly invoke pwsh or powershell.exe depending on what's installed.
In new scripts: target PS 7. $PSVersionTable.PSVersion.Major tells you which.
```


### .NET Runtime Backing — Why It Matters

```
PS 5.1  →  .NET Framework 4.x
  - Windows-only CLR
  - Assembly resolution from GAC + Framework dirs
  - Some COM interop available directly
  - Modules that P/Invoke Windows APIs or use Framework-only types work fine here
  - Will never get new language features

PS 7.x  →  .NET 8+ (formerly .NET Core)
  - Cross-platform CLR
  - Assembly resolution from NuGet paths / runtimeconfig.json
  - Some Framework-only modules break (WMI, some AD cmdlets, old SSMS modules)
  - Faster startup, better performance, ongoing investment

Module compatibility consequence:
  A module that ships a .NET Framework DLL (targets net4x) may fail to load in PS 7
  because the .NET 8 runtime refuses to load Framework assemblies in all cases.
  Check module compatibility: Import-Module Foo -Verbose  → watch for type load errors
```

### Windows Compatibility Layer (PS 7)

```powershell
# For PS 5.1-only modules that don't work natively in PS 7,
# the WindowsCompatibility shim creates an implicit PS 5.1 runspace
# in the background and proxies calls to it.

Install-Module WindowsCompatibility
Import-WinModule ActiveDirectory               # load via compat layer
Import-Module ActiveDirectory -UseWindowsPowerShell  # same thing, built-in PS 7.1+

# What it does under the hood:
#   Spins up a background PS 5.1 session
#   Creates proxy functions in the PS 7 session that forward calls
#   Return values are deserialized (same as remoting — methods lost)

# Caveats:
#   - Requires Windows (uses powershell.exe under the hood)
#   - Proxy objects are PSCustomObject, not the real types
#   - Not all modules compat-shim cleanly (anything with custom UI or complex types)
```

### ForEach-Object -Parallel — Runspace Isolation

```powershell
# Each -Parallel block runs in a SEPARATE runspace (not a thread in shared state).
# Variables from the outer scope are NOT visible inside.

$threshold = 100
Get-Process | ForEach-Object -Parallel {
    # $threshold is NOT available here — different runspace
    if ($_.CPU -gt $threshold) { $_.Name }   # WRONG: $threshold = $null
}

# Fix: $using: scope modifier copies the value into the runspace
$threshold = 100
Get-Process | ForEach-Object -Parallel {
    if ($_.CPU -gt $using:threshold) { $_.Name }   # correct
} -ThrottleLimit 10

# Implications:
#   - No shared mutable state — you cannot update $results from inside -Parallel
#   - Collect return values from the pipeline instead
#   - $using: is read-only copy — modifications inside don't propagate out
#   - For true shared state (counters), use [System.Collections.Concurrent.ConcurrentBag[object]]
#     passed via $using:

$bag = [System.Collections.Concurrent.ConcurrentBag[object]]::new()
1..20 | ForEach-Object -Parallel {
    ($using:bag).Add("result from $_")
} -ThrottleLimit 5
$bag.Count   # 20
```

### Pipeline Chain Operators — &&, || in PS 7

```powershell
# && and || in PS 7 operate on $LASTEXITCODE, NOT on $?
# This is the non-obvious part: they are for EXTERNAL executables.

git fetch && git merge && git push    # stops if any external tool returns non-zero
git pull || throw "pull failed"       # throws if git pull fails

# $LASTEXITCODE is what drives these operators.
# PowerShell cmdlet success/failure ($?) does NOT feed into && / ||.

# Test this:
function Fail-Cmdlet { throw "oops" }
Fail-Cmdlet && Write-Host "won't stop here?"   # && still runs because $LASTEXITCODE is 0

# Practical rule:
#   &&/|| for chaining native binaries (git, npm, dotnet, docker, etc.)
#   try/catch for chaining PS cmdlets
#   Mix both when your script calls external tools AND PS cmdlets
```

---

## Syntax Reference Card

### Variables

```powershell
$name = "hello"              # assign (space around = is idiomatic — opposite of Batch!)
$x = 42
[string]$typed = "hello"     # type-annotated; enforced on assignment
[int]$count = 0

# Common type accelerators:
# [string] [int] [double] [bool] [datetime] [array] [hashtable]
# [System.Collections.ArrayList] [System.Collections.Generic.List[string]]
# Coercion is automatic; explicit annotation enforces it and self-documents intent

$null                        # null value (not NULL, None, nil)
$true   $false               # booleans (capitalized; not Python's True/False)

# Scope qualifiers
$script:var                  # script scope
$global:var                  # global scope
$local:var                   # local scope (default)
$env:PATH                    # environment variable via the Env: drive

# The critical automatic variables
$_   /   $PSItem             # current pipeline object (inside Where-Object, ForEach-Object)
$?                           # bool: did the last PS cmdlet/function succeed?
$LASTEXITCODE                # int: exit code of the last EXTERNAL executable (git, node, etc.)
$Error[0]                    # ErrorRecord: most recent error object
$PSScriptRoot                # directory of the currently running script
$PSCommandPath               # full path of the currently running script
$args                        # array of args when no param() block declared
$MyInvocation                # InvocationInfo: how this was called
$PSVersionTable              # version hashtable: $PSVersionTable.PSVersion.Major
$PSBoundParameters           # hashtable of params explicitly passed to current function

# $? vs $LASTEXITCODE — the most important distinction in the whole language
git push            # external command
$?                  # TRUE — PS successfully launched git (says nothing about git's result)
$LASTEXITCODE       # 1 — git's actual exit code
# You MUST check $LASTEXITCODE after any external tool call
```

### String Quoting

```powershell
'no $interpolation here'          # single-quoted literal
"$name interpolated"              # double-quoted; $var expands
"result: $(1 + 2 * 3)"            # $() for arbitrary expressions in strings
"$($obj.Property)"                # property access inside string requires $()

# Here-strings — multiline, preserves newlines literally
$text = @"
Line one, $name is interpolated.
Line two.
"@    # CRITICAL: closing @" must be at column 0 (no leading whitespace)

$literal = @'
No $interpolation.
'@

# String operators (no method call required for these common ops)
"hello world" -replace "world", "PS"   # → "hello PS"  (regex by default)
"a::b::c"     -split "::"              # → @("a", "b", "c")
@("a","b","c") -join ", "              # → "a, b, c"
"hello"        -like "h*llo"           # wildcard match → $true
"hello"        -match "^h(\w+)o$"      # regex match; populates $Matches → $true
$Matches[0]    # "hello"
$Matches[1]    # "ell"

# Case sensitivity: default is insensitive
"Hello" -eq "hello"    # true
"Hello" -ceq "hello"   # false (c prefix = case-sensitive: -ceq -cne -clt etc.)
"Hello" -ieq "hello"   # true  (i prefix = explicit insensitive — redundant, documents intent)

# Format operator: -f
"{0} has {1} items" -f $name, $count
"{0:N2}" -f 1234.5678              # "1,234.57"
"{0:yyyy-MM-dd}" -f (Get-Date)     # "2026-02-22"
"{0:X8}" -f 255                    # "000000FF" (hex, 8 digits)
```

### Arrays and Lists

```powershell
$a = @(1, 2, 3)                    # explicit array literal
$a = 1, 2, 3                       # comma operator creates array — @() not required
$a = @()                           # empty array

$a[0]                              # first element (0-indexed)
$a[-1]                             # last element
$a[1..3]                           # slice: elements at indices 1,2,3
$a.Count  /  $a.Length             # length

# TRAP: += creates a NEW array — O(n) for each append
$a += 4                            # slow for large collections

# For frequent appends use ArrayList:
$list = [System.Collections.ArrayList]@()
[void]$list.Add("item")            # [void] suppresses the index return value
$list.Remove("item")
$list.Count

# Array manipulation
$a | Where-Object { $_ -gt 2 }     # filter (returns matching elements)
$a | ForEach-Object { $_ * 2 }     # map (transform each element)
$a -contains 2                      # membership test ($true/$false)
$a -notcontains 99
[array]::Sort($a)                   # in-place sort via .NET

# Hashtable (dictionary — preserve insertion order with [ordered])
$h = @{ name = "Alice"; age = 42 }
$h = [ordered]@{ a = 1; b = 2; c = 3 }   # preserves declaration order
$h["name"]    /    $h.name          # two equivalent access syntaxes
$h.Keys       /    $h.Values
$h.ContainsKey("name")
$h.Remove("age")
$h["new"] = "added"
$h.name = "Bob"
```

### Arithmetic

```powershell
1 + 2 * 3          # 7
10 / 3             # 3.3333... (PS returns double — unlike Batch which truncates)
[int](10 / 3)      # 3 (explicit floor/truncation via cast)
10 % 3             # 1 modulo
2 ** 3             # 8 (PS 7+; use [Math]::Pow(2,3) on PS 5.1)

[Math]::Round(3.567, 2)    # 3.57
[Math]::Floor(3.9)         # 3
[Math]::Ceiling(3.1)       # 4
[Math]::Abs(-5)            # 5
[Math]::Sqrt(16)           # 4

$x++   $x--   $x += 5   $x -= 3   $x *= 2
```

### Conditionals

```powershell
# Comparison operators — NOT ==, !=, >, <  (those mean redirection/etc.)
-eq   -ne   -gt   -lt   -ge   -le     # value comparison (case-insensitive for strings)
-ceq  -cne  -cgt  -clt  -cge  -cle   # case-sensitive variants

-like    -notlike                      # wildcard: * ? [abc]
-match   -notmatch                     # regex; -match populates $Matches
-contains   -notcontains               # $collection -contains $item
-in         -notin                     # $item -in $collection

if ($x -eq 5) {
    "five"
} elseif ($x -gt 5) {
    "more"
} else {
    "less"
}

# Ternary (PS 7+)
$label = $x -gt 5 ? "big" : "small"

# Null coalescing (PS 7+)
$val = $x ?? "default"               # use default if $x is null
$x ??= "default"                     # assign only if $x is currently null

# TRAP: $null comparisons — always put $null on the LEFT
if ($null -eq $x)   { }   # safe — explicit null check
if ($x -eq $null)   { }   # dangerous if $x is an array — can produce wrong results

# Path tests
if (Test-Path $path)                               { }   # exists (file or dir)
if (Test-Path $path -PathType Leaf)               { }   # file
if (Test-Path $path -PathType Container)          { }   # directory
```

### switch

```powershell
# Basic switch — all matching cases run (unlike C#'s implicit break)
switch ($x) {
    "a"               { "got a" }
    "b"               { "got b" }
    { $_ -gt 100 }    { "large number (expression match)" }
    default           { "other" }
}

# Use break to stop after first match (C#-style)
switch ($x) {
    "a" { "got a"; break }
    "b" { "got b"; break }
}

# Regex switch
switch -Regex ($x) {
    "^error"   { "error line: $_" }
    "^warn"    { "warning: $_" }
    "\d+"      { "contains number" }
}

# Wildcard switch
switch -Wildcard ($x) {
    "err*"   { "error variant" }
    "warn*"  { "warning variant" }
}

# switch over array — iterates and tests each element
switch ($array) {
    "target" { "found target at index $($array.IndexOf($_))" }
}

# switch -File — iterate lines of a file (memory-efficient)
switch -Regex -File "large.log" {
    "ERROR" { $errorCount++ }
    "WARN"  { $warnCount++ }
}
```

### Loops

```powershell
# foreach statement — loads all items into memory first
foreach ($item in $collection) { $item }

# ForEach-Object cmdlet — streams one at a time (better for large/pipeline data)
$collection | ForEach-Object { $_ * 2 }
$collection | ForEach-Object -Begin { "start" } -Process { $_ } -End { "done" }

# ForEach-Object -Parallel (PS 7+ only) — run blocks concurrently
$collection | ForEach-Object -Parallel { "Processing $_" } -ThrottleLimit 5

# for loop
for ($i = 0; $i -lt 10; $i++) { $i }

# while / do-while / do-until
while ($condition) { ... }
do { ... } while ($condition)
do { ... } until ($condition)     # runs until condition becomes TRUE

# Range operator — generates integer sequence
1..10 | ForEach-Object { $_ }
foreach ($i in 1..10) { $i }
$rev = 10..1                       # countdown range

# Loop control
foreach ($x in $a) {
    if ($x -eq 0) { continue }    # next iteration
    if ($x -gt 100) { break }     # exit loop
}
```

### Functions

```powershell
# Simple
function Get-Greeting { param($Name) "Hello, $Name" }

# Advanced function — full Cmdlet binding, pipeline support, validation
function Invoke-Thing {
    [CmdletBinding(SupportsShouldProcess)]           # adds -WhatIf, -Confirm
    param(
        [Parameter(Mandatory, ValueFromPipeline)]
        [string]$Name,

        [Parameter()]
        [ValidateSet("Fast", "Slow")]                # validated enum
        [string]$Mode = "Fast",

        [Parameter()]
        [ValidateRange(1, 100)]
        [int]$Count = 1,

        [ValidateScript({ Test-Path $_ })]           # arbitrary validation
        [string]$InputFile,

        [switch]$Force                               # boolean flag
    )
    begin   { Write-Verbose "Starting batch" }
    process {
        # process runs once per pipeline item when ValueFromPipeline
        if ($PSCmdlet.ShouldProcess($Name, "Invoke")) {
            "Processing $Name with $Mode × $Count"
        }
    }
    end     { Write-Verbose "Complete" }
}

# CRITICAL: PowerShell function return value = ALL pipeline output, not just `return`
function Get-Value {
    Write-Host "This goes to console — NOT returned"     # console only
    Write-Output "this is returned"                       # to pipeline
    "implicit emission — also returned"                   # any expression output is returned
    return "explicit return — also output, then exit"
}
$result = Get-Value    # array of ALL emitted values

# To suppress unwanted output: assign to $null or pipe to Out-Null
$null = $list.Add("item")
Some-CmdletThatEmits | Out-Null
```

### I/O and Redirection

```powershell
Write-Output "goes to pipeline"     # captured by variables, pipes — use for data
Write-Host   "console only"         # NOT captured — use for user-facing messages only
Write-Error  "error message"        # to error stream (stream 2)
Write-Warning "warning"             # to warning stream (stream 3)
Write-Verbose "detail" -Verbose     # stream 4 — shown only with -Verbose flag
Write-Debug   "debug"  -Debug       # stream 5

Read-Host "Enter value"             # interactive prompt
Read-Host "Password" -AsSecureString  # masked input

# Redirection streams:
#   1 = Success (stdout), 2 = Error, 3 = Warning, 4 = Verbose, 5 = Debug, 6 = Info

command > file.txt          # stream 1 → file (overwrite)
command >> file.txt         # stream 1 → file (append)
command 2> err.txt          # stream 2 → file
command 2>&1                # stream 2 → stream 1
command *> all.txt          # all streams → file
command *>&1                # all streams → stdout

$null = command             # discard output
command | Out-Null          # also discard
command > $null             # also works

# Structured output
Get-Process | Out-File processes.txt
Get-Process | Export-Csv   processes.csv  -NoTypeInformation
Get-Process | ConvertTo-Json -Depth 5 | Out-File processes.json
Get-Content processes.json | ConvertFrom-Json
```

### Exit Codes and Error Handling

```powershell
# Exit code
exit 0     # success
exit 1     # failure

# Three error signals — know all three:
# $?              bool    — last PS cmdlet/function succeeded?
# $LASTEXITCODE   int     — last EXTERNAL executable's exit code
# $Error[0]       object  — last ErrorRecord (any error)

# TRAP: $? after external commands
git push            # external
$?                  # TRUE — PS launched git successfully (not about git's result)
$LASTEXITCODE       # 1 — this is git's actual return code

# Mandatory pattern for external tools:
git push
if ($LASTEXITCODE -ne 0) { throw "git push failed: exit $LASTEXITCODE" }

# PS 7+ pipeline chain operators
git fetch && git merge && git push   # stop on first failure
git pull || throw "pull failed"      # throw if left side fails

# Make cmdlet errors terminating
$ErrorActionPreference = "Stop"     # global default (set at script top for strict scripts)
Copy-Item "src" "dst" -ErrorAction Stop   # per-call override

# Try/Catch/Finally (only catches terminating errors unless ErrorActionPreference = Stop)
try {
    $data = Get-Content "missing.txt" -ErrorAction Stop
    Invoke-RestMethod "https://api.example.com/data"
}
catch [System.IO.FileNotFoundException] {
    Write-Error "File not found: $($_.Exception.Message)"
}
catch [System.Net.Http.HttpRequestException] {
    Write-Error "HTTP error: $($_.Exception.Message)"
}
catch {
    Write-Error "Unexpected: $_"
    throw       # re-throw to propagate
}
finally {
    # Always runs — cleanup here
}
```


### Terminating vs Non-Terminating Errors

```
Two categories that control where execution goes:

Terminating error:
  - Throws immediately, can be caught by try/catch
  - Sources: throw statement; Write-Error -ErrorAction Stop;
             cmdlets called with -ErrorAction Stop;
             $ErrorActionPreference = "Stop" in scope

Non-terminating error:
  - Writes to $Error, emits to error stream, execution CONTINUES
  - Sources: most cmdlet errors by default (Get-Item on missing path, etc.)
  - try/catch DOES NOT catch these — they flow past the catch block
  - Fix: force terminating via -ErrorAction Stop or $ErrorActionPreference = "Stop"

$ErrorActionPreference scope rules:
  Set at script top  → affects all cmdlets in that script and functions it calls
  Set inside function → affects only that function's scope (restored on exit)
  -ErrorAction Stop  → overrides preference for that one call only

# Practical: set Stop at the top of production scripts, override per-call where you
# expect recoverable errors (e.g., Test-Path before Get-Item).
$ErrorActionPreference = "Stop"
$content = Get-Content "maybe-missing.txt" -ErrorAction SilentlyContinue  # this one OK
```

### $Error — The Circular Buffer

```powershell
# $Error is an ArrayList of the last N ErrorRecords (default 256, configured by $MaximumErrorCount)
$Error[0]         # most recent error
$Error[-1]        # oldest error in the buffer
$Error.Count      # how many errors accumulated

$Error.Clear()    # reset the buffer — useful before a risky section to isolate errors
$MaximumErrorCount = 50    # reduce buffer size if memory is a concern

# $Error accumulates ALL errors including ones you caught — it is NOT cleared by try/catch.
# In long-running scripts, stale entries from earlier operations can confuse diagnosis.
# Pattern: $Error.Clear() before a critical section, inspect $Error after.
```

### -ErrorVariable — Capture Non-Terminating Errors

```powershell
# Collect non-terminating errors into a named variable WITHOUT catching/aborting
Get-ChildItem "C:\MissingDir" -ErrorAction SilentlyContinue -ErrorVariable dirErrors
if ($dirErrors) {
    Write-Warning "Directory errors: $($dirErrors.Count)"
    $dirErrors | ForEach-Object { Write-Warning $_.Exception.Message }
}

# Note: variable name WITHOUT the $ prefix in -ErrorVariable
# Note: errors are still written to $Error as well
# Use case: bulk operations where you want to continue and collect all failures
```

### ErrorRecord Inspection

```powershell
# In a catch block, $_ is the ErrorRecord. Its structure:
catch {
    $_.Exception.Message             # human-readable message string
    $_.Exception.GetType().FullName  # actual .NET exception type
    $_.Exception.InnerException      # wrapped exception if present

    $_.CategoryInfo.Category         # ErrorCategory enum (ObjectNotFound, etc.)
    $_.CategoryInfo.Reason           # short reason string
    $_.CategoryInfo.TargetName       # what object caused the error

    $_.InvocationInfo.ScriptName          # file path where error occurred
    $_.InvocationInfo.ScriptLineNumber    # line number
    $_.InvocationInfo.Line               # actual source line text
    $_.InvocationInfo.PositionMessage    # formatted "At line:X char:Y" string

    $_.FullyQualifiedErrorId    # unique ID for this error (useful for filtering)
    $_.TargetObject             # the object being operated on when error occurred

    # Structured diagnostic output:
    [PSCustomObject]@{
        Type    = $_.Exception.GetType().Name
        Message = $_.Exception.Message
        Line    = $_.InvocationInfo.ScriptLineNumber
        File    = $_.InvocationInfo.ScriptName
    }
}

# For non-terminating errors captured via -ErrorVariable, same properties apply:
$dirErrors[0].InvocationInfo.ScriptLineNumber
```

### Script Arguments

```powershell
# Minimal — $args array (no IntelliSense, no validation, no tab-completion)
$name = $args[0]

# Proper param block — always prefer this
param(
    [string]$Name   = "default",
    [int]$Count     = 1,
    [switch]$Verbose,
    [Parameter(Mandatory)][string]$Required,

    [Parameter(ValueFromPipeline)]
    [string]$PipelineInput
)

# Invocation
.\script.ps1 -Name "Alice" -Count 5 -Verbose
"Alice" | .\script.ps1                         # via pipeline (requires ValueFromPipeline)

# Splatting — pass hashtable as named parameters
$params = @{ Name = "Alice"; Count = 5 }
.\script.ps1 @params           # @ not $ — this is splatting syntax

# Detect what was explicitly passed vs what used defaults
if ($PSBoundParameters.ContainsKey("Count")) { "Count was explicitly specified" }
```

### Common Patterns

```powershell
# Object inspection
$obj | Get-Member                          # list all properties and methods
$obj.GetType().FullName                    # .NET type name
Get-Process | Select-Object Name, CPU, Id  # project specific properties

# File/path operations
$fullPath = Join-Path $PSScriptRoot "config.json"
$dir      = Split-Path $fullPath -Parent
$file     = Split-Path $fullPath -Leaf
$ext      = [IO.Path]::GetExtension($fullPath)
New-Item -ItemType Directory -Path $dir -Force
Get-ChildItem -Path $dir -Filter "*.log" -Recurse | Where-Object Length -gt 1MB

# Call external tools
$output = git log --oneline -10           # captures stdout
$output = & git log --oneline -10         # & (call operator) — needed when path has spaces
$output = & "C:\path\to my app.exe" --flag
& { git status }                          # script block invocation

# JSON round-trip
$cfg = Get-Content "config.json" -Raw | ConvertFrom-Json
$cfg.property
$cfg | ConvertTo-Json -Depth 10 | Out-File "out.json" -Encoding utf8

# REST API
$response = Invoke-RestMethod "https://api.example.com/data"   # auto-deserializes JSON
$response.items | Where-Object active -eq $true

# Cross-platform guards (PS 7)
if ($IsWindows) { ... }
if ($IsLinux)   { ... }
if ($IsMacOS)   { ... }

# Module management
Install-Module Az -Scope CurrentUser
Import-Module Az
Get-Module -ListAvailable
```


---

## Modules and Dot-Sourcing

Every scripting language has a module/library system. This is PowerShell's.

### Dot-Sourcing vs Import-Module

```powershell
# Dot-sourcing: execute a script in the CURRENT scope
# Functions, variables, and aliases defined in the script become available HERE
. .\helpers.ps1          # functions from helpers.ps1 are now in scope
. "$PSScriptRoot\lib\utils.ps1"   # use $PSScriptRoot for relative-to-script paths

# Import-Module: load a packaged module (directory or .psm1 file)
Import-Module .\MyModule          # loads .\MyModule\MyModule.psd1 or .psm1
Import-Module MyModule            # searches $env:PSModulePath

# Difference in practice:
#   Dot-source: quick sharing within a script family; no encapsulation; everything leaks
#   Import-Module: proper encapsulation; only FunctionsToExport are visible; versioned

# -Force to reload (useful during development):
Import-Module MyModule -Force

# Inspect what a module exposes:
Get-Command -Module MyModule
Get-Module MyModule | Select-Object -ExpandProperty ExportedFunctions
```

### Module Manifest (.psd1)

```powershell
# Generate a skeleton:
New-ModuleManifest -Path ".\MyModule\MyModule.psd1" `
    -RootModule "MyModule.psm1" `
    -ModuleVersion "1.2.0" `
    -Author "You" `
    -Description "What it does"

# Key fields in the .psd1 hashtable:
@{
    RootModule        = 'MyModule.psm1'    # entry point (.psm1 or .dll)
    ModuleVersion     = '1.2.0'
    GUID              = 'xxxxxxxx-...'     # generated once, never change

    # Explicit export lists — if missing, PS exports everything (bad practice)
    FunctionsToExport = @('Get-Thing', 'Invoke-Thing')   # everything else is private
    CmdletsToExport   = @()
    AliasesToExport   = @()

    RequiredModules   = @(
        @{ ModuleName = 'Az.Accounts'; ModuleVersion = '2.0.0' }
    )

    RequiredAssemblies = @('bin\MyHelper.dll')   # .NET assemblies to pre-load

    PrivateData = @{
        PSData = @{
            Tags       = @('Azure', 'Automation')
            ProjectUri = 'https://github.com/...'
        }
    }
}
```

### PSModulePath — Where PS Looks

```powershell
# Ordered search path — first match wins
$env:PSModulePath -split ';'
# Typical output:
#   C:\Users\you\Documents\PowerShell\Modules    ← user-scope installs
#   C:\Program Files\PowerShell\Modules          ← system-scope installs
#   C:\WINDOWS\system32\WindowsPowerShell\v1.0\Modules   ← built-in

# Add a private feed directory (e.g., in CI/CD pipeline):
$env:PSModulePath = "C:\pipeline\modules;$env:PSModulePath"

# In Azure Pipelines: add to ##vso[task.setvariable] or set in pipeline YAML env:
# env:
#   PSModulePath: $(Build.SourcesDirectory)/modules;$(PSModulePath)
```

### #Requires — Enforce Prerequisites

```powershell
#Requires -Version 7.2                          # minimum PS version
#Requires -Modules @{ ModuleName='Az'; ModuleVersion='9.0' }   # module + version
#Requires -Modules Pester, PSScriptAnalyzer     # simple list
#Requires -RunAsAdministrator                   # elevate or fail

# Must be at the TOP of the script (before any executable code).
# PS checks before executing a single line — clean fail with clear message.
```

### Module Autoloading vs Explicit Import

```powershell
# PS 3+: if you type a command that belongs to a module in PSModulePath,
# PS will auto-import that module before running the command.
Get-AzVM    # triggers auto-import of Az.Compute if installed

# Auto-import is fine for interactive sessions.
# For scripts: use explicit Import-Module at the top.
# Why: auto-import is session-state dependent; explicit import is deterministic.
# In CI/CD always be explicit.

# Private functions in a .psm1 are simply not listed in FunctionsToExport.
# They are callable within the module but invisible outside.
function Invoke-Internal { ... }      # private — not exported
function Get-PublicThing { Invoke-Internal }   # public — exported in .psd1
```

---

## PSCustomObject and Structured Output

Returning structured data from functions is a universal pattern. In Python you'd return a dataclass; in Go a struct; in PS the idiom is `[PSCustomObject]`.

### [PSCustomObject] — Structured Return Values

```powershell
# Inline construction — cleaner than New-Object for ad-hoc objects
$result = [PSCustomObject]@{
    Name     = "Alice"
    Score    = 42
    Active   = $true
    Tags     = @("admin", "dev")
}

$result.Name      # "Alice"
$result | Get-Member   # inspect properties

# Functions that return multiple [PSCustomObject] instances compose naturally in the pipeline:
function Get-Metrics {
    [CmdletBinding()]
    param([string[]]$Hosts)
    foreach ($h in $Hosts) {
        [PSCustomObject]@{
            Host    = $h
            CPU     = (Get-Random -Max 100)
            Memory  = (Get-Random -Max 32)
            Sampled = (Get-Date)
        }
    }
}
Get-Metrics -Hosts "web01","web02" | Where-Object CPU -gt 80 | Export-Csv -NoTypeInformation
```

### Add-Member — Dynamic Extension

```powershell
# Extend an existing object at runtime
$obj = [PSCustomObject]@{ Name = "Alice" }
$obj | Add-Member -NotePropertyName Score -NotePropertyValue 100
$obj | Add-Member -MemberType ScriptMethod -Name "Greet" -Value { "Hello, $($this.Name)" }
$obj.Greet()    # "Hello, Alice"

# Extend objects from cmdlet output (e.g., add a computed property to Get-Process output):
$procs = Get-Process | ForEach-Object {
    $_ | Add-Member -NotePropertyName CPUPercent -NotePropertyValue ($_.CPU / 60) -PassThru
}
```

### Calculated Properties with Select-Object

```powershell
# Inline projection without constructing new objects:
Get-Process | Select-Object Name, CPU, @{
    Name       = "CPUSeconds"
    Expression = { [Math]::Round($_.CPU, 1) }
}, @{
    Name       = "WorkingSetMB"
    Expression = { [Math]::Round($_.WorkingSet64 / 1MB, 1) }
}

# Useful pattern for reshaping API responses before Export-Csv or ConvertTo-Json:
$response.items | Select-Object id, @{
    Name = "CreatedDate"
    Expression = { [datetime]$_.created_at }
}
```

### PowerShell Classes (PS 5+)

```powershell
# Classes exist but have different tradeoffs vs [PSCustomObject]
class ServerMetric {
    [string]$Host
    [double]$CPU
    [datetime]$Sampled

    ServerMetric([string]$h, [double]$c) {
        $this.Host    = $h
        $this.CPU     = $c
        $this.Sampled = Get-Date
    }

    [bool] IsHot() { return $this.CPU -gt 80 }
}

$m = [ServerMetric]::new("web01", 92.5)
$m.IsHot()    # $true

# Class inheritance:
class CriticalMetric : ServerMetric {
    [string]$AlertLevel = "P1"
    CriticalMetric([string]$h, [double]$c) : base($h, $c) {}
}

# CRITICAL limitation — serialization cliff:
# Classes defined in a .ps1 or .psm1 do NOT serialize cleanly across remoting or jobs.
# Class definition must exist in the receiving runspace too.
# Remoted class instances come back as bare PSCustomObject (methods gone).
# For data that crosses runspace/remoting boundaries: use [PSCustomObject] not classes.
# Classes are appropriate for: complex in-process logic, DSL builders, test helpers.
```

---

## Remoting

Remote execution is a universal ops pattern (SSH, WinRM, gRPC — run commands on a remote machine). PowerShell has first-class support with two transports.

### Transport Options

```
WinRM  (Windows Remote Management)
  - Windows-only, uses HTTP/HTTPS (ports 5985/5986)
  - Kerberos auth on domain; NTLM for workgroup
  - Required: WinRM service enabled on target (winrm quickconfig)
  - PS 5.1 and 7 both support it
  - Default in enterprise Windows environments

SSH transport (PS 7+)
  - Cross-platform: Linux → Windows, Windows → Linux, any → any
  - Requires: OpenSSH server on target with PS subsystem configured
  - Auth via SSH key or password
  - /etc/ssh/sshd_config entry: Subsystem powershell /usr/bin/pwsh -sshs -NoLogo
```

### Session Management

```powershell
# Interactive remoting (like SSH session)
Enter-PSSession -ComputerName "web01"                      # WinRM
Enter-PSSession -HostName "web01" -UserName "admin"        # SSH (PS 7)
Exit-PSSession

# One-shot command execution
Invoke-Command -ComputerName "web01" -ScriptBlock { Get-Process | Where-Object CPU -gt 50 }

# Multiple targets simultaneously
Invoke-Command -ComputerName "web01","web02","web03" -ScriptBlock {
    [PSCustomObject]@{ Host = $env:COMPUTERNAME; Uptime = (Get-Uptime) }
}

# Persistent session — avoids connection overhead for multiple operations
$session = New-PSSession -ComputerName "web01"
Invoke-Command -Session $session -ScriptBlock { $data = Get-Process }
Invoke-Command -Session $session -ScriptBlock { $data | Where-Object CPU -gt 50 }  # $data persists
Remove-PSSession $session

# Passing local variables into remote scriptblocks:
$threshold = 80
Invoke-Command -ComputerName "web01" -ScriptBlock {
    param($t)
    Get-Process | Where-Object CPU -gt $t
} -ArgumentList $threshold

# Or $using: in PS 7:
Invoke-Command -ComputerName "web01" -ScriptBlock {
    Get-Process | Where-Object CPU -gt $using:threshold
}

# Credentials (for non-domain or cross-domain scenarios):
$cred = Get-Credential                                    # prompts interactively
$cred = [PSCredential]::new("admin", (ConvertTo-SecureString "pass" -AsPlainText -Force))
Invoke-Command -ComputerName "web01" -Credential $cred -ScriptBlock { hostname }

# Fire-and-forget remote jobs:
$job = Invoke-Command -ComputerName "web01" -ScriptBlock { Start-Sleep 30; "done" } -AsJob
Receive-Job $job -Wait
```

### The Serialization Cliff

```
Remote commands serialize objects for transport and deserialize on the receiving end.
After deserialization:
  ✓  Data (properties, values) survives
  ✗  Methods are gone — object is a PSCustomObject shell
  ✗  .NET type identity is gone — $obj.GetType().Name is "Deserialized.System.Diagnostics.Process"

Remoted Get-Process returns:  System.Management.Automation.PSObject (Deserialized)
Local Get-Process returns:    System.Diagnostics.Process

Consequence: pipeline-filter and property access work fine.
             calling methods ($proc.Kill()) fails on remoted results.

Fix for method calls: move the operation to the remote scriptblock before returning.
  Wrong:  $procs = Invoke-Command ... { Get-Process }; $procs | ForEach-Object { $_.Kill() }
  Right:  Invoke-Command ... { Get-Process | Where-Object Name -eq "notepad" | Stop-Process }
```

---

## What Makes It Distinct

```
PowerShell is the only mainstream shell designed around object flow.
Every other shell (Bash, Fish, Zsh, cmd) passes text between processes.
PS passes .NET objects — which means:

  ┌──────────────────────────────────────────────────────────────────────────────┐
  │  Unix/Bash                          PowerShell                               │
  │  ─────────────────────────         ─────────────────────────────────────     │
  │  Pipeline: text                    Pipeline: typed .NET objects              │
  │  Schema: implicit (columns)        Schema: explicit (property names)         │
  │  Discovery: man page / --help      Discovery: Get-Member                     │
  │  Parsing: awk/cut/sed/grep         Parsing: none — properties already there  │
  │  Type system: none (all strings)   Type system: full CLR (int/datetime/etc.) │
  │  Error signals: exit code only     Error signals: $? + $LASTEXITCODE + $Error│
  └──────────────────────────────────────────────────────────────────────────────┘

PS is also built on .NET, which means:
  - Full access to any .NET class: [Math], [IO.File], [Regex], [System.Net.*]
  - Same type coercion rules as C#
  - Remoting that sends serialized objects over the wire (not text)
  - Desired State Configuration for declarative system config

The cmdlet naming convention (Verb-Noun) is enforced by PSScriptAnalyzer.
Approved verbs: Get-Verb | Select-Object Verb
Breaking the convention works but causes lint warnings and breaks discoverability.
```

---

## Ecosystem

| Area | Tool / Module | Notes |
|------|--------------|-------|
| Module registry | PSGallery | `Install-Module` / `Find-Module` |
| Azure management | `Az` module | Full ARM / resource management |
| Active Directory | `ActiveDirectory` module | AD/LDAP from PS |
| Windows mgmt | `CimInstance`, `Get-WmiObject` | WMI successor (CIM/DCOM) |
| Testing | Pester | BDD-style; `Describe`/`It`/`Should`; like xUnit |
| Linting | PSScriptAnalyzer | Verb-Noun conventions, common bugs |
| Remoting | `Invoke-Command`, `Enter-PSSession` | WinRM or SSH transport |
| Secrets | `SecretManagement` module | Vault abstraction (KeePass, Azure Key Vault, etc.) |
| REST API | `Invoke-RestMethod` | Auto-deserializes JSON/XML responses |
| DSC | PowerShell DSC | Declarative system configuration; push/pull modes |
| Package mgmt | `winget`, `choco`, `scoop` | All have PS wrappers or are PS-native |
| CI/CD | GitHub Actions, Azure Pipelines | Both have first-class PS task support |

---

## Gotchas and Traps

| Trap | Issue | Fix |
|------|-------|-----|
| `Write-Host` vs `Write-Output` | `Write-Host` bypasses pipeline — `$x = Write-Host "hi"` captures nothing | Use `Write-Output` (or bare expression) for data; `Write-Host` only for interactive messages |
| `$?` after external commands | `$?` is TRUE if PS launched the process, regardless of exit code | Check `$LASTEXITCODE -ne 0` after git/node/etc. |
| Function returns ALL output | Every expression that emits goes into the return value | Assign unwanted output to `$null` or pipe to `Out-Null` |
| Case-insensitive by default | `-eq "Hello"` matches "HELLO" | Use `-ceq` for case-sensitive; document if you rely on insensitivity |
| `$null` on left in comparisons | `$arr -eq $null` iterates array, returning matching elements | Always: `$null -eq $var` |
| `foreach` memory | `foreach ($x in Get-ChildItem -Recurse)` buffers everything | Use `Get-ChildItem -Recurse | ForEach-Object` to stream |
| `$a += item` performance | Recreates entire array every time — O(n) per append | `[System.Collections.ArrayList]` for frequent appends |
| ExecutionPolicy | PS blocks `.ps1` by default on Windows | `Set-ExecutionPolicy RemoteSigned` (user) or `-ExecutionPolicy Bypass` in CI |
| `powershell` vs `pwsh` | `powershell` = 5.1 (built-in); `pwsh` = 7.x (installed separately) | Ternary, `??`, `??=`, `-Parallel` require `pwsh` |
| Encoding PS 5.1 | Default output encoding is UTF-16 LE — breaks Unix tools | `Out-File -Encoding utf8` or `$PSDefaultParameterValues['Out-File:Encoding'] = 'utf8'` |
| `switch` fall-through | All matching cases run — unlike C# | Add `break` after each case if you want C#-style exclusive matching |
| `[int]` overflow | `[int]::MaxValue` is 2,147,483,647 — easy to overflow with bytes/timestamps | Use `[long]` or `[int64]` for large numbers |

---

## Bridge to Bash

| PowerShell | Bash | Notes |
|-----------|------|-------|
| `$var = "value"` | `var=value` | PS has spaces around `=`; Bash must NOT have spaces |
| `$?` (bool) | `$?` (int, 0=success) | Different semantics entirely |
| `$LASTEXITCODE` | `$?` | PS separates cmdlet success from external exit code |
| `foreach ($x in $a)` | `for x in "${a[@]}"` | Both iterate arrays |
| `$a.Count` | `${#a[@]}` | |
| `"$($obj.Prop)"` | `"$(cmd)"` | PS: property in string; Bash: command substitution |
| `Test-Path $p` | `[[ -e $p ]]` | |
| `Test-Path $p -PathType Leaf` | `[[ -f $p ]]` | |
| `Test-Path $p -PathType Container` | `[[ -d $p ]]` | |
| `-like "foo*"` | `[[ $x == foo* ]]` | Both glob-style wildcard |
| `-match "regex"` | `[[ $x =~ regex ]]` | Both populate match groups |
| `\| Out-Null` | `> /dev/null` | |
| `$null = cmd` | `cmd > /dev/null` | |
| `$PSScriptRoot` | `$(dirname "$0")` or `$BASH_SOURCE` | |
| `try { } catch { }` | `trap` / `|| { handle; }` | PS: full structured; Bash: limited |
| `-ErrorAction Stop` | `set -e` | Makes non-terminating errors terminating |
| `Get-ChildItem -Recurse` | `find .` | |
| `Select-String -Pattern "x"` | `grep "x"` | |
| `Where-Object { $_ -gt 5 }` | `awk '$1 > 5'` | PS has object properties; Bash needs awk for fields |
| `ForEach-Object { $_ * 2 }` | `awk '{print $1 * 2}'` | |
| `ConvertFrom-Json` | `jq` | PS built-in; Bash needs jq tool |
| `Invoke-RestMethod` | `curl \| jq` | PS deserializes automatically |
| `&&` / `\|\|` (PS 7+) | `&&` / `\|\|` | Same semantics; PS 7+ only |


---

## Cloud CLI Integration — Azure PowerShell

Every major cloud has a shell module (AWS has `AWS.Tools.*`, GCP has `GoogleCloud`). Azure's is the `Az` module. The patterns here are universal to cloud shell SDKs; the specifics are Azure.

### Module Structure

```
Az is a meta-module (umbrella). It installs ~70 sub-modules by service area.
You rarely need all of them. Install sub-modules directly for faster CI installs.

Az.Accounts      ← authentication, context, subscription mgmt (always needed)
Az.Compute       ← VMs, scale sets, disks, snapshots
Az.Storage       ← blob, queue, table, file share
Az.KeyVault      ← secrets, keys, certificates
Az.Network       ← VNets, NSGs, load balancers, DNS
Az.Resources     ← resource groups, ARM deployments, tags, policies
Az.Sql           ← Azure SQL, elastic pools
Az.ContainerInstance / Az.Aks   ← containers, AKS
Az.Monitor       ← metrics, alerts, diagnostics
Az.Automation    ← runbooks, DSC, automation accounts

# Full install (slow but comprehensive):
Install-Module Az -Scope CurrentUser -Repository PSGallery -Force

# Targeted install (prefer in CI/CD):
Install-Module Az.Accounts, Az.Compute, Az.Storage -Scope CurrentUser -Force
```

### Authentication Patterns

```powershell
# Interactive (dev workstation):
Connect-AzAccount                         # browser auth flow
Connect-AzAccount -TenantId "xxx"         # specific tenant

# Service principal (CI/CD with client secret — avoid in Azure Pipelines, use service connection instead):
$cred = [PSCredential]::new(
    $env:SP_CLIENT_ID,
    (ConvertTo-SecureString $env:SP_CLIENT_SECRET -AsPlainText -Force)
)
Connect-AzAccount -ServicePrincipal -Credential $cred -TenantId $env:TENANT_ID

# Service principal with certificate:
Connect-AzAccount -ServicePrincipal -ApplicationId $appId `
    -CertificateThumbprint $thumbprint -TenantId $tenantId

# Managed identity (Azure VMs, Functions, ACI — no credential needed):
Connect-AzAccount -Identity                          # system-assigned MI
Connect-AzAccount -Identity -AccountId $clientId    # user-assigned MI

# In Azure Pipelines with AzurePowerShell@5 task:
# DO NOT call Connect-AzAccount — the task injects the service connection token automatically.
# The context is already set before your script runs.
```

### Context and Subscription Management

```powershell
# List available contexts (subscriptions you've authenticated to):
Get-AzContext -ListAvailable

# Current context:
Get-AzContext

# Switch to a different subscription:
Set-AzContext -SubscriptionId "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
Set-AzContext -SubscriptionName "Production"

# Useful in multi-sub scripts — save/restore pattern:
$savedCtx = Get-AzContext
Set-AzContext -SubscriptionId $targetSubId
# ... do work ...
Set-AzContext -Context $savedCtx   # restore

# Save context between sessions:
Save-AzContext -Path "$HOME\.azure\context.json"
Import-AzContext -Path "$HOME\.azure\context.json"
```

### Common Patterns

```powershell
# List VMs in a resource group:
Get-AzVM -ResourceGroupName "prod-rg" | Select-Object Name, Location, @{
    Name = "Size"; Expression = { $_.HardwareProfile.VmSize }
}

# Stop all VMs matching a pattern:
Get-AzVM -ResourceGroupName "dev-rg" |
    Where-Object Name -like "dev-*" |
    ForEach-Object { Stop-AzVM -ResourceGroupName $_.ResourceGroupName -Name $_.Name -Force }

# ARM deployment:
New-AzResourceGroupDeployment `
    -ResourceGroupName "prod-rg" `
    -TemplateFile ".\infra\main.bicep" `
    -TemplateParameterObject @{ env = "prod"; size = "Standard_D2s_v3" }

# Key Vault secret retrieval:
$secret = Get-AzKeyVaultSecret -VaultName "my-vault" -Name "db-password" -AsPlainText
```

### Azure Pipelines Integration

```yaml
# YAML pipeline — AzurePowerShell@5 task handles auth automatically
- task: AzurePowerShell@5
  inputs:
    azureSubscription: 'my-service-connection'   # service connection name
    ScriptType: 'InlineScript'
    Inline: |
      # Context is pre-authenticated — do NOT call Connect-AzAccount
      $vms = Get-AzVM -ResourceGroupName "prod-rg"
      Write-Host "Found $($vms.Count) VMs"
    azurePowerShellVersion: 'LatestVersion'
    pwsh: true   # use pwsh (PS 7) instead of powershell.exe (PS 5.1)

# Alternative: pwsh step with manual Connect-AzAccount (service principal)
- task: PowerShell@2
  env:
    SP_ID: $(ServicePrincipalId)      # pipeline variables
    SP_SECRET: $(ServicePrincipalSecret)
    TENANT_ID: $(TenantId)
  inputs:
    pwsh: true
    script: |
      $cred = [PSCredential]::new($env:SP_ID,
          (ConvertTo-SecureString $env:SP_SECRET -AsPlainText -Force))
      Connect-AzAccount -ServicePrincipal -Credential $cred -TenantId $env:TENANT_ID
      ...
```

### AzureRM → Az Migration Note

```
AzureRM module is end-of-life (Feb 2024). Cmdlet names changed — not a 1:1 rename.
Common mappings:
  Login-AzureRmAccount    →  Connect-AzAccount
  Get-AzureRmVM           →  Get-AzVM
  New-AzureRmResourceGroup→  New-AzResourceGroup
  Set-AzureRmContext      →  Set-AzContext

Pattern: AzureRm* prefix → Az* prefix, but verify — some commands restructured entirely.
Run: Get-Command -Module Az.* | Where-Object Name -like "*VM*"  to discover current names.
```

---

## Decision Cheat Sheet

| Use PowerShell when... | Use Bash when... |
|-----------------------|-----------------|
| Windows administration (AD, services, registry) | Linux/Mac native environment |
| Azure / M365 / Entra management via SDK | Docker/Kubernetes scripting (Linux containers) |
| Working with .NET objects and types | POSIX portability required |
| Structured data without string parsing | Team uses Linux/Mac dev environments |
| Complex error handling (try/catch) | Shell script lives alongside Linux tooling |
| Remoting / DSC / desired state | `awk`/`sed`/`grep` pipelines are natural |
| CI/CD on Windows agents | Open-source project conventions favor Bash |
| Calling existing .NET libraries directly | |

> PS 7 runs on Linux/Mac — but Bash is still preferred for Linux container scripts and open-source projects because it's universally available without installation and the community expects it. Use PS 7 for Windows-centric or Azure automation; use Bash for anything targeting Linux or the open-source ecosystem.
