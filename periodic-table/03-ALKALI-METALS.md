# Alkali Metals (Group 1) — Li, Na, K, Rb, Cs, Fr

## The Big Picture

Group 1 is the most reactive column of metals. Each member has exactly **one valence electron**
in an ns¹ configuration — one electron it desperately wants to lose.

```
GROUP 1 — ELECTRON CONFIGURATIONS AND KEY DATA

  Element  Z   Config      IE₁(kJ/mol)  Radius(pm)  bp(°C)  E°(V vs SHE)
  ─────────────────────────────────────────────────────────────────────────
  Lithium  3   [He]2s¹     520          152          1342    −3.04
  Sodium   11  [Ne]3s¹     496          186          883     −2.71
  Potassium 19 [Ar]4s¹     419          227          759     −2.93
  Rubidium 37  [Kr]5s¹     403          248          688     −2.98
  Cesium   55  [Xe]6s¹     376          265          671     −3.03
  Francium 87  [Rn]7s¹     ~400(est.)   ~270         ~680    ~−2.9

TREND EXPLANATION:
  Down the group:
    • IE decreases: valence electron farther from nucleus, more shielded by inner shells
    • Atomic radius increases: new shells added
    • Reactivity increases: lower IE → easier to lose the electron
    • Melting/boiling points DECREASE: weaker metallic bonding (electrons more diffuse)
    • Note: K has lower IE than Na but slightly MORE negative E° — relativistic/solvation effects

ALL alkali metals:
  • +1 oxidation state exclusively (for Li, Na, K) in normal chemistry
  • Soft enough to cut with a knife
  • Low density (Li, Na, K float on water — density < 1 g/cm³)
  • Store under mineral oil or inert gas (air/water reactive)
```

---

## Water Reactions — Reactivity Arc

All alkali metals react with water; the violence increases down the group:

```
2 M + 2 H₂O → 2 MOH + H₂↑

  Lithium:   slow, glides on surface, gentle fizzing
  Sodium:    vigorous, melts to silver ball, darts around, H₂ ignites if confined
  Potassium: purple/lilac flame (K emission), H₂ ignites immediately
  Rubidium:  explosive on contact
  Cesium:    violently explosive, shatters container

Mechanism:
  1. Metal surface reacts: M → M⁺ + e⁻ (into water)
  2. H₂O + e⁻ → OH⁻ + ½H₂ (at metal surface)
  3. Heat generated → H₂ ignites (Cs is fast enough to ignite the H₂ in a shockwave)

WHY SODIUM MELTS: heat of reaction is sufficient to melt Na (mp = 98°C)
WHY K IGNITES: heat + lower activation energy for H₂ ignition
WHY Cs EXPLODES: Coulomb explosion mechanism — electron ejection so fast it creates
                 a solvated electron burst, then rapid H₂ generation + detonation
```

---

## Flame Test Colors

The single most useful analytical tool for these elements before spectroscopy:

```
FLAME TEST — EMISSION COLORS

  Li  →  crimson red        (670.8 nm — 2p→2s transition)
  Na  →  intense yellow     (589 nm — the famous sodium doublet D₁/D₂ lines)
  K   →  lilac/violet       (766.5 nm, 769.9 nm — often appears pale lilac)
  Rb  →  red-violet         (780 nm)
  Cs  →  blue-violet        (455 nm, 459 nm)

MECHANISM:
  Flame provides enough energy to promote valence electron to higher level
  Electron returns to ground state → emits characteristic photon
  Na's yellow is so intense it masks other colors in impure samples
  (Na contamination is ubiquitous — sweat, dust, glassware)

MODERN ATOMIC EMISSION SPECTROSCOPY (AES):
  Same physics but with plasma source (ICP-AES) instead of flame
  ppb detection limits, multiple elements simultaneously
```

---

## Lithium (Li, Z=3)

**Battery chemistry progression — what replaced what:**

| Generation | Chemistry | Specific energy | Why superseded |
|------------|-----------|-----------------|----------------|
| Lead-acid (1859) | Pb / H₂SO₄ / PbO₂ | 30–50 Wh/kg | Heavy; memory effect; toxic Pb |
| Nickel-cadmium (1899/1960s) | Ni(OH)₂ / KOH / Cd | 40–60 Wh/kg | Cd toxicity; severe memory effect |
| Nickel-metal hydride (1989) | Ni(OH)₂ / KOH / MH alloy | 60–120 Wh/kg | Lower energy than Li-ion; self-discharges |
| Lithium-ion (1991, Sony) | LiCoO₂ / organic electrolyte / graphite | 150–265 Wh/kg | Current dominant; thermal runaway risk |
| Solid-state (emerging) | Li metal / solid electrolyte | 400–500 Wh/kg (projected) | Replacing liquid electrolyte → safer + denser |

The energy density improvement is roughly 5–10× over the lead-acid baseline. The enabling factor at each step was a new electrolyte chemistry that allowed either a higher-voltage cell or a lighter anode material.

### Li-Ion Batteries — The World-Changing Application

```
LITHIUM-ION CELL ARCHITECTURE:

  ┌─────────────────────────────────────────────────────────────┐
  │  DISCHARGE (energy out):                                     │
  │                                                              │
  │  ANODE (−)          ELECTROLYTE       CATHODE (+)           │
  │  graphite           LiPF₆ in         LiCoO₂ / LiFePO₄      │
  │  (Li intercalated)  organic solvent   / NMC / NCA           │
  │                                                              │
  │  LiC₆ → C₆ + Li⁺ + e⁻    Li⁺ migrates    Li₁₋ₓCoO₂ + xLi⁺ + xe⁻ → LiCoO₂
  │         e⁻ → external circuit                                │
  │                                                              │
  │  Nominal voltage: ~3.6-3.7 V                                │
  │  Energy density: 150-265 Wh/kg (cell level)                 │
  └─────────────────────────────────────────────────────────────┘

Li INTERCALATION: Li⁺ ions insert between graphene layers (LiC₆) during charging.
  No Li metal plating at anode in healthy cell — the SEI (solid electrolyte interphase)
  stabilizes the interface.

CATHODE MATERIALS:
  LiCoO₂   (LCO)  — original, high voltage, used in phones — Co is expensive/toxic/scarce
  LiFePO₄  (LFP)  — iron phosphate, safer (thermal stability), lower voltage, long cycle life
  LiNiMnCoO₂ (NMC) — nickel-manganese-cobalt, balance of energy/safety/cost
  LiNiCoAlO₂ (NCA)  — Tesla's original 18650 chemistry — high energy, Co+Al stabilized

SOLID-STATE BATTERIES (next gen):
  Replace liquid electrolyte with solid (Li₆PS₅Cl sulfide, LLZO ceramic)
  No liquid → no thermal runaway → safer
  Enable Li metal anode → much higher energy density
  Technical challenges: solid-solid interface resistance, dendrite suppression
```

### Other Li Applications

```
Lithium in medicine:   Li₂CO₃ / Li citrate for bipolar disorder
                       Mechanism not fully understood; involves second-messenger systems
                       (IP₃ pathway, GSK-3β inhibition, neuroprotection theories)
                       Therapeutic window narrow → blood level monitoring required

Li in grease:          Lithium soap (Li stearate) is the basis of most modern grease
                       (~70% of worldwide grease production uses Li thickener)
                       Thermal stability, water resistance, wide temperature range

Li₂O in glass:        Reduces glass viscosity, lowers melting temp, increases thermal
                       shock resistance (lithia-silicate glass; telescope mirror blanks)

Li₇LaNbO₃ (LLNO):     Solid electrolyte research

Isotope enrichment:    Li-6 is used in fusion fuel (⁶Li + n → T + ⁴He for tritium breeding)
                       Li-7 for PWR coolant pH control (as LiOH)
```

---

## Sodium (Na, Z=11)

### Na-K ATPase — Biological Command and Control

```
Na-K ATPase is the ion pump that maintains the resting membrane potential of every
animal cell. It consumes ~1/3 of all neuronal ATP.

  PUMP CYCLE:
  ┌──────────────────────────────────────────────────────────┐
  │  1. 3 Na⁺ bind intracellularly                          │
  │  2. ATP phosphorylates the pump → conformational change  │
  │  3. 3 Na⁺ released extracellularly                      │
  │  4. 2 K⁺ bind extracellularly                           │
  │  5. Dephosphorylation → pump resets                      │
  │  6. 2 K⁺ released intracellularly                       │
  │                                                          │
  │  Net: 3 Na⁺ out, 2 K⁺ in (against concentration grad.) │
  │       Membrane potential = −70 mV at rest               │
  └──────────────────────────────────────────────────────────┘

Consequences:
  • High Na⁺ outside (140 mM) vs low inside (10 mM)
  • High K⁺ inside (140 mM) vs low outside (4 mM)
  • This gradient drives the action potential (depolarization = Na⁺ flows in)
  • Cardiac muscle rhythm depends on Na/K balance → digoxin inhibits pump → treats heart failure
```

### Industrial Sodium Chemistry

```
CHLOR-ALKALI PROCESS:
  2 NaCl + 2 H₂O → Cl₂ + H₂ + 2 NaOH  (electrolysis of brine)
  Three co-products sold separately:
    Cl₂  → PVC, solvents, bleach, disinfection
    NaOH → paper (kraft process), alumina refining, soap, food processing
    H₂   → fuel cells, hydrogenation, HCl synthesis

SOLVAY PROCESS (Na₂CO₃, soda ash):
  NH₃ + CO₂ + NaCl + H₂O → NaHCO₃↓ + NH₄Cl
  2 NaHCO₃ → Na₂CO₃ + H₂O + CO₂
  Uses: glass, detergents, paper, food (baking soda is NaHCO₃)

SODIUM METAL:
  Made by Downs cell electrolysis of molten NaCl:
    Cathode: Na⁺ + e⁻ → Na(l)
    Anode:   2Cl⁻ → Cl₂ + 2e⁻
  Uses: Na-S batteries (utility storage), Na metal as reductant in organic chemistry,
        street lamps (high-pressure sodium, HPS) — those yellow-orange highway lights

SALT (NaCl):
  Human biology: 1.4-1.7 g Na/day required; osmotic regulation, nerve function
  Food preservation: ancient and modern; osmotic + Cl⁻ antimicrobial effect
  De-icing: exothermic dissolution lowers freezing point (effective to ~−10°C)
  ~280 million tonnes NaCl produced annually — largest commodity chemical by volume
```

---

## Potassium (K, Z=19)

```
K in biology:
  Intracellular cation (maintained by Na-K ATPase)
  Resting membrane potential set by K⁺ gradient (Nernst potential: −89 mV for K)
  K⁺ channels in cardiac pacemaker cells → rhythm control
  Hyperkalemia (high K⁺) → cardiac arrhythmia/arrest (used in lethal injection: KCl)
  Dietary sources: bananas (~358 mg K each), potatoes, leafy greens

KOH and KCl:
  KOH  → liquid soap making, electrolyte in alkaline batteries and fuel cells
  KCl  → fertilizer (potash — K₂O equivalent), food-grade salt substitute
  KNO₃ → oxidizer in gunpowder (75% KNO₃ + 15% charcoal + 10% S)

Potash mining:
  Most K comes from ancient evaporite deposits (sylvinite = KCl + NaCl)
  Major producers: Canada (Saskatchewan), Russia, Belarus
  ~90% of K production goes to fertilizers — critical for food security
```

---

## Cesium (Cs, Z=55)

### The Cs Atomic Clock — Defining the Second

```
THE SI SECOND:
  1 second = 9,192,631,770 cycles of the radiation corresponding to the
  hyperfine transition of the ground state of ¹³³Cs

  HYPERFINE STRUCTURE:
  ¹³³Cs ground state: [Xe]6s¹
  Nuclear spin I = 7/2 + electron spin → F = 3 (lower) and F = 4 (upper)
  Energy difference = 6.8 GHz → microwave transition

  CESIUM BEAM ATOMIC CLOCK OPERATION:
  ┌─────────────────────────────────────────────────────────────┐
  │  1. Heat Cs → beam of atoms                                 │
  │  2. Magnet selects F=3 state atoms (state preparation)      │
  │  3. Microwave cavity irradiates atoms at ~9.19 GHz          │
  │  4. Magnet selects F=4 state atoms (state detection)        │
  │  5. Feedback loop locks microwave to maximize F=4 signal    │
  │  6. Count oscillations → time                               │
  │                                                              │
  │  Accuracy: ~5×10⁻¹⁴ (NIST F-2 fountain clock)             │
  │  Optical clocks (Al⁺, Sr lattice) now ~10⁻¹⁸ — better     │
  │  but Cs still defines the SI second                         │
  └─────────────────────────────────────────────────────────────┘

GPS depends on atomic clocks: 1 ns timing error → 30 cm position error.
GNSS satellites carry Cs or Rb atomic frequency standards.
```

### Cesium Uses

```
Photoelectric effect: Cs has lowest IE of stable elements → releases electrons from light
  → photomultiplier tube cathodes, solar cells research

Cesium formate (HCOOCs): oil drilling fluid (very dense liquid, ~2.3 g/cm³)
  High-density brine displaces formation fluids without solids that damage wells

Cs-137: nuclear waste product of fission (t½ = 30.2 yr, β⁻ + γ emitter)
  Radiotherapy for cancer
  Source in Goiânia accident 1987 — 249 contaminated, 4 died
  Long-lived → remains decades after Chernobyl/Fukushima

NaCs/RbCs magneto-optical traps: ultracold physics, quantum information experiments
```

---

## Rubidium (Rb, Z=37)

```
[Kr]5s¹  |  IE₁: 403 kJ/mol  |  Radius: 248 pm  |  E° = −2.98 V

RUBIDIUM ATOMIC CLOCK:
  Rb has two ground-state hyperfine levels separated by 6.834682… GHz
  → microwave transition, same physics as Cs but less accurate long-term
  Rb clocks: compact, low-power, fast warm-up → used in GPS satellites
    (each GPS satellite carries two Rb + one Cs; Rb for normal operation)
  Accuracy: ~5×10⁻¹² (vs Cs at ~5×10⁻¹⁴) — sufficient for GPS; periodically
    corrected against Cs ground standards
  Size: ~1 L module vs Cs fountain ~1 m³ → why Rb wins in space applications

Rb-Sr RADIOMETRIC DATING:
  ⁸⁷Rb → ⁸⁷Sr  (β⁻ decay, t½ = 49.23 Gyr)
  Isochron dating: plot ⁸⁷Sr/⁸⁶Sr vs ⁸⁷Rb/⁸⁶Sr for cogenetic rocks
  Slope of isochron = (eλt − 1) → solve for t
  Range: ~10 Myr to Earth's age (4.54 Gyr)
  Useful for: crustal formation ages, mantle differentiation, meteorites

LASER COOLING AND BEC:
  ⁸⁷Rb: most commonly laser-cooled atom (1995 BEC — Cornell/Wieman Nobel 2001)
  Reason: strong D1/D2 lines accessible with cheap diode lasers (~780 nm)
  Doppler cooling → magneto-optical trap → evaporative cooling → ~100 nK
  Bose-Einstein Condensate: macroscopic quantum state; tests of QM, atom interferometry
  → Rb-based atom interferometers as gravimeters (precision g measurement)

OTHER USES:
  RbAg₄I₅: solid-state ion conductor (historical battery electrolyte research)
  Rb in photomultipliers: photoelectric cathode (lower IE → sensitive to longer wavelengths)
  Rb₂CO₃: specialized optics glass dopant
```

## Francium (Fr, Z=87)

```
MOST UNSTABLE NATURAL ELEMENT:
  Most stable isotope: ²²³Fr, t½ = 22 minutes
  Daughter of ²²⁷Ac (actinium decay chain); only ~30 g on Earth at any time
  ~6700 atoms held in MOT at one time (current record, ISOLDE/CERN + TRIUMF)

No practical uses — purely academic.
Studies: atomic parity non-conservation (tests Standard Model at low energy),
         photoionization cross sections, comparison with theory.
Chemistry: similar to Cs (extrapolated), too little to measure directly.
```

---

## Decision Cheat Sheet

| Need | Element | Key compound/form |
|------|---------|-------------------|
| Battery anode material | Li | Graphite-intercalated (Li-ion) or future Li metal (solid state) |
| Nervous system ion | Na & K | Na⁺ (extracellular), K⁺ (intracellular) — maintained by Na-K ATPase |
| Time standard | Cs | ¹³³Cs hyperfine transition = SI second |
| Potash fertilizer | K | KCl (muriate of potash), K₂SO₄ (sulfate of potash) |
| Chlorine production | Na | NaCl electrolysis (chlor-alkali) |
| Bipolar disorder treatment | Li | Li₂CO₃ (lithium carbonate), serum Li⁺ monitoring required |
| GPS clock | Cs or Rb | Atomic clock using hyperfine transitions |
| Yellow flame test | Na | 589 nm sodium D-line — unambiguous |

---

## Common Confusion Points

**"K is higher in the activity series than Na, but Na has higher IE. Contradiction?"**
Not exactly. Electrochemical reduction potential (E°) depends on ionization energy + hydration
enthalpy. K⁺ has lower charge density than Na⁺ → weaker hydration → less energy recovered
on hydration. These factors nearly cancel; the result is that K(s)/K⁺(aq) is slightly more
negative (−2.93 V) than Na(s)/Na⁺(aq) (−2.71 V), meaning K is slightly more easily oxidized
in aqueous solution, even though its gas-phase IE is lower.

**"Why does cesium appear to be a better clock reference than hydrogen (maser)?"**
Hydrogen maser is actually MORE stable short-term (lower short-term noise). Cs clock wins on
long-term accuracy — the physical transition frequency is more precisely defined and measured
over many hours/days. GPS uses Rb clocks (cheap, small) that are periodically corrected by
Cs-based ground stations.

**"If all alkali metals have +1 oxidation state, why does Li behave so differently from Cs?"**
Same oxidation state, but very different ionic radii (Li⁺ = 76 pm vs Cs⁺ = 167 pm).
Small Li⁺ has very high charge density → strong hydration, forms strong covalent-like bonds,
diagonal relationship with Mg²⁺. Li compounds are often less soluble than Na/K analogs
because lattice energies are high (small cation). This is the **diagonal relationship** in
the periodic table: Li resembles Mg more than it resembles Cs.
