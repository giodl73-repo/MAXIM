# Communications Engineers — Morse, Bell, Armstrong, Farnsworth, Shannon

## Era Overview

```
THE COMMUNICATIONS REVOLUTION: 1837–1950
==========================================

  1837 ─── MORSE+VAIL: Electromagnetic telegraph demonstrated.
  1844 ─── MORSE: Washington–Baltimore telegraph line operational.
  1851 ─── Transatlantic cable attempt (fails).
  1858 ─── First transatlantic telegraph (fails after 3 weeks).
  1866 ─── ATLANTIC TELEGRAPH: SS Great Eastern lays permanent cable.
           London ↔ New York in minutes (vs. 2 weeks by ship).

  1876 ─── BELL: Telephone patent (March 7). "Mr. Watson, come here."
  1877 ─── BELL: First telephone exchange (Boston).
  1878 ─── First telephone directory. 50 subscribers.

  1887 ─── HERTZ: Demonstrates radio waves.
  1901 ─── MARCONI: Transatlantic wireless.
  1906 ─── FESSENDEN: First voice radio broadcast (Christmas Eve).
  1907 ─── DE FOREST: Triode vacuum tube amplifier.

  1920 ─── KDKA Pittsburgh: first commercial radio station.
  1920s ─── AM radio broadcasting. Nationwide networks.

  1933 ─── ARMSTRONG: FM radio demonstrated. Better audio. Less noise.
  1935 ─── ARMSTRONG: FM demonstration broadcast from Empire State Building.
  1941 ─── FM broadcasting licensed. RCA/NBC fight it anyway.

  1926 ─── BAIRD: First television demonstration (mechanical).
  1927 ─── FARNSWORTH: First electronic television image.
  1934 ─── FARNSWORTH vs. RCA patent dispute begins.
  1939 ─── RCA launches commercial TV broadcast at World's Fair.

  1948 ─── SHANNON: "A Mathematical Theory of Communication."
           (Profiled in computing-pioneers/04-INFORMATION-THEORY.md)

  1948 ─── TRANSISTOR (Bell Labs): enables miniaturization.
  1950s ─── Coaxial cable, microwave relay towers.
  1962 ─── TELSTAR: first active communications satellite.
```

---

## Samuel Morse (1791–1872) and Alfred Vail (1807–1859)

### Bio Snapshot

**Morse**: American painter and inventor. Yale. Portrait painter (painted Lafayette, DeWitt Clinton). Conceived the telegraph while sailing back from Europe in 1832, after hearing about electromagnets. Spent years developing it with limited resources.

**Vail**: New Jersey machinist's son. New York University. Became Morse's partner and principal engineer. Designed much of the practical hardware, including the code (though Morse received sole credit). Vail's family factory provided the funding and workshop.

### The Telegraph and Morse Code

**What Morse provided**: The concept — long-distance electrical signaling using pulsed current. The demonstration to Congress. The political and legal persistence to get funding and protection.

**What Vail provided**: The practical hardware design (the key, the sounder, the relay), the code optimization, and much of the engineering work.

```
THE TELEGRAPH SYSTEM
======================

  ELECTROMAGNETIC PRINCIPLE:
    Send current through a wire.
    At the far end: current energizes an electromagnet.
    Electromagnet attracts an iron lever → "click."
    No current: lever springs back → "clack."
    Series of clicks and pauses = coded message.

  THE RELAY:
    Problem: resistance of long wires reduces current.
    At 300+ miles: signal too weak to operate a sounder.
    Solution: relay stations every ~200 miles.
    Relay: weak incoming current operates a sensitive electromagnet,
           which closes a local battery circuit with fresh current.
    Repeater: regenerates signal, doesn't amplify noise.
    (Same principle as TCP/IP digital regeneration vs. analog amplification.)

  MORSE CODE:
    Short pulse = dot (dit)
    Long pulse = dash (dah)
    International Morse Code (1865):
      E = .     (most common letter → shortest code)
      T = -     (2nd most common)
      A = .-
      I = ..
      S = ...
      O = ---
    Code length inversely proportional to letter frequency.
    This is a variable-length prefix code — Shannon entropy-optimal coding
    applied intuitively by Vail (who analyzed letter frequencies in a
    printer's type case to assign short codes to common letters).
    Vail's optimization is a precursor to Huffman coding (1952).
```

**The 1844 demonstration**: "What hath God wrought" (Numbers 23:23, chosen by Annie Ellsworth). The first public long-distance telegraph message. The political importance was immediate: news that previously took weeks by rider could now travel in seconds. Stock exchanges, newspapers, military commands — all transformed.

---

## Alexander Graham Bell (1847–1922)

### Bio Snapshot

Scottish-American inventor. Edinburgh, London, Boston. Father of deaf education — his mother and wife were deaf; he was a teacher of speech to the deaf. Developed the telephone while working on harmonic telegraph research. Settled in Nova Scotia later in life. The Bell Telephone Company became AT&T — the most valuable company in the world for much of the 20th century.

### The Telephone

**The problem with telegraph**: Telegraph was message-by-message, coded, requiring trained operators. Bell wanted to transmit the human voice directly.

```
THE TELEPHONE PRINCIPLE
=========================

  SOUND WAVE → ELECTRICAL SIGNAL → SOUND WAVE

  TRANSMITTER (mouthpiece):
    Sound wave causes diaphragm to vibrate.
    Vibrating diaphragm varies the current through a circuit.
    Bell's first design: vibrating membrane over an acid bath —
    membrane movement changes resistance → changes current.
    Later: carbon granules (Edison's improvement, 1877–78) —
    sound compresses granules → resistance changes → current varies.
    This became the microphone.

  RECEIVER (earpiece):
    Varying current through an electromagnet.
    Electromagnet attracts diaphragm varying with current.
    Diaphragm vibrations → sound waves → you hear voice.

  KEY TECHNICAL CHALLENGE:
    The signal must be ANALOG — continuously varying to represent voice.
    Not on/off like telegraph. Continuously proportional to sound pressure.

  BELL vs. ELISHA GRAY:
    Gray filed a caveat (preliminary patent notice) for a telephone
    on February 14, 1876 — the same day Bell filed his patent.
    Bell's patent was filed hours before Gray's caveat.
    Bell was awarded the patent. The most profitable patent in history.
    Gray spent years in litigation. Bell and AT&T won every case.
```

**Bell's subsequent career**: Bell received royalties from his telephone patents until 1893. After that he worked on: phonograph improvements, hydrofoil boats, aeronautics (tetrahedral kite structures, airplanes), and metal detectors (tried to locate the bullet in President Garfield, 1881 — failed due to interference from metal bed springs).

### AT&T and the Bell System

Bell Telephone Company (1877) → American Telephone and Telegraph (AT&T, 1885). After Bell's original patents expired in 1893–1894, thousands of independent telephone companies formed. AT&T systematically bought or undercut them, eventually achieving near-monopoly. The Bell System was the regulated telephone monopoly in the US from roughly 1915 to 1984, when antitrust action broke it into the "Baby Bells." AT&T also owned Bell Labs — where the transistor, information theory, Unix, and C were invented.

---

## Edwin Armstrong (1890–1954)

### Bio Snapshot

American electrical engineer. Columbia. Invented three of the most important radio circuit technologies: the regenerative circuit (1912), the superheterodyne receiver (1918), and FM radio (1933). Spent the last 10+ years of his life in patent disputes with RCA/Sarnoff. Died by suicide in 1954, throwing himself from his New York apartment window. His wife continued the patent battles for 13 more years and eventually collected settlements from all defendants.

### FM Radio

**The problem with AM**: Amplitude Modulation (AM) radio encodes audio by varying the amplitude (strength) of the radio signal. Electrical noise — lightning, motors, electrical equipment — is additive amplitude noise. AM radio sounds like whatever the original signal plus the noise.

```
AM vs. FM — THE TECHNICAL DIFFERENCE
=======================================

  AM (Amplitude Modulation):
    Carrier wave: constant frequency, varying amplitude.
    Signal: audio encoded in the amplitude variation.
    Noise: electrical interference adds to amplitude.
    Signal/noise is partially separable but not cleanly.
    Audio quality: limited by noise floor.
    Range: long (AM propagates by ionospheric reflection at night).

  FM (Frequency Modulation):
    Carrier wave: constant amplitude, varying frequency.
    Signal: audio encoded in the frequency variation.
    Noise: electrical interference adds to amplitude.
    FM RECEIVERS CAN IGNORE AMPLITUDE VARIATIONS.
    "Limiter" circuit: clips the signal to constant amplitude.
    Clips off the noise. Passes only frequency variations = signal.
    Result: audio quality independent of noise.

  THE CAPTURE EFFECT:
    Two FM stations at same frequency: the stronger one wins entirely.
    No mixing, no interference — cleaner than AM where two stations
    would blend together.

  BANDWIDTH TRADEOFF:
    FM requires ~200 kHz bandwidth per station.
    AM requires ~10 kHz per station.
    FM: only viable at VHF (88–108 MHz) where bandwidth is available.
    This high frequency means FM doesn't propagate by ionospheric reflection.
    FM range: line-of-sight (40–100 miles). AM range: hundreds of miles at night.
```

**RCA's fight against FM**: David Sarnoff (RCA) controlled AM broadcasting and NBC. Armstrong's FM threatened this empire. Sarnoff fought FM at the FCC, got FM frequencies reassigned (requiring all existing FM receivers to be junked), and delayed FM's deployment for decades. Armstrong's patents expired before FM became commercially dominant. This is a classic case of an incumbent using regulatory capture to suppress a superior technology.

---

## Philo Farnsworth (1906–1971)

### Bio Snapshot

American inventor from Idaho. Largely self-taught. Conceived electronic television at 14 while plowing a field, thinking about electrons scanning a field line by line. Got his first patent at 21. Spent much of his life fighting RCA (which tried to claim his patents via Vladimir Zworykin's earlier work) and died largely unrewarded financially.

### Electronic Television

**Mechanical television (existing, 1920s)**: Used a spinning disk with holes (Nipkow disk) to scan an image. Limited resolution (30–240 lines). Low frame rate. Impractical for broadcasting.

```
FARNSWORTH'S ELECTRONIC TELEVISION (1927)
===========================================

  THE IMAGE DISSECTOR (transmitter):
    Scene projected onto photosensitive layer.
    Electrons released proportional to light intensity.
    Magnetic field deflects electron stream across the layer line by line.
    Scanning: 30 lines → 240 lines → modern 525/625 lines.
    Current from the electron stream → varying electrical signal.

  THE CATHODE RAY TUBE (receiver, not Farnsworth's invention):
    Electron gun fires beam at phosphor-coated screen.
    Magnetic deflection coils steer beam in raster pattern.
    Beam intensity varied by video signal.
    Phosphor glows where beam hits → visible image.

  SCANNING:
    525 lines × 30 frames/second = 15,750 lines/second.
    Electron beam sweeps each line in ~63 microseconds.
    Interlacing (odd lines, then even lines): reduces flicker.
    This raster scan pattern was TV for 60 years (CRT era).

  FARNSWORTH'S FIRST IMAGE (September 7, 1927):
    A horizontal line.
    He showed it to his investor and said:
    "There you have it — electronic television."

  WHY IT MATTERED:
    No moving parts in transmission or reception.
    Limited only by electronics, not mechanical speed.
    Frame rates and resolution could improve with better electronics.
    This is the architecture of all video: raster scan, frame buffers, pixels.
    Modern digital video is still raster-scanned (just digitally).
```

**The Zworykin dispute**: Vladimir Zworykin (RCA, working under Sarnoff) filed an earlier patent on an "iconoscope" (a CRT-based image pickup). RCA argued Zworykin had priority. Farnsworth's 1930 demonstration convinced the patent examiner that Farnsworth's system was working earlier. Farnsworth won the key patent. RCA eventually licensed from Farnsworth (the first time Sarnoff ever paid for an outside patent). But Farnsworth's health was ruined by stress and heavy drinking; he received little of the financial benefit.

---

## Shannon — Cross-Reference

Shannon (profiled in `computing-pioneers/04-INFORMATION-THEORY.md`) is the theoretical foundation for all communications:
- Entropy = minimum bits to represent a message
- Channel capacity = maximum reliable transmission rate
- Source coding theorem → all compression
- Noisy channel theorem → all error-correcting codes

His 1937 master's thesis (Boolean algebra → electrical circuits) is equally foundational for communication hardware.

---

## Comparison Table

| Figure | Life | Innovation | Commercialized By |
|--------|------|-----------|------------------|
| Morse + Vail | 1791–1872 / 1807–1859 | Telegraph + Morse code | Western Union |
| Bell | 1847–1922 | Telephone | AT&T |
| Armstrong | 1890–1954 | FM radio; regenerative + superheterodyne circuits | Others (after his death) |
| Farnsworth | 1906–1971 | Electronic television | RCA / NBC (after licensing) |

---

## Who to Cite for What

| Concept | Figure |
|---------|--------|
| Electric telegraph | Morse + Vail (1837–1844) |
| Morse code (optimized variable-length) | Vail (credited to Morse) |
| Telephone | Bell (1876) |
| FM radio | Armstrong (1933) |
| Capture effect / limiter circuit | Armstrong |
| Regenerative receiver | Armstrong (1912) |
| Superheterodyne receiver | Armstrong (1918) |
| Electronic television (image dissector) | Farnsworth (1927) |
| Information theory / entropy | Shannon (see computing-pioneers/04) |

---

## Common Confusion Points

**"Bell invented the telephone."**
Bell was awarded the patent for the telephone in 1876, edging out Elisha Gray by hours. The technical invention was contested, and Elisha Gray had a working device. Bell was certainly working on the problem and filed first; the exact priority is disputed. Bell's patent is the legal foundation of AT&T.

**"FM is just AM with different modulation."**
The physics of FM's noise rejection is fundamentally different. FM's advantage is not just "better modulation" — the limiter circuit can remove amplitude noise entirely, something AM cannot do. The tradeoff is bandwidth: FM requires 20x more spectrum per station.

**"RCA invented television."**
RCA commercialized it. Farnsworth invented electronic television (1927). Zworykin had concepts (1923 patent application) but had not demonstrated a working all-electronic system. The patent rulings consistently supported Farnsworth's priority on the key elements.
