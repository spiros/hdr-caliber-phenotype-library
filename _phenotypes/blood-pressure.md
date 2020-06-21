---
layout: phenotype
title: Blood Pressure
phenotype_id: FUzVABgwNAexCTqwZHPChw
name: Blood Pressure
type: Biomarker
group: Biomarker
data_sources: 
    - Clinical Practice Research Datalink GOLD
clinical_terminologies: 
    - Read Version 2
validation: prognosis
codelists:
    - rapsomaniki_blood_pressure_FUzVABgwNAexCTqwZHPChw_Read2.csv
valid_event_data_range: 01/01/1999 - 01/07/2016
sex: 
    - Female
    - Male
author: Julie George, Emily Herrett, Liam Smeeth, Harry Hemingway, Anoop Shah, Spiros Denaxas
status: FINAL
date: 2012-11-23
modified_date: 2012-11-23
version: 1
---

### Primary Care

{% include csv.html csvdata=site.data.codelists.rapsomaniki_blood_pressure_FUzVABgwNAexCTqwZHPChw_Read2 %}

### Implementation

Where multiple measurements were present in a single consultation (identified by the consid identifier) we calculated the average. We defined the range of plausible values as 20-350 mmHg for systolic measurements and 20-200 mmHg for diastolic measurements.


