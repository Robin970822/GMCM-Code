import pandas as pd
import numpy as np
from tqdm import tqdm
import os
import json

import config

data_root = config.data_root
root_path = config.root_path
is_debug = config.is_debug


def split_filename(filename):
    return filename.split('-')[-1].split('.')[0].split(',')


def get_prov_data(data):
    provs = np.unique(data['Prov'])
    result = {}
    for prov in provs:
        prov_data = data[(data['Prov'] == prov)]
        if is_debug:
            print('{}: \n {}'.format(prov, prov_data))
        prov_result = {}
        for dataName in config.data_name:
            ave = get_ave(prov_data, dataName)
            if is_debug:
                print('{}: {}'.format(dataName, ave))
            prov_result.update({dataName: ave})
        result.update({prov: prov_result})
    return result


def get_ave(data, dataName):
    sum = 0
    cnt = 0
    for index in range(len(data)):
        row_data = data.iloc[index][dataName]
        if not np.isnan(row_data):
            sum += row_data
            cnt += 1
    return sum / cnt if not cnt == 0 else np.nan


# main
result_path = config.result_path
if not os.path.exists(result_path):
    os.mkdir(result_path)

json_name = os.path.join(result_path, 'result.json')

filenames = []
for root, dirs, files in os.walk(data_root):
    for name in files:
        filenames.append(os.path.join(root, name))

all_result = {}
for filename in tqdm(filenames, desc='Read CSV'):
    [month, year] = split_filename(filename)
    print('Solving {} {}'.format(year, month))
    data = pd.read_csv(filename, skiprows=30)
    result = get_prov_data(data)
    if is_debug:
        print('Result for {}-{}:{}'.format(year, month, result))
        break
    json_split_name = os.path.join(
        result_path, '{}_{}.json'.format(year, month))
    with open(json_split_name, 'w') as jobj:
        json.dump(result, jobj)
    all_result.update({'{}_{}'.format(year, month): result})

with open(json_name, 'w') as jobj:
    json.dump(all_result, jobj)
