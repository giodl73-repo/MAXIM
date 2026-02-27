# Robotics — AI and Learning-Based Robotics

## The Big Picture

Classical robotics = explicit models + hand-crafted controllers. AI robotics = learning
from data + simulation. The frontier is merging both: learned models inside principled
control frameworks.

```
+===========================================================================+
|                       AI ROBOTICS LANDSCAPE                               |
+===========================================================================+
|                                                                           |
|  REINFORCEMENT LEARNING        IMITATION LEARNING                         |
|  ======================        ==================                         |
|  Learn from reward signal      Learn from human demonstrations            |
|  No demonstration needed       No reward engineering needed               |
|  Sample-inefficient            Efficient but limited to demo distribution  |
|  PPO, SAC, Dreamer             BC, DAgger, ACT, Diffusion Policy          |
|                                                                           |
|  FOUNDATION MODELS             PERCEPTION / REPRESENTATION                |
|  ================              ==========================                 |
|  RT-1, RT-2                    Object detection (YOLO, SAM)               |
|  Octo, pi0                     6-DOF pose estimation (FoundationPose)     |
|  OpenVLA, GROOT                Semantic scene understanding               |
|  LLM for task planning         NeRF/3DGS for scene reconstruction         |
|                                                                           |
|  SIM-TO-REAL TRANSFER          DEXTEROUS MANIPULATION                     |
|  ====================          ======================                     |
|  Domain randomization          In-hand manipulation                       |
|  System identification         Tactile sensing                            |
|  Adaptive domain random.       Contact-rich tasks                         |
|  Real-to-sim (reverse)         Deformable objects                         |
|                                                                           |
+===========================================================================+
```

---

## Reinforcement Learning for Robotics

<!-- @editor[bridge/P2]: RL for robotics section presents the MDP formulation without bridging to RL for cloud infrastructure optimization — the learner's Azure infrastructure uses RL for exactly this: VM placement (S: cluster resource state, A: where to place workload, R: cost + SLA satisfaction), autoscale policy optimization, and Azure Automanage; the MDP (S: robot state, A: joint torques, R: task completion) is structurally identical; framing "the same MDP your autoscale policies run on is what teaches a robot to walk" makes the abstraction concrete for this reader and connects two domains they already understand -->

### MDP Formulation

```
MARKOV DECISION PROCESS:
  S: state space     (robot joints, object poses, sensor data)
  A: action space    (joint torques, velocities, high-level commands)
  P(s'|s,a):         transition function (physics -- unknown, learned, or simulated)
  R(s,a,s'):         reward function (task success signal)
  gamma:             discount factor (0 < gamma < 1)

POLICY: pi(a|s) -- probability of action a given state s.
  Stochastic (outputs distribution over actions) -- used during training.
  Deterministic: a = mu(s) -- used at deployment.

OBJECTIVE: find pi that maximizes expected discounted return:
  J(pi) = E[sum_{t=0}^{inf} gamma^t * R(s_t, a_t, s_{t+1})]
```

### Reward Design Challenges

```
REWARD SHAPING is the hardest part of RL for robotics.

SPARSE REWARD:
  +10 if task complete, 0 otherwise.
  Simple to define but extremely hard to learn.
  Robot wanders randomly until accidentally completing task.
  For 6-DOF manipulation: probability of accidental success ~ 0.

DENSE REWARD:
  Proxy reward guiding robot toward goal.
  Example: r = -||p_EE - p_target|| + bonus_if_contact + penalty_if_collision

  REWARD HACKING: robot finds unintended ways to maximize reward.
    - "Run fast" reward: robot learns to be tall (falls over = no friction).
    - "Push object to target" reward: robot learns to push the target marker.
    - RL is policy optimization, not intent optimization.

GOOD REWARD STRUCTURE (practice):
  1. Dense shaping for early training.
  2. Sparse task success bonus for final performance.
  3. Safety penalties (joint limits, collision).
  4. Regularization (action magnitude penalty -> smooth motions).
  5. Terminate episode on clear failure (saves simulation time).
```

### PPO (Proximal Policy Optimization)

```
PPO (Schulman, 2017): on-policy, policy gradient method.
  The default choice for locomotion, simple manipulation.

ACTOR-CRITIC:
  Actor: pi_theta(a|s) -- policy network.
  Critic: V_phi(s) -- value network (estimates expected return from s).

TRAINING LOOP:
  1. COLLECT ROLLOUTS: run pi_theta in environment, collect (s,a,r,s') tuples.
  2. COMPUTE ADVANTAGES:
     A(s,a) = Q(s,a) - V(s)  <- how much better than average?
     GAE (Generalized Advantage Estimation): weighted sum of temporal differences.
  3. OPTIMIZE policy using clipped surrogate objective:
     L_CLIP = E[min(r_t * A_t, clip(r_t, 1-eps, 1+eps) * A_t)]
     r_t = pi_theta(a|s) / pi_theta_old(a|s)   <- probability ratio
     clip: prevents too-large policy updates (stability).
  4. REPEAT from step 1 with updated policy.

WHY CLIPPING:
  Without clipping: large update can catastrophically change policy.
  Clipping: limits how far new policy can deviate from old policy.
  eps = 0.2 is standard.

TYPICAL HYPERPARAMETERS:
  Learning rate: 3e-4
  Batch size: 4096-32768
  GAE lambda: 0.95, gamma: 0.99
  Clip ratio: 0.2
  Epochs per rollout: 5-10

PPO IS SAMPLE-INEFFICIENT: needs millions to billions of environment steps.
Practical only with fast simulation (Isaac Sim at 100k Hz).
```

### SAC (Soft Actor-Critic)

```
SAC (Haarnoja, 2018): off-policy, entropy-regularized.
  Default choice for manipulation, locomotion with fine-grained control.

ENTROPY REGULARIZATION:
  J(pi) = E[sum R_t + alpha * H(pi(.|s_t))]
  H(pi): entropy of policy. Encourages exploration.
  alpha: temperature (automatically tuned in SAC).

OFF-POLICY:
  Uses a replay buffer. Learns from past experiences.
  More sample-efficient than PPO (5-10x).
  Can learn from a mix of exploration and exploitation.

ACTOR-CRITIC (double Q):
  Actor: deterministic + noise.
  Two Q-networks: Q1, Q2. Take min (pessimistic estimate, prevents over-estimation).

SAC vs PPO CHOICE:
  SAC:  more sample-efficient, good for continuous action spaces.
        Slower wall-clock time (off-policy replay buffer overhead).
  PPO:  simpler, faster wall-clock with massive parallelism (Isaac Lab).
        Less sample-efficient per step.
```

### Sim-to-Real Transfer

```
THE SIM-TO-REAL GAP:
  Policy trained in simulation fails on real hardware.
  Causes: unmodeled friction, motor compliance, sensor noise,
          visual appearance, actuator delays, cable flex.

DOMAIN RANDOMIZATION:
  Train in simulation with randomized physics parameters.
  Random: motor strength +/-20%, friction coefficient, link masses,
          joint damping, sensor noise, visual textures.
  Policy must work across ALL randomized parameters.
  -> When deployed to real world, treats real world as "another randomized sim."

  Introduced by: OpenAI for Dactyl (2019 Rubik's Cube).
  Effective range: typically physics params +/-20-50%.
  More randomization = more robust but harder to train.

SYSTEM IDENTIFICATION (SysID):
  Measure real robot parameters (inertia, friction, motor models).
  Use measured values as center of randomization range.
  Better than random center.
  Tools: excitation trajectories, maximum-likelihood estimation.

ADAPTIVE DOMAIN RANDOMIZATION (ADR):
  Automatically expand randomization range as policy improves.
  Start narrow (easier training), gradually expand (more robustness).
  Policy "earns" harder randomization by succeeding at current level.

REAL-TO-SIM (REVERSE):
  Instead of making sim match reality: learn the gap and correct for it.
  GraspNet, DexPoint: transfer by learning from real data first,
  then use sim only for safe exploration.
```

---

## Imitation Learning

Learn robot behavior from human demonstrations. Avoids reward engineering.

### Behavioral Cloning (BC)

```
BC: supervised learning on demonstration data.
  Dataset: D = {(o_1, a_1), (o_2, a_2), ..., (o_N, a_N)}
  Policy: pi = argmin_theta E[(a - pi_theta(o))^2]

PROBLEM: COVARIATE SHIFT (distribution shift).
  Demo distribution: p_demo(o) -- states visited by human.
  Policy distribution: p_pi(o) -- states visited by trained policy.
  After slight error, policy enters state not in training data.
  -> No training data for this state -> random action -> state gets worse.
  -> Compounding error over time.

ANALOGY: BC is like teaching someone to drive by only showing them straight roads.
  The first time they need to turn, they have no data and may drive off a cliff.
```

### DAgger (Dataset Aggregation)

```
DAgger (Ross, 2011): interactive imitation learning.
  Solves covariate shift by continuously collecting data under the POLICY distribution.

ALGORITHM:
  Loop:
    1. Run current policy pi_i to collect states.
    2. Ask human expert to label actions for THOSE states (not demonstration states).
    3. Add labeled (state, action) pairs to dataset D.
    4. Retrain policy pi_{i+1} on D.

  KEY: expert labels states the policy actually visits, not just demo states.
  Policy sees its own mistakes + correct actions -> learns to recover.

PRACTICAL CHALLENGE: requires human online labeling at every iteration.
  Teleop setups (VR headset + haptic gloves) make this feasible for manipulation.
```

### Action Chunking Transformer (ACT)

```
ACT (Zhao, 2023): state-of-the-art BC for manipulation.

  KEY IDEAS:
  1. ACTION CHUNKING: predict K future actions at once (K=50-100 steps).
     Reduces compounding error (fewer autoregressive steps).
     Temporal ensembling: average overlapping chunks at deployment.

  2. TRANSFORMER ARCHITECTURE:
     Input: camera images + joint state.
     Output: sequence of K future joint positions.
     Vision encoder: CNN or ViT backbone.
     Transformer decoder: cross-attention over visual features.

  3. CVAE: Conditional Variational Autoencoder for multi-modal demos.
     Demos for the same goal may look different (grasp from left vs right).
     CVAE captures this multi-modality in latent code z.

PERFORMANCE: ~90% success on tabletop manipulation tasks.
             State-of-the-art for fine manipulation from 2 cameras.
TRAINING data: 50-100 demonstrations per task sufficient.
```

### Diffusion Policy

```
DIFFUSION POLICY (Chi, 2023): diffusion models for robot actions.

  Inspired by image diffusion (DDPM, stable diffusion).
  Policy = denoising diffusion process over action sequences.

  TRAINING:
    Corrupt demonstrations with noise.
    Train network to DENOISE.

  INFERENCE:
    Start from pure noise.
    Iteratively denoise (20-100 steps) -> clean action sequence.

  ADVANTAGES:
    Handles multi-modal action distributions (can do "grasp from left OR right").
    Stable training (vs GANs).
    High expressiveness.

  DISADVANTAGES:
    Slow inference (20-100 denoising steps per action).
    Recently: consistency models / flow matching reduce steps to 1-5.

FLOW MATCHING (pi0, 2024):
  Replaces diffusion with a flow ODE: faster inference (1-5 steps vs 20-100).
  pi0 (Physical Intelligence): uses flow matching for dexterous manipulation.
  Trains on 10,000+ demonstrations from different robots.
```

---

## Foundation Models for Robotics

The convergence of LLMs + vision models + robot control.

### RT-1 (Robotics Transformer 1)

```
RT-1 (Google / Everyday Robots, 2022):

  ARCHITECTURE:
    Input: 6 camera images + language instruction (tokenized text).
    Processing: EfficientNet vision encoder + Transformer.
    Output: tokenized robot actions (discretized joint positions/velocities).

  TRAINING DATA:
    130,000 demonstration episodes across 700+ tasks.
    13 robots, 5 months of data collection.

  RESULTS:
    97% success on tasks in training distribution.
    76% success on novel tasks (generalization).
    FAST: runs at 3 Hz on real robot.

  KEY INSIGHT:
    Large-scale diverse data + Transformer = emergent task generalization.
    Same architecture principle as GPT/BERT -- scale data and model.
```

### RT-2 (Robotics Transformer 2)

```
RT-2 (Google DeepMind, 2023):

  FOUNDATION: Vision-Language Model (VLM) fine-tuned for robotics.
    Based on PaLM-E (55B parameters) or PaLI-X (55B).

  INNOVATION: represents robot actions as TEXT TOKENS.
    "Move arm 0.05m in x direction" -> token sequence.
    Joint fine-tuning on robot demonstrations + web VLM training.

  EMERGENT CAPABILITIES:
    Zero-shot reasoning from web knowledge.
    "Pick up the object that should not be eaten" -> picks rock over apple.
    "Which object is more expensive?" -> picks phone over can.
    Novel concepts never seen in robot training data.

  RESULT:
    62% success on novel tasks (2x better than RT-1).
    Emergent semantic reasoning that crossed from language to actions.
```

### Octo (Open Source Generalist Robot)

```
OCTO (Octo Team, 2023):

  Open-source alternative to RT-2.
  780M parameters. Apache 2.0 license.
  Pre-trained on Open X-Embodiment dataset (800K+ demos, 22 robot types).

  ARCHITECTURE:
    Transformer with modular task and observation tokenizers.
    Supports: text goals, image goals, observation: RGB, depth, proprio.
    Action head: diffusion-based or regression.

  FINE-TUNING:
    Pre-trained weights can be fine-tuned for specific robot/task with ~100 demos.
    Dramatically reduces data needed vs training from scratch.
    Available at: github.com/octo-models/octo

  ANALOGY TO LLM FINE-TUNING:
    Octo = GPT-3 pre-training.
    Your fine-tuned version = ChatGPT.
    Pre-training captures general robot motion; fine-tuning specializes.
```

### pi0 (Physical Intelligence)

```
pi0 (Physical Intelligence, 2024):

  ARCHITECTURE:
    Pre-trained VLM backbone (PaliGemma-based).
    Flow matching action expert head (fast inference).
    Trained on 10,000+ demonstrations from multiple dexterous robots.

  KEY FEATURE: ZERO-SHOT dexterous manipulation.
    Folding laundry, cleaning tables, packing boxes, assembling components.
    Tasks requiring fine motor control and contact-rich interaction.

  DEPLOYMENT:
    Runs on robot with GPU inference.
    Action output: 50-step action chunks at 50 Hz.
    General-purpose: same model across many tasks.
```

---

## Open X-Embodiment Dataset

```
OPEN X-EMBODIMENT (Google et al., 2023):
  Largest open robot learning dataset as of 2024.
  1M+ episodes across 22+ robot types and 500+ tasks.
  Robots: mobile manipulators, arms, tabletop setups, bi-manual systems.
  Data types: RGB images, proprio, language instructions, actions.
  Download: tensorflow-datasets or HuggingFace datasets.

PURPOSE: Pre-train generalist robot policies (like Octo).
  Same motivation as Common Crawl for NLP or ImageNet for vision.
```

---

## Dexterous Manipulation

The hardest subproblem: fine manipulation with multi-fingered hands.

```
CHALLENGES:
  Contact instability: small errors in finger placement -> task failure.
  In-hand manipulation: rolling, pivoting, sliding objects within grasp.
  High dimensionality: 20+ DOF hand with 6 contacts each = 140+ constraint dimensions.
  Tactile sensing: fingertip force distribution needed for stable grasp.

OPENAI DACTYL (2019):
  Shadow Hand (24 DOF) + domain randomization.
  Solved Rubik's cube in-hand (one-handed).
  Required: 13,000 years of simulated experience.
  Hardware: 3 GPUs + 920 CPUs running for months.
  Transfer: sim-to-real worked because of extreme domain randomization.

TACTILE SENSING:
  Optical tactile sensors: GelSight, DIGIT (Facebook/Meta).
    Camera inside compliant gel fingertip.
    High-resolution contact geometry (1mm or better).
  MEMS arrays: 100s of pressure sensors per fingertip.
  Neural tactile processing: convolutional networks on tactile images.

CURRENT STATE (2025):
  Industrial: reliable 2-finger grasps of known objects.
  Research: dexterous manipulation of small objects (building blocks, tools).
  Frontier: generalizing dexterous manipulation to novel objects and tasks.
  Gap: factory robots can reliably grasp 99.9%+ of objects;
       dexterous manipulation of arbitrary objects < 80%.
```

---

## Perception Pipeline for Manipulation

Before you can manipulate an object, you must know where it is and how it's oriented.

### 6-DOF Object Pose Estimation

```
PROBLEM: given RGB or RGB-D image, find 6-DOF pose (x,y,z,rx,ry,rz) of target object.

CLASSICAL METHODS:
  LINEMOD: template matching at multiple scales. Fast, fragile to occlusion/lighting.
  PVNet: predict keypoints, solve PnP. Works with partial visibility.

DEEP LEARNING METHODS:
  DenseFusion: point cloud + color feature fusion. 5mm accuracy on tabletop.
  FoundationPose (NVIDIA, 2024): foundation model for 6-DOF pose.
    No per-object training needed. Single reference image sufficient.
    Outperforms per-object trained models on unseen objects.

PRACTICAL PIPELINE:
  1. Segment object from background (SAM, YOLO, or depth-based).
  2. Estimate 6-DOF pose (FoundationPose or DenseFusion).
  3. Feed pose to IK solver -> robot arm trajectory.
  4. Execute grasp.
  5. Verify with tactile feedback.
```

### Object Detection and Segmentation

```
YOLO (You Only Look Once, v8/v11):
  Real-time object detection + segmentation.
  Single forward pass: bounding boxes + class + confidence.
  Speed: 100-300 FPS on GPU. Runs on Jetson Orin.
  Use for: known object classes, fast detection.

GROUNDING DINO + SAM (Segment Anything):
  Open-vocabulary: detect arbitrary objects from text description.
  "Find the red cup" -> bounding box -> SAM -> precise segmentation mask.
  Slower: 2-5 Hz. Use for: semantic querying by language.

FOUNDATION MODEL STACK FOR MANIPULATION PERCEPTION:
  Language query -> Grounding DINO -> bounding box
                                   |
                            SAM -> segmentation mask
                                   |
                     FoundationPose -> 6-DOF pose
                                   |
                      IK + planner -> grasp trajectory
```

---

## Current State vs Hype

```
+--------------------+----------------------------------+---------------------------+
| Capability         | Actually Works (2025)            | Still Research Frontier   |
+--------------------+----------------------------------+---------------------------+
| Locomotion         | Quadruped on rough terrain:      | Agile dexterous biped     |
| (legged robots)    | YES (Spot, ANYmal, Unitree Go2)  | locomotion with loco-manip|
+--------------------+----------------------------------+---------------------------+
| Pick-and-place     | Known objects, structured env:   | Arbitrary objects, clutter|
| manipulation       | YES (industrial > 99.9%)         | packing, unstructured env |
+--------------------+----------------------------------+---------------------------+
| Dexterous          | Simple in-hand: limited.         | Reliable in-hand for      |
| manipulation       | Research demos possible          | general objects           |
+--------------------+----------------------------------+---------------------------+
| Task following     | Simple pick/place tasks          | Complex multi-step cooking|
| from language      | (RT-2, pi0) with ~70-80%         | assembly, open-ended tasks|
+--------------------+----------------------------------+---------------------------+
| Safety near humans | Cobots with contact detection:   | Full body awareness,      |
|                    | YES (UR, Franka)                 | reliable in open spaces   |
+--------------------+----------------------------------+---------------------------+
| Learning from      | ~50-200 demos for tabletop:      | Fewer demos, harder tasks |
| few demos          | YES (ACT, Diffusion Policy)      | long-horizon, outdoor     |
+--------------------+----------------------------------+---------------------------+
| Multi-task robot   | 5-20 task generalization:        | Thousands of tasks,       |
| with 1 policy      | YES (RT-2, Octo for tabletop)   | household-scale variety   |
+--------------------+----------------------------------+---------------------------+
| Autonomous mobile  | Structured warehouse, hospital:  | Open outdoor unstructured |
| navigation         | YES (Amazon Robotics, Boston     | with changing layout      |
|                    | Dynamics Scout)                  |                           |
+--------------------+----------------------------------+---------------------------+
```

---

## Training Infrastructure

```
RL TRAINING SCALE (2025 state of practice):
  Single GPU (RTX 4090):   Isaac Lab 10k-50k env steps/sec. ~hours for locomotion.
  4x GPU (A100 80GB):      100k-500k env steps/sec. Good for dexterous tasks.
  Cluster (100+ GPUs):     Used by Google/DeepMind for foundation model training.

SIMULATION ENVIRONMENTS:
  Isaac Lab: Locomotion, dexterous manipulation, industrial robotics.
  MuJoCo:    Classic benchmark. Efficient. DeepMind Control Suite.
  RoboSuite: Manipulation benchmarks (OpenAI-inspired).
  MetaWorld: 50 manipulation tasks, standard RL benchmark.
  Habitat 3: Embodied AI in photorealistic home environments.

COMPUTE ESTIMATES:
  PPO for Unitree Go2 locomotion: ~2B env steps. ~2 hours on 4x A100.
  SAC for Franka tabletop pick: ~1M steps. ~4 hours on 1 GPU.
  RT-2 fine-tuning on 100 demos: ~8 hours on 8x TPUv4 or 4x A100.
  Dactyl (OpenAI Rubik's): 13,000 sim years. Not repeatable today on budget hardware.
```

---

## Decision Cheat Sheet

| Need | Approach |
|------|----------|
| Learn locomotion policy (quadruped/biped) | PPO + Isaac Lab (massive parallelism) |
| Learn manipulation from demonstrations | ACT or Diffusion Policy (50-200 demos) |
| Fine-tune generalist robot policy | Octo or OpenVLA fine-tuning |
| Zero-shot novel task from language | RT-2 or pi0 (needs access or API) |
| Sim-to-real for unknown dynamics | Domain randomization (Isaac Lab) |
| Known object grasp from camera | FoundationPose + IK |
| Open-vocabulary object detection | Grounding DINO + SAM |
| Off-policy RL with sample efficiency | SAC (replay buffer) |
| On-policy RL with parallelism | PPO (Isaac Lab) |
| Multi-modal demonstration distribution | Diffusion Policy or ACT+CVAE |

---

## Common Confusion Points

**"Large dataset = AGI robot" -- not yet**
RT-2 is impressive but trained on 130,000 demos. Humans learn manipulation from far
fewer experiences but with richer feedback (proprioception, tactile, social). Current
foundation models are impressive interpolators. Generalization to truly novel situations
remains brittle -- they are not reasoning about physics, they are pattern-matching.

**Sim-to-real works for locomotion, harder for manipulation**
Locomotion sim-to-real: very successful (Spot, MIT Cheetah, ANYmal all use it).
Why: leg contacts are relatively predictable; domain randomization covers the gap.
Manipulation sim-to-real: harder because contact during grasping involves:
fine finger placement (mm-level), surface friction, deformable objects, all of
which are hard to simulate accurately. Current frontier: synthetic data for
pre-grasp pose estimation; actual manipulation still needs real demos.

**Behavioral cloning ≠ the robot understands the task**
A BC policy that achieves 90% success on a tabletop task is approximating the
demonstration distribution, not modeling the task structure. If the task changes
slightly (different lighting, slight object displacement), performance degrades.
The robot has no causal model. This is why large-scale foundation models (RT-2)
matter: the VLM backbone provides semantic priors that reduce this brittleness.

**Domain randomization is not free**
More randomization = more robust policy, but also more training steps needed.
An extremely broad randomization range may prevent the policy from learning the
core task at all (too hard). Adaptive domain randomization (ADR) solves this:
start narrow, expand as policy improves. Implementing ADR properly requires careful
curriculum design.

**Diffusion Policy speed is no longer the bottleneck**
Early diffusion policies required 100 denoising steps per action chunk (10-50ms on GPU).
Flow matching (pi0) reduces this to 1-5 steps. Latency is no longer the main
limitation -- data diversity and deployment hardware (GPU requirement) are.
