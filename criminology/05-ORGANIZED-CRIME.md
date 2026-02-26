# Organized Crime and Networks

## The Big Picture

Organized crime is sustained criminal enterprise -- groups that use violence, corruption, and organizational structure to run illegal markets or extract resources. The key analytical challenge: it resists easy categorization because it ranges from hierarchical bureaucracies to fluid network arrangements, and it constantly adapts to law enforcement pressure.

```
+------------------------------------------------------------------+
|                ORGANIZED CRIME LANDSCAPE                         |
+------------------------------------------------------------------+
|                                                                  |
|  ORGANIZATIONAL FORMS            ILLICIT MARKETS                 |
|  ===================             ===============                 |
|  Hierarchical (Mafia model)      Drugs (cocaine, heroin, meth,   |
|  Network (loose confederacy)       fentanyl, cannabis)           |
|  Hybrid (core + periphery)       Human trafficking               |
|                                  Weapons trafficking             |
|  GEOGRAPHIC SCOPE                Cybercrime (ransomware)         |
|  ================                Counterfeit goods               |
|  Local (street gangs)            Extortion / protection          |
|  Regional (Mexican cartels)      Gambling / loan-sharking        |
|  Transnational (Italian,                                         |
|    Russian, Chinese, Japanese)   ENABLING CONDITIONS             |
|                                  ===================             |
|  THEORETICAL APPROACHES          State weakness / corruption     |
|  =====================           Prohibition / illegality        |
|  Alien conspiracy (now outdated) High demand + low supply        |
|  Ethnic succession               Geographic/border position      |
|  Market/enterprise model         Ethnic/kinship trust networks   |
|  Network analysis                                                |
+------------------------------------------------------------------+
```

---

## Definitional Challenge

```
  WHAT MAKES CRIME "ORGANIZED"?
  ==============================

  Minimum criteria (most scholars):
  1. Three or more persons
  2. Acting together over time (ongoing)
  3. For material benefit
  4. Using violence, corruption, or intimidation

  Contested elements:
  - How hierarchical must structure be?
  - Is a street gang "organized crime"?
  - Does racketeering (protection) = organized crime even
    without drug markets?

  FBI definition: Groups that meet RICO criteria
  (enterprise + pattern of racketeering activity)

  RICO (Racketeer Influenced and Corrupt Organizations Act, 1970):
    Revolutionary legal tool -- targets the enterprise, not
    just individual acts. Allows prosecution of leaders who
    ordered crimes they didn't personally commit.
```

---

## Theoretical Models

### Alien Conspiracy Theory (now largely discredited as sole explanation)

```
  TRADITIONAL "MAFIA" MODEL (1960s-1970s dominant view)
  ======================================================

  Organized crime = foreign criminal imports
  - Italian-American Mafia (La Cosa Nostra)
  - External threat to otherwise clean society

  Structure:
  Boss (Don)
    |
    v
  Underboss
    |
    v
  Consigliere (advisor)
    |
  +--+--+
  v     v
Capos  Capos
  |
  v
Soldiers (made members)
  |
  v
Associates (non-members)

  Problems with this model:
  - Ignores indigenous organized crime (non-ethnic)
  - Overstates hierarchy (most OC is looser)
  - Obscures demand-side: Americans buy the drugs/services
  - Ignores corruption of legitimate institutions
```

### Ethnic Succession Theory (Bell, Ianni)

```
  ETHNIC SUCCESSION MODEL
  =======================

  Organized crime is a "queer ladder of mobility"
  (Daniel Bell, 1953)

  Each immigrant wave uses OC as upward mobility path
  when legitimate routes are blocked:

  1890-1930:  Irish dominate machine politics and crime
  1920-1960:  Italian immigrants dominate (Prohibition era)
  1960s-on:   Black, Puerto Rican, Colombian cartels
  1980s-on:   Russian, Vietnamese, Chinese organized crime
  2000s-on:   Mexican cartels, MS-13, cybercrime networks

  Pattern: Each group eventually achieves mainstream success
  and exits crime; next marginalized group fills the niche.

  Critique: Essentializes ethnicity; ignores that crime is
  available to any group, not inherent to immigrant status.
```

### Enterprise Theory (Smith, Reuter)

The market model: organized crime is entrepreneurship in illegal markets. Use standard industrial organization analysis.

```
  ILLEGAL MARKETS = MARKETS
  ==========================

  Supply and demand apply.
  Entry barriers (violence, corruption, trust)
  = normal barriers to competition, just informal.

  Market structure:
  +----------------------------------+
  |  Monopoly (single supplier)      |
  |  Oligopoly (few cartels)         |
  |  Competition (many street dealers|
  |  with thin margins)              |
  +----------------------------------+

  Violence is a transaction cost:
    Contract disputes between criminals can't go to court.
    Violence enforces agreements.
    High violence = inefficient market, high enforcement cost.

  Reuter's finding: Most drug markets are NOT monopolies.
    They are competitive with thin margins for street dealers.
    Kingpins capture economic rents; street dealers earn near
    minimum wage (Levitt & Venkatesh, 2000 -- Freakonomics data)
```

---

## Network Analysis Approach

**Graph-theory bridge:** Criminal network analysis is applied graph theory — the same centrality metrics from network science and social network analysis in CS. Degree centrality (number of direct connections) identifies high-volume nodes. Betweenness centrality (fraction of all shortest paths passing through a node) identifies brokers and information gatekeepers — removing a high-betweenness node fragments the network more effectively than removing a high-degree node that is peripheral. Clustering coefficient measures local density: high clustering means tight clique with limited external reach; low clustering with high betweenness identifies bridge nodes that span otherwise disconnected components. Scale-free networks (power-law degree distribution, as seen in many criminal networks) are robust to random node removal but fragile to targeted hub removal — the classic preferential attachment graph property. Law enforcement "kingpin strategies" are targeted attacks on high-betweenness hubs; the empirical finding that these often increase violence (by destabilizing the market hierarchy) mirrors the network-theory prediction that hub removal in a scale-free network creates fragmentation and competitive instability among the remaining nodes.

Modern criminology uses social network analysis to map criminal organizations without assuming hierarchy.

```
  NETWORK PROPERTIES OF CRIMINAL ORGANIZATIONS
  =============================================

  NODE = individual criminal actor
  EDGE = relationship (kinship, transaction, co-offending)

  Key metrics:
  +------------------+----------------------------------------+
  | Degree centrality| Number of direct connections          |
  |                  | High degree = potential broker or hub  |
  +------------------+----------------------------------------+
  | Betweenness      | How often on shortest paths between    |
  | centrality       | others. High = information gatekeeper  |
  +------------------+----------------------------------------+
  | Clustering coeff | How many of your contacts know each    |
  |                  | other. High = tight clique, low trust- |
  |                  | radius; low = bridge/broker position   |
  +------------------+----------------------------------------+
  | Resilience       | Does network survive node removal?     |
  |                  | Scale-free networks survive random     |
  |                  | attacks but vulnerable to hub removal  |
  +------------------+----------------------------------------+

  Law enforcement implication: Identify and remove
  high-betweenness nodes (brokers) to fragment network.
```

---

## Major Organized Crime Groups

### The American Mafia (La Cosa Nostra)

```
  PEAK (1950s-1970s):
  Five NYC families (Gambino, Lucchese, Bonanno,
  Colombo, Genovese) plus Chicago Outfit, others.
  National Commission coordinated major decisions.

  DECLINE MECHANISMS (1980s-2000s):
  - RICO prosecutions: enterprise liability made it
    possible to convict bosses for subordinates' crimes
  - Informants: Sammy Gravano, Henry Hill, Jimmy Hoffa
    testimony. Omerta (silence code) eroded
  - FBI surveillance: Appalachin meeting (1957) tipped
    off FBI to national organization
  - Generational change: Italian-American integration
    into mainstream = ethnic succession complete
  - Competition: Drug cartels, Russian mobs, gangs

  STATUS: Much diminished but not eliminated.
  NYC families still exist; extortion of construction
  industry continues; but compared to 1960s peak: minor.
```

### Mexican Drug Cartels

```
  EVOLUTION:
  1980s:  Guadalajara Cartel (Félix Gallardo) -- consolidates
  1989:   Splits into Tijuana, Sinaloa, Juárez cartels
  2000s:  Sinaloa (El Chapo Guzmán) becomes dominant
          Los Zetas emerge (ex-military special forces)
          Extreme violence -- territorial wars
  2010s:  Jalisco New Generation, Sinaloa sub-cartels
          Diversification: extortion, kidnapping, fuel theft

  VIOLENCE MECHANISM:
  - Political fragmentation (PRI regime collapse)
    removed corrupt but stabilizing state-cartel arrangement
  - Competition among multiple cartels with US DEA
    pressure pushing fragmentation
  - Los Zetas introduced military tactics + extreme violence
    as market discipline tool

  US SUPPLY CHAIN:
  Mexico --> border crossing points (now fentanyl primarily
  through ports of entry, not smuggled in vehicles) -->
  US distribution networks
```

### Russian Organized Crime

```
  ORIGIN: Post-Soviet collapse (1990s)
  Vory v Zakone (thieves-in-law) -- prison code
  enforced criminal hierarchy

  DISTINGUISHING FEATURE:
  Deep penetration of state apparatus.
  Not just corrupting police -- actually staffing
  government positions and businesses.
  "State capture" rather than just bribery.

  ACTIVITIES:
  - Fuel excise tax fraud (billions in EU)
  - Cybercrime (ransomware, banking trojans)
  - Money laundering through real estate
  - Arms trafficking (post-Soviet weapons)
  - Trafficking in persons

  TRANSNATIONAL: Operations in US, Israel, Western Europe,
  former Soviet states -- ethnically connected diaspora
  networks as trust infrastructure.
```

---

## Human Trafficking

The most serious human rights violation in organized crime analysis.

```
  TRAFFICKING TYPES
  =================

  LABOR TRAFFICKING              SEX TRAFFICKING
  ================               ==============
  Forced labor in:               Commercial sexual
  Agriculture, domestic          exploitation through
  work, construction,            force, fraud, or
  manufacturing                  coercion

  TRAFFICKING vs. SMUGGLING
  =========================

  Smuggling:                     Trafficking:
  Facilitating illegal           Exploitation is the
  migration (migrant             point; migration is
  consents)                      means or incidental

  Trafficking does not require
  movement across borders.
  Domestic trafficking is common.

  SUPPLY SIDE FACTORS:
  - Poverty, instability, conflict
  - Gender inequality
  - Social exclusion

  DEMAND SIDE FACTORS:
  - Sex tourism, commercial sex markets
  - Demand for cheap unregulated labor
  - Consumer supply chains (unmonitored)
```

---

## Cybercrime as Organized Crime

The newest major criminal market, with distinct organizational features.

```
  CYBERCRIME ECONOMY
  ==================

  DARK WEB MARKETS          RANSOMWARE-AS-A-SERVICE (RaaS)
  ================          ==============================

  Silk Road (2011-2013):    Criminal firms offer:
  First major darknet market  - Malware toolkit
  ~$1.2B in drug sales      - Infrastructure (C2 servers)
  Ross Ulbricht arrested    - Money laundering
                            - Customer service (!)
  Hydra Market (Russian):
  ~$1B/year before seized   Developers get 20-30% of ransom
  2022                      Affiliates get 70-80%

  Trust mechanisms in        --> Industrialized crime
  anonymous markets:         Conti, REvil, LockBit, ALPHV
  - Escrow services            operated like franchises
  - Reputation ratings
  - Community enforcement    Attribution: Russia/CIS-based,
  Mirror classical market    operating with state tolerance
  institutions

  CRYPTOCURRENCY LAUNDERING
  ==========================

  Three primary methods:
  1. MIXERS / TUMBLERS: Pool transactions from multiple
     wallets, redistribute in fractional amounts.
     Breaks the on-chain traceability.
     Tornado Cash: largest Ethereum mixer; OFAC sanctioned 2022.

  2. CHAIN-HOPPING: Convert BTC -> privacy coin (Monero) ->
     BTC through cross-chain bridges. Monero's ring signatures
     provide cryptographic anonymity. Lazarus Group (DPRK)
     used this extensively after Ronin bridge hack ($625M).

  3. CRYPTO-TO-CASH: Over-the-counter brokers, P2P exchanges
     with weak KYC, illicit casinos, VASP (virtual asset service
     providers) in low-regulation jurisdictions (BITZLATO, 2023).

  CHAINALYSIS estimate: ~$24B laundered via crypto in 2023.
  On-chain analytics has made large-scale laundering harder
  but not impossible; privacy coins remain a significant gap.

  STATE-SPONSORED CYBERCRIME
  ===========================

  STATE ACTOR       GROUPS              NOTED OPERATIONS
  -----------       ------              ----------------
  DPRK              Lazarus Group,      Ronin bridge ($625M, 2022)
  (North Korea)     Kimsuky, APT38      Sony Pictures (2014)
                                        WannaCry (2017)
                                        Crypto exchanges (ongoing)

  Revenue function: Lazarus operations estimated to have
  generated $3B+ in crypto for DPRK's weapons program
  (UN Panel of Experts). State-sponsored cybercrime here is
  literally sanctions evasion and weapons proliferation financing.

  RUSSIA             APT28 (Fancy Bear)  DNC hack (2016)
                     APT29 (Cozy Bear)   SolarWinds (2020)
                     Sandworm            NotPetya ($10B+ damages)
                     Turla               Ukraine power grid (2015-16)

  Russia: distinguishes between espionage/disruption (FSB/GRU)
  and financially motivated cybercrime (tolerated if
  not targeting CIS nations). The tolerance creates ambiguity
  that complicates attribution and enforcement.

  CHINA              APT10, APT41        Microsoft Exchange (2021)
                                         OPM hack (22M records, 2015)
                                         IP theft across sectors
```

---

## Decision Cheat Sheet

| Analytical Need | Best Framework | Key Insight |
|----------------|---------------|-------------|
| Explaining structure | Enterprise theory | OC = business in illegal market |
| Mapping relationships | Network analysis | Betweenness centrality identifies key nodes |
| Understanding violence | Transaction cost theory | Violence enforces contracts |
| Explaining origins | Ethnic succession | Marginalized groups use crime as mobility path |
| Targeting enforcement | RICO / conspiracy law | Enterprise liability for leadership |
| Understanding cyber | RaaS model | Industrialized, franchised crime |

---

## Common Confusion Points

**Organized Crime Is Not One Thing**
The "Mafia" model projects a single hierarchical image onto extremely varied phenomena. Mexican cartels, Russian mafias, cybercriminal networks, and street gangs are all "organized crime" but have very different structures, markets, and vulnerabilities.

**Violence Signals Market Failure**
High violence in drug markets is NOT the normal state -- it signals competitive instability. Monopolistic or oligopolistic drug markets (like the stable Sinaloa era) have lower violence because enforcement is internal. Drug war fragmentation that creates competition increases violence.

**Street Dealers Are Not Rich**
The Levitt/Venkatesh analysis of Chicago gang finances showed the average foot soldier earned less than minimum wage while taking enormous personal risk. The gang's economic structure is pyramid-like: most of the money flows up. The visible lifestyle of kingpins is not representative.

**Trafficking Does Not Require Transnational Movement**
A common misconception: trafficking must involve border crossing. The Trafficking Victims Protection Act and international law define trafficking by exploitation (force, fraud, coercion) not geography. Domestic trafficking of US citizens is common and frequently prosecuted.
