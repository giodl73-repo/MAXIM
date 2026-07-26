# HCI Full-Module R2 — Gold Rubric Evidence

Date: 2026-07-12
Scope: all 12 numbered guides in `human-computer-interaction/` (plus the two reciprocal-pointer
siblings `cognitive-science/09-APPLIED-BRIDGE` and `industrial-design/06-INTERACTION-DESIGN`,
validated but not tier-scored here)
Reviewer lenses: Gold Rubric v2, reference-editor, expert-skeptic, mechanical proof
Decision: **Silver for every guide; no Certified Gold registry insertion**

Final sign-off: **PASS — Pulse 02 DONE.** This rubric preserves the Silver tier decision after the
conservative full-module findings were repaired. The final reviewer subsequently verified all
content and record repairs; the module is marked ✅ with no unresolved BLOCK/WARN.

## Claim Boundary and Mechanical Record

This is a guide-specific review, not a cohort score copied across the module. Every guide meets the
content-side threshold used here: average at least 4.5, no dimension below 4, at least three reader
tasks pass, and no unresolved adversarial BLOCK/WARN. That does **not** establish Certified Gold.

- **Ordinary focused MDLOOM:** PASS — `14 files checked, 0 errors, 0 warnings` (twelve HCI guides plus
  the two touched siblings).
- **Adversarial review:** prototype R1/R2 (`05`, `08`) and **full-module R1 (all 12 guides)** complete;
  all findings repaired; final reviewer **PASS**; Pulse 02 **DONE**.
- **Da Vinci:** **no HCI-specific invariant** exists in `mdloom.toml`; ordinary MDLOOM cleanliness must
  not be represented as Da Vinci coverage.
- **Source custody:** `partial` for all twelve. MDLOOM literal backfill is recorded for 12/12; Git
  provenance is recorded for 0/12 and **pending for 12/12** because `human-computer-interaction/` is
  untracked; authentic external/primary-source custody remains incomplete.
- **Registry:** **no row** is added to `context/gold/REGISTRY.md`; no Certified Gold or
  Candidate-Hardened claim.

The strongest honest tier is **Silver**: the guides are editorially strong, adversarially repaired,
and ordinary-MDLOOM-clean, but lack HCI-specific Da Vinci protection and complete source custody.
Those gaps are future optional promotion work; the completed Pulse-02 module remains **Silver**.

---

## `human-computer-interaction/00-OVERVIEW.md`

| Gold dimension | Score | Guide-specific evidence |
|---|---:|---|
| Landscape power | 5 | The design↔evaluate loop wrapped in cross-cutting concerns places all eleven downstream guides on one map. |
| Layering integrity | 5 | The MECE ownership matrix, the defer matrix, the three-way HCI↔HF↔law seam, the concise shared spine, and the reading order unpack the opening loop in order. |
| ASCII precision | 4 | The lifecycle and ownership diagrams are legible and semantically load-bearing, if intentionally label-dense. |
| Explanatory compression | 5 | "Each concept claimed exactly once" compresses a twelve-guide field into one contract without erasing the loop/concern orthogonality. |
| Decision utility | 5 | The ownership and defer matrices route any question to its owning guide and its ultimate mechanism/stat owner. |
| Confusion handling | 5 | It rejects platform-organized HCI, overview-as-authority, and evaluation-without-generation. |
| Bridge quality | 5 | The API/installed-base and interface-contract bridges map the module without making Azure/.NET prior art load-bearing. |
| Cross-reference value | 5 | Exact guide + sibling links explain *why* to leave the module, not merely where a file is. |
| Voice | 5 | Peer-level, third-person, explicitly educational; the safety/ethics contract is operational, not boilerplate. |
| Factual confidence | 4 | RE-04 repaired the lineage-ownership overlap (concise spine here, detail in `01`); external claim custody remains partial. |

**Average: 4.8/5.**

| Reader task | Pass/fail evidence |
|---|---|
| Route a question to its owning guide. | **PASS** — Task 1 sends the completion-rate, status-by-color, and modal-menu questions to `05`/`08`/`02` and their mechanism/stat owners. |
| Detect a boundary violation. | **PASS** — Task 2 flags a `03` that re-derives Fitts' Law and routes the derivation to `cognitive-science/09`. |
| Split a high-consequence interface three ways. | **PASS** — Task 4 divides an infusion-pump UI across HCI, `human-factors/`, and `law/`. |

**Adversarial status:** RE-04 (lineage ownership) repaired; no finding open.
**Ordinary MDLOOM:** PASS, 0/0. **Da Vinci:** missing. **Source custody:** partial (mdloom-backfill;
Git pending). **Tier: Silver.**

---

## `human-computer-interaction/01-HISTORY-INTELLECTUAL-ROOTS.md`

| Gold dimension | Score | Guide-specific evidence |
|---|---:|---|
| Landscape power | 5 | The idea→surviving-idiom lineage (memex → augmentation → PARC/Star → Apple → web → ubicomp → multitouch) is one navigable chain. |
| Layering integrity | 5 | Each section drills one node of the chain and ties it to the guide that owns its modern form. |
| ASCII precision | 4 | The lineage and frame-shift ladders are clear; dates are the load-bearing labels. |
| Explanatory compression | 5 | "Idioms outlive their hardware" compresses a 75-year history into a persistence argument. |
| Decision utility | 5 | The idiom→source→date→modern-home cheat sheet answers "why is it like this?" for real conventions. |
| Confusion handling | 5 | It separates invention from popularization, demo from launch, and — after ES-01 — persistence from proven optimality. |
| Bridge quality | 5 | The backward-compatibility / installed-base bridge is universal to any senior engineer. |
| Cross-reference value | 4 | Every idiom routes to its owning guide; links are accurate if necessarily brief. |
| Voice | 5 | Peer-level and historical; the per-guide banner enforces sourcing-and-dating over CIs. |
| Factual confidence | 5 | ES-01 sourced the path-dependence argument (David 1985) and made QWERTY's optimality an explicitly contested case (Liebowitz & Margolis 1990) — no clean verdict remains. |

**Average: 4.8/5.**

| Reader task | Pass/fail evidence |
|---|---|
| Trace an idiom to its source and date. | **PASS** — Task 1 dates the hyperlink, mouse, WYSIWYG, desktop metaphor, and pinch-zoom to their origins. |
| Separate invention from popularization. | **PASS** — Task 2 keeps "Apple invented the GUI" false and "Apple mainstreamed it (1984)" true against PARC/Star. |
| Explain a persistence honestly. | **PASS** — Task 3 answers "why files and folders on phones?" with installed-base/relearning-cost logic, and (post-ES-01) *not* a clean optimality claim. |

**Adversarial status:** ES-01 (QWERTY clean verdict) repaired; no finding open.
**Ordinary MDLOOM:** PASS, 0/0. **Da Vinci:** missing. **Source custody:** partial. **Tier: Silver.**

---

## `human-computer-interaction/02-INTERACTION-MODELS.md`

| Gold dimension | Score | Guide-specific evidence |
|---|---:|---|
| Landscape power | 5 | The action cycle across two gulfs frames every model as a fault-localizer on one loop. |
| Layering integrity | 5 | Stages/gulfs → direct manipulation → modes → instrumental interaction → distributed cognition/activity theory → mental models layer from individual to system scale. |
| ASCII precision | 4 | The gulf diagram and the worked diagnosis are legible; label-dense but accurate. |
| Explanatory compression | 5 | "A usability problem lives in a gulf, at a stage" compresses diagnosis into a coordinate system. |
| Decision utility | 5 | The breakdown→model→prediction cheat sheet routes complaints to the right instrument and evidence. |
| Confusion handling | 5 | It rejects "direct manipulation is always best," "modes are always bad," and model-as-theory-of-mind. |
| Bridge quality | 5 | The gulfs-as-an-API-you-didn't-design bridge is universal. |
| Cross-reference value | 5 | Mechanism → `cognitive-science/09`; derivation → `03`; social system → `09`; each hand-off is justified. |
| Voice | 5 | Peer-level, third-person; the per-guide banner enforces falsifiability. |
| Factual confidence | 5 | ES-02 fixed the admission test to match each model's unit of analysis (individual step/gulf vs system-level field/coordination), removing the banner↔§5 contradiction. |

**Average: 4.9/5.**

| Reader task | Pass/fail evidence |
|---|---|
| Localize a complaint to a stage and gulf. | **PASS** — Task 1 assigns "clicked Save, nothing happened, clicked again" to Perceive/Evaluation with a think-aloud prediction. |
| Decide when direct manipulation is wrong. | **PASS** — Task 2 argues filter+command over select-and-delete with an execution-gulf prediction. |
| Match the model to the right evidence. | **PASS** — the new Task 6 routes a team-coordination claim to a field study (`06`) + `09` outcomes, not a single-user think-aloud, per the repaired banner. |

**Adversarial status:** ES-02 (unit-of-analysis mismatch) repaired; no finding open.
**Ordinary MDLOOM:** PASS, 0/0. **Da Vinci:** missing. **Source custody:** partial. **Tier: Silver.**

---

## `human-computer-interaction/03-INPUT-OUTPUT-MODALITIES.md`

| Gold dimension | Score | Guide-specific evidence |
|---|---:|---|
| Landscape power | 5 | The human-as-I/O-interface framing unifies pointing/typing/touch/gesture/voice/gaze/displays under throughput+error. |
| Layering integrity | 5 | The modality substrate → Fitts (applied) → Hick (applied) → text-entry measures → displays layer cleanly. |
| ASCII precision | 4 | The Fitts/Hick boxes carry real formulas; dense but correct after the effective-throughput fix. |
| Explanatory compression | 5 | "A modality claim is a performance claim" compresses the whole guide into one discipline. |
| Decision utility | 5 | The modality/measure cheat sheet decides what to measure and how to report it. |
| Confusion handling | 5 | It rejects "fewer menu items is always faster" and "a speed number proves a modality is better." |
| Bridge quality | 5 | The transport-selection bridge (latency vs throughput, human as client) is universal. |
| Cross-reference value | 5 | Fitts/Hick *derivation* deferred to `cognitive-science/09`; comparison stats to `05`/`statistics-applied/`. |
| Voice | 5 | Peer-level; the per-guide banner enforces estimator+sample or "illustrative." |
| Factual confidence | 5 | RE-10 corrected the ISO 9241-411 metric to **effective** throughput (accuracy-adjusted) and aligned the QWERTY aside with `01`. |

**Average: 4.9/5.**

| Reader task | Pass/fail evidence |
|---|---|
| Apply Fitts' Law and bound it. | **PASS** — Task 1 predicts a large edge target is faster to hit, then names where Fitts does not apply (steering/search). |
| Catch a Hick–Hyman misuse. | **PASS** — Task 2 rejects "12→6 items so it's faster" for a non-equiprobable, learned menu and demands measurement. |
| Demand a complete text-entry claim. | **PASS** — Task 3 lists WPM + error rate + sample + corpus for "our keyboard is 15% faster." |

**Adversarial status:** RE-10 (effective throughput; QWERTY aside) repaired; no finding open.
**Ordinary MDLOOM:** PASS, 0/0. **Da Vinci:** missing. **Source custody:** partial. **Tier: Silver.**

---

## `human-computer-interaction/04-DESIGN-PROCESS.md`

| Gold dimension | Score | Guide-specific evidence |
|---|---:|---|
| Landscape power | 5 | The double-diamond generate-half, wrapped in the design↔evaluate loop, frames design outputs as hypotheses. |
| Layering integrity | 5 | HCD/ISO 9241-210 → double diamond → requirements/personas/scenarios → prototyping fidelity → design systems layer in order. |
| ASCII precision | 4 | The process and fidelity diagrams are legible and decision-useful. |
| Explanatory compression | 5 | "Design proposes; evaluation disposes" compresses the whole guide's discipline. |
| Decision utility | 5 | The fidelity-matches-the-question and route-to-`05` cheat sheet decides real prototyping calls. |
| Confusion handling | 5 | It rejects "we did UCD so it's good" and stakeholder-admiration-as-evidence. |
| Bridge quality | 5 | The spec-is-a-hypothesis / design-review bridge is universal. |
| Cross-reference value | 5 | Personas/scenarios feed from `06`; validation defers to `05`; stats to `statistics-applied/`. |
| Voice | 5 | Peer-level; the generate/measure split is explicit. |
| Factual confidence | 5 | RE-02 corrected ISO 9241-210 to **six** principles and made Reader Task 1 self-contained. |

**Average: 4.9/5.**

| Reader task | Pass/fail evidence |
|---|---|
| Label the artifacts as hypotheses (self-contained). | **PASS** — the repaired Task 1 names the candidate evaluation families (inspection vs empirical; formative vs summative) and asks only the family, answerable within `04`. |
| Match fidelity to the question. | **PASS** — Task 2 chooses paper vs high-fi for "understand the concept" vs "does the swipe feel right." |
| Catch a self-validating design. | **PASS** — Task 3 rejects "the persona proves it" and "the demo wowed execs" and names what would validate. |

**Adversarial status:** RE-02 (six principles; self-contained task) repaired; no finding open.
**Ordinary MDLOOM:** PASS, 0/0. **Da Vinci:** missing. **Source custody:** partial. **Tier: Silver.**

---

## `human-computer-interaction/05-USABILITY-EVALUATION.md`

| Gold dimension | Score | Guide-specific evidence |
|---|---:|---|
| Landscape power | 5 | The inspection/empirical × formative/summative field, held under discovery-vs-measurement, frames all of evaluation. |
| Layering integrity | 5 | Inspection → empirical → the ISO metric triad → SUS → sizing/power → difference tests → the scaling contracts layer in order. |
| ASCII precision | 4 | The discovery-vs-measurement and method-landscape diagrams are legible and load-bearing. |
| Explanatory compression | 5 | "Discovery ≠ measurement" compresses the guide's whole discipline into one line. |
| Decision utility | 5 | The method-selection and target-rule cheat sheet decides real evaluation calls with the correct α semantics. |
| Confusion handling | 5 | It rejects "five users is enough (for what?)," heuristics-as-rules, and SUS-as-percent-satisfied. |
| Bridge quality | 5 | The benchmark/measurement-harness bridge is universal. |
| Cross-reference value | 5 | Mechanism to `cognitive-science/`; statistics to `statistics-applied/`; the `02` scaling contract now carries the unit-of-analysis split. |
| Voice | 5 | Peer-level; the gate-passed prototype discipline is intact. |
| Factual confidence | 5 | ES-07 held the 0.31 discovery-model λ apart from the ~35% single-evaluator heuristic average and corrected the n=8 curve to 95%; the SUS/Wilson figures reproduce (R2 prototype record). |

**Average: 4.9/5.**

| Reader task | Pass/fail evidence |
|---|---|
| Pick the method for a stage and goal. | **PASS** — Task 1 routes "what confuses new users" to formative × empirical think-aloud and "beats the old before rollout" to a summative benchmark/A-B. |
| Size and defend a study. | **PASS** — Task 2 defends five users for discovery in one segment but not for "task success is 88%," and names what `statistics-applied/` supplies. |
| Interpret a SUS score correctly. | **PASS** — Task 3 treats SUS 72 as a scaled score (not 72% satisfied), roughly average-plus, perceived and non-diagnostic. |

**Adversarial status:** prototype R1/R2 signed off; full-module ES-07 (0.31 vs ~35%; n=8) repaired;
no finding open. **Ordinary MDLOOM:** PASS, 0/0. **Da Vinci:** missing. **Source custody:** partial.
**Tier: Silver.**

---

## `human-computer-interaction/06-RESEARCH-METHODS.md`

| Gold dimension | Score | Guide-specific evidence |
|---|---:|---|
| Landscape power | 5 | "Each method carries its own inferential and validity contract" frames the whole method canon. |
| Layering integrity | 5 | Experiments → surveys → interviews → field/ethnography → diary/ESM → mixed methods → research ethics layer by validity trade. |
| ASCII precision | 4 | The method/validity map is legible and decision-useful. |
| Explanatory compression | 5 | The internal/external/ecological-validity trade compresses method choice into one axis set. |
| Decision utility | 5 | The method-to-question cheat sheet decides real study calls and names each method's cost. |
| Confusion handling | 5 | It rejects convenience-sample prevalence claims, diary-as-ground-truth, and κ-on-reflexive-analysis. |
| Bridge quality | 5 | The telemetry/instrumentation-validity bridge is universal. |
| Cross-reference value | 5 | Usability evaluation to `05`; general inferential statistics to `statistics-applied/`. |
| Voice | 5 | Peer-level; research ethics as concept, not IRB substitute. |
| Factual confidence | 4 | Method claims are bounded and paradigm-aware; external primary-source custody remains partial. |

**Average: 4.8/5.**

| Reader task | Pass/fail evidence |
|---|---|
| Match method to question and name its cost. | **PASS** — Task 1 chooses survey vs interview/field and states the validity each protects and sacrifices. |
| Catch a convenience-sample overreach. | **PASS** — Task 2 names coverage/nonresponse threats to "60% of an in-app poll love it, so most users do." |
| Refuse to treat a diary as ground truth. | **PASS** — Task 3 names missingness/reactivity at 55% compliance rather than reading logs as complete. |

**Adversarial status:** no guide-specific full-module finding; unit-of-analysis discipline consistent
with `02`/`09`. **Ordinary MDLOOM:** PASS, 0/0. **Da Vinci:** missing. **Source custody:** partial.
**Tier: Silver.**

---

## `human-computer-interaction/07-INFORMATION-ARCHITECTURE-VISUALIZATION.md`

| Gold dimension | Score | Guide-specific evidence |
|---|---:|---|
| Landscape power | 5 | "Structure first, then encoding — both judged by comprehension" unifies IA and visualization on one spine. |
| Layering integrity | 5 | IA → findability/scent → search UX (now with the browse/search/facet decision) → evaluation → encoding grammar → interaction → honesty layer in order. |
| ASCII precision | 4 | The encoding-effectiveness and search-decision diagrams are legible and load-bearing. |
| Explanatory compression | 5 | "Structure vs showing, both under discovery-vs-measurement" compresses two fields into one discipline. |
| Decision utility | 5 | The method + browse/search/facet + encoding cheat sheet (now with the search rows) decides real IA/viz calls. |
| Confusion handling | 5 | It rejects "first-click proved the nav" and "accurate chart = honest." |
| Bridge quality | 5 | The schema/namespace/routes bridge for IA is universal. |
| Cross-reference value | 5 | IR theory to `data-science/`; rendering to `computer-graphics/`; stats to `05`/`statistics-applied/`. |
| Voice | 5 | Peer-level; deceptive encodings named to refuse, not build. |
| Factual confidence | 5 | RE-05 attributed/bounded the first-click claim (Bailey et al. 2006) and ES-06 reframed dual axes as high-risk/manipulable, not inherently deceptive. |

**Average: 4.9/5.**

| Reader task | Pass/fail evidence |
|---|---|
| Diagnose a findability failure and pick the method. | **PASS** — Task 1 names the vocabulary gap and routes to card sort → tree test/first-click, discovery not a rate. |
| Design the get-to-the-item path. | **PASS** — the new Task 6 combines browse/search/facets for the three knowledge states and handles the zero-results cliff. |
| Scrutinize a high-risk chart. | **PASS** — the repaired Task 4 separates the truncated-baseline distortion from the high-risk/manipulable dual axis and gives the honest redesign. |

**Adversarial status:** ES-06 (dual axes) and RE-05 (search depth; first-click source) repaired; no
finding open. **Ordinary MDLOOM:** PASS, 0/0. **Da Vinci:** missing. **Source custody:** partial.
**Tier: Silver.**

---

## `human-computer-interaction/08-ACCESSIBILITY-INCLUSIVE-DESIGN.md`

| Gold dimension | Score | Guide-specific evidence |
|---|---:|---|
| Landscape power | 5 | The five independent accessibility axes (process/conformance/task/usability/inclusion) frame the field without nesting. |
| Layering integrity | 5 | Disability models → the axes → AT mechanisms/accessibility tree → WCAG (dated) → access-by-channel → conformance-vs-usability → governance layer in order. |
| ASCII precision | 4 | The accessibility-tree and axes diagrams are legible and load-bearing. |
| Explanatory compression | 5 | "Conformance is a floor, not usability" compresses the guide's whole stance. |
| Decision utility | 5 | The channel/mechanism/governance cheat sheet decides real accessibility calls. |
| Confusion handling | 5 | It rejects overlay-as-compliance, green-scan-as-usable, and accessibility-as-a-few. |
| Bridge quality | 5 | The semantic-contract / accessibility-API bridge is universal. |
| Cross-reference value | 5 | Legal obligation to `law/` (with the honesty note that `law/` is incomplete); operator safety to `human-factors/`. |
| Voice | 5 | Peer-level; the gate-passed prototype discipline is intact. |
| Factual confidence | 5 | RE-09 made the overlay reference exact and dated (Overlay Fact Sheet, 2021); WCAG citations verified in the prototype R2. |

**Average: 4.9/5.**

| Reader task | Pass/fail evidence |
|---|---|
| Diagnose a barrier across the stack. | **PASS** — Task 1 names color-blind + screen-reader + low-literacy channels for a red-dot status and one fix that closes all three (label+icon+text). |
| Explain conformant-but-unusable. | **PASS** — Task 2 shows a green WCAG scan can still block a screen-reader flow, catchable by AT walkthrough + testing with disabled users. |
| Place responsibility on the right owner. | **PASS** — Task 3 splits "no accessible name" / "operator overloaded" / "legally required?" across HCI, `human-factors/`, `law/`. |

**Adversarial status:** prototype R1/R2 signed off; full-module RE-09 (overlay source) repaired; no
finding open. **Ordinary MDLOOM:** PASS, 0/0. **Da Vinci:** missing. **Source custody:** partial.
**Tier: Silver.**

---

## `human-computer-interaction/09-SOCIOTECHNICAL-CSCW.md`

| Gold dimension | Score | Guide-specific evidence |
|---|---:|---|
| Landscape power | 5 | "A groupware claim must measure the coordination system, not one person" frames CSCW on the unit-of-analysis axis. |
| Layering integrity | 5 | Individual vs coordination → awareness/common ground → grounding cost → coordination-as-dependency-management → social translucence → group evaluation layer in order. |
| ASCII precision | 4 | The grounding-cost and coordination diagrams are legible and load-bearing. |
| Explanatory compression | 5 | "Measure the coordination, not the clicks" compresses the guide's discipline. |
| Decision utility | 5 | The awareness/translucence/measurement cheat sheet decides real groupware calls. |
| Confusion handling | 5 | It rejects "high SUS so the team is more effective" and "messages sent = coordination." |
| Bridge quality | 5 | The consistency-model / concurrency-control bridge is universal. |
| Cross-reference value | 5 | Mechanism to `cognitive-science/`; surveillance/legality to `11`/`law/`; operator safety to `human-factors/`. |
| Voice | 5 | Peer-level; awareness features framed to keep mutual/legitimate, not coercive. |
| Factual confidence | 5 | ES-04 neutralized the patient-safety outcome — HCI measures dropped/unacknowledged handoff items; the safety consequence defers to `human-factors/`/clinical. |

**Average: 4.9/5.**

| Reader task | Pass/fail evidence |
|---|---|
| Catch a unit-of-analysis error. | **PASS** — Task 1 rejects "high SUS so the team is more effective" and names three group outcomes. |
| Distinguish translucence from surveillance. | **PASS** — the awareness task separates mutual, coordination-serving visibility from one-directional monitoring. |
| Measure the right (group) outcome. | **PASS** — the worked case measures handoff completeness, dropped/unacknowledged items, awareness accuracy, and participation — not clicks or a lone SUS. |

**Adversarial status:** ES-04 (patient-safety coupling) repaired; no finding open.
**Ordinary MDLOOM:** PASS, 0/0. **Da Vinci:** missing. **Source custody:** partial. **Tier: Silver.**

---

## `human-computer-interaction/10-EMERGING-INTERFACES.md`

| Gold dimension | Score | Guide-specific evidence |
|---|---:|---|
| Landscape power | 5 | The post-WIMP paradigm map, held under one evidence discipline, frames AR/VR, tangible/ubicomp, conversational/agentic, BCI, and multimodal as paradigms not products. |
| Layering integrity | 5 | The evidence checklist → immersive → tangible/ubicomp → conversational/agentic → BCI → multimodal layer under the same hype-vs-evidence spine. |
| ASCII precision | 4 | The paradigm map and evidence-checklist diagrams are legible and load-bearing. |
| Explanatory compression | 5 | "Most numbers here are unresolved by construction" compresses the guide's stance. |
| Decision utility | 5 | The paradigm/evidence cheat sheet (now with the tangible/ambient row) decides how to read each claim. |
| Confusion handling | 5 | It rejects "studies show VR is dramatically better," "the assistant understood me," and "BCIs control computers with your mind." |
| Bridge quality | 5 | The vendor-benchmark-on-their-own-rig bridge is universal. |
| Cross-reference value | 5 | Model internals to `ai-engineering/`; rendering to `computer-graphics/`; neuroscience to `neuroscience/`; safety to `human-factors/`. |
| Voice | 5 | Peer-level; hype named and bounded, not amplified. |
| Factual confidence | 5 | ES-05 dated/anchored the BCI claims (Wolpaw 2002; Willett 2021/2023; Metzger 2023) and bounded them as small-N research, not shipped. |

**Average: 4.9/5.**

| Reader task | Pass/fail evidence |
|---|---|
| Apply the evidence checklist. | **PASS** — Task 1 walks novelty/self-selection/instrument/demo-vs-durable for "30% more productive, n=8, one session." |
| Frame BCI honestly. | **PASS** — Task 4 reads a "mind-reading" headset as a low-bandwidth, sensitive, unresolved channel (post-ES-05 dating). |
| Hold a tangible/ubicomp claim to the bar. | **PASS** — the new Task 6 credits affordances/periphery and keeps a "calm ambient" claim formative until field-proven. |

**Adversarial status:** ES-05 (BCI dating) and RE-06 (tangible task/row) repaired; no finding open.
**Ordinary MDLOOM:** PASS, 0/0. **Da Vinci:** missing. **Source custody:** partial. **Tier: Silver.**

---

## `human-computer-interaction/11-PRACTICE-ETHICS.md`

| Gold dimension | Score | Guide-specific evidence |
|---|---:|---|
| Landscape power | 5 | "The practice and the refusal — a metric is an instrument, not a goal" frames the profession and its ethics floor. |
| Layering integrity | 5 | Roles → critique → persuasion vs manipulation → dark-pattern taxonomy → VSD → sustainability → the ethics contract and refusal layer in order. |
| ASCII precision | 4 | The practice/refusal and VSD diagrams are legible and load-bearing. |
| Explanatory compression | 5 | "What you choose to optimize is an ethical act" compresses the guide's spine. |
| Decision utility | 5 | The influence/metric/VSD/sustainability cheat sheet decides real ethics calls. |
| Confusion handling | 5 | It rejects "all persuasion is manipulation," "legal = ethical," and (new) "the ACM Code gives me the right to refuse." |
| Bridge quality | 5 | The code-of-conduct / Goodhart's-law bridge is universal. |
| Cross-reference value | 5 | Moral theory to `ethics/`; legal duty to `law/`; org theory to `organizational-behavior/`; safety to `human-factors/`. |
| Voice | 5 | Peer-level; dark patterns as recognize-and-refuse, never a playbook. |
| Factual confidence | 5 | RE-03 separated the ACM Code's **duties** from organizational/contractual/legal **protection** and from individual ethical judgment; RE-07 gave sustainability a worked microcase. |

**Average: 4.9/5.**

| Reader task | Pass/fail evidence |
|---|---|
| Recognize and refuse a pattern. | **PASS** — Task 2 names obstruction + interface interference in a cancellation flow and gives the escalate/refuse response, not a tuning method. |
| Separate a duty from a protection. | **PASS** — the new Task 6 corrects "the ACM Code says I can refuse, so I'm protected," naming the duty vs the org/contract/law protection question. |
| Make a sustainability default call. | **PASS** — the new Task 7 names the environmental + inclusion cost of auto-play-4K-on-cellular and gives the honest low-consumption default. |

**Adversarial status:** RE-03 (ACM duty vs right) and RE-07 (sustainability microcase) repaired; no
finding open. **Ordinary MDLOOM:** PASS, 0/0. **Da Vinci:** missing. **Source custody:** partial.
**Tier: Silver.**

---

## Module-level decision

- **Tier:** **Silver** for all twelve guides — average ≥ 4.5, no dimension < 4, ≥ 3 reader tasks pass,
  no unresolved adversarial BLOCK/WARN.
- **Not Gold:** no HCI-specific Da Vinci invariant in `mdloom.toml`; source custody `partial`
  (mdloom-backfill literal only; Git provenance pending on an untracked module; external custody
  incomplete).
- **Registry:** **no row** added to `context/gold/REGISTRY.md`; no Certified Gold / Candidate-Hardened.
- **Pulse gate:** **PASS; Pulse 02 DONE.** The conservative full-module findings are repaired and the
  honest tier is Silver. Gold/Da Vinci/external-source completion is optional future work.
