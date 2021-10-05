---
layout: phenotype
title: Psoriasis
phenotype_id: ectjUHpFVQqpysp7Prscic
name: Psoriasis
type: Disease or Syndrome
group: Skin
sources: 
    - clinicalcodes
data_sources:
    - Clinical Practice Research Datalink GOLD
clinical_terminologies:
    - Read Version 2
validation:
codelists: Parisi_Psoriasis_ectjUHpFVQqpysp7Prscic_Read2.csv
valid_event_data_range: 01/01/1994 - 31/12/2009
sex:
    - Female
    - Male
author:
    - Rosa Parisi
    - Martin K Rutter
    - Mark Lunt
    - Helen S Young
    - Deborah PM Symmons
    - Christopher EM Griffiths
    - Darren M Ashcroft   
publications:
    - Rosa Parisi, Martin K Rutter, Mark Lunt, Helen S Young, Deborah PM Symmons, Christopher EM Griffiths, Darren M. Ashcroft, Psoriasis and the risk of myocardial infarction Cohort study using the clinical practive research datalink. 2014.
status: FINAL
date: 2014-12-31
modified_date: 2014-12-31
version: Revision 1
---


### Primary Care

{% include csv.html csvdata=site.data.codelists.Parisi_Psoriasis_ectjUHpFVQqpysp7Prscic_Read2 %}

### Implementation

Study population:
The study population included patients with a first diagnosis of psoriasis between January 1, 1994 and December 31, 2009, who were 20 years or older at the time of the diagnosis. A comparison group of up to 5 controls per psoriasis patient was selected. Patients from both cohorts did not have any history of CVD or diabetes before index date (first diagnosis of psoriasis) or corresponding consulting date and, in order to capture incident not prevalent cases of psoriasis or MI, all patients had to have at least 2 years prior registration within their general practice before entry into the study cohort. The control group consisted of patients who never received a diagnostic code for psoriasis. Controls were matched to psoriasis patients by age, gender, general practice and then by calendar time (date of first diagnosis of psoriasis). Person-time under observation for each patient was calculated from the corresponding index date up to end of the study which was the earliest date of the occurrence of the MI event, transfer out of the practice or death date, end of follow-up (December 31, 2011) or if the practice was no longer up to research data quality standards set by CPRD. 

Definition of exposure:
Patients with psoriasis were included if they had their first diagnostic code for psoriasis during January 1, 1994-December 31, 2009 and received a recognised treatment for psoriasis (emollients, topical treatment, phototherapy, systemic therapy or biologics (CG153 Psoriasis: NICE guideline) (Samarasekera and Smith, 2014)). Patients were classified as having severe psoriasis once they had received a systemic treatment (acitretin, etretinate, ciclosporin, hydroxycarbamide, methotrexate, fumaric acid), phototherapy or a biologic therapy (etanercept, adalimumab, infliximab, ustekinumab, efalizumab); alternatively they were classified as mild psoriasis.

Outcome of interest:
The outcome of interest was fatal and non-fatal incident MI events. In our main analysis, MI events were identified using Read codes in CPRD. In sensitivity analysis, we identified MI events recorded in both CPRD and national mortality records (ONS) for those patients registered in practices that provided linked data between CPRD and ONS.


### Publications

<pre>
Rosa Parisi, Martin K Rutter, Mark Lunt, Helen S Young, Deborah PM Symmons, Christopher EM Griffiths, Darren M. Ashcroft, Psoriasis and the risk of myocardial infarction Cohort study using the clinical practive research datalink. 2014.
</pre>