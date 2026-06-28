---
maxim_schema: maxim.frontmatter.v1
id: maxim:biochemistry:photosynthesis-and-carbon
kind: guide
module: biochemistry
section: biochemistry
title: Photosynthesis and Carbon Fixation
status: source-custody
source_custody: partial
current_path: biochemistry/08-PHOTOSYNTHESIS-AND-CARBON.md
canonical_path: biochemistry/08-PHOTOSYNTHESIS-AND-CARBON.md
backsource_ids: [proof-backfill:biochemistry:08-photosynthesis-and-carbon, git-history:biochemistry:08-photosynthesis]
concepts: [photosynthesis, light reactions, Calvin cycle, carbon fixation, C4, CAM, RuBisCO]
root_concepts: [photosynthesis]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Photosynthesis and Carbon Fixation — Running the Engine in Reverse

```
+------------------------------------------------------------------------+
|        PHOTOSYNTHESIS = OXIDATIVE PHOSPHORYLATION, BACKWARD            |
|                                                                        |
|   LIGHT REACTIONS (thylakoid membrane)  "convert photons to currency"  |
|   .------------------------------------------------------------.       |
|   |  sunlight + H2O                                            |       |
|   |     | photosystems split water, excite electrons          |        |
|   |     v                                                      |       |
|   |  electron transport -> PROTON GRADIENT -> ATP synthase     |       |
|   |     | also reduce NADP+ -> NADPH                           |       |
|   |     v                                                      |       |
|   |  outputs: ATP, NADPH    waste: O2 (from split water!)      |       |
|   '------------------------------------------------------------'       |
|                          |  ATP + NADPH                                |
|                          v                                             |
|   CALVIN CYCLE / DARK REACTIONS (stroma)  "spend currency to build"    |
|   .------------------------------------------------------------.       |
|   |  CO2 + ATP + NADPH  --[RuBisCO + cycle]-->  SUGAR (G3P)    |       |
|   |  fixes inorganic carbon into organic molecules            |        |
|   '------------------------------------------------------------'       |
|                                                                        |
|   NET: 6 CO2 + 6 H2O + light -> C6H12O6 (glucose) + 6 O2               |
+------------------------------------------------------------------------+
```

Photosynthesis is the **mirror image of cellular respiration**. Where respiration
burns sugar with oxygen to make ATP and release CO2, photosynthesis uses light to
make ATP, then spends it to build sugar from CO2 — releasing O2 as a byproduct.
For a software reader, the symmetry is striking and the best entry point:

```
   RESPIRATION (file 06):   glucose + O2  ->  CO2 + H2O + ATP
   PHOTOSYNTHESIS:          CO2 + H2O + light  ->  glucose + O2
```

The two halves of photosynthesis split cleanly:

- **Light reactions** — the *energy-capture* half. They use light to make ATP and
  NADPH, and split water (the source of the O2 you breathe). Mechanically, they reuse
  the *exact same chemiosmotic machinery* as file 06: an electron transport chain, a
  proton gradient, and an ATP synthase.
- **Calvin cycle** ("dark reactions") — the *biosynthesis* half. It spends that ATP
  and NADPH to fix CO2 into sugar. It does **not** require darkness — it just doesn't
  directly use light; it runs whenever ATP/NADPH are available.

This is the directory's biggest **bridge to file 06**: photosynthesis is not a new
mechanism, it's the same chemiosmotic engine wired to run uphill, powered by photons
instead of by burning fuel.

---

## The Light Reactions — Photons to Currency

Light reactions happen in the **thylakoid membrane** of the chloroplast. Two
**photosystems** (PSII and PSI) absorb light via chlorophyll, boosting electrons to
high energy. The electrons flow down a transport chain, pumping protons and reducing
NADP+ to NADPH along the way.

```
+------------------------------------------------------------------------+
|   THYLAKOID MEMBRANE — the "Z-scheme" of electron flow                 |
|                                                                        |
|   H2O --> [PHOTOSYSTEM II] --> [cyt b6f] --> [PHOTOSYSTEM I] --> NADPH |
|     |       ^ light              |             ^ light          ^      |
|     |       |                    | PUMP H+     |                |      |
|   SPLIT WATER:                   v             '--- re-excite          |
|   2 H2O -> O2 + 4 H+ + 4 e-   proton gradient      electrons           |
|     |                              |                                   |
|     '--> O2 is RELEASED            v                                   |
|         (the oxygen we breathe)  [ATP SYNTHASE] -> ATP                 |
|                                  protons flow back, spin the rotor     |
|                                                                        |
|   "Z-scheme": electrons get boosted TWICE (PSII then PSI) because      |
|   one photon isn't enough to go from water all the way to NADPH.       |
+------------------------------------------------------------------------+
```

Three facts to lock down:

1. **Water is the electron source, and O2 is the waste.** PSII rips electrons off
   water to replace the ones it lost to light. Splitting water releases O2 — the
   atmospheric oxygen that all aerobic life (including file 06's electron transport)
   depends on. **Every O2 molecule you've ever breathed came from photosynthesis
   splitting water.**
2. **Same chemiosmosis as respiration.** Electron flow pumps protons across the
   thylakoid membrane; the gradient drives an ATP synthase identical in principle to
   the mitochondrial one (file 06). This step is called **photophosphorylation** —
   chemiosmosis powered by light.
3. **The Z-scheme boosts electrons twice.** Going from water (a poor electron donor)
   all the way up to NADPH takes more energy than one photon provides, so two
   photosystems in series give the electrons two energy kicks.

| | Respiration (file 06) | Light reactions |
|---|---|---|
| Energy source | electrons from fuel (NADH) | photons (light) |
| Electron flow direction | downhill (fuel -> O2) | uphill (water -> NADPH), boosted by light |
| Terminal acceptor | O2 (-> water) | NADP+ (-> NADPH) |
| Proton-driven product | ATP | ATP (+ NADPH) |
| O2 role | consumed (sink) | produced (from splitting water) |

---

## The Calvin Cycle — Fixing Carbon Into Sugar

The Calvin cycle runs in the **stroma** (the chloroplast's fluid). It spends ATP and
NADPH from the light reactions to convert inorganic CO2 into organic sugar. Three
phases: **fixation, reduction, regeneration.**

```
+------------------------------------------------------------------------+
|   CALVIN CYCLE (to make 1 net G3P, the cycle turns 3 times,            |
|                 fixing 3 CO2)                                          |
|                                                                        |
|   1. FIXATION:  3 CO2 + 3 RuBP (5C) --[RuBisCO]--> 6x 3-PGA (3C)       |
|                 (RuBisCO is the slow, abundant key enzyme)             |
|        |                                                               |
|        v                                                               |
|   2. REDUCTION: 6x 3-PGA + 6 ATP + 6 NADPH -> 6x G3P (3C)              |
|        |        (this is where the captured energy is spent)           |
|        |                                                               |
|        +--> 1 G3P EXITS  (the net product -> glucose, starch)          |
|        |                                                               |
|        v   5 G3P remain                                                |
|   3. REGENERATION: 5x G3P + 3 ATP -> 3 RuBP   (reset the cycle)        |
|                                                                        |
|   PER net G3P: 3 CO2 + 9 ATP + 6 NADPH consumed                        |
|   (2 net G3P = 1 glucose, so 1 glucose costs 18 ATP + 12 NADPH)        |
+------------------------------------------------------------------------+
```

The star enzyme is **RuBisCO** (ribulose-1,5-bisphosphate carboxylase/oxygenase) —
the most abundant protein on Earth, and the gatekeeper that fixes CO2 onto the
5-carbon acceptor RuBP. RuBisCO is famously **slow** (a few reactions per second —
file 03's kcat at the low end) and **error-prone**, which sets up the entire C4/CAM
story below.

Note the analogy to gluconeogenesis (file 05): the Calvin cycle is **anabolism**,
spends ATP **and NADPH** (the anabolic carrier, file 00/04), and is regulated to run
when the light reactions are active — exactly the catabolic/anabolic separation the
directory has stressed throughout.

---

## Photorespiration — RuBisCO's Bug

RuBisCO has a costly flaw: it can grab **O2 instead of CO2** (it's a
carboxyl*ase* and an oxygen*ase* — hence the name). When O2 wins, the cycle runs a
wasteful salvage pathway called **photorespiration** that consumes energy and
releases CO2 — undoing photosynthesis.

```
+------------------------------------------------------------------------+
|   RuBisCO's two reactions (it can't tell CO2 from O2 perfectly)        |
|                                                                        |
|   RuBP + CO2  -> 2x 3-PGA          (productive: carbon FIXED)          |
|   RuBP + O2   -> 3-PGA + glycolate (wasteful: PHOTORESPIRATION)        |
|                                                                        |
|   PROBLEM WORSENS when:                                                |
|   - hot/dry -> plant closes stomata to save water                      |
|   - CO2 inside drops, O2 (from light reactions) builds up              |
|   - O2/CO2 ratio rises -> RuBisCO grabs more O2 -> more waste          |
+------------------------------------------------------------------------+
```

Photorespiration is a genuine inefficiency — an evolutionary holdover from when the
atmosphere had little O2 and RuBisCO never had to discriminate. It is the design
bug that C4 and CAM plants engineer around.

---

## C3 vs C4 vs CAM — Three Carbon Strategies

The fixes for photorespiration are **separation strategies** — keep CO2 high and O2
low around RuBisCO, either by *space* (C4) or by *time* (CAM).

```
+------------------------------------------------------------------------+
|   C3 (default)    fix CO2 directly with RuBisCO. Simple, but           |
|                   photorespires in heat. ~85% of plant species.        |
|                   (wheat, rice, most trees)                            |
|                                                                        |
|   C4 (spatial)    pre-fix CO2 into a 4-carbon acid (via PEP            |
|                   carboxylase, which ignores O2) in one cell type,     |
|                   then ship it to a sealed inner cell where RuBisCO    |
|                   runs in a CO2-rich, O2-poor pocket. Costs extra ATP  |
|                   but avoids photorespiration. (corn, sugarcane)       |
|                                                                        |
|   CAM (temporal)  open stomata only AT NIGHT (cool, humid) to fix CO2  |
|                   into acid; store it; by day, stomata shut and the    |
|                   stored CO2 feeds RuBisCO. Saves water. (cacti,       |
|                   succulents, pineapple)                               |
+------------------------------------------------------------------------+
```

| Strategy | Separation | Initial CO2 fixer | Wins at | Cost | Example |
|---|---|---|---|---|---|
| **C3** | none | RuBisCO | cool, wet, normal CO2 | cheapest | wheat, rice |
| **C4** | spatial (2 cell types) | PEP carboxylase | hot, sunny | extra ATP | corn, sugarcane |
| **CAM** | temporal (night vs day) | PEP carboxylase | hot, arid | extra ATP | cacti, pineapple |

The shared engineering trick: **PEP carboxylase**, an enzyme that fixes CO2 without
the O2-confusion problem RuBisCO has, acts as a CO2-concentrating front end. C4 and
CAM both use it to pump CO2 up around RuBisCO — they differ only in whether the
separation is in **space** (different cells) or **time** (night vs day). The systems
reading: both are **caching / staging layers** that feed a high-purity input to a
slow, picky downstream consumer (RuBisCO) so it doesn't make mistakes — a buffer
that batches and filters input for an expensive stage.

---

## Old World → New World Bridge

| Software / systems concept | Photosynthesis concept |
|---|---|
| Same engine wired to run in reverse | Photosynthesis reuses chemiosmosis (file 06) |
| Charge a battery, then spend it | Light reactions (ATP/NADPH) -> Calvin cycle |
| Producer of a global dependency | O2 from water-splitting feeds all aerobic life |
| Two boost stages in a pipeline | Z-scheme: PSII then PSI re-excite electrons |
| A slow, error-prone hot component | RuBisCO (slow, confuses CO2 with O2) |
| Caching/staging to protect a slow stage | C4/CAM concentrate CO2 around RuBisCO |
| Spatial vs temporal sharding | C4 (different cells) vs CAM (night vs day) |
| Legacy bug from old assumptions | Photorespiration (low-O2-era holdover) |

---

## Decision Cheat Sheet

| Question | Answer |
|---|---|
| Overall equation | 6 CO2 + 6 H2O + light -> C6H12O6 + 6 O2 |
| Where light reactions run | Thylakoid membrane |
| Where the Calvin cycle runs | Stroma |
| What the light reactions produce | ATP + NADPH (and O2 as waste) |
| Source of the released O2 | Splitting water (not from CO2!) |
| Do "dark reactions" need darkness | No — they just don't directly use light |
| Key Calvin-cycle enzyme | RuBisCO (most abundant protein on Earth) |
| Cost per glucose (Calvin) | 18 ATP + 12 NADPH |
| What photorespiration is | RuBisCO grabbing O2 -> wasteful salvage |
| C4 vs CAM difference | C4 separates by space; CAM by time |
| Front-end CO2 fixer in C4/CAM | PEP carboxylase (ignores O2) |

---

## Common Confusion Points

### "Do the dark reactions happen at night?"

No — a misleading name. The **Calvin cycle** is called "dark" only because it
doesn't *directly* use light. It runs **during the day**, fueled by the ATP and
NADPH the light reactions are producing right then. At night those run out and the
cycle stops. The better name is "light-independent reactions," and even that is
loose — they depend on light-made products. (CAM plants are the genuine exception:
they fix CO2 at night and run the Calvin cycle by day.)

### "Where does the oxygen come from — CO2 or water?"

**From water.** The O2 released by photosynthesis comes from splitting H2O in the
light reactions (Photosystem II), **not** from the CO2 that gets fixed into sugar.
This was proven with isotope-labeled water. The carbon of CO2 ends up in sugar; the
oxygen of water ends up in the air.

### "Is photosynthesis just respiration backwards?"

Conceptually yes (the overall equations are mirror images), and the **machinery is
genuinely shared** — both use an electron transport chain, a proton gradient, and an
ATP synthase (chemiosmosis). But the details differ: photosynthesis is powered by
light, splits water, produces O2 and NADPH, and runs in the chloroplast; respiration
is powered by fuel oxidation, consumes O2, produces NADH, and runs in the
mitochondrion. Same chemiosmotic chassis, opposite direction and inputs.

### "Why is RuBisCO so slow if it's so important?"

It's an evolutionary trade-off frozen in. RuBisCO arose when the atmosphere had
little O2, so distinguishing CO2 from O2 wasn't necessary, and it was never under
pressure to be fast. It's now the rate-limiting bottleneck of plant growth — which
is why plants compensate by making *enormous* amounts of it (the most abundant
protein on Earth) and why C4/CAM plants evolved CO2-concentrating workarounds. A
slow, ubiquitous, irreplaceable legacy component — every large codebase has one.
