# system
from collections import deque
import json
from pathlib import Path
from random import choice, choices
import time

# thirdparty
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter # maynot need this
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.formatted_text import HTML

from fuzzyfinder import fuzzyfinder
import click

from selenium import webdriver
from selenium.common.exceptions import WebDriverException

import sys

# local
from autochart_tv.model import ChartModel, db
from autochart_tv.exchange import ExchangeInterface



#check 4 chromedriver also check if server is running

print('loading exchange autocomoplete data...') #initallizing blah

active_symbol_interface = ExchangeInterface()

commands = ['EXIT', 'QUIT', 'DELETE', 'CLEAR', 'RANDOM', 'RANDOM_CRYPTO']

# words = stocks + list(set(crypto)) + crypto_with_exchange + commands

url = 'http://localhost:5000'

class AutoChartCompleter(Completer):
    def get_completions(self, document, complete_event):
        word_before_cursor = document.get_word_before_cursor(WORD=True)
        matches = fuzzyfinder(word_before_cursor, words)
        for m in matches:
            yield Completion(m, start_position=-len(word_before_cursor))

class MyChrome(webdriver.Chrome):
    def quit(self):
        webdriver.Chrome.quit(self)
        self.session_id = None


driver = MyChrome()
driver.get(url)  # tested in combination with scrapy

# KEY BINDINGS
bindings = KeyBindings()

@bindings.add('c-z')
def _(event):
    def print_hello():
        ChartModel.delete_last()
        driver.refresh()
    run_in_terminal(print_hello)


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
