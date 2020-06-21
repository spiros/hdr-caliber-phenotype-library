---
layout: phenotype
title: White Blood Cells
phenotype_id: m9LJwQVE3LVudvQ5bCu6MZ
name: White Blood Cells
type: Biomarker
group: Biomarker
data_sources: 
    - Clinical Practice Research Datalink GOLD
clinical_terminologies: 
    - Read Version 2
codelists:
    - shah_white_blood_cells_m9LJwQVE3LVudvQ5bCu6MZ_Read2.csv
validation: prognosis, external
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

In the Clinical Practice Research Datalink (CPRD, primary care data) we extracted white blood cell measurements using the structured data component of the test CPRD table (entity type 207) combined with a list of Read terms (see below). The value was extracted from the data2 field where the units data3 field were set as 37 [10*9/L], 153 [10*9], 17 [/L]. We filtered any values less than 50 10^9/L.

{% include csv.html csvdata=site.data.codelists.shah_white_blood_cells_m9LJwQVE3LVudvQ5bCu6MZ_Read2 %}

### Implementation

Total white cell counts can be affected by many factors such as infections, autoimmune diseases, medication and haematological conditions. Similar to our recent study on eosinophil counts,1 we sought to differentiate between a patient’s long-term ‘stable’ total white cell count and results obtained when the patient had an ‘acute’ condition which may alter leukocyte counts. We used other information in the electronic health record (prescriptions, diagnoses, symptoms, hospitalisations) to assess whether the patient was clinically ‘acute’ or ‘stable’ at the time of the blood test, adapting a set of criteria proposed by the eMERGE consortium (electronic Medical Records and Genomics)2 for studying genetic determinants of the stable leukocyte counts: in hospital on the date of blood test, vaccination in the previous 7 days, anaemia diagnosis within the previous 30 days, symptoms or diagnosis of infection within the previous 30 days, prior diagnosis of myelodysplastic syndrome, prior diagnosis of haemoglobinopathy, cancer chemotherapy or G-CSF within 6 months before index date, the use of drugs affecting the immune system such as methotrexate or steroids within the previous 3 months, prior diagnosis of HIV infection, prior splenectomy or prior dialysis.



