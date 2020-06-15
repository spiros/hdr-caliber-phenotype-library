---
layout: phenotype
title: Hearing loss
name: Hearing loss
phenotype_id: KiGT2GxSNkwPD8RPF6ZPne 
type: Disease or Syndrome
group: Disease or Syndrome
data_sources: 
    - The Health Improvement Network (THIN)
    - Hospital Episode Statistics Admitted Patient Care
clinical_terminologies: 
    - Read Version 2
    - ICD-10
validation: 
    - cross-source
codelists:    
    - cardoso_hearing_loss_KiGT2GxSNkwPD8RPF6ZPne_Read2.csv
    - cardoso_hearing_loss_KiGT2GxSNkwPD8RPF6ZPne_ICD10.csv
valid_event_data_range: 01/01/1901-31/12/2019
sex: 
    - Female
    - Male
author: 
    - Cardoso V.
    - Nirantharakumar K.
    - Gkoutos G
status: FINAL
date: 2020-06-03
modified_date: 2020-06-03
version: 1
---

### Primary care 
{% include csv.html csvdata=site.data.codelists.cardoso_hearing_loss_KiGT2GxSNkwPD8RPF6ZPne_Read2 %}

### Secondary care 
#### Diagnoses 

{% include csv.html csvdata=site.data.codelists.cardoso_hearing_loss_KiGT2GxSNkwPD8RPF6ZPne_ICD10 %}