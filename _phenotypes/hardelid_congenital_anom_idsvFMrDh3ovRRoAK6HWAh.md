---
layout: phenotype
title: Congenital anomalies in children
name: Congenital anomalies in children
phenotype_id: idsvFMrDh3ovRRoAK6HWAh 
type: Disease or Syndrome
group: Perinatal
data_sources: 
    - Hospital Episode Statistics Admitted Patient Care
    - Civil Registration - Deaths
    - General Acute Inpatient and Day Case - Scottish Morbidity Record (SMR01)
    - Scottish Birth Record (SBR)
clinical_terminologies: 
    - ICD-10
validation: 
    - prognostic
codelists: 
    - hardelid_congenital_anom_eurocat_idsvFMrDh3ovRRoAK6HWAh_ICD10.csv
    - hardelid_congenital_anom_feudtner_idsvFMrDh3ovRRoAK6HWAh_ICD10.csv
    - hardelid_congenital_anom_idsvFMrDh3ovRRoAK6HWAh_ICD10.csv
valid_event_data_range: 01/01/2003 - 31/12/2014
sex: 
    - Female
    - Male
author: 
    - Zylbersztejn A
    - Verfürden M
    - Hardelid P
    - Gilbert R
    - Wijlaars L.    
publications: 
    - 'Zylbersztejn A*, Verfürden M*, Hardelid P, Gilbert R, Wijlaars L. Phenotyping congenital anomalies in administrative hospital records. Paediatr Perinat Epidemiol. 2019; 34: 21– 28. https://doi.org/10.1111/ppe.12627'
status: FINAL
date: 2020-02-01
modified_date: 2020-02-01
version: 1
---
### EUROCAT phenotype
This code list was developed by the EUROCAT network to classify unstandardized text in congenital anomaly registries for surveillance in Europe;

Details can be found here:

1. EUROCAT Guide 1.4 and Reference Documents (Last update version 28/12/2018). 2013. Available from: [https://eu-rd-platform.jrc.ec.europa.eu/sites/default/files/Full_Guide_1_4_version_28_DEC2018.pdf](https://eu-rd-platform.jrc.ec.europa.eu/sites/default/files/Full_Guide_1_4_version_28_DEC2018.pdf)

2. EUROCAT website: [https://eu-rd-platform.jrc.ec.europa.eu/eurocat](https://eu-rd-platform.jrc.ec.europa.eu/eurocat)


{% include csv.html csvdata=site.data.codelists.hardelid_congenital_anom_eurocat_idsvFMrDh3ovRRoAK6HWAh_ICD10 %}



### Hardelid phenotype

This code list was developed to identify children with chronic conditions (including congenital anomalies) admitted to hospitals in England. We used a subgroup of Hardelid codes from Chapter 17 of ICD-10 (“Congenital malformations, deformations and chromosomal abnormalities”, that is all codes starting with “Q”) to indicate congenital anomalies. 

Details can be found here:

1. Hardelid P, Dattani N, Gilbert R. Estimating the prevalence of chronic conditions in children who die in England, Scotland and Wales: a data linkage cohort study. BMJ Open. 2014 Jan;4(8):e005331. doi: [http://dx.doi.org/10.1136/bmjopen-2014-005331](http://dx.doi.org/10.1136/bmjopen-2014-005331)

2. Hardelid P, Dattani N, Davey J, Pribramska I, Gilbert R. Overview of child deaths in the four UK countries. London; 2013. Available from: [https://www.hqip.org.uk/resource/overview-of-child-deaths-in-the-four-uk-countries/#.Xc5x1fn7Q2w](https://www.hqip.org.uk/resource/overview-of-child-deaths-in-the-four-uk-countries/#.Xc5x1fn7Q2w)(accessed 15 November 2019)

{% include csv.html csvdata=site.data.codelists.hardelid_congenital_anom_idsvFMrDh3ovRRoAK6HWAh_ICD10 %}


### Feudtner phenotype

This code list was developed to indicate children with complex chronic conditions (including congenital anomalies) admitted to hospitals in the United States. Initially it was created using ICD version 9 and it was later updated to ICD-10. Again, we only used a subgroup of Feudtner codes from Chapter 17 of ICD-10. 

Details can be found here:

1. Feudtner C, Feinstein JA, Zhong W, Hall M, Dai D. Pediatric complex chronic conditions classification system version 2: Updated for ICD-10 and complex medical technology dependence and transplantation. BMC Pediatrics 2014;14 doi: [http://dx.doi.org/10.1186/1471-2431-14-199](http://dx.doi.org/10.1186/1471-2431-14-199)

2. additional resources: [https://feudtnerlab.research.chop.edu/ccc_version_2.php](https://feudtnerlab.research.chop.edu/ccc_version_2.php) (accessed 15 November 2019)


{% include csv.html csvdata=site.data.codelists.hardelid_congenital_anom_feudtner_idsvFMrDh3ovRRoAK6HWAh_ICD10 %}

### Implementation
We compared prevalence, and risk of prognostic outcomes (hospital readmission and death) according to each code list in England and Scotland. Feudtner code list identified the least prevalent but most severe congenital anomalies. The EUROCAT code list identified the largest and least severely affected group.

### Publications

1. Zylbersztejn A*, Verfürden M*, Hardelid P, Gilbert R, Wijlaars L. Phenotyping congenital anomalies in administrative hospital records. Paediatr Perinat Epidemiol. 2019; 34: 21– 28. [https://doi.org/10.1111/ppe.12627](https://doi.org/10.1111/ppe.12627)



