---
layout: phenotype
title: Pneumonia
name: Pneumonia
phenotype_id: GL46c8PLQMdPuj7QuPtEh9 
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
    - axson_pneumonia_GL46c8PLQMdPuj7QuPtEh9_ICD10.csv
    - axson_pneumonia_GL46c8PLQMdPuj7QuPtEh9_ICD11.csv
    - axson_pneumonia_GL46c8PLQMdPuj7QuPtEh9_SNOMEDCT.csv
    - axson_pneumonia_GL46c8PLQMdPuj7QuPtEh9_UKBIOBANK.csv
valid_event_data_range: 01/01/2001 - 31/12/2019
sex: 
    - Female
    - Male
author: 
    - Eleanor L Axson
    - Jennifer K Quint
publications: 
status: BETA
date: 2020-06-03
modified_date: 2020-06-03
version: 1
---

### Primary care 
{% include csv.html csvdata=site.data.codelists.axson_pneumonia_GL46c8PLQMdPuj7QuPtEh9_SNOMEDCT %}

### Secondary care 
#### Diagnoses 
{% include csv.html csvdata=site.data.codelists.axson_pneumonia_GL46c8PLQMdPuj7QuPtEh9_ICD10 %}

{% include csv.html csvdata=site.data.codelists.axson_pneumonia_GL46c8PLQMdPuj7QuPtEh9_ICD11 %}

### UK Biobank

{% include csv.html csvdata=site.data.codelists.axson_pneumonia_GL46c8PLQMdPuj7QuPtEh9_SNOMEDCT %}

### Mortality

{% include csv.html csvdata=site.data.codelists.axson_pneumonia_GL46c8PLQMdPuj7QuPtEh9_ICD10 %}

### Implementation

These codes will capture both community- and hospital-acquired pneumonia. These codes are not intended to be mandatory, but are to be used as a starting point for the identification of pneumonia in routine EHR. Each study may differ in the sensitivity and specificity of the coding required.

Defining a community-acquired pneumonia occurrence in CPRD and HES, Millett et al. 2013 used the following algorithm:
1) Pneumonia records wtihin 28 days of each other were considered to be separate consultations for the same illness
2) First record of pneumonia was the index date
3) End of a pneumonia occurrence was defined as 28 days after the last pneumonia code within the illness episode
4) In HES, pneumonia coded as the primary diagnosis on the first day of a hospital admission

Defining a hospital-acquired pneumonia occurrence in HES and CPRD, Millett et al. 2013 used the following algorithm:
1) Pneumonia coded at any time beyond the first day of a hospital admission
2) Using CPRD in conjunction with HES, pneumonia coded in CPRD within 14 days of a hospital admission (for any cause) was deemed hospital-acquired
3) In CPRD, use of a hospital-acquired pneumonia code at any time during the pneumonia occurrence

Millett, E. R., Quint, J. K., Smeeth, L., Daniel, R. M., & Thomas, S. L. (2013). Incidence of community-acquired lower respiratory tract infections and pneumonia among older adults in the United Kingdom: a population-based study. PLoS One, 8(9), e75131. doi:10.1371/journal.pone.0075131

Defining a community-acquired pneumonia resulting in hospitalisation occurrence in HES, Hicks et al. 2016 used the following algorithm:
1) In HES, hospital admission following A&E visit, where pneumonia was coded as the primary diagnosis within two days of admission

Defining a hospital-acquired pneumonia occurrence in CPRD and HES, Hicks et al. 2016 used the following algorithm:
1) Pneumonia diagnosis in HES >2 days after hospital admission
2) Pneumonia diagnosed in CPRD within 7 days after hospital discharge

Hicks, B. M., Yin, H., Bladou, F., Ernst, P., & Azoulay, L. (2017). Androgen deprivation therapy for prostate cancer and the risk of hospitalisation for community-acquired pneumonia. Thorax, 72(7), 596-597. doi:10.1136/thoraxjnl-2016-209512

### Publications

Publications identifying pneumonia in CPRD and/or HES:

"Millett, E. R., Quint, J. K., Smeeth, L., Daniel, R. M., & Thomas, S. L. (2013). Incidence of community-acquired lower respiratory tract infections and pneumonia among older adults in the United Kingdom: a population-based study. PLoS One, 8(9), e75131. doi:10.1371/journal.pone.0075131"

"Braeken, D. C., Rohde, G. G., Franssen, F. M., Driessen, J. H., van Staa, T. P., Souverein, P. C., . . . de Vries, F. (2017). Risk of community-acquired pneumonia in chronic obstructive pulmonary disease stratified by smoking status: a population-based cohort study in the United Kingdom. Int J Chron Obstruct Pulmon Dis, 12, 2425-2432. doi:10.2147/COPD.S138435"

"Hicks, B. M., Yin, H., Bladou, F., Ernst, P., & Azoulay, L. (2017). Androgen deprivation therapy for prostate cancer and the risk of hospitalisation for community-acquired pneumonia. Thorax, 72(7), 596-597. doi:10.1136/thoraxjnl-2016-209512"

"Sun, X., Douiri, A., & Gulliford, M. (2019). Pneumonia incidence trends in UK primary care from 2002 to 2017: population-based cohort study. Epidemiol Infect, 147, e263. doi:10.1017/S0950268819001559"

