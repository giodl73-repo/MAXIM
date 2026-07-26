# Pathology Prototype R2 — Expert Skeptic (strict re-review)

> **Historical point-in-time prototype lens.** Pending-sign-off and deferred-work claims
> below are preserved as R2 evidence and superseded by the 2026-07-12 full-module final PASS;
> Pulse 05 is DONE.

> **Prototype-round panel (Pulse 05), round R2 — strict re-review.** Expert-skeptic lens
> over the two boundary prototypes `pathology/08-LABORATORY-MEDICINE` and
> `pathology/10-DIAGNOSIS-PATTERN-RECOGNITION-AND-REPORTING` after the R1 repairs. This lens
> carries the **quantitative-honesty** and **boundary-honesty** checklists mandated by the
> four-pillar contract. R1 removed the gross defects; R2 goes finer and catches residual
> unit-mixing, an over-extended change-detection statistic, a spectrum/prevalence conflation,
> and an over-actionable margin claim. All findings below are **repaired** in the guides;
> Pulse 05 is deliberately kept **IN REVIEW** (no final strict sign-off this round). See
> `R2-consolidated.md`.

## Judgment

The R1 repairs stand, but the strict pass surfaced four residual quantitative/boundary
defects at the seams these prototypes exist to de-risk: `08`'s calculated total error still
added an absolute bias to a relative CV in one expression (a unit-mix), and the change-value
paragraph still recommended the within-subject RCV for cross-hospital comparison; `10`'s
ancillary section still tied the Sn/Sp/LR *contribution* to prevalence (conflating
spectrum-driven discrimination with prevalence-driven predictive value), and the margin
narrative still implied a clear margin proves complete excision. None is an advice-creep or
forensic breach — the pillar audit stays clean — but each is a precision/honesty defect a
peer metrologist or a pathologist would catch. All are repaired.

## Findings

### ES2-01 — BLOCK: Calculated total error still mixed absolute and relative units

File: `pathology/08-LABORATORY-MEDICINE.md` (§2)

Finding: after R1, the model read `TEcalc ≈ |bias| + z·CV`, with a note that the terms could
be "a concentration … or a percentage." But as written the single expression adds a **bias
in concentration units** to `z·CV`, where `CV` is a **percentage** — an absolute quantity
plus a relative one, which is dimensionally invalid. The sigma expression `σ = (TEa − |bias|)
/ CV` carried the same latent mismatch (an absolute bias over a percentage CV).

Fix: §2 now gives **two matched-unit formulas**, never combined:

- **absolute** — `TEcalc_abs ≈ |bias_abs| + z·SD_abs`, judged against `TEa_abs` (every term
  in the analyte's concentration units);
- **relative/percent** — `TEcalc_% ≈ |bias_%| + z·CV_%`, judged against `TEa_%` (every term
  a percentage of the concentration).

The acceptance test `TEcalc ≤ TEa` is applied within one unit system, and the sigma metric
now uses **matching percentage terms**, `σ = (TEa_% − |bias_%|) / CV_%`. The `z ≈ 1.65`
convention is stated explicitly as the **one-sided** ~95% normal quantile (single upper 5%
tail), with `z ≈ 1.96` noted for the two-sided bound. The §2 table rows and the architecture
citation (MAXIM-PATH-23) were aligned.

### ES2-02 — BLOCK: Reference Change Value recommended for cross-hospital/method comparison

File: `pathology/08-LABORATORY-MEDICINE.md` (§6, Task 2, Confusion Points)

Finding: R1 fixed the percentage-vs-unit RCV *arithmetic*, but the **scope** was still wrong.
The §6 "unifying idea" advised that comparing "this hospital's [value] to that one's" is a
change-detection problem, Task 2 called a two-lab comparison "an **RCV**-scale comparison,"
and a Confusion Point framed cross-lab comparison as a "traceability + RCV" problem. RCV is a
**within-subject serial** statistic built from analytical + within-person biological
variation on **one measurement procedure**; it is not defined for reconciling two *different*
methods/labs, where the disagreement is method bias, not within-person change.

Fix: RCV is now **reserved for serial within-person change on the same or an analytically
comparable method**, stated explicitly in the §6 bullet. The cross-hospital/method
recommendation is removed: the §6 unifying idea, Task 2, and the Confusion Point now route
cross-lab reconciliation to **method bias, measurement uncertainty, commutability,
calibration traceability, and method-comparison evidence** (standardization/harmonization,
Deming/Passing–Bablok, Bland–Altman) — "RCV does not bridge methods." The two problems are
named as distinct.

### ES2-03 — BLOCK: Sn/Sp/LR discrimination tied to prevalence (spectrum/prevalence conflation)

File: `pathology/10-DIAGNOSIS-PATTERN-RECOGNITION-AND-REPORTING.md` (§4)

Finding: the Gate-2 text said the marker's "sensitivity, specificity, and likelihood-ratio
*contribution* … is population- and context-dependent … **because its predictive value
depends on which entities are in play and their prevalence**." That makes prevalence a driver
of Sn/Sp/LR, which is wrong: Sn/Sp/LR vary with the **spectrum** (which entities are in the
differential and the morphologic spectrum/case mix they present), whereas **prevalence**
drives **predictive value / posterior** (PPV, NPV), not the operating characteristics. The
post-table paragraph and the ASCII repeated the conflation.

Fix: §4 now states the discriminating power (Sn/Sp/LR contribution) is **spectrum-dependent**
and explicitly that **prevalence does not change Sn/Sp/LR**; what prevalence (pre-test
probability) drives is the **predictive value and posterior (PPV/NPV)**, a *separate*
quantity assembled downstream. The belief-update/posterior math is deferred to
`clinical-medicine/03`. The Gate-2 bullet, the two-gate ASCII, and the post-table paragraph
were all aligned to the spectrum-vs-prevalence split.

### ES2-04 — WARN: A clear margin implied proof of complete excision

File: `pathology/10-DIAGNOSIS-PATTERN-RECOGNITION-AND-REPORTING.md` (§6, §10, Task 4,
Confusion Points)

Finding: R1 removed the "clinically actionable" overclaim, but the guide still framed margin
status as answering "**was this excision complete?**" (the §6 bullet and axis table, Task 4,
and a Confusion Point). A margin is assessed on **sampled sections of the inked surface of the
specimen**, not the whole resection bed; a "clear" margin is *evidence about* complete
removal, not *proof* of it (residual tumor can lie between sampled planes or beyond the
specimen).

Fix: margin status is now defined as **tumor presence/absence and clearance distance at the
examined inked specimen margins**, with an explicit statement that it is **evidence about,
not proof of, complete excision**. The §6 bullet, the axis-table row, the §10 report payload
(margin field, Comment, and the closing note), Task 4, and the Confusion Point were all
reworded; the "completely excised" phrase became "with clear (uninvolved) examined margins."

## Advice-/Procedure-/Forensic-Creep Checklist (pillar audit)

| Pillar | Check | Result |
|---|---|---|
| 1 — no self-diagnosis / personal-result interpretation | Any reader's-own-result reading? | Clean — figures remain fictional/illustrative; no personal interpretation |
| 2 — no collection/bench SOP | Any runnable procedure? | Clean — the 09 two-stage contract keeps technique at purpose/failure-mode; no bench steps added |
| 3 — no forensic/legal determination | Any cause-/manner-of-death or legal call? | Clean — none present |
| 4 — third-person descriptive voice | Second-person/imperative to reader? | Clean — 0 `you/your`; edits stayed descriptive |

No unresolved BLOCK or WARN remains after the repairs. Sign-off is **not** granted this round —
Pulse 05 stays IN REVIEW per the pulse scope.
