---
name: maxim-review
description: "Run a MAXIM quality review panel over a guide, directory, pulse, or wave and write findings."
tags: [maxim, review, rubric, findings, editorial]
---

# maxim-review

Run a lightweight review panel for MAXIM guides, directories, pulses, or waves.

For Gold certification, the panel is not lightweight in its claim boundary:
proof-clean output, Da Vinci invariants, and Cross-References are prerequisites
only. They may justify Candidate-Hardened status, but Certified Gold requires
guide-specific rubric notes, adversarial findings, and reader-task evidence.

## Usage

```text
/maxim-review file computing/01-PACKAGE.md
/maxim-review directory distributed-systems
/maxim-review pulse 02
```

## Built-In Review Lenses

| Role | Lens |
|---|---|
| reference-editor | Style contract, layering, decision usefulness, common confusions |
| ascii-cartographer | ASCII/SVG diagrams, alignment, visual grammar, diagram density |
| expert-skeptic | Factual confidence, overclaims, missing caveats, stale statements |
| bridge-builder | Universal old-world/new-world bridges, cross-domain analogies |
| index-weaver | Cross-references, concept-index candidates, duplicated concepts |
| card-steward | Archetype voice, honor/flair continuity, volume identity |

## Gold Certification Gate

Use this gate whenever a review promotes, restores, demotes, or challenges a
Gold claim.

| Gate | Must Record |
|---|---|
| Mechanical prerequisite | Focused proof command, `--daVinci` when applicable, and confirmation that output was searched for literal `FAIL` |
| Rubric depth | Ten Gold dimensions with guide-specific notes; repeated cohort-wide scores are insufficient |
| Explanation depth | Whether the guide explains the deep model, not just the topic outline |
| Diagram usefulness | Whether ASCII/SVG figures perform conceptual work and remain terminal-readable |
| Factual density | Whether claims are bounded, current, caveated, and dense enough for expert use |
| Bridge quality | Whether universal CS/domain bridges come before stack-specific flavor |
| Table quality | Whether tables decide, compare, or compress real choices instead of summarizing prose |
| Reader-task sufficiency | 3-5 concrete tasks the guide answers without sending the reader elsewhere |
| Adversarial findings | BLOCK/WARN/NOTE findings from expert-skeptic and relevant lenses, or explicit no-finding rationale |
| Registry decision | Certified Gold, Candidate-Hardened, Proof-Clean / Uncertified, or Substantive Repair |

## Output

For wave-local review, write:

```text
context/waves/{active}/panels/{review-name}/R1-{role}.md
context/waves/{active}/panels/{review-name}/R1-consolidated.md
```

For persistent editorial findings in guides, use the existing `@editor` tag
format from `.claude/skills/reference-review/SKILL.md`.

## Finding Format

```markdown
### F-01 - BLOCK: title
File: path
Finding: what is wrong
Consequence: what breaks
Fix: concrete recommendation
```

Severity:

- `BLOCK`: must fix before marking pulse/wave done.
- `WARN`: should fix or explicitly defer.
- `NOTE`: useful carry-forward.

## Rules

- Findings lead; summaries follow.
- Cite files and exact local paths where possible.
- Do not perform implementation edits during review.
- Prefer a few consequential findings over a long style nit list.
