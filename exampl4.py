from repl import ACManager
from time import sleep
from random import choice
from twitter_scraper import get_tweets
from collections import OrderedDict
import sys
import re

TWITTER_NAMES = ['AT09_Trader']

def get_stocks_from_twitter(twitter_name):
    first_ticker_from_tweet = list()
    tickerTweetRegex = re.compile(r'\$[^\d\s]\w*')
    for tweet in get_tweets(twitter_name, pages=5): # should be a generator somewhere.
        mo = tickerTweetRegex.search(tweet['text'])
        if mo is not None:
            first_ticker_from_tweet.append(mo.group())
    clean = [ticker.replace('$', '') for ticker in first_ticker_from_tweet]
    clean = list(OrderedDict.fromkeys(clean))
    return clean[:9]

# get_stocks_from_twitter(TWITTER_NAMES[0])
#
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
