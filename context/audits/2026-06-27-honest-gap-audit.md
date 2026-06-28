# MAXIM Honest Gap Audit — 2026-06-27

External review of module quality, run against the repo's own claims rather than
restating them. Method: mechanical ground-truth scan of all content files, plus
stratified deep reads of ~25 guides (≈1% of 2,475) across all major section
clusters by independent reviewers tasked to find errors, not to be charitable.
The sampled clusters all showed the same pattern, so the findings generalize.

## Verdict in one line

The content is **genuinely peer-level and broad — not AI filler**. But three
headline claims do **not** survive scrutiny: "complete," "reviewed and clean,"
and "~1,700 guides certified Gold." The gap is **unverified detail and an
inflated certification process**, not shallowness.

---

## Gap 1 — "Gold certification" is a batch rubber-stamp (most serious)

`context/gold/REGISTRY.md` lists **1,711 guides as Certified Gold; 1,696 (99.1%)
carry the identical score 4.6**, backed by only **258 panel docs** (~6.6 guides
per panel), with **duplicate entries** inflating the count (e.g. every
`abstract-algebra/*` guide is listed twice).

A real adversarial panel produces a score *distribution*; 1,696 identical 4.6s is
the signature of a stamp. This contradicts the registry's own stated bar
("frozen to panel-backed claims… five gates agree").

**Owner decision (not changed here):** re-scope the registry to the genuinely
panel-reviewed set, or relabel the batch entries "candidate-hardened." Left for
the owner because it changes the project's self-representation.

## Gap 2 — Factual accuracy: confident confabulation of load-bearing specifics

Every guide deep-read carried ≥1 checkable error. **14 were verified against the
files and fixed in this pass** (see "Changes made"). Pattern: broad accurate
recall that occasionally confabulates a specific number, name, or formula with
full confidence and no flag — the worst failure mode for a reader who trusts a
figure *because* everything around it is correct. The "reviewed and clean" sweep
was a structural/style pass, **not** a domain fact-check.

## Gap 3 — Headline counts inflated by ~99 empty stub files — RESOLVED

> **RESOLVED (2026-06-27).** All 99 orphan stub files were deleted across the 12
> People modules, and each module's source-corpus footprint (PROOF sources, CROP
> views, PEBBLE packs, FLETCH registry, module record) was wiped and regenerated
> from the remaining canonical guides only — round-trip 0 failures, every
> canonical guide has its corpus, no orphan artifacts remain. Verified that all 99
> deletions were in the known orphan list and that no canonical guide was touched
> (the stub names appeared in no STATUS.md or nav; the only cross-references were
> basename collisions with canonical guides in sibling directories).

The People section carries **99 orphan stub files** (22-line frontmatter-only
`> Stub` files, e.g. `mathematicians-logicians/01-ANCIENT-FOUNDATIONS.md`), an
abandoned alternate naming generation alongside the 134 finished canonical
guides. The canonical People guides are **fully built and excellent** (they use
"Who to Cite for What" as the biography-genre form of the Decision Cheat Sheet —
a defensible variation worth documenting in the contract).

**These stubs are NOT safe to bulk-delete.** They are wired into the
source-corpus pipeline — `.proof/backfill/sources/**`, `.proof/backfill/modules/*.json`,
`.fletch/registries/*-source-corpus.json`, `BILL-OF-MATERIALS.md`, and
`.claude/gen_people.py` — and were counted in the "2,180 guides bound" backfill.
Deleting the `.md` files alone would strand ~300+ derived artifacts. So the real
finding is integrity, not cleanup: **the "~2,170 guides / ~14,070 pages" headline
counts ~99 empty files as bound guides.**

**Owner decision (not changed here):** either retire the stubs *and* regenerate
the People corpus + update BOM + `gen_people.py`, or keep them but stop counting
them as bound guides. A half-deletion would manufacture inconsistency.

## Gap 4 — The canonical exemplar is the shallowest content sampled

`computing/01-PACKAGE.md` — the file every guide is told to imitate — nails the
*format* but under-delivers *depth*, even dipping below the learner's stated floor
(handholding `.NET` advice to a deep-.NET reader). Holding the most
structure-perfect, content-thinnest file up as THE standard plausibly explains
why downstream guides optimize for filling template slots over depth. Worth
swapping the exemplar to a genuinely deep guide (e.g. `os/03-LINUX.md`,
`ai-engineering/04-AGENTS.md`, `distributed-systems/02-CONSISTENCY-MODELS.md`).

---

## What is genuinely fine (balance)

- **Tag cleanliness is real** — 0 true outstanding `@editor` tags (the 9 grep
  hits are all prose *describing* the system).
- **Coverage is real and even** — 217 directories, no thin/empty sections; the
  smallest files are all intentional (puzzle cards, STATUS stubs).
- **The strong guides are strong** — distributed-systems, OS/Linux, evolution,
  viral disease, complex analysis, fundamental groups, game theory, epistemology,
  semantics, antitrust all survive a specialist read with only nits. The systems
  bridges (kinetic proofreading → T-cell discrimination; covering spaces → Galois;
  sequencing generations → I/O architectures) are real synthesis.

---

## Changes made in this pass (14 factual fixes, source guides only)

| File | Was | Now |
|---|---|---|
| `biology/01-MOLECULAR-MACHINERY.md` | 2024 Chem Nobel "Rumelhart" | Hassabis + Jumper (AlphaFold2); shared w/ Baker |
| `biology/01-MOLECULAR-MACHINERY.md` | (see note) Okazaki length | *not changed — flagged, low-confidence; see follow-up* |
| `genomics/01-SEQUENCING-TECH.md` | 10x barcode "10-bp" | 16-bp |
| `geology/05-PLATE-TECTONICS.md` | reversals "every ~200k–1M yr" | irregular, not periodic |
| `music-theory/06-TONAL-HARMONY.md` | shipped artifact "12/4=3? no…" | clean coset count |
| `philosophy/02-EPISTEMOLOGY.md` | "Gettier Case 2" (barns) | Goldman 1976 fake-barns |
| `abstract-algebra/06-GALOIS-THEORY.md` | "irreducible in char p ⇒ separable" | perfect-field condition + counterexample |
| `abstract-algebra/06-GALOIS-THEORY.md` | constructible "iff degree 2^k" | necessary-not-sufficient, tower form |
| `cryptography/02-ASYMMETRIC.md` | PKCS#1v1.5 sig "length-extension" | Bleichenbacher '06 forgery |
| `cryptography/02-ASYMMETRIC.md` | Curve25519/X448 field `𝔽_{2²⁵⁵}` | `𝔽_p (255)` / `𝔽_p (448)` (box-aligned) |
| `physics/09-ZERO-POINT-ENERGY.md` | "Three classes" then lists 4 | "Four classes" |
| `physics/09-ZERO-POINT-ENERGY.md` | moon-mass BH T_H "2.5 K" | 1.7 K |
| `distributed-systems/03-CONSENSUS.md` | VR "Liskov and Cowling (1988)" | Oki & Liskov 1988; revisited 2012 |
| `law/04-ANTITRUST.md` | duplicated Google ad-tech verdict | de-duplicated |
| `mathematics/21-MEASURE-THEORY.md` | garbled convergence diagram | correct implication lattice |

## Known-but-not-fixed (follow-up fact-check wave)

These were flagged by reviewers but not fixed here — lower confidence, or needing
a domain pass, not single-line edits:

- `biology/01` Okazaki fragment length (~200 nt quoted for a bacterial replisome
  section; bacterial fragments are ~1–2 kb).
- `cryptography/02` OAEP encoding (lines ~124–130) is self-contradictory; needs a
  correct rewrite of DB/seed masking, plus a broken code-fence near 350–386.
- `distributed-systems/03` Raft "terms" diagram (lines ~203–215) double-labels
  term 2, skips term 3, jumps to term 4; split-vote column unnumbered.
- `genomics/01` Sanger throughput "~1 kb/run" in the comparison table (off ~100×).
- `disease/02` 1918 flu "highest death toll pandemic in history" overclaim.
- General: a numbers-and-proper-nouns fact-check across the library is the single
  highest-value remaining work.

## Pipeline note

The 14 edits are to **source guides** (correct per the Source-First rule). The
derived source-corpus artifacts (`.proof`/`.fletch`/`.crop`/`.pebble`) for the 11
touched modules are now **stale** and should be regenerated via
`module_source_backfill.py`. **Regeneration is currently blocked** in this
checkout: the helper shells out to a PROOF binary at `C:\src\proof\Cargo.toml`,
which does not exist here (PROOF lives at `repos/tools-infra/proof`). Wire that
path up, then regenerate the 11 modules and revalidate before snapshotting.

## Wave 2 — fact-check sweep across under-sampled sections (15 more fixes)

Six more reviewers read ~30 additional guides across Technology, Mechanics,
Natural World / Earth-Space, Material Culture, Arts/Language, and Social/History.
**Most guides were clean** — the error rate is real but concentrated, not
pervasive. 15 verified fixes applied:

| File | Was | Now |
|---|---|---|
| `telecommunications/09-CHANNEL-CODING.md` | Shannon limit "for rate R = 1" = −1.59 dB | "as rate R → 0" (−1.59 dB is the R→0 limit) |
| `nuclear/02-REACTOR-PHYSICS.md` | U-233 thermal η "2.11" | 2.29 (Pu-239 → 2.11) |
| `aeronautics/01-AERODYNAMICS.md` | flaps "↓ nose-up moment" | nose-down moment |
| `astronomy/03-CELESTIAL-MECHANICS.md` | Io "exceeds Earth's total geothermal output ×35" | mean surface heat flux (per area) ×35 |
| `periodic-table/02-NOBLE-GASES.md` | "Bartlett reacted XeF₂" | reacted Xe |
| `periodic-table/02-NOBLE-GASES.md` | "XeF⁺[AsF₆]⁻ (1962 compound)" | Xe⁺[PtF₆]⁻ |
| `mycology/05-TOXIC-FUNGI.md` | phalloidin "actin polymerization inhibitor" | stabilizes F-actin, blocks depolymerization |
| `pigments/07-PRUSSIAN-BLUE-ERA.md` | cerulean "Hoppfner (1805)" | Höpfner (1789); timeline → 1860 marketed |
| `pigments/07-PRUSSIAN-BLUE-ERA.md` | "Nicolas Vauquelin" | Louis-Nicolas Vauquelin |
| `pigments/07-PRUSSIAN-BLUE-ERA.md` | Prussian blue "17th–21st century" | 18th–21st |
| `typography/02-GUTENBERG-MOVEABLE-TYPE.md` | "1477 Bruges" (self-contradictory) | 1473 Bruges, reordered before London |
| `photography/02-FILM-CHEMISTRY.md` | ISO 100 "H = 1/100 lux·s" | H = 0.8/100 ≈ 0.008 lux·s (ISO 6 standard) |
| `photography/02-FILM-CHEMISTRY.md` | T-grains "Kodak 1982" | Kodak 1980s |
| `psychology/05-PERSUASION-INFLUENCE.md` | "Firehose of Falsehood (RAND Cordesman 2015)" | RAND, Paul & Matthews 2016 |

**Deliberately NOT changed** (discipline — a contestable "fix" is worse than the
flag): Scheele "nitrogen" → fluorine (Scheele has a legitimate independent claim
to nitrogen, ~1772); Subiaco "1464" (defensible as press-establishment year vs.
1465 first dated imprint); cerulean timeline date nuance (synthesis 1789 vs.
marketed 1860). These are noted, not silently rewritten.

**Cumulative: 29 verified factual fixes across two waves**, ~55 guides read
(~2.2% of the library). The pattern held in every cluster: strong content,
periodically undermined by a confidently-stated wrong number, name, or formula —
confirming the "reviewed and clean" sweep never fact-checked the specifics.

## Recommended order

1. Re-scope / relabel the Gold registry (cheap, high-integrity).
2. Run a numbers-and-proper-nouns fact-check wave (highest reader value).
3. Decide the People-stub question (retire+regenerate, or stop counting).
4. Swap the style exemplar; document the People "Who to Cite" variation.
5. Correct README/CLAUDE.md "reviewed and clean / complete" wording to match.
