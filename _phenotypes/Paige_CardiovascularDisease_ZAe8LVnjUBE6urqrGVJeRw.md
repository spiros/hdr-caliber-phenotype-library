---
layout: phenotype
title: Cardiovascular Disease
phenotype_id: ZAe8LVnjUBE6urqrGVJeRw
name: Cardiovascular Disease
type: Disease or Syndrome                   
group: Cardiovascular Disease
sources: 
    - clinicalcodes
data_sources:
    - Clinical Practice Research Datalink GOLD
clinical_terminologies:
    - Read Version 2
validation:
codelists: Paige_CardiovascularDisease_ZAe8LVnjUBE6urqrGVJeRw_Read2.csv
valid_event_data_range: 01/01/1997 - 18/01/2016
sex:
    - Female
    - Male
author: 
    - Ellie Paige
    - Jessica Barret
    - David Stevens
    - Ruth H Keog
    - Michael J Sweeting
    - Irwin Nazareth
    - Irene Petersen
    - Angela M Wood
publications:
    - Ellie Paige, Jessica Barret, David Stevens, Ruth H Keog, Michael J Sweeting, Irwin Nazareth, Irene Petersen, Angela M Wood, Landmark Models for Optimizing the Use of Repeated Measurements of Risk Factors in Electronic Health Records to Predict Future Disease Risk. American Journal of Epidemiology, 187(7), 1530-1538 (2018).
status: FINAL
date: 2018-03-23
modified_date: 2018-03-23
version: Revision 1
---

### Primary Care

{% include csv.html csvdata=site.data.codelists.Paige_CardiovascularDisease_ZAe8LVnjUBE6urqrGVJeRw_Read2 %}

### Implementation

Individuals entered the study from the latest of the following
dates: 
1) the date of registration at a general practice plus 6 months
2) the date for acceptable computer usage (quality measurement defined as the year in which a general practice continuously used their computer system for recording of medical events and prescribing) 
3) the date for acceptable mortality reporting (the date on which mortality recording reflected that of the United Kingdom general population) 
4) the date on which the individual turned 30 years of age 
   or 
5) January 1, 1997. Individuals exited the study at the earliest of the following dates:
	a) their first (i.e., “incident”) newly recorded CVD event
	b) transfer out of the general practice; 
	c) their date of death; 
	   or 
	d) January 18, 2016. The target population for which we wanted to estimate CVD risk included persons with general practice records and without a history of CVD or statin prescriptions

A 2-stage approach to construct a dynamic risk prediction model, first modeling historical repeated risk factor measurements using multivariate mixed-effects linear models and then estimating 10-year CVD risk using Cox proportional hazards models

### Publications

<pre>
Ellie Paige, Jessica Barret, David Stevens, Ruth H Keog, Michael J Sweeting, Irwin Nazareth, Irene Petersen, Angela M Wood, "Landmark Models for Optimizing the Use of Repeated Measurements of Risk Factors in Electronic Health Records to Predict Future Disease Risk. American Journal of Epidemiology". 187(7), 1530-1538, 2018.

</pre>
