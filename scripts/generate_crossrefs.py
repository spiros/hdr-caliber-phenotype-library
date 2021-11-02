#!/usr/bin/env python
# usage: generate_crossrefs.py
__author__ = "Susheel Varma"
__copyright__ = "Copyright (c) 2021 Susheel Varma All Rights Reserved."
__email__ = "susheel.varma@hdruk.ac.uk"
__license__ = "Apache 2"

import copy
import json
from pprint import pprint
import requests

DATASETS_URL = "https://phenotypes.healthdatagateway.org/api/v1/data-sources/?format=json"
PHENOTYPES_URL = "https://phenotypes.healthdatagateway.org/api/v1/public/phenotypes/?format=json"
PHENOTYPE_LIB_URL = "https://phenotypes.healthdatagateway.org/phenotypes/{phenotype_id}/version/{version}/detail/#home"

DATA_SOURCE_FIXES = {
    3: {
        "id": 3,
        "name": "Civil Registration - Deaths",
        "pid": "050163dc-1728-4ac5-a7d9-4dd3ca0ca12a",
        "url": "https://web.www.healthdatagateway.org/dataset/050163dc-1728-4ac5-a7d9-4dd3ca0ca12a"
    },
    17: {
        "id": 17,
        "name": "General Acute Inpatient and Day Case - Scottish Morbidity Record (SMR01)",
        "pid": "98cda353-0011-45b2-80ca-4ed24cd084bf",
        "url": "https://web.www.healthdatagateway.org/dataset/98cda353-0011-45b2-80ca-4ed24cd084bf"
    },
    19: {
        "id": 19,
        "name": "Death Registration Data - Provisional Monthly Extracts",
        "pid": "487222b7-5c13-4a92-8b41-044796048720",
        "url": "https://web.www.healthdatagateway.org/dataset/487222b7-5c13-4a92-8b41-044796048720"
    },
    21: {
        "id": 21,
        "name": "Hospitalised patients with diabetic emergencies & acute diabetic health concerns",
        "pid": "0d556d7e-be27-4979-a09e-d419b2e838f3",
        "url": "https://web.www.healthdatagateway.org/dataset/0d556d7e-be27-4979-a09e-d419b2e838f3"
    },
    22: {
        "id": 22,
        "name": "Hospitalised patients with diabetic emergencies & acute diabetic health concerns",
        "pid": "0d556d7e-be27-4979-a09e-d419b2e838f3",
        "url": "https://web.www.healthdatagateway.org/dataset/0d556d7e-be27-4979-a09e-d419b2e838f3"
    }
}

def request_url(URL):
    """HTTP GET request and load into json"""
    print(URL)
    r = requests.get(URL)
    if r.status_code != requests.codes.ok:
        r.raise_for_status()
    return json.loads(r.text)

def write_json(data, filename=None, indent=2):
   with (open(filename, 'w') if filename else sys.stdout) as file:
        json.dump(data, file, indent=indent)

def get_datasets():
    DATASETS = {}
    datasets = request_url(DATASETS_URL)
    for d in datasets:
        dataset = {
            'id': d['id'],
            'name': d['name'],
            'pid': d['uid'],
            'url': d['url'],
        }
        if d['uid'] != "":
            DATASETS[d['id']] = dataset
    
    DATASETS.update(DATA_SOURCE_FIXES)
    return DATASETS

def get_phenotypes(datasets):
    PHENOTYPES = []
    phenotypes = request_url(PHENOTYPES_URL)
    for p in phenotypes:
        if len(p['data_sources']):
            phenotype = {
                "id": p['phenotype_id'],
                "name": p['phenotype_name'],
                "type": p['type'],
            }
            latest_version = [v['version_id'] for v in p['versions'] if v['is_latest'] == True]
            if len(latest_version):
                phenotype['url'] = PHENOTYPE_LIB_URL.format(phenotype_id=p['phenotype_id'], version=latest_version[0])
            
            data_sources = [datasets[ds['id']] for ds in p['data_sources'] if ds['id'] in datasets.keys()]
            phenotype['datasets'] = data_sources
            
            PHENOTYPES.append(phenotype)
    return PHENOTYPES

def datasets2phenotypes(phenotypes):
    DATASETS = {}
    for p in phenotypes:
        temp = copy.deepcopy(p)
        del temp['datasets']
        for d in p['datasets']:
            DATASETS.setdefault(d['pid'], [])
            DATASETS[d['pid']].append(temp)
    return DATASETS


def main():
    datasets = get_datasets()
    phenotypes = get_phenotypes(datasets)
    d2p = datasets2phenotypes(phenotypes)
    write_json(d2p, "_data/dataset2phenotypes.json")


if __name__ == '__main__':
    main()
