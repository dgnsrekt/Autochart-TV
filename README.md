# autochart-tv
automated tradingview widget viewer

Basic Idea
![Alt Text](https://github.com/dgnsrekt/autochart-tv/blob/master/doc/img/autochart1.gif)
![Alt Text](https://github.com/dgnsrekt/autochart-tv/blob/master/doc/img/autochart2.gif)

## Install Chromedriver
Install chrome driver.
https://sites.google.com/a/chromium.org/chromedriver/downloads

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
'''
