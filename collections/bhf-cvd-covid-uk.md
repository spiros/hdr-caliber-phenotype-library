---
layout: page
title: British Heart Foundation (BHF) CVD-COVID-UK
---

## What is CVD-COVID-UK?

CVD-COVID-UK aims to understand the relationship between COVID-19 and cardiovascular diseases such as heart attack, heart failure, stroke, and blood clots in the lungs through analyses of de-identified, linked, nationally collated healthcare datasets across the four nations of the UK.

The CVD-COVID-UK project, led by Professor Cathie Sudlow, Director of the BHF Data Science Centre, is one of the six National Flagship Projects approved by the NIHR-BHF Cardiovascular Partnership.

#### Cardiovascular disease impact on susceptibility to and poor outcomes from COVID-19

Patients with cardiovascular disease are at increased risk of developing COVID-19 and of poor outcomes of COVID-19, such as admission to hospital or intensive care, or of dying. This could be due to cardiovascular conditions themselves (e.g., heart disease, stroke), their risk factors (e.g., age, raised blood pressure), medications, or combinations of these. Understanding which patients are affected and why will help in developing strategies to reduce this risk.

#### Impact of infection with coronavirus on patients with cardiovascular disease

The direct impacts include immediate complications (e.g., acute heart injury, stroke) and potentially increased risk of heart attack, stroke and other cardiovascular events in the longer term, through inflammation, blood clotting risk or other factors. However, the nature and extent of these direct effects are not well understood.

#### Impact of the COVID-19 pandemic on the treatment and care of cardiovascular disease patients

The response by the government and health services to the COVID-19 pandemic also has indirect impacts on the presentation, diagnosis, management and outcomes of cardiovascular diseases. The numbers of people attending hospital with heart attack and stroke declined dramatically in the lead up to and after the announcement of lockdown (as demonstrated by the 4C Initiative). Further, patients were more often arriving too late for beneficial acute treatments (e.g., clot busting drugs) and after potentially preventable complications had developed. To inform government and NHS policy, we urgently need a deeper understanding of these unintended consequences.

Visit the [website](https://www.hdruk.ac.uk/projects/cvd-covid-uk-project/) for more information.

## Phenotypes in collection

{% assign disease_phenotypes = site.phenotypes |where: "sources", "bhfcvdcoviduk" | sort: "name" %}

| Phenotype | Data Sources |
|-----------|--------------|{% for phenotype in disease_phenotypes %}
| [{{ phenotype.name }}]({{ phenotype.url }}) | {{ phenotype.data_sources | join: ", "}} {% endfor %}