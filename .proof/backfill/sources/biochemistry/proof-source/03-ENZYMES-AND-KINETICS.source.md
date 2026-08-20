---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "03-ENZYMES-AND-KINETICS.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:biochemistry:enzymes-and-kinetics
kind: guide
module: biochemistry
section: biochemistry
title: Enzymes and Kinetics
status: source-custody
source_custody: partial
current_path: biochemistry/03-ENZYMES-AND-KINETICS.md
canonical_path: biochemistry/03-ENZYMES-AND-KINETICS.md
backsource_ids: [proof-backfill:biochemistry:03-enzymes-and-kinetics, git-history:biochemistry:03-enzymes-and-kinetics]
concepts: [enzymes, catalysis, michaelis-menten, inhibition, allostery, kinetics]
root_concepts: [enzymes]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Enzymes and Kinetics — Catalysis and Control

```
+------------------------------------------------------------------------+
|                    WHAT AN ENZYME DOES                                 |
|                                                                        |
|   FREE ENERGY                                                          |
|     ^                                                                  |
|     |          uncatalyzed                                             |
|     |            .---.    <- high activation barrier (Ea)              |
|     |           /     \                                                |
|     |          /  .-.  \   catalyzed (enzyme lowers the barrier)       |
|     |         /  /   \  \                                              |
|     |   S ---'  /     \  '--- (same start)                             |
|     |          /       \                                               |
|     |         '         '------- P (same end, SAME deltaG)             |
|     |                                                                  |
|     +-------------------------------------> reaction coordinate        |
|                                                                        |
|  KEY: enzymes lower ACTIVATION energy (speed), NOT deltaG (direction). |
|        They change HOW FAST equilibrium is reached, not WHERE it is.   |
+------------------------------------------------------------------------+
```

An enzyme is a **biological catalyst** — almost always a protein (a few are RNA).
It speeds a specific reaction by factors of 10^6 to 10^17 without being consumed.
The mental model: an enzyme is a **hardware accelerator**. It doesn't change what
the result is (thermodynamics, ΔG, fixes the destination); it changes how fast you
get there by lowering the **activation energy** — the cost of reaching the
transition state.

This distinction is the crux of the file: **ΔG (file 00) says which way a reaction
*can* go and how far; the enzyme says how *fast*.** A reaction with ΔG > 0 will
not run no matter how good the enzyme — you have to couple it to ATP first. The
enzyme only accelerates reactions that are already thermodynamically allowed.

---

## Old World → New World Bridge

| Software / systems concept | Enzyme concept |
|---|---|
| Hardware accelerator (GPU, ASIC) | Enzyme: same result, far faster |
| Cache that doesn't change the answer | Catalysis lowers cost, not outcome |
| API contract (specific input type) | Substrate specificity (active site shape) |
| Hot path / bottleneck step | Rate-limiting (committed) step |
| Rate limiter on an endpoint | Vmax — saturation ceiling on throughput |
| Half-saturation tuning point | Km — substrate level at half-max rate |
| Throttle config, feature flag | Allosteric activator/inhibitor |
| Competitive lock contention | Competitive inhibition (raise input, win) |
| Poison pill that can't be outcompeted | Non-competitive / irreversible inhibition |
| Negative feedback control loop | Feedback (end-product) inhibition |

---

## How Catalysis Works — The Active Site

```
+------------------------------------------------------------------------+
|   ENZYME (E) + SUBSTRATE (S)  ->  ES complex  ->  E + PRODUCT (P)      |
|                                                                        |
|        .-------.                .-------.              .-------.       |
|       /  active \   S binds    /  E::S   \   reaction /  empty  \      |
|      |   site    | =========> |  induced  | ========>|  active   |     |
|       \  (cleft) /             \   fit    /            \  site   /     |
|        '-------'                '-------'              '-------'       |
|                                                                        |
|   The enzyme is UNCHANGED at the end — ready for the next substrate.   |
+------------------------------------------------------------------------+
```

The **active site** is a small pocket whose shape and chemistry are complementary
not to the substrate but to the **transition state** — the strained, halfway
configuration. By stabilizing that fleeting state, the enzyme lowers the barrier.
Catalytic tricks include: bringing reactants into proximity and correct
orientation, providing acid/base groups (Histidine is the favorite, pKa ~6),
forming temporary covalent intermediates, and straining the substrate toward the
transition state. The **induced-fit** model: substrate binding reshapes the
enzyme slightly to grip and strain it — not a rigid lock-and-key but a clamp.

Many enzymes need helpers: **cofactors** (metal ions like Zn2+, Mg2+) and
**coenzymes** (organic, often vitamin-derived — NAD+ from niacin, FAD from
riboflavin, coenzyme A from pantothenate). This is the chemistry link to
`nutrition/`: vitamins are largely coenzyme precursors.

---

## Michaelis-Menten Kinetics — The Core Model

This is the load-bearing quantitative model of the file. Consider one enzyme, one
substrate:

```
              k1        kcat
   E + S  <======>  ES  -----> E + P
              k-1
```

Measure the **initial reaction rate (v0)** at increasing substrate
concentration [S]. You get a **rectangular hyperbola**:

```
   v0
    ^
 Vmax|- - - - - - - - - .===================  (saturation plateau)
    |                .-'
    |             .-'
Vmax/2|- - - - .-+ - - - - - - - -            (half-max at [S] = Km)
    |       .' :
    |     .'   :
    |   .'     :
    |  /       :
    +-/--------+---------------------> [S]
              Km
```

The **Michaelis-Menten equation**:

```
            Vmax * [S]
   v0  =  --------------
             Km + [S]
```

Three parameters, each with a precise meaning:

| Parameter | Definition | Intuition |
|---|---|---|
| **Vmax** | max rate when enzyme is fully saturated | the throughput ceiling — every enzyme busy |
| **Km** | [S] at which v0 = Vmax/2 | inverse affinity: **low Km = tight binding** |
| **kcat** | turnover number = Vmax / [E]total | reactions per enzyme per second |

**Reading the curve like a systems engineer:**
- At **low [S]** (`[S] << Km`): rate is roughly proportional to [S] — first-order,
  enzyme is starved, like an underloaded server scaling linearly with requests.
- At **high [S]** (`[S] >> Km`): rate approaches Vmax — zero-order, saturated,
  every enzyme is busy. Adding more substrate doesn't help. This is a **throughput
  ceiling**, exactly like a request queue hitting max concurrency.
- **Km is the half-saturation point** — the substrate concentration where you're
  running at 50% capacity. It is *not* a rate; it has units of concentration.

**kcat/Km** is the **catalytic efficiency** — how good the enzyme is at low
substrate. An enzyme with kcat/Km near the diffusion limit (~10^8–10^9 M^-1 s^-1)
is "catalytically perfect": it reacts essentially every time a substrate diffuses
in (e.g., catalase, triose phosphate isomerase).

### Lineweaver-Burk — the linearization

The hyperbola is awkward to fit by eye (Vmax is an asymptote you never quite
reach). The **Lineweaver-Burk plot** is the classic linearization: take the
reciprocal of both sides.

```
    1       Km     1        1
   ---  =  ---- * ---  +  ------
    v0     Vmax   [S]     Vmax

   plot 1/v0  (y)   vs   1/[S]  (x)   ->  a straight line:

   1/v0
    ^
    |        .
    |      .'
    |    .'    slope = Km / Vmax
    |  .'
    |.'  y-intercept = 1/Vmax
  --+----------------> 1/[S]
   /:
  / : x-intercept = -1/Km
```

| Plot feature | Reads out |
|---|---|
| y-intercept | 1 / Vmax |
| x-intercept | -1 / Km |
| slope | Km / Vmax |

It's a double-reciprocal transform that turns the hyperbola into a line so you can
read Vmax and Km off the axes. (Modern practice fits the hyperbola directly with
nonlinear regression — the reciprocal amplifies error at low [S] — but
Lineweaver-Burk is still the standard way to *visualize* and to classify
inhibition, below.)

---

## Inhibition — Three Patterns

Inhibitors slow enzymes. The three classic reversible types are distinguished by
**how they shift Km and Vmax** — which is exactly what the Lineweaver-Burk plot
makes visible.

```
+------------------------------------------------------------------------+
|   COMPETITIVE          NON-COMPETITIVE        UNCOMPETITIVE            |
|   -----------          ---------------        -------------            |
|   binds the ACTIVE     binds ELSEWHERE        binds only the ES        |
|   SITE; competes with  (allosteric); works    COMPLEX (not free E)     |
|   substrate            even when S is bound                            |
|                                                                        |
|   Km : INCREASES       Km : unchanged         Km : DECREASES           |
|        (apparent)                                                      |
|   Vmax: UNCHANGED      Vmax: DECREASES         Vmax: DECREASES         |
|   (outcompete w/ S)    (can't outrun it)      (both drop together)     |
|                                                                        |
|   "more requests win"  "poisoned servers"     "traps busy servers"     |
+------------------------------------------------------------------------+
```

| Type | Binds | Effect on Km | Effect on Vmax | Beaten by more [S]? |
|---|---|---|---|---|
| **Competitive** | active site (vs substrate) | increases | unchanged | yes |
| **Non-competitive** | separate site, E or ES | unchanged | decreases | no |
| **Uncompetitive** | ES complex only | decreases | decreases | no |
| **Irreversible** | covalent, permanent | — | kills enzyme | no |

The systems reading: a **competitive inhibitor is lock contention** — flood the
system with substrate and you win the race, so Vmax is unchanged but you need more
substrate (higher apparent Km) to get there. A **non-competitive inhibitor is a
degraded server** — it lowers the ceiling (Vmax drops) no matter how much
substrate you throw at it. This is the basis of much of `pharmacology/`: many
drugs are deliberately designed enzyme inhibitors (statins competitively inhibit
HMG-CoA reductase; aspirin irreversibly acetylates cyclooxygenase).

---

## Allostery — Regulation as Feedback Control

Allosteric enzymes have a **regulatory site separate from the active site**.
Binding a regulator there changes the active site's shape, tuning activity up or
down. These enzymes typically have **multiple subunits** and show **cooperativity**
— a sigmoidal (S-shaped) curve instead of the hyperbola.

```
+------------------------------------------------------------------------+
|   SIGMOIDAL KINETICS (allosteric, cooperative)                         |
|                                                                        |
|   v0                          .===========                             |
|    ^                       .-'                                         |
|    |                     .'    <- steep switch region:                 |
|    |                   .'         small [S] change -> big rate change  |
|    |                 .'                                                |
|    |              .-'                                                  |
|    |   _____...--'   <- low activity until threshold                   |
|    +-------------------------------> [S]                               |
|                                                                        |
|   ACTS LIKE A SWITCH, not a dimmer. Compare hemoglobin O2 binding.     |
+------------------------------------------------------------------------+
```

```
+------------------------------------------------------------------------+
|   FEEDBACK (END-PRODUCT) INHIBITION                                    |
|                                                                        |
|   A --[E1]--> B --[E2]--> C --[E3]--> D --[E4]--> END PRODUCT          |
|   ^                                                   |                |
|   |                                                   |                |
|   '----------- inhibits E1 (the committed step) <-----'                |
|                                                                        |
|   When END PRODUCT is plentiful, it shuts down the FIRST committed     |
|   step -> the cell stops making what it already has. Negative          |
|   feedback. The setpoint is "enough product."                          |
+------------------------------------------------------------------------+
```

This is **negative feedback control**, drawn straight from control theory. The end
product of a pathway allosterically inhibits the **first committed enzyme** —
shutting the pathway off when supply meets demand, and turning it back on when the
product is consumed. Inhibiting the *committed* step (rather than a later one)
avoids wasting intermediates: you don't start the assembly line if you can't sell
the product.

**Two models of cooperativity** (worth a line for a rigorous reader): the
**concerted (MWC)** model says all subunits flip together between a tense (T,
low-affinity) and relaxed (R, high-affinity) state; the **sequential (KNF)** model
says each subunit changes one at a time. Real enzymes lie somewhere between. The
takeaway either way: **cooperativity converts a graded input into a switch-like
output** — a sharper, more decisive controller than simple Michaelis-Menten.

### Covalent modification — the other regulation knob

Besides allostery (reversible binding), enzymes are toggled by **covalent
modification** — most importantly **phosphorylation**. A kinase adds a phosphate;
a phosphatase removes it. The phosphate flips the enzyme on or off. This is a
**config patch applied at runtime**, and it's the substrate of signal cascades in
file 09.

---

## Decision Cheat Sheet

| Question | Answer |
|---|---|
| Does an enzyme change ΔG / equilibrium? | No — only the rate (activation energy) |
| What is Vmax? | Throughput ceiling at substrate saturation |
| What is Km? | [S] at half-Vmax; **low Km = high affinity** |
| What is kcat? | Turnover number (reactions/enzyme/sec) |
| Best single efficiency measure? | kcat/Km (catalytic efficiency) |
| How to read Vmax/Km off a plot | Lineweaver-Burk: y-int=1/Vmax, x-int=-1/Km |
| Inhibitor beaten by more substrate? | Competitive only |
| Inhibitor that lowers Vmax, leaves Km | Non-competitive |
| How a pathway self-regulates | Feedback inhibition of the committed step |
| Switch-like (sigmoidal) response | Allosteric cooperativity |
| Fast reversible on/off toggle | Phosphorylation (covalent modification) |

---

## Common Confusion Points

### "Low Km means weak binding, right?"

Backwards — a frequent slip. **Low Km = tight binding (high affinity).** Km is the
substrate concentration needed to reach half-max rate; if you only need a tiny
amount of substrate to get halfway, the enzyme grabs it eagerly. High Km means you
need a lot of substrate, i.e., loose binding.

### "Competitive vs. non-competitive — which can I overpower?"

```
  COMPETITIVE     fights for the active site  -> add more substrate, you WIN
                  (Vmax recoverable, Km rises)
  NON-COMPETITIVE binds elsewhere, no contest -> can't outrun it
                  (Vmax falls and stays fallen)
```

If flooding the system with substrate restores full speed, it's competitive. If
the ceiling drops permanently, it's non-competitive.

### "Why inhibit the FIRST step of a pathway, not the slow one?"

To avoid wasting raw material. Inhibiting the **first committed step** stops the
cell from pouring precursors into intermediates it will never finish. It's the
biochemical version of failing fast at the entry point rather than deep in the
pipeline after you've already spent resources.

### "Does an enzyme get used up?"

No. The enzyme returns to its original state after each reaction (it's a catalyst).
A handful of enzyme molecules can process an enormous amount of substrate — kcat
values run from ~1 to ~10^6 reactions per second per enzyme. The enzyme is reusable
infrastructure; the substrate is the throughput.
