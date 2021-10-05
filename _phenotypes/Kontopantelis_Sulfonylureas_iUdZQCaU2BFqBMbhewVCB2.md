---
layout: phenotype
title: Sulfonylureas
phenotype_id: iUdZQCaU2BFqBMbhewVCB2
name: Sulfonylureas
type: Drug
group: Drug
sources: 
    - clinicalcodes
data_sources:
    - Clinical Practice Research Datalink GOLD
clinical_terminologies:
    - CPRD Product Code	
validation:
codelists: Kontopantelis_Sulfonylureas_iUdZQCaU2BFqBMbhewVCB2_CPRDProductCode.csv
valid_event_data_range: 01/04/2006 - 31/03/2012
sex:
    - Female
    - Male
author:
    - Evangelos Kontopantelis
    - David A Springate
    - David Reeves
    - Darren M. Aschroff
    - Martin Rutter
    - Iain Buchan
    - Tim Doran
    - Matthias Pierce
    - Darren M. Ashcroft   
publications:
    - Evangelos Kontopantelis, David A Springate, David Reeves, Darren M. Aschroff, Martin Rutter, Iain Buchan, Tim Doran, Glucose, blood pressure and cholesterol levels and their relationships to clinical outcomes in type 2 diabetes: a retrospective cohort study. Diabetologia, 58:505-518, 2015. 
status: FINAL
date: 2014-12-16
modified_date: 2014-12-16
version: Revision 1
---

### Primary Care

{% include csv.html csvdata=site.data.codelists.Kontopantelis_Sulfonylureas_iUdZQCaU2BFqBMbhewVCB2_CPRDProductCode %}

### Implementation

Data source: 
We used the Clinical Practice Research Datalink (CPRD), a large primary care database that holds complete electronic patient records (including diagnoses, prescriptions and referrals) from participating family practices across the UK. A hierarchical clinical coding system (Read) is used to record the data. In July 2012, data were available for 644 practices and 13,772,992 patients. Full details of the database have been provided elsewhere.

Diabetes cohort:
We extracted data from 1 April 2006 to 31 March 2012 and, for ease of reporting and analysing, aggregated information into six financial years. Within each year, practice inclusion eligibility was determined by a CPRD assessment algorithm, which informs on practices considered to be of research standard; therefore, our cohort of practices varied over time. For each research standard practice and year, we defined as eligible patients those who were registered with the practice for the full year and were aged 18 years or over in that year. From these patients, using relevant Read codes for type 2 diabetes (e.g. C10F.00: Type 2 diabetes mellitus) and excluding those treated with insulin within 2 years of diagnosis, we identified 246,544 patients over the study period. Diagnoses were not constrained to the study period and a relevant code prior to the study as well as during the study period would flag a patient from the respective year onwards. Data on sex, age and removal from the database due to deaths were available and complete for all patients.We extracted data on diabetes-related macrovascular (myocardial infarction, stroke, peripheral vascular disease or amputation) and microvascular (retinopathy, neuropathy, nephropathy [chronic kidney disease stages 4–5] or foot ulcer) complications as well as comorbidities (asthma, coronary heart disease, chronic kidney disease [excluded from microvascular analysis], chronic obstructive pulmonary disease, depression, dementia, severe mental illness, heart failure, hypertension, stroke [excluded from macrovascular analysis], cancer, epilepsy, osteoarthritis, osteoporosis and hypothyroidism). Although we aimed to include all conditions associated with diabetes, the choice was partially determined by the domains incentivised under the Quality and Outcomes Framework (QOF), for which accuracy of diagnosis is considered high. Information was also extracted on smoking (never smoked, current, exsmoker and missing data),BMI, HbA1c levels (%), cholesterol levels (mmol/l) and systolic/diastolic BP (mmHg). Biometric measurement data were cleaned and we calculated patient means for each year when more than one relevant record was available. Using product lists we determined prescription prevalence (at least one) for relevant medications: ACE inhibitors, acarbose, α-blockers, anticoagulants, antiplatelet agents, β-blockers, calcium-channel blockers, thiazide diuretics, loop diuretics, dipeptidyl peptidase-4 inhibitors, glucagon-like peptide- 1 agonists, statins and other lipid-lowering drugs, meglitinides , metformin, sulfonylureas and thiazolidinediones. For approximately 60% of the practices, records were linked to Office of National Statistics (ONS) mortality data and we had access to death dates for all their patients. For these, using ICD-10 codes (www.who.int/classifications/icd/en/) we were able to estimate deathslinked to specific causes (underlying or in the top three): diabetes (E10–E16), ischaemic heart disease (I21–I22), stroke (I60–I64) or stroke excluding bleeds (excluding I63). 

### Publications

<pre>
Evangelos Kontopantelis, David A Springate, David Reeves, Darren M. Aschroff, Martin Rutter, Iain Buchan, Tim Doran, Glucose, blood pressure and cholesterol levels and their relationships to clinical outcomes in type 2 diabetes: a retrospective cohort study. Diabetologia, 58:505-518, 2015. 
</pre>