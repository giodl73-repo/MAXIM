---
wave: human-systems-depth
pulse: 01
kind: architecture-record
module: human-computer-interaction
date: 2026-07-12
status: final
governing_roles: [reference-editor, expert-skeptic]
---

# human-computer-interaction/ — Architecture & Research Record (Pulse 01)

Wave-local architecture record for `human-computer-interaction/`. Condenses the
Pulse-01 design research into a durable reference: the research question, the numbered
findings (MAXIM-HCI-01 … MAXIM-HCI-24), the ratified 12-guide manifest with per-guide
architecture IDs, the ownership/defer matrix, the HCI↔human-factors seam, the
safety/ethics contract, known biases/limitations, quality risks, the prototype
rationale, and the adopt/prototype/defer decisions. This record governed the completed
Pulse-02 authoring pass and remains the boundary reference for Pulse 03 human factors.

> **Current status: FINAL — Pulse 02 DONE, final reviewer PASS.** All 12 guides are authored,
> integrated, source-backfilled, and scored **Silver**. The full-module panel's 5 BLOCK +
> 13 WARN findings were all repaired, and the final reviewer returned **PASS** with no
> unresolved BLOCK/WARN. No Gold/Da Vinci eligibility or registry insertion is claimed;
> those remain optional future-tier work. The prototype and defer language below is retained
> as the **historical Pulse-01 architecture decision record**, not as current module state.

## Summary

`human-computer-interaction/` is designed as the **interaction layer of MAXIM's
Computing & Software vertical** — the discipline of *designing and evaluating
interactive computing systems for human use*. Its unique, non-duplicating value is the
**design↔evaluate lifecycle and the cross-cutting concerns of interactive systems** —
interaction models, I/O modalities, the design process, usability evaluation, research
methods, information architecture/visualization, interactive accessibility,
sociotechnical/CSCW, emerging interfaces, and professional/ethical practice. It is
**not** the cognitive psychology beneath interaction (`cognitive-science/`), the
inferential statistics behind studies (`statistics-applied/`), the physical-product
ergonomics and Norman-model heritage (`industrial-design/`), or the operator-
performance/safety of complex work (the forthcoming `human-factors/`). The pivotal
architecture call is to organize **by lifecycle and cross-cutting concern, not by
platform/technology and not by re-teaching cognitive science** — the single most
important non-duplication decision, mirroring chemistry's "split by problem, not
technique" and clinical-medicine's "reusable reasoning patterns, not per-organ
specialties." The sharpest overlap is `cognitive-science/09-APPLIED-BRIDGE`, which
already carries the "HCI/UX laws" (Fitts, Hick, Miller, cognitive load, GOMS); it is
resolved by having `cognitive-science/` own the **mechanism and the laws** while HCI
**cites and applies** them and owns the **design/evaluation methods**. A strict
safety/ethics contract (no manipulation playbook, no legal/compliance ruling, no
safety-certification) is mandatory throughout.

## Research Question

How should MAXIM add a standalone `human-computer-interaction/` module that is
independently useful as a peer-level educational reference on the design and evaluation
of interactive systems, **without** (a) duplicating the cognitive psychology
(`cognitive-science/`), inferential statistics (`statistics-applied/`), physical-product
ergonomics and interaction-design heritage (`industrial-design/`), or graphics/ML
internals MAXIM already owns; (b) colliding with the concurrent `human-factors/` module
this same wave will add; and (c) drifting into manipulation how-to or legal/compliance
advice? Sub-questions: the right 12-guide manifest and deep scope; whether to organize by
platform or by lifecycle; exact boundaries against `cognitive-science/`,
`statistics-applied/`, `industrial-design/`, `psychology/`, `data-science/`,
`computer-graphics/`, `ai-engineering/`, and `law/`; the HCI↔HF seam; and the
safety/ethics contract that keeps the module peer-level yet responsible.

## Findings

### Repository conventions & the depth bar

- **MAXIM-HCI-01 — Module shape is fixed by convention.** `00-OVERVIEW` (landscape/
  taxonomy) + `01…N` numbered `UPPERCASE-HYPHENATED.md` guides + `STATUS.md` (manifest,
  not counted in the total). Each guide carries `maxim.frontmatter.v1` YAML (`id:
  maxim:<module>:<slug>`, `module`, `section`, `title`, `status`, …). A **prototype**
  guide (pre-backfill, as here) must be truthful: `status: prototype`,
  `source_custody: needs-source`, and `backsource_ids: []`; only after source-corpus
  backfill does it graduate to `status: source-custody` with populated `backsource_ids`.
  The `section` field takes the module slug (`section: human-computer-interaction`),
  matching the `cognitive-science`/`industrial-design`/`clinical-medicine` precedent.
- **MAXIM-HCI-02 — Style contract & hard limits.** Landscape diagram first → layer
  downward → ASCII boxes → decision-useful tables → universal-CS-first bridges → end with
  **Decision Cheat Sheet** + **Common Confusion Points**. Hard cap ~32,000 tokens/guide
  (split Part 1/Part 2 if long). Learner is a peer (VP Eng, MIT Math+TCS); bridges route
  through universal CS/systems concepts (APIs, linters, flighting, fault tolerance), not
  Azure specifics.
- **MAXIM-HCI-03 — Chemistry and clinical-medicine are the governing exemplars**, both
  deliberately deeper than `computing/01-PACKAGE.md`. Reusable structure to copy: opening
  landscape + one-line caption; ownership header ("**This guide owns… builds on… defers
  to…**"); per-guide banner; software-mental-model bridge tables; reader tasks; cheat
  sheet; confusions; global/WEIRD/resource caveats.
- **MAXIM-HCI-04 — Review is adversarial and evidence-gated.** 3–5 concrete reader tasks
  answerable without another source; diagrams that do conceptual work; tables that
  decide/compare/compress; a focused numbers/names/**dates** fact-check (named laws,
  standard versions, prevalence figures). Lenses include `expert-skeptic` (overclaims,
  stale/undated figures, advice-creep) and `reference-editor` (factual/standards accuracy,
  style-contract integrity); findings are BLOCK/WARN/NOTE;
  the module exit gate requires no unresolved BLOCK.

### Placement in the library

- **MAXIM-HCI-05 — Belongs in Computing & Software as the interaction layer** of the
  computing vertical (systems → software → data/AI → **human interaction**). It has strong
  seams *out* of the section — to `cognitive-science/` (Life Sciences) for mechanism, to
  `industrial-design/` (Arts & Culture) for the physical/product interaction heritage, and
  to the forthcoming `human-factors/` for operator safety — but its center of gravity
  (interactive computing systems, ACM SIGCHI lineage) is Computing & Software. Section/nav/
  `TRACKER` integration is **deferred to Pulse 02**; this pulse leaves the incomplete module
  unintegrated per the wave guardrail.

### Overlap inventory (the core boundary problem)

- **MAXIM-HCI-06 — CRITICAL: `cognitive-science/09-APPLIED-BRIDGE` already owns the
  "HCI/UX laws."** It carries Fitts' Law, Hick's Law, Miller's "7±2", cognitive load
  theory, GOMS, cognitive ergonomics (Endsley SA, Klein NDM), nudge theory, and the
  replication-crisis lens. This is the biggest duplication risk — the HCI analog of the
  `medicine/10` overlap that dominated the clinical wave. **Resolution:** `cognitive-
  science/` owns the **mechanism and the psychophysical laws** (the psychology, the
  derivations); `human-computer-interaction/` **cites and applies** them and owns the
  **design and evaluation methods** built on them. HCI `03` (modalities) and `02`
  (interaction models) reference Fitts/Hick as attributed applied laws; they do not
  re-derive the psychology. Proven in the prototypes: `05` repeatedly defers cognitive
  mechanism to `cognitive-science/` (why users miss a control, why verbalization is
  imperfect) rather than re-teaching it.
- **MAXIM-HCI-07 — `industrial-design/06-INTERACTION-DESIGN` owns Norman's action model
  at the product level.** It carries Norman's seven stages/gulfs, affordances, feedback,
  mapping, conceptual models, and Cooper's principles for *physical/industrial products*;
  `industrial-design/05-ERGONOMICS` owns physical anthropometry/ergonomics. **Resolution:**
  HCI `02-INTERACTION-MODELS` **applies** the action model to *interactive computing*
  (modes, direct manipulation, instrumental interaction, distributed cognition applied) and
  cross-references `industrial-design/06`; it does not re-teach the framework, and **no
  edits are made to `industrial-design/` in this pulse** (per the wave guardrail —
  prototype review first).
- **MAXIM-HCI-08 — `statistics-applied/` owns inferential statistics.** Hypothesis
  testing, power analysis, confidence-interval/regression machinery, multiple-comparison
  correction. **Resolution:** HCI states *which* estimate/test a study needs and *why*
  (e.g., Wilson score CIs on completion rates, powering an A/B comparison) and defers the
  machinery. Proven in `05` §6/§8.
- **MAXIM-HCI-09 — `psychology/` owns experimental-psychology foundations and DSM.** HCI
  `06-RESEARCH-METHODS` applies experiment/field-study design **to HCI questions** and
  defers psychological theory and the statistical apparatus.
- **MAXIM-HCI-10 — `data-science/` and `computer-graphics/` own statistical-graphics
  theory and rendering internals** behind `07-INFORMATION-ARCHITECTURE-VISUALIZATION`. HCI
  owns the *interactive* visualization (encoding-for-interaction, navigation, findability,
  dashboards as interfaces); it defers the estimator theory and the render pipeline.
- **MAXIM-HCI-11 — `ai-engineering/` and `machine-learning-theory/` own model internals**
  behind `10-EMERGING-INTERFACES` (conversational/agentic UI, recommenders). HCI owns them
  *as interaction paradigms*; it defers the model architecture and training.
- **MAXIM-HCI-12 — `human-factors/` (concurrent, this wave) is the sharpest *new* seam and
  must be locked now.** Both descend from post-war human factors of computing and share
  methods (task analysis, interface evaluation). **Split:** HCI owns the *interactive
  digital interface* — interaction design, usability, and interactive-accessibility design/
  evaluation; `human-factors/` owns *operator performance and safety* — physical/cognitive
  workload, human-error taxonomy, safety-critical human-system integration. For
  accessibility this is a **three-way** split with `law/` (see the Seam and Safety sections).
  Ratify before `human-factors/` drafts.

### External framework grounding (authoritative)

- **MAXIM-HCI-13 — The discipline has a canonical spine for `00`.** ACM **SIGCHI** and the
  founding text (Card, Moran & Newell, *The Psychology of Human-Computer Interaction*, 1983)
  plus the ACM interaction-design curricula give the module a recognizable map. Cite in
  `00-OVERVIEW`.
- **MAXIM-HCI-14 — ISO 9241 is the standards backbone.** `9241-11` (1998; rev. 2018) defines
  usability as effectiveness/efficiency/satisfaction-in-context (anchors `05`, already used);
  `9241-210` (human-centred design process) anchors `04`. Date every standard reference.
- **MAXIM-HCI-15 — Usability evaluation has a canonical, datable method set** for `05`:
  Nielsen heuristics (1990/1994), cognitive walkthrough (Wharton et al. 1994), think-aloud/
  protocol analysis (Ericsson & Simon 1980/1993), the Nielsen–Landauer discovery model
  (1993), SUS (Brooke 1996). Proven at depth in the prototype.
- **MAXIM-HCI-16 — Accessibility has a canonical standard + models** for `08`: WCAG 2.2
  (W3C Rec., 2023-10-05), POUR, WAI-ARIA (2023); the medical/social/ICF (WHO 2001)/
  interaction models; universal design's seven principles (Mace/CUD 1997). Proven at depth
  in the prototype.
- **MAXIM-HCI-17 — The design process has canonical frames** for `04`: the Design Council
  **double diamond** (2005), human-centred design (ISO 9241-210), design thinking — as
  process scaffolds, attributed, not dogma.
- **MAXIM-HCI-18 — CSCW/sociotechnical has canonical concepts** for `09`: Grudin's groupware
  challenges, awareness, common ground (Clark), social translucence (Erickson & Kellogg),
  the sociotechnical-systems tradition.

### The organizing decision (pivotal call)

- **MAXIM-HCI-19 — RECOMMENDATION: organize by the design↔evaluate lifecycle plus
  cross-cutting concerns; do NOT organize by platform/technology, and do NOT re-teach
  cognitive science.** Rationale: (1) a platform organization (web UX / mobile UX / VR UX)
  **dates instantly** and duplicates content across guides, violating EXPANSION's "avoid
  duplicating 80%+ of an existing module"; (2) the transferable value is the *lifecycle
  method* (roots → interaction models → modalities → design process → evaluation → research
  methods) and the *cross-cutting concerns* (IA/viz, accessibility, CSCW, emerging
  interfaces, practice/ethics), which survive technology churn; (3) the cognitive mechanisms
  live in `cognitive-science/` and are referenced, not rebuilt. **Emerging interfaces (`10`)
  is the single paradigm-specific guide**, and is framed as *interaction paradigms* (tangible,
  immersive, conversational, agentic) with a hype-vs-evidence discipline — not a product tour.

## Ratified Guide Manifest (12 guides: 00 + 11)

Per-guide architecture IDs (MAXIM-HCI-G00 … G11) for traceability. The manifest maps the
wave's HCI scope ("usability, interaction models, research methods, accessibility, and
socio-technical design") onto 12 files with room for the discipline's spine.

| Arch ID | # | File | Uniquely owns (peer depth) | Authoring status |
|---|---|------|------------------------------|------------------|
| MAXIM-HCI-G00 | 00 | `00-OVERVIEW.md` | Discipline map; the design↔evaluate loop; SIGCHI/Card-Moran-Newell lineage; ownership/boundary table; the module safety/ethics contract; reading order; software bridges | **complete (Pulse 02)** |
| MAXIM-HCI-G01 | 01 | `01-HISTORY-INTELLECTUAL-ROOTS.md` | Roots: Bush → Engelbart → PARC → GUI → web → mobile → post-GUI; why history constrains today's idioms | **complete (Pulse 02)** |
| MAXIM-HCI-G02 | 02 | `02-INTERACTION-MODELS.md` | Norman's action model **applied to computing** (mechanism deferred to `industrial-design/06`); direct manipulation; modes; instrumental interaction; distributed cognition applied | **complete (Pulse 02)** |
| MAXIM-HCI-G03 | 03 | `03-INPUT-OUTPUT-MODALITIES.md` | The I/O substrate: pointing/touch/gesture/voice/gaze; displays; device catalog; Fitts/Hick **cited & applied** (derivation deferred to `cognitive-science/09`) | **complete (Pulse 02)** |
| MAXIM-HCI-G04 | 04 | `04-DESIGN-PROCESS.md` | User-centred / double-diamond / design-thinking; requirements, personas, scenarios, prototyping fidelity, design systems — the *generate* half of the loop | **complete (Pulse 02)** |
| MAXIM-HCI-G05 | 05 | `05-USABILITY-EVALUATION.md` | **Usability evaluation** — inspection (heuristic eval + evaluator effect, cognitive walkthrough), empirical (think-aloud, moderated tests), ISO-9241 metric triad, SUS + interpretation limits, formative/summative, controlled tests, A/B vs usability, qualitative coding, triangulation, the sample-size ceiling, benchmark→iterate | **complete (prototype, gate-passed R2)** |
| MAXIM-HCI-G06 | 06 | `06-RESEARCH-METHODS.md` | HCI research methods: field studies, interviews, surveys, diary/ESM, ethnomethodology, experiment design **for HCI**, mixed methods, research ethics; stats deferred to `statistics-applied/` | **complete (Pulse 02)** |
| MAXIM-HCI-G07 | 07 | `07-INFORMATION-ARCHITECTURE-VISUALIZATION.md` | Information architecture, navigation, findability, search UX; **interactive** data visualization (encoding, interaction, dashboards) | **complete (Pulse 02)** |
| MAXIM-HCI-G08 | 08 | `08-ACCESSIBILITY-INCLUSIVE-DESIGN.md` | **Interactive accessibility & inclusive design** — disability models; a11y vs usability vs inclusive/universal; WCAG 2.2 (dated/bounded); AT interaction & the accessibility tree; keyboard/focus/semantics; access by channel; accessible research; conformance vs usability; localization/literacy/bandwidth; procurement/governance | **complete (prototype, gate-passed R2)** |
| MAXIM-HCI-G09 | 09 | `09-SOCIOTECHNICAL-CSCW.md` | Computer-supported cooperative work; groupware; awareness; coordination; social translucence; distance; sociotechnical fit | **complete (Pulse 02)** |
| MAXIM-HCI-G10 | 10 | `10-EMERGING-INTERFACES.md` | Post-WIMP paradigms: AR/VR/XR, tangible/ubiquitous, conversational/agentic, BCI **as interaction**, multimodal fusion; hype-vs-evidence discipline | **complete (Pulse 02)** |
| MAXIM-HCI-G11 | 11 | `11-PRACTICE-ETHICS.md` | HCI as a profession: teams/roles, critique, **persuasive design & dark-pattern ethics** (recognize-and-refuse, not a playbook), value-sensitive design, sustainability, the ethics contract | **complete (Pulse 02)** |

**Alternate 10-guide "lean" variant** (fold `01` history into `00`; merge `09` CSCW into
`11` practice) was **considered and rejected** — it buries the two most distinctive
cross-cutting concerns (collaboration and ethics) and the historical grounding that
explains why today's idioms exist. Primary recommendation is **12**.

## Ownership / Defer Matrix

**Uniquely owns:** the design↔evaluate lifecycle (`00`, `04`, `05`, `06`); interaction
models applied to computing (`02`); the I/O substrate (`03`); intellectual history (`01`);
interactive information architecture & visualization (`07`); interactive accessibility &
inclusive design (`08`); sociotechnical/CSCW (`09`); emerging interaction paradigms (`10`);
professional practice & applied ethics of interaction (`11`).

| Defers to | For |
|---|---|
| `cognitive-science/09` (+ `01`–`08`) | Cognitive **mechanisms and psychophysical laws** — Fitts, Hick, Miller, cognitive load, GOMS, situation awareness, perception/attention/memory. HCI cites & applies; never re-derives |
| `statistics-applied/` | General inferential statistics — hypothesis testing, power, CIs, regression, corrections |
| `industrial-design/06`, `industrial-design/05` | Norman's action model & interaction design **at product level**; physical anthropometry/ergonomics |
| `psychology/` | Experimental-psychology foundations; DSM-5; psychotherapy |
| `data-science/`, `computer-graphics/` | Statistical-graphics theory; rendering/pipeline internals behind visualization |
| `ai-engineering/`, `machine-learning-theory/` | Model internals behind conversational/agentic/recommender interfaces |
| `human-factors/` (forthcoming) | **Operator performance, physical/cognitive workload, human-error taxonomy, safety-critical human-system integration** |
| `law/` | **Legal obligations** — accessibility statutes, privacy law, liability, compliance duty |
| `linguistics/`, `typography/` | Writing-system/script/type **mechanisms** behind localization/legibility |
| `medicine/`, `disease/` | Clinical/medical models of disability, diagnosis, rehabilitation |

## HCI ↔ Human Factors Seam (ratified for the HF pulse)

The wave's sharpest new boundary, prototyped in `08` and locked here for Pulse 03:

- **HCI owns** the *interactive digital interface*: interaction design, usability, and
  **interactive-accessibility design/evaluation**; discretionary/consumer/productivity
  systems; the experience of use.
- **Human factors owns** *operator performance and safety*: physical & cognitive
  **workload**, **human-error taxonomy**, control-room / safety-critical human-system
  integration, performance under stress/fatigue in high-consequence work.
- **At the meeting point** (a clinical-device UI, an avionics display, a benefits-triage
  console): HCI owns the **interaction-design method and its usability/accessibility
  evaluation**; HF owns the **operator-workload, error-consequence, and safety analysis**.
  For accessibility the split is **three-way** with `law/` (legal obligation). `08` already
  encodes this as its opening boundary diagram and demonstrates it in the worked case.

## Safety / Ethics Contract (mandatory review gate)

Module-level statement in `00-OVERVIEW`, embedded/referenced by every guide: educational
reference on *how interactive systems are designed and evaluated*; **not** a manipulation
manual, a legal/compliance ruling, or a safety-certification. Author rules:

1. **No dark-pattern / manipulation playbook.** Persuasive & attention-engineering
   techniques are described *to recognize and ethically refuse*, never as actionable
   coercion/deception/addiction recipes. Any manipulation how-to is a **BLOCK**.
2. **No legal / compliance advice.** Accessibility & privacy law (ADA, §508, EAA/EN 301 549,
   GDPR) is named as **dated landscape** only; the module never rules on compliance or
   obligation — that is `law/`.
3. **No safety-certification guidance.** For failure-risks-harm interfaces, HCI owns the
   interaction/usability method only; operator-performance/safety defers to `human-factors/`.
4. **Research ethics as concept, not IRB substitute.** Human-subjects guidance (consent,
   welfare, privacy, compensation, accessible participation) is principle-level, never a
   warrant to skip ethics review.
5. **Standards & "laws" attributed, dated, bounded.** WCAG version/level, statutes, and
   named "laws" (Fitts, Hick) are dated; **heuristics are heuristics, not laws**, and
   **conformance is a floor, not usability**. Any imperative manipulation or compliance
   ruling is a **BLOCK**; any undated standard/version or heuristic-as-law is a **WARN**.

## Bias / Geographic Limitations

- **MAXIM-HCI-20** — The HCI method canon is **WEIRD-sampled** (Western, educated,
  tech-literate, English-speaking convenience samples; Henrich et al. 2010). Think-aloud
  assumes a verbalization norm; the "5 users / λ≈0.31" figure is a specific research lineage,
  not a human constant. Flag in `05`/`06` (done in `05`).
- **MAXIM-HCI-21** — Instruments carry a **language and norm base**: SUS was English-normed
  (~68 mean over largely Western software studies); translated versions need re-validation.
- **MAXIM-HCI-22** — Accessibility standards & AT are **English/Latin-script- and
  resource-rich-first**: WCAG tooling, major screen readers, and reliable ASR skew to
  dominant languages; braille/premium AT is unevenly available and costly. Flag in `08`
  (done).
- **MAXIM-HCI-23** — **Bandwidth, device, and literacy are first-order globally**: a heavy
  "conformant" page can be less accessible in practice than a lightweight plain-language one;
  inclusion that stops at WCAG AA on a fast laptop has not met a global user base (done in
  `08` §8).
- **MAXIM-HCI-24** — Disability **prevalence and models vary** (WHO ~16%/1.3 billion, 2022,
  is an estimate); social/interaction models are products of particular disability-rights
  movements. Attribute and date; do not universalize.

## Quality Risks (with mitigations)

| ID | Risk | Severity | Mitigation |
|---|---|---|---|
| QR-1 | Duplicating `cognitive-science/09` "HCI laws" | Highest | Mechanism/laws stay in `cognitive-science/`; HCI cites & applies, owns design/eval methods (MAXIM-HCI-06); proven in `05` |
| QR-2 | Manipulation how-to / dark-pattern playbook creep in `11`/`05` | High | Safety contract pillar 1; recognize-and-refuse framing; any recipe = BLOCK |
| QR-3 | Legal/compliance-advice creep in `08`/`11` | High | Safety pillar 2; standards named as dated landscape; obligation routed to `law/`; proven in `08` |
| QR-4 | Platform-organized, instantly-dated content | High | Lifecycle + cross-cutting organization (MAXIM-HCI-19); `10` is the only paradigm guide, framed as paradigms |
| QR-5 | Heuristics-as-laws / conformance-as-usability overclaim | High | Explicit caveats are load-bearing in `05` (§2) and `08` (§6); undated/overclaimed = WARN |
| QR-6 | Re-deriving industrial-design's Norman model | Med-High | HCI `02` applies, cross-references `industrial-design/06`; no ID edits this pulse (MAXIM-HCI-07) |
| QR-7 | Statistics creep (teaching inference) | Med | State which test/estimate & why; defer machinery to `statistics-applied/` (MAXIM-HCI-08); proven in `05` |
| QR-8 | `human-factors/` boundary churn (concurrent) | Med-High | Lock the HCI↔HF (three-way with `law/`) seam now, before HF drafts (MAXIM-HCI-12) |
| QR-9 | US/West-centrism; undated figures | Med | Attribute & date every law/standard/figure; global/WEIRD/resource caveats mandatory (MAXIM-HCI-20…24) |
| QR-10 | "Soft outline" failure (platitudes not depth) | High | Anchor every guide in a concrete formalism (SUS math, discovery model, POUR/a11y-tree contract) + worked cases; match chemistry/clinical depth bar |

## Historical Prototype Rationale (why `05` and `08` went first)

- **`05-USABILITY-EVALUATION`** proves the two hardest *defers* hold on real content and
  that the module hits the **quantitative depth bar**: it repeatedly hands cognitive
  mechanism to `cognitive-science/` and statistical machinery to `statistics-applied/`
  while still owning a rigorous method (SUS scoring math, the Nielsen–Landauer discovery
  model, CI-width tables, A/B-vs-usability decision logic) and a full mixed-method worked
  evaluation. It also stress-tests the "heuristics are not laws / discovery is not
  measurement" honesty that is the module's intellectual signature.
- **`08-ACCESSIBILITY-INCLUSIVE-DESIGN`** proves the **three-way HCI↔HF↔law boundary** and
  the **conformance-vs-usability honesty** without leaking into legal advice or becoming a
  compliance/manipulation manual. It is the guide where the wave's new HF seam and the `law/`
  defer are sharpest, so gate-passing it de-risks both the HF pulse and the safety contract
  for the whole module.

Both prototypes are authored at full depth and pass focused MDLOOM. Both boundary-gate rounds
have now run. The R1 panel (`panels/hci-prototype-r1/`) returned conservative-prototype
findings — statistical-rigor, model-honesty, and metadata over-claims — which were
**repaired** in `05`/`08`. The independent **strict R2 re-review** (`panels/hci-prototype-r2/`)
then re-derived the statistics (Wilson interval, SUS *t*-interval, the target-rule α
equivalence), re-checked the WCAG citations and the recall attribution, confirmed the
five-axis and distinct-AT-mechanism models and the scaling contracts read cleanly, and
**signed off**. The **prototype pattern is therefore ratified** and may govern Pulse-02
authoring; integration and source backfill remain Pulse-02 work.

## Historical Adopt / Prototype / Defer Decision

**ADOPT:** the 12-guide lifecycle-plus-cross-cutting manifest; the organize-by-lifecycle-
not-platform decision (MAXIM-HCI-19); the ownership/defer matrix; the HCI↔HF (three-way
with `law/`) seam; the safety/ethics contract as a hard gate; Computing & Software
placement; the ISO-9241 / SIGCHI spine cited in `00`.

**PROTOTYPE FIRST (this pulse):** `05-USABILITY-EVALUATION` and
`08-ACCESSIBILITY-INCLUSIVE-DESIGN` (rationale above). Both ran through `maxim-review`
(`expert-skeptic` + `reference-editor`) as an R1 boundary-gate round plus an independent
strict R2 re-review (both recorded under `panels/`), which **ratified** the pattern before
Pulse-02 authors `00`–`04`, `06`, `07`, `09`–`11`.

**DEFER / OUT OF SCOPE:** platform-specific "web/mobile/VR UX" guides (duplication by
design); editing or rescoping `cognitive-science/` or `industrial-design/` (forbidden this
pulse — prototype review first; a minimal reciprocal cross-reference, if any, is a Pulse-02
decision); `human-factors/` authoring (its own Pulse 03); section/nav/`TRACKER` integration
and source-corpus backfill (Pulse 02); the neuroscience/economics/public-policy wave areas
(later pulses).

## Historical Gaps & Uncertainties (Pulse-01 carry-forward)

> Historical note: the Pulse-02 integration, reciprocal-pointer, source-backfill,
> metadata, and standard-freshness items below were subsequently completed. The
> human-factors shelf remains a Pulse-03 decision; Gold/Da Vinci remains optional
> future work.

- **Section placement inferred, not decreed.** Computing & Software is strongly implied
  (SIGCHI/CS lineage; MAXIM-HCI-05) but not explicitly assigned in wave docs; confirm against
  `.mkdocs/mkdocs.yml` during Pulse-02 integration, and decide whether a cross-listing under
  a human-systems grouping is warranted alongside `human-factors/`.
- **`human-factors/` placement still open.** HF may land in Technology, Social Sciences, or a
  new human-systems grouping; the *seam* is locked here, the *shelf* is a Pulse-03 decision.
- **Reciprocal cross-references not yet wired.** Forward defers to `cognitive-science/09` and
  `industrial-design/06` are written into the prototypes; whether those modules get a minimal
  reciprocal pointer is a Pulse-02 call (no edits to them this pulse).
- **External figures need a primary-source recheck at authoring.** Re-verify the WCAG 2.2
  criteria counts/dates, the WebAIM Million percentage, the qualitative automated-detection recall claim and any named comparison/denominator, the
  WHO prevalence figure, and the Nielsen–Landauer λ against primary sources during Pulse-02,
  per the wave numbers/names/dates check.
- **Frontmatter/id for a hyphenated module unverified in the pipeline.** By convention `id:
  maxim:human-computer-interaction:<slug>`, `module: human-computer-interaction`; confirm the
  source-backfill `--module-id human-computer-interaction` resolves during Pulse-02
  integration (source backfill is intentionally **not** run in this prototype pulse).
- **No Gold tier yet (by design).** These prototypes carry **no Da Vinci figure invariants**
  and **no Gold eligibility** — Gold certification (proof-clean + Da Vinci invariants +
  cross-references + the ten-dimension rubric with guide-specific notes) is a later-tier
  concern, sequenced after Pulse-02 authoring, integration, and source-corpus backfill. Their
  absence is **not** a Pulse-01 prototype-authoring blocker; the Pulse-01 gate is the
  boundary/quality/safety re-review, which R2 has passed.

**Post-prototype carry-forward:** Pulse 03 must ratify the HCI↔HF (three-way with `law/`)
seam before `human-factors/` authors operator-safety content. The primary-source and
standard-freshness rechecks are Pulse-02 authoring concerns, not blockers to this prototype
architecture.
