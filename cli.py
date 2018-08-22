import click
from pathlib import Path
import os

from autochart_tv.config import Configuration
from autochart_tv.server import ChartServer
from autochart_tv.repl import start_ac_repl
from autochart_tv.fomo import start_fomodd_api

config = Configuration()

@click.group()
def main():
    print('test')

@main.command('repl')
def repl():
    print('running repl') # arg to change client port here
    start_ac_repl()

@main.command('fomodd-api')
def repl():
    print('running repl') # arg to change client port here
    start_fomodd_api()

@main.command('server')
def server():
    print('running server')
    port = config.get_server_setting('port') # arg to change port here
    ChartServer.get_server().run(debug=False, port=port)


main()
