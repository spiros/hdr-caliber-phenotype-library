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

This phenotype includes prescriptions of opioid agonist therapy (OAT), indicated by 'Prodcode' under the heading 'Type', and codes indicating a history of illicit opioid use, indicated by 'Medcode' under the heading 'Type'.

#### PRODCODES

In the UK, treatment for opioid dependence involves the prescription of methadone or buprenorphine. However, these medications are also licensed for other indications including pain and palliative cough. We therefore developed a method to identify medications that are specific to OAT (see publication for more detail).

#### MEDCODES

We used keywords to search CPRD dictionaries to find Read and SNOMED codes that may inidicate a history of illicit opioid use (methadone; buprenorphine; abus*; addict; dependen*; drug user; heroin; inject; misus*; opiate; opioid; overdose). Where codes were likely to indicate illicit opioid use, but did not specifically mention opioids, we classified them as ‘probable’. For example, codes indicating injection of illicit drugs were classified as ‘probable’ because an estimated 94% of people who inject drugs in the UK use heroin. Some clinical codes described prescriptions, tests or adverse reactions relating to methadone and buprenorphine. We excluded these where the indication was unclear.

### Publications

Lewer D, Padmanathan P, Qummer ul Arfeen M et al. Healthcare use by people who use illicit opioids (HUPIO): development of a cohort based on electronic primary care records in England [version 1; peer review: awaiting peer review]. Wellcome Open Res 2020, 5:282. <a href="https://doi.org/10.12688/wellcomeopenres.16431.1">10.12688/wellcomeopenres.16431.1</a>
