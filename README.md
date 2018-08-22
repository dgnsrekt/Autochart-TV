# autochart-tv
automated tradingview widget viewer

Basic Idea
![Alt Text](https://github.com/dgnsrekt/autochart-tv/blob/master/doc/img/autochart_repl_chart.gif)
![Alt Text](https://github.com/dgnsrekt/autochart-tv/blob/master/doc/img/autochart_repl_termainal.gif)

## Required
1. Python 3.6

2. Chrome driver.
https://sites.google.com/a/chromium.org/chromedriver/downloads

3. Pipenv
https://github.com/pypa/pipenv



## Quick Start
1. Clone the repository and install dependencies.
```
git clone https://github.com/dgnsrekt/autochart-tv.git
cd autochart_tv
pipenv sync
```
2. Run autochart server.
```
pipenv shell
python3 cli.py server
```
3. Run autochart repl or Fomo Driven Development api.
open new a new terminal window.
```
cd autochart_tv
pipenv shell
python3 cli.py repl
or
python3 cli.py fomodd-api.py
```
