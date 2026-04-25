# glint Findings — languages/ scan

**Run date:** 2026-04-25  
**Tool:** glint v0.2  
**Scope:** `languages/` directory (20 files)  
**Config:** root `glint.toml` + `languages/glint.toml`

---

## Full-Library Scan Summary (after algorithm fixes)

```
files:    2,866  (across all 217+ subject directories)
errors:   47,322
warnings: 12,193

By error code (full library):
  ascii_box_col         30,907   column separator misaligned
  ascii_box_width       21,975   row/border width mismatch
  ascii_cell_padding     5,415   missing cell padding
  ascii_connector_drift    661   vertical connector drift
  ascii_arrow_gap          101   gap in horizontal arrow
  md_missing_section       354   missing required section (Decision Cheat Sheet)
  md_missing_pattern       100   missing required code block
  md_h1_count                2   genuine extra H1 headings (only 2 in entire library)
```

## Languages/ Scan Summary (initial run)

```
files:    20
errors:   388 → 293 (after Pattern C fix)
warnings: 271 → 201

By error code:
  ascii_box_col       376   column separator at wrong visual column
  ascii_box_width     183   row/border width mismatch
  ascii_cell_padding   71   missing whitespace inside box cell
  ascii_connector_drift 27  │ connector drifts column between lines
  ascii_arrow_gap       2   gap inside horizontal arrow body
```

**Errors per file (sorted by count):**
```
10-GO.md          114   worst — outer box ±1 across many rows
14-SWIFT.md        77   similar pattern to Go
03-CPP.md          76   mixed issues
07-JAVASCRIPT.md   52   systematic ±1 offset in multiple boxes
09-RUST.md         51   similar
11-HASKELL.md      41   similar
15-SCALA.md        40
04-JAVA.md         40
05-CSHARP.md       38
12-FSHARP.md       30
08-TYPESCRIPT.md   28
00-OVERVIEW.md     16
02-C.md            16
06-PYTHON.md       16
16-RUBY.md         13   all connector_drift (warnings, not errors)
13-KOTLIN.md        5   annotation-outside-box issue
01-CHEATSHEET.md    4   connector_drift warnings
17-SQL.md           2   one row with extra trailing space
```

---

## Top Directories by Error Count

```
journalism             3,077   Pattern F (side-by-side boxes) + Pattern A
mythology              2,637   Pattern A + B (systematic ±1 across all guides)
microbiology           1,958
construction-materials 1,784
rope-cordage           1,662
astronomy              1,623
immunology             1,563
masonry                1,423
scripting              1,355   Pattern G (inline floating boxes)
mathematics            1,345   Pattern A (±1, ±2 width in equation diagrams)
```

## Cross-Section Pattern Survey

| Section | Dominant Pattern | Notes |
|---------|-----------------|-------|
| languages/ | A (trailing space ±1) | Systematic across all guides |
| journalism/ | F (side-by-side boxes) | 3 boxes per landscape diagram |
| scripting/ | G (inline floating box) | Box to right of free text |
| mathematics/ | A (±1, ±2 width) | Complex equation boxes |
| codes/ | A + F | Pattern F dominant |
| oral-tradition/ | F (multi-column) | Side-by-side structure |
| periodic-table/ | F (2-col off) | Consistent ±2 across rows |

---

## Error Patterns

### Pattern A — Trailing space ±1 (HIGH confidence fix)

**What:** A content row is exactly 1 char wider or narrower than the box border.
The extra/missing char is a trailing space before the closing `│`.

**Example (SQL.md line 47):**
```
BORDER:  ┌────────────────────────────────────────────────────────────────┐  (69 wide)
BAD:     │  • Join algorithm: nested loop vs hash join vs merge join       │  (70 wide)
FIXED:   │  • Join algorithm: nested loop vs hash join vs merge join      │  (69 wide)
```

**Fix:** Remove or add exactly one trailing space before the closing `│`.

**Files affected:** Most files have at least some of these.  
**Fix confidence:** HIGH — arithmetic is unambiguous.  
**AI instruction:** Count chars in border vs content row; add/remove spaces at the right margin.

---

### Pattern B — Annotation after closing `│` (MEDIUM confidence fix)

**What:** A content row has text appended AFTER the closing `│`, making it wider than the box.
Common pattern: `│  content  │  ← explanation` or `│  content  │  # comment`.

**Example (Kotlin.md line 48):**
```
BORDER:  ┌───────────────────────────────────┐  (39 wide)
BAD:     │           JVM Runtime             │  ← same JVM as Java  (59 wide)
```

**Fix options:**
1. Move annotation to a comment line below the box (preferred)
2. Remove annotation
3. Widen the box to accommodate — but then the annotation needs its own column

**Files affected:** Kotlin.md, possibly others.  
**Fix confidence:** MEDIUM — the fix direction is clear but involves content judgment.  
**Schema implication:** This is already caught by `ascii_box_width`. No new rule needed.
Going forward: annotations must go outside code blocks or use a second cell with proper delimiter.

---

### Pattern C — Nested box false bottom-border detection (LOW confidence)

**What:** When a multi-box flowchart has a closing border (`└──┘`) immediately followed
by content lines and then an opening border (`┌──┐`), glint detects the closing border
as the TOP of a new box and the intermediate lines (arrows `▼`, text, whitespace) as
"content" of a phantom box. This generates many spurious errors.

**Example (Kotlin.md lines 41-47):**
```
41: └────────────────────────────────────────────────────────┘   ← real bottom border
42:        │
43:        ▼
44:   .class files (identical format to javac output)
45:        │                                                    ← glint sees this as a
46:        ▼                                                       "box" from 41 to 47
47: ┌───────────────────────────────────┐                       ← glint sees as bottom
```

The intermediate lines have wildly different widths → many `ascii_box_width` errors.

**Root cause:** `find_boxes()` greedily pairs any two consecutive border lines as
top/bottom of a box. A `└──┘` border is visually a BOTTOM border, not a TOP border.
The algorithm doesn't distinguish top-opening (`┌`) from bottom-closing (`└`) borders.

**Glint fix (future algorithm improvement):** Require that the top border of a box
contains `┌/╔/╭/+` corner chars (not `└/╚/╰`). A bottom-left corner opening a box
is semantically wrong.

**Content fix (not recommended):** Restructuring the flowchart. But the diagram is
visually correct — this is a detection false positive.

**Files affected:** Go.md (major), Kotlin.md, Scala.md, possibly others.  
**Fix confidence:** LOW for content edits. OPEN for algorithm fix.  
**Status:** Needs glint algorithm improvement (BENCH/PARSE issue).

---

### Pattern D — Connector drift in flowcharts (WARNING only)

**What:** A `│` connector character in a multi-branch flowchart appears at a slightly
different visual column than the `│` on the line above. Drifts of 1-3 columns.

**Example (Ruby.md):**
```
line 190: │ at col 14 drifted 1 from col 13 above
line 190: │ at col 16 drifted 3 from col 13 above
```

**Pattern:** These are in complex flowcharts where multiple branches split and rejoin.
Alignment is often intentional or reflects the branching structure.

**Fix confidence:** LOW — connector drift in flowcharts is often intentional art.
The `ascii_connector_drift` check may be too strict for complex branching diagrams.

**Schema consideration:** May want `check_arrow_alignment = false` in some section schemas,
or increase the drift tolerance for non-box flowcharts.

**Files affected:** Ruby.md (13), CHEATSHEET.md (4), others.

---

### Pattern E — Multiple `|`/`│` in a non-box context

**What:** Some content (especially cheatsheet comparison tables inside code blocks)
has `│` separators that glint's cell-padding check fires on. The content isn't actually
a cell-padded box but gets checked because the heuristic isn't tight enough.

**Files affected:** 01-CHEATSHEET.md, possibly others.  
**Fix confidence:** N/A — these may be false positives from cell padding check.

---

## Fix Strategy — Typed Passes

The key insight: **run one pass per error category, not one pass per file**.
Each pass handles a single pattern type across all files, with one uniform fix strategy.
This is safer (one change type at a time), produces cleaner diffs, and makes review easy.

```
Pass 1 — Pattern A: trailing-space width errors (±1 char)
  glint check --format rich | filter: ascii_box_width, abs_diff == 1
  fix-guide: add/remove trailing space
  fix: apply
  check: verify zero pattern-A errors remain
  commit

Pass 2 — Pattern C: false-bottom-border algorithm fix in glint
  Fix find_boxes() to reject └/╚/╰ as box top borders
  Re-run check → how many errors disappear?
  commit

Pass 3 — Pattern B: annotation-outside-box
  filter: ascii_box_width, abs_diff > 5 (large width jump → annotation)
  fix-guide: move annotation to separate line
  review diff
  commit

Pass 4 — Pattern D: connector drift (warnings only)
  Assess: are these real problems or intentional art?
  Consider: raise drift tolerance in languages/glint.toml, OR disable connector check
  commit schema change

Pass 5 — Pattern E: cell padding false positives
  Investigate cheatsheet file
  Adjust: exclude 01-CHEATSHEET.md from cell padding check if false positives confirmed
```

**Why this order:**
1. Pattern A is safe and mechanical — do it first, clear the obvious noise
2. Pattern C (algorithm fix) potentially eliminates many errors without content edits — high leverage
3. Pattern B requires content judgment — do after noise is cleared
4. D and E are warnings/false positives — last, lowest risk

### Phase 1 — High confidence fixes (automated)
Run fix-guide on Pattern A errors: add/remove exactly 1 trailing space.
- Target: 17-SQL.md (2), simple rows in 10-GO.md, 07-JAVASCRIPT.md, etc.
- Expected: ~80-100 high-confidence fixes

### Phase 2 — Medium confidence fixes (review)
Pattern B annotation-outside-box: move inline comments.
- Target: Kotlin.md, any others with `│ ... │ annotation` pattern.

### Phase 3 — Algorithm fix (glint)
Pattern C false detection: update `find_boxes()` to distinguish `┌` (opens box) from
`└` (closes box). Bottom-close corners cannot be box tops.
- Expected impact: large reduction in false positives across all files.

### Phase 4 — Schema adjustment
- Reduce `ascii_connector_drift` sensitivity or disable for flowchart-heavy sections.
- Or raise the drift tolerance from strict `> 0` to `> 2`.

---

## Schema Findings

- F# guide (12-FSHARP.md) is missing `## Decision Cheat Sheet` — real structural gap.
- All other 15 language guides have the 3 required sections.
- Overview and cheatsheet correctly excluded from per-guide requirements.

---

## Algorithm Fixes Applied to glint (no content edits)

| Fix | Impact |
|-----|--------|
| Pattern C: `can_open_box()` guard | −95 errors in languages/, estimated −thousands library-wide |
| Pattern G: skip zero-separator rows | −600 `ascii_box_width` across library |
| md_h1_count code-block mask | −2,481 false positive H1 warnings |
| `paths_exclude` prefix bug | Fixed schema application on Windows and subdirectory configs |

---

## False Positives Found During Draft Review

### FP-01: md_heading_format fires on C# and F# language names

**Trigger:** `## Gotchas from C#`, `# Language: F#`, `### F#`  
**Why:** The trailing-`#` check found headings ending with `#`. But `C#` and `F#` are language names, not markdown decoration.  
**Fix:** Only flag trailing `#` when the character before it is whitespace — `## Title ##` (space before `##`) is decoration; `## Gotchas from C#` (no space before `#`) is a name.  
**Count:** 17 false positives eliminated from the languages/ scan.  
**Lesson:** Heuristics using punctuation as structural markers must account for punctuation in human-readable identifiers. C#, F#, C++, Obj-C are the common cases in this library.

---

## Open Questions

1. Should connector drift warnings be disabled for the languages/ section?
2. Should the false bottom-border fix (Pattern C) go in glint before the plan is generated?
3. Are the Pattern B annotation-after-`│` cases consistent enough to fix programmatically?
