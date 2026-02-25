# Prosthetics and Orthotics

## The Big Picture

Prosthetics replaces missing body parts. Orthotics supports or corrects existing anatomy.
The field has evolved from passive mechanical devices to microprocessor-controlled systems
with pattern recognition control, and is advancing toward direct neural integration.

```
+---------------------------------------------------------------------+
|              PROSTHETICS — LANDSCAPE                                |
+---------------------------------------------------------------------+
|                                                                     |
|  LOWER LIMB                    UPPER LIMB                           |
|                                                                     |
|  TRANSTIBIAL (BK)              TRANSRADIAL                          |
|  Below knee                    Below elbow                          |
|  Preserves knee joint          More common (>60% upper amputees)    |
|  ESAR foot, running blade      Body-powered or myoelectric          |
|                                                                     |
|  TRANSFEMORAL (AK)             TRANSHUMERAL                         |
|  Above knee                    Above elbow                          |
|  Must replace knee+ankle       Need elbow + wrist + hand           |
|  Microprocessor knee           Harder to control, fewer DOF        |
|  (C-Leg, Genium, Rheo)                                             |
|                                                                     |
|       |                              |                              |
|       v                              v                              |
|  INTERFACE           PASSIVE         ACTIVE        NEURAL          |
|  Socket design       ESAR carbon     Myoelectric   TMR + direct    |
|  Suspension          fiber           EMG control   nerve           |
|  Liner materials     Energy-return   Pattern recog stimulation     |
+---------------------------------------------------------------------+
```

---

## Amputation Levels and Biomechanical Implications

### Amputation Level Classification

```
  LOWER LIMB AMPUTATION LEVELS
  =============================

  TRANSTIBIAL (below knee, BK) — most common (~70% of all lower limb)
  Preserves knee joint and much of tibial function.
  Residual limb: tibia + fibula stump
  Biomechanical advantage: intact knee means controlled gait possible
  with passive or simple active prosthetic foot
  Prosthetic components needed: socket + pylon + foot

  KNEE DISARTICULATION — through the knee joint
  Disarticulated knee provides long residual limb, excellent control
  Rare: structural reasons for choosing AK vs. knee dis.

  TRANSFEMORAL (above knee, AK)
  Removes knee joint — must replace both knee AND ankle/foot function
  Hip flexors/extensors must control prosthetic knee + foot
  Much more metabolic cost than BK: ~65% vs ~25% increase
  Prosthetic components: socket + microprocessor knee + pylon + foot

  HIP DISARTICULATION / HEMIPELVECTOMY
  Very high energy cost, limited mobility
  Hip joint removed, socket anchors to pelvis/buttock

  UPPER LIMB LEVELS:
  TRANSRADIAL (below elbow, BE): preserve elbow function
  TRANSHUMERAL (above elbow, AE): must replace elbow + hand
  SHOULDER DISARTICULATION / FOREQUARTER
  PARTIAL HAND: finger/ray amputation, preserve some grip

  K-LEVEL FUNCTIONAL CLASSIFICATION (Medicare/insurance):
  K0: Not a candidate; cannot ambulate
  K1: Home ambulatory on level surfaces only
  K2: Community ambulatory on low challenge terrain (ramps, curbs)
  K3: Variable cadence, uneven terrain, most daily activities
  K4: Exceeds basic ambulation (running, sports — child/active adult)
  K-level determines covered prosthetic components.
```

---

## Socket Design and Interface

The socket is the most critical component — it is the interface between residual limb and
prosthesis. Poor socket fit causes skin breakdown, discomfort, and rejection.

```
  SOCKET DESIGN — TRANSTIBIAL
  ============================

  PATELLAR TENDON BEARING (PTB) — traditional:
  Load-bearing: patellar ligament, medial tibial flare
  Relief areas: tibial crest, bony prominences, fibular head
  Limited total contact -> pressure concentrations
  Increasingly replaced by TSB

  TOTAL SURFACE BEARING (TSB) — current standard:
  Silicone liner against skin -> even load distribution
  Negative pressure (seal) or pin lock suspension
  More comfortable, fewer pressure ulcers

  SOCKET FABRICATION:
  1. Plaster casting of residual limb (or 3D scanning)
  2. Positive model creation (carve from plaster cast)
  3. Check socket: diagnostic fit, make adjustments
  4. Definitive socket: carbon fiber laminate or thermoplastic

  3D PRINTING SOCKETS:
  Polypropylene FDM or carbon fiber composite SLS
  Rapid iteration on fit
  Custom lattice structures for load distribution
  Still validation challenges for Class II socket claims

  SUSPENSION SYSTEMS:
  +-------------------+-------------------------------------------+
  | Sleeve suspension | Silicone or urethane sleeve rolls over     |
  |                   | socket rim, creates seal by pressure       |
  |                   | Simple, but sleeve wears out               |
  +-------------------+-------------------------------------------+
  | Pin lock          | Pin on distal liner threads into          |
  |                   | catch mechanism at socket base            |
  |                   | Audible/tactile click confirmation         |
  +-------------------+-------------------------------------------+
  | Vacuum-assisted   | Active pump creates negative pressure     |
  | socket system     | (-50 to -100 mmHg) at socket interface    |
  | (VASS)            | Best suspension, reduces pistoning         |
  |                   | Volume stability -> less edema, better fit |
  +-------------------+-------------------------------------------+

  RESIDUAL LIMB VOLUME FLUCTUATION:
  Major problem: limb volume changes ~5-10% through day
  -> socket loosens (pistoning) -> blisters, falls
  Solutions: volume management socks (donning 1-15 ply), VASS,
  inflatable bladder socket systems (Otto Bock Harmony)
```

---

## Prosthetic Feet and Ankles

### ESAR (Energy Storing and Returning) Feet

```
  PROSTHETIC FOOT EVOLUTION
  ==========================

  SACH (Solid Ankle Cushion Heel) — passive, simple:
  Wooden keel + foam heel compression
  No energy return. K1/K2 ambulators.
  Weight: 300-500g. Low cost.

  SINGLE-AXIS FOOT:
  Hinged ankle allows plantar/dorsiflexion
  Improves ramp/stair descent, but heavy and less dynamic

  ENERGY STORING AND RETURNING (ESAR) FOOT:
  Carbon fiber keel (leaf spring) deflects during loading
  -> stores elastic strain energy (~20-60% return)
  -> returns energy during push-off
  Key analogy: carbon fiber = stiff spring, not rigid keel

  ÖSSUR FLEX-FOOT / PROFLEX:
  Split-toe design: lateral torsion for uneven terrain
  ProFlex: articulating heel + ESAR keel
  Carbon fiber vs CFRP: affects spring stiffness profile

  RUNNING BLADES (Össur Cheetah, Ottobock Taleo):
  Shaped like J or C, stores maximum energy
  No heel: designed only for running gait
  Recreational and Paralympic sport (T44 class)
  Can generate running speeds >10 m/s (Oscar Pistorius controversy:
  2012 Olympics questioned whether blades gave advantage)

  Energy return efficiency:
  Biological ankle-foot: ~60-70% energy return
  ESAR prosthetic foot: ~20-40% return (less than biological)
  ->metabolic cost of ambulation always higher than intact
```

### Powered Ankle-Foot

```
  POWERED PROSTHETIC ANKLE-FOOT
  ==============================

  ÖSSUR PROPRIO FOOT (passive energy management, motorized angle)
  ÖSSUR POWER KNEE: powered knee + ankle
  EMPOWER (Ottobock/BioM): powered push-off

  Biomechanical advantage: powered devices can do positive work
  -> reduce metabolic cost vs. ESAR (which only returns, not adds energy)
  BiOM: 4 brushless DC motors, 2 kW peak, lithium battery
  ->metabolic cost reduction ~15-30% vs. non-powered ESAR

  Limitation: weight (1-2 kg heavier than ESAR), battery life,
  maintenance complexity, cost ($80-100k)
```

---

## Microprocessor Knees (MPK)

```
  MICROPROCESSOR KNEE (MPK) SYSTEMS
  ===================================

  RATIONALE:
  Biological knee: muscles actively resist flexion in stance
  -> prevents collapse under body weight
  Passive mechanical knee: depends on alignment + lock
  -> unpredictable on ramps, stairs, uneven terrain
  MPK: onboard sensors continuously control hydraulic resistance
  -> appropriate resistance at every gait phase

  C-LEG (Ottobock):
  First widely adopted MPK (1997-present)
  Hydraulic actuator with proportional valve
  Angular velocity sensor + force sensor in foot
  -> 50 calculations/second
  Modes: walking, sitting, standing, slopes
  Stumble recovery: detects unexpected knee flexion, increases resistance
  Battery: rechargeable, 1-2 days

  KENEVO (Ottobock):
  C-Leg variant for lower activity users (K2)
  Additional standing stability mode

  GENIUM X3 (Ottobock):
  Advanced version: step-over-step stairs, backwards walk
  Bluetooth programming by prosthetist
  Waterproof (IP67), 3-day battery

  RHEO KNEE (Össur):
  Magnetorheological fluid (MR fluid) instead of hydraulic
  MR fluid viscosity controlled by magnetic field -> faster response
  ~1000 adjustments/second

  POWER KNEE (Össur):
  Actively powered: motor provides push during stance extension
  -> reduces compensatory hip motion, more natural gait
  Most expensive MPK category (~$100k)

  CLINICAL EVIDENCE:
  Meta-analyses show MPK reduces stumbles/falls vs. non-MPK AK
  Most benefit for K3/K4 community ambulators
  Cost-effectiveness debated — Medicare coverage controversial
```

---

## Upper Limb Prosthetics

### Body-Powered

```
  BODY-POWERED PROSTHETICS
  =========================

  Mechanism: shoulder/body motion -> Bowden cable -> terminal device

  HARNESS: figure-8 or figure-9 configuration
  Cable: stainless steel Bowden cable in housing
  Terminal device:
  - Hook (Dorrance 5X, APRL): two fingers, voluntary opening (VO)
    or voluntary closing (VC). Hook preferred by most experienced users
    for function, grip force feedback
  - Hand: cosmetic appearance but less functional grip force

  VOLUNTARY OPENING (VO) — most common:
  Cable opens hook against spring resistance
  Release cable -> hook closes on spring force
  Grip force proportional to spring tension, not adjustable in real-time

  VOLUNTARY CLOSING (VC):
  Cable closes hook, release opens it
  Proportional grip force with cable tension
  More intuitive but requires constant effort to maintain grip

  TRANSHUMERAL: requires elbow lock/flex mechanism
  Body motion operates elbow (lift shoulder) AND hook (arm flex)
  -> complex dual-control, steep learning curve

  Advantage: durable, reliable, proprioceptive feedback through cable,
             low maintenance, waterproof, no battery
  Disadvantage: cosmetically concerning, limited grip patterns,
                harness discomfort
```

### Myoelectric Control

```
  MYOELECTRIC PROSTHETICS
  ========================

  Surface EMG electrodes inside socket wall
  Record EMG from residual limb muscles
  -> Processed -> control prosthetic hand/wrist/elbow

  DUAL-SITE CONTROL (traditional):
  Two electrodes over two muscle groups
  e.g., biceps + triceps (transhumeral)
  Biceps EMG > threshold -> elbow flex
  Triceps EMG > threshold -> elbow extend
  Sequential co-contraction to switch mode (hand/wrist/elbow)
  Simple, robust but limited DOF simultaneously

  PATTERN RECOGNITION CONTROL:
  Multiple electrodes (8-16) over residual limb musculature
  Extract time-domain features from each channel:
  - Mean absolute value (MAV)
  - Zero crossing rate (ZCR)
  - Waveform length (WL)
  - Slope sign change (SSC)
  Classifier: LDA (linear discriminant analysis) standard
  Trained on multiple grip patterns (open, close, pinch, wrist rotate)
  Can decode 6-10 grip patterns simultaneously
  Real-time classification: ~100ms update rate

  COAPT (prosthetic company): pattern recognition controller
  commercially available, used with multiple hands (TASKA, Ottobock)

  TARGETED MUSCLE REINNERVATION (TMR):
  Surgical procedure: reroute residual nerve endings to
  spare muscle sites (pectorals, arm muscles)
  -> more distinct EMG signals -> better pattern recognition
  -> MORE EMG channels from more muscles -> higher DOF control
  Pioneered by Todd Kuiken (Northwestern)
  Also provides sensory reinnervation (see below)

  HANDS:
  Ottobock Michelangelo: 6-grip, i-Limb Ultra, Bebionic,
  TASKA Hand, Psyonic Ability Hand (with sensory feedback)
  Modular finger drives: each finger independently actuated
```

---

## Osseointegration — Direct Skeletal Attachment

```
  OSSEOINTEGRATION FOR PROSTHETICS
  =================================

  Concept: attach prosthesis directly to bone (skeletally)
  instead of via soft tissue socket
  -> eliminates socket interface -> eliminates all socket problems

  SURGICAL PROCEDURE:
  Stage 1: Titanium implant (fixture) pressed into medullary canal
           similar to dental implant but much larger (12-18mm diameter)
           Wait 6 months for osseointegration
  Stage 2: Percutaneous abutment placed through skin
           Allows external prosthesis to attach via lock mechanism
  Rehab: progressive loading protocol

  SYSTEMS:
  OPRA (Osseoanchored Prostheses for the Rehabilitation of Amputees):
  Osseointegration Prostheses and Rehabilitation — Swedish system (Branemark)
  OPL (Osseointegration Prosthetics Limb): UK/Australian system

  CLINICAL OUTCOMES:
  Dramatic improvement in proprioception via osseointegration
  Patients feel ground texture, vibration through bone
  Elimination of all socket-related skin problems
  Substantially higher activity levels vs. socket prosthetics
  Risk: periprosthetic infection (percutaneous site)
        periprosthetic fracture (stress concentration at abutment)
        falls during osseointegration phase

  FDA STATUS: IDE (investigational) in US; approved in Sweden, UK, Australia
  Broader US approval pending — percutaneous permanent implant is
  high regulatory burden (infection risk, long-term data needed)
```

---

## Sensory Feedback

Closing the loop: the brain needs sensory input, not just motor output.

```
  PROSTHETIC SENSORY FEEDBACK APPROACHES
  ========================================

  VIBROTACTILE:
  Vibration motor (ERM or LRA) on residual limb or contralateral limb
  Encodes grip force, contact detection, slip detection
  Non-invasive, easy to implement
  Limitation: referred sensation not at prosthetic hand site
              perceptual fusion (feels like vibration, not touch)

  ELECTROTACTILE:
  Surface electrical stimulation on residual limb
  Encodes pressure, slip as modulated pulse train
  Better spatial discrimination than vibrotactile
  Limitation: pins-and-needles sensation, not natural touch quality

  OSSEOPERCEPTION:
  Osseointegrated implant transmits vibration directly to bone
  -> vibration sensed via osseointegration (mechanoreceptors in bone)
  -> natural proprioceptive pathway
  Study: osseointegrated patients report tactile sense through titanium
  Kuiken (2009): demonstrated somatosensory cortex activation

  TARGETED SENSORY REINNERVATION (TSR) / TMR:
  During TMR surgery, sensory nerves also rerouted to skin patches
  -> stimulating those skin patches -> patient FEELS sensation
  as if it is coming from the original (phantom) hand location
  "Referred phantom sensation" — the brain's coordinate mapping
  is preserved even though the limb is gone
  Can touch specific skin patch -> patient feels specific finger
  Enables sophisticated sensory feedback via surface stimulation

  PERIPHERAL NERVE STIMULATION:
  Transversal Intrafascicular Multichannel Electrode (TIME)
  Utah Slant Array implanted in ulnar/median nerve
  Direct stimulation of afferent nerve fibers
  -> more natural, precise somatotopic sensation
  Research stage, not commercially available
```

---

## Exoskeletons

```
  POWERED EXOSKELETONS
  ====================

  REHABILITATION (clinical):
  Ekso GT (Ekso Bionics): bilateral hip+knee actuation
  ReWalk (Lifeward): hip+knee, crutch-triggered step initiation
  Indego (Parker Hannifin): SCI rehabilitation, foot controls trigger

  FDA cleared as Class II medical devices for:
  - Stroke rehabilitation (assist weak leg muscles in gait training)
  - SCI rehabilitation (T4-T12 injury levels)
  Mechanism: repetitive stepping -> neuroplasticity -> recovery?
  Evidence: modest functional improvement in SCI; better for stroke
  where neuroplasticity is clearer

  INDUSTRIAL / MILITARY:
  Ekso Works (upper limb): tool support for overhead work
  Lockheed FORTIS: passive lower-limb exoskeleton, weight transfer
  Sarcos Robotics Guardian: powered industrial upper body
  ONYX (Lockheed): lower limb military exoskeleton for load carry
  No battery consumption (passive); stores energy in springs

  SOFT EXOSUITS (Wyss Institute / RehabCare):
  Textile-based, cable-driven, assists plantarflexion at toe-off
  ~7-10% metabolic reduction in walking
  Much lighter than rigid exoskeleton frame (<1 kg)
  Harvard Wyss: stroke rehabilitation clinical trials

  KEY TECHNICAL CHALLENGES:
  +-------------------------+--------------------------------------+
  | Power source            | Battery weight vs. runtime tradeoff  |
  | Transparency            | No added resistance in free motion   |
  | Intent detection        | When does user want to step?         |
  |                         | (EMG, force, inertial sensors)       |
  | Alignment               | Joint axes must align with body      |
  | Safety                  | Prevent falls, unexpected motion     |
  +-------------------------+--------------------------------------+
```

---

## Common Confusion Points

**Body-powered vs. myoelectric — which is better?** Neither is universally superior. Experienced
body-powered hook users often outperform myoelectric users on functional tasks because: (1) the
cable provides proprioceptive feedback, (2) body-powered is robust and maintenance-free, (3) grip
force is intuitively proportional to cable tension. Myoelectric wins on cosmesis and grip
strength. Most experienced upper limb amputees own both and select contextually.

**Microprocessor knee for all AK amputees?** MPK provides clear safety and gait symmetry
improvements for K3/K4 ambulators (community walkers). For K1/K2 (limited mobility), the
benefit-cost analysis is less clear and Medicare reimbursement reflects this. An MPK for someone
who walks only at home on level surfaces may provide minimal additional safety vs. a well-aligned
mechanical knee.

**Osseointegration infection risk**: Percutaneous implants create a permanent pathway through
skin — the same problem as long-term central venous catheters. The titanium abutment creates a
dermal interface zone where epithelium "seals" around it (similar to tooth-gum interface). With
proper hygiene, superficial infection is manageable. Deep periprosthetic infection is rare but
serious. The risk-benefit is favorable for appropriate patients but requires lifelong vigilance.

**TMR is both motor AND sensory**: Targeted muscle reinnervation was developed primarily to
create more EMG signal sources for prosthetic control. The sensory reinnervation aspect
(referred phantom sensation) was discovered somewhat serendipitously. Both benefits are now
used intentionally — surgery now explicitly routes both motor and sensory residual nerves.

**Exoskeleton vs. prosthesis**: A prosthesis replaces a missing limb. An exoskeleton is worn
over an intact (or weakened) limb to augment or assist it. This distinction matters for
regulatory classification (prosthetic devices vs. powered wheelchair-equivalent classification)
and for reimbursement.

---

## Decision Cheat Sheet

| Patient scenario | Primary recommendation | Notes |
|---|---|---|
| Active K3/K4 TT amputee | Carbon fiber ESAR foot (Össur Flex-Foot or equivalent) | Best balance energy return/weight |
| Active K3/K4 TF amputee | Microprocessor knee + ESAR foot (C-Leg or Genium) | MPK safety clearly demonstrated |
| K1/K2 TF amputee | Non-MPK knee (stance control) + SACH foot | MPK benefit modest, high cost |
| Bilateral TF amputee | Short pylons first, progress to longer prostheses | Balance training is primary challenge |
| Transradial amputee, working | Body-powered hook (workhorse) + myoelectric (cosmesis) | Likely needs both |
| Transhumeral amputee | TMR surgery first, then pattern recognition myoelectric | More EMG sources -> better control |
| Athletic/recreational TT | Running blade (Cheetah/Taleo) for sport, ESAR for ADL | Sport-specific device |
| SCI (T4-L1) rehabilitation | Exoskeleton (ReWalk or Ekso) for rehab program | Not ADL replacement, therapy tool |
| Chronic socket problems | Consider osseointegration evaluation | IDE in US, standard care in EU/AU |
