# 02-BONDING — Chemical Bonding

> Lewis structures to MO theory to metallic bands. VSEPR geometry. Hybridization
> as an approximation. Bond polarity and dipole moments. Weak interactions that
> dominate biology and materials science.

---

## The Bonding Landscape

```
WHAT HOLDS ATOMS TOGETHER?

  Electrostatic attraction (always)
        │
        ├── Between ions ────────────────── IONIC BONDING
        │   (cation + anion, largely full charge transfer)
        │
        ├── Between atoms sharing electrons ─ COVALENT BONDING
        │   (partial charge, quantum delocalization)
        │
        ├── Between metal cations + electron sea ─ METALLIC BONDING
        │   (full delocalization through crystal)
        │
        └── Between molecules ─── INTERMOLECULAR / WEAK INTERACTIONS
            (H-bonds, van der Waals, London dispersion, π-stacking)

BOND CHARACTER IS A SPECTRUM — not discrete categories:
  Pure covalent        Polar covalent           Ionic
  (ΔEN = 0)          (ΔEN = 0.5 – 2.0)        (ΔEN > 2.0)
  H-H, Cl-Cl          H-Cl, C-O, N-H           NaCl, MgO, CaF₂
```

---

## Ionic Bonding

Formed when one atom (metal, low IE) transfers electrons to another (nonmetal, high EA).
Held together by Coulombic attraction between the resulting ions.

### Lattice Energy

Energy to separate one mole of ionic solid into gas-phase ions:

```
U = −(Nₐ · M · z₊ · z₋ · e²) / (4πε₀ · r₀) · (1 − 1/n)

M = Madelung constant (geometry-dependent: 1.748 for NaCl structure)
z = ionic charges,  r₀ = nearest-neighbor distance,  n = Born exponent (~8–12)

Approximate intuition: U ∝ z₊z₋ / r₀
  MgO  (z=2, small ions): U ≈ 3900 kJ/mol — very hard, high melting point
  NaCl (z=1, larger ions): U ≈ 788 kJ/mol
  CsI  (z=1, large ions):  U ≈ 613 kJ/mol
```

### Born-Haber Cycle

Hess's law applied to ionic formation — connects lattice energy to measurable quantities:

```
Cs(s) + ½F₂(g) → CsF(s)        ΔHf° (formation enthalpy, measurable)

Decompose into steps:
  Cs(s) → Cs(g)                  ΔHsub  (sublimation)
  Cs(g) → Cs⁺(g) + e⁻           IE₁
  ½F₂(g) → F(g)                  ½D (bond dissociation)
  F(g) + e⁻ → F⁻(g)             EA (electron affinity, negative)
  Cs⁺(g) + F⁻(g) → CsF(s)      −U (lattice energy, large and negative)

ΔHf° = ΔHsub + IE₁ + ½D + EA − U

Use any five known values to calculate the sixth.
```

### Ionic Radii Trends

- **Cations** are smaller than parent atom (lost electrons, same Z pulls fewer electrons harder)
- **Anions** are larger (gained electrons, same Z spread over more electrons)
- Both decrease across a period (Zeff increases); increase down a group (higher n shell)
- Isoelectronic series: O²⁻ > F⁻ > Ne > Na⁺ > Mg²⁺ > Al³⁺ (same 10 e⁻, increasing Z)

---

## Covalent Bonding — Lewis Structures

### Lewis Structure Procedure

1. Count total valence electrons (Σ valence e⁻ from each atom; add 1 per negative charge)
2. Sketch connectivity (central atom usually lowest EN; H always terminal)
3. Fill octets on terminal atoms; put remainder on central atom
4. Convert lone pairs to bonds to satisfy central atom octet (double/triple bonds)
5. Assign formal charges: FC = Vₑ − Lₑ − ½Bₑ

**Formal charge (FC):** Vₑ = valence electrons, Lₑ = lone-pair electrons, Bₑ = bonding electrons

Prefer structures where:
- FC closest to zero on all atoms
- Negative FC on most electronegative atom

### Octet Rule and Exceptions

| Case | Example | Reason |
|------|---------|--------|
| Electron deficient | BF₃, BH₃ | B has only 6 electrons (empty p orbital — Lewis acid) |
| Odd-electron radical | NO, NO₂ | Odd electron count, one atom has 7 electrons |
| Expanded octet | PCl₅, SF₆, XeF₄ | Period 3+: d orbitals available (debated — hypervalent model) |

### Resonance

Multiple valid Lewis structures that differ only in electron placement (not atom positions):

```
NO₃⁻ has three equivalent resonance structures:
   O         O⁻        O⁻
   ‖         ‖         |
O-N-O⁻  ↔  O-N-O  ↔  O=N-O

Reality: bonds are equivalent (1.33 Å, between single 1.41 Å and double 1.22 Å)
Resonance = electron delocalization — NOT rapid switching between structures
```

---

## VSEPR — Geometry from Electron Pair Repulsion

Electron pairs (bonding + lone) arrange to maximize distance from each other.
Lone pairs take more space than bonding pairs.

```
Steric  Bonding  Lone   Electron       Molecular
Number  Pairs    Pairs  Geometry       Geometry       Example
──────────────────────────────────────────────────────────────────
2       2        0      linear         linear          CO₂, BeCl₂
3       3        0      trig. planar   trig. planar    BF₃, SO₃
3       2        1      trig. planar   bent            SO₂, O₃
4       4        0      tetrahedral    tetrahedral     CH₄, SiCl₄
4       3        1      tetrahedral    trig. pyram.    NH₃
4       2        2      tetrahedral    bent            H₂O  (104.5°)
5       5        0      trig. bipyram. trig. bipyram.  PCl₅
5       4        1      trig. bipyram. see-saw         SF₄
5       3        2      trig. bipyram. T-shaped        ClF₃
5       2        3      trig. bipyram. linear          XeF₂
6       6        0      octahedral     octahedral      SF₆
6       5        1      octahedral     sq. pyram.      BrF₅
6       4        2      octahedral     square planar   XeF₄
```

**Bond angle deviations from ideal:**
- Each lone pair compresses bonding angles by ~2–2.5°
- H₂O: ideal tetrahedral 109.5° → actual 104.5° (two lone pairs)
- NH₃: ideal 109.5° → actual 107° (one lone pair)

---

## Valence Bond Theory and Hybridization

VB theory: bonds form by overlap of atomic orbitals. To explain geometry,
atomic orbitals hybridize *before* bonding.

```
Hybridization  Component orbitals  Geometry         Bond angle  Example
──────────────────────────────────────────────────────────────────────────
sp             s + p               linear           180°        BeCl₂, CO₂
sp²            s + 2p              trig. planar     120°        BF₃, C in ethylene
sp³            s + 3p              tetrahedral      109.5°      CH₄, NH₃, H₂O
sp³d           s + 3p + d          trig. bipyram.   90°/120°    PCl₅
sp³d²          s + 3p + 2d         octahedral       90°         SF₆
```

### Sigma (σ) and Pi (π) Bonds

```
σ bond: end-on overlap, electron density along internuclear axis
        One per bond (single, double, triple all have one σ)
        Free rotation around σ bond (no directional constraint)

π bond: side-on overlap of p orbitals
        Electron density ABOVE and BELOW the internuclear axis
        One in double bond (σ + π), two in triple bond (σ + 2π)
        π bonds prevent rotation → cis/trans isomers possible

Example: ethylene H₂C=CH₂
  C: sp² hybridized → three sp² orbitals in plane (σ framework)
  One unhybridized p orbital per C, perpendicular to plane → π bond
  Result: planar molecule, 120° angles, restricted rotation
```

**Hybridization is an approximation / bookkeeping tool**, not a physical mechanism.
The underlying reality is MO theory (below). Hybridization gives you the right
geometry and bond counting without solving the MO problem.

---

## Molecular Orbital (MO) Theory

More rigorous than VB. Electrons occupy *molecular* orbitals delocalized over
the entire molecule, constructed as LCAO (Linear Combinations of Atomic Orbitals).

### LCAO for Homonuclear Diatomics

Two atomic orbitals → two molecular orbitals:

```
Bonding MO:     ψ_b = (1/√2)(ψ_A + ψ_B)    lower energy, electron density BETWEEN nuclei
Antibonding MO: ψ_a = (1/√2)(ψ_A − ψ_B)    higher energy, nodal plane between nuclei (*)

* = antibonding orbital symbol
```

### MO Diagram for O₂ (Period 2, Z > 7)

```
  Atomic Orbitals (left) — Molecular Orbitals (middle) — Atomic Orbitals (right)

  Energy levels, top (highest energy / antibonding) to bottom (lowest):

    σ*2p        antibonding
    π*2p, π*2p  (nonbonding pair)
    π2p,  π2p   bonding
    σ2p         bonding
    σ*2s        antibonding
    σ2s         bonding

  The 2p AOs of each oxygen atom feed into the π* / π / σ MOs.
  The 2s AOs of each oxygen atom feed into the σ*2s and σ2s MOs.

Fill 16 electrons (2×8): σ2s² σ*2s² σ2p² π2p⁴ π*2p²

Bond order = (bonding e⁻ − antibonding e⁻) / 2
           = (8 − 4) / 2 = 2  ✓ (O=O double bond)

Two unpaired electrons in degenerate π*2p → O₂ is PARAMAGNETIC
This is a VB theory failure — Lewis structure shows no unpaired electrons
```

### Bond Order, Length, and Energy Correlation

```
Molecule   Bond order   Bond length (Å)   Bond energy (kJ/mol)
──────────────────────────────────────────────────────────────
F₂              1         1.42              157
O₂              2         1.21              498
N₂              3         1.10              945
NO              2.5        1.15              631  (one e⁻ in π*)
O₂⁺             2.5        1.12              —    (remove one π*)
O₂⁻             1.5        1.26              —    (add one π*)
```

Higher bond order → shorter, stronger bond. This is universal.

### Molecular Orbital Diagram — Period 2 Homonuclear Summary

```
Molecule  Config              BO    Unpaired e⁻   Magnetic
──────────────────────────────────────────────────────────
H₂        σ1s²                1     0             diamagnetic
He₂       σ1s² σ*1s²          0     0             doesn't exist
Li₂       ..σ2s²              1     0             diamagnetic
B₂        ..σ2s²σ*2s²π2p²     1     2             paramagnetic
C₂        ..π2p⁴              2     0             diamagnetic
N₂        ..π2p⁴σ2p²          3     0             diamagnetic
O₂        ..σ2p²π2p⁴π*2p²     2     2             paramagnetic
F₂        ..π*2p⁴             1     0             diamagnetic
Ne₂       ..σ*2p²             0     0             doesn't exist
```

**Period 2 ordering flip at N₂:** for Z ≤ 7, σ2p is HIGHER in energy than π2p
(s-p mixing pushes σ2p up). For Z ≥ 8, σ2p is lower (standard ordering).

---

## Bond Polarity and Dipole Moments

### Electronegativity Difference → Bond Character

```
ΔEN = |EN_A − EN_B|
  ΔEN < 0.5:   nonpolar covalent (H₂, CH₄, Cl₂)
  0.5 – 1.7:   polar covalent    (H₂O, HCl, NH₃)
  > 1.7:        ionic character   (NaCl, MgO)
```

### Dipole Moment

```
μ = q × d     (charge × separation)
Units: Debye (D)  1 D = 3.336 × 10⁻³⁰ C·m

Molecular dipole = vector sum of all bond dipoles

Geometry matters:
  CO₂ (linear): two C=O dipoles cancel → μ = 0 (nonpolar molecule)
  H₂O (bent):   two O-H dipoles add    → μ = 1.85 D (polar molecule)
  CCl₄ (tetrahedral): four C-Cl cancel → μ = 0
  CHCl₃: three C-Cl don't cancel       → μ = 1.01 D
```

---

## Metallic Bonding and Band Theory

Metals: atoms contribute valence electrons to a delocalized sea (quantum → *conduction band*).

```
BAND THEORY (quantum mechanical picture):
  N metal atoms → N atomic orbitals → N MOs packed so tightly they form a BAND

  Conductor:     valence band partially filled (electrons free to move)
  Semiconductor: valence band full, small gap (~1 eV) to empty conduction band
  Insulator:     valence band full, large gap (>4 eV) to conduction band

  Temperature effect on conductors: increasing T → more phonon scattering → higher resistance
  Temperature effect on semiconductors: increasing T → electrons thermally excited → lower resistance

Fermi level: highest occupied MO at T=0 K
  In metals: Fermi level sits inside a band → metallic conduction
  In semiconductors: Fermi level sits in the gap
```

Band theory explains metallic luster (electrons interact with all photon frequencies),
ductility (electron sea moves when layers slip), and thermal conductivity (electrons carry heat).

---

## Intermolecular and Weak Interactions

Covalent bonds: 150–950 kJ/mol. Weak interactions: 0.1–40 kJ/mol.
But weak interactions dominate in biology (protein folding, DNA duplex, membrane structure).

```
Interaction         Strength         Origin                      Example
──────────────────────────────────────────────────────────────────────────
Ion–ion             250 kJ/mol       Coulomb q₁q₂/r             NaCl crystal
Ion–dipole          15–50 kJ/mol     Ion + polar molecule        Na⁺·H₂O hydration
Hydrogen bond       10–40 kJ/mol     X–H···Y (X,Y = N,O,F)      DNA base pairs, α-helix
Dipole–dipole       3–4 kJ/mol       Keesom interaction          HCl–HCl
Dipole–induced      0.5–2 kJ/mol     Debye induction             HCl–Ar
London dispersion   0.05–40 kJ/mol   Quantum fluctuation         all molecules; large for big/flat
π-stacking          2–10 kJ/mol      Aromatic quadrupole–quad.   DNA bases, graphite
Hydrophobic         variable         Entropic (water structure)  protein core, micelle formation
```

### Hydrogen Bonding in Detail

```
X–H···Y     X = donor (N, O, F — small, electronegative)
             Y = acceptor (lone pair on N, O, F)
             H must be between X and Y
             Directionality: nearly linear X–H···Y (>150°) for strongest bond

Why so strong relative to other dipole–dipole:
  H has no inner-shell electrons → partial positive charge exposed
  → unusually close approach to acceptor lone pair
  → significant covalent character (3-center 4-electron MO)

Water: each H₂O donates 2 and accepts 2 → tetrahedral H-bond network
  Ice: open hexagonal structure → lower density than liquid water
  This anomaly: why ice floats, why lakes freeze top-down
```

### London Dispersion (van der Waals)

Quantum fluctuations in electron distribution create instantaneous dipoles,
which induce dipoles in neighboring atoms → net attractive interaction.

```
London force ∝ α₁α₂ / r⁶     (α = polarizability)

Large, polarizable atoms (I₂, Xe, heavy halogens) → strong London forces
→ higher boiling point than small atoms despite being nonpolar

Boiling points of noble gases:
  He: 4 K,  Ne: 27 K,  Ar: 87 K,  Kr: 120 K,  Xe: 165 K
  → London dispersion increases down group
```

---

## Decision Cheat Sheet

| Question | Concept | Answer |
|----------|---------|--------|
| How many bonds does C form? | Valence = 4 | 4 bonds (tetrahedral sp³ or planar sp²) |
| Why is H₂O bent, not linear? | VSEPR — 2 lone pairs | Tetrahedral electron geometry, bent molecular |
| Why is O₂ paramagnetic? | MO theory | Two unpaired e⁻ in degenerate π*2p |
| Why is N₂ so unreactive? | Bond order 3 + no dipole | Triple bond (945 kJ/mol), symmetric |
| Why does HF have higher bp than HCl? | H-bond strength | F stronger H-bond acceptor/donor despite smaller size |
| Why is CO₂ nonpolar despite polar C=O bonds? | Vector sum | Linear molecule, dipoles cancel |
| Why is CO isoelectronic with N₂? | 10 e⁻, triple bond | Both: σ²π⁴, BO=3, ~same length and strength |
| Why does metallic radius increase down a group? | Higher n shell | More electron shielding, larger valence orbitals |
| Why can SF₆ have 12 bonding electrons? | Period 3, expanded octet | 3d orbitals accessible (hypervalent model) |
| Is hybridization real? | Approximation | Useful model for geometry/counting, not physical mechanism |

---

## Common Confusion Points

**Hybridization ≠ physical reality**
Hybridization is a mathematical transformation of atomic orbital basis sets
to match observed geometry. The "mixing" doesn't happen before bonding —
it's a bookkeeping trick. Chemists use it because it predicts geometry correctly.
MO theory is more rigorous but harder to apply by hand.

**Resonance ≠ equilibrium between structures**
Resonance structures are different mathematical representations of one
real electron distribution. The molecule doesn't oscillate. It has
one structure that is an average (superposition) of the contributing forms.

**Lewis octets for period-3+ elements**
The "expanded octet" in PCl₅, SF₆ is described as using d orbitals —
but modern computational chemistry suggests d orbitals contribute little.
Better description: hypervalent bonding with 3-center 4-electron (3c-4e)
MOs. The counting works either way for predicting geometry.

**Bond polarity ≠ molecular polarity**
A molecule with polar bonds can be nonpolar if the bond dipoles cancel by symmetry:
CO₂, CCl₄, BF₃, SF₆ — all have polar bonds, zero dipole moment.
Geometry determines whether dipoles add or cancel.

**Hydrogen bonds require N, O, or F**
C–H···O interactions exist and matter in protein structure but are weaker.
Strict definition: hydrogen bond requires high-EN atom bound to H.
"Weak" C–H H-bonds blur the boundary — context matters.

**London forces exist in ALL molecules**
Even polar molecules (water, HCl) have London dispersion in addition to
permanent dipole interactions. For large molecules and heavy atoms,
London forces dominate even over dipole–dipole interactions.
