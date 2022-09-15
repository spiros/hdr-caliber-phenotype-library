---
layout: phenotype
title: CCU029_01 COVID-19 admission types
name: CCU029_01 COVID-19 admission types
phenotype_id: 
type: Disease or Syndrome
group: Disease or Syndrome
sources:
    - bhfcvdcoviduk
data_sources:
    - Trusted Research Environments for CVD-COVID-UK / COVID-IMPACT
    - Hospital Episode Statistics Admitted Patient Care
clinical_terminologies:
    - ICD-10

valid_event_data_range: 01/07/2020 - 31/03/2022
codelists: 
    - covid_impact_ccu02901_covid-19_type_c_ICD10.csv
    - covid_impact_ccu02901_covid-19_pims-ts_ICD10.csv
    - covid_impact_ccu02901_covid-19_type_a1_ICD10.csv
    - covid_impact_ccu02901_covid-19_type_a2_ICD10.csv
    - covid_impact_ccu02901_covid-19_type_b1_ICD10.csv
    - covid_impact_ccu02901_covid-19_type_b2_ICD10.csv

sex:
    - Female
    - Male
author: 
    - Harrison Wilde, Christopher Tomlinson, Bilal A Mateen, David Selby, Hari Krishnan Kanthimathinathan, Padmanabhan Ramnarayan, Pascale Du Pre, Mae Johnson, Nazima Pathan, Arturo Gonzalez-Izquierdo, Alvina G Lai, Deepti Gurdasani, Christina Pagel, Spiros Denaxas, Sebastian Vollmer, Katherine Brown, On behalf of the CVD-COVID-UK/COVID-IMPACT consortium
publications:
    - "Hospital admissions linked to SARS-CoV-2 infection in children: a cohort study of 3.2 million first ascertained infections in England"
status: DRAFT
date: 2022-09-15
modified_date: 2022-09-15
version: Version 1

---

### Phenotypes

#### England hospitalization EHR: COVID-19 admission - Type C 
{% include csv.html csvdata=site.data.codelists.covid_impact_ccu02901_covid-19_type_c_ICD10 %}
#### England hospitalization EHR: COVID-19 admission - PIMS-TS 
{% include csv.html csvdata=site.data.codelists.covid_impact_ccu02901_covid-19_pims-ts_ICD10 %}
#### England hospitalization EHR: COVID-19 admission - Type A1 
{% include csv.html csvdata=site.data.codelists.covid_impact_ccu02901_covid-19_type_a1_ICD10 %}
#### England hospitalization EHR: COVID-19 admission - Type A2 
{% include csv.html csvdata=site.data.codelists.covid_impact_ccu02901_covid-19_type_a2_ICD10 %}
#### England hospitalization EHR: COVID-19 admission - Type B1 
{% include csv.html csvdata=site.data.codelists.covid_impact_ccu02901_covid-19_type_b1_ICD10 %}
#### England hospitalization EHR: COVID-19 admission - Type B2 
{% include csv.html csvdata=site.data.codelists.covid_impact_ccu02901_covid-19_type_b2_ICD10 %}

### Publication

Hospital admissions linked to SARS-CoV-2 infection in children: a cohort study of 3.2 million first ascertained infections in England

Harrison  Wilde, Christopher Tomlinson, Bilal A Mateen, David Selby, Hari Krishnan Kanthimathinathan, Padmanabhan Ramnarayan, Pascale Du Pre, Mae Johnson, Nazima Pathan, Arturo Gonzalez-Izquierdo, Alvina G Lai, Deepti Gurdasani, Christina Pagel, Spiros Denaxas, Sebastian Vollmer, Katherine Brown, On behalf of the CVD-COVID-UK/COVID-IMPACT consortium

Journal 2022.MM.DD; doi: [https://doi.org/](https://doi.org/)
