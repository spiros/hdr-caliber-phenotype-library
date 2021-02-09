---
layout: page
title: BHF CVD-COVID-UK
---

## What is CVD-COVID-UK?

The CVD-COVID-UK project, led by Professor Cathie Sudlow, Director of the BHF Data Science Centre, is one of the six National Flagship Projects approved by the NIHR-BHF Cardiovascular Partnership.

CVD-COVID-UK aims to understand the relationship between COVID-19 and cardiovascular diseases such as heart attack, heart failure, stroke, and blood clots in the lungs through analyses of de-identified, linked, nationally collated healthcare datasets across the four nations of the UK.

Visit the [website](https://www.hdruk.ac.uk/projects/cvd-covid-uk-project/) for more information.

## Phenotypes in collection

{% assign disease_phenotypes = site.phenotypes |where: "sources", "bhfcvdcoviduk" | sort: "name" %}

| Phenotype | Data Sources |
|-----------|--------------|{% for phenotype in disease_phenotypes %}
| [{{ phenotype.name }}]({{ phenotype.url }}) | {{ phenotype.data_sources | join: ", "}} {% endfor %}