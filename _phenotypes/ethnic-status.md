---
layout: phenotype
title: Ethnic Status
phenotype_id: PMD762GQ76BscDn5YK3Mwe
name: Ethnic Status
type: Lifestyle Risk Factor
group: Demographics
data_sources:
    - Clinical Practice Research Datalink GOLD
    - Hospital Episode Statistics Admitted Patient Care
validation: aetiology, prognosis
codelists:
    - caliber_ethnic_status_PMD762GQ76BscDn5YK3Mwe_Read2.csv
clinical_terminologies: 
    - Read Version 2
sex: 
    - Female
    - Male
author: Julie George, Rohini Mathur, Anoop Dinesh Shah, Mar Pujades-Rodriguez, Spiros Denaxas, Liam Smeeth, Adam Timmis, Harry Hemingway
status: DRAFT
date: 2012-11-23
modified_date: 2012-11-23
version: Revision 2
---

### Primary Care

{% include csv.html csvdata=site.data.codelists.caliber_ethnic_status_PMD762GQ76BscDn5YK3Mwe_Read2 %}

### Secondary Care

<div id="secondarycare" class="tab-pane active">
                  
Ethnicity information was recorded in the HES <i>patient</i> table which uses the <a href="https://www.datadictionary.nhs.uk/data_dictionary/attributes/e/end/ethnic_category_code_de.asp?shownav=0">2001 census categorization</a>. 

<br>

<pre>White
A	British
B	Irish
C	Any other White background
 
Mixed
D	White and Black Caribbean
E	White and Black African
F	White and Asian
G	Any other mixed background
 
Asian or Asian British
H	Indian
J	Pakistani
K	Bangladeshi
L	Any other Asian background
 
Black or Black British
M	Caribbean
N	African
P	Any other Black background
 
Other Ethnic Groups
R	Chinese
S	Any other ethnic group
 
Z	Not stated
</pre>
           </div>

### Implementation

<div id="implementation" class="tab-pane active">
                  

Patients were categorised as White, South Asian, Black, or Other/Mixed ethnic groups; these groups reflect the most prevalent ethnic groups in the 2011 Census in England and Wales. The White group included White British, White European and other White Groups. South Asian included patients from Indian, Pakistani, Bangladeshi and other Asian ethnic groups, including Asian British. Black included those belonging to African, Caribbean or other Black groups, including Black British. The Other/ Mixed group included those from any mixed ethnic group and other small minority ethnic groups, including Japanese and Chinese.

<figure>
    <img src="/assets/img/ethnicity_flowchart.png" alt="CALIBER Ethnicity Phenotype flowchart" class="center">
    <figcaption>Flow chart diagram illustrating the CALIBER phenotype algorithm for ethnicity </figcaption>
</figure>



            </div>


### Publications

<div id="publications" class="tab-pane active">
                  
<pre>Gho JMIH et al. An electronic health records cohort study on heart failure following myocardial infarction in England: incidence and predictors. BMJ Open. 2018 Mar 3;8(3):e018331. doi: 10.1136/bmjopen-2017-018331. PMID: <a href="https://www.ncbi.nlm.nih.gov/pubmed/29502083">29502083</a>


Steele AJ et al. Machine learning models in electronic health records can outperform conventional survival models for predicting patient mortality in coronary artery disease. PLoS One. 2018 Aug 31;13(8):e0202344. doi: 10.1371/journal.pone.0202344. eCollection 2018. PMID: <a href="https://www.ncbi.nlm.nih.gov/pubmed/30169498">30169498</a>


Archangelidi O et al. Clinically recorded heart rate and incidence of 12 coronary, cardiac, cerebrovascular and peripheral arterial diseases in 233,970 men and women: A linked electronic health record study. Eur J Prev Cardiol. 2018 Sep;25(14):1485-1495. doi: 10.1177/2047487318785228. Epub 2018 Jul 2. PMID: <a href="https://www.ncbi.nlm.nih.gov/pubmed/29966429">29966429</a>


Koudstaal S et al. Prognostic burden of heart failure recorded in primary care, acute hospital admissions, or both: a population-based linked electronic health record cohort study in 2.1 million people. Eur J Heart Fail. 2017 Sep;19(9):1119-1127. doi: 10.1002/ejhf.709. Epub 2016 Dec 23. PMID: <a href="https://www.ncbi.nlm.nih.gov/pubmed/28008698">28008698</a>


Chung SC et al. Time spent at blood pressure target and the risk of death and cardiovascular diseases. PLoS One. 2018 Sep 5;13(9):e0202359. doi: 10.1371/journal.pone.0202359. eCollection 2018. PMID: <a href="https://www.ncbi.nlm.nih.gov/pubmed/30183734">30183734</a>


Bell S et al. Association between clinically recorded alcohol consumption and initial presentation of 12 cardiovascular diseases: population based cohort study using linked health records. BMJ. 2017 Mar 22;356:j909. PMID: <a href="https://www.ncbi.nlm.nih.gov/pubmed/28331015">28331015</a>


Pasea L et al. Personalising the decision for prolonged dual antiplatelet therapy: development, validation and potential impact of prognostic models for cardiovascular events and bleeding in myocardial infarction survivors. Eur Heart J. 2017 Apr 7;38(14):1048-1055. doi: 10.1093/eurheartj/ehw683. PMID: <a href="https://www.ncbi.nlm.nih.gov/pubmed/28329300">28329300</a>


Shah AD et al. Neutrophil Counts and Initial Presentation of 12 Cardiovascular Diseases: A CALIBER Cohort Study. J Am Coll Cardiol. 2017 Mar 7;69(9):1160-1169. doi: 10.1016/j.jacc.2016.12.022. PMID: <a href="https://www.ncbi.nlm.nih.gov/pubmed/28254179">28254179</a>


Asaria M et al. Using electronic health records to predict costs and outcomes in stable coronary artery disease. Heart. 2016 May 15;102(10):755-62. doi: 10.1136/heartjnl-2015-308850. Epub 2016 Feb 10. PMID: <a href="https://www.ncbi.nlm.nih.gov/pubmed/26864674">26864674</a>


Daskalopoulou M et al. Depression as a Risk Factor for the Initial Presentation of Twelve Cardiac, Cerebrovascular, and Peripheral Arterial Diseases: Data Linkage Study of 1.9 Million Women and Men. PLoS One. 2016 Apr 22;11(4):e0153838. doi: 10.1371/journal.pone.0153838. eCollection 2016. PMID: <a href="https://www.ncbi.nlm.nih.gov/pubmed/27105076">27105076</a>


Pujades-Rodriguez M et al. Associations between polymyalgia rheumatica and giant cell arteritis and 12 cardiovascular diseases. Heart. 2016 Mar;102(5):383-9. doi: 10.1136/heartjnl-2015-308514. Epub 2016 Jan 19. PMID: <a href="https://www.ncbi.nlm.nih.gov/pubmed/26786818">26786818</a>


Pujades-Rodriguez M et al. Rheumatoid Arthritis and Incidence of Twelve Initial Presentations of Cardiovascular Disease: A Population Record-Linkage Cohort Study in England. PLoS One. 2016 Mar 15;11(3):e0151245. doi: 10.1371/journal.pone.0151245. eCollection 2016. PMID: <a href="https://www.ncbi.nlm.nih.gov/pubmed/26978266">26978266</a>


Shah AD et al. Low eosinophil and low lymphocyte counts and the incidence of 12 cardiovascular diseases: a CALIBER cohort study. Open Heart. 2016 Sep 5;3(2):e000477. doi: 10.1136/openhrt-2016-000477. eCollection 2016. PMID: <a href="https://www.ncbi.nlm.nih.gov/pubmed/27621833">27621833</a>


Timmis A et al. Prolonged dual antiplatelet therapy in stable coronary disease: comparative observational study of benefits and harms in unselected versus trial populations. BMJ. 2016 Jun 22;353:i3163. PMID: <a href="https://www.ncbi.nlm.nih.gov/pubmed/27334486">27334486</a>


Walker S et al. Long-term healthcare use and costs in patients with stable coronary artery disease: a population-based cohort using linked health records (CALIBER). Eur Heart J Qual Care Clin Outcomes. 2016 Jan 20;2(2):125-140. doi: 10.1093/ehjqcco/qcw003. PMID: <a href="https://www.ncbi.nlm.nih.gov/pubmed/27042338">27042338</a>


George J et al. How Does Cardiovascular Disease First Present in Women and Men? Incidence of 12 Cardiovascular Diseases in a Contemporary Cohort of 1,937,360 People. Circulation. 2015 Oct 6;132(14):1320-8. doi: 10.1161/CIRCULATIONAHA.114.013797. Epub 2015 Sep 1. PMID: <a href="https://www.ncbi.nlm.nih.gov/pubmed/26330414">26330414</a>


Morley KI et al. Defining disease phenotypes using national linked electronic health records: a case study of atrial fibrillation. PLoS One. 2014 Nov 4;9(11):e110900. doi: 10.1371/journal.pone.0110900. eCollection 2014. PMID: <a href="https://www.ncbi.nlm.nih.gov/pubmed/25369203">25369203</a>


Pujades-Rodriguez M et al. Heterogeneous associations between smoking and a wide range of initial presentations of cardiovascular disease in 1937360 people in England: lifetime risks and implications for risk prediction. Int J Epidemiol. 2015 Feb;44(1):129-41. doi: 10.1093/ije/dyu218. Epub 2014 Nov 20. PMID: <a href="https://www.ncbi.nlm.nih.gov/pubmed/25416721">25416721</a>


Pujades-Rodriguez M et al. Socioeconomic deprivation and the incidence of 12 cardiovascular diseases in 1.9 million women and men: implications for risk prediction and prevention. PLoS One. 2014 Aug 21;9(8):e104671. doi: 10.1371/journal.pone.0104671. eCollection 2014. PMID: <a href="https://www.ncbi.nlm.nih.gov/pubmed/25144739">25144739</a>


Rapsomaniki E et al. Blood pressure and incidence of twelve cardiovascular diseases: lifetime risks, healthy life-years lost, and age-specific associations in 1.25 million people. Lancet. 2014 May 31;383(9932):1899-911. doi: 10.1016/S0140-6736(14)60685-1. PMID: <a href="https://www.ncbi.nlm.nih.gov/pubmed/24881994">24881994</a>


Shah AD et al. Type 2 diabetes and incidence of cardiovascular diseases: a cohort study in 1.9 million people. Lancet Diabetes Endocrinol. 2015 Feb;3(2):105-13. doi: 10.1016/S2213-8587(14)70219-0. Epub 2014 Nov 11. PMID: <a href="https://www.ncbi.nlm.nih.gov/pubmed/25466521">25466521</a>


Rapsomaniki E et al. Prognostic models for stable coronary artery disease based on electronic health record cohort of 102 023 patients. Eur Heart J. 2014 Apr;35(13):844-52. doi: 10.1093/eurheartj/eht533. Epub 2013 Dec 17. PMID: <a href="https://www.ncbi.nlm.nih.gov/pubmed/24353280">24353280</a>
        
</pre>

            </div>
