---
layout: phenotype
title: CCU002_01 Cancer
name: CCU002_01 Cancer
phenotype_id: jTyUSQ6GmyGeGSuoytx7Vk
type: Disease or Syndrome
group: Disease or Syndrome
sources:
    - bhfcvdcoviduk
data_sources:
    - Trusted Research Environments for CVD-COVID-UK / COVID-IMPACT
    - GPES Data for Pandemic Planning and Research (COVID-19)
    - Hospital Episode Statistics Admitted Patient Care
    - Secondary Uses Services Payment By Results
    - Civil Registration - Deaths
    - Covid-19 Second Generation Surveillance System

    - COVID-19 Test Results (PATD)
    - Patient Episode Dataset for Wales (PEDW)
    - Welsh Longitudinal GP Dataset - Welsh Primary Care (WLGP)

clinical_terminologies:
    - SNOMED-CT
    - ICD-10
    - Read version 2

valid_event_data_range: 01/01/1997 - 07/12/2020
codelists: 
    - covid_impact_ccu00201_cancer_England_ICD10.csv
    - covid_impact_ccu00201_cancer_England_SNOMEDCT.csv
    - covid_impact_ccu00201_prostate_cancer_England_SNOMEDCT.csv
    - covid_impact_ccu00201_CANCER_Wales_Read2.csv

sex:
    - Female
    - Male
author: 
    - Rochelle Knight
    - Venexia Walker
    - Samantha Ip
    - Jennifer A Cooper
    - Thomas Bolton
    - Spencer Keene
    - Rachel Denholm
    - Ashley Akbari
    - Hoda Abbasizanjani
    - Fatemeh Torabi
    - Efosa Omigie
    - Sam Hollings
    - Teri-Louise North
    - Renin Toms
    - Emanuele Di Angelantonio
    - Spiros Denaxas,
    - Johan H Thygesen
    - Christopher Tomlinson
    - Ben Bray
    - Craig J Smith
    - Mark Barber
    - George Davey Smith
    - Nishi Chaturvedi
    - Cathie Sudlow
    - William N Whiteley
    - Angela Wood
    - Jonathan A C Sterne,
    - CVD-COVID-UK/COVID-IMPACT consortium 
    - Longitudinal Health and Wellbeing COVID-19 National Core Study
publications:
    - "Association of COVID-19 with arterial and venous vascular diseases: a population-wide cohort study of 48 million adults in England and Wales."
status: FINAL
date: 2021-11-24
modified_date: 2021-11-24
version: Revision 1

---

### Phenotypes

#### England hospitalization EHR: Cancer diagnosis 
{% include csv.html csvdata=site.data.codelists.covid_impact_ccu00201_cancer_England_ICD10 %}
#### England primary care EHR: Cancer diagnosis 
{% include csv.html csvdata=site.data.codelists.covid_impact_ccu00201_cancer_England_SNOMEDCT %}
#### England primary care EHR: Prostate cancer diagnosis 
{% include csv.html csvdata=site.data.codelists.covid_impact_ccu00201_prostate_cancer_England_SNOMEDCT %}
#### Wales primary care EHR: Cancer diagnosis 
{% include csv.html csvdata=site.data.codelists.covid_impact_ccu00201_CANCER_Wales_Read2 %}


### Publication

Rochelle Knight, Venexia Walker, Samantha Ip, Jennifer A Cooper, Thomas Bolton, Spencer Keene, Rachel Denholm, Ashley Akbari, Hoda Abbasizanjani, Fatemeh Torabi, Efosa Omigie, Sam Hollings, Teri-Louise North, Renin Toms, Emanuele Di Angelantonio, Spiros Denaxas, Johan H Thygesen, Christopher Tomlinson, Ben Bray, Craig J Smith, Mark Barber, George Davey Smith, Nishi Chaturvedi, Cathie Sudlow, William N Whiteley, Angela Wood, Jonathan A C Sterne, for the CVD-COVID-UK/COVID-IMPACT consortium and the Longitudinal Health and Wellbeing COVID-19 National Core Study. Association of COVID-19 with arterial and venous vascular diseases: a population-wide cohort study of 48 million adults in England and Wales

medRxiv 2021.11.22.21266512; doi: [https://doi.org/10.1101/2021.11.22.21266512](https://doi.org/10.1101/2021.11.22.21266512)

