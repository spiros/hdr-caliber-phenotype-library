---
layout: phenotype
title: Heart failure
name: Heart failure
phenotype_id: eJywGK6XvyoSe4SBhSexb3 
type: Disease or Syndrome
group: Cardiovascular
data_sources: 
    - Kings College Hospital NHS Foundation Trust
clinical_terminologies: 
    - SNOMED-CT
validation: 
    - expert-review
codelists: 
    - carr_heartfailure_eJywGK6XvyoSe4SBhSexb3_SNOMEDCT.csv
valid_event_data_range: 01/03/2020-05/04/2020
sex: 
    - Female
    - Male
author: 
    - Carr E
    - Bendayan R
    - Bean D
    - OGallagher K
    - Pickles A
    - Stahl D
    - Zakeri R
    - Searle T
    - Shek A
    - Kraljevic Z
    - Teo J
    - Shah A
    - Dobson R
publications: 
    - "Carr E, Bendayan R, Bean D, OGallagher K, Pickles A, Stahl D, Zakeri R, Searle T, Shek A, Kraljevic Z, Teo J, Shah A, Dobson R. (2020) Supplementing the National Early Warning Score (NEWS2) for anticipating early deterioration among patients with COVID-19 infection. https://www.medrxiv.org/content/10.1101/2020.04.24.20078006v2 DOI: 10.1101/2020.04.24.20078006"
status: FINAL
date: 2020-05-03
date: 2020-05-03
version: 1
---

### Secondary care

The data (demographics, emergency department letters, discharge summaries, clinical notes,
lab results, vital signs) were retrieved and analyzed in near real-time from the structured and
unstructured components of the electronic health record (EHR) using a variety of natural
language processing (NLP) informatics tools belonging to the CogStack ecosystem, namely
MedCAT and MedCATTrainer. The CogStack NLP pipeline captures negation, synonyms,
and acronyms for medical SNOMED-CT concepts as well as surrounding linguistic context using
deep learning and long short-term memory networks. MedCAT produces unsupervised
annotations for all SNOMED-CT concepts under parent terms Clinical Finding, Disorder,
Organism, and Event with disambiguation, pre-trained on MIMIC-III. The annotated
SNOMED-CT terms are summarised below

{% include csv.html csvdata=site.data.codelists.carr_heartfailure_eJywGK6XvyoSe4SBhSexb3_SNOMEDCT %}


### Publications

Carr E, Bendayan R, Bean D, OGallagher K, Pickles A, Stahl D, Zakeri R, Searle T, Shek A, Kraljevic Z, Teo J, Shah A, Dobson R. (2020) Supplementing the National Early Warning Score (NEWS2) for anticipating early deterioration among patients with COVID-19 infection. medRxiv DOI: <a href="https://www.medrxiv.org/content/10.1101/2020.04.24.20078006v2">10.1101/2020.04.24.20078006</a>
