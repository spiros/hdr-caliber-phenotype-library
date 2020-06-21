---
layout: phenotype
title: Asthma
name: Asthma
phenotype_id: cdd2NMH5QDWVdEfTQNNfpK 
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
    - axson_asthma_cdd2NMH5QDWVdEfTQNNfpK_ICD10.csv
    - axson_asthma_cdd2NMH5QDWVdEfTQNNfpK_ICD11.csv
    - axson_asthma_cdd2NMH5QDWVdEfTQNNfpK_SNOMEDCT.csv
    - axson_asthma_cdd2NMH5QDWVdEfTQNNfpK_UKBIOBANK.csv
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
{% include csv.html csvdata=site.data.codelists.axson_asthma_cdd2NMH5QDWVdEfTQNNfpK_SNOMEDCT %}

### Secondary care 

#### Diagnoses 
{% include csv.html csvdata=site.data.codelists.axson_asthma_cdd2NMH5QDWVdEfTQNNfpK_ICD10 %}

{% include csv.html csvdata=site.data.codelists.axson_asthma_cdd2NMH5QDWVdEfTQNNfpK_ICD11 %}

### UK Biobank

{% include csv.html csvdata=site.data.codelists.axson_asthma_cdd2NMH5QDWVdEfTQNNfpK_UKBIOBANK %}

### Mortality

{% include csv.html csvdata=site.data.codelists.axson_asthma_cdd2NMH5QDWVdEfTQNNfpK_ICD10 %}

### Implementation

These codes will capture asthma ever, not just current asthma. These codes are not intended to be mandatory, but are to be used as a starting point for the identification of asthma in routine EHR. Each study may differ in the sensitivity and specificity of the coding required.

For those interested in further discrimination of asthma phenotypes, we refer you to Nissen et al. 2019.

F. Nissen, Douglas, I. J., Mullerova, H., Pearce, N., Bloom, C. I., Smeeth, L., and Quint, J. K., ?Clinical profile of predefined asthma phenotypes in a large cohort of UK primary care patients (Clinical Practice Research Datalink)?, J Asthma Allergy, vol. 12, pp. 7-19, 2019.

### Validation

Validation of Read Codes for the Identification of COPD in CPRD

Quint et al. validated a set of Read codes for the identification of COPD in CPRD in 2014. Using diagnostic codes alone, the positive predictive value (PPV) was 86.5% (77.5?92.3%). Requiring a diagnostic code, spirometry measures, and specific medication increased PPV to 89.4% (80.7?94.5%) but reduced case numbers by 10%.

### Publications

Publications from 2019 using validated Read codes from Nissen et al. 2017

"F. Nissen, Douglas, I. J., Mullerova, H., Pearce, N., Bloom, C. I., Smeeth, L., and Quint, J. K., ?Clinical profile of predefined asthma phenotypes in a large cohort of UK primary care patients (Clinical Practice Research Datalink)?, J Asthma Allergy, vol. 12, pp. 7-19, 2019."

"C. I. Bloom, Walker, S., and Quint, J. K., ?Inadequate specialist care referrals for high-risk asthma patients in the UK: an adult population-based cohort 2006-2017?, J Asthma, pp. 1-7, 2019."

"D. Dedman, Coton, S. J., Ghosh, R. E., Meeraus, W., Crim, C., Harvey, C., Amelio, J., and Landis, S. H., ?Treatment Patterns of New Users of Fluticasone Furoate/Vilanterol in Asthma and COPD in UK Primary Care: Retrospective Cohort Study?, Pulmonary Therapy, vol. 5, pp. 81-95, 2019."

Publications from 2019 using Read codes from QOF

"P. Rockenschaub, Jhass, A., Freemantle, N., Aryee, A., Rafiq, M., Hayward, A., and Shallcross, L., ?Opportunities to reduce antibiotic prescribing for patients with COPD in primary care: a cohort study using electronic health records from the Clinical Practice Research Datalink (CPRD)?, J Antimicrob Chemother, 2019."

Wellcome Open Research

https://osf.io/kfz3n/



