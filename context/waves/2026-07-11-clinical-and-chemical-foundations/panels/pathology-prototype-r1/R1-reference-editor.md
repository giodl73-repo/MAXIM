# Pathology Prototype R1 — Reference Editor

> **Historical point-in-time prototype lens.** Pending-sign-off and deferred-work claims
> below are preserved as R1 evidence and superseded by the 2026-07-12 full-module final PASS;
> Pulse 05 is DONE.

> **Prototype-round panel (Pulse 05).** Reference-editor lens over the two boundary
> prototypes `pathology/08-LABORATORY-MEDICINE` and
> `pathology/10-DIAGNOSIS-PATTERN-RECOGNITION-AND-REPORTING`, plus the architecture record
> and `STATUS.md`. This lens owns structure, boundary/scoping honesty, taxonomy
> completeness, the report-as-interface fidelity, and the manifest/scaling plan. All
> findings are **repaired**; Pulse 05 is kept **IN REVIEW** (no final sign-off). See
> `R1-consolidated.md`.

## Initial Decision

The prototypes are structurally strong (landscape diagram, layered formalism,
decision-useful tables, ownership boundaries, reader tasks, cheat sheet, confusions,
resource caveats), but the first pass carried several **structural and scoping** defects at
the exact seams the prototypes exist to de-risk: the diagnostic taxonomy was a flat
single-axis list; the "end-to-end case" narrated the pipeline instead of showing an actual
report artifact and never demonstrated a versioned correction; report claims overreached
on staging and synoptic enforcement; neither guide branched a case for a resource-
constrained setting; and the architecture labeled every non-prototyped guide "lower-risk"
with no scaling contract for the two that most need one. All are repaired.

## Findings

### RE-01 — BLOCK: The "end-to-end case" was a narration, not a report payload, and showed no versioned correction

File: `pathology/10-DIAGNOSIS-PATTERN-RECOGNITION-AND-REPORTING.md` (§10)

Finding: §10 walked through the pipeline in prose ("Pattern…", "Differential…",
"Certainty calibration…") but never produced the *artifact* the guide is about — a report.
It also asserted the amendment concept without showing a **version 1** and a **visible
version 2**, so the correction taxonomy (§9) was never demonstrated end to end. For a guide
whose thesis is "the report is an interface," a narrated case under-delivers.

Fix: §10 is rewritten as an **actual fictional report payload**. **Version 1** renders a
diagnosis line, a name:value **synoptic block** (procedure, integrity, adequacy, size,
histologic pattern, grade estimate with system caveat, pathologic-T element, overall stage
group, margins, ancillary IHC with control validity, molecular = pending, assertion
strength, negative-finding scope), a microscopic/gross narrative, a comment carrying the
differential + limitation + the margin caveat, and a **critical-communication record**
("not applicable at v1"). **Version 2** is a visible **amendment** (status AMENDED v2, prior
version retained, reason recorded, diagnosis-line change, synoptic deltas, and an
amendment critical-communication record with read-back), with an explicit contrast to what
an **addendum** would have been. Everything is labeled fictional/illustrative.

### RE-02 — WARN: Diagnostic taxonomy was a single-axis pattern list

File: `pathology/10-DIAGNOSIS-PATTERN-RECOGNITION-AND-REPORTING.md` (§3)

Finding: §3 ("Differential Pattern Classes") presented one axis — inflammatory / injury /
growth pattern classes — as *the* taxonomy. Real diagnostic parsing scores several
orthogonal dimensions at once, and a one-axis list undersells the method and hides why the
same approach behaves differently on a cytology aspirate versus a resection.

Fix: §3 is rebuilt as a **multidimensional parse matrix** with seven orthogonal dimensions
— **adequacy, compartment, architecture, cytology, stromal/background, hematolymphoid
considerations, and sampling/discordance** — where the *joint* profile discriminates and
the *specimen type* sets which dimensions are active. Two **contrasting specimen examples**
are added as *method demonstrations, not a disease catalog*: a **thyroid-nodule FNA** (a
cytology specimen where architecture is unavailable, adequacy and a named category system
dominate) and a **lymph-node core/excision** (a tissue specimen where the hematolymphoid
axis switches the method to clonality/flow and sampling/discordance is load-bearing). A
dimension→question→owner table replaces the flat one.

### RE-03 — BLOCK: Report claims overreached — staging, synoptic enforcement, and a universal "cannot sign"

File: `pathology/10-DIAGNOSIS-PATTERN-RECOGNITION-AND-REPORTING.md` (§6, §7)

Finding: Three scoping overreaches. (a) §6 framed "stage … TNM" as if the pathology report
owns the stage, conflating the **pathologic elements** the report supplies with the
**overall stage group**. (b) §7 presented synoptic completeness as a universal property. (c)
§7 asserted "the report **cannot be signed** with a required element missing" — a universal
enforcement rule that is untrue outside a governing protocol.

Fix: (a) §6 now distinguishes the report's **pathologic TNM elements (`pT`/`pN`/`pM`)** from
the **overall stage group**, which *integrates* T/N/M (and, in current systems, selected
**non-anatomic prognostic factors**) and is often assigned downstream (registrar/treating
team); the ASCII, table row, and reader Task 4 were aligned. (b)/(c) §7 now scopes
completeness as **protocol-governed and heterogeneous**: enforceable *within* a governing
protocol (CAP in the US; ICCR/RCPath-style datasets elsewhere; accreditation may make it
mandatory for those specimens), but with **no universal "cannot sign" rule** — outside such
a protocol completeness is a professional norm, and many specimens (small biopsies,
cytology) are narrative. The Common Confusion Point and cheat sheet rows were updated.

### RE-04 — WARN: No resource-constrained branch on a case in either guide

Files: `pathology/08-LABORATORY-MEDICINE.md`,
`pathology/10-DIAGNOSIS-PATTERN-RECOGNITION-AND-REPORTING.md`

Finding: Both guides carried general resource-tier caveats, but neither *branched an actual
case* to show how an unavailable test changes the released artifact (uncertainty wording,
release status, referral) **without** changing the framework — the concrete demonstration
the caveats promise.

Fix: Each guide now adds an **alternate resource-constrained branch** on a case. Guide 08,
Task 1: with no automated HIL/hemolysis index and no prior result for a delta check, the
same total-testing-process framework yields a different artifact — the interference cannot
be instrument-flagged, so uncertainty moves into a specimen-quality comment and a
provisional/held status pending recollection or send-out. Guide 10, §10: where the
entity-decisive molecular assay is unavailable on site, the `Molecular` field reads "not
available on site," assertion strength stays at favoring/descriptive (never upgraded), the
comment records a send-out/telepathology referral, and no amendment issues — the parse
dimensions, report anatomy, and correction taxonomy are identical; only the tools, final
assertion strength, and referral wording differ.

### RE-05 — BLOCK: Architecture labeled all remaining guides "lower-risk"; no scaling contract for 09/11

Files: `context/waves/.../artifacts/PATHOLOGY-ARCHITECTURE.md`, `pathology/STATUS.md`

Finding: MAXIM-PATH-19 called the two prototypes "most at risk" and "the other ten
lower-risk mechanism/technique/systems guides." This under-rates two guides with real
scaling/boundary risk: `09` (anatomic technique) is prone to **procedure-creep** (becoming a
runnable SOP, breaching pillar 2), and `11` (laboratory-as-quality-system) shares a
**QC/error/governance seam with `08`** and risks over-broad governance scope. Treating them
as uniformly safe invites boundary failure at bulk-authoring time.

Fix: MAXIM-PATH-19 is amended to state **not all remaining guides are low-risk**. A new
**MAXIM-PATH-24** plus a dedicated **Scaling Mini-Contracts** section pins detailed contract
artifacts now: `09` is scoped to **purpose/failure-mode/consequence triples with no runnable
steps**; `11` **owns cross-process QC/error/governance** while `08` **owns method/result
generation and introduces QC/error concepts only as needed locally**, with a
forward/back cross-reference. Each requires a **focused `expert-skeptic` mini-review on a
partial draft before bulk authoring** (procedure-creep for `09`; `08`↔`11` ownership + scope
for `11`). `STATUS.md` marks `09`/`11` "scaling mini-contract + focused mini-review before
bulk authoring" and adds the "not uniformly low-risk" note; QR-12 records the risk.

### RE-06 — NOTE: Prototype R1 recorded; Pulse 05 kept IN REVIEW; no integration/backfill

Files: `pathology/STATUS.md`, `context/waves/.../pulses/05+pathology-architecture.md`,
`context/waves/.../artifacts/PATHOLOGY-ARCHITECTURE.md`,
`context/waves/.../panels/pathology-prototype-r1/`

Finding: The prototype gate needed to be recorded without over-claiming — the clinical
prototype received final sign-off, but this round must remain IN REVIEW.

Fix: The R1 panel (this file + `R1-expert-skeptic.md` + `R1-consolidated.md`) is recorded;
`STATUS.md`, the pulse record, and the architecture record all note **R1 run, findings
repaired, sign-off pending, Pulse 05 IN REVIEW**, with integration, reciprocal sibling
wiring, the `09`/`11` mini-reviews, and source-corpus backfill still deferred. No edits to
`medicine/`, `clinical-medicine/`, `sections/`, `.mkdocs/`, or `TRACKER.md`.

## Structural checklist (both prototypes)

| Property | 08 | 10 |
|---|---|---|
| Single H1; landscape diagram first | ✅ | ✅ |
| Layered model with real formalism | ✅ (TEcalc/TEa, RCV%, LoB percentile) | ✅ (parse matrix, 4 certainty dimensions) |
| Decision-useful tables | ✅ | ✅ |
| Explicit ownership / three-way split | ✅ | ✅ |
| Actual worked artifact | ✅ (institutional reasoning tasks) | ✅ (versioned report payload) |
| Resource-tier case branch | ✅ (Task 1 branch) | ✅ (§10 branch) |
| 5 reader tasks · cheat sheet · confusions | ✅ | ✅ |
| Third-person descriptive voice | ✅ (0 `you/your`) | ✅ (0 `you/your`) |
| No `@editor` tags | ✅ | ✅ |

No unresolved BLOCK or WARN remains after the repairs. Sign-off is **not** granted this
round.
