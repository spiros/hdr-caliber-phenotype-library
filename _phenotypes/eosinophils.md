---
layout: phenotype
title: PHE00322 - Eosinophils
phenotype_id: PHE00322
name: Eosinophils
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

In the Clinical Practice Research Datalink (CPRD, primary care data) we extracted eosinophil measurements using the structured data component of the test CPRD table (entity type 168) combined with a list of Read terms (see below). The value was extracted from the data2 field where the units data3 field were set as 37 [10*9/L], 153 [10*9], 17 [/L]. We filtered any values less than 50 10^9/L.

{% include csv.html csvdata=site.data.codelists.shah_white_blood_cells_m9LJwQVE3LVudvQ5bCu6MZ_Read2 %}

