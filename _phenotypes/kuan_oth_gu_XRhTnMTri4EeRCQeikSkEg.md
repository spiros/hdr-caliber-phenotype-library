---
layout: phenotype
title: Infection of other or unspecified genitourinary system
name: Infection of other or unspecified genitourinary system
phenotype_id: XRhTnMTri4EeRCQeikSkEg 
type: Disease or Syndrome
group: Infections
data_sources: 
    - Hospital Episode Statistics APC for CPRD GOLD
clinical_terminologies: 
    - ICD-10
validation: 
    - cross-source
codelists: 
    - kuan_oth_gu_XRhTnMTri4EeRCQeikSkEg_ICD10.csv
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
### Secondary care 
#### Diagnoses 
{% include csv.html csvdata=site.data.codelists.kuan_oth_gu_XRhTnMTri4EeRCQeikSkEg_ICD10 %}
### Implementation 
<pre>At the specified date, a patient is defined as having had 'Infection of other or unspecified genitourinary system' IF they meet the criteria for any of the following on or before the specified date. The earliest date on which the individual meets any of the following criteria on or before the specified date is defined as the first event date:

Secondary care
1. ALL diagnoses of 'Infection of other or unspecified genitourinary system' or history of diagnosis during a hospitalization
OR
2. ALL possible diagnosis of 'Infection of other or unspecified genitourinary system' during a hospitalization IF NO record satisfying criteria for Urinary Tract Infections, Infection of male genital system or Female pelvic inflammatory disease 30 days before or 30 days after the first event date for 'Infection of other or unspecified genitourinary system'.</pre> 
 
### Publications 
Kuan V., Denaxas S., Gonzalez-Izquierdo A. et al. _A chronological map of 308 physical and mental health conditions from 4 million individuals in the National Health Service_. The Lancet Digital Health - DOI <a href='https://www.thelancet.com/journals/landig/article/PIIS2589-7500(19)30012-3/fulltext'>10.1016/S2589-7500(19)30012-3</a>