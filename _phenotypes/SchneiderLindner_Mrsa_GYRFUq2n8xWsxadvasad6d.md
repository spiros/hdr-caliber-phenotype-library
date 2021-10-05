---
layout: phenotype
title: Methicillin-resistant Staphylococcus Aureus (Mrsa)
phenotype_id: GYRFUq2n8xWsxadvasad6d
name: Methicillin-resistant Staphylococcus Aureus (Mrsa)
type: Disease or Syndrome
group: 
sources: 
    - clinicalcodes
data_sources:
    - Clinical Practice Research Datalink GOLD
clinical_terminologies:
    - Read Version 2
    - OXMIS
validation:
codelists: SchneiderLindner_Mrsa_GYRFUq2n8xWsxadvasad6d_OXMISRead.csv
valid_event_data_range: 01/01/1993 - 31/12/2007
sex:
    - Female
    - Male
author:
    - Verena Schneider-Lindner
    - Caroline Quach
    - James A Hanley
    - Samy Suissa       
publications:
    - Verena Schneider-Lindner, Caroline Quach, James A Hanley, Samy Suissa, Antibacterial Drugs and the Risk of Community-Associated Methicillin-Resistant Staphylococcus aureus in Children. Arch Pediatr Adolesc Med, 165(12), 2011.
status: FINAL
date: 2011-08-01
modified_date: 2011-08-01
version: Revision 1
---

### Primary Care

{% include csv.html csvdata=site.data.codelists.SchneiderLindner_Mrsa_GYRFUq2n8xWsxadvasad6d_OXMISRead %}

### Implementation

Design: 
Population-based case-control study in children 1 to 19 years of age.

Setting: 
Primary care, General Practice Research Database, United Kingdom, 1994-2007.

Participants: 
Cases were children who had MRSA diagnosed as outpatients, and controls were individually matched on age and practice, with the matched case’s diagnosis date as the index date for both.

Main Exposures: 
Antibacterial agents prescribed 180 to 30 days prior to the index date, excluding prescriptions 30 days before the index date to prevent protopathic bias.

Outcome Measures: 
Rate ratios (RRs) estimated from the odds ratios of exposure in cases compared with controls using conditional logistic regression, adjusted for comorbid conditions, other prescription drug use, and hospitalization.

Results: 
The rate of MRSA was 4.5 per 100 000 per year. Of 297 cases and 9357 controls, 52.5% and 13.6%, respectively, received antibacterial drug prescriptions during the 150-day exposure window. The adjusted RR with any antibacterial drug was 3.5 (95% confidence interval [CI], 2.6-4.8). The RRs increased with the number of prescriptions (2.2 [95% CI, 1.5-3.2], 3.3 [95% CI, 1.9-5.6], 11.0 [95% CI, 5.6-21.6], and 18.2 [95% CI, 9.4-35.4] for 1, 2, 3, and >=4 prescriptions, respectively). The RR was particularly elevated for quinolones at 14.8 (95% CI, 3.9- 55.8), with wide variation among antibacterial classes.

### Publications

<pre>
Verena Schneider-Lindner, Caroline Quach, James A Hanley, Samy Suissa, Antibacterial Drugs and the Risk of Community-Associated Methicillin-Resistant Staphylococcus aureus in Children. Arch Pediatr Adolesc Med, 165(12), 2011.
</pre>
