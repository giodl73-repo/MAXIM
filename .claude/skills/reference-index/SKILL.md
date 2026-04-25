# /reference-index — Cross-Cutting Concept Index

Build and maintain a cross-cutting concept index for the MAXIM reference library. The index maps concepts that appear substantively in 2+ sections — the connections you can't find by browsing a single directory.

## Usage

```
/reference-index build              — full build: scan all directories, generate CONCEPT-INDEX.md
/reference-index update <dir>       — re-scan one directory, merge into existing index
/reference-index update-section <s> — re-scan all dirs in a section, merge into existing index
/reference-index status             — index stats: entries, coverage, most cross-cutting concepts
/reference-index validate           — check all links resolve to existing files
```

---

## Index Design

**File**: `CONCEPT-INDEX.md` at repository root

**Inclusion rule**: A concept earns an entry when it is discussed substantively in **2+ different sections** (not just 2+ directories within the same section). This filters out low-value internal cross-references (e.g., topology → manifolds within Mathematics) and surfaces the genuinely cross-cutting connections.

**The 13 sections** (from CLAUDE.md):
1. Computing & Software
2. Mathematics & Physics
3. Mechanics
4. Technology
5. Life Sciences
6. Earth & Space
7. History & Ideas
8. Social Sciences
9. Language & Communication
10. Arts & Culture
11. Material Culture
12. Natural World
13. People

**Entry format**:

```markdown
**Concept name** — [dir/NN](dir/NN-FILENAME.md) · [dir/NN](dir/NN-FILENAME.md)
```

- Bold concept name, em-dash, MkDocs-linked references separated by ` · `
- Display text is `dir/NN` (short, scannable)
- Link target is `dir/NN-FILENAME.md` (resolves in MkDocs)
- References sorted by section order (Computing first, People last), then alphabetically within section

**File structure**:

```markdown
# Concept Index

*Cross-cutting concept index for the MAXIM reference library.
Entries appear only when a concept is discussed substantively in 2+ sections.
{N} entries across {M} directories. Last built: {date}.*

## A

**Entry** — [links]

## B

...
```

Alphabetical headers (## A through ## Z). Skip letters with no entries.

---

## Concept Extraction

For each .md file, extract the **3-5 most important technical concepts**:

### Where to Look

1. **## headings** — the major topic divisions (highest signal)
2. **Bold terms** in the first paragraph of each section
3. **Diagram labels** — key nodes, axes, named components
4. **Bridge concepts** — terms that explicitly connect to other fields
5. **Decision Cheat Sheet entries** — the "use X when Y" concepts

### What Qualifies as a Concept

- A **named technical idea** with a specific meaning: "Fourier transform", "Nash equilibrium", "control loop", "plate tectonics"
- NOT a general topic word: "introduction", "history", "applications", "overview"
- NOT a tool or product name unless it's a universal concept: "Docker" is not a concept; "containerization" is
- NOT a section of the style contract: "Decision Cheat Sheet" is format, not content

### Synonyms and Grouping

Group synonymous concepts under one canonical entry:

```markdown
**Entropy (Shannon / thermodynamic)** — [links]
```

Use the most widely recognized name. Add parenthetical variants when the concept has distinct flavors that readers might search for differently.

**Do NOT** create separate entries for:
- Singular vs plural ("eigenvalue" / "eigenvalues")
- Adjective forms ("Bayesian" → list under "Bayesian inference")
- Sub-concepts that are only meaningful within their parent ("UCL/LCL" → list under "statistical process control")

---

## Mode: `build`

Full build from scratch. This is the most expensive operation — reads every content file in the library.

### Process

1. **Parallel extraction** — Launch up to 8 agents, one per section group:

   | Agent | Sections | ~Directories |
   |-------|----------|-------------|
   | 1 | Computing & Software | ~10 |
   | 2 | Mathematics & Physics | ~20 |
   | 3 | Mechanics + Technology | ~23 |
   | 4 | Life Sciences | ~18 |
   | 5 | Earth & Space | ~14 |
   | 6 | History & Ideas + Social Sciences | ~31 |
   | 7 | Language & Communication + Arts & Culture | ~29 |
   | 8 | Material Culture + Natural World + People | ~35 |

   Each agent:
   a. Reads all .md files in its directories (skip STATUS.md, 00-OVERVIEW.md)
   b. Extracts 3-5 concepts per file with source `section:directory/NN-FILENAME`
   c. Returns a flat list: `concept → section:directory/NN-FILENAME`

2. **Merge** — Collect all agent results. Group by concept (canonicalize synonyms).

3. **Filter** — Keep only entries with references in **2+ different sections**.

4. **Generate** — Write `CONCEPT-INDEX.md` with the standard format.

5. **Report** — Output:
   - Total entries
   - Top 10 most cross-cutting concepts (most section references)
   - Entries per letter
   - Section coverage (which sections contribute most/least)

**Agent launch template:**

```
You are building a concept index for the MAXIM reference library.
Read reference\.claude\skills\reference-index\SKILL.md for the full specification.
Read reference\CLAUDE.md for the library structure and learner profile.

Extract concepts from these directories:
[list of directories for this agent]

For each directory:
1. List all .md files (skip STATUS.md and 00-OVERVIEW.md)
2. Read each file
3. Extract 3-5 key technical concepts per file
4. Record each as: concept_name → section_name:directory/NN-FILENAME.md

Return your results as a flat list, one entry per line:
concept_name | section_name | directory/NN-FILENAME.md

Use canonical concept names (see Synonyms and Grouping rules in the skill).
Do NOT write any files — just return the extracted data.
```

**Important:** Extraction agents should use `mode: bypassPermissions` but only need Read access. They do NOT write to any files — the main conversation handles the merge and write.

---

## Mode: `update <dir>`

Incremental update after a directory has been added or significantly revised.

1. Read the existing `CONCEPT-INDEX.md`
2. Remove all references to `<dir>` from existing entries
3. Re-scan `<dir>`: read all .md files, extract 3-5 concepts per file
4. For each extracted concept:
   a. If the concept already exists in the index → add the new reference
   b. If the concept is new AND it appears in another section → add a new entry
   c. If the concept is new but only in this section → skip (doesn't meet 2-section threshold yet)
5. Remove any entries that now have references in fewer than 2 sections (after the removal in step 2)
6. Rewrite `CONCEPT-INDEX.md`
7. Update the "Last built" date in the header
8. Stage and commit

---

## Mode: `update-section <section>`

Re-scan all directories in a section and merge. Same as running `update <dir>` for every directory in the section, but more efficient:

1. Read `CONCEPT-INDEX.md`
2. Remove all references from directories in `<section>`
3. Launch agents to re-scan all directories in the section (parallel, up to 8)
4. Merge results into existing index
5. Apply the 2-section filter
6. Rewrite and commit

---

## Mode: `status`

Report on the current index without modifying it.

1. Read `CONCEPT-INDEX.md`
2. Report:
   - Total entries
   - Entries per letter (A: 12, B: 8, ...)
   - Top 10 most cross-cutting concepts (most references)
   - Section contribution (how many entries reference each section)
   - Directories with zero index presence (gaps)
   - Last built date

---

## Mode: `validate`

Check every link in the index resolves to an existing file.

1. Parse all MkDocs links from `CONCEPT-INDEX.md`
2. For each link, check the file exists on disk
3. Report:
   - Total links checked
   - Broken links (file not found) with the entry they belong to
   - Orphaned files (content files not referenced by any index entry — informational, not an error)

---

## Quality Bar

A good index entry:
- Names a **specific concept**, not a topic area
- Has references in **2+ sections** that genuinely discuss the concept (not just mention it)
- Uses the **canonical name** a reader would search for
- Links to the **most relevant file** in each directory (not the overview)

A bad index entry:
- Is too broad ("mathematics", "engineering", "biology")
- Is too narrow ("equation 3.7 in stellar physics")
- References a file where the concept is only mentioned in passing
- Duplicates another entry under a different name
