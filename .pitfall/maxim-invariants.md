# MAXIM Invariants

These entries summarize properties that must remain true for MAXIM content,
certification, source-corpus artifacts, review gates, and downstream reuse.

## MAXIM-I-01: Certified Gold Count Stays Evidence-Backed

**Status:** VERIFIED

**Claim:** Only guides listed in `context/gold/REGISTRY.md` under Current
Certified Gold may be called Certified Gold.

**Why it matters:** Inflated Gold counts create false confidence in a library
whose breadth is real but whose guide-level certification is narrow.

**Enforcement:** The Honesty Dashboard separates 2 Certified Gold guides from
Candidate-Hardened provenance and forbids bulk wave promotion.

**Evidence:** `context/gold/REGISTRY.md`,
`context/audits/2026-07-29-gold-registry-rescope.md`, and `README.md`.

## MAXIM-I-02: Generated Source-Corpus Artifacts Are Not Hand-Edited

**Status:** VERIFIED

**Claim:** `.proof/backfill/**`, `.mdcrop/views/**`, `.mdport/packs/**`, and
`.fletch/registries/**` are derived surfaces unless the generator or schema is
the explicit target.

**Why it matters:** Hand edits can make packs, views, registries, and guides
disagree while still looking like committed evidence.

**Enforcement:** The source-first rule and module backfill flow require source
guide edits followed by scoped regeneration.

**Evidence:** `CLAUDE.md`, `.proof/backfill/README.md`,
`context/audits/2026-07-29-module-source-backfill.md`, and
`tools/check-mdcrop-adoption.ps1`.

## MAXIM-I-03: `@editor` Tags Remain A Live Dashboard

**Status:** VERIFIED

**Claim:** Outstanding `@editor[...]` tags are review state, not prose, and they
block a guide from being treated as clean.

**Why it matters:** MAXIM's review workflow depends on inline tags being
grep-able and removed only when the issue is fixed.

**Enforcement:** `proof.toml` defines the `no_editor_tags` custom rule and
`CLAUDE.md` documents dashboard grep commands.

**Evidence:** `proof.toml`, `CLAUDE.md`, `README.md`, and `.roles/ROLE.md`.

## MAXIM-I-04: Downstream Reuse Keeps Certification And Custody Visible

**Status:** VERIFIED

**Claim:** A downstream consumer must identify the specific MAXIM guide, pack, or
prompt used and carry its certification/source-custody status.

**Why it matters:** Citing "MAXIM" as an undifferentiated authority hides whether
the source is Certified Gold, Candidate-Hardened, source-custody, or
needs-source.

**Enforcement:** The reuse boundary requires a downstream manifest with consumed
surfaces, claim boundary, attribution, and validation or blocked status.

**Evidence:** `docs/adoption/reuse-boundary.md`, `docs/dependencies/mdcrop.json`,
`README.md`, and `.roles/ROLE.md`.

## MAXIM-I-05: Broad Corpus Edits Require Scoped Validation

**Status:** PARTIAL

**Claim:** Any broad or generated-output change must be scoped to a module,
validated, and kept recoverable before it is treated as safe.

**Why it matters:** MAXIM's corpus scale makes accidental line deletion,
stale-derived output, and silent nav/count drift high-impact failures.

**Enforcement:** Safety rules prohibit content-match deletion scripts and the
backfill flow forbids whole-repo regeneration first, but full coverage remains
process-dependent.

**Evidence:** `CLAUDE.md`, `.proof/backfill/README.md`,
`context/audits/2026-06-27-honest-gap-audit.md`, and
`context/audits/2026-07-29-module-source-backfill.md`.

## MAXIM-I-06: Specific Facts Require Custody Before Reuse

**Status:** VERIFIED

**Claim:** Numbers, proper nouns, dates, formulas, standards, versions, and named
historical details in MAXIM are research leads unless a downstream consumer can
name the guide path, exact claim, certification/source-custody status,
supporting audit or fact-check wave, Reference Integrity Auditor review, and
consumer-owned verification.

**Why it matters:** A broadly strong guide can make one wrong specific more
trusted, especially when a downstream repository turns the prose into public,
scientific, legal, safety, product, or simulation authority.

**Enforcement:** The fact-custody boundary and policy check keep `MAXIM-PF-02`
visible from README, reuse, PITFALL, role, and invariant surfaces.

**Evidence:** `docs/adoption/fact-custody-boundary.md`, `README.md`,
`.pitfall/maxim-pitfalls.md`, `.roles/ROLE.md`,
`.roles/parliament/reference-integrity-auditor.md`, and
`tools/check-fact-custody-boundary.ps1`.
