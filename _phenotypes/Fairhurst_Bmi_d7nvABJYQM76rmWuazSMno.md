---
layout: phenotype
title: BMI
phenotype_id: d7nvABJYQM76rmWuazSMno
name: BMI
type: Biomarker
group: Biomarker
sources: 
    - clinicalcodes
data_sources:
    - QResearch
clinical_terminologies:
    - Read Version 2
validation:
codelists: Fairhurst_Bmi_d7nvABJYQM76rmWuazSMno_Read2.csv
valid_event_data_range: 01/01/1998 - 31/12/2013
sex:
    - Female
    - Male
author:
    - Caroline Fairhurst
    - Ian Watt
    - Fabiola Martin
    - Martin Bland
    - William J Brackenbury   
publications:
    - Caroline Fairhurst, Ian Watt, Fabiola Martin, Martin Bland, William J Brackenburry, Exposure to sodium channel-inhibiting drugs and cancer survival protocol for a cohort study using the QResearch primary care database. BMJ Open, 4:e006604 2014.
status: FINAL
date: 2014-11-14
modified_date: 2014-11-14
version: Revision 1
---

### Primary Care

{% include csv.html csvdata=site.data.codelists.Fairhurst_Bmi_d7nvABJYQM76rmWuazSMno_Read2 %}

### Implementation

A cohort study based on primary care data from the QResearch database will include patients with one of the three common tumours: breast, bowel and prostate. The primary outcome will be overall survival from the date of cancer diagnosis. Cox proportional hazards regression will be used to compare the survival of patients with cancer taking VGSC-inhibiting drugs (including anticonvulsants and class I antiarrhythmic agents) with patients with cancer not exposed to these drugs, adjusting for age and sex. Exposure to VGSC-inhibiting drugs will be defined as having at least one prescription for these drugs prior to cancer diagnosis. High and low exposure groups will be identified based on the length of use. A number of sensitivity and secondary analyses will be conducted.

### Publications

<pre>
Caroline Fairhurst, Ian Watt, Fabiola Martin, Martin Bland, William J Brackenburry, Exposure to sodium channel-inhibiting drugs and cancer survival protocol for a cohort study using the QResearch primary care database. BMJ Open, 4:e006604 2014.
</pre>
