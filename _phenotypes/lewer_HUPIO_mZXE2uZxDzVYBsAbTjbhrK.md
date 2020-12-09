---
layout: phenotype
title: Illicit opioid use
name: Illicit opioid use
phenotype_id: mZXE2uZxDzVYBsAbTjbhrK
type: Lifestyle Risk Factor
group: Lifestyle Risk Factor
data_sources: 
    - Clinical Practice Research Datalink GOLD
    - Clinical Practice Research Datalink AURUM
clinical_terminologies: 
    - SNOMED-CT
    - Read Version 2
    - CPRD product code
validation: 
    - expert-review
codelists:
    - lewer_HUPIO_mZXE2uZxDzVYBsAbTjbhrK_SNOMEDCT.csv
valid_event_data_range: 01/03/2020-05/04/2020
sex: 
    - Female
    - Male
author: 
    - Lewer D
    - Padmanathan P
    - Arfeen A
    - Denaxas S
    - Forbes H
    - Gonzalez-Izquierdo A
    - Hickman M
publications: 
    - "Lewer D, Padmanathan P, Qummer ul Arfeen M et al. Healthcare use by people who use illicit opioids (HUPIO): development of a cohort based on electronic primary care records in England [version 1; peer review: awaiting peer review]. Wellcome Open Res 2020, 5:282. DOI: 10.12688/wellcomeopenres.16431.1"
status: FINAL
date: 2020-12-08
date: 2020-12-08
version: 1
---

### Primary care

{% include csv.html csvdata=site.data.codelists.lewer_HUPIO_mZXE2uZxDzVYBsAbTjbhrK_SNOMEDCT %}

### Implementation

We selected patients by identifying product codes indicating a prescription of OAT and clinical codes indicating a history of illicit opioid use, such as ‘heroin dependence’ (see extended data for a full code list23). We prioritised specificity over sensitivity, aiming to use codes that are only applied to the target population.

We used keywords to search CPRD dictionaries to find Read and SNOMED clinical codes that may illicit opioid use (methadone; buprenorphine; abus*; addict;  ependen*; drug user; heroin; inject; misus*; opiate; opioid; overdose). Our search identified 1,098 Read codes and 1,800 SNOMED codes. Two authors (DL and PP)
screened the codes for relevance, with conflicts resolved through discussion.

Where codes were likely to indicate illicit opioid use, but did not specifically mention opioids, we classified them as ‘probable’. Some clinical codes described prescriptions, tests or adverse reactions relating to methadone and buprenorphine. 

### Publications

Lewer D, Padmanathan P, Qummer ul Arfeen M et al. Healthcare use by people who use illicit opioids (HUPIO): development of a cohort based on electronic primary care records in England [version 1; peer review: awaiting peer review]. Wellcome Open Res 2020, 5:282. <a href="https://doi.org/10.12688/wellcomeopenres.16431.1">10.12688/wellcomeopenres.16431.1</a>
