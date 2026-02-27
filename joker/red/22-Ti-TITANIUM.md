# [22] --- Titanium

**8&#9830; The Verifier** &middot; Technology &middot; T2

---

> The Verifier trusts instruments over intuition. Thirteen peaks arrived on the spectrum analyzer last night. Some carry the message. The rest are echoes. You know the difference. You just need to prove it.

---

## The Puzzle

A monitoring station recorded a burst of audio-frequency tones. The spectrum analyzer captured thirteen discrete peaks between 200 Hz and 1600 Hz. The readout below shows every detected frequency and its measured amplitude.

```
SPECTRUM ANALYZER — CAPTURE 22-Ti
═══════════════════════════════════════════════════════════════════════

 Amplitude
   (dB)
     │
  -6 ┤                          ●δ
     │
  -9 ┤           ●γ
 -10 ┤  ●α
     │
 -12 ┤       ●β
 -14 ┤                                  ●ε
     │
 -16 ┤                                          ●η
     │
     │
     │
     │
     │
 -26 ┤                                                  ●ι
     │
 -29 ┤                                      ●θ
 -30 ┤                      ●ζ
     │
     │
 -34 ┤                                                       ●λ
 -36 ┤                                                           ●μ
     │
     │
     │
 -42 ┤                                                  ●κ
 -44 ┤                                                               ●ν
     │
     └──────┬──────┬──────┬──────┬──────┬──────┬──────┬──────┬──────┬───
          200    400    600    800   1000   1200   1400   1600
                              Frequency (Hz)
```

### Peak Data

```
CAPTURED PEAKS (sorted by frequency)
═══════════════════════════════════════════
Peak    Frequency (Hz)    Amplitude (dB)
─────   ──────────────    ──────────────
  α        293.66             -10
  β        329.63             -12
  γ        349.23              -9
  δ        440.00              -6
  ε        523.25             -14
  ζ        587.33             -30
  η        659.26             -16
  θ        698.46             -29
  ι        880.00             -26
  κ        988.88             -42
  λ       1046.50             -34
  μ       1318.51             -36
  ν       1569.75             -44
═══════════════════════════════════════════
```

The burst contains a message encoded as tones. But the spectrum also contains harmonics — overtones at integer multiples of each tone's frequency, produced naturally by the signal source. The message tones are the fundamentals. The harmonics are noise.

Your job: separate the fundamentals from the harmonics. Then identify each fundamental as a musical note. The note names, read in order from lowest frequency to highest, are the answer.

Three things to find in the encyclopedia:

1. **What is the relationship between a fundamental and its harmonics?** The signal processing and music theory sections both describe the harmonic series. A fundamental at frequency f produces overtones at 2f, 3f, 4f, and so on. Higher harmonics carry less energy than the fundamental.

2. **How much less energy?** Look at the pairs you can identify. The pattern in the data will tell you what "normal" looks like — and what doesn't.

3. **How do frequencies become note names?** The music theory section maps frequencies to the notes of the Western scale. The reference pitch A₄ = 440 Hz is your anchor. Every other note has a known frequency relative to it.

One peak in this spectrum is not what it first appears to be.

---

## Worksheet

### Step 1 — Find the Harmonic Pairs

Check every pair of peaks for an exact 2:1 or 3:1 frequency ratio. Fill in the relationships you find.

```
HARMONIC RELATIONSHIPS
═══════════════════════════════════════════════════════════════════
Higher peak    Lower peak    Ratio    Relationship
───────────    ──────────    ─────    ─────────────────────────
___________    __________    2 : 1    2nd harmonic of __________
___________    __________    2 : 1    2nd harmonic of __________
___________    __________    2 : 1    2nd harmonic of __________
___________    __________    2 : 1    2nd harmonic of __________
___________    __________    2 : 1    2nd harmonic of __________
___________    __________    2 : 1    2nd harmonic of __________
___________    __________    3 : 1    3rd harmonic of __________
___________    __________    3 : 1    3rd harmonic of __________
═══════════════════════════════════════════════════════════════════
```

### Step 2 — Check the Amplitudes

For each 2:1 pair, record the amplitude gap between the lower-frequency peak and the higher-frequency peak. What is the typical gap?

```
AMPLITUDE ANALYSIS
═══════════════════════════════════════════════════════════════
Lower peak     Its dB    Upper peak    Its dB    Gap (dB)
──────────     ──────    ──────────    ──────    ────────
__________     ______    __________    ______    ________
__________     ______    __________    ______    ________
__________     ______    __________    ______    ________
__________     ______    __________    ______    ________
__________     ______    __________    ______    ________
__________     ______    __________    ______    ________

Typical gap for a 2nd harmonic: ______ dB

Which pair breaks the pattern?  ________ / ________

What does that tell you?  _______________________________________
═══════════════════════════════════════════════════════════════
```

### Step 3 — Identify the Fundamentals

List only the peaks that are message tones (fundamentals, not harmonics). Read from lowest frequency to highest.

```
FUNDAMENTALS
═══════════════════════════════════════════════════════
Peak    Frequency (Hz)    Note name    Letter
────    ──────────────    ─────────    ──────
____    ______________    _________    [___]
____    ______________    _________    [___]
____    ______________    _________    [___]
____    ______________    _________    [___]
____    ______________    _________    [___]
____    ______________    _________    [___]
═══════════════════════════════════════════════════════
```

---

**Your answer** (6 letters): _ _ _ _ _ _

*You may find the Technology and Arts & Culture sections helpful.*
