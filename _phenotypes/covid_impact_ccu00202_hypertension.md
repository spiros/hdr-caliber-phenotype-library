---
layout: phenotype
title: CCU002_02 Hypertension
name: CCU002_02 Hypertension
phenotype_id: VUrgY3KT6WDCE933KeC7YE
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
clinical_terminologies:
    - SNOMED-CT
    - DM+D
    - British National Formulary (BNF)

valid_event_data_range: 08/12/2020 - 18/03/2021
codelists: 
    - covid_impact_ccu00202_hypertension_England_SNOMEDCT.csv
    - covid_impact_ccu00202_bp_lowering_England_BNF.csv
    - covid_impact_ccu00202_hypertension_drugs_England_DMD.csv
    - covid_impact_ccu00202_hypertension_pregnancy_England_SNOMEDCT.csv

sex:
    - Female
    - Male
author: 
    - CVD-COVID-UK consortium 
    - William N Whiteley
    - Samantha Ip
    - Jennifer A Cooper
    - Thomas Bolton
    - Spencer Keene
    - Venexia Walker
    - Rachel Denholm
    - Ashley Akbari
    - Efosa Omigie
    - Sam Hollings
    - Emanuele Di Angelantonio
    - Spiros Denaxas
    - Angela Wood
    - Jonathan A C Sterne
    - Cathie Sudlow
publications:
    - "Association of COVID-19 vaccines ChAdOx1 and BNT162b2 with major venous, arterial, and thrombocytopenic events: whole population cohort study in 46 million adults in England"
status: FINAL
date: 2021-08-23
modified_date: 2021-08-23
version: Revision 1

---

### Phenotypes

Code type is set to 1 for incident events, and 0 for prevalent events.

#### England primary care EHR: Hypertension diagnosis 
{% include csv.html csvdata=site.data.codelists.covid_impact_ccu00202_hypertension_England_SNOMEDCT %}
#### England primary care EHR: Blood pressure lowering medication prescription 
{% include csv.html csvdata=site.data.codelists.covid_impact_ccu00202_bp_lowering_England_BNF %}
#### England primary care EHR: Hypertension medication prescription 
{% include csv.html csvdata=site.data.codelists.covid_impact_ccu00202_hypertension_drugs_England_DMD %}
#### England primary care EHR: Hypertension during pregnancy 
{% include csv.html csvdata=site.data.codelists.covid_impact_ccu00202_hypertension_pregnancy_England_SNOMEDCT %}

### Publication

Association of COVID-19 vaccines ChAdOx1 and BNT162b2 with major venous, arterial, and thrombocytopenic events: whole population cohort study in 46 million adults in England

CVD-COVID-UK consortium, William N Whiteley, Samantha Ip, Jennifer A Cooper, Thomas Bolton, Spencer Keene, Venexia Walker, Rachel Denholm, Ashley Akbari, Efosa Omigie, Sam Hollings, Emanuele Di Angelantonio, Spiros Denaxas, Angela Wood, Jonathan A C Sterne, Cathie Sudlow

medRxiv 2021.08.18.21262222; doi: [https://doi.org/10.1101/2021.08.18.21262222](https://doi.org/10.1101/2021.08.18.21262222)

