---
layout: phenotype
title: Self Harm
phenotype_id: C5HLbqp2kSvtQwh3fnM3YP
name: Self Harm
type: Lifestyle Risk Factor
group: Self Harm
sources: 
    - clinicalcodes
data_sources:
    - Clinical Practice Research Datalink GOLD
clinical_terminologies:
    - Read Version 2
validation:
codelists: Carr_SelfHarm_C5HLbqp2kSvtQwh3fnM3YP_Read2.csv
valid_event_data_range: 
sex:
    - Female
    - Male
author:
    - Matthew J Carr
    - Darren M Ashcrof
    - Evangelos Kontopantelis
    - Yvonne Awenant
    - Jayne Cooper
    - Carolynn Chew-Graham
    - Nav Kapur
    - Roger T. Webb
publications:
    - Matthew J Carr, Darren M Ashcroft, Evangelos Kontopantelis, Yvone Awenant, Jayne Cooper, Carolynn Chew-Graham, Nav Kapur, Roger T Webb, The epidemiology of self-harm in a UK-wide primary care patient cohort, 2001–2013. Psychiatry, 16(53) 2016.
status: FINAL
date: 2016-02-29
modified_date: 2016-02-29
version: Revision 1
---

### Primary Care

{% include csv.html csvdata=site.data.codelists.Carr_SelfHarm_C5HLbqp2kSvtQwh3fnM3YP_Read2 %}

### Implementation

Description of the data source:
This study was conducted using routinely collected data from the CPRD, the world’s largest population-based, longitudinal, primary care database. This data source contains anonymised patient information entered by general practice staff. Most clinical data is coded using the Read code system and the database includes information on diagnoses, demographics, laboratory tests, medications, and referrals to other healthcare settings. Our study utilised information from 677 general practices, with 10,396,605 patients contributing data at some stage during years 2001–2013, inclusive. We restricted our analyses to patients identified to be of an acceptable quality for research, and registered with a general practice deemed to be ‘up to standard’ on continuity of provision and data completeness criteria. We utilised an ‘open’ cohort study design in that each patient’s time at risk commenced at a different time point, and some exited prior to the end of the study period due to migration, death, or cessation of their practice’s contribution to the CPRD. 

Case definition and clinical coding:
In the UK, the National Institute for Health and Clinical Excellence (NICE) guidelines (CG16) define self-harm as any act of “self-poisoning or self-injury, irrespective of the apparent purpose”. Using this broad conceptualisation, we developed a list of Read codes incorporating all cases across the spectrum from milder forms of nonsuicidal behaviour through to near-fatal suicide attempts. Initially we searched for all Read codes that included the following terms in their description: ‘deliberate’, ‘intentional’ or ‘self ’ (to identify episodes of self-harm/harming, selfinjury/ injurious behaviour, self-inflicted harm/injury, harm/injury to self, self-poisoning, deliberate overdose, intentional overdose) and ‘suicide attempt’, ‘attempted suicide’ or ‘parasuicide’ (to identify suicide attempts). These candidate codes were then subjected to rigorous clinical review by two expert clinicians within the research team (NK and JC), with any non-relevant codes omitted. Additional potentially relevant codes were identified using the hierarchical structure of the coding system. We excluded codes that referred only to thoughts of self-harm or suicidal ideation and alcohol related codes, unless intent to actively harm oneself was specified. 

Self-harm frequency measures:
Calculating a rate based on the total number of general practice consultations could be dominated unduly by frequent attenders. We therefore deployed a dual approach at the patient-level to investigate: (i) rates of new cases in the population (incidence); (ii) the proportion of patients affected annually (presentation rates). We restricted our study to this more recent time period to maximise data quality and the relevance of our findings. Patients were eligible for inclusion in a given year if they were aged 15–64 years and registered with a CPRD contributing practice at the start of the year. The rationale for imposing these age restrictions was that the determinants and implications of self-harm in children and older adults are quite distinct from those of the rest of the population, and therefore warrant separate investigation and consideration. Among older persons who harm themselves, specific mechanisms such as bereavement,loneliness and social isolation and physical illness, multi-morbidity and impairment play a predominant role; children aged below 15 years who harm themselves tend to have an unusually low suicidal intent, and this behaviour is associated with a relatively low long-term risk of suicide.

Incidence:
When calculating incidence rates, denominator estimates were restricted to patients registered at the start of the year with a practice that contributed data throughout the year. Patients with a history of self-harm were excluded. The numerators were estimated as the number of patients included in the denominator with a first recorded episode of self-harm during the year. We excluded patients who were no longer registered on the episode date. Annual presentation rates Denominator estimates were restricted to patients registered at the start of the year with a practice that contributed data throughout the year. No restriction was placed regarding prior episodes of self-harm. The numerators were estimated as the number included in the denominator, with one or more presentations of self-harm during the year, and still registered on the first of those presentations. Gender-specific estimates of incidence and annual presentation rates are presented throughout. We report stratified analyses by age (10-year bands), nation (England, Northern Ireland, Scotland, and Wales), and socio-economic deprivation quintiles from 1 (least) to 5 (most deprived).

Measurement of deprivation:
Deprivation quintiles were applied according to the postcode of the general practice of registration, and were derived using the Index of Multiple Deprivation (IMD) for 2010 in each of the four UK nations. The specification differs slightly for each nation, but throughout the UK the IMD is a measure of area-level deprivation constructed from domains including income, employment, health, education, barriers to services (including housing), crime, and general living environment. In England, Wales and Northern Ireland, the indices are derived for geographical areas designated as Lower-layer Super Output Areas (LSOA’s), which contain 1000–3000 people and are Census-derived. In Scotland, the small area concentrations are called datazones. The IMD provides a means of ranking and assessing whether an area is more/less deprived than others in the same nation.

Statistical analyses:
The focus of our investigation was comparison of selfharm risk between subgroups of the UK population. Firstly, we compared rates for male versus female patients. Secondly, we conducted gender-specific comparisons across age bands, nations, and deprivation quintiles. Crude rate comparisons could have been misleading if the populations being compared had differed significantly with respect to potential confounders. Therefore, to enhance comparability, all subgroup rates were directly standardised for age, geographical region, and deprivation quintile. We derived directly standardised rates by applying categoryspecific rates from each subgroup to the demographic distribution of the total CPRD population to produce group-specific rates that would have been observed if the subgroups all had the same distribution. Rates per 10,000 patients are reported as 3-year moving averages, centred on the middle year of each 3-year period. Variations between demographic subgroups were examined formally using Mantel-Haenszel risk ratios, stratified by study year. Chi-squared tests were applied to assess homogeneity of rates over time and logistic regression to test for temporal linear trends. Each test for trend involved fitting two regression models with time represented as a categorical variable in the first and as a continuous variable in the second. Linear trends were confirmed if a likelihood ratio test on the two models was non-significant but the effect of time was significant in the second model. Significance was assessed at an α level of 0.05 (two-sided). All of the analyses were conducted using Stata version 13.

### Publications

<pre>
Matthew J Carr, Darren M Ashcroft, Evangelos Kontopantelis, Yvone Awenant, Jayne Cooper, Carolynn Chew-Graham, Nav Kapur, Roger T Webb, The epidemiology of self-harm in a UK-wide primary care patient cohort, 2001–2013. Psychiatry, 16(53) 2016.
</pre>
