---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "06-NMR-SPECTROSCOPY.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:chemistry:nmr-spectroscopy
kind: guide
module: chemistry
section: chemistry
title: NMR Spectroscopy - Small-Molecule Structure Determination
status: source-custody
source_custody: partial
current_path: chemistry/06-NMR-SPECTROSCOPY.md
canonical_path: chemistry/06-NMR-SPECTROSCOPY.md
backsource_ids: [mdloom-backfill:chemistry:06-nmr-spectroscopy, git-history:chemistry:06-nmr-spectroscopy]
concepts: [nmr, chemical-shift, spin-coupling, two-dimensional-nmr, structure-elucidation]
root_concepts: [nmr-spectroscopy]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# NMR Spectroscopy — Small-Molecule Structure Determination

**This guide owns** NMR as used to solve the structure of an organic small molecule
(≲1 kDa): ¹H and ¹³C interpretation, DEPT, and the 2D toolbox (COSY, HSQC, HMBC,
NOESY). **It defers** protein/macromolecule NMR (triple-resonance assignment,
relaxation dynamics of a folded chain) to `biophysics/03` — same physics, a
different problem: here you are reconstructing a covalent skeleton atom by atom, not
assigning a 200-residue fold. NMR answers *connectivity* and *stereochemistry*; MS
(`07`) supplies the formula; together they close a structure.

```
NMR = MAP A MOLECULE FROM ITS NUCLEI'S ENVIRONMENTS
==========================================================================
  external field B0 splits nuclear spin states; RF flips them;
  each chemically distinct nucleus resonates at a slightly shifted freq

  FOUR OBSERVABLES, FOUR QUESTIONS:

  1. CHEMICAL SHIFT (delta, ppm)  -> "what kind of environment?"
        electron shielding; higher delta = more deshielded
  2. INTEGRATION (1H area)        -> "how many H of this type?"
  3. MULTIPLICITY / J-COUPLING    -> "how many neighbors, how far?"
        n+1 rule; J in Hz encodes geometry
  4. 2D CORRELATIONS              -> "which atom is bonded to which?"
        COSY / HSQC / HMBC / NOESY build the whole graph

  OUTPUT: the covalent connectivity graph + relative stereochemistry
==========================================================================
```

The measured quantity is the **chemical shift** δ = (ν_sample − ν_ref)/ν_ref × 10⁶,
in ppm relative to TMS (δ = 0), which makes it field-independent (a peak at δ 7.2 is
δ 7.2 on a 300 or an 800 MHz magnet). Higher field = better dispersion and
sensitivity, but the *interpretation* is field-invariant.

---

## ¹H NMR: Shift, Integration, Coupling

**Chemical shift** places a proton by its electronic environment; electron-
withdrawing neighbors and π ring currents *deshield* (move δ downfield/higher):

```
   1H SHIFT MAP (delta, ppm)
   12   11   10    9    8    7    6    5    4    3    2    1    0
   |----|----|----|----|----|----|----|----|----|----|----|----|
   COOH      CHO     Ar-H    C=C-H  O-CH  N-CH  C(=O)-CH  C-CH   TMS
                     (6.5-8) (4.5-  (3.3- (2.3- (2.0-2.6) (0.9-  (0)
                              6.5)   4.5)  3.0)             1.7)
```

**Integration** gives the *relative number* of protons in each signal — the ratio,
not the absolute count, so you anchor it against a known group.

**Spin-spin coupling** encodes neighbors. Equivalent neighbors split a signal into
**n+1** lines (the multiplet), separated by the **coupling constant J** (in Hz,
field-independent, and *mutual* — coupled partners share the same J). Multiplicity
reads out the neighbor count; J reads out the geometry:

| Relationship | Typical ³J or nJ (Hz) | Diagnostic |
|---|---|---|
| vicinal H–C–C–H (free rotation) | ~6–8 | the default "quartet/triplet" pattern |
| alkene trans | 12–18 | large J → E-alkene |
| alkene cis | 6–12 | smaller J → Z-alkene |
| aromatic ortho / meta / para | ~8 / ~2 / ~0 | ring substitution pattern |
| geminal ²J, sp³ CH₂ | ~12–18 (magnitude; sign typically −) | diastereotopic methylene |
| geminal ²J, terminal =CH₂ (sp²) | ~0–3 | small — opposite trend to sp³ |

The Karplus relation ties ³J(H–C–C–H) to the H–C–C–H dihedral angle (max near 0°
and 180°, minimum near 90°), which is how you read ring-junction and sugar
stereochemistry from coupling alone.

### Reading a two-signal fragment

A signal at **δ 4.1 (2H, doublet, J = 6 Hz)** coupled to **δ 5.8 (1H, triplet,
J = 6 Hz)** is a textbook fragment: the 2H doublet is a **–CH₂–** with exactly one
neighbor; the 1H triplet is a **=CH–** with two equivalent neighbors (the CH₂); the
shared J = 6 Hz confirms they are bonded (–CH₂–CH=). The CH₂ at δ 4.1 is deshielded,
so it sits next to an electronegative atom (e.g., O or a carbonyl) — i.e., an
**allylic, oxygenated methylene adjacent to a vinyl proton**, such as an
–O–CH₂–CH=CR₂ allylic ether/ester unit.

---

## ¹³C NMR and DEPT

¹³C is only 1.1% abundant, so ¹³C–¹³C coupling is invisible; standard spectra are
**proton-decoupled** — one sharp singlet per unique carbon. Shifts span ~0–220 ppm:

```
   13C SHIFT MAP (delta, ppm)
   220        190      160      130       90       60       30        0
   |-----------|--------|--------|---------|--------|--------|---------|
   ketone/     acid/   aromatic / alkene   C-O      C-N     aliphatic  TMS
   aldehyde    ester    (100-150)          (50-90)  (40-60) C  (0-40)
   (190-220)   (160-185)
```

**DEPT** (Distortionless Enhancement by Polarization Transfer) sorts carbons by how
many attached H's they carry:

```
   DEPT-135:   CH and CH3  -> POSITIVE peaks
               CH2         -> NEGATIVE peak
               quaternary C -> ABSENT (no attached H)
   -> subtract DEPT from the full 13C to find the quaternary carbons.
```

DEPT is the fastest way to count CH₃/CH₂/CH/C and pin down the hydrogenation pattern
of each carbon before you even open the 2D data.

---

## The 2D Toolbox: Building the Bond Graph

One-dimensional spectra list environments; **2D experiments draw the edges** of the
molecular graph. Learn them as four correlation types:

```
   COSY   1H <-> 1H, through-bond (2-3 bonds)   -> which H's are neighbors
          cross-peak (Hx,Hy) means Hx couples to Hy -> trace the H-H chain

   HSQC   1H <-> 13C, ONE bond                  -> which H sits on which C
          (edited HSQC also gives CH2 vs CH/CH3 sign)

   HMBC   1H <-> 13C, 2-3 bonds (long range)    -> connect across quaternary C
          and heteroatoms; stitches fragments over carbonyls, O, N

   NOESY  1H <-> 1H, through-SPACE (< ~5 A)     -> stereochemistry / conformation
   ROESY  (small/medium molecules)              -> which H's are close in 3D
```

**Structure-elucidation workflow (the standard order):**

1. **Formula** from HRMS (`07`) → degrees of unsaturation.
2. **¹H + integration** → proton inventory; **¹³C + DEPT** → carbon inventory by type.
3. **HSQC** → attach each H to its carbon (define the CH_n units).
4. **COSY** → link adjacent CH_n units into contiguous spin systems.
5. **HMBC** → bridge the spin systems across quaternary carbons, carbonyls, O and N
   (the atoms COSY can't see through).
6. **NOESY** → set relative stereochemistry (cis/trans, ring-junction, E/Z).
7. Cross-check against IR functional groups and the MS fragments.

**Tracing a skeleton:** from a COSY, a chain of cross-peaks H1↔H2↔H3 gives a
contiguous –CH–CH–CH– spin system; HSQC then labels the carbons those protons sit
on; HMBC correlations from those protons to a carbon at δ 205 place a ketone at the
end of the chain that COSY could never reach through the carbonyl.

**Distinguishing a cis vs trans ring junction:** run NOESY. A mutual NOE between the
two ring-junction protons (same face, < ~4 Å apart) is positive evidence for a
**cis** fusion. The *absence* of an NOE is only suggestive, not proof, of **trans**:
NOEs also vanish for reasons unrelated to distance — an unfavorable molecular
correlation time (the NOE passes through zero for mid-sized molecules), spin
diffusion, peak overlap, or weak signal — so a negative result must be corroborated.
Coupling constants (Karplus) are the corroboration: a large diaxial ³J (~10–12 Hz)
supports the trans-diaxial arrangement.

---

## Dynamic and Solid-State NMR

**Dynamic NMR** turns the spectrometer into a stopwatch for conformational exchange.
When two exchanging environments swap faster than their frequency separation Δν, the
signals **coalesce** into one; from the coalescence temperature T_c and Δν you get
the rate and the free energy of activation (e.g., hindered amide C–N rotation, ring
flips). The exchange rate at coalescence is k_c = πΔν/√2.

**Solid-state NMR** removes the "everything averages out" luxury of solution: dipolar
coupling and chemical-shift anisotropy broaden lines enormously. **Magic-angle
spinning (MAS)** at 54.74° plus **cross-polarization (CPMAS)** recovers sharp lines,
enabling structure work on insoluble solids, polymorphs, membrane proteins, and
materials — the bridge to `08` (which pins the same solids by diffraction).

---

## Reader Tasks

1. **Identify a fragment: δ 4.1 (2H, d, J = 6) + δ 5.8 (1H, t, J = 6).** A
   –CH₂– (one neighbor) bonded to a =CH– (two neighbors); shared J confirms the bond;
   the deshielded CH₂ implies an adjacent O/carbonyl → an allylic –O–CH₂–CH= unit.
2. **Trace a carbon skeleton from COSY + HSQC.** COSY chains link adjacent protonated
   carbons into spin systems; HSQC assigns each proton to its ¹³C. Then HMBC bridges
   across the quaternary/carbonyl carbons COSY cannot cross.
3. **cis vs trans ring junction?** NOESY — a mutual NOE between the ring-junction
   protons is positive evidence they share a face (**cis**). Absence of an NOE is
   *not* proof of **trans** on its own (NOEs also fail for non-distance reasons);
   confirm trans with a large diaxial ³J (~10–12 Hz, Karplus).
4. **How many carbons are quaternary?** Compare full ¹³C to DEPT-135: peaks present in
   ¹³C but absent in DEPT are quaternary (no attached H).
5. **E or Z alkene from ¹H?** Read the vinyl ³J: ~12–18 Hz → **E (trans)**; ~6–12 Hz →
   **Z (cis)**.

## Decision Cheat Sheet

| Question | Experiment | Read |
|---|---|---|
| What environment is this H/C? | 1D ¹H / ¹³C | chemical shift δ |
| How many H of a type? | ¹H integration | relative area |
| How many neighbors? geometry? | ¹H multiplicity / J | n+1 rule; J in Hz |
| CH₃ vs CH₂ vs CH vs C? | DEPT-135 | signs; quaternary absent |
| Which H on which C? | HSQC | one-bond H–C map |
| Which protons are neighbors? | COSY | H–H cross-peaks |
| Connect across C=O / O / N? | HMBC | 2–3 bond H–C |
| Relative stereochemistry / 3D? | NOESY / ROESY | through-space proximity |
| Conformational exchange rate? | variable-T (dynamic) | coalescence |
| Insoluble solid / polymorph? | CPMAS solid-state | MAS-sharpened lines |

## Common Confusion Points

- **Chemical shift (ppm) is field-independent, and so is J (Hz) — but the *shift
  separation between peaks* is not.** A fixed Δδ keeps the same ppm gap on any
  magnet, while its separation *in hertz* scales with field: Δν(Hz) = Δδ(ppm) ×
  ν₀(MHz). Because J stays fixed in Hz, the Δν/J ratio grows with field, so
  second-order multiplets resolve toward first-order (better dispersion) at higher
  field.
- **Integration gives ratios, not absolute counts.** Anchor to a group you know (a
  CH₃, an aromatic set), then scale.
- **Coupling is mutual.** Two multiplets that couple must show the *same* J; a J-match
  is how you pair partners in a crowded spectrum.
- **HSQC ≠ HMBC.** HSQC is one-bond (the H on that C); HMBC is 2–3 bonds (H to a
  nearby C, including quaternary). Confusing them scrambles the connectivity.
- **NOE is through-space, coupling is through-bond.** A strong NOE without a coupling
  means the protons are close in 3D but not bonded neighbors — exactly the
  stereochemistry signal.
- **A missing NOE does not prove a trans/distant geometry.** NOE intensity depends on
  distance *and* on molecular tumbling (it crosses zero for mid-sized molecules),
  spin diffusion, and signal-to-noise; treat a *positive* NOE as evidence and a
  *negative* one as inconclusive — corroborate geometry with ³J/Karplus.
- **This is not protein NMR.** For a folded macromolecule the strategy (triple-
  resonance backbone assignment, relaxation) is different — that is `biophysics/03`.
- **DEPT shows no quaternary carbons at all.** A "missing" carbonyl or ipso carbon in
  DEPT is expected, not an error; find it in the plain ¹³C.
