# Reference Library — Expansion Process

Repeatable process for selecting and executing content expansion batches.
Used every time a new batch of directories is added.

---

## 1. Selection Criteria

New directories are chosen against these filters — all three must be true:

| Filter | Test |
|--------|------|
| **Coverage gap** | Domain not covered (or only a stub) in any existing directory |
| **Thematic coherence** | Fits into an identifiable intellectual cluster (pure math, earth systems, media history, etc.) |
| **Learner relevance** | Useful to a VP-level technical leader or enriches a domain the learner cares about |

**Avoid**:
- Directories that would duplicate 80%+ of an existing module
- Hyper-narrow topics better served as a section inside an existing guide
- Topics where the learner has no adjacent background and no clear entry ramp

---

## 2. Grouping Principles

Each batch is organized into 4 parallel writing groups for agent parallelism:

```
Batch N
├── Group NA  (3 directories, ~10-12 files each, ~30-36 files total)
├── Group NB  (3 directories, ~10-12 files each, ~30-36 files total)
├── Group NC  (3 directories, ~10-12 files each, ~30-36 files total)
└── Group ND  (3 directories, ~10-12 files each, ~30-36 files total)
```

**Grouping rules**:
- Keep thematically related directories together (earth science dirs together, math dirs together, etc.)
- Balance file counts across groups (~30-36 files per group)
- Each group gets exactly one writing agent — avoid cross-group dependencies

**File count per directory**:
- Minimum 8, maximum 14
- `00-OVERVIEW.md` is always file 0 — the landscape / taxonomy guide
- Files numbered `01` through `N` covering distinct subtopics
- `STATUS.md` is the internal manifest (not a content file; doesn't count toward the file total)

---

## 3. Stub Creation Format

Each new directory requires:

### STATUS.md (internal manifest)

```markdown
# {DirectoryName}/ — Status

## Files

| File | Topic | Status |
|------|-------|--------|
| 00-OVERVIEW.md | Landscape, taxonomy, key concepts | 🔜 |
| 01-TOPIC.md    | First subtopic | 🔜 |
| ...            | ... | 🔜 |

## Coverage Notes

One-paragraph summary of what the directory covers and what makes it distinct.
Key connections to other directories in the library.
```

### Content stubs

Each content file gets a minimal 3-line stub:

```markdown
# {Topic Title}

> Stub — to be written.
```

This ensures the file exists in the scaffolded tree and will be found by any tool
scanning the directory, even before content is written.

---

## 4. Agent Prompt Template

Use this template when launching each writing agent. Customize the bracketed fields.

```
You are writing Group {NA} of Batch {N} of the reference library at C:\src\reference.

DIRECTORIES: {dir1}/ ({N1} files), {dir2}/ ({N2} files), {dir3}/ ({N3} files)

LEARNER PROFILE (from C:\src\reference\CLAUDE.md):
- VP of Software Engineering, Microsoft, age 52
- MIT double major: Mathematics + Theoretical Computer Science
- Deep background: .NET, Azure, VSTS, ADO.NET, ADF, Power Query
- ~10-year leadership gap (not hands-on coder)
- Peer-level technical writing — no handholding
- Bridges to Azure/.NET/VSTS where natural

STYLE CONTRACT (follow computing/01-PACKAGE.md format exactly):
1. Big Picture diagram first — full landscape in one ASCII diagram
2. Layer downward — each section drills into one component
3. ASCII boxes for system diagrams, flow charts, decision trees
4. Tables for comparisons and cheat sheets
5. "Old world → new world" bridges where the learner has prior art
6. End each file with Decision Cheat Sheet + Common Confusion Points sections

INSTRUCTIONS:
1. Read C:\src\reference\CLAUDE.md for full learner profile
2. Read each directory's STATUS.md for planned file list and coverage notes
3. Write every file listed in each STATUS.md — full content, not stubs
4. Follow the format of computing/01-PACKAGE.md exactly
5. When you finish all files in a directory, update that directory's STATUS.md
   — change all 🔜 to ✅, add a completion timestamp
6. Token budget: keep each file under ~32,000 tokens; split to Part 1 / Part 2 if needed

DOMAIN-SPECIFIC NOTES:
{Any domain bridges, depth notes, or special instructions for this group}
```

---

## 5. TRACKER.md Update Checklist

Before launching agents:
- [ ] Add rows to Summary Dashboard table (one per new directory, status 🔜)
- [ ] Add new batch section at bottom (list groups, directories, file counts)
- [ ] Commit the scaffolding (TRACKER.md + STATUS.md stubs + content stubs)

After agents complete:
- [ ] Verify each STATUS.md shows all files ✅
- [ ] Update Summary Dashboard: change 🔜 → ✅ for each completed directory
- [ ] Update file counts if any files were added during writing
- [ ] Update the top-level file count summary line

---

## 6. Completion Verification

Run these before the final commit:

```bash
# Count total files
find C:/src/reference -name "*.md" | wc -l

# Check for unfinished stubs
grep -r "^> Stub" C:/src/reference --include="*.md" -l

# Verify STATUS.md completions
grep -r "🔜" C:/src/reference --include="STATUS.md" -l
```

All three should return clean results before declaring a batch done.

**Section landing page update pass** — after completing a batch, scan which `sections/*.md` files need new directory entries. Each new directory gets one row added to its section's Directories table and wired into the mkdocs.yml nav. Sections: `computing-software`, `mathematics-physics`, `engineering`, `life-sciences`, `earth-space`, `history-ideas`, `social-sciences`, `language-communication`, `arts-culture`, `material-culture`, `natural-world`.

---

## 7. Commit Sequence

```bash
# Stage everything in the new directories
git add C:/src/reference/<dir1>/ C:/src/reference/<dir2>/ ...

# Stage TRACKER.md and EXPANSION.md
git add C:/src/reference/TRACKER.md C:/src/reference/EXPANSION.md

# Commit
git commit -m "Add Batch N: 12 new reference directories, NNN files"
```

Commit message format: `Add Batch {N}: {X} new reference directories, {Y} files`

---

## Batch History

| Batch | Groups | Directories | Files | Date |
|-------|--------|-------------|-------|------|
| 1 | A–E | medicine, law, philosophy, aeronautics, cryptography, spices, pigments, colors, statistics-applied, textiles, plumbing, coatings, climate-science, jewelry, ceramics, glassmaking, organizational-behavior, hvac, political-science, psychology, geography | ~189 | 2026-02 |
| 2 | 2A–2D | construction-materials, architecture-history, electrical-grid, culinary-history, food-plants, botany, fermentation-spirits, games-history, sports-history, cartography, typography, watchmaking | ~131 | 2026-02 |
| 3 | 3A–3D | signal-processing, acoustics, telecommunications, semiconductor-manufacturing, geology, meteorology, ecology, agriculture, art-history, economic-history, military-history, history-of-science, metalworking, photography, nutrition, sociology | ~181 | 2026-02 |
| 4 | 4A–4D | robotics, optics, biomedical-engineering, formal-methods, energy-systems, anthropology, religious-studies, architecture, game-theory, transportation, urban-planning, environmental-engineering | ~96 | 2026-02 |
| 5 | 5A–5D | oceanography, hydrology, paleontology, number-theory, abstract-algebra, topology, printing-publishing, cinema-film, radio-television, public-health, demography, behavioral-economics | ~129 | 2026-02 |
