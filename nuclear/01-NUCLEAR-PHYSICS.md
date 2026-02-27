# 01 — Nuclear Physics for Engineers

## Binding Energy, Cross Sections, Decay, Fission

<!-- @editor[audience/P2]: File opens by explaining "Nucleus: Z protons + N neutrons → mass number A = Z + N" — this learner has MIT physics and knows nuclear structure. The Building Blocks block can open directly at the scale/energy section without the nuclide primer. The nuclide notation is fine for reference; the explanatory framing isn't needed. -->
```
NUCLEAR PHYSICS BUILDING BLOCKS

Nucleus: Z protons + N neutrons → mass number A = Z + N
         Nuclide notation: ᴬ_Z X  (e.g., ²³⁵₉₂U)

Key scales:
  Nuclear size:   r ≈ 1.2 A^(1/3) fm  (1 fm = 10⁻¹⁵ m)
  Nuclear density: ~2.3×10¹⁷ kg/m³  (same for all nuclei)
  Mass unit:      1 u = 1.66054×10⁻²⁷ kg = 931.5 MeV/c²
  Nuclear energy: MeV scale (vs eV for atomic/chemical)
```

---

## Binding Energy

**Mass defect and binding energy:**
```
B = (Z mₚ + N mₙ − M_nucleus) c²   [MeV]

where:
  mₚ = 938.272 MeV/c²  (proton rest mass)
  mₙ = 939.565 MeV/c²  (neutron rest mass)
  M_nucleus = actual nuclear mass
  c² = 931.5 MeV/u (conversion)

Binding energy per nucleon B/A:
  Peaks at ⁵⁶Fe (~8.8 MeV/nucleon)
  → Fusing light nuclei (left of Fe): releases energy (fusion)
  → Fissioning heavy nuclei (right of Fe): releases energy (fission)
```

**Semi-empirical mass formula (Bethe-Weizsäcker):**
```
B = a_V A − a_S A^(2/3) − a_C Z(Z−1)/A^(1/3) − a_A(A−2Z)²/A + δ

a_V ≈ 15.56 MeV  (volume term: bulk nuclear attraction)
a_S ≈ 17.23 MeV  (surface term: surface nucleons less bound)
a_C ≈ 0.697 MeV  (Coulomb repulsion between protons)
a_A ≈ 23.3 MeV   (asymmetry: N ≈ Z preferred by Pauli exclusion)
δ = pairing term (even-even nuclei most stable)
```

---

## Radioactive Decay

**Decay law:**
```
dN/dt = −λN    →    N(t) = N₀ exp(−λt)

λ = decay constant [s⁻¹]
T₁/₂ = half-life = ln2/λ = 0.693/λ
Activity: A = λN [Becquerels: 1 Bq = 1 decay/s]
  1 Curie = 3.7×10¹⁰ Bq ≈ activity of 1 g of ²²⁶Ra
```

**Half-life reference table:**

| Nuclide | T₁/₂ | Decay | Significance |
|---------|------|-------|-------------|
| ²³⁵U | 7.0×10⁸ yr | α | Primary fissile material |
| ²³⁸U | 4.5×10⁹ yr | α | Fertile → ²³⁹Pu |
| ²³⁹Pu | 2.4×10⁴ yr | α | Fissile, produced in reactor |
| ¹³⁷Cs | 30 yr | β⁻ | Major fission product, dose concern |
| ⁹⁰Sr | 28 yr | β⁻ | Bone-seeking, dose concern |
| ¹³¹I | 8 days | β⁻, γ | Short-lived, thyroid dose |
| ¹³⁵Xe | 9.2 hr | β⁻ | Reactor poison (large σ_a) |
| ¹⁴⁹Sm | stable | — | Reactor poison |
| ⁶⁰Co | 5.27 yr | β⁻, γ | Activation product in steel |
| ³H (tritium) | 12.3 yr | β⁻ | D-T fusion fuel, CANDU/fusion concern |

### Decay Modes

**Alpha decay (A > 200):**
```
ᴬ_Z X → ᴬ⁻⁴_{Z-2} Y + ⁴₂He + Q
Q = B(daughter) + B(α) − B(parent)
Range in air: few cm; stopped by paper
High LET → high biological effectiveness
```

**Beta decay:**
```
β⁻: n → p + e⁻ + ν̄_e  (excess neutrons: fission products)
β⁺: p → n + e⁺ + ν_e  (proton-rich nuclides)
EC: p + e⁻ → n + ν_e   (electron capture, competes with β⁺)

Continuous energy spectrum (shared with antineutrino) → average E_β ≈ E_max/3
Penetration: mm to cm in tissue; stopped by plastic/aluminum
```

**Gamma decay:**
```
No change in A or Z; nucleus relaxes from excited state
EM radiation: penetrating (requires cm of lead/meters of concrete)
Detection: NaI(Tl), HPGe detectors for γ spectroscopy

Compton scattering: dominant interaction 0.1–10 MeV
Photoelectric effect: dominates at low E (< 0.1 MeV)
Pair production: threshold 1.022 MeV, dominates > 10 MeV
```

---

## Nuclear Cross Sections

**Microscopic cross section σ:** effective target area for a given reaction [barn = 10⁻²⁴ cm²]

```
Reaction rate R = n v σ N_target = φ Σ

where:
  φ = neutron flux = n v  [neutrons/(cm²·s)]
  n = neutron density [neutrons/cm³]
  v = neutron speed [cm/s]
  N = atom density [atoms/cm³]
  Σ = macroscopic cross section = N σ [cm⁻¹]
  Mean free path: λ = 1/Σ
```

**Cross section behavior vs energy:**
```
Thermal region (E < 1 eV): σ ∝ 1/v  (inversely proportional to velocity)
Resonance region (~1 eV – 1 MeV): sharp peaks (Breit-Wigner resonances)
Fast region (> 1 MeV): smooth, decreasing
```

**Key cross sections for reactor physics (thermal neutrons, ~0.025 eV):**

| Reaction | σ [barns] | Notes |
|---------|-----------|-------|
| ²³⁵U fission | 584 | Primary fissile |
| ²³⁵U absorption | 681 | Includes fission + capture |
| ²³⁸U fission | 0.00011 | Only fast neutrons |
| ²³⁸U absorption | 2.7 | → ²³⁹Pu (breeding) |
| ²³⁹Pu fission | 748 | Better than U-235 at thermal |
| H₂O scattering | 49 | Good moderator |
| H₂O absorption | 0.66 | Some neutron loss |
| ¹³⁵Xe absorption | 2.6×10⁶ | Xenon poison |
| ¹⁰B absorption | 3838 | Control rod material |
| Hf absorption | ~2000 | Control rod material |
| Cd absorption | 2450 | Control rod material |

---

## Fission Physics

**Mechanism (Bohr & Wheeler liquid drop model):**
```
n + ²³⁵U → ²³⁶U* (compound nucleus, excited) → fission fragments + 2–3 neutrons + γ + β
```

**Energy release per fission (~200 MeV total):**
```
Fission fragment kinetic energy:  ~168 MeV  (deposited locally in fuel)
Prompt neutron kinetic energy:     ~5 MeV   (deposited in moderator)
Prompt gamma energy:               ~7 MeV   (deposited in structures)
Beta decay of fission products:    ~8 MeV   (decay heat, released over time)
Antineutrino energy:               ~12 MeV  (escapes, not recoverable)
TOTAL recoverable:                ~188 MeV
```

<!-- @editor[bridge/P2]: Fission product decay chains (¹³⁵Te → ¹³⁵I → ¹³⁵Xe → ¹³⁵Cs) are topological dependency trees — same data structure as package dependency graphs, build DAGs, and service dependency maps. The "xenon precluded restart" scenario (a downstream decay product blocks operation hours after its precursor was produced) maps directly to cascading dependency failures in service graphs: removing a service doesn't remove the downstream effects that already propagated. Worth naming: "decay chains are dependency trees, and the xenon poisoning problem is a deferred side-effect of a dependency you thought you removed." -->
**Fission products:** Bimodal mass distribution — light peak ~95 u (Kr, Rb, Sr, Y, Zr) and heavy peak ~140 u (Cs, Ba, La, Ce, Nd). Very neutron-rich → extensive β decay chains.

**Prompt vs delayed neutrons:**
```
Prompt neutrons: emitted within 10⁻¹⁴ s after fission
  ν̄_prompt ≈ 2.47 per fission (U-235 thermal)
  Average energy ~2 MeV (fast spectrum)

Delayed neutrons: from β decay of fission product precursors
  β_eff ≈ 0.0065 for U-235 thermal  (0.65% of all neutrons)
  Range: 0.01–55 s delay
  Six precursor groups (I: 55s, II: 22s, ... VI: 0.23s)

Importance: delayed neutrons make control possible!
  Without delayed: reactor too fast to control with rods
  With delayed: effective generation time ~0.1 s → controllable
```

---

## Radiation Interaction with Matter

**Linear attenuation coefficient μ [cm⁻¹] for photons:**
```
I(x) = I₀ exp(−μx)    (exponential attenuation)
Half-value layer HVL = ln2/μ

Typical HVL for 1 MeV gamma:
  Air: ~12,000 cm
  Water: ~14 cm
  Lead: ~1 cm
```

**Neutron radiation:** Doesn't directly ionize. Interacts via nuclear reactions (scattering → thermalize, then absorption). Activates materials via (n,γ) reactions.

**Dose units:**
```
Absorbed dose: Gray (Gy) = J/kg
Effective dose: Sievert (Sv) = Gy × radiation weighting factor × tissue weighting factor

Radiation weighting factors:
  Photons, beta: 1
  Neutrons (1 MeV): 20
  Alpha: 20

Dose limits (ICRP):
  Occupational: 20 mSv/yr (average over 5 years)
  Public: 1 mSv/yr above background
  Emergency workers (life-saving): up to 250 mSv/yr
```

---

## Fusion (for Context)

```
D + T → ⁴He (3.52 MeV) + n (14.1 MeV)    Q = 17.6 MeV

Lawson criterion for energy-break-even:
  n τ_E > 10²⁰ s/m³   (particle density × energy confinement time)

ITER goal: Q = 10 (fusion power / heating power = 10)
  n ≈ 10²⁰ m⁻³, τ_E ≈ 3–4 s, T ≈ 150 million K (10 × T_sun core)

Ignition temperature: ~100 million K (Maxwellian average for D-T)
Fuel resources: D from seawater (abundant), T must be bred from Li-6 in blanket
```

---

## Common Confusion Points

**Activity vs dose:** Activity [Bq] = disintegration rate. Dose [Sv] = biological effect. A high-activity source can be low-dose (if it emits weak beta with short range). A low-activity alpha emitter inside the body can be high-dose (high LET, deposited locally).

**Fission cross sections at thermal vs fast:** U-235 thermal σ_f = 584 b, but σ_f,fast ≈ 1 b. Thermal reactors achieve much higher fission rates per neutron. That's why moderation (slowing neutrons to thermal energies) is so important.

**Delayed neutrons and β_eff:** β_eff ≈ 0.65% seems tiny, but the entire concept of reactor control depends on it. The delayed neutron fraction extends the effective generation time from microseconds to hundreds of milliseconds — the difference between controllable and uncontrollable.

**Half-life vs activity:** High activity ≠ long-lived hazard. ¹³¹I has T½ = 8 days → very high activity, but gone in weeks. ²³⁹Pu has T½ = 24,000 yr → low activity but very long-lived. Both are hazardous, but in different ways.

---

## Decision Cheat Sheet

| Question | Formula | Notes |
|----------|---------|-------|
| Decay rate after time t | N = N₀ e^(−λt) | λ = ln2/T½ |
| Activity from sample | A = λN | N = mass × N_A/M |
| Reaction rate in reactor | R = φ Σ | per unit volume |
| Energy from fission | ~200 MeV per event | Only ~188 recoverable |
| Fission vs fusion energy | Compare Q-values | Fusion ~4× more per nucleon |
| Cross section units | 1 barn = 10⁻²⁴ cm² | Macro: Σ = nσ |
| Dose from gamma | HVL = ln2/μ | 1 cm Pb per MeV gamma |
