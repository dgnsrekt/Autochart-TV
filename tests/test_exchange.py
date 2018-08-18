from autochart_tv import exchange
from autochart_tv.exchange import ExchangeInterface
import pytest

def test_import():
    pass

@pytest.fixture
def exchange_interface_fixture():
    exchange = ExchangeInterface(auto_load=False)
    exchange.crypto_tickers = ['ETCBTC', 'ZRXETH', 'ZECXMR', 'BTCUSD', 'NEOBTC']
    exchange.crypto_tickers_with_exchange = ['POLONIEX:EOSUSDT', 'POLONIEX:ETCBTC',
                                             'POLONIEX:STEEMBTC', 'POLONIEX:XBCBTC',
                                             'POLONIEX:NEOSBTC',]
    exchange.stocks = ['PSC', 'TUSDUSDT', 'CMSS', 'EEMV', 'CLLS', 'LMAT', 'CROP', 'ADAUSDT']
    return exchange


def test_all_symbols(exchange_interface_fixture):
    assert exchange_interface_fixture.all_symbols == ['PSC', 'TUSDUSDT', 'CMSS', 'EEMV', 'CLLS',
    'LMAT', 'CROP', 'ADAUSDT', 'ETCBTC', 'ZRXETH', 'ZECXMR', 'BTCUSD', 'NEOBTC','POLONIEX:EOSUSDT',
    'POLONIEX:ETCBTC', 'POLONIEX:STEEMBTC', 'POLONIEX:XBCBTC', 'POLONIEX:NEOSBTC',]

def test_all_crypto_symbols(exchange_interface_fixture):
    assert exchange_interface_fixture.all_crypto_symbols== ['ETCBTC', 'ZRXETH', 'ZECXMR', 'BTCUSD',
    'NEOBTC','POLONIEX:EOSUSDT','POLONIEX:ETCBTC', 'POLONIEX:STEEMBTC', 'POLONIEX:XBCBTC',
    'POLONIEX:NEOSBTC',]

def test_get_random_symbols_single(exchange_interface_fixture):
    assert len([exchange_interface_fixture.get_random_symbols()]) == 1

@pytest.mark.parametrize('a', [(x) for x in range(1, 9)])
def test_get_random_symbols_multiple(a, exchange_interface_fixture):
    assert len(exchange_interface_fixture.get_random_symbols(a)) == a

def test_get_random_stock_single(exchange_interface_fixture):
    assert len([exchange_interface_fixture.get_random_stock()]) == 1

@pytest.mark.parametrize('a', [(x) for x in range(1, 9)])
def test_get_random_stock_multiple(a, exchange_interface_fixture):
    assert len(exchange_interface_fixture.get_random_stock(a)) == a


def test_get_random_crypto_single(exchange_interface_fixture):
    assert len([exchange_interface_fixture.get_random_crypto()]) == 1

@pytest.mark.parametrize('a', [(x) for x in range(1, 9)])
def test_get_random_crypto_multiple(a, exchange_interface_fixture):
    assert len(exchange_interface_fixture.get_random_crypto(a)) == a
