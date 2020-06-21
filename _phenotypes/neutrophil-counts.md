---
layout: phenotype
title: Lymphocytes
phenotype_id: h8uDoPABk2tJXyh7cv3HjL
name: Neutrophils
type: Biomarker
group: Biomarker
data_sources: 
    - Clinical Practice Research Datalink GOLD
clinical_terminologies: 
    - Read Version 2
codelists:
    - shah_neutrophils_h8uDoPABk2tJXyh7cv3HjL_Read2.csv
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

In the Clinical Practice Research Datalink (CPRD, primary care data) we extracted neutrophil measurements using the structured data component of the test CPRD table (entity type 184) combined with a list of Read terms (see below). The value was extracted from the data2 field where the units data3 field were set as 37 [10*9/L], 153 [10*9], 17 [/L]. We filtered any values less than 50 10^9/L.

{% include csv.html csvdata=site.data.codelists.shah_neutrophils_h8uDoPABk2tJXyh7cv3HjL_Read2 %}

### Implementation

We used information in the primary care and hospitalization records to classify the patient state on the date of the differential leukocyte count. These criteria were based on the recommendations of the eMERGE consortium (http://phenotype.mc.vanderbilt.edu/group/emerge-phenotype-wg) for studies to identify genetic determinants of the underlying stable leukocyte count. The eMERGE criteria were modified to be suitable for a cohort study, avoiding the use of clinical events after the index date in order to avoid immortal time bias. The criteria for an 'acute' patient state were: in hospital on the date of blood test, vaccination in the previous 7 days, anemia diagnosis within the previous 30 days, symptoms or diagnosis of infection within the previous 30 days, prior diagnosis of myelodysplastic syndrome, prior diagnosis of hemoglobinopathy, cancer chemotherapy or G-CSF within 6 months before index date, or the use of drugs affecting the immune system such as methotrexate or steroids within the previous 3 months.

Values with missing units frequently have zero recorded, but this is not the case if units are provided. It is theoretically possible to have a neutrophil count measured as zero (severely immunosuppressed patients, or if white cell count is below the lower limit of detection). It is up to the analyst to remove zero values if desired.

