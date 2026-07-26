---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "04-IMMUNOPATHOLOGY-AND-TISSUE-INJURY.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:pathology:immunopathology-and-tissue-injury
kind: guide
module: pathology
section: pathology
title: Immunopathology and Tissue Injury
status: source-custody
source_custody: partial
current_path: pathology/04-IMMUNOPATHOLOGY-AND-TISSUE-INJURY.md
canonical_path: pathology/04-IMMUNOPATHOLOGY-AND-TISSUE-INJURY.md
backsource_ids: [mdloom-backfill:pathology:04-immunopathology-and-tissue-injury]
concepts: [hypersensitivity, autoimmunity, transplant-rejection, immunodeficiency-lesion, amyloid-deposition]
root_concepts: [immunopathology]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Immunopathology and Tissue Injury

**This guide owns** immune-mediated injury *as a tissue-injury mechanism*: the four
**hypersensitivity mechanisms** (the Gell and Coombs types I–IV) framed as *how the immune
response damages host tissue*; **autoimmunity** as the lesion produced when self-tolerance is
lost; **transplant rejection** and graft-versus-host injury as alloimmune tissue damage; and
**immunodeficiency as a lesion** — what tissue shows when defense fails. It also owns
**amyloidosis** as a protein-deposition tissue lesion (classically grouped with immunity).
**It builds on** `01-CELL-INJURY-ADAPTATION-AND-DEATH` (immune effectors kill cells by the
same final mechanisms — including fibrinoid necrosis) and `02-INFLAMMATION-AND-TISSUE-REPAIR`
(hypersensitivity injury *is* inflammation with a specific trigger, and type IV includes the
granulomatous pattern), and it feeds `10` (these injury patterns are read on the slide).

**It explicitly defers** the *immune-cell biology and signaling* — how lymphocytes develop,
how antigen is presented, how antibodies are made, cytokine and receptor mechanism — to
`immunology/`, which is the owner of *the immune system itself*. This guide is the *pathology*
view: **the immune response as a cause of tissue damage**, not the biology of the immune cells.
It also defers the *disease entities* (specific autoimmune diseases, specific
immunodeficiencies) to `disease/`; the *organisms* that exploit immunodeficiency to
`microbiology/`/`virology/`; the *transplantation/HLA genetics* to `genomics/`/`immunology/`;
and any *therapy* to `pharmacology/`/`clinical-medicine/`.

> **This module is an educational reference about *how pathology reasons about disease
> mechanism* — never medical advice. It does *not* interpret any reader's own results,
> images, or symptoms, does *not* diagnose, and gives *no* treatment, dosing, specimen, or
> bench instructions and *no* forensic/legal determinations. All cases are fictional teaching
> vignettes; all numbers are illustrative and, where a real standard is named, attributed and
> dated.**

*Per-guide banner: educational reference on immune-mediated tissue-injury mechanism — never
self-diagnosis, never personal-result interpretation, never a procedure, never forensic/legal
advice. Disease entities are named only to illustrate a mechanism; the catalog is `disease/`,
and immune-cell biology is `immunology/`.*

---

## The Big Picture: Immunopathology Is Friendly Fire — a Defense System Injuring Its Own Host

The novice mental model is "the immune system fights infection; sometimes it's weak." The
expert model is that the immune system is a **powerful weapons platform** whose whole job is to
destroy targets, and immunopathology is the study of **that platform injuring the host** — by
firing at the *wrong target* (autoimmunity), *too hard* at a harmless target
(hypersensitivity), at a *foreign but medically desirable* target (transplant rejection), or
by being *unable to fire* so that opportunists injure the tissue instead (immunodeficiency).
The unifying insight is that the *effector mechanisms are the same ones that protect* — this
guide is the pathology of defense turned against the tissue it defends.

```
THE FOUR FAILURE MODES OF IMMUNITY  (this guide owns the tissue injury each causes)
==================================================================================
  WRONG TARGET        AUTOIMMUNITY        immune attack on SELF antigens
        |                                 (tolerance is lost)
  TOO HARD            HYPERSENSITIVITY    excessive/inappropriate response to an
        |                                 antigen (self, environmental, or microbial)
  FOREIGN-BUT-WANTED  TRANSPLANT REJECT.  attack on a grafted tissue (alloimmunity);
        |                                 GVHD is the mirror image
  CANNOT FIRE         IMMUNODEFICIENCY    defense fails -> opportunists + unusual
                                          lesions injure the tissue instead
  -----------------------------------------------------------------------------
  COMMON THREAD: the EFFECTOR mechanisms (antibody, complement, T cells,
  phagocytes) are the SAME weapons that protect. Injury = the weapon + a
  target it should not be destroying (or the absence of the weapon).
```

Two facts organize the guide. First, **the type of injury is set by the effector, not the
trigger**: the same antigen can cause different lesions depending on whether antibody,
immune complexes, or T cells do the damage — which is exactly what the Gell and Coombs
classification captures. Second, this guide **stops at the tissue-injury mechanism**: it owns
*how the immune response damages tissue and what that damage looks like*, and hands the biology
of the immune cells to `immunology/` and the specific diseases to `disease/`.

**Bridge — an authorization system doing damage.** Immunity is an *access-control and
enforcement* system. Autoimmunity is enforcement acting on *legitimate principals* (self) —
the allow-list is corrupted. Hypersensitivity is enforcement *over-reacting* to a low-risk
request. Rejection is enforcement correctly flagging a *foreign principal* that the operator
actually wanted admitted. Immunodeficiency is *enforcement disabled*, so intruders roam. In
every case the enforcement machinery is intact and powerful; what varies is the target and
the calibration.

---

## 1. The Four Hypersensitivity Mechanisms (Gell and Coombs)

**Hypersensitivity** is an excessive or inappropriate immune response that injures tissue. The
**Gell and Coombs** classification (P.G.H. Gell and R.R.A. Coombs, mid-20th century) sorts the
injury by **which effector does the damage**, and it is the organizing spine of this guide.
The classification is a *mechanistic taxonomy of tissue injury*, and real diseases often blend
more than one type — so it is best held as "which effector mechanism" rather than a rigid
label.

```
THE FOUR TYPES  (sorted by EFFECTOR, i.e., what mechanism injures the tissue)
============================================================================
  TYPE I    IMMEDIATE          pre-formed antibody on mast cells + antigen ->
            (mediator release)  rapid release of vasoactive mediators ->
                                vasodilation, permeability, smooth-muscle effects

  TYPE II   ANTIBODY-MEDIATED  antibody binds an antigen ON a cell or in matrix ->
            (cytotoxic/         complement + phagocytes destroy it, OR antibody
             dysfunction)       alters function without destruction

  TYPE III  IMMUNE-COMPLEX     antigen-antibody complexes form in blood ->
            (complex deposition) DEPOSIT in vessel walls/tissue -> complement ->
                                neutrophil inflammation (fibrinoid necrosis, see 01)

  TYPE IV   DELAYED /          NO antibody: sensitized T cells (and macrophages)
            CELL-MEDIATED       drive injury -> direct cytotoxicity or delayed
                                inflammation (includes the GRANULOMA, see 02)
```

**Type I (immediate)** injury is driven by **pre-formed antibody bound to mast cells**: on
re-exposure, antigen cross-links the antibody and the mast cell **degranulates**, releasing
vasoactive mediators within minutes → vasodilation, increased permeability, and smooth-muscle
contraction. It is *immediate* because the antibody is already in place; the lesion is the
mediator effect, ranging from local to systemic (the systemic extreme links to the
distributive shock of `03`).

**Type II (antibody-mediated)** injury is driven by **antibody binding an antigen on a cell
surface or in the extracellular matrix**. Three sub-mechanisms follow: **complement- and
phagocyte-mediated destruction** of the coated cell (opsonization → lysis or phagocytosis),
**recruitment of inflammation** at the site the antibody bound, or **functional alteration
without destruction** — antibody that blocks or over-stimulates a receptor, causing
dysfunction with little inflammation. The key idea is that the antigen is *fixed to a target
structure*, so the injury is *localized to that structure*.

**Type III (immune-complex)** injury is driven by **antigen–antibody complexes that form in
the circulation and then deposit** in vessel walls and tissues (they are not fixed to a target;
they *precipitate* where flow and filtration favor it). Deposited complexes activate
complement, recruit neutrophils, and produce inflammation and vessel-wall damage — the
**fibrinoid necrosis** of `01`. Because the complexes deposit at multiple filtration sites, the
injury is often **multi-site** rather than organ-specific — a distinguishing feature from type
II.

**Type IV (delayed / cell-mediated)** injury uses **no antibody**: **sensitized T cells** (with
macrophages) drive the damage, either by *direct cytotoxic killing* of target cells or by a
*delayed inflammatory* reaction that peaks over a day or more. Type IV includes the
**granulomatous** pattern of `02` (macrophage-driven walling-off) and is the mechanism behind
many chronic and contact reactions. It is *delayed* because T cells must be recruited and
activated at the site — there is no pre-formed effector.

| Type | Effector | Speed | Signature tissue injury | Links to |
|---|---|---|---|---|
| I | Antibody on mast cells → mediators | Immediate | Vasodilation, permeability, smooth-muscle effects | `03` (systemic → shock) |
| II | Antibody vs cell/matrix antigen | Hours | Localized cell destruction or dysfunction | `01` (cell death) |
| III | Circulating immune complexes deposit | Hours | Multi-site vasculitis, fibrinoid necrosis | `01`, `02` |
| IV | Sensitized T cells + macrophages | Delayed (day+) | Cytotoxic injury; granulomas | `02` (granuloma) |

The mnemonic value is not the numbers but the **effector question**: faced with immune-mediated
injury, the productive move is to ask *which mechanism is doing the damage* — mast-cell
mediators, antibody on a target, deposited complexes, or T cells — because that determines the
lesion, the distribution, and the tempo. The *molecular biology* of each effector is
`immunology/`.

---

## 2. Autoimmunity: Injury From Loss of Self-Tolerance

**Self-tolerance** is the immune system's normal ability to *not* attack the host's own
antigens; **autoimmunity** is the tissue injury that results when that tolerance fails and the
immune response turns on self. This guide owns autoimmunity as a **mechanism of injury** (the
lesion), not as immune-cell biology (`immunology/`) or as a catalog of autoimmune diseases
(`disease/`).

```
AUTOIMMUNITY  (tolerance fails -> self becomes a target -> injury by types II-IV)
================================================================================
  NORMAL: tolerance deletes/controls self-reactive lymphocytes
        |
        |  breakdown: susceptibility genes + an environmental trigger
        v
  SELF-REACTIVE RESPONSE  (antibodies and/or T cells against self antigens)
        |
        +--> injures tissue by the SAME effector mechanisms as Section 1:
        |      antibody vs self cell/matrix (type II-like)
        |      self immune complexes deposit (type III-like)
        |      self-reactive T cells attack (type IV-like)
        v
  ORGAN-SPECIFIC (one target organ)  <---->  SYSTEMIC (widespread self antigen)
```

Autoimmunity arises from a **breakdown of tolerance**, and the recurring theme is that it is
**multifactorial**: inherited susceptibility (certain immune-gene variants raise risk — the
genetics owned by `genomics/`/`immunology/`) combined with an environmental trigger
(infection, tissue injury exposing hidden antigens, or molecular mimicry between a microbe and
a self antigen). Once tolerance fails, the injury proceeds by the **same effector mechanisms**
as hypersensitivity — antibody against self structures, self immune-complex deposition, or
self-reactive T cells — which is why autoimmunity is taught *after* the Gell and Coombs types:
it reuses them with a self antigen.

The most useful *pathologic* axis is **organ-specific vs systemic**: some autoimmune injury
targets a single organ's antigen (localized lesion), while some targets antigens present
throughout the body (widespread, multi-organ lesions, often immune-complex–mediated). This
axis predicts the *distribution* of the lesion. The specific diseases along it are `disease/`;
the mechanism — tolerance failure reusing the effector toolkit against self — is owned here.

---

## 3. Transplant Rejection and Graft-Versus-Host Injury

**Transplant rejection** is immune injury to a grafted tissue because the recipient recognizes
the graft as **foreign** (alloimmunity). It is a clean demonstration of immunopathology because
the immune response is *working correctly* — correctly identifying non-self — but the outcome is
medically undesirable. It is classified **by tempo and mechanism**, which also encodes the
dominant effector.

```
TRANSPLANT REJECTION  (foreign-but-wanted: the response is correct, the outcome bad)
===================================================================================
  HYPERACUTE   minutes-hours   PRE-EXISTING recipient antibody vs the graft ->
                               immediate vascular injury, thrombosis (see 03)
  ACUTE        days-weeks+     newly mounted response: T-cell-mediated attack on
                               graft cells AND/OR antibody-mediated vascular injury
  CHRONIC      months-years    prolonged low-grade injury -> vascular wall thickening,
                               fibrosis (see 02), progressive graft dysfunction
  ----------------------------------------------------------------------------
  MIRROR IMAGE — GRAFT-VERSUS-HOST: immune cells IN the graft attack the
  RECIPIENT's tissues (the graft rejects the host).
```

**Hyperacute** rejection is driven by **pre-existing recipient antibody** against the graft,
producing immediate vascular injury and thrombosis (the `03` mechanism) within minutes to
hours — a type II–like, antibody-on-target mechanism. **Acute** rejection is a **newly mounted**
response over days to weeks: a T-cell–mediated attack on graft cells (type IV–like) and/or an
antibody-mediated attack on the graft vasculature (type II–like). **Chronic** rejection is
**prolonged, low-grade** injury over months to years, producing vascular wall thickening and
**fibrosis** (`02`) with progressive loss of graft function. The **mirror image** is
**graft-versus-host** injury, where immunocompetent cells *within the graft* attack the
*recipient's* tissues — the graft rejecting the host. The point owned here is the **injury
pattern and its tempo**; the immunology of allorecognition and the HLA system are
`immunology/`/`genomics/`, and clinical management is `clinical-medicine/`.

---

## 4. Immunodeficiency as a Lesion

Where the preceding sections are the immune system doing *too much* to the wrong target,
**immunodeficiency** is the immune system doing *too little* — and its *pathology* is not the
missing cells but the **tissue injury the opportunists produce in their absence**. This guide
owns immunodeficiency as a **lesion pattern**, not as the immunology of the defect
(`immunology/`) or the microbiology of the organisms (`microbiology/`/`virology/`).

```
IMMUNODEFICIENCY  (owned here as the LESION the missing defense allows)
======================================================================
  PRIMARY (inherited)   a component of immunity is congenitally defective
  SECONDARY (acquired)  immunity is lost to another cause (far more common)
        |
        v
  THE PATHOLOGY IS THE CONSEQUENCE, NOT THE DEFECT:
    - unusual / opportunistic infections in tissue (organisms that a
      competent immune system would clear) -> owned as ORGANISMS by micro/virology
    - reduced or atypical inflammatory response (few responders to recruit)
    - increased risk of certain neoplasms (lost immune surveillance, see 05)
```

Immunodeficiency is **primary** (an inherited defect in a component of immunity) or
**secondary/acquired** (immunity lost to another cause — the far more common category). The
*pathologic* signature, which is what this guide owns, is the **downstream consequence**: an
**opportunistic** injury pattern (infections by organisms a competent immune system would
clear — the organisms themselves owned by `microbiology/`/`virology/`), an **attenuated or
atypical inflammatory response** (because there are fewer effectors to recruit — a direct
consequence of `02` machinery being depleted), and an **increased risk of certain neoplasms**
(the loss of immune surveillance, connecting to `05`). The recurring pathology lesson is that
**an immunodeficient tissue does not look like a normally infected tissue**: the response is
blunted, the organisms are unusual, and the pattern itself is a clue. The specific
immunodeficiency *entities* are `disease/`.

---

## 5. Amyloidosis: A Protein-Deposition Lesion

**Amyloidosis** is grouped here because it is classically taught with immunity and because it
is a distinctive **tissue-injury-by-deposition** mechanism. **Amyloid** is a pathologic
**misfolded protein** that aggregates into insoluble fibrils with a characteristic structure,
deposits in the extracellular space, and **physically disrupts tissue** — a mechanical and
functional lesion rather than an inflammatory one.

```
AMYLOIDOSIS  (misfolded protein -> fibrils -> extracellular deposit -> dysfunction)
==================================================================================
  a precursor protein misfolds into a stable, insoluble fibril
        |
        v
  fibrils deposit in the EXTRACELLULAR space of tissues/vessel walls
        |
        v
  progressive accumulation -> pressure atrophy of adjacent cells (see 01),
  stiffening, and organ dysfunction
        |
        v
  MANY precursor proteins can do this -> amyloidosis is a FAMILY defined by
  the SHARED misfolding+deposition mechanism, not one protein or one disease
```

The unifying feature is the **mechanism, not the protein**: many different precursor proteins
can misfold into the same fibrillar, insoluble form, so amyloidosis is a **family of
conditions defined by a shared deposition mechanism**. The deposits accumulate progressively,
causing **pressure atrophy** of adjacent cells (`01`), stiffening, and organ dysfunction. On
tissue examination amyloid has characteristic staining properties that identify the *deposit*;
identifying *which precursor protein* (which determines the specific disease and its cause) is
an entity-level question owned by `disease/`, and the protein-folding biochemistry is
`biochemistry/`. This guide owns the *mechanism* — misfolded protein depositing extracellularly
and injuring tissue by accumulation.

---

## 6. Worked Fictional Cases: Mechanism, Not Diagnosis

Each case is a fictional teaching vignette tracing the immune-injury mechanism. None interprets
a real person's findings.

**Case A — The same antigen, two different lesions (effector determines injury).**
Two fictional tissue reactions to conceptually similar antigens look nothing alike: one shows
**deposited immune complexes** with complement, neutrophils, and vessel-wall fibrinoid necrosis
at *multiple* sites; the other shows a **T-cell and macrophage** infiltrate forming
**granulomas** at a *localized* site with no antibody. The mechanistic reading: the first is a
**type III** (immune-complex) injury — complexes form in blood and deposit where filtration
favors it, so the injury is multi-site; the second is a **type IV** (cell-mediated) injury —
sensitized T cells drive delayed, granulomatous inflammation. The lesson is that **the effector,
not the trigger, sets the lesion** — the organizing claim of Section 1.

**Case B — Rejection tempo reveals the effector (transplant injury).**
A fictional graft fails at three different tempos in three scenarios. Failure within
**minutes-to-hours** with immediate vascular thrombosis points to **hyperacute** rejection from
**pre-existing antibody** (type II–like). Failure over **days-to-weeks** with a T-cell
infiltrate and/or antibody-mediated vascular injury points to **acute** rejection. Slow failure
over **months-to-years** with vascular thickening and **fibrosis** points to **chronic**
rejection. The tempo and the injury pattern *encode the mechanism*, which is why rejection is
classified this way. The allo-immunology is `immunology/`; management is `clinical-medicine/`.

**Case C — An infection that looks wrong (immunodeficiency as a lesion).**
A fictional tissue shows an **opportunistic** organism and a **blunted** inflammatory response —
few of the responders that `02` would normally recruit. The mechanistic reading is that the
lesion is a *consequence of absent defense*: an organism a competent immune system would clear,
in a tissue that cannot mount a normal reaction. The pathology is the *pattern* (unusual
organism + attenuated response), not the immunologic defect itself (`immunology/`) or the
organism's biology (`microbiology/`). Recognizing "this response is too weak for this organism"
is the mechanistic clue.

---

## Reader Tasks (answerable from this guide)

Each task is a *mechanism-reasoning* exercise — how the immune system injures tissue — not a
personal-result interpretation.

**Task 1 — "Why does pathology sort immune injury by 'type I–IV' instead of by disease?"
(Section 1)**
Because the **effector mechanism**, not the disease, determines the lesion. Types I–IV are a
taxonomy of *which weapon does the damage* — mast-cell mediators (I), antibody on a target
(II), deposited immune complexes (III), or T cells (IV) — and that choice sets the tissue
injury, its distribution, and its tempo. Sorting by disease would obscure the shared machinery;
sorting by effector predicts the lesion. Real diseases often blend types, so the classification
is a mechanistic lens, not a rigid label.

**Task 2 — "Type II and type III are both antibody-mediated. What actually separates them?"
(Section 1)**
*Where the antigen is.* In **type II** the antigen is **fixed** — bound to a cell surface or in
the matrix — so the injury is **localized to that structure**. In **type III** the antigen is
**soluble**, so antigen–antibody complexes form in the *circulation* and then **deposit** where
flow and filtration favor it, producing **multi-site** injury (vasculitis, fibrinoid necrosis).
Same class of weapon (antibody + complement), different target location, different distribution.

**Task 3 — "A transplant fails within hours; another fails over years. Why classify these
together?" (Section 3)**
Because both are **alloimmune tissue injury** — the recipient recognizing the graft as foreign —
and the *tempo encodes the effector*. Hours means **pre-existing antibody** (hyperacute);
days-to-weeks means a **newly mounted** T-cell/antibody response (acute); months-to-years means
**prolonged low-grade** injury producing vascular thickening and fibrosis (chronic). Classifying
by tempo is classifying by mechanism, which is what makes rejection a single coherent topic.

**Task 4 — "In immunodeficiency, why is the *pathology* the infection rather than the missing
cells?" (Section 4)**
Because pathology studies **lesions**, and the lesion of immunodeficiency is what the *absence*
of defense allows: opportunistic organisms injuring tissue, an attenuated inflammatory response,
and raised neoplasm risk from lost surveillance. The missing immune component is an
*immunology* fact (`immunology/`); the *tissue consequence* — an unusual organism with a
too-weak response — is the pathology this guide owns. Recognizing that mismatch is the
diagnostic clue.

**Task 5 — "Amyloid is called a 'family,' not a disease. Why?" (Section 5)**
Because it is defined by a **shared mechanism**, not a shared protein. Many different precursor
proteins can misfold into the same insoluble, fibrillar form that deposits extracellularly and
injures tissue by accumulation and pressure atrophy. The *deposit* is identified by its
staining properties; *which precursor* it is (and hence the specific disease and cause) is an
entity-level question for `disease/`, and the folding biochemistry is `biochemistry/`. The
unifying pathology is the deposition mechanism.

---

## Decision Cheat Sheet

| Observation / signal | Mechanism to reach for | Key caveat |
|---|---|---|
| Rapid vasodilation/permeability after antigen re-exposure | Type I: mast-cell mediator release | Systemic version links to distributive shock (`03`) |
| Localized cell destruction or dysfunction | Type II: antibody on a fixed cell/matrix antigen | Can destroy *or* merely alter function (block/stimulate) |
| Multi-site vasculitis with fibrinoid necrosis | Type III: circulating immune complexes deposit | Distribution follows filtration, not one organ |
| Delayed inflammation or granulomas, no antibody | Type IV: sensitized T cells + macrophages | Includes the `02` granulomatous pattern |
| Injury to the host's own tissue | Autoimmunity: tolerance lost → effectors reused vs self | Organ-specific vs systemic predicts distribution |
| A grafted tissue failing | Rejection; tempo (hyperacute/acute/chronic) encodes the effector | GVHD is the mirror: graft attacks host |
| Unusual organism + weak inflammatory response | Immunodeficiency lesion (defense absent) | The pattern, not the defect, is the pathology here |
| Extracellular deposits stiffening an organ | Amyloidosis: misfolded protein → fibrils → deposition | A family by mechanism; the precursor is `disease/` |

---

## Common Confusion Points

**Hypersensitivity is sorted by effector, not by antigen.**
Types I–IV name *which mechanism injures the tissue* (mast-cell mediators, antibody-on-target,
deposited complexes, T cells). The same antigen can cause different types; many diseases blend
types. Hold the classification as a mechanistic lens.

**Type II vs type III.**
Both use antibody, but type II antigen is *fixed* (localized injury) while type III antigen is
*soluble* and forms circulating complexes that *deposit* (multi-site injury). Location of the
antigen is the discriminator.

**Autoimmunity is not a separate weapon.**
Autoimmune injury reuses the *same* effector mechanisms (types II–IV) with a *self* antigen after
tolerance fails. It is multifactorial (susceptibility genes + trigger), and its key pathologic
axis is organ-specific vs systemic.

**Rejection means the immune system is working.**
Transplant rejection is *correct* recognition of foreign tissue with an undesirable outcome —
not an immune malfunction. It is classified by tempo/mechanism (hyperacute/acute/chronic), and
graft-versus-host is its mirror image.

**Immunodeficiency's pathology is the consequence.**
The lesion is the opportunistic injury and blunted response the missing defense permits — not
the immunologic defect itself (that is `immunology/`) or the organism (that is
`microbiology/`/`virology/`).

**Immunopathology (this guide) vs immunology (the sibling).**
`immunology/` owns the immune system's normal biology and cells; this guide owns the immune
system as a **cause of tissue injury** — the lesions of hypersensitivity, autoimmunity,
rejection, and immunodeficiency. Name the cell biology by reference; re-derive none of it.

---

## Resource, Geographic, and Bias Caveats

- **The specific autoimmune and immunodeficiency diseases, and the organisms that exploit
  immunodeficiency, vary strongly by population and geography** — those *entities* and
  *organisms* are `disease/`, `microbiology/`, and `virology/`. This guide teaches the
  effector-based injury mechanism, which transfers; the epidemiology does not.
- **The Gell and Coombs classification is a teaching taxonomy, not a strict partition.** Real
  immune-mediated diseases frequently involve more than one type, and the framework has been
  refined over time. This guide uses it as a mechanistic lens and attributes it to its
  originators rather than presenting it as an exhaustive law.
- **Detecting immune-mediated injury depends on technique and ancillary tests** (immunofluorescence
  and immunohistochemistry patterns, the `09` substrate, and the `10` ancillary-evidence logic);
  interobserver variability and access to those tests differ by resource tier. A pattern narrows
  the mechanism; it rarely proves an entity alone.
- **Transplantation and its immunology are resource-concentrated and rapidly evolving.** The HLA
  genetics, matching, and management are `immunology/`/`genomics/`/`clinical-medicine/`; this
  guide owns only the injury pattern and its tempo, and asserts no clinical guidance.
