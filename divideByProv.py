import pandas as pd
import numpy as np
from tqdm import tqdm
import os
import json

import config

root_path = config.root_path
is_debug = config.is_debug
data_name = config.data_name

result_path = config.result_path
json_name = os.path.join(result_path, 'result.json')

prov_list = config.prov_list

# main
# data: {'year_month': {'prov': prov_data}}
with open(json_name, 'r') as jobj:
    data = json.load(jobj)

prov_dict = {}
for prov in prov_list:
    dic = {'Year':[], 'Month':[], 'Tm':[], 'Tx':[], 'Tn':[]}
    prov_dict.update({prov: dic})

for key, value in data.items():
    [year, month] = key.split('_')
    for prov, t in value.items():
        prov_dict[prov]['Year'].append(int(year))
        prov_dict[prov]['Month'].append(int(month))
        prov_dict[prov]['Tm'].append(t['Tm'])
        prov_dict[prov]['Tx'].append(t['Tx'])
        prov_dict[prov]['Tn'].append(t['Tn'])

for prov in prov_list:
    prov_path = os.path.join(result_path, '{}.csv'.format(prov))
    df = pd.DataFrame(prov_dict[prov])
    df.sort_values(['Year', 'Month'])
    df.to_csv(prov_path, header=True, index=False)
