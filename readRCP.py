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

csv_name = 'RCP85_MIDYEAR_CONCENTRATIONS.csv'
csv_path = os.path.join(data_root, csv_name)

raw_data = pd.read_csv(csv_path, skiprows=37)
year_column = raw_data.columns[0]
data = raw_data[raw_data[year_column] <= 2018]
year = np.array(data[year_column])

plt.figure()
for rcp_kind in rcp_list:
    rcp_data = np.array(data[rcp_kind])
    plt.plot(year, rcp_data, label=rcp_kind)

plt.legend()
plt.grid()
plt.title('RCP8.5 Atmospheric Concentrations in 1765-2045', fontsize=24)
plt.ylabel('/$10^{-6}$ ppm', fontsize=18)
plt.xlabel('Year', fontsize=18)
plt.yticks(fontsize=16)
plt.xticks(fontsize=16)
plt.show()
