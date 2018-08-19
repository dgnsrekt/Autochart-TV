from repl import ACManager
from time import sleep
from random import choice
from twitter_scraper import get_tweets
import sys
import re

# TWITTER_NAMES = ['SeekingAlpha', 'StockTexts', 'JrwlkrT']
TWITTER_NAMES = ['SeekingAlpha']

def get_stocks_from_twitter(twitter_name):
    first_ticker_from_tweet = list()
    tickerTweetRegex = re.compile(r'\$\w*')
    for tweet in get_tweets(twitter_name, pages=1):
        mo = tickerTweetRegex.search(tweet['text'])
        if mo is not None:
            first_ticker_from_tweet.append(mo.group())
    clean = list(set([ticker.replace('$', '') for ticker in first_ticker_from_tweet]))
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
                print(stocks)
            # print(stocks)
            ACM['CHART'].execute(*stocks)
            sleep(5)
            loops +=1
            print('.', end='')
            if loops > 10:
                print()
                break
