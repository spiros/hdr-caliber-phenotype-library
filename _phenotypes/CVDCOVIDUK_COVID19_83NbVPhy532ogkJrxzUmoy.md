---
layout: phenotype
title: COVID-19 infection
phenotype_id: 83NbVPhy532ogkJrxzUmoy
name: COVID-19 infection
type: Disease or Syndrome                   
group: COVID-19 infection
sources: 
    - bhfcvdcoviduk
data_sources:
    - GPES Data for Pandemic Planning and Research (COVID-19)
    - Hospital Episode Statistics Admitted Patient Care
    - Civil Registration - Deaths
    - Covid-19 Second Generation Surveillance System
clinical_terminologies:
    - SNOMED-CT
    - ICD-10
validation:
codelists: 
    - cvdcoviduk_COVID19_bhfcvdcoviduk_ICD10.csv
    - cvdcoviduk_COVID19_bhfcvdcoviduk_SNOMEDCT.csv
valid_event_data_range: 01/01/2020 - 31/10/2020
sex:
    - Female
    - Male
author: 
    - BHF CVD COVID UK Consortium
publications:
status: FINAL
date: 2020-10-31
modified_date: 2021-01-01
version: Revision 1
---

### Primary Care

{% include csv.html csvdata=site.data.codelists.cvdcoviduk_COVID19_bhfcvdcoviduk_SNOMEDCT %}

### Hospitalizations

{% include csv.html csvdata=site.data.codelists.cvdcoviduk_COVID19_bhfcvdcoviduk_ICD10 %}

### Implementation

We ascertained people with a confirmed or suspected Covid-19 diagnosis as follows: 

1) a positive PCR or antigen test from the Covid-19 laboratory test data, with specimen date on or before 31 October 2020; or 

2) a Covid-19 diagnosis SNOMED-CT concept code appearing in the primary care data, with event date on or before 31 October; or 

3) a diagnosis ICD-10 code appearing in the hospital episodes (main or secondary diagnostic code position in the admitted patient care component of the hospital episode statistics), with admission date on or before 31 October or 

4) death registration with a mention (as underlying on contributing cause) of a diagnosis ICD-10 code , with death registration date on or before 31 October 2020.


