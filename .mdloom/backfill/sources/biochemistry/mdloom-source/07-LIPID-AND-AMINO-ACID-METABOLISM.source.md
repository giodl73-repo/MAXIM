---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "07-LIPID-AND-AMINO-ACID-METABOLISM.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:biochemistry:lipid-and-amino-acid-metabolism
kind: guide
module: biochemistry
section: biochemistry
title: Lipid and Amino Acid Metabolism
status: source-custody
source_custody: partial
current_path: biochemistry/07-LIPID-AND-AMINO-ACID-METABOLISM.md
canonical_path: biochemistry/07-LIPID-AND-AMINO-ACID-METABOLISM.md
backsource_ids: [mdloom-backfill:biochemistry:07-lipid-and-amino-acid-metabolism, git-history:biochemistry:07-lipid-aa]
concepts: [beta-oxidation, ketone bodies, fatty acid synthesis, urea cycle, amino acid catabolism, transamination]
root_concepts: [lipid metabolism]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Lipid and Amino Acid Metabolism — The Other Two Fuels

```
+------------------------------------------------------------------------+
|        FATS AND PROTEINS FEED THE SAME ENGINE AS SUGAR                 |
|                                                                        |
|   FATS                          PROTEINS                               |
|   triglyceride                  dietary / muscle protein               |
|       | lipolysis                   | proteolysis                      |
|       v                             v                                  |
|   fatty acids                   amino acids                            |
|       | BETA-OXIDATION              | remove the nitrogen first        |
|       | (chop 2C at a time)         | (transamination/deamination)     |
|       v                             v                                  |
|   acetyl-CoA  +  lots of        carbon skeleton -> enters as           |
|   NADH/FADH2                     acetyl-CoA, pyruvate, or TCA          |
|       |                          intermediate                          |
|       |                             |                                  |
|       '---------> TCA + ox-phos <---'    NITROGEN -> UREA CYCLE -> pee |
|                   (file 06)                                            |
|                                                                        |
|   FASTING SPECIAL CASE: liver turns acetyl-CoA into KETONE BODIES      |
|   to fuel the brain when glucose is scarce.                            |
+------------------------------------------------------------------------+
```

Carbohydrate is not the only fuel. **Fat is the dense, long-term store** (~9 kcal/g,
more than double carbohydrate), and **protein can be burned** when needed. Both feed
into the central engine (file 06) — but each has a twist:

- **Fat catabolism (β-oxidation)** chops fatty acids into acetyl-CoA units, yielding
  large amounts of NADH/FADH2. It is the highest-yield fuel.
- **Amino acid catabolism** must first deal with the **nitrogen** — you can't just
  burn an amino acid; the amino group is toxic as ammonia and must be safely
  excreted via the **urea cycle**.

This is the "other two macronutrients" file — the bridge to `nutrition/` (why fat is
dense fuel, why protein isn't a primary fuel) and to `medicine/`/`disease/`
(ketoacidosis, urea-cycle disorders).

---

## Beta-Oxidation — Burning Fat

Fatty acids are long hydrocarbon chains. **β-oxidation** dismantles them two carbons
at a time, in the mitochondrial matrix, producing acetyl-CoA plus reducing power
each cycle.

```
+------------------------------------------------------------------------+
|   BETA-OXIDATION: one cycle shortens the chain by 2 carbons            |
|                                                                        |
|   fatty acyl-CoA (Cn)                                                  |
|       |  1. oxidation     -> FADH2                                     |
|       |  2. hydration                                                  |
|       |  3. oxidation     -> NADH                                      |
|       |  4. thiolysis (cleave off 2C)                                  |
|       v                                                                |
|   fatty acyl-CoA (Cn-2)  +  acetyl-CoA                                 |
|       |                                                                |
|       '--> repeat until the whole chain is acetyl-CoA                  |
|                                                                        |
|   PER CYCLE:  1 acetyl-CoA  +  1 NADH  +  1 FADH2                      |
+------------------------------------------------------------------------+
```

**Worked example — palmitate (C16):**

```
   C16 -> 8 acetyl-CoA requires 7 cycles (last cycle yields 2 acetyl-CoA)
   7 cycles      -> 7 NADH + 7 FADH2
   8 acetyl-CoA  -> each into TCA: 8 x (3 NADH + 1 FADH2 + 1 GTP)
                                   = 24 NADH + 8 FADH2 + 8 GTP

   Total reducing power: 31 NADH + 15 FADH2 + 8 GTP
   At ~2.5/NADH, ~1.5/FADH2, 1/GTP:  ~108 ATP gross
   minus 2 ATP equiv. to ACTIVATE the fatty acid first  ->  ~106 ATP net

   Compare: one glucose -> ~30-32 ATP. Fat is far denser fuel.
```

The transport detail worth knowing: long-chain fatty acids can't cross the inner
mitochondrial membrane on their own — they're ferried in by the **carnitine
shuttle** (carnitine palmitoyltransferase, CPT-1). CPT-1 is the regulated gate and
is inhibited by malonyl-CoA, the fat-synthesis signal — so the cell never burns and
builds fat at the same time (the same mutual-exclusion logic as glycolysis vs
gluconeogenesis in file 05).

**Fatty acid synthesis is the rough reverse**, but — as with every catabolic/
anabolic pair — it's a *separate* pathway: it runs in the **cytosol** (not matrix),
uses **NADPH** (not NADH/FADH2), carries the growing chain on **ACP** instead of
CoA, and is built by **fatty acid synthase**. Same "2 carbons at a time" logic,
opposite direction, independently regulated.

---

## Ketone Bodies — Fasting Fuel for the Brain

The brain normally runs on glucose and **cannot burn fatty acids** (they don't cross
the blood-brain barrier well). During prolonged fasting or starvation, glucose runs
low — so the liver converts excess acetyl-CoA (from heavy β-oxidation) into **ketone
bodies**, a water-soluble fuel the brain *can* use.

```
+------------------------------------------------------------------------+
|   LIVER (fasting): acetyl-CoA piling up faster than TCA can burn it    |
|       |                                                                |
|       v  ketogenesis                                                   |
|   ACETOACETATE  <-> beta-hydroxybutyrate   (+ acetone, the breath one) |
|       |  exported in blood                                             |
|       v                                                                |
|   BRAIN, HEART, MUSCLE: convert ketones back to acetyl-CoA -> TCA      |
|                                                                        |
|   The brain can meet ~2/3 of its energy from ketones in starvation,    |
|   sharply reducing how much glucose (and thus muscle protein) the      |
|   body must sacrifice for gluconeogenesis.                             |
+------------------------------------------------------------------------+
```

Ketone bodies are a clever **fuel-format conversion**: fat energy (which the brain
can't directly use) is repackaged by the liver into a soluble form the brain can
import. The three ketone bodies are **acetoacetate**, **β-hydroxybutyrate** (the
most abundant; technically not a ketone), and **acetone** (the minor one exhaled —
the fruity breath of ketosis).

This is normal and adaptive in fasting/low-carb states. It becomes pathological as
**diabetic ketoacidosis (DKA)**: in untreated type 1 diabetes, no insulin signal
means the body acts permanently "starved," over-produces ketones (which are acids),
and blood pH crashes. The bridge to `disease/`/`medicine/`: the *mechanism* is
benign fuel-switching; the *failure mode* is unregulated overproduction.

---

## Amino Acid Catabolism — Dealing With Nitrogen First

Unlike fat and sugar, amino acids carry **nitrogen** (the amino group), which can't
be oxidized for energy and is toxic as free ammonia (NH3/NH4+). So burning protein
is a two-part job: **strip the nitrogen, then burn the carbon skeleton.**

```
+------------------------------------------------------------------------+
|   STEP 1: REMOVE THE NITROGEN                                          |
|                                                                        |
|   TRANSAMINATION: amino acid + alpha-ketoglutarate                     |
|                   -> keto-acid + GLUTAMATE                             |
|                   (collect nitrogen onto glutamate; needs vitamin B6)  |
|                                                                        |
|   DEAMINATION:    glutamate -> alpha-ketoglutarate + NH4+              |
|                   (release the nitrogen as ammonia, in the liver)      |
|        |                                                               |
|        v   ammonia is toxic -> must be detoxified                      |
|   STEP 2: UREA CYCLE packages NH4+ into safe, excretable UREA          |
+------------------------------------------------------------------------+
```

The carbon skeletons that remain enter metabolism at various points and are
classified by where:

| Class | Skeleton enters as | Can become glucose? |
|---|---|---|
| **Glucogenic** | pyruvate or TCA intermediates | yes (-> gluconeogenesis) |
| **Ketogenic** | acetyl-CoA or acetoacetate | no (only ketones/fat) |
| **Both** | (Phe, Tyr, Ile, Trp, Thr) | partially |

Only Leucine and Lysine are **purely ketogenic** — they can become fat or ketones
but never glucose, because acetyl-CoA cannot be turned back into pyruvate (PDH is
irreversible, file 06). This is the same one-way valve that means **fat cannot
become glucose** in animals.

---

## The Urea Cycle — Detoxifying Nitrogen

Ammonia is toxic (especially to the brain). The **urea cycle**, running partly in
mitochondria and partly in cytosol of **liver** cells, converts two nitrogen atoms
into one molecule of **urea**, which is non-toxic, soluble, and excreted by the
kidneys.

```
+------------------------------------------------------------------------+
|   NH4+  +  CO2  (mitochondrion)                                        |
|       |  carbamoyl phosphate synthetase I (the committed step)         |
|       v                                                                |
|   carbamoyl phosphate                                                  |
|       |  joins ornithine -> CITRULLINE                                 |
|       v  (citrulline exits to cytosol)                                 |
|   citrulline + aspartate (2nd nitrogen source)                         |
|       |  -> argininosuccinate -> ARGININE + fumarate                   |
|       v                                                                |
|   arginine --[arginase]--> UREA  +  ornithine                          |
|       |                       |        |                               |
|       |                  excreted   recycled back into the cycle       |
|       '-----------------------------------------'                      |
|                                                                        |
|   NET: 2 NH3 (as NH4+ and aspartate) + CO2 -> 1 UREA + H2O             |
|   COST: ~4 ATP equivalents per urea (detox isn't free)                 |
+------------------------------------------------------------------------+
```

Key points:

- **Two nitrogen atoms per urea**, from two different sources: one as free ammonia
  (NH4+), one carried in on **aspartate**. The cycle is a nitrogen-disposal
  pipeline.
- **Ornithine is catalytic** — consumed and regenerated each turn, like
  oxaloacetate in the TCA cycle. The cycle threads its substrate through a
  regenerating carrier.
- It is **energetically expensive** (~4 ATP per urea). Detoxification costs energy —
  this is overhead the cell pays to keep ammonia safe, the metabolic equivalent of
  paying for garbage collection.
- The fumarate produced links the urea cycle to the **TCA cycle** (fumarate is a TCA
  intermediate) — the two cycles are wired together (the "Krebs bicycle").

**Failure modes** (bridge to `disease/`/`medicine/`): inherited urea-cycle enzyme
deficiencies cause **hyperammonemia** — ammonia builds up and is neurotoxic. Liver
failure does the same, because the urea cycle is liver-specific. Different organisms
excrete nitrogen differently: mammals make **urea** (urotelic), birds/reptiles make
**uric acid** (uricotelic, saves water), fish dump **ammonia** directly (ammonotelic,
diluted by surrounding water).

---

## Old World → New World Bridge

| Software / systems concept | Lipid/AA metabolism concept |
|---|---|
| Cold storage vs working memory | Fat (dense, slow) vs glycogen (fast) |
| Batch loop processing 2 units/iter | β-oxidation chopping 2 carbons per cycle |
| Format transcoding for a consumer | Ketone bodies (fat -> brain-usable fuel) |
| Separate read and write paths | β-oxidation (NADH) vs FA synthesis (NADPH) |
| Mandatory cleanup before processing | Strip nitrogen before burning the skeleton |
| Garbage collection with overhead cost | Urea cycle (~4 ATP to detox ammonia) |
| One-way pipeline stage | Acetyl-CoA can't go back to glucose |
| Mutual-exclusion interlock | CPT-1 blocked by malonyl-CoA (no burn+build) |

---

## Decision Cheat Sheet

| Question | Answer |
|---|---|
| How is fat burned | β-oxidation: 2 carbons/cycle -> acetyl-CoA + NADH + FADH2 |
| Why is fat denser fuel than sugar | More C–H bonds (more reduced) -> ~9 vs ~4 kcal/g |
| ATP from one palmitate (C16) | ~106 ATP net |
| What activates/gates fat burning | Carnitine shuttle (CPT-1), blocked by malonyl-CoA |
| What are ketone bodies for | Brain fuel during fasting (fat repackaged) |
| The three ketone bodies | Acetoacetate, β-hydroxybutyrate, acetone |
| First step of amino acid catabolism | Remove nitrogen (transamination + deamination) |
| Where the nitrogen goes | Urea cycle -> urea -> kidneys |
| Can fat/ketogenic AAs become glucose | No (acetyl-CoA can't reverse to pyruvate) |
| Cost of making urea | ~4 ATP equivalents per urea molecule |
| Which organ runs the urea cycle | Liver |

---

## Common Confusion Points

### "Can the body turn fat into glucose?"

**No** (in animals). Fat is burned to acetyl-CoA, and acetyl-CoA cannot be converted
back to pyruvate — the pyruvate dehydrogenase step (file 06) is irreversible. So the
two carbons of acetyl-CoA can't be used to net-synthesize glucose. The **glycerol**
backbone of a triglyceride *can* make a little glucose, but the bulk fatty-acid
carbon cannot. This is why fasting still requires gluconeogenesis from protein.

### "Why does burning protein require extra work?"

Because amino acids carry **nitrogen**, which can't be oxidized for energy and is
toxic as ammonia. The cell must strip the nitrogen (transamination + deamination)
and safely package it (urea cycle) before the carbon skeleton can be burned. Fat and
sugar have no nitrogen, so they skip this step. Protein is a fuel of last resort
partly because of this overhead — and because burning it means tearing down muscle.

### "Are ketones dangerous?"

Ketone production is **normal and adaptive** during fasting or a low-carbohydrate
diet — it's the body switching the brain onto fat-derived fuel. It only becomes
dangerous as **ketoacidosis** when production runs unregulated (untreated type 1
diabetes), because ketone bodies are acids and overwhelm the blood's buffering,
dropping pH. Mechanism benign; the failure mode (no insulin -> unbounded production)
is what's pathological.

### "β-oxidation vs fatty-acid synthesis — same pathway reversed?"

No — another deliberately separate forward/reverse pair. β-oxidation runs in the
**matrix**, uses **CoA** and produces **NADH/FADH2**; synthesis runs in the
**cytosol**, uses **ACP** and **NADPH**, built by a different enzyme (fatty acid
synthase). Separate locations, carriers, and enzymes let the cell independently
regulate burning vs building fat — never both at once.
