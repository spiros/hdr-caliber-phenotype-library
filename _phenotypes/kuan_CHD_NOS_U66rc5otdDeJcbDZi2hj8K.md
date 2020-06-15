---
layout: phenotype
title: Coronary heart disease not otherwise specified
name: Coronary heart disease not otherwise specified
phenotype_id: U66rc5otdDeJcbDZi2hj8K 
type: Disease or Syndrome
group: Cardiovascular
data_sources: 
    - Clinical Practice Research Datalink GOLD
    - Hospital Episode Statistics APC for CPRD GOLD
clinical_terminologies: 
    - Read Version 2
    - ICD-10
validation: 
    - cross-source
codelists: 
    - kuan_CHD_NOS_U66rc5otdDeJcbDZi2hj8K_Read2.csv
    - kuan_CHD_NOS_U66rc5otdDeJcbDZi2hj8K_ICD10.csv
valid_event_data_range: 01/01/1999 - 01/07/2016
sex: 
    - Female
    - Male
author: 
    - Kuan V
    - Denaxas S
    - Gonzalez-Izquierdo A
    - Direk K
    - Bhatti O
    - Husain S
    - Sutaria S
    - Hingorani M
    - Nitsch D
    - Parisinos C
    - Lumbers T
    - Mathur R
    - Sofat R
    - Casas JP
    - Wong I
    - Hemingway H
    - Hingorani A
publications: 
    - 'Kuan V., Denaxas S., Gonzalez-Izquierdo A. et al. A chronological map of 308 physical and mental health conditions from 4 million individuals in the National Health Service. The Lancet Digital Health - DOI: 10.1016/S2589-7500(19)30012-3' 
status: FINAL
date: 2019-05-20
modified_date: 2019-05-20
version: 1
---
### Primary care 
{% include csv.html csvdata=site.data.codelists.kuan_CHD_NOS_U66rc5otdDeJcbDZi2hj8K_Read2 %}
### Secondary care 
#### Diagnoses 
{% include csv.html csvdata=site.data.codelists.kuan_CHD_NOS_U66rc5otdDeJcbDZi2hj8K_ICD10 %}
### Implementation 
<pre>Use MODIFIED CALIBER 'Coronary heart disease not otherwise specified' phenotyping algorithm

At the specified date, a patient is considered to have had 'Coronary heart disease not otherwise specified' IF they meet any of the criteria below on or before the specified date. 

The earliest date on which the individual meets any of the following criteria on or before the specified date is defined as the first event date. 
1.	No previous records meeting the criteria for stable angina OR unstable angina OR myocardial infarction 
AND {
2.	Primary care:  chd_nos_gprd: category 1, 3
    a)	IF Read code in chd_nos_gprd list, THEN chd_nos_gprd= appropriate category
    b)	OR IF enttype = 16, chd_nos_gprd = 1
OR
3.	Secondary care: chd_nos_hes: category 3 }</pre> 
 
### Publications 
Kuan V., Denaxas S., Gonzalez-Izquierdo A. et al. _A chronological map of 308 physical and mental health conditions from 4 million individuals in the National Health Service_. The Lancet Digital Health - DOI <a href='https://www.thelancet.com/journals/landig/article/PIIS2589-7500(19)30012-3/fulltext'>10.1016/S2589-7500(19)30012-3</a>