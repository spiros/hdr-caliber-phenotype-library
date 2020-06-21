---
layout: phenotype
title: LDL Cholesterol
phenotype_id: XqKwYhySZhoQKu8gqeUtdr
name: LDL Cholesterol
type: Biomarker
group: Biomarker
data_sources: 
    - Clinical Practice Research Datalink GOLD
clinical_terminologies: 
    - Read Version 2
codelists:
    - shah_ldl_cholesterol_plasma_XqKwYhySZhoQKu8gqeUtdr_Read2.csv
    - shah_ldl_cholesterol_serum_XqKwYhySZhoQKu8gqeUtdr_Read2
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

In the Clinical Practice Research Datalink (CPRD, primary care data) we extracted Low Density Liporotein (LDL) measurements using the structured data component of the test CPRD table (entity type 177 and 288) combined with the Read terms below.

Measurements were extracted from the data2 field and units from the data3 field. We extracted all values recorded in mmol/L (SUM lookup 96) or mg/dL (SUM lookup 82) and filtered out values below 0 or above 50 mmol/L. Where multiple measurements were present in a single consultation (identified by the consid identifier) we calculated the average.

#### Plasma measurements

{% include csv.html csvdata=site.data.codelists.shah_ldl_cholesterol_plasma_XqKwYhySZhoQKu8gqeUtdr_Read2 %}

#### Serum measurements

{% include csv.html csvdata=site.data.codelists.shah_ldl_cholesterol_serum_XqKwYhySZhoQKu8gqeUtdr_Read2 %}

