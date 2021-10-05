---
layout: phenotype
title: Cancer
phenotype_id: U2ah4LMd6wZK8itYxz4UKg
name: Cancer
type: Disease or Syndrome
group: Cancers
sources: 
    - clinicalcodes
data_sources:
    - Clinical Practice Research Datalink GOLD
clinical_terminologies:
    - Read Version 2
validation:
codelists: Reeves_Cancer_U2ah4LMd6wZK8itYxz4UKg_Read2.csv
valid_event_data_range: 01/01/1996 - 17/12/20003 
sex:
    - Female
    - Male
author:
    - David Reeves
    - David A Springate
    - Darren M Ashcroft
    - Ronan Ryan
    - Tim Doran
    - Richard Morris
    - Ivan Olier
    - Evangelos Kontopantelis
publications:
    - David Reeves, David A Springate, Darren M Ashcroft, Ronan Ryan, Tim Doran, Richard Morris, Ivan Olier, Evangelos Kontopantelis, Can analyses of electronic patient records be independently and externally validated? The effect of statins on the mortality of patients with ischaemic heart disease: a cohort study with nested case–control analysis. BMJ Open, 4:e004952 2014.
status: FINAL
date: 2014-04-23
modified_date: 2014-04-23
version: Revision 1
---

### Primary Care

{% include csv.html csvdata=site.data.codelists.Reeves_Cancer_U2ah4LMd6wZK8itYxz4UKg_Read2 %}

### Implementation

Data:
CPRD and THIN obtain their data from practices using the Vision electronic record system, while QResearch obtains data from practices using EMIS software. We felt that comparisons would be most informative between databases drawing data from different capture systems. Across the time-period studied, two versions of EMIS were in use, the more common being the text-based EMIS LV system with navigation and data entry mainly via the keyboard; EMIS PCS, which is Windows-based with mouse control and drop-down menus, was introduced from 1999. Vision was Windows-based throughout the study period. A small-scale direct comparison of EMIS LV and Vision indicated that coded data entry, excepting prescribing information, was faster with Vision and that more items were likely to be coded. Practices running Vision have slightly higher achievement rates for most Quality and Outcomes Framework (QOF) indicators than practices running either version of EMIS, even after controlling for differences in practice and area characteristics. We had access to CPRD, and therefore chose to replicate a study previously conducted using QResearch. CPRD and QResearch both draw data from general practices spread throughout the UK—currently more than 600 practices each—and comparisons to the national age-gender structure and prevalence rates for common conditions mostly show good correspondence for both datasets. For practical reasons, we focused on studies of the effectiveness of medicinal interventions and, after assessing the available studies, chose to replicate an investigation into the effects of statins on the mortality of patients with ischaemic heart disease (IHD) by Hippisley-Cox and Coupland (H-C&C). The methodological details provided in the published paper were insufficient on their own to allow a close replication to be conducted, and we therefore obtained additional details from the authors. We requested purely factual information about the methods used and did not share any of our analyses or results. We replicated the methods of H-C&C as closely as possible, given the differences between the two databases. All of the methods described below, including the study period, variable specifications and analytical procedures, are exact replications of those used in the original study, unless indicated otherwise. We selected all practices in CPRD that provided up to standard (UTS) data (UTS is CPRD’s designation for data meeting their internal quality standards) for the whole of the period from 1 January 1996 to 17 December 2003. We next identified all patients with a first diagnosis of IHD within this period, based on the QOF business rules for 2004. We excluded patients whose IHD diagnosis fell within the first 3 months of registration with their general practice or was on or subsequent to their recorded date of death, or who were prescribed statins prior to first diagnosis. We extracted data for these patients from the date of IHD diagnosis up until 17 December 2003, or until the date of death or exit from the practice, or the last recorded date for practices that stopped providing data before 17 December 2003, giving a maximum possible length of follow-up postdiagnosis of just under 8 years.

Analysis:
The main outcome was all-cause mortality, identified through a record of death in the CPRD. Following H-C&C, we conducted two main analyses: (1) a cohort analysis and (2) a case-control analysis nested within the full cohort. All analyses were conducted using R. Following H-C&C, statistical significance was assessed using p<0.01 (two tailed), but 95% CIs are reported in tables and figures. We made an a priori decision not to attempt to ‘improve’ on the analysis conducted by H-C&C, as our specific aim was to determine whether the same results and conclusions would emerge from using identical methods on a different underlying dataset targeting the same population.

Cohort analysis:
The cohort analysis used a Cox proportional hazards model to examine the effect of statin use on patient survival, with survival time determined by the time (in days) between the date of first diagnosis and date of death. Patients who transferred out of their practice before death or who were still alive at the end of the study period were treated as censored observations. Statin exposure was used as a time-varying covariate, with the period of exposure from the date of first prescription to when the statin was stopped (estimated as the date of last prescription plus 90 days; intervening breaks in the use of statins were ignored), or if not stopped until the end of the study period, date of death or date of transfer out of practice. Covariates adjusted for in the analysis were year of diagnosis, gender, comorbidities (diabetes, hypertension, myocardial infarction, congestive cardiac failure and cancer), and age (coded as 0–44, 45–54, 55–64, 65–74, 75–84, 85–94 or ≥95), smoking (ever smoked, never smoked, not recorded) and body mass index (BMI; coded as <25, 25–30, >30 kg/m2) all at the date of diagnosis. The presence of each comorbidity was indicated by a diagnosis in the patient record (using the 2004 QOF business rules) and coded as present/not present at the date of IHD diagnosis. If smoking status or BMI was not recorded within 4 years prior to diagnosis of IHD, we coded it as missing. The analysis was undertaken using the R survival analysis package accounting for the clustering of patients by practice and using the Huber-White robust estimate of SE. The proportional hazards assumption was checked graphically and with a test for proportional hazards. 

Nested case-control study:
The nested case-control analysis compared all patients from the cohort who died during the follow-up period (the cases) with a group of matched control patients (also with IHD) who did not die. For each case, we defined an ‘index date’ as the date of death. We then used an incidence density sampling procedure (as per the original study; personal correspondence) to randomly select four control patients for each case matched on gender, year of IHD diagnosis and age (coded in 5-year age-bands). General practice was not used as a matching variable. Controls were patients with IHD alive at the time their matched case died (including patients who themselves became cases at a later time-point). The incidence sampling procedure allowed the same patient to be selected as a control for more than one case, thus providing a full set of four controls for each case, while still producing unbiased estimates of risk. Statin exposure was based on the first and last prescription dates prior to the index date and coded into: (1) currently taking statins (last prescription was within 90 days of the index date); (2) previously took statins (last prescription more than 90 days prior to the index date) and (3) has never taken statins. We did this for all statins as a group and also separately for five different types of statin (atorvastatin, cerivastatin, fluvastatin, pravastatin and simvastatin). For ‘all statins’, the last prescription could be for a different statin type than the first; for individual statins, it had to be the same type. One further formulation, rosuvastatin, was in use that did not appear in the QResearch study. We included this in the ‘all statins’ group but did not analyse it individually as only 22 patients had received the statin. Analysis of the case-control study used conditional logistic regression accounting for the matching of cases with controls, to obtain ORs for the risk of death in relation to use of statins. We allowed for clustering by general practice and used a robust estimate of SE, in line with the cohort analysis. Covariates in the analysis were smoking status, BMI and comorbidities, specified as in the Cohort analysis but based on the index date rather than the date of diagnosis. Additional covariates in this analysis were the Townsend deprivation score for the practice postcode (in national quintiles; H-C&C used quintiles of patient-level Townsend scores) and use of β-blockers, aspirin, ACE inhibitors and calcium channel blockers, identified through the British National Formulary chapter codes in the patient record. Each medication was coded as either used or not used prior to the index date but after the date of IHD diagnosis. Interactions between use of statins and each of gender, age (less than 75 vs 75 and over) and diabetes were tested by adding interaction terms into the model.

### Publications

<pre>
David Reeves, David A Springate, Darren M Ashcroft, Ronan Ryan, Tim Doran, Richard Morris, Ivan Olier, Evangelos Kontopantelis, Can analyses of electronic patient records be independently and externally validated? The effect of statins on the mortality of patients with ischaemic heart disease: a cohort study with nested case–control analysis. BMJ Open, 4:e004952 2014.
</pre>
