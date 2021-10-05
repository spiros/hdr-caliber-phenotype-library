---
layout: phenotype
title: Cancer
phenotype_id: juDLNphaLJPzkbjm2AsG68
name: Cancer
type: Disease or Syndrome
group: Cancer
sources: 
    - clinicalcodes
data_sources:
    - Clinical Practice Research Datalink GOLD
clinical_terminologies:
    - Read Version 2
validation:
codelists: Fairhurst_Cancer_juDLNphaLJPzkbjm2AsG68_Read2.csv
valid_event_data_range: start - 31/12/2014
sex:
    - Female
    - Male
author:
    - Caroline Fairhust
    - Fabiola Martin
    - Ian Watt
    - Tim Doran
    - Martin Bland
    - William J Brackenbury    
publications:
    - Caroline Fairhust, Fabiola Martin, Ian Watt, Tim Doran, Martin Bland, William J Brackenbury, Sodium channel-inhibiting drugs and cancer survival: protocol for a cohort study using the CPRD primary care database. BMJ Open, 6(e0111661),  2016.
status: FINAL
date: 2016-09-06
modified_date: 2016-09-06
version: Revision 1
---

### Primary Care

{% include csv.html csvdata=site.data.codelists.Fairhurst_Cancer_juDLNphaLJPzkbjm2AsG68_Read2 %}

### Implementation

Introduction:  
Voltage-gated sodium channel (VGSC)- inhibiting drugs are commonly used to treat epilepsy and cardiac arrhythmia. VGSCs are also widely expressed in various cancers, including those of the breast, bowel and prostate. A number of VGSCinhibiting drugs have been shown to inhibit cancer cell proliferation, invasion, tumour growth and metastasis in preclinical models, suggesting that VGSCs may be novel molecular targets for cancer treatment. Surprisingly, we previously found that prior exposure to VGSC-inhibiting drugs may be associated with reduced overall survival in patients with cancer, but we were unable to control for the cause of death or indication for prescription. The purpose of the present study is to interrogate a different database to further investigate the relationship between VGSC-inhibiting drugs and cancer-specific survival. 

Methods and analysis: 
A cohort study using primary care data from the Clinical Practice Research Datalink database will include patients with diagnosis of breast, bowel and prostate cancer (13 000). The primary outcome will be cancer-specific survival from the date of cancer diagnosis. Cox proportional hazards regression will be used to compare survival of patients taking VGSC-inhibiting drugs (including antiepileptic drugs and class I antiarrhythmic agents) with patients with cancer not taking these drugs, adjusting for cancer type, age and sex. Drug exposure will be treated as a time-varying covariate to account for potential immortal time bias. Various sensitivity and secondary analyses will be performed.

### Publications

<pre>
Caroline Fairhust, Fabiola Martin, Ian Watt, Tim Doran, Martin Bland, William J Brackenbury, Sodium channel-inhibiting drugs and cancer survival: protocol for a cohort study using the CPRD primary care database. BMJ Open, 6(e0111661),  2016.
</pre>
