---
name: maxim-plan
description: "Create MAXIM wave or pulse plans with mission, artifacts, governing roles, gates, and non-goals."
tags: [maxim, plan, wave, pulse, gates]
---

# maxim-plan

Use this skill when drafting a MAXIM quality wave, pulse checklist, editorial
sweep, proof upgrade, or execution plan.

## Wave Card Minimum

Write wave cards to `context/waves/YYYY-MM-DD-wave-slug/WAVE.md` with:

- frontmatter: `wave`, `date_open`, `status`, optional `source_goal`
- mission
- claim boundary
- inputs
- pulse status table
- validation gates
- done criteria
- non-goals
- closeout/lessons when complete

## Pulse Plan Format

Write pulse plans to `context/waves/{active}/pulses/NN+slug.md` with:

- frontmatter: `wave`, `pulse`, `date`, `status`, `depends_on`,
  `governing_roles`
- mission
- scope inventory
- pre-implementation scout
- deliverables checklist
- validation gates
- non-goals
- evidence/commits when backfilling completed work

## Planning Rules

- Prefer one committable outcome per pulse.
- Name source artifacts and generated artifacts explicitly.
- Include review roles when the pulse changes doctrine, rubric, proof gates, or
  claim status.
- Put gates in the plan before implementation.
- Backfilled pulses must cite commits or artifacts instead of pretending they
  were planned before the work happened.
- History/flair integration belongs in the wave closeout and `/honor` flow.
