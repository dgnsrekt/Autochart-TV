from autochart_tv import chart

import pytest


def test_import():
    pass


@pytest.fixture
def chart_fixture():
    return chart.Chart()


def test_chart_class_default_init(chart_fixture):
    assert chart_fixture.symbol == 'BITFINEX:BTCUSD'
    assert chart_fixture.interval == 'D'
    assert chart_fixture.timezone == 'Etc/UTC'
    assert chart_fixture.theme == 'Dark'
    assert chart_fixture.barstyle == '1'


@pytest.mark.parametrize("test_input,expected", [
    ('1m', '1'),
    ('3m', '3'),
    ('5m', '5'),
    ('15m', '15'),
    ('30m', '30'),
    ('1h', '60'),
    ('2h', '120'),
    ('3h', '180'),
    ('4h', '240'),
    ('1d', 'D'),
    ('1w', 'W'),

])
def test_chart_intervals(test_input, expected):
    chart_obj = chart.Chart(interval=test_input)
    assert chart_obj.interval == expected


@pytest.mark.parametrize("test_input,expected", [
    ('Bars', '0',),
    ('Candles', '1',),
    ('Hollow_Candles', '2',),
    ('Heikin_Ashi', '3',),
    ('Line', '4',),
    ('Area', '5',),
    ('Renko', '6',),
    ('Line_Break', '7',),
    ('Kagi', '8',),
    ('Point_and_Figure', '9'),
])
def test_chart_barstyles(test_input, expected):
    chart_obj = chart.Chart(barstyle=test_input)
    assert chart_obj.barstyle == expected
