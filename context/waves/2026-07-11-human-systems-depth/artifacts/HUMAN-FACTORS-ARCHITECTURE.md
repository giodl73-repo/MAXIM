---
wave: human-systems-depth
pulse: 03
kind: architecture-record
module: human-factors
date: 2026-07-12
status: ratified
governing_roles: [reference-editor, expert-skeptic]
---

# human-factors/ — Architecture & Research Record (Pulse 03)

Wave-local architecture record for `human-factors/`. Condenses the Pulse-03 design
research into a durable reference: the research question, the numbered findings
(MAXIM-HF-01 … MAXIM-HF-20), the ratified 12-guide manifest with per-guide architecture
IDs (G00 … G11), the ownership/defer matrix, the HCI↔human-factors seam, the safety/ethics
contract, the standards/citation-risk register, known biases/limitations, quality risks,
the prototype/scaling rationale (the two-stage scaling gate for `02` and the review gates
for `03`/`06`), and the adopt/prototype/defer decisions. This record governs the Pulse-04
authoring pass.

> **Current status: DONE — Pulse 03 prototype boundary review; prototype pattern/gate
> ratified (R1 + independent R2).** The architecture is recorded and the 12-guide manifest is
> fixed; the three prototype guides (`02` scaling-gate, `03` and `06` review-gated) are
> authored at full peer depth and pass focused MDLOOM (3 files checked, 0 errors, 0 warnings).
> The R1 boundary-gate panel (`panels/hf-prototype-r1/`) found and drove repair of the
> conservative-prototype findings; because it both raised and repaired them it could not
> self-ratify, so an **independent strict re-review (R2)** (`panels/hf-prototype-r2/`) —
> which neither authored nor repaired those findings — re-derived the quantitative passes,
> re-checked the standards, and confirmed the safety-contract, seam, and record repairs,
> closing its finer-grained findings with **no unresolved BLOCK/WARN**. The prototype
> **pattern/gate is now ratified**. Load-bearing standards/dataset claims were verified
> against primary sources (see the register below). **No** module integration, **no** source
> backfill, and **no** edits to sibling modules were made. **No** Gold/Da Vinci eligibility
> or registry insertion is claimed.

## Summary

`human-factors/` is designed as the **operator-and-safety layer of MAXIM's engineering
verticals** — the discipline of *human performance, error, and safety in the operation of
complex systems*. Its unique, non-duplicating value is the **quantitative-systems view of
the human in a system of work**: physical ergonomics/anthropometrics at population-
distribution depth, cognitive workload and situation awareness as measured constructs,
human-error taxonomies, human-reliability analysis, safety-critical display/control/
control-room design, automation and function allocation, safety-systems and hazard
analysis, domain applications, methods/measurement, and organizational safety culture. It
is **not** the compact product-form ergonomics of `industrial-design/05`, the cognitive
mechanism of `cognitive-science/`, the interactive digital usability of
`human-computer-interaction/`, the reliability mathematics of `systems-engineering/06`, or
the domain systems of `nuclear/`, `aeronautics/`, `transportation/`, and
`biomedical-engineering/`. The pivotal architecture call is to organize **by the
human-factors problem (fit, load, error, reliability, interface, automation, hazard,
method, culture), not by domain** — the single most important non-duplication decision,
mirroring chemistry's "split by problem, not technique" and clinical-medicine's "reusable
reasoning patterns, not per-organ specialties." The sharpest overlap is
`industrial-design/05-ERGONOMICS`, which already carries a broad "ergonomics and human
factors" treatment; it is resolved by keeping `industrial-design/05` the **compact
product-form entry** while human factors owns the **quantitative-systems depth**. A strict
safety/ethics contract (no operational instruction, no certification, no accident/legal
ruling, no individual fitness assessment) is mandatory throughout and is *stricter* than
HCI's, because human factors touches operations where advice-creep is dangerous.

## Research Question

How should MAXIM add a standalone `human-factors/` module that is independently useful as a
peer-level educational reference on human performance and safety in complex systems,
**without** (a) duplicating the product-form ergonomics (`industrial-design/05`), cognitive
mechanism (`cognitive-science/`), reliability mathematics (`systems-engineering/06`),
clinical patient-safety practice (`clinical-medicine/11`), or domain systems (`nuclear/`,
`aeronautics/`, `transportation/`, `biomedical-engineering/`) MAXIM already owns; (b)
re-opening or contradicting the completed `human-computer-interaction/` module and the
HCI↔HF seam it already locked; and (c) drifting into operational instruction, safety
certification, or accident/legal determination? Sub-questions: the right 12-guide manifest
and deep scope; whether to organize by domain or by human-factors problem; exact boundaries
against the seven overlap modules; the reciprocal HCI↔HF seam; the safety/ethics contract;
and which guides to prototype to prove the hardest boundaries before authoring the rest.

## Findings

### Repository conventions & the depth bar

- **MAXIM-HF-01 — Module shape is fixed by convention.** `00-OVERVIEW` (landscape/taxonomy)
  + `01…N` numbered `UPPERCASE-HYPHENATED.md` guides + `STATUS.md` (manifest, not counted).
  Each guide carries `maxim.frontmatter.v1` YAML (`id: maxim:human-factors:<slug>`,
  `module`, `section: human-factors`, `title`, `status`, …). A **prototype** guide
  (pre-backfill, as here) must be truthful: `status: prototype`,
  `source_custody: needs-source`, `backsource_ids: []`; only after source-corpus backfill
  does it graduate to `status: source-custody` with populated `backsource_ids`. The three
  Pulse-03 prototypes (`02`, `03`, `06`) carry exactly this truthful metadata.
- **MAXIM-HF-02 — Style contract & MDLOOM surface.** Landscape diagram first → layer down →
  ASCII boxes → decision-useful tables → universal-first bridges → **Decision Cheat Sheet**
  + **Common Confusion Points**; ~32,000-token cap per guide. `mdloom.toml` enforces
  `max_h1 = 1`, a required `## Decision Cheat Sheet`, at least one code block, and
  ASCII-box width consistency (±2 tolerance); it **excludes** `*/STATUS.md`,
  `*/00-OVERVIEW.md`, and `context/**`, so only the numbered content guides are MDLOOM-checked.
  The prototypes use an "open" diagram idiom (rules + indentation + arrows) that passes the
  box-width checker cleanly.
- **MAXIM-HF-03 — clinical-medicine and chemistry are the governing depth exemplars**, both
  deeper than the `computing/01-PACKAGE.md` floor; the completed HCI prototypes (`05`, `08`)
  are the immediate in-wave pattern. Reusable structure inherited: opening landscape + caption;
  ownership header ("owns / builds on / defers to"); per-guide banner; a fully worked
  **fictional** case; 3–5 reader tasks; Decision Cheat Sheet; Common Confusion Points;
  global/WEIRD/resource caveats; a **non-WEIRD contrasting case**; and — for the scaling-gate
  prototype — the **Guide-Family Scaling Contracts**.
- **MAXIM-HF-04 — Review is adversarial and evidence-gated.** 3–5 reader tasks answerable
  without another source; diagrams that do conceptual work; tables that decide/compare/
  compress; a focused numbers/names/**dates** fact-check. Lenses: `expert-skeptic`
  (overclaims, advice-creep, stale/undated figures, construct reification) and
  `reference-editor` (factual/standards accuracy, style-contract integrity); findings are
  BLOCK/WARN/NOTE; the exit gate requires no unresolved BLOCK.

### Placement in the library

- **MAXIM-HF-05 — Belongs in the Technology (Ray 7) engineering vertical**, adjacent to
  `systems-engineering/` and `biomedical-engineering/`, with strong seams *out* to
  `human-computer-interaction/` (Computing & Software), `cognitive-science/` (Life Sciences),
  and `industrial-design/` (Arts & Culture). Section/nav/`TRACKER` integration is **deferred
  to Pulse 04**; this pulse leaves the incomplete module unintegrated per the wave guardrail.

### Overlap inventory (the core boundary problem)

- **MAXIM-HF-06 — CRITICAL: `industrial-design/05-ERGONOMICS` already carries a broad
  "ergonomics and human factors" treatment** (physical/cognitive/organizational ergonomics,
  anthropometrics with 5th/50th/95th percentiles, RULA, grip/posture, universal design).
  This is the biggest duplication risk — the HF analog of the `cognitive-science/09` overlap
  that dominated the HCI wave. **Resolution:** `industrial-design/05` remains the **compact
  product-form entry** (the object in the hand/under the body; Norman affordances; the seven
  universal-design principles), while `human-factors/02` owns the **quantitative-systems
  depth** (population-distribution modeling with z-scores and *multivariate* accommodation;
  occupational biomechanics; the NIOSH lifting model as a bounded model; posture indices;
  work–rest/environment; population MSD dose–response). Guide `02` **prototypes** this
  boundary and is the module's scaling gate.
- **MAXIM-HF-07 — CRITICAL: `cognitive-science/09-APPLIED-BRIDGE` owns the psychophysical
  laws AND Endsley SA + Klein NDM as cognitive theory** (its "Cognitive Ergonomics" section).
  **Resolution:** `cognitive-science/` owns the **mechanism and the theory**; `human-factors/03`
  owns the **operator-in-context measurement and design** — workload instruments (NASA-TLX
  raw/weighted, physiological, performance), the vigilance decrement, SA *measurement*
  (SAGAT/SPAM/SART) and its critiques, tunneling, and team/distributed SA. Guide `03`
  **prototypes** this boundary (review gate).
- **MAXIM-HF-08 — `human-computer-interaction/` (COMPLETE, Pulse 02) already locked the
  HCI↔HF seam from its side.** Human factors adopts the reciprocal without re-opening HCI:
  **HF owns** operator performance, physical/cognitive workload, human-error taxonomy,
  safety-critical integration, and performance under stress/fatigue; **HCI owns** interactive
  digital usability, interaction design, IA/visualization, interactive accessibility, and
  evaluation. Guide `06` **prototypes** the safety-critical-UI↔HCI-usability seam (review gate).
- **MAXIM-HF-09 — `systems-engineering/06-FMEA-RELIABILITY` owns FMEA/FTA and reliability
  mathematics/hardware.** Human factors' guides `05` (HRA) and `08` (hazard analysis) **extend
  this to the human** — human-error-probability estimation, performance-shaping factors,
  human-inclusive FMEA/bow-tie/STAMP — borrowing the machinery, not re-deriving it.
- **MAXIM-HF-10 — `clinical-medicine/11-SAFETY-QUALITY-AND-WORKFLOW` owns the *clinical*
  patient-safety systems practice** (Swiss cheese, just culture, RCA, HRO, Donabedian,
  clinical error taxonomy). Human factors owns the **generic** error taxonomy (`04`), HRA
  (`05`), and organizational safety culture (`11`); the clinical application defers to
  `clinical-medicine/11`. Both cite Reason/Swiss-cheese/just-culture from different ownership;
  the reciprocal pointer is a Pulse-04 decision.
- **MAXIM-HF-11 — Domain modules own their systems.** `nuclear/05-SAFETY-SYSTEMS` (defense-in-
  depth, RPS/ECCS, PRA), `aeronautics/04-AVIONICS` (FMS, autopilot, cockpit displays),
  `transportation/07-AUTONOMOUS-VEHICLES` (SAE J3016), `biomedical-engineering/07-MEDICAL-
  DEVICES` (regulation) and `/01-BIOMECHANICS` (engineering biomechanics). Human factors'
  guides `06`/`07`/`09` **apply HF principles and defer the domain systems**; guide `09`
  (Domain Applications) is the one deliberately domain-organized guide and exists precisely to
  *apply and defer*, never to re-teach a domain.

### External framework grounding (authoritative but datable)

- **MAXIM-HF-12 — The discipline's named models are real, attributable, and datable** and
  must be treated as such (see the standards/citation-risk register below): multiple resource
  theory (Wickens, 1984/2002); NASA-TLX (Hart & Staveland, 1988); SAGAT (Endsley, 1988/1995);
  SPAM (Durso et al., 1990s); SART (Taylor, 1990); the vigilance decrement (Mackworth, 1948);
  the NIOSH lifting equation (1981; revised Waters, Putz-Anderson, Garg & Fine, 1993;
  applications manual 1994); RULA (McAtamney & Corlett, 1993); REBA (Hignett & McAtamney,
  2000); OWAS (Karhu et al., 1977); Snook tables (Snook & Ciriello, 1991); Warrick's principle
  (1947); EEMUA 191 (4th ed. 2024; 1st ed. 1999); ANSI/ISA-18.2-2016; IEC 62682:2022;
  Rasmussen's SRK (1983); ecological
  interface design (Vicente & Rasmussen, 1992); the ironies of automation (Bainbridge, 1983);
  levels of automation (Sheridan & Verplank, 1978; Parasuraman, Sheridan & Wickens, 2000);
  Reason's Swiss-cheese/GEMS (1990); HEART (Williams, 1988); THERP (Swain & Guttmann, 1983);
  SPAR-H (2005); STAMP/STPA (Leveson, 2004+); Safety-II/resilience engineering (Hollnagel).
- **MAXIM-HF-13 — Every quantitative model is a *bounded* model** with an explicit validity
  domain and a failure mode outside it (the NIOSH equation "goes silent," not conservative,
  outside its assumptions; a human-error probability is a wide, method-bounded estimate, not a
  fact). This bounded-model stance is the module's signature epistemic contribution and is
  prototyped in guide `02` (the lifting model) and inherited module-wide.

### The organizing decision (pivotal call)

- **MAXIM-HF-14 — Organize by the human-factors *problem*, not by domain.** Domain-first
  organization (aviation HF / medical HF / nuclear HF) would collide head-on with the domain
  modules and force re-teaching their systems. Problem-first organization (fit, load, error,
  reliability, interface, automation, hazard, method, culture) keeps every guide
  non-duplicating and lets guide `09` *apply* the models across domains while *deferring* the
  systems. This is the module's most important non-duplication decision.
- **MAXIM-HF-15 — Two orthogonal spines, joined.** A **fit/load** spine (physical `02`,
  cognitive `03`) and an **error/safety** spine (`04` taxonomy, `05` reliability, `08` hazard,
  `11` culture), joined by the **interface/automation** guides (`06`, `07`), grounded by
  **method** (`10`) and **domain application** (`09`), and framed by **history** (`01`) and the
  **overview** (`00`). The three prototypes deliberately sample both spines and the join.

### Prototype & scaling decisions

- **MAXIM-HF-16 — Guide `02` is the two-stage *scaling-gate* prototype.** It simultaneously
  stresses the module's quantitative-model depth (population statistics + the NIOSH bounded
  model) and its sharpest overlap (`industrial-design/05`), and it carries the module-wide
  **Guide-Family Scaling Contracts**. It is the gate the other eleven guides scale from.
- **MAXIM-HF-17 — Guides `03` and `06` are review-gated prototypes** that stress the other two
  hard boundaries: the cognitive-mechanism seam (`03`↔`cognitive-science/09`) and the
  HCI-usability + domain-deferral seam (`06`↔HCI/nuclear/aero/bme/transport). Each records its
  gate as a "Prototype Seam Contract."
- **MAXIM-HF-18 — No source backfill in this pulse.** Per the wave guardrail, prototype
  boundary review runs no MDLOOM/MDCROP/MDPORT/FLETCH backfill; metadata stays `needs-source` /
  `backsource_ids: []`. Backfill is a Pulse-04 deliverable.

### Safety/ethics, bias, and reification

- **MAXIM-HF-19 — The safety/ethics contract is a hard gate and is stricter than HCI's.**
  Educational systems reference only; no operational instruction (no lifting how-to, no
  operating procedures); no certification/compliance ruling; no accident/legal determination;
  no individual fitness-for-duty or clinical assessment; all named models/standards/stereotypes
  attributed, dated, bounded. Human factors touches operations (lifting, plant control, clinical
  work) where advice-creep is materially dangerous, so the contract is enforced by a banner in
  every guide plus the bounded-model framing.
- **MAXIM-HF-20 — The data and instrument canon is WEIRD/Western-industrial/military-skewed.**
  ANSUR/CAESAR anthropometry, TLX/SAGAT validation samples, alarm-management standards, and
  population stereotypes are all culture- and era-bound. Every guide carries global/WEIRD/
  resource caveats and a non-WEIRD contrasting case.

## Ratified Guide Manifest (12 guides: 00 + 11)

| ID | # | File | Uniquely owns (at peer depth) | Pulse-03 state |
|---|---|---|---|---|
| G00 | 00 | `00-OVERVIEW.md` | Discipline map; fit/load + workload/SA frames; ownership/defer matrix; HCI↔HF seam; safety/ethics contract; reading order | planned (Pulse 04) |
| G01 | 01 | `01-HISTORY-FOUNDATIONS.md` | HF intellectual roots (scientific management → WWII knobs-and-dials/aviation psychology → Fitts/Chapanis → systems ergonomics → resilience engineering) and why lineage constrains idioms | planned (Pulse 04) |
| G02 | 02 | `02-PHYSICAL-ERGONOMICS-ANTHROPOMETRICS.md` | Population distribution/percentile & multivariate accommodation; clearance/reach/strength logic; occupational biomechanics; NIOSH lifting model as bounded model; posture indices; work–rest/environment; MSD dose–response; product↔workplace boundary | **authored — scaling-gate prototype** |
| G03 | 03 | `03-COGNITIVE-WORKLOAD-SITUATION-AWARENESS.md` | Workload (MRT, dissociation, NASA-TLX raw/weighted+limits, physiological/performance measures), vigilance, SA levels/measurement (SAGAT/SPAM/SART)+critiques, tunneling, team/distributed SA; mechanism deferred | **authored — prototype (review-gated)** |
| G04 | 04 | `04-HUMAN-ERROR-TAXONOMIES.md` | Slips/lapses/mistakes (Reason), skill/rule/knowledge errors, violations, latent conditions, error as a systems property | planned (Pulse 04) |
| G05 | 05 | `05-HUMAN-RELIABILITY-ANALYSIS.md` | HRA methods (THERP/HEART/SPAR-H/CREAM), human-error-probability as bounded estimate, performance-shaping factors; borrows FTA/reliability math from `systems-engineering/06` | planned (Pulse 04) |
| G06 | 06 | `06-DISPLAY-CONTROL-INTERFACE-DESIGN.md` | Compatibility & population stereotypes (cultural caveats), coding/redundancy, alarm philosophy, salience vs nuisance, mode/state visibility, EID, control-room layout; safety-critical-UI↔HCI seam; domains deferred | **authored — prototype (review-gated)** |
| G07 | 07 | `07-AUTOMATION-HUMAN-MACHINE.md` | Levels of automation (Sheridan; Parasuraman–Sheridan–Wickens), ironies of automation (Bainbridge), trust/complacency/automation bias, out-of-the-loop, function allocation, human–autonomy teaming; domain autopilots deferred | planned (Pulse 04) |
| G08 | 08 | `08-SAFETY-SYSTEMS-AND-HAZARD-ANALYSIS.md` | Barrier/defense-in-depth models, HAZOP/what-if, human-inclusive FMEA, bow-tie, STAMP/STPA, safety-case reasoning; borrows FTA/FMEA from `systems-engineering/06`; no certification | planned (Pulse 04) |
| G09 | 09 | `09-DOMAIN-APPLICATIONS.md` | Aviation/healthcare/process/rail/maritime/road applications that **apply** the models and **defer** domain systems to their owners | planned (Pulse 04) |
| G10 | 10 | `10-METHODS-AND-MEASUREMENT.md` | Task analysis (HTA, cognitive task analysis), observation, simulation, physiological-measurement instrumentation, usability-for-safety; inferential statistics deferred | planned (Pulse 04) |
| G11 | 11 | `11-ORGANIZATIONAL-SAFETY-CULTURE.md` | Safety culture/climate, HRO, just culture, Safety-I vs Safety-II/resilience, reporting systems, normalization of deviance | planned (Pulse 04) |

## Ownership / Defer Matrix

| Area | Owner | Human factors' relationship |
|---|---|---|
| Product-form ergonomics (handles, seats, knobs, affordances, universal design) | `industrial-design/05-ERGONOMICS` | **Defer**; HF owns the quantitative-systems depth (G02) |
| Cognitive mechanism; psychophysical laws; SA/NDM as theory | `cognitive-science/` (esp. `09`) | **Defer**; HF owns operator-in-context measurement/design (G03) |
| Interactive digital usability, interaction design, IA/visualization, a11y evaluation | `human-computer-interaction/` | **Defer** (reciprocal seam); HF owns safety-critical interface (G06) |
| FMEA/FTA and reliability mathematics/hardware | `systems-engineering/06-FMEA-RELIABILITY` | **Borrow**; HF extends to the human (G05, G08) |
| Clinical patient-safety practice; diagnosis/treatment | `clinical-medicine/` (esp. `11`) | **Defer**; HF owns generic error/culture/HRA (G04, G05, G11) |
| Engineering biomechanics; medical-device engineering/regulation | `biomedical-engineering/01`, `/07` | **Defer**; HF owns occupational load-screening (G02) and use-safety concepts (G09) |
| Domain systems (reactor safety, avionics, vehicle autonomy) | `nuclear/05`, `aeronautics/04`, `transportation/07` | **Defer**; HF applies principles (G06, G07, G09) |
| Inferential statistics, sampling, power | `statistics-applied/` | **Defer**; HF owns study/measurement design (G10) |
| Legal obligation, liability, compliance | `law/` | **Defer**; HF issues no legal/compliance ruling |
| General organizational theory | `organizational-behavior/` | **Defer**; HF owns safety culture specifically (G11) |

## HCI ↔ Human Factors Seam (ratified, reciprocal to the completed HCI module)

- **HCI owns** interactive digital-interface design, usability, interactive accessibility,
  and evaluation.
- **Human factors owns** operator performance, physical/cognitive workload, human-error
  taxonomy, safety-critical integration, and performance under stress or fatigue.
- At shared systems (clinical-device, avionics, control-room touchscreens): **HCI** owns
  interaction design and usability/accessibility evaluation; **human factors** owns
  workload/SA support, error-consequence, alarm philosophy, mode visibility, and safety
  analysis; **domain modules** own the systems; **`law/`** owns legal obligation. This is the
  reciprocal of the seam `human-computer-interaction/STATUS.md` already records.
- **Evidence vs acceptance (safety-critical systems remain HCI systems).** A safety-critical
  console is still an HCI system, not a lesser or "non-user" one — the discretionary/casual-
  user caricature is rejected. The MAXIM modules own **methods and evidence, not sign-off**:
  HCI supplies the interaction/visualization/accessibility **methods/evidence**; human factors
  supplies the **workload/error and performance-under-stress evidence** (plus the safety
  requirements it can state); **acceptance and implementation are owned by the accountable
  domain organization and its regulator**, not by any reference module; `law/` owns legal
  obligation. No reference module signs off or vetoes a real system. Recorded in guides
  `02` (§8), `06` (§9), and `STATUS.md`.

## Safety / Ethics Contract (mandatory review gate)

1. **Educational systems reference** — no operational instructions (no lifting how-to, no
   operating procedures, no runnable operations).
2. **No certification or compliance ruling** — nothing declares a task, operator, or system
   safe/compliant/passing.
3. **No accident or legal determination** — event causation belongs to the module's
   error/hazard methods (`04`/`08`), not to labels ("loss of SA").
4. **No individual fitness-for-duty or clinical assessment** — screening models are
   population-level estimates, never a medical judgment about a person.
5. **Attributed, dated, bounded** — every named model/standard/stereotype (NIOSH, RULA/REBA,
   NASA-TLX, SAGAT, EEMUA 191/ISA-18.2, population stereotypes) carries a date, an attribution,
   and an explicit validity domain.

## Standards / Citation-Risk Register

The three prototypes are truthfully `source_custody: needs-source` with `backsource_ids: []`
and **no source-corpus backfill runs in this pulse**. The **load-bearing** standards and
dataset claims were **verified** against primary/authoritative sources during the R1 boundary
review (`panels/hf-prototype-r1/`) and **re-checked in the independent R2 re-review**
(`panels/hf-prototype-r2/`); remaining low-risk figures are precision spot-checks deferred to
Pulse-04 backfill. On the deferred items the risk is *precision*, not *direction*, and every
guide already frames each figure as dated/bounded. Per the guide-`02` Definition of Done
(closure gates), **no citation-risk item may remain unresolved at a guide's final sign-off**
— these deferred spot-checks are Pulse-04 authoring items, not open items at the prototype
gate, whose load-bearing claims are already verified.

| Claim (in guide) | Risk | Verification status (this pulse) / residual action |
|---|---|---|
| NIOSH revised equation: 23 kg load constant + **six** multipliers (HM,VM,DM,AM,FM,CM); revised 1991, Waters et al. 1993, applications manual 1994 (`02`) | Was medium — guide had said "seven multipliers" | **Verified now** (NIOSH 94-110): **six** multipliers plus the load constant; guide corrected; forms kept conceptual/synthetic |
| Anthropometric sets: ANSUR II 2012 (n≈6,068, 93 measures); CAESAR ~**4,431 total** (~2,400 North America, ~1,200 NL, ~775 Italy), ~1998–2000 (`02`) | Was medium — guide had used "~2,400" as the total | **Verified now** (CAESAR Final Report, Robinette et al. 2002): total ~4,431, North America ~2,400; guide corrected |
| Wickens MRT four dimensions: processing **stage**, perceptual **modality**, **visual channel (focal/ambient)**, processing **code** (`03`) | Was medium — guide had listed response modality as the 4th | **Verified now** (Wickens 2002): the 4th dimension is the focal/ambient visual channel; response modality maps onto code and is noted separately; guide corrected |
| Alarm standards: **EEMUA 191 4th ed. 2024** (1st ed. 1999); **ANSI/ISA-18.2-2016**; **IEC 62682:2022** (`06`) | Was **high** — guide had only 1st-ed EEMUA / ISA-18.2 2009 | **Verified now** (EEMUA/ISA/IEC catalogue records): editions corrected; benchmark rates kept as dated process-industry guidelines, never limits |
| EEMUA benchmark rates (steady-state ~a few/hr; flood > 10/10 min) (`06`) | Medium — specific figures | **Framed now** as dated, process-industry guideline figures (not limits); confirm exact figures vs EEMUA 191 4th ed. at backfill |
| z-quantiles (±1.645, ±2.326); rho=0.5 joint central coverage ~0.8245 (bivariate-normal box, inclusion–exclusion); RNLE sensitivity with CM/FM from public-domain NIOSH 94-110 (`02`) | Low — standard quantiles; reproducible synthetic arithmetic; public-domain lookup | **Re-derived in R2**: joint coverage 0.8245 confirmed and bounded over rho in [0.3, 0.7]; CM=1.00 for V>=75 cm/fair coupling and explicit FM (F=3/min, <=1 h) corrected; math synthetic/illustrative, no external-citation risk |
| RULA 1–7 bands; REBA/OWAS/Snook attributions & dates (`02`) | Medium — score-band wording | Confirm band cut-points and citation years at backfill |
| NASA-TLX six subscales, 15 pairwise weights, RTLX; toy TLX arithmetic (`03`) | Low/Medium — procedure well known; synthetic data | Confirm procedure (Hart & Staveland 1988); **re-derived in R2** for one representative participant with **common weighting** across conditions (RTLX A 49.2 / B 48.8; weighted A 53.9 / B 60.3); numbers **synthetic** |
| SAGAT/SPAM/SART attributions & dates (`03`) | Medium — attribution precision | Confirm Endsley 1988/1995, Durso, Taylor 1990 at backfill |
| Vigilance decrement onset "~20–35 min" (`03`) | Medium — task-dependent | Framed as task-dependent range (caveated); cite Mackworth 1948 at backfill |
| Warrick's principle (1947); EID (Vicente & Rasmussen 1992); SRK (Rasmussen 1983) (`06`) | Low/Medium — attribution precision | Confirm citation years at backfill |
| Color-vision-deficiency "~8% of males" (`06`) | Low — widely cited | Spot-check at backfill |
| Air Inter 1992 mode-confusion illustration (`06`) | Medium — mode-visibility lesson only; system deferred to `aeronautics/04` | Confirm framing; keep system out of scope |

## Bias / Geographic Limitations

- **Anthropometry and instruments are Western/military-skewed** (ANSUR, CAESAR; TLX/SAGAT
  validation), so tails and norms mis-transfer to other populations — mitigated by per-guide
  caveats and non-WEIRD contrasting cases.
- **Population stereotypes are cultural and dated** (switch/rotary direction, color meaning),
  so `06` verifies against the actual operator population and hardens with redundant coding.
- **Alarm/EID standards are process-industry, Western-industrial** guidance, not universal.
- **Resource asymmetry** (scanners, EEG, simulators, alarm platforms) shapes which methods
  are available; low-resource practice reuses foreign tables/instruments, magnifying error —
  the correction is stated uncertainty, not a borrowed constant.

## Quality Risks (with mitigations)

| Risk | Mitigation |
|---|---|
| **Advice-creep** into operational instruction/certification/accident rulings (the top risk for HF) | The safety/ethics contract + per-guide banner + the "bounded model, no procedure" framing; worked cases are explicitly fictional and non-operational |
| **Duplication** with `industrial-design/05`, `cognitive-science/09`, `clinical-medicine/11`, `systems-engineering/06` | The ownership/defer matrix + the three prototypes that prove the boundaries on real content |
| **Stale/undated figures; universalized constants** | Dated/attributed/bounded discipline; the standards/citation-risk register; the Pulse-04 numbers/names/dates fact-check |
| **Reifying constructs** (workload/SA treated as facts) | Proxy-measurement framing + the SA-construct (folk-model/circularity) critique carried in `03` |
| **Re-teaching domain systems** in guide `09` | Guide `09` is defined as *apply-and-defer*; domain systems point to their owners |

## Prototype / Scaling Rationale (why `02`, `03`, `06` went first)

Rather than author twelve guides and discover the boundaries in review, the three guides
that most stress the module's boundaries were authored first:

- **`02` de-risks the sharpest overlap** (`industrial-design/05`) *and* the quantitative-model
  depth in one guide, so it is the **two-stage scaling gate** (Stage 1: the percentile/
  multivariate math and the NIOSH bounded model are correct, dated, bounded; Stage 2: the
  product↔workplace split is clean, and the guide carries the Guide-Family Scaling Contracts).
- **`03` de-risks the cognitive-mechanism seam** — proving human factors can own workload/SA
  *measurement and design* while deferring the *theory* to `cognitive-science/09`, and can
  carry the SA-construct critique without reifying it.
- **`06` de-risks the HCI-usability seam and the domain-deferral discipline** — proving human
  factors can own the safety-critical interface (alarms, salience, modes, compatibility) while
  deferring digital usability to HCI and the domain systems to their owners, and issuing no
  procedure and no certification.

These gates were **exercised by R1 and ratified by the independent R2 re-review**
(`panels/hf-prototype-r2/`), so the pattern the remaining nine guides inherit is ratified —
exactly as the HCI prototypes (`05`, `08`) did for that module. The Definition of Done the
pattern carries (guide `02`) now includes explicit **closure gates** — ordinary MDLOOM;
truthful metadata / source-custody transition; source-hierarchy/edition & citation-risk
closure; independent adversarial closure; and records/integration closure — so a remaining
guide is *done* only when independently cleared with no unresolved BLOCK/WARN and **no open
citation risk** at sign-off.

## Adopt / Prototype / Defer Decision

- **Adopt now:** the 12-guide problem-first manifest; the ownership/defer matrix; the
  reciprocal HCI↔HF seam; the safety/ethics contract; the bounded-model epistemic stance; the
  two-stage scaling gate (`02`) and review gates (`03`, `06`).
- **Prototype now (this pulse):** guides `02`, `03`, `06` at full peer depth, with truthful
  pre-backfill metadata and focused MDLOOM only.
- **Defer to Pulse 04:** `00-OVERVIEW` + guides `01`, `04`, `05`, `07`, `08`, `09`, `10`,
  `11`; section/nav/`TRACKER` integration; reciprocal pointers into `industrial-design/05`,
  `cognitive-science/09`, and `human-computer-interaction/`; source-corpus backfill; the
  full-module adversarial panel; and any Gold/Da Vinci or legal-content work.

## Gaps & Uncertainties (Pulse-03 carry-forward)

- **Standards/citation precision** — the **load-bearing** standards/dataset claims (NIOSH
  six multipliers + 23 kg; CAESAR ~4,431/~2,400 NA; Wickens MRT focal/ambient; EEMUA 191 4th
  ed. 2024 / ANSI/ISA-18.2-2016 / IEC 62682:2022) were **verified and re-checked in R2**, and
  the guides corrected; the remaining **low-risk precision** figures (score-band cut-points,
  attribution years, the ~8% CVD figure) are spot-checks deferred to Pulse-04 backfill, where
  the Definition-of-Done closure gates require every citation-risk item resolved before a
  guide's sign-off. Guides frame all as dated/bounded.
- **Reciprocal pointers** — whether to add minimal reciprocal cross-references into
  `industrial-design/05`, `cognitive-science/09`, and `human-computer-interaction/` is a
  Pulse-04 decision (no sibling-module edits in this pulse).
- **Placement details** — the exact `sections/` home and `.mkdocs/mkdocs.yml` wiring are
  Pulse-04 integration work.
- **Clinical/organizational overlap** — the `clinical-medicine/11` and `organizational-
  behavior/` boundaries for guides `04`/`05`/`11` are scoped here but authored/verified in
  Pulse 04.
