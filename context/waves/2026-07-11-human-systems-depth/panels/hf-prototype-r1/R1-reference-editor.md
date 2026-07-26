# R1 Reference Editor — HF Prototype Boundary Gate (`02`, `03`, `06`)

Round-1 editorial and factual pass over the three prototype guides. Lens: factual accuracy
of named standards/datasets/models (with dates/editions), quantitative-demonstration
completeness, style-contract integrity, scaling-contract completeness, and record
consistency (STATUS / architecture / pulse). Review-only record; fixes were applied in the
same repair pass and marked *disposition: repaired*. Does **not** clear the gate.

## Finding Summary

| # | Guide/record | Lens | Severity | Disposition |
|---|---|---|---|---|
| RE-01 | 02 | CAESAR "~2,400 subjects" stated as the total; the total is ~4,431 (~2,400 North America) | BLOCK | repaired |
| RE-02 | 02 | Reader task says "the seven multipliers"; the NIOSH revised equation has **six** multipliers + a load constant | BLOCK | repaired |
| RE-03 | 03 | Wickens MRT fourth dimension listed as response modality; it is the **visual channel (focal/ambient)** | BLOCK | repaired |
| RE-04 | 06 | Alarm standards stale/incorrect: "EEMUA 191 1st ed. 1999", "ISA-18.2 (2009)" | BLOCK | repaired |
| RE-05 | 02 | No reproducible quantitative demonstration (percentile/joint-accommodation + bounded RNLE sensitivity) | WARN | repaired |
| RE-06 | 06 | No quantitative alarm demonstration (before/after metrics, prioritization, validation) | WARN | repaired |
| RE-07 | 02 | Scaling contracts are per-family slogans, not testable definitions of done for the nine remaining guides | WARN | repaired |
| RE-08 | architecture / pulse | Findings range "MAXIM-HF-01 … 24" (actual 20); gate written as "ratified / remaining step" without a recorded panel | BLOCK | repaired |
| RE-09 | 02 / 03 / 06 | Reader tasks recall-oriented; WARN diagrams/register (schematics, joint-distribution, joint handoff, citation-risk) missing | WARN | repaired |

BLOCK: 5 · WARN: 4.

## Findings

### RE-01 — BLOCK: CAESAR sample count mis-stated
File: `02` (§3 anthropometric data sets; Common Confusion Points)

Finding: "CAESAR … ~2,400 subjects" presents the North-America figure as the whole survey.
Per the CAESAR Final Report (Robinette et al., 2002), the survey totalled **~4,431**
subjects — North America ~2,400, the Netherlands ~1,200, Italy ~775.

Fix: Correct to "~4,431 TOTAL (~2,400 North America, ~1,200 NL, ~775 Italy)"; **verified now**
against the primary source. *Disposition: repaired.*

### RE-02 — BLOCK: "seven multipliers" for the NIOSH equation
File: `02` (Reader Task 4; architecture citation register)

Finding: A reader task asked the reader to describe "the seven multipliers". The revised
NIOSH lifting equation is `RWL = LC x HM x VM x DM x AM x FM x CM` — a **load constant plus
six** dimensionless multipliers (the guide's own §6 structure diagram is correct; the reader
task and the register were not).

Fix: Correct to "the six multipliers" (plus the 23 kg load constant); **verified now** (NIOSH
94-110). *Disposition: repaired.*

### RE-03 — BLOCK: Wickens MRT fourth dimension wrong
File: `03` (§1 multiple resource theory; Reader Task 1)

Finding: The MRT diagram listed the four dimensions as stage / modality / code / **response**.
Wickens' four dimensions are processing **stage**, perceptual **modality**, **visual channel
(focal/ambient)**, and processing **code**; response modality (manual/vocal) is a related but
separate output distinction that maps onto the code dimension.

Fix: Replace the fourth row with the focal/ambient **visual channel**, note response modality
separately, and update the reader task; **verified now** (Wickens, 2002). *Disposition:
repaired.*

### RE-04 — BLOCK: alarm standards stale / mis-editioned
File: `06` (§4 alarm philosophy; Common Confusion Points)

Finding: The guide cited "EEMUA 191 (1st ed. 1999; later editions)" and "ISA-18.2 (2009) /
IEC 62682" without current editions. The current, authoritative editions are **EEMUA 191 4th
ed. (2024)**, **ANSI/ISA-18.2-2016**, and **IEC 62682:2022**.

Fix: Update to the current editions, cite them as **primary/authoritative** sources, and state
they are **industry-specific** (process-industry) guidance — other sectors have their own;
**verified now** against EEMUA/ISA/IEC catalogue records. Benchmark rates kept as dated
guideline figures, never limits. *Disposition: repaired.*

### RE-05 — WARN: no reproducible quantitative demonstration in the scaling gate
File: `02`

Finding: The scaling-gate prototype asserted the percentile/multivariate math and the NIOSH
model but showed no reproducible computation.

Fix: Add a **synthetic worked pass** — percentiles from stated N(mu, sigma); the
joint-accommodation trap computed (`0.90^k`; the positive-correlation bound); a
**joint-distribution anthropometry diagram**; and a **bounded RNLE sensitivity** (all six
multipliers computed, RWL/LI, an H-sweep, and input-error/validity-domain notes). *Disposition:
repaired.*

### RE-06 — WARN: no quantitative alarm demonstration
File: `06`

Finding: The alarm guide reasoned qualitatively with no metrics.

Fix: Add a **synthetic before/after alarm-metrics pass** (steady-state rate, peak flood,
standing alarms, % actionable, priority mix P1/P2/P3), a **prioritization rationale**
(urgency x consequence), and an **uncertainty/validation** note framing the "after" as a
modeled projection and every candidate as a hypothesis for hazard review/MoC/validation.
*Disposition: repaired.*

### RE-07 — WARN: scaling contracts not testable
File: `02` (Guide-Family Scaling Contracts)

Finding: The contracts were per-family prose ("fails if…") without a checkable definition of
done for each remaining guide.

Fix: Add a **Testable Definition of Done** — eight pass/fail gates (required formal model(s),
minimum quantitative demonstration, uncertainty/validity/bias, source hierarchy/edition
checks, boundary test, conceptual diagram, worked fictional case, 3–5 reader tasks) for every
remaining guide (`00`, `01`, `04`, `05`, `07`, `08`, `09`, `10`, `11`), a per-guide specifics
table, and a **common safety & accessibility contract** (incl. HCI/HF/domain joint
acceptance). *Disposition: repaired.*

### RE-08 — BLOCK: records overstate the gate and mis-count the findings
File: `HUMAN-FACTORS-ARCHITECTURE.md`; `03+human-factors-architecture.md`; `STATUS.md`

Finding: The architecture header and pulse cited findings "MAXIM-HF-01 … 24" though only
**MAXIM-HF-01 … 20** exist, and the records described the architecture as "ratified" with the
panel merely a "remaining step", asserting a gate that had not been exercised or recorded.

Fix: Correct the range to **20**; reframe the prototype **pattern/gate as proposed, not
ratified until a strict R2 re-review**; record that R1 ran and its findings were repaired in
the same pass; and note that **load-bearing standards were verified now**. The manifest stays
fixed/ratified; only the pattern/gate is "in review". *Disposition: repaired.*

### RE-09 — WARN: recall-oriented tasks; missing WARN diagrams and register
File: `02` / `03` / `06`; architecture

Finding: Reader tasks leaned on recall; the WARN deliverables (clearly-labelled workload
schematics, a joint-distribution anthropometry diagram, a joint HCI/HF/domain handoff diagram,
and an expanded citation-risk register) were absent.

Fix: Recast all reader tasks to require **calculation / interpretation / uncertainty /
boundary resolution**; label the workload diagrams as schematics; add the joint-distribution
(`02`) and joint-acceptance handoff (`06`) diagrams; and **expand the citation-risk register**
with the verified-now results. *Disposition: repaired.*

## Style-contract check (all three guides)

| Lens | Assessment |
|---|---|
| Landscape-first + layered | PASS: each opens with a landscape diagram and layers down. |
| Decision Cheat Sheet + Confusions | PASS: present and decision-useful; updated to match repairs. |
| Diagrams do conceptual work | PASS: MRT, performance-resource schematic, joint-distribution, alarm, EID, joint-acceptance all intact after edits. |
| Dates/standards attributed | PASS after RE-01…04: editions/counts corrected and verified now. |
| Reader tasks answerable | PASS: 5 each, now computation/boundary-focused. |

## Verdict

Factual, quantitative, scaling, and record defects in this lens are corrected and focused
MDLOOM is green (**3 files checked, 0 errors, 0 warnings**). Because every fix was made in the
same repair pass, the pattern is **not** ratified on this record alone. **Recommend Pulse 03
stays IN REVIEW pending a strict R2 re-review.**
