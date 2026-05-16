# Proof Gate Tightening Plan

## Purpose

`proof.toml` should become a staged quality gate, not a single brittle global
switch. The goal is to catch real defects while avoiding another unsafe
bulk-fix cycle.

## Current Leniencies

| Area | Current Setting | Why It Exists | Risk |
|---|---|---|---|
| ASCII box tolerance | `tolerance = 2` | remaining off-by-1/2 errors may require content edits | lets visibly imperfect boxes pass |
| Column separators | `check_col_separators = false` | spatial diagrams caused false positives | misses malformed table-like boxes |
| Wide chars | `error_on_wide = false` | CJK and language examples are intentional | true alignment bugs may hide |
| Required H2s | `["Decision Cheat Sheet"]` | first universal structural rule | misses missing Common Confusion sections |
| Landscape diagram | any code block pattern, warning | cheap proxy for a diagram | code sample can satisfy it falsely |
| Editor tags | warning | allowed while review is in progress | "clean" claims can pass with tags |
| Tables | extra body cols ignored | math/code uses `|` heavily | real table overflows may be missed |
| Atlas excluded | `atlas/**` excluded | atlas has separate SVG rules | atlas quality depends on separate review |

## Staged Modes

### Baseline

Purpose: protect the whole repository from obvious breakage.

| Rule | Severity |
|---|---|
| Markdown parse / max one H1 | error |
| Missing `Decision Cheat Sheet` | error for content guides |
| Any `@editor[` in files claiming clean | warning globally, error in release check |
| Broken table row with too few columns | error |
| ASCII width mismatch beyond tolerance 2 | error |

### Silver

Purpose: normal content-guide publishing gate.

| Rule | Severity |
|---|---|
| ASCII tolerance >1 | error |
| Missing `Common Confusion Points` | error |
| No Markdown table | error |
| No fenced diagram/code block in first major section | error |
| `@editor[` tag | error |
| Known Da Vinci invariant missing | error |

### Gold

Purpose: canonical guide gate.

| Rule | Severity |
|---|---|
| ASCII tolerance >0, unless waiver names why | error |
| Minimum 3 structural diagrams or approved visual equivalents | error |
| Decision Cheat Sheet must contain "use X when Y" semantics | review BLOCK if absent |
| Reader task test present in wave/panel artifact | required |
| Gold Rubric v2 score average >=4.5, no dimension <4 | required |
| Adversarial factual pass complete | required |

Gold mode should initially run on a small explicit file list, not the full
library.

## Mechanical Rules Safe To Tighten First

| Rule | Proposed Move |
|---|---|
| `@editor[` in publishable guides | warning -> error in silver/gold |
| Required `Common Confusion Points` | add to silver/gold required H2s |
| Missing Markdown table | add as silver/gold rule |
| Da Vinci invariant failures | keep as error |
| `Decision Cheat Sheet` missing | keep as error for content guides |

## Rules That Need False-Positive Measurement

| Rule | Why Not Global Yet |
|---|---|
| ASCII tolerance 0 | many diagrams are intentionally spatial, not rectangular |
| Column separator checking | side-by-side diagrams and nested boxes trigger false positives |
| Opening diagram proxy | proof must distinguish code examples from conceptual diagrams |
| Table extra columns | math notation, regex, and bitwise examples use pipe characters |
| Diagram count | some small guides may be excellent with fewer diagrams |

## Gold Pilot Set

| Guide | Why |
|---|---|
| `computing/01-PACKAGE.md` | original style contract exemplar |
| `distributed-systems/03-CONSENSUS.md` | expert CS guide with algorithm diagrams |
| `periodic-table/01-HYDROGEN.md` | dense cross-domain science guide |
| `music-theory/01-PITCH-SCALES.md` | notation-heavy mathematical arts guide |
| `atlas/02-GLOBAL-WINDS.md` | hybrid SVG/ASCII atlas exemplar |

## Proof Tooling Blocker

In the current environment:

```powershell
python -m proof check
```

fails with:

```text
No module named proof
```

Before changing `proof.toml`, the next implementation wave should identify how
the peer `proof` tool is installed or vendored, then run baseline checks without
modifying content.

## Recommended Next Move

1. Finish the ASCII Perfection Spec.
2. Run the Pilot Gold Audit as a review-only pass.
3. Add a separate proof config or mode for the pilot set.
4. Only after false positives are measured, tighten global `proof.toml`.
