# Scripting: AWK

> Record-oriented stream processor. Not a shell — a declarative query language for text tables. The Unix equivalent of a mini SQL for stdin.

## Language Snapshot

| Attribute | Value |
|-----------|-------|
| Platform | All Unix/Linux/macOS; Windows via WSL/Git Bash |
| Extension | `.awk` |
| Shebang | `#!/usr/bin/awk -f` |
| Paradigm | Pattern-action; data-driven; declarative |
| Typing | Dual type (string/number — context-dependent) |
| Execution | Compiled per-invocation (not interpreted line by line) |

---

## Execution Model

```
AWK processing pipeline:

  input file/stream
       │
       ▼
  ┌─────────────────────────────────────────────────────┐
  │  BEGIN { }    <- runs once before first record      │
  │                                                     │
  │  for each record (line by default):                 │
  │    split record into fields: $1 $2 ... $NF         │
  │    for each rule:                                   │
  │      if pattern matches (or no pattern):            │
  │        execute action { }                           │
  │                                                     │
  │  END { }      <- runs once after last record        │
  └─────────────────────────────────────────────────────┘
       │
       ▼
  output (print/printf go to stdout by default)

AWK is a compiled program, not an interpreter:
  awk 'program' file
  -> awk parses+compiles 'program' to internal bytecode
  -> streams file through compiled program
  -> exit
  Much faster than equivalent Perl/Python for simple column ops.
```

---

## Built-in Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `$0` | Entire current record | |
| `$1, $2, ..., $NF` | Individual fields | |
| `NF` | Number of fields in current record | |
| `NR` | Total records processed so far | |
| `FNR` | Records in current file (resets per file) | |
| `FS` | Input field separator | `" "` (whitespace) |
| `RS` | Input record separator | `"\n"` |
| `OFS` | Output field separator | `" "` |
| `ORS` | Output record separator | `"\n"` |
| `FILENAME` | Current input file name | |
| `ARGC` / `ARGV` | Arg count / array | |
| `SUBSEP` | Multi-dim array separator | `\034` |
| `OFMT` | Output format for numbers | `"%.6g"` |
| `CONVFMT` | Conversion format | `"%.6g"` |

---

## Syntax Reference Card

### The Pattern-Action Rule

```awk
# Syntax: pattern { action }
# Pattern: omitted = match all; action: omitted = { print $0 }

/regex/        { print }          # print lines matching regex
$2 > 100       { print $1, $2 }  # print col1,col2 where col2 > 100
NR == 1        { print "header:", $0 }  # first line only
NR > 1         { sum += $3 }      # accumulate all lines except first
/start/,/end/  { print }          # range: from /start/ to /end/ inclusive
!seen[$0]++    { print }          # unique lines (print if not seen before)

BEGIN {
    FS = ","                      # set field separator before first record
    OFS = "\t"                    # set output field separator
    print "Starting"
}
END {
    print "Total records:", NR
    print "Sum:", sum
}
```

### Variables, Types, Arithmetic

```awk
# Variables: auto-initialized to "" or 0; no declaration
total = 0
count = 0
name = "Alice"

# AWK dual-type: same value is string or number depending on context
x = "42"
y = x + 0        # -> 42 (numeric context)
z = x "hello"    # -> "42hello" (string context — concatenation by juxtaposition!)
# NOTE: no + for string concat — adjacent values/strings concatenate

# Arithmetic: full C-style
+  -  *  /  %  ^     # (^ = exponent, not **)
++x  x++  --x  x--
x += 5   x -= 3   x *= 2   x /= 4   x %= 3   x ^= 2
int(3.9)           # -> 3 (truncate to integer)
sqrt(16)           # -> 4
log(2.718)         # -> 1
exp(1)             # -> 2.718...
sin(0)  cos(0)  atan2(1,1)   # trig
rand()             # -> random float [0,1)
srand(seed)        # seed random number generator
```

### String Functions

```awk
length("hello")          # -> 5
length($0)               # -> length of current record
length                   # same as length($0) (AWK shorthand)

substr("hello", 2, 3)    # -> "ell" (1-indexed! start=2, length=3)
substr("hello", 3)       # -> "llo" (from index 3 to end)

index("hello world", "world")  # -> 7 (position of substring; 0 if not found)

split("a:b:c", arr, ":")  # splits into arr[1]="a" arr[2]="b" arr[3]="c"; returns 3
split($0, fields)          # split using FS by default

sub(/pattern/, "replacement")      # replace FIRST match in $0
sub(/pattern/, "replacement", $2)  # replace in specific field
gsub(/pattern/, "replacement")     # replace ALL matches in $0
gsub(/pattern/, "replacement", $2) # replace all in field

match("hello", /l+/)    # -> 4 (position of match; sets RSTART, RLENGTH)
RSTART                   # start position of last match()
RLENGTH                  # length of last match() (-1 if no match)

sprintf("%-10s %5.2f", name, val)  # format without printing
tolower("HELLO")         # -> "hello"
toupper("hello")         # -> "HELLO"
```

### Arrays (Associative Only)

```awk
# AWK only has associative arrays (hash maps)
count[$1]++                          # increment count for key $1
total[$2] += $3                      # accumulate $3 by category $2

# Access
print count["Alice"]
print count[$1]

# Delete
delete count["Alice"]
delete count                          # delete entire array

# Check existence
if ("Alice" in count) print "found"

# Iterate (unordered — no guaranteed order!)
for (key in count) {
    print key, count[key]
}

# Multidimensional (simulated with SUBSEP)
a[1,2] = "val"
if ((1,2) in a) print a[1,2]

# Numeric sort of keys: pipe to sort
for (k in count) print k, count[k] | "sort -k2 -rn"
```

### Conditionals

```awk
# C-style control flow
if ($2 > 100) {
    print "high:", $0
} else if ($2 > 50) {
    print "medium:", $0
} else {
    print "low:", $0
}

# Ternary
result = (x > 0) ? "positive" : "non-positive"

# No switch/case in POSIX AWK (gawk has switch)
# Use if-else chain
```

### Loops

```awk
# C-style for
for (i = 1; i <= NF; i++) {
    printf "Field %d: %s\n", i, $i
}

# For-in (associative arrays)
for (key in array) {
    print key, array[key]
}

# While
i = 1
while (i <= 10) {
    print i
    i++
}

# Do-while
do {
    print i++
} while (i <= 10)

# next — skip to next record (like continue for the outer loop)
/^#/ { next }           # skip comment lines
NF == 0 { next }        # skip blank lines

# exit — exit immediately (still runs END block)
NR > 100 { exit }

# nextfile (gawk) — skip to next input file
FNR > 10 { nextfile }
```

### Functions

```awk
function square(n) {
    return n * n
}

function max(a, b) {
    return (a > b) ? a : b
}

# Local variables: extra parameters with leading spaces (AWK convention)
function count_words(str,    words, n) {   # words,n are locals (extra params)
    n = split(str, words, " ")
    return n
}

BEGIN {
    print square(5)         # -> 25
    print max(3, 7)         # -> 7
}
```

### I/O & Pipes

```awk
print "output"                    # to stdout
printf "formatted: %s\n", val     # formatted output
print "msg" > "file.txt"          # to file (stays open until close)
print "msg" >> "file.txt"         # append
print "msg" | "sort"              # pipe to command (command stays open)
close("sort")                     # explicitly close pipe/file

# Read from file or command
while ((getline line < "file.txt") > 0) {
    print "Read:", line
}
close("file.txt")

while (("command" | getline line) > 0) {
    print "Got:", line
}

getline                           # read next record into $0 (advances NR)
getline var                       # read into var (doesn't change fields)
getline var < "file"              # read from file into var

print "query" | "cat -n" | getline result   # chain
```

---

## Practical One-Liners (The Real Value)

```bash
# Print specific columns
awk '{print $2, $4}' file
awk '{print $NF}' file                     # last field
awk '{print $(NF-1)}' file                 # second-to-last field

# CSV with comma separator
awk -F, '{print $1, $3}' file.csv
awk 'BEGIN{FS=","; OFS="\t"} {print $1,$2,$3}' file.csv  # reformat CSV to TSV

# Filter lines
awk '/ERROR/' file                         # lines containing ERROR
awk '!/^#/' file                           # non-comment lines
awk '$3 > 100' file                        # where field 3 > 100
awk 'NF > 0' file                          # non-blank lines
awk 'NR >= 10 && NR <= 20' file            # lines 10-20

# Print between markers
awk '/START/,/END/' file                   # inclusive range
awk '/START/{found=1} found; /END/{found=0}' file  # START to END

# Sum / stats
awk '{sum += $1} END {print sum}' file
awk '{sum+=$1; n++} END {print sum/n}' file  # mean
awk 'BEGIN{max=-999} $1>max{max=$1} END{print max}' file

# Count occurrences / frequency
awk '{count[$1]++} END {for(k in count) print k, count[k]}' file
awk '{count[$1]++} END {for(k in count) print count[k], k}' file | sort -rn

# Deduplicate (preserve order)
awk '!seen[$0]++'  file                    # print if not seen before

# Remove/keep columns
awk '{$2=$4=""; print}' file              # blank out fields 2 and 4
awk '{$2=""; $1=$1; print}' file          # remove field 2, re-join with OFS

# In-place field edit
awk '{$3 = toupper($3); print}' file      # uppercase field 3
awk '{gsub(/foo/, "bar", $2); print}' file  # replace in field 2

# Add line numbers
awk '{print NR, $0}' file
awk '{printf "%4d  %s\n", NR, $0}' file   # padded

# Header + data
awk 'NR==1{print; next} $3>100' file      # keep header, filter data rows

# Join two files (match on field 1)
awk 'NR==FNR{a[$1]=$2; next} $1 in a {print $0, a[$1]}' file1.txt file2.txt
# NR==FNR is true only while reading the FIRST file

# Reformat / transpose
awk '{for(i=1;i<=NF;i++) a[i][NR]=$i} END{for(i=1;i<=NF;i++){for(j=1;j<=NR;j++) printf "%s%s",a[i][j],(j<NR?OFS:ORS)}}' file

# Print unique values of a column
awk '!seen[$1]++ {print $1}' file

# Word count (like wc -w)
awk '{w+=NF} END{print w}' file

# Process JSON fields (simple flat JSON only)
# (for real JSON use jq instead)
```

---

## gawk-Specific Extensions

```awk
# BEGINFILE / ENDFILE (gawk only)
BEGINFILE { print "--- Processing:", FILENAME }
ENDFILE   { print "--- Done:", FILENAME, "records:", FNR }

# true multidimensional arrays (gawk 4.0+)
a[1][2] = "val"

# Regex intervals (gawk with --re-interval or gawk 4+)
/x{2,4}/   # match 2-4 x's

# @include (gawk)
@include "functions.awk"

# PROCINFO (gawk)
PROCINFO["version"]    # gawk version
PROCINFO["uid"]        # process UID

# Pipe to/from array (gawk)
"ls *.txt" | getline

# printf to stderr
printf "Error: %s\n", msg > "/dev/stderr"
```

---

## What Makes AWK Distinct

```
AWK's mental model is not "write a program", it's "define a transformation":

  SQL analogy:
    SELECT col1, col2        ->  { print $1, $2 }
    FROM file                ->  awk '...' file
    WHERE condition          ->  condition { ... }
    GROUP BY key             ->  count[key]++; END { for k in count }
    ORDER BY col             ->  ... | sort
    LIMIT n                  ->  NR > n { exit }

  AWK excels at:
    - Extracting/reformatting columns from text tables
    - Aggregating (sum, count, avg, frequency)
    - Joining two text files on a key
    - Filtering rows by condition
    - Simple text transformations per-line

  AWK does NOT excel at:
    - Complex string parsing (use Perl or Python)
    - Binary data
    - Real JSON/XML/CSV with escaping (use jq/xmllint)
    - Stateful multi-pass processing (use Python)
```

---

## Ecosystem

| Implementation | Notes |
|----------------|-------|
| `gawk` | GNU AWK — most feature-rich; standard on Linux |
| `mawk` | Fast, minimal — often default on Ubuntu/Debian |
| `nawk` | "New AWK" — standard on Solaris/AIX |
| `one true awk` | Original Kernighan AWK; on macOS as `/usr/bin/awk` |
| `goawk` | Go implementation with some extensions |

```bash
awk --version            # check which awk
gawk --version           # explicitly use gawk
awk 'BEGIN{print PROCINFO["version"]}'  # gawk version check
```

---

## Gotchas & Traps

| Trap | Issue | Fix |
|------|-------|-----|
| `$0` vs `$1` | `$0` = whole line; `$1` = first field | Remember `$0` is the full record |
| Default FS | `" "` means "any whitespace, multiple collapsed" | `-F ","` for CSV; `FS="\t"` for TSV |
| String concat | `"a" + "b"` -> 0+0=0; use `"a" "b"` | Concatenation is juxtaposition |
| 1-indexed | `substr` and `split` are 1-indexed | `substr(s, 1, 3)` = first 3 chars |
| Unordered for-in | `for (k in arr)` order is unpredictable | Pipe to `sort` for ordered output |
| `print` vs `printf` | `print` adds OFS/ORS; `printf` adds nothing | Use `printf` for precise formatting |
| `$2=""` rebuilding | Deleting a field leaves extra OFS | `$1=$1; print` forces rebuild with OFS |
| macOS old awk | `/usr/bin/awk` on macOS is Brian Kernighan's nawk (not gawk) | `brew install gawk` for gawk features |
| Regex in `-F` | `-F '\|'` is regex OR — matches any of the chars | Escape: `-F '\|'` or `FS="[|]"` |
| Pipe stays open | `print \| "sort"` accumulates all output, then flushes on close | `close("sort")` to flush mid-program |

---

## Decision Cheat Sheet

| Use AWK when... | Use something else when... |
|-----------------|--------------------------|
| Extract/reformat columns | Complex logic -> Perl or Python |
| Filter rows by condition | Real JSON/CSV -> jq / csvkit |
| Sum/count/average a column | Multi-file joins > 2 files -> Python |
| Quick frequency table | Need arrays of arrays -> Python |
| One-liner faster than a script | Need libraries/HTTP/DB -> anything else |
| On any Unix box (always available) | Maintaining readable code -> Python |
| `-F` to parse delimited text | Binary data -> Python or C |

> AWK one-liners are archaeology: every sysadmin has dozens. Learn them once; read them forever.
