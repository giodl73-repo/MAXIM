# [30] --- Zinc

**2&#9829; The Collector** &middot; Natural World &middot; T2

---

> The Collector hears what others dismiss as noise. Five birds sing at dawn. She records each one. The spectrograms sit on your desk now -- every call a shape in time. The duration is the message. Listen with your eyes.

---

## The Puzzle

**Type:** Birdsong as Morse -- spectrogram patterns decode as Morse code
**Answer:** --- (T2)
**References:** ornithology/05-SONG-COMMUNICATION.md, codes/01-MORSE.md

Five birds were recorded at a single dawn survey. Each recording was converted to a spectrogram -- a standard sonogram showing time (horizontal axis) versus frequency (vertical axis), with note intensity shown by the density of the marks. This is the same visualization described in the ornithology section's guide to song and communication.

Study the five spectrograms below. Each bird produces a sequence of discrete notes. Some notes are brief pulses. Others are long, sustained tones. Every note in every recording is clearly one or the other -- there is nothing ambiguous about the distinction.

The codes section of the encyclopedia contains a reference for a system that maps sequences of short and long signals to letters.

Five birds. Five patterns. Five letters.

---

### Recording 1 -- Chaffinch *(Fringilla coelebs)*

Recorded at forest edge, 06:12. Frequency range 2-6 kHz. Four distinct notes.

```
  kHz
  6 |
    |          ████████
  5 |         ██████████       ███████████████
    |   ██   ███████████      █████████████████
  4 |  ████  ████████████     █████████████████    ██
    |  ████   ██████████       ███████████████     ██
  3 |  ████    ████████                            ██
    |   ██                                         ██
  2 |
    +---+----+----+----+----+----+----+----+----+----+----+---→
    0  0.1  0.2  0.3  0.4  0.5  0.6  0.7  0.8  0.9  1.0  1.1
                           time (seconds)
```

---

### Recording 2 -- Hermit Thrush *(Catharus guttatus)*

Recorded in dense understory, 06:18. Frequency range 2-4 kHz. Four distinct notes with characteristic frequency sweeps.

```
  kHz
  4.0 |
      |                 ████████████████
  3.5 |   ██           ██████████████████
      |  ████   █████████████████████████     ██
  3.0 |  ████  ████████████████████████████   ████
      |  ████   █████████████████████████     ████
  2.5 |   ██           ██████████████████     ████
      |                 ████████████████       ██
  2.0 |
      +---+----+----+----+----+----+----+----+----+----+------→
      0  0.1  0.2  0.3  0.4  0.5  0.6  0.7  0.8  0.9  1.0
                           time (seconds)
```

---

### Recording 3 -- Black-capped Chickadee *(Poecile atricapillus)*

Recorded at feeder station, 06:24. Frequency range 3-5 kHz. Three distinct notes.

```
  kHz
  5 |
    |   ████       ████
  4 |  ██████     ██████         █████████████████
    |  ██████     ██████        ███████████████████
  3 |   ████       ████         ███████████████████
    |                            █████████████████
  2 |
    +---+----+----+----+----+----+----+----+----+----+----→
    0  0.1  0.2  0.3  0.4  0.5  0.6  0.7  0.8  0.9  1.0
                           time (seconds)
```

---

### Recording 4 -- Mourning Dove *(Zenaida macroura)*

Recorded at field edge, 06:31. Frequency range 0.3-0.8 kHz. Two distinct notes, low and resonant.

```
  kHz
  0.8 |
      |  ████████████████████     ███████████████████
  0.7 | ██████████████████████   █████████████████████
      | ██████████████████████   █████████████████████
  0.6 | ██████████████████████   █████████████████████
      | ██████████████████████   █████████████████████
  0.5 |  ████████████████████     ███████████████████
      |
  0.4 |
      |
  0.3 |
      +---+----+----+----+----+----+----+----+----+----+-----→
      0  0.2  0.4  0.6  0.8  1.0  1.2  1.4  1.6  1.8  2.0
                           time (seconds)
```

---

### Recording 5 -- Cedar Waxwing *(Bombycilla cedrorum)*

Recorded overhead in flight, 06:37. Frequency range 6-8 kHz. A single note.

```
  kHz
  8.0 |
      |      ████
  7.5 |     ██████
      |     ██████
  7.0 |     ██████
      |      ████
  6.5 |
      |
  6.0 |
      +---+----+----+----+----+----+----+----+----+----+---→
      0  0.05 0.10 0.15 0.20 0.25 0.30 0.35 0.40 0.45 0.50
                           time (seconds)
```

---

## Worksheet

For each recording, note the number of distinct tones, their relative durations, and the resulting symbol sequence. Then decode.

```
Recording   # Notes   Sequence (brief / sustained)      Decoded letter
─────────   ───────   ──────────────────────────────    ──────────────
  1            4       ___  ___  ___  ___                   [___]
  2            4       ___  ___  ___  ___                   [___]
  3            3       ___  ___  ___                        [___]
  4            2       ___  ___                             [___]
  5            1       ___                                  [___]
```

### Read the answer

```
  ___  ___  ___  ___  ___
   1    2    3    4    5
```

---

**Your answer** (5 letters): _ _ _ _ _

*You may find the Natural World and Language & Communication sections helpful.*
