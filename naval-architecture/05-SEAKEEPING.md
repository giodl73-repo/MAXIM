---
maxim_schema: maxim.frontmatter.v1
id: maxim:naval-architecture:seakeeping
kind: guide
module: naval-architecture
section: naval-architecture
title: Seakeeping
status: source-custody
source_custody: partial
current_path: naval-architecture/05-SEAKEEPING.md
canonical_path: naval-architecture/05-SEAKEEPING.md
backsource_ids: [proof-backfill:naval-architecture:05-seakeeping, git-history:naval-architecture:05-seakeeping]
concepts: [seakeeping, ship motions, response amplitude operator, slamming, roll stabilization, resonance]
root_concepts: [seakeeping]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Seakeeping

## The Big Picture

Hydrostatics [01] treats the ship at rest in calm water. Seakeeping treats the ship as a
*dynamic* system being shaken by waves. A floating body is a mass on a spring (buoyancy is
the spring) with damping (it radiates waves), driven by an irregular forcing function (the
seaway). The whole field is the theory of a damped, driven oscillator — extended to six
degrees of freedom and a random input. For a reader fluent in linear systems and Fourier
analysis, seakeeping is the most familiar territory in this module: it is signals and
systems applied to a hull.

```
SEAKEEPING = A DAMPED, DRIVEN OSCILLATOR (x6 degrees of freedom)
===============================================================================

   THE SEA (random waves)         THE SHIP (a 6-DOF dynamic system)
   ----------------------         --------------------------------
   irregular wave elevation       mass-spring-damper in each mode:
   = sum of many regular waves      mass  = inertia + added mass
   (a spectrum S(omega))            spring= buoyancy / metacentric restoring
        |                           damping= wave radiation + viscous
        v                                |
   .----------.      transfer       .----------.      .-------------.
   | WAVE     | --- function ----> | SHIP     | --->  | MOTIONS:    |
   | SPECTRUM |     (the RAO)       | DYNAMICS |      | heave,roll, |
   | S_wave(w)|                     |          |      | pitch ...   |
   '----------'                     '----------'      '-------------'

   OUTPUT spectrum = |RAO(w)|^2 x INPUT spectrum   (linear superposition)
   S_motion(w) = |RAO(w)|^2 x S_wave(w)
```

That last line is the entire workflow: decompose the sea into a spectrum, multiply by the
ship's transfer function (the RAO), and read off the motion statistics. It is the input →
transfer-function → output pipeline, exactly as in linear systems theory.

---

## Layer 1: The Six Degrees of Freedom

A rigid ship in the sea has six rigid-body motions — three translations and three
rotations. Three are *restored* (they have a stiffness and oscillate); three are *free*
(no restoring force, the ship just drifts).

```
THE SIX SHIP MOTIONS (6-DOF)
===============================================================================

                        z (up)
                        |   yaw (about z)
                        |  /
                        | /
            roll <------+------> (about x, longitudinal)
           (about x)   /|
                      / |
                 surge  |  y (transverse)
            x ---------- pitch (about y)
         (forward)

   +----------+-----------+----------------------------+--------------+
   | Motion   | Type      | Restoring force?           | Matters for  |
   |----------|-----------|----------------------------|--------------|
   | SURGE    | translate | NO (free) - x, fore/aft    | added resist.|
   | SWAY     | translate | NO (free) - y, sideways    | maneuvering  |
   | YAW      | rotate z  | NO (free) - heading change | course-keep  |
   |----------|-----------|----------------------------|--------------|
   | HEAVE    | translate | YES - buoyancy spring (z)  | comfort,deck |
   | ROLL     | rotate x  | YES - GM x displacement    | comfort,cargo|
   | PITCH    | rotate y  | YES - long. GM (huge)      | slamming,bow |
   +----------+-----------+----------------------------+--------------+
```

The three *restored* motions — **heave, roll, pitch** — are oscillators with natural
frequencies, and they are where seakeeping does its work. The three *free* motions — surge,
sway, yaw — have no restoring stiffness and are handled by maneuvering and control, not
oscillation theory. (Roll is the troublesome one: its restoring spring is the GM from
[01], and GM is small, so roll is lightly stiffened and lightly damped — a recipe for large
resonant response.)

---

## Layer 2: Each Motion Is a Mass-Spring-Damper

Take heave as the cleanest example. The vertical equation of motion is a textbook damped
oscillator, with two marine twists: **added mass** and **wave-radiation damping**.

```
HEAVE AS A DAMPED OSCILLATOR
===============================================================================

   (m + a) z'' + b z' + c z  =  F(t)
    \___/      |     |          |
   inertia   damping spring   wave forcing
   + ADDED              \
     MASS                c = rho x g x A_w  (waterplane area = the spring rate)
        \
         a = ADDED MASS: water that must be accelerated WITH the hull.
             A ship heaving drags a slug of surrounding water along; its
             inertia ADDS to the ship's own. Can be ~the ship's own mass.

   b = RADIATION DAMPING: the ship makes waves as it heaves; that radiated
       wave energy is lost from the motion -> damping. (Plus viscous damping.)

   Natural frequency:  omega_n = sqrt( c / (m + a) )
```

Two ideas a dynamics reader should pin down:

- **Added mass** is not a fudge; it is the kinetic energy of the entrained fluid expressed
  as an effective inertia. It can roughly equal the ship's own mass, so it shifts natural
  frequencies substantially. (It is the hydrodynamic cousin of the effective-mass terms in
  any fluid-loaded oscillator.)
- **Radiation damping** is the *useful* damping: the ship dumps motion energy into radiated
  waves. Roll, however, radiates very weakly (a rolling hull is a poor wavemaker), so roll
  damping is small and mostly viscous — which is exactly why roll needs help (Layer 5).

The roll and pitch natural periods follow the same form:

```
   Roll natural period:   T_roll  ~  2pi x k_xx / sqrt(g x GM)
        k_xx = roll radius of gyration (~0.35-0.40 B). Note 1/sqrt(GM):
        a STIFF ship (big GM) has a SHORT, snappy roll period.
   Pitch natural period:  T_pitch ~ similar form with longitudinal GM_L,
        which is huge -> pitch is much stiffer and shorter-period than roll.
```

---

## Layer 3: The Response Amplitude Operator (RAO)

The **RAO** is the ship's transfer function: for a regular wave of unit amplitude at
frequency ω (and a given heading), it gives the amplitude (and phase) of each motion. It is
the marine name for |H(ω)| — the frequency response of the hull-as-oscillator.

```
A ROLL RAO (transfer function of the ship in roll)
===============================================================================

  roll
  amplitude
  per wave  |
  slope     |              /\  <- RESONANCE PEAK at omega = omega_n_roll
  (deg/m)   |             /  \    (wave encounter period = roll natural period)
            |            /    \   height of peak set by DAMPING (low damping
            |           /      \   = tall sharp peak = dangerous)
            |          /        \
            |   ______/          \________
            |  /                          \_____
            | /                                  ----____
            +----------------------------------------------> encounter freq w_e
            0      low freq (long waves):       high freq (short waves):
                   ship follows the wave        ship can't respond, RAO -> 0
                   like a cork, RAO -> 1
```

Three regimes, exactly as for any second-order system:

| Regime | Wave vs. ship | Behavior |
|--------|---------------|----------|
| Low frequency (long waves) | Wave ≫ ship period | Ship rides the wave like a cork; RAO → 1 (it just follows the surface) |
| Resonance (ω_e ≈ ω_n) | Encounter period = natural period | RAO peaks — the dangerous regime; magnification set by damping |
| High frequency (short waves) | Wave ≪ ship period | Ship too sluggish to respond; RAO → 0 |

The **encounter frequency** ω_e is what the moving ship actually feels, Doppler-shifted by
its own speed and heading. Steaming into the waves raises ω_e; running with them lowers it.
This is operationally huge: a captain can dodge roll resonance by **changing speed or
heading** to move ω_e off the roll natural frequency — tuning the forcing frequency away
from the system's resonance, in real time.

```
   Encounter frequency (the Doppler shift the ship feels):
        omega_e = omega - (omega^2 / g) x V x cos(mu)
        mu = heading angle (0 = following seas, 180 = head seas)
        -> head seas (mu=180): omega_e INCREASES (waves hit faster)
        -> following seas (mu=0): omega_e DECREASES (can even go to ~0)
```

> Old world -> new world bridge. The RAO is |H(jω)|, the magnitude of a transfer function;
> resonance is a lightly-damped pole; the encounter frequency is a Doppler shift on the
> input. Predicting motions is `output spectrum = |H|² × input spectrum` — Wiener-Khinchin
> applied to a hull. A reader from signal processing already owns the entire mathematical
> machinery of seakeeping; only the vocabulary (RAO, added mass, encounter frequency) is new.

---

## Layer 4: From Regular Waves to the Real Sea — Spectra

The real ocean is irregular, but (to first order) it is a *linear superposition* of regular
waves — a random Gaussian process described by a **wave spectrum** S(ω) giving the energy at
each frequency. Standard spectra (Pierson-Moskowitz for fully-developed seas, JONSWAP for
fetch-limited) are parameterized by significant wave height and period.

```
THE SEAKEEPING WORKFLOW (linear, spectral)
===============================================================================

   WAVE SPECTRUM            RAO (ship transfer fn)        MOTION SPECTRUM
   S_wave(omega)      x        |RAO(omega)|^2        =    S_motion(omega)
   (energy vs freq)         (response vs freq)            (motion energy)

      /\                         /\                            /\
     /  \  many                 /  \ resonance               /  \ motion
    /    \ frequencies   --->   /    \ filter        --->    /    \ concentrated
   /______\ in the sea        _/      \_                   _/      \_ near where
                                                              wave x RAO overlap

   Then INTEGRATE the motion spectrum for statistics:
     area m0 = variance -> significant motion = 4 x sqrt(m0)
     (e.g. significant roll amplitude, probability of exceeding a limit)
```

This is the payoff of linearity: you never have to time-simulate a storm. Multiply the wave
spectrum by |RAO|², integrate, and out come the motion statistics — significant roll, RMS
vertical acceleration, the probability of slamming this hour. **Significant** anything (wave
height, roll) is conventionally the mean of the highest third, ≈ 4√(variance). The whole
edifice rests on superposition holding; in extreme seas the response goes nonlinear and you
fall back to direct simulation or model tests.

---

## Layer 5: The Nasty Nonlinear Events — Slamming, Green Water, Parametric Roll

Linear theory predicts comfort and fatigue loads. The *dangerous* events are nonlinear.

```
THE THREE VIOLENT EVENTS
===============================================================================

  SLAMMING                 GREEN WATER              PARAMETRIC ROLL
  --------                 -----------              ---------------
  bow lifts clear in       a wave boards the        head/following seas, no
  pitch, then crashes      deck (not spray --        beam wave at all, yet
  down onto the next       solid "green" water)      the ship rolls violently
  wave: huge impact        sweeping the deck

  bow ___                  wave over the bow         restoring GM PULSATES as
     \  out of water       ~~~~~/~~~~ floods         the wave crest/trough moves
      \                    over deck                 along the hull -> GM(t).
   ~~~~\~~~  SLAM down ->                            If GM oscillates at ~2x the
        |   #IMPACT#       damages hatches,          roll natural freq, energy
        v                  containers, fittings      pumps INTO roll -> blow-up
   peak pressure can                                 (Mathieu-equation instability)
   exceed 10 bar
```

Three failure modes worth knowing precisely:

- **Slamming.** In head seas the bow emerges and re-enters, generating an impulsive
  pressure (whipping the hull girder — a transient that excites the structural modes of
  [04]). Mitigated by reducing speed ("voluntary speed loss") and by flare/bow design.
- **Green water.** Solid water on deck, not spray — heavy and destructive. Drives
  freeboard, hatch-cover strength, and forecastle design.
- **Parametric roll.** The subtle one. In head or following seas with no beam excitation,
  the **GM itself oscillates** as crests and troughs pass (the waterplane changes), at
  roughly twice the roll frequency. This is a **Mathieu-equation parametric instability** —
  energy is pumped into roll from the heave/pitch input, and roll can grow to 40° from
  nothing. It famously hit a post-Panamax containership (APL China, 1998) and is now a
  required check. A dynamical-systems reader will recognize it instantly as parametric
  resonance: the *coefficient* of the oscillator, not the forcing, is being modulated.

> Old world -> new world bridge. Parametric roll is the swinging-child-on-a-swing
> phenomenon — you pump energy in by changing the *system parameter* (effective pendulum
> length, here GM) at twice the natural frequency, not by pushing at the natural frequency.
> It is the Mathieu equation, the same parametric instability seen in `dynamical-systems/`.
> Ordinary resonance excites at ω_n; parametric resonance excites by modulating a coefficient
> at 2ω_n — which is why it can blow up even when there is no direct rolling moment at all.

---

## Layer 6: Stabilization — Fighting Roll

Roll is the motion that ruins comfort, shifts cargo, and (at worst) capsizes. Because roll
is lightly damped, small added damping or counter-moment makes a large difference at
resonance. The toolkit:

| Stabilizer | How it works | Trade-off |
|------------|--------------|-----------|
| Bilge keels | Long fins along the bilge add viscous damping | Cheap, passive, always-on; small drag; ~30% roll cut |
| Anti-roll tanks | Water in a tank sloshes out of phase with roll | Works at zero speed; costs space/weight; tuned to T_roll |
| Active fins | Retractable wings generate counter-moment via lift | Strong; need forward speed; cost, complexity |
| Gyroscopic | Spinning flywheel precesses to oppose roll | Good at zero speed (yachts); heavy, power-hungry |
| Rudder roll stabilization | High-speed rudder use induces counter-roll | Free hardware; couples with steering |

Bilge keels are nearly universal because they are passive, cheap, and add the scarce
commodity — roll damping — at the resonance where it matters most. Anti-roll tanks and
gyros work at *zero speed* (cruise ships at anchor, yachts), where speed-dependent fins are
useless. The choice maps directly onto the RAO: damping devices lower and broaden the
resonant peak; tuned tanks add a second absorber mode that splits the peak — the marine
form of a tuned-mass damper.

---

## Worked Example: Roll Resonance and Tuning Out of It

A ferry with GM = 1.2 m, beam B = 22 m, roll radius of gyration k = 0.38·B. Find its roll
natural period, then show how the captain avoids resonance in a beam swell of period 8 s.

```
   STEP 1 -- roll radius of gyration:
     k_xx = 0.38 x 22 = 8.36 m

   STEP 2 -- roll natural period:
     T_roll = 2 pi x k_xx / sqrt(g x GM)
            = 2 pi x 8.36 / sqrt(9.81 x 1.2)
            = 52.5 / sqrt(11.77) = 52.5 / 3.43 = 15.3 s

   STEP 3 -- the threat:
     A beam swell of period 8 s. In BEAM seas (mu = 90 deg) the ship is not
     moving relative to the wave crests, so encounter period ~ wave period
     ~ 8 s. That is well off the 15.3 s natural period -> little roll. Good.

   STEP 4 -- the trap (why heading matters):
     Suppose instead a long swell of 15 s period in QUARTERING seas. The
     encounter period could stretch toward T_roll = 15.3 s -> RESONANCE ->
     violent roll. The fix:

   STEP 5 -- tune out of resonance (operational control):
     Change HEADING (alter mu) or SPEED (alter V) to shift the encounter
     period away from 15.3 s:
        omega_e = omega - (omega^2/g) V cos(mu)
     Increasing speed or turning toward head seas RAISES omega_e (shortens
     encounter period), pulling the forcing off the roll resonance.

   STEP 6 -- note on GM (links to [01]):
     A STIFFER ship (raise GM) shortens T_roll (T ~ 1/sqrt(GM)) -- but a
     short snappy roll is uncomfortable and high-acceleration. Stability and
     seakeeping pull GM in OPPOSITE directions: [01] wants enough GM for
     safety, [05] wants it modest for a long, gentle roll. The design spiral
     [00] arbitrates.
```

The structural insight: roll safety is not only a hardware problem (stabilizers) but a
*control* problem — the master detunes the forcing frequency from the system's resonance by
changing speed and heading, in real time, exactly as you would move an excitation off a
lightly-damped pole.

---

## Common Confusion Points

### A stiff ship (high GM) is not a comfortable ship

```
   HIGH GM:  short roll period, fast snappy roll, HIGH accelerations
             -> safe against capsize but miserable and cargo-damaging
   LOW GM:   long roll period, gentle slow roll, low accelerations
             -> comfortable but closer to the stability margin
```

Stability [01] and seakeeping [05] want opposite GM. The design is a compromise, not a
maximization — the same Goldilocks point flagged in [01].

### Resonance is about encounter frequency, not wave frequency

What matters is the wave frequency *as the moving ship experiences it* (ω_e), which depends
on the ship's speed and heading. The same ocean swell can be benign or catastrophic
depending purely on course and speed. This is why "change course and slow down" is the
universal heavy-weather response.

### Parametric roll happens with no beam waves at all

Ordinary roll needs a sideways wave force. Parametric roll needs *none* — it is driven by
the GM oscillating (a parameter changing) in head or following seas. Crews unaware of it
have been blindsided by 40° rolls while steaming directly into the waves with no beam
excitation present.

### Added mass is real inertia, not a correction factor

The "added mass" is the entrained water the hull must accelerate with it; it genuinely
changes the natural frequency and can equal the ship's own mass. Ignoring it gives natural
periods that are wrong by tens of percent.

---

## Decision Cheat Sheet

| I want to... | Use |
|---|---|
| Model ship motion in waves | 6-DOF; heave/roll/pitch as damped oscillators |
| Get a motion's natural frequency | ω_n = √(c/(m+a)), include added mass |
| Get the ship's transfer function | RAO = motion amplitude per unit wave |
| Find what frequency the ship feels | Encounter frequency ω_e (Doppler) |
| Predict motions in a real sea | S_motion = \|RAO\|²·S_wave, then integrate |
| Avoid roll resonance | Change speed/heading to shift ω_e off ω_n_roll |
| Reduce roll, passively | Bilge keels (damping); anti-roll tank (tuned) |
| Reduce roll, actively | Active fins (need speed); gyro (zero speed) |
| Guard against bow impact loads | Slamming check; voluntary speed loss |
| Guard against parametric roll | Mathieu stability check in head/following seas |
| Review the GM that sets the roll spring | guide [01] Hydrostatics & Stability |
| Review the hull-girder whipping from slams | guide [04] Ship Structures |
