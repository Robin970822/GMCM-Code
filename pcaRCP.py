from matplotlib import pyplot as plt

import pandas as pd
import numpy as np
from tqdm import tqdm
import os
import json

import config

root_path = config.root_path
data_root = os.path.join(root_path, 'database_RCP_org')
rcp_list = config.rcp_list
is_debug = True


def normalization(data):
    _range = np.max(data) - np.min(data)
    return (data - np.min(data)) / _range


def standardization(data):
    mu = np.mean(data, axis=1)
    sigma = np.std(data, axis=1)
    return ((data.T - mu) / sigma).T


def pca(X):
    [_, n] = X.shape
    C = (np.matmul(X, X.T)) / n
    [lamda, v] = np.linalg.eig(C)
    pc = np.matmul(v.T, X)
    return lamda, v, pc, C


csv_name = 'RCP85_MIDYEAR_CONCENTRATIONS.csv'
csv_path = os.path.join(data_root, csv_name)

raw_data = pd.read_csv(csv_path, skiprows=37)
year_column = raw_data.columns[0]
data = raw_data[raw_data[year_column] <= 2018]
year = np.array(data[year_column])

rcp = []
for rcp_kind in rcp_list:
    rcp_data = np.array(data[rcp_kind])
    rcp.append(rcp_data)

rcp = np.array(rcp)

lamda, v, pc, C = pca(standardization(rcp))

plt.figure()
plt.plot(year, pc[0, :])
plt.grid()
plt.xlabel('Year/y', fontsize=18)
plt.yticks(fontsize=16)
plt.xticks(fontsize=16)
plt.show()

plt.imshow(C)
plt.colorbar()
plt.show()
