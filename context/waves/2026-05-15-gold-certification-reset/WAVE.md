---
wave: gold-certification-reset
date_open: 2026-05-15
date_close: 2026-05-15
status: complete
source_goal: "Restore Gold as deep editorial certification, not factory polish"
---

# Gold Certification Reset

## Mission

Reset the MAXIM Gold strategy so "Gold" means peer-level editorial excellence,
not merely proof-clean guide polish. Proof, Da Vinci invariants, and
Cross-References remain required prerequisites, but they no longer certify a
guide without independent rubric review, adversarial findings, and reader-task
evidence.

## Claim Boundary

This wave governs certification doctrine and registry status. It does not judge
the intrinsic quality of every factory-hardened guide; it only withdraws the
automatic Gold claim until those guides pass a reset-era panel.

## Inputs

| Artifact | Use |
|---|---|
| `context/gold/REGISTRY.md` | Source of truth for Gold claims, candidates, invariants, and promotion protocol |
| `context/waves/2026-05-15-gold-factory-wave-*` | Recent factory evidence with proof, cross-link, invariant, and uniform rubric patterns |
| `context/waves/2026-05-14-gold-factory-wave*` | Earlier factory cohorts using the same promotion lane |
| `proof.toml` | Da Vinci invariant inventory and mechanical prerequisite gate |
| `.claude/skills/reference-review/SKILL.md` | Operational review rubric and inline finding system |
| `.claude/skills/maxim-review/SKILL.md` | Panel-review lenses and finding format |

## Audit Findings

| Finding | Consequence | Reset Decision |
|---|---|---|
| Registry had 893 rows under Current Certified Gold | The label made factory hardening look equivalent to editorial certification | Freeze Certified Gold to panel-backed entries only |
| Gold Factory waves contributed 816 registered rows | Factory evidence emphasized proof, Cross-References, Da Vinci invariants, and uniform 4.6 scoring | Reclassify as Candidate-Hardened pending panel |
| Other promotion/cohort waves contributed 75 registered rows | Useful evidence exists, but most waves do not show guide-specific adversarial findings | Reclassify as Candidate-Hardened pending panel |
| Pilot Gold Rescore contributed 2 rows | It contains differentiated dimension scores and reader-task findings after remediation | Keep as Certified Gold |

## Pulse Status

| Pulse | Status | Governing Roles | Evidence |
|---|---|---|---|
| 01 - Registry status reset | DONE | reference-editor, expert-skeptic, index-weaver | `context/gold/REGISTRY.md` now separates Certified Gold, Candidate-Hardened, Proof-Clean / Uncertified, and Substantive Repair |
| 02 - Review gate hardening | DONE | reference-editor, ascii-cartographer, expert-skeptic, bridge-builder | `.claude/skills/reference-review/SKILL.md` and `.claude/skills/maxim-review/SKILL.md` now state prerequisite-only hardening and required panel evidence |
| 03 - First reset panel | DONE | full review panel | `panels/first-reset-panel/R1-consolidated.md` keeps three Wave 37 samples at Candidate-Hardened with WARN findings |

## Validation Gates

| Gate | Requirement |
|---|---|
| Mechanical prerequisite | Focused proof passes with `--daVinci`; output is checked for literal `FAIL` |
| Editorial rubric | Ten Gold dimensions have guide-specific notes, not repeated cohort scores |
| Adversarial review | Panel records BLOCK/WARN/NOTE findings from domain-reader objections |
| Reader tasks | 3-5 concrete tasks pass within the guide under review |
| Registry update | Only panel-backed guides enter Current Certified Gold; all others remain Candidate-Hardened or lower |

## Done Criteria

1. Registry no longer presents factory-hardened guides as automatically certified.
2. Review doctrine states that proof, invariants, and cross-links are necessary
   but not sufficient.
3. First reset-era panel demonstrates the stricter gate on a small cohort.
4. Any restored Gold guide has guide-specific scores, adversarial notes, reader
   tasks, and validation evidence.

## Non-Goals

- Do not remove Da Vinci invariants or Cross-References from candidate-hardened
  guides.
- Do not bulk edit guide content solely to chase labels.
- Do not downgrade guide quality claims silently; every status change must cite
  this reset or a later panel.

## Closeout

This wave stops the degradation from Gold into polish. The registry now exposes
the difference between Certified Gold and Candidate-Hardened; the review skills
require guide-specific editorial evidence; and the first reset panel showed that
three mechanically clean, invariant-protected Wave 37 guides remain candidates
until WARN findings are repaired and re-panelled.
