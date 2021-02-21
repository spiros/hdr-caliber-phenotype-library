---
layout: phenotype
title: Depression
name: Depression
phenotype_id: cEacXgEFhPdVWcUgWULATV 
type: Disease or Syndrome
group: Psychiatric
data_sources: 
    - Clinical Practice Research Datalink GOLD
    - Hospital Episode Statistics APC for CPRD GOLD
clinical_terminologies: 
    - Read Version 2
    - ICD-10
validation: 
    - cross-source
codelists: 
    - kuan_depression_cEacXgEFhPdVWcUgWULATV_Read2.csv
    - kuan_depression_cEacXgEFhPdVWcUgWULATV_ICD10.csv
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
{% include csv.html csvdata=site.data.codelists.kuan_depression_cEacXgEFhPdVWcUgWULATV_Read2 %}
### Secondary care 
#### Diagnoses 
{% include csv.html csvdata=site.data.codelists.kuan_depression_cEacXgEFhPdVWcUgWULATV_ICD10 %}
### Implementation 
<pre>At the specified date, a patient is defined as having had 'Depression' IF they meet the criteria for any of the following on or before the specified date. The earliest date on which the individual meets any of the following criteria on or before the specified date is defined as the first event date:

Primary care
1. 'Depression' diagnosis or history of diagnosis during a consultation 
OR
Secondary care
1. ALL diagnoses of 'Depression' or history of diagnosis during a hospitalization</pre> 
 
<button type="button" class="btn btn-sm"><a href="https://kclhi.org/phenoflow/phenotype/download/13">Phenoflow implementation</a></button>
### Publications 
Kuan V., Denaxas S., Gonzalez-Izquierdo A. et al. _A chronological map of 308 physical and mental health conditions from 4 million individuals in the National Health Service_. The Lancet Digital Health - DOI <a href='https://www.thelancet.com/journals/landig/article/PIIS2589-7500(19)30012-3/fulltext'>10.1016/S2589-7500(19)30012-3</a>