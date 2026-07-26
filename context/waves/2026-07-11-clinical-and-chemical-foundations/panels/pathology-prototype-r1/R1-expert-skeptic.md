# Pathology Prototype R1 — Expert Skeptic

> **Historical point-in-time prototype lens.** Pending-sign-off and deferred-work claims
> below are preserved as R1 evidence and superseded by the 2026-07-12 full-module final PASS;
> Pulse 05 is DONE.

> **Prototype-round panel (Pulse 05).** Expert-skeptic lens over the two boundary
> prototypes `pathology/08-LABORATORY-MEDICINE` and
> `pathology/10-DIAGNOSIS-PATTERN-RECOGNITION-AND-REPORTING`. This lens carries the
> **advice-creep + procedure-creep** and **quantitative-honesty** checklists mandated by
> the four-pillar contract (PATHOLOGY-ARCHITECTURE MAXIM-PATH-19/QR-1/QR-2). All findings
> below are **repaired** in the guides; Pulse 05 is deliberately kept **IN REVIEW** (no
> final sign-off this round). See `R1-consolidated.md`.

## Judgment

The two prototypes hit the intended metrology and diagnostic-method depth, but the first
pass carried a cluster of **quantitative-honesty defects** (a conflated total-error model,
a percentage-vs-unit reference-change comparison, a wrong detection-limit definition, a
universal error-share claim), a **false-calibration overclaim** (a universal certainty
ladder mapped to posteriors), an **analytical-vs-diagnostic conflation** in the ancillary
section, an overreaching **clinically-actionable margin** claim, pervasive
**advice-/procedure-creep** (second-person imperatives and a patient-style result with
redraw framing), and **citations presented as authoritative** while unverified. No
personal-result interpretation, bench SOP, or forensic/legal determination survived. All
findings are repaired.

## Findings

### ES-01 — BLOCK: Calculated total error conflated with allowable total error

File: `pathology/08-LABORATORY-MEDICINE.md` (§2)

Finding: The guide wrote `TEa ≈ |bias| + z·CV` and then `σ = (TEa − |bias|)/CV`, using the
symbol `TEa` for **both** the quantity *computed* from a method's bias and imprecision and
the quantity that is an *externally set allowance*. This is the classic total-error
conflation: allowable total error (`TEa`) is a **specification** (from biological
variation, a regulatory/EQA criterion, or clinical need), not something computed from the
method's own bias and CV. Using one symbol for both makes the sigma formula circular and
misrepresents what the budget means.

Fix: Split the two. **Calculated total error** `TEcalc ≈ |bias| + z·CV` is now the
method's *estimated worst-case single-result error*, stated in the analyte's units (a
concentration, or a percentage if bias and CV are both relative — the conventions are not
mixed), with `z ≈ 1.65` labeled the **one-sided ~95% normal quantile** (upper 5% tail).
`TEa` is defined separately as the *allowable* tolerance (a spec), with an explicit
acceptance rule `TEcalc ≤ TEa`. Sigma is reframed as `σ = (TEa − |bias|)/CV` scoring the
gap between what the method *does* and what it is *allowed* to do. The §2 table row was
split into `TEcalc` and `TEa`, and the Decision Cheat Sheet row now reads "calculated
total error judged against its allowable bound."

### ES-02 — BLOCK: Reference-Change-Value worked case mixed percentages and units

File: `pathology/08-LABORATORY-MEDICINE.md` (§6 formula, Task 4)

Finding: `RCV = √2·z·√(CV_a² + CV_i²)` is a **percentage** (relative-change) threshold
because it is built from CVs, but the worked case compared it to "the observed 13-unit
move" (42 → 55) — an absolute-unit change. Comparing a percentage threshold to a raw-unit
difference is a category error, and the case gave no explicit `CV_a`, `CV_i`, or
confidence assumptions, so the conclusion was unfalsifiable.

Fix: The §6 formula now states RCV is expressed as a *percentage* change and is compared to
the *relative* change, never a raw-unit subtraction. Task 4 is reworked with explicit
illustrative assumptions — `CV_a = 5%`, `CV_i = 12%`, `z ≈ 1.96` for a two-sided ~95%
either-direction change (`z ≈ 1.65` noted for the one-sided question) — giving
`RCV ≈ 1.41 × 1.96 × √(5² + 12²) ≈ 36%`. The observed move is the *relative* change
`(55 − 42)/42 ≈ 31%`; since `31% < 36%`, it is not distinguishable from combined
analytic + biological variation. A note adds that large/asymmetric changes are refined on
the **log scale** (asymmetric up/down thresholds), with the percentage form as the common
first approximation. The marker is labeled fictional.

### ES-03 — BLOCK: Limit of Blank defined as the highest raw signal

File: `pathology/08-LABORATORY-MEDICINE.md` (§3)

Finding: LoB was defined as "the highest signal a true-zero sample produces." Per CLSI
EP17, LoB is a **chosen upper percentile of the blank *results*** — conventionally the
95th, `mean_blank + 1.645·SD_blank` — in **concentration units**, not the single largest
raw signal ever observed. The original conflated a statistical percentile of results with
an extremal raw signal, and dropped the units.

Fix: LoB is redefined as `mean_blank + 1.645·SD_blank` (the one-sided 95th percentile of
blank *results*, in concentration units), with an explicit "the result value that ~95% of
blanks fall below, not the single highest raw signal." LoD is stated as
`LoB + 1.645·SD` of low-level samples, and the ordering `LoB ≤ LoD ≤ LoQ` is retained "by
construction" (replacing the reader-directed "always"). EP17 is named with its actual
title (*Evaluation of Detection Capability*).

### ES-04 — WARN: "~60–70% of all errors" asserted as a universal constant

File: `pathology/08-LABORATORY-MEDICINE.md` (Big Picture diagram + prose)

Finding: The total-testing-process diagram annotated the pre-analytic phase with
"~60-70% of all errors" and the prose called it "the large majority," presented as a law.
The figure is real but derives from particular stat-laboratory error series (Carraro &
Plebani and later work) and varies widely by setting, era, and how "error" is defined and
counted.

Fix: The diagram annotation is now "error-dense phase*"; the prose presents an
**attributed, bounded, illustrative** range ("roughly one-half to two-thirds … in several
widely cited series," pre-analytic most often the single largest contributor) with an
explicit setting-dependence caveat and a `*` note that the shares are illustrative, not a
universal constant. The overclaim "the machine was working is never a sufficient defense"
was softened to "not by itself a sufficient defense."

### ES-05 — BLOCK: Advice-/procedure-creep — patient-style result, redraw framing, and second-person imperatives

Files: `pathology/08-LABORATORY-MEDICINE.md`,
`pathology/10-DIAGNOSIS-PATTERN-RECOGNITION-AND-REPORTING.md` (throughout)

Finding: (a) The potassium example ("6.2 mmol/L with a hemolysis flag") read like a
patient result and ended with "reason toward a **redraw** on a cleanly collected
specimen," which frames a specimen-handling action. (b) Both guides carried pervasive
second-person / imperative voice — "systems you already reason about," "you never say,"
"the hook effect inverts your intuition," "Always say which you mean," "You do not stain
for everything," "You want both, and you never put…," "check controls," plus imperative
Decision-Cheat-Sheet column headers — which reads as instructions to the reader, violating
pillar 4 (third-person descriptive voice).

Fix: (a) The potassium value is labeled "an illustrative, fictional value," the reasoning
is recast into an **institutional model state** ("the institutional model state is to hold
the flagged value as provisional pending recollection of the specimen"), and no redraw
*advice* remains. (b) All reader-directed second-person and imperative constructions in
both guides are recast to descriptive institutional model states; a grep confirms **zero**
`you/your` and no `Always/Never/you want/make sure/compare`-to-reader instructions remain.
Cheat-sheet headers became "Situation / signal" and the intro reads "which concept a given
situation involves (all descriptive model states)."

### ES-06 — BLOCK: A universal certainty ladder mapped to fixed posteriors

File: `pathology/10-DIAGNOSIS-PATTERN-RECOGNITION-AND-REPORTING.md` (§5)

Finding: The certainty section presented a single **universal ladder** of words
("diagnostic of" → "consistent with" → "suspicious for" → …) and asserted "each rung means
a different posterior," with "suspicious for" defined as "roughly, more likely than not."
This manufactures a false, cross-institutional probability calibration: these terms do not
carry stable numeric posteriors, and their force is governed locally.

Fix: §5 is rewritten around **four independent, orthogonal dimensions** — material
adequacy (gates the rest), positive assertion strength, negative-finding scope, and
residual uncertainty — each stated on its own axis. The wording is explicitly **locally
governed** (service convention or a *named, dated category system*), with a direct
statement that "consistent with"/"suspicious for" do **not** carry a stable
cross-institutional posterior. The Big-Picture pipeline node, §11, reader Task 3, the
cheat sheet, and the Common Confusion Point were all updated to match; the "guide owns"
header now reads "independent dimensions of diagnostic certainty (locally governed
lexicons, not a universal ladder)."

### ES-07 — BLOCK: Analytical validity conflated with diagnostic evidence

File: `pathology/10-DIAGNOSIS-PATTERN-RECOGNITION-AND-REPORTING.md` (§4)

Finding: The ancillary-test section ran the assay's *analytical* behavior (control
failure, antigen loss, fixation, cross-reactivity) and its *diagnostic* discrimination
(sensitivity/specificity/LR against a differential) together as "every ancillary test is a
test with an analytical Sn/Sp." These are two different things: whether the stain
technically worked is independent of how much a valid result discriminates in a given
population/context.

Fix: §4 now runs an explicit **two-gate** model. **Gate 1 — analytical validity**:
controls, antigen detectability, fixation, probe/antibody performance; a failed-control
"negative" is *uninformative*, a property of this stain on this block, independent of
disease. **Gate 2 — diagnostic evidence**: only a valid result becomes evidence, and its
Sn/Sp/LR *contribution* is **population- and context-dependent** (strong in one
differential, weak in another), with the belief-update math deferred to
`clinical-medicine/03`. The four disciplines, the ASCII, the table header ("Gate-1
analytical failure"), and reader Task 2 were aligned to the split.

### ES-08 — WARN: A sub-millimetre margin called generically clinically actionable

File: `pathology/10-DIAGNOSIS-PATTERN-RECOGNITION-AND-REPORTING.md` (§10)

Finding: The end-to-end case stated "the deep-margin proximity is **clinically
actionable**" for a "<1 mm" clearance, presenting a generic margin distance as inherently
actionable — an overclaim that also drifts toward clinical advice. Margin significance is
entity-, protocol-, and context-dependent and is owned downstream.

Fix: The rewritten report payload reports the margin as a **measured boundary condition**
("neoplasm to within 0.8 mm of the inked deep margin") and states explicitly that its
clinical significance "is entity-, protocol-, and context-dependent and is NOT a generic
actionable threshold — interpretation and management belong to the treating team
(`clinical-medicine/03`), not this report." A dedicated note reinforces that the
sub-millimetre value is not a generically actionable result.

### ES-09 — WARN: Framework citations presented as authoritative but unverified

File: `context/waves/.../artifacts/PATHOLOGY-ARCHITECTURE.md`

Finding: The framework section was headed "External framework grounding (**authoritative**)"
while the Gaps section admitted the same attributions were "grounded from standard
summaries, not primary PDFs." Calling unverified summaries authoritative is a
self-contradiction and an honesty defect.

Fix: The heading is de-authoritized ("grounded in standard summaries — verify against
primary sources") with a citation-status caveat. A new **MAXIM-PATH-23** records a focused
verification/qualification pass on the load-bearing attributions: Lundberg 1981 JAMA
(brain-to-brain loop); GUM/ISO uncertainty; the `TEcalc` vs `TEa` split; CLSI EP17 LoB as a
blank-result percentile; CLSI AUTO10-A superseded/expanded by AUTO15; UICC/AJCC TNM
elements vs stage group; and CAP/ICCR/RCPath synoptic heterogeneity. `08` now cites
AUTO10-A→AUTO15; the Gaps carry-forward and a new QR-13 row track the residual
verification.

## Advice-/Procedure-/Forensic-Creep Checklist (pillar audit)

| Pillar | Check | Result |
|---|---|---|
| 1 — no self-diagnosis / personal-result interpretation | Any reader's-own-result reading? | Clean — potassium value labeled fictional; framed as institutional model state |
| 2 — no collection/bench SOP | Any runnable procedure or redraw *advice*? | Clean — redraw recast to "provisional pending recollection"; guide 09 scope pinned to purpose/failure-mode (MAXIM-PATH-24) |
| 3 — no forensic/legal determination | Any cause-/manner-of-death or legal call? | Clean — none present |
| 4 — third-person descriptive voice | Second-person/imperative to reader? | Clean — zero `you/your`; imperatives recast |

No unresolved BLOCK or WARN remains after the repairs. Sign-off is **not** granted this
round — Pulse 05 stays IN REVIEW per the pulse scope.
