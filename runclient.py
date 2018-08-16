# system
from collections import deque
import json
from pathlib import Path
import time

# thirdparty
import iexfinance
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter # maynot need this
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.completion import Completer, Completion

from fuzzyfinder import fuzzyfinder

from selenium import webdriver
from selenium.common.exceptions import WebDriverException

import sys
import pandas as pd
import ccxt

#check 4 chromedriver also check if server is running
print('loading exchange autocomoplete data...') #initallizing blah
crypto_exchanges = ['binance', 'bittrex', 'poloniex']
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

commands = ['EXIT', 'QUIT', 'DELETE', 'RANDOM', 'CLEAR', 'FULL_RANDOM', 'FULL_RANDOM_CRYPTO']
crypto = list(set(crypto))
words = stocks + list(set(crypto)) + crypto_with_exchange + commands
url = 'http://localhost:5000'

class AutoChartCompleter(Completer):
    def get_completions(self, document, complete_event):
        word_before_cursor = document.get_word_before_cursor(WORD=True)
        matches = fuzzyfinder(word_before_cursor, words)
        for m in matches:
            yield Completion(m, start_position=-len(word_before_cursor))

tv_wordcompleter = WordCompleter(words, ignore_case=True)

class MyChrome(webdriver.Chrome):
    def quit(self):
        webdriver.Chrome.quit(self)
        self.session_id = None


from autochart_tv.model import ChartModel, db
import sys
from random import choice, choices

driver = MyChrome()
driver.get(url)  # tested in combination with scrapy

# KEY BINDINGS
from prompt_toolkit.application import run_in_terminal
from prompt_toolkit.key_binding import KeyBindings
import click

bindings = KeyBindings()

@bindings.add('c-z')
def _(event):
    def print_hello():
        ChartModel.delete_last()
        driver.refresh()
    run_in_terminal(print_hello)

from prompt_toolkit import prompt
from prompt_toolkit.formatted_text import HTML

def bottom_toolbar():
    return HTML('This is a <b><style bg="ansired">Toolbar</style></b>!')

class InvalidEntryError(Exception):
    pass
    
while True:
    inp = prompt('> ',
                 completer=AutoChartCompleter(), complete_while_typing=True, history=FileHistory('history.txt'), key_bindings=bindings, bottom_toolbar=bottom_toolbar)
    print(inp)
    print(type(inp))
    print(driver.session_id)
    if inp.upper() == 'EXIT' or inp.upper() == 'QUIT':
        driver.quit()
        break

    if inp.upper() == 'RANDOM': # dont let this full threw use own update and continue
        inp = choice(words)
        print(inp)

    if inp.upper() == 'FULL_RANDOM':
        inp = choices(words, k=9)
        for tick in inp:
            ChartModel.add(tick)
        driver.refresh()
        continue

    if inp.upper() == 'FULL_RANDOM_CRYPTO':
        inp = choices(crypto + crypto_with_exchange, k=9)
        for tick in inp:
            ChartModel.add(tick)
        driver.refresh()
        continue


    if inp.upper() == 'DELETE':
        ChartModel.delete_last()
        driver.refresh()
        continue

    if inp.upper() == 'CLEAR':
        ChartModel.clear_all()
        driver.refresh()
        continue

    if ChartModel.add(inp):
        try:
            driver.refresh()
        except WebDriverException: #TODO REFACTOR to check instead and exit if is is clsd own section in loop
            print('Browser is closed.')
            break
