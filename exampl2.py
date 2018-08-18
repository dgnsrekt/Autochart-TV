from repl import ACManager
from time import sleep
import requests

def get_coins():
    url = 'https://api.fomodd.io/superfilter'
    r = requests.get(url)
    data = r.json()
    binance = data['BINANCE']['coins']
    binance = [f'BINANCE:{coin}' for coin in binance]
    bittrex = data['BITTREX']['coins']
    bittrex = [f'BITTREX:{coin}' for coin in bittrex]

    coins = binance + bittrex
    return coins

with ACManager() as ACM:
    while True:
        ACM['CHART'].execute(*get_coins())
        sleep(15)
