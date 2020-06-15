---
layout: phenotype
title: Neonatal jaundice (excl haemolytic dz of the newborn)
name: Neonatal jaundice (excl haemolytic dz of the newborn)
phenotype_id: MEqZPyc5s3rBZqLaCnkMfB 
type: Disease or Syndrome
group: Perinatal
data_sources: 
    - Clinical Practice Research Datalink GOLD
    - Hospital Episode Statistics APC for CPRD GOLD
clinical_terminologies: 
    - Read Version 2
    - ICD-10
validation: 
    - cross-source
codelists: 
    - kuan_neo_jaundice_MEqZPyc5s3rBZqLaCnkMfB_Read2.csv
    - kuan_neo_jaundice_MEqZPyc5s3rBZqLaCnkMfB_ICD10.csv
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
{% include csv.html csvdata=site.data.codelists.kuan_neo_jaundice_MEqZPyc5s3rBZqLaCnkMfB_Read2 %}
### Secondary care 
#### Diagnoses 
{% include csv.html csvdata=site.data.codelists.kuan_neo_jaundice_MEqZPyc5s3rBZqLaCnkMfB_ICD10 %}
### Implementation 
<pre>At the specified date, a patient is defined as having had 'Neonatal jaundice (excl haemolytic dz of the newborn)' (excl haemolytic dz of the newborn) IF they meet the criteria for any of the following on or before the specified date. The earliest date on which the individual meets any of the following criteria on or before the specified date is defined as the first event date:

Primary care
1. 'Neonatal jaundice (excl haemolytic dz of the newborn)' (excl haemolytic dz of the newborn) diagnosis or history of diagnosis during a consultation AND IF the patient is aged < 1y at the first event date
OR
Secondary care
1. ALL diagnoses of  'Neonatal jaundice (excl haemolytic dz of the newborn)' (excl haemolytic dz of the newborn) or history of diagnosis during a hospitalization AND IF the patient is aged < 1y at the first event date</pre> 
 
### Publications 
Kuan V., Denaxas S., Gonzalez-Izquierdo A. et al. _A chronological map of 308 physical and mental health conditions from 4 million individuals in the National Health Service_. The Lancet Digital Health - DOI <a href='https://www.thelancet.com/journals/landig/article/PIIS2589-7500(19)30012-3/fulltext'>10.1016/S2589-7500(19)30012-3</a>