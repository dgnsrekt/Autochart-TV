from pathlib import Path
import sys
from time import sleep

from autochart_tv.manager import ACManager
from autochart_tv.exchange import ExchangeInterface
import requests


def start_gainers():
    with ACManager() as ACM:
        while True:
            try:
                tickers = ExchangeInterface.get_stock_top_gainers(9)
                print(tickers)
            except KeyError:
                tickers = []
            finally:
                ACM['CHART'].execute(*tickers)
                sleep(15)


def start_losers():
    with ACManager() as ACM:
        while True:
            try:
                tickers = ExchangeInterface.get_stock_top_losers(9)
            except KeyError:
                tickers = []
            finally:
                ACM['CHART'].execute(*tickers)
                sleep(15)
