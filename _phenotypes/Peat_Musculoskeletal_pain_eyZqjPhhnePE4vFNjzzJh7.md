---
layout: phenotype
title: Musculoskeletal Pain/injury in Adults
name: Musculoskeletal Pain/injury in Adults
phenotype_id: eyZqjPhhnePE4vFNjzzJh7
type: Musculoskeletal
group: Musculoskeletal
data_sources: 
    - Clinical Practice Research Datalink AURUM
    - OpenSAFELY SNOMED CT 
clinical_terminologies: 
    - SNOMED-CT
validation:
    - prognostic
codelists:
    - Peat_eyZqjPhhnePE4vFNjzzJh7_Musculoskeletal_pain_Concept_ID.csv
    - Peat_eyZqjPhhnePE4vFNjzzJh7_Musculoskeletal_pain_Description_ID.csv
    - Peat_eyZqjPhhnePE4vFNjzzJh7_Musculoskeletal_pain_body_region_look_ups.csv
valid_event_data_range: 01/01/2016 - 31/05/2021
sex: 
    - Female
    - Male
author: 
    - Professor George Peat, Professor Kelvin Jordan, James Bailey, Doctor Claire Burton, Doctor Victoria Welsh, Simon Wathall, Professor Jonathan Hill, Doctor Emma Parry, Doctor Dahai Yu, Steff Garvin, Michael Longeran
publications: 
    - 
status: FINAL
date: 2021-11-05
modified_date: 2021-11-05
version: 1
---

### SNOMED_CT_CONCEPT_ID code list
{% include csv.html csvdata=site.data.codelists.Peat_eyZqjPhhnePE4vFNjzzJh7_Musculoskeletal_pain_Concept_ID.csv %}

### SNOMED_CT_DESCRIPTION_ID code list
{% include csv.html csvdata=site.data.codelists.Peat_eyZqjPhhnePE4vFNjzzJh7_Musculoskeletal_pain_Description_ID.csv %}

### BODY REGION LOOK UP
{% include csv.html csvdata=site.data.codelists.Peat_eyZqjPhhnePE4vFNjzzJh7_Musculoskeletal_pain_body_region_look_ups.csv %}

### Implementation

A list of SNOMED CT Concept IDs suitable for practical application in UK primary care data for identifying consultations and clinical events for musculoskeletal pain conditions and injuries in adults. 

### Evaluation

Identifying potentially relevant MSK Concept IDs from existing studies (pathway 1)
Lists of musculoskeletal Read codes and/or SNOMED CT Concept and Description IDs developed in prior and current studies within the School of Medicine, Keele University were collated:
    - PRELIM: knee pain, hip pain, low back pain, shoulder pain, neck pain, hand/wrist pain, osteoarthritis 
    - TAPS: pain and osteoarthritis in the knee, shoulder, neck and back (lower & upper including trauma), and general/widespread pain
    - MSKCOM: low back pain, hand/wrist pain, hip pain, knee pain and osteoarthritis
    - SNIPE: all musculoskeletal disorders

Amalgamation of these code lists resulted in 13,200 provisional unique entities (combination of SNOMED CT Concept ID, Description ID, term). Any additional SNOMED CT description IDs and terms contained within the included Concept IDs were then added. This resulted in an additional 3,414 entities and an overall total of 16,614 entities.
KPJ (senior statistician and electronic health record researcher), GMP (senior epidemiologist), JH (academic physiotherapist), and EP (academic GP) then met to decide on general categories for inclusion and exclusion (Appendix A).

Selecting relevant MSK pain/injury Concept IDs by consensus
KPJ allocated the 16,614 entities to “provisionally include” (n=6,838), “provisionally exclude” (n=9,400), or “provisionally uncertain” (n=376) based on matching to the general categories for exclusion above. The “provisionally uncertain” list included all entities under a Concept ID where some of the entities within that Concept ID but not all would fit under “provisionally include”. The rationale here was that final selection would be at the Concept ID level and all entities (including all Description IDs) under an included Concept ID should be included. Similarly all entities under an excluded Concept ID would be excluded. GMP, JH, and EP then independently reviewed each of these three lists, with disagreements resolved in a consensus meeting. This resulted in 6,767 entities being taken forward. These 6,767 entities comprised 3,226 unique Concept IDs.

Independent search of OpenSafely Codelists (pathway 2)
An independent search of the OpenCodelists SAFELY portal within the OpenSAFELY platform was made by KPJ.  Phrases searched for within SNOMED CT terms were back, hand, hip, wrist, ankle, foot, spine, knee, shoulder, dislocation, spondylosis, meniscus, arthritis, bursitis, fracture, sprain, strain, subluxation, carpal, rotator, pain, widespread, arthralgia, arthropathy, coxalgia. This resulted in 8258 unique Concept IDs and included 2,454 (76%) of the 3,226 Concept IDs identified from the consensus exercise pathway 1. 5,804 additional Concept IDs were therefore potentially relevant and added to the 3,226 Concept IDs from pathway 1 (9,030 Concept IDs in total).
Reducing the number of Concept IDs for practical application
The number of Concept IDs remaining after pathway 1 and 2 was felt to be impractical to apply in practice, and was likely to include a large proportion of codes either describing very rare conditions or rarely used. Following permission from CPRD (on basis of no wider dissemination of detailed findings without further approval), a search was made of the number of recorded uses of each of the 9,030 Concept IDs in the Aurum database from January 2016 to July 2021. 3,762 (42%) Concept IDs had been used at least once during that time period, with 2,982 (79%) of these having been identified through pathway 1 and 780 from pathway 2. Concept IDs with an annual prevalence of 0.5 records per 10,000 registered population (all age) in any year 2016-2021 were retained. This resulted in 488 Concept IDs, which between them accounted for >97% of all events in each year recorded with one of the 3,762 Concept IDs. GMP, JH, and EP then did a final review reducing the list to 473 Concept IDs (466 from pathway 1 and 7 from pathway 2).

Finalising the Core Set
A final check of the Concept ID list by entering them into the SNOMED CT browser (termbrowser.nhs.uk) revealed 27 of these Concept IDs were inactive as at 30 Sep 2021. Therefore, added to the list were replacement(s) suggested within the SNOMED browser and/or Concept IDs with the same term if these were not already included. The final inclusion list contained 498 Concept IDs.

