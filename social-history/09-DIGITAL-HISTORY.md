# Digital History and Big Data Methods

## The Big Picture

Digital history applies computational methods to historical questions — text mining, network
analysis, geographic information systems (GIS), database construction, and machine learning.
It ranges from digitizing archives to data-driven macro-history. The tools are from computer
science and data science; the questions are historical.

```
+-------------------------------------------------------------------+
|              DIGITAL HISTORY LANDSCAPE                            |
|                                                                   |
|  DATA SOURCES              METHODS                 APPLICATIONS   |
|  +---------------+         +------------------+   +-----------+  |
|  | Digitized     |         | Text mining:     |   | Corpus    |  |
|  | archives      |         | NLP, topic       |   | analysis  |  |
|  | Newspapers    |         | modeling (LDA),  |   |           |  |
|  | Books         |         | word2vec,        |   | Discourse |  |
|  | Census data   |         | sentiment        |   | change    |  |
|  | Maps          |         | analysis         |   |           |  |
|  | Photos        |         +------------------+   | Language  |  |
|  | Social media  |         | GIS: mapping,    |   | change    |  |
|  |               |         | spatial analysis |   |           |  |
|  | Linked        |         +------------------+   | Migration |  |
|  | Open Data     |         | Network analysis:|   | routes    |  |
|  | (genealogy,   |         | social nets,     |   |           |  |
|  | authority     |         | correspondence   |   | Social    |  |
|  | files)        |         | networks         |   | networks  |  |
|  +---------------+         +------------------+   +-----------+  |
|                                                                   |
|  KEY TOOLS AND PROJECTS                                           |
|  +-----------------------------------------------------------+    |
|  | Voyant Tools  |  MALLET (topic model)  |  QGIS / ArcGIS  |    |
|  | Gephi (nets)  |  Google Ngrams  |  JSTOR DFR  |  Palladio  |    |
|  +-----------------------------------------------------------+    |
+-------------------------------------------------------------------+
```

---

## The Digital Turn in Historical Archives

### Mass Digitization

```
  THE SCALE OF DIGITIZATION:
  Google Books (2004-): scanned 40+ million books by 2020.
  HathiTrust: 17+ million volumes from partner libraries.
  Europeana: 58+ million cultural heritage objects.
  Internet Archive: books, web pages, audio, video.
  Newspapers: Chronicling America (Library of Congress), British Newspaper Archive.

  WHAT THIS ENABLES:
  Full-text search across corpora previously requiring decades of manual reading.
  Statistical analysis of word frequencies across time.
  Topic modeling of vast document collections.
  Pattern recognition impossible with manual methods.

  OCR QUALITY ISSUES:
  Optical Character Recognition for historical texts is imperfect.
  Old typefaces, damaged documents, multiple languages: OCR error rates vary.
  Methods must account for systematic OCR errors.
  Machine learning is improving OCR quality dramatically (Transkribus for
  handwritten documents).

  STRUCTURED DATABASES:
  Historical census data (IPUMS: Integrated Public Use Microdata Series).
  Tax records (Medieval and Early Modern Data Bank).
  Trade statistics (Global Price and Income History Group).
  Prosopographies: databases of individuals (SNAP, OCLC Name Authorities).
```

---

## Text Mining and Natural Language Processing

### Computational Analysis of Texts

```
  WORD FREQUENCY ANALYSIS:
  How often does a word appear over time?

  GOOGLE NGRAMS (Michel et al., Science 2011):
  "Culturomics": analysis of word frequencies in 5 million digitized books.
  Showed: rapid changes in cultural references over time.
  Word "men" peaked mid-20th century; word "women" rising.
  Names of individuals rise and fall (fame has a measurable timescale).

  CRITICISM:
  What does raw word frequency mean?
  Context matters: "slavery" rising after 1860 in US books
  might mean more discussion of abolition OR more defense of slavery.
  Raw counts must be interpreted with historical knowledge.
```

### Topic Modeling (LDA)

```
  LATENT DIRICHLET ALLOCATION (LDA):
  Assumes documents are mixtures of topics.
  Topics are distributions over words.
  Algorithm: find the topic distributions that best explain the corpus.

  APPLICATION TO HISTORY:
  Cameron Blevins, "Topic Modeling Martha Ballard's Diary" (2010):
  Used LDA on a 27-year diary to find temporal patterns in topics.
  Medical topics shifted over time; domestic topics remained stable.

  Robert Nelson, Mining the Dispatch (2012):
  LDA on Richmond, VA Confederate newspapers during Civil War.
  Tracked how the war affected civilian discourse over time.

  WHAT LDA DOES:
  Discovers hidden thematic structure in large corpora.
  Not definition-dependent: the topics emerge from the data.
  Can reveal patterns invisible to manual reading.

  LIMITATIONS:
  Topics are probabilistic and require human interpretation.
  Number of topics (k) must be specified; different k gives different results.
  Works best on large, relatively homogeneous corpora.
  Does not capture argument, narrative, irony, or context.
```

### Word Embeddings and Semantic Change

```
  WORD2VEC AND SEMANTIC CHANGE:
  Train word embeddings on historical corpora.
  Word vectors capture semantic relationships.
  Compare word2vec models trained on different time periods.

  WILLIAM HAMILTON et al. (Diachronic Word Embeddings, 2016):
  Trained embeddings on corpora by decade.
  Showed: words change meaning systematically over time.
  "Gay" shifted from positive (merry, cheerful) to referring to
  homosexuality over the 20th century — measurably.
  "Cell" went from biology/prison to technology.

  APPLICATION:
  Track semantic drift of political vocabulary.
  How did "democracy," "freedom," "race" change meaning across centuries?
  Quantitative evidence for claims Koselleck made qualitatively.

  BERT AND CONTEXTUAL EMBEDDINGS:
  Contextualized models (BERT, GPT) understand word meaning in context.
  Historical BERT: trained on historical texts.
  More nuanced than word2vec for historical semantic analysis.
```

---

## Geographic Information Systems (GIS)

### Spatial History

```
  GIS IN HISTORY:
  Map historical data spatially.
  Overlay: physical geography, political boundaries, population, events.
  Temporal dimension: how spatial patterns changed over time.

  RICHARD WHITE (Stanford Spatial History Project):
  Mapping the American West: railroads, settlement, agriculture.
  Visualization reveals patterns invisible in tables or narrative.

  APPLICATIONS:
  Slavery's spatial structure: ArcGIS mapping of slave populations
  and cotton production across the antebellum South.
  Atlantic slave trade: SLATEVOYAGES database + GIS.
  Disease spread: cholera maps (originally John Snow, 1854).
  WWII bombing: visualizing strategic bombing patterns.
  Migration: tracking population movement over time.

  HISTORICAL ATLAS:
  Geographic Information Systems replace traditional historical atlases.
  Dynamic: the viewer can choose what to display and when.
  Interactive: query the data behind the visualization.
  Examples: Atlas of Early Printing, Mapping the Republic of Letters.
```

### Geospatial Databases

```
  KEY DATABASES:
  SLAVEVOYAGES (slavevoyages.org):
  36,000+ documented slave trade voyages.
  Embarkation, disembarkation ports, dates, numbers.
  Enables: mapping the Atlantic slave trade spatially and temporally.

  MAPPING THE REPUBLIC OF LETTERS (Stanford):
  Correspondence networks of early modern European intellectuals.
  Who wrote to whom? From where to where?
  Visualizes intellectual networks and their geography.

  PLEIAS (Pelagios Commons):
  Linked open data for ancient world places.
  Allows: mapping textual references to ancient places across
  thousands of ancient texts.

  PROBLEMS:
  Historical data is messy: place names change, borders shift.
  Historical gazetteers required (place name -> coordinates over time).
  DARE (Digital Atlas of the Roman Empire), World Historical Gazetteer.
```

---

## Network Analysis

### Social Networks in History

```
  NETWORK ANALYSIS:
  Nodes: individuals, places, institutions.
  Edges: relationships, exchanges, communications.
  Metrics: degree, betweenness centrality, clustering, modularity.

  APPLICATION TO INTELLECTUAL HISTORY:
  Correspondence networks: who knew whom?
  Citation networks: who cited whom?
  Co-authorship networks: collaboration patterns.

  MAPPING THE REPUBLIC OF LETTERS:
  Erasmus's correspondence: 1300+ letters to 900+ people.
  Who was central to early modern intellectual life?
  Betweenness centrality: who was a bridge between communities?

  THE EARLY AMERICAN FOREIGN SERVICE (Petitjean):
  Network analysis of early American diplomats.
  Reveals: who had leverage, who was peripheral.

  PADGETT AND ANSELL (American Journal of Sociology, 1993):
  Cosimo de Medici's rise to power in Florence.
  Network analysis: Medici were brokers between otherwise unconnected factions.
  Their structural position (bridging) gave them power beyond their resources.
  Classic application of network theory to historical power.
```

---

## Quantitative Macro-History and Cliodynamics

```
  CLIODYNAMICS (Turchin):
  Mathematical modeling of macro-historical dynamics.
  (See also Module 04: Quantitative History for full treatment.)

  "AGES OF DISCORD" (Turchin, 2023):
  Structural-demographic theory applied to US history.
  Data: real wages, elite numbers, state finances, political instability.
  Model: rising inequality -> elite overproduction -> political instability.
  Applied to the 2020s: predicted peak instability.

  DATABASE:
  Seshat: Global History Databank.
  Systematic quantitative data on past societies.
  Tests: what variables correlate with social complexity, stability?

  PIKETTY AND HISTORICAL INEQUALITY:
  Thomas Piketty (Capital in the 21st Century, 2013):
  Long-run inequality data from tax records.
  France, UK, US back to 1800s.
  r > g: return on capital exceeds growth rate -> inequality increases.
  Historical dataset enabled the argument.
```

---

## Digital Public History and Crowdsourcing

```
  WIKIPEDIA AS HISTORICAL RECORD:
  The most consulted historical reference.
  Open editing: strengths and weaknesses.
  Point of View (POV) problems in contested historical events.
  Research: Wikipedia is internally consistent but has systematic gaps
  (less coverage of non-Western, female, non-English topics).

  CROWDSOURCED TRANSCRIPTION:
  Transcription of historical handwritten documents.
  Zooniverse: galaxy classification -> historical document transcription.
  NYPL Building Inspector: crowdsourced georectification of historical maps.
  FromThePage: platform for crowdsourced transcription.

  ORAL HISTORY DIGITAL:
  StoryCorps: crowdsourced oral history archive.
  Densho: Japanese American WWII internment oral histories.
  Voice of Witness: human rights oral histories.

  SOCIAL MEDIA AS HISTORICAL SOURCE:
  The Internet Archive's web crawls (Wayback Machine).
  Twitter Academic API: archive of tweets.
  Challenges: ephemerality, volume, format, provenance.
  "Digital dark age": the fragility of born-digital records.
```

---

## Limitations and Critiques

```
  THE DIGITAL HUMANITIES DEBATES:

  WHIG DIGITAL HISTORY:
  Treating "more data" and "better methods" as inherently producing
  better history. Scales Whig history to quantitative level.

  CULTURAL ANALYTICS CRITIQUE (Nan Z. Da, 2019):
  Argued that most computational literary/historical claims are
  statistically fragile, methodologically flawed, or trivially confirmed.
  The methods don't add to what close reading already showed.
  Response: some Digital Humanities scholars accepted some criticisms.

  THE "GARBAGE IN, GARBAGE OUT" PROBLEM:
  Historical data is biased before it is collected.
  What was recorded? Who recorded it? What was lost?
  Google Books: overrepresents certain periods, languages, genres.
  Digitization is not random sampling.

  INTERPRETIVE THINNESS:
  Text mining reveals patterns; it doesn't explain them.
  The pattern requires historical interpretation.
  Risk: mistaking correlation for significance; finding patterns without meaning.

  THE MATTHEW EFFECT IN DIGITIZATION:
  Well-funded archives with English-language materials are best digitized.
  African, Asian, indigenous, oral historical traditions: underrepresented.
  Digital history can amplify existing historiographical biases.
```

---

## Tools and Infrastructure

```
  TEXT ANALYSIS:
  Voyant Tools (web): frequency, concordance, trends.
  MALLET: command-line topic modeling.
  spaCy, NLTK: Python NLP libraries.
  R: tidytext, stm (structural topic models).

  GIS:
  QGIS: free, open-source desktop GIS.
  ArcGIS: commercial; widely used in academic GIS.
  Leaflet.js, Mapbox: web mapping.
  ESRI Story Maps: narrative + map.

  NETWORK ANALYSIS:
  Gephi: interactive network visualization.
  NetworkX (Python): analysis.
  Palladio (Stanford): humanities network visualization, user-friendly.

  DATABASES:
  MySQL / PostgreSQL: structured historical data.
  Omeka: collections management for digital archives.
  CollectiveAccess: museum/archive collections.
  Recogito: annotation of historical texts with place names.

  MACHINE LEARNING:
  Transkribus: HTR (Handwritten Text Recognition) for historical documents.
  ImageNet / ResNet fine-tuned for historical photographs.
  Named entity recognition (NER) for people, places in historical texts.
```

---

<!-- @editor[structure/P2]: No comparison tables beyond the Decision Cheat Sheet — a table comparing text mining vs. GIS vs. network analysis (input data, method, output, typical question, limitations) would help the learner pick the right approach -->
## Decision Cheat Sheet

| I want to do... | Use |
|---|---|
| Find word frequency trends in historical texts | Google Ngrams, Voyant Tools |
| Topic modeling of a document corpus | MALLET, Python stm |
| Detect semantic change in vocabulary over time | Diachronic word embeddings (word2vec) |
| Map historical data spatially | QGIS, ArcGIS, Palladio |
| Analyze historical correspondence networks | Gephi, Palladio |
| Access digitized historical newspapers | Chronicling America, British Newspaper Archive |
| Access historical census data | IPUMS, national census archives |
| Transcribe handwritten historical documents | Transkribus |
| Study Atlantic slave trade spatially | SLAVEVOYAGES database |
| Apply quantitative macro-history models | Turchin (Seshat, Ages of Discord) |

---

<!-- @editor[bridge/P2]: No old-world -> new-world bridge — the learner's CS/data science background makes this the most natural bridge point in the entire directory: topic modeling (LDA) is a generative probabilistic model the learner knows from ML; word2vec is familiar from NLP; regression/IV/RD are standard causal inference; GIS is spatial databases; network analysis is graph theory — connect these tools explicitly to their CS foundations rather than presenting them as "digital humanities" novelties -->
## Common Confusion Points

**Digital history is not the same as digitization.**
Digitization = scanning and making accessible. Digital history = using computational
methods to ask historical questions. A digitized archive is raw material; digital history
is the analysis.

**Topic modeling does not "understand" texts.**
LDA finds statistical patterns of word co-occurrence. It does not understand argument,
context, irony, or meaning. The topics it produces require human interpretation. The
method surfaces patterns; the historian explains them.

**"Big data" in history has different validation than in natural science.**
Historical data is not generated by controlled processes. Selection bias (what survived,
what was recorded) is structural, not random. Methods that assume random sampling
are often misapplied to historical corpora.

**Computational methods can confirm, refute, or nuance existing claims.**
The best digital history does not just confirm what we already know. Blevins's Martha
Ballard analysis revealed patterns invisible to manual reading. The question is whether
the computational method adds to what close reading and traditional analysis could achieve.
