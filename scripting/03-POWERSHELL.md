# Scripting: PowerShell

> .NET-native shell where the pipeline moves objects, not text. The fundamental difference from every Unix shell — and from Batch.

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
