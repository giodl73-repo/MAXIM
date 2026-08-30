# MAXIM Principles

These entries summarize durable MAXIM decision rules for reference integrity,
source custody, certification, downstream reuse, and reader-facing claims.

## MAXIM-P-01: Breadth Is Not Certification

**Status:** ACTIVE

**Statement:** A completed library, clean style pass, or candidate-hardening wave
does not certify guide-level factual quality.

**Rationale:** The Gold audit showed that batch rows and uniform scores can make
large-scale progress look like individual adversarial certification.

**Decision rule:** Public claims must distinguish authored coverage,
Candidate-Hardened provenance, and Certified Gold guides.

**Evidence:** `context/gold/REGISTRY.md`,
`context/audits/2026-06-27-honest-gap-audit.md`,
`context/audits/2026-07-29-gold-registry-rescope.md`, and `README.md`.

## MAXIM-P-02: Source Guides Are Canonical

**Status:** ACTIVE

**Statement:** Numbered module guides are the source of truth; PROOF, MDCROP,
MDPORT, and FLETCH artifacts are derived outputs.

**Rationale:** Hand-editing generated source-corpus artifacts breaks custody and
can leave downstream packs inconsistent with the guide text.

**Decision rule:** Edit source guides first, regenerate derived artifacts for the
touched module, and commit source plus generated outputs together.

**Evidence:** `CLAUDE.md`, `.proof/backfill/README.md`,
`context/audits/2026-07-29-module-source-backfill.md`, and
`tools/check-mdcrop-adoption.ps1`.

## MAXIM-P-03: Specific Facts Need Specific Review

**Status:** ACTIVE

**Statement:** Peer-level synthesis is not enough for load-bearing numbers,
names, dates, formulas, and standards claims.

**Rationale:** The honest-gap audits found strong guides repeatedly undermined
by confident but checkable wrong specifics.

**Decision rule:** Fact-check waves should prioritize numbers, proper nouns,
formulas, edition-sensitive standards, and claims that readers may reuse.

**Evidence:** `context/audits/2026-06-27-honest-gap-audit.md`,
`context/audits/2026-07-29-ks-fact-and-rescore.md`, and
`.roles/parliament/reference-integrity-auditor.md`.

## MAXIM-P-04: Reuse Names Sources, Not MAXIM As Authority

**Status:** ACTIVE

**Statement:** Downstream consumers may use named MAXIM guides, prompts,
published packs, or `md://` references, but must preserve certification and
source-custody state.

**Rationale:** A reference corpus can guide research without validating a game,
simulation, legal, medical, scientific, or safety claim.

**Decision rule:** A reuse claim requires a manifest naming consumed guides or
packs, certification/source-custody status, transformation boundary, attribution,
and validation or blocked-evidence status.

**Evidence:** `docs/adoption/reuse-boundary.md`, `docs/dependencies/mdcrop.json`,
`README.md`, and `.roles/ROLE.md`.

## MAXIM-P-05: Bulk Repair Is A High-Risk Operation

**Status:** ACTIVE

**Statement:** Broad automated edits across MAXIM are dangerous unless scoped,
tested, and recoverable.

**Rationale:** The repo records a prior destructive bulk SVG/content operation
that required re-cloning and rebuilding trust in generated artifacts.

**Decision rule:** Avoid content-match deletion scripts, scope file operations to
the target module, test on one file first, and keep a recoverable git state
before generated-output work.

**Evidence:** `CLAUDE.md`, `.proof/backfill/README.md`, and
`context/audits/2026-07-29-module-source-backfill.md`.
