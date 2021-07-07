---
layout: phenotype
title: COVID-19
phenotype_id: Q9nBeqkXWqwqtNpcq3XFKd
name: COVID-19
type: Disease or Syndrome
group: Respiratory
data_sources:
    - 
validation: aetiology, prognosis
codelists:
    - susheel_covid_Q9nBeqkXWqwqtNpcq3XFKd_ICD10.csv
    - susheel_covid_Q9nBeqkXWqwqtNpcq3XFKd_SNOMEDCT.csv
clinical_terminologies: 
    - ICD10
    - SNOMED CT
sex: 
    - Female
    - Male
author: Susheel Varma
status: DRAFT
date: 2021-02-07
modified_date: 2021-02-07
version: Revision 1
---

### Primary Care

{% include csv.html csvdata=site.data.codelists.susheel_covid_Q9nBeqkXWqwqtNpcq3XFKd_ICD10 %}

### Secondary Care

{% include csv.html csvdata=site.data.codelists.susheel_covid_Q9nBeqkXWqwqtNpcq3XFKd_SNOMEDCT %}