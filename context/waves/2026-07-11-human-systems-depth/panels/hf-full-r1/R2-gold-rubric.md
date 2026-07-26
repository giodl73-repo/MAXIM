# Human-Factors Full-Module R2 — Gold Rubric Evidence

Date: 2026-07-13
Scope: all 12 numbered guides in `human-factors/` (`00`–`11`)
Reviewer lenses: Gold Rubric v2, reference-editor, expert-skeptic, mechanical PROOF
Decision: **Silver for every guide; no Certified Gold registry insertion**

Disposition: **IN REVIEW pending an independent final re-review.** This rubric scores the module
after the full-module R1 panel (`R1-consolidated.md`) surfaced and repaired a conservative superset
of findings (6 BLOCK + 6 WARN). Because that panel both raised and repaired the findings, the wave is
**not** closed; the tier below is the honest ceiling reachable now, not a final sign-off.

## Claim boundary and mechanical record

This is a guide-specific review, not a cohort score copied across the module. Every guide meets the
content-side threshold used here: average at least 4.5, no dimension below 4, at least three reader
tasks pass, and no unresolved adversarial BLOCK/WARN. That does **not** establish Certified Gold.

- **Ordinary focused PROOF:** PASS — `12 files checked, 0 errors, 0 warnings` (all twelve HF guides),
  recorded in `.proof/last-check.json`. Sibling warnings, if any, are tracked separately.
- **Source-backfill `--validate` (human-factors):** 12/12 round-trip PASS; tables 20; structured
  blocks 81; FLETCH registry 61.
- **Adversarial review:** prototype R1/R2 (`02`,`03`,`06`) and **full-module R1 (all 12 guides)**
  complete; all findings repaired; **independent final re-review pending** (wave IN REVIEW).
- **Da Vinci:** **no HF-specific invariant** exists in `proof.toml` (tolerance = 2,
  `check_col_separators = false`); ordinary PROOF cleanliness must not be represented as Da Vinci
  coverage.
- **Source custody:** `partial` for all twelve. PROOF literal backfill is recorded for 12/12; Git
  provenance is `pending` for 12/12 because `human-factors/` is untracked; authentic external/
  primary-source custody is incomplete.
- **Registry:** **no row** is added to `context/gold/REGISTRY.md`; no Certified Gold or
  Candidate-Hardened claim. **No Gold without pins and custody.**

The strongest honest tier is **Silver**: the guides are editorially strong, adversarially repaired,
and ordinary-PROOF-clean, but lack an HF-specific Da Vinci invariant and complete source custody.

---

## `human-factors/00-OVERVIEW.md`

| Gold dimension | Score | Guide-specific evidence |
|---|---:|---|
| Landscape power | 5 | The fit/load + workload/SA frames and the error/safety spine place all eleven downstream guides on one map. |
| Layering integrity | 5 | The ownership/defer matrix claims each concept once; the HCI↔HF seam and reading order unpack the map in order. |
| ASCII precision | 4 | The discipline-map and seam diagrams are legible and load-bearing, if label-dense. |
| Explanatory compression | 5 | "Organize by the human-factors problem, not the domain" compresses the whole architecture into one rule. |
| Decision utility | 5 | The ownership/defer matrix routes any question to its owning guide and ultimate owner. |
| Confusion handling | 5 | Rejects domain-first HF, overview-as-authority, and treating a label as a verdict. |
| Bridge quality | 4 | The interface-contract / installed-base bridges are universal without making Azure/.NET load-bearing. |
| Cross-reference value | 5 | Now clickable to every sibling owner (`industrial-design/05`, `systems-engineering/06`, `cognitive-science/`, …). |
| Voice | 5 | Peer-level, third-person, explicitly educational; the safety contract is operational, not boilerplate. |
| Factual confidence | 4 | RE-05 aligned the totals it references (239 complete / 240 target); external custody partial. |

**Average: 4.7/5.**

| Reader task | Pass/fail evidence |
|---|---|
| Route a question to its owning guide. | **PASS** — the ownership/defer matrix sends a HEP question to `05`, an alarm question to `06`, a lifting question to `02`/`industrial-design/05`. |
| Apply the HCI↔HF seam to a shared system. | **PASS** — a control-room touchscreen splits interaction/accessibility to HCI and workload/error/alarm to HF, with acceptance to the domain. |
| Hold the safety contract. | **PASS** — the reader refuses a "certify this console" request and defers acceptance to the accountable organization. |

**Adversarial status:** RE-05 (totals) repaired; no finding open. **Ordinary PROOF:** PASS, 0/0.
**Da Vinci:** missing. **Source custody:** partial. **Tier: Silver.**

---

## `human-factors/01-HISTORY-FOUNDATIONS.md`

| Gold dimension | Score | Guide-specific evidence |
|---|---:|---|
| Landscape power | 5 | The four-turn lineage (scientific management → WWII knobs-and-dials → systems/cognitive ergonomics → resilience) is one navigable chain. |
| Layering integrity | 5 | Each turn ties to the guide that owns its modern form; the "why the lineage constrains idioms" thesis holds. |
| ASCII precision | 4 | The lineage ladder is clear; dates are the load-bearing labels. |
| Explanatory compression | 5 | "Idioms outlive their hardware" compresses 75 years into a persistence argument. |
| Decision utility | 4 | The turn→idiom→modern-home mapping answers "why is it like this?" for real conventions. |
| Confusion handling | 5 | Separates invention from popularization and refuses ahistorical shortcuts. |
| Bridge quality | 4 | The backward-compatibility/installed-base bridge is universal to any senior engineer. |
| Cross-reference value | 5 | Now clickable to `cognitive-science/`, `02`, `04`/`05`/`08`. |
| Voice | 5 | Peer-level, historical; the per-guide banner enforces attributed/dated claims. |
| Factual confidence | 5 | RE-06 corrected Leveson to **MIT Press 2011** (paper *Safety Science* 2004); RE-04 added the ≥2-channel note anchored to the design-induced-error turn. |

**Average: 4.7/5.**

| Reader task | Pass/fail evidence |
|---|---|
| Place five milestones on the four turns. | **PASS** — Taylor (1911), Chapanis's landing-gear (WWII), TMI, resilience each map to a turn. |
| Run the average-man collapse. | **PASS** — with `p = 0.30` and independence the multi-dimension "average airman" fraction collapses, shown as dated (Daniels 1952), not universal. |
| Refuse the ahistorical shortcut. | **PASS** — "just automate it" is placed as a Fitts-list (1951) idiom with its critique. |

**Adversarial status:** RE-06 (Leveson date), RE-04 (accessibility note) repaired; no finding open.
**Ordinary PROOF:** PASS, 0/0. **Da Vinci:** missing. **Source custody:** partial. **Tier: Silver.**

---

## `human-factors/02-PHYSICAL-ERGONOMICS-ANTHROPOMETRICS.md`

| Gold dimension | Score | Guide-specific evidence |
|---|---:|---|
| Landscape power | 5 | Body-as-distribution → design-limit logic → load model organizes the whole physical-fit field. |
| Layering integrity | 5 | Percentile/multivariate accommodation, the NIOSH RNLE, and the product↔workplace split with `industrial-design/05` layer cleanly. |
| ASCII precision | 5 | The accommodation and RNLE diagrams carry real formulas and hold PROOF alignment. |
| Explanatory compression | 5 | "Design for a distribution, not the average" compresses the discipline. |
| Decision utility | 5 | The percentile/RNLE/RULA-REBA cheat sheet routes real fit/load questions. |
| Confusion handling | 5 | Rejects the "average person" fallacy and the single-multiplier misread of the RNLE. |
| Bridge quality | 4 | Distribution/tolerance-stack bridges are universal. |
| Cross-reference value | 5 | Now clickable to `industrial-design/05`, `biomedical-engineering/01`, `03`, `statistics-applied/`. |
| Voice | 5 | Peer-level; the scaling-gate prototype carries the module's Definition of Done. |
| Factual confidence | 5 | RE-06 fixed the RNLE load-constant provenance (23 kg **set by the revised 1993 equation**; 1993/1994 primaries already correct); joint-coverage method verified in prototype R2. |

**Average: 4.9/5.**

| Reader task | Pass/fail evidence |
|---|---|
| Compute joint accommodation. | **PASS** — with stature ~ N(170,10) and reach ~ N(75,5) the bivariate-normal joint coverage (ρ = 0.5 → ~0.8245) is derived with an explicit method. |
| Read the load, not just the fit. | **PASS** — the RNLE lift is scored with the six multipliers and reported bounded, not as a pass/fail. |
| Name the validity limits. | **PASS** — the reader flags out-of-domain thermal/coupling assumptions and defers product-form to `industrial-design/05`. |

**Adversarial status:** RE-06 (RNLE wording) repaired; no finding open. **Ordinary PROOF:** PASS, 0/0.
**Da Vinci:** missing. **Source custody:** partial. **Tier: Silver.**

---

## `human-factors/03-COGNITIVE-WORKLOAD-SITUATION-AWARENESS.md`

| Gold dimension | Score | Guide-specific evidence |
|---|---:|---|
| Landscape power | 5 | Workload (supply vs demand) + SA (three levels + measurement) frames operator mental state as measurable-in-context. |
| Layering integrity | 5 | Multiple-resource theory, the workload–performance dissociation, and the SAGAT/SPAM/SART measures with their critiques layer cleanly. |
| ASCII precision | 4 | The resource and SA-measurement diagrams are legible and load-bearing. |
| Explanatory compression | 5 | "Workload and SA are constructs measured by proxy" is the guide's discipline in one line. |
| Decision utility | 5 | The measure→confound→use cheat sheet routes real measurement choices. |
| Confusion handling | 5 | Keeps the SA construct critique without reifying it; separates measurement from mechanism. |
| Bridge quality | 4 | Supply/demand and signal/noise bridges are universal. |
| Cross-reference value | 5 | Now clickable to `cognitive-science/09-APPLIED-BRIDGE`, `human-computer-interaction/`, `statistics-applied/`. |
| Voice | 5 | Peer-level; per-guide banner enforces proxy/validity discipline. |
| Factual confidence | 5 | RE-04 added the ≥2-channel note anchored to SA-cue perceivability; mechanism kept deferred. |

**Average: 4.8/5.**

| Reader task | Pass/fail evidence |
|---|---|
| Read the workload–performance dissociation. | **PASS** — flat performance with rising workload is read as reduced reserve, not "fine." |
| Choose an SA measure and its confound. | **PASS** — SAGAT freeze vs SPAM latency chosen with the intrusiveness/validity trade named. |
| Hold the mechanism boundary. | **PASS** — "why attention tunnels" routes to `cognitive-science/`; the guide owns measurement-in-context. |

**Adversarial status:** RE-04 (accessibility note) repaired; no finding open. **Ordinary PROOF:** PASS,
0/0. **Da Vinci:** missing. **Source custody:** partial. **Tier: Silver.**

---

## `human-factors/04-HUMAN-ERROR-TAXONOMIES.md`

| Gold dimension | Score | Guide-specific evidence |
|---|---:|---|
| Landscape power | 5 | Reason's GEMS × Rasmussen's SRK generates the whole taxonomy on one grid. |
| Layering integrity | 5 | Slips/lapses/mistakes/violations, latent conditions, and error-as-systems-property layer cleanly. |
| ASCII precision | 5 | The SRK×GEMS matrix is legible and (after the RE-06 trim) whitespace-clean. |
| Explanatory compression | 5 | "Each cell implies a different fix" compresses classification into action. |
| Decision utility | 5 | The level→fix-family cheat sheet routes each error class to its remedy. |
| Confusion handling | 5 | Rejects the person-model / blame reflex and the outcome-severity relabel. |
| Bridge quality | 4 | The exception-vs-bug and defense-in-depth bridges are universal. |
| Cross-reference value | 5 | Now clickable to `cognitive-science/`, `clinical-medicine/11`, `05`, `systems-engineering/06`. |
| Voice | 5 | Peer-level; the per-guide banner keeps error a systems property. |
| Factual confidence | 5 | Reason/Rasmussen attributions dated; ≥2-channel note already present; diagram trailing whitespace fixed (RE-06). |

**Average: 4.9/5.**

| Reader task | Pass/fail evidence |
|---|---|
| Classify and prescribe. | **PASS** — events E1–E4 get an SRK level, a GEMS class, and a fix family. |
| Reframe person → system. | **PASS** — "who opened the wrong valve" becomes "what made the wrong valve easy to open." |
| Hand off the rest. | **PASS** — recurrence probability routes to `05`; barrier value to `08`; no blame/legal verdict. |

**Adversarial status:** RE-06 (whitespace) repaired; no finding open. **Ordinary PROOF:** PASS, 0/0.
**Da Vinci:** missing. **Source custody:** partial. **Tier: Silver.**

---

## `human-factors/05-HUMAN-RELIABILITY-ANALYSIS.md`

| Gold dimension | Score | Guide-specific evidence |
|---|---:|---|
| Landscape power | 5 | The HRA pipeline (nominal → PSFs → dependency → bounded HEP → tree) frames the whole field. |
| Layering integrity | 5 | THERP/HEART/SPAR-H/CREAM, PSFs, dependency, and uncertainty layer cleanly onto the pipeline. |
| ASCII precision | 5 | The SPAR-H excerpt and the range box carry correct formulas and hold PROOF alignment. |
| Explanatory compression | 5 | "A HEP is a model output, not a measurement" is the whole epistemic point. |
| Decision utility | 5 | The method-selection and "give central + EF + method + PSFs" cheat rows route real HRA choices. |
| Confusion handling | 5 | Rejects the point-HEP, the independence fallacy, and (now) the naive EF band. |
| Bridge quality | 4 | The basic-event / reliability-block bridges are universal. |
| Cross-reference value | 5 | Now clickable to `systems-engineering/06`, `statistics-applied/`, `cognitive-science/`, `clinical-medicine/11`. |
| Voice | 5 | Peer-level; the banner frames every HEP as a wide, dated, method-bounded interval. |
| Factual confidence | 5 | ES-01 fixed the EF convention, the bounded-probability ceiling, and the ≥3-negative-PSF trigger; RE-04 added the ≥2-channel PSF note. |

**Average: 4.9/5.**

| Reader task | Pass/fail evidence |
|---|---|
| Compute a SPAR-H HEP and its adjustment. | **PASS** — three negative PSFs trigger the adjustment; `0.01×40/(0.01×39+1) ≈ 0.288`, and the ≥3-negative-PSF trigger is stated. |
| Report it as a bounded range. | **PASS** — `median/EF = 0.06`; `median×EF = 1.45` is shown inadmissible; a truncated/logit-normal gives ~0.8; a bare "0.06–0.9 from EF=5" is named misleading. |
| Find the dominant PSF. | **PASS** — the time sweep (×10 → ×1 → ×0.1) shows the adjustment dropping out below three negative PSFs (0.288 → 0.04 → 0.004). |

**Adversarial status:** ES-01 (EF/ceiling/trigger), RE-04 (accessibility) repaired; no finding open.
**Ordinary PROOF:** PASS, 0/0. **Da Vinci:** missing. **Source custody:** partial. **Tier: Silver.**

---

## `human-factors/06-DISPLAY-CONTROL-INTERFACE-DESIGN.md`

| Gold dimension | Score | Guide-specific evidence |
|---|---:|---|
| Landscape power | 5 | Compatibility → coding/redundancy → alarm philosophy → mode visibility → EID → layout organizes the safety-critical UI. |
| Layering integrity | 5 | Each layer drills one element and holds the HCI-usability seam and domain-system deferrals. |
| ASCII precision | 5 | The alarm-metric and EID diagrams carry a traceable event inventory and hold PROOF alignment. |
| Explanatory compression | 5 | "Never one channel" compresses redundant coding into a safety rule. |
| Decision utility | 5 | The compatibility/alarm/mode cheat sheet routes real interface choices. |
| Confusion handling | 5 | Separates population stereotypes (with cultural caveats) from universal constants. |
| Bridge quality | 4 | The API-affordance and mode-as-state bridges are universal. |
| Cross-reference value | 5 | Now clickable to `human-computer-interaction/08`, `nuclear/05`, `aeronautics/04`, `biomedical-engineering/07`, `transportation/07`, `industrial-design/05`. |
| Voice | 5 | Peer-level; review-gated prototype; banner keeps stereotypes dated/bounded. |
| Factual confidence | 5 | Owns the ≥2-channel invariant the other guides cite; alarm standards (EEMUA 191/ISA-18.2/IEC 62682) dated in prototype R2. |

**Average: 4.9/5.**

| Reader task | Pass/fail evidence |
|---|---|
| Fix compatibility and stereotypes first. | **PASS** — valve layout and movement stereotypes are corrected with cultural caveats. |
| Code redundantly. | **PASS** — "open/closed" and "within/over limit" each ride on ≥2 channels; a single failed channel does not hide state. |
| Attack the alarm flood. | **PASS** — rationalize/prioritize rather than add a master alarm; alarms separated from notifications. |

**Adversarial status:** no full-module finding open (owns the ≥2-channel invariant). **Ordinary
PROOF:** PASS, 0/0. **Da Vinci:** missing. **Source custody:** partial. **Tier: Silver.**

---

## `human-factors/07-AUTOMATION-HUMAN-MACHINE.md`

| Gold dimension | Score | Guide-specific evidence |
|---|---:|---|
| Landscape power | 5 | Levels/types × the ironies frames automation as a trade, not a subtraction. |
| Layering integrity | 5 | The stage×level grid, the ironies, trust/bias, OOTL, and function allocation layer cleanly. |
| ASCII precision | 5 | The redesigned allocation model and sweep carry correct arithmetic and hold PROOF alignment. |
| Explanatory compression | 5 | "Automation is a trade with a named cost" is the whole guide. |
| Decision utility | 5 | The cheat sheet routes "how much to automate" to a per-stage level and the irony tax. |
| Confusion handling | 5 | Refuses "higher is safer"; separates LOA from SAE J3016. |
| Bridge quality | 4 | The supervision/monitoring bridges are universal. |
| Cross-reference value | 5 | Now clickable to `aeronautics/04`, `transportation/07`, `nuclear/05`, `cognitive-science/`, `06`, `08`. |
| Voice | 5 | Peer-level; banner frames each level as a trade with a named cost. |
| Factual confidence | 5 | ES-02 redesigned the model (common off-normal `p` + level-specific `C(L)`; L1 no takeover term; optimum slides, no winner); Bainbridge/PSW dated. |

**Average: 4.9/5.**

| Reader task | Pass/fail evidence |
|---|---|
| Place a design in the stage×level grid. | **PASS** — the four PSW stages get a level and the SA-costliest stage is named. |
| Compute the LOA trade. | **PASS** — `E(L)=(1−p)W(L)+p·C(L)` with `W=[8,5,3,1]`, `C=[3,12,30,60]` gives the optimum sliding L4→L2 as `p` grows, and L1 carries no takeover term. |
| Refuse "higher is safer." | **PASS** — "just go full autonomy" is answered with the irony tax and deferred acceptance. |

**Adversarial status:** ES-02 (model/L1) repaired; no finding open. **Ordinary PROOF:** PASS, 0/0.
**Da Vinci:** missing. **Source custody:** partial. **Tier: Silver.**

---

## `human-factors/08-SAFETY-SYSTEMS-AND-HAZARD-ANALYSIS.md`

| Gold dimension | Score | Guide-specific evidence |
|---|---:|---|
| Landscape power | 5 | Two views of failure (barrier + control) frame every method as one lens or the other. |
| Layering integrity | 5 | Barriers, HAZOP-for-humans, human-inclusive FMEA, bow-tie, STAMP/STPA layer cleanly. |
| ASCII precision | 5 | The bow-tie and common-cause decomposition carry correct arithmetic and hold PROOF alignment. |
| Explanatory compression | 5 | "Every barrier is a fallible hypothesis" is the guide's discipline. |
| Decision utility | 5 | The method cheat sheet routes hazard-ID / triage / control-rich choices. |
| Confusion handling | 5 | Now rejects reading barrier strength off the category, and the independence assumption. |
| Bridge quality | 4 | The defense-in-depth and control-loop bridges are universal. |
| Cross-reference value | 5 | Now clickable to `systems-engineering/06`, `nuclear/05`, `aeronautics/04`, `transportation/07`, `biomedical-engineering/07`, `statistics-applied/`. |
| Voice | 5 | Peer-level; banner keeps a clean analysis "evidence of diligence, not proof of safety." |
| Factual confidence | 5 | ES-05 fixed the barrier-ranking overclaim, the dust barrier advice (→ MoC/hazard review), and made the common-cause decomposition explicit; ES-01a aligned the shared HEP range; Leveson → 2011. |

**Average: 4.9/5.**

| Reader task | Pass/fail evidence |
|---|---|
| Order barriers by type (not universal strength). | **PASS** — interlock/alarm/rule are classified by type, with reliability assessed in context, and detection-dependent barriers ride ≥2 channels. |
| Quantify a bow-tie branch and its range. | **PASS** — `0.1×0.01×0.29 = 2.9e-4/yr`; bounded HEP `~0.06–0.8` gives `~6e-5–8e-4/yr`; the common-cause term (0.005) dominates. |
| Catch the independence error. | **PASS** — a shared sensor makes "two barriers" closer to one; the decomposition splits shared vs independent parts. |

**Adversarial status:** ES-05, ES-01a, RE-06 (Leveson) repaired; no finding open. **Ordinary PROOF:**
PASS, 0/0. **Da Vinci:** missing. **Source custody:** partial. **Tier: Silver.**

---

## `human-factors/09-DOMAIN-APPLICATIONS.md`

| Gold dimension | Score | Guide-specific evidence |
|---|---:|---|
| Landscape power | 5 | The model×domain grid makes the apply-and-defer thesis visible in one picture. |
| Layering integrity | 5 | Aviation/healthcare/process/rail/maritime/road each apply the models and defer the systems. |
| ASCII precision | 5 | The grid and the two-domain alarm read carry correct arithmetic and hold PROOF alignment. |
| Explanatory compression | 5 | "One toolkit, many domains" compresses the guide's reason to exist. |
| Decision utility | 5 | The apply-model / defer-system cheat sheet routes each domain problem to owner. |
| Confusion handling | 5 | Now offers candidate mechanisms and evidence questions, not prescriptions. |
| Bridge quality | 4 | The portable-mechanism bridge (CRM as team-SA) is universal. |
| Cross-reference value | 5 | Now clickable to `aeronautics/04`, `clinical-medicine/11`, `biomedical-engineering/07`, `nuclear/05`, `transportation/`. |
| Voice | 5 | Peer-level; banner keeps every domain example an illustration, not a procedure. |
| Factual confidence | 5 | ES-04 removed the "same fix"/checklist/handoff/second-check prescriptions; RE-04 added the cross-domain ≥2-channel note; WHO/CRM dated. |

**Average: 4.9/5.**

| Reader task | Pass/fail evidence |
|---|---|
| Read the grid two ways. | **PASS** — the healthcare column and the mode-confusion row each name the model and the deferred system owner. |
| Apply one model across two domains. | **PASS** — the ICU and control-room alarm inventories share a candidate mechanism; the *fix* is deferred to the domain owner. |
| Port an intervention without re-teaching. | **PASS** — "port CRM to ferries" becomes "port the team-SA mechanism and verify," deferring systems and acceptance. |

**Adversarial status:** ES-04 (prescriptions), RE-04 (accessibility) repaired; no finding open.
**Ordinary PROOF:** PASS, 0/0. **Da Vinci:** missing. **Source custody:** partial. **Tier: Silver.**

---

## `human-factors/10-METHODS-AND-MEASUREMENT.md`

| Gold dimension | Score | Guide-specific evidence |
|---|---:|---|
| Landscape power | 5 | The question→bounded-evidence pipeline frames the whole methods field and its two break points. |
| Layering integrity | 5 | Task analysis, observation, instrumentation, simulation, and use-error study layer onto the pipeline. |
| ASCII precision | 5 | The crossed-factor frame and coverage boxes carry correct arithmetic and hold PROOF alignment. |
| Explanatory compression | 5 | "Coverage is the difference between evidence and a convenient anecdote" is the discipline. |
| Decision utility | 5 | The method cheat sheet routes decompose/observe/simulate/use-error choices. |
| Confusion handling | 5 | Now separates orthogonal crossed factors from overlapping strata, and coverage from power. |
| Bridge quality | 4 | The test-coverage / sampling-frame bridges are universal. |
| Cross-reference value | 5 | Now clickable to `statistics-applied/`, `cognitive-science/`, `human-computer-interaction/06`. |
| Voice | 5 | Peer-level; banner frames every measure as a proxy with a validity domain. |
| Factual confidence | 5 | ES-03 replaced the overlapping 12-cell strata with orthogonal E×P×T×C = 16 cells (convenience 1/16 ≈ 6%); RE-04 added the measurement-side ≥2-channel note. |

**Average: 4.9/5.**

| Reader task | Pass/fail evidence |
|---|---|
| Pick HTA vs CTA. | **PASS** — layout-by-movement routes to HTA; novel-fault diagnosis to CTA/CDM. |
| Compute coverage and name the gap. | **PASS** — the convenience sample touches 1 of 16 crossed cells (~6%); the uncovered novice/tail/critical/night cells are named. |
| Separate coverage from power. | **PASS** — "did we touch the critical cells?" (here) vs "is n-per-cell enough?" (`statistics-applied/`). |

**Adversarial status:** ES-03 (crossed factors), RE-04 (accessibility) repaired; no finding open.
**Ordinary PROOF:** PASS, 0/0. **Da Vinci:** missing. **Source custody:** partial. **Tier: Silver.**

---

## `human-factors/11-ORGANIZATIONAL-SAFETY-CULTURE.md`

| Gold dimension | Score | Guide-specific evidence |
|---|---:|---|
| Landscape power | 5 | HRO + just culture + Safety-II + normalization-of-deviance frame the sustaining layer. |
| Layering integrity | 5 | Each idea drills one mechanism and ties to the barrier/error guides it sustains. |
| ASCII precision | 5 | The metric-reading and leading/lagging boxes carry correct readings and hold PROOF alignment. |
| Explanatory compression | 5 | "Safety culture is not a single number" is the guide's discipline. |
| Decision utility | 5 | The cheat sheet routes score/rank temptations to a triangulated basket. |
| Confusion handling | 5 | Now treats reporting-rate as indeterminate without triangulation; separates personal vs process safety. |
| Bridge quality | 4 | The Goodhart / metric-gaming bridge is universal. |
| Cross-reference value | 5 | Now clickable to `clinical-medicine/11`, `statistics-applied/`. |
| Voice | 5 | Peer-level; banner keeps culture "not one score." |
| Factual confidence | 5 | RE-01 made the reporting-rate comparison indeterminate-without-triangulation and listed the additional evidence; ≥2-channel reporting note already present. |

**Average: 4.9/5.**

| Reader task | Pass/fail evidence |
|---|---|
| Read the reporting rate as indeterminate. | **PASS** — A (120) vs B (18) is indeterminate; the reader lists exposure/definitions/severity/near-miss/climate/audit before concluding. |
| Separate personal from process safety. | **PASS** — a flat low injury rate is shown to coexist with rising major-accident risk. |
| Catch Goodhart. | **PASS** — "reduce reported incidents" as a target erodes learning; a basket of indicators resists gaming. |

**Adversarial status:** RE-01 (triangulation) repaired; no finding open. **Ordinary PROOF:** PASS,
0/0. **Da Vinci:** missing. **Source custody:** partial. **Tier: Silver.**

---

## Module tier summary

| Guide | Average | Adversarial | PROOF | Da Vinci | Custody | Tier |
|---|---:|---|---|---|---|---|
| `00` | 4.7 | clear | 0/0 | missing | partial | Silver |
| `01` | 4.7 | clear | 0/0 | missing | partial | Silver |
| `02` | 4.9 | clear | 0/0 | missing | partial | Silver |
| `03` | 4.8 | clear | 0/0 | missing | partial | Silver |
| `04` | 4.9 | clear | 0/0 | missing | partial | Silver |
| `05` | 4.9 | clear | 0/0 | missing | partial | Silver |
| `06` | 4.9 | clear | 0/0 | missing | partial | Silver |
| `07` | 4.9 | clear | 0/0 | missing | partial | Silver |
| `08` | 4.9 | clear | 0/0 | missing | partial | Silver |
| `09` | 4.9 | clear | 0/0 | missing | partial | Silver |
| `10` | 4.9 | clear | 0/0 | missing | partial | Silver |
| `11` | 4.9 | clear | 0/0 | missing | partial | Silver |

**Tier: Silver for all 12 guides. No Certified Gold. No `context/gold` registry insertion. No Gold
without an HF-specific Da Vinci invariant and complete source-custody pins.** Wave disposition:
**IN REVIEW pending an independent final re-review** of the full-module R1 repairs.
