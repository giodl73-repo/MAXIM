# 02 — Reactor Physics

## Criticality, Neutron Transport, Neutron Economy, Kinetics

```
NEUTRON LIFE CYCLE IN A THERMAL REACTOR

 Fast fission                          Resonance capture
 (U-238 fissions)                      (U-238 captures ~6 eV–100 keV)
       ↓ε                                    ↓(1-p)
ν neutrons born ──fast──► ε·ν ──slow down──► p·ε·ν ──thermal──► f·p·ε·ν
 at ~2 MeV                              region              (fraction absorbed in fuel)
                                                                    ↓
                                                          η = fission neutrons
                                                            per absorption in fuel
                                                                    ↓
                                              k∞ = η · ε · p · f  (infinite medium)
                                                                    ↓
                                         Add leakage: k_eff = k∞ · P_FNL · P_TNL
```

Nuclear reactor design is the engineering of a self-sustaining neutron chain reaction.
The challenge: balance neutron production against all loss mechanisms (absorption + leakage)
to hold k_eff exactly at 1.000, then **control** it with small reactivity changes.

---

## The Six-Factor Formula

### Four-Factor Formula (Infinite Reactor, No Leakage)

```
k∞ = η · ε · p · f

η (eta) = thermal fission factor = ν · σ_f / σ_a^(fuel)
  = neutrons produced per neutron absorbed in fuel
  ≈ 2.07 (U-235 in thermal spectrum)  2.11 (U-233)  2.09 (Pu-239)
  Note: η = ν · [σ_f/(σ_f + σ_c)] where σ_c = capture cross section in fuel

ε (epsilon) = fast fission factor
  = accounts for fissions in U-238 by fast neutrons
  ≈ 1.03–1.08 depending on fuel enrichment and lattice geometry
  Increases with fuel-to-moderator ratio

p (rho) = resonance escape probability
  = fraction of neutrons that slow down past resonance region without capture
  Dominates in U-238 (many large resonances 6–200 eV)
  p ≈ exp(−N_U A_r / ξ Σ_s)  where A_r = resonance integral, ξ = lethargy gain
  p ≈ 0.75–0.90 for typical LWRs
  Increases with moderator-to-fuel ratio; Doppler broadening decreases p (safety feedback)

f (f) = thermal utilization factor
  = fraction of thermal neutrons absorbed in fuel (vs fuel + moderator + structure)
  f = Σ_a^(fuel) / (Σ_a^(fuel) + Σ_a^(mod) + Σ_a^(clad) + ...)
  f ≈ 0.71–0.94 depending on enrichment, moderator, poison loading
```

### Six-Factor Formula (Finite Reactor, With Leakage)

```
k_eff = k∞ · P_FNL · P_TNL

P_FNL = fast non-leakage probability = 1/(1 + L_f² B²)
P_TNL = thermal non-leakage probability = 1/(1 + L_th² B²)

L_f² = fast diffusion area (≈ Fermi age τ for graphite/D₂O; larger for heavy moderators)
L_th² = thermal diffusion length squared = D/Σ_a  [cm²]
B² = geometric buckling (set by reactor shape and size)

Combined: k_eff = k∞ / [(1 + L_th² B²)(1 + τ B²)]
          ≈ k∞ / (1 + M² B²)  where M² = L² + τ (migration area)
```

**Material vs Geometric Buckling:**
```
Material buckling:  B²_m = (k∞ − 1) / M²
  = "how much excess multiplication" the material provides

Geometric buckling: B²_g = function of reactor geometry and critical size
  Bare sphere:   B²_g = (π/R)²
  Bare slab:     B²_g = (π/a)²
  Bare cylinder: B²_g = (2.405/R)² + (π/H)²

CRITICAL CONDITION: B²_m = B²_g
  → determines critical mass/size for given material composition
  → subcritical if B²_g > B²_m (too small — too much leakage)
  → supercritical if B²_g < B²_m (too large)
```

---

## Moderation Physics

### Why Moderate?

Fast neutrons at ~2 MeV have σ_f(U-235) ≈ 1 barn. Thermal neutrons at 0.025 eV have σ_f ≈ 584 barn.
Slowing down multiplies effective cross section by ~584×. This is why thermal reactors can sustain
criticality with low enrichment (3–5%), while fast reactors need >15–20%.

### Moderator Comparison

```
Moderator   ξ*    σ_s [b]  σ_a [b]   Moderating     Moderating
                                      Power ξΣ_s      Ratio ξΣ_s/Σ_a
──────────────────────────────────────────────────────────────────────────
H₂O         0.920  49.2     0.66      1.425 cm⁻¹     72
D₂O         0.570  10.6     0.001     0.176 cm⁻¹     5,670
Graphite     0.158   4.7    0.0034    0.064 cm⁻¹     216
Beryllium    0.209   6.1    0.0092    0.158 cm⁻¹     159

ξ = average lethargy gain per collision = 1 + (A-1)²/(2A) ln[(A-1)/(A+1)]
  H¹: ξ ≈ 1.0 (most efficient per collision)
  C¹²: ξ = 0.158 (requires ~110 collisions to thermalize)

Slowing-down power = ξ Σ_s [cm⁻¹]
Moderating ratio = ξ Σ_s / Σ_a  (high = good moderator, low parasitic absorption)
```

D₂O wins on moderating ratio → allows natural uranium fuel in CANDU.
H₂O wins on moderating power (compact core) but requires enrichment.
Graphite: good ratio, but slow per collision, needs large reactor.

---

## Neutron Diffusion Theory

### Diffusion Equation

```
One-speed (one-group) diffusion equation (steady state):

  D∇²φ − Σ_a φ + S = 0

where:
  φ = neutron flux [n/(cm²·s)]
  D = diffusion coefficient = 1/(3 Σ_tr) = λ_tr/3  [cm]
  Σ_a = macroscopic absorption cross section [cm⁻¹]
  S = neutron source density [n/(cm³·s)]

Diffusion length: L² = D/Σ_a
  → neutrons diffuse ~ L cm before being absorbed
  H₂O: L ≈ 2.85 cm    D₂O: L ≈ 170 cm    Graphite: L ≈ 50 cm

For a fissioning medium with k∞:
  D∇²φ + (k∞/M² − 1/M²)φ = 0
  D∇²φ + B²_m φ = 0     (Helmholtz equation)
  → solutions: sinusoids and cosines (bounded at extrapolated boundary φ=0)
```

### One-Group Critical Dimensions

```
Critical bare slab (width a):  φ = A cos(πx/a),  B² = (π/a)²
  → a_crit = π / B_m

Critical bare sphere (radius R):  φ = A sin(πr/R)/(πr/R)
  → R_crit = π / B_m  (≈ 97 cm for light-water-moderated 3.5% enriched uranium)

Reflector savings: δ (reflector reduces critical size)
  For thick reflector: δ ≈ L_reflector (diffusion length in reflector material)
  H₂O reflector: δ ≈ 2–3 cm for fast; ~5 cm for thermal
```

### Two-Group Theory

Separates neutrons into "fast" and "thermal" groups with coupling:
```
Group 1 (fast): D_1 ∇²φ_1 − (Σ_r1) φ_1 + χ_1 k∞ Σ_a2 φ_2 = 0
Group 2 (thermal): D_2 ∇²φ_2 − Σ_a2 φ_2 + Σ_r1 φ_1 = 0

Σ_r1 = removal cross section (fast → thermal by moderation)
χ_1 = fast fission spectrum fraction

→ Gives more accurate flux shape (thermal flux peaks near moderator, fast near fuel)
→ Foundation for PWR design codes (CASMO, SIMULATE)
```

---

## Reactivity and Control

### Reactivity Units

```
ρ = (k_eff − 1) / k_eff    [dimensionless, but often in pcm or dollars]

pcm = per cent mille = 10⁻⁵  → ρ = 1 pcm means k_eff = 1.00001
Dollar ($): ρ/β_eff  → $1 = prompt critical threshold (very dangerous)
           (β_eff ≈ 0.0065 for U-235 → $1 ≈ 650 pcm)

Typical operating range: |ρ| < 200 pcm  (deep within delayed-critical regime)
Shutdown margin: ρ ≤ −1000 pcm with most reactive rod stuck out
```

### Control Rod Worth

```
Differential worth: dρ/dz  [pcm/cm] as function of insertion depth z
  Peaks at mid-core (highest flux there → maximum perturbation)
  Sinusoidal flux shape → dρ/dz ∝ sin²(πz/H)

Integral worth: ρ(z) = ∫₀^z (dρ/dz') dz'
  S-curve shape: slow at top and bottom, rapid in middle

Boron worth: ~8–11 pcm per ppm in PWR coolant
  Typical shutdown boron concentration: ~2000 ppm
  Boron dilution accident: inadvertent dilution → positive reactivity insertion

Control materials: B-4C, Ag-In-Cd (PWR), B₄C (BWR), hafnium
  Ag-In-Cd: better worth distribution, but more expensive
```

---

## Point Kinetics — Reactor Dynamics

### Point Kinetics Equations

```
dP/dt = [(ρ − β_eff)/Λ] P + Σᵢ λᵢ Cᵢ  + S_ext

dCᵢ/dt = (βᵢ/Λ) P − λᵢ Cᵢ     for i = 1...6 precursor groups

P = power (proportional to flux)
ρ = reactivity
β_eff = effective delayed neutron fraction ≈ 0.0065 (U-235 thermal)
Λ = prompt neutron generation time ≈ 10⁻⁴ s (LWR with delayed contribution)
  (prompt alone ≈ 10⁻⁶–10⁻⁵ s, but delayed extend effective Λ to ~0.1 s)
λᵢ = decay constant of i-th precursor group
Cᵢ = concentration of i-th precursor group
```

### Inhour Equation

```
Relates reactivity to steady-state reactor period T:

ρ = Λ/T + Σᵢ βᵢ/(1 + λᵢ T)

For |ρ| ≪ β_eff and T ≫ 1/λᵢ: one precursor group approximation
  T ≈ β_eff / (ρ λ_eff)   (stable period, positive ρ insertion)

Example: ρ = 10 pcm = 0.0001 insertion into U-235 reactor
  T ≈ 0.0065 / (0.0001 × 0.08) ≈ 800 seconds → very slow rise (controlled!)
```

### Prompt Criticality — The Danger Line

```
At ρ = β_eff ($1): prompt neutrons alone sustain criticality
  → reactor period collapses from hundreds of seconds to milliseconds
  → cannot control with mechanical rods

Normal operation: ρ < β_eff always (operating below prompt critical)
  Delayed neutrons extend effective generation time:
  Λ_eff ≈ β_eff / (Σᵢ βᵢ λᵢ) ≈ 0.1 s  (vs Λ_prompt ≈ 10⁻⁵ s)
  This 10,000× time extension makes rod control possible
```

---

## Reactivity Coefficients (Feedback)

### Doppler Broadening (Fuel Temperature Coefficient)

```
As T_fuel increases:
  → U-238 resonances (6–100 eV) thermally broaden
  → more neutron captures during slowing down → p decreases → ρ decreases

α_Doppler = dρ/dT_fuel ≈ −1.5 to −3 pcm/°C (for UO₂ fuel)

This is the FASTEST feedback: responds in < 1 second
  → the primary safety mechanism in thermal reactors
  → even before rods can move, Doppler dampens power excursion

Physical basis: Doppler width Γ_D ∝ √T
  Increased width → reduced peak cross section (area conserved) → more capture below resonance peak
```

### Moderator Temperature Coefficient (MTC)

```
As T_mod increases:
  → water density decreases → less moderation → neutrons shift to higher energy
  → less thermal absorption → σ_f decreases (at higher energy)
  → also: less parasitic absorption in coolant-poison → depends on boron concentration

α_MTC = dρ/dT_mod ≈ −20 to −80 pcm/°C (PWR, no soluble boron)
  IMPORTANT: α_MTC can be slightly positive at high boron concentration
  → NRC requires α_MTC ≤ 0 at Hot Full Power (no boron)
  → ensures self-stabilizing behavior during power changes

MTC slower than Doppler: thermal response time ~10 s
```

### Void Coefficient

```
As coolant voids (steam bubbles form):
  → less moderation → neutron spectrum hardens
  → in LWRs (H₂O): hardened spectrum → more captures in U-238 → ρ decreases
    α_void < 0 (NEGATIVE — stabilizing) for LWRs

  → in RBMK (graphite moderator + water coolant):
    Voiding removes water but graphite still moderates
    Less water absorption (water is poison!) → ρ INCREASES
    α_void > 0 (POSITIVE — destabilizing) — contributed to Chernobyl

  → in CANDU: α_void ≈ +5 to +10 mk (positive but small, compensated by design)
```

---

## Xenon Poisoning

### Xenon-135 Production and Decay

```
Fission products → 135Te → 135I (T½=6.7hr) → 135Xe (T½=9.2hr) → 135Cs → stable
                         direct yield                σ_a = 2.6×10⁶ b  (HUGE!)

At steady state:
  135Xe equilibrium:  X_eq = (γ_I + γ_Xe) Σ_f φ / (λ_Xe + σ_Xe φ)

  γ_I ≈ 0.061  (I-135 fission yield)
  γ_Xe ≈ 0.003 (direct Xe fission yield)
  → ~95% of 135Xe comes from 135I decay (not directly from fission)

  At high flux (φ > 10¹⁴ n/cm²·s): Xe mainly burned out (σ_Xe φ dominates)
  Reactivity penalty at equilibrium: ~250–350 pcm in PWR
```

### Xenon Transient After Shutdown

```
After power reduction or shutdown:
  1. 135I continues decaying → 135Xe production continues
  2. 135Xe burnout by flux ceases (no flux)
  3. Xe concentration INCREASES — peaks 6–10 hours after shutdown

  → "Xenon peak" can add 2000–3000 pcm negative reactivity
  → Must have enough positive reactivity (control rod withdrawal, boron dilution)
     to override xenon if attempting restart within ~40 hrs
  → If not enough excess reactivity: reactor "xenon precluded" from restart

  Xenon override capability: reactor has enough excess reactivity to override Xe peak
  Large PWRs: typically ±3000 pcm xenon override margin built in
```

### Xenon Oscillations

```
In large cores (axis length >> migration length):
  Flux tilts spatially → more Xe in low-flux regions → less Xe in high-flux regions
  → power shift to low-Xe regions → more Xe produced there
  → oscillations grow (axial Xe oscillations, period ~30 hr)

  Spatial oscillations require distributed control (axial offset monitoring)
  Controlled by: excore detectors, AO (axial offset) limits, part-length rods
```

---

## Samarium Poisoning

```
149Nd (fission product) → 149Pm (T½=54hr) → 149Sm (stable, σ_a=41,000 b)

At equilibrium: Sm poisons ~100 pcm (less than Xe, but permanent after burnup)

Post-shutdown transient: DIFFERENT from Xe!
  → 149Pm no longer burned out → decays to 149Sm
  → Sm concentration RISES after shutdown
  → Reactivity penalty increases then stabilizes (does not peak and disappear like Xe)
  → Must account for Sm peak in startup reactivity balance

  Sm buildup post-shutdown peak: ~200–400 pcm additional penalty
```

---

## Fuel Burnup and Transmutation

### Actinide Buildup

```
²³⁸U + n → ²³⁹U ---(β⁻, 23 min)--► ²³⁹Np ---(β⁻, 2.4 d)--► ²³⁹Pu

²³⁹Pu fission: σ_f = 748 b (thermal), η ≈ 2.09
  → At burnup >10 GWd/tU, Pu contributes ~1/3 of total fissions

Higher plutonium isotopes:
  ²³⁹Pu + n → ²⁴⁰Pu (non-fissile in thermal) + n → ²⁴¹Pu (fissile) + n → ²⁴²Pu (non-fissile)
  ²⁴⁰Pu: large resonance at 1 eV → absorber, "reactor grade Pu" less weapons-usable

Burnup units: GWd/tU (gigawatt-days per tonne of uranium)
  Typical PWR discharge burnup: 40–55 GWd/tU (extended burnup: 60–70)
  Requires reload enrichment ~4–5% U-235 to achieve target burnup
```

### Bateman Equations

```
dN_i/dt = Σⱼ λⱼ N_j + Σⱼ σ_j φ N_j − λᵢ Nᵢ − σᵢ φ Nᵢ
  (production from j by decay + neutron capture) − (loss from i by decay + capture)

Solved by ORIGEN-S, SCALE, CASMO, SIMULATE codes
→ tracks ~1,000+ isotopes across reactor cycle
```

### Fuel Management

```
Reload: 1/3 to 1/4 of assemblies replaced each cycle (12–24 months)
Shuffling pattern: fresh fuel (high enrichment) placed near edge
  "Out-in" (old fuel center): flux peaks at center
  "In-out" (fresh fuel center): better power peaking but higher leakage
  Typical: low-leakage loading (fresh near edge for flux flattening)

Burnable absorbers (BA):
  Purpose: reduce excess reactivity early in cycle (flat boron-free reactivity)
  Materials: gadolinium (Gd₂O₃ in fuel), erbia (Er₂O₃), boron in glass rods (IFBA)
  Gd: very high σ_a → "self-shielded" → burns from outside in (slow rate)
  At end of life: BA nearly completely burned out → minimal residual penalty

Power peaking factor F_Q:
  = max local power / average power
  Design limit typically F_Q ≤ 2.5
  Controlled by enrichment zoning, rod patterns, burnup distribution
```

---

## Multigroup Transport (Advanced)

```
Boltzmann Transport Equation (exact):

Ω̂·∇ψ + (Σ_t) ψ = ∫∫ Σ_s(r,E'→E,Ω'→Ω) ψ dE' dΩ' + S_f(r,E,Ω)

ψ = angular flux [n/(cm²·s·sr·eV)]
Σ_t = total cross section
Σ_s = scattering kernel (energy + angle change)
S_f = fission source

Numerical methods:
  Discrete ordinates (Sₙ): discretize directions → ray effects + streaming
  Diffusion theory: P₁ approximation of transport; accurate away from boundaries
  Monte Carlo (MCNP, OpenMC): track individual neutrons statistically
    → no geometry approximation; most accurate; slow for routine design
    → gold standard for validation of deterministic codes
```

---

## Common Confusion Points

**k_eff = 1 is NOT a dangerous state:** Operating reactors run at k_eff ≈ 1.0000 continuously.
"Critical" just means self-sustaining — the normal operating condition, not an emergency.
Accidents involve prompt criticality (ρ → β_eff) or loss of cooling, not just k_eff = 1.

**Reactivity ρ vs multiplication k_eff:** ρ = (k−1)/k, so ρ = 0 at criticality, ρ > 0 supercritical,
ρ < 0 subcritical. Engineers work in ρ (and pcm) not k for small deviations. $1 of reactivity
= β_eff ≈ 650 pcm for U-235. Never approach $1 in normal operations.

**Doppler is not a Doppler shift of neutron energy:** It's thermal broadening of resonance peaks in
the cross section vs energy curve. As fuel heats, U-238 resonances broaden → more captures →
negative reactivity. This is the fast, inherent safety mechanism in thermal reactors.

**Xenon precluded restart:** If you cannot start back up 8–40 hours after shutdown, it's because
Xe-135 (from I-135 decay) has overwhelmed your positive reactivity capability. You wait ~40 hours
for Xe to decay away. This is why unplanned shutdowns can cost days of lost generation.

**Burnup and enrichment relationship:** Higher discharge burnup requires higher reload enrichment.
At ~5% enrichment (NRC limit for "low enriched"), typical discharge burnup ≈ 50–60 GWd/tU.
Going to 70+ GWd/tU ("high burnup fuel") requires regulatory approval and advanced cladding materials.

---

## Decision Cheat Sheet

| Reactor physics question | Tool/Concept | Key relation |
|--------------------------|-------------|-------------|
| Is this composition critical? | Six-factor formula + buckling | B²_m = B²_g at criticality |
| What size is critical? | Geometric buckling for shape | R_crit = π/B_m (sphere) |
| How fast will power change? | Point kinetics + inhour equation | T ≈ β_eff/(ρ λ_eff) for small ρ |
| Will this be inherently safe? | Reactivity coefficients | Need α_Doppler < 0, α_MTC < 0 at HFP |
| How much boron to shut down? | Boron worth × required ρ | ~10 pcm/ppm → ~1000 ppm for 10,000 pcm |
| Xenon restart possible? | Xe reactivity vs available override | Peak Xe ~2500–3500 pcm at t≈8h |
| Burnup calculation | Bateman equations + ORIGEN | Track actinides + fission products |
| Accurate critical calculation | Monte Carlo transport | MCNP/OpenMC with continuous energy XS |
| Moderator selection | Moderating ratio ξΣ_s/Σ_a | D₂O: 5,670 vs H₂O: 72 |
