import requests
import json
import time

import requests
import json
import time

Data = {}


def Data_update():
    get_cr = requests.get('https://api.exmo.com/v1/ticker/')
    cr_list = json.loads(get_cr.text)

    for pair in cr_list:
        name = pair.replace('_', ' ').split()
        Data.update({name[0]: {}})
        Data.update({name[1]: {}})

    for pair in cr_list:
        name = pair.replace('_', ' ').split()
        sell = float(cr_list[pair]['sell_price'])
        buy = float(cr_list[pair]['buy_price'])
        # sell red это мы покупаем 1 ETH
        # buy green это мы продаём 1 ETH
        Data[name[0]].update({name[1]: buy})
        Data[name[1]].update({name[0]: 1 / sell})


Data_update()
print(Data)
i = 0
for one_name in Data:
    for two_name in Data[one_name]:
        for tree_name in Data[two_name]:
            for four_nema in Data[tree_name]:
                if four_nema == one_name:
                    sum_start = 1
                    tr_1 = Data[one_name][two_name] * sum_start
                    tr_2 = Data[two_name][tree_name] * tr_1
                    sum_end = Data[tree_name][four_nema] * tr_2
                    pro = 0
                    if (sum_end > 1):
                        pro = (sum_end - sum_start) * 100 / sum_end
                        print(one_name, "->", two_name, "->", tree_name, "->", four_nema)
                        print(sum_start, "------>", sum_end, "  %", pro)

# sell red это мы покупаем 1 ETH
# buy green это мы продаём 1 ETH
