# R1 Expert Skeptic — HF Prototype Boundary Gate (`02`, `03`, `06`)

Round-1 adversarial pass over the three `human-factors/` prototype guides authored in
Pulse 03:

- `human-factors/02-PHYSICAL-ERGONOMICS-ANTHROPOMETRICS.md` (scaling-gate prototype)
- `human-factors/03-COGNITIVE-WORKLOAD-SITUATION-AWARENESS.md` (review-gated)
- `human-factors/06-DISPLAY-CONTROL-INTERFACE-DESIGN.md` (review-gated)

Lens: advice-creep into operational instruction, construct/threshold reification,
heuristic-as-law diagrams, over-claim, the discretionary/casual-user caricature at the HCI
seam, and metadata truthfulness. This is a **review-only** record; the fixes it calls for
were applied in the same repair pass and are marked *disposition: repaired*. It does **not**
clear the gate — see the verdict.

## Finding Summary

| # | Guide | Risk | Severity | Disposition |
|---|---|---|---|---|
| ES-01 | 02 | Worked case reads as operational lifting direction ("cut the horizontal distance", "raise the origin", "remove the twist", set the work–rest schedule) | BLOCK | repaired |
| ES-02 | 03 | Vigilance/flood advice prescribes live-operational intervention (shorter watch rotations, injected live signals, real-time probes during a live flood response) | BLOCK | repaired |
| ES-03 | 06 | Alarm section issues operational direction (delete / suppress / set deadband) on a running alarm system | BLOCK | repaired |
| ES-04 | 03 | Performance–workload curve presents "the redline" as a near-universal threshold rule | WARN | repaired |
| ES-05 | 03 | Heuristic "WORKLOAD = demand / supply" drawn as an equation, inviting computation | WARN | repaired |
| ES-06 | 06 | HCI's users caricatured as "discretionary / (possibly casual)"; a safety-critical UI framed as not-an-HCI-system | WARN | repaired |
| ES-07 | 03 | Worked case asserts instrument dissociation but never computes it | WARN | repaired |

BLOCK: 3 · WARN: 4.

## Findings

### ES-01 — BLOCK: the worked case reads as operational lifting instruction
File: `02` (worked case, steps 3 and 5)

Finding: The Meridian Freight case told the reader to "cut the horizontal distance (cart
closer, no reaching across)", "raise the origin (cart shelf, not floor)", "remove the twist
(linear layout)", and to set the work–rest schedule "against the hot case". Written as
directives, these are operational ergonomics instructions — exactly the advice-creep the
safety/ethics contract forbids.

Consequence: A reader could treat a fictional teaching case as a workplace prescription.

Fix: Recast the lift terms as a **design-variable analysis** — hypothetical model
comparisons (nearer/farther cart changes HM, a raised origin changes VM, a twist-free layout
changes AM) that identify which variable the modeled LI is most sensitive to, explicitly
labelled **model comparisons, not recommendations**, with any actual change to placement,
origin, layout, rate, or schedule requiring **qualified assessment and local validation**.
The work–rest line became a modeled hot-vs-nominal comparison, not a set schedule.
*Disposition: repaired.*

### ES-02 — BLOCK: live-operational vigilance/flood interventions prescribed
File: `03` (§4 vigilance; cheat sheet; non-WEIRD contrasting example)

Finding: The vigilance section prescribed "shorter watch rotations, injected
signals/verification" and the cheat sheet said "rotate/inject/alert"; the flood-response
contrasting example substituted "real-time SPAM-style probes over the radio" *during a live
flood response*. Injecting live signals into a running watch and probing operators mid-
emergency are operational interventions, not educational measurement.

Consequence: Reads as direction to intervene in live safety-critical operations.

Fix: Recast to **offline simulation / replay** or **descriptive measurement** — characterize
the decrement offline via simulation/replay of recorded signals or descriptive
detection-vs-time measurement (not by injecting live signals or altering live rotations);
candidate mitigations are framed as design **hypotheses to validate**. The flood example now
uses descriptive, retrospective reconstruction from radio/log records plus offline replay in
a training setting, with the weakened evidential value stated. *Disposition: repaired.*

### ES-03 — BLOCK: the alarm section issues operational direction
File: `06` (§4 alarm management; worked case step 3; non-WEIRD example)

Finding: The alarm-management block directed the reader to "SUPPRESS SMARTLY", set
"deadbands", apply "state-based suppression", and (in the non-WEIRD case) "delete no-action
alarms". Applied to a running alarm system these are operational changes with direct safety
consequence.

Consequence: Advice-creep into plant operating direction — the highest-risk failure mode for
this module.

Fix: Reframe every lever as a **candidate change / hypothesis** subject to **hazard review,
management of change (MoC), qualified domain validation, and local procedures** before any
live change; "delete" became "candidate for demotion", the CHATTERING deadband became "a
candidate for a deadband, subject to review", and the worked case routes each candidate
through MoC rather than editing a live system. *Disposition: repaired.*

### ES-04 — WARN: the "redline" is presented as a near-universal threshold rule
File: `03` (§2 performance-resource function)

Finding: The performance-resource diagram and caption read as if a fixed "redline" governs
every operator, treating a schematic inflection as a law.

Fix: Relabel the diagram **(schematic — positions are task-dependent)** and state that the
curve's shape and where the "redline" sits depend on **task, strategy, expertise, and
context — there is NO universal redline value**; keep only the reusable point (performance is
flat until the drop-off, so measure the reserve). *Disposition: repaired.*

### ES-05 — WARN: a heuristic drawn as an equation
File: `03` (Big Picture)

Finding: "WORKLOAD = demand / supply" is a heuristic, but the equation form invites the
reader to treat it as a computable ratio.

Fix: Relabel as a **schematic** ("WORKLOAD: demand-vs-supply (schematic; how much
reserve?)"), consistent with the guide's proxy-measurement framing. *Disposition: repaired.*

### ES-06 — WARN: the discretionary/casual-user caricature at the HCI seam
File: `06` (§9 seam; prototype seam contract)

Finding: HCI's object was described as "a discretionary interactive system used by a
(possibly casual) user", implicitly framing the safety-critical UI as *not* an HCI system.
This caricatures HCI and mis-draws the seam.

Fix: State that **safety-critical systems remain HCI systems**; HCI owns the
interaction/visualization/accessibility **methods** for *every* interactive system, human
factors supplies the **safety requirements + performance-under-stress validation**, and the
**domain module** owns implementation/acceptance. Record **joint acceptance** (a new handoff
diagram) in `06` (§9) and `02` (§8), and in STATUS and the architecture record. *Disposition:
repaired.*

### ES-07 — WARN: dissociation asserted but never computed
File: `03` (worked case)

Finding: The redesign case claimed workload/SA instruments dissociate but showed no numbers,
so the reader cannot see the dissociation or resolve it.

Fix: Add a **synthetic worked pass** with a toy NASA-TLX (six subscales, raw **and** weighted
computed in full: RTLX 48.8 vs weighted 60.3), plus primary-task, secondary-task, and SAGAT
figures that **disagree**, and three explicit alternative interpretations (dissociation vs
instrument/underpowered vs profile), with uncertainty/validity notes. *Disposition:
repaired.*

## Metadata check

Frontmatter on all three guides is already truthful (`status: prototype`,
`source_custody: needs-source`, `backsource_ids: []`) and no Gold/Da Vinci tier or
`context/gold` row is claimed — no change required in this lens.

## Verdict

The prototypes now clear the advice-creep, reification, heuristic-diagram, and seam-caricature
risks in this lens, and focused MDLOOM stays green (**3 files checked, 0 errors, 0 warnings**).
**This does not ratify the pattern.** All seven findings were fixed by the same author in the
same pass; an independent, **strict re-review (R2)** is required before the pattern can govern
the Pulse-04 authoring of the remaining nine guides. Recommendation: **Pulse 03 remains IN
REVIEW.**
