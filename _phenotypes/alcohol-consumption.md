---
layout: phenotype
title: Alcohol Consumption
phenotype_id: 7aXDiYMtSR6aYEkZKPBdvm
name: Alcohol Consumption
type: Lifestyle Risk Factor
group: Lifestyle Risk Factor
data_sources:
    - Clinical Practice Research Datalink GOLD
clinical_terminologies:
    - Read Version 2
validation: prognosis
codelists:
    - caliber_alcohol_consumption_7aXDiYMtSR6aYEkZKPBdvm_Read2.csv
    - caliber_alcohol_daily_intake_7aXDiYMtSR6aYEkZKPBdvm_Read2.csv
    - caliber_alcohol_harm_7aXDiYMtSR6aYEkZKPBdvm_Read2.csv
valid_event_data_range: 01/01/1999 - 01/07/2016
sex: Female/Male
author: Bell S, Daskalopoulou M, Rapsomaniki E, George J, Britton A, Bobak M, Casas JP, Dale CE, Denaxas S, Shah AD, Hemingway H
status: FINAL
date: 2012-11-23
modified_date: 2012-11-23
version: Revision 1
---

### Primary Care

In the Clinical Practice Research Datalink (CPRD, primary care data) we extracted information on alcohol consumption based on:

    - Clinician-recorded alcohol consumption information
    - Stuctured data elements related to daily/weekly alcohol unit consumption
    - Evidence of alcohol abuse
    - Evidence of alcohol-related harm

#### Alcohol consumption information

{% include csv.html csvdata=site.data.codelists.caliber_alcohol_consumption_7aXDiYMtSR6aYEkZKPBdvm_Read2 %}

####  Daily/weekly alcohol intake

We extracted alcohol unit intake information using the structured data part (entity type 5) of the <i>additional</i> table (units recorded in <i>data2</i>) field. We additionally extract information on intake through clinician-recorded classifications using Read terms (see below). 


{% include csv.html csvdata=site.data.codelists.caliber_alcohol_daily_intake_7aXDiYMtSR6aYEkZKPBdvm_Read2 %}

####  Alcohol abuse

{% include csv.html csvdata=site.data.codelists.caliber_alcohol_harm_7aXDiYMtSR6aYEkZKPBdvm_Read2 %}

### Implementation

<figure>
        <img src="/assets/img/alcohol_flowchart.png" alt="CALIBER Alcohol consumption Phenotype flowchart" 
            class="center">
        <figcaption>Flow chart diagram illustrating the CALIBER phenotype algorithm for alcohol consumption </figcaption>
    </figure>


The most recent alcohol consumption record in the
five years before entry into the study was used to classify participants drinking behaviour. In light of
current debates on the U/J-shaped relationship observed between alcohol consumption and aggregated
CVD outcomes10 five drinking categories were defined including: (1) non-drinkers (Read66 codes such
as "tee-total" and "non-drinkers"), former drinkers (those with codes for "stopped drinking alcohol"
and/or "ex-drinker"), occasional drinkers (those with codes for "drinks rarely" and/or "drinks
occasionally"), current moderate drinkers (those who had a code for current alcohol consumer and an
indicator of whether they drank within daily [32g or 24g of alcohol for men and women respectively]
and/or weekly [168g of alcohol for men and 112g for women] recommended sensible drinking limits
for the UK at the time of observation69) and current heavy drinkers (defined as those who exceeded
daily and/or weekly sensible drinking limits). We also utilised data fields with information entered on
daily and/or weekly amount of alcohol consumed to define participants as non-drinkers, moderate
drinkers (drank within daily and/or weekly guidelines) and heavy drinkers. Weekly alcohol data was
available as a continuous variable, so we were able to classify consumption using standard thresholds

Data on daily alcohol intake was entered using categories of: (1) < 1
UK unit (8 grams of ethanol), (2) 1-2 UK units, (3) 3-6 UK units, (4) 7-9 UK units, and (5) > 9 UK
units [Read codes 1362.00-1366.00], for which we defined moderate drinking as anything >1 UK
unit but less than 3 (women) or 7 (men) UK units. Unfortunately information on binge drinking was
only available for a select minority of the cohort (~100 people) therefore a separate category for this
drinking behaviour was not defined (but these patients were coded as heavy drinkers). We reclassified
non-drinkers as former drinkers if they had any record of drinking recorded in their entire clinical
record entered on CPRD prior to study entry (in cases whereby non-drinkers had no record of
drinking before entering the study we assumed that they were not former drinkers). This resulted in
19,853 (out of 184,747; 10.7%) non-drinkers being recoded as former drinkers, a further 6,826 (3.7%)
participants were reclassified through having a positive history of alcohol abuse. 

### Publications

<pre>
Gho JMIH et al. An electronic health records cohort study on heart failure following myocardial infarction in England: incidence and predictors. BMJ Open. 2018 Mar 3;8(3):e018331. doi: 10.1136/bmjopen-2017-018331. PMID: <a href='https://www.ncbi.nlm.nih.gov/pubmed/29502083'>29502083</a>


Steele AJ et al. Machine learning models in electronic health records can outperform conventional survival models for predicting patient mortality in coronary artery disease. PLoS One. 2018 Aug 31;13(8):e0202344. doi: 10.1371/journal.pone.0202344. eCollection 2018. PMID: <a href='https://www.ncbi.nlm.nih.gov/pubmed/30169498'>30169498</a>


Archangelidi O et al. Clinically recorded heart rate and incidence of 12 coronary, cardiac, cerebrovascular and peripheral arterial diseases in 233,970 men and women: A linked electronic health record study. Eur J Prev Cardiol. 2018 Sep;25(14):1485-1495. doi: 10.1177/2047487318785228. Epub 2018 Jul 2. PMID: <a href='https://www.ncbi.nlm.nih.gov/pubmed/29966429'>29966429</a>


Koudstaal S et al. Prognostic burden of heart failure recorded in primary care, acute hospital admissions, or both: a population-based linked electronic health record cohort study in 2.1 million people. Eur J Heart Fail. 2017 Sep;19(9):1119-1127. doi: 10.1002/ejhf.709. Epub 2016 Dec 23. PMID: <a href='https://www.ncbi.nlm.nih.gov/pubmed/28008698'>28008698</a>


Chung SC et al. Time spent at blood pressure target and the risk of death and cardiovascular diseases. PLoS One. 2018 Sep 5;13(9):e0202359. doi: 10.1371/journal.pone.0202359. eCollection 2018. PMID: <a href='https://www.ncbi.nlm.nih.gov/pubmed/30183734'>30183734</a>


Bell S et al. Association between clinically recorded alcohol consumption and initial presentation of 12 cardiovascular diseases: population based cohort study using linked health records. BMJ. 2017 Mar 22;356:j909. PMID: <a href='https://www.ncbi.nlm.nih.gov/pubmed/28331015'>28331015</a>


Pasea L et al. Personalising the decision for prolonged dual antiplatelet therapy: development, validation and potential impact of prognostic models for cardiovascular events and bleeding in myocardial infarction survivors. Eur Heart J. 2017 Apr 7;38(14):1048-1055. doi: 10.1093/eurheartj/ehw683. PMID: <a href='https://www.ncbi.nlm.nih.gov/pubmed/28329300'>28329300</a>


Shah AD et al. Neutrophil Counts and Initial Presentation of 12 Cardiovascular Diseases: A CALIBER Cohort Study. J Am Coll Cardiol. 2017 Mar 7;69(9):1160-1169. doi: 10.1016/j.jacc.2016.12.022. PMID: <a href='https://www.ncbi.nlm.nih.gov/pubmed/28254179'>28254179</a>


Asaria M et al. Using electronic health records to predict costs and outcomes in stable coronary artery disease. Heart. 2016 May 15;102(10):755-62. doi: 10.1136/heartjnl-2015-308850. Epub 2016 Feb 10. PMID: <a href='https://www.ncbi.nlm.nih.gov/pubmed/26864674'>26864674</a>


Daskalopoulou M et al. Depression as a Risk Factor for the Initial Presentation of Twelve Cardiac, Cerebrovascular, and Peripheral Arterial Diseases: Data Linkage Study of 1.9 Million Women and Men. PLoS One. 2016 Apr 22;11(4):e0153838. doi: 10.1371/journal.pone.0153838. eCollection 2016. PMID: <a href='https://www.ncbi.nlm.nih.gov/pubmed/27105076'>27105076</a>


Pujades-Rodriguez M et al. Associations between polymyalgia rheumatica and giant cell arteritis and 12 cardiovascular diseases. Heart. 2016 Mar;102(5):383-9. doi: 10.1136/heartjnl-2015-308514. Epub 2016 Jan 19. PMID: <a href='https://www.ncbi.nlm.nih.gov/pubmed/26786818'>26786818</a>


Pujades-Rodriguez M et al. Rheumatoid Arthritis and Incidence of Twelve Initial Presentations of Cardiovascular Disease: A Population Record-Linkage Cohort Study in England. PLoS One. 2016 Mar 15;11(3):e0151245. doi: 10.1371/journal.pone.0151245. eCollection 2016. PMID: <a href='https://www.ncbi.nlm.nih.gov/pubmed/26978266'>26978266</a>


Shah AD et al. Low eosinophil and low lymphocyte counts and the incidence of 12 cardiovascular diseases: a CALIBER cohort study. Open Heart. 2016 Sep 5;3(2):e000477. doi: 10.1136/openhrt-2016-000477. eCollection 2016. PMID: <a href='https://www.ncbi.nlm.nih.gov/pubmed/27621833'>27621833</a>


Timmis A et al. Prolonged dual antiplatelet therapy in stable coronary disease: comparative observational study of benefits and harms in unselected versus trial populations. BMJ. 2016 Jun 22;353:i3163. PMID: <a href='https://www.ncbi.nlm.nih.gov/pubmed/27334486'>27334486</a>


Walker S et al. Long-term healthcare use and costs in patients with stable coronary artery disease: a population-based cohort using linked health records (CALIBER). Eur Heart J Qual Care Clin Outcomes. 2016 Jan 20;2(2):125-140. doi: 10.1093/ehjqcco/qcw003. PMID: <a href='https://www.ncbi.nlm.nih.gov/pubmed/27042338'>27042338</a>


George J et al. How Does Cardiovascular Disease First Present in Women and Men? Incidence of 12 Cardiovascular Diseases in a Contemporary Cohort of 1,937,360 People. Circulation. 2015 Oct 6;132(14):1320-8. doi: 10.1161/CIRCULATIONAHA.114.013797. Epub 2015 Sep 1. PMID: <a href='https://www.ncbi.nlm.nih.gov/pubmed/26330414'>26330414</a>


Morley KI et al. Defining disease phenotypes using national linked electronic health records: a case study of atrial fibrillation. PLoS One. 2014 Nov 4;9(11):e110900. doi: 10.1371/journal.pone.0110900. eCollection 2014. PMID: <a href='https://www.ncbi.nlm.nih.gov/pubmed/25369203'>25369203</a>


Pujades-Rodriguez M et al. Heterogeneous associations between smoking and a wide range of initial presentations of cardiovascular disease in 1937360 people in England: lifetime risks and implications for risk prediction. Int J Epidemiol. 2015 Feb;44(1):129-41. doi: 10.1093/ije/dyu218. Epub 2014 Nov 20. PMID: <a href='https://www.ncbi.nlm.nih.gov/pubmed/25416721'>25416721</a>


Pujades-Rodriguez M et al. Socioeconomic deprivation and the incidence of 12 cardiovascular diseases in 1.9 million women and men: implications for risk prediction and prevention. PLoS One. 2014 Aug 21;9(8):e104671. doi: 10.1371/journal.pone.0104671. eCollection 2014. PMID: <a href='https://www.ncbi.nlm.nih.gov/pubmed/25144739'>25144739</a>


Rapsomaniki E et al. Blood pressure and incidence of twelve cardiovascular diseases: lifetime risks, healthy life-years lost, and age-specific associations in 1.25 million people. Lancet. 2014 May 31;383(9932):1899-911. doi: 10.1016/S0140-6736(14)60685-1. PMID: <a href='https://www.ncbi.nlm.nih.gov/pubmed/24881994'>24881994</a>


Shah AD et al. Type 2 diabetes and incidence of cardiovascular diseases: a cohort study in 1.9 million people. Lancet Diabetes Endocrinol. 2015 Feb;3(2):105-13. doi: 10.1016/S2213-8587(14)70219-0. Epub 2014 Nov 11. PMID: <a href='https://www.ncbi.nlm.nih.gov/pubmed/25466521'>25466521</a>


Rapsomaniki E et al. Prognostic models for stable coronary artery disease based on electronic health record cohort of 102 023 patients. Eur Heart J. 2014 Apr;35(13):844-52. doi: 10.1093/eurheartj/eht533. Epub 2013 Dec 17. PMID: <a href='https://www.ncbi.nlm.nih.gov/pubmed/24353280'>24353280</a>
        
</pre>

