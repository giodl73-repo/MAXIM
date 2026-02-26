# Physical Chemistry — Van 't Hoff, Arrhenius, Nernst, Lewis, Pauling

## The Program: Quantitative Laws for Chemical Systems

Physical chemistry emerged ~1880–1920 as the bridge between chemistry and
physics: thermodynamics applied to solutions, equilibria, and rates; quantum
mechanics applied to chemical bonds.

```
PHYSICAL CHEMISTRY — WHAT IT IS
==================================

CHEMISTRY had:
  - Qualitative reactions
  - Empirical formulas and rates
  - Phenomenological thermodynamics (Gibbs, 1870s)

PHYSICS had:
  - Statistical mechanics (Boltzmann)
  - Electromagnetism (Maxwell)
  - Later: quantum mechanics (1900–1930)

PHYSICAL CHEMISTRY bridges:
  van 't Hoff (1880s): quantitative laws for solutions (osmosis, equilibrium)
  Arrhenius (1880s):   ionic dissociation; temperature-dependence of rates
  Nernst (1880s–1906): electrochemical potential; 3rd law of thermodynamics
  Lewis (1900–1930s):  covalent bond as electron pair; activity coefficients
  Pauling (1930s–50s): quantum mechanics of the chemical bond; resonance;
                       electronegativity; protein structure

KEY ARTIFACT: The Arrhenius equation k = A·exp(-Ea/RT) appears in:
  - Semiconductor reliability modeling (MTTF at temperature)
  - Battery degradation
  - Food shelf-life calculation
  - Reaction engineering everywhere
```

---

## Jacobus Henricus van 't Hoff (1852–1911)

### Who He Was

Dutch chemist. First Nobel Prize in Chemistry, 1901 (the inaugural Nobel in
chemistry). Two main contributions: stereochemistry (tetrahedral carbon,
independently of Le Bel, 1874) and physical chemistry of solutions (1880s).

### The Contribution: Stereochemistry and Thermodynamics of Solutions

**Tetrahedral Carbon (1874)**

```
VAN 'T HOFF — STEREOCHEMISTRY (1874)
======================================

PROBLEM: Pasteur showed that tartaric acid has two mirror-image forms.
  Why? What is the 3D structure that causes chirality?

VAN 'T HOFF + LE BEL (independently, 1874):
  Carbon makes 4 bonds arranged TETRAHEDRALLY (pointing to the corners
  of a regular tetrahedron).

  If all 4 substituents on a carbon are different:
    → 2 non-superimposable mirror images (enantiomers)
    → The carbon is a "chiral center" (stereocentre)

    H   Cl          Cl  H
     \ /              \ /
      C    ≠           C
     / \              / \
   Br   F          Br   F
  (L)                (D)

  These two are related as left hand to right hand:
  identical 2D connectivity, different 3D arrangement.

CONNECTION TO PASTEUR:
  Now we know WHY tartaric acid exists as two forms:
  It has two chiral centers. The L form rotates polarized light left;
  the D form rotates it right. Racemic = 50:50 mixture.

SIGNIFICANCE:
  This is the founding insight of STEREOCHEMISTRY.
  Van 't Hoff was 22 when he published this.
  Kolbe (the prominent German chemist) called it "fantastic rubbish."
  Van 't Hoff was vindicated completely by X-ray crystallography
  (Bijvoet, 1951 — actual 3D structure confirmed).
```

**Osmotic Pressure and the van 't Hoff Equation (1885–1887)**

```
VAN 'T HOFF EQUATION
======================

PFEFFER'S OSMOTIC PRESSURE MEASUREMENTS (1877):
  Osmotic pressure π of dilute solutions was measured.
  Van 't Hoff noticed: the numbers looked like the ideal gas law.

VAN 'T HOFF (1885):

  π = nRT/V = cRT

  where:
    π = osmotic pressure (Pa)
    c = molar concentration (mol/L)
    R = gas constant (8.314 J/mol·K)
    T = absolute temperature (K)

  Identical in form to PV = nRT for ideal gases!

INTERPRETATION:
  Solute molecules behave like gas molecules in terms of entropy —
  they create pressure against a semipermeable membrane proportional to
  their concentration, just as gas molecules create pressure against walls.

APPLICATIONS:
  - Determining molecular weights of polymers by osmometry
  - Understanding how cells regulate volume (red blood cell lysis
    in hypotonic solution vs. crenation in hypertonic)
  - Dialysis (kidneys, artificial kidney machines)
  - Reverse osmosis water purification (desalination)
  - The driving force for water transport in plants (xylem)

FOR ELECTROLYTES (van 't Hoff factor i):
  NaCl dissociates: π = icRT, i ≈ 2 (Na⁺ + Cl⁻)
  CaCl₂: i ≈ 3 (Ca²⁺ + 2Cl⁻)
  This connects to Arrhenius's ionic dissociation (below).
```

**van 't Hoff Equation for Equilibrium Constants**

d(ln K)/dT = ΔH°/RT² — temperature dependence of equilibrium constant.
Integrate: ln(K₂/K₁) = -ΔH°/R · (1/T₂ - 1/T₁). Direct precursor to
Le Chatelier's principle quantified.

---

## Svante Arrhenius (1859–1927)

### Who He Was

Swedish chemist, Stockholm. Nobel Prize in Chemistry, 1903. His doctoral
thesis (ionic dissociation, 1884) was nearly failed by his committee —
he got the lowest passing grade. Twenty years later it won the Nobel Prize.
Also made early quantitative predictions about greenhouse warming from CO₂.

### The Contribution: Ionic Dissociation and the Arrhenius Equation

**Ionic Dissociation (1884)**

```
ARRHENIUS'S IONIC THEORY
==========================

CONTEXT: Faraday had established electrolysis (1830s) — electric current
  through solution causes chemical change. But why do solutions conduct
  electricity at all?

ARRHENIUS'S PROPOSAL (1884):
  When acids, bases, and salts dissolve in water, they spontaneously
  dissociate into charged ions — EVEN WITHOUT AN ELECTRIC CURRENT.

  NaCl → Na⁺ + Cl⁻  (in water)
  HCl  → H⁺ + Cl⁻   (strong acid — fully dissociated)
  CH₃COOH ⇌ CH₃COO⁻ + H⁺  (weak acid — partially dissociated)

ACIDS (Arrhenius definition, 1884):
  Substances that produce H⁺ ions in water.
  H₂SO₄ → 2H⁺ + SO₄²⁻

BASES (Arrhenius definition):
  Substances that produce OH⁻ ions in water.
  NaOH → Na⁺ + OH⁻

STRONG vs WEAK:
  Strong acids/bases: fully dissociated
  Weak acids/bases: equilibrium between associated and dissociated forms
  Ka = [H⁺][A⁻]/[HA] — acid dissociation constant
  pH = -log[H⁺]  (Sørensen's notation, 1909, based on Arrhenius's framework)

This is still taught as the first acid-base definition.
Brønsted-Lowry (1923) generalized it to proton donor/acceptor;
Lewis (below) generalized it further to electron pair acceptor/donor.
```

**The Arrhenius Equation (1889)**

```
ARRHENIUS EQUATION
===================

OBSERVATION: Reaction rates increase dramatically with temperature.
  van 't Hoff had noted d(ln k)/dT = Ea/RT² (1884).
  Arrhenius integrated this to the explicit form:

  k = A · exp(-Ea/RT)

  where:
    k   = rate constant (units depend on reaction order)
    A   = pre-exponential factor ("frequency factor") — collision frequency
    Ea  = activation energy (J/mol) — energy barrier
    R   = 8.314 J/mol·K
    T   = temperature in Kelvin

PHYSICAL INTERPRETATION:
  Molecules must exceed an energy threshold Ea to react.
  Only the fraction exp(-Ea/RT) of collisions has enough energy.
  (This is the Boltzmann factor for exceeding Ea.)

LINEAR FORM (Arrhenius plot):
  ln(k) = ln(A) - Ea/RT
  Plot ln(k) vs. 1/T → straight line, slope = -Ea/R

USES IN TECHNOLOGY (the MIT/Azure VP connection):
  Semiconductor reliability (MTTF models):
    MTTF = A · exp(Ea/kT)
    Every processor reliability spec uses this.
    Ea ≈ 0.6–0.9 eV for most failure mechanisms.
    10°C rise → ~2× shorter lifetime (rule of thumb, from Arrhenius).

  Battery degradation:
    Capacity fade ∝ exp(-Ea/RT)
    EV battery pack lifetime modeled with Arrhenius at cell level.

  Chemical vapor deposition (chip fab):
    Deposition rate ∝ exp(-Ea/RT)
    Temperature control in CVD furnaces follows Arrhenius.

  Food shelf life, pharmaceutical stability: same equation.
```

---

## Walther Nernst (1864–1941)

### Who He Was

German physical chemist. Nobel Prize in Chemistry, 1920 (for the 3rd law).
Student of Arrhenius and van 't Hoff. Invented an early electric lamp
(the Nernst lamp, predecessor to tungsten filament lamps). Worked on
acoustics, thermodynamics, and chemistry. In WWI, initiated Germany's
chemical weapons program (a catastrophic use of his talents).

### The Contribution: Electrochemical Potential and the Third Law

**The Nernst Equation (1889)**

```
NERNST EQUATION
================

PROBLEM: The EMF (voltage) of an electrochemical cell depends on
  concentrations. At standard conditions (1 M, 1 atm) → standard EMF E°.
  What is EMF at other concentrations?

NERNST EQUATION:
  E = E° - (RT/nF) · ln(Q)

  where:
    E   = actual cell potential (V)
    E°  = standard cell potential (V)
    R   = 8.314 J/mol·K
    T   = temperature (K)
    n   = number of electrons transferred
    F   = Faraday constant = 96,485 C/mol
    Q   = reaction quotient [products]/[reactants]

  At 25°C: E = E° - (0.0592/n) · log₁₀(Q)

APPLICATIONS:
  - Ion-selective electrodes (pH meters work on the Nernst equation)
  - Biological membrane potentials (action potential in neurons):
    E_Nernst = (RT/zF) · ln([ion_out]/[ion_in])
    Na⁺ Nernst potential ≈ +60 mV, K⁺ Nernst potential ≈ -90 mV
    Resting membrane potential ≈ -70 mV (weighted mix)
  - Electroplating, corrosion engineering, battery design
  - Gibbs free energy connection: ΔG = -nFE

NERNST EQUATION AT EQUILIBRIUM:
  When Q = K (equilibrium constant): E = 0 (no net driving force)
  → ΔG° = -nFE° = -RT·ln(K)
  Links electrochemistry to thermodynamics.
```

**The Third Law of Thermodynamics (1906)**

```
THIRD LAW (NERNST HEAT THEOREM, 1906)
=======================================

First law:  Energy is conserved. ΔU = q - w.
Second law: Entropy of the universe increases. dS ≥ δQ/T.
Third law (Nernst): As T → 0 K, the entropy of a perfect crystal → 0.

  lim(T→0) S = 0  [for a perfect crystal]

STATEMENT: It is impossible to reach absolute zero by any finite number
  of thermodynamic steps.

WHY IT MATTERS:
1. Establishes an ABSOLUTE SCALE for entropy (unlike energy, which has
   an arbitrary zero).
2. Enables calculation of absolute entropies from heat capacity data:
   S(T) = ∫₀ᵀ (Cp/T) dT
3. Implications for low-temperature physics and quantum behavior
   (Bose-Einstein condensates, superconductivity).
4. Practical: explains why cooling to absolute zero is impossible in practice.

ENTROPY OF REAL SUBSTANCES AT 0 K:
  Glasses have residual entropy (disorder frozen in).
  CO has residual entropy of Rln(2) at 0 K (two orientations: CO vs OC
  in the crystal, frozen in before equilibrium).
  This is directly connected to the third law.
```

---

## Gilbert Newton Lewis (1875–1946)

### Who He Was

American chemist, Berkeley. Never won the Nobel Prize — widely considered
one of the greatest chemistry Nobel omissions in history. The Prize
committee had a complicated relationship with American chemists in his era.
He made foundational contributions to chemical bonding, acid-base theory,
and thermodynamics.

### The Contribution: The Covalent Bond and Chemical Thermodynamics

**The Lewis Dot Structure and Covalent Bond (1916)**

```
LEWIS'S COVALENT BOND
=======================

CONTEXT (1916): Ionic bonding (electron transfer) was understood.
  But why do H₂, CH₄, N₂ exist? Atoms of similar electronegativity
  don't transfer electrons.

LEWIS (1916) — "The Atom and the Molecule":
  The covalent bond is a SHARED PAIR OF ELECTRONS.

  H:H    → hydrogen molecule (one shared pair = single bond)
  O::O   → oxygen molecule (two shared pairs = double bond)
  N:::N  → nitrogen molecule (three shared pairs = triple bond)

  Lewis dot structures: each dot represents one valence electron.
  An octet (8 electrons around each heavy atom) = stable configuration.
  Exception: H wants a duet (2 electrons, like He).

WHY H₂ IS STABLE:
  Both hydrogens share the two electrons.
  Neither "owns" them exclusively.
  The quantum mechanical explanation (orbital overlap, Heitler-London 1927)
  came 11 years after Lewis's model, and confirmed it.

MOLECULES WITH LEWIS STRUCTURES:

  Methane CH₄:
        H
        |
    H - C - H    (each line = shared electron pair)
        |
        H

  Each C-H bond is a shared pair.
  4 bonds × 2 electrons = 8 electrons around carbon (octet satisfied).

  Water H₂O:
    H-O-H  with 2 lone pairs on O.
    O has 4 electron pairs: 2 bonding, 2 non-bonding.

LONE PAIRS:
  Non-bonding electron pairs on atoms — important for molecular geometry
  (VSEPR theory) and Lewis acid-base chemistry (below).
```

**Lewis Acids and Bases (1923)**

```
LEWIS ACID-BASE THEORY
=======================

ARRHENIUS (1884): Acid = H⁺ source; Base = OH⁻ source.
BRØNSTED-LOWRY (1923): Acid = proton donor; Base = proton acceptor.
LEWIS (1923): Acid = electron pair ACCEPTOR; Base = electron pair DONOR.

Lewis base: has a lone pair to donate.
Lewis acid: has an empty orbital to accept a lone pair.

EXAMPLES:
  BF₃ + NH₃ → F₃B-NH₃
  BF₃ is Lewis acid (empty p orbital on B accepts N's lone pair)
  NH₃ is Lewis base (lone pair on N)

  Metal ions are Lewis acids: Fe³⁺, Cu²⁺, Zn²⁺
  Water, ammonia, chloride are Lewis bases
  → Coordination chemistry (transition metal complexes) all follows
    from Lewis acid-base theory.

SCOPE: Lewis's definition is the most general.
  Every Brønsted acid is a Lewis acid (H⁺ accepts an electron pair).
  Many Lewis acids are not Brønsted acids (BF₃, AlCl₃, etc.).

IN TECHNOLOGY:
  Acid catalysis in industrial chemistry (zeolites are Lewis acids)
  Drug-receptor binding (Lewis acid-base interactions at active sites)
  Coordination chemistry for metal extraction and purification
```

**Chemical Thermodynamics: Activity and Fugacity**

Lewis formalized the concepts of activity (a = effective concentration
in non-ideal solutions) and fugacity (effective pressure in non-ideal gases),
making thermodynamic calculations applicable to real chemical systems rather
than just ideal ones. Every real-world equilibrium calculation in industrial
chemistry uses Lewis's formalism.

---

## Linus Pauling (1901–1994)

### Who He Was

American chemist, Caltech. Two Nobel Prizes: Chemistry (1954) for the nature
of the chemical bond; Peace (1962) for nuclear test ban activism.
The only person to win two unshared Nobel Prizes. He was also wrong
about DNA structure (his "triple helix" was incorrect — Watson and Crick
beat him), but right about almost everything else.

### The Contribution: Quantum Mechanics of the Chemical Bond

**Electronegativity (1932)**

```
ELECTRONEGATIVITY
==================

PROBLEM: In HCl, both atoms contribute to the bond, but chlorine
  "pulls" the electrons toward itself. How do we quantify this tendency?

PAULING ELECTRONEGATIVITY SCALE (1932):
  Assign each element a number χ (chi) between 0.7 and 4.0.
  The more electronegative, the more it attracts bonding electrons.

  F: 4.0 (most electronegative)   Na: 0.9
  O: 3.5                           Mg: 1.2
  N: 3.0, Cl: 3.2                  C:  2.5
  H: 2.2                           Si: 1.9
  S: 2.6, P: 2.2                   Fe: 1.8

Pauling defined χ from bond energies:
  |χ_A - χ_B|² ∝ "extra" ionic stabilization energy of A-B bond
  (A-B is stronger than the average of A-A and B-B bonds by an amount
  proportional to the ionic character)

BOND TYPE FROM ELECTRONEGATIVITY DIFFERENCE:
  Δχ = 0:     Purely covalent (H₂, Cl₂)
  Δχ = 0–0.4: Mostly covalent, slightly polar
  Δχ = 0.5–1.7: Polar covalent (HCl: Δχ=1.0, H₂O: Δχ=1.3)
  Δχ > 1.7:   Ionic (NaCl: Δχ=2.1, NaF: Δχ=3.1)

  (The boundary is gradual, not sharp.)

APPLICATIONS:
  Predicts molecular polarity → dipole moments
  Explains solubility ("like dissolves like" — quantified by Δχ)
  Drug design: polarity affects membrane permeability
  Semiconductor doping: Si (2.5), P (2.2), B (2.0) have Δχ near zero
    → dopant bonds are covalent, not ionic
```

**Resonance and Hybridization (1928–1931)**

```
PAULING'S RESONANCE THEORY
============================

BENZENE PROBLEM: Kekulé proposed alternating single/double bonds.
  But all C-C bonds in benzene are identical (length 1.40 Å).

PAULING (1928, extended 1931–1933):
  The actual molecule is a RESONANCE HYBRID of contributing structures.
  No single Lewis structure describes it correctly.
  The true electron distribution is a quantum superposition:

  Kekulé 1 + Kekulé 2 + (minor Dewar structures) = benzene

  Each bond is partly single, partly double → intermediate length.
  The "resonance energy" (extra stabilization) ≈ 150 kJ/mol.

HYBRIDIZATION:
  Pauling introduced sp, sp², sp³ hybridization to explain molecular geometry.

  sp³ hybridization (carbon in CH₄):
    1 s + 3 p orbitals → 4 equivalent sp³ orbitals
    Pointing to tetrahedral corners (109.5°)
    Explains why methane is tetrahedral (not flat or L-shaped)

  sp² (carbon in ethylene C₂H₄, benzene):
    1 s + 2 p → 3 sp² orbitals (120° apart, flat)
    1 remaining p orbital → forms π bond

  sp (carbon in acetylene C₂H₂):
    1 s + 1 p → 2 sp orbitals (180° apart, linear)
    2 remaining p → two π bonds (triple bond)

MODERN STATUS:
  Resonance is a description of limitations of Lewis structures.
  Molecular orbital theory (Hückel, Woodward-Hoffmann) gives
  a more complete picture. But resonance + hybridization is still
  taught as the practical working model for organic chemistry.
```

**The Alpha Helix and Beta Sheet (1951)**

```
PROTEIN STRUCTURE (1951)
=========================

Pauling used his knowledge of:
  - X-ray diffraction (learned from Bragg)
  - Covalent bond geometry (from quantum chemistry work)
  - Hydrogen bonding (he had formalized H-bond theory)

to deduce the alpha-helix:
  A right-handed helix where each NH hydrogen bonds to the C=O
  of the amino acid 4 positions earlier in the chain.
  Repeat unit: 3.6 amino acids per turn.
  Rise per residue: 1.5 Å.

He also predicted the beta-sheet (extended chains hydrogen-bonded
side by side).

He did this from first principles (bond lengths, angles, hydrogen bond
geometry) WITHOUT knowing any protein sequence. He built physical models.

Watson and Crick (DNA, 1953) acknowledged that Pauling's model-building
method inspired their approach. Pauling himself was racing to solve DNA —
his triple-helix model (1953) was wrong, partly because he didn't have
access to Franklin's X-ray data.

SIGNIFICANCE:
  The alpha helix and beta sheet are the two universal secondary structures
  of proteins. All of structural biology descends from this.
```

---

## Comparison Table

| Figure | Dates | Core Contribution | What Changed | Legacy |
|--------|-------|-------------------|-------------|--------|
| **van 't Hoff** | 1852–1911 | Tetrahedral carbon; osmotic pressure equation | 3D molecular structure; quantitative solution chemistry | Stereochemistry; reverse osmosis; first Nobel in Chemistry |
| **Arrhenius** | 1859–1927 | Ionic dissociation; Arrhenius equation | Acids/bases as ions; rate-temperature law | pH chemistry; semiconductor lifetime models |
| **Nernst** | 1864–1941 | Nernst equation; 3rd law | Quantitative electrochemistry; absolute entropy | Ion-selective electrodes; membrane biology; batteries |
| **Lewis** | 1875–1946 | Covalent bond as electron pair; Lewis acids/bases | Molecular bonding theory | Structural chemistry; acid-base chemistry |
| **Pauling** | 1901–1994 | Electronegativity; resonance; hybridization; protein secondary structure | Quantum chemistry of bonds; structural biology | Everything in modern chemistry and biochemistry |

---

## Who to Cite for What

| Concept | Cite | Notes |
|---------|------|-------|
| Tetrahedral carbon / chirality explanation | van 't Hoff + Le Bel | 1874, independently |
| Osmotic pressure π = cRT | van 't Hoff | 1885–1887 |
| van 't Hoff factor i for electrolytes | van 't Hoff | |
| Ionic dissociation theory | Arrhenius | 1884 |
| Arrhenius acid/base definition | Arrhenius | H⁺ and OH⁻ |
| Arrhenius equation k = A·exp(-Ea/RT) | Arrhenius | 1889 |
| Nernst equation E = E° - (RT/nF)ln(Q) | Nernst | 1889 |
| Third law of thermodynamics | Nernst | 1906 |
| Covalent bond as shared electron pair | Lewis | 1916 |
| Lewis dot structures / octet rule | Lewis | |
| Lewis acid-base theory (e⁻ pair donor/acceptor) | Lewis | 1923 |
| Activity / fugacity in thermodynamics | Lewis | |
| Electronegativity scale | Pauling | 1932 |
| Resonance theory | Pauling | 1928–1933 |
| sp/sp²/sp³ hybridization | Pauling | |
| Alpha helix and beta sheet | Pauling | 1951 |

---

## Common Confusion Points

**"Van 't Hoff only worked on osmosis"** — His tetrahedral carbon paper (1874)
is the foundation of stereochemistry. He published it at 22. The osmosis work
was 10+ years later. He essentially did two Nobel Prize-worthy research programs.
He won for the osmosis/equilibrium work.

**"The Arrhenius equation is a physics formula"** — It derives from the Boltzmann
distribution (statistical mechanics), but it was Arrhenius who applied it to
reaction rates with the concept of activation energy as a barrier. The physical
chemists borrowed from statistical physics and made it chemically useful. In
semiconductor reliability, it's often called the "Arrhenius model" with no
mention of its chemical origins.

**"Lewis structures are just a mnemonic"** — They encode real physical information:
electron pair sharing is the quantum mechanical reality, and Lewis's 1916 paper
anticipated much of what wave mechanics explained 11 years later. The covalent
bond as a shared electron pair is a quantum mechanical result (Heitler-London,
1927); Lewis predicted it from electrochemical reasoning.

**"Pauling made the covalent bond quantum mechanical"** — More precisely:
Pauling translated quantum mechanics (wave functions, orbital overlap) into
chemical language (hybridization, resonance, electronegativity) that chemists
could use without solving Schrödinger equations. His framework is an
approximation, but a remarkably good one. Molecular orbital theory (Hückel,
Woodward-Hoffmann) is more rigorous, but Pauling's language (sp³, aromatic,
resonance) is what organic chemists use daily.

**"Lewis never won the Nobel — that's just politics"** — It was politics (partly).
But also: Arrhenius was on the Nobel Committee and held a grudge over Lewis's
criticism of Arrhenius's strong electrolyte theory. Personal enmities in small
academic communities can determine Nobel outcomes. Lewis's contributions —
covalent bond theory, Lewis acids/bases, thermodynamic activity — are
unambiguously foundational.
