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

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| What are the three energy systems in order? | PCr (0–10s), glycolytic (10s–2min), oxidative (>2min) |
| What limits VO2max? | Central (cardiac output) and peripheral (O₂ extraction) |
| What is the best predictor of endurance performance? | Lactate threshold (not VO2max) when comparing trained athletes |
| What is the most evidence-supported ergogenic aid? | Creatine monohydrate |
| What is "polarized training"? | ~80% training below LT1, ~20% above LT2; Seiler's model |
| What is the biological passport? | Longitudinal athlete biomarker profile used to detect doping manipulation |
| What is flow state in sport? | Csikszentmihalyi's "zone": challenge-skill balance → effortless performance |
| What is the acute:chronic workload ratio? | Current week load / rolling 4-week average; >1.5 = injury risk spike |

---

## Common Confusion Points

**Sports science vs. sports medicine**: sports science is performance optimization (physiology, biomechanics, psychology, nutrition, conditioning). Sports medicine is injury prevention and treatment (clinical, requires medical degree in most jurisdictions). They overlap substantially but are distinct professions.

**"Exercise physiology" is not just about elite athletes**: the same principles govern exercise response from bedridden patients to Olympic sprinters. The difference is dose and context, not mechanism.

**Correlation between metrics and performance does not imply causation**: GPS load data predicts injury risk probabilistically but does not cause injury. High VO2max correlates with endurance performance but building VO2max alone does not guarantee elite performance (lactate threshold and economy matter equally).

**"No pain, no gain" has a specific domain of validity**: some training adaptations require sufficient stimulus (progressive overload). But chronic pain indicates tissue damage, not adaptation. Confusing training stimulus with tissue damage is the source of most overuse injuries.
