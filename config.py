import os
import json

root_path = 'C://Users/hasee007/Desktop/GMCM/'                      # 根目录
data_root = os.path.join(root_path, 'database_canada_tempr_org')    # 数据根目录
result_path = os.path.join(root_path, 'result')                     # 结果目录
json_name = os.path.join(result_path, 'result.json')                # csv结果文件

data_name = ['Tm', 'Tx', 'Tn']
prov_list = ['NS', 'ON', 'QC', 'BC', 'MB', 'NB',
             'NL', 'PE', 'AB', 'SK', 'NT', 'YT', 'NU', 'XX']
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
