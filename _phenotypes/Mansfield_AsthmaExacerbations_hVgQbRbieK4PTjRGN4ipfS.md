---
layout: phenotype
title: Asthma Exacerbations
phenotype_id: hVgQbRbieK4PTjRGN4ipfS
name: Asthma Exacerbations
type: Disease or Syndrome
group: Respiratory
data_sources:
    - Clinical Practice Research Datalink AURUM
clinical_terminologies:
    - SNOMED-CT
validation:
codelists: Mansfield_AsthmaExacerbations_hVgQbRbieK4PTjRGN4ipfS_SNOMEDCT.csv 
valid_event_data_range: 01/01/2017 - 12/07/2020 
sex:
    - Female
    - Male
author: 
    - Kathryn E Mansfield
    - Rohini Mathur
    - John Tazare
    - Alasdair D Henderson
    - Amy Mulick
    - Helena Carreira
    - Anthony A Matthews
    - Patrick Bidulka
    - Alicia Gayle
    - Harriet Forbes
    - Sarah Cook
    - Angel YS Wong
    - Helen Strongman
    - Kevin Wing
    - Charlotte Warren-Gash
    - Sharon L Cadogan
    - Liam Smeeth
    - Joseph Hayes
    - Jennifer K Quint
    - Martin McKee
    - Sinéad M Langan
publications:
    - Kathryn E Mansfield, Rohini Mathur, John Tazare, Alasdair D Henderson, Amy Mulick, Helena Carreira, Anthony A Matthews, Patrick Bidulka, Alicia Gayle, Harriet Forbes, Sarah Cook, Angel YS Wong, Helen Strongman, Kevin Wing, Charlotte Warren-Gash, Sharon L Cadogan, Liam Smeeth, Joseph Hayes, Jennifer K Quint, Martin McKee, Sinéad M Langan, COVID-19 collateral Indirect acute effects of the pandemic on physical and mental health in the UK. medRxiv (2020).
status: FINAL
date: 2020-10-30
modified_date: 2020-10-30
version: Revision 1
---

### Primary Care

{% include csv.html csvdata=site.data.codelists.Mansfield_AsthmaExacerbations_hVgQbRbieK4PTjRGN4ipfS_SNOMEDCT %}

### Implementation

This study used a routinely collected primary care data from electronic health records from general practices
contributing to Clinical Research Practice Datalink (CPRD) Aurum database (August 2020 build) in the three
years prior to the COVID-19 pandemic and four months after introducing population-wide restrictions (i.e.
‘lockdown’) on 23rd March 2020 (1st January 2017- 12th July 2020) and an interrupted time series (ITS) analysis is used to formally quantify changes in conditions. 

All individuals (aged ≥11 years) with a current asthma diagnosis (i.e. asthma code
in the last two or three years if aged <18 years or 18+ years, respectively).
Individuals joined the study population from the start of follow-up in the overall
population if there was a current asthma diagnosis (i.e. within last 2-3 years) at
this time or from the date of their first record indicating an asthma diagnosis
within overall follow-up. Participants remained in the study until there was no
current asthma diagnosis or the end of overall follow-up. They were able to reenter
the study if there was a later diagnostic code for asthma before the end of
overall follow-up. Following an existing definition, individuals 40 years and over
with asthma were considered as likely to have COPD (and therefore not included
in the asthma study population [denominator]) if they had a subsequent COPD
diagnosis recorded within the two years following the current asthma record<sup>(#footnote1)</sup>.

<a name="footnote1">Bloom CI, Nissen F, Douglas IJ, Smeeth L, Cullinan P, Quint JK. Exacerbation risk and characterisation of
the UK’s asthma population from infants to old age. Thorax 2018; 73: 313–20.</a>

### Publications

<pre>
Kathryn E Mansfield, Rohini Mathur, John Tazare, Alasdair D Henderson, Amy Mulick, Helena Carreira, Anthony A Matthews, Patrick Bidulka, Alicia Gayle, Harriet Forbes, Sarah Cook, Angel YS Wong, Helen Strongman, Kevin Wing, Charlotte Warren-Gash, Sharon L Cadogan, Liam Smeeth, Joseph Hayes, Jennifer K Quint, Martin McKee, Sinéad M Langan, "COVID-19 collateral: Indirect acute effects of the pandemic on physical and mental health in the UK." medRxiv (2020).      
</pre>
