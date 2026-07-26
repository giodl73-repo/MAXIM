---
maxim_schema: maxim.frontmatter.v1
id: maxim:chemistry:physical-chemistry-depth
kind: guide
module: chemistry
section: chemistry
title: Physical Chemistry Depth - Stat Thermo, Non-Ideal Solutions, Surfaces
status: source-custody
source_custody: partial
current_path: chemistry/09-PHYSICAL-CHEMISTRY-DEPTH.md
canonical_path: chemistry/09-PHYSICAL-CHEMISTRY-DEPTH.md
backsource_ids: [proof-backfill:chemistry:09-physical-chemistry-depth, git-history:chemistry:09-physical-chemistry-depth]
concepts: [statistical-thermodynamics, partition-function, activity-coefficient, adsorption, surface-catalysis]
root_concepts: [physical-chemistry]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Physical Chemistry Depth — Stat Thermo, Non-Ideal Solutions, Surfaces

**This guide owns** the theory floor that the rest of the module stands on:
statistical thermodynamics (partition functions → bulk thermochemistry), non-ideal
solution theory (activity, Debye-Hückel), and interfacial/surface chemistry
(adsorption isotherms, heterogeneous-catalysis kinetics). **It sits between**
`natural-sciences/03-04` (the four laws, ΔG, intro kinetics — assumed, not repeated)
and `statistical-mechanics/` in Math & Physics (which owns condensed-matter phase
transitions, Ising, RG). Same formalism, different problem: here partition functions
predict *chemical* equilibria and rates, not critical exponents.

```
FROM ONE MOLECULE'S ENERGY LEVELS TO BULK CHEMISTRY
==========================================================================
  quantum energy levels (translation, rotation, vibration, electronic)
              |
              v   Boltzmann weighting
  PARTITION FUNCTION  q = SUM g_i exp(-eps_i / kT)  = q_t q_r q_v q_e
              |
              |----->  THERMODYNAMICS (U, S, A, Cv)
              |----->  EQUILIBRIUM CONSTANT K
                       |
                       v
  REAL SYSTEMS ARE NON-IDEAL:
    solutions  -> activity a = gamma*x ; Debye-Huckel for ions
    interfaces -> adsorption (Langmuir/BET) ; surface catalysis
==========================================================================
```

---

## Statistical Thermodynamics: q Is the Bridge

Everything thermodynamic about an ideal gas of independent molecules is encoded in
the **molecular partition function** q — the Boltzmann-weighted count of accessible
states. Because the energy separates, q factorizes:

```
   q = q_trans * q_rot * q_vib * q_elec

   q_trans = (2*pi*m*kT / h^2)^(3/2) * V         (huge; ~10^30 for a small molecule)
   q_rot   = T / (sigma * Theta_rot)             (linear rotor; Theta_rot = hcB/k)
   q_vib   = 1 / (1 - exp(-Theta_vib / T))       (per mode; Theta_vib = h*nu/k)
   q_elec  = g_0  (degeneracy of the ground state; add excited terms if low-lying)
```

Characteristic temperatures make the physics legible: Θ_rot is small (N₂: 2.9 K) so
rotation is fully excited at 298 K; Θ_vib is large (N₂: 3374 K) so vibration is
mostly frozen in the ground state at 298 K. That single comparison tells you which
degrees of freedom contribute to heat capacity.

**Thermodynamic functions** come from the *canonical* partition function. For N
independent, **indistinguishable** molecules the system partition function is
**Q = qᴺ/N!** — the N! removes the overcounting of identical-particle permutations
and is what makes entropy extensive (it resolves the Gibbs paradox). Every bulk
quantity follows from Q, and the Helmholtz energy is where the N! shows up via
**Stirling's approximation**:

```
   Q = q^N / N!                 (N independent, indistinguishable molecules)
   A - A(0) = -kT ln Q = -kT [ N ln q - ln N! ]
   Stirling (large N):  ln N! ~ N ln N - N
     => A - A(0) = -kT [ N ln q - N ln N + N ]
                 = -N k T [ ln(q/N) + 1 ]
   U - U(0) = N k T^2 (d ln q / dT)_V           (N! is T-independent)
   S = [U - U(0)]/T - (A - A(0))/T
     = [U - U(0)]/T + N k ln(q/N) + N k
```

The **+1** inside A (and the matching **+Nk** in S) is exactly the Stirling term
−(−N); writing A − A(0) = −NkT·ln(q/N) without it is a common slip that also breaks
the S/A consistency above. For translation this reproduces the **Sackur-Tetrode**
entropy exactly. The
**equipartition theorem** is the high-T limit: each quadratic degree of freedom
contributes ½kT to energy and ½R to C_{V,m} — giving 3/2 R (monatomic), 5/2 R
(diatomic, vibration frozen), rising toward 7/2 R once vibration activates.

**Equilibrium from first principles** — the payoff. For a gas-phase reaction the
equilibrium constant is a ratio of partition functions and a ground-state energy gap:

```
   K° = PROD_j ( q_j°/N_A )^(nu_j) * exp( -Delta E_0 / RT )     (dimensionless)
        q_j° = STANDARD MOLAR partition function of species j
             = q_int,j * (2*pi*m_j*kT/h^2)^(3/2) * V_m°
        V_m° = RT/p°   (standard molar volume; p° = 1 bar)
        (2*pi*m*kT/h^2)^(3/2) has units 1/volume, so q_j°/N_A is DIMENSIONLESS
        and K° is dimensionless, referenced to p° = 1 bar
        nu_j = signed stoichiometry ; Delta E_0 = molar 0 K reaction energy
```

**Standard-state bookkeeping matters when the gas mole number changes.** Each factor
q_j°/N_A is dimensionless because q° uses the *standard molar volume* V_m° = RT/p°;
the p° (1 bar) enters once per net change in gas moles Δν = Σν_j. For a dissociation
like I₂ ⇌ 2 I (Δν = +1) the p° term does **not** cancel and sets the standard state;
for a mole-conserving reaction (Δν = 0, e.g. H₂ + Cl₂ ⇌ 2 HCl) it cancels and K is
standard-state–independent. This computes K for **H₂ + Cl₂ ⇌ 2 HCl** from nothing but
spectroscopic constants (masses, bond lengths → B, vibrational frequencies → Θ_vib,
and the dissociation energies that set ΔE₀). Molecular structure → measurable
equilibrium: the deepest bridge in physical chemistry.

---

## Non-Ideal Solutions and Activity

Real solutions deviate from ideality; the fix is to replace concentration with
**activity** a = γ·x in every equilibrium and in the chemical potential:

```
   mu = mu^o + RT ln a ,   a = gamma * x    (or gamma * c/c^o)
   IDEAL (Raoult):  gamma -> 1 as x -> 1     (solvent, and ideal mixtures)
   DILUTE (Henry):  a_B = K_H x_B            (solute in the dilute limit)
   GASES:           f = phi * P              (fugacity; phi from an equation of state)
```

For **electrolytes**, long-range Coulomb interactions make γ deviate even in dilute
solution. **Debye-Hückel** captures it via the **ionic strength** I = ½ Σ cᵢzᵢ²:

```
   LIMITING LAW (I < ~0.01 M):   log10 gamma_pm = -A |z+ z-| sqrt(I)
                                 A = 0.509  (water, 25 C)
   EXTENDED:   log10 gamma_pm = -A |z+ z-| sqrt(I) / (1 + B a sqrt(I))
   DAVIES (up to I ~ 0.5 M):    log10 gamma_pm = -A |z+ z-| ( sqrt(I)/(1+sqrt(I)) - 0.3 I )
```

**Worked — γ± for 0.1 M NaCl:** I = 0.1, |z₊z₋| = 1. Limiting law gives log γ± =
−0.509√0.1 = −0.161 → γ± = 0.69 (too low). The **extended** law with the
(1+√I) denominator gives log γ± = −0.161/(1+0.316) = −0.122 → **γ± ≈ 0.75**, close to
the experimental 0.78. The lesson: the limiting law is only for very dilute
solutions; at physiological (I ≈ 0.15 M) or geochemical strengths you need the
extended/Davies forms — which is why `04` (ISEs, EDTA constants) and `geochemistry/`
care about this correction.

Beyond electrolytes, **excess Gibbs energy** G^E = RT Σ xᵢ ln γᵢ parameterizes
non-ideality; regular-solution theory and the Margules / NRTL / UNIQUAC models feed
the VLE and liquid-liquid extraction design used in `05` and `chemical-eng/`.

---

## Interfaces and Adsorption Isotherms

At a surface, molecules adsorb; the coverage-vs-pressure relation is the
**isotherm**. The **Langmuir** model (monolayer, equivalent independent sites)
derives from a kinetic balance:

```
   adsorption rate = desorption rate:  k_a P (1 - theta) = k_d theta
   =>  theta = K P / (1 + K P) ,   K = k_a / k_d
       linearized:  P/(V_ads) = 1/(V_m K) + P/V_m   (plot to get V_m and K)
   assumptions: monolayer, all sites equal, no lateral interactions
```

| Isotherm | Form | Physical picture |
|---|---|---|
| **Langmuir** | θ = KP/(1+KP) | monolayer, uniform sites (chemisorption) |
| **BET** | multilayer extension of Langmuir | physisorption; **surface-area measurement** |
| **Freundlich** | θ ∝ P^(1/n) | empirical; heterogeneous surfaces |

**BET** is how specific surface area is measured: N₂ physisorption at 77 K, fit the
BET equation to extract the monolayer capacity, multiply by N₂'s cross-section
(0.162 nm²) to get area (m²/g); mesopore size distributions come from the BJH
analysis of the same isotherm. This is the standard catalyst/adsorbent
characterization number.

---

## Heterogeneous Catalysis: Surface Kinetics

Once reactants adsorb, the rate law depends on *how* they meet on the surface:

```
   LANGMUIR-HINSHELWOOD : both reactants adsorbed    rate = k * theta_A * theta_B
        -> rate can DECREASE at high P (one species crowds the other off)
   ELEY-RIDEAL          : one adsorbed + one from gas  rate = k * theta_A * P_B
   MARS-VAN KREVELEN    : substrate reacts with lattice O; catalyst re-oxidized by O2
        -> common in selective oxidation over metal oxides
```

The organizing principle across all of them is **Sabatier**: the best catalyst binds
the key intermediate *neither too weakly (won't activate) nor too strongly (won't
release)* — an optimum that plots as a **volcano curve** of activity vs binding
energy. Brønsted-Evans-Polanyi (BEP) linear scaling relations link activation
energies to adsorption energies, letting you screen catalysts by a single descriptor
— the theoretical backbone of computational catalyst design in `10`.

---

## Rotational and Vibrational Spectroscopy from QM

The same energy levels that build q are what IR/microwave spectroscopy (`07`)
measures — this closes the loop between theory and spectrum:

```
   RIGID ROTOR:  E_J = B J(J+1) ,  selection rule Delta J = +/-1
        adjacent line spacing = 2B  ->  B = h/(8*pi^2*I*c)  ->  bond length (from I)
   HARMONIC OSC: E_v = (v + 1/2) h*nu ,  Delta v = +/-1  (fundamental)
   ANHARMONIC (Morse): overtones ~ near-integer multiples ; a Birge-Sponer plot
        of level spacings extrapolates to the DISSOCIATION energy D_0
```

So a microwave spectrum's line spacing gives a bond length, and an IR progression's
convergence gives a bond dissociation energy — molecular constants that then feed
straight back into the partition-function equilibrium calculation above.

---

## Reader Tasks

1. **Worked — compute K for H₂ + Cl₂ ⇌ 2 HCl at 500 K from spectroscopic data
   alone.** Because Δν_gas = 0, K is dimensionless and standard-state-independent, and
   the translational **volume** and all **T-dependence** in q_trans and q_rot cancel
   — only a mass ratio, a rotational-constant ratio, the vibrational partition
   functions, and the Boltzmann term survive:

```
   K = [ m_HCl^2 / (m_H2 * m_Cl2) ]^(3/2)                 <- translational (mass)
       * [ (sig_H2 B_H2)(sig_Cl2 B_Cl2) / (sig_HCl B_HCl)^2 ]    <- rotational
       * q_vib(HCl)^2 / [ q_vib(H2) q_vib(Cl2) ]          <- vibrational
       * exp( -Delta E_0 / RT )                            <- ground-state gap

   INPUTS  (m in g/mol; B and nu~ in cm^-1; sigma = symmetry number):
     H2 :  m=2.016    B=60.85   nu~=4401   sigma=2
     Cl2:  m=70.906   B=0.2440  nu~=560    sigma=2
     HCl:  m=36.461   B=10.593  nu~=2991   sigma=1
     Delta E_0 = -(2 D0(HCl) - D0(H2) - D0(Cl2))
               = -(2*427.8 - 432.1 - 239.2) = -184.3 kJ/mol   (0 K, from D0)

   EVALUATE at T = 500 K  (Theta_vib = 1.4388*nu~ ; q_vib = 1/(1 - e^-Theta/T)):
     translational : (36.461^2/(2.016*70.906))^1.5 = 9.300^1.5   = 28.4
     rotational    : (2*60.85 * 2*0.2440)/(1*10.593)^2 = 59.4/112.2 = 0.529
     vibrational   : q_vib(HCl)=1.0002, q_vib(H2)=1.0000, q_vib(Cl2)=1.250
                     -> 1.0002^2 / (1.0000 * 1.250)             = 0.800
     Boltzmann     : exp(184300/(8.314*500)) = exp(44.33)       = 1.79e19

   K(500 K) = 28.4 * 0.529 * 0.800 * 1.79e19  ~=  2.1e20
```

   **Cross-check against tabulated thermodynamics** (independent of the partition
   functions): with ΔH° ≈ −184.6 kJ/mol and ΔS° ≈ +20 J·mol⁻¹·K⁻¹,
   ΔG°(500 K) = ΔH° − TΔS° ≈ −194.6 kJ/mol, giving K = exp(194600/(8.314·500)) ≈
   **2.1×10²⁰** — the spectroscopic route reproduces the calorimetric one, and the
   enormous K correctly says HCl formation is essentially complete. (The vibrational
   partition functions are referenced to v = 0, so ΔE₀ uses the ZPE-inclusive 0 K
   dissociation energies D₀; that convention must match.)
2. **γ± for 0.1 M NaCl?** Extended Debye-Hückel: log γ± = −0.509√0.1/(1+√0.1) ≈ −0.122
   → **γ± ≈ 0.75** (limiting law's 0.69 is too low at this I).
3. **Specific surface area from N₂ adsorption?** Fit the **BET** equation to the 77 K
   isotherm for the monolayer capacity, multiply by 0.162 nm²/molecule and N_A →
   m²/g.
4. **Which C_{V,m} for a diatomic at 298 K?** 5/2 R (translation + rotation active,
   vibration frozen because Θ_vib ≫ 298 K); it rises toward 7/2 R only when vibration
   activates.
5. **Why can a Langmuir-Hinshelwood rate fall at high pressure?** Both reactants
   compete for the same sites; excess of one lowers the other's coverage, so
   k·θ_A·θ_B drops — a signature that distinguishes it from Eley-Rideal.

## Decision Cheat Sheet

| Goal | Tool | Key relation |
|---|---|---|
| Predict K° from structure | partition functions | K° = Π(q°/N_A)^ν·exp(−ΔE₀/RT), dimensionless (q° at V_m°=RT/p°) |
| Heat capacity of a gas | equipartition + Θ | ½R per active quadratic DOF |
| Activity of a nonelectrolyte | Raoult/Henry | a = γx; γ→1 pure/dilute limits |
| Activity of ions (dilute) | Debye-Hückel limiting | log γ± = −0.509·\|z₊z₋\|·√I |
| Ions at moderate I | extended DH / Davies | (1+√I) denominator; Davies to I≈0.5 |
| Surface area | BET (N₂, 77 K) | monolayer × 0.162 nm² |
| Monolayer chemisorption | Langmuir | θ = KP/(1+KP) |
| Rate law on a surface | L-H vs E-R vs MvK | which species is adsorbed |
| Best catalyst binding strength | Sabatier / volcano | optimum intermediate binding |
| Bond length / dissociation E | rotational / vibrational | 2B spacing; Birge-Sponer |

## Common Confusion Points

- **Molecular partition function q vs canonical Q.** For N independent,
  indistinguishable molecules Q = qᴺ/N!; the N! (via q/N in S and A) is what makes
  entropy extensive and fixes the Gibbs paradox. Don't drop it.
- **This is not condensed-matter stat mech.** Partition functions here predict
  chemical equilibria and heat capacities of gases/solutions; Ising models, critical
  exponents, and RG are `statistical-mechanics/`.
- **Debye-Hückel *limiting* law is genuinely limited.** It only holds below ~0.01 M;
  using it at 0.1 M (let alone seawater/physiological) underestimates γ± noticeably.
- **Activity is not a fudge factor.** It is the thermodynamically correct variable; K
  is constant in activities, not in concentrations. Equilibrium "shifting" with ionic
  strength is just γ changing.
- **Langmuir assumptions are strong.** Real surfaces are heterogeneous and interacting;
  a good Langmuir fit does not prove a uniform monolayer — check against BET/Freundlich.
- **Sabatier optimum, not "stronger binding is better."** Too-strong adsorption
  poisons the catalyst by blocking product release; the volcano peak is the whole
  point.
