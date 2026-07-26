---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "03-HEMODYNAMIC-DISORDERS-THROMBOSIS-AND-SHOCK.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:pathology:hemodynamic-disorders-thrombosis-and-shock
kind: guide
module: pathology
section: pathology
title: Hemodynamic Disorders, Thrombosis, and Shock
status: source-custody
source_custody: partial
current_path: pathology/03-HEMODYNAMIC-DISORDERS-THROMBOSIS-AND-SHOCK.md
canonical_path: pathology/03-HEMODYNAMIC-DISORDERS-THROMBOSIS-AND-SHOCK.md
backsource_ids: [mdloom-backfill:pathology:03-hemodynamic-disorders-thrombosis-and-shock]
concepts: [edema-congestion, hemostasis, virchow-triad, thrombosis-embolism-infarction, shock]
root_concepts: [hemodynamics]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Hemodynamic Disorders, Thrombosis, and Shock

**This guide owns** the *mechanics of blood and fluid gone wrong*: normal fluid balance and
the mechanisms of **edema**; **hyperemia and congestion**; **hemostasis** as the normal
protective clotting program (primary platelet plug, secondary coagulation cascade, and the
anticoagulant controls that keep it local); **thrombosis** as that same program firing in the
wrong place, organized around **Virchow's triad**; the **fate of a thrombus**; **embolism**
(thromboembolic and the non-thrombotic embolus types as mechanisms); **infarction** as the
tissue consequence of vascular occlusion; and **shock** as the final common pathway of
circulatory failure, by class and by stage. **It builds on**
`01-CELL-INJURY-ADAPTATION-AND-DEATH` (ischemia → infarction is cell injury at tissue scale),
`02-INFLAMMATION-AND-TISSUE-REPAIR` (the transudate/exudate distinction; septic shock is
systemic inflammation), and `human-biology/`/`biochemistry/` (normal circulation, endothelium,
clotting-factor biology).

**It explicitly defers** the *clotting-factor and platelet biochemistry* (the molecular
cascade in full) to `biochemistry/` and `human-biology/`; the *disease entities* (deep-vein
thrombosis, pulmonary embolism, myocardial infarction, the specific bleeding and clotting
disorders) to `disease/`; the *laboratory measurement* of coagulation (how a clotting time is
generated and bounded) to `08-LABORATORY-MEDICINE`; and *drug action* (anticoagulants,
thrombolytics) to `pharmacology/`. Hemodynamics is owned here as a **tissue-level mechanism**,
not as a coagulation-biochemistry text, a disease list, or a treatment guide.

> **This module is an educational reference about *how pathology reasons about disease
> mechanism* — never medical advice. It does *not* interpret any reader's own results,
> images, or symptoms, does *not* diagnose, and gives *no* treatment, dosing, specimen, or
> bench instructions and *no* forensic/legal determinations. All cases are fictional teaching
> vignettes; all numbers are illustrative and, where a real standard is named, attributed and
> dated.**

*Per-guide banner: educational reference on hemodynamic mechanism — never self-diagnosis,
never personal-result interpretation, never a procedure, never forensic/legal advice. Disease
entities are named only to illustrate a mechanism; the catalog is `disease/`.*

---

## The Big Picture: The Circulation Is a Pressure/Flow/Volume System With a Self-Sealing Repair Layer

The novice mental model is "blood flows in tubes; clots are bad; bleeding is bad." The expert
model has two coupled control problems. The first is **fluid balance** — keeping the right
volume of fluid inside vessels against the forces trying to push it out, so that edema
(too much fluid in tissue) and congestion (too much blood pooled in vessels) are *control
failures* of the same system. The second is **hemostasis** — a self-sealing repair layer that
must clot *exactly enough, exactly where a vessel is breached, and nowhere else*. Thrombosis,
embolism, and infarction are what happen when the repair layer fires in the wrong place;
shock is what happens when the whole pressure/flow/volume system loses the ability to perfuse
tissue.

```
THE HEMODYNAMIC SYSTEM  (this guide owns both control problems)
==============================================================
  CONTROL PROBLEM 1: FLUID BALANCE            CONTROL PROBLEM 2: HEMOSTASIS
  ------------------------------              ----------------------------
  keep fluid IN vessels                       clot ONLY at a breach, ONLY enough
        |                                            |
  failure: EDEMA (fluid -> tissue)            failure A: BLEEDING (clot too little)
           CONGESTION (blood pools)           failure B: THROMBOSIS (clot wrong place)
                                                     |
                                              a thrombus can BREAK OFF -> EMBOLISM
                                                     |
                                              occlusion -> ISCHEMIA -> INFARCTION (see 01)

  SYSTEM-WIDE FAILURE: SHOCK
  perfusion fails everywhere -> cellular hypoxia -> (if unbroken) multi-organ death
```

Two facts organize the guide. First, **the same machinery is protective and pathological**:
hemostasis that seals a wound is the identical process that, misplaced, forms an occluding
thrombus — pathology here is almost always *the right mechanism in the wrong context*. Second,
**these disorders cascade**: a thrombus embolizes, an embolus occludes, an occlusion infarcts,
and widespread perfusion failure is shock — so the guide is best read as a **connected chain**,
not a set of independent topics.

**Bridge — a connection pool with an auto-reconnect that can deadlock.** Hemostasis is an
*auto-healing* layer: on a fault (vessel breach) it seals the connection locally. Thrombosis
is that auto-heal *triggering without a real fault or failing to stay local* — the pool fills
with half-open, occluding connections. An embolus is one of those bad connections *migrating
downstream* to block a resource it never belonged to. Shock is *total resource starvation* —
every consumer blocked waiting on a supply that can no longer be delivered.

---

## 1. Fluid Balance and Edema

Fluid movement across capillary walls is governed by a balance of forces (the Starling
principle): **hydrostatic pressure** pushes fluid *out* of vessels, **colloid osmotic
(oncotic) pressure** — set mainly by plasma proteins — pulls fluid *in*, and the lymphatics
drain the small net leak. **Edema** is the accumulation of excess fluid in the interstitium,
and it has a *small number of mechanistic causes*, each a specific derailment of that balance.

```
THE FOUR MECHANISMS OF EDEMA  (each is a broken term in the fluid balance)
==========================================================================
  (1) INCREASED HYDROSTATIC PRESSURE   too much "push out"
      (impaired venous return / volume overload) -> TRANSUDATE

  (2) DECREASED ONCOTIC PRESSURE       too little "pull in"
      (low plasma protein: loss or reduced synthesis) -> TRANSUDATE

  (3) INCREASED VASCULAR PERMEABILITY  the wall itself leaks
      (INFLAMMATION, see 02) -> EXUDATE

  (4) LYMPHATIC OBSTRUCTION            the drain is blocked
      (lymphedema; often protein-rich local fluid)
```

The four mechanisms are **increased hydrostatic pressure** (too much outward push — from
impaired venous return or volume overload), **reduced oncotic pressure** (too little inward
pull — from low plasma protein, whether lost or under-synthesized), **increased vascular
permeability** (the wall itself leaking — this is *inflammation*, owned mechanistically by
`02`), and **lymphatic obstruction** (the drain blocked). Two of these produce a protein-poor
**transudate** (a pressure/osmotic problem across intact vessels); the permeability route
produces a protein-rich **exudate** (active inflammation). This is the same
transudate/exudate discrimination `02` introduced, applied to why fluid left the vessel. The
*entities* that cause each — and their management — are `disease/` and `clinical-medicine/`.

---

## 2. Hyperemia and Congestion

Both terms describe **increased blood in a tissue**, but they differ by mechanism and are worth
separating precisely.

```
HYPEREMIA vs CONGESTION  (active inflow vs passive backup)
=========================================================
  HYPEREMIA (active)                   CONGESTION (passive)
  -----------------                    --------------------
  arteriolar dilation pulls MORE       impaired venous OUTFLOW; blood backs up
  blood IN                                    |
        |                              deoxygenated blood pools (bluish, cyanotic)
  oxygenated inflow (reddish)                 |
        |                              chronic congestion -> hypoxic injury,
  e.g., exercise, early inflammation   small hemorrhages, and eventual fibrosis
```

**Hyperemia** is an *active* process — arteriolar dilation increases inflow of oxygenated
blood (as in exercising muscle or an early inflamed site), and the tissue looks red.
**Congestion** is a *passive* process — impaired venous *outflow* backs deoxygenated blood up
into a tissue, which looks bluish (cyanotic). **Chronic passive congestion** matters most:
persistently pooled, poorly oxygenated blood causes low-grade hypoxic cell injury (`01`),
small hemorrhages that leave iron-pigment deposits (the hemosiderin of `01`), and eventually
**fibrosis** (`02`) — a slow, congestion-driven scarring whose organ-specific forms are
`disease/`. Active in, passive out: the mechanism is the whole distinction.

---

## 3. Hemostasis: The Normal Protective Program

**Hemostasis** is the tightly regulated process that stops bleeding at a site of vascular
injury — a defense program with an on-switch, an amplifier, and, crucially, brakes. It has two
coupled arms plus a regulatory layer.

```
HEMOSTASIS  (seal the breach — locally, proportionately, then stop)
===================================================================
  vessel injury exposes the subendothelium
        |
        v
  PRIMARY HEMOSTASIS  (platelets: the fast, temporary plug)
    adhesion  -> platelets stick to the exposed surface
    activation-> they change shape and release signals
    aggregation-> more platelets recruited -> soft PLATELET PLUG
        |
        v
  SECONDARY HEMOSTASIS  (coagulation cascade: the durable mesh)
    a proteolytic cascade converges on generating THROMBIN
    thrombin -> converts soluble fibrinogen into insoluble FIBRIN
    fibrin weaves through the platelet plug -> STABLE CLOT
        |
        v
  REGULATION + FIBRINOLYSIS  (keep it local; remove it later)
    natural anticoagulants confine the clot to the injury site;
    the fibrinolytic system later dissolves it during repair
```

**Primary hemostasis** builds a fast, temporary **platelet plug**: platelets *adhere* to the
exposed subendothelium, *activate* (change shape, release signals), and *aggregate* into a soft
plug. **Secondary hemostasis** stabilizes it: a **coagulation cascade** — a sequential
proteolytic amplifier — converges on generating **thrombin**, which converts soluble
**fibrinogen** into insoluble **fibrin** that weaves through the platelet plug to form a
stable clot. (The full factor-by-factor cascade is `biochemistry/`; the *laboratory
measurement* of clotting times is `08`; this guide owns the *program and its balance*.)

The decisive third element is **regulation**: **natural anticoagulant systems** confine the
clot to the injury site, and the **fibrinolytic system** later dissolves it during repair.
Endothelium is not a passive pipe — intact endothelium is *actively anti-thrombotic*, and
**injured or activated endothelium becomes pro-thrombotic**. Hemostasis is thus a **balance**
between pro- and anti-clotting forces, tipped locally and briefly toward clotting at a breach
and held anticoagulant everywhere else. Everything in the rest of the guide is that balance
tipping in the wrong place, the wrong amount, or the wrong extent.

---

## 4. Thrombosis and Virchow's Triad

**Thrombosis** is the formation of a clot (a **thrombus**) inside an intact vessel — hemostasis
firing *without* a hemorrhage to stop. Its predisposing conditions are captured by
**Virchow's triad** (Rudolf Virchow, mid-19th century), the single most useful mental model in
this guide: three categories of abnormality that promote pathologic clotting.

```
VIRCHOW'S TRIAD  (three routes to a thrombus; usually acting together)
======================================================================
                    ENDOTHELIAL INJURY
                    (damaged/activated vessel lining ->
                     the surface turns pro-thrombotic)
                          /            \
                         /              \
        ABNORMAL BLOOD FLOW  --------  HYPERCOAGULABILITY
        (stasis or turbulence:         (the blood itself is more
         clotting factors + platelets   prone to clot: inherited or
         pool; anticoagulants           acquired shifts in the
         wash out; endothelium          pro/anti-clotting balance)
         is activated)
```

**Endothelial injury** turns the vessel lining from anti-thrombotic to pro-thrombotic (the
dominant factor in arterial and cardiac thrombi). **Abnormal blood flow** — **stasis**
(sluggish flow) or **turbulence** — lets platelets and clotting factors contact the wall and
accumulate, washes out anticoagulants, and activates endothelium (the dominant factor in
venous thrombi). **Hypercoagulability** is a shift of the *blood itself* toward clotting,
whether inherited or acquired (the specific hereditary and acquired states are `disease/`).
The triad's power is that it is **exhaustive and additive**: almost every real predisposition
maps to one of the three vertices, and risk compounds when more than one is present. It is the
classic worked example of a *complete, orthogonal cause taxonomy* — the same discipline as
enumerating the independent failure modes of a system so none is missed.

Arterial/cardiac thrombi (high-flow, injury-driven) and venous thrombi (low-flow,
stasis-driven) differ in composition and appearance accordingly — a mechanism-driven
morphologic difference, with the specific clinical syndromes owned by `disease/`.

---

## 5. The Fate of a Thrombus

Once formed, a thrombus has **four possible fates**, and predicting them is pure mechanism.

```
FOUR FATES OF A THROMBUS
========================
  (1) PROPAGATION     the thrombus grows (accretes more platelets/fibrin) ->
                      may enlarge toward occlusion
  (2) EMBOLIZATION    part/all breaks free -> travels downstream (Section 6)
  (3) DISSOLUTION     fibrinolysis removes a fresh thrombus (older ones resist)
  (4) ORGANIZATION +  ingrowth of cells/vessels incorporates it into the wall;
      RECANALIZATION  new channels may re-establish some flow
```

A thrombus may **propagate** (grow toward occlusion), **embolize** (break loose and travel),
undergo **dissolution** by fibrinolysis (effective on *fresh* thrombi; older, cross-linked
ones resist — a mechanistic reason timing matters), or **organize and recanalize** (be
invaded by cells and vessels, incorporated into the wall, and partly re-channeled). The fate
is set by the thrombus's age, size, location, and the balance of pro- and anti-thrombotic
forces around it — the same variables from Section 3. This guide owns the fates as
*mechanisms*; the clinical decisions they drive are `clinical-medicine/`.

---

## 6. Embolism

An **embolus** is any intravascular mass — solid, liquid, or gas — carried by the blood to a
site distant from its origin, where it **lodges and occludes** a vessel too small to pass. The
overwhelming majority are **thromboemboli** (a detached thrombus), but the *category* is
defined by the mechanism (a migrating occluder), which is why several non-thrombotic embolus
types belong here.

```
EMBOLISM  (a migrating occluder; the destination is set by the plumbing)
========================================================================
  TYPE            SOURCE / NATURE               MECHANISTIC POINT
  ----            ---------------               -----------------
  thromboembolus  a detached thrombus           by far the most common
  fat             marrow/adipose after some     droplets occlude microvessels
                  injuries
  air / gas       gas enters the circulation    bubbles obstruct flow
  amniotic fluid  amniotic contents enter        a rare peripartum mechanism
                  maternal circulation
  --------------------------------------------------------------------
  DESTINATION LOGIC: an embolus lodges wherever the vessel first becomes
  too small to pass -> venous emboli tend toward the pulmonary circulation;
  arterial emboli travel to systemic end-organs. The route is set by where
  it starts and which way the blood flows.
```

The **destination is determined by the plumbing**: an embolus travels with the blood until it
reaches a vessel too small to pass, so *where it lodges is a function of where it started and
the direction of flow* — venous emboli tend to travel toward the pulmonary circulation, while
emboli originating on the arterial/systemic side travel to systemic end-organs. This is a
tidy, deterministic routing problem, and it is why the mechanism (a migrating occluder) is
taught separately from the specific clinical syndromes (which are `disease/`). The
non-thrombotic types (fat, gas, amniotic) are included because they share the mechanism, not
because this guide catalogs them clinically.

---

## 7. Infarction

An **infarct** is an area of **ischemic necrosis** caused by occlusion of the blood supply —
the tissue-scale consequence of Sections 4–6, and the direct continuation of the ischemia →
coagulative-necrosis mechanism from `01`. Occlusion (usually thrombotic or embolic) cuts
perfusion; the deprived tissue crosses the point of no return and dies.

```
TWO KINDS OF INFARCT  (the color encodes the vascular anatomy)
==============================================================
  WHITE (pale) INFARCT                 RED (hemorrhagic) INFARCT
  --------------------                 -------------------------
  arterial occlusion in a SOLID        occlusion in tissue with a DUAL supply
  organ with END-ARTERIAL supply       or COLLATERALS, or with venous occlusion,
        |                              or reperfusion into fragile dead tissue
  little collateral inflow ->                 |
  the dead zone stays pale             blood seeps into the loose/dead zone ->
                                       the infarct is red/hemorrhagic
```

Infarcts are classically **white (pale)** or **red (hemorrhagic)**, and the difference is
mechanistic: a **white** infarct occurs with arterial occlusion in a *solid organ with an
end-arterial supply* and few collaterals, so the dead zone stays pale; a **red** infarct
occurs where tissue has a *dual blood supply or collaterals*, in *loose* tissue, with *venous*
occlusion, or when blood **reperfuses** into a fragile dead zone, so blood seeps in and the
infarct is red. Whether an occlusion actually infarcts depends on the **anatomy of the supply**
(end-arterial vs collateralized), the **rate** of occlusion (slow occlusion may allow
collaterals to develop), the tissue's **vulnerability to hypoxia**, and the **oxygen content**
of the blood. These are the mechanistic modifiers; the specific infarct syndromes by organ are
`disease/`.

---

## 8. Shock: The Final Common Pathway

**Shock** is a state of **systemic hypoperfusion** — circulatory failure so widespread that
tissue oxygen delivery is inadequate to meet demand, producing cellular hypoxia (`01`) across
many organs at once. It is the system-wide failure of both control problems in the landscape.
Its power as a concept is that **several very different initiating problems converge on one
end-state**, so it is classified by *which part of the circulation failed*.

```
SHOCK CLASSES  (different first failures; one converging end-state)
===================================================================
  CLASS            THE PRIMARY FAILURE                   MECHANISM SUMMARY
  -----            -------------------                   -----------------
  HYPOVOLEMIC      not enough volume in the system       (hemorrhage / fluid loss)
  CARDIOGENIC      the pump cannot move the volume        (pump failure)
  DISTRIBUTIVE     the vessels dilate / leak -> volume    (e.g., SEPTIC shock:
                   is mislocated, resistance collapses     systemic inflammation,
                                                           see 02; also anaphylactic,
                                                           neurogenic)
  OBSTRUCTIVE      a mechanical block to flow             (e.g., a large embolus,
                   (inflow/outflow obstructed)             external compression)
```

The classes are **hypovolemic** (too little volume — hemorrhage or fluid loss), **cardiogenic**
(the pump fails to move the volume), **distributive** (the vessels dilate and leak so blood
volume is mislocated and vascular resistance collapses — the category that includes **septic**
shock, which is *systemic inflammation* from `02` turned circulatory, plus anaphylactic and
neurogenic forms), and **obstructive** (a mechanical block to flow, such as a large embolus).
Different first failures; one converging end-state.

```
THE STAGES OF SHOCK  (compensation -> decompensation -> irreversibility)
=======================================================================
  (1) COMPENSATED     reflexes defend perfusion of vital organs
        |             (the system is still holding pressure)
        v
  (2) PROGRESSIVE     compensation fails -> widespread tissue hypoxia,
        |             anaerobic metabolism, acidosis, further pump/vessel decline
        v
  (3) IRREVERSIBLE    cellular + organ injury so severe that survival is not
                      recoverable even if the cause is corrected
```

Shock also **progresses in stages**: an early **compensated** stage in which reflexes defend
perfusion of vital organs; a **progressive** stage in which compensation fails and widespread
tissue hypoxia, anaerobic metabolism, and acidosis set in and feed further decline; and an
**irreversible** stage in which cellular and organ injury is too severe to recover even if the
underlying cause is corrected — the tissue-scale version of `01`'s point of no return. A
notable convergence: severe systemic activation of the clotting system can consume clotting
factors and platelets faster than they are made, producing **disseminated intravascular
coagulation** — simultaneous widespread microthrombosis *and* bleeding, the ultimate
demonstration that hemostasis is a *balance* that can fail catastrophically in *both*
directions at once. The management of shock is `clinical-medicine/`; the mechanism and stages
are owned here.

---

## 9. Worked Fictional Cases: Mechanism, Not Diagnosis

Each case is a fictional teaching vignette tracing the hemodynamic chain. None interprets a
real person's findings.

**Case A — Swelling in a limb: which term in the fluid balance broke? (edema mechanism).**
A fictional limb shows soft, pitting swelling. The mechanistic method walks the four edema
causes: is there increased *hydrostatic* pressure (impaired venous return), reduced *oncotic*
pressure (low plasma protein), increased *permeability* (inflammation, `02`), or *lymphatic*
obstruction? The fluid's protein content discriminates a **transudate** (pressure/osmotic) from
an **exudate** (inflammatory). The reasoning localizes to the broken term without naming an
entity — the specific disease is `disease/`, and the measurement of the fluid is `08`.

**Case B — A venous thrombus and its downstream fate (Virchow → embolism → occlusion).**
A fictional venous thrombus forms in a low-flow segment. Virchow's triad explains the *why*:
**stasis** (abnormal flow) is the dominant vertex in veins, often compounded by
hypercoagulability. The fate analysis then predicts the *what next*: the thrombus may
propagate, dissolve, organize, or **embolize** — and a venous embolus travels with the blood
toward the pulmonary circulation, lodging where the vessel first becomes too small. If it
occludes an end-arterial territory downstream, the result is an **infarct** (`01`). The chain
— triad → fate → embolus routing → infarction — is the whole guide in one case. Entities and
management are `disease/`/`clinical-medicine/`.

**Case C — Low perfusion with warm, dilated vessels vs cold, clamped-down vessels (shock
class).**
Two fictional shock presentations: one with widespread *vasodilation* and collapsed vascular
resistance, one with intense *vasoconstriction* defending a failing pump. The mechanistic
classification differs: the first points to a **distributive** mechanism (vessels
dilating/leaking — e.g., septic shock, systemic inflammation from `02`), the second toward
**cardiogenic** or **hypovolemic** mechanisms (the body clamping down to defend perfusion). The
same end-state (systemic hypoperfusion) is reached by opposite vascular behaviors — which is
exactly why shock is classified by *which part of the circulation failed*. No management is
implied.

---

## Reader Tasks (answerable from this guide)

Each task is a *mechanism-reasoning* exercise — how the hemodynamic system fails — not a
personal-result interpretation.

**Task 1 — "The same clotting process that saves a life by sealing a wound can kill by
occluding an artery. What separates the two?" (Sections 3–4)**
Context, not mechanism. Hemostasis and thrombosis use the **same machinery**; the difference is
*where, how much, and whether it stays local*. Hemostasis is the balance tipped toward clotting
**briefly and locally at a real breach**, then reversed. Thrombosis is that balance tipped in an
**intact vessel** by one or more vertices of Virchow's triad — endothelial injury, abnormal
flow, hypercoagulability. The pathology is the right program in the wrong context, which is why
the triad (not the biochemistry) is the key mental model.

**Task 2 — "Why does an embolus lodge where it does?" (Section 6)**
Because it is a *migrating occluder in a directional plumbing system*. An embolus travels with
the blood until it reaches a vessel too small to pass, so its destination is determined by
**where it started and the direction of flow** — venous emboli travel toward the pulmonary
circulation; arterial/systemic emboli travel to systemic end-organs. The routing is
deterministic given the origin and the flow path, which is why the mechanism is taught apart
from the specific clinical syndromes (`disease/`).

**Task 3 — "Two infarcts in different tissues are different colors. What does that reveal?"
(Section 7)**
That the **vascular anatomy** differs. A **white (pale)** infarct means arterial occlusion in a
*solid, end-arterial* organ with few collaterals — the dead zone stays pale. A **red
(hemorrhagic)** infarct means the tissue had a *dual supply or collaterals*, was *loose*, had a
*venous* occlusion, or was *reperfused*, so blood seeped into the dead zone. The color encodes
the supply anatomy and the mechanism of occlusion; it is a mechanistic read-out, not a
diagnosis.

**Task 4 — "Two people are both in shock, but one has warm, dilated vessels and the other is
cold and clamped down. Same problem?" (Section 8)**
No — opposite first failures, same end-state. Warm, dilated, low-resistance vessels point to a
**distributive** mechanism (the vessels themselves dilating/leaking, as in septic shock — `02`
inflammation gone systemic). Cold, clamped-down vessels point to the body defending perfusion
against a **pump** (cardiogenic) or **volume** (hypovolemic) failure. Shock is classified by
*which part of the circulation failed* precisely because different mechanisms converge on the
one end-state of systemic hypoperfusion.

**Task 5 — "How can a person bleed uncontrollably and clot uncontrollably at the same time?"
(Section 8)**
Because hemostasis is a **balance that can fail in both directions at once**. In disseminated
intravascular coagulation, a severe systemic trigger activates the clotting system so widely
that microthrombi form throughout the small vessels **and** the clotting factors and platelets
are *consumed* faster than they can be replaced — so widespread clotting and widespread
bleeding coexist. It is the definitive demonstration that this guide is about a *balance*, not
a switch; the entity and its management are `disease/` and `clinical-medicine/`.

---

## Decision Cheat Sheet

| Observation / signal | Mechanism to reach for | Key caveat |
|---|---|---|
| Excess fluid in tissue | The four edema mechanisms: ↑hydrostatic, ↓oncotic, ↑permeability, lymphatic block | Protein content splits transudate (pressure/osmotic) from exudate (inflammation, `02`) |
| More blood in a tissue | Hyperemia (active arteriolar inflow) vs congestion (passive venous backup) | Chronic congestion → hypoxia, hemosiderin, fibrosis |
| A clot inside an intact vessel | Virchow's triad: endothelial injury, abnormal flow, hypercoagulability | Vertices are additive; arterial = injury-led, venous = stasis-led |
| What happens to a thrombus next | Four fates: propagate, embolize, dissolve, organize/recanalize | Fibrinolysis works on *fresh* thrombi; old ones resist |
| A migrating occluder | Embolism; destination set by origin + flow direction | Venous → pulmonary circulation; arterial → systemic end-organs |
| Ischemic tissue death | Infarction; white (end-arterial/solid) vs red (dual supply/venous/reperfused) | Whether occlusion infarcts depends on collaterals, rate, and O₂ |
| System-wide perfusion failure | Shock classes: hypovolemic, cardiogenic, distributive (septic), obstructive | Different first failures, one end-state; stages run compensated → irreversible |
| Simultaneous clotting *and* bleeding | Consumptive coagulopathy — the balance failing both ways at once | Demonstrates hemostasis is a balance, not a switch |

---

## Common Confusion Points

**Transudate vs exudate (again, from the fluid side).**
A transudate is protein-poor fluid from a hydrostatic/osmotic imbalance across *intact*
vessels; an exudate is protein-rich fluid from *increased permeability* (inflammation, `02`).
Edema from heart/venous or low-protein causes is transudative; edema from inflammation is
exudative.

**Hyperemia vs congestion.**
Hyperemia is *active* increased arteriolar inflow (red, oxygenated); congestion is *passive*
impaired venous outflow (blue, deoxygenated). "Active in, passive out."

**Hemostasis vs thrombosis.**
Same machinery, different context. Hemostasis seals a real breach locally and transiently;
thrombosis is that machinery firing in an intact vessel (Virchow's triad). Pathology is the
right process in the wrong place.

**Thrombus vs embolus vs infarct.**
A thrombus forms *in situ*; an embolus is material that *traveled* and lodged (most emboli are
detached thrombi); an infarct is the *tissue death* that results when occlusion cuts perfusion.
They are three sequential links in one chain, not synonyms.

**Shock is not low blood pressure.**
Shock is *inadequate tissue perfusion*, which usually but not always tracks blood pressure —
early (compensated) shock can maintain pressure while perfusion is already failing, and the
converge is defined at the tissue level, not the cuff.

---

## Resource, Geographic, and Bias Caveats

- **The specific causes and frequencies of thrombosis, embolism, and shock vary by population,
  age, and setting** — the *entities* and their epidemiology are `disease/`. This guide teaches
  the mechanism (Virchow's triad, fate analysis, embolus routing, shock classes), which
  transfers; the case mix does not.
- **Coagulation is measured differently across resource tiers**, and clotting assays are
  exquisitely pre-analytic-sensitive (owned by `08`); the reference bands are `medicine/10`.
  This guide owns *why* the clotting balance shifts, not the assay or its interpretation.
- **Whether a thrombus dissolves, an occlusion infarcts, or shock reverses depends on timing,
  collateral anatomy, and host factors** that vary between individuals; the guide teaches the
  mechanistic modifiers rather than fixed outcomes, and the clinical decisions are
  `clinical-medicine/`.
- **Drug action (anticoagulation, thrombolysis) is out of scope** and owned by `pharmacology/`;
  nothing here should be read as guidance to start, stop, or dose any therapy.
