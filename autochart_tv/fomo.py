from pathlib import Path
import sys
from time import sleep

from autochart_tv.manager import ACManager
from autochart_tv.exchange import ExchangeInterface


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
