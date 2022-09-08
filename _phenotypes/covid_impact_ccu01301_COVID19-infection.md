---
layout: phenotype
title: CCU013_01 COVID-19 infection
name: CCU013_01 COVID-19 infection
phenotype_id: AxcNj8ncFxkUraPBzcLwnk
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
    - OPCS

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
    - Johan H Thygesen, Christopher Tomlinson, Sam Hollings, Mehrdad Mizani, Alex Handy, Ashley Akbari, Amitava Banerjee, Jennifer Cooper, Alvina Lai, Ken Li, Bilal Mateen, Naveed Sattar, Reecha Sofat, Ana Torralbo, Honghan Wu, Angela Wood, Jonathan A C Sterne, Christina Pagel, William Whiteley, Cathie Sudlow, Harry Hemingway, Spiros Denaxas, on behalf of the Longitudinal Health and Wellbeing COVID-19 National Core Study and the CVD-COVID-UK/COVID-IMPACT Consortium

publications:
    - "COVID-19 trajectories among 57 million adults in England: a cohort study using electronic health records."
status: FINAL
date: 2021-11-09
modified_date: 2022-09-08
version: Revision 2

---

### Phenotypes

#### England hospitalization EHR: COVID-19 diagnosis 
{% include csv.html csvdata=site.data.codelists.covid_impact_ccu01301_01_GP_covid_diagnosis_England_SNOMEDCT %}
#### England hospitalization EHR: COVID-19 hospitalization 
{% include csv.html csvdata=site.data.codelists.covid_impact_ccu01301_02_Covid_admission_England_ICD10 %}
#### England hospitalization EHR: Extracorporeal membrane oxygenation 
{% include csv.html csvdata=site.data.codelists.covid_impact_ccu01301_03_ECMO_treatment_England_OPCS %}
#### England hospitalization EHR: Invasive ventilation 
{% include csv.html csvdata=site.data.codelists.covid_impact_ccu01301_03_IMV_treatment_England_OPCS %}
#### England hospitalization EHR: Continuous positive airway pressure 
{% include csv.html csvdata=site.data.codelists.covid_impact_ccu01301_03_NIV_treatment_England_OPCS %}
#### England hospitalization EHR: COVID-19 death 
{% include csv.html csvdata=site.data.codelists.covid_impact_ccu01301_04_Fatal_with_covid_diagnosis_England_ICD10 %}

### Publication

COVID-19 trajectories among 57 million adults in England: a cohort study using electronic health records

Johan H Thygesen, Christopher Tomlinson, Sam Hollings, Mehrdad Mizani, Alex Handy, Ashley Akbari, Amitava Banerjee, Jennifer Cooper, Alvina Lai, Ken Li, Bilal Mateen, Naveed Sattar, Reecha Sofat, Ana Torralbo, Honghan Wu, Angela Wood, Jonathan A C Sterne, Christina Pagel, William Whiteley, Cathie Sudlow, Harry Hemingway, Spiros Denaxas, on behalf of theLongitudinal Health and Wellbeing COVID-19 National Core Study and the CVD-COVID-UK/COVID-IMPACT Consortium

Lancet Digital Health. 2022;4(7):e542-e557. Published Online June 8, 2022; doi: [https://doi.org/10.1016/S2589-7500(22)00091-7](https://doi.org/10.1016/S2589-7500(22)00091-7)
