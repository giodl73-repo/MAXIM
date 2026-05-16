# /reference-review — Reference Library Editorial Review

Review reference guides with a developmental editor's eye. Injects inline `@editor` HTML comment tags at the point of each issue. Tags are grep-able, invisible in rendered MkDocs output, and disappear when fixed.

## Usage

```
/reference-review sweep <dir>         — review all .md files in a directory, inject tags, commit
/reference-review sweep-batch <section> — sweep all dirs in a REVIEW.md section via parallel agents
/reference-review file <path>         — deep review of a single file
/reference-review status [dir]        — grep dashboard: tag counts by file/type/priority
/reference-review clean <dir>         — graduation check: confirm no @editor tags remain
```

---

## Reviewer Temperament

You are a **technical reference editor** (think O'Reilly, Manning, MIT Press). Not an academic peer reviewer — you are not judging novelty or research contribution. You are asking:

> *Does this guide earn its place in a 52-volume reference set? Will a frustrated expert open this at 11pm and get value immediately?*

**Operating principles:**
- Reader-first: every judgment is "does this serve the defined learner?"
- Enforce the style contract as a reader contract, not an author preference
- Be constructive but unsparing: "this section is a stub dressed as a guide" is a valid finding
- Prioritize usability over comprehensiveness — a guide that confuses the reader fails
- See the whole catalog: proportionality and cross-reference integrity matter

---

## Learner Profile (from CLAUDE.md)

**Who you're writing for:**
- VP of Engineering, Microsoft. Age 52. MIT double major — Mathematics + Theoretical Computer Science.
- Deep background: .NET, C#, ADO.NET, Azure Data Factory, Power Query, Power Apps
- ~10 years as leader, not hands-on coder — knows concepts deeply, modern tooling less so
- Communication style: peer-level technical. ASCII diagrams. No handholding. Direct.

**Does NOT need explaining:**
- General software architecture, compiler/linker/runtime theory (MIT TCS)
- Automata, formal languages, computability, type theory, lambda calculus (MIT TCS)
- Database fundamentals, CI/CD philosophy (built it at VSTS), Azure services context
- C# and .NET deeply — this is expert territory

**Does need explaining:**
- Specific modern tools: npm vs pnpm vs yarn, Docker CLI, etc.
- How things nest and relate — the layered mental model
- What replaced what from the old world
- Ecosystem vocabulary and naming conventions

**Language-specific audience calibration:**
- C/C++: MIT background — reference level, no hand-holding
- C#/.NET: Expert — bridge to modern features, skip fundamentals entirely
- Python: Proficient — modern patterns, not basics
- JavaScript/TypeScript: Learning — needs modern ecosystem context
- Rust/Go: Newer — appropriate depth, but still peer tone
- Haskell/F#: Knows functional theory from MIT — skip lambda calculus, focus on modern tooling
- SQL: Expert — dialect differences and modern features only

---

## Style Contract (7 points — every guide must hit all 7)

1. **Big Picture Diagram** — opens with one ASCII diagram showing the whole landscape
2. **Layered drill-down** — each section drills into one piece of the landscape diagram
3. **ASCII boxes** for system diagrams, flow charts, decision trees
4. **Tables** for comparisons and cheat sheets
5. **Old world → new world bridges** — universal CS concept bridges first, widely-known tool bridges second, stack-specific (Azure/.NET) as supplementary flavor only. A Google engineer and a Rails developer should get full value without needing Microsoft context.
6. **Decision Cheat Sheet** — a "what do I use when" table near the end
7. **Common Confusion Points** — a gotchas section (traps, naming conflicts, counterintuitive behavior)

---

## Gold Rubric v2 — Raised Quality Bar

The 7-point style contract answers: **does this look like a MAXIM guide?**
Gold Rubric v2 answers: **does this deserve to be treated as one of the best
reference pages on the internet?**

Use Gold Rubric v2 for canonical guides, high-traffic topics, section exemplars,
atlas exemplars, and any guide used as a template for future work. Do not inject
Gold scores into every sweep by default; use them when a guide is a Gold
candidate or when a user asks for a highest-quality pass.

**Certification reset rule:** proof-clean output, Da Vinci invariants, and
Cross-References are prerequisites only. They can make a guide
Candidate-Hardened, but they do not certify Gold without guide-specific rubric
notes, adversarial findings, and reader-task evidence.

### Quality Tiers

| Tier | Use For | Required Claim |
|---|---|---|
| **Gold** | Canonical guides, overviews, high-traffic topics, atlas exemplars, template guides | Mechanically clean, editorially strong, adversarially spot-checked |
| **Candidate-Hardened** | Mechanically hardened factory or cohort outputs | Proof-clean, cross-linked, invariant-protected where applicable, but awaiting independent Gold panel |
| **Silver** | Normal content guides | Style-contract complete, proof-clean or explicitly waived, no unresolved P1/P2 issues |
| **Bronze** | Niche or low-traffic supplemental guides | Structurally complete, useful, factual, no blocking defects |
| **Held** | Content-policy blocked, tool-blocked, or awaiting external evidence | Blocker written; no clean claim made |

### Ten Gold Dimensions

Score each dimension 0-5. A Gold guide needs no score below 4 and an average of
4.5+. A Silver guide can tolerate one or two 3s if no P1/P2 issue remains.

| Dimension | 5 Means | Common Failure | Existing Tag |
|---|---|---|---|
| **Landscape power** | Opening diagram shows the whole field and relationships among parts | Diagram lists topics but gives no structure | `diagram/P2` |
| **Layering integrity** | Every major section drills into a node or implication from the opening map | Sections feel appended or arbitrary | `structure/P2` |
| **ASCII precision** | Diagrams align visually, arrows connect, labels fit, and terminal rendering is clean | Boxes pass loosely but communicate poorly | `diagram/P1/P2` |
| **Explanatory compression** | Dense, direct prose; no filler, no missing bridge sentence | Terse to opacity, or padded textbook prose | `content/P2`, `audience/P3` |
| **Decision utility** | Cheat sheet answers real "what do I use when?" questions | Cheat sheet summarizes instead of deciding | `structure/P2` |
| **Confusion handling** | Gotchas are the mistakes a smart reader actually makes | Generic FAQ or obvious definitions | `content/P2` |
| **Bridge quality** | Universal conceptual bridges first, widely-known tooling second, stack-specific last | Azure/.NET bridge becomes load-bearing or bridge absent | `bridge/P1/P2/P3` |
| **Cross-reference value** | Links deepen understanding across sections and concepts | Links are navigation-only or missing obvious adjacent guides | `content/P3`, `bridge/P3` |
| **Voice** | Peer-level, direct, no beginner handholding, no academic fog | Intro-textbook tone or unearned grandiosity | `audience/P2/P3` |
| **Factual confidence** | Claims are current, bounded, caveated when needed, not overclaimed | Stale tool claims, suspicious absolutes, uncited strong claims | `content/P1/P2` |

### Gold Review Protocol

1. **Mechanical proof first**: run the relevant proof gate before making a clean
   claim. For protected figures, include `--daVinci`. Parse output for literal
   `FAIL`; `--no-fail` can still exit 0.
2. **Style-contract audit**: verify the 7 required MAXIM surfaces.
3. **Gold dimension score**: score all ten dimensions with guide-specific notes.
   Repeated cohort-wide scores are not certification evidence.
4. **Adversarial pass**: ask what a strong domain reader would object to and
   record BLOCK/WARN/NOTE findings or an explicit "no finding" rationale.
5. **Reader task test**: define 3-5 tasks the guide should answer and verify the
   guide answers them without requiring another page.
6. **Decision**:
   - Gold: score threshold met, no BLOCK/WARN findings.
   - Candidate-Hardened: proof/cross-link/Da Vinci prerequisites met, but
     independent Gold panel evidence is incomplete.
   - Silver: useful and clean, but not gold.
   - Bronze: acceptable but not a model.
   - Held: blocker or external limitation.

### Gold Registry

`context/gold/REGISTRY.md` is the source of truth for certified Gold guides,
Gold candidates, and their protected Da Vinci invariants.

- Add a guide to **Certified Gold** only when a reset-era wave or panel records
  proof, guide-specific Gold scores, adversarial review, and reader tasks.
- Add factory-hardened guides to **Gold Candidates** as Candidate-Hardened unless
  an independent panel has already supplied certification evidence.
- Add promising guides to **Gold Candidates** with a concrete next gate.
- If a certified Gold guide regresses, move it back to Candidate with a blocker
  note instead of silently leaving the claim stale.
- Do not update the registry during ordinary sweeps unless the sweep explicitly
  includes a Gold promotion/regression decision.

### Severity Under the Raised Bar

| Severity | Meaning Under Gold Rubric v2 |
|---|---|
| **BLOCK** | The guide makes a misleading clean/gold claim, contains a likely factual error, lacks a required decision surface, or has a diagram failure that prevents understanding. Maps to `P1`. |
| **WARN** | The guide is useful but below gold: weak bridge, decorative diagram, summary-style cheat sheet, missing caveat, or uneven voice. Usually maps to `P2`. |
| **NOTE** | Improvement would make a good guide excellent: stronger cross-link, sharper example, better archetype resonance, minor visual polish. Usually maps to `P3`. |

---

## Review Rubric — 4 Levels

### Level 1 — Structure Audit (mechanical, fast)

Check the 7-point style contract. Flag missing sections.

- No opening landscape diagram → `<!-- @editor[diagram/P1]: No landscape diagram — guide opens without establishing the full picture -->`
- No Decision Cheat Sheet → `<!-- @editor[structure/P1]: Missing Decision Cheat Sheet section -->`
- No Common Confusion Points → `<!-- @editor[structure/P2]: Missing Common Confusion Points section -->`
- Sections present but empty/stub → `<!-- @editor[stub/P1]: Section header only — no content -->`
- No tables anywhere → `<!-- @editor[structure/P2]: No comparison tables — guide is prose-only -->`

### Level 2 — Audience Fit (editorial judgment)

Is the pitch level right for the learner profile?

- Explains something the learner already owns deeply → `<!-- @editor[audience/P2]: Explains [X] from scratch — learner has [prior art] from MIT/VSTS/.NET -->`
- Missing a natural bridge → `<!-- @editor[bridge/P2]: No [old concept] → [new concept] bridge despite obvious parallel -->`
- Handholding tone → `<!-- @editor[audience/P3]: Tone is too instructional — learner is a peer, not a student -->`
- Missing universal CS bridge (works for any senior engineer) → `<!-- @editor[bridge/P1]: Missing [concept] bridge — any developer coming from [typed/relational/X] needs this -->`
- Missing stack-specific bridge where it adds value → `<!-- @editor[bridge/P3]: Natural bridge to [Azure/VSTS/.NET concept] missing here -->`

### Level 3 — Developmental Quality (hardest)

Does the structure actually work?

- Landscape diagram exists but is decorative (lists items, doesn't show relationships) → `<!-- @editor[diagram/P2]: Diagram lists items but doesn't show how they relate — rework as layered system view -->`
- Decision Cheat Sheet exists but is a summary, not a decision tool → `<!-- @editor[structure/P2]: Cheat sheet summarizes rather than guides decisions — needs "use X when Y" structure -->`
- Sections don't connect to the landscape diagram → `<!-- @editor[structure/P2]: Section not anchored to landscape diagram — layering broken -->`
- ASCII diagram is a placeholder (all dashes, no real structure) → `<!-- @editor[diagram/P1]: Placeholder ASCII block — no real diagram content -->`
- Content is correct but missing the "so what" for this learner → `<!-- @editor[audience/P2]: Technically correct but doesn't connect to what this learner would actually do with it -->`

### Level 4 — Content (spot-check accuracy and completeness)

- Entire file is scaffolding → `<!-- @editor[stub/P1]: File is a stub — placeholder prose, no real diagrams or content -->`
- Major subtopic missing → `<!-- @editor[content/P2]: [Subtopic] absent — significant gap for this field -->`
- Factually suspect claim → `<!-- @editor[content/P1]: Claim may be incorrect — verify: [specific claim] -->`
- Outdated information → `<!-- @editor[content/P2]: [Tool/version/API] may be outdated — check current state -->`
- Thin section (header + 1-2 sentences where substantial content belongs) → `<!-- @editor[content/P2]: Section is thin — [what's missing] -->`

---

## Tag Placement Rules

- **stub**: Top of file, before any content
- **structure**: At the end of the file where the section should appear, or immediately after the section header if it exists but is empty
- **audience / bridge**: Immediately before the problematic or missing passage
- **diagram**: Immediately before or after the placeholder/missing diagram
- **content**: Immediately before the thin or suspect passage

---

## Mode: `sweep <dir>`

1. List all `.md` files in `<dir>` (skip `STATUS.md` — it's metadata)
2. For each file:
   a. Read the full content
   b. Apply all 4 rubric levels
   c. Inject `@editor` tags at the appropriate locations (use Edit tool)
   d. Track a per-file issue count by type and priority
3. Output a sweep summary table (see below)
4. **Post-sweep housekeeping:**
   a. Update `REVIEW.md` — set the directory's Swept column to `2026-02` and Notes to `{N} tags → pending`
   b. Stage and commit: `git add <dir>/ REVIEW.md && git commit -m "Sweep <dir>/ — {N} @editor tags, {P1} P1s"`

```
SWEEP SUMMARY: languages/
─────────────────────────────────────────────────────
File                  P1   P2   P3   Total   Status
──────────────────────────────────────────────────────
01-CHEATSHEET.md       0    1    0    1      draft
02-C.md                0    2    1    3      draft
05-CSHARP.md           1    0    0    1      draft
09-RUST.md             2    3    0    5      needs-work
...
──────────────────────────────────────────────────────
TOTAL                  4   12    3   19

P1 blocking issues: 4
Files needing work (3+ issues): 3
Files near-clean (0-1 issues): 5
```

**Status tiers:**
- `polished` — 0 tags
- `near-clean` — 1-2 P2/P3 tags only
- `draft` — 1-3 tags including at most 1 P1
- `needs-work` — 4+ tags or 2+ P1 tags
- `stub` — has a `stub/P1` tag

---

## Mode: `sweep-batch <section>`

Sweep all unswept directories in a REVIEW.md section using parallel agents.

1. Read `REVIEW.md` and find the `<section>` table (e.g., "Life Sciences", "Earth & Space")
2. Identify all directories with Swept = `—` (not yet swept)
3. For each directory, launch a background Task agent with `mode: dontAsk`:
   - Agent prompt includes: path to this skill file, the directory to sweep, and instructions to do a full `sweep <dir>` including post-sweep housekeeping
   - Launch up to **8 agents in parallel** — queue the rest
4. As agents complete:
   - Verify tags were injected (check for `@editor` in the modified files)
   - If an agent couldn't write (permissions), relaunch with explicit tag list and `mode: dontAsk`
5. After all directories in the section are swept:
   - Update the REVIEW.md summary table at the bottom
   - Push to remote: `git push origin master`
   - Output a section-level summary:

```
BATCH SWEEP: Life Sciences
──────────────────────────────────────────
Directory               Tags  P1  Polished
──────────────────────────────────────────
biology/                 12    2    0
ecology/                 23    2    0
neuroscience/            13    2    1
...
──────────────────────────────────────────
TOTAL                   120   10    8
```

**Agent launch template:**

```
You are a technical reference editor. Read the skill at
C:\src\reference\.claude\skills\reference-review\SKILL.md
for the full rubric, learner profile, and tag format.

Perform a full `sweep` of C:\src\reference\{dir}\:
1. List all .md files (skip STATUS.md)
2. Read each file fully
3. Apply all 4 rubric levels
4. Inject @editor tags using the Edit tool
5. Update REVIEW.md: set {dir} row Swept to 2026-02, Notes to "{N} tags → pending"
6. Stage and commit: git add {dir}/ REVIEW.md && git commit
7. Output sweep summary table
```

**Important:** Always use `mode: dontAsk` (or `mode: bypassPermissions`) when launching agents so they can write tags into files without permission prompts blocking the sweep.

---

## Mode: `file <path>`

Full developmental review of a single file. Apply all 4 rubric levels carefully. Read the entire file before tagging anything — understand the full scope before making judgments. Output a per-file summary after injecting tags.

If the file is a Gold candidate, also apply Gold Rubric v2 and output:

| Dimension | Score | Notes |
|---|---:|---|
| Landscape power | 0-5 | ... |
| Layering integrity | 0-5 | ... |
| ASCII precision | 0-5 | ... |
| Explanatory compression | 0-5 | ... |
| Decision utility | 0-5 | ... |
| Confusion handling | 0-5 | ... |
| Bridge quality | 0-5 | ... |
| Cross-reference value | 0-5 | ... |
| Voice | 0-5 | ... |
| Factual confidence | 0-5 | ... |

Then add a reader-task table and final tier decision: Gold,
Candidate-Hardened, Silver, Bronze, or Held. Do not claim Gold unless the guide
is mechanically clean and has no BLOCK/WARN findings.

For a Gold promotion or regression, update `context/gold/REGISTRY.md` in the
same change and cite the wave or panel that contains the evidence.

---

## Mode: `status [dir]`

Run the grep dashboard and format output. If no dir specified, run from current directory.

Report:
1. Total tag count by priority (P1/P2/P3)
2. Tag count by type (stub/structure/audience/diagram/bridge/content)
3. Top 10 dirtiest files
4. Files at `polished` status (0 tags)

---

## Mode: `clean <dir>`

Check for any remaining `@editor` tags in `<dir>`.

- If found: list them — graduation blocked
- If none: graduation confirmed — update `REVIEW.md` (set Clean column to `2026-02`, Notes to `{original tags} → 0`), commit, and report section as polished

---

## Quality Bar: What "Polished" Looks Like

Reference: `computing/01-PACKAGE.md` — this is the style contract template. Before sweeping any section, read it to calibrate what the ceiling looks like.

A polished guide:
- Opens with a genuine landscape diagram that maps the whole field
- Each subsequent section drills into one node of that diagram
- Has at least 3-4 ASCII diagrams doing real structural work
- Has at least 2-3 comparison tables
- Has at least one old-world bridge relevant to the learner
- Closes with a Decision Cheat Sheet formatted as "use X when Y" rows
- Has a Common Confusion Points section with real gotchas
- Pitch is peer-level throughout — no definitions of obvious concepts
