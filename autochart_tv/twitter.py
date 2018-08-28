from autochart_tv.tickergroup import TickerGroup
from autochart_tv.tools import get_peers_from_ticker
from datetime import datetime
from time import sleep

from twitter_scraper import get_tweets

import re
from functools import reduce
from lxml.etree import ParserError
from collections import OrderedDict


def get_first_tickers_from_twitter_page(name, pages=1):
    raw_tickers, all_times = [], []
    ticker_regex = re.compile(r'\$[^\d\s]\w*')

    for i, tweet in enumerate(get_tweets(name, pages=pages)):
        mo = ticker_regex.search(tweet['text'])
        if mo is not None:
            all_times.append([tweet['time']])
            raw_tickers.append(mo.group())
            break  # added this to only retrive the latests ticker
    else:
        print(f'Searched {i} of {name} tweets for stock tickers.')

    time = max(all_times)[0]
    clean_tickers = [ticker.replace('$', '') for ticker in raw_tickers]
    tickers = list(OrderedDict.fromkeys(clean_tickers))
    print(f"found {len(tickers)} tickers from {name}'s tweets.")
    return name, time, tickers


def search_twitter_profiles_for_stock_tickers(twitter_profiles, join=True):
    if isinstance(twitter_profiles, str):
        twitter_profiles = [twitter_profiles]
    TwitterTickerGroups = []
    for profile in twitter_profiles:
        try:
            name, time, tickers = get_first_tickers_from_twitter_page(profile)
            majors, minors = get_peers_from_ticker(tickers)
            TwitterTickerGroups.append(TickerGroup(name, time, majors, minors))
        except (ValueError, ParserError) as e:
            print(profile, 'error:', e)
    if join:
        # join will concat all the Ticker groups into one ordered by latest ticker
        return reduce((lambda x, y: x + y), TwitterTickerGroups)
    else:
        return TwitterTickerGroups
