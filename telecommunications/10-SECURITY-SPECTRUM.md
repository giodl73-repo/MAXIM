# Spectrum Security — A Layered Guide

## The Big Picture

Wireless communications are inherently broadcast — anyone with a receiver can hear them.
Spectrum security encompasses protecting confidentiality, preventing jamming, ensuring
GPS integrity, and the frontier of cognitive radio and quantum comms.

```
SPECTRUM SECURITY THREAT LANDSCAPE
════════════════════════════════════════════════════════════════════

THREAT              TECHNIQUE                  DEFENSE
──────────────────────────────────────────────────────────────────────
Eavesdropping       Passive intercept           Encryption (TLS/AES-GCM)
                    IMSI catcher                Mutual auth (LTE+)
                    Rogue AP

Jamming             Noise flood                 FHSS, DSSS, MIMO diversity
                    Deceptive jamming           Power management
                    Smart jamming               HARQ retransmission

GPS spoofing        Broadcast fake GPS          Multiple GNSS, RAIM
                    Meaconing (relay/replay)    Clock authentication (OSNMA)
                    Signal manipulation         IMU fusion

Spectrum sensing    Detect transmissions        Low probability of detection (LPD)
                    SIGINT classification        LPI waveforms, spread spectrum

Cognitive radio     Opportunistic access        Spectrum sensing, coexistence
                    Dynamic spectrum access     Database + sensing hybrid
```

---

## Spread Spectrum: FHSS and DSSS

Spread spectrum techniques spread the signal over a wide bandwidth, providing
both resistance to jamming and low probability of detection/interception.

```
DIRECT SEQUENCE SPREAD SPECTRUM (DSSS):

Data bit rate R_b × Spreading code chip rate R_c >> R_b

Data: ──0──1──1──0──1──
PN code (chip rate R_c): 0011011100100011011100100...
XOR: ────────────────────────────────────────────►
     Wideband spread signal (R_c chips per data bit)

PROCESSING GAIN: PG = R_c/R_b = BW_spread/BW_data (linear)
  In dB: PG_dB = 10·log₁₀(R_c/R_b)
  Example: GPS: R_b = 50 bps, R_c = 1.023 Mcps → PG = 43 dB!

ANTI-JAMMING: Jammer at wideband → after despreading, jamming energy reduced by PG
  Jamming Margin = PG - required Eb/N₀ - loss
  GPS: 43 dB PG → can work in 43 dB of jamming (jammer 20,000× stronger than signal)

GPS C/A CODE (DSSS):
  1,023-chip maximal-length sequence (Gold code), period 1 ms
  Different code per satellite → code-division multiplexing (CDMA)
  All GPS satellites transmit at same frequency (1575.42 MHz); distinguished by code
```

```
FREQUENCY HOPPING SPREAD SPECTRUM (FHSS):

Transmitter and receiver hop frequencies synchronously using shared pseudo-random sequence.

Each symbol transmitted on a different frequency:
  Time 1: 902.0 MHz
  Time 2: 918.5 MHz
  Time 3: 906.0 MHz
  Time 4: 925.5 MHz
  ...

TYPES:
  Fast FHSS: hop rate > symbol rate → multiple hops per symbol
  Slow FHSS: hop rate < symbol rate → multiple symbols per hop

ANTI-JAMMING: Jammer must jam all frequencies simultaneously (wideband jamming)
  Or predict the hop sequence (impossible with synchronized PN codes)

BLUETOOTH: FHSS, 79 channels at 1 MHz spacing in 2.4 GHz, 1600 hops/second
  Classical Bluetooth is FHSS-based → robust against narrowband interference

MILITARY UHF HAVE QUICK: 7 frequencies per second, 25 kHz hops in 225-400 MHz
MILITARY VHF SINCGARS: 100+ hops/second over 30-88 MHz
```

---

## Jamming

```
JAMMING TYPES

1. BARRAGE JAMMING (wideband noise):
   Flood entire band with high-power noise
   Reduces SNR of all signals in band
   Simple but power-hungry; detectable

2. SPOT JAMMING (narrowband):
   Target specific frequency
   More power-efficient against fixed-frequency targets
   Defeated by FHSS (target must hop with the signal)

3. SWEEP JAMMING:
   Sweep narrowband jammer across frequency range
   Hits each frequency briefly → partial effectiveness

4. DECEPTIVE JAMMING (more sophisticated):
   Record and re-transmit (replay) signal with modification
   More effective against GPS (spoofing is a form of deceptive jamming)
   Against radar: return false range/velocity (range gate pull-off, velocity gate pull-off)

5. SMART (FOLLOWER) JAMMING:
   Sense frequency, jump to jam it → attack FHSS
   Effective only if sensing + jam in < 1 hop dwell time
   Modern FHSS hops faster than smart jammers can follow

6. PARTIAL BAND JAMMING:
   Jam portion of DSSS bandwidth
   Creates non-Gaussian noise → more effective than full-band for same power
   Optimum fraction depends on modulation

ELECTRONIC COUNTERMEASURES (ECM) HIERARCHY:
  EW: Electronic Warfare (umbrella)
  ESM: Electronic Support Measures (sensing, SIGINT)
  ECM: Electronic Countermeasures (jamming, deception)
  ECCM: Electronic Counter-Countermeasures (anti-jamming, FHSS, DSSS, LPI/LPD)
```

---

## GPS Spoofing

```
GPS SPOOFING

ATTACK: Generate fake GPS signals stronger than real satellites
  → Victim GPS receiver locks onto fake signals
  → Reports false position, false time, or both

MECHANISM:
  1. Receive real GPS signals (know current pseudoranges)
  2. Generate coherent replicas with modified ranging codes
  3. Transmit at higher power → overpower genuine satellites
  4. Gradually shift pseudoranges → receiver "walks" to false position
     (sudden position jump causes alarm; gradual drift is covert)

HISTORICAL INCIDENTS:
  2011: Iran claims captured US RQ-170 drone via GPS spoofing
  2017-2023: Black Sea incidents → ships showing false positions near airports
  2022-2024: Middle East widespread GPS spoofing disrupting airline navigation
  Gaza conflict area (2024): widespread interference affecting commercial aviation

MITIGATIONS:
  RAIM (Receiver Autonomous Integrity Monitoring):
    Cross-check multiple satellites for consistency
    Flag anomalies (one satellite inconsistent with others)
    Limited against coordinated spoofing of all satellites

  Multi-constellation GNSS:
    GPS + Galileo + GLONASS + BeiDou — harder to spoof all simultaneously

  Galileo OSNMA (Open Service Navigation Message Authentication):
    Cryptographic authentication of navigation data
    Receiver can verify messages came from genuine Galileo satellites
    Deployed 2023 → first open-standard GPS authentication

  IMU (Inertial Measurement Unit) fusion:
    GPS + accelerometer + gyro + barometer
    IMU provides relative position between GPS updates
    Spoofing creates inconsistency with IMU dead-reckoning
    Aviation: IRS (Inertial Reference System) is mandatory backup

  Timing receivers: use multiple GPS + oscillator + PTP (1588) cross-checks
```

---

## Cognitive Radio and Dynamic Spectrum Access

```
COGNITIVE RADIO (SDR + AI spectrum sensing)

PROBLEM: Licensed spectrum is mostly empty most of the time.
  FCC surveys: licensed UHF spectrum occupied <5% of time at most locations.
  "Spectrum scarcity" is partly artificial — inefficient static allocation.

COGNITIVE RADIO CONCEPT (Mitola, 1999):
  1. SENSE: detect presence/absence of primary (licensed) users
  2. DECIDE: determine which spectrum bands are available
  3. ACT: transmit in available bands
  4. LEARN: adapt to environment, improve sensing/decision

PRIMARY VS SECONDARY USERS:
  Primary: licensed user (TV broadcaster, cellular operator)
  Secondary (cognitive radio): opportunistic user, must not interfere with primary

SPECTRUM SENSING TECHNIQUES:
  Energy detection: compare energy in band to threshold
    Simple, no prior knowledge needed, but can't distinguish signal from noise
  Matched filter detection: correlate with known signal structure
    Best performance, requires knowledge of primary signal
  Cyclostationary feature detection: exploit periodicity in modulated signals
    Can distinguish signal types, robust to noise

IEEE 802.22 (WRAN — Wireless Regional Area Network):
  First cognitive radio standard
  Uses unused TV white space (470–710 MHz in US)
  Geolocation database + sensing to avoid TV interference
  50 km range, 22 Mbps per channel

CBRS (Citizens Broadband Radio Service, US, 3550-3700 MHz):
  3-tier hierarchy: incumbents (naval radar, satellite) → PAL (licensed) → GAA (unlicensed)
  Spectrum Access System (SAS) database manages assignments in real-time
  Used for: private 5G LTE networks, indoor enterprise deployment
```

---

## Low Probability of Detection / Interception (LPD/LPI)

```
LPD/LPI WAVEFORM DESIGN

GOAL: Transmit without adversary knowing transmission is occurring.

TECHNIQUES:
1. Spread spectrum (DSSS/FHSS): signals appear as noise to non-intended receivers
2. Power management: transmit minimum power needed → reduces detection range
3. Burst transmission: compress data, transmit in very short burst
4. Frequency agility: change frequency unpredictably
5. Waveform diversity: vary PRF, pulse shape, modulation adaptively
6. Low sidelobe antennas: concentrate energy toward intended receiver

INTERCEPT FACTOR:
  I = P_detect / P_communicate  < 1 is good (intercept harder than reception)

MILITARY LPD/LPI RADAR:
  LFM chirp at very low PRF + long integration time
  Power spectral density below noise floor
  Coherent processing over minutes → detect target without being detected

MILITARY COMMUNICATIONS:
  EPLRS (Enhanced Position Location Reporting System): TDMA + FHSS for LPD
  Link 16 (JTIDS/MIDS): TDMA, FHSS, DSSS, encrypted → jam/intercept resistant
  SINCGARS: VHF FHSS, standard US Army tactical radio
```

---

## Quantum Key Distribution (QKD)

```
QKD — QUANTUM KEY DISTRIBUTION

PRINCIPLE: Use quantum properties to distribute cryptographic keys such that
any eavesdropping attempt disturbs the quantum states and is detectable.

BB84 PROTOCOL (Bennett & Brassard, 1984):
  1. Alice sends qubits (photons) in one of 4 polarization states:
     Rectilinear basis: 0° (bit 0) or 90° (bit 1)
     Diagonal basis: 45° (bit 0) or 135° (bit 1)
  2. Alice randomly chooses which basis for each photon
  3. Bob randomly chooses which basis to measure each photon
  4. Bob correctly measures when using same basis as Alice (~50% of time)
  5. Bob tells Alice which basis he used (public channel, not the measurement result)
  6. Alice tells Bob which were correct → keep only correct-basis bits (sifted key)
  7. Eavesdropper (Eve) forced to guess basis → disturbs 25% of correct-basis bits
  8. Alice and Bob compare subset → detect Eve → discard compromised key

CURRENT QKD LIMITATIONS:
  Range: ~100 km terrestrial (photon loss in fiber)
  Chinese Micius satellite: 1,200 km QKD demonstrated (2017)
  Rate: ~10 kbps secure key rate at 50 km, ~1 bps at 100 km
  Cost: very high, requires specialized equipment
  Practical deployment: banking systems (Korea, Japan), government (China)

STATUS (2025):
  Commercially deployed in limited contexts (financial, government)
  Not replacing classical encryption near-term
  Post-quantum cryptography (ML-KEM, ML-DSA) more practical near-term defense
  against quantum computers (see cryptography/ module)
```

---

## Decision Cheat Sheet

| Threat | Mitigation |
|--------|-----------|
| Eavesdropping of cellular data | Use LTE/5G (mutual auth + AES-128) |
| GPS spoofing of vehicles/aircraft | Multi-constellation + OSNMA + IMU fusion |
| Narrowband jamming of radio | FHSS (frequency hop away from jammer) |
| Wideband jamming of CDMA | DSSS processing gain |
| Unauthorized spectrum use detection | Cognitive radio sensing |
| Long-term protection of keys from quantum computers | Post-quantum crypto (ML-KEM) |
| Ultra-secret key exchange | QKD (limited range, high cost, niche) |

---

## Common Confusion Points

**Spread spectrum is not encryption**: Spreading with a PN code provides jamming resistance and
low probability of interception, but NOT confidentiality. Anyone who knows the spreading code
can despread and read the signal. You need encryption on top of spread spectrum for confidentiality.

**GPS spoofing ≠ jamming**: Jamming prevents GPS from working (receiver can detect it — "no fix").
Spoofing gives the receiver a false position it believes is correct — no alert. Spoofing is
far more dangerous operationally. A jammed aircraft knows it's GPS-denied; a spoofed aircraft
may fly confidently into a mountain or restricted airspace.

**Cognitive radio is mostly theoretical in consumer products (so far)**: TV white space (802.22,
Google TV Bands Device) and CBRS have seen limited commercial deployment. Most "cognitive radio"
research hasn't reached mass-market consumer devices. The coordination infrastructure (databases,
sensing) is complex and costly.

**QKD doesn't protect against all quantum threats**: QKD protects the key distribution. But if the
endpoint devices are compromised, or if classical algorithms (RSA/ECC) are still used elsewhere,
QKD alone doesn't secure the system. Post-quantum algorithms (ML-KEM, Kyber) are a more practical
near-term approach to the quantum threat.
