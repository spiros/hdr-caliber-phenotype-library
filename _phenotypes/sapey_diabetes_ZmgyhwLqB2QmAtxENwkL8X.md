---
layout: phenotype
title: Diabetes
name: Diabetes mellitus, of various forms
phenotype_id: ZmgyhwLqB2QmAtxENwkL8X 
type: Disease or Syndrome
group: Endocrine # this has been tagged by the majority of the other diabetes sets
data_sources: 
    - University Hospitals Birmingham electronic patient administration and communications system
    - University Hospitals Birmingham HES submission
clinical_terminologies: 
    - SNOMED-CT
    - ICD-10
validation: 
    - prognostic
codelists:
    - sapey_diabetes_ZmgyhwLqB2QmAtxENwkL8X_ICD10.csv
    - sapey_diabetes_ZmgyhwLqB2QmAtxENwkL8X_SNOMED-CT.csv
valid_event_data_range: 06/10/2004 - 18/02/2021
sex: 
    - Female
    - Male
author: 
    - Prof. Elizabeth Sapey (UHB)
    - PIONEER
publications: 
     - 'Gallier S, Price G, Pandya H, McCarmack G, James C, Ruane B, Forty L, Crosby B, Atkin C, Evans R, Dunn K, Marston E, Crawford C, Levermore M, Modhwadia S, Attwood J, Perks S, Doal R, Gkoutos G, Dormer R, Rosser R, Fanning H, Sapey E: Infrastructure and operating processes of PIONEER, the HDR-UK Data Hub in Acute Care and the workings of the Data Trust Committee: a protocol paper, BMJ Health Care Informatics DOI 10.1136/bmjhci-2020-100294'
status: DRAFT
date: 2021-04-06 # these two seem to use a hyphen in the examples
modified_date: 2021-04-06
version: 1
---

### Secondary care 
{% include csv.html csvdata=site.data.codelists.sapey_diabetes_ZmgyhwLqB2QmAtxENwkL8X_ICD10 %}
{% include csv.html csvdata=site.data.codelists.sapey_diabetes_ZmgyhwLqB2QmAtxENwkL8X_SNOMED-CT %}