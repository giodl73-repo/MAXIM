# MAXIM Pitfalls

These entries capture recurring reference-library evidence failure classes and
map them to MAXIM controls or open repo-local risks.

## MAXIM-PF-01: Candidate-Hardened Becomes Certified Gold

**Status:** MITIGATED

**Pattern:** Batch review rows, proof-clean results, or uniform scores are
reported as guide-level Gold certification.

**Domain:** README, Gold registry, public summaries, downstream reuse, and
portfolio reporting.

**Detection difficulty:** The provenance is real and large, so the overclaim is
not obviously fabricated; the error is certification semantics.

**Structural solution:** Publish an Honesty Dashboard, list only reset-era
panel-backed guides as Certified Gold, and retain batch rows as
Candidate-Hardened provenance.

**Evidence:** `context/gold/REGISTRY.md`,
`context/audits/2026-06-27-honest-gap-audit.md`,
`context/audits/2026-07-29-gold-registry-rescope.md`, and `README.md`.

## MAXIM-PF-02: Confident Specifics Hide In Strong Guides

**Status:** MITIGATED

**Pattern:** A guide is broadly strong but includes a wrong number, name, date,
formula, or standard detail stated with confidence.

**Domain:** Knowledge guides, Gold candidates, reader-facing summaries,
downstream citation, and research reuse.

**Detection difficulty:** The surrounding synthesis is often correct, which
makes the bad specific more trusted and harder to notice.

**Structural solution:** Run targeted numbers/proper-nouns/formulas/standards
fact-check waves and record fixes source-first with regenerated custody
artifacts when applicable. Until that evidence exists, require the specific
guide path, exact claim, certification/source-custody status, supporting audit or
fact-check wave, role review, and consumer-owned verification before any number,
proper noun, date, formula, standard, version, or named historical detail is
reused as fact authority.

**Evidence:** `context/audits/2026-06-27-honest-gap-audit.md`,
`context/audits/2026-07-29-ks-fact-and-rescore.md`, and
`.roles/parliament/reference-integrity-auditor.md`,
`docs/adoption/fact-custody-boundary.md`, `README.md`, `.roles/ROLE.md`, and
`tools/check-fact-custody-boundary.ps1`.

## MAXIM-PF-03: Source-Corpus Derivatives Drift From Guides

**Status:** MITIGATED

**Pattern:** Source guides are fixed but PROOF, MDCROP, MDPORT, or FLETCH
artifacts are not regenerated or validated for the touched module.

**Domain:** `.proof/backfill`, `.mdcrop/views`, `.mdport/packs`,
`.fletch/registries`, downstream consumers, and snapshot readiness.

**Detection difficulty:** Derived files remain present and plausible after a
source edit, so stale custody is easy to miss.

**Structural solution:** Use module-scoped backfill and consumer proof commands;
do not hand-edit generated artifacts or publish packs before validation. The
current MDCROP provider revision drift was fixed by syncing
`docs/dependencies/mdcrop.json` to the local provider and rerunning the consumer
proof.

**Evidence:** `.proof/backfill/README.md`,
`context/audits/2026-07-29-module-source-backfill.md`,
`tools/check-mdcrop-adoption.ps1`, `docs/dependencies/mdcrop.json`, and
`powershell -ExecutionPolicy Bypass -File tools\check-mdcrop-adoption.ps1`.

## MAXIM-PF-04: Reference Grounding Becomes Downstream Authority

**Status:** MITIGATED

**Pattern:** A downstream repo cites MAXIM theme language as if it validates a
game, simulation, legal, medical, scientific, historical, or safety claim.

**Domain:** BANISH adoption, gamepacks, local adaptation, published packs,
portfolio summaries, and customer-facing reuse.

**Detection difficulty:** MAXIM can be legitimately useful as grounding, so the
unsafe step is treating guidance as product or domain validation.

**Structural solution:** Require named guides/packs, certification and custody
status, transformation boundary, attribution, and consumer-owned validation.

**Evidence:** `docs/adoption/reuse-boundary.md`, `README.md`,
`docs/dependencies/mdcrop.json`, and `.roles/ROLE.md`.

## MAXIM-PF-05: Bulk Cleanup Deletes Or Strands Corpus State

**Status:** MITIGATED

**Pattern:** A broad content or generated-artifact cleanup removes files or lines
without preserving nav, source-corpus, pack, registry, and count consistency.

**Domain:** Guide files, People stub retirement, generated source-corpus
artifacts, atlas/naturalis assets, and whole-repo scripts.

**Detection difficulty:** A deletion can look locally correct while stranding
hundreds of derived references or invalidating headline counts.

**Structural solution:** Keep bulk safety rules, module-scoped regeneration, and
explicit owner decisions for stub retirement or count changes.

**Evidence:** `CLAUDE.md`, `context/audits/2026-06-27-honest-gap-audit.md`,
`.proof/backfill/README.md`, and
`context/audits/2026-07-29-module-source-backfill.md`.
