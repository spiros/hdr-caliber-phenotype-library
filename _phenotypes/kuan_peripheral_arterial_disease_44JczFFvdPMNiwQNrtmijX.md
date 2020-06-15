---
layout: phenotype
title: Peripheral arterial disease
name: Peripheral arterial disease
phenotype_id: 44JczFFvdPMNiwQNrtmijX 
type: Disease or Syndrome
group: Cardiovascular
data_sources: 
    - Clinical Practice Research Datalink GOLD
    - Hospital Episode Statistics APC for CPRD GOLD
clinical_terminologies: 
    - OPCS-4
    - Read Version 2
    - ICD-10
validation: 
    - cross-source
codelists: 
    - kuan_peripheral_arterial_disease_44JczFFvdPMNiwQNrtmijX_Read2.csv
    - kuan_peripheral_arterial_disease_44JczFFvdPMNiwQNrtmijX_ICD10.csv
    - kuan_peripheral_arterial_disease_44JczFFvdPMNiwQNrtmijX_OPCS4.csv
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
{% include csv.html csvdata=site.data.codelists.kuan_peripheral_arterial_disease_44JczFFvdPMNiwQNrtmijX_Read2 %}
### Secondary care 
#### Diagnoses 
{% include csv.html csvdata=site.data.codelists.kuan_peripheral_arterial_disease_44JczFFvdPMNiwQNrtmijX_ICD10 %}
#### Procedures 
{% include csv.html csvdata=site.data.codelists.kuan_peripheral_arterial_disease_44JczFFvdPMNiwQNrtmijX_OPCS4 %}
### Implementation 
<pre>Use MODIFIED CALIBER 'Peripheral arterial disease' (PAD) phenotyping algorithm: 

At the specified date, a patient is considered to have 'Peripheral arterial disease' IF they meet any of the criteria below on or before the specified date. 

The earliest date on which the individual meets any of the following criteria on or before the specified date is defined as the first event date:
1.	Primary care
    1.	Peripheral vascular disease diagnosis during a consultation. arterial_gprd: category 7
    2.	Record of history of PVD during a consultation. The following Read codes from CPRD:
        1.	Read:14F7.00	Medcode: 106762	Descr:H/O: arterial lower limb ulcer
        2.	Read:14NB.00	Medcode: 59534	Descr: H/O: Peripheral vascular disease procedure
    3.	Leg or aortic embolism or thrombosis diagnosis during a consultation. arterial_gprd: category 8
    4.	'Peripheral arterial disease' procedures, excluding repair of AAA recording during a consultation. pad_opcs_gprd: category 3
    5.	Abnormal 'Peripheral arterial disease' (PAD) ultrasound or Doppler study results recorded during a consultation. As per implementation of pad_ud_gprd in CALIBER
    6.	Abnormal 'Peripheral arterial disease' angiography results recorded during a consultation. As per implementation of pad_angio_gprd in CALIBER
2.	Secondary care
    1.	Primary or secondary diagnosis of Peripheral vascular disease during a hospitalization. arterial_hes: category 7
    2.	Primary or secondary diagnosis of leg or aortic embolism or thrombosis during a hospitalization. arterial_hes: category 8
    3.	Recording of 'Peripheral arterial disease' procedures, excluding repair of AAA. pad_procs_opcs: category 3</pre> 
 
### Publications 
Kuan V., Denaxas S., Gonzalez-Izquierdo A. et al. _A chronological map of 308 physical and mental health conditions from 4 million individuals in the National Health Service_. The Lancet Digital Health - DOI <a href='https://www.thelancet.com/journals/landig/article/PIIS2589-7500(19)30012-3/fulltext'>10.1016/S2589-7500(19)30012-3</a>