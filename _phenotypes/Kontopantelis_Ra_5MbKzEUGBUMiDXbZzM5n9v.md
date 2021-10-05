---
layout: phenotype
title: Rheumatoid Arthritis
phenotype_id: 5MbKzEUGBUMiDXbZzM5n9v
name: Rheumatoid Arthritis
type: Disease or Syndrome
group: Musculoskeletal
sources: 
    - clinicalcodes
data_sources:
    - Clinical Practice Research Datalink GOLD
clinical_terminologies:
    - Read Version 2
validation:
codelists: Kontopantelis_Ra_5MbKzEUGBUMiDXbZzM5n9v_Read2.csv
valid_event_data_range: 01/04/2000 - 31/03/2012
sex:
    - Female
    - Male
author:
    - Evangelos Kontopantelis
    - Ivan Olier
    - Claire Planner
    - David Reeves
    - Darren M Ashcroft
    - Linda Gask
    - Tim Doran
    - Sioban Reilly    
publications:
    - Evangelos Kontopantelis, Ivan Olier, Claire Panner, David Reeves, Darren M Ashcroft, Linda Gask, Tim Doran, Siobhan Reilly, Primary care consultation rates among people with and without severe mental illness a UK cohort study using the Clinical Practice Research Datalink. BMJ Open, 5 (e008650), 2015.
status: FINAL
date: 2015-12-16
modified_date: 2015-12-16
version: Revision 1
---


### Primary Care

{% include csv.html csvdata=site.data.codelists.Kontopantelis_Ra_5MbKzEUGBUMiDXbZzM5n9v_Read2 %}

### Implementation

The database:
The CPRD is a large computerised database of anonymised primary care medical records. It contains complete patient information for participating practices, with the healthcare events (diagnoses, treatments, referrals, tests and prescriptions) recorded using coding systems (Read coding for diagnoses). Practice characteristics are described in detail elsewhere. The database is broadly representative of the UK population, although larger practices are over-represented. Practices need to meet prespecified data entry quality criteria to be defined as ‘up to research standard’, and for each study year, our main sample included all CPRD practices that were classed as such for the whole year. We also generated two data sets to test the sensitivity of our findings. First, we included all practices contributing data across the entire study period. Second, we included a subsample of 50 practices, representative of UK practices in terms of area deprivation, and practice list size.

Defining people with SMI and controls:
Information was extracted for the period 1 April 2000 to 31 March 2012 and aggregated into 12 yearly ‘bins’, to correspond with financial years 2000/2001–2011/2012. We used Read codes to identify the presence of SMI. First, we identified relevant keywords (or key-stubs) and codes, for example ‘paranoi’ and ‘E100.00’ (simple schizophrenia). Next, the CPRD was searched for codes that matched the list in either the code or the description field. Finally, the matched code list was reviewed by clinical experts and a final conservative list of codes was agreed. A similar process was used to define comorbidities (hypertension, asthma, hypothyroidism, osteoarthritis, chronic kidney disease, coronary heart disease, epilepsy, chronic obstructive pulmonary disease, cancer, stroke, heart failure, rheumatoid arthritis, dementia and psoriasis). All code lists we used are available from http://www.clinicalcodes.org. All conditions, bar asthma, were treated as unresolvable (ie, permanent). Within each year, all patients registered with a CPRD practice for the whole year and aged 18 or over were eligible for inclusion. The final SMI Read code list was used to identify cases of SMI, which were then grouped into three broad subcategories, in line with the diagnoses used when compiling primary care QOF SMI registers: schizophrenia; affective psychoses (bipolar disorder or other unspecified affective psychosis); other types of psychosis. In the event that an individual received more than one SMI diagnosis over the study period, we used the last available diagnosis to retrospectively ‘correct’ the original diagnosis (ie, we assumed that the latest diagnosis was the correct one). Within each year, each SMI case was then matched on age, sex and practice to five randomly selected patients not associated with SMI up until that time point. More details on the extraction of the cohort have been provided elsewhere,21 and a flow chart of the data extraction process is available in the online appendix figure A2.

Defining consultation type:
We defined a ‘consultation’ as involving direct contact between a patient and a healthcare professional within the primary care setting. We divided consultations into two main categories: face-to-face (our primary outcome), and by telephone (see online appendix table A1). We also constructed a third ‘other’ grouping of all other activities that are captured by the ‘consultation type’ codes within the CPRD. This includes mail/email contact, third party consultations (including referrals), secondary care episodes, other administrative tasks and consultations of unknown content. This group is highly heterogeneous and includes many activities that cannot be classed as consultations. However, we decided to use this grouping as an aggregate secondary outcome since it can potentially provide insight into the overall workload associated with patient care in the primary care context. We decided against breaking down the ‘other’ group in more subcategories as we are very doubtful regarding the reliability and across practice consistency of the coding within these ‘other’ categories. In instances where a patient had two or more consultations within a day, we conservatively assumed a single consultation took place, to reduce the likelihood of including duplicate records.


### Publications

<pre>
Evangelos Kontopantelis, Ivan Olier, Claire Panner, David Reeves, Darren M Ashcroft, Linda Gask, Tim Doran, Siobhan Reilly, Primary care consultation rates among people with and without severe mental illness a UK cohort study using the Clinical Practice Research Datalink. BMJ Open, 5 (e008650), 2015.
</pre>
