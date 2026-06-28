---
maxim_schema: maxim.frontmatter.v1
id: maxim:biochemistry:glycolysis-and-gluconeogenesis
kind: guide
module: biochemistry
section: biochemistry
title: Glycolysis and Gluconeogenesis
status: source-custody
source_custody: partial
current_path: biochemistry/05-GLYCOLYSIS-AND-GLUCONEOGENESIS.md
canonical_path: biochemistry/05-GLYCOLYSIS-AND-GLUCONEOGENESIS.md
backsource_ids: [proof-backfill:biochemistry:05-glycolysis-and-gluconeogenesis, git-history:biochemistry:05-glycolysis]
concepts: [glycolysis, gluconeogenesis, pyruvate, fermentation, reciprocal regulation]
root_concepts: [glycolysis]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Glycolysis and Gluconeogenesis — Splitting and Rebuilding Glucose

```
+------------------------------------------------------------------------+
|        GLYCOLYSIS: glucose (6C) -> 2 pyruvate (3C each)                |
|                                                                        |
|   GLUCOSE  (6 carbons)                                                 |
|      |  INVESTMENT PHASE: spend 2 ATP to prime the molecule            |
|      |  (steps 1-5)                                                    |
|      v                                                                 |
|   fructose-1,6-bisphosphate                                            |
|      |  SPLIT into two 3-carbon pieces                                 |
|      v                                                                 |
|   2x glyceraldehyde-3-phosphate (G3P)                                  |
|      |  PAYOFF PHASE: each 3C piece yields 2 ATP + 1 NADH              |
|      |  (steps 6-10)                                                   |
|      v                                                                 |
|   2x PYRUVATE  (3 carbons each)                                        |
|                                                                        |
|   LEDGER (per glucose):  gross 4 ATP - 2 ATP invested = NET 2 ATP      |
|                          + 2 NADH  + 2 pyruvate                        |
+------------------------------------------------------------------------+
```

Glycolysis ("sugar splitting") is the ancient, universal, **cytosolic** pathway
that cleaves one 6-carbon glucose into two 3-carbon pyruvate molecules. It needs no
oxygen, runs in essentially every cell, and is the on-ramp to the rest of energy
metabolism. The structure is a **deferred-payoff investment**: spend 2 ATP up
front to destabilize glucose, then recover 4 ATP on the back end.

**Commit these three numbers — they are the most-misquoted facts in metabolism:**

```
   PER GLUCOSE, glycolysis nets:   2 ATP  +  2 NADH  +  2 PYRUVATE
```

Gross ATP is 4; you spent 2 to prime; **net is 2**. Confusing gross with net is the
classic error — track both columns.

---

## The Two Phases

```
+------------------------------------------------------------------------+
|   PHASE 1: ENERGY INVESTMENT (steps 1-5)        deltaATP = -2          |
|                                                                        |
|   1. glucose --[HEXOKINASE]--> G6P        spend 1 ATP  (irreversible)  |
|   2. G6P -> fructose-6-phosphate (F6P)    isomerize                    |
|   3. F6P --[PFK-1]--> F1,6BP              spend 1 ATP (COMMITTED STEP) |
|   4. F1,6BP -> split into DHAP + G3P      aldolase cleaves 6C -> 3C+3C |
|   5. DHAP <-> G3P                         now have 2x G3P              |
|                                                                        |
|   PHASE 2: ENERGY PAYOFF (steps 6-10, x2 because two G3P)              |
|                                                                        |
|   6. G3P -> 1,3-BPG          + NADH       capture electrons (x2)       |
|   7. 1,3-BPG -> 3-PG         + ATP        substrate-level phos. (x2)   |
|   8. 3-PG -> 2-PG                         isomerize                    |
|   9. 2-PG -> PEP                          dehydrate                    |
|  10. PEP --[PYRUVATE KINASE]--> pyruvate  + ATP (x2, irreversible)     |
|                                                                        |
|   Payoff: 4 ATP + 2 NADH produced (each step 6/7/10 happens twice)     |
+------------------------------------------------------------------------+
```

| Phase | Steps | ATP | NADH | Net effect |
|---|---|---|---|---|
| Investment | 1–5 | −2 | 0 | prime + split glucose into 2× G3P |
| Payoff | 6–10 (×2) | +4 | +2 | oxidize G3P to pyruvate, harvest energy |
| **Total** | | **net +2** | **+2** | 1 glucose -> 2 pyruvate |

Two mechanistic points worth flagging for a rigorous reader:

- **Substrate-level phosphorylation** (steps 7 and 10): ATP is made *directly* by
  transferring a phosphate from a high-energy intermediate onto ADP — no membrane,
  no oxygen, no electron transport chain. Contrast this with **oxidative**
  phosphorylation (file 06), where ATP is made indirectly via a proton gradient.
  Glycolysis's 2 ATP are substrate-level; this is why it works anaerobically.
- The **NADH must be reoxidized** or glycolysis halts. Step 6 reduces NAD+ to
  NADH, and NAD+ is finite. The cell *must* recycle NADH back to NAD+ to keep
  going — which is the whole reason fermentation exists (below).

---

## Three Irreversible (Regulated) Steps

Most glycolytic steps are near-equilibrium and reversible. Three are strongly
exergonic and effectively one-way — and those three are the **control points** and
the steps gluconeogenesis must bypass:

```
+------------------------------------------------------------------------+
|   STEP   ENZYME            WHY REGULATED                               |
|   ----   ------            ------------                                |
|   1      HEXOKINASE        traps glucose in the cell (G6P can't leave) |
|   3      PFK-1             THE committed step; the main throttle       |
|   10     PYRUVATE KINASE   final commitment to pyruvate                |
+------------------------------------------------------------------------+
```

**PFK-1 (phosphofructokinase-1)** is the master regulator — the admission-control
valve for the whole pathway:

| Signal | Effect on PFK-1 | Meaning |
|---|---|---|
| **ATP** (high) | inhibits | "we have energy — stop burning glucose" |
| **AMP** (high) | activates | "energy is low — burn glucose now" |
| **Citrate** (high) | inhibits | TCA backed up — no need for more fuel |
| **Fructose-2,6-bisphosphate** | strongly activates | hormonal "fed state, run glycolysis" |

This is **negative feedback on the committed step** (file 03/04 in action). High
ATP throttles its own production; high AMP (low energy) opens the valve. **Fructose-
2,6-bisphosphate (F2,6BP)** is the hormonal override — its level is set by
insulin/glucagon signaling (file 09), letting the body coordinate glycolysis across
tissues, not just within one cell.

---

## After Pyruvate — Three Fates

```
+------------------------------------------------------------------------+
|                          PYRUVATE                                      |
|                   .---------+---------.                                |
|        AEROBIC    |         |         |   ANAEROBIC                    |
|        (O2 present)         |         (no O2)                          |
|        v                    v         v                                |
|   ACETYL-CoA          (alanine, etc.) FERMENTATION                     |
|   -> TCA cycle (06)   biosynthesis    regenerate NAD+                  |
|   -> ox-phos                          to keep glycolysis going         |
|   -> ~30-32 ATP total                                                  |
|                                       LACTATE (animals, muscle)        |
|                                       ETHANOL + CO2 (yeast)            |
+------------------------------------------------------------------------+
```

The whole point of the anaerobic fates is **NAD+ regeneration**, not energy:

```
   LACTATE fermentation:   pyruvate + NADH -> lactate + NAD+
   ETHANOL fermentation:   pyruvate -> acetaldehyde + CO2;
                           acetaldehyde + NADH -> ethanol + NAD+
```

Fermentation produces **no extra ATP** — it exists solely to recycle NADH back to
NAD+ so step 6 of glycolysis can keep running when the electron transport chain
(which normally reoxidizes NADH) is unavailable. A sprinting muscle ferments
pyruvate to lactate because it's burning glucose faster than oxygen can be
delivered; yeast ferments to ethanol because it's the same trick with a different
endpoint (and the basis of brewing — see `natural-sciences/` /
`fermentation-spirits`). The bridge: **fermentation is a fallback mode** — low
throughput (2 ATP) but always available, like a degraded service path that keeps
the pipeline from deadlocking when the main route is down.

---

## Gluconeogenesis — Rebuilding Glucose

Gluconeogenesis makes glucose **from non-carbohydrate precursors** (lactate, amino
acids, glycerol) — essential during fasting because the brain and red blood cells
demand glucose. It runs mostly in the **liver**.

```
+------------------------------------------------------------------------+
|   GLUCONEOGENESIS = glycolysis run backward, BUT bypassing the 3       |
|   irreversible steps with DIFFERENT enzymes.                           |
|                                                                        |
|   glucose  <--- glucose-6-phosphatase ------------ G6P                 |
|     ^                                               ^                  |
|     |  (bypass hexokinase)                          |                  |
|     |                                          F6P  |                  |
|     |  fructose-1,6-bisphosphatase ---<-------- F1,6BP                 |
|     |  (bypass PFK-1)                                ^                 |
|     |                                               |                  |
|     |  PEP <-- PEP carboxykinase <-- oxaloacetate <-- pyruvate         |
|     |          + pyruvate carboxylase (bypass pyruvate kinase)         |
|                                                                        |
|   COST: ~6 ATP equivalents per glucose (it is NOT free reversal)       |
+------------------------------------------------------------------------+
```

The reason gluconeogenesis is **not** just glycolysis in reverse: the three
irreversible glycolytic steps have ΔG too negative to push backward. Each is
bypassed by a separate enzyme that makes the reverse direction favorable (at ATP
cost). The **pyruvate -> PEP bypass** is the elaborate one: it routes through
oxaloacetate using two enzymes (pyruvate carboxylase, then PEP carboxykinase) and
spends ATP/GTP to climb back uphill.

| Glycolysis (down) | Gluconeogenesis bypass (up) |
|---|---|
| hexokinase | glucose-6-phosphatase |
| PFK-1 | fructose-1,6-bisphosphatase |
| pyruvate kinase | pyruvate carboxylase + PEP carboxykinase |

---

## Reciprocal Regulation — Don't Run Both at Once

Running glycolysis and gluconeogenesis simultaneously would just burn ATP in a
**futile cycle** (make glucose, immediately break it, net waste as heat). The cell
prevents this by regulating both with **opposite responses to the same signals** —
reciprocal control.

```
+------------------------------------------------------------------------+
|   SIGNAL            GLYCOLYSIS (PFK-1)   GLUCONEOGENESIS (F1,6BPase)   |
|   ------            ------------------   ---------------------------   |
|   AMP (low energy)  ACTIVATE             INHIBIT                       |
|   F2,6BP (fed)      ACTIVATE             INHIBIT                       |
|   ATP / citrate     inhibit              (allow)                       |
|   high              (fasting)                                          |
|                                                                        |
|   ONE signal pushes the two pathways in OPPOSITE directions ->         |
|   only one runs at a time. (Mutual exclusion via shared signal.)       |
+------------------------------------------------------------------------+
```

This is the cleanest **mutual-exclusion** pattern in metabolism: a single
allosteric signal (notably F2,6BP, hormonally set by insulin vs glucagon — file 09)
simultaneously turns one direction on and the other off. It's a hardware interlock,
guaranteeing the two opposing pathways can't both be active and waste ATP.

---

## Old World → New World Bridge

| Software / systems concept | Glycolysis concept |
|---|---|
| Deferred-payoff / invest-then-return | Investment phase (−2 ATP) then payoff (+4) |
| Gross vs net throughput accounting | Gross 4 ATP vs net 2 ATP |
| Admission-control valve | PFK-1 gating the committed step |
| Runtime override flag | F2,6BP hormonal control of PFK-1 |
| Degraded/fallback service path | Fermentation (low yield, always available) |
| Deadlock avoidance (resource recycling) | NAD+ regeneration keeps glycolysis flowing |
| Mutual exclusion / interlock | Reciprocal regulation of glycolysis vs gluconeogenesis |
| Reverse op with different cost | Gluconeogenesis bypasses, not reverses |

---

## Decision Cheat Sheet

| Question | Answer |
|---|---|
| Glycolysis net ATP per glucose | **2 ATP** (gross 4, minus 2 invested) |
| Glycolysis NADH per glucose | **2 NADH** |
| Glycolysis pyruvate per glucose | **2 pyruvate** |
| Where does glycolysis run | Cytosol (no organelle, no O2 needed) |
| The committed/regulated step | PFK-1 (step 3) |
| How is ATP made in glycolysis | Substrate-level phosphorylation (steps 7, 10) |
| Purpose of fermentation | Regenerate NAD+ (not to make ATP) |
| Anaerobic products | Lactate (animals) or ethanol + CO2 (yeast) |
| What gluconeogenesis costs | ~6 ATP equivalents per glucose |
| Why it isn't just reverse glycolysis | 3 irreversible steps need bypass enzymes |
| What prevents futile cycling | Reciprocal regulation (F2,6BP, AMP) |

---

## Common Confusion Points

### "Is glycolysis 2 ATP or 4 ATP?"

Both numbers are real — don't mix them up. **Gross production is 4 ATP**, but the
investment phase **spends 2 ATP**, so the **net is 2 ATP**. Always specify gross
vs. net. The 2 NADH and 2 pyruvate are produced net (no investment of those).

### "Does fermentation make energy?"

No. Fermentation produces **zero net ATP beyond glycolysis's 2**. Its only job is
to regenerate NAD+ so glycolysis can keep cycling. Anaerobic glycolysis nets the
same 2 ATP per glucose whether it ends in lactate or ethanol — the fermentation
step itself is purely a recycling reaction.

### "Why can't gluconeogenesis just reverse glycolysis?"

Three glycolytic steps (hexokinase, PFK-1, pyruvate kinase) release so much free
energy that reversing them is thermodynamically impossible under cellular
conditions. Gluconeogenesis uses four different enzymes to bypass these three
steps, spending ATP/GTP to make the uphill direction favorable. Same overall
transformation, different — and more expensive — route.

### "Where does the NADH from glycolysis go?"

Aerobically, it's carried into the mitochondrion (via shuttle systems) and feeds
the electron transport chain (file 06), where it yields ATP. Anaerobically, it's
spent locally on fermentation to regenerate NAD+. The fate of glycolytic NADH is
what links this file to file 06 and determines the total ATP yield.
