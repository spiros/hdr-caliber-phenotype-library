---
layout: page
title: ClinicalCodes.org 
---

ClinicalCodes.org – An online clinical codes repository to improve validity and reproducibility of medical database research

## What is ClinicalCodes.org?

The ClinicalCodes repository aims to hold code lists for all published electronic medical record studies, irrespective of code type (e.g. Read, ICD9-10, SNOMED) and database (CPRD, QResearch, THIN etc.). ClinicalCodes.org is hosted at the <a href="http://www.population-health.manchester.ac.uk/">Institute of Population Health</a> (IPH) at the <a href="http://www.mhs.manchester.ac.uk/">University of Manchester Faculty of Medical and Human Sciences</a>.

It a collaborative project involving the following University of Manchester centres:
<ul>
<li><a href="http://www.population-health.manchester.ac.uk/primarycare" target="_blank">The Centre for Primary Care</a></li>
<li><a href="http://www.population-health.manchester.ac.uk/healthinformatics" target="_blank">The Centre for Health Informatics</a></li>
<li><a href="http://www.population-health.manchester.ac.uk/biostatistics" target="_blank">The Centre for Biostatistics</a></li>
<li><a href="http://www.pharmacy.manchester.ac.uk/cpds" target="_blank">The Centre for Pharmacoepidemiology and Drug Safety, Manchester Pharmacy School</a></li>
</ul>

Visit the [website](https://clinicalcodes.rss.mhs.man.ac.uk/) or read the [paper](http://www.plosone.org/article/info%3Adoi%2F10.1371%2Fjournal.pone.0099825) for more information.


## Citation and attribution.

All ClinicalCodes.org phenotypes, metadata and material deposited in the HDR Phenotype Library __remain the intellectual property__ of ClinicalCodes.org. 

If you use phenotypes from the ClinicalCodes.org collection in your research, please cite:
  <blockquote>
    <cite>
      Springate DA, Kontopantelis E, Ashcroft DM, Olier I, Parisi R, Chamapiwa E, Reeves D(2014) <em>ClinicalCodes: An online clinical codes repository to improve validity and reproducibility of research using electronic medical records</em> PLoS ONE DOI: 10.1371/journal.pone.0099825
    </cite>
  </blockquote>

## Phenotypes in collection

{% assign disease_phenotypes = site.phenotypes |where: "sources", "clinicalcodes" | sort: "name" %}

| Phenotype | Data Sources |
|-----------|--------------|{% for phenotype in disease_phenotypes %}
| [{{ phenotype.name }}]({{ phenotype.url }}) | {{ phenotype.data_sources | join: ", "}} {% endfor %}

