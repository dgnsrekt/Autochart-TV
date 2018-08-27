# autochart-tv
Automate Tradingview chart widgets.

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
## CommandList

Command | Descriptions|Args
--------|-------------|----------
REFRESH | Refreshes the browser.|None
EXIT | Closes the browser and ends the script.|None
CLEAR | Deletes all charts.|None
DELETE | Deletes the most recently displayed ticker.|None
CHART | Displays the chart for the ticker.| ticker
RANDOM | Generates and displays random tickers | Number of tickers. Max=9
RANDOMSTOCK | Generates and displays random stockmarket tickers | Number of tickers. Max=9
RANDOMCRYPTO | Generates and displays random crypto tickers | Number of tickers. Max=9
SCREENSHOT | Takes a screenshot of the currently displayed tickers | None

## Contact
Twitter = Telegram = 'dgnsrekt'
email dgnsrekt@pm.me
