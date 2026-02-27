# Telecommunications — Overview

## The Big Picture

Telecommunications is the engineering of transmitting information across distance.
The fundamental constraint is Shannon's channel capacity — a hard physical limit
on how much information can flow through any channel.

```
THE SHANNON CHANNEL MODEL (Shannon 1948)
════════════════════════════════════════════════════════════════════

Information     Source       Channel         Destination
Source          Encoder      (noisy)         Decoder
   │               │            │               │
[Text/     ──► [Compress] ──► [Modulate] ──► [Demodulate] ──► [Decode] ──► [Reconstruct]
 Voice/        [Encrypt]      [Transmit]     [Filter]          [Correct
 Video]        [Channel-      over medium    [Amplify]          errors]
                code]
                  │               │                               │
                  │         ┌─────┴─────┐                        │
                  │         │  Noise N  │                        │
                  │         └───────────┘                        │
                  │               │                               │
                  └───────────────┴───────────────────────────────
                         Information rate ≤ Channel capacity C

SHANNON CAPACITY:
C = B · log₂(1 + S/N)   bits/second

B = bandwidth (Hz)
S = signal power (W)
N = noise power (W)
S/N = signal-to-noise ratio (dimensionless)

This is a HARD UPPER BOUND — no coding scheme, no matter how clever, can exceed it.
But with the right channel codes, you can get arbitrarily close.
```

---

## The Spectrum as Finite Resource

EM spectrum is scarce, shared, and regulated. The entire modern wireless economy is
built on efficient use of this finite resource.

```
SPECTRUM ALLOCATION OVERVIEW

Frequency    Band    Wavelength    Dominant Use
─────────────────────────────────────────────────────────────────────────
3–30 Hz      ELF     100,000 km   Submarine communication
30–300 Hz    SLF     10,000 km    Submarine communication
300–3000 Hz  ULF     1000 km      Natural noise
3–30 kHz     VLF     100 km       Navigation (OMEGA), military
30–300 kHz   LF      10 km        AM broadcast (long wave), LORAN
300–3000 kHz MF      1 km         AM broadcast (medium wave)
3–30 MHz     HF      100 m        Shortwave, amateur, military
30–300 MHz   VHF     10 m         FM radio, TV, aircraft comms
300–3000 MHz UHF     1 m          TV, mobile phones, WiFi, GPS
3–30 GHz     SHF     10 cm        Satellite, radar, 5G mmWave, WiFi
30–300 GHz   EHF     1 mm         5G mmWave, satellite, millimeter radar
300 GHz+     THF     1 mm+        Experimental THz

REGULATORY BODIES:
ITU: International Telecommunication Union — global spectrum allocation (Radio Regulations)
FCC: Federal Communications Commission — US domestic spectrum
ETSI: European Telecommunications Standards Institute — European standards
3GPP: 3rd Generation Partnership Project — cellular standards (LTE/5G)
IEEE: 802.11 (WiFi), 802.15 (Bluetooth/Zigbee), 802.3 (Ethernet)
```

---

## The SNR-Bandwidth-Rate Triangle

Shannon's formula defines the fundamental trade space for any link:

```
SNR-BANDWIDTH-RATE TRADE-OFF

Given target rate R (bits/s):

         ┌─────────────────────────────────────────────────────┐
         │                                                      │
         │  C = B · log₂(1 + S/N) ≥ R                        │
         │                                                      │
         │  To achieve higher rate R, you need:                │
         │  • More bandwidth B (spectrum)                      │
         │  • Higher S/N ratio (more power or less noise)      │
         │  • OR both                                          │
         │                                                      │
         │  PRACTICAL LIMIT: Real-world SNR is limited by:     │
         │  • Transmit power constraints (cell battery, satellite ERP) │
         │  • Path loss (free space, foliage, buildings)       │
         │  • Noise floor (thermal noise, interference)        │
         │                                                      │
         └─────────────────────────────────────────────────────┘

SPECTRAL EFFICIENCY (bits/s/Hz):
η = C/B = log₂(1 + SNR)

At SNR = 10 dB (10:1 ratio): η ≤ 3.46 bits/s/Hz
At SNR = 20 dB (100:1):     η ≤ 6.66 bits/s/Hz
At SNR = 30 dB (1000:1):    η ≤ 9.97 bits/s/Hz

Modern 5G NR: achieves ~7-8 bits/s/Hz at high SNR (close to Shannon limit!)
```

---

## Wired vs Wireless Taxonomy

```
TELECOMMUNICATIONS MEDIA

GUIDED (wired):
  Twisted pair (UTP/STP):
    Telephone (POTS): 4 kHz bandwidth → 33 kbps
    VDSL2: 30 MHz → 100 Mbps at short distance
    Cat6A/8: 500 MHz–2 GHz → 10–40 Gbps (ethernet)

  Coaxial cable:
    CATV (cable TV): 5–1000 MHz → multi-Gbps DOCSIS 3.1
    RG-6, RG-11: for distribution

  Optical fiber:
    SMF (single-mode): 1310/1550 nm → Tbps per fiber with DWDM
    MMF (multimode): 850/1300 nm → 40-400G for datacenter
    Submarine cables: up to 400 Tbps per cable (2020s)

UNGUIDED (wireless):
  Radio: ground wave, sky wave, line-of-sight
  Microwave: point-to-point (LOS), satellite
  Infrared: short range (TV remotes, IrDA)
  Optical FSO: laser through air
  Acoustic (underwater): sonar, OFDM modems
```

---

## Module Map

```
telecommunications/
│
├── 01-ELECTROMAGNETIC-SPECTRUM    EM spectrum: VLF to EHF, propagation per band
│
├── 02-MODULATION                  How information encodes onto carriers
│       AM/FM/PM; ASK/BPSK/QAM; OFDM
│
├── 03-RADIO-BROADCASTING          AM/FM, antennas, link budgets, propagation
│
├── 04-CELLULAR-NETWORKS           2G GSM → 3G WCDMA → 4G LTE → 5G NR
│
├── 05-SATELLITE-COMMUNICATIONS    GEO/MEO/LEO, latency, Starlink, GPS
│
├── 06-OPTICAL-COMMUNICATIONS      Fiber types, WDM/DWDM, EDFA, coherent, submarine
│
├── 07-INTERNET-BACKBONE           Tier 1/2/3, peering/transit, IXPs, BGP, CDN
│
├── 08-WIRELESS-STANDARDS          WiFi 802.11, Bluetooth, Zigbee, LoRa, NFC
│
├── 09-CHANNEL-CODING              Shannon, Hamming, turbo, LDPC, polar, HARQ
│
└── 10-SECURITY-SPECTRUM           Cognitive radio, jamming, frequency hopping, QKD
```

---

## Bridges to Prior Knowledge

| Universal CS Concept | Telecom Equivalent |
|----------------------|-------------------|
| **Complexity bound** (hard limit no algorithm beats) | Shannon capacity C = B*log2(1+SNR) — provable upper limit on data rate for any code |
| **Hardware abstraction layer** (OS hides hardware) | OSI physical layer abstracts EM propagation from protocols above |
| **Resource scheduling under scarcity** (CPU/memory) | Spectrum allocation = scheduling a shared, finite resource among competing users |
| **Multiplexing** (time-sharing, threads) | TDM, FDM, CDM, OFDMA — same concept, different physical resources |

| Azure/Infrastructure Background | Telecom Equivalent |
|---------------------------|-------------------|
| Azure networking (VNets, gateways) | Physical layer that carries IP packets |
| TCP/IP protocols | Built on top of physical + data link telecom layers |
| Azure CDN | Content distribution network (physical layer = fiber/cable/wireless) |
| Azure regions / datacenters | Connected by backbone fiber and submarine cables |
| Azure ExpressRoute | Dedicated fiber connection bypassing public internet |
| Network bandwidth in cloud | Physical: fiber capacity (Tbps), user sees slice of it |
| Signal processing background | Modulation, channel coding, demodulation |

---

## Decision Cheat Sheet

| Need | Technology |
|------|-----------|
| Highest data rate, fixed location | Optical fiber (SMF + DWDM) |
| Wide-area mobile data | 4G LTE / 5G NR |
| Low-power IoT sensor | LoRa / NB-IoT / Zigbee |
| Short-range, low-power personal devices | Bluetooth LE (BLE) |
| Direct broadband to remote location | Starlink (LEO) or VSAT (GEO) |
| Timing reference (nanosecond) | GPS/GNSS (uses satellite ranging signals) |
| Secure links over fiber | QKD (quantum key distribution, near-term) or AES-GCM (standard) |
| Global broadcast (one to many) | Geostationary satellite |

---

## Common Confusion Points

**Bandwidth means different things**: In analog/RF: Hz (spectral width). In digital networking: bits/s
(data rate). In signal processing: both. Shannon's formula connects these: C (bits/s) = B (Hz) × log₂(1+SNR).

**Channel capacity is not throughput**: Real systems operate below Shannon capacity due to overhead
(headers, guard bands, pilots, error correction), practical modulation limits, and implementation
imperfections. LTE at 20 MHz theoretically achieves ~150 Mbps peak; practical throughput is 50–80 Mbps.

**5G is not just faster 4G**: 5G adds sub-1 ms latency (ultra-reliable low latency, uRLLC), network
slicing, massive MIMO, and operation in mmWave bands (24–100 GHz). These are fundamentally new
capabilities, not just speed increases.

**Wired and wireless share the same Shannon limit**: Both obey C = B·log₂(1+SNR). Fiber has
enormous bandwidth (THz) and very low noise → huge capacity. Radio has limited bandwidth allocation
and noise → constrained. The physics is the same.
