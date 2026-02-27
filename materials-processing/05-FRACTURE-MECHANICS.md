# Fracture Mechanics and Fatigue

## The Big Picture

Fracture mechanics quantifies the conditions under which a crack will grow. Classical materials strength (ultimate tensile stress, yield stress) cannot predict failure when cracks or defects exist. Fracture mechanics provides the critical framework: given a crack of known size, at what applied stress does it become unstable and propagate catastrophically?

```
WHY FRACTURE MECHANICS EXISTS
──────────────────────────────────────────────────────────────────
Classical stress analysis:                 Fracture mechanics:
  Safe if σ < σ_uts                         Accounts for existing cracks
  Assumes no defects                         Inevitable in real structures
  Fails when:
    Liberty ships fractured at             Griffith (1921): cracks are sharp
    stresses well below σ_uts              stress concentrators → local stress
    Comet aircraft disintegrated           at crack tip → ∞ for perfectly sharp
    at stress levels that                  crack in elastic solid
    "should have been safe"

Answer: real structures ALWAYS have cracks.
  The question is not "is there a crack?"
  The question is "at what size does this crack become critical?"
```

---

## Linear Elastic Fracture Mechanics (LEFM)

### The Stress Intensity Factor K

```
STRESS INTENSITY FACTOR (K)
──────────────────────────────────────────────────────────────────
K characterizes the stress field near a crack tip:
  σ_ij ≈ K / (√(2πr)) × f_ij(θ)

  where r = distance from crack tip, θ = angle

K = Y × σ × √(πa)
  Y = geometry factor (dimensionless, from handbooks)
  σ = applied stress (MPa)
  a = crack half-length (m) for internal crack
      crack length for edge crack

Units: MPa√m  (or ksi√in in old US literature)

Three modes:
  Mode I: Opening (tension perpendicular to crack plane) — dominant
  Mode II: Sliding (shear in crack plane, in-plane)
  Mode III: Tearing (shear in crack plane, out-of-plane)

Fracture occurs when: K_I = K_IC
  K_IC = plane-strain fracture toughness (material property)
  Minimum K needed to fracture in most severe (plane strain) condition
```

### Critical Crack Size and Safety

```
FRACTURE MECHANICS DESIGN EQUATION
──────────────────────────────────────────────────────────────────
At fracture: K_IC = Y × σ_f × √(πa_c)

Three linked variables — given any two, solve for third:

SCENARIO 1: Given K_IC and σ, find critical crack size a_c
  a_c = (1/π) × (K_IC / (Y × σ))²

  Example: 4340 steel, K_IC = 50 MPa√m, σ = 600 MPa, Y = 1.0
  a_c = (1/π) × (50/600)² = (1/π) × 0.00694 = 2.2 mm
  Any crack larger than 2.2 mm → catastrophic fracture at 600 MPa

SCENARIO 2: Given K_IC and a, find fracture stress σ_f
  σ_f = K_IC / (Y × √(πa))
  Used for: retired aircraft with known crack sizes (NDT results)

SCENARIO 3: Given σ and a, check if material K_IC is sufficient
  K_I = Y × σ × √(πa)
  Compare to K_IC of candidate materials

SAFETY FACTOR:
  N = K_IC / K_I  (applied)
  N = a_c / a_detected  (if NDT finds crack of size a)
  Typically N ≥ 2–4 for non-critical structure
  Aerospace damage tolerance: find crack, verify it won't grow to critical
    size before next inspection interval
```

### Fracture Toughness Values

| Material | K_IC (MPa√m) | Notes |
|----------|-------------|-------|
| Glass | 0.5–1 | Very brittle |
| Alumina (Al₂O₃) | 3–5 | Structural ceramic |
| Si₃N₄ | 5–8 | Tougher ceramic |
| Steel (4340, high strength) | 40–60 | Structural aerospace |
| Steel (4340, low strength Q&T) | 80–120 | Tougher, lower strength |
| Aluminum 2024-T3 | 34–44 | Aircraft wing skin |
| Aluminum 7075-T6 | 25–30 | High strength, lower K_IC |
| Titanium Ti-6Al-4V | 50–80 | Aerospace structural |
| Inconel 718 | 100–130 | Ni superalloy, tough |
| Mild steel | 140–200 | Very tough |

---

## Ductile vs Brittle Fracture

```
FRACTURE MODE COMPARISON
──────────────────────────────────────────────────────────────────
BRITTLE FRACTURE:
  Little or no plastic deformation before fracture
  Crack propagates rapidly (near speed of sound in material)
  Fracture surface: flat, crystalline appearance (cleavage)
  Common in: ceramics, glass, BCC metals at low T
  Energy absorbed: minimal
  Macroscopic warning: none (sudden)

DUCTILE FRACTURE:
  Significant plastic deformation precedes fracture
  Fracture surface: fibrous, dimpled (microvoid coalescence)
  Common in: FCC metals (Al, Cu), BCC steel at high T
  Energy absorbed: substantial (dimples = microvoid nucleation and growth)
  Macroscopic warning: necking, distortion visible before fracture

DUCTILE-BRITTLE TRANSITION (DBT):
  BCC metals (ferritic steel, W, Mo) transition from ductile to brittle
  as temperature decreases. FCC metals (Al, Cu, austenitic SS) do NOT.

  Ductile-Brittle Transition Temperature (DBTT):
    Measured by Charpy impact test (energy vs temperature curve)
    Ferritic steel: DBTT ≈ 0°C to −50°C depending on composition
    High-N steel: higher DBTT (embrittled)
    Ni additions: lower DBTT (better low-temp toughness)
```

---

## Fatigue

### S-N (Wöhler) Curves

```
S-N CURVE STRUCTURE
──────────────────────────────────────────────────────────────────
Stress amplitude
  │
  │ High stress
  │  ●
  │    ●
  │      ●  Low cycle (LCF)
  │        ●
  │          ●──── Endurance limit (steel only)
  │                (no failure below this stress, regardless of N)
  │
  │                For aluminum, no true endurance limit
  │                (failure eventually at any stress)
  └─────────────────────────────────────────────────────────► log N
     10²    10³   10⁴   10⁵   10⁶   10⁷   10⁸
                         ↑
                    ~10⁷ cycles = commonly used "infinite life"

Ferrous (steel): True endurance limit σ_e ≈ 0.5 × UTS (for polished bar)
Non-ferrous (Al, Ti): Use σ at 10⁷ or 10⁸ cycles (no true limit)
```

### Factors That Reduce Fatigue Life

```
FATIGUE REDUCTION FACTORS
──────────────────────────────────────────────────────────────────
Surface finish:
  Rough surface → stress concentrations → early crack initiation
  Polished specimen (S-N data): Ra 0.4 µm
  Machined shaft: Ra 1.6 µm → 80% of polished endurance
  Hot-rolled surface: Ra 6 µm → 50–60% of polished
  Corroded surface: 30–50% reduction

Stress concentrations (Kt):
  Notch, keyway, shoulder fillet, hole, thread → amplifies stress
  Kt = σ_local_max / σ_nominal
  Fatigue notch factor Kf = 1 + q(Kt-1)
  q = notch sensitivity (0 = no sensitivity, 1 = full effect)
  Fine-grained materials: high q → more notch sensitive

Mean stress effect (Goodman relationship):
  Fatigue life decreases as mean stress increases (tensile mean)
  Goodman: σ_a/σ_e + σ_m/σ_UTS = 1
  (σ_a = alternating component, σ_m = mean, σ_e = endurance limit)

Compressive residual stress:
  IMPROVES fatigue life (opposes crack opening)
  Shot peen, case harden, autofrettage all add compressive surface stress

Size effect:
  Larger specimens have lower fatigue strength
  More volume at high stress → higher probability of initiating crack
```

### Paris Law (Fatigue Crack Growth)

<!-- @editor[bridge/P2]: The Paris law integration (N = ∫ da / C(ΔK)^m from a_i to a_c) is a first-order ODE integration — crack size a(N) evolves according to da/dN = f(a), and we integrate numerically to find when a reaches the critical value a_c. Any numerical methods background immediately recognizes this as an IVP (initial value problem) for crack growth, solved by standard quadrature or Euler-like stepping. The life calculation is just integrating the ODE — naming this connection would help any CS reader who knows numerical integration but finds "integrate the Paris law" opaque. -->
```
PARIS LAW: DA/DN = C × ΔK^m
──────────────────────────────────────────────────────────────────
da/dN = C × (ΔK)^m

da/dN = crack growth rate (m/cycle or in/cycle)
ΔK    = stress intensity factor RANGE = K_max - K_min = Y × Δσ × √(πa)
C, m  = material constants (from crack growth test data)
         m ≈ 2–4 for most metals (steel: m ≈ 3, Al: m ≈ 4)

FATIGUE CRACK GROWTH CURVE (da/dN vs ΔK):
               log(da/dN)
                     │              Region III:
              Rapid  │            unstable crack
              growth │          /  growth (K_IC)
                     │         /
              Paris  │       /  slope = m
              regime │     /
                     │   /
              Thresh │ /
              hold   ◄ ΔK_th (threshold — no growth below this)
                     └──────────────────────────────► log(ΔK)

ΔK_th (threshold):  crack does not grow below this ΔK
  Steel: ~5–10 MPa√m
  Aluminum: ~1–3 MPa√m (lower threshold = more crack growth concern)
```

### Damage Tolerance and Inspection Intervals

<!-- @editor[bridge/P1]: Damage tolerance engineering IS reliability engineering applied to crack growth. The framework maps exactly: assume a worst-case initial defect (= assume worst-case initial condition), integrate the failure model forward (Paris law = crack growth rate equation), set maintenance interval = fraction of time-to-failure (= inspection interval = half the predicted life). This is probabilistic safety analysis — the same framework used in aerospace software certification (DO-178C reliability analysis), nuclear safety (fault tree analysis), and dependable systems design. Any software infrastructure engineer who thinks about MTBF and maintenance intervals maps this immediately. The connection is never named. -->
```
DAMAGE TOLERANCE APPROACH (aircraft structures)
──────────────────────────────────────────────────────────────────
Philosophy: cracks are inevitable; design so they are detectable
  before they become critical.

1. Assume initial crack size = NDT detection threshold
   (e.g., NDT finds cracks > 0.5mm: assume a_initial = 0.5mm)

2. Calculate crack growth life from a_initial to a_critical
   Integrate Paris law: N = ∫(da) / (C × (Y × Δσ × √(πa))^m)

3. Set inspection interval = fraction of calculated growth life
   Typical: inspect at ≤ half the calculated life
   (Factor of 2 safety on inspection intervals)

4. At each inspection: if crack found below a_critical → OK, reinspect
   If crack at or near a_critical → repair or retire

FAR Part 25 (airworthiness):
  Two-load-path (fail-safe) structures required where possible
  Single-load-path: must pass damage tolerance analysis
  Critical crack detection must be achievable with available NDT
```

---

## Fracture Toughness Testing

### K_IC Test (ASTM E399)

```
PLANE-STRAIN K_IC TEST
──────────────────────────────────────────────────────────────────
Specimen types: compact tension (CT), single edge notch beam (SENB)
  Pre-cracked: fatigue pre-crack at notch root
  Sharp natural crack: ΔK must be < 0.002 E b (specimen thickness b)

Test conditions:
  Slow, monotonic loading
  Load-displacement curve measured
  K_IC = f(P_Q, B, W, a₀)

Validity requirements (plane strain):
  B ≥ 2.5 (K_IC/σ_YS)²     specimen thickness
  a ≥ 2.5 (K_IC/σ_YS)²     crack length
  W-a ≥ 2.5 (K_IC/σ_YS)²   remaining ligament

If requirements not met: K_Q (provisional value, not valid K_IC)
  High-strength materials (σ_YS high): easier to meet thickness req
  Tough, low-strength materials: need very thick specimens for plane strain
```

### Charpy Impact Test

```
CHARPY IMPACT TEST
──────────────────────────────────────────────────────────────────
Standardized notched bar struck by pendulum hammer
Measures energy absorbed in fracture (joules)
Rapid, cheap, qualitative → widely used for acceptance testing

NOT the same as K_IC:
  Dynamic loading (vs. quasi-static K_IC)
  No stress intensity factor units
  Correlations to K_IC exist but are empirical

Key uses:
  DBTT (ductile-brittle transition temperature) determination
  Acceptance testing (ASTM A370: structural steel CVN requirements)
  Weld qualification (heat-affected zone toughness)
  Low-temperature toughness verification (cryogenic structures)

DBTT from Charpy:
  Run tests at multiple temperatures → energy vs T curve
  DBTT = temperature where 50% of fracture surface is cleavage
         or where energy = 27 J (ASTM A36/A572 spec)
```

---

## Failure Mode Analysis

### Fractography (Fracture Surface Analysis)

```
FRACTOGRAPHIC FEATURES
──────────────────────────────────────────────────────────────────
OVERLOAD (monotonic fracture):
  Ductile: dimpled surface (microvoid coalescence)
    Dimple size ~ inclusion/precipitate spacing
  Brittle: river marks (cleavage)
    River marks converge on crack origin (use to trace back)
    Herringbone pattern on macroscale

FATIGUE:
  Beach marks (macro): curved parallel marks, visible to naked eye
    Each mark = change in loading or crack arrest
    Converge to origin (find origin with beach marks)
  Striations (micro): SEM visible (~1 nm to µm/cycle spacing)
    Each striation = one load cycle
    Count striations → quantify growth rate at that location
  Ratchet marks: multiple initiation sites (overloaded or corrosion)

STRESS CORROSION CRACKING (SCC):
  Brittle-looking fracture in ductile material
  Intergranular (grain boundary attack) or transgranular
  Associated with specific material/environment combinations:
    High-strength Al in NaCl or moist air
    Brass in ammonia
    Stainless in hot chlorides

HYDROGEN EMBRITTLEMENT:
  Brittle fracture, intergranular or transgranular
  Whittle-like marks, no dimples
  Delayed fracture (hours or days after loading)
  Common: high-strength steel fasteners with cadmium plating,
          electroplated parts (hydrogen from plating bath)
```

---

## Decision Cheat Sheet

| Fracture/Fatigue Challenge | Approach |
|---------------------------|----------|
| Find critical crack size at given stress | K_IC = Y × σ × √(πa_c), solve for a_c |
| Determine if material choice affects crack tolerance | Compare K_IC values |
| Calculate inspection interval | Integrate Paris law, divide by safety factor |
| Improve fatigue life of shaft | Shot peen, improve surface finish, fillet radii |
| Diagnose fracture origin from fracture surface | Fractography (beach marks, river marks) |
| Test weld HAZ toughness for structural qualification | Charpy impact at specified temperature |
| Identify ductile-brittle transition | Charpy vs temperature curve |
| Assess low-temperature suitability | Check DBTT vs operating temperature |

---

## Common Confusion Points

**K and K_IC have the same units, but different roles**: K (stress intensity factor) is a loading parameter — it describes the applied crack-tip stress field. K_IC (plane-strain fracture toughness) is a material property — it is the K at which the material fractures. Failure when K ≥ K_IC. They are the same quantity only at fracture.

**Endurance limit is only for ferrous materials**: Steel and iron have a true endurance limit (no failure below σ_e, regardless of cycles). Aluminum, titanium, copper, most non-ferrous alloys do NOT have a true endurance limit — they will eventually fail at any positive cyclic stress if enough cycles are applied. This is critical for rotating aluminum aircraft structures.

**Paris law integration understates life in region I and III**: The Paris law (middle of the da/dN vs ΔK curve) is the region where growth is approximately linear in log-log space. Near threshold (region I), growth rate drops dramatically — life is dominated by cracks spending millions of cycles at near-threshold ΔK. Near K_IC (region III), growth accelerates rapidly. For accurate life prediction: use the full sigmoidal curve, not just Paris law.

**Charpy energy ≠ K_IC**: Charpy is qualitative, impact-loaded, uncontrolled crack length. K_IC is quasi-static, pre-cracked specimen, geometrically rigorous. Empirical correlations between Charpy CVN (ft-lb) and K_IC (ksi√in) exist for steels (CVN ≈ K_IC²/5E — Sailors/Corten), but they are rough estimates, not substitutes.

**High K_IC is not always better**: High fracture toughness usually comes with lower yield strength (strength-toughness tradeoff). An ultra-high-strength structure (aircraft landing gear: 1500 MPa) has lower K_IC (~50 MPa√m). A medium-strength structure (structural steel: 500 MPa) has much higher K_IC (~200 MPa√m). The DESIGN must match material selection to the combination of stress level and expected crack size.
