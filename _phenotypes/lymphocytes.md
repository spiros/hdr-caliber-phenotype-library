---
layout: phenotype
title: Lymphocytes
phenotype_id: WhLcDKoLxY4qzMKfgAN5DJ
name: Lymphocytes
type: Biomarker
group: Biomarker
data_sources: 
    - Clinical Practice Research Datalink GOLD
clinical_terminologies: 
    - Read Version 2
codelists:
    - shah_lymphocytes_WhLcDKoLxY4qzMKfgAN5DJ_Read2.csv
validation: prognosis
valid_event_data_range: 01/01/1999 - 01/07/2016
sex: 
    - Female
    - Male
author: 
    - Shah A
status: FINAL
date: 2012-11-23
modified_date: 2012-11-23
version: Revision 1
---

### Primary Care

In the Clinical Practice Research Datalink (CPRD, primary care data) we extracted lymphocyte measurements using the structured data component of the test CPRD table (entity type 208) combined with a list of Read terms (see below). The value was extracted from the data2 field where the units data3 field were set as 37 [10*9/L], 153 [10*9], 17 [/L]. We filtered any values less than 50 10^9/L.

{% include csv.html csvdata=site.data.codelists.shah_lymphocytes_WhLcDKoLxY4qzMKfgAN5DJ_Read2 %}

### Implementation

If a patient had more than one measurement on a given day, the values were aggregated by taking the mean. We analysed eosinophil and lymphocyte counts as categorical variables in order to avoid presuming a particular shape for the association with cardiovascular diseases. There were no clinically obvious cutpoints or consistent definitions of ‘normal’ lymphocyte or eosinophil counts in the literature. In the absence of a clear rationale for choosing specific cutpoints, we chose to study quintiles; however, the number of decimal places varied between laboratories (units: cells×109/L) and the absolute values of eosinophil counts were small relative to the precision of recording. In order to avoid biasing the category allocation by precision, we manually adjusted the eosinophil category boundaries, so that the second decimal place was 5, thus ensuring that any values recorded to two decimal places would end up in the same category if they were recorded to only one decimal place. We derived quintile-based categories for lymphocyte counts by a similar method. All category intervals were closed at the lower bound and open at the upper bound, that is, ‘0.05 to 0.15’ includes 0.05 but not 0.15.

Eosinophil and lymphocyte counts can be affected by many factors such as infections, autoimmune diseases, medication and haematological conditions. We sought to differentiate between a patient's long-term ‘stable’ leucocyte profile and results obtained when the patient had an ‘acute’ condition which may alter leucocyte counts. We used other information in the electronic health record to assess whether the patient was clinically ‘acute’ or ‘stable’ at the time of the blood test, adapting a set of criteria proposed by the eMERGE consortium (electronic Medical Records and Genomics) for studying genetic determinants of the stable leucocyte counts: in hospital on the date of blood test, vaccination in the previous 7 days, anaemia diagnosis within the previous 30 days, symptoms or diagnosis of infection within the previous 30 days, prior diagnosis of myelodysplastic syndrome, prior diagnosis of haemoglobinopathy, cancer chemotherapy or granulocyte colony stimulating factor (G-CSF) within 6 months before index date, or the use of drugs affecting the immune system such as methotrexate or steroids within the previous 3 months. Patients with HIV, splenectomy or on dialysis were excluded from this study, as their leucocyte counts may be difficult to interpret.
