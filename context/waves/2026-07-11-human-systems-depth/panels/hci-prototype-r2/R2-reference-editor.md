# R2 Reference Editor — HCI Prototype Boundary Gate, Strict Re-Review (`05`, `08`)

Strict editorial and factual re-review after the R1 repairs. Lens: coverage/scaling
completeness, factual accuracy of standards/figures/dates, model correctness, record
consistency (STATUS / architecture / pulse), and truthful tier claims. Review-only record;
fixes were applied in this repair-and-R2 pass and marked *disposition: repaired*.

## Findings

### RE2-01 — WARN: the scaling contracts did not cover every remaining guide
File: `05` (Guide-Family Scaling Contracts)

Finding: R1 (RE-05) added scaling contracts, but only for **five** families (`01`; `06`/`09`;
`07`; `10`; `11`). A prototype meant to govern the whole Pulse-02 authoring pass must scale to
**every** remaining guide, and the accessibility/safety discipline of `08` must ride along —
otherwise `00`, `02`, `03`, `04` inherit nothing and the two `08` invariants are unstated.

Fix: Extend to **every remaining guide — `00`, `01`, `02`, `03`, `04`, `06`, `07`, `09`, `10`,
`11`** — each contract stating the object judged **and the test that would fail it** (not
boilerplate): `00` coverage/boundary-MECE; `01` sourcing/dating not CIs; `02` models as
falsifiable diagnostic instruments; `03` modality claims as bounded performance claims with
named estimator + *n*, Fitts/Hick cited-not-derived; `04` design outputs as hypotheses
unresolved until `05` confirms. Then **propagate the `08` invariants** as a cross-cutting
contract riding all families: (1) disabled users + their AT are a first-class, per-segment
sample, not an afterthought; (2) the safety/ethics floor — no manipulation playbook, no legal
ruling, no safety-certification; conformance is a floor; defer operator-safety to
`human-factors/` and legal obligation to `law/`. Closing invariant updated to name the `08`
carry-through. *Disposition: repaired.*

### RE2-02 — WARN: cheat-sheet "native control" row overstated what native gives for free
File: `08` (Decision Cheat Sheet; §3 "Semantics before ARIA")

Finding: The cheat-sheet native-controls row read *"native gives name/role/value + keyboard."*
Native semantics reliably provide **role, state behavior, and keyboard support** (and value
where it applies), but the accessible **name** is *not* always free — an icon-only `<button>`
or an `<input>` without an associated `<label>` has a correct role and no name. Stating name
as free contradicts §3's own name-required / value-state-when-applicable contract.

Fix: Rewrite the row: native semantics give **role/state behavior + keyboard** for free, but
the accessible **name must still be supplied where needed** (icon buttons, inputs),
**value/state only when applicable**, and **relationships/descriptions where required**. Bring
the §3 "Semantics before ARIA" bullet into line (role/state/keyboard free; name supplied where
not derived from content). *Disposition: repaired.*

### RE2-03 — WARN: records carried stale/over-stated claims to reconcile
Files: architecture record; pulse `01+hci-architecture.md`; `08` §3 (via pulse)

Findings and fixes (all *repaired*):

- **Architecture — adjusted-Wald "canonical" claim.** MAXIM-HCI-08 illustrated the stats
  defer with *"adjusted-Wald CIs on completion rates,"* but `05` canonically reports the
  **Wilson score** interval (adjusted-Wald named only as a close relative). Changed the
  example to **Wilson score CIs** so the record matches the guide.
- **Pulse — flat `name/role/value/state`.** The pulse described the accessibility-tree
  contract as flat *"name/role/value/state"* (the exact shape R1's RE-03 corrected in `08`).
  Reworded both occurrences to **name + role required; value/state when applicable; +
  descriptions/relationships** so the record cannot re-introduce the flat contract.
- **Manifest vs pattern.** Records now state the distinction cleanly: the **12-guide manifest
  was ratified at authoring (Pulse 01)**; the **prototype pattern** was pending a strict R2
  and is **ratified only now** that R2 has signed off.
- **Actual R1 lenses (no fictional `index-weaver`).** The frontmatter `governing_roles` and
  two prose spots named `index-weaver` (and `ascii-cartographer`) as review lenses, but the
  R1 panel that actually ran was **`expert-skeptic` + `reference-editor`** (there is no
  `index-weaver` artifact). Records corrected to the lenses that actually governed.
- **R2 record.** R1 required a strict re-review before ratification; that record
  (`panels/hci-prototype-r2/`) did not exist. Created, and the pulse deliverable / STATUS /
  architecture updated to mark the pattern **ratified**.

### RE2-04 — NOTE: no Da Vinci invariants and no Gold eligibility yet (by design)
Files: STATUS; architecture record; pulse

Finding: A strict reader could ask why these guides carry **no Da Vinci figure invariants**
and are not **Gold-eligible**. They should not — Gold certification (proof-clean + Da Vinci
invariants + cross-references + the ten-dimension rubric with guide-specific notes) is a
later-tier concern, sequenced **after** Pulse-02 authoring, integration, and source-corpus
backfill. Their absence is future-tier work, **not** a Pulse-01 prototype-authoring blocker;
the Pulse-01 gate is the boundary/quality/safety re-review, which R2 has passed.

Fix: Record this explicitly in STATUS, the architecture carry-forward, and the pulse so the
scope boundary is unambiguous. *Disposition: recorded.*

## Standards / figures re-check (R1 checklist item 2)

| Item | Record in `08` | R2 verification |
|---|---|---|
| WCAG 2.0 / 2.1 / 2.2 dates | 2008-12-11 / 2018-06-05 / 2023-10-05 | correct; 2.2 added 9 SC, removed 4.1.1 Parsing — correct |
| Text contrast | SC **1.4.3** AA, 4.5:1 / 3:1 large | correct (text only) |
| Non-text contrast | SC **1.4.11** AA, 3:1 | correct (added in 2.1) |
| Reflow | SC 1.4.10 AA | correct |
| Use of color | SC 1.4.1 A | correct |
| Target size | SC **2.5.8** AA, 24×24 px + 5 exceptions (spacing / equivalent / inline / user-agent / essential) | correct and bounded |
| Captions | 1.2.2 (A) / 1.2.4 (AA) | correct |
| WAI-ARIA | ARIA 1.2, W3C Rec 2023 | correct |
| Disability prevalence | WHO ~16% / ~1.3 bn (2022) | attributed + dated |
| Detectable-failure prevalence | WebAIM Million 2024 ~96% | named source; retained (distinct from recall) |
| Automated recall | de-numbered → "a minority / limited" | correct after ES2-03 (no named denominator) |

## Style-contract check (both guides)

| Lens | Assessment |
|---|---|
| Landscape-first + layered | PASS |
| Decision Cheat Sheet + Confusions | PASS; updated for the target-rule row and native-control row |
| Diagrams do conceptual work | PASS; no ASCII disturbed by edits |
| Dates/standards attributed & bounded | PASS |
| Reader tasks answerable | PASS (5 each; task 3 now carries the target rule) |
| Scaling contracts load-bearing | PASS after RE2-01 (all 10 remaining families + `08` invariants, each with a failing test) |

## Verdict

Factual, coverage, and record-consistency defects in this lens are corrected; standards and
figures re-check clean; the no-Gold / no-Da-Vinci scope is now explicit. Recommend **PASS** —
see `R2-consolidated.md`.
