---
layout: phenotype
title: Bronchiestasis
name: Bronchiestasis
phenotype_id: ZckoXfUWNXn8Jn7fdLQuxj 
type: Disease or Syndrome
group: Respiratory
data_sources: 
    - Clinical Practice Research Datalink GOLD
    - Clinical Practice Research Datalink Aurum
    - Hospital Episode Statistics APC for CPRD GOLD
    - Hospital Episode Statistics APC for CPRD Aurum
    - Death Registration data for CPRD GOLD
    - Death Registration data for CPRD Aurum
    - UK Biobank
clinical_terminologies: 
    - Read Version 2
    - SNOMED-CT
    - ICD-10
    - ICD-11
validation: 
codelists:
    - axson_bronchiestasis_ZckoXfUWNXn8Jn7fdLQuxj_ICD10.csv
    - axson_bronchiestasis_ZckoXfUWNXn8Jn7fdLQuxj_ICD11.csv
    - axson_bronchiestasis_ZckoXfUWNXn8Jn7fdLQuxj_SNOMEDCT.csv
    - axson_bronchiestasis_ZckoXfUWNXn8Jn7fdLQuxj_UKBIOBANK.csv
valid_event_data_range: 01/01/2001 - 31/12/2019
sex: 
    - Female
    - Male
author: 
    - Eleanor L Axson
    - Jennifer K Quint
publications: 
status: BETA
date: 2019-06-20
modified_date: 2019-06-20
version: 1
---

### Primary care 
{% include csv.html csvdata=site.data.codelists.axson_bronchiestasis_ZckoXfUWNXn8Jn7fdLQuxj_SNOMEDCT %}

### Secondary care 
#### Diagnoses 
{% include csv.html csvdata=site.data.codelists.axson_bronchiestasis_ZckoXfUWNXn8Jn7fdLQuxj_ICD10 %}

{% include csv.html csvdata=site.data.codelists.axson_bronchiestasis_ZckoXfUWNXn8Jn7fdLQuxj_ICD11 %}

### UK Biobank

{% include csv.html csvdata=site.data.codelists.axson_bronchiestasis_ZckoXfUWNXn8Jn7fdLQuxj_UKBIOBANK %}

### Mortality

{% include csv.html csvdata=site.data.codelists.axson_bronchiestasis_ZckoXfUWNXn8Jn7fdLQuxj_ICD10 %}
