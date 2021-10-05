---
layout: phenotype
title: Ankylosing Spondylitis
phenotype_id: jeGDCzz6pKhMTgBmS9TDDm
name: Ankylosing Spondylitis
type: Disease or Syndrome
group: Musculoskeletal
sources: 
    - clinicalcodes
data_sources:
    - Clinical Practice Research Datalink GOLD
clinical_terminologies:
    - Read Version 2
validation:
codelists: Muller_AnkylosingSpondylitis_jeGDCzz6pKhMTgBmS9TDDm_Read2.csv
valid_event_data_range: 01/01/2010 - 31/12/2012
sex:
    - Female
    - Male
author:
    - Sara Muller
    - Samantha L Hider
    - Karim Raza
    - Rebecca J Stack
    - Richard A Hayward
    - Christian D Mallen      
publications:
    - Sara Muller, Samantha L Hider,Karim Raza, Rebecca J Stack, Richard A Hayward, Christian D Mallen, An algorithm to identify rheumatoid arthritis in primary care a Clinical Practice Research Datalink study. BMJ Open, 5(e009309), 2015.
status: FINAL
date: 2015-12-23
modified_date: 2015-12-23
version: Revision 1
---

### Primary Care

{% include csv.html csvdata=site.data.codelists.Muller_AnkylosingSpondylitis_jeGDCzz6pKhMTgBmS9TDDm_Read2 %}

### Implementation

The original algorithm consisted of two criteria. Individuals meeting at least one were considered to have RA. Criterion 1: ≥1 RA Read code and a disease modifying antirheumatic drug (DMARD) without an alternative indication. Criterion 2: ≥2 RA Read codes, with at least one ‘strong’ code and no alternative diagnoses. Lists of codes for consultations and prescriptions were obtained from the authors of the original algorithm where these were available, or compiled based on the original description and clinical knowledge. 4161 people with a first Read code for RA between 1 January 2010 and 31 December 2012 were selected from the Clinical Practice Research Datalink (CPRD, successor to the GPRD), and the criteria applied.

### Publications

<pre>
Sara Muller, Samantha L Hider,Karim Raza, Rebecca J Stack, Richard A Hayward, Christian D Mallen, An algorithm to identify rheumatoid arthritis in primary care a Clinical Practice Research Datalink study. BMJ Open, 5(e009309), 2015.
</pre>
