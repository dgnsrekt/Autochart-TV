from pathlib import Path
import sys

newpath = Path(__file__).parent.parent
sys.path.insert(0, str(newpath))

from autochart_tv.manager import ACManager
import requests

from time import sleep
from random import choice
from twitter_scraper import get_tweets
from collections import OrderedDict
import sys
import re

import pandas as pd

TWITTER_NAMES = 'InvestorsLive'

def get_stocks_from_twitter(twitter_name, max_tickers=9):
    tickerTweetRegex = re.compile(r'\$[^\d\s]\w*')
    tickers = list()
    for tweet in get_tweets(twitter_name, pages=5): # should be a generator somewhere.
        mo = tickerTweetRegex.findall(tweet['text'])
        if len(mo) > 0:
            clean = [ticker.replace('$', '') for ticker in mo]
            tickers += clean

    results = pd.unique(tickers)

    return list(results[:9])

with ACManager() as ACM: #TODO add var to change the title
    last = []
    while True:
        twitter = TWITTER_NAMES
        print(f'Pulling nine tickers from {twitter} tweets')
        while True:
            stocks = get_stocks_from_twitter(twitter)
            if last != stocks:
                last = stocks
                print()
                print(f'New stock found {stocks[0]}')
            ACM['CHART'].execute(*stocks)
            sleep(5)
            print('.', end='', flush=True)
