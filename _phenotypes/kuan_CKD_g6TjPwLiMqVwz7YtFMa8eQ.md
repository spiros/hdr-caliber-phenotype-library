---
layout: phenotype
title: Chronic Kidney Disease
name: Chronic Kidney Disease
phenotype_id: g6TjPwLiMqVwz7YtFMa8eQ 
type: Disease or Syndrome
group: Genitourinary
data_sources: 
clinical_terminologies: 
validation: 
    - cross-source
codelists: 
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
### Implementation 
<pre>Apply modified CALIBER 'Chronic Kidney Disease' algorithm in CPRD primary care data as follows:

A patient is defined as having had CKD stage 3 or above at a specified date:

IF egfr_ckdepi recorded on or before specified date, THEN 
IF egfr_ckdepi <60 ml/min on the most recent date (index date) before the specified date
AND
IF egfr_ckdepi <60 ml/min on any date greater than 90 days BEFORE the index date above
THEN classify as having CKD3 or above
ELSE the patient is not defined as having CKD stage 3 or above.

Where egfr_ckdepi up to and including 31 Dec 2013 is defined as: 
egfr_ckdepi = 141 * min(crea_gprd * 0.010746 / K, 1)^alpha
* max(crea_gprd * 0.010746 / K, 1)^-1.209 
* 0.993^age * 1.018 [if female]  * 1.159 [if black]

where:
alpha = -0.329 for females, -0.411 for males
K = 0.7 for females, 0.9 for males

Where egfr_ckdepi from and including 1 Jan 2014 is defined as: 
egfr_ckdepi = 141 * min(crea_gprd * 0.010746 / K, 1)^alpha
* max(crea_gprd * 0.0.011312/ K, 1)^-1.209 
* 0.993^age * 1.018 [if female]  * 1.159 [if black]

where:
alpha = -0.329 for females, -0.411 for males
K = 0.7 for females, 0.9 for males

Where crea_gprd is defined as:
IF enttype = 165 [Serum creatinine] 
AND data1 [Operator] = 3 ["="] AND data2 [Value] > 0
THEN crea_gprd = data2</pre> 
 
### Publications 
Kuan V., Denaxas S., Gonzalez-Izquierdo A. et al. _A chronological map of 308 physical and mental health conditions from 4 million individuals in the National Health Service_. The Lancet Digital Health - DOI <a href='https://www.thelancet.com/journals/landig/article/PIIS2589-7500(19)30012-3/fulltext'>10.1016/S2589-7500(19)30012-3</a>