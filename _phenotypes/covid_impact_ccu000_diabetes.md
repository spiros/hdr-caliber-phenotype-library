---
layout: phenotype
title: CCU000 Diabetes
name: CCU000 Diabetes
phenotype_id: HKHVFZSTWKw65j8JDwcgDc
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
    - ICD-10

valid_event_data_range: 31/01/2020 - 31/10/2020
codelists:
    - covid_impact_ccu000_England_diabetes_ICD10.csv
    - covid_impact_ccu000_England_diabetes_SNOMEDCT.csv

sex:
    - Female
    - Male
author:
    - Angela Wood, Rachel Denholm, Sam Hollings, Jennifer Cooper, Samantha Ip,Venexia Walker, Spiros Denaxas, Ashley Akbari, Amitava Banerjee, William Whiteley, Alvina Lai, Jonathan Sterne, Cathie Sudlow, CVD-COVID-UK consortium
publications:
    - Linked electronic health records for research on a nationwide cohort of more than 54 million people in England data resource
status: FINAL
date: 29-03-2020
modified_date: 29-03-2020
version: Revision 1

---

### Phenotypes

#### England hospitalization EHR: Diabetes diagnosis 
{% include csv.html csvdata=site.data.codelists.covid_impact_ccu000_England_diabetes_ICD10 %}
#### England primary care EHR: Diabetes diagnosis 
{% include csv.html csvdata=site.data.codelists.covid_impact_ccu000_England_diabetes_SNOMEDCT %}

### Publication


Angela Wood, Rachel Denholm, Sam Hollings, Jennifer Cooper, Samantha Ip,Venexia Walker, Spiros Denaxas, Ashley Akbari, Amitava Banerjee, William Whiteley, Alvina Lai, Jonathan Sterne, Cathie Sudlow, CVD-COVID-UK consortium. 
Linked electronic health records for research on a nationwide cohort of more than 54 million people in England data resource BMJ 2021; 373 :n826 doi:10.1136/bmj.n826

[https://www.bmj.com/content/373/bmj.n826]([https://www.bmj.com/content/373/bmj.n826)



