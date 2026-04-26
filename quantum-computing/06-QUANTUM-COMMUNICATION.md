# Quantum Communication and QKD

## Big Picture: Quantum vs Classical Security

```
┌─────────────────────────────────────────────────────────────────────┐
│              QUANTUM KEY DISTRIBUTION — PROTOCOL FAMILY             │
│                                                                     │
│  PREPARE-AND-MEASURE              ENTANGLEMENT-BASED                │
│  ┌──────────────────────────┐     ┌────────────────────────────┐    │
│  │  BB84 (1984)             │     │  E91 / Ekert (1991)        │   │
│  │  Alice prepares qubits   │     │  Source emits entangled     │   │
│  │  in 2 conjugate bases    │     │  pairs to Alice + Bob      │   │
│  │  Bob measures randomly   │     │  Bell inequality violation  │   │
│  │                          │     │  = security certificate    │   │
│  │  Security: info-disturbance     │  Security: device-        │   │
│  │  tradeoff                │     │  independent possible      │   │
│  └──────────────────────────┘     └────────────────────────────┘   │
│                                                                     │
│  B92 (1992): 2 non-orthogonal states — simpler but lower rate      │
│                                                                     │
│  NETWORK LAYERS:                                                    │
│  Physical ──► Entanglement ──► Network ──► Application             │
│  (photons)   (Bell pairs)    (routing)   (QKD/teleport/sensing)    │
└─────────────────────────────────────────────────────────────────────┘

  Security model: INFORMATION-THEORETIC (unconditional)
  No assumption on Eve's computational power — security from physics
  Contrast: RSA/ECC assumes computational hardness (broken by Shor)
```

---

## BB84 Protocol — Full Detail

### Qubit Encoding

```
TWO CONJUGATE BASES:

  Rectilinear (Z) basis: |0⟩ = ↕  (vertical)    |1⟩ = ─ (horizontal)
  Diagonal (X) basis:    |+⟩ = ↗  (45°)          |−⟩ = ↘ (135°)

  |+⟩ = (|0⟩ + |1⟩)/√2     |−⟩ = (|0⟩ − |1⟩)/√2

  COMPLEMENTARITY: Measuring |+⟩ in Z basis → 50/50 outcome (random)
                   Measuring |0⟩ in X basis → 50/50 outcome (random)
  → Measuring in wrong basis destroys information and introduces errors
```

### Protocol Steps

```
STEP 1: QUBIT TRANSMISSION
  Alice generates random bits b ∈ {0,1} and bases B_A ∈ {Z, X}
  She sends qubit in state:
    B_A=Z, b=0 → |0⟩    B_A=Z, b=1 → |1⟩
    B_A=X, b=0 → |+⟩    B_A=X, b=1 → |−⟩

STEP 2: BOB MEASURES
  Bob chooses random basis B_B ∈ {Z, X}
  If B_B = B_A: Bob gets Alice's bit deterministically
  If B_B ≠ B_A: Bob gets random outcome (50% error)

STEP 3: BASIS RECONCILIATION (public classical channel)
  Alice and Bob announce their bases (NOT the bits)
  Keep only positions where B_A = B_B → raw key (~50% of transmissions)

STEP 4: ERROR RATE ESTIMATION (QBER)
  Sacrifice a random subset of raw key bits
  Announce them publicly, compute QBER = (# errors) / (# compared bits)
  If QBER > 11%: ABORT (eavesdropping detected)
  If QBER ≤ 11%: proceed

STEP 5: INFORMATION RECONCILIATION (error correction over classical channel)
  Fix remaining errors using e.g. Cascade protocol
  Leaks some information to Eve

STEP 6: PRIVACY AMPLIFICATION
  Hash the corrected key to shorter key
  Amount to hash = f(QBER, leaked info in reconciliation)
  Result: final secure key that Eve has negligible information about
```

### Eavesdropping Detection

```
EVE'S INTERCEPT-RESEND ATTACK:
  Eve intercepts each qubit, measures in random basis, resends

  When Eve chooses wrong basis (50% of the time):
    She sends wrong state → Bob gets error when bases match

  Error introduced per bit (bases match, Eve attacks):
    P(Eve wrong basis) × P(wrong result) = 0.5 × 0.5 = 0.25

  QBER introduced by intercept-resend = 25%  >> 11% threshold
  → Attack is ALWAYS detected if Eve intercepts all qubits

  PARTIAL INTERCEPT: Eve intercepts fraction ε
    QBER = ε × 0.25 → detectable for any ε above noise floor
```

### Security Proof Sketch

The formal security proof uses the **information-disturbance tradeoff**:

```
MAYERS (1996) / LO-CHAU (1999) / SHOR-PRESKILL (2000):

Any attack by Eve can be decomposed into:
  1. Attaching ancilla |E⟩ to each qubit
  2. Applying joint unitary U_E
  3. Storing her ancilla for later measurement

Key insight: CSS codes + random hashing

If we used CSS code to encode classical bits as quantum states,
error correction + privacy amplification is equivalent to
quantum error correction on CSS code.

The X-basis error rate (phase errors) bounds information leaked to Eve.
Privacy amplification removes this information: compress by
  ℓ = n - leak_reconciliation - n·h(δ_phase)
where h is binary entropy, δ_phase is phase error rate.

COMPOSABLE SECURITY (Renner 2008):
  Security parameter: ε-secure means Eve's state is ε-close
  to tensor product with uniform key (trace distance ≤ ε)
  This composes: key is safe to use in AES, OTP, etc.
```

---

## E91 — Entanglement-Based QKD

### Bell State and CHSH

```
ENTANGLED SOURCE:
  |Φ⁺⟩ = (|00⟩ + |11⟩)/√2  (Bell state)

  Alice and Bob each receive one qubit
  Each measures in randomly chosen basis from set {0°, 45°, 90°} (Alice)
                                              and {45°, 90°, 135°} (Bob)

KEY GENERATION:
  When both choose basis 45°: outcomes perfectly correlated → raw key
  When both choose basis 90°: outcomes perfectly correlated → raw key

SECURITY TEST (CHSH inequality):
  E(a, b) = P(same result | bases a, b) - P(different result | bases a, b)

  S = E(0°,45°) - E(0°,135°) + E(90°,45°) + E(90°,135°)

  CLASSICAL: |S| ≤ 2  (Bell-CHSH bound for local hidden variables)
  QUANTUM:    S = 2√2 ≈ 2.83  (Tsirelson bound, achieved by |Φ⁺⟩)

  If Eve tampers with entanglement → S decreases toward 2
  Full Bell inequality violation = no eavesdropping
```

### Device-Independent QKD

The E91 paradigm extends to **device-independent QKD (DI-QKD)**:
- Security proof requires ONLY that Bell inequality is violated
- No need to trust the quantum devices themselves (could be manufactured by Eve)
- Bell violation certifies entanglement and hence security
- Implementation: requires loophole-free Bell test (detection efficiency > ~82%)

---

## B92 Protocol (Bennett 1992)

```
SIMPLIFICATION: Only 2 non-orthogonal states

Alice sends: bit 0 → |0⟩,  bit 1 → |+⟩

Bob measures: bit 0 → in X basis,  bit 1 → in Z basis

KEY INSIGHT: Non-orthogonal states cannot be perfectly distinguished
  If Bob measures |0⟩ in X basis:  gets |+⟩ → inconclusive
                                    gets |−⟩ → conclusive: Alice sent |0⟩
  If Bob measures |+⟩ in Z basis:  gets |0⟩ → inconclusive
                                    gets |1⟩ → conclusive: Alice sent |+⟩

Key rate lower than BB84 (~25% vs ~50% of transmitted qubits)
Simpler implementation: only 2 states needed
Less used in practice (lower key rate)
```

---

## Practical QKD Implementation

### Physical Layer

```
PHOTON SOURCES:
  Ideal: single-photon source (on-demand)
  Practical: attenuated laser pulses (coherent states)
    Problem: Poisson photon number distribution
    Multi-photon pulses → PNS (photon number splitting) attack by Eve

  DECOY STATE METHOD (Hwang/Lo-Ma-Chen 2005):
    Send pulses with random intensities (signal + decoy + vacuum)
    Statistical analysis of detection rates for each intensity
    Bounds Eve's information even with imperfect single-photon source
    → Enables secure QKD with practical laser sources

DETECTORS:
  InGaAs avalanche photodiodes: ~10% efficiency, ~10⁻⁵ dark count rate
  Superconducting nanowire (SNSPD): >90% efficiency, <1 dark count/s
    → SNSPD enables much higher key rates and longer distances

CHANNEL LOSSES:
  Telecom fiber: ~0.2 dB/km at 1550 nm
  100 km: 20 dB = 1/100 transmission
  Key rate drops linearly with channel transmission (for fixed detector)
  Practical fiber QKD: ≤ 400 km with extremely low noise + SNSPD
```

### Distance Limits and Repeaters

```
FUNDAMENTAL LIMIT WITHOUT REPEATERS:
  PLOB bound (Pirandola-Laurenza-Ottaviani-Banchi):
  Key rate ≤ -log₂(1 - η)  bits per channel use
  where η = transmission = 10^{-αL/10}
  → Key rate drops exponentially with distance

QUANTUM REPEATER CONCEPT:
  ┌───────┐  entanglement  ┌────────┐  entanglement  ┌───────┐
  │ Alice │◄──────────────►│ Repeat.│◄──────────────►│  Bob  │
  └───────┘                └────────┘                └───────┘
                             performs
                           entanglement
                             swapping

  Entanglement swapping: if A-R and R-B are entangled,
    measure R in Bell basis → projects A-B into entangled state
    (teleports entanglement through R without R seeing the qubit)

REPEATER GENERATIONS:
  Gen 1: Entanglement swapping + classical error correction
         Need quantum memory (store Bell pairs while waiting for heralding)
  Gen 2: + entanglement purification (distill high-fidelity pairs from noisy ones)
  Gen 3: Full quantum error correction at each node
         → Only Gen 3 beats PLOB bound unconditionally
```

### Satellite QKD (Micius)

```
CHINESE MICIUS SATELLITE (2017):
  LEO orbit (~500 km altitude)
  Downlink: satellite sends entangled pairs / BB84 qubits to ground
  Loss: ~40 dB (vs ~200 dB for equivalent ground fiber)
  Achievement: QKD over 1200 km ground separation (via satellite relay)
  Key rate: ~kbps (much lower than fiber at short range)

FREE-SPACE QKD:
  Low atmosphere loss (<1 dB/km in clear conditions)
  Requires pointing/tracking, adaptive optics for turbulence
  Daytime operation difficult (background photons)
  Applications: ground-to-drone, ground-to-satellite, building-to-building
```

---

## Quantum Internet Architecture

```
LAYERS (analogous to classical networking):

┌──────────────────────────────────────────────────────────────────────┐
│ LAYER 4: APPLICATION                                                 │
│   QKD, blind quantum computing, quantum sensing, clock sync          │
├──────────────────────────────────────────────────────────────────────┤
│ LAYER 3: NETWORK                                                     │
│   Quantum routing, multiplexing, resource management                 │
│   (active research — no standard protocol yet)                       │
├──────────────────────────────────────────────────────────────────────┤
│ LAYER 2: ENTANGLEMENT                                                │
│   Create, store, purify Bell pairs; entanglement swapping            │
│   Requires: quantum memory (ms to s coherence), heralded generation  │
├──────────────────────────────────────────────────────────────────────┤
│ LAYER 1: PHYSICAL                                                    │
│   Photon transmission (telecom fiber 1550 nm, free space)            │
│   Bell state measurements at repeater nodes                          │
│   Single-photon detectors (SNSPD)                                    │
└──────────────────────────────────────────────────────────────────────┘

STATUS (2025):
  Layer 1: Commercial (ID Quantique, Toshiba, MagiQ offer QKD systems)
  Layer 2: Lab demonstrations (Delft, Harvard, MIT Lincoln Lab)
  Layer 3-4: Research phase; no deployed quantum repeater networks
```

---

## Decision Cheat Sheet

```
┌──────────────────────────────────────────────────────────────────────┐
│ SCENARIO                     │ RECOMMENDATION                        │
├──────────────────────────────┼───────────────────────────────────────┤
│ Need information-theoretic   │ QKD (BB84 with decoy states in       │
│ security for key exchange    │ practice); requires authenticated    │
│                              │ classical channel                    │
├──────────────────────────────┼───────────────────────────────────────┤
│ Distance < 100 km, fiber     │ BB84 with attenuated laser + decoy;   │
│                              │ commercial systems available          │
├──────────────────────────────┼───────────────────────────────────────┤
│ Distance 100-400 km          │ BB84 with SNSPD + trusted repeater  │
│                              │ nodes (security degrades at nodes)   │
├──────────────────────────────┼───────────────────────────────────────┤
│ Distance > 400 km            │ Satellite relay (Micius-style) or     │
│                              │ wait for quantum repeaters (Gen 3)    │
├──────────────────────────────┼───────────────────────────────────────┤
│ Distrust devices             │ DI-QKD based on E91/Bell violation;  │
│ (untrusted manufacturer)     │ requires loophole-free Bell test     │
├──────────────────────────────┼───────────────────────────────────────┤
│ QBER > 11% observed          │ Abort — either eavesdropping or       │
│                              │ channel too noisy for secure QKD      │
├──────────────────────────────┼───────────────────────────────────────┤
│ Post-quantum security for    │ Use ML-KEM (Kyber) / ML-DSA (Dilith.)│
│ classical data                │ Shor-resistant, deployable now      │
└──────────────────────────────┴───────────────────────────────────────┘
```

---

## Common Confusion Points

**QKD ≠ quantum computing.** QKD is about key distribution using quantum channel properties (no-cloning, measurement disturbance). It does not require a quantum computer. A QKD system is closer to an optical communications device than a quantum processor.

**BB84 security requires an authenticated classical channel.** Without authentication, BB84 is vulnerable to a man-in-the-middle attack: Eve intercepts everything, runs BB84 with Alice pretending to be Bob, and BB84 with Bob pretending to be Alice. Authentication requires information-theoretically secure MACs (Wegman-Carter universal hashing over a short pre-shared secret), not the computational MACs (HMAC-SHA256) used in standard TLS. This is because BB84's unconditional security guarantee would be undermined by a computationally-secure MAC that a quantum adversary could break. The pre-shared secret is consumed but the QKD session generates enough new key material to replenish it — a key-growing protocol.

**QKD does not replace TLS for most applications.** QKD distributes symmetric keys. You still need authentication, key management, and a classical communication protocol. For most applications, post-quantum classical cryptography (ML-KEM) is sufficient and far cheaper. QKD is for adversaries with long-term quantum capability and extremely high-value information.

### QKD vs Post-Quantum Cryptography — Infrastructure Decision

```
┌──────────────────────┬────────────────────────────┬────────────────────────────┐
│ DIMENSION            │ QKD (BB84/E91)             │ PQC (ML-KEM, ML-DSA)       │
├──────────────────────┼────────────────────────────┼────────────────────────────┤
│ Security basis       │ Physics (info-theoretic)    │ Math (computational)       │
│ Quantum-safe?        │ Yes — by definition         │ Yes — believed hard for QC │
│ Deployment cost      │ $50K–$500K per link         │ Software update            │
│ Range                │ ≤400 km fiber; satellite    │ Global (internet)          │
│ Topology             │ Point-to-point only         │ Any (mesh, CDN, cloud)     │
│ Key rate             │ ~kbps–Mbps (distance-dep)   │ Unlimited (CPU-bound)      │
│ Needs new hardware?  │ Yes — photon sources, SNSPD │ No — software/firmware     │
│ Standards            │ ETSI QKD ISG (limited)      │ NIST FIPS 203/204/205      │
│ Integration          │ Dedicated fiber or free-    │ Drop-in TLS 1.3 upgrade    │
│                      │ space optical link          │ (X25519Kyber768 deployed)  │
│ Authentication       │ Requires pre-shared secret  │ Standard PKI               │
│ Maturity             │ Commercial (limited vendors)│ Shipping (Chrome, CF, AWS) │
└──────────────────────┴────────────────────────────┴────────────────────────────┘

WHEN QKD MAKES SENSE:
  1. Information-theoretic security REQUIRED (not just computational)
  2. Point-to-point link with dedicated fiber already available
  3. Adversary has nation-state quantum capability AND targets your data specifically
  4. Data lifetime exceeds confidence horizon of lattice-based PQC (decades)
  Examples: diplomatic communications, nuclear command/control, central bank reserves

WHEN PQC IS THE RIGHT ANSWER (vast majority of enterprise):
  1. Standard TLS/VPN traffic — upgrade to ML-KEM hybrid
  2. Any topology beyond point-to-point (CDN, mesh, cloud)
  3. Cost matters (it always does)
  4. Need to protect data in transit AND at rest
```

**Entanglement swapping does not transmit information.** When a repeater performs entanglement swapping between Alice-Repeater and Repeater-Bob pairs, Alice and Bob become entangled — but the correlation only becomes useful once Alice and Bob communicate classically which Bell measurement outcome the repeater got. No faster-than-light signaling.

**Device-independent QKD is theoretically powerful but practically very hard.** It requires a loophole-free Bell test, meaning detection efficiency > ~82%. With current detectors and distances, achieving this requires extraordinary experimental conditions. DI-QKD remains a research goal as of 2025.

**QBER threshold of 11% is not universal.** The 11% threshold is for intercept-resend attacks on BB84. More sophisticated attacks (coherent attacks) are covered by composable security proofs, which require lower QBER for the same security parameter. In practice, systems target QBER < 5-6%.
