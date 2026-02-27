# Sports Science — Landscape and Taxonomy

## The Big Picture

Sports science is the application of scientific disciplines to athletic performance, health, and injury prevention. It is fundamentally a systems optimization problem: the human body as a complex adaptive system being tuned for a specific output.

```
SPORTS SCIENCE DISCIPLINES:

  +------------------+   +------------------+   +------------------+
  | EXERCISE         |   | BIOMECHANICS     |   | SPORTS           |
  | PHYSIOLOGY       |   |                  |   | PSYCHOLOGY       |
  |                  |   |                  |   |                  |
  | Energy systems   |   | Force analysis   |   | Motivation       |
  | VO2max           |   | Movement patterns|   | Anxiety          |
  | Lactate threshold|   | Injury mechanics |   | Flow state       |
  | Muscle fiber     |   | Equipment design |   | Mental skills    |
  +------------------+   +------------------+   +------------------+
          |                      |                      |
          +------------- --------+------------- --------+
                                 |
          +------------------+   |   +------------------+
          | STRENGTH &       |   |   | SPORTS NUTRITION |
          | CONDITIONING     |<--+-->|                  |
          |                  |       | Macronutrient    |
          | Periodization    |       | timing           |
          | Force-velocity   |       | Ergogenic aids   |
          | Neuromuscular    |       | Energy systems   |
          +------------------+       +------------------+
                    |
          +------------------+   +------------------+
          | SPORTS MEDICINE  |   | MEASUREMENT &    |
          |                  |   | TECHNOLOGY       |
          | Injury prevention|   | GPS; wearables   |
          | Rehabilitation   |   | Force plates     |
          | Return to sport  |   | Video analysis   |
          +------------------+   +------------------+
```

---

## The Performance Optimization Pipeline

```
ATHLETE DEVELOPMENT PATHWAY:

  TALENT IDENTIFICATION          DEVELOPMENT              COMPETITION
  +------------------+          +------------------+      +------------------+
  | Genetic screens  |          | Training load    |      | Periodization    |
  | Physical testing |---->     | management       |--+-> | Taper            |
  | Early screening  |          | Technical dev.   |  |   | Race/game plan   |
  | Youth programs   |          | Psychological    |  |   | Recovery between |
  +------------------+          | development      |  |   | events           |
                                 +------------------+  |   +------------------+
                                                       |
                                                       v
                                              RECOVERY
                                              +------------------+
                                              | Sleep            |
                                              | Nutrition        |
                                              | Physiotherapy    |
                                              | Load monitoring  |
                                              +------------------+

KEY INSIGHT: The gap between talent and elite performance is primarily
training quality and accumulated load management over years.
Genetics sets the ceiling; training determines how close you get to it.
```

---

## How Sports Science Connects to Medicine and Public Health

```
CONTINUUM FROM HEALTH TO PERFORMANCE:

  POPULATION HEALTH          CLINICAL EXERCISE         SPORTS PERFORMANCE
  (public health goals)      (rehabilitation)          (elite optimization)
  +------------------+       +------------------+      +------------------+
  | Reduce chronic   |       | Cardiac rehab    |      | Maximise VO2max  |
  | disease risk     |       | Cancer rehab     |      | Optimise lactate |
  | 150 min/week     |       | Diabetes mgmt    |      | threshold        |
  | moderate PA      |       | Weight mgmt      |      | Injury prevention|
  +------------------+       +------------------+      +------------------+

  Same physiology. Different dose and context.
  Exercise science principles apply across the entire continuum.

MILITARY READINESS CONNECTION:
  Military physical testing and training draws directly from sports science.
  Load management, heat acclimatization, combat fitness testing,
  overtraining prevention — all use sports science principles.
  US Army Physical Fitness Test → ACFT redesign: sports scientists involved.
```

---

## The Professionalization of Coaching

```
COACHING HISTORY:
  Pre-1970s: intuition-based coaching.
    "More is better." "Pain is weakness leaving the body."
    Training: run more, lift more, push through fatigue.
    Recovery: ignored or considered weakness.

  1970s–80s: Soviet/East Bloc periodization science.
    Matveyev's periodization (1964, published) becomes Western knowledge.
    Systematic load management; supercompensation theory.
    Sports science departments in universities expand.

  1990s–2000s: evidence-based sports science.
    Randomized controlled trials applied to training interventions.
    Heart rate monitors, power meters (cycling: 1989, SRM).
    GPS in team sports (early 2000s in rugby/soccer).
    The "moneyball" moment: data shows intuition was often wrong.

  2010s–2020s: data revolution.
    Player tracking in all major sports (cameras + wearables).
    Machine learning applied to player monitoring and tactics.
    Wearable physiological monitors (HRV, lactate, oxygen saturation).
    The challenge: too much data; interpretation expertise scarce.
```

---

## The Measurement Revolution

```
MEASUREMENT TECHNOLOGY EVOLUTION:

  Technology         Capability                    Adopted
  ─────────────────────────────────────────────────────────────────
  HR monitor         Heart rate (resting + exercise) 1977 (Polar)
  Power meter (bike) Actual mechanical output (W)    1989 (SRM)
  GPS                Position, speed, distance       Early 2000s
  Accelerometer      3D acceleration (load)          2005+
  Force plate        Ground reaction forces          1980s (lab);
                                                      portable 2010s
  Video (2D)         Joint angles, kinematics        1990s (routine)
  3D motion capture  Full 3D kinematics              1990s (lab)
  Markerless 3D      3D without marker suit          2015+
  Lactate analyzer   Blood lactate (capillary sample) 1980s (lab);
                                                       portable 1990s
  HRV logger         Heart rate variability          Smartphone era
  Inertial sensors   IMU-based load in clothing      2010s
  ─────────────────────────────────────────────────────────────────

  THE ENGINEERING PARALLEL:
  Sports science has the same data collection problem as software
  observability: we can now instrument everything, but the signal-to-noise
  ratio is low and interpretability is the bottleneck.
  A team producing 50,000 GPS data points per player per training session
  needs the same abstraction principles as distributed systems observability:
  summarize, threshold, alert, drill-down.
```

---

## Directory Map

| File | Topic |
|------|-------|
| 01-EXERCISE-PHYSIOLOGY.md | Energy systems: PCr, glycolysis, oxidative; fiber types; metabolic adaptation |
| 02-VO2MAX.md | VO2max, Fick equation, lactate threshold, polarized training |
| 03-STRENGTH-POWER.md | Neuromuscular adaptation, force-velocity, periodization of strength |
| 04-BIOMECHANICS.md | Kinematics vs. kinetics, GRF, gait analysis, wearables |
| 05-TRAINING-PERIODIZATION.md | Matveyev, block periodization, load monitoring, overtraining |
| 06-NUTRITION-PERFORMANCE.md | Macronutrient periodization, creatine, caffeine, RED-S |
| 07-DOPING.md | EPO, anabolic steroids, biological passport, WADA detection |
| 08-SPORTS-PSYCHOLOGY.md | Flow state, arousal, anxiety, self-efficacy, mental skills |
| 09-REHABILITATION.md | Tissue healing, ACL, concussion, return-to-sport criteria |

---

## Engineering Bridges

Sports science is applied physics, applied chemistry, and applied control theory
operating on a biological plant. If you already know the engineering, you already
know 80% of the sports science — the rest is domain-specific measurement and
biological variability.

### Biomechanics = Applied Newtonian Mechanics

```
BIOMECHANICS MAPPING

  Classical Mechanics         Biomechanics Application
  ──────────────────────────────────────────────────────────────────
  F = ma                      Ground reaction force analysis:
                              force plate measures F; body mass is m;
                              acceleration determines jump height,
                              sprint force, landing impact

  Torque = r × F              Joint moments: how hard a muscle must
                              pull (F) at its insertion distance (r)
                              to produce movement. Short moment arm
                              = muscle must generate more force.

  Impulse = F × Δt            Why sprinters need high force AND short
                              ground contact time. Impulse determines
                              velocity change; elite sprinters minimize
                              Δt while maximizing F.

  Work = F · d                Mechanical efficiency of movement:
                              metabolic energy in vs. mechanical work
                              out. Running economy = how many mL O₂
                              per km — the "miles per gallon" of gait.

  Free body diagram           Every joint analysis in biomechanics IS
                              a free body diagram: forces at insertion,
                              joint reaction force, gravity, external load.
  ──────────────────────────────────────────────────────────────────
```

### VO2max as Metabolic Efficiency

```
THE METABOLIC ENGINE

  Metabolic model:
    Chemical energy (food) → ATP → Mechanical work + Heat

  VO2max = maximum rate of O₂ consumption (mL/kg/min)
         = maximum aerobic power output of the metabolic engine

  Fick equation:  VO2 = HR × SV × (a-v)O₂ diff
                        ──────────   ────────────
                        Cardiac      O₂ extraction
                        output       efficiency
                        (pump rate)  (tissue utilization)

  Engineering analog:
    Cardiac output   = flow rate through the system (L/min)
    (a-v)O₂ diff     = extraction efficiency at the load (tissue)
    VO2max           = max throughput of the aerobic pipeline

  A 70kg elite cyclist at VO2max ~80 mL/kg/min produces ~400W.
  Gross efficiency ≈ 22-25%. The rest is heat.
  Same thermal management problem as any power system:
  the body's radiator (evaporative cooling via sweat) is the
  performance limiter in hot environments.
```

### Periodization as Control Theory

```
TRAINING AS A CONTROL SYSTEM

  ┌──────────┐     ┌──────────────┐     ┌──────────────┐
  │ TRAINING │     │   ATHLETE    │     │ PERFORMANCE  │
  │ LOAD     │────>│   (PLANT)    │────>│ OUTPUT       │
  │ (input)  │     │              │     │ (measured)   │
  └──────────┘     └──────────────┘     └──────┬───────┘
       ^                                       │
       │           ┌──────────────┐            │
       └───────────│  COACH       │<───────────┘
                   │  (CONTROLLER)│
                   └──────────────┘

  Control Theory Term        Sports Science Equivalent
  ──────────────────────────────────────────────────────────────
  Input signal               Training load (volume × intensity)
  Plant                      Athlete's physiology
  Output                     Performance (race time, power, speed)
  Transfer function          Dose-response: how load → adaptation
  Feedback                   Testing, monitoring (HRV, lactate, RPE)
  Setpoint                   Target performance / race goal
  Gain too high              Overtraining: system driven past
                             stability — performance crashes,
                             immune suppression, mood disturbance
  Gain too low               Undertraining: insufficient stimulus,
                             no adaptation, plateau
  Time constant              Adaptation latency: aerobic base takes
                             6-8 weeks; neural strength gains 2-4 wks
  Supercompensation          Overshoot in the step response:
                             performance temporarily exceeds baseline
                             after recovery from a training block
  ──────────────────────────────────────────────────────────────

  Matveyev's periodization (1964) is a manually designed input
  waveform: ramp load for 3 weeks, deload for 1 week, repeat with
  higher amplitude. Block periodization concentrates one quality
  per mesocycle — the equivalent of training one degree of freedom
  at a time rather than exciting the whole system simultaneously.
```

### Acute:Chronic Workload Ratio as a Moving Average Filter

```
ACWR SIGNAL PROCESSING

  Acute load  = this week's total load (the "now" signal)
  Chronic load = rolling 4-week exponentially weighted moving average

  ACWR = acute / chronic

  ┌──────────────────────────────────────────────────────┐
  │  ACWR    │  Zone          │  Interpretation          │
  │──────────│────────────────│──────────────────────────│
  │  < 0.8   │  Undertraining │  Insufficient stimulus   │
  │  0.8–1.3 │  Sweet spot    │  Progressive overload    │
  │  > 1.5   │  Danger zone   │  Spike: injury risk ↑↑   │
  └──────────────────────────────────────────────────────┘

  This is exactly a ratio of a short-window MA to a long-window MA.
  Same structure as a MACD crossover in finance or a moving average
  convergence detector in signal processing.

  When acute >> chronic, the system has been shocked with a step input
  it hasn't been conditioned for. The biological equivalent of
  resonance: tissue fatigue accumulates faster than repair.

  Limitation: ACWR treats all load as fungible. Running load and
  swimming load stress different tissues. A composite ACWR can mask
  tissue-specific overload — same problem as aggregating heterogeneous
  metrics in any monitoring system.
```

---

## Decision Cheat Sheet

### Quick Reference

| Question | Answer |
|----------|--------|
| What are the three energy systems in order? | PCr (0-10s), glycolytic (10s-2min), oxidative (>2min) |
| What limits VO2max? | Central (cardiac output) and peripheral (O2 extraction) |
| What is the best predictor of endurance performance? | Lactate threshold (not VO2max) when comparing trained athletes |
| What is the most evidence-supported ergogenic aid? | Creatine monohydrate |
| What is "polarized training"? | ~80% training below LT1, ~20% above LT2; Seiler's model |
| What is the biological passport? | Longitudinal athlete biomarker profile used to detect doping manipulation |
| What is flow state in sport? | Csikszentmihalyi's "zone": challenge-skill balance -> effortless performance |
| What is the acute:chronic workload ratio? | Current week load / rolling 4-week average; >1.5 = injury risk spike |

### Which Metric for Which Sport?

```
METRIC SELECTION BY SPORT TYPE

  Metric             Best For                    Less Useful For
  ──────────────────────────────────────────────────────────────────
  VO2max             Endurance ceiling:           Already-elite endurance
  (mL/kg/min)        rowing, XC skiing,           athletes (LT matters
                     distance running             more at that level)

  Lactate threshold  Sustained-effort events:     Short-burst sports
  (speed/power       marathon, cycling TT,        (sprints, weightlifting)
   at LT2)           triathlon, 10K+

  Power-to-weight    Cycling (climbing),          Flat-ground or water
  (W/kg)             running (hills),             sports where weight
                     any gravity-dependent sport  is not penalized

  Peak power output  Sprinting, jumping,          Endurance events
  (Watts)            throwing, weightlifting       (wrong energy system)

  Rate of force      Ballistic sports: baseball   Steady-state endurance
  development (N/s)  pitch, golf drive, shot put

  Ground contact     Sprinting, middle-distance   Non-running sports
  time (ms)          running; shorter = better

  Heart rate         General load monitoring;     Poor proxy for actual
  variability (HRV)  readiness / recovery status  performance capacity

  GPS load           Team sport session load:     Individual endurance
  (PlayerLoad,       soccer, rugby, AFL           (power meter is better)
  total distance)
  ──────────────────────────────────────────────────────────────────
```

### VO2max vs. Lactate Threshold vs. Power-to-Weight

```
WHEN EACH METRIC IS THE LIMITING FACTOR

  Athlete Level    Limiting Factor         Training Priority
  ──────────────────────────────────────────────────────────────
  Beginner         VO2max (low ceiling)    Build aerobic base;
                                           any training helps

  Intermediate     VO2max still growing    Mix of base + threshold
                   but LT becoming         work; some intervals
                   relevant

  Advanced         LT is the limiter:     Threshold intervals;
                   VO2max is near genetic  polarized model (80/20)
                   ceiling

  Elite            Economy + LT at high   Micro-gains: running
                   % of VO2max            economy, heat adaptation,
                                          altitude, race tactics

  Climber/hilly    Power-to-weight is     Lose non-functional mass
  course           the deciding metric    OR increase FTP; both
                                          improve W/kg
  ──────────────────────────────────────────────────────────────
```

---

## Common Confusion Points

**Sports science vs. sports medicine**: sports science is performance optimization (physiology, biomechanics, psychology, nutrition, conditioning). Sports medicine is injury prevention and treatment (clinical, requires medical degree in most jurisdictions). They overlap substantially but are distinct professions.

**"Exercise physiology" is not just about elite athletes**: the same principles govern exercise response from bedridden patients to Olympic sprinters. The difference is dose and context, not mechanism.

**Correlation between metrics and performance does not imply causation**: GPS load data predicts injury risk probabilistically but does not cause injury. High VO2max correlates with endurance performance but building VO2max alone does not guarantee elite performance (lactate threshold and economy matter equally).

**"No pain, no gain" has a specific domain of validity**: some training adaptations require sufficient stimulus (progressive overload). But chronic pain indicates tissue damage, not adaptation. Confusing training stimulus with tissue damage is the source of most overuse injuries.
