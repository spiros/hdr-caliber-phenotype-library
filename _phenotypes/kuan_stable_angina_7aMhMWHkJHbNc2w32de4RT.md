---
layout: phenotype
title: Stable angina
name: Stable angina
phenotype_id: 7aMhMWHkJHbNc2w32de4RT 
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
    - kuan_stable_angina_7aMhMWHkJHbNc2w32de4RT_Read2.csv
    - kuan_stable_angina_7aMhMWHkJHbNc2w32de4RT_ICD10.csv
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
{% include csv.html csvdata=site.data.codelists.kuan_stable_angina_7aMhMWHkJHbNc2w32de4RT_Read2 %}
### Secondary care 
#### Diagnoses 
{% include csv.html csvdata=site.data.codelists.kuan_stable_angina_7aMhMWHkJHbNc2w32de4RT_ICD10 %}
### Implementation 
<pre>Use MODIFIED CALIBER 'Stable angina' phenotyping algorithm:

At the specified date, a patient is considered to have had 'Stable angina' IF they meet the criteria for any of the following on or before the specified date:
    1. Recorded diagnosis of 'Stable angina' in primary or secondary care
    2. Coronary revascularisation without un'Stable angina' or myocardial infarction in the previous 30 days
    3. Primary care record of abnormal coronary angiogram or test showing evidence of myocardial ischaemia

The earliest date on which the individual meets any of the following criteria on or before the specified date is defined as the first event date. Include terms for h/o 'Stable angina':
1.	Recorded diagnosis:
    a)	Primary care diagnosis of ischaemic chest pain: chest_pain_gprd, category 4
    b)	Primary care diagnosis of 'Stable angina': sa_diagnosis_gprd, category 1, category 4
    c)	Secondary care diagnosis of 'Stable angina': angina_hes, category 4
2.	Coronary revascularisation without un'Stable angina' (phenotype_ua) or myocardial infarction (phenotype_mi) in the previous 30 days:
    a)	Primary care record of percutaneous coronary intervention (PCI): pci_gprd, category 2
    b)	Secondary care record of PCI: pci_opcs, category 2
    c)	Primary care record of coronary artery bypass graft (CABG): cabg_gprd, category 2
    d)	Secondary care record of CABG: cabg_opcs, category 2
3.	Test results:
    a)	Primary care record of abnormal stress echocardiogram: stress_echo_gprd, category 3
    b)	Primary care record of abnormal invasive coronary angiogram: angio_gprd, category 3
    c)	Primary care record of abnormal computed tomography coronary angiogram: ct_angio_gprd, category 3
    d)	Primary care record of abnormal magnetic resonance coronary angiogram: mr_angio_gprd, category 3
    e)	Primary care record of abnormal exercise ECG: eecg_gprd, category 3
    f)	Primary care record of myocardial ischaemia on resting ECG: recg_gprd, category 2
    g)	Primary care record of abnormal myocardial perfusion scan: radio_scan_gprd, category 3</pre> 
 
### Publications 
Kuan V., Denaxas S., Gonzalez-Izquierdo A. et al. _A chronological map of 308 physical and mental health conditions from 4 million individuals in the National Health Service_. The Lancet Digital Health - DOI <a href='https://www.thelancet.com/journals/landig/article/PIIS2589-7500(19)30012-3/fulltext'>10.1016/S2589-7500(19)30012-3</a>