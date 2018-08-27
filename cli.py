import click
from pathlib import Path
import os

from autochart_tv.config import Configuration
from autochart_tv.server import ChartServer
from autochart_tv.repl import start_ac_repl
from autochart_tv.fomo import start_fomodd_api
from autochart_tv.top import start_gainers, start_losers

config = Configuration()


@click.group()
def main():
    print('test')


@main.command('repl')
def repl():
    print('running repl')  # arg to change client port here
    start_ac_repl()


@main.command('fomodd-api')
def fomodd():
    print('running api.fomodd.io/superfiler')  # arg to change client port here
    print('Helps filter then shit from the shitcoins.')
    start_fomodd_api()


@main.command('iex-stock-gainers')
def gainers():
    print('running tops gainers from iex')  # arg to change client port here
    start_gainers()


@main.command('iex-stock-losers')
def losers():
    print('running tops losers from iex')  # arg to change client port here
    start_losers()


@main.command('server')
def server():
    print('running server')
    port = config.get_server_setting('port')  # arg to change port here
    ChartServer.get_server().run(debug=False, port=port)


main()
