import os
import json

root_path = 'C://Users/hasee007/Desktop/GMCM/'                      # 根目录
data_root = os.path.join(root_path, 'database_canada_tempr_org')    # 数据根目录
result_path = os.path.join(root_path, 'result')                     # 结果目录
json_name = os.path.join(result_path, 'result.json')                # csv结果文件

data_name = ['Tm', 'Tx', 'Tn']
prov_list = ['NS', 'ON', 'QC', 'BC', 'MB', 'NB',
             'NL', 'PE', 'AB', 'SK', 'NT', 'YT', 'NU', 'XX']
month_list = [3, 6, 9, 12]
rcp_list = ['CO2', 'CH4', 'N2O', 'CF4', 'C2F6', 'C6F14', 'HFC23', 'SF6', 'CFC_11', 'CH3BR', 'CH3CL']
data_color = {'Tm': '#CBDEFA', 'Tx': '#FBE5D5', 'Tn': '#CCCCFF',
              'Tm_a': '#2B579A', 'Tx_a': 'orange', 'Tn_a': 'purple'}
is_debug = False


def get_prov_list(data):
    prov_list = []
    for _, value in data.items():
        # print('Key: {}, Value: {}'.format(key, value))
        for prov, _ in value.items():
            if prov not in prov_list:
                prov_list.append(prov)
    print(prov_list)
    return prov_list
