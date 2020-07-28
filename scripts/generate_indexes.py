#!/usr/bin/env python
# usage: generate_indexes.py
__author__ = "Susheel Varma"
__copyright__ = "Copyright (c) 2019-2020 Susheel Varma All Rights Reserved."
__email__ = "susheel.varma@hdruk.ac.uk"
__license__ = "Apache 2"

import os
import markdown
import json
from slugify import slugify
from pprint import pprint

def get_phenotype_files(dir):
    phenotype_files = []
    for file in os.listdir(dir):
        if file.endswith(".md"):
            phenotype_files.append(os.path.join(dir, file))
    return phenotype_files

def get_data_sources():
    import yaml
    with open("_data/data_sources.yml", 'r', encoding="utf-8") as yml_file:
        yaml_text = yml_file.read()
        return yaml.safe_load(yaml_text)

def get_phenotype(file):
    filename = os.path.basename(file)
    url = "https://portal.caliberresearch.org/phenotypes/" + slugify(os.path.splitext(filename)[0])
    with open(file, 'r', encoding="utf-8") as md_file:
        text = md_file.read()
        md = markdown.Markdown(extensions=['meta', 'toc'])
        html = md.convert(text)
        
        meta = md.Meta
        toc = ["Metadata"]
        toc.extend([t['name'] for t in md.toc_tokens])
        data_sources = []
        for ds in meta['data_sources']:
            if ds != '':
                if ds.startswith("- "):
                    data_sources.append(ds.split("- ")[1])
                else:
                    data_sources.append(ds)
    return {
        'name': meta['name'][0],
        'type': meta['type'][0],
        'id': meta['phenotype_id'][0],
        'filename': filename,
        'url': url,
        'toc': toc,
        'data_sources': data_sources
    }

def get_phenotypes(dir="_phenotypes"):
    phenotypes =[]
    DATA_SOURCES = get_data_sources()
    files = get_phenotype_files(dir)
    for file in files:
        pt = get_phenotype(file)
        resolved_data_sources = []
        for ds in pt['data_sources']:
            if ds in DATA_SOURCES.keys():
                resolved_data_sources.append(DATA_SOURCES[ds])
            else:
                resolved_data_sources.append(ds)
        pt.pop('data_sources')
        pt['data_sources'] = resolved_data_sources
        phenotypes.append(pt)
    return phenotypes

def export_phenotype2datasets(phenotypes, filename="_data/phenotype2datasets.json"):
    phenotype2datasets = {}
    for p in phenotypes:
        name = p['name']
        if name not in phenotype2datasets.keys():
            phenotype2datasets[name] = []
        for ds in p['data_sources']:
            if type(ds) is dict:
                phenotype2datasets[name].append(ds)
    with open(filename, 'w') as json_file:
        json_file.write(json.dumps(phenotype2datasets, indent=2))

def export_dataset2phenotypes(phenotypes, filename="_data/dataset2phenotypes.json"):
    dataset2phenotypes = {}
    for p in phenotypes:
        for ds in p['data_sources']:
            if type(ds) is dict:
                if ds['id'] not in dataset2phenotypes.keys():
                    dataset2phenotypes[ds['id']] = []
                dataset2phenotypes[ds['id']].append({
                    'name': p['name'],
                    'id': p['id'],
                    'url': p['url']
                })
    with open(filename, 'w') as json_file:
        json_file.write(json.dumps(dataset2phenotypes, indent=2))

def main():
    phenotypes = get_phenotypes()
    export_phenotype2datasets(phenotypes)
    export_dataset2phenotypes(phenotypes)

if __name__ == "__main__":
    main()
