# Pathology Full-Module R1 — Expert-Skeptic

> **Historical point-in-time R1 lens.** Its findings and then-current pending-sign-off
> language are preserved as evidence and are superseded by the final PASS recorded
> 2026-07-12 in `R1-consolidated.md` and `R2-gold-rubric.md`; Pulse 05 is DONE.

> **Full-module panel (Pulse 05), lens: `expert-skeptic`. Status: REPAIRED — R2 confirmed clean.**
> A conservative, whole-module adversarial pass over all **twelve** authored guides
> (`00`–`11`) plus the source-corpus custody surface, run after authoring/integration/backfill.
> The expert-skeptic lens owns **mechanistic accuracy, over-generalization, the four-pillar
> non-advice/non-procedure contract, and provenance honesty**. Findings below are a conservative
> superset; each is **repaired** in the guides or the backfill generator. Consistent with the
> R2 guide-specific scoring and reader-task review subsequently confirmed the residual set
> clean. Pulse 05 remains **IN REVIEW only for final sign-off**. No commit/push.

## Scope reviewed

All twelve guides at peer depth; the `08`↔`10`↔`11` boundary seams; the four-pillar contract
(no self-diagnosis, no bench procedure, no forensic/legal, third-person voice); and the
`.claude/skills/maxim-source-backfill` generator + its emitted `pathology/` frontmatter and
source records.

## Findings

**ES-01 — BLOCK — Guide 05: basement-membrane invasion presented as the *general* definition of
malignancy.** The benign/malignant split, the ASCII "decisive line," Section 6, worked Case A, the
Reader Task, the cheat sheet, and a Confusion Point all defined cancer as "invasion through the
basement membrane + metastatic capacity." That is the **epithelial (carcinoma)** picture; it
mis-scopes **hematologic malignancies** (leukemias, lymphomas) and some other tumors, which are
malignant **without** a basement-membrane breach and **without** demonstrated distant metastasis.
*Repaired:* the general definition is now **capacity for destructive invasion and clinically
aggressive (typically metastatic) spread**; the basement-membrane criterion is explicitly scoped
to epithelia (in situ → invasive carcinoma), with a hematologic caveat added to Section 1, Section
6 (scope note), Case A, the Reader Task, the Decision Cheat Sheet, and a new dedicated Common
Confusion Point; the guide-00 overview cheat-sheet line is aligned.

**ES-02 — BLOCK — Guide 09: bare operational imperatives (procedure-/voice-creep, pillars 2 & 4).**
Three "Consequence and quality checks" blocks issued commands — *confirm* the specimen matches the
request, *document* orientation, *sample* the interfaces, *re-embed* or *obtain deeper levels* —
reading as bench instructions rather than system states. *Repaired:* each is recast to a
**descriptive system state / failure control** (identity *reconciled*; orientation *recorded*;
interfaces *within the sampled set*; ambiguity a *blocking* state; fixation adequacy *established*;
an inadequate plane a *recoverable* condition), preserving the no-runnable-steps boundary.

**ES-03 — BLOCK — Guide 09: cytology IHC/molecular substrate claimed "only via cell block."** The
substrate table and prose asserted IHC/molecular work is possible *only* through a cell block.
Factually wrong: validated **direct smears, cytospins, liquid-based/residual material, or cell
blocks** can all serve as IHC/molecular substrates when the assay is validated for that
preparation. *Repaired:* the box reads "YES, on validated preps"; the prose states IHC/molecular
are **not confined to the cell block** and enumerates the validated alternatives (cell block
preferred as most tissue-like, not required); the cheat-sheet row updated.

**ES-04 — WARN — Guide 09: over-absolute small-biopsy orientation claim.** The guide said an
oriented resection "demands orientation and surface marking, whereas a small biopsy is submitted in
its entirety and needs neither." *Repaired:* qualified — small biopsies are *often* submitted
whole with far less extensive orientation, but **some** still require orientation or surface
identification when an edge, level, or laterality carries the clinical question ("needs neither" is
a tendency, not a rule).

**ES-05 — BLOCK — Guide 07: "non-ionizing radiation mainly heats" (unqualified).** The big-picture
box, the prose, and the cheat sheet reduced all non-ionizing radiation to heating. **Ultraviolet**
is non-ionizing yet causes **direct photochemical DNA injury** (pyrimidine dimers) and
**carcinogenesis** — not a thermal lesion. *Repaired:* non-ionizing is split — **UV →** direct
photochemical DNA lesions → mutation/carcinogenesis (`05`); **infrared/radiofrequency →** primarily
thermal — in the box, the prose, and a new cheat-sheet row; the unqualified "just heats" claim is
removed.

**ES-06 — WARN — Guide 08: measurand conflated with measurement procedure.** The result-definition
prose and table folded the method into the measurand ("total calcium in serum **by
o-cresolphthalein complexone**"; "the exact quantity intended, including matrix **and method**").
The measurand is the **quantity intended** (analyte + system/matrix + kind of quantity); the
**measurement procedure** is separate, and the method enters the measurand definition **only when
the quantity is method-defined** (operationally defined). *Repaired:* the two are separated in the
prose and the table, with the method-defined exception stated explicitly.

**ES-07 — BLOCK — Source-corpus custody: git-history backsource stamped with no real history.**
`module_source_backfill.py` unconditionally added a `git-history:<module>:<n>-<slug>` backsource to
both guide frontmatter and generated source records, even when `git log -- <path>` returns **no
commits** (as it does for the untracked `pathology/`). This claims provenance that does not exist,
and contradicted the source record's own `Git provenance | pending`. *Repaired:* the generator now
adds the `git-history` backsource **only when real tracked history exists**; untracked/historyless
files carry `proof-backfill` only, and the source record's Git provenance stays `pending`. Focused
unit tests cover tracked-history-present vs untracked/no-history. Pathology + siblings regenerated;
tracked `disease`/`medicine` correctly retain `git-history`, untracked `pathology`/
`clinical-medicine` correctly drop it.

## Pillar checks (whole module)

- **Pillar 1 (no self-diagnosis / personal-result interpretation).** Holds — all cases fictional;
  ES-01/03/05 repairs keep mechanism/technique general, never reader-specific.
- **Pillar 2 (no runnable procedure).** ES-02/03/04 were the procedure-creep surface; after repair,
  guide `09` reads as *purpose → failure mode → downstream consequence* end to end (consistent with
  the `pathology-09-scaling` Stage-2 PASS).
- **Pillar 3 (no forensic/legal).** Holds — no cause-/manner-of-death or legal determination.
- **Pillar 4 (third-person voice; illustrative/dated numbers).** ES-02 removed the residual
  imperatives; `0` `you/your` across the module; ES-05/06 numbers/claims remain
  illustrative/attributed.

## Decision

**REPAIRED — no unresolved BLOCK or WARN after this pass; Pulse 05 remains IN REVIEW.** The module
hits the peer-depth bar; the conservative pass surfaced one mis-scoped definition (05), three
technique-accuracy/procedure-creep defects (09), one physics over-generalization (07), one
metrology-definition conflation (08), and one provenance-custody defect (generator). All are
repaired in the guides or the generator, validated by focused module-scope PROOF and the generator
unit tests. R2 now confirms the full-module residual set clean; see `R1-consolidated.md` and
`R2-gold-rubric.md`. Final module sign-off remains deliberately **withheld**, so Pulse 05
stays IN REVIEW only for that sign-off.
