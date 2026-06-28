---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "04-METABOLISM-OVERVIEW.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:biochemistry:metabolism-overview
kind: guide
module: biochemistry
section: biochemistry
title: Metabolism Overview
status: source-custody
source_custody: partial
current_path: biochemistry/04-METABOLISM-OVERVIEW.md
canonical_path: biochemistry/04-METABOLISM-OVERVIEW.md
backsource_ids: [proof-backfill:biochemistry:04-metabolism-overview, git-history:biochemistry:04-metabolism-overview]
concepts: [metabolism, catabolism, anabolism, ATP, NADH, NADPH, bioenergetics, regulation]
root_concepts: [metabolism]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Metabolism Overview — The Flux Network

```
+------------------------------------------------------------------------+
|                METABOLISM = ONE BIG DATAFLOW GRAPH                     |
|                                                                        |
|   CATABOLISM (break down)            ANABOLISM (build up)              |
|   energy-releasing, deltaG<0         energy-requiring, deltaG>0        |
|                                                                        |
|   big molecules                      small precursors                  |
|       |                                  ^                             |
|       v                                  |                             |
|   oxidize, release e- and energy     reduce, consume energy            |
|       |                                  ^                             |
|       v                                  |                             |
|   .----------------------------------------------------.               |
|   |   SHARED CURRENCY POOL                              |              |
|   |   ATP  (energy)    NADH (catabolic e-)              |              |
|   |   NADPH (anabolic reducing power)                   |              |
|   '----------------------------------------------------'               |
|       |                                  ^                             |
|       '-- catabolism CHARGES the pool ---'                             |
|       .-- anabolism SPENDS the pool ------.                            |
|                                                                        |
|   The pool COUPLES the two halves. Energy is a shared resource budget. |
+------------------------------------------------------------------------+
```

Metabolism is the **entire network of chemical reactions** in a cell. It splits
cleanly into two opposed flows that share one resource budget:

- **Catabolism** breaks molecules down, releases energy, *charges* the ATP/NADH
  pool (ΔG < 0, runs downhill).
- **Anabolism** builds molecules up, *spends* energy from the pool (ΔG > 0, must be
  paid for).

The whole field clicks into place once you see it as a **dataflow graph with a
global resource budget**. Metabolites are nodes, enzymes are edges, and ATP/NADPH
are the shared currency that lets the cell run uphill reactions by coupling them to
downhill ones. This file is the systems-level map; files 05–08 zoom into specific
subgraphs.

---

## Energy Coupling — The Central Trick

How does a cell run a reaction that wants to go the *wrong* way (ΔG > 0)? It
**couples** it to ATP hydrolysis (strongly ΔG < 0). If the sum of the two ΔGs is
negative, the combined reaction proceeds.

```
+--------------------------------------------------------------------------+
|   UNFAVORABLE alone:   glucose + Pi -> G6P + H2O   deltaG = +13.8 kJ/mol |
|   ATP hydrolysis:      ATP + H2O -> ADP + Pi       deltaG = -30.5 kJ/mol |
|   ---------------------------------------------------------------------  |
|   COUPLED (one step):  glucose + ATP -> G6P + ADP  deltaG = -16.7 kJ/mol |
|                                                                          |
|   The enzyme does BOTH in one active site so the energy never escapes    |
|   as heat between steps. Net deltaG < 0 -> it runs.                      |
+--------------------------------------------------------------------------+
```

This is exactly the first reaction of glycolysis (hexokinase). The systems analogy:
the cell **borrows from the ATP budget** to fund an operation that couldn't run on
its own, then later refills the budget by burning fuel. ATP is working capital; the
cell keeps it charged so the "loan" is always available.

**Why ATP and not a stronger bond?** ATP sits in the *middle* of the
phosphoryl-transfer energy scale — high enough to drive most biosynthesis, low
enough to be recharged easily. It's an intermediate denomination, like a $20 bill:
big enough to buy most things, small enough to make change. Cells turn over their
entire ATP mass many times per minute; a human cycles roughly their body weight in
ATP per day.

---

## The Carriers — Reusable Currency (Recap + Detail)

```
+------------------------------------------------------------------------+
|   CARRIER     CHARGED   SPENT     CARRIES         USED MOSTLY IN       |
|   -------     -------   -----     -------         -------------        |
|   ATP/ADP     ATP       ADP+Pi    phosphoryl /    everywhere (energy)  |
|                                   free energy                          |
|   NAD+/NADH   NADH      NAD+      2e- + H+         CATABOLISM          |
|                                                   (feeds ETC -> ATP)   |
|   NADP+/NADPH NADPH     NADP+     2e- + H+         ANABOLISM           |
|                                                   (biosynthesis)       |
|   FAD/FADH2   FADH2     FAD       2e- + 2H+        TCA, beta-oxidation |
|   FMN, CoQ,...                    e- relay        electron transport   |
|                                                                        |
|   Coenzyme A (CoA-SH): carries ACYL groups (e.g., acetyl-CoA),         |
|   the activated 2-carbon unit at the hub of the whole map.             |
+------------------------------------------------------------------------+
```

The key conceptual move: **electron transfer = energy transfer.** When a fuel is
"oxidized" (loses electrons), those electrons are captured by NAD+ -> NADH. The
NADH then carries that reducing power to the electron transport chain (file 06),
which uses it to pump protons and make ATP. So burning fuel is, mechanically, a
controlled flow of electrons from fuel down to oxygen, with ATP skimmed off along
the way.

**Oxidation/reduction shorthand (OIL RIG):** Oxidation Is Loss of electrons,
Reduction Is Gain. Fuels are reduced (electron-rich); CO2 is oxidized (electron-
poor). Catabolism is a slow, staged oxidation that captures the released energy
instead of letting it flash off as heat (which is what burning sugar in a flame
does).

---

## The Shape of the Map — Convergence and Divergence

```
+------------------------------------------------------------------------+
|   CATABOLISM CONVERGES        ANABOLISM DIVERGES                       |
|                                                                        |
|   many fuels                   few precursors                          |
|     \  |  /                       /  |  \                              |
|      \ | /                       / | | \                               |
|   carbs fats proteins         (acetyl-CoA, pyruvate, etc.)             |
|       \ | /                       / | | \                              |
|        \|/                       /  |  \                               |
|     acetyl-CoA  <--- HUB --->   thousands of products                  |
|         |                       (lipids, amino acids, nucleotides...)  |
|         v                                                              |
|    TCA + ETC                                                           |
|                                                                        |
|   FUNNEL IN to a few hubs       FAN OUT from a few hubs                |
+------------------------------------------------------------------------+
```

Catabolism is a **funnel**: dozens of input molecules all converge on a handful of
central intermediates (pyruvate, acetyl-CoA, the TCA intermediates). Anabolism is
the reverse — a **fan-out** from those same few hubs to thousands of products. This
hub-and-spoke topology is why you only need to learn a few central pathways to
understand most of metabolism: everything routes through the same junctions.

Catabolic and anabolic routes for the "same" transformation are usually **not the
exact reverse** of each other — they share most steps but differ at the regulated,
irreversible steps, and often use different carriers (NADH out, NADPH in). This is
deliberate: separate forward and reverse routes can be **independently regulated**,
so the cell can shut one down while running the other. (Glycolysis vs.
gluconeogenesis in file 05 is the textbook case.)

---

## Three Stages of Catabolism

```
   STAGE 1: DIGESTION         polymers -> monomers (hydrolysis)
            proteins -> amino acids, carbs -> sugars, fats -> FA+glycerol
                 |
                 v
   STAGE 2: TO ACETYL-CoA     monomers -> a few central intermediates
            glycolysis (05), beta-oxidation (07), amino acid catabolism (07)
            -> pyruvate -> ACETYL-CoA      (some NADH/ATP captured here)
                 |
                 v
   STAGE 3: OXIDATION         acetyl-CoA -> CO2; reducing power -> ATP
            TCA cycle (06) + electron transport / ox-phos (06)
            -> the BULK of ATP is made here
```

The headline quantitative fact, set up here and derived in 05–06: **most ATP comes
from stage 3 (oxidative phosphorylation), not from the substrate-level steps in
glycolysis.** Glycolysis nets only 2 ATP per glucose; complete oxidation yields
**~30–32 ATP**. Roughly 90% of the energy is harvested in the mitochondrion.

---

## Regulation — The Scheduler

A flux network needs control or it would burn fuel uselessly (running catabolism
and anabolism at once = a "futile cycle" wasting ATP as heat). Cells regulate flux
at three timescales:

```
+------------------------------------------------------------------------+
|   MECHANISM            SPEED         ANALOGY                           |
|   ---------            -----         -------                           |
|   1. ALLOSTERIC        milliseconds  runtime flag flips a hot path     |
|      (binding)         - seconds     (e.g., ATP inhibits PFK-1)        |
|                                                                        |
|   2. COVALENT MOD      seconds -      config patch via signal cascade  |
|      (phosphorylation) minutes       (hormones -> kinases, file 09)    |
|                                                                        |
|   3. GENE EXPRESSION   minutes -      recompile: make more/less enzyme |
|      (enzyme amount)   hours          (transcription, biology/)        |
+------------------------------------------------------------------------+
```

The **energy charge** is the master signal. The cell senses the ratio of charged to
spent currency:

```
                 [ATP] + 1/2 [ADP]
  energy charge = ------------------------     (ranges 0 to 1; cells hold ~0.85-0.95)
                 [ATP] + [ADP] + [AMP]

  HIGH charge (plenty of ATP)  -> inhibit catabolism, allow anabolism
  LOW charge  (ATP depleted)   -> fire up catabolism to refill the pool
```

This is a **PID-style controller reading a single scalar** and steering the whole
network. Key sensors: high ATP/AMP ratio throttles catabolism; **AMP-activated
protein kinase (AMPK)** is the literal low-fuel sensor — it switches on when AMP
rises (ATP is depleted) and turns on catabolism while shutting off biosynthesis.
NADH/NAD+ ratio is a parallel signal for the oxidative side.

**Rate-limiting steps** are the control points. Each pathway has a committed,
effectively irreversible, allosterically regulated step that acts as the network's
throttle — phosphofructokinase-1 (PFK-1) for glycolysis is the classic example
(file 05). Regulating the committed step is the same engineering principle as
admission control at a system's entry point.

---

## Old World → New World Bridge

| Software / systems concept | Metabolism concept |
|---|---|
| Dataflow / pipeline graph | The metabolic map (metabolites + enzymes) |
| Global resource budget / quota | ATP / NADPH pool |
| Borrowing from a budget to run a job | Energy coupling (ΔG > 0 paid by ATP) |
| Hub-and-spoke architecture | Convergent catabolism / divergent anabolism |
| Admission control at entry | Regulating the committed (first) step |
| Scheduler reading a load metric | Energy charge driving allosteric control |
| Runtime flag vs config patch vs recompile | Allosteric vs covalent vs gene-expression control |
| Wasted CPU in a busy-loop | Futile cycle (catabolism + anabolism at once) |
| Low-battery throttling | AMPK firing when AMP rises |

---

## Decision Cheat Sheet

| Question | Answer |
|---|---|
| Catabolism vs anabolism | Break-down (releases energy) vs build-up (consumes it) |
| What couples the two halves | The shared ATP/NADPH/NADH pool |
| NADH vs NADPH role | NADH -> ATP (catabolic); NADPH -> biosynthesis (anabolic) |
| Central hub metabolite | Acetyl-CoA |
| Where most ATP is made | Oxidative phosphorylation (stage 3), not glycolysis |
| How fast is allosteric control | Milliseconds–seconds |
| How fast is hormonal control | Seconds–minutes (covalent mod) |
| How fast is enzyme-amount control | Minutes–hours (gene expression) |
| Master "how much fuel?" signal | Energy charge / ATP:AMP ratio (AMPK) |
| Where the throttle sits in a pathway | The committed, irreversible, regulated step |

---

## Common Confusion Points

### "Why have separate NADH and NADPH at all?"

So the cell can run catabolism (which produces NADH to make ATP) and anabolism
(which consumes NADPH to build molecules) **at the same time** without the two
ledgers short-circuiting. Same electrons, different tag (one phosphate), enforced
by enzyme specificity. It is pure accounting separation — a "revenue" pool and a
"capital" pool that hold identical dollars but never mix.

### "Is anabolism just catabolism run backwards?"

Almost, but deliberately not. The two share many reversible steps but diverge at
the regulated, irreversible steps, often using different enzymes and different
carriers. Separate control points let the cell turn one direction on and the other
off — you can't independently throttle a road that's the exact reverse of another.

### "Does the cell store ATP for later?"

No. ATP is spent within seconds of being made. Long-term energy is stored as
**glycogen** (fast access) and **fat** (dense, ~9 kcal/g). ATP is the on-demand
currency those stores are converted *into* — never the savings account itself.

### "Where does the energy in fuel actually live?"

In the **electrons** of reduced (C–H rich) bonds. Fuels like glucose and fat are
electron-rich; oxidizing them moves electrons "downhill" to oxygen, and the cell
skims that flow to make ATP. Fat stores more energy per gram than carbohydrate
precisely because it is more reduced — more C–H bonds, more electrons to harvest.
