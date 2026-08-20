# human-factors/ — Status

**12 of 12 guides authored · Module COMPLETE & WIRED · WAVE IN REVIEW (full-module adversarial panel conducted — 6 BLOCK + 6 WARN repaired; independent final re-review pending) · Pulse 04 (Human factors authoring & review) — authoring/integration/backfill + full-module R1/R2 panel done**

> The three gate-passed prototypes — `02-PHYSICAL-ERGONOMICS-ANTHROPOMETRICS` (the
> **scaling-gate** prototype), `03-COGNITIVE-WORKLOAD-SITUATION-AWARENESS`, and
> `06-DISPLAY-CONTROL-INTERFACE-DESIGN` (both **review-gated** prototypes) — de-risked
> the module's three hardest boundaries in Pulse 03. **Pulse 04** then authored the
> remaining nine guides on the ratified pattern — `00-OVERVIEW`, `01`, `04`, `05`, `07`,
> `08`, `09`, `10`, `11` — each satisfying its per-guide Definition of Done (the eight
> content gates) and the common safety & accessibility contract carried by guide `02`.
> The module is now **wired** into `sections/technology.md`, `.mkdocs/mkdocs.yml`, and
> `TRACKER.md`; **minimal reciprocal pointers** were added to the six boundary siblings
> (`industrial-design/05`, `human-computer-interaction/`, `cognitive-science/09`,
> `clinical-medicine/11`, `systems-engineering/06`, `biomedical-engineering/07`); and
> **source-corpus backfill** ran for `human-factors` and every changed sibling, so all
> twelve guides graduate to `status: source-custody` / `source_custody: partial` with
> `proof-backfill` backsources. The **full-module adversarial panel** (independent R2
> closure per DoD gate 12) has now been **conducted** — `panels/hf-full-r1/` surfaced a
> conservative **6 BLOCK + 6 WARN** superset, all **repaired** in the guides and records, and
> `R2-gold-rubric.md` scores every guide **Silver** with **no registry row**. Because that panel
> both raised and repaired the findings, an **independent final re-review is still pending** —
> hence **WAVE IN REVIEW**, not closed. **No** Gold/Da Vinci tier and **no** `context/gold`
> registry row are claimed.

## Scope in one line

`human-factors/` owns, at quantitative-systems depth, the **performance, safety, and
limits of humans operating complex systems**: physical ergonomics/anthropometrics,
cognitive workload and situation awareness, human-error taxonomies, human-reliability
analysis, safety-critical display/control/control-room design, automation and
human–machine function allocation, safety-systems and hazard analysis, domain
applications, methods/measurement, and organizational safety culture. It is the
operator-and-safety layer of MAXIM's engineering verticals. It is an **educational
systems reference**, not operational, certification, legal, or clinical advice.

## Guide Manifest (12 guides: 00 + 11)

| # | File | Uniquely owns (at peer depth) | Status |
|---|---|---|---|
| 00 | `00-OVERVIEW.md` | Discipline map; the fit/load and workload/SA frames; ownership/defer matrix; HCI↔HF seam; safety/ethics contract; reading order | ✅ authored (Pulse 04) |
| 01 | `01-HISTORY-FOUNDATIONS.md` | HF intellectual roots (scientific management → WWII "knobs-and-dials"/aviation psychology → Fitts/Chapanis → systems ergonomics → resilience engineering) and why the lineage constrains current idioms | ✅ authored (Pulse 04) |
| 02 | `02-PHYSICAL-ERGONOMICS-ANTHROPOMETRICS.md` | Population distributions/percentile & multivariate accommodation; clearance/reach/strength design-limit logic; occupational biomechanics; NIOSH lifting equation as a bounded model; posture indices; work–rest/environment; population MSD-risk; the product↔workplace boundary vs `industrial-design/05` | ✅ authored (**scaling-gate prototype**) |
| 03 | `03-COGNITIVE-WORKLOAD-SITUATION-AWARENESS.md` | Workload (multiple-resource theory, the performance dissociation, NASA-TLX raw/weighted + limits, physiological/performance measures), vigilance decrement, SA levels/measurement (SAGAT/SPAM/SART) **and the construct critiques**, attentional tunneling, team/distributed SA — measurement-in-context, mechanism deferred to `cognitive-science/` | ✅ authored (**prototype, review-gated**) |
| 04 | `04-HUMAN-ERROR-TAXONOMIES.md` | Slips/lapses/mistakes (Reason), skill/rule/knowledge errors, violations, latent conditions, error as a systems property (not blame) | ✅ authored (Pulse 04) |
| 05 | `05-HUMAN-RELIABILITY-ANALYSIS.md` | HRA methods (THERP, HEART, SPAR-H, CREAM), human-error-probability as a bounded estimate, performance-shaping factors; borrows FTA/reliability math from `systems-engineering/06` | ✅ authored (Pulse 04) |
| 06 | `06-DISPLAY-CONTROL-INTERFACE-DESIGN.md` | Display/control compatibility & population stereotypes (with cultural caveats), coding/redundancy, alarm philosophy, salience vs nuisance, mode/state visibility, ecological interface design, control-room layout; the safety-critical-UI ↔ HCI seam; domain systems deferred | ✅ authored (**prototype, review-gated**) |
| 07 | `07-AUTOMATION-HUMAN-MACHINE.md` | Levels of automation (Sheridan; Parasuraman–Sheridan–Wickens), the ironies of automation (Bainbridge), trust/complacency/automation bias, out-of-the-loop, function allocation, human–autonomy teaming; domain autopilots deferred | ✅ authored (Pulse 04) |
| 08 | `08-SAFETY-SYSTEMS-AND-HAZARD-ANALYSIS.md` | Barrier/defense-in-depth models, HAZOP/what-if, human-inclusive FMEA, bow-tie, STAMP/STPA, safety-case reasoning as concept; borrows FTA/FMEA from `systems-engineering/06`; no certification | ✅ authored (Pulse 04) |
| 09 | `09-DOMAIN-APPLICATIONS.md` | Aviation/healthcare/process/rail/maritime/road applications that **apply** the models and **defer** domain systems to their owners | ✅ authored (Pulse 04) |
| 10 | `10-METHODS-AND-MEASUREMENT.md` | Task analysis (HTA, cognitive task analysis), observation, simulation, physiological-measurement instrumentation, usability-for-safety; inferential statistics deferred to `statistics-applied/` | ✅ authored (Pulse 04) |
| 11 | `11-ORGANIZATIONAL-SAFETY-CULTURE.md` | Safety culture/climate, high-reliability organizations, just culture, Safety-I vs Safety-II/resilience engineering, reporting systems, normalization of deviance | ✅ authored (Pulse 04) |

## Boundary Contracts

| Defers to | For |
|---|---|
| `industrial-design/05-ERGONOMICS` | Compact **product-form** ergonomics: handles, seats, knobs, affordances, the Norman action model, the seven universal-design principles (remains MAXIM's product-form entry) |
| `cognitive-science/` (esp. `09-APPLIED-BRIDGE`) | Cognitive **mechanisms**, the psychophysical laws (Fitts/Hick/Miller/GOMS), and Endsley-SA / NDM as **cognitive theory** |
| `human-computer-interaction/` | General **digital-interface** usability, interaction design, information architecture/visualization, and interactive-accessibility evaluation |
| `statistics-applied/` | Inferential statistics, sampling, and power behind any HF study |
| `systems-engineering/06-FMEA-RELIABILITY` | FMEA/FTA machinery and reliability **mathematics/hardware** (HF adds the human-reliability extension) |
| `biomedical-engineering/01-BIOMECHANICS`, `/07-MEDICAL-DEVICES` | Tissue/joint/gait biomechanics as an engineering science; medical-device engineering and regulation |
| `clinical-medicine/` (esp. `11-SAFETY-QUALITY-AND-WORKFLOW`) | Clinical diagnosis/treatment/rehabilitation; **clinical** patient-safety practice |
| `nuclear/05`, `aeronautics/04`, `transportation/07` | The domain **systems** themselves (reactor safety systems, avionics/FMS, vehicle autonomy) |
| `law/` | Legal obligation, liability, and compliance duties |
| `organizational-behavior/` | General organizational theory beyond safety culture |

## HCI ↔ Human Factors Seam (reciprocal to `human-computer-interaction/STATUS.md`)

- **HCI owns** interactive digital-interface design, usability, interactive
  accessibility, and evaluation.
- **Human factors owns** operator performance, physical/cognitive workload,
  human-error taxonomy, safety-critical integration, and performance under stress or
  fatigue.
- At shared systems (clinical-device, avionics, control-room touchscreens): HCI owns
  interaction design and usability/accessibility evaluation; human factors owns
  workload/SA support, error-consequence, alarm philosophy, mode visibility, and safety
  analysis. Domain systems defer to `nuclear/`, `aeronautics/`, `transportation/`, and
  `biomedical-engineering/`; legal obligation defers to `law/`.
- **Evidence vs acceptance (safety-critical systems remain HCI systems).** A safety-critical
  console is still an HCI system, not a lesser or "non-user" one. The MAXIM modules own
  **methods and evidence, not sign-off**: `human-computer-interaction/` supplies the
  interaction/visualization/accessibility **methods/evidence**; human factors supplies the
  **workload/error and performance-under-stress evidence** (and the safety requirements it
  can state); and **acceptance and implementation belong to the accountable domain
  organization and its regulator**, not to any reference module — no module signs off or
  vetoes a real system. This is recorded in guides `02` (§8) and `06` (§9) and in the
  architecture record.

## Safety / Ethics Contract

1. **Educational systems reference** — no operational instructions (no lifting how-to, no
   operating procedures, no runnable operations).
2. **No certification or compliance ruling** — nothing here declares a task, operator, or
   system "safe," "compliant," or "passing."
3. **No accident or legal determination** — event causation belongs to the module's
   error/hazard methods (guides `04`/`08`), not to labels like "loss of SA."
4. **No individual fitness-for-duty or clinical assessment** — screening models are
   population-level estimates, never a medical judgment about a person.
5. **Named models, standards, and stereotypes are attributed, dated, and bounded** — the
   NIOSH equation, RULA/REBA, NASA-TLX, SAGAT, EEMUA 191/ISA-18.2, and population
   stereotypes are context, with an explicit validity domain, not universal constants.

## Placement (WIRED)

Home: **Technology (Ray 7)** engineering vertical, adjacent to `systems-engineering/`
and `biomedical-engineering/`, with strong seams to `human-computer-interaction/`
(Computing & Software), `cognitive-science/` (Life Sciences), and `industrial-design/`
(Arts & Culture). As of **Pulse 04** the module is **wired** into `sections/technology.md`
(Directories table, landscape SYSTEMS-ENGINEERING track, count, volume plan, adjacent-section
bridge), `.mkdocs/mkdocs.yml` (Technology nav entry), and `TRACKER.md` (Summary Dashboard row
+ totals). **Minimal reciprocal pointers** were added to the six boundary siblings —
`industrial-design/05-ERGONOMICS`, `human-computer-interaction/` (overview + STATUS seam),
`cognitive-science/09-APPLIED-BRIDGE`, `clinical-medicine/11-SAFETY-QUALITY-AND-WORKFLOW`,
`systems-engineering/06-FMEA-RELIABILITY`, and `biomedical-engineering/07-MEDICAL-DEVICES` —
and **source-corpus backfill** (`--validate`) ran for `human-factors` and every changed
sibling, so all twelve guides carry real `proof-backfill` backsources. Home is now live.

## Pulse 04 status — authoring/integration/backfill + full-module R1/R2 panel DONE · WAVE IN REVIEW (final re-review pending)

The remaining nine guides — `00-OVERVIEW`, `01`, `04`, `05`, `07`, `08`, `09`, `10`, `11` —
are authored at full peer depth on the ratified (Pulse-03) prototype pattern. Each satisfies
its **per-guide Definition of Done** (the eight content gates: required formal model(s) named
and dated; a reproducible synthetic quantitative demonstration; uncertainty/validity/bias
analysis; source-hierarchy/edition attribution; an explicit boundary test; a conceptual
terminal-readable diagram; a fully worked fictional case; 3–5 calculation/interpretation reader
tasks) and the **common safety & accessibility contract** (no operational instruction /
certification / accident-or-legal ruling / individual fitness assessment; accessibility as a
≥2-channel safety requirement; the evidence-vs-acceptance seam). The whole module passes
**focused PROOF (12 files checked, 0 errors, 0 warnings)** with the module's `proof.toml`
(tolerance = 2, `check_col_separators = false`), integration and reciprocal pointers are
landed, and the source-corpus backfill is regenerated and validated. The **independent full-module
adversarial panel (DoD closure gate 12)** has now been **conducted** — `panels/hf-full-r1/`
(expert-skeptic, reference-editor, consolidated) surfaced a conservative **6 BLOCK + 6 WARN**
superset (guide `05` HRA error-factor/bounded-probability/SPAR-H-trigger; guide `07` automation
model + L1 takeover; guide `10` overlapping coverage strata; guide `09` domain prescriptions; guide
`11` reporting-without-triangulation; records/citations; guide `08` barrier-ranking + dust advice;
cross-references; accessibility reach; totals; Leveson/RNLE/whitespace; PROOF-artifact truth), **all
repaired** in the guides and records, and `R2-gold-rubric.md` scores every guide **Silver** with
**no registry row**. The citation/edition items (gates 4/11) are closed against authoritative sources
and recorded. **Remaining before the pulse closes:** because the panel both raised and repaired the
findings, an **independent final re-review** is still required (the last DoD closure step), so the
wave is **IN REVIEW**, not DONE. No Gold/Da Vinci tier, no registry row.

## Pulse 03 status — DONE (prototype pattern/gate ratified)

The architecture is recorded
(`context/waves/2026-07-11-human-systems-depth/artifacts/HUMAN-FACTORS-ARCHITECTURE.md`,
findings **MAXIM-HF-01 … MAXIM-HF-20** + G00 … G11), the 12-guide manifest is fixed, and
the ownership/defer matrix, HCI↔HF seam, and safety/ethics contract are recorded. The three
prototype guides are authored at full peer depth and pass focused PROOF (**3 files checked,
0 errors, 0 warnings**). The **two-stage scaling gate** for guide `02` and the **review
gates** for guides `03`/`06` are now **ratified**: the R1 boundary-gate panel
(`panels/hf-prototype-r1/`) found and drove repair of the conservative-prototype findings,
and an **independent strict re-review (R2)** (`panels/hf-prototype-r2/`) — which neither
authored nor repaired those findings — re-derived the quantitative passes, re-checked the
standards, and confirmed the safety-contract/seam/record repairs, closing its finer-grained
findings with **no unresolved BLOCK/WARN**. Load-bearing standards were **verified**
(CAESAR ~4,431 total / ~2,400 North America; the NIOSH revised equation's **six**
multipliers plus the 23 kg load constant; Wickens MRT's four dimensions incl. the
focal/ambient visual channel; EEMUA 191 4th ed. 2024; ANSI/ISA-18.2-2016; IEC 62682:2022),
and the R2 corrections landed (rho=0.5 joint coverage ~0.8245 with an explicit
bivariate-normal method; RNLE coupling CM=1.00 for the stated V>=75 cm / fair coupling with
an explicit FM frequency/duration and the out-of-domain hot comparison removed; the guide-03
worked pass framed as one representative participant with common weighting and the
mis-counted "four families" fixed; guide-06 alarm metrics given a traceable event inventory
with alarms separated from informational notifications).
Hence **DONE**. No module integration, no source backfill, and no edits to sibling
modules were made; metadata stays truthful (`status: prototype`, `source_custody:
needs-source`, `backsource_ids: []`). Pulse 04 is now unblocked; Gold/Da Vinci promotion
remains future scope.

## Prototype & gate design

- **`02` — two-stage scaling gate.** Stage 1 (quantitative-model gate): the percentile/
  multivariate-accommodation math, the design-limit logic, and the NIOSH lifting model
  are correct, dated, attributed, and bounded, with the validity domain explicit. Stage 2
  (boundary gate): the product↔workplace split with `industrial-design/05` is clean and
  non-duplicating, and the guide carries the module-wide **Guide-Family Scaling
  Contracts** the other eleven guides inherit.
- **`03` / `06` — review gates.** `03` must keep cognitive **mechanism** deferred to
  `cognitive-science/` while owning operator-in-context **measurement/design**, and must
  carry the SA-construct critique without reifying it. `06` must hold the **HCI-usability
  seam** and the **domain-system deferrals** (nuclear/aero/medical/transport) while
  issuing **no procedure and no certification**. Each prototype records its gate as a
  "Prototype Seam Contract" section.

- **Gate status — ratified (R1 + independent R2).** The scaling gate (`02`) and the review
  gates (`03`/`06`) were **exercised** by the R1 boundary-gate panel
  (`panels/hf-prototype-r1/`), which found and drove repair of the conservative-prototype
  findings (B1 factual/model, B2 quantitative worked cases, B3 safety contract, B4 HCI↔HF
  seam, B5 scaling contracts, B6 records). Because R1 both raised and repaired those
  findings, it could not self-ratify; an **independent strict R2 re-review**
  (`panels/hf-prototype-r2/`) then closed the remaining finer-grained findings (joint-coverage
  method, RNLE CM/FM correctness + hot-environment removal, guide-03 participant framing,
  guide-06 alarm-vs-notification separation, evidence-vs-acceptance seam, and the
  Definition-of-Done closure gates) with **no unresolved BLOCK/WARN**, so the pattern/gate is
  now **ratified**. Pulse 04 (author the remaining nine guides, integrate, backfill,
  full-module panel) is unblocked; Gold/Da Vinci remains future scope.

Gold/Da Vinci certification and legal-content expansion remain future scope and are not a
Pulse 03 gate.
