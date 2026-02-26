<!-- @editor[diagram/P1]: No landscape diagram — guide opens with hydrogen atom detail instead of establishing the full picture (atomic structure → multi-electron → periodic table → spectroscopy → computation). Needs a visual map showing how the pieces relate before drilling in. -->
# 01-ATOMIC-QUANTUM — Atomic Structure & Quantum Mechanics of Chemistry

> The hydrogen atom solved exactly. Multi-electron approximations. Quantum numbers
> as orbital taxonomy. Periodic table as electron-configuration map. Spectroscopy
> as the experimental bridge between QM and chemistry.

---

## The Hydrogen Atom — The Exact Solution

The hydrogen atom (one proton, one electron) is the *only* atom with an exact
analytic solution. Everything else in atomic chemistry is an approximation derived
from it. Understanding *why* it's solvable and what breaks in multi-electron atoms
is the foundation.

```
Schrödinger equation (time-independent):
Ĥ ψ = E ψ

Hamiltonian:
Ĥ = − (ℏ²/2m)∇² − e²/(4πε₀r)
        kinetic       Coulomb attraction

Separation of variables in spherical coordinates (r, θ, φ):
ψ(r,θ,φ) = R(r) · Y(θ,φ)
             radial  angular

Angular piece: spherical harmonics Yₗᵐ(θ,φ)  — standard basis on S²
Radial piece: associated Laguerre polynomials × exponential decay
```

The exact energy eigenvalues (in eV):

```
Eₙ = − 13.6 eV / n²       n = 1, 2, 3, …

E₁ = −13.6 eV  (ground state)
E₂ = −3.4 eV
E∞ = 0          (ionization threshold)
```

**What the quantum numbers actually are:**
They emerge from the separation-of-variables boundary conditions — not postulated,
they fall out of requiring ψ to be square-integrable and single-valued.

---

## Quantum Number Taxonomy

```
Symbol  Name             Range             Physical meaning
────────────────────────────────────────────────────────────────────
n       Principal        1, 2, 3, …        Shell / energy (for H)
                                            Distance scale ~ n²a₀

l       Angular momentum 0, 1, …, n-1      Orbital shape; magnitude |L| = ℏ√(l(l+1))
                         (s, p, d, f, g)

mₗ      Magnetic         -l, …, 0, …, +l   Orientation (z-component of L)

mₛ      Spin             ±½                Intrinsic spin (no classical analog)
```

**Letter-to-number map (historical spectroscopy labels):**

```
l = 0 → s   (sharp)
l = 1 → p   (principal)
l = 2 → d   (diffuse)
l = 3 → f   (fundamental)
l = 4 → g   (continuation alphabetically)
```

**Orbital count per subshell:** 2l + 1 orbitals, each holding 2 electrons (±½ spin)

```
s subshell (l=0): 1 orbital  ×  2 electrons  =  2 per shell
p subshell (l=1): 3 orbitals ×  2 electrons  =  6
d subshell (l=2): 5 orbitals ×  2 electrons  = 10
f subshell (l=3): 7 orbitals ×  2 electrons  = 14
```

---

## Orbital Shapes (Physical Content of ψ)

`|ψ|²` is electron probability density. Orbital "shapes" are boundary surfaces
enclosing ~90% of the probability density.

```
s orbitals:    spherically symmetric.  ψ ∝ e^(-r/na₀)
               Nodes: n-1 spherical nodes (radial)

p orbitals:    dumbbell along x, y, or z axis.
               px ∝ r·e^(-r)·sin(θ)cos(φ),  etc.
               1 angular node (the nodal plane through nucleus)
               Nodes: n-2 radial + 1 angular = n-1 total

d orbitals:    Four-lobed (dxy, dxz, dyz, dx²-y²) or dz² (two lobes + torus)
               2 angular nodes

f orbitals:    Complex multilobed shapes; 3 angular nodes
               Rarely need explicit visualization at this level
```

**Node count rule:** ψ has n-1 total nodes = (n-l-1) radial + l angular.
More nodes → higher kinetic energy (standing wave analogy).

---

## Multi-Electron Atoms — Why the Exact Solution Breaks

In multi-electron atoms, the Hamiltonian gains electron–electron repulsion terms:

```
Ĥ = Σᵢ [−(ℏ²/2m)∇ᵢ² − Ze²/rᵢ] + Σᵢ<ⱼ e²/rᵢⱼ
                                        ↑
                        electron–electron repulsion:
                        NO analytic solution for this term
```

The e–e repulsion breaks the exact separability. Every multi-electron atom
requires approximation. The most important for chemistry:

### Hartree-Fock / Self-Consistent Field (SCF)

Each electron moves in the *average* field of all others.
Yields single-electron wavefunctions called **orbitals** — hydrogenic in form
but with modified effective charges.

### Shielding and Effective Nuclear Charge (Zeff)

Outer electrons are partially screened from the nucleus by inner electrons:

```
Zeff = Z − σ
where σ = shielding constant (sum of contributions from other electrons)

Slater's rules (approximate σ):
  Same shell (n,l):      0.35 each
  One shell in (n-1):    0.85 each (for s,p) or 1.00 each (for d,f)
  Two+ shells in:        1.00 each

Examples:
  Na (Z=11), valence 3s electron:
  σ = (2 × 1.00) + (8 × 0.85) = 8.80
  Zeff = 11 − 8.80 = 2.20

  Cl (Z=17), valence 3p electron:
  σ = (2 × 1.00) + (8 × 0.85) + (6 × 0.35) = 10.90
  Zeff = 17 − 10.90 = 6.10
```

Higher Zeff → tighter, lower-energy orbital → harder to remove electron.
This is the root cause of most periodic trends.

### Orbital Energy Ordering in Multi-Electron Atoms

For hydrogen: energy depends *only* on n (all l degenerate in same shell).
For multi-electron: s penetrates closer to nucleus than p → lower energy than p.

```
Observed ordering (n + l rule / Madelung rule):
1s < 2s < 2p < 3s < 3p < 4s < 3d < 4p < 5s < 4d < 5p < 6s < 4f < 5d < ...

Remember: 4s fills before 3d because 4s electrons penetrate to nucleus
(r = 0 has finite ψ for s orbitals, not for d orbitals).
```

---

## Electron Configuration

Three rules:

1. **Aufbau** ("build-up"): fill lowest energy orbitals first
2. **Pauli exclusion**: no two electrons can have identical (n, l, mₗ, mₛ) — at most 2 per orbital
3. **Hund's rules**: for degenerate orbitals (same subshell), maximize unpaired spin (maximize S) before pairing

```
H:   1s¹
He:  1s²
Li:  [He] 2s¹
C:   [He] 2s² 2p²     (two 2p electrons in DIFFERENT orbitals, parallel spin)
Ne:  [He] 2s² 2p⁶     (full 2p shell)
Na:  [Ne] 3s¹
Cr:  [Ar] 3d⁵ 4s¹     ← exception: half-filled d is extra stable (Hund's)
Cu:  [Ar] 3d¹⁰ 4s¹    ← exception: full d is extra stable
```

**Isoelectronic series**: atoms/ions with same electron count.
Na⁺, Ne, F⁻, O²⁻ all have 10 electrons. Their properties differ
solely because of nuclear charge Z → Zeff differences.

---

## The Periodic Table as an Electron-Configuration Map

```
                   s-block      p-block
                   (l=0)        (l=1,2)
Period   1:  H He
         2:  Li Be | B  C  N  O  F  Ne
         3:  Na Mg | Al Si P  S  Cl Ar
         4:  K  Ca | d-block (l=2) | Ga Ge As Se Br Kr
             ...  Sc Ti V Cr Mn Fe Co Ni Cu Zn ...
         6:  Cs Ba | f-block (l=3)             | Tl Pb Bi Po At Rn
             ...  La-Lu (lanthanides) / Hf ... /

Blocks:
  s-block  (groups 1-2):       filling ns subshell
  p-block  (groups 13-18):     filling np subshell
  d-block  (groups 3-12):      filling (n-1)d subshell
  f-block  (lanthanides/       filling (n-2)f subshell
            actinides):
```

**Why periods have the lengths they do:**
Period 1: 2 elements  (1s fills: 2 electrons)
Period 2: 8 elements  (2s + 2p: 2+6)
Period 3: 8 elements  (3s + 3p: 2+6)
Period 4: 18 elements (4s + 3d + 4p: 2+10+6)
Period 6: 32 elements (6s + 4f + 5d + 6p: 2+14+10+6)

---

## Periodic Trends

All trends derive from two competing effects: **increasing Z** and **increasing shielding**.

```
ATOMIC RADIUS
  Across period (left → right): DECREASES
    Reason: Z increases, same shell, Zeff rises → orbital contracts
  Down group (top → bottom):   INCREASES
    Reason: outer electrons enter higher n shell

IONIZATION ENERGY (IE₁ = energy to remove first electron)
  Across period: INCREASES (higher Zeff → electron harder to remove)
  Down group:   DECREASES (outer electron farther from nucleus)
  Exceptions:
    Group 2 → Group 13: IE drops (removing 2p vs 2s; 2p higher energy)
    Group 15 → Group 16: IE drops (pairing 2p forces electrons into same orbital; repulsion)

ELECTRON AFFINITY (energy released when anion formed: X + e⁻ → X⁻)
  Most negative: halogens (F, Cl) — one e⁻ away from noble gas config
  Counterintuitive: F has lower |EA| than Cl (F 2p orbital small, electron–electron repulsion)
  Noble gases: EA ≈ 0 or positive (stable filled shells resist additional electron)

ELECTRONEGATIVITY (Pauling scale)
  Most electronegative: F (3.98) > O (3.44) > N (3.04) > Cl (3.16)
  Least: Fr, Cs (~0.7-0.8)
  Trend: same as IE (high IE → high EN)
  Pauling definition: derived from bond dissociation energies
  Mulliken definition: EN ∝ (IE + EA)/2  (more physically transparent)

POLARIZABILITY
  Large, diffuse electron cloud: high polarizability
  Trend: opposite to IE — large atoms, heavy halogens, softly held electrons
  Relevance: London dispersion forces (van der Waals), soft–hard acid–base theory
```

---

## Spectroscopy — The Experimental Bridge

Quantum mechanics predicts discrete energy levels. Spectroscopy measures them.

### Atomic Emission / Absorption

Photon absorbed or emitted when electron transitions between energy levels:

```
ΔE = Efinal − Einitial = hν = hc/λ

For hydrogen (Rydberg formula):
  1/λ = R∞ (1/n₁² − 1/n₂²)
  R∞ = 1.097 × 10⁷ m⁻¹ (Rydberg constant)

Series:
  Lyman:   n → 1   UV
  Balmer:  n → 2   visible (Hα at 656 nm = red, Hβ at 486 nm = blue-green)
  Paschen: n → 3   IR
```

**Why discrete lines identify elements**: electron configurations are unique.
An atomic "fingerprint" — the basis of all spectroscopic analysis from flame
tests to stellar composition to ICP-MS.

### X-Ray Spectroscopy

Transitions involving inner-shell electrons (1s → vacancy created by high-energy photon):
- **Kα emission**: L→K transition (n=2 → n=1 vacancy)
- **Kβ emission**: M→K transition
- Energies depend on Z → **elemental fingerprint** (EDX in electron microscopy, XRF)

### Selection Rules

Not all transitions are allowed. Electric dipole selection rules:

```
Allowed:   Δl = ±1,   Δmₗ = 0, ±1,   Δmₛ = 0
Forbidden: Δl = 0, ±2, …

Physical reason: photon carries angular momentum ℏ → must be absorbed/emitted
in the transition. Δl = ±1 conserves angular momentum.
"Forbidden" transitions occur but are slower (magnetic dipole, quadrupole).
```

### Molecular Spectroscopy (Preview for Later Modules)

| Type | What it probes | Frequency range |
|------|---------------|-----------------|
| Microwave rotational | Molecular rotation, bond lengths | GHz range |
| IR vibrational | Bond stretching/bending (IR active if Δμ ≠ 0) | 400–4000 cm⁻¹ |
| Raman | Vibrational (Raman active if Δα ≠ 0) | Stokes/anti-Stokes shifts |
| UV-Vis | Electronic transitions (π→π*, n→π*) | 200–800 nm |
| NMR | Nuclear spin in magnetic field (chemical shift) | Radio frequencies |
| EPR/ESR | Unpaired electron spin | Microwave |

---

## Relativistic Effects in Heavy Atoms

For heavy atoms (Z > 50), electron velocities approach c → relativistic corrections matter:

```
Relativistic mass increase → orbital contraction → lower energy for s (and p) orbitals
                          → relative expansion of d and f orbitals

Consequences:
  Au (gold): relativistic contraction of 6s → absorbs blue, reflects yellow → gold color
  Hg: 6s contracted → liquid at room temperature (weak metallic bonding)
  Pb: relativistic stabilization of 6s² → "inert pair effect" → Pb²⁺ preferred over Pb⁴⁺
  Pt, Pd: enables catalytic activity (d orbital accessibility)
  Superheavy elements: chemistry differs substantially from periodic-table prediction
```

The Dirac equation replaces Schrödinger for relativistic QM.
In practice: relativistic ECPs (effective core potentials) handle this in DFT/HF codes.

---

<!-- @editor[bridge/P2]: No old-world bridge — e.g., classical mechanics → quantum mechanics transition, or numerical methods (Gaussian elimination, matrix diagonalization) → computational chemistry methods. A senior engineer with linear algebra background would benefit from connecting SCF iteration to iterative eigenvalue solvers they already know. -->
## Quantum Chemistry Computation — The Ladder

```
Method          What it solves              Cost        Accuracy
────────────────────────────────────────────────────────────────────
HF/SCF          Mean-field (no correlation) O(N⁴)       ~95% of binding energy
DFT             Exchange-correlation approx  O(N³)       Good for structure/energy
MP2             2nd-order perturbation      O(N⁵)       Better correlation
CCSD            Singles/doubles CC          O(N⁶)       High accuracy
CCSD(T)         Gold standard               O(N⁷)       Benchmark quality
FCI             Exact (within basis)        O(Nᵉˣᵖ)     Only tiny molecules

Basis sets:
  STO-3G    Minimal — fast, qualitative only
  6-31G(d)  Pople split-valence — everyday DFT
  cc-pVTZ   Dunning correlation-consistent — high-accuracy calculations
  aug-cc-pVTZ  adds diffuse functions — needed for anions, polarizabilities
```

For 99% of chemistry, DFT (density functional theory — B3LYP, M06, ωB97X-D)
with a triple-ζ basis set gives reliable structures, energies, and spectra.

---

## Decision Cheat Sheet

| Question | Concept | Key equation / concept |
|----------|---------|----------------------|
| Why does Na have lower IE than Mg? | Zeff trend across period | Zeff(Na) < Zeff(Mg) → 3s electron easier to remove |
| Why does Cl have higher IE than S? | Hund's rule penalty | S 3p⁴ has paired electrons (repulsion), lower IE |
| Why is F more electronegative than I? | Zeff + orbital size | F 2p: smaller, tighter, higher Zeff |
| Why is gold yellow? | Relativistic contraction | 6s orbital lowered → absorbs blue photons |
| Why does Cu deviate from Aufbau? | Half-/full-shell stability | [Ar] 3d¹⁰ 4s¹ lower energy than [Ar] 3d⁹ 4s² |
| Why do atomic spectra have discrete lines? | Quantized energy levels | ΔE = hν, transitions between eigenvalues |
| Why is 4s filled before 3d? | Orbital penetration | 4s electrons penetrate near nucleus; lower energy |
| How many d electrons does Fe²⁺ have? | Configuration + ionization | Fe = [Ar]3d⁶4s²; Fe²⁺ loses 4s first → [Ar]3d⁶ |

---

## Common Confusion Points

**"Orbitals" are not orbits**
Bohr orbits (1913) are wrong for electron trajectories. Quantum orbitals are
wave functions — probability amplitude distributions. There is no trajectory.
The orbital is a *region of space* where the electron is likely to be found.

**4s fills before 3d but ionizes first**
Filling order: 4s before 3d (Aufbau, lower energy when empty).
Ionization order: 4s removed first from transition metals.
The two orders differ because the energy ordering *changes* once the 3d is populated.
Fe is [Ar]3d⁶4s², Fe²⁺ is [Ar]3d⁶ (not [Ar]3d⁴4s²).

**l quantum number labels are historical accidents**
s/p/d/f = sharp/principal/diffuse/fundamental — spectroscopic series names
from the 1800s that happened to map to l = 0/1/2/3. The labels have no
mnemonic connection to orbital shape.

**Nodes ≠ zero probability everywhere**
A radial node is a *sphere* where ψ = 0. An angular node is a *plane* (or cone)
where ψ = 0. The electron has zero probability at a node but non-zero probability
both inside and outside — quantum mechanics, not a shell.

**Electron "spin" is not rotation**
Spin is a purely quantum mechanical property with no classical analog.
A spinning charged sphere model gives the wrong gyromagnetic ratio by factor 2.
The "spin" label is historical; it refers to intrinsic angular momentum.

**Electronegativity scales are not unique**
Pauling (bond energies), Mulliken ((IE+EA)/2), Allred-Rochow (Zeff/r²),
Allen (spectroscopic average energy) — all different numbers, all valid for
their intended use. When in doubt which to use: Pauling for organic chemistry,
Allen for precise trends.
