# Receptor Theory: Agonists, Antagonists, Affinity

## The Big Picture

Receptor theory is the mathematical and mechanistic framework for how drugs interact with their molecular targets. It predicts drug effect from concentration and provides the language for comparing drugs.

```
+──────────────────────────────────────────────────────────────────+
|                  RECEPTOR THEORY LANDSCAPE                       |
|                                                                  |
|  RECEPTOR = Macromolecule that binds drug → transduces signal   |
|                                                                  |
|  DRUG-RECEPTOR INTERACTION                                       |
|  Drug (D) + Receptor (R) ⇌ Drug-Receptor complex (DR) → Effect  |
|                                                                  |
|  KEY QUESTIONS                                                    |
|  1. How tightly does drug bind?   → Affinity (Kd)               |
|  2. How much receptor is occupied? → Occupancy                  |
|  3. What effect does binding produce? → Efficacy / Intrinsic    |
|                                         activity                 |
|  4. Full agonist? Partial? Antagonist? Inverse?                  |
|                                                                  |
|  OCCUPANCY THEORY (Clark 1926)                                   |
|  Effect ∝ fraction of receptors occupied by drug                |
+──────────────────────────────────────────────────────────────────+
```

---

## Receptor Types

```
MEMBRANE RECEPTORS (extracellular target)
──────────────────────────────────────────

  TYPE                 MECHANISM               SPEED    EXAMPLES
  ─────────────────    ─────────────────────   ─────    ────────────────────
  Ionotropic (ligand-  Drug opens ion channel  ms       GABA_A, nAChR
  gated ion channel)                                    NMDA (glutamate)

  GPCR (G-protein      Drug → G-protein →      sec      Adrenergic (β-blocker)
  coupled receptor)    adenylyl cyclase →              Opioid, dopamine
                       cAMP, PKA cascade               Muscarinic (atropine)

  Receptor tyrosine    Drug → autophospho-     min      Insulin receptor
  kinase (RTK)         rylation → MAPK, PI3K           EGF receptor (erlotinib)
                       cascades

  Cytokine receptors   JAK-STAT pathway        min-hr   EPO, IL-2, IFN-γ

INTRACELLULAR RECEPTORS
────────────────────────
  Nuclear receptors: Steroid/thyroid hormones enter cell,
  bind nuclear receptor → transcription factor → gene expression changes.
  Time: hours. Duration: long.

  Examples:
    Glucocorticoid receptor → cortisol, prednisone
    Estrogen receptor → estrogens, tamoxifen (antagonist)
    PPAR → fibrates (cardiovascular), thiazolidinediones (diabetes)
    Retinoid receptor → vitamin A, isotretinoin

STRUCTURAL FEATURES
  All receptors: binding domain (orthosteric site) + effector domain
  Allosteric sites: distinct from orthosteric, modulate without blocking
```

---

## Law of Mass Action and Occupancy

**The fundamental equation of receptor pharmacology:**

```
DRUG-RECEPTOR BINDING
──────────────────────
  D + R ⇌ DR
       k₊₁
  D + R ──→ DR  (association rate)
       k₋₁
  DR ──→ D + R  (dissociation rate)

  At equilibrium:
    Kd = k₋₁/k₊₁ = [D][R] / [DR]   (dissociation constant)

FRACTIONAL RECEPTOR OCCUPANCY (pO)
  pO = [DR] / ([R] + [DR]) = [D] / ([D] + Kd)

  This is the Hill equation with n=1 (no cooperativity).

  When [D] = Kd:   pO = 0.5    (50% occupancy)
  When [D] = 9Kd:  pO = 0.9    (90% occupancy)
  When [D] = 99Kd: pO = 0.99   (99% occupancy)

  Kd has units of concentration (nM, μM, μg/mL).
  Lower Kd = higher affinity = drug binds at lower concentration.
```

---

## Efficacy: What Happens After Binding

Occupancy ≠ effect. A drug can bind without producing an effect (antagonist):

```
INTRINSIC ACTIVITY (α)
────────────────────────
Effect = α × pO × Emax

  α = 1.0   Full agonist (maximum possible response)
  0 < α < 1 Partial agonist (less than maximum response)
  α = 0     Antagonist (no response, just blocks)
  α < 0     Inverse agonist (active receptors turned OFF)

EFFICACY vs POTENCY
  Efficacy = maximum achievable effect (Emax × α)
  Potency  = concentration needed for 50% of maximum response (EC50)

  ┌─────────────────────────────────────────────────────────┐
  │           DOSE-RESPONSE CURVES                          │
  │                                                         │
  │ Effect  100% │ ━━━━━━━━━━━━ A (full agonist)           │
  │          75% │     ━━━━━━━━ B (partial agonist)        │
  │          50% │ A50%          B50%                       │
  │              │ │              │                         │
  │              └─│──────────────│──────────→ [Drug]      │
  │                EC50_A         EC50_B                    │
  │                (lower = more potent)                    │
  └─────────────────────────────────────────────────────────┘

  Drug A: high efficacy, high potency (low EC50)
  Drug B: lower efficacy, lower potency — different in BOTH ways
```

---

## Antagonism Types

```
COMPETITIVE (SURMOUNTABLE) ANTAGONISM
───────────────────────────────────────
Antagonist competes with agonist for same binding site.
At equilibrium:

  pO = [D] / ([D] + Kd(1 + [I]/Ki))

  where [I] = antagonist concentration, Ki = antagonist Kd

  Effect: shifts agonist dose-response curve RIGHT (higher EC50)
  Enough agonist can overcome the antagonist (surmountable).

  Example: atropine (anticholinergic) blocks acetylcholine at mAChR.
  High doses of ACh can overcome atropine.

NON-COMPETITIVE ANTAGONISM
───────────────────────────
Antagonist binds at a different site (allosteric) or binds
irreversibly to the orthosteric site.

  Effect: reduces Emax (cannot be surmounted by more agonist)
  Dose-response: same EC50, lower ceiling.

  Example: phenoxybenzamine (irreversible α-blocker in pheochromocytoma)

IRREVERSIBLE ANTAGONISM
────────────────────────
Covalent binding. Drug effect outlasts drug presence.
Duration determined by rate of new protein synthesis, not drug clearance.

  Examples:
    Aspirin: irreversibly acetylates COX-1 in platelets.
    Platelet effect lasts 7-10 days (platelet lifetime — platelets
    have no nucleus, can't make new COX-1).

UNCOMPETITIVE ANTAGONISM
─────────────────────────
Binds to agonist-BOUND receptor only. Rare but important:
  Memantine (Alzheimer's): binds NMDA channel when open.
  More activated channel = more blocking.
```

---

## Partial Agonists: The Dual Role

```
PARTIAL AGONIST BEHAVIOR
──────────────────────────
In presence of full agonist:
  Partial agonist competes with full agonist.
  Net effect: REDUCES response (acts as functional antagonist).

  If full agonist is causing toxicity/addiction:
    Partial agonist displaces full agonist → less effect
    But doesn't produce zero effect (has own intrinsic activity)

In absence of full agonist:
  Partial agonist is the only thing activating receptor → some effect.

CLINICAL EXAMPLE: BUPRENORPHINE
  Full agonist at opioid receptor = morphine, heroin → high efficacy, addiction
  Partial agonist = buprenorphine (Suboxone)
    • If opioid-dependent: buprenorphine displaces heroin → prevents withdrawal
    • Ceiling effect: buprenorphine can't cause the same euphoria as full agonist
    • Difficult to overdose (ceiling on respiratory depression)
    • Used to treat opioid addiction

  Partial agonist = "ceiling" drug — both antagonist (displaces full agonist)
  and agonist (prevents withdrawal).

OTHER PARTIAL AGONISTS
  Aripiprazole (atypical antipsychotic): D2 partial agonist
  Buspirone (anxiolytic): 5-HT1A partial agonist
  Varenicline (smoking cessation): nAChR partial agonist
```

---

## GPCR Signaling Cascade: The Full Mechanism

```
GPCR → EFFECTOR PATHWAY
──────────────────────────

  AGONIST
    │
    v
  ┌─────────────────────────────────────────────────────┐
  │  RECEPTOR (7-transmembrane GPCR)                   │
  │  Conformational change → activates Gα subunit       │
  └───────────────────────┬─────────────────────────────┘
                          │
          ┌───────────────┼──────────────────┐
          │               │                  │
          v               v                  v
   Gαs (stimulates)  Gαi (inhibits)    Gαq (activates)
   adenylyl cyclase  adenylyl cyclase  phospholipase C
          │               │                  │
          v               v                  v
        cAMP↑           cAMP↓          DAG + IP3
          │                                  │
          v                          ┌───────┴──────┐
         PKA                         │              │
          │                        PKC           Ca²⁺ release
          v                          │              │
    Phosphorylation              Protein           CaM kinase
    of target proteins           phosphorylation        │
                                                   Multiple effects

BETA-ADRENERGIC RECEPTOR (heart)
  Epinephrine → Gαs → ↑cAMP → ↑PKA → ↑heart rate, ↑contractility
  β-blocker (propranolol): competitive antagonist → blocks this cascade
  → ↓heart rate, ↓blood pressure
```

---

## Receptor Regulation: Desensitization and Upregulation

```
PROLONGED AGONIST EXPOSURE → DESENSITIZATION
──────────────────────────────────────────────
Tolerance: the need for more drug to achieve the same effect.

  TIME COURSE
  Short-term (min-hr): Receptor phosphorylation → β-arrestin binding
                        → Uncoupled from G-protein (functional desensitization)

  Medium-term (hr-days): Receptor internalization (endocytosis)
                          → Fewer receptors on surface (downregulation)

  Long-term (days-wk): Decreased receptor gene expression
                        → Fewer receptors total

  CLINICAL: Opioid tolerance, β-agonist tolerance in asthma,
  nitrate tolerance (nitroglycerin becomes ineffective with constant use)

RECEPTOR UPREGULATION (after antagonist exposure)
  β-blocker (propranolol) chronically used → heart upregulates β-receptors
  → Suddenly stopping propranolol: excess β-receptors + normal catecholamines
  → Rebound tachycardia, potentially dangerous
  → NEVER abruptly stop β-blockers in cardiac patients
```

---

## Hill Equation and Cooperativity

```
HILL EQUATION (generalized)
────────────────────────────
  pO = [D]ⁿ / ([D]ⁿ + Kd^n)

  n = Hill coefficient
  n = 1: no cooperativity (standard Michaelis-Menten)
  n > 1: positive cooperativity (binding promotes more binding)
  n < 1: negative cooperativity

SIGMOIDAL DOSE-RESPONSE CURVE
  Plotted as effect vs log[D]:
  n = 1: sigmoidal, symmetric about EC50
  n > 1: steeper sigmoid
  n < 1: shallower sigmoid

  The log-scale plot linearizes the curve for reading EC50 directly.

EXAMPLES OF COOPERATIVITY
  Hemoglobin + O₂: n ≈ 2.8 (positive cooperativity — O₂ binding
    promotes further O₂ binding)
  Most drug-receptor interactions: n ≈ 1 (no cooperativity)
  Allosteric enzymes: can be positive (n>1) or negative (n<1)
```

---

<!-- @editor[bridge/P3]: Natural bridge: receptor binding/occupancy theory maps directly to CS lock contention and resource allocation — Kd is the dissociation constant analogous to a timeout/backoff constant, competitive antagonism is resource contention at a shared binding site -->
## Decision Cheat Sheet

<!-- @editor[structure/P3]: Cheat sheet reads as a reference summary rather than a decision tool — consider reframing as "I need to..." / "Look at..." / "Because..." to give it a decision-guiding structure (see 04-CYP for a good example) -->
| Concept | Key Equation/Relationship | Clinical Relevance |
|---------|--------------------------|-------------------|
| Affinity | Kd = [D][R]/[DR] | Determines concentration needed to occupy receptor |
| Occupancy | pO = [D]/([D]+Kd) | At Kd, 50% occupied |
| Agonist | α > 0; produces response | Full (α=1) vs partial (0<α<1) |
| Competitive antagonist | Shifts EC50 right; same Emax | Overcome with more drug |
| Non-competitive antagonist | Reduces Emax | Cannot overcome with more drug |
| Partial agonist in full-agonist presence | Reduces net response | Buprenorphine for opioid addiction |
| Desensitization | Prolonged exposure reduces response | Opioid tolerance, β-agonist tolerance |
| Rebound on stopping antagonist | Receptor upregulation | β-blocker withdrawal |

---

## Common Confusion Points

**"EC50 and Kd — are they the same?"**
Not necessarily. Kd is a thermodynamic constant for drug-receptor binding (occupancy at 50%). EC50 is the concentration producing 50% of maximal effect. If the effect is linearly proportional to occupancy, EC50 = Kd. But receptor-effector coupling can amplify: even 10% receptor occupancy might produce 50% maximal effect (receptor reserve). So EC50 can be much lower than Kd.

**"If a drug is an antagonist, how does it have a therapeutic effect?"**
By blocking the action of an endogenous ligand that is overactive. β-blockers block adrenaline at β-receptors — therapeutic because blocking excessive sympathetic drive reduces heart rate and blood pressure. Antihistamines block histamine — therapeutic in allergic conditions because blocking histamine prevents inflammatory signaling.

**"Inverse agonist vs antagonist — clinical difference?"**
An inverse agonist reduces the activity of constitutively active receptors (active without ligand). An antagonist just blocks binding. For most drug targets, constitutive activity is minimal, so inverse agonists behave like antagonists in practice. Important exceptions: some cancer mutations cause constitutively active receptor tyrosine kinases — inverse agonism there would suppress the mutant signaling.
