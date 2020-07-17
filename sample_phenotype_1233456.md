---
layout: phenotype
title: Example disease
name: Example disease
phenotype_id: 123456 
type: Disease or Syndrome
group: Respiratory
data_sources: 
    - Datasource 1
    - Datasource 2
    - Datasource 3
clinical_terminologies: 
    - Terminology 1
    - Terminology 2
    - Terminology 3
validation:
    - prognostic
codelists:
    - doe_example_123456_term1.csv
    - doe_example_123456_term2.csv
    - doe_example_123456_term3.csv
valid_event_data_range: 01/01/2001 - 31/12/2019
sex: 
    - Female
    - Male
author: 
    - Jane Doe
publications: 
    - Doe J. et al. Example phenotype. PLOS ONE. 2020
status: BETA
date: 2019-06-20
modified_date: 2019-06-20
version: 1
---

### Data source 1
{% include csv.html csvdata=site.data.codelists.doe_example_123456_term1 %}

### Data source 2 
{% include csv.html csvdata=site.data.codelists.doe_example_123456_term2 %}

### Data source 3
{% include csv.html csvdata=site.data.codelists.doe_example_123456_term3 %}

### Implementation

Cupcake ipsum dolor. Sit amet powder. Biscuit apple pie marshmallow jelly gummi bears. Candy canes cotton candy jujubes. Jelly-o jelly beans sesame snaps. Ice cream pudding pudding halvah sugar plum. Marshmallow cheesecake gingerbread pie gingerbread gummi bears. Gummi bears cotton candy tiramisu caramels jelly oat cake caramels ice cream.

### Evaluation

Cupcake ipsum dolor. Sit amet powder. Biscuit apple pie marshmallow jelly gummi bears. Candy canes cotton candy jujubes. Jelly-o jelly beans sesame snaps. Ice cream pudding pudding halvah sugar plum. Marshmallow cheesecake gingerbread pie gingerbread gummi bears. Gummi bears cotton candy tiramisu caramels jelly oat cake caramels ice cream.
