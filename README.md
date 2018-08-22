# autochart-tv
Automate Tradingview chart widgets

## REPL example
![Alt Text](https://github.com/dgnsrekt/autochart-tv/blob/master/doc/img/autochart_repl_chart.gif)
![Alt Text](https://github.com/dgnsrekt/autochart-tv/blob/master/doc/img/autochart_repl_terminal2.gif)

## Simple example script
```
from autochart_tv.manager import ACManager

with ACManager() as ACM:
    sleep(2)
    ACM['CHART'].execute('AAPL')
    sleep(2)
    ACM['CHART'].execute('BTCUSDT', 'TSLA')
    sleep(2)
    ACM['RANDOM'].execute()
    sleep(2)
    ACM['RANDOMCRYPTO'].execute(9)
    sleep(60)
```
## Required
1. Python 3.6

2. Chrome driver
https://sites.google.com/a/chromium.org/chromedriver/downloads

3. Pipenv
https://github.com/pypa/pipenv



## Quick Start
1. Clone the repository and install dependencies.
```
git clone https://github.com/dgnsrekt/autochart-tv.git
cd autochart-tv
pipenv sync
```
2. Run autochart server.
```
pipenv shell
python3 cli.py server
```
3. Run autochart REPL or connect to Fomo Driven Development API.

Open a new terminal window.
```
cd autochart-tv
pipenv shell
python3 cli.py repl
or
python3 cli.py fomodd-api
```
