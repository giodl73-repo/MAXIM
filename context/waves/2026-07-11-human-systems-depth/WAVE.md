---
wave: human-systems-depth
date_open: 2026-07-12
date_close: null
status: active
depends_on: clinical-and-chemical-foundations
---

# Human Systems Depth

## Mission

Strengthen fields where MAXIM's systems perspective is useful but current
coverage is compressed.

## Scope

| Area | Action |
|---|---|
| Human-computer interaction | Add usability, interaction models, research methods, accessibility, and socio-technical design. |
| Human factors | Add ergonomics, cognitive workload, control-room/interface design, error taxonomies, and safety-critical practice. |
| Neuroscience | Expand from five guides into neuroanatomy, systems, computational, imaging, plasticity, and clinical boundaries. |
| Economics | Add labor, environmental, public, international, and industrial economics without duplicating game theory. |
| Public policy | Add policy design, implementation, budgeting, regulation, bureaucracy, and evaluation. |

## Guardrails

- Follow the repo learner profile and style contract; match the depth bar of the
  strongest local exemplars (e.g., `chemistry/`, `clinical-medicine/`), not the
  `computing/01-PACKAGE.md` floor.
- MAXIM remains **independently readable and standalone**. External sources may
  *support* fact-checking, but no sibling repo (FONTES included) is a runtime,
  binding, or publication gate for a module to be considered complete.
- Each new/expanded module needs a reviewed scope map, clear ownership/defer
  boundaries, mixed quantitative/qualitative methods, non-US/non-WEIRD examples,
  and adversarial review with no unresolved BLOCK items.
- Do not integrate an incomplete module into `sections/`, `.mkdocs/mkdocs.yml`,
  or `TRACKER.md`; prototype boundary guides pass review first.
- Every canonical source edit regenerates MDLOOM/CROP/MDPORT/FLETCH artifacts —
  but source-corpus backfill is a per-pulse deliverable, run only when a pulse
  authors or integrates content, never during a prototype boundary review.

## Pulse Sequence

The wave lands the **human-interaction spine first** — human-computer interaction
(HCI) and human factors (HF) — because those two modules share the sharpest new
boundary in the wave (the HCI↔HF seam) and the heaviest overlap against existing
modules (`cognitive-science/`, `industrial-design/`, `psychology/`,
`statistics-applied/`). Neuroscience, economics, and public policy are sequenced
into later pulses once the interaction spine and its seams are ratified.

**HCI prototypes lead.** Rather than scope HF against a hypothetical HCI module,
HCI is prototyped first: its two highest-risk boundary guides are authored and
gate-reviewed so the HCI↔HF seam, the cognitive-mechanism defer to
`cognitive-science/`, and the statistics defer to `statistics-applied/` are all
proven on real content *before* HF is scoped against them.

| Pulse | Title | Status | Scope |
|---:|---|---|---|
| 01 | HCI architecture & prototype boundary review | DONE | Ratified `human-computer-interaction/` scope, 12-guide manifest, ownership matrix, HCI↔HF seam, safety/ethics contract, and guide-family scaling contracts; prototype guides `05` and `08` passed independent R2 review. No full-module integration or source backfill in this pulse. |
| 02 | HCI authoring & review | DONE | Authored `00` + the remaining guides (`01`–`04`, `06`, `07`, `09`–`11`) on the gate-passed prototype pattern; wired section/nav/TRACKER integration; added bounded reciprocal pointers; and ran source-corpus backfill. The full-module panel's 5 BLOCK + 13 WARN findings were all repaired, every guide is **Silver**, and the final reviewer returned **PASS** with no unresolved BLOCK/WARN. No Gold/Da Vinci tier or registry row is claimed. |
| 03 | Human factors architecture & prototype boundary review | DONE | Ratified `human-factors/` scope against the HCI↔HF seam, `industrial-design/05`, `cognitive-science/09`, `systems-engineering/06`, `clinical-medicine/11`, and the domain owners (`nuclear/05`, `aeronautics/04`, `transportation/07`, `biomedical-engineering/07`); fixed the 12-guide problem-first manifest, ownership/defer matrix, reciprocal HCI↔HF seam, and safety/ethics contract; authored the three highest-risk guides — `02` (two-stage **scaling gate**) plus `03` and `06` (**review-gated** prototypes) — at full peer depth, passing focused MDLOOM (3 files, 0 errors, 0 warnings). The scaling gate (`02`) and review gates (`03`/`06`) were exercised by the R1 panel and **ratified by an independent strict R2 re-review** (`panels/hf-prototype-r1/`, `panels/hf-prototype-r2/`) with no unresolved BLOCK/WARN. No full-module integration, no source backfill, no sibling-module edits. |
| 04 | Human factors authoring & review | IN REVIEW | Authored remaining HF guides (`00`, `01`, `04`, `05`, `07`–`11`) on the ratified prototype pattern + the Testable Definition of Done from `02`; added `human-factors/mdloom.toml`; wired `sections/technology.md`, `.mkdocs/mkdocs.yml`, `TRACKER.md`; added minimal reciprocal pointers to the six boundary siblings (`industrial-design/05`, `human-computer-interaction/`, `cognitive-science/09`, `clinical-medicine/11`, `systems-engineering/06`, `biomedical-engineering/07`); ran source-corpus backfill for HF + the five changed content-guide siblings; focused MDLOOM clean (12 files, 0/0). **The independent full-module adversarial panel (DoD closure gate 12, `panels/hf-full-r1/`) has now been conducted — it surfaced a conservative 6 BLOCK + 6 WARN superset, all repaired in the guides and records, and `R2-gold-rubric` scores every guide Silver with no registry row. Because that panel both raised and repaired the findings, an independent final re-review is still pending, so the wave stays IN REVIEW, not closed.** No Gold/Da Vinci, no registry row. |
| 05+ | Neuroscience / economics / public policy expansions | TODO | Sequenced after the interaction spine; each scoped in its own architecture pulse against existing modules. |

**Current wave state:** Human Systems Depth remains **active**. HCI Pulse 02 is
closed; Pulse 03 (Human factors architecture & prototype boundary review) is DONE; and
**Pulse 04 (Human factors authoring & review) is IN REVIEW** — all twelve `human-factors/`
guides are authored on the ratified prototype pattern and the Testable Definition of Done,
the module is wired into section/navigation/`TRACKER`, minimal reciprocal pointers were added
to the six boundary siblings, source-corpus backfill ran for HF and the five changed
content-guide siblings, and focused MDLOOM is clean (12 files, 0/0). **The Definition-of-Done
closure gate — the independent full-module adversarial panel (`panels/hf-full-r1/`) — has now been
conducted: it raised and repaired a conservative 6 BLOCK + 6 WARN superset and scored every guide
Silver (no registry). Because that panel both raised and repaired the findings, an independent final
re-review is still pending, so the wave stays IN REVIEW, not closed.** Gold/Da Vinci promotion
and legal-content expansion remain future work and do not reopen HCI Pulse 02.

## Quality Gate

1. Every file reads like a durable MAXIM reference guide, not a generated outline.
2. Every guide answers 3–5 concrete reader tasks without another source.
3. Diagrams perform conceptual work and remain terminal-readable.
4. Tables compare, decide, or compress real choices.
5. Factual specifics (named laws, standards, versions, dates) receive a focused
   numbers/names/dates check and are attributed and bounded, not universalized.
6. MDLOOM passes for touched content guides; source-corpus artifacts are
   regenerated from canonical numbered guides in the authoring/integration pulse.

## Exit Gate

Each new or expanded module has a reviewed scope map, clear ownership/defer
boundaries, numbered guides at peer depth, mixed quantitative/qualitative methods,
non-US/non-WEIRD examples, section/navigation integration, source-corpus
regeneration, and adversarial expert review with no unresolved BLOCK items. MAXIM
stays standalone: source/citation evidence is **optional supporting** material,
not a binding requirement, and no sibling repo is a completion gate.
