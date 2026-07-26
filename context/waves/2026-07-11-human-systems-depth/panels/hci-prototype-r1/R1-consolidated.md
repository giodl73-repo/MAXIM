# HCI Prototype Boundary Gate — R1 Consolidated

Consolidated Round-1 boundary-gate review of the two `human-computer-interaction/`
prototype guides authored in Pulse 01:

- `human-computer-interaction/05-USABILITY-EVALUATION.md`
- `human-computer-interaction/08-ACCESSIBILITY-INCLUSIVE-DESIGN.md`

Panel lenses: **expert-skeptic** (`R1-expert-skeptic.md`) and **reference-editor**
(`R1-reference-editor.md`). This record merges their findings, records dispositions, and
sets the gate decision. It is **review-only** and edits no source itself.

## Scope & method

The two guides were chosen as prototypes precisely because they sit on the module's hardest
boundaries (evaluation vs `cognitive-science/` + `statistics-applied/`; interactive
accessibility vs `human-factors/` + `law/`). R1 stress-tested them for statistical rigor,
model honesty, standards accuracy, global coverage, and metadata truthfulness. The findings
below were **repaired in the same pass**; that is why R1 **conditionally** clears its own
findings but does **not** ratify the pattern — an independent strict re-review is required.

## Consolidated findings & disposition

| ID | Guide/record | Issue | Sev | Disposition |
|---|---|---|---|---|
| C-01 | 05 | n=5 4/5 CI inconsistent & un-named → standardize on Wilson 95% **[0.38, 0.96]**, reproducible | BLOCK | repaired |
| C-02 | 05 | SUS 77 / CI [72,82] vs target 75 called "at target" → **target not demonstrated**; expose mean/SD/n; pre-committed pass rule | BLOCK | repaired |
| C-03 | 05 | "exceed the CI" comparison rule → **CI/test on the difference** (independent vs paired) | BLOCK | repaired |
| C-04 | 05 | deterministic method landscape → axes narrow a family; six fit factors (risk/task/population/ecological validity/maturity/constraints) | WARN | repaired |
| C-05 | 05 | reflexive TA vs coding-reliability/codebook; κ only where coding is measurement | WARN | repaired |
| C-06 | 05 | inspection-only unseen in small sample = **unresolved**, not false positive/"refuted" | WARN | repaired |
| C-07 | 05 | missing non-WEIRD **worked** example + guide-family scaling contracts | WARN | repaired |
| C-08 | 08 | nested model + "binary-ish floor" → **five independent axes** | BLOCK | repaired |
| C-09 | 08 | AT model = "the keyboard" → distinct keyboard / a11y-API-tree / touch-pointer-voice-switch; name+role required, value/state when applicable, +descriptions/relationships | WARN | repaired |
| C-10 | 08 | usability testing = "ground truth" → **bounded evidence**, never ground truth | WARN | repaired |
| C-11 | 08 | disabled-led participatory/co-design across discovery/design/evaluation + community authority + compensation (was missing) | WARN | repaired |
| C-12 | 08 | WCAG: SC 1.4.3 text contrast vs SC 1.4.11 non-text; bound SC 2.5.8 with exceptions | BLOCK | repaired |
| C-13 | 08 | "~one-third recall" defined, attributed, and bounded (else de-numbered) | WARN | repaired |
| C-14 | 08 | non-Western/low-bandwidth/literacy/AT-access **worked** branch (not caveat only); `law/` does not yet cover digital-accessibility statutes → legal obligation still deferred | WARN | repaired |
| C-15 | 05/08 | frontmatter → `status: prototype`, `source_custody: needs-source`, `backsource_ids: []` | BLOCK | repaired |
| C-16 | STATUS / architecture / pulse | drop "passed prototype pattern"; state proposed/ratified(manifest)/in-review; record this R1 panel | BLOCK | repaired |

BLOCK: 7 · WARN: 9 · all **repaired** in the repair pass; none outstanding in source.

## Validation observed

- Focused MDLOOM (repo `mdloom.toml`, the two guides only): **2 files checked, 0 errors, 0
  warnings** after repairs.
- `git diff --check`: clean on the touched files.
- No source-corpus backfill was run (out of scope, by pulse design); no edits to
  `cognitive-science/`, `industrial-design/`, or `law/`.

## Gate decision

**Pulse 01 remains IN REVIEW.** R1 found and drove the repair of 16 conservative-prototype
findings, but every fix was made by the authoring pass itself; R1 cannot both raise and
clear its own findings. Ratification requires an independent **strict re-review (R2)** that:

1. re-derives the Wilson interval and the SUS *t*-interval from the stated inputs;
2. re-checks every WCAG citation (1.4.1, 1.4.3, 1.4.11, 2.5.8 + exceptions, 2.2 dates)
   and the recall attribution against primary sources;
3. confirms the five-axis model and the distinct-AT-mechanism model read cleanly end to
   end (no residual nesting / "floor" / "ground truth" language);
4. confirms the non-WEIRD worked example, the scaling contracts, and the co-design /
   authority / compensation additions are load-bearing, not decorative;
5. confirms frontmatter and the STATUS/architecture/pulse records stay truthful (prototype,
   needs-source, no "passed pattern").

Only after R2 signs off may the prototype pattern be marked **ratified** and govern the
Pulse-02 authoring of the remaining ten guides. Until then: no integration, no backfill,
no Pulse-02 authoring.
