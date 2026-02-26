# Digital Preservation: Recording, Archives, Language Revitalization

## The Big Picture

```
DIGITAL PRESERVATION LANDSCAPE FOR ORAL TRADITION
===================================================

+------------------------------------------------------------------+
|  DOCUMENTATION PIPELINE                                          |
|                                                                  |
|  COMMUNITY       FIELDWORK        PROCESSING       ARCHIVE       |
|  ---------       ---------        ----------       -------       |
|  Living          Recording        Transcription    Long-term     |
|  tradition       (audio/video)    Annotation       deposit       |
|  bearers         Metadata         Translation      Access        |
|  at risk         capture          Analysis         Repatriation  |
+------------------------------------------------------------------+
                                                          |
                                    +---------------------+
                                    |
                              REVITALIZATION
                              (separate process --
                               documentation != revitalization)
                                    |
                              Community-controlled
                              language programs
                              Immersion schools
                              Speaker-to-learner
```

**The critical distinction**: language documentation and language revitalization are different activities. Documentation produces an archive; revitalization rebuilds a speaking community. Documentation helps revitalization but cannot replace it.

---

## Recording Standards

```
ARCHIVAL AUDIO STANDARDS
==========================

MINIMUM ARCHIVAL QUALITY:
  Format: PCM WAVE (uncompressed)
  Bit depth: 24-bit (vs. CD-quality 16-bit)
    -> 24-bit preserves more dynamic range
    -> Future technology can use the extra information
  Sample rate: 96 kHz (vs. CD-quality 44.1 kHz)
    -> Captures full ultrasonic range
    -> Downsampling to 44.1 is lossless; upsampling is not
  File format: .WAV (not .MP3, .AAC, .OGG -- those are lossy)

WHY THESE STANDARDS MATTER:
  MP3 is lossy -- it permanently discards frequency data
  You cannot recover what was discarded
  A 128kbps MP3 of an elder's last performance
  is an unrecoverable loss of linguistic data
  Tonal languages (Mandarin, Yoruba, Vietnamese) especially
  sensitive -- tonal distinctions are in frequency ranges
  that lossy compression may degrade

VIDEO STANDARDS:
  Minimum: 1080p, H.264 encoding in container (MKV or MP4)
  Archival preferred: ProRes 422 or lossless H.264
  Audio track: separate 24-bit/96kHz audio preferred
  Lighting: document that gesture and facial expression are visible
    (embodied knowledge -- see 07-PERFORMANCE.md)

STORAGE:
  3-2-1 rule: 3 copies, 2 media types, 1 offsite
  Format migration: required every ~10 years
    (formats become unreadable; hardware changes)
  WAVE file at 24-bit/96kHz: ~1 GB per 30 minutes
    (manageable at current storage costs)
```

---

## Metadata Schemas

Documentation without metadata is nearly unusable:

```
METADATA REQUIREMENTS
======================

MINIMUM METADATA (per recording):
  Who: speaker name, birth date/place, language(s) spoken
  What: genre (narrative, song, conversation, ritual)
  When: date of recording, date of content (if historical)
  Where: recording location; location of described content
  Why: context of recording; occasion
  How: equipment, interviewer name

OLAC (Open Language Archives Community):
  International standard for language resource metadata
  Extends Dublin Core (standard library metadata)
  Adds: linguistic type, content language, subject language
  Required by major archives (AILLA, PARADISEC, ELAR)

IMDI (ISLE Metadata Initiative):
  More detailed than OLAC
  Session-level and corpus-level metadata
  Used by ELAR (Endangered Languages Archive)
  Handles complex multi-participant recordings

LANGUAGE CODES:
  ISO 639-3: three-letter codes for 8,000+ languages
  Glottocode: Glottolog unique identifier for each language
  Both systems needed: ISO for broad use; Glottolog for research
  Why: some languages have multiple names and disputed boundaries
    (what counts as a dialect vs. separate language)
    Glottolog attempts principled classification

SPEAKER METADATA:
  Age, gender, geographic origin affect linguistic variables
  "Consultant" is preferred term over "informant" (implies police)
  Consent documentation: stored WITH the recording metadata
```

---

## Major Archives and Platforms

### Endangered Archives Programme (EAP)

```
EAP — BRITISH LIBRARY
======================

Funder: Arcadia Fund (until 2022); now transitioning
Administrator: British Library, London
Focus: endangered materials in all media
       (not exclusively language -- also manuscripts, film, photos)
       with emphasis on materials in risk of physical loss

Grants awarded: 500+ grants, 80+ countries
Types: pilot (small), major (large-scale)
Output: all materials deposited in British Library AND
        returned to originating community (digital copy)
Web: eap.bl.uk

What makes it distinctive:
  - Not language-exclusive (any endangered cultural material)
  - Repatriation built into grant conditions
  - Both institutional and community-level applicants
```

### ELDP (Endangered Languages Documentation Programme)

Now subsumed into the Endangered Languages Archive (ELAR) at SOAS, London. ELDP funded fieldwork specifically; ELAR stores and provides access to the results.

### AILLA (Archive of the Indigenous Languages of Latin America)

```
AILLA — UNIVERSITY OF TEXAS AT AUSTIN
=======================================

Founded: 2000
Focus: Indigenous languages of Latin America and Mexico
Technology: custom web interface; OLAC-compliant metadata
Access: Tiered -- some materials open, some restricted
       (community-controlled access levels)
Content: 50+ languages, 20,000+ media files

Community control feature:
  Depositing communities can set access restrictions
  Some materials viewable only by community members
  Community can update access permissions over time
  (Repatriation without losing archival backup)
```

### PARADISEC (Pacific and Regional Archive for Digital Sources in Endangered Cultures)

```
PARADISEC
==========

Home: Australian universities consortium
Focus: Pacific, Southeast Asian, Australian Aboriginal materials
Scale: 40 TB of content, 14,000+ items, 1,300+ languages
Technology: open source repository; OAIPMH harvesting
Access: tiered, community-negotiated
Notable: first archive to work systematically with
         Australian Aboriginal communities on digital repatriation

URL: catalog.paradisec.org.au
```

### SayMore (Field Recording Software)

SayMore is fieldwork software, not an archive — it helps linguists organize recordings in the field before deposit:

```
SAYMORE
========

Developer: SIL International
Platform: Windows (open source)
Function: organize recordings during fieldwork
          automated transcription assistance (limited)
          metadata entry workflow
          preparation for archive deposit
Output: package suitable for ELAR/AILLA deposit
Workflow:
  1. Record (external recorder, import to SayMore)
  2. Add speaker metadata
  3. Add session metadata
  4. Create annotations (ELAN format) within SayMore
  5. Export package -> deposit in archive
```

### ELAN (Linguistic Annotation Software)

```
ELAN
=====

Developer: Max Planck Institute for Psycholinguistics
Function: time-aligned transcription and annotation
          multiple annotation tiers per recording
          e.g.: Tier 1: transcription in source language
                Tier 2: morpheme segmentation
                Tier 3: glosses
                Tier 4: free translation
                Tier 5: notes
Export: ELAN XML, EAF format, also FLEx, Toolbox
Standard: most major archives require ELAN format
```

---

## Endangered Languages: Scale of the Problem

```
LANGUAGE ENDANGERMENT SCALE
=============================

Total languages in world: ~7,000 (Ethnologue 2024)
  (Some estimates as low as 6,500 or as high as 7,400
   depending on dialect/language boundary criteria)

Languages at risk:
  Critically endangered: ~800 (< 100 speakers)
  Severely endangered: ~1,500 (100-999 speakers)
  Definitely endangered: ~1,000 (small intergenerational gap)

Languages with > 1 million speakers: ~300 (~4% of languages)
  but those 300 languages are spoken by ~94% of world population

Rate of loss:
  Estimate: ~90% of languages will be gone or moribund by 2100
  Hale et al. (1992): "When a language dies,
  we lose a cultural complexity equivalent to burning down the Louvre"

What is lost with each language:
  - Unique vocabulary encoding distinctions other languages miss
  - Cultural practices encoded in lexical and grammatical structure
  - Oral literature that cannot be fully translated
  - Ecological knowledge (species names, traditional land use)
  - Grammatical structures expanding our understanding of
    what human language can do
```

---

## Language Revitalization: Documentation is Not Enough

```
DOCUMENTATION vs. REVITALIZATION
==================================

DOCUMENTATION:
  Produces: recordings, transcriptions, grammars, dictionaries
  Timeline: can be done by outside researchers in 3-10 years
  Outcome: archive of materials ABOUT the language
  Who benefits: future researchers, partially the community
  Analogy: photographing a burning building

REVITALIZATION:
  Produces: new speakers with native or near-native competence
  Timeline: one generation minimum (20-30 years)
  Outcome: living speaking community
  Who benefits: the community itself
  Requires: political will, resources, community commitment
  Analogy: rebuilding the building

The gap:
  Archives full of beautifully documented dead languages
  Documentation done by linguists, not community-controlled
  Community could not use the materials to revitalize
  because materials were in formats inaccessible to
  non-specialists (IPA transcription, linguistic glosses)

Second gap:
  Language without community: even with materials,
  if the community has no economic/social motivation to use
  the language in daily life, revitalization fails
  Welsh succeeded: government support + identity politics
  Maori succeeded: Kohanga Reo (language nest) immersion schools
                   + government recognition
  Many others: materials exist; speakers still declining
```

---

## Endangered Languages Project

A Google-supported aggregation project (endangeredlanguages.com):

```
ENDANGERED LANGUAGES PROJECT
==============================

Launched: 2012 (Google + First Peoples' Cultural Council)
Now: run by partnership of organizations
Function: aggregate links to documentation resources
          crowd-sourced reports on language status
          not itself an archive -- a directory

Value:
  Single entry point to find resources for a language
  Community members can contribute content directly
  Maps showing geographic distribution of endangered languages

Limitation:
  Quality varies enormously across entries
  Not a substitute for systematic documentation
  Some entries are outdated (language may have recovered
  or declined further since entry was created)
```

---

## Digital Repatriation: Ethics

```
REPATRIATION ETHICS
====================

PROBLEM:
  Colonial-era collection:
    Materials collected without community consent
    Held in Western archives without community access
    Communities cannot access their own heritage materials
    Materials may include restricted/sacred content
    now visible to the general public

REPATRIATION SPECTRUM:
  Physical repatriation: transfer of original materials
    (rare with digital; possible with original recordings)
  Digital repatriation: provide digital copies to community
    (standard practice in modern archives)
  Community control: community sets access conditions
    (emerging standard -- AILLA/PARADISEC model)
  Co-curation: community and archive jointly manage
    (aspirational; requires resources on both sides)

PRACTICAL REPATRIATION CHALLENGES:
  - Community may lack infrastructure to store/access
  - Researcher's institutional agreement may limit sharing
  - Copyright may be held by original collector or institution
  - What "the community" is may be contested
  - Restricted sacred material: who in the community has authority?

DECOLONIZATION FRAMEWORK:
  Kim TallBear, Shawn Wilson, Linda Tuhiwai Smith:
  Research methodology should be accountable to Indigenous communities
  Documentation should serve the community, not just the archive
  Community determines appropriate use of their materials
  This changes the role of the outside researcher fundamentally
```

---

## Decision Cheat Sheet

| Need | Tool / Resource |
|------|----------------|
| Archive audio/video from field | AILLA (Latin America), PARADISEC (Pacific), ELAR (worldwide) |
| Organize field recordings | SayMore (Windows), ELAN for annotation |
| Find metadata standard | OLAC (language-focused), Dublin Core extended |
| Find endangered language resources | Endangered Languages Project (endangeredlanguages.com) |
| Audio quality minimum | WAVE 24-bit/96kHz; never MP3 for archival |
| Community consent framework | AILLA model: tiered access with community control |
| Revitalization (not documentation) | Welsh/Maori models: immersion schools + official status |

---

## Common Confusion Points

**Documentation does not revitalize languages.** An archive of a language is not a speaking community. Documentation is necessary but far from sufficient for revitalization. Language communities have been told "we've documented your language" as a substitute for support of revitalization — this is politically convenient for funders and does not serve communities.

**MP3 is not acceptable for archival purposes.** Lossy compression permanently discards audio data. This is especially critical for tonal languages where frequency distinctions carry meaning. Record to WAVE; compress only for distribution copies.

**Digital archives are not permanent without active management.** Storage media degrade; formats become unreadable; institutions close. The 3-2-1 rule and format migration plans are not optional — they are the difference between preservation and deferred loss.

**Community consent for digital archives is not a legal formality.** It determines what future researchers can access, protects communities from misuse of sacred material, and determines whether the community can actually benefit from the archive. Consent frameworks designed for Western research do not transfer to Indigenous community contexts.

**The Endangered Languages Project is a directory, not an archive.** It links to materials; it doesn't hold them. For research purposes, go directly to AILLA, PARADISEC, ELAR, or ELAR's predecessor DOBES materials.
