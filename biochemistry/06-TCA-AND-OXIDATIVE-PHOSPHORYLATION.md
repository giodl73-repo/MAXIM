---
maxim_schema: maxim.frontmatter.v1
id: maxim:biochemistry:tca-and-oxidative-phosphorylation
kind: guide
module: biochemistry
section: biochemistry
title: TCA Cycle and Oxidative Phosphorylation
status: source-custody
source_custody: partial
current_path: biochemistry/06-TCA-AND-OXIDATIVE-PHOSPHORYLATION.md
canonical_path: biochemistry/06-TCA-AND-OXIDATIVE-PHOSPHORYLATION.md
backsource_ids: [proof-backfill:biochemistry:06-tca-and-oxidative-phosphorylation, git-history:biochemistry:06-tca]
concepts: [TCA cycle, citric acid cycle, electron transport chain, chemiosmosis, ATP synthase, ATP yield]
root_concepts: [oxidative phosphorylation]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# TCA Cycle and Oxidative Phosphorylation — Where the ATP Is Made

```
+------------------------------------------------------------------------+
|        THE OXIDATIVE ENGINE (inside the mitochondrion)                 |
|                                                                        |
|   acetyl-CoA (2C)                                                      |
|       |                                                                |
|       v                                                                |
|   .-------------------.   per turn produces:                           |
|   |   TCA / CITRIC    |   3 NADH + 1 FADH2 + 1 GTP + 2 CO2             |
|   |   ACID CYCLE      |   (the cycle's real product is REDUCING POWER) |
|   '-------------------'                                                |
|       |  NADH, FADH2 carry electrons ->                                |
|       v                                                                |
|   .-------------------------------------------.                        |
|   | ELECTRON TRANSPORT CHAIN (Complexes I-IV) |                        |
|   | electrons flow downhill to O2;            |                        |
|   | energy PUMPS PROTONS across the membrane  |                        |
|   '-------------------------------------------'                        |
|       |  builds a PROTON GRADIENT (proton-motive force)                |
|       v                                                                |
|   .-------------------.                                                |
|   |   ATP SYNTHASE    |   protons flow back through it ->              |
|   |  (Complex V)      |   the flow SPINS a rotor that makes ATP        |
|   '-------------------'                                                |
|                                                                        |
|   NET: this stage makes ~26 of the ~30-32 ATP per glucose.             |
+------------------------------------------------------------------------+
```

This is where biology generates the **bulk of its ATP**. Glycolysis (file 05)
netted only 2 ATP. Here, the carriers (NADH, FADH2) that earlier steps produced are
cashed in: the TCA cycle squeezes more reducing power out of acetyl-CoA, then the
electron transport chain converts that reducing power into a **proton gradient**,
and ATP synthase turns the gradient into ATP. The genius of the design is the
intermediate currency — **a proton gradient across a membrane** — which decouples
"burning fuel" from "making ATP."

The systems framing: this is a **water-wheel powered by a dam**. Electron transport
pumps protons uphill to fill a reservoir (the gradient); ATP synthase is a turbine
the protons spin on the way back down. **Chemiosmosis** is the name for using a
membrane gradient as an energy intermediate — and it is one of the most surprising
ideas in biology (Peter Mitchell won a Nobel for it; nobody believed energy was
stored as a *gradient* rather than a chemical bond).

---

## Step 0: Pyruvate -> Acetyl-CoA (The Link Reaction)

Before the cycle, pyruvate (from glycolysis) must enter the mitochondrion and be
converted to acetyl-CoA by the **pyruvate dehydrogenase complex (PDH)**:

```
   pyruvate (3C) + NAD+ + CoA  ->  acetyl-CoA (2C) + NADH + CO2

   PER GLUCOSE (2 pyruvate):  2 acetyl-CoA + 2 NADH + 2 CO2
```

PDH is a huge, heavily regulated multienzyme complex and an irreversible
commitment: once carbon is acetyl-CoA it cannot go back to glucose (this is why fat,
which enters as acetyl-CoA, cannot be turned into glucose — file 07). PDH is
inhibited by its products (NADH, acetyl-CoA) and by ATP — the usual energy-charge
feedback.

---

## The TCA Cycle — One Turn

The **TCA cycle** (tricarboxylic acid cycle; also **citric acid cycle** or **Krebs
cycle** — three names, one pathway) runs in the **mitochondrial matrix**. Each turn
oxidizes one acetyl group (2 carbons) fully to 2 CO2, capturing the energy as
reducing power.

```
+------------------------------------------------------------------------+
|   acetyl-CoA (2C) + oxaloacetate (4C)                                  |
|        |  citrate synthase                                             |
|        v                                                               |
|   CITRATE (6C)                                                         |
|        |                                                               |
|        v   (2 oxidations release 2 CO2, capture 2 NADH)                |
|   isocitrate -> alpha-ketoglutarate  [+NADH +CO2]  (isocitrate DH)     |
|        |                                                               |
|        v   alpha-KG -> succinyl-CoA  [+NADH +CO2]  (alpha-KG DH)       |
|        |                                                               |
|        v   succinyl-CoA -> succinate [+GTP]   (substrate-level!)       |
|        |                                                               |
|        v   succinate -> fumarate     [+FADH2] (succinate DH = Cx II)   |
|        |                                                               |
|        v   fumarate -> malate -> OXALOACETATE [+NADH]                  |
|        |                                                               |
|        '---> oxaloacetate regenerated -> cycle repeats                 |
+------------------------------------------------------------------------+
```

**Per turn (one acetyl-CoA):**

```
   3 NADH  +  1 FADH2  +  1 GTP  +  2 CO2
```

**Per glucose (2 turns, because glycolysis made 2 pyruvate -> 2 acetyl-CoA):**

```
   6 NADH  +  2 FADH2  +  2 GTP  +  4 CO2
```

Two things to internalize:

- **The cycle's real output is electrons, not ATP.** Only 1 GTP per turn is made
  directly (substrate-level phosphorylation, at the succinyl-CoA step). The 3 NADH +
  1 FADH2 are the valuable product — they carry electrons to the ETC for the big
  payoff. The TCA cycle is a *fuel-prep stage*, not the power plant itself.
- **Oxaloacetate is catalytic.** It's consumed at the start and regenerated at the
  end, so a little goes a long way — like a reaction catalyst that loops. But TCA
  intermediates are also drained for biosynthesis (amino acids, heme), so they must
  be topped up by **anaplerotic** reactions (e.g., pyruvate -> oxaloacetate). The
  cycle is simultaneously a power source *and* a parts depot for anabolism.

---

## The Electron Transport Chain — Pumping Protons

The ETC is four protein complexes embedded in the **inner mitochondrial membrane**.
Electrons from NADH and FADH2 are passed complex-to-complex, falling to
progressively lower energy, and at three of the complexes that energy **pumps
protons (H+) out of the matrix** into the intermembrane space.

```
+------------------------------------------------------------------------+
|  INNER MITOCHONDRIAL MEMBRANE (electrons flow LEFT-to-RIGHT, downhill) |
|                                                                        |
|   NADH                          FADH2                                  |
|    |                              |                                    |
|    v                              v                                    |
|  [ I ]---> Q --->[ III ]---> cyt c --->[ IV ]---> 1/2 O2 -> H2O        |
|    |        ^      |                     |                             |
|    |      [ II ]   |                     |                             |
|  PUMP H+   (no    PUMP H+              PUMP H+                         |
|            pump)                                                       |
|                                                                        |
|   Complex I  : NADH -> Q       (pumps H+)                              |
|   Complex II : FADH2 -> Q      (succinate DH; NO pumping)              |
|   Complex III: Q -> cyt c      (pumps H+)                              |
|   Complex IV : cyt c -> O2     (pumps H+; O2 is the FINAL acceptor)    |
|                                                                        |
|   This is WHY FADH2 yields less ATP than NADH: it enters at Cx II,     |
|   skipping Complex I's proton pump.                                    |
+------------------------------------------------------------------------+
```

Key points a rigorous reader will want pinned down:

- **Oxygen is the terminal electron acceptor.** At Complex IV, electrons combine
  with O2 and protons to form water. This is the *only* place O2 is used — which is
  why you breathe. No O2 -> the chain backs up -> NADH can't be reoxidized -> the
  TCA cycle stalls -> the cell falls back to fermentation. Oxygen's role is to be
  the electron sink at the bottom of the hill.
- **NADH enters at Complex I; FADH2 enters at Complex II.** FADH2 bypasses Complex
  I's proton pump, so it drives fewer protons across, so it yields **less ATP**.
  This single fact explains the ~2.5 vs ~1.5 ATP difference below.
- The electrons don't make ATP directly — they make a **proton gradient**. That's
  the whole trick.

---

## Chemiosmosis and ATP Synthase

The pumped protons create an electrochemical gradient — the **proton-motive force
(PMF)** — with two components: a chemical gradient (more H+ outside, a pH
difference) and an electrical gradient (positive charge outside). Protons "want" to
flow back into the matrix, and the only easy door back is through **ATP synthase
(Complex V)**.

```
+------------------------------------------------------------------------+
|   INTERMEMBRANE SPACE (HIGH H+, the filled reservoir)                  |
|   H+ H+ H+ H+ H+ H+ H+ H+ H+ H+ H+ H+ H+ H+ H+ H+ H+ H+                |
|        |                                      | |                      |
|        | (ETC pumped them up here)            v v  protons flow back   |
|        |                              .---------------.                |
|   =================================== |  ATP SYNTHASE |=============== |
|   inner membrane                      |   (a turbine) |    matrix      |
|                                       |   c-ring spins|                |
|                                       '---------------'                |
|                                              |                         |
|   MATRIX (low H+)                            v                         |
|                                       ADP + Pi -> ATP                  |
|                                                                        |
|   ~4 protons through the turbine  ->  1 ATP made                       |
|   (about 3 to spin the rotor + 1 to import Pi/export ATP)              |
+------------------------------------------------------------------------+
```

ATP synthase is a literal **rotary motor**. Protons flowing through its membrane-
embedded c-ring make it spin (like water through a turbine); the rotation
mechanically drives conformational changes in the catalytic head that squeeze ADP +
Pi together into ATP. Boyer and Walker won a Nobel for showing it's a rotating
molecular machine — one of the few cases where a protein literally turns.

This is the **chemiosmotic coupling** that confused everyone for a decade:
"burning fuel" (ETC, electron flow) and "making ATP" (synthase) are **two separate
machines** linked only by the proton gradient between them. That decoupling is also
exploitable: **uncouplers** (e.g., the poison DNP, or the natural protein UCP1 in
brown fat) punch a hole in the membrane so protons leak back *without* going through
the synthase — energy then dissipates as heat instead of ATP. Brown fat does this
deliberately for thermogenesis (a link to `human-biology/` / `nutrition/`).

---

## The ATP Ledger — Why ~30–32, Not 36–38

Here is the careful accounting. The modern consensus stoichiometry:

```
   1 NADH  ->  ~2.5 ATP    (older texts said 3)
   1 FADH2 ->  ~1.5 ATP    (older texts said 2)
   1 GTP   =   1 ATP       (made directly in the cycle)
```

These are **non-integer** because ATP synthase needs ~4 protons per ATP and the
complexes pump a non-integer number of protons per electron pair. Building the
ledger per glucose:

```
+------------------------------------------------------------------------+
|   STAGE                  YIELDS              ATP EQUIVALENT            |
|   -----                  ------              --------------            |
|   Glycolysis             2 ATP               = 2.0                     |
|                          2 NADH (cytosolic)  = ~3.0 to 5.0 *           |
|   Pyruvate -> AcCoA       2 NADH              = 5.0  (2 x 2.5)         |
|   TCA cycle (x2 turns)   6 NADH              = 15.0 (6 x 2.5)          |
|                          2 FADH2             = 3.0  (2 x 1.5)          |
|                          2 GTP               = 2.0                     |
|   ---------------------------------------------------------------------|
|   TOTAL                                      = ~30 to 32 ATP           |
|                                                                        |
|   * The 2 cytosolic NADH must be SHUTTLED into the mitochondrion.      |
|     - Glycerol-phosphate shuttle: each becomes FADH2 -> ~1.5 ATP each  |
|       -> ~3 ATP total -> grand total ~30 ATP                           |
|     - Malate-aspartate shuttle:   each stays NADH -> ~2.5 ATP each     |
|       -> ~5 ATP total -> grand total ~32 ATP                           |
+------------------------------------------------------------------------+
```

**Why the old 36–38 figure was wrong:** older textbooks assumed clean integers
(3 ATP/NADH, 2 ATP/FADH2) and ignored the energetic cost of the NADH shuttle and of
transporting ATP/Pi across the membrane. When the actual proton stoichiometry of
ATP synthase was measured (~4 H+/ATP) and the shuttle and transport costs were
counted, the realistic number dropped to **~30–32**. The exact figure depends on
which NADH shuttle a given tissue uses (heart/liver favor malate-aspartate -> ~32;
muscle/brain often use glycerol-phosphate -> ~30). State it as a range; biology
does not produce a clean integer.

| Era | NADH | FADH2 | Glucose total | Why |
|---|---|---|---|---|
| **Old textbook** | 3 ATP | 2 ATP | 36–38 | assumed integer ratios, ignored costs |
| **Modern consensus** | ~2.5 | ~1.5 | **~30–32** | measured H+/ATP, shuttle + transport costs |

---

## Old World → New World Bridge

| Software / systems concept | Ox-phos concept |
|---|---|
| Dam + turbine (stored head -> power) | Proton gradient (PMF) + ATP synthase |
| Energy stored as potential, not in a part | Energy in the gradient, not a chemical bond |
| Decoupled producer / consumer via a buffer | ETC and synthase coupled only by the H+ pool |
| Rotary motor / spinning rotor | ATP synthase literally rotates |
| Terminal sink in a pipeline | O2 as final electron acceptor |
| Leaky buffer wasting throughput as heat | Uncouplers (DNP, UCP1) -> heat not ATP |
| Honest vs. idealized perf numbers | ~30–32 (measured) vs 36–38 (idealized) |

---

## Decision Cheat Sheet

| Question | Answer |
|---|---|
| TCA per turn | 3 NADH + 1 FADH2 + 1 GTP + 2 CO2 |
| TCA per glucose (2 turns) | 6 NADH + 2 FADH2 + 2 GTP + 4 CO2 |
| Where TCA runs | Mitochondrial matrix |
| What the cycle's real product is | Reducing power (NADH/FADH2), not ATP |
| ATP per NADH (modern) | **~2.5** |
| ATP per FADH2 (modern) | **~1.5** |
| Why FADH2 < NADH | Enters at Complex II, skips Complex I's pump |
| Final electron acceptor | O2 (-> water, at Complex IV) |
| How ATP synthase works | Proton flow spins a rotor (chemiosmosis) |
| Total ATP per glucose | **~30–32** (NOT 36–38) |
| Why not 36–38 | ~4 H+/ATP, plus shuttle + transport costs |
| What uncouplers do | Leak protons -> heat, not ATP (brown fat) |

---

## Common Confusion Points

### "Is it 36–38 or 30–32 ATP per glucose?"

The modern, measured answer is **~30–32**. The 36–38 figure persists in old
textbooks and assumed clean integer yields (3 ATP/NADH, 2 ATP/FADH2) while ignoring
the cost of shuttling cytosolic NADH and transporting ATP across the membrane. Use
~30–32, and quote it as a range — the exact value depends on the NADH shuttle the
tissue uses.

### "Does the electron transport chain make ATP?"

No — directly, it makes a **proton gradient**. ATP is made separately by ATP
synthase using that gradient. This separation (chemiosmosis) is the whole point:
the ETC and the synthase are distinct machines coupled only through the membrane's
proton reservoir. That's why you can poison one without the other and why
uncouplers can dissipate the gradient as heat.

### "Why does the cycle make so little ATP itself?"

Because the TCA cycle is a **fuel-prep stage**, not the power plant. It makes only
1 GTP directly per turn; its valuable output is the 3 NADH + 1 FADH2, which carry
electrons to the ETC where the real ATP is generated. Roughly 90% of a glucose's ATP
comes from oxidative phosphorylation, not from any substrate-level step.

### "Why is oxygen necessary if it never touches the ATP?"

Oxygen is the **electron sink** at the bottom of the chain (Complex IV). Without it,
electrons have nowhere to go, the chain backs up, NADH can't be reoxidized to NAD+,
and both the TCA cycle and (eventually) glycolysis stall. O2 enables the entire
electron flow indirectly — you breathe to keep the bottom of the waterfall open.

### "Three names — TCA, citric acid, Krebs — same thing?"

Yes. **TCA cycle** (tricarboxylic acid), **citric acid cycle**, and **Krebs cycle**
are three names for the identical pathway. "Citric acid" names the first
intermediate; "Krebs" honors Hans Krebs, who worked it out; "TCA" describes the
tri-acid chemistry. Pick one and move on.
