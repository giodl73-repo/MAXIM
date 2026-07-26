---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "01-INORGANIC-CHEMISTRY.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:chemistry:inorganic-chemistry
kind: guide
module: chemistry
section: chemistry
title: Inorganic Chemistry - Coordination, Organometallics, Bioinorganic
status: source-custody
source_custody: partial
current_path: chemistry/01-INORGANIC-CHEMISTRY.md
canonical_path: chemistry/01-INORGANIC-CHEMISTRY.md
backsource_ids: [mdloom-backfill:chemistry:01-inorganic-chemistry, git-history:chemistry:01-inorganic-chemistry]
concepts: [coordination-chemistry, crystal-field-theory, organometallics, catalysis, bioinorganic]
root_concepts: [inorganic-chemistry]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Inorganic Chemistry — Coordination, Organometallics, Bioinorganic

**This guide owns** the electronic-structure and reactivity of metal complexes:
crystal/ligand field theory, coordination geometry and isomerism, substitution
kinetics, the 18-electron rule, organometallic bonding, homogeneous catalysis,
and bioinorganic active sites. **It does not** re-describe element-by-element
periodic trends (`periodic-table/`), basic ionic/covalent bonding
(`natural-sciences/02`), or solid-state band theory (`materials/02`). The mental
switch versus general chemistry: stop thinking about *main-group Lewis
structures* and start thinking about *d electrons in a field of ligands*.

```
COORDINATION COMPLEX: THE OBJECT THIS GUIDE STUDIES
==========================================================================
                    L        L
                     \      /            L  = ligand (Lewis base,
                      \    /                  donates an electron pair)
              L ------ M ------ L         M  = metal center (Lewis acid,
                      /    \                  has empty d orbitals)
                     /      \            M-L = dative (coordinate) bond
                    L        L

  WHAT DETERMINES BEHAVIOR:
  d-electron count (dn)  x  ligand field strength  x  geometry
            |                      |                       |
            v                      v                       v
  color, magnetism,     high-spin vs low-spin,   isomerism, reactivity
  redox potential       Jahn-Teller distortion    substitution rate

  THREE SUBFIELDS IN THIS GUIDE:
  [A] Werner coordination  -> CFT/LFT, isomerism, kinetics (classic)
  [B] Organometallic       -> M-C bonds, 18e rule, catalysis (Pd, Ru)
  [C] Bioinorganic         -> metals in enzymes (Fe, Zn, Cu, Mo, Mn)
==========================================================================
```

---

## A. Crystal Field Theory: Where d-Electron Energies Come From

Ligand lone pairs approach the metal along fixed directions and **electrostatically
raise the energy of any d orbital pointing at them**. In an octahedron the six
ligands lie on the ±x, ±y, ±z axes. The two orbitals pointing *along axes*
(d_z², d_x²−y²) are destabilized; the three pointing *between axes* (d_xy, d_xz,
d_yz) are stabilized.

```
   FREE ION        OCTAHEDRAL FIELD              KEY NUMBERS
   (5 degenerate                                 Delta_oct = 10 Dq
    d orbitals)      ___  ___   e_g  (+0.6 Do)   e_g  = dz2, dx2-y2
                    /                             t2g  = dxy, dxz, dyz
      _____ ______ <     Delta_oct (Do)          CFSE = (-0.4 n_t2g
                    \  ___ ___ ___  t2g (-0.4 Do)        +0.6 n_eg) Do
                                                         + m*P (pairing)
   barycenter is conserved: the split is 0.6/0.4 about the mean energy.
```

- **Δ_oct (= 10Dq)** is the splitting; typical values 8,000–30,000 cm⁻¹.
- **CFSE** (crystal field stabilization energy) = (−0.4·n_{t2g} + 0.6·n_{eg})·Δ_oct.
  It explains hydration-enthalpy "double-hump" trends across the 3d series and the
  extra thermodynamic stability of d³ and low-spin d⁶.
- **Spin state** is a competition: put the next electron in the upper e_g set
  (cost Δ_oct) or pair it in a half-full t_2g orbital (cost = pairing energy **P**).
  - Δ_oct > P → **low spin** (strong field).
  - Δ_oct < P → **high spin** (weak field).
  - Only d⁴–d⁷ octahedral have a choice; d¹⁻³ and d⁸⁻¹⁰ have a single ground config.

### Geometry changes the diagram

| Geometry | Splitting pattern (low→high) | Δ vs octahedral | Spin |
|---|---|---|---|
| Octahedral | t_2g < e_g | Δ_oct (reference) | high or low (d⁴–d⁷) |
| Tetrahedral | e < t_2 | Δ_tet ≈ (4/9)Δ_oct | **always high spin** (Δ too small to pair) |
| Square planar | e_g(d_xz,d_yz) < d_z² < d_xy < d_x²−y² | large gap below d_x²−y² | usual for **d⁸** strong field |

Square planar is the d⁸ story: Ni(II) with strong ligands, and essentially all of
Pd(II), Pt(II), Rh(I), Ir(I), Au(III). The huge d_x²−y² gap makes the eighth pair
sit in a low, filled set — diamagnetic and geometrically rigid, which is exactly
why square-planar substitution has clean stereochemistry (see kinetics below).

### Ligand field theory (the MO upgrade)

CFT is electrostatic and wrong about *why* CO and CN⁻ split so strongly. **Ligand
field theory** treats M–L bonding with molecular orbitals and classifies ligands:

- **σ-donor only** (NH₃, en, H⁻): raise e_g, moderate Δ.
- **π-donor** (halides, OH⁻, O²⁻): fill metal t_2g-like π orbitals, *lower* Δ →
  weak field.
- **π-acceptor** (CO, CN⁻, phosphines, bipy): metal donates into ligand π* →
  *raises* the effective Δ → strong field. This backdonation is the whole reason
  the spectrochemical series ends with CO.

```
SPECTROCHEMICAL SERIES  (weak field / small Delta  ->  strong field / large Delta)
  I- < Br- < S2- < SCN- < Cl- < NO3- < F- < OH- < ox2- ~ H2O < NCS-
      < CH3CN < NH3 < en < bipy < phen < NO2- < PPh3 < CN- ~ CO
  |------ pi-donors ------|--- sigma only ---|------ pi-acceptors ------|
```

---

## Jahn-Teller Distortion

**Theorem (Jahn-Teller, 1937):** any nonlinear molecule in a spatially
degenerate electronic ground state distorts to remove the degeneracy and lower
its energy. In octahedral complexes the distortion is strong when the degeneracy
lives in the **e_g set** (orbitals pointing straight at ligands), weak when it
lives in t_2g.

| Configuration | e_g occupancy | JT? | Classic example |
|---|---|---|---|
| high-spin d⁴ | e_g¹ | **strong** | Mn(III), Cr(II) |
| low-spin d⁷ | e_g¹ | strong | — |
| d⁹ | e_g³ | **strong** | **Cu(II)** — elongated octahedra everywhere |
| high-spin d⁶, d¹, d² | t_2g asym | weak | Ti(III) |
| d³, d⁵ h.s., d⁶ l.s., d⁸, d¹⁰ | symmetric | none | Cr(III), Ni(II) |

The usual distortion is **axial elongation** (two long *trans* bonds, four short):
it stabilizes the d_z²-derived orbital that half of the degenerate pair occupies.
Cu(II) is the poster child — its aqueous "octahedral" ion is really 4+2. This is a
recurring gotcha when you read Cu bond lengths.

---

## Coordination Isomerism and the Tanabe-Sugano Map

Complexes show a richer isomerism than organic molecules:

| Isomer type | What differs | Example |
|---|---|---|
| Geometric | cis/trans, fac/mer arrangement | cis/trans-[PtCl₂(NH₃)₂] |
| Optical | non-superimposable mirror images | Δ/Λ-[Co(en)₃]³⁺ |
| Linkage | which donor atom of an ambidentate ligand binds | –NO₂ (nitro) vs –ONO (nitrito); SCN vs NCS |
| Ionization | which ion is inside vs. outside the sphere | [Co(NH₃)₅Br]SO₄ vs [Co(NH₃)₅SO₄]Br |
| Coordination | ligand distribution between two metal centers | [Cr(NH₃)₆][Co(CN)₆] vs swap |

**Electronic spectra** are read from **Tanabe-Sugano diagrams**, which plot term
energies (E/B) versus field strength (Δ/B), where **B** is the Racah
inter-electron repulsion parameter. Practical uses: assign the d–d transitions in
a UV-Vis spectrum, extract Δ_oct and B, and detect the **nephelauxetic effect**
(B in the complex < B free-ion → covalent, "cloud-expanding" bonding). For a
high-spin ion the simpler **Orgel diagram** suffices; you need Tanabe-Sugano when
a low-spin ground state can cross over.

---

## Kinetics: Chelate Effect, Inertness, and the Trans Effect

**Thermodynamic stability ≠ kinetic lability.** Keep them separate.

**Chelate effect:** multidentate ligands form far more stable complexes than an
equal number of monodentate donors. The driver is **entropy** — one
hexadentate EDTA⁴⁻ releasing six waters increases particle count (ΔS > 0), so
ΔG = ΔH − TΔS is strongly negative even when ΔH is similar. The **macrocyclic
effect** adds further stability (preorganized ring: crown ethers, cryptands,
porphyrins).

**Inert vs. labile (Taube):** a complex is *inert* if ligand substitution is slow
(minutes–days), *labile* if fast (< 1 min), independent of thermodynamic
stability. CFT rationalizes much of it: octahedral d³ (Cr³⁺) and low-spin d⁶ (Co³⁺,
Pt⁴⁺) are **inert**; ions with empty t_2g or occupied e_g (most first-row M²⁺) are
**labile**. This is why [Co(NH₃)₆]³⁺ survives in acid for days while [Ni(H₂O)₆]²⁺
exchanges water in microseconds.

**Square-planar d⁸ is not uniformly inert — it is a kinetic *series*.** These
complexes substitute *associatively*, so the rate is set by the incoming nucleophile
and the metal, and it falls by roughly **10⁵–10⁶ at each step down the triad**:
**Ni(II) > Pd(II) ≫ Pt(II)** in lability (equivalently, inertness rises Ni < Pd <
Pt with the 5d contraction and stronger M–L bonds). Only **Pt(II)** is genuinely
inert — precisely why cisplatin's aquation is slow enough to act as a drug; Pd(II)
is far more labile (part of why Pd⁰/Pdᴵᴵ cycles turn over quickly in catalysis), and
square-planar Ni(II) exchanges ligands fast, further accelerated by a facile
square-planar ⇌ octahedral (axial-solvent) equilibrium. The kinetics are also
**environment-sensitive**: a strong trans-director labilizes the ligand *trans* to
it (trans effect, below), bulky cis ligands and non-coordinating solvents slow
substitution, and a coordinating solvent opens a parallel solvolysis path. So
"d⁸ square-planar → inert" is a safe shorthand only for 5d Pt(II), with caveats.

**Substitution mechanisms:** dissociative (**D**, rate independent of incoming
ligand), associative (**A**, rate depends on nucleophile), and interchange (I_d,
I_a). Octahedral complexes mostly go dissociative; square-planar go associative
through a 5-coordinate trigonal-bipyramidal intermediate.

**Trans effect** (kinetic) and **trans influence** (thermodynamic) govern
square-planar substitution. Strong trans-directors labilize the ligand *trans* to
them:

```
TRANS-DIRECTING SERIES (weak -> strong)
  H2O ~ OH- ~ NH3 ~ py < Cl- < Br- < I- ~ NO2- ~ SCN- ~ Ph-
      < SO3^2- < PR3 ~ H- ~ CH3- < C2H4 ~ CN- ~ CO
```

This is a *synthesis tool*: it is how cisplatin (**cis**-[PtCl₂(NH₃)₂]) is made
selectively. Starting from [PtCl₄]²⁻, the first NH₃ enters; because Cl⁻ out-directs
NH₃, the second NH₃ goes *trans to a Cl* (i.e., *cis to the first NH₃*), giving the
cis isomer that is the active anticancer drug. Reverse the reagent order and you
get inactive transplatin.

---

## B. Organometallic Chemistry and the 18-Electron Rule

Organometallic = at least one **M–C bond**. The organizing principle is the
**18-electron rule**: stable diamagnetic complexes tend to fill the metal's nine
valence orbitals (one s, three p, five d) with 18 electrons — the transition-metal
analog of main-group's octet. Two counting conventions give the same total:

```
FERROCENE  Fe(C5H5)2, two eta5-cyclopentadienyl rings
  NEUTRAL (covalent) method       IONIC method
    Fe atom       = 8 e             Fe(II)          = 6 e
    2 x Cp (5e)   = 10 e            2 x Cp- (6e)    = 12 e
    ------------------              -------------------
    TOTAL         = 18 e            TOTAL           = 18 e   -> stable, robust
```

| Complex | Count | Notes |
|---|---|---|
| Ni(CO)₄ | 10 + 4×2 = 18 | tetrahedral d¹⁰; volatile, toxic |
| Fe(CO)₅ | 8 + 5×2 = 18 | trigonal bipyramidal |
| Cr(CO)₆ | 6 + 6×2 = 18 | octahedral |
| [Mn(CO)₅]• | 7 + 10 = 17 | odd → dimerizes to Mn₂(CO)₁₀ |
| Vaska IrCl(CO)(PPh₃)₂ | 16 | d⁸ square planar → does oxidative addition |

**Carbonyl backbonding** is the diagnostic. Free CO stretches at **2143 cm⁻¹**;
terminal M–CO at ~1850–2120 cm⁻¹; bridging μ₂-CO at ~1700–1850 cm⁻¹. More
backdonation → more C–O antibonding population → **lower ν(CO)**. IR frequency is
therefore a direct probe of metal electron richness — anionic carbonyls stretch
lowest, cationic highest.

### Elementary steps of catalysis

```
OXIDATIVE ADDITION       REDUCTIVE ELIMINATION     MIGRATORY INSERTION
  M + X-Y -> X-M-Y         X-M-Y -> M + X-Y          M-CO + R -> M-C(=O)R
  ox. state +2             ox. state -2              no change in ox. state
  needs <=16e, d8/d10      forms new C-C/C-X bond    builds the chain (e.g.
  (Vaska, Pd0, Pt0)        (product release)          polymerization, hydroformyl.)
```

Other core steps: **transmetalation** (R group transferred from a main-group
partner to the metal) and **β-hydride elimination** (the chief decomposition/chain-
transfer path for M–alkyls, and the reason "living" catalysts suppress it).

### Palladium cross-coupling (2010 Nobel: Heck, Negishi, Suzuki)

```
              R-X (aryl/vinyl halide)
                     |  1. OXIDATIVE ADDITION
                     v
      Pd(0) ----> R-Pd(II)-X
       ^                 |  2. TRANSMETALATION (R'-[M])
       |                 v          R'-B(OH)2 (Suzuki), R'-ZnX (Negishi)
       |          R-Pd(II)-R'
       |                 |  3. REDUCTIVE ELIMINATION
       +-----------------+  ->  R-R'  (new C-C bond)
```

| Reaction | Transmetalating partner | Couples |
|---|---|---|
| Suzuki-Miyaura | R'–B(OH)₂ / boronate | aryl–aryl (biaryls) |
| Negishi | R'–ZnX | broad, high selectivity |
| Stille | R'–SnR₃ | tolerant but toxic tin |
| Heck | alkene (insertion, not transmetal.) | vinyl arenes |
| Sonogashira | terminal alkyne (Cu co-cat) | aryl–alkynyl |
| Buchwald-Hartwig | amine | C–N (aryl amines) |

Olefin **metathesis** (Grubbs Ru carbenes; also 2005 Nobel) swaps alkene partners
via a metallacyclobutane — the workhorse for ring-closing and cross metathesis in
synthesis (`03`).

---

## C. Bioinorganic Chemistry

Biology uses ~10 metals as the reactive hardware enzymes cannot build from C, H,
N, O alone. This is inorganic chemistry's bridge back to `biochemistry/`.

| Metal site | System | Function / chemistry |
|---|---|---|
| Fe-porphyrin (heme) | hemoglobin/myoglobin | reversible O₂ binding; Fe(II) high↔low spin on binding |
| Fe-porphyrin | cytochromes, P450 | electron transfer; P450 does C–H oxidation via Fe(IV)=O |
| Fe–S clusters | ferredoxins, aconitase | 1-electron transfer; substrate binding |
| Mo/Fe (FeMoco) | nitrogenase | N₂ → 2 NH₃ at ambient conditions |
| Mn₄CaO₅ | Photosystem II OEC | 2 H₂O → O₂ (the source of atmospheric O₂) |
| Zn²⁺ | carbonic anhydrase | Lewis-acid activation of water; CO₂ hydration |
| Cu | cytochrome c oxidase, SOD | O₂ reduction; radical dismutation |
| Co (corrin) | vitamin B₁₂ | rare biological M–C bond; radical rearrangements |

The clinical exemplar is **cisplatin**: cis-[PtCl₂(NH₃)₂] enters the cell, the low
intracellular chloride lets aquation occur, and the Pt binds two adjacent guanine
N7 atoms (a 1,2-intrastrand GG crosslink) that kinks DNA and blocks replication.
Everything about its selectivity — the *cis* geometry, the labile chlorides, the
inert amines — is the coordination chemistry above.

---

## Reader Tasks

1. **Why is [Co(en)₃]³⁺ inert but [Co(H₂O)₆]²⁺ labile?** Co(III) is low-spin d⁶
   (t_2g⁶, large CFSE, no e_g electrons) → substitution-inert; Co(II) is d⁷ with
   e_g occupation and lower CFSE → labile. Oxidation state changes the d-count and
   the field, and that flips the kinetics.
2. **Why does CO split the d orbitals more than H₂O?** CO is a strong **π-acceptor**:
   backdonation from filled metal t_2g into CO π* raises the effective Δ. H₂O is a
   weak π-donor, which *lowers* Δ. Hence CO is at the strong-field end.
3. **Electron count for ferrocene?** 18 (Fe 8 + two η⁵-Cp at 5 e each), or ionically
   Fe(II) 6 + two Cp⁻ at 6 e. Either convention → 18 e, diamagnetic, air-stable.
4. **Predict the Pt(II) substitution product.** Use the trans-directing series: the
   incoming ligand ends up *trans* to the strongest director already present. This
   is how cis-[PtCl₂(NH₃)₂] (cisplatin) is made from [PtCl₄]²⁻.
5. **Which of Mn(III), Cr(III), Cu(II), Ni(II) show strong Jahn-Teller distortion?**
   Mn(III) (h.s. d⁴, e_g¹) and Cu(II) (d⁹, e_g³) — asymmetric e_g. Cr(III) (d³) and
   Ni(II) (d⁸) do not.

## Decision Cheat Sheet

| Question | Tool | Rule of thumb |
|---|---|---|
| High or low spin? | Δ_oct vs P | strong-field ligands + 4d/5d metals → low spin |
| Complex color source? | d–d transition | color ≈ complement of absorbed λ; ε small (Laporte-forbidden) |
| Distorted geometry? | Jahn-Teller table | e_g asymmetry (d⁹, h.s. d⁴) → axial elongation |
| Fast or slow substitution? | inert/labile table | d³, l.s. d⁶ inert; sq-planar d⁸ a trend — Ni(II) labile → Pt(II) inert |
| Stable organometallic? | 18-electron count | aim for 18; 16e d⁸ is a catalyst entry point |
| Metal electron richness? | ν(CO) in IR | lower stretch → more backbonding → richer metal |
| Which isomer forms (Pt II)? | trans effect | product trans to strongest director |

## Common Confusion Points

- **Δ_oct is a property of the *pair*, not the metal alone.** Same Cr³⁺ gives
  different colors with F⁻ vs CN⁻ because Δ depends on both metal *and* ligand.
- **"Strong field" ≠ "strong bond" energetically.** It refers to the size of the
  d-orbital splitting, driven largely by π-effects, not the σ-bond strength.
- **Tetrahedral is always high spin** — Δ_tet ≈ 4/9 Δ_oct is too small to beat the
  pairing energy. Don't compute a "low-spin tetrahedral" state.
- **18-electron rule is a guideline, not a law.** Early metals, bulky ligands, and
  square-planar d⁸ routinely sit at 16 e; f-block and many Werner complexes ignore
  it entirely. Use it for organometallics, not for [Co(NH₃)₆]³⁺.
- **Thermodynamic stability vs. kinetic inertness are orthogonal.** [Fe(H₂O)₆]³⁺ is
  thermodynamically stable yet kinetically labile; the two words answer different
  questions.
- **Bioinorganic metals are chosen for chemistry carbon can't do** — reversible
  redox, Lewis acidity, O₂ handling — not as trace impurities.
