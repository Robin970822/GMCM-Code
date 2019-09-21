# coding:utf-8
from matplotlib import pyplot as plt
from tqdm import tqdm

import pandas as pd
import numpy as np
import json
import os

import config

result_path = config.result_path
data_name = config.data_name
data_color = config.data_color
prov_list = config.prov_list
month_list = config.month_list
month_dict = {3: 'Mar.', 6: 'Jun.', 9: 'Sep.', 12: 'Dec.'}

is_debug = False


def slide_window_ave(data, window, stride=1):
    length = len(data)
    out_length = int((length - window + 1) / stride)
    out = []
    for i in range(out_length):
        left = i + (i - 1) * (stride - 1)
        right = left + window
        # print(left, right)
        out.append(np.sum(data[left: right]) / window)
    return out


def show_month_raw_data(data, prov, month):
    year = np.array(data['Year'])
    plt.figure(figsize=(16, 9))
    for name in data_name:
        array = np.array(data[name])
        plt.scatter(year, array, label=name, color=data_color[name])
        ave_array = slide_window_ave(array, window=5)
        # print(len(ave_array), len(year), len(year[-len(ave_array)-1:-1]))
        plt.plot(year[-len(ave_array)-1:-1], ave_array, label='{} 5-year Average'.format(
            name), color=data_color['{}_a'.format(name)], linewidth=3)
    title = 'The Trend of Temperature in {} in {}'.format(
        month_dict[month], prov)
    plt.title(title, fontsize=24)
    plt.legend(loc='best', fontsize=16)
    plt.grid()
    plt.xlabel('Year', fontsize=24)
    plt.ylabel('Temperatue($^\circ C$)', fontsize=24)
    fig_name = '{}_{}.png'.format(prov, month)
    plt.savefig(os.path.join(result_path, fig_name))


def save_statics_data(data, prov, month):
    statics_dict = {}
    for name in data_name:
        array = np.array(data[name])
        mean = np.mean(array[~np.isnan(array)])
        std = np.std(array[~np.isnan(array)])
        statics_dict.update({name: [mean, std]})
    df = pd.DataFrame(statics_dict, index=['mean', 'std'])
    prov_path = os.path.join(result_path, '{}_{}.csv'.format(prov, month))
    df.to_csv(prov_path, header=True, index=True)
    return statics_dict


# main
statics_dict = {}
for prov in tqdm(prov_list, desc='ProvData'):
    prov_dict = {}
    csv_path = os.path.join(result_path, '{}.csv'.format(prov))
    data = pd.read_csv(csv_path)
    # print(data)
    for month in month_list:
        month_data = data[data['Month'] == month]
        # print('month {} \n: {}'.format(month, month_data))
        # show_month_raw_data(month_data, prov, month)
        statics_data = save_statics_data(month_data, prov, month)
        prov_dict.update({month: statics_data})
        if is_debug:
            break
    statics_dict.update({prov: prov_dict})
    if is_debug:
        break

statics_path = os.path.join(result_path, 'statics.json')
with open(statics_path, 'w') as jobj:
    json.dump(statics_dict, jobj)
