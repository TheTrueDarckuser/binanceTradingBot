import requests
from binance import client as Bclient
from binance import exceptions as Bexceptions
from binance import helpers as Bhelpers
from binance import enums as Benums
from binance import depthcache as Bdepthcache
from binance import websockets as Bwebsockets

token = "JKBuzPijK5s9SIZ6wdsHKWEFbijmMEjqXZVCMnOCxlsIO7osmehLGG9autoxR3km"
secretKey = "X9ZR7PPHzpIX6lUmA7vWO5tE6KVNrpQQ5hCT3XPI4aFHDu3FVmTt0VchBFzm48YK"
# url = "https://api.binance.com"
# req = requests.get(url+"/sapi/v1/capital/config/getall")
# print(req.json())

client = Bclient.Client(api_key=token, api_secret=secretKey)
print(client.get_all_tickers()) # вывод всех монет
print(client.get_margin_account())
# print(client.get_margin_order(symbol='DOGEUSDT'))
depth = client.get_order_book(symbol='BNBBTC')
print(depth)

