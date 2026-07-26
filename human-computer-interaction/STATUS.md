# human-computer-interaction/ — Status

**12 of 12 guides authored · Module COMPLETE · Pulse 01 COMPLETE (prototype pattern ratified, R2) · Pulse 02 DONE (final reviewer PASS) · Silver for all 12 guides · No unresolved BLOCK/WARN**

> Guides `05-USABILITY-EVALUATION` and
> `08-ACCESSIBILITY-INCLUSIVE-DESIGN` were authored first as Pulse-01
> prototypes to de-risk the module's hardest boundaries. The independent strict
> prototype R2 review signed off on that pattern. Pulse 02 authored the other
> ten guides, wired the module into the section/nav/tracker surfaces, added
> minimal reciprocal pointers to `industrial-design/06` and
> `cognitive-science/09`, and ran source-corpus backfill. The full-module panel
> then raised 5 BLOCK + 13 WARN conservative findings; all were repaired. Its
> tier rubric scores every guide **Silver**, with no Gold/Da Vinci claim and no
> `context/gold` registry row. The final reviewer returned **PASS** after all
> content and record repairs, closing Pulse 02 with no unresolved BLOCK/WARN.

## Scope in one line

`human-computer-interaction/` owns the **design and evaluation of interactive
computing systems for human use**: interaction models, input/output modalities,
the design process, usability evaluation, research methods, information
architecture/visualization, interactive accessibility, sociotechnical/CSCW,
emerging interfaces, and professional/ethical practice. It is the
human-interaction layer of the Computing & Software vertical. It is an
educational reference, not legal, compliance, or safety-certification advice.

## Guide Manifest (12 guides: 00 + 11)

| # | File | Uniquely owns (at peer depth) | Status |
|---|---|---|---|
| 00 | `00-OVERVIEW.md` | Discipline map; design↔evaluate loop; ownership/defer matrix; safety/ethics contract; reading order | ✅ authored (Pulse 02) |
| 01 | `01-HISTORY-INTELLECTUAL-ROOTS.md` | HCI intellectual roots and why lineage constrains current idioms | ✅ authored (Pulse 02) |
| 02 | `02-INTERACTION-MODELS.md` | Interaction models applied to computing; direct manipulation, modes, activity theory, distributed cognition | ✅ authored (Pulse 02) |
| 03 | `03-INPUT-OUTPUT-MODALITIES.md` | Pointing, typing, touch, gesture, voice, gaze, displays, and bounded Fitts/Hick applications | ✅ authored (Pulse 02) |
| 04 | `04-DESIGN-PROCESS.md` | User-centred process, requirements, personas, scenarios, prototyping fidelity, and design systems | ✅ authored (Pulse 02) |
| 05 | `05-USABILITY-EVALUATION.md` | Inspection and empirical evaluation, ISO-9241 metrics, SUS limits, mixed methods, and benchmark→iterate | ✅ authored (prototype, gate-passed R2) |
| 06 | `06-RESEARCH-METHODS.md` | Field studies, interviews, surveys, diary/ESM, experiments, mixed methods, and research ethics | ✅ authored (Pulse 02) |
| 07 | `07-INFORMATION-ARCHITECTURE-VISUALIZATION.md` | Findability, search UX, interactive visualization, encoding, interaction, and dashboards | ✅ authored (Pulse 02) |
| 08 | `08-ACCESSIBILITY-INCLUSIVE-DESIGN.md` | Interactive accessibility, inclusive design, AT interaction, WCAG context, and governance | ✅ authored (prototype, gate-passed R2) |
| 09 | `09-SOCIOTECHNICAL-CSCW.md` | CSCW, groupware, awareness, coordination, collaboration, and sociotechnical fit | ✅ authored (Pulse 02) |
| 10 | `10-EMERGING-INTERFACES.md` | AR/VR/XR, tangible/ubiquitous, conversational/agentic, BCI-as-interaction, and multimodal systems | ✅ authored (Pulse 02) |
| 11 | `11-PRACTICE-ETHICS.md` | Professional practice, critique, recognize-and-refuse dark patterns, value-sensitive design, and sustainability | ✅ authored (Pulse 02) |

## Boundary Contracts

| Defers to | For |
|---|---|
| `cognitive-science/` | Cognitive mechanisms and psychophysical-law derivations |
| `statistics-applied/` | General inferential statistics and power machinery |
| `industrial-design/` | Product-level Norman action model and physical ergonomics |
| `human-factors/` (Pulse 03) | Operator workload, error taxonomy, safety-critical integration, and performance under stress/fatigue |
| `law/` | Legal obligations, liability, and compliance duties |
| `medicine/`, `disease/` | Clinical models of disability, diagnosis, and rehabilitation |
| `linguistics/`, `typography/` | Script, language, and type mechanisms |
| `data-science/`, `computer-graphics/` | Statistical-graphics theory and rendering internals |
| `ai-engineering/`, `machine-learning-theory/` | Model internals behind agentic and recommender interfaces |

## HCI ↔ Human Factors Seam

- **HCI owns** interactive digital-interface design, usability, interactive
  accessibility, and evaluation.
- **Human factors owns** operator performance, physical/cognitive workload,
  human-error taxonomy, safety-critical integration, and performance under
  stress or fatigue.
- At shared systems such as clinical-device or avionics interfaces, HCI owns
  interaction design and usability/accessibility evaluation; human factors owns
  workload, error-consequence, and safety analysis.
- **Reciprocal pointer (`human-factors/` now authored, Human Systems Depth Pulse 04, in
  review).** For the safety-critical workload/error/performance-under-stress **evidence**,
  route to [`human-factors/03`](../human-factors/03-COGNITIVE-WORKLOAD-SITUATION-AWARENESS.md)
  (workload/SA measurement), [`human-factors/06`](../human-factors/06-DISPLAY-CONTROL-INTERFACE-DESIGN.md)
  (alarm philosophy, mode/state visibility), [`human-factors/04`](../human-factors/04-HUMAN-ERROR-TAXONOMIES.md)
  (error taxonomy), and [`human-factors/08`](../human-factors/08-SAFETY-SYSTEMS-AND-HAZARD-ANALYSIS.md)
  (hazard analysis). HCI **retains** the interaction, information-architecture/visualization,
  and interactive-accessibility **methods**. A safety-critical console is **still an HCI
  system**: the modules supply **methods and evidence, not sign-off** — **acceptance and
  implementation belong to the accountable domain organization and its regulator**, never to a
  reference module.

## Safety / Ethics Contract

1. No dark-pattern or manipulation playbook.
2. No legal or compliance ruling; standards and statutes are dated context only.
3. No safety-certification or safety-case guidance.
4. Research-ethics guidance is not a substitute for ethics review.
5. Standards and named “laws” are attributed, dated, and bounded.

## Placement (wired)

Home: **Computing & Software**. Pulse 02 wired the module into
`sections/computing-software.md`, `.mkdocs/mkdocs.yml`, and `TRACKER.md`; added
the two bounded reciprocal pointers; and ran PROOF/CROP/PEBBLE/FLETCH backfill.
All 12 guides carry `status: source-custody` / `source_custody: partial`.

The digital-accessibility statute gap remains an explicit future `law/` concern.
HCI names the dated standards landscape but does not answer legal-duty questions.

## Pulse 02 status — DONE

All ten remaining guides were authored at full peer depth on the gate-passed
prototype pattern and its family-specific scaling contracts. Integration,
reciprocal pointers, and source backfill are complete. The full-module panel's
5 BLOCK + 13 WARN findings were all repaired; every guide is **Silver**. The
final reviewer returned **PASS** after those content and record repairs. Pulse
02 is **DONE**, the module is **COMPLETE** (✅), and there are no unresolved
BLOCK/WARN. Gold/Da Vinci certification and registry work remain optional future
scope; legal content remains deferred to a future `law/` pulse.

## Current validation summary

- Final reviewer: **PASS** after all content and record repairs.
- Adversarial ledger: **5 BLOCK + 13 WARN raised, all repaired; 0 unresolved**.
- Tier: **Silver for all 12 guides**; no Gold/Da Vinci claim and no registry row.
- Focused PROOF record: **14 files checked, 0 errors, 0 warnings**.
- Source-backfill validation: HCI **12/12 PASS**; generator tests **9 passed**.
- Current record checks: `git diff --check` and focused stale-status grep run at finalization.

## Pulse 01 historical record

Pulse 01 ratified the architecture and the prototype pattern. The prototype R1
panel returned conservative statistical, model-honesty, and metadata findings;
all were repaired in `05` and `08`. The independent strict prototype R2 review
verified the repairs and signed off. Pulse 01 intentionally performed no module
integration or source backfill and claimed no Gold/Da Vinci eligibility.