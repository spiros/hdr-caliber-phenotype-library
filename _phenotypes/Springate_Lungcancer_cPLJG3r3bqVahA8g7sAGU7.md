---
layout: phenotype
title: Lung cancer
phenotype_id: cPLJG3r3bqVahA8g7sAGU7
name: Lung Cancer
type: Disease or Syndrome
group: Cancer
sources: 
    - clinicalcodes
data_sources:
    - Clinical Practice Research Datalink GOLD
    - Doctors Independent Network
clinical_terminologies:
    - Read Version 2
validation:
codelists: Springate_Lungcancer_cPLJG3r3bqVahA8g7sAGU7_Read2.csv
valid_event_data_range: 01/01/19997 - 31/12/2006
sex:
    - Female
    - Male
author:
    - David A Springate
    - Darren M Aschroft
    - Evangelos Kontopantelis
    - Tim Doran
    - Ronan Ryan
    - David Reeves    
publications:
    - David A Springate, Darrent M Aschroft, Evangelos Kontopantelis, Tim Doran, Ronan Ryan, David Reeves, Can analyses of electronic patient records be independently and externally validated? Study 2—the effect of β-adrenoceptor blocker therapy on cancer survival a retrospective cohort study. BMJ Open, 5(e007299), 2014.
status: FINAL
date: 2020-10-08
modified_date: 2020-10-08
version: Revision 1
---


### Primary Care

{% include csv.html csvdata=site.data.codelists.Springate_Lungcancer_cPLJG3r3bqVahA8g7sAGU7_Read2 %}

### Implementation

Objectives: 
To conduct a fully independent, external validation of a research study based on one electronic health record database using a different database sampling from the same population. 

Design: 
Retrospective cohort analysis of β-blocker therapy and all-cause mortality in patients with cancer. 

Setting: 
Two UK national primary care databases (PCDs): the Clinical Practice Research Datalink (CPRD) and Doctors’ Independent Network (DIN). 

Participants: 
CPRD data for 11 302 patients with cancer compared with published results from DIN for 3462 patients; study period January 1997 to December 2006. 

Primary and secondary outcome measures:
All-cause mortality: overall; by treatment subgroup (β-blockers only, β-blockers plus other blood pressure lowering medicines (BPLM), other BPLMs only); and by cancer site.

Results: 
Using CPRD, β-blocker use was not associated with mortality (HR=1.03, 95% CI 0.93 to 1.14, vs patients prescribed other BPLMs only), but DIN β-blocker users had significantly higher mortality (HR=1.18, 95% CI 1.04 to 1.33). However, these HRs were not statistically different (p=0.063), but did differ for patients on β-blockers alone (CPRD=0.94, 95% CI 0.82 to 1.07; DIN=1.37, 95% CI 1.16 to 1.61; p<0.001). Results for individual cancer sites differed by study, but only significantly for prostate and pancreas cancers. Results were robust under sensitivity analyses, but we could not be certain that mortality was identically defined in both databases.

Conclusions: 
We found a complex pattern of similarities and differences between databases. Overall treatment effect estimates were not statistically different, adding to a growing body of evidence that different UK PCDs produce comparable effect estimates. However, individually the two studies lead to different conclusions regarding the safety of β-blockers and some subgroup effects differed significantly. Single studies using even internally wellvalidated databases do not guarantee generalisable results, especially for subgroups, and confirmatory studies using at least one other independent data source are strongly recommended.

### Publications

<pre>
David A Springate, Darrent M Aschroft, Evangelos Kontopantelis, Tim Doran, Ronan Ryan, David Reeves, Can analyses of electronic patient records be independently and externally validated? Study 2—the effect of β-adrenoceptor blocker therapy on cancer survival a retrospective cohort study. BMJ Open, 5(e007299), 2014.
</pre>
