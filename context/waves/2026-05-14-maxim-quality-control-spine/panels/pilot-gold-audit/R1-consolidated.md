# Pilot Gold Audit - Consolidated Review

## Scope

This is a review-only pilot applying Gold Rubric v2 to five representative
guides. It does not edit guide content and does not inject `@editor` tags.

| Guide | Tier | Average | Decision |
|---|---:|---:|---|
| `computing/01-PACKAGE.md` | Gold | 4.8 | model guide; protect with invariants |
| `distributed-systems/03-CONSENSUS.md` | Gold-candidate | 4.5 | strong; one deeper internals pass would make it gold |
| `periodic-table/01-HYDROGEN.md` | Silver+/Gold-candidate | 4.3 | excellent density; needs integration polish |
| `music-theory/01-PITCH-SCALES.md` | Silver+ | 4.1 | mathematically strong; notation/wording polish needed |
| `atlas/02-GLOBAL-WINDS.md` | Gold-candidate | 4.4 | visual system works; atlas-specific proof needed |

## Score Table

| Dimension | Package | Consensus | Hydrogen | Pitch | Winds |
|---|---:|---:|---:|---:|---:|
| Landscape power | 5 | 4 | 5 | 4 | 5 |
| Layering integrity | 5 | 4 | 4 | 4 | 5 |
| ASCII precision | 5 | 4 | 4 | 4 | 4 |
| Explanatory compression | 5 | 5 | 4 | 4 | 4 |
| Decision utility | 5 | 5 | 4 | 4 | 5 |
| Confusion handling | 5 | 5 | 5 | 4 | 4 |
| Bridge quality | 5 | 4 | 5 | 4 | 4 |
| Cross-reference value | 4 | 4 | 4 | 3 | 4 |
| Voice | 5 | 5 | 4 | 4 | 5 |
| Factual confidence | 4 | 5 | 4 | 4 | 4 |

## Findings

### F-01 - WARN: protect `computing/01-PACKAGE.md` as canonical

File: `computing/01-PACKAGE.md`

Finding: This is the strongest style-contract exemplar. It should be a Da Vinci
protected guide, not just an informal reference.

Consequence: Future edits could degrade the template that all other guides are
implicitly measured against.

Fix: Add invariants for the opening package-stack diagram and Decision Cheat
Sheet in a later proof pulse.

### F-02 - WARN: consensus guide is excellent but "internals" claim is slightly ahead of depth

File: `distributed-systems/03-CONSENSUS.md`

Finding: The guide explains Paxos/Raft well, but the title promises algorithm
internals. It could use one deeper failure trace: competing proposers in Paxos,
Raft log conflict repair, or quorum intersection proof.

Consequence: Expert readers may expect one more layer of algorithmic detail.

Fix: Add one sequence diagram or trace table in a future content pulse.

### F-03 - WARN: Hydrogen has one pasted-in bridge paragraph

File: `periodic-table/01-HYDROGEN.md`

Finding: The PEMFC/Nafion/ion-channel/CPU-die bridge is strong, but it appears
before the `Hydrogen Economy & Fuel Cells` heading as an unheaded paragraph.

Consequence: The bridge feels inserted rather than layered.

Fix: Move or reframe it under a bridge subheading inside the fuel-cell section.

### F-04 - WARN: Pitch guide has strong math but some notation passages need cleanup

File: `music-theory/01-PITCH-SCALES.md`

Finding: 12-TET and continued fractions are excellent for this audience. The
interval inversion passage is slightly awkward and could confuse readers.

Consequence: A strong guide loses polish at exactly the point where notation
discipline matters.

Fix: Rewrite interval inversion as a small table with interval number,
semitones, and quality inversion.

### F-05 - NOTE: Atlas wind map needs atlas-specific proof, not generic Markdown proof

File: `atlas/02-GLOBAL-WINDS.md`

Finding: The hybrid SVG/ASCII approach works well: ASCII explains mechanisms,
SVG handles geography, tables support survival decisions. Generic proof cannot
fully validate coordinate conventions, labels, and scale bars.

Consequence: A guide can pass Markdown proof while still having a cartographic
defect.

Fix: Keep atlas under `/atlas-review` criteria and add map-specific invariants.

## Reader Task Results

| Guide | Reader Tasks Pass? | Notes |
|---|---|---|
| Package | yes | Answers nesting, tool choice, common confusion |
| Consensus | yes | Answers when/why consensus; deeper trace would improve |
| Hydrogen | mostly | Broad coverage excellent; one section transition weak |
| Pitch | mostly | Formula and scale tasks pass; interval task needs polish |
| Winds | yes | Strong practical weather/navigation decisions |

## Rollout Recommendation

1. Treat `computing/01-PACKAGE.md` as the first protected Gold guide.
2. Run a remediation micro-pulse for the three WARN findings before expanding
   the pilot.
3. Add Da Vinci invariants for Package, Consensus, and Global Winds.
4. Keep proof tightening staged: do not globally force ASCII tolerance 0 yet.
