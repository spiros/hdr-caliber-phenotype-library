---
layout: phenotype
title: COPD
name: COPD
phenotype_id: Y9JxuQRFPprJDMHSPowJYs 
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
    - axson_COPD_Y9JxuQRFPprJDMHSPowJYs_ICD10.csv
    - axson_COPD_Y9JxuQRFPprJDMHSPowJYs_ICD11.csv
    - axson_COPD_Y9JxuQRFPprJDMHSPowJYs_SNOMEDCT.csv
    - axson_COPD_Y9JxuQRFPprJDMHSPowJYs_UKBIOBANK.csv
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
{% include csv.html csvdata=site.data.codelists.axson_COPD_Y9JxuQRFPprJDMHSPowJYs_SNOMEDCT %}

### Secondary care 

#### Diagnoses 
{% include csv.html csvdata=site.data.codelists.axson_COPD_Y9JxuQRFPprJDMHSPowJYs_ICD10 %}

{% include csv.html csvdata=site.data.codelists.axson_COPD_Y9JxuQRFPprJDMHSPowJYs_ICD11 %}

### UK Biobank

{% include csv.html csvdata=site.data.codelists.axson_COPD_Y9JxuQRFPprJDMHSPowJYs_UKBIOBANK %}

### Mortality

{% include csv.html csvdata=site.data.codelists.axson_COPD_Y9JxuQRFPprJDMHSPowJYs_ICD10 %}

### Implementation

These codes are not intended to be mandatory, but are to be used as a starting point for the identification of COPD in routine EHR. Each study may differ in the sensitivity and specificity of the coding required.

According to the National Institute for Health and Care Excellence (NICE) guidelines for the diagnosis of COPD, COPD should be suspected in patients over 35 years old who have a risk factor (typically smoking) and at least one symptom. It is therefore recommended that these codes are only utilised in an adult population at least 35 years old with a history of smoking.

https://www.nice.org.uk/guidance/ng115/chapter/Recommendations#diagnosing-copd

### Validation

Validation of Read Codes for the Identification of COPD in CPRD

"Quint et al. validated a set of Read codes for the identification of COPD in CPRD in 2014. Using diagnostic codes alone, the positive predictive value (PPV) was 86.5% (77.5?92.3%). Requiring a diagnostic code, spirometry measures, and specific medication increased PPV to 89.4% (80.7?94.5%) but reduced
case numbers by 10%."

### Publications

Publications in 2019 using validated Read codes from Quint et al. 2014

"D. Stolz, Kostikas, K., Loefroth, E., Fogel, R., Gutzwiller, F. S., Conti, V., Cao, H., and Clemens, A., ?Differences in COPD exacerbation risk between women and men: analysis from the UK Clinical Practice Research Datalink data?, Chest, 2019."

"M. Pikoula, Quint, J. K., Nissen, F., Hemingway, H., Smeeth, L., and Denaxas, S., ?Identifying clinically important COPD sub-types using data-driven approaches in primary care population based electronic health records?, BMC Med Inform Decis Mak, vol. 19, p. 86, 2019."

"H. R. Whittaker, Mullerova, H., Jarvis, D., Barnes, N. C., Jones, P. W., Compton, C. H., Kiddle, S. J., and Quint, J. K., ?Inhaled corticosteroids, blood eosinophils, and FEV1 decline in patients with COPD in a large UK primary health care setting?, Int J Chron Obstruct Pulmon Dis, vol. 14, pp. 1063-1073, 2019."

"C. I. Bloom, Ricciardi, F., Smeeth, L., Stone, P., and Quint, J. K., ?Predicting COPD 1-year mortality using prognostic predictors routinely measured in primary care?, BMC Med, vol. 17, p. 73, 2019."

"D. Dedman, Coton, S. J., Ghosh, R. E., Meeraus, W., Crim, C., Harvey, C., Amelio, J., and Landis, S. H., ?Treatment Patterns of New Users of Fluticasone Furoate/Vilanterol in Asthma and COPD in UK Primary Care: Retrospective Cohort Study?, Pulmonary Therapy, vol. 5, pp. 81-95, 2019."

"J. D. Chalmers, Poole, C., Webster, S., Tebboth, A., Dickinson, S., and Gayle, A., ?Assessing the healthcare resource use associated with inappropriate prescribing of inhaled corticosteroids for people with chronic obstructive pulmonary disease (COPD) in GOLD groups A or B: an observational study using the Clinical Practice Research Data?, Respir Res, vol. 19, p. 63, 2018."

Publications in 2019 using Read codes from QOF

"P. Rockenschaub, Jhass, A., Freemantle, N., Aryee, A., Rafiq, M., Hayward, A., and Shallcross, L., ?Opportunities to reduce antibiotic prescribing for patients with COPD in primary care: a cohort study using electronic health records from the Clinical Practice Research Datalink (CPRD)?, J Antimicrob Chemother, 2019."





