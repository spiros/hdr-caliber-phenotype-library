---
layout: page
title: BHF Data Science Centre
---

## What is the BHF Data Science Centre?

The BHF Data Science Centre is a partnership between Health Data Research UK (HDR UK) and the British Heart Foundation (BHF), and sits within HDR UK.

We work with a wide range of partners including patients, public, clinicians, researchers and NHS organisations to help them carry out research using health data into the causes, prevention and treatment of all diseases of the heart and circulation (such heart attacks, stroke and vascular dementia). We do this to ensure new advances in treatment and care for diseases of the heart and circulation get to the patient as quickly as possible.

Visit the [website](https://www.hdruk.ac.uk/helping-with-health-data/bhf-data-science-centre/) for more information.

## Phenotypes in collection

{% assign disease_phenotypes = site.phenotypes |where: "sources", "bhfcvdcoviduk" | sort: "name" %}

| Phenotype | Data Sources |
|-----------|--------------|{% for phenotype in disease_phenotypes %}
| [{{ phenotype.name }}]({{ phenotype.url }}) | {{ phenotype.data_sources | join: ", "}} {% endfor %}