---
layout: phenotype
title: CCU002_01 COVID19 infection
name: CCU002_01 COVID19 infection
phenotype_id: COVID-IMPACT
type: Disease or Syndrome
group: Disease or Syndrome
sources:
    - bhfcvdcoviduk
data_sources:
    - Trusted Research Environments for CVD-COVID-UK / COVID-IMPACT
    - GPES Data for Pandemic Planning and Research (COVID-19)
    - Hospital Episode Statistics Admitted Patient Care
    - Civil Registration - Deaths
    - Covid-19 Second Generation Surveillance System
    - COVID-19 SARI-Watch (formerly CHESS)
    - Secondary Uses Services Payment By Results
clinical_terminologies:
    - SNOMED-CT
    - ICD-10
valid_event_data_range: 23/01/2020 - 31/05/2021
codelists: 
    - covid_impact_ccu01301_01_GP_covid_diagnosis_England_SNOMEDCT.csv
    - covid_impact_ccu01301_02_Covid_admission_England_ICD10.csv
    - covid_impact_ccu01301_03_ECMO_treatment_England_OPCS.csv
    - covid_impact_ccu01301_03_IMV_treatment_England_OPCS.csv
    - covid_impact_ccu01301_03_NIV_treatment_England_OPCS.csv
    - covid_impact_ccu01301_04_Fatal_with_covid_diagnosis_England_ICD10.csv

sex:
    - Female
    - Male
author: 
    - Johan H Thygesen, Christopher Tomlinson, Sam Hollings, Mehrdad Mizani, Alex Handy, Ashley Akbari, Amitava Banerjee, Jennifer Cooper, Alvina Lai, Ken Li, Bilal Mateen, Naveed Sattar, Reecha Sofat, Ana Torralbo, Honghan Wu, Angela Wood, Jonathan A C Sterne, Christina Pagel, William Whiteley, Cathie Sudlow, Harry Hemingway, Spiros Denaxas
publications:
    - "Understanding COVID-19 trajectories from a nationwide linked electronic health record cohort of 56 million people: phenotypes, severity, waves & vaccination."
status: FINAL
date: 2021-11-09
modified_date: 2021-11-09
version: Revision 1

---

### Publication

Understanding COVID-19 trajectories from a nationwide linked electronic health record cohort of 56 million people: phenotypes, severity, waves & vaccination

Johan H Thygesen, Christopher Tomlinson, Sam Hollings, Mehrdad Mizani, Alex Handy, Ashley Akbari, Amitava Banerjee, Jennifer Cooper, Alvina Lai, Ken Li, Bilal Mateen, Naveed Sattar, Reecha Sofat, Ana Torralbo, Honghan Wu, Angela Wood, Jonathan A C Sterne, Christina Pagel, William Whiteley, Cathie Sudlow, Harry Hemingway, Spiros Denaxas

medRxiv 2021.11.08.21265312; doi: https://doi.org/10.1101/2021.11.08.21265312

### Primary care EHR England
{% include csv.html csvdata=site.data.codelists.covid_impact_ccu01301_01_GP_covid_diagnosis_England_SNOMEDCT %}
### Hospitalization EHR England
{% include csv.html csvdata=site.data.codelists.covid_impact_ccu01301_02_Covid_admission_England_ICD10 %}
### Primary care EHR England
{% include csv.html csvdata=site.data.codelists.covid_impact_ccu01301_03_ECMO_treatment_England_OPCS %}
### Primary care EHR England
{% include csv.html csvdata=site.data.codelists.covid_impact_ccu01301_03_IMV_treatment_England_OPCS %}
### Primary care EHR England
{% include csv.html csvdata=site.data.codelists.covid_impact_ccu01301_03_NIV_treatment_England_OPCS %}
### Hospitalization EHR England
{% include csv.html csvdata=site.data.codelists.covid_impact_ccu01301_04_Fatal_with_covid_diagnosis_England_ICD10 %}
