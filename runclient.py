# system
from collections import deque
import json
from pathlib import Path
import time

# thirdparty
import iexfinance
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.history import FileHistory
from selenium import webdriver
from selenium.common.exceptions import WebDriverException

import sys
import pandas as pd
import ccxt

#check 4 chromedriver also check if server is running
print('loading exchange autocomoplete data...') #initallizing blah
crypto_exchanges = ['binance', 'bitfinex', 'bittrex', 'poloniex']
crypto = list()
crypto_with_exchange = list()
# notify which exchange is being downloaded symbols
for exchange__ in crypto_exchanges:
    try:
        assert exchange__ in ccxt.exchanges
        exchange = getattr(ccxt, exchange__)()
        markets = exchange.load_markets()
        coins = list(markets.keys())
        coins = [coin.replace('/', '').upper() for coin in coins]
        processsed = [f"{exchange__.upper()}:{coin}" for coin in coins]

        crypto += coins
        crypto_with_exchange += processsed
        print('.', end='')

    except AssertionError:
        raise Exception(f'{exchange} exchange doesnt exist.')

df = pd.DataFrame(iexfinance.get_available_symbols())
stocks = list(df[df.isEnabled == True]['symbol'])
print('.')
print('loaded')

commands = ['EXIT', 'QUIT', 'DELETE', 'RANDOM']
words = stocks + list(set(crypto)) + crypto_with_exchange + commands
url = 'http://localhost:5000'


tv_wordcompleter = WordCompleter(words, ignore_case=True)

# CHECK IF FILE EXISTS, IF JSON EXISTS LOAD, ELSE CREATE A NEW ONE
tickers = deque(maxlen=9)
tickers.append('BITTREX:BTCUSDT')


class MyChrome(webdriver.Chrome):
    def quit(self):
        webdriver.Chrome.quit(self)
        self.session_id = None


from autochart_tv.model import ChartModel, db
import sys
from random import choice

driver = MyChrome()
driver.get(url)  # tested in combination with scrapy

# KEY BINDINGS
from prompt_toolkit.application import run_in_terminal
from prompt_toolkit.key_binding import KeyBindings

bindings = KeyBindings()

@bindings.add('c-z')
def _(event):
    def print_hello():
        ChartModel.delete_last()
        driver.refresh()
    run_in_terminal(print_hello)


while True:
    inp = prompt('> ',
                 completer=tv_wordcompleter, complete_while_typing=True, history=FileHistory('history.txt'), key_bindings=bindings)
    # run_in_terminal(print(inp))
    print(driver.session_id)
    if inp.upper() == 'EXIT' or inp.upper() == 'QUIT':
        driver.quit()
        break

    if inp.upper() == 'RANDOM':
        inp = choice(words)
        print(inp)

    if inp.upper() == 'DELETE':
        ChartModel.delete_last()
        driver.refresh()
        continue

    if ChartModel.add(inp):
        try:
            driver.refresh()
        except WebDriverException:
            print('Browser is closed.')
            break
    # tickers.appendleft(inp)
    # write(tickers)
    # add exit
    # add close browser on exit
