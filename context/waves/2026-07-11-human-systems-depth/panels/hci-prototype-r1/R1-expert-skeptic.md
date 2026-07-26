# R1 Expert Skeptic — HCI Prototype Boundary Gate (`05`, `08`)

Round-1 adversarial pass over the two prototype guides
`human-computer-interaction/05-USABILITY-EVALUATION.md` and
`08-ACCESSIBILITY-INCLUSIVE-DESIGN.md`. Lens: overclaim, stale/undated or invented
figures, advice-creep, heuristics-as-laws, conformance-as-usability, statistical
over-claim, model determinism, and metadata truthfulness. This is a **review-only**
record; the fixes it calls for were applied in the same repair pass and are noted as
*disposition: repaired*. It does **not** clear the gate — see the verdict.

## Finding Summary

| # | Guide | Risk | Severity | Disposition |
|---|---|---|---|---|
| ES-01 | 05 | Inconsistent / un-named small-sample CIs (n=5 4/5 given as ±30→[.50,.96] in §1 vs adjusted-Wald [.44,.96] in §6) | BLOCK | repaired |
| ES-02 | 05 | "At target" claimed while the CI crosses the target (SUS 77, CI [72,82], target 75) | BLOCK | repaired |
| ES-03 | 05 | Invalid comparison rule ("a change must **exceed the CI**") substituted for a test/CI on the difference | BLOCK | repaired |
| ES-04 | 05 | Deterministic method landscape ("pick a cell … the method is decided") | WARN | repaired |
| ES-05 | 05 | Reflexive TA mis-attributed; inter-rater reliability treated as a universal quality criterion | WARN | repaired |
| ES-06 | 05 | Inspection findings unseen in a small user sample declared "probably false positive" / "refuted" | WARN | repaired |
| ES-07 | 08 | Nested `inclusive ⊃ usability ⊃ accessibility` model; accessibility called a "binary-ish floor" | BLOCK | repaired |
| ES-08 | 08 | AT model collapses everything to "the keyboard is the universal substrate" | WARN | repaired |
| ES-09 | 08 | Usability testing with disabled users called "ground truth" / "the truth" | WARN | repaired |
| ES-10 | 08 | Bare "~one-third / ~⅓ recall" figure, unattributed and undefined | WARN | repaired |
| ES-11 | 05/08 | Frontmatter overstates custody (`status: source-custody`, `source_custody: partial`, populated `backsource_ids`) before any backfill | BLOCK | repaired |

## Findings

### ES-01 — BLOCK: n=5, 4/5 completion CI is stated three different ways
File: `05-USABILITY-EVALUATION.md` (§1, §6, worked case)

Finding: The same quantity — a 95% interval on 4 successes in 5 — appears as "±30 pts,
~50%–96%" in §1 and as an "adjusted-Wald [0.44, 0.96]" in the §6 table, and no method is
named as canonical. A prototype whose intellectual signature is "discovery ≠ measurement"
cannot itself be loose with the measurement.

Consequence: A reader cannot reproduce or trust the headline number; the two values are
mutually inconsistent and neither matches a correct small-sample computation.

Fix: Name **one** method (Wilson score interval, 95%), compute it (4/5 → **[0.38, 0.96]**,
±29 pts; verified), and make every occurrence consistent; expose the method so it is
reproducible. *Disposition: repaired.*

### ES-02 — BLOCK: "at target" asserted when the CI spans the target
File: `05-USABILITY-EVALUATION.md` (worked case, "Reading against targets")

Finding: SUS 77 with a 95% CI of [72, 82] against a target of 75 was reported as "at or
just above target." An interval that includes sub-target values does not demonstrate the
target.

Consequence: This is exactly the over-claim the guide warns against, committed in its own
worked example.

Fix: Report the SUS target as **not demonstrated** at n=40 (point above, interval spans
it); expose mean/SD/n and a reproducible *t*-interval; add a **pre-committed pass rule**
(whole CI at or beyond target). *Disposition: repaired.*

### ES-03 — BLOCK: "exceed the CI" is not a comparison test
File: `05-USABILITY-EVALUATION.md` (§9, cheat sheet, worked case)

Finding: The guide told readers a change "counts only if it **exceeds the confidence
interval**." Comparing one run's point estimate to another run's single-sample CI is not a
valid test; a difference needs its own CI/test, and the right one depends on the design.

Consequence: Readers would systematically mis-judge A/B and benchmark comparisons.

Fix: Remove the "exceeds the CI" rule; require a **CI or test on the difference** —
two-sample for independent groups, paired (McNemar / paired *t*) for within-subjects.
*Disposition: repaired.*

### ES-04 — WARN: the method landscape is presented as deterministic
File: `05-USABILITY-EVALUATION.md` (Big Picture)

Finding: "Pick a cell in (Axis 1 × Axis 2), and the method is decided" over-promises. The
two axes narrow a *family*; the actual choice turns on risk/stakes, task type, population,
ecological validity, maturity, and constraints.

Fix: Reframe the axes as a *starting filter* and add the six fit factors. *Disposition:
repaired.*

### ES-05 — WARN: qualitative paradigms conflated
File: `05-USABILITY-EVALUATION.md` (§8)

Finding: Braun & Clarke's thematic analysis was cited while simultaneously prescribing
inter-rater reliability (Cohen's κ) as the quality check. Reflexive TA explicitly rejects
IRR as a quality criterion; κ belongs to coding-reliability / codebook paradigms.

Fix: Distinguish the paradigms — κ where coding is treated as measurement; reflexivity and
coherence for reflexive TA — and report κ only when the paradigm warrants it. *Disposition:
repaired.*

### ES-06 — WARN: a small sample cannot "refute" an inspection finding
File: `05-USABILITY-EVALUATION.md` (§8 diagram + prose; worked case Round 2)

Finding: Inspection predictions not seen by 5–6 users were labelled "likely false positive"
and "refuted." A discovery-sized sample lacks power to refute a low-λ prediction.

Fix: Treat inspection-only findings unseen in a small user sample as **unresolved** —
confirm, do not dismiss. *Disposition: repaired.*

### ES-07 — BLOCK: the nested accessibility model and the "binary-ish floor"
File: `08-ACCESSIBILITY-INCLUSIVE-DESIGN.md` (Big Picture, §2)

Finding: The guide nested `inclusive ⊃ usability ⊃ accessibility` and called accessibility
a "floor … Binary-ish." Accessibility is neither a subset of usability nor a binary gate;
the axes do not contain one another.

Fix: Replace with **five independent axes** — participatory/inclusive design process,
technical conformance, task accessibility, usability outcomes, inclusion/equity — scored
separately; drop "binary-ish floor." *Disposition: repaired.*

### ES-08 — WARN: "the keyboard is the universal substrate"
File: `08-ACCESSIBILITY-INCLUSIVE-DESIGN.md` (§3)

Finding: Touch screen readers, voice control, and switch access do not all reduce to the
keyboard. The claim erases distinct mechanisms and would misdirect engineering effort.

Fix: Separate **keyboard operability**, the **accessibility API / semantic tree**, and
**touch/pointer/voice/switch** input mechanisms; require name+role for interactive
semantics, value/state only when applicable, plus descriptions/relationships. *Disposition:
repaired.*

### ES-09 — WARN: user testing called "ground truth"
File: `08-ACCESSIBILITY-INCLUSIVE-DESIGN.md` (§6, §7, cheat sheet)

Finding: Usability testing with disabled users was repeatedly called "ground truth" / "the
truth." It is bounded evidence for the specific people, tasks, AT versions, and contexts
sampled.

Fix: Replace with **bounded evidence, never ground truth**; state sample bounds.
*Disposition: repaired.*

### ES-10 — WARN: the "~one-third recall" number is unattributed
File: `08-ACCESSIBILITY-INCLUSIVE-DESIGN.md` (§6, §7, reader task, cheat sheet, confusions)

Finding: A precise "~a third / ~⅓" automated-recall figure recurs with no source and no
definition of "recall."

Fix: **Define** recall (share of genuine barriers a tool detects), **attribute/bound** the
figure as a rough, tool- and page-dependent estimate (not a constant), and remove the bare
fraction elsewhere in favour of "a minority." *Disposition: repaired.*

### ES-11 — BLOCK: frontmatter overstates source custody
File: both guides (YAML frontmatter)

Finding: `status: source-custody`, `source_custody: partial`, and populated
`backsource_ids` claim a backfill relationship that does not exist — no source-corpus
backfill has run, by design, in this pulse.

Fix: `status: prototype`, `source_custody: needs-source`, `backsource_ids: []`.
*Disposition: repaired.*

## Verdict

The prototypes now clear the specific over-claim, statistical-rigor, model-honesty, and
metadata risks in this lens, and focused MDLOOM stays green. **This does not ratify the
pattern.** All eleven findings were fixed by the same author in the same pass; an
independent, **strict re-review (R2)** is required before the pattern can govern Pulse-02
authoring. Recommendation: **Pulse 01 remains IN REVIEW.**
