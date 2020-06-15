---
layout: page
title: Lifestyle Risk Factors
---

{% assign lifestyle_phenotypes = site.phenotypes | where: "type", "Lifestyle Risk Factor" %}
| Phenotype | Data Sources | 
|-----------|--------------|{% for phenotype in lifestyle_phenotypes %}
| [{{ phenotype.name }}]({{ phenotype.url }}) | {{ phenotype.data_sources | join: ", "}} |{% endfor %}
