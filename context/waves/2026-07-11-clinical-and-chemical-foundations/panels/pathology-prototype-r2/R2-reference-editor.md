# Pathology Prototype R2 — Reference Editor (strict re-review)

> **Historical point-in-time prototype lens.** Pending-sign-off and deferred-work claims
> below are preserved as R2 evidence and superseded by the 2026-07-12 full-module final PASS;
> Pulse 05 is DONE.

> **Prototype-round panel (Pulse 05), round R2 — strict re-review.** Reference-editor lens
> over the two boundary prototypes plus the architecture record and `STATUS.md`, after the R1
> repairs. This lens owns taxonomy/method fidelity, the scaling-contract depth for the
> non-prototyped boundary guides, source-custody/metadata honesty, and the review record.
> R1 built the scaffolding; R2 tightens a cytology-method nuance, hardens the `09`/`11`
> scaling gate, and removes a metadata claim to artifacts that do not yet exist. All findings
> are **repaired**; Pulse 05 is kept **IN REVIEW** (no final strict sign-off). See
> `R2-consolidated.md`.

## Initial Decision

The prototypes remain structurally strong and the R1 taxonomy/scope repairs hold. The strict
pass found three residual defects the reviewer owns: (1) the thyroid-FNA method demonstration
overstated that "architecture is unavailable" in cytology, blurring *tissue-level* architecture
(genuinely unavailable) with *cell-group* cytoarchitecture (available and diagnostic); (2) the
`09`/`11` scaling mini-contracts named only a thin partial-draft slice and no whole-guide gate,
under-specifying the review that most needs specificity; and (3) the prototype frontmatter
carried generated `mdloom-backfill`/`git-history` backsource IDs and `source_custody: partial`
though no such artifacts exist and the module is untracked. All are repaired; the round is
recorded and held IN REVIEW.

## Findings

### RE2-01 — WARN: Thyroid-FNA example conflated unavailable tissue architecture with meaningful cytologic group arrangements

File: `pathology/10-DIAGNOSIS-PATTERN-RECOGNITION-AND-REPORTING.md` (§3)

Finding: the R1 method demonstration said *"Architecture is largely unavailable — an aspirate
has cells, not tissue organization."* That over-generalizes. What an FNA cannot show is
**tissue-level architecture and invasion** — an intact capsule, stromal relationships,
capsular/vascular invasion, overall growth pattern (which is why an aspirate cannot separate a
follicular adenoma from a follicular carcinoma). But the **cytoarchitecture of the aspirated
cell groups** — *microfollicular* groups, papillary fragments, syncytial sheets, dispersed
single cells — **is** available and is diagnostically load-bearing. Flattening both into
"architecture unavailable" undersells the cytology method and mis-teaches the parse.

Fix: §3 now distinguishes the two explicitly: **tissue-level architecture/invasion is
unavailable**, while the **cell-group cytoarchitecture (e.g., microfollicular patterns) is
available and diagnostically meaningful**, and the parse leans on adequacy, cytology, those
group-architecture cues, and stromal/background — reporting through a named category system.
A sentence notes the *tissue-architecture* matrix row is dimmed but its *cytologic* counterpart
is not, and the two must not be conflated.

### RE2-02 — WARN: 09/11 scaling mini-contracts under-specified the review gate

Files: `context/waves/.../artifacts/PATHOLOGY-ARCHITECTURE.md` (Scaling Mini-Contracts,
MAXIM-PATH-19/24, QR-12), `pathology/STATUS.md`

Finding: R1 pinned `09`/`11` scaling mini-contracts with a **single focused mini-review on a
thin partial draft** (for `09`, "fixation + IHC-substrate sections"; for `11`, "error-taxonomy
+ QC-program sections") and **no completed-guide gate**. For the two guides most at risk of
procedure-creep (`09`) and governance/`08`-seam creep (`11`), a thin partial slice is not a
sufficient gate: the highest-risk material (grossing/orientation for `09`; governance/
accreditation and the total-testing-process seam for `11`) was not required in the sampled
draft, and nothing re-checked the *finished* guide before sign-off.

Fix: both mini-contracts now specify a **two-stage gate**. Stage 1 (before bulk authoring)
requires a scoped `expert-skeptic` pass on **representative high-risk draft sections** — for
`09`, **grossing/orientation plus the staining, frozen-section, and cytology-preparation**
purpose/failure-mode sections; for `11`, the **governance/accreditation** section **plus the
total-testing-process error-taxonomy/QC section carrying the `08`↔`11` seam**. Stage 2 (before
sign-off) requires a **completed-guide whole-procedure (`09`) / whole-seam (`11`)** review
across the finished guide end to end. MAXIM-PATH-19/24, the Scaling Mini-Contracts section,
QR-12, and the `STATUS.md` 09/11 rows + risk paragraph were all updated; "a representative
partial draft is necessary but not sufficient."

### RE2-03 — BLOCK: Prototype frontmatter claimed source-corpus artifacts that do not exist

Files: `pathology/08-LABORATORY-MEDICINE.md`, `pathology/10-DIAGNOSIS-PATTERN-RECOGNITION-AND-
REPORTING.md` (frontmatter); `context/waves/.../artifacts/PATHOLOGY-ARCHITECTURE.md`

Finding: both prototype guides carried `status: source-custody`, `source_custody: partial`, and
`backsource_ids: [mdloom-backfill:pathology:…, git-history:pathology:…]` — the *post-backfill*
values emitted by `module_source_backfill.py`. But **no backfill was run**: there are no
`.mdloom/backfill/sources/pathology/` records, and the entire `pathology/` tree is **untracked**
(no git history). The metadata therefore asserted a MDLOOM backfill artifact and a git-history
backsource that do not exist — a source-custody honesty defect, and one that would poison the
CROP `source_custody eq 'partial'` view if the module were indexed.

Fix: the frontmatter is set to the contract's documented **pre-backfill** state
(`.mdloom/backfill/frontmatter-contract.md`; README "mark missing source custody as
`needs-source`"): `status: prototype`, `source_custody: needs-source`, `backsource_ids: []`.
The generated `mdloom-backfill`/`git-history` IDs are removed. This is **forward-compatible**:
the deferred `module_source_backfill.py --module-id pathology` run generates the real backsource
records and promotes the triple to `source-custody` / `partial|verified` / real IDs during
integration. Recorded as **MAXIM-PATH-25** and **QR-14**; the `STATUS.md`/architecture Gaps
notes were updated.

### RE2-04 — NOTE: R2 recorded; Pulse 05 kept IN REVIEW; no integration/backfill/commit

Files: `pathology/STATUS.md`, `context/waves/.../pulses/05+pathology-architecture.md`,
`context/waves/.../artifacts/PATHOLOGY-ARCHITECTURE.md`,
`context/waves/.../panels/pathology-prototype-r2/`

Finding: the strict re-review must be recorded without over-claiming — like R1, R2 repairs the
findings but does **not** grant final sign-off.

Fix: the R2 panel (this file + `R2-expert-skeptic.md` + `R2-consolidated.md`) is recorded;
`STATUS.md`, the pulse record, and the architecture record all note **R2 run, findings
repaired, final strict sign-off pending, Pulse 05 IN REVIEW**, with integration, reciprocal
sibling wiring, the `09`/`11` mini-reviews, and source-corpus backfill still deferred. No edits
to `medicine/`, `clinical-medicine/`, `sections/`, `.mkdocs/`, or `TRACKER.md`; no source
backfill; no commit.

## Structural checklist (both prototypes, post-R2)

| Property | 08 | 10 |
|---|---|---|
| Single H1; landscape diagram first | ✅ | ✅ |
| Layered model with real formalism | ✅ (matched-unit TEcalc/TEa, % sigma, RCV scope) | ✅ (parse matrix, spectrum-vs-prevalence gates) |
| Boundary/scoping honesty | ✅ (RCV within-subject only; cross-lab → method comparison) | ✅ (margin = examined inked planes; posterior → `clinical-medicine/03`) |
| Taxonomy/method fidelity | n/a | ✅ (FNA tissue-arch vs cytologic group arrangement) |
| Truthful source-custody metadata | ✅ (prototype/needs-source/[]) | ✅ (prototype/needs-source/[]) |
| Third-person descriptive voice | ✅ (0 `you/your`) | ✅ (0 `you/your`) |
| No `@editor` tags | ✅ | ✅ |

No unresolved BLOCK or WARN remains after the repairs. Sign-off is **not** granted this round.
