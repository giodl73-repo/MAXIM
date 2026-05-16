# Gold Rubric v2

## Purpose

The original MAXIM style contract answers: *does this guide look like a MAXIM
guide?* Gold Rubric v2 answers: *does this guide deserve to be treated as one of
the best reference pages on the internet?*

This rubric does not replace `@editor` tags. It raises the judgment behind them.

## Quality Tiers

| Tier | Use For | Required Claim |
|---|---|---|
| **Gold** | canonical guides, overviews, high-traffic topics, atlas exemplars, guides used as templates | mechanically clean, editorially strong, adversarially spot-checked |
| **Silver** | normal content guides | style-contract complete, proof-clean or explicitly waived, no unresolved P1/P2 issues |
| **Bronze** | niche or low-traffic supplemental guides | structurally complete, useful, factual, no blocking defects |
| **Held** | content-policy blocked, tool-blocked, or awaiting external evidence | blocker written; no clean claim made |

## Ten Gold Dimensions

Each dimension scores 0-5. A Gold guide needs no score below 4 and an average of
4.5+. A Silver guide can tolerate one or two 3s if no P1/P2 issue remains.

| Dimension | 5 Means | Common Failure | Existing Tag |
|---|---|---|---|
| **Landscape power** | Opening diagram shows the whole field and relationships among parts | diagram lists topics but gives no structure | `diagram/P2` |
| **Layering integrity** | Every major section drills into a node or implication from the opening map | sections feel appended or arbitrary | `structure/P2` |
| **ASCII precision** | Diagrams align visually, arrows connect, labels fit, and the terminal rendering is clean | boxes pass loosely but communicate poorly | `diagram/P1/P2` |
| **Explanatory compression** | Dense, direct prose; no filler, no missing bridge sentence | terse to the point of opacity, or padded textbook prose | `content/P2`, `audience/P3` |
| **Decision utility** | Cheat sheet answers real "what do I use when?" questions | cheat sheet summarizes instead of deciding | `structure/P2` |
| **Confusion handling** | Gotchas are the mistakes a smart reader actually makes | generic FAQ or obvious definitions | `content/P2` |
| **Bridge quality** | Universal conceptual bridges first, widely-known tooling second, stack-specific last | Azure/.NET bridge becomes load-bearing or bridge absent | `bridge/P1/P2/P3` |
| **Cross-reference value** | Links deepen understanding across sections and concepts | links are navigation-only or missing obvious adjacent guides | `content/P3`, `bridge/P3` |
| **Voice** | Peer-level, direct, no beginner handholding, no academic fog | "intro textbook" tone or unearned grandiosity | `audience/P2/P3` |
| **Factual confidence** | Claims are current, bounded, caveated when needed, and not overclaimed | stale tool claims, suspicious absolutes, uncited strong claims | `content/P1/P2` |

## Severity Under the Raised Bar

| Severity | Meaning Under Gold Rubric v2 |
|---|---|
| **BLOCK** | The guide makes a misleading clean/gold claim, contains a likely factual error, lacks a required decision surface, or has a diagram failure that prevents understanding. Maps to `P1`. |
| **WARN** | The guide is useful but below gold: weak bridge, decorative diagram, summary-style cheat sheet, missing caveat, or uneven voice. Usually maps to `P2`. |
| **NOTE** | Improvement would make a good guide excellent: stronger cross-link, sharper example, better archetype resonance, minor visual polish. Usually maps to `P3`. |

## Gold Review Protocol

1. **Mechanical proof first**: no broken Markdown/table/ASCII issues in the chosen gate.
2. **Style-contract audit**: landscape, layering, diagrams, tables, bridges,
   decision cheat sheet, common confusions.
3. **Gold dimension score**: score all ten dimensions 0-5.
4. **Adversarial pass**: ask what a strong domain reader would object to.
5. **Reader task test**: define 3-5 tasks the guide should answer; verify it
   answers them without requiring another page.
6. **Decision**:
   - Gold: score threshold met, no BLOCK/WARN findings.
   - Silver: useful and clean, but not gold.
   - Bronze: acceptable but not a model.
   - Held: blocker or external limitation.

## Reader Task Test

Each Gold candidate gets a task table:

| Task | Guide Must Answer |
|---|---|
| "What is the whole landscape?" | Opening diagram plus first paragraph |
| "Which option should I choose?" | Decision Cheat Sheet |
| "What will I misunderstand?" | Common Confusion Points |
| "How does this connect to what I already know?" | Bridge passages |
| "Where do I go next?" | Cross-references or adjacent-guide pointers |

## Where This Rubric Should Live

For now, this rubric lives as a wave artifact:

`context/waves/2026-05-14-maxim-quality-control-spine/artifacts/GOLD-RUBRIC-V2.md`

After the pilot audit, promote the stable version to either:

| Destination | Use If |
|---|---|
| `.claude/skills/reference-review/SKILL.md` | The rubric should directly govern future `/reference-review` work |
| `SCORECARD.md` | The rubric should rescore volume-level quality |
| `REVIEW.md` companion section | The rubric should become operational dashboard policy |
| New root `QUALITY.md` | The rubric should be reader-visible project doctrine |

Do not edit structural root docs until the pilot audit proves the rubric is
stable.
