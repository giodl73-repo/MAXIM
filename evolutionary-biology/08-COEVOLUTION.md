# Coevolution and Arms Races

## The Big Picture

Coevolution is reciprocal evolutionary change in two or more species, each acting as
a selective agent on the other. It drives some of the most spectacular adaptations
in biology — and some of the most rapid evolutionary change.

```
┌──────────────────────────────────────────────────────────────────┐
│                   COEVOLUTION LANDSCAPE                           │
│                                                                    │
│  TYPE              INTERACTION      EXAMPLE                      │
│  ────              ───────────      ───────                      │
│  Arms race         Antagonistic     Predator-prey                │
│  (+ / -)           parasite-host    Toxin-resistance             │
│                    pathogen-host    Parasite virulence           │
│                                                                    │
│  Mutualism         Cooperative      Plant-pollinator             │
│  (+ / +)                            Fig-fig wasp                 │
│                                    Mycorrhizal fungi              │
│                                                                    │
│  Red Queen         Parasites drive  Sexual reproduction          │
│                    host diversity   MHC diversity                │
│                                                                    │
│  Cospeciation      Parallel clade   Figs & fig wasps            │
│                    divergence       Pocket gopher lice           │
│                                                                    │
│  KEY TENSION: coevolution happens at population level            │
│  Geographic mosaic: different outcomes in different locations    │
└──────────────────────────────────────────────────────────────────┘
```

---

## Arms Races

### The Concept

In an antagonistic interaction, each party evolves adaptations that overcome the
other's defenses. Each evolutionary step by one party selects for counter-adaptations
in the other.

```
  Classic prey example: Taricha newts and Garter snakes (Brodie & Brodie)
  ─────────────────────────────────────────────────────────────────────
  Taricha (rough-skinned newt): produces tetrodotoxin (TTX)
  TTX: blocks voltage-gated sodium channels → paralyzes predator → lethal
  Some populations: one newt contains enough TTX to kill 25 humans

  Thamnophis (garter snake): evolved resistance to TTX
  Mechanism: amino acid substitutions in Nav1.4 sodium channel
  (same gene affected in human congenital myotonias)

  GEOGRAPHIC MOSAIC:
  ──────────────────
  Different populations show different co-evolutionary states:
  - California coast: very toxic newts + very resistant snakes (co-evolutionary hotspot)
  - Idaho: mildly toxic newts + little resistance (cold spot)
  - Allopatric snake populations: no resistance at all

  COST OF RESISTANCE:
  ────────────────────
  High resistance = slower locomotion in snakes (reduced nerve conduction)
  → Natural selection against resistance where newts are not present or mild
  → Resistance only spreads where newt predation is the dominant mortality source
```

### Evolutionary Arms Race Dynamics

```
  Simple two-species model:

  Attack ability (predator/parasite): a(t) evolves upward by Δa per generation
  Defense ability (prey/host): d(t) evolves upward by Δd per generation

  If Δa > Δd: parasite wins — host extinction or coexistence with high parasite load
  If Δd > Δa: host wins — parasite extinction
  If Δa ≈ Δd: Red Queen dynamics — continuous co-evolution without either winning

  The "Red Queen" (Van Valen 1973): species must keep evolving just to maintain
  relative fitness against co-evolving enemies. Standing still = extinction.
```

---

## Red Queen Hypothesis

Van Valen observed that extinction probability is roughly constant over time
regardless of lineage age. He proposed a biotic treadmill: the environment (biotic)
never stops changing because all species are co-evolving with each other.

### Red Queen and the Evolution of Sex

Hamilton and others applied Red Queen to explain why sexual reproduction is so
widespread despite its "two-fold cost":

```
  TWO-FOLD COST OF SEX:
  ──────────────────────
  Asexual female: 100% of offspring are daughters who reproduce
  Sexual female:  50% sons, 50% daughters → only half as many reproductive offspring
  → Asexual clones should spread twice as fast
  → Why does sex persist? This is the "queen of evolutionary problems"

  RED QUEEN RESOLUTION:
  ──────────────────────
  Parasites track host genotypes:
  - Common host genotype = common target
  - Parasite adapts to infect the common genotype
  - Offspring produced asexually all share mother's genotype → all vulnerable
  - Offspring produced sexually have shuffled genomes → diverse genotypes
  - Rare genotypes are harder to infect (moving target)

  Sexual reproduction generates the genetic diversity that makes populations
  harder for parasites to track.

  EVIDENCE:
  ──────────
  New Zealand snail Potamopyrgus antipodarum:
  - Sexual and asexual forms coexist
  - Sexual reproduction more common in high-parasite (trematode) habitats
  - Frequency of asexual clones fluctuates with parasite load (Hamilton et al.)
```

### Red Queen and MHC Diversity

```
  MHC (Major Histocompatibility Complex):
  ──────────────────────────────────────
  Most polymorphic region in vertebrate genomes
  Humans: HLA locus — >2,000 alleles at HLA-B alone

  Why so diverse?
  Balancing selection driven by pathogens:
  - Each MHC allele presents a different range of pathogen peptides
  - Common allele: pathogens evolve to escape that allele's binding
  - Rare allele advantage: harder to escape, fitness increases when rare
  - → Frequency-dependent selection maintains diversity
  - → Trans-species polymorphism: some MHC alleles are shared between
      humans and chimpanzees (older than the species split!)

  MHC diversity measures: extraordinary standing variation maintained by
  pathogen-driven frequency-dependent selection. The same mechanism
  operates at immune receptor loci in vertebrates globally.
```

---

## Host-Parasite Coevolution

### Virulence Evolution

Why do parasites (including pathogens) not simply kill their hosts as fast as possible?

```
  TRANSMISSION-VIRULENCE TRADE-OFF:
  ──────────────────────────────────
  Virulence (harm to host) is often linked to transmission rate:
  - Higher within-host replication → more transmission opportunity
  - Higher within-host replication → faster host death (less time to transmit)

  Optimal virulence:  maximize R₀ = β / (α + μ)
    β = transmission rate (increases with virulence)
    α = host death rate from infection (increases with virulence)
    μ = natural host death rate

  Result: intermediate virulence is often optimal
  Prediction: obligate pathogens (no free-living stage) should evolve lower
              virulence than facultative pathogens

  CLASSIC EXAMPLE: Myxoma virus in Australian rabbits
  ────────────────────────────────────────────────────
  1950: introduced as biocontrol for introduced European rabbits
  Original strain: >99% mortality
  By 1958: strain virulence reduced; rabbit resistance increased
  Both populations co-evolved toward intermediate virulence and resistance
  → textbook example of rapid coevolutionary change in a managed context
```

---

## Mutualism — Coevolution with Benefit

Not all coevolution is arms race. Many interactions are mutualistic (both species benefit).

### Plant-Pollinator Coevolution

```
  POLLINATOR SYNDROMES:
  ─────────────────────
  Bee-pollinated: blue/yellow flowers, landing platform, nectar guide UV patterns
  Butterfly: deep red/orange tubular flowers (long proboscis)
  Moth: white, night-blooming, strong scent (night-flying)
  Hummingbird: red/orange tubular (long bill), no scent needed (color vision)
  Fly (dung fly): dull brown/purple, smell like rotting meat (deceptive mimicry)

  Each syndrome evolved by reciprocal selection:
  - Pollinator more efficient at accessing reward → plant benefits from specialization
  - Flower morphology specializes → pollinator evolves matching morphology

  DARWIN'S ORCHID: predicted the existence of Xanthopan morgani praedicta
  Madagascar orchid (Angraecum sesquipedale) has 30-cm nectar spur
  Darwin predicted: a moth must exist with 30-cm proboscis
  Discovery: 21 years after Darwin's death — Xanthopan (hawk moth)
  Mechanism confirmed: X. morgani praedicta, proboscis extends ~25-30 cm
```

### Fig-Fig Wasp Mutualism

The most specialized mutualism known:
- Each of ~700 Ficus species has its own wasp species (Agaonidae)
- Wasp pollinates the fig (enters, deposits pollen, lays eggs)
- Fig provides wasp larvae with food
- Phylogenies of figs and wasps are largely concordant — parallel speciation

But the mutualism is also a conflict: cheating wasps (lay eggs without pollinating)
exist; figs abort fruits with too many wasp eggs.

---

## Geographic Mosaic of Coevolution

Thompson's theory: coevolution does not happen uniformly across a species' range.

```
  HOT SPOTS: local coevolutionary dynamics — both species respond to selection
             from each other. High toxin + high resistance (Taricha/Thamnophis)

  COLD SPOTS: one or both species absent, or interaction not reciprocal
             Plain populations where Taricha lacks predators, TTX is low

  OUTCOME:
  ─────────
  Coevolution is locally variable, creating a geographic mosaic of outcomes.
  The overall trajectory of the interaction is determined by gene flow between
  hot spots and cold spots.

  This explains why population samples of interacting species often show
  inconsistent (variable) coevolutionary outcomes across the range.
```

---

## Cospeciation vs. Host Switching

When host and parasite speciate together, their phylogenies should be congruent.

```
  COSPECIATION:
  ─────────────
  Host species A splits into A1 and A2
  Parasite species B (on A) splits into B1 (on A1) and B2 (on A2)
  → Parallel cladogenesis → congruent phylogenies

  TEST: compare parasite phylogeny with host phylogeny
  Significant topological congruence → cospeciation has occurred
  Tools: Jane (cophylogenetics), ParaFit (matrix correlation)

  HOST SWITCHING:
  ───────────────
  Parasite transfers to a new host (not its ancestral host lineage)
  Results in incongruence between host and parasite trees
  Common in viruses (cross-species transmission events)

  REALITY:
  ────────
  Both cospeciation and host switching occur.
  Human lice and chimpanzee lice: cospeciated with hominids (mitochondrial
  lice diverged when human and chimp lineages diverged ~6 mya)
  BUT: human pubic lice (Pthirus pubis) are more closely related to gorilla
  lice than to human head lice → host switch from gorilla to human lineage
```

---

## Decision Cheat Sheet

| Scenario | Framework | Key prediction |
|----------|-----------|---------------|
| Why does toxin-resistance evolve? | Arms race, geographic mosaic | Resistance where toxin is high |
| Why is sex maintained? | Red Queen + parasites | Sex more common in high-parasite environments |
| Why is MHC so diverse? | Frequency-dep. selection | Rare allele advantage |
| Why don't pathogens always kill hosts? | Transmission-virulence tradeoff | Intermediate virulence optimal |
| Do parasite/host phylogenies match? | Cospeciation analysis | Congruent if cospeciated |
| Why is this flower tube so long? | Plant-pollinator coevolution | Pollinator with matching morphology |

---

## Common Confusion Points

**Arms races don't always escalate to extremes.** Multiple factors limit escalation:
costs of defense, other selective pressures, and the geographic mosaic effect (cold
spots do not drive escalation). Real arms races cycle around intermediate levels
rather than escalating without bound.

**Mutualism is not always stable.** Mutualisms are inherently vulnerable to cheating.
A plant-pollinator mutualism is vulnerable to a pollinator that takes nectar without
depositing pollen. Stability requires mechanisms that reward cooperation and punish
defection — the same logic as in game theory / evolution of cooperation.

**Red Queen and good-genes sexual selection are not mutually exclusive.** Both can
drive sex simultaneously. The Red Queen focuses on parasite resistance (time-varying
selection favoring diversity). Good-genes focuses on broadly fit mates (consistent
direction selection). Both predict choosy females.

**Cospeciation does not imply obligate association.** Even if host and parasite
phylogenies are congruent, the parasite may still survive on multiple hosts. The
congruence just means that speciation events were temporally associated.

**Virulence is not fixed.** It evolves under selection driven by the transmission-
virulence trade-off and the host's immune response. Managing disease evolution
(e.g., vaccination policy) can shift the selective environment and alter virulence
evolution trajectories — this is applied evolutionary medicine.
