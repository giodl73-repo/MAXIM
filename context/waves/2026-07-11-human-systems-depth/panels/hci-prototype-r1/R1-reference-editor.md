# R1 Reference Editor — HCI Prototype Boundary Gate (`05`, `08`)

Round-1 editorial and factual pass over the two prototype guides. Lens: style-contract
integrity, factual accuracy of named standards/figures/dates, model correctness,
coverage/scaling completeness, and record consistency (STATUS / architecture / pulse).
Review-only record; fixes were applied in the same repair pass and marked
*disposition: repaired*. Does **not** clear the gate.

## Finding Summary

| # | Guide/record | Lens | Severity | Disposition |
|---|---|---|---|---|
| RE-01 | 08 | WCAG accuracy: 1.4.3 conflated text + non-text contrast | BLOCK | repaired |
| RE-02 | 08 | SC 2.5.8 target-size stated as a universal rule, no exceptions | WARN | repaired |
| RE-03 | 08 | AT semantic contract lists a flat "name/role/value/state," omits descriptions/relationships and the value/state-when-applicable rule | WARN | repaired |
| RE-04 | 05 | No non-WEIRD *worked* example; WEIRD limits appear only as caveats | WARN | repaired |
| RE-05 | 05 | No guide-family scaling contracts for the other guide families | WARN | repaired |
| RE-06 | 08 | No non-Western/low-bandwidth/literacy/AT-access *worked* branch; only caveats | WARN | repaired |
| RE-07 | 08 | `law/` deferral points at a target that does not yet cover digital-accessibility statutes; not disclosed | WARN | repaired |
| RE-08 | STATUS / architecture | "passed prototype pattern" language asserts a gate that has not been passed | BLOCK | repaired |
| RE-09 | pulse | R1 panel deliverable unrecorded; no `panels/hci-prototype-r1/` artifacts | WARN | repaired |

## Findings

### RE-01 — BLOCK: contrast SC mis-cited
File: `08-ACCESSIBILITY-INCLUSIVE-DESIGN.md` (§4, Visual)

Finding: "WCAG 1.4.3: 4.5:1 normal text, 3:1 large text/**non-text** at AA" folds two
different criteria into one. SC 1.4.3 (Contrast (Minimum)) governs **text** (4.5:1 normal,
3:1 large); **non-text** contrast (3:1 for UI components/graphical objects) is **SC 1.4.11
(Non-text Contrast)**, added in WCAG 2.1.

Fix: Split the citation: 1.4.3 for text, 1.4.11 for non-text. *Disposition: repaired.*

### RE-02 — WARN: target-size rule stated without its exceptions
File: `08-ACCESSIBILITY-INCLUSIVE-DESIGN.md` (§4, Motor)

Finding: "24×24 CSS px at AA" was given as a blanket rule. SC 2.5.8 (Target Size (Minimum))
carries defined exceptions (spacing, equivalent, inline, user-agent control, essential);
the shorthand misstates the norm.

Fix: Bound the rule with its five exceptions. *Disposition: repaired.*

### RE-03 — WARN: semantic contract incomplete
File: `08-ACCESSIBILITY-INCLUSIVE-DESIGN.md` (§3)

Finding: "Every interactive element must expose … name/role/value/state" is wrong on two
counts: **value/state apply only when relevant**, and the contract also includes
**descriptions** and **relationships**. Name+role are the required interactive semantics.

Fix: Rework the table — name+role required, value/state when applicable, add
description/relationships. *Disposition: repaired.*

### RE-04 — WARN: WEIRD limits are asserted but never worked
File: `05-USABILITY-EVALUATION.md` (Global/WEIRD caveats)

Finding: The guide states the method canon is WEIRD-sampled but never shows a contrasting
case, leaving the point abstract.

Fix: Add a **worked** non-US/non-WEIRD, low-resource contrasting example (the *Saheli*
IVR/low-literacy case) that changes methods, instruments, and sample frame. *Disposition:
repaired.*

### RE-05 — WARN: no scaling contract to the rest of the module
File: `05-USABILITY-EVALUATION.md`

Finding: A prototype meant to govern ten more guides gives no account of how its evaluation
discipline scales to the other guide families.

Fix: Add **guide-family scaling contracts** for history (`01`), ethnography/CSCW (`06`,
`09`), emerging-tech (`10`), ethics (`11`), and the combined IA/visualization guide (`07`).
*Disposition: repaired.*

### RE-06 — WARN: global inclusion is caveat-only
File: `08-ACCESSIBILITY-INCLUSIVE-DESIGN.md` (§8, worked case)

Finding: Non-Western, low-bandwidth, low-literacy, and limited-AT-access realities appear
as a bullet list, not as a worked design branch.

Fix: Add a **non-Western/low-bandwidth branch** to the worked case with concrete design
responses (USSD/IVR fallback, light path, local co-design). *Disposition: repaired.*

### RE-07 — WARN: the legal deferral target is incomplete and undisclosed
File: `08-ACCESSIBILITY-INCLUSIVE-DESIGN.md` (§5, §9, worked case)

Finding: The guide routes legal obligation to `law/`, but `law/` currently treats the ADA
only in an employment context and does not yet cover digital-accessibility statutes
(Section 508, EAA, EN 301 549). Deferring to an incomplete target without saying so reads
as a stronger hand-off than exists.

Fix: Add an honesty note that `law/` does not yet deeply cover digital-accessibility
statutes and that the legal-obligation question is **deferred, not answered**. *Disposition:
repaired.*

### RE-08 — BLOCK: records claim a pattern that has not passed
File: `human-computer-interaction/STATUS.md`; architecture record

Finding: STATUS said "The **passed** prototype pattern will govern the remaining ten
guides," and the architecture record framed the guides as merely awaiting sign-off, without
recording the R1 outcome. The gate has not been passed.

Fix: State the pattern as **proposed / not yet ratified**, keep the manifest "ratified" but
the pattern "in review," and record that R1 ran, findings were repaired, and a strict
re-review is pending. *Disposition: repaired.*

### RE-09 — WARN: R1 panel deliverable unrecorded
File: pulse `01+hci-architecture.md`

Finding: The pulse lists the boundary-gate review as a pending deliverable under
`panels/hci-prototype-r1/`, but no such records existed.

Fix: Create the `hci-prototype-r1/` panel records (this file among them) and update the
pulse deliverable to "R1 recorded; findings repaired; strict re-review pending → IN REVIEW."
*Disposition: repaired.*

## Style-contract check (both guides)

| Lens | Assessment |
|---|---|
| Landscape-first + layered | PASS: both open with a landscape diagram and layer downward. |
| Decision Cheat Sheet + Confusions | PASS: present and decision-useful; updated to match repairs. |
| Diagrams do conceptual work | PASS: axes, a11y-tree, discovery-vs-measurement diagrams intact after edits. |
| Dates/standards attributed | PASS after RE-01/02: WCAG versions dated (2.0/2.1/2.2), figures bounded. |
| Reader tasks answerable | PASS: 5 each, consistent with repaired content. |

## Verdict

Factual and structural defects in this lens are corrected and focused MDLOOM is green.
Because every fix was made in the same repair pass, the pattern is **not** ratified on this
record alone. **Recommend Pulse 01 stays IN REVIEW pending a strict R2 re-review.**
