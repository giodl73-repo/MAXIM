# Network Information Theory

```
FROM POINT-TO-POINT TO NETWORKS

Single link (Shannon):         X ──[Channel]──> Y     C = max I(X;Y)  SOLVED

Network primitives:
  MAC  (many → one):   X₁ ─┐
                            ├──[Channel]──> Y
                       X₂ ─┘
  BC   (one → many):        ┌──> Y₁
                   X ──────┤
                            └──> Y₂
  IC   (two pairs):   X₁ ──> Y₁ (+ interference from X₂)
                      X₂ ──> Y₂ (+ interference from X₁)
  Relay:             X ──[Channel]──> Z (relay) ──> Y
                      └──────────────────────────> Y

Solved: MAC (1970s), degraded BC, degraded relay
Open: general IC capacity region (decades-old open problem)
```

---

## 1. Multiple Access Channel (MAC)

Two independent senders, one receiver.

```
X₁ ~ p(x₁)  ─────────────────────────────┐
                                           ├──> p(y|x₁,x₂) ──> Y ──> [Decoder] ──> (M₁, M₂)
X₂ ~ p(x₂)  ─────────────────────────────┘

Capacity region: set of (R₁, R₂) simultaneously achievable

Constraints:
  R₁       ≤ I(X₁; Y | X₂)          ← X₁ alone vs Y, X₂ known
  R₂       ≤ I(X₂; Y | X₁)          ← X₂ alone vs Y, X₁ known
  R₁ + R₂  ≤ I(X₁,X₂; Y)            ← sum rate constraint

    R₂
    │  ●─────────────────●
    │   \                │
    │    \   Capacity    │
    │     \   region     │
    │      \  (pentagon) │
    │       \            │
    │        ●───────────● ──────── R₁
    │
    Sum capacity: I(X₁X₂;Y) = I(X₁;Y) + I(X₂;Y|X₁)
```

**Achievability**: Random coding + joint typicality decoding. Each user encodes at rate Rᵢ.
Decoder finds unique (m₁,m₂) jointly typical with received Y. Error → 0 iff interior of
capacity region.

**Successive Interference Cancellation (SIC)**: Decode X₂ first (treating X₁ as noise),
then subtract X₂ and decode X₁. Achieves the corner point (I(X₁;Y|X₂), I(X₂;Y)).
Reverse order achieves the other corner. Time-sharing achieves the full capacity region boundary.

**Why TDMA is suboptimal**:
```
TDMA: X₁ transmits fraction α, X₂ transmits (1-α)
  R₁ = α·I(X₁;Y),  R₂ = (1-α)·I(X₂;Y)
  Max sum = max{I(X₁;Y), I(X₂;Y)}  (convex combination)

MAC with SIC: R₁ + R₂ = I(X₁X₂;Y) ≥ max{I(X₁;Y), I(X₂;Y)}

The gap: TDMA wastes the time the other user is silent.
MAC uses the full channel simultaneously — multiuser gain.
```

**Gaussian MAC**: X₁ ~ N(0,P₁), X₂ ~ N(0,P₂), Y = X₁ + X₂ + Z, Z ~ N(0,N₀)
```
  R₁ + R₂ ≤ ½ log(1 + (P₁+P₂)/N₀)    (sum capacity)
  R₁      ≤ ½ log(1 + P₁/N₀)
  R₂      ≤ ½ log(1 + P₂/N₀)
```
SIC achieves sum capacity: decode weaker user first, subtract, decode stronger user.

---

## 2. Broadcast Channel (BC)

One sender, two receivers with different channel quality.

```
                        ┌──> p(y₁|x) ──> Y₁ ──> [Dec₁] ──> M₁
X ~ p(x)  ──[Channel]──┤
                        └──> p(y₂|x) ──> Y₂ ──> [Dec₂] ──> M₂
```

**Degraded BC** (Y₂ is a degraded version of Y₁: X → Y₁ → Y₂ Markov chain):

**Superposition coding** (Cover 1972): Encode M₂ (for weak receiver) at cloud layer, encode M₁
(for strong receiver) at satellite layer on top of cloud.

```
X = f(X_cloud, X_satellite)    cloud and satellite codewords

Strong receiver Y₁: decode both layers → gets M₁ (and M₂)
Weak receiver Y₂:   decode only cloud → gets M₂

Capacity region (degraded BC):
  R₁ ≤ I(X_s; Y₁ | X_c)      (satellite rate to Y₁)
  R₂ ≤ I(X_c; Y₂)             (cloud rate to Y₂)
  for some p(x_c)p(x_s|x_c) with X = g(X_c, X_s)
```

**Non-degraded BC and Dirty Paper Coding (DPC)**:
For non-degraded BC (interference known at transmitter), Costa (1983) showed:
capacity of AWGN channel with additive interference S known non-causally at transmitter
equals the interference-free capacity. The encoder pre-cancels S at zero cost.

```
DPC capacity = capacity without S (interference is free if known at TX)

Y = X + S + Z,  S known at TX (not at RX)
C = max_{p(x): E[X²]≤P} I(X; Y) = ½ log(1 + P/N)   [same as S=0 channel]
```

**Gaussian BC via DPC = MIMO downlink**: The capacity of the MIMO broadcast channel
(base station to multiple users) equals the capacity of the dual MIMO MAC via DPC.
This is the fundamental result for cellular downlink design.

---

## 3. Relay Channel

Sender X → Relay Z + direct link → Receiver Y.

```
X ─────────────────────────────────────────────> [Dec] ─> M
│                                                 ↑
└──> p(y_R,y|x) ──> Y_R ──> [Relay Z] ──> Z ───┘

Relay strategies:

  ┌─────────────────────────────────────────────────────────┐
  │  Decode-and-Forward (DF):                               │
  │    Relay fully decodes M, re-encodes, forwards          │
  │    Rate ≤ min{I(X;Y_R), I(X,Z;Y)}                       │
  │    Best when: relay closer to source than destination   │
  │                                                         │
  │  Compress-and-Forward (CF):                             │
  │    Relay compresses Y_R, forwards compressed version    │
  │    Applies Wyner-Ziv coding (Y at destination is SI)    │
  │    Rate ≤ I(X; Y, Y̌_R) - I(Y_R; Y̌_R | X, Y)          │
  │    Best when: relay closer to destination               │
  │                                                         │
  │  Amplify-and-Forward (AF):                              │
  │    Relay scales and forwards (analog)                   │
  │    No decoding; noise amplified too                     │
  │    SNR_eff = (SNR_SR · SNR_RD) / (SNR_SR + SNR_RD + 1)  │
  │    Best for: low complexity, full-duplex systems        │
  └─────────────────────────────────────────────────────────┘
```

**Degraded relay channel capacity** (Cover-El Gamal 1979): When X → Y_R → Y (degraded),
decode-and-forward is capacity-achieving.

**Cut-set bound**: Upper bound for all relay strategies:
C ≤ min over all cuts S containing source of I(X_S; Y_{S^c} | X_{S^c})

---

## 4. Interference Channel

Two independent transmitter-receiver pairs sharing a medium.

```
X₁ ──────────────────────────────────> Y₁  (wants M₁)
  └────[cross interference]──────────> Y₂
X₂ ──────────────────────────────────> Y₂  (wants M₂)
  └────[cross interference]──────────> Y₁
```

**Why this is hard**: Neither receiver can subtract interference (it's private to the other TX).
Capacity region of the general IC is an OPEN PROBLEM (> 50 years unsolved).

**Special cases with known capacity**:

| Regime | Condition | Capacity | Strategy |
|--------|-----------|----------|----------|
| Strong IC | Each RX decodes both TXs | C = MAC capacity (ignore interference) | Treat as MAC, decode both |
| Very strong IC | I(X₁;Y₁\|X₂) ≥ I(X₁;Y₂) etc. | Full single-user rates | Each pair ignores interference |
| Weak IC | Interference is negligible | Treat as two independent channels | Treat interference as noise (TIN) |
| Z-channel | One-sided interference | Known (El Gamal-Costa) | Precoding |

**Han-Kobayashi scheme**: Split each message into public (decoded by both) and private (decoded
by own receiver only). Best known achievable region. Chong-Motani-Garg (2008) showed HK is
within 1 bit of capacity for Gaussian IC — the best known result.

**1-bit gap result**: For the two-user Gaussian IC, HK achieves within 1 bit/dim/user of
capacity. The gap matters at high SNR but is bounded — interference channels have
"approximately" known capacity.

---

## 5. MIMO Capacity

Multiple antennas create parallel spatial channels.

```
TX (nT antennas) ──[H + noise]──> RX (nR antennas)

Y = Hx + Z,   H ∈ ℝ^{nR × nT},  Z ~ N(0, N₀I)

SVD: H = UΣVᴴ  →  r = min(nT, nR) parallel channels with gains σᵢ

Capacity with total power P:
  C = Σᵢ log(1 + Pᵢσᵢ²/N₀)

  where Pᵢ solves waterfilling:  Pᵢ = (μ - N₀/σᵢ²)⁺,  Σ Pᵢ = P

┌──────────────────────────────────────────────────────────────┐
│  Waterfilling across singular values:                        │
│                                                              │
│     μ ─────────────────────────────── water level            │
│         ┌───┐   ┌───┐                                        │
│         │P₁ │   │P₂ │                                       │
│   σᵢ² ──┼───┼───┼───┼──────────────── noise floor N₀/σᵢ²  │
│         │   │   │   │   ┌───┐   ┌───┐                     │
│         │   │   │   │   │ 0 │   │ 0 │  ← silent channels   │
│         └───┘   └───┘   └───┘   └───┘                      │
│          i=1     i=2     i=3     i=4                        │
└──────────────────────────────────────────────────────────────┘

MIMO = r parallel AWGN channels; gains from SVD; power from waterfilling
```

**Channel unknown at TX (no CSIT)**: Equal power allocation, capacity = Σᵢ log(1 + P/(nT·N₀)·σᵢ²).
**Ergodic capacity** (fast fading): E_H[C(H)] — ergodic theorem applies.
**Outage capacity** (slow fading): P(C(H) < R) ≤ ε — probabilistic guarantee.

---

## 6. Network Coding

Move from routing to coding over networks. Fundamental insight: intermediate nodes can
XOR (or more generally linearly combine) packets — not just copy and forward.

```
Butterfly network:            s
                            /   \
   (unicast wouldn't work) a     b
                            \  X /       ← node mixes a and b
                              c
                            / | \
                           d  e  f
                          (d wants s, e wants s, f wants s)

Linear network coding achieves min-cut capacity for multicast.
```

**Max-flow min-cut for networks** (Ahlswede-Cai-Li-Yeung 2000):
For multicast (one source, multiple sinks), the achievable rate to each sink equals
the max-flow (min-cut) from source to that sink. This requires network coding — routing alone
may be insufficient.

**Algebraic framework**: Assign transfer matrices. Source sends x ∈ 𝔽_q^k. Each edge carries
linear combination of source symbols. Each sink receives H_i·x where H_i is the transfer matrix
to sink i. Capacity achieved iff transfer matrices have full rank.

**Random linear network coding**: Each node independently picks random coefficients from 𝔽_q.
With probability ≥ 1 - k²/q, achieves capacity. For q = 2^8 (byte), success probability > 99%.

---

## 7. Key Theorems and Open Problems

```
┌────────────────────────────────────────────────────────────────────┐
│ SOLVED                              OPEN                           │
├────────────────────────────────────────────────────────────────────┤
│ MAC capacity region                 General BC capacity (non-degrad)│
│ Degraded BC capacity                General IC capacity region      │
│ Gaussian BC capacity (via DPC)      Gaussian IC beyond 1-bit gap   │
│ Degraded relay capacity             General relay capacity         │
│ MIMO point-to-point (waterfilling)  Interference networks          │
│ Multicast min-cut via net coding    Distributed source coding      │
│ Wyner-Ziv source coding             Secrecy capacity (generally)   │
│ MAC with common message             Compute-and-forward capacity    │
└────────────────────────────────────────────────────────────────────┘
```

**Wyner-Ziv source coding**: Lossy compression of X when decoder has correlated side info Y.
Rate-distortion function = R(D|Y) = min I(X;X̂|Y) — side information reduces required rate.
Used in video coding (B-frames know neighboring frames) and CF relay strategy.

---

## Decision Cheat Sheet

| Scenario | Setup | Key result | Achievability |
|----------|-------|------------|---------------|
| Multiple uplink users | MAC | Pentagon capacity region | SIC decoding |
| Cellular downlink | Gaussian BC | DPC achieves capacity | Costa precoding |
| Two co-channel users | IC | Open; HK within 1 bit | Public/private split |
| Cooperative relay | Relay channel | DF for degraded | Decode + re-encode |
| Multi-antenna link | MIMO | SVD + waterfilling | Spatial multiplexing |
| Network multicast | DAG network | Max-flow min-cut | Linear network coding |
| Rate-limited relay | CF relay | Wyner-Ziv compression | Compress + Wyner-Ziv |

**When to use SIC vs treat-interference-as-noise**:
- Interference power ≫ desired signal: decode interference first (SIC)
- Interference power ≪ desired signal: treat as noise (TIN is near-optimal for weak IC)
- Interference power ≈ desired signal: Han-Kobayashi splitting

---

## Common Confusion Points

**MAC ≠ TDMA**: TDMA allocates orthogonal time slots — its sum rate is strictly less than
MAC sum capacity (except for users with equal SNR). MAC with SIC achieves strictly higher sum
capacity. The "pentagon" strictly contains the TDMA line segment.

**DPC "free" cancellation**: In dirty paper coding, interference S is pre-subtracted at
zero rate cost — but only if S is known non-causally at the transmitter. The receiver does
NOT need to know S. The encoder "writes on dirty paper" — the receiver reads without seeing the dirt.

**MAC and BC duality**: The capacity region of the Gaussian MIMO MAC (multiple uplink users)
with power constraints equals the capacity region of the dual Gaussian MIMO BC (base station
downlink) under the same total power. This duality is non-trivial and does not hold for
non-Gaussian channels.

**IC capacity open problem**: The two-user Gaussian interference channel capacity is unknown
in general. The best known result (HK, 1 bit gap) is from 2008. This is not a trivially hard
problem — it represents a genuine gap in our understanding of fundamental limits.

**Network coding and routing**: For unicast and multicast, network coding achieves min-cut bound.
For general multiple unicast (multiple source-destination pairs), network coding does NOT generally
help over routing — this is a major open area in network information theory.
