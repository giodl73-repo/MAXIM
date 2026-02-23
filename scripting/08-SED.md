# Scripting: sed

> Stream editor. A state machine over an input stream — pattern space, hold space, and a command language that predates C. The right tool for in-place file edits and single-line stream transforms.

---

## Language Snapshot

| Attribute | Value |
|-----------|-------|
| Platform | All Unix/Linux/macOS; Windows via WSL/Git Bash |
| Extension | `.sed` (rare) |
| Shebang | `#!/usr/bin/sed -f` |
| Paradigm | Address-command stream processing |
| Typing | Text only |
| Execution | Compiled per-invocation; state machine model |

---

## Execution Model

```
sed execution model:
  ┌──────────────────────────────────────────────────────────────┐
  │  for each input line:                                        │
  │    1. read line into pattern space                           │
  │    2. for each sed command:                                  │
  │       a. if address matches (or no address):                 │
  │          execute command (may modify pattern space)          │
  │    3. print pattern space to stdout (unless -n)              │
  │    4. clear pattern space                                    │
  │                                                              │
  │  Two buffers:                                                │
  │    pattern space — current line being processed              │
  │    hold space    — persistent storage between lines          │
  └──────────────────────────────────────────────────────────────┘

  sed 'command' file
  sed -e 'cmd1' -e 'cmd2' file      # multiple commands
  sed -f script.sed file            # from script file
  sed -n 'cmd' file                 # suppress auto-print (explicit p needed)
  sed -i 's/a/b/g' file            # in-place edit (GNU sed)
  sed -i.bak 's/a/b/g' file        # in-place with backup (GNU + BSD)
  sed -i '' 's/a/b/g' file         # BSD/macOS in-place (requires '' !)
```

---

## Address Types

```sed
# No address: applies to every line
s/foo/bar/

# Line number
5 s/foo/bar/          # line 5 only
$ s/foo/bar/          # last line only
1~2 s/foo/bar/        # every other line starting at 1 (GNU only)

# Regex address
/pattern/ s/x/y/      # lines matching /pattern/
\|pattern| s/x/y/     # alternate delimiter (| can be any char after \)

# Range: addr1,addr2  (inclusive)
2,5 s/foo/bar/                    # lines 2 through 5
/start/,/end/ s/foo/bar/          # from /start/ to /end/ line (inclusive)
0,/pattern/ s/x/y/                # from line 0 to first match (GNU — handles line 1 match)

# Negation: !
/pattern/! s/x/y/     # lines NOT matching pattern
5! d                  # delete all lines except line 5
```

---

## Core Commands

```sed
# s — substitute (the 90% use case)
s/pattern/replacement/            # replace first match per line
s/pattern/replacement/g           # replace ALL matches
s/pattern/replacement/2           # replace only 2nd occurrence
s/pattern/replacement/I           # case-insensitive (GNU)
s/pattern/replacement/p           # print if substitution made (use with -n)
s/pattern/replacement/gp          # replace all + print

# Delimiter can be any character (useful for paths)
s|/usr/local|/opt|g
s,/old/path,/new/path,g

# Backreferences in replacement (BRE — default)
s/\(foo\)\(bar\)/\2\1/            # swap foo and bar → barfoo
s/\([0-9]*\)/[\1]/g               # wrap numbers in brackets

# ERE with -E flag
sed -E 's/(foo)(bar)/\2\1/'       # no escaping of ()
sed -E 's/([0-9]+)/[\1]/g'

# & in replacement = entire match
s/[0-9]*/(&)/                     # wrap match in parens
s/.*/[&]/                         # wrap whole line in brackets

# d — delete line (then skip remaining commands; start next cycle)
d
/^#/ d                            # delete comment lines
/^$/ d                            # delete blank lines

# p — print pattern space
-n '/pattern/ p'                  # print only matching lines (grep equivalent)
-n '10,20 p'                      # print lines 10-20
-n '$p'                           # print last line

# q — quit
10 q                              # process first 10 lines, then quit
/pattern/ q                       # quit after first matching line

# = — print current line number
=                                 # print each line number before the line
/pattern/ =                       # print line numbers of matching lines

# a — append text AFTER current line
/pattern/ a\
text to append

# i — insert text BEFORE current line
/pattern/ i\
text to insert

# c — change (replace entire matched line)
/pattern/ c\
replacement line

# GNU one-liner forms (no backslash-newline required)
sed '/pattern/a\appended text'
sed '/pattern/i\inserted text'
sed '/pattern/c\changed line'

# y — transliterate (character-by-character, like tr)
y/abc/ABC/                        # a→A, b→B, c→C
y/abcdefghijklmnopqrstuvwxyz/ABCDEFGHIJKLMNOPQRSTUVWXYZ/

# r — read file (append contents after current line)
/pattern/ r file.txt

# w — write matching lines to file
/pattern/ w output.txt

# n — print current, read next line into pattern space
n

# N — append next line to pattern space (join with \n; do not print)
N

# Multiple commands in braces
/pattern/ {
    s/x/y/
    s/a/b/
    p
}
```

---

## Multiline Commands: N / P / D

```sed
# N — append next line to pattern space (with embedded \n)
# Enables multi-line patterns

# Collapse two lines into one (remove the embedded newline)
N
s/\n/ /

# Join continuation lines (lines ending with \)
:loop
/\\$/ {
    N
    s/\\\n//
    b loop
}

# P — print only the first line of a multi-line pattern space
# D — delete first line of pattern space, then restart the script
#     (does NOT read a new input line — reruns with remainder of pattern space)

# The N/P/D triad is the sed equivalent of a sliding window:
/start/,/end/ {
    N
    P
    D
}
```

---

## Hold Space Operations

```
Pattern space: current line — cleared at end of each cycle
Hold space:    persistent scratch buffer — survives across lines
               (initialized to empty string at start)

h   copy pattern space TO hold space   (overwrite)
H   APPEND pattern space to hold space (with \n prefix)
g   copy hold space TO pattern space   (overwrite)   "get"
G   APPEND hold space to pattern space (with \n)     "Get"
x   EXCHANGE pattern and hold spaces
```

```sed
# Reverse a file (tac equivalent)
sed -n '1!G; h; $p' file
# Breakdown:
#   1!G  — if NOT first line: append pattern space to hold space
#   h    — copy pattern space to hold space (now hold has current line)
#   $p   — if last line: print (hold space now holds all lines reversed)

# Print the line BEFORE the matching line
sed -n '/pattern/{g;p}; h' file
# h saves current line to hold at each step;
# when match found, g restores previous line, p prints it

# Delete duplicate adjacent lines (uniq equivalent)
sed 'N; /^\(.*\)\n\1$/!P; D'
```

---

## Labels and Branching

```sed
# :label    — define a label
# b label   — branch unconditionally (goto)
# t label   — branch if last s/// succeeded since last t or line start
# T label   — branch if last s/// did NOT succeed (GNU)

# Loop: collapse multiple spaces into one
:loop
s/  / /g
t loop            # keep looping while s// made a substitution

# Conditional skip to end of script
/pattern/ b end
s/x/y/
:end

# Delete leading whitespace via loop
:trim
s/^ //
t trim
```

---

## Common Practical Patterns

```bash
# In-place replace — most common sed use case
sed -i 's/foo/bar/g' file.txt                # GNU (Linux)
sed -i '' 's/foo/bar/g' file.txt             # BSD/macOS
sed -i.bak 's/foo/bar/g' file.txt            # GNU with backup
perl -i.bak 's/foo/bar/g' file.txt           # portable cross-platform alternative

# Delete blank lines
sed '/^$/d' file
sed '/^[[:space:]]*$/d' file                 # blank or whitespace-only

# Delete comment lines
sed '/^#/d' file
sed '/^[[:space:]]*#/d' file                 # indented comments too

# Print lines N through M
sed -n '10,20p' file
sed -n '10,20p;20q' file                     # + quit at line 20

# Strip leading/trailing whitespace
sed 's/^[[:space:]]*//' file                 # leading only
sed 's/[[:space:]]*$//' file                 # trailing only
sed 's/^[[:space:]]*//; s/[[:space:]]*$//' file  # both

# Add prefix or suffix to every line
sed 's/^/PREFIX: /' file
sed 's/$/ SUFFIX/' file

# Extract between markers (inclusive)
sed -n '/START/,/END/p' file

# Extract between markers (exclusive)
sed -n '/START/,/END/{/START/d; /END/d; p}' file

# Replace only between markers
sed '/START/,/END/ s/foo/bar/g' file

# Multiple substitutions
sed -e 's/foo/bar/g' -e 's/baz/qux/g' file
sed 's/foo/bar/g; s/baz/qux/g' file         # semicolon form

# Insert line after match
sed '/pattern/a\new line after' file

# Insert line before match
sed '/pattern/i\new line before' file

# Number lines (classic technique)
sed = file | sed 'N; s/\n/\t/'

# Remove XML/HTML tags (naive — use xmllint for real XML)
sed 's/<[^>]*>//g' file

# Delete lines NOT matching a pattern
sed '/pattern/!d' file
```

---

## GNU sed vs BSD sed (macOS)

| Feature | GNU sed (Linux) | BSD sed (macOS) |
|---------|-----------------|-----------------|
| `-i` in-place | `sed -i 's/a/b/' file` | `sed -i '' 's/a/b/' file` (empty string required) |
| `-i` with backup | `sed -i.bak 's/a/b/' file` | Same syntax |
| `-E` ERE flag | `sed -E` | `sed -E` (same) |
| `\w` `\d` `\s` shortcuts | Supported | NOT supported — use POSIX classes |
| `\+` in BRE | Supported | NOT supported |
| `\|` alternation in BRE | `\(a\|b\)` works | NOT supported — use `-E` |
| `{n,m}` intervals in BRE | Supported | NOT supported in BRE |
| `0,/pat/` zero address | Supported | NOT supported |
| `1~2` step address | Supported | NOT supported |

```bash
# Cross-platform in-place idiom
if sed --version 2>/dev/null | grep -q GNU; then
    sed -i 's/foo/bar/g' file
else
    sed -i '' 's/foo/bar/g' file    # BSD/macOS
fi
# Or: just use Perl for portability
perl -i.bak -pe 's/foo/bar/g' file
```

---

## BRE vs ERE Reference

```
BRE (Basic Regular Expressions) — default in sed
  ( ) { } + ?    are LITERAL — must escape to get metacharacter behavior
  \( \) \{ \}    are the ACTUAL grouping/quantifier metacharacters
  |              is LITERAL — no alternation in BRE

ERE (Extended Regular Expressions) — enabled with sed -E
  ( ) { } + ? |  are metacharacters — no escaping needed
  \( \)          are literal parens in ERE

Examples:
  BRE: sed 's/\(foo\)\(bar\)/\2\1/'
  ERE: sed -E 's/(foo)(bar)/\2\1/'

  BRE: sed 's/[0-9]\{2,4\}/NUM/'
  ERE: sed -E 's/[0-9]{2,4}/NUM/'

POSIX character classes (portable across both):
  [[:alpha:]]   [[:digit:]]   [[:alnum:]]
  [[:space:]]   [[:blank:]]   [[:upper:]]   [[:lower:]]
  [[:punct:]]   [[:print:]]
```

---

## What Makes sed Distinct

- **Speed**: faster than awk/perl for simple s// on large files — minimal parsing overhead
- **Ubiquity**: present on every Unix system; guaranteed available in shell scripts
- **In-place editing**: `sed -i` is the canonical way to modify files in shell pipelines
- **Hold space**: the one cross-line state mechanism; technically makes sed Turing-complete
- **Line-based model**: no concept of "variables" or "program flow" — purely address+command pairs
- **Composability**: trivially pipes with grep, awk, sort, cut — the Unix text tool chain

---

## Gotchas & Traps

| Trap | Issue | Fix |
|------|-------|-----|
| `-i` without `''` on macOS | `sed -i 's/a/b/' file` fails on BSD — expects suffix arg | `sed -i '' 's/a/b/' file` on macOS |
| BRE vs ERE | Default is BRE: `(`, `)`, `+`, `?` are literal characters | Use `-E` for ERE; or escape `\(`, `\+` in BRE |
| `\w` on macOS | Not in BSD sed | Use `[[:alnum:]_]` for portability |
| No non-greedy | `s/a.*b/x/` matches longest `a...b` | sed has no `.*?` — use negated class: `[^b]*` |
| `&` in replacement | `&` = entire match; to get literal `&` use `\&` | `s/foo/\&/` inserts literal `&` |
| Newline in pattern | `/\n/` won't match in single-line mode | Use `N` to pull next line into pattern space first |
| `d` skips remaining commands | After `d`, no further commands run for that line | Structure scripts so `d` is the last action |
| BSD step address | `1~2` (every other line) is GNU-only | Use awk or a counter loop for BSD |
| `0,/pat/` GNU-only | Zero address for first-line match is GNU extension | On BSD, `1,/pat/` skips the match if it's on line 1 |
| Backup extension typo | `sed -i.bak` creates `file.txtbak` not `file.txt.bak` | `sed -i .bak` (with space) or `sed -i'.bak'` |

---

## Decision Cheat Sheet

| Task | Tool |
|------|------|
| Simple `s///` in-place file edits | sed (or `perl -i` for portability) |
| Delete lines matching a pattern | sed `/pattern/d` |
| Print line ranges | sed `-n '10,20p'` |
| Insert/append lines at a pattern | sed `a\` / `i\` |
| Fastest stream edit on large files | sed beats awk/perl for pure s// |
| Multi-column field processing | awk |
| Arithmetic or aggregation | awk |
| Non-greedy regex | Perl |
| Complex logic / loops | Perl or awk |
| Multiple transforms per line with conditions | Perl |
| Cross-platform portability | `perl -i.bak -pe 's/a/b/g'` |
| Unicode-aware text processing | Perl with `use utf8` |
