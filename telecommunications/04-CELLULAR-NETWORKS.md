# Cellular Networks — A Layered Guide

## The Big Picture

Cellular networks divide a geographic area into cells, reuse frequencies between non-adjacent
cells, and hand off mobiles between cells. Each generation fundamentally changed the radio
access technology.

```
CELLULAR GENERATIONS OVERVIEW
════════════════════════════════════════════════════════════════════

Gen  Year  Standard      Radio Access     Core           Peak Rate
──────────────────────────────────────────────────────────────────
1G   1981  AMPS, NMT     FDMA analog      Circuit        14.4 kbps
2G   1991  GSM           TDMA digital     Circuit + GPRS  384 kbps
     1993  IS-95 (cdmaOne) CDMA           Circuit        14.4 kbps
2.5G 2000  GPRS (GSM+)   TDMA + packet   Packet (partial) 384 kbps
2.75G 2003 EDGE          8-PSK TDMA      Packet          384 kbps
3G   2001  UMTS/WCDMA    CDMA 5MHz       All-IP (partial) 7.2 Mbps
3.5G 2006  HSDPA         CDMA adaptive   All-IP          14.4 Mbps
4G   2009  LTE Release 8 OFDMA/SC-FDMA  All-IP (EPC)   300 Mbps
4G+  2013  LTE-A (R10)   Carrier agg.   EPC             1 Gbps
5G   2019  NR Release 15 OFDM/Massive    5GC (slicing)   20 Gbps
           3GPP          MIMO + mmWave

KEY EVOLUTIONARY TREND:
FDMA (divide by frequency) → TDMA (divide by time) → CDMA (divide by code) →
OFDMA (divide by subcarrier) → Massive MIMO (divide by spatial beam)
```

---

## The Cellular Concept

```
FREQUENCY REUSE

Problem: RF spectrum is finite. One transmitter per area = can't serve many users.
Solution: Reuse the same frequency in cells far enough apart that interference is acceptable.

CLUSTER SIZE (N = 1, 3, 4, 7, 12, 19...):
N = 7 (hexagonal cells):
  ┌──────┬──────┬──────┐
  │      │      │      │
  │  1   │  2   │  3   │
  │      │      │      │
  ├──────┼──────┼──────┤
  │      │      │      │
  │  4   │  5   │  6   │
  │      │      │      │
  ├──────┼──────┼──────┤
  │      │  7   │  1   │  ← frequency 1 reused here
  │      │      │      │
  └──────┴──────┴──────┘

Co-channel reuse ratio: D/R = √(3N)  (D = distance to nearest co-channel cell, R = cell radius)
For N=7: D/R = 4.58 → interference well-controlled

SMALL CELLS: Reduce cell radius R → more cells → more frequency reuse → more capacity.
Coverage: macro (R=1-35 km) → micro (100m-1km) → pico (10-200m) → femto (indoor, 10-50m)
```

---

**Reader note**: 1G/2G/3G sections below provide evolutionary context — each generation represents one architectural shift. The substantive depth begins at 4G LTE and the full treatment is at 5G NR, which is the direct enterprise cloud networking integration point.

## 2G: GSM

GSM introduced global roaming and digital voice. Still operational in many regions.

```
GSM (Global System for Mobile Communications)

RADIO ACCESS: FDMA + TDMA
  FDMA: 200 kHz channel bandwidth
  TDMA: 8 time slots per carrier frame
  → Each call gets 1 time slot in every 8-frame cycle (12.5% duty cycle)
  → One carrier serves 8 simultaneous users

FREQUENCY BANDS:
  GSM-900: 890-915 MHz uplink, 935-960 MHz downlink (25 MHz each = 124 channels)
  GSM-1800 (DCS-1800): 1710-1785 MHz uplink, 1805-1880 MHz downlink
  GSM-850 (US): similar to 900

VOICE CODEC:
  GSM Full Rate: 13 kbps
  Enhanced Full Rate (EFR): 12.2 kbps (better quality)
  Half Rate: 5.6 kbps (doubles capacity at lower quality)

SIM (Subscriber Identity Module):
  Smart card with IMSI, encryption keys, authentication data
  Authentication: challenge-response (A3 algorithm), not used elsewhere
  Key innovation: SIM made carrier identity separate from handset

SECURITY NOTE: GSM A5/1 stream cipher is known to be broken.
  Downgrade attacks possible. No mutual authentication (base station to phone).
  Exploitable by IMSI catchers ("Stingrays").
```

---

## 3G: WCDMA/UMTS

```
UMTS/WCDMA (Wideband CDMA)

RADIO ACCESS: CDMA with 5 MHz wideband channels
  FDMA distinction eliminated: all users share the same 5 MHz channel simultaneously
  Each user assigned a unique spreading code (Walsh/Hadamard + PN codes)

CDMA SPREADING:
  User data at R bps spread to chip rate W = 3.84 Mcps (chips per second)
  Processing gain: PG = W/R = 3,840,000/12,200 = 315 = 25 dB (for voice)
  Each user's signal appears as noise to others; despreading recovers original data
  Capacity: determined by total interference, not channel slots

RAKE RECEIVER:
  Multipath arrivals (from reflections) are treated as additional signal
  Multiple correlators ("fingers") each aligned to a path → combine coherently
  → CDMA exploits multipath rather than fighting it

SOFT HANDOFF:
  Mobile can be connected to multiple base stations simultaneously
  "Make before break" (vs. GSM hard handoff: break then make)
  → Eliminates coverage gaps in handoff zone, reduces call drops

PEAK RATE:
  HSDPA (3.5G): 14.4 Mbps downlink (64-QAM, fast scheduling, HARQ)
  HSUPA: 5.76 Mbps uplink
```

---

## 4G: LTE

```
LTE (Long Term Evolution) — the dominant mobile technology from 2010s

FUNDAMENTAL CHANGE: All-IP from the beginning. No circuit-switched voice.
  Voice over LTE (VoLTE): voice is just another IP application (IMS)

RADIO ACCESS: OFDMA downlink, SC-FDMA uplink
  OFDMA: multiple users each assigned different subcarriers in same OFDM symbol
  SC-FDMA: single carrier with frequency domain equalization (lower PAPR than OFDMA)

OFDM PARAMETERS (20 MHz bandwidth):
  Subcarrier spacing: 15 kHz
  FFT size: 2048
  Active subcarriers: 1200 (100 resource blocks × 12 subcarriers/RB)
  Symbol duration: 71.4 µs (66.7µs useful + 4.7µs CP)

MIMO (Multiple Input Multiple Output):
  2×2 MIMO: 2 Tx antennas, 2 Rx antennas → 2 spatial streams → 2× throughput (theoretically)
  4×4 MIMO (LTE-A): 4 spatial streams at high SNR
  Physical basis: multipath creates independent spatial channels

LTE PEAK RATES:
  Category 4: 150 Mbps DL, 50 Mbps UL (2×2 MIMO, 64-QAM)
  Cat 9/10 (LTE-A): 600 Mbps+ (carrier aggregation, 4×4 MIMO)
  Cat 20: 2 Gbps (256-QAM, 4 carrier aggregation)

EPC (Evolved Packet Core):
  eNB (base station) → S-GW (Serving Gateway) → P-GW (PDN Gateway) → Internet
  MME: Mobility Management Entity (authentication, location, paging)
  HSS: Home Subscriber Server (subscriber database, authentication)
  Completely flat IP architecture — no circuit switching

LTE SECURITY (compared to GSM):
  Mutual authentication (network authenticates to UE and vice versa)
  AES-128 encryption for data and signaling
  Integrity protection on control plane (prevents man-in-middle)
```

---

## 5G NR (New Radio)

```
5G ARCHITECTURE — THREE USE CASES:

eMBB (Enhanced Mobile Broadband):  → Video streaming, AR/VR, hotspot
  Goal: 20 Gbps peak, 100 Mbps experienced
  Technology: mmWave + massive MIMO + carrier aggregation

uRLLC (Ultra-Reliable Low Latency):  → Autonomous vehicles, industrial control
  Goal: 1 ms OTA latency, 99.999% reliability
  Technology: short slots (μ = 3,4 numerology), HARQ retransmission, mini-slots

mMTC (Massive Machine Type):  → IoT, smart city sensors
  Goal: 1 million devices per km²
  Technology: NB-IoT, eMTC (LTE-M)

5G NR NUMEROLOGIES:
  μ = 0: 15 kHz subcarrier spacing, 71.4 µs symbol, sub-3 GHz
  μ = 1: 30 kHz, sub-3 GHz and 3-7 GHz
  μ = 2: 60 kHz, sub-6 GHz and mmWave
  μ = 3: 120 kHz, mmWave (24-100 GHz)

mmWave (FR2: 24-40 GHz):
  Available: 400 MHz – 800 MHz bandwidth per operator → 10-20× LTE bandwidth
  Problem: very high path loss, no building penetration, short range (200-400m)
  Solution: massive MIMO beamforming, dense small cells
  Status: mainly outdoor dense urban, stadiums, fixed wireless access (FWA)

Sub-6 GHz (FR1: 450 MHz – 6 GHz):
  Reuses existing cellular bands + new spectrum (n77/n78 3.5 GHz C-band)
  Better coverage, moderate bandwidth gain over LTE
  3.5 GHz C-band: 100 MHz bandwidth, main 5G deployment worldwide

MASSIVE MIMO:
  64, 128, 192, 256 antenna elements at base station
  Beam-steering in 3D (azimuth + elevation) to each UE
  MU-MIMO: serve multiple users in same time/frequency resource, different beams
  Beamforming gain: log₂(M_antennas) ≈ 7-8 dB for 192 elements
```

```
5G CORE (5GC) — SERVICE BASED ARCHITECTURE (SBA):

Replaces EPC with microservices:
  AMF: Access and Mobility Management (replaces MME)
  SMF: Session Management Function
  UPF: User Plane Function (data forwarding)
  PCF: Policy Control Function
  NRF: Network Repository Function (service registry)

Network Slicing:
  Create multiple virtual networks on same physical infrastructure
  Each slice has dedicated QoS, security, capacity
  NSI (Network Slice Instance): separate for eMBB, uRLLC, mMTC
  This is why 5G is critical for industry 4.0 applications
  A 5G network slice is the wireless equivalent of a Kubernetes namespace or VNet:
  an isolated resource pool with a policy boundary and QoS SLA, enforced at the RAN
  level via RAN slicing and at the core via SBA microservices. The mapping is direct:
  K8s namespace → VNet + NSG → 5G network slice (dedicated bandwidth + latency + security).
```

---

## Decision Cheat Sheet

| Scenario | Technology |
|----------|-----------|
| Voice call in rural area | 2G GSM / 3G WCDMA (better coverage) |
| Video streaming urban | 4G LTE or 5G NR sub-6 |
| Low latency industrial automation | 5G uRLLC (URLLC slice, private 5G) |
| Dense IoT deployment (millions of sensors) | NB-IoT or eMTC on cellular |
| Stadium events (high user density) | 5G mmWave small cells |
| Rural broadband | 4G LTE FWA or 5G sub-6 FWA |
| Private network enterprise | Private 5G (dedicated spectrum) or cbrs (US) |

---

## Common Confusion Points

**5G standalone (SA) vs non-standalone (NSA)**: NSA uses 5G NR for data but LTE for control plane
(anchors). No latency improvement, partial features. SA uses 5G core (5GC) directly — enables network
slicing, true URLLC, full 5G capability. Most deployments through 2023 were NSA.

**LTE categories are not the same as bands**: LTE band (frequency band, e.g., Band 4 at 1700 MHz)
determines coverage. LTE category (e.g., Cat 12) determines peak data rate. Both matter for device
performance.

**CDMA spreading gain ≠ free capacity**: In CDMA, all users are interference to each other.
As more users are added, the noise floor rises for all → eventually all users see degraded quality.
The "soft capacity limit" can be exceeded: quality degrades gracefully (unlike TDMA/FDMA hard limits).
This is both a strength and a weakness.

**5G mmWave doesn't penetrate anything**: Not just building walls — mmWave doesn't penetrate human
hands well. Hold your phone differently → 10-20 dB signal loss. This forced 5G mmWave phones to have
antenna arrays on multiple sides of the phone. Indoor coverage from outdoor mmWave BSs is basically zero.
