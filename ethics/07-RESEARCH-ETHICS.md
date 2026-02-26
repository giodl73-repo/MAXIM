# Research Ethics: Nuremberg, Helsinki, and IRBs

## The Big Picture

```
+-----------------------------------------------------------------------+
|                    RESEARCH ETHICS FRAMEWORK                           |
+-----------------------------------------------------------------------+
|                                                                       |
|  RESEARCH ETHICS: Constraints on the use of human subjects in        |
|  scientific research. Born out of catastrophic historical failures.  |
|                                                                       |
|  HISTORICAL TIMELINE:                                                 |
|  Nazi experiments (1939-1945)                                        |
|       ↓                                                               |
|  Nuremberg Code (1947): 10 basic principles                          |
|       ↓                                                               |
|  Tuskegee Syphilis Study (1932-1972) revealed                        |
|       ↓                                                               |
|  National Research Act (1974)                                        |
|       ↓                                                               |
|  Belmont Report (1979): 3 principles + applications                  |
|       ↓                                                               |
|  45 CFR 46 (Common Rule, 1991; revised 2018)                        |
|       ↓                                                               |
|  Modern IRB system                                                    |
|                                                                       |
|  SCOPE: Medical research, social/behavioral research, computing      |
|  research (data, algorithms, systems using human data).              |
+-----------------------------------------------------------------------+
```

---

## Historical Atrocities: Nazi Medical Experiments

```
NAZI MEDICAL EXPERIMENTS (1939-1945)
======================================

SCALE AND NATURE:
  Conducted primarily at concentration camps (Dachau, Auschwitz, Ravensbrück).
  Subjects: prisoners, Jews, Roma, POWs -- involuntary in all cases.
  Extreme coercion: subjects had no ability to refuse.
  Many experiments designed to cause death.

TYPES OF EXPERIMENTS:
  +-----------------------------+--------------------------------------+
  | Hypothermia (Dachau)        | Subjects submerged in ice water.     |
  |                             | Medical data on survival/rewarming.  |
  |                             | Ostensibly for Luftwaffe pilots.     |
  +-----------------------------+--------------------------------------+
  | High-altitude (Dachau)      | Low-pressure chamber, asphyxiation.  |
  |                             | For Luftwaffe pilots.                |
  +-----------------------------+--------------------------------------+
  | Malaria (Dachau)            | Deliberately infected; tested drugs. |
  +-----------------------------+--------------------------------------+
  | Sulfanilamide (Ravensbrück) | Simulated battlefield wounds;        |
  |                             | infected with gangrene; tested drugs.|
  +-----------------------------+--------------------------------------+
  | Bone/muscle transplants     | Removed bones, muscles, nerves from  |
  | (Ravensbrück)               | subjects; often fatal.               |
  +-----------------------------+--------------------------------------+
  | Sterilization               | Irradiation, castration, chemical.  |
  | (multiple camps)            | Scale up for mass sterilization.    |
  +-----------------------------+--------------------------------------+
  | Mengele's twin studies      | Experiments on twins; often killed  |
  | (Auschwitz)                 | to enable comparative autopsy.      |
  +-----------------------------+--------------------------------------+

  Estimated 15,000-20,000+ subjects. Most died or were left permanently injured.

DOCTORS' TRIAL (Nuremberg, 1946-1947):
  23 German physicians and administrators tried for war crimes.
  16 convicted. 7 executed.
  Verdict created the foundation for the Nuremberg Code.

THE LEGITIMACY QUESTION:
  Were the data scientifically valid?
  Debate: some immunologists argued the hypothermia data had value.
  Consensus position (U.S. government, scientific community):
  Data from unethical experiments should not be used.
  Reasons:
  1. Using data rewards and legitimizes the methods.
  2. The data quality is suspect: subjects were tortured, not tested.
     Motivations of researchers were not scientific accuracy.
  3. The data could be replicated by ethical means.
```

---

## Nuremberg Code (1947)

```
NUREMBERG CODE (1947)
======================

Written in response to the Doctors' Trial verdicts.
The foundational statement of human subjects research ethics.

TEN PRINCIPLES:

1. VOLUNTARY CONSENT is absolutely essential.
   The person must have:
   - Legal capacity to consent.
   - Ability to exercise free choice.
   - Sufficient understanding to make an enlightened decision.
   This means: no coercion, no fraud, no duress.

2. Experiment must be for the good of society, with results
   obtainable by no other means.

3. Based on prior animal experimentation and knowledge of the problem.

4. All unnecessary physical and mental suffering must be avoided.

5. No experiment should be conducted if there is a priori reason to
   believe it will cause death or disabling injury.
   Exception: experiments in which the experimental physicians also
   serve as subjects.

6. Risk must not exceed the humanitarian importance of the problem.

7. Proper preparations and facilities to protect subjects from
   even remote possibilities of harm.

8. Only scientifically qualified persons should conduct the experiments.

9. Subject must be free to leave the experiment at any time.

10. Investigator must be prepared to terminate the experiment at any time
    if harm appears probable.

INFLUENCE AND LIMITS:
  The Nuremberg Code was the first international standard.
  BUT: had limited practical effect for decades.
  Most researchers viewed Nazi experiments as unique evil, not a general
  template. "It can't happen here" reasoning.
  Proof that this reasoning was wrong: Tuskegee.

  Also: Nuremberg Code focuses on individual consent.
  Does not address: institutional review, equity in subject selection,
  benefits to subjects, post-trial care.
```

---

## Tuskegee Syphilis Study

```
TUSKEGEE SYPHILIS STUDY (1932-1972)
======================================

SETUP:
  U.S. Public Health Service study.
  399 Black men with latent syphilis; 201 controls.
  Macon County, Alabama.
  Purpose: observe natural progression of untreated syphilis in Black men.
  (USPHS had a pre-existing (false) hypothesis that syphilis progressed
  differently in Black men than white men.)

ENROLLMENT:
  Men were told they were being treated for "bad blood."
  This was deceptive -- "bad blood" was a local colloquial term for
  various illnesses, not specifically syphilis.
  They received free meals, transportation, burial insurance.
  They were NOT told they had syphilis.

PENICILLIN (1947):
  Penicillin became the standard treatment for syphilis.
  The USPHS continued the study WITHOUT treating subjects.
  Active measures to prevent subjects from receiving treatment:
  - USPHS had subjects excluded from WWII draft boards' syphilis treatment.
  - Letter sent to local doctors asking them NOT to treat study subjects.

  This is the central ethical violation: withholding KNOWN effective treatment
  from people who could have been cured, without their knowledge or consent,
  for 25 years after penicillin was available.

REVELATION AND AFTERMATH:
  Peter Buxtun, USPHS venereal disease investigator, raised concerns in 1966.
  USPHS review panel (1969) voted to continue the study.
  Buxtun went to the press. Washington Star, AP (1972).
  Study ended in 1972.

  At that point:
  - 28 of original subjects had died of syphilis.
  - 100 had died of related complications.
  - 40 wives had been infected.
  - 19 children had been born with congenital syphilis.

LEGAL AFTERMATH:
  Class action lawsuit settled for $10 million (1974).
  Lifetime medical benefits for surviving participants and families.
  Presidential apology: Bill Clinton, 1997.
  Last known survivor died 2004.

LEGACY:
  Tuskegee created profound and persistent mistrust of medical
  and public health institutions among Black Americans.
  Documented effect on clinical trial participation rates.
  Documented effect on COVID-19 vaccine hesitancy in 2020-2021.
  The trust damage from research ethics violations persists for generations.

ADDITIONAL U.S. VIOLATIONS:
  Guatemala syphilis study (1946-1948):
  USPHS intentionally infected Guatemalan prisoners, soldiers, mental patients
  with syphilis and gonorrhea.
  Conducted by the same researcher as Tuskegee (John Cutler).
  Revealed in 2010. Obama administration issued formal apology.

  Willowbrook State School (1956-1970):
  Children with intellectual disabilities deliberately infected with hepatitis
  to study the disease progression and experimental vaccines.
  Rationalized: children were likely to contract hepatitis anyway in the
  institution's conditions.
```

---

## Declaration of Helsinki

```
DECLARATION OF HELSINKI (1964, revised 10 times)
==================================================

World Medical Association declaration.
Medical profession's own standards for human subjects research.
Most recent revision: 2013.

KEY ADVANCES OVER NUREMBERG CODE:
  1. THERAPEUTIC vs. NON-THERAPEUTIC RESEARCH:
     Nuremberg Code didn't distinguish.
     Helsinki: different standards for therapeutic (patient-subjects)
     vs. non-therapeutic (healthy volunteers) research.

  2. VULNERABLE POPULATIONS:
     Special protections for those who cannot consent for themselves:
     children, cognitively impaired, prisoners, pregnant women.
     Proxy consent + ongoing assent.

  3. RESEARCH PROTOCOL REVIEW:
     Independent ethics committee review BEFORE research begins.
     This is the precursor to the modern IRB.

  4. PLACEBO CONTROLS:
     Helsinki (2000 revision): placebo controls only when no proven
     intervention exists.
     Controversy: when prior standard treatment exists, placebo
     is unethical because it withholds known effective treatment.
     U.S. FDA disagreed: retained broader use of placebo controls.
     This tension continues in drug approval regulation.

  5. POST-TRIAL OBLIGATIONS:
     Subjects should have access to beneficial treatments found in trials.
     Study sponsor obligations after trial ends.

  6. REGISTRATION AND PUBLICATION:
     Clinical trials must be registered before recruitment begins.
     Negative results must be published or made available.
     (Publication bias problem: only positive results published,
     giving inflated view of treatment efficacy.)

LIMITS:
  Declaration of Helsinki is not legally binding.
  It is a professional standard that regulators (FDA, NIH) have incorporated.
  Different national implementations.
```

---

## Belmont Report and the Common Rule

```
BELMONT REPORT (1979)
======================

National Commission for Protection of Human Subjects of Biomedical
and Behavioral Research. Mandated by National Research Act (1974),
passed in direct response to Tuskegee revelation.

THREE PRINCIPLES:

1. RESPECT FOR PERSONS:
   Individuals should be treated as autonomous agents.
   Individuals with diminished autonomy are entitled to protection.

   APPLICATION:
   - Informed consent.
   - Voluntary participation.
   - Comprehension (not just disclosure -- actual understanding).

2. BENEFICENCE:
   Two rules:
   (a) Do not harm.
   (b) Maximize possible benefits and minimize possible harms.

   APPLICATION:
   - Assessment of risks and benefits.
   - Benefits to subjects and to knowledge.
   - Medical vs. research activities (must distinguish).

3. JUSTICE:
   Fair distribution of research burdens and benefits.
   Who bears the risks? Who benefits?

   APPLICATION:
   - Fair subject selection.
   - NOT: select vulnerable populations for research because they're
     convenient (institutionalized, poor) while benefits go to the wealthy.
   - Historical injustice: most research benefits went to white,
     affluent populations while burdens fell on marginalized groups.
   - Modern equity agenda: include women, minorities in clinical trials.
     (Pre-1990s: women often excluded -- left major knowledge gaps.)

BELMONT vs. BEAUCHAMP-CHILDRESS:
  Both use autonomy, beneficence, justice.
  Belmont: research-specific, 3 principles.
  B-C: medical practice, 4 principles (adds non-maleficence).
  Belmont was the foundation; B-C extended to medical practice.

THE COMMON RULE (45 CFR 46, 1991; revised 2018):
  Federal regulation implementing Belmont principles.
  Applies to: federally funded human subjects research.
  Core requirements:
  1. IRB review and approval.
  2. Informed consent.
  3. Additional protections for vulnerable populations (subparts B, C, D).

  2018 REVISION (IMPORTANT CHANGES):
  - Broad consent for biospecimen/data research.
  - New exemption categories for low-risk research.
  - Single IRB mandate for multi-site studies.
  - Requirements for posting consent forms.
```

---

## Institutional Review Boards

```
INSTITUTIONAL REVIEW BOARDS (IRBs)
=====================================

STRUCTURE:
  Every U.S. institution receiving federal research funding
  must have an IRB (or rely on an external IRB).

  Minimum composition (45 CFR 46.107):
  - At least 5 members.
  - Not all from same profession.
  - At least one scientist.
  - At least one non-scientist.
  - At least one community member (not affiliated with institution).
  - Members with expertise relevant to research being reviewed.

REVIEW LEVELS:
  +------------------+------------------------------------------------+
  | EXEMPT           | Low risk; limited categories.                  |
  |                  | Survey research, observations, existing data.  |
  |                  | IRB determines exemption (not researcher).     |
  +------------------+------------------------------------------------+
  | EXPEDITED        | Minimal risk research.                         |
  |                  | 18 categories (45 CFR 46.110).                |
  |                  | Reviewed by IRB chair or designee.            |
  |                  | No full board meeting required.               |
  +------------------+------------------------------------------------+
  | FULL BOARD       | Greater than minimal risk.                     |
  |                  | Vulnerable populations.                        |
  |                  | Clinical trials.                               |
  |                  | Full committee review at convened meeting.    |
  +------------------+------------------------------------------------+

WHAT IRBs EVALUATE:
  1. RISKS to subjects: physical, psychological, social, economic, legal.
  2. BENEFITS to subjects and to knowledge.
  3. RISK/BENEFIT RATIO: favorable?
  4. SUBJECT SELECTION: equitable? Appropriate inclusion/exclusion criteria?
  5. INFORMED CONSENT: adequate? Comprehensible? Voluntarily given?
  6. MONITORING: data safety monitoring boards for clinical trials.
  7. PRIVACY AND CONFIDENTIALITY: data protection.

ONGOING OVERSIGHT:
  Continuing review (annual for most studies).
  Adverse event reporting: unanticipated problems must be reported.
  Protocol amendments must be reviewed.

LIMITATIONS AND CRITICISMS:
  1. IRBs are inconsistent: same protocol reviewed differently at
     different institutions.
  2. Bureaucratic burden: small-risk research undergoes full review.
     Chilling effect on social science research.
  3. Local bias: IRB members at an institution may be captured
     by institutional interests (reputation, funding).
  4. Limited expertise for novel research types (AI, genetics).
  5. Consent is fetishized: focus on consent form compliance rather
     than actual comprehension or genuine voluntariness.
  6. Post-consent: little ongoing protection once consent is obtained.
```

---

## Research Ethics in Computing

```
RESEARCH ETHICS IN COMPUTING
==============================

HISTORY:
  Early computing research: largely exempt from human subjects oversight.
  IRB oversight: designed for medical/social science research.
  Data-driven computing research: new ethical landscape.

FACEBOOK EMOTIONAL CONTAGION STUDY (2014):
  Facebook manipulated news feeds of ~700,000 users.
  Showed users more positive or more negative emotional content.
  Measured effect on users' own post positivity/negativity.
  Published in PNAS without individual informed consent.

  ETHICAL ISSUES:
  - Participants had no idea they were in an experiment.
  - Emotional manipulation without consent.
  - Cornell IRB: study was not federally funded, so not subject to
    Common Rule. IRB reviewed after the fact; said study was "not human
    subjects research" because data was collected by Facebook.
  - This interpretation was widely criticized as evasion.

  AFTERMATH:
  - ACM, USENIX issued ethics guidelines.
  - Growing recognition that internet research requires ethical frameworks.
  - 2018 Common Rule revision: broad consent for re-use of data.

OKCupid STUDY (2016):
  Researchers published private OKCupid user data (scraped) including
  usernames, sexual orientation, drug use.
  Defense: data was "public."
  Problem: "public" in context of a dating site ≠ consent to research
  publication linking profiles to sexual preferences.
  Contextual integrity (Nissenbaum): information flows are appropriate
  when they match the context in which the information was shared.

CAMBRIDGE ANALYTICA / FACEBOOK (2018):
  Survey app collected data on ~270,000 Facebook users who consented.
  Also collected data on their ~87 million Facebook friends who did NOT consent.
  Data used for political targeting.
  Not a research study, but illustrates the research ethics problems
  of data re-use and secondary subjects.

IRB APPLICABILITY TO COMPUTING RESEARCH:
  When does computing research require IRB review?

  REQUIRES IRB: Research that:
  - Involves interacting with human subjects.
  - Analyzes identifiable private information about individuals.
  - Experiments that could harm participants.

  TYPICALLY EXEMPT OR NOT APPLICABLE:
  - Analyzing purely public data (no identifiable individuals).
  - Building systems without involving human subjects.
  - Theoretical/algorithmic research.

  GRAY AREA:
  - Web scraping of "public" social media data.
  - A/B testing on live platforms.
  - Machine learning on sensitive datasets.
  - Research using datasets originally collected for other purposes.

EMERGING AREAS:
  AI SYSTEM EVALUATION ON HUMAN SUBJECTS:
  Testing AI systems' effects on users raises human subjects issues.
  Red-teaming, usability studies: IRB review may be required.

  SENSITIVE ATTRIBUTE PREDICTION:
  ML models predicting race, sexual orientation, political views.
  Research ethics question: should researchers build tools with
  this capability even for academic understanding?

  DATA JUSTICE:
  Communities that generate data (health records of marginalized communities)
  often don't benefit from research on that data.
  CARE Principles (indigenous data governance):
  Collective benefit, Authority to control, Responsibility, Ethics.
  Emerging framework for equitable data research.
```

---

## Research Integrity

```
RESEARCH INTEGRITY
===================

FABRICATION, FALSIFICATION, PLAGIARISM (FFP):
  These are the three categories of research misconduct.

  FABRICATION: making up data or results.
  FALSIFICATION: manipulating data, images, protocols to misrepresent results.
  PLAGIARISM: using another's ideas/words without attribution.

  Distinguished from: honest error and legitimate scientific disagreement.

HIGH-PROFILE CASES:

  HWANG WOO-SUK (2004-2005):
  South Korean stem cell researcher.
  Claimed to have created first human embryonic stem cell lines by cloning.
  Science cover stories, global acclaim.
  2005: investigation revealed the data was fabricated.
  Retraction of landmark papers.
  Criminal conviction in South Korea.
  Illustrates: individual misconduct + institutional failure (reviewers,
  co-authors, institutional oversight all failed).

  ANDREW WAKEFIELD (1998):
  Lancet paper claiming link between MMR vaccine and autism.
  Used by anti-vaccine movement for decades.
  2010: retraction after investigation revealed:
  - Undisclosed financial conflicts of interest (paid by lawyers suing vaccine makers).
  - Patient data manipulated.
  - Ethics violations in data collection.
  Wakefield lost his medical license.
  Damage: measles outbreaks due to vaccination decline persist today.

  DIEDERIK STAPEL (2011):
  Dutch social psychologist.
  Fabricated data in at least 55 publications over years.
  Collected data himself (unusual); no co-authors checked the raw data.
  Complete fabrication: invented datasets.

PUBLICATION BIAS AND P-HACKING:
  Journals publish positive results more than negative results.
  Effect: inflated view of treatment effects in published literature.
  Researchers are incentivized to find positive results.

  P-HACKING (HARKing = Hypothesizing After Results are Known):
  Researcher collects data; no significant effect.
  Tries multiple analyses until p < 0.05 appears.
  Reports as if that analysis was the pre-specified one.
  Not technically fabrication -- but produces false positives.

  OPEN SCIENCE MOVEMENT:
  Pre-registration: register hypothesis and analysis plan BEFORE collecting data.
  ClinicalTrials.gov: required for clinical trials since 2007.
  OSF (Open Science Framework): pre-registration for social/behavioral research.
  Open data: raw data publicly available for replication.
  Registered reports: journal commits to publish before results are known.

REPLICATION CRISIS:
  Open Science Collaboration (2015): attempted to replicate 100
  psychology studies. Only ~39% replicated.
  Cancer Biology Replication Project: ~50% replicated.
  Causes:
  - Small sample sizes → underpowered studies.
  - Publication bias.
  - P-hacking.
  - Inadequate reporting of methods.
  - Fraud (a small component).

  RESPONSE: Power analysis requirements; larger samples; pre-registration;
  registered replication reports; data sharing mandates.
```

---

## Decision Cheat Sheet

| Framework | Origin | Key requirements | Applies to |
|---|---|---|---|
| Nuremberg Code | 1947, Doctors' Trial | Voluntary consent paramount; no prior harm | All human subjects research |
| Declaration of Helsinki | 1964 (WMA) | IRB review; vulnerable populations; placebo limits | Medical research (professional standard) |
| Belmont Report | 1979 (NCPHSBBR) | Respect persons, beneficence, justice | Federally funded human subjects research |
| Common Rule (45 CFR 46) | 1991/2018 | IRB review, informed consent, vulnerable population protections | U.S. federally funded research |
| HIPAA | 1996 | Health data privacy; de-identification standards | Healthcare data |
| GDPR | 2018 | Consent, purpose limitation, data minimization | EU personal data (including research) |

| IRB Review Level | When | Requires |
|---|---|---|
| Exempt | Minimal risk, specific categories | IRB determination (not self-determined) |
| Expedited | Minimal risk, 18 categories | Chair/designee review |
| Full board | Greater than minimal risk | Convened committee |

---

## Common Confusion Points

**"The Nazi experiments were uniquely evil — normal research ethics rules don't apply to us."**
This was exactly the reasoning that allowed Tuskegee to continue for decades after Nuremberg. Researchers believed themselves fundamentally different from the Nazis. The Belmont Report exists precisely because U.S. government researchers, with bureaucratic funding and academic prestige, engaged in systematic deception and harm. The ethical failures were structural (lack of oversight, vulnerable population selection, deceptive recruitment) not unique to exceptional criminals.

**"Tuskegee participants could have left the study at any time."**
Technically, but the coercion was embedded in the design. Subjects were deceived about what they had and what they were receiving. They were actively prevented from receiving treatment elsewhere. The researchers leveraged economic vulnerability (free meals, transportation, burial insurance in an era of severe poverty and racial exclusion from the healthcare system). Voluntariness is formal (no physical restraint) but hollow when deception and structural coercion are in play.

**"IRB approval means the research is ethical."**
IRB approval means the research complied with the regulatory framework as interpreted by one institutional committee. IRBs are inconsistent, can be risk-averse about the wrong things, and can miss novel ethical issues. The Facebook emotional contagion study was technically compliant (not federally funded, data collected by Facebook). It was still widely criticized as ethically deficient. IRB approval is a floor, not a ceiling.

**"Data from the public internet doesn't require ethical review."**
Contextual integrity (Nissenbaum): the ethical assessment depends on whether the information flow matches the norms of the original context. Users who share information on a dating app have not consented to that information being published in research linking them to their sexual preferences, even if the data was technically "public." The OKCupid case and related controversies have pushed the field toward recognizing that "public" does not mean "fair game for any re-use."

**"Pre-registration prevents all false positive findings."**
Pre-registration reduces p-hacking and HARKing by requiring researchers to specify hypotheses and analyses before seeing data. It does not prevent honest error, measurement problems, or deviations from the pre-registered plan that can be justified post-hoc. Pre-registration improves credibility but is not a guarantee of truth. It also does not address publication bias unless paired with registered reports (commitment to publish regardless of results).

**"The replication crisis means psychology (or social science) is junk."**
The replication crisis is a scientific self-correction process, not evidence that the entire field is worthless. It exposed methodological weaknesses (small N, p-hacking, inadequate reporting) that are now being systematically addressed. Many findings do replicate; the failed replications cluster in specific research areas and methodologies. The appropriate response is reform (power analysis, pre-registration, data sharing) not dismissal of entire fields.
