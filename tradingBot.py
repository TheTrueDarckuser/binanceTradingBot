import requests
import json

bookTicker = requests.get('https://api.binance.com/api/v3/ticker/bookTicker').json()
Book = {}
for block in bookTicker:
    Book.update({block["symbol"]: [block["bidPrice"], block["askPrice"]]})

Info_list = requests.get('https://api.binance.com/api/v3/exchangeInfo').json()

Data = {}
for block in Info_list["symbols"]:
    if (block["status"] == "TRADING"):
        Data.update({block["baseAsset"]: {}})
        Data.update({block["quoteAsset"]: {}})

for block in Info_list["symbols"]:
    if (block["status"] == "TRADING"):
        Data[block["baseAsset"]].update({block["quoteAsset"]: float(Book[block["symbol"]][0])})
        Data[block["quoteAsset"]].update({block["baseAsset"]: 1 / (float(Book[block["symbol"]][1]))})


for one_name in Data:
    for two_name in Data[one_name]:
        for tree_name in Data[two_name]:
            for four_name in Data[tree_name]:
                if four_name == one_name:
                    sum_start = 1
                    tr_1 = Data[one_name][two_name]*sum_start
                    tr_2 = Data[two_name][tree_name]*tr_1
                    sum_end = Data[tree_name][four_name]*tr_2
                    pro = 0
                    if (sum_end>1):
                        pro = (sum_end - sum_start) * 100 / sum_end
                        if float(pro) >= 0.1:
                            print(tr_1)
                            print(tr_2)
                            print(one_name, "->", two_name, "->", tree_name, "->", four_name)
                            print(sum_start,"------>",sum_end,"  %",pro)