# Mathematics & Physics

11 directories · Formal foundations — pure math through quantum, with the applied bridges between them

---

## Landscape

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                           MATHEMATICS & PHYSICS                                     │
└─────────────────────────────────────────────────────────────────────────────────────┘

 PURE MATHEMATICS
 ┌─────────────────┐   ┌───────────────────┐   ┌──────────────────┐
 │  mathematics/   │   │  number-theory/   │   │ abstract-algebra/ │
 │  vector calc    │   │  primes · modular │   │  groups · rings   │
 │  linear algebra │   │  Diophantine      │   │  fields · Galois  │
 │  ODEs · PDEs    │   │  RSA foundations  │   │  representation   │
 │  probability    │   │  analytic NT      │   │  homomorphisms    │
 │  topology primer│   └───────────────────┘   └──────────────────┘
 │  numerical meth │           │                        │
 └────────┬────────┘           └────────────┬───────────┘
          │                                 │
          │                        ┌────────▼────────┐
          │                        │    topology/    │
          │                        │  point-set      │
          │                        │  manifolds      │
          │                        │  homology /     │
          │                        │  cohomology     │
          │                        │  fundamental    │
          │                        │  group          │
          │                        └────────────────-┘
          │
          ▼
 APPLIED MATHEMATICS
 ┌──────────────────────┐   ┌─────────────────────┐   ┌──────────────────┐
 │  signal-processing/  │   │  information-theory/ │   │  control-theory/ │
 │  Fourier/Laplace/z   │   │  entropy · capacity  │   │  transfer fn     │
 │  FFT · filters · DSP │   │  source/channel code │   │  PID · state sp. │
 │  wavelets · Nyquist  │   │  compression · AIT   │   │  Lyapunov        │
 └──────────┬───────────┘   └─────────────────────┘   │  optimal ctrl    │
            │                                          └──────────────────┘
            ▼
 PHYSICAL LAYER
 ┌──────────────────┐   ┌──────────────────┐   ┌─────────────────────┐
 │    physics/      │   │   electronics/   │   │    materials/       │
 │  E&M · Maxwell   │   │  circuits · PCB  │   │  crystal structure  │
 │  mechanics · MHD │   │  op-amps · CMOS  │   │  phase diagrams     │
 │  thermodynamics  │   │  digital logic   │   │  failure modes      │
 │  liquid metals   │   │  power elec.     │   │  mech/thermal/elec  │
 │  quantum intro   │   └──────────────────┘   └─────────────────────┘
 └────────┬─────────┘
          │
          ▼
 QUANTUM LAYER
 ┌──────────────────────────────────────────────────────────┐
 │  quantum-computing/                                      │
 │  qubits · gates · Shor/Grover · error correction        │
 │  hardware platforms (superconducting/photonic/ion trap)  │
 └──────────────────────────────────────────────────────────┘
```

---

## Directories

| Directory | Focus | Entry Point | Bridges to |
|-----------|-------|-------------|------------|
| `mathematics/` | Vector calculus, linear algebra, ODEs/PDEs, probability theory, topology primer, numerical methods (Newton/Runge-Kutta/finite difference) | `01-VECTOR-CALC.md` — grad/div/curl/Stokes/Green | `physics/` for E&M application; `signal-processing/` for Fourier analysis; `control-theory/` for state-space |
| `number-theory/` | Primes, modular arithmetic, Chinese Remainder Theorem, Diophantine equations, RSA/DH/ECC mathematical foundations, analytic number theory (Riemann hypothesis framing) | `01-PRIMES.md` — prime distribution and sieve methods | `abstract-algebra/` for algebraic structures; `cryptography/` (Computing) for application |
| `abstract-algebra/` | Groups, rings, fields, Galois theory, homomorphisms/isomorphisms, representation theory, applications to coding theory | `01-GROUPS.md` — group axioms through Lagrange/Sylow | `number-theory/` for finite fields; `topology/` for algebraic topology; `cryptography/` (Computing) for elliptic curves |
| `topology/` | Point-set topology, metric spaces, compactness/connectedness, manifolds, homology/cohomology, fundamental group, applications to data (TDA) | `01-POINT-SET.md` — open sets through compactness | `mathematics/` for continuity foundations; `abstract-algebra/` for algebraic topology |
| `signal-processing/` | Fourier series/transform, Laplace transform, z-transform, filter design (FIR/IIR), FFT algorithms, DSP, wavelets, Nyquist-Shannon, sampling theory | `01-FOURIER.md` — Fourier series through DFT | `mathematics/` for functional analysis substrate; `physics/` for wave phenomena; `electronics/` for analog filter implementation |
| `information-theory/` | Shannon entropy, mutual information, channel capacity (Shannon-Hartley), source coding (Huffman/LZ), channel coding (Hamming/turbo/LDPC), algorithmic information theory | `01-ENTROPY.md` — entropy through KL divergence | `signal-processing/` for coding channel models; `cryptography/` (Computing) for entropy in key generation |
| `control-theory/` | Transfer functions, Bode plots, PID tuning, state-space representation, controllability/observability, stability (Lyapunov, Routh-Hurwitz), optimal control (LQR/LQG) | `01-TRANSFER-FUNCTIONS.md` — Laplace domain control | `mathematics/` for ODEs; `signal-processing/` for frequency-domain analysis; `robotics/` (Engineering) for implementation |
| `physics/` | Classical E&M (Coulomb through Maxwell equations), mechanics (Lagrangian/Hamiltonian), thermodynamics (laws through stat mech), MHD, liquid metals, quantum mechanics intro | `01-EM-FIELDS.md` — electrostatics through Maxwell | `mathematics/` for PDEs and vector calculus; `electronics/` for circuit-level E&M; `materials/` for condensed matter |
| `electronics/` | Circuit analysis (KVL/KCL/Thevenin), passive/active components, op-amp configurations, digital logic (gates through flip-flops), PCB layout, power electronics | `01-CIRCUIT-FUNDAMENTALS.md` — charge, current, KVL/KCL | `physics/` for electromagnetic substrate; `materials/` for semiconductor physics; `signal-processing/` for analog filter design |
| `materials/` | Crystal structure (Bravais lattices, Miller indices), phase diagrams (lever rule, eutectic), mechanical properties (stress/strain, fatigue, fracture mechanics), thermal/electrical properties | `01-CRYSTAL-STRUCTURE.md` — lattice types through X-ray diffraction | `physics/` for quantum band theory; `electronics/` for semiconductor materials; `chemical-eng/` (Engineering) for materials processing |
| `quantum-computing/` | Qubit models (Bloch sphere), quantum gates and circuits, key algorithms (Shor factoring, Grover search), quantum error correction (stabilizer codes), hardware platforms comparison | `01-QUBITS.md` — superposition, entanglement, measurement | `physics/` for quantum mechanics substrate; `cryptography/` (Computing) for post-quantum motivation; `mathematics/` for linear algebra and group theory |

---

## Paths

### From MIT foundations into applied engineering math
`mathematics/` → `signal-processing/` → `control-theory/`
*The vector calc and ODE machinery from your MIT background plugs directly into the s-domain and state-space formulations — this path makes explicit what those courses were building toward.*

### Cryptographic mathematics
`number-theory/` → `abstract-algebra/` → `cryptography/` (Computing & Software)
*RSA and ECC are group-theoretic constructions over number fields — build the algebraic machinery first, then the cryptographic application is almost immediate.*

### Physics into hardware
`physics/` → `electronics/` → `materials/` → `semiconductor-manufacturing/` (Engineering)
*Maxwell through circuits through solid-state physics through fab — the vertical stack from equations to transistors.*

---

## Adjacent Sections

| Section | The bridge |
|---------|------------|
| Computing & Software | `number-theory/` + `abstract-algebra/` are the mathematical underpinnings of everything in `cryptography/`. `information-theory/` underpins compression, entropy sources for key generation, and conceptually grounds LLM tokenization. `signal-processing/` is directly below audio/image ML pipelines in `ai-engineering/`. |
| Engineering | `signal-processing/` feeds directly into `acoustics/` and `telecommunications/` — the transform tools are shared. `control-theory/` is the mathematical substrate for `robotics/` and industrial process control in `chemical-eng/`. `physics/` and `materials/` underlie the entire physical engineering track. |
| Earth & Space | `physics/` MHD section is the governing framework for solar physics and magnetospheric dynamics in `astronomy/`. Thermodynamics in `physics/` connects to atmospheric dynamics in Earth sciences. |
