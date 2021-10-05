---
layout: phenotype
title: Sore Throat
phenotype_id: 3dUKuzEkGxZZW8pfoh8jG8
name: Sore Throat
type: Disease or Syndrome
group: 
sources: 
    - clinicalcodes 
data_sources:
    - The Health Improvement Network
clinical_terminologies:
    - Read Version 2
validation:
codelists: Hawker_Sorethroat_3dUKuzEkGxZZW8pfoh8jG8_Read2.csv
valid_event_data_range: 1995 - 2011
sex:
    - Female    
author:
    - Jeremy I Hawker
    - Sue Smith
    - Gillian E Smith
    - Roger Morbey
    - Alan P Johnson
    - Douglas M Fleming
    - Laura Shallcross
    - Andrew C Hayward    
publications:
    - Jeremy I Hawker, Sue Smith, Gillian E Smith, Roger Morbey, Alan P Johnson, Douglas M Fleming, Laura Shallcross, Andrew C Hayward, Trends in antibiotic prescribing in primary care for clinical syndromes subject to national recommendations to reduce antibiotic resistance, UK 1995–2011: analysis of a large database of primary care consultations. J Antimicrob Chemother, 69(3423-3430), 2014.
status: FINAL
date: 2014-08-04
modified_date: 2014-08-04
version: Revision 1
---


### Primary Care

{% include csv.html csvdata=site.data.codelists.Hawker_Sorethroat_3dUKuzEkGxZZW8pfoh8jG8_Read2 %}

### Implementation

This was an indication–prescription descriptive cross-sectional study using data from The Health Improvement Network (THIN), a computerized database of consultation data from 570 general practices that use the Vision practice software system, covering 3.8 million active patients (resulting in 68 million patient–years of data). The population covered has similar demographic characteristics to the national UK population,and the recording of consultations and prescriptions is comparable to national levels. Data are validated to ensure that they meet quality standards12 and data quality compliance dates are included to show when practices meet recording standards: practice data were only included in our analyses after the later of the acceptable mortality reporting date or the acceptable computer usage date, resulting in 537 practices being included in our study.

Diagnosis and prescribing data at the individual (anonymized) patient level were linked to determine the condition for which the antimicrobial was prescribed. For each clinical syndrome a list of search terms (keywords and synonyms) was produced and used to search the descriptions in the Read code dictionary. In the resulting Read code list, code stems were searched to include all codes containing the specified sequence of characters. This list was then pruned by two medical epidemiologists (J. I. H. and G. E. S.) to decide on the codes to be included for each condition and were checked by A. C. H., A. P. J. and D. M. F. Code lists were constructed for specificity rather than sensitivity (e.g. tonsillitis, but not influenza, was included in the sore throat list) and codes were excluded if they were likely to contain a significant number of consultations for which the relevant SMAC/PHLS recommendation was likely to be inappropriate: for example, those sore throats that were recorded as ‘bacterial’ or ‘streptococcal’ were excluded fromthe sore throat code list, and the UTI code list did not include chronic or recurring infections, kidney infections or conditions related to pregnancy (the code lists are available in Table S1, available as Supplementary data at JACOnline). The drug code list included all antibiotics in Chapter 5.1 of the British National Formulary, excluding antituberculosis drugs and antileprotic drugs. A prescription was linked to a consultation if both occurred on the same date. An episode of acute infection was defined as a newly recorded diagnosis that was not preceded by a consultation for the same diagnosis reported in the previous 14 days.

Stata v12 survival analysis commands were used to obtain overall incidence rates for each clinical condition in total and those cases prescribed an antibiotic. Yearly changes were assessed by calculating CIs reflecting the average change in percentiles year on year within practices, thereby removing the effect of between-practice variation. Variation by practice was illustrated by a funnel plot, which allowed an inspection of random variation according to practice size and was presented as a range from the 10th percentile to the 90th percentile (TNPR) or IQR to exclude outlying practices that might be atypical. The variation in the proportion of patients prescribed antibiotics was analysed by age group (0–4, 5–14, 15–24, 25–54, 55–64, 65–74, 75–84 and 85–94 years) and, for the cough/cold indicator, by socioeconomic status, using quintiles of increasing deprivation provided in the THIN database (derived from Townsend scores based on patients’ postcodes). For UTI, only women aged 16–74 years were included, and for trimethoprim and nitrofurantoin prescriptions the course length was calculated by dividing the ‘quantity prescribed’ field by the ‘calculated daily dosage’ field. The protocol for this work was approved by the THIN Scientific Review Committee (SRC ref 12-002). No patient-identifiable data were used and no new information was collected for this project.

### Publications

<pre>
Jeremy I Hawker, Sue Smith, Gillian E Smith, Roger Morbey, Alan P Johnson, Douglas M Fleming, Laura Shallcross, Andrew C Hayward, Trends in antibiotic prescribing in primary care for clinical syndromes subject to national recommendations to reduce antibiotic resistance, UK 1995–2011: analysis of a large database of primary care consultations. J Antimicrob Chemother, 69(3423-3430), 2014.
</pre>