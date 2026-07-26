# HCI Full-Module R1 — Reference-Editor

> **Historical R1 lens; superseded final disposition: PASS — Pulse 02 DONE.** At this
> review stage the `reference-editor` status was REPAIRED and awaited an independent final
> re-review. The final reviewer subsequently passed all content and record repairs. This is the
> preserved whole-module pass over taxonomy and
> factual accuracy, standards/dates, coverage and structure, the two reciprocal-pointer siblings, and
> the wave records. The reference-editor lens owns **taxonomic/factual correctness, standards
> citation, style-contract completeness, self-containment, and record/registry truthfulness** (does
> the module read like one book, and do the records match the code and the library?). Findings are
> repaired in the guides and records. Review-only; does not clear the gate. No commit/push.

## Scope reviewed

The style-contract sections of all twelve guides (landscape diagram, worked cases, Reader Tasks,
Decision Cheat Sheet, Common Confusion Points, caveats); named-standard citations (ISO 9241-210 /
-411, WCAG, ACM Code, Fitts/Hick/Shannon, Nielsen & Landauer); the two reciprocal pointers into
`cognitive-science/09` and `industrial-design/06`; and the wave records — `STATUS.md`, the Pulse-02
pulse file, and `WAVE.md`.

## Findings

**RE-01 — BLOCK — `cognitive-science/09` reciprocal pointer: the taxonomy flattened three different
kinds of thing into one "psychophysical law derivation" bucket.** The pointer box said the section
owns "the psychophysical *law derivations* (Fitts, Hick, Miller's '7±2', cognitive load, GOMS)" —
but **Fitts/Hick are psychophysical/performance laws**, **Miller's "7±2" and cognitive load are
memory/load constructs (not psychophysical laws)**, and **GOMS/KLM is an HCI engineering model** built
*on* the laws and constructs. Flattening them mislabels the science HCI defers to. *Repaired:* the
box now names the **three distinct levels explicitly** (performance laws / memory-load constructs /
HCI engineering model), keeps the applied use in HCI (`03`, `05`), and — per the expert-skeptic
ES-03 — certifies only the well-established forms, not the strongest information-theoretic
interpretation.

**RE-02 — WARN — Guide 04: ISO 9241-210 stated as "four principles" (it has six), and a reader task
not self-contained.** §1 said the standard "codifies four iterative activities and **four**
principles," and the diagram listed four numbered plus two "+" items. ISO 9241-210:2019 defines
**six** principles of human-centred design (understanding of users/tasks/contexts; user involvement;
user-centred evaluation; iteration; the whole user experience; multidisciplinary skills). Reader
Task 1 also asked the reader to "name the specific `05` method" — not answerable from `04` alone.
*Repaired:* the prose reads **six principles**, the diagram renumbers all six **1–6**, and Reader
Task 1 is made self-contained — it names the **candidate evaluation families** (inspection/analytic
vs empirical/user-based; formative vs summative) and asks only for the family choice, leaving the
specific method to `05`.

**RE-03 — BLOCK — Guide 11: the ACM Code framed as granting a legal/professional *right to refuse*.**
§7 said the ACM Code (2018) obliges professionals "to speak up and refuse" and that "you have a …
**right** to refuse to build a harm." The Code establishes **duties** (avoid harm, be honest and
**disclose**, respect privacy, be fair, hold the public good paramount); it does **not** grant an
express legal or professional right to refuse. *Repaired:* §7 now separates three things — the
**Code's duties**; whether refusing is **protected** (organizational policy, contract, whistleblower/
labor law → `law/` and `organizational-behavior/`); and the **individual ethical judgment** to
refuse, which the Code *informs* but does not license as a guaranteed right. The Decision Cheat Sheet
row, a new Common Confusion Point ("The ACM Code gives me the right to refuse"), and a new Reader Task
("Separate a duty from a protection") are aligned; the "This guide owns" header is reworded.

**RE-04 — WARN — Guide 00 vs Guide 01: the overview over-claimed "the discipline's lineage."** `00`'s
ownership header said it owns "the discipline's **lineage**," while the ownership matrix (correctly)
assigns the detailed intellectual lineage to `01`. *Repaired:* `00` now owns only the **concise
shared spine** (the datable anchors every guide cites, and the route into the story); the header and
the "Lineage — the concise shared spine" section state that the **detailed lineage is `01`'s alone**
and `00` names the anchors and points to it rather than retelling it.

**RE-05 — WARN — Guide 07: search UX was thin, and the first-click claim was unsourced.** §3 listed
query/results/facets/zero-results but gave no **browse-vs-search-vs-facet decision**, the worked case
had no **search/facet thread**, there was no search reader task or cheat-sheet decision surface, and
"first-click correctness strongly tracks success" carried no citation. *Repaired:* §3 adds a
**browse / search / facet decision** (by what the user can express); the worked case adds a
**search + facets** thread (typo/synonym-tolerant query, faceted result set by department/year/format,
zero-results handling); a **new Reader Task** and **four cheat-sheet rows** give the decision surface;
and the first-click claim is **attributed and bounded** (Bailey et al. 2006 — a strong signal on
their tasks, not a law).

**RE-06 — WARN — Guide 10: no tangible/ubiquitous-computing reader task or decision row.** §3 covered
tangible/ubicomp, but the five reader tasks and the cheat sheet skipped it (AR/VR, agents, BCI, and
multimodal each had one; tangible/ubicomp had none). *Repaired:* a **tangible/ubicomp Reader Task**
(credit affordances/periphery; hold to the evidence bar) and a **cheat-sheet row** ("a tangible /
ambient 'calm' design claim → keep it formative until field-proven") are added.

**RE-07 — WARN — Guide 11: sustainability had no worked microcase, reader task, or cheat-sheet
decision.** §6 stated the environmental/human-sustainability stakes abstractly. *Repaired:* a
**worked microcase** (a fictional app's auto-play-4K-on-cellular default, where the environmental and
inclusion wins are the *same* low-consumption default), a **Reader Task**, and a **cheat-sheet row**
make it decision-useful and tie it to the metric-is-not-the-goal spine.

**RE-08 — WARN — `industrial-design/06` reciprocal pointer: a false exclusive-ownership boundary.**
The box said this guide "owns interaction design at the **physical / industrial-product level**" and
routed all "digital" to HCI ("the physical-product entry point stays here") — but the guide's body
legitimately spans the **physical-product-to-digital transition** (its title, the physical→hybrid→
digital spectrum, personas, UX design). *Repaired:* the box is made honest — this guide covers IxD
from its industrial-design origins **through the product-to-digital transition**; it does **not**
exclusively own "digital"; the **dedicated depth** of digital interaction design and the **evaluation**
of interactive computing live in HCI (`02`, `05`); the two are **complementary, not a clean
physical-vs-digital partition**, and neither exclusively owns the boundary. The body's transition
material is retained.

**RE-09 — WARN — Guide 08: the overlay warning cited a vague "Overlay Fact Sheet."** *Repaired:* the
reference is made exact and dated — the *Overlay Fact Sheet* (overlayfactsheet.com, first published
**2021**).

**RE-10 — WARN — Guide 03: the ISO 9241-411 throughput wording was inexact, and a QWERTY aside needed
aligning with `01`.** The Fitts box gave "throughput TP = ID / MT … the ISO 9241-411 comparison
metric," omitting that the standard uses the **effective** index of difficulty (target width adjusted
to the observed endpoint spread, folding accuracy in). A prose aside also said QWERTY "persists by
installed base, **not optimality**," a clean claim now corrected in `01`. *Repaired:* the box and the
throughput bullet state **effective throughput (IDe, accuracy-adjusted, not gameable by trading
accuracy for speed)**, and the QWERTY aside reads "installed base and switching cost … its own
optimality is contested, not settled (`01`)."

**RE-11 — BLOCK — Records: STATUS said "Pulse 02 COMPLETE" while the review gate was still open, and
this full-module panel was unrecorded.** `STATUS.md`'s header read "Pulse 02 COMPLETE," contradicting
`WAVE.md` and the pulse file (both "IN REVIEW") and the module's own outstanding-gate note.
*Historical R1 repair:* `STATUS.md`, the Pulse-02 pulse file, and `WAVE.md` were reconciled to
**IN REVIEW** while this **full-module R1 panel** awaited independent final review. The panel's
conservative findings were repaired and the tier set to **Silver**, with **no Gold and no registry
row**. *Superseding final disposition:* the final reviewer returned **PASS**; Pulse 02 is **DONE**.

## Style-contract completeness (whole module, post-repair)

| Lens | Assessment |
|---|---|
| Landscape-first + layered | PASS — every guide opens with a landscape diagram and layers downward. |
| Worked cases | PASS — `02`,`05`,`07`,`09`,`10`,`11` carry fictional worked cases; `07`/`11` gained search-facet and sustainability threads. |
| Reader tasks (3–5+) | PASS — every guide answers concrete tasks; `02`,`07`,`10`,`11` gained the tasks the findings required. |
| Decision Cheat Sheet + Confusions | PASS — present and decision-useful; updated for the unit-of-analysis, ACM-duty, dual-axis, search, tangible, and sustainability repairs. |
| Dates/standards attributed & bounded | PASS after RE-02/09/10 and ES-01/03/05 — ISO 9241-210 (six principles), ISO 9241-411 (effective TP), WCAG, ACM Code (duties), Fitts/Hick/Shannon, BCI reviews, David/Liebowitz-Margolis all cited/bounded. |
| Cross-references / reciprocal pointers | PASS — `cognitive-science/09` and `industrial-design/06` pointers now taxonomically correct and non-exclusive; `02`↔`09` unit-of-analysis seam consistent. |

## Decision

**Historical R1 decision: REPAIRED — no unresolved BLOCK or WARN after this pass.** The
taxonomic/factual, standards, coverage, boundary, and record defects are all repaired; the module
reads as one book and the records match the authored/integrated/backfilled/reviewed state.
**Superseding final disposition:** the final reviewer returned **PASS**; Pulse 02 is **DONE**.
The tier decision — **Silver**, no Gold, no registry — is carried in `R2-gold-rubric.md`; see also
`R1-consolidated.md`.
