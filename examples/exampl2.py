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

# TWITTER_NAMES = ['SeekingAlpha', 'StockTexts', 'JrwlkrT']
TWITTER_NAMES = ['SeekingAlpha']

def get_stocks_from_twitter(twitter_name):
    first_ticker_from_tweet = list()
    tickerTweetRegex = re.compile(r'\$\D\w*')
    for tweet in get_tweets(twitter_name, pages=1):
        mo = tickerTweetRegex.search(tweet['text'])
        if mo is not None:
            first_ticker_from_tweet.append(mo.group())
    clean = [ticker.replace('$', '') for ticker in first_ticker_from_tweet]
    clean = list(OrderedDict.fromkeys(clean))
    print(clean)
    return clean[:9]

with ACManager() as ACM:
    last = ''
    while True:
        twitter = choice(TWITTER_NAMES)
        print(f'Pulling nine tickers from {twitter} tweets')
        loops = 0
        while True:
            stocks = get_stocks_from_twitter(twitter)
            if last != stocks:
                last = stocks
                print(f'New stock found {stocks[0]}')
            # print(stocks)
            ACM['CHART'].execute(*stocks)
            sleep(5)
            loops +=1
            print('.', end='')
            if loops > 10:
                print()
                break
