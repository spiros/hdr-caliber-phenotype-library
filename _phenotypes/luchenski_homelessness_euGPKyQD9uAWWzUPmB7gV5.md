---
layout: phenotype
title: Homelessness
name: Homelessness
phenotype_id: euGPKyQD9uAWWzUPmB7gV5 
type: Lifestyle Risk Factor
group: Lifestyle Risk Factor
data_sources: 
    - Primary care
    - Hospital Episode Statistics Admitted Patient Care
clinical_terminologies: 
    - ICD-10
validation: 
codelists: 
    - luchenski_homelessness_euGPKyQD9uAWWzUPmB7gV5_ICD10.csv
    - luchenski_homelessness_euGPKyQD9uAWWzUPmB7gV5_GPPractices
valid_event_data_range: 
sex: 
    - Female
    - Male
author: 
    - Luchenski S
publications: 
status: FINAL
date: 2019-05-20
modified_date: 2019-05-20
version: 1
---

### Primary care 

#### Specialist centres or GP practices

{% include csv.html csvdata=site.data.codelists.luchenski_homelessness_euGPKyQD9uAWWzUPmB7gV5_GPPractices %}

### Secondary care 
{% include csv.html csvdata=site.data.codelists.luchenski_homelessness_euGPKyQD9uAWWzUPmB7gV5_ICD10 %}

### Implementation 

Homelessness is not routinely recorded in hospital care records.  We consulted people with lived experience of homelessness and clinical collaborators to produce a set of homeless identifiers including:

    - Those whose address is recorded as ‘no fixed abode’, (NFA)
    - Those who are registered at a known homeless GP practice that exclusively serves those with homelessness problems
    - Those who have a diagnosis that includes the ICD-10 code for homelessness (Z59.0)

Although HES data has undergone cleaning prior to its release by NHS Digital, additional cleaning is necessary to produce a sample ready for analysis.  We applied University of York Centre for Health Economics rules for cleaning including:

    1. Drop poorly coded observations        
        a. Missing on:
            i. HESID (unique identifier)
            ii. Epiend (episode end date)
            iii. Epidur (episode duration)

    2. Drop duplicates – any duplicates across the following variables
        a. HESID (unique identifier), epistart (episode start date), epiorder (episode order), epiend (episode end date), and transit (a variable I derived using the University of York’s code to account for transfers in and out of hospitals that are part of the same admission)

We also applied cleaning rules adapted from the Department of Health report for analysing ‘No Fixed Abode’ (NFA) data:

    3. Drop if age is less than 16yrs for whole cohort 
    4. Drop all neonatal diagnoses
    5. Drop pregnancy termination if patient is only coded with NFA and not coded with HGP or Z59.0 

We also dropped any FCEs included in the data extract if they were not homeless as per the inclusion criteria (i.e. not NFA, HGP, or Z59.0).

