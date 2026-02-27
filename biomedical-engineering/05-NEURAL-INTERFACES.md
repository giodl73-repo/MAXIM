# Neural Interfaces — Recording and Stimulating the Nervous System

## The Big Picture

Neural interfaces translate between electrical activity of neurons and external devices.
The signal hierarchy spans six orders of magnitude in spatial scale. The fundamental
challenge is the mismatch between rigid silicon electronics and the soft, moving, immunoreactive
brain — the "biotic-abiotic interface problem."

```
+---------------------------------------------------------------------+
|              NEURAL INTERFACE — SIGNAL HIERARCHY                   |
+---------------------------------------------------------------------+
|                                                                     |
|  SINGLE UNIT (SPIKE)   LFP          ECoG          EEG             |
|  Single neuron         Population   Subdural      Scalp            |
|  ~100 μV               ~1 mV        ~1 mV         ~10-100 μV      |
|  ~1 ms duration        1-300 Hz     1-300 Hz      0.1-100 Hz      |
|  400 μm spacing        1-3 mm       1-10 mm       1-10 cm         |
|  (Utah array)          coverage     coverage      coverage        |
|  Intracortical         Intracortical Subdural grid Scalp           |
|  recording             recording    (ECoG)        electrodes       |
|       |                    |            |              |            |
|       +--------------------+------------+--------------+            |
|                            |                                        |
|              RECORDING -> PROCESSING -> DECODING                   |
|              Filtering, spike sorting, feature extraction,         |
|              machine learning decoder, control output              |
|                                                                     |
|              OUTPUT: cursor, prosthetic, communication device      |
+---------------------------------------------------------------------+
```

---

## Neural Signal Characteristics

### Action Potentials

```
  ACTION POTENTIAL
  ================

  Resting potential: -70 mV (inside negative relative to outside)
  Na+ channels closed, K+ channels slightly open.

  Depolarization:
  Stimulus -> Na+ channels open -> Na+ flows in -> membrane
  depolarizes -> positive feedback (Hodgkin-Huxley) -> spike

  +40 mV  |     /\
           |    /  \
           |   /    \
     0 mV  |  /      \
           | /        \
   -70 mV  |/          \___________  (refractory period)
           +------------------------> time (ms)
           |<-- ~1 ms -->|

  EXTRACELLULAR RECORDING:
  Electrode near neuron sees the current sink/source dipole
  -> negative deflection (usually) ~100 μV amplitude
  Signal falls off as 1/r² with distance from neuron
  Recording radius: ~50-100 μm (only nearby neurons contribute)
  -> each electrode records 1-4 well-isolated single units typically
```

### Local Field Potentials (LFP)

```
  LFP — POPULATION ACTIVITY
  ==========================

  Sum of synaptic currents from a local population (~1mm³)
  Dominated by pyramidal neuron dendrites (largest dipoles)
  Not action potentials — subthreshold and synaptic

  FREQUENCY BANDS:
  Band       Frequency    State/Correlation
  -------    ---------    -----------------
  Delta      0.5-4 Hz     Deep sleep, anesthesia
  Theta      4-8 Hz       Hippocampal navigation, working memory
  Alpha      8-12 Hz      Idle (occipital), visual rest
  Beta       12-30 Hz     Motor cortex: anti-correlated with movement
                          DBS targets beta synchrony in Parkinson's
  Gamma      30-100 Hz    Active processing, attention, binding
  High-gamma 100-300 Hz   Broadband, best correlates of cortical activity

  LFP is the dominant signal in ECoG (more signal per electrode than spikes)
  and is used in DBS closed-loop systems (sensing + stimulation same lead)
```

---

## Recording Technologies

### Utah Array

The most commonly used intracortical recording array in human BCI research.

```
  UTAH ARRAY (Blackrock Neurotech)
  =================================

  96 silicon shanks in 10x10 grid (minus 4 corners)
  Shank length: 1.5 mm (cortical layers II-IV)
  Electrode pitch: 400 μm
  Tip coating: iridium oxide or sputtered iridium
  Impedance: 200-800 kΩ at 1 kHz

  PEDOT:PSS or IrOx tip coatings increase charge injection capacity:
  IrOx: ~50-100 μC/cm²
  PEDOT:PSS: >1000 μC/cm² (conducting polymer, compliant)

  +-------+-------+-------+-------+
  |   o   |   o   |   o   |   o   |
  +-------+-------+-------+-------+
  |   o   |   o   |   o   |   o   |  Each dot = electrode
  +-------+-------+-------+-------+  400 μm pitch
  |   o   |   o   |   o   |   o   |
  +-------+-------+-------+-------+
  10x10 grid (96 functional electrodes)

  RECORDING QUALITY:
  Initial implant: high yield, well-isolated units
  Weeks: glial response begins (reactive astrogliosis, microglia)
  Months-years: signal degradation (impedance increase, fewer units)
  Root cause: mechanical mismatch (silicon E ~170 GPa vs brain ~1 kPa)
              + tethering forces from cable + electrode tip trauma

  Chronic recording in humans: Matthew Nagle (BrainGate 2004),
  Jan Scheuermann (multiple years, high quality), participant S3
  (Willett 2021: 90 char/min typing via imagined handwriting)
```

### Neuropixels

High-density silicon probe for rodent research. Not yet in human use, but transforming
systems neuroscience.

```
  NEUROPIXELS 1.0 (IMEC)
  =======================

  960 recording sites on 9.5 mm shank
  Site spacing: 25 μm (vertical), 16-32 μm (horizontal)
  Site size: 12 × 12 μm
  Impedance: ~150 kΩ at 1 kHz
  Record 384 channels simultaneously

  Key advance: record from entire cortical column simultaneously
  + subcortical structures in single penetration

  Drift correction critical: probe moves relative to brain over time
  -> spike sorting algorithms must correct for drift
  (Kilosort 3.0 + 4.0 handle this explicitly)

  Neuropixels 2.0:
  4-shank version, smaller footprint, better chronic recording
  Ultra-high density (80 sites/mm on shank)
```

### Flexible Polymer Probes

```
  FLEXIBLE PROBE APPROACH
  =======================

  Rationale: reduce mechanical mismatch with brain tissue
  Silicon: Young's modulus ~170 GPa
  Polyimide: ~8 GPa
  SU-8: ~4 GPa
  Parylene-C: ~2.8 GPa
  Hydrogels: ~kPa range (approaching brain stiffness)

  Approaches:
  +-------------------+--------------------------------------+
  | Flat flex probes  | Polyimide or Parylene-C shanks       |
  | (Michigan, NeuroPixels flex)                             |
  | Mesh electronics  | Harvard/Lieber lab: injectable mesh  |
  | (injectable)      | becomes structurally integrated      |
  | Syringe-injectable| Thread-like probes (Neuralink)       |
  +-------------------+--------------------------------------+

  NEURALINK N1 IMPLANT:
  64 threads, 1024 electrodes total
  ASIC on skull, BLE transmission
  Autonomous robot for insertion (avoids vasculature)
  First human implant: January 2024 (BCI for paralysis)

  TRADE-OFFS:
  Flexible probes: lower glial response (hypothesis), harder to insert
  Rigid: easy insertion, precise placement, proven long-term in humans
  Active ongoing area: no clear winner for chronic implants yet
```

---

## Electrode-Tissue Interface

The interface between electrode and neural tissue governs signal quality, noise floor, and
stimulation safety.

```
  ELECTRODE-TISSUE INTERFACE PHYSICS
  ====================================

  EQUIVALENT CIRCUIT:
        Rsol (solution resistance)
         |
     Cdl (double-layer capacitance) -- in parallel with Rct
         |
         v
    electrode surface

  Impedance at 1 kHz (measurement standard):
  Lower impedance = better signal conduction = less thermal noise
  Target: <200 kΩ for recording, <1 kΩ for stimulation

  ELECTRODE NOISE:
  Johnson noise: V = sqrt(4kTRΔf)
  k = Boltzmann constant, T = temperature, R = electrode resistance, Δf = bandwidth
  At T=37°C, R=100kΩ, BW=10kHz: ~4 μV RMS (comparable to action potential!)
  -> reduce R (larger electrode or better coating) to improve SNR
  But: larger electrode -> lower spatial resolution (averages more neurons)

  CHARGE INJECTION:
  Stimulation delivers charge to tissue. Exceeding limits -> irreversible
  electrochemical reactions -> tissue damage.
  Safe charge density: Pt/Ir ~0.05-0.3 μC/cm²
  Safe charge per phase: limits derived from McCreery et al. damage model
  Charge-balanced biphasic waveforms required: equal cathodic/anodic charge
  -> no net charge accumulation on electrode or in tissue

  PROTEIN FOULING:
  Serum proteins adsorb to electrode surface -> impedance increases
  PEG coatings reduce fouling but reduce charge injection capacity
  Zwitterionic polymers (pCBMA): anti-fouling + conductive
```

---

## Signal Processing Pipeline

<!-- @editor[bridge/P2]: The pipeline is described step by step but never connected to general DSP concepts the reader knows. Key bridges missing: (1) bandpass filtering = digital FIR/IIR filter design, same Nyquist constraints as any sampled system; (2) 30 kHz sampling rate is chosen so Nyquist frequency (15 kHz) is well above the spike bandwidth (6 kHz), exactly the oversampling principle from DSP; (3) the Kalman filter decoder is the same Kalman filter from control theory/signal processing — state-space model with process noise and observation noise. Adding these one-line bridges would make this section immediately structured for any engineer with DSP background. -->
```
  BCI SIGNAL PROCESSING PIPELINE
  ================================

  RAW SIGNAL (sampled at 30 kHz)
       |
       v
  BANDPASS FILTER
  Spikes: 300-6000 Hz (high-pass removes LFP, low-pass removes noise)
  LFP: 1-300 Hz (or sub-bands as needed)
       |
       v
  THRESHOLD DETECTION (spikes)
  Threshold = k * median(|signal|) / 0.6745  (robust noise estimate)
  k typically 3-5
  Detects potential action potential waveforms
       |
       v
  SPIKE SORTING
  Extract waveform snippets (e.g., 1ms before, 2ms after threshold crossing)
  Dimensionality reduction: PCA, t-SNE, UMAP
  Clustering: k-means, GMM, template matching
  Kilosort (Pachitariu): GPU-accelerated, handles drift
  MountainSort, SpyKING CIRCUS: alternatives
       |
       v
  FEATURE EXTRACTION
  Firing rate: spikes per time bin (often 50-100ms)
  Trajectory: spike rate as function of time
  LFP power in bands (beta, gamma, high-gamma)
       |
       v
  DECODING
  Liner regression / LDA for discrete states
  Kalman filter: state-space model, standard for continuous cursor control
  RNN, LSTM: capture temporal structure in population activity
  Population vector: cosine tuning model (motor cortex)
       |
       v
  OUTPUT
  Cursor position, robotic arm trajectory, speech synthesis, text
```

---

## Brain-Computer Interface Systems

### BrainGate

```
  BRAINGATE — FIRST HUMAN BCI WITH UTAH ARRAY
  =============================================

  2004: Matthew Nagle — first human with Utah array in motor cortex
  Institution: Brown University / Massachusetts General Hospital
  FDA IDE: investigational device (non-commercial)

  Current participants:
  - Cursor control: 2D cursor from motor cortex intent
  - Limb control: direct robotic arm control (Hochberg 2012, Nature)
  - Speech BCI: RNN decoder for phonemes -> text (Willett 2023: 62 words/min)
  - Handwriting BCI: imagined handwriting -> letters (Willett 2021: 90 char/min)

  Limitation: percutaneous cable through skull
  -> infection risk, mobility limitation
  Current work: fully implanted, wireless (BrainGate 2)
```

### Neuralink

```
  NEURALINK N1 IMPLANT
  ====================

  Commercial-track BCI company (Elon Musk, 2016-)
  First human: Noland Arbaugh, January 2024

  HARDWARE:
  N1 implant: 23x8mm titanium can
  64 flexible threads (16 electrodes each = 1024 channels)
  Robot-assisted insertion: avoiding surface vasculature
  Bluetooth Low Energy transmission, inductive charging
  Onboard signal processing (spike detection in implant)

  INITIAL RESULTS (2024):
  Participant with ALS: cursor control, gaming
  Thread retraction issue (~85% of threads retracted initially)
  -> company working on improved fixation
  FDA cleared IDE (investigational)

  vs. BrainGate:
  Neuralink: wireless, fully implanted, more electrodes, private
  BrainGate: academic, decades of data, proven long-term recording
```

---

## Neural Stimulation

### Deep Brain Stimulation (DBS)

```
  DEEP BRAIN STIMULATION
  =======================

  High-frequency electrical stimulation (~130 Hz) via implanted
  electrode inhibits pathological activity in target nuclei.

  ANATOMY (Parkinson's disease targets):
  Subthalamic nucleus (STN): most common, both motor + psychiatric
  Globus pallidus interna (GPi): dyskinesias, dystonia

  DBS HARDWARE:
  Lead: 4-8 electrode contacts, implanted in target nucleus
  Extension cable: subcutaneous, skull to IPG
  IPG (Implantable Pulse Generator): similar to pacemaker
  ~ clavicle pocket, battery 3-5 years (rechargeable 10+ years)

  MECHANISM (still debated):
  Depolarization block? Synaptic depression? Network effects?
  Most evidence: drives output neurons at stimulation frequency
  -> overrides pathological oscillations (4-6 Hz tremor, 13-30 Hz beta sync)

  PROGRAMMING:
  Contact selection (which electrode, mono/bipolar)
  Amplitude (0-10 mA or V)
  Pulse width (60-450 μs)
  Frequency (typically 130 Hz for Parkinson's)

  CLOSED-LOOP DBS (aDBS):
  Problem: conventional DBS is always on -> side effects at
  continuous high stimulation (speech, gait, mood)
  Solution: sense LFP beta power on DBS lead itself
  -> beta elevated: increase stim; beta suppressed: decrease stim
  -> 40-50% less total stimulation, better therapeutic window
  Medtronic Percept PC: FDA cleared for closed-loop DBS (2023)

  INDICATIONS (FDA approved):
  Parkinson's disease (tremor, rigidity, bradykinesia)
  Essential tremor
  OCD (bilateral anterior limb of internal capsule)
  Dystonia (GPi target)
  Epilepsy (anterior thalamus — SANTE trial)
  Under investigation: depression, Alzheimer's, chronic pain
```

### Cochlear Implants

```
  COCHLEAR IMPLANT
  ================

  ANATOMY:
  Cochlea: snail-shaped, 2.5 turns, tonotopic (frequency-place mapping)
  Base: high frequency (20 kHz)
  Apex: low frequency (200 Hz)
  Hair cells: mechano-electric transducers. Damaged in SNHL.

  IMPLANT ARCHITECTURE:
  Microphone -> Processor (external) -> Transmitter coil (external)
  -> Receiver (internal, under skin) -> Electrode array (in cochlea)

  Electrode array: silicone carrier, 12-22 platinum electrodes
  Insertion via round window or cochleostomy
  Length: 25-31 mm (partial or full cochlear insertion)
  Each electrode stimulates different tonotopic location

  SPEECH PROCESSING STRATEGIES:
  CIS (Continuous Interleaved Sampling): dominant current strategy
  Extract frequency bands -> apply amplitude envelope to each channel
  -> stimulate tonotopically corresponding electrode with envelope-modulated pulses
  Channel interaction: current spreads -> activates multiple channels
  -> limits effective number of independent channels to ~8-10 from 22 electrodes

  PERFORMANCE:
  Mean open-set sentence recognition: ~80% (vast range, 20-100%)
  Prelingually deaf: better outcomes with earlier implantation
  Post-lingual adults: typically good outcome
  Music perception: poor (limited frequency resolution)

  FDA APPROVED FOR:
  Adults: profound SNHL bilaterally, limited benefit from hearing aids
  Children: 12 months (some bilateral, under 9 months in trials)
```

### Retinal Prosthetics

```
  RETINAL PROSTHETICS
  ====================

  DISEASE TARGET: photoreceptor degeneration (RP, AMD)
  Inner retinal neurons (bipolar, ganglion cells) remain viable
  -> electrically stimulate inner retina to bypass dead photoreceptors

  ARGUS II (Second Sight Medical Products):
  Only FDA-approved retinal prosthesis (2013, voluntary recall 2023
  when company exited business)
  60-electrode epiretinal array (implanted on inner retina surface)
  External camera -> video processor -> wireless transmitter
  -> inductive link -> ASIC -> stimulate ganglion cells
  Results: patients could detect light, large objects, some mobility

  LIMITATIONS:
  60 electrodes -> extremely coarse visual percept (phosphenes)
  No high-acuity vision — regulatory endpoint was "functional benefit"
  Company bankruptcy (2023) left existing patients without support
  -> highlights long-term device support obligations

  CURRENT RESEARCH:
  Epiretinal (ganglion cell stimulation): larger current, less specific
  Subretinal (bipolar cell stimulation): more anatomically correct
  PRIMA (Pixium Vision): subretinal photovoltaic chip, no external power
  Alpha AMS (Retina Implant AG): 1600 electrodes subretinal, Germany
  Genetically targeted (ChR2/opsins): optogenetic approach, clinical trials
```

---

## Regulatory: IDE for Neural Devices

Neural BCIs are universally Class III (significant risk, invasive in brain) and require
IDE for clinical investigation. No neural BCI device is currently FDA-approved (PMA) for
commercial sale — all are under IDE or cleared only for specific applications.

```
  NEURAL INTERFACE REGULATORY STATUS (2026)
  ==========================================

  BrainGate:       IDE (Investigational) — academic, Brown/MGH
  Neuralink:       IDE cleared 2023, first human 2024
  Synchron Stentrode: IDE cleared 2021 (endovascular, less invasive)
  Medtronic DBS:   PMA approved (Parkinson's, essential tremor)
  Abbott DBS:      PMA approved
  Boston Scientific DBS: PMA approved
  Cochlear Implants: PMA approved (multiple manufacturers)
  Retinal: Argus II PMA approved but company exited

  Key regulatory considerations:
  - Benefit-risk: significant clinical burden + surgical risk justified
    for severe disability (paralysis, blindness, Parkinson's)
  - Post-market obligations: longitudinal follow-up required
  - Software updates to algorithm: potentially a device modification
    requiring regulatory notification or submission
  - Closed-loop systems: stimulation based on sensed signal ->
    additional safety considerations (feedback loop stability)
```

---

## Common Confusion Points

**EEG vs. MEG**: EEG measures the electric potential on the scalp (smeared by skull and scalp).
MEG (magnetoencephalography) measures the magnetic field generated by the same neural currents.
MEG is not affected by head geometry in the same way, giving slightly better spatial localization,
but requires cryogenic superconducting detectors (SQUID) — expensive and not portable. New
optically pumped magnetometers (OPM) enable wearable MEG.

**Single unit vs. multiunit activity**: Spike sorting attempts to assign recorded spikes to
individual neurons (single unit). When sorting is ambiguous, waveforms are combined as multiunit
activity. For BCIs, multiunit activity often works nearly as well as single units (and is more
stable over time) — this was a key insight from early BrainGate work.

**DBS mechanism is not "pacemaker for brain"**: This analogy is used clinically but misleads.
A cardiac pacemaker drives the heart at its exact frequency (heart follows pacemaker). DBS
does not drive the motor system at 130 Hz — 130 Hz stimulation at the STN modulates the
basal ganglia-thalamo-cortical circuit indirectly. The circuit output is not at 130 Hz.

**Cochlear implant channel interaction**: The claimed 22-electrode device provides ~8-10
effective spectral channels due to current spread. Closer electrode spacing would help, but
endocochlear anatomy limits this. Intraneural stimulation and optical cochlear implants (using
light-gated channelrhodopsins) are research directions for better spectral resolution.

**Neural interface "biocompatibility" is a dynamic problem**: ISO 10993 biocompatibility testing
on extract media or in short-term implant tests does not capture the chronic inflammatory
cascade that degrades neural recordings over months to years. Biocompatibility of neural probes
is an active research problem, not a solved one — this is unlike passive orthopedic implants
where decades of osseointegration data exist.

---

## Decision Cheat Sheet

| Need | Technology | Notes |
|---|---|---|
| Research, rodent | Neuropixels | Best spatial density, drift correction needed |
| Clinical BCI (human) | Utah Array (BrainGate) or Neuralink | Proven vs. novel/wireless |
| Non-invasive BCI | EEG (P300, SSVEP, motor imagery) | Lower performance, no surgery |
| Non-invasive BCI, better spatial | ECoG or Synchron Stentrode | Subdural or endovascular |
| Parkinson's therapy | DBS (Medtronic/Abbott/BSci) | FDA approved, closed-loop available |
| Hearing restoration | Cochlear implant | FDA approved, excellent outcomes |
| Vision restoration | Experimental (PRIMA, Orion) | No FDA-approved product currently |
| Kinetics without animal harm | In vitro MEA (multielectrode array) | Culture dish, drug screening |
| Population dynamics, behaving | Neuropixels + calcium imaging | Complementary modalities |
