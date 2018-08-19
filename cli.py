import click
from pathlib import Path
import os

from autochart_tv.config import Configuration
from autochart_tv.server import ChartServer
from autochart_tv.repl import start_ac_repl

config = Configuration()

@click.group()
def main():
    print('test')

@main.command('repl')
def repl():
    print('running repl')
    start_ac_repl()

@main.command('server')
def server():
    print('running server')
    port = config.get_server_setting('port')
    ChartServer.get_server().run(debug=False, port=port)


main()
