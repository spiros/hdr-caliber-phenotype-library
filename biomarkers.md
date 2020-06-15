---
layout: page
title: Biomarkers
---

{% assign biomarker_phenotypes = site.phenotypes | where: "type", "Biomarker" %}
| Phenotype | Data Sources |
|-----------|--------------|{% for phenotype in biomarker_phenotypes %}
| [{{ phenotype.name }}]({{ phenotype.url }}) | {{ phenotype.data_sources | join: ", "}} |{% endfor %}

