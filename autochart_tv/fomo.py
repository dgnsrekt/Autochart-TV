from pathlib import Path
import sys
from time import sleep

from autochart_tv.manager import ACManager
from autochart_tv.exchange import ExchangeInterface
from autochart_tv.twitter import search_twitter_profiles_for_stock_tickers


def start_twitter_stock_search(twitter_profiles):
    with ACManager() as ACM:
        while True:
            try:
                tickers = search_twitter_profiles_for_stock_tickers(twitter_profiles)
                print(tickers)
            except KeyError:
                tickers = []
            finally:
                ACM['CHART'].execute(*tickers)
                sleep(15)


def start_fomodd_api():
    with ACManager() as ACM:
        while True:
            try:
                coins = ExchangeInterface.get_fomoddio_api_superfiltered_coins(amount=9)
            except KeyError:
                coins = []
            finally:
                ACM['CHART'].execute(*coins)
                sleep(15)


if __name__ == '__main__':
    start_fomodd_api()
