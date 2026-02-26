# Biophysics — Landscape and Taxonomy

## The Big Picture

Biophysics applies the tools of physics — thermodynamics, statistical mechanics,
electrostatics, mechanics, optics — to biological systems. It operates at scales
ranging from individual atoms (protein folding, ion channels) to cells (membrane
mechanics) to tissues (collective cell dynamics).

<!-- @editor[diagram/P2]: Landscape diagram categorizes items but doesn't show how subfields feed into each other — consider adding arrows or layering to show that structural methods feed dynamical studies, which inform functional understanding -->
```
┌──────────────────────────────────────────────────────────────────┐
│                    BIOPHYSICS LANDSCAPE                           │
│                                                                    │
│  STRUCTURAL               DYNAMICAL                FUNCTIONAL    │
│  ──────────               ─────────                ──────────    │
│  X-ray crystallography    Molecular motors         Ion channels  │
│  NMR spectroscopy         Cytoskeletal dynamics    Membrane pot. │
│  Cryo-EM                  Protein folding/unfolding Signaling    │
│  SAXS                     Diffusion in membranes   Gene networks │
│                                                                    │
│  SCALE:                                                          │
│  ───────                                                          │
│  Å:       Bond lengths, small molecule binding                   │
│  nm:      Proteins, DNA/RNA, molecular motors                    │
│  100 nm:  Viruses, organelle membranes                           │
│  μm:      Cells, cytoskeleton, vesicles                          │
│  10-100μm: Cell aggregates, tissues                              │
│                                                                    │
│  METHODS:                                                        │
│  ─────────                                                        │
│  Structural:  X-ray, NMR, cryo-EM, SAXS, AFM                    │
│  Single mol.: optical tweezers, magnetic tweezers, FRET, TIRF    │
│  Electrophys.: patch clamp, MEA, voltage clamp                   │
│  Computational: MD simulation, coarse-grained models, AlphaFold  │
└──────────────────────────────────────────────────────────────────┘
```

---

## The Physical Framework for Biology

Life operates under two apparent paradoxes:
1. Life is highly ordered but exists in thermal equilibrium with its environment
2. Life harnesses free energy to do work, but cannot violate thermodynamics

Resolution:
- Life is a far-from-equilibrium thermodynamic system maintained by continuous free
  energy input (chemical energy from food, light from the sun)
- Order is not free: it costs free energy to maintain
- Entropy is not the enemy: biological machines convert chemical free energy into
  work by allowing entropy to increase elsewhere (coupling)

---

## Field Taxonomy

```
┌─────────────────────────────────────────────────────────────────┐
│                      BIOPHYSICS                                  │
├──────────────────┬──────────────────┬────────────────────────── ┤
│  STRUCTURAL       │  SINGLE MOLECULE  │  CELLULAR                 │
│  BIOPHYSICS       │  BIOPHYSICS       │  BIOPHYSICS               │
│                  │                   │                           │
│  Protein folding  │  Optical tweezers │  Membrane biophysics      │
│  Cryo-EM         │  Magnetic tweezers│  Ion channel gating       │
│  X-ray crystal.  │  AFM              │  Hodgkin-Huxley            │
│  NMR             │  FRET             │  Action potentials         │
│  AlphaFold       │  TIRF microscopy  │  Cytoskeletal mechanics   │
├──────────────────┼──────────────────┼───────────────────────────┤
│  STATISTICAL      │  MOLECULAR        │  COMPUTATIONAL            │
│  BIOPHYSICS       │  MOTORS           │  BIOPHYSICS               │
│                  │                   │                           │
│  Fluctuation-     │  Kinesin          │  MD simulation            │
│  dissipation      │  Myosin           │  Coarse-grained           │
│  Jarzynski eq.   │  ATP synthase     │  Stochastic modeling      │
│  Langevin eq.    │  Polymerases      │  Neural network models    │
│  Free energy calc │  Brownian ratchet │  Systems biology          │
└──────────────────┴──────────────────┴───────────────────────────┘
```

---

## Unifying Physical Concepts

### 1. Thermal Energy
At T = 310 K (body temperature): k_B T ≈ 4.1 pN·nm = 4.1 × 10⁻²¹ J = 0.6 kcal/mol

This is the fundamental energy unit of biophysics. It determines:
- Spontaneous fluctuations in molecular conformations
- Diffusion rates (D = k_B T / (6πηr) by Stokes-Einstein)
- Bond stability (bonds with ΔG >> k_B T are stable; bonds with ΔG ≈ k_B T fluctuate)

### 2. Electrostatics in Water
Coulomb force is screened by water's high dielectric constant (ε = 80) and by
dissolved ions (Debye-Hückel screening):

```
  Electrostatic potential: V(r) = q / (4πε₀εr) × exp(-r/λ_D)

  Debye length λ_D = sqrt(ε₀ε k_B T / (2 × e² × I))

  I = ionic strength = Σ(cᵢ × zᵢ²) / 2

  Physiological salt (150 mM NaCl, I = 150 mM):  λ_D ≈ 0.8 nm
  → Electrostatic interactions are screened beyond ~1 nm in cells
  → Long-range electrostatics matter for charged surfaces (membranes)
    but not for soluble protein-protein interactions (which are mostly short-range)
```

### 3. Stochastic Dynamics
Biological systems at the nanoscale are fundamentally stochastic. The Langevin equation
describes a particle subject to both a deterministic force and thermal noise:

```
  m·ẍ = F_det(x) - γ·ẋ + ξ(t)

  γ = friction coefficient (Stokes: γ = 6πηr)
  ξ(t) = Gaussian white noise with ⟨ξ(t)ξ(t')⟩ = 2γk_BT·δ(t-t')

  In overdamped limit (inertia negligible — always valid at nanoscale):
  γ·ẋ = F_det(x) + ξ(t)

  Diffusion coefficient D = k_B T / γ (Einstein relation)
```

---

## Module Map

| File | Core question |
|------|---------------|
| 01-THERMODYNAMICS-BIO.md | How do thermodynamic principles apply to biomolecules? |
| 02-PROTEIN-FOLDING.md | How do proteins fold? What did AlphaFold solve? |
| 03-STRUCTURAL-METHODS.md | How do we determine molecular structures? |
| 04-MEMBRANE-BIOPHYSICS.md | What are the physics of lipid bilayers and ion channels? |
| 05-HODGKIN-HUXLEY.md | How does the action potential arise from ion conductances? |
| 06-MOLECULAR-MOTORS.md | How do molecular motors work as Brownian ratchets? |
| 07-SINGLE-MOLECULE.md | What can single-molecule experiments tell us? |
| 08-STOCHASTIC-BIO.md | How do stochastic processes shape biological systems? |
| 09-ALPHAFOLD-ERA.md | What did AlphaFold actually solve — and not solve? |

---

## Scale and Energy Reference Table

| Scale | Entity | Energy scale |
|-------|--------|-------------|
| 0.1 nm | Bond length | Single bond: ~80 kcal/mol (350 kJ/mol) |
| 0.3 nm | Water molecule | Hydrogen bond: ~5 kcal/mol |
| 1-5 nm | Small protein domain | Folding ΔG: ~5-15 kcal/mol |
| 10-100 nm | Large protein complex | ATP hydrolysis: ~12 kcal/mol (in cell) |
| 8 nm | Kinesin step | Kinesin does ~8 pN·nm work = 2 k_BT per step |
| 0.1 μm | Virus | Action potential: ~70 mV × charge |
| 1-100 μm | Cell | Cell mechanics: ~1 nN forces, kPa stiffness |

---

## Connections to Other Reference Directories

| Biophysics concept | Where else it appears |
|-------------------|----------------------|
| Protein structure | genomics/ (structural genomics), medicine/ (drugs) |
| Ion channels / electrophysiology | neuroscience/ (neurons), medicine/ (cardiology) |
| Thermodynamics | chemistry block (natural-sciences/) |
| Statistical mechanics | statistical-mechanics/ (physics) |
| Stochastic processes | probability-statistics/ |
| AlphaFold | ai-engineering/ (LLM-CONCEPTS bridges) |
| Membrane biophysics | biology/ (cell membranes) |
| Molecular motors | cell-biology (natural-sciences/) |

---

<!-- @editor[bridge/P2]: No old-world bridge in this overview — a brief bridge from classical physics/engineering (e.g., circuit theory to ion channels, continuum mechanics to membrane elasticity, signal processing to noise analysis) would orient the learner across the whole catalog -->
## Decision Cheat Sheet

| Question | Biophysics framework | Module |
|----------|---------------------|--------|
| How does a protein fold spontaneously? | Energy landscape theory | 01, 02 |
| How was the ribosome structure determined? | Cryo-EM | 03 |
| How does a neuron fire an action potential? | Hodgkin-Huxley | 05 |
| How does kinesin walk on microtubules? | Brownian ratchet | 06 |
| Can I measure single-molecule force? | Optical tweezers | 07 |
| Is a biochemical process at equilibrium? | Fluctuation-dissipation | 01, 08 |
| What was left unsolved after AlphaFold? | Function, dynamics, design | 09 |

---

## Common Confusion Points

**Biophysics is not the same as biochemistry.** Biochemistry focuses on chemical
reactions and molecular mechanisms. Biophysics focuses on physical principles:
forces, energies, dynamics, and information. A biochemist asks "what reacts with
what"; a biophysicist asks "what forces and energies determine the outcome."

**Equilibrium thermodynamics applies only when systems are at equilibrium.** Many
biological processes are explicitly non-equilibrium (motors, signaling, gene expression).
Using equilibrium thermodynamics for non-equilibrium biology gives wrong answers.
The Jarzynski equality provides the bridge between equilibrium free energies and
non-equilibrium work measurements.

**Diffusion is fast enough.** Cytoplasm appears "crowded" but diffusion of small
molecules across a cell (~10 μm) takes only ~10-100 ms. Large protein complexes
are slower, but most intracellular signaling is diffusion-limited, not reaction-
rate-limited. Active transport (motor proteins) is needed for longer distances
and directed delivery (axonal transport in neurons: meters away from cell body).
