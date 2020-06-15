---
layout: page
title: Disease or syndrome
---

{% assign disease_phenotypes = site.phenotypes | where: "type", "Disease or Syndrome" | sort: "name" %}

| Phenotype | Data Sources |
|-----------|--------------|{% for phenotype in disease_phenotypes %}
| [{{ phenotype.name }}]({{ phenotype.url }}) | {{ phenotype.data_sources | join: ", "}} {% endfor %}
