import pytest

from autochart_tv import webdriver
from autochart_tv.webdriver import AutoChartWebDriver

def test_import():
    pass

def test_webdriver():
    ACWebDriver = AutoChartWebDriver()
    assert ACWebDriver.url == 'http://localhost:5000'
    ACWebDriver = AutoChartWebDriver(port=6666)
    assert ACWebDriver.url == 'http://localhost:6666'
